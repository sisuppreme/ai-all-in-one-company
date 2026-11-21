# performance-optimization

## Metadata

- **Owner department:** D12 Analytics & Observability (AN)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Grafana k6, "Thresholds" — https://grafana.com/docs/k6/next/using-k6/thresholds/ ; web.dev, "Web Vitals" — https://web.dev/articles/vitals
- **Depends on:** performance-budgets, core-web-vitals
- **Feeds into:** performance-budgets

## When to use / Do NOT use

- **Use when:** a measured performance problem exists — a template failing its field p75, an endpoint breaching its p95/p99 target, a load test failing its thresholds, or a client rendering problem (jank, dropped frames, a long list that will not hold its frame rate) — and the job is to find the cause, fix it, and prove the fix with the same instrument that found the problem.
- **Do NOT use when:** the job is setting or changing the numeric limits themselves. **Boundary: performance-budgets sets and enforces the numbers (the budget file, the CI assertions, the field checks); this skill does the fixing work inside those numbers and never edits a budget to make a fix pass.** A budget that is genuinely wrong goes back to performance-budgets as a recorded decision. Diagnosis of a failing vital's subparts belongs to core-web-vitals; the fix itself is executed by the owning department's skill (D3 frontend, D4 backend, D5 data) under this skill's measure–fix–verify loop.

## Rules

1. **AN-241 — No fix without a baseline.** Before any change, record the problem as a measurement: the metric (field p75 vital, API p95/p99, load-test result), its current value, the instrument that produced it, the environment class, and the observation window. A problem stated as "the page feels slow" is not yet work; measure until it has a number.
2. **AN-242 — The after-measurement uses the same harness.** The fix is verified with the identical instrument, configuration, dataset, and environment class as the baseline. A change with no after-measurement on that harness is incomplete; a "should be faster" change whose after-measurement never arrives is reverted.
3. **AN-243 — Optimize the tail, not the average.** Targets are stated at p95/p99 for APIs and p75 for web vitals. An average that improves while the tail worsens is a regression, and the change is reported as one — never as a win with a footnote.
4. **AN-244 — The big costs first, in measured order.** Rank candidate causes by their measured share of the problem — asset and image weight, JavaScript weight and main-thread time, render-blocking resources, query and backend time — and fix the largest first. Micro-optimizations (loop tweaks, memoization, string handling) are not started while a big cost stands unaddressed.
5. **AN-245 — Profile to a specific cause before fixing.** The baseline is decomposed to the named cause — a query plan, a long task, an oversized bundle module, an uncompressed hero image — before code changes. "The endpoint is slow" licenses profiling, not a rewrite.
6. **AN-246 — One optimization per change.** Each change carries exactly one optimization, so the before/after delta attributes to that cause. Bundled optimizations are split; if a combined change regresses, there must never be a guessing game about which part did it.
7. **AN-247 — Image and asset weight is fixed at the source.** When measurement names asset weight: serve images at the dimensions the layout displays, in a modern format, compressed, with below-the-fold media lazy-loaded and the LCP image prioritized. Shipping a 4 MB hero to a phone-sized slot is a defect regardless of how it looked on the office connection.
8. **AN-248 — JavaScript weight is cut, not reshuffled.** When measurement names JS: code-split by route, remove unused code and dependencies, and defer non-critical work off the critical path. The change records the bundle-size delta; moving the same bytes behind a loader is not a reduction.
9. **AN-249 — Queries are bounded and plan-verified.** No optimization ships a query that fetches unbounded rows to filter in memory. Filters, limits, and pagination live in the query; indexes are added only where the query plan (e.g. `EXPLAIN ANALYZE`) shows the scan they remove, and the plan after the change is recorded.
10. **AN-250 — Caching is a correctness decision first.** Before any cache is added, the change writes down what is cached, where, for how long, and how it invalidates. Personalized or per-user responses are never served from a shared cache entry; an optimization that serves stale prices or another user's data is a defect, not a win.
11. **AN-251 — Performance claims require a real load test.** Any claim about behavior under load comes from scripted virtual users on the journeys that matter (sign-in, checkout — not the homepage alone) with codified thresholds that fail the run on breach, e.g. k6 `http_req_failed: ['rate<0.01']` and `http_req_duration: ['p(95)<200']`. "Tested with 10 users, it was fast" is not evidence.
12. **AN-252 — The cost side is recorded.** Every optimization records what it cost: complexity added, a cache to maintain, infrastructure to pay for. Performance work competes honestly with feature work only when its price is written next to its gain.

## BAN list

