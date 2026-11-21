# sitemaps

## Metadata

- **Owner department:** D9 SEO & Content (CO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Google Search Central, "Build and submit a sitemap" — https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap ; Sitemaps protocol — https://www.sitemaps.org/protocol.html
- **Depends on:** technical-seo
- **Feeds into:** internal-linking, web-analytics

## When to use / Do NOT use

- **Use when:** a site launches, migrates, restructures, or changes its route or content inventory, and whenever sitemap correctness, freshness, or Search Console sitemap errors are in question. This skill owns the sitemap as a generated claim about which URLs exist and are indexable.
- **Do NOT use when:** the question is whether a page should be indexable or canonical at all (technical-seo sets that contract; this skill generates against it), or how pages get discovered by users (internal-linking — the sitemap is a crawler fallback, never a linking strategy).

## Rules

1. **CO-181 — Generated, never hand-maintained.** The sitemap is a build artifact generated from the actual route and content inventory at publish time. No sitemap file is ever edited by hand; a needed change is made in the inventory or the generator, never in the output.
2. **CO-182 — Canonical entries only.** Every listed URL returns HTTP 200, is indexable (no `noindex`, no robots block), and is its own canonical. An entry is a claim that the URL is live and canonical — if any leg fails, the URL does not belong in the file.
3. **CO-183 — No dead or redirected entries.** Redirects (3xx), errors (4xx/5xx), non-canonical variants, and parameter, filter, sort, or session URLs are never listed. The sitemap names destinations, not paths to them.
4. **CO-184 — One host, one scheme, absolute URLs.** Every entry is an absolute URL on the site's single canonical host and scheme (per technical-seo CO-009). No relative URLs, no mixed www/non-www, no HTTP entries on an HTTPS site.
5. **CO-185 — Truthful lastmod.** `lastmod` is the date the page's content last changed significantly, taken from the content record — never the build or deploy timestamp. When the change date is not known, omit `lastmod` rather than invent one; engines discount sitemaps whose dates cry wolf.
6. **CO-186 — Event-driven regeneration.** The sitemap regenerates in the same build or publish event that changes the inventory: publish, unpublish, route change, redirect change. A sitemap older than the newest content change is stale by definition and is a defect, not a backlog item.
7. **CO-187 — Protocol limits.** Each sitemap file holds at most 50,000 URLs and 50 MB uncompressed, per the sitemaps protocol. Beyond either limit, split into multiple files under a sitemap index. The limit is measured on the uncompressed file, even when the served file is gzipped.
8. **CO-188 — Shard by section.** Large sites shard sitemaps by content type or section (posts, products, docs) under one sitemap index, so a broken or stale section is visible in Search Console reporting instead of diluted across one giant file.
9. **CO-189 — Count reconciliation.** After every generation, the sitemap URL count is reconciled against the route/content inventory count. Every difference has a named reason (draft, noindex by design, redirect) recorded with the build; an unexplained difference fails the release.
10. **CO-190 — Discovery wiring.** The sitemap is referenced by a `Sitemap:` line in robots.txt and submitted in Search Console. After a domain change, restructure, or index rebuild, the submission is re-verified — the file existing on the server is not evidence any engine knows about it.
11. **CO-191 — Production purity.** A staging sitemap never deploys to production, and a production sitemap never lists staging hosts or staging URLs. The sitemap host check is part of technical-seo's staging-vs-production promotion diff.
12. **CO-192 — No invented priority or changefreq.** `priority` and `changefreq` are omitted, or set truthfully per section from the actual update pattern. Values that misstate the pages (1.0 and "always" site-wide) are fabricated metadata and are never emitted to look thorough.

## BAN list

- **BAN-CO-091 — Dead and excluded URLs listed.** Banned: a sitemap containing URLs that return 404/410, redirect, carry `noindex`, or canonicalize to a different URL. Defeats: DET-CON-015. Bad: the launch sitemap still lists 214 URLs a year later; 96 are deleted products, 41 redirect to category pages, and 12 are `noindex` landing pages. Instead: generate from the live inventory and filter on 200 + indexable + self-canonical before writing any entry (CO-182, CO-183). Severity: BLOCK.
- **BAN-CO-092 — Deploy-date lastmod.** Banned: stamping every entry's `lastmod` with the build or deploy date, so unchanged pages claim to have changed on every release. Defeats: DET-CON-018. Bad: a nightly deploy rewrites all 8,000 `lastmod` values to today's date, including a legal page untouched for two years. Instead: take `lastmod` from each content record's real change date, and omit it where that date is unknown (CO-185). Severity: BLOCK.
- **BAN-CO-093 — The hand-maintained sitemap.** Banned: a static `sitemap.xml` written or edited by hand — typically generated once at launch and shipped untouched ever after while the site changes around it. Defeats: DET-CON-002. Bad: a developer hand-adds three new pages to the XML, misses eleven others, and the file still lists the scaffold's sample page. Instead: the sitemap is generated from the route/content inventory on every publish event; hands never touch the output (CO-181, CO-186). Severity: BLOCK.
- **BAN-CO-094 — Variant URLs listed as pages.** Banned: listing parameter, filter, sort, session, or print variants as separate sitemap entries to inflate the URL count. Defeats: DET-CON-025. Bad: `/products?color=red`, `/products?sort=price`, and `/products?utm_source=newsletter` all appear as entries alongside `/products`. Instead: list only the canonical URL of each substantively distinct page (CO-183); variants canonicalize or carry `noindex` under technical-seo. Severity: BLOCK.
- **BAN-CO-095 — Staging URLs in the production sitemap.** Banned: a production sitemap listing staging hosts, preview URLs, or internal hostnames. Defeats: DET-CON-015. Bad: after a rushed release, `https://staging.example.com/pricing` ships in the live sitemap and crawlers are sent to an auth-walled preview. Instead: generate against the production inventory on the canonical host only, and run the host check in the promotion diff (CO-184, CO-191). Severity: BLOCK.

## Gates

- **G-CO-091 — Sitemap audit script.** Verifies: CO-182, CO-183, CO-184. Check: automated — `python3 scripts/sitemap_audit.py --sitemap https://example.com/sitemap.xml` fetches the sitemap (following the index to every shard), requests every listed URL (or a statistically sound random sample above 10,000 URLs), and asserts per URL: HTTP 200, no redirect, canonical tag equal to the listed URL, no `noindex` in meta robots or X-Robots-Tag, host and scheme equal to the canonical host. Pass: zero assertion failures. Fail: block the release; fix the inventory or generator, never the output file. Recorded in: progress.md.
- **G-CO-092 — Count reconciliation.** Verifies: CO-181, CO-189. Check: automated — the build compares the generated sitemap's URL count against the route/content inventory count and writes both numbers plus a reason for every excluded inventory item (draft, noindex, redirect) to the build log. Pass: counts reconcile with every difference explained. Fail: block the release until the difference is explained. Recorded in: progress.md.
- **G-CO-093 — Regeneration-on-change test.** Verifies: CO-181, CO-186. Check: automated — in the staging build, publish one test page and unpublish another, rebuild, and diff the sitemap: the published URL must appear and the unpublished URL must disappear, with no manual step. Pass: both changes reflected by the build alone. Fail: the generator is not wired to the inventory; fix before launch. Recorded in: progress.md.
- **G-CO-094 — lastmod spot-check.** Verifies: CO-185. Check: automated assist — sample 25 entries carrying `lastmod` and compare each against the content record's actual last-change timestamp (CMS field or version-control history for that page's source). Pass: every sampled `lastmod` matches the record, or the entry omits `lastmod`. Fail: remove or correct the dates at the generator and re-run. Recorded in: progress.md.
- **G-CO-095 — Discovery wiring check.** Verifies: CO-190, CO-191. Check: automated — fetch robots.txt and assert it contains a `Sitemap:` line naming the production sitemap index on the canonical host; fetch that URL and assert HTTP 200 and zero listed URLs on any non-production host. Pass: both assertions hold and the Search Console submission is confirmed in the project log. Fail: fix robots.txt or the generator's host configuration and re-check. Before a production environment is provisioned, this gate's disposition is a recorded provisioning waiver per the §6.3 protocol; it unblocks when the production site is deployed on its canonical host and Search Console access exists. Recorded in: progress.md.

