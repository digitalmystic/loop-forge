# Operationalizing the Repository Landscape

This package turns the repository map into something local nodes can validate and report.

## Validate the repository registry

```bash
python3 scripts/validate-registry.py
```

## Validate a node manifest

```bash
python3 scripts/validate-node.py nodes/beaver-lodge-dev-01.yaml
```

The node validator now also checks referenced evidence records and capability leases.

## Evidence Records

Evidence is stored as structured YAML and validated against:

`schemas/evidence-record.v1.schema.json`

An evidence record answers:

- what claim is being made,
- what node/capability it concerns,
- who or what collected the evidence,
- how it was collected,
- which artifacts support it,
- whether the result is VERIFIED, NOT_VERIFIED, or INDETERMINATE,
- whether a required human/council review accepted it.

**APPROVED** and **IMPLEMENTED** capabilities must reference evidence records.

## Capability Leases

Capability leases are stored as structured YAML and validated against:

`schemas/capability-lease.v1.schema.json`

A lease binds:

- actor,
- node,
- capability,
- purpose,
- targets,
- allowed actions,
- network/filesystem scope,
- issue/expiry time,
- human approval,
- evidence requirements,
- stop conditions.

A lease is authorization metadata, not merely configuration.

## Promotion Rule

```text
ASPIRATIONAL
    |
EVALUATING
    |
APPROVED
    |
IMPLEMENTED
```

Promotion requires progressively stronger evidence.

### EVALUATING
May have provisional evidence and proposed leases.

### APPROVED
Must have verified, accepted evidence. Lease-governed capabilities must reference a PROPOSED or ACTIVE lease.

### IMPLEMENTED
Must have verified, accepted evidence. Lease-governed capabilities must have an ACTIVE lease or retained evidence of a historically active lease.

A capability may also be moved to:

```text
RESEARCH
DISABLED
```

## Status Report

```bash
python3 scripts/render-status.py nodes/beaver-lodge-dev-01.yaml
```

## Bootstrap Check

```bash
sh scripts/nexus-bootstrap-check.sh nodes/beaver-lodge-dev-01.yaml
```

## Commissioning Discipline

When the first local node is powered on:

1. replace assumed hardware details with measured facts,
2. record package/runtime versions,
3. pin repository commits,
4. collect hashes/configuration snapshots,
5. generate evidence records,
6. review evidence,
7. activate only the leases needed,
8. promote capabilities one state at a time,
9. commit the resulting node manifest and evidence trail.

The manifest should describe reality, not intention.


## Nexus CLI

The initial CLI surface is:

```bash
python3 scripts/nexus.py status nodes/beaver-lodge-dev-01.yaml
python3 scripts/nexus.py verify nodes/beaver-lodge-dev-01.yaml
python3 scripts/nexus.py attest nodes/beaver-lodge-dev-01.yaml --issuer digitalmystic
```

### status

Shows the node role, maturity state, and capability status/authority.

### verify

Calculates the manifest SHA-256 digest and confirms referenced local evidence/lease records exist.

This is intentionally narrower than full trust verification. Schema validation and semantic checks remain in `validate-node.py`.

### attest

Creates a hash-only attestation record for the exact manifest bytes supplied.

The generated attestation explicitly states that a hash alone does **not** prove issuer identity.

Signature support is represented in the schema but intentionally not activated until node identity and key-management procedures are approved.

## Run Records

Consequential executions should be represented by immutable run records validated against:

`schemas/run-record.v1.schema.json`

A run record captures actor, capability, lease reference, inputs, outputs, evidence, command, outcome, and timestamps.

The included Semgrep example is deliberately marked `DENIED` because its example capability lease is only `PROPOSED`. This demonstrates the intended fail-closed semantics.

## Attestation Records

Attestations are validated against:

`schemas/attestation-record.v1.schema.json`

A valid attestation binds explicit claims to a digest and named issuer.

The trust rule remains:

```text
existence != trust
installation != authority
authority != execution
execution != correctness
evidence != interpretation
attestation != universal truth
```
