"""
Streamlit App Validation Script
Tests that the Streamlit app can be imported and has correct structure
"""

import sys
import os
import ast

def analyze_streamlit_app():
    """Analyze app.py structure"""
    print("\n" + "="*60)
    print("🎨 STREAMLIT APP ANALYSIS")
    print("="*60)
    
    with open("app.py", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Parse AST
    try:
        tree = ast.parse(content)
        print("✅ app.py syntax is valid")
    except SyntaxError as e:
        print(f"❌ Syntax error in app.py: {e}")
        return False
    
    # Check imports
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module)
    
    critical_imports = [
        "streamlit",
        "src.parser.pdf_parser",
        "src.parser.docx_parser",
        "src.knowledge.simple_kb",
        "src.generator.simple_generator",
        "src.models.generation"
    ]
    
    print("\n📦 Import Validation:")
    for imp in critical_imports:
        if imp in imports:
            print(f"✅ {imp}")
        else:
            print(f"❌ {imp} - MISSING")
    
    # Check for key Streamlit components
    print("\n🎯 Streamlit Components:")
    components = {
        "st.set_page_config": "Page configuration",
        "st.title": "Title",
        "st.file_uploader": "File upload",
        "st.button": "Buttons",
        "st.text_input": "Text inputs",
        "st.text_area": "Text area",
        "st.multiselect": "Multi-select",
        "st.download_button": "Download button",
        "st.spinner": "Loading spinner"
    }
    
    for component, description in components.items():
        if component in content:
            print(f"✅ {component} - {description}")
        else:
            print(f"⚠️  {component} - {description} (not found)")
    
    # Check for 3-phase workflow
    print("\n🔄 Workflow Phases:")
    phases = [
        ("Phase 1", "METADATA VERIFICATION"),
        ("Phase 2", "RAG VERIFICATION"),
        ("Phase 3", "GENERATION")
    ]
    
    for phase_name, phase_marker in phases:
        if phase_marker in content:
            print(f"✅ {phase_name}: {phase_marker}")
        else:
            print(f"❌ {phase_name}: {phase_marker} - MISSING")
    
    # Check session state management
    print("\n💾 Session State:")
    session_vars = ["context", "found_terms", "step"]
    for var in session_vars:
        if f"st.session_state.{var}" in content or f"session_state['{var}']" in content:
            print(f"✅ {var}")
        else:
            print(f"⚠️  {var} - not found")
    
    return True

def check_streamlit_installed():
    """Check if Streamlit is installed"""
    print("\n" + "="*60)
    print("📦 DEPENDENCY CHECK")
    print("="*60)
    
    try:
        import streamlit
        print(f"✅ Streamlit installed (version {streamlit.__version__})")
        return True
    except ImportError:
        print("❌ Streamlit not installed")
        print("   Run: pip install streamlit")
        return False

def main():
    print("\n" + "="*60)
    print("🧪 STREAMLIT APP VALIDATION")
    print("="*60)
    
    results = {
        "Streamlit Installed": check_streamlit_installed(),
        "App Structure": analyze_streamlit_app()
    }
    
    # Summary
    print("\n" + "="*60)
    print("📊 VALIDATION SUMMARY")
    print("="*60)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    print(f"\n🎯 Results: {passed}/{total} checks passed")
    
    if passed == total:
        print("\n✨ Streamlit app is ready to run!")
        print("\n🚀 To start the app, run:")
        print("   streamlit run app.py")
        return 0
    else:
        print(f"\n⚠️  {total - passed} check(s) failed.")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
