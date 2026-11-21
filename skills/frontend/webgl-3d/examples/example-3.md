# Example 3 — Always-on render loop replaced by a visibility-gated, DPR-capped loop

Corrects rules **FE-305** (cap resolution, scale quality) and **FE-306** (render only when visible; handle context loss).

## Before

```js
// Renders at full device pixel ratio, forever — including when
// the canvas is scrolled offscreen or the tab is hidden — and
// a lost context leaves a frozen frame with no recovery.
const renderer = new THREE.WebGLRenderer({ canvas });
renderer.setPixelRatio(window.devicePixelRatio); // uncapped: 3x on flagship phones

function tick() {
  requestAnimationFrame(tick);
  controls.update();
  renderer.render(scene, camera);
}
tick();
```

## After

```js
// DPR is capped, rendering pauses when the canvas is offscreen,
// and context loss swaps in the fallback instead of freezing.
const renderer = new THREE.WebGLRenderer({ canvas });
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

let visible = true;
new IntersectionObserver(([entry]) => { visible = entry.isIntersecting; })
  .observe(canvas);

canvas.addEventListener("webglcontextlost", (event) => {
  event.preventDefault();
  document.getElementById("viewer-fallback").hidden = false;
  canvas.hidden = true;
});
canvas.addEventListener("webglcontextrestored", () => {
  document.getElementById("viewer-fallback").hidden = true;
  canvas.hidden = false;
});

function tick() {
  requestAnimationFrame(tick);
  if (!visible || document.hidden) return; // no work for an unseen scene
  controls.update();
  renderer.render(scene, camera);
}
tick();
```

Note: the before loop spends battery and GPU on frames nobody sees and dies silently on context loss. The after version renders only a visible scene, at a capped resolution, and degrades to the designed fallback — the behavior FE-305 and FE-306 require.
