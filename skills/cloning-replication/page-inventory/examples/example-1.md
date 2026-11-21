# Example 1 — Four sources merged, one reconciled table

## Before

The inventory is built from the navigation menu and a homepage crawl: 22 rows. The sitemap's 140 blog posts, the analytics top-pages list (which includes a campaign landing page no longer linked anywhere), and 31 archived-only pages in the CDX index never appear. The deliverable calls the 22 rows "all pages," so reconstruction rebuilds a fraction of the site while claiming full coverage.

## After

All four sources are merged and deduplicated into one table of 196 canonical rows. Each source difference carries a reconciliation note: the campaign landing page is `archived-only` provenance, the 31 CDX-only pages are marked with their last capture dates, and sitemap-only URLs that return 404 are recorded as excluded with the reason "gone, no capture." The client signs off the in-scope count of 158 before reconstruction starts.

Note: corrects CL-021 — the inventory merges crawl, sitemap, analytics, and CDX sources and reconciles every difference; it is never built from navigation alone.
