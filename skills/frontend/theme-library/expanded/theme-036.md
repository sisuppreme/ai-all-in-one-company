# 36. Monsoon Arrival — Expanded (v1 + v2)

> Expansion of theme #36 from `themes-026-050.md`, written directly to
> the full standard: the v1 10-part structure plus the v2 deepening
> layers (per-element choreography timelines, state matrices, breakpoint
> behaviour, edge cases, accessibility specs and token lists; per-theme
> component inventory, copywriting voice, three worked examples, scroll
> choreography map, performance budget, build-order checklist).
> Identity preserved exactly: the same concept, the same five palette
> anchors, the same two typefaces, the same nine signature elements —
> deepened, never redesigned — plus nine page-family elements.

## 1. Concept & world

Most websites hold one climate from the first pixel to the last. This
theme is a page with **weather that arrives**. The site opens in the
dry season: pale cracked earth, dust, a headline holding its breath.
As the visitor reads downward, the monsoon breaks over the page —
section by section the ground darkens, colour saturates, surfaces go
from matte to wet, and by the footer the whole page is lush, green and
still dripping. The scroll is not navigation here; it is the season
turning, and the visitor's reading *is* the rain's advance. Nothing on
the page is rained on decoratively: the photographs are the landscape
getting wet, the progress indicator is a rain gauge filling, the hero
sentence itself changes when the weather does — "the earth, waiting"
becomes "the earth, breathing" — because in this world copy is soil
and soil responds to rain.

The world is a complete meteorological vocabulary, not a skin. The
page has **the dry** (the opening state: cracked mud, heat shimmer,
figures held at their pre-season values), **the cloud band** (a dark
horizontal actor that crosses sections and announces that weather is
coming), **the rain moment** (one pinned passage, roughly 40% down the
page, where the first rain actually falls and the copy change fires),
**the wet front** (the darker leading edge that sweeps each section as
it is read, leaving the surface visibly rained-on behind it), **the
gauge** (the margin instrument that measures the visitor's rainfall in
millimetres), and **the soak** (the final state: saturated colour, wet
forest ground, droplets still running off the footer after the reading
is done). Every animated thing on the page is one of these six, or it
does not belong to the theme.

**The theme's one law: the rain is earned by reading, and every figure
is measured.** Saturation is a declared function of scroll progress
(§6.3) — never of time, never of hover, never random. The rain moment
fires once, at its pinned section, and is irreversible within the
session: a visitor who scrolls back up returns to ground that has
already been rained on, because rain does not un-fall. Rainfall
millimetres in the gauge are a stated conversion of page progress
(§6.5: the gauge's full scale is the season's real recorded rainfall
for the place the site is about, printed in the ledger §6.17), and
harvest or rainfall figures in §6.16 count to publisher-supplied
numbers with their source named in the caption — or they are not
printed at all. A Monsoon Arrival build that invents "214 mm of rain"
because the gauge needed a number has falsified the season, and the
quality gate (§10) fails it on sight. The copy change is bound by the
same law: the struck-through "waiting" must remain legible under its
rain line forever after (§6.2), because the page keeps its own
before-and-after as evidence.

**Arrival is the interaction model.** The visitor does not operate
this site; they witness a season change by reading through it. Their
acts are small and physical: they scroll and the front advances
(§6.4), they hover and a card's surface beads (§6.7), they click and a
raindrop ripples the button (§6.9), they watch the gauge fill (§6.5).
That is why the theme fits stories with a genuine before and after —
a season, a harvest, a restoration, a recovery, a launch after a long
wait — and why it curdles around anything that has no dry season to
leave behind.

**Best-fit sites and audiences.**

- Agriculture and food provenance: farms, tea and coffee estates,
  vineyards, spice growers — anywhere the year's story genuinely runs
  from dry waiting to wet abundance, and the rainfall figures are the
  estate's own records.
- Climate, water and environment storytelling: watershed restoration
  reports, reforestation journals, monsoon explainers, reservoir and
  river authorities publishing a season review.
- Travel and place writing about monsoon regions: Kerala, the Western
  Ghats, Bangladesh, northern Australia — journeys whose turning point
  is the day the rain came.
- Organisations reporting a recovery: a drought-relief programme's
  annual story, a rewilding project's first wet season, a community
  that waited out a dry year. The before/after must be real and dated.
- Launches after a long, public wait: a product, book or season
  announced as "arriving" — used once, for the arrival itself, not as
  a permanent skin.

**When NOT to use it.**

- For content with no before/after. If the material does not change
  state — a catalogue, a settings page, a reference manual — the rain
  is a costume on a filing cabinet, and the copy change has nothing
  true to say.
- For anything that must stay dry. Urgent, clinical or legal content
  (emergency information, medical instructions, compliance text) must
  not ask its reader to travel through weather to reach it; the
  theme's pace is a season's pace.
- Where the figures would be theatre. If the publisher will not
  supply real rainfall, harvest or recovery numbers with dates, the
  gauge and counters become props; use another theme.
- For short pages. The ramp needs room: below roughly six sections
  the season turns too fast to feel, and the rain moment lands before
  the dry has registered. A two-screen page has no monsoon.
- For repeat-visit utility. The arrival is a first-reading ceremony;
  a dashboard the same visitor opens daily would make them re-wait
  through the dry season every morning. Returning visitors in the
  same session keep the soaked page (§6.3), but a daily-use tool
  should not wear this theme at all.

## 2. Palette

Five anchors, inherited unchanged. The palette is one landscape at two
moments: three colours of the dry season (pale earth, cracked mud,
the first tentative green) and two of the wet (deep forest, new leaf).
The page's whole colour story is the ratio between them shifting as
the ramp (§6.3) advances: dry earth dominates the first viewport;
wet forest owns the footer. No sixth hue is admitted; the gauge's
water (§6.5) is a declared derivative of new leaf and first green,
never a blue imported from another theme.

| Token | Hex | Role | Usage ratio | Pairing & contrast notes |
|---|---|---|---|---|
| `--dry-earth` | `#D8C7A8` | The dry ground: opening page background, dry-section surfaces, card faces before the front passes | ~34% of pixels at load, falling to ~6% at the footer | Wet forest on it: **7.48:1** (AAA) — the footer's ink may letter the hero's ground. First green on it: **4.64:1**, the only green permitted for text on dry ground. New leaf on it: **1.52:1** — a glow and a fill only, never text at any size; a new-leaf word on dry earth is a gate failure (§10). |
| `--cracked-mud` | `#8A6D4B` | The dry structure: crack lines, dry headings' secondary tone, gauge housing, table rules in the dry chapters | ~14% of pixels | On dry earth only **2.90:1** — line-work, large display (≥24px) and texture only, never body text. Body text in the dry chapters is set in its darkened derivative `--mud-deep` `#5C4630` (**5.33:1** on dry earth). On wet forest 2.58:1 — banned there entirely; the wet chapters' structure is new leaf and dry earth. |
| `--first-green` | `#3F5A36` | The turning: the first green of the middle chapters — links and text-grade green on dry and mid grounds, the root-line's living segment (§6.6), gauge water's deep end | ~16% of pixels | On dry earth **4.64:1** (AA for text). On new leaf 3.05:1 — graphical use only. It is the hinge colour: the last colour of the dry palette that may carry words, and the first colour of the wet one. |
| `--wet-forest` | `#22392E` | The soaked ground: final-section and footer backgrounds, the cloud band's body, body text on dry grounds | ~26% of pixels by the footer | On dry earth **7.48:1** (AAA). Dry earth on it 7.48:1 and new leaf on it **4.91:1** — the two lettering colours of the wet chapters. It never appears above the rain moment except in the cloud band and in text: forest ground before the rain is a spoiler and a gate failure. |
| `--new-leaf` | `#7FB069` | The new growth: accents in the wet chapters, gauge water's lit surface, the root-line's growing tip, focus rings on wet grounds, the footer's dripping highlights | ~10% of pixels | On wet forest **4.91:1** (AA) — text permitted there only. On dry earth 1.52:1 and on first green 3.05:1 — fill, line and glow only. A build that sets a caption in new leaf on a pale ground has failed §10, however pretty it looks in the dry light. |

