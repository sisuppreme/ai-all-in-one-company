# competitive-analysis

## Metadata

- **Owner department:** D1 Product & Requirements (PR)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://www.nngroup.com/articles/competitive-usability-evaluations/
- **Depends on:** user-research, fact-sheet
- **Feeds into:** pricing-monetization, requirements-writing, roadmapping

## When to use / Do NOT use

- **Use when:** positioning a product, deciding build/skip on a feature a competitor has, preparing differentiation claims for copy, or capturing competitor pricing as an input to pricing decisions.
- **Do NOT use when:** the question is what users need (use user-research and discovery), or the output would be a feature checklist with no decisions attached — that is unfinished work under this skill, not a deliverable.

## Rules

1. **PR-161 — Named comparison set.** The analysis names 2–4 direct competitors plus the relevant indirect alternatives, including "do nothing" / the current workaround the customer uses today.
2. **PR-162 — Same tasks, hands-on.** The same core tasks are run in each product using trial or real accounts. A capability is recorded as present only when the analyst performed it or saw it performed.
3. **PR-163 — Every cell is dated evidence.** Every cell of the comparison matrix carries a date and an evidence link (screenshot, note file, or trial record). A cell without both is empty, whatever text it contains.
4. **PR-164 — Unverified means labeled unverified.** A feature known only from a competitor's marketing page is recorded as "claimed, unverified" and is never used as the basis for a build decision or a differentiation claim.
5. **PR-165 — Pricing from the source.** Competitor prices are captured from the actual pricing page or trial checkout, with the capture date, and handed to the fact sheet. Prices are never re-typed from memory, screenshots of screenshots, or third-party roundup articles.
6. **PR-166 — Shared scoring criteria.** Products are scored against the same criteria for every row: capability coverage, usability on the task, price as actually charged, and proof offered. Criteria are fixed before scoring starts.
7. **PR-167 — Analysis ends in decisions.** The document closes with recorded decisions — build / skip / position against — each citing the matrix cells it rests on. A matrix with no decisions section is unfinished.
8. **PR-168 — Differentiation names its set.** Any differentiation claim states the comparison set it was measured against ("of the three tools trialed on 2026-11-10…"). A claim with no named set does not leave this document.
9. **PR-169 — Refresh interval is stated.** The matrix carries a refresh date. Cells older than the refresh interval are expired and cannot support new claims or decisions until re-verified.
10. **PR-170 — Conclusions cite cells.** Every conclusion (table stakes, gap, differentiation) cites the specific matrix cells behind it, so a reviewer can re-run the evidence without redoing the analysis.

## BAN list

- **BAN-PR-081 — Marketing-page matrix.** Banned: filling a comparison matrix from competitors' marketing pages without running the tasks hands-on. Defeats: DET-CON-026. Bad: the matrix records "Competitor X: AI reports ✓" because X's landing page shows a screenshot of a report, though the trial account has no such feature. Instead: verify hands-on or mark the cell "claimed, unverified" (PR-164). Severity: BLOCK.
- **BAN-PR-082 — Setless superlative.** Banned: a differentiation claim of the form "#1", "best", "leading", or "fastest" with no named comparison set, criteria, or date. Defeats: DET-CON-026. Bad: the positioning doc declares "the best invoicing tool for freelancers" after trialing no other invoicing tool. Instead: name the set and criteria, or rewrite as a plain description of what the product does (PR-168). Severity: BLOCK.
- **BAN-PR-083 — Unsourced competitor numbers.** Banned: quoting a competitor's user count, rating, or market figure in the analysis or in copy without a source the reader can check. Defeats: DET-CON-011. Bad: "Competitor Y serves 50,000 teams" copied from Y's own homepage counter into a pitch deck as established fact. Instead: cite the source and its nature ("per Y's homepage, 2026-11-21"), or drop the number. Severity: BLOCK.
- **BAN-PR-084 — Memory-typed competitor prices.** Banned: entering a competitor's price into the matrix, the fact sheet, or a pricing decision from memory or from a roundup article instead of the live pricing page or checkout. Defeats: DET-CON-016. Bad: the matrix lists Y at "$19/user" from a blog roundup; Y's actual pricing page charges $24, and the team's own price is set against the wrong figure. Instead: capture from the source with a date (PR-165). Severity: WARN.

