# Event Horizon: BUILD ALL

Event Horizon is the execution program for building an open, vendor-independent corporate technology stack for Network Iron's real operations, then publishing the reusable machinery for others to inspect, adopt, fork, improve, and federate.

This is not a big-bang rewrite and it is not a collection of disconnected prototypes. The whole stack will be built through verified vertical slices. Each slice must solve a real operational or customer problem while advancing several architectural layers at once.

## Mission

Build a trust-native, portable, observable, resilient, and progressively open corporate technology substrate that Network Iron can operate in production.

> Identity stays. Infrastructure can move. Trust must be evidenced.

## Stack

| Layer | Responsibility |
| --- | --- |
| Network Iron | Commercial operator, support, integration, governance, and service delivery |
| viIO | Vendor-independent Infrastructure Operator doctrine and operating model |
| viEYE0 | Evidence, observability, trust state, dependency, and portability intelligence |
| DNSCompass | Service discovery, DNS configuration, validation, health, and routing authority |
| Project Tumbleweed | Provider-independent manifests, migration, synchronization, rollback, and portability |
| LSNs | Autonomous execution nodes and customer-controlled sovereignty anchors |
| Ethereal Nexus | Inter-node identity, provenance, trust, policy, and coordination fabric |
| The Source Lab | Research, documentation, standards, public evidence, and knowledge commons |

## BUILD ALL strategy

BUILD ALL means preserve the complete architecture while delivering it in high-leverage increments:

1. Solve a real Network Iron or customer problem.
2. Capture the provider-independent service model.
3. Build the smallest reusable tooling that removes repeated manual work.
4. Verify security, portability, trust, economics, and operability.
5. Operate it in a controlled pilot.
6. Publish reusable code, schemas, runbooks, tests, and evidence.
7. Back-propagate what works into the rest of the stack.

## Vertical Slice 0: Managed Email Portability

The first slice uses Friendly Geek's difficult email workloads as the practical proving ground, without placing customer data or credentials in this public repository.

It must produce a provider-independent service manifest; Canadian-first/non-US provider evaluation; DNSCompass mail checks; Tumbleweed migration and rollback phases; viEYE0 evidence and readiness states; an LSN/Ethereal Nexus signed evidence interface; and a repeatable Network Iron Managed Email service definition.

## Agentic team

Agents may research, design, write code, test, and open draft pull requests. They may not merge, deploy, modify production DNS, access customer credentials, spend money, or contact customers without human approval.

Detailed authorities are defined in `team.yaml`.

## #SCOPELOCK

Use the smallest state model that preserves every distinction required for correct action.

- `+`: known good, verified, trusted for the stated scope, or operating as required.
- `0`: unknown, unresolved, transitional, awaiting evidence, or not yet evaluated.
- `-`: known bad, failed, degraded beyond policy, denied, compromised, or revoked.

Lifecycle uses richer categorical states because `backlog`, `ready`, `active`, `review`, `blocked`, `done`, and `retired` drive different actions.

Unknown is not false. Transitional is not failed. Degraded is not necessarily dead.

## Operating authority

Launch autonomy is capped at **L2**:

- L0: observe and report.
- L1: propose plans, designs, issues, and patches.
- L2: create isolated branches, code, tests, documentation, and draft pull requests.
- L3: merge, deploy, change production, spend money, or communicate externally.

L3 always requires explicit human approval.

## First release boundary

Event Horizon v0.1 is complete when an anonymized email workload can be represented in a portable manifest, assessed against provider/jurisdiction policy, audited for DNS/authentication health, given a migration and rollback plan, assigned evidence-backed trust/readiness states, anchored to an LSN-compatible signed evidence record, and packaged as a repeatable Network Iron managed service.

No production migration is part of v0.1.
