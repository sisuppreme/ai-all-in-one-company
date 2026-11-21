# system-design

## Metadata

- **Owner department:** D2 Architecture & System Design (AR)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** C4 model — https://c4model.com/ ; Pattern language for distributed designs — https://microservices.io/
- **Depends on:** requirements-writing, stack-selection
- **Feeds into:** c4-diagrams, adr-writing, data-architecture

## When to use / Do NOT use

- **Use when:** a new system or a major subsystem is being designed; the container topology, data ownership, or failure behavior of an existing system is being changed; a design review is requested.
- **Do NOT use when:** the change fits inside one existing container without new cross-boundary calls (build it and update the diagram via c4-diagrams instead), or when the open question is which stack to build on (stack-selection comes first).

## Rules

1. **AR-001 — Containers are real.** Every container in the design corresponds to a deployable unit, data store, or external system that exists in the repo or infrastructure config. Aspirational boxes are deleted or marked as future work outside the diagram.
2. **AR-002 — Every arrow is labeled.** Each relationship between containers carries a protocol or format label (HTTPS/JSON, gRPC, AMQP, SQL). An unlabeled arrow fails review.
3. **AR-003 — Failure behavior per call.** For every cross-container call, the design states the timeout, the retry policy, and what the caller does when the callee is down. A call missing any of the three is incomplete.
4. **AR-004 — Monolith by default.** The default topology is a modular monolith. A distributed design must cite, in an ADR, the requirement that forces it (independent scaling, team autonomy, isolation) — "future scale" without a load figure does not qualify.
5. **AR-005 — One writer per store.** Each data store has exactly one owning container that writes to it. Other containers read through the owner's interface or a replicated read model, never by writing directly.
6. **AR-006 — Quality attributes first.** Decomposition starts from the stated quality attributes (scale, latency, consistency, availability, tenancy), each with a target figure where one exists. A design that names components before attributes is sent back.
7. **AR-007 — Failure in the same pass.** Timeouts, retries, backpressure, and degradation are designed in the same pass as the happy path for every flow, not retrofitted after the first outage.
8. **AR-008 — Decisions become ADRs when made.** Each significant choice in the design (topology, ownership, protocol, consistency model) gets an ADR at the moment it is made, not reconstructed at the end of the project.
9. **AR-009 — Revisit on attribute change.** The design is revisited when a quality attribute changes (a new tenancy requirement, a 10× load target), not on a calendar schedule. The triggering change is named in the review note.
10. **AR-010 — External systems are explicit.** Every external system on the diagram is named, with the direction of the integration, whether it is synchronous or asynchronous, and who owns the relationship.

## BAN list

- **BAN-AR-001 — The generic three-box diagram.** Banned: a design whose whole model is boxes labeled "Frontend", "Backend", "Database" with unlabeled arrows. Defeats: DET-CODE-008. Bad: ARCHITECTURE.md contains one diagram, three boxes, no actors, no protocols; nobody can tell what calls what. Instead: a C4 container diagram with typed elements, named protocols on every arrow, and data stores as first-class containers (AR-001, AR-002). Severity: BLOCK.
- **BAN-AR-002 — Aspirational containers.** Banned: containers in the design that exist in no deployable unit, data store, or infrastructure config. Defeats: DET-INF-024. Bad: the diagram shows a "Recommendations Service" and a "Search Cluster"; the repo deploys one application and one PostgreSQL database. Instead: draw what exists; put the recommendations box in a clearly marked future-work note outside the diagram. Severity: BLOCK.
- **BAN-AR-003 — Distribution without a forcing requirement.** Banned: splitting the system into services with no ADR citing the requirement that forces distribution. Defeats: DET-CODE-015. Bad: six microservices for a CRUD application with one developer and no independent scaling need, chosen "so it can scale later." Instead: a modular monolith with module boundaries, plus an ADR naming the load or isolation figure that would trigger a split (AR-004). Severity: BLOCK.
- **BAN-AR-004 — Shared writable database.** Banned: two or more containers writing directly to the same tables. Defeats: DET-CODE-030. Bad: the billing worker and the web app both UPDATE the orders table; a race between them corrupts an order total. Instead: one owning writer; the other container calls the owner's interface or consumes its events (AR-005). Severity: WARN.

## Gates

- **G-AR-001 — Container-to-deployable walk.** Verifies: AR-001, AR-010. Check: manual — walk the container diagram element by element against the repo's deployable units and infrastructure config; every element must match a real unit, store, or named external system, and every relationship line in the diagram source must carry a protocol label (checked here, by eye, because label syntax differs across diagram formats). Pass: zero unmatched elements and zero unlabeled relationships. Fail: block design approval. Recorded in: progress.md.
- **G-AR-002 — Design document completeness.** Verifies: AR-002, AR-008. Check: automated — a script confirms ARCHITECTURE.md contains a container section and that every ADR file it references exists under `docs/decisions/`. Pass: script exits 0. Fail: block design approval. Recorded in: progress.md.
- **G-AR-003 — Failure-behavior review.** Verifies: AR-003, AR-007. Check: manual — for each cross-container call in the design, point at the row stating its timeout, retry policy, and callee-down behavior. Pass: every call has all three. Fail: block design approval. Recorded in: progress.md.
- **G-AR-004 — Data-ownership audit.** Verifies: AR-005. Check: manual — list every store in the design and its owning writer; confirm no second container writes to it directly. Pass: exactly one writer per store. Fail: block design approval. Recorded in: progress.md.

## Anti-patterns

- **Resume-driven topology.** The design mirrors whatever architecture is fashionable this year rather than the stated quality attributes. Catch it: ask which attribute each split serves; a split nobody can tie to AR-006's list is fashion, not design.
- **The happy-path sketch.** Flows are drawn only for success; timeouts and partial failure are "implementation details." Catch it: pick the busiest arrow and ask what happens at 10× load and when the callee hangs — if the design is silent, AR-007 was skipped.
- **Design by reconstruction.** ADRs written at project end from memory, with alternatives nobody actually considered. Catch it: check the ADR dates against the git history of the code they govern; a cluster of same-day ADRs for month-old decisions is reconstruction.
- **The invisible external system.** A third-party API the system depends on appears nowhere in the design because "it's just an SDK call." Catch it: grep the dependency manifest for HTTP clients and SaaS SDKs and match each against the diagram (AR-010).

## Examples

- [Example 1 — From three generic boxes to a real container design](examples/example-1.md) — corrects AR-001, AR-002.
- [Example 2 — Adding failure behavior to a happy-path design](examples/example-2.md) — corrects AR-003, AR-007.
- [Example 3 — Microservices by default, corrected to a modular monolith](examples/example-3.md) — corrects AR-004.

## Recall anchors

- Start from quality attributes, not components.
- Every container is real; every arrow is labeled.
- Timeout, retry, callee-down — for every call.
- Monolith by default; distribution needs a forcing requirement.
- One writer per store, always.

## Checklist

- [ ] Every container matches a deployable unit, store, or named external system (G-AR-001).
- [ ] Every arrow carries a protocol or format label (AR-002).
- [ ] Every cross-container call states timeout, retry policy, and callee-down behavior (G-AR-003).
- [ ] Data ownership is drawn: exactly one writer per store (G-AR-004).
- [ ] A distributed topology, if any, cites its forcing requirement in an ADR (AR-004).
- [ ] Each significant decision has an ADR written when it was made (AR-008).
- [ ] External systems are named with direction and sync/async marked (AR-010).
