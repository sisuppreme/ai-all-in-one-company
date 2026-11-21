# ai-cost-control

## Metadata

- **Owner department:** D17 AI Features (AI)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://www.promptfoo.dev/docs/red-team/owasp-llm-top-10/ ; https://docs.langchain.com/langsmith/cost-tracking
- **Depends on:** llm-integration, ai-observability
- **Feeds into:** ai-evaluation

## When to use / Do NOT use

- **Use when:** an AI feature is being designed, routed to a model, given quotas or budgets, or reviewed for spend — and whenever a cost or savings figure about an AI feature is about to be stated anywhere.
- **Do NOT use when:** the task is recording traces and usage in the first place (use ai-observability; this skill consumes its metering stream), choosing a model on quality grounds alone (use ai-evaluation for the scores that justify a tier), or setting product prices (an operator business decision this skill only supplies unit costs for).

## Rules

1. **AI-181 — Every feature has a named budget and an owner.** Before release, each AI feature records in configuration: a per-request token budget, a per-user quota, a per-period spend budget, and the person or role who owns them. A feature with no recorded budget does not ship; "the provider invoice" is never the first signal of overspend.
2. **AI-182 — Cost is computed from metered usage, never hard-coded rates.** The wrapper records tokens in and out for every call (see ai-observability), and cost is computed as metered tokens multiplied by the operator's current price sheet. The price sheet lives in one configuration location, names its source and the date it was last checked, and is the only thing that changes when a provider reprices; no price, rate, or per-call cost figure is written into feature code.
3. **AI-183 — Caps are enforced in the wrapper, server-side.** When a per-user quota or a per-feature budget is reached, the wrapper stops the call or degrades it (AI-188) before any provider request is made. An alert, email, or dashboard warning by itself is not enforcement and does not satisfy this rule.
4. **AI-184 — Retries and loops have hard bounds.** Every call path records a maximum retry count with backoff, a maximum iteration count for agent or tool loops, and a maximum spend per task or session. Hitting any bound terminates the path with a typed error; there is no code path in which a failure can retry, loop, or re-plan without limit.
5. **AI-185 — Model tier is justified by eval scores at that tier.** Simple tasks (classification, extraction, short rewrites) route to the smallest model whose recorded eval results meet the feature's quality floor (see ai-evaluation). Defaulting a task class to the largest available model requires a stored eval comparison showing the cheaper tier fails the floor.
6. **AI-186 — Caching is exact-match and disclosed.** Responses may be cached only for identical requests, with a cache key that includes the prompt version and model ID. A cache hit is marked as a hit in the trace and in any usage report; a cached or template response is never presented to a user or a report as a fresh model generation.
7. **AI-187 — Context is budgeted, not stuffed.** Prompt assembly enforces a maximum input-token budget per request. Retrieved chunks, history, and examples are selected or truncated by a stated policy that fits the budget; assembly never sends whatever happens to fit the provider's context window.
8. **AI-188 — Degradation is graceful and honest.** When a budget or quota is exhausted, the feature degrades along a documented path — cheaper model, reduced context, non-AI fallback, or a plain statement that the feature is unavailable — and the trace records that degradation occurred. Silently lowering quality while presenting the output as full-strength is forbidden.
9. **AI-189 — Every paid-model endpoint has a per-user quota.** Quotas and rate limits apply to authenticated and unauthenticated endpoints alike, are enforced server-side, and are counted from server-side records. A limit that lives only in client state, a cookie, or the UI does not count as a quota.
10. **AI-190 — Cost is reported per feature and per model.** On a fixed cycle, each feature's report shows metered usage, spend against its budget, and unit cost (spend divided by successful tasks or requests), broken down by model. A feature whose unit cost crosses its recorded threshold is flagged for a routing, caching, or retirement review — an unprofitable feature must be visible, not averaged away.
11. **AI-191 — Abuse is treated as a cost attack.** Maximal-size requests, high-frequency calls from one identity, and inputs designed to induce loops or maximal output are rate-limited and bounded like any other unbounded-consumption threat (OWASP LLM10:2025). Cost limits are part of the security design, not only the finance design.
12. **AI-192 — A cost figure carries its provenance.** Any cost, unit-cost, or savings figure stated in a UI, report, or release note names the metering period, the feature scope, and the price-sheet date it was computed from. A figure that cannot be recomputed from stored traces under AI-182 is not published.

