"""Custom exceptions for document ingestion."""

from typing import Optional


class DocumentIngestionError(Exception):
    """Base exception for document ingestion errors."""

    def __init__(self, message: str, file_path: Optional[str] = None):
        self.message = message
        self.file_path = file_path
        super().__init__(self.message)


class CorruptedFileError(DocumentIngestionError):
    """Raised when a document file is corrupted or unreadable."""

    def __init__(self, file_path: str, details: Optional[str] = None):
        message = f"File is corrupted or unreadable: {file_path}"
        if details:
            message += f" - {details}"
        super().__init__(message, file_path)
        self.details = details


class UnsupportedFormatError(DocumentIngestionError):
    """Raised when document format is not supported."""

    SUPPORTED_FORMATS = ["pdf", "docx"]

    def __init__(self, file_path: str, detected_format: Optional[str] = None):
        message = f"Unsupported file format: {file_path}"
        if detected_format:
            message += f" (detected: {detected_format})"
        message += f". Supported formats: {', '.join(self.SUPPORTED_FORMATS)}"
        super().__init__(message, file_path)
        self.detected_format = detected_format


class OCRFailureError(DocumentIngestionError):
    """Raised when OCR processing fails."""

    def __init__(self, file_path: str, details: Optional[str] = None):
        message = f"OCR processing failed for: {file_path}"
        if details:
            message += f" - {details}"
        super().__init__(message, file_path)
        self.details = details


class EncodingError(DocumentIngestionError):
    """Raised when character encoding issues occur."""

    def __init__(self, file_path: str, encoding: Optional[str] = None):
        message = f"Character encoding error in: {file_path}"
        if encoding:
            message += f" (attempted encoding: {encoding})"
        super().__init__(message, file_path)
        self.encoding = encoding
