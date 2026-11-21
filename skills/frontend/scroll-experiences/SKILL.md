# scroll-experiences

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** MDN, Scroll-driven animation timelines (scroll() and view()) — https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines ; CSS Scroll-Driven Animations Module Level 1 (specification) — https://drafts.csswg.org/scroll-animations/
- **Depends on:** motion, layout-responsive
- **Feeds into:** frontend-core

## When to use / Do NOT use

- **Use when:** building or reviewing anything tied to scroll position — reveal choreography, parallax, progress indicators, pinned sections. This skill owns the scroll half of WCPM §7 and designs to pass the scroll-related G-MOT gates; the general motion system (tokens, purposes, reduced-motion variants) is owned by motion and assumed here.
- **Do NOT use when:** the animation is a state change or micro-interaction (motion), the scene is 3D (webgl-3d), or the real question is whether the content should exist (content skills). If the page reads perfectly with every scroll effect deleted, that is the correct baseline — this skill only adds on top of it.

## Rules

1. **FE-101 — Content is visible if nothing runs.** Every section renders fully visible with JavaScript disabled, with the animation timeline unsupported, and before any observer fires. Reveal effects start from visible and enhance; content is never hidden by CSS alone waiting for a script to rescue it.
2. **FE-102 — Platform mechanisms only.** Scroll effects are built with CSS scroll-driven animations (`animation-timeline: scroll()` / `view()`) or IntersectionObserver. Per-frame `scroll` event handlers doing layout work are forbidden.
3. **FE-103 — No scroll-jacking.** The user's scroll position, direction, and speed are never overridden: no forced snapping through content, no hijacked wheel or touch handling, no auto-advance. The scrollbar remains the user's.
4. **FE-104 — Reduced motion turns scroll effects off.** Parallax and scroll-linked animation are disabled under `prefers-reduced-motion: reduce`, inheriting motion's variant discipline (FE-085, WCPM CR-09); the static page underneath is complete (DET-VIS-041).
5. **FE-105 — Choreography paces a story; it never gates reading.** Scroll effects may sequence genuinely sequential content (a process, a timeline, a build-up). Any text the user needs must be reachable by ordinary scrolling at the user's pace — never locked behind a completed animation.
6. **FE-106 — Progress is never only decorative.** A scroll progress indicator is optional ornament. Position and progress through a document are communicated by structure (headings, landmarks, a table of contents where warranted), never solely by a progress bar.
7. **FE-107 — Pinned sections respect focus.** Sticky and pinned elements must not trap keyboard focus or obscure the focused element (WCAG 2.4.11 focus-not-obscured); a pinned header shrinks or yields rather than covering the focus target.
8. **FE-108 — Degradation is designed, not discovered.** Browser support for scroll-driven animations is uneven, so the unsupported-browser experience is specified in advance: content simply present, statically laid out. "Simply present" is a designed state, not a broken one (FE-101 makes it safe by construction).
9. **FE-109 — Scroll performance is measured.** A full-page scroll is profiled for long tasks and layout thrash on a mid-range device profile; scroll-linked work that produces jank is simplified or removed, not shipped and hoped for.

## BAN list

- **BAN-FE-051 — Reveal-from-hidden content.** Banned: sections styled `opacity: 0` (or translated off-view) in CSS, revealed only when JavaScript adds a class — so no-JS, a failed script, or an unsupported timeline leaves a blank page. Defeats: DET-VIS-040. Bad: `.reveal { opacity: 0; transform: translateY(24px); }` with the visible state applied by an IntersectionObserver callback; with scripts blocked, the page is five empty viewports. Instead: render visible by default and let the observer add an *enhancement* (or animate from visible states only), per FE-101. Severity: BLOCK.
- **BAN-FE-052 — Scroll-jacking.** Banned: overriding the user's scroll — snapping forcibly between sections, translating wheel input into custom animation, or auto-scrolling the reader through content. Defeats: DET-VIS-037. Bad: a marketing page that captures wheel events and animates one full screen per tick, so a trackpad user lurches past the pricing details they were trying to read. Instead: native scrolling, always; choreography rides on the user's scroll position, never replaces it (FE-103). Severity: BLOCK.
- **BAN-FE-053 — Parallax with no off switch.** Banned: parallax layers or scroll-linked motion that continue under `prefers-reduced-motion: reduce`. Defeats: DET-VIS-041. Bad: three background layers drifting at different rates keep drifting in reduced-motion emulation; no reduce block exists. Instead: parallax disabled under the reduce query, layers resting in a complete static composition (FE-104). Severity: BLOCK.
- **BAN-FE-054 — The clipping pinned hero.** Banned: a pinned or `100vh` hero section whose foreground text or CTA is clipped or overlapped on short or narrow viewports while the pin holds. Defeats: DET-VIS-039. Bad: at 360×640 the pinned hero's CTA sits half under the following section for the first 400px of scroll, unreachable and unreadable. Instead: heroes sized to content with `min-height` (layout-responsive, DET-VIS-039 discipline), pins tested at 360×640 and 1280×600 before they ship. Severity: BLOCK.
- **BAN-FE-055 — The per-frame scroll handler.** Banned: `window.addEventListener('scroll', …)` code that reads layout and writes styles on every event, producing jank on mid-range devices. Defeats: DET-VIS-040. Bad: a handler calling `getBoundingClientRect()` on nine elements and setting transforms per scroll event; the profiler shows a chain of long tasks through the whole page. Instead: a CSS `view()` timeline or an IntersectionObserver with a passive, rAF-throttled fallback (FE-102). Severity: WARN.

