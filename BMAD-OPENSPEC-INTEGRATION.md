# BMAD + OpenSpec Integration Guide

**Framework Strategy**: BMAD-METHOD (Primary) + OpenSpec (Supplementary)

This document explains how to use both frameworks together for the AI Engine development.

---

## Why This Combination?

### BMAD-METHOD (Primary)

- **Scale-adaptive tracks** match your 5-phase development plan
- **21 specialized agents** for different engineering tasks
- **Guided workflows** for complex multi-component systems
- **Brownfield support** for working with existing documents

### OpenSpec (Supplementary)

- **Delta-based tracking** for evolving specifications
- **Change proposals** for cross-cutting modifications
- **Multi-tool support** (works with all AI assistants)
- **Lightweight process** without heavy ceremony

---

## Framework Mapping

| Development Phase              | BMAD Track            | OpenSpec Usage                                         |
| ------------------------------ | --------------------- | ------------------------------------------------------ |
| **Phase 1: Data Analysis**     | Quick Flow (~5 min)   | Track document structure templates as specs            |
| **Phase 2: Knowledge Base**    | BMad Method (~15 min) | Proposal for vector DB schema, ontology design         |
| **Phase 3: NLP Pipeline**      | BMad Method           | Proposals for Arabic NLP integration, embedding models |
| **Phase 4: Generation System** | BMad Method           | Proposals for template engine, BOQ generation          |
| **Phase 5: Integration**       | Enterprise (~30 min)  | Proposals for API design, deployment architecture      |

---

## Daily Workflow

### Starting a New Feature

```bash
# 1. Activate BMAD Master Agent
# In your AI assistant, run:
/bmad-master

# 2. Choose appropriate track based on complexity
# Quick Flow: Bug fixes, small tasks
# BMad Method: New features, structured development
# Enterprise: API design, deployment, compliance

# 3. For significant changes, create OpenSpec proposal
openspec list --specs  # Check existing specs
# Then ask AI: "Create an OpenSpec proposal for [feature]"

# 4. Implement using BMAD workflows
# BMAD guides you through implementation steps

# 5. Archive OpenSpec change when complete
openspec archive <change-id> --yes
```

---

## Integration Patterns

### Pattern 1: Phase-Level Specs (OpenSpec)

Each development phase has a corresponding spec:

```
openspec/specs/
├── document-ingestion/
│   ├── spec.md          # Requirements for PDF/DOCX processing
│   └── design.md        # Architecture decisions
├── arabic-nlp-pipeline/
│   ├── spec.md          # Arabic text processing requirements
│   └── design.md        # CAMeL Tools + AraBERT integration
├── knowledge-base/
│   ├── spec.md          # Vector DB, metadata storage
│   └── design.md        # Qdrant schema, indexing strategy
├── rag-generation/
│   ├── spec.md          # RAG retrieval + LLM generation
│   └── design.md        # LlamaIndex configuration
└── engineering-validation/
    ├── spec.md          # HEC-RAS/SWMM integration
    └── design.md        # Validation pipeline
```

### Pattern 2: Feature-Level Changes (OpenSpec)

When adding features within a phase:

```
openspec/changes/
├── add-geotechnical-templates/
│   ├── proposal.md      # Why: Support geotechnical proposals
│   ├── tasks.md         # Implementation checklist
│   └── specs/
│       └── rag-generation/
│           └── spec.md  # ADDED: Geotechnical template requirements
└── optimize-arabic-embeddings/
    ├── proposal.md      # Why: Improve Arabic retrieval accuracy
    ├── tasks.md
    └── specs/
        └── arabic-nlp-pipeline/
            └── spec.md  # MODIFIED: Embedding model selection
```

### Pattern 3: BMAD Task → OpenSpec Proposal

When BMAD workflow identifies a complex task:

```
BMAD Task: "Integrate HEC-RAS result extraction"
    ↓
OpenSpec Proposal: "add-hec-ras-integration"
    ↓
BMAD Implementation: Execute tasks from proposal
    ↓
OpenSpec Archive: Mark complete, update specs
```

---

## Practical Examples

### Example 1: Adding Arabic OCR Support

**Step 1: BMAD Quick Flow** (Exploratory)

```
You: /bmad-master
BMAD: [Shows menu]
You: I want to explore Arabic OCR options for scanned PDFs
BMAD: [Guides research using RAS-Commander pattern]
```

**Step 2: OpenSpec Proposal** (Once approach is clear)