## BAN list

- **BAN-AI-091 — Alert-only cap presented as enforcement.** Banned: a budget or quota whose only effect at the limit is sending an alert, while calls continue and the UI shows the feature as "protected." Defeats: DET-FAKE-022. Bad: the admin panel shows "Monthly cap set — spend protected," the cap passes on a Tuesday, an email goes to an unmonitored inbox, and calls run unbounded until the invoice arrives. Instead: enforce the cap in the wrapper before the provider call (AI-183) and degrade honestly at the limit (AI-188); alerts are an addition to enforcement, never a substitute. Severity: BLOCK.
- **BAN-AI-092 — Frozen cost dashboard.** Banned: an AI spend or usage display rendered from constants, estimates typed into config, or a one-time snapshot, presented as the feature's actual consumption. Defeats: DET-FAKE-004. Bad: the "AI costs" panel shows a tidy figure computed at launch from expected volume; real usage triples and the panel never moves. Instead: compute every displayed figure from the metered traces for the stated period (AI-182, AI-190). Severity: BLOCK.
- **BAN-AI-093 — Silent canned or cached substitution.** Banned: serving stored, template, or previously generated responses in place of model calls to save money, while the UI and reports present them as live model output. Defeats: DET-FAKE-009. Bad: similar prompts are answered from a template table "to control costs," users believe they are talking to the model, and usage reports count the answers as generations. Instead: cache only identical requests, mark hits in the trace, and disclose any non-model fallback where it is served (AI-186, AI-188). Severity: BLOCK.
- **BAN-AI-094 — Cost report fabricated from hard-coded rates.** Banned: a cost report or export whose figures are computed from prices or per-call costs written into code or a spreadsheet, rather than from metered tokens and the current price sheet. Defeats: DET-FAKE-019. Bad: the monthly export multiplies request counts by a per-call price typed in at launch; the provider repriced twice since, and finance is reconciling against numbers that were never real. Instead: generate every report from stored traces with the dated price sheet named on it (AI-182, AI-192). Severity: BLOCK.
- **BAN-AI-095 — Client-side quota counter.** Banned: a per-user AI usage limit counted in browser state, local storage, or a cookie, so reloading, clearing storage, or calling the API directly resets it. Defeats: DET-FAKE-005. Bad: free-tier users get "10 AI summaries a day" enforced by a counter in the page; a hard reload restores all 10 and a script bypasses the limit entirely. Instead: count usage in server-side records keyed to the user or identity and enforce the quota in the wrapper (AI-189, AI-183). Severity: BLOCK.

## Gates

- **G-AI-091 — Budget-guard test.** Verifies: AI-181, AI-183, AI-189. Check (automated): in staging, set a low test per-user quota and a low test per-feature budget, then drive scripted traffic past both. Pass: once each limit is reached, further provider calls are stopped or degraded per AI-188, the alert fires, and the trace records the enforcement; zero provider calls occur past the cap. Fail: block release. Recorded in: progress.md.
- **G-AI-092 — Runaway-loop test.** Verifies: AI-184, AI-191. Check (automated): fault-inject with a provider stub that returns retryable errors indefinitely, plus a tool-loop scenario whose plan never converges. Pass: both paths terminate at the recorded retry, iteration, or spend bound with a typed error, and total tokens consumed stay at or below the bound's ceiling. Fail: block release — an uncapped loop is a release blocker. Recorded in: progress.md.
- **G-AI-093 — Metering reconciliation.** Verifies: AI-182, AI-190. Check (automated): run a known set of test calls with recorded token counts, then recompute the feature's reported spend from the stored traces and the current price sheet. Pass: every test call has a trace with tokens in/out and model ID, and the recomputed total matches the reported total exactly. Fail: cost reporting is treated as unmeasured and fixed before the next report is published. Recorded in: progress.md.
- **G-AI-094 — Routing evidence check.** Verifies: AI-185. Check (manual): open the routing configuration for each feature and list every task class with its assigned model tier. Pass: each tier assignment links an eval report at that tier meeting the feature's floor, and any largest-tier assignment links the comparison showing the cheaper tier fails. Fail: unproven task classes are re-routed to the smallest tier or the eval is run before release. Recorded in: progress.md.
- **G-AI-095 — Degradation drill.** Verifies: AI-186, AI-188. Check (manual): exhaust a test budget in staging and use the feature as an end user, including repeating an earlier request exactly. Pass: the user sees the documented fallback or a clear unavailability statement, any cached answer is identifiable as cached in the trace, and nothing is presented as full-strength model output that was not generated at full strength. Fail: block release. Recorded in: progress.md.

