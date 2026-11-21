# unit-economics

## Metadata

- **Owner department:** D1 Product & Requirements (PR)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://www.forentrepreneurs.com/ltv-cac/ ; https://www.construx.com/wp-content/uploads/2019/02/CxWhitePaper_ConeOfUncertainty.pdf
- **Depends on:** product-metrics, pricing-monetization
- **Feeds into:** scope-control, roadmapping

## When to use / Do NOT use

- **Use when:** judging whether an acquisition motion or business model can work; computing or publishing CAC, LTV, their ratio, or payback; producing a cost or effort estimate for a project, feature, or plan.
- **Do NOT use when:** the acquisition motion does not exist yet and the honest output is "directional only" (say so and stop), or the numbers are published marketing metrics rather than economics (use product-metrics).

## Rules

1. **PR-221 — CAC is fully loaded.** CAC = (all sales + marketing cost for the period) ÷ (new customers acquired in the same period). "All" includes salaries, commissions, tools, agencies, and content production — never media spend alone.
2. **PR-222 — LTV is margin-based.** LTV = average revenue per account × gross margin ÷ churn rate, with revenue, margin, and churn stated for the same cohort and period. Revenue-based LTV is never reported as LTV.
3. **PR-223 — Payback uses gross profit.** CAC payback (months) = CAC ÷ monthly gross profit per customer. Ratio and payback are always reported together; either one alone hides the cash problem or the value problem.
4. **PR-224 — Heuristics are heuristics.** LTV:CAC above 3 and payback under 12 months are viability heuristics (Skok), recorded as defaults with an explicit override note when a project departs from them — never applied as universal pass/fail laws to non-SaaS models.
5. **PR-225 — No ratio before a repeatable motion.** LTV:CAC is not computed as a decision number until a repeatable acquisition motion exists. Figures computed earlier are labeled "directional" wherever they appear and cannot anchor commitments.
6. **PR-226 — Estimates are ranges with a method.** Every estimate states a range, the named assumptions, and the method used (analogy, decomposition, or parametric). A single-point estimate with none of these fails review.
7. **PR-227 — Estimate, target, commitment are separate.** The estimate (what the work is expected to take), the target (what the business wants), and the commitment (what was promised externally) are three distinct numbers, recorded separately and never silently merged.
8. **PR-228 — Estimate vs. actual is logged.** Every completed item records its estimate and its actual. A team with no such history states in writing that its estimates are uncalibrated guesses.
9. **PR-229 — Cohort before aggregate.** Economics are computed per cohort or segment first. A blended figure that hides a losing segment is a reporting defect, and the losing segment is reported, not averaged away.
10. **PR-230 — Cone position is stated.** Early estimates name their position on McConnell's Cone of Uncertainty (an initial-concept estimate can run 0.25x–4x the actual) and narrow only as named decisions and decomposition reduce the uncertainty.

## BAN list

- **BAN-PR-111 — Media-only CAC.** Banned: computing CAC from advertising spend alone, excluding salaries, commissions, tools, and agency cost. Defeats: DET-CON-011. Bad: a report states "CAC: $45" from $9,000 of ad spend over 200 customers, while the same period carried $27,000 of salaries, commissions, tools, and agency fees — the real CAC is $180, and every downstream decision inherits the false figure. Instead: fully load the numerator under PR-221. Severity: BLOCK.
- **BAN-PR-112 — Revenue LTV labeled as LTV.** Banned: dividing revenue per account by churn and presenting the result as LTV without applying gross margin. Defeats: DET-CON-011. Bad: "LTV: $4,000" from $120/month ÷ 3% churn, when 75% gross margin makes the margin-based LTV $3,000 — and the published 4.0 ratio is really 3.0. Instead: apply margin under PR-222 and show both inputs. Severity: BLOCK.
- **BAN-PR-113 — Single-point estimate.** Banned: quoting one number ("$80k, three months") with no range, no assumptions, and no method. Defeats: DET-CON-011. Bad: a client plan commits to "the migration will cost $80,000" at concept stage — inside the Cone's 0.25x–4x band, the honest statement is a range roughly four times wide in each direction, and the single point becomes a promise nobody derived. Instead: estimate under PR-226 and PR-230. Severity: BLOCK.
- **BAN-PR-114 — Blended ratio hiding a losing segment.** Banned: publishing one blended LTV:CAC while a named segment's ratio is below 1 and undisclosed. Defeats: DET-CON-015. Bad: the board deck reports a blended 3.4 while the self-serve segment runs at 0.8 and consumes half the spend; the fact sheet and the deck end up telling different stories about the same business. Instead: report per-cohort figures first (PR-229). Severity: BLOCK.

