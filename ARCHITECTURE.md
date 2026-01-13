# AI-Proposal Engine Architecture: Simplified POC

This document outlines the architectural decisions for the Simplified Proof of Concept (POC) as discussed by the BMAD team (Winston, Cloud Dragonborn, and Morgan).

## Architectural Principles

### 1. Schema-First Design (Winston's Principle)
To avoid "throwaway" code, we define a strict **JSON Schema** for the data interface between the parser and the generator. This ensures that:
- The Parser can be upgraded (e.g., from simple regex/rule-based to complex AI/OCR) without breaking the Generator.
- The Generator can be tested with mock data that adheres to the schema.
- We have a clear "contract" for what technical information is required to generate a proposal.

### 2. State Management via ProposalContext (Cloud's Principle)
Instead of passing raw dictionaries, the system uses a `ProposalContext` object (the "Game Loop State").
- **Update**: The Parser populates the `ProposalContext`.
- **Process**: The Knowledge Base Query enriches the `ProposalContext` with engineering standards.
- **Render**: The Generator uses the `ProposalContext` to fill templates.
- **Benefit**: This allows for state persistence, easy debugging, and re-runnable generation cycles.

### 3. Modular Scaffolding (Morgan's Principle)
The project structure is designed to be a reusable module that can grow into the full system.

```text
src/
  ├── models/      # Data schemas (Pydantic) and the ProposalContext state object.
  ├── parser/      # Logic for extracting data from input PDF/DOCX.
  ├── knowledge/   # The static knowledge base (JSON for POC, Vector DB later).
  └── generator/   # Logic for rendering templates (python-docx-template).
```

## Data Flow (The "Game Loop")

1. **Load**: Read input document (PDF/DOCX).
2. **Parse (Update)**: Extract key entities (Project Name, Client, Location, Scope Items) into the `ProposalContext`.
3. **Enrich (Process)**: Use the Knowledge Base to find relevant technical standards or glossaries for the identified Scope.
4. **Generate (Render)**: Merge the enriched `ProposalContext` with a Word template to produce the final document.

## Implementation Path

- **Week 1**: Define `ProposalContext` schema; Build basic Parser and Knowledge lookup.
- **Week 2**: Build Template Generator and basic Validation layer.
