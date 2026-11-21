# Example 3 — Monotone headings given a per-level scheme

## Before

```css
h1, h2, h3, h4 {
  text-transform: uppercase;
  font-weight: 600;
  letter-spacing: 0.02em;
}
h1 { font-size: 2rem; }
h2 { font-size: 1.75rem; }
h3 { font-size: 1.5rem; }
h4 { font-size: 1.25rem; }
```

Every level is the same voice at a slightly different volume: uppercase,
600-weight, tracked the same. A reader scanning the page cannot tell a section
heading from a card label by form — only by size, and barely.

## After

```css
h1 { /* display: sentence case, tight, heaviest */
  font: var(--type-display);
  font-weight: 700;
  letter-spacing: -0.01em;
}
h2 { /* section: sentence case, strong */
  font: var(--type-heading);
  font-weight: 650;
}
h3 { /* group: sentence case, medium */
  font: var(--type-title);
  font-weight: 600;
}
.eyebrow { /* labels only: uppercase, tracked out */
  font: var(--type-caption);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.12em;
}
```

Case and weight now carry meaning: display and section headings read as prose
titles, and the uppercase tracked style is reserved for the one job it suits —
short labels above headings — instead of being applied to everything.

Note: corrects FE-143 — case and weight vary by level and purpose; one pattern across all headings fails review.
