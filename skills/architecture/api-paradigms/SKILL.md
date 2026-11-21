# api-paradigms

## Metadata

- **Owner department:** D2 Architecture & System Design (AR)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** GraphQL Specification, October 2021 edition — https://spec.graphql.org/October2021/ ; OpenAPI Specification 3.1.0 — https://spec.openapis.org/oas/v3.1.0 ; AsyncAPI Specification 3.1.0 — https://www.asyncapi.com/docs/reference/specification/v3.1.0
- **Depends on:** api-architecture, system-design
- **Feeds into:** event-driven, api-documentation

## When to use / Do NOT use

- **Use when:** choosing the interface paradigm for a new surface (REST, GraphQL, gRPC, event-based, end-to-end-typed RPC), or reviewing whether an existing surface is on the wrong paradigm.
- **Do NOT use when:** the paradigm is already settled and the work is designing within it (api-architecture for REST), or the question is how events themselves are specified once an event-based interface is chosen (event-driven).

## Rules

1. **AR-121 — The choice is an ADR naming the interaction shape.** Every paradigm adoption is recorded in an ADR that names the interaction shape driving it: resource CRUD, client-shaped reads, streaming, or fan-out facts. A paradigm with no stated shape has no justification.
2. **AR-122 — REST is the default.** REST over HTTP+JSON is the default for resource CRUD and for all public APIs. Any other paradigm carries the burden of proof in its ADR.
3. **AR-123 — GraphQL must earn its place.** GraphQL is adopted only when multiple client types need divergent, client-shaped reads over a richly connected graph — and the ADR names those clients and the reads.
4. **AR-124 — GraphQL ships with cost controls.** A GraphQL API ships with query depth and complexity limits and a field deprecation policy (`@deprecated` in the schema). An unbounded public GraphQL endpoint is a defect.
5. **AR-125 — gRPC stays internal by default.** gRPC fits internal service-to-service calls needing strict contracts and streaming performance. Exposing gRPC to public consumers requires an explicit ADR overruling this default.
6. **AR-126 — Events are for facts with independent consumers.** An event-based interface is chosen when multiple consumers react independently to facts. If one producer secretly depends on one specific consumer executing, it is a command, not an event — model it as one.
7. **AR-127 — Typed RPC stays inside one codebase.** tRPC-style end-to-end-typed RPC is acceptable only inside a single TypeScript codebase with no external consumers. The moment an outside client appears, a contract-first paradigm replaces it.
8. **AR-128 — No paradigm hides a modeling problem.** If the resources cannot be named, no paradigm fixes it. Unnameable resources send the work back to domain modeling, not to a more flexible query language.
9. **AR-129 — Every paradigm has its contract artifact.** Each paradigm in use keeps its contract in the repo: OpenAPI for REST, the SDL for GraphQL, `.proto` for gRPC, AsyncAPI for events. No contract artifact, no interface.
10. **AR-130 — Public surfaces get the boring paradigm.** Public consumers get the most boring paradigm that fits (REST first). Internal novelty never leaks into the public surface.
11. **AR-131 — Mixed paradigms are justified per surface.** Mixing paradigms is allowed; each surface's choice is justified by its own interaction shape in its own ADR. One paradigm's justification never covers another surface by association.

## BAN list

