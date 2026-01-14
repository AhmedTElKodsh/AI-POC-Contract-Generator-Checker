# Quick Start Guide: AI Engine Development

**Project**: Civil Engineering Proposal Generator  
**Frameworks**: BMAD-METHOD (Primary) + OpenSpec (Supplementary)  
**Status**: ✅ Both frameworks initialized and configured

---

## 🚀 Getting Started (Next 30 Minutes)

### Step 1: Verify Setup (5 minutes)

```bash
# Check BMAD installation
ls _bmad/core/

# Check OpenSpec installation
openspec list

# Verify AI tools configured
ls .claude/commands/
ls .antigravity/workflows/
ls .gemini/commands/
```

**Expected Output**: You should see BMAD directories and OpenSpec commands for multiple AI tools.

---

### Step 2: Populate Project Context (10 minutes)

The project context has been pre-populated in `openspec/project.md`. Review it:

```bash
# Read the context
cat openspec/project.md

# Or ask your AI assistant:
"Please review openspec/project.md and confirm you understand
 the project scope, tech stack, and constraints"
```

**Key Points to Verify**:

- ✅ 5 engineering disciplines covered
- ✅ Bilingual (Arabic/English) requirements
- ✅ 14 existing documents to process
- ✅ 5-phase development plan

---

### Step 3: Create Initial Specs (15 minutes)

Create OpenSpec specifications for each development phase:

**Ask your AI assistant**:

```
"Based on AI-Engine-Research-Report.md and openspec/project.md,
 create OpenSpec specifications for all 5 development phases:

 1. document-ingestion (Phase 1)
 2. knowledge-base (Phase 2)
 3. arabic-nlp-pipeline (Phase 3)
 4. rag-generation (Phase 4)
 5. engineering-validation (Phase 5)

 Each spec should include requirements and scenarios."
```

**Expected Structure**:

```
openspec/specs/
├── document-ingestion/
│   ├── spec.md
│   └── design.md
├── knowledge-base/
│   ├── spec.md
│   └── design.md
├── arabic-nlp-pipeline/
│   ├── spec.md
│   └── design.md
├── rag-generation/
│   ├── spec.md
│   └── design.md
└── engineering-validation/
    ├── spec.md
    └── design.md
```

---

## 📋 Phase 1: Data Analysis & Preparation (Weeks 1-4)

### Objective

Analyze 14 existing proposals/reports and create document structure templates.

### Using BMAD Quick Flow

```bash
# Start BMAD Master Agent
# In your AI assistant:
/bmad-master

# Or for Claude Code:
/bmad:master

# Select from menu:
[PM] Start Party Mode  # For exploratory analysis
```

**Tasks for Phase 1**:

1. **Document Analysis**

   ```
   "Analyze the 14 existing proposals/reports in the corpus.
    Categorize by:
    - Project type (structural, geotechnical, etc.)
    - Complexity level
    - Document structure patterns"
   ```

2. **Template Creation**

   ```
   "Create document structure templates for:
    - Hydrological studies
    - Feasibility reports
    - Technical proposals
    - BOQ (Bill of Quantities)"
   ```

3. **Metadata Tagging**
   ```
   "Design metadata schema for:
    - Engineering concepts
    - Project requirements
    - Client information
    - Cost/timeline data"
   ```

### Creating OpenSpec Proposal

When you identify a specific feature to build:

```bash
# Example: Document structure templates
"Create an OpenSpec proposal for document-structure-templates
 that will standardize how we parse and categorize proposals"
```

**Expected Output**:

```
openspec/changes/add-document-templates/
├── proposal.md
├── tasks.md
└── specs/document-ingestion/spec.md
```

---

## 🗄️ Phase 2: Knowledge Base Development (Weeks 5-8)

### Objective

Index 14 documents into Qdrant, build engineering ontology, create regulatory database.

### Using BMAD Method Track

```bash
# Start BMAD with Method track
/bmad-master
# Select: [LW] List Workflows
# Choose: Knowledge Base Development workflow
```

### Key Tasks

1. **Vector Database Setup**

   ```bash
   # Install Qdrant
   docker run -p 6333:6333 qdrant/qdrant

   # Create OpenSpec proposal
   "Create proposal for qdrant-integration with schema design
    for engineering documents"
   ```

2. **Document Indexing**

   ```python
   # Libraries from AI-Engine-Research-Report.md
   pip install qdrant-client pymupdf4llm camel-tools

   # Ask AI:
   "Implement document indexing pipeline using:
    - pymupdf4llm for PDF extraction
    - CAMeL Tools for Arabic preprocessing
    - Qdrant for vector storage"
   ```

