# 35. Dune Cartography — Expanded (v1 + v2)

> Expansion of theme #35 from `themes-026-050.md`, written directly to
> the full standard: the v1 10-part structure plus the v2 deepening
> layers (per-element choreography timelines, state matrices, breakpoint
> behaviour, edge cases, accessibility specs and token lists; per-theme
> component inventory, copywriting voice, three worked examples, scroll
> choreography map, performance budget, build-order checklist).
> Identity preserved exactly: the same concept, the same five palette
> anchors, the same two typefaces, the same nine signature elements —
> deepened, never redesigned — plus nine page-family elements.

## 1. Concept & world

Most websites are floor plans: flat, fixed, indifferent to weather.
This theme is the opposite wager. The site is **a desert surveyed like
a map the wind keeps redrawing** — the page is a chart of real ground,
drawn in contour lines, and the wind (the visitor's scroll) is always
quietly re-surveying it. Contour lines of dunes form every section's
background; content never sits on the exposed crest but rests in the
**lee** — the flat, calm side of each dune, where a traveller would
pitch a tent. A route crosses the chart with named stops; the map pins
while the itinerary is read and each stop lights as its paragraph
passes. Distances are not kilometres. They are **camel-hours**.

The world is the surveyor's chart, treated as a complete interface
vocabulary rather than a skin. The page has **contours** (the section
backgrounds, drawn as SVG line-work, never as images), **crests** (the
high line of each dune, which performs the section title's reveal),
**lees** (the calm flat where all reading matter lives), **stations**
(survey markers dropped at measured points, carrying elevations),
**the route** (a drawn line crossing the pinned map, segment by
segment, as the itinerary is read), **the compass** (a corner rose
whose needle is the page's progress, sweeping the visitor's bearing),
and **the camp** (the footer, in night blue, where the day's survey
ends). Nothing on the page is decoration that happens to look like a
map; the map is the page's structure, and every animated thing on it
is either the terrain, the route, or the instruments.

**The theme's one law: every figure on the map is surveyed, or it is
not printed.** A camel-hour distance is computed from a real distance
by the stated conversion (§12: 1 camel-hour = 4.2 km at laden pace)
and the workings are printed in the legend (§6.17). An elevation on a
survey marker is the content's own datum — a real height, a real
count, a real price restated in metres — or the marker carries no
figure at all. The compass needle's bearing is a declared function of
scroll position (§6.7), labelled as the visitor's bearing, never
dressed up as geography. A Dune Cartography build that invents a
distance because the itinerary "needed one more stop" has not bent
the theme; it has falsified a chart, and the quality gate (§10) fails
it on sight. Everything else in this theme is craft. That one is
cartographic ethics.

**Surveying is the interaction model.** Because the chart is being
drawn as it is read, the visitor's acts are a surveyor's acts: they
travel the route (§6.6), they drop brass markers on the stops they
choose (§6.9), they disturb a contour by touching a stop (§6.8), and
their bearing is always known (§6.7). The site does not have users;
it has travellers crossing surveyed ground. That is why the theme
fits journeys, expeditions, field work and anything whose content is
genuinely a route with stops and distances — and why it curdles
around anything that has no ground to cross.

**Best-fit sites and audiences.**

- Travel and expedition content with a real route: desert and
  overland tour operators, trekking and caravan itineraries, rally
  and expedition journals, pilgrimage routes — anywhere the stops,
  the order and the distances between them are facts the publisher
  will state in writing.
- Field-science and survey storytelling: geological surveys,
  archaeological digs, ecological transects, expedition reports —
  content that already thinks in stations, elevations and bearings.
- Brands rooted in arid places: desert lodges, kasbah hotels, oasis
  agriculture, solar farms in desert regions — a single journey from
  arrival to the night camp as the site's spine.
- Long-form journeys through any subject, honestly mapped: a product's
  road to market told as a route with surveyed milestones, a research
  programme's stations, a migration story. The ground may be
  metaphorical; the figures may not be.
- Portfolios structured as expeditions: a studio's projects as stops
  on one route, each with its surveyed distance from the last.

**When NOT to use it.**

- For content with no route. If the material is a grid of equivalent
  items (a catalogue, a dashboard, a news index), the map is a costume
  on a spreadsheet; the itinerary has nowhere to go.
- For anything urgent or transactional at speed. The theme's pace is a
  traveller's pace — contours drift, profiles redraw over 120vh of
  scroll, the route takes the whole page to cross. A visitor trying to
  check out in ninety seconds will feel lost in sand.
- Where distances would be theatre. If the publisher will not commit
  real distances, elevations and stop orders to the page, the
  camel-hours become a joke the chart tells about itself; use another
  theme.
- For dense data products. The lee is a calm, low-density reading
  ground by law (§4); tables of forty rows cannot pitch there.
- For audiences who must not be asked to learn a unit. Camel-hours are
  charming exactly once removed from a conversion the legend prints;
  a build whose readers cannot spare that one step should state
  kilometres in the lee and keep camel-hours for the itinerary only —
  or choose a different theme.

## 2. Palette

Five anchors, inherited unchanged. The palette is a printed chart on a
surveyor's table at two times of day: four colours of daylight paper
and ink, one colour of the night the survey ends in. Nothing else is
admitted; every other colour on the page is one of these five, tinted,
shaded or set at an opacity over sand.

| Token | Hex | Role | Usage ratio | Pairing & contrast notes |
|---|---|---|---|---|
| `--sand` | `#EFE3CB` | The paper: every page background, every lee surface | ~78% of pixels | Warm survey paper, never swapped for `#FFFFFF` anywhere, including form fields and the unmapped page (§6.18). Escarpment on it: 9.35:1. |
| `--gold` | `#D9B87C` | The dune fill: crest shading, the lit side of contours, marker halos, the filled route stop | ~9% of pixels | On sand only **1.49:1** — a fill and a glow, never text on sand at any size. On night camp 6.81:1, so gold may letter the camp. A gold word on sand is a gate failure (§10). |
| `--shadow-side` | `#A9743F` | The dune's shadow face: contour lines at mid strength, station rings, hover states, the route line under drawing | ~6% of pixels | On sand **3.14:1** — graphical and large-display use only (≥24px or non-text line-work). Its darkened derivative `--shadow-deep` (4.60:1) is the only form in which this hue may set text on sand. |
| `--escarpment` | `#4A3220` | The ink: body text, headings, contour lines at full strength, the drawn route, marker pins | ~5% of pixels | On sand 9.35:1 (AAA); on gold 6.29:1 (AA), so escarpment may letter a filled stop. The only colour body text may be set in on the daylight chart. |
| `--night` | `#26343B` | The camp: the footer ground, the dark scheme, the compass rose's night face | ~2% of pixels (daylight pages) | Sand on it 10.11:1 (AAA); gold on it 6.81:1. Never a section background in the daylight journey — night is where the route ends, not a stop on it (§9). |

**Derived tokens** (computed from the anchors; never new hues):

| Token | Derivation | Use |
|---|---|---|
| `--sand-deep` | `#E2D0A9` (sand darkened ~8%) | The lee's far edge: card grounds, the legend plate (§6.17), skeleton sheets (§6.15). Escarpment on it 8.31:1. |
| `--shadow-deep` | `#8A5A2E` (shadow side darkened ~18%) | The text-grade form of the shadow hue: captions, station figures, form labels on sand. On sand 4.60:1 — AA at all sizes. |
| `--brass` | `#9A742A` (gold darkened toward escarpment) | The visitor's dropped marker (§6.9) and the compass needle (§6.7). On sand 3.37:1 — a graphical object, always paired with an escarpment outline so it never relies on fill alone. |
| `--brass-bright` | `#C49A44` (brass lightened toward the light) | The specular edge of the brass marker and needle; the marker's settle glint (§6.9). Graphical only. |
| `--contour` | `--escarpment` at 26% over `--sand` | Contour line-work at rest (§4 density law). At 26% the lines read as printed chart work; they are never darker behind text (see `--contour-faint`). |
| `--contour-faint` | `--escarpment` at 11% over `--sand` | Contour line-work where it passes behind a lee text block — the lee clearance (§4) is enforced by dropping to this strength, never by letting a full-strength line cross type. |
| `--night-deep` | `#1B262C` (night darkened ~16%) | The camp's inner shadow: footer rule lines, the night skeleton. Sand on it 11.6:1. |
| `--hairline` | `--escarpment` at 18% over `--sand` | Ruled lines under itinerary stops, the scale bar's ticks (§6.17), table rules. Decorative only. |

**Dark-mode behaviour.** The chart does not invert; **night falls on
it.** Under `prefers-color-scheme: dark` (or the camp toggle, §11)
the whole page moves to the night scheme: ground `--night`, reading
surfaces `--night-deep`, text `--sand` (10.11:1), contours `--gold` at
30% over `--night`, crests `--gold`, the route `--sand`, markers
`--brass-bright` with sand outlines. The footer camp is identical in
both schemes — the traveller arrives at the same camp either way.
The transition between schemes is a 600ms `--ease-drift` crossfade of
background and line colours, fired once, never animated per scroll.

## 3. Typography

Two typefaces, inherited unchanged. **Marcellus** — a Roman inscriptional
capital face, one weight only — is the voice of the chart's names: the
places, the titles, the stations, everything the surveyor letters onto
the map by hand. **Alegreya Sans** (400 / 500 / 700, plus its small-cap
setting) is the voice of the survey's record: body text, figures,
labels, the apparatus. Marcellus has no italic and no bold; the theme
never fakes either. Emphasis inside display type is done by size,
letterspacing or a gold rule — never by synthesis.

| Role | Face & setting | Size / line-height / tracking | Rules |
|---|---|---|---|
| Display (hero title) | Marcellus | 64px / 1.04 / +0.01em, max 2 lines | Settles grain by grain (§6.2). Never centred on the crest — it sits on the ridge's left shoulder, reading with the contour. |
| Section title (crest title) | Marcellus | 40px / 1.1 / +0.015em | Rises over its crest (§6.4). One per crest; a section with two titles has two crests. |
| Station name | Marcellus | 24px / 1.2 / +0.02em | The name on a survey marker or itinerary stop. Always paired with its figure line (below). |
| Body | Alegreya Sans 400 | 17px / 1.65 / 0 | Measure 58–66ch, pitched in the lee (§4). The only face long text is set in. |
| Figure line (data) | Alegreya Sans 500, tabular figures | 15px / 1.5 / +0.01em | Elevations, distances, bearings: "ELEV 1,204 M · 3.5 CAMEL-HOURS". Tabular lining figures always — a rolling counter (§6.16) must never change width. |
| Caption / apparatus | Alegreya Sans 500 small caps | 13px / 1.5 / +0.09em | Chart furniture: "SURVEYED 2026 · SHEET 3 OF 7", legend labels, the compass cardinals. |
| Form label | Alegreya Sans 700 small caps | 13px / 1.4 / +0.09em | Set in `--shadow-deep` on sand (4.60:1) — the one place the shadow hue letters text, in its darkened form only. |

**Type laws.**

1. **Marcellus names places; Alegreya Sans keeps records.** A paragraph
   in Marcellus or a station name in Alegreya Sans is a casting error
   the gate checks by class, not by eye (§10).
2. **Figures are always tabular and always carry their unit.** "1,204"
   alone is unfinished typesetting; the chart prints "1,204 M". A
   distance without "CAMEL-HOURS" (or its dual kilometre figure, §12)
   is a broken figure under the one law (§1).
3. **No italics in the survey record.** Alegreya Sans italic exists and
   is refused for data, captions and figures; it is permitted only
   inside quoted traveller's prose in the body, at most twice per page.
4. **Titles are short enough to sit on a ridge.** Display ≤ 7 words,
   section titles ≤ 5. A title that needs a third line is two sections
   wearing one crest.
5. **The compass cardinals are set, never drawn as text paths.** N / E /
   S / W are DOM text in the apparatus setting around the rose (§6.7),
   so the instrument is announced correctly and survives font failure.

## 4. Layout language

**The sheet.** The page is one chart sheet, max width 1240px, on a
`--sand` ground that extends to the viewport edges — the sheet is the
page; there is no card floating on a different-coloured desk. Sheet
furniture (sheet number, surveyed date, scale) sits in the top margin
in the apparatus setting, like a printed map's margin information.

**Crests and lees.** Every section is one dune: a **crest line** (an
SVG contour path, the section's high line) and a **lee** (the flat
reading ground on the crest's sheltered side). The geometry is law:

- The crest path crosses the section at a shallow diagonal (4–9°
  apparent slope), entering and leaving at different heights; no two
  adjacent sections share the same crest profile — the wind redrew
  each one.
- All reading matter sits in the lee: a block whose top edge is at
  least **56px below** the crest line at its nearest point, inside a
  calm zone where contour strength drops to `--contour-faint`.
- **Lee clearance:** no contour line at `--contour` strength may pass
  within 24px of any text block. Where a contour would cross the lee,
  it either fades to `--contour-faint` for that span or bends around
  the block — decided at build time in the generated path (§6.3),
  never left to overlap and hope.

**Contour fields.** Section backgrounds are generated SVG contour
fields: 5–9 closed-ish contour paths per section, drawn from layered
sine/noise functions seeded per section (§6.3), spaced 26–44px apart,
tightening near the crest (a steep face) and opening in the lee (flat
ground). Line weight 1.25px at `--contour`; the crest itself 2px at
`--escarpment` 55%. Contour fields are background-only: they are
`aria-hidden`, `pointer-events: none`, and sit behind every content
layer at all times.

**Spacing rhythm.** A 4px base unit; section padding 96px top / 80px
bottom on desktop (the survey is unhurried); lee blocks separated by
40px; station rows by 24px. The route section (§6.6) breaks the rhythm
deliberately: it is 100vh pinned stage plus its scroll length, the one
place the sheet stops and the map takes over.

**Density rules.** At most one crest, one route stage and one pinned
scene per page region; at most 9 itinerary stops on the route (§6.6);
at most 5 survey markers in any single section (§6.5). A page that
needs more stops is two sheets, and the sheet furniture says so
("SHEET 3 OF 7" is content, §6.17).

**Whitespace is the flat desert.** The calm between contour groups is
not empty space to be filled; it is the erg, the flat ground the
traveller crosses between features. Sections end with at least 64px
of contour-free lee before the next crest rises.

## 5. Full motion system

The theme's motion is weather and surveying: things drift, are drawn,
settle, or are crossed. Nothing bounces for joy, nothing spins, and
the fastest event on the page (a marker's drop, §6.9) is over in
520ms. Five named easings carry the whole system:

| Token | Curve | Used by |
|---|---|---|
| `--ease-settle` | `cubic-bezier(0.22, 1, 0.36, 1)` | Sand and paper landings: grain settle (§6.2), marker drop settle (§6.9), stop cards |
| `--ease-drift` | `cubic-bezier(0.45, 0, 0.55, 1)` | Contour drift (§6.3), scheme crossfade, ripple travel (§6.8) |
| `--ease-survey` | `cubic-bezier(0.65, 0, 0.35, 1)` | Stroke drawing: survey redraw (§6.5), route segments (§6.6), legend assembly (§6.17) |
| `--ease-drop` | `cubic-bezier(0.3, 1.35, 0.55, 1)` | The brass marker's fall — one overshoot of ≤2px, the weight of brass (§6.9) |
| `--ease-needle` | `cubic-bezier(0.34, 1.2, 0.64, 1)` | The compass needle's settle wobble at section boundaries (§6.7) |

**Every motion term, translated into this theme's language:**

- **Scroll-triggered reveals** → crest-clipped titles (§6.4) and
  survey-marker drops (§6.5): content arrives the way features appear
  crossing a ridge — over the crest, or planted by the surveyor.
- **Scroll-driven / scrubbed animation** → the survey redraw (§6.5),
  the route line's drawing (§6.6), the compass sweep (§6.7), crest
  drift (§6.3). All scrubbed values run through the one shared rAF
  loop at lerp **0.12** (§14); there is no second loop.
- **Parallax** → line-work only: three contour layers drifting at
  −14 / +8 / −4 px per 100vh (§6.3). Images never parallax in this
  theme — the chart is line-work, and a photograph sliding against it
  would tear the paper.
- **Pinned sections** → exactly one: the route map (§6.6). A second
  pin on a page is a gate failure.
- **Smooth scrolling** → *wind-glide*: native scroll, with every
  scrubbed value lerped by the shared loop so the chart glides rather
  than steps. Scroll position itself is never hijacked or re-mapped.
- **Progress indicator** → the compass bearing (§6.7): the needle
  sweeps ~160° across the page; percentages are forbidden anywhere on
  the chart (§9).
- **Staggered reveals** → survey markers at 120ms intervals (§6.5),
  sand grains at 40ms (§6.2), itinerary stops in route order (§6.6).
  Stagger always follows a real order — measurement order, reading
  order, route order — never decoration order.
- **Masked reveals** → the crest clip (§6.4): the mask path *is* the
  section's crest contour, so the mask is the terrain.
- **Blur-to-sharp** → refused. A surveyed line is either drawn or not
  yet drawn; blur is fog, and this chart's weather is wind, not fog.
  The survey redraw (§6.5) is the theme's substitute: undrawn →
  drawn, at full sharpness throughout.
- **Animated counters** → field figures (§6.16): elevations and
  camel-hour distances count in tabular figures as their stations
  arrive — replays between two true values, never invented motion
  between fake ones.
- **Marquee** → refused. A chart does not scroll sideways. The wind
  report (§11) is a static apparatus line in the sheet margin whose
  text is set at build time; it changes between sheets, never during
  reading.
- **Ambient loops** → exactly two: one contour somewhere on the page
  breathing in a slow drift loop (§6.3), and the sand-grain noise
  shifting a few px with scroll (§6.15). A third ambient loop is a
  gate failure — a desert is quiet.
- **Kinetic typography** → refused, except the one licensed act: the
  hero title settling grain by grain (§6.2). Type on a chart is
  lettered once and stays lettered.
- **Micro-interactions** → the contour ripple (§6.8) and the brass
  marker drop (§6.9): touching the map disturbs its surface at the
  touched point, or plants a marker on it. Both are acts on the
  chart, not on chrome.
- **Hover physics** → no magnetic pull, no tilt. A chart lies flat on
  the table; the pointer's approach is answered by the ripple (§6.8)
  and a 2px lift of a stop card's shadow — the paper's edge, not the
  map leaning.
- **Image treatments** → plates (photographs, map details) scale
  1.06 → 1 inside their survey frames as they cross the viewport
  centre, framed by a drawn survey border (§6.12). The frame never
  moves; the plate settles into it like a pasted survey photo.
- **Page transitions** → the sand-sheet transition (§6.15): a sheet of
  contour line-work sweeps once across the viewport and the new sheet
  stands surveyed. 480ms, once per navigation, never on back/forward.
- **Skeleton loading** → the unsurveyed sheet (§6.15): contour fields
  at rest with blank lees — the ground before the survey party
  arrives, resolving as content lands, with a hard 1200ms law.
- **Custom cursor** → refused (standing rule). The system cursor is
  the surveyor's pencil; it is not themed.

## 6. Signature elements

### 6.1 Headline ripple — the wind crosses the ridge

- **What & why.** The theme's opening weather. On load, contour rings
  ripple outward once from the headline's position — scale and fade
  over 1400ms — like wind crossing a ridge and disturbing the drawn
  surface exactly where the title landed. It belongs because the
  headline sits *on* the ridge (§4): the map should register its
  arrival the way sand registers a gust, once, and then be still. A
  ripple that loops is a pond; this is a desert, so it happens once.
- **Structure.** An SVG layer inside the hero contour field, centred
  on the headline's baseline midpoint: 3 concentric contour-shaped
  rings (the section's own contour path geometry, scaled 1.0 / 1.35 /
  1.7), stroke `--shadow-side` at 45% → 0 opacity. The rings are
  clones of the hero crest's path data, so the ripple follows the
  ridge's real shape rather than a generic circle. The layer is
  `aria-hidden`, `pointer-events: none`, inserted by JS only — the
  no-JS page has no ripple and loses nothing.
- **Motion spec.** Trigger: page load, gated on `fonts.ready` (the
  ripple must centre on the *set* headline, not a fallback-font
  approximation). Ring 1: scale 0.92 → 1.12, opacity 0.5 → 0, 900ms
  `--ease-drift`. Rings 2 and 3 follow at +140ms and +280ms, 1100ms
  and 1400ms, peak opacity 0.35 and 0.22. Transform origin is the
  headline centre. After the last ring fades, the layer is removed
  from the DOM — the disturbance is over and the chart is still.
- **Choreography timeline (v2).** t+0: hero paints complete (headline
  set, contours at rest) → fonts ready → t+80ms: ring 1 begins →
  t+220ms: ring 2 → t+360ms: ring 3 → t+980ms: ring 1 gone →
  t+1760ms: final ring at opacity 0, layer removed → the grain settle
  (§6.2) has been running concurrently since t+120ms — the title
  settles *while* the wind crosses, so the two opening acts read as
  one weather event, not two animations in a queue.
- **State matrix (v2).** *Rest (pre-load / no-JS):* no rings; the hero
  is the finished chart. *Rippling:* 1400ms, non-interactive, identical
  on desktop and touch. *Hover / focus:* no effect — the ripple is
  weather, not a control, and hovering the headline never re-fires it.
  *Scrolled-past:* if the visitor scrolls before the ripple completes,
  it finishes off-screen or is cut at the hero's exit (whichever is
  sooner); it never follows the visitor down the page. *Disabled:*
  reduced-motion and no-JS both rest (below).
- **Content merge.** The rings are the hero's own contour geometry
  expanding from the headline's own position — the disturbance is
  drawn from the terrain the title names. Remove the headline and
  there is nothing to ripple from; remove the ripple and the hero is
  complete, merely unannounced.
- **Failure fallback.** If `fonts.ready` has not resolved by 900ms,
  the ripple fires anyway centred on the laid-out headline (its box
  is measurable in any font). If the SVG layer fails to build, the
  hero stands as the static chart — the watchdog is structural: the
  ripple is an inserted layer, and its absence is the fallback.
- **Reduced-motion variant.** No ripple. The hero is the printed
  chart from first paint; the grain settle (§6.2) is also stilled, so
  the opening is a single still image — the sheet as it would hang in
  the survey office.
- **Breakpoints (v2).** ≥1200px: 3 rings as specced. 768–1199px: 3
  rings, scale travel reduced (1.0 → 1.08 max). <768px: 2 rings,
  durations ×0.85 — a phone's ridge is narrower and a long weather
  event delays reading.
- **Edge cases & failure modes (v2).** *Return visit in the same
  session:* the ripple fires again — it is load weather, not a
  one-time ceremony; but if the page is restored from bfcache, it does
  not (the chart was never left). *Headline wraps to two lines:* the
  origin is the first line's centre, measured after layout. *Hero
  taller than the viewport:* rings still centre on the headline, not
  the viewport. *Slow device:* if the first frame of ring 1 measures
  >32ms, rings 2–3 are dropped and ring 1 completes alone.
- **Accessibility spec (v2).** Purely decorative and `aria-hidden`;
  nothing is announced, nothing is focusable, and the headline is
  ordinary DOM text readable from first paint — the ripple never
  masks it (peak ring opacity over the title's own pixels is 0 by
  construction: rings expand *outward* from the baseline midpoint and
  their stroke at t+0 sits outside the glyph boxes).
- **Performance budget & mobile variant.** Three stroked paths, one
  transform + opacity each, compositor-only; ≤0.4ms script per frame.
  Mobile: the 2-ring variant above; the layer is built lazily after
  first paint so it never competes with the hero's text.
- **Tokens consumed (v2).** `--sand`, `--shadow-side`, `--ease-drift`,
  `--ripple-dur` (1400ms), `--ripple-stagger` (140ms).

### 6.2 Sand-grain title settle

- **What & why.** The hero title arrives the way its subject does: as
  grains. Each letter drops 3–6px and settles, staggered 40ms in
  reading order, with a soft landing ease — then absolute stillness.
  It belongs because the title is made of the same material as the
  ground it names, and because it is the theme's single licensed act
  of kinetic type (§5): letters are grains, grains settle, settled
  sand does not move again.
- **Structure.** The hero `<h1>`'s text is split by JS into per-letter
  `<span class="grain">` wrappers (spaces and the full string remain
  in the DOM as the accessible text — the split is visual, via
  `aria-hidden` spans and a visually-hidden full-text node, or the
  h1 carries `aria-label` with the complete title). Each span is
  `display: inline-block` with a per-letter drop distance drawn from a
  fixed table (3–6px by letter index, deterministic — two builders,
  one title). The pre-settle state exists only under a JS-armed class
  on the root; the server-rendered title is fully settled.
- **Motion spec.** Trigger: load, at t+120ms (concurrent with §6.1).
  Per letter: translateY −(3–6px) → 0 with opacity held at 1 (grains
  are visible while they fall — a fading letter is a ghost, not a
  grain), 380ms `--ease-settle`, stagger 40ms in reading order. A
  24-letter title completes at ~120 + 23×40 + 380 = 1420ms. Letters
  never move again: no hover state, no replay, no loop.
- **Choreography timeline (v2).** t+0: title painted settled (no-JS
  state) → t+120ms: JS arms the unset state and the first grain drops
  → each subsequent grain at +40ms → mid-settle: the headline ripple
  (§6.1) is crossing the same ridge — the letters land inside the
  gust → last grain lands → t+1600ms watchdog: any letter not at rest
  (interrupted rAF, hidden tab) is snapped to rest instantly.
- **State matrix (v2).** *Rest:* settled title — the permanent state,
  and the no-JS state. *Settling:* 380ms per grain, staggered; touch
  identical. *Hover:* none — titles do not perform for pointers.
  *Focus:* the h1 is not focusable; a heading-navigation jump lands on
  settled text at any moment (a mid-settle letter is at ≥60% of its
  6px travel for at most 150ms and fully legible throughout — the drop
  is 6px, not a mask). *Scrolled-past / back:* settled, always.
  *Disabled:* JS off = settled; the split never happens.
- **Content merge.** The grains are the title's own letters and the
  distances are grain-scale (3–6px — a letter falling further would be
  a stone, not sand). The settle performs the theme's material claim
  on the theme's most important words, then stops forever, which is
  the claim.
- **Failure fallback.** The settled title is the DOM default; JS adds
  the unset state only when it can animate it, and the 1600ms
  watchdog guarantees rest. If the split fails partway, the partial
  spans are removed and the plain text node restored — the code path
  is delete-and-show, never repair-and-hope.
- **Reduced-motion variant.** No split, no drop. The title is simply
  set — the printed chart's title, which is what reduced motion asks
  every element in this theme to become.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: drop range
  3–5px, stagger 36ms. <768px: drop range 2–4px, stagger 30ms, and
  titles over 34 letters settle in two waves by word (≤17 letters per
  wave, 120ms between waves) so the ceremony stays under ~1.1s.
- **Edge cases & failure modes (v2).** *Very long title (a German
  expedition name):* law 4 of §3 caps display at 7 words; if the set
  title still exceeds 40 letters, the settle is cancelled for that
  build — a minute of falling letters is a screensaver, and the gate
  (§10) treats an over-long hero title as a copy error, not an
  animation problem. *Fonts late:* the settle waits for the §6.1
  fonts gate (900ms cap), because Marcellus and its fallback have
  different letter widths and grains must fall in their final boxes.
  *RTL titles:* stagger runs in reading order (right to left); drop
  distances unchanged — gravity is not localised.
- **Accessibility spec (v2).** The full title is in the accessibility
  tree once, complete, from first paint (visually-hidden text node or
  `aria-label` on the h1; the letter spans are `aria-hidden`). The
  motion is transform-only on ≤6px, far below any vestibular concern
  threshold, and is removed entirely under reduced motion. Contrast:
  escarpment on sand, 9.35:1, at every point of the fall.
- **Performance budget & mobile variant.** ≤40 transformed spans,
  compositor-only, no layout after the split (spans are sized by
  their glyphs before the first frame). Mobile: the two-wave variant
  above; the split itself is skipped on devices reporting ≤2GB RAM
  via `deviceMemory` where available — the title simply stands.
- **Tokens consumed (v2).** `--escarpment`, `--ease-settle`,
  `--grain-drop` (3–6px), `--grain-stagger` (40ms), `--grain-dur`
  (380ms).

### 6.3 Crest drift parallax — the line-work moves, the lee stays calm

- **What & why.** The page's ground is never quite still. Each
  section's contour field is drawn in three line-work layers that
  drift horizontally at different speeds as the visitor scrolls —
  −14 / +8 / −4 px per 100vh — so the chart itself moves under the
  content while the lee blocks, pitched on the calm side, do not move
  at all. It belongs because it is the theme's central spatial claim
  performed continuously: crests are weather, lees are shelter, and
  the visitor reads in the shelter while the weather slides past.
- **Structure.** Per section, one inline SVG (viewBox 1440×560,
  `preserveAspectRatio="xMidYMid slice"`) holding three `<g>` layers:
  far contours (the section's full field at `--contour-faint`), mid
  contours (the field's upper half at `--contour`), and the crest
  group (the crest path at escarpment 55% plus its two nearest
  contours). Paths are generated at build time from layered sine
  sums seeded by section index — deterministic geometry, identical
  for every builder and every visitor. Each layer is drawn 120px
  wider than the section on both sides, so drift never exposes an
  edge. The shared rAF loop writes one `transform: translateX` per
  layer per frame, only while the section is within one viewport.
- **Motion spec.** Scrubbed, lerped at 0.12 by the shared loop. Layer
  travel per 100vh of scroll: far −14px, mid +8px, crest −4px (the
  crest is the heaviest line and moves least — mass, in line-work).
  Directions alternate by section parity (odd sections mirror the
  signs) so the wind does not blow the same way down the whole sheet.
  **Ambient breath:** independent of scroll, exactly one contour on
  the page — the one nearest the viewport centre — breathes: its
  layer adds a ±3px `--ease-drift` drift on a 9000ms sine loop. When
  the centre changes sections, the breath hands over (the old layer
  eases to its scrubbed position over 600ms; the new one takes up the
  breath). One breath per page, always (§5).
- **Choreography timeline (v2).** Continuous, so the timeline is a
  map: section enters the loop's watch band → its layers begin
  tracking scroll from their current offsets (no jump — offsets are
  pure functions of scroll position) → section crosses viewport
  centre → its crest layer holds the page's single breath until the
  next section's centre arrives → section leaves the band → loop
  stops writing it; its layers rest at the mapped offset.
- **State matrix (v2).** *Rest (any fixed scroll position):* layers at
  their mapped offsets; the centre section's layer breathing ±3px.
  *Scrolling:* offsets track with 0.12 lerp — desktop and touch
  identical (touch scroll is the same scroll). *Hover:* none — ground
  does not respond to pointers; the stop-level ripple is §6.8.
  *Focus:* none. *Scrolled-past:* layers hold their end offsets; the
  breath has moved on. *Disabled (no-JS):* all layers at offset 0 —
  the printed chart, fully legible.
- **Content merge.** The drifting layers are the section's own
  background terrain and the lee blocks are the section's own text;
  the calm/motion contrast is drawn between the content's ground and
  the content itself. Nothing drifts that is not the map, and the map
  is the page.
- **Failure fallback.** Static SVG at offset 0 is the base state; JS
  only ever writes transforms onto it. If the loop stalls 1200ms,
  layers freeze at their last offsets — a frozen chart is a printed
  chart, and no watchdog theatre is needed beyond the loop's own
  stall rule (§14).
- **Reduced-motion variant.** No drift, no breath. All layers at
  offset 0 at all scroll positions — the chart as a wall map.
- **Breakpoints (v2).** ≥1200px: full travel (−14/+8/−4). 768–1199px:
  travel ×0.7. <768px: travel ×0.45 and the far layer is not rendered
  (two layers only) — a phone's chart is smaller and its processor is
  the survey's mule; the breath is also cut on <768px (the page's one
  ambient loop is the grain shift there, §6.15).
- **Edge cases & failure modes (v2).** *Lee clearance under drift:*
  layers drift horizontally only, and the lee fade (§4) is baked into
  each path's opacity profile across the lee span widened by the
  layer's full travel (±14px), so a drifting contour can never carry
  full-strength line into the text zone. *Very tall sections
  (>200vh):* drift maps to the section's own transit, capped at the
  100vh rates — a long section's ground moves at the same speed, for
  longer. *Resize:* offsets recompute from scroll position on the
  next frame; no stored state exists to go stale. *Print:* transforms
  are ignored by the print stylesheet, which sets all layers to
  offset 0 and `--contour-faint`.
- **Accessibility spec (v2).** The fields are `aria-hidden`
  background; no information is carried by drift (a contour's position
  is never data — §6.5's profile is the data-bearing line, and it does
  not drift). Contrast of line-work against text is governed by the
  lee clearance, not by the text itself, which always sits on plain
  `--sand` or `--sand-deep`.
- **Performance budget & mobile variant.** Per section: 3 transforms
  on SVG groups, compositor-only; the loop writes only sections in
  the watch band (≤3 sections, ≤9 transforms per frame). Path count
  per section ≤ 9 paths × ~60 points. Mobile: the two-layer, ×0.45
  variant above.
- **Tokens consumed (v2).** `--contour`, `--contour-faint`,
  `--escarpment`, `--ease-drift`, `--drift-far` (−14px), `--drift-mid`
  (+8px), `--drift-crest` (−4px), `--breath` (9000ms), `--loop-lerp`
  (0.12).

### 6.4 Crest-clipped titles — type comes over the ridge

- **What & why.** Every section title rises into place clipped by its
  own crest line, so the type appears to come over the ridge from the
  windward side and settle in the lee. It belongs because the crest is
  the section's horizon: a title that fades in mid-air belongs to no
  terrain, but a title that crosses its crest has *arrived* from
  somewhere. This is the theme's masked reveal (§5), and the mask is
  the terrain itself.
- **Structure.** Each section title sits in a `.crest-title` wrapper
  positioned so its baseline rests 8px into the lee below the crest
  path (§4 geometry). An SVG `clipPath` per section, built from that
  section's crest path closed downward, clips the title's inner span.
  The span starts translated 55% of its height downward (hidden below
  the crest line, inside the clip) — a JS-armed state only; the DOM
  default is the risen title. The crest path data is shared with
  §6.3's crest group (one geometry, two jobs), so the clip can never
  disagree with the drawn line.
- **Motion spec.** Trigger: the crest crossing 72% of viewport height
  on entry (IntersectionObserver, threshold on the section). The span
  rises translateY 55% → 0 over 700ms `--ease-settle`, while the crest
  path itself draws a 120ms highlight pass (`--shadow-side` overlay
  stroke fading in and out) at the moment the title's cap-height
  crosses the line — the ridge flashes once as the name comes over it.
  One-shot per section per session; scrolling back up never lowers a
  title (names, once lettered on a chart, stay lettered).
- **Choreography timeline (v2).** t+0: crest crosses the 72% line →
  t+0–700ms: title rises through the clip → t+~380ms (cap-height at
  the crest): the crest highlight pass fires, 120ms → t+700ms: title
  at rest in the lee; the clip is removed (`clip-path: none`) so no
  later layout change can re-hide a descender → watchdog at t+1100ms:
  any title not fully risen is set to rest and unclipped.
- **State matrix (v2).** *Rest (below trigger, JS armed):* span held
  at 55% inside the clip — this state exists only below the fold,
  never on a printed or no-JS page. *Rising:* 700ms. *Risen
  (terminal):* unclipped, at rest. *Hover:* none. *Focus:* if focus
  enters the section (a skip link or heading jump targets it) before
  the trigger, the title is set risen instantly — a keyboard traveller
  never waits for weather. *Scrolled-past:* risen. *Disabled / no-JS:*
  risen — the clip is never applied without JS.
- **Content merge.** The title is the section's name and the crest is
  the section's own high line; the reveal is performed by the terrain
  the section describes. The clip geometry is not a generic wipe — it
  is this dune's profile, shared with the background the visitor has
  been looking at.
- **Failure fallback.** Titles are fully visible in markup; JS arms
  the clip and the offset only for sections below the fold that it
  will actually observe. IO unsupported → no arming, all titles
  printed. The 1100ms watchdog and the clip removal at completion
  guarantee no title can be stranded mid-rise by a stalled frame.
- **Reduced-motion variant.** No clip, no rise. Titles stand lettered
  on their sections; the crest highlight pass is also cut (it is
  motion in service of motion).
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: rise 600ms,
  travel 45%. <768px: rise 480ms, travel 35%, highlight pass cut —
  the phone crest is lower and the flash reads as a glitch at small
  sizes.
- **Edge cases & failure modes (v2).** *Title longer than its crest
  span:* §3 law 4 caps titles at 5 words; a title that wraps to two
  lines rises as a block (clip still follows the crest) — the build
  gate measures the set title against the crest width and fails a
  three-line title as a copy error. *Jump scroll (anchor into section
  5):* all sections above the landing point are set risen instantly
  on arrival; the landed section's title rises normally if its crest
  is below the 72% line, else stands risen. *Resize mid-rise:* the
  clip path is in user units tied to the SVG viewBox and scales with
  the section; the rise is a transform and completes unaffected.
- **Accessibility spec (v2).** The title is a real heading in document
  order, present in the accessibility tree at full text from first
  paint — the clip is visual only. Heading order is section order;
  the rise is never announced. Focus-instant-rise (state matrix)
  keeps keyboard and screen-reader navigation free of animation
  waits.
- **Performance budget & mobile variant.** One transform + one clip
  per title, active ≤700ms; clip paths are static geometry (no
  per-frame path work). Mobile: the reduced-travel variant above;
  clips are dropped entirely on ≤2GB-RAM devices (titles simply
  stand, as in reduced motion).
- **Tokens consumed (v2).** `--escarpment`, `--shadow-side`,
  `--ease-settle`, `--rise-dur` (700ms), `--rise-travel` (55%),
  `--crest-flash` (120ms).

### 6.5 Survey redraw — the ridge is surveyed as you read

- **What & why.** In one designated section, a single ridge profile —
  the surveyed cross-section of the dune the page's route crosses —
  is redrawn stroke by stroke, scrubbed to scroll, while survey
  markers drop in sequence at the measured points along it. It
  belongs because it is the theme's thesis at full strength: the
  chart is not a picture of a survey, it *is* one, and the visitor's
  reading performs the measuring. The profile carries real data —
  its stations are the route's actual elevations (§6.6), printed in
  the figure line beneath each marker.
- **Structure.** An SVG stage (viewBox 1440×420) inside the survey
  section: the profile path (a single open path, the ridge's
  cross-section, drawn from the route's real elevation data at build
  time), a baseline rule (the datum), and up to 5 station groups —
  each a marker pin (a 10px escarpment triangle on a 28px stem), a
  station ring, and an HTML figure line positioned under the stage
  (figures are DOM text, never SVG text, so they are selectable and
  announced). The profile's `stroke-dasharray` is set from its
  measured length; scrub writes `stroke-dashoffset` from the shared
  loop. Markers are separate DOM/SVG groups armed by JS; in markup
  all markers stand dropped and the profile stands fully drawn.
- **Motion spec.** Scrub range: the section's transit from 80% to 30%
  of viewport height (≈120vh of scroll on desktop). Profile progress
  `p` maps linearly across the range, lerped 0.12. Stations sit at
  fixed profile fractions (their true positions along the route —
  e.g. 0.0 / 0.27 / 0.52 / 0.78 / 1.0); when `p` passes a station's
  fraction, its marker drops: fall 14px, 300ms `--ease-settle`, with
  its ring expanding 6 → 18px and fading over 500ms `--ease-drift`,
  and its figure line fading in over 200ms. Scrubbing back up
  reverses the profile draw (the line is a function of position) but
  markers, once dropped, stay dropped — a planted marker is not
  unplanted by walking backwards.
- **Choreography timeline (v2).** Spatial, per station: profile tip
  reaches the station's fraction → marker begins its 14px fall →
  +300ms: marker planted, ring pulse begins → +500ms: figure line
  fully in → the profile continues past the station; the planted
  marker is now chart furniture. Final station at p = 1.0 coincides
  with the section's lee text reaching reading position — the survey
  completes exactly as its account is read.
- **State matrix (v2).** *Rest (section unentered):* profile undrawn
  beyond the scrub's start (JS-armed only; markup is fully drawn),
  markers unplanted. *Surveying:* profile tip advancing with scroll,
  stations dropping as passed — desktop and touch identical. *Surveyed
  (p = 1):* full profile, all markers planted, all figures printed.
  *Hover:* a planted marker's figure line underlines in
  `--shadow-deep` (the only hover — the profile is not a control).
  *Focus:* markers are not focusable; the figure lines are ordinary
  text in reading order. *Scrolled-past:* surveyed state persists.
  *Disabled / no-JS:* the completed survey — full profile, planted
  markers, printed figures.
- **Content merge.** The profile is drawn from the route's elevation
  data and its stations are the itinerary's stops (§6.6 shares the
  dataset — one record, drawn twice, §6.6's content-merge). The
  animation is the act the section's text describes ("the ridge was
  surveyed in March; here is its profile") performed at reading
  speed.
- **Failure fallback.** The fully drawn profile is the markup state;
  JS withholds the draw only when it owns the scrub. If elevation
  data is missing for a station, that station is omitted at build
  time — the profile interpolates between true stations; it never
  invents a height to fill a gap (the one law, §1). Watchdog: if the
  loop stalls, the profile snaps to the mapped offset for the current
  scroll position on the next frame — a scrubbed element's fallback
  is its function, evaluated once.
- **Reduced-motion variant.** The completed survey at all scroll
  positions: full profile, planted markers, printed figures. The
  section reads as a finished chart plate.
- **Breakpoints (v2).** ≥1200px: as specced, 5 stations max.
  768–1199px: scrub range ≈100vh, 4 stations max (the closest pair
  merges at build time — merged, not dropped: its figure line carries
  both elevations). <768px: the stage becomes a vertical profile
  (rotated composition, same data) with scrub range ≈90vh and 3
  stations max; marker fall 10px.
- **Edge cases & failure modes (v2).** *Fast fling through the
  section:* `p` jumps; all stations whose fractions were passed drop
  in a compressed stagger (60ms apart, max 3 animating at once, the
  rest planted instantly) — the survey catches up like a party
  running to its instruments. *Route with only 2 elevations:* the
  profile is drawn with 2 stations and a longer single span; the
  theme permits a minimum of 2 — a 1-station "profile" is a point,
  and the section must not be built. *Profile data revised after
  build:* the path is regenerated from the dataset; markers'
  fractions are data, never hand-placed. *Section printed:* the
  completed survey prints (print stylesheet forces p = 1 state).
- **Accessibility spec (v2).** The SVG is `role="img"` with an
  `aria-label` stating the profile in words ("Ridge profile: rises
  from 812 m at the well to 1,204 m at the crest, falling to 940 m at
  the kasbah") — generated from the same dataset at build time.
  Figure lines are DOM text in route order. The scrub is scroll-only;
  no content is reachable solely by scrubbing (the lee text beside
  the stage repeats every figure in prose).
- **Performance budget & mobile variant.** One dashoffset write per
  frame; marker drops are ≤5 small transforms per section. Path
  length measured once at build and stored — no runtime
  `getTotalLength`. Mobile: the vertical variant above.
- **Tokens consumed (v2).** `--escarpment`, `--shadow-side`,
  `--shadow-deep`, `--gold`, `--ease-settle`, `--ease-drift`,
  `--survey-range` (120vh), `--marker-fall` (14px), `--loop-lerp`
  (0.12).

### 6.6 Route illumination — reading a stop lights its place

- **What & why.** The page's set piece. The route map pins for its
  scroll length while the itinerary's stops illuminate in order —
  each stop's marker fills escarpment brown and the route segment
  from the previous stop draws itself — exactly as the stop's text
  block passes the reading line. It belongs because text and map are
  one itinerary here: to read a stop is to arrive at it, and the map
  keeps the traveller's place the way a finger on a chart does. This
  is the theme's one pinned scene (§5), and it spends the pin on the
  content itself.
- **Structure.** A two-part stage: a pinned map panel (the route's
  SVG chart — a simplified contour field, the route path as a dashed
  undrawn line, stop markers as circles with station numerals) and
  the itinerary column (the stops as lee text blocks, each with
  station name, figure line, and prose). On desktop (≥1200px) the map
  pins left (55% width) while the column scrolls beside it; the pin
  is `position: sticky` inside a stage whose height is set by the
  column — no JS pinning. Route progress is computed in the shared
  loop from each text block's position relative to the reading line
  (55% viewport height). One dataset (stops, order, elevations,
  camel-hour distances) drives the map, the column, and §6.5's
  profile.
- **Motion spec.** When a stop's block crosses the reading line
  upward: its marker fills `--gold` → `--escarpment` over 300ms
  `--ease-settle`, a ring pulse (6 → 20px, fade, 600ms
  `--ease-drift`) fires once, and the route segment to it draws over
  600ms `--ease-survey` (dashoffset scrubbed to the block's transit
  through the reading zone, so a slow reader watches the line crawl;
  a fast scroll completes segments instantly by the catch-up rule
  below). The previously lit stop stays filled at 55% strength — the
  travelled route stays visible behind the traveller. The current
  stop's name letters in the map's margin list (apparatus setting)
  in `--escarpment`; upcoming stops sit at `--shadow-deep`.
- **Choreography timeline (v2).** Per stop: block top crosses 70%
  viewport height → marker begins filling → block crosses the 55%
  reading line → ring pulse fires, segment draw completes → block
  crosses 40% → stop settles to "travelled" (55% fill) as the next
  stop begins. Final stop: the full route stands drawn, the map's
  margin reads "ROUTE COMPLETE — N STOPS", and the stage releases
  into the camp-ward sections.
- **State matrix (v2).** *Unreached stop:* hollow marker (escarpment
  outline, sand fill), segment undrawn (JS-armed; markup shows the
  completed route). *Current:* filled, ring pulsed, name inked.
  *Travelled:* 55% fill, segment drawn. *Hover (map marker):* the
  marker's ripple (§6.8) plus its stop block in the column outlines
  in `--hairline` — map and text point at each other. *Focus:* stops
  in the column are reachable by heading navigation; focusing a stop
  block lights its marker instantly (no draw animation — the
  traveller has arrived by a different road). *Touch:* no hover
  pairing; tap on a marker scrolls its block to the reading line
  (native smooth scroll, 500ms) and lights it on arrival. *Disabled /
  no-JS:* the completed route — all stops filled, all segments drawn,
  margin reading the full itinerary.
- **Content merge.** The map is the itinerary and the itinerary is
  the map: same stops, same order, same figures, one dataset. The
  illumination is not an effect on the content; it is the state of
  having read it, drawn on the chart where the reading happened.
- **Failure fallback.** Markup ships the completed route; JS un-draws
  segments and un-fills markers only for stops below the reading line
  at arm time. Sticky unsupported (ancient browsers) → the map sits
  at the stage's head and illumination still tracks the column — the
  pairing survives the loss of the pin. Watchdog: any stop whose
  block is above the reading line at arm time or after a jump is set
  travelled instantly.
- **Reduced-motion variant.** No pin (the map heads the section as a
  static plate), no drawing: segments and fills follow the reading
  line instantly as state changes, or — if the build prefers — the
  completed route stands throughout and the column's apparatus margin
  notes the current stop in text. Either is lawful; mixing them is
  not.
- **Breakpoints (v2).** ≥1200px: pinned side-by-side as specced.
  768–1199px: map pins at the stage's top as a 34vh banner, column
  scrolls beneath it; segment draws shorten to 400ms. <768px: no pin
  — the map is a static plate at the section head with the completed
  route, and each stop block carries a miniature route strip (its own
  segment, drawn statically) above its prose; illumination becomes
  the margin-note variant. A pinned map on a phone is a map the
  traveller cannot see around.
- **Edge cases & failure modes (v2).** *More than 9 stops:* §4 caps
  the route at 9; a longer itinerary is split across two sheets with
  the route continuing ("ROUTE CONTINUES — SHEET 4"), each sheet's
  stage complete in itself. *A stop with no elevation:* lawful — its
  marker carries no figure (§6.5 omits it there too; the dataset is
  shared, so the omission is consistent everywhere, automatically).
  *Visitor scrolls up:* travelled stops stay travelled; the current
  marker follows the reading line back (state is a function of the
  highest block read for fills, of position for "current"). *Print:*
  the completed route and all stops print; the pin is released.
- **Accessibility spec (v2).** The map SVG is `role="img"` labelled
  with the route in words ("Route: 6 stops from the well to the
  kasbah, 11.5 camel-hours in all"). The column is the primary
  content and is fully readable without the map. The current stop is
  exposed to AT via `aria-current="true"` on its block, updated at
  reading-line crossings (state changes only, never per frame).
  Marker tap targets on touch are ≥44px (the marker's hit area, not
  its 12px glyph).
- **Performance budget & mobile variant.** Per frame: one position
  read per stop (cached, invalidated on resize) and ≤2 dashoffset
  writes. The contour field inside the map is a reduced 4-path
  version of §6.3 (no drift layers — the pinned map does not drift;
  the traveller's place must be findable). Mobile: the static-plate
  variant above.
- **Tokens consumed (v2).** `--escarpment`, `--gold`, `--shadow-side`,
  `--shadow-deep`, `--sand`, `--ease-settle`, `--ease-survey`,
  `--ease-drift`, `--seg-draw` (600ms), `--reading-line` (55%).

### 6.7 Compass bearing — progress is navigation

- **What & why.** In the sheet's corner sits a compass rose, and its
  needle is the page's progress indicator: it sweeps ~160° across the
  full scroll, showing the visitor's bearing down the page, with a
  small settle wobble at each section boundary. It belongs because in
  this theme progress is not a percentage consumed but a heading
  held — the traveller always knows their bearing through the
  content, and arriving at the camp (the footer) means the needle has
  swung to its final rest. It is the only progress indicator the
  theme permits (§5).
- **Structure.** A fixed-position rose, 84px diameter, in the sheet's
  bottom-right corner (inside the sheet margin, never over the lee):
  an SVG ring with tick marks at 16 points, DOM-text cardinals (N /
  E / S / W, §3 law 5) positioned around it, and a needle group —
  brass north half (`--brass` with an escarpment outline), sand south
  half — rotating about the centre. Beneath the rose, an apparatus
  caption: "BEARING 042° · SHEET 3 OF 7" — the bearing as a number,
  because a chart's instrument is also a readout. The rose is
  `aria-hidden` as a graphic; the caption's bearing figure is the
  accessible form and is a real DOM node updated at section
  boundaries only.
- **Motion spec.** Scrubbed by the shared loop (lerp 0.12): bearing =
  12° + (scroll progress × 160°), so the needle rests at 012° at the
  sheet's head and 172° at the camp. At each section boundary the
  needle overshoots its mapped value by 2.5° and settles back over
  450ms `--ease-needle` — the wobble of a compass card finding north
  as the traveller checks it. The caption figure updates at
  boundaries (never per frame — a flickering readout is an instrument
  no one trusts). The rose fades to 45% opacity while the route stage
  (§6.6) is pinned (the map has its own place-keeping there) and
  returns as the stage releases.
- **Choreography timeline (v2).** Continuous map: progress 0 →
  bearing 012°, caption "BEARING 012°" → each section boundary: wobble
  (overshoot 2.5°, settle 450ms) + caption steps to the new bearing →
  route stage entered: rose dims to 45% over 300ms → stage released:
  rose restores → progress 1: bearing 172°, caption "BEARING 172° ·
  CAMP", needle at rest for the remainder of the footer.
- **State matrix (v2).** *Rest (any scroll position):* needle at the
  mapped bearing; caption showing the current section's bearing.
  *Scrolling:* needle tracks with lerp; wobble at boundaries. *Hover:*
  the rose brightens to full (if dimmed) and the needle's brass half
  catches `--brass-bright` — an instrument acknowledged, not operated.
  *Focus:* the rose is not focusable and contains no controls.
  *Scrolled-past (in the camp):* needle at 172°, caption at CAMP.
  *Touch:* identical scrub; the rose shrinks (below) rather than
  covering content. *Disabled / no-JS:* the rose stands at 012° with
  the caption "BEARING — · SHEET 3 OF 7" (no figure invented: the
  dash is the honest no-JS bearing, §1).
- **Content merge.** The needle's angle is computed from the page's
  own length and the caption names the sheet the visitor is on — the
  instrument reads the journey it is pinned to. It is not a scroll
  bar in costume: a scroll bar says how much is left; a bearing says
  which way you are facing, and the theme's whole fiction is that
  facing matters.
- **Failure fallback.** Static rose at 012° (markup state). If the
  loop dies, the needle freezes at its last true bearing — a stopped
  compass still points somewhere real, which is more than a frozen
  progress bar can say; the caption keeps its last boundary figure.
- **Reduced-motion variant.** The compass is **fixed north** (012°)
  at all times, per the original entry's standing rule, and the
  caption reads "BEARING — (COMPASS FIXED)" — the instrument is
  present as chart furniture; progress is carried by the sheet
  furniture and headings alone.
- **Breakpoints (v2).** ≥1200px: 84px rose, bottom-right sheet
  corner. 768–1199px: 72px, same corner. <768px: 56px rose, moved to
  the top-right of the sheet margin (a phone's bottom corner is thumb
  country and browser chrome), cardinals reduced to N only, caption
  hidden — the bearing figure lives in the sheet furniture instead.
- **Edge cases & failure modes (v2).** *Short page (one section):*
  the sweep still maps 0→1 across the page; with no boundaries there
  is no wobble and one caption step — a one-stop sheet's compass is
  nearly still, which is correct. *Lee overlap:* the rose's corner
  zone is reserved in the sheet margin at build time; if a build's
  lee would run beneath it, the rose moves to the opposite corner —
  it never floats over text (checked at the gate, §10). *Bfcache
  restore mid-page:* bearing recomputes from scroll position on the
  first frame; no stored state exists.
- **Accessibility spec (v2).** Graphic `aria-hidden`; the caption is
  the instrument's accessible readout, updated at section boundaries
  with `aria-live="off"` (it is ambient information, never an
  announcement — a bearing that shouts is unusable). Contrast: needle
  brass on sand is graphical (3.37:1 with escarpment outline); the
  caption text is escarpment on sand, 9.35:1. The rose never overlaps
  a focusable element (gate-checked).
- **Performance budget & mobile variant.** One rotation write per
  frame, compositor-only; caption writes at boundaries only. Mobile:
  the 56px top-corner variant above; wobble amplitude halves (1.2°).
- **Tokens consumed (v2).** `--brass`, `--brass-bright`, `--escarpment`,
  `--sand`, `--ease-needle`, `--bearing-start` (12°), `--bearing-sweep`
  (160°), `--wobble` (450ms), `--loop-lerp` (0.12).

### 6.8 Contour ripple hover — touching the map disturbs its surface

- **What & why.** Hovering a map stop (on the route map, §6.6, or a
  station in the survey, §6.5) expands a ripple ring along its contour
  line — a stroke pulse travelling outward along the line the stop
  sits on, 800ms — so touching the map disturbs its surface exactly
  at the stop being considered. It belongs because it is the theme's
  answer to the hover state: not a colour change on a card, but the
  chart itself responding at the point of attention, along the
  terrain's own line.
- **Structure.** Each stop marker carries, in its section's SVG, a
  hidden ripple path: the local contour segment the stop sits on,
  extracted at build time as its own path (the stop's `data-contour`
  geometry). On hover/focus, a stroke overlay of that path
  (`--shadow-side`, 2px) draws outward from the stop in both
  directions via dashoffset, while a soft ring at the stop expands
  8 → 26px and fades. The overlay is removed at the end of the pulse.
  Stops without a contour segment (a stop in open flat ground — the
  build may place at most one, the well) ripple as a plain ring only;
  the exception is data (there is no line there), not an oversight.
- **Motion spec.** Trigger: pointerenter or focus-visible on the
  stop. Ring: scale/opacity 800ms `--ease-drift`. Line pulse: the
  overlay's visible dash travels from the stop outward to ±140px of
  path length over 800ms `--ease-drift`, stroke opacity 0.75 → 0.
  Re-entering the stop after leaving re-fires it; dwelling does not
  loop it — one disturbance per arrival, like a finger touching water
  once.
- **Choreography timeline (v2).** t+0: pointer lands → t+0–120ms:
  ring expands through its first third, line pulse ignites at the
  stop → t+400ms: pulse at ±70px, ring at 18px fading → t+800ms:
  pulse spent at ±140px, ring gone, overlay removed → the stop's own
  hover state (marker lift, §6.9's shadow grammar) persists while the
  pointer remains.
- **State matrix (v2).** *Rest:* no overlay, no ring. *Hover:*
  ripple as specced, once per entry. *Focus (keyboard):* identical
  ripple on focus-visible — parity is non-negotiable; the keyboard
  traveller disturbs the same water. *Active (press):* the ripple
  cuts instantly and the marker drop (§6.9) begins if the stop is
  clickable. *Scrolled-past:* ripples never fire off-screen (hover
  cannot reach them). *Touch:* no hover — a tap on a stop fires the
  ripple *and* selects (§6.6's tap rule); the ripple is the tap's
  acknowledgement. *Disabled stop (a closed well, a cancelled
  departure):* no ripple; the marker is struck through in the margin
  list instead — the map shows closures, it does not invite touch to
  them.
- **Content merge.** The pulse travels along the stop's own contour —
  the line that defines the ground the stop stands on. It cannot be
  moved to another theme or another element: it is this stop, this
  line, this touch.
- **Failure fallback.** The ripple is an inserted overlay; its absence
  (no-JS, build omission) leaves the stop's ordinary hover (a
  `--shadow-deep` underline on its name) fully functional. No content
  depends on it.
- **Reduced-motion variant.** No travel, no ring. Hover/focus shows a
  static 120ms fade-in of the contour segment at 40% strength for the
  duration of the hover — the line is *indicated*, not disturbed.
- **Breakpoints (v2).** ≥1200px: ±140px travel. 768–1199px: ±110px.
  <768px: tap-only, ±80px, ring 8 → 20px; pulse duration 650ms.
- **Edge cases & failure modes (v2).** *Pointer skims five stops in a
  row:* a 70ms intent delay before ignition, so a diagonal sweep
  across the map does not set the whole chart rippling; leaving
  within the delay cancels cleanly. *Two ripples at once:* at most
  one line pulse page-wide; a second stop's hover queues its ring
  only, and its pulse fires when the first completes or is cut.
  *Stop near a path end:* the pulse travels the available length and
  fades early — it never wraps or reflects.
- **Accessibility spec (v2).** The ripple is decorative feedback on an
  already-labelled control; the stop's name and figures are DOM text
  (in the margin list / figure line), announced independent of the
  pulse. Focus-visible parity (state matrix) plus a 2px escarpment
  focus ring on the stop's hit area (≥44px on touch, §6.6) means the
  ripple is a supplement to, never the only sign of, focus.
- **Performance budget & mobile variant.** One dashoffset + one ring
  transform per ripple, ≤800ms; the overlay path is pre-built in the
  SVG (no runtime path surgery). Mobile: the tap variant above.
- **Tokens consumed (v2).** `--shadow-side`, `--escarpment`,
  `--ease-drift`, `--ripple-travel` (140px), `--ripple-dur` (800ms).

### 6.9 Brass marker drop — the visitor marks the map

- **What & why.** Clicking a stop drops a brass marker onto it — the
  marker falls 18px, settles with one small bounce, casts a thin
  shadow — and pins its detail card open in the lee. It belongs
  because marking the map is how a traveller selects: not pressing a
  button beside the content, but planting their brass on the place
  itself. The marker is heavy, singular and persistent — the physical
  opposite of a tooltip.
- **Structure.** A marker element (SVG: a brass pin — circle head with
  escarpment outline, short stem, the stop's numeral in the head) held
  in a per-stop slot in the map SVG, initially absent (markup carries
  no marker; the detail card stands open in the lee by default for the
  first stop only, §6.12). On activation the marker is inserted above
  the stop, animated down 18px, and a shadow ellipse beneath it scales
  0.6 → 1 and darkens as it lands. One marker per visitor per map:
  dropping it on a second stop lifts it from the first (a 300ms rise
  and fade there) — a traveller carries one brass marker, and the
  map's honesty about that is the interaction's character. The marked
  stop is stored in the URL hash (`#stop=kasbah`) so a shared link
  arrives pre-marked.
- **Motion spec.** Trigger: click/tap/Enter on a stop. Fall: 18px,
  380ms `--ease-drop` (overshoot ≤2px at ~t+300ms — one bounce, the
  weight of brass; a second bounce is a toy). Shadow: 380ms
  `--ease-settle` in step. Card: the stop's detail card opens in the
  lee — its top edge slides from under the crest shadow over 350ms
  `--ease-settle` beginning at t+120ms, as the marker lands. Total
  ceremony ≤520ms. Unmarking (clicking the marked stop again): the
  marker lifts 10px and fades over 240ms; the card closes by the
  reverse slide, 280ms.
- **Choreography timeline (v2).** t+0: activation; any previous marker
  begins its lift → t+0–380ms: marker falls, shadow gathers →
  t+120ms: detail card begins opening → t+300ms: marker overshoots
  2px, settles → t+470ms: card fully open, its heading receives no
  focus (the traveller's place is kept — focus management below) →
  t+520ms: ceremony complete; hash updated without a scroll jump
  (`history.replaceState`).
- **State matrix (v2).** *Unmarked stop:* no marker; hover gives
  §6.8's ripple. *Falling:* 380ms, non-interactive. *Marked
  (terminal):* marker planted, card open, stop's margin-list name set
  in escarpment with a brass dot. *Hover on marked stop:* the marker
  lifts 2px (a held breath) — it does not re-drop. *Focus:* stops are
  buttons in the margin list and on the map (44px hit areas);
  focus-visible fires §6.8 and shows the escarpment ring. *Touch:*
  tap = click, identical ceremony. *Disabled stop:* cannot be marked
  (§6.8's struck-through rule). *No-JS:* no markers; all detail cards
  stand open in the lee in route order — the full itinerary, unmarked
  but complete.
- **Content merge.** The marker lands on the place and opens the
  place's own detail — distance from the previous stop, elevation,
  the stop's prose. The selection, the indicator and the content are
  one object in three forms (map, card, list), kept in agreement by
  the shared dataset (§6.6).
- **Failure fallback.** If the hash names a stop that no longer exists
  (a revised itinerary), the marker simply does not drop and the
  first card stands open — a dead link in a chart is corrected by
  ignoring it, never by erroring at the traveller. If SVG fails, the
  card still opens (the card is DOM; the marker is its ornament) and
  the margin list's brass dot carries the marked state alone.
- **Reduced-motion variant.** No fall. The marker appears planted
  (120ms fade) with its shadow at rest, and the card opens instantly.
  The marked state and hash behaviour are unchanged — state is not
  motion.
- **Breakpoints (v2).** ≥1200px: as specced, card opens in the lee
  beside the map. 768–1199px: card opens beneath the pinned banner
  map. <768px: there is no pinned map (§6.6); markers live on the
  static plate and the card opens inline under the stop's block;
  fall shortens to 12px.
- **Edge cases & failure modes (v2).** *Rapid clicking across stops:*
  ceremonies are single-flight — a new activation cuts the current
  fall at its present position and starts the new one; markers never
  duplicate (one marker element, re-parented). *Marker on the final
  stop + page end:* the card opens upward into the lee if the
  downward slide would cross the camp boundary. *Shared link with
  hash:* the marker starts planted (no fall — the traveller arrives
  to a map already marked by whoever sent them, and the margin note
  says so: "MARKED BEFORE YOUR ARRIVAL").
- **Accessibility spec (v2).** Stops are real `<button>`s (map hit
  areas) with names ("Mark the Kasbah — 3.5 camel-hours from the
  well"); `aria-pressed` carries the marked state. Opening a card
  does not move focus; the card's heading is reachable by the next
  Tab and the marked state is announced via the button's pressed
  state, not a live region. The marker glyph is `aria-hidden`; its
  numeral duplicates the margin list's text numeral.
- **Performance budget & mobile variant.** One transform + one shadow
  per ceremony, ≤520ms; the marker SVG is ~12 elements. Mobile: the
  inline variant above.
- **Tokens consumed (v2).** `--brass`, `--brass-bright`, `--escarpment`,
  `--gold`, `--ease-drop`, `--ease-settle`, `--marker-fall` (18px),
  `--drop-dur` (380ms).

### Page-family elements

### 6.10 Sheet-margin navigation (page family: navigation)

- **What & why.** Navigation in this theme is the chart's own margin:
  a rail along the sheet's top margin listing the journey's sections
  as a surveyor's contents — section name in Marcellus, its sheet
  position in the apparatus setting, joined by a hairline — because a
  map is consulted by its margin information, not by a hamburger. The
  current section is shown by ink (its name in `--escarpment` with a
  brass tick at its left), never by a filled pill.
- **Structure.** A `<nav class="sheet-margin">` in the sheet's top
  margin: items in route order (section order = journey order,
  §6.6's dataset order where sections are stops), each an `<a>` with
  name, a flexible hairline span, and its folio ("III"). The sheet
  furniture (sheet number, surveyed date, scale) sits at the rail's
  right end. On mobile the rail becomes a "CONTENTS OF THIS SHEET"
  toggle opening a panel that wipes down (§6.15's sheet grammar at
  300ms). Scrollspy runs on the shared IntersectionObserver: the
  section crossing the reading line (§6.6's 55%) inks its item.
- **Motion spec.** Hover/focus: the item's hairline draws from the
  name toward the folio (background-position sweep, 180ms
  `--ease-survey`) and the folio's numeral warms to `--shadow-deep`.
  Scrollspy change: outgoing item drains to `--shadow-deep` over
  200ms as the incoming item inks to `--escarpment` and its brass
  tick fades in — the two overlap for one beat, like a hand moving
  down a contents list. The mobile panel opens with the 300ms sheet
  wipe; Esc closes it and returns focus to the toggle.
- **Choreography timeline (v2).** Hover: t+0 hairline sweep begins →
  t+180ms line complete, folio warmed → pointer leave: line relaxes
  over 240ms. Scrollspy: boundary crossed → 200ms crossfade of ink
  weights + tick swap → apparatus caption under the rail updates
  ("YOU ARE CROSSING: THE LONG DUNES") at the same beat.
- **State matrix (v2).** *Rest:* items in `--shadow-deep`, hairlines
  at rest. *Hover / focus:* sweep + warm folio, identical for
  keyboard. *Current:* escarpment ink, brass tick, `aria-current`.
  *Scrolled-past:* the rail scrolls away with the sheet margin — no
  sticky nav ever appears; the compass (§6.7) is the page's persistent
  instrument instead. *Disabled:* a section with no content is absent
  from the margin — a chart does not list ground it has not surveyed.
  *Touch:* behind the Contents toggle; rows ≥44px.
- **Content merge.** The items are the page's real sections with
  their real sheet positions, generated from the page's own headings
  and the route dataset — add a section and the margin gains a line,
  because the margin *is* the sheet's table of contents.
- **Failure fallback.** Plain anchor list in the margin; hairlines
  are CSS and survive without JS; scrollspy is the only JS behaviour
  and its absence leaves the first item inked (server-rendered where
  known) and the rest at rest weight.
- **Reduced-motion variant.** No sweep (hairline appears full), no
  wipe (panel opens instantly), scrollspy ink changes are instant.
- **Breakpoints (v2).** ≥1200px: horizontal rail, hairlines flexible
  (min 24px, else the item wraps to two lines rather than squeezing
  the line below legibility). 768–1199px: rail wraps to two rows.
  <768px: Contents toggle + wipe panel, one column, folios retained.
- **Edge cases & failure modes (v2).** *More than 7 sections:* the
  rail lists first-level sections only; stops live in §6.6's margin
  list. A margin with 14 items is an index, not a contents — the
  build splits the sheet (§4). *Long names:* truncate at 24ch on the
  rail with the full name in the panel and in `aria-label`. *Single-
  section page:* the rail is omitted — a one-feature sheet has no
  contents.
- **Accessibility spec (v2).** Real `<nav aria-label="Contents of
  this sheet">`; current item carries `aria-current="true"` (updated
  at section changes only). Hairlines are CSS, invisible to AT.
  Focus order = journey order. Toggle is `<button aria-expanded>`;
  all rows ≥44px on mobile, ≥28px desktop with the name's full line
  box as the target.
- **Performance budget & mobile variant.** Scrollspy on the shared
  observer — free. The sweep is a background-position transition on
  one span. Mobile: the toggle variant above.
- **Tokens consumed (v2).** `--escarpment`, `--shadow-deep`, `--brass`,
  `--hairline`, `--ease-survey`, `--leader-draw` (180ms), `--spy-fade`
  (200ms).

### 6.11 The survey camp hero (page family: hero)

- **What & why.** The hero is the expedition's point of departure:
  the headline on the first ridge (§6.1, §6.2), the standfirst in the
  first lee, and the chart's opening facts — where the route starts,
  how many stops, how many camel-hours in all — set as the margin
  figures of a departure. It belongs because a journey page must
  depart from somewhere named: the hero is not a billboard above the
  map, it is the map's first ground.
- **Structure.** A full-sheet-width section: the hero contour field
  (§6.3) with its crest crossing at ~38% height; the `<h1>` on the
  crest's left shoulder; the standfirst (≤34 words) in the lee below;
  a departure line in the apparatus setting ("DEPARTS THE WELL ·
  6 STOPS · 11.5 CAMEL-HOURS IN ALL") whose figures come from the
  route dataset; and one action — "Follow the route" — an escarpment
  text link with a drawn underline that scrolls to the route stage
  (§6.6). No image: the first plate on the sheet is the chart itself.
- **Motion spec.** The hero's motion is §6.1's ripple and §6.2's
  settle, plus the departure line's figures counting in once
  (§6.16's machinery at hero scale: stops count 0 → N over 600ms,
  camel-hours 0 → total over 900ms, tabular, one-shot at load +400ms)
  — the expedition's size being tallied as the traveller arrives.
  The action link's underline draws on hover (200ms `--ease-survey`).
- **Choreography timeline (v2).** t+0: sheet paints, hero complete in
  markup → t+80ms: ripple begins (§6.1) → t+120ms: grains begin
  settling (§6.2) → t+400ms: departure figures begin their count →
  t+1300ms: counts complete; hero at permanent rest. Nothing in the
  hero moves after t+1800ms except §6.3's drift when scrolled.
- **State matrix (v2).** *Rest:* the departed-from camp — title set,
  figures printed (the markup state; counts are an enhancement replay
  between 0 and the true figure). *Hover:* only the action link's
  underline. *Focus:* the link is the hero's sole focusable element;
  focus shows the drawn underline plus the theme ring. *Scrolled-past:*
  the hero's crest joins §6.3's drift like any section. *Disabled /
  no-JS:* the printed hero — title, standfirst, true figures, link.
- **Content merge.** Every hero element is the journey's own data:
  the title names the crossing, the standfirst is its first lee text,
  the departure line is the route dataset's totals. There is no
  decorative layer to remove — remove the dataset and the hero has
  no figures, which is the test.
- **Failure fallback.** The printed hero is the fallback; counts
  never gate the figures' presence (the true totals are in the DOM
  from first paint; the count masks them visually only while it
  runs, and a 1400ms watchdog prints them outright).
- **Reduced-motion variant.** No ripple, no settle, no counts. The
  hero stands printed.
- **Breakpoints (v2).** ≥1200px: crest at 38%, title 64px.
  768–1199px: title 52px, crest at 34%. <768px: title 40px, crest at
  30%, departure line wraps to two lines with figures kept tabular,
  standfirst measure full lee width.
- **Edge cases & failure modes (v2).** *Route dataset empty (a
  single-feature sheet):* the departure line is omitted and the hero
  carries the sheet furniture instead — a hero that departs nowhere
  says nothing about departing. *Title over a busy contour span:* the
  lee-clearance rule (§4) applies to the crest's own field — contours
  behind the title's glyphs are at `--contour-faint`, enforced in the
  generated field, not by a scrim.
- **Accessibility spec (v2).** One `<h1>`; the departure line is text,
  read as text ("Departs the well. 6 stops. 11.5 camel-hours in
  all."); counts are visual replays over printed figures (the tree
  holds the totals throughout). The action link's name is "Follow
  the route to [destination]" in full.
- **Performance budget & mobile variant.** The hero ships no image;
  its cost is §6.1 + §6.2 + §6.3's first field. LCP is the title's
  text paint. Mobile: as breakpoints.
- **Tokens consumed (v2).** `--sand`, `--escarpment`, `--gold`,
  `--shadow-deep`, `--ease-survey`, `--count-stops` (600ms),
  `--count-hours` (900ms).

### 6.12 Itinerary stop cards (page family: cards / listing)

- **What & why.** The card in this theme is a survey plate: a stop's
  photograph or chart detail pasted into a drawn survey frame, its
  name in Marcellus, its figure line, and one line of prose — the
  unit of any listing the theme produces (more stops, related
  crossings, the season's other routes). It belongs because a listing
  in a chart world is a set of plates from the survey, each framed
  the way the survey office frames its photographs — with a drawn
  border, a plate number, and the figures lettered beneath.
- **Structure.** `<article class="plate-card">`: the frame (2px
  escarpment border with a 6px inner hairline offset — a double rule,
  drawn), the plate image inside (scale-in treatment below), plate
  number in the apparatus setting at the frame's foot ("PLATE IV"),
  name, figure line (distance from the previous stop + elevation,
  from the dataset), one prose line (≤18 words), and the whole card
  as one link to the stop's place on the route (§6.6 anchor) — or,
  on listing pages, to the stop's own sheet.
- **Motion spec.** Entry: the card's frame draws (its double rule is
  an SVG rect, 500ms `--ease-survey`) as the card enters, then the
  plate settles scale 1.06 → 1 over 600ms `--ease-settle` — the
  photograph being pasted flat. Hover: the plate's scale holds; the
  frame's shadow (a flat `--sand-deep` offset, the pasted plate's
  thickness) grows 3px → 6px over 200ms and the name warms to
  `--shadow-deep`. Focus: same as hover plus the ring. The draw is
  one-shot; cards never redraw.
- **Choreography timeline (v2).** t+0: card crosses 80% viewport →
  t+0–500ms: frame rule draws → t+150ms: plate begins settling →
  t+750ms: plate flat, card at rest. A row of cards staggers by 90ms
  in reading order, capped at 4 drawing at once; the rest stand
  drawn.
- **State matrix (v2).** *Rest:* framed plate, flat. *Entering:*
  drawing/settling as above. *Hover / focus:* shadow growth + warm
  name. *Active:* shadow collapses to 2px (the plate pressed) for
  the press duration. *Scrolled-past:* rest. *Touch:* no hover
  grammar; a card at viewport centre receives the plate settle only.
  *Disabled:* a card for a stop removed from the route is not
  rendered as a card — it becomes an apparatus note in the listing
  ("THE WELL AT KHARGA IS DRY THIS SEASON — SEE SHEET 5"), because
  the chart records closures rather than greying them out.
- **Content merge.** The card's figures are the dataset's figures for
  that stop — the same numbers the route map and the survey profile
  carry. The frame draw manufactures the plate in front of the
  reader; the plate is the stop's own photograph.
- **Failure fallback.** Static framed card, plate at scale 1 (markup
  state; the draw and settle are JS/CSS-armed enhancements). A card
  with no photograph uses a contour plate (a generated §6.3 field
  fragment for that stop's ground) — never a grey box, never a stock
  desert.
- **Reduced-motion variant.** No draw, no settle. Hover changes the
  name's ink only. Cards stand framed.
- **Breakpoints (v2).** ≥1200px: cards in the lee in mixed spans
  (never a uniform 3×3 grid — plate sizes vary as survey plates do).
  768–1199px: two-up. <768px: one-up, frame draw shortened to 350ms,
  plate settle cut (plates stand flat — a phone listing is read, not
  exhibited).
- **Edge cases & failure modes (v2).** *Missing figure (a stop with
  no elevation):* the figure line prints the distance alone — the
  dataset's omission is honoured on the card exactly as on the map
  (§6.6). *Long stop name:* clamps at 2 lines; the full name is the
  link's accessible name. *Plate image fails:* the contour plate
  fallback swaps in (build-time alternative, not a runtime guess).
- **Accessibility spec (v2).** One link per card (the name), full
  name as its accessible name; the plate's `alt` names the place
  ("The kasbah at dusk, from the south ridge") — a plate is content,
  not decoration, on a survey. Focus ring 2px escarpment offset 3px,
  visible against the grown shadow. Figure lines are real text in
  reading order.
- **Performance budget & mobile variant.** Frame draws are ≤4
  concurrent transforms/strokes; plates are responsive images ≤90KB
  each (§14). Mobile: the one-up, no-settle variant above.
- **Tokens consumed (v2).** `--escarpment`, `--hairline`, `--sand-deep`,
  `--shadow-deep`, `--ease-survey`, `--ease-settle`, `--frame-draw`
  (500ms), `--plate-settle` (600ms).

### 6.13 The caravan form (page family: forms / conversion)

- **What & why.** The theme's conversion form is a page from the
  expedition ledger: the traveller writes their name, their party
  size, and the stop they mean to join at, on ruled lines, and the
  entry is stamped with a survey seal when it is accepted. It belongs
  because joining an expedition *is* being entered in its ledger —
  the form's honesty (few fields, real figures, a confirmation that
  is a ledger entry with a number) is the theme's answer to the
  growth-hacked signup.
- **Structure.** `<form class="ledger-form">` in a lee panel framed
  by a drawn double rule (§6.12's frame grammar at form scale):
  fields as bottom-ruled inputs (transparent ground, 2px escarpment
  bottom rule, Alegreya Sans 17px input text, §3 form labels above),
  a stop selector rendered as the route's own margin list (radio
  rows: stop name + figure line — the traveller chooses a place, not
  an option code), a party-size stepper drawn as survey tally marks
  (|||| — count shown as tallies plus the tabular figure), and the
  submit as a seal button: an escarpment-bordered circle-and-rule
  device lettered "ENTER IN THE LEDGER".
- **Motion spec.** Entry: the panel's frame draws per §6.12, then the
  seal device draws its circle (400ms `--ease-survey`) last — the
  form is complete when it can be sealed. Field focus: the field's
  rule thickens 2px → 3px and a `--gold` underline plate slides in
  beneath it from the left (200ms `--ease-settle`) — the line being
  written on is lit by the sun side of the dune. Error: the rule
  turns `--shadow-deep` (the theme has no red; an error on a chart is
  a correction, marked in the surveyor's brown) and the error note
  letters in beneath in the ledger voice (§12) over 240ms. Submit:
  the seal presses — scale 1 → 0.94 → 1, 180ms `--ease-drop` — and on
  success the panel is *entered*: a ledger line draws across its head
  with the entry number and the confirmation text ("ENTERED AS NO.
  214 — WE WILL WRITE BEFORE THE NEW MOON"), the form replaced by
  its own record.
- **Choreography timeline (v2).** Entry: frame 500ms → seal circle at
  +300–700ms. Focus: rule + plate in 200ms. Submit: t+0 press begins
  → t+180ms seal at rest, request in flight (the seal holds a 15%
  escarpment wash while waiting — the ink is wet) → success: ledger
  line draws 400ms, entry text fades in at +250ms → error: the
  offending field's rule browns and its note letters in; focus moves
  to the first error; **the traveller's entered text is never cleared
  by an error, including a server 500** — the ledger does not burn
  its pages.
- **State matrix (v2).** *Rest:* ruled fields, seal drawn. *Focus:*
  thickened rule + gold plate. *Filled:* the rule carries a small
  brass tick at its right end (entered, not yet sealed). *Error:*
  brown rule + ledger-voice note, `aria-invalid` set. *Submitting:*
  seal washed, fields inert but legible. *Success (terminal):* the
  entry record replaces the form. *Disabled:* a closed expedition
  renders no form — the panel becomes the ledger's closed entry
  ("THE 2026 CROSSING IS FULL — THE LEDGER OPENS AGAIN IN OCTOBER").
  *Touch:* identical, with ≥48px field rows.
- **Content merge.** The stop choices are the route's stops with
  their real figures; the party tally counts the traveller's own
  party; the entry number on success is the server's real sequence —
  the form is a page of the same ledger the whole site keeps.
- **Failure fallback.** A plain ruled form posts natively without JS
  (the seal is a submit button; the entry record is a server-rendered
  page state). No-JS loses the focus plate and the press, nothing
  else. If the entry number cannot be returned, the confirmation
  prints without a number — never with an invented one (§1).
- **Reduced-motion variant.** No frame draw, no press, no lettering-
  in: errors appear whole, the seal changes by wash only, success
  replaces the panel instantly.
- **Breakpoints (v2).** ≥1200px: form in the lee at 560px measure,
  stop radios in two columns. 768–1199px: one column of radios.
  <768px: full lee width, tally stepper rows 56px, the seal button
  full-width at the panel's foot.
- **Edge cases & failure modes (v2).** *Party larger than the
  expedition's stated capacity:* the stepper caps at the real
  capacity (from the dataset) and the note says the true figure
  ("THE CROSSING TAKES 14 — FOR A LARGER PARTY, WRITE TO THE CAMP")
  — a cap invented by the front end is a gate failure. *Duplicate
  submission:* the seal disables on first press; a second entry for
  the same name+stop returns the original entry number ("ALREADY
  ENTERED AS NO. 198") rather than a duplicate row. *Long names:*
  the ruled field scrolls horizontally; the ledger line on success
  wraps the name at 2 lines, never truncates it.
- **Accessibility spec (v2).** Real `<label>`s; errors are text,
  linked by `aria-describedby`, announced by the browser's native
  invalid handling — no live-region shouting. The tally stepper is a
  pair of real buttons ("One more traveller" / "One fewer") with the
  count as a labelled output. Focus order = ledger order (name →
  stop → party → seal). Contrast: labels `--shadow-deep` 4.60:1 ✓;
  input text escarpment 9.35:1 ✓; error notes `--shadow-deep` on
  sand 4.60:1 ✓ (never gold — 1.49:1 would be a gate failure).
- **Performance budget & mobile variant.** The form's motion is ≤3
  small transitions; the frame/seal draws run once. No JS library —
  validation is native + a submit handler. Mobile: the full-width
  variant above.
- **Tokens consumed (v2).** `--escarpment`, `--gold`, `--shadow-deep`,
  `--brass`, `--sand-deep`, `--ease-survey`, `--ease-settle`,
  `--ease-drop`, `--seal-press` (180ms).

### 6.14 The night camp footer (page family: footer)

- **What & why.** Every route in this theme ends the same way: the
  traveller reaches the camp at nightfall. The footer is that camp —
  a `--night` ground across the sheet's full width, the day's route
  summarised in sand and gold, the compass at rest, and the survey's
  colophon. It belongs because a journey's footer is not a sitemap
  with a logo; it is where the travelling stops, and the theme's one
  use of night (§2) is spent here, at the end, where night belongs.
- **Structure.** A full-bleed `--night` section: at its head, the
  route summary line in Marcellus sand ("THE WELL TO THE KASBAH — 6
  STOPS · 11.5 CAMEL-HOURS") drawn from the dataset; beneath it, the
  stops listed in route order as a camp roll (name + figure, sand at
  85%); the compass rose (§6.7) at its rest bearing; the colophon in
  the apparatus setting ("SURVEYED AND DRAWN BY … · SHEET 3 OF 7 ·
  DISTANCES IN CAMEL-HOURS, 1 = 4.2 KM"); and the ordinary footer
  obligations (contact, legal) set as camp records in Alegreya Sans.
  A single gold contour — the last dune — crosses the camp's top edge
  as its horizon.
- **Motion spec.** Entry: the horizon contour draws once (900ms
  `--ease-survey`) as the camp enters, and the camp roll's stops fade
  in in route order at 60ms stagger — the roll being called. That is
  all. The camp does not drift, breathe or shimmer: night in this
  theme is stillness after weather, and the footer's restraint is
  its statement (§9).
- **Choreography timeline (v2).** t+0: camp top crosses 85% viewport
  → t+0–900ms: horizon draws → t+200ms: roll call begins, 60ms per
  stop → t+200+60×N ms: roll complete → permanent rest; §6.7's needle
  arrives at 172° concurrently and stops.
- **State matrix (v2).** *Rest:* the camp, complete (markup state).
  *Entering:* horizon + roll call as above, once. *Hover:* links
  warm to `--gold` (6.81:1 on night — the one place gold may letter,
  §2). *Focus:* gold name + sand ring. *Scrolled-past:* n/a — the
  camp is the end. *Disabled / no-JS:* the camp stands complete; the
  horizon is drawn in markup and the roll is printed.
- **Content merge.** The roll is the route dataset read back at
  journey's end; the colophon's conversion line is the legend's
  honesty (§6.17) repeated where the traveller leaves. Remove the
  route and the camp has nothing to summarise — the footer is the
  itinerary's past tense.
- **Failure fallback.** Static night section; the horizon draw and
  roll stagger are enhancements on a complete camp.
- **Reduced-motion variant.** No draw, no stagger. The camp stands.
- **Breakpoints (v2).** ≥1200px: roll in two columns, compass right.
  768–1199px: one column, compass above the colophon. <768px: roll
  one column, compass at 56px (§6.7's mobile size), colophon lines
  stack.
- **Edge cases & failure modes (v2).** *A page with no route (a
  single-feature sheet):* the camp carries the sheet's own summary
  (its crests listed as ground crossed) — the structure survives; the
  dataset differs. *Very long routes (9 stops):* the roll caps at the
  route's stops by definition (§4); a two-sheet journey's camp lists
  this sheet's stops and notes the continuation.
- **Accessibility spec (v2).** A real `<footer>`; the roll is a list
  in route order; contrast sand on night 10.11:1 ✓, gold on night
  6.81:1 ✓ (links), apparatus text sand at 85% on night ≈ 8.4:1 ✓.
  The horizon SVG is `aria-hidden`.
- **Performance budget & mobile variant.** One 900ms stroke draw +
  ≤9 opacity fades, once. No loops in the camp, ever. Mobile: as
  breakpoints.
- **Tokens consumed (v2).** `--night`, `--night-deep`, `--sand`,
  `--gold`, `--ease-survey`, `--horizon-draw` (900ms),
  `--roll-stagger` (60ms).

### 6.15 Unsurveyed sheet + sand-sheet transition (page family: loader / transition)

- **What & why.** The theme's two state-change rituals, sharing one
  material: unmeasured ground. **Loading** shows the unsurveyed
  sheet — the section's contour field at rest with its lee blank and
  its figure lines as unlettered rules — resolving as content lands:
  the survey party arriving. **Navigation** is the sand-sheet: a
  full-viewport sheet of contour line-work sweeps once across
  (480ms), the route changes at full coverage, and the new sheet
  stands surveyed. Both belong because they are the chart's own
  before-states — ground not yet measured, a sheet not yet turned —
  not a spinner borrowed from another world.
- **Structure.** Skeleton: the real section markup rendered with
  `.is-unsurveyed` — contour field present (§6.3 geometry), lee
  blocks as `--sand-deep` plates at the content's true geometry
  (aspect and height reserved — layout shift zero by construction),
  figure lines as hairline rules. Content swap replaces plate
  children in place. Transition: a fixed `.sand-sheet` (sand ground,
  a sparse contour field, one escarpment rule at its leading edge)
  parked off-canvas left; on navigation it translates across, the
  route swaps at full coverage, and it exits right.
- **Motion spec.** Skeleton resolve: per block, the plate fades to
  the real content over 240ms `--ease-settle` as it lands, its
  figure rules lettering in last (the survey writes figures after
  ground). Hard cap: any block still unsurveyed at **1200ms** has
  its plates stripped to plain `--sand` and receives content plainly
  when it comes — no ground stays blank because the machinery failed.
  Transition: 480ms total `--ease-drift` (240ms cover, swap, 240ms
  reveal); the incoming sheet arrives *surveyed* (its reveals do not
  re-run after a sheet change — a turned sheet is a finished sheet).
  The page's second ambient loop lives here: the skeleton's contour
  field carries the **grain shift** — a background noise layer
  translating 0 → 3px scrubbed to scroll (§5's ambient ration, shared
  with §6.3's breath: the two never run on the same section at once).
- **Choreography timeline (v2).** Transition (t₀ = link activation):
  t+0 sheet enters, rule leading → t+240ms full coverage, route swaps,
  new sheet at its head → t+480ms sheet exits; focus moves to the new
  sheet's `<h1>` → watchdog t+560ms: an incomplete transition is torn
  down and the destination shown plainly. Skeleton (per block, t₀ =
  content landed): plate fade 240ms → figure rules letter at +120ms →
  block surveyed.
- **State matrix (v2).** *Unsurveyed:* plates in true geometry,
  `aria-busy="true"` on the section. *Resolving:* 240ms fade.
  *Surveyed:* normal behaviour. *Turning:* outgoing sheet inert from
  t+0; destination live at reveal. *Hover:* links show §6.10's sweep;
  the transition has no hover state. *Focus:* keyboard activation of
  a link fires the same turn; focus lands on the destination's `<h1>`
  (tabindex −1). *Disabled / no-JS:* no unsurveyed states are ever
  rendered unresolved (server ships surveyed pages); plain
  navigation, no sweep.
- **Content merge.** The skeleton is the section's own unsurveyed
  self — same contours, same geometry; the transition's sheet is a
  sheet of the same chart stock that covers the old sheet to reveal
  the new one. Neither introduces a foreign object.
- **Failure fallback.** Skeletons exist only inside client-side
  fetches that own their 1200ms watchdog. The transition decorates
  links it can intercept and never breaks one it can't: modified
  clicks, new-tab and external links bypass it entirely; a slow
  destination holds the sheet at full coverage for up to 3s with the
  leading rule pulsing once per second (the party is still crossing),
  then aborts, retreats (200ms), and lets the native load proceed.
- **Reduced-motion variant.** Skeleton: plain `--sand` plates, content
  appears whole (120ms fade at most). Transition: no sweep — instant
  navigation with a 120ms escarpment outline flash on the sheet
  furniture to mark the change of sheet.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: transition
  440ms. <768px: transition 380ms, skeleton figure rules reduced to
  one per block, grain shift cut (mobile's ambient ration is spent
  on nothing — a phone chart is still).
- **Edge cases & failure modes (v2).** *Content that never arrives:*
  the unsurveyed block resolves into the theme's error note (§11) in
  the ledger voice ("THIS GROUND COULD NOT BE SURVEYED — THE PARTY
  WILL RETURN") with a retry that re-runs the fetch, not the whole
  page. *Same-sheet anchors:* no transition — anchors glide natively
  (§6.10). *Prefetched destination:* the 480ms ritual runs anyway;
  the ceremony is the point, not the wait.
- **Accessibility spec (v2).** During a turn the outgoing page is
  `inert`; at reveal, focus moves to the destination `<h1>` and a
  polite announcement names the new sheet ("Sheet: The Long Dunes").
  Unsurveyed sections announce once ("This ground is being surveyed")
  via the section's `aria-busy` resolution, not per block. The
  transition is skipped for reduced motion and for router-managed
  focus.
- **Performance budget & mobile variant.** Skeleton plates are CSS;
  the sheet is one transform on one fixed element with a pre-built
  SVG field. Mobile: the reduced variant above.
- **Tokens consumed (v2).** `--sand`, `--sand-deep`, `--escarpment`,
  `--hairline`, `--ease-drift`, `--ease-settle`, `--sheet-turn`
  (480ms), `--resolve-dur` (240ms), `--fallback-strip` (1200ms).

### 6.16 Field figures — camel-hour & elevation counters (page family: data)

- **What & why.** The chart's numbers arrive the way readings do: as
  their stations are reached, the figures count up in tabular
  Alegreya Sans — elevations in metres, distances in camel-hours —
  and come to rest on the true value. It belongs because in a survey
  the figures *are* the content arriving; a number that is simply
  printed is a claim, a number that is read off an instrument as you
  reach its station is a measurement. The count is a replay between
  zero (or the previous station's value) and the surveyed value —
  never a performance between invented ones.
- **Structure.** Every figure line (§3) in a station, stop or
  departure line carries its values as DOM text (the true figures,
  server-rendered). JS wraps each numeric run in a `.figure-run`
  span and, when its station arrives (§6.5's drop, §6.6's lighting,
  §6.11's tally), animates the displayed integer/decimal from its
  start value to the true value by rewriting the span's text —
  tabular figures mean the width never changes. Camel-hour values
  count in tenths (0.1 steps — the unit's honest precision, §12);
  elevations in whole metres; counts of stops in whole numbers.
- **Motion spec.** Duration by magnitude: ≤10 → 400ms; ≤100 → 650ms;
  elevations (hundreds–thousands) → 900ms; all `--ease-settle`
  (decelerating — an instrument settling, not a slot machine). Steps
  are whole increments at the value's precision, one per frame at
  most, so a 1,204m elevation visibly climbs through real readings.
  One-shot per figure per session; a figure that has read its value
  never re-reads.
- **Choreography timeline (v2).** Per figure: its station's arrival
  beat → +60ms: count begins → climbs at the eased rate → final value
  lands exactly as the station's own ceremony (§6.5's marker drop /
  §6.6's fill) completes — figure and marker agree about when the
  station was reached.
- **State matrix (v2).** *Rest:* the true figure, printed (markup
  state and terminal state are identical). *Counting:* ≤900ms, the
  span showing true intermediate readings. *Hover:* none. *Focus:*
  none — figures are text, reached by reading. *Scrolled-past:*
  printed. *Disabled / no-JS:* printed. *Reduced motion:* printed —
  the count is cut entire (below).
- **Content merge.** The counting number is the station's own figure,
  in its own figure line, at the moment the station is reached on the
  map — three views of one datum (§6.5, §6.6) arriving together. A
  figure with no station (a lone statistic in prose) does not count;
  it is simply printed, because it was not measured anywhere.
- **Failure fallback.** The true figure is the DOM text; JS masks it
  only while counting, and a 1000ms watchdog per figure restores the
  printed value regardless. A figure whose dataset value is absent
  does not exist as a span — the line prints without it (§6.5's
  omission rule).
- **Reduced-motion variant.** No counts. Figures stand printed — an
  instrument already read.
- **Breakpoints (v2).** Identical at all sizes (a reading is a
  reading); on <768px the elevation duration compresses to 700ms —
  the phone traveller's stations arrive faster.
- **Edge cases & failure modes (v2).** *Decimal camel-hours:* tenths
  step cleanly (3.5 counts 0.1 → 3.5 through tenths, never through
  hundredths displayed and rounded — the intermediate readings are
  true at the printed precision). *Figure revised by the publisher:*
  the printed value changes; the count replays to the new value on
  the next visit only if the station is re-surveyed (a new sheet
  date) — otherwise the correction appears as an erratum in the
  legend (§6.17), because charts correct by errata, not by quietly
  moving numbers. *Very large elevations (8,000m+):* duration caps
  at 1100ms with step size rising to keep the count legible.
- **Accessibility spec (v2).** The accessibility tree holds the true
  figure at all times (the count rewrites a visually-presented span
  whose `aria-hidden` twin carries the animation; the real text node
  is visually hidden during the count and restored after — or,
  simpler and preferred: the span is `aria-hidden` and an adjacent
  visually-hidden node holds the true figure permanently). Counts are
  never announced mid-flight.
- **Performance budget & mobile variant.** Text writes on ≤6 spans
  per frame worst case; no layout (tabular figures, reserved width).
  Mobile: the compressed durations above.
- **Tokens consumed (v2).** `--shadow-deep`, `--escarpment`,
  `--ease-settle`, `--count-sm` (400ms), `--count-md` (650ms),
  `--count-lg` (900ms).

### 6.17 The legend & scale bar (page family: chart furniture / trust)

- **What & why.** Every honest chart carries its key: what the lines
  mean, what the markers mean, the scale, and — in this theme — the
  workings of its one playful unit. The legend assembles in the sheet
  margin as the traveller first reaches it: each symbol drawn beside
  its meaning, the scale bar ruled to its true length, and the line
  that keeps the whole theme honest: "DISTANCES IN CAMEL-HOURS —
  1 CAMEL-HOUR = 4.2 KM AT LADEN PACE, BY THE CAMP'S OWN MEASUREMENT."
  It belongs because the theme's figures (§1) are only as good as the
  traveller's ability to check them, and the legend is where checking
  lives.
- **Structure.** A `--sand-deep` plate in the lee of the final
  section (or the sheet margin on long pages): rows of symbol +
  meaning (contour line / crest / lee / route / travelled route /
  survey marker / brass marker / station figure), each symbol a small
  inline SVG in its true page styling; the scale bar — a ruled bar
  whose segments are labelled in camel-hours *and* kilometres, its
  pixel length computed from the stated conversion and the sheet's
  declared scale; the conversion line; and the errata line, empty at
  first printing ("ERRATA: NONE AT THIS SURVEY") and the lawful home
  of every later correction (§6.16).
- **Motion spec.** Assembly on first entry: each row's symbol draws
  (its line or marker, 300ms `--ease-survey`) as its meaning fades
  in, rows staggered 70ms in reading order — the key being drawn the
  way the chart was. The scale bar rules itself left to right over
  600ms, its labels appearing at their segments. One-shot; the legend
  thereafter is furniture.
- **Choreography timeline (v2).** t+0: plate crosses 75% viewport →
  rows assemble at 70ms stagger (≤8 rows ≈ 560ms + draw) → scale bar
  rules at the final row's beat → conversion line fades in last — the
  honesty lands after the symbols it governs → legend at rest.
- **State matrix (v2).** *Rest:* the complete key, printed (markup
  state). *Assembling:* ≤1.2s, once. *Hover:* a row's symbol warms to
  full strength (the meaning is being pointed at). *Focus:* rows are
  not focusable; the legend contains no controls except an optional
  "PRINT THIS SHEET" text link (native print). *Scrolled-past:*
  printed. *Disabled / no-JS:* printed, fully drawn.
- **Content merge.** The legend's symbols are the page's actual
  symbols at their actual styles — sampled from the same SVG defs the
  sections use, so the key cannot drift from the chart it keys. The
  scale bar's length is computed from the conversion it prints: the
  honesty is geometric, not rhetorical.
- **Failure fallback.** The printed legend is the markup state; if a
  symbol's def is missing, its row prints the meaning with a hairline
  placeholder box — a key with a gap is corrected by errata, and the
  gate (§10) treats a missing symbol as a build error regardless.
- **Reduced-motion variant.** No assembly. The legend stands drawn.
- **Breakpoints (v2).** ≥1200px: two-column plate (symbols left,
  scale + conversion right). 768–1199px: one column, scale bar full
  width. <768px: one column; the scale bar shortens to its first two
  segments with the full bar in the print stylesheet (a phone's key
  is consulted, not exhibited).
- **Edge cases & failure modes (v2).** *A build using a symbol the
  legend lacks:* gate failure (§10) — the chart may not speak a
  language its key does not teach. *Conversion revised (a camp that
  walks faster):* the legend's line, the scale bar's length and
  every camel-hour figure derive from one build-time constant; change
  the constant and the sheet re-surveys itself consistently — a
  hand-edited figure anywhere is detectable by the gate's figure
  audit (§10).
- **Accessibility spec (v2).** The legend is a real list; symbols are
  `aria-hidden`, meanings are text. The scale bar carries a text
  equivalent ("Scale: one camel-hour, 4.2 kilometres, is 96 pixels at
  this sheet's scale" — generated from the same constants). Contrast:
  meanings in escarpment on `--sand-deep`, 8.31:1 ✓.
- **Performance budget & mobile variant.** ≤8 small stroke draws,
  once; symbols are shared defs (no duplicate path data). Mobile: the
  shortened-bar variant above.
- **Tokens consumed (v2).** `--sand-deep`, `--escarpment`,
  `--shadow-deep`, `--gold`, `--brass`, `--hairline`, `--ease-survey`,
  `--legend-draw` (300ms), `--scale-rule` (600ms).

### 6.18 The unmapped page (page family: 404 / empty state)

- **What & why.** The theme's 404 is a sheet of unmapped ground: the
  contour field thins to almost nothing, one survey marker stands
  planted with no figure, and the apparatus states the position
  honestly — "YOU ARE OFF THE SURVEYED SHEET" — with the routes back
  to mapped ground listed as departures. Empty states (a route with
  no departures this season, a search with no stops) use the same
  ground at section scale. It belongs because a chart's way of saying
  "not here" is to show the edge of the known world, not an error
  code wearing a costume.
- **Structure.** A lee-centred composition: a sparse contour field
  (2 paths at `--contour-faint`, the thinnest field on any sheet),
  the lone marker (escarpment, planted, no figure line — the one
  lawful figureless marker, §6.5's omission carried to its limit),
  the heading in Marcellus ("UNMAPPED GROUND"), two lines of
  apparatus prose (what was asked for, stated plainly; that it is not
  on this sheet), and the departures list: links to the sheet's real
  sections, set as §6.10 margin items. The HTTP 404 is real; the
  empty-state variant carries its own honest heading ("NO DEPARTURES
  THIS SEASON").
- **Motion spec.** Almost none, by law: the lone marker drops once on
  load (14px, 300ms `--ease-settle` — the surveyor planting a flag at
  the edge of the known) and the departures' hairlines behave per
  §6.10. The contour field does not drift (§6.3's breath is withheld
  — unmapped ground has no weather yet). Stillness is the message:
  there is nothing here to animate because there is nothing here.
- **Choreography timeline (v2).** t+0: sheet paints (marker planted
  in markup) → t+150ms: JS re-plants the marker with its single drop
  → t+450ms: permanent rest. Empty-state variant: no drop — the
  marker stands in the section from render.
- **State matrix (v2).** *Rest:* the unmapped sheet, complete.
  *Hover / focus:* departures per §6.10. *Active:* native navigation
  (§6.15's transition applies on the way back to mapped ground).
  *Touch:* identical. *Disabled / no-JS:* the planted marker and
  printed departures — the state a traveller actually needs.
- **Content merge.** The emptiness is the content: the thinned field
  is the map admitting its edge, and the departures are the sheet's
  real contents offered as ways back. Nothing is decorated; the
  absence is surveyed like everything else.
- **Failure fallback.** The page is its own fallback — static,
  complete, no JS required for any of it. (A 404 page that itself
  fails to load its enhancements has lost nothing.)
- **Reduced-motion variant.** No drop. The marker stands.
- **Breakpoints (v2).** ≥1200px: composition centred at 720px.
  768–1199px: 600px. <768px: full lee width, departures one column,
  marker at the composition's head.
- **Edge cases & failure modes (v2).** *A soft 404 (a stop removed
  from the route):* the unmapped page names the stop if the URL's
  slug matches a retired stop in the dataset ("THE WELL AT KHARGA IS
  NO LONGER ON THE ROUTE — IT WAS REMOVED AT THE 2026 SURVEY") — the
  chart remembers its own revisions; unknown slugs get the generic
  ground. *Search with results:* not this element — results are
  §6.12 plates; the unmapped ground is only for true absence.
- **Accessibility spec (v2).** The heading is the page's `<h1>`; the
  prose states the situation in words a screen reader delivers
  whole; the departures are a labelled nav ("Ways back to surveyed
  ground"). Contrast escarpment on sand throughout ✓. The marker is
  `aria-hidden`.
- **Performance budget & mobile variant.** The lightest page in the
  theme: one small SVG field, one 300ms transform. Mobile: as
  breakpoints.
- **Tokens consumed (v2).** `--sand`, `--contour-faint`, `--escarpment`,
  `--shadow-deep`, `--ease-settle`, `--marker-fall` (14px).

## 7. Page application map

- **Home (the crossing).** The full journey on one sheet: survey camp
  hero (§6.11) → two or three crest sections (§6.3, §6.4) → the
  survey redraw (§6.5) → the pinned route (§6.6) → stop cards for the
  season's other crossings (§6.12) → the caravan form (§6.13) → the
  legend (§6.17) → the night camp (§6.14). The compass rides the
  whole sheet (§6.7). This is the reference build; every other page
  type is a contraction of it.
- **Listing (the season's routes).** A sheet of plates: margin nav
  (§6.10), a short hero crest with the season's name, plate cards
  (§6.12) in mixed spans — one card per route, its figure line
  carrying that route's stops and total camel-hours — then the legend
  and camp. No pinned route (the routes are the list; pinning one
  would lie about the others), no survey redraw.
- **Detail (one stop, one crossing).** A single ground surveyed deep:
  hero crest naming the place, its survey profile (§6.5, if elevation
  data exists — else crest sections only), its plates, its figure
  lines, and the caravan form (§6.13) pre-set to this stop. The route
  stage appears in miniature: a static plate of the full route with
  this stop filled — the detail page shows where its place sits in
  the crossing, drawn, never pinned.
- **About (the survey party).** Crest sections for the party's
  history, told as past surveys: each era a crest, its stations the
  milestones (with real dates in the figure lines — a date is a
  figure under the one law, and a milestone without one is prose, not
  a station). The legend carries the party's own key: who surveys,
  how the camp measures a camel-hour, when the sheets are revised.
- **Contact / join (the ledger).** The caravan form (§6.13) is the
  page: a short hero crest, the ledger panel in the first lee, the
  camp as footer. No route stage, no cards — a traveller who has
  arrived at the ledger has finished crossing.
- **404 / empty.** The unmapped page (§6.18), at page scale or
  section scale respectively.
- **Print.** The sheet prints as a chart: contour fields at
  `--contour-faint`, the completed route, all figures printed, the
  legend complete, the compass omitted (a printed sheet has no
  bearing to keep). A Dune Cartography page that prints badly has
  failed at being a map.

## 8. Worked examples

### 8.1 The hero — departure from the well

A desert-crossing operator's home sheet opens. The sheet furniture
reads "SHEET 3 OF 7 · SURVEYED MARCH 2026 · SCALE: 1 CAMEL-HOUR =
96PX". The hero crest crosses at 38% height; on its left shoulder the
title "The Long Crossing" is lettered in Marcellus 64px, escarpment
on sand. In the lee, the standfirst: "Six stops from the well to the
kasbah, across the erg and over the surveyed ridge — the route our
caravans have walked since 1962." The departure line beneath:
"DEPARTS THE WELL · 6 STOPS · 11.5 CAMEL-HOURS IN ALL".

Timeline: t+0 the sheet paints complete — a no-JS visitor reads this
exact hero. With JS: t+80ms the headline ripple (§6.1) begins, three
rings of the crest's own geometry expanding from the title's
baseline; t+120ms the grains of "The Long Crossing" begin to settle
(§6.2), 40ms apart, the last landing at ~t+1340ms inside the passing
gust; t+400ms the departure figures count — stops 0 → 6 over 600ms,
camel-hours 0 → 11.5 over 900ms in tenths (§6.16) — landing as the
ripple's last ring fades. By t+1800ms the hero is a still chart. The
traveller scrolls; the hero's contours take up their drift (§6.3) and
the compass needle leaves 012°.

### 8.2 Mid-page — the ridge is surveyed, then crossed

Halfway down the sheet, the survey section: its lee text says the
ridge between the third and fourth stops was surveyed in March, and
beside it the profile stage (§6.5) waits with its datum rule. As the
traveller scrolls the section through its 120vh scrub range, the
profile draws from the dataset: 812m at the well-side station, rising
through 1,050m at the col, to the crest station at 1,204m — where the
marker drops 14px, its ring pulses, and "ELEV 1,204 M" letters in
beneath — then falling to 940m at the kasbah side. The final station
plants exactly as the lee paragraph naming the descent reaches the
reading line.

The next section is the route stage (§6.6): the map pins, and the
itinerary column begins. Reading "The Col — 3.5 camel-hours from the
well" lights the col's marker gold → escarpment and draws the segment
from the previous stop across the profile the traveller has just
watched being surveyed — the same elevations, the same order, one
dataset drawn twice. The traveller taps the kasbah's marker: the
ripple runs along its contour (§6.8), the brass marker falls 18px
with its single bounce (§6.9), and the kasbah's detail card opens in
the lee with its figure line — "2 CAMEL-HOURS FROM THE COL · ELEV
940 M" — and its prose. The hash becomes `#stop=kasbah`; the link
they send a friend arrives pre-marked.

### 8.3 Conversion — entered in the ledger

Below the route, the caravan form (§6.13) stands in its lee panel,
frame drawn, seal circle complete: "JOIN THE 2026 CROSSING". The
traveller writes their name on the first ruled line (the rule
thickens, the gold plate slides beneath), chooses the kasbah from
the stop radios — each row a place with its figures, not an option
code — and steps the party tally to ||| (3, with "3 TRAVELLERS" in
tabular figures beside the tallies). They press the seal: it dips
0.94 and holds its wet wash while the request crosses. The panel
answers with a drawn ledger line: "ENTERED AS NO. 214 — A PLACE FOR
3, JOINING AT THE KASBAH. WE WILL WRITE BEFORE THE NEW MOON." The
number is the server's sequence; had the same name and stop been
entered before, the line would read "ALREADY ENTERED AS NO. 198" —
the ledger keeps one entry per traveller, and says so.

## 9. Anti-slop — what makes THIS theme look cheap

1. **Stock-photo deserts.** A photograph of dunes as a hero background
   with the contour field laid over it. The chart is line-work; the
   moment a photo carries the terrain, the survey is a screensaver.
   Cure: terrain is generated SVG (§6.3) or it is a plate inside a
   frame (§6.12) — never a backdrop.
2. **Invented distances.** "About 3 camel-hours" typed because the
   itinerary looked thin. This is the one law broken (§1) — the
   theme's capital crime. Cure: figures derive from real distances by
   the printed conversion, or the stop carries no figure.
3. **Contours crossing text.** Full-strength lines wandering behind
   paragraphs because the lee was never enforced. Cure: §4's lee
   clearance, baked into the generated paths; the gate measures it.
4. **Percentages and progress bars.** "73% through the journey" —
   the theme measures in bearings and camel-hours. Cure: the compass
   (§6.7) is the only progress; grep for "%" in progress contexts.
5. **Night sections mid-page.** A dark band for "contrast" halfway
   down the sheet spends the camp's one night in the wrong place.
   Cure: `--night` is the footer and the dark scheme, nothing else.
6. **Gold text on sand.** Gilt lettering at 1.49:1, unreadable and
   pleased with itself. Cure: gold fills and glows; escarpment and
   `--shadow-deep` letter (§2's table is law).
7. **Every contour breathing.** Ambient loops multiplied until the
   chart shimmers like a screensaver. Cure: §5's ration — one breath,
   one grain shift, never on the same section.
8. **Bouncy markers.** A marker that bounces twice, wiggles, or
   pulses for attention after landing. Brass does not bounce twice.
   Cure: §6.9's single ≤2px overshoot, then furniture.
9. **The route as decoration.** A dashed line drawn across a hero
   with stops that are not the page's stops. Cure: one dataset —
   map, column, profile, cards, camp roll — or the route is not
   drawn at all.
10. **Camel-hours without the conversion.** The unit used as flavour
    with the workings nowhere printed. Cure: §6.17's legend line is
    a required element, and the gate fails a sheet whose legend omits
    it.
11. **Compass as clip-art.** A rose pasted in a corner that does not
    turn, or turns by a mapping nobody declared. Cure: §6.7's stated
    function (12° + progress × 160°) and its caption readout — an
    instrument or nothing.
12. **Uniform card grids.** Nine identical plates in a 3×3 lattice.
    Survey plates vary; so do the cards (§6.12's mixed spans). A
    lattice is a spreadsheet wearing the chart's clothes.

## 10. Quality gate

**Blocking — a build failing any of these may not ship:**

1. **Figure audit.** Every distance, elevation and count on the page
   traces to the dataset or the publisher's stated data; every
   camel-hour figure equals its kilometre source × (1/4.2), rounded
   to tenths. Sampled by hand against the legend's conversion.
2. **Lee clearance.** No contour at `--contour` strength passes
   within 24px of any text block at any scroll position (drift
   included) — checked by scripted screenshot sampling at 5 scroll
   depths per section.
3. **One pin.** Exactly one pinned stage per page (§6.6); exactly two
   ambient loops page-wide (§5); exactly one brass marker per map
   (§6.9).
4. **No-JS completeness.** With JavaScript disabled: every title
   risen, the route complete, all figures printed, the form
   submittable, the camp complete. Tested, not assumed.
5. **Reduced-motion completeness.** With `prefers-reduced-motion`:
   no drift, no breath, no counts, no falls, the compass fixed north,
   and every content item reachable and readable.
6. **Contrast.** Body text escarpment on sand (9.35:1) or sand on
   night (10.11:1) only; captions/labels `--shadow-deep` (4.60:1)
   minimum; no gold text on sand anywhere (grep + visual pass).
7. **Legend completeness.** Every symbol used on the sheet appears in
   the legend; the conversion line is present verbatim in substance;
   the scale bar's pixel length matches the stated scale ±2%.
8. **Dataset unity.** Map, column, profile, cards, departure line and
   camp roll render from one dataset — verified by changing one
   stop's elevation in the data and confirming every view follows.

**Standard — checked every build:**

9. Marcellus sets names only; Alegreya Sans sets records (§3 law 1).
10. Stagger orders are real orders (measurement, reading, route).
11. The ripple, settle and counts never re-fire on scroll-back.
12. Print stylesheet produces the completed chart (§7).
13. The unmapped page returns a real 404 and names retired stops.
14. Watchdogs verified: 1200ms skeleton strip, 1100ms title rise,
    1000ms figure restore, 560ms transition teardown.

## 11. Component inventory

Every component a real site in this theme needs, with its treatment.
Components the theme refuses are named with their in-world
replacement — a refusal without a replacement is a gap, not a style.

| Component | Treatment in this theme |
|---|---|
| Primary button | The seal device (§6.13): escarpment-bordered, lettered in apparatus caps, presses with the 180ms seal dip. One per view. |
| Secondary button / link | Text link with the drawn underline (§6.11): escarpment, underline draws on hover/focus in 200ms `--ease-survey`. |
| Text input | Ruled-line field (§6.13): transparent ground, 2px bottom rule, gold focus plate. Never a boxed input — the ledger has lines, not boxes. |
| Select | **Refused.** Choices of place are radio rows from the dataset (§6.13); choices of sheet are margin items (§6.10). A dropdown hides the ground it names. |
| Radio / checkbox | Radio: the stop rows (§6.13) — a small escarpment ring that fills with a brass centre. Checkbox: a survey tick-box, a drawn square that takes a hand-style tick stroke (draws 160ms) when checked. |
| Stepper | The tally stepper (§6.13): minus/plus as real buttons, the count as tally marks + tabular figure. |
| Table | A station table: hairline rules, figure columns tabular and right-aligned, the header row in apparatus caps on `--sand-deep`. Row hover warms the rule to `--shadow-deep` — tables in the lee do not ripple. |
| Badge / tag | **Refused** as chrome. A stop's status is a figure-line word ("DRY THIS SEASON") or a margin strike-through (§6.8). Pills are not chart furniture. |
| Alert / notice | The wind report: an apparatus line in the sheet margin or at a section's head, escarpment on `--sand-deep`, prefixed by its subject ("WIND: KHAMSIN FROM THE SOUTH-WEST, FROM THURSDAY"). Set at build/publish time; never animated in. A blocking alert (the crossing is cancelled) takes the ledger voice and a drawn double rule — still not a coloured banner. |
| Toast | **Refused.** Confirmations are ledger entries (§6.13) or margin notes — records that persist where they were made. Nothing in a survey evaporates in 4 seconds. |
| Modal | **Refused.** Detail opens in the lee as a card (§6.9) or a new sheet. A chart is not covered by its own UI. |
| Tooltip | **Refused.** A stop's detail is its card; a symbol's meaning is the legend (§6.17). Hover gives the ripple (§6.8), never a floating label. |
| Tabs | **Refused.** Sheets succeed one another (§6.15) or sections succeed down one sheet. Parallel hidden panels are unsurveyed ground pretending to be surveyed. |
| Accordion | The departures list (§6.18's grammar at section scale): a ground's detail unfolds downward in the lee, its crest hairline drawing as it opens, 300ms `--ease-settle`. One open at a time per section. |
| Pagination | Sheet succession: "SHEET 3 OF 7 — THE NEXT SHEET: THE LONG DUNES" as a margin item at the lee's foot (§6.10 grammar). Numbered page pills refused. |
| Breadcrumbs | The route itself, in miniature: the stops so far, in order, as text ("THE WELL › THE COL › —") in the margin. Only on detail sheets (§7). |
| Progress | The compass (§6.7). Progress bars and percentages refused (§9.4). |
| Search | The station index: a ruled field (§6.13 grammar) whose results are §6.12 plates; no results is §6.18's ground at section scale. |
| Card | The survey plate (§6.12). |
| Form errors | Ledger-voice notes under browned rules (§6.13, §12). |
| Loading | The unsurveyed sheet (§6.15). Spinners refused — the survey has no spinning part except the compass needle, and it does not spin for loading. |
| 404 / empty | The unmapped page (§6.18). |

## 12. Content & copywriting voice

The voice is the surveyor's: plain, measured, exact about figures and
dry about everything else. Two registers — the **chart** (names,
titles, apparatus) and the **record** (prose, notes, confirmations) —
and the conversion that governs the theme's signature unit:

> **1 camel-hour = 4.2 km at laden pace** — the distance a loaded
> caravan camel walks in one hour on flat ground. Distances print in
> camel-hours first (the journey's own measure) with kilometres in
> the figure line where a reader must plan by them: "3.5 CAMEL-HOURS
> (14.7 KM)". The conversion is stated in the legend (§6.17) and
> nowhere contradicted.

**Headline style.** Marcellus names places and crossings, ≤7 words,
no verbs of marketing. ✓ "The Long Crossing" · ✓ "Stations of the
Ridge Survey" · ✗ "Discover Your Ultimate Desert Adventure!" — the
chart does not exclaim; there are no exclamation marks anywhere on
the sheet, in any register.

**Label style.** Apparatus caps, short, factual. ✓ "DEPARTS THE WELL"
· ✓ "SURVEYED MARCH 2026" · ✗ "Don't miss out!" · ✗ "Limited
places!!" — scarcity, when real, is a figure in the ledger ("THE
CROSSING TAKES 14 — 3 PLACES REMAIN"), never an adjective.

**Figure style.** Every figure carries its unit and its precision:
elevations whole metres, camel-hours in tenths, bearings in three
digits ("BEARING 042°"). ✓ "ELEV 1,204 M" · ✗ "Elevation: high" ·
✗ "approx. 3-ish camel-hours" — approximation is stated as a figure
with its tolerance ("3.5 CAMEL-HOURS ± 0.5 BY THE CAMP'S MEASURE") or
not stated.

**Error voice (the ledger corrects).** Plain, specific, in the
surveyor's brown. ✓ "THE NAME IS NOT ENTERED — THE LEDGER CANNOT
SEAL AN UNSIGNED PAGE." · ✓ "THIS ADDRESS ENDS MID-WORD — THE CAMP'S
LETTERS GO BY CARAVAN AND MUST BE COMPLETE." · ✗ "Oops! Something
went wrong 😢" — no oops, no emoji, no vagueness: the note names the
field, the fault, and what to do.

**Empty-state voice.** ✓ "NO DEPARTURES THIS SEASON — THE WELLS ARE
DRY. THE NEXT SURVEY IS IN OCTOBER." · ✗ "Nothing here yet — check
back soon!" The empty ground states its reason and its next date, or
says it does not know (§6.18).

**Confirmation voice.** ✓ "ENTERED AS NO. 214 — WE WILL WRITE BEFORE
THE NEW MOON." A confirmation is a record with a number and a next
act with a date. ✗ "Awesome! You're in!" — the ledger does not cheer.

**Banned words:** ultimate, discover (as an imperative), adventure™,
oops, awesome, journey (as a metaphor for a signup), "don't miss".
**Owned words:** surveyed, entered, planted, crossed, laden, the lee,
the camp, by the camp's own measure.

## 13. Full-page scroll choreography map

The home sheet (§7), top to camp. Every beat in order; "sees" is the
visitor's experience, "feels" is the intended register.

| # | Beat | The visitor sees | Feels |
|---|---|---|---|
| 1 | Load | Ripple crosses the ridge; the title settles grain by grain; departure figures tally (§8.1) | Arrival at a surveyed place |
| 2 | Hero exit | Hero contours take up their three-speed drift; the needle leaves 012° | The ground beginning to move |
| 3 | First crest | The section title comes over its crest (§6.4); contours drift, lee stays calm | Crossing into new ground |
| 4 | First stations | Survey markers drop in a lee section as it is read; figures count (§6.16) | Being measured alongside |
| 5 | Survey section | The ridge profile draws with the scroll; stations plant at their fractions (§6.5) | Performing the survey |
| 6 | Route stage pins | The map takes over; the compass dims to 45% (§6.7) | The journey narrowing to the route |
| 7 | The crossing | Stops light in order; segments draw; the travelled route holds behind (§6.6) | Travelling, with a finger on the chart |
| 8 | A marking | The traveller drops the brass marker; a detail card opens in the lee (§6.9) | Claiming a place |
| 9 | Route complete | "ROUTE COMPLETE — 6 STOPS"; the stage releases; the compass returns | Arrival, first of two |
| 10 | Other crossings | Plate cards draw their frames and settle (§6.12) | Browsing the survey's plates |
| 11 | The ledger | The form's frame and seal draw; the traveller is entered (§6.13) | Commitment, recorded |
| 12 | The legend | The key assembles; the conversion line lands last (§6.17) | Being handed the means to check |
| 13 | The camp | Night falls; the horizon draws; the roll is called in route order; the needle rests at 172° (§6.14) | Journey's end, stillness |

**Reverse pass.** Scrolling up: drift offsets and the survey profile
retrace (they are functions of position); titles, markers, counts,
fills and the roll never un-happen (they are records). The needle
retraces its bearing — a traveller walking back faces back.

**Jump-scroll catch-up.** Anchor jumps and restored scroll positions
settle every scrubbed value to its mapped state on the first frame
and every one-shot record for ground above the landing point to its
completed state — the traveller arrives to a chart already surveyed
up to where they stand.

## 14. Whole-page performance budget

**Asset budget (home sheet).** HTML + CSS + JS ≤ 210KB gzipped
total; fonts: Marcellus (1 weight, subset to Latin + figures) +
Alegreya Sans (3 weights, subset) ≤ 95KB woff2; images: plates only,
≤90KB each, ≤6 per sheet, responsive + lazy below the first lee.
**Zero image assets for terrain** — all contour work is inline SVG
generated at build time (≤ 9 paths × ~60 points per section, ≤ 7
sections ≈ 26KB of path data in the HTML, gzip-friendly repeated
geometry).

**Animation frame budget.** The one shared rAF loop (lerp 0.12)
writes, per frame, at most: 9 contour transforms (3 sections in the
watch band × 3 layers), 1 profile dashoffset, 2 route dashoffsets,
1 needle rotation, 6 figure text writes — ≈ 20 style writes, all
compositor-friendly properties except the figure text (tabular,
width-stable, no reflow beyond the span). Long tasks: none over
50ms; path generation and dataset rendering happen at build time,
never in the browser. The loop sleeps when the tab is hidden and
when no watched section is in band.

**Cut order when the budget is exceeded** (cut in this order, never
skip ahead):
1. The grain shift (§6.15) — the second ambient loop goes first.
2. The contour breath (§6.3) — drift remains; breathing stops.
3. Crest drift on the far layer (two layers remain).
4. Plate settle (§6.12) — plates stand flat; frames still draw.
5. Figure counts (§6.16) — figures print directly.
6. The headline ripple (§6.1) — the settle remains.

**Never cut:** the route illumination (§6.6), the survey redraw
(§6.5), crest-clipped titles (§6.4), the brass marker (§6.9), the
compass (§6.7), any fallback or watchdog, any reduced-motion variant.
If the budget still fails after step 6, the build reduces sections
per sheet (the sheet splits, §4) — it does not cut the never-cut
list.

## 15. Build-order checklist

1. **Dataset first.** Stops, order, elevations, kilometre distances,
   the conversion constant — one source file. Nothing renders before
   the data is true (§1).
2. **The static sheet.** Full page with JS disabled as the target:
   contours at rest, route complete, figures printed, form native,
   camp complete. This is the fallback and the print view in one.
3. **Sheet furniture & margin nav** (§6.10) from the page's real
   headings.
4. **Contour generation.** Build-time path generator (seeded per
   section) with the lee clearance (§4) enforced geometrically;
   verify clearance by the §10 scripted sampling.
5. **The shared loop.** One rAF loop, lerp 0.12, watch-band logic,
   stall rule. No element ships its own loop.
6. **Crest system.** Crest-clipped titles (§6.4) wired to the shared
   crest geometry (§6.3).
7. **Drift.** §6.3's three layers + the single breath, with the
   ambient ration enforced in code review.
8. **The survey.** Profile path from the dataset (§6.5), stations,
   figure lines, aria-label generation.
9. **The route stage.** Sticky pin, reading-line tracking, segment
   draws, catch-up rules (§6.6); then the mobile static-plate
   variant.
10. **Instruments.** Compass (§6.7) with its declared mapping and
    caption; legend (§6.17) sampled from the same SVG defs.
11. **Interactions.** Ripple (§6.8), brass marker + hash state (§6.9),
    stop cards (§6.12).
12. **The ledger.** Form (§6.13) with native-first submission, error
    voice, entry-number handling, duplicate rule.
13. **State rituals.** Unsurveyed skeleton + sand-sheet transition
    (§6.15) with all watchdogs; unmapped page (§6.18).
14. **Camp.** Footer (§6.14) from the dataset; night scheme check
    (the camp is identical in both schemes).
15. **Reduced-motion pass & gate.** Every element's variant verified;
    the §10 gate run — figure audit and dataset-unity test last,
    signed by someone who did not build the sheet.
