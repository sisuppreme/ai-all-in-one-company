# revenue-analytics

## Metadata

- **Owner department:** D12 Analytics & Observability (AN)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** PROJECT_ANATOMY.md, "Analytics" (revenue named as an analytics purpose; revenue-analytics listed as a serving skill); D11 research file, §1 (provider is the source of truth for money state; reconciliation repairs drift)
- **Depends on:** payments (D11 — the provider of record), product-analytics (shared metrics document and tracking plan), webhooks (D11)
- **Feeds into:** dashboards, unit-economics (D1), pricing-monetization (D1)

## When to use / Do NOT use

- **Use when:** defining, computing, or reporting any money figure for a project — revenue, MRR, refunds, LTV inputs — or setting up the reconciliation between the analytics pipeline and the payment provider.
- **Do NOT use when:** the question is moving money (charging, refunding, dunning — D11's payments, refunds-disputes, and dunning skills own execution; this skill only measures), product usage metrics with no money attached (product-analytics), or bookkeeping and tax filing (invoicing-tax, D11, and the operator's accountant own those).

## Rules

1. **AN-061 — The provider of record wins.** Every revenue figure is computed from the payment provider's records — charges, refunds, disputes, fees — never from analytics events. When the analytics pipeline and the provider disagree, the provider figure is reported and the pipeline is fixed; the disagreement is never averaged away.
2. **AN-062 — Every revenue metric has a written definition.** Before a metric is computed, its definition is written in the metrics document: gross or net, recognized or collected, the period a transaction is attributed to, and the treatment of trials, discounts, refunds, and failed payments. A figure without a definition is not reported.
3. **AN-063 — Charges minus refunds; fees on their own line.** Reported revenue for a period is successful charges minus refunds settled in the defined attribution model (AN-065). Provider fees are shown as a separate line, never silently folded into a number labeled "revenue" and never double-counted in both gross and net.
4. **AN-064 — Test-mode is excluded by construction.** Test-mode, sandbox, and internal transactions are filtered out in the source query that feeds reporting. Exclusion is a property of the pipeline, never a manual cleanup step performed on an export.
5. **AN-065 — Refunds belong to the original transaction.** For cohort, LTV, and per-period revenue reporting, a refund or dispute is attributed to the period of the original charge, so the original period's figure is restated. Cash reporting shows refunds as their own line in the period they settled. One report never mixes the two attributions without labeling which it uses.
6. **AN-066 — Currency is never silently converted.** Amounts are stored in the transaction currency. A figure reported in a different currency records the conversion rate and the rate date alongside it; a multi-currency total states the rates used. No single unstated rate is applied across periods.
7. **AN-067 — Reconciliation runs on a schedule and classifies every difference.** A scheduled job diffs analytics-reported revenue against the provider export for the period. Every difference is classified — refund timing, dispute, test-mode record, missed webhook, currency conversion — or carried as unexplained. An unclassified difference is a defect in the pipeline, not a rounding note.
8. **AN-068 — Dashboards state source and reconciliation freshness.** Every revenue dashboard or report names its source (the provider of record) and the time of its last successful reconciliation. A dashboard whose reconciliation is stale displays that fact on the dashboard itself.
9. **AN-069 — Failed payments and unpaid trials are not revenue.** A charge that failed, a subscription past due in dunning, and a trial that has not converted contribute zero to collected revenue. If a metric counts them (e.g. booked or contracted value), it is named and defined as such under AN-062 and never presented as revenue received.
10. **AN-070 — A period closes only at zero unexplained difference.** A reporting period is "closed" when the reconciliation's unexplained difference is zero, or every remaining cent is itemized with its classification. Reports for unclosed periods are labeled preliminary wherever they appear.
11. **AN-071 — Figures are computed, never typed.** Revenue numbers in dashboards and reports are produced by the reporting query over provider records at build or read time. A hand-typed or copy-pasted revenue figure is a defect even if the number happens to be right today.
12. **AN-072 — Definition changes are versioned.** Changing a revenue metric's definition bumps the metrics document version and notes which historical periods are restated under the new definition and which are not. Two periods computed under different definitions are never placed in one trend line without that note.

## BAN list

- **BAN-AN-031 — Hand-typed revenue figure.** Banned: a revenue or MRR number typed, pasted, or hardcoded into a dashboard, report, or page instead of computed from provider records. Defeats: DET-FAKE-004. Bad: the investor update carries "MRR: $12,400" typed from last month's spreadsheet; the panel shows $12,400 for three more months while real subscriptions churn. Instead: compute the figure from the provider's subscription and charge records under its AN-062 definition, and state the last reconciliation time per AN-068. Severity: BLOCK.
- **BAN-AN-032 — Analytics events reported as revenue truth.** Banned: treating the analytics event stream's revenue total as the revenue figure when it differs from the provider's records. Defeats: DET-CON-015. Bad: the growth dashboard reports $48,210 from `Order Completed` events while the provider settled $45,930; both numbers circulate and each team quotes its own. Instead: report the provider figure (AN-061) and open a reconciliation item for the gap — here, refunds and two missed webhooks. Severity: BLOCK.
- **BAN-AN-033 — Test-mode transactions in reported revenue.** Banned: letting test-mode, sandbox, or internal transactions reach a reported revenue figure, then removing them by hand when someone notices. Defeats: DET-CON-011. Bad: a launch-week report claims $3,150 in sales; $2,900 of it is the team's own test checkouts, deleted from the spreadsheet by hand before the next report. Instead: exclude test-mode records in the source query (AN-064) so no report can contain them. Severity: BLOCK.
- **BAN-AN-034 — Silent currency conversion.** Banned: converting amounts to a reporting currency with an unstated rate, or summing amounts in different currencies as if they were one. Defeats: DET-CON-015. Bad: EUR and USD charges are added raw into a single "total revenue" cell; the total changes meaning every time the mix shifts. Instead: store transaction currency, convert with a recorded rate and rate date, and state both on the report (AN-066). Severity: BLOCK.
- **BAN-AN-035 — Fees and refunds invisibly netted.** Banned: presenting one unlabeled number that has provider fees or refunds silently netted out — or not netted — so the reader cannot tell gross from net. Defeats: DET-CON-014. Bad: the pricing page's "average revenue per customer" quietly uses gross charges while the metrics document defines the metric as net of refunds; the two contradict. Instead: show charges, refunds, and fees as separate lines and label every total gross or net per its AN-062 definition. Severity: WARN.

