# structured-data

## Metadata

- **Owner department:** D9 SEO & Content (CO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Google Search Central, introduction to structured data — https://developers.google.com/structured-data/ ; Schema.org vocabulary and validator — https://schema.org ; Google Search spam policies — https://developers.google.com/search/docs/essentials/spam-policies
- **Depends on:** real-content (whether reviews, ratings, and claims may exist at all), fact-sheet (D1, for page-external facts)
- **Feeds into:** technical-seo, aeo, web-analytics

## When to use / Do NOT use

- **Use when:** a page type gains, changes, or loses JSON-LD markup; a template or data model feeding markup changes; or Search Console reports a rich-result error. This skill owns the markup contract; D3 frontend implements the templates against it.
- **Do NOT use when:** the question is whether the underlying content may be published (real-content decides), what the page says (copywriting), or whether the page is crawlable (technical-seo). Never use markup to make a claim the page itself does not make.

## Rules

1. **CO-161 — Generated, never hand-written.** Every JSON-LD block is emitted by a template from the same data store that renders the visible page. No per-page hand-edited or copy-pasted blocks exist; if a value is wrong, the fix lands in the data or the template, never in one page's markup.
2. **CO-162 — Markup says only what the page shows.** Every rating, price, date, author, and availability value in JSON-LD has a visible counterpart on the same page with an identical value. A field with no visible counterpart is removed, not "completed" (DET-CON-024).
3. **CO-163 — One template per page type, kept small.** A schema type is added only when pages of that type genuinely contain the content the type describes. Marking up content the page type does not have — a recipe schema on a product page — is a defect, not ambition.
4. **CO-164 — Required properties complete.** Each template carries every property Google requires for the rich result that page type is eligible for, plus recommended properties wherever the underlying data exists. Eligibility is checked against Google's structured-data documentation per type, not assumed.
5. **CO-165 — No placeholder values, ever.** Generator defaults — "Product Name", price `0.00`, `example.com` URLs, sample organization names — are build failures. A template that cannot populate a required property from real data does not ship.
6. **CO-166 — Review markup follows real reviews.** `Review` and `aggregateRating` markup exists only on pages where real reviews are visibly rendered and have passed real-content. The markup question is never asked before the real-content question is answered.
7. **CO-167 — Prices match everywhere.** `Offer.price` and `priceValidUntil` in markup are identical to the price rendered on the page and the price charged at checkout, drawn from the same price source (DET-CON-016). A sale that ended removes the offer markup in the same change.
8. **CO-168 — JSON-LD, syntactically valid.** JSON-LD is the only format. Every block parses as valid JSON — one trailing comma invalidates the whole block — and validation runs in the build, not by eyeball.
9. **CO-169 — Dates and authors match.** `datePublished`, `dateModified`, and `author` in markup are identical to the visible byline and dates. `dateModified` changes only when the content actually changed, never on a bare redeploy.
10. **CO-170 — Change triggers revalidation.** Any template or data-model change re-runs validation on every affected page type before release. A refactor that touches rendering is presumed to touch markup until validation proves otherwise.
11. **CO-171 — Monitored after deployment.** Search Console enhancement reports are reviewed on the web-analytics cadence. A new error or invalid-item class is a defect with a named owner, not a statistic to watch.
12. **CO-172 — Page-external fields verified, not exempt.** Fields with no visible counterpart by design (e.g. an organization's founding date or logo) are verified against fact-sheet.md before the template ships, and re-verified when the fact sheet changes.

## BAN list

- **BAN-CO-081 — Markup-only claims.** Banned: JSON-LD stating ratings, prices, dates, or authors the visible page never shows. Defeats: DET-CON-024. Bad: a product page renders no rating, but its JSON-LD declares `aggregateRating: 4.8, reviewCount: 212`. Instead: generate the block from the page's data (CO-161); if no reviews render, no rating markup ships (CO-166). Severity: BLOCK.
- **BAN-CO-082 — Generator placeholders in production.** Banned: shipping JSON-LD containing scaffold values such as "Product Name", `price: 0.00`, or `https://example.com/logo.png`. Defeats: DET-CON-003. Bad: a pasted generator block names the product "Product Name" with price 0.00 on the live pricing page. Instead: bind every property to the page's data store and fail the build on placeholder patterns (CO-165, G-CO-083). Severity: BLOCK.
- **BAN-CO-083 — Fabricated review markup.** Banned: `aggregateRating` or `Review` markup without real, visible, attributable reviews behind it. Defeats: DET-CON-013. Bad: markup claims 300 five-star reviews on a page whose review section is empty because "the widget loads later". Instead: no real visible reviews, no review markup — route the reviews themselves through real-content first (CO-166). Severity: BLOCK.
- **BAN-CO-084 — Separately maintained markup copies.** Banned: static JSON-LD blocks stored apart from the page data and edited by hand, so markup and page drift apart over time. Defeats: DET-CON-015. Bad: a developer updates the price in the CMS; the hard-coded JSON-LD in the template footer keeps the old price for three months. Instead: one template reads the same record the page renders (CO-161); price changes propagate in the same commit (CO-167). Severity: BLOCK.
- **BAN-CO-085 — Marking up hidden content.** Banned: describing in JSON-LD any content that is hidden from users on the page (display:none sections, unloaded tabs, geo-gated blocks). Defeats: DET-CON-024. Bad: FAQ markup lists eight questions, but only three are visible; five sit in a hidden div "for SEO". Instead: mark up exactly the visible set; if a question matters, show it (CO-162). Severity: BLOCK.

## Gates

- **G-CO-081 — CI schema validation.** Verifies: CO-164, CO-168. Check: automated — on every build, fetch one sample URL per page type from the staging build, extract each `application/ld+json` block, parse it as JSON, and validate required properties per type against Google's rich-result requirements (Rich Results Test during development). Pass: every block parses and carries all required properties. Fail: block the build. Recorded in: progress.md.
- **G-CO-082 — Markup-vs-visible diff.** Verifies: CO-162, CO-167, CO-169. Check: automated — script diffs `aggregateRating`, `price`, `datePublished`/`dateModified`, and `author` values in JSON-LD against the rendered page text for the same sample URLs. Pass: zero fields without an identical visible counterpart (page-external fields checked against fact-sheet.md per CO-172). Fail: block shipment; this gate runs the DET-CON-024 check. Recorded in: progress.md.
- **G-CO-083 — Placeholder scan.** Verifies: CO-165. Check: automated — grep all emitted JSON-LD in the build output for `Product Name`, `example.com`, `example.org`, `"price": 0`, `Lorem`, and `TODO`. Pass: zero hits. Fail: block the build. Recorded in: progress.md.
- **G-CO-084 — Change-triggered revalidation.** Verifies: CO-170. Check: manual with checklist — any merge touching a markup template or its data model lists the affected page types, and G-CO-081/G-CO-082 results for those types are attached to the change before release. Pass: revalidation evidence present for every affected type. Fail: hold the release. Recorded in: progress.md.
- **G-CO-085 — Enhancement-report review.** Verifies: CO-171. Check: manual — on the web-analytics cadence, open Search Console's rich-result enhancement reports and log new error/invalid classes with a named owner and fix date. Pass: review logged for the current cycle with no unowned error class. Fail: escalate as a defect before the next release. Recorded in: progress.md.

## Anti-patterns

- **Schema maximalism.** Emitting every type in the vocabulary "for coverage" — Event, JobPosting, Course — on pages that contain none of that content. Catch it: for each type on a page, point at the visible content it describes; a type with nothing to point at comes out (CO-163).
- **The copied competitor block.** Lifting a competitor's JSON-LD and swapping the brand name, importing their claims, dates, and ratings along with the structure. Catch it: every value must trace to this site's data store, never to the clipboard (CO-161).
- **Validate-once launch.** Markup validated at launch, then template refactors silently break it for months. Catch it: validation lives in CI and in the change checklist (G-CO-081, G-CO-084), not in launch memory.
- **Rich-result chasing.** Reshaping visible content to fit a markup type the page does not naturally have — inventing an FAQ section solely to earn FAQ markup. Catch it: content decisions come from copywriting and real-content; markup describes what exists, it never commissions what does not.

## Examples

- [Example 1 — Rating markup with no reviews on the page](examples/example-1.md) — violates/corrects CO-166.
- [Example 2 — The generator block that shipped with placeholders](examples/example-2.md) — violates/corrects CO-165.
- [Example 3 — Markup price disagrees with the page and checkout](examples/example-3.md) — violates/corrects CO-167.

## Recall anchors

- Generated from the same data that renders the page — never decorated.
- If the page doesn't show it, the markup doesn't say it.
- No real visible reviews, no rating markup.
- Placeholders are build failures, not drafts.
- Template change means revalidation, every affected type.

## Checklist

- [ ] Every JSON-LD block is template-generated from the page's own data store (CO-161).
- [ ] Every markup field has an identical visible counterpart, or a fact-sheet entry (CO-162, CO-172).
- [ ] Required properties complete for each type's rich result (G-CO-081).
- [ ] Review/aggregateRating markup exists only over real, visible reviews (CO-166).
- [ ] Markup price equals page price equals checkout price (CO-167).
- [ ] Placeholder scan returns zero hits in the build output (G-CO-083).
- [ ] Markup-vs-visible diff passes on a sample URL per page type (G-CO-082).
- [ ] Template or data-model changes carry revalidation evidence (G-CO-084).
