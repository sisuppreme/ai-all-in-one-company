# vector-db

## Metadata

- **Owner department:** D5 Databases & Data (DB)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** pgvector documentation — https://access.crunchydata.com/documentation/pgvector/0.8.3/pdf/pgvector.pdf
- **Depends on:** schema-design, indexing, data-access
- **Feeds into:** embeddings-search, rag-retrieval, search-engines

## When to use / Do NOT use

- **Use when:** a feature needs nearest-neighbor search over embeddings — semantic search, recommendations, retrieval for AI features — and the embedding store, index, and recall bar are being designed or changed.
- **Do NOT use when:** the need is keyword or structured search (use search-engines), or the corpus is small enough that an exact scan inside a normal query is simpler and fast — do not add an ANN index to a table whose full scan is already cheap.

## Rules

1. **DB-281 — Operator matches index.** The distance operator in the query (`<=>` cosine, `<#>` inner product, `<->` L2) is the one the embedding model was trained for, and the index is built with the matching operator class. A mismatched query silently falls back to a full scan.
2. **DB-282 — Dimension is fixed and validated.** Each vector column has one dimension, equal to the producing model's output dimension. Writes are validated against it; a wrong-dimension vector is rejected, never truncated or padded.
3. **DB-283 — Model identity is stored.** Every embedding row records its source record, model name, and model version. Embeddings from different model versions never share an index without a version filter on every query.
4. **DB-284 — Recall is measured, not assumed.** ANN recall is measured against exact search on a fixed sample query set before launch and after any index-parameter change, and the measured figure is recorded next to the threshold it must meet.
5. **DB-285 — Embeddings are derived data.** Every embedding traces to its source record and the chunking rule that produced it. When a source record is deleted, its embeddings are deleted in the same flow.
6. **DB-286 — pgvector is the default.** Embeddings live in PostgreSQL via pgvector unless a named scale or filtering need that Postgres cannot meet is written down. A dedicated vector database is an escalation with a stated reason, not a default.
7. **DB-287 — Index type is a recorded choice.** HNSW is the default index (better speed/recall trade-off); IVFFlat is chosen when build time or memory dominates. The choice and its parameters are recorded with the schema.
8. **DB-288 — The index is earned by volume.** An ANN index is created once data volume makes exact scan hurt, measured on production-shaped data. Below that threshold, exact search is the honest implementation.
9. **DB-289 — One writer stamps identity.** All embedding writes go through one code path that stamps model name, model version, and dimension. A model change triggers a planned re-embed (backfill, verify, swap), never in-place mixing.
10. **DB-290 — Filtered recall is tested too.** Queries that combine vector search with tenant or metadata filters are included in the recall sample set; a filter that collapses recall or leaks across tenants fails the same bar as unfiltered search.

## BAN list

- **BAN-DB-141 — The decorative index.** Banned: shipping a nearest-neighbor query whose operator does not match the index operator class, so the ANN index is never used and every query is a full scan. Defeats: DET-CODE-033. Bad: the index is built with `vector_cosine_ops` but queries use `<->` (L2); `EXPLAIN` shows a sequential scan over 2M rows at 800 ms per search. Instead: build the index with the operator class matching the model's distance and the query operator, and prove index use with `EXPLAIN`. Severity: BLOCK.
- **BAN-DB-142 — Mixed-model index.** Banned: writing embeddings from a new model version into an index that still holds the previous version's vectors, with no version filter. Defeats: DET-CODE-032. Bad: the embedding model is upgraded in a deploy; for a week the index returns neighbors from two incompatible vector spaces and result quality quietly rots. Instead: stamp every row with model version (DB-283), re-embed into a new column or table, verify recall, then swap. Severity: BLOCK.
- **BAN-DB-143 — Unvalidated dimensions.** Banned: inserting embedding vectors without checking their dimension against the column and model. Defeats: DET-CODE-019. Bad: a provider change returns 768-dimension vectors into a 1536-dimension pipeline; the write path pads them with zeros and search returns garbage instead of an error. Instead: reject any vector whose dimension differs from the column's declared dimension, at the single writer (DB-289). Severity: BLOCK.
- **BAN-DB-144 — Recall by vibes.** Banned: launching ANN search, or changing HNSW/IVFFlat parameters, with no recall measurement against exact search. Defeats: DET-CODE-013. Bad: `ef_search` is lowered to cut latency; nobody measures recall, which fell from 0.97 to 0.71, and users just see worse results. Instead: run the recall-vs-exact check on the fixed query set and record the figure before the change ships (DB-284). Severity: BLOCK.

