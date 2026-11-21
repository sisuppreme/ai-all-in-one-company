# apm

## Metadata

- **Owner department:** D12 Analytics & Observability (AN)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** OpenTelemetry, "Observability primer" — https://opentelemetry.io/docs/concepts/observability-primer/ ; Google, *Site Reliability Engineering*, "Monitoring Distributed Systems" — https://sre.google/sre-book/monitoring-distributed-systems/
- **Depends on:** logging, monitoring
- **Feeds into:** performance-optimization, dashboards, error-tracking

## When to use / Do NOT use

- **Use when:** instrumenting a service for application performance monitoring: choosing and configuring tracing, setting the sampling strategy, propagating trace context across services, queues, and jobs, building per-service performance views (throughput, error rate, duration percentiles, top endpoints, downstream dependencies), or diagnosing a slow endpoint or database call from traces.
- **Do NOT use when:** the question is browser-side, real-user performance — LCP, INP, and CLS field metrics, per-template vitals, and lab reproduction. **core-web-vitals owns the browser-side field metrics; this skill owns server-side application tracing** — spans, slow endpoints, and database time — and the two meet only where a trace explains what the server contributed to a page load. Host and platform telemetry belong to D6; SLI/SLO definitions and metric-label policy belong to monitoring; this skill consumes both.

## Rules

