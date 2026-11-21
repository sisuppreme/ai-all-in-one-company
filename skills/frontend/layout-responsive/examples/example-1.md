# Example 1 — Fixed-height hero that clips its CTA

## Before

```css
.hero {
  height: 100vh;
  padding: 6rem 1.5rem;
}
```

On a 667px-tall phone in landscape, or with a large browser toolbar, the fixed
height plus padding pushes the headline's last line and the signup button below
the fold — and because the height is fixed rather than a minimum, the button is
clipped outright on short screens.

## After

```css
.hero {
  min-height: 92svh;
  padding: 6rem 1.5rem 4rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
```

The hero now grows with its content: `min-height` gives the intended presence
on tall screens, and on short screens the section simply becomes taller than
the viewport instead of cutting off its own call to action.

Note: corrects FE-125 — heroes size to content with `min-height`; fixed heights that can clip text or CTAs are forbidden.
