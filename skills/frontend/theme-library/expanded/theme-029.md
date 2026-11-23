# 29. The Weather Map — Expanded (v1 + v2)

*Expansion written to `EXPANSION-STANDARD.md` v1 + the v2 deepening pass
(50x standard), ordered 2026-11-23. This file is the complete, buildable
specification of theme #29. The original library entry's identity is
preserved exactly — the broadsheet synoptic chart as information art,
the four palette anchors (Chart cream `#EEE9D6`, front red `#C23B2A`,
front blue `#2A4E7E`, isobar grey `#7A7E72`), Libre Franklin chart labels
with IBM Plex Mono observations, the pinned chart stage with the report
rail beside it, and all nine original signature elements — deepened,
never redesigned. Where this file and the short library entry disagree,
this file governs.*

**The one law of the theme, stated before everything else:** every
symbol meteorologically correct, every value real, every mapping
declared. A cold front's triangles point in the front's true direction
of travel; a wind barb's feathers sum to the station's true speed; an
isobar is labelled from the 4 hPa sequence and never crosses another.
And because the chart plots the *site's* subject, not the weather, the
page must print its mapping — what a station, a pressure, a front means
in this site's data — in the chart's key (§6.16), where any reader can
audit it. An invented reading, a decorative front pointing the wrong
way, or an undeclared mapping is not a rounding error in this theme —
it is a failed build. The synoptic chart has been trusted for a century
because sailors bet their lives on its conventions. This site inherits
that obligation.

---

## 1. Concept & world

The broadsheet weather page — the synoptic chart printed above the
shipping forecast, town-by-town tables beneath — treated as pure
information art and applied to any subject. The site's content is drawn
as a synoptic chart of itself: its regions, products, teams, or metrics
become stations plotted on a chart of the subject's own geography; its
trends become pressure systems; its conflicts and transitions become
fronts, drawn with correct symbols, moving the way fronts move. The
visitor does not read *about* the data and then look at a picture of
it. The chart is the data, plotted by the conventions forecasters have
used since the first telegrams arrived from outlying stations.

The world of the theme is the chart room at a synoptic hour: cream
chart paper, graticule ruled faintly over the region, a plotter's hand
entering observations in mono figures around station circles, fronts
ruled in red and blue, the whole sheet issued at a stated hour and
signed by a stated office. Nothing on the page is styled "like" a
weather map. It is built *as* one: the station model is the real WMO
station plot, the isobar interval is the real 4 hPa, the synoptic hours
are the real 00/06/12/18 UTC. The theme's luxury is correctness under
scrutiny — it ends with the original entry's invitation, printed on the
page: a note inviting pedants to check.

**Best-fit sites and audiences.** Data-rich subjects with a real
geography or a real topology that can honestly stand in for one:
regional service networks (stations = offices, pressure = load),
logistics and shipping (stations = ports), climate and environment
reporting (the literal case), sports leagues (stations = clubs,
fronts = form swings), finance dashboards that want print gravity
instead of glassmorphism, documentation for distributed systems
(stations = regions, fronts = incident boundaries), election and census
explainers (stations = constituencies). Audiences: readers who trust
print conventions — analysts, engineers, sailors, farmers, hobbyist
meteorologists, and anyone who has ever turned to the back page for the
chart. The theme flatters a knowledgeable reader: it rewards the
visitor who knows what a wind barb says.

**When NOT to use it.** When the subject has no mappable structure and
the "chart" would be a coastline invented to hold decorations — the
mapping law (§6.16) cannot be honoured, so the theme cannot be used.
When values change faster than a synoptic rhythm (live trading ticks,
chat): the chart is issued at hours, not streamed; a page that
re-plots every second betrays the world. When the audience needs
glanceable consumer warmth — wedding sites, children's products,
hospitality: the chart room is austere by design. When the data is
personal or grief-adjacent (health records, memorials): observations
are public facts in this world, and plotting a person's data as weather
is a category error. And never as a skin over a generic dashboard: if
the fronts could be deleted without losing information, they were
decoration, and this theme forbids decoration.

