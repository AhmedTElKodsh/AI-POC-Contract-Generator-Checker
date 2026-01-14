"""Pytest configuration and shared fixtures for AI Engine tests."""

import pytest
from hypothesis import settings, Verbosity

# Configure Hypothesis for property-based testing
settings.register_profile(
    "default",
    max_examples=100,
    deadline=5000,
    verbosity=Verbosity.normal,
)
settings.register_profile(
    "ci",
    max_examples=200,
    deadline=10000,
    verbosity=Verbosity.verbose,
)
settings.register_profile(
    "dev",
    max_examples=10,
    deadline=None,
    verbosity=Verbosity.verbose,
)
settings.load_profile("default")


@pytest.fixture
def sample_arabic_text() -> str:
    """Sample Arabic text for testing."""
    return "دراسة هيدرولوجية لمشروع الصرف الصحي"


@pytest.fixture
def sample_english_text() -> str:
    """Sample English text for testing."""
    return "Hydrological study for drainage project"


@pytest.fixture
def sample_mixed_text() -> str:
    """Sample mixed Arabic-English text for testing."""
    return "دراسة هيدرولوجية using HEC-RAS model للمشروع"


@pytest.fixture
def sample_boq_items() -> list[dict]:
    """Sample BOQ items for testing."""
    return [
        {
            "item_number": "1.1",
            "description": "Excavation works",
            "unit": "m3",
            "quantity": 1500.0,
            "unit_rate": 25.0,
        },
        {
            "item_number": "1.2",
            "description": "Concrete works C30",
            "unit": "m3",
            "quantity": 500.0,
            "unit_rate": 450.0,
        },
        {
            "item_number": "2.1",
            "description": "Steel reinforcement",
            "unit": "ton",
            "quantity": 50.0,
            "unit_rate": 15000.0,
        },
    ]


@pytest.fixture
def sample_project_metadata() -> dict:
    """Sample project metadata for testing."""
    return {
        "project_type": "hydrological_study",
        "client_name": "Ministry of Water Resources",
        "engineering_discipline": "hydraulic",
        "location": "Cairo, Egypt",
    }
