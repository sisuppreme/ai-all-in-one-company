# search-relevance

## Metadata

- **Owner department:** D17 AI Features (AI)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://cloud.google.com/generative-ai-app-builder/docs/custom-ranking ; https://docs.cloud.google.com/generative-ai-app-builder/docs/ranking
- **Depends on:** embeddings-search
- **Feeds into:** ai-evaluation, ai-observability

## When to use / Do NOT use

- **Use when:** building or tuning a search feature whose results are ranked — candidate retrieval, ranking signals and weights, filters and sorting, zero-result handling — or when a ranking change, boost, or reranker is proposed.
- **Do NOT use when:** the task is indexing and embedding the corpus (use embeddings-search), answering questions from retrieved documents (use rag-retrieval), or ranking a personalized recommendation feed (use recommendations). This skill owns the relevance of query-driven search results.

## Rules

1. **AI-121 — Ranking is tuned against a maintained judged query set.** The set holds real queries drawn from query logs, each with graded relevance labels for its expected results. It is versioned in the repo, and it — not opinion — is the baseline every tuning decision is measured against.
2. **AI-122 — No ranking change ships without an offline NDCG comparison.** Before release, the candidate ranking is scored against the current ranking on the judged set (AI-121) and NDCG@10 for both is recorded in the change. A regression blocks the release.
3. **AI-123 — The judged set grows from real query logs.** Each review cycle, zero-result queries and reformulated queries (the user immediately searched again in different words) are triaged: labeled and added to the set, or fixed and recorded as fixed.
4. **AI-124 — Zero-result rate is a monitored metric with a named owner.** Every zero-result search is logged with its query and active filters. The owner reviews the log on the recorded cycle and fixes causes — missing synonyms, unhandled spelling variants, indexing gaps — at the cause, not per complaint.
5. **AI-125 — Fixes target the query class, never one query.** A change must improve the class of queries that share the failure (a synonym group, a field-weight problem, an indexing gap). A boost, pin, or special case that helps exactly one query string is forbidden.
6. **AI-126 — A zero-result search returns an honest recovery state.** The state says that nothing matched, shows the active query and filters, and offers a working path: clear or loosen filters, corrected spelling, or the closest broader category. A blank area is never the answer.
7. **AI-127 — Filters never silently contradict the query.** Active filters are always visible, result counts are computed by the same query that produces the results, and when a filter combination excludes everything the query itself would match, the UI says so and offers to remove the conflicting filter.
8. **AI-128 — Paid and boosted placement is labeled and kept honest.** Sponsored or business-boosted results carry a visible label and are visually distinguishable from organic results. Payment never changes the organic ranking order while the surface presents that order as relevance.
9. **AI-129 — Sort labels say what the sort does.** The default order may be labeled "Relevance" only when it is produced by the ranking signals (AI-132). An order by date, price, or popularity is labeled by that field, never dressed up as relevance.
10. **AI-130 — Any LLM reranker carries a latency and cost budget.** The reranker runs under a recorded per-query latency budget and cost budget, with a timeout that falls back to the non-LLM ranking. A reranker with no budget or no fallback is forbidden.
11. **AI-131 — Search queries the real index over the real dataset.** Queries reach a server-side index over the full catalog or corpus; a record added through the product becomes findable without a redeploy. Filtering a small client-side array and presenting it as the catalog is forbidden.
12. **AI-132 — Ranking signals are explicit, weighted configuration.** The signals (semantic relevance, keyword match, freshness, popularity, document fields, business rules) and their weights live in one versioned ranking configuration. Scattered hard-coded boosts in feature code are forbidden.

## BAN list

- **BAN-AI-061 — Search with canned results.** Banned: every query returning the same fixture list, or results filtered client-side from a small hard-coded array presented as the catalog. Defeats: DET-FAKE-008. Bad: searching "invoice export", "zzzqqq", and a term from a record created a minute ago all return the same eight products. Instead: query the server index over the real dataset so contents and counts vary with the query and the data (AI-131). Severity: BLOCK.
- **BAN-AI-062 — Sort and filter controls that only rearrange a fixture.** Banned: sort, filter, and pagination controls that reorder one small hard-coded set while counts and pages claim a larger dataset. Defeats: DET-FAKE-017. Bad: "Sort by relevance" and "Sort by newest" return the same twelve items in slightly different orders, and page 2 repeats page 1. Instead: execute filtering, sorting, and pagination against the real dataset with counts derived from the same query (AI-127, AI-131). Severity: BLOCK.
- **BAN-AI-063 — Blank zero-result state.** Banned: a search that matches nothing renders an empty container with no explanation. Defeats: DET-UX-009. Bad: a misspelled query leaves a white gap under the search box; the user cannot tell whether search is broken, loading, or genuinely empty. Instead: render the recovery state — what matched nothing, the active constraints, and the next action (AI-126). Severity: WARN.
- **BAN-AI-064 — Filter dead end with invisible constraints.** Banned: a filter combination returning zero results while the active filters are hidden and no clear-or-adjust action exists. Defeats: DET-UX-025. Bad: three facets are still applied from an earlier session; every new search returns nothing and the page offers no way to see or remove them. Instead: show active filters on the results view and offer one-action clear/broaden whenever results are empty (AI-126, AI-127). Severity: WARN.
- **BAN-AI-065 — Paid placement disguised as relevance.** Banned: sponsored or boosted items inserted into the organic order, unlabeled, so payment reads as relevance. Defeats: DET-FAKE-017. Bad: a vendor's product sits at position 1 for unrelated queries under a "Best match" heading, with no label and no entry in the ranking configuration. Instead: label boosted placement visibly, keep it distinguishable from the organic order, and record every boost in the ranking configuration (AI-128, AI-132). Severity: BLOCK.

