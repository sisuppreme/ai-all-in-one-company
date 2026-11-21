# Example 3 — Markup price disagrees with the page and checkout

Demonstrates CO-167 (prices match everywhere) and BAN-CO-084.

## Before

The store raises the bottle's price from $29 to $34 in the CMS. The visible page and checkout update. A hard-coded JSON-LD block in the template footer — maintained separately, by hand — does not:

```json
{
  "@type": "Product",
  "name": "Trailhead Insulated Bottle",
  "offers": {
    "@type": "Offer",
    "price": "29.00",
    "priceCurrency": "USD",
    "priceValidUntil": "2026-01-31"
  }
}
```

Search results show $29; the page and checkout charge $34. The markup contradicts the site (DET-CON-015) and the price source (DET-CON-016).

## After

The hand-maintained block is deleted. The product template reads price and sale end date from the same product record that renders the page and feeds checkout, so one edit updates all three surfaces in the same commit:

```json
{
  "@type": "Product",
  "name": "Trailhead Insulated Bottle",
  "offers": {
    "@type": "Offer",
    "price": "34.00",
    "priceCurrency": "USD"
  }
}
```

The markup-vs-visible diff (G-CO-082) now asserts price equality on every build.

Note: corrects CO-167 — markup price, page price, and checkout price are one value from one source.
