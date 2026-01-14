"""
AI-Proposal Engine POC Implementation
Core building blocks for generating Civil Engineering Proposals and Technical/Financial Reports
"""

import os
import json
from pathlib import Path
from typing import Dict, List, Any
from llama_index.core import (
    VectorStoreIndex, 
    SimpleDirectoryReader, 
    StorageContext, 
    load_index_from_storage
)
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.core.prompts import PromptTemplate
from llama_index.core.query_engine import CitationQueryEngine
import docx
from docxtpl import DocxTemplate
import asyncio
from llama_index.core.workflow import Workflow, step, Event
from llama_index.core.tools import FunctionTool
from llama_index.llms.openai import OpenAI
from llama_index.core import Settings

# Configure settings
Settings.embed_model = "local:BAAI/bge-small-en-v1.5"  # Using a lightweight model

class ProposalEnginePOC:
    """
    Proof of Concept for the AI-Proposal Engine
    Implements the core building blocks for generating Civil Engineering Proposals
    """
    
    def __init__(self, data_dir: str = "./data", storage_dir: str = "./storage"):
        self.data_dir = Path(data_dir)
        self.storage_dir = Path(storage_dir)
        self.documents = []
        self.index = None
        self.query_engine = None
        
        # Create directories if they don't exist
        self.data_dir.mkdir(exist_ok=True)
        self.storage_dir.mkdir(exist_ok=True)
        
    def load_documents(self, file_paths: List[str]):
        """
        Load engineering documents (PDF, DOCX) for processing
        """
        print(f"Loading documents from: {file_paths}")
        loader = SimpleDirectoryReader(input_files=file_paths)
        self.documents = loader.load_data()
        print(f"Loaded {len(self.documents)} documents")
        
    def build_knowledge_base(self):
        """
        Build vector index from loaded documents for RAG
        """
        print("Building knowledge base...")
        
        # Split documents into chunks
        node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=50)
        nodes = node_parser.get_nodes_from_documents(self.documents)
        
        # Create embedding model
        embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
        
        # Build index
        self.index = VectorStoreIndex(nodes, embed_model=embed_model)
        
        # Persist index
        self.index.storage_context.persist(persist_dir=self.storage_dir)
        print("Knowledge base built and persisted")
        
    def load_knowledge_base(self):
        """
        Load existing knowledge base from storage
        """
        print("Loading existing knowledge base...")
        storage_context = StorageContext.from_defaults(persist_dir=self.storage_dir)
        self.index = load_index_from_storage(
            storage_context,
            # embed_model=HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
        )
        print("Knowledge base loaded")
        
    def setup_query_engine(self):
        """
        Setup query engine for retrieving relevant information
        """
        if self.index is None:
            raise ValueError("Index not built. Call build_knowledge_base() first.")
            
        # Create query engine with citation support
        self.query_engine = CitationQueryEngine.from_args(
            self.index,
            similarity_top_k=3,
            citation_chunk_attr_name="citation",
        )
        print("Query engine setup complete")
        
    def generate_proposal_section(self, query: str) -> str:
        """
        Generate a section of the proposal based on the query
        """
        if self.query_engine is None:
            raise ValueError("Query engine not setup. Call setup_query_engine() first.")
            
        response = self.query_engine.query(query)
        return str(response)
        
    def validate_proposal_content(self, content: str) -> List[str]:
        """
        Basic validation of proposal content
        """
        issues = []
        
        # Check for common issues
        if len(content.strip()) < 100:
            issues.append("Content too short")
            
        if "TODO" in content.upper():
            issues.append("Contains TODO placeholder")
            
        if "UNDEFINED" in content.upper():
            issues.append("Contains undefined elements")
            
        return issues
        
    def generate_proposal_template(self, template_path: str, context: Dict[str, Any]) -> str:
        """
        Generate proposal using a template
        """
        # Load template
        doc = DocxTemplate(template_path)
        
        # Render template with context
        doc.render(context)
        
        # Save to output file
        output_path = template_path.replace('.docx', '_generated.docx')
        doc.save(output_path)
        
        return output_path

# Example usage
def main():
    print("Starting AI-Proposal Engine POC...")
    
    # Initialize the engine
    engine = ProposalEnginePOC()
    
    # Example: Load sample documents (this would be your proposal templates and reference docs)
    # For now, we'll skip this step since we don't have actual files to load
    print("POC initialized successfully")
    print("\nNext steps:")
    print("1. Add your engineering documents to the data directory")
    print("2. Call engine.load_documents() with your file paths")
    print("3. Call engine.build_knowledge_base()")
    print("4. Call engine.setup_query_engine()")
    print("5. Use engine.generate_proposal_section() to generate content")
    
    # Example of how to use the engine once documents are loaded:
    # engine.load_documents(["path/to/your/documents"])
    # engine.build_knowledge_base()
    # engine.setup_query_engine()
    # content = engine.generate_proposal_section("Generate a technical specification for flood protection systems")
    # print(content)
    
    print("\nPOC framework ready for implementation!")

if __name__ == "__main__":
    main()