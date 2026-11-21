# Example 2 — Canvas-only product view given a real fallback

Corrects rules **FE-302** (build the fallback first) and **FE-304** (WebGL never gates content).

## Before

```html
<!-- The canvas is the only product view. If WebGL is blocked
     or the context fails, the section is an empty box and the
     color information exists nowhere else. BAN-FE-153. -->
<section class="product-view">
  <canvas id="viewer"></canvas>
  <script type="module">
    import { startViewer } from "./viewer.js";
    startViewer(document.getElementById("viewer")); // throws on no-WebGL devices
  </script>
</section>
```

## After

```html
<!-- Capability is checked first. Without WebGL, a designed
     still plus the same color information in markup renders
     instead — the message never depends on the canvas. -->
<section class="product-view">
  <figure id="viewer-fallback">
    <img src="/img/jacket-front.jpg"
         alt="Field jacket in rust red, front view, chest and cuff pockets visible">
    <figcaption>Field jacket — Rust Red. Also available in Forest and Sand.</figcaption>
  </figure>
  <canvas id="viewer" hidden
          role="img"
          aria-label="Interactive 3D view of the field jacket in rust red"></canvas>
  <script type="module">
    const canvas = document.getElementById("viewer");
    const gl = canvas.getContext("webgl2") || canvas.getContext("webgl");
    if (gl) {
      const { startViewer } = await import("./viewer.js");
      startViewer(canvas);
      canvas.hidden = false;
      document.getElementById("viewer-fallback").hidden = true;
    }
    // No context: the fallback figure simply stays. Nothing is lost.
  </script>
</section>
```

Note: the before version makes one browser capability the gatekeeper for the product's core information. The after version treats the 3D view as an enhancement over a complete static presentation — which is what gate G-FE-151 asserts with WebGL disabled.
