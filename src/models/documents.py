"""Document-related data models."""

from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, Field

from src.models.enums import (
    DocumentType,
    EngineeringDiscipline,
    Language,
    ProjectType,
    SectionType,
)


class TableData(BaseModel):
    """Represents a table extracted from a document."""

    headers: list[str] = Field(description="Table column headers")
    rows: list[list[str]] = Field(description="Table rows")
    caption: Optional[str] = Field(None, description="Table caption/title")
    page_number: Optional[int] = Field(None, description="Page number where table appears")


class DocumentSection(BaseModel):
    """Represents a section within a document."""

    section_type: SectionType = Field(description="Type of section")
    title: str = Field(description="Section title")
    content: str = Field(description="Section text content")
    subsections: list["DocumentSection"] = Field(
        default_factory=list, description="Nested subsections"
    )
    tables: list[TableData] = Field(default_factory=list, description="Tables in this section")
    page_start: Optional[int] = Field(None, description="Starting page number")
    page_end: Optional[int] = Field(None, description="Ending page number")


class DocumentMetadata(BaseModel):
    """Metadata for an engineering document."""

    document_id: str = Field(description="Unique document identifier")
    filename: str = Field(description="Original filename")
    document_type: DocumentType = Field(description="Type of document")
    language: Language = Field(description="Primary language")
    discipline: Optional[EngineeringDiscipline] = Field(
        None, description="Engineering discipline"
    )
    project_type: Optional[ProjectType] = Field(None, description="Project type")
    project_name: Optional[str] = Field(None, description="Project name")
    client: Optional[str] = Field(None, description="Client name")
    location: Optional[str] = Field(None, description="Project location")
    date: Optional[datetime] = Field(None, description="Document date")
    author: Optional[str] = Field(None, description="Document author")
    total_pages: Optional[int] = Field(None, description="Total page count")
    total_cost: Optional[float] = Field(None, description="Total project cost (if applicable)")
    currency: Optional[str] = Field("EGP", description="Currency code")
    tags: list[str] = Field(default_factory=list, description="Custom tags")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Ingestion timestamp")


class ParsedDocument(BaseModel):
    """Complete parsed document with content and metadata."""

    metadata: DocumentMetadata = Field(description="Document metadata")
    sections: list[DocumentSection] = Field(description="Document sections")
    raw_text: str = Field(description="Full raw text content")
    markdown: Optional[str] = Field(None, description="Markdown representation")


class IndexedChunk(BaseModel):
    """A chunk of document content indexed in vector database."""

    chunk_id: str = Field(description="Unique chunk identifier")
    document_id: str = Field(description="Parent document ID")
    content: str = Field(description="Chunk text content")
    embedding: Optional[list[float]] = Field(None, description="Vector embedding")
    metadata: dict[str, Any] = Field(
        default_factory=dict,
        description="Chunk metadata (section, page, etc.)",
    )
    start_char: int = Field(description="Start character position in document")
    end_char: int = Field(description="End character position in document")


# Enable forward references
DocumentSection.model_rebuild()
