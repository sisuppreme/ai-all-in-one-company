# webgl-3d

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** MDN, Getting started with WebGL — https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Tutorial/Getting_started_with_WebGL ; inherited Web Craft Pro Max §3.6 GL tells (GL-01…GL-05), rules R-7.6-1…R-7.6-4, and gates G-VIS-09 / G-MOT-10, mapped in docs/WCPM_MAPPING.md
- **Depends on:** motion, frontend-core
- **Feeds into:** scroll-experiences, ui-states

## When to use / Do NOT use

- **Use when:** a page includes a WebGL or 3D scene — product viewers, configurators, data globes, 3D heroes — or a 3D library (Three.js, Babylon.js) is being introduced.
- **Do NOT use when:** the visual is achievable in 2D (CSS, SVG, canvas 2D) at equal clarity — 2D wins by default and this skill's budgets do not apply; or the motion is ordinary UI animation (motion owns it).

## Rules

1. **FE-301 — Use a maintained library.** Build on Three.js or Babylon.js; raw WebGL is written only with a recorded justification (size, a narrow fixed pipeline), never by default.
2. **FE-302 — Build the fallback first.** Before the scene ships, check for a usable WebGL context; where WebGL is unavailable or the device cannot sustain the frame budget, render a designed static image or content equivalent (inherited R-7.6-2; gate G-MOT-10). The fallback is a designed still, not a blank.
3. **FE-303 — Zero GL tells.** The scene carries none of the §3.6 tells at P0/P1 (gate G-VIS-09): GL-01 ambient-only flat lighting, GL-02 uniform plastic materials, GL-03 dead-center default camera, GL-04 abstract blob decoration, GL-05 no shadows or default tone mapping. Lighting has a key light and a shadow side; materials vary; the camera is chosen, not defaulted.
4. **FE-304 — WebGL never gates content.** Every 3D scene has a fallback that conveys the same information or product view. If removing the canvas removes the message, the design is wrong.
5. **FE-305 — Cap resolution, scale quality.** Device pixel ratio is capped, and quality (pixel ratio, shadow size, geometry detail) scales to device capability before frame rate collapses — not after.
6. **FE-306 — Render only when visible, survive context loss.** The render loop pauses when the canvas is offscreen or the tab is hidden, and `webglcontextlost` / `webglcontextrestored` are handled explicitly — a lost context restores the scene or the fallback, never a frozen frame.
7. **FE-307 — Reduced motion stops camera motion.** Auto-rotation and camera animation stop under `prefers-reduced-motion: reduce`; user-controlled motion (drag, scroll-driven) remains available (inherited CR-09).
8. **FE-308 — The canvas is accessible.** It carries a text alternative describing what it shows, and any control the scene exposes is reachable and operable by keyboard.
9. **FE-309 — Verify the frame budget on a low-end device.** Frame rate is profiled on a low-end phone, not the development machine; the scene holds its budget there with quality scaling engaged.
10. **FE-310 — Respect the weight and settle budgets.** 3D assets stay ≤500 KB before first interaction, streaming progressively after it, and a camera intro settles within 1.5 s (inherited R-7.6-4, R-7.6-1). A full-screen WebGL hero that delays primary content fails the frontend-core performance review unless explicitly justified.

## BAN list

- **BAN-FE-151 — Abstract 3D blob hero.** Banned: an abstract 3D blob, torus, or fluid shape as hero decoration with no relationship to the product (tell GL-04, P0). Defeats: DET-VIS-028. Bad: a chrome torus slowly rotating beside the headline of an invoicing tool. Instead: show the product, or use a 2D visual that carries the page's actual message (FE-304). Severity: BLOCK.
- **BAN-FE-152 — The engine-default scene.** Banned: shipping a scene lit by one white ambient light, built from one stock material, shot from the default centered camera (tells GL-01, GL-02, GL-03). Defeats: DET-VIS-023. Bad: a product viewer where the shoe floats, shadowless, in flat gray plastic light. Instead: a key light with shadows, materials matched to the real surfaces, and a deliberate camera (FE-303). Detection note: a stock Three.js example with the demo object swapped for the product is this same defect; the GL-01/02/03 tells (flat light, plastic material, centered camera) are its fingerprint. Severity: BLOCK.
- **BAN-FE-153 — WebGL-only content.** Banned: content or product information that exists only inside the canvas, with no fallback. Defeats: DET-VIS-032. Bad: the only view of the product's color range is the 3D configurator; with WebGL blocked, the page shows an empty box. Instead: the fallback still plus the same information in markup (FE-302, FE-304). Severity: BLOCK.
- **BAN-FE-154 — Motion that ignores reduced-motion.** Banned: auto-rotating scenes or animated camera moves that run under `prefers-reduced-motion: reduce`. Defeats: DET-VIS-041. Bad: the hero product spins continuously for a user who has asked their system for stillness. Instead: a static default view under reduced motion; motion only on user control (FE-307). Severity: BLOCK.

