# embeddings-search

## Metadata

- **Owner department:** D17 AI Features (AI)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://developers.openai.com/api/docs/guides/embeddings ; https://www.promptfoo.dev/docs/red-team/owasp-llm-top-10/
- **Depends on:** llm-integration
- **Feeds into:** rag-retrieval, search-relevance, recommendations

## When to use / Do NOT use

- **Use when:** a feature needs semantic or similarity search over a corpus — "find documents like this," natural-language search, similar-items — or when an existing embedding index is built, re-indexed, or its model is changed. This skill owns the embedding and index layer: model choice, chunking, index metadata, hybrid retrieval, and thresholds.
- **Do NOT use when:** the task is the grounded-answer pipeline that consumes retrieved chunks — prompts, citations, abstention (use rag-retrieval), ranking policy and relevance tuning across signals (use search-relevance), or the model call path itself (use llm-integration). This skill ends at returning candidate chunks; what an answer does with them is rag-retrieval's.

## Rules

1. **AI-081 — This layer returns candidates, not answers.** The embedding/index layer embeds, stores, and retrieves chunks with their source IDs and scores. It never assembles prompts, generates text, or decides what an answer claims; rag-retrieval owns that pipeline and consumes this layer's output.
2. **AI-082 — One model per index, recorded with it.** Every index carries metadata naming its embedding model and vector dimension. All vectors in one index come from that one model; a second model's vectors are never inserted, appended, or compared inside it.
3. **AI-083 — A model or dimension change means a full re-embed.** Changing the embedding model or dimension rebuilds the entire index from the source corpus, followed by a recall re-measurement against the recorded baseline (G-AI-042) before rollout. Partial re-indexing under a new model is forbidden.
4. **AI-084 — Queries are embedded by the index's model.** The runtime query embedder is the same model recorded in the index metadata. A query embedded by any other model is never run against the index, even if the dimension happens to match.
5. **AI-085 — Chunking is deliberate and documented.** Chunk size, overlap, and boundary strategy (heading, paragraph, sentence, fixed window) are chosen per corpus, recorded in the indexing configuration with the reason, and changed only against retrieval measurements — never left at a library or tutorial default by accident.
6. **AI-086 — Retrieval is hybrid where exact terms matter.** Vector results are combined with a keyword path so exact names, SKUs, codes, and quoted phrases match literally. The merge strategy (interleave, score blend, keyword-wins-on-exact) is recorded in configuration. A corpus containing identifiers always has the keyword path.
7. **AI-087 — Thresholds and top-K are measured, not copied.** The similarity cutoff and candidate count are tuned on the project's fixed query set of real queries with known relevant items, and the chosen values plus the measurements behind them are recorded. A threshold taken from a tutorial, blog post, or another project is not a value.
8. **AI-088 — The index inherits the corpus's access controls.** Each stored chunk carries the access-control attributes of its source document, and retrieval filters on the requesting user's permissions at this layer, before candidates leave it (OWASP LLM08). An index that returns restricted chunks for callers to filter later is a defect.
9. **AI-089 — Re-indexing is repeatable, and deletes propagate.** Indexing is a documented, scripted operation that can be re-run end to end. Updating or deleting a source document updates or removes its chunks in the index on the next run; a deleted document that still surfaces in search is a defect.
10. **AI-090 — Model selection is an eval decision.** The embedding model is chosen by recall@K measured on the fixed query set against at least one alternative, and the comparison is recorded. "The provider's default" or "the newest model" is not a selection rationale.
11. **AI-091 — Search runs against the real corpus.** The shipped search path queries the production index built from the real corpus. A fixture or sample index may exist only behind a visibly labeled demo mode (see llm-integration AI-012); it is never the shipped default.
12. **AI-092 — Config and index metadata must agree.** Deployment configuration names the expected embedding model and dimension; a mismatch with the index's recorded metadata fails the build/deploy check (G-AI-043) rather than degrading search quality silently.

## BAN list

- **BAN-AI-041 — Search over a fixture presented as the corpus.** Banned: semantic search that queries a small in-memory array, seed file, or sample dataset while the UI presents results as the product's real catalog or corpus. Defeats: DET-FAKE-008. Bad: the help-center search embeds 40 hand-written sample articles shipped in the frontend bundle; a document the admin published yesterday can never be found. Instead: build the index from the real corpus with the scripted indexing run (AI-089) and query that index (AI-091). Severity: BLOCK.
- **BAN-AI-042 — "Semantic search" with no embeddings.** Banned: labeling substring, keyword, or hand-written synonym matching as AI/semantic search when no embedding model or vector index exists anywhere in the path. Defeats: DET-FAKE-009. Bad: the "AI-powered semantic search" badge sits over a function that lowercases the query and checks `title.includes(query)`; a paraphrase of a document's title finds nothing. Instead: embed corpus and queries with one recorded model behind a real index (AI-082, AI-084), or label the feature keyword search and drop the semantic claim. Severity: BLOCK.
- **BAN-AI-043 — Model swapped, index not rebuilt.** Banned: pointing the query embedder at a new model — or re-embedding new documents with it — while old vectors from the previous model remain in the same index. Defeats: DET-FAKE-008. Bad: after a provider model upgrade, new documents are embedded with the new model and appended; search now returns near-random results that no longer track the data, and nobody can say why. Instead: full re-embed of the corpus and a recall re-measurement before rollout (AI-083, G-AI-042). Severity: BLOCK.
- **BAN-AI-044 — Fixed "similar items" list.** Banned: a similar/recommended-items surface that renders the same stored list for every source item instead of computing similarity per item. Defeats: DET-FAKE-017. Bad: every product page shows the same five "You may also like" items from a JSON file, including the product the visitor is already viewing. Instead: compute neighbors from the item's own vector at request or indexing time (AI-081), excluding the item itself. Severity: BLOCK.
- **BAN-AI-045 — Vector-only search for exact identifiers.** Banned: shipping vector-only retrieval on a corpus with SKUs, codes, or proper names, so an exact identifier query returns plausible near-misses presented as matches. Defeats: DET-FAKE-008. Bad: searching the exact part number "XR-2041" returns three semantically related parts and never the XR-2041 record itself. Instead: run the hybrid path so an exact identifier match wins (AI-086) and verify it with G-AI-044. Severity: WARN.

