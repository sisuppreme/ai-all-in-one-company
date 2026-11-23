# OmniForge — Repo-First Protocol (Claude Code)

Add this file's contents to the project's `CLAUDE.md` (or paste it at the start of a session) whenever a project is built with the OmniForge skill repository. It is a procedure to run at the start of every task, not background reading.

## Repository

- Repo: https://github.com/sisuppreme/ai-all-in-one-company (placeholder URL until the repo is published — use this exact address until the user provides the final one).
- Pinned version: OmniForge repo v1.2.0 (2026-11-23).

## At the start of every task

1. Clone the repo, or `git pull` your existing clone, at the start of every task — always work from the repo's current state, never from a stale local copy or from memory. Read `VERSION` and the top entry of the repo's root `CHANGELOG.md` and compare with the pin above. If the repo's version is **newer** than the pin, the repo wins: these instructions are stale, but do not stop and do not ask permission — follow the repo's current `BOOTSTRAP.md`, rebuild your picture of the skill set from the current `SKILLS_INDEX.md` (new skills and playbooks may exist since the pin; discover them from the index, never assume the set named anywhere in these instructions is complete), load bundles from the current repo, and tell the user once, briefly, that the repo has been updated to the new version and you are using the new files. If the version matches the pin or is older, proceed normally; if the repo is more than 6 months old, warn the user and re-verify tool and API claims against live sources. Note the version in the project's `progress.md` (step 5).
2. Read `BOOTSTRAP.md` in full — it is the entry point.
3. Scan `SKILLS_INDEX.md` by department section and Keywords; identify the task's departments. Do not read every entry.
4. Load only the relevant skills fully, plus the always-on core: `project-templates` + `progress-tracking` (D10), `secrets-management` (D7), `qa-gates` (D8). If the task matches a playbook type, load that playbook bundle from `bundles/`; otherwise load the matching department bundles. Honor each skill's `Depends on` field. Never load `bundles/ALL_SKILLS.md` whole — it is a human reference artifact only.
5. Docs before code: create `requirements.md`, `stack.md`, `progress.md`, `fact-sheet.md` first — no code before these exist. Record the repo version at the top of `progress.md`. Vague requirements bounce back to the user as questions.
6. Run the loaded skills' gates as you work; record every gate result in `progress.md` with evidence (command output, test result, screenshot). A gate without evidence is not passed. If two loaded skills conflict, apply the repo's precedence order (§5.7) and log the conflict in the project's `DECISIONS.md`.
7. Keep `progress.md` updated. Stop for user approval after requirements, before deployment, and before go-live.

Multi-session projects: the step 1 pull and version check runs at the start of every session. If the repo changed mid-project, note it in `progress.md` and adopt new or changed skills for work not yet done; do not retroactively rewrite completed, gate-passed work unless a changed gate affects safety, legal, or Real Content, in which case re-check the affected work against the new gate.

Small-task fast path: a single-file fix or one-skill task skips the full bootstrap — load the one skill and its gates, update `progress.md`.

## Fallback

If the repo cannot be fetched, say so explicitly — never silently rely on a stale clone, on memory, or on an old paste. Ask the user to paste the **current** `bundles/core.md` from the repo (plus the playbook bundle for the task, if one applies), warn that pasted content may be older than the repo itself, proceed with the pasted bundles only, and flag the gap in `progress.md`. Do not improvise unloaded skills.

## UI/UX skills — compulsory, not optional

For any task that creates or changes a user interface, the OmniForge UI/UX skill set MUST be loaded and applied — every time, in full. It is never skipped for speed, for a small task, or via the small-task fast path:

- The frontend theme library (`skills/frontend/theme-library/`) — pick one theme and apply its full system (concept, palette, typography, full motion system, signature animated elements).
- `design-intelligence`, `design-system`, `design-tokens`, `typography`, `layout-responsive`, `component-library`, `ui-states`, `motion`, and `scroll-experiences` — plus `webgl-3d` when the chosen theme calls for it.
- Before any UI work is called done, run the `design-intelligence` quality gate and record its result in `progress.md` with the other gates.

The ONLY exception: the user explicitly says not to use these skills — for that task, or as a standing instruction. Silence, a tight deadline, or a small change is not an opt-out.

## Design standard — every website UI

Any task that builds a website UI is held to the OmniForge premium design standard:

- Before building any website UI, load the frontend theme library (`skills/frontend/theme-library/`) and pick a theme. Apply the theme's full system — its concept, palette, typography, full motion system, and its signature animated elements — not just its colours.
- The `motion` and `scroll-experiences` skills' positive premium standard applies in full on every page.
- Standing rules: use the normal system cursor only (heavy custom cursors are banned); reveals can never leave content invisible — every reveal needs a fallback, and the page stays readable with JavaScript disabled; built elements (jars, trains, instruments, any themed object) must be merged with the site's content, never pasted on top of it; scroll-driven motion is smoothed (requestAnimationFrame lerp, no jitter); `prefers-reduced-motion` is honoured.
- The bar is "premium beyond premium": when a design feels finished, push it one step further. A merely standard-looking site is a failed build.

## Rules that always apply

- You work alone: never claim a multi-agent handoff is needed or wait for another agent; department labels are roles you play sequentially yourself.
- Real Content Rule: never invent content, data, people, reviews, statistics, or functionality — if something is not verified, say so.
- Never ask for secrets in chat; secrets go in the project's environment or secret store and are referenced by name only (see the repo's `secrets-management` skill).

---

<!-- OMNIFORGE EMBEDDED UI/UX SKILL PACK: START — the full UI/UX + theme skill set follows inside this file. It is compulsory (see the rule at its top). -->

# OmniForge UI/UX + Theme Skill Pack — EMBEDDED, COMPULSORY

Everything below this line is part of these instructions. It is the full text of
the OmniForge UI/UX skill set and the 100-theme library, embedded here so it
applies even where the repository itself cannot be fetched.

COMPULSORY RULE: for any task that creates or changes a user interface, this
pack MUST be applied — every time, in full. Pick one theme from the theme
library and apply its full system (concept, palette, typography, full motion
system, signature animated elements). Follow the design-intelligence, motion,
and scroll-experiences standards on every page. The ONLY exception: the user
explicitly says not to use these skills. Silence, a tight deadline, or a small
change is not an opt-out.

Contents of this pack:
- design-intelligence (art-direction decisions + quality gate)
- motion (premium motion standard)
- scroll-experiences (premium scroll standard)
- design-system, design-tokens, typography, layout-responsive,
  component-library, ui-states, webgl-3d
- Theme library: 100 fully detailed themes (001-100), each with concept,
  palette, typography, full motion system and 8-12 signature animated
  elements merged with the site's content.


---

<!-- BEGIN EMBEDDED: Skill: design-intelligence — source: skills/frontend/design-intelligence/SKILL.md -->

