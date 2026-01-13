"""Main Document Ingestion Module."""

import uuid
from pathlib import Path
from typing import Optional

from src.ingestion.docx_parser import DOCXParser
from src.ingestion.exceptions import CorruptedFileError, UnsupportedFormatError
from src.ingestion.language_detector import LanguageDetector
from src.ingestion.pdf_parser import PDFParser
from src.ingestion.table_extractor import TableExtractor
from src.models.documents import DocumentMetadata, ParsedDocument, TableData
from src.models.enums import DocumentType, Language


class DocumentIngestionModule:
    """
    Main module for document ingestion and parsing.

    Supports PDF and DOCX documents with Arabic/English content.
    Extracts text, tables, and document structure.
    """

    SUPPORTED_FORMATS = {".pdf": DocumentType.PDF, ".docx": DocumentType.DOCX}

    def __init__(self):
        """Initialize the document ingestion module."""
        self.pdf_parser = PDFParser()
        self.docx_parser = DOCXParser()
        self.language_detector = LanguageDetector()
        self.table_extractor = TableExtractor()

    def parse(self, file_path: str, document_id: Optional[str] = None) -> ParsedDocument:
        """
        Parse a document and extract structured content.

        Args:
            file_path: Path to the document file
            document_id: Optional document ID (generated if not provided)

        Returns:
            ParsedDocument with extracted content

        Raises:
            UnsupportedFormatError: If file format is not supported
            CorruptedFileError: If file cannot be parsed
        """
        path = Path(file_path)

        # Validate file exists
        if not path.exists():
            raise CorruptedFileError(file_path, "File does not exist")

        # Determine document type
        suffix = path.suffix.lower()
        if suffix not in self.SUPPORTED_FORMATS:
            raise UnsupportedFormatError(file_path, suffix)

        doc_type = self.SUPPORTED_FORMATS[suffix]

        # Parse based on document type
        if doc_type == DocumentType.PDF:
            parsed = self.pdf_parser.parse(file_path)
        elif doc_type == DocumentType.DOCX:
            parsed = self.docx_parser.parse(file_path)
        else:
            raise UnsupportedFormatError(file_path, suffix)

        # Set document ID
        parsed.metadata.document_id = document_id or str(uuid.uuid4())

        return parsed

    def parse_pdf(self, file_path: str, document_id: Optional[str] = None) -> ParsedDocument:
        """
        Parse a PDF document.

        Args:
            file_path: Path to the PDF file
            document_id: Optional document ID

        Returns:
            ParsedDocument with extracted content
        """
        parsed = self.pdf_parser.parse(file_path)
        parsed.metadata.document_id = document_id or str(uuid.uuid4())
        return parsed

    def parse_docx(self, file_path: str, document_id: Optional[str] = None) -> ParsedDocument:
        """
        Parse a DOCX document.

        Args:
            file_path: Path to the DOCX file
            document_id: Optional document ID

        Returns:
            ParsedDocument with extracted content
        """
        parsed = self.docx_parser.parse(file_path)
        parsed.metadata.document_id = document_id or str(uuid.uuid4())
        return parsed

    def extract_tables(self, file_path: str) -> list[TableData]:
        """
        Extract all tables from a document.

        Args:
            file_path: Path to the document

        Returns:
            List of TableData objects
        """
        parsed = self.parse(file_path)

        # Collect tables from all sections
        tables = []
        for section in parsed.sections:
            tables.extend(section.tables)

        # Also extract from markdown if available
        if parsed.markdown:
            md_tables = self.table_extractor.extract_from_markdown(parsed.markdown)
            # Avoid duplicates by checking content
            existing_headers = {tuple(t.headers) for t in tables}
            for table in md_tables:
                if tuple(table.headers) not in existing_headers:
                    tables.append(table)

        return tables

    def detect_language(self, text: str) -> Language:
        """
        Detect the primary language of text content.

        Args:
            text: Text content to analyze

        Returns:
            Language enum indicating detected language
        """
        return self.language_detector.detect(text)

    def get_supported_formats(self) -> list[str]:
        """Get list of supported file formats."""
        return list(self.SUPPORTED_FORMATS.keys())

    def is_supported(self, file_path: str) -> bool:
        """Check if a file format is supported."""
        suffix = Path(file_path).suffix.lower()
        return suffix in self.SUPPORTED_FORMATS

    def update_metadata(
        self,
        parsed_doc: ParsedDocument,
        project_type: Optional[str] = None,
        client: Optional[str] = None,
        project_name: Optional[str] = None,
        location: Optional[str] = None,
        **kwargs,
    ) -> ParsedDocument:
        """
        Update metadata of a parsed document.

        Args:
            parsed_doc: The parsed document to update
            project_type: Project type
            client: Client name
            project_name: Project name
            location: Project location
            **kwargs: Additional metadata fields

        Returns:
            Updated ParsedDocument
        """
        if project_type:
            # Convert string to enum if needed
            from src.models.enums import ProjectType
            try:
                parsed_doc.metadata.project_type = ProjectType(project_type)
            except ValueError:
                pass

        if client:
            parsed_doc.metadata.client = client
        if project_name:
            parsed_doc.metadata.project_name = project_name
        if location:
            parsed_doc.metadata.location = location

        # Handle additional fields
        for key, value in kwargs.items():
            if hasattr(parsed_doc.metadata, key):
                setattr(parsed_doc.metadata, key, value)

        return parsed_doc
