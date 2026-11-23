# 58. Storm Glass — Expanded (v1 + v2)

**Identity (preserved from the original entry, deepened — never
redesigned).** The Victorian storm glass: a sealed tube of camphor
solution whose crystals grow feathery in fair weather's opposite
and dissolve as pressure rises — Admiral FitzRoy's instrument,
beautiful, temperamental, and only loosely connected to the
weather it claims to read. The site is an instrument maker's
cabinet: brass, glass and mahogany; crystals that grow and
dissolve as the page's weather changes. Palette anchors:
instrument card `#EFE8D8`, brass `#8C6A2F`, mahogany `#4A3A22`,
crystal haze `#A9B8B0`, storm coming `#22303A`. Type: Libre
Caslon Text (display) + IBM Plex Mono (readings and labels).
Sections are forecast states — Clear → Changeable → Storm — and
a brass needle in the margin tracks the page's barometric
pressure as the reader descends.

## 1. Concept & world

Storm Glass is the website of a maker of beautiful, doubtful
instruments. Its central object is a sealed glass tube of
camphor, alcohol and salts, in which crystals feather, fern and
dissolve in patterns that Victorian sailors swore foretold the
weather. The science is unkind — the crystals answer temperature
more than pressure — and the theme does not hide this: the
maker's honesty about his instrument is the brand. The page is
his cabinet. Every section sits inside a glass panel over an
engraved card; brass plates carry the labels; mahogany carries
everything. As the visitor descends, the weather worsens on
schedule: the first panels are Clear, their solution dissolved
and bright; the middle panels grow wisps and turn Changeable;
the last chapter is Storm — crystals dense, light low, pressure
fallen — and at its pinned climax the whole instrument gives one
small shake, the rumble, the only violence on the page.

The world the page performs is a workshop-cabinet in a port town,
kept by a maker who engraves his own plates, mixes his own
solution, and prints his doubts on the label. Nothing here is a
metaphor laid over the content: the products are forecast by the
instrument because the instrument is the product line — storm
glasses, barometers, thermometers, ships' sets. The page's
progress indicator is the maker's barometer needle. Its ambient
life is the crystal cycle in whichever panel you are reading.
Its click feedback is a tap on the glass, which — as any
Victorian keeper knew — disturbs the solution and starts a
crystal growing. The visitor is not browsing a catalogue; they
are standing at the cabinet while the weather comes in.

**The theme's one law: one pressure, printed four ways.** The
page declares a single barometric function, `pressureAt(p)`,
mapping the reader's position on the page's weather track to a
reading in inches of mercury: **30.42 in at the top, falling to
28.61 in at the end of the storm chapter's pin**. Four things on
the page are printings of that one function and may never
disagree: (1) the margin needle's angle (§6.4), (2) the printed
pressure reading wherever it appears (§6.13), (3) the crystal
density inside every panel, computed as `branches =
clamp(round((30.55 − P) × 13.5), 0, 30)` (§6.2), and (4) the
state word — FAIR at P ≥ 30.20, CHANGE at 29.80–30.19, RAIN at
29.20–29.79, STORM below 29.20, FitzRoy's own scale words. A
panel dense with crystals under a needle that reads Fair is not
a styling choice; it is the instrument contradicting itself, and
it is a blocking gate failure (§10). The corollary is the glass
law: **crystals live behind glass, words live on the card.**
Crystal growth happens inside the panel's solution layer, in the
panel's margins and around its headline — never across body
text, never beneath a paragraph at less than the §2 contrast
floor. Every forecast state is a background treatment of the
panel; the engraved card laid on top of it carries the copy at
checked contrast in all three states. A crystal that crosses a
line of text is a crack in the instrument, and the gate counts
them.

**Best-fit sites and audiences.** Makers and sellers of storm
glasses, barometers and heritage scientific instruments;
maritime and nautical gift shops with a serious streak;
restorers of antique instruments; a chandlery that sells brass
and means it; museum shops attached to science or maritime
collections; a weather-heritage or FitzRoy exhibition microsite;
makers of ships-in-bottles, sextants, chronometers — any trade
where the object is brass, glass, patience and a claim the maker
is honest enough to qualify. The audience is unhurried and
literate in objects: people who read a maker's plate, who
understand that an instrument can be treasured without being
trusted, who will reach the storm chapter because the descent
was the point. Conversion in this world is a commission, an
order for a named instrument, or a visit to the workshop — acts
taken slowly, in writing.

**When NOT to use it.** Not for an actual forecasting service:
a page that sells real weather data inside a fiction of falling
pressure teaches the visitor to distrust the numbers, and §12's
voice rules exist precisely to keep the theatre and the data
apart — a meteorological product needs a plainer theme. Not for
fast commerce: the descent is the design, and a visitor in a
hurry is being rained on. Not for dashboards or dense data —
crystal layers and haze are enemies of tabular scanning, and
§11 refuses the data table rather than frost it. Not for
children's products (the register is a Victorian workshop:
camphor, alcohol, and a storm). Not where the client cannot
supply real instrument photography or drawn plates: the framed
plates (§6.17) carry the cabinet's credibility, and stock photos
of generic "science" break it on sight. And not for any maker
unwilling to print the disclaimer — "The glass is often wrong.
It is never dull." is load-bearing (§6.14); a storm glass sold
as a reliable forecast is a lie this theme refuses to typeset.

## 2. Palette

Five anchors from the original entry, a closed list of derived
tokens, and measured contrasts computed for this expansion.
Ratios are WCAG relative-luminance figures against the stated
ground.

| Token | Hex | Role | Share |
|---|---|---|---|
| `--card` | `#EFE8D8` | Instrument card — the engraved card inside every panel; the page's reading surface | ~55% |
| `--brass` | `#8C6A2F` | Brass — plates, needle, frames, rules; the maker's metal | ~12% |
| `--mahogany` | `#4A3A22` | Mahogany — the cabinet ground behind and between panels | ~20% |
| `--haze` | `#A9B8B0` | Crystal haze — the solution's pale green-grey; atmosphere, wisps, glass tint | ~8% |
| `--storm` | `#22303A` | Storm coming — the dark blue-grey of the last chapter; also the ink on card | ~5% |

