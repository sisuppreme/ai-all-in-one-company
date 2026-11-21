# Example 2 — An unchecked amber pair becomes a passing token pair

## Before

A pricing page puts its "Most popular" tier on an amber panel:

```css
.tier-featured { background: #e8a33d; }
.tier-featured p { color: #ffffff; }
```

Chosen by eye, never measured. Computed contrast of white on `#e8a33d`
is ≈ 2.2:1 — far below the 4.5:1 floor for body text (DET-VIS-022). The
panel looks warm in a screenshot and is unreadable for many users.

## After

The pair is treated as a token decision, not a styling hunch:

1. The contrast script (G-FE-023) rejects `text-on-signal` as proposed.
2. The surface deepens and the foreground switches to the ink token:
   - `color-surface-signal`: `#c07f1f` (deepened amber)
   - `color-text-on-signal`: `#1c2430` (the system's ink)
   - Computed ratio ≈ 5.4:1 — admitted to the token set with the ratio
     recorded in the token's `$description`.
3. The component consumes the pair by name:

```css
.tier-featured {
  background: var(--color-surface-signal);
  color: var(--color-text-on-signal);
}
```

Any future change to either value re-runs the script; a failing pair
cannot be named, so it cannot ship.

Note: corrects FE-046 — a semantic foreground/background pair is admitted only after its WCAG ratio is computed and passes.
