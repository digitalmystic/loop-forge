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

## Generate a status report

```bash
python3 scripts/render-status.py nodes/beaver-lodge-dev-01.yaml
```

## Run the basic bootstrap check

```bash
sh scripts/nexus-bootstrap-check.sh nodes/beaver-lodge-dev-01.yaml
```

## Promotion Rule

A capability must move through explicit states:

```text
ASPIRATIONAL
    |
EVALUATING
    |
APPROVED
    |
IMPLEMENTED
```

A capability may also be moved to:

```text
RESEARCH
DISABLED
```

Promotion should require evidence.

Examples:
- installed binary/package version,
- pinned repository commit,
- configuration snapshot,
- successful test,
- security review,
- human approval.

## Intended Next Step

Once the first local node is powered on, replace assumptions in the pre-commissioning manifest with measured facts and generate the first signed or committed node status snapshot.
