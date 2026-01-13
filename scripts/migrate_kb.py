import json
import os
import shutil
from typing import List, Dict, Any

# LlamaIndex Imports
from llama_index.core import Document, VectorStoreIndex, StorageContext, Settings
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.ollama import OllamaEmbedding
import chromadb

# --- Configuration ---
KB_JSON_PATH = "knowledge_base.json"
CHROMA_DB_PATH = "./chroma_db"
EMBEDDING_MODEL_NAME = "nomic-embed-text" # Must be pulled: `ollama pull nomic-embed-text`
BASE_URL = "http://localhost:11434"

def load_knowledge_base(path: str) -> Dict[str, Any]:
    """Loads the legacy JSON knowledge base."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Knowledge base not found at {path}")
    
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_documents_from_standards(kb_data: Dict[str, Any]) -> List[Document]:
    """Extracts 'Standards' (Glossary, References) into LlamaIndex Documents."""
    docs = []
    
    # Traverse the 'knowledge_base' root
    # Civil Engineering, GIS, Hydrological, etc.
    for category, content in kb_data.get("knowledge_base", {}).items():
        # 1. Glossaries
        glossary = content.get("glossary", {})
        for term, definition in glossary.items():
            text = f"Term: {term}\nDefinition: {definition}\nCategory: {category}"
            docs.append(Document(
                text=text,
                metadata={
                    "type": "glossary",
                    "category": category,
                    "term": term
                }
            ))
            
        # 2. Technical References
        refs = content.get("technical_references", [])
        for ref in refs:
            docs.append(Document(
                text=f"Standard Reference: {ref}\nCategory: {category}",
                metadata={
                    "type": "standard",
                    "category": category
                }
            ))
            
        # 3. API Docs & Integration Guides
        apis = content.get("api_docs", [])
        for api in apis:
             docs.append(Document(
                text=f"API Tool: {api}\nCategory: {category}",
                metadata={"type": "tool", "category": category}
            ))

    print(f"✅ Extracted {len(docs)} Standard/Glossary documents.")
    return docs

def create_documents_from_archives(kb_data: Dict[str, Any]) -> List[Document]:
    """Extracts 'Proposals' & 'Reports' into LlamaIndex Documents."""
    docs = []
    
    # We iterate over keys that start with "proposals_" or "reports_"
    # In the provided JSON structure, these are top-level keys
    for key, content in kb_data.items():
        if key == "knowledge_base": continue # Skip the standards section
        
        doc_type = content.get("type", "unknown") # proposals vs reports
        segments = content.get("segments", {})
        
        # Create a document for each major segment (Intro, Methodology, etc)
        # This improves retrieval accuracy over chunking one giant doc
        for section_name, text in segments.items():
            if not text: continue
            
            full_text = f"Project Document: {key}\nSection: {section_name}\nContent: {text}"
            docs.append(Document(
                text=full_text,
                metadata={
                    "type": "archive",
                    "doc_type": doc_type, # proposal vs report
                    "project_key": key,
                    "section": section_name
                }
            ))
            
    print(f"✅ Extracted {len(docs)} Archive segments (Project History).")
    return docs

def migrate():
    print(f"🚀 Starting Migration: {KB_JSON_PATH} -> {CHROMA_DB_PATH}")
    
    # 1. Load Data
    data = load_knowledge_base(KB_JSON_PATH)
    
    # 2. Prepare Documents
    docs_standards = create_documents_from_standards(data)
    docs_archives = create_documents_from_archives(data)
    
    # 3. Initialize ChromaDB (Persistent)
    # We use TWO collections to keep "Rules" separate from "Examples"
    db_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
    
    # 4. Initialize Embedding Model (Ollama)
    print(f"🔌 Connecting to Ollama ({EMBEDDING_MODEL_NAME})...")
    embed_model = OllamaEmbedding(
        model_name=EMBEDDING_MODEL_NAME,
        base_url=BASE_URL,
        ollama_additional_kwargs={"mirostat": 0}
    )
    Settings.embed_model = embed_model
    Settings.llm = None # We don't need generation for migration
    
    # 5. Ingest 'Standards' Collection
    print("📚 Indexing Standards & Glossaries...")
    chroma_collection_rules = db_client.get_or_create_collection("engineering_standards")
    vector_store_rules = ChromaVectorStore(chroma_collection=chroma_collection_rules)
    storage_context_rules = StorageContext.from_defaults(vector_store=vector_store_rules)
    
    VectorStoreIndex.from_documents(
        docs_standards, 
        storage_context=storage_context_rules,
        show_progress=True
    )
    
    # 6. Ingest 'Archives' Collection
    print("🗄️ Indexing Project Archives...")
    chroma_collection_archives = db_client.get_or_create_collection("project_archives")
    vector_store_archives = ChromaVectorStore(chroma_collection=chroma_collection_archives)
    storage_context_archives = StorageContext.from_defaults(vector_store=vector_store_archives)
    
    VectorStoreIndex.from_documents(
        docs_archives, 
        storage_context=storage_context_archives,
        show_progress=True
    )
    
    print("\n🎉 Migration Complete!")
    print(f"📂 Data stored in: {os.path.abspath(CHROMA_DB_PATH)}")
    print("Use these collection names in your Agent:")
    print("   - 'engineering_standards'")
    print("   - 'project_archives'")

if __name__ == "__main__":
    # Ensure Ollama is running and model is pulled before executing!
    # Run: `ollama pull nomic-embed-text`
    migrate()
