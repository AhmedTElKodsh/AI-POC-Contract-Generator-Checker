"""Document Ingestion Module for parsing PDF and DOCX documents."""

from src.ingestion.exceptions import (
    CorruptedFileError,
    DocumentIngestionError,
    OCRFailureError,
    UnsupportedFormatError,
)
from src.ingestion.module import DocumentIngestionModule

__all__ = [
    "DocumentIngestionModule",
    "DocumentIngestionError",
    "CorruptedFileError",
    "UnsupportedFormatError",
    "OCRFailureError",
]
