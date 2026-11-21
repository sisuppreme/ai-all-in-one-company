# Example 1 — Per-type cache headers

## Before

One CDN default TTL is applied to every response:

```text
GET /            -> Cache-Control: max-age=86400
GET /app.js      -> Cache-Control: max-age=86400
GET /account     -> Cache-Control: max-age=86400   (authenticated page, publicly cached)
```

After a deploy, some users get the new HTML with yesterday's `app.js`, and an authenticated page sits in the shared cache.

## After

Cache policy is set per content type, and asset URLs are fingerprinted:

```text
GET /                     -> Cache-Control: max-age=0, must-revalidate
GET /assets/app.9f31c2.js -> Cache-Control: public, max-age=31536000, immutable
GET /account              -> Cache-Control: private, no-store
```

The deploy ships new fingerprints, so old and new assets never mix on one page.

Note: demonstrates DO-182 and DO-183 — per-type cache policy with versioned assets and designed invalidation.
