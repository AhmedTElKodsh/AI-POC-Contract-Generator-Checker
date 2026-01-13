"""Validation and engineering calculation models."""

from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, Field

from src.models.enums import IssueSeverity, SimulationType


class HydrologicalParameters(BaseModel):
    """Parameters for hydrological analysis."""

    catchment_area_km2: float = Field(description="Catchment area in km²")
    rainfall_intensity_mm_hr: float = Field(description="Rainfall intensity in mm/hr")
    return_period_years: int = Field(description="Return period in years (e.g., 25, 50, 100)")
    runoff_coefficient: float = Field(ge=0.0, le=1.0, description="Runoff coefficient (0-1)")
    time_of_concentration_min: float = Field(description="Time of concentration in minutes")
    peak_discharge_m3_s: Optional[float] = Field(None, description="Peak discharge in m³/s")


class DrainageParameters(BaseModel):
    """Parameters for drainage system design."""

    pipe_diameter_mm: float = Field(description="Pipe diameter in mm")
    pipe_length_m: float = Field(description="Pipe length in meters")
    pipe_slope: float = Field(description="Pipe slope (e.g., 0.005 for 0.5%)")
    manning_n: float = Field(description="Manning's roughness coefficient")
    design_flow_m3_s: float = Field(description="Design flow in m³/s")
    velocity_m_s: Optional[float] = Field(None, description="Flow velocity in m/s")
    capacity_m3_s: Optional[float] = Field(None, description="Pipe capacity in m³/s")


class SimulationResult(BaseModel):
    """Result from hydraulic simulation (HEC-RAS, SWMM)."""

    simulation_type: SimulationType = Field(description="Type of simulation")
    simulation_id: str = Field(description="Simulation identifier")
    input_parameters: dict[str, Any] = Field(description="Input parameters")
    results: dict[str, Any] = Field(description="Simulation results")
    warnings: list[str] = Field(default_factory=list, description="Simulation warnings")
    errors: list[str] = Field(default_factory=list, description="Simulation errors")
    success: bool = Field(description="Whether simulation completed successfully")
    execution_time_seconds: float = Field(description="Execution time")
    created_at: datetime = Field(default_factory=datetime.utcnow)


class QualityIssue(BaseModel):
    """A quality issue found during validation."""

    severity: IssueSeverity = Field(description="Issue severity")
    category: str = Field(description="Issue category (e.g., 'technical', 'consistency')")
    description: str = Field(description="Issue description")
    location: Optional[str] = Field(None, description="Location in document (e.g., section name)")
    suggestion: Optional[str] = Field(None, description="Suggested fix")


class QualityReport(BaseModel):
    """Quality validation report for generated content."""

    job_id: str = Field(description="Job identifier")
    total_issues: int = Field(description="Total number of issues")
    critical_issues: int = Field(description="Number of critical issues")
    high_issues: int = Field(description="Number of high severity issues")
    medium_issues: int = Field(description="Number of medium severity issues")
    low_issues: int = Field(description="Number of low severity issues")
    issues: list[QualityIssue] = Field(description="List of all issues")
    overall_score: float = Field(ge=0.0, le=100.0, description="Overall quality score (0-100)")
    passed: bool = Field(description="Whether validation passed")
    created_at: datetime = Field(default_factory=datetime.utcnow)
