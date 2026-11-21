# design-extraction

## Metadata

- **Owner department:** D16 Cloning & Replication (CL)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/ ; https://backlight.dev/docs/style-dictionary
- **Depends on:** clone-ethics (D14 gate), site-discovery, page-inventory
- **Feeds into:** page-reconstruction, fidelity-verification

## When to use / Do NOT use

- **Use when:** An authorized rebuild needs the target's design system — tokens for color, type, spacing, radii, shadows, breakpoints, and component states — sampled from the live or archived source.
- **Do NOT use when:** No D14 authorization record exists (stop; clone-ethics gates first), when only one page's appearance is needed (record it in page-inventory instead), or to capture the target's branding for reuse (never; see BAN-CL-024).

## Rules

1. **CL-041 — Authorization precedes sampling.** No computed style is sampled before the D14 clone-ethics authorization record exists and predates the first sampling log entry.
2. **CL-042 — Sample the system, not a page.** Sample computed styles across at least one page per template from page-inventory, never from a single page; a token set built from one page is a trace, not a system.
3. **CL-043 — Sample every interactive state.** For each interactive component, sample default, hover, focus, disabled, and error states; a state that cannot be reached within authorization is recorded as unsampled, never invented.
4. **CL-044 — Tokens are measurements only.** Each token records a measured value (hex/rgb, px/rem, font stack, weight, shadow, radius, breakpoint) traced to at least one sampled element's page, selector, and state.
5. **CL-045 — Cluster near-identical values.** Raw values within a recorded tolerance (e.g. spacing within 1px, colors within one hex step per channel) collapse into one token; the token file keeps the cluster's sample count so distributions stay visible.
6. **CL-046 — Type is a scale, not a list.** Record the full font stack, every sampled font-size/line-height/weight pairing, and the ratio pattern between steps; a flat list of sizes with no scale fails the extraction.
7. **CL-047 — Breakpoints are sampled, not assumed.** Record each media-query breakpoint found in the source's CSS or observed by resizing; never substitute framework defaults (768/1024) for measured values.
8. **CL-048 — Export in DTCG format.** The token file uses the W3C Design Tokens format (`$value`, `$type`, groups, aliases) and is the single source the rebuild consumes.
9. **CL-049 — Compile, never retype.** CSS variables and JS constants are generated from the token file with Style Dictionary or an equivalent compiler; no token value is hand-typed into a page stylesheet.
10. **CL-050 — Font substitution is a recorded decision.** If a sampled font is commercial and unlicensed for the rebuild, the token file names the substitute and the accepted visual delta in a substitution record; silent substitution is a defect.
11. **CL-051 — Branding is flagged, never tokenized.** The target's logo, wordmarks, brand artwork, and copy strings are recorded in a replace-list for the operator's own assets; they never appear as token values or rebuild assets.
12. **CL-052 — Sampling obeys crawl rules.** Sampling uses authorized/public pages only, honors robots.txt, identifies the agent, and never bypasses a login or paywall to capture a gated state.

## BAN list

- **BAN-CL-021 — Invented palette.** Banned: publishing tokens whose values were guessed or "close enough" rather than sampled. Defeats: DET-CRWL-018. Bad: the rebuild uses #2563eb because the source "looked like Tailwind blue." Instead: sample the element's computed `color`/`background-color` and tokenize the returned value. Severity: BLOCK.
- **BAN-CL-022 — Hardcoded values in the rebuild.** Banned: hex, px, or font-stack literals in page CSS that exist in no token. Defeats: DET-VIS-043. Bad: one template ships `border-radius: 10px` typed inline while the token says 8px. Instead: reference the compiled variable generated from the token file. Severity: BLOCK.
- **BAN-CL-023 — Silent font substitution.** Banned: swapping an unlicensed source font for a similar-looking one with no record. Defeats: DET-VIS-011. Bad: the rebuild quietly uses Inter where the source used a commercial grotesque. Instead: add a substitution record naming the source font, the substitute, and the accepted delta. Severity: BLOCK.
- **BAN-CL-024 — Tokenized branding.** Banned: capturing the target's logo, wordmark, brand artwork, or copy as tokens or reusable assets. Defeats: DET-CRWL-009. Bad: the source's logo SVG is saved into the rebuild's asset folder "as a token." Instead: log the logo on the replace-list with its measured size and placement; the operator supplies their own mark. Severity: BLOCK.
- **BAN-CL-025 — Gated-state capture by bypass.** Banned: sampling styles behind a login or paywall using borrowed credentials or an access workaround. Defeats: DET-CRWL-014. Bad: a shared customer login is used to sample the dashboard theme. Instead: record gated states as unsampled, or sample only through access the client legitimately provisions. Severity: BLOCK.

