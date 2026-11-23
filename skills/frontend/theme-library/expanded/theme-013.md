# Theme 013 — The Shipping Forecast (Expanded: v1 + v2 / 50x standard)

> Source identity preserved exactly from `themes-001-025.md` §13: the poetry of
> maritime weather bulletins; the 31 sea areas are the site's geography; the
> layout is a chart of regions, not a stack of sections; scroll travels
> *across* the chart while a fixed broadcast column types the forecast for
> whichever region is passing. Palette anchors: Chart paper `#EDE8D8`, Sea ink
> `#1D3A4A`, Buoy red `#C0392B`, Gale grey `#6B7680`. Faces: Fraunces (area
> names, display) + IBM Plex Mono (the forecast voice — all bulletin text and
> readings). This file deepens that entry; it does not redesign it.

---

## 1. Concept & world

**The world.** A synoptic chart on a chart table, and a voice reading the
weather over it. The Shipping Forecast is the BBC/Met Office bulletin for the
31 sea areas around the British Isles, read in a fixed order, in a fixed
grammar, at fixed times of day. Its areas have names like poetry — Viking,
Forties, Dogger, FitzRoy, Fastnet, Rockall — and its sentences are built from
a closed vocabulary: a wind direction and a Beaufort force, a weather word, a
sea state, a visibility. "FORTIES. SOUTHWESTERLY 5 OR 6. RAIN LATER.
MODERATE." Nothing in it is decorative. Every mark on a synoptic chart is a
measurement; every word in the bulletin is an observation or a warning. This
theme takes that discipline as its whole aesthetic: **the site is a chart,
the sections are sea areas, and a broadcast column reads the site aloud as
you cross it.**

**The fiction the visitor lives inside.** The visitor is not "browsing a
page". They are standing at a chart table while the forecast is read. Scroll
is the hand moving across the chart from Viking in the north-east, area by
area in broadcast order, to Southeast Iceland at the end of the list — the
same journey the spoken bulletin makes four times a day. The broadcast column
pinned at the right is the radio on the shelf: it types, in mono, the
forecast for whichever area is currently centred under the visitor's eye.
Progress is not a percentage; it is a compass needle and a count of areas
covered, because on a chart you are never "63% done" — you are *somewhere*,
and somewhere has a name and a bearing.

**Mood.** Calm authority at 3 a.m. The forecast is famous for being read to
people who are asleep, half-asleep, or alone on watch. The theme's register
is therefore: unhurried, exact, faintly melancholic, completely trustworthy.
Nothing shouts except a gale warning, and even that shouts only by
letterspacing. The paper is warm, the ink is deep sea blue-black, the single
red is the red of a buoy and of a warm front — a colour that means *attend*,
never *buy now*.

**Best-fit sites and audiences.**
- Travel and expedition brands whose product is literally a journey across
  named waters: ferry operators, sailing schools, expedition cruise lines,
  tall-ship charters, island-hopping tour companies.
- Weather products: a forecast app or data service that wants its data to
  feel like an instrument reading rather than a dashboard widget.
- Coastal hotels and harbour businesses, where the "areas" become rooms,
  beaches, walks, or menu sections named for the waters offshore.
- Publishers and long-form storytellers: a documentary, a book, a podcast
  season structured as a passage through named places.
- Any brand whose content naturally divides into 8–31 named regions with a
  fixed visiting order and a short factual bulletin per region.

**When NOT to use it.**
- When the content has no geography and no fixed order. If the sections
  could be shuffled without loss, the chart is a lie and the theme collapses
  into clip-art.
- When the primary task is rapid comparison shopping or dense data entry:
  horizontal travel is a passage, not a grid; users in a hurry need a table,
  not a voyage.
- When there are fewer than 5 or more than 31 content regions. Below 5 the
  chart is empty paper; above 31 the areas stop being places and become
  noise. (Sub-divide into "inshore waters" annexes instead — see §7.)
- When the brand voice is exclamatory. This theme cannot shout, bounce, or
  sparkle. If the copy needs exclamation marks, pick another theme; the only
  permitted emphasis is a gale warning.
- On sites that must be fully usable in under 10 seconds by first-time
  visitors with no guidance: the horizontal act needs one beat of learning
  (the porthole reveal teaches it), and §10's gate blocks shipping without
  the reduced-motion vertical stack that removes the learning curve.

**The one law.** Every visual element on the chart must be a real piece of
chart furniture or a real piece of forecast grammar. If a mark does not
correspond to a pressure, a front, a station, an area, or a word in the
bulletin, it is deleted. Decoration that is not information is this theme's
definition of slop (§9).

---

## 2. Palette

Four anchors from the source entry, plus derived tokens. Derived tokens are
labelled DERIVED and are tints/shades of the anchors only — no fifth hue
enters the chart. (On a real synoptic chart, cold fronts are drawn blue and
warm fronts red; this theme's two chromatic inks map exactly: cold front =
sea ink, warm front = buoy red. Occluded fronts alternate both.)

| Token | Hex | Role | Usage ratio | Pairing / contrast |
|---|---|---|---|---|
| `--paper` | `#EDE8D8` | Chart paper — page ground, chart field | 62% of surface | Ground for `--ink` text: 10.9:1. Ground for `--gale` text: 4.6:1 (large/mono labels only, never body) |
| `--ink` | `#1D3A4A` | Sea ink — body text, isobars, area boundaries, cold fronts | 24% | On `--paper` 10.9:1 (AAA body). The only colour body text may use |
| `--buoy` | `#C0392B` | Buoy red — warm fronts, gale words, the needle's north point, click ping | 3% | On `--paper` 4.9:1 — display and bold mono only, never body text below 14px bold |
| `--gale` | `#6B7680` | Gale grey — secondary labels, station metadata, disabled states, hairline annotations | 8% | On `--paper` 4.6:1 — minimum size 12px mono uppercase; never below |
| `--paper-deep` (DERIVED) | `#E2DBC4` | Chart table shadow side — panel fills, card ground, the broadcast column's inset | 3% | With `--ink` text 9.8:1 |
| `--ink-pale` (DERIVED) | `#1D3A4A` at 18% | Area hover fill (§6.10), selected-area wash | overlay only | Never carries text; text above it stays `--ink` on `--paper` (effective contrast ≥9:1 through the wash) |
| `--ink-hairline` (DERIVED) | `#1D3A4A` at 35% | Chart grid lines, isobar secondary rings, table rules | lines only | Non-text; exempt from text contrast, held ≥3:1 against `--paper` for the grid's structural lines |
| `--paper-line` (DERIVED) | `#EDE8D8` at 0% → used as `rgba(237,232,216,0)` | Fade masks at chart edges during travel | overlay only | — |

**Usage law.** The ratio is a discipline, not a suggestion: a screen that is
more than ~6% buoy red has cried wolf; red is rationed to warm fronts, gale
words, one needle point, and the click ping. Gale grey never sets a headline.
Sea ink is the voice; paper is the silence around it.

**Dark-mode behaviour — "night watch".** The chart does not invert. A chart
table at night is lit by a dim red lamp (red light preserves night vision —
a real chart-room practice), so the dark variant is: ground becomes a deep
ink `#12242F` (a shade of `--ink`, DERIVED for dark use only), paper-text
becomes `#EDE8D8` at full strength for bulletin text (contrast 11.6:1) and at
72% for secondary text (7.4:1), isobars and grid drop to `--paper` at 28%,
buoy red lightens one step to `#D84A38` (5.1:1 on the dark ground, display
only), gale grey lifts to `#93A0AA` (5.8:1). The porthole reveal, the
breathing, and the marching fronts are unchanged — a lamp does not change
the weather. The variant is triggered by `prefers-color-scheme: dark` or a
manual "Night watch" toggle in the header (§6.13); it is never triggered by
time of day automatically, because a visitor in daylight with a dark OS
setting has already made their choice.

---

## 3. Typography

Two faces only. **Fraunces** sets area names and display — it has the
engraved, slightly eccentric serif character of chart lettering, where area
names were lettered by hand-spaced capitals along a curve. **IBM Plex Mono**
is the forecast voice: every bulletin sentence, reading, label, counter, and
piece of data. Nothing else is set in anything else. A third typeface on a
chart is a forgery.

| Role | Face / settings | Size (desktop / mobile) | Line-height | Tracking | Rules |
|---|---|---|---|---|---|
| Area name (on chart) | Fraunces 560, uppercase, set along the area's centroid | 44–96px by area size / 30–44px | 1.0 | +0.04em | Never rotated more than the area's own long axis; never outlined; ink only |
| Display / headline | Fraunces 480 | 56px / 34px | 1.04 | −0.01em | Sentence case — the chart does not shout its headlines |
| Section heading (in vertical acts) | Fraunces 560, uppercase | 28px / 22px | 1.1 | +0.05em | Always an area name or a chart term (Synopsis, Inshore Waters) |
| Bulletin text (forecast voice) | IBM Plex Mono 400, uppercase | 15px / 13.5px | 1.55 | +0.02em | The grammar of §12 is mandatory; full stops are the punctuation |
| Body copy | IBM Plex Mono 400 | 15.5px / 14.5px | 1.65 | 0 | Lowercase permitted only outside the broadcast column; inside the column, all bulletin |
| Reading / data | IBM Plex Mono 500 | 15px tabular | 1.4 | +0.01em | Digits never proportional; odometer rolls (§6.6) require tabular figures |
| Caption / station metadata | IBM Plex Mono 400, uppercase, `--gale` | 12px / 11.5px | 1.45 | +0.08em | Never below 11.5px; never in `--buoy` |
| Compass / instrument labels | IBM Plex Mono 500, uppercase | 11.5px | 1.3 | +0.12em | Set like dial engraving |

**Type laws.**
1. Area names are lettering, not headings: they sit inside their areas, sized
   by the area's extent (largest area, largest name — Rockall small and
   lonely, Biscay broad), exactly as chart lettering is sized by the water it
   names.
2. The forecast voice is always uppercase mono. The moment bulletin text is
   set in a proportional face or sentence case, the radio is off and it is
   just a website again.
3. Numbers are instruments. Pressures are 4 digits with `HPA` once per group;
   wind is a Beaufort force, never km/h, inside the bulletin (a conversion
   may appear in station cards, §6.15, labelled as conversion).
4. Fraunces never sets a number and mono never sets an area name. The two
   voices never swap jobs.

---

## 4. Layout language

**The chart is the layout.** The page's main act is a synoptic chart,
rendered as one wide SVG field (viewBox `0 0 6400 1000`) carrying: the chart
grid (lat/long hairlines every 160 units), the 31 area boundaries as drawn
polygons with their names lettered inside, isobars as concentric smooth
curves around 2–4 pressure centres, cold and warm fronts as symbol lines,
station dots at coastal stations, and a compass-rose watermark at 6% ink in
the field's north-west. The chart sits in a horizontal travel act: a tall
vertical scroll region (the "passage", §5) whose scroll progress scrubs the
chart's `translateX` from 0 to −(chart width − viewport width).

**Fixed furniture.**
- **Header (the masthead bar):** 56px, paper ground, hairline rule below.
  Left: the wordmark set as a broadcast header (§6.13). Centre-right: the
  compass instrument (§6.8). Right: areas-covered counter and the Night
  watch toggle.
- **Broadcast column:** pinned at the right edge, 320px wide at ≥1200px,
  full-height, `--paper-deep` ground with a hairline left rule. It carries:
  the current area's name (Fraunces), its typed forecast (§6.3), its station
  readings (§6.6), and the gale-warning slot (§6.7). The chart travels
  *behind* the page but never *under* the column: the pan range is computed
  so the centred area is centred in the space left of the column.
- **The passage:** the scroll length of the travel act is
  `31 areas × 38vh ≈ 1180vh` at desktop; each area owns an equal share of
  the scrub, so travel speed is constant in areas-per-scroll, not
  pixels-per-scroll.

**Vertical acts.** Before the chart: the hero (§6.14), which is the chart's
own opening (porthole reveal, §6.9) — the hero is not a separate banner, it
is the chart arriving. After the chart: the general synopsis strip (§6.18),
the station cards (§6.15), the conversion section (§6.16), and the footer
(§6.17), all set as vertical "inshore waters" annexes on the same paper,
with isobar hairline rules between them. The vertical acts reuse the chart's
grid as their background ruling at 40% opacity — the paper never changes,
only the act does.

**Spacing rhythm.** Base unit 8px. Chart furniture uses the chart's own
module: area padding = 1 grid cell (160 SVG units ≈ 10vw at desktop).
Vertical acts use a 62ch mono measure for bulletin-adjacent copy — the width
of a typed bulletin page — and section padding of 96px top / 96px bottom at
desktop, 56px at mobile. Whitespace on the chart is *sea room*: areas are
never crowded to their boundaries; a boundary must keep 24 SVG units of
clear water from any name or station dot, because on a real chart, clutter
at a boundary is where readings get misread.

**Density rules.** One pressure system per viewport-width of chart, maximum.
Two fronts may share a viewport; three may not — if the content's geography
demands it, the chart widens (areas get more sea room) rather than the marks
getting denser. The broadcast column shows exactly one area's forecast: the
instant two areas' bulletins are visible, the radio metaphor is broken.

---

## 5. Full motion system

Every motion term, in this theme's own language. The governing metaphor:
**nothing on a chart moves like a website; it moves like weather, water, and
a typewriter.** Motion is either the weather (slow, ambient, physical) or the
broadcast (typed, stepped, exact) — never bouncy, never elastic, never
"playful".