1. **AN-181 — One instrumentation standard: OpenTelemetry.** Every service is instrumented with OpenTelemetry libraries and OTel semantic conventions for span names and attributes, exported through a collector to the project's backend. A service instrumented with a proprietary one-off agent is recorded as a correlation break and a migration debt, not as an acceptable variation.
2. **AN-182 — One trace ID from edge to database.** Trace context propagates across every boundary a request crosses — inbound HTTP, outbound HTTP, message queues, and background jobs, whose payloads carry the trace context explicitly. The same trace ID appears on every span and on the request's log lines (logging owns the log format; this skill owns the shared ID), so one production request can be reconstructed end to end and pivoted from span to logs without SSH or new code.
3. **AN-183 — Sampling is a written decision.** The repo records the sampling strategy with its reason: the head-based baseline rate, what is always kept (errors and slow outliers, via tail sampling at the collector where volume justifies it), and what the blind spot costs. "Whatever the default was" is not a strategy; a sampler that can discard the only trace of an incident has failed its purpose.
4. **AN-184 — Rich detail lives on spans, never in metric labels.** Span attributes carry the high-cardinality detail traces exist for — endpoint, query shape, downstream target, result status. User IDs, request IDs, and full URLs never leak from spans into metric labels; monitoring's cardinality budget applies unchanged (AN-107).
5. **AN-185 — No secrets or personal data in span attributes.** Span attributes and span events never carry passwords, tokens, authorization headers, card numbers, emails, or free-text user input. Attribute keys come from the semantic conventions or a reviewed project list; a trace backend is a data store, and whatever lands in a span is retained like one.
6. **AN-186 — Instrumentation coverage is inventoried.** Every service and every async path is listed in the repo as instrumented or explicitly not instrumented, with the gap's owner named. "No trace" during an incident must be a known, recorded gap — never a surprise discovered mid-investigation.
7. **AN-187 — Per-service views are built from the traces.** Each instrumented service has a standard view built from its telemetry: throughput, error rate, duration percentiles (p50/p95/p99, never averages), top endpoints by traffic and by duration, and its downstream dependencies with their share of its latency. A slow endpoint is identified from this view, not from anecdote.
8. **AN-188 — A latency claim without a trace is an opinion.** No statement about where time goes — in a review, a postmortem, or an optimization proposal — stands unless it names the trace evidence behind it: the service, endpoint, and span breakdown (self time versus downstream time, database time shown separately). Claims are restated from percentile data over a stated window, not from a single hand-picked trace.
9. **AN-189 — Exemplars link spikes to traces.** Latency metrics carry exemplars where the backend supports them, so a p99 spike on a chart opens the actual slow traces behind it. Where exemplars are unsupported, the view links the chart's time window and filters into the trace search — a spike nobody can descend into is decoration.
10. **AN-190 — Database time is its own span.** Database calls appear as child spans with the operation and target recorded (never the literal parameter values), so an endpoint's duration decomposes into application time, database time, and downstream-call time. An endpoint whose duration is one opaque span is uninstrumented where it matters most.
11. **AN-191 — Critical paths get manual spans where automation goes blind.** Where automatic instrumentation misses the work that matters — a queue consumer's processing body, a batch loop, a cache layer — explicit manual spans are added with semantic-convention names. The test is behavioral: the primary flow's trace shows every hop it actually took.
12. **AN-192 — Trace retention is stated, like sampling.** The repo records how long traces are retained and what the sampling-plus-retention combination makes unanswerable (for example, last month's rare error on a low-traffic endpoint). Performance comparisons across releases use windows inside retention; a comparison the telemetry cannot support is reported as unmeasurable, not estimated.

## BAN list

- **BAN-AN-091 — One-off proprietary instrumentation.** Banned: instrumenting a service with a vendor-specific agent or hand-rolled timing calls while the rest of the system uses OpenTelemetry, so its spans join no shared trace. Defeats: DET-INF-011. Bad: the payments service ships a proprietary agent; during a checkout incident every other service's trace stops at its door, and its own data sits in a separate console nobody can correlate. Instead: instrument with OpenTelemetry and semantic conventions, exported through the same collector as every other service (AN-181). Severity: BLOCK.
- **BAN-AN-092 — Trace context dropped at the queue.** Banned: enqueueing a job or message without the trace context, so the consumer starts an unrelated trace and the request's story ends at the exact boundary where the incident lives. Defeats: DET-INF-013. Bad: the order request traces cleanly to `enqueue confirmation-email`, but the job that times out and double-charges runs under a fresh ID; the two halves are never connected. Instead: carry the trace context in the job payload and continue the originating trace in the consumer (AN-182). Severity: BLOCK.
- **BAN-AN-093 — The default sampler as the strategy.** Banned: shipping whatever sampling the library defaulted to, with no written decision, so errors and slow outliers are sampled away at the same rate as routine traffic. Defeats: DET-INF-011. Bad: a 1-in-1,000 default keeps almost nothing; the one checkout failure mode that matters occurs eleven times in a week and leaves zero traces. Instead: record a baseline rate and always keep errors and slow requests, with tail sampling at the collector where volume justifies it (AN-183). Severity: BLOCK.
- **BAN-AN-094 — Identifiers as metric labels via APM.** Banned: promoting span attributes such as user ID, request ID, or full URL into metric labels because the APM view made it one click. Defeats: DET-INF-027. Bad: a `user_id` label on the duration metric explodes series count, the metrics store saturates and drops data, and every golden-signal dashboard gaps during the incident the labels were meant to explain. Instead: keep identifiers on spans and log fields, where high cardinality is their purpose (AN-184). Severity: WARN.
- **BAN-AN-095 — Secrets and personal data in span attributes.** Banned: attaching credentials, tokens, emails, or raw user input as span attributes or span events. Defeats: DET-INF-021. Bad: a debugging pass adds the full request body to every span; the trace backend now retains customer emails and a password-reset token, searchable by anyone with dashboard access. Instead: record operation, target, and status attributes from the reviewed list only (AN-185). Severity: BLOCK.

## Gates

- **G-AN-091 — Trace-completeness test.** Verifies: AN-182, AN-186, AN-191. Check: automated — drive a synthetic request through the primary flow in staging (sign-in, the core action, checkout where one exists) and fetch its trace from the backend API; assert a span exists for every service and every async hop the flow touches, all under one trace ID. Pass: zero missing spans. Fail: block; the flow is unobservable where it matters. Recorded in: progress.md.
- **G-AN-092 — Queue propagation test.** Verifies: AN-182. Check: automated — in staging, perform the action that enqueues the primary background job, then query the backend for the job consumer's spans; assert they carry the originating request's trace ID, not a fresh one. Pass: the consumer's spans join the originating trace. Fail: block the change that touched the enqueue or consume path. Recorded in: progress.md.
- **G-AN-093 — Coverage inventory check.** Verifies: AN-186. Check: automated — diff the instrumentation inventory in the repo against the service registry, including async paths. Pass: every service and async path is listed as instrumented or explicitly not, with an owner on each gap. Fail: an unlisted service is a release defect. Recorded in: progress.md.
- **G-AN-094 — Always-kept sampling test.** Verifies: AN-183. Check: automated — with the production sampling configuration applied in staging, drive a forced error response and a deliberately slow request on the primary flow, then query the backend for both traces. Pass: both traces are present despite the baseline rate. Fail: block; the sampler can discard the next incident. Recorded in: progress.md.
- **G-AN-095 — Span-to-log pivot test.** Verifies: AN-182, AN-187. Check: automated — take the trace from G-AN-091, extract its trace ID, and query the central log store for that ID; assert entries exist from every service the trace touched, and that the service's standard view renders throughput, error rate, and duration percentiles from the same window. Pass: the pivot resolves for every service and the view renders. Fail: the correlation chain is declared broken until fixed. Recorded in: progress.md.

## Anti-patterns

- **The three-console observability story.** Metrics in one tool, logs in another, a tracing trial in a third, with no shared ID between them — sold internally as "we have observability". Catch it: run the behavioral test — reconstruct one request end to end; if you open a second console and start guessing, it fails (AN-182).
- **The single opaque span.** The endpoint's trace is one long bar with no children: no database span, no downstream calls, so "the endpoint is slow" is all anyone can ever say. Catch it: if the trace cannot decompose duration into app, database, and downstream time, instrumentation is unfinished (AN-190).
- **Cherry-picked trace as proof.** One slow trace pasted into a review thread presented as the endpoint's latency profile. Catch it: ask for the percentile over a stated window with the trace as illustration, never as the dataset (AN-188).
- **Instrumenting only the happy path.** Spans wrap successful operations while error branches, retries, and fallback paths emit nothing — so traces are plentiful exactly when nothing is wrong. Catch it: force the error path in staging and read its trace before signing off coverage (G-AN-094).

## Examples

- [Example 1 — The trace that ended at the queue](examples/example-1.md) — violates/corrects AN-182.
- [Example 2 — The default sampler that threw away the incident](examples/example-2.md) — violates/corrects AN-183.
- [Example 3 — The 200 ms claim with no trace behind it](examples/example-3.md) — violates/corrects AN-188.

## Recall anchors

- One trace ID, edge to database — or the story ends where the incident lives.
- Sampling is a written decision; errors and slow requests are always kept.
- Detail belongs on spans; labels stay low-cardinality.
- A latency claim without a trace behind it is an opinion.
- Browser vitals belong to core-web-vitals; spans and database time belong here.

## Checklist

- [ ] Every service is instrumented with OpenTelemetry and semantic conventions (AN-181).
- [ ] Trace-completeness test passes: every service and async hop on the primary flow under one trace ID (G-AN-091).
- [ ] Queue propagation test passes: consumer spans join the originating trace (G-AN-092).
- [ ] Sampling strategy is written in the repo, and the always-kept test passes for an error and a slow request (AN-183, G-AN-094).
- [ ] Coverage inventory matches the service registry, gaps owned (G-AN-093).
- [ ] No secrets or personal data in span attributes; no identifiers promoted to metric labels (AN-184, AN-185).
- [ ] Span-to-log pivot resolves for every service on the primary flow (G-AN-095).
- [ ] Retention window is recorded, and no performance claim cites data outside it (AN-192).
