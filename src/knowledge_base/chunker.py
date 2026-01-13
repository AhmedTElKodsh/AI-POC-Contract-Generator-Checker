"""Document chunking for knowledge base indexing."""

import re
import uuid
from typing import Optional

from src.models.documents import DocumentSection, IndexedChunk, ParsedDocument
from src.models.enums import Language


class DocumentChunker:
    """
    Split documents into chunks for vector indexing.

    Supports semantic chunking based on document structure,
    with configurable chunk sizes and overlap.
    """

    DEFAULT_CHUNK_SIZE = 500
    DEFAULT_OVERLAP = 50
    MIN_CHUNK_SIZE = 100

    def __init__(
        self,
        chunk_size: int = DEFAULT_CHUNK_SIZE,
        overlap: int = DEFAULT_OVERLAP,
    ):
        """
        Initialize the document chunker.

        Args:
            chunk_size: Target chunk size in characters
            overlap: Overlap between chunks in characters
        """
        self.chunk_size = max(chunk_size, self.MIN_CHUNK_SIZE)
        self.overlap = min(overlap, chunk_size // 2)

    def chunk_document(self, document: ParsedDocument) -> list[IndexedChunk]:
        """
        Split a parsed document into indexed chunks.

        Args:
            document: Parsed document to chunk

        Returns:
            List of IndexedChunk objects
        """
        chunks = []
        char_offset = 0

        # Process each section
        for section in document.sections:
            section_chunks = self._chunk_section(
                section=section,
                document_id=document.metadata.document_id,
                char_offset=char_offset,
                language=document.metadata.language,
            )
            chunks.extend(section_chunks)

            # Update character offset
            section_text = f"{section.title}\n{section.content}"
            char_offset += len(section_text)

        # If no sections, chunk raw text
        if not chunks and document.raw_text:
            chunks = self._chunk_text(
                text=document.raw_text,
                document_id=document.metadata.document_id,
                section_type="content",
                language=document.metadata.language,
            )

        return chunks

    def _chunk_section(
        self,
        section: DocumentSection,
        document_id: str,
        char_offset: int,
        language: Language,
    ) -> list[IndexedChunk]:
        """Chunk a single document section."""
        chunks = []

        # Combine title and content
        section_text = f"{section.title}\n\n{section.content}"

        # If section is small enough, keep as single chunk
        if len(section_text) <= self.chunk_size:
            chunk = IndexedChunk(
                chunk_id=str(uuid.uuid4()),
                document_id=document_id,
                content=section_text.strip(),
                embedding=None,
                metadata={
                    "section_type": section.section_type.value,
                    "section_title": section.title,
                    "language": language.value,
                },
                start_char=char_offset,
                end_char=char_offset + len(section_text),
            )
            chunks.append(chunk)
        else:
            # Split into multiple chunks
            text_chunks = self._split_text(section_text)
            current_offset = char_offset

            for i, text in enumerate(text_chunks):
                chunk = IndexedChunk(
                    chunk_id=str(uuid.uuid4()),
                    document_id=document_id,
                    content=text.strip(),
                    embedding=None,
                    metadata={
                        "section_type": section.section_type.value,
                        "section_title": section.title,
                        "chunk_index": i,
                        "language": language.value,
                    },
                    start_char=current_offset,
                    end_char=current_offset + len(text),
                )
                chunks.append(chunk)
                current_offset += len(text) - self.overlap

        return chunks


    def _chunk_text(
        self,
        text: str,
        document_id: str,
        section_type: str,
        language: Language,
    ) -> list[IndexedChunk]:
        """Chunk plain text without section structure."""
        chunks = []
        text_chunks = self._split_text(text)
        current_offset = 0

        for i, chunk_text in enumerate(text_chunks):
            chunk = IndexedChunk(
                chunk_id=str(uuid.uuid4()),
                document_id=document_id,
                content=chunk_text.strip(),
                embedding=None,
                metadata={
                    "section_type": section_type,
                    "chunk_index": i,
                    "language": language.value,
                },
                start_char=current_offset,
                end_char=current_offset + len(chunk_text),
            )
            chunks.append(chunk)
            current_offset += len(chunk_text) - self.overlap

        return chunks

    def _split_text(self, text: str) -> list[str]:
        """Split text into chunks respecting sentence boundaries."""
        if len(text) <= self.chunk_size:
            return [text]

        chunks = []
        start = 0

        while start < len(text):
            end = start + self.chunk_size

            if end >= len(text):
                # Last chunk
                chunks.append(text[start:])
                break

            # Try to find sentence boundary
            best_break = self._find_sentence_break(text, start, end)

            if best_break > start:
                chunks.append(text[start:best_break])
                start = best_break - self.overlap
            else:
                # No good break found, use word boundary
                word_break = self._find_word_break(text, start, end)
                chunks.append(text[start:word_break])
                start = word_break - self.overlap

            # Ensure we make progress
            if start <= 0:
                start = end - self.overlap

        return [c for c in chunks if c.strip()]

    def _find_sentence_break(self, text: str, start: int, end: int) -> int:
        """Find the best sentence break point."""
        # Sentence endings
        sentence_endings = [".", "!", "?", "。", "！", "？", "\n\n"]

        best_break = start
        for ending in sentence_endings:
            pos = text.rfind(ending, start, end)
            if pos > best_break:
                best_break = pos + len(ending)

        return best_break

    def _find_word_break(self, text: str, start: int, end: int) -> int:
        """Find the best word break point."""
        # Look for whitespace
        pos = text.rfind(" ", start, end)
        if pos > start:
            return pos + 1

        # Arabic word boundaries
        pos = text.rfind("\u0020", start, end)  # Arabic space
        if pos > start:
            return pos + 1

        return end

    def rechunk(
        self,
        chunks: list[IndexedChunk],
        new_chunk_size: Optional[int] = None,
        new_overlap: Optional[int] = None,
    ) -> list[IndexedChunk]:
        """
        Re-chunk existing chunks with new parameters.

        Args:
            chunks: Existing chunks to re-chunk
            new_chunk_size: New chunk size (uses current if None)
            new_overlap: New overlap (uses current if None)

        Returns:
            New list of chunks
        """
        if new_chunk_size:
            self.chunk_size = max(new_chunk_size, self.MIN_CHUNK_SIZE)
        if new_overlap:
            self.overlap = min(new_overlap, self.chunk_size // 2)

        # Combine all chunks back into text
        combined_text = " ".join(c.content for c in chunks)

        # Get document_id from first chunk
        document_id = chunks[0].document_id if chunks else ""
        language = Language(chunks[0].metadata.get("language", "en")) if chunks else Language.ENGLISH

        return self._chunk_text(combined_text, document_id, "content", language)