```bash
# AI creates proposal
openspec/changes/add-arabic-ocr/
├── proposal.md
│   ## Why
│   Scanned Arabic PDFs need OCR before text extraction
│
│   ## What Changes
│   - Add PPStructureV3 (PaddleOCR) for Arabic OCR
│   - Integrate with document ingestion pipeline
│   - Add OCR quality validation
│
├── tasks.md
│   ## 1. Setup
│   - [ ] 1.1 Install PaddleOCR dependencies
│   - [ ] 1.2 Download Arabic OCR models
│
│   ## 2. Integration
│   - [ ] 2.1 Create OCR preprocessing stage
│   - [ ] 2.2 Add quality validation
│   - [ ] 2.3 Update pipeline configuration
│
└── specs/document-ingestion/spec.md
    ## ADDED Requirements
    ### Requirement: Arabic OCR Processing
    The system SHALL extract text from scanned Arabic PDFs.

    #### Scenario: Scanned proposal processing
    - **WHEN** a scanned Arabic PDF is uploaded
    - **THEN** text is extracted with >90% accuracy
```

**Step 3: BMAD Method Implementation**

```
You: /bmad-method
BMAD: [Guides through implementation]
You: Implement tasks from openspec/changes/add-arabic-ocr/tasks.md
BMAD: [Executes each task with validation]
```

**Step 4: Archive**

```bash
openspec archive add-arabic-ocr --yes
# Moves to archive/, updates specs/document-ingestion/spec.md
```

---

### Example 2: Cross-Cutting Change (Multiple Specs)

**Scenario**: Switching from OpenAI to Claude for better Arabic support

**OpenSpec Proposal**:

```
openspec/changes/switch-to-claude/
├── proposal.md
│   ## Why
│   Claude 3.5 has better Arabic language understanding
│
│   ## What Changes
│   - **BREAKING**: Replace OpenAI API with Anthropic Claude
│   - Update prompt templates for Claude format
│   - Modify cost estimation (different pricing)
│
│   ## Impact
│   - Affected specs: rag-generation, arabic-nlp-pipeline
│   - Affected code: src/llm/, src/generation/
│
├── tasks.md
│   ## 1. API Migration
│   - [ ] 1.1 Add anthropic Python package
│   - [ ] 1.2 Create Claude API wrapper
│   - [ ] 1.3 Update environment variables
│
│   ## 2. Prompt Engineering
│   - [ ] 2.1 Convert OpenAI prompts to Claude format
│   - [ ] 2.2 Test Arabic generation quality
│   - [ ] 2.3 Update prompt templates
│
├── design.md
│   ## Context
│   OpenAI GPT-4 struggles with Arabic technical terminology.
│   Claude 3.5 shows 15% better accuracy in tests.
│
│   ## Decisions
│   - Use Claude 3.5 Sonnet (balance of cost/quality)
│   - Keep OpenAI as fallback for high-load periods
│   - Implement retry logic with exponential backoff
│
└── specs/
    ├── rag-generation/spec.md
    │   ## MODIFIED Requirements
    │   ### Requirement: LLM Integration
    │   The system SHALL use Claude 3.5 for proposal generation.
    │   [Full updated requirement with scenarios]
    │
    └── arabic-nlp-pipeline/spec.md
        ## MODIFIED Requirements
        ### Requirement: Arabic Text Generation
        [Updated for Claude-specific Arabic handling]
```

**BMAD Execution**:

```
You: /bmad-enterprise
BMAD: [Enterprise track for breaking changes]
You: Execute migration from openspec/changes/switch-to-claude/
BMAD: [Guides through tasks with validation gates]
```

---

## When to Use Each Framework

### Use BMAD Alone

- ✅ Bug fixes (restore intended behavior)
- ✅ Quick experiments (trying libraries)
- ✅ Refactoring without behavior changes
- ✅ Documentation updates

### Use OpenSpec Alone

- ✅ Spec clarifications (no code changes)
- ✅ Requirement updates (before implementation)
- ✅ Design decisions (architecture docs)

### Use Both Together

- ✅ New features (OpenSpec proposal → BMAD implementation)
- ✅ Breaking changes (OpenSpec tracks impact → BMAD executes)
- ✅ Cross-cutting changes (OpenSpec deltas → BMAD workflows)
- ✅ Phase transitions (OpenSpec specs → BMAD tracks)

---

## Quality Gates

### Before Starting Implementation