3. **Engineering Ontology**
   ```
   "Create engineering ontology covering:
    - 5 disciplines (Structural, Geotechnical, etc.)
    - Technical terminology (Arabic/English)
    - Regulatory standards
    - Material specifications"
   ```

### OpenSpec Workflow

```bash
# Create proposal
"Create OpenSpec proposal for engineering-ontology"

# Implement with BMAD
/bmad-method
"Implement tasks from openspec/changes/add-engineering-ontology/"

# Archive when complete
openspec archive add-engineering-ontology --yes
```

---

## 🔤 Phase 3: NLP Pipeline (Weeks 9-12)

### Objective

Build Arabic/English text processing pipeline with embeddings.

### Critical: Arabic NLP Integration

This is your **highest risk area**. Start early!

```bash
# Install Arabic NLP tools
pip install camel-tools transformers torch

# Test with actual documents
"Test CAMeL Tools and AraBERT on our 14 Arabic documents.
 Report accuracy and issues."
```

### Using BMAD Method + OpenSpec

1. **Create Proposal**

   ```
   "Create OpenSpec proposal for arabic-nlp-integration covering:
    - CAMeL Tools for morphology
    - AraBERT for embeddings
    - Dialect handling (Egyptian, Gulf, Levantine)
    - Technical term extraction"
   ```

2. **Implement Pipeline**

   ```bash
   /bmad-method
   "Implement Arabic NLP pipeline from proposal"
   ```

3. **Validate Quality**
   ```
   "Run validation tests on Arabic text extraction.
    Target: >90% accuracy on technical terminology"
   ```

---

## 🤖 Phase 4: Multi-Modal Generation (Weeks 13-16)

### Objective

Template-based proposal generation with BOQ automation.

### Using BMAD Method Track

```bash
# Install generation tools
pip install docxtpl python-docx weasyprint

# Create proposal
"Create OpenSpec proposal for proposal-generation-system covering:
 - python-docx-template integration
 - Jinja2 template design
 - BOQ table generation
 - Cross-reference validation"
```

### Template Development

```python
# Example template structure
from docxtpl import DocxTemplate

doc = DocxTemplate("templates/proposal_template.docx")

context = {
    'project_name': "{{ project_name }}",
    'client_name': "{{ client_name }}",
    'scope_items': "{{ scope_items }}",
    'total_cost': "{{ total_cost }}",
    'duration': "{{ duration }}"
}

doc.render(context)
doc.save("generated_proposal.docx")
```

**Ask AI**:

```
"Create proposal templates for:
 1. Hydrological studies
 2. Structural design proposals
 3. Geotechnical reports

 Each with Jinja2 tags for dynamic content"
```

---

## 🔧 Phase 5: Integration & Deployment (Weeks 17-20)

### Objective

FastAPI backend, React frontend, Docker deployment.

### Using BMAD Enterprise Track

```bash
# Start enterprise track for production deployment
/bmad-master
# Select: Enterprise track

# Create comprehensive proposal
"Create OpenSpec proposal for production-deployment covering:
 - FastAPI REST API design
 - React frontend with RTL Arabic support
 - Docker containerization
 - CI/CD pipeline with GitHub Actions
 - Monitoring and logging"
```

### API Design

```python
# FastAPI structure
from fastapi import FastAPI, UploadFile
from pydantic import BaseModel

app = FastAPI()

class ProposalRequest(BaseModel):
    project_type: str
    client_name: str
    scope: list[str]
    language: str  # "ar" or "en"

@app.post("/generate-proposal")
async def generate_proposal(request: ProposalRequest):
    # RAG retrieval + LLM generation
    pass

@app.post("/upload-document")
async def upload_document(file: UploadFile):
    # Document ingestion pipeline
    pass
```

---

## 🎯 Daily Workflow Examples

### Scenario 1: Adding a New Feature

```bash
# 1. Check existing specs
openspec list --specs

# 2. Create proposal
"Create OpenSpec proposal for add-transportation-templates"

# 3. Validate proposal
openspec validate add-transportation-templates --strict

# 4. Implement with BMAD
/bmad-method
"Implement openspec/changes/add-transportation-templates/"

# 5. Archive when done
openspec archive add-transportation-templates --yes
```

---

### Scenario 2: Bug Fix (No Proposal Needed)

```bash
# Use BMAD Quick Flow
/bmad-master
# Select: Quick Flow

"Fix Arabic text encoding issue in PDF extraction"
# BMAD guides you through fix
```

---

### Scenario 3: Cross-Cutting Change

