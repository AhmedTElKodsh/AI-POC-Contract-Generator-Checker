# Appendix: Architectural Illustrations and Explanations

This document serves as a repository for deep-dive explanations and illustrations of the architectural patterns used in the AI-Proposal Engine project.

## 1. The "Review & Approve" 3-Phase UI Architecture

This pattern was established during the transition from CLI to Streamlit GUI to ensure that the "Human-in-the-Loop" (HITL) is deeply integrated with the RAG (Retrieval-Augmented Generation) process.

### Phase 1: The "Truth" Foundation (Ingestion)
*   **Goal**: Establish a trusted baseline of project metadata.
*   **Logic**: 
    1.  The `PDFParser` extracts raw text and attempts to identify entities (Project Name, Client, etc.).
    2.  The UI displays these values in editable fields.
*   **HITL Action**: The user verifies and corrects any parsing errors. This ensures the "System of Record" is accurate before any expensive RAG or Generation steps occur.

### Phase 2: The "Brain" Check (Enrichment)
*   **Goal**: Validate the AI's semantic reasoning and knowledge retrieval.
*   **Logic**:
    1.  The system takes the *verified* Scope from Phase 1.
    2.  It queries the `SimpleKnowledgeBase` (RAG Engine) to find relevant engineering terms and references.
    3.  The UI displays these findings (Glossary Terms, Standards).
*   **HITL Action**: The user curates the list. They can uncheck irrelevant terms or add missing ones. This prevents "AI Hallucinations" or irrelevant technical filler from entering the final proposal.

### Phase 3: The "Seal" (Generation)
*   **Goal**: Finalize and produce the technical artifact.
*   **Logic**:
    1.  The fully curated and verified `ProposalContext` is passed to the `SimpleGenerator`.
    2.  The Word template is rendered using only the human-approved data.
*   **Outcome**: A "clean" document that requires significantly less manual post-processing, as the data was sanitized upstream.

---

## 2. The "Game Loop" Document Pipeline
*   **Concept**: Treating document processing as a state-driven loop (Update -> Process -> Render).
*   **Implementation**: Use of a central `ProposalContext` object that maintains state throughout the lifecycle, allowing for "Save/Load" and "Debug" capabilities at any stage.