## Gates

- **G-AI-041 — Known-item retrieval test.** Verifies: AI-082, AI-084, AI-091. Check (automated): seed the test index with documents carrying unique marker content, then query with paraphrases of each document (different words, same meaning) and assert each seeded document appears in the top-K results for its paraphrase, e.g. `python scripts/eval_known_items.py --index test --k 10`. Pass: every seeded document is found by its paraphrase query. Fail: block shipment. Recorded in: progress.md.
- **G-AI-042 — Recall baseline gate.** Verifies: AI-083, AI-087, AI-090. Check (automated): run the fixed query set with known relevant items against the index and report recall@K, e.g. `python scripts/eval_recall.py --queries eval/queries.json --index prod`. Pass: recall@K is at or above the recorded baseline; this gate runs before and after any model, chunking, or threshold change, and a regression blocks the change. Fail: block rollout. Recorded in: progress.md.
- **G-AI-043 — Index metadata agreement check.** Verifies: AI-082, AI-092. Check (automated): a deploy-time script reads the index metadata (model name, dimension) and compares it with deployment configuration, e.g. `python scripts/check_index_metadata.py --config config/search.yaml --index prod`. Pass: model and dimension match exactly. Fail: block deployment. Recorded in: progress.md.
- **G-AI-044 — Exact-identifier hybrid test.** Verifies: AI-086. Check (automated): run a recorded set of exact queries — real SKUs, codes, and proper names from the corpus — and assert the exact record is the top result for each. Pass: all exact queries return their record first. Fail: block shipment. Recorded in: progress.md.
- **G-AI-045 — Permission-leak test.** Verifies: AI-088. Check (automated): index a document restricted to a test role, then query as a user without that role using the document's own distinctive terms; assert the restricted chunk appears in no result set. Pass: zero leaks across the restricted-document query set. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Default chunking by habit.** The corpus is split into fixed-size chunks with a copied overlap value and nobody can say what was tried or measured. Catch it by asking for the indexing configuration's recorded rationale (AI-085); if none exists, run the chunking comparison before launch.
- **Boilerplate in the index.** Navigation text, footers, cookie notices, and template chrome are embedded alongside content, so generic queries return chrome-heavy pages. Catch it by inspecting the top results for a few broad queries — repeated boilerplate chunks mean extraction, not embedding, is the problem.
- **Top-K inflation as a recall cure.** Candidate count is raised again and again to mask poor retrieval, pushing cost and noise onto reranking and prompts. Catch it in the recall report: if recall only passes at a K far above what callers consume, fix chunking or the model (AI-085, AI-090), not K.
- **Stale-index drift.** Source documents are edited for weeks while the index is rebuilt "when someone remembers," so search quietly describes an older product. Catch it by comparing the index build timestamp and document count against the corpus on every deploy (AI-089).

## Examples

- [Example 1 — The model swap that silently scrambled search](examples/example-1.md) — violates/corrects AI-083 (BAN-AI-043).
- [Example 2 — The exact part number semantic search could not find](examples/example-2.md) — violates/corrects AI-086 (BAN-AI-045).
- [Example 3 — The 0.8 threshold copied from a tutorial](examples/example-3.md) — violates/corrects AI-087.

## Recall anchors

- One index, one model — a swap means a full re-embed.
- This layer returns candidates; rag-retrieval owns answers.
- Exact names and codes travel the keyword path.
- Thresholds are measured on real queries, never copied.
- If a deleted document still searches, the index is lying.

## Checklist

- [ ] Index metadata records the embedding model and dimension, and deploy config agrees with it (AI-082, AI-092, G-AI-043).
- [ ] Any model or dimension change was a full re-embed with recall re-measured against the baseline before rollout (AI-083, G-AI-042).
- [ ] Chunk size, overlap, and boundary strategy are recorded in the indexing configuration with their rationale (AI-085).
- [ ] A keyword path exists and exact SKUs, codes, and names return their own record first (AI-086, G-AI-044).
- [ ] Similarity threshold and top-K were tuned on the fixed real-query set, with measurements recorded (AI-087, G-AI-042).
- [ ] Chunks carry source access-control attributes and the permission-leak test passes (AI-088, G-AI-045).
- [ ] The known-item paraphrase test passes, and search runs against the real corpus, not a fixture (AI-091, G-AI-041).
- [ ] Re-indexing is scripted and repeatable, and deleted source documents no longer surface (AI-089).
