# domain-driven-design

## Metadata

- **Owner department:** D2 Architecture & System Design (AR)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Eric Evans, *Domain-Driven Design Reference* (definitions of bounded context, aggregate, ubiquitous language) — https://www.domainlanguage.com/ ; Pattern context for how DDD boundaries interact with data ownership and sagas — https://microservices.io/
- **Depends on:** requirements-writing, system-design
- **Feeds into:** data-architecture, api-architecture, schema-design

## When to use / Do NOT use

- **Use when:** a domain is complex enough that its language and consistency rules drive the design: finding bounded contexts, drawing aggregates around invariants, building the ubiquitous language, or mapping how contexts integrate.
- **Do NOT use when:** the area is plain CRUD over one table with no invariants worth the name — model it as a simple CRUD module (AR-228) and spend the effort elsewhere. Do not use this skill as a naming ceremony for a design already fixed; the language work comes first or not at all.

## Rules

1. **AR-221 — Language first.** The ubiquitous language is built from domain conversations and the requirements before tactical modeling starts; one term has one meaning inside a context.
2. **AR-222 — Contexts are recorded.** Every bounded context has a name, a one-paragraph responsibility, its context-map relationships, and an owning module or service, recorded in ARCHITECTURE.md. A context that exists only in a slide is not a context.
3. **AR-223 — Boundaries follow language shifts.** Where the same word changes meaning (an "order" in sales is not an "order" in fulfillment), that shift marks a context boundary.
4. **AR-224 — Aggregates follow invariants.** If two objects must be consistent in the same transaction, they belong to one aggregate; if not, they reference each other by identity and accept eventual consistency.
5. **AR-225 — References by identity across aggregates.** Code never reaches through one aggregate's object graph into another's internals; cross-aggregate references are by ID.
6. **AR-226 — Declared cross-context mechanisms only.** Contexts communicate through the mechanism the context map declares (API, events, anti-corruption layer). Direct reads of another context's tables are forbidden.
7. **AR-227 — The glossary is testable.** Type, field, and endpoint names inside a context use its glossary terms verbatim; a synonym introduced in code is a defect.
8. **AR-228 — Honest CRUD.** An area that is CRUD over one table is modeled and named as a simple CRUD module, not dressed in tactical DDD vocabulary it does not use.
9. **AR-229 — Inferred terms are flagged.** When no domain expert is available, the glossary is derived from the requirements and fact sheet, and every inferred term is marked UNVERIFIED until a domain source confirms it.
10. **AR-230 — Domain events mark real state changes.** Events crossing a context boundary are named from the domain language for state changes that actually happened (see event-driven), not for technical row mutations.
11. **AR-231 — Invariants are enforced in one transaction.** For every named invariant, one aggregate enforces it atomically; an invariant checked in one transaction and applied in another is unenforced.
12. **AR-232 — Anti-corruption layer at hostile boundaries.** Integration with a legacy or external model goes through an anti-corruption layer that translates it into this context's language; foreign terms never leak inward.

## BAN list

- **BAN-AR-111 — Reading another context's tables.** Banned: one bounded context querying another context's database tables directly. Defeats: DET-CODE-027. Bad: the fulfillment module joins the sales schema's `orders` table, absorbing sales' pricing rules into its own queries; when sales remodels, fulfillment breaks without a single shared contract changing. Instead: consume the sales context's published API or events, through an anti-corruption layer if its model is foreign. Severity: BLOCK.
- **BAN-AR-112 — Synonym drift.** Banned: introducing a code name that differs from the glossary term for the same concept. Defeats: DET-CODE-008. Bad: the glossary says "customer," the API exposes `/clients`, the schema has `buyer_id`, and every cross-team conversation needs a translation table. Instead: rename the code to the glossary term — `customer` everywhere in this context — and treat the rename as a defect fix, not a refactor. Severity: BLOCK.
- **BAN-AR-113 — Tactical theater.** Banned: wrapping plain CRUD in aggregates, repositories, and domain services that add no invariant or language value. Defeats: DET-CODE-015. Bad: a settings page backed by one table ships with a `SettingsAggregate`, a repository interface with one implementation, and a domain service that copies fields — three files where one module sufficed. Instead: model it as an honest CRUD module and reserve tactical patterns for contexts with real invariants. Severity: WARN.
- **BAN-AR-114 — Invariant split across transactions.** Banned: checking a consistency invariant in one transaction and applying the change in another. Defeats: DET-CODE-030. Bad: "never oversell the last seat" is checked by a read, then the booking is written a moment later; two concurrent requests both pass the check and the seat sells twice. Instead: enforce the invariant inside the aggregate's transaction — the seat inventory aggregate decrements and rejects atomically. Severity: BLOCK.

