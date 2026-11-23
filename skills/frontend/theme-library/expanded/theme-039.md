# 39. Verdigris — Expanded (v1 + v2)

> Expansion of theme #39 from `themes-026-050.md`, written directly to
> the full standard: the v1 10-part structure plus the v2 deepening
> layers (per-element choreography timelines, state matrices, breakpoint
> behaviour, edge cases, accessibility specs and token lists; per-theme
> component inventory, copywriting voice, three worked examples, scroll
> choreography map, performance budget, build-order checklist).
> Identity preserved exactly: the same concept, the same five palette
> anchors, the same two typefaces, the same nine signature elements —
> deepened, never redesigned — plus nine page-family elements.

## 1. Concept & world

Most websites are finished the moment they load. This theme is the
opposite wager: **the site is a copper object, and reading it ages
it.** The page opens bright — polished new copper, brushed grain,
light still moving on the metal — and as the visitor descends, every
metallic surface oxidises in step with the reading: copper warms to
aged bronze, bronze greens to verdigris, verdigris deepens to the
dark green-black of old roofs and harbour statues. By the footer the
visitor is standing in front of something that has weathered. The
page is about time, care, and things that improve by being exposed —
and it proves the claim by undergoing it.

The world is the metalworker's bench and the conservator's studio,
treated as a complete interface vocabulary rather than a texture. The
page has **plates** (the copper-rimmed frames that carry images and
specimens), **the margin strip** (a band of copper down the page's
edge that oxidises as the progress gauge), **the grain** (brushed
metal at the top, dissolving into mottled mineral patina at the
bottom), **stages** (the five named oxidation states — bright,
warmed, bronzed, verdigris, deep — that every metallic surface passes
through in order), **the cloth** (the visitor's polishing hand: hover
re-polishes, click leaves a thumbprint), and **the plate** in the
footer (an engraved sheet of metal that is signed with the maker's
mark and keeps the patina log). Nothing on the page is a photograph
of metal used as wallpaper; the metal is the page's furniture, and
everything that moves is either the metal ageing, the visitor caring
for it, or the record of both.

**The theme's one law: the patina never lies.** Oxidation on this
page is a declared function, printed where a visitor can audit it:
stage is computed from scroll depth and dwell by the formula in §5,
the same formula drives every surface, and no surface may be greener
than the formula says — a decorative green panel pasted at the top of
the page "for mood" is a falsified assay, and the quality gate (§10)
fails it. The corollary governs the numbers: years in service, alloy
percentages and objects restored are the publisher's real figures or
they do not appear (§6.14); the patina log (§6.9) reports only what
it measured — this visitor's dwell and depth, computed in the
browser, labelled as an estimate of one visit. A Verdigris build
that invents a founding year to look established has not bent the
theme; it has cast a fake hallmark, which in the metal trades is the
one unforgivable act. Everything else in this theme is craft. That
one is metallurgy's ethics.

**Ageing is the interaction model.** Because the page weathers as it
is read, the visitor's acts are a custodian's acts: they descend and
the metal ages (§6.2), they touch a surface and it brightens under
their hand (§6.5), they press a button and their thumbprint stays on
it for four seconds (§6.6), and at the end their visit is entered in
the object's own log (§6.9), the way a conservator logs every
handling. The site does not have users; it has keepers, and the page
keeps the marks of their keeping. That is why the theme fits things
whose value genuinely grows with time and care — and why it curdles
around anything disposable, instant or ashamed of its age.

**Best-fit sites and audiences.**

- Restoration and conservation studios: metalwork, furniture,
  instruments, buildings — anywhere before/after is the whole
  argument and the showcase (§6.4) can perform the service on the
  photograph itself.
- Makers whose objects age by design: copper and bronze foundries,
  leather-and-brass goods, raw-denim and waxed-canvas brands,
  luthiers, watchmakers — products sold on the promise that they
  will look better in ten years.
- Heritage and craft institutions: museums of making, guild and
  assay offices, historic houses, archives — content that already
  thinks in provenance, accession numbers and care records.
- Long-lived services with real tenure: family firms, cooperatives,
  mutual insurers, schools and practices whose years-in-service
  figure (§6.14) is a fact they can print and defend.
- Personal sites of craftspeople: one maker, one bench, a body of
  work that has visibly weathered — the patina log's "your visit
  aged this page" lands hardest on a single-object page.

**When NOT to use it.**

- For anything that must feel new every visit. A fintech launch, a
  flash sale, a breaking-news surface: the theme's whole grammar is
  decay and care, and a page that greys as you read it argues
  against novelty by construction.
- For content with no objects. If there is nothing that could be
  made of metal — no product, no building, no artefact, no tenure —
  the copper is a costume on a text page and the patination is a
  colour-change gimmick; choose a theme whose material is the
  content's own.
- Where the publisher will not commit real figures. Years, alloys
  and restoration counts are assay data here (§6.14); a build that
  needs invented heritage to fill the counters has already failed
  the one law.
- For high-frequency transactional flows. Checkout, dashboards and
  search results are visited at speed and revisited daily; a surface
  that re-oxidises and re-polishes under the hand becomes noise
  where the visitor wants a tool.
- For audiences on very low-power devices as the *only* experience.
  The scrubbed patination is cheap (§14), but the full theme leans
  on layered gradients and masks; the reduced build is specced
  (§14 cut order) — if even that is too much, the static mid-patina
  variant (§5) is the honest fallback, not a stripped embarrassment.

## 2. Palette

Five anchors from the original entry, held exactly. Around them a
closed list of derived tokens, each labelled, each with its measured
contrast. The governing fact of this palette: **the metal colours
are materials, not text colours.** Of the five anchors only deep
patina clears AA for body text on limestone (6.26:1); verdigris on
limestone is 2.14:1 and may never carry text on the light ground.
All reading text is `--ink-bronze` (12.46:1 on limestone) at every
oxidation stage — the words do not age; the furniture does. That
separation is what makes the theme's central promise possible: the
page can green completely without ever dropping below AA, because
the green was never load-bearing for legibility.

| Token | Hex | Role | Ratio / pairing law |
|---|---|---|---|
| `--copper` | `#B87333` | New copper: stage 0 metal, hero frames, the margin strip's bright end, polish targets | 3.17:1 on limestone — display and surfaces only, never text on light ground; `--ink-bronze` on copper is 3.93:1, large display only |
| `--bronze` | `#8C5A2B` | Aged bronze: stage 2 metal, mid-page frames and rules, the warmed state of every surface | 4.86:1 on limestone — the only mid-stage anchor allowed for large labels (≥18px) on light ground; never body text |
| `--verdigris` | `#43B3A2` | Verdigris: stage 3 metal, late-page frames, the strip's green end, bloom colour | 2.14:1 on limestone — surfaces and large display only; on the dark ground (`--night-patina`) 5.38:1, where it may carry large labels |
| `--patina-deep` | `#2F5D50` | Deep patina: stage 4 metal, footer plate ground, late section grounds | 6.26:1 against limestone both ways — the one anchor that may carry text (limestone on deep) and ground text |
| `--limestone` | `#F2EAD9` | The stone the metal sits on: page ground (upper), text on deep grounds, plate lettering ground | Against `--ink-bronze` 12.46:1; the page's constant — stone does not oxidise |
| `--ink-bronze` | `#33241A` | All reading text on light grounds, at every stage | 12.46:1 on limestone; 5.83:1 on verdigris surfaces (still AA — the emergency pairing if text must sit on a stage-3 plate) |
| `--stage-1` | `#A96A30` | Warmed copper (derived, stage 1): the first tarnish, frames in the second eighth of the page | Surfaces only; computed as the formula's first stop, never hand-placed |
| `--stage-mid` | `#5E8A6E` | The fixed mid-patina of the reduced-motion / static variant: a green between verdigris and deep | Surfaces only; the whole page sits here when motion is refused (§5) |
| `--night-patina` | `#22302B` | Dark-scheme ground: deep patina taken to near-black-green | Limestone on it 10.12:1 (`#E8DCC2` text tint), verdigris 5.38:1; see dark ruling below |
| `--copper-hi` | `#E09A52` | The polish highlight: the bright streak inside a polish pass (§6.1) and the re-polish reveal (§6.5) | Never a surface at rest; exists only inside motion, ≤1300ms at a time |
| `--thumbprint` | `#D98E46` | The bright mark a click leaves (§6.6) | Fades to the surface's current stage colour over 4000ms; never text |

**Oxidation stages (the formula's stops, §5).** Stage 0 bright
(`--copper`) → stage 1 warmed (`--stage-1`) → stage 2 bronzed
(`--bronze`) → stage 3 verdigris (`--verdigris`) → stage 4 deep
(`--patina-deep`). Every metallic surface interpolates through
exactly these five stops in this order; a surface may never skip a
stage, reverse without the visitor's hand (§6.5 is the only lawful
reversal, and it is local and temporary), or sit at a stage the
formula has not reached. The interpolation is computed in the shared
loop from one global `--age` value (0→1) so two surfaces at the same
depth can never disagree about what year it is.

**Dark-mode ruling: the foundry at night, not an inversion.**
`prefers-color-scheme: dark` does not invert the page; the day's
work is done and the bench is lit by one lamp. Grounds become
`--night-patina`; limestone text lightens to `#E8DCC2` (10.12:1);
the metal stages shift one stop brighter so the ageing arc stays
legible against the dark (stage 0 renders as `--copper` at full
saturation, stage 4 as `--verdigris` lit — 5.38:1 as a surface
accent). The formula, the order and the log are unchanged: it is the
same object, seen at night.

**Usage ratios.** Limestone and ink-bronze carry ~78% of any
viewport (ground + text). Metal at all stages together ~17% —
frames, rules, the strip, plates — and it is rationed by depth: the
top quarter of the page is mostly bright metal on stone, the bottom
quarter mostly deep grounds with limestone lettering. `--copper-hi`
and `--thumbprint` together under 1%, and only while moving.

## 3. Typography

Two families from the original entry, held exactly: **Fraunces** for
display — its soft, old-style serifs and optical sizing read as cast
and engraved letterforms — and **Archivo Narrow** for body and data,
a grotesque compressed enough to feel like stamped specification
type. No third family is admitted; the maker's mark and the log are
set in these two, because a foundry stamps its name in its own type.

| Role | Font | Size / line-height | Tracking | Rules |
|---|---|---|---|---|
| Display (hero plate title) | Fraunces 72pt optical, 560 | clamp(44px, 7.2vw, 84px) / 1.02 | −0.01em | Set as if engraved on the hero plate; the polish pass (§6.1) is its only entrance |
| Section title | Fraunces 48pt optical, 540 | clamp(30px, 4vw, 46px) / 1.08 | −0.005em | Emerges from patina to full contrast (§6.16); never more than 2 lines |
| Plate caption / standfirst | Fraunces italic 400 | 19–21px / 1.45 | 0 | The conservator's hand — used for before/after captions and the log's voice lines |
| Body | Archivo Narrow 400 | 17.5px / 1.55 | 0.002em | Measure 58–66ch; text is `--ink-bronze` at every stage (§2) |
| Specification / data | Archivo Narrow 500, tabular | 15px / 1.4 | 0.04em, uppercase for labels | Alloys, years, counts (§6.14); figures are assay data and are set like it |
| Apparatus (strip readings, log, stamps) | Archivo Narrow 600 | 12.5px / 1.35 | 0.09em uppercase | The bench's paperwork: stage names, log lines, the mark's lettering |

**Type laws.**

1. **The words do not age.** Text colour, weight and size are
   invariant across all five stages. Only metal surfaces interpolate;
   if a build tints body text toward green "for atmosphere", it has
   broken §2 and will fail contrast somewhere in the arc.
