# 🔬 Deep Research Report: Open-Source Libraries for Civil Engineering AI Proposal Generator

**Date:** January 8, 2026  
**Purpose:** Comprehensive catalog of open-source tools for building an AI Engine to generate engineering proposals and technical reports

---

## Executive Summary

This report catalogs open-source libraries and tools discovered through deep research across GitHub, web sources, and code repositories. The tools are organized by functional layers required for the AI Engine development plan.

**Key Findings:**

- Strong ecosystem exists for HEC-RAS/SWMM automation via Python
- Arabic NLP has matured significantly with CAMeL Tools and AraBERT leading
- RAGFlow and LlamaIndex are top choices for document-based RAG systems
- python-docx-template is the go-to for proposal generation from templates

---

## 1️⃣ HYDRAULIC ENGINEERING & MODELING

### HEC-RAS Integration

| Library           | GitHub                                                                          | Stars | Description                                                              | Use Case                                    |
| ----------------- | ------------------------------------------------------------------------------- | ----- | ------------------------------------------------------------------------ | ------------------------------------------- |
| **RAS-Commander** | [gpt-cmdr/ras-commander](https://github.com/gpt-cmdr/ras-commander)             | 15    | Python API for HEC-RAS 6.x automation + HDF data access, built with LLMs | Automate flood modeling, extract results    |
| **pyHMT2D**       | [psu-efd/pyHMT2D](https://github.com/psu-efd/pyHMT2D)                           | -     | 2D Hydraulics Modeling Tools - supports HEC-RAS & SRH-2D                 | Parametric studies, Monte Carlo simulations |
| **raspy**         | [quantum-dan/raspy](https://github.com/quantum-dan/raspy)                       | 47    | Python interface for HEC-RAS                                             | Simulation automation                       |
| **rascontrol**    | [mikebannis/rascontrol](https://github.com/mikebannis/rascontrol)               | 89    | Python wrapper for HEC-RAS controller (win32com)                         | Legacy HEC-RAS control                      |
| **parserasgeo**   | [mikebannis/parserasgeo](https://github.com/mikebannis/parserasgeo)             | 47    | Import/export HEC-RAS geometry files                                     | Geometry manipulation                       |
| **pandss**        | [CentralValleyModeling/pandss](https://github.com/CentralValleyModeling/pandss) | 5     | Unified HEC-DSS Library for Python                                       | Time-series data management                 |

### Stormwater/Drainage Modeling

| Library          | GitHub/URL                                                                                  | Description                                            | Use Case                           |
| ---------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ---------------------------------- |
| **PySWMM**       | [pyswmm.org](https://www.pyswmm.org/)                                                       | Python interface to EPA SWMM for stormwater modeling   | Drainage design, real-time control |
| **swmm_api**     | [PyPI](https://pypi.org/project/swmm-api/)                                                  | Python package for SWMM automation & visualization     | Urban drainage modeling            |
| **SWMManywhere** | [ImperialCollegeLondon/SWMManywhere](https://github.com/ImperialCollegeLondon/SWMManywhere) | Derive & simulate sewer networks anywhere in the world | Rapid drainage network generation  |

### Installation

```bash
pip install ras-commander pyswmm swmm-api
```

---

## 2️⃣ RAG FRAMEWORKS (Document Retrieval & Generation)

| Library              | GitHub                                                                    | Stars | Description                                | Best For                    |
| -------------------- | ------------------------------------------------------------------------- | ----- | ------------------------------------------ | --------------------------- |
| **RAGFlow**          | [infiniflow/ragflow](https://github.com/infiniflow/ragflow)               | 25K+  | Deep document understanding RAG engine     | Complex PDF/DOCX processing |
| **R2R (SciPhi-AI)**  | [SciPhi-AI/R2R](https://github.com/SciPhi-AI/R2R)                         | 7.6K  | Production-ready agentic RAG with REST API | Enterprise deployment       |
| **LlamaIndex**       | [run-llama/llama_index](https://github.com/run-llama/llama_index)         | 35K+  | Data framework for LLM applications        | Document indexing, querying |
| **LangChain**        | [langchain-ai/langchain](https://github.com/langchain-ai/langchain)       | 90K+  | Framework for LLM-powered applications     | Chain orchestration         |
| **Verba (Weaviate)** | [weaviate/verba](https://github.com/weaviate/verba)                       | 5K+   | Modular open-source RAG application        | Quick RAG prototyping       |
| **LightRAG**         | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)                       | 8K+   | Simple & fast RAG implementation           | Lightweight deployments     |
| **TrustRAG**         | [gomate-community/TrustRAG](https://github.com/gomate-community/TrustRAG) | -     | Hybrid retrieval + reranking               | High-accuracy retrieval     |

### Recommended Choice

**RAGFlow** - Best for your use case due to:

- Deep document understanding for complex engineering PDFs
- Built-in table extraction
- Template-based chunking
- Multi-format support (PDF, DOCX, XLSX)

### Installation

```bash
pip install llama-index langchain ragflow
```

---

## 3️⃣ ARABIC NLP LIBRARIES

> **Critical for your bilingual corpus (Arabic/English proposals and reports)**

| Library         | GitHub/URL                                                                                   | Stars | Description                          | Key Features                              |
| --------------- | -------------------------------------------------------------------------------------------- | ----- | ------------------------------------ | ----------------------------------------- |
| **CAMeL Tools** | [CAMeL-Lab/camel_tools](https://github.com/CAMeL-Lab/camel_tools)                            | 511   | NYU Abu Dhabi Arabic NLP suite       | Tokenization, POS, dialect ID, morphology |
| **SinaTools**   | [sina.birzeit.edu/sinatools](https://sina.birzeit.edu/sinatools)                             | -     | Comprehensive Arabic NLP toolkit     | Lemmatization (90.5%), POS (93.8%), WSD   |
| **Maha**        | [TRoboto/Maha](https://github.com/TRoboto/Maha)                                              | 202   | Arabic text processing library       | Cleaning, parsing, streaming              |
| **Yarub**       | [Omdena Project](https://www.omdena.com/blog/building-yarub-library-for-arabic-nlp-purposes) | -     | Open-source Arabic NLP library       | Sentiment, NER, POS tagging               |
| **anltk**       | [Abdullah-AlAttar/anltk](https://github.com/Abdullah-AlAttar/anltk)                          | 21    | Arabic NLP Toolkit                   | Basic Arabic processing                   |
| **AraT5**       | [UBC-NLP/araT5](https://github.com/UBC-NLP/araT5)                                            | 93    | Text-to-Text Transformers for Arabic | Generation, summarization                 |
| **Farasa**      | [farasa.qcri.org](https://farasa.qcri.org/)                                                  | -     | Arabic text processing toolkit       | Segmentation, diacritization              |

### Arabic Transformer Models (HuggingFace)

| Model          | HuggingFace ID                   | Use Case                    |
| -------------- | -------------------------------- | --------------------------- |
| **AraBERT v2** | `aubmindlab/bert-base-arabertv2` | Embeddings, classification  |
| **MARBERT**    | `UBC-NLP/MARBERT`                | Dialect-aware embeddings    |
| **AraGPT2**    | `aubmindlab/aragpt2-base`        | Arabic text generation      |
| **AraELECTRA** | `aubmindlab/araelectra-base`     | Efficient Arabic embeddings |

### Installation

```bash
pip install camel-tools sinatools maha transformers
```

### Usage Example (CAMeL Tools)

```python
from camel_tools.morphology.analyzer import Analyzer
from camel_tools.tokenizers.word import simple_word_tokenize

# Tokenize Arabic text
text = "ذهب الولد إلى المدرسة"
tokens = simple_word_tokenize(text)

# Morphological analysis
analyzer = Analyzer.builtin_analyzer()
analyses = analyzer.analyze(tokens[0])
```

---

## 4️⃣ PDF/DOCUMENT PROCESSING

| Library            | GitHub                                                                            | Description                            | Best For                 |
| ------------------ | --------------------------------------------------------------------------------- | -------------------------------------- | ------------------------ |
| **LlamaParse**     | [run-llama/llama_parse](https://github.com/run-llama/llama_parse)                 | Cloud PDF parser with table extraction | Complex engineering PDFs |
| **pymupdf4llm**    | [pymupdf/RAG](https://github.com/pymupdf/RAG)                                     | PDF to Markdown converter              | Fast local processing    |
| **Docling**        | [DS4SD/docling](https://github.com/DS4SD/docling)                                 | IBM's document understanding           | Structured extraction    |
| **OpenParse**      | [Filimoa/open-parse](https://github.com/Filimoa/open-parse)                       | Document parsing with table detection  | Engineering tables       |
| **PPStructureV3**  | [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)               | PaddleOCR's document structure         | Arabic OCR support       |
| **DeepDoctection** | [deepdoctection/deepdoctection](https://github.com/deepdoctection/deepdoctection) | Layout analysis pipeline               | Complex document layouts |
| **gmft**           | [conjuncts/gmft](https://github.com/conjuncts/gmft)                               | Table detection & extraction           | BOQ tables               |
| **Agentic-Doc**    | [landing-ai/agentic-doc](https://github.com/landing-ai/agentic-doc)               | AI-powered document parsing            | Multi-format extraction  |
| **OCRFlux**        | [chatdoc-com/OCRFlux](https://github.com/chatdoc-com/OCRFlux)                     | PDF document processing pipeline       | Scanned documents        |

### Recommended for Engineering Documents

1. **pymupdf4llm** - Fast, local, good for text-heavy PDFs
2. **OpenParse** - Excellent table detection for BOQs
3. **PPStructureV3** - Best Arabic OCR support

### Installation

```bash
pip install pymupdf4llm open-parse paddleocr llama-parse
```

### Usage Example (pymupdf4llm)

```python
import pymupdf4llm

# Convert PDF to Markdown
md_text = pymupdf4llm.to_markdown("hydrological_report.pdf")

# Save as file
with open("output.md", "w", encoding="utf-8") as f:
    f.write(md_text)
```

---

## 5️⃣ DOCUMENT GENERATION (Proposal Templates)

| Library                  | GitHub                                                                            | Stars | Description                          | Use Case                   |
| ------------------------ | --------------------------------------------------------------------------------- | ----- | ------------------------------------ | -------------------------- |
| **python-docx-template** | [elapouya/python-docx-template](https://github.com/elapouya/python-docx-template) | 2.4K  | Jinja2 templates in DOCX             | Proposal generation        |
| **Carbone**              | [carboneio/carbone](https://github.com/carboneio/carbone)                         | 1.9K  | JSON to PDF/DOCX/ODT generator       | Report automation          |
| **LOTemplate**           | [Probesys/lotemplate](https://github.com/Probesys/lotemplate)                     | 44    | LibreOffice-based document generator | ODT/DOCX/PDF output        |
| **python-docx**          | [python-openxml/python-docx](https://github.com/python-openxml/python-docx)       | 4K+   | Create/modify Word documents         | Programmatic DOCX creation |
| **WeasyPrint**           | [Kozea/WeasyPrint](https://github.com/Kozea/WeasyPrint)                           | 6K+   | HTML/CSS to PDF                      | Styled PDF reports         |

### Recommended: python-docx-template

Best for your use case - allows creating Word templates with Jinja2 tags that can be filled programmatically.

### Installation

```bash
pip install docxtpl python-docx weasyprint
```

### Usage Example

```python
from docxtpl import DocxTemplate

# Load template
doc = DocxTemplate("proposal_template.docx")

# Define context (from RAG system or database)
context = {
    'project_name': "Hydrological Study - Ras El Hekma",
    'client_name': "Ministry of Housing",
    'scope_items': [
        "Catchment delineation",
        "Flood frequency analysis",
        "Drainage design"
    ],
    'total_cost': "1,500,000 EGP",
    'duration': "6 months"
}

# Render and save
doc.render(context)
doc.save("generated_proposal.docx")
```

---

## 6️⃣ VECTOR DATABASES (For RAG Storage)

| Database     | GitHub                                                      | Type           | Best For                         | Notes               |
| ------------ | ----------------------------------------------------------- | -------------- | -------------------------------- | ------------------- |
| **Qdrant**   | [qdrant/qdrant](https://github.com/qdrant/qdrant)           | Open-source    | Cost-sensitive, edge deployments | Rust-based, fast    |
| **Weaviate** | [weaviate/weaviate](https://github.com/weaviate/weaviate)   | Open-source    | Hybrid search, modularity        | GraphQL API         |
| **Milvus**   | [milvus-io/milvus](https://github.com/milvus-io/milvus)     | Open-source    | Billion-scale vectors            | Industrial strength |
| **Chroma**   | [chroma-core/chroma](https://github.com/chroma-core/chroma) | Open-source    | Prototyping, small apps          | Developer-friendly  |
| **pgvector** | [pgvector/pgvector](https://github.com/pgvector/pgvector)   | PostgreSQL ext | Existing Postgres infra          | Simple integration  |
| **Pinecone** | [pinecone.io](https://www.pinecone.io/)                     | Managed        | Zero-ops, fast prototyping       | Serverless          |

### Comparison Summary (2025)

| Feature       | Qdrant    | Weaviate  | Milvus   | Chroma    | Pinecone  |
| ------------- | --------- | --------- | -------- | --------- | --------- |
| Self-hosted   | ✅        | ✅        | ✅       | ✅        | ❌        |
| Managed cloud | ✅        | ✅        | ✅       | ✅        | ✅        |
| Hybrid search | ✅        | ✅        | ✅       | ❌        | ✅        |
| Filtering     | Excellent | Excellent | Good     | Basic     | Good      |
| Scale         | Millions  | Millions  | Billions | Thousands | Millions  |
| Ease of use   | High      | Medium    | Low      | Very High | Very High |

### Recommended: Qdrant

- Best balance of performance, features, and ease of deployment
- Excellent filtering for metadata (project type, date, client)
- Self-hosted option for data privacy

### Installation

```bash
pip install qdrant-client
# Or run with Docker
docker run -p 6333:6333 qdrant/qdrant
```

---

## 7️⃣ RECOMMENDED ARCHITECTURE

```
┌─────────────────────────────────────────────────────────────────┐
│                    DOCUMENT INGESTION LAYER                      │
├─────────────────────────────────────────────────────────────────┤
│  Arabic PDFs → PPStructureV3 (OCR) → pymupdf4llm → Markdown     │
│  English PDFs → LlamaParse / OpenParse → Structured JSON        │
│  DOCX → python-docx → Text extraction                           │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    NLP PROCESSING LAYER                          │
├─────────────────────────────────────────────────────────────────┤
│  Arabic Text → CAMeL Tools (morphology) → AraBERT (embeddings)  │
│  English Text → sentence-transformers → embeddings              │
│  Technical Terms → Custom engineering ontology                   │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    KNOWLEDGE BASE LAYER                          │
├─────────────────────────────────────────────────────────────────┤
│  Vector Store: Qdrant (self-hosted) or Weaviate                 │
│  Metadata: PostgreSQL (project info, costs, timelines)          │
│  Engineering Data: HEC-RAS results, SWMM outputs                │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    RAG & GENERATION LAYER                        │
├─────────────────────────────────────────────────────────────────┤
│  Framework: LlamaIndex or RAGFlow                               │
│  LLM: Claude 3.5 / GPT-4 (Arabic support)                       │
│  Templates: python-docx-template (DOCX) + WeasyPrint (PDF)      │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    ENGINEERING VALIDATION                        │
├─────────────────────────────────────────────────────────────────┤
│  Hydraulic Checks: RAS-Commander + PySWMM                       │
│  Unit Validation: Custom Python validators                       │
│  Cost Estimation: Historical data regression models              │
└─────────────────────────────────────────────────────────────────┘
```

---

## 8️⃣ IMPLEMENTATION ROADMAP

### Phase 1: Quick Wins (Weeks 1-4)

```bash
# Core dependencies
pip install docxtpl pymupdf4llm camel-tools llama-index qdrant-client openai
```

**Deliverables:**

- [ ] Index existing 14 proposals/reports into Qdrant
- [ ] Create 3 proposal templates with Jinja2 tags
- [ ] Build basic RAG query interface

### Phase 2: Arabic NLP Integration (Weeks 5-8)

```bash
pip install transformers torch arabert
```

**Deliverables:**

- [ ] Arabic text preprocessing pipeline
- [ ] Bilingual embedding model integration
- [ ] Dialect-aware text normalization

### Phase 3: Engineering Integration (Weeks 9-12)

```bash
pip install pyswmm ras-commander swmm-api
```

**Deliverables:**

- [ ] HEC-RAS result extraction automation
- [ ] Hydraulic calculation validator
- [ ] Cost estimation model from historical data

### Phase 4: Production Deployment (Weeks 13-16)

**Deliverables:**

- [ ] FastAPI backend with REST endpoints
- [ ] React frontend with RTL Arabic support
- [ ] Docker containerization
- [ ] CI/CD pipeline

---

## 9️⃣ KEY RESOURCES & DOCUMENTATION

### Official Documentation

- [LlamaIndex Docs](https://docs.llamaindex.ai/)
- [CAMeL Tools Docs](https://camel-tools.readthedocs.io/)
- [Qdrant Docs](https://qdrant.tech/documentation/)
- [python-docx-template Docs](https://docxtpl.readthedocs.io/)
- [PySWMM Docs](https://pyswmm.readthedocs.io/)
- [HEC-RAS Documentation](https://www.hec.usace.army.mil/software/hec-ras/documentation.aspx)

### Research Papers

- AraBERT: [arxiv.org/abs/2003.00104](https://arxiv.org/abs/2003.00104)
- RAG Survey: [arxiv.org/abs/2312.10997](https://arxiv.org/abs/2312.10997)

### Community Resources

- [Arabic NLP Observatory (AUB)](https://sites.aub.edu.lb/arabicnlp/tools/)
- [Open Water Analytics](https://github.com/OpenWaterAnalytics)

---

## 🔟 CONCLUSION

This research identifies a robust ecosystem of open-source tools that can be combined to build your AI Engine for civil engineering proposal generation. The key recommendations are:

1. **RAG Framework:** LlamaIndex or RAGFlow
2. **Arabic NLP:** CAMeL Tools + AraBERT
3. **Document Processing:** pymupdf4llm + OpenParse
4. **Document Generation:** python-docx-template
5. **Vector Database:** Qdrant (self-hosted)
6. **Engineering Integration:** RAS-Commander + PySWMM

The bilingual (Arabic/English) nature of your documents is the primary technical challenge - prioritize Arabic NLP integration early in development.

---

_Report generated from deep research using Exa, GitHub, and web sources_
