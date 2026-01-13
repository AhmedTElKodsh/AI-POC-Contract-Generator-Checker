import os
import sys

# Ensure project root is in path
sys.path.append(os.getcwd())

from src.parser.pdf_parser import PDFParser
from src.knowledge.simple_kb import SimpleKnowledgeBase
from src.models.generation import ProposalContext

def test_human_in_loop_logic():
    """
    Simulates the logic flow inside the Streamlit app to verify RAG enrichment.
    """
    print("--- [DEBUG] Testing RAG Logic with Simulated Human Intervention ---")
    
    # 1. Simulating PDF Ingestion
    test_pdf = "Reports/Final Design of Drainage System Report.pdf"
    if not os.path.exists(test_pdf):
        print(f"Error: {test_pdf} not found.")
        return

    parser = PDFParser()
    context = parser.parse_file(test_pdf)
    print(f"1. Initial Scope Extracted (Length: {len(context.sections.get('scope', ''))})")

    # 2. Simulating Human Edit
    # We manually add some keywords to the scope to see if the KB picks them up
    simulated_scope = context.sections.get('scope', '') + "\nKeywords: reinforced concrete foundation for abutment and seismic protection."
    context.sections['scope'] = simulated_scope
    print("2. Human Edit: Added 'concrete', 'foundation', 'abutment', 'seismic' to scope.")

    # 3. Simulating RAG Enrichment
    kb = SimpleKnowledgeBase()
    found_terms = kb.search_terms(simulated_scope)
    
    expected_terms = ["Concrete", "Foundation", "Abutment", "Seismic"]
    found_keys = list(found_terms.keys())
    
    print(f"3. RAG Results: Found {len(found_keys)} terms.")
    for term in expected_terms:
        status = "✅" if term in found_keys else "❌"
        print(f"   {status} {term}")

    # 4. Final Verification
    if len(found_keys) >= len(expected_terms):
        print("\n🎉 SUCCESS: The RAG engine correctly enriched the context based on the modified scope.")
    else:
        print("\n⚠️ WARNING: Some terms were missed. Check SimpleKB matching logic.")

if __name__ == "__main__":
    test_human_in_loop_logic()