## Gates

- **G-PR-111 — Formula audit.** Verifies: PR-221, PR-222, PR-223. Check (automated): recompute CAC, LTV, ratio, and payback from the raw inputs with a script or spreadsheet and diff against the reported figures (tolerance: rounding only). Pass: all four recomputed values match the report. Fail: block shipment of the report. Recorded in: progress.md.
- **G-PR-112 — Estimate-record check.** Verifies: PR-226, PR-227, PR-230. Check (automated): every estimate record contains the fields range-low, range-high, method, assumptions, cone-position, and separate estimate/target/commitment values; a field-presence scan over the estimates file returns zero incomplete records. Pass: zero incomplete records. Fail: block shipment. Recorded in: progress.md.
- **G-PR-113 — Cohort disclosure check.** Verifies: PR-229. Check (automated): any document reporting a blended LTV, CAC, or ratio must also contain a per-cohort table; `grep -ci "cohort" report.md` ≥ 1 wherever a blended figure appears, and each cohort row shows its own ratio. Pass: blended figures never appear without the cohort table. Fail: warn; the table is added before the figures are used in a decision. Recorded in: progress.md.
- **G-PR-114 — Calibration log review.** Verifies: PR-228. Check (manual): open the estimate-vs-actual log; the last five completed items have both numbers recorded, or the document states that the team is uncalibrated. Pass: log current or the uncalibrated statement present. Fail: warn. Recorded in: progress.md.

## Anti-patterns

- **Precision from nowhere.** A ratio quoted to two decimals ("3.47") whose inputs are a founder's guesses. Catch it by asking for the raw inputs; if they cannot be produced, the decimals are decoration and the figure is directional at best (PR-225).
- **Churn shopping.** Trying monthly, quarterly, and annualized churn and publishing whichever makes LTV largest. Catch it by requiring the churn definition to be written next to the LTV figure and identical across documents.
- **Estimate amnesia.** Each new estimate is produced fresh, with no reference to how the last three estimates performed. Catch it with the calibration log (G-PR-114): an estimate that does not cite the team's historical error range is starting over.
- **Heuristic lawyering.** Treating "above 3" as proof of health while payback stretches past two years, or killing a viable non-SaaS model for missing a SaaS heuristic. Catch it against PR-223 and PR-224: ratio and payback travel together, and overrides are recorded, not smuggled.

## Examples

- [Example 1 — The $45 CAC](examples/example-1.md) — violates/corrects PR-221.
- [Example 2 — Revenue LTV in disguise](examples/example-2.md) — violates/corrects PR-222.
- [Example 3 — The $80,000 promise](examples/example-3.md) — violates/corrects PR-226, PR-230.

## Recall anchors

- CAC is fully loaded or it is fiction.
- LTV is margin-based, or it is revenue wearing a costume.
- Ratio and payback travel together.
- Estimates are ranges with assumptions; single points are promises.
- Cohort before aggregate — blends hide losers.

## Checklist

- [ ] CAC numerator includes salaries, commissions, tools, agencies, content (PR-221, G-PR-111).
- [ ] LTV computed from margin, with revenue, margin, and churn stated (PR-222).
- [ ] Payback reported alongside the ratio (PR-223).
- [ ] Heuristic departures recorded as overrides, not hidden (PR-224).
- [ ] Pre-motion figures labeled "directional" (PR-225).
- [ ] Every estimate carries range, method, assumptions, cone position (PR-226, PR-230, G-PR-112).
- [ ] Estimate, target, and commitment recorded as three numbers (PR-227).
- [ ] Estimate-vs-actual log current for the last completed items (PR-228, G-PR-114).
- [ ] Cohort table present wherever a blended figure appears (PR-229, G-PR-113).
