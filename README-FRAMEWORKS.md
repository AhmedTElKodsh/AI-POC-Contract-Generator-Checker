# Framework Integration Guide

**Project**: AI Engine for Civil Engineering Proposal Generator  
**Status**: ✅ BMAD-METHOD + OpenSpec Configured  
**Last Updated**: January 11, 2026

---

## 📚 Documentation Index

This project uses **BMAD-METHOD** (primary) + **OpenSpec** (supplementary) for spec-driven development. Here's your complete documentation guide:

### 🎯 Start Here

| Document                                                         | Purpose                                  | Read Time |
| ---------------------------------------------------------------- | ---------------------------------------- | --------- |
| **[QUICK-START-GUIDE.md](QUICK-START-GUIDE.md)**                 | Step-by-step guide to begin development  | 15 min    |
| **[openspec/project.md](openspec/project.md)**                   | Project context, tech stack, conventions | 10 min    |
| **[AI-Engine-Research-Report.md](AI-Engine-Research-Report.md)** | Library research and recommendations     | 30 min    |

### 🔧 Framework Guides

| Document                                                                   | Purpose                               | Read Time |
| -------------------------------------------------------------------------- | ------------------------------------- | --------- |
| **[BMAD-OPENSPEC-INTEGRATION.md](BMAD-OPENSPEC-INTEGRATION.md)**           | How to use both frameworks together   | 20 min    |
| **[FRAMEWORK-COMPARISON-SUMMARY.md](FRAMEWORK-COMPARISON-SUMMARY.md)**     | Detailed comparison of all frameworks | 15 min    |
| **[docs/FRAMEWORK-DECISION-MATRIX.md](docs/FRAMEWORK-DECISION-MATRIX.md)** | Visual decision trees and matrices    | 10 min    |

### 📖 Reference Documentation

| Document                                          | Purpose                        |
| ------------------------------------------------- | ------------------------------ |
| **[openspec/AGENTS.md](openspec/AGENTS.md)**      | OpenSpec workflow and commands |
| **[\_bmad/core/README.md](_bmad/core/README.md)** | BMAD workflows and agents      |

---

## 🚀 Quick Start (5 Minutes)

### 1. Verify Setup

```bash
# Check BMAD
ls _bmad/core/

# Check OpenSpec
openspec list

# Check AI tool configurations
ls .claude/commands/
ls .antigravity/workflows/
ls .gemini/commands/
```

### 2. Start BMAD Master Agent

In your AI assistant (Claude Code, Antigravity, Gemini, etc.):

```bash
/bmad-master
# or
/bmad:master
```

### 3. Begin Phase 1

```
"Let's start Phase 1: Data Analysis.
 Analyze the 14 existing documents and create categorization."
```

---

## 📊 Project Overview

### Development Phases

| Phase                    | Duration    | BMAD Track  | OpenSpec Usage         |
| ------------------------ | ----------- | ----------- | ---------------------- |
| **1. Data Analysis**     | Weeks 1-4   | Quick Flow  | Document templates     |
| **2. Knowledge Base**    | Weeks 5-8   | BMad Method | Vector DB schema       |
| **3. NLP Pipeline**      | Weeks 9-12  | BMad Method | Arabic NLP integration |
| **4. Generation System** | Weeks 13-16 | BMad Method | Template engine        |
| **5. Integration**       | Weeks 17-20 | Enterprise  | API design, deployment |

### Tech Stack Summary

```
Document Processing:  pymupdf4llm, OpenParse, PPStructureV3
Arabic NLP:          CAMeL Tools, AraBERT, Maha
RAG Framework:       LlamaIndex
Vector Database:     Qdrant (self-hosted)
Generation:          python-docx-template
Engineering Tools:   RAS-Commander, PySWMM
Backend:             FastAPI
Frontend:            React (RTL Arabic support)
```

---

## 🎯 Framework Strategy

### Why BMAD-METHOD + OpenSpec?

**BMAD-METHOD** (Primary):

- ✅ Scale-adaptive tracks match your 5 phases
- ✅ 21 specialized agents for different tasks
- ✅ Handles high complexity (AI/ML + Engineering)
- ✅ Strong brownfield support (14 existing documents)
- ✅ Guided workflows for multi-component systems

**OpenSpec** (Supplementary):

- ✅ Delta-based change tracking
- ✅ Lightweight proposals for features
- ✅ Multi-tool support (Claude, Gemini, Antigravity, etc.)
- ✅ Cross-cutting change management
- ✅ Spec evolution tracking

### Daily Workflow

```
1. Start BMAD → Choose track (Quick/Method/Enterprise)
2. For features → Create OpenSpec proposal
3. Implement → BMAD guides through tasks
4. Complete → Archive with OpenSpec
```

---

## 📋 Common Tasks

