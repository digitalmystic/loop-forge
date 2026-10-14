# Ethereal Nexus Trust and Attestation Model

## Purpose

The trust model separates four questions that are often collapsed into one:

1. **Identity** — who or what is acting?
2. **Authority** — what is the actor allowed to do?
3. **Evidence** — what happened and what supports the claim?
4. **Attestation** — what exact state or claim is being vouched for?

A model response, tool output, node manifest, and attestation are not interchangeable.

## Node Identity

Each commissioned node should eventually have a node identity keypair.

The private key remains local to the node.

The public key or its fingerprint may be shared.

A node ID must remain stable across routine software upgrades, but replacing identity keys should create an explicit key-rotation event.

## Run IDs

Every consequential execution should receive an immutable run ID.

Recommended shape:

```text
<node-id>.<utc-timestamp>.<capability>.<nonce>
```

Example:

```text
beaver-lodge-dev-01.20261014T020000Z.semgrep.0001
```

The run record links actor, capability, lease, inputs, outputs, evidence, and result.

## Evidence

Evidence records answer whether a particular claim is:

- VERIFIED
- NOT_VERIFIED
- INDETERMINATE

Evidence is retained separately from interpretation.

## Attestation

An attestation binds a digest to explicit claims.

Example:

> The SHA-256 digest corresponds to the exact node manifest reviewed on this date, and the claims listed here were accepted by the named issuer.

An attestation should never make claims broader than the evidence supports.

## Hashes vs Signatures

A hash proves content identity.

A signature additionally binds that content to a key.

This initial implementation provides hash-based attestations and a schema field for signatures. Cryptographic signing should be activated only after a node identity/key-management procedure is approved.

## Trust Rule

```text
existence != trust
installation != authority
authority != execution
execution != correctness
evidence != interpretation
attestation != universal truth
```

Each layer proves a narrower fact.

## Public Verification

A future public verifier should be able to:

1. load a node manifest,
2. validate its schema,
3. validate repository references,
4. validate evidence records,
5. validate lease references,
6. recalculate content hashes,
7. validate signatures when present,
8. report exactly which claims are supported and which remain unresolved.
