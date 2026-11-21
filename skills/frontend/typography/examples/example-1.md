# Example 1 — Flat arbitrary sizes replaced by a token scale

## Before

```css
.hero-title    { font-size: 26px; }
.section-title { font-size: 22px; }
.card-title    { font-size: 17.5px; }
.body-text     { font-size: 15px; }
.fine-print    { font-size: 13px; }
```

Five sizes chosen by eye, all within a few pixels of each other. The hero title
is barely larger than a card title, so nothing on the page reads as the main
message — a flat scale with no hierarchy.

## After

```css
:root {
  --type-display:  clamp(2.75rem, 6vw, 4rem) / 1.05;  /* 44–64px */
  --type-heading:  1.75rem / 1.2;                     /* 28px */
  --type-title:    1.25rem / 1.3;                     /* 20px */
  --type-body:     1rem / 1.6;                        /* 16px */
  --type-caption:  0.8125rem / 1.45;                  /* 13px */
}
.hero-title    { font: var(--type-display); }
.section-title { font: var(--type-heading); }
.card-title    { font: var(--type-title); }
.body-text     { font: var(--type-body); }
.fine-print    { font: var(--type-caption); }
```

Every size is now a named scale step with its line-height, the display size is
2.75× body at minimum, and a new size can only appear by adding a step with a
role to the scale itself.

Note: corrects FE-141 and FE-142 — sizes come only from the type scale, and the largest heading is dramatically larger than body.
