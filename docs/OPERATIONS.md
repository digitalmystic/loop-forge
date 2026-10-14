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
