# ai-observability

## Metadata

- **Owner department:** D17 AI Features (AI)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://docs.langchain.com/langsmith/cost-tracking
- **Depends on:** llm-integration, prompt-engineering
- **Feeds into:** ai-evaluation, ai-cost-control

## When to use / Do NOT use

- **Use when:** An AI feature is being built, changed, or debugged and its model calls need traces — prompt version, model, tokens, latency, cost, retrieval sources, guardrail verdicts, and user quality signals — so any production answer can be explained and reproduced.
- **Do NOT use when:** The telemetry is about the product or infrastructure itself (page events, uptime, server metrics, error tracking) — that is D12 Analytics & Observability. This skill owns observability of the AI features only; it consumes D12's pipelines, it does not replace them.

## Rules

1. **AI-161 — One trace per AI call.** Every model interaction emits exactly one trace carrying: feature name, prompt version, model ID, tokens in/out, latency, computed cost, and final outcome (success, error, refusal, fallback). A call with no trace is treated as a call that never happened — and a defect.
2. **AI-162 — Versions come from the artifacts.** The prompt version recorded is the version of the versioned prompt artifact that ran (per prompt-engineering), and the model ID is the exact identifier returned by the provider via the llm-integration wrapper — never a hand-typed label, so a silent prompt or model change cannot hide behind a stale string.
3. **AI-163 — Trace the whole chain.** Retrieval, guardrail, and tool-call steps are child spans of the trace, recording retrieved chunk IDs, guardrail verdicts, and tool names with success/failure — enough that a bad answer can be reproduced from its trace alone.
4. **AI-164 — Hash inputs, redact content.** Inputs are stored as a hash plus a redacted form; raw prompt and output text is stored only where the product's privacy rules explicitly allow it, and never by default.
5. **AI-165 — Redact before logging.** Secrets and PII are detected and redacted before any trace or log write, not filtered later at read time; a secret that reaches the trace store is a security incident, not a logging bug.
6. **AI-166 — Retention is defined.** Trace and log retention periods are set per feature in writing before launch; traces are not kept forever "just in case," and deletion actually deletes.
7. **AI-167 — Failures are never sampled away.** Sampling may reduce successful-trace volume, but errors, refusals, guardrail blocks, and fallbacks are captured at 100% — the cases you most need are the ones sampling must not drop.
8. **AI-168 — Quality signals ride the trace.** Thumbs up/down, user edits of AI output, retries, regenerations, and escalations are recorded as events on the trace of the output they judge, so failures can be mined into the ai-evaluation golden dataset.
9. **AI-169 — One schema across providers.** All providers write the same tracing schema; provider-specific fields are normalized at the wrapper (per llm-integration), so dashboards and alerts never fork per provider.
10. **AI-170 — Dashboards read the trace store.** Every number on an AI dashboard (calls, tokens, cost, error rate, feedback rate) is aggregated from stored traces, broken down by feature, model, and prompt version — computed, never entered or estimated.
11. **AI-171 — Alerts have named thresholds.** Each feature defines alert thresholds before launch for error-rate spikes, latency regression, cost spikes, and quality-signal drops (feedback rate, eval-score drift on sampled traffic); an alert names the feature and the threshold crossed.
12. **AI-172 — Stay inside the boundary.** This skill instruments AI features; product analytics, infrastructure metrics, and uptime monitoring belong to D12. AI traces may link to D12 events by ID, but AI dashboards do not re-implement infrastructure monitoring.

## BAN list

- **BAN-AI-081 — Fixture dashboard.** Banned: An AI usage/cost dashboard whose figures are constants, fixtures, or hand-updated values instead of aggregations of real traces. Defeats: DET-FAKE-004. Bad: The admin panel shows "Tokens this month: 1,250,000" from a config value that never changes when calls are made. Instead: Compute every figure from the trace store so a known test call moves the number by exactly its token count. Severity: BLOCK.
- **BAN-AI-082 — Timer-driven "live" AI metrics.** Banned: A "live" calls-per-minute chart, model-status indicator, or activity feed animated by a timer or random drift with no trace stream behind it. Defeats: DET-FAKE-018. Bad: The status page pulses "42 requests/min" from a random walk while the provider is down. Instead: Drive every live indicator from the actual trace/event stream, and show "no data" when the stream stops. Severity: BLOCK.
- **BAN-AI-083 — In-memory counters.** Banned: Usage, token, or feedback counters held in process memory or client state that reset on restart or reload. Defeats: DET-FAKE-005. Bad: The cost counter resets to zero on every deploy, so monthly spend is unknowable. Instead: Persist every counter as trace records in the store and read totals from there on every load. Severity: BLOCK.
- **BAN-AI-084 — Health state that lies.** Banned: An AI feature status or sync indicator that reports "healthy" / "up to date" on a schedule without checking the last real call outcomes. Defeats: DET-FAKE-022. Bad: The dashboard shows a green "AI operational" badge because a cron sets it hourly, through a full provider outage. Instead: Derive status from recent trace outcomes (error rate over a stated window) and show the degraded state when traces say so. Severity: BLOCK.
- **BAN-AI-085 — Fabricated usage export.** Banned: A "Download usage report" export generated from a sample template instead of the traces in the selected period and filters. Defeats: DET-FAKE-019. Bad: The exported CSV lists the same round token figures regardless of the date range chosen. Instead: Generate exports from the trace store under the exact filters shown, so a call made seconds earlier appears in the file. Severity: WARN.

