# Framework Comparison Summary

Quick reference for choosing between spec-driven development frameworks.

---

## At a Glance

| Framework       | Best For                           | Complexity          | Setup Time | Vibe-Coding Friendly |
| --------------- | ---------------------------------- | ------------------- | ---------- | -------------------- |
| **Spec-Kit**    | Teams, compliance, governance      | Medium-High         | ~15 min    | ⭐⭐                 |
| **OpenSpec**    | Evolving features, change tracking | Low-Medium          | ~5 min     | ⭐⭐⭐               |
| **BMAD-METHOD** | Any scale, guided workflows        | High (configurable) | ~5-30 min  | ⭐⭐⭐ (Quick Flow)  |
| **Agent-OS**    | Established codebases              | Medium              | ~10 min    | ⭐⭐⭐               |
| **GSD**         | Solo devs, rapid prototyping       | Low                 | ~2 min     | ⭐⭐⭐⭐⭐           |

---

## Detailed Comparison

### Spec-Kit (GitHub)

**Philosophy**: Constitution-first governance with 7 sequential phases

**Pros**:

- ✅ Official GitHub backing
- ✅ Clear audit trails
- ✅ Excellent for compliance
- ✅ Branch-per-feature Git integration

**Cons**:

- ❌ Rigid sequential phases
- ❌ Constitution required upfront
- ❌ Overkill for solo developers
- ❌ Weak brownfield support

**When to Use**:

- Teams needing governance
- Projects requiring audit trails
- Greenfield 0→1 development
- Stakeholder justification needed

**When NOT to Use**:

- Quick fixes or hotfixes
- Solo rapid prototyping
- Complex existing codebases

---

### OpenSpec (Fission-AI)

**Philosophy**: Delta-based change tracking with two-folder model

**Pros**:

- ✅ Lightweight but structured
- ✅ Widest AI tool support (15+ tools)
- ✅ Excellent for evolving features
- ✅ Change deltas track modifications
- ✅ AGENTS.md compatible

**Cons**:

- ❌ Strict delta format syntax
- ❌ Less structure for greenfield
- ❌ Requires understanding proposal workflow
- ❌ Telemetry enabled by default

**When to Use**:

- Modifying existing features
- Cross-spec updates
- Multi-tool teams
- Lightweight process preferred

**When NOT to Use**:

- Greenfield 0→1 (less structure)
- Enterprise compliance requirements

---

### BMAD-METHOD

**Philosophy**: Scale-adaptive with 21 specialized agents and 3 tracks

**Pros**:

- ✅ Most comprehensive framework
- ✅ Scale-adaptive (bug fix → enterprise)
- ✅ Specialized agent personas
- ✅ Strong brownfield support
- ✅ Creative Intelligence Suite

**Cons**:

- ❌ Steepest learning curve
- ❌ 21 agents can overwhelm
- ❌ Agent personas require "staying in character"
- ❌ Can feel like "enterprise theater"

**When to Use**:

- Any scale project
- Need guided workflows
- Complex multi-phase projects
- Want specialized agents

**When NOT to Use**:

- Simple projects (overkill)
- Dislike agent personas
- Want minimal ceremony

**Tracks**:

- **Quick Flow** (~5 min): Bug fixes, small tasks
- **BMad Method** (~15 min): Structured features
- **Enterprise** (~30 min): Production deployment

---

### Agent-OS (Builder Methods)

**Philosophy**: Capture your standards, stack, and codebase details

**Pros**:

- ✅ Works with any AI tool
- ✅ Captures YOUR patterns
- ✅ Good for established codebases
- ✅ Practitioner-created (Brian Casel)

**Cons**:

- ❌ Less prescriptive
- ❌ Requires existing standards
- ❌ Smaller community
- ❌ Less structure for greenfield

**When to Use**:

- Established codebases
- Have existing patterns to capture
- Multi-tool environments
- Want to document institutional knowledge

**When NOT to Use**:

- Greenfield without patterns
- Need prescriptive guidance

---

### GSD (Get-Shit-Done)

**Philosophy**: Lightweight context engineering for Claude Code

**Pros**:

- ✅ Simplest to start
- ✅ Designed for solo developers
- ✅ Fresh subagent context per task
- ✅ Atomic git commits
- ✅ "No enterprise roleplay"
- ✅ Strong brownfield support

**Cons**:

- ❌ Claude Code ONLY
- ❌ Opinionated XML prompts
- ❌ File size limits
- ❌ Not for team coordination
- ❌ Security implications (skip permissions mode)

**When to Use**:

- Solo developer
- Rapid prototyping
- Claude Code user
- Hate process, want results

**When NOT to Use**:

- Large teams
- Enterprise compliance
- Using Cursor, Copilot, etc.

---

## Use Case Matrix

| Scenario                        | Recommended Framework       |
| ------------------------------- | --------------------------- |
| Solo developer, weekend project | GSD                         |
| Team with compliance needs      | Spec-Kit                    |
| Evolving existing system        | OpenSpec                    |
| Any scale, want guidance        | BMAD-METHOD                 |
| Capture existing standards      | Agent-OS                    |
| Quick bug fix                   | GSD or BMAD Quick Flow      |
| Enterprise from scratch         | Spec-Kit or BMAD Enterprise |
| Multi-tool team                 | OpenSpec or Agent-OS        |
| Need audit trail                | Spec-Kit                    |
| Hate ceremony                   | GSD                         |

---

## For Your Project (AI Engine)

### Recommended: BMAD-METHOD + OpenSpec

