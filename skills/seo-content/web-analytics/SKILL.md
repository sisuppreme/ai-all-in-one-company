# web-analytics

## Metadata

- **Owner department:** D9 SEO & Content (CO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Google Analytics developer documentation — https://developers.google.com/analytics ; Google Search Central, "AI features and your website" (measurement section) — https://developers.google.com/search/docs/appearance/ai-features
- **Depends on:** technical-seo, product-analytics (D12 — owner of the shared tracking plan)
- **Feeds into:** content-strategy, on-page-seo, growth-experiments

## When to use / Do NOT use

- **Use when:** search and acquisition measurement is set up, audited, or reported: Search Console verification, coverage and performance review, GA4 organic landing-page analysis, and the content decisions that follow from them. This skill owns the search/acquisition slice of measurement.
- **Do NOT use when:** the question is product behavior inside the app — funnels, feature usage, retention — or the event taxonomy itself: those belong to D12 (product-analytics, event-tracking). **Boundary: one shared tracking plan, two consumers.** D12 owns the plan and the event names; this skill consumes them for search reporting and never invents, renames, or duplicates an event.

## Rules

1. **CO-241 — Search and acquisition only.** This skill measures how search and acquisition channels deliver visitors: Search Console performance (queries, pages, clicks, impressions), coverage/indexing, rich-result reports, and GA4 organic landing-page behavior. Anything past the landing page is D12's slice of the shared plan.
2. **CO-242 — Every production property verified.** Search Console is verified for every production property, including domain variants, and the GA4 property is linked. An unverified property is a blind spot and is treated as a defect with an owner, not an oversight.
3. **CO-243 — The tracking plan is the contract.** Every tag and event this skill relies on is an entry in the shared tracking plan (D12-owned): name, trigger, parameters, owner. A live tag with no plan entry, or a plan entry with no live implementation, is a defect found by the G-CO-121 diff.
4. **CO-244 — Configuration is verified, never assumed.** A pasted snippet proves nothing. Each relied-on event is observed firing — in GA4 DebugView or Tag Assistant — with the plan's exact name and parameters, and the primary conversion is completed end to end in a debug session before anyone reports on it.
5. **CO-245 — Consent is respected end to end.** Where consent mode applies, analytics does not collect before the visitor's consent state allows it, and the consent configuration is verified in a fresh, no-consent session — not inferred from the banner being visible on the page.
6. **CO-246 — Fixed review cadence.** Search Console coverage and performance are reviewed monthly at minimum, and the review is logged with the actions it produced. A review that produces no briefs, refreshes, retirements, or technical fixes — and says why — is an incomplete review.
7. **CO-247 — No content decision without a citation.** Every brief, refresh, and retirement this skill informs names the query, page, or landing-page evidence behind it. "We should write about X" with no Search Console or GA4 evidence cited does not enter content-strategy's queue.
8. **CO-248 — AI-feature traffic is read where Google reports it.** Appearances in Google's AI features are reported inside Search Console's overall Performance data. They are never split out, estimated, or presented as a separate metric — no platform publishes such a number, so any standalone "AI traffic" figure is invented.
9. **CO-249 — Every reported figure reproduces from source.** Each number in a report names its platform, property, report, date range, and filters, and can be re-pulled to the same value. A figure nobody can reproduce is cut from the report, not footnoted.
10. **CO-250 — Event and tag changes go through the plan.** Changes are proposed into the shared tracking plan, keep D12's names consistent, and are debug-validated before release. No duplicate or variant spellings of an existing event are ever shipped (BAN-CO-124).
11. **CO-251 — Indexing regressions are incidents.** A spike in excluded or error URLs, or a sudden drop in indexed pages, is triaged to a named cause with an owner and a fix or an accepted-risk note — never left as an observation on a chart.
12. **CO-252 — Reports are dated and current.** Every report states its pull date, date range, and comparison convention, and its figures come from that pull. A recycled screenshot or a figure from a previous period presented as current is stale copy (BAN-CO-125).

## BAN list

- **BAN-CO-121 — Invented metrics reported as measured.** Banned: presenting any metric no platform produces — a standalone "AI Overview traffic" number, a paid "GEO score" shown as a platform metric, an estimated citation share — as measured fact in a plan or report. Defeats: DET-CON-011. Bad: the monthly report carries a line "AI Overview visits: 1,240 (+18%)" that appears in no Search Console or GA4 report and cannot be re-pulled. Instead: report AI-feature appearances only inside overall Performance data (CO-248); label anything else with its evidence level or cut it. Severity: BLOCK.
- **BAN-CO-122 — Measurement claimed, never configured.** Banned: announcing that analytics or conversion tracking is "set up" when the snippet is pasted but no tracking-plan entry exists and no debug session has ever verified an event firing. Defeats: DET-CON-028. Bad: the launch checklist marks "analytics done"; three months later the team discovers the signup conversion was never marked and DebugView shows no events at all. Instead: no measurement claim until the G-CO-121 plan diff is clean and a G-CO-122 debug session has completed the primary conversion. Severity: BLOCK.
- **BAN-CO-123 — Consent promise without the configuration.** Banned: privacy or consent copy stating that tracking starts only after consent, while tags fire on page load regardless of consent state. Defeats: DET-CON-015. Bad: the cookie policy says "we track only with your permission," but a fresh no-consent session fires the full GA4 event stream. Instead: make the firing match the promise — consent state gates collection (CO-245) and the fresh-session check in G-CO-122 proves it. Severity: BLOCK.
- **BAN-CO-124 — Duplicate and misspelled event variants.** Banned: shipping variant spellings of one event (`sign_up`, `signup`, `SignUp`) so a single action fragments across several report rows. Defeats: DET-CON-017. Bad: the signup conversion is split across three event names, each showing a third of the real total, and the team debates which is "the" number. Instead: one canonical name from the shared tracking plan (CO-250); variants are removed and the change is debug-validated before release. Severity: BLOCK.
- **BAN-CO-125 — Stale figures presented as current.** Banned: reusing a previous period's screenshot, export, or headline number in a current report, including after the underlying tag has broken. Defeats: DET-CON-018. Bad: this month's report reuses last month's traffic chart while the GA4 tag has been missing from the redesigned template for two weeks. Instead: every report is built from a fresh, dated pull (CO-252), and a broken tag is a CO-251 incident, not a quiet gap. Severity: WARN.

## Gates

- **G-CO-121 — Tracking-plan diff.** Verifies: CO-243, CO-250. Check: automated — export the live tag/event list (GTM container export or a crawl grep for measurement IDs, e.g. `grep -rhoE "G-[A-Z0-9]{6,}" dist/ | sort -u`, plus the implemented event names) and diff it against the shared tracking plan's entries. Pass: zero live tags or events missing from the plan, and zero plan entries with no live implementation. Fail: block the release until the diff is clean. Recorded in: progress.md.
- **G-CO-122 — DebugView conversion and consent session.** Verifies: CO-244, CO-245. Check: manual with tooling — in a fresh browser profile, load the site with no consent given and confirm no analytics collection beyond consent-state pings; then grant consent, complete the primary conversion flow, and watch GA4 DebugView. Pass: the conversion event fires exactly once, under its plan name with its plan parameters, and nothing collected before consent. Fail: block; fix configuration and re-run. Recorded in: progress.md.
- **G-CO-123 — Monthly Search Console review.** Verifies: CO-242, CO-246, CO-251. Check: manual — the review log holds an entry for the current month covering every verified property: coverage counts, performance summary, each exclusion or error spike triaged to a named cause and owner, and the actions the review produced. Pass: entry complete for the current month. Fail: the review is overdue; complete it before the next release. Recorded in: progress.md.
- **G-CO-124 — Report reproducibility audit.** Verifies: CO-247, CO-248, CO-249, CO-252. Check: semi-automated — list every figure in the latest report; each must cite platform, property, report, and date range; re-pull a sample of at least two figures and compare values; scan the report for any standalone AI-feature metric. Pass: every sampled figure reproduces exactly and no invented metric appears. Fail: withdraw and reissue the report. Recorded in: progress.md.

## Anti-patterns

- **Dashboard theater.** A polished dashboard exists, so the team feels measured — but no review ever opens it and no decision ever cites it. Catch it: if this month's G-CO-123 log entry is missing, the dashboard is decoration.
- **Vanity slicing.** The review leads with whichever number rose — impressions up — while organic landing-page conversions fell, unmentioned. Catch it: every review opens with coverage health and the primary conversion, in that order; growth metrics come second.
- **Two sources of truth, averaged.** Search Console and GA4 disagree (they measure different things), so someone blends them into one comfortable number. Catch it: each metric has exactly one named source platform under CO-249; a discrepancy gets an explanation of the definitions, never an average.
- **The drifting comparison.** Comparison periods quietly change month to month — vs. last month, vs. last quarter, vs. launch — so the trend always flatters. Catch it: the comparison convention is fixed in the tracking plan; changing it is a noted plan amendment, not an editorial choice.

## Examples

- [Example 1 — The "AI traffic" line nobody could reproduce](examples/example-1.md) — corrects CO-248.
- [Example 2 — The snippet that measured nothing](examples/example-2.md) — corrects CO-244.
- [Example 3 — Three names for one signup](examples/example-3.md) — corrects CO-250.

## Recall anchors

- Search and acquisition here; product events are D12's — one plan, two consumers.
- Snippet present is not configured. DebugView, or it didn't happen.
- No content decision without a citation.
- AI appearances live inside overall Performance data — never invent the split.
- A figure nobody can reproduce is a figure you cut.

## Checklist

- [ ] Search Console verified for every production property and domain variant (CO-242).
- [ ] Tracking-plan diff is clean: no live tag or event missing from the plan (G-CO-121).
- [ ] DebugView session completed the primary conversion exactly once, under its plan name (G-CO-122).
- [ ] Fresh no-consent session collects nothing before consent (CO-245).
- [ ] This month's Search Console coverage and performance review is logged, spikes triaged (G-CO-123).
- [ ] Every figure in the latest report reproduces from its cited source (G-CO-124).
- [ ] No standalone "AI traffic" or other invented metric appears in any report (CO-248).
