# Example 3 — DOM-order stack recomposed by priority

## Before

```css
@media (max-width: 768px) {
  .product {
    display: flex;
    flex-direction: column; /* gallery, description, reviews, price, buy */
  }
}
```

The desktop layout is a two-column arrangement: gallery left; description,
reviews, price, and buy button right. Stacked in DOM order on mobile, the price
and buy button land after forty lines of description and the full review list —
the one thing a phone user came for is four scrolls away.

## After

```css
.product {
  display: grid;
  grid-template-areas:
    "gallery"
    "buybox"
    "description"
    "reviews";
}
@media (min-width: 60rem) {
  .product {
    grid-template-columns: 1.2fr 1fr;
    grid-template-areas:
      "gallery buybox"
      "gallery description"
      "reviews reviews";
  }
}
.gallery     { grid-area: gallery; }
.buybox      { grid-area: buybox; }      /* price + stock + buy button */
.description { grid-area: description; }
.reviews     { grid-area: reviews; }
```

Each breakpoint assigns its own order: on mobile the buy box follows the
gallery immediately, and description and reviews come after. The DOM stays in a
sensible reading order for assistive technology; the visual order is a layout
decision per width, not an accident of stacking.

Note: corrects FE-123 — mobile layouts are recomposed by priority, not stacked in desktop DOM order.
