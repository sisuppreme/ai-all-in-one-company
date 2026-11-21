# reduced-motion

## Metadata

- **Owner department:** D13 Accessibility & i18n (AC)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** WCAG 2.2 criteria 2.2.2, 2.3.1, 2.3.3, W3C — https://www.w3.org/TR/WCAG22/ ; `prefers-reduced-motion`, MDN — https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion
- **Depends on:** wcag (this skill operationalizes its motion criteria)
- **Feeds into:** accessibility-audit, accessibility-testing, motion, scroll-experiences

## When to use / Do NOT use

- **Use when:** A product contains any motion — scroll animations, parallax, carousels, auto-playing media, page transitions, animated counters or charts — and needs a reduced-motion behavior for each, plus the normative motion floors (flash, pause/stop) verified before release.
- **Do NOT use when:** Designing the motion itself (motion and scroll-experiences own the design; this skill constrains it), running the full conformance evaluation (accessibility-audit), or judging non-motion visual criteria such as contrast (wcag).

## Rules

1. **AC-101 — The OS setting is an instruction, not a hint.** `prefers-reduced-motion: reduce` is a user instruction delivered through the operating system. When it is set, every non-essential animation in the product is removed or replaced; no component, page, or third-party embed may opt out individually.
2. **AC-102 — One global CSS block neutralizes decorative motion.** A single global `@media (prefers-reduced-motion: reduce)` block disables decorative `@keyframes` animation and transitions (or reduces them to instant state changes / short crossfades) and turns off smooth scrolling (`scroll-behavior: auto`). Per-component overrides of this block are defects.
3. **AC-103 — JavaScript motion checks the same signal.** JS-driven motion — scroll listeners, IntersectionObserver animations, canvas/WebGL loops, animation libraries, animated counters — reads `window.matchMedia('(prefers-reduced-motion: reduce)')` before starting and subscribes to its change event, so a mid-session OS change takes effect without a reload. CSS coverage alone is not coverage.
4. **AC-104 — Inventory every motion, assign each a behavior.** Before release, the motion inventory lists every animated element (scroll reveals, parallax, carousels, auto-playing media, page transitions, counters, loading animations) with its reduced-motion behavior: remove, replace with an instant change, replace with a crossfade, or gate behind explicit user activation. An unlisted animation is an unreviewed animation.
5. **AC-105 — Auto-playing media is pausable in every mode.** Any video, carousel, or animated image that starts automatically and lasts more than five seconds ships with a visible pause/stop control, in reduced-motion mode and in full-motion mode alike (WCAG 2.2.2). Under reduced motion, auto-play does not start at all; the user starts it deliberately or not at all.
6. **AC-106 — Nothing flashes above the threshold.** No content flashes more than three times in any one-second period (WCAG 2.3.1). This applies to video, animated images, ad slots, and transition effects, and it applies in every motion mode — reduced-motion settings are not the control for seizure risk.
7. **AC-107 — Animation is never the only carrier of meaning.** Every state change an animation shows — step completed, item added, error arrived, progress advanced — also changes text, an icon, or an ARIA state, so the change is fully communicated when the animation is removed. If deleting the animation deletes information, the design fails this rule.
8. **AC-108 — Essential motion stays minimal and vestibular-safe.** Motion that is itself the information (a progress indicator, a map zoom the user drives) may remain under reduced motion, reduced to the minimum: no parallax, no zooming or panning of large screen areas, no spinning, no motion that simulates camera movement through space.
9. **AC-109 — Interaction-triggered animation can be disabled.** Non-essential animation triggered by interaction (hover effects, click ripples, animated route transitions) is disabled under reduced motion, per WCAG 2.3.3 — adopted as department practice even though the criterion is AAA and the baseline is AA.
10. **AC-110 — New motion is justified like new copy.** A design review that adds motion states, in the same ticket, what the motion communicates and its reduced-motion equivalent from AC-104's behavior list. Motion with no stated purpose is removed, not accommodated.
11. **AC-111 — Reduced motion never removes function.** The reduced-motion experience completes every task the full-motion experience completes, in the same number of steps: content revealed by scroll animation is present without the animation, carousel slides are reachable without auto-advance, and nothing waits on an animation finishing to become usable.
12. **AC-112 — Third-party embeds are in scope.** Embedded players, chat widgets, ad slots, and social feeds are checked under reduced-motion emulation like first-party code. An embed that cannot honor the setting is replaced, wrapped behind explicit user activation, or recorded as a finding with the vendor named — never silently shipped.

## BAN list

- **BAN-AC-051 — CSS-only reduced-motion coverage.** Banned: shipping a `@media (prefers-reduced-motion: reduce)` block while JavaScript-driven parallax, scroll animations, or animated counters keep running untouched. Defeats: DET-VIS-041. Bad: stylesheet disables CSS transitions under reduced motion, but the hero parallax is a scroll listener and still moves the background at full speed. Instead: gate every JS animation on `matchMedia('(prefers-reduced-motion: reduce)')` per AC-103 and verify under emulation per G-AC-051. Severity: BLOCK.
- **BAN-AC-052 — Auto-play with no pause control.** Banned: auto-playing video, carousels, or animated heroes that start on load and offer no visible pause/stop control, in any motion mode. Defeats: DET-VIS-041. Bad: a hero carousel auto-advances every four seconds with dot indicators as the only control. Instead: ship a visible pause button per AC-105, and under reduced motion do not auto-start or auto-advance at all. Severity: BLOCK.
- **BAN-AC-053 — Flashing content above the WCAG threshold.** Banned: any content — video, animated image, ad creative, transition effect — that flashes more than three times in one second. Defeats: DET-NONE — no DET parameter names this signal; pattern owned by this skill. Bad: a promotional banner strobes its background color six times per second to draw the eye. Instead: remove the strobe; draw attention with a static badge or a single slow crossfade, and run the flash check in G-AC-052 before publication. Severity: BLOCK.
- **BAN-AC-054 — Animation as the only signal of a state change.** Banned: communicating a completed action, error, or progress change solely by animation, with no text, icon, or ARIA change. Defeats: DET-UX-011. Bad: adding an item flies a thumbnail to the cart icon and nothing else changes — with animation off, the user gets no confirmation at all. Instead: pair the animation with a persistent signal per AC-107 (cart count text updates, a polite live-region announcement, a visible confirmation). Severity: BLOCK.
- **BAN-AC-055 — One global scroll animation applied to everything.** Banned: a single library-default fade-up (or equivalent) applied uniformly to every section on scroll, with no per-element purpose and no reduced-motion removal. Defeats: DET-VIS-040. Bad: 90% of sections share the identical 600ms fade-and-rise, including under reduced-motion emulation. Instead: animate selectively where motion explains a change (AC-110), and remove scroll reveals entirely under reduced motion per AC-102/AC-104. Severity: WARN.

