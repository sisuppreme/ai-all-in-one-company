# real-content

## Metadata

- **Owner department:** D9 SEO & Content (CO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://www.jdsupra.com/legalnews/a-guide-to-understanding-ftc-s-4503495/ ; skills/detection/content/PARAMETERS.md (DET-CON-010…016, 019, 020, 028)
- **Depends on:** fact-sheet (D1)
- **Feeds into:** copywriting, structured-data, content-strategy, growth-experiments

## When to use / Do NOT use

- **Use when:** Any page, post, email, metadata set, or JSON-LD block is about to publish and contains a factual element — a testimonial, review, statistic, credential, person, price, promise, or byline. This skill is the pre-publish enforcement pass for the Real Content Rule (QB-10).
- **Do NOT use when:** Drafting copy from scratch (use copywriting, then run this pass on the result), deciding whether a claim is legal in a specific jurisdiction (route to D14 legal-privacy — this skill blocks, it does not give legal advice), or checking code-level fake functionality (use D8 placeholder-scan and the DET-FAKE parameters).

## Rules

1. **CO-121 — Classify before you publish.** Before publication, list every factual element in the piece and classify it: testimonial, review, statistic, credential, person, price, promise, or authorship. Each element is matched to its evidence — a source record the business can produce, a fact-sheet.md entry, or the live data the page renders from. An element with no match does not ship.
2. **CO-122 — The blocker list is absolute.** A fabricated testimonial (DET-CON-010), review set (DET-CON-013), third-party statistic (DET-CON-011), credential or press claim (DET-CON-012), or person (DET-CON-019) fails the entire content pass. There is no "mostly real" grade and no averaging against the elements that check out.
3. **CO-123 — First-party counters are not exempt.** A self-attested usage counter ("84 million accounts") needs a fact-sheet.md entry recording its source system and as-of date, and the same figure must appear everywhere it is used (DET-CON-011 check (b), DET-CON-015). A counter contradicted by another page is a fail; a consistent counter with no fact-sheet entry is a gap to close before publish, not a pass.
4. **CO-124 — Prices come from one source.** Every price, plan name, and billing term renders from the single pricing data source and is verified against a test checkout total before publish. A marketing page may never carry a price the checkout contradicts (DET-CON-016). Promotions carry visible dates and terms.
5. **CO-125 — No backing artifact, no promise.** Every operational promise — support hours, response times, guarantees, refund and cancellation terms — links to the policy page or documented process that makes it true (DET-CON-028). If the backing artifact does not exist, the promise is removed, not reworded.
6. **CO-126 — Bylines name real people or an honest house byline.** An individual byline requires an author page plus one independent trace (staff page, professional profile). Genuinely collective content may use an accountable team byline ("The Support Team"). An invented individual is never acceptable (DET-CON-020).
7. **CO-127 — Cut, don't soften.** An element with no evidence is deleted. It is never rescued with hedges ("up to", "as much as", "customers love us"), moved to a less prominent slot, or kept "until we get the real one." Placeholder social proof is fabrication with a deadline.
8. **CO-128 — Metadata and structured data pass the same gate.** Titles, meta descriptions, OG tags, and JSON-LD fields are factual elements under CO-121. Every JSON-LD rating, price, date, and author has a visible counterpart with an identical value, or a fact-sheet entry (DET-CON-024). Review markup exists only where real, visible reviews exist.
9. **CO-129 — A named human verifies the facts.** AI may draft and assemble evidence, but a named person checks each classified element against its source and records their name and the date in progress.md before publish. "The model wrote it" is not a verification step.
10. **CO-130 — Dated claims have owners and expiry.** Every date-bearing claim (sale end, event date, "new for <year>") carries an owner and a review-by date. Expired promotions and past events presented as current are removed or reframed as archive at the review date (DET-CON-018).
11. **CO-131 — Team imagery is real or absent.** Portraits captioned with employee names and roles are photographs of those people. Where no real photo exists, the page runs without a portrait — never a stock image or generated face in its place (DET-CON-019).
12. **CO-132 — Block and route legal questions; never improvise them.** Superlatives, guarantees, review displays, and testimonial use can be advertising-law questions. This skill blocks the element and routes the question to D14; it never clears a claim by arguing the law itself.

## BAN list

- **BAN-CO-061 — Invented testimonial.** Banned: a quoted endorsement from a person whose quote the business cannot produce as a source record. Defeats: DET-CON-010. Bad: "TaskBoard cut our planning time in half." — Sarah M., Marketing Manager, with no customer, email, or review behind it. Instead: publish only quotes held as source records (email, platform review, signed quote) with permission, or ship the section with no testimonial. Severity: BLOCK.
- **BAN-CO-062 — Unsourced third-party statistic.** Banned: a rating, market, benchmark, or comparison figure with no provenance anywhere on the domain or on file. Defeats: DET-CON-011. Bad: "Rated 4.9/5 — the fastest-growing tool in its category" with no review platform, survey, or dataset behind either number. Instead: cite the dataset or platform the figure came from, or delete the figure and describe the product plainly. Severity: BLOCK.
- **BAN-CO-063 — Substitute people.** Banned: a stock photograph or generated portrait captioned as a named employee, founder, or customer. Defeats: DET-CON-019. Bad: a stock headshot labeled "Amara Osei, Head of Support" on the About page. Instead: use a real photograph of the named person, or publish the name and role with no portrait. Severity: BLOCK.
- **BAN-CO-064 — Unbacked promise.** Banned: a present-tense operational promise with no policy or process behind it. Defeats: DET-CON-028. Bad: "24/7 support and a 30-day money-back guarantee" on the pricing page when support is email-only on weekdays and no refund policy exists. Instead: link the promise to the policy or documented process that honors it, or remove the promise and state the actual terms. Severity: BLOCK.
- **BAN-CO-065 — Seed people presented as real users.** Banned: demo, seed, or sample accounts, reviews, or activity shipped in production copy as real customers or demand. Defeats: DET-FAKE-014. Bad: the launch homepage shows a "recent signups" feed populated from the development seed data. Instead: exclude seed data from production surfaces entirely; social proof comes only from real, attributable users. Severity: BLOCK.

## Gates

- **G-CO-061 — Claim-trace audit.** Verifies: CO-121, CO-123, CO-124. Check: run `python3 scripts/claim-trace.py --pages dist/ --fact-sheet fact-sheet.md` — the script extracts checkable facts (numbers, prices, dates, names) from the rendered pages and diffs them against fact-sheet.md, exiting non-zero on any unmatched or contradicted fact. Pass: exit code 0; every extracted fact traces to a fact-sheet entry. Fail: block publication; fix the copy or the stale fact-sheet side and record which was corrected. Recorded in: progress.md.
- **G-CO-062 — DET-CON pre-publish scan.** Verifies: CO-122, CO-127, CO-128, CO-130. Check: run the DET-CON-001…028 checks over the rendered pages, metadata, and JSON-LD; the automatable subset runs as `python3 scripts/det-con-scan.py --pages dist/` (placeholder strings, template tokens, date extraction, JSON-LD-vs-page field diff), and the remaining parameters (010–013, 019, 020, 028) are worked as a manual checklist against the evidence register. Pass: zero blocker hits and zero unaddressed major hits. Fail: block publication — one fabricated element fails the whole pass. Recorded in: progress.md.
- **G-CO-063 — Evidence register completeness.** Verifies: CO-121, CO-122, CO-126. Check: for every testimonial, review, statistic, credential, and byline in the piece, the evidence register holds a source-record reference (file path, platform URL, or fact-sheet line). Run `grep -c "source:" evidence-register.md` and compare the count against the classified element list from CO-121; then open two records at random and confirm each actually contains the claim it is cited for. Pass: counts match and both spot-checks support their claims. Fail: block publication; the unsupported element is cut under CO-127. Recorded in: progress.md.
- **G-CO-064 — Named human verification.** Verifies: CO-129. Check: progress.md contains the verifier's name, the date, and the list of pages passed, entered before the publish timestamp. **Human-required:** the verifier is by definition a named human; no automated or agent-produced substitute satisfies this gate, and autonomous publication is blocked until the human entry exists. Single-agent disposition: the agent prepares the verification packet — the page list plus the G-CO-061 claim-trace and G-CO-063 evidence-register results — records this gate as human-required in progress.md, and stops at the publication step; the packet and the recorded gate state are the agent's complete deliverable for this gate. Pass: entry present and complete. Fail: block publication until a named human has done the check — an automated pass alone never satisfies this gate. Recorded in: progress.md.

## Anti-patterns

- **Hedge laundering.** An invented number kept alive as "up to 87% faster" or "teams save hours every week." The hedge changes the grammar, not the evidence; catch it by asking for the source record exactly as you would for the unhedged claim.
- **Evidence theater.** A citation that exists but does not contain the claim — a link to a homepage offered as proof of a rating, a study cited for a figure it never reports. Catch it by opening every cited source and finding the number on the page, which G-CO-063's spot-check samples.
- **Screenshot proof.** Accepting a screenshot of a review, dashboard, or inbox as a source record. Screenshots are producible by anyone in minutes; require the record itself — the platform URL, the exported file, the fact-sheet entry.
- **Body-only verification.** The visible copy passes, so the title tag, OG card, and JSON-LD ship unchecked — where the fabricated rating or stale price actually lives. Catch it by running G-CO-062 over metadata and markup, not just body text.

## Examples

- [Example 1 — The testimonial with no customer](examples/example-1.md) — violates/corrects CO-122 and BAN-CO-061.
- [Example 2 — The counter that disagreed with itself](examples/example-2.md) — violates/corrects CO-123.
- [Example 3 — The promise with nothing behind it](examples/example-3.md) — violates/corrects CO-125 and BAN-CO-064.

## Recall anchors

- No evidence, no element — cut it, don't soften it.
- One fabricated item fails the whole pass.
- First-party numbers need a fact-sheet entry too.
- No backing policy, no promise.
- Metadata and JSON-LD are claims, and they get checked like claims.

## Checklist

- [ ] Every factual element is classified and matched to evidence (CO-121).
- [ ] Zero blocker-list fabrications: testimonials, reviews, statistics, credentials, people (CO-122).
- [ ] Every first-party counter has a fact-sheet entry and agrees site-wide (CO-123).
- [ ] Every price matches the pricing source and a test checkout total (CO-124).
- [ ] Every operational promise links to its backing policy or process (CO-125).
- [ ] Every byline is a real, traceable person or an honest house byline (CO-126).
- [ ] Claim-trace audit (G-CO-061) and DET-CON scan (G-CO-062) both pass.
- [ ] A named human has verified the facts and signed progress.md (CO-129, G-CO-064).
