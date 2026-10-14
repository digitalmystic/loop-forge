# Ethereal Nexus Repository Landscape

This document is the human-readable companion to `registry/repositories.yaml`.

Its purpose is to keep the center of Ethereal Nexus small while allowing a large, replaceable ecosystem around it.

## Repository Classes

- **Class A — Nexus Core**: code that defines Nexus behavior, authority, policy, provenance, or control-plane semantics.
- **Class B — Nexus Infrastructure**: replaceable infrastructure Nexus may run on or depend upon.
- **Class C — Nexus Capability**: bounded tools that Nexus may invoke under explicit scope and authority.
- **Class D — Research / Reference**: projects to study, compare, or quarantine; not trusted as production dependencies by default.

## Decision States

- **ELIGIBLE** — approved for the defined role, subject to pinned version and controls.
- **CONDITIONAL** — promising, but review requirements remain.
- **RESEARCH_ONLY** — useful for learning or comparison, not approved for trusted execution.
- **INELIGIBLE** — rejected for the proposed role.
- **UNREVIEWED** — catalogued but not yet assessed.

## Domain Map

### Agent Control Plane
- `digitalmystic/loop-forge` — Class A — review-gated agent loops and Nexus orchestration experiments.
- `digitalmystic/loop-engineering` — Class D/B candidate — production loop patterns and tooling.
- `digitalmystic/hermes-agent` — Class D/B candidate — general-purpose agent runtime research.
- `digitalmystic/clawcodex` — Class D — coding-agent architecture research.
- `digitalmystic/agent-skills` — Class C/D — portable capability definitions.
- `digitalmystic/hindsight` — Class B/C candidate — agent memory and learning substrate.

### Sovereign Inference
- `Yamz-Labs/kyojin` — Class B candidate — AMD/ROCm local inference.
- `ggml-org/llama.cpp` — Class B candidate — portable local inference primitive.
- `ollama/ollama` — Class B candidate — local model serving and packaging.

### Security Reasoning
- `GreyDGL/PentestGPT` — Class D/C candidate — agentic penetration-testing reasoning.
- `usestrix/strix` — Class D/C candidate — agentic application security testing.
- `0x4m4/hexstrike-ai` — Class D — quarantined architectural study.

### Deterministic Security Capabilities
- `semgrep/semgrep` — Class C candidate — code-aware static analysis.
- `projectdiscovery/nuclei` — Class C candidate — template-driven vulnerability testing.
- `wazuh/wazuh` — Class B/C candidate — endpoint/security monitoring and telemetry.
- `prowler-cloud/prowler` — Class C candidate — cloud security posture and compliance.
- `owasp-amass/amass` — Class C candidate — attack-surface discovery.
- `gitleaks/gitleaks` — Class C candidate — secret detection.
- `caido/caido` — Class C/D candidate — human web-security workbench.
- `digitalmystic/portmaster` — Class B/C candidate — host/network policy and privacy.

### Voice and Human Interface
- `OpenWhispr/openwhispr` — Class B/C candidate — local voice interface.
- `OpenWhispr/openwhispr-mcp` — Class C candidate — voice-to-tool bridge.
- `OpenWhispr/openwhispr-cli` — Class C candidate — CLI interface.
- `ggerganov/whisper.cpp` — Class B/C candidate — local speech recognition primitive.
- `digitalmystic/meetily` — Class B/C candidate — local transcription and meeting intelligence.

### Integration / Capability Transport
- `digitalmystic/hub-mcp` — Class C candidate — Docker Hub MCP bridge.
- `digitalmystic/open-connector` — Class B/C candidate — auth/integration gateway.

### Local-First / Resilience
- `digitalmystic/project-nomad` — Class D/B candidate — offline and resilient computing reference.
- Raspberry Pi experiments — Class D/B candidates — edge-node patterns.
- `digitalmystic/LibreHardwareMonitor` — Class C candidate — hardware telemetry.

### Organizational Applications
- `digitalmystic/frappe`
- `digitalmystic/erpnext`
- `digitalmystic/hrms`
- `digitalmystic/crm`
- `digitalmystic/helpdesk`
- `digitalmystic/lms`

These are application-layer systems, not Nexus Core.

## Architectural Rule

A useful upstream project must not become Nexus Core merely because it is powerful.

The preferred integration order is:

```text
Nexus Policy
  -> Identity / ScopeLock / Capability Lease
  -> Agent or Service
  -> Bounded Capability
  -> Raw Evidence
  -> Verification
  -> Provenance Record
```

## Machine-Readable Registry

All repository decisions should be mirrored in `registry/repositories.yaml`.

That registry is intended to become readable by:
- local nodes,
- review loops,
- CI checks,
- councils,
- dependency tooling,
- future dashboards.

## Share-Ready Rule

When sharing this work publicly, distinguish clearly between:
1. what is implemented,
2. what is approved,
3. what is under evaluation,
4. what is research-only,
5. what is aspirational.

Do not present architectural intent as deployed capability.
