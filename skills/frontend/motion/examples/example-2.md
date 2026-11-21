# Example 2 — A parallax hero gains its reduced-motion variant

## Before

```css
.hero-bg {
  background-image: url("/map-hero.jpg");
  background-attachment: fixed; /* parallax on scroll */
}
.hero-logo-marquee {
  animation: marquee 22s linear infinite;
}
```

Under `prefers-reduced-motion: reduce` emulation, both keep moving: the
background drifts against the scroll and the logo strip scrolls forever.
The media query appears nowhere in the stylesheet (DET-VIS-041) — the
user's OS-level request for calm is simply ignored.

## After

```css
.hero-bg {
  background-image: url("/map-hero.jpg");
  background-attachment: fixed;
}
.hero-logo-marquee {
  animation: marquee var(--duration-marquee) linear infinite;
}

@media (prefers-reduced-motion: reduce) {
  .hero-bg {
    background-attachment: scroll; /* static background */
  }
  .hero-logo-marquee {
    animation: none; /* logos rest in a static row, fully legible */
  }
  *, *::before, *::after {
    transition-duration: 0.01ms !important;
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
  }
}
```

Same commit, same pass (WCPM CR-09): parallax detached, the marquee
stopped with every logo still visible and readable, and transitions
collapsed to their end states. The Playwright reduced-motion pass
(G-FE-041) verifies the behavior, not just the presence of the block.

Note: corrects FE-085 — every animation ships with its reduced-motion variant designed in the same pass.
