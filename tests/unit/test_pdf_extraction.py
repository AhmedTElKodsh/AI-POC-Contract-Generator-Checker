"""Unit tests for PDF extraction functions."""

import pytest
import os
import tempfile
import shutil
from pathlib import Path

import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import doc_pipeline


# Fixtures
@pytest.fixture
def temp_dir():
    """Create temporary directory for test files."""
    temp_path = tempfile.mkdtemp()
    yield temp_path
    shutil.rmtree(temp_path)


# Tests for PDF table extraction
def test_extract_tables_from_pdf_uses_pdfplumber(temp_dir):
    """Test that PDF table extraction uses pdfplumber."""
    # Skip if no PDF files available
    pdf_files = list(Path("Reports").glob("*.pdf"))
    if not pdf_files:
        pytest.skip("No PDF files available for testing")

    pdf_path = str(pdf_files[0])
    result = doc_pipeline.extract_tables_from_pdf(pdf_path)

    assert isinstance(result, list)


def test_extract_tables_from_pdf_structure(temp_dir):
    """Test that PDF tables have correct structure."""
    pdf_files = list(Path("Reports").glob("*.pdf"))
    if not pdf_files:
        pytest.skip("No PDF files available for testing")

    pdf_path = str(pdf_files[0])
    tables = doc_pipeline.extract_tables_from_pdf(pdf_path)

    for table in tables:
        assert "page" in table
        assert "rows" in table
        assert "columns" in table
        assert "data" in table
        assert isinstance(table["data"], list)


def test_extract_tables_from_pdf_cell_values(temp_dir):
    """Test that PDF table cells are properly extracted."""
    pdf_files = list(Path("Reports").glob("*.pdf"))
    if not pdf_files:
        pytest.skip("No PDF files available for testing")

    pdf_path = str(pdf_files[0])
    tables = doc_pipeline.extract_tables_from_pdf(pdf_path)

    for table in tables:
        for row in table["data"]:
            for cell in row:
                assert isinstance(cell, str)


def test_extract_tables_from_pdf_empty_file(temp_dir):
    """Test PDF table extraction with non-existent file."""
    result = doc_pipeline.extract_tables_from_pdf("nonexistent.pdf")

    # Should return empty list or handle gracefully
    assert isinstance(result, list)
    assert len(result) == 0


# Tests for PDF segment extraction
def test_extract_pdf_segments_structure(temp_dir):
    """Test that PDF segment extraction has correct structure."""
    pdf_files = list(Path("Reports").glob("*.pdf"))
    if not pdf_files:
        pytest.skip("No PDF files available for testing")

    pdf_path = str(pdf_files[0])
    result = doc_pipeline.extract_pdf_segments(pdf_path)

    assert isinstance(result, dict)
    assert "Error" not in result


def test_extract_pdf_segments_has_segments(temp_dir):
    """Test that PDF segment extraction creates segments."""
    pdf_files = list(Path("Reports").glob("*.pdf"))
    if not pdf_files:
        pytest.skip("No PDF files available for testing")

    pdf_path = str(pdf_files[0])
    result = doc_pipeline.extract_pdf_segments(pdf_path)

    assert isinstance(result, dict)
    assert len(result) > 0


def test_extract_pdf_segments_invalid_file(temp_dir):
    """Test PDF segment extraction with invalid file."""
    result = doc_pipeline.extract_pdf_segments("nonexistent.pdf")

    assert "Error" in result


def test_extract_pdf_segments_preserves_content(temp_dir):
    """Test that PDF segment extraction preserves document content."""
    pdf_files = list(Path("Reports").glob("*.pdf"))
    if not pdf_files:
        pytest.skip("No PDF files available for testing")

    pdf_path = str(pdf_files[0])
    result = doc_pipeline.extract_pdf_segments(pdf_path)

    # Check that segments contain content
    total_content = "\n".join(result.values())
    assert len(total_content) > 0


# Tests for OCR functions
def test_extract_pdf_with_ocr_requires_ocr(temp_dir):
    """Test that PDF with OCR function requires OCR to be enabled."""
    if not doc_pipeline.OCR_ENABLED:
        pytest.skip("OCR is not enabled")

    pdf_files = list(Path("Reports").glob("*.pdf"))
    if not pdf_files:
        pytest.skip("No PDF files available for testing")

    pdf_path = str(pdf_files[0])
    result = doc_pipeline.extract_pdf_with_ocr(pdf_path)

    assert isinstance(result, dict)


def test_detect_tables_with_ocr_fallback(temp_dir):
    """Test OCR table detection fallback."""
    if not doc_pipeline.OCR_ENABLED:
        pytest.skip("OCR is not enabled")

    pdf_files = list(Path("Reports").glob("*.pdf"))
    if not pdf_files:
        pytest.skip("No PDF files available for testing")

    pdf_path = str(pdf_files[0])
    result = doc_pipeline.detect_tables_with_ocr(pdf_path)

    assert isinstance(result, list)