## Anti-patterns

- **Ping-and-pray resubmission.** Resubmitting the same stale sitemap in Search Console hoping indexing improves, while the file still lists dead URLs. Catch it: a resubmission with no generator or inventory change since the last one fixes nothing — run G-CO-091 first.
- **Sitemap as linking strategy.** Adding an orphan page to the sitemap instead of linking it from navigation, a hub, or body content, and calling it discoverable. Catch it: if the page's only inbound reference is the sitemap, internal-linking owns the fix, not this file.
- **Count pride.** Reporting "12,000 URLs submitted" as an SEO result while a third are excluded, redirected, or dead. Catch it: the honest numbers are the reconciled count (G-CO-092) and the audit pass rate (G-CO-091), never the raw entry count.
- **The forgotten index.** Restructuring shards — renaming, merging, removing sections — without updating the sitemap index, so the index points at files that no longer exist. Catch it: after any shard change, fetch every child named in the index; a 404 child is a release defect.

## Examples

- [Example 1 — The launch-day sitemap, one year later](examples/example-1.md) — corrects CO-181.
- [Example 2 — Every lastmod is the deploy date](examples/example-2.md) — corrects CO-185.
- [Example 3 — The audit: 1,200 entries, 214 bad claims](examples/example-3.md) — corrects CO-182.

## Recall anchors

- Generated from the inventory — hands never touch the output.
- Every entry is a claim: 200, indexable, self-canonical.
- lastmod is the content's change date, or it is omitted.
- Counts reconcile, or the difference has a name.
- The sitemap is a crawler fallback, not a linking strategy.

## Checklist

- [ ] Sitemap generated from the route/content inventory in this build — no hand edits (CO-181).
- [ ] Audit script passes: every listed URL returns 200, self-canonical, indexable (G-CO-091).
- [ ] Sitemap count reconciles with the inventory count; every difference explained (G-CO-092).
- [ ] Publish/unpublish test changes the sitemap with no manual step (G-CO-093).
- [ ] Sampled `lastmod` values match real content change dates (G-CO-094).
- [ ] No staging host or non-canonical URL anywhere in the file (G-CO-095).
- [ ] Each file within 50,000 URLs / 50 MB uncompressed; index current (CO-187, CO-188).
- [ ] robots.txt names the sitemap and Search Console submission is confirmed (CO-190).
