# product-metrics

## Metadata

- **Owner department:** D1 Product & Requirements (PR)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://info.amplitude.com/rs/138-CDN-550/images/ai-product-metrics-worksheet-bundle.pdf
- **Depends on:** discovery, fact-sheet
- **Feeds into:** roadmapping, unit-economics, scope-control

## When to use / Do NOT use

- **Use when:** choosing the metrics a product or release will be judged by; writing or changing a metric definition; setting up a dashboard; preparing any number for publication in copy, decks, or the fact sheet.
- **Do NOT use when:** the numbers are financial per-customer economics (use unit-economics), or the task is instrumenting events in code (this skill defines what must exist; implementation follows the definition).

## Rules

1. **PR-181 — One North Star, value first.** The product has exactly one North Star metric, and it captures the value customers get, stated in plain words. The North Star leads revenue; it is never revenue itself.
2. **PR-182 — Three to five input metrics.** The North Star is decomposed into 3–5 input metrics spanning breadth, depth, frequency, and efficiency — levers a team can move weekly, not outcomes it can only watch.
3. **PR-183 — Exact written definitions.** Every metric has a definition in the metric dictionary stating the event, the time window, the segment, and the exclusions. A metric that cannot be defined this precisely is not yet a metric.
4. **PR-184 — Owner and source for every metric.** Each dictionary entry names an owning team and the data source (system and query or report) the number comes from.
5. **PR-185 — Definitions are versioned.** A definition change is a changelog entry with date, old definition, new definition, and reason. Numbers computed under different definitions are never trended together without a visible break marker.
6. **PR-186 — Nothing publishes without a definition and a source.** No number appears in copy, decks, investor material, or the fact sheet unless it resolves to a dictionary definition and a queryable source.
7. **PR-187 — Guardrails are named.** The framework names the guardrail metrics that must not degrade while the North Star grows (for example: error rate, support tickets per active account, churn).
8. **PR-188 — Vanity metrics are not success.** Registrations, raw pageviews, and total accounts may be reported as context but never serve as the success measure for a product, release, or experiment. The North Star must rise only when customers succeed.
9. **PR-189 — Inputs are re-validated against outcomes.** At each metric review, input metrics are checked against the North Star: an input that no longer predicts it is replaced, and the replacement is recorded in the changelog.
10. **PR-190 — Every input has a team that can move it.** An input metric no named team can influence is decoration; it is removed from the framework or reassigned until an owner with real leverage exists.

## BAN list

- **BAN-PR-091 — Publishing an undefined number.** Banned: putting a metric in copy, a deck, or the fact sheet that has no dictionary definition or no queryable source behind it. Defeats: DET-CON-011. Bad: the homepage announces "teams ship 40% faster with us" — no event, window, or dataset exists that computes "ship faster." Instead: define the metric, compute it from its source, then publish the figure with its definition available (PR-183, PR-186). Severity: BLOCK.
- **BAN-PR-092 — Silent redefinition.** Banned: changing what a metric counts (window, exclusions, event) without a changelog entry, so the trend line silently mixes two different measures. Defeats: DET-CON-015. Bad: "active users" quietly changes from 28-day to 7-day in March; the April report shows a "decline" that is purely the definition, and the about page and the dashboard now state different growth stories. Instead: version the definition under PR-185 and mark the break. Severity: BLOCK.
- **BAN-PR-093 — Dashboard metric with no dictionary entry.** Banned: a chart or KPI tile on any dashboard whose metric does not exist in the dictionary with definition, owner, and source. Defeats: DET-CON-014. Bad: the exec dashboard shows "Engagement score: 72" — a number no document defines and the fact sheet cannot reproduce. Instead: add the dictionary entry first, or remove the tile (PR-184). Severity: BLOCK.
- **BAN-PR-094 — Vanity count as success proof.** Banned: presenting a vanity count (total signups, total downloads, raw pageviews) as evidence that customers succeed or that the product is growing in value. Defeats: DET-CON-011. Bad: the release announcement leads with "10,000 accounts created!" while activation sits at 6% and most accounts never complete setup. Instead: report the North Star and its inputs; vanity counts appear only as labeled context (PR-188). Severity: WARN.

## Gates

- **G-PR-091 — Dictionary completeness scan.** Verifies: PR-183, PR-184, PR-186. Check (automated): list every metric name displayed on any dashboard or report; for each, `grep -i "<metric name>" metric-dictionary.md` must find an entry containing definition, owner, and source fields. Pass: zero displayed metrics missing a complete entry. Fail: block shipment. Recorded in: progress.md.
- **G-PR-092 — Instrumentation name check.** Verifies: PR-183. Check (automated): for each dictionary definition, extract the named event and run `grep -rn "<event_name>" analytics/ src/` (or query the analytics tool's event list) to confirm the event exists under exactly that name. Pass: every definition's event found under the same name. Fail: block shipment — a definition naming a non-existent event measures nothing. Recorded in: progress.md.
- **G-PR-093 — Definition changelog audit.** Verifies: PR-185. Check (automated): `grep -c "definition changed" metric-dictionary.md` is compared against the count of definition edits in the file's version history for the period; any edit without a matching changelog entry is flagged. Pass: zero unlogged definition edits. Fail: warn; the changelog is completed before the next report ships. Recorded in: progress.md.
- **G-PR-094 — North Star sanity review.** Verifies: PR-181, PR-188. Check (manual): read the North Star statement and answer two questions in writing — does it rise only when customers succeed, and does it lead rather than equal revenue? Pass: both answers are yes with a one-line justification each. Fail: block shipment of the framework until the North Star is rewritten. Recorded in: progress.md.

## Anti-patterns

- **Dashboard sprawl.** Every stakeholder's favorite number gets a tile until the dashboard answers nothing. Catch it by asking which decision each tile changed in the last quarter; tiles with no decision are removed.
- **Metric of the month.** The team optimizes whichever input is red this month, whipsawing effort while the North Star stays flat. Catch it in the review cadence: inputs are re-validated on schedule (PR-189), not swapped on anxiety.
- **Precision theater.** Metrics reported to three decimal places from a pipeline nobody has audited. Catch it by tracing one published number back through its source query by hand; if the trace fails, the precision was theater.
- **Lagging-only framework.** Every metric in the set is a monthly outcome (revenue, churn) with no weekly lever, so reviews become obituaries. Catch it against PR-182: at least one input must be movable weekly.

## Examples

- [Example 1 — Signups as the North Star](examples/example-1.md) — violates/corrects PR-181, PR-188.
- [Example 2 — The 40% faster claim](examples/example-2.md) — violates/corrects PR-186.
- [Example 3 — The definition that changed quietly](examples/example-3.md) — violates/corrects PR-185.

## Recall anchors

- One North Star: customer value, leading revenue, never revenue itself.
- No definition, no dashboard; no source, no publication.
- Definition changes are changelog entries, never edits in the night.
- Vanity counts are context, not success.
- An input nobody can move is decoration.

## Checklist

- [ ] Exactly one North Star, stated as customer value (PR-181, G-PR-094).
- [ ] 3–5 input metrics across breadth, depth, frequency, efficiency (PR-182).
- [ ] Every metric defined exactly: event, window, segment, exclusions (PR-183).
- [ ] Every dictionary entry names owner and data source (PR-184, G-PR-091).
- [ ] Instrumentation events exist under the dictionary's names (G-PR-092).
- [ ] All definition changes since last review are in the changelog (PR-185, G-PR-093).
- [ ] Guardrail metrics named (PR-187).
- [ ] No number queued for publication lacks a definition and a source (PR-186).
