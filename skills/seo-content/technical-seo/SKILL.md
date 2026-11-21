# technical-seo

## Metadata

- **Owner department:** D9 SEO & Content (CO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Google Search Central, SEO guide for developers — https://developers.google.com/search/docs/fundamentals/get-started-developers ; RFC 9309, Robots Exclusion Protocol — https://www.rfc-editor.org/rfc/rfc9309.html ; Google Search spam policies — https://developers.google.com/search/docs/essentials/spam-policies ; Google Search Central, "AI features and your website" — https://developers.google.com/search/docs/appearance/ai-features ; Sitemaps protocol — https://www.sitemaps.org/protocol.html
- **Depends on:** none — standalone: it audits the site's own rendered output, server responses, and robots/sitemap files — the crawl-and-index contract is checked against the site itself, not another skill's output. It feeds on-page-seo, aeo, geo, sitemaps, and web-analytics.
- **Feeds into:** on-page-seo, aeo, geo, sitemaps, web-analytics

## When to use / Do NOT use

- **Use when:** a site is built, migrated, redesigned, or promoted between environments, and whenever crawlability, rendering, indexation, canonicalization, or redirect behavior is in question. This skill owns the crawl-and-index contract between the site and search engines.
- **Do NOT use when:** the question is what a page says (copywriting, on-page-seo), what its markup declares (structured-data), or which URLs the sitemap lists (sitemaps — this skill sets the contract that skill generates against). Never use it to promise a ranking: Google documents eligibility requirements, not ranking outcomes.

## Rules

1. **CO-001 — The indexable-page contract.** Every page intended for search returns HTTP 200, carries a self-referencing canonical, and is reachable by following links from the site itself. A page failing any leg is a defect to fix, not a ranking mystery to explain.
2. **CO-002 — Server-rendered by default.** Indexable content ships as server-rendered or statically generated HTML. Client-side rendering of indexable content is an exception that must be verified under CO-003, never a default.
3. **CO-003 — Verify the rendered HTML.** JavaScript-dependent content is checked in the rendered HTML (Search Console URL Inspection or an equivalent rendered-DOM fetch), never assumed from source code, view-source, or a local build.
4. **CO-004 — robots.txt discipline.** robots.txt follows RFC 9309 syntax, is served at the host root with HTTP 200, and never blocks the CSS or JavaScript assets that rendering the pages requires. Every change to it is reviewed like a code change.
5. **CO-005 — The promotion indexability diff.** Before every production release, staging and production are diffed on robots.txt, `noindex` (meta and X-Robots-Tag), basic-auth walls, and canonical host. Any staging protection found in production is a release blocker.
6. **CO-006 — One canonical URL per page.** Each page has exactly one canonical URL, stated as an absolute URL that itself returns 200 and is indexable. Parameter, filter, sort, session, and print variants canonicalize to the base URL or carry `noindex`; they are never indexable duplicates competing with it.
7. **CO-007 — Redirect hygiene.** Permanent moves use 301 or 308. Redirects are single-hop wherever the destination is known; a chain longer than two hops is fixed at the source, not documented and left.
8. **CO-008 — Real status codes.** Missing content returns a real 404 or 410. An error page served with HTTP 200 (a soft 404) is a defect, as is redirecting every removed URL to the homepage.
9. **CO-009 — One host, one scheme.** The site canonicalizes to a single host form (www or non-www) over HTTPS. Every other host/scheme combination 301-redirects to it, and canonicals, sitemaps, and internal links use only that form.
10. **CO-010 — The sitemap contract.** The XML sitemap lists only canonical, indexable URLs that return 200, is regenerated when routes change, stays within protocol limits (50,000 URLs / 50 MB per file, sitemap index beyond that), and is referenced in robots.txt. Generation itself belongs to the sitemaps skill; this rule is the contract it must satisfy.
11. **CO-011 — Directive consistency.** robots.txt, meta robots, X-Robots-Tag, and canonicals never contradict each other on the same URL, and no CDN, firewall, or hosting rule blocks search or AI crawlers that robots.txt allows — Google names CDN/hosting-level blocking as a real eligibility failure for its AI features.
12. **CO-012 — Coverage reviewed on a cadence.** Search Console coverage and indexing reports are reviewed on a fixed cadence (monthly at minimum) and the review is logged. Every spike in excluded or error URLs is triaged to a named cause. Reports state eligibility and defects found; they never state or imply a ranking guarantee.

## BAN list

- **BAN-CO-001 — Staging protection shipped live.** Banned: promoting a build whose production environment still carries staging `noindex`, `Disallow: /`, a basic-auth wall, or staging-host canonicals. Defeats: DET-CON-002. Bad: the redesigned site launches with `<meta name="robots" content="noindex">` copied from the staging template, and organic traffic falls to zero over two weeks before anyone checks. Instead: run the CO-005 promotion diff; production ships only when no staging directive survives. Severity: BLOCK.
- **BAN-CO-002 — Indexable duplicate URL variants.** Banned: letting parameter, filter, sort, or session URLs be indexed as separate pages with self-referencing canonicals, splitting signals across duplicates of one page. Defeats: DET-CON-025. Bad: `/products?color=red`, `/products?sort=price`, and `/products` are all indexed, each canonicalizing to itself. Instead: variants canonicalize to the base URL or carry `noindex` (CO-006); only substantively different pages are indexable. Severity: BLOCK.
- **BAN-CO-003 — Soft 404s.** Banned: serving "page not found" content with HTTP 200, or answering every deleted URL with a redirect to the homepage. Defeats: DET-CON-015. Bad: a removed product URL returns 200 with a "this item is gone" template, so the index fills with dead pages the status code calls healthy. Instead: return a real 404/410 for gone content, and 301 only to a genuinely equivalent replacement (CO-008). Severity: BLOCK.
- **BAN-CO-004 — Ranking guarantees and fabricated visibility wins.** Banned: promising a ranking, traffic figure, or AI-citation outcome in any plan or report, or reporting an unadopted proposal (e.g. llms.txt, which Google states on the record it does not use) as an AI-visibility win. Defeats: DET-CON-026. Bad: the launch report claims the new llms.txt file "secures AI Overview citations" and projects a "#1 ranking within 90 days". Instead: report only what Google documents — indexed, snippet-eligible, defects fixed — and label every other claim with its evidence level or cut it. Severity: BLOCK.

## Gates

- **G-CO-001 — Promotion indexability diff.** Verifies: CO-005, CO-004, CO-011. Check: automated — script fetches staging and production robots.txt plus the response headers and meta robots of the top route templates, and diffs directives and canonical host. Pass: zero staging protections (noindex, Disallow: /, auth wall, staging canonical) present in production. Fail: block the release. Before a production environment is provisioned, this gate's disposition is a recorded provisioning waiver per the §6.3 protocol; it unblocks when a production environment is provisioned and the release is deployed to it. Recorded in: progress.md.
- **G-CO-002 — Route inventory crawl.** Verifies: CO-001, CO-006, CO-009. Check: automated — crawl the production route inventory and assert, per indexable URL: HTTP 200, self-referencing canonical in the canonical host form, no `noindex`. Pass: 100% of indexable URLs satisfy all three. Fail: block shipment of the affected routes. Recorded in: progress.md.
- **G-CO-003 — Redirect and status audit.** Verifies: CO-007, CO-008. Check: automated — follow every redirect reachable from internal links and the sitemap; assert chains are ≤2 hops, permanent moves are 301/308, and a sample of deleted URLs returns 404/410, not 200 or a homepage redirect. Pass: all assertions hold. Fail: fix at the source and re-run. Recorded in: progress.md.
- **G-CO-004 — Rendered-content verification.** Verifies: CO-002, CO-003. Check: manual with tooling — for a sample of JavaScript-dependent templates, compare the rendered HTML (URL Inspection or rendered-DOM fetch) against the expected primary content: heading, body text, links, canonical. Pass: primary content fully present in the rendered HTML for every sampled template. Fail: treat as a rendering defect; do not ship the template. Recorded in: progress.md.
- **G-CO-005 — Coverage review log.** Verifies: CO-012. Check: manual — the monthly Search Console review exists in the project log with excluded/error counts, each spike triaged to a named cause, and no ranking or traffic guarantee stated anywhere in it. Pass: log entry complete for the current month. Fail: the review is overdue; complete it before the next release. Recorded in: progress.md.

## Anti-patterns

- **The view-source check.** Verifying a JavaScript page by reading its source HTML and concluding the content is "there" or "missing" from an unrendered shell. Catch it: any verification note that does not name the rendered-HTML tool used is not a verification (CO-003).
- **Folklore-first fixes.** Implementing tactics with no basis in Google's documentation — meta keywords, keyword-density targets, llms.txt as a ranking lever — while documented crawl or indexation defects stay open. Catch it: ask of every task, "which Google document requires this?"; no answer, no priority.
- **Canonical roulette.** Changing the canonical host, scheme, or trailing-slash strategy repeatedly, each time without a recorded decision, so the index never settles. Catch it: the canonical form is a one-time decision under CO-009; a second change in a quarter demands a written reason.
- **The one-and-done audit.** A thorough launch audit, then silence while template refactors quietly break canonicals, directives, and status codes for months. Catch it: gates G-CO-001–G-CO-003 run per release and G-CO-005 monthly — an audit with no cadence is a snapshot, not a control.

## Examples

- [Example 1 — The staging noindex that shipped to production](examples/example-1.md) — corrects CO-005.
- [Example 2 — Filter URLs indexed as duplicates](examples/example-2.md) — corrects CO-006.
- [Example 3 — The page that existed only after JavaScript](examples/example-3.md) — corrects CO-003.

## Recall anchors

- 200, self-canonical, reachable by links — or it is a defect.
- Verify the rendered HTML, never the source.
- Diff staging against production before every release.
- One canonical URL per page; variants canonicalize or noindex.
- Report eligibility and defects — never promise a ranking.

## Checklist

- [ ] Promotion indexability diff is clean: no staging directive in production (G-CO-001).
- [ ] Every indexable URL returns 200 with a self-referencing canonical (G-CO-002).
- [ ] robots.txt is RFC 9309-valid and blocks no render asset (CO-004).
- [ ] Redirect chains are ≤2 hops; permanent moves are 301/308 (G-CO-003).
- [ ] Deleted URLs return a real 404/410 — no soft 404s (CO-008).
- [ ] JavaScript-dependent templates verified in rendered HTML (G-CO-004).
- [ ] Sitemap lists only canonical, indexable, 200 URLs (CO-010).
- [ ] This month's Search Console coverage review is logged, with no ranking guarantee stated (G-CO-005).
