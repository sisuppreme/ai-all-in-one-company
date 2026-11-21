# Example 1 — Rating markup with no reviews on the page

Demonstrates CO-166 (review markup follows real reviews) and BAN-CO-083.

## Before

The product page renders a description, a price, and a buy button. There is no review section — the business has no reviews yet. The template still emits:

```json
{
  "@type": "Product",
  "name": "Trailhead Insulated Bottle",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "212"
  }
}
```

The 4.8 / 212 figures were copied from a competitor's page during scaffolding. No user has ever reviewed this product.

## After

The `aggregateRating` block is removed entirely. The template emits rating markup only when the page's data contains real reviews that are rendered visibly on the same page:

```json
{
  "@type": "Product",
  "name": "Trailhead Insulated Bottle",
  "offers": {
    "@type": "Offer",
    "price": "34.00",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock"
  }
}
```

When genuine reviews exist and are displayed, the template generates `aggregateRating` from that same review data — same values, same page.

Note: corrects CO-166 — review and rating markup exists only where real, visible reviews exist.
