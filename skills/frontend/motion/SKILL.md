# motion

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** MDN, prefers-reduced-motion media query — https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion ; W3C WCAG 2.2 technique C39, Using the CSS reduce-motion query to prevent animation — https://www.w3.org/WAI/WCAG22/Techniques/css/C39.html
- **Depends on:** design-tokens
- **Feeds into:** scroll-experiences, webgl-3d, ui-states

## When to use / Do NOT use

- **Use when:** specifying, building, or reviewing any animation or transition — its purpose, its tokens, and its reduced-motion variant. WCPM's motion bans (M- working IDs), the CM cure family, and §7's motion rules land here; this skill designs to pass the WCPM G-MOT gate family.
- **Do NOT use when:** the motion is scroll-linked choreography (scroll-experiences), 3D scene motion (webgl-3d), or a state a view must communicate (ui-states — motion may present the state, it does not define it). Accessibility verdicts on motion belong to D13's reduced-motion skill; this skill implements them.

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

## BAN list

- **BAN-FE-041 — The global fade-up.** Banned: one scroll-triggered fade-and-rise applied to every section, same distance, same duration, same easing. Defeats: DET-VIS-040. Bad: a library default (`data-aos="fade-up"` on all 14 sections) makes the whole page bob upward in identical beats. Instead: content present by default; animation only where arrival carries information (FE-084). Severity: BLOCK.
- **BAN-FE-042 — Reduced motion ignored.** Banned: shipping animation with no `prefers-reduced-motion` handling, so parallax, auto-play, and scroll effects run unchanged for users who asked the OS for calm. Defeats: DET-VIS-041. Bad: a hero parallax and an auto-scrolling logo marquee keep moving under reduced-motion emulation; the string `prefers-reduced-motion` appears nowhere in the CSS. Instead: a reduce block per FE-085 — non-essential motion off, state changes rendered statically. Detection note: reduced-motion handling "planned for later" is this same defect — the reduce block is written in the same commit as the animation (FE-085); check the diff. Severity: BLOCK.
- **BAN-FE-043 — Improvised motion values.** Banned: durations and easing curves written per component (`transition: all .37s cubic-bezier(.2,.7,.3,1)` in one card, `.5s ease` in the next). Defeats: DET-VIS-040. Bad: seven components, seven unrelated timings; the interface feels like seven products. Instead: the motion tokens — a small set of named durations and curves consumed everywhere (FE-082). Severity: WARN.
- **BAN-FE-044 — Bounce and elastic easing on UI state changes.** Banned: springy overshoot curves on menus, modals, toggles, and other functional state changes. Defeats: DET-VIS-040. Bad: a settings dropdown bounces past its resting position twice before settling, on every open. Instead: a token easing that arrives once and stops; playfulness, where wanted at all, is confined to the one attention moment (FE-088). Severity: WARN.
- **BAN-FE-045 — Motion that gates content.** Banned: content that is invisible, collapsed, or unusable until an animation completes — including text split into spans that only assemble after a timed sequence. Defeats: DET-VIS-041. Bad: the hero headline renders word-by-word over 1.8s; a user on a slow device, or one who interrupts the tab, sees a partial sentence. Instead: the complete end state renders first; animation, if any, replays a change on top of readable content (FE-086). Severity: BLOCK.

## Gates

- **G-FE-041 — Reduced-motion emulation pass.** Verifies: FE-085, FE-086, FE-089. Check: automated — a Playwright pass with reduced-motion emulation over the main flows, asserting that flagged animations (parallax, auto-play, scroll-triggered) are disabled or absent and that every state change still reaches its end state. Pass: zero continuing non-essential animations; all end states legible. Fail: block shipment. Recorded in: progress.md.
- **G-FE-042 — Reduce-block presence check.** Verifies: FE-085. Check: automated — grep the shipped CSS for `prefers-reduced-motion`; if any animation or transition is defined and no reduce block exists, the check fails. Pass: reduce block present wherever animation is used. Fail: block shipment. Recorded in: progress.md.
- **G-FE-043 — Motion-token lint.** Verifies: FE-082, FE-083. Check: automated — the design-tokens literal lint extended to motion: duration/easing literals outside tokens fail, and a scan for animated layout properties (`transition-property` or keyframes touching `width`, `height`, `top`, `left`, margins) fails without a recorded exception. Pass: zero unexcused hits. Fail: block until tokenized or excepted in writing. Recorded in: progress.md.
- **G-FE-044 — Motion purpose review.** Verifies: FE-081, FE-084, FE-087, FE-088. Check: manual — DevTools rendering-emulation walk of the main flows: list every animation, name its purpose, count attention moments per view, and try to act during each transition. Pass: every animation has a named purpose, ≤ 1 attention moment per view, input never blocked. Fail: warn; block if input is blocked or content is gated. Recorded in: progress.md.

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
- Durations and easings are tokens, never improvisation.
- Transform and opacity only.
- Reduced-motion variant ships in the same pass (CR-09).
- Motion never blocks input or gates content.

## Checklist

- [ ] Every animation names its purpose: feedback, continuity, or the one attention moment (FE-081).
- [ ] No global entrance animation on sections (FE-084).
- [ ] All durations/easings resolve to motion tokens (G-FE-043).
- [ ] Only `transform` and `opacity` animate, or an exception is recorded (FE-083).
- [ ] Reduced-motion pass is green; end states legible without movement (G-FE-041).
- [ ] A `prefers-reduced-motion` block exists wherever animation is used (G-FE-042).
- [ ] Input works during every transition; feedback is immediate (FE-087).
- [ ] At most one attention moment per view (FE-088).
