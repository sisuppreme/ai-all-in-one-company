# Example 1 — Parallax hero under reduced motion

## Before

The stylesheet carries a reduced-motion block that shortens CSS transitions, but the hero parallax is a JavaScript scroll listener, so it never sees the setting:

```js
window.addEventListener('scroll', () => {
  heroBg.style.transform = `translateY(${window.scrollY * 0.4}px)`;
});
```

```css
@media (prefers-reduced-motion: reduce) {
  * { transition-duration: 0.01ms !important; }
}
```

With reduced motion emulated, the CSS transitions stop but the background still slides at 40% of scroll speed — exactly the vestibular-risk pattern the user asked the OS to prevent.

## After

The JS animation reads the same signal as the CSS, subscribes to changes, and the global block replaces decorative animation with instant state changes:

```js
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
function applyParallax() {
  heroBg.style.transform = reduceMotion.matches
    ? 'none'
    : `translateY(${window.scrollY * 0.4}px)`;
}
window.addEventListener('scroll', applyParallax);
reduceMotion.addEventListener('change', applyParallax);
```

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
  html { scroll-behavior: auto !important; }
}
```

Under reduced motion the hero background is static and scrolling is instant; under no-preference the parallax runs as designed.

Note: demonstrates AC-101 and AC-103 — the OS setting governs JavaScript motion too, not only CSS.
