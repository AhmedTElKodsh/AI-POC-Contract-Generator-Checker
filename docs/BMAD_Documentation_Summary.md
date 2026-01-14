# BMAD Method: Documentation & Research Summary

This document provides a comprehensive overview of the **Breakthrough Method for Agile AI-Driven Development (BMAD)**, based on the latest documentation and Version 6 (Alpha) updates.

---

## 🚀 1. Core Philosophy: "Architecture-First"

BMAD is designed to move beyond basic AI chat interactions by implementing a structured, engineering-first approach.

- **Context Engineering:** Prevents "context pollution" by restricting AI access to only the necessary files and instructions for a specific step.
- **Modular Architecture:** In V6, the method shifts to an "Architecture-First" model where implementation stories are derived from a finalized technical blueprint.

---

## 🤖 2. Agents & Subagents

The framework utilizes a ecosystem of 21+ specialized agents.

### **Core Agent Roles**

- **Analyst (Mary):** Product discovery and market research.
- **Product Manager (John):** PRD creation and story mapping.
- **Architect (Winston):** Technical decision-making and ADR (Architecture Decision Record) management.
- **Scrum Master (Bob):** Sprint orchestration and progress tracking.
- **Developer (Amelia):** Feature implementation and code reviews.
- **Test Architect (TEA/Murat):** Quality assurance and automated test framework setup.
- **Solo Dev (Barry):** Optimized for rapid, end-to-end development in "Quick Flow" mode.

### **Subagents (Tiny Agents)**

Subagents are transient, highly specialized AI instances triggered by core agents to handle granular tasks like:

- Generating unit tests for a specific function.
- Running terminal commands and interpreting logs.
- Formatting documentation.

---

## 🔄 3. The 4-Phase Lifecycle

BMAD guides projects through a predictable, high-quality workflow:

1.  **Phase 1: Analysis:** Brainstorming, Research, and Product Briefing.
2.  **Phase 2: Planning:** PRDs, Requirements, and User Stories.
3.  **Phase 3: Solutioning:** Technical Architecture, ADRs, and Implementation Readiness.
4.  **Phase 4: Implementation:** Sprint Planning, Feature Development, and Code Reviews.

**Special Modes:**

- **Quick Flow:** A streamlined `tech-spec → dev → review` cycle for faster delivery.
- **Party Mode:** Multi-agent collaborative sessions for complex problem-solving.

---

## 📂 4. Version 6 Updates ("The Future is Now")

V6 represents a significant architectural evolution:

- **Unified Agent Workflow:** A single, consolidated flow for creating and managing agents.
- **Sidecar Memory:** Agents now use specialized "sidecar" folders to maintain persistent knowledge across different project stages.
- **Astro/Starlight Docs:** Migration to the Diataxis documentation framework for improved clarity.
- **Sharded Workflows:** Modular workflow components that provide better performance and easier updates.

---

## 🛠️ 5. BMAD App Builder (BoMB)

The **BMAD Builder Module** allows users to extend the framework:

- **Custom Agent Creation:** Author agents using a YAML-to-XML compilation process.
- **Expansion Packs:** Create non-software modules (e.g., Content Creation, Business Strategy).
- **Module Sharing:** Package custom workflows and tools for distribution within teams.

---

## 🔗 Related Links

- **[Official Documentation](https://docs.bmad-method.org/)** - Core tutorials and conceptual guides.
- **[GitHub Repository](https://github.com/bmad-code-org/BMAD-METHOD)** - Main source code, issue tracker, and V6 updates.
- **[Full Documentation (Text)](https://docs.bmad-method.org/llms-full.txt)** - A single-file summary optimized for AI context windows.
- **[Installation Guide](https://docs.bmad-method.org/how-to/installation/quick-start/)** - How to get BMAD running in your project.
- **[Agent Roles Overview](https://docs.bmad-method.org/explanation/core-concepts/agent-roles/)** - Detailed descriptions of every specialized agent.

---

## 🛠️ Agent Mapping by 4-Phase Lifecycle

This section maps specific BMAD agents to the structural phases of development.

### **Phase 1: Analysis (Discovery & Ideation)**

- **bmm-analyst**: Core lead for product discovery and mission definition.
- **cis-brainstorming-coach**: Facilitates initial creative ideation.
- **cis-creative-problem-solver**: Breaks through technical or strategic blockers.
- **cis-design-thinking-coach**: Applies human-centered design frameworks.
- **cis-innovation-strategist**: Analyzes market disruption and strategy.
- **cis-storyteller**: Crafts the product narrative and vision.

### **Phase 2: Planning (Requirements & UX)**

- **bmm-pm (Product Manager)**: Owns the PRD and decomposes vision into stories.
- **bmm-ux-designer**: Designs the user experience and interface blueprints.
- **bmgd-game-designer**: Specialized lead for Game Design Documents (GDD).

### **Phase 3: Solutioning (Architecture & Spec)**

- **bmm-architect**: Core lead for technical architecture and ADRs.
- **bmgd-game-architect**: Specialized lead for game systems and engine selection.
- **bmm-tech-writer**: Produces technical specs and documentation.

### **Phase 4: Implementation (Dev, QA & Ops)**

- **bmm-sm (Scrum Master)** / **bmgd-game-scrum-master**: Orchestrates the sprint and task flow.
- **bmm-dev** / **bmgd-game-dev**: Executes code implementation and peer reviews.
- **bmm-tea** / **bmgd-game-qa**: Owns automated testing and quality gates.
- **cis-presentation-master**: Used at project completion for stakeholder reporting.

---

### **Specialized Agents**

- **The Orchestrator:** **core-bmad-master** (Guides you through the entire method).
- **The Solo/POC Flow:** **bmm-quick-flow-solo-dev** / **bmgd-game-solo-dev** (Combined Phases 3 & 4).
- **Framework Builders:** **bmb-agent-builder**, **bmb-module-builder**, **bmb-workflow-builder** (Used to build BMAD itself).
