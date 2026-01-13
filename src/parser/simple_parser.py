import re
import os
from typing import Optional, Dict, Any
from src.models.generation import ProposalContext

class SimpleParser:
    """
    A rule-based document parser using Regular Expressions.
    
    This class demonstrates the 'Update' phase of our Game Loop architecture.
    It reads raw unstructured text and converts it into a structured ProposalContext object.
    
    In a full production system, this would be replaced by an AI-based parser (OCR/LLM),
    but the interface (taking a file and returning a Context) would remain the same.
    """

    def __init__(self):
        # Dictionary of Regex patterns for single-line entity extraction.
        # (?i) flag makes the match case-insensitive.
        # (.*) captures the value we want.
        self.patterns = {
            "project_name": [
                r"(?i)Project Name:\s*(.*)",
                r"(?i)Project:\s*(.*)",
                r"(?i)Name of Project:\s*(.*)"
            ],
            "client": [
                r"(?i)Client:\s*(.*)",
                r"(?i)Client Name:\s*(.*)",
                r"(?i)Prepared for:\s*(.*)"
            ],
            "location": [
                r"(?i)Location:\s*(.*)",
                r"(?i)Site:\s*(.*)",
                r"(?i)Project Location:\s*(.*)"
            ],
            # Captures digits (\d+) for the month count
            "duration": [
                r"(?i)Duration:\s*(\d+)\s*months?",
                r"(?i)Project Duration:\s*(\d+)\s*months?"
            ]
        }

    def parse_file(self, file_path: str) -> ProposalContext:
        """
        Main entry point for parsing.

        Args:
            file_path (str): Path to the input text file.

        Returns:
            ProposalContext: The structured state object containing extracted data.
        
        Raises:
            FileNotFoundError: If the input file does not exist.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Default values ensure the Context is valid even if extraction fails
        extracted_data: Dict[str, Any] = {
            "project_name": "Unknown Project",
            "client": "Unknown Client",
            "location": "Unknown Location",
            "duration_months": 6
        }

        # 1. Extract Metadata using Regex patterns
        for key, patterns in self.patterns.items():
            for pattern in patterns:
                match = re.search(pattern, content)
                if match:
                    val = match.group(1).strip()
                    if key == "duration":
                        try:
                            extracted_data["duration_months"] = int(val)
                        except ValueError:
                            pass # Keep default if parsing int fails
                    else:
                        extracted_data[key] = val
                    break # Stop checking other patterns for this key if one matches

        # 2. Extract Scope of Work (Multi-line extraction)
        # Pattern explanation:
        # (?is)     -> flags: case-insensitive (i), dot matches newline (s)
        # Scope...: -> matches the header "Scope of Work:" or "Scope:"
        # \s*\n     -> matches whitespace and the immediate newline
        # (.*?)     -> Non-greedy capture of the body content
        # (?=...)   -> Lookahead (don't consume): Stop when we see a double newline OR end of string ($) 
        #              This allows us to grab the paragraph block without grabbing the whole rest of the file.
        scope_match = re.search(r"(?i)Scope(?: of Work)?[:\s]*\n(.*?)(?=\n\n|$)", content, re.DOTALL)
        
        sections = {}
        if scope_match:
            # Clean up the extracted text (remove extra whitespace/newlines)
            sections["scope"] = scope_match.group(1).strip()
        else:
            # Fallback: If regex fails, try to find the line and take everything after it
            # This is helpful for our POC if the text formatting is messy
            if "Scope" in content:
                parts = content.split("Scope", 1)
                if len(parts) > 1:
                     # Take the first 500 characters after "Scope" as a fallback
                    sections["scope"] = parts[1].split("\n\n")[0].strip(" :of Work\n")

        return ProposalContext(
            project_name=extracted_data["project_name"],
            client=extracted_data["client"],
            location=extracted_data["location"],
            duration_months=extracted_data["duration_months"],
            sections=sections
        )