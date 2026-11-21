# aeo

## Metadata

- **Owner department:** D9 SEO & Content (CO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://developers.google.com/search/docs/appearance/ai-features ; https://arxiv.org/abs/2311.09735 ; https://www.kevinleary.net/blog/llms-txt-myth/ ; https://www.getdigitize.com/blog/llms-txt-for-brands/ ; https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- **Depends on:** technical-seo, on-page-seo, fact-sheet
- **Feeds into:** geo, copywriting, structured-data, web-analytics

## When to use / Do NOT use

- **Use when:** a page should be liftable by an answer engine — featured snippets, voice answers, Google AI Overviews / AI Mode — or when an AEO plan, tactic, or result is being written, reviewed, or reported.
- **Do NOT use when:** the problem is crawlability or indexation (use technical-seo), page intent and metadata (use on-page-seo), citation inside synthesized multi-source answers as a program (use geo), or markup implementation (use structured-data).

## Rules

1. **CO-041 — Answer first, self-contained.** The passage that answers the query sits at the top of its section and is true and complete when lifted alone: no "as mentioned above", no pronoun whose antecedent lives in another paragraph, no fact that needs the surrounding page to make sense.
2. **CO-042 — Question-shaped headings for question queries.** Where the target query is a question, the heading states that question in the searcher's wording and the answer passage follows it immediately; statements and procedures use descriptive headings instead.
3. **CO-043 — Extractable formats for extractable facts.** Procedural steps go in ordered lists, comparisons in tables, and definitions in a single sentence followed by expansion — formats that survive extraction intact.
4. **CO-044 — One canonical statement of every fact.** A fact used in an answer passage is stated once, in one canonical wording, and matches fact-sheet.md exactly; answer engines amplify contradictions, so a second wording of the same fact anywhere on the site is a defect (DET-CON-015 discipline).
5. **CO-045 — One version of the content.** The same page serves people and engines. No separate "AI version", no answer text hidden from users, no engine-only variant of a passage.
6. **CO-046 — AI-feature eligibility is ordinary Search eligibility (Documented).** For Google AI Overviews and AI Mode, a page must be indexed and eligible to appear in Search with a snippet; Google states there are no additional technical requirements, no special optimizations, and no special schema.org markup. Any plan claiming a further Google requirement must cite the Google page that states it.
7. **CO-047 — Every tactic carries an evidence-level tag.** Each AEO tactic in a plan, audit, or report is labeled Documented (platform-stated), Peer-reviewed (with the study's limits), Correlational (vendor/observational), or Hype (unsupported or contradicted). An untagged tactic fails review.
8. **CO-048 — llms.txt is hygiene, never a result (Hype if claimed otherwise).** llms.txt is a 2024 proposal, not an adopted standard; Google has stated on the record that it does not use the file, and a study of nearly 300,000 domains found no correlation with LLM citation frequency. The file may be shipped, but it is never reported as an AI-visibility win and never described as a Google-endorsed ranking factor.
9. **CO-049 — Crawler access is verified at every layer.** AI and search crawlers allowed in robots.txt must also pass the CDN, firewall, and hosting layer; Google's AI-features guidance names CDN/hosting blocking as a real eligibility failure, so access is tested with the crawler's user agent, not assumed.
10. **CO-050 — Answer-supporting structured data matches the visible text.** Any markup behind an answer (FAQ, HowTo, product facts) is generated from the same data as the rendered page and agrees with it field for field (DET-CON-024).
11. **CO-051 — Citability additions are sourced or absent (Peer-reviewed, limited).** Adding citations, quotations, and statistics is the one tactic with peer-reviewed support for raising visibility in generated answers (Aggarwal et al., KDD '24, GEO-bench, 2023-era models — an upper-bound result, not an average). Every added statistic or quotation must trace to a real source record under the real-content rule; an invented figure is a DET-CON-011 blocker even if it earns citations.
12. **CO-052 — Answer presence is measured on a fixed query set.** A written set of target queries is checked on a monthly cadence in AI Overviews and featured snippets, with date, engine, and citing URL logged. One screenshot of one answer is an anecdote, never a reported result.

## BAN list

- **BAN-CO-021 — llms.txt sold as a ranking factor.** Banned: presenting llms.txt (or any "AI text file") as a Google-endorsed ranking factor, a requirement for AI Overviews, or a measured visibility result. Defeats: DET-NONE — no DET parameter names this signal; governed by CO-048. Bad: client report reads "Implemented llms.txt — expected to improve AI Overview citations." Instead: ship the file as hygiene if wanted and report it as such, tagged Hype/contradicted per CO-048, citing Google's on-record statements. Severity: BLOCK.
- **BAN-CO-022 — Separate or hidden AI-only content.** Banned: an engine-facing version of a page, or answer passages hidden from users (display:none, off-screen, crawler-only rendering) that differ from what users read. Defeats: DET-CON-024. Bad: the crawler receives a keyword-rich FAQ block that never renders for visitors. Instead: one page serves both — write the answer into the visible content (CO-045). Severity: BLOCK.
- **BAN-CO-023 — Fabricated citation bait.** Banned: inventing a statistic, quotation, or study result to make a passage more citable by answer engines. Defeats: DET-CON-011. Bad: "Studies show 87% of teams ship faster with checklists" with no study behind it. Instead: cite a real, producible source or delete the figure (CO-051). Severity: BLOCK.
- **BAN-CO-024 — Templated answer-page matrix.** Banned: stamping out one thin Q&A page per query variant with swapped keywords and no page-specific substance, to capture answer placements at scale. Defeats: DET-CON-025. Bad: 60 pages answering "best X for Y" from one skeleton, differing only in the product name. Instead: one canonical answer page per topic, expanded only with verified page-specific material. Severity: BLOCK.
- **BAN-CO-025 — Contradictory canonical answers.** Banned: two pages (or a page and its markup) stating different values for the same fact an engine might lift — prices, limits, dates, counts. Defeats: DET-CON-015. Bad: the pricing page says "50 GB included" while the FAQ answer says "100 GB included". Instead: state the fact once, from fact-sheet.md, and link rather than restate (CO-044). Severity: WARN.

## Gates

- **G-CO-021 — Evidence-tag audit.** Verifies: CO-047, CO-048. Check: manual review of the AEO plan/report — every tactic line carries one of the four evidence tags, and no llms.txt or "AI file" line is tagged Documented or reported as a result. Pass: 100% of tactics tagged, zero hype presented as fact. Fail: return the plan for re-tagging before any work ships. Recorded in: progress.md.
- **G-CO-022 — Answer-presence log.** Verifies: CO-052. Check: monthly — run the fixed target-query set, record date, surface (AI Overview / featured snippet / none), and the citing URL in the log; compare against the previous month. Pass: log entry complete for every query in the set. Fail: the month's AEO reporting is marked unmeasured, not estimated. Recorded in: progress.md.
- **G-CO-023 — Passage self-containment and fact diff.** Verifies: CO-041, CO-044. Check: automated assist — grep answer sections for cross-reference dependencies: `grep -rniE 'as mentioned above|see above|as noted earlier|the aforementioned' content/` returns nothing; then diff every checkable fact in answer passages against fact-sheet.md. Pass: zero cross-references, zero fact mismatches. Fail: rewrite the passage before release. Recorded in: progress.md.
- **G-CO-024 — Crawler access test.** Verifies: CO-049. Check: automated — request key pages with the search crawler's user agent and assert a 200 with full content: `curl -s -o /dev/null -w "%{http_code}" -A "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" https://example.com/pricing` returns `200`, and robots.txt shows no Disallow for the path. Pass: 200 and no block at CDN, firewall, or robots layer. Fail: fix the blocking layer before claiming AEO eligibility. Recorded in: progress.md.
- **G-CO-025 — Answer markup match.** Verifies: CO-050. Check: automated — parse each page's JSON-LD and diff answer-relevant fields (FAQ answers, prices, ratings) against the rendered text. Pass: every field has an identical visible counterpart. Fail: regenerate the markup from page data or remove it. Recorded in: progress.md.

## Anti-patterns

- **Snippet lottery rewrites.** Rewriting the answer passage after every monthly check, so no version is ever live long enough to measure; catch it by dating passage changes in the log and requiring a full measurement cycle between edits.
- **Answer bloat.** Padding the answer passage with background until the direct answer is no longer liftable; catch it by reading the first two sentences alone — if they don't answer the query, cut.
- **Vendor-metric reporting.** Quoting a tool's "AI visibility score" as if it were a platform metric; catch it at report review — every number must name its source and evidence level (CO-047).
- **Heading stuffing for questions.** Forcing every H2 into question form, including statements and procedures; catch it by checking each question heading against a real query — no query, no question heading (CO-042).

## Examples

- [Example 1 — Answer passage made self-contained](examples/example-1.md) — violates/corrects CO-041, CO-042.
- [Example 2 — llms.txt reported as a win, corrected with evidence tags](examples/example-2.md) — violates/corrects CO-047, CO-048.
- [Example 3 — Citation bait replaced with a sourced statistic](examples/example-3.md) — violates/corrects CO-051.

## Recall anchors

- Answer first, and make the answer stand alone when lifted.
- For Google AI features there is no separate discipline: indexed + snippet-eligible is the whole requirement.
- Tag every tactic: Documented, Peer-reviewed, Correlational, or Hype.
- llms.txt is hygiene, never a result — Google does not use it.
- A fact an engine can lift is stated once, canonically, from the fact sheet.

## Checklist

- [ ] Each target passage answers its query in its first sentences and stands alone when lifted (CO-041, G-CO-023).
- [ ] Question headings match real queries; procedures and comparisons use lists and tables (CO-042, CO-043).
- [ ] Every fact in an answer passage matches fact-sheet.md, stated in one canonical wording (CO-044).
- [ ] No AI-only or hidden content variant exists (CO-045).
- [ ] Every tactic in the plan/report carries an evidence-level tag; llms.txt is not claimed as a result (CO-047, CO-048, G-CO-021).
- [ ] Crawler access verified at robots, CDN, and hosting layers (CO-049, G-CO-024).
- [ ] Answer-supporting structured data matches the visible text field for field (CO-050, G-CO-025).
- [ ] This month's fixed-query answer-presence log is complete (CO-052, G-CO-022).