## Gates

- **G-PR-081 — Evidence coverage scan.** Verifies: PR-163. Check (automated): export the matrix to CSV and run `awk -F, '$4=="" || $5=="" {n++} END {print n+0}' matrix.csv` (columns 4–5: evidence link, date). Pass: output is 0 — 100% of filled cells carry a dated evidence link. Fail: block shipment. Recorded in: progress.md.
- **G-PR-082 — Freshness check.** Verifies: PR-169. Check (automated): `grep -i "refresh" analysis.md` shows a stated refresh interval, and no cell date in the matrix export is older than that interval relative to today. Pass: zero expired cells in use. Fail: warn; expired cells are re-verified or struck before the analysis supports new decisions. Recorded in: progress.md.
- **G-PR-083 — Decisions-present check.** Verifies: PR-167, PR-170. Check (automated): `grep -ciE "decision|build:|skip:|position" analysis.md` returns at least one decision entry. Pass: decisions section present. Fail: block shipment — the analysis is unfinished. Recorded in: progress.md.
- **G-PR-084 — Hands-on sample audit.** Verifies: PR-162, PR-164, PR-167, PR-170. Check (manual): pick three cells marked verified; the analyst's trial notes or screenshots must show the task being performed. Any cell that cannot be evidenced is relabeled "claimed, unverified". Also verify that each decision line in the decisions section cites at least one cell reference; a decision with no cell citation is unfinished. Pass: all three sampled cells evidenced and every decision line carries a cell citation. Fail: warn and relabel before use. Recorded in: progress.md.

## Anti-patterns

- **Checklist envy.** The matrix grows a row for every feature any competitor mentions, and the roadmap inherits all of them. Catch it by asking, per row, which recorded user problem the feature answers; rows with no answer are context, not backlog.
- **Strawman competitor.** The weakest or most outdated competitor is chosen as the comparison anchor so the home product wins every row. Catch it by checking the set against PR-161: the set must include the competitor customers actually name.
- **Screenshot archaeology.** Cells are "verified" against screenshots from an old trial, a YouTube review, or a previous quarter's matrix. Catch it with the date column: evidence older than the refresh interval is archaeology, not verification.
- **Matrix as decoration.** A thorough matrix is produced, presented once, and never cited by any later decision. Catch it at review: ask for the last three product decisions and whether any cite a cell.

## Examples

- [Example 1 — The landing-page feature matrix](examples/example-1.md) — violates/corrects PR-162, PR-164.
- [Example 2 — "Best" with no set](examples/example-2.md) — violates/corrects PR-168.
- [Example 3 — A matrix that decided nothing](examples/example-3.md) — violates/corrects PR-167.

## Recall anchors

- A competitor's marketing page is a claim, not evidence.
- Every cell: a date and an evidence link, or it is empty.
- Pricing comes from the pricing page, never from memory.
- Differentiation names its comparison set or it is cut.
- A matrix with no decisions is unfinished.

## Checklist

- [ ] Comparison set named: 2–4 direct competitors plus indirect/do-nothing (PR-161).
- [ ] Same core tasks run hands-on in each product (PR-162).
- [ ] 100% of matrix cells carry date + evidence link (PR-163, G-PR-081).
- [ ] Unverified features labeled "claimed, unverified" (PR-164).
- [ ] Competitor prices captured from live pricing pages and handed to the fact sheet (PR-165).
- [ ] Decisions section written, each decision citing matrix cells (PR-167, PR-170, G-PR-084).
- [ ] No superlative claim without a named comparison set (PR-168).
- [ ] Refresh date stated and no expired cells in use (PR-169, G-PR-082).
