# D2 Example — System Design for Adding Real-Time Collaboration

## Scenario

The SaaS from the D1 example (a two-person team, one modular codebase, a few
hundred users) wants live cursors and shared editing. D2's job: a container
design, the data-ownership rules, a stack decision with criteria, and the
ADR that records it — before D4 writes any code.

## Before

The design doc, as first drafted:

```markdown
## Architecture
[ Web App ] ---> [ API ] ---> [ Database ]
We will use microservices: auth-service, doc-service, presence-service,
billing-service, each with its own deploy pipeline. All services read and
write the shared Postgres database for simplicity.
Stack: we will use Framework X (very popular right now) with the newest
database everyone's talking about. Diagrams and decisions to be documented
once the system is built.
```

No arrow labels, no failure behavior, no criteria for the stack choice, no
ADR, and the prose names a framework version that the project manifest does
not contain.

## What the skills caught

- **BAN-AR-001 — The generic three-box diagram**: three boxes, unlabeled
  arrows, no protocols, no failure behavior. **AR-002 — Every arrow is
  labeled** and **AR-003 — Failure behavior per call** both fail; the
  container-to-deployable walk **G-AR-001** cannot even start.
- **BAN-AR-003 — Distribution without a forcing requirement**: four services
  for a two-person team with no quality attribute (scale, independent
  deploy, fault isolation) that forces distribution. **AR-004 — Monolith by
  default** and **AR-006 — Quality attributes first** were never applied.
- **BAN-AR-004 — Shared writable database**: every service writes every
  table, violating **AR-005 — One writer per store**; any service can
  corrupt any invariant.
- **BAN-AR-021 — Fashion adoption**: "very popular right now" is the only
  criterion. **AR-041 — Criteria before candidates** and **AR-044 —
  Popularity is not a criterion** fail; the prose/manifest version mismatch
  is **BAN-AR-022 — Version drift between prose and manifest**.
- No decision record at all: **AR-250 — Every significant decision gets
  one** and **AR-008 — Decisions become ADRs when made** fail. Documenting
  "once built" is how decisions become unrecoverable.

## After

One deployable: a modular monolith plus a separate presence process (the
only component with a genuine forcing requirement — thousands of idle
WebSocket connections must not share the request-serving process's fate).

```markdown
## Containers (C4, level 2)
Browser ──HTTPS/JSON──▶ Web app (SSR + API) ──SQL──▶ Postgres (sole writer: app)
Browser ──WSS──▶ Presence service ──Redis pub/sub──▶ Web app (fan-out)
Failure behavior: presence down → editing continues, cursors hidden, banner
shown (AR-003). Postgres down → API returns 503 problem-details, no writes
accepted. Redis down → presence restarts into single-node mode, logged.
```

Data ownership: the web app is the only writer to Postgres; the presence
service owns no durable state. The stack decision is recorded the same day:

```markdown
# ADR-001: Stay a modular monolith; isolate only presence
Status: accepted. Drivers: team of two; p95 API latency budget 300 ms;
deploy frequency weekly. Options: (1) modular monolith + presence process
(chosen); (2) four microservices. Negative consequence accepted: presence
and API share a release train until the monolith is split along the module
boundary this ADR names.
```

That satisfies **AR-243 — At least two considered options** and **AR-244 —
At least one negative consequence**, and the title states the decision
(**AR-247**), not the topic.

## Skills used

- [system-design](../skills/architecture/system-design/SKILL.md)
- [stack-selection](../skills/architecture/stack-selection/SKILL.md)
- [adr-writing](../skills/architecture/adr-writing/SKILL.md)
- [api-architecture](../skills/architecture/api-architecture/SKILL.md)
