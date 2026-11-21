# fidelity-verification

## Metadata

- **Owner department:** D16 Cloning & Replication (CL)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://playwright.dev/docs/test-snapshots ; http://umatechnology.org/best-seo-site-migration-monitoring-tools-for-redirects-crawling-and-indexing/
- **Depends on:** clone-ethics (D14 gate), page-inventory, design-extraction, behavior-cloning, page-reconstruction
- **Feeds into:** handover

## When to use / Do NOT use

- **Use when:** An authorized rebuild is ready to be proven against its source — per inventory page, at the agreed viewports, with pixel diffing, DOM comparison, and the behavior-cloning interaction checklist.
- **Do NOT use when:** No D14 authorization record or frozen capture set exists (stop; site-discovery and clone-ethics come first), when a page is labeled `designed` in page-reconstruction (it carries no parity claim to verify), or as a substitute for D8 functional QA on the rebuild's own features.

## Rules

1. **CL-121 — Verify against the frozen capture set.** All comparisons run against the authorized WARC/CDX captures frozen at inventory sign-off, never against the live source, so the target cannot drift mid-verification.
2. **CL-122 — Fix viewports and thresholds before the first run.** The viewport list, the similarity bar (≥95% pixel similarity on key viewports), the per-page vs. aggregate scoring rule, and the masking rules are committed in writing before any comparison runs.
3. **CL-123 — Same engine, same conditions.** Source captures and rebuild screenshots are produced in the same browser engine and version, at the same viewport, in the same state (auth state, fixture data, locale); a mismatch in conditions invalidates the run.
4. **CL-124 — Verify page by page against the inventory.** Every in-scope inventory row receives a comparison result; a page with no run is reported as unverified, never silently counted as passing.
5. **CL-125 — Mask dynamic regions by rule.** Timestamps, rotating content, and similar dynamic regions are masked only via selectors/rules committed under CL-122 before the run; no region is masked ad hoc to rescue a failing page.
6. **CL-126 — Compare DOM structure alongside pixels.** Each comparison reports a structural diff (headings, landmarks, interactive elements present/absent) next to the pixel score; a pixel pass with missing structure is a defect.
7. **CL-127 — Run the behavior checklist per element.** The interaction tests recorded by behavior-cloning execute against the rebuild for every in-scope interactive element; verification is incomplete while any in-scope element is untested.
8. **CL-128 — Log every difference.** Each above-tolerance diff becomes a defect entry or an accepted-deviation record naming the page, the difference, the reason, and the approver; differences are never absorbed into a prose summary.
9. **CL-129 — Baseline changes need a reason and re-approval.** A golden baseline is regenerated only with a recorded reason tied to an approved change; the change and its approver are logged before the new baseline is committed.
10. **CL-130 — Score font deltas by the substitution record.** Where design-extraction recorded a licensed-font substitution, the expected rendering delta is scored as that accepted deviation; it is never hidden by widening a mask or the tolerance.
11. **CL-131 — Exclude and report unverifiable views.** A source view that cannot be captured within the D14 authorization and robots rules is excluded from scoring and listed as unverified in the report; it is never captured by bypass and never scored by guess.
12. **CL-132 — Every claim cites its run.** Any fidelity statement in a deliverable (a percentage, "verified", a per-page verdict) names the run that produced it: date, engine, viewport set, and per-page scores.

## BAN list

- **BAN-CL-061 — Eyeball verdict.** Banned: declaring a page "pixel-perfect", "identical", or "verified" from looking at two screenshots with no diff run behind the claim. Defeats: DET-CRWL-002. Bad: the report says the pricing page is "a pixel-perfect clone" after a side-by-side glance. Instead: run the committed visual comparison and cite its per-page score and diff image. Severity: BLOCK.
- **BAN-CL-062 — Silent baseline regeneration.** Banned: regenerating a golden baseline so a failing comparison turns green, with no reason record. Defeats: DET-CRWL-018. Bad: the home page diff fails at 91%, the baseline is re-screenshotted from the rebuild, and the suite passes at 100%. Instead: log the difference as a defect or an accepted deviation under CL-128, and regenerate only under CL-129. Severity: BLOCK.
- **BAN-CL-063 — Post-failure renegotiation.** Banned: lowering the similarity bar, dropping a viewport, or switching from per-page to aggregate scoring after a run has failed. Defeats: DET-CRWL-018. Bad: after two pages score 93%, the bar is "revisited" to 90% so the report can ship. Instead: keep the CL-122 thresholds; fix the pages or record accepted deviations with reasons. Severity: BLOCK.
- **BAN-CL-064 — Bypass capture for scoring.** Banned: defeating a login, paywall, or robots rule to screenshot a source view for the comparison. Defeats: DET-CRWL-008. Bad: a borrowed customer login is used to capture the dashboard so it can be scored. Instead: exclude the view under CL-131 and report it as unverified, or capture it only through access the client legitimately provisions. Severity: BLOCK.
- **BAN-CL-065 — Full-size source assets in reports.** Banned: embedding the target's full-resolution photography, artwork, or trademark assets in comparison reports beyond the thumbnails the diff itself requires. Defeats: DET-CRWL-009. Bad: the verification appendix ships the source's full-size hero images and logo files "for reference." Instead: include only the expected/actual/diff thumbnails the comparison generated, and reference source assets by capture ID. Severity: BLOCK.

