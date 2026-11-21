# Example 3 — The audit: 1,200 entries, 214 bad claims

## Before

The sitemap lists 1,200 URLs and the launch report cites that number as
coverage. Nobody has ever requested the URLs it names. When a crawl is
finally run for a redesign, it finds 96 entries returning 404, 41 that
redirect to category pages, 65 parameter variants of pages already listed,
and 12 `noindex` landing pages — 214 entries claiming to be live,
canonical pages that are none of those things. Search Console's sitemap
report has been quietly showing errors the whole time; nobody owned them.

## After

The audit script runs in CI on every release. It fetches the sitemap,
requests every listed URL, and asserts 200, no redirect, a canonical tag
equal to the listed URL, and no `noindex`:

```
$ python3 scripts/sitemap_audit.py --sitemap https://example.com/sitemap.xml
1,200 URLs checked — 214 FAIL
  96 × HTTP 404
  41 × 301 → /category/…
  65 × canonical points to another URL (parameter variants)
  12 × meta robots: noindex
```

The failures trace back to the generator's filter, which is fixed to admit
only URLs the inventory marks live, indexable, and canonical — the entries
themselves are never hand-deleted. The next build's audit reads `1,041 URLs
checked — 0 FAIL`, and the count reconciles exactly with the inventory:
the 159 dropped entries are the dead, redirected, variant, and noindex
URLs, each named in the build log.

Note: corrects CO-182 — every sitemap entry is a claim that the URL returns 200, is indexable, and is its own canonical, and the audit script verifies that claim mechanically.