## Gates

- **G-AR-111 — Glossary cross-check.** Verifies: AR-227. Check: manual — sample type and field names from the codebase and API schemas and match each against the context glossaries. Pass: every sampled name is a glossary term used verbatim. Fail: warn; each synonym found is filed as a defect. Recorded in: progress.md.
- **G-AR-112 — Context dependency check.** Verifies: AR-226. Check: automated — CI module-dependency rules fail the build when one context imports another context's internals or connects to its tables. Pass: the check exits 0. Fail: block merge. Recorded in: progress.md.
- **G-AR-113 — Invariant trace.** Verifies: AR-224, AR-231. Check: manual — pick one named invariant and find the aggregate that enforces it, in a single transaction, in code. Pass: the enforcing aggregate and transaction are identified. Fail: block release until the invariant has an owner. Recorded in: progress.md.
- **G-AR-114 — Context record completeness.** Verifies: AR-222. Check: automated — a script over ARCHITECTURE.md asserts every context section carries a name, responsibility paragraph, context-map relationships, and an owning module. Pass: all four fields present for every context. Fail: block merge of the architecture change. Recorded in: progress.md.

## Anti-patterns

- **One context for everything.** A single "domain model" spans sales and fulfillment, and the colliding meanings of its terms are resolved in hallway conversations. Catch it: find a term the glossary defines twice, differently; that is an unmarked boundary.
- **The slide-deck glossary.** The ubiquitous language lives in a presentation while the code evolves its own dialect. Catch it: the glossary is not in the repo, or its last edit predates the last three schema changes.
- **The aggregate of everything.** One giant aggregate serializes all writes through itself because "everything must be consistent." Catch it: measure contention — if unrelated operations queue behind one aggregate, its boundary followed the diagram, not the invariants.
- **Row-mutation events.** Boundary events named `RowUpdated` or `RecordChanged` expose the storage model instead of the domain. Catch it: read the event names aloud to a domain speaker; if they cannot say what happened in the business, the names are technical, not domain.

## Examples

- [Example 1 — One word, two contexts](examples/example-1.md) — corrects AR-223.
- [Example 2 — The cross-context table read, replaced](examples/example-2.md) — corrects AR-226.
- [Example 3 — The oversold seat, fixed at the aggregate](examples/example-3.md) — corrects AR-224, AR-231.

## Recall anchors

- One term, one meaning, per context.
- A word changing meaning marks a boundary.
- Aggregates follow invariants, not diagrams.
- Contexts talk through the map's declared mechanisms only.
- Plain CRUD is modeled as plain CRUD.

## Checklist

- [ ] Every bounded context is recorded with name, responsibility, relationships, and owner (AR-222).
- [ ] The glossary lives in the repo and inferred terms are marked UNVERIFIED (AR-229).
- [ ] Glossary cross-check passed on sampled code and schema names (G-AR-111).
- [ ] Context dependency check exits 0 in CI (G-AR-112).
- [ ] One named invariant was traced to the aggregate enforcing it in a single transaction (G-AR-113).
- [ ] Cross-context integrations use the context map's declared mechanisms, with an ACL where the model is foreign (AR-226, AR-232).
- [ ] CRUD-only areas are named and modeled as CRUD modules (AR-228).
