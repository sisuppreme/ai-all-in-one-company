# Example 3 — Improvised timings become motion tokens

## Before

Motion values scattered across components, each invented on the spot:

```css
.card        { transition: transform .37s cubic-bezier(.2,.7,.3,1); }
.menu        { transition: opacity .5s ease; }
.modal       { animation: pop .22s cubic-bezier(.34,1.56,.64,1); }
.toast       { transition: all .45s ease-in-out; }
.tab-panel   { transition: opacity 180ms linear; }
```

Five components, five unrelated timings and curves — one menu drifts in
slowly, a modal bounces with an overshoot curve, a tab snaps linearly.
The interface feels like several products stitched together, and no
reviewer can say which value is "right".

## After

A small motion scale in the token source, consumed everywhere:

```json
{
  "duration": {
    "feedback": { "$value": "120ms", "$type": "duration",
      "$description": "Role: feedback — hovers, presses, toggles" },
    "move":     { "$value": "240ms", "$type": "duration",
      "$description": "Role: move — elements changing position or state" },
    "enter":    { "$value": "320ms", "$type": "duration",
      "$description": "Role: enter — overlays and panels arriving" }
  },
  "easing": {
    "standard": { "$value": "cubic-bezier(.2, 0, 0, 1)", "$type": "cubicBezier",
      "$description": "Role: standard — arrives once and stops; no overshoot" }
  }
}
```

```css
.card      { transition: transform var(--duration-move) var(--easing-standard); }
.menu      { transition: opacity var(--duration-feedback) var(--easing-standard); }
.modal     { animation: arrive var(--duration-enter) var(--easing-standard); }
.toast     { transition: transform var(--duration-move) var(--easing-standard),
                        opacity var(--duration-move) var(--easing-standard); }
.tab-panel { transition: opacity var(--duration-feedback) var(--easing-standard); }
```

The modal's bounce is gone (it arrives once, on the standard curve), and
the motion-token lint (G-FE-043) fails any new literal that tries to
sneak back in.

Note: corrects FE-082 — durations and easings come from the motion tokens; per-component improvisation is a defect.
