import docx
import re
import os
from typing import Dict, Any
from src.models.generation import ProposalContext

class DocxParser:
    """
    Parses a DOCX file to extract project metadata and scope.
    """

    def __init__(self):
        # Reusing the same patterns for consistency
        self.patterns = {
            "project_name": [
                r"(?i)Project Name[:\s]*(.*)",
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
        Parses a DOCX file and returns a ProposalContext.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        try:
            doc = docx.Document(file_path)
        except Exception as e:
            raise Exception(f"Failed to read DOCX file: {e}")

        # Convert full doc text to a single string (preserving newlines)
        full_text = "\n".join([p.text for p in doc.paragraphs])

        extracted_data: Dict[str, Any] = {
            "project_name": "Unknown Project",
            "client": "Unknown Client",
            "location": "Unknown Location",
            "duration_months": 6
        }

        # 1. Metadata Extraction
        for key, patterns in self.patterns.items():
            for pattern in patterns:
                match = re.search(pattern, full_text, re.MULTILINE)
                if match:
                    val = match.group(1).strip()
                    if key == "duration":
                        try:
                            extracted_data["duration_months"] = int(val)
                        except ValueError:
                            pass
                    else:
                        extracted_data[key] = val
                    break

        # 2. Scope Extraction
        # Look for "Scope of Work" header and grab text until the next header
        sections = {}
        
        # Simple heuristic: Split by "Scope" and take the chunk until the next "3." or similar header
        if "Scope" in full_text:
            # Try to capture everything after "Scope"
            # In a real DOCX parser, we would iterate paragraphs to find the Header style
            # But for this POC, splitting text is sufficient.
            parts = re.split(r"(?i)Scope(?: of Work)?", full_text, maxsplit=1)
            if len(parts) > 1:
                scope_content = parts[1]
                # Stop at the next likely header (e.g., "3. Deliverables")
                # We look for a newline followed by a digit and a dot
                scope_match = re.split(r"\n\d+\.", scope_content)
                sections["scope"] = scope_match[0].strip()
        
        if "scope" not in sections:
             # Fallback
             sections["scope"] = full_text[:2000]

        return ProposalContext(
            project_name=extracted_data["project_name"],
            client=extracted_data["client"],
            location=extracted_data["location"],
            duration_months=extracted_data["duration_months"],
            sections=sections
        )