**The mapping, stated once here and printed on every page.** Each build
declares, in the key (§6.16): what a station is (the unit observed),
what the plotted values are (which real fields sit at the station
model's positions), what pressure represents (the charted quantity
whose gradient the isobars contour), what a front represents (a real
boundary between two regimes of that quantity), and what the synoptic
hours are (the page's sections, in order). Everything in §§5–6 is
written against that declaration. A build that cannot write its
declaration in five sentences does not build this theme.

---

## 2. Palette

Four anchors from the original entry, a closed set of derived tokens,
and a night-chart dark scheme. Ratios are measured (WCAG relative
luminance) against Chart cream unless stated.

| Token | Hex | Role | Usage ratio | Pairing / contrast notes |
|---|---|---|---|---|
| `--chart-cream` | `#EEE9D6` | Chart paper; the page ground and the chart sheet itself | ~72% of pixels | The only ground on light pages. Everything is plotted *on* it |
| `--front-red` | `#C23B2A` | Warm fronts, H centres, gale accents, the warm sector | ~4% | 4.4:1 on cream — large symbols, front lines, labels ≥14px bold only; never small text (use `--red-deep`) |
| `--front-blue` | `#2A4E7E` | Cold fronts, L centres, links, the cold sector | ~6% | 6.9:1 on cream — passes AA for text; the theme's working colour |
| `--isobar-grey` | `#7A7E72` | Isobars, graticule, secondary rules, apparatus text at display size | ~10% | 3.4:1 on cream — lines and graphics only; never text below 18px (use `--ink-soft`) |
| `--ink` | `#23282E` | Station values, body text, station circles, wind barbs | ~8% | 12.2:1 on cream — the plotter's hand; all observations print in it |
| `--ink-soft` | `#4A4A42` | Captions, table apparatus, key text | text only | 7.6:1 on cream — the smallest text colour permitted |
| `--red-deep` | `#A02E20` | Warm-front labels and gale text at small sizes | text only | 5.9:1 on cream — where `--front-red` would fail at size |
| `--blue-deep` | `#1E3A5F` | Cold-front labels at small sizes, link hover | text only | 9.4:1 on cream |
| `--cream-deep` | `#E2DABE` | Rail ground, table zebra, key panel fill | ~8% | One step below the sheet; panels sit *on* the chart, never float above it |
| `--cream-edge` | `#D5CCAB` | Chart sheet edge, hairline borders of panels | hairlines | The sheet's cut edge; 1px only |

**Pairing laws.** Fronts are the only elements that may carry pure
`--front-red` or `--front-blue` at full strength; a button, badge, or
heading in front red is a category error (it claims a warm front
exists there). H is always `--front-red`, L always `--front-blue` —
the international convention, not a brand choice. Isobars are always
`--isobar-grey`, 1.25px, never coloured by value. Station ink is always
`--ink`; a station's values never take the colour of the system they
sit in. The gale warning (§6.17) is the one permitted red field, and
only when a station truly crosses the gale threshold.

**Dark mode — the night chart.** Charts are also plotted for the night
watch, on the plotting room's dimmed sheet. `--chart-cream` becomes
`--chart-night #20262E`; `--ink` becomes `#E8E2CE` (12.5:1 on night);
`--front-red` lightens to `#DE6A52` (4.6:1 on night, symbols and large
labels only); `--front-blue` lightens to `#7FA3CC` (5.8:1); `--isobar-grey`
becomes `#8B9082` (lines only). The graticule stays the faintest layer.
Dark mode is a re-plotting, not an inversion: line weights grow 0.25px
because light lines on dark paper bloom, and the chart grain (§5) is
dropped — night paper is smooth. `prefers-color-scheme` selects it;
the issue line in the masthead prints "NIGHT CHART" when it is active,
because a real office would say so.

---

## 3. Typography

Two families, as in the original entry, with a strict division of
labour: **Libre Franklin** speaks for the chart room (labels, headings,
station names, the office's voice); **IBM Plex Mono** is the plotter's
hand (every observed value, every figure, every timestamp). A value set
in Franklin or a heading set in Mono is a mis-plot and fails the gate.

| Role | Font | Size / line-height | Tracking | Rules |
|---|---|---|---|---|
| Chart title (H1) | Libre Franklin 800 | 40px / 1.05 (≥1200), 32px (<768) | −0.01em | The region and the hour: "NORTH ATLANTIC — 12 UTC". Never a marketing headline |
| Section heading (station name) | Libre Franklin 700 | 22px / 1.2 | +0.04em, uppercase | Station names are gazetteer names: uppercase, letter-spaced like chart lettering |
| General situation (standfirst) | Libre Franklin 400 | 18px / 1.55 | 0 | The forecaster's paragraph (§6.11); present tense, observational |
| Body / report text | Libre Franklin 400 | 16.5px / 1.6 | 0 | Reports read as prose filed from the station |
| Chart labels | Libre Franklin 600 | 11–13px | +0.06em, uppercase | Placed on the chart beside their features; isobar labels sit *in* a break in their line, rotated to the line's angle |
| Observations (values) | IBM Plex Mono 500 | 13px on chart, 15px in rail | 0, tabular figures always | The station model's figures (§4); never proportional, never bold |
| Data tables | IBM Plex Mono 400/500 | 14px | 0, tabular | Town-by-town tables (§6.18); row height 36px |
| Apparatus (key, issue line, footnotes) | Libre Franklin 500 | 12px / 1.5 | +0.02em | The office's small print: issue hour, mapping declaration, pedant's note |
| Clock numerals | IBM Plex Mono 600 | 15px | 0 | Synoptic hours only: 00, 06, 12, 18 — the dial has no other stops |

**Type laws.** (1) Every number on the page is IBM Plex Mono with
`font-variant-numeric: tabular-nums` — a column of pressures must align
to the unit. (2) Pressure is always printed as the plotter codes it at
the station (three digits, §4) and in full hPa in tables and text
("1004 hPa"); the two never mix in one breath. (3) Wind is always
direction-then-speed in words ("NW 35 kt") and by barb on the chart;
never an arrow emoji, never a rotated chevron. (4) Uppercase is for
chart lettering and station names only; body copy is sentence case —
the chart shouts in symbols, not in type. (5) No italic anywhere on the
chart itself; italics are reserved for the rail's editorial asides, the
one place the office speaks personally.

---

## 4. Layout language

**The stage and the rail.** The layout signature, preserved from the
original entry: a pinned synoptic chart occupies the main stage while
station reports stream in a rail beside it, and the chart highlights
each station as its report arrives. At ≥1200px the stage is 62% of the
measure (max 880px) and the rail 38% (min 340px), separated by a 48px
gutter ruled with a single `--cream-edge` hairline — the fold of the
broadsheet. The chart pins for the full height of the rail's reports
and releases when the last report has been read (§6.3 governs the
synchronisation). At 768–1199px the stage is 56% and the rail 44%. At
<768px the pin is abolished: the chart sits at the head of the page at
full width, and each report carries a small static locator inset of the
chart with its own station ringed — the synchronisation survives as a
picture, not a mechanism.

**The chart.** Drawn to a fixed internal coordinate system of
1000 × 720 units (the sheet), scaled to its box. The graticule is ruled
every 100 units (the chart's declared degrees), `--isobar-grey` at
0.5px and 35% opacity — the faintest layer, below everything. The
coastline or region boundary of the subject's geography is drawn in
`--ink` at 1.5px, filled with nothing: chart paper shows through land
and sea alike, as on a real synoptic sheet where only the plotting
differs. Chart furniture is fixed by convention and never rearranged:
title block top-left (region, hour, issuing office), the key (§6.16)
bottom-left or directly beneath the sheet, the observation clock
(§6.7) in the masthead, H and L centres lettered at their stations of
maximum curvature.

**The station model.** Every station is plotted by the real WMO
station model, and the positions are law, not styling: the station
circle (Ø 10px, `--ink`, 1.5px stroke) at the station's coordinates;
the shaft leaves the circle toward the direction the wind comes *from*,
carrying the barbs (§6.5); the primary value (the theme's "temperature"
slot) at top-left of the circle, 13px mono; the secondary value
("dew point" slot) at bottom-left; the charted quantity ("pressure"
slot) at top-right, coded to three digits (1004 hPa plots as `040`,
996 as `960` — the leading 9 or 10 is dropped, the decimal implied);
the trend ("tendency" slot) at bottom-right with its +/− sign. A build
whose mapping puts a value in the wrong slot has mis-plotted the
station, and §10 fails it.

**Density and rhythm.** The page breathes at the synoptic rhythm:
sections are reports, and reports are separated by 96px of chart paper
at ≥1200px (64px <768) — the pause between stations filing. Tables are
dense (36px rows) because tables are apparatus; prose is loose (1.6
line-height) because prose is filed copy. Whitespace is chart paper:
empty sea. A region of the chart with no stations is not a gap to fill
but water to leave empty — the layout never invents a station to
balance a composition (§9).

**Section choreography.** Page order follows the filing order: masthead
with clock → general situation (§6.11) → the stage-and-rail (chart +
reports) → the town-by-town table (§6.18) → the key and mapping
(§6.16) → conversion (§6.13) → colophon (§6.14). The visitor reads the
day the way the office issues it: situation first, evidence second,
apparatus last.

---

## 5. Full motion system

Every motion term, in this theme's own language. The shared engine is
one `requestAnimationFrame` loop with lerp **0.14** driving all
scroll-scrubbed values (front offsets, breathing phase, clock
position); nothing else may start a second loop. Five named easings:
`--ease-advance` cubic-bezier(0.3, 0.6, 0.2, 1) — a front's steady push;
`--ease-contour` cubic-bezier(0.4, 0, 0.2, 1) — ink finding its line;
`--ease-snap-hour` cubic-bezier(0.34, 1.4, 0.64, 1) — the clock hand's
overshoot; `--ease-plot` cubic-bezier(0.25, 1, 0.5, 1) — a station
opening; `--ease-settle` cubic-bezier(0.16, 1, 0.3, 1) — values and
reports arriving. The global stall law, from the original entry: **if
any chart animation stalls beyond 1200ms, the fully drawn static chart
appears** — a watchdog per element, never `transitionend`.

- **Scroll-triggered reveals — station arrivals.** Each report section,
  on entry, fires its station's arrival: pulse (§6.3), values roll
  (§6.4), barb sets (§6.5). Trigger line: section top crossing 70% of
  viewport height. West-to-east stagger, 90ms per station of longitude,
  when several arrive in one scroll.
- **Scroll scrub — the front march (§6.1).** Front symbols advance
  along their lines in proportion to scroll through the stage, lerped
  at 0.14. The weather moves because the visitor reads.
- **Parallax — three chart layers.** Within the pinned chart, the
  graticule parallaxes slowest (0.92× scroll delta), isobars mid
  (0.97×), stations and values fastest (1.0×) — depth by draughtsman's
  layers, total displacement capped at 6px so plotted positions are
  never falsified by more than a hair.
- **Pinned scene — the stage.** The chart pins beside the rail for the
  reports' full length (§4); the pin is the theme's one pinned scene
  and no other element may pin.
- **Masked reveal — the expanding station circle.** On first load the
  chart reveals through a `clip-path: circle()` centred on the
  principal station, expanding 0 → 150% of the sheet over 1400ms
  `--ease-contour`, as if the plotter's compass opens the chart. The
  fully drawn chart is underneath from first paint (§6.12's skeleton
  rules); the mask is a performance over a finished sheet.
- **Blur-to-sharp — refused, with reason.** Observations are never
  blurred: a blurred reading is a mis-reading, and this theme's values
  are text first (§6.4). The single licensed softness is the chart
  grain's drift (below), which never touches a glyph.
- **Animated counters — rolling observations (§6.4).** Values roll
  from the previous synoptic hour's real reading to the current one —
  a replay between two true values, never from zero, never to an
  invented number. 600ms `--ease-settle`, tabular mono.
- **Progress indicator — the observation clock (§6.7).** The header
  clock advances through 00/06/12/18 UTC as the page's watches pass;
  its hand snaps with a 300ms `--ease-snap-hour` overshoot. There is no
  other progress bar on the page.
- **Marquee — refused, with reason.** Nothing on a synoptic chart
  crawls. Urgency is expressed by the gale warning (§6.17), which is
  still, red, and printed — a marquee would be a siren in a chart room.
- **Kinetic typography — refused, with reason.** Letters on a chart are
  plotted, not performed. Headlines arrive by the issue, whole.
- **Ambient loops — isobar breathing (§6.6) and grain drift.** Isobars
  undulate ±2px on a 9s sine, phase-offset per line; the chart grain
  drifts 14px over 26s like high cloud. Both pause off-screen, both
  die under reduced motion.
- **Micro-interactions.** Station expansion on hover/focus (§6.8),
  pin-to-rail on click (§6.8), the time-step buttons' front-step
  (§6.9), form fields that plot like station entries (§6.13).
- **Page transition — the time-step (§6.9).** Navigation crossfades to
  the next observation time with the fronts visibly advanced one step:
  to leave the page is to move the weather on.
- **Skeleton / loading — the unplotted sheet (§6.12).** Loading shows
  the sheet, graticule, and coastline with station circles hollow —
  "awaiting observations" — and plots each station as its data lands.
- **Reduced motion (global).** The chart stands static at the latest
  observation, fronts at their final positions, all reports listed,
  values printed. Every element's own variant is specified in §6.

---

## 6. Signature elements

### 6.1 Front march

- **What & why.** The theme's signature and its thesis performed. Cold
  fronts carry blue triangles, warm fronts red semicircles, and the
  symbols sit *on* their front lines pointing in the front's true
  direction of travel — the way the front is actually moving across
  the chart. Scrolling scrubs the advance: as the visitor reads down
  the reports, the fronts march along their lines, the weather system
  itself moving through the page's hours. It belongs here because a
  front that does not move, or moves the wrong way, is not a front —
  it is clip art. Here the motion is the meteorology.
- **Structure.** Each front is an SVG `<path>` (the line, 2.5px,
  `--front-blue` or `--front-red`) plus a group of symbol glyphs
  (triangles 14px long, semicircles r 7px) placed along the path by
  arc-length parameter `s` via `getPointAtLength`, spaced 56 units
  apart, each rotated to the path tangent at its position. Symbols are
  clipped to the sheet. The scrub offset `o` (0 → 140 units across the
  stage's scroll range) shifts every symbol's `s`; symbols that run
  off the leading end are hidden, new symbols enter at the trailing
  end at the same spacing — the front advances as a body, its length
  constant, exactly as a plotted front translates. Occluded fronts
  alternate triangle/semicircle on the same side; stationary fronts
  carry symbols on opposite sides and, by law, do not march.
- **Motion spec.** Scrub: `o` = lerped scroll progress (shared loop,
  lerp 0.14) × 140 units, applied per frame to symbol positions only —
  the line itself never moves, because the line is where the front
  *is* at issue time and the symbols show where it is *going*.
  Entrance: on first plot, the line draws 900ms `--ease-contour`, then
  symbols fade-plot in sequence along the line at 60ms intervals,
  trailing end first (the front arrives from where it came from).
  Direction law: symbols always point along the local tangent in the
  declared direction of travel (§6.16's key states it); a front whose
  travel direction reverses between issues is re-plotted, never
  animated backwards.
- **States.** *Rest (pre-scroll):* symbols at `o = 0`, the issue-time
  position. *Scrubbing:* symbols offset by `o`. *Scrolled-past:*
  symbols rest at full advance (o = 140) — the forecast position,
  which the key labels as such. *Hover:* none — fronts are not
  controls. *No-JS:* symbols printed at the forecast position with the
  key's note; the chart is complete.
- **Content merge.** The fronts cross the same chart the reports
  describe, and each front is a real boundary in the site's declared
  mapping — the boundary between two regimes of the charted quantity.
  Delete the march and the front still separates the regimes; delete
  the front and two sections of the page lose their relationship.
- **Failure fallback.** Symbols are in the DOM at their forecast
  positions by default; JS rewinds them to `o = 0` only when the loop
  is running. If `getPointAtLength` throws or the loop stalls 1200ms,
  the watchdog leaves every symbol at its DOM position — a fully
  plotted chart. A front path that fails to load renders its symbols
  along the straight chord between its endpoints rather than vanishing.
- **Reduced-motion variant.** No march, no draw: fronts printed
  complete at forecast position. The key's note carries the direction
  of travel in words ("advancing SE at 15 kt"), so the information
  survives without the motion.
- **Performance budget & mobile variant.** Per front: ≤ 24 symbols,
  position writes only for fronts on the pinned stage; ≤ 0.8ms/frame
  for all fronts together. Mobile: symbol spacing widens to 72 units
  (fewer, larger glyphs: triangles 16px), advance range 100 units.

#### 6.1 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| 0ms | Chart complete in DOM, symbols at forecast position |
| JS ready | Symbols rewind to issue position over 0ms (no visible jump: chart still masked by §5's circle reveal) |
| +200ms | Front lines draw, 900ms `--ease-contour`, cold before warm (the cold air pushes) |
| +1100ms | Symbols plot in along each line, 60ms apart, trailing end first |
| First scroll into stage | Scrub engages; symbols advance with lerped scroll, 0.14 |
| Scroll rest | Symbols settle at the exact offset for the resting progress within 300ms |
| Stage exit | Symbols rest at full advance; loop stops writing this front |

#### 6.1 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Issue position, lines drawn | Same |
| Hover | No change (not a control) | n/a |
| Focus | Fronts are not focusable; the chart's accessible name states each front's direction in text | Same |
| Active | n/a | n/a |
| Scrolled-past | Forecast position, labelled in key | Same |
| Disabled / no-JS | Forecast position, complete chart | Same |

#### 6.1 v2 — Breakpoint behaviour

≥1200px: full spec, 56-unit spacing, 140-unit advance. 768–1199px:
spacing 64 units, advance 120 units. <768px: spacing 72 units, advance
100 units, and the chart is unpinned (§4), so the scrub range is the
chart's own pass through the viewport rather than the rail's length.

#### 6.1 v2 — Edge cases & failure modes

*Front longer than the sheet:* symbols clip at the sheet edge; the
front is understood to continue off-chart, as real fronts do. *Two
fronts converging on one low:* symbols stop 20 units short of the
centre so glyphs never collide at the L. *Scroll-back:* the offset is
a pure function of scroll position and reverses exactly — the weather
un-advances, which is correct for a scrub. *Very fast fling:* the lerp
settles symbols to the true offset; a 300ms settle timer forces the
exact final positions at scroll rest. *A front with no declared travel
direction in the data:* it is plotted as a stationary front (symbols
both sides, no march) — the theme never invents a direction.

#### 6.1 v2 — Accessibility spec

Fronts are data, announced in text: the chart's `role="img"` label and
the adjacent reports state each front's type, position, and direction
("Cold front lying from the L south-west to the coast, advancing
south-east"). No meaning rides on colour alone — triangle vs
semicircle shape carries the type, and the key (§6.16) prints the
shapes beside their names. The scrub is scroll-driven, needs no focus,
and strands nothing: every report the fronts relate is ordinary text
in the rail.

#### 6.1 v2 — Tokens consumed

`--front-red`, `--front-blue`, `--ease-contour`, `--ease-advance`,
`--dur-draw-front` (900ms), `--front-advance` (140 units),
`--symbol-gap` (56 units), `--loop-lerp` (0.14).

### 6.2 Isobar contouring

- **What & why.** The isobars — lines of equal value of the charted
  quantity — draw themselves around the highs and lows in pressure
  order, the way a plotter contours an analysis: out of the low's
  centre, ring by ring, then around the high. It belongs here because
  the isobars are the chart's argument: their spacing *is* the gradient,
  and watching them contour in sequence teaches the visitor to read
  the chart's pressure field before a single report is read.
- **Structure.** Each isobar is an SVG `<path>`, 1.25px `--isobar-grey`,
  unclosed only where it exits the sheet. Every isobar carries its
  value from the 4 hPa sequence (…, 992, 996, 1000, 1004, 1008, …) as a
  label set into a 34-unit break in the line, rotated to the line's
  angle at that point, 11px Franklin 600. Contours are grouped per
  system: the low's family (centre value first, ascending outward) and
  the high's family (centre value first, descending outward). Isobars
  never cross — a build whose paths intersect has drawn impossible air
  and fails §10.
- **Motion spec.** Draw: `stroke-dashoffset` from full length to 0,
  1100ms `--ease-contour` per line, staggered 120ms in pressure order
  (low family first, then the high's — the plotter analyses the low
  before the high because the fronts hang off it). Re-contour: when a
  new chart region enters (a second chart on a long page), its isobars
  contour on the same order as it arrives. The draw runs once per
  chart per visit; scrolling away and back does not re-analyse.
- **States.** *Rest:* fully contoured chart. *Drawing:* lines in
  pressure order, labels fade in at each line's completion (150ms).
  *Hover:* none. *Scrolled-past:* contoured, breathing (§6.6) if in
  view. *No-JS:* all lines printed with labels — the analysis is the
  content, so the DOM ships it finished.
- **Content merge.** The lines contour the site's real charted
  quantity under the declared mapping; their values are computed from
  the data (the build interpolates contours from station values, it
  does not draw plausible-looking rings). Ring spacing therefore means
  something: tight rings, steep gradient, and the reports in the rail
  say why.
- **Failure fallback.** Paths render fully drawn by default; JS arms
  the dash state only for lines it will animate, and the 1200ms
  watchdog completes any line still drawing. If a contour's computed
  path self-intersects (bad interpolation), the build falls back to
  that system's station values printed without the offending ring and
  flags it in the key — a missing isobar is honest, a crossing one is
  a lie.
- **Reduced-motion variant.** No draw: the analysis stands complete.
  Labels present. Nothing about the information changes.
- **Performance budget & mobile variant.** ≤ 14 isobars per chart;
  dash animation on composited paths only during the 1100ms draw.
  Mobile: interval doubles to 8 hPa (half the lines) below 768px —
  the standard small-chart practice — and labels drop to every second
  line, values still in sequence.

#### 6.2 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| 0ms | All isobars printed in DOM with labels |
| JS ready | Dash states armed only on the entering chart's lines |
| Chart reveal (§5) midpoint | Low's centre isobar begins, 1100ms |
| +120ms × n | Next isobar in pressure order begins |
| Each line completes | Its hPa label fades in, 150ms |
| Low family done | 240ms pause — the plotter lifts the pen — then the high's family |
| All done | Breathing (§6.6) fades in over 1s; contouring never repeats this visit |

#### 6.2 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Fully contoured | Fully contoured (8 hPa interval) |
| Hover | No change | n/a |
| Focus | Isobars are not focusable; values are in the table (§6.18) as text | Same |
| Active | n/a | n/a |
| Scrolled-past | Contoured; breathing paused off-screen | Same |
| Disabled / no-JS | Fully contoured with labels | Same |

#### 6.2 v2 — Breakpoint behaviour

≥1200px: 4 hPa interval, ≤14 lines, all labelled. 768–1199px: 4 hPa,
labels on alternate lines. <768px: 8 hPa interval, labels on alternate
lines, line weight 1.5px (small screens need the ink).

#### 6.2 v2 — Edge cases & failure modes

*A col (saddle) between systems:* contours of the two families
approach but never touch; the build leaves the saddle un-contoured
rather than joining lines — correct practice. *A system centred
off-chart:* its rings enter from the sheet edge unclosed, labelled at
the edge. *Data too sparse to contour (fewer than 5 stations):* no
isobars are drawn at all; the key states "Analysis not drawn —
insufficient reports", and the chart carries stations and fronts only.
Inventing a smooth field from three points is the theme's cardinal
sin. *Resize:* paths are in sheet coordinates and scale; dash states
are not re-armed.

#### 6.2 v2 — Accessibility spec

Isobars are graphical data with a full text equivalent: the
town-by-town table (§6.18) prints every station's value, and the
general situation (§6.11) states the gradient in words ("a steep
gradient over the north"). Labels are real SVG `<text>`, in reading
order after the chart title. Contrast: isobar grey is a line, not
text; its labels print in `--ink-soft` (7.6:1), never in the grey.

#### 6.2 v2 — Tokens consumed

`--isobar-grey`, `--ink-soft`, `--ease-contour`, `--dur-contour`
(1100ms), `--stagger-contour` (120ms), `--interval-hpa` (4),
`--watchdog-chart` (1200ms).

---

### 6.3 Station arrival pulse

- **What & why.** When a report section in the rail enters, its
  station on the pinned chart pulses once — a ring expanding from the
  station circle and fading — so the visitor sees *where* the report
  they are reading comes from at the moment they begin reading it. It
  belongs here because the theme's whole layout is the synchronisation
  of chart and rail; the pulse is that synchronisation made visible,
  once, at the only moment it is needed.
- **Structure.** An SVG `<circle>` per station, r animated 6 → 26px,
  stroke `--ink` 1.5px, fill none, centred on the station circle,
  `pointer-events: none`, living in the chart's station layer (top).
  One pulse element is reused across stations (moved to the arriving
  station's coordinates) — 40 stations do not mean 40 rings.
- **Motion spec.** Trigger: the report section's top crossing 70% of
  viewport height (IntersectionObserver, threshold on the rail
  sections). Pulse: r 6 → 26px and opacity 0.55 → 0 over 700ms
  `--ease-settle`, once per entry. An entry counts only after the
  section has been fully out of view; rapid scroll fires pulses in
  filing order with a 90ms minimum gap, skipping any station whose
  report was scrolled past unread (its pulse is spent silently — the
  chart does not shout about reports already gone). On <768px (no pin),
  the pulse fires on the report's own locator inset instead.
- **States.** *Rest:* no ring. *Pulsing:* 700ms, once. *Scrolled-past:*
  no ring; the station keeps its plotted values. *Hover:* none (hover
  is §6.8's). *Disabled:* if the observer never fires (very short
  page, everything visible at load), all stations pulse in filing
  order once at load, west to east, 90ms apart — arrival still happens.
- **Content merge.** The ring is drawn around the station whose real
  report is entering; it carries no content of its own and points at
  content that exists. Remove it and the synchronisation is merely
  less visible, never broken.
- **Failure fallback.** The pulse is pure enhancement: if the observer
  or the loop fails, nothing is missing — reports and stations are all
  in the DOM. A pulse interrupted by a tab switch simply does not
  complete; it is never re-fired for that entry.
- **Reduced-motion variant.** No expanding ring. The arriving station's
  circle thickens 1.5px → 2.5px for 600ms — emphasis by line weight,
  the plotter underlining the station he is reading.
- **Performance budget & mobile variant.** One circle, transform/opacity
  only; negligible. Mobile: the pulse targets the locator inset's ring
  (r 4 → 16px, 600ms).

#### 6.3 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| t₀ | Report section top crosses 70% vh |
| t₀ + 0ms | Pulse ring placed at the station, r 6, opacity 0.55 |
| t₀ + 350ms | r ≈ 17px, opacity ≈ 0.25 |
| t₀ + 700ms | r 26px, opacity 0; ring removed from the layer |
| Same beat | The station's values begin their roll (§6.4) and its barb sets (§6.5) — arrival is one event with three hands |

#### 6.3 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | No ring | No ring |
| Hover | No change (expansion is §6.8) | n/a |
| Focus | A report focused by keyboard fires its station's pulse on focus entry | Same |
| Active | n/a | n/a |
| Scrolled-past | Spent; no re-pulse without a full exit and re-entry | Same |
| Disabled / no-JS | No ring; chart and rail both complete | Same |

#### 6.3 v2 — Breakpoint behaviour

≥1200px and 768–1199px: pulse on the pinned chart as specced.
<768px: chart unpinned; pulse fires on each report's locator inset;
if the inset is off-screen when its report is read, no pulse is owed —
the inset is a picture, and pictures do not perform for an empty room.

#### 6.3 v2 — Edge cases & failure modes

*Many reports entering at once (page restored mid-scroll):* pulses
queue in filing order, 90ms apart, capped at 4; the rest are marked
arrived silently. *The pinned chart released (rail exhausted):* later
sections have no stations and fire nothing. *A report with no station
(editorial sections):* no pulse — the absence is correct; not every
paragraph is an observation. *Browser find-in-page jumping:* treated
as an entry; one pulse, no queue.

#### 6.3 v2 — Accessibility spec

The pulse is decorative synchronisation, `aria-hidden`, never
announced. The information it carries — which station this report is
from — is in the report's own heading ("LERWICK — …") and in the
locator inset's alt text on mobile. Keyboard focus entering a report
fires the same pulse (§6.3 state matrix), so the synchronisation is
not pointer-only.

#### 6.3 v2 — Tokens consumed

`--ink`, `--ease-settle`, `--dur-pulse` (700ms), `--pulse-r0` (6px),
`--pulse-r1` (26px), `--trigger-line` (70% vh).

### 6.4 Rolling observations

- **What & why.** Every plotted value — the station's figures on the
  chart and in its report — rolls from the previous synoptic hour's
  reading to the current reading when the station arrives. In this
  theme the data motion is total: numbers are the content, and their
  arrival is the animation. The roll is a *replay between two true
  values*: the office received the new observation, and the plotter
  re-enters the figure. It never counts from zero and never lands
  anywhere but the real reading.
- **Structure.** Each value is a `<span class="obs">` in IBM Plex Mono
  tabular figures, carrying `data-prev` and `data-now` (the two real
  readings). On the chart, values sit at their station-model slots
  (§4); in the rail and tables, the same component is reused. Pressure
  rolls in its coded three-digit form on the chart (`038` → `040`)
  and in full hPa in text. Wind rolls direction in words through the
  compass points between the two real directions (NW → N → NE is a
  veer through north, never a jump), speed as a figure.
- **Motion spec.** Trigger: the station's arrival (§6.3's beat).
  Duration 600ms `--ease-settle`; figures interpolate linearly in
  value and render rounded to the value's own precision (temperatures
  to 0.1, pressure to whole hPa, wind speed to whole knots). Values at
  one station stagger 70ms apart in plotting order: primary,
  secondary, pressure, tendency — the order the plotter's hand moves.
  A value whose reading is unchanged between hours does not roll; the
  plotter does not re-enter a figure that stands.
- **States.** *Rest (pre-arrival):* the **current** value is printed —
  the DOM always shows the latest observation; JS rewinds to `prev`
  only at the moment it arms the arrival, in the same frame as the
  pulse, so no visitor ever reads a stale figure as current.
  *Rolling:* 600ms between the two true values. *Settled:* current
  value, terminal. *Scrolled-past:* current value. *No-JS:* current
  value everywhere; the previous hour lives in the table's "prev"
  column (§6.18) as text.
- **Content merge.** The rolling figures *are* the observations; the
  animation is the act of plotting them. There is no decorative
  counter anywhere in the theme — §6.7's clock and §6.18's table use
  the same component, and every number it has ever shown is a reading.
- **Failure fallback.** If the roll's rAF stalls, a 700ms watchdog
  snaps the value to `data-now`. If `data-prev` is missing (a station
  commissioned this hour), the value does not roll — it plots in with
  a 150ms fade, and the report says "first reports this hour". A value
  that fails validation (non-numeric in data) renders as the plotter's
  missing-observation mark `///` — the real convention — never as 0.
- **Reduced-motion variant.** No roll. Values print at the current
  reading; the previous hour is available in the table. Nothing is
  counted, anywhere, under reduced motion in this theme.
- **Performance budget & mobile variant.** ≤ 4 values per station, ≤ 6
  stations rolling concurrently (the arrival stagger enforces this
  naturally); text writes only, no layout (tabular figures, fixed
  precision). Mobile: identical — the roll is the theme's cheapest
  signature and is never cut.

#### 6.4 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| t₀ | Station arrival (§6.3 pulse begins); values rewound to prev in the same frame |
| t₀ + 0ms | Primary value begins its roll |
| t₀ + 70ms × n | Secondary, pressure, tendency follow in plotting order |
| t₀ + 600ms | Primary settles on the true current reading |
| t₀ + 810ms | Last value settled; station fully plotted |
| t₀ + 700ms (watchdog) | Any value not settled is snapped to current |

#### 6.4 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Current values printed | Same |
| Hover | No change | n/a |
| Focus | A value inside a focused report is already settled (focus fires arrival first, §6.3) | Same |
| Active | n/a | n/a |
| Scrolled-past | Current values | Same |
| Disabled / no-JS | Current values; prev in the table column | Same |

#### 6.4 v2 — Breakpoint behaviour

≥1200px: chart values 13px, rail values 15px. 768–1199px: chart values
12px. <768px: the full station plot does not fit the unpinned chart —
chart stations show circle + primary value only, and the complete plot
lives in each report and in the table, where the roll runs identically.

#### 6.4 v2 — Edge cases & failure modes

*Negative and sub-zero values:* the roll interpolates through zero
correctly and the minus sign is part of the figure's width from the
start (no layout shift when it appears). *Pressure crossing the
coding boundary (999 → 1002):* the coded form rolls `990` → `002`
through the boundary as the plotter would write the sequence; the
table's full-hPa column removes all ambiguity. *A value revised after
issue (corrected observation):* the report prints the correction with
the plotter's convention — the old figure struck through once, the new
figure beside it, and no roll: corrections are not arrivals. *Huge
ranges (a front passage swings pressure 18 hPa):* the roll stays
600ms; speed of counting is not drama, and the tendency slot (+/−)
carries the story.

#### 6.4 v2 — Accessibility spec

Values are plain text in reading order; the roll is a visual replay
and is `aria-hidden` during its 600ms — the settled current value is
what the accessibility tree ever exposes (the span's text is swapped
to `data-now` for AT at arm time, animated visually only). Tabular
figures guarantee screen-reader and sighted reading agree digit for
digit. Contrast: `--ink` on cream 12.2:1 at every state.

#### 6.4 v2 — Tokens consumed

`--ink`, `--ease-settle`, `--dur-roll` (600ms), `--stagger-plot`
(70ms), `--watchdog-roll` (700ms), `--font-obs` (IBM Plex Mono).

---

### 6.5 Wind barb spin

- **What & why.** One station on every chart is the gale station — the
  station whose wind (under the declared mapping, the mapped quantity
  in its wind slot) crosses the gale threshold of 34 kt, Beaufort
  force 8. When it arrives, its wind barb rotates once to point at its
  true direction, feathers summing to its true speed: a correct
  meteorological glyph performing its own meaning. It belongs here
  because the barb is the chart's most compressed sentence — direction
  and speed in one mark — and the spin is the plotter drawing the
  shaft and laying the feathers.
- **Structure.** An SVG group at the station: shaft line leaving the
  circle toward the direction the wind comes *from* (a NW wind's shaft
  points NW — the air arrives from there), feathers at the shaft's far
  end: long feather = 10 kt, short feather = 5 kt, filled pennant =
  50 kt, combined to the true speed rounded to the nearest 5 kt (35 kt
  plots as three long + one short). Calm plots as a double circle
  around the station and never spins. The barb is drawn in `--ink`,
  1.5px, feather length 9 units, shaft length 26 units.
- **Motion spec.** Trigger: the gale station's arrival (§6.3). The
  shaft starts pointing north (the plotter's resting hand) and rotates
  by the shortest arc to the true direction over 720ms with an
  easeOut cubic (`--ease-settle`'s sharper sibling,
  cubic-bezier(0.22, 1, 0.36, 1)); feathers fade-plot in sequence from
  the shaft outward at 90ms intervals as the rotation completes, so
  the speed is read after the direction — the order a forecaster reads
  a barb. Exactly once per arrival; re-entry after full exit re-arms
  it (a new hour, a new plot). Only the gale station spins; other
  stations' barbs are plotted statically at their true angles from
  first paint — singling out every barb would make none of them the
  gale.
- **States.** *Rest:* barb at true direction with true feathers (the
  DOM state). *Spinning:* 720ms from north, once. *Settled:* true
  barb, terminal. *Hover:* none (expansion is §6.8, and the expanded
  string states the wind in words). *No-JS:* true barb printed.
- **Content merge.** The glyph is the station's wind observation —
  remove the spin and the barb still says NW 35 kt to anyone who can
  read it; remove the barb and the station has no wind. The animation
  adds nothing but the drawing of it.
- **Failure fallback.** The barb ships drawn at its true angle; JS
  rewinds it to north only when arming the arrival. If the rotation
  stalls, the 1200ms chart watchdog snaps it to the true angle with
  feathers shown. A station whose speed is missing plots the shaft
  with no feathers and the report prints `///` for wind (§6.4's
  convention).
- **Reduced-motion variant.** No spin, no feather sequence: the true
  barb stands plotted. The gale is announced by §6.17's warning line,
  which reduced motion keeps.
- **Performance budget & mobile variant.** One SVG group, one rotation;
  negligible. Mobile: the barb is part of the full station plot, which
  lives in the report (§6.4's breakpoint rule), and the spin runs
  there at the same 720ms; the unpinned chart's locator inset shows
  the settled barb only.

#### 6.5 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| t₀ | Gale station arrives (§6.3 pulse); shaft rewound to north, feathers hidden |
| t₀ + 0–720ms | Shaft rotates by the shortest arc to the true direction, easeOut |
| t₀ + 720ms | Direction settled; first feather plots (150ms fade) |
| t₀ + 810ms × n | Remaining feathers plot outward, 90ms apart |
| t₀ + ~1100ms | Barb complete: direction and speed readable |
| Watchdog 1200ms | Any incomplete state snaps to the true barb |

#### 6.5 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | True barb plotted | True barb (in report plot) |
| Hover | No change | n/a |
| Focus | Gale station focused via §6.8 shows wind in words | Same |
| Active | n/a | n/a |
| Scrolled-past | True barb | Same |
| Disabled / no-JS | True barb printed | Same |

#### 6.5 v2 — Breakpoint behaviour

≥1200px: barb on the chart at the gale station, full spec. 768–1199px:
same, shaft 24 units. <768px: spin runs on the report's full station
plot; the chart inset carries the settled barb.

#### 6.5 v2 — Edge cases & failure modes

*Two stations over the gale threshold:* the higher wind is the gale
station and spins; the other plots statically and is still named in
§6.17's warning ("gales at LERWICK and FAIR ISLE"). *Speed exactly on
a 5 kt boundary:* rounds to the plotted convention (nearest 5, halves
up — 32.5 kt is not a real reading; instrument precision is 1 kt and
plotting precision is 5, both stated in the key). *A veering wind
between hours:* the barb plots the current hour only; the veer is
told by §6.4's word-roll in the report. *Direction variable (VRB):*
no shaft; the station circle carries a small `V` and the spin does
not exist — the theme never points a barb at a direction it does not
have.

#### 6.5 v2 — Accessibility spec

The barb is a glyph with a mandatory text twin: the station's report
heading line states "Wind NW 35 kt, gale" in words, and the chart's
accessible description names the gale station and its wind. Feather
count is never the only carrier of speed. The spin is decorative
emphasis over a complete static glyph and is not announced.

#### 6.5 v2 — Tokens consumed

`--ink`, `--dur-barb` (720ms), `--ease-barb` cubic-bezier(0.22, 1,
0.36, 1), `--gale-threshold` (34 kt), `--feather-long` (10 kt),
`--feather-short` (5 kt), `--pennant` (50 kt).

### 6.6 Isobar breathing

- **What & why.** The contoured isobars undulate very slowly — ±2px on
  a 9-second sine, phase offset per line — like weather breathing
  behind the reports. It is the chart's pulse: the smallest motion
  that keeps the sheet a living analysis rather than a scanned page,
  and its restraint is the spec. It belongs here because a synoptic
  chart is a snapshot of a moving fluid; the breathing is the fluid,
  remembered, at the edge of perception.
- **Structure.** Each isobar ships with two path states: its analysed
  `d` and a breathed `d` whose control points are offset ≤2px normal
  to the line (computed at build from the same interpolation as §6.2,
  nudged along the local gradient — the line swells toward lower
  values, as air does). The shared loop interpolates between the two
  states by path-point lerp (equal point counts by construction) with
  weight `(sin(t/9000 × 2π + φ) + 1) / 2`, φ = line index × 0.7 rad.
  Labels ride their lines (the label's anchor point interpolates with
  the same weight).
- **Motion spec.** Continuous while the chart is within one viewport
  of the reading position; 9s period; amplitude 2px at ≥1200px, 1.5px
  below. Pauses when the chart is off-screen (IntersectionObserver),
  when the tab is hidden, and while any isobar is still contouring
  (§6.2 owns the lines until the analysis completes, then breathing
  fades in over 1s). Never applies to fronts, station glyphs, or text
  other than the isobars' own labels — the plotted facts do not
  breathe; only the analysis does.
- **States.** *Resting (analysed):* the base state and the no-JS
  state. *Breathing:* in view, motion allowed. *Paused:* off-screen,
  hidden tab, or hovered chart region under §6.8 expansion (the
  visitor is reading a station; the field holds still for them).
  *Reduced motion:* never runs.
- **Content merge.** The breathing moves the analysis lines around the
  stations they contour; it touches no value, no front, no word of the
  reports. Remove it and the chart is a finished chart.
- **Failure fallback.** If path interpolation throws for a line (point
  count mismatch after a data revision), that line is pinned to its
  analysed path and excluded from breathing; the rest continue. If the
  loop stalls, all lines rest at their analysed paths — the watchdog's
  static chart (§5) *is* the fallback state.
- **Reduced-motion variant.** None. The analysed chart, still. This
  element has the strictest reduced-motion ruling in the theme because
  it is the only purely ambient one.
- **Performance budget & mobile variant.** Path interpolation is the
  theme's most expensive ambient cost: capped at 14 lines, points per
  line ≤ 120, writes only while in view; measured budget ≤ 1.5ms/frame
  for all lines together. The §14 cut order removes breathing first.
  Mobile: amplitude 1.5px, and only the 6 innermost lines of each
  system breathe — outer rings hold still on phones.

#### 6.6 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| Analysis complete (§6.2) | Breathing weight fades 0 → 1 over 1s |
| Continuous | Each line's weight follows its phase-offset 9s sine |
| Chart exits viewport | Weights freeze at current values; loop stops writing paths |
| Chart re-enters | Breathing resumes from the frozen phase — no jump, no restart |
| Station expanded (§6.8) | Breathing pauses for the expansion's duration |

#### 6.6 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Analysed paths | Analysed paths |
| Breathing | ±2px, 9s sine, phase-offset | ±1.5px, innermost 6 lines per system |
| Hover (chart) | Continues, except during a station expansion | n/a |
| Focus | Continues; pauses while a station holds focus-expanded state | Same |
| Scrolled-past | Paused off-screen | Paused |
| Disabled / no-JS | Analysed paths | Same |
| Reduced motion | Never runs | Never runs |

#### 6.6 v2 — Breakpoint behaviour

≥1200px: all ≤14 lines, ±2px. 768–1199px: all lines, ±1.75px.
<768px: innermost 6 lines per system, ±1.5px; the unpinned chart
breathes only while it is actually on screen.

#### 6.6 v2 — Edge cases & failure modes

*Photosensitivity:* ±2px at 0.11 Hz is far below any flash or vestibular
threshold; the spec's slowness is a safety property, and "enlivening"
it is a gate failure. *A line whose breathed state would cross its
neighbour:* amplitudes are validated at build — if the breathed path
comes within 3px of an adjacent isobar, that line's amplitude is
halved until it clears; breathing may never make isobars touch, let
alone cross (§6.2's law). *Low-power device:* if the loop measures
sustained <40fps, breathing is cut entirely (it is first in §14's cut
order) and the chart rests analysed. *Print:* paths print at their
analysed state.

#### 6.6 v2 — Accessibility spec

Purely decorative ambience over a complete static chart; the SVG
carries `aria-hidden` on the breathed duplicates (the analysed paths
are the accessible ones) and no information rides on the motion. It is
fully disabled under `prefers-reduced-motion` and pauses for focused
content so it never competes with reading.

#### 6.6 v2 — Tokens consumed

`--isobar-grey`, `--dur-breathe` (9000ms), `--amp-breathe` (2px),
`--phase-step` (0.7 rad), `--loop-lerp` (0.14).

---

### 6.7 Observation clock

- **What & why.** The page's progress indicator is the chart room's
  clock: an analogue dial in the masthead whose hand advances through
  the synoptic hours — 00, 06, 12, 18 UTC — as the visitor passes the
  page's watches, snapping to each hour with a small overshoot. It
  belongs here because progress in this theme is chart-time: the
  visitor reads the page the way forecasters read the day, issue by
  issue, and the clock says which issue they are in. There is no
  scroll bar, no percentage, no "3 min read" anywhere in the theme —
  the clock is the whole of progress.
- **Structure.** A 54px SVG dial in the masthead: four stops only (00
  at top, 06 right, 12 bottom, 18 left — the dial is a compass of the
  day), a single hand, and the current hour printed beside it in IBM
  Plex Mono ("12 UTC"). The page's sections are grouped into four
  watches in the build's declaration (§1); each watch maps to one
  synoptic hour in order. The digital readout is the primary text; the
  hand is its glyph.
- **Motion spec.** Trigger: the reading position crossing a watch
  boundary (the watch's first section crossing 50% vh). The hand
  rotates to the new hour over 300ms `--ease-snap-hour`, overshooting
  by 4° and settling — a clock hand with weight. The readout swaps at
  the rotation's midpoint. Between watches the hand rests exactly on
  the hour; it never creeps with scroll (a synoptic clock ticks at
  issues, not continuously). On a page with a single watch, the hand
  is set at issue and never moves.
- **States.** *Rest:* hand on the current watch's hour, readout
  matching. *Advancing:* 300ms snap. *Scrolled-past / back:* the hand
  follows the watch in view in both directions — time on this clock is
  the visitor's position, and scrolling back returns to the earlier
  issue. *No-JS:* the clock prints the page's *first* watch hour with
  the readout "FROM 00 UTC" — the issue line, static and true.
- **Content merge.** The watches are the page's real sections; the
  clock's hours are their declared synoptic times. The clock tells the
  visitor where in the issued day they are reading — it is the table
  of contents, told in the theme's own units.
- **Failure fallback.** If watch tracking fails, the clock holds the
  first hour and the readout stands as the issue line — a clock
  stopped at issue time is still a true statement about the page. The
  hand is SVG in the DOM at the correct hour by default; JS moves it.
- **Reduced-motion variant.** No snap, no overshoot: the hand and
  readout change instantly at watch boundaries. The information is
  identical.
- **Performance budget & mobile variant.** One rotation per watch
  change; negligible. Mobile: dial shrinks to 40px and moves into the
  masthead's second row beside the issue line; the readout stays 15px
  — the hour is never shrunk below legibility to save the dial.

#### 6.7 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| t₀ | Watch boundary crossed (first section of new watch at 50% vh) |
| t₀ + 0ms | Hand begins rotation toward the new hour |
| t₀ + 150ms | Readout swaps to the new hour at the rotation's midpoint |
| t₀ + 270ms | Hand overshoots the hour by 4° |
| t₀ + 300ms | Hand settles exactly on the hour; watch change complete |

#### 6.7 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Hand on current hour, readout matching | Same |
| Hover | No change | n/a |
| Focus | Clock is not focusable; the readout is plain text in the masthead's reading order | Same |
| Active | n/a | n/a |
| Scrolled-past | Hand follows the watch in view, both directions | Same |
| Disabled / no-JS | First watch's hour, "FROM 00 UTC" | Same |

#### 6.7 v2 — Breakpoint behaviour

≥1200px: 54px dial in the masthead's right block. 768–1199px: 46px
dial, same position. <768px: 40px dial in the second masthead row;
watches and hours unchanged.

#### 6.7 v2 — Edge cases & failure modes

*More sections than watches:* watches are declared groupings, not
per-section hours — a page with 11 reports still has 4 watches, and
the declaration (§1) says which reports belong to which hour. *A page
with two charts (two issues):* each chart's stage carries its own
issue hour in its title block; the masthead clock follows the watches
of the page as a whole, declared in the build. *Midnight boundary
(the 18 → 00 wrap):* the hand rotates forward through the wrap
(90° clockwise), never backwards the long way — the day rolls over.
*Restored scroll position mid-page:* the clock sets instantly to the
restored watch on load, no rotation — the visitor opens the paper at
the page they left.

#### 6.7 v2 — Accessibility spec

The readout is real text ("12 UTC") in the masthead, updated in place;
watch changes are not announced by live region (they are ambient
position, like a scrollbar) but the current watch is always available
as text. The dial itself is `aria-hidden` decoration beside its own
readout. Contrast: hand and stops in `--ink` (12.2:1); readout
`--ink` mono 15px.

#### 6.7 v2 — Tokens consumed

`--ink`, `--ease-snap-hour`, `--dur-clock` (300ms), `--overshoot`
(4°), `--dial-size` (54/46/40px), `--font-obs`.

### 6.8 Station expansion & pin-to-rail

- **What & why.** The chart's two interactions, one gesture family.
  Hovering (or focusing, or tapping) a station circle expands it to
  reveal its full observation string in mono inside the circle's halo
  — detail lives on the chart itself, not in a tooltip detached from
  the data. Clicking a station pins its report to the rail and centres
  the chart on it: the visitor takes the station they found on the
  chart and reads its filing. It belongs here because a chart you
  cannot interrogate is a poster; these two gestures make the chart
  the page's primary instrument, with the rail as its readout.
- **Structure.** Each station circle is a real `<button>` in an HTML
  overlay aligned to the SVG chart (buttons, not SVG hit areas, so
  focus and touch targets are honest). The expansion is a halo disc
  (Ø grows 10px → 120px) centred on the station, filled
  `--chart-cream` at 96% with a 1.5px `--ink` ring, carrying the full
  observation string in 11px IBM Plex Mono, laid out as the plotter
  writes it: name, then the values in words ("LERWICK NW 35KT 1004
  +2 7.1/3.2"). The halo never covers a neighbouring station's values:
  it renders above lines but below other stations' circles, and shifts
  its text block to the emptier side of the station (sea side, by the
  build's per-station `data-halo` side).
- **Motion spec.** Expand: halo scales 1 → 1.8-equivalent (Ø 10 → 120px
  via the disc, circle itself stays 10px — the *halo* grows, the
  station does not swell) over 250ms `--ease-plot`; the string fades
  in at 150ms. Collapse: 180ms `--ease-plot` on leave/blur. Pin: on
  click, the rail scrolls the station's report into view (smooth,
  500ms, or instant under reduced motion), the report's head gains a
  2px `--ink` left rule for 2s, and the chart translates so the
  station sits at the stage's centre (400ms `--ease-advance`, capped
  120 units of pan; the chart's plotted coordinates do not change —
  the *view* moves, as a plotter slides the sheet). A second click
  unpins and returns the view.
- **States.** *Rest:* circle + plotted values. *Hover/focus:* halo
  expanded, string readable. *Active (pinned):* halo ring thickens to
  2.5px and stays while pinned; the report in the rail carries its
  marker rule. *Scrolled-past:* pin persists until another station is
  pinned or the stage is left; expansion collapses. *Disabled:* a
  station with no report (plotted for context) is not a button — it
  expands on hover for sighted pointer users only via CSS, and its
  string is in the table (§6.18) regardless.
- **Content merge.** The expanded string is the station's own
  observation, the pinned report is the station's own filing. The
  chart and the rail are two views of one dataset, and these gestures
  are the join between them.
- **Failure fallback.** Every observation string is fully available
  without the halo: in the station's report and in the table. If the
  overlay alignment fails (chart reflow mid-hover), the halo collapses
  rather than floating detached. No-JS: stations are links to their
  reports' anchors — the join still works, as navigation.
- **Reduced-motion variant.** Halo appears/disappears instantly (no
  scale); pinning jumps the rail without smooth scroll and centres
  without pan. The 2s marker rule becomes a persistent rule while
  pinned.
- **Performance budget & mobile variant.** One halo element reused
  across stations; transforms only. Mobile: no hover — tap expands,
  tap again (or the string's "Read the report" link) pins; halo Ø
  104px, string 10.5px, and the halo always opens toward the chart's
  centre so it never leaves the sheet.

#### 6.8 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| t₀ (hover/focus/tap) | Halo disc begins scaling, 250ms `--ease-plot` |
| t₀ + 150ms | Observation string fades in |
| t₀ + 250ms | Halo at full Ø; string fully readable |
| Leave/blur | String fades 100ms; halo collapses 180ms |
| Click (pin) | Rail scrolls to the report (500ms); chart pans station to centre (400ms); report marker rule draws in |
| +2s | Marker rule fades to a 1px persistent rule while pinned |

#### 6.8 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Circle + plotted values | Same |
| Hover | Halo expanded, string shown | n/a — tap expands |
| Focus | Same as hover, with a visible 2px focus ring on the button | Same (external keyboard) |
| Active (pinned) | Thick ring; report marked in rail; view centred | Same; halo stays until dismissed |
| Scrolled-past | Pin persists; expansion collapsed | Same |
| Disabled | Context stations (no report) are not buttons | Same |

#### 6.8 v2 — Breakpoint behaviour

≥1200px: full spec, halo Ø 120px. 768–1199px: halo Ø 108px, pan cap 90
units. <768px: the unpinned chart's stations are not interactive on
the chart itself (too small to interrogate honestly); expansion and
pinning live on each report's locator inset and full station plot
instead — same gestures, legible size.

#### 6.8 v2 — Edge cases & failure modes

*Stations closer together than a halo:* expanding one station in a
cluster shifts its text block to its declared sea side; if both sides
are occupied, the halo grows to Ø 140px and the string wraps to three
lines rather than covering a neighbour's values — covering data is
the one unforgivable halo sin. *Keyboard traversal through 40
stations:* buttons are in gazetteer order (west to east, north to
south — chart order), and the rail's reports are reachable by the
page's normal flow; a "Stations" skip list in the navigation (§6.10)
jumps by name. *Pinning while the stage is unpinned (mobile):* pin
scrolls to the report only; no pan exists to perform. *The pinned
station's report is filtered out (§6.18 table filters do not touch
reports; if a build adds report filtering, pinning clears the filter
first — a pin must always land).*

#### 6.8 v2 — Accessibility spec

Stations are `<button>`s with names that are the observation's head:
"LERWICK — wind NW 35 knots, pressure 1004, rising". Focus ring: 2px
`--ink` outline offset 2px, visible against cream and against the
halo. Touch targets: the button's hit area is 40×40px minimum around
the 10px circle (the circle is the glyph, the button is the target).
The halo string is exposed to AT as the button's description. Pinning
moves no focus (the visitor stays on the chart); the rail scroll is
visual, and the report is reachable by the next Tab presses in DOM
order.

#### 6.8 v2 — Tokens consumed

`--ink`, `--chart-cream`, `--ease-plot`, `--ease-advance`,
`--dur-expand` (250ms), `--dur-collapse` (180ms), `--halo-d`
(120/108/104px), `--pan-cap` (120 units).

---

### 6.9 Time-step transition

- **What & why.** Navigation in this theme is a forecast time-step:
  when the visitor follows a link to another chart page, the outgoing
  chart crossfades to the incoming one *at the next observation time*,
  its fronts visibly advanced one step (their symbols shifted +35
  units along their lines) and its clock showing the next synoptic
  hour. To change pages is to move the weather on — the same operation
  the chart itself performs. It belongs here because a weather site is
  a sequence of issues; a transition that ignored the issue rhythm
  would be a foreign object between two charts.
- **Structure.** A fixed full-viewport overlay holding a clone of the
  chart frame (sheet border, title block) — not the destination's full
  chart, which the visitor has not loaded yet. The overlay's front
  symbols are generic-issue glyphs in the theme's colours; the
  destination page, on arrival, plots its own real chart beneath the
  overlay's fade. Links the transition may enhance are same-site chart
  pages only; it decorates `<a>` clicks and never replaces href
  behaviour (modified clicks, new tab, and external links bypass it
  entirely).
- **Motion spec.** Total 650ms: overlay fades in 200ms over the
  outgoing page; at full cover the navigation commits; the incoming
  page's chart reveals through §5's station-circle mask while the
  overlay fades out over 250ms; the incoming fronts' symbols start at
  their issue positions but the *overlay's* symbols sit one step
  advanced (+35 units), so the eye reads continuity: the weather moved
  while the page turned. The incoming clock is already at its hour —
  clocks do not spin during transitions.
- **States.** *Idle:* no overlay. *Covering:* 200ms. *Covered:*
  navigation commits; if the destination is slow, the overlay holds
  with its issue line updating to "AWAITING THE 18 UTC CHART" — up to
  3s, after which the overlay retreats (200ms) and the browser's
  native load proceeds; the theme never traps a visitor inside a
  transition. *Revealing:* 250ms fade + mask. *Back/forward:* no
  transition — the browser's history gesture rules.
- **Content merge.** The overlay is a sheet of the same chart paper
  with the same furniture; the step it performs (+35 units, next hour)
  is the chart's own grammar. It carries the issue line of the
  destination, which is real information about where the visitor is
  going.
- **Failure fallback.** Without JS: ordinary navigation. If the
  destination errors, the overlay retreats and the browser shows its
  error or the site's §6.15 page. Prefetched destinations still run
  the full 650ms — the ritual is the point, not the wait.
- **Reduced-motion variant.** No overlay, no mask: instant navigation,
  with the destination's issue line present as usual. The step is
  conveyed by the charts themselves (each page's hour differs), not by
  a performance between them.
- **Performance budget & mobile variant.** One overlay, transforms and
  opacity only. Mobile: total 500ms (150ms cover, 200ms reveal); the
  symbol advance reads at the smaller sheet because the glyphs are
  drawn at mobile size (§6.1's variant).

#### 6.9 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| t₀ (link activation) | Overlay begins fading in; outgoing page goes `inert` |
| t₀ + 200ms | Full cover; navigation commits underneath |
| Destination ready | Incoming chart's mask reveal begins; overlay fades 250ms |
| t₀ + ~650ms | Overlay gone; focus moves to the destination's chart title (see a11y) |
| t₀ + 3s (slow destination) | Overlay retreats; native load proceeds |
| t₀ + 430ms after retreat | Watchdog tears down any stuck overlay |

#### 6.9 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Idle | No overlay | Same |
| Covering | 200ms fade | 150ms fade |
| Covered | Holds with live issue line, ≤3s | Same |
| Revealing | 250ms fade + chart mask | 200ms fade + mask |
| Hover | Links show §6.10's nav hover; the transition has no hover state | n/a |
| Focus | Keyboard-activated links fire the same transition | Same |
| Disabled / no-JS | Plain navigation | Same |

#### 6.9 v2 — Breakpoint behaviour

≥1200px: full spec. 768–1199px: 600ms total. <768px: 500ms total,
overlay furniture reduces to sheet border + issue line (no title block
— the phone sheet is a half-sheet).

#### 6.9 v2 — Edge cases & failure modes

*Same-page anchors:* no transition — anchors scroll within the issue.
*Links to non-chart pages (a PDF, a data download):* no transition;
the step belongs between charts. *A destination that is the same hour
(a detail page of the current issue):* the overlay's symbols do not
advance — the step is zero and the transition says so honestly ("SAME
ISSUE — STATION DETAIL"). *Double-clicking a link:* the second click
is ignored while covering; navigation commits once. *The visitor's
back button during cover:* the overlay tears down instantly and
history proceeds.

#### 6.9 v2 — Accessibility spec

During cover, the outgoing page is `inert`; on reveal, focus moves to
the destination's `<h1>` (tabindex −1) and a polite announcement
"Chart for 18 UTC" is made — SPA navigation focus law, executed in
the theme's grammar. The transition is skipped entirely under reduced
motion and when the router manages focus itself. The overlay is
`aria-hidden` while covering (its issue line duplicates the
announcement).

#### 6.9 v2 — Tokens consumed

`--chart-cream`, `--front-red`, `--front-blue`, `--ease-contour`,
`--dur-step` (650ms), `--step-advance` (35 units), `--hold-max` (3s).

### 6.10 Chart-room masthead & station index (page family: navigation)

- **What & why.** Navigation is the chart room's own furniture: a
  masthead ruled like the chart's title block — issuing office, region,
  the observation clock (§6.7), and the issue line — with the site's
  sections listed as a *station index*: name, and the synoptic hour at
  which that section files. It belongs here because a chart is not
  navigated by a hamburger; it is consulted by its index, and the
  index of a chart is its list of stations and hours.
- **Structure.** `<header>` with three blocks: office block (site name
  set as a chart title, 20px Franklin 800, with the issuing-office
  line beneath in apparatus type), the clock (§6.7) at right, and
  beneath, a `<nav class="station-index">`: a horizontal rule-bound
  list of section links, each carrying its watch hour in mono
  ("REPORTS · 06", "TABLE · 12"). The current section's item is
  printed in `--front-blue` with its hour underlined by a 2px rule —
  currentness by ink, never by a pill. On mobile the index collapses
  behind a "STATION INDEX" toggle that opens with a hard downward wipe
  (300ms, §5's panel grammar), never a fade.
- **Motion spec.** Hover/focus on an index item: the hour's rule draws
  in from the name toward the hour (background-position sweep, 180ms
  `--ease-plot`) and the item inks from `--ink-soft` to `--ink`.
  Current-watch tracking: as §6.7's clock advances, the index item of
  the watch in view gains its blue over 200ms — the index and the
  clock are two hands of the same instrument. The mobile panel wipes
  300ms. Nothing else in the masthead moves; a masthead is furniture.
- **States.** *Rest:* ink items, hours in mono. *Hover/focus:* rule
  draws, item inks. *Current:* blue item, full rule. *Pinned state:*
  the masthead is *not* sticky — the chart pins (§4), the masthead
  scrolls away with the situation, because the office does not follow
  the reader down the page; a slim issue strip (region + hour + clock
  readout, 36px) takes its place at the viewport top once the stage is
  entered, and leaves with it.
- **Content merge.** The index items are the page's real sections with
  their real filing hours, generated from the page's own headings —
  add a watch and the index gains a line, because it *is* the page's
  contents, printed as a chart index.
- **Failure fallback.** Plain anchor list in a ruled header; the wipe
  and the watch tracking are the only JS behaviours, and their absence
  leaves a complete, legible masthead with the first item marked
  current by the server where known.
- **Reduced-motion variant.** No rule draw (rule appears full), no
  wipe (panel opens instantly), watch colour changes instant.
- **Performance budget & mobile variant.** Watch tracking rides §6.7's
  observer — free. Mobile: office block and clock stack; the index
  toggle is a full-width 44px apparatus button; the issue strip is
  32px and carries the readout only.

#### 6.10 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| t₀ (hover an index item) | Rule sweep begins at the section name |
| t₀ + 180ms | Rule reaches the hour; item fully inked |
| Pointer leave | Rule relaxes over 240ms; item returns to `--ink-soft` |
| Watch change (§6.7) | Outgoing item's blue drains 200ms as the incoming item inks blue — one beat of overlap, like passes on the press |
| Stage entered | Issue strip slides in with the pin (one motion, §4) |

#### 6.10 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Ink-soft items, mono hours | Behind the STATION INDEX toggle |
| Hover | Rule draws, item inks | n/a |
| Focus | Same as hover | Same |
| Active / current | Blue item, full rule | Marked in the index panel |
| Scrolled-past | Masthead gone; issue strip serves while the stage lasts | Same |
| Disabled | A section with no content is absent from the index — never a greyed item | Same |

#### 6.10 v2 — Breakpoint behaviour

≥1200px: three-block masthead, index in one rule-bound row (wraps to
two rows rather than shrinking type). 768–1199px: index wraps; clock
46px. <768px: stacked masthead, toggle + wipe panel, index items at
44px row height with hours right-aligned in mono.

#### 6.10 v2 — Edge cases & failure modes

*More sections than the row holds (>6):* the index lists watches, not
sections — four to six entries by construction (§6.7); a build with
more watches than hours re-declares its mapping (§1) rather than
crowding the row. *Very long section names:* truncate at 24ch on the
row with the full name in the mobile panel and the link's accessible
name. *Single-watch page:* the index is omitted — a one-issue page has
no contents to index; the issue strip still serves. *The issue strip
and a pinned station halo (§6.8) competing for the top:* the strip is
36px and the halo renders below it; the chart's pan cap (§6.8) already
accounts for the strip's height.

#### 6.10 v2 — Accessibility spec

A real `<nav aria-label="Station index">`; the current item carries
`aria-current="true"`, updated on watch changes only. The mobile
toggle is a `<button aria-expanded>`; Esc closes the panel and returns
focus to the toggle. Focus order = reading order. Index rows ≥24px
desktop, ≥44px mobile. The issue strip's readout duplicates §6.7's
text and is `aria-hidden` to avoid a second clock announcement.

#### 6.10 v2 — Tokens consumed

`--ink`, `--ink-soft`, `--front-blue`, `--cream-edge`, `--ease-plot`,
`--dur-rule-draw` (180ms), `--dur-wipe` (300ms), `--strip-h` (36px).

---

### 6.11 General situation hero (page family: hero)

- **What & why.** Every issued chart carries the forecaster's summary
  paragraph — the "general situation" — before the map: three to five
  sentences stating what the systems are doing. The theme's hero is
  that paragraph, set large above the chart, with the chart's title
  block as its furniture. It belongs here because the hero's job in
  this world is not to sell but to *situate*: by the time the visitor
  reaches the chart, they already know there is a deepening low west
  of the region and a front arriving by evening — in the site's data,
  whatever its declared mapping says those are.
- **Structure.** A section above the stage: the title block line
  (region — hour — issuing office, apparatus type between two rules),
  the H1 (the region and hour, §3), the situation paragraph (18px
  Franklin, max measure 62ch), and the issue's vital line in mono: the
  principal system's centre value, the gale station and its wind, the
  next issue time. The paragraph's system names are links into the
  chart (they pin the relevant station/system per §6.8's grammar when
  the stage is reached — in the hero they are plain anchors to the
  stage).
- **Motion spec.** Entrance, once, on load: title block rules draw
  600ms `--ease-contour`; the paragraph arrives as a whole (no
  per-line performance — filed copy is filed whole) with a 200ms fade;
  the vital line's figures roll (§6.4's component, from the previous
  issue's real figures) at +400ms. The hero never parallaxes and never
  pins; it is read and left. If the situation names a front, that
  front's line on the chart below draws 200ms early in §6.2's order —
  the paragraph and the chart are one issue.
- **States.** *Rest:* printed situation. *Scrolled-past:* gone; the
  issue strip (§6.10) carries region + hour onward. *Hover:* only the
  system-name links respond (underline rule draw, §6.10's grammar).
  *No-JS:* everything printed, vital figures at current values.
- **Content merge.** The paragraph *is* the issue's summary, written
  from the same data the chart plots; its figures are the chart's
  figures. A hero written before the data exists is marketing copy in
  a chart's clothing and fails §9.
- **Failure fallback.** Static printed hero. The vital line degrades
  to the issue line (region, hour, office) if any figure is missing —
  never a row of `///` in the hero; missing observations belong in
  reports, where the convention lives (§6.4).
- **Reduced-motion variant.** No draws, no roll: the hero stands
  printed. Identical words, identical figures.
- **Performance budget & mobile variant.** Text and two rule draws;
  negligible. Mobile: H1 32px, paragraph 17px, vital line wraps to two
  mono rows; the title block keeps all three facts (region, hour,
  office) — furniture is never dropped for size, only reflowed.

#### 6.11 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| 0ms | Hero printed in DOM |
| +100ms | Title block rules draw, 600ms |
| +300ms | Paragraph fade completes (200ms) |
| +400ms | Vital line figures roll from the previous issue's values, 600ms |
| +1000ms | Hero fully issued; the chart below begins its reveal (§5) |

#### 6.11 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Printed situation | Same |
| Hover | System-name links draw their rules | n/a |
| Focus | Same as hover | Same |
| Active | n/a | n/a |
| Scrolled-past | Gone; issue strip serves | Same |
| Disabled / no-JS | Printed, current figures | Same |

#### 6.11 v2 — Breakpoint behaviour

≥1200px: full spec, paragraph at 62ch beside the title block's right
rail of vital figures. 768–1199px: vital line moves beneath the
paragraph. <768px: stacked; vital line two rows; rules full width.

#### 6.11 v2 — Edge cases & failure modes

*A situation with no systems (a quiet issue — a ridge, in the site's
terms a flat period):* the paragraph says so in the forecaster's
words ("A quiet issue: no fronts on the chart") and the vital line
carries the ridge's centre value — quiet is a real synoptic state,
not an empty hero. *A situation longer than five sentences:* it is
edited, not shrunk — the gate (§10) caps the situation at 90 words;
detail belongs in reports. *Previous issue's figures unavailable
(first issue of a series):* the vital line prints current figures
with no roll and the line is labelled "FIRST ISSUE".

#### 6.11 v2 — Accessibility spec

The H1 is the page's heading; the situation is a paragraph in normal
flow; the vital line is a list of labelled facts ("Centre: 984 hPa ·
Gale: LERWICK NW 35 kt · Next issue: 18 UTC"), each label real text,
not a title attribute. Link names name their systems ("the low west
of the region — go to chart"), never "click here".

#### 6.11 v2 — Tokens consumed

`--ink`, `--ink-soft`, `--cream-edge`, `--ease-contour`, `--dur-rule`
(600ms), `--font-obs`.

### 6.12 The unplotted sheet (page family: loader / skeleton)

- **What & why.** Loading in this theme is a chart awaiting its
  observations: the sheet, graticule, and coastline stand printed,
  station circles hollow, their value slots empty, the issue line
  reading "AWAITING OBSERVATIONS". As each station's data lands, the
  station plots — circle inks, values print, barb draws. It belongs
  here because a chart room has a real state between the blank sheet
  and the issued chart, and this is it; a spinner would be a foreign
  object on the sheet.
- **Structure.** The real chart markup in `.is-awaiting` state: sheet
  and graticule at full presence, coastline drawn, station circles as
  1px hollow rings with their slots empty (no grey blocks — the
  skeleton is the sheet's own furniture, unfilled), fronts absent
  (fronts are analysis; analysis waits for data), the rail's report
  skeletons as ruled lines at report height. Per-station resolution:
  the station's group loses `.is-awaiting` and plots in 240ms
  (`--ease-plot` fades + §6.4's print, no roll — a first plot is not a
  replay).
- **Motion spec.** Stations plot in arrival order as data resolves,
  each 240ms. Hard cap from the standing law: **any station still
  awaiting at 1200ms has its skeleton stripped** — the circle fills
  plain, the slots print the missing mark `///`, and the report
  carries the line "Observation not received" (§12's voice); the
  station receives its real plot plainly whenever data does arrive,
  without ceremony. The full-chart watchdog (§5) is this element's
  global form.
- **States.** *Awaiting:* hollow stations, issue line marked.
  *Plotting:* per station, 240ms. *Issued:* complete chart, issue
  line normal. *Failed station:* `///` slots + the report's line —
  a terminal, honest state, not an eternal shimmer.
- **Content merge.** The skeleton *is* the chart, unfilled: same
  sheet, same stations, same geometry — layout shift is zero by
  construction, and the visitor watches the actual issue assemble from
  actual arrivals.
- **Failure fallback.** Server-rendered pages ship issued (the
  skeleton exists only inside client-side fetches that own their
  watchdog). Without JS no `.is-awaiting` state is ever rendered
  unresolved. A fetch error resolves the station to the failed state
  above, never to a permanent skeleton.
- **Reduced-motion variant.** Awaiting stations are plain hollow
  circles with the issue line marked; plotting is instant. The 1200ms
  cap and the `///` convention are unchanged.
- **Performance budget & mobile variant.** Skeleton is pure CSS/SVG
  state on real markup — no payload. Mobile: identical, at the mobile
  chart's reduced station plot (§6.4's rule).

#### 6.12 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| t₀ (fetch begins) | Sheet stands awaiting; issue line marked |
| Each station's data lands | Circle inks, values print, barb draws — 240ms |
| t₀ + 1200ms | Any station still awaiting is stripped to the failed state (`///`) |
| All stations resolved | Issue line clears its mark; §6.2 contouring begins on the real field |

#### 6.12 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Awaiting | Hollow circles, empty slots | Same |
| Plotting | 240ms per station | Same |
| Issued | Complete chart | Same |
| Failed | `///` slots, report line printed | Same |
| Hover / focus | No skeleton states respond | Same |
| Disabled / no-JS | Issued chart only — skeleton never rendered | Same |

#### 6.12 v2 — Breakpoint behaviour

≥1200px: full station plots in the skeleton. 768–1199px: same.
<768px: skeleton stations show circle + primary slot only, matching
§6.4's mobile plot.

#### 6.12 v2 — Edge cases & failure modes

*Partial data (a station's wind missing, values present):* the station
plots what arrived; the wind slot carries `///` — partial observations
are a real chart-room event with a real convention. *Data arriving
after the 1200ms strip:* plotted plainly in place, and the report's
"not received" line is replaced by the report with a correction mark
(§6.4's struck-figure convention applies to the line). *All stations
failing:* the chart issues as an empty sheet with the colophon's
apology in the office's voice (§12) — a failed issue, honestly
labelled, never a spinning page. *Slow rail data with fast chart
data:* the chart issues when its stations resolve; reports skeleton
independently with the same 1200ms law.

#### 6.12 v2 — Accessibility spec

The awaiting chart carries `aria-busy="true"` and the issue line's
mark is real text ("Awaiting observations"); resolution announces
once, politely: "Chart issued for 12 UTC". Failed stations are
announced in their reports' text, not by live region per station.
Skeleton lines in the rail are `aria-hidden`; the reports' headings
are present from the start so the page's outline never changes shape.

#### 6.12 v2 — Tokens consumed

`--ink`, `--isobar-grey`, `--cream-edge`, `--ease-plot`,
`--dur-plot-in` (240ms), `--fallback-strip` (1200ms), `--mark-missing`
(`///`).

---

### 6.13 File an observation (page family: forms / conversion)

- **What & why.** The theme's conversion form is the chart room's
  observation slip: the visitor files a report from their own station
  — a signup, a contact, a data submission, whatever the build's
  conversion is — on a slip ruled like a station entry, and the office
  accepts it with a plotted acknowledgement. It belongs here because
  conversion in this world is not a funnel; it is a citizen observer
  joining the network, and the network's paperwork is an observation
  form: station, values, remarks. The form's honesty (few fields, no
  dark patterns, errors in the office's plain voice) is the theme's
  answer to growth-hacking.
- **Structure.** A `<form class="obs-slip">` on `--cream-deep` inside a
  sheet-bordered panel: a slip header (form title as a chart label,
  the visitor's provisional station code assigned by the build —
  e.g. "NEW STATION — UNPLOTTED"), fields as station entries: label in
  apparatus type above, input as a bottom-ruled line (transparent
  ground, 2px `--ink` bottom rule, IBM Plex Mono 15px input text —
  the visitor writes in the plotter's hand), and the submit as a
  `.plot-button`: ink-bordered, uppercase Franklin, "FILE THE
  OBSERVATION". Success replaces the slip with its acknowledgement: a
  plotted station entry — the visitor's station now printed on a
  miniature chart inset with its circle inked — and a filed line
  ("Filed 12 UTC · Station No. 41") whose number is the real record
  count from the server.
- **Motion spec.** Entry: the slip panel's border draws 500ms
  `--ease-contour` when it arrives; the provisional station code types
  in mono at 24ms/char (a telegraph rhythm) once. Field focus: the
  bottom rule thickens 2px → 3px and a `--front-blue` rule slides in
  beneath it from the left (200ms `--ease-plot`) — the line being
  written on is underlined by the office. Error: the field's rule
  turns `--red-deep`, the error line letters in beneath at 45ms/word
  in §12's error voice. Submit: the button presses (scale 0.97, 120ms
  `--ease-snap-hour` without overshoot); on success the acknowledgement
  station plots per §6.12's 240ms plot-in and the filed line's number
  rolls (§6.4) from the previous count.
- **States.** *Rest:* ruled empty fields. *Focus:* thickened rule +
  blue underline. *Error:* red-deep rule + error line; the visitor's
  entered values are never cleared by an error, including a server
  500 — the slip keeps the copy. *Submitting:* button pressed state,
  fields inert, a mono "FILING…" in the slip header (never a spinner).
  *Filed:* acknowledgement state, terminal; the form does not reset
  itself or offer to file another without the visitor asking.
- **Content merge.** The fields are the build's real conversion data,
  labelled in the mapping's terms where the mapping honestly allows
  (a coastal-town field is a station; an email is the observer's
  call-sign) — and plainly labelled where it does not. The theme never
  renames a password field into poetry. The acknowledgement's station
  number and filed hour are the server's real values.
- **Failure fallback.** A plain HTML form that submits without JS;
  errors return as a re-rendered slip with the error lines printed
  (not lettered) and values preserved. The telegraph typing of the
  station code is enhancement only — the code is in the DOM.
- **Reduced-motion variant.** No border draw, no typing (code printed),
  no lettering of errors (printed), button press without scale. The
  acknowledgement plots instantly.
- **Performance budget & mobile variant.** Negligible motion cost.
  Mobile: fields full width, input text 16px (no iOS zoom), the
  acknowledgement inset shrinks to the station's locality at 160px
  wide.

#### 6.13 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| Slip enters | Border draws 500ms; header prints |
| +500ms | Provisional station code types, 24ms/char, once |
| Field focus | Rule thickens; blue underline slides 200ms |
| Error returned | Rule turns red-deep; error line letters 45ms/word |
| Submit | Button presses 120ms; header shows "FILING…" |
| Success | Acknowledgement station plots 240ms; filed number rolls 600ms |

#### 6.13 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Ruled fields, printed header | Same |
| Hover | Button border thickens 2px → 3px | n/a |
| Focus | Rule 3px + blue underline; visible focus ring on the button | Same |
| Active | Button scale 0.97 | Same |
| Submitting | Fields inert, "FILING…" | Same |
| Filed | Acknowledgement, terminal | Same |
| Disabled | A disabled field prints its reason beneath in apparatus type — never a bare grey box | Same |

#### 6.13 v2 — Breakpoint behaviour

≥1200px: slip at 520px in a sheet panel beside the key (§6.16) — the
office's two documents side by side. 768–1199px: slip full width below
the chart. <768px: slip full width; header code on its own row; submit
button full width, 48px tall.

#### 6.13 v2 — Edge cases & failure modes

*Validation that depends on the server (a station code already
taken):* the error line names the field and the fact ("That call-sign
is already plotted — try the next") in §12's voice; the value stays
for editing. *Optional fields:* marked "(may be left blank)" in
apparatus type — the chart room's words, not an asterisk with a
footnote hunt. *A conversion needing payment:* payment fields leave
the theme's grammar entirely (a bordered, plainly-labelled secure
block inside the slip panel, announced as such) — the theme does not
dress card fields as observations; honesty outranks atmosphere at the
money step. *Double submission:* the button disables at first press
and the filed number is idempotent — filing twice plots one station.

#### 6.13 v2 — Accessibility spec

Real `<label>`s, `aria-describedby` for error lines, errors announced
via a polite live region summarising count and first field ("Two
entries need attention — the first is your call-sign"). Focus moves
to the first errored field on return. Input text `--ink` 15–16px on
`--cream-deep` (≥11:1). Touch targets: fields 48px tall, button 48px.
The acknowledgement is a heading + text, reachable and readable, not
an image of a chart.

#### 6.13 v2 — Tokens consumed

`--ink`, `--front-blue`, `--red-deep`, `--cream-deep`, `--ease-contour`,
`--ease-plot`, `--dur-slip-draw` (500ms), `--dur-type-code` (24ms/char),
`--font-obs`.

### 6.14 Chart colophon footer (page family: footer)

- **What & why.** The footer is the chart's colophon: the block every
  issued chart carries at its foot — issuing office, issue hour, next
  issue, the data sources, and this theme's signature line, the
  pedant's note carried from the original entry: an open invitation to
  check the symbols. It belongs here because a chart's authority is
  its provenance, and the footer is where provenance is printed. It is
  also where the theme proves its honesty when nobody is performing:
  the mapping declaration (§6.16) is repeated here in short form.
- **Structure.** A ruled block across the sheet's foot: three columns
  of apparatus text — *Issued* (office, hour of this issue, next issue
  hour, all real values from the build), *Sources* (the data feeds the
  chart plots, named), *The chart* (short mapping, the pedant's note,
  a link to the full key). Beneath, a final rule and the sign-off line
  in the office's voice: "End of the 12 UTC issue." No social icons
  row, no newsletter box (that is §6.13's job, in its place), no
  back-to-top rocket — a "Return to the masthead" text link, ruled
  like an index entry.
- **Motion spec.** Nearly none, by law: the footer is where motion
  stops. The final rule draws 400ms `--ease-contour` when the footer
  first enters — the plotter ruling off the sheet — and the next-issue
  hour's figure is live text (it rolls §6.4-style only if the issue
  actually changes while the page is open, at the synoptic boundary).
  Everything else is print.
- **States.** *Rest:* printed colophon. *Scrolled-to (end of page):*
  the §6.7 clock shows the final watch; the footer is its caption.
  *Hover:* links underline per §6.10's grammar. *No-JS:* identical —
  the footer has no JS behaviour except the live next-issue figure,
  which degrades to the printed schedule.
- **Content merge.** Every line is the issue's real provenance. The
  pedant's note is not a joke pasted on: it links to the key where the
  checking can actually be done.
- **Failure fallback.** Static text. If the next-issue value cannot be
  computed, the line prints the standing schedule ("Issued at 00, 06,
  12, 18 UTC") instead of a wrong hour.
- **Reduced-motion variant.** The final rule is printed, not drawn.
  Nothing else changes.
- **Performance budget & mobile variant.** One rule draw. Mobile:
  columns stack in issue order (Issued, Sources, The chart); the
  sign-off keeps its own line at every width.

#### 6.14 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| Footer enters | Final rule draws, 400ms — the sheet is ruled off |
| Synoptic boundary crossed while open | Next-issue figure rolls to the new hour (600ms, §6.4) — the only live event the footer permits |
| Otherwise | Print. The footer does not perform |

#### 6.14 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Printed colophon | Stacked colophon |
| Hover | Link rules draw | n/a |
| Focus | Same as hover | Same |
| Active | n/a | n/a |
| Scrolled-past | n/a — it is the end | Same |
| Disabled / no-JS | Printed colophon, standing schedule | Same |

#### 6.14 v2 — Breakpoint behaviour

≥1200px: three columns. 768–1199px: two columns (Issued + Sources,
then The chart full width). <768px: stacked, apparatus at 12.5px —
small print may be small, never below 12px.

#### 6.14 v2 — Edge cases & failure modes

*A build with no real next issue (a one-off chart):* the line prints
"Single issue" — the colophon never invents a schedule. *Sources that
update at different hours:* each source line carries its own hour;
the colophon does not average them into a false single issue time.
*The pedant's note drawing a correction:* corrections are filed as a
printed erratum line added to the colophon with its date ("Erratum,
14 May: the Fair Isle barb in the 06 UTC issue plotted 30 kt for
35 kt") — the theme's errors are corrected in the open, in the
footer, forever. This is a feature of the world, not an embarrassment.

#### 6.14 v2 — Accessibility spec

A real `<footer>` with three `<section>`s, each headed by its
apparatus label as a heading. Links are text links with full names.
Contrast: apparatus `--ink-soft` 7.6:1 minimum at 12px. The sign-off
line is a paragraph, in flow.

#### 6.14 v2 — Tokens consumed

`--ink-soft`, `--cream-edge`, `--ease-contour`, `--dur-rule-off`
(400ms), `--font-obs`.

---

### 6.15 The missing chart (page family: 404 / empty states)

- **What & why.** The 404 and the empty state are the same event in a
  chart room: the chart for that hour was not issued. The page shows
  the sheet — graticule, coastline, furniture — with no analysis on
  it, and the office's line: "No chart was issued for this position."
  It belongs here because the theme's honesty law extends to absence:
  a missing page is reported like a missing observation, in the open,
  with the route back to the issued charts. It never draws a fake
  chart to fill the sheet.
- **Structure.** The unplotted sheet (§6.12's awaiting state, but
  terminal): stations absent entirely (not hollow — there is no
  station here), the title block reading the requested position as
  coordinates-style text (the path rendered as the office received
  it), the situation line (§12's empty voice), and the way back: the
  station index (§6.10) and the latest issued chart as a printed card
  (§6.18's row grammar). Search, if the site has it, is offered as
  "Ask the office" — a plain input, §6.13's field grammar.
- **Motion spec.** The sheet stands still — an unissued chart does not
  perform. The single permitted motion: the graticule's grain drift
  (§5) continues, because the paper is real even when the chart is
  not. Entry of the way-back card follows §6.18's row reveal.
- **States.** *Rest:* the empty sheet and the office's line.
  *Hover/focus:* only the way-back links respond. *No-JS:* identical.
  There is no loading state for an absence.
- **Content merge.** The empty sheet is the site's real geography with
  nothing plotted — the visitor sees the shape of the service and the
  exact place where their page is not. The way-back card is the real
  latest issue.
- **Failure fallback.** This element *is* a failure state; its own
  fallback is that it must render with no data at all — if even the
  latest-issue card cannot load, the station index alone carries the
  way back, as text links.
- **Reduced-motion variant.** The grain drift stops. Nothing else
  exists to stop.
- **Performance budget & mobile variant.** Negligible. Mobile: the
  sheet crops to the requested position's locality rather than
  shrinking the whole region to illegibility.

#### 6.15 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| Load | Sheet stands, unissued, still |
| Continuous | Grain drift only (§5), the paper breathing for an absent chart |
| Way-back card enters | Row reveal per §6.18 |

#### 6.15 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Empty sheet, office line, way back | Same, cropped sheet |
| Hover | Way-back links only | n/a |
| Focus | Same as hover | Same |
| Active | n/a | n/a |
| Scrolled-past | n/a | n/a |
| Disabled / no-JS | Identical | Same |

#### 6.15 v2 — Breakpoint behaviour

≥1200px: full sheet. 768–1199px: full sheet, way-back card beneath.
<768px: sheet cropped to locality at legible scale; the office line
above the sheet, not on it (small screens do not set text over paper
texture).

#### 6.15 v2 — Edge cases & failure modes

*A position that exists but has no chart this hour (a real section,
an unissued time):* the page says exactly that — "This station files
at 18 UTC; the current issue is 12 UTC" — and shows the station's last
report as the way-back card. Absence has kinds, and the office names
the right one. *A malformed position:* the title block prints it as
received, struck through once (the plotter's correction convention),
with the nearest valid reading beside it. *Empty search results:*
the same sheet, the office line "No station answers to that name",
and the index — never a dead end with a mascot.

#### 6.15 v2 — Accessibility spec

The page's H1 is the office line itself ("No chart was issued for
this position"), so the absence is the heading, not a decoration
above a generic "404". The requested path is text. The way back is a
nav list. HTTP status is a real 404 (or the empty state's 200) — the
theme's honesty extends to status codes.

#### 6.15 v2 — Tokens consumed

`--chart-cream`, `--isobar-grey`, `--ink`, `--ink-soft`,
`--ease-settle`.

### 6.16 Legend & the declared mapping (page family: key / reference)

- **What & why.** The key is the theme's constitution printed on the
  page: every symbol the chart uses, drawn true, beside its name —
  cold front, warm front, occluded front, stationary front, isobar
  with its interval, H, L, the wind barbs at 5/10/35/50 kt, the
  station model with its slots labelled — and beneath the symbols,
  the **declared mapping** (§1): what a station, the plotted values,
  pressure, a front, and the synoptic hours mean in this site's data.
  It belongs here because the theme's one law is auditable only if the
  audit instruments are on the page. A build that hides its mapping
  has something to hide.
- **Structure.** A panel on `--cream-deep` beneath the chart (or in
  the chart's bottom-left furniture position on detail pages): two
  columns — *Symbols* (an SVG strip of the glyphs at chart scale, each
  with its Franklin label) and *This chart plots* (the mapping, five
  short lines of apparatus text, §12's voice). The station model
  diagram is drawn at 3× chart scale with leader lines to its slot
  labels, because the model is the part readers most need taught.
  The key is present on every page that carries a chart, in full —
  never behind a "?" tooltip, never on a separate help page only.
- **Motion spec.** The key is print. Its one motion: when a visitor
  expands a station (§6.8) for the first time, the key's station-model
  diagram pulses its ring once (§6.3's pulse at diagram scale) — the
  chart teaching its own reading, once, at the moment of first
  curiosity. Otherwise the key does not move, fade, or reveal; it is
  apparatus, and apparatus is simply there.
- **States.** *Rest:* printed key. *First-expansion beat:* one pulse
  on the model diagram. *Print:* the key is in the print stylesheet's
  keep list — a printed chart without its key is an unfinished sheet.
  *No-JS:* identical.
- **Content merge.** The key's symbols are the chart's actual glyphs
  (same SVG defs, referenced, not redrawn) — the key cannot drift from
  the chart it explains. The mapping lines are the build's real
  declaration, written by whoever owns the data.
- **Failure fallback.** If the shared glyph defs fail, the key falls
  back to text-only symbol names with their plotting rules in words
  ("Cold front: blue line, triangles on the side toward which the
  front is moving") — a key that can be read with no images at all.
- **Reduced-motion variant.** The teaching pulse does not fire. The
  key is otherwise unchanged at every setting — it is the theme's
  most static element by design.
- **Performance budget & mobile variant.** Static SVG + text;
  negligible. Mobile: the two columns stack (Symbols, then the
  mapping); the model diagram stays 3× — teaching does not shrink —
  and the symbol strip wraps to two rows.

#### 6.16 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| Page load | Key stands printed; no entrance |
| Visitor's first station expansion (§6.8) | Model diagram's ring pulses once, 700ms, diagram scale |
| Never again | The key has taught; it does not repeat itself |

#### 6.16 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Printed key | Stacked key |
| Hover | No change | n/a |
| Focus | Key contains no interactive elements except the full-key link on summary placements (see edge cases) | Same |
| Active | n/a | n/a |
| Scrolled-past | Printed | Same |
| Disabled / no-JS | Printed, with text fallback for glyphs if defs fail | Same |

#### 6.16 v2 — Breakpoint behaviour

≥1200px: two columns in the panel beneath the chart. 768–1199px: two
columns, model diagram at 2.5×. <768px: stacked, diagram 3×, symbol
strip two rows.

#### 6.16 v2 — Edge cases & failure modes

*A chart using a subset of symbols (no occluded front this issue):*
the key still prints the full symbol set — a key describes the
chart's language, not one issue's vocabulary — but the mapping lines
cover only what this page plots. *A build whose mapping changes
between issues:* the key is versioned in its header ("Key — as issued
from 06 UTC, 14 May") and the colophon (§6.14) notes the change; a
silent mapping change is a §10 blocking failure. *Space pressure on a
detail page:* the key may be summarised to the model diagram + mapping
with a "Full key" link to the home chart's key — the mapping itself
may never be the part summarised away.

#### 6.16 v2 — Accessibility spec

The symbol strip's SVG is labelled glyph by glyph (`role="img"` with
each glyph's name as its title), and the mapping is plain text — the
key is fully usable by a screen reader, because the audit it enables
is not a sighted-only privilege. The model diagram's slot labels are
real text beside it, not only leader-line callouts inside the SVG.
Contrast: labels `--ink` on `--cream-deep` (≥11:1).

#### 6.16 v2 — Tokens consumed

`--cream-deep`, `--ink`, `--front-red`, `--front-blue`, `--isobar-grey`,
`--dur-pulse` (700ms).

---

### 6.17 Gale warning banner (page family: alerts)

- **What & why.** When a station's wind crosses the gale threshold
  (34 kt, §6.5), the issue carries a gale warning — the one alert this
  theme permits itself, printed as the real thing is printed: a red
  ruled block at the head of the chart naming the stations, the wind,
  and the expected duration. It belongs here because urgency in a
  chart room is a *fact about the data*, issued in words, not a
  marketing device; and because its rarity is its power — a page that
  warns when nothing is gale has cried wolf in print.
- **Structure.** A block directly beneath the masthead, present in the
  DOM only when a gale truly exists in the issue's data: top and
  bottom rules in `--front-red` 2px, the label "GALE WARNING" in
  Franklin 700 `--red-deep`, then the warning text in the office's
  voice ("Gale force 8 veering north-west at LERWICK and FAIR ISLE,
  expected until 18 UTC"), the stations named being exactly the
  stations over threshold, each a link that pins it (§6.8). If the
  mapped "wind" is not literal wind, the label is the mapping's honest
  equivalent declared in the key ("SEVERE — " plus the mapped term);
  the word GALE is used only when the theme plots weather or a mapping
  the key has explicitly named gale-equivalent.
- **Motion spec.** The warning does not animate in. It is *issued*:
  present at first paint, or — if data arrives async — plotted in
  with §6.12's 240ms plot-in and the issue line gains "WARNING ISSUED"
  in apparatus type. No flashing, no pulsing, no slide-down: a warning
  that performs is a warning that can be mistaken for an advertisement.
  When the gale passes (a later issue), the block is removed and the
  colophon records it ("The 12 UTC gale warning was cancelled at
  15 UTC") — warnings have a lifecycle in print.
- **States.** *Absent:* the common state — no block, no placeholder,
  no reserved space. *Issued:* printed block, stations linked.
  *Cancelled:* removed, colophon line added. *Hover/focus:* only the
  station links respond. *No-JS:* if the server knows of the gale, the
  block is server-rendered; a client-only build shows it from the same
  data as the chart, never from a separate "alerts" feed that could
  disagree with the plotted barbs.
- **Content merge.** The warning is computed from the same observations
  the chart plots: the gale station's barb (§6.5) and this block are
  two printings of one fact, and §10's gate cross-checks them — a
  warning naming a station whose barb shows 20 kt fails the build.
- **Failure fallback.** If the warning's data and the chart's data
  conflict (different fetch times), the block prints the more recent
  and the colophon notes the discrepancy hour; if the warning cannot
  be verified against the chart data, it is not printed — an
  unverifiable warning is worse than none.
- **Reduced-motion variant.** Identical. The warning has no motion to
  reduce; that is the point of it.
- **Performance budget & mobile variant.** Static block; negligible.
  Mobile: the block stacks (label row, then text), station links wrap;
  the rules stay full width — a warning is never truncated to fit.

#### 6.17 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| Issue (server-known) | Block present at first paint |
| Issue (async data) | Block plots in 240ms with the station that triggered it; issue line gains "WARNING ISSUED" |
| Gale passes | Block removed at the next issue; colophon records the cancellation |
| Never | No entrance flourish, no exit flourish, no flashing at any beat |

#### 6.17 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Absent | Nothing rendered | Same |
| Issued | Printed block, linked stations | Stacked block |
| Hover | Station links underline | n/a |
| Focus | Same as hover | Same |
| Active | n/a | n/a |
| Scrolled-past | Block stays at the head — it does not follow the reader (only §6.10's strip serves, and the strip does not carry the warning) | Same |
| Disabled / no-JS | Server-rendered if known | Same |

#### 6.17 v2 — Breakpoint behaviour

≥1200px: label and text on one ruled block, stations inline.
768–1199px: text wraps to two lines. <768px: stacked label/text;
block's vertical padding grows (14px) — urgency gets air, not size.

#### 6.17 v2 — Edge cases & failure modes

*The whole chart is gale (a storm issue):* the warning names the
region instead of listing 30 stations ("Gales at all stations west of
the front") — the office summarises; it does not enumerate the
obvious. *A station crossing the threshold mid-issue (async update):*
the warning issues at the next synoptic boundary, not mid-hour —
warnings belong to issues, and mid-issue changes ride as a correction
line in the affected report. *Threshold semantics:* "crossing" means
the sustained value ≥34 kt; a gust figure, if the mapping has one, is
named as a gust in the text and never silently promoted to the
sustained wind.

#### 6.17 v2 — Accessibility spec

The block is a `<section role="alert">` only when it issues
asynchronously; server-rendered warnings are plain sections (an alert
that fires on every page load trains visitors to ignore it). Text is
`--ink` and `--red-deep` on cream (≥5.9:1); the red rules are
decoration around a fully textual warning — colour is never the only
signal: the words GALE WARNING lead. Station links have full names
("LERWICK — gale, wind NW 35 knots").

#### 6.17 v2 — Tokens consumed

`--front-red`, `--red-deep`, `--ink`, `--cream-edge`, `--dur-plot-in`
(240ms), `--gale-threshold` (34 kt).

### 6.18 Town-by-town table (page family: data table)

- **What & why.** Beneath every broadsheet chart sits the town-by-town
  table: every station, every observation, in rows — the chart's
  evidence in its most checkable form. In this theme the table is the
  chart's text twin: the same data, plotted for the eye in §6 and
  tabulated for the record here. It belongs here because the theme's
  honesty law needs a form of the data that can be searched, sorted,
  copied, and read by a machine — the table is where the chart proves
  itself.
- **Structure.** A real `<table>`: columns per the declared mapping —
  Station (Franklin, gazetteer order), then the plotted values in
  station-model order (primary, secondary, pressure in full hPa,
  tendency with sign, wind in words), then the previous hour's
  pressure (the `prev` §6.4 rolls from). 36px rows, `--cream-deep`
  zebra on alternate rows, the gale station's row carrying a
  `--red-deep` left tick (2px) — the table's only colour. A totals /
  extremes foot row prints the issue's real extremes ("Highest:
  STORNOWAY 1009 · Lowest: the L, 984") computed from the rows, never
  typed by hand.
- **Motion spec.** Rows reveal on entry as printed lines: each row's
  bottom rule draws 300ms `--ease-contour` staggered 40ms in gazetteer
  order, values already printed (the table does not roll its figures —
  §6.4's roll belongs to arrivals; the table is the record, and
  records do not perform). Sorting (by any column, via the header
  buttons) re-orders rows instantly with no animation — a sorted table
  is a new statement, not a performance. The extremes row recomputes
  and reprints on sort only if the sort changes nothing about extremes
  (it cannot) — it is computed from data, not from DOM order.
- **States.** *Rest:* full table, gazetteer order. *Sorted:* the
  sorted column's header carries the plotter's mark (a small ▲/▼ in
  mono — the table's one glyph pair) and `aria-sort`. *Hover:* row
  ground deepens one step (`--cream-deep` → `--cream-edge` at 40%).
  *Focus:* rows are not focusable; the station name is a link to its
  report (§6.8's join, from the table side). *No-JS:* full table,
  gazetteer order, extremes printed — sorting is the only lost
  behaviour.
- **Content merge.** The table *is* the content in its second form;
  its rows are generated from the same dataset as the chart, and §10
  cross-checks three random rows against the chart's plotted values.
- **Failure fallback.** If chart data fails but table data loads, the
  table stands alone with the office line "The chart was not issued;
  the observations follow" — the record outranks the picture. If a
  cell's value is missing, it prints `///` (§6.4's convention), and
  the extremes row excludes missing values and says so if an extreme
  is affected.
- **Reduced-motion variant.** Row rules are printed, not drawn.
  Sorting identical. Nothing else moves in a table.
- **Performance budget & mobile variant.** ≤ 60 rows per table (a
  bigger network paginates by region as separate tables with their own
  headings — chart-room practice, not infinite scroll). Mobile: the
  table scrolls horizontally inside a ruled frame with the Station
  column sticky; columns are never dropped — a phone reader gets the
  whole record, scrolled, not an abridged one.

#### 6.18 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| Table enters | Row rules draw in gazetteer order, 40ms stagger, 300ms each |
| Values | Printed from first paint — no roll, no fade |
| Sort activated | Rows re-order instantly; header mark moves; extremes unchanged |
| Gale row | The red tick is present from paint — the table does not discover drama |

#### 6.18 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Gazetteer order, zebra rows | Same, horizontal scroll frame |
| Hover | Row ground deepens | n/a |
| Focus | Station links and sort buttons take the theme focus ring | Same |
| Active (sorted) | Header mark + `aria-sort` | Same |
| Scrolled-past | Static record | Same |
| Disabled / no-JS | Full table, no sorting | Same |

#### 6.18 v2 — Breakpoint behaviour

≥1200px: all columns, 36px rows. 768–1199px: all columns, 34px rows,
mono at 13.5px. <768px: ruled scroll frame, sticky station column,
16px vertical row padding for touch on the station links.

#### 6.18 v2 — Edge cases & failure modes

*A station with a very long name:* the Station column caps at 22ch
with the full name in the report heading and the link's accessible
name; values never truncate — a truncated figure is a wrong figure.
*Ties in extremes (two stations at 1009):* both are named; the office
does not pick a winner. *A table for a detail page (one station, 24
hours):* the same grammar transposed — rows are hours, columns the
values; the extremes row becomes the day's range. The component is
the record, whatever its rows are. *Print:* the table prints in full
across as many pages as it needs; the zebra drops to rules only.

#### 6.18 v2 — Accessibility spec

A native `<table>` with `<th scope="col">`, sort controls as real
buttons inside the headers with `aria-sort` on the sorted column, and
a `<caption>` that is the table's situation line ("Observations for
12 UTC, 24 stations"). The gale tick is decoration beside a text fact
(the wind value itself, and §6.17). Mono figures at 14px, `--ink` on
cream/cream-deep (≥11:1). Sticky-column shadow never obscures a value
at rest.

#### 6.18 v2 — Tokens consumed

`--ink`, `--cream-deep`, `--cream-edge`, `--red-deep`, `--ease-contour`,
`--dur-row-rule` (300ms), `--stagger-row` (40ms), `--font-obs`.

---

## 7. Page application map

- **Home (the full issue).** The complete grammar: masthead + clock
  (§6.10, §6.7), gale warning if earned (§6.17), general situation
  (§6.11), the pinned stage and rail (chart + all station reports,
  §§6.1–6.8), the town-by-town table (§6.18), key + mapping (§6.16),
  the observation slip (§6.13), colophon (§6.14). This is the page the
  worked examples (§8) describe.
- **Listing / region page (a sub-chart).** One region of the network
  at larger scale: the chart crops to the region (stations at the
  region's own spacing, isobars at 2 hPa — a bigger chart earns a
  finer interval, stated in its key), reports for the region's
  stations only, its own table. The parent chart appears as a locator
  in the situation block with this region ringed. Time-step (§6.9)
  moves between regions at the same hour: symbols do not advance, and
  the transition says "SAME ISSUE — REGION".
- **Detail / station page (one station, all hours).** The chart is the
  station's locality at the largest scale, the station itself at
  centre plotted in full; the rail becomes the day's hours (00/06/12/
  18 reports for this station), and the table (§6.18's transposed
  form) is the day's record. The barb (§6.5) spins on arrival if any
  hour is gale; the clock (§6.7) is fixed to the page's issue and the
  hours are navigated in the rail, not the masthead.
- **About (the chart room).** The office explains itself: how the
  chart is plotted, where the observations come from, the mapping's
  history. The chart on this page is a worked specimen — a real past
  issue, labelled with its date — never a decorative live chart. The
  pedant's note (§6.14) is promoted into the text: this page *is* the
  invitation, expanded.
- **Contact / conversion.** §6.13's slip is the page; the chart
  reduces to the visitor's locality inset (where their station will
  be plotted), and the key (§6.16) sits beside the form — the office's
  two documents, per §6.13's layout rule.
- **404 / empty.** §6.15, exactly as specced: the unissued chart, the
  office's line, the way back.
- **Print.** The home chart prints as a broadsheet sheet: chart,
  table, key, colophon on the keep list; rail reports flow as
  columns; all motion states resolve to their printed forms (fronts
  at forecast position, values current, isobars analysed).

## 8. Worked examples

### 8.1 The hero — a harbour network's 12 UTC issue

*The build: a port-services company's status page. Declared mapping:
stations = its 9 ports; "temperature" slot = berths free; "dew point"
slot = berths occupied in 6h (booked); pressure = harbour load index
in hPa-equivalents (declared formula in the key); fronts = the
boundary between ports at capacity and ports with room; wind = the
literal wind at each port, from the met office feed; hours = the
page's four watches.*

The visitor lands. The masthead stands printed: office block, clock
hand on 00 (the first watch), issue line "ISSUED 12 UTC — NEXT 18
UTC". No gale block: the highest literal wind is 28 kt, and the theme
does not warn below 34. The hero (§6.11) issues the situation in 71
words: a deepening low (load centre 984 over the western ports), a
cold front (capacity boundary) lying from the low to the southern
coast and advancing south-east, rain of bookings behind it. The vital
line rolls at +400ms: centre 991 → 984, busiest port's figure from
the 06 UTC issue to now. Below, the chart reveals through the
principal port's station circle (1400ms mask) over a fully drawn
sheet: isobars contour in pressure order out of the 984 low
(1100ms lines, 120ms stagger), the cold front's line draws and its
blue triangles plot in trailing-first, pointing south-east — the way
the capacity boundary is actually moving, because the front's mapped
motion is computed from the ports' booking curves, and the key says
so. The visitor scrolls; the stage pins; the front begins its march.

### 8.2 Mid-page — the Lerwick report arrives

The third report in the rail is the northernmost port. Its section
top crosses 70% vh: on the pinned chart, 600px away, the station's
pulse ring expands 6 → 26px and fades (700ms). In the same beat its
values roll in plotting order — berths free 4 → 2 (70ms), booked
9 → 11 (140ms), load `038` → `041` (210ms), tendency `+3` (280ms) —
each a replay between the 06 and 12 UTC truths. The port's literal
wind is NW 35 kt: it is the gale station after all — the async met
feed landed after the hero printed, so §6.17's lifecycle applies: the
warning issues at the next synoptic boundary of the page (the 18 UTC
watch's head), plotted in 240ms, naming this port; here, at arrival,
the barb performs §6.5: shaft rewound to north, rotating by the
shortest arc to NW over 720ms, then feathers plotting outward —
three long, one short: 35 kt, readable by anyone who can read a barb,
and stated in words in the report's head for everyone else: "Wind NW
35 kt, gale." The visitor hovers the station: the halo opens to its
sea side (the port's `data-halo` side is west, over water) with the
full string. They click: the rail smooth-scrolls the report to centre,
the chart pans 60 units so the port sits mid-stage, and the report's
head carries its ink rule. The chart and the filing are one dataset,
and the visitor has just walked the join in both directions.

### 8.3 Conversion — filing an observation

At the page's foot, beside the key, sits the observation slip (§6.13):
the company takes berth requests here. The slip's header assigns the
visitor a provisional station — "NEW STATION — UNPLOTTED" — and types
its code at telegraph pace when the slip arrives. The fields are the
honest ones: port (a select drawn as a station list), date required,
berths required, the observer's email as call-sign, remarks. The
visitor mis-keys the email; on submit the field's rule turns
`--red-deep` and the error letters in beneath in the office's voice:
"That call-sign will not carry a reply — check the address." Nothing
they typed is cleared. They fix it, file again: the button presses,
the header shows "FILING…", and the acknowledgement plots in — a
160-unit locality inset of the chart with a new station circle inked
at their port, and the filed line: "Filed 12 UTC · Station No. 41 ·
Berth request held until 18 UTC." The number is the server's real
count of requests; the hold hour is the office's real promise. The
colophon below records the issue's provenance, and — because the gale
warning issued during this visit — its lifecycle line: "Gale warning
issued this page-view at the 18 UTC watch; the printed 12 UTC issue
carried none." Honesty about what changed while you were reading is
still honesty.

---

## 9. Anti-slop — what makes THIS theme look cheap

1. **A front pointing the wrong way.** Triangles or semicircles on the
   trailing side, or pointing against the declared travel — the single
   most damning error in the theme, because every knowledgeable reader
   sees it instantly. *Cure:* the direction is data (§6.1); the gate
   (§10) checks each front's glyph orientation against its declared
   travel, by eye, on the printed chart.
2. **Wind barbs with decorative feathers.** Feathers that don't sum to
   the station's speed, or a barb on every station spun for effect.
   *Cure:* feathers are computed from the speed (§6.5); only the gale
   station spins; the key prints the feather values so anyone can add
   them up.
3. **Isobars that cross, kiss, or wander.** Smooth plausible rings
   drawn by eye instead of contoured from values. *Cure:* contours are
   interpolated from station data (§6.2); crossing paths fail the
   build; sparse data means *no* analysis, stated in the key.
4. **Pressures off the sequence.** Labels like 1003 or 998.5 — values
   no plotter would write. *Cure:* isobar labels come only from the
   4 hPa ladder (§6.2); station coded values follow the three-digit
   convention (§4).
5. **A station plot with values in the wrong slots.** The primary
   figure at bottom-right because it "looked balanced". *Cure:* the
   station model is law (§4); the key's diagram teaches it; the gate
   checks two stations against the diagram.
6. **Numbers that count from zero, or to invented values.** A roll
   that starts at 0 is a slot machine. *Cure:* every roll is a replay
   between the previous and current real readings (§6.4); a missing
   previous means no roll, and a missing value means `///`, never 0.
7. **A gale warning with no gale.** Red urgency as a style. *Cure:*
   the block exists only when data crosses 34 kt, is cross-checked
   against the barbs (§6.17), and its absence is the normal state.
8. **Stations invented to balance the composition.** A lonely corner
   of the chart gets a fake port. *Cure:* empty sea is left empty
   (§4); stations come from the dataset, and the dataset's size is
   printed in the table caption.
9. **Weather clip-art.** A sun icon by the H, a cloud emoji in a
   heading, a rainbow gradient "temperature scale". *Cure:* the
   chart's entire iconography is the plotted symbol set (§6.16); if it
   isn't in the key, it isn't on the chart.
10. **The mapping hidden or embarrassed.** Calling things "pressure"
    and "fronts" without saying what they mean in this site's data.
    *Cure:* the declared mapping prints in the key on every chart page
    (§6.16) and in short form in the colophon (§6.14). A build that
    won't declare doesn't ship.
11. **Motion on the facts.** Values that bounce, headings that slide,
    a breathing front. *Cure:* motion lives only where §5 puts it —
    arrivals, the march, the breathing *analysis* — and the plotted
    facts (figures, barbs, station positions) never move for style.
12. **A generic dashboard wearing a chart skin.** Cards with drop
    shadows floating over a map wallpaper. *Cure:* panels sit *on* the
    sheet (§2's `--cream-deep`, no shadows anywhere in the theme);
    if a component could be lifted off the page without the data
    noticing, it is rebuilt as plotted furniture or removed.

## 10. Quality gate

**Blocking — all must pass:**

1. **Front audit.** Every front's symbols sit on the correct side and
   point along the declared direction of travel; stationary fronts
   carry opposed symbols and do not march. Checked by eye against the
   key on the rendered chart.
2. **Barb audit.** For three stations (including the gale station):
   feathers sum to the plotted speed ±0 (nearest-5 convention), shaft
   points from the true direction, calm stations carry the double
   circle.
3. **Isobar audit.** All labels from the 4 hPa sequence (8 hPa on
   mobile); no two isobar paths intersect; if stations < 5, no
   analysis is drawn and the key says why.
4. **Station-model audit.** Two stations checked slot by slot against
   §4/§6.16's diagram, including the three-digit pressure coding.
5. **Value-truth audit.** Every roll's `data-prev`/`data-now` traced
   to the dataset; every counter and filed number traced to a server
   count; three random table rows match the chart's plotted values.
6. **Mapping audit.** The declared mapping is printed in the key on
   every chart page and matches the data actually plotted; the
   mapping's five sentences (§1) are written and current.
7. **Warning cross-check.** If §6.17's block is present, its stations'
   barbs show ≥34 kt; if any barb shows ≥34 kt, the block is present
   (or its issue-boundary timing is documented per §6.17).
8. **JS-off audit.** With JavaScript disabled: the complete chart at
   forecast positions, all reports, the full table, the key, and a
   working form. Nothing invisible, nothing `///` that has a value.
9. **Stall audit.** With the rAF loop frozen: the 1200ms watchdog
   delivers the fully drawn static chart; no element waits on
   `transitionend`.
10. **Reduced-motion audit.** With `prefers-reduced-motion`: the
    chart static at the latest observation, all values current, the
    warning (if any) present, zero ambient loops running.

**Standard — should pass, fix before ship unless noted:**

11. Every element's stated performance budget measured on a mid-tier
    phone: breathing ≤1.5ms/frame, all scrub writes in the one loop.
12. Contrast spot-checks: values 12.2:1, apparatus ≥7.6:1, front-red
    text never below its size floor (§2).
13. The situation (§6.11) is ≤90 words and every figure in it appears
    on the chart.
14. Print check: chart + table + key + colophon print complete; fronts
    at forecast positions.
15. The pedant's note is present in the colophon, and the key it
    points to is reachable in one click from every chart page.

---

## 11. Component inventory

Every component a real site in this theme needs, with its themed
treatment — and the theme's refusals, each with its in-world
replacement.

| Component | Treatment in this theme |
|---|---|
| Buttons (primary) | The plot-button (§6.13): ink-bordered, uppercase Franklin 600, transparent ground; press = scale 0.97, 120ms. One primary per view |
| Buttons (secondary) | Text links with the drawn rule (§6.10's grammar) — the chart room has one button weight; everything else is an index entry |
| Links | `--front-blue` in prose, ink + rule in apparatus; visited = `--blue-deep`; never underlined by default in chart labels |
| Text inputs | Station-entry fields (§6.13): bottom-ruled, mono input text, apparatus labels |
| Selects | A station list: the native select restyled to the slip's ruled grammar, options in gazetteer order; on the chart pages, region choice is a chart-frame tab (below) |
| Checkboxes / radios | Plotted squares/circles: an empty station circle that inks in when chosen (radio), a square ruled box with an ink tick (checkbox) — the marks are the theme's own glyphs |
| Tables | §6.18, the town-by-town grammar: mono, zebra `--cream-deep`, sortable by header buttons |
| Badges / chips | **Refused.** A category on a chart is a symbol in the key, not a pill. Replacement: the fact printed in apparatus type beside its subject ("GALE", "FIRST REPORTS") |
| Alerts | §6.17's gale warning is the only alert grammar; lesser notices are printed lines in the affected report or the colophon — never banners |
| Pagination | The time-stepper: "← 06 UTC · 12 UTC · 18 UTC →" as index entries under the chart; numbered pages do not exist in an issued world |
| Tabs | Chart frames: region tabs are ruled title-block strips above the chart (the sheet for that region); switching re-plots per §6.9 at the same hour |
| Accordions | The report rail is the accordion's honest form: reports are open by default; on mobile they collapse to their head lines with a ruled "Read the filing" disclosure — a real `<button>` + region, opening by wipe (300ms) |
| Modals | **Refused.** Nothing in a chart room interrupts. Replacement: station expansion (§6.8) for detail on the chart; the slip (§6.13) in flow for tasks |
| Toasts | **Refused.** News in this world is issued, not popped. Replacement: the colophon's erratum/cancellation lines (§6.14) and the report's own correction marks |
| Tooltips | **Refused.** Replacement: §6.8's halo — detail plotted on the chart itself, at chart scale |
| Progress bars | **Refused.** Replacement: the observation clock (§6.7) for page progress; the awaiting sheet (§6.12) for loading |
| Spinners | **Refused, absolutely.** Replacement: §6.12's unplotted sheet and §6.13's "FILING…" — states of the work, not abstractions of it |
| Search | "Ask the office" (§6.15): a ruled input whose results are a station index list — names + hours, no cards |
| Breadcrumbs | The issue line: Region / Station / Hour, set as chart furniture with rule separators — the visitor's position stated as a chart position |
| Cards | Station cards exist only as the way-back card (§6.15) and take §6.18's row grammar enlarged: ruled, flat on the sheet, no shadow |
| Empty states | §6.15's unissued chart; empty tables print their columns with the office line as the single row |
| Error states | §6.13's field errors (red-deep rule + lettered line) and §6.12's failed stations (`///`); page errors are §6.15 with the error named |
| Focus ring | 2px `--ink` outline, offset 2px, everywhere; on the chart's station buttons, offset 3px against the sheet |
| Skip link | "Skip to the reports" — apparatus type, appears on focus at the masthead's head |

## 12. Content & copywriting voice

**The forecaster's voice.** The office writes the way the shipping
forecast is written: present tense, observational, economical, every
sentence carrying a fact. Headlines are situations, not slogans.
Labels are gazetteer names. The theme has two registers and never
mixes them: **the chart** (symbols, figures, labels — no adjectives)
and **the office** (the situation, reports, errors, the colophon —
plain sentences, dry warmth allowed exactly once per page, usually in
the colophon).

**Headline style.** Region + hour, or the situation's core fact.
✓ "North Atlantic — 12 UTC" · ✓ "The low deepens west of the region"
✗ "Your data, visualized like never before!" ✗ "Welcome to the
dashboard"

**The general situation (§6.11).** ≤90 words, systems named as the
chart names them, movement stated with direction and time.
✓ "A deep low, 984, lies west of the region and is deepening. Its
cold front advances south-east, reaching the southern stations by
18 UTC. Behind it, the ridge builds and the northern ports clear."
✗ "There's a lot going on in your data today! Let's dive in and see
what the numbers are up to."

**Report heads.** Station name, then the observation in words, in
station-model order.
✓ "LERWICK — Wind NW 35 kt, gale. Load 1004, rising 3. Berths 2 of 14."
✗ "Lerwick is having a busy one!! 🌬️"

**Error voice (§6.13).** Name the entry, state the fact, say what to
do. No apology theatre, no blame.
✓ "That call-sign will not carry a reply — check the address."
✓ "Observation not received — the station's last report stands."
✗ "Oops! Something went wrong 😢" ✗ "Invalid input."

**Empty voice (§6.15).** Absence reported as a fact of the issue.
✓ "No chart was issued for this position." ✓ "This station files at
18 UTC; the current issue is 12 UTC."
✗ "404 — you've wandered off the map!" (the theme does not joke about
being lost at sea, and neither should the build)

**Confirmation voice (§6.13).** The filed line: hour, station number,
the promise with its hour.
✓ "Filed 12 UTC · Station No. 41 · Held until 18 UTC."
✗ "Success! 🎉 You're all set!"

**Banned words and habits.** "Dashboard", "widget", "leverage",
"supercharge", exclamation marks outside a quoted report, emoji
everywhere (the chart's symbols are the only icons), "content" as a
noun for the observations, and any adjective the data hasn't earned
("dramatic" pressure fall — the tendency figure says how dramatic).
**Owned words.** Issued, plotted, filed, observed, the office, the
issue, station, watch, "at the last observation".

**Fixed strings (verbatim, do not paraphrase).** The pedant's note:
*"Every symbol on this chart is drawn as the convention requires —
fronts point the way they are moving, and a barb's feathers sum to its
wind. Pedants are invited to check."* · The awaiting line: "Awaiting
observations." · The missing mark: `///`. · The sign-off: "End of the
[hour] issue."

---

## 13. Full-page scroll choreography map

The home issue (§7), top to foot. One loop (lerp 0.14) drives every
scrubbed beat; everything else is triggered, once, in filing order.

| Beat | Position | What the visitor sees and feels |
|---|---|---|
| 1 | Load | Masthead printed; clock on the first watch; hero rules draw (600ms); the situation issues |
| 2 | Load +400ms | Hero vital figures roll from the previous issue's truths (§6.11) |
| 3 | Load +~1s | Chart reveals through the principal station's circle (1400ms mask) over the finished sheet |
| 4 | Chart reveal | Isobars contour in pressure order out of the low, then the high (§6.2); fronts draw, symbols plot trailing-first (§6.1) |
| 5 | Chart settled | Breathing fades in over 1s (§6.6); grain begins its 26s drift — the sheet is alive, barely |
| 6 | Stage pins | Issue strip takes the masthead's place; the rail begins filing |
| 7 | Each report enters | Pulse on its station → values roll in plotting order → barb sets; the gale station spins (§§6.3–6.5) |
| 8 | Throughout the rail | Fronts march with scroll (140 units over the stage); the clock snaps watch to watch (§6.7); parallax holds its 6px discipline (§5) |
| 9 | A warning earned mid-page | Issues at the next watch's head, plotted in, never performed (§6.17) |
| 10 | Rail exhausted | Stage releases; the last report's station rests at forecast position — the weather has fully advanced |
| 11 | Table enters | Row rules draw in gazetteer order; the record stands (§6.18) |
| 12 | Key | Print, and stillness; the mapping read at rest (§6.16) |
| 13 | The slip | Border draws; the station code types once; the visitor files (§6.13) |
| 14 | Colophon | The final rule draws — the sheet ruled off; the sign-off (§6.14) |

**Emotional arc.** Authority (the office, the situation) → wonder
(the chart assembling itself correctly) → participation (the weather
moves because *you* read) → trust (the table, the key, the invitation
to check) → membership (your own station, filed). **Reverse pass:**
scrolling up reverses every scrubbed value exactly (fronts
un-advance, clock returns to earlier watches); triggered beats
(arrivals, rolls) do not re-fire without a full exit and re-entry —
the issue does not un-happen. **Jump-scroll catch-up:** a jump to the
foot fires, in order and compressed: chart fully contoured, all
passed stations marked arrived silently, fronts at the jump's true
offset, clock on the jump's watch — the state is always a function of
position, never of the path taken.

## 14. Whole-page performance budget

| Budget | Limit |
|---|---|
| Chart SVG (all layers, gzipped inline) | ≤ 60 KB |
| Total page weight (fonts subsetted: Franklin 400/600/700/800, Plex Mono 400/500/600) | ≤ 420 KB |
| Isobars per chart | ≤ 14 paths, ≤ 120 points each |
| Front symbols per chart | ≤ 48 glyphs total |
| Stations per chart | ≤ 40 plotted, ≤ 60 in the table |
| Animation frame budget (the one loop) | ≤ 3ms/frame total; breathing ≤ 1.5ms of it |
| Long tasks during scroll | none > 50ms; contour computation happens at build, never at runtime |
| Layout shift | 0 from any animation (tabular figures, reserved slots, sheet geometry fixed) |

**Cut order when the budget is exceeded** (cut in this order, restore
in reverse): 1. Isobar breathing (§6.6) — ambience goes first. 2.
Chart grain drift. 3. Parallax layer separation (§5) — the chart
scrolls flat. 4. The circle-mask chart reveal (§5) — the chart simply
stands issued. 5. Halo pan on pin (§6.8) — pinning still scrolls the
rail. 6. Front symbol density (spacing 56 → 72 units at all sizes).
**Never cut:** value rolls (§6.4 — they are the arrival), the front
march (the signature), the clock (the only progress), the watchdogs,
or any fallback. A build that cuts a never-cut item to afford an
ambience has the theme backwards.

## 15. Build-order checklist

1. **The static issued chart first.** Sheet, graticule, coastline,
   stations plotted complete at forecast positions, values current —
   with JavaScript off. This is the page's truth; everything after is
   performance over it.
2. **The declared mapping** written (§1's five sentences) and the key
   (§6.16) built from the chart's real glyph defs.
3. **The table** (§6.18) from the same dataset; cross-check three rows
   against the chart by hand.
4. **Masthead, clock (static), hero, colophon** — the issue's
   furniture, printed.
5. **The rail and the pin** (§4): stage pins, reports file, locator
   insets for mobile.
6. **Arrivals:** observer, pulse (§6.3), rolls (§6.4), barb (§6.5) —
   in that wiring order, one beat.
7. **The march:** front scrub in the shared loop (§6.1); parallax
   layers (§5).
8. **Contouring** (§6.2) armed over the finished lines; breathing
   (§6.6) last of the chart systems, behind the fps check.
9. **Interactions:** expansion + pin (§6.8), index + issue strip
   (§6.10), clock watch tracking (§6.7).
10. **The slip** (§6.13) with its error and acknowledgement states;
    the warning (§6.17) wired to the same dataset as the barbs.
11. **Transitions** (§6.9) and the unplotted sheet (§6.12) for
    client-side loads; the missing chart (§6.15).
12. **Reduced-motion pass:** every element's variant verified against
    §10 item 10.
13. **The audits:** §10 blocking items 1–9, in order — front, barb,
    isobar, station model, value truth, mapping, warning, JS-off,
    stall.
14. **Print stylesheet:** chart, table, key, colophon complete on
    paper.
15. **The gate** (§10) signed by someone who did not build the chart —
    the pedant is a role, and it is never the plotter.