2. **Display is engraved, never outlined.** Fraunces display sits
   *in* its plate (solid fill, the plate's stage colour as ground or
   ink per §2's pairings) — no stroke text, no metallic gradient
   clipped into glyphs at rest. The one exception is inside the
   polish pass (§6.1), where the highlight travels *across* set type
   for 1300ms and leaves it solid.
3. **Figures are tabular everywhere.** Years, percentages and counts
   never jitter as they count (§6.14); Archivo Narrow's tabular
   figures are mandatory in data roles, with `font-variant-numeric:
   tabular-nums` set on the token, not per element.
4. **Uppercase is for apparatus only.** Labels, stamps and the log
   may shout in 12.5px tracked capitals; headlines and body never
   do. A page that sets its section titles in caps has mistaken the
   paperwork for the object.
5. **Italics are the conservator's voice.** Fraunces italic is
   reserved for captions, before/after notes and quoted care
   instructions — the human commentary on the object. Navigation,
   buttons and errors never use it (§12).


## 4. Layout language

The page is a bench laid out in depth: bright work at the top, aged
work at the bottom, and the visitor's descent is the timeline. The
grid is a 12-column frame at ≥1200px inside a 1240px measure, but
the theme's real layout unit is **the plate** — a metal-rimmed
rectangular field (frame 2px at the surface's current stage colour,
inner mat of limestone 18–28px) that carries one object: a
photograph, a specimen, a before/after pair, a form. Plates never
tile into a uniform grid of equals; they sit on the stone like
objects on a bench, at deliberate sizes, with the margin strip
running past all of them.

- **The margin strip.** A 14px copper band fixed to the left edge
  (≥1200px) for the page's whole length — the progress gauge (§6.3).
  Content keeps a 96px left gutter so the strip never touches a
  plate. At 768–1199px the strip thins to 8px; below 768px it moves
  to the top edge as a 4px horizontal band (§6.3's mobile ruling) —
  a phone has no margin to spare, and the gauge moves rather than
  crushing the plates.
- **Depth rhythm.** Sections are spaced on a 120px vertical rhythm
  (88px at 768–1199, 64px below 768), and each section declares the
  stage band it lives in (§5's map): the page is composed in five
  broad bands, one per stage, so the greening reads as descent, not
  as random tinting. Within a band, individual surfaces interpolate
  continuously — the bands are composition, the formula is law.
- **The working margin.** At ≥1200px a 300px right margin carries
  the conservator's apparatus: stage readings, care notes, the
  pinned showcase's captions (§6.4). Body plates occupy the 760px
  reading column. The margin is where the page keeps its paperwork;
  nothing decorative is allowed to live there.
- **Density law.** At most 3 plates per viewport at ≥1200px, 2 at
  768–1199px, 1 below 768px. Metal is heavy; a wall of plates is a
  scrapyard. Whitespace in this theme is stone — limestone ground
  left bare is the bench showing between objects, and it is a
  material, not an absence.
- **The footer is a plate, full width.** The page ends in one
  engraved sheet (§6.15): deep-patina ground, limestone lettering,
  the mark, the log. It is the only full-bleed element on the page —
  the object the whole visit has been ageing toward.

## 5. Full motion system

One physical process drives almost everything: **oxidation**, plus
its lawful opposite, **the visitor's polishing hand**. Every motion
term in the vocabulary is either translated into one of those two,
or refused with a reason. A Verdigris page that fades content in
generically has imported another theme's weather.

**The age formula (the law §1 cites).** One global value `--age`
(0→1) is computed in the shared rAF loop as
`age = clamp(0.72 × scrollDepth + 0.28 × dwellNorm, 0, 1)`, where
`scrollDepth` is document scroll progress (0 at top, 1 at footer)
and `dwellNorm` is elapsed visit time normalised over 240s, capped
at its 0.28 share. Scroll dominates because descent is the theme's
timeline; dwell contributes so that a visitor who reads one long
plate slowly still watches it age. Each surface maps `--age`
through its own depth offset (a surface's position in the page
shifts its local stage by up to ±0.06, so the footer is always the
oldest thing on screen) and interpolates the five stage stops of
§2. The formula is printed in the footer (§6.15) in apparatus type —
the audit trail the one law requires.

**Named easings (the bench's five).**

- `--ease-polish` — `cubic-bezier(0.22, 0.9, 0.28, 1)`: the cloth's
  stroke; fast contact, long bright tail. Polish passes and
  re-polish reveals.
- `--ease-age` — `cubic-bezier(0.6, 0.02, 0.9, 0.4)`: chemistry, not
  mechanics; slow to start, slower to stop. Re-formation of patina
  (§6.5), bloom creep (§6.7).
- `--ease-glide` — `cubic-bezier(0.25, 0.75, 0.2, 1)` at lerp 0.09:
  the metallic-glide scroll smoothing; heavy, unhurried, the page
  feels cast rather than printed.
- `--ease-engrave` — `cubic-bezier(0.7, 0, 0.2, 1)`: a chisel's
  bite; decisive start, no overshoot. The mark's draw (§6.8),
  stamp-like apparatus changes.
- `--ease-settle` — `cubic-bezier(0.3, 1.4, 0.4, 1)`: a plate set
  down on stone, one small overshoot. Plate entrances (§6.17),
  cards.

**Term by term.**

- *Scroll-triggered reveals* — titles emerge from patina (§6.16):
  the title's plate starts one stage greener than its band and
  resolves to full contrast as it crosses the reading line. Nothing
  fades from transparent; metal clears.
- *Scroll-driven / scrubbed animation* — the patination itself
  (§6.2) and the margin strip (§6.3): both pure functions of
  `--age`, lerped at 0.09 in the shared loop.
- *Parallax* — two strata only: brushed-grain plates drift at 0.96×
  against mottled-patina grounds at 1.0× in the upper half; below
  stage 3 parallax stops entirely — deep patina is still, the way
  old roofs are still.
- *Pinned sections* — one: the restoration showcase (§6.4), pinned
  for 160vh while its crossfade is scrubbed.
- *Staggered reveals* — plates polish in one by one (§6.17),
  120ms apart in reading order, each a small local polish pass.
- *Masked reveals* — the polish pass (§6.1) and re-polish (§6.5)
  are mask work: a radial or linear `--copper-hi` mask travelling
  over a surface. Masked *line* reveals are refused — type is
  engraved here, not unmasked.
- *Blur-to-sharp* — refused. Oxidation is a colour and texture
  process; blur reads as camera failure on a metal object. The
  before/after crossfade (§6.4) is opacity and stage, never blur.
- *Kinetic typography* — refused. Engraved letters do not move; the
  headline's letters brighten in sequence during the polish pass
  (§6.1) and that is the theme's whole concession to lively type.
- *Marquee* — refused, permanently. Nothing in a foundry streams
  sideways forever; the log (§6.9) updates by appending a line,
  not by scrolling one.
- *Counters* — assay counters (§6.14): years and percentages count
  once, on entry, in tabular figures, and only to figures the
  publisher supplied.
- *Progress indicator* — the margin strip (§6.3), made of the
  theme's own metal undergoing its own process.
- *Hover / micro-interactions* — re-polish (§6.5), thumbprint
  (§6.6), link rules drawing as if scribed (§6.10).
- *Page transitions* — the burnish (§6.18): a polish sweep crosses
  the viewport and the new page arrives one stage younger than the
  old one left — travel is a small restoration.
- *Ambient loops* — one only: the patina bloom (§6.7) in its single
  corner panel, 30s, and it stills off-screen. A page of ambient
  loops is a page that cannot sit still on the bench.
- *Reduced motion* — the page sits at fixed `--stage-mid` (§2): one
  fully legible mid-patina, no scrub, no polish passes, counters at
  final values, the showcase a static side-by-side (§6.4). The
  static variant is a designed state, not a broken animation.

## 6. Signature elements

### 6.1 Headline polish pass

- **What & why.** The page's first act of care. On load, one light
  sweep polishes across the copper headline plate — a bright mask
  travelling left to right over 1300ms, the Fraunces letters
  brightening in sequence as the cloth passes, like a restorer's
  first stroke across a nameplate. It belongs because the title is
  a copper plate being prepared: the visitor watches the brightest
  moment of the page's life happen once, at the start, knowing the
  whole page after it is the slow greening. It never repeats —
  polish a headline twice and it becomes a logo animation.
- **Structure.** The hero headline sits in its plate (§4) as solid
  Fraunces in `--ink-bronze` on a stage-0 `--copper` ground (3.93:1,
  display only per §2). Above it, a `pointer-events: none`,
  `aria-hidden` overlay duplicates the plate's box: a linear
  gradient mask (`--copper-hi` at 0 → 0.55 → 0 across a 34% band)
  whose `mask-position` / background position is animated by CSS
  keyframes once. The letters' sequential brightening is faked
  honestly: the gradient band is narrower than the headline, so
  glyphs brighten as it crosses them — no per-letter spans, no DOM
  surgery on the title text.
- **Motion spec.** Trigger: load, gated on `fonts.ready` raced
  against a 900ms watchdog (the sweep must cross set type, not a
  fallback face). Sweep: 1300ms `--ease-polish`, band travelling
  −40% → 140% of plate width. Peak overlay opacity 0.55 at the
  band's centre. At completion the overlay is removed from the DOM.
- **Choreography timeline (v2).** t+0: page paints, headline solid
  and readable (the sweep is not the reveal) → fonts ready →
  t+120ms: band enters at the plate's left rim → t+650ms: band
  centre crosses the headline's midpoint, first half of the title
  at peak bright → t+1180ms: last glyphs pass peak → t+1300ms:
  band exits, overlay removed → the headline rests at stage 0,
  the brightest it will ever be; §6.2 owns it from here.
- **State matrix (v2).** *Rest (pre-sweep / no-JS):* solid headline
  at stage 0 — the finished state. *Sweeping:* 1300ms, identical
  desktop and touch. *Hover:* no effect; the pass does not re-fire
  (re-polish of the hero plate is §6.5's, and it is the visitor's
  act, not a replay). *Focus:* the headline is not focusable; its
  plate's link, if any, behaves per §6.10. *Scrolled-past:* if the
  visitor scrolls during the sweep it completes off-screen or is
  cut at plate exit; it never follows. *Disabled:* no-JS and
  reduced-motion rest (below).
- **Content merge.** The sweep polishes the title's own plate; the
  brightening letters are the headline itself. Remove the headline
  and there is nothing to polish; remove the sweep and the hero is
  complete, merely unannounced.
- **Failure fallback.** The overlay is JS-inserted; its absence is
  the fallback. If `fonts.ready` never resolves, the 900ms watchdog
  fires the sweep anyway or not at all — either way the headline
  has been readable since first paint.
- **Reduced-motion variant.** No sweep. The headline rests at the
  static variant's `--stage-mid` plate (§5), fully legible.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: sweep
  1150ms, band 40% wide. <768px: sweep 950ms, band 55% — a phone's
  plate is narrow and a long ceremony delays the reading.
- **Edge cases & failure modes (v2).** *Headline wraps to 3 lines:*
  the band travels diagonally (gradient angle 12°) so line 3 is
  polished last, not simultaneously. *bfcache restore:* no replay —
  the object was never un-polished in the visitor's absence.
  *Slow device:* if the first sweep frame measures >32ms, the
  overlay is dropped and the headline simply rests.
- **Accessibility spec (v2).** The overlay is `aria-hidden` and the
  headline is plain DOM text, readable from t+0 at every instant —
  the sweep never reduces glyph contrast below its rest value
  (it only adds light). Nothing is announced; nothing is focusable.
- **Performance budget & mobile variant.** One gradient layer, one
  composited position animation, ≤0.3ms script per frame, removed
  at completion. Mobile: the 950ms variant above.
- **Tokens consumed (v2).** `--copper`, `--copper-hi`,
  `--ink-bronze`, `--ease-polish`, `--dur-polish` (1300ms).

### 6.2 Scroll patination

- **What & why.** The theme's thesis, performed by the scroll. Every
  metallic surface on the page — plate frames, rules, the strip,
  furniture — greens as the visitor descends, interpolating the
  five stages of §2 in order, driven by the one `--age` formula of
  §5. It belongs because it is not an effect applied to the page;
  it is the page's material obeying its nature at reading speed.
  A visitor who scrolls back up watches the metal *hold* its age —
  oxidation does not run backwards for a reader's convenience;
  only the visitor's hand (§6.5) reverses it, locally, briefly.
- **Structure.** Each metallic surface carries `data-metal` and a
  depth offset. Its colour is not set in CSS directly: the shared
  loop writes one `--stage-col` custom property per surface (a
  colour interpolated in JS between the five stop hexes, or — the
  cheaper build — a crossfade of two stacked layers at adjacent
  stages with opacities summing to 1; §14 chooses per build, the
  spec is identical either way). Text never consumes `--stage-col`
  (§3 law 1). The mottled texture layer (an SVG feTurbulence tile,
  `aria-hidden`) gains opacity from stage 2 onward, so late surfaces
  are not flat green but mineral.
- **Motion spec.** Continuous scrub: `--age` per §5's formula,
  lerped at 0.09 (`--ease-glide`) in the shared loop. Stage bands:
  age 0–0.12 stage 0→1, 0.12–0.38 →2, 0.38–0.68 →3, 0.68–1 →4,
  with each surface's depth offset applied before banding. Scrolling
  up: `--age` does not decrease from scroll (the dwell share may
  still grow it slowly); the value is `max(previous, computed)` for
  the scroll share — a ratchet, stated openly in §12's voice: "the
  page does not un-age."
- **Choreography timeline (v2).** Spatial, not temporal: at scroll
  0% the hero plate is stage 0 bright → 25%: upper plates at stage
  1–2, the strip (§6.3) a quarter green → 50%: mid-page at stage
  2–3, mottle visible on frames → 75%: stage 3 dominant, parallax
  already stilled (§5) → 100%: the footer plate at stage 4, the
  strip fully verdigris, the log (§6.9) prints the visit's total.
- **State matrix (v2).** *Rest (any scroll position):* surfaces at
  the formula's stage for that position — the state *is* the
  position. *Hover:* §6.5 locally overrides the hovered surface
  only. *Focus:* no change. *Active:* §6.6's thumbprint is a local
  bright mark on top of the stage colour. *Scrolled-past:*
  surfaces keep the greatest stage they reached (ratchet).
  *Disabled:* no-JS renders every surface at its band's *final*
  stage from markup classes — the printed page is the fully aged
  page, complete and legible.
- **Content merge.** The surfaces that age are the content's own
  furniture: the frame around *this* photograph, the rule above
  *this* section. There is no background layer ageing behind
  unrelated content; the metal that greens is the metal the
  visitor has been reading against.
- **Failure fallback.** If the loop stalls for 1200ms (watchdog),
  all surfaces snap to the stage their markup class declares —
  the no-JS state — and the page continues as a static aged
  object. A surface whose texture tile fails simply stays a flat
  stage colour: correct, if plainer.
- **Reduced-motion variant.** No scrub, no ratchet: every surface
  sits at `--stage-mid` (§2), one fixed mid-patina, per §5.
- **Breakpoints (v2).** ≥1200px: full spec, texture from stage 2.
  768–1199px: texture opacity capped at 0.5. <768px: texture cut
  entirely (flat stage colours), band thresholds unchanged — the
  arc must survive the phone intact even when the mottle cannot.
- **Edge cases & failure modes (v2).** *Very short page (one
  screen):* scrollDepth is ~0 forever, so dwell alone drives age
  to its 0.28 cap — the page warms to stage 1 and stops, honestly:
  a page barely read has barely aged. *Anchor jump to footer:*
  surfaces snap to the jumped-to stages within one frame; no
  catch-up sweep (chemistry does not perform for teleporting
  visitors). *Print:* surfaces print at their markup stages.
- **Accessibility spec (v2).** Colour change is never the sole
  carrier of information: stage is also printed as apparatus text
  at each band boundary ("STAGE III — VERDIGRIS" in the margin,
  §4), so a visitor who cannot see the green still reads the
  ageing. Text contrast is stage-invariant by §3 law 1.
- **Performance budget & mobile variant.** One custom-property
  write per visible metallic surface per frame, ≤24 surfaces
  tracked, loop cost ≤1.0ms/frame. Mobile: flat-colour variant
  above; tracked surfaces ≤12.
- **Tokens consumed (v2).** `--copper`, `--stage-1`, `--bronze`,
  `--verdigris`, `--patina-deep`, `--age`, `--ease-glide`,
  `--lerp` (0.09).

### 6.3 Margin oxidising strip

- **What & why.** Progress, made of the theme's own metal
  undergoing its own process. The copper strip down the page's
  margin (§4) oxidises in step with scroll — bright at the top,
  full verdigris exactly as the footer arrives — so the gauge and
  the page age together and the visitor reads their progress off
  the corrosion. It belongs because a progress bar borrowed from a
  video player would be the one foreign object on the bench; this
  one is a strip of the same copper, cut from the same sheet as
  every frame it runs beside.
- **Structure.** A fixed rail at the left edge (§4 geometry): a
  track in `--limestone` shadow and a fill whose gradient is the
  five stage stops laid along its length, revealed by a
  `clip-path` inset scrubbed to `--age` in the shared loop — the
  strip does not change colour as a block; the green *front*
  descends it, with a 60px mottled leading edge (the texture tile
  of §6.2 at full opacity) where fresh oxidation is eating in.
  Beside the front, at ≥1200px only, a rotated apparatus label
  names the current stage ("STAGE II — BRONZE").
- **Motion spec.** Scrubbed 1:1 with `--age` (§5), lerp 0.09. The
  label's text changes only at stage boundaries (age crossing
  0.12 / 0.38 / 0.68), swapped instantly — paperwork, not theatre.
  At age 1 the front reaches the rail's foot and the mottle edge
  settles to flat verdigris over 600ms `--ease-age`: the gauge is
  done ageing because the page is.
- **Choreography timeline (v2).** Scrubbed map: age 0: fill 0%,
  label "STAGE 0 — BRIGHT COPPER" → 0.12: front at 12%, label
  flips to stage I → 0.5: front mid-rail, mottled edge at its
  widest → 0.68: stage III label → 1.0: front at foot, edge
  settles, label "STAGE IV — DEEP PATINA".
- **State matrix (v2).** *Rest:* front at the age-mapped position,
  holding when scroll stops — corrosion does not retreat.
  *Scrolling up:* the front holds (ratchet, §6.2); only the label
  stays honest to the *greatest* stage reached. *Hover / focus:*
  the rail is not interactive; no states. *Disabled:* no-JS ships
  the rail fully oxidised (its markup end-state) with the stage IV
  label — the printed gauge reads complete.
- **Content merge.** The strip is the margin's own metal, running
  beside the plates whose stages it summarises; its front is at
  any moment level with the visitor's depth in the page's ageing.
- **Failure fallback.** JS off: full-length verdigris strip,
  static. Loop stall: the 1200ms watchdog (§6.2) snaps it to the
  markup end-state with everything else.
- **Reduced-motion variant.** The strip is drawn to the
  age-mapped length instantly per scroll position (a scrubbed
  state, not an animation), in flat `--stage-mid`, label updates
  at boundaries as specced.
- **Breakpoints (v2).** ≥1200px: 14px rail + rotated label.
  768–1199px: 8px rail, label horizontal at the rail's head,
  updated at boundaries. <768px: the rail moves to the top edge,
  4px high, full width, no label — the stage name appears instead
  in the navigation (§6.10) as apparatus text.
- **Edge cases & failure modes (v2).** *Short page:* the strip
  maps the dwell-capped age (§6.2) and may end at stage I — the
  gauge reports the visit truthfully rather than forcing a full
  green. *Resize:* rail length re-measures, front re-maps
  proportionally in one frame. *Print:* rail absent.
- **Accessibility spec (v2).** The rail is `aria-hidden`; the
  information it carries (progress + stage) is duplicated as real
  text: the stage label is a live-region-free plain element at
  ≥768px, and §6.10's navigation carries "Stage n of IV" as text
  at every size, so nothing is lost by hiding the rail from AT.
- **Performance budget & mobile variant.** One clip-path write
  per frame in the shared loop; the gradient is a single painted
  layer. Mobile: the top-edge variant above.
- **Tokens consumed (v2).** `--copper`, `--stage-1`, `--bronze`,
  `--verdigris`, `--patina-deep`, `--age`, `--ease-age`.

### 6.4 Before/after restoration showcase

- **What & why.** The theme's proof, performed on the product
  photograph itself. The restoration section pins for 160vh while
  one object — a verdigris-crusted lamp, a green door knocker, a
  harbour bell — crossfades between its *before* (as-found, full
  patina) and *after* (restored, polished) states, scrubbed to
  scroll, so the visitor performs the restoration at reading speed
  with their own hand on the scroll. It belongs because this is the
  service the theme's best-fit sites sell (§1), and a before/after
  slider the visitor drags would make it a tool demo; the pin
  makes it a narrative: you descend, the object is cared for.
- **Structure.** A sticky stage (100vh) holding one plate (§4):
  two renditions of the same photograph, pixel-registered, the
  *after* stacked over the *before*, its opacity scrubbed 0→1
  across the pin's 160vh by the shared loop. A hairline `--copper`
  rule marks the blend front on the image's edge. In the working
  margin (§4): the conservator's caption in Fraunces italic —
  object name, as-found condition, treatment, hours — and a stage
  readout that counts the blend ("RESTORATION 62%") in tabular
  apparatus figures. Both renditions carry the same alt text base;
  the pair is one figure with one caption.
- **Motion spec.** Pin: 160vh scroll length, stage sticky.
  Crossfade: opacity of the after-layer = clamp(pin progress ×
  1.15 − 0.075), so the blend starts 7.5% into the pin and
  completes at 93% — the object rests briefly in each pure state
  at the pin's ends. Lerp 0.09. No scale, no blur (§5's refusal):
  restoration is surface, not focus.
- **Choreography timeline (v2).** Pin progress 0: pure before,
  readout "AS FOUND" → 0.075: blend begins at the object's
  brightest edge (the mask is a linear gradient following the
  opacity, angled to the object's own highlight direction,
  declared per build) → 0.5: half-restored, readout "RESTORATION
  50%" → 0.93: fully polished → 1.0: pin releases; the restored
  object scrolls away as an ordinary plate, and the caption's
  final line ("Returned to the client, October.") has been
  readable since 0.8.
- **State matrix (v2).** *Rest (before pin):* before-state plate,
  ordinary. *Blending:* scrubbed, reversible within the pin —
  scrolling up un-restores, the one lawful reversal besides
  §6.5, because the pin is a demonstration, not the page's own
  ageing. *After pin:* after-state, static. *Hover:* none (the
  stage is not a control). *Focus:* the figure is not focusable;
  its caption link behaves per §6.10. *Touch:* identical scrub —
  the pin is scroll, not gesture. *Disabled:* no-JS shows the two
  renditions stacked vertically, before above after, each
  captioned — the printed comparison.
- **Content merge.** The crossfade happens *on the object's own
  photograph*, registered pixel to pixel; the readout counts this
  object's restoration, and the caption is its real treatment
  record. There is no generic slider chrome anywhere in it.
- **Failure fallback.** If either rendition fails to load, the
  other stands alone with its caption and a clerk's line in the
  margin: "ONE STATE OF THIS OBJECT IS NOT SHOWN — THE RECORD IS
  INCOMPLETE." (§12's error voice) — never a broken frame, never
  a silent substitution. If the loop stalls, the watchdog leaves
  whichever state is nearer, fully opaque.
- **Reduced-motion variant.** No pin, no scrub: before and after
  sit side by side (≥768px) or stacked (<768px), each at full
  opacity with its own caption line. The comparison survives
  entire; only the performance rests.
- **Breakpoints (v2).** ≥1200px: pin 160vh, caption in the working
  margin. 768–1199px: pin 130vh, caption beneath the plate.
  <768px: pin 110vh, blend thresholds widened (starts 4%,
  completes 96%) because phone scroll is fast and the pure states
  deserve their moment.
- **Edge cases & failure modes (v2).** *Misregistered renditions:*
  a build error, caught at the gate (§10) — the two states must
  align to the pixel or the restoration reads as a dissolve
  between two objects. *Very tall object:* the plate crops to
  4:3 maximum; the crop is declared in the caption. *Second
  showcase on one page:* forbidden — one restoration performed
  per page; further objects use §6.12 cards with both states
  printed statically.
- **Accessibility spec (v2).** One figure, one alt ("The harbour
  bell, as found and as restored"), the blend `aria-hidden` as a
  visual state of that single figure; the readout's percentage
  is visual apparatus and is *not* live-announced (a screen
  reader gets the caption's prose, which states the treatment
  and its result in words).
- **Performance budget & mobile variant.** Two image layers, one
  opacity write per frame inside the pin only; layers are
  `visibility: hidden` outside the pin's range. Rendition set
  ≤380KB total. Mobile: the 110vh variant above.
- **Tokens consumed (v2).** `--copper`, `--verdigris`,
  `--ink-bronze`, `--ease-glide`, `--lerp` (0.09),
  `--pin-showcase` (160vh).

### 6.5 Re-polish hover

- **What & why.** Care, enacted by the visitor's hand. Hovering
  any patinated metallic surface wipes the patina away radially
  under the pointer — a circular mask centred on the cursor
  reveals bright stage-0 copper beneath, as if the visitor's
  thumb had rubbed the metal clean — and on leave, the patina
  re-forms over ~6s, the green creeping back from the mask's edge
  inward. It belongs because it is the theme's promise in
  miniature: these objects respond to handling, and their beauty
  is maintained by touch, not despite it. It is also the one
  lawful reversal of §6.2's ratchet — local, temporary, and
  visibly the visitor's own doing.
- **Structure.** Each `data-metal` surface gains a polish layer:
  an absolutely positioned clone of its surface at stage 0
  (`--copper` with the brushed-grain tile), masked by a radial
  gradient centred on the pointer (`--polish-x`, `--polish-y`
  custom properties written by the loop), mask radius 90px at
  ≥1200px. The layer is `aria-hidden`, `pointer-events: none`,
  inserted by JS only. Text sits above the layer and is never
  masked — the polish reveals the *surface*, and §3 law 1 keeps
  the words out of the chemistry entirely.
- **Motion spec.** Pointer enter: mask radius grows 0 → 90px over
  260ms `--ease-polish`, following the pointer thereafter with
  lerp 0.35 (tight — the rubbed spot must feel *held*, not
  chased). Pointer leave: radius holds 400ms (the hand lifts,
  the bright spot lingers), then the patina re-forms over 6000ms
  `--ease-age` as the mask radius shrinks 90 → 0 with the
  mottled edge (§6.3's texture) leading the shrink — the green
  returns from the edges, as it does on real metal.
- **Choreography timeline (v2).** t+0: pointer enters surface →
  t+0–260ms: bright disc opens under the pointer → hold: disc
  follows at lerp 0.35, radius breathing ±4px with pointer speed
  (faster hand, wider rub — capped at 110px) → leave t+0: disc
  holds → t+400ms: re-formation begins → t+3400ms: disc at ~30px,
  mottle edge dominant → t+6400ms: surface fully back at its
  formula stage; layer idles (kept, at radius 0).
- **State matrix (v2).** *Rest:* no disc; surface at formula
  stage. *Hover (desktop):* as specced. *Focus:* keyboard focus
  on an interactive metal element (a §6.13 button, a §6.10 link
  plate) opens the disc centred on the element for as long as
  focus holds — parity is non-negotiable; the disc is centred,
  not pointer-tracked. *Active:* §6.6's thumbprint adds on top.
  *Scrolled-past:* layers idle at radius 0; no re-formation runs
  off-screen. *Touch:* no hover exists — a tap on a metal surface
  opens the disc at the tap point for 1200ms then re-forms over
  3000ms (a shorter arc; a phone visitor's tap is a nudge, not a
  rub), and the tap still performs the surface's own action if it
  has one — polish never taxes the first tap. *Disabled:* a
  surface whose content is unavailable carries no polish layer.
- **Content merge.** The disc reveals the surface's *own* younger
  self — the same frame, the same plate, at stage 0. It is not a
  spotlight laid over content; it is the content's material
  remembering what it looked like new, exactly where the visitor
  touched it.
- **Failure fallback.** No JS: no layer, surfaces at their stages,
  complete. If the mask fails (unsupported), the layer is never
  inserted — the build detects mask support before arming.
- **Reduced-motion variant.** No disc, no re-formation: focus (not
  hover) on an interactive metal element swaps its frame to
  stage 0 instantly for the focus duration — the information
  ("this brightens under attention") survives as a state change,
  not a performance.
- **Breakpoints (v2).** ≥1200px: radius 90px, re-form 6000ms.
  768–1199px: radius 72px, re-form 5000ms. <768px: tap variant
  only, radius 56px.
- **Edge cases & failure modes (v2).** *Pointer races across many
  surfaces:* each surface owns its layer; enter/leave are
  debounced 60ms so a diagonal skim doesn't strike six discs.
  *Surface smaller than the disc:* radius clamps to the surface's
  smaller dimension × 0.6 — a rule line can be polished, but the
  disc may not spill onto the stone. *Re-entry during
  re-formation:* the shrink reverses from its current radius —
  the hand returns mid-creep and the green retreats again, no
  jump. *Contrast:* the disc reveals stage-0 copper under
  `--ink-bronze` display text at 3.93:1 — display sizes only,
  which is why §2 forbids body text on metal in the first place.
- **Accessibility spec (v2).** Purely visual; `aria-hidden`; the
  focus variant exists so keyboard visitors receive the same
  state information sighted pointer users do. Nothing about the
  content's meaning rides on the disc.
- **Performance budget & mobile variant.** One masked layer per
  hovered surface, two custom-property writes per frame, only
  while a pointer is down on metal. Mobile: the tap variant
  above; layers are built lazily per surface on first touch.
- **Tokens consumed (v2).** `--copper`, `--copper-hi`,
  `--polish-x`, `--polish-y`, `--ease-polish`, `--ease-age`,
  `--dur-reform` (6000ms), `--polish-r` (90px).

### 6.6 Thumbprint click

- **What & why.** Handling metal leaves a mark. Clicking any
  button in this theme leaves a bright thumbprint-polish at the
  exact click point — an elliptical bright patch, slightly
  smudged in the direction of the press — which fades back to
  the button's stage colour over 4s. It belongs because click
  feedback in a metal world should be a physical trace, not a
  ripple borrowed from a touchscreen demo: the visitor pressed
  the object, and the object shows where. It is also honest
  feedback — the mark is *at* the point of contact, sized like a
  thumb, and it decays like a real polish mark under fresh
  oxidation.
- **Structure.** Every `<button>` and button-styled link carries
  a `::after`-equivalent span (a real child, `.thumb`, inserted
  by JS) sized 34×26px, border-radius 50%, background
  `--thumbprint` with a soft irregular edge (two overlapping
  radial gradients, rotated −18° — the smudge). On activation
  the span is positioned at the pointer coordinates (or the
  element's centre for keyboard activation), scaled 0.7 → 1 over
  120ms `--ease-engrave` (the press), then its opacity decays
  0.85 → 0 over 4000ms `--ease-age`. One span per button, reused;
  a second click re-stamps at the new point.
- **Motion spec.** Press: 120ms. Hold at full: 300ms. Decay:
  4000ms to invisible, with the last 800ms accelerating (the
  final tarnish closes quickly). The button's own press state
  (translateY 1px) runs concurrently and independently — the
  thumbprint is the *trace*, not the button's whole feedback.
- **Choreography timeline (v2).** t+0: activation → t+0–120ms:
  print stamps in at the point → t+120–420ms: print at full
  brightness, button's action proceeds immediately (the mark
  never delays the deed) → t+420–3620ms: slow tarnish →
  t+3620–4420ms: final fade → span idles invisible.
- **State matrix (v2).** *Rest:* no print (span at opacity 0).
  *Hover:* no print — hovering is §6.5's rub, and a print
  without a press would be a lie. *Focus:* no print until
  activation. *Active:* as specced; keyboard Enter/Space stamps
  at centre with a rounder print (no smudge direction — a key
  has no thumb angle). *Scrolled-past:* a decaying print
  continues off-screen harmlessly; it is opacity only.
  *Disabled button:* no print, ever — a disabled control must
  not record a handling it refused. *Touch:* identical, stamped
  at the tap point.
- **Content merge.** The print lands on the button the visitor
  actually pressed, at the point they pressed it — feedback
  physically continuous with the action. Remove the button and
  there is nowhere for the mark to live.
- **Failure fallback.** No JS: buttons are plain, fully
  functional, with the standard focus and active states of
  §11. The print is an inserted span; its absence is invisible.
- **Reduced-motion variant.** The print appears at full for
  600ms and vanishes (no decay animation) — acknowledgement
  without the chemistry lesson.
- **Breakpoints (v2).** All sizes identical; print size scales
  to 28×22px below 768px (thumbs on phones press smaller
  targets, and §11's 44px minimum target law still holds).
- **Edge cases & failure modes (v2).** *Rapid clicking:* the
  span re-stamps per click, restarting the decay — a much-used
  button looks much-handled, which is the truth of it. *Click
  near the button's edge:* the print clamps inside the button's
  box (overflow hidden) — a half-print at the rim is correct
  and intended. *Form submit with validation errors:* the
  print still stamps (the press happened) and §6.13's error
  notes appear — the mark never claims success, only contact.
- **Accessibility spec (v2).** Decorative, `aria-hidden`; the
  button's action result is announced by its own live region
  or page change per §11, never by the print. Focus ring
  (§11) is unaffected and renders above the print.
- **Performance budget & mobile variant.** One span, opacity +
  transform on the compositor; negligible. Mobile: as specced.
- **Tokens consumed (v2).** `--thumbprint`, `--ease-engrave`,
  `--ease-age`, `--dur-thumb` (4000ms).

### 6.7 Patina bloom

- **What & why.** Even at rest, the page's materials keep ageing.
  In one designated corner panel — a specimen plate in the
  page's second half — patina mottling slowly blooms outward
  from one corner over 30s: irregular green islands expanding,
  merging, deepening, the quiet chemistry of a surface left to
  the air. It belongs because it is the theme's only ambient
  motion and it earns that singularity: it happens *inside a
  content panel* (a specimen of untreated copper, labelled as
  such), at chemistry's pace, and it stills the moment it
  leaves the viewport. A page where everything drifts is a
  screensaver; a page where one specimen keeps oxidising is a
  laboratory.
- **Structure.** The specimen plate (§4) holds a stage-1 copper
  field whose mottle layer (the §6.2 SVG turbulence tile,
  masked by three overlapping radial gradients anchored at the
  plate's bottom-left corner) scales its mask radii from 12% →
  88% of the plate over 30000ms `--ease-age`, looping only in
  the sense that at full bloom it holds for 10s and resets
  during an off-screen interval — the reset is never witnessed;
  if the plate is on-screen at the 40s mark, the bloom simply
  holds at full until it next leaves the viewport. The plate's
  caption states what it is: "Untreated copper, cast [year].
  Blooming since you arrived." — with the year the publisher's
  real casting year (§1's law).
- **Motion spec.** Mask radii interpolate linearly in the
  shared loop from the plate's first viewport entry; total
  30000ms to full bloom, mottle opacity 0 → 0.85 across the
  same span, deepening `--stage-1` → `--verdigris` by the
  §6.2 stage interpolation at double rate (the specimen is
  *untreated* — it ages faster than the cared-for page, which
  is the caption's point). Pauses off-screen
  (IntersectionObserver) and when the tab is hidden.
- **Choreography timeline (v2).** t+0: plate enters viewport,
  bloom at 12% → t+10000ms: islands at ~40%, first merges →
  t+20000ms: ~65%, green dominant in the corner half →
  t+30000ms: 88%, full bloom, hold → t+40000ms: if off-screen,
  reset to 12% for the next viewing; if on-screen, hold.
- **State matrix (v2).** *Rest (pre-entry / no-JS):* the plate
  ships at 55% bloom, static — a specimen mid-age, honest at
  any moment. *Blooming:* as specced, desktop and touch
  identical. *Hover:* §6.5's disc works on the specimen too —
  the visitor can rub one spot clean and watch the bloom
  re-take it; the two systems compose, neither cancels.
  *Focus:* none (not a control). *Scrolled-past:* paused at
  its current radius. *Disabled:* reduced-motion rests at the
  shipped 55%.
- **Content merge.** The bloom happens to the specimen the
  caption describes, inside its own plate, at the rate the
  caption claims. It is a demonstration the page makes about
  its own material, not weather pasted behind text.
- **Failure fallback.** The shipped 55% static state is the
  fallback in full: no JS, no mask support, no loop — the
  specimen simply *is* half-bloomed, and the caption still
  tells the truth about it.
- **Reduced-motion variant.** Static at 55%, permanently.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px:
  bloom span 36000ms (a smaller plate, a slower read).
  <768px: bloom span 36000ms, mask anchors simplify to one
  radial gradient — the phone specimen keeps the chemistry,
  drops the cartography.
- **Edge cases & failure modes (v2).** *Plate near the
  footer:* the bloom and §6.2's late stages coincide — the
  specimen may reach full bloom *and* deep stage; that is
  correct, it is the oldest object on the page. *Visitor
  reads for 10 minutes:* the bloom holds at full; chemistry
  that finished does not restart for entertainment.
  *Battery saver:* the loop's observer caps apply; the bloom
  is the first ambient cut in §14's order.
- **Accessibility spec (v2).** Decorative layer `aria-hidden`;
  the caption is real text and carries the meaning. The bloom
  never crosses text (the caption sits outside the metal
  field, on stone).
- **Performance budget & mobile variant.** One mask-position
  interpolation on one layer, only while visible. Mobile:
  the single-gradient variant above.
- **Tokens consumed (v2).** `--stage-1`, `--verdigris`,
  `--ease-age`, `--dur-bloom` (30000ms).

### 6.8 Maker's mark engraving

- **What & why.** The footer plate is signed. As it enters,
  the maker's mark — the foundry's or maker's device, an SVG
  monogram or hallmark punch — draws itself stroke by stroke
  over 1400ms, then inks dark: the lines deepen from scribed
  bright to filled `--ink-bronze`-on-metal over 400ms, the way
  an engraving fills with ink when it is wiped and printed. It
  belongs because authorship on a metal object is not a logo
  pasted in a footer; it is cut into the plate, and the visitor
  who reaches the end — the oldest part of the page — watches
  the object being signed in front of them.
- **Structure.** An inline SVG of the mark (paths only, stroke
  `--copper-hi` at draw time, fill transparent), set in the
  footer plate (§6.15) at 64–88px, beside the colophon
  lettering. Each path carries `pathLength="1"`; dashoffset is
  armed by JS only — the shipped state is fully drawn and
  inked, so no-JS shows the signed plate. After the draw, a
  class swap transitions stroke to the inked state and fades
  in the fill at 12% (an engraved line is a groove, not a
  solid).
- **Motion spec.** Trigger: footer plate crosses 30% viewport.
  Draw: strokes in path order, total 1400ms `--ease-engrave`,
  stagger proportional to path length (the longest cut gets
  the longest time — the chisel does not hurry a long line).
  Ink: 400ms `--ease-polish` beginning at draw completion.
  Fires once per page view; scrolling away and back does not
  re-engrave.
- **Choreography timeline (v2).** t+0: plate at 30% viewport →
  t+0–1400ms: strokes draw in order → t+1400ms: last cut
  completes → t+1400–1800ms: ink deepens, fill settles at 12%
  → the mark rests, signed; the log line (§6.9) prints beneath
  it at t+1800ms — the signature first, then the record.
- **State matrix (v2).** *Rest (shipped / no-JS):* mark fully
  drawn and inked. *Drawing:* 1400ms, identical desktop and
  touch. *Hover:* none — one does not hover a hallmark.
  *Focus:* the mark is not focusable; the footer's links
  behave per §6.10. *Scrolled-past:* inked, terminal.
  *Disabled:* reduced-motion shows the inked rest state.
- **Content merge.** The mark is the plate's own signature —
  the same device the maker's real objects carry (the build
  uses the client's actual hallmark artwork; an invented
  monogram for a real maker is a §10 failure under the one
  law's corollary).
- **Failure fallback.** Shipped drawn; JS only re-arms the
  dash. If the SVG fails, the maker's name in Fraunces
  (§6.15's colophon line) still signs the plate in type.
- **Reduced-motion variant.** Inked at rest; no draw.
- **Breakpoints (v2).** ≥1200px: mark 88px, draw 1400ms.
  768–1199px: 72px, 1250ms. <768px: 64px, 1100ms — the
  signature is not smaller in *importance*, only in plate.
- **Edge cases & failure modes (v2).** *Footer reached by
  anchor jump:* the mark is already inked when the visitor
  lands (the draw is for those who *arrive* by reading; a
  jump fires the completed state via the watchdog rule of
  §6.2). *Mark with many paths (>12):* stagger compresses so
  the total stays 1400ms — the gate (§10) caps path count at
  build, since a hallmark is a punch, not a picture.
- **Accessibility spec (v2).** The SVG carries `role="img"`
  and the maker's name as its label ("Mark of [maker]") —
  the one decorative-adjacent element that is *not*
  aria-hidden, because a signature is content.
- **Performance budget & mobile variant.** ≤12 stroked paths,
  one draw, then static forever. Mobile: as specced.
- **Tokens consumed (v2).** `--copper-hi`, `--ink-bronze`,
  `--ease-engrave`, `--ease-polish`, `--dur-engrave` (1400ms).

### 6.9 Patina log

- **What & why.** The theme's signature record, and its
  anti-slop detail raised to a system. The footer keeps a
  log, set in apparatus type, of what this visit did to the
  page: "YOUR VISIT AGED THIS PAGE BY 0.03 YEARS." — computed
  from the visit's real dwell and depth by the declared
  conversion (§12 prints it: 1 page-year = 240s of attended
  reading at full depth, pro-rated). It belongs because it
  closes the theme's argument in the visitor's own case: they
  came to read about things that age, and the page enters
  *their* handling into its history, the way a conservator
  logs every touch an object receives. It is the only element
  in the library that is about *this* visitor, and it works
  because every number in it is measured, not scripted.
- **Structure.** A log block in the footer plate (§6.15):
  a heading line ("PATINA LOG — THIS COPY"), then up to
  four lines appended as events occur: arrival ("OPENED AT
  STAGE 0 — BRIGHT."), the showcase completed ("ONE
  RESTORATION WITNESSED."), deepest stage reached ("DEEPEST
  STAGE REACHED: III."), and the closing line with the
  computed years figure, printed when the footer first
  enters and updated live while the visitor lingers there.
  Lines are real DOM text, appended (never marquee-scrolled,
  §5's refusal), each fading in over 300ms `--ease-settle`
  as a clerk enters it. The figure computes as
  `years = age × (dwellSeconds / 240)` rounded to 2 decimals,
  capped at 1.00 — one visit can age the page at most one
  full year, and the cap is printed in §12 so the number's
  honesty is auditable.
- **Motion spec.** Line entry: opacity 0 → 1, 300ms, no
  transform (paperwork does not slide). The years figure
  counts in tabular numerals over 600ms when the closing
  line first prints, then updates in place every 10s while
  the footer is on-screen (a figure that ticks every second
  is a stopwatch, not a log).
- **Choreography timeline (v2).** Arrival line: logged at
  load (visible when the footer is reached). Showcase line:
  appended at §6.4's pin completion. Deepest-stage line:
  appended at the moment age first crosses 0.68. Closing
  line: printed at footer entry with the then-current
  figure → updates at +10s intervals while visible → the
  mark (§6.8) finishes engraving above it at footer
  entry +1800ms, and the log is complete beneath the
  signature.
- **State matrix (v2).** *Rest:* lines logged so far, static
  text. *Hover / focus:* none — the log is read, not used.
  *Active:* n/a. *Scrolled-past:* lines persist (a record
  does not unwrite). *Disabled / no-JS:* the log prints a
  single honest line: "PATINA LOG — KEPT BY HAND IN THE
  WORKSHOP; THIS PRINTED COPY RECORDS NO VISIT." — the
  no-JS page admits it cannot measure, rather than inventing
  a figure. *Reduced motion:* lines appear without the fade.
- **Content merge.** Every line is a fact of *this page and
  this visit*: the stages named are the stages §6.2 actually
  reached, the restoration is §6.4's, the figure is the
  formula's. The log is the page's memory of being read —
  there is no version of it that could sit on another site.
- **Failure fallback.** If measurement fails (no rAF, no
  clock), the log degrades to the no-JS line above — an
  honest gap in the record, in the theme's own voice.
- **Reduced-motion variant.** Lines print instantly; the
  figure appears at its current value without counting.
- **Breakpoints (v2).** Identical at all sizes; below 768px
  the log wraps to full plate width and the heading shortens
  to "PATINA LOG".
- **Edge cases & failure modes (v2).** *Visitor bounces in
  3s:* the log, if ever seen, reads 0.00 years and stage 0 —
  the truth, and quietly funny, which the theme permits
  itself exactly here. *Return visit:* the log is per-visit
  (sessionStorage holds the running record within a session;
  a new session starts a new log — the object is re-polished
  between keepers, and §12's voice line says so). *Tab
  hidden for an hour:* dwell counts *attended* time only —
  `visibilitychange` pauses the clock, because an unread
  page on an open tab has not been handled.
- **Accessibility spec (v2).** Plain text in reading order;
  updates are *not* live-announced (a log that interrupts a
  screen reader every 10s is vandalism); the closing figure
  is readable as ordinary text when the visitor reaches it.
- **Performance budget & mobile variant.** A few DOM appends
  per visit and a 10s interval gated on footer visibility;
  negligible. Mobile: as specced.
- **Tokens consumed (v2).** `--ink-bronze`, `--limestone`,
  `--ease-settle`, `--age`.

### 6.10 Foundry navigation (page family: navigation)

- **What & why.** Navigation as the bench's index rail: a slim
  bar carrying the site's sections as engraved plate labels —
  Fraunces small caps on metal tabs whose stage is *fixed at
  the stage of the section they name*, so the nav is a legend
  of the page's ageing: the first tab is bright copper, the
  last is deep patina, and the visitor reads the whole arc in
  the menu before scrolling an inch. The current section's tab
  is the one being polished: it alone carries §6.5's bright
  disc, pinned at its centre by the scrollspy.
- **Structure.** A `<nav>` bar, sticky at the page top below
  768px and resident in the header plate at ≥768px: one tab
  per section, each tab a small plate (stage colour fixed by
  its section's band, §4) with its label in `--ink-bronze`
  (on deep tabs, `--limestone`). Beneath the active tab, a
  scribed rule draws to full width (180ms `--ease-engrave`)
  — links in this theme are underlined by a line *cut*, not
  coloured. At <768px the bar also carries the stage readout
  (§6.3's mobile ruling) as apparatus text at its right end.
- **Motion spec.** Hover/focus: the scribed rule draws under
  the tab (180ms) and the tab's stage brightens one stop
  toward copper (a half-polish, 240ms `--ease-polish`) —
  attention warms metal. Scrollspy: as sections cross the
  reading line, the active rule retracts from the old tab
  (140ms) and draws under the new (180ms); the pinned bright
  disc (§6.5) migrates with it over 300ms.
- **Choreography timeline (v2).** Hover: t+0 rule begins →
  t+180ms rule full, brighten complete at t+240ms → leave:
  brighten re-forms over 2000ms `--ease-age` (a nav tab
  re-oxidises faster than a plate — it is handled constantly,
  and the theme says so). Scrollspy change: t+0 old rule
  retracts → t+140ms new rule begins → t+320ms settled.
- **State matrix (v2).** *Rest:* tabs at their fixed stages,
  active tab ruled. *Hover:* as specced. *Focus:* identical
  to hover (keyboard parity), plus §11's focus ring.
  *Active / current:* ruled, disc pinned. *Scrolled-past:*
  the bar scrolls away with the header at ≥768px (no
  persistent sticky chrome on desktop — the strip, §6.3, is
  the page's persistent instrument); below 768px it sticks,
  because a phone visitor needs the index more than the
  purity. *Disabled:* a section that does not exist gets no
  tab — never a greyed tab (§11's refusal).
- **Content merge.** The tabs *are* the sections, coloured by
  the sections' own stages — the nav is a true map of the
  page's ageing, generated from the sections it names.
- **Failure fallback.** Plain link list in the header plate;
  rules are CSS, scrollspy is the only JS, and its absence
  leaves the first tab ruled by the server where known.
- **Reduced-motion variant.** No rule draws, no brighten:
  the active tab is marked by weight and the rule appears
  instantly.
- **Breakpoints (v2).** ≥1200px: tabs in one row in the
  header plate. 768–1199px: tabs wrap to two rows, brighten
  retained. <768px: sticky bar, horizontal scroll of tabs
  (with the stage readout fixed at the right), rule draws
  retained at 140ms.
- **Edge cases & failure modes (v2).** *Many sections
  (>7):* the nav lists first-level sections only; subsections
  are reached from their section's own plate links — an index
  rail of 15 tabs is a directory, not a bench. *Long section
  names:* truncate at 18ch on the tab, full name in the
  section heading and `aria-label`. *Single-section page:*
  the nav is omitted; a one-object page has no index.
- **Accessibility spec (v2).** Real `<nav>`, `aria-label`
  "Sections of this page"; `aria-current="true"` on the
  active tab, updated on scrollspy changes only. Tabs are
  links ≥44px tall below 768px, ≥32px at desktop with the
  rule as the visible state. Stage colours never carry the
  current-state information alone — the rule and weight do.
- **Performance budget & mobile variant.** Scrollspy on the
  shared IntersectionObserver; rule draws are CSS. Mobile:
  the sticky variant above.
- **Tokens consumed (v2).** `--copper`, `--bronze`,
  `--verdigris`, `--patina-deep`, `--ink-bronze`,
  `--limestone`, `--ease-engrave`, `--ease-polish`.

### 6.11 The bright threshold (page family: hero composition)

- **What & why.** The hero is the object at the brightest
  moment of its life: one large plate at stage 0 — the
  foundry's or maker's emblematic object (the bell, the gate,
  the flagship piece) photographed on limestone, its copper
  frame still warm from the polish pass — with the headline
  plate (§6.1) overlapping its lower rim and nothing else in
  the first screen competing. The composition's job is a
  promise the rest of the page keeps by contrast: *this is
  what new looks like; scroll, and watch what time does —
  and what care answers.*
- **Structure.** First viewport: the header plate with
  §6.10's nav; the hero plate (image at 4:3 or the object's
  own ratio, frame 3px stage-0 `--copper`, mat 24px
  limestone); the headline plate overlapping the frame's
  bottom-left by 40px at ≥1200px; one standfirst line in
  Fraunces italic (the conservator's voice, §3) and one
  action — a §6.13 button in bright copper, the only
  stage-0 interactive element on the page. Below the fold,
  the second section's first plate just shows, already a
  breath warmer (stage 1 at its top edge) — the arc is
  visible from the first screen.
- **Motion spec.** On load: §6.1's polish pass, and nothing
  else moves. The hero plate's parallax (§5's upper-half
  strata) engages only once the visitor scrolls. No entrance
  fade, no rise: a cast object does not float up; it is
  *there*, heavy, from first paint.
- **Choreography timeline (v2).** t+0: hero complete at
  stage 0 → t+120ms–1420ms: §6.1's sweep → first scroll:
  §6.2's formula takes ownership of every surface including
  this frame — the hero begins, almost imperceptibly, to
  warm. The visitor who never scrolls keeps a perfect,
  bright, complete page: the threshold is a whole statement,
  not a teaser.
- **State matrix (v2).** *Rest:* as composed. *Hover:*
  §6.5 on the frame; the action button per §6.13. *Focus:*
  first tab stop is the nav (§6.10), then the hero action.
  *Scrolled-past:* the hero ages with everything else (its
  frame is `data-metal` like any other) — returning to the
  top shows a page slightly older than the one first seen,
  which is the theme's quietest joke and its whole point.
  *Disabled:* no-JS renders the hero complete at stage 0
  with the second section at its markup stage.
- **Content merge.** The object in the plate is the site's
  real subject — the maker's actual flagship piece, the
  studio's actual emblematic restoration. A stock photograph
  of generic copperware here fails §10: the threshold shows
  *the* object, or the theme has nothing to age.
- **Failure fallback.** If the hero image fails, the plate
  carries the object's name and specification in type
  (Fraunces display + apparatus data) — a nameplate without
  the object, still a true threshold.
- **Reduced-motion variant.** The hero at `--stage-mid`
  (§5's static variant), complete; the polish pass does not
  run.
- **Breakpoints (v2).** ≥1200px: overlap composition as
  specced. 768–1199px: headline plate below the image, no
  overlap (a tablet's threshold is narrower). <768px: plate
  full-width, headline plate stacked, action full-width —
  one object, one statement, no squeeze.
- **Edge cases & failure modes (v2).** *Short viewport
  (<600px tall):* the mat compresses to 14px and the
  standfirst is cut before the object is — the object must
  be visible in the first screen at any height (§10 checks
  600px). *Object with no good photograph:* the nameplate
  fallback above becomes the design, not the exception —
  better a true plate of type than a borrowed image.
- **Accessibility spec (v2).** The hero image carries real
  alt naming the object; the headline is the page's `<h1>`;
  DOM order is nav → headline → standfirst → action, with
  the image decorative-adjacent to the headline it
  illustrates (alt still provided — the object is content,
  §6.8's ruling applies in spirit).
- **Performance budget & mobile variant.** Hero image ≤220KB
  (it is the LCP; the theme spends its weight budget here
  first, §14). Mobile: the stacked variant above.
- **Tokens consumed (v2).** `--copper`, `--limestone`,
  `--ink-bronze`, `--ease-polish`.

### 6.12 Object cards (page family: cards / listing)

- **What & why.** Where the site lists comparable things —
  restored objects, pieces for sale, case studies — they are
  object cards: small plates, each holding one object's
  photograph in a frame at *the stage that object has
  reached in the page's own arc* (cards are placed in the
  bands of §4, so a listing reads as a descent from bright
  to deep), its name in Fraunces, its facts in apparatus
  data (year, alloy, status), and one line of conservator's
  italic. A card in this theme is a specimen on the bench,
  not a tile in a grid.
- **Structure.** `<article class="object-card">`: figure
  (photograph, frame at the card's band stage), body (name,
  apparatus fact row, one italic line ≤16 words), and one
  action — a text link with §6.10's scribed rule, or, for an
  object with both states photographed, a two-state figure
  printed statically (before small, after large) in place of
  the single image. The whole card is never a link; the name
  is.
- **Motion spec.** Entry: §6.17's plate polish-in at card
  scale. Hover: the frame takes §6.5's disc (the card's own
  metal, rubbed), and the card lifts 2px with its plate
  shadow deepening (200ms `--ease-settle`) — a specimen
  picked up an inch, no more; objects are heavy. Focus:
  same lift, disc centred (§6.5's parity rule).
- **Choreography timeline (v2).** Entry per §6.17. Hover:
  t+0 disc opens (§6.5) → t+200ms lift settled → leave:
  lift returns 240ms, disc re-forms over the full 6000ms
  of §6.5 — a card once examined keeps its bright spot
  longest, which is how a bench actually looks at day's end.
- **State matrix (v2).** *Rest:* flat, at band stage.
  *Hover / focus:* as specced. *Active (name link):* the
  §6.18 burnish carries the visitor away. *Scrolled-past:*
  flat; disc state persists per §6.5. *Unavailable object:*
  the card is not greyed — its fact row is stamped
  "WITHDRAWN — IN THE WORKSHOP" in apparatus type and the
  link is removed; the object remains on the bench, marked
  by the clerk, not dimmed into illegibility. *Disabled:*
  no-JS shows the finished card.
- **Content merge.** The card's stage is its position in
  the page's ageing; its facts are the object's own assay
  data; its italic line is the conservator's note on *this*
  object. Nothing on the card is template furniture.
- **Failure fallback.** Static plate with photograph and
  facts; the lift and disc are enhancements on a complete
  specimen.
- **Reduced-motion variant.** No lift, no disc: hover/focus
  thickens the frame 2px → 3px and warms the name one stage
  toward copper.
- **Breakpoints (v2).** ≥1200px: cards in mixed spans within
  the reading column + margin composition (§4) — never a
  uniform 3-across grid (§9). 768–1199px: two-up.
  <768px: one-up, lift cut, disc tap variant (§6.5).
- **Edge cases & failure modes (v2).** *Missing photograph:*
  the card becomes a nameplate card (type only, §6.11's
  fallback pattern) — never a grey box, never a substitute
  object's photo. *Long italic line:* the 16-word ration is
  a build rule (§12); overflow truncates the fact row
  before the italic line is touched — the note outranks
  the data. *Many cards (>9):* the listing paginates as
  §11's plate-leaves; an endless scroll of specimens is a
  warehouse, not a bench.
- **Accessibility spec (v2).** Name link is the card's
  accessible name; photograph alt names the object or is
  empty when the name already does; fact row is real text
  in reading order; the withdrawn stamp is text, not an
  image.
- **Performance budget & mobile variant.** Card images
  ≤90KB each, lazy below the fold; lift/disc inherit
  §6.5's caps. Mobile: one-up variant above.
- **Tokens consumed (v2).** `--copper`, `--bronze`,
  `--verdigris`, `--patina-deep`, `--ink-bronze`,
  `--ease-settle`, `--ease-age`.

### 6.13 The commission form (page family: forms / conversion)

- **What & why.** Conversion in this theme is a commission:
  the visitor asks the workshop to make, restore or value an
  object. The form is a brass plate on the bench — fields as
  engraved lines to write on, labels as stamped apparatus,
  and a submit button cast at the page's current stage, which
  the visitor's own click will thumbprint (§6.6). It belongs
  because a commission is the theme's natural transaction:
  slow, specified, and answered by a person — and the form's
  honesty (name, direction, the object's story, one consent)
  is the theme's answer to the dark-pattern checkout.
- **Structure.** `<form class="commission">` inside its plate:
  fields as bottom-ruled inputs (transparent ground, 2px rule
  in the plate's stage colour, Archivo Narrow 17px input
  text, apparatus labels above): the visitor's name; their
  direction (email, labelled "YOUR DIRECTION — FOR THE
  REPLY"); the commission type as three radio *plates* (MAKE
  / RESTORE / VALUE — small metal tabs that polish when
  chosen, §6.5's disc pinned); the object's story (textarea,
  ruled lines every 31px); one consent checkbox drawn as an
  unstruck hallmark square that fills with the stage colour
  and an engraved tick when checked. Submit: a cast button,
  apparatus capitals, "COMMISSION THE WORKSHOP".
- **Motion spec.** Focus: the field's rule inks from stage
  colour to `--copper` (220ms `--ease-polish`) and a bright
  disc (§6.5, radius 40px) opens at the rule's start — the
  line being written on is the line being polished. Error:
  the rule turns `--patina-deep` darkened one step (the
  theme has no red; an error on metal is a *flaw mark*, a
  dark stamp — see §12) and the clerk's note letters in
  beneath in apparatus type. Submit: §6.6's thumbprint
  stamps, the button holds pressed at 0.98 for the send,
  and on success the whole plate is *hallmarked*: a struck
  mark (the §6.8 device at 28px) stamps beside the heading
  (scale 1.4 → 1, 160ms `--ease-engrave`) and the form is
  replaced by the acknowledgement — a short letter in the
  conservator's voice with a real reference ("COMMISSION
  Nº —" + the server's number, never a fabricated one).
- **Choreography timeline (v2).** Focus: t+0 rule inks,
  disc opens by t+260ms. Error on submit: t+0 thumbprint →
  t+160ms the first bad field's rule darkens and its note
  letters in (300ms) → focus moves to that field at t+380ms
  (§11's law). Success: t+0 print → send → response:
  hallmark stamps (160ms) → form fades at the plate's rim
  (300ms, the one lawful fade — a plate exchanged for a
  letter) → acknowledgement stands, reference and all.
- **State matrix (v2).** *Rest:* ruled plate at its band
  stage. *Hover:* §6.5 disc on the plate's rim only (fields
  are for writing, not rubbing). *Focus:* as specced; focus
  ring per §11 in addition to the inking rule. *Active:*
  the press + print. *Scrolled-past:* a half-written form
  keeps its values (no state lost to scrolling). *Disabled
  (sending):* fields disabled at full contrast — labels
  stay `--ink-bronze`; only the button dims to 0.85 — a
  disabled field that greys its text below AA is a §10
  failure. *Error:* per-field, persistent until corrected,
  never auto-dismissed; the visitor's text is never cleared
  by an error, including a server 500 (§12's kept-letter
  rule, translated: "NOT SENT — THE COURIER FAILED. YOUR
  COMMISSION IS KEPT BELOW.").
- **Content merge.** The fields are the commission's own
  particulars; the radio plates are the workshop's actual
  three services; the success state is the workshop's
  acknowledgement letter, filed on the same plate. Nothing
  about the form is a generic contact widget in costume.
- **Failure fallback.** A working HTML form — labels,
  inputs, submit — that posts without JS; server errors
  re-render in the same clerk's notes. The cast button is a
  real `<button type="submit">` with a text label.
- **Reduced-motion variant.** No disc, no stamp scale: the
  hallmark appears inked; the acknowledgement replaces the
  form without the fade; errors appear instantly with their
  notes.
- **Breakpoints (v2).** ≥1200px: form plate in the reading
  column, radio plates in a row. 768–1199px: one column,
  radio plates wrap. <768px: inputs at 17px (no iOS zoom),
  radio plates full-width stacked, submit full-width at
  52px — a thumb presses this seal, and the layout admits
  it.
- **Edge cases & failure modes (v2).** *Long object story:*
  the textarea's ruled lines extend to 10 lines, then it
  scrolls internally — a commission longer than its plate
  is the one case the fiction yields to function. *Radio
  re-choice:* the previously chosen plate re-oxidises over
  2000ms `--ease-age` while the new one polishes in 240ms —
  changing one's mind leaves a tarnish where the first
  choice was; charming, and harmless, because the *value*
  changes instantly and accessibly. *Double submit:* the
  pressed state disables the button until resolution.
- **Accessibility spec (v2).** Real `<label>` for every
  field; hints are `aria-describedby`, never placeholders
  (a blank ruled line is the invitation). Error notes are
  linked by `aria-describedby` and summarised in a
  `role="alert"` heading on failed submit. Contrast: labels
  12.46:1; error text `--patina-deep` darkened on limestone
  ≥7:1 (computed at build, §10). Touch targets: field rows
  ≥48px; radio plates ≥44px.
- **Performance budget & mobile variant.** Transitions on
  focus/submit only; no loops. Mobile: the stacked variant
  above.
- **Tokens consumed (v2).** `--copper`, `--bronze`,
  `--patina-deep`, `--ink-bronze`, `--limestone`,
  `--ease-polish`, `--ease-engrave`, `--dur-thumb` (4000ms).

### 6.14 Assay counters (page family: data)

- **What & why.** The figures a Verdigris site is allowed to
  boast with: years in service, alloy percentages, objects
  restored, generations at the bench. They are set as an
  assay table — a small engraved plate of figures in tabular
  Archivo Narrow — and they count up once, on entry, each to
  its true value. It belongs because in the metal trades a
  number is an assay: a claim about composition that can be
  tested. The counters are the theme's credibility, machined.
- **Structure.** A plate (§4) holding 2–4 figures, each:
  the figure itself (Fraunces 40px or apparatus tabular at
  display size), its label in apparatus capitals ("YEARS AT
  THE BENCH", "COPPER IN THE ALLOY", "OBJECTS RESTORED"),
  and — the theme's distinguishing discipline — a *source
  line* in 12.5px apparatus beneath the row: "FROM THE
  WORKSHOP LEDGER, [year]" or "ASSAYED [month year]". A
  figure without a source line does not ship (§10, blocking).
- **Motion spec.** Trigger: plate crosses 40% viewport.
  Count: 1200ms `--ease-age` (chemistry's easing — figures
  here *develop*, they do not snap), whole integers only,
  tabular figures, each figure staggered 150ms in reading
  order. Percentages count to their decimal as printed
  (87.5% counts to 87.5, not 88). Counts fire once; the
  plate keeps its figures thereafter.
- **Choreography timeline (v2).** t+0: plate at 40% →
  t+0–1200ms: first figure develops → t+150ms: second
  begins → t+1350ms: last figure settles → figures rest,
  permanent. If the plate is reached by anchor jump, figures
  stand at final values (the §6.2 watchdog rule).
- **State matrix (v2).** *Rest (shipped / no-JS):* figures
  at their final values — the count is a replay of the
  truth, never the only carrier of it. *Counting:* as
  specced, desktop and touch identical. *Hover / focus:*
  none. *Scrolled-past:* final values. *Disabled:*
  reduced-motion shows final values instantly.
- **Content merge.** The figures are the workshop's own
  assay data with their sources printed under them; the
  counting is the plate being read aloud slowly, once.
- **Failure fallback.** Final values in markup; JS only
  re-arms the count from a floor of 60% of value (never
  from 0 — a workshop of "0 years" for one frame is a lie
  told briefly, and the theme does not tell it).
- **Reduced-motion variant.** Final values, instantly.
- **Breakpoints (v2).** ≥1200px: figures in a row of up to
  4. 768–1199px: 2×2. <768px: stacked, figure size 32px.
- **Edge cases & failure modes (v2).** *A figure the
  publisher cannot source:* it is cut at build, and the
  plate ships with fewer figures — an assay table of two
  true numbers outranks four with a guest among them.
  *Years figure and the calendar:* "years at the bench" is
  computed from the founding year at build time and the
  source line names the ledger year, so the figure can be
  audited rather than merely believed.
- **Accessibility spec (v2).** Figures are real text at
  final values in the DOM from first paint (JS re-arms the
  count visually via a duplicate `aria-hidden` layer — the
  accessible figure never flickers through false values).
- **Performance budget & mobile variant.** One rAF-driven
  count on one plate; negligible. Mobile: stacked variant.
- **Tokens consumed (v2).** `--ink-bronze`, `--bronze`,
  `--ease-age`, `--dur-count` (1200ms).

### 6.15 The engraved plate footer (page family: footer)

- **What & why.** The page ends as the object it has become:
  one full-width plate at stage 4 (§4), limestone lettering
  on deep patina (6.26:1), carrying the maker's mark (§6.8),
  the patina log (§6.9), the colophon, and the formula — the
  audit trail of §1's law, printed where the visitor who
  aged the page can check it. There are no link columns
  pretending to be a sitemap; a plate has a face, and its
  face holds a signature, a record, and a name.
- **Structure.** `<footer>` plate: top rim a 3px rule at
  `--verdigris`; left, the mark (§6.8) above the maker's
  name in Fraunces; centre, the colophon in apparatus type
  (who made this, of what, in what year — the real facts);
  right, the patina log (§6.9); beneath all, one line in
  12.5px apparatus: "AGE ON THIS PAGE = 0.72 × DEPTH +
  0.28 × DWELL (240s). THE PAGE DOES NOT UN-AGE." — the
  formula, printed. Legal links sit in the colophon's last
  line as ordinary text links with §6.10's scribed rules.
- **Motion spec.** The mark engraves (§6.8); the log
  appends (§6.9); nothing else in the footer moves, ever.
  The stillness is the statement: the oldest thing on the
  page is also the calmest.
- **Choreography timeline (v2).** Footer entry → §6.8's
  draw (1400ms) and §6.9's closing line print concurrently
  → t+1800ms: the plate is complete — signed, logged,
  audited.
- **State matrix (v2).** *Rest:* complete plate. *Hover /
  focus:* links per §6.10. *Scrolled-past:* n/a — it is the
  end. *Disabled:* no-JS prints the plate complete with the
  honest log line (§6.9).
- **Content merge.** Every element of the footer is the
  page's own record: its maker's real mark, its real
  colophon facts, the visitor's real measured visit, the
  real formula. A footer that could be lifted onto another
  site unchanged fails §9 on sight.
- **Failure fallback.** The static plate, complete.
- **Reduced-motion variant.** Mark inked at rest; log lines
  printed without fades.
- **Breakpoints (v2).** ≥1200px: three columns as specced.
  768–1199px: two columns (mark + colophon, log beneath).
  <768px: one column, mark centred above the colophon —
  on a phone the plate is read top to bottom like a
  plaque on a wall, which is what it is.
- **Edge cases & failure modes (v2).** *Maker with no
  hallmark artwork:* the colophon line signs in Fraunces
  type and §6.8 is omitted — a typed signature is honest;
  an invented device is a forged hallmark (§10, blocking).
  *Very long log (all four lines + updates):* the log
  column caps at the four event lines; the closing figure
  updates in place rather than appending.
- **Accessibility spec (v2).** `<footer>` landmark; all
  text real and in reading order (mark label → colophon →
  log → formula); link contrast limestone on deep 6.26:1,
  focus ring `--verdigris` at 2px offset on the deep ground.
- **Performance budget & mobile variant.** The footer's
  motion is §6.8's and §6.9's budgets; the plate itself is
  static. Mobile: the plaque variant above.
- **Tokens consumed (v2).** `--patina-deep`, `--verdigris`,
  `--limestone`, `--ink-bronze`.

### 6.16 Section title emergence (page family: headings)

- **What & why.** Section titles in this theme do not fade
  in; they *clear*. Each title's plate enters one stage
  greener than its band (§4) — the heading half-lost in
  patina, legible but weathered — and as the title crosses
  the reading line it is resolved: the plate settles to its
  true band stage and the Fraunces title comes to full
  contrast, the way a conservator's first wipe reveals an
  inscription on a green door. It belongs because it is the
  theme's reveal grammar in its purest form: nothing appears
  from nothing; things are *uncovered*.
- **Structure.** The title sits in a slim plate (no mat —
  titles are inscriptions, not specimens) whose ground is a
  `data-metal` surface with a +1 stage entry offset. The
  title text itself is always `--ink-bronze` at full opacity
  (§3 law 1) — what changes is the plate behind it, from one
  stage too green to its true stage. A 24px scribed rule
  beneath the title draws as the emergence completes.
- **Motion spec.** Trigger: title's top crosses 62%
  viewport. Emergence: the plate's local stage offset
  animates +1 → 0 over 700ms `--ease-age`, scrubbed to the
  title's travel through the 62%→45% viewport band (the
  visitor's scroll does the wiping), then the rule draws
  180ms `--ease-engrave`. If the visitor scrolls fast, the
  emergence compresses to its end state — a wiped title
  never waits for its ceremony.
- **Choreography timeline (v2).** Title top at 62%: offset
  +1, rule undrawn → travel to 45%: offset → 0, title at
  full band contrast → +180ms: rule drawn → the title
  rests, a permanent part of its band. Scrolling back up:
  no re-greening — an inscription once uncovered stays
  uncovered (ratchet, §6.2).
- **State matrix (v2).** *Rest (below band / no-JS):* title
  at its true band stage, rule drawn — the shipped state is
  the emerged state. *Emerging:* as specced. *Hover /
  focus:* none (titles are not controls). *Scrolled-past:*
  emerged, terminal. *Disabled:* reduced-motion ships
  emerged.
- **Content merge.** The patina being cleared is on the
  title's own plate; the inscription uncovered is the
  section's actual name. The reveal *is* the heading
  arriving, in the material the section is about.
- **Failure fallback.** Shipped emerged; JS only arms the
  +1 offset for titles below the fold, and the 1200ms
  watchdog (§6.2) clears any title the loop abandons.
- **Reduced-motion variant.** Emerged at rest, rule drawn.
- **Breakpoints (v2).** Identical at all sizes; below
  768px the scrub band narrows (62%→52%) so the emergence
  completes within a phone's shorter throw.
- **Edge cases & failure modes (v2).** *Title at the very
  top of a band boundary:* its entry offset is computed
  from its own plate, not the band's average — two adjacent
  titles may sit a half-stage apart mid-emergence, which
  reads as weather, not error. *Title longer than 2 lines:*
  a §3 violation caught at build; the emergence is specced
  for inscriptions, not paragraphs.
- **Accessibility spec (v2).** The title is a real heading
  at correct level, readable at every instant (the +1 stage
  ground keeps `--ink-bronze` text at ≥5.8:1 even
  mid-emergence — §2's verdigris pairing). Heading order is
  document order; the emergence is never announced.
- **Performance budget & mobile variant.** One stage-offset
  write per emerging title in the shared loop; ≤2 titles
  emerging concurrently by construction. Mobile: the
  narrowed band above.
- **Tokens consumed (v2).** `--ink-bronze`, `--bronze`,
  `--verdigris`, `--ease-age`, `--ease-engrave`.

### 6.17 Plate polish-in (page family: entrance / stagger)

- **What & why.** When a group of plates enters together —
  a row of object cards (§6.12), a gallery of specimens —
  they do not fade up as a class. Each plate is polished in
  individually: a small local polish pass (§6.1's grammar at
  plate scale) crosses its frame as it arrives, staggered
  120ms apart in reading order, so the bench fills the way a
  restorer's bench fills — one object set down and brightened
  at a time. It belongs because it makes the page's entrances
  obey the same physics as its hero: things here are handled
  into place, not rendered into view.
- **Structure.** Each plate in a group carries the §6.5
  polish layer pre-built (frame-only variant: the bright
  band travels along the frame's rim, not across the
  photograph — polishing a *photograph* would be a lie about
  what the cloth touches). An IntersectionObserver on the
  group arms the stagger; CSS transitions keyed to a
  `--polish-delay` custom property (120ms × reading index)
  run the passes — no per-plate JS timers.
- **Motion spec.** Trigger: group 25% visible. Per plate:
  rim band travels the frame's perimeter over 600ms
  `--ease-polish` (a linear gradient rotating through the
  frame's border via `border-image`-free construction: four
  rim strips, sequenced top → right → bottom → left at
  150ms each). Simultaneously the plate settles from
  translateY 6px / shadow flat to rest over 500ms
  `--ease-settle`. Total ceremony for a 4-plate group:
  600 + 3×120 = 960ms.
- **Choreography timeline (v2).** t+0: group at 25% →
  t+0–600ms: plate 1 polished and settled → t+120ms:
  plate 2 begins → t+240ms: plate 3 → t+360ms: plate 4 →
  t+960ms: group at rest, all frames at their band stages.
  Plates already >50% past centre when the group arms
  (fast scroll) skip the pass and stand settled — catch-up
  is law, not an afterthought.
- **State matrix (v2).** *Rest (shipped / no-JS):* plates
  settled at band stages, fully visible — the pre-pass
  state exists only under a JS-armed class. *Polishing:*
  as specced. *Hover / focus:* §6.5/§6.12 behaviour, which
  waits for the pass to complete (a plate being set down
  is not yet being rubbed). *Scrolled-past:* settled,
  never re-polished on re-entry. *Disabled:* reduced
  motion ships settled.
- **Content merge.** The pass travels the plate's own
  frame — the rim of the object being placed. The stagger
  order is the reading order, so the ceremony and the
  content's hierarchy are the same sequence.
- **Failure fallback.** The pre-pass state is JS-armed
  only; no JS, no IO, or a stalled loop (1200ms watchdog)
  all resolve to the settled state.
- **Reduced-motion variant.** Plates appear settled, in
  order, instantly.
- **Breakpoints (v2).** ≥1200px: stagger 120ms, rim pass
  600ms. 768–1199px: stagger 90ms. <768px: stagger 60ms,
  rim pass 450ms, settle cut (plates are stacked singly
  on a phone; a long ceremony per plate taxes a thumb).
- **Edge cases & failure modes (v2).** *Group of one:*
  the pass runs solo — a single plate still deserves its
  handling. *Group re-entering after partial scroll:* only
  un-passed plates run; the index is per-plate state, not
  per-group. *Plate with a §6.4 figure inside:* forbidden
  composition — the showcase never sits in a polish-in
  group; it has its own entrance law.
- **Accessibility spec (v2).** DOM order is reading order
  and matches the stagger; the pass is never announced;
  focus entering an un-passed plate settles it instantly.
  All plate content meets §2 contrast at rest and during
  the pass (the rim band never crosses text).
- **Performance budget & mobile variant.** Four rim strips
  per plate, composited transforms/opacity only; ≤4 plates
  passing concurrently by the stagger's construction.
  Mobile: the compressed variant above.
- **Tokens consumed (v2).** `--copper-hi`, `--ease-polish`,
  `--ease-settle`, `--dur-rim` (600ms), `--stagger-plate`
  (120ms).

### 6.18 Burnish transition + cast-plate skeleton (page family: loader / transition)

- **What & why.** The theme's two state-change rituals,
  sharing one material logic. **Leaving** a page is a
  burnish: a polish sweep (§6.1's band, widened to the
  full viewport) crosses once, 500ms, and the destination
  arrives *one stage younger* than the page just left —
  travel in this theme is a small restoration, because you
  return to the top of a new object. **Loading** shows
  cast-plate skeletons: the real plates' frames at stage 1
  with limestone interiors and apparatus rules where text
  will sit — the object as an unpolished casting, honest
  about not yet being finished.
- **Structure.** Burnish: a fixed full-viewport layer
  (`--copper-hi` gradient band, `pointer-events: none`)
  parked off-canvas; on internal navigation it sweeps
  (translateX −20% → 120%, 500ms `--ease-polish`), the
  route swaps at full coverage (~250ms), and the new page's
  surfaces initialise at `max(0, age − 0.25)` before the
  formula resumes — the one sanctioned un-ageing, declared
  in §12's voice as the traveller's rule. Skeleton: the
  real plate markup with `.is-casting` — frame at stage 1,
  interior limestone, text as `--bronze`-ruled bars at true
  line-heights; content replaces children in place, the
  plate never resizes.
- **Motion spec.** Burnish: 500ms total; it enhances
  interceptable internal links only (modified clicks,
  new-tab, external links bypass entirely). Skeleton
  resolve: as content lands, the casting's frame warms
  stage 1 → its band stage over 400ms `--ease-age` while
  the interior crossfades to the real content (240ms).
  Hard cap: any plate still casting at 1400ms has its
  frame stripped to plain limestone with an apparatus note
  ("THIS PLATE IS STILL IN THE FOUNDRY.") — no object may
  stay a promise if the machinery fails.
- **Choreography timeline (v2).** Burnish: t+0 link
  activated → t+0–250ms band covers → t+250ms route swap,
  new page at scroll top, one stage younger → t+500ms band
  exits → t+580ms watchdog: any burnish not completed is
  torn down and the destination stands plainly. Skeleton:
  per plate, resolve per above; the 1400ms cap is absolute.
- **State matrix (v2).** *Rest:* no layer; pages stand at
  their formula stages. *Burnishing:* pointer locked out
  for 500ms. *Casting:* skeleton per above. *Hover /
  focus:* links show §6.10's rule; keyboard activation
  fires the same burnish, focus landing on the
  destination's `<h1>` at band exit. *Disabled / no-JS:*
  plain navigation; skeletons are never rendered in a
  state the server cannot resolve.
- **Content merge.** The burnish band is the page's own
  polish, widened; the skeleton is the plate's own
  unpolished casting at its true geometry — layout shift
  is zero by construction.
- **Failure fallback.** A slow destination (>3s under the
  band): the band retreats (200ms) and native loading
  proceeds — the theme never traps a visitor inside a
  transition. A fetch error resolves the casting into
  §11's flaw-mark alert in §12's error voice.
- **Reduced-motion variant.** No sweep: instant navigation
  with a 120ms stage flash on the header plate (one stop
  brighter, then back) to mark the change of object.
  Skeletons are plain limestone blocks; content fades at
  120ms or appears.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px:
  burnish 450ms. <768px: burnish 380ms, skeleton text bars
  reduce to two per plate.
- **Edge cases & failure modes (v2).** *Same-page anchors:*
  no burnish — anchors scroll per §5's glide. *Back/forward:*
  no burnish; the browser's gesture rules, and the
  destination's age is its own formula's, not decremented.
  *Prefetch on hover:* permitted; the burnish still runs
  its full 500ms — the ritual is the point, not the wait.
- **Accessibility spec (v2).** During a burnish the
  outgoing page is `inert` from t+0; at band exit focus
  moves to the destination `<h1>` (tabindex −1) with a
  polite announcement "Taken to: [page name]" — SPA focus
  law in the theme's grammar. Casting plates carry
  `aria-busy="true"` until resolved.
- **Performance budget & mobile variant.** One transform
  on one fixed layer; skeletons are CSS only. Mobile: the
  compressed variant above.
- **Tokens consumed (v2).** `--copper-hi`, `--stage-1`,
  `--bronze`, `--ease-polish`, `--ease-age`,
  `--dur-burnish` (500ms), `--fallback-cast` (1400ms).

## 7. Page application map

**Home — the full arc.** The one page type that must run
the complete ageing: bright threshold (§6.11), polish pass
(§6.1), patination (§6.2) through five bands, the showcase
(§6.4) in band 3, the specimen (§6.7) in band 4, assay
counters (§6.14) wherever the publisher's figures belong,
and the engraved footer (§6.15). A Verdigris home page that
does not reach stage 4 by its footer has not made its
argument.

**Listing (objects, case studies, restorations).** The arc
compresses: the page opens at stage 1 (a listing is a bench
already in use, not a christening) and the cards (§6.12)
descend the bands as the list descends. Filters, where
they exist, are §11's plate-leaves, and filtering
re-polishes the surviving cards (§6.17 at half duration) —
the bench is re-laid, not re-rendered.

**Detail (one object).** The arc inverts its emphasis: the
object's own page opens at *its* stage — an old object's
page opens deep and the polish is in the photography
(before/after per §6.4's static variant); a new object's
page opens bright and ages only to stage 2 — the detail
page's depth is one object's life, not the whole foundry's.

**About / the maker.** The tenure page: assay counters
(§6.14) are its hero, the maker's portrait sits in a frame
at the stage their years have earned (computed from the
founding year against the formula, and the caption says
so), and the commission form (§6.13) closes it.

**Contact / commission.** §6.13's plate is the page; the
arc is minimal (stages 1–2) because a visitor with an
object in hand should not have to descend a whole foundry
to ask for help.

**404 — the uncast page.** A plate that was never poured:
limestone ground, a stage-0 frame outline with nothing in
it, the requested path stamped in apparatus as the flaw
record ("NO CASTING EXISTS AT THIS ADDRESS."), and
§6.10's index offered as the way back to the bench. One
motion only: the frame outline draws once (§6.8's
engrave, 900ms) — an empty frame being marked out, then
stillness.

## 8. Worked examples

### 8.1 The hero — a foundry's threshold

*The commission: a bronze foundry's home page; the flagship
object is a harbour bell cast in 1962, restored by the
foundry in 2024.*

- **The composition (§6.11).** First screen: header plate
  with §6.10's tabs (WORKSHOP bright, RESTORATIONS bronzed,
  THE BENCH verdigris, COMMISSION deep — the arc legible in
  the menu). The hero plate: the bell's photograph, frame
  3px `--copper`, mat 24px. Headline plate overlapping the
  rim: "CAST TO BE KEPT." Standfirst, Fraunces italic: "The
  bell from St. Cuthbert's pier, home again." One bright
  action: "COMMISSION THE WORKSHOP".
- **The opening (§6.1).** Fonts settle; at t+120ms the
  polish band enters the headline plate; by t+770ms the
  first half of the title has peaked bright; at t+1420ms
  the sweep is done and the overlay is gone. Nothing else
  has moved. The second section's first frame shows at the
  fold, stage 1 at its top edge.
- **Scroll timeline.** 0–15% depth: the foundry's story,
  plates warming to stage 1–2; the strip's front a tenth
  down the rail. 40%: the assay plate (§6.14) counts —
  YEARS AT THE BENCH to 63 (from 60% floor, 1200ms),
  OBJECTS RESTORED to its ledger figure, source lines
  beneath both. 55–75%: the bell's own showcase (§6.4)
  pins; the visitor restores it by descending. 90%: the
  untreated specimen (§6.7) is mid-bloom in its corner.
  100%: the plate footer — mark engraving, log printing
  "YOUR VISIT AGED THIS PAGE BY 0.41 YEARS.", formula
  beneath. The visitor has read a page and aged an object,
  and both records agree.

### 8.2 Mid-page — the restoration showcase

*The commission: §8.1's bell, mid-page, in its working
margin.*

- **Entry.** The section title "THE BELL, RESTORED"
  emerges (§6.16) as it crosses 62% — its plate clearing
  from verdigris-dark to its band-3 stage, rule drawing
  beneath. The margin apparatus reads "STAGE III —
  VERDIGRIS" as the visitor arrives.
- **The pin (§6.4).** The plate sticks; the as-found bell
  (green-crusted, harbour-worn) holds for the pin's first
  7.5%. The blend begins along the bell's own highlight
  direction (declared in the build: from the crown down).
  At pin 50% the readout counts "RESTORATION 50%" and the
  margin caption's second line becomes readable in the
  reading order: "Forty-one hours at the bench. The
  inscription was under the crust." At 93% the bell stands
  polished; at pin end the caption's last line — "Returned
  to the pier, October." — has been on screen since 80%.
- **What the visitor feels.** They did the work. Their
  scroll was the cloth; the object brightened under their
  descent at the pace they chose, and the record of the
  treatment was waiting in the margin like paperwork
  beside a bench. Scrolling back up un-restores it — the
  one place the page lets time run backwards, because a
  demonstration is not a life.

### 8.3 Conversion — the commission plate

*The commission: §8.1's foundry; a visitor with a green
garden gate to restore.*

- **Arrival.** The form plate (§6.13) sits in band 4 —
  the deepest part of the page, where decisions are made.
  Its frame is verdigris-deep; its fields are ruled lines
  on limestone. The radio plates read MAKE / RESTORE /
  VALUE.
- **Interaction timeline.** The visitor tabs to YOUR
  NAME: the rule inks to `--copper` over 220ms, a small
  disc opens at the rule's start. They choose RESTORE:
  the plate polishes in 240ms, its disc pinned. They type
  the gate's story in the ruled textarea. They mistype
  their direction (no @): on submit, their thumbprint
  stamps the button (the press happened), then the
  direction field's rule darkens and the clerk notes
  beneath, in apparatus: "THE DIRECTION WILL NOT CARRY —
  CHECK THE ADDRESS." Focus lands on the field at
  t+380ms. They fix it; the note clears, the rule returns
  to copper.
- **The hallmarking.** Second submit: print, press, send.
  On response the hallmark stamps beside the heading
  (160ms) and the plate's contents exchange for the
  acknowledgement letter: "Your commission is on the
  bench. We will write within two working days." —
  reference "COMMISSION Nº 118" (the server's number),
  and beneath, in italic: "The gate will come home
  brighter than it left. They usually do."
- **Failure rehearsed.** If the send fails, the letter
  stays written on the plate, word for word; the clerk
  notes "NOT SENT — THE COURIER FAILED. YOUR COMMISSION
  IS KEPT BELOW." and the button un-presses. The visitor
  never re-writes a commission because a network blinked
  (§10, blocking gate 7).

## 9. Anti-slop — what makes THIS theme look cheap

1. **The green filter.** A CSS hue-rotate or a green overlay
   slapped over a normal site, deepening with scroll. *Cure:*
   the five declared stage stops (§2), interpolated per
   surface by the one formula (§5), with texture arriving at
   stage 2 — oxidation is per-object chemistry, not a colour
   grade on the whole viewport.
2. **Text that ages.** Body copy tinting green "for mood",
   contrast quietly dying by the footer. *Cure:* §3 law 1 —
   text is `--ink-bronze` at every stage; §10 samples
   contrast at five depths and blocks below AA.
3. **The fake antique.** Sepia photographs, distressed-paper
   backgrounds and "EST. 1892" for a firm founded in 2019.
   *Cure:* the one law (§1) — every year, alloy and count is
   the publisher's real figure with its source line (§6.14),
   or it is absent.
4. **Patina as wallpaper.** A mottled green background behind
   unrelated content, ageing nothing in particular. *Cure:*
   §6.2's content-merge — the surfaces that green are the
   content's own frames and rules; there is no background
   patina layer anywhere in the theme.
5. **The un-ageing scroll.** Patina that reverses when the
   visitor scrolls up, yo-yoing green-brown-green. *Cure:*
   the ratchet (§6.2), with exactly two lawful reversals —
   the hand (§6.5) and the demonstration (§6.4) — each local
   and visibly caused.
6. **Hover sparkle.** Generic shine sweeps on every card,
   looping glints, a cursor trail of polish. *Cure:* §6.5's
   disc is pointer-held, single, and re-forms over 6s; the
   cursor is the normal system cursor, always (§ standing
   rules); nothing glints that a hand is not touching.
7. **The lying log.** A patina log whose years are scripted
   theatre ("0.03 years" hard-coded for every visitor).
   *Cure:* §6.9 computes from measured dwell and depth,
   pauses when the tab hides, caps at 1.00, and prints its
   conversion in §12 and its formula in the footer (§6.15).
8. **Uniform card grids.** Twelve identical plates in a
   3-across matrix, stages randomised for variety. *Cure:*
   §4's density law and §6.12's mixed spans; a card's stage
   is its band, never a dice roll.
9. **Metal type.** Gradient-clipped "chrome" headline text,
   bevelled buttons, embossed everything. *Cure:* §3 law 2
   — display is solid and engraved; the only gradient that
   ever touches type is §6.1's travelling light, for 1300ms,
   once.
10. **The instant antique footer.** A page that stays bright
    for 90% of its length and jumps to deep green at the
    footer for drama. *Cure:* the formula is continuous and
    the bands are composition (§4); §10's stage audit samples
    five depths and requires the arc to be monotone.
11. **Restoration by blur.** Before/after done as a
    blur-to-sharp or a generic dissolve between two
    unrelated photos. *Cure:* §6.4 — pixel-registered
    renditions of the *same* object, opacity and stage only,
    alignment checked at the gate.
12. **The costume commission.** A generic contact form with
    copper-coloured submit button calling itself themed.
    *Cure:* §6.13 entire — radio plates for the real three
    services, the hallmarking success, the kept-letter
    failure law.

## 10. Quality gate

**Blocking (any failure stops the build).**

1. **Formula audit.** Sample `--age` and five surfaces'
   stages at scroll depths 0 / 25 / 50 / 75 / 100%: stages
   are monotone non-decreasing with depth, match §5's
   formula within ±0.03, and no surface sits at a stage its
   position has not reached.
2. **Contrast at depth.** Body text contrast ≥4.5:1 sampled
   at the same five depths, in both colour schemes; display
   pairings match §2's table exactly (no verdigris text on
   limestone anywhere, at any stage).
3. **Assay audit.** Every figure in §6.14 and every year,
   alloy or count anywhere on the page traces to a
   publisher-supplied source; each carries its source line.
   One unsourced figure fails the build.
4. **Log truth test.** With a scripted 60s attended visit to
   50% depth, the patina log's figure matches §6.9's
   computation within rounding; with the tab hidden for the
   full 60s, the figure is ~0.
5. **Registration test.** §6.4's two renditions overlay with
   zero perceptible offset at 200% zoom on the object's
   three sharpest edges.
6. **Ratchet test.** Scroll down 60%, up 30%, down 10%: no
   surface's stage decreases except inside §6.5's disc or
   §6.4's pin.
7. **Kept-letter test.** Force a network failure on §6.13's
   submit: the visitor's text survives intact, the clerk's
   note appears, and the button is pressable again.
8. **JS-off test.** With JavaScript disabled, the page is
   complete: surfaces at markup stages, showcase stacked,
   counters at final values, log printing its honest line,
   form submittable.

**Standard (must pass before ship).**

9. Reduced-motion: the whole page sits at `--stage-mid`,
   every element in its specced static variant, nothing
   scrubbed, nothing counting.
10. The polish pass (§6.1) fires exactly once, and the
    headline is readable at full contrast before, during
    and after it.
11. §6.5's disc never exceeds one per surface, never
    spills past a small surface's clamp, and focus parity
    works with keyboard only.
12. The bloom (§6.7) is the page's only ambient loop, and
    it pauses off-screen and on hidden tabs.
13. Performance: §14's budgets met on a mid-range Android
    over 4G; the shared loop stays ≤1.6ms/frame with all
    systems live.
14. The five-second test: a first-time visitor, shown the
    top and then the footer, can say what the site makes
    and that the page aged as they read it. (Human-checked;
    the one gate no script can pass for you.)

## 11. Component inventory

Every component a real Verdigris site needs, with its
themed treatment. Refusals are part of the inventory: each
names its in-theme replacement.

- **Buttons (primary).** Cast plates at the page's current
  stage, apparatus capitals, §6.6 thumbprint on press,
  §6.5 disc on hover/focus. One primary per plate.
- **Buttons (secondary).** Scribed-rule text links (§6.10's
  grammar): no box, the rule draws on hover/focus.
- **Inputs / textarea.** Ruled lines per §6.13; labels in
  apparatus above; hints as described-by text, never
  placeholders.
- **Radio / checkbox.** Radio plates (§6.13) and the
  hallmark-square checkbox; native inputs visually
  re-skinned, never replaced — semantics and keyboard
  behaviour are the platform's.
- **Select.** *Refused.* A native dropdown is a plastic
  object on the bench; option sets are radio plates
  (≤5 options) or a §6.12-style list of nameplate links
  (>5). Where a platform forces a select (country lists),
  it is styled as a ruled line and forgiven in §10's notes.
- **Tables (assay / specification).** Apparatus header row
  scribed top and bottom, tabular figures, stage-coloured
  row rules that age with the page like everything else;
  the source line (§6.14) as the table's mandatory footer
  row.
- **Cards.** Object cards (§6.12).
- **Badges.** *Refused as pills.* Status is a stamped
  apparatus line on the object itself ("WITHDRAWN — IN
  THE WORKSHOP", §6.12) — clerks stamp objects; they do
  not pin badges on them.
- **Alerts.** The flaw mark: a slim plate at stage colour,
  dark-stamped apparatus text (§6.13's error grammar),
  persistent until resolved. Never auto-dismissing.
- **Modal.** *Refused.* Nothing in a workshop pops over
  the bench. Detail goes on a detail page (§7) reached by
  the burnish (§6.18); the one overlay the theme permits
  is §6.4's margin caption, which is layout, not a modal.
- **Toast.** *Refused.* Confirmations are letters (§6.13's
  acknowledgement) or log lines (§6.9) — records, not
  notifications that evaporate.
- **Tabs.** Plate-leaves: §6.10's stage-fixed tabs used
  in-page; switching leaves re-polishes the incoming
  leaf's frame (§6.17 at half duration).
- **Accordion.** The drawer of plates: sections stacked as
  plates whose frames polish (§6.17) as each opens; one
  open at a time in apparatus contexts (ledgers, care
  instructions), many in reading contexts.
- **Pagination.** Plate-leaves: "LEAF 2 OF 5" in apparatus
  with scribed-rule links — the listing is a sheaf of
  plates, turned, not a numbered strip of buttons.
- **Progress bar.** *Refused* — replaced by the margin
  strip (§6.3), the theme's own metal as gauge.
- **Spinner.** *Refused* — replaced by the cast-plate
  skeleton (§6.18); metal does not spin to say "wait".
- **Tooltip.** *Refused.* Explanation lives in the working
  margin (§4) or a caption; a floating hint is chrome from
  another world.
- **Search.** An index plate: a ruled input (§6.13's
  grammar) over §6.12 nameplate results; the query is
  "entered in the index", results are objects found on the
  bench.
- **Breadcrumbs.** The assay trail: apparatus lines naming
  the path as provenance ("BENCH → RESTORATIONS → THE
  BELL") — where an object has been, not where a user
  clicked.
- **Footer.** The engraved plate (§6.15).
- **404 / empty states.** The uncast page (§7); empty
  listings show an empty bench — a limestone plate with
  the clerk's line "NOTHING ON THE BENCH answers to that
  name." and the index offered.
- **Focus ring (all components).** 2px `--copper` outline,
  2px offset, on light grounds; `--verdigris` on the deep
  footer. Never the stage colour of the moment — focus
  must be findable in any year of the page's life.

## 12. Content & copywriting voice

Two voices share the page, and they never swap lines.

**The Conservator speaks** (Fraunces, sentence case, italic
for captions) — the human who handles the objects. Warm,
specific, unhurried; speaks of objects by name and of time
in years. Headlines are statements about the object, not
the brand: ✓ "Cast to be kept." ✗ "Timeless Elegance
Redefined." Captions carry facts a hand would know:
✓ "Forty-one hours at the bench. The inscription was under
the crust." ✗ "Lovingly restored to perfection!"

**The Clerk stamps** (Archivo Narrow apparatus, tracked
capitals) — the bench's paperwork: labels, stage readings,
log lines, errors. Terse, factual, never apologetic in the
corporate manner. ✓ "STAGE III — VERDIGRIS." ✓ "THE
DIRECTION WILL NOT CARRY — CHECK THE ADDRESS." ✗ "Oops!
That email looks a bit off."

**Fixed strings (verbatim, do not paraphrase).**

- The traveller's rule: "THE PAGE DOES NOT UN-AGE."
- The formula line (§6.15): "AGE ON THIS PAGE = 0.72 ×
  DEPTH + 0.28 × DWELL (240s)."
- The log's conversion: "ONE PAGE-YEAR = 240 SECONDS OF
  ATTENDED READING AT FULL DEPTH, PRO-RATED."
- No-JS log line (§6.9): "PATINA LOG — KEPT BY HAND IN THE
  WORKSHOP; THIS PRINTED COPY RECORDS NO VISIT."
- Kept-letter line (§6.13): "NOT SENT — THE COURIER
  FAILED. YOUR COMMISSION IS KEPT BELOW."
- Empty bench (§11): "NOTHING ON THE BENCH answers to
  that name."

**Error voice.** Errors are flaw marks: they name the
flaw and the remedy, in the clerk's capitals, without
blame and without cuteness. ✓ "THE OBJECT'S STORY IS
EMPTY — THE WORKSHOP NEEDS SOMETHING TO WORK FROM."
✗ "This field is required."

**Empty-state voice.** The bench is empty, plainly:
what was looked for, that it is not here, and where the
index lives. Never a mascot, never a pun about rust.

**Confirmation voice.** A letter, not a toast (§6.13):
the conservator acknowledges, the clerk references.
✓ "Your commission is on the bench. COMMISSION Nº 118."
✗ "Awesome! We've received your request 🎉" — the emoji
alone would fail this section.

**Banned words.** *Timeless* (the theme's whole point is
time), *vintage-inspired*, *rustic charm*, *shiny new*,
*cutting-edge*, *disruptive*, exclamation marks in the
clerk's voice, and any founding year the ledger cannot
produce.

**Owned words.** *Cast, kept, assayed, at the bench,
as found, returned, handled, weathered, bright, deep* —
and *verdigris* itself, used precisely: it is a stage
(§2), not a synonym for "greenish".

## 13. Full-page scroll choreography map

The home page (§7), top to footer. Age values are §5's
formula at typical reading pace.

| Beat | Depth / age | What the visitor sees and feels |
|---|---|---|
| 1 | 0% / 0.00 | The bright threshold (§6.11): the flagship object at stage 0, the nav already showing the whole arc in its tabs |
| 2 | 0% / 0.00 | §6.1's polish pass crosses the headline — the page's brightest moment, once |
| 3 | 5% / 0.05 | First scroll: the glide (lerp 0.09) makes the page feel cast; the strip's front leaves the rail's head |
| 4 | 15% / 0.14 | Stage I: frames warm; the hero's own frame has begun — the visitor notices the top is no longer quite as bright as memory says |
| 5 | 30% / 0.27 | Stage II: bronze rules and frames; parallax still live in the upper strata; §6.17 polish-ins set the story plates down one by one |
| 6 | 40% / 0.36 | The assay plate (§6.14) counts its figures with their source lines — the page states its credentials in numbers |
| 7 | 55% / 0.50 | Stage III boundary: the margin apparatus flips to "STAGE III — VERDIGRIS"; parallax stills; the green is now the page's dominant metal |
| 8 | 55–75% / 0.50–0.68 | The showcase pin (§6.4): the visitor restores the object by descending; the margin keeps the treatment record |
| 9 | 80% / 0.74 | The specimen (§6.7) mid-bloom in its corner; §6.12 cards at deep stages; the commission plate (§6.13) waits in band 4 |
| 10 | 92% / 0.86 | Stage IV approaches: grounds deepen, limestone lettering takes over from ink on the late plates |
| 11 | 100% / 1.00 | The engraved plate (§6.15): the mark draws and inks, the log prints the visit's years, the formula sits beneath — the page, fully aged, signs itself |

**Reverse pass.** Scrolling back up: stages hold (ratchet,
§6.2); discs re-form where hands left them (§6.5); the
showcase alone un-restores inside its pin (§6.4). The
visitor returns up a page that remembers being read —
which is the theme's whole argument, felt rather than
stated.

**Jump-scroll catch-up.** Anchor jumps snap every surface
to its landed stage in one frame (§6.2); titles land
emerged (§6.16), counters at final values (§6.14), the
mark inked (§6.8). No catch-up ceremonies: chemistry does
not perform for teleporting visitors.

## 14. Whole-page performance budget

- **Assets.** Total page weight ≤780KB: hero image ≤220KB
  (§6.11), showcase renditions ≤380KB the pair (§6.4),
  card images ≤90KB each and lazy, the mottle texture is
  one inline SVG tile (~3KB) reused everywhere, fonts are
  the two families subset (Fraunces optical + Archivo
  Narrow, ≤120KB combined). No image may be a photograph of
  generic metal used as texture — weight spent on wallpaper
  is weight stolen from the objects.
- **Frame budget.** The shared loop (age, strip, parallax,
  discs, bloom, showcase — one rAF, lerp per system) ≤1.6ms
  script per frame on a mid-range Android; compositor-only
  properties for every moving layer (transform, opacity,
  clip-path, mask position); no layout writes in the loop.
- **Long tasks.** None >50ms after load; the polish pass
  and engraving are CSS/SMIL-free declarative animations
  armed by class, not JS-driven frame work.
- **Cut order (when the budget is exceeded).** 1) The bloom
  (§6.7) stills at its shipped 55%. 2) Upper-half parallax
  (§5) flattens. 3) Mottle texture drops from frames
  (flat stage colours remain — the arc survives). 4)
  §6.17's rim passes shorten to settles. 5) §6.5's disc
  radius halves. **Never cut:** the patination itself
  (§6.2), the strip (§6.3), the ratchet, any fallback, any
  text contrast. A Verdigris page that cannot afford its
  ageing is not a Verdigris page.
- **Low-power rule.** If the loop measures sustained
  <40fps for 3s, cuts 1–3 apply automatically and the page
  notes it in the log ("KEPT AT A SLOWER FIRE — THIS
  DEVICE.") — the record stays honest even about its own
  machinery.

## 15. Build-order checklist

1. Static aged page first: all surfaces at markup stages,
   showcase stacked, counters final, log's honest line —
   the complete no-JS object (§10 gate 8 must pass before
   any motion exists).
2. Tokens and type: §2's table (with the dark ruling),
   §3's scale and laws; verify no text role consumes a
   stage colour.
3. Layout: plates, margin strip geometry, working margin,
   bands (§4) — with the stage audit's sampling points
   marked in the DOM.
4. The age formula and shared loop (§5), ratchet included;
   wire §6.2 and §6.3; pass gate 1 and gate 6.
5. Headings and entrances: §6.16 emergence, §6.17
   polish-ins, §6.1 polish pass (once-only logic and the
   fonts watchdog).
6. The hand: §6.5 re-polish (with focus parity), §6.6
   thumbprint; mask-support detection before arming.
7. The showcase (§6.4): registration checked at 200% zoom
   before the pin is wired (gate 5).
8. Data and records: §6.14 counters (aria-hidden replay
   layer), §6.9 log with attended-time clock, §6.8 mark,
   §6.15 footer with the printed formula.
9. The commission form (§6.13) with the kept-letter
   failure rehearsed (gate 7) and the hallmarking success.
10. Navigation (§6.10) and transitions (§6.18): burnish,
    skeletons, the 1400ms casting cap.
11. The specimen (§6.7) last of the elements — ambient
    motion is fitted around a finished page, never before.
12. Reduced-motion pass: the whole page at `--stage-mid`,
    every element in its specced variant (§10 gate 9).
13. Dark-scheme pass: the foundry at night (§2), all
    pairings re-measured.
14. Full gate (§10): formula, contrast, assay, log truth,
    registration, ratchet, kept-letter, JS-off — in that
    order, signed by someone who did not build the page.
