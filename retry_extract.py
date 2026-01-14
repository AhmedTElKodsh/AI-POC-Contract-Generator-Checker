import os
from pathlib import Path
import logging
from docx import Document


def extract_docx(file_path):
    """Extract text from DOCX file with proper error handling."""
    try:
        doc = Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return "\n".join(full_text)
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except Exception as e:
        logging.error(f"Error reading DOCX file {file_path}: {str(e)}")
        raise


if __name__ == "__main__":
    # Use relative path instead of hardcoded absolute path
    base_dir = Path(__file__).parent
    file_path = base_dir / "proposals" / "AIEcon Ras ElHekma Tech..docx"

    # Validate file exists before processing
    if not file_path.exists():
        print(f"File not found: {file_path}")
        print("Available proposal files:")
        proposals_dir = base_dir / "proposals"
        if proposals_dir.exists():
            for file in proposals_dir.glob("*.docx"):
                print(f"  - {file.name}")
        exit(1)

    try:
        text = extract_docx(str(file_path))
        print(text[:5000])  # Print first 5000 chars
    except Exception as e:
        print(f"Error: {e}")
