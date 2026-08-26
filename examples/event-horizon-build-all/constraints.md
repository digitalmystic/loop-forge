# Event Horizon Constraints

## Safety and authority

- Agents operate at L2 or below.
- All merges, deployments, production DNS changes, customer migrations, spending, external communication, and releases require explicit human approval.
- Work must occur in isolated branches or worktrees and be submitted as draft pull requests.
- The implementer cannot be the sole verifier.

## Privacy and secrets

- No customer names, mailbox addresses, mailbox content, credentials, tokens, private keys, billing details, or identifiable operational data in public repositories.
- Use synthetic or anonymized fixtures.
- Stop immediately if sensitive material is discovered.

## Architecture

- Customer identity, domain, policy, and data ownership are distinct from the selected provider.
- Provider-specific behaviour belongs behind an adapter or explicit compatibility boundary.
- An LSN is a preferred control and execution anchor where justified, not a mandatory dependency.
- Ethereal Nexus membership never implies trust by itself.
- Open formats, standards, export paths, and recovery procedures are preferred.

## #SCOPELOCK semantics

- Use binary only for genuinely two-state conditions.
- Use ternary when unknown, transitional, or indeterminate must not be collapsed into true or false.
- Use richer categorical or quantitative evidence where three states would still lose meaning.
- Simplified operational states must be traceable to underlying evidence.

## Delivery discipline

- Build through vertical slices, not horizontal subsystem sprawl.
- Every iteration must produce a testable artifact or a falsifiable decision.
- Do not build a new mail server, webmail client, office suite, DNS server, or cloud platform in v0.1.
- Prefer integration and orchestration of best-of-breed open components.
- Record assumptions, unresolved questions, failures, and rejected options.
- Stop after two iterations without measurable progress.