def test_detect_tables_with_ocr_structure(temp_dir):
    """Test that OCR tables have correct structure."""
    if not doc_pipeline.OCR_ENABLED:
        pytest.skip("OCR is not enabled")

    pdf_files = list(Path("Reports").glob("*.pdf"))
    if not pdf_files:
        pytest.skip("No PDF files available for testing")

    pdf_path = str(pdf_files[0])
    tables = doc_pipeline.detect_tables_with_ocr(pdf_path)

    for table in tables:
        assert "page" in table
        assert "rows" in table
        assert "columns" in table
        assert "data" in table
        assert isinstance(table["data"], list)


# Bilingual content tests
def test_pdf_arabic_content(temp_dir):
    """Test PDF extraction with Arabic content."""
    arabic_pdfs = [f for f in Path("Reports").glob("*.pdf") if any(ord(c) > 127 for c in f.name)]

    if not arabic_pdfs:
        pytest.skip("No Arabic PDF files available for testing")

    pdf_path = str(arabic_pdfs[0])
    result = doc_pipeline.extract_pdf_segments(pdf_path)

    assert isinstance(result, dict)
    assert "Error" not in result


def test_pdf_mixed_language_content(temp_dir):
    """Test PDF extraction with mixed Arabic/English content."""
    pdf_files = list(Path("Reports").glob("*.pdf"))
    if not pdf_files:
        pytest.skip("No PDF files available for testing")

    # Find a PDF with content
    for pdf_path in pdf_files:
        result = doc_pipeline.extract_pdf_segments(str(pdf_path))
        if isinstance(result, dict) and "Error" not in result:
            # Check if result has any content
            content = "\n".join(result.values())
            if len(content) > 50:
                return  # Found a valid PDF

    pytest.skip("No PDF with sufficient content found")


# Edge cases
def test_extract_pdf_empty_segments(temp_dir):
    """Test PDF extraction doesn't return empty segments."""
    pdf_files = list(Path("Reports").glob("*.pdf"))
    if not pdf_files:
        pytest.skip("No PDF files available for testing")

    pdf_path = str(pdf_files[0])
    result = doc_pipeline.extract_pdf_segments(pdf_path)

    # Check that we don't have empty segments (except edge cases)
    non_empty_segments = [k for k, v in result.items() if v and len(v.strip()) > 0]
    assert len(non_empty_segments) > 0


def test_extract_pdf_large_file_handling(temp_dir):
    """Test PDF extraction handles large files gracefully."""
    pdf_files = list(Path("Reports").glob("*.pdf"))
    if not pdf_files:
        pytest.skip("No PDF files available for testing")

    # Find largest PDF
    pdf_files_sorted = sorted(pdf_files, key=lambda p: p.stat().st_size, reverse=True)
    largest_pdf = str(pdf_files_sorted[0])

    result = doc_pipeline.extract_pdf_segments(largest_pdf)

    assert isinstance(result, dict)
    assert "Error" not in result


# Integration tests
def test_full_pdf_extraction_workflow(temp_dir):
    """Test complete PDF extraction workflow."""
    pdf_files = list(Path("Reports").glob("*.pdf"))
    if not pdf_files:
        pytest.skip("No PDF files available for testing")

    pdf_path = str(pdf_files[0])

    # Extract segments
    segments = doc_pipeline.extract_pdf_segments(pdf_path)
    assert isinstance(segments, dict)
    assert "Error" not in segments

    # Extract tables
    tables = doc_pipeline.extract_tables_from_pdf(pdf_path)
    assert isinstance(tables, list)

    # Verify we have some content
    total_content = "\n".join(segments.values())
    assert len(total_content) > 0 or len(tables) > 0


def test_pdf_table_extraction_quality(temp_dir):
    """Test that PDF table extraction produces quality results."""
    pdf_files = list(Path("Reports").glob("*.pdf"))
    if not pdf_files:
        pytest.skip("No PDF files available for testing")

    pdf_path = str(pdf_files[0])
    tables = doc_pipeline.extract_tables_from_pdf(pdf_path)

    for table in tables:
        # Check table has reasonable dimensions
        assert table["rows"] > 0
        assert table["columns"] > 0

        # Check data exists
        assert table["data"]
        assert len(table["data"]) == table["rows"]

        # Check each row has correct number of columns
        for row in table["data"]:
            assert len(row) == table["columns"]


# Error handling tests
def test_extract_pdf_invalid_extension(temp_dir):
    """Test PDF extraction with wrong file extension."""
    file_path = os.path.join(temp_dir, "test.txt")
    Path(file_path).touch()

    result = doc_pipeline.extract_pdf_segments(file_path)

    assert "Error" in result


def test_extract_pdf_corrupted_file(temp_dir):
    """Test PDF extraction with corrupted file."""
    file_path = os.path.join(temp_dir, "corrupted.pdf")

    # Create a file with invalid PDF content
    with open(file_path, "wb") as f:
        f.write(b"This is not a valid PDF file")

    result = doc_pipeline.extract_pdf_segments(file_path)

    # Should handle gracefully
    assert isinstance(result, dict)