## Gates

- **G-AC-051 — Reduced-motion emulation run (automated).** Verifies: AC-101, AC-102, AC-103, AC-104. Check: run the primary flows in Playwright with `reducedMotion: 'reduce'` emulation (or browser devtools emulation), with a script asserting no element on each primary page has a running CSS animation or auto-playing media, and grep the built CSS/JS for the media query and for animation entry points lacking a `matchMedia` gate. Pass: zero non-essential animations running and zero un-gated animation entry points. Fail: block shipment. Recorded in: progress.md.
- **G-AC-052 — Flash and pause-control check (automated + manual).** Verifies: AC-105, AC-106. Check: scripted DOM pass asserting every auto-playing `video`/`carousel` element has an associated visible pause/stop control; manual/tool-assisted flash review of every video and animated image before publication, counting flashes per second. Pass: every auto-playing element is pausable and no content exceeds three flashes per second. Fail: block shipment. Recorded in: progress.md.
- **G-AC-053 — Reduced-motion task walk (manual).** Verifies: AC-107, AC-111. Check: with reduced motion emulated, complete each primary process end to end and confirm every state change is communicated by text, icon, or ARIA state, and every task completes in the same number of steps as in full-motion mode. Pass: a dated walk record lists each primary process as pass/fail with no missing-signal findings. Fail: block shipment. Recorded in: progress.md.
- **G-AC-054 — Motion inventory complete.** Verifies: AC-104, AC-110, AC-112. Check: diff the motion inventory against the shipped build's animated components (from the G-AC-051 scan output); confirm every shipped animation, including third-party embeds, has an inventory row with an assigned reduced-motion behavior. Pass: zero shipped animations missing from the inventory. Fail: block shipment. Recorded in: progress.md.
- **G-AC-055 — Full-motion regression check.** Verifies: AC-102, AC-108. Check: with `prefers-reduced-motion: no-preference`, load the primary pages and confirm intended animations still run and essential indicators (progress, loading) still animate; then re-check that essential motion under `reduce` contains no parallax, large-area zoom/pan, or spinning. Pass: full-motion experience intact, essential motion vestibular-safe in both modes. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Media query as decoration.** A `prefers-reduced-motion` block exists in the CSS, so the team believes the work is done — but it only shortens transition durations while parallax and auto-play continue. Catch it by running G-AC-051's emulation scan instead of reading the stylesheet.
- **Duration-zero hacks.** Setting every `animation-duration` to `0.01ms` globally and calling it reduced motion, which breaks animation-dependent state (elements stuck mid-state, end events the code waits on). Catch it by completing G-AC-053's task walk: functions that depended on the animation finishing are now visibly broken.
- **Reduced means removed content.** Under reduced motion, scroll-reveal sections never appear because the reveal class was the only thing making them visible. Catch it in G-AC-053: content that requires an animation to exist fails AC-111.
- **Settings-page substitute.** Adding an in-app "reduce animations" toggle while ignoring the OS setting, so users who already declared the preference at OS level must find and set it again per product. Catch it by checking the build reads the media query itself (AC-101) — a toggle may supplement the OS setting, never replace it.

## Examples

- [Example 1 — Parallax hero under reduced motion](examples/example-1.md) — violates/corrects AC-101, AC-103.
- [Example 2 — Auto-advancing carousel with no pause control](examples/example-2.md) — violates/corrects AC-105.
- [Example 3 — State change carried by animation alone](examples/example-3.md) — violates/corrects AC-107.

## Recall anchors

- The OS setting is an instruction, not a hint.
- CSS coverage alone is not coverage — gate the JavaScript too.
- Auto-play always ships a pause; under reduced motion it never starts.
- Three flashes per second is the ceiling, in every mode.
- If removing the animation removes information, the design fails.

## Checklist

- [ ] Motion inventory lists every animation, including third-party embeds, with an assigned reduced-motion behavior (AC-104).
- [ ] Global CSS block neutralizes decorative animation and smooth scrolling under `prefers-reduced-motion: reduce` (AC-102).
- [ ] Every JS-driven animation checks `matchMedia('(prefers-reduced-motion: reduce)')` and reacts to changes (AC-103).
- [ ] Emulation run passes: no non-essential animation or auto-play active under reduced motion (G-AC-051).
- [ ] Every auto-playing element has a visible pause/stop control in both modes (AC-105).
- [ ] Flash check passed on all video and animated content — never more than three flashes per second (AC-106).
- [ ] Reduced-motion task walk confirms every state change is signaled without animation and every task completes (AC-107, AC-111, G-AC-053).
