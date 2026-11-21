# site-discovery

## Metadata

- **Owner department:** D16 Cloning & Replication (CL)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://github.com/internetarchive/wayback/blob/master/wayback-cdx-server/README.md ; https://www.rfc-editor.org/rfc/rfc9309.html
- **Depends on:** clone-ethics
- **Feeds into:** page-inventory

## When to use / Do NOT use

- **Use when:** an authorized replication or migration engagement begins and the target's full URL space — routes, templates, and states — must be established before anything is inventoried or built. This skill produces the reconciled discovery record (live crawl, sitemap, archive lists) that page-inventory consumes.
- **Do NOT use when:** no D14 clone-ethics authorization record exists yet (run clone-ethics first; this skill refuses to start), the task is the inventory table itself (page-inventory), asset capture (asset-harvesting), or general evidence harvesting for the detection pipeline (X-Crawl owns that; DET-CRWL parameters gate it).

## Rules

1. **CL-001 — Authorization artifact precedes the first request.** No target request of any kind — no discovery crawl, no sitemap fetch, no archive enumeration — runs before the project's clone-ethics authorization record exists, is dated, names the target domains in scope, and predates the first crawl log entry. The robots.txt and sitemap fetches under CL-003 are the first authorized step, taken only after the record exists. The crawl tooling checks for the record and fails closed when it is absent, stale, or out of scope. A verbal go-ahead or a record written after crawling started does not satisfy this rule.
2. **CL-002 — The crawler identifies itself honestly.** Every request carries a user agent naming the project and a contact address. The crawler never spoofs a consumer browser user agent, rotates identities to evade throttling, or otherwise disguises automated access as human browsing.
3. **CL-003 — Robots and sitemap are fetched first, and the check is logged.** For each in-scope domain, fetch `robots.txt` and the sitemap index before the first content request, and log the robots check with its date in the crawl log. A domain with no robots.txt is logged as "no robots.txt" — absence is recorded, never silently assumed.
4. **CL-004 — Disallow and crawl-delay are honored in full.** A path matched by a Disallow rule is recorded as "excluded by robots" and never fetched; a stated crawl-delay sets the minimum request interval. Per RFC 9309, robots rules "are not a form of access authorization": a missing Disallow is crawl access only and grants no reuse rights in anything discovered.
5. **CL-005 — Request rate stays inside the recorded limit.** The crawl plan states a maximum request rate per host before the run; the crawler enforces it, backs off on 429/503 responses, and the crawl log shows the observed rate. Discovery that degrades the target's availability is a failed run, however complete its output.
6. **CL-006 — The URL space comes from at least three independent sources.** Build three lists: (a) a browser-rendered crawl from the home page, (b) the XML sitemap(s), (c) the Wayback CDX index queried with `matchType=domain` (or `prefix` per host). When the client provides analytics or Search Console top pages, add them as a fourth source. A single-source list is a draft, never a discovery result.
7. **CL-007 — Every cross-source difference is reconciled in writing.** Diff the lists; each URL present in one source and absent from another gets a reconciliation note (redirected, archived-only, robots-excluded, JS-routed, gated, removed). No URL is dropped silently, and discovery is not complete while any difference is unexplained.
8. **CL-008 — JavaScript routes are discovered, not assumed away.** The crawl runs in a real browser engine so JS-rendered links resolve, and route manifests are extracted from the served JS bundles to expose client-side routes no anchor points to. Routes found only in bundles enter the crawl list tagged `js-route` and are spot-checked against the rendered site.
9. **CL-009 — Gated space is recorded as gated, never entered by bypass.** Discovery never authenticates with borrowed, shared, or client-unrelated credentials, never routes around a login or paywall, and never fetches a URL the authorization does not cover. Login-walled and paywalled URL spaces are recorded as gated with the evidence that shows they exist (sitemap entry, CDX capture, bundle route).
10. **CL-010 — Discovery records structure, not content rights.** The deliverable is URLs, statuses, template hints, and provenance — never copied page text, images, or marks. Nothing discovered here licenses reusing the target's copy, imagery, or branding; rights decisions belong to clone-ethics and asset-harvesting.
11. **CL-011 — Every discovered URL carries provenance.** Each URL in the discovery record is tagged with the source list(s) that found it (`crawl`, `sitemap`, `cdx`, `analytics`), its HTTP status or archive status, and the discovery date. A URL with no provenance tag is treated as unverified and cannot pass to page-inventory.
12. **CL-012 — Thin evidence triggers the fallback, and archive exclusion routes to D14.** When CDX coverage or a sitemap is missing or sparse, fall back to client-provided exports and analytics lists and record which sources were unavailable; the three-source gate (G-CL-003) then runs on the sources that exist, with the gap stated. If the target's robots.txt excludes archiving or crawling outright, stop and route the case to clone-ethics (D14) — the exclusion may signal against capture generally, and discovery does not decide that question itself.

