# Example 3 — Microservices by default, corrected to a modular monolith

## Before

A solo-built CRUD application with a few hundred expected users is designed as six microservices — gateway, auth, catalog, orders, billing, notifications — each with its own repository and deployment, "so it can scale later." No load figure, isolation need, or team boundary forces the split; every feature change now crosses three repositories.

## After

The design is a modular monolith: one deployable with feature modules (auth, catalog, orders, billing, notifications) that may only interact through module interfaces. ADR-0007 records the decision and names the trigger that would revisit it: a module needing independent scaling demonstrated by load measurements, or a second team taking ownership of a module.

## Note

Corrects AR-004 (modular monolith by default; a distributed design must cite the requirement that forces it, in an ADR).
