# Example 2 — Transform mirroring replaced by `dir="rtl"`, and blanket icon flip replaced by the flip list

Violates/corrects AC-161, AC-164, AC-165: direction is declared on the root and never faked with transforms, and only the directional icons on the design-system flip list flip — semantic icons, logos, and media never do.

## Before

```css
/* "RTL support": flip the whole app and every icon in it */
[dir="rtl"] .app-shell {
  transform: scaleX(-1);
}
[dir="rtl"] svg {
  transform: scaleX(-1);
}
```

The shell flip mirrors text glyph-by-glyph in rendering, leaves focus and reading order running left-to-right, and the blanket `svg` rule also flips the logo, the clock icon, and the media play glyph.

## After

```html
<html lang="ar" dir="rtl">
```

```css
/* Direction comes from dir="rtl" + logical properties (see example-1).
   Only icons on the design-system flip list flip, via one utility: */
[dir="rtl"] .icon--directional {
  transform: scaleX(-1);
}
```

```html
<button class="back-button">
  <svg class="icon--directional" aria-hidden="true">…</svg> Back
</button>
<svg class="icon--clock" aria-hidden="true">…</svg>
<img class="logo" src="logo.svg" alt="Example Co.">
```

The back chevron (on the flip list) points toward inline-start in RTL; the clock icon and the logo render unmirrored on every screen, and G-AC-085 can diff the flipped set against the list exactly.