**Named easings (the theme's only curves):**
- `--ease-swell: cubic-bezier(0.22, 0.61, 0.21, 1)` — the long ease of a
  swell rising and settling; used for travel, fills, blooms.
- `--ease-settle: cubic-bezier(0.16, 0.84, 0.30, 1)` — a thing coming to rest
  on the chart table; used for entrances and the porthole.
- `--ease-front: linear` — fronts march at constant speed; weather does not
  ease.
- `--ease-tick: steps(1)` within odometer rolls — digits change in steps,
  never blur (see §6.6).
- Typing is not eased: 45ms per character, fixed, like a teleprinter (§6.3).

**Global motion laws.**
1. **One rAF loop.** All scroll-scrubbed values (pan, needle, isobar scrub,
   breathing phase, front offsets) are written by a single
   requestAnimationFrame loop with lerp smoothing: `current += (target −
   current) × 0.12` for the pan, `0.18` for the needle. No scroll handler
   writes styles directly.
2. **The 1.2s fallback.** Every animated reveal arms a 1.2s timer: if the
   animation has not completed (JS stalled, observer never fired, tab
   backgrounded), the element is set to its final state. No content may be
   invisible after 1.2s for any reason. This is the source entry's standing
   rule, enforced per element in §6.
3. **Scrubbed, not triggered, for travel.** Anything tied to the passage is a
   continuous function of scroll progress — reversing scroll reverses the
   weather. One-shot triggered animations are reserved for entrances and
   clicks.
4. **Ambient motion is subliminal.** Breathing is ±2px over 9s; mist drift is
   0.4% opacity moving 12px over 40s. If a visitor *notices* the ambient
   layer as an animation, it is too strong (§9).

**The motion vocabulary, term by term:**

| Term | This theme's implementation | Duration / easing | Trigger |
|---|---|---|---|
| Scroll-triggered reveals | In vertical acts: sections surface like a front arriving — a hairline rule draws across (400ms), then copy fades/rises 8px (600ms `--ease-settle`), staggered 90ms per block | 600ms settle | IntersectionObserver at 25% visible |
| Parallax | Three chart layers: grid slowest (pan × 0.92), isobars mid (pan × 1.0), area names fastest (pan × 1.06) — weather over paper over lettering | scrubbed, lerp 0.12 | Scroll |
| Pinned scenes | The broadcast column is pinned for the whole passage; the hero's pressure systems pin for the first 120vh while the chart settles around them | passage length | Scroll |
| Masked line reveals | Headlines in vertical acts are revealed line-by-line under a paper mask (clip-path inset from bottom), one line per 140ms, like lines appearing on a typed bulletin | 140ms/line, settle | Section entry |
| Blur-to-sharp reveals | **Refused as a headline device** — a chart is never out of focus. Used once, physically: the porthole reveal (§6.9) starts with the chart's grain layer blurred 6px sharpening to 0 as the porthole opens — it reads as condensation clearing from glass, not as a focus effect | 900ms, inside §6.9 | Load |
| Animated counters | Station readings roll odometer-style (§6.6); areas-covered counts in whole areas only (n/31), stepping at area boundaries | 800ms rolls | Scroll entry / area change |
| Progress indicators | Compass-needle progress (§6.8) + "AREAS COVERED n/31" — orientation and count, never a bar | scrubbed | Scroll |
| Marquees | **Refused.** Nothing on a chart scrolls sideways on its own; the only lateral motion is the visitor's own travel. A "latest warnings" ticker would be a television, not a radio bulletin | — | — |
| Ambient loops | Pressure breathing (9s), mist drift (40s), marching fronts (~20s per traverse) — §6.4, §6.5 | loops as stated | Time, always on (paused off-screen) |
| Micro-interactions | Area-fill hover (250ms), buoy-bell ping (700ms), card tilt 1° (300ms), link underlines draw as hairlines (200ms) | as stated | Hover / click / focus |
| Hover physics | Chart cards tilt a maximum of 1° toward the pointer with `--ease-swell` and a 300ms return — a chart table in a swell, not a toy. No magnetic pull, no scale-up | 300ms | Pointer position |
| Page transitions | Static-tune: 120ms of broadcast static (paper-grain noise burst), then the destination area tunes in centred (§6.12) | 120ms + 400ms settle | Route change |
| Image treatments | Coastal photographs sit inside chart-grid frames and scale-in-frame 1.06→1.0 (900ms `--ease-settle`) with a duotone wash (ink/paper) at 12% that lifts on hover — photographs pinned to the chart, weathered by it | 900ms | Scroll entry |
| Kinetic typography | The typing broadcast column (§6.3) and the IMMINENT letterspacing pulse (§6.7) are the theme's only kinetic type. Headlines never move | per element | Area change / gale |
| Scroll-driven (scrub) animation | Isobars redraw scrubbed as fronts advance with depth: each front's symbol train advances along its path proportional to passage progress, in addition to its ambient march | scrubbed | Scroll |

**Reduced-motion global ruling.** With `prefers-reduced-motion`: the passage
is abolished. The chart becomes a vertical stack of the 31 areas (§6.2's
variant), each printed in full with its forecast beneath it; typing becomes
instant text; rolls become set values; breathing, marching, mist, and the
porthole are all rendered in their final state. Nothing is "slowed down" —
the theme changes medium, from broadcast to printed bulletin. This is the
source entry's standing rule and it is a blocking gate in §10.

---

## 6. Signature elements

Each element carries its v1 build spec and its v2 deepening layers
(choreography timeline · state matrix · breakpoints · edge cases ·
accessibility · tokens). Elements 6.1–6.12 are the source entry's signature
elements, deepened. Elements 6.13–6.18 are the page-family elements.

---

### 6.1 Self-drawing isobars

- **What & why.** On load, the isobar curves draw themselves around the
  headline in SVG, and the L/H pressure centres bloom at their hearts. The
  chart's weather draws itself around the chart's title — the first thing
  the visitor learns is that on this page, marks are measurements.
- **Structure.** One inline `<svg class="chart-field">` per chart act. Each
  pressure system is a `<g class="system" data-kind="low|high">` holding 3–6
  concentric `<path class="isobar">` (smooth closed curves, `pathLength=100`
  normalised) and a `<text class="system-mark">` (L or H + pressure value,
  mono 500). Draw via `stroke-dasharray: 100; stroke-dashoffset: 100 → 0`.
- **Motion spec.** Draw: 1200ms per ring, `--ease-settle`, staggered 110ms
  per ring outward from the centre, systems staggered 250ms apart in
  west-to-east chart order. Bloom: centre mark scales 0.9→1 and fades 0→1
  over 600ms `--ease-swell`, starting when its innermost ring is 60% drawn.
  Trigger: load (hero) / first entry into the passage.
- **States.** *Rest:* fully drawn chart (the drawn state is the resting
  state — the animation is a birth, not a loop). *Hover:* none (isobars are
  not interactive; hover lives on areas, §6.10). *Scrolled-past:* drawn,
  breathing (§6.5) only.
- **Content merge.** The isobars ring the headline the way a real low sits
  over the Atlantic approaches: the headline is *inside* the weather system
  it announces. Remove the headline and the rings still describe a real
  pressure field from the page's data.
- **Failure fallback.** Base CSS renders all rings fully drawn
  (`stroke-dashoffset: 0`); JS adds the draw state only after measuring
  `pathLength` support, and the global 1.2s fallback (§5) forces the final
  state. No-JS = a finished chart.
- **Reduced-motion variant.** Rings appear drawn; bloom is instant.
- **Performance budget & mobile variant.** ≤ 24 isobar paths per chart act;
  dashoffset animation is compositor-cheap (stroke, no layout). Mobile:
  systems keep 3 rings maximum (outer rings are dropped, not shrunk), draw
  time 900ms.

**V2 — Choreography timeline** (t=0 = chart act initialised):
| Beat | Time | Event |
|---|---|---|
| 1 | 0ms | Grid + boundaries fade in at final state (they are paper, not weather — they do not draw) |
| 2 | 150ms | First system's innermost ring begins drawing |
| 3 | 150–1350ms | Rings draw outward, 110ms stagger |
| 4 | ~870ms | Centre mark blooms (innermost ring at 60%) |
| 5 | 400ms steps | Remaining systems begin, 250ms apart, west to east |
| 6 | ≤2400ms | All systems complete; breathing (§6.5) takes over the same paths |

**V2 — State matrix.**
| State | Desktop | Touch |
|---|---|---|
| Rest | Drawn, breathing | Drawn, breathing |
| Hover | n/a — paths are `pointer-events: none` by design | n/a |
| Focus | n/a — never focusable; the chart's data is reachable via §6.18's index | n/a |
| Active | n/a | n/a |
| Scrolled-past | Drawn; breathing pauses when off-screen (IO) | Same |
| Disabled | n/a — decorative-data layer; if chart data fails to load, §6.12's skeleton holds instead | Same |

**V2 — Breakpoints.** ≥1200px: full ring counts (3–6 per system). 768–1199px:
max 4 rings per system; stagger 90ms. <768px: max 3 rings; systems drawn in
centred-area order rather than west-to-east (the visitor's area is the
weather that matters first); total draw ≤1500ms.

**V2 — Edge cases.** *Slow network:* the chart is inline SVG — no fetch, so
the draw begins regardless; webfont delay must not block it (text uses
`font-display: swap`, marks may bloom in fallback mono for one frame —
acceptable, it reads as a retune). *No SVG stroke support* (legacy): paths
render filled-state via the base CSS. *Content longer than expected:* a 5th
pressure system is permitted only if §4's density rule holds (one system per
viewport width); otherwise the data's weakest system is drawn as a single
ring + centre mark. *Scroll back up:* the draw never replays; re-entry shows
the finished chart (weather does not un-happen).

**V2 — Accessibility.** The whole SVG is `role="img"` with an `aria-label`
naming the systems and extremes ("Low, 984 hectopascals, west of Rockall;
High, 1031, over the Forties"). Decorative duplicate paths are
`aria-hidden`. Contrast: isobar strokes are `--ink-hairline` (≥3:1 on
`--paper`) — they are data graphics, held to the graphics contrast floor;
centre marks are full `--ink` (10.9:1). The draw animation is disabled under
reduced motion (above), so no vestibular trigger exists in the final state.

**V2 — Tokens consumed.** `--ink`, `--ink-hairline`, `--paper`,
`--ease-settle`, `--ease-swell`, `--draw-ring: 1200ms`,
`--draw-stagger: 110ms`, `--bloom: 600ms`.

---

### 6.2 Horizontal chart travel

- **What & why.** The passage: vertical scroll is converted into lateral
  travel across the wide chart, sea area by sea area, in broadcast order.
  Travelling *is* reading — the site's geography and its table of contents
  are the same object.
- **Structure.** `<section class="passage">` with height set by JS to
  `31 × 38vh` (fallback CSS `height: 1180vh`). Inside, a `position: sticky;
  top: 0; height: 100vh` stage holding the chart SVG in a
  `<div class="chart-pan">` (transform: translateX) and the pinned broadcast
  column (§6.3). Progress `p = scrollY_within_passage / passage_height`;
  `panX = −p × (chartWidth − stageWidth)`, lerped at 0.12 in the shared rAF
  loop. The "current area" is the area whose centroid is nearest the stage's
  centre line (computed left of the broadcast column at ≥1200px).
- **Motion spec.** Continuous scrub — no easing curve on the mapping itself;
  smoothness comes only from the lerp. Area changes fire when the centred
  area changes (hysteresis: the centroid must pass centre by 24px before the
  change commits, so hovering at a boundary never flickers the broadcast).
- **States.** *Rest (top):* Viking centred. *Travelling:* pan lerps toward
  target. *End:* Southeast Iceland centred; the stage un-stickies into the
  synopsis act. *Scrolled-past:* final area held.
- **Content merge.** The areas are the sections: each area's polygon contains
  its content anchor (headline stat, link, or image), so the pan is the
  visitor reading the site's actual content in geographic order.
- **Failure fallback.** If JS is absent or the sticky stage fails, the chart
  renders as a static full-width chart at its natural aspect with all areas
  labelled, followed by the areas' content as a vertical list (the same DOM,
  CSS-only reflow: `.passage` becomes `height: auto`, stage static, pan
  transform none, chart scaled to fit width, content list visible). The 1.2s
  rule applies to the stage's initialisation.
- **Reduced-motion variant.** The vertical stack (see §5): no sticky, no
  pan; areas print one per block in broadcast order with forecasts beneath.
- **Performance budget & mobile variant.** Pan writes one transform per
  frame; the SVG is composited as a single layer (will-change on the pan
  wrapper only, removed at passage end). Mobile: the passage shortens to
  `31 × 30vh`, pan distance is the same chart (areas are wider relative to
  the screen, so each area gets more dwell); the broadcast column becomes a
  bottom sheet (§6.3 breakpoints).

**V2 — Choreography timeline** (per area crossing, scrubbed — times are
scroll-relative, stated at a reference scroll speed of 100vh/s):
| Beat | Event |
|---|---|
| 1 | Area's leading boundary crosses stage centre −25% — its name begins full-ink fade from 60% |
| 2 | Centroid crosses centre +24px hysteresis — area commits: broadcast retypes (§6.3), needle swings (§6.8), readings roll (§6.6) |
| 3 | Centroid at centre — area name at full ink; area's content anchor is the stage's focus |
| 4 | Centroid passes centre +25% — name returns to 60% ink; next area's beat 1 begins |

**V2 — State matrix.**
| State | Desktop | Touch |
|---|---|---|
| Rest | Viking centred, column typing first forecast | Same; bottom sheet shows Viking |
| Hover | Areas highlight per §6.10 (pan continues) | No hover — tap = §6.11 ping + area commit if tapped area is ≥50% visible |
| Focus | Keyboard: the passage is reachable by Tab via §6.18's index links, which scroll the passage to the named area (scroll-driven, 600ms programmatic scroll) | Same via index |
| Active (scrolling) | Lerp chase at 0.12; fronts scrub-advance | Same; lerp 0.14 (shorter chase reads as responsiveness on small screens) |
| Scrolled-past | Final area held; stage released | Same |
| Disabled | If `IntersectionObserver`/sticky unsupported → static fallback (above) | Same |

**V2 — Breakpoints.** ≥1200px: column right, centre computed in remaining
width; passage 1180vh. 768–1199px: column narrows to 272px (§6.3);
passage 1050vh. <768px: column becomes a 168px bottom sheet; the chart stage
is the top ~62vh; passage 930vh (30vh per area); area names 30–44px.

**V2 — Edge cases.** *Fast scroll to bottom:* the lerp chase must not take
>900ms to settle after scroll stops; if `|target − current|` exceeds two
areas' width, the loop snaps to within two areas instantly, then lerps —
the visitor never watches the chart "catch up" across the whole ocean.
*Scroll back up:* fully symmetric — areas un-commit in reverse, the
broadcast retypes the earlier area (this is correct: the radio reports where
you are). *Resize mid-passage:* pan range recomputed on the next frame;
current area preserved by re-deriving scroll position from the committed
area, not from pixels. *Content shorter than 31 areas:* the passage height
formula uses the real area count `n` everywhere (`n/31` in the source copy
becomes `n/N` — see §12: the count printed is always the true count).
*Low-power device:* if the rAF loop measures <40fps sustained for 2s, the
pan lerp rises to 0.3 (less smooth, less work) and ambient layers pause
(§6.4/§6.5) — travel itself is never removed.

**V2 — Accessibility.** The passage is a scroll region, not a keyboard trap:
no keyboard interaction is required to traverse it. Screen-reader users get
the same content from §6.18's area index (a semantic list, each item linking
to the area's content anchor in the vertical annex) and from the broadcast
column's DOM text, which is always the *committed* area's full forecast —
never a half-typed string (§6.3 a11y). `aria-live` is OFF for the column
(it would announce 31 forecasts); instead the column is a labelled region
("Forecast for the area in view") whose text updates silently. Focus is
never moved by scrolling. Touch targets: area polygons are not targets;
their content anchors are real links/buttons ≥44px.

**V2 — Tokens consumed.** `--paper`, `--ink`, `--lerp-pan: 0.12`,
`--area-dwell: 38vh`, `--hysteresis: 24px`, `--stage-h: 100vh`.

---

### 6.3 Live broadcast column

- **What & why.** A mono column pinned at the right that types the forecast
  for whichever area is currently centred — "FORTIES. SOUTHWESTERLY 5 OR 6.
  RAIN LATER. MODERATE." Map and bulletin are the same report in two media;
  the column is the radio that reads the chart aloud.
- **Structure.** `<aside class="broadcast" aria-label="Forecast for the area
  in view">` containing: area name (`<h3>`, Fraunces), the bulletin
  paragraph (`<p class="bulletin">`), a readings list (§6.6), and the gale
  slot (§6.7). The full forecast text for every area lives in the DOM from
  first render (one hidden template per area, or a `data-forecast`
  attribute set) — typing is a reveal of real text, never generated text.
- **Motion spec.** On area commit: the old bulletin clears in 90ms (a single
  fade — typewriters do not backspace poetically), then the new bulletin
  types at 45ms/char, mono, with the area name first, a 300ms pause after
  the area name's full stop (the reader's breath), then wind/weather/sea/
  visibility in grammar order (§12). A block cursor (▌ in `--ink`, 530ms
  blink) rides the typing head and parks at the end, blinking twice, then
  rests solid for 2s and disappears.
