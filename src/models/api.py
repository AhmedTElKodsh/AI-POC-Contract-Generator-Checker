"""API request/response models."""

from datetime import datetime
from typing import Any, Generic, Optional, TypeVar

from pydantic import BaseModel, Field

from src.models.enums import JobStatus

T = TypeVar("T")


class APIResponse(BaseModel, Generic[T]):
    """Generic API response wrapper."""

    success: bool = Field(description="Whether request was successful")
    data: Optional[T] = Field(None, description="Response data")
    message: Optional[str] = Field(None, description="Response message")
    error: Optional[str] = Field(None, description="Error message if failed")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Response timestamp")


class AsyncJob(BaseModel):
    """Async job status."""

    job_id: str = Field(description="Job identifier")
    status: JobStatus = Field(description="Job status")
    progress_percent: float = Field(default=0.0, ge=0.0, le=100.0, description="Progress (0-100)")
    message: Optional[str] = Field(None, description="Status message")
    result: Optional[dict[str, Any]] = Field(None, description="Job result (when completed)")
    error: Optional[str] = Field(None, description="Error message (when failed)")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Job creation time")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="Last update time")
    completed_at: Optional[datetime] = Field(None, description="Completion time")