### Adding a New Feature

```bash
# 1. Check existing specs
openspec list --specs

# 2. Create proposal
"Create OpenSpec proposal for add-geotechnical-templates"

# 3. Validate
openspec validate add-geotechnical-templates --strict

# 4. Implement with BMAD
/bmad-method
"Implement openspec/changes/add-geotechnical-templates/"

# 5. Archive
openspec archive add-geotechnical-templates --yes
```

### Quick Bug Fix

```bash
# Use BMAD Quick Flow (no proposal needed)
/bmad-master
# Select: Quick Flow

"Fix Arabic text encoding issue in PDF extraction"
```

### Cross-Cutting Change

```bash
# Example: Switching LLM provider

# 1. Create proposal with impact analysis
"Create OpenSpec proposal for switch-to-claude covering:
 - Impact on rag-generation
 - Impact on arabic-nlp-pipeline
 - Migration plan"

# 2. Execute with BMAD Enterprise
/bmad-enterprise
"Execute migration from proposal"

# 3. Archive
openspec archive switch-to-claude --yes
```

---

## 🔍 Framework Comparison

### When to Use Each

| Scenario              | Framework                           |
| --------------------- | ----------------------------------- |
| Exploring options     | BMAD Quick Flow                     |
| New feature           | OpenSpec proposal + BMAD Method     |
| Bug fix               | BMAD Quick Flow                     |
| Breaking change       | OpenSpec proposal + BMAD Enterprise |
| Cross-cutting change  | OpenSpec deltas + BMAD Method       |
| Production deployment | BMAD Enterprise                     |

### Why NOT the Others?

**Spec-Kit**: Too rigid for AI/ML exploration, constitution-first delays start  
**Agent-OS**: Not enough structure for complex multi-phase project  
**GSD**: Claude Code only, team needs multi-tool support

---

## 📁 File Organization

```
project-root/
├── openspec/                    # Requirements & specs
│   ├── project.md              # Project context ⭐
│   ├── AGENTS.md               # OpenSpec workflow
│   ├── specs/                  # Current truth
│   │   ├── document-ingestion/
│   │   ├── knowledge-base/
│   │   ├── arabic-nlp-pipeline/
│   │   ├── rag-generation/
│   │   └── engineering-validation/
│   └── changes/                # Proposed changes
│       └── archive/            # Completed changes
│
├── _bmad/                      # BMAD workflows
│   ├── core/                   # Core BMAD system
│   ├── bmm/                    # BMad Method workflows
│   ├── _config/                # Task/workflow manifests
│   └── _memory/                # Session memory
│
├── src/                        # Implementation
│   ├── ingestion/              # Document processing
│   ├── nlp/                    # Arabic NLP pipeline
│   ├── knowledge_base/         # Vector DB integration
│   ├── generation/             # Proposal generation
│   └── validation/             # Engineering checks
│
├── docs/                       # Documentation
│   ├── FRAMEWORK-DECISION-MATRIX.md
│   └── reports/
│
├── tests/                      # Test suite
│
├── QUICK-START-GUIDE.md        # Start here! ⭐
├── BMAD-OPENSPEC-INTEGRATION.md  # Integration guide ⭐
├── FRAMEWORK-COMPARISON-SUMMARY.md  # Detailed comparison
├── AI-Engine-Research-Report.md  # Library research ⭐
└── README-FRAMEWORKS.md        # This file
```

---

## 🎓 Learning Path

### Day 1: Setup & Context (2 hours)

1. ✅ Verify BMAD + OpenSpec installed
2. ✅ Read `openspec/project.md`
3. ✅ Read `QUICK-START-GUIDE.md`
4. ✅ Start BMAD Master Agent

### Week 1: Phase 1 - Data Analysis (Weeks 1-4)

1. Analyze 14 existing documents
2. Create document structure templates
3. Design metadata schema
4. Create OpenSpec specs for all phases

### Week 2-4: Continue Phase 1

1. Refine document categorization
2. Build tagging system
3. Prepare for Phase 2 (Knowledge Base)

### Week 5-8: Phase 2 - Knowledge Base

1. Set up Qdrant vector database
2. Index 14 documents
3. Build engineering ontology
4. Create regulatory database

### Week 9-12: Phase 3 - NLP Pipeline

1. Integrate CAMeL Tools
2. Add AraBERT embeddings
3. Test Arabic accuracy (>90% target)
4. Extract technical terminology

### Week 13-16: Phase 4 - Generation System

1. Integrate python-docx-template
2. Create proposal templates
3. Automate BOQ generation
4. Build cross-reference validation

### Week 17-20: Phase 5 - Integration & Deployment

1. Build FastAPI backend
2. Create React frontend (RTL)
3. Docker containerization
4. CI/CD pipeline

---

## 🔧 Command Reference

