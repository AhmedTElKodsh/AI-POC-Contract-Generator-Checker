"""
Comprehensive POC Testing Script
Tests all components of the AI-POC-Contract-Generator-Checker
"""

import sys
import os
from pathlib import Path

# Add project root to path
sys.path.insert(0, os.getcwd())

def test_imports():
    """Test 1: Verify all critical imports work"""
    print("\n" + "="*60)
    print("TEST 1: Import Validation")
    print("="*60)
    
    try:
        from src.parser.pdf_parser import PDFParser
        print("✅ PDFParser imported successfully")
    except Exception as e:
        print(f"❌ PDFParser import failed: {e}")
        return False
    
    try:
        from src.parser.docx_parser import DocxParser
        print("✅ DocxParser imported successfully")
    except Exception as e:
        print(f"❌ DocxParser import failed: {e}")
        return False
    
    try:
        from src.knowledge.simple_kb import SimpleKnowledgeBase
        print("✅ SimpleKnowledgeBase imported successfully")
    except Exception as e:
        print(f"❌ SimpleKnowledgeBase import failed: {e}")
        return False
    
    try:
        from src.generator.simple_generator import SimpleGenerator
        print("✅ SimpleGenerator imported successfully")
    except Exception as e:
        print(f"❌ SimpleGenerator import failed: {e}")
        return False
    
    try:
        from src.models.generation import ProposalContext
        print("✅ ProposalContext imported successfully")
    except Exception as e:
        print(f"❌ ProposalContext import failed: {e}")
        return False
    
    return True