- **BAN-AN-121 — Unmeasured optimization.** Banned: merging a performance change with no baseline and no after-measurement on the same harness. Defeats: DET-INF-011. Bad: "added memoization across the dashboard, should be much faster now" merges with no number before or after; the p99 never moves and nobody can tell. Instead: record the baseline first, then re-measure on the identical harness and attach the pair to the change (AN-241, AN-242). Severity: BLOCK.
- **BAN-AN-122 — Homepage-only load proof.** Banned: presenting a load test of the homepage alone, or a run with no pass/fail thresholds, as evidence the system is fast under load. Defeats: DET-CODE-012. Bad: a script hammers `/` for a minute, reports a pleasant average, and the checkout journey — never scripted — falls over on launch day. Instead: script the journeys that matter with codified k6 thresholds that fail the run on breach (AN-251). Severity: BLOCK.
- **BAN-AN-123 — Unbounded fetch, optimize later.** Banned: shipping an endpoint that loads an entire table or collection and filters, sorts, or paginates in memory. Defeats: DET-CODE-033. Bad: the orders endpoint loads all 40,000 rows and slices the first page in application code; latency grows linearly with the business. Instead: bound the query with filters, limit, and pagination, verified by the recorded query plan (AN-249). Severity: BLOCK.
- **BAN-AN-124 — Shared cache for personalized responses.** Banned: caching a per-user or price-bearing response under a shared key without a written invalidation rule. Defeats: DET-CODE-030. Bad: the account page is cached under one key at the edge; the second user to arrive sees the first user's balance until the entry expires. Instead: write the cache spec first — what, where, TTL, invalidation — and never share personalized entries (AN-250). Severity: BLOCK.
- **BAN-AN-125 — Whole library for one function.** Banned: importing an entire library or framework module into the shipped bundle to use a single helper, with the unused remainder sent to every user. Defeats: DET-CODE-002. Bad: a date-formatting library ships in full so one page can render one timestamp, adding more JavaScript than the page's own code. Instead: import the single function, code-split it to the route that needs it, and record the bundle delta (AN-248). Severity: WARN.

## Gates

- **G-AN-121 — Before/after evidence check.** Verifies: AN-241, AN-242. Check: automated — a script scans performance-labeled changes for the evidence block: baseline value, after value, instrument, and environment class; a missing field fails the check. Pass: every performance change carries a complete before/after pair from the same harness. Fail: the change is incomplete and does not merge. Recorded in: progress.md.
- **G-AN-122 — Load-threshold re-run.** Verifies: AN-243, AN-251. Check: automated — re-run the k6 suite (or the project's equivalent) in the same environment class as the baseline, e.g. `k6 run load/checkout.js` with thresholds `http_req_failed: ['rate<0.01']` and `http_req_duration: ['p(95)<200']`. Pass: exit code 0 with all thresholds green. Fail: block; the fix is not proven under load. Recorded in: progress.md.
- **G-AN-123 — Budget re-check.** Verifies: AN-244, AN-246. Check: automated — run `lhci autorun` post-change and compare per-template results against the pre-change run. Pass: the performance-budgets CI gate passes and no other template regressed past its budget. Fail: block; an optimization that fixes one template by bloating another does not ship. Recorded in: progress.md.
- **G-AN-124 — Field verification.** Verifies: AN-242, AN-243. Check: scheduled — after the release window, compare the field p75 (vitals) or production p95/p99 (APIs) against the baseline window. Pass: the targeted metric moved in the field, not only in the lab. Fail: the fix is reworked or reverted; it is never reported as done. Recorded in: progress.md.
- **G-AN-125 — Cache correctness test.** Verifies: AN-250. Check: automated — where a cache was added, run the two-user test: authenticate as user A, load the cached response, authenticate as user B, assert B receives only B's data; then mutate the underlying record and assert the cached response reflects the invalidation rule. Pass: no cross-user data and invalidation behaves as written. Fail: block; the cache is removed, not patched around. Recorded in: progress.md.

## Anti-patterns

- **Optimization theater.** A sprint of visible tweaks — minifiers toggled, memoization sprinkled — with no baseline anywhere, so the team feels faster while the field p75 sits still. Catch it: ask for the before/after pair; if none exists, the work has not started (AN-241).
- **The lab mirage.** A throttled desktop lab run on a fast office connection says green while real phones on real networks fail. Catch it: field data is the verdict; the lab is only the flashlight for finding the cause (AN-242, G-AN-124).
- **Premature micro-optimization.** Days spent shaving a string routine while a 4 MB hero image dominates the page weight. Catch it: rank causes by measured share and work down the list (AN-244).
- **The rewrite in perf clothing.** A slow endpoint becomes an excuse to rewrite a working module in a new pattern, unmeasured and unprofiled. Catch it: no profile naming the cause, no change (AN-245).
- **Victory by average.** A release note celebrates mean latency down 20% while p99 doubled. Catch it: read the tail first; the average is the last number on the page (AN-243).

## Examples

- [Example 1 — Memoization without a measurement](examples/example-1.md) — violates/corrects AN-241, AN-242.
- [Example 2 — The 4 MB hero on a phone-sized slot](examples/example-2.md) — violates/corrects AN-244, AN-247.
- [Example 3 — The orders endpoint that loaded everything](examples/example-3.md) — violates/corrects AN-243, AN-249.

## Recall anchors

- Measure first, fix the measured cause, re-measure on the same harness.
- No before/after pair, no optimization — only a guess.
- Big costs first: images, JavaScript, render-blocking, queries — micro last.
- The tail is the target; an average win with a worse p99 is a regression.
- A cache is a correctness decision before it is a speed decision.

## Checklist

- [ ] Baseline recorded with metric, value, instrument, environment class, and window (AN-241).
- [ ] Cause named by profiling before any code changed (AN-245).
- [ ] Causes ranked by measured share; the largest addressed first (AN-244).
- [ ] One optimization in this change, attributable on its own (AN-246).
- [ ] After-measurement taken on the identical harness and attached (AN-242, G-AN-121).
- [ ] Tail checked: p95/p99 or field p75 improved, not only the average (AN-243).
- [ ] k6 threshold re-run green and budget re-check passed (G-AN-122, G-AN-123).
- [ ] Any cache has a written spec and passed the two-user test (AN-250, G-AN-125).
- [ ] Cost side of the optimization recorded in the change (AN-252).
