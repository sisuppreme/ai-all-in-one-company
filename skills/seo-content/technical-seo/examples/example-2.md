# Example 2 — Filter URLs indexed as duplicates

## Before

A catalog page generates a URL for every filter combination, and each one is
a full indexable page with a self-referencing canonical:

```
/products                  canonical: /products
/products?color=red        canonical: /products?color=red
/products?sort=price       canonical: /products?sort=price
/products?color=red&sort=price  canonical: /products?color=red&sort=price
```

Search Console shows all four indexed. The same products, the same text,
four competing URLs — and the engine picks a different one each week.

## After

Only the base URL is indexable. Every parameter variant canonicalizes to it:

```
/products?color=red&sort=price
  <link rel="canonical" href="https://example.com/products">
```

Combinations with no search value of their own also carry `noindex` as a
second line of defense. The route inventory crawl now asserts one canonical
URL per page, and Search Console's duplicate report drains as the variants
drop out of the index.

Note: corrects CO-006 — parameter and filter variants canonicalize to the base URL or carry noindex; they are never indexable duplicates.
