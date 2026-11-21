# fact-sheet

## Metadata

- **Owner department:** D1 Product & Requirements (PR)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Mitchell et al., "Model Cards for Model Reporting," FAT* 2019 — https://arxiv.org/html/1810.03993 ; GOV.UK publishing guidance, "Use clear language" — https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-language/
- **Depends on:** requirements-writing, competitive-analysis, pricing-monetization
- **Feeds into:** real-content, copywriting, structured-data

## When to use / Do NOT use

- **Use when:** any fact about the product is about to be published anywhere — copy, pricing pages, structured data, decks, sales material — or when the single source of truth for product facts is created or re-verified. The sheet is written before any public copy.
- **Do NOT use when:** the content makes no factual claim (pure interface text, navigation labels). Do not use the sheet as a marketing document; the moment it reads like a brochure it has stopped being a fact sheet.

## Rules

1. **PR-121 — Sheet-first.** A fact enters copy, pricing pages, structured data, or sales material only after it exists in the fact sheet with its evidence. Copy is never the first place a fact appears.
2. **PR-122 — Fixed template.** The sheet uses the fixed sections: identity and provenance, intended use, inputs and dependencies, measured performance, risks, and limitations. No section is omitted. The section names come from model reporting; for a non-AI product, map the product's facts onto them instead of forcing them into model terms: identity and provenance holds the canonical product, plan, and company names (PR-129), the plan terms and prices (mirrored against billing, PR-130), and the source each fact came from; inputs and dependencies holds the data the product collects and processes, its third-party services and processors, and its billing configuration; measured performance holds the product's measured operational figures and its published limits and quotas, each with evidence (PR-123, PR-125). Where a model reading of a section does not apply — model identity under identity and provenance, training or evaluation data under inputs and dependencies — mark that reading "not applicable — non-AI product" in the sheet; the marked section satisfies G-PR-061, while an invented model fact or a plausible fill fails PR-126.
3. **PR-123 — Every number traces.** Each quantitative claim in the sheet links to the measurement, dataset, or document behind it. An untraceable number is removed, or marked UNVERIFIED in the sheet itself.
4. **PR-124 — No marketing register.** The sheet contains no superlatives and no promotional language. It reads like a lab report, not a brochure.
5. **PR-125 — Disaggregate performance.** Performance is reported broken down by the conditions that change it. An aggregate-only figure is flagged in the sheet as incomplete until the breakdown exists.
6. **PR-126 — Unknown means "not measured".** A field with no data states "not measured". A plausible fill is a fabrication.
7. **PR-127 — Owned and dated.** The sheet names an owner and a review date. A sheet past its review date blocks new claims until the owner re-verifies it.
8. **PR-128 — Limitations are mandatory.** The limitations section is non-empty for every product. A sheet claiming no limitations is rejected on sight.
9. **PR-129 — Names are canonical.** Product, plan, company, and person names appear in the sheet in their one canonical form. Every surface copies the name from the sheet, character for character.
10. **PR-130 — Prices mirror billing.** Prices and plan terms in the sheet match the billing configuration exactly. The sheet is updated in the same change as any price change — never after, never separately. Where no billing provider exists, the sheet's own price entries are the source of truth (see G-PR-063).
11. **PR-131 — One sheet per product.** All departments cite the same sheet. Private copies and per-page fact variants are merged into it or deleted.
12. **PR-132 — Changes are versioned.** Every fact change carries a date and a reason in the sheet's history, and downstream surfaces are re-checked against the new value.

## BAN list

