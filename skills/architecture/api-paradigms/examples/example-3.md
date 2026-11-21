# Example 3 — Splitting a leaked internal paradigm from the public surface

## Before

Two internal services communicate over gRPC for its strict contracts and streaming. When a partner asks for API access, the team exposes the same gRPC service publicly "because it already works." Partners now depend on internal message shapes, and every internal refactor becomes a public breaking change.

## After

The gRPC interface stays where it belongs — internal, governed by its `.proto` contract. A public REST API is built over the same capabilities per api-architecture, with its own OpenAPI contract, house-profile conventions, and api-versioning discipline. The internal services can now evolve at their own pace without partner impact, and partners get the boring, stable paradigm.

## Note

Corrects AR-125 (gRPC stays internal by default) and AR-130 (public consumers get the most boring paradigm that fits; internal novelty never leaks into the public surface).
