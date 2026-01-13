import streamlit as st
import os
import sys
import tempfile
from datetime import datetime

# Ensure project modules are importable
sys.path.append(os.getcwd())

from src.parser.pdf_parser import PDFParser
from src.parser.docx_parser import DocxParser
from src.knowledge.simple_kb import SimpleKnowledgeBase
from src.generator.simple_generator import SimpleGenerator
from src.models.generation import ProposalContext

# --- UI CONFIGURATION ---
st.set_page_config(page_title="ICON AI-Proposal Engine", layout="wide", page_icon="🏗️")

st.title("🏗️ ICON AI-Proposal Engine")
st.markdown("""
This tool uses a **3-Phase RAG Workflow** to generate engineering proposals.
1. **Ingest**: Extract data from PDF/DOCX.
2. **Enrich**: Verify Knowledge Base (RAG) results.
3. **Generate**: Create the final Word document.
""")

# --- SESSION STATE INITIALIZATION ---
if 'context' not in st.session_state:
    st.session_state.context = None
if 'found_terms' not in st.session_state:
    st.session_state.found_terms = {}
if 'step' not in st.session_state:
    st.session_state.step = 1

# --- SIDEBAR: FILE UPLOAD ---
with st.sidebar:
    st.header("1. Upload Request")
    uploaded_file = st.file_uploader("Upload Client RFP (PDF or DOCX)", type=["pdf", "docx"])
    
    if uploaded_file:
        if st.button("🚀 Start Processing"):
            # Determine file extension
            file_ext = os.path.splitext(uploaded_file.name)[1].lower()
            
            # Save uploaded bytes to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as tmp:
                tmp.write(uploaded_file.getvalue())
                tmp_path = tmp.name
            
            with st.spinner(f"Parsing {file_ext.upper()}..."):
                try:
                    if file_ext == ".pdf":
                        parser = PDFParser()
                    elif file_ext == ".docx":
                        parser = DocxParser()
                    else:
                        st.error("Unsupported file format.")
                        parser = None

                    if parser:
                        # PHASE 1: Initial Ingestion
                        st.session_state.context = parser.parse_file(tmp_path)
                        st.session_state.step = 1
                        st.success("File Parsed Successfully!")
                except Exception as e:
                    st.error(f"Error parsing file: {e}")
                finally:
                    if os.path.exists(tmp_path):
                        os.unlink(tmp_path) # Clean up

    st.divider()
    if st.button("🧹 Clear All"):
        st.session_state.context = None
        st.session_state.step = 1
        st.rerun()

# --- MAIN UI LOGIC (3 PHASES) ---

if st.session_state.context:
    ctx = st.session_state.context

    # --- PHASE 1: METADATA VERIFICATION ---
    st.header("Phase 1: Verify Extracted Metadata")
    col1, col2 = st.columns(2)
    
    with col1:
        ctx.project_name = st.text_input("Project Name", value=ctx.project_name)
        ctx.client = st.text_input("Client", value=ctx.client)
    with col2:
        ctx.location = st.text_input("Location", value=ctx.location)
        ctx.duration_months = st.number_input("Duration (Months)", value=ctx.duration_months)

    # Use the 'scope' section from the context dictionary
    scope_text = ctx.sections.get("scope", "")
    new_scope = st.text_area("Scope of Work (Edit if needed)", value=scope_text, height=200)
    ctx.sections["scope"] = new_scope

    if st.button("🔍 Step 2: Enrich with Knowledge Base"):
        with st.spinner("Searching Knowledge Base..."):
            kb = SimpleKnowledgeBase()
            # PHASE 2: RAG / Enrichment
            st.session_state.found_terms = kb.search_terms(new_scope)
            ctx.metadata["references"] = kb.get_references("hydrological")
            st.session_state.step = 2
            st.toast("Knowledge Base Queried!")

    st.divider()

    # --- PHASE 2: RAG VERIFICATION ---
    if st.session_state.step >= 2:
        st.header("Phase 2: Verify Technical Knowledge (RAG)")
        st.info("The AI found the following technical terms in your scope. Select the ones you want to include in the glossary.")
        
        all_found = st.session_state.found_terms
        
        if all_found:
            # Multi-select for terms
            selected_term_names = st.multiselect(
                "Confirmed Glossary Terms",
                options=list(all_found.keys()),
                default=list(all_found.keys())
            )
            
            # Filter the glossary based on selection
            curated_glossary = {k: v for k, v in all_found.items() if k in selected_term_names}
            ctx.metadata["glossary"] = curated_glossary
            
            # Show preview
            with st.expander("Preview Definitions"):
                for term, definition in curated_glossary.items():
                    st.write(f"**{term}**: {definition}")
        else:
            st.warning("No specific engineering terms detected in the scope. You can manually add terms in the final document.")

        st.subheader("Technical References")
        refs = ctx.metadata.get("references", [])
        selected_refs = st.multiselect("Standards & Codes to Include", options=refs, default=refs)
        ctx.metadata["references"] = selected_refs

        if st.button("📝 Step 3: Finalize & Generate"):
            st.session_state.step = 3

    st.divider()

    # --- PHASE 3: GENERATION ---
    if st.session_state.step >= 3:
        st.header("Phase 3: Generate Proposal")
        
        output_filename = f"Proposal_{ctx.project_name.replace(' ', '_')}.docx"
        output_path = os.path.join("proposals", output_filename)
        os.makedirs("proposals", exist_ok=True)

        if st.button("🪄 Generate Word Document"):
            with st.spinner("Rendering Template..."):
                generator = SimpleGenerator()
                generator.generate(ctx, output_path)
                
                with open(output_path, "rb") as f:
                    st.download_button(
                        label="💾 Download Generated Proposal",
                        data=f,
                        file_name=output_filename,
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
                st.success(f"Proposal Generated: {output_filename}")

else:
    st.info("Please upload a PDF in the sidebar to begin.")

# --- FOOTER ---
st.divider()
st.caption("BMAD-Powered AI Engine | Civil Engineering Proposal POC v1.0")