## Gates

- **G-AI-061 — Offline NDCG regression gate.** Verifies: AI-121, AI-122. Check (automated): run the project's eval script, e.g. `python3 scripts/search_eval.py --judged search/judged-queries.json --candidate candidate --baseline current`, which prints NDCG@10 for both rankings. Pass: candidate NDCG@10 is at or above the baseline, and both scores are recorded in the change. Fail: block shipment. Recorded in: progress.md.
- **G-AI-062 — Zero-result audit.** Verifies: AI-123, AI-124. Check (automated): run the zero-result report over the period's query log, e.g. `python3 scripts/zero_result_report.py --log search-queries.log`, which prints the zero-result rate and the untriaged zero-result queries. Pass: the rate is at or below the recorded threshold and every listed query is either added to the judged set with labels or recorded as fixed with its cause. Fail: block shipment of the ranking release. Recorded in: progress.md.
- **G-AI-063 — Findability and honesty probe.** Verifies: AI-131. Check (automated): create a record containing a unique marker term through the product's normal write path, search the marker, then search a gibberish string. Pass: the marker search returns the new record with no redeploy, and the gibberish search returns the honest zero-result state (AI-126). Fail: block shipment. Recorded in: progress.md.
- **G-AI-064 — Filter recovery walk.** Verifies: AI-126, AI-127. Check (manual): in the running product, run a nonsense search, then apply a filter combination that excludes everything the query matches. Pass: both cases show what matched nothing, display the active query and filters, and offer a working clear/broaden action; counts shown equal the results the same query returns. Fail: block shipment. Recorded in: progress.md.
- **G-AI-065 — Placement and label audit.** Verifies: AI-128, AI-129, AI-132. Check (automated + manual): diff the ranking configuration for the release — every boost or pin must appear there with a reason — then inspect the rendered results for a boosted query. Pass: no boost exists outside the configuration, every boosted item carries its label in the UI, and the default sort is labeled "Relevance" only when produced by the configured signals. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **The manager's query.** One stakeholder searches once, dislikes the order, and the team starts tuning to that single anecdote. Catch it by asking which judged-set queries the change improves — if the answer names one person's search, it is AI-125 failing in conversation before it fails in code.
- **Freshness creep.** A "small" change makes results effectively sort by date, and within a month the default order is a changelog wearing a "Relevance" label. Catch it by checking the recorded NDCG delta and the effective signal weights in the ranking configuration at each release.
- **Synonym whack-a-mole.** Each zero-result complaint gets its own one-off synonym until the table is an unmaintainable list of individual grievances. Catch it in the zero-result report: fixes should cluster into classes (spelling, indexing gaps, missing fields), not accumulate as singletons.
- **Reranker by vibes.** An LLM reranker is added because it "feels smarter," with no judged-set score, latency measurement, or timeout behavior recorded. Catch it by asking for its G-AI-061 scores and its budget line — if neither exists, it is decoration, not ranking.

## Examples

- [Example 1 — The same eight results for every query](examples/example-1.md) — violates/corrects AI-131 (BAN-AI-061).
- [Example 2 — The manager's pinned product](examples/example-2.md) — violates/corrects AI-122, AI-125, AI-132 (BAN-AI-065).
- [Example 3 — The zero-result dead end](examples/example-3.md) — violates/corrects AI-124, AI-126, AI-127 (BAN-AI-064).

## Recall anchors

- No judged set, no tuning — opinion is not a baseline.
- Every ranking change records its NDCG delta.
- Zero results are logged, owned, and fixed at the cause.
- Fix the query class, never the one query.
- Boosted is labeled, or it does not ship.

## Checklist

- [ ] The judged query set is versioned, built from real queries with graded labels, and grew this cycle from zero-result and reformulated queries (AI-121, AI-123).
- [ ] The release records candidate vs. baseline NDCG@10 and shows no regression (AI-122, G-AI-061).
- [ ] The zero-result rate is reported, at or below threshold, with an owner and every untriaged query resolved (AI-124, G-AI-062).
- [ ] A newly created record is findable by search without a redeploy, and gibberish returns the honest empty state (AI-131, G-AI-063).
- [ ] Zero-result and impossible-filter states explain themselves, show active constraints, and offer a working recovery action (AI-126, AI-127, G-AI-064).
- [ ] All boosts live in the ranking configuration with reasons; boosted items are labeled in the UI; sort labels name the actual sort (AI-128, AI-129, AI-132, G-AI-065).
- [ ] Any LLM reranker has a recorded latency and cost budget and a tested timeout fallback to the non-LLM ranking (AI-130).