- **BAN-PR-061 — Copy-first facts.** Banned: publishing a claim that does not exist in the fact sheet. Defeats: DET-CON-014. Bad: the landing page announces "founded in 2019" while the sheet holds no founding date at all — the year was invented to fill the layout. Instead: add the fact to the sheet with its evidence first, then publish it. Severity: BLOCK.
- **BAN-PR-062 — The invented statistic.** Banned: any number, in the sheet or in copy, with no measurement, dataset, or document behind it. Defeats: DET-CON-011. Bad: "87% faster onboarding" generated for the hero section. Instead: measure it and cite the dataset, or delete the number. Severity: BLOCK.
- **BAN-PR-063 — The borrowed credential.** Banned: entering an award, certification, press mention, or partnership claim without the issuer's own confirmation. Defeats: DET-CON-012. Bad: "As featured in TechDaily" in the sheet, with no article in existence. Instead: link the issuer's or outlet's own listing, or remove the claim. Severity: BLOCK.
- **BAN-PR-064 — The plausible fill.** Banned: filling an unknown sheet field with a reasonable-sounding value instead of "not measured". Defeats: DET-CON-011. Bad: uptime recorded as "99.9%" because "that is the standard figure". Instead: write "not measured" until instrumentation exists, then record the measured value with its source. Severity: BLOCK.
- **BAN-PR-065 — The brochure sheet.** Banned: superlatives or promotional claims inside the sheet itself. Defeats: DET-CON-026. Bad: the sheet's summary calls the product "the leading platform for dispatch teams". Instead: state the measurable fact (customers, market, date) or state nothing. Severity: WARN.

## Gates

- **G-PR-061 — Template completeness.** Verifies: PR-122, PR-127, PR-128. Check: automated — run a script over fact-sheet.md confirming all fixed sections are present, the limitations section is non-empty, an owner is named, and the review date is in the future. Pass: all four conditions true. Fail: block new claims until the sheet is repaired. Recorded in: progress.md.
- **G-PR-062 — Claim-trace audit.** Verifies: PR-121, PR-123. Check: semi-automated — extract quantitative claims from shipped copy with a script, sample 10, and resolve each against a sheet entry with an evidence link. Pass: 10 of 10 trace. Fail: one untraceable claim fails the release's content pass. Recorded in: progress.md.
- **G-PR-063 — Price mirror diff.** Verifies: PR-130. Check: automated — diff the sheet's prices and plan names against the billing configuration export. Where no billing provider exists, the diff runs against the fact sheet's own price entries as the source of truth, per pricing-monetization PR-210. Pass: zero differences. Fail: block the release. Recorded in: progress.md.
- **G-PR-064 — Staleness block.** Verifies: PR-127. Check: automated — compare the sheet's review date against today's date at release time. Pass: the review date is in the future. Fail: block new claims until the owner re-verifies the sheet. Recorded in: progress.md.

## Anti-patterns

- **The fossil sheet.** Written once at launch and never re-verified; review dates are quietly pushed forward instead. Catch it: read the history — date edits with no fact changes and no re-verification note are the tell.
- **Shadow sheets.** A sales deck or help doc keeps its own numbers, which drift from the sheet a little more each quarter. Catch it: search the project for second copies of the key figures; every copy found is merged or deleted (PR-131).
- **Evidence-link rot.** The links behind the numbers die, or point at dashboards nobody outside one team can open. Catch it: at review, open every evidence link; a dead or inaccessible link demotes its claim to UNVERIFIED until repaired.
- **Precision theater.** Numbers stated to three decimal places from a sample of four customers. Catch it: compare the stated precision against the dataset size recorded in the evidence; precision the data cannot support is cut back.

## Examples

- [Example 1 — A copy-first fact corrected to sheet-first](examples/example-1.md) — corrects PR-121.
- [Example 2 — Disaggregating a performance figure](examples/example-2.md) — corrects PR-125.
- [Example 3 — Replacing a plausible fill with "not measured"](examples/example-3.md) — corrects PR-126.

## Recall anchors

- Sheet first, copy second — never the reverse.
- Every number traces or it is marked UNVERIFIED.
- Unknown is written "not measured", never filled.
- No superlatives in the sheet, ever.
- One sheet, one owner, one review date.

## Checklist

- [ ] Template completeness passes: all sections, non-empty limitations, owner, future review date (G-PR-061).
- [ ] Every quantitative claim in the sheet links to evidence (PR-123).
- [ ] Performance figures are disaggregated by condition (PR-125).
- [ ] No field carries a plausible fill; unknowns say "not measured" (PR-126).
- [ ] Names match the canonical forms used on every surface (PR-129).
- [ ] Prices diff clean against the billing configuration (G-PR-063).
- [ ] The claim-trace audit sample resolved 10 of 10 (G-PR-062).
- [ ] Fact changes carry date and reason in the history (PR-132).