```bash
# Example: Switching embedding model

# 1. Create proposal with impact analysis
"Create OpenSpec proposal for switch-to-multilingual-e5 covering:
 - Impact on arabic-nlp-pipeline
 - Impact on knowledge-base (re-indexing needed)
 - Impact on rag-generation (retrieval changes)
 - Migration plan"

# 2. Review design.md for technical decisions
cat openspec/changes/switch-to-multilingual-e5/design.md

# 3. Execute with BMAD Enterprise (breaking change)
/bmad-enterprise
"Execute migration from proposal"

# 4. Archive
openspec archive switch-to-multilingual-e5 --yes
```

---

## 📊 Progress Tracking

### Weekly Checklist

**Week 1-4 (Phase 1)**:

- [ ] 14 documents analyzed and categorized
- [ ] Document structure templates created
- [ ] Metadata schema designed
- [ ] OpenSpec specs created for all phases

**Week 5-8 (Phase 2)**:

- [ ] Qdrant running and configured
- [ ] 14 documents indexed with embeddings
- [ ] Engineering ontology built (5 disciplines)
- [ ] Regulatory compliance database created

**Week 9-12 (Phase 3)**:

- [ ] CAMeL Tools integrated
- [ ] AraBERT embeddings working
- [ ] Arabic text accuracy >90%
- [ ] Technical term extraction validated

**Week 13-16 (Phase 4)**:

- [ ] python-docx-template integrated
- [ ] 3+ proposal templates created
- [ ] BOQ generation automated
- [ ] Cross-reference validation working

**Week 17-20 (Phase 5)**:

- [ ] FastAPI backend deployed
- [ ] React frontend with RTL
- [ ] Docker containers built
- [ ] CI/CD pipeline active

---

## 🆘 Troubleshooting

### "I'm not sure which framework to use"

**Quick Decision Tree**:

```
Is this a new feature or breaking change?
├─ Yes → OpenSpec proposal + BMAD implementation
└─ No → Is it complex (>1 hour)?
    ├─ Yes → BMAD workflow
    └─ No → Fix directly
```

### "Arabic NLP isn't working"

```bash
# Test CAMeL Tools installation
python -c "from camel_tools.tokenizers.word import simple_word_tokenize; print('OK')"

# Test AraBERT
python -c "from transformers import AutoModel; print('OK')"

# Ask AI for help
"Debug Arabic text processing issue. Test with sample text:
 'ذهب المهندس إلى موقع البناء'"
```

### "OpenSpec validation failing"

```bash
# Run strict validation
openspec validate <change-id> --strict

# Check JSON output for details
openspec show <change-id> --json --deltas-only

# Common issues:
# - Scenarios must use #### (4 hashtags)
# - Every requirement needs at least one scenario
# - Delta operations must be ADDED/MODIFIED/REMOVED
```

---

## 📚 Key Resources

### Documentation

- **BMAD**: `_bmad/core/README.md`
- **OpenSpec**: `openspec/AGENTS.md`
- **Integration**: `BMAD-OPENSPEC-INTEGRATION.md`
- **Libraries**: `AI-Engine-Research-Report.md`

### Commands Reference

```bash
# BMAD
/bmad-master              # Start BMAD
/bmad-quick-flow          # Quick tasks
/bmad-method              # Structured dev
/bmad-enterprise          # Production

# OpenSpec
openspec list             # Active changes
openspec list --specs     # Specifications
openspec validate --strict  # Validate
openspec archive <id> --yes  # Archive
```

---

## ✅ Success Criteria

You'll know you're on track when:

1. **Week 4**: All 14 documents categorized, templates created
2. **Week 8**: Documents indexed in Qdrant, ontology built
3. **Week 12**: Arabic NLP accuracy >90% on test documents
4. **Week 16**: Can generate a complete proposal from templates
5. **Week 20**: Production system deployed and accessible

---

## 🎉 Next Actions

**Right Now** (next 10 minutes):

```bash
# 1. Verify setup
openspec list
ls _bmad/core/

# 2. Start BMAD
# In your AI assistant:
/bmad-master

# 3. Begin Phase 1
"Let's start Phase 1: Data Analysis.
 Analyze the 14 existing documents and create categorization."
```

**This Week**:

- [ ] Complete document analysis
- [ ] Create structure templates
- [ ] Design metadata schema
- [ ] Create OpenSpec specs for all phases

**Next Week**:

- [ ] Set up Qdrant vector database
- [ ] Begin document indexing
- [ ] Start engineering ontology

---

**Remember**:

- Start with BMAD Quick Flow for exploration
- Create OpenSpec proposals for features
- Use BMAD Method for implementation
- Archive changes when complete

**You're ready to build! 🚀**