## BAN list

- **BAN-CL-001 — Crawl first, authorize later.** Banned: any discovery crawl that starts before the clone-ethics authorization record exists and predates it. Defeats: DET-CRWL-014. Bad: the agent crawls a client's old site "just to scope it" on Monday; the authorization record is filed Friday. Instead: commit the authorization record first and let the pre-flight gate (G-CL-001) refuse any earlier crawl, under CL-001. Severity: BLOCK.
- **BAN-CL-002 — Fetching robots-disallowed paths.** Banned: requesting any URL matched by the target's robots.txt Disallow rules, for any reason, including "just to confirm it exists". Defeats: DET-CRWL-014. Bad: the crawl log shows 14 fetches under `/internal/` because the crawler's robots handling was switched off to "get the full picture". Instead: record each disallowed space as "excluded by robots" without fetching it, under CL-004. Severity: BLOCK.
- **BAN-CL-003 — Completing discovery through a login or paywall bypass.** Banned: enumerating gated URL space using borrowed or shared credentials, a harvested session cookie, or a mirror/cache route around a login wall or paywall. Defeats: DET-CRWL-008. Bad: a teammate's personal account login is used to crawl the members' area so the route list looks complete. Instead: record the space as gated with its public evidence and proceed only through access the client legitimately provides, under CL-009. Severity: BLOCK.
- **BAN-CL-004 — Home-page links declared "fully mapped".** Banned: presenting a crawl of home-page links alone as the site's complete URL space, with orphan, archived-only, and JS-routed pages silently absent. Defeats: DET-CRWL-013. Bad: the discovery report claims "site fully mapped: 38 pages" from one crawl, while the sitemap lists 112 URLs and the CDX index holds 40 more, none of them checked. Instead: build the three source lists and reconcile every difference in writing before claiming completeness, under CL-006 and CL-007. Severity: BLOCK.
- **BAN-CL-005 — The disguised crawler.** Banned: sending a spoofed consumer-browser user agent, rotating user agents or IPs to evade rate limits, or stripping identifying headers so automated discovery reads as human traffic. Defeats: DET-CRWL-016. Bad: the crawler presents as "Mozilla/5.0 (Windows NT 10.0) Chrome" with no project identity after the target begins throttling it. Instead: identify the project and a contact in the user agent and slow down or stop when throttled, under CL-002 and CL-005. Severity: BLOCK.

## Gates