## Gates

- **G-DB-141 — Index-use plan check.** Verifies: DB-281, DB-288. Check: automated — run `EXPLAIN` on the production nearest-neighbor query against a production-shaped fixture and assert the plan names the HNSW/IVFFlat index, not a sequential scan. Pass: index scan present in the plan. Fail: block shipment. Recorded in: progress.md.
- **G-DB-142 — Recall-vs-exact check.** Verifies: DB-284, DB-290. Check: automated — for each query in the fixed sample set, compare ANN top-k against exact top-k (index disabled) and compute recall, including the tenant-filtered queries; where no recorded production query set exists yet, the sample set is generated by the synthetic fixture procedure in example-4. Pass: recall meets or exceeds the threshold recorded with the index. Fail: block shipment until parameters or index are fixed. Recorded in: progress.md.
- **G-DB-143 — Identity audit.** Verifies: DB-282, DB-283, DB-289. Check: automated — SQL audit asserting zero embedding rows whose model version differs from the current version without a filter migration in progress, and zero rows whose vector dimension differs from the column definition. Pass: both counts are zero. Fail: block the release. Recorded in: progress.md.
- **G-DB-144 — Orphan sweep.** Verifies: DB-285. Check: automated — count embeddings whose source record no longer exists. Pass: the count is zero. Fail: block until the delete flow removes orphans with their sources. Recorded in: progress.md.

## Anti-patterns

- **Toy-data benchmarks.** Recall and latency are measured on a few hundred rows, where every strategy looks fast and exact. Catch it: the fixture's row count is stated next to every measurement; a benchmark without a production-shaped volume is not evidence.
- **Parameter astrology.** HNSW/IVFFlat parameters are copied from a blog post or tuned until one demo query looks right. Catch it: every parameter value traces to a recall measurement on the project's own query set (DB-284), not to an article.
- **Embedding hoarding.** Every chunking experiment and model trial leaves its vectors in the table "just in case". Catch it: the identity audit (G-DB-143) shows one current model version; anything else is a migration in progress or a deletion that has not happened.
- **Post-filter top-k.** The query takes the global top-k first and applies the tenant filter afterward, so tenants see thin or wrong result sets. Catch it: filtered queries are in the recall set (DB-290); an unfiltered-only test suite is the tell.

## Examples

- [Example 1 — An index the query never used](examples/example-1.md) — corrects DB-281.
- [Example 2 — A model upgrade that mixed two vector spaces](examples/example-2.md) — corrects DB-283.
- [Example 3 — Recall measured before the parameter change shipped](examples/example-3.md) — corrects DB-284.
- [Example 4 — A generated recall fixture](examples/example-4.md) — corrects DB-284.

## Recall anchors

- The query operator and the index operator class are one decision.
- Dimension and model version are stamped on every row.
- Recall is a measured number with a threshold, not a hope.
- Embeddings die with their source record.
- pgvector first; a dedicated vector store needs a written reason.

## Checklist

- [ ] Query operator matches the index operator class and the model (DB-281).
- [ ] `EXPLAIN` shows the ANN index in use on production-shaped data (G-DB-141).
- [ ] Every row carries source, model name, and model version (DB-283).
- [ ] Recall vs exact meets the recorded threshold, filtered queries included (G-DB-142).
- [ ] Wrong-dimension writes are rejected at the single writer (DB-282, DB-289).
- [ ] Deleting a source record deletes its embeddings (DB-285).
- [ ] Index type and parameters are recorded with their reason (DB-287).
