# Example 3 — A clipping pinned hero becomes a content-sized hero

Render spec for the same hero at two viewports, before and after.

## Before

```css
.hero {
  height: 100vh;          /* fixed to the viewport */
  position: sticky; top: 0; /* pinned while the next section slides over */
}
```

| Viewport | Result |
|---|---|
| 1440×900 | Looks fine — the demo screenshot size. |
| 360×640 | Headline wraps to 4 lines; the CTA sits half beneath the following section for the first 400px of scroll — visible in slices, never clickable (DET-VIS-039). |
| 1280×600 | The subtext is clipped by the fold; keyboard focus on the CTA is hidden under the pinned hero's own image layer. |

The hero was sized to a screenshot, not to its content.

## After

```css
.hero {
  min-height: min(88vh, 720px);  /* a floor, never a cage */
  padding-block: var(--space-hero-y);
  position: relative;            /* no pin */
}
.hero:focus-within { z-index: 1; } /* focused content never covered */
```

| Viewport | Result |
|---|---|
| 1440×900 | Same visual weight; the hero still fills most of the first screen. |
| 360×640 | The hero grows to fit the wrapped headline and CTA; everything is reachable by ordinary scrolling. |
| 1280×600 | Nothing clips; tabbing to the CTA shows it fully, outline visible. |

Verified in the pin-inspection gate (G-FE-054): screenshots at 360×640
and 1280×600, plus a keyboard focus walk, before the page ships.

Note: corrects FE-107 via BAN-FE-054 — pinned and fixed-height heroes must never clip content or obscure the focused element at any viewport.
