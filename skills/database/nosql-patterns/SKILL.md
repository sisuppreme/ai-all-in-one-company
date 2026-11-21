# nosql-patterns

## Metadata

- **Owner department:** D5 Databases & Data (DB)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** pgvector documentation (the counter-pattern: specialized data staying inside Postgres when it fits) — https://access.crunchydata.com/documentation/pgvector/0.8.3/pdf/pgvector.pdf
- **Depends on:** schema-design, data-architecture
- **Feeds into:** data-access, search-engines, vector-db

## When to use / Do NOT use

- **Use when:** a named access pattern is a poor fit for the relational model (document-shaped reads, key-value lookups, wide-column time series, graph traversal), or when reviewing an existing NoSQL data model.
- **Do NOT use when:** the data is relational in shape and Postgres serves it — the relational default stands (use schema-design and sql-fundamentals). Do not reach for this skill because NoSQL feels simpler; simplicity is decided per access pattern, not per project.

## Rules

1. **DB-041 — Patterns before model.** The access patterns are listed, in writing, before any data model is drawn. NoSQL is chosen only for a named pattern the relational model serves badly; "flexible schema" is not a pattern.
2. **DB-042 — Every pattern has a model entry.** Each listed pattern maps to a concrete document shape and query. A pattern with no model entry does not ship; it is remodeled, moved to the relational store, or cut.
3. **DB-043 — Embed together, reference shared.** Data read together is embedded in one document. Data that is shared between documents or grows without bound is referenced, not embedded.
4. **DB-044 — Growth is capped by design.** Every document has a stated maximum size/growth shape. Unbounded arrays and ever-growing embedded lists are forbidden.
5. **DB-045 — One source of truth per field.** Every duplicated field names its single source of truth and a written update strategy (fan-out on write, reconciliation job, or accepted staleness with a stated bound).
6. **DB-046 — Invariants get machinery.** A rule spanning multiple documents is enforced by the engine's transaction support or by an explicit reconciliation job with an owner and a schedule. It is never enforced by hope.
7. **DB-047 — Validation is on.** Schema validation rules (e.g. JSON Schema validators) are enabled on every collection that accepts writes, covering required fields and types.
8. **DB-048 — The exit note exists.** The design document states what would trigger re-evaluating the relational default (a new cross-document pattern, a reporting need, a scale ceiling), so the choice stays a decision instead of becoming an accident.
9. **DB-049 — Postgres first for special data.** Embeddings, JSON documents, and full-text search that fit inside PostgreSQL (pgvector, JSONB, `tsvector`) stay there unless a named need — scale, filtering, analyzer support — says otherwise.
10. **DB-050 — Cross-document joins are a smell.** A read that must reassemble many documents in application code on a hot path means the model is wrong for that pattern: remodel around the pattern or move that pattern to the relational store.

## BAN list

- **BAN-DB-021 — Engine chosen with no pattern list.** Banned: adopting a NoSQL store because it is "flexible," "fast," or "what the tutorial used," with no written access-pattern list behind the choice. Defeats: DET-CODE-015. Bad: the team picks a document store for an order system whose main reads are joins across customers, orders, and payments; the app re-implements joins by hand for a year. Instead: list the patterns first (DB-041); if they are relational, the relational default stands. Severity: WARN.
- **BAN-DB-022 — Unbounded embedded growth.** Banned: embedding an ever-growing array inside a document (all comments inside the post, all events inside the user). Defeats: DET-CODE-033. Bad: a popular post's document grows past the engine's document size limit and writes start failing in production. Instead: reference the growing side from its own collection and keep a capped preview/count on the parent. Severity: WARN.
- **BAN-DB-023 — Cross-document invariants by hope.** Banned: maintaining a rule that spans documents (stock decrement + order creation, balance transfer between accounts) with no transaction and no reconciliation job. Defeats: DET-CODE-030. Bad: the order document is written, the stock update fails silently, and inventory is wrong forever with no process that would ever notice. Instead: use the engine's multi-document transaction, or a reconciliation job that compares the two sides and repairs drift on a schedule. Severity: BLOCK.
- **BAN-DB-024 — Duplication with no owner.** Banned: copying a field into other documents with no named source of truth and no update strategy. Defeats: DET-CODE-027. Bad: `displayName` is copied into 10,000 order documents; a user renames themselves and every historical and current screen disagrees about who they are. Instead: name the source document, and write down how copies are updated or why their staleness is acceptable. Severity: WARN.
- **BAN-DB-025 — Validation disabled on a writable collection.** Banned: a collection that accepts writes with schema validation off or absent, so any shape can be stored. Defeats: DET-CODE-019. Bad: one buggy deploy writes orders missing `total` for a weekend; every downstream read crashes or silently skips them. Instead: enable the validator with required fields and types before the collection accepts traffic. Severity: BLOCK.

