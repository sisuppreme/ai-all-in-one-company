# copywriting

## Metadata

- **Owner department:** D9 SEO & Content (CO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://developers.google.com/search/docs/fundamentals/creating-helpful-content ; https://developers.google.com/search/docs/essentials/spam-policies ; skills/detection/content/PARAMETERS.md (DET-CON-006, 007, 009, 010, 011, 017, 026, 027, 028)
- **Depends on:** fact-sheet, real-content
- **Feeds into:** on-page-seo, lifecycle-email, social-open-graph, structured-data

## When to use / Do NOT use

- **Use when:** Writing or editing any user-facing copy — landing pages, product pages, blog posts, metadata, alt text, captions, email and ad copy.
- **Do NOT use when:** The task is verifying whether a factual element may exist at all (that is real-content's gate; copywriting consumes its verdicts), setting topic inventory (content-strategy), or writing documentation (D10 owns documentation-writing; the voice guide is shared, not duplicated).

## Rules

1. **CO-101 — Competitor-verbatim test.** Every benefit sentence must name a mechanism, a user, or a verifiable outcome specific to this product. If a competitor could print the sentence unchanged, rewrite it with a product-specific fact from fact-sheet.md or delete it. (DET-CON-006)
2. **CO-102 — Fact-sheet traceability.** Every factual claim in copy — feature, number, price, name, outcome — traces to an entry in fact-sheet.md or a source record the business can produce. A claim with no trace is cut, never softened into vagueness.
3. **CO-103 — Cluster-term editing pass.** Before shipping, search the draft for model-default vocabulary clusters (delve, tapestry, realm, furthermore, moreover, "it's important to note", "in today's fast-paced world") and rewrite each hit in the house voice. Co-occurrence of several cluster terms on one page is a defect, not a style choice. (DET-CON-007)
4. **CO-104 — One qualifier maximum.** A product claim carries at most one honest qualifier. Three or more qualifiers stacked on one claim ("may potentially help to possibly improve") mean the claim is unverified: verify it and state it plainly, or cut it. (DET-CON-009)
5. **CO-105 — Measurable superlatives need substantiation.** "#1", "best-rated", "largest", and any rank, share, or rated-position claim require substantiation on file (ranking, survey, or criteria) before use; without it, rewrite as plain description. Unmeasurable puffery is a style note, not a finding. (DET-CON-026)
6. **CO-106 — No invented numbers.** Every statistic, percentage, rating, and count in copy cites its source or dataset, and one canonical figure is used site-wide. Third-party claims (ratings, market share, comparisons) need provenance somewhere on the domain; first-party counters need a fact-sheet entry. (DET-CON-011)
7. **CO-107 — No invented social proof.** Testimonials, review quotes, and endorsements are used only when a producible source record exists (signed quote, review-platform link, customer email) and permission is held. No record, no quote — the section ships empty or not at all. (DET-CON-010)
8. **CO-108 — Naming list is exact.** Company, product, feature, plan, and people names are copied from the project's naming list character-for-character — capitalization, spacing, and spelling — on every surface. Never re-type a name from memory. (DET-CON-017)
9. **CO-109 — Alt text from the rendered image.** Alt text and captions describe the actual rendered image: what a sighted reader sees. Never write them from the filename, a keyword list, or the prompt that generated the image. Decorative images get `alt=""`, not a description. (DET-CON-027)
10. **CO-110 — Structure follows the material.** Page structure — headings, paragraph order, length — varies with the subject. Never stamp one skeleton across pages with only keywords swapped; if two drafts share a heading sequence, rewrite one from its own brief. (DET-CON-008)
11. **CO-111 — Promises need backing.** A present-tense operational promise ("24/7 support", "money-back guarantee", "cancel anytime") appears in copy only when the policy page or documented process that makes it true exists and is linked. No backing artifact, no promise. (DET-CON-028)
12. **CO-112 — People-first, metadata last.** Copy is written to help the named reader complete a task, in the house voice guide's register; titles and descriptions are written after the page is finished, from what the page actually delivers. (Google people-first guidance)

## BAN list

- **BAN-CO-051 — Invented testimonial.** Banned: a quoted endorsement from a person whose source record the business cannot produce. Defeats: DET-CON-010. Bad: "TaskBoard cut our planning time in half." — Sarah M., Marketing Manager (no such customer). Instead: use only a quote with a signed or platform-verifiable source record and permission, or ship the section without testimonials. Severity: BLOCK.
- **BAN-CO-052 — Unsourced statistic.** Banned: a precise figure (percentage, rating, user count, comparison) with no source, dataset, or fact-sheet entry behind it. Defeats: DET-CON-011. Bad: "Teams ship 87% faster with TaskBoard." Instead: cite the dataset the figure came from and record it in fact-sheet.md, or delete the number and describe the mechanism. Severity: BLOCK.
- **BAN-CO-053 — Unsubstantiated measurable superlative.** Banned: a rank or rated-position claim ("#1", "best-rated", "the leading provider") with no ranking, survey, or criteria on file. Defeats: DET-CON-026. Bad: "The #1 project tool for remote teams." Instead: name the comparison set and source ("Top-rated in the 2026 Remote Work Tools survey, n=412"), or write a plain description of what the product does. Severity: BLOCK.
- **BAN-CO-054 — Competitor-verbatim benefit filler.** Banned: a benefit sentence any competitor could print unchanged, with no product-specific fact attached. Defeats: DET-CON-006. Bad: "Unlock the power of seamless collaboration and take your team to the next level." Instead: name the mechanism and outcome — "Comments resolve into tasks with one click, so decisions stop getting lost in threads." Severity: WARN.
- **BAN-CO-055 — Hedge stack.** Banned: three or more qualifiers protecting a single product claim. Defeats: DET-CON-009. Bad: "TaskBoard may potentially help your team to possibly improve how it might track work." Instead: verify and commit — "TaskBoard tracks every task's owner and due date in one board" — or cut the claim. Severity: WARN.

## Gates

- **G-CO-051 — Pre-publish lint (automated).** Verifies: CO-103, CO-104. Check: run `grep -rniE "delve|tapestry|realm|furthermore|moreover|it's important to note|in today's fast-paced world" <copy files>` and a qualifier-cluster scan for `may|might|can` within five words of `potentially|possibly|generally`; every hit is listed for the editor. Pass: zero unrewritten hits. Fail: block shipment until the editor rewrites or justifies each hit in progress.md. Recorded in: progress.md.
- **G-CO-052 — Substantiation spot-check (manual).** Verifies: CO-102, CO-105, CO-106, CO-107. Check: list every measurable claim, statistic, superlative, and testimonial in the piece; trace each to its fact-sheet entry or source record. Pass: 100% traced. Fail: block shipment; untraced items are cut, not footnoted. Recorded in: progress.md.
- **G-CO-053 — Naming lint (automated).** Verifies: CO-108. Check: extract proper nouns from the copy and diff against the naming list; flag every variant form of a listed entity. Pass: exactly one live form per entity. Fail: block shipment until variants are corrected. Recorded in: progress.md.
- **G-CO-054 — Competitor-verbatim review (manual).** Verifies: CO-101, CO-110. Check: highlight every benefit sentence and ask "could a competitor print this verbatim?"; on interior pages flag any yes with no specific within one sentence either side, on heroes judge the page as a whole; compare heading sequences against two sibling pages. Pass: no flagged sentence survives and no shared skeleton. Fail: warn and rewrite before publish. Recorded in: progress.md.

## Anti-patterns

- **Category-first drafting.** Opening a blank page and writing what "tools like this" say, then bolting the product name on. Catch it: if the draft was finished before fact-sheet.md was opened, restart from the fact sheet.
- **Synonym laundering.** Swapping generic words for fancier synonyms ("use" → "leverage" → "utilize") to fake specificity. Catch it: the sentence still names no mechanism after the swap — rewrite for fact, not vocabulary.
- **Padding instead of cutting.** When a page feels thin, adding paragraphs of altitude copy rather than one verified fact or a shorter page. Catch it: word count grew while the fact count stayed flat.
- **Register whiplash.** Hero in house voice, body in model-default register, because sections were drafted in separate sessions without the voice guide loaded. Catch it: read the page aloud end to end; a tone shift marks the unedited section.

## Examples

- [Example 1 — Benefit filler rewritten with a mechanism](examples/example-1.md) — violates/corrects CO-101.
- [Example 2 — Hedge stack and cluster terms edited to a plain claim](examples/example-2.md) — violates/corrects CO-103, CO-104.
- [Example 3 — Superlative and statistic cut to substantiated copy](examples/example-3.md) — violates/corrects CO-105, CO-106.

## Recall anchors

- If a competitor could print it, rewrite it or cut it.
- No trace in the fact sheet, no claim on the page.
- Three qualifiers means unverified: commit or cut.
- Names are copied, never re-typed.
- Alt text describes the image you can see, not the file you named.

## Checklist

- [ ] Every benefit sentence passes the competitor-verbatim test (CO-101).
- [ ] Every factual claim traces to fact-sheet.md or a source record (CO-102).
- [ ] Cluster-term and hedge lint run; all hits rewritten (CO-103, CO-104, G-CO-051).
- [ ] Every superlative and statistic has substantiation on file (CO-105, CO-106, G-CO-052).
- [ ] Every testimonial has a producible source record and permission (CO-107).
- [ ] All names match the naming list exactly (CO-108, G-CO-053).
- [ ] Alt text and captions written from the rendered images (CO-109).
- [ ] Every operational promise links to its backing policy or process (CO-111).
