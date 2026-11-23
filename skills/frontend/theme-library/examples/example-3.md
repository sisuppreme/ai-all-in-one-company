# Example 3 — The stranding reveal, fixed with the spec's watchdog pattern

Corrects rules **FE-347** (every reveal has a watchdog fallback) and **FE-348** (the reduced-motion variant ships in the same pass); BAN-FE-174 is the banned form.

## Before

A themed build ships with its section headings held at opacity 0 until an IntersectionObserver fires. On a fast scroll — and for every visitor whose script stalls — several headings never appear: the page shows handsome empty sections and reads as broken. With reduced motion emulated it is worse: the reveal code is skipped entirely, so the pre-hidden states are never released and half the page is missing. The animation worked in the demo and strands content in the world.

## After

The build is reworked to the pattern every expanded spec already defines. Content ships complete in the DOM (FE-346); scripts may *arm* a pre-state only on elements they will animate, and each armed element carries the spec's named watchdog — a timeout that forces the final, visible state if the trigger path fails, stalls, or is interrupted. Re-entry re-triggers the reveal; a completed reveal never re-hides. The reduced-motion variant is built in the same pass: final states, full content, no loops — the same page, still. Gate G-FE-173 drills all three passes (JS disabled, reduced motion, maximum-speed scroll) before the page may ship.