## Gates

- **G-FE-151 — WebGL-disabled fallback run.** Verifies: FE-302, FE-304. Check: automated — Playwright launched with WebGL disabled (browser flag) loads every page containing a canvas; assert the fallback element is visible and the page's message is present in markup. Pass: fallback renders on every 3D page. Fail: block shipment. Recorded in: progress.md.
- **G-FE-152 — GL-tell inspection.** Verifies: FE-303. Check: manual — walk the rendered scene against GL-01…GL-05: key light and shadow side present, materials varied and surface-appropriate, camera deliberate, shadows and tone mapping on, no abstract decoration. Pass: 0 tells at P0/P1 (gate G-VIS-09). Fail: block shipment. Recorded in: progress.md.
- **G-FE-153 — Low-end frame profile.** Verifies: FE-305, FE-309. Check: manual — profile the scene on a low-end phone (or throttled equivalent): sustained frame rate holds the project's budget with quality scaling engaged, and the render loop pauses when the canvas leaves the viewport. Pass: budget held for a full interaction session. Fail: warn, fix before release. Recorded in: progress.md.
- **G-FE-154 — Reduced-motion emulation check.** Verifies: FE-307. Check: automated — Playwright with `prefers-reduced-motion` emulated loads the scene; assert no auto-rotation or camera animation runs, and the static view still shows the product. Pass: scene is still and complete. Fail: block shipment. Recorded in: progress.md.

## Intelligence — decisions & gates

> **Judgment layer.** These decisions apply the judgment layer above this skill — `skills/frontend/design-intelligence/SKILL.md` and the theme library (`skills/frontend/theme-library/`). Settle the theme's art direction there first, then decide here inside it; where a decision below and a rule above disagree, the rule above wins.

### Decision rules — placing 3D

| Decision | Read the situation | Decide |
|---|---|---|
| Whether 3D at all | Whether a photograph or 2D graphic conveys the same thing at equal clarity | If it does, ship 2D. 3D earns its place for inspection (rotate, zoom), configuration, or genuinely spatial data — nothing else. |
| Interactivity level | The audience's task | Shoppers configuring a product: full orbit plus live variants. Casual visitors: a constrained, well-chosen presentation with optional drag. Data stories: a guided camera the user can take over. |
| Realism budget | What the scene must prove | Commerce: the product must look like itself — materials taken from its real surfaces. Editorial or data: stylized rendering is acceptable when it stays honest about what it represents. |
| Performance tier | The audience's actual devices | Mobile-heavy or emerging-market audience: aggressive DPR caps and low-poly defaults. Desktop professional audience: higher fidelity — with quality scaling still engaged (FE-305). |
| Camera behavior | The content's job | Product viewer: user-controlled, damped, angle-limited — never under the floor. Hero: one slow, deliberate move that settles within 1.5s (FE-310). |
| Fallback investment | How much traffic may lack WebGL | The larger that share (old devices, locked-down browsers), the more art direction the fallback still deserves — it is a designed image, not an apology (FE-302). |
| Lighting and materials | The product's real context | Light and surround the scene as the product is actually met — studio, desk, street — never a void with a floating object (FE-303). |

### Self-check gate

