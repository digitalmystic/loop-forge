# Local Node Readiness Checklist

Use this before describing a node as ready for public demonstration, collaboration, or external contribution.

## 1. Identity and Provenance
- [ ] Node has a unique node ID.
- [ ] Hostname and role are documented.
- [ ] Base OS/version recorded.
- [ ] Hardware inventory recorded.
- [ ] Git commit/release identifiers recorded for Nexus components.
- [ ] Model/runtime versions recorded.
- [ ] Time synchronization confirmed.
- [ ] Logs include node ID and timestamps.

## 2. Security Boundary
- [ ] Administrative access restricted.
- [ ] Firewall policy active.
- [ ] Default credentials removed.
- [ ] Secrets are not committed to Git.
- [ ] Service accounts use minimum required permissions.
- [ ] Outbound network access is documented.
- [ ] Inbound services are explicitly enumerated.
- [ ] Remote execution paths are known and controlled.
- [ ] Unreviewed MCP/tool servers are disabled by default.

## 3. ScopeLock / Capability Authority
- [ ] Every mutating capability has an explicit scope.
- [ ] Human approval requirements are defined.
- [ ] Tool invocation is logged.
- [ ] Capability leases can expire or be revoked.
- [ ] Unknown authority state fails closed.
- [ ] Research-only tools cannot reach production resources.

## 4. AI Runtime
- [ ] At least one local model runtime works without cloud dependency.
- [ ] Model provenance is recorded.
- [ ] Model files are checksum-verifiable.
- [ ] Runtime can be replaced without changing Nexus policy.
- [ ] Model output is not treated as authoritative evidence by default.
- [ ] External model providers, if enabled, are clearly marked.

## 5. Evidence and Verification
- [ ] Raw tool output is retained separately from AI interpretation.
- [ ] Findings use VERIFIED / NOT VERIFIED / INDETERMINATE semantics.
- [ ] A second verifier or human review path exists for consequential findings.
- [ ] Run logs can be exported.
- [ ] Reproducible commands/configuration are captured where practical.

## 6. Repository Registry
- [ ] `registry/repositories.yaml` validates against the registry schema.
- [ ] Every enabled upstream component appears in the registry.
- [ ] Every enabled component has an assigned class.
- [ ] Every Class B/C component has a defined role.
- [ ] Prohibited roles are documented.
- [ ] Reviewed versions/commits are pinned before production use.

## 7. Resilience
- [ ] Node can boot without external cloud services.
- [ ] Critical documentation is available locally.
- [ ] Recovery procedure exists.
- [ ] Configuration backup exists.
- [ ] Restore has been tested.
- [ ] Loss of one external service does not silently transfer authority elsewhere.

## 8. Accessibility / Human Operation
- [ ] Critical controls can be operated without relying on one sensory modality.
- [ ] Logs/status are available in accessible text.
- [ ] Human approval gates are understandable and reversible.
- [ ] Emergency stop/revoke procedure is obvious.

## 9. Public Sharing Gate
Before sharing a node publicly, classify every claim as one of:

- **IMPLEMENTED** — running and demonstrated.
- **APPROVED** — reviewed and authorized, not necessarily deployed.
- **EVALUATING** — under active review.
- **RESEARCH** — reference/experiment only.
- **ASPIRATIONAL** — design direction, not implemented.

Do not present EVALUATING, RESEARCH, or ASPIRATIONAL work as deployed capability.

## 10. Minimum Demonstration Package
A shareable node demonstration should include:
- node role and hardware,
- architecture diagram,
- enabled capabilities,
- disabled/research-only capabilities,
- repository registry snapshot,
- provenance summary,
- one reproducible demonstration,
- one verified audit trail,
- known limitations,
- next review milestone.
