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
