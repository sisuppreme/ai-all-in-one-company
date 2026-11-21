# Example 1 — Reveal-from-hidden becomes visible-by-default enhancement

## Before

```css
.reveal {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity .6s ease, transform .6s ease;
}
.reveal.is-visible { opacity: 1; transform: none; }
```

```js
const io = new IntersectionObserver(es => es.forEach(e => {
  if (e.isIntersecting) e.target.classList.add('is-visible');
}));
document.querySelectorAll('.reveal').forEach(el => io.observe(el));
```

With JavaScript disabled, a blocked script, or an observer that never
fires, every `.reveal` section stays at `opacity: 0` forever — the page
is a series of blank viewports. The content's existence depends on an
animation completing.

## After

```css
/* Content renders in its final, visible state by default. */
.reveal { opacity: 1; transform: none; }

/* Enhancement only: when JS is available it adds the class `js` to
   <html>; the pre-reveal state exists solely under that gate, and the
   observer is created in the same script — if the script fails, the
   class is never added and nothing is hidden. */
.js .reveal.pre {
  opacity: 0;
  transform: translateY(24px);
}
.js .reveal.pre.is-visible {
  opacity: 1;
  transform: none;
  transition: opacity var(--duration-enter) var(--easing-standard),
              transform var(--duration-enter) var(--easing-standard);
}

@media (prefers-reduced-motion: reduce) {
  .js .reveal.pre { opacity: 1; transform: none; }
}
```

The failure modes invert: scripts blocked → fully visible page;
observer unsupported → the script's own feature check skips the `pre`
class; reduced motion → no hidden state at all. Visibility is the
default, animation the enhancement.

Note: corrects FE-101 — content is visible if the script or timeline never runs; reveal effects start from visible.
