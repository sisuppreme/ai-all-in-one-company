# Example 2 — A janky scroll handler becomes a CSS view() timeline

## Before

```js
window.addEventListener('scroll', () => {
  document.querySelectorAll('.stat').forEach(el => {
    const r = el.getBoundingClientRect();      // layout read
    const p = 1 - r.top / window.innerHeight;
    el.style.transform = `translateY(${(1 - p) * 40}px)`;  // style write
    el.style.opacity = Math.max(0, Math.min(1, p));          // per event
  });
});
```

Every scroll event forces layout reads on nine elements interleaved
with style writes — read/write thrash on the main thread. On a
mid-range phone the Performance panel shows a chain of long tasks for
the entire scroll; the animation stutters exactly when the user is
moving.

## After

The same effect declared in CSS, driven by the compositor:

```css
.stat {
  animation: stat-in linear both;
  animation-timeline: view();
  animation-range: entry 0% entry 60%;
}
@keyframes stat-in {
  from { opacity: 0; transform: translateY(40px); }
  to   { opacity: 1; transform: translateY(0); }
}

@media (prefers-reduced-motion: reduce) {
  .stat { animation: none; }
}
```

No JavaScript, no scroll events, no layout reads: the browser runs the
timeline off the main thread. Where `view()` is unsupported, the
designed degradation applies — the stats are simply present, statically
(FE-108). The scroll-handler scan (G-FE-053) now finds nothing to flag.

Note: corrects FE-102 — scroll effects use CSS scroll-driven animations or IntersectionObserver, never per-frame scroll handlers.