## Anti-patterns

- **Invoice-driven discovery.** Nobody can say what a feature costs until the provider bill lands, and the post-mortem is an argument about whose usage it was. Catch it by asking for last cycle's per-feature report (AI-190): if it does not exist, cost control does not exist either.
- **Blended-average comfort.** A single average cost per request across all features hides the one feature burning the budget behind nine cheap ones. Catch it by refusing any cost report without the per-feature, per-model breakdown AI-190 requires.
- **Retry-as-reliability.** Flaky outputs are "fixed" by raising retry counts and timeouts, quietly multiplying spend per successful task. Catch it in review: any retry-count increase without a bound check against AI-184 and a unit-cost note is a cost change disguised as a reliability change.
- **Launch-day price sheet.** The price sheet was copied once at launch and never re-checked, so every computed cost has been drifting from reality since the first repricing. Catch it by reading the sheet's recorded check date (AI-182): an old date invalidates every figure derived from it.

## Examples

- [Example 1 — The cap that only sent an email](examples/example-1.md) — violates/corrects AI-183 (BAN-AI-091).
- [Example 2 — The retry loop that billed all weekend](examples/example-2.md) — violates/corrects AI-184.
- [Example 3 — The dashboard that never moved](examples/example-3.md) — violates/corrects AI-182, AI-190 (BAN-AI-092).

## Recall anchors

- No recorded budget and owner, no ship — the invoice is never the first signal.
- Cost = metered tokens × the operator's current price sheet; rates never live in code.
- A cap that only alerts does not exist; enforcement happens in the wrapper, before the call.
- Every retry, loop, and task has a hard bound — an uncapped loop is a release blocker.
- Cheapest tier the evals justify, honest degradation at the limit, per-feature reports or it didn't happen.

## Checklist

- [ ] Every AI feature has a recorded per-request token budget, per-user quota, per-period budget, and a named owner (AI-181).
- [ ] The wrapper meters tokens in/out per call, and cost is computed from the dated price sheet in its single config location — no rates in feature code (AI-182, G-AI-093).
- [ ] The budget-guard test passes: past the cap, calls stop or degrade and zero provider calls leak through (AI-183, AI-189, G-AI-091).
- [ ] Retry counts, loop iterations, and per-task spend all have recorded hard bounds, and the runaway-loop test terminates at them (AI-184, G-AI-092).
- [ ] Every task class routes to a tier backed by an eval report at that tier; largest-tier assignments carry their justification (AI-185, G-AI-094).
- [ ] Caching is exact-match, keyed on prompt version and model, with hits marked in traces and reports; prompt assembly enforces the input-token budget with a stated truncation policy (AI-186, AI-187).
- [ ] The degradation drill passes: at the limit the user gets the documented fallback or a clear unavailability statement, recorded in the trace (AI-188, G-AI-095).
- [ ] The latest per-feature, per-model cost report exists, and every published cost figure names its period, scope, and price-sheet date (AI-190, AI-192).
