# performance-budgets

## Metadata

- **Owner department:** D12 Analytics & Observability (AN)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://web.dev/articles/vitals ; https://www.performanceisolation.com/monitoring-measuring-third-party-performance/enforcing-performance-budgets-with-lighthouse-ci/ ; PROJECT_ANATOMY.md, "Performance budgets"
- **Depends on:** core-web-vitals, monitoring
- **Feeds into:** performance-optimization, dashboards

## When to use / Do NOT use

- **Use when:** Setting or changing the numeric performance limits for a web project; wiring Lighthouse CI into the merge pipeline; reviewing a budget breach, a waiver request, or a third-party script addition.
- **Do NOT use when:** Diagnosing why a specific template is slow (use core-web-vitals), or making the optimization change itself (use performance-optimization; the fix is executed by the owning department's skill).

## Rules

1. **AN-201 — Budgets live in a committed budget file, per page template.** The file is committed to the repo before the work it judges begins, and it names limits per template (home, product, checkout), never as one site-wide average that hides a bad template.
2. **AN-202 — Every budget is numeric and covers the minimum set.** Each template's entry names numeric limits for LCP, INP, CLS, JavaScript size, total page weight, image weight, and request count; a limit stated as "fast" or "lightweight" does not count as set.
3. **AN-203 — Web-vital limits anchor to the Core Web Vitals "good" thresholds.** LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1, assessed at the 75th percentile; a project may set tighter limits, never looser ones without a recorded decision (AN-210).
4. **AN-204 — CI enforces the budget on every merge.** Lighthouse CI (`lhci autorun`) runs as a required status check: its `assert` block guards audit values (LCP, total blocking time, CLS) and `budget.json` caps timings, resource sizes, and resource counts; a breach exits non-zero and blocks the merge.
5. **AN-205 — Lab verdicts use the median of multiple runs on a pinned setup.** Collect at least three runs per template and assert the median; the device profile, network throttling, and tool versions are pinned in the CI configuration, because a single throttled run is noise.
6. **AN-206 — Critical API endpoints carry a p95 latency budget.** Each critical endpoint names a numeric p95 limit in the budget file; averages are never used, because they hide the tail users feel.
7. **AN-207 — Third-party scripts are a named budget line.** The `third-party` resource type in `budget.json` has its own size and count limits; adding a tag is a budget change under AN-210, not a marketing afterthought.
8. **AN-208 — A breach has exactly two exits.** Fix the regression, or take a written waiver under AN-209. Merging with a known breach and neither is prohibited.
9. **AN-209 — Waivers carry an owner, a reason, and an expiry date.** The waiver is recorded in the repo next to the budget file; when the expiry date passes, the gate fails again until the breach is fixed or the waiver is renewed as a budget decision.
10. **AN-210 — Raising a budget is a recorded decision, never a quiet edit.** A limit increase ships as its own change with the reason recorded in the project's DECISIONS.md, and is never bundled into the change that breached the limit.
11. **AN-211 — Budgets ratchet.** When a template sits comfortably inside its size budget, the budget is tightened to current reality plus stated headroom at the next budget review, so a past win cannot silently become future bloat.
12. **AN-212 — Field data is checked against the same numbers.** A scheduled check compares the rolling 28-day field p75 per template (mobile and desktop separately) against the budget and opens a defect on breach; CI green does not imply field green.

## BAN list

- **BAN-AN-101 — The prose budget.** Banned: a budget stated in words ("pages should feel fast", "keep it lightweight") with no numeric limits in a committed file. Defeats: DET-INF-027. Bad: the performance section of the plan says "fast load times" and the checkout template ships 900 KB of JavaScript unchallenged. Instead: commit a budget file with numeric LCP/INP/CLS and size limits per template (AN-201, AN-202). Severity: BLOCK.
- **BAN-AN-102 — The advisory check.** Banned: running Lighthouse CI with `continue-on-error`, as a non-required check, or with assertions set to warn-only, so merges proceed on a breach. Defeats: DET-INF-002. Bad: the workflow step `lhci autorun` is followed by `if: always()` publishing and a green merge on a failed assertion. Instead: make `lhci autorun` a required status check whose non-zero exit blocks the merge (AN-204). Severity: BLOCK.
- **BAN-AN-103 — The same-PR raise.** Banned: increasing a budget limit inside the same change that breached it, so the gate passes by moving the goalposts. Defeats: DET-INF-002. Bad: a feature PR adds 180 KB of JavaScript and edits `budget.json` from 300 KB to 500 KB in the same commit, with no other record. Instead: fix the regression, or land the raise as its own change with the reason in DECISIONS.md (AN-210). Severity: BLOCK.
- **BAN-AN-104 — The single-run gate.** Banned: asserting a budget on one lab run, so normal throttling variance randomly fails or passes the build. Defeats: DET-INF-002. Bad: CI runs Lighthouse once; the team re-runs the job until it passes and learns to ignore the gate. Instead: collect at least three runs on the pinned setup and assert the median (AN-205). Severity: BLOCK.
- **BAN-AN-105 — The permanent waiver.** Banned: a budget waiver with no owner or no expiry date, which is a silent budget increase. Defeats: DET-INF-002. Bad: `waivers.md` says "checkout LCP waived — known issue" with no name and no date, still in force a year later. Instead: record owner, reason, and expiry; an expired waiver fails the build again (AN-209). Severity: BLOCK.

## Gates

- **G-AN-101 — CI budget assertion.** Verifies: AN-202, AN-204, AN-205. Check: `lhci autorun` runs in the merge pipeline with the `assert` block and `budget.json` from the repo, collecting at least three runs per template and asserting the median. Local/offline path: where Lighthouse CI cannot run, assert the same `budget.json` values from a local Lighthouse run (median of at least three runs per template) or an equivalent local measurement of the same metrics, and record the tool substitution in progress.md. Pass: exit code 0 on every template. Fail: block the merge; the breach exits only via fix or waiver (AN-208). Recorded in: progress.md.
- **G-AN-102 — Budget-file lint.** Verifies: AN-201, AN-202, AN-203, AN-206, AN-207. Check: a CI script parses the budget file and asserts every template entry names numeric LCP, INP, and CLS limits no looser than 2.5 s / 200 ms / 0.1, numeric JavaScript, total-weight, image-weight, and request-count limits, a `third-party` line, and a p95 limit for each critical endpoint. Pass: zero missing or non-numeric entries. Fail: block the merge. Recorded in: progress.md.
- **G-AN-103 — Waiver scan.** Verifies: AN-209, AN-210. Check: a CI script scans the waiver record and fails if any waiver lacks an owner or expiry date, if any expiry date has passed, or if any budget-file limit changed in a commit that also changed application code. Pass: zero violations. Fail: block the merge. Recorded in: progress.md.
- **G-AN-104 — Field budget check.** Verifies: AN-212. Check: a scheduled job pulls the rolling 28-day field p75 for LCP, INP, and CLS per template, mobile and desktop separately, and compares each value against the budget file. Pass: every template inside budget. Fail: open a defect naming the template, metric, and observed p75; the defect closes only on a later in-budget field window or a recorded budget decision. Recorded in: progress.md.
- **G-AN-105 — Budget-change review.** Verifies: AN-210, AN-211. Check: manual review of any budget-file diff — the change is standalone, the DECISIONS.md entry states the reason and the new headroom, and at each budget review any template comfortably inside its size budget has been ratcheted or the review notes why not. Pass: reviewer confirms all three. Fail: block shipment of the budget change. Recorded in: progress.md.

## Anti-patterns

- **The homepage-only audit.** Lighthouse runs on the homepage alone because it is easy, while the slow checkout template is never measured; catch it by listing templates in the budget file and checking the CI matrix covers every one.
- **Lab-confidence theater.** The team trusts a passing desktop lab run on the office connection while field p75 fails on real phones; catch it by reading the G-AN-104 field report before calling any template "fast".
- **Set-and-forget budgets.** The budget file is written at launch and never reviewed while templates, tags, and content change around it; catch it at the scheduled budget review — a budget file untouched across two reviews is a finding, not a comfort.
- **Gaming the metric.** Hitting a number by removing content users need, deferring the main content itself, or excluding the heavy page from the run; catch it by checking that what changed is weight and timing, not the page's substance or the template list.

## Examples

- [Example 1 — Prose budget to numeric budget file](examples/example-1.md) — violates/corrects AN-201, AN-202.
- [Example 2 — Advisory Lighthouse step to required gate](examples/example-2.md) — violates/corrects AN-204.
- [Example 3 — Quiet same-PR raise to waiver and recorded decision](examples/example-3.md) — violates/corrects AN-209, AN-210.

## Recall anchors

- A budget is a number in the repo, or it is not a budget.
- The gate blocks the merge, or it is decoration.
- Median of runs, pinned setup — one run is noise.
- Fix it or waive it in writing; waivers expire.
- CI green is not field green.

## Checklist

- [ ] Budget file is committed and names numeric limits per template (AN-201, AN-202).
- [ ] Web-vital limits are at or tighter than 2.5 s / 200 ms / 0.1 (AN-203).
- [ ] `lhci autorun` is a required status check asserting the median of at least three runs (AN-204, AN-205).
- [ ] Every critical endpoint has a numeric p95 budget (AN-206).
- [ ] Third-party scripts have their own budget line (AN-207).
- [ ] Every open waiver names an owner, a reason, and an unexpired date (AN-209).
- [ ] Any limit increase is a standalone change with a DECISIONS.md entry (AN-210).
- [ ] The scheduled field check is running and its last report is in budget or has open defects (AN-212).
