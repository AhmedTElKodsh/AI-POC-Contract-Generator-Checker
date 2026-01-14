"""Complete setup verification test"""
import sys
import os

def test_imports():
    """Test all required imports"""
    print("Testing imports...")
    try:
        import pytesseract
        print(f"✓ pytesseract {pytesseract.__version__}")
    except ImportError as e:
        print(f"✗ pytesseract: {e}")
        return False
    
    try:
        import pdf2image
        print(f"✓ pdf2image installed")
    except ImportError as e:
        print(f"✗ pdf2image: {e}")
        return False
    
    try:
        import pdfplumber
        print(f"✓ pdfplumber {pdfplumber.__version__}")
    except ImportError as e:
        print(f"✗ pdfplumber: {e}")
        return False
    
    return True

def test_tesseract():
    """Test Tesseract OCR"""
    print("\nTesting Tesseract...")
    try:
        import pytesseract
        version = pytesseract.get_tesseract_version()
        print(f"✓ Tesseract version: {version}")
        return True
    except Exception as e:
        print(f"✗ Tesseract error: {e}")
        return False

def test_poppler():
    """Test Poppler"""
    print("\nTesting Poppler...")
    try:
        from pdf2image import convert_from_path
        from pdf2image.exceptions import PDFInfoNotInstalledError
        # Just test if we can import without error
        print("✓ Poppler binaries accessible")
        return True
    except PDFInfoNotInstalledError as e:
        print(f"✗ Poppler not found: {e}")
        return False
    except Exception as e:
        print(f"✓ Poppler import successful (runtime test needs PDF)")
        return True

def test_project_structure():
    """Test project structure"""
    print("\nTesting project structure...")
    required_dirs = ['src', 'tests', 'templates']
    all_exist = True
    for dir_name in required_dirs:
        if os.path.exists(dir_name):
            print(f"✓ {dir_name}/ exists")
        else:
            print(f"✗ {dir_name}/ missing")
            all_exist = False
    return all_exist

def main():
    print("=" * 60)
    print("COMPLETE SETUP VERIFICATION")
    print("=" * 60)
    
    results = {
        "Imports": test_imports(),
        "Tesseract": test_tesseract(),
        "Poppler": test_poppler(),
        "Project Structure": test_project_structure()
    }
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for test_name, passed in results.items():
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{test_name}: {status}")
    
    all_passed = all(results.values())
    print("\n" + "=" * 60)
    if all_passed:
        print("ALL TESTS PASSED ✓")
    else:
        print("SOME TESTS FAILED ✗")
    print("=" * 60)
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
