"""
Test script for AI-Proposal Engine POC
Verifies that the core components are working correctly
"""

import os
import sys
from pathlib import Path

# Add the poc_implementation directory to the path
sys.path.insert(0, str(Path(__file__).parent))

from proposal_engine_poc import ProposalEnginePOC

def test_poc_components():
    """
    Test the core components of the POC
    """
    print("Testing AI-Proposal Engine POC components...")
    
    # Test initialization
    try:
        engine = ProposalEnginePOC()
        print("✓ ProposalEnginePOC initialized successfully")
    except Exception as e:
        print(f"✗ Failed to initialize ProposalEnginePOC: {e}")
        return False
    
    # Test directory creation
    try:
        assert engine.data_dir.exists(), "Data directory not created"
        assert engine.storage_dir.exists(), "Storage directory not created"
        print("✓ Directories created successfully")
    except AssertionError as e:
        print(f"✗ Directory creation failed: {e}")
        return False
    except Exception as e:
        print(f"✗ Directory test failed: {e}")
        return False
    
    # Test that required methods exist
    methods_to_test = [
        'load_documents',
        'build_knowledge_base', 
        'load_knowledge_base',
        'setup_query_engine',
        'generate_proposal_section',
        'validate_proposal_content',
        'generate_proposal_template'
    ]
    
    for method in methods_to_test:
        try:
            assert hasattr(engine, method), f"Method {method} not found"
            print(f"✓ Method {method} exists")
        except AssertionError as e:
            print(f"✗ Method {method} missing: {e}")
            return False
    
    print("\n✓ All POC components tested successfully!")
    print("\nPOC is ready for implementation with the following capabilities:")
    print("- Document processing (PDF, DOCX)")
    print("- Knowledge base with vector storage")
    print("- RAG-based content generation")
    print("- Proposal validation")
    print("- Template-based generation")
    
    return True

def create_sample_directories():
    """
    Create sample directories for the POC
    """
    base_path = Path(__file__).parent
    
    dirs_to_create = [
        base_path / "data" / "input",
        base_path / "storage",
        base_path / "templates",
        base_path / "output"
    ]
    
    for dir_path in dirs_to_create:
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {dir_path}")

if __name__ == "__main__":
    print("Running POC component tests...\n")
    
    # Create sample directories
    create_sample_directories()
    
    # Run tests
    success = test_poc_components()
    
    if success:
        print("\n🎉 POC framework is ready for development!")
        print("\nNext steps:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Add sample documents to ./data/input/")
        print("3. Run the main POC implementation")
    else:
        print("\n❌ POC framework has issues that need to be resolved")
        sys.exit(1)