- **States.** *Rest:* current area's full bulletin typed out. *Retyping:*
  during a crossing (≤ ~1.6s for the longest bulletin). *Gale:* the gale
  slot activates (§6.7). *Scrolled-past (beyond passage):* the column
  un-pins and its final area's bulletin remains as the last word before the
  synopsis.
- **Content merge.** The column is not a caption for the chart; it is the
  chart's content in its second, canonical form. Every number it types is
  the number printed at that area's station on the chart (§6.6) — the two
  can never disagree, because both render from one data object per area.
- **Failure fallback.** If JS fails, the column shows the first area's
  complete bulletin statically, and every area's forecast is printed in its
  vertical annex (§6.2 fallback) — no forecast exists only inside the
  typing effect. If the typing loop is interrupted (rapid area changes),
  the newest area wins and typing restarts from its name — never a queue.
- **Reduced-motion variant.** Bulletin swaps instantly, complete, no cursor.
- **Performance budget & mobile variant.** Typing is one `setInterval`-free
  rAF-driven counter writing `textContent` slices — ≤ 1 DOM write per frame,
  longest bulletin ~180 chars ≈ 8 DOM writes/s at 45ms/char... (one write
  per character tick, ~22 writes/s, trivial). Mobile: the column becomes a
  bottom sheet (see breakpoints) showing area name + bulletin only;
  readings move into the sheet's expandable second line.

**V2 — Choreography timeline** (t=0 = area commit from §6.2):
| Beat | Time | Event |
|---|---|---|
| 1 | 0ms | Previous bulletin begins 90ms fade |
| 2 | 90ms | Area name (Fraunces) swaps instantly — names are lettering, they do not type |
| 3 | 120ms | Bulletin clears; block cursor appears at line start |
| 4 | 120ms + 45ms/char | Area name line types ("FORTIES.") |
| 5 | +300ms pause | The reader's breath after the name |
| 6 | resumes 45ms/char | Wind, weather, sea state, visibility type in grammar order |
| 7 | last char +0ms | Readings roll (§6.6); gale slot checks (§6.7) |
| 8 | +1060ms | Cursor blinks twice (2 × 530ms), rests solid 2s, disappears |

**V2 — State matrix.**
| State | Desktop | Touch |
|---|---|---|
| Rest | Full bulletin, cursor gone | Full bulletin in bottom sheet |
| Hover | Column is inert to hover (it is an instrument, not a card) | n/a |
| Focus | Column contains the area's content link ("Full report for Forties →") — focus ring is a 2px `--ink` outline offset 2px; focusing it does not change the bulletin | Same |
| Active (retyping) | Per timeline | Same; sheet height animates 200ms `--ease-swell` if the new bulletin wraps longer |
| Scrolled-past | Un-pinned, final bulletin static | Sheet docks as a static block above the synopsis |
| Disabled | Data failure → §6.12 skeleton state; column shows "FORECAST UNAVAILABLE. SEE AREA INDEX." in voice (§12) | Same |

**V2 — Breakpoints.** ≥1200px: 320px right column, full readings list.
768–1199px: 272px; readings compress to two lines (wind + pressure; sea
state and visibility fold into the bulletin only). <768px: bottom sheet
168px tall (name 22px Fraunces + bulletin 13.5px, max 4 lines, readings
hidden — they remain on the chart at their stations and in the annex).

**V2 — Edge cases.** *Rapid crossings* (fast scroll through 4 areas in 1s):
typing is cancelled per area, never queued; if commits arrive faster than
one per 400ms, the column waits for a 400ms quiet period, then types only
the final area — intermediate areas flash their names only. *Very long
bulletin* (>200 chars): type rate tightens to 38ms/char so total retype
stays ≤1.9s; grammar is never truncated. *Scroll back up:* retypes the
earlier area in full (the radio reports where you are, not where you were
going). *Tab hidden mid-type:* typing pauses with the rAF loop and resumes;
the 1.2s fallback does not apply mid-type (the text is a reveal of DOM
content, and the completed state is guaranteed by the pause-resume, plus a
5s hard timer that snaps any bulletin to complete).

**V2 — Accessibility.** The visible typing is a visual effect over complete
DOM text: each area's full bulletin is present in a visually-hidden
`<template>`-equivalent (a `hidden` list in the annex) so assistive tech
reads finished sentences, never partial strings. The column region is
labelled; updates are `aria-live="off"`. The block cursor is `aria-hidden`
decoration. Contrast: bulletin mono `--ink` on `--paper-deep` = 10.2:1.
Focus order: the column's single link sits after the chart in DOM order,
matching the visual reading order (chart, then its reading).

**V2 — Tokens consumed.** `--paper-deep`, `--ink`, `--gale`, `--buoy`
(gale slot only), `--type-char: 45ms`, `--type-breath: 300ms`,
`--cursor-blink: 530ms`, `--ease-swell`.

---

### 6.4 Marching fronts

- **What & why.** Cold-front triangles and warm-front semicircles march
  continuously along their front lines — the chart's own weather symbols
  moving the way fronts move: along their lines, in the direction they
  point. It is the chart's slowest, most physical ambient motion.
- **Structure.** Each front is an SVG `<path class="front-line">` (the line
  itself, `--ink-hairline`) plus a `<g class="front-symbols">` of symbol
  instances (triangles for cold, semicircles for warm, alternating both for
  occluded) placed with `offset-path: path(...)` where supported, or
  positioned by the shared rAF loop via `getPointAtLength` as the fallback
  engine. Symbols: cold = filled triangles in `--ink`; warm = filled
  semicircles in `--buoy`; 14px along the line, spaced 90 SVG units.
- **Motion spec.** Ambient march: each front's symbol train advances at a
  constant `--ease-front: linear` rate — one full traverse of its line in
  ~20s, offset per front so no two fronts are in phase. Scrub advance: the
  train also advances proportionally to passage progress (the fronts move
  *with* the visitor's depth — the weather is later in the day at the far
  side of the chart): scrub contributes up to 30% of a traverse across the
  whole passage, added to the ambient offset.
- **States.** *Rest:* marching. *Hover:* none (fronts are not interactive).
  *Scrolled-past / off-screen:* paused by IntersectionObserver. *Gale area
  centred:* the front nearest the gale area does not speed up — fronts do
  not hurry; the warning lives in §6.7, not here.
- **Content merge.** The symbols are the front: remove them and the line is
  an unlabelled curve; with them, any mariner can read which way the weather
  is going. The march direction is always the meteorological direction of
  travel from the page's data — never reversed for effect.
- **Failure fallback.** Static symbols at evenly spaced intervals (the
  printed-chart state) — which is exactly what a real chart looks like.
  No-JS = the printed state.
- **Reduced-motion variant.** Static printed state; scrub advance also
  removed (the stack has no passage to scrub).
- **Performance budget & mobile variant.** ≤ 4 fronts per chart act, ≤ 60
  symbols total; the rAF fallback engine samples `getPointAtLength` only for
  symbols in the current viewport window (±1 viewport), the rest hold
  position. Mobile: symbol spacing widens to 120 units (fewer, larger
  symbols), traverse 26s.

**V2 — Choreography timeline** (ambient, per front):
| Beat | Time | Event |
|---|---|---|
| 1 | 0s | Symbols at data-defined start offsets |
| 2 | continuous | Train advances 1 line-length per 20s, linear, wrapping: a symbol leaving the line's end re-enters at its start (fronts are long; the line is a segment of a longer weather system) |
| 3 | on area commit | Scrub offset eases to its new progress value over 600ms `--ease-swell` (added to, never replacing, the ambient offset) |
| 4 | off-screen | March freezes mid-step; resumes from the same offset (no jump) |

**V2 — State matrix.**
| State | Desktop | Touch |
|---|---|---|
| Rest | Marching + scrub | Marching + scrub |
| Hover | n/a | n/a |
| Focus | n/a — fronts are `aria-hidden` data graphics; their information (front type, direction) is in §6.18's synopsis text | n/a |
| Active | n/a | n/a |
| Scrolled-past | Paused off-screen | Paused off-screen |
| Disabled | `offset-path` and rAF both unavailable → printed state | Same |

**V2 — Breakpoints.** ≥1200px: as spec. 768–1199px: ≤3 fronts animated; a
4th front prints statically. <768px: ≤2 fronts animated (the two nearest the
centred area); others print; spacing 120 units.

**V2 — Edge cases.** *Low-power mode* (§6.2's <40fps ruling): fronts are
the first ambient layer cut — they print statically while travel and typing
continue. *Front line shorter than one spacing:* a single symbol sits at the
line's midpoint, static (a front too short to march is a trough line, and
the data should say so). *Content change* (data refresh): symbols re-seed
from the new line geometry in one frame, no transition — weather data does
not animate between editions. *Scroll back up:* scrub offset decreases
symmetrically; ambient march never reverses.

**V2 — Accessibility.** Purely decorative-data: `aria-hidden="true"` on the
symbol layer; the front's meaning is carried in text by the synopsis (§6.18)
and each area's bulletin (weather words imply the front). No contrast
requirement beyond the line's ≥3:1 graphics floor. Motion is ambient-slow
(max symbol speed ≈ 0.05 line-lengths/s) and fully removed under reduced
motion.

**V2 — Tokens consumed.** `--ink`, `--buoy`, `--ink-hairline`,
`--ease-front`, `--front-traverse: 20s`, `--front-spacing: 90u`,
`--front-scrub-share: 30%`.

---

### 6.5 Pressure breathing

- **What & why.** The isobar hairlines undulate almost imperceptibly — path
  morphs of ±2px on a 9s ease-in-out loop — and the chart's grain drifts
  like sea mist. The weather system is alive on its paper; the chart is not
  a photograph of weather, it is weather, resting.
- **Structure.** Each isobar path carries a precomputed alternate `d`
  (generated at build time by offsetting control points ±2px
  perpendicular), and the loop interpolates between the two `d` values with
  a sine phase per system (offset so systems never breathe in unison). The
  mist is a single full-chart `<div class="mist">` with a repeating
  paper-grain background, translating 12px over 40s at 0.4% effective visual
  weight (opacity 0.05, `--ink` grain on `--paper`).
- **Motion spec.** Breathing: 9s sine loop, amplitude ±2px at desktop scale,
  phase-offset per system by its index × 1.7s. Mist: 40s linear drift,
  wrapping seamlessly. Both pause when the chart is off-screen and both are
  the first things cut in low-power mode.
- **States.** *Rest:* breathing. *Hover/focus/active:* unaffected (the
  weather does not respond to being watched). *Scrolled-past:* paused.
- **Content merge.** The breathing is *in* the printed lines — the isobars
  themselves flex as pressure flexes. It is not a glow, a shadow, or a
  particle layer laid over the chart; remove it and the chart is the same
  chart on a still day.
- **Failure fallback.** Static `d` (the mean path). If path interpolation is
  unavailable, the loop is skipped entirely — a stepped morph would read as
  a glitch, and this theme does not glitch.
- **Reduced-motion variant.** Mean path, no mist. (Non-negotiable: ambient
  loops are the first casualty of reduced motion, always.)
- **Performance budget & mobile variant.** Path interpolation ≤ 24 paths;
  cost is one attribute write per path per frame — capped by updating at
  30fps (every other frame) since 9s sine motion is indistinguishable at
  30fps. Mobile: amplitude ±1.2px, mist removed (grain alone, static).

**V2 — Choreography timeline:**
| Beat | Time | Event |
|---|---|---|
| 1 | Draw complete (§6.1 beat 6) | Breathing fades in over 2s from the mean path — the system "starts" breathing only once it exists |
| 2 | continuous | Sine loop, 9s period, per-system phase |
| 3 | Area commit | No change — breathing is global weather, not local UI |
| 4 | Off-screen / low-power / reduced-motion | Amplitude lerps to 0 over 600ms (never a hard cut — a held breath, released) |

**V2 — State matrix.**
| State | Desktop | Touch |
|---|---|---|
| Rest | Breathing + mist | Breathing (reduced amplitude), no mist |
| Hover / Focus / Active | n/a — non-interactive layer | n/a |
| Scrolled-past | Paused | Paused |
| Disabled | Static mean paths (the printed chart) | Same |

**V2 — Breakpoints.** ≥1200px: ±2px, mist on. 768–1199px: ±1.6px, mist on
at 0.03 opacity. <768px: ±1.2px, mist off.

**V2 — Edge cases.** *Amplitude vs. legibility:* isobars that ring a station
dot never breathe across the dot — paths whose morph would move a stroke
within 6px of a station or a name are amplitude-clamped to ±0.8px at build
time. *Very long pages:* the vertical acts' hairline rules do not breathe —
breathing belongs to the chart's weather only; annex rules are paper.
*Data refresh:* new mean paths replace old in one frame; breathing phase
restarts (a new edition of the chart).

**V2 — Accessibility.** `aria-hidden` layer; amplitude and speed are far
below vestibular-risk thresholds, and the layer is fully removed under
reduced motion. No information is carried by the breathing (pressure values
are printed at the centres, §6.1).

**V2 — Tokens consumed.** `--ink`, `--paper`, `--breathe-amp: 2px`,
`--breathe-period: 9s`, `--mist-drift: 40s`, `--mist-opacity: 0.05`.

---

### 6.6 Rolling station readings

- **What & why.** Wind speeds, pressures, and visibilities roll to their
  readings — odometer-style digit rolls, 800ms — as each station area
  arrives. The numbers are the areas' actual observations, printed on the
  chart at their stations and repeated in the broadcast column (§6.3); the
  roll is the instrument settling on the value.
- **Structure.** Each reading is a `<span class="reading" data-value="1013"
  data-unit="HPA">` containing per-digit `<span class="digit">` columns,
  each column a vertical strip of 0–9 translated by the roll. On the chart,
  readings sit at station dots (small mono labels: station name + pressure).
  In the column, the current area's readings list: WIND (direction + force),
  PRESSURE (hPa + tendency word: RISING / FALLING / STEADY), SEA STATE,
  VISIBILITY.
