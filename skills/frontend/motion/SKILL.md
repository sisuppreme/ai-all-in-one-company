# motion

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.1.0
- **Last verified:** 2026-11-23
- **Sources:** MDN, prefers-reduced-motion media query — https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion ; W3C WCAG 2.2 technique C39, Using the CSS reduce-motion query to prevent animation — https://www.w3.org/WAI/WCAG22/Techniques/css/C39.html
- **Depends on:** design-tokens
- **Feeds into:** scroll-experiences, webgl-3d, ui-states

## When to use / Do NOT use

- **Use when:** specifying, building, or reviewing any animation or transition — its purpose, its tokens, and its reduced-motion variant. WCPM's motion bans (M- working IDs), the CM cure family, and §7's motion rules land here; this skill designs to pass the WCPM G-MOT gate family.
- **Do NOT use when:** the motion is scroll-linked choreography (scroll-experiences), 3D scene motion (webgl-3d), or a state a view must communicate (ui-states — motion may present the state, it does not define it). Accessibility verdicts on motion belong to D13's reduced-motion skill; this skill implements them.

## The positive standard — what every build must ship

The bans below stop bad motion; they are not the design. Every build is expected to arrive with a complete, deliberate motion system (FE-091) in its theme's own material language — the rules in this skill exist so that system is crafted, safe, and fast, never so the page ships static and plain. A page with no motion system is as defective as a page with a banned one. Where an older restraint rule and this standard appear to conflict, the reading is: the *uniform, undesigned* version is banned (BAN-FE-041, FE-084, FE-088); the *designed, per-theme* version is required (FE-091, FE-092).

## Rules

