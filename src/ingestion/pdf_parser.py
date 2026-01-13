"""PDF document parser using pymupdf4llm."""

import os
from pathlib import Path
from typing import Any, Optional

from src.ingestion.exceptions import CorruptedFileError, UnsupportedFormatError
from src.ingestion.language_detector import LanguageDetector
from src.ingestion.table_extractor import TableExtractor
from src.models.documents import DocumentMetadata, DocumentSection, ParsedDocument, TableData
from src.models.enums import DocumentType, Language, SectionType


class PDFParser:
    """Parse PDF documents and extract structured content."""

    def __init__(self):
        """Initialize the PDF parser."""
        self.language_detector = LanguageDetector()
        self.table_extractor = TableExtractor()
        self._pymupdf4llm = None
        self._pymupdf = None
        self._load_dependencies()

    def _load_dependencies(self):
        """Load optional dependencies."""
        try:
            import pymupdf4llm
            self._pymupdf4llm = pymupdf4llm
        except ImportError:
            pass

        try:
            import pymupdf
            self._pymupdf = pymupdf
        except ImportError:
            try:
                import fitz as pymupdf
                self._pymupdf = pymupdf
            except ImportError:
                pass

    def parse(self, file_path: str) -> ParsedDocument:
        """
        Parse a PDF document and extract structured content.

        Args:
            file_path: Path to the PDF file

        Returns:
            ParsedDocument with extracted content

        Raises:
            UnsupportedFormatError: If file is not a PDF
            CorruptedFileError: If file cannot be parsed
        """
        path = Path(file_path)

        # Validate file exists and is PDF
        if not path.exists():
            raise CorruptedFileError(file_path, "File does not exist")

        if path.suffix.lower() != ".pdf":
            raise UnsupportedFormatError(file_path, path.suffix)

        try:
            # Extract content using pymupdf4llm
            markdown_text, page_data = self._extract_with_pymupdf4llm(file_path)

            # Detect primary language
            primary_language = self.language_detector.detect(markdown_text)

            # Extract tables from markdown
            tables = self.table_extractor.extract_from_markdown(markdown_text)

            # Parse sections from markdown
            sections = self._parse_sections(markdown_text, primary_language)

            # Get page count
            page_count = len(page_data) if page_data else self._get_page_count(file_path)

            # Create metadata
            metadata = DocumentMetadata(
                document_id="",  # Will be set by caller
                filename=path.name,
                document_type=DocumentType.PDF,
                language=primary_language,
                total_pages=page_count,
            )

            return ParsedDocument(
                metadata=metadata,
                sections=sections,
                raw_text=markdown_text,
                markdown=markdown_text,
            )

        except Exception as e:
            if isinstance(e, (CorruptedFileError, UnsupportedFormatError)):
                raise
            raise CorruptedFileError(file_path, str(e))


    def _extract_with_pymupdf4llm(
        self, file_path: str
    ) -> tuple[str, Optional[list[dict[str, Any]]]]:
        """Extract content using pymupdf4llm."""
        if self._pymupdf4llm is None:
            # Fallback to basic extraction
            return self._extract_basic(file_path), None

        try:
            # Extract with page chunks for better structure
            page_data = self._pymupdf4llm.to_markdown(
                doc=file_path,
                page_chunks=True,
                show_progress=False,
            )

            # Combine all pages into single markdown
            if isinstance(page_data, list):
                markdown_parts = []
                for page in page_data:
                    if isinstance(page, dict) and "text" in page:
                        markdown_parts.append(page["text"])
                    elif isinstance(page, str):
                        markdown_parts.append(page)
                markdown_text = "\n\n".join(markdown_parts)
                return markdown_text, page_data
            else:
                return str(page_data), None

        except Exception as e:
            # Fallback to basic extraction on error
            return self._extract_basic(file_path), None

    def _extract_basic(self, file_path: str) -> str:
        """Basic text extraction fallback using PyMuPDF."""
        if self._pymupdf is None:
            raise CorruptedFileError(
                file_path, "Neither pymupdf4llm nor pymupdf is available"
            )

        try:
            doc = self._pymupdf.open(file_path)
            text_parts = []
            for page in doc:
                text_parts.append(page.get_text())
            doc.close()
            return "\n\n".join(text_parts)
        except Exception as e:
            raise CorruptedFileError(file_path, f"PyMuPDF extraction failed: {e}")

    def _get_page_count(self, file_path: str) -> int:
        """Get page count from PDF."""
        if self._pymupdf is None:
            return 0

        try:
            doc = self._pymupdf.open(file_path)
            count = len(doc)
            doc.close()
            return count
        except Exception:
            return 0

    def _parse_sections(
        self, markdown_text: str, primary_language: Language
    ) -> list[DocumentSection]:
        """Parse markdown text into document sections."""
        sections = []
        lines = markdown_text.split("\n")
        current_section = None
        current_content = []

        for line in lines:
            # Check for headers (# Header, ## Header, etc.)
            if line.startswith("#"):
                # Save previous section
                if current_section:
                    current_section.content = "\n".join(current_content).strip()
                    sections.append(current_section)
                    current_content = []

                # Determine header level
                level = 0
                for char in line:
                    if char == "#":
                        level += 1
                    else:
                        break

                title = line[level:].strip()
                section_type = self._detect_section_type(title)

                current_section = DocumentSection(
                    section_type=section_type,
                    title=title,
                    content="",
                    subsections=[],
                    tables=[],
                    page_start=None,
                    page_end=None,
                )
            else:
                current_content.append(line)

        # Save last section
        if current_section:
            current_section.content = "\n".join(current_content).strip()
            sections.append(current_section)
        elif current_content:
            # No headers found, create single section
            sections.append(
                DocumentSection(
                    section_type=SectionType.OTHER,
                    title="Content",
                    content="\n".join(current_content).strip(),
                    subsections=[],
                    tables=[],
                    page_start=None,
                    page_end=None,
                )
            )

        return sections

    def _detect_section_type(self, title: str) -> SectionType:
        """Detect section type from title."""
        title_lower = title.lower()

        # English patterns
        patterns = {
            SectionType.EXECUTIVE_SUMMARY: ["executive summary", "summary", "abstract", "ملخص"],
            SectionType.INTRODUCTION: ["introduction", "background", "مقدمة"],
            SectionType.SCOPE_OF_WORK: ["scope", "scope of work", "نطاق العمل"],
            SectionType.METHODOLOGY: ["methodology", "approach", "method", "المنهجية"],
            SectionType.TECHNICAL_APPROACH: ["technical", "technical approach", "النهج الفني"],
            SectionType.TIMELINE: ["timeline", "schedule", "الجدول الزمني"],
            SectionType.TEAM_COMPOSITION: ["team", "personnel", "staff", "فريق العمل"],
            SectionType.DELIVERABLES: ["deliverables", "outputs", "المخرجات"],
            SectionType.COST_ESTIMATE: ["cost", "budget", "pricing", "التكلفة"],
            SectionType.BOQ: ["boq", "bill of quantities", "جدول الكميات"],
            SectionType.TERMS_AND_CONDITIONS: ["terms", "conditions", "الشروط"],
            SectionType.APPENDIX: ["appendix", "annex", "الملحق"],
            SectionType.REFERENCES: ["references", "bibliography", "المراجع"],
            SectionType.CONCLUSIONS: ["conclusion", "الخلاصة"],
            SectionType.RECOMMENDATIONS: ["recommendation", "التوصيات"],
        }

        for section_type, keywords in patterns.items():
            for keyword in keywords:
                if keyword in title_lower:
                    return section_type

        return SectionType.OTHER
