# internal-linking

## Metadata

- **Owner department:** D9 SEO & Content (CO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** PROJECT_ANATOMY.md, "Internal linking and sitemaps"; Google Search Central, "AI features and your website" (internal links named an AI-visibility fundamental) — https://developers.google.com/search/docs/appearance/ai-features
- **Depends on:** technical-seo, sitemaps
- **Feeds into:** content-strategy, aeo, geo

## When to use / Do NOT use

- **Use when:** designing a site's navigation, hubs, and breadcrumbs; publishing or retiring any page; reviewing a crawl; or diagnosing a page that gets no organic or referral traffic.
- **Do NOT use when:** the question is which URLs exist in the sitemap file (sitemaps — the sitemap is a fallback, never the linking strategy), what a page says (copywriting, on-page-seo), or whether a URL should exist at all (content-strategy).

## Rules

1. **CO-201 — No orphan pages.** Every indexable page is linked from at least one non-sitemap page. An indexable page with zero inbound internal links is a defect, and every defect gets a named owner and a fix date.
2. **CO-202 — Shallow depth.** Every indexable page is reachable from the home page in at most 3 clicks by following links. Depth is measured on the crawl-derived link graph, never estimated.
3. **CO-203 — The brief names inbound links first.** Every new page's content brief names its planned inbound links (source page + anchor text) before the page is written. A page with no planned inbound links does not enter production.
4. **CO-204 — Anchor text describes the destination.** Anchor text names the destination page's topic, so it reads correctly out of context. "Click here", "here", and a bare "read more" are never the anchor for a content link.
5. **CO-205 — One anchor, one destination.** Identical anchor text never points to two different pages, and one destination is not linked under contradictory names. Collisions found in a crawl are renamed until each anchor maps to exactly one page.
6. **CO-206 — Link the canonical URL directly.** Internal links point at the canonical URL itself. No internal link may resolve through a redirect: if the target moved, the link is updated to the new URL in the same change.
7. **CO-207 — Critical pages earn in-content links.** Pricing, signup, and flagship content pages receive deliberate in-content links from relevant high-traffic pages. Nav or footer placement alone does not satisfy this rule.
8. **CO-208 — Retirement is one change.** When a page is retired or merged, its inbound internal links are updated or removed and its redirect is added in the same change — never in a later cleanup.
9. **CO-209 — The link graph is reviewed per release.** Every release produces a crawl-derived link graph (depth, in-degree, orphan list) and the review is recorded. A release with no graph review does not ship link or template changes.
10. **CO-210 — Hubs and breadcrumbs carry the structure.** Every section has a hub page that links its children, and every child page links back via breadcrumb or hub. No section is reachable only through site search or the sitemap.
11. **CO-211 — No broken internal links.** Every internal link resolves to a live page returning HTTP 200. A link to a 404, an error page, or an empty route is a defect with an owner, fixed like any other broken feature.
12. **CO-212 — Links are placed for readers.** A link exists because a reader at that point benefits from the destination. Link blocks, footer dumps, and pages built only to pass crawl equity to other pages are not a linking strategy.

## BAN list

- **BAN-CO-101 — Sitemap-only discovery.** Banned: shipping an indexable page whose only discovery path is the XML sitemap, with no inbound link from any real page. Defeats: DET-CON-025. Bad: the new pricing page is in sitemap.xml and returns 200, but no page on the site links to it, so neither users nor crawlers following links ever reach it. Instead: add at least one in-content inbound link from a relevant page before publish (CO-201, CO-203). Severity: BLOCK.
- **BAN-CO-102 — Generic anchor text.** Banned: using "click here", "here", or "read more" as the anchor text for content links. Defeats: DET-CON-006. Bad: a features page ends three sections with "To learn more, click here", "click here", and "click here", pointing at pricing, docs, and a case study. Instead: write the anchor as the destination's topic — "See pricing plans", "Read the API docs", "Read the Acme case study" (CO-204). Severity: BLOCK.
- **BAN-CO-103 — Anchor promises the destination doesn't keep.** Banned: anchor text naming a topic, offer, or document the destination page does not contain. Defeats: DET-CON-022. Bad: the anchor "Download the 2026 pricing PDF" links to a generic contact page with no PDF and no pricing. Instead: make the anchor describe what the destination actually delivers, or create the promised page and link that (CO-204). Severity: BLOCK.
- **BAN-CO-104 — Same anchor, different destinations.** Banned: one anchor string (e.g. "Our platform") linking to the product page in one place, the home page in another, and a landing page in a third. Defeats: DET-CON-015. Bad: "Our platform" resolves to three different URLs across the blog, so readers and crawlers cannot tell which page the phrase names. Instead: assign each anchor string exactly one destination site-wide and rename the variants (CO-205). Severity: WARN.
- **BAN-CO-105 — Template and staging links shipped live.** Banned: production navigation, footer, or body links still pointing at scaffold demo pages, a staging host, or placeholder routes from the site template. Defeats: DET-CON-002. Bad: the footer "Company" column links to the theme's demo About page on staging.example.com. Instead: repoint every shipped link at the real production page or remove it, and verify with the G-CO-102 scan before release. Severity: BLOCK.

## Gates

- **G-CO-101 — Orphan and depth report.** Verifies: CO-201, CO-202, CO-210. Check: automated — crawl the production site, build the link graph, and list every indexable URL with in-degree 0 (sitemap excluded as a link source) plus every URL deeper than 3 clicks from home. Pass: zero orphans and zero pages deeper than 3 clicks. Fail: block the release; each orphan is assigned a named owner in progress.md. Recorded in: progress.md.
- **G-CO-102 — Direct-target scan.** Verifies: CO-206, CO-211. Check: automated — request every internal href found by the crawl and record the status chain. Pass: 100% of internal links return HTTP 200 with no redirect hop. Fail: block shipment of the affected templates until links point at canonical URLs directly. Recorded in: progress.md.
- **G-CO-103 — Anchor-text audit.** Verifies: CO-204, CO-205. Check: semi-automated — grep the rendered pages for the banned anchor strings ("click here", "here", "read more" as the complete anchor) and group all anchors by string to find one string mapping to multiple URLs; then manually read a sample of 20 in-content anchors against their destinations. Pass: zero banned anchors, zero multi-destination anchor strings, and every sampled anchor describes its destination. Fail: rework the failing anchors and re-run. Recorded in: progress.md.
- **G-CO-104 — New-page inbound check.** Verifies: CO-203, CO-207. Check: manual — at publish, open each inbound link named in the page's brief and confirm it is live on the production page it was planned from, with the planned anchor text. Pass: every planned inbound link exists live at publish. Fail: do not announce or promote the page until the links are in place. Recorded in: progress.md.

## Anti-patterns

- **Nav-only thinking.** Assuming the main menu links everything that matters, so in-content linking is skipped and deep pages depend on two menu levels and luck. Catch it: the G-CO-101 graph shows in-degree, not menu membership — check it, not the menu.
- **The stale hub.** A hub page written at launch and never updated, so everything published since is missing from the one page meant to collect it. Catch it: diff the hub's link list against the section's current page inventory at every release.
- **Redesign amnesia.** Rebuilding navigation or templates without re-running the crawl, silently orphaning pages the old structure used to reach. Catch it: any nav or template change triggers CO-209's graph review before it ships, not after traffic drops.
- **Footer-dump compensation.** Answering "this page needs links" by adding it to a 60-link footer block nobody reads, instead of one relevant in-content link. Catch it: CO-207 asks where the in-content link lives; a footer entry is not an answer.

## Examples

- [Example 1 — The pricing page only the sitemap knew about](examples/example-1.md) — violates/corrects CO-201.
- [Example 2 — Three "click here"s, three destinations](examples/example-2.md) — violates/corrects CO-204.
- [Example 3 — Every blog post linking through a redirect](examples/example-3.md) — violates/corrects CO-206.

## Recall anchors

- If only the sitemap links to it, it is an orphan — and an orphan is a defect with an owner.
- Anchor text is a micro-description of the destination.
- Link the canonical URL, never the redirect.
- The brief names inbound links before the page is written.
- Retire a page and fix its links in the same change.

## Checklist

- [ ] Crawl graph generated this release: zero orphan indexable pages (G-CO-101).
- [ ] Every indexable page is within 3 clicks of home (G-CO-101).
- [ ] Every internal link returns 200 directly — no redirect hops, no 404 targets (G-CO-102).
- [ ] No "click here" / "here" / bare "read more" anchors anywhere (G-CO-103).
- [ ] No anchor string points to more than one destination (G-CO-103).
- [ ] Each new page's brief named its inbound links, and they are live at publish (G-CO-104).
- [ ] Pricing, signup, and flagship pages have in-content links from relevant high-traffic pages (CO-207).
- [ ] Any retired page had its inbound links updated and its redirect added in the same change (CO-208).