# design-intelligence

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-23
- **Sources:** skills/frontend/theme-library/ — the 150-theme catalog and its 10 living reference demos (themes #3, #41, #63, #76, #92, #105, #124, #132, #149, #150), each demo reviewed against real user verdicts 2026-11-23; WCPM §2 parameter catalog (DET-VIS-001…044) and G-DES-01 rubric, served by design-system.
- **Depends on:** design-system, theme-library, motion, scroll-experiences
- **Feeds into:** frontend-core, layout-responsive, component-library, typography

## When to use / Do NOT use

- **Use when:** a page, site, or theme application must be *decided*, not just built — choosing a theme from the theme-library, setting layout and motion intensity, composing sections, judging whether an animated element belongs, adapting one theme across product types, or scoring a finished page before it ships. This skill is the judgment layer: design-system governs the system, motion and scroll-experiences supply technique, theme-library supplies the worlds; this skill decides which, how much, and whether it worked.
- **Do NOT use when:** the question is a token value (design-tokens), a component's internals (component-library), a single animation's implementation (motion), or a DET-VIS parameter lookup (design-system). Intelligence chooses; those skills execute the choice.

## Rules

1. **FE-321 — Decide before designing.** Every build opens with a recorded decision set: theme (from theme-library), layout family, motion-intensity dial level, colour posture, typography posture — produced by the decision system in §1, plus at least one named alternative that was rejected and why. A build that starts by opening an editor has already failed; the decision record is checked at G-FE-161.
2. **FE-322 — Audience trust outranks brand ego.** When decision inputs conflict, resolve in this order: (1) the audience's task and trust, (2) the content's truth, (3) brand personality, (4) the builder's taste. A spectacle choice that costs a cautious audience its trust is wrong no matter how good it looks in a screenshot.
3. **FE-323 — The dial is set once, by content type.** Motion intensity is one dial per page (§1.3), set from content type and audience before building — never tuned section-by-section on taste. Changing the dial mid-build requires a written reason in the decision record.
4. **FE-324 — One focal point per viewport.** At any scroll position exactly one element is loudest, and it wins clearly (§2). Two elements competing for first attention is a composition defect, not a style.
5. **FE-325 — Pacing is composed, not accumulated.** Sections alternate dense and quiet by plan (§2.4). A page assembled by stacking equally loud sections has no rhythm and reads as noise at any quality level.
6. **FE-326 — Every technique has a job.** Each animation technique on the page names the job it does from the motion-judgment table (§3). A technique that cannot name its job is removed, however well it is implemented.
7. **FE-327 — Signature elements must carry content.** A theme's signature animated elements pass the merge test (§3.3): remove the element and the page must lose information or story, not just decoration. An element that fails is pasted-on spectacle (BAN-FE-162), whatever it cost to build.
8. **FE-328 — Spectacle is budgeted.** At most one spectacle moment per three viewport heights of scroll; inside task flows (forms, checkout, tools, dashboards) restraint wins by default and the dial drops (§3.2). Spectacle is spent where the visitor came to feel or decide, never where they came to finish.
9. **FE-329 — Score before shipping.** The finished page is scored on the self-critique gate (§5 / G-FE-162) by the builder acting as its own harshest reviewer. Below threshold means: fix the lowest category first, re-score the whole page, and only then ship. Shipping below threshold "to fix later" is banned (BAN-FE-163).
10. **FE-330 — Diagnose slop by symptom.** When a page feels like AI slop, do not restyle on instinct: find the symptom in the anti-slop table (§4), apply its stated fix, and re-check. Each symptom's fix is cheaper and more reliable than a redesign.
11. **FE-331 — Adapt the theme, never abandon it.** One theme serves many product types by bending dial, layout family, and pacing (§6) — its material language (palette roles, type pairing, element vocabulary) stays intact. Switching themes per page type produces a site with no identity.
12. **FE-332 — Reasoning is recorded.** Each shipped build leaves its decision trail — brief → choices → why → what was rejected — in the project's progress record, in the form of the worked examples in §7. Unrecorded reasoning cannot be reviewed, taught, or repeated.

## §1 — Art-direction decision system

Run the four decisions in order. Record all four (FE-321).

### 1.1 Inputs

Fix these first, in writing: **brand personality** (one primary: institutional / craft / playful / rebellious / serene / precise / luxurious), **industry**, **audience** (who, and what they came to do), **content type** (conversion / story / catalogue / tool / reference).

### 1.2 Theme, layout, and posture by input

| Brand personality + audience | Content type | Theme family (theme-library) | Layout family | Colour posture | Typography posture |
|---|---|---|---|---|---|
| Institutional, precise — B2B decision-makers, finance, legal | Conversion, reference | Archive / ledger / instrument themes (e.g. #3 Redacted Archive at low intensity, calibre/instrument themes) | Bento grid + editorial column hybrid | Restrained neutrals, one accent, no gradients | Grotesque body, mono for data and labels |
| Craft, handmade — consumers buying made things | Story + catalogue | Material themes (e.g. #41 Kintsugi, kiln/indigo/vat themes) | Narrative chapters, catalogue grid for the shop | Warm material palette, texture over flatness | Serif display + humanist body |
| Playful — families, casual consumers, community | Conversion, story | Pocket / toy / game themes (e.g. #150 Pocket Pal, #132 Side A / Side B) | Split stage: character/world + content column | Saturated brand-forward, chunky shapes | Rounded or pixel display accents, friendly grotesque body |
| Serene — wellness, retreats, slow brands | Story | Day-cycle / landscape themes (e.g. #124 One Full Day, #149 Jar of Light) | Canvas-first: one living scene, content docked to edges | Light-shifting palette that follows the scene | Elegant serif display, quiet grotesque body |
| Precise, technical — data products, research, deep tech | Reference, tool, story | Instrument / signal themes (e.g. #63 Sonar Room, #76 Ice Core Archive) | Instrument rail + content column; dashboards stay grid | Dark or lab-light, one signal colour | Mono-forward, tabular numerals everywhere |
| Luxurious — hospitality, culture, premium retail | Story, event | After-dark / gallery themes (e.g. #92 Museum After Dark, #105 The Night Train) | Narrative chapters, generous negative space | Deep ground, metallic accent, ivory text | Classical serif display, letterspaced small caps labels |
| Rebellious — music, street culture, launches | Event, story | Bold/poster themes from the playful-bold batch | Poster stack: oversized type, broken grid (once, deliberately) | High-contrast duotone, one loud accent | Expressive display at poster sizes, grotesque body |

Rules of the table: content type picks the layout family; personality picks the theme family and postures; audience can veto either (FE-322). If no row fits, take the nearest row and record the deviation — never fall back to "generic SaaS".

### 1.3 The motion-intensity dial

| Dial | Name | What it means in the build | Right for |
|---|---|---|---|
| 1 | Still | No scroll animation. Hover/focus states only. Content is the experience. | Legal, compliance, data-dense tools, print-adjacent pages |
| 2 | Quiet | Entry reveals (fade/rise ≤ 400 ms), animated counters for real numbers, section transitions. No parallax, no pinning. | Trust-first B2B, reference content, repeat-visit products |
| 3 | Alive | Dial 2 + parallax layers, staggered entrances, ambient loops, one signature element per two sections, marquee where in-theme. | Most marketing pages, commerce, community |
| 4 | Cinematic | Dial 3 + pinned scenes, scroll-scrubbed sequences, hero choreography, a signature element per section. | Storytelling, launches, cultural/hospitality, portfolios |
| 5 | Spectacle | Dial 4 + canvas/WebGL worlds, scroll-driven narrative chapters, multiple pinned scenes. Only when the experience *is* the content and the performance budget is proven on a mid-range phone. | Portfolio centrepieces, campaign microsites, exhibitions |

Set the dial from the table in §1.2's row (institutional 1–2, craft 3–4, playful 3–4, serene 3–4, technical 2–4 by content, luxurious 4, rebellious 4–5) and the content type. A dial above the row's range needs a written reason (FE-323).

### 1.4 Theme choice within the family

Pick the specific theme by its material metaphor: the theme's world must be one the brand's own content can live in (a survey company's world *is* the sonar room; a repair studio's *is* the mended bowl). If the metaphor needs explaining to the client, it is the wrong theme. Then read the theme's full library entry — palette, type, motion system, signature elements — before designing anything; the library entry, not taste, is the starting point.

## §2 — Composition intelligence

Apply and check, with numbers. "Feels balanced" is not a check.

1. **Focal order.** Every viewport has a 1-2-3 reading order the builder can state out loud: what is seen first, second, third. The first element beats the second by a clear margin — ≥ 1.6× in size, or a full weight step plus the section's only accent colour. If two elements tie, demote one; ties are defects (FE-324).
2. **The 3-second first viewport.** The opening viewport answers three questions without scrolling: whose is this, what is it about, what do I do next. Test by showing the hero for 3 seconds and asking — if any answer is missing, recompose before polishing anything else.
3. **Type scale.** One modular scale per page, ratio 1.25 (quiet) to 1.333 (expressive); body 16–18 px; line length 45–75 characters for prose; display sizes only from the scale. Off-scale sizes are drift (FE-022 in design-system).
4. **Whitespace is a ratio, not a leftover.** Space *between* groups must be at least 2× the space *within* a group (proximity ratio ≥ 2:1), all spacing on an 8 pt scale. If a section feels cramped, the fix is removing an element or doubling a gap — never shrinking type below the scale.
5. **Section pacing.** Alternate dense and quiet sections by plan; never more than 2 loud sections in a row; at least every third section is quiet (one idea, generous space, low motion). Section padding alternates deliberately (e.g. 96 px / 160 px), assigned by role per FE-025 — uniform padding is a tell (DET-VIS-001).
6. **One grid, one deliberate break.** Everything aligns to the page grid; at most one element per page may break it, as a named accent in the decision record. Accidental misalignment and repeated "creative" breaks both read as sloppiness.
7. **Imagery carries weight.** A real photograph of the product, place, or people outranks any heading (FE-026, FE-030). Decorative imagery that depicts nothing real is removed, not resized (BAN-FE-013 in design-system).
8. **The footer is a section.** It gets the same focal order, pacing, and theme language as every other section (FE-031). A footer that could belong to any site fails composition review on sight.

## §3 — Motion judgment

### 3.1 Technique by job

| Job to do | Technique | Do NOT use when |
|---|---|---|
| Land a section's message as it arrives | Staggered / masked entry reveal | The content is reference material users re-scan daily — reveal once per session or not at all |
| Show change, process, or a journey | Scroll-scrubbed sequence (values interpolated from smoothed progress) | A labelled static diagram communicates it as well — or on low-end devices that cannot hold frame rate |
| Give a world depth | Parallax layers (≤ 3 depths, small offsets) | Over forms, tables, or checkout; or when it makes text swim against its background |
| Hold one moment while the story moves | Pinned section | The pinned content is a paragraph that could simply be read; pinning is for scenes, not text blocks |
| Prove magnitude | Animated counter | The number is invented, estimated, or re-read often — animate only real, sourced figures, once |
| Make type itself the event | Kinetic typography | The line is legal, instructional, or must be copyable/searchable as-is |
| Keep a section alive while read | Ambient loop in the theme's material (drifting motes, breathing glow, passing landscape) | It competes with the section's focal element, or the section is a task surface |
| Connect two views as one object | Shared-element / page transition | Across payment, auth, or error states — continuity there reads as trickery |
| Fill a real wait | Skeleton / shimmer | The wait is under ~300 ms — skeletons for instant loads feel slower than the load |
| Show craft or a path | SVG line-drawing | It draws nothing meaningful — the line must trace a seam, a route, a signature, a real shape |
| Reward the pointer | Magnetic pull, 3D tilt, hover states (feather-light, transform-only) | Touch-primary audiences (give tap/scroll equivalents), or anywhere the effect delays the click it decorates |

### 3.2 Spectacle versus restraint

- The dial (§1.3) is the budget; §3.1 is how it is spent. Do not smuggle dial-4 techniques into a dial-2 page one "small" exception at a time.
- Spectacle is justified only when the visitor's job is to *feel, remember, or decide* — launches, stories, portfolios, cultural work. When the job is to *finish* — forms, checkout, settings, tools — restraint is the premium choice and spectacle is a defect.
- One spectacle moment per three viewport heights (FE-328). Two spectacles in one viewport cancel each other and read as noise.
- Performance floor beats ambition: if a mid-range phone cannot hold a smooth frame rate, drop one dial level. Never drop content, readability, or the reduced-motion variant instead.
- Restraint is not emptiness: a dial-1 page earns its quality from composition (§2), typography, and real imagery. "Quiet" pages that are merely empty fail the aliveness category of the score gate like any other dead section.

### 3.3 The merge test (signature elements)

A theme's signature elements are the page's identity — and the easiest place to produce slop. An element is **merged** when all four hold:

1. **It carries content.** The jar holds the collection count; the train carries the timetable; the ice core *is* the depth readout. Delete-test: removing it removes information or story, not just decoration.
2. **It is built from the content's own material.** Its shapes, colours, and behaviour come from the theme's world and the brand's real subject — not from a generic effects library.
3. **It lives in the layout.** It occupies grid space planned for it, at sizes that never cover the content it accompanies (an element that hides text at any scroll position fails outright — see §4, symptom 5 and 19).
4. **It obeys the page's physics.** It responds to the same smoothed scroll progress, the same state, and the same dial as everything around it — no independent loops fighting the page's rhythm.

An element passing all four reads as the site itself. Failing any one, it reads as pasted on — rebuild it into the content or cut it (BAN-FE-162).

## §4 — Anti-slop detection

Walk this table against the built page at 1440 px and 390 px (G-FE-163). Find the symptom, apply its fix, re-check. Never treat a symptom by restyling the whole page (FE-330).

| # | Symptom | Likely cause | Fix |
|---|---|---|---|
| 1 | Generic centred hero: gradient, default font, one button | No decision record; the template default shipped | Run §1; pick a theme and layout family; rewrite the brief until it could not describe another company (FE-029) |
| 2 | Every section is the same block with new copy | Composition by default, not by role | Recompose by role (FE-025): vary padding, alignment, and loudest element per section |
| 3 | Effects pasted on: blobs, waves, particle rain unrelated to the brand | Decoration chosen before content | Apply the merge test (§3.3); rebuild each element from the content's own material or cut it |
| 4 | Scroll animation jitters or stutters | Raw scrollY applied per event; layout properties animated | One rAF loop, lerped progress, transform/opacity only (§3.2 performance floor) |
| 5 | Content invisible: headings or cards never appear | Reveal trigger missed during fast scroll; no fallback | JS-gated hidden states only, force-reveal timeouts, re-trigger on re-entry; page fully readable with JS off |
| 6 | Dead sections: long stretches where nothing moves or holds attention | Motion treated as a hero-only concern | Give each section its in-theme ambient life or deliberate stillness with stronger composition (§2.5); check the aliveness score |
| 7 | Everything animates at once; the eye has nowhere to land | No choreography, no focal order | One focal mover per viewport; stagger the rest; demote competing motion (§2.1) |
| 8 | The custom cursor lags, sticks, or fights the pointer | Heavy cursor-follow physics | Remove it or reduce to a feather-light transform that never impedes movement — standing rule, BAN-FE-164 |
| 9 | Impressive numbers nobody can source | Counters filled with plausible invented figures | Animate only real, sourced numbers; if none exist, the counter goes (BAN-FE-012 in design-system) |
| 10 | Custom colours, same template smell | Palette changed, layout family untouched | Change the layout family and pacing, not just the palette (§1.2) |
| 11 | Text unreadable over dark scenes or animation | Contrast checked once, statically, on the resting state | Check contrast at *every* scroll state; raise the ambient light floor so text is legible before any beam/glow arrives |
| 12 | Marquee, counters, and tilt on every section | Techniques copied as a starter pack | One job per technique per page (§3.1); delete every instance that cannot name its job |
| 13 | Delight exists only on hover; mobile gets a lesser site | Desktop-first build, touch never reviewed | Every hover delight gets a tap/scroll equivalent; review at 390 px is a gate, not a courtesy |
| 14 | Page feels heavy: fans spin, scroll hitches | Multiple rAF loops, unbounded particles, layout thrash | Single loop, capped particle counts, change-guarded DOM writes; re-test on a mid-range phone |
| 15 | Footer looks like a different, older website | Footer never designed | Design it in-theme with the page's focal order and material (FE-031); it is the last impression, not an appendix |
| 16 | Type feels like the framework default | No typography posture chosen | Choose the posture in §1.2; pair display and body deliberately; mono only where data lives |
| 17 | Reduced-motion users get a broken or empty page | Static variant never built | Build the complete static variant (final states, all content, no loops) and gate it (§5) |
| 18 | Loud, louder, loudest — the page shouts throughout | No pacing plan | Alternate dense/quiet (§2.5); a quiet section at least every third; spectacle budget enforced (FE-328) |
| 19 | A showcase element covers the content it decorates | Element sized for drama, not for its grid home | Size elements to their planned space with margins at every scroll position (§3.3.3); content wins every overlap dispute |

## §5 — Self-critique quality gates (scored)

Before shipping, the builder scores its own page — honestly, as a hostile reviewer — on eight categories, 0–10 each, against these anchors. This is the detailed instrument behind G-FE-162 and the rubric bar in design-system (FE-028); both must pass.

| Category | 10 looks like | Threshold |
|---|---|---|
| 1. Hierarchy & focal order | Every viewport has an obvious 1-2-3; the 3-second test passes cold | ≥ 8 |
| 2. Element integration | Every signature element passes all four merge tests (§3.3) | ≥ 8 |
| 3. Readability & contrast | All text ≥ WCAG AA at every scroll state, over every animation | ≥ 9 — hard |
| 4. Motion smoothness | Smoothed scroll throughout; no jitter on fast scroll, trackpad, or 120 Hz; transform/opacity only | ≥ 8 |
| 5. Performance | One rAF loop; capped particles; smooth on a mid-range phone; no layout thrash | ≥ 7 |
| 6. Never-invisible safety | JS off = fully readable; every reveal has a fallback; re-entry re-triggers | 10 — hard, binary |
| 7. Reduced motion | Complete static variant: final states, full content, zero loops | 10 — hard, binary |
| 8. Aliveness | No section feels dead; stillness, where used, is visibly deliberate | ≥ 7 |

**Pass rule:** total ≥ 64 / 80 **and** every category at or above its threshold **and** both hard categories at 10. Any failure: fix the lowest-scoring category first (its §4 row or §3 rule usually names the fix), then re-score the *whole* page — scores from before the fix are void. Never ship below threshold, and never average away a hard-category failure with high scores elsewhere.

## §6 — Adaptation rules

Same theme, bent — never abandoned (FE-331). The theme's palette roles, type pairing, and element vocabulary stay; these change:

| Product type | Dial shift | Layout bend | What changes in practice |
|---|---|---|---|
| SaaS / B2B product | −1 from the family row | Bento + editorial hybrid; proof moves up to section 2 | Signature elements carry product data (a drawn ledger line that balances with real figures); story yields to comprehension; no pinned scenes inside the product tour |
| Editorial / magazine | +1 for features, −1 for index pages | Narrative chapters for features; dense grid for listings | Kinetic typography earns its place on features; listings stay quiet and scannable; reveals fire once per session |
| Commerce | Cap at 3; 1–2 at checkout | Catalogue grid; product is always the focal point | Motion shows the product *in use* (the vessel reassembles, the fabric drapes); nothing animates between the visitor and the buy button |
| Portfolio | Up to 5 | Canvas-first; the work is the layout | The signature element *is* the work itself, presented at full size; chrome and navigation go quiet so pieces carry every viewport |
| Event | 3–4 | Poster stack; mobile-first | The countdown is a real counter (§3.1); kinetic type carries date/venue as the hero; after the event the same theme bends to a recap story at dial 3 |
| Product storytelling | 4 | Pinned chapters following the product's own beats | Scrubbed sequences show the product changing state (assembled, opened, aged, repaired); each chapter's element is a stage of the product, never a mascot pasted beside it |

Bend test: screenshot the adapted page beside the theme's reference demo — same world, different posture. If they read as different worlds, the bend went too far; if they read as the same page, it did not bend at all.

## §7 — Worked reasoning examples

The form every decision record takes (FE-332): brief → choices → why → what was rejected.

**Example A — "Ledgerline", B2B accounting SaaS.** Brief: institutional product, CFOs and finance leads, conversion + reference content; the audience has been burned by flashy fintech before. Choices: archive/instrument theme family (§1.2, row 1); bento + editorial hybrid layout; dial 2; restrained neutrals with one accent; grotesque + mono-for-data posture. Signature element: in the pricing section, a ledger line draws itself across the table and *balances* — the debit and credit columns animate to the plan's real totals, so the element is the product's core promise (books that balance) carrying real figures. Why: trust is the conversion mechanism for this audience; quiet competence, visibly accurate numbers, and a mono data voice signal it better than any claim. Rejected: a dark cinematic theme at dial 4 (spectacle reads as risk to a CFO — FE-322), kinetic-type hero (the claim must stay quotable), animated counters with market-size numbers (unsourced — §4, symptom 9).

**Example B — "Kiln & Co", pottery studio with a shop.** Brief: craft brand, consumers, story + catalogue; the maker's hands and the repair service are the differentiators. Choices: theme #41 Kintsugi from the library, as-is; narrative chapters for the studio story, catalogue grid for the shop; dial 4 on story pages, dial 2 in the shop, dial 1 at checkout (§6, commerce row); warm material palette; serif display + humanist body. Signature elements: the story's hero vessel cracks and mends with gold as the visitor scrolls the studio's own history — the repair service *is* the brand story — and shop cards reuse the same vessel language at hover scale, so story and shop are one world. Why: the theme's metaphor needs no explaining to this client (§1.4), and the mending animation demonstrates the paid service better than copy can. Rejected: a minimal white gallery theme (erases the craft; the work photographs beautifully but so does every competitor's), a WebGL clay world at dial 5 (unproven performance on shoppers' phones, and it would fake the product instead of photographing it — FE-030).

**Example C — Exam-prep content site for students.** Brief: editorial/reference content, students on mid-range Android phones, returning daily in the weeks before exams; content is guides, ranked topic lists, and document links. Choices: editorial theme family; dense scannable grid; dial 2; light airy posture with one accent; grotesque body + mono for counts and dates. Signature element: a progress spine running down each guide that fills as topics are checked off and holds the student's place between visits — the element *is* the study plan, not decoration beside it. Counters appear only where real counts exist (papers actually counted, documents actually in the library). Why: repeat visitors scanning under time pressure punish novelty — reveals fire once per session, nothing is pinned, and every animation survives the §5 performance category on a cheap phone. Rejected: cinematic pinned chapters (scrubbing fights scanning — §3.1), a custom cursor (banned outright for this audience, BAN-FE-164), spectacle dial 4 (ego over audience — FE-322).

## BAN list

- **BAN-FE-161 — Design by default.** Banned: shipping the framework's template layout with a new palette and calling it a theme. Defeats: DET-VIS-006 (rule FE-321). Bad: the "redesign" changes hex codes and a logo; layout family, pacing, and section template are the starter's. Instead: run the decision system (§1) and change layout family, pacing, and posture with the palette. Severity: BLOCK.
- **BAN-FE-162 — Pasted-on spectacle.** Banned: any animated element that fails a merge test in §3.3 — carries no content, is built from generic effect material, floats outside the layout, or runs on its own physics against the page. Defeats: DET-VIS-028 (rule FE-327). Bad: a particle starfield behind a plumbing company's pricing table; a spinning 3D logo covering the hero copy it decorates. Instead: rebuild the element from the content's own material, sized into the grid — or cut it. Severity: BLOCK.
- **BAN-FE-163 — Ship now, score later.** Banned: releasing a page below the §5 thresholds with a promise to improve it after launch. Defeats: DET-VIS-022 (rule FE-329). Bad: the self-critique scores readability 6 ("the dark section is moody") and ships because the deadline arrived. Instead: fix the lowest category, re-score the whole page, ship at threshold. Severity: BLOCK.
- **BAN-FE-164 — The heavy cursor.** Banned: a custom cursor whose physics, size, or lag can impede pointer movement, however beautiful. Defeats: DET-VIS-042 (rule FE-326). Bad: a trailing glass jar follows the pointer at 200 ms lag; users overshoot every link. Instead: the normal system cursor, with at most feather-light hover responses on the elements themselves. Severity: BLOCK.
- **BAN-FE-165 — Dial by taste.** Banned: setting motion intensity per section by feel, so one page mixes dial-1 tables with dial-5 spectacle. Defeats: DET-VIS-040 (rule FE-323). Bad: a quiet SaaS page whose footer suddenly pins, scrubs, and plays a canvas world. Instead: one dial per page, set in the decision record; deviations get a written reason. Severity: WARN.

## Gates

- **G-FE-161 — Decision record check.** Verifies: FE-321, FE-323, FE-332. Check: manual — before build and at review, read the decision record: theme, layout family, dial, both postures, and at least one rejected alternative with its reason. Pass: all present and traceable to §1's tables. Fail: no build starts, or the milestone blocks. Recorded in: progress.md.
- **G-FE-162 — Self-critique score.** Verifies: FE-329. Check: manual scoring of the built page on the eight §5 categories at 1440 px and 390 px, hard categories tested directly (JS disabled; reduced-motion emulation on). Pass: total ≥ 64/80, every category at threshold, hard categories at 10. Fail: fix lowest category, re-score in full, block shipment until pass. Recorded in: progress.md.
- **G-FE-163 — Slop sweep.** Verifies: FE-330. Check: manual — walk the §4 table row by row against full-page screenshots; each live symptom is marked with its row number and fixed by that row's stated fix. Pass: zero symptoms live. Fail: block the milestone. Recorded in: progress.md.
- **G-FE-164 — Motion smoothness and safety audit.** Verifies: FE-326, FE-327. Check: manual + device — fast-scroll and trackpad passes on a mid-range phone; confirm lerped progress (no raw-scroll jumps), elements sized inside their grid homes at every scroll position, and one rAF loop driving scroll-linked motion. Pass: no jitter, no covered content, frame rate holds. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Intelligence as decoration.** The decision record is written after the build, rationalising whatever was made. Catch it: G-FE-161 runs *before* build; a record whose "rejected alternative" was never buildable is fiction.
- **The dial that only goes up.** Every review adds motion; nothing is ever cut, and the page accretes spectacle until it fails performance. Catch it: FE-326 — a technique that loses its job in review is removed in the same review.
- **Scoring your own homework kindly.** Self-critique drifts generous: 8s for effort. Catch it: score against the §5 anchors with screenshots as evidence, and treat any category argued up from a 6 to an 8 without a change as a 6.
- **Adapting by reskinning.** A theme "adapted" to a new product type by swapping accent colours while keeping the old dial and layout. Catch it: run the §6 bend test — same world, visibly different posture, or it did not happen.

## Examples

The three worked reasoning examples in §7 (Ledgerline, Kiln & Co, the exam-prep content site) are the canonical decision records for this skill; the files in `examples/` present the same three decisions in Before/After form — the page as it would have shipped by default, and the page the decision system produced.

- `examples/example-1.md` — Ledgerline (B2B accounting SaaS): template default vs a dial-2 archive/instrument build whose signature element carries real figures.
- `examples/example-2.md` — Kiln & Co (pottery studio + shop): minimal gallery default vs theme #41 Kintsugi applied whole, bent per page type.
- `examples/example-3.md` — Exam-prep content site: cinematic default vs a dial-2 scannable build whose progress spine is the study plan itself.

## Recall anchors

- Decide before designing: theme, layout, dial, postures — in writing.
- Audience trust outranks brand ego, every time.
- Every technique names its job, or it is removed.
- If deleting it loses only decoration, it was pasted on.
- Score it like a hostile reviewer: ≥ 64, hard gates at 10, or fix and re-score.

## Checklist

- [ ] Decision record written before build: theme, layout family, dial, colour and typography postures, one rejected alternative (G-FE-161).
- [ ] Dial set once from §1.2/§1.3; any change carries a written reason (FE-323).
- [ ] Every viewport passes the focal-order and 3-second tests (§2.1, §2.2).
- [ ] Pacing plan alternates dense/quiet; spectacle budget respected (§2.5, FE-328).
- [ ] Every animation technique names its job from §3.1 (FE-326).
- [ ] Every signature element passes all four merge tests (§3.3).
- [ ] Slop sweep walked at 1440 px and 390 px; zero symptoms live (G-FE-163).
- [ ] Self-critique scored: ≥ 64/80, all thresholds met, hard categories at 10 (G-FE-162).
- [ ] Smoothness audit passed on a mid-range phone; nothing covers content at any scroll position (G-FE-164).
- [ ] Adaptation bends recorded where one theme serves multiple product types (§6).

<!-- END EMBEDDED: Skill: design-intelligence -->


---

<!-- BEGIN EMBEDDED: Skill: motion — source: skills/frontend/motion/SKILL.md -->

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

<!-- END EMBEDDED: Skill: motion -->


---

<!-- BEGIN EMBEDDED: Skill: scroll-experiences — source: skills/frontend/scroll-experiences/SKILL.md -->

# scroll-experiences

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.1.0
- **Last verified:** 2026-11-23
- **Sources:** MDN, Scroll-driven animation timelines (scroll() and view()) — https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines ; CSS Scroll-Driven Animations Module Level 1 (specification) — https://drafts.csswg.org/scroll-animations/
- **Depends on:** motion, layout-responsive
- **Feeds into:** frontend-core

## When to use / Do NOT use

- **Use when:** building or reviewing anything tied to scroll position — reveal choreography, parallax, progress indicators, pinned sections. This skill owns the scroll half of WCPM §7 and designs to pass the scroll-related G-MOT gates; the general motion system (tokens, purposes, reduced-motion variants) is owned by motion and assumed here.
- **Do NOT use when:** the animation is a state change or micro-interaction (motion), the scene is 3D (webgl-3d), or the real question is whether the content should exist (content skills). If the page reads perfectly with every scroll effect deleted, that is the correct baseline — this skill only adds on top of it.

## The positive standard — scroll is a designed system

The safety rules below keep scroll honest; they are not the design. On any page long enough to scroll, the scroll itself is choreographed as part of the theme's motion system (motion FE-091): the reader's descent reveals, scrubs, deepens, and progresses through the theme's world. A long page whose scroll does nothing — sections simply stacked, statically present — is unfinished, however safe it is. FE-101 remains the floor: everything the choreography adds is enhancement on top of content that is already fully there.

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
10. **FE-110 — Every long page has a scroll system.** Where a page scrolls beyond a couple of viewports, the build implements, in the theme's own language: scroll-triggered reveals choreographed per section (varied, never one uniform fade — motion BAN-FE-041); scroll-driven/scrubbed animation tied to descent (a thing fills, travels, deepens, or assembles as the reader descends); parallax depth where the scene has depth to give; a scroll progress indication in-theme (a filling jar, a route line, a depth gauge — a bare bar only when the theme is genuinely minimal); and pinned sections where a moment in the story earns the reader's full viewport (FE-113). Missing components need a recorded in-theme reason, as in motion FE-091.
11. **FE-111 — Scroll-driven values are smoothed, never raw.** JavaScript scroll effects read a *target* progress (a passive listener or observer may record position; that is all it may do) and the page's single rAF loop eases the displayed value toward it with lerp, so motion has weight and nothing jitters — not on trackpad steps, not at 120 Hz, not on a mid-range phone. Applying raw `scrollY` (or a raw ratio derived from it) directly to styles per event is banned (BAN-FE-056). This refines FE-102/BAN-FE-055: the forbidden thing was never the listener; it is per-frame layout work and unsmoothed application. CSS `scroll()`/`view()` timelines remain preferred where support allows, with the smoothed-JS path as the designed fallback (FE-108).
12. **FE-112 — A scroll reveal can never strand content.** Hidden start states are JS-gated (added by script, never shipped in CSS/HTML — FE-101 by construction). Every reveal also carries: a force-reveal fallback timeout that lands the content visible even if its trigger never fires; and re-trigger/re-check on re-entry, so a fast or smooth scroll that skips a section cannot leave it blank — the section is verified visible when it is actually in view, not only when its threshold crossing was observed. This is the scroll case of motion FE-096 and it is testable (G-FE-056).
13. **FE-113 — Pins serve the story, and earn their viewport.** A pinned section exists because the narrative has a moment that deserves to hold still while the world moves through it (tape transferring spool to spool, a sun crossing the sky) — not as decoration and never two pins competing in one viewport span. Pins inherit FE-107 (focus never trapped or obscured), BAN-FE-054 (never clip content at 360×640 or 1280×600), and FE-103 (the pin rides native scroll; it never captures it).
14. **FE-114 — The theme's scroll signature is present and merged.** Each theme in skills/frontend/theme-library/ specifies how scrolling itself behaves in its world — drilling down through ice strata, descending a sonar gauge, a pal walking the page's bottom edge. That signature is implemented and woven into the content it measures (the gauge *is* the article's depth; the walk *is* the page's progress), per motion FE-092's removal test: delete it and the page's meaning thins. A generic progress bar pasted over a themed page is the scroll form of BAN-FE-048.
15. **FE-115 — No dead stretches.** Ambient, scroll-aware life runs the length of the page (motion FE-091): layers drift, instruments tick, the scene breathes at every depth — quietly, under the one attention moment (motion FE-088), and all of it off under reduced motion (FE-104). A viewport where nothing in the theme's world responds to the reader's presence is a gap in the system, recorded and filled, not a rest.

## BAN list

- **BAN-FE-051 — Reveal-from-hidden content.** Banned: sections styled `opacity: 0` (or translated off-view) in CSS, revealed only when JavaScript adds a class — so no-JS, a failed script, or an unsupported timeline leaves a blank page. Defeats: DET-VIS-040. Bad: `.reveal { opacity: 0; transform: translateY(24px); }` with the visible state applied by an IntersectionObserver callback; with scripts blocked, the page is five empty viewports. Instead: render visible by default and let the observer add an *enhancement* (or animate from visible states only), per FE-101. Severity: BLOCK.
- **BAN-FE-052 — Scroll-jacking.** Banned: overriding the user's scroll — snapping forcibly between sections, translating wheel input into custom animation, or auto-scrolling the reader through content. Defeats: DET-VIS-037. Bad: a marketing page that captures wheel events and animates one full screen per tick, so a trackpad user lurches past the pricing details they were trying to read. Instead: native scrolling, always; choreography rides on the user's scroll position, never replaces it (FE-103). Severity: BLOCK.
- **BAN-FE-053 — Parallax with no off switch.** Banned: parallax layers or scroll-linked motion that continue under `prefers-reduced-motion: reduce`. Defeats: DET-VIS-041. Bad: three background layers drifting at different rates keep drifting in reduced-motion emulation; no reduce block exists. Instead: parallax disabled under the reduce query, layers resting in a complete static composition (FE-104). Severity: BLOCK.
- **BAN-FE-054 — The clipping pinned hero.** Banned: a pinned or `100vh` hero section whose foreground text or CTA is clipped or overlapped on short or narrow viewports while the pin holds. Defeats: DET-VIS-039. Bad: at 360×640 the pinned hero's CTA sits half under the following section for the first 400px of scroll, unreachable and unreadable. Instead: heroes sized to content with `min-height` (layout-responsive, DET-VIS-039 discipline), pins tested at 360×640 and 1280×600 before they ship. Severity: BLOCK.
- **BAN-FE-055 — The per-frame scroll handler.** Banned: `window.addEventListener('scroll', …)` code that reads layout and writes styles on every event, producing jank on mid-range devices. Defeats: DET-VIS-040. Bad: a handler calling `getBoundingClientRect()` on nine elements and setting transforms per scroll event; the profiler shows a chain of long tasks through the whole page. Instead: a CSS `view()` timeline or an IntersectionObserver with a passive, rAF-throttled fallback (FE-102). Severity: WARN.

- **BAN-FE-056 — Raw scrollY application.** Banned: styles written directly from `scrollY` or an unsmoothed ratio on scroll events, so elements jump in trackpad-sized steps and jitter against each other at different rates. Defeats: DET-VIS-040. Bad: a depth readout, a parallax layer, and a progress fill each compute from raw scroll in separate handlers; on a fast scroll they visibly disagree and shiver. Instead: one target, one rAF loop, lerp-smoothed displayed progress that every scroll effect reads (FE-111). Severity: BLOCK.
- **BAN-FE-057 — The observer-only reveal.** Banned: a reveal whose only path to visible is one IntersectionObserver threshold crossing — no fallback timeout, no re-entry check — so a fast scroll, a restored scroll position, or an unusual viewport leaves the section blank forever. Defeats: DET-VIS-041. Bad: jumping to a mid-page anchor on load leaves three sections above the fold permanently at `opacity: 0`. Instead: FE-112 — JS-gated states, force-reveal timeout, re-check on entry. Severity: BLOCK.

## Gates

- **G-FE-051 — No-JS visibility pass.** Verifies: FE-101, FE-105, FE-108. Check: automated — Playwright loads every route with JavaScript disabled and asserts each section's text is present and visible in the rendered page. Pass: all content visible on all routes. Fail: block shipment. Recorded in: progress.md.
- **G-FE-052 — Reduced-motion scroll pass.** Verifies: FE-104. Check: automated — Playwright with reduced-motion emulation scrolls the full page and asserts parallax layers are static and no scroll-linked animation is running. Pass: zero scroll-linked motion under emulation. Fail: block shipment. Recorded in: progress.md.
- **G-FE-053 — Scroll-handler scan.** Verifies: FE-102. Check: automated — grep shipped scripts for `addEventListener('scroll'` / `onscroll`; any hit requires a recorded exception proving the handler does no per-frame layout work. Pass: zero unexcused hits. Fail: warn; block if the handler touches layout. Recorded in: progress.md.
- **G-FE-054 — Scroll profile and pin inspection.** Verifies: FE-107, FE-109. Check: manual — DevTools Performance recording of a full-page scroll on a mid-range CPU-throttled profile, checking for long tasks tied to scroll; plus a focus walk through pinned sections at 360×640 and 1280×600 screenshots. Pass: no scroll-linked long tasks; focus never obscured; no clipped hero content. Fail: block until simplified or unpinned. Recorded in: progress.md.

- **G-FE-055 — Scroll-system completeness and smoothness.** Verifies: FE-110, FE-111, FE-114, FE-115. Check: manual + automated — walk the page against the FE-110 component list and the theme's scroll signature; then profile a full-page scroll (fast, slow, and trackpad-stepped) on a mid-range CPU-throttled profile, confirming every scroll-driven value moves smoothly (single smoothed progress source; no per-effect disagreement) and no frame budget is broken. Pass: system complete and in-theme, signature merged, zero visible jitter. Fail: block shipment. Recorded in: progress.md.
- **G-FE-056 — Force-reveal fallback test.** Verifies: FE-112, FE-101. Check: automated — Playwright loads each route with IntersectionObserver disabled/stubbed and with scripted instant jumps (anchor navigation, restored scroll) to mid-page positions, then asserts every section reaches full visibility within its fallback window. Pass: zero stranded sections under every failure mode. Fail: block shipment. Recorded in: progress.md.

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
- The scrollbar belongs to the user.
- Reduced motion: scroll effects off, page complete.
- One target, one loop, lerp — raw scrollY is never applied.
- Every reveal has a fallback; nothing can be stranded invisible.

## Checklist

- [ ] Full page readable with JavaScript disabled (G-FE-051).
- [ ] No per-frame scroll handlers doing layout work (G-FE-053).
- [ ] No scroll-jacking: native position, direction, and speed throughout (FE-103).
- [ ] Parallax and scroll-linked motion off under reduced motion (G-FE-052).
- [ ] Progress never communicated by a progress bar alone (FE-106).
- [ ] Pinned elements never obscure the focused element (FE-107).
- [ ] Scroll profile shows no scroll-linked long tasks (G-FE-054).
- [ ] Unsupported-browser experience is the designed static page (FE-108).
- [ ] Scroll system complete: reveals, scrubbed animation, progress, and pins where the story earns them (FE-110, G-FE-055).
- [ ] All scroll-driven values read one lerp-smoothed progress; no raw scrollY application (FE-111).
- [ ] Every reveal JS-gated with a force-reveal fallback; observer-disabled test strands nothing (FE-112, G-FE-056).
- [ ] Theme scroll signature implemented and merged into the content (FE-114).
- [ ] No dead stretches: ambient scroll-aware life at every depth (FE-115).

<!-- END EMBEDDED: Skill: scroll-experiences -->


---

<!-- BEGIN EMBEDDED: Skill: design-system — source: skills/frontend/design-system/SKILL.md -->

# design-system

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** GOV.UK Design System, button component (usage guidance incl. when not to use) — https://design-system.service.gov.uk/components/button/ ; Design Tokens Specification 2025.10, first stable version announcement — https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/
- **Depends on:** design-tokens
- **Feeds into:** frontend-core, component-library, typography, layout-responsive

## When to use / Do NOT use

- **Use when:** establishing or governing the system itself — its tokens, component inventory, usage rules, and changelog — and when reviewing a page for system-level failures: monotony, drift, invented proof. This skill is the primary home for WCPM's visual-language material: §2 catalog (as reference), §3 diagnosis and CV cures, §4 design brief and distinctiveness, and §6 visual craft.
- **Do NOT use when:** the question is a single token value (design-tokens), a single component's internals (component-library), or a single page's layout (layout-responsive). The system governs; those skills execute.

## Rules

1. **FE-021 — The system is four artifacts.** The token set, the component library, written usage rules, and a changelog. A visual decision that exists only inside one page's code is not part of the system and does not ship as one.
2. **FE-022 — Every decision traces.** Each visual choice on a shipped page traces to a token, a library component, or a documented one-off exception with a written reason. Untraceable styling is drift and is removed or absorbed into the system.
3. **FE-023 — Guidance includes refusal.** Every component's documentation states its purpose, its variants, and at least one "do not use when" case, on the GOV.UK pattern. A component documented only with happy paths will be misused.
4. **FE-024 — Changes are versioned.** A token or component change ships with a changelog entry and a visual-regression pass, never as a silent edit. Consumers of the system learn about change from the changelog, not from a screenshot diff.
5. **FE-025 — Composition varies by role.** Section composition follows content role (hero, proof, dense content, closing): a page where every section shares the same padding, alignment, and loudest element fails system review (DET-VIS-001, DET-VIS-002, DET-VIS-010).
6. **FE-026 — Proof may outrank headings.** Hierarchy serves the message: a metric, a product shot, or a customer quote may be the most prominent element in its section. The heading is not entitled to be loudest by default.
7. **FE-027 — Diagnose before redesigning.** Visual failures are diagnosed against the parameter catalog (WCPM §2, served in this repo by DET-VIS-001…044) and cured with the matching cure rules (CV family) — not by restyling on taste. Clusters are scored as clusters: 3 or more minor tells in one component or section count as one major (WCPM CLU-01…06; enforced by G-DES-02).
8. **FE-028 — The acceptance bar is scored, not felt.** A page passes visual acceptance on the rubric: zero P0 parameters, rubric score ≥ 90, every category ≥ 7, zero F1–F8 auto-fails (WCPM G-DES-01). "Looks fine to me" is not a verdict — human detection of generated design is a near-chance instrument, so the score carries the decision.
9. **FE-029 — Distinctiveness is briefed before building.** Each project opens with a design brief that names its divergence: the visual choices that make this product unlike the template default (WCPM §4, BR- divergence rules and D-MIN minimum thresholds). A brief that could describe any SaaS site is rejected and rewritten.
10. **FE-030 — Imagery belongs to the system.** Photography and illustration follow one documented style and depict the business's real product, place, or people (DET-VIS-023); aspect ratios follow an art-directed grid so subjects survive their crops (DET-VIS-029). Stock or generated imagery depicting nothing real is not a system asset.
11. **FE-031 — The footer is designed.** The footer uses the system's tokens and carries a brand statement, real contact paths, and legal links that resolve — not a generic link grid pasted under the page (DET-VIS-009).

## BAN list

- **BAN-FE-011 — The one-gradient, one-font "system".** Banned: calling a violet-blue gradient, one default font, and copy-pasted cards a design system. Defeats: DET-VIS-017. Bad: every hero, button, and headline on the site carries the same purple-to-blue gradient; the "system" page lists a logo, a gradient, and Inter. Instead: a chosen brand palette with roles, a deliberate type choice, and tokenized scales (design-tokens). Severity: BLOCK.
- **BAN-FE-012 — Invented social proof in the system.** Banned: logo clouds, testimonials, or metrics built from invented marks, people, or numbers as reusable system components. Defeats: DET-VIS-034. Bad: a "trusted-by" component shipping with six plausible-looking wordmarks of companies that are not customers. Instead: the component renders only real, permitted logos — and renders nothing when none exist. Severity: BLOCK.
- **BAN-FE-013 — Imagery that depicts nothing.** Banned: stock or AI imagery with no connection to the business as the system's default visual language. Defeats: DET-VIS-023. Bad: a bakery's site illustrated throughout with fintech dashboard renders and abstract 3D blobs. Instead: photographs of the actual bakery, its products, and its people, in one documented style. Severity: BLOCK.
- **BAN-FE-014 — The uniform section template.** Banned: one section layout — same padding, centered heading, three cards — repeated for every content role on a page. Defeats: DET-VIS-001. Bad: hero, features, story, pricing, and FAQ all rendered as 96px-padded centered blocks differing only in copy. Instead: composition assigned per role (FE-025), with padding and alignment varying deliberately. Severity: WARN.
- **BAN-FE-015 — Generic wave and blob decoration.** Banned: SVG wave dividers, blurred color blobs, and dotted grids pasted between sections as decoration. Defeats: DET-VIS-028. Bad: a purple blob behind the hero, a wave divider before pricing, a dotted grid behind testimonials — none of them brand assets, all of them defaults. Instead: transitions that are structural (color change, overlap, imagery) or a custom brand device used consistently. Severity: WARN.

## Gates

- **G-FE-011 — DET-VIS cluster review.** Verifies: FE-025, FE-026, FE-027, FE-030, FE-031. Check: manual — per milestone, walk DET-VIS-001…044 in ID order against full-page screenshots at 1440px and 390px; mark each hit with a screenshot or measured value; apply the cluster rule (3+ minors in one section = 1 major). Pass: zero blockers, zero majors, clusters resolved. Fail: block the milestone. Recorded in: progress.md.
- **G-FE-012 — Rubric acceptance score.** Verifies: FE-028. Check: manual scoring against the WCPM G-DES-01 bar — count P0 parameter hits, score the rubric, check every category ≥ 7 and zero F1–F8 auto-fails. Pass: 0 P0, score ≥ 90, all categories ≥ 7, zero auto-fails. Fail: block shipment. Recorded in: progress.md.
- **G-FE-013 — System trace audit.** Verifies: FE-021, FE-022, FE-024. Check: automated + manual — sample 10 styled elements per page and resolve each to a token, a library component, or a logged exception; confirm the system changelog has an entry for every token/component change in the release. Pass: 10 of 10 trace, changelog complete. Fail: block until drift is absorbed or removed. Recorded in: progress.md.
- **G-FE-014 — Token and contrast enforcement.** Verifies: FE-022 (via design-tokens). Check: automated — the design-tokens gates run as this skill's enforcement arm: token-literal lint and the semantic-pair contrast script (G-FE-022, G-FE-023). Pass: both green. Fail: block shipment. Recorded in: progress.md.

## Intelligence — decisions & gates

> **Judgment layer.** These decisions apply the judgment layer above this skill — `skills/frontend/design-intelligence/SKILL.md` and the theme library (`skills/frontend/theme-library/`). Settle the theme's art direction there first, then decide here inside it; where a decision below and a rule above disagree, the rule above wins.

### Decision rules — governing the system

| Decision | Read the situation | Decide |
|---|---|---|
| How much system to build first | Content still changing, one surface | Ship the core only — color, type, and spacing tokens plus 8–12 components — and grow by evidence, not speculation. |
| How much system to build first | Three or more surfaces share components | Invest in full variant and state matrices up front; inconsistency costs more than the build. |
| How expressive the system may be | Audience needs trust first (finance, health, regulated) | Restraint: fewer display devices, proof-led composition; expression lives in typography and imagery, not decoration. |
| How expressive the system may be | Consumer or creative brand | Choose one signature device and carry it in the tokens, so every page inherits it instead of inventing its own (FE-029). |
| Where saturated color may live | Data-heavy product | Reserve saturation for data and status semantics; brand color stays quiet so meaning stays legible. |
| Where saturated color may live | Editorial or marketing surface | Wider neutrals with one accent; imagery and type carry the temperature. |
| Which imagery style to standardize | What the business can actually supply, week after week | Standardize the style the team can sustain (FE-030); a style abandoned after launch is worse than a plainer one that holds. |
| How many exceptions a page may carry | Page type | Campaign and landing pages may hold more logged exceptions; core product flows hold near zero (FE-022). A third exception of one kind becomes a token or a component. |

### Self-check gate

- **G-FE-015 — Pre-ship intelligence self-check (design-system).** Verifies: FE-021, FE-022, FE-025, FE-029, FE-030 as judgment, not just compliance. Check: manual — the builder scores each item pass/fail against the shipped pages: (1) ★ every visual choice on the page traces to a token, a component, or a logged exception; (2) ★ the page's distinctiveness can be named in one sentence, and it matches the brief; (3) composition differs by section role — no two adjacent sections share padding, alignment, and loudest element; (4) the loudest element in each section is the message's proof, not a default heading; (5) imagery depicts the real business in the one documented style; (6) the footer reads as a designed brand surface, not a pasted link grid. Pass: both ★ items pass and at least 5 of 6 overall. Fail: fix, or log a written exception, before shipping. Recorded in: progress.md.

### Anti-pattern table — symptom → cause → fix

| Symptom | Cause | Fix |
|---|---|---|
| Every new page needs a new shade or size | Palette and scales were defined as raw values, never as semantic roles | Define roles (surface, action, emphasis, danger) in design-tokens; pages consume roles, not values. |
| Two surfaces under one brand look unrelated | The system documented components but never composition or voice | Brief distinctiveness (FE-029) and record composition per content role (FE-025). |
| Builders keep asking "which one do I use?" | Near-duplicate components accumulated without refusal guidance | Merge into variants of one component; write the "do not use when" case (FE-023). |
| A brand refresh breaks pages unpredictably | Untraceable one-off styling absorbed the change unevenly | Run the trace audit (G-FE-013); absorb or remove drift before refreshing. |
| The system is complete and documented, yet pages still look generic | Tokens encode only safe defaults; no signature device was ever chosen | Choose one brand device — type voice, imagery style, or layout motif — and encode it in tokens and components (FE-029). |
| Consumers are surprised by system changes | Changes shipped silently or unversioned | Version every change with a changelog entry and a visual-regression pass (FE-024). |
| The exception log grows every milestone | The system lacks a pattern pages genuinely need, so pages route around it | Promote the third exception of a kind into the system, or remove the need (FE-022). |

## Anti-patterns

- **The system that is a screenshot.** A Figma frame or a "brand" page exists, but pages are styled ad hoc and nothing traces back to it. Catch it: run the trace audit (G-FE-013); untraceable elements are the system failing, not the page.
- **Drift by a thousand cuts.** Each page is almost consistent — slightly different padding, an off-scale size, a near-miss color. Catch it: drift is a cluster phenomenon; the per-milestone DET-VIS review exists because no single diff looks wrong.
- **Restyle instead of diagnose.** A flagged page gets a new coat of paint with the same structure underneath, and the same parameters hit again next milestone. Catch it: every rework names the parameter and the cure applied (FE-027).
- **Exception inflation.** "Documented one-offs" multiply until the exception is the real system. Catch it: count exceptions per page at review; a third exception of the same kind becomes a token or component, or is removed.

## Examples

- [Example 1 — Uniform sections recomposed by role](examples/example-1.md) — corrects FE-025.
- [Example 2 — A gradient signature replaced by a brand system](examples/example-2.md) — corrects FE-029.
- [Example 3 — An invented logo cloud removed and replaced with real proof](examples/example-3.md) — corrects FE-022 (via BAN-FE-012).

## Recall anchors

- Four artifacts: tokens, components, guidance, changelog.
- If it doesn't trace to the system, it's drift.
- Diagnose against parameters; never restyle on taste.
- The rubric decides — 0 P0, ≥ 90, no category under 7.
- Proof is allowed to be louder than the heading.

## Checklist

- [ ] The system has all four artifacts, current (FE-021).
- [ ] Sampled elements trace to token, component, or logged exception (G-FE-013).
- [ ] Every component documents a "do not use when" case (FE-023).
- [ ] Token/component changes carry changelog entries (FE-024).
- [ ] DET-VIS cluster review walked at 1440px and 390px (G-FE-011).
- [ ] Rubric acceptance bar met: 0 P0, ≥ 90, categories ≥ 7, zero F1–F8 (G-FE-012).
- [ ] Composition varies by section role; proof may outrank headings (FE-025, FE-026).
- [ ] Imagery depicts the real business in one documented style (FE-030).

<!-- END EMBEDDED: Skill: design-system -->


---

<!-- BEGIN EMBEDDED: Skill: design-tokens — source: skills/frontend/design-tokens/SKILL.md -->

# design-tokens

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Design Tokens Format Module 2025.10 (DTCG) — https://www.designtokens.org/tr/2025.10/ ; Style Dictionary, DTCG support — https://styledictionary.com/info/dtcg/
- **Depends on:** none — standalone: tokens are defined from the project's own visual decisions (user-supplied palette and type choices) in the token source files; this is the source layer, so nothing upstream feeds it. Its tokens feed design-system, component-library, typography, frontend-core, and motion.
- **Feeds into:** design-system, component-library, typography, frontend-core, motion

## When to use / Do NOT use

- **Use when:** defining, changing, or auditing the token source files — the single place a visual value may be defined — and when a page shows value-level tells: gradient signatures, shadow monoculture, radius scatter, unchecked contrast. WCPM's colour/gradient bans (C- working IDs), the COL family, and the SPC family are prevented here, at the token layer.
- **Do NOT use when:** the question is how a value is used (component-library, layout-responsive) or whether a composition works (design-system). Tokens define values; they do not design pages.

## Rules

1. **FE-041 — One format, one source.** Tokens are authored once in DTCG-format JSON — every token an object with `$value`, `$type`, and aliases by dot-path — and transformed by Style Dictionary (or Terrazzo) into CSS custom properties and other platform outputs. Hand-edited output files are defects.
2. **FE-042 — Three tiers.** Primitive (raw values) → semantic (roles: `color-action-primary`, `surface-raised`) → component. Theming happens at the semantic tier by overriding the same names; a theme never duplicates the primitive file.
3. **FE-043 — Semantic only in components.** Components reference semantic tokens exclusively. A primitive value, hex code, pixel, or millisecond literal in component styles is a defect found by lint, not by opinion.
4. **FE-044 — Every token is documented.** Each token carries a `$description` naming its role. Retired tokens are marked `$deprecated` with a pointer to their replacement — never silently deleted, so existing code fails loudly instead of drifting.
5. **FE-045 — Scales with named roles.** Elevation, radius, spacing, and duration are scales whose steps have roles (radius: input / card / pill; elevation: flat / card / menu / modal). Values are applied by role — the direct counter to the single-shadow default (DET-VIS-021) and radius scatter (DET-VIS-043).
6. **FE-046 — Pairs pass contrast before they are named.** A semantic foreground/background pair is only admitted to the token set after its WCAG ratio is computed: ≥ 4.5:1 for body text, ≥ 3:1 for large text and non-text indicators — including pairs that sit on tinted or gradient surfaces (DET-VIS-022).
7. **FE-047 — The palette has roles, not a hue.** The color system defines primary, secondary, semantic (success / warning / error), and a neutral ramp as distinct tokens. One accent hue covering every role, semantic states included, fails review (DET-VIS-020).
8. **FE-048 — Gradients are tokens with a reason, or absent.** A gradient exists only as a named token whose description states its brand basis and where it may be used. The violet-blue linear gradient is never a default primary, background, or text treatment (DET-VIS-017, DET-VIS-018).
9. **FE-049 — Dark surfaces are layered, not glowing.** Dark themes are built from layered surface tokens with restrained elevation; colored glow shadows are not an elevation device (DET-VIS-019).
10. **FE-050 — Token changes are reviewed as diffs.** Any change to the token source ships with a diff review and the design-system changelog entry (FE-024); a changed value with no diff review is treated as an accidental edit.

## BAN list

- **BAN-FE-021 — Raw values in component styles.** Banned: hex codes, pixel values, or millisecond literals written directly in component or page styles. Defeats: DET-VIS-020. Bad: `.btn-primary { background: #6d5df6; padding: 13px 22px; }` — a one-off violet and an off-scale padding that exist nowhere in the token set and will never theme, never be audited, and never match the next page. Instead: `background: var(--color-action-primary); padding: var(--space-control-y) var(--space-control-x)`. Severity: BLOCK.
- **BAN-FE-022 — The violet-blue gradient as default.** Banned: a purple-to-blue (or purple-to-pink) linear gradient as the site's primary color event — hero background, buttons, or clipped into headline text. Defeats: DET-VIS-017. Bad: hero background, primary button, and H1 all carrying `linear-gradient(90deg,#8b5cf6,#3b82f6)`. Instead: a chosen solid brand color with a supporting palette; a gradient only as a named token with a stated brand basis (FE-048). Severity: BLOCK.
- **BAN-FE-023 — Text on an unchecked surface.** Banned: naming a text/surface token pair that has never had its contrast ratio computed. Defeats: DET-VIS-022. Bad: white button text on a mid-tone amber panel chosen by eye, measuring 2.9:1 — unreadable for body-size text and never checked. Instead: darken the foreground token or deepen the surface until the pair computes ≥ 4.5:1, then admit the pair (FE-046). Severity: BLOCK.
- **BAN-FE-024 — One shadow for everything.** Banned: a single box-shadow value applied to cards, menus, modals, and buttons alike. Defeats: DET-VIS-021. Bad: `box-shadow: 0 8px 30px rgba(0,0,0,.12)` on every elevated element regardless of height or light direction. Instead: the elevation scale — subtle for cards, deeper for menus and modals, matched to one light direction (FE-045). Severity: WARN.
- **BAN-FE-025 — Radius scatter.** Banned: unrelated border-radius values assigned per component with no role pattern. Defeats: DET-VIS-043. Bad: 8px cards, 12px buttons, 24px images, full-pill inputs on one page — pieces pasted from different templates. Instead: the radius scale applied by role (input / card / pill) everywhere (FE-045). Severity: WARN.

## Gates

- **G-FE-021 — Token build in CI.** Verifies: FE-041, FE-042, FE-044. Check: automated — Style Dictionary build runs in CI; a broken alias, a missing `$type`, or a hand-edited output file fails the build. Pass: build green and outputs regenerate byte-identical from source. Fail: block shipment. Recorded in: progress.md.
- **G-FE-022 — Literal lint.** Verifies: FE-043. Check: automated — a stylelint custom rule (or grep script) fails on hex, px, or ms literals in component and page style files, excluding the token source and generated outputs. Pass: zero hits. Fail: block until values move into tokens. Recorded in: progress.md.
- **G-FE-023 — Contrast script.** Verifies: FE-046, FE-047. Check: automated — a script computes the WCAG ratio for every semantic text-on-surface token pair, including tinted and gradient surfaces. Pass: every pair ≥ 4.5:1 (≥ 3:1 for pairs designated large-text or non-text). Fail: block; the pair is not admitted or is fixed. Recorded in: progress.md.
- **G-FE-024 — Token diff review.** Verifies: FE-044, FE-050. Check: manual — review the token diff for the release: new tokens have descriptions, retired tokens are `$deprecated` with replacements, no scale gained a step without a role. Pass: diff approved and changelog entry present. Fail: warn and hold the token change. Recorded in: progress.md.

## Anti-patterns

- **Token sprawl.** Forty near-identical grays and six "primary" blues accumulate because adding a token is easier than choosing one. Catch it: count tokens per role at review; duplicates collapse into one semantic name.
- **The bypass variable.** A component defines a local CSS variable with a raw value to "just fix this one screen" — a primitive smuggled past the lint. Catch it: the literal lint covers local variable definitions too (G-FE-022).
- **Theme by duplication.** Dark mode ships as a second, diverging token file instead of semantic-tier overrides. Catch it: both themes must resolve the same semantic names (FE-042); a name existing in only one theme fails the build review.
- **Deprecated forever.** Tokens marked `$deprecated` years ago are still referenced by live components. Catch it: the build report lists references to deprecated tokens; the count must trend to zero.

## Examples

- [Example 1 — Hard-coded values become semantic tokens](examples/example-1.md) — corrects FE-043.
- [Example 2 — An unchecked amber pair becomes a passing token pair](examples/example-2.md) — corrects FE-046.
- [Example 3 — One default shadow becomes an elevation scale](examples/example-3.md) — corrects FE-045.

## Recall anchors

- Values live in tokens; components name roles, never numbers.
- Three tiers; themes override semantic names, not files.
- A pair passes contrast before it is named.
- Scales have roles — radius, elevation, spacing, duration.
- Retire with `$deprecated` and a pointer, never by deletion.

## Checklist

- [ ] Token source is DTCG JSON; outputs regenerate cleanly (G-FE-021).
- [ ] No raw hex/px/ms literals in component or page styles (G-FE-022).
- [ ] Every token carries a `$description` (FE-044).
- [ ] Every semantic text/surface pair computes ≥ 4.5:1 or ≥ 3:1 large (G-FE-023).
- [ ] Palette defines primary, secondary, semantic, and neutral roles (FE-047).
- [ ] Elevation and radius applied by role from their scales (FE-045).
- [ ] Any gradient is a named token with a stated brand basis (FE-048).
- [ ] Token diff reviewed; deprecations point at replacements (G-FE-024).

<!-- END EMBEDDED: Skill: design-tokens -->


---

<!-- BEGIN EMBEDDED: Skill: typography — source: skills/frontend/typography/SKILL.md -->

# typography

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** GOV.UK Design System, headings and typography styles — https://design-system.service.gov.uk/styles/headings/ ; Design Tokens Format Module 2025.10 (typography tokens) — https://www.designtokens.org/tr/2025.10/
- **Depends on:** design-tokens
- **Feeds into:** frontend-core, component-library, forms

## When to use / Do NOT use

- **Use when:** defining or reviewing a type system; setting headings, body, captions, or data text; choosing or loading font families; fixing flat hierarchy, arbitrary sizes, or unfinished prose detail.
- **Do NOT use when:** the question is which token file or transform pipeline holds the values — that is design-tokens. Do not use this skill to set text color pairs; contrast pairs are chosen in design-tokens and only consumed here (FE-146).

## Rules

1. **FE-141 — Sizes come only from the type scale.** Every font size in a component is a type-scale token (display, heading levels, body, caption, data). An off-scale size is a defect (DET-VIS-012).
2. **FE-142 — Hierarchy is unmistakable.** On marketing and editorial pages the largest heading is at least 2.5× body size, heading levels step down clearly, and captions are distinctly smaller than body (DET-VIS-012).
3. **FE-143 — Case and weight vary by level and purpose.** Heading levels differ in size and, where the design calls for it, weight or case; one weight and one case pattern across every level fails review (DET-VIS-015).
4. **FE-144 — Micro-typography is finished work.** Prose uses real quotation marks and en/em dashes, uppercase labels are tracked out, and tables and data use tabular numerals (DET-VIS-014).
5. **FE-145 — Emphasis is solid.** Emphasis is achieved with weight, size, italic, or a solid accent color; gradient-clipped headline text is not a default device (DET-VIS-018).
6. **FE-146 — Body text meets AA contrast.** Body and caption text — including "muted" gray styles — meet WCAG AA (4.5:1, 3:1 for large text) on the surface they sit on.
7. **FE-147 — Two families, only the weights used.** A project loads at most two font families and only the weights its scale actually uses, self-hosted or delivered with subsetting and `font-display: swap` (or the stack's equivalent).
8. **FE-148 — Line length and leading are set per size.** Body columns run near 45–80 characters, and line-height is specified per type role — display text tight, body text open — never one leading for all sizes (DET-VIS-013).
9. **FE-149 — Fluid sizing comes from tokens.** Responsive type uses `clamp()` ranges defined in the type tokens (minimum, preferred, maximum), not per-component viewport arithmetic.
10. **FE-150 — Emoji are never structural.** Emoji do not appear as heading decoration, list markers, or iconography in the interface (DET-VIS-016); icons come from the component library's icon set.
11. **FE-151 — Inherited typography law.** The WCPM TYP parameter family applies as cited in docs/WCPM_MAPPING.md §2.4, and typography work is designed to pass the G-VIS gate family.

## BAN list

- **BAN-FE-071 — Gradient headline text.** Banned: `background-clip: text` gradient fills on headlines as the default emphasis device. Defeats: DET-VIS-018. Bad: every H1 on the site is a purple-to-blue gradient. Instead: a solid token color with weight and size doing the emphasis (FE-145). Severity: WARN.
- **BAN-FE-072 — Off-scale font sizes.** Banned: any font size that is not a type-scale token value. Defeats: DET-VIS-012. Bad: components variously set 13px, 15px, 17.5px, and 22px by eye. Instead: the nearest scale step, or a new step added to the scale with a role (FE-141). Severity: BLOCK.
- **BAN-FE-073 — Emoji as iconography.** Banned: emoji used in headings, navigation, feature lists, or buttons in place of icons. Defeats: DET-VIS-016. Bad: feature headings read "🚀 Fast", "🔒 Secure", "📊 Insightful". Instead: the library's icon set, or no icon at all. Severity: BLOCK.
- **BAN-FE-074 — Monotone headings.** Banned: every heading level set in the same weight and the same case pattern. Defeats: DET-VIS-015. Bad: H1 through H4 are all uppercase 600-weight, differing only slightly in size. Instead: a per-level case/weight scheme recorded in the type tokens (FE-143). Severity: WARN.
- **BAN-FE-075 — Unexamined default pairing.** Banned: shipping the framework's or generator's default font pairing as the design without a recorded choice. Defeats: DET-VIS-011. Bad: the site launches in the starter template's fonts because nobody picked any. Instead: choose families against the brand and content, record the choice, load per FE-147. Severity: WARN.

## Gates

- **G-FE-071 — Computed-style type audit.** Verifies: FE-141, FE-142. Check: automated — a script lists distinct font families, sizes, and weights rendered on each main page and diffs them against the type-scale tokens. Pass: every rendered value is in the scale and the largest heading is ≥ 2.5× body on marketing pages. Fail: block shipment. Recorded in: progress.md.
- **G-FE-072 — Font payload check.** Verifies: FE-147, FE-149. Check: automated — the build report lists loaded families and weights; fail if families exceed two, a loaded weight is unused by the scale, or `clamp()` ranges in components are not token values. Pass: all three conditions clean. Fail: warn; a third family blocks. Recorded in: progress.md.
- **G-FE-073 — Micro-typography scan.** Verifies: FE-144. Check: manual — scan headings and prose for straight quotes, hyphens used as dashes, untracked uppercase labels, and proportional numerals in data tables. Pass: no instances on main pages. Fail: warn and fix before release. Recorded in: progress.md.
- **G-FE-074 — Text contrast verification.** Verifies: FE-146. Check: automated — run the design-tokens contrast script over every text-on-surface token pair actually used, including muted styles. Pass: all pairs ≥ 4.5:1 (3:1 large text). Fail: block shipment. Recorded in: progress.md.

## Intelligence — decisions & gates

> **Judgment layer.** These decisions apply the judgment layer above this skill — `skills/frontend/design-intelligence/SKILL.md` and the theme library (`skills/frontend/theme-library/`). Settle the theme's art direction there first, then decide here inside it; where a decision below and a rule above disagree, the rule above wins.

### Decision rules — choosing type

| Decision | Read the situation | Decide |
|---|---|---|
| Family pairing | Expressive or editorial brand | A characterful display face for headings over a quiet text face; the display face is the brand voice, the text face disappears. |
| Family pairing | Product UI or data product | One grotesque family across a wide weight range; spend the second family only if editorial content truly needs it (FE-147). |
| Scale ratio | Long-form reading dominates | A gentler ratio (≈1.2–1.25) with more steps, so adjacent levels stay calm and scannable. |
| Scale ratio | Marketing or landing pages | A steeper ratio (≈1.333–1.5) with fewer steps; the display step does the persuading (FE-142). |
| Measure | Articles and essays vs docs and panels | 55–70 characters for essays; 45–60 for documentation and UI panels; hero lines are set deliberately, never run to the container edge (FE-148). |
| Body floor | Older or low-literacy audience | Body at 16px or above with open leading; never trade legibility for density. |
| Numerals | Prices, tables, metrics in the content | Tabular lining figures wherever data aligns; old-style figures belong to prose only (FE-144). |
| Loading strategy | Performance-sensitive audience or slow networks | One variable font or a system stack beats two static families; subset and swap (FE-147, FE-149). |
| Script coverage | Multilingual audience | Choose families with full coverage of the shipped scripts before judging aesthetics; a beautiful face missing a script is a defect, not a trade-off. |

### Self-check gate

- **G-FE-075 — Pre-ship intelligence self-check (typography).** Verifies: FE-141, FE-142, FE-143, FE-144, FE-146, FE-148 as judgment, not just compliance. Check: manual — the builder scores each item pass/fail on the shipped pages: (1) ★ squint test — blur or step back: heading levels still read as distinct bands of emphasis; (2) ★ on marketing and editorial pages the largest heading is at least 2.5× body size; (3) every rendered size is a scale step — no strays in computed styles; (4) body columns measure 45–80 characters at the widest viewport; (5) data uses tabular numerals, and quotes and dashes are finished typography; (6) muted and caption styles pass AA on the actual surfaces they sit on. Pass: both ★ items pass and at least 5 of 6 overall. Fail: fix, or log a written exception, before shipping. Recorded in: progress.md.

### Anti-pattern table — symptom → cause → fix

| Symptom | Cause | Fix |
|---|---|---|
| Hierarchy collapse — heading, subheading, and body sit within ~1.2× of each other and nothing leads | Scale ratio too flat; sizes picked per component by eye | Re-derive the scale with a steeper ratio; largest heading ≥ 2.5× body (FE-142). |
| Measure drift — line length swings from 40 to 110 characters across templates | Container widths set by layout habit, not by type role | Set measure per role in the type tokens and hold 45–80 characters (FE-148). |
| Scale without rhythm — sizes form a scale, yet pages feel uneven and restless | Type scale defined without a matching leading and spacing rhythm | Tie line-height and vertical margins to the same modular scale; leading per role, never one value for all sizes (FE-148). |
| Weight-only hierarchy — every level is the same face at similar size, separated only by bold | The display step was never created; large type felt risky | Add a display step and vary case and weight per level under a recorded scheme (FE-143). |
| Elegant gray captions nobody can read | Muted color chosen by eye on white, then placed on tinted surfaces | Verify every muted pair on its actual surface (FE-146, G-FE-074). |
| Font tourism — a fashionable display face fights the copy (condensed face, endless headlines; script face in UI) | Family chosen from a gallery, never tested against real content | Adopt a face only after it survives the product's longest real headline and a full body paragraph; record the choice (FE-147). |
| Prices and table columns jitter and refuse to align | Default proportional figures used in data | Tabular numerals for all data text (FE-144). |

## Anti-patterns

- **Arbitrary size creep.** A 13.5px here and a 15px there accumulate until no scale exists. Catch it: if the computed-style audit lists more sizes than the scale has steps, creep has already happened.
- **All-caps everything.** Headings, labels, buttons, and body emphasis all shouted in uppercase. Catch it: count distinct case patterns; one pattern everywhere is the tell.
- **Muted-gray body text.** Body copy set in a light gray that "looks softer" and fails AA. Catch it: run the contrast check on the muted style specifically, not just the default body pair.
- **Straight quotes in finished prose.** Prose ships with typewriter quotes and hyphens where dashes belong. Catch it: the micro-typography scan (G-FE-073) exists precisely for this.

## Examples

- [Example 1 — Flat arbitrary sizes replaced by a token scale](examples/example-1.md) — corrects FE-141, FE-142.
- [Example 2 — Gradient headline and straight quotes finished properly](examples/example-2.md) — corrects FE-145, FE-144.
- [Example 3 — Monotone headings given a per-level scheme](examples/example-3.md) — corrects FE-143.

## Recall anchors

- Sizes come from the scale or they do not ship.
- Hierarchy you can see from across the room.
- Emphasis is solid: weight, size, italic, accent.
- Quotes, dashes, and numerals are finished work.
- Two families, only the weights used.

## Checklist

- [ ] Computed-style audit matches the type scale exactly (G-FE-071).
- [ ] Largest heading is ≥ 2.5× body size on marketing/editorial pages (FE-142).
- [ ] Heading levels vary in case/weight per the recorded scheme (FE-143).
- [ ] No gradient headline text; no emoji in headings or UI structure (BAN-FE-071, BAN-FE-073).
- [ ] Font payload is ≤ 2 families with only used weights (G-FE-072).
- [ ] Muted text styles pass AA contrast (G-FE-074).
- [ ] Micro-typography scan is clean (G-FE-073).

<!-- END EMBEDDED: Skill: typography -->


---

<!-- BEGIN EMBEDDED: Skill: layout-responsive — source: skills/frontend/layout-responsive/SKILL.md -->

# layout-responsive

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** GOV.UK Design System, layout styles — https://design-system.service.gov.uk/styles/layout/ ; WCAG 2.2 criteria summary (reflow SC 1.4.10, target size SC 2.5.8) — https://convarso.com/blog/web-accessibility-guide-wcag/
- **Depends on:** design-tokens, design-system
- **Feeds into:** frontend-core, forms, data-visualisation

## When to use / Do NOT use

- **Use when:** building or reviewing any page or component layout; choosing breakpoints or container widths; fixing overflow, clipping, or a mobile view that is a squeezed desktop page.
- **Do NOT use when:** the decision is a token value (spacing, radius scales) — that is design-tokens. Do not use this skill to justify hiding content on mobile; hiding is a content decision owned by the page's requirements, and FE-131 still applies.

## Rules

1. **FE-121 — No page-level horizontal scrolling.** At every width from 320 CSS px up, the page itself never scrolls horizontally (DET-VIS-038; WCAG 1.4.10 reflow). Overflow is fixed in the layout, never by clipping the page.
2. **FE-122 — Breakpoints where content breaks.** Layouts are fluid first; a breakpoint is added at the width where the content actually fails, and breakpoints are named for the layout change (`nav-collapses`, `cards-two-up`), never for a device.
3. **FE-123 — Mobile is recomposed, not stacked.** Small-screen layouts reorder by priority — primary content and actions first — instead of stacking desktop DOM order top to bottom (DET-VIS-037).
4. **FE-124 — Targets stay tappable at every width.** Interactive targets are at least 24×24 CSS px (WCAG 2.5.8 floor) at every breakpoint; 44px is the working target for primary actions.
5. **FE-125 — Heroes size to content.** Hero height comes from `min-height` plus content and padding; fixed `100vh` or pixel heights that can clip text or CTAs on short screens are forbidden (DET-VIS-039).
6. **FE-126 — Width follows content role.** Reading content, galleries, data tables, and media each get the width their role needs; one container width applied to every section is a defect (DET-VIS-005).
7. **FE-127 — Reading measure is held.** Body-text columns stay near 45–80 characters at wide viewports instead of running to the container edge.
8. **FE-128 — Media space is reserved before load.** Every image and embed carries `width`/`height` or an `aspect-ratio`, so layout does not shift when assets arrive (CLS budget, frontend-core).
9. **FE-129 — Components respond to their own space.** A component used in both wide and narrow contexts adapts with container queries to the space it is given, not with page-level breakpoints written for one placement.
10. **FE-130 — Wide content is contained or reformatted.** Tables, code blocks, and charts get a contained scroll region or a small-screen reformat (stacked rows, priority columns); they never force page overflow and are never silently truncated.
11. **FE-131 — Nothing essential disappears on small screens.** Content or actions removed at a breakpoint must be reachable another way on that viewport; "it didn't fit" is not a removal reason (DET-VIS-037).
12. **FE-132 — Inherited layout law.** The WCPM LAY, SEC, and SPC parameter families apply as cited in docs/WCPM_MAPPING.md §2.4, and layout work is designed to pass the G-EXP gate family.

## BAN list

- **BAN-FE-061 — Fixed-height hero.** Banned: a hero with a fixed `100vh` or pixel height whose text or CTA clips on short or landscape screens. Defeats: DET-VIS-039. Bad: `.hero { height: 100vh; }` cuts the signup button off on a 667px-tall phone. Instead: `min-height` sized by content, with the CTA always in flow. Severity: BLOCK.
- **BAN-FE-062 — Page-level horizontal overflow.** Banned: shipping a page where `scrollWidth` exceeds the viewport at any width ≥ 320px. Defeats: DET-VIS-038. Bad: a 900px-wide pricing table forces sideways page scrolling on every phone. Instead: a contained scroll region or a stacked reformat for the table (FE-130). Severity: BLOCK.
- **BAN-FE-063 — Essential content hidden on mobile.** Banned: `display: none` on content or actions at small breakpoints with no alternate path to them. Defeats: DET-VIS-037. Bad: the spec sheet and the support link vanish below 768px "because they didn't fit." Instead: recompose by priority (FE-123) or move the content behind a reachable disclosure. Severity: BLOCK.
- **BAN-FE-064 — One container width for every section.** Banned: a single `.container` max-width governing prose, galleries, tables, and media alike. Defeats: DET-VIS-005. Bad: a photo gallery squeezed into the 65ch reading column. Instead: width tokens per content role (FE-126). Severity: WARN.
- **BAN-FE-065 — Uniform section template.** Banned: every section shipping with identical padding, alignment, and loudest element regardless of its role. Defeats: DET-VIS-001. Bad: hero, features, proof, and pricing all render as centered text in the same vertical rhythm. Instead: composition varies by section role, per design-system. Severity: WARN.

## Gates

- **G-FE-061 — Overflow assertion.** Verifies: FE-121, FE-130. Check: automated — Playwright loads every route at 320/390/768/1440px and asserts `document.scrollingElement.scrollWidth <= window.innerWidth` on each. Pass: zero routes overflow at any width. Fail: block shipment. Recorded in: progress.md.
- **G-FE-062 — Screenshot matrix review.** Verifies: FE-123, FE-125, FE-131. Check: manual — review screenshots at 320/390/768/1440px per main page; confirm priority order on mobile, unclipped heroes, and no essential content missing at small widths. Pass: all four widths conform. Fail: block shipment. Recorded in: progress.md.
- **G-FE-063 — Target-size audit.** Verifies: FE-124. Check: automated — a script reads computed sizes of all interactive elements at 390px and fails any below 24×24 CSS px. Pass: zero undersized targets. Fail: warn; a primary action below the floor blocks. Recorded in: progress.md.
- **G-FE-064 — Resize walk.** Verifies: FE-122, FE-127. Check: manual — drag the viewport continuously from 320px to 1920px on the main pages, watching for overlap, orphaned controls, and unreadable line lengths between breakpoints. Pass: no failure at any intermediate width. Fail: warn and log the failing width range. Recorded in: progress.md.

## Intelligence — decisions & gates

> **Judgment layer.** These decisions apply the judgment layer above this skill — `skills/frontend/design-intelligence/SKILL.md` and the theme library (`skills/frontend/theme-library/`). Settle the theme's art direction there first, then decide here inside it; where a decision below and a rule above disagree, the rule above wins.

### Decision rules — composing layout

| Decision | Read the situation | Decide |
|---|---|---|
| Layout model | Editorial content | A measure-led single column with deliberate breakout media; the reading line is the layout. |
| Layout model | Product or app surface | A grid with persistent navigation and stable regions; users build a spatial map and resent it moving. |
| Layout model | Gallery or portfolio | A fluid grid keyed to media aspect ratios, not to a card template. |
| How many breakpoints | Content complexity | One breakpoint per named layout change (FE-122); two well-placed beats three guessed at device widths. |
| Mobile priority order | The audience's primary task | The primary task's content and action come first; proof and secondary material move below — never raw DOM order (FE-123). |
| Density | Expert desktop users vs consumer mobile-first audience | Experts may get denser grids; consumer small screens get generous targets and air (FE-124). Density is an audience decision, not a taste. |
| Wide-screen behavior | Content role at 1600px+ | Reading measure stays capped; media and data may use the width. Prose stretched to the viewport edge is a defect (FE-126, FE-127). |
| Sticky elements | Whether the element serves the primary task at that width | At most one sticky element per viewport; on small screens a sticky element must earn its scarce height or scroll away. |
| Wide-table strategy | Data shape | Few columns: reformat with priority columns. Many columns: contained scroll region with a sticky first column (FE-130). Never page overflow, never silent truncation. |

### Self-check gate

- **G-FE-065 — Pre-ship intelligence self-check (layout).** Verifies: FE-122, FE-123, FE-126, FE-127, FE-131 as judgment, not just compliance. Check: manual — the builder scores each item pass/fail on the shipped pages: (1) ★ a continuous resize walk from 320px to 1920px shows no breakage at any in-between width; (2) ★ at 390px the content order is the priority order, not the desktop DOM order; (3) nothing essential is unreachable at small widths; (4) gaps between sibling sections all come from the spacing scale — no eyeballed one-offs; (5) at wide viewports prose holds its measure while media and data use their own widths; (6) at most one sticky element is visible per viewport. Pass: both ★ items pass and at least 5 of 6 overall. Fail: fix, or log a written exception, before shipping. Recorded in: progress.md.

### Anti-pattern table — symptom → cause → fix

| Symptom | Cause | Fix |
|---|---|---|
| Grid monotony — every section is the same three-column card grid | One layout pattern reused for every content role | Assign composition per role: prose, proof, gallery, and data each get their own structure (FE-126; design-system FE-025). |
| Spacing chaos — sibling sections are separated by 13px here, 41px there | Spacing set per component by eye; no shared rhythm | Take every gap from the spacing scale (design-tokens) and audit sibling gaps side by side. |
| Breakpoint afterthoughts — the layout breaks at widths nobody tested, between the "official" sizes | Breakpoints placed at device sizes and checked only at those sizes | Place breakpoints where content breaks (FE-122) and run the resize walk (G-FE-064). |
| The squeezed desktop — the phone view is the desktop page at 40% scale | Compression substituted for recomposition | Recompose by priority; re-decide type, targets, and order for small screens (FE-123). |
| The hero eats the page — content starts below the fold on short screens, CTA clipped | Fixed viewport height chosen as a style | `min-height` sized by content, CTA always in flow (FE-125). |
| Container tyranny — galleries and tables squeezed into the prose column | A single container width governing every role | Width tokens per content role (FE-126). |
| Sticky pile-up — nav, banner, and CTA bar consume half the phone screen | Each feature added its own sticky element in isolation | One sticky element per viewport; the rest scroll away. |

## Anti-patterns

- **The 768 stack.** One `max-width: 768px` query stacks everything in DOM order and calls it the mobile design. Catch it: if the mobile order is the desktop order, no recomposition happened (FE-123).
- **Desktop-first afterthought.** The desktop page is finished, then squeezed until it fits a phone. Catch it: check whether spacing, type, and targets were re-decided for small screens or merely compressed.
- **Device-named breakpoints.** Breakpoints called "tablet" or "iPhone" encode hardware, not content failure. Catch it: read the breakpoint names; a device name means the breakpoint was placed by guess.
- **Shrink-to-fit type.** Text is made smaller and smaller at narrow widths instead of the layout changing. Catch it: body text below the type scale's minimum at any width is the tell.

## Examples

- [Example 1 — Fixed-height hero that clips its CTA](examples/example-1.md) — corrects FE-125.
- [Example 2 — Wide table overflowing the page](examples/example-2.md) — corrects FE-121, FE-130.
- [Example 3 — DOM-order stack recomposed by priority](examples/example-3.md) — corrects FE-123.

## Recall anchors

- No page scroll sideways, ever, from 320px up.
- Mobile is recomposed by priority, not stacked.
- Heroes size to content; nothing essential is hidden.
- Width follows the content's role.
- Breakpoints live where content breaks, not on devices.

## Checklist

- [ ] Overflow assertion passes on every route at 320/390/768/1440px (G-FE-061).
- [ ] Mobile order follows priority, not desktop DOM order (FE-123).
- [ ] All interactive targets are ≥ 24×24 CSS px at mobile widths (G-FE-063).
- [ ] Heroes use `min-height` and cannot clip text or CTAs (FE-125).
- [ ] Container widths vary by content role (FE-126).
- [ ] Wide tables and code are contained or reformatted (FE-130).
- [ ] Nothing essential is unreachable on small screens (FE-131).

<!-- END EMBEDDED: Skill: layout-responsive -->


---

<!-- BEGIN EMBEDDED: Skill: component-library — source: skills/frontend/component-library/SKILL.md -->

# component-library

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Structuring your Storybook (component-driven development, stories per variant and state) — https://storybook.js.org/blog/structuring-your-storybook/ ; GOV.UK Design System, button component — https://design-system.service.gov.uk/components/button/
- **Depends on:** design-tokens, design-system
- **Feeds into:** frontend-core, layout-responsive, forms, ui-states

## When to use / Do NOT use

- **Use when:** building, extending, or reviewing the components pages are assembled from — their variants, state sets, iconography, and content stress behavior. WCPM's component bans and the CMP and ICO families land here, as does the component half of WCPM §8 (components & states).
- **Do NOT use when:** the state belongs to a data view rather than a component (ui-states owns the view-level state matrix), or the question is page composition (layout-responsive, design-system). Components are built here; pages are composed elsewhere.

## Rules

1. **FE-061 — Built bottom-up, in the workshop.** Components are built and reviewed in Storybook, isolated from pages, one story per variant and per state. A component first seen inside a finished page was never reviewed.
2. **FE-062 — The full state set, or a written exception.** Every component ships its applicable states — default, hover, focus-visible, active, disabled, loading, error — or its state matrix states explicitly why a state does not apply (DET-VIS-032).
3. **FE-063 — Behavior lives in the component.** Focus order, keyboard interaction, disabled semantics, and ARIA wiring are implemented and tested once, inside the component — never re-implemented per page.
4. **FE-064 — One icon set.** One icon library or custom set, one stroke weight, one metaphor style across the whole library (DET-VIS-025). A second set is a system change (FE-024), not a per-component choice.
5. **FE-065 — Emoji are never structural icons.** Icons in headings, feature lists, and navigation are drawn icons from the set. Emoji may appear in informal copy, never as the icon for a feature (DET-VIS-016).
6. **FE-066 — Stress-tested with real content.** Components are tested with the longest real names, labels, and words the product will hold; overflow, clipping, or broken wrapping at ordinary content lengths is a component bug (DET-VIS-007).
7. **FE-067 — Variants express hierarchy.** Button and action variants differ by emphasis and context (primary / secondary / destructive / text; sizes by placement), not one treatment at one size for every action (DET-VIS-031). Destructive actions are never styled as primary.
8. **FE-068 — Badges carry actionable information.** A badge or pill states something the user can act on — a status, a genuine novelty, a filterable category. Decorative labeling is removed (DET-VIS-033).
9. **FE-069 — Cards earn their weight.** In a grid, content of unequal importance gets unequal weight: one item may be featured, span wider, or carry richer media. Identical cards are permitted only where the content is genuinely parallel — and their copy must still be specific, not interchangeable (DET-VIS-003).
10. **FE-070 — Pages assemble, they do not imitate.** A page needing something new extends the library; hand-rolled markup that duplicates a library component is a defect, found by the grep gate (G-FE-033), not by taste.

## BAN list

- **BAN-FE-031 — The interchangeable card grid.** Banned: a grid of identical cards whose descriptions could be swapped between cards — or between products — without anyone noticing. Defeats: DET-VIS-003. Bad: three feature cards of identical height and two-line descriptions ("Powerful tools for modern teams", "Built for the way you work", "Everything you need to succeed") that fit any SaaS product ever made. Instead: cards weighted by importance (FE-069) with copy that names this product's specific capability. Severity: WARN.
- **BAN-FE-032 — The icon-in-tinted-circle formula.** Banned: every feature icon presented in an identical soft-tinted circle or rounded square in the accent color, in every grid on the site. Defeats: DET-VIS-026. Bad: six features, six identical lavender circles, repeated unchanged on three pages. Instead: icon treatment that varies by context or uses a distinctive brand device; the chip is one option, not the universal default. Severity: WARN.
- **BAN-FE-033 — Emoji as feature icons.** Banned: 🚀 ⚡ 🔒-style emoji prefixed to feature headings or list items in place of an icon system. Defeats: DET-VIS-016. Bad: "🚀 Fast setup", "🔒 Secure by default", "⚡ Blazing performance" as the product's feature list. Instead: drawn icons from the library's single set (FE-064). Severity: BLOCK.
- **BAN-FE-034 — One button for everything.** Banned: a single button size, radius, and treatment for every action on the site, primary and secondary differing only by fill. Defeats: DET-VIS-031. Bad: the nav CTA, the hero CTA, the delete-account action, and the form submit are the same pill at the same size; delete differs from save only by being red. Instead: a variant hierarchy by emphasis and context, with destructive actions distinctly styled and never primary (FE-067). Severity: WARN.
- **BAN-FE-035 — The template pricing table.** Banned: the three-tier, middle-highlighted, check-icon pricing table applied to a product whose model is not seat-based SaaS. Defeats: DET-VIS-036. Bad: a usage-based API product squeezed into Starter/Pro/Enterprise tiers with a "Most Popular" pill and feature rows differing by one line. Instead: pricing presentation that follows the actual model — usage bands, a calculator, one-time pricing (pricing rules owned by D1's pricing-monetization). Severity: WARN.

## Gates

- **G-FE-031 — Storybook visual regression.** Verifies: FE-061, FE-062, FE-066. Check: automated — Storybook test-runner plus screenshot visual regression over all stories runs in CI, including the long-content stress stories. Pass: all tests green, zero unreviewed screenshot diffs. Fail: block shipment. Recorded in: progress.md.
- **G-FE-032 — State matrix coverage.** Verifies: FE-062, FE-063. Check: manual — walk the state matrix per component: every applicable state (default, hover, focus-visible, active, disabled, loading, error) has a story, and every non-applicable state has its written reason. Pass: matrix complete. Fail: warn and hold the component. Recorded in: progress.md.
- **G-FE-033 — Duplicate-markup grep.** Verifies: FE-070. Check: automated — grep page code for raw `<button`/`<input`/`<select` markup duplicating a library component, and for icon imports outside the library's single set (FE-064). Pass: zero hits. Fail: block until the page uses the library. Recorded in: progress.md.
- **G-FE-034 — Icon and badge audit.** Verifies: FE-064, FE-065, FE-068. Check: manual + automated — scan headings and feature lists for emoji codepoints (automated); screenshot all icons in one view to check stroke weight and metaphor consistency; count badges per viewport and name the action each enables. Pass: no structural emoji, one icon style, every badge actionable. Fail: warn; block if emoji carry a feature list. Recorded in: progress.md.

## Intelligence — decisions & gates

> **Judgment layer.** These decisions apply the judgment layer above this skill — `skills/frontend/design-intelligence/SKILL.md` and the theme library (`skills/frontend/theme-library/`). Settle the theme's art direction there first, then decide here inside it; where a decision below and a rule above disagree, the rule above wins.

### Decision rules — growing the library

| Decision | Read the situation | Decide |
|---|---|---|
| New component or new variant | What actually differs | Emphasis, size, or content only: a variant. Behavior or anatomy differs: a new component. |
| When to abstract | Evidence of reuse | First real use may stay page-level; the second use is the signal to build the library component; a third page-level copy is a defect (FE-070). |
| Variant budget | Whether the variants can still be enumerated | Past roughly six variants, the design is asking for two components — split by purpose rather than adding a seventh. |
| Content model | The product's real data | Design and stress-test against the longest real names and labels the product holds, including other shipped languages (FE-066). |
| Icon treatment | The component's context | Dense UI (nav, toolbars): icons carry meaning and may stand alone. Marketing: icons support specific copy, never replace it (FE-064, FE-065). |
| Card weight | Whether the content is genuinely parallel | Parallel items get equal cards; unequal importance gets a featured, wider, or richer treatment (FE-069). |
| Destructive styling | The action's risk | Destructive actions get a distinct treatment and a confirmation pattern; they are never styled as primary (FE-067). |
| Badge use | Whether the user can act on it | A badge ships only if it states something actionable — a status, genuine novelty, a filter (FE-068). Decorative badges are removed. |

### Self-check gate

- **G-FE-035 — Pre-ship intelligence self-check (components).** Verifies: FE-062, FE-064, FE-066, FE-067, FE-068, FE-070 as judgment, not just compliance. Check: manual — the builder scores each item pass/fail against the library: (1) ★ every component has a story per variant and per applicable state, or a written exception in its state matrix; (2) ★ the longest real content the product holds renders in every text-bearing component without overflow or clipping; (3) every component in the library has a second real use, present or concretely planned — single-use components are demoted to page code; (4) a new hire could enumerate each component's variants from its documentation alone; (5) every badge on the page names an action the user can take; (6) destructive actions are visually distinct from, and never styled as, primary actions. Pass: both ★ items pass and at least 5 of 6 overall. Fail: fix, or log a written exception, before shipping. Recorded in: progress.md.

### Anti-pattern table — symptom → cause → fix

| Symptom | Cause | Fix |
|---|---|---|
| Component soup — forty components, half of them used exactly once | Abstraction on first use, with no reuse evidence | Demote single-use components to page code; a library entry requires a second real use. |
| Variant explosion — the button has fourteen variants nobody can list | Every page request was granted a variant instead of a decision | Cap the variants, split by purpose, and document each variant's "do not use when" (design-system FE-023). |
| State gaps debut in production — disabled and loading states are broken in the app, fine in the mockups | Stories were built for default and hover only | Ship the full state set or a written exception (FE-062); check coverage against stories (G-FE-032). |
| Placeholder-perfect, real-content broken — cards clip the longest customer name | Components were tested with "John Doe" and lorem ipsum | Stress stories with the longest real content (FE-066). |
| Lookalike duplication — pages hand-roll near-copies of library components | The library component almost fit, so the page team routed around it | Extend the component; find imitations with the grep gate (G-FE-033). |
| Prop sprawl — a component takes twenty props and behaves unpredictably in combination | Configuration was used to avoid making design decisions | Decide variants; props carry content, not layout personalities. |
| Mixed iconography — two stroke weights and two metaphor styles across pages | Icons imported ad hoc, per page and per component | One set, one stroke weight (FE-064); audit with G-FE-034. |

## Anti-patterns

- **The near-duplicate folder.** `Card`, `CardNew`, `PricingCard2`, and `FeatureCardOld` coexist because extending the original felt risky. Catch it: inventory the library at review; duplicates merge into variants of one component or are deleted.
- **The bypass page.** Under deadline, a page hand-rolls its markup "just this once" and the exception becomes the template for the next three pages. Catch it: the grep gate (G-FE-033) runs on every page, not just new components.
- **Props as a junk drawer.** A component accumulates boolean props (`isAlt`, `noIcon`, `wide2`) until no story shows the real combinations. Catch it: count props at review; a component whose variants cannot be enumerated becomes two components.
- **States designed, never rendered.** The state matrix exists on paper but the loading and error stories were never built, so the states debut in production. Catch it: coverage is checked against stories, not documents (G-FE-032).

## Examples

- [Example 1 — Interchangeable feature cards become weighted, specific cards](examples/example-1.md) — corrects FE-069.
- [Example 2 — A mixed icon drawer becomes one icon set](examples/example-2.md) — corrects FE-064.
- [Example 3 — A button with two states becomes a full state matrix](examples/example-3.md) — corrects FE-062.

## Recall anchors

- One story per variant and state, or it wasn't reviewed.
- Behavior is built once, inside the component.
- One icon set, one stroke weight; emoji are not icons.
- Test with the longest real content, not the placeholder.
- Pages assemble from the library — they never imitate it.

## Checklist

- [ ] Every variant and state has a Storybook story (G-FE-031).
- [ ] State matrix complete, with written reasons for non-applicable states (G-FE-032).
- [ ] Longest real content renders without overflow or clipping (FE-066).
- [ ] All icons come from the single set at one stroke weight (FE-064).
- [ ] No emoji serve as structural icons anywhere (FE-065).
- [ ] No raw component-duplicating markup in page code (G-FE-033).
- [ ] Every badge names an action the user can take (FE-068).
- [ ] Button variants express hierarchy; destructive is never primary (FE-067).

<!-- END EMBEDDED: Skill: component-library -->


---

<!-- BEGIN EMBEDDED: Skill: ui-states — source: skills/frontend/ui-states/SKILL.md -->

# ui-states

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Nielsen Norman Group, Designing Empty States in Complex Applications — https://www.nngroup.com/articles/empty-state-interface-design/ ; W3C WCAG technique C39, Using the CSS reduce-motion query — https://www.w3.org/WAI/WCAG22/Techniques/css/C39.html
- **Depends on:** component-library, data-fetching
- **Feeds into:** forms, client-routing, frontend-core

## When to use / Do NOT use

- **Use when:** building or reviewing any view that depends on data or an action's outcome — lists, dashboards, search results, submissions — and specifying its loading, empty, error, partial, and success behavior.
- **Do NOT use when:** the state belongs to a single component's visual variants (hover, focus, disabled styling) — that is component-library. Do not invent states for purely static content; a page with no data dependency has no loading state to design.

## Rules

1. **FE-161 — The state matrix comes first.** Before a data-dependent view is built, its states are specified in a matrix: loading, empty (first use / no results / cleared), error, partial, and success. A view built without the matrix is incomplete (DET-VIS-032).
2. **FE-162 — No silently blank containers.** Every view renders a designed state for every condition it can be in; an empty region where content failed or has not arrived is a defect (DET-VIS-032).
3. **FE-163 — Errors speak plainly.** Error copy names what happened and the next step, in the user's language. Raw error codes, stack text, and "No data" as the sole copy of any state are forbidden.
4. **FE-164 — Actions end visibly.** Every mutating action ends in a visible success confirmation or an error state with a retry path. Silent completion — the user guessing whether it worked — is a defect.
5. **FE-165 — Hover never gates.** Hover may enhance, but every hover reveal or action has a tap/click and a keyboard-focus equivalent (DET-VIS-042).
6. **FE-166 — Skeletons match the final layout.** Loading skeletons reproduce the shape of the content they precede, so the loading-to-loaded transition does not reflow the page (CLS budget, frontend-core).
7. **FE-167 — Empty states explain and offer.** An empty state says what belongs here and offers the next action; first-use, no-results, and cleared/filtered empties are different states with different copy and actions.
8. **FE-168 — Spinners are for short, bounded waits.** A bare spinner is used only where the wait is brief and the result's shape is unknown; content loads use skeletons (FE-166).
9. **FE-169 — Indicators report reality.** Progress bars, sync badges, and "saved" indicators reflect the actual operation state; a timer-driven or assumed success indicator is a fake state (DET-FAKE-022).
10. **FE-170 — State changes survive reduced motion.** Under `prefers-reduced-motion`, state changes remain fully legible without movement — no information is carried by animation alone (WCPM rule CR-09, cited per docs/WCPM_MAPPING.md §2.2).
11. **FE-171 — Inherited state law.** The WCPM §8 component-and-state rules and the BEH parameter family apply as cited in docs/WCPM_MAPPING.md §2.2 and §2.4, and state work is designed to pass the G-EXP gate family.

## BAN list

- **BAN-FE-081 — Blank container state.** Banned: a view that renders an empty region when data is empty, loading, or failed. Defeats: DET-VIS-032. Bad: a new account's dashboard is a white page with a sidebar because the list is empty. Instead: the designed empty state for that condition (FE-167). Severity: BLOCK.
- **BAN-FE-082 — Hover-only reveal.** Banned: content or actions reachable only by hovering. Defeats: DET-VIS-042. Bad: a card's Edit and Delete buttons appear only on mouse hover, unreachable on touch and by keyboard. Instead: always-visible actions, or a tap/focus-triggered menu (FE-165). Severity: BLOCK.
- **BAN-FE-083 — Raw error text to users.** Banned: showing error codes, exception text, or stack fragments in the UI. Defeats: DET-VIS-032. Bad: the page prints "Error 500: NullReference at OrdersController.cs:118". Instead: plain-language copy naming the problem and the retry step (FE-163), with the technical detail logged, not displayed. Severity: BLOCK.
- **BAN-FE-084 — Fake progress or sync state.** Banned: progress or "synced/saved" indicators driven by timers or optimism rather than the operation's real state. Defeats: DET-FAKE-022. Bad: an upload bar animates to 100% in two seconds while the request is still running, then shows "Saved". Instead: bind the indicator to the request lifecycle, including its failure state (FE-169). Severity: BLOCK.
- **BAN-FE-085 — One generic spinner for every wait.** Banned: a centered spinner as the loading state for every view regardless of duration or layout. Defeats: DET-VIS-032. Bad: a full dashboard, a table, and a settings form all load behind the identical spinner for several seconds. Instead: layout-matched skeletons for content loads (FE-166); spinners only for short bounded waits (FE-168). Severity: WARN.

## Gates

- **G-FE-081 — Four-state screenshot pass.** Verifies: FE-161, FE-162, FE-163. Check: manual — for each main view, capture four states: throttled network (loading), empty account (empty), blocked API request (error), completed action (success). Pass: all four states are designed and legible in every view. Fail: block shipment. Recorded in: progress.md.
- **G-FE-082 — Mocked-state render tests.** Verifies: FE-162, FE-167. Check: automated — Playwright tests mock empty and error API responses for the main views and assert the corresponding state components render with their next-action controls. Pass: all mocked states render as designed. Fail: block shipment. Recorded in: progress.md.
- **G-FE-083 — Hover-parity check.** Verifies: FE-165. Check: manual — walk every hover reveal in the interface using only touch tap and keyboard focus; confirm each has a working equivalent. Pass: zero hover-only paths. Fail: block shipment. Recorded in: progress.md.
- **G-FE-084 — Indicator honesty test.** Verifies: FE-169. Check: automated — a test kills the network mid-operation (upload, save, sync) and asserts the indicator shows the failure state, never success. Pass: the indicator tracks the real outcome. Fail: block shipment. Recorded in: progress.md.

## Intelligence — decisions & gates

> **Judgment layer.** These decisions apply the judgment layer above this skill — `skills/frontend/design-intelligence/SKILL.md` and the theme library (`skills/frontend/theme-library/`). Settle the theme's art direction there first, then decide here inside it; where a decision below and a rule above disagree, the rule above wins.

### Decision rules — designing states

| Decision | Read the situation | Decide |
|---|---|---|
| Loading treatment | The wait's shape and length | Known layout and a wait beyond ~300ms: skeleton (FE-166). Unknown shape or a short bounded wait: spinner (FE-168). Cached or instant: no indicator at all. |
| Empty-state investment | Whose moment it is | First-use empties are onboarding surfaces — invest in explanation and a first action. No-results empties are recovery surfaces — help the user change the query. Cleared empties are confirmations — keep them light (FE-167). |
| Error placement | How the user recovers | Field errors sit at the field; a failed view region is replaced by its error state with retry; a global outage takes the page. Toasts carry only non-critical notices, never the sole record of a failure. |
| Optimism | Whether failure is rare and the action reversible | Optimistic UI only where undo exists and failure is unlikely. Payments, permissions, and destructive actions show real pending, then real confirmation (FE-169). |
| Partial data | How critical each region is | Render what arrived; give the missing region its own visible gap state. Never hold the whole view hostage to its slowest widget. |
| Success visibility | The action's weight | Irreversible or destructive: an explicit confirmation state. Trivial and reversible: a lightweight inline confirmation is enough (FE-164). |
| Retry design | The failure's cause | Transient (network, timeout): automatic retry with backoff plus a manual retry. User-caused (validation): fix in place — a retry button for a form error is a dead end. |

### Self-check gate

- **G-FE-085 — Pre-ship intelligence self-check (states).** Verifies: FE-161, FE-162, FE-164, FE-166, FE-167, FE-169 as judgment, not just compliance. Check: manual — the builder scores each item pass/fail on the shipped views: (1) ★ a state matrix exists for every data-dependent view, and every cell of it has a designed render; (2) ★ kill the network mid-action: the interface lands on an error state with a retry path — never a spinner that outlives the test; (3) first-use, no-results, and cleared empties each carry their own copy and next action; (4) every mutation ends in a visible confirmation or an error — none end in silence; (5) skeletons match the layout that replaces them, with no visible reflow on load; (6) every hover reveal has a working touch and keyboard equivalent. Pass: both ★ items pass and at least 5 of 6 overall. Fail: fix, or log a written exception, before shipping. Recorded in: progress.md.

### Anti-pattern table — symptom → cause → fix

| Symptom | Cause | Fix |
|---|---|---|
| Missing empty state — a new user's dashboard is a blank page with a sidebar | The state matrix was skipped; only the success path was designed | Specify the matrix before building (FE-161); design each empty kind with copy and a next action (FE-167). |
| Missing error state — a failed fetch leaves a spinner turning forever | No timeout and no error branch were wired to the request | Every request gets an error state that names the problem and offers the next step (FE-162, FE-163). |
| Loading dead-end — the skeleton renders, the content never swaps in, and nothing ever fails visibly | The loading indicator is decorative, not bound to the request lifecycle | Bind indicators to real operation state, including failure (FE-169); test by killing the network (G-FE-084). |
| Toast-only failure — the error vanishes in four seconds and cannot be acted on | Errors were treated as notifications instead of states | Keep the failure as a persistent state with retry in place; a toast may supplement it, never replace it. |
| One empty for all empties — "No results found" greets a first-time user who has no data yet | First-use, no-results, and cleared conditions were conflated into one component | Treat them as three states with different copy and different actions (FE-167). |
| The skeleton lies — content arrives in a different shape and the page jumps | A generic skeleton was reused across unlike views | Mirror each view's real layout in its skeleton (FE-166). |
| Silent success — the save completes, nothing confirms, the user saves again and duplicates work | The mutation has no designed end state | Every action ends visibly: confirmation or error with retry (FE-164). |
| Fake "Saved" — the badge claims success while the request is still running, or has failed | The indicator is driven by a timer or by optimism | Drive it from the request outcome only, and assert its failure state under test (FE-169, G-FE-084). |

## Anti-patterns

- **Toast-only errors.** Failures appear as a toast that vanishes in four seconds, leaving no state and no retry. Catch it: if dismissing the toast erases the only record of the error, the state was never designed.
- **Empty state as dead end.** "Nothing here yet" with no explanation and no action. Catch it: an empty state with zero controls is a dead end, whatever its illustration.
- **Loading forever.** A spinner with no timeout and no error path, so a hung request hangs the interface. Catch it: block the API in testing — if the spinner outlives the test, there is no error state.
- **Success by silence.** The action completes and nothing changes on screen. Catch it: perform each mutation and watch for a confirmation; if you have to check another page to know, it failed FE-164.

## Examples

- [Example 1 — Blank list replaced by a designed empty state](examples/example-1.md) — corrects FE-167.
- [Example 2 — Raw error replaced by plain language with retry](examples/example-2.md) — corrects FE-163.
- [Example 3 — Hover-only card actions made reachable](examples/example-3.md) — corrects FE-165.

## Recall anchors

- Every view, every condition, a designed state.
- Errors name the problem and the next step.
- Hover enhances; it never gates.
- Indicators report reality or they are removed.
- Actions end visibly — never in silence.

## Checklist

- [ ] A state matrix exists for every data-dependent view (FE-161).
- [ ] Four-state screenshot pass is complete for all main views (G-FE-081).
- [ ] Mocked empty and error states render as designed (G-FE-082).
- [ ] No hover-only content or actions remain (G-FE-083).
- [ ] Progress and sync indicators track real outcomes under failure (G-FE-084).
- [ ] Empty states explain what belongs and offer the next action (FE-167).
- [ ] No raw error text reaches the UI (BAN-FE-083).

<!-- END EMBEDDED: Skill: ui-states -->


---

<!-- BEGIN EMBEDDED: Skill: webgl-3d — source: skills/frontend/webgl-3d/SKILL.md -->

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

<!-- END EMBEDDED: Skill: webgl-3d -->


---

<!-- BEGIN EMBEDDED: Skill: theme-library — source: skills/frontend/theme-library/SKILL.md -->

# theme-library

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-23
- **Sources:** this folder — `INDEX.md` (the library index and canonical-source rule), the four range indexes (`themes-001-025.md`, `themes-026-050.md`, `themes-051-075.md`, `themes-076-100.md`), the 100 canonical specs in `expanded/theme-NNN.md`, and `EXPANSION-STANDARD.md` (the depth standard every expanded spec was written and verified against)
- **Depends on:** design-intelligence (theme choice is a decision-record act), design-system, motion, scroll-experiences
- **Feeds into:** frontend-core, layout-responsive, component-library, typography, webgl-3d

## When to use / Do NOT use

- **Use when:** a build has a chosen theme (or a theme family from design-intelligence §1.2) and the builder needs the theme's full specification — its world and one law, palette anchors and derived tokens, type pairing, layout system, full motion system, signature animated elements with build specs, page application map, worked examples, anti-slop failures, quality gate, component inventory, copywriting voice, scroll choreography map, performance budget, and build order. This skill is the library itself: it supplies the worlds; design-intelligence decides which world and how far to bend it.
- **Do NOT use when:** no theme has been chosen yet and the open question is *which* theme or *how much* motion (design-intelligence decides; this skill is then read for the chosen theme's spec), the question is a token value (design-tokens), a single animation's technique (motion), or scroll mechanics in the abstract (scroll-experiences). Never build a themed page from memory, from a summary, or from the range indexes — they contain no specifications.

## Rules

1. **FE-341 — Build from the canonical expanded spec.** The canonical full specification for theme *N* is `expanded/theme-NNN.md` (zero-padded). Before designing anything, read the chosen theme's expanded file end to end. The four range files are indexes only — they list themes and point here; a build that follows an index entry, a summary, or the builder's memory of a theme is not a themed build (gate G-FE-171).
2. **FE-342 — The theme is chosen, not browsed into existence.** A theme enters a build only through a design-intelligence decision record (theme, layout family, dial, postures, one rejected alternative). If the record names a family, pick the specific theme by its material metaphor: the theme's world must be one the brand's own content can live in without explanation.
3. **FE-343 — The theme's one law governs.** Every expanded spec declares one law (§1 of the spec) and one declared record (§6.17 or its equivalent) from which every figure on the page derives. Honour both: no number, total, name, or date appears on the page unless it traces to the record, and totals must re-add exactly wherever they are printed (gate G-FE-172).
4. **FE-344 — Signature elements are built as specified, merged into content.** Each spec's §6 elements carry full build specs (structure, millisecond choreography, state matrix, breakpoints, edge cases, accessibility, tokens). Build them to spec, at the sizes and grid homes the spec assigns: an element must carry the content it accompanies — if removing it loses only decoration, it was pasted on (BAN-FE-172) — and it must never cover that content at any scroll position.
5. **FE-345 — The cursor is the system cursor.** No theme in this library uses a custom cursor. Hover and focus delight lives on the elements themselves, feather-light and transform-only; a cursor effect that can impede pointer movement is a defect, not a signature (BAN-FE-173).
6. **FE-346 — Content is readable with no JavaScript.** The page ships complete in the DOM: every heading, figure, table, and form is present and legible before any script runs. Animation is an enhancement layered over a finished page, never the mechanism that delivers content (gate G-FE-173).
7. **FE-347 — Every reveal has a watchdog fallback.** Any state a script arms (hidden, dimmed, unlit, unexposed) carries the spec's named watchdog: a timeout that forces the final, visible state if the animation path fails, stalls, or is interrupted. A reveal that can leave content invisible is a build failure (BAN-FE-174).
8. **FE-348 — The reduced-motion variant ships in the same pass.** Each spec defines per-element reduced-motion variants and a complete static state of the page. Build them with the page, not after it: under `prefers-reduced-motion`, the page is the same page — full content, final states, no loops (BAN-FE-175).
9. **FE-349 — One shared rAF loop, lerped progress.** All scroll-driven and ambient motion in a theme runs on a single requestAnimationFrame loop reading one smoothed (lerped) scroll progress, animating transform and opacity only. Raw scroll values are never applied per event, and no element runs a private loop against the page's rhythm.
10. **FE-350 — Nothing enters from outside the theme's world.** Every element, figure, and effect on the page comes from the theme's own spec and the brand's real content. Generic effect-library material — particle rain, blobs, waves, stock counters — is filler wherever it appears, however polished (the anti-filler law, EXPANSION-STANDARD.md).
11. **FE-351 — The spec's performance budget is a ceiling, not a target.** Build inside the page performance budget in the spec (§14): total weight, per-frame cost, particle/element caps, and its cut order when something must go. When budget and spectacle conflict, the budget wins and the dial drops (design-intelligence §3.2).
12. **FE-352 — Apply the theme whole, bend it by the rules.** Palette roles, type pairing, and element vocabulary are taken from the spec intact. Adapting a theme to another product type bends dial, layout family, and pacing only (design-intelligence §6) — never a reskin that keeps a different theme's skeleton under this theme's colours.

## BAN list

- **BAN-FE-171 — Building from the index, a summary, or memory.** Banned: producing a "themed" page from a range-index entry, a catalogue card, or what the builder remembers of the theme, without reading `expanded/theme-NNN.md`. Defeats: DET-VIS-006. Bad: a "Sonar Room" page built from its one-line catalogue description ships a generic dark dashboard with a sweep graphic — the formula hero wearing the theme's name. Instead: read the canonical spec end to end first (FE-341); the decision record cites the expanded file. Severity: BLOCK.
- **BAN-FE-172 — Pasted-on spectacle.** Banned: animated elements imported from a generic effects library or invented ad hoc, instead of the theme's own §6 signature elements built to spec. Defeats: DET-VIS-028. Bad: floating blobs and a particle starfield behind a ledger theme's pricing table, because "the page felt empty". Instead: build the spec's elements from the content's own material, sized into the grid — or leave the space quiet (FE-344, FE-350). Severity: BLOCK.
- **BAN-FE-173 — The heavy custom cursor.** Banned: any custom cursor — trailing, magnetic, morphing, or lagged — in a themed build. Defeats: DET-VIS-042. Bad: a glowing jar follows the pointer at 200 ms lag through a census page; visitors overshoot every link. Instead: the normal system cursor, with feather-light hover responses on the elements themselves (FE-345). Severity: BLOCK.
- **BAN-FE-174 — The stranding reveal.** Banned: shipping any reveal, exposure, or aggregation whose failure path can leave content invisible, dimmed, or unformed. Defeats: DET-VIS-032. Bad: headings sit at opacity 0 after a fast scroll because their trigger never fired and no watchdog exists; the page reads as broken, not premium. Instead: JS-gated pre-states only, each with the spec's named watchdog forcing the final state (FE-347). Severity: BLOCK.
- **BAN-FE-175 — Reduced motion as an afterthought.** Banned: shipping a themed page whose reduced-motion or no-JS state is missing, partial, or content-poor, with a promise to add it later. Defeats: DET-VIS-041. Bad: with reduced motion on, the hero's counted figure never forms and its section is an empty dark panel. Instead: build the spec's per-element reduced-motion variants and the complete static page in the same pass (FE-348). Severity: BLOCK.

## Gates

- **G-FE-171 — Canonical-source check.** Verifies: FE-341, FE-342. Check: manual — the decision record names the theme and cites its `expanded/theme-NNN.md`; spot-check the build's palette anchors, type pairing, and three signature elements against that file. Pass: every spot-check matches the spec. Fail: the build restarts from the spec. Recorded in: progress.md.
- **G-FE-172 — Record reconciliation.** Verifies: FE-343. Check: manual — pick the spec's declared record and re-derive every total printed on the page (hero figure, tables, footer); each must match the record or a function printed in the spec. Pass: all figures trace and re-add exactly. Fail: block the milestone; the untraced figure is removed or corrected at the record. Recorded in: progress.md.
- **G-FE-173 — Never-invisible drill.** Verifies: FE-346, FE-347, FE-348. Check: manual + browser — load the page with JavaScript disabled, then with reduced-motion emulated, then scroll at maximum speed with scripts on. Pass: in all three passes the full content is present and readable, and every armed state resolves to its final state. Fail: block shipment. Recorded in: progress.md.
- **G-FE-174 — Budget and loop audit.** Verifies: FE-349, FE-351. Check: manual + device — profile the page on a mid-range phone: one rAF loop drives scroll-linked motion, transform/opacity only, totals inside the spec's §14 budget. Pass: budget holds with the cut order untriggered or applied as specified. Fail: apply the spec's cut order; never cut content or the reduced-motion variant. Recorded in: progress.md.

## Anti-patterns

- **Theme tourism.** Skimming five specs and mixing their elements into one page. Catch it: G-FE-171 — one theme per site world; borrowed elements fail FE-350 on sight.
- **Spec drift.** The build starts from the spec, then improvises durations, palettes, and element behaviour "to taste" until it matches nothing. Catch it: spot-checks at G-FE-171 compare the build to the file, not to the builder's intent.
- **Index as spec.** Treating a range file's one-line entry as enough to build from because the expanded file is long. Catch it: the indexes state their own rule — they contain no specifications (BAN-FE-171).
- **Demo as ceiling.** Copying a theme's living demo page instead of building from its spec for the actual content. Catch it: the demo proves the level; the spec, applied to the real content, is the deliverable (FE-344).

## Examples

The files in `examples/` show this skill being applied — choosing from the index, building from the canonical spec, and rescuing a build that skipped it.

- `examples/example-1.md` — Theme #71 The Bioluminescent Census: a generic dark dashboard replaced by the census built from `expanded/theme-071.md`, every glow traced to the sheet's record.
- `examples/example-2.md` — Finding and opening a theme: index card and memory on one side; the canonical expanded spec and a decision record on the other.
- `examples/example-3.md` — A stranding reveal in a themed build, fixed with the spec's watchdog pattern and the reduced-motion variant it already defined.

## Recall anchors

- The canonical spec is `expanded/theme-NNN.md`; the range files are indexes, not specs.
- Every figure traces to the theme's one declared record — or it is cut.
- The cursor is the system cursor; delight lives on the elements.
- JS off and reduced motion are the same page: complete, readable, final states.
- One theme, one law, one shared loop — nothing enters from outside the theme's world.

## Checklist

- [ ] Theme chosen through a design-intelligence decision record; rejected alternative recorded (FE-342).
- [ ] The theme's `expanded/theme-NNN.md` read end to end before designing (FE-341).
- [ ] Palette anchors, type pairing, and element vocabulary taken from the spec intact (FE-352).
- [ ] Every §6 signature element built to spec and merged into the content it accompanies (FE-344).
- [ ] Every printed figure traces to the theme's declared record; totals re-add (G-FE-172).
- [ ] System cursor only; hover/focus delight is feather-light and on-element (FE-345).
- [ ] Page complete and readable with JavaScript disabled (FE-346).
- [ ] Every armed state carries its named watchdog fallback (FE-347).
- [ ] Reduced-motion variant built in the same pass; static page is complete (FE-348).
- [ ] One shared rAF loop, lerped progress, transform/opacity only (FE-349).
- [ ] Page inside the spec's §14 performance budget; cut order followed if triggered (FE-351, G-FE-174).

<!-- END EMBEDDED: Skill: theme-library -->


---

<!-- BEGIN EMBEDDED: Theme library: INDEX — source: skills/frontend/theme-library/INDEX.md -->

# OmniForge Theme Library — Index

The library holds **100 themes**, each specified exactly once, in full, in [`expanded/`](expanded/).

## Canonical source rule

- The canonical full specification for theme *N* is **`expanded/theme-NNN.md`** (zero-padded: theme 7 → `expanded/theme-007.md`). Build from that file.
- The four range files are **indexes only** — they list their themes and point to the canonical expanded files. They contain no specifications.
  - [themes-001-025.md](themes-001-025.md) — Themes 1–25
  - [themes-026-050.md](themes-026-050.md) — Themes 26–50
  - [themes-051-075.md](themes-051-075.md) — Themes 51–75
  - [themes-076-100.md](themes-076-100.md) — Themes 76–100
- [EXPANSION-STANDARD.md](EXPANSION-STANDARD.md) is the depth standard every expanded spec was written and verified against (per-element build specs, choreography timelines, state matrices, breakpoint behaviour, edge cases, accessibility, tokens, worked examples, scroll choreography map, performance budget, build order).

## History

Each theme began as a short entry (~950–1,400 words) inside the range files. Once a theme's 50x expansion in `expanded/` was verified, its short entry was removed, per the standing rule that the final library holds only the deep versions.

<!-- END EMBEDDED: Theme library: INDEX -->


---

<!-- BEGIN EMBEDDED: Theme library: themes 001-025 — source: skills/frontend/theme-library/themes-001-025.md -->

# OmniForge Theme Library — Themes 001–025 (Editorial & Print Reinvention)

> **Index only — the full specifications live in `expanded/`.** Each theme below has a complete, verified 50x expansion (full build spec per element: choreography timelines, state matrices, breakpoint behaviour, edge cases, accessibility, tokens) at `expanded/theme-NNN.md`. That expanded file is the canonical source for the theme — build from it, not from any older summary. The original short entries that used to live in this file were removed once every expansion was verified, so the library holds only the deep versions.

**Global rules for every theme in this library**

- Every theme's motion system uses the full vocabulary — scroll-triggered and scroll-scrubbed animation, pinned sections, staggered and masked reveals, kinetic typography, counters, SVG line-draw, parallax, hover/magnetic/tilt micro-interactions, skeleton loading, page transitions, and a reduced-motion variant — always translated into the theme's own material language, never copy-pasted between themes.
- Signature animated elements are part of the page's content and reading flow — they carry data, mark progress, or perform the theme's central act — never decoration pasted on top.
- Normal system cursor only, everywhere. No custom cursors, no cursor-follow effects.
- All content is complete and readable in the DOM without JavaScript. Every reveal carries a timed fallback (timeout or observer safety) so content can never be left invisible.
- `prefers-reduced-motion` always gets the theme's own fully lit, static, complete variant.
- Performance: one shared `requestAnimationFrame` loop per page, transform/opacity-only animation, capped particle counts.

---

| # | Theme | Canonical full spec |
|---|-------|---------------------|
| 1 | The Midnight Press Run | [expanded/theme-001.md](expanded/theme-001.md) |
| 2 | Marginalia | [expanded/theme-002.md](expanded/theme-002.md) |
| 3 | Redacted Archive | [expanded/theme-003.md](expanded/theme-003.md) |
| 4 | Letterpress Atelier | [expanded/theme-004.md](expanded/theme-004.md) |
| 5 | The Colophon | [expanded/theme-005.md](expanded/theme-005.md) |
| 6 | Palimpsest | [expanded/theme-006.md](expanded/theme-006.md) |
| 7 | The Proofreader's Desk | [expanded/theme-007.md](expanded/theme-007.md) |
| 8 | The Index Card Library | [expanded/theme-008.md](expanded/theme-008.md) |
| 9 | The Sunday Supplement | [expanded/theme-009.md](expanded/theme-009.md) |
| 10 | Risograph Confessional | [expanded/theme-010.md](expanded/theme-010.md) |
| 11 | The Telegraph Wire | [expanded/theme-011.md](expanded/theme-011.md) |
| 12 | Microfilm Reader | [expanded/theme-012.md](expanded/theme-012.md) |
| 13 | The Shipping Forecast | [expanded/theme-013.md](expanded/theme-013.md) |
| 14 | Broadside & Ballad | [expanded/theme-014.md](expanded/theme-014.md) |
| 15 | The Corrections Column | [expanded/theme-015.md](expanded/theme-015.md) |
| 16 | Vellum & Wax | [expanded/theme-016.md](expanded/theme-016.md) |
| 17 | The Classifieds | [expanded/theme-017.md](expanded/theme-017.md) |
| 18 | Manicule & Catchword | [expanded/theme-018.md](expanded/theme-018.md) |
| 19 | The Linotype Line | [expanded/theme-019.md](expanded/theme-019.md) |
| 20 | Halftone Confessions | [expanded/theme-020.md](expanded/theme-020.md) |
| 21 | The Almanack | [expanded/theme-021.md](expanded/theme-021.md) |
| 22 | Dust Jacket | [expanded/theme-022.md](expanded/theme-022.md) |
| 23 | The Printer's Devil | [expanded/theme-023.md](expanded/theme-023.md) |
| 24 | Tabloid Confessional | [expanded/theme-024.md](expanded/theme-024.md) |
| 25 | The Obituaries Page | [expanded/theme-025.md](expanded/theme-025.md) |

<!-- END EMBEDDED: Theme library: themes 001-025 -->


---

<!-- BEGIN EMBEDDED: Theme library: themes 026-050 — source: skills/frontend/theme-library/themes-026-050.md -->

# OmniForge Theme Library — Themes 026–050

> **Index only — the full specifications live in `expanded/`.** Each theme below has a complete, verified 50x expansion (full build spec per element: choreography timelines, state matrices, breakpoint behaviour, edge cases, accessibility, tokens) at `expanded/theme-NNN.md`. That expanded file is the canonical source for the theme — build from it, not from any older summary. The original short entries that used to live in this file were removed once every expansion was verified, so the library holds only the deep versions.

**Global rules for every theme in this library**

- Every theme's motion system uses the full vocabulary — scroll-triggered and scroll-scrubbed animation, pinned sections, staggered and masked reveals, kinetic typography, counters, SVG line-draw, parallax, hover/magnetic/tilt micro-interactions, skeleton loading, page transitions, and a reduced-motion variant — always translated into the theme's own material language, never copy-pasted between themes.
- Signature animated elements are part of the page's content and reading flow — they carry data, mark progress, or perform the theme's central act — never decoration pasted on top.
- Normal system cursor only, everywhere. No custom cursors, no cursor-follow effects.
- All content is complete and readable in the DOM without JavaScript. Every reveal carries a timed fallback (timeout or observer safety) so content can never be left invisible.
- `prefers-reduced-motion` always gets the theme's own fully lit, static, complete variant.
- Performance: one shared `requestAnimationFrame` loop per page, transform/opacity-only animation, capped particle counts.

---

| # | Theme | Canonical full spec |
|---|-------|---------------------|
| 26 | Movable Type Chaos | [expanded/theme-026.md](expanded/theme-026.md) |
| 27 | The Society Pages | [expanded/theme-027.md](expanded/theme-027.md) |
| 28 | Errata Slip | [expanded/theme-028.md](expanded/theme-028.md) |
| 29 | The Weather Map | [expanded/theme-029.md](expanded/theme-029.md) |
| 30 | First Edition | [expanded/theme-030.md](expanded/theme-030.md) |
| 31 | Basalt Cathedral | [expanded/theme-031.md](expanded/theme-031.md) |
| 32 | Tidal Ledger | [expanded/theme-032.md](expanded/theme-032.md) |
| 33 | Silk Unspooling | [expanded/theme-033.md](expanded/theme-033.md) |
| 34 | Kiln Opening | [expanded/theme-034.md](expanded/theme-034.md) |
| 35 | Dune Cartography | [expanded/theme-035.md](expanded/theme-035.md) |
| 36 | Monsoon Arrival | [expanded/theme-036.md](expanded/theme-036.md) |
| 37 | Glacier Confession | [expanded/theme-037.md](expanded/theme-037.md) |
| 38 | Paper Mulberry | [expanded/theme-038.md](expanded/theme-038.md) |
| 39 | Verdigris | [expanded/theme-039.md](expanded/theme-039.md) |
| 40 | Loam & Strata | [expanded/theme-040.md](expanded/theme-040.md) |
| 41 | Kintsugi | [expanded/theme-041.md](expanded/theme-041.md) |
| 42 | Salt Mirror | [expanded/theme-042.md](expanded/theme-042.md) |
| 43 | Forest Floor, Magnified | [expanded/theme-043.md](expanded/theme-043.md) |
| 44 | Hammam | [expanded/theme-044.md](expanded/theme-044.md) |
| 45 | Indigo Vat | [expanded/theme-045.md](expanded/theme-045.md) |
| 46 | Amber Hour | [expanded/theme-046.md](expanded/theme-046.md) |
| 47 | Fjord Stillness | [expanded/theme-047.md](expanded/theme-047.md) |
| 48 | Sun-Fired Clay | [expanded/theme-048.md](expanded/theme-048.md) |
| 49 | Pearl Diver's Breath | [expanded/theme-049.md](expanded/theme-049.md) |
| 50 | Charcoal & Ink | [expanded/theme-050.md](expanded/theme-050.md) |

<!-- END EMBEDDED: Theme library: themes 026-050 -->


---

<!-- BEGIN EMBEDDED: Theme library: themes 051-075 — source: skills/frontend/theme-library/themes-051-075.md -->

# OmniForge Theme Library — Themes 51–75 (Detailed)

> **Index only — the full specifications live in `expanded/`.** Each theme below has a complete, verified 50x expansion (full build spec per element: choreography timelines, state matrices, breakpoint behaviour, edge cases, accessibility, tokens) at `expanded/theme-NNN.md`. That expanded file is the canonical source for the theme — build from it, not from any older summary. The original short entries that used to live in this file were removed once every expansion was verified, so the library holds only the deep versions.

**Global rules for every theme in this library**

- Every theme's motion system uses the full vocabulary — scroll-triggered and scroll-scrubbed animation, pinned sections, staggered and masked reveals, kinetic typography, counters, SVG line-draw, parallax, hover/magnetic/tilt micro-interactions, skeleton loading, page transitions, and a reduced-motion variant — always translated into the theme's own material language, never copy-pasted between themes.
- Signature animated elements are part of the page's content and reading flow — they carry data, mark progress, or perform the theme's central act — never decoration pasted on top.
- Normal system cursor only, everywhere. No custom cursors, no cursor-follow effects.
- All content is complete and readable in the DOM without JavaScript. Every reveal carries a timed fallback (timeout or observer safety) so content can never be left invisible.
- `prefers-reduced-motion` always gets the theme's own fully lit, static, complete variant.
- Performance: one shared `requestAnimationFrame` loop per page, transform/opacity-only animation, capped particle counts.

---

| # | Theme | Canonical full spec |
|---|-------|---------------------|
| 51 | Quarry Cut | [expanded/theme-051.md](expanded/theme-051.md) |
| 52 | Fog Harvest | [expanded/theme-052.md](expanded/theme-052.md) |
| 53 | Moon Garden | [expanded/theme-053.md](expanded/theme-053.md) |
| 54 | Beeswax & Comb | [expanded/theme-054.md](expanded/theme-054.md) |
| 55 | River Stone | [expanded/theme-055.md](expanded/theme-055.md) |
| 56 | Frost Fern | [expanded/theme-056.md](expanded/theme-056.md) |
| 57 | Ochre & Pigment | [expanded/theme-057.md](expanded/theme-057.md) |
| 58 | Storm Glass | [expanded/theme-058.md](expanded/theme-058.md) |
| 59 | Linen Field | [expanded/theme-059.md](expanded/theme-059.md) |
| 60 | Meteorite Iron | [expanded/theme-060.md](expanded/theme-060.md) |
| 61 | The Flight Director's Ledger | [expanded/theme-061.md](expanded/theme-061.md) |
| 62 | Celestial Navigation Atelier | [expanded/theme-062.md](expanded/theme-062.md) |
| 63 | Sonar Room | [expanded/theme-063.md](expanded/theme-063.md) |
| 64 | The Cyanotype Vault | [expanded/theme-064.md](expanded/theme-064.md) |
| 65 | Waveform Observatory | [expanded/theme-065.md](expanded/theme-065.md) |
| 66 | The Data Cartographer's Atlas | [expanded/theme-066.md](expanded/theme-066.md) |
| 67 | Calibre & Escapement | [expanded/theme-067.md](expanded/theme-067.md) |
| 68 | Cryo Lab Monograph | [expanded/theme-068.md](expanded/theme-068.md) |
| 69 | The 1962 Space Clipper Brochure | [expanded/theme-069.md](expanded/theme-069.md) |
| 70 | Telemetry Tape | [expanded/theme-070.md](expanded/theme-070.md) |
| 71 | The Bioluminescent Census | [expanded/theme-071.md](expanded/theme-071.md) |
| 72 | Solar Weather Almanac | [expanded/theme-072.md](expanded/theme-072.md) |
| 73 | The Instrument Maker's Bench | [expanded/theme-073.md](expanded/theme-073.md) |
| 74 | Lagrange Post | [expanded/theme-074.md](expanded/theme-074.md) |
| 75 | Seismograph Diary | [expanded/theme-075.md](expanded/theme-075.md) |

<!-- END EMBEDDED: Theme library: themes 051-075 -->


---

<!-- BEGIN EMBEDDED: Theme library: themes 076-100 — source: skills/frontend/theme-library/themes-076-100.md -->

# OmniForge Theme Library — Themes 076–100

> **Index only — the full specifications live in `expanded/`.** Each theme below has a complete, verified 50x expansion (full build spec per element: choreography timelines, state matrices, breakpoint behaviour, edge cases, accessibility, tokens) at `expanded/theme-NNN.md`. That expanded file is the canonical source for the theme — build from it, not from any older summary. The original short entries that used to live in this file were removed once every expansion was verified, so the library holds only the deep versions.

**Global rules for every theme in this library**

- Every theme's motion system uses the full vocabulary — scroll-triggered and scroll-scrubbed animation, pinned sections, staggered and masked reveals, kinetic typography, counters, SVG line-draw, parallax, hover/magnetic/tilt micro-interactions, skeleton loading, page transitions, and a reduced-motion variant — always translated into the theme's own material language, never copy-pasted between themes.
- Signature animated elements are part of the page's content and reading flow — they carry data, mark progress, or perform the theme's central act — never decoration pasted on top.
- Normal system cursor only, everywhere. No custom cursors, no cursor-follow effects.
- All content is complete and readable in the DOM without JavaScript. Every reveal carries a timed fallback (timeout or observer safety) so content can never be left invisible.
- `prefers-reduced-motion` always gets the theme's own fully lit, static, complete variant.
- Performance: one shared `requestAnimationFrame` loop per page, transform/opacity-only animation, capped particle counts.

---

| # | Theme | Canonical full spec |
|---|-------|---------------------|
| 76 | Ice Core Archive | [expanded/theme-076.md](expanded/theme-076.md) |
| 77 | The Listening Dish | [expanded/theme-077.md](expanded/theme-077.md) |
| 78 | Trajectory Tables | [expanded/theme-078.md](expanded/theme-078.md) |
| 79 | Vent Field Survey | [expanded/theme-079.md](expanded/theme-079.md) |
| 80 | The Ephemeris Press | [expanded/theme-080.md](expanded/theme-080.md) |
| 81 | Dead Reckoning | [expanded/theme-081.md](expanded/theme-081.md) |
| 82 | Containment Log: Tokamak Shift B | [expanded/theme-082.md](expanded/theme-082.md) |
| 83 | The Tide Engine | [expanded/theme-083.md](expanded/theme-083.md) |
| 84 | The Tube Weather Bureau | [expanded/theme-084.md](expanded/theme-084.md) |
| 85 | Transit Photometry | [expanded/theme-085.md](expanded/theme-085.md) |
| 86 | The Drift Buoy Network | [expanded/theme-086.md](expanded/theme-086.md) |
| 87 | Calibration Standard No. 9 | [expanded/theme-087.md](expanded/theme-087.md) |
| 88 | Subglacial Dispatch | [expanded/theme-088.md](expanded/theme-088.md) |
| 89 | Custodian of the Orbit | [expanded/theme-089.md](expanded/theme-089.md) |
| 90 | Cymatics Garden | [expanded/theme-090.md](expanded/theme-090.md) |
| 91 | The Projectionist's Booth | [expanded/theme-091.md](expanded/theme-091.md) |
| 92 | Museum After Dark | [expanded/theme-092.md](expanded/theme-092.md) |
| 93 | Marginalia | [expanded/theme-093.md](expanded/theme-093.md) |
| 94 | The Long Exposure | [expanded/theme-094.md](expanded/theme-094.md) |
| 95 | The Cartographer's Table | [expanded/theme-095.md](expanded/theme-095.md) |
| 96 | From the Wings | [expanded/theme-096.md](expanded/theme-096.md) |
| 97 | Reel to Reel | [expanded/theme-097.md](expanded/theme-097.md) |
| 98 | Tales by the Hearth | [expanded/theme-098.md](expanded/theme-098.md) |
| 99 | The Grand Tour Ledger | [expanded/theme-099.md](expanded/theme-099.md) |
| 100 | The Velvet Note | [expanded/theme-100.md](expanded/theme-100.md) |

<!-- END EMBEDDED: Theme library: themes 076-100 -->


<!-- OMNIFORGE EMBEDDED UI/UX SKILL PACK: END -->