- [ ] OpenSpec proposal created and validated
- [ ] BMAD track selected (Quick/Method/Enterprise)
- [ ] Affected specs identified
- [ ] Tasks broken down in tasks.md

### During Implementation

- [ ] BMAD workflow guides each step
- [ ] Tests written for each task
- [ ] Engineering validation passes (HEC-RAS/SWMM checks)
- [ ] Arabic NLP quality validated

### After Implementation

- [ ] All tasks.md items marked complete
- [ ] OpenSpec validation passes (`--strict`)
- [ ] BMAD quality checks complete
- [ ] Change archived to OpenSpec

---

## Troubleshooting

### "Which framework should I use?"

**Decision Tree**:

```
Is this a new feature or breaking change?
├─ Yes → Create OpenSpec proposal first
│   └─ Then use BMAD for implementation
└─ No → Is it complex (>1 hour)?
    ├─ Yes → Use BMAD workflow
    └─ No → Fix directly
```

### "OpenSpec and BMAD specs conflict"

**Resolution**:

1. OpenSpec specs are **requirements** (what to build)
2. BMAD specs are **implementation plans** (how to build)
3. Keep them in sync: OpenSpec proposal → BMAD tasks

### "Too much process overhead"

**Simplification**:

- Phase 1-2: Use BMAD Quick Flow + minimal OpenSpec
- Phase 3-4: Add OpenSpec proposals for major features
- Phase 5: Full process for production deployment

---

## File Organization

```
project-root/
├── openspec/                    # Requirements & specs
│   ├── project.md              # Project context (THIS FILE)
│   ├── specs/                  # Current truth
│   └── changes/                # Proposed changes
│
├── _bmad/                      # BMAD workflows
│   ├── core/                   # Core BMAD system
│   ├── bmm/                    # BMad Method workflows
│   └── _memory/                # Session memory
│
├── src/                        # Implementation
│   ├── ingestion/              # Document processing
│   ├── nlp/                    # Arabic NLP pipeline
│   ├── knowledge_base/         # Vector DB integration
│   ├── generation/             # Proposal generation
│   └── validation/             # Engineering checks
│
├── tests/                      # Test suite
├── docs/                       # Documentation
└── AI-Engine-Research-Report.md  # Library research
```

---

## Quick Reference

### BMAD Commands

```bash
/bmad-master          # Start BMAD Master Agent
/bmad-quick-flow      # Quick tasks (<5 min)
/bmad-method          # Structured development (~15 min)
/bmad-enterprise      # Production deployment (~30 min)
```

### OpenSpec Commands

```bash
openspec list                    # List active changes
openspec list --specs            # List specifications
openspec show <item>             # View details
openspec validate <item> --strict  # Validate
openspec archive <change-id> --yes  # Archive completed
```

### Integration Commands

```bash
# Create proposal from BMAD task
openspec list --specs            # Check existing
# Ask AI: "Create OpenSpec proposal for [BMAD task]"

# Execute OpenSpec proposal with BMAD
/bmad-method
# Tell BMAD: "Implement openspec/changes/<change-id>/"

# Archive after BMAD completion
openspec archive <change-id> --yes
```

---

## Success Metrics

Track these to ensure frameworks are helping, not hindering:

| Metric                           | Target  | Framework                    |
| -------------------------------- | ------- | ---------------------------- |
| Time to first working feature    | <1 week | BMAD Quick Flow              |
| Spec-to-code alignment           | >90%    | OpenSpec validation          |
| Cross-cutting change tracking    | 100%    | OpenSpec deltas              |
| Engineering validation pass rate | >95%    | BMAD QA workflows            |
| Arabic NLP accuracy              | >90%    | Both (spec + implementation) |

---

## Next Steps

1. **Populate OpenSpec specs** for each phase:

   ```bash
   # Ask AI to create initial specs
   "Create OpenSpec specs for Phase 1: Data Analysis based on
    AI-Engine-Research-Report.md"
   ```

2. **Start BMAD Quick Flow** for Phase 1:

   ```bash
   /bmad-master
   # Select Quick Flow track
   # Begin document analysis tasks
   ```

3. **Create first OpenSpec proposal** when ready:

   ```bash
   # After exploring in BMAD, formalize with OpenSpec
   "Create OpenSpec proposal for document structure templates"
   ```

4. **Iterate**: Use BMAD for execution, OpenSpec for tracking changes

---

**Remember**:

- BMAD = How to build (workflows, agents, execution)
- OpenSpec = What to build (specs, requirements, changes)
- Together = Structured vibe coding with traceability
