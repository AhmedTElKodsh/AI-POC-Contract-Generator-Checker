"""
Extract text from DOCX and PDF files.
Uses configuration for default paths and supports command-line overrides.
"""

import os
import sys
from pathlib import Path

from docx import Document
import pymupdf4llm

# Configuration - centralized settings for easy maintenance
CONFIG = {
    "DEFAULT_PROPOSAL_DIR": "proposals",
    "DEFAULT_PROPOSAL_FILE": "العرض الفنى والمالى للدراسة الهيدرولوجية وصلة مطار أسوان.docx",
    "DEFAULT_REPORT_DIR": "Reports",
    "DEFAULT_REPORT_FILE": "Final Design of Drainage System Report.pdf",
    "PREVIEW_LENGTH": 2000,
}

# Get script directory for relative paths
SCRIPT_DIR = Path(__file__).parent.resolve()


def extract_docx(file_path):
    """Extract text from a DOCX file."""
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return "\n".join(full_text)


def extract_pdf(file_path):
    """Extract text from a PDF file using pymupdf4llm."""
    md_text = pymupdf4llm.to_markdown(file_path)
    return md_text


def get_default_proposal_path():
    """Get the default proposal file path."""
    return SCRIPT_DIR / CONFIG["DEFAULT_PROPOSAL_DIR"] / CONFIG["DEFAULT_PROPOSAL_FILE"]


def get_default_report_path():
    """Get the default report file path."""
    return SCRIPT_DIR / CONFIG["DEFAULT_REPORT_DIR"] / CONFIG["DEFAULT_REPORT_FILE"]


def main():
    """Main entry point for the document extraction script."""
    import argparse

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Extract text from DOCX and PDF files")
    parser.add_argument(
        "--proposal",
        type=str,
        help="Path to proposal DOCX file (overrides default)",
    )
    parser.add_argument("--report", type=str, help="Path to report PDF file (overrides default)")
    parser.add_argument(
        "--preview-length",
        type=int,
        default=CONFIG["PREVIEW_LENGTH"],
        help=f"Length of preview text to show (default: {CONFIG['PREVIEW_LENGTH']})",
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")

    args = parser.parse_args()

    # Determine proposal file path
    if args.proposal:
        proposal_file = Path(args.proposal)
        if args.verbose:
            print(f"[INFO] Using provided proposal path: {proposal_file}")
    else:
        proposal_file = get_default_proposal_path()
        if args.verbose:
            print(f"[INFO] Using default proposal path: {proposal_file}")

    # Determine report file path
    if args.report:
        report_file = Path(args.report)
        if args.verbose:
            print(f"[INFO] Using provided report path: {report_file}")
    else:
        report_file = get_default_report_path()
        if args.verbose:
            print(f"[INFO] Using default report path: {report_file}")

    # Extract from proposal
    print("--- PROPOSAL EXTRACTION ---")
    try:
        if not proposal_file.exists():
            print(f"[WARN] Proposal file not found: {proposal_file}")
            print("[INFO] Use --proposal flag to specify a different file")
        else:
            content = extract_docx(str(proposal_file))
            preview = content[: args.preview_length]
            print(preview)
            if len(content) > args.preview_length:
                print("... [truncated]")
    except Exception as e:
        print(f"Error reading docx: {e}")

    # Extract from report
    print("\n--- REPORT EXTRACTION ---")
    try:
        if not report_file.exists():
            print(f"[WARN] Report file not found: {report_file}")
            print("[INFO] Use --report flag to specify a different file")
        else:
            content = extract_pdf(str(report_file))
            preview = content[: args.preview_length]
            print(preview)
            if len(content) > args.preview_length:
                print("... [truncated]")
    except Exception as e:
        print(f"Error reading pdf: {e}")


if __name__ == "__main__":
    main()
