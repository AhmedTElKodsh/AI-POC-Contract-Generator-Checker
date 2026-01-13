# AI Engine for Civil Engineering Proposal Generation

An AI-powered engine for generating technical and financial proposals for civil engineering projects, with specialized support for hydrological studies and infrastructure documentation.

## Overview

This engine uses RAG (Retrieval-Augmented Generation) technology combined with bilingual NLP processing to generate high-quality engineering proposals based on historical project data and domain-specific knowledge bases.

## Simplified POC (Proof of Concept)

We are currently implementing a **Simplified POC** focused on core-essential functionality:
- **Architecture**: Follows a [Schema-First and Modular design](ARCHITECTURE.md) agreed upon by the development team.
- **Goal**: Demonstrate a complete end-to-end flow from input document parsing to formatted proposal generation.
- **Core Loop**: `Input -> Parser -> ProposalContext -> KB Enrichment -> Generator -> Output`.

## Project Structure

```
src/                    # Core engine modules
├── models/            # Data models and enums
├── ingestion/         # Document parsing (PDF, DOCX)
├── nlp/               # Arabic/English NLP processing
├── knowledge_base/    # Vector storage and semantic search
├── rag/               # RAG-based content generation
├── templates/         # Document template rendering
├── validation/        # Engineering calculation validation
└── api/               # REST API endpoints

proposals/             # Sample proposal documents (Arabic/English)
Reports/               # Hydrological study reports and technical docs
templates/             # Document templates for generation
tests/                 # Unit and property-based tests
```

## Key Features

- **Document Ingestion**: Parse PDF and DOCX files with Arabic OCR support
- **Bilingual NLP**: Process Arabic (MSA) and English technical text
- **Knowledge Base**: Semantic search over historical proposals and reports
- **RAG Generation**: Context-aware proposal section generation
- **Template Engine**: Render proposals with dynamic content and tables
- **Hydraulic Validation**: Integration with HEC-RAS and SWMM
- **Cost Estimation**: Historical cost retrieval with inflation adjustment

## Sample Data

### Proposals Directory

Technical and financial proposal documents:

- AIEcon Ras ElHekma technical proposals
- AL AIN DESTINATION infrastructure proposals (Roads, Wet & Dry Utilities)
- NDC Hydroprojects 2025 technical documentation
- Various hydrological study proposals in Arabic

### Reports Directory

Hydrological study reports and drainage system designs:

- Hydrological study reports for Egyptian infrastructure projects
- EET (Egyptian Electric Transmission) sector reports
- Drainage system design reports
- Flood mitigation studies for roads and infrastructure

## Technologies

- **Python 3.11+** with FastAPI, Pydantic
- **Vector DB**: Qdrant for semantic search
- **NLP**: CAMeL Tools (Arabic), sentence-transformers
- **RAG**: LlamaIndex/LangChain with LLM integration
- **Testing**: pytest with Hypothesis (property-based testing)

## Getting Started

```bash
# Install dependencies
pip install -e .

# Run tests
pytest tests/ -v

# Start API server (when implemented)
uvicorn src.api.main:app --reload
```

## Development Status

See `.kiro/specs/ai-engine-proposal-generator/tasks.md` for the detailed implementation plan and current progress.

## License

This project is for demonstration and research purposes.
