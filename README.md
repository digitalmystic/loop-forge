---
name: loop-forge
description: Loop Forge — design, audit, and run review-gated agent loops. Fusion of ksimback/looper (cross-model council, plan/delivery gates) + cobusgreyling/loop-engineering (production primitives, audit scoring). Works with Hermes, Claude Code, and Codex agents.
version: 1.0.0
category: autonomous-ai-agents
tags: [looper, loop-engineering, agent-loops, review-gates, cross-model, council, design, audit]
---

# Loop Forge

**Design loops that audit themselves.** A Hermes-native plugin fusing two proven loop frameworks:

| From | What we took | Why |
|------|-------------|-----|
| **[ksimback/looper](https://github.com/ksimback/looper)** | Loop spec (goal→gates→council→stop), cross-model review, plan/delivery gates with revision caps | Design discipline before execution |
| **[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)** | Production primitives (scheduling, worktrees, skills, MCP, sub-agents, state), audit scoring, drift detection | Production durability + measurable quality |

**Works with:** Hermes Agent (native), Claude Code (via skill), Codex CLI (via spec), any agent that reads YAML and spawns sub-agents.

## Quick Start

```bash
# Scaffold a loop from pattern
bash scripts/loop-init.sh . --pattern daily-triage --tool hermes

# Audit loop readiness (score 0-100)
bash scripts/loop-audit.sh .

# Run from resolved spec
bash scripts/loop-run.sh loop.resolved.json
```

## What It Provides

| Phase | Tool | What It Does |
|-------|------|-------------|
| **DESIGN** | `loop-design` | Interview → critique → loop.yaml → loop.resolved.json |
| **INIT** | `loop-init` | Scaffold from pattern, create STATE.md + constraints |
| **AUDIT** | `loop-audit` | Score loop readiness (0-100), suggest fixes |
| **RUN** | `loop-run` | Execute resolved spec in-session or via cron |
| **SYNC** | `loop-sync` | Detect drift between STATE.md and LOOP.md |

## Loop Anatomy

```
┌─────────────────────────────────────────────────────┐
│                    LOOP SPEC                         │
│  ┌──────────┐   ┌──────────┐   ┌──────────────┐    │
│  │   GOAL   │ → │   PLAN   │ → │   DELIVER    │    │
│  │ +verify  │   │  +gate   │   │   +gate      │    │
│  └──────────┘   └──────────┘   └──────────────┘    │
│       ↑              ↑                ↑             │
│       │         ┌─────────┐     ┌─────────┐         │
│       │         │REVIEWER │     │  JUDGE  │         │
│       │         │(council)│     │(council)│         │
│       │         └─────────┘     └─────────┘         │
│       │                                              │
│  ┌──────────────────────────────────────────┐       │
│  │  STOP GUARDS: max_iterations, no_progress,│       │
│  │  budget_caps, revision_limits             │       │
│  └──────────────────────────────────────────┘       │
│                                                      │
│  ┌──────────────────────────────────────────┐       │
│  │  OBSERVABILITY: state.json + run-log.md  │       │
│  │  + loop-audit score badge                 │       │
│  └──────────────────────────────────────────┘       │
└─────────────────────────────────────────────────────┘
```

## Patterns

| Pattern | Description | When to Use |
|---------|-------------|------------|
| `daily-triage` | Scan, categorize, report. Read-only. | Monitoring, alerting, daily briefings |
| `continuous-enhance` | Probe, scrape, cross-ref, update, deploy. | DMA intel, competitive monitoring |
| `minimal-fix` | Diagnose, propose, verify, commit. | Bug fixes, small improvements |
| `verifier` | Independent spot-check of another agent's work. | QA, hallucination detection |
| `issue-triage` | Label, prioritize, assign. | GitHub issue management |
| `research-synthesis` | Search, extract, synthesize, publish. | Research reports, market intel |

## Cross-Model Council

The killer feature from looper: a **different model** checks the work. In Hermes:

```yaml
council:
  - id: reviewer-1
    role: judge
    provider: anthropic          # Different provider from host
    model: claude-sonnet-4
    scope: [plan, delivery]
    max_revisions: 3
```

The host (DeepSeek, Codex, Grok) does the work. The council (Claude, Gemini, different model) verifies it. **Self-grading is the root cause of loop failure** — the council fixes this.

## Production Primitives (from loop-engineering)

| Primitive | Hermes Implementation |
|-----------|----------------------|
| **Automation/Scheduling** | `cronjob` (native) |
| **Worktrees** | `git worktree` (terminal) |
| **Skills** | `skill_manage` + `skill_view` (native) |
| **Plugins/Connectors** | MCP bridges (native-mcp skill) |
| **Sub-agents** | `delegate_task` (native) |
| **Memory/State** | `memory` + `STATE.md` + `state.json` |

## Files

```
loop-forge/
├── SKILL.md                    ← This file
├── schemas/
│   └── loop.v1.schema.json    ← Loop spec schema (from looper, adapted)
├── templates/
│   ├── loop.yaml.template      ← Loop spec template
│   ├── STATE.md.template       ← State file template
│   ├── constraints.md.template ← Budget + stop guards
│   └── run-log.md.template     ← Run log template
├── patterns/
│   ├── daily-triage.yaml
│   ├── continuous-enhance.yaml
│   ├── minimal-fix.yaml
│   ├── verifier.yaml
│   ├── issue-triage.yaml
│   └── research-synthesis.yaml
├── scripts/
│   ├── loop-init.sh            ← Scaffold from pattern
│   ├── loop-audit.sh           ← Score readiness
│   ├── loop-design.py          ← Interactive designer
│   └── loop-run.sh             ← Execute resolved spec
└── examples/
    └── dma-signal-intel/       ← First production example
        └── loop.yaml
```

## Audit Scoring

`loop-audit` scores your loop on 10 dimensions (0-10 each → 0-100 total):

| # | Dimension | What It Checks |
|---|-----------|---------------|
| 1 | Goal clarity | Is the definition of done falsifiable? |
| 2 | Verification | Are there programmatic/judge/human checks? |
| 3 | Council | Is a different model reviewing? |
| 4 | Gates | Are plan and delivery gates defined? |
| 5 | Stop guards | Max iterations, no-progress, budget caps? |
| 6 | State | Is STATE.md present and scannable? |
| 7 | Constraints | Are budgets, worktrees, isolation defined? |
| 8 | Observability | state.json + run-log.md present? |
| 9 | Schema valid | Does loop.yaml pass schema validation? |
| 10 | Resolved ready | Can loop.resolved.json be generated? |

**Score interpretation:**
- 0-30: Raw prompt, no loop design
- 31-60: Basic loop shape, missing gates
- 61-85: Well-designed, minor gaps
- 86-100: Production-ready loop

## Example: DMA Signal Intelligence Loop

See `examples/dma-signal-intel/loop.yaml` for a complete continuous-enhance loop with:
- Goal: enhance DMA intel dashboard
- Cross-model council (DeepSeek host → Claude reviewer)
- Plan gate + delivery gate with revision caps
- Stop guards: max 12 iterations, no-progress x2, budget $5
- Observability: state.json + run-log.md + git commit log

---

**Built by Legolas** for the SWC Devices Network.  
Fuses [ksimback/looper](https://github.com/ksimback/looper) (MIT) + [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) (MIT).  
License: MIT