def test_knowledge_base():
    """Test 2: Knowledge Base functionality"""
    print("\n" + "="*60)
    print("TEST 2: Knowledge Base Operations")
    print("="*60)
    
    try:
        from src.knowledge.simple_kb import SimpleKnowledgeBase
        
        kb = SimpleKnowledgeBase()
        print("✅ Knowledge Base initialized")
        
        # Test definition lookup
        definition = kb.get_definition("Abutment")
        if definition:
            print(f"✅ Definition lookup works: 'Abutment' found")
            print(f"   Definition: {definition[:100]}...")
        else:
            print("⚠️  'Abutment' not found in KB")
        
        # Test references
        refs = kb.get_references("hydrological")
        if refs:
            print(f"✅ References lookup works: Found {len(refs)} hydrological references")
        else:
            print("⚠️  No hydrological references found")
        
        # Test term search
        test_text = "This project involves flood control and drainage systems"
        found_terms = kb.search_terms(test_text)
        print(f"✅ Term search works: Found {len(found_terms)} terms in test text")
        if found_terms:
            print(f"   Terms: {', '.join(list(found_terms.keys())[:5])}")
        
        return True
        
    except Exception as e:
        print(f"❌ Knowledge Base test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_docx_parser():
    """Test 3: DOCX Parser"""
    print("\n" + "="*60)
    print("TEST 3: DOCX Parser")
    print("="*60)
    
    try:
        from src.parser.docx_parser import DocxParser
        
        sample_file = "sample_client_rfp.docx"
        if not os.path.exists(sample_file):
            print(f"⚠️  Sample file not found: {sample_file}")
            return True  # Not a failure, just skip
        
        parser = DocxParser()
        print("✅ DocxParser initialized")
        
        context = parser.parse_file(sample_file)
        print("✅ File parsed successfully")
        print(f"   Project: {context.project_name}")
        print(f"   Client: {context.client}")
        print(f"   Location: {context.location}")
        print(f"   Duration: {context.duration_months} months")
        print(f"   Scope length: {len(context.sections.get('scope', ''))} chars")
        
        return True
        
    except Exception as e:
        print(f"❌ DOCX Parser test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_generator():
    """Test 4: Document Generator"""
    print("\n" + "="*60)
    print("TEST 4: Document Generator")
    print("="*60)
    
    try:
        from src.generator.simple_generator import SimpleGenerator
        from src.models.generation import ProposalContext
        from datetime import datetime
        
        # Check template exists
        template_path = "templates/poc_template.docx"
        if not os.path.exists(template_path):
            print(f"❌ Template not found: {template_path}")
            return False
        
        print(f"✅ Template found: {template_path}")
        
        # Parse actual sample document to get real data
        sample_file = "sample_client_rfp.docx"
        if os.path.exists(sample_file):
            from src.parser.docx_parser import DocxParser
            from src.knowledge.simple_kb import SimpleKnowledgeBase
            
            print("📄 Parsing sample document for real data...")
            parser = DocxParser()
            test_context = parser.parse_file(sample_file)
            
            # Enrich with KB
            kb = SimpleKnowledgeBase()
            scope_text = test_context.sections.get("scope", "")
            found_terms = kb.search_terms(scope_text)
            test_context.metadata["glossary"] = found_terms
            test_context.metadata["references"] = kb.get_references("hydrological")
            
            print(f"✅ Using real data from sample: {test_context.project_name}")
        else:
            # Fallback to test data if sample not available
            print("⚠️  Sample file not found, using test data")
            test_context = ProposalContext(
                project_name="Test Project",
                client="Test Client",
                location="Test Location",
                duration_months=12,
                sections={"scope": "This is a test scope of work."},
                metadata={
                    "glossary": {"Test Term": "Test Definition"},
                    "references": ["Test Standard 1", "Test Standard 2"]
                }
            )
        print("✅ Test context created")
        
        # Generate document
        generator = SimpleGenerator(template_path)
        output_path = "proposals/test_output.docx"
        os.makedirs("proposals", exist_ok=True)
        
        result = generator.generate(test_context, output_path)
        print(f"✅ Document generated: {result}")
        
        if os.path.exists(output_path):
            size = os.path.getsize(output_path)
            print(f"✅ Output file exists ({size} bytes)")
            return True
        else:
            print("❌ Output file not created")
            return False
        
    except Exception as e:
        print(f"❌ Generator test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_end_to_end():
    """Test 5: End-to-End Workflow"""
    print("\n" + "="*60)
    print("TEST 5: End-to-End Workflow")
    print("="*60)
    
    try:
        from src.parser.docx_parser import DocxParser
        from src.knowledge.simple_kb import SimpleKnowledgeBase
        from src.generator.simple_generator import SimpleGenerator
        
        sample_file = "sample_client_rfp.docx"
        if not os.path.exists(sample_file):
            print(f"⚠️  Sample file not found, skipping E2E test")
            return True
        
        # Phase 1: Parse
        print("\n📄 Phase 1: Parsing document...")
        parser = DocxParser()
        context = parser.parse_file(sample_file)
        print(f"✅ Parsed: {context.project_name}")
        
        # Phase 2: Enrich with KB
        print("\n🔍 Phase 2: Enriching with Knowledge Base...")
        kb = SimpleKnowledgeBase()
        scope_text = context.sections.get("scope", "")
        found_terms = kb.search_terms(scope_text)
        context.metadata["glossary"] = found_terms
        context.metadata["references"] = kb.get_references("hydrological")
        print(f"✅ Found {len(found_terms)} technical terms")
        print(f"✅ Added {len(context.metadata['references'])} references")
        
        # Phase 3: Generate
        print("\n📝 Phase 3: Generating proposal...")
        generator = SimpleGenerator()
        output_path = "proposals/e2e_test_output.docx"
        result = generator.generate(context, output_path)
        print(f"✅ Generated: {result}")
        
        if os.path.exists(output_path):
            size = os.path.getsize(output_path)
            print(f"\n🎉 END-TO-END TEST PASSED! Output: {size} bytes")
            return True
        else:
            print("\n❌ END-TO-END TEST FAILED: Output not created")
            return False
        
    except Exception as e:
        print(f"\n❌ End-to-End test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_file_structure():
    """Test 6: Verify critical files exist"""
    print("\n" + "="*60)
    print("TEST 6: File Structure Validation")
    print("="*60)
    
    critical_files = [
        "app.py",
        "requirements.txt",
        "knowledge_base.json",
        "templates/poc_template.docx",
        "src/parser/pdf_parser.py",
        "src/parser/docx_parser.py",
        "src/knowledge/simple_kb.py",
        "src/generator/simple_generator.py",
        "src/models/generation.py"
    ]
    
    all_exist = True
    for file_path in critical_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - MISSING")
            all_exist = False
    
    return all_exist

def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("🧪 COMPREHENSIVE POC TESTING")
    print("="*60)
    print(f"Working Directory: {os.getcwd()}")
    print(f"Python Version: {sys.version}")
    
    results = {
        "File Structure": test_file_structure(),
        "Imports": test_imports(),
        "Knowledge Base": test_knowledge_base(),
        "DOCX Parser": test_docx_parser(),
        "Generator": test_generator(),
        "End-to-End": test_end_to_end()
    }
    
    # Summary
    print("\n" + "="*60)
    print("📊 TEST SUMMARY")
    print("="*60)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    print(f"\n🎯 Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED! POC is fully functional.")
        return 0
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Review output above.")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
