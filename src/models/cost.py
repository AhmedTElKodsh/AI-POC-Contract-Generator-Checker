"""Cost estimation data models."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class CostItem(BaseModel):
    """A cost item from historical data."""

    item_id: str = Field(description="Unique item identifier")
    description: str = Field(description="Item description")
    unit: str = Field(description="Unit of measurement")
    unit_rate: float = Field(description="Unit rate in currency")
    currency: str = Field(default="EGP", description="Currency code")
    source_document_id: str = Field(description="Source document ID")
    project_type: Optional[str] = Field(None, description="Project type")
    date: datetime = Field(description="Date of cost data")
    location: Optional[str] = Field(None, description="Project location")
    notes: Optional[str] = Field(None, description="Additional notes")


class CostEstimate(BaseModel):
    """Cost estimate for a project."""

    project_name: str = Field(description="Project name")
    items: list["BOQItem"] = Field(description="Cost items")
    subtotal: float = Field(description="Subtotal cost")
    contingency_percent: float = Field(default=10.0, description="Contingency percentage")
    contingency_amount: float = Field(description="Contingency amount")
    total: float = Field(description="Total cost including contingency")
    currency: str = Field(default="EGP", description="Currency code")
    inflation_adjusted: bool = Field(
        default=False, description="Whether costs are inflation-adjusted"
    )
    base_date: Optional[datetime] = Field(None, description="Base date for inflation adjustment")
    created_at: datetime = Field(default_factory=datetime.utcnow)


# Import BOQItem to avoid circular dependency
from src.models.generation import BOQItem  # noqa: E402

CostEstimate.model_rebuild()