**Derived tokens (closed list).** `--mud-deep` `#5C4630` (dry-chapter
body text, 5.33:1 on dry earth); `--earth-pale` `#E9DCC2` (dry card
faces and the skeleton's unsoaked sheet, §6.15); `--forest-deep`
`#182A21` (the cloud band's underside and the footer's lowest band,
where dry earth letters it at 8.9:1); `--leaf-pale` `#A8CBA0` (wet-
chapter secondary text on wet forest, **6.92:1**); `--gauge-water`
`#4E8266` (the gauge's water body — a first-green/new-leaf midpoint,
declared here so no builder imports a blue); `--petrichor` `#6E5638`
(the struck "waiting" line and rain-line stroke of §6.2, 4.15:1 on dry
earth — graphical, never text). No other derivatives are permitted; a
colour not in this table or derivable from it by opacity over a named
ground does not ship.

**Dark-mode behaviour.** The theme does not invert. A
`prefers-color-scheme: dark` visitor is given **the page after
nightfall in the wet season**: grounds move one step down the ramp
(dry sections render at the ramp's 40% values, the footer at
`--forest-deep`), text pairs are re-declared from the same table
(dry earth and leaf-pale letter the dark grounds), and the dry
chapters keep their crack line-work in cracked mud at 40% opacity so
the before-state is still readable as *dry*, not merely *dark*. The
ramp, the rain moment and the copy change run identically. A build
that simply swaps background and text colours has not made a dark
mode; it has made a negative.

## 3. Typography

Two typefaces, inherited unchanged. **Newsreader** carries the
weather: display headlines, section titles, and — in its italic — the
theme's distinctive second voice, the *weather note*, the short
observational aside ("First clouds over the ridge, 4 June.") that
comments on the season as it turns. **Source Sans 3** carries the
record: body text, data, labels, forms, tables. The casting law is
absolute: Newsreader never sets a figure, a label or a form field;
Source Sans never sets a headline or a weather note. A page where a
rainfall figure appears in Newsreader has miscast its instruments as
poetry, and §10 fails it.

| Role | Face & cut | Size / line-height / tracking | Rules |
|---|---|---|---|
| Display (hero) | Newsreader, regular, optical size auto | clamp(44px, 7.2vw, 84px) / 1.02 / −0.01em | The hero line exists in two states (§6.2): "waiting" and "breathing" share this setting exactly, so the copy change never shifts a baseline. Never bold — Newsreader's weight is weather, not emphasis. |
| Section title | Newsreader, regular | clamp(30px, 4vw, 46px) / 1.08 / −0.005em | One per section, set in the ground's ink (mud-deep in dry chapters, dry earth on wet forest). |
| Weather note | Newsreader, italic | 17–19px / 1.45 / 0 | The italic is a dateline voice: every weather note carries a real date or a real place, or it is cut. Max 34 words. Never used for marketing copy — a weather note that sells something is a gate failure. |
| Body | Source Sans 3, regular | 17px / 1.62 / 0 (18px ≥1200px) | Measure 58–68ch in the lee of each section (§4). Dry chapters on `--mud-deep`; wet chapters on dry earth / leaf-pale over wet forest. |
| Caption / figure note | Source Sans 3, regular | 13.5px / 1.5 / 0.005em | Every figure's caption names its source and date (§6.16, §6.17). A caption without a source is an unpublished figure. |
| Data / gauge figures | Source Sans 3, semibold, tabular numerals | 14–28px by instrument / 1.2 / 0.01em | Tabular figures are mandatory wherever a number changes (gauge, counters) so digits never reflow the layout as they count. |
| Labels / apparatus | Source Sans 3, semibold, uppercase | 11.5px / 1.4 / 0.14em | Section kickers are apparatus, not headlines: "THE DRY SEASON", "THE RAIN MOMENT", "AFTER THE RAIN". The apparatus names the weather, never the marketing. |

**Type laws.**

1. **The two states of the hero line are set once.** "The earth,
   waiting" and "the earth, breathing" occupy the same box, same
   size, same line breaks at every breakpoint; the change (§6.2) is a
   strike and a substitution inside a fixed measure, never a reflow.
2. **Figures are Source Sans, always tabular, always sourced.** No
   exceptions for "display numbers" — a 64px rainfall figure is data
   wearing a bigger size, not a headline.
3. **Italic is a dateline.** Newsreader italic appears only in
   weather notes and in the struck first state of the hero line
   (§6.2). It is never used for emphasis inside body text.
4. **No exclamation marks.** The monsoon does not shout. The single
   permitted exception is a quoted voice in supplied content, marked
   as quotation.
5. **Dry text never lightens below its declared pair.** As the ramp
   darkens grounds (§6.3), text colours swap at the declared section
   boundaries (§4), not continuously — a paragraph whose ink colour
   is mid-transition is a paragraph nobody can read at some scroll
   position, and §10 tests the ramp's midpoint explicitly.

## 4. Layout language

The layout is a **descent through a watershed**. The page is a single
column of chapters arranged as the season's own chronology, and the
saturation ramp (§6.3) is drawn on the layout itself: grounds deepen
chapter by chapter, so a visitor who jumps to the footer has visibly
arrived in a different climate from the one they left at the top. The
structure has five named parts.

**The chapters.** Six chapter bands in fixed order: (1) *The Dry*
(hero + the waiting content), (2) *First Clouds* (signs, forecasts,
the cloud band's home), (3) *The Rain Moment* (the pinned passage,
§6.2 — exactly one per page), (4) *The Front Passes* (the main body,
each section swept by the wet front §6.4), (5) *The Soak* (results,
figures, the ledger §6.17), (6) *Still Dripping* (footer, §6.14). A
page may hold more sections inside a chapter, but chapters never
reorder and no page has two rain moments: a season breaks once.

**The lee.** Body content rests in a calm reading column of 58–68ch,
set against each chapter's ground, offset to the side opposite the
gauge (§6.5). Images sit in the lee's full width or break out to the
chapter's full width at chapter boundaries only — never mid-paragraph.
The crack (§6.6) runs through the dry chapters' open ground, never
through the lee's text column: damage is drawn on the land, not across
the words.

**The margin and the gauge.** On ≥1200px the right margin (fixed
72px rail) carries the rain gauge (§6.5) for the whole descent; the
left margin carries the crack/root line (§6.6) in the chapters where
it lives. Margins are instruments, not whitespace: anything placed in
them must measure or grow.

**Spacing rhythm.** An 8px base unit. Chapter padding is 96px top /
96px bottom in the dry chapters, growing to 128px in the wet chapters
— the page literally breathes wider as it gets wetter, a 4px-per-
chapter increase in section gap (24px → 40px) that the visitor feels
as lushness before they can name it. Card grids hold a 24px gutter at
all sizes. The cloud band (§6.10) is 18vh tall wherever it crosses —
the theme's one fixed weather dimension.

**Density rules.** Dry chapters are sparse: at most 3 content blocks
per viewport, wide pale ground between them — scarcity is the dry
season's texture. Density rises one step per chapter to the soak's
maximum of 6 blocks per viewport. A dry chapter as crowded as the
soak has broken the season's arc and §10 fails it. Whitespace in this
theme is not empty; in the dry chapters it is *thirst*, and it is
spent deliberately.

**Ground steps (the layout's half of the ramp).** Continuous filter
saturation belongs to images (§6.3); grounds move in six declared
steps, one per chapter, so text contrast is always at a tested value:
step 0 `#D8C7A8` (the Dry — text `--mud-deep` 5.33:1), step 1
`#C4B28D` (First Clouds — text `--mud-deep` 4.6:1), step 2 `#8A8262`
(the Rain Moment's mid-transition ground — text in wet forest at
5.1:1), step 3 `#55663F` (Front Passes opens — text switches to dry
earth, 4.7:1), step 4 `#33503C` (late Front / the Soak opening — dry
earth 6.3:1), step 5 `#22392E` (the Soak and footer — dry earth
7.48:1). Text colour swaps
exactly at the chapter boundary where its pair crosses AA; the swap
is a hard cut at the boundary, dressed by the wet front's sweep
(§6.4) so it reads as weather, not as a theme toggle.

## 5. Full motion system

One shared `requestAnimationFrame` loop drives every scrubbed value
on the page — the ramp (§6.3), the wet front (§6.4), the gauge
(§6.5), the root (§6.6) — with a single lerp factor of **0.12**; no
element runs its own scroll listener or its own loop. Five named
easings, and no others: `--ease-downpour` `cubic-bezier(0.55, 0, 1,
0.45)` (things that fall: rain streaks, droplets); `--ease-soak`
`cubic-bezier(0.25, 0.6, 0.2, 1)` (things that darken and saturate:
the front, the title's wetting); `--ease-drip`
`cubic-bezier(0.34, 1.3, 0.64, 1)` (things that bead and release:
droplets, the meniscus); `--ease-glide` `cubic-bezier(0.22, 0.9,
0.24, 1)` (the scroll's own wet glide and the cloud band's travel);
`--ease-crack` `cubic-bezier(0.85, 0, 0.15, 1)` (the crack's draw —
long hesitation, sudden run). Every motion term in the standard
vocabulary, translated into this theme's weather:

- **Scroll-triggered reveals.** Sections do not fade up; they are
  *rained on*. The wet front (§6.4) sweeps each section on entry —
  700ms `--ease-soak` — and the section is at full contrast from its
  first painted pixel underneath the front; the front is a darkening
  wash, never a mask that hides content awaiting reveal.
- **Scroll-driven / scrub animation.** The saturation ramp (§6.3) is
  the page's master scrub: image saturation 0.55 → 1.05 and contrast
  1.0 → 1.06 mapped to total document progress, lerped in the shared
  loop. The gauge (§6.5) and root (§6.6) scrub from the same progress
  value, so the whole page agrees about how much rain has fallen at
  every scroll position.
- **Parallax.** Three rates only: cloud band 0.86×, grounds 1.0×,
  gauge/root instruments 1.0× (they are fixed margin instruments and
  do not parallax at all). The dry chapters' crack field parallaxes
  at 0.94× against the lee so the ground feels deeper than the text.
  No other parallax exists; a fourth rate is slop.
- **Pinned sections.** Exactly one: the rain moment (§6.2), pinned
  for 160vh of scroll while the rain falls and the copy changes. The
  gauge is sticky, not pinned — it never traps the scroll.
- **Smooth scrolling.** The page's scroll behaviour changes state at
  the rain moment: before it, native scroll (the dry season is dusty
  and resistant — no smoothing is applied, deliberately); after it, a
  light lerp glide (`--ease-glide`, lerp 0.12 in the shared loop) is
  applied to anchor jumps and programme-driven scroll only — the
  visitor's own wheel/touch scroll is never hijacked at any point in
  either season.
- **Progress indicator.** The rain gauge (§6.5). There is no bar,
  percentage or "n of N" anywhere on the page; progress is rainfall.
- **Staggered + masked reveals.** The first rain (§6.1) is the page's
  one masked reveal: the cloud band wipes across the hero (1200ms)
  and the streaks stagger at 8ms intervals behind it. Card groups
  enter under their section's wet front with a 90ms stagger in
  reading order (§6.12). Nothing else staggers.
- **Kinetic typography.** Refused, with one exception that is not
  kinetic: the hero line's substitution (§6.2) — words are struck and
  replaced once, at reading pace, never animated letter by letter.
  Type in this theme is soil and record; it does not dance.
- **Marquee.** Refused. Nothing in a monsoon moves sideways forever.
  The cloud band crosses once per chapter boundary and stops.
- **Counters.** Rainfall and harvest figures (§6.16) count once, on
  entry, in tabular Source Sans, at the stated rates — and only to
  figures the publisher supplied with a source (§1's law).
- **SVG line-draw.** The crack and the root (§6.6): one continuous
  path drawn across two seasons. The gauge's meniscus line is the
  only other drawn line.
- **Image scale-in-frame.** Photographs sit in fixed frames and scale
  1.06 → 1.0 as they cross the viewport centre, scrubbed by the
  shared loop, *under* the saturation ramp — the landscape both
  settles and wets as it is read (§6.3).
- **Hover / magnetic / tilt micro-interactions.** Hover beads a card
  (§6.7); hover on a gauge tick reads its millimetres (§6.5). No
  magnetic pull, no tilt: wet ground does not lean toward the
  visitor. Buttons ripple on click (§6.9).
- **Custom cursor.** Refused — the standing rule. The system cursor
  is the only cursor; there is not even a themed variant.
- **Skeleton loading.** The cracked sheet (§6.15): dry, pale, cracked
  placeholders that soak to content — the skeleton is the page before
  rain, never grey bars.
- **Page transitions.** The cloud-wipe (§6.15): a cloud band crosses,
  the page changes under its cover, the band leaves from the other
  side — 900ms total, and plain navigation without it whenever JS or
  the band is unavailable.
- **Reduced motion.** The page loads at the final state (§6.3's
  static soaked page): full saturation, copy already "breathing",
  gauge full, root grown, no rain, no shimmer, no glide. This is the
  spec's own ruling inherited from the original entry, and it is a
  complete page, not a diminished one.
- **Ambient loops.** Exactly two, both post-rain: the footer's
  dripping (§6.8, one droplet every ~4s) and the gauge meniscus's
  wobble at chapter boundaries (§6.5). The dry chapters' one ambient
  is the heat shimmer over the hero headline (§6.11) — it dies the
  moment the rain falls and never returns.

## 6. Signature elements

### 6.1 First rain pass — the rain falls on the headline

- **What & why.** The theme's opening weather, performed once, on the
  hero. A dark cloud band slides across the hero as a mask wipe and
  ~40 thin rain streaks fall a single time while the headline darkens
  from dry-earth tones to wet-soil tones — the title is the first
  ground the monsoon touches. It belongs because every later wetting
  on the page (the front, the ramp, the footer drip) is a larger
  version of this first one; the hero teaches the page's physics in
  1.8 seconds. It happens exactly once per page load. Rain that falls
  on a loop is a screensaver.
- **Structure.** The hero (§6.11) carries three JS-inserted layers
  above its ground and below its text's reading order in the DOM: a
  `.cloud-band` div (18vh tall, `--forest-deep` with a soft lower
  edge, full bleed), an SVG `.rain-field` of 40 line segments (1px,
  `--petrichor` at 55% opacity, lengths 26–44px, each pre-rotated 4°
  — monsoon rain slants), and a colour transition on the headline
  itself (its ink is a CSS custom property the pass animates). All
  layers are `aria-hidden`, `pointer-events: none`, and inserted only
  when JS runs and motion is allowed — the no-JS hero is complete
  without them.
- **Motion spec.** Trigger: page load, gated on `fonts.ready` (the
  rain must fall on the *set* headline), watchdog 900ms (§ below).
  t+0: cloud band enters from the left, mask-wiping across the hero
  over 1200ms `--ease-glide`. Streaks begin at t+350ms as the band's
  leading edge passes the headline: each streak falls 600ms
  `--ease-downpour` from 12vh above its ground point to the hero's
  lower third, staggered 8ms apart in a left-to-right sweep that
  follows the band (streak *n* starts when the band's edge reaches
  its x position — the stagger is spatial, not arbitrary). Headline
  ink darkens across t+400–1600ms `--ease-soak` (dry-earth-toned
  `--mud-deep` → wet forest). At t+1800ms the band exits right, the
  rain layer is removed from the DOM, and the hero is at rest in its
  post-first-rain state: headline wet, ground still dry — the season
  has announced itself, not finished.
- **Choreography timeline (v2).** t+0 load → fonts ready (or 900ms
  watchdog) → t+80ms band enters → t+350ms first streaks under the
  band's edge → t+400ms headline begins to darken → t+950ms last
  streak falls → t+1280ms band fully across → t+1600ms headline at
  wet-soil ink → t+1800ms band gone, rain layer removed, hero at
  rest. The heat shimmer (§6.11) stops at t+350ms — the shimmer and
  the rain never share a frame.
- **State matrix (v2).** *Rest (pre-load / no-JS):* the composed dry
  hero, headline in mud-deep, fully readable. *Passing:* 1800ms,
  non-interactive, identical on desktop and touch. *Hover / focus:*
  no effect; weather is not a control and hovering never re-fires it.
  *Active:* n/a. *Scrolled-past:* if the visitor scrolls during the
  pass, it completes off-screen or is cut at the hero's exit,
  whichever is sooner; it never follows them. *Disabled:*
  reduced-motion and no-JS both rest (below).
- **Content merge.** The rain falls *on the headline* and the
  headline's own ink is what darkens — the animation's object is the
  page's first content, not a backdrop behind it. Remove the headline
  and there is nothing for the first rain to touch; remove the rain
  and the hero still says everything it said, merely unannounced.
- **Failure fallback.** `fonts.ready` unresolved by 900ms → the pass
  fires anyway, centred on the laid-out headline. SVG layer fails to
  build → the band and the ink-darkening still run (they are a div
  and a property). All three fail → the dry hero stands, complete.
  The watchdog is structural: every layer is inserted, so every
  layer's absence is survivable by construction.
- **Reduced-motion variant.** No band, no streaks, no darkening
  animation: the headline simply stands in its post-rain wet-forest
  ink from first paint, as part of the static soaked page (§5).
- **Breakpoints (v2).** ≥1200px: 40 streaks, band 18vh as specced.
  768–1199px: 32 streaks, band 15vh. <768px: 22 streaks, streak
  length 20–32px, total pass compressed to 1400ms — a phone's hero is
  short and the weather must not delay the reading.
- **Edge cases & failure modes (v2).** *bfcache restore:* the pass
  does not re-fire (the page was never left; session state §6.3
  already holds the season). *Hero shorter than viewport on a tall
  phone:* streaks fall to the hero's own lower third, measured, not
  to 100vh. *Slow device:* if the first streak frame measures >32ms,
  streaks halve to 20 and the band carries the pass alone.
  *Headline in two lines:* darkening applies to both lines as one
  property; streaks target the block, not a line.
- **Accessibility spec (v2).** Purely decorative, `aria-hidden`; the
  headline is ordinary DOM text, readable from first paint in
  mud-deep (5.33:1) and after darkening in wet forest (7.48:1) — at
  no frame of the transition does its contrast drop below 4.5:1,
  because both endpoints and the soak curve between them stay on the
  dark side of the ground. Nothing is announced; nothing is
  focusable.
- **Performance budget & mobile variant.** 40 line segments, one
  transform each, compositor-only; band is one transformed div; ink
  transition is a single custom-property animation. ≤0.5ms script per
  frame. Mobile: the 22-streak variant; the rain layer is built after
  first paint so it never competes with the hero's text.
- **Tokens consumed (v2).** `--forest-deep`, `--petrichor`,
  `--mud-deep`, `--wet-forest`, `--ease-glide`, `--ease-downpour`,
  `--ease-soak`, `--rain-count` (40), `--rain-fall` (600ms),
  `--rain-stagger` (8ms), `--band-h` (18vh).

### 6.2 The copy change — "waiting" is struck, "breathing" remains

- **What & why.** The theme's thesis, enacted on the page's own
  words. In the pinned rain-moment chapter, the hero line "the earth,
  waiting" is struck through by a single rain line and replaced by
  "the earth, breathing". It belongs because it is the one moment the
  page admits, in its own text, that the weather changed it — the
  anti-slop detail the original entry named the petrichor note. Every
  other element is weather; this one is *evidence*. It fires once, at
  the pin, and never reverses within the session: scrolling back up
  shows the struck line and its replacement, settled, because the
  rain has already fallen (§1's law).
- **Structure.** Inside the pinned rain-moment section (§4, chapter
  3): a `.copy-change` block holding both states in one fixed box
  (§3's law 1). The first state is a `<span class="was">` containing
  "the earth, waiting" in Newsreader italic, with an SVG rain-line
  (a single 2px `--petrichor` stroke, slanted 4° like §6.1's rain)
  drawn across it. The second state, "the earth, breathing" in
  Newsreader regular, sits in the same line box, revealed beneath the
  strike. The struck original is never removed from the DOM, never
  `display: none`, and remains legible at 60% opacity after the
  change — the page keeps its before-state as a permanent footnote to
  its after-state. A visually hidden text alternative gives screen
  readers the settled sentence plus the history ("The earth,
  breathing — before the rain: the earth, waiting").
- **Motion spec.** Trigger: the pin's scrub progress crossing 0.45
  of its 160vh travel (shared loop). Rain-line draws across the
  struck words: 500ms `--ease-crack` (hesitation, then the run —
  the strike lands like weather, not like a pen). At the draw's
  completion, "waiting" settles to 60% opacity over 300ms
  `--ease-soak` while "breathing" rises from the line's baseline
  (translateY 8px → 0, opacity 0 → 1) over 450ms `--ease-soak`,
  staggered so the replacement is fully present at pin progress
  0.62. Simultaneously the pinned section's own rain (a denser
  field, 60 streaks, §6.1's construction) falls behind the block
  across the whole pin. After progress 0.62 nothing in the block
  moves again, at any scroll position, in either direction.
- **Choreography timeline (v2).** Pin enters → progress 0–0.45:
  section rain begins, ground at ramp step 2 → 0.45: rain-line draw
  starts → +500ms: strike complete → +550ms: "breathing" begins its
  rise → progress 0.62 / +1000ms: settled state reached → pin
  releases at 160vh with the block in its final state, which it
  keeps for the rest of the session and on any return scroll.
- **State matrix (v2).** *Rest (before the pin):* "waiting" at full
  opacity, no strike, "breathing" present in DOM but visually
  unrevealed — desktop and touch identical. *Changing:* the 1000ms
  sequence above; non-interactive. *Settled:* strike drawn, original
  at 60%, replacement at full — permanent. *Hover / focus:* no
  effect; the block is a statement, not a control. *Scrolled-past:*
  settled state persists (one-way law). *Disabled:* reduced-motion /
  no-JS show the settled state from first paint (below).
- **Content merge.** The animation's object is the sentence itself,
  and the sentence is the page's thesis — there is no content beneath
  the effect for it to decorate. The strike is drawn *through* the
  words it retires; the replacement occupies the retired words' own
  line.
- **Failure fallback.** The settled state is the DOM default: JS arms
  the pre-change state only when the pin machinery initialises
  successfully, and a 1200ms watchdog after the section's first entry
  forces the settled state if the scrub stalls. With JS off, the
  visitor reads "the earth, breathing" with the struck "waiting"
  beneath it — the full meaning, statically.
- **Reduced-motion variant.** The settled state from first paint; the
  pin itself is released (the section scrolls as ordinary content,
  §13). No draw, no rise.
- **Breakpoints (v2).** ≥1200px: as specced, line set at display size
  (§3). 768–1199px: pin travel shortens to 140vh. <768px: pin travel
  120vh, strike draw 420ms, and the block's two states stack (struck
  line above, replacement below) rather than sharing a line box,
  because at phone measure the substitution reads clearer stacked —
  the fixed-box law (§3) is kept *within* each line.
- **Edge cases & failure modes (v2).** *Jump scroll past the pin*
  (anchor link, find-in-page, restored scroll position): the block is
  settled instantly — the catch-up rule of §13; a visitor must never
  land below the rain moment and scroll up to find the earth still
  "waiting". *Very fast scroll through the pin:* the sequence
  compresses (draw 200ms, rise 200ms) but still completes in order;
  it never skips the strike — the strike is the meaning. *Session
  restore mid-page:* settled state, via the session flag (§6.3).
  *Longer supplied headline* (a translated or client-edited line):
  the strike path is measured from the rendered span at build/init,
  never hard-coded; if the line wraps to three lines, the strike
  draws across the final word only and §10's gate flags the build
  for copy review.
- **Accessibility spec (v2).** The visual strike is `aria-hidden`;
  the accessible text is the settled sentence with its history (see
  Structure), so a screen reader meets exactly the meaning sighted
  readers end with. Contrast: struck original at 60% opacity over
  the chapter ground measures 3.4:1 — it is retained history, not
  reading matter, and the live sentence beside it is 7.48:1; the
  gate (§10) requires the *replacement* at AA and the original
  legible, which 3.4:1 at display size satisfies for large text.
  Nothing focusable; the pin never traps focus (§13's pin law).
- **Performance budget & mobile variant.** One SVG path draw, two
  opacity/transform animations, one rain field shared with §6.1's
  construction. ≤0.3ms script per frame inside the shared loop.
  Mobile: the stacked variant above; rain field 36 streaks.
- **Tokens consumed (v2).** `--petrichor`, `--wet-forest`,
  `--mud-deep`, `--ease-crack`, `--ease-soak`, `--strike-dur`
  (500ms), `--settle-dur` (450ms), `--pin-travel` (160vh).

### 6.3 The saturation ramp — the landscape gets wet

- **What & why.** The page's master process: every photograph's
  colour deepens as the monsoon advances — saturation 0.55 → 1.05,
  contrast 1.0 → 1.06, scrubbed to total page progress. It belongs
  because it is the theme itself stated as a single function: the
  same pictures, monsoon applied. A visitor who sees only one image
  twice — pale near the top, saturated near the footer — has
  understood the entire site. The ramp also governs the session's
  memory: once the rain moment (§6.2) has passed, the ramp's floor
  rises permanently, so returning to the top shows a landscape that
  has been rained on and stays rained on (§1's one-way law).
- **Structure.** Every content image carries `data-ramp` and sits in
  a fixed-aspect frame (§5's scale-in-frame runs inside the same
  frame). The shared loop writes one custom property, `--ramp`
  (0 → 1), on the root; image filters are declared once in CSS as
  `saturate(calc(0.55 + 0.5 * var(--ramp))) contrast(calc(1 + 0.06 *
  var(--ramp)))`, so the loop performs a single property write per
  frame for the entire page's imagery — no per-image JS. Ground
  colours do **not** ride this property; they step per chapter (§4),
  because text contrast must stay at tested values.
- **Motion spec.** `--ramp` = lerped document progress (shared loop,
  lerp 0.12), with two amendments. (1) *The floor:* before the rain
  moment, ramp maps progress 0 → 0.5 across chapters 1–3; after
  §6.2 settles, the floor locks at 0.5 and progress through chapters
  4–6 maps 0.5 → 1. Scrolling back above the rain moment after it
  has fired shows ramp 0.5, never less — the one-way amendment.
  (2) *Per-image clamp:* images in the dry chapters never exceed
  ramp 0.35 locally (their CSS caps the property), so the hero's
  landscape cannot look wet before its own rain (§6.1) has fallen —
  the global value is clamped per chapter by a `data-ramp-cap`.
- **Choreography timeline (v2).** Continuous scrub, so the timeline
  is a map: progress 0 → ramp 0 (images at 0.55 saturation — visibly
  thirsty) → rain moment fires → floor locks 0.5 → footer reached →
  ramp 1 (1.05 saturation — the same photographs, drenched).
  Scrolling up after the lock: ramp falls only to 0.5. First frame
  after load: ramp is initialised from the restored scroll position
  before first paint wherever possible, so a mid-page reload never
  flashes the dry state.
- **State matrix (v2).** *Rest (top, pre-rain):* ramp 0, dry images.
  *Scrubbing:* lerped, both directions within the current floor.
  *Post-rain rest:* floor 0.5 at the top, 1.0 at the footer.
  *Hover / focus:* no effect — the ramp is climate, not a control.
  *Scrolled-past:* per the map. *Disabled:* no-JS and reduced-motion
  render `--ramp: 1` statically (below).
- **Content merge.** The filter is applied to the photographs
  themselves — the content *is* the landscape, and the ramp is its
  weather. There is no overlay, tint layer or backdrop involved; the
  same image element is pale, then wet.
- **Failure fallback.** Filters are enhancement-only over fully
  legible images: if the loop never runs, images render at the
  browser's natural saturation (equivalent to ramp ≈ 0.8) and the
  page is complete. If CSS `calc()` inside `saturate()` is
  unsupported, the filter declaration is dropped wholesale by the
  parser and images are natural — again complete. The DOM default is
  never the desaturated state: desaturation is applied only by the
  armed ramp, so a stalled page can never strand the landscape in
  artificial drought.
- **Reduced-motion variant.** `--ramp: 1` from first paint; the whole
  page is the soaked page (§5). No scrub, no floor logic.
- **Breakpoints (v2).** Identical mapping at all sizes; on <768px
  the lerp rises to 0.16 so the ramp keeps up with faster thumb
  scroll and never lags a full chapter behind the reading position.
- **Edge cases & failure modes (v2).** *Images added late* (lazy
  load below the fold): they inherit the root property — a photograph
  loaded at the footer arrives already saturated, correctly, with no
  per-image catch-up. *Print:* filters print at the value held when
  printing starts; the print stylesheet pins `--ramp: 1` so the
  paper copy is the finished season. *User prefers contrast:*
  `prefers-contrast: more` pins contrast at 1.06 and halves the
  saturation swing (0.75 → 1.05) so the ramp never lowers figure/
  ground separation for anyone. *Battery-saver / loop throttling:*
  the ramp snaps to the mapped value on the loop's return — a scrub
  state, never a catch-up animation.
- **Accessibility spec (v2).** Alt text is unaffected by the filter;
  no information is carried by saturation alone — every image's
  caption (§3) states in words what the photograph shows, and the
  season's state is always also stated by the apparatus ("THE DRY
  SEASON" / "AFTER THE RAIN"). Images that are themselves evidence
  (a chart, a document scan) are excluded from the ramp by
  `data-ramp="off"` — the theme is not for content whose colour is
  testimony (§1), and §10 audits the exclusion list.
- **Performance budget & mobile variant.** One custom-property write
  per frame; filter cost is the browser's compositor on
  already-rendered images. Cap: at most 12 ramped images per page;
  beyond that, later images ship pre-saturated variants instead of
  live filters (build-time decision, §15). Mobile: identical, lerp
  0.16 as above.
- **Tokens consumed (v2).** `--ramp`, `--sat-min` (0.55),
  `--sat-max` (1.05), `--con-max` (1.06), `--loop-lerp` (0.12).

### 6.4 Wet front sweep — every section gets rained on

- **What & why.** Sections in this theme do not appear; they are
  rained on, in reading order. As a section enters, a darker wet edge
  — a gradient band ~18vh tall — sweeps down it, and the surface
  behind the edge is visibly darker, permanently: the section's
  ground steps from its dry value to its chapter's wet value (§4)
  under the front's cover. It belongs because it is the ramp (§6.3)
  made local and legible: the visitor watches the exact line where
  dry becomes wet cross the words they are about to read, once per
  section, and the page's before/after stops being a global filter
  and becomes a place.
- **Structure.** Each `<section data-front>` carries a `.wet-front`
  child: an absolutely positioned band, height 18vh, background a
  vertical gradient from transparent through `--forest-deep` at 88%
  opacity (its leading lower edge) to transparent, `pointer-events:
  none`, clipped to the section. The section's ground is two stacked
  layers — dry ground beneath, wet ground above at opacity 0 — and
  the front's passage is synchronised with the wet layer's opacity
  rising behind the band's edge, so the darkening appears to be
  *caused* by the band crossing. Text sits above both ground layers
  at all times, at its final colour (§3 law 5): the front darkens
  ground, never words.
- **Motion spec.** Trigger: section's top crossing 75% of viewport
  height, fired once per section per session (the session's soaked
  set, §6.3). The band travels the section's full height over 700ms
  `--ease-soak` (sections taller than 200vh: 1100ms), written by the
  shared loop as a scrub tied to the section's entry progress, so a
  visitor who scrolls slowly sees the front keep pace with their
  reading and a fast scroller sees it complete without queueing.
  Wet-layer opacity rises in the band's wake: at any moment, ground
  above the band's edge is wet (opacity 1), below it dry (0) — a
  hard horizon with a 6vh soft shoulder. On completion the band is
  removed and the wet layer is simply the ground.
- **Choreography timeline (v2).** Section top at 75% vh → t+0 band
  enters at the section's top edge → t+350ms band at midpoint, upper
  half wet → t+700ms band exits the section's foot, ground fully at
  its wet step → section added to the session's soaked set; on any
  later visit to this section (either scroll direction) it is wet
  from first visibility, no band, no sweep.
- **State matrix (v2).** *Rest (unvisited):* dry ground, no band —
  desktop and touch identical. *Sweeping:* 700–1100ms, scrub-paced.
  *Wet (visited):* permanent for the session. *Hover / focus:* no
  effect; focus entering an unvisited section fires its front
  instantly (a keyboard visitor must never read across a moving
  horizon — see Accessibility). *Scrolled-past without firing*
  (jump scroll): the section is wet instantly (catch-up, §13).
  *Disabled:* no-JS / reduced-motion sections render at their wet
  step from first paint (below).
- **Content merge.** The front crosses the section's own ground and
  the darkening it leaves is the section's own ground colour
  changing — the weather happens to the content's surface, not in a
  layer above the words. The band itself carries no text and covers
  no text at full opacity at any frame (its peak over the text
  column is capped, Edge cases).
- **Failure fallback.** Grounds are ordinary CSS backgrounds: if the
  loop or the band fails, sections render on their chapter's wet
  step (the DOM default is the wet layer at opacity 1; JS arms the
  dry-first state only on successful init, per section, with a
  1000ms watchdog from first visibility that forces the wet state).
  A section can therefore never be stranded dry-and-unreadable, and
  never hidden at all — the front governs colour, not visibility.
- **Reduced-motion variant.** No band, no sweep: sections are at
  their wet step from first paint (the soaked page, §5).
- **Breakpoints (v2).** ≥1200px: band 18vh as specced. 768–1199px:
  band 15vh, sweep 650ms. <768px: band 12vh, sweep 600ms, and the
  front fires at 85% viewport crossing (later, closer) so a phone
  section is mostly on screen before its weather arrives.
- **Edge cases & failure modes (v2).** *Band over text:* the band's
  gradient over the lee's text column is capped at 55% opacity (the
  full 88% applies only over open ground and image zones — build-time
  zoning, §15), so ink contrast never falls below its declared pair
  mid-sweep. *Short sections (<40vh):* the sweep compresses to
  450ms and the band to 10vh so the front reads as a pass, not a
  flood. *Two sections entering together* (fast scroll): fronts run
  in parallel, each on its own ground; no queue, no stagger — rain
  does not wait its turn. *Scrolling back up mid-sweep:* the sweep
  completes regardless (one-way law); the band never retreats.
- **Accessibility spec (v2).** The band is `aria-hidden` decoration;
  the ground change is never the sole carrier of meaning (the
  chapter apparatus names the weather in text). Focus-into-section
  forces the instant wet state (above) so focus is never inside a
  moving colour field. Contrast at every frame: text pairs are the
  declared chapter pairs (§4) because text colour swaps at the
  boundary the front performs — mid-sweep, text sits on whichever
  ground its pair was declared for, and the zoning cap keeps the
  transient dip above 4.5:1 (audited in §10).
- **Performance budget & mobile variant.** One transform + one
  opacity per active front, inside the shared loop; at most 2 fronts
  active concurrently (a third section entering defers its band
  until a slot frees, its ground still stepping instantly). Mobile:
  the 12vh / 600ms variant above.
- **Tokens consumed (v2).** `--forest-deep`, `--ease-soak`,
  `--front-h` (18vh), `--front-dur` (700ms), `--front-peak` (0.88),
  `--front-text-cap` (0.55).

### 6.5 Rain gauge progress — progress is measured rainfall

- **What & why.** The page's only progress indicator, and the theme's
  thesis as an instrument: a gauge in the margin that fills with
  blue-green water as the visitor reads, marked in millimetres, its
  full scale the season's real recorded rainfall for the place the
  site is about. It belongs because progress in this world is not a
  percentage of a document — it is the quantity the whole page exists
  to deliver, accumulating beside the reading like weather beside a
  window. When the gauge is full, the visitor has read the season
  and the season has, measurably, arrived.
- **Structure.** A fixed rail in the right margin (≥1200px; §4):
  a 10px-wide vertical tube (`--gauge-water` fill over a
  `--cracked-mud` housing at 30% opacity), height 46vh, centred
  vertically, with tick marks and mm labels at 0 / 25 / 50 / 75 /
  100% of full scale in tabular Source Sans (§3), and a meniscus
  line (2px, `--new-leaf`) at the water's surface. The full-scale
  figure is real data printed in the ledger (§6.17) — e.g. "Gauge
  full = 412 mm, the season's recorded rainfall at the estate gauge,
  1 June – 30 September" — and the current reading is a real DOM
  element (`.gauge-now`, "137 mm") updated at chapter boundaries.
  The whole instrument is one SVG + one text node; the fill is a
  rect whose height the shared loop writes.
- **Motion spec.** Fill height is scrubbed to document progress via
  the shared loop (lerp 0.12), mapped through the same floor logic
  as the ramp (§6.3): before the rain moment the gauge may fill
  only to 8% — anticipation, the first spots in an empty gauge —
  because a gauge that fills during the dry chapters is lying about
  rain that has not fallen. At the rain moment the mapping unlocks
  and progress maps 8% → 100% across chapters 3–6. At each chapter
  boundary the meniscus wobbles once: ±3px, 600ms `--ease-drip`, as
  if the instrument were tapped. The mm readout changes only at
  chapter boundaries (never mid-scroll — an instrument that flickers
  is not trusted), rounding to the whole millimetre computed from
  the declared full scale.
- **Choreography timeline (v2).** Scrubbed map: load → gauge at 0mm,
  dry → first clouds → 8% cap reached, meniscus still → rain moment
  fires → unlock → each chapter boundary: readout steps to its
  computed mm, meniscus wobble 600ms → footer → gauge full, readout
  at full scale, one final wobble, then stillness — a full gauge
  does not slosh.
- **State matrix (v2).** *Rest (dry chapters):* fill ≤8%, readout at
  its computed value. *Filling:* scrubbed, both directions within
  the unlocked range — scrolling up after the rain moment lowers the
  water (the gauge measures *reading*, honestly, in both
  directions; the one-way law governs ground and copy, not this
  instrument). *Full:* at the footer. *Hover:* hovering a tick
  highlights it and the readout shows that tick's mm (a reading
  aid, §5). *Focus:* the gauge is not focusable; its information is
  duplicated in the chapter apparatus text ("Rain so far: 137 mm"
  in the soak chapter's kicker line — see Accessibility).
  *Disabled:* no-JS / reduced-motion show the gauge full with the
  full-scale readout (the soaked page).
- **Content merge.** The gauge measures the page's own subject with
  the page's own number: its full scale is the season's real
  rainfall, printed and sourced in the ledger, and its reading is a
  true function of how much of the season the visitor has read.
  Remove the site's rainfall figure and the gauge has nothing honest
  to measure — which is precisely §1's when-NOT-to-use test.
- **Failure fallback.** The DOM ships the gauge full (soaked
  default); JS arms the empty start and the scrub only on loop
  init. A stalled loop leaves a static gauge at whatever height —
  decoration degraded, information intact, because the readout text
  and the full-scale figure are real DOM text regardless.
- **Reduced-motion variant.** Gauge full, readout at full scale,
  no wobble, no scrub (the soaked page, §5).
- **Breakpoints (v2).** ≥1200px: margin rail as specced. 768–1199px:
  the gauge leaves the margin and becomes a slim horizontal tube
  (height 8px, width 100%) fixed under the header (§6.10), ticks at
  the same fractions, readout at its right end. <768px: horizontal
  tube, ticks unlabelled except 0 and full scale, readout retained —
  a phone gauge keeps its number and loses its furniture, never the
  reverse.
- **Edge cases & failure modes (v2).** *Full scale missing from the
  supplied data:* the gauge is not built (§1's law); the page ships
  without a progress indicator rather than with an invented one,
  and §10 records the omission as a content failure, not a design
  choice. *Very short page:* the gauge is omitted for the same
  reason §1 refuses short pages. *Resize:* tube height re-measures,
  fill re-maps proportionally on the next frame — no animation.
  *Print:* gauge prints full, with its full-scale caption.
- **Accessibility spec (v2).** The SVG is `aria-hidden`; the reading
  is real text, present in the chapter apparatus at every chapter
  boundary (so the information exists in reading order, not only in
  a fixed margin a screen reader may never visit), and the soak
  chapter carries the final figure in its body. Tick hover is an
  enhancement; every tick's value is also printed in the ledger
  table (§6.17). Contrast: mm labels in `--mud-deep` on dry ground
  (5.33:1) and dry earth on wet forest (7.48:1) as the page descends
  — the rail's labels swap with the chapter steps like all text
  (§3 law 5).
- **Performance budget & mobile variant.** One rect height write per
  frame in the shared loop; the wobble is one transform. Negligible.
  Mobile: the horizontal variant above.
- **Tokens consumed (v2).** `--gauge-water`, `--new-leaf`,
  `--cracked-mud`, `--mud-deep`, `--ease-drip`, `--gauge-cap-dry`
  (0.08), `--wobble-dur` (600ms), `--loop-lerp` (0.12).

### 6.6 Crack and root — one line, two seasons

- **What & why.** A single continuous SVG line tells the page's whole
  story in the margin. In the dry chapters it is a crack: it draws
  itself across the hero's dry earth and runs down the left margin,
  branching the way dry ground branches. At the rain moment the same
  line — from the crack's own endpoint — becomes a root: it greens,
  thickens almost imperceptibly, and grows downward through the wet
  chapters, putting out one rootlet per section passed. Damage and
  growth as one unbroken line is the theme's argument drawn instead
  of written: the crack is where the water got in, and the root is
  what the water did next. It belongs because no other element so
  completely refuses to be decoration — it is a diagram of the
  content's own ground, drawn through it.
- **Structure.** One SVG path in the left margin rail (desktop) /
  page edge (mobile), spanning the full document height in segments
  per chapter, positioned against the lee. The dry segment is drawn
  in `--cracked-mud` 2px with two authored branch paths; the wet
  segment continues from the identical endpoint coordinate in
  `--first-green` 2.5px, with rootlet branches (short 14–22px paths)
  at each section boundary of chapters 4–6. Path lengths are measured
  at init (`getTotalLength`) and drawn via `stroke-dashoffset`
  written by the shared loop. The endpoint continuity is a build
  rule, checked in §10: the root's first point is the crack's last
  point, to the pixel.
- **Motion spec.** The crack draws across the hero over 900ms
  `--ease-crack` on first entry (hesitation at 60% of its length,
  then the sudden run — the easing is the sound of ground giving
  way). Through chapters 1–2 the crack's margin segment extends
  scrubbed to progress. At the rain moment the line pauses (the
  pin's duration is its held breath); from chapter 4 the root grows
  scrubbed — its drawn length maps section progress, each rootlet
  drawing over 300ms `--ease-soak` as its section's midpoint passes.
  Growth is one-way (§1): scrolling up never un-grows the root; the
  drawn length is the maximum reached, held.
- **Choreography timeline (v2).** Hero entry → crack draws 900ms →
  chapters 1–2: crack extends with scroll → rain moment: line holds
  at the crack's endpoint for the pin's full travel → chapter 4
  entry: root's first 40px grow, colour already green (the change
  of colour happens at the endpoint during the pin, over 600ms
  `--ease-soak`, while nothing moves — the visitor who watches the
  margin during the rain sees the line *become* a root) → each later
  section midpoint: one rootlet, 300ms → footer: root reaches the
  footer's top edge and stops; the line does not enter the footer,
  whose dripping (§6.8) is its continuation by other means.
- **State matrix (v2).** *Rest (pre-hero):* nothing drawn (JS-armed
  state; no-JS shows the full line, below). *Drawing / growing:*
  scrubbed per the map. *Grown:* maximum reached, permanent for the
  session. *Hover / focus:* no effect — the line is a record, not a
  control. *Scrolled-past:* holds its maximum. *Disabled:* static
  full line (below).
- **Content merge.** The line runs through the margin of the very
  chapters it describes, its crack in the dry chapters' ground and
  its root beside the wet chapters' text; its rootlets count the
  sections actually passed. It is the page's ground drawn in cross-
  section along the reading — remove the chapters and the line has
  nothing to run beside.
- **Failure fallback.** The SVG ships fully drawn (dashoffset 0);
  JS arms the undrawn state only on init, and a 1200ms watchdog per
  chapter forces any stalled segment to drawn. No-JS: the complete
  crack-and-root stands in the margin as a static diagram — the
  argument survives without the drawing.
- **Reduced-motion variant.** The full line, drawn, from first
  paint; no draw, no growth (the soaked page's margin shows the
  finished root).
- **Breakpoints (v2).** ≥1200px: left margin rail as specced.
  768–1199px: the rail narrows to 28px, branch/rootlet lengths scale
  ×0.7. <768px: the line moves to the page's left edge (4px inset),
  rootlets are cut (the root grows as a single stem — a phone margin
  cannot hold a root system), crack branches reduce to one.
- **Edge cases & failure modes (v2).** *Document height changes*
  (late images, font swap): segment endpoints re-measure on resize
  and the drawn fraction is preserved proportionally — the root
  never visibly jumps. *A chapter removed in the CMS:* segments are
  generated per present chapter; the endpoint-continuity rule is
  re-checked at build (§10) rather than assumed. *Jump scroll to
  the footer:* the whole line draws instantly to its footer state
  (catch-up, §13). *Print:* the line prints fully drawn.
- **Accessibility spec (v2).** `aria-hidden` throughout: the line is
  the visual form of an argument the copy itself makes in words
  (the rain-moment weather note names it: "The crack is where the
  water got in."). No state, link or figure depends on it. Its
  colours are graphical (cracked mud 2.90:1 on dry earth is line-
  work, permitted §2; first green root 4.64:1).
- **Performance budget & mobile variant.** One dashoffset write per
  frame in the shared loop for the active segment only; completed
  segments leave the loop's watch list. Mobile: the single-stem
  variant above.
- **Tokens consumed (v2).** `--cracked-mud`, `--first-green`,
  `--ease-crack`, `--ease-soak`, `--crack-dur` (900ms),
  `--rootlet-dur` (300ms).

### 6.7 Droplet beading hover — the card's surface is a leaf

- **What & why.** In the wet chapters, hovering a card gathers
  droplets on its surface: small radial-gradient beads fade in across
  the card's top edge and face, and one bead swells until it lets go
  and runs 30px down the card before fading. It belongs because by
  chapter 4 the page's surfaces are wet, and a surface that behaves
  dry under the visitor's hand breaks the season the rest of the page
  has built. The card is a leaf in the rain the page has become; the
  hover is the visitor touching the leaf. In the dry chapters the
  same hover does something else entirely — nothing beads on dry
  ground; instead a faint dust sheen lifts (§ below) — because the
  theme's physics are seasonal, not decorative.
- **Structure.** Each card (§6.12) carries a `.beading` layer:
  absolutely positioned, inset 0, `pointer-events: none`, holding
  7–9 bead elements (radial-gradient circles 3–9px, highlight offset
  top-left, `--new-leaf` at 35% with a white core at 50%) placed
  along the card's top edge and upper face at build-authored
  positions, plus one `.runner` bead (7px) parked at the top edge.
  The layer exists only in chapters 4–6 cards; dry-chapter cards
  carry a `.dusting` layer instead (a warm gradient sheen,
  `--dry-earth` at 0 → 18%).
- **Motion spec.** Trigger: pointerenter / focus-within on a wet
  card. Beads fade in staggered by distance from the card's top-left
  (12ms per 40px, so the beading appears to condense across the
  surface) over 260ms `--ease-drip` each. At t+500ms the runner
  swells 7px → 10px over 300ms `--ease-drip`, then releases: it runs
  30px down over 650ms `--ease-downpour`, thinning to 5px as it
  goes, and fades at its run's end. On leave, remaining beads fade
  out over 300ms; the runner, if mid-run, completes its run (water
  does not un-fall) and does not repeat while the same hover lasts.
  Re-hover after leaving restarts the cycle once. Dry cards: sheen
  fades in over 300ms `--ease-soak` on hover, out over 400ms — dust
  disturbed, nothing more.
- **Choreography timeline (v2).** t+0 enter → t+0–260ms beads
  condense in stagger → t+500ms runner swells → t+800ms runner
  releases → t+1450ms run ends, runner gone → beads hold while hover
  lasts → leave: beads fade 300ms; cycle closed.
- **State matrix (v2).** *Rest:* no beads (wet cards), no sheen (dry
  cards). *Hover (desktop):* the cycle above. *Focus-within:* same
  cycle — keyboard visitors get the wet surface too; the runner's
  release is delayed until focus has rested 500ms, matching hover's
  dwell. *Touch:* no hover cycle; a tap on the card fires one runner
  only (swell + run, 950ms) as the tap's acknowledgement, before the
  card's own action — water answers the touch, then the link works.
  *Active:* the click ripple (§6.9) supersedes; beading freezes
  during the press. *Scrolled-past:* no beading off-screen.
  *Disabled card* (a sold-out / past-date card, §6.12): beads form
  but the runner never releases — the water sits on a leaf that will
  not be picked; the distinction is small and regulars will feel it.
- **Content merge.** The beads gather on the card's own surface, at
  its own top edge where rain would land, and the runner runs down
  the card's own face past its own text block (behind the text layer
  — Edge cases). The effect is the card's material state in the
  current chapter, not an overlay applied to arbitrary content: dry
  cards in the same page, same grid, cannot bead.
- **Failure fallback.** The layers are pure CSS/JS enhancement: with
  JS off or the layer unbuilt, cards are simply cards. Hover states
  still carry the theme's non-motion feedback (border ink deepens,
  §11) so no card depends on beading for its affordance.
- **Reduced-motion variant.** No beads, no runner, no sheen motion:
  wet cards show a static 3-bead cluster at the top edge (painted,
  not animated) so the surface still reads wet; dry cards show
  nothing.
- **Breakpoints (v2).** ≥1200px: 7–9 beads as specced. 768–1199px:
  6 beads, run 24px. <768px: hover does not exist — the tap-runner
  only, 5 beads painted statically on wet cards so the surfaces
  still read wet at a glance.
- **Edge cases & failure modes (v2).** *Beads over text:* the
  beading layer sits above the card's ground but below its text
  layer (z-order fixed at build); a bead may cross a photograph or
  the card's open ground, never a glyph. *Rapid hover cycling:*
  enter/leave within 200ms cancels cleanly — beads fade from their
  current opacity, the runner never fires on a skim. *Many cards in
  a grid:* at most one card beads at a time (the hovered one); the
  loop holds no per-card state for the rest. *Low-power device:*
  beads reduce to 4 and the runner is cut — the surface reads wet
  from the painted cluster alone.
- **Accessibility spec (v2).** Purely decorative, `aria-hidden`,
  never the sole hover signal: focus-within also raises the card's
  declared focus ring (§11) and the border deepening, so the beading
  is a third, redundant cue. Touch target is the whole card
  (≥44px in both dimensions by construction, §6.12). No information
  is carried by the beads; a card's state (sold out, etc.) is always
  in its text.
- **Performance budget & mobile variant.** Opacity/transform on ≤10
  small elements on one card at a time; gradients are pre-rendered
  CSS, no canvas. Mobile: the tap-runner variant above.
- **Tokens consumed (v2).** `--new-leaf`, `--dry-earth`,
  `--ease-drip`, `--ease-downpour`, `--ease-soak`, `--bead-dur`
  (260ms), `--run-dur` (650ms), `--run-len` (30px).

### 6.8 Footer dripping — the monsoon outlasts the reading

- **What & why.** The page's last ambient act. After the rain moment
  has passed, droplets bead along the footer image's top edge, swell,
  and run down its face in a slow loop — one droplet every ~4s, never
  synchronised, never hurried. It belongs because it is the theme's
  closing sentence: the reading is finished, the visitor is leaving,
  and the last content on the page is *still dripping*. A page that
  goes dry the moment it is read was never wet. The dripping is also
  the root line's continuation (§6.6): the margin line stops at the
  footer's top edge, and the dripping takes over from exactly there.
- **Structure.** The footer (§6.14) opens with a full-width image —
  the site's landscape, post-rain, at ramp 1.0 — whose top edge
  carries a `.drip-line`: 5 authored bead points along the edge,
  each a small element (radial-gradient bead as §6.7's construction)
  with a run track down the image's face (height 40–70% of the
  image, varying by point). Below the image, the footer's own
  content sits on `--forest-deep`; droplets run only on the image,
  never over footer text.
- **Motion spec.** Trigger: time, ambient, armed only when (a) the
  rain moment has fired this session and (b) the footer image is in
  the viewport (IntersectionObserver gates the loop; off-screen, no
  drips are produced or queued). Cycle per point, points staggered
  pseudo-randomly from a seeded order so the pattern never visibly
  repeats within a minute: bead fades in at the edge over 600ms
  `--ease-drip`, swells 5px → 9px over 1400ms, holds 400–900ms,
  releases and runs its track over 900–1400ms `--ease-downpour`
  (longer tracks run longer — duration = track length × 14ms/px,
  clamped 900–1600ms), thinning and fading in the last 20%. Mean
  interval between releases across all points: ~4s. The loop runs
  at most 2 droplets concurrently.
- **Choreography timeline (v2).** Footer image enters → first bead
  already mid-swell (the loop pre-warms one point by 800ms so the
  footer never arrives dry) → releases begin → continuous slow cycle
  while in view → image exits → cycle pauses at the next release
  boundary; beads mid-swell freeze and resume on re-entry.
- **State matrix (v2).** *Rest (pre-rain session):* no dripping —
  if a visitor jumps straight to the footer before the rain moment,
  the footer image is at its chapter's ramp value and dry-edged;
  the dripping arms only after §6.2 has fired (one-way law applied
  to ambience). *Dripping:* the cycle above, desktop and touch
  identical. *Hover / focus:* no effect; the dripping ignores the
  pointer entirely. *Scrolled-past:* paused by the observer.
  *Disabled:* reduced-motion / no-JS show the static variant
  (below).
- **Content merge.** The droplets run down the footer image's own
  face from its own top edge — the water is the landscape's, held
  over from the rain the visitor scrolled through. The image was
  chosen at build as the page's wettest photograph; the dripping is
  its state, not a widget placed near it.
- **Failure fallback.** Enhancement-only: without JS the image is a
  photograph at full saturation and the footer is complete. A
  stalled loop degrades to the static beads (below) — the CSS
  default state paints 3 beads at the edge, and JS animates from
  there, so failure reads as stillness, not absence.
- **Reduced-motion variant.** No runs, no swells: 3 painted beads
  rest at the edge (the CSS default), and one bead is shown
  mid-track, frozen — the *fact* of dripping without its motion.
- **Breakpoints (v2).** ≥1200px: 5 points as specced. 768–1199px: 4
  points, tracks ×0.8. <768px: 3 points, mean interval ~5s, tracks
  capped at 50% of image height — a phone footer is a glance, and
  the dripping must read within it.
- **Edge cases & failure modes (v2).** *Tab hidden:* the loop
  suspends (the observer + visibilitychange); no backlog of drips
  fires on return. *Image fails to load:* the drip-line is not
  built — dripping over a broken-image icon would be farce, and
  §10's image gate should have caught the asset anyway. *Visitor
  lingers 5 minutes:* the cycle continues unchanged; the seeded
  order reshuffles every 16 releases so no rhythm becomes a
  metronome. *Battery saver:* interval stretches to ~8s (the loop
  reads the shared frame budget, §14, and degrades gracefully
  rather than stopping).
- **Accessibility spec (v2).** `aria-hidden`, unannounced, and the
  footer's information (colophon, counts, links) is entirely in
  text below the image. The motion is slow, small and peripheral —
  well under any photosensitivity threshold (no flashing; luminance
  change is a 9px bead on a photograph).
- **Performance budget & mobile variant.** ≤2 concurrent transform/
  opacity animations on ≤9px elements; the loop sleeps entirely
  off-screen. Mobile: the 3-point variant above.
- **Tokens consumed (v2).** `--new-leaf`, `--forest-deep`,
  `--ease-drip`, `--ease-downpour`, `--drip-interval` (~4s),
  `--drip-track-ms` (14ms/px).

### 6.9 Puddle ripple click — confirmation is weather

- **What & why.** Clicking a button in the wet chapters sends one
  ripple ring expanding across the button's surface from the exact
  click point — a raindrop landing in a puddle — 600ms, fading as it
  reaches the edges. It belongs because it is the theme's only click
  feedback, and it makes the smallest interaction in the site obey
  the same physics as the largest: the button is a wet surface, the
  click is a drop, the acknowledgement is a ring. In the dry chapters
  buttons do not ripple (there is no water yet); they answer with a
  dry press (§11) and a faint dust puff at the click point — one
  physics per season, consistently.
- **Structure.** Each button (§11) is `position: relative;
  overflow: hidden` and carries a `.ripple` span created on demand:
  a circle border (1.5px, current button ink at 55%) sized to the
  button's diagonal, centred on the click coordinates (keyboard
  activation: the button's centre), scaled 0 → 1. The span is
  removed at animation end. Dry-chapter buttons carry `.dust` — a
  radial gradient puff, `--cracked-mud` at 30%, scaling 0.3 → 1 and
  fading over 450ms.
- **Motion spec.** Trigger: click / tap / Enter / Space on a wet-
  chapter button. Ring: scale 0 → 1 over 600ms `--ease-soak` (the
  ease's soft start is the drop's entry; its long tail is the ring
  dying into the surface), opacity 0.55 → 0 across the same span,
  with a second, fainter ring at +90ms at 25% opacity — a real drop
  throws a secondary ring, and the detail costs one span. The
  button's action fires on the click as normal: the ripple never
  delays, gates or confirms the action; it is the surface's
  response, not a loading state. Maximum 2 ripples per button
  concurrently; a third click restarts from its own point.
- **Choreography timeline (v2).** t+0 click → ring 1 begins at the
  point → t+90ms ring 2 → t+300ms ring 1 at ~70% reach, opacity
  ~0.25 → t+600ms both gone, spans removed, button at rest (or in
  its pressed/active state per §11 if the action holds it).
- **State matrix (v2).** *Rest:* plain button. *Hover:* no ripple
  (hover has its own feedback, §11); the surface merely deepens 4%.
  *Focus:* no ripple; the focus ring (§11) is the feedback.
  *Active (click):* the ripple above, identical for mouse, touch
  and keyboard (origin differs: point vs centre). *Disabled
  button:* no ripple, no dust — a disabled surface is inert, and
  §11's disabled styling says so in text weight, not in missing
  weather. *Scrolled-past:* n/a.
- **Content merge.** The ripple expands across the button's own
  surface from the visitor's own click point and dies at the
  button's own edges — it is the button behaving as the material
  its chapter says it is. A ripple on a dry button would be a lie
  about the season; the theme forbids it (§9).
- **Failure fallback.** Pure enhancement: buttons work identically
  without it. If the span fails to build, the click still lands —
  the ripple is attached to the event, never wrapped around the
  handler.
- **Reduced-motion variant.** No expanding ring: the button flashes
  its ink border once (opacity pulse 120ms) as the click's
  acknowledgement — feedback survives, motion rests.
- **Breakpoints (v2).** Identical at all sizes; on <768px the
  secondary ring is cut (one ring reads clearly at thumb scale and
  the second is jewellery).
- **Edge cases & failure modes (v2).** *Long buttons* (full-width
  submit): the ring scales to the diagonal and clips at the corners
  — correct puddle behaviour in a rectangular vessel. *Rapid
  clicking:* capped at 2 concurrent; spans are pooled per button
  and reused. *Button that navigates:* the ripple runs under the
  page transition (§6.15) — the cloud-wipe covers at 300ms, by
  which time the ring has read; the ripple never delays navigation.
  *Submit with validation errors:* the ripple still fires (the drop
  landed) and the error appears per §6.13 — weather and outcome are
  separate channels, deliberately.
- **Accessibility spec (v2).** Decorative, `aria-hidden`; the click's
  *real* feedback is the action's result and, for toggles, the
  button's `aria-pressed` — the ripple announces nothing and
  replaces nothing. Keyboard origin at centre guarantees the
  feedback exists without a pointer. Contrast is the button's own
  declared pair (§11) at every frame; the ring is an addition, never
  a dimming.
- **Performance budget & mobile variant.** One or two spans,
  transform + opacity, compositor-only; spans pooled. Negligible.
  Mobile: the single-ring variant above.
- **Tokens consumed (v2).** `--ease-soak`, `--ripple-dur` (600ms),
  `--ripple-ink` (currentColor at 55%), `--dust-dur` (450ms).

### Page-family elements

### 6.10 Cloud-band navigation (page family: navigation)

- **What & why.** The site's navigation lives under a cloud band:
  the header is a horizontal band of deepening grey-green whose
  underside is the theme's recurring actor (§1), and its links are
  the chapters named as weather — "The Dry", "First Clouds", "The
  Rain", "After the Rain" — with the current chapter marked by the
  band's edge having passed it: links behind the reading position
  sit on the band's darker, rained-on side. It belongs because
  navigation in this world is a forecast: the header shows where in
  the season the visitor is, the way the gauge (§6.5) shows how much
  rain has fallen — the two instruments agree, one in words, one in
  water.
- **Structure.** A `<header>` (sticky on ≥768px, static on <768px)
  whose ground is a left-to-right gradient from the current chapter
  ground to `--forest-deep`, with a soft lower edge (the band's
  underside, an SVG curve). Inside: the site name in Newsreader, a
  `<nav>` of chapter links in apparatus type (§3), and — on the
  tablet breakpoint where the gauge leaves the margin (§6.5) — the
  horizontal gauge tube under the band. Current chapter link carries
  `aria-current="true"`, is set in dry earth, and is underlined by a
  2px `--new-leaf` rule that is drawn (not slid) when the chapter
  changes.
- **Motion spec.** On chapter change (shared loop's chapter
  watcher): the band's gradient steps one chapter darker over
  600ms `--ease-soak`, and the new current link's rule draws over
  300ms `--ease-soak`. The band itself crosses the header once at
  load (a 900ms `--ease-glide` wipe, the §6.1 band at header scale)
  — after that it is a place, not an animation. Hover on a link:
  its ground spot darkens 6% over 180ms (a cloud thickening over
  that chapter's name). No other motion.
- **Choreography timeline (v2).** Load → band wipe 900ms → header at
  rest → chapter boundary crossed → t+0 gradient step begins →
  t+300ms new rule drawn → t+600ms band at its new darkness → rest.
- **State matrix (v2).** *Rest:* band at the current chapter's
  darkness, current link ruled. *Hover:* spot-darkening (desktop);
  touch: none. *Focus:* link takes the theme focus ring (§11) plus
  the spot-darkening, so keyboard and pointer agree. *Active /
  current:* as specced. *Scrolled-past:* the header is sticky, so
  there is no scrolled-past state on ≥768px; on mobile it scrolls
  away and the gauge tube (§6.5) remains the only instrument.
  *Disabled:* a chapter with no content is absent from the nav —
  never a greyed link (§11's refusal rule).
- **Content merge.** The links are the chapters, the band's darkness
  is the reading position, the tablet gauge in the same header
  measures the same progress in water — three views of one fact,
  all in the site's furniture. The nav could not be lifted onto
  another theme: its ground is this page's weather.
- **Failure fallback.** A plain header with text links on the
  chapter ground; current chapter still marked in text weight and
  `aria-current`. The gradient and wipe are enhancements over a
  complete nav.
- **Reduced-motion variant.** No wipe, no gradient step animation
  (the step is instant at chapter change), rule pre-drawn.
- **Breakpoints (v2).** ≥1200px: sticky band, full chapter names.
  768–1199px: sticky band + horizontal gauge beneath it, names
  shorten ("Dry", "Clouds", "Rain", "After") with full names in
  `aria-label`. <768px: static header, nav becomes a two-row wrap of
  chapter chips in apparatus type; the gauge tube pins to the
  viewport top alone (8px, §6.5) so an instrument survives the
  header's departure.
- **Edge cases & failure modes (v2).** *More than 5 chapters:*
  chapter links cap at the 6 named bands (§4); sub-sections live in
  their chapter's own apparatus lines, never as extra nav items —
  a forecast with 14 entries is a timetable, not a band. *Long site
  name:* truncates at 24ch on the band; the full name is in the
  footer colophon (§6.14). *Sticky + anchor jumps:* anchors carry
  `scroll-margin-top` equal to band height + 16px at every
  breakpoint.
- **Accessibility spec (v2).** Real `<nav aria-label="Chapters of
  the season">`; current link `aria-current="true"` updated only at
  chapter changes. Link contrast: dry earth on the band's darkest
  step 7.48:1; on its lightest (chapter 1) step, links are
  `--mud-deep` at 5.33:1 — the link colour swaps with the band's
  step, declared per chapter in §4's table, never mid-step. Focus
  order is DOM order; targets ≥44px tall on touch breakpoints.
- **Performance budget & mobile variant.** One gradient transition
  and one rule draw per chapter change; nothing per frame. Mobile:
  the static variant above.
- **Tokens consumed (v2).** `--forest-deep`, `--dry-earth`,
  `--mud-deep`, `--new-leaf`, `--ease-glide`, `--ease-soak`,
  `--band-wipe` (900ms), `--band-step` (600ms).

### 6.11 The waiting hero (page family: hero composition)

- **What & why.** §6.1 specifies the first rain; this element
  specifies the composition it falls on: the dry season's portrait.
  First viewport: a wide landscape photograph at ramp 0 (0.55
  saturation — visibly thirsty) occupying the lower two-thirds, the
  crack (§6.6) drawn across its dry foreground, and above it the
  hero line in its first state, "the earth, waiting", with a weather
  note (§3) carrying a real date — the last rain, or the forecast's
  promise. The composition's job is *withholding*: pale ground, low
  colour, a sentence in the present tense of waiting. Everything the
  page later becomes is measured against this first screen.
- **Structure.** `<section class="hero">`: kicker apparatus ("THE
  DRY SEASON"), the hero line (Newsreader display, §3), the weather
  note (Newsreader italic, dated), one action link (the page's
  primary — into chapter 2), and the landscape figure with its
  caption (Source Sans, sourced, §3 law 2). The heat shimmer layer
  sits over the headline zone only: a 6vh-tall gradient strip,
  `aria-hidden`, animated by a slow vertical wobble (translateY
  ±2px, 2.6s, `--ease-soak` alternate) that blurs nothing and moves
  almost nothing — shimmer is refraction suggested, not applied;
  the strip carries a 1px backdrop distortion via SVG filter where
  supported and is simply absent where not.
- **Motion spec.** On load: §6.1's pass (which ends the shimmer at
  its first streak). Before the pass, and on any load where the pass
  is skipped (bfcache), the shimmer runs alone. The hero photograph
  performs the §5 scale-in-frame (1.06 → 1) scrubbed to its
  viewport transit. Nothing else moves: a dry hero that fidgets is
  a hero that isn't thirsty.
- **Choreography timeline (v2).** t+0 hero paints (dry, complete) →
  shimmer runs → fonts ready → §6.1 pass t+80–1800ms (shimmer dies
  at its t+350) → hero at post-first-rain rest: headline wet-ink,
  ground still dry, photograph still at ramp ~0 → the visitor
  scrolls; the season begins in earnest.
- **State matrix (v2).** *Rest (pre-pass):* dry composition,
  shimmering. *Post-pass rest:* as above. *Hover:* the action link
  behaves per §11 (dust press — the hero is dry ground). *Focus:*
  the action link is the hero's only focusable element; focus never
  triggers the pass. *Scrolled-past:* the hero's photograph holds
  its local ramp cap (§6.3); returning shows it post-rain if the
  session's rain has fallen. *Disabled:* no-JS hero is the complete
  dry composition with the headline in wet-forest ink (the settled
  choice — a static page states its thesis in its final ink).
- **Content merge.** Every element of the composition is the site's
  own first content: its landscape, its sentence, its dated note,
  its one action. The shimmer lies over the headline's air, the
  crack across the photograph's own foreground — both are states of
  the content, not overlays upon it.
- **Failure fallback.** The composition is static-first: photograph,
  headline, note and link are complete HTML/CSS. The shimmer and the
  pass are inserted layers; their absence leaves the dry hero
  intact.
- **Reduced-motion variant.** No shimmer, no pass: the soaked
  page's hero (§5) — photograph at ramp 1, headline in its final
  state, and the weather note's date unchanged (facts don't soak).
- **Breakpoints (v2).** ≥1200px: photograph lower two-thirds, hero
  line above at display size. 768–1199px: photograph 55% height,
  line wraps to two lines (the fixed-box law of §3 applies to §6.2's
  block, not to this headline's first state — but its measure is
  still set once, at build). <768px: photograph 46% height, weather
  note below the action link, shimmer strip 4vh.
- **Edge cases & failure modes (v2).** *Photograph missing / slow:*
  the hero composes on `--earth-pale` with the crack drawn and the
  caption in place; when the image lands it fades in at its current
  ramp value over 300ms — a late photograph joins the season at the
  season's current state, never at a flash of dry. *Very tall
  viewport:* the photograph caps at 72vh so the weather note never
  leaves the first screen. *Client-supplied hero line longer than
  9 words:* §10's gate flags it — the waiting line is a held breath,
  and a paragraph cannot hold one.
- **Accessibility spec (v2).** The hero line is the page's `<h1>`;
  the weather note is a `<p>`; the photograph's alt describes the
  landscape, and its caption carries the source. Shimmer is
  `aria-hidden` and sub-perceptual by design (2px, 2.6s — no flash
  risk). Contrast: headline mud-deep 5.33:1 pre-pass, wet forest
  7.48:1 after; note in first green 4.64:1.
- **Performance budget & mobile variant.** One photograph (the
  page's LCP — budget §14), one shimmer strip, the §6.1 layers.
  Mobile: the compressed composition above; shimmer strip is the
  first cut on low-power devices (§14's cut order).
- **Tokens consumed (v2).** `--dry-earth`, `--earth-pale`,
  `--mud-deep`, `--wet-forest`, `--first-green`, `--ease-soak`,
  `--shimmer-cycle` (2.6s).

### 6.12 Field cards (page family: cards / listing)

- **What & why.** The listing unit of the wet chapters: a card is a
  field report — a photograph of a place or crop, its name, one line
  of record (a figure with its date, §3 law 2), and a link onward.
  Cards are printed on the chapter's ground and obey the chapter's
  physics: dry-chapter cards are pale, matte and dust-hovered; wet-
  chapter cards bead (§6.7). The same card component crossing the
  rain moment in a listing that spans chapters changes its material
  with the season — which is the theme's whole argument, at card
  scale.
- **Structure.** `<article class="field-card">`: figure (photograph
  in a fixed 4:3 frame, ramped per §6.3, scale-in-frame per §5),
  name (Newsreader 22px), record line (Source Sans semibold tabular:
  the figure, its unit, its date), one line of body (17px, max 2
  lines), and the whole card as one stretched link over the name.
  A card with a state (harvested, sold out, season closed) carries
  the state as a stamped line in `--first-green` (wet) / `--mud-deep`
  (dry) across its record line — text, never a badge (§11).
- **Motion spec.** Entry: cards arrive under their section's wet
  front (§6.4) with a 90ms stagger in reading order — they do not
  animate separately; the front is their entrance. Hover: §6.7's
  beading (wet) or dusting (dry), plus the photograph's register —
  its scale settles the last 0.01 to 1.0 over 200ms `--ease-soak`,
  as if the visitor's attention brings the field into focus.
  Focus: identical to hover, plus the focus ring (§11).
- **Choreography timeline (v2).** Section front fires → cards wet
  in stagger (90ms apart, front-paced, §6.4) → rest → hover cycle
  per §6.7 → click: §6.9's dust/ripple by chapter, then navigation
  (§6.15).
- **State matrix (v2).** *Rest:* printed card at its chapter's
  material. *Hover:* §6.7 + settle. *Focus:* hover's treatment +
  ring. *Active:* press per §11. *Scrolled-past:* printed; beading
  off. *Disabled (state card):* the stamped state line; the card
  still links to its record (a closed season's report is still
  readable) unless it never had a destination, in which case it is
  not a link at all and says so by its cursor and its text.
  *Touch:* tap-runner per §6.7, then the link.
- **Content merge.** The card's photograph is ramped by the page's
  season, its surface beads in the wet chapters, its record line is
  a real dated figure — every themed behaviour is a property of the
  card's own content and position in the season. A card lifted into
  another theme would take nothing with it but a border.
- **Failure fallback.** Static card: photograph at natural
  saturation, all text present, link live. Entry is the section
  front's business; if the front fails, cards are simply there
  (§6.4's fallback).
- **Reduced-motion variant.** No stagger (cards present with their
  section), no beading animation — the static bead cluster of §6.7
  on wet cards; photographs at ramp 1.
- **Breakpoints (v2).** ≥1200px: grid of 3, gutter 24px, spans may
  vary by chapter rhythm (a wide 2-span card opens each wet chapter
  grid — the season's abundance gets the big field first).
  768–1199px: 2-up. <768px: 1-up, photograph 16:10, record line
  wraps under the name.
- **Edge cases & failure modes (v2).** *Missing photograph:* the
  card's figure becomes a contour of the crack/root line (§6.6's
  geometry in miniature, `--cracked-mud` on `--earth-pale`) — a
  drawn field, never a grey box or a substituted stock photo.
  *Figure without a date:* the record line is not printed (§3 law
  2); the card carries its body line only, and §10 flags the
  content. *Very long name:* clamps at 2 lines; the full name is
  the link's accessible name.
- **Accessibility spec (v2).** One link per card (the name), its
  accessible name the full name + the record line's figure, so a
  screen-reader listing hears the data, not just titles. The
  photograph is decorative (`alt=""`) when the name identifies the
  place, or carries real alt when the image is the evidence —
  chosen per build, consistently (§6.3's exclusion rule applies to
  ramped evidence images). Focus ring per §11; targets ≥44px.
- **Performance budget & mobile variant.** Cards inherit §6.3's
  image caps and §6.7's one-card-at-a-time beading. Mobile: 1-up,
  tap-runner only.
- **Tokens consumed (v2).** `--earth-pale`, `--first-green`,
  `--mud-deep`, `--ease-soak`, `--stagger-card` (90ms).

### 6.13 The rain-letter form (page family: forms / conversion)

- **What & why.** Conversion in this theme is a letter sent into the
  coming season: the form — a subscription to the season's letters,
  an order for the harvest, a booking for the rains — is set as a
  sheet that is itself mid-season. Its top half sits on the dry
  ground of the chapter where it lives; as the visitor fills it, the
  sheet's lower edge darkens field by field, as if completing the
  letter were itself a small rainfall. On submit, the sheet is
  *sealed by weather*: the confirmation arrives as a weather note
  (§3) with a real date — "Received before the rains, 14 May. Your
  first letter follows the first storm." It belongs because it makes
  the site's one transactional moment obey the theme's causality:
  to write is to commit to the season, and the page answers in the
  season's voice.
- **Structure.** `<form class="rain-letter">` on a sheet
  (`--earth-pale` face, deckled lower edge): fields as ruled lines
  (label in apparatus above, input on a 1px `--cracked-mud` rule,
  Source Sans 17px), in the order a letter is written — name (the
  signature), direction (email — labelled "Your direction", with
  the hint "FOR THE SEASON'S LETTERS"), the choice the form exists
  for (radio lines in the letter voice, e.g. "THE FULL SEASON" /
  "ONLY THE RAINS"), one free line (optional, ruled textarea, max
  4 lines), and the submit: a full-width button (§11) in wet forest
  whose label is the commitment in words ("Send it into the
  season"). Behind the fields, the sheet's wet layer (§6.4's
  construction) whose height is driven by completion fraction.
- **Motion spec.** Field focus: the field's rule inks from
  `--cracked-mud` to `--first-green` over 220ms `--ease-soak` and a
  6px bead (§6.7's construction) forms at the rule's right end.
  Field completed (valid, on blur): the sheet's wet layer rises one
  field-step (its height = completed fields / total fields × the
  sheet's lower 40%) over 500ms `--ease-soak` — the letter wets from
  the bottom up as it is written. Error: the rule turns
  `--petrichor` (the theme's correction colour, §6.2) and the error
  note appears beneath in the desk voice (§12) — e.g. "THE
  DIRECTION WILL NOT CARRY — CHECK THE ADDRESS." — with the field's
  bead drying (fading) until corrected. Submit: the button ripples
  (§6.9 — the form lives in a wet chapter by the time it is
  complete), the sheet's wet layer completes its rise over 600ms,
  and on success the form is replaced by the confirmation weather
  note + a record line (the real reference, if the backend issues
  one — §12's law: no invented references).
- **Choreography timeline (v2).** Focus: t+0 rule inks (220ms), bead
  forms at t+220. Blur-valid: wet layer steps (500ms). Submit:
  t+0 ripple → t+0–600ms wet layer completes → response → form
  exchanged for the confirmation over 300ms `--ease-soak` (a fade is
  lawful here exactly once: a letter exchanged for its answer) →
  the header gauge (§6.5) performs one meniscus wobble — the
  season acknowledges the letter.
- **State matrix (v2).** *Rest:* dry-topped sheet, fields empty,
  wet layer at 0. *Focus:* inked rule + bead. *Filled:* wet layer
  at its fraction — persistent across scroll (a half-written letter
  stays half-wet; no state is lost to scrolling). *Error:*
  per-field, persistent until corrected; errors never auto-dismiss
  and never clear the visitor's text. *Submitting:* fields disabled
  at full contrast (labels stay at their declared pairs — a greyed
  label below AA is a §10 failure), button label becomes "Sending —
  the post is going out" (no spinner exists in this theme).
  *Success:* the confirmation state, terminal. *Disabled (form
  closed — e.g. the season's list is full):* the whole sheet is
  replaced by the closed-state letter (§12's empty voice) with its
  date — never a disabled form sitting mute.
- **Content merge.** The wet layer rises over the sheet the visitor
  is actually writing on, in proportion to the writing actually
  done; the confirmation is a dated weather note in the site's own
  voice; the form's fields are a letter's parts (signature,
  direction, the ask). Remove the visitor's writing and the sheet
  stays dry — the weather is caused by the content.
- **Failure fallback.** A working HTML form: labels, inputs, submit
  — posts without JS; server errors re-render in the same desk
  voice beneath their fields; the wet layer is a JS/CSS enhancement
  over a complete form. A failed send keeps every field's text and
  notes beneath the button: "NOT SENT — THE POST FAILED. YOUR
  LETTER IS KEPT BELOW." (§12).
- **Reduced-motion variant.** No rising layer animation (the layer
  jumps to its fraction instantly on blur), no bead, no ripple —
  the border flash of §6.9's variant on submit; the confirmation
  replaces the form without the fade.
- **Breakpoints (v2).** ≥1200px: sheet at the lee's measure, fields
  one column (letters are one column), name/direction sharing a
  ruled pair at sheet widths ≥900px. 768–1199px: one column
  throughout. <768px: inputs at 17px (no iOS zoom), submit button
  52px tall, wet layer's travel halves (lower 20% of the sheet) so
  the effect reads at phone scale without swallowing the fields.
- **Edge cases & failure modes (v2).** *Optional fields:* the wet
  fraction counts required fields only — a visitor is never told
  their letter is half-wet for skipping an optional line. *Back
  button after success:* the confirmation state persists (server
  state); the form does not resurrect half-filled. *Double
  submit:* the submitting state disables the button until
  resolution. *Long free line:* the ruled textarea extends to 4
  lines then scrolls internally — the sheet does not grow; a letter
  longer than its sheet is the one place the fiction yields.
  *Network failure:* per the fallback — text kept, seal unpressed,
  retry offered in words.
- **Accessibility spec (v2).** Every field has a real `<label>`;
  hints are `aria-describedby`, never placeholders (a blank ruled
  line is the invitation). Errors are linked via `aria-describedby`
  and summarised in a polite live region on submit failure only.
  Contrast: labels `--mud-deep` 5.33:1 on the sheet; error text
  `--petrichor` darkened to `--mud-deep` weight for text (the
  graphical petrichor is 4.15:1 — the *note* is set in mud-deep
  with a petrichor rule, so words never ride a graphical contrast).
  Touch targets: field hit rows 48px; submit 52px.
- **Performance budget & mobile variant.** Transitions on focus,
  blur and submit only; the wet layer is one height/opacity write
  per field event, not per frame. Mobile: the halved-travel variant
  above.
- **Tokens consumed (v2).** `--earth-pale`, `--cracked-mud`,
  `--first-green`, `--petrichor`, `--mud-deep`, `--wet-forest`,
  `--ease-soak`, `--wet-step` (500ms).

### 6.14 The still-dripping footer (page family: footer)

- **What & why.** The footer is the season completed: the landscape
  image still dripping (§6.8), and beneath it, on the deepest
  ground, the colophon set as the record of the season — who
  published it, the place, the year, and the season's own figures
  restated once (the gauge's full scale and the harvest total, with
  their dates) so the page ends with its evidence in order. There
  are no link columns dressed as landscape; a monsoon site ends the
  way a season ends — with the ground soaked, the numbers written
  down, and water still coming off the edges.
- **Structure.** `<footer>`: the dripping image (§6.8) full-bleed at
  the top; then the colophon block on `--forest-deep` — site name
  (Newsreader), "Written at —" + the place, the year, the season's
  figures line (Source Sans tabular, each figure with its date),
  the legal line, and one line of apparatus closing the page: "END
  OF THE SEASON — RAINFALL AS GAUGE: nnn MM" (the true full-scale
  figure, §6.5 — the same number the gauge filled to, so the page's
  first instrument and its last line agree). One "Further seasons"
  link (the archive) may sit above the colophon — the only
  navigation the footer carries.
- **Motion spec.** §6.8's dripping on the image; nothing else in the
  footer moves. The figures line does not count (its counting
  happened at §6.16, in the soak chapter; the footer *restates*,
  and restated figures are still). The colophon is static at every
  scroll position.
- **Choreography timeline (v2).** Footer enters → dripping cycle
  per §6.8 (pre-warmed) → colophon readable throughout → nothing
  further, at any time, however long the visitor stays.
- **State matrix (v2).** *Rest:* as composed. *Hover / focus:* the
  archive link behaves per §6.10's link rules. *Scrolled-past:*
  n/a — it is the end. *Disabled:* dripping static (§6.8), colophon
  unchanged.
- **Content merge.** The footer's image is the hero's landscape
  (§6.11) returned at full saturation — the same ground, after the
  season — and its figures are the page's own figures, restated.
  The footer is the before/after's second half; it could not close
  any other page.
- **Failure fallback.** Static image, static colophon; nothing in
  the footer can fail into absence.
- **Reduced-motion variant.** §6.8's static beads; colophon
  identical.
- **Breakpoints (v2).** All sizes: colophon at the lee's measure;
  <768px the figures line stacks one figure per line (a phone
  colophon is a list, not a table).
- **Edge cases & failure modes (v2).** *A season with no harvest
  figure:* the figures line carries rainfall alone — an absent
  figure is omitted, never zero-filled (§1's law). *Archive link
  absent:* the colophon follows the image directly; the footer
  never depends on §6.10 or the archive existing.
- **Accessibility spec (v2).** A real `<footer>` with real text; the
  image is decorative here (its informative appearance was the
  hero's, with alt and caption) and carries `alt=""`. Figures are
  text, readable in order. Contrast: dry earth on forest-deep 8.9:1;
  leaf-pale secondary 6.92:1 on wet forest.
- **Performance budget & mobile variant.** §6.8's budget; the rest
  is static. Mobile: the stacked figures line above.
- **Tokens consumed (v2).** `--forest-deep`, `--dry-earth`,
  `--leaf-pale`, `--new-leaf`.

### 6.15 Cracked-sheet skeleton + cloud-wipe transition (page family: loader / transition)

- **What & why.** The theme's two state-change rituals, sharing one
  logic: before the rain, everything is dry. **Loading** shows the
  cracked sheet — the page's real layout rendered as dry, pale,
  cracked placeholders (text as ruled dry lines, images as
  `--earth-pale` frames with a crack line drawn through them) that
  *soak* into content as it arrives: saturation and ground step in
  over 400ms, as if the fetched page were being rained on at last.
  **Navigation** is the cloud-wipe: a cloud band (§6.1's band at
  full-viewport scale) crosses, the route changes beneath its
  cover, and the band leaves from the far side. Both belong because
  they are the theme's own substances — dry ground and cloud — doing
  the two jobs every site must do; a spinner or a fade would be
  foreign weather.
- **Structure.** Skeleton: the real section markup rendered with
  `.is-loading` — frames at their true aspect ratios in
  `--earth-pale` with an SVG crack (a short 3-branch path,
  `--cracked-mud` at 60%), text as `--cracked-mud` rules at 25%
  opacity at true line-heights; content swap replaces children in
  place (zero layout shift by construction). Wipe: a fixed
  full-viewport `.cloud-wipe` (the band's material: `--forest-deep`
  with the soft underside edge, §6.10) parked off-canvas left; on
  navigation it sweeps across, the route swaps at full coverage,
  and it exits right.
- **Motion spec.** Skeleton soak: as each block's content lands, its
  placeholder crossfades to content over 400ms `--ease-soak` while
  its crack fades — a miniature of the whole theme. Hard cap: any
  block still loading at 1400ms has its crack and rules stripped to
  plain `--earth-pale` (the standing law: no placeholder may stay
  theatrical if the machinery has failed); content then arrives
  plainly. Wipe: 900ms total `--ease-glide` — 400ms cover, swap at
  full coverage, 400ms reveal, 100ms settle. The incoming page
  arrives at *its* season state (per the session's ramp floor,
  §6.3) — navigation never resets the weather.
- **Choreography timeline (v2).** Wipe, t+0 link activation → band
  enters → t+400ms full coverage, route swaps, new page at its
  scroll top in its session season state → t+800ms band exits →
  t+900ms focus lands on the new page's `<h1>` (Accessibility) →
  t+1200ms watchdog: any wipe not completed is torn down and the
  destination shown plainly.
- **State matrix (v2).** *Loading:* cracked placeholders inside real
  geometry. *Soaking:* 400ms per block. *Loaded:* normal behaviour.
  *Wiping:* 900ms, pointer locked out. *Hover:* links show §6.10
  hover; the wipe has no hover state. *Focus:* keyboard activation
  fires the same wipe; focus lands per the timeline. *Disabled /
  no-JS:* no skeletons rendered unresolved (server pages ship
  loaded; skeletons exist only inside client fetches that own
  their watchdog) and plain navigation — the wipe enhances `<a>`
  clicks it can intercept and never breaks one it can't (modified
  clicks, new tab, external links bypass it entirely).
- **Content merge.** The skeleton is the page's own unsoaked self —
  same geometry, same cracks the hero wears (§6.6's line at block
  scale). The wipe's band is the same cloud that opened the site
  (§6.1) returning to move the visitor; leaving a page is weather
  here, as arriving was.
- **Failure fallback.** As specced in the state matrix: plain
  navigation, plain content arrival. A fetch that errors resolves
  its skeleton block into the theme's error block (§11) with a
  desk-voice note (§12) — a section apologises in character rather
  than cracking forever.
- **Reduced-motion variant.** Skeleton blocks are plain
  `--earth-pale` (no crack, no soak animation — content fades at
  120ms or appears). Wipe: none; instant navigation with the
  header band's step (§6.10) marking the change of page.
- **Breakpoints (v2).** ≥1200px: full spec. 768–1199px: wipe 800ms.
  <768px: wipe 700ms and the band's soft edge simplifies to a
  straight 24px gradient (the curve's subtlety is lost at phone
  width; its cover is not).
- **Edge cases & failure modes (v2).** *Slow destination:* the band
  holds at full coverage with the gauge's meniscus wobble (§6.5)
  running on the band's own small gauge mark — up to 3s; then the
  wipe aborts, the band retreats (250ms), and native load proceeds.
  The theme never traps a visitor inside weather. *Same-page
  anchors:* no wipe — the §5 glide applies instead. *Prefetch:*
  hovered internal links may prefetch; the wipe still runs its full
  900ms — the ritual is the point, not the wait.
- **Accessibility spec (v2).** During a wipe the outgoing page is
  `inert` from t+0 and the destination is made live at reveal with
  focus moved to its `<h1 tabindex="-1">` and a polite announcement
  "Arrived: [page name]". Loading blocks carry `aria-busy="true"`
  until resolved; a region announces "The page is still dry —
  content is coming" once, not per block. The wipe is skipped for
  reduced-motion and for router-managed focus.
- **Performance budget & mobile variant.** Skeleton is CSS + one
  small SVG per block. The wipe is one transform on one fixed
  element. Mobile: the 700ms variant above.
- **Tokens consumed (v2).** `--earth-pale`, `--cracked-mud`,
  `--forest-deep`, `--ease-soak`, `--ease-glide`, `--soak-dur`
  (400ms), `--fallback-strip` (1400ms), `--wipe-dur` (900ms).

### 6.16 Monsoon figures — rainfall & harvest counters (page family: data)

- **What & why.** The soak chapter's numbers, counted honestly. Two
  or three large figures — the season's rainfall, the harvest, a
  reservoir's recovery — each count up once as the chapter enters,
  in tabular Source Sans at display-data size, and each stands
  beside its caption naming the source and the period ("412 mm —
  estate gauge, 1 June to 30 September"). It belongs because the
  theme's climax is not a colour but a quantity: the rain, measured.
  A monsoon page whose numbers are decorative has missed its own
  point; these figures are the reason the gauge (§6.5) has a full
  scale.
- **Structure.** A `.figures` row in the soak chapter: each figure a
  `<figure>` with the number (`.fig-value`, tabular, 44–56px), its
  unit and label in apparatus, and its `<figcaption>` with source +
  period (§3 law 2). Values are server-rendered at their final
  numbers in the DOM; the count is a JS replay from a stated start
  (rainfall counts from the pre-season baseline the caption names —
  e.g. from the 96mm that fell before June — never from 0 unless 0
  is the true baseline).
- **Motion spec.** Trigger: the figures row crossing 55% viewport.
  Each figure counts over 1400ms `--ease-soak` with a 120ms stagger
  in reading order, whole units only, tabular figures throughout so
  nothing reflows. The count is once-only and ends exactly on the
  DOM value; a figure whose count is interrupted (fast scroll away)
  completes instantly off-screen — a number must never be caught
  mid-lie.
- **Choreography timeline (v2).** Row at 55% → t+0 first figure
  begins → t+120ms second → t+240ms third → t+1400–1640ms all at
  their true values, still forever after.
- **State matrix (v2).** *Rest (pre-entry):* figures at their final
  DOM values (the count is armed by JS only). *Counting:* 1400ms,
  non-interactive. *Counted:* permanent. *Hover / focus:* no
  effect. *Scrolled-past:* counted or instantly completed.
  *Disabled:* final values (the DOM default).
- **Content merge.** The figures are the chapter's content — the
  season's measured result — and the gauge's full scale is one of
  them, printed here in full. The count replays the accumulation the
  visitor has just scrolled through; it is the ramp (§6.3) rendered
  as arithmetic.
- **Failure fallback.** DOM values are final; no JS, no count, no
  problem. A figure supplied without a source is not built (§1's
  law) — the row simply holds fewer figures, and §10 records the
  content gap.
- **Reduced-motion variant.** No count: figures stand at their
  values.
- **Breakpoints (v2).** ≥1200px: row of up to 3. 768–1199px: row of
  2 + 1 stacked. <768px: one per line, value 38px — a phone figure
  is a headline of data and is set like one.
- **Edge cases & failure modes (v2).** *Baseline disputes:* if the
  publisher cannot state a baseline, the count starts at the value
  minus 15% and the caption says "counted from a partial record" —
  honesty in the caption, or no count at all. *Decimal figures*
  (a reservoir at 61.4%): count in tenths, tabular, ending exact.
  *A figure that fell* (a failed crop in a recovery story): it
  counts *down* from its previous season's value, and the caption
  names both seasons — the theme's honesty covers bad years.
- **Accessibility spec (v2).** The counting is visual only: the DOM
  value is final from first paint (JS rewinds it only in the visual
  layer via a `aria-hidden` clone technique — the accessible value
  never animates), so screen readers meet the true figure once, in
  order. Captions are read as part of the figure.
- **Performance budget & mobile variant.** Three text updates per
  frame in the shared loop for 1400ms. Negligible. Mobile: the
  stacked variant above.
- **Tokens consumed (v2).** `--ease-soak`, `--count-dur` (1400ms),
  `--count-stagger` (120ms).

### 6.17 The season ledger (page family: data table / trust)

- **What & why.** The soak chapter's evidence table: the season
  written down week by week — date, rainfall that week, cumulative
  rainfall, and one line of record (what was sown, cut, repaired,
  released). It is also where the gauge's full scale is defined
  (§6.5) and where every figure used anywhere on the page can be
  traced to its row. It belongs because a theme whose law is
  *measured or not printed* needs its ledger on the page, not in a
  PDF: the visitor who doubts the gauge can audit it here, row by
  row, against the same numbers.
- **Structure.** A `<table class="ledger">` on the soak ground:
  Source Sans throughout (figures tabular), a header row in
  apparatus, week rows with hairline rules (`--new-leaf` at 30%),
  the cumulative column in semibold, and a totals row that must
  equal the gauge's full scale and §6.16's rainfall figure exactly
  — one number, three printings, zero disagreement (checked in
  §10). Rows beyond 12 collapse behind a "The full ledger" disclosure
  that expands in place (the remaining rows are in the DOM).
- **Motion spec.** Rows do not animate on entry (a ledger is
  consulted, not performed) beyond inheriting the section's wet
  front (§6.4). The disclosure expands over 350ms `--ease-soak`
  (height auto via grid-rows technique); the totals row's figures
  never count — totals are stated, not replayed (§6.16's rule
  inverted: the ledger is where counting stops).
- **Choreography timeline (v2).** Section front passes → table at
  rest → disclosure (if used): t+0 click → t+350ms rows revealed,
  focus stays on the control, its label changes to "Close the
  ledger".
- **State matrix (v2).** *Rest:* printed table. *Hover:* a row's
  ground deepens 4% (the reader's finger on the line). *Focus:*
  the disclosure control takes the focus ring (§11); rows are not
  focusable. *Expanded / collapsed:* as specced; state persists
  across scroll. *Disabled:* with JS off the disclosure renders
  expanded — the full ledger, statically.
- **Content merge.** The table is the page's data with its sleeves
  rolled up: the same rainfall the gauge measured and the figures
  counted, at weekly resolution, with the record lines that give
  the numbers their meaning. It is not a component placed near the
  content; it is the content's audit trail.
- **Failure fallback.** A plain HTML table — the most durable
  element on the page. Nothing about it can fail except its data,
  which is §10's business.
- **Reduced-motion variant.** Disclosure expands instantly; all else
  identical.
- **Breakpoints (v2).** ≥1200px: full 4-column table at the lee's
  measure. 768–1199px: the record column wraps under the date
  (rows become two-line). <768px: the table becomes a stacked list
  — each week a block: date + rainfall on one line, cumulative +
  record beneath — with the totals row pinned as the list's final
  block; horizontal scrolling tables are refused outright (§9).
- **Edge cases & failure modes (v2).** *A week with no rain:* the
  row prints "0 mm" and its record line says what a dry week meant
  ("Week 6 — 0 mm. The tanks were opened.") — a zero is data, and
  the ledger prints it; only *invented* numbers are banned.
  *Partial season (page published mid-monsoon):* rows stop at the
  last completed week, the totals row is labelled "TO DATE", and
  the gauge's full scale becomes the *forecast* total with its
  source named as the forecast — the one lawful use of a not-yet
  figure, declared as such in §6.5's caption and here.
  *Disagreement between totals and §6.16:* a build error, caught by
  §10's three-printings check, never resolved by editing the table
  to match silently — the source data is fixed, then all three
  printings follow.
- **Accessibility spec (v2).** Real `<table>` with `<th scope>` and
  a `<caption>` naming the season and the gauge ("Season ledger —
  the gauge's full scale is this table's total"). The disclosure is
  a `<button aria-expanded>`. Row hover deepening is redundant with
  position; nothing is conveyed by it. Contrast: body figures dry
  earth 7.48:1 on the soak ground; hairlines are graphical.
- **Performance budget & mobile variant.** Static. The disclosure is
  one height transition. Mobile: the stacked-list variant above.
- **Tokens consumed (v2).** `--new-leaf`, `--dry-earth`,
  `--ease-soak`, `--disclose-dur` (350ms).

### 6.18 The drought page (page family: 404 / empty state)

- **What & why.** A wrong address in this theme is a place the rain
  did not reach: the 404 is the one page of the site that stays dry
  — pale cracked ground, the crack (§6.6) drawn, no ramp, no green
  except the way home. It belongs because it is the theme's negative
  proof: the visitor sees, once, what the whole site would have
  been without the season, and the joke is told entirely in ground
  colour. The page's line, in the weather-note voice: "No rain fell
  here. This page was never in the season." — with the requested
  path printed as the place's name.
- **Structure.** A single dry section on `--dry-earth`: apparatus
  kicker "UNRAINED GROUND", the weather-note line as the `<h1>`'s
  companion (the `<h1>` itself is plain: "This page could not be
  found"), the requested path set in Source Sans mono-like tabular
  as the place name, struck through once in `--petrichor` (the
  clerk's correction colour — something was misaddressed), the
  crack drawn across the lower ground, and two links home: to the
  hero ("The start of the season") and to the ledger ("The season's
  record") — the way back is the way into the rain.
- **Motion spec.** One motion only: on load the crack draws (900ms
  `--ease-crack`, §6.6's own gesture) — the drought page's single
  event, after which the page is perfectly still. No ramp is
  applied to anything on this page, at any scroll position, ever:
  its dryness is total and permanent, the theme's one refusal.
- **Choreography timeline (v2).** t+0 page paints dry → t+150ms
  crack begins → t+1050ms crack complete → stillness.
- **State matrix (v2).** *Rest:* dry, cracked, still. *Hover /
  focus:* the home links behave per §6.10/§11, and clicking the
  primary link answers with §6.9's *dry* variant — the press and a
  dust puff, never a ripple: this page has no water, and its
  physics hold even here. *Scrolled-past:* n/a (one
  screen; if the viewport is short, the page scrolls and stays dry).
  *Disabled:* crack pre-drawn.
- **Content merge.** The struck path is the actual requested URL;
  the dryness is the actual situation (the season never reached
  this address). Nothing decorative is added — no mascot cloud, no
  illustration of a lost traveller (§9).
- **Failure fallback.** It is a static page with two links; there
  is nothing to fail.
- **Reduced-motion variant.** Crack pre-drawn; page identical
  otherwise.
- **Breakpoints (v2).** The single section takes the standard
  measure at all sizes; <768px the crack shortens to one branch.
- **Edge cases & failure modes (v2).** *A path that almost matches
  a real page:* a clerk's line may be added — "NEAREST RAINED
  GROUND: [page]" with its link — only when the match is real
  (slug similarity computed server-side); a guessed suggestion is
  forbidden (§1's invented-facts law). *Empty states generally*
  (a listing with no entries this season): they reuse this page's
  grammar at section scale — dry ground, one weather-note line
  ("Nothing was planted here this season."), the way onward —
  never a generic "no results" block.
- **Accessibility spec (v2).** The `<h1>` is the plain statement
  ("This page could not be found"); the weather note follows it —
  screen readers meet the meaning first, the climate second. The
  struck path is wrapped so it reads as "address attempted:" + the
  path, the strike presentational. Contrast: all text in
  `--mud-deep` / wet forest on dry earth (5.33:1 / 7.48:1).
- **Performance budget & mobile variant.** One 900ms draw, once.
  Mobile: the one-branch crack above.
- **Tokens consumed (v2).** `--dry-earth`, `--petrichor`,
  `--mud-deep`, `--wet-forest`, `--ease-crack`, `--crack-dur`
  (900ms).

## 7. Page application map

**Home — the season itself.** The canonical build: hero (§6.11) →
First Clouds (signs and the forecast, figures withheld or labelled
as forecast) → the Rain Moment (§6.2, the pin) → the Front Passes
(the main content, field cards §6.12) → the Soak (figures §6.16,
ledger §6.17) → the rain-letter form (§6.13) → the still-dripping
footer (§6.14). Most Monsoon Arrival sites are one page deep; the
season is the site.

**The season report / long-form story.** The home structure with the
Front Passes chapter extended: each report section is swept by its
own front (§6.4), weather notes (§3) date each turn, and the ledger
closes the argument. The copy change (§6.2) is used once, at the
story's own turning point — a report whose rain moment is not its
real turning point has placed the pin wrong, and no layout fixes it.

**Listing (harvest, tours, plantings).** Field cards (§6.12) in
chapter order: this season's listings in the wet chapters (beading,
full ramp), last season's in a dry chapter above them (pale, dust
hover, their figures dated last year) — the listing page's scroll is
a walk from last year's drought to this year's crop. Filters, where
needed, are apparatus lines (§11), never a toolbar.

**Detail (one field, one tour, one project).** A detail page opens
at the chapter its subject belongs to: a this-season subject opens
in the wet (ramp floor at its chapter value, §6.3 — detail pages
declare their starting ramp in the build, they do not replay the
whole season). Its gallery images ramp locally; its figures follow
§6.16; its booking/order form is §6.13 unchanged.

**About / the people.** The estate's or project's people are
presented as field cards (§6.12) with portraits, inside the chapter
of the season they joined — founders in the dry chapters (they
waited), this year's team in the wet. A résumé grid breaks the
fiction; credentials belong in the record line, dated.

**Checkout equivalents.** There is none beyond §6.13. A purchase
needing a cart, options matrix or payment form leaves the theme at
that step: hand off to a plainly designed transactional flow and
return to a Monsoon confirmation (the weather-note pattern of
§6.13). Pretending a payment form is a rain-letter is the theme's
most dangerous costume (§9).

**The drought page (404) and empty states.** §6.18, everywhere,
unchanged.

## 8. Worked examples

### 8.1 The hero — an estate's waiting

*The commission: a tea estate in the Western Ghats opens its season
site in late May. The rain has not come. The hero is §6.11.*

- **The composition.** Kicker: "THE DRY SEASON". Hero line: "The
  earth, waiting" — set once, in the fixed measure (§3 law 1),
  Newsreader at clamp(44px, 7.2vw, 84px). Weather note, dated:
  *"Last rain over the estate: 19 April. The forecast promises the
  monsoon by the second week of June."* One action: "Read the
  season" (anchor to First Clouds). The photograph: the estate's
  own valley in May, dust-pale, at ramp 0; its caption names the
  photographer and the date it was taken.
- **The first rain (§6.1).** Fonts settle; at t+80ms the cloud band
  enters; the shimmer over the headline dies at t+350ms as the
  first streaks fall; the headline's ink soaks from mud-deep to wet
  forest by t+1600ms; at t+1800ms the band is gone. The photograph
  does not change — this was a promise, not the monsoon. The crack
  (§6.6) has drawn across the photograph's foreground during the
  same window.
- **Scroll timeline.** 0–30vh: the visitor reads the note; the
  gauge (§6.5) sits at 0mm. 30–80vh: First Clouds enters, its front
  (§6.4) sweeps, the gauge creeps toward its 8% dry cap — the first
  spots in an empty gauge. The hero's photograph, scrolled past,
  holds its local cap; if the visitor returns to the top *now*, it
  is still dry. It will not be dry after the pin.

### 8.2 Mid-page — the rain moment and the first field

*The same site, chapter 3 into chapter 4.*

- **The pin (§6.2).** The section pins for 160vh. Its ground is
  ramp step 2 (§4). Rain (60 streaks) falls behind the copy-change
  block. At pin progress 0.45 the rain-line draws across "waiting"
  (500ms, `--ease-crack`); by 0.62 "the earth, breathing" stands at
  full opacity and the struck original rests at 60% beneath its
  line. In the left margin, the crack's endpoint greens over 600ms
  — the line becomes a root while the visitor watches the sentence
  change. The gauge unlocks.
- **The first field (§6.12).** The pin releases into chapter 4. The
  first field card — the estate's lowest field, the first to flood —
  is swept by its front (§6.4) and arrives beaded-ready (§6.7). Its
  record line: "First picking — 214 kg, 28 June." The visitor
  hovers: beads condense; the runner swells, releases, runs 30px
  down the card's face. The ramp is at ~0.55; the same card, seen
  in the §8.1 hero's dry grid last season, was pale and dusted.
- **What the visitor feels.** The sentence changed because the
  weather did; the margin line changed with it; the numbers from
  here on are wet numbers. Nothing announced any of this. The page
  simply stopped waiting.

### 8.3 Conversion — the rain-letter (harvest subscription)

*The estate sells a season subscription: four deliveries across the
monsoon. The form is §6.13, the last letter of the page.*

- **Arrival.** The sheet sits on the soak ground, its top dry-pale,
  its fields ruled: name, direction, the choice ("THE FULL SEASON —
  FOUR DELIVERIES" / "ONLY THE RAINS — TWO"), one free line ("A
  note for the packers — optional"). The submit reads "Send it into
  the season".
- **Interaction timeline.** The visitor tabs to the name field: its
  rule inks to first green (220ms), a bead forms at the rule's end.
  They complete name and direction; on each blur the sheet's wet
  layer steps up its lower edge — two of three required fields, the
  letter is two-thirds wet. They mistype the direction (no @): the
  rule turns petrichor, the desk notes beneath: "THE DIRECTION WILL
  NOT CARRY — CHECK THE ADDRESS." They correct it; the note clears,
  the bead re-forms. They choose the full season; the letter is
  fully wet at its lower 40%.
- **The sending.** Submit: the button ripples (§6.9), the wet layer
  completes (600ms), the gauge wobbles once in the header. The
  answer replaces the form (300ms fade — the theme's one lawful
  fade): a weather note — *"Received before the rains, 14 May.
  Your first letter follows the first storm."* — and beneath it the
  record line with the real order reference from the backend. If
  the post had failed, the letter would still be on the sheet, word
  for word, with "NOT SENT — THE POST FAILED. YOUR LETTER IS KEPT
  BELOW." beneath the button (§6.13).

## 9. Anti-slop — what makes THIS theme look cheap

1. **Rain as wallpaper.** A looping rain animation over unrelated
   content — a pricing grid, a settings page — with the copy
   unchanged. *Cure:* rain exists at exactly three moments (§6.1,
   §6.2's pin, §6.8's dripping), each attached to content it changes;
   if removing the content leaves the rain with nothing to fall on,
   it was weather; if not, it was wallpaper — delete it.
2. **The instant-green page.** Full saturation from the top because
   "the wet version looked better in review". *Cure:* the ramp is
   the theme; a build that starts soaked has no season, and §10's
   first screenshot test compares hero and footer saturation
   numerically.
3. **Invented rainfall.** A gauge scaled to a round, plausible
   number nobody measured. *Cure:* §1's law — the full scale is a
   sourced figure printed in the ledger (§6.17), or the gauge is
   not built.
4. **The copy change as a gimmick.** "Waiting → breathing" pasted
   onto a page whose subject never waited for anything. *Cure:* the
   struck line must be *true* of the content's before-state; §10
   asks the builder to state, in one sentence, what the site was
   waiting for — if the sentence is embarrassing, the theme is
   wrong for the content.
5. **Ripple everywhere.** Puddle ripples on dry-chapter buttons,
   beading on dry cards, dripping in the middle chapters. *Cure:*
   one physics per season (§6.7, §6.9); water before the rain moment
   is a continuity error, and §10 checks it like one.
6. **Percentage progress.** A "62% read" bar next to the gauge, or
   the gauge relabelled in percent "for clarity". *Cure:* progress
   is rainfall in millimetres (§6.5); percent is a foreign unit and
   is banned from the page (§12).
7. **Saturation doing contrast's job.** Text set in new leaf on dry
   earth because it "pops" in the dry chapters (1.52:1). *Cure:*
   §2's pairing table is law; §10 measures the actual pairs at the
   ramp's midpoint as well as its ends.
8. **Two rain moments.** A second pin with a second copy change
   because the page is long. *Cure:* a season breaks once (§4); a
   long page extends the Front Passes, never re-breaks.
9. **The costume checkout.** A payment form with ruled lines and a
   wax-seal submit. *Cure:* §7's handoff rule — leave the theme for
   the transaction, return for the confirmation.
10. **Generic empty states.** "No results found" in a grey box on a
    monsoon site. *Cure:* §6.18's grammar — dry ground, one weather
    note, the way onward.
11. **A horizontal-scrolling ledger** on mobile because the table
    "didn't fit". *Cure:* §6.17's stacked list; a table the visitor
    must pan is a table that failed.
12. **The shimmer that never dies.** Heat shimmer still running in
    the wet chapters (an ambient loop nobody switched off). *Cure:*
    the shimmer's life is bounded by §6.1's first streak, in code,
    not by intention.

## 10. Quality gate

**Blocking — the build may not ship while any item fails.**

1. **Saturation audit.** Sampled screenshots at progress 0, at the
   rain moment, and at the footer: image saturation measures
   0.55 ±0.03, ≥0.75, and 1.05 ±0.03 respectively (§6.3), and the
   hero's local cap holds (no hero image above its chapter cap
   before §6.1).
2. **Figure truth audit.** Every number on the page (gauge full
   scale, §6.16 figures, ledger totals, card record lines) traces
   to a supplied source named in its caption; the three printings
   of the rainfall total (gauge, §6.16, §6.17 totals row) agree to
   the digit.
3. **Copy-change test.** §6.2 fires once, at the pin, in order
   (strike before replacement), is irreversible in-session, and
   survives jump-scroll-past in its settled state; the struck
   original remains legible in the DOM and on screen.
4. **One-way audit.** After the rain moment: scrolling to the top
   shows ramp floor 0.5, wet grounds on visited sections, the root
   grown — nothing on the page has un-rained.
5. **Season-physics audit.** No water behaviour (ripple, beading,
   dripping, gauge fill beyond 8%) occurs anywhere before the rain
   moment; no dry behaviour (dust, shimmer) occurs after it.
6. **Contrast at the midpoint.** All text pairs measured at ramp
   0.5 and at every chapter ground step (§4) meet their declared
   ratios (§2); new leaf carries no text on any ground except wet
   forest.
7. **JS-off test.** The full page, JS disabled, is the soaked page:
   copy settled, gauge full, root drawn, all content present and
   readable; the 404 page is dry and complete.
8. **Pin discipline.** Exactly one pinned section (§6.2); the pin
   never traps focus; keyboard and reduced-motion visitors receive
   the section unpinned with identical content.

**Standard — fix before the theme is reused, note if shipped.**

9. Endpoint continuity of crack and root verified to the pixel
   (§6.6), rootlets equal to wet sections passed.
10. Gauge readout changes only at chapter boundaries; meniscus
    wobble fires once per boundary (§6.5).
11. Footer figures restate §6.16's values exactly, with dates
    (§6.14); the closing apparatus line's rainfall equals the
    gauge's full scale.
12. Every weather note carries a real date or place; no weather
    note sells anything (§3).
13. Frame budget held under §14's caps on a mid-range phone;
    dripping and shimmer are the first cuts and are observed to cut
    in that order.
14. The drought page (§6.18) applies no ramp at any scroll position
    and offers the nearest-rained-ground line only for real
    matches.

## 11. Component inventory

Every component a real Monsoon Arrival site needs, with its themed
treatment. Components the theme refuses are listed with their
in-world replacement — a refusal without a replacement is a gap, not
a stance.

- **Primary button.** Wet chapters: wet-forest ground, dry-earth
  text, §6.9 ripple on click, press = scale 0.98 over 120ms
  `--ease-soak`. Dry chapters: `--mud-deep` ground, dry-earth text,
  dust press (§6.9). One primary per view; its label is a verb in
  the season's voice ("Send it into the season", "Read the
  season").
- **Secondary button / link-button.** Ruled-line treatment: text in
  the chapter's ink over a 1px rule that inks to first green on
  hover/focus (220ms). Never a grey box.
- **Text link.** First green (dry/mid grounds) / new leaf (wet
  forest ground), underlined by the ground's hairline; hover
  deepens the underline to full ink over 180ms. Links never sit in
  new leaf on pale grounds (§2).
- **Inputs (text, email, textarea).** Ruled lines per §6.13: label
  in apparatus above, 1px `--cracked-mud` rule, focus inks the rule
  to first green + the bead. No boxes, no fills, no placeholders.
- **Radio / choice lines.** Full-width ruled lines in the letter
  voice (§6.13); the chosen line's rule inks first green and a bead
  sits at its end. Rendered as real `<input type="radio">` visually
  integrated, 48px hit rows.
- **Checkbox.** A small square of ruled ground that fills with
  first green and a dry-earth tick when checked (180ms
  `--ease-drip` — the fill lands like a drop). Used sparingly:
  consent and add-ons only.
- **Select.** **Refused.** A monsoon letter does not drop down.
  Replacement: choice lines (above) for ≤6 options; for more, a
  ledger-style list (§6.17) with the chosen row stamped.
- **Data table.** The ledger (§6.17) is the only table pattern:
  apparatus header, hairline rules, tabular figures, stacked list
  on mobile.
- **Badge / tag.** **Refused.** States are stamped lines in text
  (§6.12) or apparatus kickers — a coloured pill is foreign
  plastic on wet paper.
- **Alert / notice.** A weather note (§3) in a ruled block: the
  season's own voice announces ("The gauge road is closed this
  week — deliveries leave on Friday instead."). Error red is never
  used; corrections are `--petrichor` rules with mud-deep text
  (§6.13).
- **Toast.** **Refused.** Nothing on this site pops up from the
  bottom of the screen. Replacement: the confirmation weather note
  in place (§6.13) or the chapter apparatus updated at its boundary
  (§6.5).
- **Modal.** **Refused.** A season has no overlays. Replacement:
  content expands in place (the ledger disclosure, §6.17) or lives
  on its own page reached by the cloud-wipe (§6.15).
- **Tabs.** **Refused.** Chapters are the page's only segmentation,
  and they are scrolled, not tabbed. Replacement: the chapter nav
  (§6.10).
- **Accordion.** Permitted once, as the ledger disclosure (§6.17)
  and for long record lines in listings — styled as a ruled sheet
  unfolding, 350ms `--ease-soak`, never with a chevron icon (the
  label's words change: "The full ledger" / "Close the ledger").
- **Pagination.** **Refused** as numbered pages. A listing that
  outgrows one page continues by season ("Last season's fields" —
  an archive link in the dry chapter, §7), because the listing's
  order is chronological, not numerical.
- **Progress bar.** **Refused.** The gauge (§6.5) is the progress
  indicator; a bar anywhere on the page is a gate failure (§10.6's
  foreign-unit rule extends to foreign instruments).
- **Spinner.** **Refused.** Loading is the cracked sheet (§6.15);
  submitting is the button's words ("Sending — the post is going
  out", §6.13).
- **Tooltip.** **Refused.** Anything worth saying is said in a
  caption, a weather note or the ledger. The gauge ticks' hover
  reading (§6.5) is the single exception, and its values are also
  printed in the ledger.
- **Breadcrumb.** **Refused.** The chapter apparatus ("AFTER THE
  RAIN — THE SOAK") already states where the visitor is in the
  season; a second path is a second geography.
- **Card.** The field card (§6.12) is the only card.
- **Form errors.** Desk-voice notes beneath their fields (§6.13),
  persistent until corrected; a summary live region on submit
  failure only.
- **Empty state.** §6.18's grammar at section scale.
- **Focus ring (global).** 2px solid first green, offset 3px, on
  dry/mid grounds; 2px `--new-leaf` offset 3px on wet forest. Never
  removed, never replaced by a colour change alone.

## 12. Content & copywriting voice

Two voices, cast by §3 and never swapped. **The Weather** (Newsreader,
italic for notes, regular for headlines) observes the season: dated,
placed, unhurried. **The Record** (Source Sans) states facts:
figures, labels, forms, the ledger. A sentence's voice is chosen by
its job, not its importance — the harvest total is Record even when
it is the page's climax, and a two-word weather note is Weather even
in the footer.

**Headline style.** Short, present-tense, grounded in the subject's
own waiting or arriving. ✓ "The earth, waiting" / "The tanks are
full" / "First picking". ✗ "Welcome to our amazing estate
experience!" (exclamation, marketing tense, no ground in it) /
"Monsoon Mega Season 2026" (the season is not a sale).

**Weather notes.** Dated or placed, ≤34 words, observational, never
selling. ✓ "Last rain over the estate: 19 April. The forecast
promises the monsoon by the second week of June." ✗ "Don't miss
this year's incredible monsoon — book now!" (a note that sells is a
gate failure, §10.12).

**Labels & apparatus.** The apparatus names the weather, in
capitals, without ornament: "THE DRY SEASON", "FIRST CLOUDS", "THE
RAIN MOMENT", "AFTER THE RAIN", "THE SOAK", "STILL DRIPPING".
Buttons are verbs with their object: "Read the season", "Send it
into the season", "See the full ledger". ✗ "Submit", "Click here",
"Learn more" — verbs without a world.

**Figures.** Always with unit, source and period: ✓ "412 mm —
estate gauge, 1 June to 30 September". ✗ "412mm of rain!!" / "tons
of rain" (a figure without a source is unpublished, §3 law 2).
**Percentages are banned** for progress and rainfall alike; a
recovery figure may be a percentage only when the underlying
measure is itself a percentage (a reservoir's capacity), and then
its caption says of what.

**Error voice (the Desk).** Short, capitalised apparatus-style
notes that say what is wrong and what to do, without blame:
✓ "THE DIRECTION WILL NOT CARRY — CHECK THE ADDRESS." / "NOT SENT —
THE POST FAILED. YOUR LETTER IS KEPT BELOW." ✗ "Oops! Something
went wrong 😢" / "Invalid input" (the Desk names the field's
trouble in the world's words, and never apologises with emoji).

**Empty voice.** One weather note on dry ground: ✓ "Nothing was
planted here this season." / "No rain fell here. This page was
never in the season." ✗ "No results found." / "There's nothing
here yet — check back soon!" (soon is a promise the page cannot
date; the Weather never promises without a date).

**Confirmation voice.** A weather note with the real date: ✓
"Received before the rains, 14 May. Your first letter follows the
first storm." ✗ "Success! Your order #INV-2026-XXXX has been
confirmed" — and a reference is printed only when a real system
issued it (§6.13); an invented reference is an invented figure and
§1's law applies.

**Banned words.** amazing, incredible, stunning, ultimate, mega,
delve, unlock, elevate, seamless, "game-changer", exclamation marks
outside quotation. **Owned words.** waiting, breathing, the dry,
first clouds, the front, the soak, still dripping, gauge, ledger,
record, direction (for an address), letter (for a message or
subscription).

## 13. Full-page scroll choreography map

Eleven beats, top to footer, for the canonical home page (§7). The
map is the build's contract: a beat that cannot be pointed to in the
running page is a beat that was not built.

1. **Load — the dry.** Hero composed (§6.11), shimmer running,
   gauge at 0mm, crack undrawn. The visitor's first impression is
   thirst, held.
2. **t+80–1800ms — first rain.** §6.1's pass: band, streaks,
   headline soaks, shimmer dies, crack draws across the hero's
   foreground (§6.6).
3. **Chapter 2 entry — first clouds.** The first wet front (§6.4)
   sweeps the forecast section; the gauge creeps to its 8% dry cap
   and stops — anticipation, instrument-honest.
4. **The descent through the dry.** Crack extends down the margin
   (§6.6); images at ramp ≤0.35 locally; scroll is native and
   resistant (no glide — §5).
5. **The pin — the rain moment.** 160vh: rain falls, the copy
   changes (§6.2), the crack greens into the root at the margin,
   the gauge unlocks. The page's hinge; everything before was
   waiting, everything after is weather.
6. **Chapter 4 — the front passes.** Each section swept on entry
   (§6.4); the first field card beads under the visitor's hand
   (§6.7); scroll gains its wet glide for programme-driven movement
   (§5).
7. **Mid-descent.** Ramp crosses 0.75; root puts out rootlets per
   section (§6.6); gauge readout steps at each chapter boundary
   with its wobble (§6.5).
8. **The soak — figures.** §6.16 counts the season (rainfall,
   harvest) once, from their true baselines, captions sourced.
9. **The ledger.** §6.17 stands still and is consulted; its total
   is the gauge's full scale — the visitor who checks finds the
   page agreeing with itself.
10. **The letter.** §6.13's sheet wets as it is written; on submit,
    the gauge wobbles once in the header — the season acknowledges.
11. **The footer — still dripping.** §6.8's droplets run down the
    hero's landscape returned at full saturation; the colophon
    restates the figures; the closing line names the rainfall the
    gauge filled to. The visitor leaves a page that is still wet.

**Reverse pass.** Scrolling up after beat 5: grounds stay wet on
visited sections, the copy stays changed, the root stays grown, the
ramp holds its 0.5 floor, the gauge (alone) drains honestly with
reading position. Before beat 5, the reverse pass is a true reverse
— nothing has happened yet that cannot unhappen.

**Jump-scroll catch-up.** Any discontinuous jump (anchor, restored
position, find-in-page) resolves every beat at or above the landing
point instantly to its settled state: sections wet, counts at
value, copy settled if the pin was passed, root grown to the
landing chapter. A visitor must never land in a half-rained page.

**Pin law.** The one pin (§6.2) releases for keyboard focus (focus
moves through the section as ordinary flow), for reduced motion
(unpinned, settled), and on <768px shortens rather than disables —
the copy change is content, and content is never withheld from any
visitor class.

## 14. Whole-page performance budget

- **Assets.** Total page weight ≤ 1.4MB on the canonical home build:
  photographs ≤ 780KB total (hero ≤ 220KB — it is the LCP), fonts ≤
  120KB (Newsreader + Source Sans 3, subset, `font-display: swap`
  with the §6.1 watchdog covering late arrival), CSS ≤ 60KB, JS ≤
  45KB. No video, no canvas anywhere on the page — every effect in
  §6 is DOM/SVG/CSS by design.
- **Frame budget.** The shared loop's per-frame script cost ≤ 1.5ms
  on a mid-range phone: one root property write (ramp), one gauge
  rect, one dashoffset (active line segment), front writes for ≤2
  active sections. Filters are compositor work; the 12-image cap
  (§6.3) is the budget's enforcement.
- **Long tasks.** No task > 50ms after load; the rain fields (§6.1,
  §6.2) are built in one ≤8ms task after first paint. Counters and
  wobbles are timer-free — all inside the shared loop.
- **Cut order when the budget is exceeded** (in order, stop when
  back under budget): (1) the footer's dripping interval stretches
  4s → 8s, then dripping is cut to its static variant; (2) the heat
  shimmer (§6.11) is cut; (3) beading (§6.7) reduces to the painted
  cluster; (4) ramped images beyond 8 ship pre-saturated instead of
  live-filtered; (5) the cloud-wipe (§6.15) becomes instant
  navigation. **Never cut:** the ramp itself, the copy change, the
  gauge, the ledger, any fallback or watchdog — the season and its
  evidence are the page; the jewellery goes first.
- **Low-power rule.** If the loop measures sustained <40fps over 3s,
  cuts (1)–(3) apply automatically and the lerp rises to 0.2 so
  scrubbed values settle faster with fewer frames.

## 15. Build-order checklist

1. **Static soaked page first.** Build the complete page in its
   final state (copy settled, gauge full, root drawn, ramp 1) with
   no JS. This is the fallback, the reduced-motion page and the
   print page — it must be excellent alone (§10.7 tests it).
2. **Grounds and type.** Chapter ground steps (§4), text-pair swaps,
   the two voices (§3, §12) — verified at the midpoint before any
   motion exists.
3. **The ledger and figures as data.** §6.17's table from the real
   source data; §6.16's figures and the gauge's full scale derived
   from it — the three-printings agreement (§10.2) is checked on
   the static page.
4. **The shared loop.** One rAF loop, lerp 0.12, chapter watcher,
   session state (soaked set, rain-fired flag) — nothing animates
   before this exists.
5. **The ramp.** §6.3's root property, chapter caps, floor logic —
   with the loop's first consumer in place, verify §10.1's
   saturation audit on the static page's imagery.
6. **The gauge.** §6.5: dry cap, unlock, boundary readouts, wobble.
7. **Crack and root.** §6.6: measured paths, endpoint continuity
   check (§10.9), per-chapter segments.
8. **Wet fronts.** §6.4 per section, with zoning caps over text.
9. **The hero and first rain.** §6.11's composition, §6.1's pass,
   the shimmer's bounded life.
10. **The pin and the copy change.** §6.2, with jump-scroll
    catch-up and the focus/reduced-motion releases (§13's pin law).
11. **Cards and surfaces.** §6.12 cards, §6.7 beading/dusting,
    §6.9 ripple/dust — the seasonal physics pass, audited against
    §10.5.
12. **The form.** §6.13 with its wet layer, desk-voice errors and
    the no-loss failure path rehearsed (§8.3).
13. **Footer and drought page.** §6.14 + §6.8's dripping; §6.18
    built dry and verified ramp-free.
14. **Transitions and skeleton.** §6.15's cracked sheet and
    cloud-wipe, with watchdogs and the abort path.
15. **Gate.** Run §10 in order — blocking items first, on a
    mid-range phone and with JS off — and record the season's
    figures' sources in the build notes. A gate item that cannot be
    tested is a gate item that has failed.