**Derived tokens (closed list — no others may be coined).**
`--brass-deep #6E5223`, the only brass licensed for text on
card; `--brass-bright #C49A4A`, the polish highlight, graphical
only; `--card-deep #E2D7BE`, card shading at panel edges and
under plates; `--mahogany-deep #38291A`, cabinet shadow and the
footer's ground; `--haze-deep #7E938A`, crystal strokes at full
growth (the wisps' darkest licensed tone); `--storm-soft
#3D4F5C`, secondary ink on card for captions and apparatus.

**Measured contrast (computed for this expansion).**
`--storm` on `--card`: **11.08:1** — the body-text pairing,
passes at every size. `--card` on `--mahogany`: **8.96:1** —
plate reversals and footer text pass. `--brass-deep` on
`--card`: **5.94:1** — labels, readings' captions and small
apparatus in brass-deep pass at ≥13px. `--brass` on `--card`:
**4.08:1** — display and graphical use only; brass anchor never
sets text below 20px. `--brass-bright` on `--mahogany`:
**4.20:1** — large display and shine only. `--haze` on
`--card`: **1.69:1** — never text, never a rule that must be
seen; haze is weather, not information. `--haze` on `--storm`:
**6.55:1** — in the storm chapter, crystal strokes and the
state word may be set in haze over storm ground. `--storm-soft`
on `--card` measures 6.96:1 by the same computation and is the
caption voice.

**State shading.** The three forecast states shade the *panel*,
never the card: Clear panels sit at full card brightness with
the solution dissolved (haze at 0–6% behind the card); Change
panels dim their glass surround by 8% and carry haze at 12–20%;
Storm panels dim the surround by 22%, the mahogany behind them
deepens toward `--mahogany-deep`, and the card itself stays
`--card` — the copy's ground never darkens, which is what makes
the glass law (§1) affordable. Text contrast is therefore
identical in all three states, and §10 audits it in the storm
state, not the fair one.

**Dark-mode behaviour.** There is no inverted scheme. The
cabinet after hours is the storm state held: `prefers-color-
scheme: dark` deepens panel surrounds to `--mahogany-deep`,
holds every card at `--card`, and stills the living cycle
(§6.5) — the instruments rest in the dark, they do not glow.
The print stylesheet is the cabinet on paper: mahogany and
storm print as card, crystals print as their final grown state
in haze-deep hairlines, the needle prints at the reading of the
page's foot.

## 3. Typography

Two faces, kept apart as strictly as their jobs. **Libre Caslon
Text** is the maker's hand — display, headings, the state words,
anything engraved on a plate. **IBM Plex Mono** is the record —
readings, labels, captions, prices, form apparatus: everything
that claims to be a measurement is set in the mono, because a
reading is a number before it is a sentence.

**Type scale (desktop ≥1200px; tablet and mobile in §6
breakpoints).** Display 54px Caslon / 1.08 / −0.01em. H2 (plate
titles) 34px Caslon / 1.15. H3 22px Caslon / 1.25. Body 17px
Caslon / 1.62 — Caslon carries the long copy; the maker's prose
is prose. Readings 15px Plex Mono / 1.5, tabular figures always
(Plex Mono is monospace by construction; the law is that no
reading may ever be set in a proportional face where digits
could swim). Labels and apparatus 12.5px Plex Mono, uppercase,
+0.14em tracking — the engraved-label voice. Captions 13px Plex
Mono in `--storm-soft`. The state words (FAIR / CHANGE / RAIN /
STORM) are set 12.5px Plex Mono letterspaced on the gauge, and
34px Caslon small-caps at a chapter's head — the same word in
both registers, the instrument's and the maker's.

**Five type laws.**
1. **Readings are mono, stories are Caslon.** A pressure, a
   price, a count, a date of making — mono. A claim, a history,
   an apology — Caslon. A number found in Caslon is a defect
   (§9 failure 6).
2. **The headline lives in the glass.** The hero headline is set
   inside the hero panel's solution (§6.1); its letters are the
   crystals' trellis. It is never set over a photograph or on
   bare mahogany.
3. **Engraving is hairline first.** Every plate label exists in
   two weights — the etched hairline and the filled weight
   (§6.6) — and the filled weight is the printed state; no label
   may ship hairline-only.
4. **No italics in the record.** Plex Mono apparatus never
   italicises; emphasis in a reading is weight or position.
   Caslon italics are licensed for the maker's asides and the
   disclaimer only.
5. **Figures never round silently.** A printed pressure carries
   two decimals (30.42 in) everywhere it prints — needle scale,
   counters, footer record. A rounded pressure ("about 29
   inches") may appear only in Caslon prose, never in a reading.

## 4. Layout language

**The cabinet.** The page is a mahogany cabinet wall. Content
lives in **panels**: a glass surround (haze-tinted, reflection
layer §6.10) over an engraved `--card` inset by 14px on desktop,
10px on mobile. Panels are separated by mahogany rails of 72px
(desktop) in which the brass plates (§6.6) sit. The cabinet is
never full-bleed: a mahogany margin of at least 24px frames the
wall at every breakpoint, because a cabinet has edges and a
webpage pretending otherwise is a poster, not an instrument.

**Grid and measure.** Panel interiors run a 12-column grid at
≥1200px with a reading measure of 62ch for Caslon body; the
maker's sections centre the card column at 760px with the
instrument figures (the glass, the scale, the plates) in the
flanking columns. The margin rail at the right (128px at
≥1200px) is reserved for the barometer (§6.4) and nothing else —
no share buttons, no sticky offers; the gauge's margin is the
instrument's mounting board.

**Density falls with the weather.** Clear chapters are airy:
panels at 96px internal padding, solution dissolved, the card
mostly empty glass around it. Change chapters tighten to 72px.
The storm chapter is the densest object on the page: 56px
padding, crystals at up to 30 branches per panel (§6.2), light
at its lowest — the layout itself is barometric, and a storm
chapter laid out as airily as a clear one has broken the
forecast (§9 failure 4). Whitespace in this theme is *fair
weather*: it is spent at the top of the page and gone by the
foot, and that spending is the page's argument.

**Section choreography.** The canonical descent: cabinet head
(§6.11) → hero panel (the maker's name in his glass, §6.1) →
the instruments (catalogue cards, §6.12) → the maker's section
(how to read the glass; the scale draws, §6.7) → the forecast
chapters (Clear, Changeable, Storm — product chapters wearing
their states, §6.2; the storm chapter pins, §6.3) → the
commission form (§6.14) under its disclaimer → the cabinet foot
(§6.16) printing the pressure at the bottom of the page. No
section may be reordered ahead of a fairer one: weather on this
page only ever worsens downward, and scroll-back is the only
way home to fair.

## 5. Full motion system

Every motion term from the library vocabulary, translated into
the instrument's language or refused with a reason. Five named
easings, and no others may appear in built CSS (§10 motion
audit): `--ease-grow cubic-bezier(0.22, 0.61, 0.21, 1)` —
crystal growth, quick to start branching, slow to finish;
`--ease-etch cubic-bezier(0.65, 0, 0.35, 1)` — the engraver's
even pressure; `--ease-swing cubic-bezier(0.34, 1.3, 0.44, 1)` —
the needle's mechanical overshoot, the only easing licensed to
exceed its target; `--ease-polish cubic-bezier(0.4, 0, 0.2, 1)`
— a shine crossing brass; `--ease-settle cubic-bezier(0.25,
0.8, 0.3, 1)` — panels and cards coming to rest in the cabinet.

**The shared loop and the heaviness.** One `requestAnimationFrame`
loop with lerp drives every scrubbed value: pressure, needle
angle, crystal density, reflection offsets, scroll heaviness.
The loop's pressure lerp is 0.10; its scroll-smoothing lerp is
itself barometric — **0.14 while the reading is FAIR or CHANGE,
0.08 in RAIN and STORM** — the page literally feels heavier as
the pressure drops (the original entry's "barometric heaviness
on the smooth scroll", made a number). Reduced-motion and
no-JS visitors get native scroll; the heaviness is a texture,
never a toll.

- **Scroll-triggered reveals.** Etch-then-fill plates (§6.6) at
  35% visibility; framed plates scale-in-frame (§6.17); the
  scale draw (§6.7) on entry. No element fades up from below —
  things in a cabinet are *revealed by being made*: etched,
  drawn, grown, polished.
- **Scroll-driven / scrubbed animation.** The master scrub:
  forecast states (§6.2) — density, haze and light are pure
  functions of lerped pressure, fully reversible; the needle
  (§6.4); reflection parallax (§6.10).
- **Parallax.** Three depths inside every panel (§6.10): card
  at 1.0, crystal layer at 0.92, reflection at 0.40. Nothing
  outside a panel parallaxes — mahogany does not move.
- **Pinned sections.** Exactly one pin per page: the storm
  chapter (§6.3), 160vh of pin in which density climbs to its
  ceiling and the rumble waits at the end. A second pin is a
  gate failure.
- **Smooth scrolling & progress.** The barometric heaviness
  above; progress *is* the needle (§6.4). No progress bar
  exists in this theme (§11).
- **Masked reveals.** The glass-reflection wipe (§6.10's
  companion beat in §6.2): a reflection band clears across each
  panel as it first centres — a wipe of light, not a mask over
  text; the card beneath is complete throughout.
- **Staggered reveals.** Plate etching staggers 90ms plate to
  plate within a rail (§6.6); catalogue cards settle 70ms apart
  (§6.12).
- **Kinetic typography.** Refused beyond one licensed case: the
  hero headline's letters crystallise in sequence (§6.1) — the
  type is grown around, never itself in motion. Letters that
  bounce, slide or flip are a music-hall act in a workshop.
- **Marquee.** Refused. Nothing in a cabinet hurries past.
- **Counters.** Pressure readings and forecast counts (§6.13)
  roll/count to their true values once, on entry, from the
  declared function and the DOM — never from zero by default
  (a barometer does not start at zero; counters start at the
  previous chapter's reading, §6.13).
- **SVG line-draw.** The barometer scale (§6.7), the hero
  crystals (§6.1), the tap-grown branch (§6.9): all stroke-draw
  in the maker's order — stems before branches, arc before
  ticks, ticks before words.
- **Image scale-in-frame.** Framed plates (§6.17): the image
  settles 1.06→1 inside its brass-and-glass frame while its
  reflection recentres.
- **Hover / magnetic / tilt micro-interactions.** Brass polish
  (§6.8) on every brass surface; instrument cards tilt ≤3° like
  plates lifted from the cabinet (§6.12). Magnetic drift is
  refused — brass plates are heavy and stay where they were
  put.
- **Custom cursor.** Refused. Normal system cursor only; the
  glass-tap (§6.9) answers the click itself, not the pointer's
  travel.
- **Skeleton loading.** Empty glass panels under haze (§6.15):
  the cabinet's shapes, unfilled, with the maker's line "The
  glass is being filled."
- **Page transitions.** The clouding (§6.15): crystals cloud
  the glass over 450ms, the page changes beneath the frost,
  the new page's glass dissolves clear over 600ms.
- **Ambient loops.** The living crystal cycle (§6.5) in the
  centred panel only; the hatching light crawl on brass plates
  (§6.6, a 9s traverse, plates in view only). Two ambient
  systems, never three, and both pause off-screen and on
  hidden tabs.
- **Reduced motion.** Weather fixed at Changeable: needle
  still at 29.94 in, density fixed at the Change value,
  crystals pre-grown in decorative panels, no rumble, no pin,
  no cycle, no wipe. The descent becomes a printed table of
  states — every chapter labelled with the reading it *would*
  have shown (§6.2's variant), so no information is lost with
  the weather.

## 6. Signature elements

### 6.1 Feathering hero crystals

- **What & why.** Inside the hero glass panel, SVG crystal
  branches feather into form around the maker's name over one
  ~2s pass — main stems first, then feathery side-branches at
  30–45°. It belongs because the headline is suspended in the
  glass's own medium: the maker's name is the first specimen in
  his cabinet, and watching the solution grow around it teaches
  the visitor what the instrument *does* before a word of copy
  is read. The crystals are the hero's frame, grown, not drawn.
- **Structure.** A real `<h1>` (the maker's name and trade, e.g.
  "Hartnell & Vane — Instrument Makers") printed in the DOM at
  full contrast on the hero card from first paint. Behind and
  around it, inside the panel's solution layer, an inline SVG
  crystal field: 7 authored main stems radiating from the
  panel's lower-left and upper-right corners (the solution
  grows from the glass's edges, as camphor does), each stem
  carrying 4–9 side-branches at authored 30–45° angles. Branch
  paths are hand-authored vector data per hero, never generated
  noise (§9 failure 2). The crystal layer is `aria-hidden`,
  `pointer-events: none`, and clipped to the panel's margin
  zones and the headline's surround — the glass law (§1) is
  enforced by the clip path, not by hope: no branch path may
  intersect the headline's text box or any body copy.
- **Motion spec.** Trigger: load, gated on
  `document.fonts.ready` raced against 800ms — growing crystals
  around a fallback face would misalign the trellis, so if fonts
  lose the race the field ships grown (see fallback). Stems draw
  0–900ms `--ease-grow`, stroke-dashoffset, staggered 120ms stem
  to stem in growth order (longest stem first — the solution
  starts where it is deepest). Side-branches draw from t=500ms,
  260ms each, staggered 60ms, parent stem before its branches,
  always. At t≈1400ms the headline's letters crystallise: a
  hairline haze-deep branch tip touches each letter's serif in
  sequence, 45ms per letter, cap 24 letters (a longer name
  shortens the touch to the first and last letters of each
  word). Total ceremony ≤2000ms; it plays once per session
  (`sessionStorage`), and returning visitors find the field
  grown.
- **States.** Ungrown (JS-armed only, dashoffset at full) →
  growing (stems, then branches, then letter-touches) → grown
  (rest; the field thereafter belongs to §6.5's cycle if the
  hero panel is the centred one). Hover/focus: none — the hero
  is not a control. Scrolled-past mid-growth: growth completes
  on its own timeline; the ceremony is load-locked, not
  scroll-locked.
- **Content merge.** The crystals grow around the page's actual
  `<h1>` inside the product the maker sells; they are the
  instrument demonstrating itself on its maker's name. Remove
  the crystals and the hero is a plain card — the merge test:
  the headline's meaning ("this name lives in the glass") is
  carried by the growth, not by decoration near it.
- **Failure fallback.** Watchdog at 2600ms: if growth has not
  completed, all dashoffsets snap to 0 (fully grown) — the field
  can never be left half-formed, and the headline was never
  hidden at any point: the ungrown state is a property of the
  crystal layer only. No JS: the SVG ships with dashoffset 0 —
  the field is printed grown.
- **Reduced-motion variant.** No growth. The field stands fully
  grown at the Change density (11 branches, §6.2's fixed
  weather), letter-touches omitted; the information (the name
  lives among crystals) survives as a still.
- **Performance budget & mobile variant.** Inline SVG ≤18KB;
  the pass animates `stroke-dashoffset` only — no layout, no
  filter. Mobile (<768px): 4 stems, branches capped at 5 per
  stem, ceremony compressed to 1400ms with 80ms stem stagger;
  letter-touches cut entirely.
- **Choreography timeline (v2).** t=0 fonts ready (or race lost
  → grown state, ceremony skipped) → t=0–900 stems draw,
  120ms stagger → t=500–1500 side-branches, 60ms stagger,
  parent-first → t≈1400 letter-touches begin, 45ms/letter →
  t≤2000 field complete → t=+400 the standfirst's plate etches
  (§6.6) → the hero rests; §6.5 may adopt the panel.
- **State matrix (v2).** *Rest:* grown field, headline printed.
  *Hover:* none. *Focus:* focus entering the hero does not alter
  the field; if focus lands mid-growth, growth completes
  instantly (a keyboard visitor is never asked to wait for
  weather). *Active:* n/a. *Scrolled-past:* grown. *Disabled /
  no-JS:* grown at first paint. *Touch:* identical; first touch
  anywhere completes a running growth.
- **Breakpoints (v2).** ≥1200px: 7 stems, full branch counts,
  54px display. 768–1199px: 6 stems, 44px display, ceremony
  1800ms. <768px: 4 stems, ≤5 branches/stem, 34px display,
  1400ms, no letter-touches.
- **Edge cases & failure modes (v2).** *Font swap after
  arming:* the layer is armed only after `fonts.ready`; a late
  swap disarms to grown. *Tab hidden mid-growth:* rAF pauses;
  on return, wall-clock past 2600ms fires the watchdog snap.
  *Name edited in a CMS:* branch paths are authored per hero —
  an edited headline without new paths ships grown, never
  misaligned (build check, §15). *Very long name:* letter-touch
  cap applies; stems are corner-anchored and cannot collide
  with a two-line headline because the clip zone is the panel
  margin, not the text box.
- **Accessibility spec (v2).** The `<h1>` is complete in the
  accessibility tree from first paint; the crystal layer is
  `aria-hidden="true"`. Growth is never announced. Contrast is
  the card's at all times — `--storm` on `--card` 11.08:1 —
  because the readable layer is never under a crystal (§1 glass
  law).
- **Tokens consumed (v2).** `--card`, `--haze`, `--haze-deep`,
  `--storm`, `--ease-grow`, `--dur-grow-stem` (900ms),
  `--dur-grow-branch` (260ms), `--dur-fallback-hero` (2600ms).

### 6.2 Forecast-state sections

- **What & why.** Each content section declares a forecast
  state, and its panel's crystal density, haze and light scrub
  continuously with scroll position between states: Clear
  (dissolved, bright), Changeable (wisps), Storm (dense, dark).
  It belongs because the weather is the page's information
  architecture — the maker's chapters are literally forecast by
  the instrument he sells, and the descent from fair to storm
  is the page's narrative spine. A section's state is declared
  in its data (`data-state-from`, `data-state-to` as pressure
  bounds), never hand-tuned per panel.
- **Structure.** Each panel carries three layers: the glass
  surround (state shading, §2), the solution layer (an SVG
  crystal field whose visible branch count is set from the
  density function), and the engraved card with the copy. The
  crystal field per panel is one authored SVG of 30 branches in
  growth order; density is rendered by revealing branches
  1..n — the field is grown by *count*, so density and the
  printed reading can be audited against each other (§10). The
  section's state word prints on its plate (§6.6) and updates
  only at threshold crossings (29.20/29.80/30.20), never
  flickering mid-band.
- **Motion spec.** Trigger: the shared loop's lerped pressure
  (lerp 0.10). Density, surround dimming (0% → 8% → 22% across
  the three bands) and haze opacity (0.06 → 0.20 → 0.38 in the
  surround only) are pure functions of pressure — scrubbed,
  fully reversible, no timers. A branch appearing or dissolving
  cross-fades over 600ms `--ease-grow` so density changes read
  as growth, not popping; at most 2 branch fades run per panel
  per frame (the loop queues the rest). The reflection wipe
  (§6.10) clears once as each panel first centres.
- **States.** *Clear* (P ≥ 30.20 in the panel's span): 0–2
  branches, surround undimmed. *Change* (29.80–30.19): 3–8
  branches, wisps only, dimming 8%. *Rain* (29.20–29.79): 9–17
  branches, dimming 15%. *Storm* (< 29.20): 18–30 branches,
  dimming 22%, haze at ceiling. Scrolled-past: a panel holds
  the state of the pressure at its own position — scrolling
  back up dissolves the storm behind you; the page's weather
  is positional, not accumulative (the rumble, §6.3, is the
  single exception).
- **Content merge.** The states are assigned by content, not by
  position alone: the catalogue chapter sits in Change (the
  weather of choosing), the maker's cautions chapter in Rain,
  the storm chapter is the maker's chapter on shipwreck sets
  and why ships carried the glass at all. The forecast is the
  table of contents wearing the product.
- **Failure fallback.** If the loop dies, panels render at the
  state their `data-state` midpoint declares, printed in the
  HTML — the no-JS page shows each panel at its chapter's
  honest mid-state with its state word printed, and a 2000ms
  watchdog forces any panel stuck between states to its
  nearer band. Content is never dimmed: dimming applies to the
  surround only, at every failure level.
- **Reduced-motion variant.** Weather fixed at Changeable for
  the whole page: every panel at 11 branches, dimming 8%, the
  state word on each plate reads the state the chapter *would*
  have reached ("This chapter's weather: Storm — held at
  Change for stillness"), so the descent's information survives
  as print.
- **Performance budget & mobile variant.** Per panel: one SVG
  ≤12KB, branch fades transform/opacity only; at most 3 panels
  animate density concurrently (the loop services the centred
  panel and its neighbours; distant panels snap). Mobile: branch
  ceiling 18 per panel, haze layers flattened to a single
  tint, dimming steps coarsened to the three bands.
- **Choreography timeline (v2).** Continuous: loop tick →
  pressure lerps toward `pressureAt(scroll)` → density target
  recomputed → branch fades queued (≤2/frame) → state word
  swaps within 120ms of a threshold crossing → plate (§6.6)
  re-prints the word. On panel first-centre: reflection wipe
  700ms (§6.10), then the panel joins §6.5's eligibility.
- **State matrix (v2).** *Rest:* the panel at its positional
  state. *Hover:* no change (hover belongs to brass, §6.8).
  *Focus:* focus inside a panel holds its density steady —
  growth pauses while a keyboard or reading visitor is *in*
  the panel, resuming 800ms after focus leaves; content must
  never change density under a reader. *Active:* n/a.
  *Scrolled-past:* state persists positionally. *Disabled /
  no-JS:* mid-state printed. *Touch:* identical; no
  hover-dependent states exist here.
- **Breakpoints (v2).** ≥1200px: full 30-branch fields, rail
  layout per §4. 768–1199px: 24-branch ceiling, dimming bands
  unchanged. <768px: 18-branch ceiling, single haze tint,
  panels stack with 48px mahogany rails.
- **Edge cases & failure modes (v2).** *Jump scroll to the
  foot:* pressure target leaps; density catches up at the
  queued fade rate — the storm visibly *arrives* over ~1.2s
  rather than popping, and the state word waits for density
  within ±3 branches before swapping. *Scroll back up fast:*
  dissolution uses the same queue; branches never linger above
  the target by more than 3. *Short page (few sections):* the
  pressure track compresses — `pressureAt` is defined over the
  weather track's length, not the document's, so a short page
  still reaches Storm only inside its storm chapter.
  *Content added to a panel:* branch clip zones are margin
  zones; added copy extends the card, and the field's clip is
  recomputed from the card box at build, not by hand.
- **Accessibility spec (v2).** State words are real text on the
  plate, not colour alone; density is never the only carrier
  of a state change — the printed reading (§6.13) and the
  needle (§6.4) announce the same weather in two other media.
  Surround dimming never reduces card contrast (§2: text
  pairings are state-invariant, audited in Storm). Live
  regions: none — weather changes are ambient, and announcing
  them would be noise; the reading is available on demand.
- **Tokens consumed (v2).** `--card`, `--card-deep`, `--haze`,
  `--haze-deep`, `--mahogany`, `--mahogany-deep`, `--ease-grow`,
  `--dur-branch-fade` (600ms), `--pressure-min` (28.61),
  `--pressure-max` (30.42).

### 6.3 The rumble

- **What & why.** At the storm section's pinned peak, after the
  crystals reach full density, the whole instrument gives
  exactly one 2px shake — 120ms, decaying — never repeated. It
  belongs because it is the page's only violence, and it is
  placed at the climax of the storm chapter: the instrument
  reacting to its own forecast. One shake, once, is thunder; a
  shake on every visit is a screensaver.
- **Structure.** The storm chapter's panel group sits inside a
  pin wrapper (160vh of scroll at ≥1200px). The shake is a
  `translate3d` keyframe sequence on the pin's inner cabinet
  frame — ±2px, ±1px, 0 — applied to the frame only, never to
  body text nodes directly (text moves *with* its panel, as a
  physical cabinet's contents would). A `sessionStorage` flag
  (`sg-rumbled`) records the event; the pin's end marker is a
  1px sentinel at the pin's final 5%.
- **Motion spec.** Trigger: the sentinel crossing while density
  is at ceiling (≥27 branches) and pressure ≤ 28.75 — all three
  conditions, so a fast fling through the pin without the storm
  having formed does not earn the rumble. The shake: 120ms
  total, offsets 0 → +2px → −2px → +1px → 0 at 0/30/65/90/100%,
  `--ease-settle` decay, one iteration. It fires at most once
  per session and never on re-entry, re-scroll, or resize.
- **States.** *Armed* (pin not yet completed, flag unset) →
  *fired* (flag set; the pin thereafter is a still storm) →
  *spent* (all later sessions in the same session). Hover/
  focus: none. Scrolled-past without firing (conditions unmet):
  stays armed until the conditions are truly met — the rumble
  is earned by the storm forming, not by arriving at a
  coordinate.
- **Content merge.** The shake moves the chapter the visitor is
  reading — the shipwreck-sets chapter, whose copy at the pin's
  end concerns the night the glass fell off a cabin wall. The
  instrument enacts the copy's event at the copy's moment; it
  is not a page-wide effect in search of a place to happen.
- **Failure fallback.** If the pin is unsupported (no
  IntersectionObserver, JS off), there is no rumble and nothing
  is missing: the chapter reads as a dense static storm panel,
  and the copy carries the moment alone. A watchdog is
  deliberately absent — an effect whose fallback is *not
  happening* needs no rescue.
- **Reduced-motion variant.** Never fires. The pin itself is
  also removed: the storm chapter is a normal dense panel
  (§6.2's variant), and the copy at its end gains the printed
  line "(Here the glass is said to shudder.)" — the event
  survives as a stage direction.
- **Performance budget & mobile variant.** One transform
  animation on one wrapper, 120ms, no layout. Mobile: the pin
  shortens to 120vh and the shake reduces to ±1px — a small
  cabinet shakes less — or is cut entirely below 360px width
  (§14 cut order).
- **Choreography timeline (v2).** Pin progress 0 → density
  climbs with pressure (§6.2) → p=0.95 sentinel armed →
  conditions checked (density ≥27, P ≤ 28.75, flag unset) →
  t=0 shake begins as the chapter's final plate etches (§6.6)
  → t=120ms rest → flag written → the pin releases 300ms
  later into the chapter's tail.
- **State matrix (v2).** *Rest (pre-storm):* armed, invisible.
  *Hover:* none. *Focus:* if focus is inside the storm panel
  when conditions are met, the shake is **suppressed** and the
  flag is set anyway — the page never moves under a reader who
  is reading by keyboard or switch; the stage-direction line
  prints instead. *Active:* n/a. *Scrolled-past:* spent or
  armed per conditions. *Disabled / no-JS:* absent. *Touch:*
  identical, ±1px amplitude under 768px.
- **Breakpoints (v2).** ≥1200px: 160vh pin, ±2px. 768–1199px:
  140vh pin, ±2px. <768px: 120vh pin, ±1px; <360px: no shake.
- **Edge cases & failure modes (v2).** *Resize during the
  pin:* pin length recomputes; the sentinel re-arms only if
  the flag is unset and conditions still hold. *Session flag
  blocked (private mode):* the rumble may fire once per page
  load instead of once per session — accepted, since the
  alternative (tracking) is worse than the repetition.
  *Density ceiling unreachable (mobile 18-branch cap):* the
  density condition scales to the breakpoint's ceiling (≥90%
  of cap), so mobile still earns its rumble.
- **Accessibility spec (v2).** The shake is decorative and
  unannounced; it moves no focus and changes no content.
  Vestibular safety: amplitude ≤2px, duration 120ms, once —
  within the theme's own strictest reading of safe motion, and
  fully removed under `prefers-reduced-motion` and under
  focus-within (above). No information is carried by the shake
  that is not also in the copy.
- **Tokens consumed (v2).** `--ease-settle`, `--dur-rumble`
  (120ms), `--rumble-amp` (2px; 1px <768px), `--pressure-min`
  (28.61).

### 6.4 Barometer progress needle

- **What & why.** A brass needle on an engraved margin scale —
  FAIR / CHANGE / RAIN / STORM — swings scrubbed to scroll
  depth: progress *is* pressure. It belongs because the reader
  descends through weather, and the maker's own gauge is the
  page's indicator; a progress bar would be a foreign object in
  the cabinet, while the needle is the product working. The
  needle is also the law's most public printing (§1): its angle
  is computed from the same lerped pressure as every panel's
  density, so the margin and the panels can be caught agreeing
  or the gate fails.
- **Structure.** A fixed-position instrument in the right
  margin rail (§4): an SVG arc scale spanning 150°, graduated
  28.00–31.00 inHg, ticks every 0.10 in with longer ticks at
  the whole inches, the four state words engraved along the
  arc, and a brass needle (SVG path, counterweighted tail)
  rotating about the dial's centre. Beneath the dial, the
  current reading prints in Plex Mono (`--reading-now`, e.g.
  "29.94 IN"), updated from the same value. The dial face is
  `--card`; its bezel is a brass ring; the whole instrument is
  ~112px wide in the rail. The needle's angle is a declared
  function of pressure alone: `angle = −75° + (31.00 − P) ×
  50°`, mapping 31.00 in → −75° and 28.00 in → +75° linearly
  across the 150° sweep — so the track's ends land at −46°
  (30.42 in, FAIR) and +44.5° (28.61 in, STORM), and any
  builder can check a needle against a reading with one
  multiplication.
- **Motion spec.** Trigger: the shared loop; the needle's
  rotation is the lerped pressure (lerp 0.10) rendered through
  `--ease-swing`'s character — the lerp gives the swing its
  mechanical overshoot naturally as pressure crosses section
  boundaries, and an additional authored overshoot of 1.5°
  decaying over 400ms fires at each state-threshold crossing,
  the needle tapping past the word and settling back onto it,
  as a real needle trembles at a change. The printed reading
  updates at most every 120ms (a barometer's figures do not
  flicker) and always equals the needle's pressure to two
  decimals.
- **States.** *Rest (top):* needle at 30.42 in, FAIR. *In
  descent:* swinging with the lerp, overshooting at
  thresholds. *Scrolled-past / at foot:* 28.61 in, STORM, and
  the dial's foot prints "AT THE BOTTOM — 28.61 IN" (§6.16
  agrees). *Hover:* the dial brightens its bezel polish (§6.8)
  — the one instrument the visitor may handle. *Focus:* the
  dial is not focusable; it is an indicator. *Disabled /
  no-JS:* the needle ships printed at 29.94 in (Change, the
  page's honest mid-state) with the reading printed beneath.
- **Content merge.** The gauge measures the page the visitor is
  inside; its scale words name the chapters they are passing
  (§6.2). It is mounted in the margin like the maker's own
  shop barometer beside his bench — an instrument among
  instruments, not a widget.
- **Failure fallback.** If the loop dies, a 1500ms watchdog
  parks the needle at the pressure of the current scroll
  position computed once (no lerp) — the gauge remains true,
  merely less alive. If SVG fails, the printed reading alone
  remains in the rail, updated on scroll by the same watchdog
  path.
- **Reduced-motion variant.** Needle still at 29.94 in for the
  whole page; the printed reading beneath is replaced by the
  table of chapter readings (each chapter's pressure as print,
  §5) — progress information survives as a list, not a swing.
- **Performance budget & mobile variant.** One SVG ≤6KB; one
  transform per frame. Mobile (<768px): the margin rail does
  not exist, so the instrument becomes a compact horizontal
  barometer fixed at the foot of the cabinet head — a 44px
  brass strip with a travelling needle marker and the printed
  reading — retiring once the commission form (§6.14) is on
  screen, so it never competes with the conversion.
- **Choreography timeline (v2).** Continuous: loop tick →
  pressure lerps → needle rotates → reading reprints ≤ every
  120ms. At a threshold crossing: t=0 needle passes the word →
  +1.5° overshoot → 400ms decay back onto the reading → the
  crossed chapter's plate (§6.6) re-prints its state word
  within the same 120ms window.
- **State matrix (v2).** *Rest:* as States above. *Hover:*
  bezel polish only. *Focus:* n/a (not focusable); focus
  elsewhere never moves the needle. *Active:* n/a.
  *Scrolled-past:* holds foot reading. *Disabled / no-JS:*
  printed at Change. *Touch:* identical; the compact mobile
  strip is not tappable (taps belong to glass, §6.9).
- **Breakpoints (v2).** ≥1200px: full dial, 112px, in the rail.
  768–1199px: dial shrinks to 88px, state words abbreviated to
  F / C / R / S with the full words in the printed reading's
  line ("CHANGE — 29.94 IN"). <768px: the foot-strip variant
  above.
- **Edge cases & failure modes (v2).** *Jump scroll:* the lerp
  swings the needle through the intervening weather over
  ~900ms — the visitor watches the needle fall, which is the
  point; the reading updates en route and lands true.
  *Threshold flutter* (scroll hovering at a boundary): the
  overshoot fires once per crossing with a 1000ms refractory —
  the needle may tremble, it may not chatter. *Very short
  page:* the pressure track is the weather track (§6.2), so
  the needle still traverses its full arc across the chapters
  that exist.
- **Accessibility spec (v2).** The dial is `role="img"` with an
  `aria-label` carrying the current reading and state ("Barometer:
  29.94 inches, Change"), updated at most every 2s to avoid
  chatter, and the printed reading is real text. The needle's
  motion is ambient; no information exists only in the angle —
  reading and state word are both text.
- **Tokens consumed (v2).** `--brass`, `--brass-bright`,
  `--brass-deep`, `--card`, `--storm`, `--ease-swing`,
  `--dur-reading-print` (120ms), `--pressure-min` (28.61),
  `--pressure-max` (30.42).

### 6.5 Living crystal cycle

- **What & why.** In whichever panel is centred, crystal wisps
  slowly grow (over ~8s) then dissolve (over ~6s) in an endless,
  unsynchronised cycle — one panel at a time. It belongs because
  the instrument beside the copy is alive while you read about
  it: the product demonstrates itself continuously, in the
  corner of the eye, at the pace of a real solution (which is to
  say, almost too slow to watch — and that slowness is the
  luxury being sold).
- **Structure.** Each panel's solution layer (§6.2) carries, in
  addition to its density field, a **cycle cluster**: 3–5 wisp
  paths in the panel's margin zones, authored per panel, drawn
  in `--haze-deep` hairlines. Only the centred panel's cluster
  is active; "centred" means the panel occupying the viewport's
  middle third, resolved by the shared loop. The cluster's
  growth is a dashoffset cycle on its own paths, independent of
  the density field — the cycle is weather *within* the state,
  and it may never push a panel's visible branch count more
  than ±2 from the density function's figure (§1 audit counts
  the density field only, and the cycle's wisps are drawn in a
  lighter hand so the two are distinguishable).
- **Motion spec.** Trigger: a panel becoming centred. Grow
  phase 8000ms `--ease-grow` (dashoffset to full), hold 2000ms,
  dissolve phase 6000ms (dashoffset back, opacity to 0.0 at the
  end), rest 3000ms — a 19s full cycle, deliberately out of
  phase with any other rhythm on the page. When the panel stops
  being centred, the cycle freezes mid-phase and resumes on
  return; a panel never restarts its cycle for a passer-by.
  Only one cluster animates at a time, ever (§5's ambient
  budget).
- **States.** *Dormant* (panel not centred): cluster at its
  frozen phase, rendered. *Growing / holding / dissolving /
  resting:* the cycle phases. *Hover:* no change. *Focus:*
  focus inside the panel freezes the cycle (with §6.2's
  density hold) — the solution stills while it is being read
  closely. *Scrolled-past:* dormant. *Disabled / no-JS:*
  clusters ship at full growth, printed.
- **Content merge.** The cycle lives in the panel whose copy
  the visitor is reading — the instrument next to the words
  about itself. In the maker's section, the centred panel's
  cluster sits beside the paragraph explaining that crystals
  grow and dissolve with the weather: the sentence and the
  specimen perform each other.
- **Failure fallback.** If the loop dies, clusters freeze where
  they are — a frozen wisp is still a wisp; nothing is lost and
  no watchdog is needed beyond the loop's own (§6.2). If a
  cluster's SVG fails, the panel simply lacks its cycle; the
  density field is a separate layer and is unaffected.
- **Reduced-motion variant.** No cycle. Clusters print at full
  growth in every panel — the stillness variant trades the
  life for the specimen, complete.
- **Performance budget & mobile variant.** Per panel ≤4KB of
  paths; one dashoffset animation on the active cluster only.
  Mobile: cycle clusters are cut to 2 wisps and the cycle
  lengthens (grow 10000ms / dissolve 8000ms) — fewer, slower,
  cheaper; below 360px the cycle is cut entirely (§14).
- **Choreography timeline (v2).** Panel centres → t=+600ms
  (a settle delay, so scrolling through never triggers it) →
  grow 8000ms → hold 2000ms → dissolve 6000ms → rest 3000ms →
  repeat while centred. Panel decentres → freeze within one
  frame. Another panel centres → the first freezes, the new
  one begins after its own 600ms settle.
- **State matrix (v2).** *Rest:* dormant or mid-cycle as above.
  *Hover:* none. *Focus:* frozen. *Active:* n/a.
  *Scrolled-past:* dormant, phase preserved. *Disabled /
  no-JS:* printed full-grown. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: 3–5 wisps, 19s cycle.
  768–1199px: 3 wisps, 19s. <768px: 2 wisps, 21s; <360px: cut.
- **Edge cases & failure modes (v2).** *Two panels share the
  middle third* (short panels): the one with the larger share
  wins; ties keep the incumbent — the cycle never splits.
  *Hidden tab:* the loop pauses; phases resume by wall-clock
  so a returning visitor finds the cycle where time says it
  should be, not where the tab left it. *Panel edited longer:*
  the cluster's margin clip recomputes from the card box (§6.2).
- **Accessibility spec (v2).** The cluster is `aria-hidden`;
  it carries no information (the density field and the reading
  carry the weather). Its motion is sub-perceptual in speed —
  8s growth — and fully removed under reduced motion.
- **Tokens consumed (v2).** `--haze`, `--haze-deep`,
  `--ease-grow`, `--dur-cycle-grow` (8000ms),
  `--dur-cycle-dissolve` (6000ms).

### 6.6 Etch-then-fill plates

- **What & why.** Section plates — the brass labels that head
  each chapter and name each instrument — enter by etching:
  label strokes draw in hairline form (~500ms), then fill with
  ink weight and colour. It belongs because the plates are
  engraved before your eyes in the maker's own sequence: first
  the burin's line, then the ink worked into it. The reveal is
  the craft that made the object being labelled.
- **Structure.** Each plate is a brass plaque (rounded 2px —
  the cabinet's only radius besides the seal-slip, §11) bearing
  an SVG text-path label: the label's letterforms exist as
  stroke paths (etched state) over a filled text element in
  Libre Caslon (filled state). The etched layer draws with
  dashoffset; the filled layer cross-fades in beneath it and
  the etched layer retires. Plates carry: chapter name, state
  word (§6.2), and where relevant a reading or a price — the
  plate is the panel's nameplate, not a heading substitute (the
  real `<h2>` is inside the card; the plate is its brass twin,
  `aria-hidden`).
- **Motion spec.** Trigger: scroll into view at 35% visibility.
  Etch 500ms `--ease-etch` (strokes in reading order, 30ms
  stagger per character group), hold 120ms, fill 300ms
  `--ease-settle` (filled layer opacity 0→1, etched layer
  1→0.25 then removed). Within a rail of plates, stagger 90ms
  plate to plate. A plate etches once; scrolled-past plates are
  filled, permanently — engraving is not undone by leaving the
  room. The brass hatching on each plate carries §5's light
  crawl: a faint highlight traversing the engraving over 9s,
  plates in view only.
- **States.** *Un-etched* (JS-armed only: filled layer at 0,
  etched at 0) → *etching* → *filling* → *filled* (rest).
  *Hover:* a filled plate takes the polish (§6.8). *Focus:* a
  plate that is a link (chapter plates in the nav, §6.11)
  etches instantly on focus if not yet etched — a keyboard
  visitor never waits for engraving. *Scrolled-past:* filled.
  *Disabled / no-JS:* the filled layer is the DOM default; the
  etched layer is inserted by JS only.
- **Content merge.** The plate names the thing it is screwed
  to: the chapter plate is physically at the chapter panel's
  head on the mahogany rail; an instrument's plate is on its
  card (§6.12). The etching happens where the maker's hand
  would have worked — on the object, at its naming.
- **Failure fallback.** Watchdog at 1200ms per plate: any plate
  not filled by then snaps to filled. The DOM default is
  filled, so a dead script leaves a cabinet of finished plates.
- **Reduced-motion variant.** Plates arrive filled. The
  two-weight fact (§3 law 3) is preserved in print: the label
  shows a hairline ghost of the etch at 20% beside the filled
  weight — the process survives as evidence, not performance.
- **Performance budget & mobile variant.** Per plate ≤3KB SVG;
  etch animates dashoffset only. Mobile: etch compresses to
  350ms, stagger 50ms, and the light crawl is cut (plates are
  smaller; a crawl on a 40mm plate is noise).
- **Choreography timeline (v2).** Plate at 35% visibility →
  t=0 etch begins → t=500 etch complete → t=620 fill begins →
  t=920 filled, etched layer removed → t=+2000 the plate joins
  the hatching crawl rotation if in view. Rail of plates:
  +90ms per plate.
- **State matrix (v2).** *Rest:* filled. *Hover:* polish
  (§6.8). *Focus:* instant fill if un-etched; focus ring is the
  brass-deep outline (§11). *Active:* press behaviour where the
  plate is a link (§6.11). *Scrolled-past:* filled.
  *Disabled / no-JS:* filled. *Touch:* no hover polish; tap on
  a plate that is a link navigates (§6.11), tap on a plain
  plate does nothing — plates are not glass (§6.9).
- **Breakpoints (v2).** ≥1200px: plates 44px tall, labels
  12.5px mono / chapter plates Caslon 20px. 768–1199px: 40px.
  <768px: 36px, etch 350ms, crawl cut.
- **Edge cases & failure modes (v2).** *Plate edited in a CMS:*
  stroke paths are authored per label; an edited label without
  new paths ships filled (build check, §15). *Fast scroll
  through a rail:* plates passed above 35% visibility etch in
  compressed time (200ms) or fill instantly if already above
  the viewport — no plate is ever left hairline-only (§3 law
  3). *Long labels:* two-line plates are refused at build; a
  chapter name that needs two lines is renamed (§12).
- **Accessibility spec (v2).** Plates are `aria-hidden` twins;
  the accessible name lives on the real heading inside the
  card. Where a plate *is* the label of a control (nav), the
  control carries its own `aria-label` and the plate is still
  decorative. Filled labels meet §2 contrasts: a plate's
  display label is set in `--card` directly on the brass at
  ≥20px only (4.08:1 — a large-text pass, and the reason plate
  labels are never small), and all small apparatus on a plate
  sits on the plate's `--card` inset strip in `--brass-deep`
  (5.94:1). Dark-engraved text straight on brass is refused:
  measured for this expansion, `--mahogany-deep` on `--brass`
  is only 2.81:1, and a plate nobody can read is jewellery,
  not an instrument.
- **Tokens consumed (v2).** `--brass`, `--brass-deep`,
  `--brass-bright`, `--card`, `--mahogany-deep`, `--ease-etch`,
  `--ease-settle`, `--dur-etch` (500ms), `--dur-fill` (300ms).

### 6.7 Barometer scale draw

- **What & why.** In the maker's section ("How to read the
  glass"), an engraved arc scale — 28 to 31 inches, the state
  words in their bands — strokes itself over ~1.6s, and the
  needle then sweeps to the current reading. It belongs because
  the diagram is the instrument's own face, drawn in the order
  the engraver cut it, at the moment the copy explains how to
  read it: the lesson and the instrument arrive together.
- **Structure.** A large inline SVG (the section's centrepiece,
  ~520px wide at desktop): the arc path, 31 tick paths (0.10 in
  divisions, whole-inch ticks longer), four state-word labels
  as filled text (printed from first paint — words are not
  drawn, they are *revealed* by the arc reaching them), and a
  needle identical in geometry to §6.4's. Around the scale, the
  maker's reading instructions in Caslon, and a printed table
  of the four bands with their pressures (the same thresholds
  as §1 — the section's data is the law's data). All stroke
  layers are JS-armed; the complete scale is the DOM default.
- **Motion spec.** Trigger: the scale entering view at 40%.
  Arc draws 0–900ms `--ease-etch`; ticks draw 700–1400ms,
  staggered 12ms in reading order (28 upward — the engraver
  works from Storm to Fair, as the copy notes); state words
  fade in as the arc passes their band (at their arc positions'
  draw times); the needle then sweeps from its rest at 31.00
  to the *current page reading* over 600ms `--ease-swing` with
  its 1.5° overshoot, and thereafter this needle is slaved to
  the same lerped pressure as §6.4 — the section's instrument
  and the margin's instrument are the same instrument twice.
- **States.** *Undrawn* (JS-armed only) → *drawing* → *drawn,
  needle live* (rest). *Hover:* the scale's needle takes the
  polish (§6.8). *Focus:* if focus reaches the section before
  the draw, the draw completes instantly. *Scrolled-past:*
  drawn, needle live. *Disabled / no-JS:* complete scale,
  needle printed at the section's own chapter reading (Change,
  29.94 in).
- **Content merge.** The scale is the subject of the section
  that contains it — the copy's verbs ("read the needle against
  the word it leans to") refer to the drawing happening beside
  them. It is a working instrument, not an illustration of one:
  its needle never stops being true after the draw.
- **Failure fallback.** Watchdog at 2200ms: any undrawn stroke
  snaps drawn; the needle snaps to the current reading. DOM
  default is the finished scale.
- **Reduced-motion variant.** The scale stands drawn, needle at
  29.94 in still; the band table beside it carries the section's
  full information (as it does in every variant).
- **Performance budget & mobile variant.** SVG ≤14KB; draw
  animates dashoffset only. Mobile: scale scales to container
  width (SVG viewBox), draw compresses to 1100ms total, tick
  stagger 6ms; the band table stacks beneath.
- **Choreography timeline (v2).** Section at 40% → t=0 arc →
  t=700 ticks begin → t=1400 ticks complete, words all revealed
  → t=1500 needle sweep begins → t=2100 needle settled on the
  live reading → the needle joins the shared loop.
- **State matrix (v2).** *Rest:* drawn, live. *Hover:* needle
  polish. *Focus:* instant draw. *Active:* n/a. *Scrolled-past:*
  drawn, live. *Disabled / no-JS:* drawn, printed needle.
  *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: 520px scale beside the copy
  column. 768–1199px: 440px, stacked above the copy. <768px:
  full-width, 1100ms draw, band table below.
- **Edge cases & failure modes (v2).** *Section reached by
  anchor jump:* draw is skipped, scale printed, needle live —
  nobody is made to watch engraving because they clicked a
  link. *Reading at draw time is Storm* (visitor scrolled the
  long way first): the needle sweeps the full arc to 28.61 —
  the longest sweep is the most instructive, and it is allowed
  its 900ms. *Re-entry:* never redraws.
- **Accessibility spec (v2).** The SVG is `role="img"` labelled
  "Barometer scale, 28 to 31 inches; the needle reads [current
  reading], [state]" — the label updates with the printed
  reading (§6.4's 2s throttle). The band table is real text and
  carries the same thresholds for AT without the diagram.
- **Tokens consumed (v2).** `--brass`, `--brass-deep`,
  `--card`, `--storm`, `--ease-etch`, `--ease-swing`,
  `--dur-scale-draw` (1600ms), `--pressure-min` (28.61),
  `--pressure-max` (30.42).

### 6.8 Brass polish hover

- **What & why.** Hovering any brass element passes a shine
  gradient across it (500ms) and darkens its engraving by 15%
  while hovered. It belongs because handling brass polishes it:
  the visitor's attention maintains the instruments, as the
  maker's hand would. It is the theme's universal hover — one
  gesture for every brass surface, so the cabinet feels like
  one material under one hand.
- **Structure.** A `--brass-bright` linear-gradient layer masked
  to each brass element (plates §6.6, bezels §6.4, frames
  §6.17, nav plates §6.11, buttons §11), translating across the
  element's width; beneath it, the element's engraved detail
  (an SVG or text layer) carries a `filter: brightness(0.85)`
  state — the 15% darkening. Both layers are composited; no
  layout property animates.
- **Motion spec.** Trigger: pointerenter / focus-visible. The
  shine traverses in 500ms `--ease-polish`, entering from the
  side the pointer entered (left/right by pointer x relative
  to centre — a small truthfulness: the hand comes from
  somewhere). The engraving darkens over 200ms, holds while
  hovered, and restores over 350ms on leave — polishing is
  quick, tarnish returns slowly. One traverse per entry; a
  pointer that stays does not re-polish.
- **States.** *Rest:* matte brass, engraving at full value.
  *Hover:* shine traverse + darkened engraving. *Focus:* same
  as hover, shine entering from the left (keyboard has no
  side). *Active:* the shine is suppressed during press (the
  press has its own feedback, §11) and the darkening deepens to
  25% for the press duration. *Scrolled-past:* n/a.
  *Disabled:* a disabled brass control takes no polish — dull
  brass is the disabled state (§11), and polishing it would
  lie.
- **Content merge.** The polish is applied to the brass that
  carries content — plates with names, frames with pictures,
  the needle that tells the weather. It is maintenance of the
  instruments the visitor is using, not a glow sprayed on
  chrome: UI elements that are not brass (text links, card
  controls) never polish.
- **Failure fallback.** If gradients or filters are
  unsupported, hover falls back to the darkening alone, then to
  nothing — hover feedback is an enhancement on elements whose
  function never depends on it. No watchdog: a shine that fails
  to shine strands nothing.
- **Reduced-motion variant.** No traverse. Hover/focus applies
  the 15% engraving darkening instantly (a state change, not a
  motion) — the feedback survives, the gesture rests.
- **Performance budget & mobile variant.** Gradient + filter on
  the hovered element only; zero cost at rest. Touch: no hover
  — tap on brass controls gives the darkening for 200ms as
  press feedback; tap on brass *panels* belongs to §6.9, and
  the two never fire together (the tap handler claims it).
- **Choreography timeline (v2).** t=0 pointerenter → shine
  starts at the entry edge → t=200 engraving at −15% → t=500
  shine exits → hover held: darkening holds → pointerleave →
  t=+350 engraving restored.
- **State matrix (v2).** *Rest:* matte. *Hover:* as spec.
  *Focus:* as spec, left-entry. *Active:* shine suppressed,
  −25% while pressed. *Scrolled-past:* n/a. *Disabled:* no
  polish, brass rendered dull (brightness 0.92, engraving at
  60% contrast). *Touch:* press-darkening only.
- **Breakpoints (v2).** Identical at all breakpoints; traverse
  duration scales with element width (300ms under 120px wide,
  500ms above) so a small plate is not polished slower than a
  frame.
- **Edge cases & failure modes (v2).** *Pointer skims across a
  rail of plates:* each plate polishes in turn with its own
  entry side; a plate entered and left within 100ms completes
  its traverse in the background rather than restarting —
  no flicker. *Focus and hover together:* one traverse, from
  the pointer's side. *Forced-colors mode:* shine and darkening
  are removed; focus and hover use the system outline (§11).
- **Accessibility spec (v2).** Polish is never the only hover
  signal on a control: links and buttons also take the
  brass-deep underline/outline (§11), because a shine is not
  perceivable to everyone. Darkening never reduces text
  contrast below its §2 floor — engraving darkens, but text
  insets (§6.6) sit on card and are exempt from the filter.
- **Tokens consumed (v2).** `--brass`, `--brass-bright`,
  `--brass-deep`, `--ease-polish`, `--dur-polish` (500ms).

### 6.9 Glass-tap click

- **What & why.** Clicking a glass panel grows one tiny crystal
  branch (3 strokes, ~400ms) from the click point, which stays
  for the session. It belongs because tapping the glass is what
  every keeper of a storm glass has always done — it disturbs
  the solution and starts a crystal — and the theme makes the
  folklore functional on the panel itself. The tap is the
  page's signature click: not a ripple, not a burst — a small,
  permanent consequence in the solution.
- **Structure.** Each panel's solution layer carries a tap
  layer (SVG, `pointer-events: none`, above the density field,
  below the card). A tap computes the click point in panel
  coordinates, clamps it to the panel's margin zones (the glass
  law — a tap landing on the card itself grows its branch from
  the nearest margin point, so a branch never crosses text even
  when the visitor taps the text), and appends one authored
  3-stroke branch (a stem and two side-branches at 30–45°, the
  §6.1 vocabulary at miniature scale) rotated toward the
  panel's nearest corner — crystals grow toward the glass's
  edges. Branches persist in the DOM for the session; a panel
  holds at most 12 tap-branches, after which the oldest
  dissolves over 2000ms to make room (the solution can only
  hold so much disturbance).
- **Motion spec.** Trigger: click/tap on a panel (not on a
  control inside it — clicks on links, buttons and fields are
  theirs alone and grow nothing). The branch draws over 400ms
  `--ease-grow`: stem 0–200ms, side-branches 150–400ms
  staggered 60ms. No sound, no shake (the rumble is rationed,
  §6.3), no motion outside the 24px neighbourhood of the tap.
- **States.** *Rest:* tap layer holds the session's branches.
  *Growing:* the new branch's 400ms. *Settled:* branch at full
  hairline. *Dissolving:* the 13th tap fades the oldest over
  2000ms. *Hover:* none (hover is brass's, §6.8). *Focus:*
  keyboard equivalent — a panel that contains focus offers its
  branch through the Enter key on the panel's plate (§6.6)
  only where the plate is already a control; panels are not
  made focusable for decoration's sake (§11 refuses fake
  controls).
- **Content merge.** The branch grows in the solution of the
  panel whose content the visitor is reading, from the spot
  they touched: the visitor's reading leaves a mark in the
  instrument they are reading about. Session-persistent, so a
  returning scroll shows the panels *they* weathered.
- **Failure fallback.** If the tap layer fails, clicks simply
  do nothing extra — no content depends on a tap. If JS is
  off, panels carry no tap layer; nothing is missing, because
  the tap is a response, not a feature with content.
- **Reduced-motion variant.** The branch appears fully drawn
  (no growth) — the consequence survives, the 400ms rests.
  The 12-branch cap and dissolution become instant swaps.
- **Performance budget & mobile variant.** Each branch ≤0.4KB
  of path; ≤12 per panel; drawing animates dashoffset only.
  Mobile: identical (taps are native to touch); branch size
  scales to 18px so a fingertip's branch is proportionate.
- **Choreography timeline (v2).** t=0 click on panel →
  coordinates clamped to margin zone → t=0–200 stem draws →
  t=150–400 side-branches → branch settles into the tap layer
  → if count >12, oldest begins its 2000ms dissolve at t=400.
- **State matrix (v2).** *Rest:* branches held. *Hover:* none.
  *Focus:* none (see States). *Active:* the tap itself.
  *Scrolled-past:* branches persist. *Disabled / no-JS:* no
  tap layer. *Touch:* identical, 18px branches.
- **Breakpoints (v2).** ≥1200px: 24px branches, cap 12.
  768–1199px: 20px, cap 10. <768px: 18px, cap 8 — a small
  panel's solution saturates sooner, which is honest.
- **Edge cases & failure modes (v2).** *Rapid tapping:* taps
  queue at most 3 growing branches per panel; further taps
  during the queue are ignored (a shaken solution grows
  nothing — the copy in the maker's section says exactly this).
  *Tap on the hero during §6.1's growth:* the tap branch waits
  for the ceremony's end. *Session restore:* branches are
  DOM-only and do not survive reload — the session is the
  sitting, as at a real cabinet.
- **Accessibility spec (v2).** The tap layer is `aria-hidden`;
  a tap is never announced and never required. No information
  is stored only in tap-branches. The interaction is
  pointer-only by design and is therefore exempt from keyboard
  parity *as decoration* — the rule (§11) is that anything
  with content must have parity, and the tap has none.
- **Tokens consumed (v2).** `--haze-deep`, `--ease-grow`,
  `--dur-tap-grow` (400ms).

### 6.10 Reflection parallax

- **What & why.** Each glass panel carries a diagonal reflection
  layer that parallaxes against the crystals inside at a 0.4×
  offset, so glass, crystal and card read as three real depths.
  It belongs because the panel's construction — glass over
  crystal over card — *is* the product's construction; the depth
  is the instrument's anatomy, demonstrated by the slight
  disagreement between its layers when the visitor moves.
- **Structure.** Per panel: the card (scrolls at 1.0, in flow),
  the solution layer (§6.2) translated at 0.92× of the panel's
  viewport traverse, and the reflection layer — a diagonal
  `--card` gradient band at 12% opacity over a haze wash —
  translated at 0.40×, clipped to the panel's glass surround
  (never over the card: reflections live on glass, and glass is
  the surround). Both offsets are computed by the shared loop
  from the panel's position; layers are `aria-hidden`,
  `pointer-events: none`.
- **Motion spec.** Trigger: scroll, via the shared loop (lerp
  0.10 shared with pressure — one loop, one clock). The
  reflection band also performs the **wipe**: as a panel first
  centres, the band sweeps once across the glass over 700ms
  `--ease-polish` — the glass clearing as you arrive at it —
  then settles into its parallax offset. The wipe fires once
  per panel per session.
- **States.** *Unwiped* (JS-armed: band parked at the panel's
  left edge) → *wiping* → *settled parallax* (rest). *Hover:*
  none. *Focus:* a panel receiving focus has its wipe completed
  instantly if pending. *Scrolled-past:* settled. *Disabled /
  no-JS:* the reflection prints at its centred offset — the
  three depths read statically, which is how a real cabinet
  reads standing still.
- **Content merge.** The reflection is on the glass *of the
  panel whose content it fronts* — the depth belongs to that
  instrument, not to the page's chrome. The wipe's clearing is
  the visitor arriving at that instrument in the cabinet.
- **Failure fallback.** If the loop dies, layers hold their
  last offsets — a still cabinet. No watchdog needed: nothing
  can be stranded by a reflection standing still.
- **Reduced-motion variant.** No parallax, no wipe. The
  reflection prints at its centred offset in every panel.
- **Performance budget & mobile variant.** Two transforms per
  panel per frame, on composited layers; panels outside the
  viewport are skipped by the loop. Mobile: the crystal layer's
  offset is cut (solution at 1.0) and only the reflection moves
  at 0.40× — two depths on a phone, which is depth enough.
- **Choreography timeline (v2).** Panel approaches centre →
  wipe begins at 45% visibility → 700ms sweep → band settles
  to its 0.40× offset → continuous parallax while the panel
  traverses → loop retires the panel off-screen.
- **State matrix (v2).** *Rest:* settled parallax. *Hover:*
  none. *Focus:* wipe completed instantly. *Active:* n/a.
  *Scrolled-past:* settled. *Disabled / no-JS:* printed offset.
  *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: full three depths. 768–1199px:
  full. <768px: two depths (reflection only), wipe 500ms.
- **Edge cases & failure modes (v2).** *Panels taller than the
  viewport:* offsets are computed over the panel's traverse
  capped at 150vh of travel, so a long panel's layers do not
  drift absurdly. *Jump scroll:* the lerp settles layers over
  ~600ms — glass arriving a breath after the page is correct
  physics, not lag. *Reflection over dark storm surround:* the
  band's opacity drops to 8% in the storm band (§6.2) so the
  glass reads darker as the weather does.
- **Accessibility spec (v2).** Purely decorative and
  `aria-hidden`; the layers never overlap the card, so contrast
  is untouched at every offset (the glass law, §1).
- **Tokens consumed (v2).** `--card`, `--haze`, `--ease-polish`,
  `--dur-wipe` (700ms), `--parallax-glass` (0.40),
  `--parallax-solution` (0.92).

### 6.11 Cabinet navigation

- **What & why.** The cabinet head: a mahogany rail carrying
  the maker's nameplate and the section plates — Instruments,
  Reading the Glass, The Forecast, Commission — each a small
  brass plate (§6.6) that is a real link. It belongs because a
  cabinet is entered at its head, and the navigation should be
  the maker's own plates screwed to his own wood, not a web
  header that wandered in.
- **Structure.** A sticky mahogany bar (64px) at the page top:
  left, the maker's plate (name + est. line, a link home);
  right, the section plates in Caslon 15px on brass, the
  current section's plate filled brighter with its state word
  printed beneath in mono 10px. On mobile the plates collapse
  behind a single brass "Cabinet" plate that opens a mahogany
  panel listing the sections as plates in a column — the one
  licensed overlay in the theme (§11).
- **Motion spec.** The bar sticks with no animation of its own
  (a cabinet head does not bounce). On scroll past 140px it
  compresses to 48px over 250ms `--ease-settle` and the
  nameplate's est. line retires. The current-section plate
  migrates by scrollspy: the incoming plate fills over 300ms
  while the outgoing returns to matte, with the §6.8 polish
  traversing the incoming plate once. Internal anchor jumps run
  §6.15's clouding only for cross-cabinet jumps (hero ↔ form);
  short hops scroll natively under the barometric heaviness.
- **States.** *Rest:* matte plates, current filled. *Hover:*
  polish (§6.8). *Focus:* polish + brass-deep outline (§11);
  an un-etched plate fills instantly (§6.6). *Active:* press —
  the plate takes a 1px settle and its engraving deepens 25%
  (§6.8 active). *Current:* filled plate + state word.
  *Disabled:* n/a. *No-JS:* all plates printed filled; the
  mobile panel is a plain list (the toggle is JS-only; without
  JS the list stands open).
- **Content merge.** The plates name the cabinet's actual
  sections and carry the weather each section is under — the
  nav is the cabinet's index and its forecast in one object.
- **Failure fallback.** If scrollspy fails, no plate is marked
  current — an honest absence, never a wrong section lit.
  Sticky failure degrades to a static head; the plates remain
  links.
- **Reduced-motion variant.** No compression, no polish
  traverse (darkening only, §6.8), current plate swaps
  instantly.
- **Performance budget & mobile variant.** The bar is one
  sticky element; scrollspy is an IntersectionObserver, not a
  scroll handler. Mobile: the column panel (§ above), plates
  48px touch height.
- **Choreography timeline (v2).** Scroll >140px → 250ms
  compression. Section boundary crossed → outgoing plate
  mattes (300ms) as incoming fills + polishes (500ms traverse
  within the fill). Anchor click (long jump) → §6.15 clouding
  450ms → scroll → dissolve 600ms → focus lands on the target
  heading.
- **State matrix (v2).** *Rest:* as States. *Hover:* polish.
  *Focus:* polish + outline, instant fill. *Active:* press
  settle. *Scrolled-past:* n/a (the bar is the frame).
  *Disabled:* n/a. *Touch:* plates at 48px; tap = navigate;
  press-darkening 200ms (§6.8).
- **Breakpoints (v2).** ≥1200px: full bar, nameplate + 4
  plates. 768–1199px: plates lose their state words (kept in
  the dial, §6.4). <768px: Cabinet plate + panel.
- **Edge cases & failure modes (v2).** *Many sections:* the
  plate row caps at 5; a sixth section joins the mobile-style
  panel at all widths rather than shrinking plates below
  legibility. *Long section names:* plates are one line (§6.6's
  refusal) — names are shortened at build, never shrunk.
- **Accessibility spec (v2).** A real `<nav>` with a list of
  links; `aria-current="location"` on the current plate's link;
  the mobile panel is a disclosure pattern with
  `aria-expanded`, Esc closes, focus returns to the Cabinet
  plate. Touch targets ≥48px on mobile, ≥40px desktop.
- **Tokens consumed (v2).** `--mahogany`, `--mahogany-deep`,
  `--brass`, `--brass-bright`, `--card`, `--ease-settle`,
  `--dur-nav-fill` (300ms).

### 6.12 Instrument cards

- **What & why.** The catalogue: each instrument (storm glass,
  barometer, ship's set) is a card in a glass-fronted cabinet
  cell — a framed plate image (§6.17), its brass nameplate
  (§6.6), its reading line (what it measures, in mono), its
  maker's note in Caslon, and its price. The cards tilt ≤3°
  like plates lifted from the cabinet when handled. It belongs
  because the catalogue is the cabinet's middle shelves: the
  visitor lifts each instrument out, looks, and puts it back.
- **Structure.** A grid of cells (3 across ≥1200px). Each cell:
  glass surround over card, the plate image in its brass frame,
  nameplate, mono apparatus lines (RANGE / SOLUTION / CASE —
  the instrument's facts), a two-line Caslon note, price in
  mono, and one link ("Examine") to the instrument's detail.
  One cell in each row is the **honest cell**: the instrument
  currently out of true — its note says so ("This batch reads
  high. We are re-mixing.") and its link is absent, replaced by
  the maker's line. Honesty is stocked on the shelf, not buried
  in a footnote.
- **Motion spec.** Cells settle in on first view: 70ms stagger,
  each rising 8px and settling over 450ms `--ease-settle` with
  its plate etching (§6.6) in the same beat. Tilt: on
  pointermove over a cell at ≥1200px, the cell rotates toward
  the pointer ≤3° (rotateX/rotateY from pointer position,
  lerp 0.18 in the shared loop) with its frame's reflection
  (§6.10) shifting against the tilt; on leave it settles back
  over 600ms. Tilt is frozen while focus is within the cell.
- **States.** *Rest:* seated in the cell. *Hover:* tilt +
  frame polish (§6.8). *Focus-within:* no tilt; the Examine
  link takes its outline. *Active:* the link's press (§11).
  *Scrolled-past:* settled, etched. *Out of true:* the honest
  cell never tilts — you do not handle an instrument the maker
  has condemned — and carries no link. *Disabled / no-JS:*
  cells printed seated, plates filled.
- **Content merge.** The card's apparatus is the instrument's
  real specification; the tilt lifts the object the copy
  describes. The honest cell merges the theme's thesis (§1)
  into the catalogue's middle: the maker's doubt is merchandise
  information.
- **Failure fallback.** Watchdog: cells not settled within
  1400ms of entering view snap seated. No-JS: all seated.
- **Reduced-motion variant.** No settle, no tilt. Cells print
  seated; hover gives the frame polish's darkening only.
- **Performance budget & mobile variant.** Tilt transforms on
  the hovered cell only. Mobile: no tilt (touch has no hover);
  cells stack 1-up under 768px, 2-up at 768–1199px; settle
  stagger cut, cells print seated if the row is above the fold
  on load.
- **Choreography timeline (v2).** Row enters → cells settle at
  70ms stagger, plates etch within the settle → pointer enters
  a cell → tilt lerps in (0.18) → pointer leaves → 600ms settle
  home. Examine click → §6.15 clouding to the detail page.
- **State matrix (v2).** *Rest:* seated. *Hover:* tilt ≤3° +
  polish. *Focus:* tilt frozen, outline on the link. *Active:*
  link press. *Scrolled-past:* seated. *Disabled / no-JS:*
  seated, filled. *Touch:* no tilt; tap = the link.
- **Breakpoints (v2).** ≥1200px: 3-up, tilt on. 768–1199px:
  2-up, tilt ≤2°. <768px: 1-up, no tilt, plates 36px (§6.6).
- **Edge cases & failure modes (v2).** *A row of one:* the
  single cell takes the row's left cell, never centred — a
  cabinet shelf is filled from the left. *Long maker's notes:*
  notes are capped at two lines at build (§12); a longer note
  belongs on the detail page. *Missing image:* the frame holds
  the instrument's engraved outline plate (§6.17's fallback) —
  never a broken-image icon in a brass frame.
- **Accessibility spec (v2).** Each cell is an `<article>` with
  the instrument's name as its heading; the whole cell is not a
  link (only Examine is), so AT users get the apparatus as
  text, not as one long link label. Tilt is pointer-only and
  never moves content under a keyboard user.
- **Tokens consumed (v2).** `--card`, `--brass`, `--brass-deep`,
  `--storm`, `--storm-soft`, `--ease-settle`, `--dur-card-settle`
  (450ms), `--tilt-max` (3deg).

### 6.13 Readings & forecast counters

- **What & why.** The maker's numbers: pressure readings in
  inches and forecast counts ("instruments in the cabinet: 14;
  glasses filled this season: 61") that count to their values
  on entry. It belongs because a maker's page must show its
  figures the way its instruments show them — arriving at the
  true value by travel, not by appearing — and because every
  figure here is one of the law's printings (§1): the pressure
  counter prints `pressureAt` at its position; the counts count
  things that exist on the page or in the maker's stated record.
- **Structure.** Reading blocks sit in the maker's section and
  the cabinet foot: a mono figure (28px) with its mono caption
  beneath. Two kinds, kept apart: **live readings** (the
  pressure at this point of the page — bound to the loop, §6.4's
  value, printed not counted) and **record counts** (fixed
  figures from the maker's record or the DOM: instruments
  counted from §6.12's cells, forecast chapters counted from
  §6.2's sections). A count's source is printed in its caption
  ("counted from the shelves above") — a figure without a
  source line is refused at build (§12).
- **Motion spec.** Record counts animate once, on entry at 40%
  visibility: from the *previous figure in the same column*
  (or from 60% of value for the first) to the true value over
  900ms `--ease-settle`, digits rolling in the units column
  only — a barometer's travel, not a slot machine. Live
  readings never count; they print and update with §6.4's
  120ms throttle. Counts never re-run on re-entry.
- **States.** *Uncounted* (JS-armed: figure at its start value)
  → *counting* → *counted* (rest, true value). *Hover/focus:*
  none. *Scrolled-past:* counted. *Disabled / no-JS:* figures
  print at true value — the DOM carries the truth; the count
  is JS theatre over it.
- **Content merge.** The figures are the maker's record of the
  cabinet the visitor is standing in — two of the three record
  counts are literally counted from this page's shelves and
  chapters, so the numbers describe the room, not a marketing
  quarter.
- **Failure fallback.** Watchdog at 1600ms: any count mid-travel
  snaps to its true value. A count whose DOM source is missing
  (a shelf removed in a CMS) renders its caption without a
  figure rather than inventing one — the absent number is the
  honest state (§9 failure 7).
- **Reduced-motion variant.** Figures print at true value. No
  travel.
- **Performance budget & mobile variant.** Counting animates
  `textContent` at most every 40ms per counter, ≤3 counters
  concurrently. Mobile: identical, figures at 24px.
- **Choreography timeline (v2).** Block at 40% → t=0 count
  begins from start value → 900ms travel, units digit leading
  → t=900 true value, caption's source line etches (§6.6
  timing at miniature scale: 300ms) → rest.
- **State matrix (v2).** *Rest:* true value. *Hover:* none.
  *Focus:* none. *Active:* n/a. *Scrolled-past:* true value.
  *Disabled / no-JS:* true value printed. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: figures 28px, in a 3-across
  record row. 768–1199px: 24px, 2-across. <768px: 24px,
  stacked; travel shortens to 700ms.
- **Edge cases & failure modes (v2).** *Figure edited in the
  record:* record counts are hand-set from the maker's record
  (§8's worked figures) and audited at build against the
  caption's claim. *Zero:* a true zero prints as "0" and does
  not count (nothing travels to nothing). *Huge counts:* above
  999 the count travels in 1400ms and the figure is set with
  its thousands separator at every frame — a half-set "1,2 4"
  is a gate failure.
- **Accessibility spec (v2).** Counting figures are
  `aria-hidden` during travel with a visually-hidden true value
  beside them; AT always meets the settled figure. Live
  readings follow §6.4's throttled label, not a live region.
- **Tokens consumed (v2).** `--storm`, `--storm-soft`,
  `--brass-deep`, `--ease-settle`, `--dur-count` (900ms).

### 6.14 The commission form

- **What & why.** The conversion: a form for commissioning or
  ordering an instrument — name, direction (email), the
  instrument (chosen from §6.12's real catalogue as stampable
  rows, §11), case and engraving choices, and the message.
  Beneath it, in Caslon italic, the theme's anti-slop
  signature: **"The glass is often wrong. It is never dull."**
  It belongs because the form is the maker's order book — a
  ruled page in the cabinet's last panel — and the disclaimer
  under it is the maker's honesty at the exact moment of sale,
  which is where honesty costs something and therefore where it
  means something.
- **Structure.** A ruled form on the card inside the final
  panel: mono labels above Caslon fields (§11's ruled-field
  treatment), the instrument choice as a list of plates that
  take a brass seal-slip when chosen (the §11 radio treatment),
  the submit as a brass plate-button "Enter in the order book".
  Success replaces the form with the order-book entry: the
  visitor's commission written back as a filled plate (§6.6's
  filled state) with its entry number — derived from the count
  of entries the page can show (the form's own stated sequence,
  e.g. "Entry № 58 in this season's book", where 58 is the
  season's printed count from §6.13's record + 1 — computed,
  never random).
- **Motion spec.** Field focus: the rule beneath inks from
  hairline to 2px `--brass-deep` over 200ms `--ease-etch`.
  Choice: the seal-slip stamps onto the chosen plate — 180ms
  `--ease-settle` press with the §6.8 darkening at 25%.
  Submit: the button presses (1px settle), the form's panel
  clouds lightly (§6.15's clouding at 40% strength, 450ms) and
  clears onto the entry over 600ms. Errors: the field's rule
  turns `--storm` and the maker's note appears in the margin in
  his voice (§12) — no shaking, no red; a maker corrects an
  order book in pencil, not in alarm.
- **States.** *Rest:* ruled, empty, the disclaimer beneath.
  *Focus:* rule inking. *Filled:* rules rest at 60% ink.
  *Error:* storm rule + margin note; input preserved, always.
  *Submitting:* button settled, panel clouding. *Success:* the
  entry plate. *Disabled:* the submit is never pre-disabled —
  an empty order book entry is an error the maker answers, not
  a button withheld (§11).
- **Content merge.** The form's choices are the catalogue's
  instruments; its entry number is the record's next number;
  its disclaimer is the theme's thesis at the point of sale.
  Nothing in the form is generic: a field that could belong to
  any checkout has been re-cut as an order-book line or
  refused (§11).
- **Failure fallback.** The form is a real form: without JS it
  submits natively and the entry is returned by the server as
  a printed page. JS validation is an enhancement layered over
  HTML validation, never the only gate. A failed submission
  (network) keeps every field's content and prints the maker's
  line: "The book did not take the entry. Your words are still
  on the page — try the post again."
- **Reduced-motion variant.** No clouding; the entry replaces
  the form instantly. Rule-inking and stamping become instant
  state changes.
- **Performance budget & mobile variant.** The form is DOM and
  CSS only; clouding reuses §6.15's layer at reduced opacity.
  Mobile: single column, fields 48px, the seal-slip rows full
  width; the disclaimer stays directly beneath the submit at
  every breakpoint — it may never be footnoted away.
- **Choreography timeline (v2).** Focus → rule inks 200ms →
  choice → slip stamps 180ms → submit → press 120ms → cloud
  450ms → entry plate etches-filled (§6.6 compressed: etch
  300ms + fill 200ms) → the cabinet foot (§6.16) updates its
  entry count by one, live, in the same beat.
- **State matrix (v2).** *Rest:* as States. *Hover:* brass
  parts polish (§6.8). *Focus:* rule ink + outline (§11).
  *Active:* press settles. *Scrolled-past:* n/a. *Disabled:*
  submit never disabled; a *chosen* instrument that is out of
  true (§6.12) is unchoosable — its row carries the maker's
  line instead of a slip. *Touch:* rows at 48px, stamps on tap.
- **Breakpoints (v2).** ≥1200px: two-column order book (fields
  left, instrument rows right). 768–1199px: single column,
  rows above fields. <768px: single column, disclaimer
  immediately under the submit.
- **Edge cases & failure modes (v2).** *Engraving text too
  long:* the engraving field counts characters against the
  plate's real capacity (24) and says so in the maker's voice
  before the limit, not after. *Returning visitor:* the form
  does not pre-fill from storage — an order book starts each
  sitting blank; the success entry, once made, persists in the
  DOM for the session. *Double submit:* the press disables
  itself at first activation (the one licensed disabling —
  after the act, not before it).
- **Accessibility spec (v2).** Labels always visible (mono,
  above); errors are text beside the field with
  `aria-describedby`, never colour alone; the storm rule is a
  cue, not the message. Focus order follows the order book's
  reading order; the success entry is a `role="status"` region
  that announces "Entered in the order book as № 58."
- **Tokens consumed (v2).** `--card`, `--brass`, `--brass-deep`,
  `--storm`, `--storm-soft`, `--ease-etch`, `--ease-settle`,
  `--dur-rule-ink` (200ms).

### 6.15 Empty-glass skeleton & the clouding transition

- **What & why.** Two linked instruments. The **skeleton**: a
  panel whose content has not arrived renders as empty glass
  under haze — the panel's true shape, unfilled, with the
  maker's line "The glass is being filled." The **clouding**:
  navigation between pages (or §6.11's long jumps) clouds the
  glass with crystals over 450ms, changes the page beneath the
  frost, and dissolves clear over 600ms on arrival. They belong
  together because both are the same fact — glass with nothing
  behind it yet — at two scales: a panel waiting, and a page
  turning.
- **Structure.** Skeleton: the panel's glass surround and card
  outline at true size, the card carrying 3–5 haze bars at the
  copy's real line-heights (the skeleton is drawn from the
  layout, not a generic shimmer block), `aria-busy="true"` on
  the region. Clouding: a fixed glass layer over the viewport
  (haze wash + a crystal field identical in vocabulary to
  §6.2's) whose density animates; beneath it, nothing of the
  old page is interactive (`inert` during the cloud).
- **Motion spec.** Skeleton: bars breathe at 4% opacity over a
  2400ms cycle (the solution settling, not a shimmer sweep —
  no highlight travels; §9 failure 8 refuses the shimmer).
  Content arriving cross-fades in over 300ms as the bars
  dissolve. Clouding: density climbs to the Storm ceiling
  (30-branch equivalent) over 450ms `--ease-grow`; the swap
  happens at full cloud; the new page dissolves from Storm
  density to its own top-of-page state (Fair) over 600ms.
  Hard cap: if the new page is not ready in 3000ms, the cloud
  thins to Change and waits there — a visitor is never held
  behind full frost.
- **States.** *Skeleton:* loading → resolving → content.
  *Clouding:* clear → clouding → clouded (swap) → dissolving
  → clear. *Hover/focus:* during clouding, focus is held and
  restored to the target heading after the dissolve; during
  skeleton, the region is inert to AT until resolved.
  *Disabled / no-JS:* no skeleton states are JS-rendered (the
  server ships content or a printed "not in the cabinet"
  notice); navigation is native, unclouded.
- **Content merge.** The skeleton is the panel's own shape —
  the visitor sees the cabinet with one glass empty, which is
  information about the room. The clouding is the weather
  doing the page-turn: the same crystals that forecast are the
  ones that frost the glass between rooms.
- **Failure fallback.** A skeleton unresolved after 6000ms
  resolves to the maker's printed line in the card — "This
  glass has not been filled. The maker has been told." — with
  a retry link; an empty panel may never sit breathing forever.
  A failed navigation leaves the cloud dissolved and the old
  page intact.
- **Reduced-motion variant.** Skeleton bars are static; content
  swaps instantly. Clouding becomes a 150ms crossfade with no
  crystal growth.
- **Performance budget & mobile variant.** The cloud layer is
  one fixed composited layer, built once and reused; skeleton
  bars are CSS only. Mobile: clouding caps at 20-branch
  equivalent density; skeleton bars reduce to the card's first
  three lines.
- **Choreography timeline (v2).** Nav click → t=0 cloud climbs
  → t=450 full cloud, swap/focus moved → new page ready →
  dissolve 600ms → clear, focus on target heading. Skeleton:
  region mounts empty → content resolves → bars dissolve
  300ms as content fades in → `aria-busy` clears.
- **State matrix (v2).** *Rest:* clear / content. *Hover:*
  none. *Focus:* held through clouding, restored after.
  *Active:* the click that starts it. *Scrolled-past:* n/a.
  *Disabled / no-JS:* native. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px and 768–1199px: full cloud.
  <768px: 20-branch cap, dissolve 500ms.
- **Edge cases & failure modes (v2).** *Back button during
  clouding:* the cloud dissolves immediately (100ms) onto
  whichever page history delivers — the frost never argues
  with the browser. *Slow content in one panel:* only that
  panel skeletons; the rest of the cabinet is live. *Prefetch
  hit:* if the target is instant, the cloud still plays its
  minimum 700ms total — a transition faster than its own
  grammar reads as a glitch, not as speed.
- **Accessibility spec (v2).** Skeleton regions use
  `aria-busy` and are labelled by their panel's plate; the
  cloud layer is `aria-hidden` and focus management is as
  §6.11's timeline. Reduced-motion and vestibular safety per
  the variant above.
- **Tokens consumed (v2).** `--haze`, `--haze-deep`, `--card`,
  `--ease-grow`, `--dur-cloud` (450ms), `--dur-dissolve`
  (600ms).

### 6.16 The cabinet foot

- **What & why.** The footer: a mahogany-deep ground carrying
  the maker's colophon, the cabinet's index repeated as plain
  links, and — the footer's signature — the **pressure at the
  bottom of the page**, printed as a reading: "AT THE FOOT —
  28.61 IN — STORM." It belongs because the descent must be
  *closed* by the instrument: the visitor who reaches the foot
  is told, in the record's voice, exactly how far the weather
  fell to get them there. The footer is the barometer's final
  printing (§1), and it must agree with the needle (§6.4) to
  the second decimal.
- **Structure.** `--mahogany-deep` ground, `--card` text
  (8.96:1 family per §2, computed against mahogany; against
  mahogany-deep the same text measures higher still). Three
  columns: the colophon (maker, town, est. year, the line "Set
  in Libre Caslon Text & IBM Plex Mono"), the cabinet index
  (text links, §6.11's sections), and the record column: the
  foot reading, the season's entry count (§6.13 — which
  §6.14's success increments live), and the maker's standing
  line. A brass hairline rule draws across the footer's head
  as it enters (§6.7's draw at footer scale).
- **Motion spec.** The rule draws 600ms `--ease-etch` on entry.
  The foot reading does not animate — it *is* the settled
  value, printed; if the visitor scrolls back up, the footer
  leaves view with the needle, and both resume their travel.
  The entry count updates instantly on §6.14's success (a
  figure changing in a record does not celebrate).
- **States.** *Rest:* printed. *Hover:* links take the brass
  polish's darkening (§6.8) with a card underline. *Focus:*
  outline in card. *Scrolled-past:* n/a — the foot is the end.
  *Disabled / no-JS:* the reading prints as the track's end
  value (28.61 IN — STORM) because that is where the foot
  stands on the track, JS or none.
- **Content merge.** The footer's record column is generated
  from the same values as the needle, the counters and the
  form — four printings, one pressure (§1). The colophon's
  type credit is the page's actual typography (§3).
- **Failure fallback.** If the loop is dead, the foot reading
  still prints 28.61 IN (it is a property of position, computed
  at build for the foot). The entry count falls back to the
  season's printed figure.
- **Reduced-motion variant.** The rule prints drawn; all else
  is already still.
- **Performance budget & mobile variant.** Static but for the
  rule draw. Mobile: columns stack — colophon, record, index —
  the record second because the reading is the footer's point.
- **Choreography timeline (v2).** Footer enters → rule draws
  600ms → the record column is already printed (no stagger —
  records do not perform) → rest.
- **State matrix (v2).** *Rest:* printed. *Hover:* link
  darkening + underline. *Focus:* outline. *Active:* press
  (§11 link behaviour). *Scrolled-past:* n/a. *Disabled /
  no-JS:* printed at track values. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: three columns. 768–1199px:
  two (colophon + record; index as a row beneath). <768px:
  stacked as above.
- **Edge cases & failure modes (v2).** *A page with no storm
  chapter* (a short cabinet page): the foot reading prints the
  track's end wherever the track ends — the function, not the
  chapter, decides (§6.2). *Entry count disagreement:* the
  footer's count and §6.13's are one DOM value printed twice;
  a build that hard-codes either fails §10.
- **Accessibility spec (v2).** A real `<footer>` with labelled
  link lists; the reading is text. Contrast per §2 against
  mahogany-deep exceeds the mahogany figures.
- **Tokens consumed (v2).** `--mahogany-deep`, `--card`,
  `--brass`, `--ease-etch`, `--pressure-min` (28.61).

### 6.17 Framed plates

- **What & why.** Images — the instruments, the workshop, the
  maker's bench — live in brass-and-glass frames: a brass
  frame, a glass reflection over the image (§6.10's layer at
  plate scale), and the image settling into its frame as it
  centres. It belongs because a cabinet's pictures are plates
  behind glass; the frame is not a border decoration but the
  object's mounting, and the reflection on the glass is what
  tells the visitor there *is* glass.
- **Structure.** A `<figure>`: brass frame (6px brass, 2px
  card inset line), the image, a reflection layer clipped to
  the frame's interior, and a `<figcaption>` beneath in mono
  (the plate's catalogue line: subject, maker, year — every
  plate is catalogued, §12). Where an image is missing or
  fails, the frame holds the **engraved outline plate**: the
  subject's outline as an etched SVG (§6.6's vocabulary) with
  the caption intact — a frame in this cabinet is never empty
  and never shows a broken-image icon.
- **Motion spec.** Trigger: the figure centring. The image
  scales 1.06→1 over 700ms `--ease-settle` inside the frame's
  clip (scale-in-frame: the frame never moves, the plate
  settles into it), while the reflection layer recentres from
  its entry offset to its §6.10 parallax rest. Hover: the
  frame takes the polish (§6.8) and the reflection brightens
  4% — the visitor leans closer to the glass.
- **States.** *Unsettled* (JS-armed: image at 1.06, reflection
  offset) → *settling* → *seated* (rest). *Hover:* polish +
  reflection +4%. *Focus:* a figure that is a link seats
  instantly on focus. *Scrolled-past:* seated. *Disabled /
  no-JS:* seated at 1.0, reflection at rest offset.
- **Content merge.** The plates are the cabinet's evidence:
  the actual instruments §6.12 sells, the actual bench where
  §6.7's scale was engraved. Their captions catalogue them
  into the same record as everything else.
- **Failure fallback.** Image error → the outline plate swaps
  in (the caption already describes the subject, so the swap
  loses a photograph, not the information). Watchdog: a figure
  not seated within 1400ms of centring snaps seated.
- **Reduced-motion variant.** Seated at 1.0, reflection static;
  hover brightening removed (polish darkening only).
- **Performance budget & mobile variant.** Scale/transform on
  the image only; reflection is one gradient layer. Images are
  the page's main weight (§14): responsive sizes, the frame's
  aspect reserved so seating never shifts layout. Mobile: the
  settle shortens to 500ms; reflection offset halves.
- **Choreography timeline (v2).** Figure at centre approach →
  image settling 700ms, reflection recentring in the same
  beat → seated → joins §6.10's panel parallax if inside a
  panel.
- **State matrix (v2).** *Rest:* seated. *Hover:* polish +
  +4% reflection. *Focus:* instant seat if pending. *Active:*
  n/a (or the link's press). *Scrolled-past:* seated.
  *Disabled / no-JS:* seated. *Touch:* no hover; tap follows
  the link if any.
- **Breakpoints (v2).** ≥1200px: frames at catalogue sizes per
  §4. 768–1199px: identical, settle 600ms. <768px: full-measure
  frames, settle 500ms, reflection offset halved.
- **Edge cases & failure modes (v2).** *Slow image:* the frame
  and caption stand from first paint (the frame is the
  layout); the image fades in inside the frame when it lands,
  then seats — the settle never waits on the network beyond
  the watchdog. *Portrait vs landscape:* frame aspects are
  authored per plate at build; a CMS-swapped image with the
  wrong aspect is cropped by the frame's clip, never stretched.
- **Accessibility spec (v2).** Real `alt` text written as the
  catalogue would (subject, state, detail), not "image of";
  the reflection is `aria-hidden`; captions are text.
- **Tokens consumed (v2).** `--brass`, `--brass-bright`,
  `--card`, `--haze`, `--storm-soft`, `--ease-settle`,
  `--dur-plate-settle` (700ms).

### 6.18 The unfilled glass (404)

- **What & why.** The error page is an empty place in the
  cabinet: a glass panel with no instrument behind it, its
  plate reading "NOT IN THE CABINET", and the maker's line:
  "This instrument is not in the cabinet. The shelves that are
  are below." It belongs because a missing page in this world
  is a missing object — the cabinet admits the gap, labels it,
  and points at what exists. No weather is faked for the
  occasion: the empty glass holds the Change state, the
  cabinet's resting weather.
- **Structure.** One panel, Change density (11 branches,
  printed), an empty brass frame (§6.17) holding nothing but
  its reflection, the plate, the maker's line in Caslon, and
  three real links (Instruments, Reading the Glass, the
  Cabinet head) as plates. The needle (§6.4) prints at 29.94 —
  an error page is not on the weather track, and inventing a
  pressure for it would break the law (§1): the gauge rests at
  Change, as it does with JS off, for the same reason — *no
  reading is claimed where none was taken.*
- **Motion spec.** One licensed motion: as the page loads, a
  single wisp in the empty panel grows and dissolves once
  (§6.5's vocabulary, one 14s pass) — the solution in an empty
  glass is still solution. Nothing else moves. No rumble, no
  pin, no counters.
- **States.** *Rest:* the empty glass, wisp cycling once.
  *Hover:* the link plates polish (§6.8). *Focus:* outlines
  per §11. *Disabled / no-JS:* identical, wisp printed grown.
- **Content merge.** The 404's links are the cabinet's real
  shelves; its frame is §6.17's frame with the plate honestly
  absent — the same furniture, one object missing, which is
  the whole content of an error page told straight.
- **Failure fallback.** The page *is* a fallback; its own
  fallback is that every element on it is printed-state by
  default.
- **Reduced-motion variant.** The wisp prints grown; the page
  is still.
- **Performance budget & mobile variant.** The lightest page in
  the theme (≤120KB total, §14). Mobile: identical, stacked.
- **Choreography timeline (v2).** Load → plate filled (no
  etch — an empty shelf is not unveiled) → t=+800ms the wisp's
  single pass begins → t≈14800 grown and dissolved → rest.
- **State matrix (v2).** *Rest:* as States. *Hover:* polish on
  link plates. *Focus:* outlines. *Active:* link press.
  *Scrolled-past:* n/a (the page is one panel). *Disabled /
  no-JS:* printed. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: the panel centred at 760px.
  768–1199px: same. <768px: full-measure panel, frame above
  the plate.
- **Edge cases & failure modes (v2).** *A soft 404* (empty
  listing, no search results): the same furniture at panel
  scale inside the listing page — "Nothing is on this shelf"
  — with the shelf's real neighbours linked. *A visitor
  arriving from the storm chapter:* the needle still rests at
  Change; the error page does not inherit weather.
- **Accessibility spec (v2).** The heading is the plate's text
  as a real `<h1>` ("Not in the cabinet"); links are links;
  the empty frame's `alt` is "" with the maker's line as text
  beside it — the absence is described, not pictured.
- **Tokens consumed (v2).** `--card`, `--haze`, `--haze-deep`,
  `--brass`, `--storm`, `--ease-grow`.

## 7. Page application map

- **Home (the cabinet).** The canonical descent of §4:
  head, hero in the glass, instruments, the maker's section,
  forecast chapters, commission, foot. The full weather track
  (30.42 → 28.61) exists only here; other pages borrow states,
  not the track.
- **Listing (the shelves).** A category of instruments: the
  page holds one state throughout — chosen by the category
  (barometers sit in Change; ships' sets in Rain) — printed on
  its head plate. Cards per §6.12; the needle rests at the
  state's mid-pressure; an empty shelf is §6.18's furniture at
  panel scale. No descent, no rumble: a shelf is a place, not
  a journey.
- **Detail (one instrument).** The instrument's own page: its
  framed plates (§6.17) large, its apparatus as a record list
  (§11), its maker's note at length, and a small glass of its
  own in the margin whose density is the instrument's
  *character* (a storm glass's page carries its crystals at
  the density its own description claims — the claim and the
  specimen agree, or §10 fails it). Commission (§6.14) arrives
  with this instrument pre-chosen.
- **About (the maker).** The workshop: bench plates, the
  scale section (§6.7) may live here instead of home, the
  maker's history in Caslon, weather held at Fair-to-Change —
  the about page is the fair end of the cabinet; a maker's
  life is not a storm.
- **Commission / contact.** §6.14 as the page's whole body,
  weather at Change (the weather of writing a letter), the
  disclaimer beneath the form, the foot printing the Change
  reading.
- **The unfilled glass (404).** §6.18.
- **Print.** The cabinet on paper (§2): states print as their
  chapter's mid-state, the needle at the foot's reading, tap
  branches and cycle wisps print grown — a printed page is a
  cabinet with the weather held.

## 8. Worked examples

The maker throughout: **Hartnell & Vane, Instrument Makers**,
of Wapping — storm glasses, barometers and ships' sets since
1891. Figures below are the examples' record; a real build
substitutes its own record and re-derives every count (§6.13).

### 8.1 The hero — the name in the glass

*Build.* The cabinet head (§6.11) at 64px. Below it, the hero
panel: glass surround at Fair shading (undimmed), the card
inset 14px, and inside the solution layer the crystal field —
7 stems from the panel's lower-left and upper-right corners.
The `<h1>`: "Hartnell & Vane" at 54px Caslon, with the
standfirst on its plate beneath: "Instrument makers — storm
glasses, barometers & ships' sets" (mono, brass-deep, on the
plate's card inset). To the right of the card, inside the
glass, the hero instrument itself: a framed plate (§6.17) of
the No. 4 storm glass. The needle (§6.4) in the right rail
reads 30.42 IN — FAIR.

*Scroll timeline.* t=0 (load, fonts ready): stems begin,
120ms stagger, longest first. t=500: side-branches, 60ms
stagger. t≈1400: letter-touches walk "Hartnell & Vane" at
45ms per letter (14 touches — under the 24 cap). t≤2000:
field grown; the standfirst's plate etches (§6.6, 500ms) as
the growth completes. The visitor scrolls: pressure begins
its fall; the hero panel's density stays at its printed Fair
state (0–2 branches in the density field — the *ceremony*
field is the cycle's, and §6.5 adopts the hero panel while it
is centred, its wisps breathing at ±2 of the density figure).
t=scroll-past: the hero is a grown field and a printed name —
the cabinet's first room, visited.

### 8.2 Mid-page — the storm chapter and the rumble

*Build.* The third forecast chapter: "Sets for Ships" — the
maker's chapter on storm glasses for vessels, and why a glass
that is often wrong still sailed on every ship (it was never
the only instrument; it was the one that made the crew *look*
at the sky). The chapter's panels carry Rain shading deepening
into Storm across the pin wrapper (160vh). Inside the pin:
three panels — the set's plate (§6.17), the chapter's copy,
and the density field climbing 18 → 30 branches as pressure
falls 29.20 → 28.61. The chapter plate (§6.6) reads "SETS FOR
SHIPS — STORM". At the pin's end, the copy's final paragraph
concerns the night a glass fell from a cabin wall in the
Channel.

*Scroll timeline.* Pin begins: pressure 29.20, needle crossing
into STORM with its 1.5° overshoot and 400ms settle (§6.4).
Pin progress 0–0.9: density climbs by the function (branches
revealed by count, ≤2 fades per frame), surround dimming to
22%, the scroll's own lerp now at 0.08 — the visitor *feels*
the heaviness before they can name it. p=0.95: sentinel armed.
Conditions met (density 30 ≥ 27, P = 28.66 ≤ 28.75, flag
unset): as the final plate etches, the rumble fires — 120ms,
±2px, the whole pinned cabinet, once. The session flag sets.
Pin releases 300ms later into the chapter's tail: one quiet
panel at Storm density, and the maker's line: "The glass fell.
The ship did not." Scroll back up at any point: density
dissolves by the same queue, the needle rises, the rumble does
not repeat — the storm, once survived, is a story.

### 8.3 Conversion — the commission

*Build.* The final panel at Change shading (the descent's
weather spent, the form sits in the cabinet's resting state —
a deliberate local exception to §4's worsening order, declared
here: after the storm, the commission is written in calm, and
the panel's plate says so: "COMMISSIONS — CHANGE"). Left
column: the ruled form (§6.14) — name, direction, engraving
(24 characters, the plate's real capacity, counted live),
message. Right column: the instrument rows — No. 4 Storm
Glass (£240), No. 7 Barometer (£310), Ship's Set No. 2 (£520)
— each a plate that takes the seal-slip; the Ship's Set row
carries a fourth line: "Six weeks at the bench" (the making
time is part of the price's honesty). Beneath the submit, in
Caslon italic: "The glass is often wrong. It is never dull."

*Scroll timeline.* The panel centres: its plate etches
(§6.6), the form's rules stand at hairline. Focus enters the
name field: rule inks 200ms. The visitor chooses the No. 4:
the slip stamps (180ms, darkening 25%). A direction missing
its @ draws the margin note in the maker's voice: "That
direction will not carry — the @ is wanting." (§12), the rule
in storm, nothing erased. Submit: press, cloud at 40% (450ms),
clear (600ms) onto the entry plate: "Entered in the order
book as № 58 — No. 4 Storm Glass, for [the name as given]."
— 58 being §6.13's printed season count (57) + 1, computed
from the DOM record, and the cabinet foot's entry count
increments in the same beat (§6.16). The form's panel now
holds the entry; the disclaimer remains beneath it. It remains
beneath everything.

## 9. Anti-slop — what makes THIS theme look cheap

1. **The snow globe.** Crystals as generic particle glitter
   floating everywhere, including over text. *Cure:* crystals
   exist only as authored branch fields inside panels, clipped
   to margin zones (§1 glass law); a particle system anywhere
   on the page fails the gate.
2. **Generated crystal noise.** Procedural fractal branches
   that all look alike and grow like frost on a window ad.
   *Cure:* branch paths are authored vector data per panel
   (§6.1, §6.2); two panels' fields may not share a path.
3. **The lying gauge.** A needle, a reading and a density that
   tell three different weathers (the classic build: needle
   scrubbed, density hand-tuned, reading static). *Cure:* one
   function, four printings (§1); §10 samples five scroll
   positions and compares all four.
4. **Fair-weather layout in the storm.** A storm chapter with
   the same airy padding as the hero — the forecast says storm,
   the layout says spring. *Cure:* §4's density law (96/72/56px
   padding by band) is checked in the gate's screenshots.
5. **The repeated rumble.** The shake as a reusable "delight"
   on buttons, section entries, add-to-cart. *Cure:* one
   shake, one place, once per session (§6.3); any other
   translate-shake in the CSS is a gate failure by grep.
6. **Numbers in Caslon.** Prices and pressures set in the
   display face because it "looks classier". *Cure:* §3 law 1
   — readings are mono; the gate font-audits every figure.
7. **The invented figure.** A count ("over 500 ships
   supplied") with no source, or a counter whose DOM source
   was deleted still printing its number. *Cure:* §6.13's
   source-line rule; a figure without a source renders no
   figure.
8. **The shimmer skeleton.** A grey shimmer sweep copied from
   a SaaS kit. *Cure:* §6.15's breathing haze bars drawn from
   the real layout; no travelling highlight exists in the
   theme.
9. **Brass everything.** Brass buttons, brass links, brass
   text, brass hover states on card controls — the cabinet
   becomes a trumpet. *Cure:* brass is for plates, frames,
   needles and the submit (§11); text links on card are ink
   with rules, and §10 counts brass-text violations.
10. **The trustworthy storm glass.** Copy that sells the glass
    as a reliable forecast ("know tomorrow's weather today!").
    *Cure:* §12's voice rules and the §6.14 disclaimer are
    load-bearing; marketing copy that overclaims is a gate
    failure, not a tone issue.
11. **Weather by colour alone.** States conveyed only by the
    surround darkening, invisible to a visitor who can't
    perceive it. *Cure:* every state is also a word on a plate
    (§6.2) and a figure in the record (§6.13).
12. **The helpful cursor.** A custom cursor — a little needle,
    a droplet — following the visitor. *Cure:* refused (§5);
    the system cursor, and the tap (§6.9) answers clicks in
    the glass, not on the pointer.

## 10. Quality gate

Blocking unless marked (A = advisory):

- [ ] **One-pressure audit:** at five sampled scroll positions
  (top, quarter, mid, storm pin mid, foot), needle angle,
  printed reading, panel branch counts and state words all
  agree with `pressureAt` and the §1 thresholds — density
  within ±2 branches (the §6.5 cycle's allowance), figures to
  two decimals.
- [ ] **Glass law:** no crystal path intersects any text box
  on any tested page (automated overlay check on screenshots
  at three breakpoints); tap-branches clamp to margin zones.
- [ ] **Printed-state test:** with JS disabled, every page is
  complete — headline printed, fields grown, plates filled,
  scale drawn, needle at its honest printed position, forms
  working, counters at true value.
- [ ] **Watchdog test:** with the rAF loop frozen, every armed
  element reaches its printed state within its stated fallback
  (hero 2600ms, plates 1200ms, scale 2200ms, counters 1600ms,
  cards 1400ms).
- [ ] **Rumble audit:** exactly one shake in the built CSS
  (grep for the rumble keyframes), fired once per session,
  suppressed under focus-within and reduced motion; amplitude
  ≤2px.
- [ ] **Contrast audit:** text pairings measured against §2's
  table *in the Storm state*; no text on haze; no brass text
  below 20px; plate small print only on card insets.
- [ ] **Motion audit:** easings grep — only the five named
  easings in built CSS; pins per page ≤1; marquee and
  blur-to-sharp absent; ambient systems ≤2 and both pausing
  off-screen.
- [ ] **Figure-truth audit:** every printed figure traces to
  the declared function, the DOM, or the maker's record with
  its source line present; the §6.14 entry number rehearsed
  against the record count (0, 1 and 3 entries).
- [ ] **Reduced-motion pass:** full page walk with
  `prefers-reduced-motion`: weather held at Change, plates
  filled, no pin, no rumble, no cycle, state information
  present as print on every chapter.
- [ ] **Disclaimer test:** the commission form's page carries
  "The glass is often wrong. It is never dull." directly
  beneath the submit at every breakpoint.
- [ ] (A) **Five-second test:** a first-time viewer, shown the
  hero for five seconds, can say "an instrument maker" and
  "the name is inside a glass" unprompted.
- [ ] (A) **Heaviness check:** a tester scrolling the descent
  notices the page grow heavier into the storm chapter
  without being told why.

## 11. Component inventory

Every component a real site in this theme needs, with its
themed treatment. Global rules: radius 2px on plates and
frames only (brass is rolled, not rounded); no shadows except
a panel's mounting shadow on the mahogany (`--mahogany-deep`
at 30%, offset 0/8px, blur 0 — a cabinet's shadow is a line);
focus ring is a 2px `--brass-deep` outline offset 3px on card,
a 2px `--card` outline offset 3px on mahogany.

- **Buttons.** *Primary:* the brass plate-button — brass
  ground, `--card` label in Caslon 15px (4.08:1 at display
  size, §6.6's ruling), 48px tall, engraved hairline border.
  Press: 1px settle + engraving darkens 25% (`--ease-settle`
  150ms) — buttons are *pressed into the order book*, not
  clicked. *Secondary:* a card button — card ground, storm
  label, brass hairline border. *Text links on card:* storm
  text with a hairline rule that inks to brass-deep on hover.
  *Refused:* pill buttons, gradient buttons, floating action
  buttons.
- **Inputs & textarea.** Ruled fields (§6.14): transparent on
  card, 1px `--storm-soft` hairline beneath, inking to 2px
  `--brass-deep` on focus over 200ms `--ease-etch`. Labels
  always visible above, mono 12.5px. No floating labels, no
  placeholder-as-label. Textarea is a ruled page (28px line
  pitch matching its line-height).
- **Selects.** Refused as native dropdowns in the cabinet:
  choices are *rows that take the seal-slip* (below). Where a
  platform forces a native select (a checkout's country), it
  is styled as a ruled field and accepted as a foreign object,
  min 48px.
- **Radios & checkboxes.** Radio = a plate row that takes the
  brass seal-slip when chosen (§6.14). Checkbox = a small
  square seal-slip that fills with a brass stamp when checked.
  Never the platform's round radio in a coloured ring.
- **Tables.** **Refused** as data grids inside panels. The one
  licensed table is the barometer band table (§6.7): real
  `<table>`, mono figures, hairline rules — a scale's table is
  part of the instrument. All other tabular matter is set as
  record lists (§6.13's pattern).
- **Badges & tags.** Refused as coloured pills. A status is a
  line in the record ("Out of true — re-mixing", §6.12) or a
  state word on a plate. No count bubbles.
- **Alerts.** A *margin note* (§6.14): a `--card-deep` slip at
  the head of the panel it concerns, in the maker's voice, with
  a brass rule at its left for notices and a storm rule for
  errors. Nothing pushes content mid-read; nothing vanishes.
- **Modals.** Refused. A work's enlargement is its detail page
  (§7); a confirmation is §6.14's entry. The one overlay is
  the mobile nav panel (§6.11), a mahogany board of plates.
- **Toasts.** Refused outright. Feedback is written where it
  belongs: stamps on choices, entries in the book, records in
  the foot.
- **Tabs.** Refused. Chapters are panels in sequence; category
  views are separate shelves (§7), reached by plates.
- **Accordions.** One licensed form: care-and-keeping clauses
  on a detail page open as *drawers in the cabinet* — the
  clause's body settles in under its plate over 300ms
  `--ease-settle`, one open at a time. Never for primary
  content.
- **Pagination.** The clouding (§6.15) with a printed apparatus
  line — "Shelf 2 of 3" — and named next/previous plates.
  Numbered pills refused.
- **Breadcrumbs.** Refused. The cabinet is shallow; §6.11's
  plates and the detail page's shelf line carry orientation.
- **Search.** Where a large catalogue needs it, it lives on
  the listing page as a ruled field (§6.14's treatment) whose
  results re-lay the shelves; the query is a line in the
  order book, never an expanding icon.
- **Loader.** The empty glass (§6.15). Spinners refused in all
  forms — a wheel in a cabinet is a toy.
- **Progress.** The needle (§6.4) is the only progress
  component. No bars, no percentages, no step indicators — a
  commission is one order-book page (§6.14), not a wizard.
- **Cards.** §6.12's cabinet cells. No other card exists.
- **Tooltip.** Refused. Anything worth saying is printed on a
  plate or in the apparatus.
- **Avatar / byline.** The maker is represented by his
  nameplate (§6.11) and his bench plates (§6.17), never a
  circular headshot.

## 12. Content & copywriting voice

Two registers, kept apart as strictly as the two typefaces
(§3 law 1).

**The Maker** (Caslon contexts — headlines, chapter prose, the
disclaimer): first person plural of the workshop ("we"), plain,
dry, honest about doubt. Headlines name the thing or the
chapter, never a promise: ✓ "Sets for ships" / ✓ "How to read
the glass" / ✗ "Know tomorrow's weather today" / ✗ "The last
barometer you'll ever buy". The maker's doubt is stated as
fact, not apology: ✓ "The glass is often wrong. It is never
dull." / ✓ "This batch reads high. We are re-mixing." / ✗
"Results may vary!" — the exclamation alone fails it (§9.10).

**The Record** (mono contexts — labels, readings, apparatus,
errors): terse, tabular, sourced. Labels name the measurement:
✓ "RANGE — 28 TO 31 IN" / ✓ "AT THE FOOT — 28.61 IN — STORM" /
✗ "Amazing specs". Every figure carries its source or its
function (§6.13): ✓ "INSTRUMENTS IN THE CABINET — 14 (counted
from the shelves)" / ✗ "Over 500 ships supplied". Error voice
is the maker correcting the book, in pencil: ✓ "That direction
will not carry — the @ is wanting." / ✓ "The engraving takes
24 letters. This asks for 31." / ✗ "Invalid input!!" Empty
states are admissions with directions: ✓ "Nothing is on this
shelf. The shelves that are are below." (§6.18) / ✗ "Oops!
Nothing here".

**Fixed strings (verbatim, never paraphrased).** The
disclaimer: "The glass is often wrong. It is never dull." The
skeleton line: "The glass is being filled." The unfilled line:
"This glass has not been filled. The maker has been told." The
404 plate: "NOT IN THE CABINET". The foot reading's form: "AT
THE FOOT — [P] IN — [STATE]".

**Banned words.** Revolutionary, game-changing, smart (of an
instrument), guaranteed (of any forecast), never-miss,
crystal-clear (the pun is beneath the maker), and any
percentage applied to the glass's accuracy. **Owned words.**
Glass, plate, shelf, cabinet, reading, true (as in *out of
true*), dull (only in the disclaimer), the bench, the book.

## 13. Full-page scroll choreography map

The home page, top to foot, in order. Pressures are the
track's; densities are §6.2's function of them.

1. **Cabinet head** (P 30.42, FAIR): plates filled or etching
   on first view; needle at FAIR; heaviness lerp 0.14.
2. **Hero panel** (§8.1): crystal ceremony on load (2000ms);
   on scroll-away, the field is grown, the name printed.
3. **Hero's tail:** the standfirst plate etches; §6.5 adopts
   the hero panel while it centres (wisps at ±2 of density).
4. **The instruments** (P falls 30.42 → 30.05, FAIR → CHANGE at
   the chapter's second row): cards settle in rows of three,
   70ms stagger; the honest cell sits in the second row; the
   needle overshoots once at the CHANGE threshold.
5. **The maker's section** (P ≈ 29.94, CHANGE): the scale
   draws (1600ms) and its needle sweeps to the live reading;
   the band table prints; record counts travel to their
   figures (§6.13).
6. **Forecast chapter I — Clear goods** (P 29.90 → 29.80,
   CHANGE held at its fair edge): panels at Change density
   thinning toward Clear as the copy describes fair-weather
   keeping — the one place the track's fall is locally
   flattened, declared in the chapter's plate ("HELD AT
   CHANGE — THE CLEAR CHAPTER"). Density still agrees with
   the printed reading at every point (§10 samples it).
7. **Forecast chapter II — Changeable** (P 29.80 → 29.20,
   CHANGE → RAIN): wisps thicken; the scroll lerp drops to
   0.08 at the RAIN threshold; plates re-print their words.
8. **Forecast chapter III — the storm** (§8.2): the pin;
   density 18 → 30; dimming to 22%; the rumble at p=0.95 if
   earned; the tail panel and "The glass fell. The ship did
   not."
9. **The commission** (§8.3): weather declared at CHANGE on
   its plate; the form's rules ink under focus; the disclaimer
   beneath the submit.
10. **The cabinet foot** (§6.16): the brass rule draws; the
    record prints "AT THE FOOT — 28.61 IN — STORM"; the entry
    count agrees with §6.13 and §6.14.
*Reverse pass:* every scrubbed value reverses by the same
functions — density dissolves, the needle rises, heaviness
lifts at the thresholds — except the three things that are
acts, not states: etched plates stay filled, the rumble stays
spent, tap-branches stay grown. *Jump scroll:* the loop's
lerps traverse the skipped weather at their own rates (~900ms
for the needle, ~1.2s for density); watchdogs, not the jump,
decide any ceremony's completion.

## 14. Whole-page performance budget

- **Total page weight:** ≤900KB home (images are the cost —
  §6.17 plates at responsive sizes, ≤520KB of the budget);
  ≤640KB listing/detail; ≤120KB the unfilled glass (§6.18).
  Inline SVG: hero field ≤18KB, per-panel fields ≤12KB, cycle
  clusters ≤4KB, the scale ≤14KB, plates ≤3KB each.
- **Frame budget:** the shared loop ≤1.6ms per frame on a
  mid-tier phone: one pressure lerp, one needle transform,
  density fades for ≤3 panels, parallax for panels in view.
  No layout reads inside the loop (panel geometry is cached
  on resize and on content settle).
- **Long tasks:** none over 50ms; the hero ceremony is
  dashoffset-only and split across its 2000ms.
- **Cut order when the budget is exceeded:** (1) the rumble on
  <360px (§6.3); (2) cycle clusters on mobile (§6.5); (3) the
  solution parallax layer (§6.10's two-depth variant); (4)
  plate light crawl (§6.6); (5) card tilt (§6.12); (6) the
  clouding's density cap (§6.15). **Never cut:** the needle,
  the density function, any watchdog, the disclaimer, the
  printed states — the law (§1) is not a performance feature.

## 15. Build-order checklist

1. The static cabinet first: panels, cards, plates filled,
   scale drawn, needle printed at each page's honest position,
   forms native — the whole site complete with JS disabled
   (§10 printed-state test passes before any motion exists).
2. The pressure function and its four printings (needle,
   reading, density, state words) wired to a *manual* scroll
   value and audited (§10 one-pressure audit) before any
   easing is applied.
3. The shared loop with its two lerps (pressure 0.10;
   heaviness 0.14/0.08 by band) and its watchdog.
4. Crystal fields authored per panel (no shared paths, §9.2)
   and clipped to margin zones; the glass-law overlay check.
5. Etch-then-fill plates, with per-label stroke paths; edited
   labels default to filled.
6. The scale draw and its slaved needle.
7. The storm pin and the rumble (conditions, flag,
   focus-suppression) — built late, tested first (§10).
8. The living cycle, tap layer, reflection parallax — the
   ambient systems, in that order, each behind the loop's
   pause rules.
9. The commission form: native first, then rule-inking,
   seal-slips, clouded success, the computed entry number.
10. Counters with their source lines; the footer's record
    column generated from the same values.
11. Skeleton and clouding; the 404.
12. Reduced-motion pass over everything (weather held at
    Change, states printed), then the §10 gate, signed by
    someone who did not build the page.
