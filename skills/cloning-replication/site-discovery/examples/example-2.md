# Example 2 — "Fully mapped" from the home page

## Before

```text
Discovery report (excerpt)
Method: crawled all links reachable from the home page.
Result: site fully mapped — 38 pages.
```

The sitemap for the same domain lists 112 URLs and the Wayback CDX index holds captures of 40 URLs the live site no longer serves. None were checked, so landing pages, archived-only pages, and JS-routed app screens are missing from the "complete" map — and nothing in the report shows they were ever looked for.

## After

```text
Discovery record (excerpt)
Sources: rendered crawl (96 URLs) · sitemap (112 URLs) · CDX matchType=domain
         (138 URLs) · analytics top pages (not provided by client — gap noted)
Reconciled total: 141 canonical URLs. Differences explained:
  - 42 CDX-only URLs: archived-only, live site returns 404 → tagged archived-only
  - 16 sitemap-only URLs: not linked from any page → orphan landing pages, in scope
  - 9 crawl-only URLs: JS-bundle routes (/app/*) absent from sitemap → tagged js-route
  - 3 sitemap URLs under /internal/: Disallow in robots.txt → recorded
    "excluded by robots", never fetched
G-CL-003: zero unexplained differences.
```

## Note

Violates CL-006 and CL-007 (the URL space is built from at least three independent sources and every cross-source difference is reconciled in writing); corrected by diffing crawl, sitemap, and CDX lists and explaining each difference instead of declaring a single-source crawl complete.
