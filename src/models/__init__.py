"""Data models for the AI Engine."""

from src.models.api import APIResponse, AsyncJob
from src.models.cost import CostEstimate, CostItem
from src.models.documents import (
    DocumentMetadata,
    DocumentSection,
    IndexedChunk,
    ParsedDocument,
    TableData,
)
from src.models.enums import (
    DocumentType,
    EngineeringDiscipline,
    IssueSeverity,
    JobStatus,
    Language,
    OutputFormat,
    ProjectType,
    SectionType,
    SimulationType,
)
from src.models.generation import (
    BOQItem,
    GeneratedSection,
    GenerationResult,
    ProjectParameters,
    ProposalContext,
    RenderResult,
)
from src.models.search import SearchResult
from src.models.validation import (
    DrainageParameters,
    HydrologicalParameters,
    QualityIssue,
    QualityReport,
    SimulationResult,
)

__all__ = [
    # Enums
    "DocumentType",
    "Language",
    "SectionType",
    "ProjectType",
    "EngineeringDiscipline",
    "OutputFormat",
    "JobStatus",
    "IssueSeverity",
    "SimulationType",
    # Documents
    "DocumentMetadata",
    "DocumentSection",
    "ParsedDocument",
    "TableData",
    "IndexedChunk",
    # Generation
    "ProjectParameters",
    "GeneratedSection",
    "GenerationResult",
    "BOQItem",
    "ProposalContext",
    "RenderResult",
    # Search
    "SearchResult",
    # Cost
    "CostItem",
    "CostEstimate",
    # Validation
    "HydrologicalParameters",
    "DrainageParameters",
    "SimulationResult",
    "QualityIssue",
    "QualityReport",
    # API
    "APIResponse",
    "AsyncJob",
]
