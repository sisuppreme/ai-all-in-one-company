# Example 2 — Wide table overflowing the page

## Before

```html
<table class="plans">
  <!-- 8 columns, natural width ~900px -->
</table>
```

```css
.plans { width: 100%; }
```

The table's content cannot compress below roughly 900px, so at 390px the whole
page scrolls sideways — the reader must pan horizontally to read anything,
including the text above and below the table.

## After

```html
<div class="table-scroll" tabindex="0" role="region" aria-label="Plan comparison, scrollable">
  <table class="plans">
    <!-- same 8 columns -->
  </table>
</div>
```

```css
.table-scroll {
  overflow-x: auto;
  max-width: 100%;
}
.plans th:first-child,
.plans td:first-child {
  position: sticky;
  left: 0;
  background: var(--surface);
}
```

The page no longer overflows; only the table's own region scrolls, the row
labels stay visible while scrolling, and the region is keyboard-focusable and
labeled so the contained scroll is discoverable.

Note: corrects FE-121 and FE-130 — wide content gets a contained scroll region; the page itself never scrolls horizontally.