### BMAD Commands

```bash
/bmad-master              # Start BMAD Master Agent
/bmad-quick-flow          # Quick tasks (~5 min)
/bmad-method              # Structured development (~15 min)
/bmad-enterprise          # Production deployment (~30 min)

# Menu options
[MH] Menu Help            # Redisplay menu
[CH] Chat                 # Chat with agent
[LT] List Tasks           # Available tasks
[LW] List Workflows       # Available workflows
[PM] Party Mode           # Exploratory mode
[DA] Dismiss Agent        # Exit
```

### OpenSpec Commands

```bash
# Essential
openspec list                    # List active changes
openspec list --specs            # List specifications
openspec show <item>             # View change or spec
openspec validate <item> --strict  # Validate
openspec archive <change-id> --yes  # Archive completed

# Debugging
openspec show <change> --json --deltas-only
openspec validate <change> --strict

# Project management
openspec init [path]             # Initialize OpenSpec
openspec update [path]           # Update instruction files
```

---

## ⚠️ Important Considerations

### Arabic NLP (Highest Risk)

- Start testing CAMeL Tools + AraBERT early
- Create test cases with actual Arabic documents
- Target: >90% accuracy on technical terminology
- Handle dialect variations (Egyptian, Gulf, Levantine)

### Engineering Validation

- HEC-RAS/SWMM integration is critical
- Validate hydraulic calculations
- Cost estimation from historical data
- Regulatory compliance checks

### Document Quality

- Scanned PDFs may have OCR errors
- PPStructureV3 for Arabic OCR
- Quality validation at each stage

### Performance Targets

- Proposal generation: < 5 minutes
- Concurrent users: 10+
- Document size: up to 50MB
- Vector search: sub-second retrieval

---

## 📊 Success Metrics

Track these to ensure frameworks are helping:

| Metric                           | Target   | Framework           |
| -------------------------------- | -------- | ------------------- |
| Time to first feature            | < 1 week | BMAD Quick Flow     |
| Spec-to-code alignment           | > 90%    | OpenSpec validation |
| Cross-cutting change tracking    | 100%     | OpenSpec deltas     |
| Engineering validation pass rate | > 95%    | BMAD QA workflows   |
| Arabic NLP accuracy              | > 90%    | Both frameworks     |
| Phase completion rate            | 100%     | BMAD tracks         |

---

## 🆘 Troubleshooting

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

### "OpenSpec validation failing"

```bash
# Run strict validation
openspec validate <change-id> --strict

# Check JSON output
openspec show <change-id> --json --deltas-only

# Common issues:
# - Scenarios must use #### (4 hashtags)
# - Every requirement needs at least one scenario
# - Delta operations: ADDED/MODIFIED/REMOVED
```

### "BMAD agent not responding"

```bash
# Restart agent
/bmad-master

# Check configuration
cat _bmad/core/config.yaml

# Verify workflows
ls _bmad/_config/
```

### "Arabic NLP not working"

```bash
# Test installation
python -c "from camel_tools.tokenizers.word import simple_word_tokenize; print('OK')"

# Test AraBERT
python -c "from transformers import AutoModel; print('OK')"

# Ask AI for help
"Debug Arabic text processing. Test with: 'ذهب المهندس إلى موقع البناء'"
```

---

## 🎉 Next Actions

**Right Now** (5 minutes):

```bash
# 1. Verify setup
openspec list
ls _bmad/core/

# 2. Start BMAD
/bmad-master

# 3. Begin Phase 1
"Let's start Phase 1: Data Analysis"
```

**This Week**:

- [ ] Complete document analysis
- [ ] Create structure templates
- [ ] Design metadata schema
- [ ] Create OpenSpec specs for all phases

**Next Week**:

- [ ] Set up Qdrant
- [ ] Begin document indexing
- [ ] Start engineering ontology

---

## 📞 Support & Resources

### Documentation

- **BMAD**: `_bmad/core/README.md`
- **OpenSpec**: `openspec/AGENTS.md`
- **Integration**: `BMAD-OPENSPEC-INTEGRATION.md`
- **Libraries**: `AI-Engine-Research-Report.md`

### Community

- **BMAD Discord**: [Join](https://discord.gg/gk8jAdXWmj)
- **OpenSpec Discord**: [Join](https://discord.gg/YctCnvvshC)

### GitHub

- **BMAD**: [github.com/bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD)
- **OpenSpec**: [github.com/Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec)

---

## 📝 Version History

| Version | Date       | Changes                            |
| ------- | ---------- | ---------------------------------- |
| 1.0.0   | 2026-01-11 | Initial setup with BMAD + OpenSpec |

---

**You're ready to build! 🚀**

Start with `QUICK-START-GUIDE.md` and begin Phase 1: Data Analysis.
