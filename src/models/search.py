"""Search-related data models."""

from typing import Any, Optional

from pydantic import BaseModel, Field


class SearchResult(BaseModel):
    """A single search result from vector database."""

    chunk_id: str = Field(description="Chunk identifier")
    document_id: str = Field(description="Source document ID")
    content: str = Field(description="Chunk content")
    score: float = Field(description="Similarity score (0-1)")
    metadata: dict[str, Any] = Field(
        default_factory=dict,
        description="Chunk metadata",
    )
    document_metadata: Optional[dict[str, Any]] = Field(
        None, description="Parent document metadata"
    )
