# content-strategy

## Metadata

- **Owner department:** D9 SEO & Content (CO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Mailchimp, content planning guide — https://mailchimp.com/resources/content-planning/ ; Google Search spam policies (scaled content abuse) — https://developers.google.com/search/docs/essentials/spam-policies ; Google Search Central, "Creating helpful, reliable, people-first content" — https://developers.google.com/search/docs/fundamentals/creating-helpful-content ; Google Search Central Blog, "Google Search's guidance about AI-generated content" — https://developers.google.com/search/blog/2023/02/google-search-and-ai-content
- **Depends on:** fact-sheet, web-analytics
- **Feeds into:** copywriting, on-page-seo, real-content, internal-linking

## When to use / Do NOT use

- **Use when:** deciding what content a site will produce, in what order, for whom, and to what end — topic maps, editorial calendars, briefs, and refresh/retire decisions. This skill owns the production system: strategy sets audience, goals, and topic ownership before any drafting starts.
- **Do NOT use when:** the question is how a single page is written (copywriting), how its metadata is set (on-page-seo), or whether a specific factual element is evidenced (real-content — that gate runs at publish time and its blocker list outranks any plan made here). Never use strategy to justify volume the evidence cannot support.

## Rules

1. **CO-081 — No brief, no draft.** Every piece of content starts from a brief naming its audience, goal, target query or intent, owner, and reviewer. A brief missing any of the five does not enter production, and no draft is written against an unwritten brief.
2. **CO-082 — Volume is an output, never a quota.** The plan never sets a pages-per-week or pages-per-month target. Output is whatever number of briefs clear the CO-081 bar; Google's scaled content abuse policy makes volume-for-rankings the violation regardless of whether humans or AI wrote the pages.
3. **CO-083 — One canonical page per topic.** The topic map assigns each topic to exactly one canonical page. A second page on the same topic is admitted only with a written differentiation: a different audience, format, or body of page-specific verified material the canonical page does not carry.
4. **CO-084 — The swap test for variants.** A location, keyword, or product variant page ships only with real page-specific data (staff, stock, pricing, regulations, local facts) such that swapping the keyword back would break the page. If two variants stay interchangeable after the swap, they are one page, not two.
5. **CO-085 — Every piece carries an owner and a review-by date.** At publication, each page records a named owner and the date by which its claims are re-verified. A page with no owner or no review-by date is not finished, however polished the copy.
6. **CO-086 — Authorship is real.** Pieces are credited to real people the publisher can evidence, or to an accountable house byline ("The Support Team"). Invented author personas — names, headshots, bios for people who do not exist — are never planned, briefed, or published.
7. **CO-087 — Decisions cite data.** Every brief, refresh, and retirement names the evidence behind it: Search Console query/page data, analytics landing-page evidence, or a documented audience need. "We should write about X" with no cited evidence is an opinion, and opinions do not enter the calendar.
8. **CO-088 — Topics stay inside the real offer.** The topic map covers only subjects the business can actually serve and evidence from its own operation. A topic the business has no product, service, data, or experience behind is out of scope, however much search demand it shows.
9. **CO-089 — Refresh or retire on schedule.** When a page's review-by date arrives, its owner re-verifies its claims and then refreshes, retires, or re-dates it with the verification recorded. Silently editing the date without re-verifying the content is not a refresh.
10. **CO-090 — The programmatic admission bar.** Templated or programmatic page sets are admitted only when every page in the set carries page-specific verified data passing CO-084. A set whose pages differ only in a swapped term is rejected at planning, not discovered at audit.
11. **CO-091 — Distribution is part of the brief.** A brief is incomplete until it names the page's planned inbound internal links and its distribution step (newsletter, social, partner, in-product). A page planned to be found "by the sitemap" is planned to be orphaned.
12. **CO-092 — Depth per topic over page count.** When a topic cannot support another substantively different page, the plan deepens the canonical page — new verified data, better coverage of the intent — instead of spawning a sibling. The plan records this choice so the refusal of volume is a decision on file, not an omission.

## BAN list

- **BAN-CO-041 — Volume-quota planning.** Banned: setting a content target in pages per week/month, or back-filling a calendar to hit a count. Defeats: DET-CON-025. Bad: the Q3 plan commits to "120 location pages in 6 weeks" before anyone asks what each page would say. Instead: plan briefs that clear CO-081 and let the count be whatever survives; depth per topic (CO-092) absorbs the remaining effort. Severity: BLOCK.
- **BAN-CO-042 — Template-stamped page sets.** Banned: approving a set of pages built from one skeleton with keywords swapped per page. Defeats: DET-CON-008. Bad: forty "Best plumber in {city}" pages share identical headings and paragraph order; only the city name and a stock photo change. Instead: admit only variants carrying real local data that passes the swap test (CO-084); merge the rest into one canonical page (CO-083). Severity: BLOCK.
- **BAN-CO-043 — Invented author personas.** Banned: creating fictional writers — name, headshot, bio, credentials — to make the content program look staffed. Defeats: DET-CON-020. Bad: the plan launches "Meet our experts" with three generated portraits and invented job histories. Instead: credit real people with an author page and an independent trace, or use an honestly collective house byline (CO-086). Severity: BLOCK.
- **BAN-CO-044 — Expired claims left live by default.** Banned: letting dated copy (sale banners, "new for 2024", registration for past events) stay published past its date with no owner action. Defeats: DET-CON-018. Bad: the spring sale banner is still on the homepage in November because no page owned its expiry. Instead: every dated claim carries an owner and review-by date (CO-085) and is refreshed or retired on schedule (CO-089). Severity: WARN.

## Gates

- **G-CO-041 — Brief traceability audit.** Verifies: CO-081, CO-087. Check: automated — diff the published URL inventory against the brief register; every published URL must map to a brief containing audience, goal, intent, owner, reviewer, and a cited evidence source. Pass: 100% of published URLs trace to a complete brief. Fail: unbriefed pages are pulled from the calendar owner's queue and briefed retroactively or unpublished. Recorded in: progress.md.
- **G-CO-042 — Corpus similarity clustering.** Verifies: CO-083, CO-084, CO-090. Check: automated — cluster published pages by text similarity; for every cluster of more than three pages, apply the swap test to a sample pair. Pass: no cluster whose sampled pages are interchangeable after keyword swap. Fail: the set is merged to its canonical page or each page is rebuilt with verified page-specific data before the next release. Recorded in: progress.md.
- **G-CO-043 — Stale-date and review-by scan.** Verifies: CO-085, CO-089. Check: automated — extract date-bearing claims from published copy and diff the page inventory against the review-by register; flag any page past its review-by date and any claim asserting a past event as current. Pass: zero overdue pages and zero expired claims live. Fail: flagged pages are refreshed, retired, or re-dated with verification recorded before the next publish. Recorded in: progress.md.
- **G-CO-044 — Authorship audit.** Verifies: CO-086. Check: manual — list every byline on the site; for each individual byline, require an author page plus one independent trace (staff page, professional profile); house bylines must name an accountable team, not a fake individual. Pass: every byline resolves to a real person or an honest collective. Fail: block publication under that byline until it does. Recorded in: progress.md.

## Anti-patterns

- **The self-filling calendar.** An editorial calendar padded weeks ahead with topics nobody has briefed, so the schedule looks productive while every slot is an IOU. Catch it: pick any future slot at random — if no brief exists behind it, the calendar is decoration (CO-081).
- **Topic sprawl.** Chasing every adjacent query the keyword tool surfaces until the site publishes on subjects the business cannot serve or evidence. Catch it: for each new topic, ask "what do we operate, sell, or measure that makes us the source for this?" — no answer, no topic (CO-088).
- **Refresh theater.** Bumping a page's date, reordering paragraphs, and calling it a refresh while every claim stays unverified. Catch it: a refresh note that lists no claim re-checked against its source is a date edit, not a review (CO-089).
- **The deck-only strategy.** The plan lives in a slide deck that is never diffed against what actually shipped, so production quietly drifts into whatever was easiest to generate. Catch it: if the last brief traceability audit (G-CO-041) is older than the last publish, the strategy is not governing anything.

## Examples

- [Example 1 — The 200-city page matrix](examples/example-1.md) — corrects CO-084.
- [Example 2 — The article nobody briefed](examples/example-2.md) — corrects CO-081.
- [Example 3 — The evergreen page selling last spring's sale](examples/example-3.md) — corrects CO-085.

## Recall anchors

- No brief, no draft.
- Volume is an output, never a quota.
- One canonical page per topic; variants must survive the swap test.
- Every page: a real author, a named owner, a review-by date.
- Deepen the canonical page before spawning a sibling.

## Checklist

- [ ] Every item in production traces to a brief with audience, goal, intent, owner, and reviewer (G-CO-041).
- [ ] The plan states no pages-per-week or pages-per-month target anywhere (CO-082).
- [ ] Each topic maps to one canonical page; variants carry a written differentiation (CO-083).
- [ ] Every variant page passes the swap test with real page-specific data (CO-084).
- [ ] Every published page has a named owner and a review-by date (CO-085).
- [ ] All bylines are real people or an accountable house byline (G-CO-044).
- [ ] Each brief, refresh, and retirement cites the data behind it (CO-087).
- [ ] Similarity clustering shows no interchangeable page set (G-CO-042).
