# Framework Decision Matrix

Visual guide for selecting the right spec-driven development framework.

---

## Quick Selection Chart

```
┌─────────────────────────────────────────────────────────────────┐
│                    PROJECT CHARACTERISTICS                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Team Size:    Solo ────────────────────────────── Enterprise   │
│                 │                                        │       │
│                GSD                                  Spec-Kit     │
│                                                                  │
│  Complexity:   Simple ──────────────────────────── Complex      │
│                 │              │                       │         │
│                GSD        OpenSpec              BMAD-METHOD      │
│                                                                  │
│  Process:      Minimal ─────────────────────── Structured       │
│                 │              │                       │         │
│                GSD        Agent-OS              Spec-Kit         │
│                                                                  │
│  Codebase:     Greenfield ──────────────────── Brownfield       │
│                 │              │                       │         │
│             Spec-Kit      OpenSpec              Agent-OS        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Feature Comparison Matrix

```
┌──────────────────┬──────────┬──────────┬──────────┬──────────┬──────────┐
│ Feature          │ Spec-Kit │ OpenSpec │   BMAD   │ Agent-OS │   GSD    │
├──────────────────┼──────────┼──────────┼──────────┼──────────┼──────────┤
│ Constitution     │    ✅    │    ❌    │    ❌    │    ❌    │    ❌    │
│ Delta Tracking   │    ❌    │    ✅    │    ❌    │    ❌    │    ❌    │
│ Agent Personas   │    ❌    │    ❌    │    ✅    │    ❌    │    ❌    │
│ Scale-Adaptive   │    ❌    │    ❌    │    ✅    │    ❌    │    ❌    │
│ Multi-Tool       │    ✅    │    ✅    │    ✅    │    ✅    │    ❌    │
│ Brownfield       │    ⚠️    │    ✅    │    ✅    │    ✅    │    ✅    │
│ Vibe-Coding      │    ⚠️    │    ✅    │    ✅    │    ✅    │    ✅    │
│ Audit Trail      │    ✅    │    ✅    │    ✅    │    ⚠️    │    ⚠️    │
│ Learning Curve   │  Medium  │   Easy   │   Hard   │  Medium  │   Easy   │
│ Setup Time       │  15 min  │  5 min   │ 5-30 min │  10 min  │  2 min   │
└──────────────────┴──────────┴──────────┴──────────┴──────────┴──────────┘

Legend: ✅ Strong  ⚠️ Partial  ❌ Not Available
```

---

## Workflow Comparison

### Spec-Kit: Sequential Phases

```
Constitution → Specify → Clarify → Plan → Tasks → Analyze → Implement
     ↓            ↓         ↓        ↓       ↓        ↓          ↓
  Required    Feature   Questions  Tech   Breakdown  Validate   Code
  Upfront     Spec      (max 5)   Stack   Tasks     Consistency

  ⚠️ Cannot skip phases
  ⚠️ Constitution must be first
  ✅ Clear governance
  ✅ Audit trail
```

### OpenSpec: Proposal → Apply → Archive

```
Specs (Current Truth)
  ↓
Changes (Proposals)
  ├─ proposal.md  (Why/What/Impact)
  ├─ tasks.md     (Implementation)
  ├─ design.md    (Technical decisions)
  └─ specs/       (Deltas: ADDED/MODIFIED/REMOVED)
  ↓
Apply (Implement)
  ↓
Archive (Complete)
  ↓
Specs (Updated Truth)

✅ Lightweight
✅ Delta tracking
✅ Multi-tool support
⚠️ Less structure for greenfield
```

### BMAD-METHOD: Scale-Adaptive Tracks

```
Quick Flow (~5 min)
  ├─ Bug fixes
  ├─ Small tasks
  └─ Exploration

BMad Method (~15 min)
  ├─ New features
  ├─ Structured development
  └─ Clear deliverables

Enterprise (~30 min)
  ├─ API design
  ├─ Deployment
  └─ Compliance

✅ Scale-adaptive
✅ 21 specialized agents
✅ Guided workflows
⚠️ Steep learning curve
```

### Agent-OS: Capture Standards

```
Codebase Analysis
  ↓
