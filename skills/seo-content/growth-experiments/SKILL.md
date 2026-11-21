# growth-experiments

## Metadata

- **Owner department:** D9 SEO & Content (CO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://docs.optimizely.com/experimentation-strategy/docs/take-action-based-on-the-results-of-an-experiment ; Kohavi, Tang & Xu, *Trustworthy Online Controlled Experiments* (Cambridge University Press, 2020)
- **Depends on:** web-analytics, real-content
- **Feeds into:** content-strategy, copywriting

## When to use / Do NOT use

- **Use when:** an A/B test or controlled experiment on a page, flow, price display, or message is being planned, launched, read, or reported — and whenever an experiment result is cited in a decision, brief, or report.
- **Do NOT use when:** the change is a defect fix or a legal/compliance requirement (ship it; do not test whether to fix a bug), the question is what the data says without an intervention (use web-analytics), or the variant copy itself is being written (use copywriting — this skill governs the test around it).

## Rules

1. **CO-261 — Registered before launch.** Every experiment exists in the experiment register before it receives traffic, with: a hypothesis tied to a named user problem, exactly one primary metric, guardrail metrics, the surface it runs on, and an owner. An unregistered test does not launch.
2. **CO-262 — Sample size and runtime computed in advance.** Before launch, the register records the pre-computed sample size per variant, the expected traffic split, and a fixed end date covering at least one full business cycle for the surface (a full week minimum on weekly-cycle traffic). "Run it until it looks significant" is not a runtime.
3. **CO-263 — No peeking decisions.** Results are read at the pre-registered horizon. The only exception is a sequential-testing method (e.g. an alpha-spending or always-valid p-value approach) named in the register before launch. A test stopped early because a variant was "winning" is void and is recorded as void.
4. **CO-264 — The primary metric decides.** The ship / kill / extend decision follows the primary metric alone. Secondary metrics may generate the next hypothesis; they never overturn, soften, or substitute for the primary result.
5. **CO-265 — One experiment per surface.** Two experiments never run on the same surface at the same time unless the register records an interaction-aware design (mutually exclusive buckets or a factorial design) before either launches.
6. **CO-266 — Random assignment, verified split.** Traffic is assigned randomly at the pre-registered split, and a sample ratio mismatch (SRM) check runs before any result is read. An SRM failure invalidates the experiment: the result is not interpreted, the assignment bug is fixed, and the test restarts.
7. **CO-267 — Effect size with a confidence interval.** Every reported result states the primary-metric effect size and its confidence interval, the sample sizes, and the runtime. A bare "significant" / "not significant" verdict, or a percentage lift with no interval, is not a reportable result.
8. **CO-268 — Variants pass the real-content gates.** Variant copy and claims pass the same gates as any shipped page before launch: no fabricated claim or statistic, no unsubstantiated superlative (DET-CON-026), no promise without a backing process (DET-CON-028). An experiment never tests whether a false claim converts better.
9. **CO-269 — Every conclusion is recorded, including losers.** At the horizon, the register entry is completed with the SRM result, the primary-metric effect and interval, and the decision (ship, kill, or inconclusive-extend with its reason). Losing and inconclusive experiments are recorded with the same completeness as winners; an experiment with no completed entry is treated as never having run.
10. **CO-270 — Guardrails can veto a win.** If a guardrail metric (e.g. revenue per visitor, unsubscribe rate, page performance, error rate) degrades beyond the bound set in the register, the variant does not ship even when the primary metric improves; the conflict is recorded in the entry.
11. **CO-271 — No mid-flight changes.** Variant content, traffic split, primary metric, and end date do not change after launch. A needed change closes the experiment as inconclusive and restarts it under a new register ID with the change recorded.
12. **CO-272 — Reports trace to the register.** Any number quoted from an experiment — in a report, brief, case study, or page — matches the register entry and its underlying results export exactly. Screenshots of a dashboard mid-flight and recollected figures are not sources.

## BAN list

- **BAN-CO-131 — The peek-and-stop win.** Banned: ending an experiment before its pre-registered horizon because an interim look showed a variant ahead, and reporting that lead as a result. Defeats: DET-CON-011. Bad: on day two the dashboard shows variant B up 18% at p = 0.04; the test is stopped and the weekly report announces "B wins, +18% conversions". Instead: run to the registered horizon (or use a sequential method named in advance, CO-263) and report the effect with its confidence interval. Severity: BLOCK.
- **BAN-CO-132 — The secondary-metric rescue.** Banned: declaring success on a secondary metric after the primary metric came back flat or negative. Defeats: DET-CON-015. Bad: signup rate (primary) is unchanged, but time-on-page rose, so the experiment is reported as a win and the variant ships. Instead: record the decision the primary metric dictates (CO-264); log the secondary observation as the hypothesis for a new registered experiment. Severity: BLOCK.
- **BAN-CO-133 — Testing a fabricated claim.** Banned: putting an invented statistic, testimonial, or unsubstantiated superlative into a variant to see if it lifts conversion. Defeats: DET-CON-026. Bad: variant B's headline reads "Join 50,000+ teams — rated #1 by founders", figures the business cannot produce a source for. Instead: variants use only fact-sheet-backed claims (CO-268); test the presentation of a true claim, never the invention of one. Severity: BLOCK.
- **BAN-CO-134 — The unrecorded experiment.** Banned: running, stopping, or citing an experiment that has no register entry, or quoting its outcome from memory or a dashboard screenshot. Defeats: DET-CON-014. Bad: "We tested the red button last month, it did about 10% better" appears in a planning brief, with no hypothesis, sample size, or data anywhere. Instead: no entry, no experiment (CO-261); results are cited only from a completed register entry and its export (CO-272). Severity: BLOCK.
- **BAN-CO-135 — The unbacked-promise variant.** Banned: testing a variant whose offer, guarantee, or service promise has no backing policy or process behind it. Defeats: DET-CON-028. Bad: variant B promises "replies within one hour, guaranteed" on a support page staffed for next-business-day responses. Instead: the promise ships in a variant only when the process that makes it true exists and is linked (CO-268). Severity: BLOCK.

## Gates

- **G-CO-131 — SRM check (automated).** Verifies: CO-266. Check: in the results pipeline, run the chi-square test on observed vs expected assignment counts, e.g. `python3 -c "from scipy.stats import chisquare; print(chisquare([5231, 4769], f_exp=[5000, 5000]))"` with the experiment's real counts substituted. Pass: p-value > 0.001. Fail: the result is void — do not read the metrics; fix the assignment, record the failure, restart. Recorded in: progress.md.
- **G-CO-132 — Pre-launch registration check.** Verifies: CO-261, CO-262, CO-265. Check: `grep -A 12 "EXP-<id>" experiments/register.md` and confirm the entry shows the hypothesis, one primary metric, guardrails, pre-computed sample size, fixed end date, surface, and owner — and that no other active entry names the same surface. Pass: all fields present, surface exclusive. Fail: block the launch until the entry is complete. Recorded in: progress.md.
- **G-CO-133 — Variant real-content pass.** Verifies: CO-268. Check: extract every claim, figure, and promise from each variant and trace it to fact-sheet.md or a producible source record; assist with `grep -niE "best|#1|guarantee|risk-free|trusted by|% (faster|better|more)" variants/<id>/` and clear or cut each hit. Pass: every claim traced. Fail: the variant does not launch. Recorded in: progress.md.
- **G-CO-134 — Horizon and decision audit.** Verifies: CO-263, CO-264, CO-269. Check: manual audit of the last concluded experiment — the decision date is on or after the registered end date, the recorded decision follows the primary metric, and the entry carries the SRM result, effect size, and confidence interval. Pass: all four hold. Fail: the conclusion is withdrawn, the entry corrected, and the result is not cited anywhere until it passes. Recorded in: progress.md.
- **G-CO-135 — Register completeness sweep.** Verifies: CO-269, CO-272. Check: list every experiment marked concluded in the register; each has a completed entry (hypothesis, primary metric, SRM, effect, decision), including losers and inconclusive runs. Pass: zero concluded experiments with incomplete entries. Fail: complete the entries from the results exports before any new launch. Recorded in: progress.md.

## Anti-patterns

- **The daily dashboard glance.** Checking the experiment every day "just to watch", then unconsciously timing unrelated decisions around a mid-flight lead. Catch it: if you cannot state the pre-registered end date without looking it up, you are watching, not running a test.
- **The kitchen-sink variant.** Variant B changes the headline, price display, layout, and CTA at once, so a win (or loss) can never be attributed. Catch it: a variant that needs the word "and" twice to describe what changed is several experiments pretending to be one.
- **Novelty read as durability.** A week-one spike from returning users reacting to any visible change is reported as a lasting lift. Catch it: results read before one full business cycle, or with no new-vs-returning split considered, get an inconclusive-extend, not a ship.
- **The underpowered null.** Traffic far below the pre-computed sample size produces "no significant difference", which is then quoted as proof the change does not matter. Catch it: compare achieved sample against the CO-262 computation — an underpowered null is an inconclusive result, recorded as such.

## Examples

- [Example 1 — The two-day "winner"](examples/example-1.md) — corrects CO-263 and CO-266.
- [Example 2 — The secondary-metric rescue](examples/example-2.md) — corrects CO-264 and CO-269.
- [Example 3 — The variant with an unbacked promise](examples/example-3.md) — corrects CO-268.

## Recall anchors

- Registered before launch, or it does not run.
- Read at the horizon, never at the peek.
- The primary metric decides; secondaries only suggest the next test.
- SRM first — a broken split voids everything downstream.
- Losers get register entries too.

## Checklist

- [ ] Register entry complete before launch: hypothesis, one primary metric, guardrails, owner (G-CO-132).
- [ ] Sample size computed and end date fixed, covering at least one full business cycle (CO-262).
- [ ] Surface is exclusive to this experiment, or an interaction-aware design is recorded (CO-265).
- [ ] Every variant claim traced to the fact sheet — no invented figures, superlatives, or unbacked promises (G-CO-133).
- [ ] SRM check passed before any metric was read (G-CO-131).
- [ ] Decision taken at the horizon, on the primary metric, with guardrails checked (CO-263, CO-264, CO-270).
- [ ] Register entry completed with effect size, confidence interval, SRM result, and decision — win, loss, or inconclusive (G-CO-135).