1. **FE-081 — Every animation names its purpose.** Feedback (an action registered), continuity (a thing moved or changed state), or one deliberate moment of attention. "It looked empty" is not a purpose, and purposeless animation is deleted.
2. **FE-082 — Durations and easings are tokens.** Motion values come from the motion tokens in design-tokens (FE-045); a per-component improvised duration or curve is a defect found by the literal lint, not a style choice.
3. **FE-083 — Transform and opacity only.** Animation is restricted to `transform` and `opacity` so it stays on the compositor. Animating layout properties (`width`, `height`, `top`, margins) needs a written exception with a measured frame budget.
4. **FE-084 — Most content is simply present.** There is no global entrance animation. A fade-up applied to every section as it scrolls into view is forbidden (DET-VIS-040); entrances are reserved for elements whose arrival itself carries information.
5. **FE-085 — The reduced-motion variant is designed in the same pass.** For every animation, the `prefers-reduced-motion: reduce` behavior is specified alongside it (WCPM CR-09; W3C technique C39): parallax and auto-playing motion off, non-essential animation removed, state changes still legible without movement (DET-VIS-041).
6. **FE-086 — State changes remain legible without movement.** A user who receives no animation still sees what changed: the end state is complete and readable on its own. Motion explains a change; it never is the change's only record.
7. **FE-087 — Motion never blocks input.** No animation delays access to content or controls; a user can act during any transition, and interactive feedback begins effectively immediately — a button that waits for its ripple before responding has failed.
8. **FE-088 — One attention moment per view.** At most one element per view animates purely to draw the eye. Competing loops, pulses, and auto-playing carousels cancel each other and all are removed but one.
9. **FE-089 — Looping motion is rare and stoppable.** Any looping or auto-playing animation longer than a few seconds has a pause/stop control or stops under reduced motion (FE-085); nothing beside reading content moves forever.
10. **FE-090 — Cure, don't improvise.** A flagged motion pattern is fixed with the matching CM cure rule and the parameter it defeats (DET-VIS-040, DET-VIS-041) — recorded in the review, not replaced with a different untested effect.
11. **FE-091 — Every build ships a full motion system.** Not one effect: a system, designed per theme and present on every page of the build — scroll-triggered reveals; scroll-driven/scrubbed animation; parallax where depth serves the scene; pinned sections where they serve the story (scroll-experiences owns the scroll mechanics); staggered and masked/clip-path entrances; a choreographed hero entrance; kinetic typography; a marquee where in-theme; animated counters tied to real values; SVG line-drawing; image scale-in-frame; hover, magnetic, and 3D-tilt micro-interactions; skeleton/shimmer where data loads; page and section transitions; and ambient loops so no section ever feels dead. Each component is translated into the theme's own material language — the same technique in two themes must not look copy-pasted. A missing component needs a recorded reason ("not in-theme because…"), never silent absence. This rule is what FE-084 and FE-088 actually protect: entrances are required, but choreographed per section (varied distance, duration, mask, and order in the theme's style) — the banned thing is the identical library fade-up, not the entrance. Ambient loops are atmosphere, not attention moments: FE-088's one attention moment is the single element that *demands* the eye; quiet ambient life underneath it is required, not counted against it.
12. **FE-092 — The theme's signature elements are mandatory and merged.** Every page carries its theme's signature animated elements (specified in skills/frontend/theme-library/ — minimum 5, maximum 20 per theme) built INTO the content: a jar that fills as the reader finishes sections, a train that is the journey the timetable describes. An element that reads as pasted on top of the site — decorative, disconnected from the content it sits beside — is a defect of the same severity as a missing element. Test: remove the element mentally; if the content loses meaning, it is merged; if nothing changes, it is pasted.
13. **FE-093 — The cursor is the system cursor.** The normal OS cursor is the default and the expectation. A custom cursor is permitted only when it is feather-light: transform-only, driven by the page's single rAF loop (FE-095), with zero perceptible input lag, no physics that trails behind the pointer, and fully removed under reduced motion. A cursor that is heavy, laggy, or hard to move is a defect, not a flourish (BAN-FE-046). When in doubt, ship the system cursor.
14. **FE-094 — "Premium enough" is not done.** The bar is one level past the point where the build feels premium: when the motion system feels finished, do one more pass — detail inside the signature elements (secondary fissures, not single strokes; individual blink rhythms, not one sine), physics in the motion (eased, weighted, settling — never linear, never raw), and life in every section (no viewport the reader can rest in is completely still unless stillness is the theme's deliberate statement). A build that stops at "looks premium" has stopped one pass early.
15. **FE-095 — One loop, compositor only, capped counts.** All animation on a page is driven by a single `requestAnimationFrame` loop where feasible; per-effect timers and competing loops are a defect. Animation stays on `transform` and `opacity` (FE-083). Particle systems declare a capped count in the build notes and stay under it (a firefly field is tens, not thousands). Scroll-driven values are never applied raw — they are smoothed per scroll-experiences FE-111. The loop must hold frame budget on a mid-range device profile (FE-109's profiling discipline applies to all motion, not only scroll).
16. **FE-096 — Reveals can never strand content.** Any hidden start state is JS-gated: the hidden class is added by script, never present in shipped CSS/HTML, so with JS off the content is simply there. Every reveal carries a force-reveal fallback — a timeout (and re-trigger on re-entry) that lands the content in its final visible state even if its observer, timeline, or trigger never fires. A reveal that *can* leave content invisible is a build failure regardless of how it looks when it works (BAN-FE-047; scroll-experiences FE-112 owns the scroll case).
17. **FE-097 — The static variant is a designed page, not a broken one.** Under `prefers-reduced-motion`, the build delivers a complete static composition: signature elements present in their final states, counters at final values, state changes legible (FE-085, FE-086). Reduced motion removes movement, never content, meaning, or the theme's identity.

## BAN list

- **BAN-FE-041 — The global fade-up.** Banned: one scroll-triggered fade-and-rise applied to every section, same distance, same duration, same easing. Defeats: DET-VIS-040. Bad: a library default (`data-aos="fade-up"` on all 14 sections) makes the whole page bob upward in identical beats. Instead: content present by default; animation only where arrival carries information (FE-084). Severity: BLOCK.
- **BAN-FE-042 — Reduced motion ignored.** Banned: shipping animation with no `prefers-reduced-motion` handling, so parallax, auto-play, and scroll effects run unchanged for users who asked the OS for calm. Defeats: DET-VIS-041. Bad: a hero parallax and an auto-scrolling logo marquee keep moving under reduced-motion emulation; the string `prefers-reduced-motion` appears nowhere in the CSS. Instead: a reduce block per FE-085 — non-essential motion off, state changes rendered statically. Detection note: reduced-motion handling "planned for later" is this same defect — the reduce block is written in the same commit as the animation (FE-085); check the diff. Severity: BLOCK.
- **BAN-FE-043 — Improvised motion values.** Banned: durations and easing curves written per component (`transition: all .37s cubic-bezier(.2,.7,.3,1)` in one card, `.5s ease` in the next). Defeats: DET-VIS-040. Bad: seven components, seven unrelated timings; the interface feels like seven products. Instead: the motion tokens — a small set of named durations and curves consumed everywhere (FE-082). Severity: WARN.
- **BAN-FE-044 — Bounce and elastic easing on UI state changes.** Banned: springy overshoot curves on menus, modals, toggles, and other functional state changes. Defeats: DET-VIS-040. Bad: a settings dropdown bounces past its resting position twice before settling, on every open. Instead: a token easing that arrives once and stops; playfulness, where wanted at all, is confined to the one attention moment (FE-088). Severity: WARN.
- **BAN-FE-045 — Motion that gates content.** Banned: content that is invisible, collapsed, or unusable until an animation completes — including text split into spans that only assemble after a timed sequence. Defeats: DET-VIS-041. Bad: the hero headline renders word-by-word over 1.8s; a user on a slow device, or one who interrupts the tab, sees a partial sentence. Instead: the complete end state renders first; animation, if any, replays a change on top of readable content (FE-086). Severity: BLOCK.

- **BAN-FE-046 — The heavy custom cursor.** Banned: a custom cursor that lags, trails with physics the user must wait for, or makes the pointer feel hard to move. Defeats: DET-VIS-040. Bad: a drawn object chases the pointer with spring physics, arriving a beat late on every move; the user fights it across the whole page. Instead: the system cursor (FE-093); if a custom cursor ships at all, it is transform-only, on the single rAF loop, with zero perceptible lag, and gone under reduced motion. Severity: BLOCK.
- **BAN-FE-047 — The reveal that can strand content.** Banned: any reveal whose failure mode is invisible content — hidden states shipped in CSS/HTML rather than JS-gated, observers with no fallback timeout, triggers a fast scroll can skip with no re-entry. Defeats: DET-VIS-041. Bad: five section headings stay at `opacity: 0` forever because the smooth-scroll pass outran their observer and nothing re-checks them. Instead: FE-096 — JS-gated hidden states, force-reveal timeouts, re-trigger on re-entry, content complete with JS off. Severity: BLOCK.
- **BAN-FE-048 — The pasted-on element.** Banned: a signature or decorative animated element dropped onto a page without integration — it illustrates nothing, responds to nothing in the content, and could be deleted without the page losing meaning. Defeats: DET-VIS-040. Bad: a glowing jar floats in the corner of a pricing page whose sections never mention, fill, or interact with it. Instead: FE-092 — the element is built from and into the content (it fills, empties, travels, or reacts *because* of what the reader is doing in that content). Severity: WARN; BLOCK when it is the theme's primary signature element.

## Gates

- **G-FE-041 — Reduced-motion emulation pass.** Verifies: FE-085, FE-086, FE-089. Check: automated — a Playwright pass with reduced-motion emulation over the main flows, asserting that flagged animations (parallax, auto-play, scroll-triggered) are disabled or absent and that every state change still reaches its end state. Pass: zero continuing non-essential animations; all end states legible. Fail: block shipment. Recorded in: progress.md.
- **G-FE-042 — Reduce-block presence check.** Verifies: FE-085. Check: automated — grep the shipped CSS for `prefers-reduced-motion`; if any animation or transition is defined and no reduce block exists, the check fails. Pass: reduce block present wherever animation is used. Fail: block shipment. Recorded in: progress.md.
- **G-FE-043 — Motion-token lint.** Verifies: FE-082, FE-083. Check: automated — the design-tokens literal lint extended to motion: duration/easing literals outside tokens fail, and a scan for animated layout properties (`transition-property` or keyframes touching `width`, `height`, `top`, `left`, margins) fails without a recorded exception. Pass: zero unexcused hits. Fail: block until tokenized or excepted in writing. Recorded in: progress.md.
- **G-FE-044 — Motion purpose review.** Verifies: FE-081, FE-084, FE-087, FE-088. Check: manual — DevTools rendering-emulation walk of the main flows: list every animation, name its purpose, count attention moments per view, and try to act during each transition. Pass: every animation has a named purpose, ≤ 1 attention moment per view, input never blocked. Fail: warn; block if input is blocked or content is gated. Recorded in: progress.md.

- **G-FE-045 — Motion-system completeness check.** Verifies: FE-091, FE-092, FE-094. Check: manual + automated — walk every route against the FE-091 component list and the theme's signature-element spec (theme-library): each component is present and in-theme, or its absence has a recorded in-theme reason; each signature element passes the FE-092 removal test (content loses meaning without it); and the reviewer confirms the FE-094 extra pass happened (element detail, motion physics, per-section life). Pass: system complete, elements merged, extra pass evidenced. Fail: block shipment — a static page is not a neutral outcome. Recorded in: progress.md.
- **G-FE-046 — Cursor, loop, and budget audit.** Verifies: FE-093, FE-095, FE-096. Check: automated + manual — grep shipped code for cursor-follow implementations and count rAF loops (one per page, or recorded exceptions); profile the page on a mid-range CPU-throttled profile for frame budget with all ambient systems running; disable the reveal triggers (block IntersectionObserver) and assert every reveal still lands visible via its fallback timeout. Pass: system cursor or a feather-light exception, one loop, budget held, zero stranded reveals. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **The animation library as house style.** Installing an animation library and accepting its defaults as the product's motion language — the uniform fade-up is the signature. Catch it: if every entrance has the same distance and duration, the library decided, not the designer (BAN-FE-041).
- **Motion as apology.** Animation added to make a thin page feel substantial — reveals and parallax over content that says nothing. Catch it: remove the motion mentally; if the view is empty without it, the defect is content, not stillness.
- **Feedback theater.** Elaborate success animations that delay the next action — a 900ms checkmark flourish before the form unlocks. Catch it: time from click to usable next state; feedback that delays is a defect (FE-087).

## Examples

- [Example 1 — A global fade-up becomes selective, purposeful motion](examples/example-1.md) — corrects FE-084.
- [Example 2 — A parallax hero gains its reduced-motion variant](examples/example-2.md) — corrects FE-085.
- [Example 3 — Improvised timings become motion tokens](examples/example-3.md) — corrects FE-082.

## Recall anchors

- No purpose, no animation.
- Transform and opacity only.
- Reduced-motion variant ships in the same pass (CR-09).
- A full motion system ships on every page — designed per theme, never the library default.
- A reveal that can strand content invisible is a build failure.

## Checklist

- [ ] Every animation names its purpose: feedback, continuity, or the one attention moment (FE-081).
- [ ] No global entrance animation on sections (FE-084).
- [ ] All durations/easings resolve to motion tokens (G-FE-043).
- [ ] Only `transform` and `opacity` animate, or an exception is recorded (FE-083).
- [ ] Reduced-motion pass is green; end states legible without movement (G-FE-041).
- [ ] A `prefers-reduced-motion` block exists wherever animation is used (G-FE-042).
- [ ] Input works during every transition; feedback is immediate (FE-087).
- [ ] At most one attention moment per view (FE-088).
- [ ] Full motion system present on every page, each component in-theme or its absence justified in writing (FE-091, G-FE-045).
- [ ] Theme signature elements present and merged into the content (FE-092).
- [ ] System cursor, or a feather-light custom cursor with zero perceptible lag (FE-093).
- [ ] The FE-094 extra pass is done: element detail, motion physics, life in every section.
- [ ] One rAF loop drives the page; particle counts capped and declared (FE-095).
- [ ] Every reveal is JS-gated with a force-reveal fallback; blocking the observer strands nothing (FE-096, G-FE-046).
- [ ] Reduced-motion variant is a complete designed page, not a stripped one (FE-097).