Capture Standards
  ├─ Tech stack
  ├─ Conventions
  └─ Patterns
  ↓
Structured Workflows
  ↓
AI Follows Standards

✅ Works with any tool
✅ Captures YOUR patterns
⚠️ Less prescriptive
⚠️ Requires existing standards
```

### GSD: Context Engineering

```
Idea
  ↓
Questions (Extract context)
  ↓
PROJECT.md (Vision)
  ↓
ROADMAP.md (Phases)
  ↓
PLAN.md (Tasks)
  ↓
Subagent Execution (Fresh context per task)
  ↓
Atomic Git Commits
  ↓
Ship

✅ Simplest workflow
✅ Fresh context per task
✅ No ceremony
⚠️ Claude Code only
```

---

## Use Case Decision Tree

```
┌─────────────────────────────────────────────────────────────────┐
│                    WHAT ARE YOU BUILDING?                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │  Team or Solo?      │
                    └─────────────────────┘
                       │              │
                    Solo            Team
                       │              │
                       ▼              ▼
              ┌──────────────┐  ┌──────────────┐
              │ Claude Code? │  │ Compliance?  │
              └──────────────┘  └──────────────┘
                 │        │        │        │
               Yes       No      Yes       No
                 │        │        │        │
                 ▼        ▼        ▼        ▼
               GSD    BMAD     Spec-Kit  OpenSpec
                    Quick Flow          + BMAD

┌─────────────────────────────────────────────────────────────────┐
│                    WHAT'S YOUR CODEBASE?                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │ Greenfield or       │
                    │ Brownfield?         │
                    └─────────────────────┘
                       │              │
                  Greenfield      Brownfield
                       │              │
                       ▼              ▼
              ┌──────────────┐  ┌──────────────┐
              │ Need         │  │ Have         │
              │ Governance?  │  │ Standards?   │
              └──────────────┘  └──────────────┘
                 │        │        │        │
               Yes       No      Yes       No
                 │        │        │        │
                 ▼        ▼        ▼        ▼
             Spec-Kit   BMAD   Agent-OS  OpenSpec
                                         + BMAD

┌─────────────────────────────────────────────────────────────────┐
│                    WHAT'S YOUR PRIORITY?                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │ Speed or Quality?   │
                    └─────────────────────┘
                       │              │
                    Speed          Quality
                       │              │
                       ▼              ▼
              ┌──────────────┐  ┌──────────────┐
              │ Prototype or │  │ Audit Trail  │
              │ Production?  │  │ Required?    │
              └──────────────┘  └──────────────┘
                 │        │        │        │
            Prototype  Prod     Yes       No
                 │        │        │        │
                 ▼        ▼        ▼        ▼
               GSD    OpenSpec  Spec-Kit  BMAD
                      + BMAD              Method
```

---

## Complexity vs. Structure Matrix

```
High Structure
      ▲
      │
      │  Spec-Kit
      │     ●
      │
      │           BMAD Enterprise
      │              ●
      │
      │                    Agent-OS
      │                       ●
      │
      │        BMAD Method
      │           ●
      │
      │                 OpenSpec
      │                    ●
      │
      │  BMAD Quick Flow
      │     ●
      │
      │              GSD
      │               ●
      │
      └────────────────────────────────────────────▶
   Low Complexity                        High Complexity