## Gates

- **G-AI-081 — Trace-completeness test.** Verifies: AI-161, AI-162, AI-163, AI-169. Check: Run the feature's automated test requests (at least one success, one retrieval, one guardrail block), then query the trace store and assert each call produced exactly one trace containing prompt version, model ID, tokens in/out, latency, cost, outcome, and child spans where applicable. Pass: 100% of test calls fully traced. Fail: Block shipment. Recorded in: progress.md.
- **G-AI-082 — Redaction test.** Verifies: AI-164, AI-165. Check: Send a test request containing a unique canary secret string and a fake PII value, then search all traces and logs for both strings (`grep -r "<canary>" <trace/log store export>` or the store's search equivalent). Pass: Neither string appears anywhere; only the redacted form and input hash are stored. Fail: Block shipment and treat any stored copy as an incident. Recorded in: progress.md.
- **G-AI-083 — Dashboard data-change test.** Verifies: AI-170. Check: Record the dashboard's token and call totals, fire one known test call with counted tokens, wait one stated refresh cycle, and reload. Pass: Both totals move by exactly that call's values. Fail: Block shipment (fixture dashboard). Recorded in: progress.md.
- **G-AI-084 — Feedback-linkage test.** Verifies: AI-168. Check: In a test environment, rate an AI output (thumbs down), edit an output, and retry once; then open each event and follow its reference. Pass: Every signal event resolves to the exact trace of the output it judged. Fail: Block shipment. Recorded in: progress.md.
- **G-AI-085 — Version-visibility test.** Verifies: AI-162. Check: Bump the prompt version (or switch the model) in staging, fire one request, and inspect the trace. Pass: The trace shows the new prompt version / model ID with no code change to the logging path. Fail: Block shipment — a change that leaves no trace is a silent change. Recorded in: progress.md.

## Anti-patterns

- **Logs nobody can query.** Traces written as free-text log lines with versions and tokens buried in prose; if answering "which prompt version produced this answer?" needs a regex expedition, the schema rule was skipped.
- **Sampling set once, forgotten.** A sample rate chosen at launch quietly drops the long tail of weird failures months later; re-check that failure capture is still 100% after any sampling change.
- **Vanity latency.** Reporting average latency while the p95 doubles; aggregates by feature and version exist precisely so regressions are visible — check the tail, not the mean.
- **Feedback collected, never mined.** Thumbs-down events pile up unreviewed while the golden dataset stays frozen at launch-day examples; unmined feedback is observability theater.

## Examples

- [Example 1 — The untraceable bad answer](examples/example-1.md) — violates/corrects AI-161, AI-163.
- [Example 2 — The secret in the trace](examples/example-2.md) — violates/corrects AI-165.
- [Example 3 — The dashboard that never moved](examples/example-3.md) — violates/corrects AI-170.

## Recall anchors

- No trace, no ship.
- Version in every record, or the change was silent.
- Redact before the write, not after the leak.
- Failures at 100%, successes may sample.
- A bad answer must be reproducible from its trace alone.

## Checklist

- [ ] Every AI call emits one trace with prompt version, model ID, tokens, latency, cost, and outcome (AI-161, AI-162).
- [ ] Retrieval, guardrail, and tool steps are child spans with IDs and verdicts (AI-163).
- [ ] Redaction test passed: canary secret and PII appear in no trace or log (G-AI-082).
- [ ] Retention period is written down for this feature's traces (AI-166).
- [ ] Errors, refusals, and fallbacks are captured at 100% regardless of sampling (AI-167).
- [ ] Feedback signals (thumbs, edits, retries) link to the trace they judge (AI-168).
- [ ] Dashboard figures are trace-store aggregations and moved by exactly one test call (G-AI-083).
- [ ] Alert thresholds for errors, latency, cost, and quality drift are named for this feature (AI-171).
