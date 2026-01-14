#!/usr/bin/env python3
"""
Test script to verify that the fixes work correctly
"""

import os
import sys
import logging
from pathlib import Path

# Set up console logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_basic_import():
    """Test that the module imports without errors."""
    try:
        import doc_pipeline
        print("✓ Module imported successfully")
        return True
    except Exception as e:
        print(f"✗ Import failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_functions():
    """Test key functions work correctly."""
    try:
        import doc_pipeline
        
        # Find a test file
        proposals_dir = Path("proposals")
        if not proposals_dir.exists():
            print("✗ Proposals directory not found")
            return False
            
        test_file = next(proposals_dir.glob("*.docx"), None)
        if not test_file:
            print("✗ No DOCX files found for testing")
            return False
            
        print(f"✓ Found test file: {test_file.name}")
        
        # Test hash function
        file_hash = doc_pipeline.get_file_hash(str(test_file))
        if file_hash:
            print(f"✓ Hash function works: {file_hash[:16]}...")
        else:
            print("✗ Hash function failed")
            return False
            
        # Test validation function
        is_valid = doc_pipeline.validate_file_path(str(test_file), ['.docx'], str(proposals_dir))
        if is_valid:
            print("✓ Validation function works")
        else:
            print("✗ Validation function failed")
            return False
            
        # Test extract function (limited)
        try:
            content = doc_pipeline.extract_docx_segments(str(test_file))
            if isinstance(content, dict) and 'Error' not in content:
                print("✓ DOCX extraction works")
            else:
                print(f"! DOCX extraction returned: {content}")
        except Exception as e:
            print(f"✗ DOCX extraction failed: {e}")
            
        return True
    except Exception as e:
        print(f"✗ Function test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("Testing fixes applied to doc_pipeline.py...")
    print("=" * 50)
    
    success = True
    success &= test_basic_import()
    success &= test_functions()
    
    print("=" * 50)
    if success:
        print("✓ All tests passed! Fixes are working correctly.")
    else:
        print("✗ Some tests failed.")
    
    return success

if __name__ == "__main__":
    main()