Ideal Zone for Your Project:
┌─────────────────────────────────────┐
│  BMAD Method + OpenSpec             │
│  ● ● (Combined)                     │
│                                     │
│  Medium-High Structure              │
│  High Complexity                    │
│  Multi-Phase Development            │
└─────────────────────────────────────┘
```

---

## Tool Support Matrix

```
┌──────────────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
│ AI Tool          │Spec-Kit │OpenSpec │  BMAD   │Agent-OS │   GSD   │
├──────────────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│ Claude Code      │    ✅   │    ✅   │    ✅   │    ✅   │    ✅   │
│ Cursor           │    ✅   │    ✅   │    ✅   │    ✅   │    ❌   │
│ GitHub Copilot   │    ✅   │    ✅   │    ✅   │    ✅   │    ❌   │
│ Gemini CLI       │    ✅   │    ✅   │    ✅   │    ✅   │    ❌   │
│ Antigravity      │    ✅   │    ✅   │    ✅   │    ✅   │    ❌   │
│ Cline            │    ✅   │    ✅   │    ✅   │    ✅   │    ❌   │
│ Codex            │    ✅   │    ✅   │    ✅   │    ✅   │    ❌   │
│ Windsurf         │    ✅   │    ✅   │    ✅   │    ✅   │    ❌   │
│ Qwen Code        │    ✅   │    ✅   │    ✅   │    ✅   │    ❌   │
│ OpenCode         │    ✅   │    ✅   │    ✅   │    ✅   │    ❌   │
│ Others           │   Many  │   15+   │   Many  │   Any   │    ❌   │
└──────────────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
```

---

## Your Project: AI Engine for Civil Engineering

### Project Characteristics

```
┌─────────────────────────────────────────────────────────────────┐
│ PROJECT PROFILE                                                  │
├─────────────────────────────────────────────────────────────────┤
│ Team Size:           Small team (2-5 developers)                │
│ Complexity:          High (AI/ML, NLP, Engineering validation)  │
│ Codebase:            Brownfield (14 existing documents)         │
│ Duration:            20 weeks (5 phases)                        │
│ Domain:              Civil Engineering (5 disciplines)          │
│ Languages:           Bilingual (Arabic/English)                 │
│ Tools:               Multiple AI assistants                     │
│ Compliance:          Engineering standards, regulations         │
└─────────────────────────────────────────────────────────────────┘
```

### Recommended Framework Combination

```
┌─────────────────────────────────────────────────────────────────┐
│ PRIMARY: BMAD-METHOD                                             │
├─────────────────────────────────────────────────────────────────┤
│ ✅ Scale-adaptive tracks (Quick → Method → Enterprise)          │
│ ✅ 21 specialized agents for different tasks                    │
│ ✅ Handles high complexity                                      │
│ ✅ Strong brownfield support                                    │
│ ✅ Guided workflows for multi-phase projects                    │
└─────────────────────────────────────────────────────────────────┘
                              +
┌─────────────────────────────────────────────────────────────────┐
│ SUPPLEMENTARY: OpenSpec                                          │
├─────────────────────────────────────────────────────────────────┤
│ ✅ Delta-based change tracking                                  │
│ ✅ Lightweight proposals for features                           │
│ ✅ Multi-tool support (Claude, Gemini, Antigravity, etc.)      │
│ ✅ Cross-cutting change management                              │
│ ✅ Spec evolution tracking                                      │
└─────────────────────────────────────────────────────────────────┘
```

### Phase-to-Framework Mapping

```
Phase 1: Data Analysis (Weeks 1-4)
├─ BMAD: Quick Flow (exploratory)
└─ OpenSpec: Document structure templates as specs

Phase 2: Knowledge Base (Weeks 5-8)
├─ BMAD: Method Track (structured development)
└─ OpenSpec: Vector DB schema proposals

Phase 3: NLP Pipeline (Weeks 9-12)
├─ BMAD: Method Track (complex integration)
└─ OpenSpec: Arabic NLP integration proposals

Phase 4: Generation System (Weeks 13-16)
├─ BMAD: Method Track (multi-component)
└─ OpenSpec: Template engine proposals

Phase 5: Integration & Deployment (Weeks 17-20)
├─ BMAD: Enterprise Track (production)
└─ OpenSpec: API design, deployment proposals
```

---

## Why NOT the Others?

### Why NOT Spec-Kit?

```
❌ Too Rigid
   ├─ Sequential phases don't fit AI/ML exploration
   ├─ Constitution-first delays getting started
   └─ Weak brownfield support for existing documents

❌ Wrong Focus
   ├─ Designed for governance, not rapid iteration
   ├─ Branch-per-feature doesn't fit multi-phase work
   └─ Overkill for team of 2-5 developers
