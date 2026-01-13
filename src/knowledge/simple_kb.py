import json
import os
from typing import Dict, List, Optional

class SimpleKnowledgeBase:
    """
    A simple interface for interacting with the JSON-based Knowledge Base.
    
    This class is responsible for loading engineering definitions, technical references,
    and API documentation references from a static JSON file.
    
    Attributes:
        path (str): The file path to the JSON knowledge base.
        data (dict): The loaded JSON data in memory.
    """

    def __init__(self, json_path: str = "knowledge_base.json"):
        """
        Initialize the Knowledge Base.

        Args:
            json_path (str): Path to the knowledge_base.json file. Defaults to current directory.
        """
        # Robust path resolution:
        # 1. Check if path exists as is
        if os.path.exists(json_path):
            self.path = json_path
        else:
            # 2. Check relative to the project root (assuming we are in src/knowledge)
            # This handles cases where we run from a subdir
            project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
            potential_path = os.path.join(project_root, json_path)
            if os.path.exists(potential_path):
                self.path = potential_path
            else:
                self.path = json_path # Fallback to original to show error in _load

        self.data = {}
        self._load()

    def _load(self):
        """
        Internal method to load the JSON file from disk.
        
        Handles FileNotFoundError gracefully by initializing an empty dict, 
        preventing the program from crashing if the KB is missing.
        """
        if os.path.exists(self.path):
            try:
                with open(self.path, 'r', encoding='utf-8') as f:
                    # We expect the root key to be "knowledge_base" based on the file structure
                    self.data = json.load(f).get("knowledge_base", {})
            except json.JSONDecodeError:
                print(f"Error: Failed to decode JSON from {self.path}")
                self.data = {}
        else:
            print(f"Warning: Knowledge base file not found at {self.path}")

    def get_definition(self, term: str) -> Optional[str]:
        """
        Search for a specific term's definition across all knowledge categories.

        Args:
            term (str): The term to define (e.g., "Abutment").

        Returns:
            Optional[str]: The definition if found, otherwise None.
        """
        # Iterate through categories like 'civil_engineering', 'hydrological', etc.
        for category, content in self.data.items():
            glossary = content.get("glossary", {})
            if term in glossary:
                return glossary[term]
        return None

    def get_references(self, category: str) -> List[str]:
        """
        Retrieve a list of technical references (codes, standards) for a specific category.

        Args:
            category (str): The category key (e.g., 'civil_engineering', 'hydrological').

        Returns:
            List[str]: A list of reference strings. Returns empty list if category not found.
        """
        return self.data.get(category, {}).get("technical_references", [])

    def search_terms(self, text: str) -> Dict[str, str]:
        """
        Scan a block of text to find any known glossary terms.

        This is a simple keyword matching algorithm. It checks if any term 
        in our knowledge base exists within the provided text (case-insensitive).

        Args:
            text (str): The input text (e.g., the Scope of Work from a proposal).

        Returns:
            Dict[str, str]: A dictionary of {term: definition} for all matches found.
        """
        found_terms = {}
        # Normalize input text to lowercase for case-insensitive matching
        text_lower = text.lower()
        
        for category, content in self.data.items():
            glossary = content.get("glossary", {})
            for term, definition in glossary.items():
                # specific check: ensure the term is actually in the text
                # We use lower() on both sides to ensure "Flood" matches "flood"
                if term.lower() in text_lower:
                    found_terms[term] = definition
                    
        return found_terms