## Gates

- **G-AN-031 — Reconciliation diff.** Verifies: AN-061, AN-067, AN-070. Check: automated — the scheduled reconciliation job compares analytics-reported revenue to the provider export for the period and emits the classified difference list. Pass: unexplained difference is zero, or every remaining amount is itemized with a classification. Fail: the period stays open and its reports are labeled preliminary. Recorded in: progress.md.
- **G-AN-032 — Test-mode leak test.** Verifies: AN-064. Check: automated — query the reporting tables for any transaction flagged test-mode, sandbox, or internal for the current period (`SELECT COUNT(*) FROM revenue_facts WHERE mode != 'live'`). Pass: the count is zero. Fail: block the report; fix the source filter, not the output. Recorded in: progress.md.
- **G-AN-033 — Recompute check.** Verifies: AN-063, AN-071. Check: automated — independently recompute the period's headline figure from raw provider records (successful charges minus refunds, fees listed separately) and diff it against the figure the dashboard/report displays. Pass: the figures match to the cent and fees appear as their own line. Fail: block publication of the report until the pipeline discrepancy is resolved. Recorded in: progress.md.
- **G-AN-034 — Definition lint.** Verifies: AN-062, AN-072. Check: automated — list every revenue metric rendered on live dashboards and reports; for each, confirm a current definition exists in the metrics document (gross/net, recognition, attribution, trial/refund treatment) and that the rendered label matches it. Pass: 100% of displayed revenue metrics trace to a definition. Fail: remove or define the untraceable metric before the next report ships. Recorded in: progress.md.
- **G-AN-035 — Currency audit.** Verifies: AN-066. Check: automated — sample transactions per currency in the period and assert each stored record carries its transaction currency and, where converted, the rate and rate date used. Pass: every sampled record is complete; no mixed-currency sum exists without stated rates. Fail: block the multi-currency report until rates are recorded. Recorded in: progress.md.

## Anti-patterns

- **The spreadsheet cleanup ritual.** Each month someone exports, eyeballs, and hand-deletes the test rows and odd entries before sharing the numbers. Catch it: if producing the report requires a human editing data, AN-064 and AN-071 have already failed — fix the query, not the export.
- **MRR by vibes.** Trials, past-due accounts, and one-off charges are counted into MRR because the total "felt low". Catch it: read the metric's AN-062 definition aloud; any component not named in it does not belong in the number.
- **The stale green checkmark.** The dashboard still shows "Reconciled ✓" from a reconciliation that last ran six weeks ago, before a webhook outage. Catch it: AN-068 requires the timestamp on the dashboard; a badge without a fresh date is decoration.
- **Refund amnesia.** Refunds are booked in the month they settle and never restated against the original cohort, so early cohorts look permanently better than they were. Catch it: compare cohort revenue before and after the refund window closes; if it never moves, AN-065 is not implemented.

## Examples

- [Example 1 — The MRR number typed into the deck](examples/example-1.md) — violates/corrects AN-071.
- [Example 2 — Two revenue totals, one provider truth](examples/example-2.md) — violates/corrects AN-061.
- [Example 3 — The multi-currency total that meant nothing](examples/example-3.md) — violates/corrects AN-066.

## Recall anchors

- The provider of record wins every dispute — report its figure, fix the pipeline.
- Charges minus refunds; fees on their own line; gross and net always labeled.
- Test-mode is excluded in the query, never cleaned by hand.
- Currency converts only with a recorded rate and date.
- No period closes with an unexplained difference.

## Checklist

- [ ] Every reported revenue metric has a written definition in the metrics document (AN-062, G-AN-034).
- [ ] Headline figure recomputed from provider records matches the displayed figure to the cent (G-AN-033).
- [ ] Reconciliation ran for the period; unexplained difference is zero or fully itemized (G-AN-031).
- [ ] Reporting tables contain zero test-mode, sandbox, or internal transactions (G-AN-032).
- [ ] Refunds and disputes are attributed to the original transaction's period, with cash view shown separately (AN-065).
- [ ] Every converted amount records its rate and rate date; no silent conversions (AN-066, G-AN-035).
- [ ] Dashboards name the provider source and show the last successful reconciliation time (AN-068).
- [ ] Failed payments and unconverted trials contribute zero to collected revenue (AN-069).