## Gates

- **G-DB-021 — Access-pattern coverage check.** Verifies: DB-041, DB-042. Check: manual review against the profiler — each pattern in the design document maps to a query in the repository, and the staging profiler/slow-query log shows no full collection scan serving a listed pattern. Pass: every pattern covered, no collection scans. Fail: block shipment. Recorded in: progress.md.
- **G-DB-022 — Validator presence check.** Verifies: DB-047. Check: automated — a script queries the database metadata (e.g. `listCollections` with options) and asserts every writable collection carries a validator. Pass: all collections validated. Fail: block shipment. Recorded in: progress.md.
- **G-DB-023 — Document-growth test.** Verifies: DB-044. Check: automated — an integration test appends the design's stated maximum number of children to a parent document and asserts the document stays under the design cap (with margin to the engine limit). Pass: size under cap at maximum stated growth. Fail: block shipment. Recorded in: progress.md.
- **G-DB-024 — Reconciliation drill.** Verifies: DB-045, DB-046. Check: automated in staging — run each reconciliation job and assert its drift report is empty; deliberately corrupt one duplicated field and assert the job detects it. Pass: clean report plus detection of the planted drift. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Relational cosplay.** Documents are normalized into tiny pieces and the application re-joins everything on every read — the costs of both models, the benefits of neither. Catch it: count the queries per screen; if a screen needs five round trips to assemble, the model fights the patterns.
- **The junk-drawer document.** Every new feature adds fields to the user document until it is a schema-free attic. Catch it: list the document's fields and ask which access pattern each one serves; orphans get their own home.
- **The eventual-consistency shrug.** Stale duplicated data is waved away as "NoSQL being NoSQL," with no update strategy and no staleness bound. Catch it: for each duplicated field, ask "how does this become right again?" — silence is the finding.
- **Scale theater.** A clustered, sharded deployment is built for a dataset that fits comfortably in one PostgreSQL instance. Catch it: state the data volume and the read/write rates; if they fit the relational default, the burden of proof is on the cluster.

## Examples

- [Example 1 — Modeling from the pattern list](examples/example-1.md) — corrects DB-041, DB-043.
- [Example 2 — Capping document growth](examples/example-2.md) — corrects DB-044.
- [Example 3 — A duplicated field with a source of truth](examples/example-3.md) — corrects DB-045.

## Recall anchors

- Patterns first; the model is the answer to the pattern list.
- Embed what is read together; reference what is shared or unbounded.
- Every duplicated field has one named source of truth.
- Cross-document invariants get transactions or reconciliation — never hope.
- If it fits in Postgres, it starts in Postgres.

## Checklist

- [ ] The access-pattern list exists and every pattern maps to a modeled query (DB-041, DB-042, G-DB-021).
- [ ] Every document shape has a stated growth cap, tested at the cap (DB-044, G-DB-023).
- [ ] Every duplicated field names its source of truth and update strategy (DB-045).
- [ ] Every cross-document invariant uses a transaction or a reconciliation job (DB-046, G-DB-024).
- [ ] Validators are enabled on all writable collections (DB-047, G-DB-022).
- [ ] The exit note states what would trigger re-evaluating the relational default (DB-048).