## Gates

- **G-CL-021 — Token traceability diff (automated).** Verifies: CL-044, CL-045. Check: script re-samples computed styles from the recorded source pages/states and diffs every token value against the samples; any token with no matching sample (within its cluster tolerance) fails. Pass: 100% of tokens trace to ≥1 sample. Fail: block shipment. Recorded in: progress.md. Pattern-reference mode: NOT APPLICABLE — tokens are authored, not extracted, so no source samples exist; token discipline is gated by G-CL-022 and G-CL-025 (adapted); see the pattern-reference disposition table in the clone-rebuild playbook.
- **G-CL-022 — Orphan-value scan (automated).** Verifies: CL-049. Check: `grep -rE '#[0-9a-fA-F]{3,8}|font-family:'` run against the built CSS output (e.g. `dist/assets/*.css`, adjusted to the project's actual output layout) and compare every hit against the compiled token output; any value present in no token fails. The gate record must name the actual path scanned, so the scan never runs vacuously against a path the project does not produce. Pass: zero orphan values. Fail: block shipment. Recorded in: progress.md.
- **G-CL-023 — State coverage check (automated).** Verifies: CL-043. Check: script asserts every interactive component in the extraction log has entries for default/hover/focus/disabled/error or an explicit "unsampled — reason" record. Pass: no state silently missing. Fail: block shipment. Recorded in: progress.md. Pattern-reference mode: ADAPTED — the component list checked is the pattern inventory's, and unsampled records read as designed-state records from the design record; see the pattern-reference disposition table in the clone-rebuild playbook.
- **G-CL-024 — Replace-list completeness (manual).** Verifies: CL-051. Check: review the extraction output for logo, wordmark, artwork, and copy items; each must appear on the replace-list and none in the token file or asset folders. Pass: replace-list covers all branding found; token file contains measurements only. Fail: block shipment. Recorded in: progress.md. Pattern-reference mode: ADAPTED — the review runs over the pattern inventory and the build's asset folders, and the replace-list is the inventory's protected-items list; see the pattern-reference disposition table in the clone-rebuild playbook.
- **G-CL-025 — Token-only render (manual).** Verifies: CL-042, CL-048. Check: render one page per template using only the compiled token file, side by side with the source capture; check palette, type scale, spacing rhythm, radii, and states. Pass: no systematic drift; per-value differences trace to a substitution record. Fail: rework extraction. Recorded in: progress.md. Pattern-reference mode: ADAPTED — the token-only render runs, compared against the pattern inventory's recorded design characteristics, not a source capture; see the pattern-reference disposition table in the clone-rebuild playbook.

## Anti-patterns

- **Homepage-only extraction.** Sampling stops at the home page because it "represents the brand"; interior templates quietly drift. Catch it: compare the sampled page list against page-inventory's template list before exporting.
- **Single-sample spacing.** One measured margin becomes "the spacing scale." Catch it: a spacing token with sample count 1 is a suspicion, not a scale — sample more pages.
- **Screenshot eyeballing.** Values are read off a screenshot with a color picker instead of computed styles, baking in compression and scaling error. Catch it: every token must name the element it was computed from.
- **State blindness.** Only the default state is sampled, so hover/focus/error styling is invented during the rebuild. Catch it: run the state coverage check before calling extraction done.

## Examples

- [Example 1 — Guessed palette vs. sampled tokens](examples/example-1.md) — violates/corrects CL-044, BAN-CL-021.
- [Example 2 — Inline radius vs. compiled token](examples/example-2.md) — violates/corrects CL-049, BAN-CL-022.
- [Example 3 — Logo as asset vs. replace-list entry](examples/example-3.md) — violates/corrects CL-051, BAN-CL-024.

## Recall anchors

- Sample the system across templates and states, never one page.
- Every token traces to a computed style — no sample, no token.
- Compile from the token file; never retype a value.
- Branding goes on the replace-list, never in the token file.
- Unlicensed font? Record the substitution and the delta.

## Checklist

- [ ] D14 authorization record exists and predates the first sampling entry (CL-041).
- [ ] At least one page per inventory template was sampled (CL-042).
- [ ] All five states sampled or explicitly recorded unsampled per component (CL-043).
- [ ] Token file is valid DTCG format and every token traces to a sample (CL-048, G-CL-021).
- [ ] Built CSS contains zero values absent from the token file (G-CL-022).
- [ ] Every font substitution has a record naming the accepted delta (CL-050).
- [ ] Replace-list covers all logos, wordmarks, artwork, and copy found (CL-051).
- [ ] Token-only render checked against source captures for one page per template (G-CL-025).
