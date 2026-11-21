# Example 1 — The 4 MB hero video that "looked fine on the office connection"

## Before

The launch status report carries a performance line written from a single desktop lab run:

```text
Performance: Lighthouse 98 — LCP 1.1 s. Site is fast.
```

The homepage hero is a 4 MB autoplay video. On the office fiber connection it paints instantly, so nobody questions the line. The first field report tells a different story: mobile LCP p75 on the home template is 5.8 s, and the hero video is the LCP element for most mobile visits. Real users were failing for weeks behind a green lab score.

## After

The status report quotes field data, and the lab is demoted to diagnosis:

```text
Home template, field p75 (28-day, mobile): LCP 5.8 s — POOR (threshold ≤ 2.5 s)
Home template, field p75 (28-day, desktop): LCP 2.2 s — good
LCP element (mobile): hero video. Defect AN-232 #perf-14 opened.
Lab (throttled mobile profile): reproduces LCP 5.4 s; dominant subpart =
resource load duration — the video itself.
Fix: poster frame as the LCP element, video compressed and deferred;
field verdict due after the next window.
```

Note: the Before violates AN-221 (field data is the verdict; a lab score is never reported as the user experience); the After corrects it.
