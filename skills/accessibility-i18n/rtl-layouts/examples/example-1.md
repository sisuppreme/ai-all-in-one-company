# Example 1 — Physical CSS converted to logical properties

Violates/corrects AC-162, AC-163: directional layout is written in CSS logical properties, and flex/grid are left to follow direction on their own.

## Before

```css
.card-actions {
  margin-left: auto;
  padding-right: 16px;
  text-align: left;
}
.step-icon {
  position: absolute;
  left: 0;
}
.toolbar {
  display: flex;
  flex-direction: row-reverse; /* added to "fix" RTL by hand */
}
```

Under `dir="rtl"` the card actions stay pinned to the physical left, the step icon overlaps the step title, and the hand-added `row-reverse` double-flips the toolbar once the physical properties elsewhere are corrected.

## After

```css
.card-actions {
  margin-inline-start: auto;
  padding-inline-end: 16px;
  text-align: start;
}
.step-icon {
  position: absolute;
  inset-inline-start: 0;
}
.toolbar {
  display: flex; /* row follows the inline direction automatically */
}
```

The same stylesheet now serves both directions: flipping `dir` on the root mirrors the layout, and the G-AC-081 physical-property scan reports zero findings for this component.