- **BAN-AR-061 — The unbounded public GraphQL endpoint.** Banned: exposing GraphQL publicly with no query depth or complexity limits. Defeats: DET-CODE-033. Bad: the public schema accepts arbitrarily nested queries; one recursive query from a curious client pins the resolvers and takes the API down for everyone. Instead: ship depth and complexity limits, and persisted queries where clients are known, before the endpoint is public (AR-124). Severity: BLOCK.
- **BAN-AR-062 — Paradigm by fashion.** Banned: adopting a paradigm with no ADR and no named interaction shape. Defeats: DET-CODE-015. Bad: the new public API is GraphQL "because the frontend lead prefers it"; the API is plain CRUD for one web client, and the team now owns schema governance it never needed. Instead: write the ADR naming the interaction shape, or take the REST default (AR-121, AR-122). Severity: BLOCK.
- **BAN-AR-063 — The contractless interface.** Banned: an interface in production with no contract artifact in the repo. Defeats: DET-CODE-004. Bad: a gRPC service ships with the `.proto` file living only in one developer's generated code; consumers reverse-engineer the wire format and break on every regeneration. Instead: commit the contract artifact — OpenAPI, SDL, `.proto`, or AsyncAPI — as the interface's source of truth (AR-129). Severity: BLOCK.
- **BAN-AR-064 — Flexibility as a modeling shortcut.** Banned: choosing GraphQL or generic RPC to avoid naming the domain's resources. Defeats: DET-CODE-008. Bad: the team cannot agree on what an "order" is, so the API becomes a generic query surface over the database tables; the disagreement is now encoded in every client's queries instead of resolved in the model. Instead: return to domain modeling until the resources can be named, then pick the paradigm (AR-128). Severity: WARN.

## Gates

- **G-AR-061 — Contract artifact validation.** Verifies: AR-129. Check: automated — CI validates whichever artifacts exist: OpenAPI lint for REST, GraphQL SDL validation against the spec's type-system rules, `protoc` compilation for gRPC, AsyncAPI validation for events. Pass: every artifact validates. Fail: block merge. Recorded in: progress.md.
- **G-AR-062 — GraphQL limits check.** Verifies: AR-124. Check: automated — if a GraphQL schema exists, a script confirms the server configuration sets a maximum query depth and a complexity limit, and the schema's deprecations use `@deprecated`. Pass: both limits configured. Fail: block release. Recorded in: progress.md.
- **G-AR-063 — ADR-to-traffic review.** Verifies: AR-121, AR-123, AR-131. Check: manual — for each paradigm in use, read its ADR and compare the stated interaction shape with the API's actual dominant traffic (logs or analytics). Pass: every paradigm's stated shape matches its real traffic. Fail: warn and open a re-evaluation ADR. Recorded in: progress.md.

## Anti-patterns

- **Paradigm tourism.** Each new service picks a different paradigm because each author wanted to try one. Catch it: list the surfaces and their paradigms; if the count of paradigms approaches the count of services, AR-131's per-surface justification has become a rubber stamp.
- **REST in name only.** A "REST API" that is verb-named POST endpoints over HTTP — RPC wearing REST's clothes, gaining none of its properties. Catch it: if removing the HTTP method names changes nothing about how clients call it, send it to api-architecture for remodeling.
- **The internal leak.** An internal convenience (gRPC streaming, typed RPC) exposed publicly because "it already works." Catch it: check AR-130 — public consumers inherit your internal constraints and cannot be migrated when you change your mind.
- **Events as hidden commands.** A producer that blocks, retries, or alarms until one specific consumer processes its "event." Catch it: if the producer cares which consumer acts, it issued a command; model the dependency honestly (AR-126).

## Examples

- [Example 1 — GraphQL proposed for plain CRUD, REST chosen instead](examples/example-1.md) — corrects AR-122, AR-123.
- [Example 2 — Cost controls added to a public GraphQL API](examples/example-2.md) — corrects AR-124.
- [Example 3 — Splitting a leaked internal paradigm from the public surface](examples/example-3.md) — corrects AR-125, AR-130.

## Recall anchors

- Name the interaction shape, or take the REST default.
- GraphQL earns its place — and ships with cost controls.
- gRPC internal, events for facts, typed RPC inside one codebase.
- No contract artifact, no interface.
- Public consumers get the boring paradigm.

## Checklist

- [ ] Every paradigm in use has an ADR naming its interaction shape (AR-121).
- [ ] Public surfaces use REST unless an ADR proves another paradigm (AR-122, AR-130).
- [ ] GraphQL, where used, has depth/complexity limits and a deprecation policy (G-AR-062).
- [ ] Every interface has its contract artifact in the repo, validating in CI (G-AR-061).
- [ ] Event-based surfaces carry facts for independent consumers, not hidden commands (AR-126).
- [ ] Typed RPC, where used, has no external consumers (AR-127).
- [ ] Each mixed-paradigm surface is justified by its own ADR (AR-131).