- **G-CL-001 — Authorization pre-flight check.** Verifies: CL-001. Check (automated): before the crawler starts, a script asserts the project's clone-ethics authorization record file exists, is dated, names the target domains, covers discovery of those domains, and its commit timestamp predates the current run. Pass: record complete, in scope, and pre-committed. Fail: the crawler refuses to start (fail closed); no partial crawl is permitted. Recorded in: progress.md. Pattern-reference mode: ADAPTED — the authorization record names the pattern class and zero target domains, and its timestamp is compared against the first inventory artifact; see the pattern-reference disposition table in the clone-rebuild playbook.
- **G-CL-002 — Robots and terms compliance check.** Verifies: CL-003, CL-004, CL-005. Check (automated): the crawl log is grepped against each domain's robots.txt Disallow set — any fetched disallowed path fails; the log must also show a robots fetch per domain before its first content request, the identifying user agent on every request, and an observed request rate at or under the crawl plan's limit. Pass: zero disallowed fetches, robots logged first, identity and rate compliant. Fail: block delivery of the discovery record; each breach is filed as a finding. Recorded in: progress.md. Pattern-reference mode: ADAPTED — no domain is fetched, so compliance is evidenced by the zero-fetch crawl log and the record's no-target scope; see the pattern-reference disposition table in the clone-rebuild playbook.
- **G-CL-003 — Three-source reconciliation check.** Verifies: CL-006, CL-007, CL-012. Check (automated + manual): a script diffs the crawl, sitemap, and CDX URL lists and lists every URL not present in all sources; each listed URL must carry a reconciliation note in the discovery record. Where a source was unavailable, the record states the gap and the fallback used. Pass: zero unexplained differences. Fail: block; discovery is incomplete until every difference is explained or the URL is carried into page-inventory with its note. Recorded in: progress.md. Pattern-reference mode: ADAPTED — the pattern inventory replaces the crawl, sitemap, and CDX lists as the reconciliation source; see the pattern-reference disposition table in the clone-rebuild playbook.
- **G-CL-004 — JS-route spot-check.** Verifies: CL-008. Check (manual): pick 5 routes found only in JS bundle manifests; load each in a browser and confirm the route renders and matches its discovery-record entry (URL, status, template hint). Pass: all 5 confirmed. Fail: re-extract route manifests and re-run the rendered crawl before discovery closes. Recorded in: progress.md. Pattern-reference mode: NOT APPLICABLE — no JS bundle manifests exist and no target page may be loaded; route existence rests on the pattern inventory; see the pattern-reference disposition table in the clone-rebuild playbook.
- **G-CL-005 — Gated-space and provenance audit.** Verifies: CL-009, CL-010, CL-011. Check (automated + manual): assert every URL in the discovery record carries at least one provenance tag and a status; assert no fetched URL required authentication (no session cookies or Authorization headers in the crawl log); assert every gated space appears as a gated record, not as fetched pages. Pass: provenance complete, zero authenticated fetches, gated spaces recorded as gated. Fail: block; the offending fetches are removed from the record and filed as findings. Recorded in: progress.md. Pattern-reference mode: ADAPTED — provenance tags read “pattern reference” and the zero-authenticated-fetch assertion is evidenced by the zero-fetch crawl log; see the pattern-reference disposition table in the clone-rebuild playbook.

## Anti-patterns

- **The sitemap treated as the site.** The sitemap is one source of three; it routinely omits new, orphaned, and utility pages. Catch it by never closing discovery until the crawl and CDX lists have been diffed against it (G-CL-003).
- **Reconciliation by deletion.** Cross-source differences are "resolved" by deleting the odd URL from the list instead of explaining it. Catch it by counting: the reconciled record's URL total must be at least the largest single source's total, with notes accounting for the rest.
- **Completeness theater.** The report says "full URL space" while the crawl depth, rate limit, or robots exclusions quietly truncated coverage. Catch it by stating crawl depth, exclusions, and unavailable sources in the record itself — coverage claims must name their limits.
- **Discovery drifting into harvesting.** Page bodies, images, and copy start accumulating in the discovery folder "for reference". Catch it by checking the discovery output contains URLs and metadata only; content capture belongs to asset-harvesting under its own rights decisions.

## Examples

- [Example 1 — Discovery launched on a verbal OK](examples/example-1.md) — violates/corrects CL-001.
- [Example 2 — "Fully mapped" from the home page](examples/example-2.md) — violates/corrects CL-006, CL-007.
- [Example 3 — The members' area, enumerated with a borrowed login](examples/example-3.md) — violates/corrects CL-009.

## Recall anchors

- No authorization record, no first request — the crawler fails closed.
- Three lists or it is a draft: crawl, sitemap, CDX — every difference explained.
- Disallowed means recorded, never fetched.
- Gated means recorded as gated, never entered.
- Discovery maps structure; it grants no rights in anything it finds.

## Checklist

- [ ] The clone-ethics authorization record is committed, dated, and covers the target domains — and predates the first crawl log entry (CL-001, G-CL-001).
- [ ] robots.txt and the sitemap index were fetched and logged per domain before any content request (CL-003, G-CL-002).
- [ ] No disallowed path was fetched; each is recorded as "excluded by robots" (CL-004, G-CL-002).
- [ ] The crawler identified the project and contact, and stayed inside the recorded rate limit (CL-002, CL-005, G-CL-002).
- [ ] Crawl, sitemap, and CDX lists are built and every difference carries a reconciliation note (CL-006, CL-007, G-CL-003).
- [ ] JS-bundle routes are extracted, tagged, and spot-checked in a browser (CL-008, G-CL-004).
- [ ] No login, paywall, or access control was bypassed; gated spaces are recorded as gated (CL-009, G-CL-005).
- [ ] Every URL carries provenance tags and a status, and the record holds URLs and metadata only — no copied content (CL-010, CL-011, G-CL-005).
