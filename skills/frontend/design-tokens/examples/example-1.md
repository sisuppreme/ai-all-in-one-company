# Example 1 — Hard-coded values become semantic tokens

## Before

```css
/* PlanCard.module.css */
.card {
  background: #ffffff;
  border: 1px solid #e4e4e7;
  border-radius: 14px;
  padding: 22px;
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.1);
}
.card .price { color: #6d5df6; }
```

Every value is a one-off: 14px and 22px exist on no scale, `#6d5df6` is a
violet invented for this card, and the dark theme cannot reach any of it.
The next page invents its own set, and the site drifts.

## After

Token source (DTCG JSON, excerpt):

```json
{
  "color": {
    "surface": { "card": { "$value": "{color.neutral.0}", "$type": "color",
      "$description": "Background for card-level surfaces" } },
    "action": { "primary": { "$value": "{color.brand.600}", "$type": "color",
      "$description": "Primary action and price emphasis" } }
  },
  "radius": { "card": { "$value": "12px", "$type": "dimension",
    "$description": "Role: card — all card-level surfaces" } },
  "space": { "card-inset": { "$value": "24px", "$type": "dimension",
    "$description": "Internal padding for card-level surfaces" } }
}
```

Component, after transformation to CSS custom properties:

```css
.card {
  background: var(--color-surface-card);
  border: 1px solid var(--color-border-subtle);
  border-radius: var(--radius-card);
  padding: var(--space-card-inset);
  box-shadow: var(--elevation-card);
}
.card .price { color: var(--color-action-primary); }
```

The component names roles only. The literal lint (G-FE-022) now passes,
the dark theme overrides the semantic tier, and a future radius change is
one token edit reviewed as a diff.

Note: corrects FE-043 — components reference semantic tokens only; raw values in component styles are defects.