**Why This Combination**:

1. **BMAD-METHOD** (Primary)

   - Scale-adaptive tracks match your 5 phases
   - Specialized agents for engineering domain
   - Brownfield support for existing documents
   - Guided workflows for complex systems

2. **OpenSpec** (Supplementary)
   - Delta tracking for evolving specs
   - Change proposals for cross-cutting changes
   - Multi-tool support (Claude, Antigravity, Gemini, etc.)
   - Lightweight without heavy ceremony

**Mapping to Your Phases**:

| Phase                   | BMAD Track  | OpenSpec Usage                   |
| ----------------------- | ----------- | -------------------------------- |
| Phase 1: Data Analysis  | Quick Flow  | Document templates as specs      |
| Phase 2: Knowledge Base | BMad Method | Vector DB schema proposals       |
| Phase 3: NLP Pipeline   | BMad Method | Arabic NLP integration proposals |
| Phase 4: Generation     | BMad Method | Template engine proposals        |
| Phase 5: Integration    | Enterprise  | API design, deployment proposals |

---

## Key Considerations

### Spec-Kit

- ⚠️ Requires Python 3.11+, Git, uv
- ⚠️ Constitution MUST be first
- ⚠️ Sequential phases enforced
- ⚠️ Branch-per-feature discipline

### OpenSpec

- ⚠️ Strict delta format (@@, +/-, context)
- ⚠️ Understand specs/ vs changes/ folders
- ⚠️ Archive workflow required
- ⚠️ Telemetry opt-out: `OPENSPEC_TELEMETRY=0`

### BMAD-METHOD

- ⚠️ Requires Node.js v20+
- ⚠️ Choose right track for task
- ⚠️ Agent personas require character
- ⚠️ 21 agents = learning curve

### Agent-OS

- ⚠️ Capture standards first
- ⚠️ Less prescriptive
- ⚠️ Documentation-focused

### GSD

- ⚠️ Claude Code ONLY
- ⚠️ Skip permissions mode (security)
- ⚠️ File size limits enforced
- ⚠️ Atomic commits need clean git

---

## Decision Tree

```
What are you building?
│
├─ Solo weekend project
│  └─ GSD (if Claude Code) or BMAD Quick Flow
│
├─ Team product with compliance
│  └─ Spec-Kit (governance) or BMAD Enterprise
│
├─ Evolving existing system
│  └─ OpenSpec (deltas) + BMAD Method
│
├─ Complex multi-phase project
│  └─ BMAD-METHOD + OpenSpec (YOUR PROJECT)
│
└─ Capture existing patterns
   └─ Agent-OS
```

---

## Vibe Coding Compatibility

**Most Vibe-Friendly** → **Least Vibe-Friendly**

1. **GSD** ⭐⭐⭐⭐⭐

   - "No enterprise roleplay bullshit"
   - Describe what you want, it builds it

2. **OpenSpec** ⭐⭐⭐

   - Lightweight proposals
   - Minimal ceremony

3. **Agent-OS** ⭐⭐⭐

   - Works naturally with any tool
   - Captures your flow

4. **BMAD Quick Flow** ⭐⭐⭐

   - ~5 minutes to first story
   - Exploratory-friendly

5. **Spec-Kit** ⭐⭐
   - Constitution-first = upfront investment
   - Sequential phases = less spontaneous

---

## Tool Support

| Framework | Claude Code | Cursor | Copilot | Gemini | Others      |
| --------- | ----------- | ------ | ------- | ------ | ----------- |
| Spec-Kit  | ✅          | ✅     | ✅      | ✅     | Many        |
| OpenSpec  | ✅          | ✅     | ✅      | ✅     | 15+ tools   |
| BMAD      | ✅          | ✅     | ✅      | ✅     | Many        |
| Agent-OS  | ✅          | ✅     | ✅      | ✅     | Any         |
| GSD       | ✅          | ❌     | ❌      | ❌     | Claude only |

---

## Installation Commands

```bash
# Spec-Kit
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

# OpenSpec
npm install -g @fission-ai/openspec

# BMAD-METHOD
npm install -g bmad-method

# Agent-OS
# (Installation varies - see docs)

# GSD
npx get-shit-done-cc
```

---

## Final Recommendation

For your **Civil Engineering AI Proposal Generator**:

### Primary: BMAD-METHOD

- Handles your 5-phase complexity
- Specialized agents for engineering domain
- Scale-adaptive as project grows

### Supplementary: OpenSpec

- Track spec changes across phases
- Change proposals for features
- Multi-tool team support

### Why Not Others:

- **Spec-Kit**: Too rigid for exploratory AI/ML work
- **Agent-OS**: Need more structure than it provides
- **GSD**: Team project, not solo; need multi-tool support

---

## Quick Commands

```bash
# BMAD
/bmad-master              # Start
/bmad-quick-flow          # Explore
/bmad-method              # Build
/bmad-enterprise          # Deploy

# OpenSpec
openspec list             # What's active?
openspec show <item>      # View details
openspec validate --strict  # Check quality
openspec archive <id> --yes  # Complete

# Integration
# 1. Create OpenSpec proposal
# 2. Implement with BMAD
# 3. Archive with OpenSpec
```

---

**See Also**:

- `BMAD-OPENSPEC-INTEGRATION.md` - How to use both together
- `QUICK-START-GUIDE.md` - Step-by-step for your project
- `openspec/project.md` - Project context
- `AI-Engine-Research-Report.md` - Library research
