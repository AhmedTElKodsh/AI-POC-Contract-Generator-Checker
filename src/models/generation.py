"""Generation-related data models."""

from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, Field

from src.models.enums import (
    EngineeringDiscipline,
    Language,
    OutputFormat,
    ProjectType,
    SectionType,
)


class ProjectParameters(BaseModel):
    """Input parameters for proposal/report generation."""

    project_name: str = Field(description="Project name")
    client: str = Field(description="Client name")
    location: str = Field(description="Project location")
    project_type: ProjectType = Field(description="Type of project")
    discipline: EngineeringDiscipline = Field(description="Engineering discipline")
    language: Language = Field(default=Language.ARABIC, description="Output language")
    scope_description: str = Field(description="Brief scope description")
    deliverables: list[str] = Field(description="List of deliverables")
    duration_months: int = Field(description="Project duration in months")
    budget_range: Optional[str] = Field(None, description="Budget range (e.g., '1M-2M EGP')")
    special_requirements: Optional[str] = Field(None, description="Special requirements or notes")
    include_sections: list[SectionType] = Field(
        default_factory=list, description="Sections to include (empty = all)"
    )
    output_format: OutputFormat = Field(default=OutputFormat.DOCX, description="Output format")


class GeneratedSection(BaseModel):
    """A generated section of a proposal/report."""

    section_type: SectionType = Field(description="Type of section")
    title: str = Field(description="Section title")
    content: str = Field(description="Generated content")
    citations: list[str] = Field(
        default_factory=list, description="Source document citations"
    )
    confidence_score: float = Field(
        ge=0.0, le=1.0, description="Generation confidence (0-1)"
    )
    tokens_used: int = Field(description="LLM tokens consumed")


class BOQItem(BaseModel):
    """Bill of Quantities item."""

    item_number: str = Field(description="Item number (e.g., '1.1.1')")
    description: str = Field(description="Item description")
    unit: str = Field(description="Unit of measurement (e.g., 'm3', 'ton', 'lump sum')")
    quantity: float = Field(description="Quantity")
    unit_rate: float = Field(description="Unit rate in currency")
    total: float = Field(description="Total cost (quantity × unit_rate)")
    notes: Optional[str] = Field(None, description="Additional notes")


class ProposalContext(BaseModel):
    """Context data for rendering proposal template."""

    project_name: str
    client: str
    location: str
    date: datetime = Field(default_factory=datetime.utcnow)
    sections: dict[str, str] = Field(
        description="Section content keyed by section type"
    )
    boq_items: list[BOQItem] = Field(default_factory=list)
    total_cost: float = Field(default=0.0)
    currency: str = Field(default="EGP")
    duration_months: int = Field(default=6)
    team_members: list[dict[str, str]] = Field(default_factory=list)
    timeline_milestones: list[dict[str, Any]] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)


class GenerationResult(BaseModel):
    """Complete generation result."""

    job_id: str = Field(description="Job identifier")
    project_parameters: ProjectParameters = Field(description="Input parameters")
    generated_sections: list[GeneratedSection] = Field(description="Generated sections")
    boq_items: list[BOQItem] = Field(default_factory=list, description="BOQ items")
    total_cost: float = Field(default=0.0, description="Total estimated cost")
    total_tokens: int = Field(description="Total LLM tokens used")
    generation_time_seconds: float = Field(description="Generation time")
    created_at: datetime = Field(default_factory=datetime.utcnow)


class RenderResult(BaseModel):
    """Document rendering result."""

    job_id: str = Field(description="Job identifier")
    output_format: OutputFormat = Field(description="Output format")
    file_path: str = Field(description="Path to generated file")
    file_size_bytes: int = Field(description="File size in bytes")
    page_count: Optional[int] = Field(None, description="Number of pages")
    created_at: datetime = Field(default_factory=datetime.utcnow)