- **Motion spec.** On area commit: each digit column rolls from its current
  digit to the target digit over 800ms with `--ease-tick` stepping (the
  strip moves in discrete digit steps at 80ms per step, decelerating —
  a mechanical counter, not a slot machine: maximum 10 steps, shortest path
  direction per column, never a full spin for effect). Stagger: pressure
  first (it is the chart's primary number), then wind force, then sea state
  word (which crossfades — words do not roll), then visibility, 90ms apart.
- **States.** *Rest:* readings at value. *Rolling:* during the 800ms after
  commit. *Stale:* if data is older than the current edition (§12's
  edition law), readings gain a `--gale` suffix " (EARLIER)" — staleness is
  printed, never hidden.
- **Content merge.** The roll happens *at the station on the chart* and in
  the column simultaneously, from the same data object (§6.3) — the
  instrument and its reading are one thing in two places.
- **Failure fallback.** Values are the text content from first render; the
  roll is a JS enhancement over printed numbers. No-JS = correct numbers,
  no roll.
- **Reduced-motion variant.** Values swap instantly at commit.
- **Performance budget & mobile variant.** ≤ 4 readings per area roll at
  once; digit strips are transform-only. Mobile: chart station labels show
  pressure only (wind lives in the column/sheet); rolls shorten to 600ms.

**V2 — Choreography timeline** (t=0 = area commit):
| Beat | Time | Event |
|---|---|---|
| 1 | 0ms | Pressure digits begin rolling |
| 2 | 90ms | Wind force digit rolls; direction word crossfades (120ms) |
| 3 | 180ms | Sea state word crossfades; tendency word follows pressure at its landing |
| 4 | 270ms | Visibility word crossfades |
| 5 | 800ms | All rolls landed; readings are the area's printed truth |

**V2 — State matrix.**
| State | Desktop | Touch |
|---|---|---|
| Rest | Values printed | Values printed |
| Hover | A station label on the chart underlines its twin in the column (hairline draw, 200ms) — chart and column answer together (cf. §6.10) | Tap station = same underline + the bottom sheet rises to that area |
| Focus | Readings are text — focusable only as part of their area link (§6.18 index) | Same |
| Active (rolling) | Per timeline | Per timeline, 600ms |
| Scrolled-past | Last committed area's values hold | Same |
| Disabled | Data missing for one reading → that reading prints "—" and the word NO REPORT in the column (§12 error voice); others unaffected | Same |

**V2 — Breakpoints.** ≥1200px: full readings list in column + station
labels with pressure + wind on chart. 768–1199px: column shows pressure +
wind; chart labels pressure only. <768px: chart labels pressure only;
column/sheet shows the bulletin (readings are inside its grammar).

**V2 — Edge cases.** *Equal values* (new area, same pressure): no roll —
the instrument does not perform for a non-change; only the tendency word
may change. *Extreme values* (pressure <950 or >1050): the roll takes the
long path if the short path would pass through a value the station never
reported... no — simpler and truer: rolls always take the shortest path;
extremes are just digits. *Long station names:* labels truncate with a
hairline leader to the name in the annex, never shrink below 11.5px.
*Scroll back up:* readings roll *back* to the earlier area's values —
instruments report where you are.

**V2 — Accessibility.** Rolling digits are a visual layer over a static
text value: the accessible name of each reading is its final value, exposed
via `aria-label` on the reading and a visually-hidden static twin; the
animated digit strips are `aria-hidden`. A screen reader never hears a
half-rolled number. Contrast: readings are `--ink` mono 500 (10.9:1);
tendency words in `--gale` at 12px uppercase minimum (4.6:1, large-text
floor met by weight + tracking per §3).

**V2 — Tokens consumed.** `--ink`, `--gale`, `--ease-tick`,
`--roll: 800ms`, `--roll-step: 80ms`, `--roll-stagger: 90ms`.

---

### 6.7 "IMMINENT" letterspacing pulse

- **What & why.** When a gale area is in view, its gale word — IMMINENT —
  pulses its letterspacing (0 → 0.12em → 0, 1.8s loop) in the broadcast
  column and on the chart label. The warning shouts in the forecast text
  itself, only while its area is on screen. In the real bulletin, gale
  warnings carry a timing word: *imminent* (within 6 hours), *soon* (6–12),
  *later* (beyond 12). Only IMMINENT pulses; SOON and LATER print still —
  the pulse is rationed by the same grammar that rations the word.
- **Structure.** `<span class="gale-word" data-timing="imminent">IMMINENT</
  span>` inside the bulletin's gale line, and a twin `<text>` label at the
  area's chart marker. Both are driven by one CSS animation toggled by a
  class on the passage root (`data-gale-area`), so the two instances can
  never drift out of sync.
- **Motion spec.** Letterspacing 0 → 0.12em → 0 over 1800ms, sine-in-out,
  infinite while the gale area is committed. Colour: `--buoy` in the column
  (it is the one red word allowed in the bulletin), `--ink` on the chart
  label with a `--buoy` underline rule (the chart's labels stay ink; the
  red is a rule beneath, like a chart correction in red pencil).
- **States.** *Rest (non-gale area):* no gale line at all — the slot is
  absent, not empty. *Gale area committed:* pulse runs. *Scrolled away:*
  pulse stops mid-beat (class removed; letterspacing returns to 0 over
  200ms, never snaps). *Two gale areas adjacent:* each pulses only while
  its own area is committed.
- **Content merge.** The pulse is applied to the warning word in the actual
  forecast sentence — it is emphasis inside the content, not a badge pasted
  beside it. Remove the animation and the sentence still warns.
- **Failure fallback.** Static IMMINENT in `--buoy`: a printed gale warning
  is still a gale warning.
- **Reduced-motion variant.** Static `--buoy` word, letterspacing fixed at
  0.06em (the emphasis survives as typography, not motion).
- **Performance budget & mobile variant.** One CSS animation, two nodes.
  Mobile: identical (the word is in the bottom sheet's bulletin).

**V2 — Choreography timeline:**
| Beat | Time | Event |
|---|---|---|
| 1 | Area commit +0ms | Gale line is present in the typed bulletin from its first character (the warning types with the forecast — it is never added after) |
| 2 | Typing complete | Pulse class applied; letterspacing begins from 0 |
| 3 | 1800ms loop | 0 → 0.12em → 0, sine |
| 4 | Area un-commits | Class removed; 200ms return to 0 |

**V2 — State matrix.**
| State | Desktop | Touch |
|---|---|---|
| Rest | No gale line (non-gale area) | Same |
| Hover | n/a — the word is text inside the bulletin | n/a |
| Focus | n/a | n/a |
| Active (gale area in view) | Pulsing in column + chart label | Pulsing in sheet + chart label |
| Scrolled-past | Stopped, letterspacing 0 | Same |
| Disabled | Static red word (no-JS / reduced motion) | Same |

**V2 — Breakpoints.** Identical at all sizes; on <768px the chart-label
twin is dropped (the sheet's bulletin carries the warning; two pulsing
words on a small screen is alarm, not emphasis).

**V2 — Edge cases.** *Gale wording variants:* the data may carry SOON or
LATER — printed `--ink`, no pulse, no red (red follows the pulse's ration).
*Multiple warnings in one area* (gale + fog): fog is a visibility word, it
never pulses; only the gale timing word does. *Data marks a gale but the
area is never centred* (visitor skips the passage): the synopsis (§6.18)
carries the warning in static red — a warning must be reachable without the
chart.

**V2 — Accessibility.** The pulse is never the only signal: the word itself,
its red colour (column), and its presence in the bulletin grammar all carry
the meaning without motion. `aria` text is the plain sentence. Letterspacing
animation does not trigger reflow of surrounding text beyond its own line
(the gale line is its own line by grammar, §12). Contrast: `--buoy` on
`--paper-deep` 4.7:1 at 15px bold mono — passes large/bold floor; the word
is additionally always preceded by "GALE WARNING" in `--ink`.

**V2 — Tokens consumed.** `--buoy`, `--ink`, `--pulse-gap: 0.12em`,
`--pulse-period: 1800ms`.

---

### 6.8 Compass-needle progress

- **What & why.** A compass rose in the header rotates its needle, scrubbed,
  to point toward the current area's bearing on the chart, with "AREAS
  COVERED n/31" counted beside it. Progress as orientation: you are not 40%
  through a page, you are *off Dogger, bearing north-east*.
- **Structure.** `<div class="compass">` — an inline SVG rose (64px desktop,
  44px mobile): outer ring and cardinal ticks in `--ink-hairline`, N/E/S/W
  letters in instrument mono (§3), and a needle group (two triangles: north
  half `--buoy`, south half `--ink`) rotated via CSS `rotate()` on the SVG
  group, driven by the shared rAF loop (lerp 0.18). The counter is
  `<p class="areas-covered">AREAS COVERED <span>7</span>/31</p>` in mono.
  Each area's bearing is real data: the bearing from the chart's origin
  (the hero's position, area 1's centroid) to the area's centroid, computed
  at build time and stored as `data-bearing` degrees.
- **Motion spec.** Needle rotation is scrubbed to passage progress mapped
  through the committed area's bearing: within an area's dwell, the needle
  eases from the previous area's bearing to the current one's across the
  crossing (it swings as you travel, like a compass settling after a turn).
  Shortest-path rotation always (a swing from 350° to 10° goes +20°, never
  −340°). Counter steps at commit, no roll (areas are counted, not measured).
- **States.** *Rest:* bearing of Viking. *Travelling:* swinging/settling.
  *Vertical acts:* the needle holds the last area's bearing and the counter
  reads the final count — the instrument remembers the passage. *Hero
  (before passage):* needle points to Viking, counter 0/31... corrected by
  the grammar: before entry it reads "AREAS COVERED 0/31" only once the
  passage begins; in the hero it reads the first area's name instead
  ("FIRST AREA: VIKING") — an instrument shows position before it shows
  progress.
- **Content merge.** The needle reads the same chart the visitor is
  crossing: its bearings are computed from the chart's own geometry. It is
  a working instrument of the page, not a logo that spins.
- **Failure fallback.** Static rose pointing north, counter replaced by the
  area index link (§6.18). No-JS: same.
- **Reduced-motion variant.** Needle jumps (no swing) to the committed
  area's bearing at commit; in the vertical stack it updates per area block
  as they pass the viewport centre.
- **Performance budget & mobile variant.** One transform per frame.
  Mobile: rose 44px, counter shortens to "7/31" with the words in its
  `aria-label` and a caption beneath at ≥360px width only.

**V2 — Choreography timeline** (per crossing):
| Beat | Event |
|---|---|
| 1 | Previous area un-commits — needle begins shortest-path swing |
| 2 | Swing duration = crossing duration (scrubbed, lerp 0.18) — no fixed ms: the needle is slaved to travel |
| 3 | New area commits — counter steps n → n+1 (or n−1 travelling back) |
| 4 | Needle settles within ±0.5° of bearing and rests (loop stops writing when settled — the rAF loop idles the needle) |

**V2 — State matrix.**
| State | Desktop | Touch |
|---|---|---|
| Rest | Bearing of current area | Same, smaller rose |
| Hover | Rose brightens one step (`--ink-hairline` → `--ink` at 60%) and a tooltip-label names the current area + bearing ("DOGGER — 042°") | n/a |
| Focus | The compass is a link to §6.18's index ("Area index") — focus ring 2px `--ink`; the needle keeps working | Same |
| Active (travelling) | Swinging per timeline | Same |
| Scrolled-past | Holds final bearing | Same |
| Disabled | Static north + index link | Same |

**V2 — Breakpoints.** ≥1200px: 64px rose + full counter text. 768–1199px:
56px rose + full counter. <768px: 44px rose + "n/N" counter.

**V2 — Edge cases.** *Bearing wrap:* shortest-path rule (above). *Areas
with near-identical bearings* (Forth/Tyne): the needle barely moves — that
is correct, and the counter carries the progress signal instead. *Travel
back up:* needle swings back; counter decrements — the instrument reports
position, not achievement. *Missing bearing data for an area:* the needle
holds the previous bearing and the area is flagged in the build log —
never interpolate a fake bearing (§9).

**V2 — Accessibility.** The compass link's accessible name: "Area index —
currently Dogger, area 7 of 31". The needle's rotation is `aria-hidden`
(the number and name carry the information). Counter text is real text.
Contrast: needle `--buoy` half is display-only; the counter is `--ink`
10.9:1. Touch target: the whole compass block ≥44×44px.

**V2 — Tokens consumed.** `--ink`, `--ink-hairline`, `--buoy`, `--gale`
(counter label), `--lerp-needle: 0.18`, `--rose-size: 64px`.

---

### 6.9 Porthole chart reveal

- **What & why.** The chart first reveals through a porthole-round
  clip-path that expands to the full frame (900ms) on load: the ship's
  window opening onto the chart. It is the theme's single entrance
  ceremony, and it teaches the whole metaphor in one beat — you are aboard,
  the chart is outside the glass, and the glass is about to stop mattering.
- **Structure.** The hero stage (§6.14) wraps the chart's opening view in
  `<div class="porthole">` with `clip-path: circle(18% at 50% 42%)` as the
  JS-armed start state (base CSS has no clip — see fallback), animating to
  `circle(75% at 50% 50%)` (full frame coverage) over 900ms
  `--ease-settle`. A brass-less ring — this theme has no brass; the ring is
  a double hairline in `--ink` at 40% — is drawn as an SVG circle overlay
  that fades out as the clip passes 60%.
- **Motion spec.** 900ms total: clip expands 0–900ms; inside it, the grain
  layer's blur goes 6px → 0 across 200–800ms (condensation clearing, §5);
  the first isobar system begins its draw (§6.1) at 500ms, visible through
  the widening glass; at 900ms the clip and ring are removed entirely
  (`clip-path: none`) so no clipping context survives into the passage.
- **States.** *Rest (after):* no trace — the porthole exists only as the
  memory of an opening. *Re-entry (back navigation):* never replays; the
  chart arrives whole (a window you have already opened stays open).
- **Content merge.** The porthole frames the actual chart the visitor is
  about to travel — not a hero image. What is revealed is the working map,
  mid-draw.
- **Failure fallback.** Base CSS: no clip-path at all — the chart is simply
  there. JS arms the clip only after confirming the chart SVG has rendered
  (one rAF), and the 1.2s fallback removes any clip unconditionally. A
  stalled load can never leave the site's content inside a small circle.
- **Reduced-motion variant.** No porthole. The chart fades in as a whole
  over 200ms (or is simply present, in the stack).
- **Performance budget & mobile variant.** Clip-path animation on one
  wrapper, 900ms, once per session (sessionStorage flag). Mobile: the
  circle centres at 50% 38% (over the first area, not the empty sea), same
  duration.

**V2 — Choreography timeline:**
| Beat | Time | Event |
|---|---|---|
| 1 | 0ms | Page paints with chart unclipped (base state) |
| 2 | +1 rAF (~16ms) | JS arms clip at 18% — before first paint in practice via an inline `js` class on `<html>` set in `<head>`; if that class is absent, beats 2–6 never happen |
| 3 | 0–900ms | Clip expands, `--ease-settle` |
| 4 | 200–800ms | Grain blur 6px → 0 |
| 5 | 500ms | §6.1 draw begins inside the opening |
| 6 | 900ms | Clip + ring removed; hero hands over to the passage |

**V2 — State matrix.**
| State | Desktop | Touch |
|---|---|---|
| Rest | Post-reveal, no clip | Same |
| Hover / Focus / Active | n/a — a one-shot load ceremony | n/a |
| Scrolled-past | Never replays | Never replays |
| Disabled | No-JS / reduced-motion / session replay → chart simply present | Same |

**V2 — Breakpoints.** ≥1200px: circle at 50% 42%. 768–1199px: 50% 40%.
<768px: 50% 38%, start radius 22% (the first area must be legible inside
the porthole on a small screen — a circle of empty sea teaches nothing).

**V2 — Edge cases.** *Slow first paint:* if the chart SVG is not ready
within 600ms, the ceremony is skipped (the clip arms only on readiness) —
a late porthole over a late chart is a double delay. *Browser without
clip-path circle support:* feature-detected; the reveal degrades to the
200ms whole-chart fade. *Visitor scrolls during the 900ms:* the ceremony
completes regardless (it is load-locked, not scroll-locked), and the
passage scrub takes over from the actual scroll position.

**V2 — Accessibility.** The clip is a visual mask over content that is
fully present in the DOM and never `visibility`-hidden — screen readers
read the hero normally throughout. The ceremony is skipped under reduced
motion. No focus is moved. The ring overlay is `aria-hidden`.

**V2 — Tokens consumed.** `--ink`, `--ease-settle`,
`--porthole-dur: 900ms`, `--porthole-from: 18%`.

---

### 6.10 Area-fill hover + forecast highlight

- **What & why.** Hovering a sea area fills its boundary with pale sea ink
  and simultaneously highlights that area's line in the broadcast column.
  Map and bulletin answer together — one region, two renderings, linked.
  It is the theme's core interaction: the chart and the radio are one
  instrument, and this is where the visitor feels it.
- **Structure.** Each area is an SVG `<path class="area" data-area="forties"
  tabindex="-1">` (pointer-events on the fill) with a paired
  `<li data-area-line="forties">` in the column's area list (the column
  carries, beneath the current bulletin, a compact list of all areas'
  one-line summaries — the "later bulletins" — from which the highlight
  reads). Fill is a dedicated underlay path (same `d`) filled
  `--ink-pale`, opacity 0, so the boundary stroke and name never tint.
- **Motion spec.** Fill opacity 0 → 0.18 over 250ms `--ease-swell`;
  the paired line in the column gains a `--paper` background wash and a
  2px `--ink` left rule drawing in 200ms. On leave, both reverse (200ms).
  The currently *centred* area is exempt: it wears a permanent 0.10 fill
  (you are *in* it), and hovering it deepens to 0.18 without touching the
  column (its line is the bulletin itself).
- **States.** *Rest:* fills at 0 (centred area 0.10). *Hover:* as above.
  *Focus:* keyboard focus on an area's content anchor produces the identical
  fill + highlight (hover and focus are the same signal in this theme).
  *Scrolled-past:* fills persist per current area only.
- **Content merge.** The highlight target is the area's real forecast line —
  the interaction navigates the content, not a tooltip about it.
- **Failure fallback.** Without JS, areas are not hoverable, but every
  forecast line is printed in the annex (§6.2 fallback) — the link between
  map and text is an enhancement, never the only path.
- **Reduced-motion variant.** Fill and wash swap instantly (0ms); the link
  between the two renderings is information, and information is not motion.
- **Performance budget & mobile variant.** Two style writes per hover.
  Mobile: no hover — a tap on an area's name commits §6.11's ping and, if
  the area is off-centre, scrolls the passage to centre it (the tap *is*
  the travel).

**V2 — Choreography timeline:**
| Beat | Time | Event |
|---|---|---|
| 1 | pointerenter +0ms | Underlay fill begins 0 → 0.18 (250ms) |
| 2 | +40ms | Column line's left rule draws (200ms) — a hair behind the fill, so the eye lands on the map first, then the text |
| 3 | +60ms | Column wash fades in (200ms) |
| 4 | pointerleave | All reverse over 200ms, rule first |

**V2 — State matrix.**
| State | Desktop | Touch |
|---|---|---|
| Rest | Fill 0 (centred 0.10) | Fill 0 (centred 0.10) |
| Hover | Fill 0.18 + column highlight | n/a |
| Focus | Identical to hover | Identical via anchor focus |
| Active (tap/click) | §6.11 ping fires; fill holds during press | Ping + travel-to-centre |
| Scrolled-past | Only centred area filled | Same |
| Disabled | Annex-only mode (no JS): no fills, all text printed | Same |

**V2 — Breakpoints.** ≥1200px: full pairing with the column list.
768–1199px: the column's area list is collapsed to the current ± 2 areas;
hovering an area outside that window highlights by scrolling the list to
its line (the list is short; the scroll is instant, not animated).
<768px: no column list (bottom sheet) — hover pairing is replaced by the
tap behaviour above; the *centred* fill remains.

**V2 — Edge cases.** *Pointer crossing boundaries quickly:* enter/leave
debounced at 60ms so skimming the chart does not strobe the column.
*Adjacent-area overlap at boundaries:* the topmost (smallest) area wins
hit-testing — boundaries are drawn so small areas (Cromarty, Dover) sit
above their neighbours in z-order. *Keyboard user tabs through anchors
while the chart is off-screen:* the fill still applies (the state is
honest), and the annex copy of the anchor is what they are reading — the
chart state and the annex never disagree.

**V2 — Accessibility.** Areas are not tab stops (31 polygons in the tab
order is a trap); their anchors are, in the index (§6.18) and annex. The
hover pairing is duplicated for focus exactly. The fill is a ≥0.18 ink wash
— area names remain `--ink` on paper through it (≥9:1 effective). The
column line's highlight is not colour-only: the left rule + wash + the
line's area name in 500 weight.

**V2 — Tokens consumed.** `--ink-pale`, `--ink`, `--paper`,
`--fill-dur: 250ms`, `--ease-swell`, `--fill-centred: 0.10`,
`--fill-hover: 0.18`.

---

### 6.11 Buoy-bell click

- **What & why.** Clicking an area marker pings a ring outward from it —
  an expanding circle stroke, fading, 700ms — a buoy bell's sound drawn on
  water. It is the theme's only click flourish, and it belongs to the
  chart's physics: sound travels across water in rings.
- **Structure.** A `<circle class="ping">` in an overlay SVG group, spawned
  at the marker's coordinates on click: `r` from 4 → 90 SVG units, stroke
  `--buoy` 2px → 0.5px, opacity 0.75 → 0. Maximum 3 concurrent pings
  (older ones are removed) — a harbour of bells is noise.
- **Motion spec.** 700ms `--ease-swell` (fast birth, long decay — the
  swell curve's tail *is* the bell's decay). The marker itself gives a
  single 120ms scale pulse 1 → 1.15 → 1 (the bell struck). No sound —
  the theme is silent; the ring is the sound, drawn.
- **States.** *Rest:* no rings. *Click:* ring + marker pulse. *Rapid
  clicks:* capped at 3 rings; the marker pulse retriggers. *Scrolled-past:*
  markers in the annex (station cards) ping identically on their card's
  chart thumbnail (§6.15) — one behaviour, everywhere.
- **Content merge.** The ring radiates across the chart surface from the
  area's own marker and crosses its neighbours' water — it maps the
  area's acoustic presence on the same geography everything else uses.
- **Failure fallback.** Without JS, markers are plain links to the area's
  annex section — the click still *goes* somewhere true.
- **Reduced-motion variant.** No ring. The marker pulse becomes a static
  200ms outline flash (a drawn circle at fixed r=24, fading) — acknowledgement
  without travel.
- **Performance budget & mobile variant.** ≤3 SVG nodes animated, transform/
  opacity only... (r is an attribute — animated via `transform: scale` on a
  unit circle to stay compositor-only). Mobile: ring radius 64 units
  (smaller water), otherwise identical.

**V2 — Choreography timeline:**
| Beat | Time | Event |
|---|---|---|
| 1 | click +0ms | Marker pulse begins (120ms) |
| 2 | +30ms | Ring spawns at r=4, opacity 0.75 |
| 3 | 30–730ms | Ring expands to r=90, stroke thins, opacity → 0 |
| 4 | +730ms | Ring node removed |

**V2 — State matrix.**
| State | Desktop | Touch |
|---|---|---|
| Rest | No rings | No rings |
| Hover | Marker warms: its dot fills `--buoy` at 40% (120ms) — the bell is touchable | n/a |
| Focus | Marker link focus = same warm + 2px outline | Same |
| Active | Ring + pulse per timeline | Ring + travel-to-centre (§6.10) |
| Scrolled-past | Rings complete even if the area leaves view (they are on the chart, not the screen) | Same |
| Disabled | No-JS: markers are annex links | Same |

**V2 — Breakpoints.** Identical behaviour at all sizes; ring radius 90 /
72 / 64 units by breakpoint band.

**V2 — Edge cases.** *Clicking the centred area:* ring fires, no travel.
*Clicking during a fast pan:* the ring spawns in chart coordinates, so it
travels with the chart — correct: the bell is in the water, not on the
glass. *Marker near a chart edge:* the ring clips at the chart boundary —
also correct; sound stops at the shore (the chart's edge).

**V2 — Accessibility.** The ping is acknowledgement decoration on a real
link/button: the control's accessible name is "Go to Forties report" (or
the area's action), never "ping". The ring is `aria-hidden`. The action's
result (navigation/centring) is the accessible feedback; motion is not
the only signal.

**V2 — Tokens consumed.** `--buoy`, `--ink`, `--ping-dur: 700ms`,
`--ping-r: 90u`, `--ease-swell`.

---

### 6.12 Skeleton chart + static-tune transition

- **What & why.** The theme's two in-between states. Loading draws the
  skeleton chart — grid and station circles first, isobars drawing as data
  lands. Navigation is a beat of broadcast static (120ms of noise), then
  the next area tunes in centred. Both states are made of the theme's two
  materials — chart and broadcast — so even waiting is in-world.
- **Structure.** Skeleton: the chart SVG with grid + boundaries at final
  state (paper is never "loading"), station circles as pulseless hollow
  dots, isobar groups held at `stroke-dashoffset` start; as each data
  chunk resolves, its system draws per §6.1 (600ms version). Static-tune:
  a full-stage overlay `<div class="static">` — the paper-grain background
  at 100% weight, animated by 3 steps of background-position jitter over
  120ms — followed by the destination rendering with its area centred.
- **Motion spec.** Skeleton draw per system: 600ms `--ease-settle`, in
  data-arrival order (not chart order — the skeleton is honest about what
  has actually arrived). Static: 120ms, `steps(3)`, then a 400ms settle
  (fade 120ms + the destination's isobars at final state — transitions do
  not redraw the whole chart; only the newly centred area's name fades in,
  200ms).
- **States.** *Loading:* skeleton until data, then §6.1's ceremony is
  *skipped* (the skeleton already drew the chart — two drawings is a
  repeat). *Loaded:* normal theme. *Navigating:* static beat, then tuned.
  *Error:* see edge cases.
- **Content merge.** The skeleton is the chart's own underdrawing — grid,
  coasts, stations: everything that is true before the weather arrives.
  The static is the broadcast's own between-stations noise.
- **Failure fallback.** If data fails: the skeleton completes as a printed
  chart (boundaries + names, no isobars) and the column prints the §12
  failure bulletin. The page is a chart with no weather — still navigable,
  still honest. Hard cap: skeleton state may not persist beyond 4s; at 4s
  the printed-chart fallback renders regardless.
- **Reduced-motion variant.** No static burst (a plain 120ms paper fade
  between routes); skeleton appears complete, systems fade in whole.
- **Performance budget & mobile variant.** The static overlay is one div,
  120ms. Mobile: identical.

**V2 — Choreography timeline** (route change):
| Beat | Time | Event |
|---|---|---|
| 1 | click +0ms | Static overlay in (30ms) |
| 2 | 30–150ms | Grain jitter, 3 steps |
| 3 | 150ms | Destination renders beneath (area centred, systems drawn) |
| 4 | 150–270ms | Static fades out |
| 5 | 270–470ms | Centred area's name fades to full ink; column types (§6.3) |

**V2 — State matrix.**
| State | Desktop | Touch |
|---|---|---|
| Rest | n/a (transient states only) | n/a |
| Loading | Skeleton per above | Same |
| Navigating | Static-tune per timeline | Same |
| Error | Printed chart + failure bulletin | Same |
| Disabled | No-JS: full printed chart, normal link navigation, no static | Same |

**V2 — Breakpoints.** Identical at all sizes.

**V2 — Edge cases.** *Slow data in chunks:* systems draw as they land;
areas whose data has not arrived show their boundary + name + "NO REPORT
YET" in the column list (§12) — absence is labelled, never faked.
*Back-button during static:* the transition is <500ms total; a popstate
mid-beat cancels the overlay (the destination is already rendered beneath).
*Repeated rapid navigation:* static beats never queue — a second click
restarts the single beat.

**V2 — Accessibility.** The skeleton region carries `aria-busy="true"`
until data lands, with a visually-hidden "Chart loading" text; the static
burst is `aria-hidden` and is never announced (it is 120ms of texture, and
under reduced motion it does not exist). Route changes move focus to the
destination's heading per standard SPA practice — the one focus move the
theme permits itself.

**V2 — Tokens consumed.** `--paper`, `--ink`, `--ink-hairline`, `--gale`,
`--static-dur: 120ms`, `--ease-settle`, `--skeleton-cap: 4s`.

---

### 6.13 Chart-table navigation (header)

- **What & why.** The header is the broadcast's own opening: the wordmark is
  set as the bulletin's first line — the service name in Fraunces, and
  beneath/behind it the mono line "AND NOW, THE SHIPPING FORECAST" as the
  header's kicker. Navigation links are named for chart furniture, not web
  furniture: THE CHART (the passage), AREAS (the index, §6.18), STATIONS
  (§6.15), THE BULLETIN (the conversion section, §6.16). The compass
  (§6.8) sits in the header as its instrument.
- **Structure.** 56px bar, `--paper`, hairline bottom rule. Left: kicker
  (11.5px mono, `--gale`) over wordmark (Fraunces 22px). Centre-right:
  nav links (mono 13px uppercase, 44px targets). Right: compass + counter
  (§6.8) and the Night watch toggle (a mono text toggle, "NIGHT WATCH:
  OFF/ON" — no switch UI; §11's ruling).
- **Motion spec.** Links: hover draws a hairline underline left-to-right
  (200ms `--ease-swell`) and inks from `--gale` to `--ink`. The current
  section's link carries a permanent hairline + full ink. On scroll into
  the passage, the header's kicker crossfades from "AND NOW, THE SHIPPING
  FORECAST" to the current area's name (200ms) — the broadcast is now *in*
  the areas. Nothing else moves; a header that performs is a header that
  lies about being an instrument panel.
- **States.** *Rest / hover / focus:* as above; focus = hover state + 2px
  outline. *In-passage:* kicker shows the area. *In vertical acts:* kicker
  shows the act's chart term (SYNOPSIS, STATIONS, INSHORE WATERS).
- **Content merge.** The nav names are the site's actual geography and
  documents; the kicker's area display is the same committed-area state
  that drives the column, needle, and readings — one state, four
  instruments.
- **Failure fallback.** Plain header, plain links, kicker static. No-JS:
  identical minus the kicker's area updates.
- **Reduced-motion variant.** Underline and kicker swap instantly.
- **Performance budget & mobile variant.** Negligible. Mobile: nav
  collapses to two links (AREAS, THE BULLETIN) + the compass; the rest
  live in the index (§6.18) — a chart table does not grow a hamburger; it
  points to its index.

**V2 — Choreography timeline:**
| Beat | Time | Event |
|---|---|---|
| 1 | Passage entry | Kicker crossfades to first area name (200ms) |
| 2 | Each area commit | Kicker name swaps (instant — it is a readout, not a headline) |
| 3 | Passage exit | Kicker crossfades to the act's term |

**V2 — State matrix.**
| State | Desktop | Touch |
|---|---|---|
| Rest | Links `--gale`, current full ink + hairline | Two links + compass |
| Hover | Underline draw + ink | n/a |
| Focus | Hover state + outline | Same |
| Active | Link inks `--buoy` for the press duration only (120ms) — red is rationed even here | Same |
| Scrolled-past | Kicker per act | Same |
| Disabled | n/a | n/a |

**V2 — Breakpoints.** ≥1200px: full nav. 768–1199px: nav links at 12.5px,
kicker hidden (the column already names the area). <768px: two links,
compass 44px.

**V2 — Edge cases.** *Long service names:* the wordmark truncates never —
the header grows to two lines before the wordmark shrinks below 19px (a
name is not a logo slot). *Night watch toggle:* state persists in
localStorage; the toggle's label always states the *current* state, not
the action.

**V2 — Accessibility.** Header is a `banner`; nav is a labelled `nav`;
the kicker's changing area name is `aria-hidden` (the column and counter
carry it accessibly). Skip link: "Skip to the area index" — the index is
this site's true table of contents. Targets ≥44px.

**V2 — Tokens consumed.** `--paper`, `--ink`, `--gale`, `--buoy`,
`--ink-hairline`, `--ease-swell`.

---

### 6.14 The opening area (hero)

- **What & why.** The hero is not a banner above the chart; it is the
  chart's first area arriving: the porthole (§6.9) opens onto the chart
  with Viking centred, the headline set *inside* Viking's water as chart
  lettering's guest, and the first bulletin already typing in the column.
  The hero's job is to teach the whole site in one screen: here is a chart,
  it will travel, and a voice will read it to you.
- **Structure.** Full-viewport stage: the chart SVG's opening view (Viking
  + North Utsire + the top of Forties), the headline (Fraunces 56px,
  2 lines max, set in Viking's open water, clear of boundaries per §4's
  sea-room rule), a one-line mono standfirst in bulletin voice ("VIKING.
  NORTHERLY 4 OR 5. SHOWERS. GOOD." — the hero *is* the first forecast),
  and a single action: "BEGIN THE PASSAGE" (a text link with a hairline,
  scrolling into the passage). The broadcast column is present from the
  hero onward (it is pinned furniture, not passage-only).
- **Motion spec.** Porthole ceremony (§6.9) → isobars draw (§6.1) →
  headline lines mask-reveal (2 lines × 140ms, §5) starting at porthole
  600ms → standfirst types at §6.3's rate after the headline → the
  BEGIN link's hairline draws. Total ceremony ≤ 2.4s, and the visitor can
  scroll at any moment — scrolling cancels nothing and breaks nothing
  (all states land via the 1.2s fallback).
- **States.** *Rest:* chart open, Viking committed, bulletin complete.
  *Scrolled:* the hero *is* the passage's first dwell — Viking's commit
  is the passage's first beat.
- **Content merge.** The headline sits in the first area's water and the
  standfirst is that area's real forecast: the hero's copy and the site's
  data are the same sentences.
- **Failure fallback.** Static chart opening, headline printed, standfirst
  printed, column showing Viking's bulletin. Complete without JS.
- **Reduced-motion variant.** The stack's first block: Viking's area
  printed with its forecast; headline above it as a normal heading.
- **Performance budget & mobile variant.** The hero is the LCP: chart SVG
  inline (no fetch), headline text paints before the ceremony arms.
  Mobile: headline 34px set in the widened Viking view; the porthole
  centres on Viking (§6.9).

**V2 — Choreography timeline:**
| Beat | Time | Event |
|---|---|---|
| 1 | 0ms | First paint: headline + standfirst visible (base state) |
| 2 | ~16ms | Porthole arms (if JS + first visit) |
| 3 | 500ms | Isobars begin drawing inside the opening |
| 4 | 600ms | Headline mask-reveal (only if the ceremony is running; otherwise it was never hidden) |
| 5 | 900ms | Porthole fully open, clip removed |
| 6 | ~1100ms | Column types Viking's bulletin (or it was already printed) |
| 7 | ≤2400ms | All ceremony complete; breathing + fronts take over |

**V2 — State matrix.**
| State | Desktop | Touch |
|---|---|---|
| Rest | Open chart, Viking centred | Same |
| Hover | Areas per §6.10 | n/a |
| Focus | BEGIN link reachable as the page's first action; focus never auto-moved | Same |
| Active | Scrolling enters the passage seamlessly | Same |
| Scrolled-past | Hero is passage beat 1; no separate exit state | Same |
| Disabled | Static printed opening | Same |

**V2 — Breakpoints.** ≥1200px: as spec. 768–1199px: headline 44px.
<768px: headline 34px, standfirst max 3 lines, column = bottom sheet.

**V2 — Edge cases.** *Headline longer than 2 lines:* the hero's copy
budget is a build-time law (§12) — headlines are written to the water they
sit in; if a headline cannot fit Viking's water at 34px, the copy is
rewritten, never shrunk below 34px and never allowed across a boundary.
*Return visit:* porthole skipped (session flag), chart arrives whole.
*Slow device:* ceremony beats are time-based, not frame-based — a 30fps
device sees the same 900ms, coarser.

**V2 — Accessibility.** Headline is the page's `<h1>`. The standfirst's
typed reveal follows §6.3's a11y (complete text in DOM). The BEGIN link's
name: "Begin the passage — travel the chart". Contrast per §2/§3.

**V2 — Tokens consumed.** `--paper`, `--ink`, `--gale`, `--ease-settle`,
`--porthole-dur`, `--type-char`.

---

### 6.15 Station cards

- **What & why.** In the vertical acts, coastal stations become cards: each
  card is a station report — name, its area, its latest readings, a small
  chart thumbnail (the area's boundary with the station dot), and a
  photograph if the station has one. A card in this theme is not a tile in
  a grid of offers; it is a line in a logbook, framed like a chart
  correction slip.
- **Structure.** `<article class="station-card">`: header row (station name
  Fraunces 20px + area name mono `--gale`), readings block (mono, §6.6's
  values as static text), thumbnail SVG (boundary path + station dot +
  the station's isobar fragment), optional photo in a chart-grid frame
  (§5 image treatment). Cards lay out in a ruled grid: hairline rules
  between rows, like a logbook's lines — no shadows, no rounded corners
  (charts do not have rounded corners; corner radius is 0 everywhere in
  this theme).
- **Motion spec.** Entry: the card's top rule draws (400ms), card fades/
  rises 8px (600ms `--ease-settle`), staggered 90ms within a row. Hover:
  the 1° chart-table tilt (§5) toward the pointer, 300ms, plus the
  thumbnail's station dot pings once (§6.11, small radius 40 units) on
  first hover per card per session. Photo: scale-in-frame per §5.
- **States.** *Rest:* printed report. *Hover:* tilt + dot ping. *Focus:*
  tilt replaced by a 2px outline (tilt under keyboard focus is noise).
  *Stale data:* the card's readings gain §6.6's "(EARLIER)" suffix.
- **Content merge.** Every visual in the card is the station's own data:
  its boundary, its dot, its numbers, its photograph of its own coast.
- **Failure fallback.** Static ruled list of reports — the logbook without
  the tilt. Complete without JS.
- **Reduced-motion variant.** No tilt, no ping; entry is instant.
- **Performance budget & mobile variant.** ≤ 12 cards animate entry per
  page; thumbnails are inline SVG ≤ 2KB each. Mobile: single column,
  thumbnail moves above the readings (the geography before the numbers),
  tilt off (no pointer), tap = the dot ping only.

**V2 — Choreography timeline** (per card, on entry):
| Beat | Time | Event |
|---|---|---|
| 1 | 0ms | Top rule draws (400ms) |
| 2 | 100ms | Card rises/fades in (600ms) |
| 3 | 300ms | Thumbnail's isobar fragment draws (500ms) |
| 4 | 700ms | Readings at value (they do not roll here — logbook entries are already written; rolling belongs to the live chart) |

**V2 — State matrix.**
| State | Desktop | Touch |
|---|---|---|
| Rest | Printed report | Printed report |
| Hover | 1° tilt + one dot ping | n/a |
| Focus | Outline, no tilt | Outline |
| Active | Card's link press: tilt settles to 0° in 120ms (the slip is picked up flat) | Same |
| Scrolled-past | Static | Static |
| Disabled | Stale variant per §6.6 | Same |

**V2 — Breakpoints.** ≥1200px: 3 per row. 768–1199px: 2 per row.
<768px: 1 per row, thumbnail-first order.

**V2 — Edge cases.** *Station with no photograph:* the thumbnail enlarges
to fill the frame — never a placeholder image, never a stock coast (§9).
*Station with no current readings:* the card prints "NO REPORT" and the
last report's time — a logbook shows its gaps. *Very long station names:*
wrap to two lines at 20px; never truncate a place's name.

**V2 — Accessibility.** Card is an `<article>` with its station name as
heading; the thumbnail SVG is `role="img"` labelled "Chart of {area},
{station} marked". Readings are text. Tilt is disabled for keyboard focus
and reduced motion. Touch targets: the card's link ≥44px tall.

**V2 — Tokens consumed.** `--paper`, `--paper-deep`, `--ink`, `--gale`,
`--ink-hairline`, `--ease-settle`, `--ease-swell`, `--ping-dur`.

---

### 6.16 The bulletin form (conversion)

- **What & why.** The conversion section is styled as a station log entry:
  the visitor is not "subscribing to a newsletter", they are asking to be
  sent the bulletin — by email, at the broadcast's own times. The form is a
  ruled log page: fields are lines in the log, labels are mono apparatus,
  and the confirmation is a broadcast sign-off. Best for: bulletin
  subscriptions, expedition enquiries, hotel booking enquiries — any
  conversion that is a *request for a report or a passage*.
- **Structure.** `<form class="log-form">` on `--paper-deep`, hairline-ruled:
  fields — NAME (the log's "reported by"), EMAIL, AREAS OF INTEREST (a
  checkbox list set as a two-column area index — the visitor ticks sea
  areas, §11), FREQUENCY (radio: EVERY BROADCAST / GALE WARNINGS ONLY /
  THE EVENING SYNOPSIS — the bulletin's real cadences), and the submit
  plate: a full-width ink block labelled in mono, "SEND ME THE BULLETIN".
  Errors appear as proof-style margin notes in `--buoy` beside the field,
  in §12's error voice.
- **Motion spec.** Focus: the field's rule inks from `--ink-hairline` to
  full `--ink` (200ms) and the label takes full ink. Submit: the plate
  presses (scale 0.99, 120ms), the form's rules redraw once (400ms — the
  log page is ruled fresh for the entry), then the confirmation replaces
  the form: a typed bulletin (§6.3's typing, 45ms/char) reading the §12
  confirmation copy with the visitor's reference number. Error: the field
  shakes *never* — charts do not shake; the margin note draws in (300ms)
  and the field's rule turns `--buoy` until corrected.
- **States.** *Rest:* faint rules, `--gale` labels. *Focus:* inked rule +
  label. *Filled:* rule stays at 60% ink (a written line is darker than an
  untouched one). *Error:* buoy rule + margin note, persistent until fixed.
  *Submitting:* plate pressed, fields disabled at full ink (never greyed —
  ink does not grey). *Success:* the typed confirmation, permanent.
- **Content merge.** The form is a page of the site's own logbook; its
  confirmation is a bulletin about the visitor's own request. The areas
  checkbox list is the chart's index — choosing areas on the form is
  pointing at the map's geography in text form.
- **Failure fallback.** A plain HTML form with server validation rendering
  the same margin notes as text. No-JS keeps the entire transaction.
- **Reduced-motion variant.** All state changes instant; confirmation
  prints complete, untyped.
- **Performance budget & mobile variant.** No loops; transitions on state
  only. Mobile: single column, area checkboxes one per row (44px targets),
  inputs at 16px minimum (also prevents iOS zoom).

**V2 — Choreography timeline** (submit):
| Beat | Time | Event |
|---|---|---|
| 1 | 0ms | Plate presses (120ms) |
| 2 | 120ms | Fields lock at full ink; rules redraw (400ms) |
| 3 | ~520ms | Request resolves (or error notes draw, per field) |
| 4 | +100ms | Confirmation types at 45ms/char, or the first error field receives focus |
| 5 | complete | Confirmation's reference number is the log entry's number — it is also sent in the email |

**V2 — State matrix.**
| State | Desktop | Touch |
|---|---|---|
| Rest | Faint rules, grey labels | Same |
| Hover | Field row's background washes `--paper` at 50% (200ms) | n/a |
| Focus | Rule + label ink (200ms) | Same |
| Active | Per submit timeline | Same |
| Scrolled-past | n/a — form state persists | Same |
| Disabled (submitting) | Full-ink lock, plate pressed | Same |

**V2 — Breakpoints.** ≥1200px: form at 62ch with a right margin column
for notes (the log's margin). 768–1199px: 56ch, notes move beneath fields.
<768px: full width, notes beneath, area list single column.

**V2 — Edge cases.** *Server failure:* the form keeps every value, the
plate re-labels "NOT SENT. TRY AGAIN." and a margin note at the form's
head gives §12's failure copy — an entry that failed is still an entry in
the log. *Duplicate submit:* the plate locks after first press; a second
entry is impossible until the state resolves. *Areas list with none
ticked:* valid — it means "all areas", and the confirmation says so in
voice ("ALL AREAS") rather than erroring: the bulletin's default is the
whole chart.

**V2 — Accessibility.** Labels are real `<label>`s; errors are tied by
`aria-describedby` and announced via a `role="alert"` summary at the
form's head on submit (margin notes are visual duplicates of that text,
never the only copy). Error is never colour-only: note + rule + text.
Focus order follows the log's reading order. Contrast: labels `--gale`
at 12px uppercase is the floor — inside the form, labels are 13px to stay
clear of it.

**V2 — Tokens consumed.** `--paper`, `--paper-deep`, `--ink`, `--gale`,
`--buoy`, `--ink-hairline`, `--type-char`, `--ease-swell`.

---

### 6.17 The sign-off footer

- **What & why.** The broadcast ends with a sign-off, and so does the site:
  the footer is the bulletin's closing — the general synopsis in one line,
  the edition line ("ISSUED AT 1130 ON MONDAY 23 NOVEMBER" — the page's
  real build/data time, §12's edition law), and the words the forecast
  itself ends with, set in Fraunces: "AND THAT CONCLUDES THE SHIPPING
  FORECAST." Beneath, the legal line and links set as colophon apparatus.
- **Structure.** Centred apparatus column on `--paper`: the closing line
  (Fraunces 28px), the synopsis line (mono, §6.18's text), the edition
  line (mono `--gale`), a hairline, then links (Imprint, Terms, Contact,
  Area index) with §6.13's underline behaviour, and the compass rose
  printed once, static, at 44px — the instrument at rest.
- **Motion spec.** The footer impresses once on entry: the closing line
  mask-reveals (140ms/line), the rose's needle swings from the last area's
  bearing to north over 900ms `--ease-swell` and stops — the instrument
  is put away pointing north. Nothing loops in the footer; the end of the
  broadcast is quiet.
- **States.** *Rest:* printed sign-off. *Hover:* links per §6.13.
  *Scrolled-past:* n/a — it is the end.
- **Content merge.** The edition line is the page's real data timestamp —
  the footer is the one place the site states its own edition, exactly as
  the bulletin does.
- **Failure fallback.** Static text block; needle printed north.
- **Reduced-motion variant.** Needle printed north; closing line unmasked.
- **Performance budget & mobile variant.** One 900ms transform, once.
  Mobile: unchanged (it was always a narrow column).

**V2 — Choreography timeline:**
| Beat | Time | Event |
|---|---|---|
| 1 | Footer enters | Closing line reveals (2 × 140ms) |
| 2 | +200ms | Needle begins swing to north (900ms) |
| 3 | +1100ms | Needle rests at north; page is still |

**V2 — State matrix.**
| State | Desktop | Touch |
|---|---|---|
| Rest | Printed sign-off | Same |
| Hover | Link underlines | n/a |
| Focus | Underline + outline | Same |
| Active / Scrolled-past / Disabled | n/a | n/a |

**V2 — Breakpoints.** Identical at all sizes; closing line 28 / 24 / 21px.

**V2 — Edge cases.** *Stale data edition:* if the data is from an earlier
edition, the edition line says so with its real timestamp — never a
freshened date. *No passage visited* (visitor jumped to the footer): the
needle starts at north already; the swing is skipped (an instrument that
was never used does not need putting away).

**V2 — Accessibility.** Footer is `contentinfo`; the closing line is a
paragraph, not a heading (the page's heading structure ended at the last
section). Edition line is text. All links ≥44px targets with 8px gaps.

**V2 — Tokens consumed.** `--paper`, `--ink`, `--gale`, `--ink-hairline`,
`--buoy` (needle north half), `--ease-swell`.

---

### 6.18 General synopsis strip + area index

- **What & why.** Two linked instruments that make the chart honest and
  navigable without it. The **general synopsis** — a real part of every
  broadcast ("AT 1800, LOW 984 WEST OF ROCKALL MOVING NORTH-EAST. HIGH
  1031 OVER THE FORTIES DECLINING.") — runs as a strip between the passage
  and the annexes, summarising the page's whole weather in one typed
  sentence. The **area index** is the chart's key: all 31 areas in
  broadcast order as a ruled mono list, each row carrying its one-line
  forecast and linking to its annex section. The index is the site's
  accessible spine — the chart, as a list.
- **Structure.** Synopsis: a full-width `--paper-deep` band, one mono
  sentence (15px, max 90ch), typed once on entry (§6.3 rate) or printed.
  Index: `<ol class="area-index">` — 31 rows (or N), each: area number
  (mono `--gale`), area name (Fraunces 18px), one-line forecast (mono,
  truncated never — rows grow), a hairline rule beneath. Rows are links
  to the area's annex block, where the area's full content prints
  vertically (the fallback stack, §6.2, is *this* list's expansion — the
  annex and the index are one document at two densities).
- **Motion spec.** Synopsis types on first entry (or prints). Index rows:
  entry stagger 40ms per row, rule draw + fade; hover: the row's area name
  inks and its chart twin's fill lights (§6.10 in reverse — if the chart
  is on screen in another viewport region, the fill answers; if not, the
  row alone highlights). The row for the currently committed area (during
  the passage) carries a `--buoy` index number — the one red numeral on
  the page's paper, marking *you are here* in the list.
- **States.** *Rest:* printed list. *Hover/focus:* as above. *Current:*
  red numeral. *Scrolled-past:* static.
- **Content merge.** The index is not a sitemap bolted on; it is the
  bulletin's own running order — the list the reader reads from. The
  synopsis is the broadcast's own summary sentence, generated from the
  page's pressure data by §12's grammar.
- **Failure fallback.** The index *is* the fallback — it works with no JS,
  no chart, no motion. The synopsis prints statically.
- **Reduced-motion variant.** Synopsis printed; rows instant; the red
  current-numeral still applies (state is not motion).
- **Performance budget & mobile variant.** 31 rows of text — negligible.
  Mobile: forecast line wraps under the name; rows ≥52px tall.

**V2 — Choreography timeline:**
| Beat | Time | Event |
|---|---|---|
| 1 | Synopsis enters | Sentence types (45ms/char) or prints |
| 2 | Index enters | Rows stagger in, 40ms apart, rules drawing |
| 3 | During passage | Current-area numeral updates at each commit |

**V2 — State matrix.**
| State | Desktop | Touch |
|---|---|---|
| Rest | Printed list | Printed list |
| Hover | Name inks + chart fill answers (if chart mounted) | n/a |
| Focus | Identical to hover | Identical |
| Active | Row press: name inks `--buoy` 120ms | Same |
| Scrolled-past | Static | Static |
| Disabled | n/a — this element is the fallback layer itself | n/a |

**V2 — Breakpoints.** ≥1200px: index in two columns (areas 1–16 / 17–31)
like a printed key. 768–1199px: two columns at narrower measure.
<768px: one column, full order.

**V2 — Edge cases.** *Fewer areas than 31:* the list is the true count;
columns split at the midpoint of the real list. *An area with NO REPORT:*
its row prints the words, and the row is not a link (there is nothing to
link to) — it remains in the running order, because the bulletin reads
every area, even the silent ones. *Synopsis data missing a pressure
system:* the sentence reports what exists ("LOW 984 WEST OF ROCKALL. NO
HIGH REPORTED.") — the grammar has a form for absence (§12).

**V2 — Accessibility.** This is the chart's text equivalent: a real
ordered list, in broadcast order, with the same forecasts. It satisfies
the chart's `role="img"` label by existing (the SVG's aria-label points
here: "…full list follows as the area index"). Every row's link name is
"{Area} — {one-line forecast}". Current-area state is conveyed by the
numeral colour *and* an `aria-current="true"` plus a visually-hidden
"(area in view)".

**V2 — Tokens consumed.** `--paper`, `--paper-deep`, `--ink`, `--gale`,
`--buoy`, `--ink-hairline`, `--ink-pale`, `--type-char`, `--ease-swell`.

---

## 7. Page application map

| Page type | How the theme plays out |
|---|---|
| **Home** | The full form: hero (§6.14) → passage (§6.2) through all areas → synopsis (§6.18) → station cards (§6.15) → bulletin form (§6.16) → sign-off (§6.17). The home page *is* one complete broadcast. |
| **Listing** (e.g. all stations, all voyages) | No passage. The listing is ruled like the area index (§6.18) at card density: §6.15 station cards in a logbook grid, headed by a synopsis line summarising the list ("24 STATIONS REPORTING. GALES IN TWO AREAS."). Filters are chart terms (BY AREA / BY SEA STATE), set as index tabs (§11), never as pill chips. |
| **Detail** (one area, one station, one voyage) | The detail page is one area, enlarged: its boundary drawn large at the head with its isobars, its full bulletin typed in a column that is now a sidebar, its stations as §6.15 cards. The compass (§6.8) sits in the header pointing at *this* area's bearing permanently — on a detail page, the instrument has arrived. |
| **About** | The "inshore waters" page: vertical, chart-paper, telling the service's own story as a log — dated entries ruled like §6.16's form, photographs in chart-grid frames. The one permitted flourish: the company's home-port area drawn as a small chart with its live forecast in the margin (the theme's elements, at annex scale). |
| **Contact / conversion** | §6.16's log form as the whole page, headed by the synopsis strip and the areas index as the areas-of-interest picker. Confirmation is a typed bulletin (§6.16). |
| **Article / story** | The passage in miniature: a story with 5–9 named stops may use a short chart (its own mini-geography, drawn to the same laws) with a broadcast column typing each stop's standfirst. Below 5 stops, the article is a vertical annex with chart furniture only — never force the passage. |
| **404** | "NO REPORT." — the missing page is an area that did not report: its would-be name in Fraunces, the bulletin line "THE PAGE YOU SOUGHT HAS NOT REPORTED. IT MAY HAVE MOVED, OR THE ADDRESS WAS MISREAD." and the area index as the way back. The 404 is in-grammar, in-voice, and genuinely useful. |
| **Search results** | Ruled index rows (§6.18 pattern) with the matched term underlined by a drawn hairline — results are findings in the log, not cards. Empty results use §12's empty-state voice. |

---

## 8. Worked examples (three, end-to-end)

### 8.1 The hero — "Harbourlight Ferries, opening screen"

A fictional ferry operator running to northern isles. Data: Viking is the
home area; the day's real forecast is loaded.

- **0ms** — First paint: paper, header (§6.13) with kicker "AND NOW, THE
  SHIPPING FORECAST", headline printed in Viking's water: "The islands are
  still there. So are we." (2 lines, Fraunces 56px), standfirst printed:
  "VIKING. NORTHERLY 4 OR 5. SHOWERS. GOOD." Column shows Viking's full
  bulletin statically. A screen-reader user and a no-JS user are already
  reading the finished hero.
- **~16ms** — JS arms the porthole (§6.9) at 18% over Viking.
- **200–800ms** — Condensation blur clears inside the glass.
- **500ms** — The low west of Rockall begins drawing its isobars (§6.1),
  visible through the widening porthole.
- **600ms** — Headline lines mask-reveal (they were never hidden from the
  DOM — the mask is a visual overlay state armed by JS).
- **900ms** — Porthole fully open and removed; the chart is simply the
  page. Breathing starts (§6.5); the front south of Viking begins its
  march (§6.4).
- **1100ms** — The column retypes Viking's bulletin at 45ms/char (a
  ceremony for sighted JS users; the text was already there) — *or*, if
  the studio prefers honesty over ceremony, the column is left as printed
  and typing is reserved for area changes. Either is lawful; §10's gate
  accepts both, and the choice is recorded per build.
- **Scroll begins** — the passage's first dwell: Viking is already
  committed, so the first crossing is Viking → North Utsire: needle swings
  (§6.8), counter steps to 2, column clears and types "NORTH UTSIRE.
  NORTHERLY 5. FAIR. MODERATE OR GOOD." Readings roll (§6.6).
- **Numbers audit** — Ceremony total ≤2.4s; LCP is the headline text
  (painted at 0ms, never held for the porthole); the hero works with JS
  off, fonts failed, or data stale (staleness prints per §6.6).

### 8.2 Mid-page — the passage crossing Dogger, with a gale in German Bight

The visitor is mid-passage. Dogger is centred; German Bight, two areas
ahead, carries a gale warning, IMMINENT.

- **Scroll beat 1** — Fisher un-commits; its fill drops from 0.10, the
  needle begins its shortest-path swing toward Dogger's bearing.
- **Scroll beat 2** — Dogger's centroid passes centre +24px hysteresis:
  commit. Column: 90ms clear, "DOGGER." types, 300ms breath, then
  "SOUTHWESTERLY 4 OR 5. FAIR. SLIGHT. GOOD." Pressure rolls 1013 → 1009
  (800ms), wind digit rolls 6 → 5, tendency prints FALLING.
- **Scroll beat 3** — While Dogger is centred, German Bight is visible at
  the stage's right edge. Its chart label carries the gale word with the
  red rule beneath (§6.7) — *not* pulsing: the pulse belongs to the
  committed area only. The visitor can see weather coming without the
  page crying wolf early. This restraint is the theme in one beat.
- **Scroll beat 4** — The visitor hovers Thames (behind them, still on
  screen at the left edge): fill 0.18, and the column list's Thames line
  highlights (§6.10) — the current bulletin is untouched. Map and list
  answer; the radio keeps reading Dogger.
- **Scroll beat 5** — German Bight commits: the bulletin types "GERMAN
  BIGHT. SOUTHWESTERLY 6 TO GALE 8. RAIN. ROUGH. MODERATE." and the gale
  line types with it: "GALE WARNING: IMMINENT." On the final character,
  the pulse starts (§6.7) in the column and on the chart label together.
  The needle settles on German Bight's bearing; the counter reads 10.
- **Reverse scroll** — the visitor scrolls back: German Bight un-commits,
  pulse stops (200ms letterspacing return), Dogger retypes in full. The
  radio reports where they are. Nothing is cached as "already seen" —
  the forecast is read as many times as you cross the water.

### 8.3 Conversion — the bulletin form, with an error and a success

Evening. The visitor wants the forecast by email, gales only, for three
areas.

- **Entry** — The section surfaces: rule draws (400ms), the log form
  fades/rises (600ms). Headline in voice: "THE BULLETIN, SENT." Standfirst:
  "FOUR TIMES A DAY, AS BROADCAST. NO OTHER MAIL." (a promise the
  service must keep — §12).
- **Interaction beat 1** — Focus NAME: rule inks (200ms), label inks.
  The visitor types. Focus EMAIL: same. They enter "a. mariner@"
  (incomplete) and move on: nothing happens yet — the log does not
  correct a writer mid-line.
- **Interaction beat 2** — They tick areas: FAIR ISLE, HEBRIDES, BAILEY
  (checkbox rows, §6.16/§11). They choose GALE WARNINGS ONLY (radio).
- **Submit** — Plate presses (120ms). Validation: the email field's rule
  turns `--buoy`; a margin note draws in (300ms): "EMAIL INCOMPLETE.
  THE ADDRESS ENDS MID-WORD." — §12's error voice: what is wrong, in the
  log's grammar, no apology, no exclamation. Focus moves to the field
  (the form's one permitted focus move, because the visitor asked for a
  verdict by submitting). The `role="alert"` summary announces the same
  text.
- **Correction** — The visitor completes the address; the note fades
  (200ms), the rule returns to ink. Resubmit: rules redraw (400ms),
  fields lock at full ink.
- **Success** — The form is replaced by a typed bulletin (45ms/char):
  "ENTRY LOGGED. A. MARINER WILL RECEIVE GALE WARNINGS FOR FAIR ISLE,
  HEBRIDES AND BAILEY. FIRST WARNING AT THE NEXT GALE. REFERENCE: LOG
  214." The reference is real (server-issued) and appears in the email.
  The visitor has not "subscribed"; they have been entered in the log —
  and the site now owes them a standard of behaviour, stated in the
  standfirst, that a newsletter never promises.

---

## 9. Anti-slop — what makes THIS theme look cheap, and the cure

1. **Clip-art weather icons** (a smiling sun SVG in a corner). *Cure:* the
   theme has no weather icons. Weather is isobars, fronts, and words. Any
   icon that is not a chart symbol is deleted at review.
2. **A fake "live" ticker of invented data.** *Cure:* every number on the
   chart comes from the build's data object, and its edition is printed
   (§6.17). If real data cannot be supplied, the theme ships with the
   source entry's own device — conditions generated from the *visitor's
   real local weather*, translated into forecast voice — and labelled as
   such in the synopsis. Invented readings presented as live are a
   blocking defect (§10).
3. **Areas as generic cards in a grid** (the chart quietly replaced by a
   card wall). *Cure:* §4's law — areas are polygons on a chart with
   lettering inside them. Cards exist only in the annex (§6.15), as
   station reports, under the chart's authority.
4. **Everything pulsing.** Three gale words pulsing, a bouncing needle, a
   blinking LIVE dot. *Cure:* the rationing laws — one pulse (§6.7), one
   red numeral (§6.18), red ≤ ~6% of surface (§2). Stillness is the
   theme's loudest signal.
5. **Pirate / nautical-kitsch drift** (ropes, anchors, "ahoy", parchment
   textures, navy-and-gold). *Cure:* this is the *forecast*, not the age
   of sail: chart paper is a printed artefact, not a treasure map. No
   texture beyond the paper grain; no word the bulletin would not say.
6. **The horizontal scroll that fights the user** (hijacked wheel, sticky
   traps, a passage that cannot be skipped). *Cure:* the passage is
   ordinary document scroll scrubbing a transform (§6.2) — no wheel
   handlers, no `scroll-jacking` listeners — and the area index (§6.18)
   plus the stack fallback give every visitor a vertical way through.
7. **Typing that gates content** (bulletins that exist only mid-type, or a
   column that is empty until JS runs). *Cure:* §6.3's DOM law — full
   text first, typing as reveal, 5s hard completion timer.
8. **Rounded corners, drop shadows, gradient buttons** (generic SaaS skin
   over chart paper). *Cure:* radius 0 everywhere; depth is drawn with
   hairlines and paper tones (`--paper-deep`), never shadows; the one
   "button" is an ink plate (§11).
9. **A compass that is a logo.** *Cure:* §6.8's bearings are computed from
   the chart's geometry; a decorative rose that points nowhere is §9
   slop even if it is beautiful. (The footer's resting rose, §6.17, is
   the single licensed exception — it points north, which is a true
   statement about a resting instrument.)
10. **Exclamation and hype in the bulletin voice** ("STORM INCOMING!!").
    *Cure:* §12's grammar is a build-time lint: bulletin strings are
    checked against the closed vocabulary; a string that fails does not
    ship.

---

## 10. Quality gate (blocking — all must pass)

1. Every forecast text exists complete in the DOM before any typing; the
   column is never the sole copy of any bulletin.
2. Reduced-motion build = the vertical stack: no passage, no typing, no
   ambient loops, all forecasts printed. Verified by rendering with
   `prefers-reduced-motion` and diffing the text content against the
   motion build — they must be identical.
3. No-JS render: full chart printed, hero complete, form submittable,
   index complete.
4. The 1.2s fallback: with JS artificially stalled, no element remains in
   a hidden/pre-animation state after 1.2s (skeleton cap 4s, §6.12).
5. Bearings audit: every area's `data-bearing` recomputed from the shipped
   SVG geometry matches within 1°.
6. Grammar lint: every bulletin string parses against §12's grammar
   (area → wind → weather → sea → visibility; timing words from the
   closed set).
7. Red ration: buoy red ≤ 6% of any viewport's pixels at rest (screenshot
   histogram), excluding the needle's north half and one gale word.
8. Contrast: body ink on paper ≥ 10:1 measured; gale-grey text never
   below 12px; buoy-red text only ≥14px bold or in the gale line.
9. Performance: §14's budgets measured on the reference device (below).
10. One current area: at any scroll position, exactly one area is
    committed, exactly one bulletin is current, exactly one index numeral
    is red. Automated scroll-through test, both directions.
11. No wheel/scroll listeners that preventDefault; the passage is pure
    document scroll.
12. Radius audit: `border-radius: 0` on all themed components (the
    porthole's clip-path circle is the only curve allowed to be round —
    it is glass, not a component).

---

## 11. Component inventory (complete, with themed treatments)

| Component | Shipping Forecast treatment |
|---|---|
| Primary button | The **ink plate**: full-ink block, paper mono uppercase label ("SEND ME THE BULLETIN"), press = scale 0.99 + 120ms. Never rounded, never gradient, never shadowed. One per view. |
| Secondary button / link | Text link with hairline underline that draws on hover (§6.13). |
| Text input | A log line: label above in mono apparatus, input on a hairline rule that inks on focus (§6.16). No boxes. |
| Select | A ruled line with the chosen value in mono and a small ink triangle (a chart symbol, not a chevron icon font). Options list = a paper slip with hairline rows. |
| Checkbox | A small square outline (ink) that fills with a drawn tick (a proof tick, 150ms draw) — used as the area picker (§6.16). |
| Radio | A small circle outline; chosen = filled station dot (the chart's own mark). |
| Toggle switch | **Refused.** State is stated in words ("NIGHT WATCH: ON") as a text toggle (§6.13) — the bulletin states things; it does not slide them. |
| Table | A station log: mono, hairline row rules, tabular figures, right-aligned readings, left-aligned station names in Fraunces small caps. Header row = apparatus labels in `--gale`. |
| Badge | A **stamp**: uppercase mono in a hairline rectangle ("GALE", "EARLIER", "NO REPORT"). `--buoy` border only for GALE. Never pill-shaped. |
| Alert | A **warning line**: full-width `--paper-deep` band with a buoy left rule and bulletin-voice text (§12). Errors in forms use §6.16's margin notes instead. |
| Pagination | Folio style: "AREAS 1–8 OF 31" with PREV / NEXT as mono links and a hairline — the count is geographic, not paginated chrome. |
| Modal | A **chart laid over the table**: paper panel, hairline frame, the page dims to `--ink` at 45% (the room darkens; nothing blurs). Title in Fraunces, actions as ink plate + text link. One modal deep, ever. |
| Toast | **Refused as a pattern.** Transient confirmations are log entries: a line types into a "recent entries" slip at the page foot (or the §6.16 confirmation pattern in place). Nothing floats, nothing auto-dismisses that a visitor might need to re-read. |
| Tabs | **Index tabs**: mono uppercase labels on a shared hairline; the active tab's label is full ink with a 2px ink rule above it (a tab on a chart folder). Content swaps instantly (tabs are filing, not weather). |
| Accordion | **Index expansion**: a row whose forecast line expands downward, pushing rows apart with a 250ms `--ease-swell` height settle — the list grows like a log being written, one entry open at a time. |
| Search | An index lookup: input on a rule; results are §7's ruled rows with the matched term hairline-underlined. The empty state is §12's "NO ENTRY UNDER THAT NAME." |
| Progress | Never a bar. Progress is the compass + count (§6.8) or, in a form, the log's entry number ("ENTRY 2 OF 4 FIELDS COMPLETE" — stated, not drawn). |
| Tooltip | A **margin note**: small mono text on `--paper-deep`, appearing beside (never over) its subject after 400ms hover, dismissed on leave. Carries facts only ("BEARING FROM VIKING: 042°"). |
| Breadcrumb | A **track line**: "THE CHART / DOGGER / STATIONS" in mono apparatus with hairline separators — the course sailed so far. |
| Divider | A drawn hairline, or at act boundaries an isobar fragment (one curve + its pressure value) — the chart signing the page break. |
| Avatar / image | Photographs only, in chart-grid frames (§5). No avatar circles — circles are portholes and compass roses in this theme, and both are taken. |
| Skeleton | §6.12's skeleton chart (for the chart) and ruled grey lines at bulletin widths (for text) — skeletons are underdrawings, never grey rounded blocks. |
| Empty state | A printed absence (§12): the area/section reports "NO REPORT" with the reason and the way onward. |

---

## 12. Content & copywriting voice

**The bulletin grammar (mandatory for all forecast-voice text).**
`AREA. WIND. WEATHER. SEA STATE. VISIBILITY.` — in that order, full stops
between clauses, all uppercase in the column. Wind = direction (16-point
compass, e.g. SOUTHWESTERLY, or VARIABLE) + Beaufort force ("5 OR 6",
"GALE 8", "4 OR 5, BECOMING 6"). Weather from the closed set: FAIR, SHOWERS,
RAIN, RAIN LATER, DRIZZLE, THUNDERI (only as "THUNDERY SHOWERS"), FOG
PATCHES, WINTRY SHOWERS. Sea state from: SMOOTH, SLIGHT, MODERATE, ROUGH,
VERY ROUGH, HIGH, VERY HIGH. Visibility from: GOOD, MODERATE, POOR, VERY
POOR (fog). Timing words: IMMINENT (≤6h), SOON (6–12h), LATER (>12h) —
attached to the change they time. Pressure tendency: RISING, FALLING,
STEADY, with the amount in words only in the synopsis ("FALLING SLOWLY").

**Headline voice** (Fraunces, sentence case, outside the column): plain,
weather-beaten, no hype. ✓ "The islands are still there. So are we."
✗ "Sail the Adventure of a Lifetime!!" Headlines may be lyrical about
place; they may never be excited about the product.

**Label voice** (apparatus mono): chart terms, stated as facts. ✓ "AREAS
COVERED 7/31". ✗ "You're 23% through your journey!" The count law: any
count printed (areas, stations, readings) is the true count from the data —
the source copy's "n/31" is a template for the real N, never a hard-coded
31 on a site with fewer areas.

**Error voice:** what is wrong, where, in log grammar; no apology, no
exclamation, no blame. ✓ "EMAIL INCOMPLETE. THE ADDRESS ENDS MID-WORD."
✗ "Oops! That email looks wrong 😕". Server failure: ✓ "NOT SENT. THE
LINE IS DOWN AT OUR END. YOUR ENTRY IS KEPT — TRY AGAIN." (and the entry
*is* kept, §6.16).

**Empty-state voice:** ✓ "NO REPORT FROM THIS STATION SINCE 0600." /
"NO ENTRY UNDER THAT NAME." An absence is reported like weather: plainly,
with its time and its reason if known.

**Success voice:** the entry is logged and numbered. ✓ "ENTRY LOGGED.
REFERENCE: LOG 214." A reference shown must be a real reference (§8.3).

**The edition law.** Every page states its data's edition once (§6.17):
"ISSUED AT {HHMM} ON {DAY DATE}". The time is the data's real issue time.
A page that cannot state its edition does not have data — it has
decoration, and §10 blocks it.

**Anti-slop detail, deepened (from the source entry).** Conditions on the
chart are generated from the visitor's real local weather, translated
into forecast voice ("FAIR, BECOMING MAINLY FAIR LATER"). Implementation
law: the translation is a documented mapping (condition code → weather
word; wind speed → Beaufort force via the standard scale; visibility in
metres → the four visibility words), the visitor's location is used only
in the browser (never sent to the site's server by the theme's code), and
the synopsis labels the source ("FROM YOUR OWN SKY, TRANSLATED."). If
geolocation or the weather fetch fails, the chart falls back to the
page's home-area data and says so. The device exists to keep the theme
honest — a chart of invented weather is a novel, not a forecast.

---

## 13. Full-page scroll choreography map

The canonical home page, top to footer. "Beat" = what the visitor sees and
feels, in order.

| # | Scroll position | Beat |
|---|---|---|
| 1 | Load | Porthole opens on Viking; isobars draw; headline lands in the water (§8.1). The visitor understands: *chart, voice, journey.* |
| 2 | Hero dwell | Fronts march, isobars breathe. Stillness with life in it. The BEGIN link waits. |
| 3 | Passage, areas 1–6 (Viking → Forth) | Travel establishes its rhythm: pan, type, roll, needle. By the third area the visitor has stopped noticing the mechanism — the radio is just on. |
| 4 | Areas 7–10 (Tyne → Humber) | First content anchors with photographs scale-in-frame; the chart proves it carries real cargo, not just weather. |
| 5 | Areas 11–15 (Thames → Plymouth) | The chart's most familiar waters; if a gale exists in the data, its red rule is sighted ahead before its area commits (§8.2 beat 3) — anticipation without alarm. |
| 6 | Areas 16–21 (Biscay → Lundy) | The long western leg: the widest areas, the slowest-feeling travel (same rate — the sea room makes it feel slower; this is intended, and §4's dwell math keeps the *rate* honest). |
| 7 | Areas 22–27 (Fastnet → Hebrides) | The bulletin voice is now fully trusted; readings' tendency words start telling a story across areas (FALLING, FALLING, FALLING — the visitor *feels* the low approaching before the synopsis says it). |
| 8 | Areas 28–31 (Bailey → Southeast Iceland) | The end of the running order: the counter approaches N/N; the needle's swings shorten (the northern areas cluster in bearing). |
| 9 | Passage exit | The stage releases. The synopsis strip types the whole page's weather in one sentence — the first time the visitor hears the *whole* sky at once. |
| 10 | Station cards | The logbook: the same stations, at reading pace, in rows. The tempo drops from travel to study. |
| 11 | Bulletin form | The conversion, framed as joining the log. The tempo is now one field at a time. |
| 12 | Footer | The needle swings home to north; the sign-off line. *That concludes the shipping forecast.* The page ends the way the broadcast ends: completely, and without asking for anything else. |

Reverse scroll replays the map backwards with §6.2's symmetry — the map
has no memory and no "already seen" states.

---

## 14. Whole-page performance budget

**Asset budget (home page, first load):**
- Total ≤ 700KB compressed, of which: inline chart SVG ≤ 120KB (the 31
  areas + isobars + fronts — geometry is cheap; if it exceeds 120KB the
  paths are over-sampled and must be simplified at build), fonts ≤ 130KB
  (Fraunces + IBM Plex Mono, subset to Latin + the bulletin's closed
  vocabulary for mono), photographs ≤ 300KB total above the fold (chart
  acts lazy-load the rest), JS ≤ 60KB gz (one rAF loop, one typing engine,
  one pan mapper — this theme needs no framework on the client).
- No webfont may block the headline: `font-display: swap` everywhere; the
  ceremony (§6.9) never waits for fonts.

**Runtime budget (reference device: mid-tier Android, 4× CPU throttle):**
- Frame budget: the shared rAF loop ≤ 3ms average per frame while
  travelling (pan transform + needle rotation + breathing interpolation
  at 30fps + front sampling for on-screen symbols only).
- No long task > 50ms after load; typing writes ≤ 1 text node per frame.
- LCP ≤ 2.0s (the headline — it is text and paints first), CLS ≤ 0.02
  (the chart's geometry is fixed by the SVG viewBox; nothing may reflow
  when data lands — readings reserve their digit widths), INP ≤ 200ms.
- Ambient layers (fronts, breathing, mist) are capped at 30fps updates.

**Cut order when the budget is exceeded** (cut in this order, never skip
ahead): 1) mist drift, 2) breathing amplitude → 0, 3) fronts beyond the
nearest two print statically, 4) isobar ring counts reduce to 3 per system,
5) photograph duotone hover lift removed. **Never cut:** the typing column
(it is content), the pan/needle (they are the progress instrument), any
fallback, any reduced-motion variant, the form's function.

---

## 15. Build-order checklist

1. **Tokens & paper.** Implement §2's tokens (incl. night-watch set) and
   §3's type scale; verify contrast pairs by measurement.
2. **The static chart.** Build the full SVG chart (grid, boundaries,
   names, stations, printed isobars/fronts) from the data object. Gate:
   the no-JS render is already a complete, beautiful printed chart (§10.3).
3. **The annex & index.** §6.18's index + the vertical area annexes +
   §6.15 cards + §6.17 footer, all static. The site is now fully usable
   with zero motion. This is deliberate: the theme is built as a printed
   bulletin first, a broadcast second.
4. **The form.** §6.16 with server validation; success/error in §12 voice.
5. **The broadcast column (static → typed).** Column shows committed
   area's bulletin from the data object; then add the typing reveal +
   cursor + hard completion timer (§10.1).
6. **The passage.** Sticky stage + pan mapping + commit logic with
   hysteresis; verify §10.10 (one current area) with an automated
   scroll-through, both directions.
7. **Instruments.** Compass needle from computed bearings (§10.5 audit) +
   counter; readings rolls (§6.6).
8. **Ceremonies.** Porthole (§6.9) + skeleton/static-tune (§6.12), each
   behind its fallback timers (§10.4).
9. **Ambient layer.** Breathing, mist, marching fronts — in that order,
   each with its off-screen pause and low-power cut (§14).
10. **Interactions.** Area fill/hover pairing (§6.10), buoy ping (§6.11),
    card tilt (§6.15), header states (§6.13).
11. **Gale system.** §6.7 pulse rationing + synopsis warnings (§10.7 red
    ration measured on screenshots).
12. **Reduced-motion build.** The stack; text-diff against the motion
    build (§10.2).
13. **Night watch.** Dark token set; verify no element hard-codes a light
    token.
14. **Performance pass.** §14 budgets measured on the reference device;
    apply the cut order if needed — and record what was cut in the build
    log, because a cut the next builder cannot see will be re-added.
15. **Final gate.** §10, all twelve items, in order, no partial credit.

*End of Theme 013 — The Shipping Forecast (expanded).*
