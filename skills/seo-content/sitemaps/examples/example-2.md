# Example 2 — Every lastmod is the deploy date

## Before

The sitemap generator stamps each entry from the build clock:

```xml
<url>
  <loc>https://example.com/terms</loc>
  <lastmod>2026-11-21</lastmod>
</url>
```

Every nightly deploy rewrites all 8,000 `lastmod` values to that day's
date — including the terms page, unchanged for two years, and blog posts
from 2023. The file claims the entire site changed last night, every
night. Crawlers learn the dates are noise and stop trusting them, so
genuinely updated pages get no freshness benefit either.

## After

The generator reads `lastmod` from each content record's own change
timestamp — the CMS field set when an editor actually saves the page:

```xml
<url>
  <loc>https://example.com/terms</loc>
  <lastmod>2024-09-03</lastmod>
</url>
<url>
  <loc>https://example.com/pricing</loc>
  <lastmod>2026-11-19</lastmod>
</url>
```

Pages whose source has no reliable change date (a few legacy imports)
omit `lastmod` entirely rather than carrying an invented one. The spot-check
gate samples 25 entries against the content records each release; a
mismatch is fixed in the generator, never by editing the XML.

Note: corrects CO-185 — `lastmod` is the date the content last changed, taken from the content record, and omitted when that date is not known.
