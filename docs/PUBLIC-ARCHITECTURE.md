# Ethereal Nexus — Public Architecture Overview

## What It Is

Ethereal Nexus is an evolving local-first architecture for combining AI reasoning, human authority, open protocols, verifiable tooling, and resilient local infrastructure.

The design goal is not to create one giant application.

The goal is to create a small trusted control layer surrounded by replaceable capabilities.

## Core Pattern

```text
Human / Organization
        |
Identity + Policy
        |
ScopeLock + Capability Authority
        |
Reasoning / Agent Coordination
        |
Bounded Tools and Services
        |
Raw Evidence
        |
Independent Verification
        |
Provenance + Audit Record
```

## Repository Classes

### A — Nexus Core
Defines authority, policy, provenance, and core control semantics.

### B — Nexus Infrastructure
Replaceable infrastructure such as model runtimes, monitoring systems, communications services, and data systems.

### C — Nexus Capability
Bounded tools invoked for a specific purpose under explicit authority.

### D — Research / Reference
Systems studied for design lessons or evaluated in isolation.

## Why This Matters

AI systems are powerful, but reasoning quality and operational authority are different things.

Ethereal Nexus treats AI as a participant in a governed system rather than assuming the model itself is the governing authority.

That means:
- models can be replaced,
- tools can be replaced,
- evidence remains independently inspectable,
- authority can remain human and organizational,
- local nodes can continue operating when external services disappear.

## Local Nodes

A local node is intended to be an independently operable unit with:
- local compute,
- local identity,
- local policy,
- defined capabilities,
- documented network boundaries,
- auditable actions,
- optional federation with other trusted nodes.

Nodes may have different hardware and roles while following the same control principles.

## Current Status Language

Public material should use these terms consistently:

**IMPLEMENTED** — running now.

**APPROVED** — reviewed for the specified role.

**EVALUATING** — being tested or reviewed.

**RESEARCH** — studied but not trusted for operational use.

**ASPIRATIONAL** — planned or conceptual.

## Current Work

The active engineering work includes:
- review-gated agent loops,
- repository/dependency eligibility,
- sovereign/local inference,
- security capability isolation,
- provenance and evidence handling,
- local voice and communications,
- resilient node operation,
- machine-readable architecture registries.

See `docs/REPOSITORY-LANDSCAPE.md` for the current ecosystem map.
