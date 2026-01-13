import pymupdf4llm
import re
import os
from typing import Dict, Any
from src.models.generation import ProposalContext

class PDFParser:
    """
    A robust PDF parser that converts PDF content to Markdown before extraction.
    
    This class implements the same interface as SimpleParser but handles binary PDF inputs.
    It uses 'pymupdf4llm' to preserve layout and structure (like headers and tables) 
    in a Markdown format, which is then easier to parse with Regex or passed to an LLM.
    """

    def __init__(self):
        # We reuse the same patterns as SimpleParser for consistency,
        # but in a real system, we might have PDF-specific patterns.
        self.patterns = {
            "project_name": [
                r"(?i)Project Name[:\s]*(.*)",
                r"(?i)^#+\s*(.*Project.*)",  # Markdown header
                r"(?i)Project[:\s]*(.*)"
            ],
            "client": [
                r"(?i)Client[:\s]*(.*)",
                r"(?i)Prepared for[:\s]*(.*)",
                r"(?i)Client Name[:\s]*(.*)"
            ],
            "location": [
                r"(?i)Location[:\s]*(.*)",
                r"(?i)Site[:\s]*(.*)"
            ],
            "duration": [
                r"(?i)Duration[:\s]*(\d+)\s*months?",
                r"(?i)Time for Completion[:\s]*(\d+)\s*months?"
            ]
        }

    def parse_file(self, file_path: str) -> ProposalContext:
        """
        Parses a PDF file and returns a ProposalContext.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        # 1. Convert PDF to Markdown using pymupdf4llm
        # This gives us a nice text representation with tables preserved as pipe-tables
        try:
            md_content = pymupdf4llm.to_markdown(file_path)
        except Exception as e:
            print(f"Error reading PDF with pymupdf4llm: {e}")
            # Fallback to empty content or re-raise
            raise e

        # 2. Extract Data using Regex (same logic as SimpleParser)
        extracted_data: Dict[str, Any] = {
            "project_name": "Unknown Project",
            "client": "Unknown Client",
            "location": "Unknown Location",
            "duration_months": 6
        }

        for key, patterns in self.patterns.items():
            for pattern in patterns:
                match = re.search(pattern, md_content, re.MULTILINE)
                if match:
                    val = match.group(1).strip().strip('*#_') # Clean markdown syntax
                    if key == "duration":
                        try:
                            extracted_data["duration_months"] = int(val)
                        except ValueError:
                            pass
                    else:
                        extracted_data[key] = val
                    break

        # 3. Extract Scope (Slightly smarter regex for Markdown headers)
        # Look for "## Scope" or "**Scope**", then "Introduction", then "Objective"
        scope_patterns = [
            r"(?i)(?:^#+|\*\*)\s*Scope(?: of Work)?.*?\n(.*?)(?=\n#|\n\*\*|$)",
            r"(?i)(?:^#+|\*\*)\s*Introduction.*?\n(.*?)(?=\n#|\n\*\*|$)",
            r"(?i)(?:^#+|\*\*)\s*Objective.*?\n(.*?)(?=\n#|\n\*\*|$)"
        ]
        
        sections = {}
        for pattern in scope_patterns:
            scope_match = re.search(pattern, md_content, re.DOTALL | re.MULTILINE)
            if scope_match:
                candidate = scope_match.group(1).strip()
                # Only accept if it has some substance (e.g., > 50 chars)
                # This prevents capturing empty space between "1. INTRODUCTION" and "1.1 General"
                if len(candidate) > 50:
                    sections["scope"] = candidate
                    break
        
        if "scope" not in sections:
             # Fallback: If no specific section found, use the first 5000 chars 
             # (excluding TOC likely) to ensure KB has something to search.
             # Finding the end of TOC is hard with regex, so we just take a chunk.
             print("⚠️ No specific Scope/Intro section found. Using full text chunk for context.")
             sections["scope"] = md_content[:5000]

        return ProposalContext(
            project_name=extracted_data["project_name"],
            client=extracted_data["client"],
            location=extracted_data["location"],
            duration_months=extracted_data["duration_months"],
            sections=sections
        )
