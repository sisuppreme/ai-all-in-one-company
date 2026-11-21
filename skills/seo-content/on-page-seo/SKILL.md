# on-page-seo

## Metadata

- **Owner department:** D9 SEO & Content (CO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://developers.google.com/search/docs/appearance ; https://developers.google.com/search/docs/essentials/spam-policies
- **Depends on:** technical-seo, fact-sheet
- **Feeds into:** aeo, geo, structured-data, internal-linking

## When to use / Do NOT use

- **Use when:** an indexable page is created, rewritten, or audited — assigning its search intent, writing its title, H1, heading outline, body, and meta description, or resolving two pages that compete for the same query.
- **Do NOT use when:** the problem is crawlability, indexation, canonicals, or rendering (use technical-seo), when the deliverable is structured data markup (use structured-data), or when the page is non-indexable app UI that no searcher should land on.

## Rules

1. **CO-021 — One page, one primary intent.** Every indexable page is mapped in the intent map to exactly one primary search intent drawn from real query data (Search Console or documented keyword research); a page with no mapped intent is not published as indexable.
2. **CO-022 — Metadata is written last.** The title and meta description are written from the finished page content, never from the brief or template, so both describe what the visitor actually gets.
3. **CO-023 — Unique title and description per page.** No two indexable pages share a title or a meta description, and neither is ever a template default or placeholder string.
4. **CO-024 — Titles state topic and offer plainly.** A title names the page's topic and its concrete offer in natural language a searcher would type; it contains no repeated keyword variants and no claim the page does not support.
5. **CO-025 — One H1, real heading outline.** Each page has exactly one H1 matching its primary intent, and H2/H3 headings form a true outline of the page's argument in reading order — no heading exists only to hold a keyword.
6. **CO-026 — Body satisfies the intent first.** The page's opening section answers the primary query directly with page-specific facts; supporting sections expand it. Generic filler that could sit on any competitor's page is cut.
7. **CO-027 — Descriptions promise only what the page delivers.** Every offer, price, feature, or outcome named in the meta description appears on the page itself, worded consistently with fact-sheet.md.
8. **CO-028 — Intent collisions are resolved in writing.** When a new page targets an intent an existing page owns, the intent map records the resolution before publication: merge, redirect, or a written differentiation (page-specific facts, audience, or format).
9. **CO-029 — Claims on the page are sourced or removed.** Any statistic, ranking, or superlative in title, headings, or body carries a citation on the page or in fact-sheet.md; unmeasurable superlatives ("best", "leading") are deleted, not softened.
10. **CO-030 — Intent map is re-checked quarterly.** The top indexable pages are sampled against Search Console query data each quarter; a page whose real queries no longer match its mapped intent is reassigned, merged, or rewritten.

## BAN list

- **BAN-CO-011 — Keyword-stuffed title.** Banned: a title that repeats keyword variants or lists services instead of stating the topic plainly. Defeats: DET-CON-022. Bad: `<title>Cheap Shoes | Best Shoes Online | Buy Shoes Sale Shoes Store</title>`. Instead: state the topic and offer once, in natural language: `<title>Running Shoes for Flat Feet — Fit Guide & Picks</title>`. Severity: BLOCK.
- **BAN-CO-012 — Duplicate or default metadata.** Banned: the same title or meta description on multiple pages, or template defaults shipped to production. Defeats: DET-CON-022. Bad: twelve product pages all titled "Our Products — Company" with description "Add a description here". Instead: write a unique title and description per page from its finished content (CO-022, CO-023). Severity: BLOCK.
- **BAN-CO-013 — Meta description advertising an absent offer.** Banned: a description that promises a discount, feature, or outcome the page does not contain. Defeats: DET-CON-022. Bad: description says "Free returns for a year" while the page and policy allow 30 days. Instead: describe only what the page delivers, consistent with fact-sheet.md (CO-027). Severity: BLOCK.
- **BAN-CO-014 — Scaled near-duplicate intent pages.** Banned: publishing many pages that target the same intent with swapped nouns (city, product, audience) and no page-specific substance. Defeats: DET-CON-025. Bad: 40 location pages identical except the city name and one stock photo. Instead: merge into one strong page, or differentiate each with real page-specific facts, audience, or format recorded in the intent map (CO-028). Severity: BLOCK.
- **BAN-CO-015 — Unsubstantiated superlative in title or body.** Banned: "the best", "#1", "leading" or similar claims with no cited substantiation. Defeats: DET-CON-026. Bad: H1 reads "The #1 Project Tool for Teams" with no ranking source anywhere on the site. Instead: state the verifiable fact ("Used by 4,000 teams", with the figure in fact-sheet.md) or drop the claim (CO-029). Severity: WARN.

## Gates

- **G-CO-011 — Metadata lint.** Verifies: CO-023, CO-024. Check: automated CI lint over the route inventory — extract every indexable page's `<title>` and meta description and fail on duplicates, missing values, or placeholder strings: `grep -rhoP '(?<=<title>).*?(?=</title>)' dist/ | sort | uniq -d` returns nothing, and the same for descriptions. Pass: zero duplicates, zero missing, zero defaults. Fail: block shipment. Recorded in: progress.md.
- **G-CO-012 — Intent map coverage.** Verifies: CO-021, CO-028. Check: diff the indexable route inventory against the intent map; every route has exactly one primary intent and every collision has a recorded resolution. Pass: 100% coverage, no unresolved collisions. Fail: block shipment of the unmapped page. Recorded in: progress.md.
- **G-CO-013 — Description-to-page promise check.** Verifies: CO-022, CO-027. Check: manual sample — for each new or changed page, list every offer named in the meta description and point to the page section that delivers it. Pass: every promise located on the page and consistent with fact-sheet.md. Fail: rewrite the description before release. Recorded in: progress.md.
- **G-CO-014 — Heading outline check.** Verifies: CO-025. Check: automated — parse each indexable page and assert exactly one H1 and no skipped heading levels: a DOM query for `h1` returns count 1 per page. Pass: all pages conform. Fail: fix the outline and re-run. Recorded in: progress.md.

## Anti-patterns

- **Outline by keyword list.** Headings read as a keyword checklist rather than the page's argument; catch it by reading only the headings — if they don't summarize the page, rewrite the outline before the body.
- **Metadata written first.** Title and description drafted from the brief, then never revisited after the page changed; catch it by re-reading the finished page against its description at checklist time.
- **Intent drift by accretion.** A page gradually absorbs sections targeting other queries until it competes with three siblings; catch it in the quarterly review when its Search Console queries stop matching its mapped intent.
- **Snippet chasing.** Rewriting titles weekly in reaction to ranking wiggles, so no version is ever measured; catch it by dating every metadata change in the intent map and requiring a measurement window before the next change.

## Examples

- [Example 1 — Title and description rewritten from the finished page](examples/example-1.md) — violates/corrects CO-022, CO-023, CO-024.
- [Example 2 — Two pages, one intent, resolved by differentiation](examples/example-2.md) — violates/corrects CO-021, CO-028.
- [Example 3 — Description promise and superlative removed](examples/example-3.md) — violates/corrects CO-027, CO-029.

## Recall anchors

- One page, one job: one primary intent per indexable page.
- Metadata is written last, from the finished page.
- A title states the topic plainly — stuffing is a spam violation, not a technique.
- If the description promises it, the page must deliver it.
- Colliding intents are merged, redirected, or differentiated in writing.

## Checklist

- [ ] Every indexable page is in the intent map with exactly one primary intent (CO-021).
- [ ] Title and meta description were written or re-checked against the finished page (CO-022).
- [ ] Metadata lint passes: no duplicate, missing, or default titles/descriptions (G-CO-011).
- [ ] Exactly one H1 per page and headings form a real outline (CO-025, G-CO-014).
- [ ] Every offer in each description is delivered on its page and matches fact-sheet.md (CO-027).
- [ ] No unsubstantiated superlatives or unsourced statistics in titles, headings, or body (CO-029).
- [ ] Every intent collision has a written merge, redirect, or differentiation (CO-028).