## Gates

- **G-FE-051 — No-JS visibility pass.** Verifies: FE-101, FE-105, FE-108. Check: automated — Playwright loads every route with JavaScript disabled and asserts each section's text is present and visible in the rendered page. Pass: all content visible on all routes. Fail: block shipment. Recorded in: progress.md.
- **G-FE-052 — Reduced-motion scroll pass.** Verifies: FE-104. Check: automated — Playwright with reduced-motion emulation scrolls the full page and asserts parallax layers are static and no scroll-linked animation is running. Pass: zero scroll-linked motion under emulation. Fail: block shipment. Recorded in: progress.md.
- **G-FE-053 — Scroll-handler scan.** Verifies: FE-102. Check: automated — grep shipped scripts for `addEventListener('scroll'` / `onscroll`; any hit requires a recorded exception proving the handler does no per-frame layout work. Pass: zero unexcused hits. Fail: warn; block if the handler touches layout. Recorded in: progress.md.
- **G-FE-054 — Scroll profile and pin inspection.** Verifies: FE-107, FE-109. Check: manual — DevTools Performance recording of a full-page scroll on a mid-range CPU-throttled profile, checking for long tasks tied to scroll; plus a focus walk through pinned sections at 360×640 and 1280×600 screenshots. Pass: no scroll-linked long tasks; focus never obscured; no clipped hero content. Fail: block until simplified or unpinned. Recorded in: progress.md.

## Anti-patterns

- **The demo scroll.** A page built to impress in a screen recording: pinned scenes, scrubbed animations, choreographed everything — and miserable to actually read. Catch it: read the page as a user, top to bottom, at your own speed; friction you feel is the defect (FE-105).
- **Invisible until proven.** Content whose visibility depends on an observer threshold that some viewport sizes never trigger, leaving a permanent blank gap mid-page. Catch it: the no-JS pass (G-FE-051) plus a slow scroll at an unusual viewport height.
- **Progress bar as wayfinding.** A thin progress bar is the only indication of where the reader is in a long document. Catch it: remove the bar mentally — if position is now unknowable, the structure failed (FE-106).
- **Pin accumulation.** Each redesign pins one more element — header, toolbar, summary card — until the content column is a slit. Catch it: measure the unobstructed content height at 640px viewport height at review; pins compete for one budget.

## Examples

- [Example 1 — Reveal-from-hidden becomes visible-by-default enhancement](examples/example-1.md) — corrects FE-101.
- [Example 2 — A janky scroll handler becomes a CSS view() timeline](examples/example-2.md) — corrects FE-102.
- [Example 3 — A clipping pinned hero becomes a content-sized hero](examples/example-3.md) — corrects FE-107 (via BAN-FE-054).

## Recall anchors

- Visible if nothing runs — enhancement only adds.
- CSS timelines or IntersectionObserver; never per-frame handlers.
- The scrollbar belongs to the user.
- Reduced motion: scroll effects off, page complete.
- Pins never trap or cover the focused element.

## Checklist

- [ ] Full page readable with JavaScript disabled (G-FE-051).
- [ ] No per-frame scroll handlers doing layout work (G-FE-053).
- [ ] No scroll-jacking: native position, direction, and speed throughout (FE-103).
- [ ] Parallax and scroll-linked motion off under reduced motion (G-FE-052).
- [ ] Progress never communicated by a progress bar alone (FE-106).
- [ ] Pinned elements never obscure the focused element (FE-107).
- [ ] Scroll profile shows no scroll-linked long tasks (G-FE-054).
- [ ] Unsupported-browser experience is the designed static page (FE-108).