```

### Why NOT Agent-OS Alone?

```
⚠️ Not Enough Structure
   ├─ Less prescriptive than needed for complex project
   ├─ Requires existing standards (you're building them)
   └─ Better as supplement, not primary framework
```

### Why NOT GSD?

```
❌ Tool Limitation
   ├─ Claude Code only (team uses multiple tools)
   ├─ Not designed for team coordination
   └─ Solo developer focus

⚠️ Scale Concerns
   ├─ 20-week project needs more structure
   ├─ 5 phases need phase-level tracking
   └─ Multi-discipline complexity
```

---

## Integration Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                    DAILY WORKFLOW                                │
└─────────────────────────────────────────────────────────────────┘

1. Start with BMAD
   ├─ /bmad-master
   ├─ Choose track (Quick/Method/Enterprise)
   └─ Begin exploration or implementation

2. Create OpenSpec Proposal (for features)
   ├─ openspec list --specs (check existing)
   ├─ Create proposal with AI
   └─ openspec validate --strict

3. Implement with BMAD
   ├─ BMAD guides through tasks
   ├─ Execute from OpenSpec tasks.md
   └─ Validate at each step

4. Archive with OpenSpec
   ├─ openspec archive <change-id> --yes
   ├─ Updates specs/ with changes
   └─ Moves to archive/

┌─────────────────────────────────────────────────────────────────┐
│                    DECISION POINTS                               │
└─────────────────────────────────────────────────────────────────┘

New Feature?
├─ Yes → OpenSpec proposal + BMAD implementation
└─ No → Bug fix? → BMAD Quick Flow

Breaking Change?
├─ Yes → OpenSpec proposal (track impact) + BMAD Enterprise
└─ No → Continue with current track

Cross-Cutting Change?
├─ Yes → OpenSpec deltas (multiple specs) + BMAD Method
└─ No → Single spec change
```

---

## Success Metrics

```
┌──────────────────────────────────────────────────────────────────┐
│ FRAMEWORK EFFECTIVENESS METRICS                                   │
├──────────────────────────────────────────────────────────────────┤
│                                                                   │
│ Time to First Feature:        < 1 week  (BMAD Quick Flow)       │
│ Spec-to-Code Alignment:       > 90%     (OpenSpec validation)   │
│ Cross-Cutting Change Tracking: 100%     (OpenSpec deltas)       │
│ Engineering Validation:        > 95%    (BMAD QA workflows)     │
│ Arabic NLP Accuracy:           > 90%    (Both frameworks)       │
│ Phase Completion Rate:         100%     (BMAD tracks)           │
│ Change Proposal Quality:       > 85%    (OpenSpec strict mode)  │
│                                                                   │
└──────────────────────────────────────────────────────────────────┘
```

---

## Quick Reference Commands

```bash
# BMAD
/bmad-master              # Start BMAD Master Agent
/bmad-quick-flow          # Quick tasks (~5 min)
/bmad-method              # Structured development (~15 min)
/bmad-enterprise          # Production deployment (~30 min)

# OpenSpec
openspec list             # List active changes
openspec list --specs     # List specifications
openspec show <item>      # View change or spec
openspec validate --strict  # Comprehensive validation
openspec archive <id> --yes  # Archive completed change

# Integration
# 1. Start BMAD → 2. Create OpenSpec proposal → 3. Implement → 4. Archive
```

---

## Next Steps

1. **Review Setup** (5 min)

   ```bash
   openspec list
   ls _bmad/core/
   ```

2. **Read Project Context** (10 min)

   ```bash
   cat openspec/project.md
   cat BMAD-OPENSPEC-INTEGRATION.md
   ```

3. **Start Phase 1** (Now!)
   ```bash
   /bmad-master
   # Begin data analysis
   ```

---

**See Also**:

- `BMAD-OPENSPEC-INTEGRATION.md` - Detailed integration guide
- `QUICK-START-GUIDE.md` - Step-by-step walkthrough
- `FRAMEWORK-COMPARISON-SUMMARY.md` - Detailed comparison
- `openspec/project.md` - Project context
