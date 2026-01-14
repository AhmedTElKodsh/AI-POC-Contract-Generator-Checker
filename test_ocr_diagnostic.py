"""
OCR Diagnostic Test Script
Tests Tesseract OCR integration and document processing pipeline
"""

import sys
import os
from pathlib import Path

def test_tesseract_installation():
    """Test 1: Verify Tesseract is installed and accessible"""
    print("\n" + "="*60)
    print("TEST 1: Tesseract Installation")
    print("="*60)
    
    try:
        import pytesseract
        
        # Test with explicit path
        tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        if os.path.exists(tesseract_path):
            pytesseract.pytesseract.tesseract_cmd = tesseract_path
            version = pytesseract.get_tesseract_version()
            print(f"✅ Tesseract Version: {version}")
            
            # Check languages
            languages = pytesseract.get_languages()
            print(f"✅ Total Languages: {len(languages)}")
            print(f"✅ Arabic Support: {'ara' in languages}")
            print(f"✅ English Support: {'eng' in languages}")
            
            return True
        else:
            print(f"❌ Tesseract not found at: {tesseract_path}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_doc_pipeline_ocr():
    """Test 2: Verify doc_pipeline OCR integration"""
    print("\n" + "="*60)
    print("TEST 2: Document Pipeline OCR Integration")
    print("="*60)
    
    try:
        import doc_pipeline
        
        print(f"✅ OCR Enabled: {doc_pipeline.OCR_ENABLED}")
        print(f"✅ Tesseract Version: {doc_pipeline.TESSERACT_VERSION}")
        
        if not doc_pipeline.OCR_ENABLED:
            print("❌ OCR is not enabled in doc_pipeline")
            return False
            
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_knowledge_base_quality():
    """Test 3: Check knowledge base extraction quality"""
    print("\n" + "="*60)
    print("TEST 3: Knowledge Base Quality")
    print("="*60)
    
    try:
        import json
        
        with open('knowledge_base.json', 'r', encoding='utf-8') as f:
            kb = json.load(f)
        
        docs = [k for k in kb.keys() if not k.startswith('knowledge_base')]
        
        print(f"✅ Total Documents: {len(docs)}")
        
        # Calculate quality metrics
        total_segments = 0
        total_tables = 0
        docs_with_content = 0
        
        for doc_key in docs:
            doc_data = kb[doc_key]
            if isinstance(doc_data, dict):
                segments = doc_data.get('segments', {})
                tables = doc_data.get('tables', [])
                
                if segments or tables:
                    docs_with_content += 1
                    total_segments += len(segments)
                    total_tables += len(tables)
        
        print(f"✅ Documents with Content: {docs_with_content}/{len(docs)}")
        print(f"✅ Total Segments: {total_segments}")
        print(f"✅ Total Tables: {total_tables}")
        print(f"✅ Avg Segments/Doc: {total_segments/len(docs):.1f}")
        print(f"✅ Avg Tables/Doc: {total_tables/len(docs):.1f}")
        
        # Quality gate
        if docs_with_content == len(docs) and total_segments > 0:
            print("✅ QUALITY CHECK: PASSED")
            return True
        else:
            print("⚠️  QUALITY CHECK: Some documents may have extraction issues")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_pdf_text_extraction():
    """Test 4: Test PDF text extraction capability"""
    print("\n" + "="*60)
    print("TEST 4: PDF Text Extraction")
    print("="*60)
    
    try:
        import doc_pipeline
        from pathlib import Path
        
        # Find a PDF to test
        pdf_files = list(Path('Reports').glob('*.pdf'))
        
        if not pdf_files:
            print("⚠️  No PDF files found in Reports folder")
            return False
        
        test_pdf = pdf_files[0]
        print(f"Testing with: {test_pdf.name}")
        
        # Try to extract
        result = doc_pipeline.extract_pdf_segments(str(test_pdf), max_pages=1)
        
        if isinstance(result, dict) and 'Error' not in result:
            print(f"✅ Extraction successful")
            print(f"✅ Sections found: {len(result.get('segments', {}))}")
            return True
        else:
            print(f"❌ Extraction failed: {result.get('Error', 'Unknown error')}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def main():
    """Run all diagnostic tests"""
    print("\n" + "="*60)
    print("OCR & DOCUMENT PROCESSING DIAGNOSTIC SUITE")
    print("="*60)
    
    results = {
        'Tesseract Installation': test_tesseract_installation(),
        'Pipeline OCR Integration': test_doc_pipeline_ocr(),
        'Knowledge Base Quality': test_knowledge_base_quality(),
        'PDF Text Extraction': test_pdf_text_extraction(),
    }
    
    # Summary
    print("\n" + "="*60)
    print("DIAGNOSTIC SUMMARY")
    print("="*60)
    
    passed = sum(results.values())
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 ALL SYSTEMS OPERATIONAL - NO ISSUES FOUND")
        return 0
    else:
        print(f"\n⚠️  {total - passed} test(s) failed - review output above")
        return 1


if __name__ == "__main__":
    sys.exit(main())