## Gates

- **G-CL-061 — Visual comparison suite (automated).** Verifies: CL-122, CL-124. Check: run the Playwright visual comparison suite in CI against the committed baselines (`npx playwright test --grep @visual`) and collect the per-page diff report. Pass: every in-scope page has a result and every key viewport scores ≥95% similarity or carries an accepted-deviation record. Fail: block shipment. Recorded in: progress.md. Pattern-reference mode: NOT APPLICABLE — no source captures exist to baseline against and this mode makes no visual-parity claim; visual quality is gated by G-CL-025 (adapted) and the D13 gates; see the pattern-reference disposition table in the clone-rebuild playbook.
- **G-CL-062 — Baseline-change audit (automated).** Verifies: CL-129. Check: script lists baseline files changed since the last approved run (`git diff --name-only <last-approved-tag> -- tests/visual/baselines/`) and asserts each has a matching reason record in the deviation log. Pass: zero baseline changes without a reason record and approver. Fail: block shipment. Recorded in: progress.md. Pattern-reference mode: NOT APPLICABLE — no baselines exist (follows G-CL-061); rebuild regression-baseline changes are reviewed under G-CL-064 (adapted); see the pattern-reference disposition table in the clone-rebuild playbook.
- **G-CL-063 — Interaction checklist completeness (automated).** Verifies: CL-127. Check: diff the behavior-cloning in-scope element/flow list against the executed checklist results; any element with no passing test result is listed. Pass: zero untested in-scope elements. Fail: block shipment. Recorded in: progress.md.
- **G-CL-064 — Deviation log review (manual).** Verifies: CL-128, CL-131. Check: review the defect/deviation log against the latest diff report; every above-tolerance diff has a defect entry or an accepted deviation with reason and approver, and every unverified page is listed with its exclusion reason. Pass: log accounts for 100% of reported differences. Fail: block shipment. Recorded in: progress.md. Pattern-reference mode: ADAPTED — the review runs over the deviation log against the playbook's disposition table; every adapted or not-applicable gate and excluded row must carry its entry and reason; see the pattern-reference disposition table in the clone-rebuild playbook.
- **G-CL-065 — Report claim check (automated).** Verifies: CL-132. Check: `grep -rniE 'pixel-perfect|[0-9]+% similar|verified clone' deliverables/` and assert each match cites a run ID present in the verification results store. Pass: no fidelity claim without a backing run. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Aggregate-only reporting.** A single "97% overall" hides the two pages at 88%. Catch it: require the per-page minimum next to any aggregate figure before accepting a report.
- **Viewport cherry-picking.** Only the desktop viewport is compared because mobile "is responsive anyway." Catch it: diff the run's viewport list against the CL-122 committed set.
- **Mask creep.** Masked regions grow run over run until half a page is excluded from scoring. Catch it: track masked-area percentage per page across runs and question any increase.
- **Stale-condition comparison.** The rebuild is screenshotted logged-in while the source capture is logged-out, and the "differences" are all session chrome. Catch it: check the run manifest's state fields against CL-123 before reading scores.

## Examples

- [Example 1 — Eyeball verdict vs. measured diff run](examples/example-1.md) — violates/corrects CL-124, BAN-CL-061.
- [Example 2 — Regenerated baseline vs. reason-recorded change](examples/example-2.md) — violates/corrects CL-129, BAN-CL-062.
- [Example 3 — Buried failing page vs. per-page deviation log](examples/example-3.md) — violates/corrects CL-128, CL-131.

## Recall anchors

- No run, no verdict — fidelity is measured, never eyeballed.
- Thresholds and viewports are fixed before the first run, not after a failure.
- Baselines are evidence: regenerate only with a reason and re-approval.
- Every difference is a defect or an accepted deviation with a name on it.
- Unverifiable means excluded and reported — never bypassed, never guessed.

## Checklist

- [ ] Viewport list, ≥95% bar, scoring rule, and masking rules committed before the first run (CL-122).
- [ ] Comparisons ran against the frozen capture set in one engine under matched conditions (CL-121, CL-123).
- [ ] Every in-scope inventory page has a comparison result or an unverified listing (CL-124, CL-131).
- [ ] DOM structure diff reported alongside every pixel score (CL-126).
- [ ] Interaction checklist shows zero untested in-scope elements (G-CL-063).
- [ ] Every above-tolerance diff is a defect or an accepted deviation with reason and approver (CL-128).
- [ ] Baseline-change audit passes: no unexplained baseline changes (G-CL-062).
- [ ] Every fidelity claim in the deliverables cites its run (CL-132, G-CL-065).
