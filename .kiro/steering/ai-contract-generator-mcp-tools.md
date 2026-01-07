---
inclusion: fileMatch
fileMatchPattern: "**/ai-contract-generator/**"
---

# MCP Tools for AI Contract Generator & Compliance Checker

Project-specific MCP tools guidance for building the AI Contract Generation & Compliance Checker POC.

## Primary Tools for This Project

### Sequential Thinking (Complex Analysis)

Use for:

- Designing compliance checking algorithms
- Planning RAG-enhanced clause analysis workflows
- Debugging semantic similarity issues
- Architecting the Ollama Cloud fallback mechanism

```
Tool: mcp_sequential_thinking_sequentialthinking
When: Multi-step reasoning, architecture decisions, debugging complex flows
```

### Research Tools

**Exa Code Context** - Use for implementation patterns:

- Sentence Transformers usage examples
- Ollama Python client patterns
- Streamlit/Gradio form handling
- python-docx template generation
- Property-based testing with Hypothesis

```
Tool: mcp_exa_get_code_context_exa
Queries:
- "sentence-transformers semantic similarity python"
- "ollama python client chat completion"
- "streamlit form validation python"
- "python-docx template generation"
- "hypothesis property-based testing python"
```

**Exa Web Search** - Use for documentation:

- Ollama Cloud API documentation
- Sentence Transformers model selection
- Streamlit deployment options

```
Tool: mcp_exa_web_search_exa
```

### Hugging Face Tools

**Model Search** - Find embedding models:

```
Tool: mcp_hf_mcp_server_model_search
Queries:
- task: "sentence-similarity" for embedding models
- query: "legal document" for domain-specific models
- query: "all-MiniLM" for lightweight options
```

**Documentation Search** - Transformers/Sentence-Transformers docs:

```
Tool: mcp_hf_mcp_server_hf_doc_search
product: "sentence-transformers"
```

### GitHub Tools

**Code Search** - Find implementation examples:

```
Tool: mcp_github_search_code
Queries:
- "sentence-transformers compliance check"
- "ollama client fallback python"
- "contract clause similarity"
- "python-docx template"
```

**Repository Search** - Find reference projects:

```
Tool: mcp_github_search_repositories
Queries:
- "contract compliance python"
- "legal document nlp"
- "ollama rag python"
```

## Project-Specific Patterns

### Semantic Similarity Implementation

1. Use `mcp_exa_get_code_context_exa` for Sentence Transformers patterns
2. Use `mcp_hf_mcp_server_model_search` to compare embedding models
3. Use `mcp_sequential_thinking_sequentialthinking` for threshold tuning logic

### Ollama Integration

1. Use `mcp_exa_web_search_exa` for Ollama Cloud API docs
2. Use `mcp_exa_get_code_context_exa` for Python client examples
3. Use `mcp_sequential_thinking_sequentialthinking` for fallback logic design

### Compliance Checking Logic

1. Use `mcp_sequential_thinking_sequentialthinking` for algorithm design
2. Use `mcp_github_search_code` for similar implementations
3. Use `mcp_exa_get_code_context_exa` for NLP extraction patterns

### Property-Based Testing

1. Use `mcp_exa_get_code_context_exa` for Hypothesis examples
2. Use `mcp_sequential_thinking_sequentialthinking` for property definition

### Export Functionality

1. Use `mcp_exa_get_code_context_exa` for python-docx patterns
2. Use `mcp_github_search_code` for DOCX template examples

## Quick Reference

| Task                        | Primary Tool               | Query/Action                       |
| --------------------------- | -------------------------- | ---------------------------------- |
| Design compliance algorithm | sequential-thinking        | Multi-step analysis                |
| Find ST code examples       | exa_get_code_context       | "sentence-transformers similarity" |
| Ollama client patterns      | exa_get_code_context       | "ollama python chat completion"    |
| Compare embedding models    | hf_model_search            | task: "sentence-similarity"        |
| Find contract NLP repos     | github_search_repositories | "contract nlp python"              |
| Streamlit form patterns     | exa_get_code_context       | "streamlit form validation"        |
| DOCX generation             | exa_get_code_context       | "python-docx template"             |
| Hypothesis testing          | exa_get_code_context       | "hypothesis property test"         |

## Best Practices

1. **Start with Sequential Thinking** for complex design decisions
2. **Combine tools** - Use web search to find docs, then code context for examples
3. **Verify patterns** - Cross-reference GitHub examples with official docs
4. **Cache research** - Document useful patterns found for team reference
5. **Model selection** - Use HF tools to compare embedding model performance
