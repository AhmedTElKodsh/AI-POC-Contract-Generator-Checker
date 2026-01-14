# Project Context

## Purpose

AI Engine for generating civil engineering proposals and technical reports. The system processes existing proposals/reports (Arabic/English), extracts domain knowledge, and generates new proposals using RAG-based AI with engineering validation.

## Tech Stack

### Core Framework

- **Python 3.11+** - Primary language
- **FastAPI** - Backend API framework
- **React** - Frontend (with RTL Arabic support)

### AI/ML Stack

- **LlamaIndex** - RAG framework for document retrieval
- **AraBERT** - Arabic language embeddings
- **sentence-transformers** - English embeddings
- **OpenAI/Claude API** - LLM for generation

### Document Processing

- **pymupdf4llm** - PDF to Markdown conversion
- **OpenParse** - Table detection for BOQs
- **PPStructureV3 (PaddleOCR)** - Arabic OCR
- **python-docx-template** - Proposal generation from templates

### Arabic NLP

- **CAMeL Tools** - Arabic morphology, tokenization
- **Maha** - Arabic text cleaning and parsing

### Engineering Tools

- **RAS-Commander** - HEC-RAS automation
- **PySWMM** - Stormwater modeling
- **swmm_api** - SWMM automation

### Data Storage

- **Qdrant** - Vector database (self-hosted)
- **PostgreSQL** - Metadata and project info
- **HDF5** - HEC-RAS results storage

## Project Conventions

### Code Style

- **Python**: PEP 8, Black formatter, type hints required
- **Naming**: snake_case for functions/variables, PascalCase for classes
- **Docstrings**: Google style for all public functions
- **Max line length**: 100 characters

### Architecture Patterns

- **Layered Architecture**:

  1. Document Ingestion Layer (PDF/DOCX → structured data)
  2. NLP Processing Layer (Arabic/English → embeddings)
  3. Knowledge Base Layer (Vector DB + metadata)
  4. RAG & Generation Layer (retrieval + LLM)
  5. Engineering Validation Layer (HEC-RAS/SWMM checks)

- **Modular Design**: Each engineering discipline (Structural, Geotechnical, Transportation, Environmental, Construction) has isolated modules
- **Pipeline Pattern**: Document processing uses composable pipeline stages

### Testing Strategy

- **Unit Tests**: pytest for all core functions
- **Integration Tests**: Test document processing pipelines end-to-end
- **Validation Tests**: Engineering calculation validators
- **Arabic NLP Tests**: Test cases with actual Arabic documents
- **Coverage Target**: 80% minimum

### Git Workflow

- **Branching**: feature/[phase-name] for development phases
- **Commits**: Conventional commits (feat:, fix:, docs:, test:)
- **PRs**: Required for all changes, must pass CI/CD
- **Tags**: Version tags for each phase completion

## Domain Context

### Engineering Disciplines

1. **Structural Engineering** - Building design, load calculations
2. **Geotechnical Engineering** - Soil analysis, foundation design
3. **Transportation Engineering** - Road design, traffic analysis
4. **Environmental Engineering** - Water treatment, environmental impact
5. **Construction Engineering** - Project management, cost estimation

### Document Types

- **Proposals**: Technical + financial offers for projects
- **Reports**: Hydrological studies, feasibility studies, design reports
- **BOQs (Bill of Quantities)**: Itemized cost breakdowns
- **Technical Specifications**: Material and method requirements

### Bilingual Requirements

- All documents are Arabic/English bilingual
- Arabic is right-to-left (RTL)
- Technical terms often use English within Arabic text
- Dialect variations in Arabic text (Egyptian, Gulf, Levantine)

### Engineering Standards

- Egyptian Code for Design and Construction
- ASCE standards for hydraulic engineering
- Local government regulations and requirements

## Important Constraints

### Technical Constraints

- **Arabic NLP Complexity**: Morphology, diacritics, dialects
- **Document Quality**: Scanned PDFs may have OCR errors
- **Engineering Validation**: Must verify hydraulic calculations
- **Template Flexibility**: Proposals vary by project type and client

### Business Constraints

- **Data Privacy**: Client proposals are confidential
- **Accuracy Requirements**: Engineering calculations must be validated
- **Regulatory Compliance**: Must meet government standards
- **Cost Estimation**: Historical data may be outdated

### Performance Constraints

- **Response Time**: Proposal generation < 5 minutes
- **Concurrent Users**: Support 10+ simultaneous users
- **Document Size**: Handle PDFs up to 50MB
- **Vector Search**: Sub-second retrieval from 1000+ documents

## External Dependencies

### APIs & Services

- **OpenAI API** - GPT-4 for generation (fallback: Claude)
- **HuggingFace** - AraBERT model hosting
- **HEC-RAS** - Hydraulic modeling software (Windows-based)
- **SWMM** - Stormwater modeling (EPA software)

### Data Sources

- **Existing Corpus**: 14 proposals/reports (Arabic/English)
- **Engineering Standards**: PDF documents of codes/regulations
- **Historical Projects**: Cost and timeline data
- **Client Requirements**: Project-specific specifications

### Infrastructure

- **Docker**: Containerized deployment
- **Qdrant Cloud**: Optional managed vector DB
- **AWS/Azure**: Cloud hosting options
- **GitHub Actions**: CI/CD pipeline

## Development Phases

### Phase 1: Data Analysis & Preparation (Weeks 1-4)

- Analyze 14 existing documents
- Create document structure templates
- Build metadata tagging system

### Phase 2: Knowledge Base Development (Weeks 5-8)

- Index documents into Qdrant
- Build engineering ontology
- Create regulatory compliance database

### Phase 3: NLP Pipeline (Weeks 9-12)

- Arabic text preprocessing
- Bilingual embedding integration
- Technical term extraction

### Phase 4: Multi-Modal Generation (Weeks 13-16)

- Template-based proposal generation
- Automated BOQ generation
- Cross-reference validation

### Phase 5: Integration & Deployment (Weeks 17-20)

- FastAPI backend
- React frontend with RTL
- Docker deployment
- CI/CD pipeline

## Framework Integration

This project uses **BMAD-METHOD** (primary) + **OpenSpec** (supplementary):

- **BMAD**: Guides development through phases with specialized agents
- **OpenSpec**: Tracks spec changes and proposals within each phase
- **Integration**: OpenSpec change proposals map to BMAD tasks

See `_bmad/core/README.md` for BMAD workflows and `openspec/AGENTS.md` for OpenSpec workflow.
