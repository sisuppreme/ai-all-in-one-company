# D12 Analytics & Observability — End-to-End Example

## Scenario

"NoteNest," a small note-taking SaaS, instruments its signup funnel and builds an
operations dashboard before launch. The team needs to answer two questions honestly:
where do signups drop off, and is the service healthy right now? The first AI-built
version produces numbers for both — and neither number can be trusted.

## Before — the slop version

Events emitted from scattered raw calls across the codebase (no tracking plan):

```js
track('signed_up', { email: user.email });
track('Signup Completed', { user_email: user.email, plan: 'pro' });
track('checkoutBtnClicked');
track('Support Requested', { message: form.message });   // user's typed text, email included
```

Dashboard definition, edited by hand in the web console, never committed:

```
Panel: "Revenue today"      → text card: "$4,820"        (typed in at launch)
Panel: "Live visitors"      → widget labeled LIVE, value incremented by a
                              client-side random timer; pipeline batches hourly
Panel: "Latency"            → headline: "avg latency 120 ms" (no percentiles)
```

What is wrong, visibly: one funnel event exists under two names, so the funnel
silently halves; event properties carry an email address and a user's free-text
message into the analytics store; the revenue figure is a constant typed once and
shown every day; a "live" panel is animated by a timer while the data is an hourly
batch; and the latency headline is a mean that hides the tail.

## What the skills caught

- **BAN-AN-011 — Event-name variants** (defeats DET-CON-017). `signed_up` and
  "Signup Completed" are one event with two live spellings. **AN-022** fixes one
  naming convention, enforced mechanically; **AN-028** routes every emission through
  one typed wrapper.
- **BAN-AN-012 — Personal data in event properties** (defeats DET-CON-003). Emails
  and typed message text do not belong in the event stream. **AN-026**: people are
  referenced by opaque IDs only; content stays in the system of record.
- **BAN-AN-071 — Frozen figures** (defeats DET-FAKE-004). The "Revenue today" panel
  renders a hand-typed constant. **AN-144**: every figure is computed from live
  records at read time; **AN-143**: the query and metric definition are visible on
  the panel.
- **BAN-AN-073 — Fake "live" panels** (defeats DET-FAKE-018). A timer-animated
  widget over hourly data is not live. **AN-145**: the panel states its true
  aggregation interval and lag; "live" appears only where the data is current.
- **BAN-AN-074 — Averages as the latency story** (defeats DET-INF-011). A 120 ms
  mean stays green while p99 sits at seconds. **AN-147**: latency panels show
  p50/p95/p99 bands, success and error charted separately.
- **BAN-AN-072 — Console-only dashboards** (defeats DET-INF-024). The dashboard
  exists only in the console; a redeploy would silently restore an older version.
  **AN-141**: dashboards are code — defined in the repo, reviewed, deployed from it.
- **AN-021** underlies all of it: no event is emitted that is not first recorded in
  the versioned tracking plan, with properties, types, owner, and the question it
  answers.

## After — the corrected version

`tracking-plan.md` (versioned in the repo; the wrapper is generated from it):

```markdown
# Tracking Plan v3 — NoteNest

| Event              | Properties (typed)                          | Owner    | Question it answers            |
|--------------------|---------------------------------------------|----------|--------------------------------|
| Signup Completed   | plan: enum(free, pro), source: string       | growth   | Where do signups come from?    |
| Subscription Started | plan: enum(pro), interval: enum(month, year) | billing | How many trials convert?       |
| Support Requested  | category: enum(billing, bug, how-to, other) | support  | What do users ask for help with? |

Rules: names are Object-Action, past tense (AN-022); no dynamic values in names
(AN-023); no personal data in properties — users are opaque IDs (AN-026);
events fire only after consent state is known (AN-030).
```

Dashboard definition, committed as provisioning JSON and deployed from the repo:

```
Panel: "Revenue today"      → query over live payment records; definition named
                              on the panel (AN-143, AN-144)
Panel: "Active sessions"    → labeled "aggregated hourly, ~15 min lag" (AN-145)
Panel: "API latency"        → p50 / p95 / p99 bands, success vs. error split,
                              SLO line shown (AN-147, AN-148)
Panel: any empty query      → renders "no data for this window" and files a
                              data-source defect — never a silent blank (AN-151)
```

Before release, the primary flows are run in a test session and every expected
event is confirmed in the platform's debug view — correct name, properties, types,
fired once (AN-029). A production sweep on a fixed cadence files any unplanned
event as a defect (AN-032).

## Skills used

- [event-tracking](../skills/analytics-observability/event-tracking/SKILL.md)
- [dashboards](../skills/analytics-observability/dashboards/SKILL.md)
- [product-analytics](../skills/analytics-observability/product-analytics/SKILL.md)
- [monitoring](../skills/analytics-observability/monitoring/SKILL.md)
