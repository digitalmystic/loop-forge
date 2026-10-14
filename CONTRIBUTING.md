# Contributing to Ethereal Nexus / Loop Forge

This repository is being used as a review-gated engineering workspace for Ethereal Nexus experiments.

## Contribution Principles

1. **Keep the core small.**
   A useful project does not automatically belong in Nexus Core.

2. **Separate authority from capability.**
   Tools, models, MCP servers, and agents expose capabilities. Nexus policy defines whether those capabilities may be used.

3. **Preserve raw evidence.**
   AI interpretation must not replace the underlying source, command output, finding, or artifact.

4. **Fail closed on uncertain authority.**
   If scope, identity, approval, or permission is unclear, do not execute the consequential action.

5. **Declare maturity clearly.**
   Mark work as IMPLEMENTED, APPROVED, EVALUATING, RESEARCH, or ASPIRATIONAL.

6. **Prefer replaceable infrastructure.**
   Class B and C components should be swappable wherever practical.

## Repository Classification

Every proposed external repository must receive one class:

- **A — Nexus Core**
- **B — Nexus Infrastructure**
- **C — Nexus Capability**
- **D — Research / Reference**

Class A requires the highest review threshold.

## Required Proposal Information

When proposing a repository or major dependency, include:

```yaml
repo:
upstream:
domain:
proposed_class:
proposed_role:
forbidden_role:
license:
local_first:
network_requirements:
privileges_required:
data_access:
execution_capability:
telemetry:
known_security_concerns:
review_status:
```

## Review Outcome

Use one of:

- ELIGIBLE
- CONDITIONAL
- RESEARCH_ONLY
- INELIGIBLE
- UNREVIEWED

## Pull Requests

PRs affecting authority, execution, scope, identity, evidence, provenance, or security boundaries should explain:

- what authority changes,
- what new capability is introduced,
- what data it can access,
- what it can mutate,
- how it is constrained,
- how it is audited,
- how it can be disabled,
- how failure behaves.

## AI-Generated Contributions

AI-assisted code and documentation are welcome, but:
- authorship assistance must not be confused with verification,
- generated claims should be checked,
- generated code affecting security boundaries requires human review,
- provenance should be retained where practical.

## Public Communication

Do not imply that upstream projects endorse Ethereal Nexus unless they explicitly do.

Do not imply that a catalogued or experimental integration is deployed or trusted.

The public architecture should always distinguish current implementation from intended direction.