- **G-FE-155 — Pre-ship intelligence self-check (WebGL/3D).** Verifies: FE-302, FE-303, FE-304, FE-305, FE-307, FE-309 as judgment, not just compliance. Check: manual — the builder scores each item pass/fail on the shipped scene: (1) ★ with WebGL disabled, the page still delivers its full message through the fallback; (2) ★ the delete test passes — removing the canvas would remove information or capability, not just decoration; (3) a low-end profile holds the frame budget with quality scaling engaged; (4) the rendered scene shows zero GL tells — key light with a shadow side, surface-true materials, a chosen camera; (5) under reduced-motion emulation the camera is still and the view complete; (6) the render loop pauses offscreen and a lost context restores the scene or the fallback, never a frozen frame. Pass: both ★ items pass and at least 5 of 6 overall. Fail: fix, or log a written exception, before shipping. Recorded in: progress.md.

### Anti-pattern table — symptom → cause → fix

| Symptom | Cause | Fix |
|---|---|---|
| Effect pasted over content — a 3D scene floats beside copy it has no relationship to | 3D was added as decoration after the page was designed | The scene must carry its section's message and sit inside the layout's structure; if removing it loses nothing, remove it (FE-304, BAN-FE-151). |
| Performance collapse — 60fps in the demo, under 20fps on the audience's phones | Profiled only on the development GPU; DPR uncapped; geometry heavier than the scene needs | Cap DPR, scale quality to capability, and profile on a low-end device (FE-305, FE-309, G-FE-153). |
| No fallback — WebGL blocked or unsupported leaves an empty box | The fallback was treated as optional polish and cut under deadline | Build the fallback first (FE-302) and prove it with the WebGL-disabled run (G-FE-151). |
| Engine-default look — flat light, plastic materials, dead-center camera | A starter example shipped with the demo object swapped for the product | Key light with shadows, materials matched to real surfaces, a deliberate camera (FE-303, BAN-FE-152). |
| Battery bonfire — the scene renders all day in background tabs and offscreen | The render loop never checks visibility | Pause offscreen and when hidden; render on demand where the scene allows it (FE-306). |
| Motion-sickness camera — swooping auto-orbits and fly-throughs nobody asked for | Camera animation used as default ambience | Settle within 1.5s, then hand control to the user; reduced motion means still (FE-307, FE-310). |
| Context-loss freeze — a GPU reset leaves a frozen frame on the page forever | `webglcontextlost` and `webglcontextrestored` were never handled | Handle both events explicitly: restore the scene or fall back, never freeze (FE-306). |
| Canvas as a black box — screen readers get nothing and keyboard users can't reach the controls | The canvas was treated as pure decoration | Text alternative describing the scene, and keyboard-operable controls (FE-308). |

## Anti-patterns

- **The dev-machine demo.** The scene is buttery on the author's GPU laptop and a slideshow on a mid-range phone. Catch it: if no low-end profile exists, FE-309 was skipped — the demo proves nothing.
- **The perpetual loop.** `requestAnimationFrame` rendering an unchanged scene all day, draining battery on a background tab. Catch it: if the loop never checks visibility, FE-306 was skipped.
- **The screenshot fallback.** The "fallback" is a blurry screenshot of the scene with none of the scene's information. Catch it: compare fallback and scene side by side; the fallback must convey the same information (FE-304), not the same pixels.

## Examples

- [Example 1 — Engine-default scene replaced by a lit, material-true scene](examples/example-1.md) — corrects FE-303.
- [Example 2 — Canvas-only product view given a real fallback](examples/example-2.md) — corrects FE-302 and FE-304.
- [Example 3 — Always-on render loop replaced by a visibility-gated, DPR-capped loop](examples/example-3.md) — corrects FE-305 and FE-306.

## Recall anchors

- Fallback first: no WebGL, no problem.
- Zero GL tells — key light, real materials, chosen camera.
- 3D never gates content.
- Reduced motion means the camera stops.
- Profile on the worst phone, not your machine.

## Checklist

- [ ] WebGL context check and designed fallback in place (FE-302).
- [ ] WebGL-disabled Playwright run passes on every 3D page (G-FE-151).
- [ ] GL-tell inspection: 0 tells at P0/P1 (G-FE-152).
- [ ] DPR capped; quality scaling verified on a low-end device (FE-305, G-FE-153).
- [ ] Render loop pauses offscreen; context loss handled (FE-306).
- [ ] Reduced-motion emulation: no auto-rotation, static view complete (G-FE-154).
- [ ] Canvas has a text alternative; scene controls are keyboard-operable (FE-308).
- [ ] Pre-interaction 3D weight ≤500 KB; camera intro settles ≤1.5 s (FE-310).
