"""Enumeration types for the AI Engine."""

from enum import Enum


class DocumentType(str, Enum):
    """Supported document types for ingestion."""

    PDF = "pdf"
    DOCX = "docx"


class Language(str, Enum):
    """Supported languages for document processing."""

    ARABIC = "ar"
    ENGLISH = "en"
    MIXED = "mixed"


class SectionType(str, Enum):
    """Types of sections in engineering proposals and reports."""

    EXECUTIVE_SUMMARY = "executive_summary"
    INTRODUCTION = "introduction"
    SCOPE_OF_WORK = "scope_of_work"
    METHODOLOGY = "methodology"
    TECHNICAL_APPROACH = "technical_approach"
    TIMELINE = "timeline"
    TEAM_COMPOSITION = "team_composition"
    DELIVERABLES = "deliverables"
    COST_ESTIMATE = "cost_estimate"
    BOQ = "boq"
    TERMS_AND_CONDITIONS = "terms_and_conditions"
    APPENDIX = "appendix"
    REFERENCES = "references"
    CONCLUSIONS = "conclusions"
    RECOMMENDATIONS = "recommendations"
    OTHER = "other"


class ProjectType(str, Enum):
    """Types of civil engineering projects."""

    HYDROLOGICAL_STUDY = "hydrological_study"
    DRAINAGE_DESIGN = "drainage_design"
    FLOOD_ANALYSIS = "flood_analysis"
    STORMWATER_MANAGEMENT = "stormwater_management"
    WATER_SUPPLY = "water_supply"
    WASTEWATER = "wastewater"
    ROAD_DESIGN = "road_design"
    BRIDGE_DESIGN = "bridge_design"
    STRUCTURAL_ANALYSIS = "structural_analysis"
    GEOTECHNICAL_INVESTIGATION = "geotechnical_investigation"
    ENVIRONMENTAL_ASSESSMENT = "environmental_assessment"
    MASTER_PLANNING = "master_planning"
    FEASIBILITY_STUDY = "feasibility_study"
    OTHER = "other"


class EngineeringDiscipline(str, Enum):
    """Engineering disciplines covered by the system."""

    STRUCTURAL = "structural"
    GEOTECHNICAL = "geotechnical"
    TRANSPORTATION = "transportation"
    ENVIRONMENTAL = "environmental"
    CONSTRUCTION = "construction"
    HYDRAULIC = "hydraulic"
    WATER_RESOURCES = "water_resources"
    COASTAL = "coastal"
    URBAN_PLANNING = "urban_planning"


class OutputFormat(str, Enum):
    """Output formats for generated documents."""

    DOCX = "docx"
    PDF = "pdf"


class JobStatus(str, Enum):
    """Status of async processing jobs."""

    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class IssueSeverity(str, Enum):
    """Severity levels for quality issues."""

    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class SimulationType(str, Enum):
    """Types of hydraulic simulations."""

    STEADY_FLOW = "steady_flow"
    UNSTEADY_FLOW = "unsteady_flow"
    DRAINAGE = "drainage"
    HEC_RAS = "hec_ras"
    SWMM = "swmm"
