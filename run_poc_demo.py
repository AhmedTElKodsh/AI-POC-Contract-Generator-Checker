import os
import sys

# Ensure the project root is in the Python path so imports work
sys.path.append(os.getcwd())

from src.parser.simple_parser import SimpleParser
from src.parser.pdf_parser import PDFParser
from src.knowledge.simple_kb import SimpleKnowledgeBase
from src.generator.simple_generator import SimpleGenerator
from src.models.generation import ProposalContext

def run_demo():
    """
    Orchestrates the Simplified POC "Game Loop".
    
    Flow:
    1. Input: Select a real PDF file from the 'Reports' directory.
    2. UPDATE: Parse that PDF into a structured ProposalContext state object.
    3. PROCESS: Enrich that state object by looking up terms in the Knowledge Base.
    4. RENDER: Generate a final .docx proposal from the enriched state.
    """
    
    # --- PREPARATION: Select Input Data ---
    # We use a real file now, as per Cloud Dragonborn's request.
    input_path = "Reports/Final Design of Drainage System Report.pdf"
    
    # Fallback if file doesn't exist (for safety in new envs)
    if not os.path.exists(input_path):
        print(f"⚠️ Test PDF not found at {input_path}. Falling back to text file.")
        input_path = "tmp/sample_request.txt"
        use_pdf = False
    else:
        use_pdf = True

    print(f"--- [INPUT] Using input file: {input_path} ---")

    # --- STEP 1: PARSE (The 'Update' Loop) ---
    print("\n--- [STEP 1] Parsing Document ---")
    
    if use_pdf:
        print("Using PDFParser (pymupdf4llm)...")
        parser = PDFParser()
    else:
        print("Using SimpleParser (Regex)...")
        parser = SimpleParser()
        
    try:
        context = parser.parse_file(input_path)
    except Exception as e:
        print(f"❌ Critical Error parsing file: {e}")
        return
    
    print(f"✅ Extracted Project: {context.project_name}")
    print(f"✅ Extracted Client:  {context.client}")
    scope_val = context.sections.get('scope', 'N/A')
    print(f"✅ Extracted Scope (First 500 chars): {repr(scope_val[:500])}")

    # --- STEP 2: ENRICH (The 'Process' Loop) ---
    print("\n--- [STEP 2] Enriching with Knowledge Base ---")
    kb = SimpleKnowledgeBase()
    
    scope_text = context.sections.get("scope", "")
    enriched_terms = kb.search_terms(scope_text)
    
    if enriched_terms:
        print(f"✅ Found {len(enriched_terms)} glossary terms: {list(enriched_terms.keys())}")
    else:
        print("⚠️ No glossary terms found. (Check matching logic or input text)")

    context.metadata["glossary"] = enriched_terms
    
    # Also fetch standard references
    refs = kb.get_references("hydrological")
    context.metadata["references"] = refs
    print(f"✅ Added {len(refs)} standard technical references.")

    # --- STEP 3: GENERATE (The 'Render' Loop) ---
    print("\n--- [STEP 3] Generating Proposal Document ---")
    generator = SimpleGenerator()
    os.makedirs("proposals", exist_ok=True)
    output_path = "proposals/poc_output_from_pdf.docx"
    
    try:
        generator.generate(context, output_path)
        print(f"🎉 SUCCESS! Proposal generated at: {output_path}")
        print("You can open this file to see the final result.")
    except Exception as e:
        print(f"❌ Error during generation: {e}")

if __name__ == "__main__":
    run_demo()