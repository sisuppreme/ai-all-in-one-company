# Example 2 — Auto-advancing carousel with no pause control

## Before

A testimonials carousel starts on page load, advances every four seconds, and offers only dot indicators:

```html
<div class="carousel" data-autoplay="4000">
  <div class="slide">…testimonial 1…</div>
  <div class="slide">…testimonial 2…</div>
  <div class="slide">…testimonial 3…</div>
  <div class="dots">● ○ ○</div>
</div>
```

A user reading a slide has it replaced mid-sentence, with no way to stop the rotation — and it behaves identically under `prefers-reduced-motion: reduce`.

## After

The carousel ships a visible pause/play control, never auto-starts under reduced motion, and remains fully navigable by buttons in both modes:

```html
<div class="carousel" data-autoplay="4000">
  <button class="carousel-pause" aria-pressed="false">Pause slides</button>
  <div class="slide">…testimonial 1…</div>
  <div class="slide">…testimonial 2…</div>
  <div class="slide">…testimonial 3…</div>
  <button class="carousel-prev">Previous testimonial</button>
  <button class="carousel-next">Next testimonial</button>
</div>
```

```js
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
let timer = null;
function startAutoplay() {
  if (reduceMotion.matches || timer) return; // never auto-start under reduced motion
  timer = setInterval(nextSlide, 4000);
}
pauseBtn.addEventListener('click', () => {
  clearInterval(timer); timer = null;
  pauseBtn.textContent = 'Play slides';
  pauseBtn.setAttribute('aria-pressed', 'true');
});
startAutoplay();
```

Under reduced motion the first slide simply sits still until the user chooses to move; in full-motion mode the rotation is one click away from stopped.

Note: demonstrates AC-105 — auto-playing content is pausable in every mode and does not auto-start under reduced motion.
