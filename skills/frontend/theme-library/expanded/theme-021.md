# 21. The Almanack — Expanded (v1 + v2)

*Expansion written to `EXPANSION-STANDARD.md` v1 + the v2 deepening pass
(50x standard), ordered 2026-11-23. This file is the complete, buildable
specification of theme #21. The original library entry's identity is
preserved exactly — the farmer's-almanac world, the true-phase corner
moon, the four palette anchors, Fraunces + Source Serif 4, stiff-leaf
chapter turns, ruled tide tables, the zodiac man — and deepened, never
redesigned. Where this file and the short library entry disagree, this
file governs.*

**The one law of the theme, stated before everything else:** every
astronomical and tidal figure on the page is either computed from the
visitor's real date by the stated formula, or printed from data the
publisher actually supplied for that place and month. An invented tide
height, a decorative moon at the wrong phase, or a planting count that
counts nothing is not a rounding error in this theme — it is a failed
build. The almanac has been trusted for three hundred years because
farmers bet crops on it. This site inherits that obligation.

---

## 1. Concept & world

The printed farmer's almanac is the oldest continuously published
periodical form in the English-speaking world: one cheap book, bought
once a year, that tells a household when the moon rises, when the tide
turns, which days to sow, which to let lie, what the weather will
*probably* do, and — tucked between the tables, in exactly the same
deadpan type — that they should beware of geese near the 14th. It is a
calendar, an astronomy lesson, a tide chart, a joke book and a household
ledger bound in one stiff paper cover, and it assumes its reader will
keep it by the door for twelve months and write in its margins.

The Almanack builds a website out of that book. The site does not
*theme itself* as old paper; it *behaves* as an almanac. It knows what
month it is. Its corner moon is drawn at tonight's true phase, computed
from the date, not chosen from a set of moon clip-art. Its chapters are
months and turn like stiff leaves. Its tables are ruled, dense and
real: tide heights, moon ages, planting-day counts that roll to
tonight's computed values when they enter. Its progress is measured in
the almanac's own elements — the moon waxing as the month's pages pass,
a tide-line rising in the margin as the reading deepens. Prognostications
are set in the same serif as the tides, because in an almanac a
prediction and a tide table carry the same typographic authority, and
the comedy — and there must be comedy — comes from that deadpan
equality.

**The world.** A kitchen table in late afternoon, the book open at this
month's spread: a woodcut of the harvest on the left, ruled tables on
the right, the moon printed small in the corner of the spread where
almanacs have always put it, the zodiac man — that strange flayed figure
ringed by signs, each pointing at the part of the body its sign governs
— standing beside the calendar where he has stood since the fifteenth
century. Somebody has marked a tide row with a thumb. Somebody has
pencilled a planting day. The pages are stiff; they do not flutter,
they *turn*, with effort, and lie flat with a slight bend of light
across them. That stiffness is the theme's physics. Nothing in this
theme bounces, floats or springs. Leaves turn, lines rule, moons wax,
tides rise. Slow forces, honestly rendered.

**Why the calendar must be real (the theme's ground).** An almanac
whose moon is wrong is worse than a site with no moon at all, because
the moon is a *claim*. The theme therefore computes phase from a stated
epoch (see §6.1: synodic month 29.530588853 days from the new moon of
2000-01-06 18:14 UTC), derives tonight's age and illumination from the
visitor's local date, and treats every other figure — tides, planting
days, days-in-month — as publisher data printed in the DOM, counted
from the DOM when a counter needs a total. A builder who cannot source
real tide data for a location does not fake the table; the table becomes
a moon-and-planting table (computable) and the absence is stated in the
table's own footnote. That honesty is not a limitation of the theme. It
is the theme.

**Mood.** Patient, dry, quietly funny, and useful before it is
beautiful. The emotional arc of a page is a month passing: the visitor
arrives at the month's opening spread, reads down through its days, and
leaves at the month's end with the moon nearer full (or nearer new)
than when they came. The copy sounds like a person who has edited the
book for thirty years and no longer wastes a word.

**Best-fit sites and audiences.**

- Gardening, seed and nursery brands whose customers genuinely plant by
  a calendar — the planting tables are the product's working tool.
- Coastal tourism, harbours, sailing and wild-swimming operators whose
  visitors need real tides for a named place.
- Seasonal food, farm shops and CSA schemes organised by month and crop.
- Wellness and retreat brands structured by lunar or seasonal cycles —
  only where the cycle is actually observed, not used as a mood word.
- Publishers of annuals, diaries and yearbooks: the site *is* the annual.

**When NOT to use it.**

- Anything that must be current to the minute: news, live sport, trading.
  The almanac's fastest honest unit is the day.
- Sites with no real calendar content. If there are no dates, tides,
  seasons or cycles to publish, the moon becomes clip-art and the law
  is broken on the first page.
- Dense SaaS, account dashboards, checkout-heavy commerce: ruled tables
  here are for reading, not for scanning fifty SKUs under time pressure.
- Brands that need a joke-free register throughout. The absurd
  prognostication is load-bearing (§9); removing it makes the rest of
  the book sound like it is pretending.

---

## 2. Palette

Four anchors, inherited from the original entry, plus derived tokens
that exist only to keep the anchors honest at text sizes and in the
night reading the theme's moon implies.

| Token | Hex | Role | Ratio | Pairing & contrast |
|---|---|---|---|---|
| `--paper` | `#F2EAD2` | Almanac paper; spread grounds, table grounds, card faces | 58% of the page | Ground for `--ink` text (≈14.6:1) and `--madder-deep` (≈6.9:1) |
| `--ink` | `#24211B` | Woodcut black; woodcuts, rules, display and body text, moon shadow | 26% | On `--paper` ≈14.6:1; the only colour a woodcut is printed in |
| `--madder` | `#A63A2A` | Madder red; thumb marks, prognostication markers, tide ticks, the zodiac man's pointing hand | 5% | ≈5.4:1 on `--paper` — display, rules and large labels only; never body text (see `--madder-deep`) |
| `--gold` | `#C99A2E` | Harvest gold; moon lit limb at full, zodiac ring, harvest marks, high-water ticks | 4% | ≈2.5:1 on `--paper` — graphic only by design; never text (see `--gold-deep`) |
| `--madder-deep` | `#8C2E21` | Derived: madder darkened one register for text-bearing uses | within the 5% | ≈6.9:1 on `--paper` — footnote text, error text, red labels under 18px |
| `--gold-deep` | `#86620F` | Derived: gold darkened for labels that must be read | within the 4% | ≈5.1:1 on `--paper` — table subheads, the moon-age caption when set in gold's role |
| `--ink-soft` | `#4A463C` | Derived: softened black for secondary table text, footnotes, captions | — | ≈8.9:1 on `--paper`; used where full `--ink` would shout in a dense table |
| `--paper-deep` | `#E4D7B4` | Derived: the turned leaf's underside, card reverses, skeleton ruled ground | — | One step behind `--paper`; carries no text alone except `--ink` at ≈11.8:1 |
| `--paper-shade` | `#D9C89E` | Derived: leaf-bend shading stop and pinned-spread shadow | — | Only ever a gradient stop on a turning leaf, never a flat surface |
| `--night` | `#1D1B16` | Derived: night-reading ground (see dark behaviour) | 7% in light scheme | `--paper` on it ≈13.9:1; the moon instrument panel and footer sit on it |
| `--rule` | `rgba(36,33,27,.92)` | Table rule colour at print strength | — | 1px rules; hairline variant `--rule-hair` at .38 alpha for row lines |
| `--moonlit` | `rgba(201,154,46,.16)` | Moonlight wash gradient stop for §6.9 | — | Only a moving wash over the spread, never a surface |

**Usage discipline.** The 58/26/5/4 ratio is measured on a month page at
rest, hero spread excluded. Madder above 8% of any viewport means every
row has been marked and therefore none has. Gold is the scarcest ink on
the page: the moon's lit limb, the ring, the high-water tick. A gold
button is a §9 failure on sight.

**Dark-mode behaviour.** There is no inverted-paper mode and no
preference toggle in the chrome. Under `prefers-color-scheme: dark`
the book is read by lamplight: spread grounds become `--night`, table
grounds become `#26231C`, text becomes `--paper`, rules become
`rgba(242,234,210,.8)`, woodcuts print in `--paper` with `--gold`
reserved for the same marks it makes in daylight. Madder lifts to
`#C65A46` (≈5.6:1 on `--night`) for its graphic roles and
`--madder-deep` is retired — red text in the dark scheme is set in the
lifted madder at 18px+ or in `--paper`. The corner moon does not change:
it was always a night instrument. A build that cannot restyle its
woodcuts for the night ground must not ship the dark scheme.

---

## 3. Typography

Two faces, inherited: **Fraunces** for display and **Source Serif 4**
for tables and text. No third face is admitted; figures, captions and
the editor's footnotes are all Source Serif 4 doing different jobs at
different sizes, because the printed almanac had one text fount and used
it for everything below the headline.

| Role | Face / weight | Size / line-height | Tracking | Rules specific to this theme |
|---|---|---|---|---|
| Display 1 — month name | Fraunces 72pt optical, 560 | 64px / 1.02 desktop, 44px <768px | −0.01em | The month's name only. One per spread. Never a slogan in its place. |
| Display 2 — chapter heads | Fraunces 560 | 36px / 1.1 | −0.005em | Chapter = a month part (The Tides, Planting, Prognostications). Always paired with its ruled head (§6.5's ring may sit beside it). |
| Heading — table titles | Source Serif 4 600 | 19px / 1.25 | 0 | A table title names place and month: “Tides at Harboursmouth — November”, never “Tide times”. |
| Body — prognostications & prose | Source Serif 4 400 | 17.5px / 1.62 | 0 | Deadpan serif. Prognostications are body text, not display — their authority comes from being set like facts. |
| Table text | Source Serif 4 400 | 15px / 1.45 | 0 | Dense and ruled. Numerals tabular (`font-variant-numeric: tabular-nums`) in every cell, without exception. |
| Table figures — heights, times | Source Serif 4 600 | 15px / 1.45 | 0.01em | Heights to one decimal with unit once per column head (m), times 24-hour with the zone named once per table. |
| Caption / footnote | Source Serif 4 400 italic | 13.5px / 1.5 | 0 | The editor's voice lives here. Absurd footnotes are italic; factual footnotes are roman — the reader learns the code in one page. |
| Data label — moon age, counts | Source Serif 4 600, small caps | 12.5px / 1.3 | 0.14em, uppercase | Labels are engraved, not shouted: small, spaced, `--ink-soft` or `--gold-deep`. |
| The date line | Fraunces 480 | 21px / 1.2 | 0 | Today's full date as the almanac prints it: “Tuesday 11 November”, weekday first, no year unless the page is an archive year. |

**Type laws.** (1) Numerals in tables never kern and never use old-style
figures — a tide height is read at arm's length on a wet pier. (2)
Prognostications never use exclamation marks; the deadpan is the joke's
mechanism (§12). (3) The zodiac man's labels are set in the data-label
style, rotated only where the printed figure rotates them, and never
below 11px. (4) Fraunces is never used inside a table. (5) A headline
that names a month must name the *current* month for the visitor unless
the page is explicitly an archive spread, in which case the year joins
the date line.

---

## 4. Layout language

**The spread is the unit.** Every page is composed as a sequence of
opening spreads — two facing leaves — even on a single-column phone,
where the spread becomes a stack in the same reading order: woodcut or
instrument first, tables second, prognostications last. A section that
cannot say which leaf it sits on does not belong on the page.

**Grid.** Desktop ≥1200px: a 12-column grid inside a 1240px measure,
but tables and spreads are laid on a stricter inner measure of 1120px
centred, leaving the outer columns as the **margin** — a real margin,
120–160px, which is working space: the tide-line rises in it (§6.7),
thumb marks appear in it (§6.10), the corner moon's caption sits in it
on archive pages. At 768–1199px the measure is fluid with 32px gutters
and the margin narrows to 56px (tide-line survives, thumb marks move
inside the table edge). Below 768px: single column, 20px gutters, the
margin is abolished and its instruments move inline (§6.7, §6.10).

**Spacing rhythm.** The vertical unit is the **ruled line**: 8px base,
table rows at 5 units (40px) desktop and 44px on touch, spread padding
at 12 units (96px) top and 10 units (80px) bottom, chapter gaps at 16
units (128px) — the stiff leaf needs room to turn. Nothing sits on a
spacing value that is not a multiple of 8 except the moon instrument,
which is centred optically in its corner and exempt by three centuries
of precedent.

**Density rules.** Tables are dense (15px text, 40px rows, hairline row
rules, full rules at head and foot) and everything around them is not:
one woodcut per spread, one prognostication column per spread, at most
three instruments (moon, ring, tide-line) visible in any viewport.
Density alternates — ruled table, open spread, ruled table — so the eye
rests the way it rests turning from a table page to a picture page.

**Whitespace as material.** The bare paper at a chapter bound is the
leaf that is about to turn; it is never filled with a banner, a badge
or a newsletter strip. The footer spread is the emptiest on the page:
the book closing.

**Placed imperfections.** One per spread, maximum: a thumb-marked row,
a slightly heavier rule where the leaf was scored, the zodiac man's
hand resting at today's sign. Imperfections are placed in the build,
never randomised per visit — the book the visitor returns to tomorrow
is the same book.

---

## 5. Full motion system

Five named easings carry the whole theme. No other easing is admitted.

| Token | Curve | Used by |
|---|---|---|
| `--ease-leaf` | `cubic-bezier(.22,.9,.26,1)` | Leaf turns, sheet feeds — stiff paper accelerating late |
| `--ease-rule` | `cubic-bezier(.4,0,.2,1)` | Rules drawing, lines ruling in, ring and moon outline draw |
| `--ease-wax` | `linear` scrubbed (no easing) | Moon waxing, tide-line rising, temperature drift — astronomical forces do not ease |
| `--ease-settle` | `cubic-bezier(.2,.7,.3,1)` | Rows filling, cards landing, moon drawing last in a sequence |
| `--ease-tap` | `cubic-bezier(.3,1.4,.5,1)` | The zodiac man's tap and the thumb mark's smudge — the only overshoot in the theme, rationed to hands |

**Duration tokens.** `--dur-row: 60ms` stagger per table row;
`--dur-rule: 600ms` a full rule draw; `--dur-leaf: 640ms` a stiff leaf
turn; `--dur-draw: 1000ms` the hero ring/moon draw; `--dur-roll: 800ms`
a real-data odometer roll; `--dur-unfold: 350ms` a footnote unfold;
`--dur-tap: 200ms` the zodiac tap; `--dur-mark: 200ms` the thumb mark.

**Every motion term, in this theme's language:**

- **Scroll-triggered reveals** — spreads assemble in printed order:
  woodcut first (opacity + 1.03→1 scale-in-frame, 500ms `--ease-settle`),
  tables ruling in second (head rule draws 600ms `--ease-rule`, rows
  fill at 60ms stagger), instruments last (moon/ring draw 1000ms).
  Trigger: 78% viewport line, once per spread per session.
- **Scroll-driven / scrubbed animation** — the corner moon waxes and
  the margin tide-line rises, both scrubbed 1:1 to scroll through the
  month's pages with rAF lerp 0.12 (§6.1, §6.7). Scrubbed values never
  ease; the hand is moving the month.
- **Parallax** — woodcut plates drift at 0.92× scroll speed against the
  ruled tables they interrupt (max 18px travel), because a printed
  picture sits *in* the leaf while a table is read *on* it. Nothing
  else parallaxes.
- **Pinned sections** — one pin per page: the month's opening spread
  pins for 120vh while its daily tables scroll beneath (§6.4). Pin
  retires <900px viewport height, <768px width, and under reduced motion.
- **Staggered reveals** — table rows only, 60ms per row, capped at
  14 rows animating; longer tables fill the remainder instantly (a
  31-row month table must not take 1.9s to exist).
- **Masked line reveals** — prognostications reveal through a
  woodcut-frame clip-path: the frame's inner rectangle expands from
  88% to 100% width over 500ms `--ease-settle`, text static inside.
  Text itself never masks or splits; almanac prose is not a headline act.
- **Blur-to-sharp** — refused for text. Licensed once: a woodcut plate
  entering focus goes from 1.2px blur to sharp over its scale-in-frame,
  because a picture coming into lamplight is a physical event and a
  blurred sentence is not.
- **Kinetic typography** — refused. The month name does not move. The
  only moving letterforms are odometer digits (§6.8) and the zodiac
  labels carried by the turning ring (§6.5).
- **Marquee** — refused. Nothing in a printed almanac crawls. A
  publisher who needs a notice prints it as a prognostication and lets
  it be read.
- **Counters** — moon age, tide heights, planting-day counts roll as
  odometer digits over 800ms `--ease-settle` to tonight's real values
  (§6.8). A counter's target is computed or counted from the DOM; an
  invented target fails §10.
- **Progress indicator** — the moon itself (phase = position in the
  month's reading) plus the margin tide-line (§6.7). No bar exists.
- **Ambient loops** — two only: harvest dust drifting in the hero
  (§6.9, ≤14 motes, paused off-screen) and the moonlight temperature
  drift (§6.9, ±3% warmth, scrubbed not looped). The page otherwise
  holds still, like a book.
- **Micro-interactions** — thumb-mark hover (§6.10, 200ms), footnote
  unfold (§6.11, 350ms), zodiac tap (§6.6, 200ms), woodcut plate tilt
  ≤2° (§6.15). Each is a reader's gesture, not a UI effect.
- **Page transitions** — a stiff leaf flip with bend shading, 450ms
  `--ease-leaf` (§6.12). Back/forward reverses the leaf's direction.
- **Image scale-in-frame** — woodcuts scale 1.06→1 inside their ruled
  frames over 700ms `--ease-settle` as the frame enters; the frame
  never moves.
- **SVG line-draw** — the zodiac ring, the moon outline, the tide-line's
  surface wave and the colophon fleuron draw by dashoffset at
  `--ease-rule` speeds (§6.5, §6.7, §6.17).
- **Skeleton loading** — ruled empty tables that fill row by row
  (§6.12): the skeleton is the table's own ruling with no figures yet.
- **Reduced motion** — §6 variants per element; globally: moon shown at
  tonight's phase statically, leaves become plain scroll, tables print
  complete, dust and drift off. No information is motion-only in any
  variant.

**Scroll architecture.** One shared `requestAnimationFrame` loop,
lerp 0.12, drives moon waxing, tide-line, temperature drift and woodcut
parallax from a single lerped scroll value. Timed animations (draws,
turns, rolls) run on CSS/WAAPI and never write to the loop's values.
The loop sleeps when the tab is hidden and when no scrubbed element is
within 1.5 viewports.

---

## 6. Signature elements

### 6.1 True-phase moon

- **What & why.** A 56px SVG moon in the spread's top corner, drawn at
  tonight's actual phase and waxing (or waning) scrubbed as the visitor
  scrolls through the month's pages. It is the theme's calendar
  instrument, its progress indicator and its proof of honesty in one
  object. Almanacs print the moon in the corner of the spread; this one
  is correct.
- **Structure.** Inline SVG: a circle clipped by an ellipse mask whose
  rx is computed from the phase fraction. Phase computation, stated so
  two builders produce the same moon: synodic month `S = 29.530588853`
  days; epoch new moon `E = 2000-01-06T18:14:00Z`; age
  `A = ((localDate − E) / 86400000) mod S`, using the visitor's local
  *date* at noon to avoid timezone edge flips; illumination
  `k = (1 − cos(2πA/S)) / 2`. The terminator ellipse rx is
  `|1 − 2k| × r`, filled on the waxing side when `A < S/2`, waning side
  otherwise. A caption beneath, in data-label type, prints the computed
  truth: “Moon age 11.3 days · Waxing gibbous”. Phase names follow the
  standard eight divisions of A/S. Scroll scrub adds a *reading offset*:
  across the month page's full scroll, the displayed age advances by up
  to +6 days from tonight's true age, and the caption gains the word
  “by month's end” when the offset exceeds 0.5 day — the scrub is a
  preview of the month, never a silent falsification of tonight.
- **Motion spec.** Initial draw: outline draws 1000ms `--ease-rule`
  last in the hero sequence (§6.5 shares the beat). Scrub: displayed
  age = true age + (lerped scroll progress through the month page × 6
  days), updated in the shared rAF loop, `--ease-wax` (linear). The
  mask is recomputed per frame only when the age changes by ≥0.02 day.
  Recompute on local midnight rollover if the page is left open
  (checked every 60s against the stored date).
- **States.** *Rest:* tonight's phase, caption true. *Scrubbed:* age
  advanced per above, caption amended. *Scrolled-past:* the moon stays
  in its corner — it is chrome of the book, not a section. *No-JS:*
  server or build renders the phase for the build's date with the
  caption “Moon at printing” and a static crescent fallback image
  behind the SVG.
- **Content merge.** The moon *is* the month's data, printed where the
  book prints it. Remove the animation and the correct moon remains.
- **Failure fallback.** If the date computation throws, the static
  crescent fallback shows with the caption “Moon” and no age figure —
  a silent instrument, never a wrong one. A 1200ms watchdog forces the
  drawn state if the draw animation is interrupted.
- **Reduced-motion variant.** No scrub, no draw: the moon appears at
  tonight's phase with its true caption. Scrolling changes nothing.
- **Performance budget & mobile variant.** One SVG mask recompute per
  changed frame; ≤0.4ms per frame. Mobile: 44px moon, caption shortens
  to age only (“Age 11.3 d”), scrub range reduces to +4 days.

#### 6.1 v2 — Choreography timeline

| Beat (from page load) | What happens |
|---|---|
| 0ms | Static fallback moon visible (correct at build date) |
| fonts ready / 300ms cap | Hero sequence starts (§6.14); moon waits |
| +700ms | Woodcut and tables have landed; moon outline begins draw |
| +700–1700ms | Outline draws; mask fades from fallback to computed phase |
| +1700ms | Caption types in as printed text (no animation beyond 150ms fade) |
| first scroll | Scrub engages only after 40px of scroll, so a resting page shows tonight, truly |

#### 6.1 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | True phase, full caption | True phase, age-only caption |
| Hover | Caption expands to add illumination % (150ms) | n/a — no hover |
| Focus | Moon is not focusable; its caption is plain text in reading order | Same |
| Active | n/a | n/a |
| Scrolled-past | Remains fixed in spread corner; scrub continues | Remains; scrub range +4d |
| Disabled | n/a — if computation fails, static fallback state (above) | Same |

#### 6.1 v2 — Breakpoint behaviour

≥1200px: 56px, full caption, margin corner. 768–1199px: 48px, caption
keeps age + phase name, illumination % dropped. <768px: 44px, sits in
the date line's row (the margin is abolished), age-only caption.

#### 6.1 v2 — Edge cases & failure modes

Clock set wrong on the visitor's device: the moon is wrong honestly —
the caption's age lets a knowledgeable reader catch it, and the theme
does not pretend otherwise. Page open across midnight: 60s check
recomputes and crossfades the mask over 600ms. Page open across a
month boundary: the scrub base stays the *page's* month; tonight's
caption updates. Leap years and DST: age uses date arithmetic on local
noon, immune to 23/25-hour days. Scroll-back: the offset reverses
exactly; at offset 0 the caption's amendment word disappears.

#### 6.1 v2 — Accessibility spec

The moon is decorative-with-data: `role="img"`, `aria-label` = the
caption text (“Moon age 11.3 days, waxing gibbous”). The visible caption
is real text immediately after it in DOM order. Contrast: moon ink on
paper 14.6:1; caption `--ink-soft` 8.9:1. No interaction, no focus.
Scrub changes are not announced (they are ambient); the true tonight
values are present in text from first paint.

#### 6.1 v2 — Tokens consumed

`--paper, --ink, --gold` (lit limb at k ≥0.92 only), `--ink-soft`,
`--ease-rule, --ease-wax, --dur-draw`, `--moon-size` (56/48/44px),
`--synodic: 29.530588853`, `--epoch-new-moon: 2000-01-06T18:14Z`.

### 6.2 Stiff leaf chapter turns

- **What & why.** At each chapter bound the current leaf turns: it
  rotates on its left edge to −18° and back to flat while a bend-shading
  gradient sweeps across it, revealing the next chapter already printed
  beneath. Stiff, effortful, flat again — paper, not a page-curl toy.
- **Structure.** Each chapter is a `<section class="leaf">` in a stack
  context; the turning leaf carries a `::after` gradient
  (`--paper` → `--paper-shade` → `--paper-deep`) whose position is
  driven by the turn progress. `transform-origin: left center`,
  `perspective: 1600px` on the chapter container. The next chapter is
  ordinary DOM beneath, fully rendered before the turn begins.
- **Motion spec.** Turn zone: 50vh of scroll centred on the chapter
  bound. Progress scrubbed through the shared loop: rotation
  0→−18° over the first 60% of the zone, hold 10%, −18°→0 over the
  last 30%; shading gradient sweeps left→right across the same span.
  Maximum rotation is −18° by law — a stiffer leaf reads as paper; −90°
  reads as a door.
- **States.** *Rest (before bound):* flat, shading at 0%. *Turning:*
  per above. *Scrolled-past:* flat, shading gone; the leaf is read.
  *Scroll-back:* the turn reverses symmetrically through the same zone.
- **Content merge.** The turning leaf is the chapter's own first page;
  the reveal is the next chapter's actual opening, not a teaser card.
- **Failure fallback.** No transform support or JS off: chapters are a
  plain vertical stack with a full rule at each bound — the book
  without the turn, complete. Watchdog: if scroll leaves the zone
  mid-turn (jump scroll), the leaf snaps to the nearest flat state in
  120ms rather than resting bent.
- **Reduced-motion variant.** No rotation, no shading: a 24px paper
  gap and the bound's rule mark the chapter change.
- **Performance budget & mobile variant.** One transform + one gradient
  position per frame, only within a turn zone; ≤0.5ms/frame. Mobile:
  rotation capped at −10°, perspective 1100px, zone 36vh — a smaller
  leaf in a smaller hand.

#### 6.2 v2 — Choreography timeline

| Scroll position in 50vh zone | Leaf |
|---|---|
| 0–10% | Flat; hairline shadow gathers at the bound (opacity 0→.5) |
| 10–70% | Rotates 0→−18°; bend gradient sweeps 0→100% across the leaf |
| 70–80% | Holds at −18° — the stiff leaf's pause at the top of its turn |
| 80–100% | Rotates −18°→0 onto the next chapter; shadow releases |

#### 6.2 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Flat leaf, rule at bound | Flat, rule at bound |
| Hover | n/a — leaves are not hover targets | n/a |
| Focus | Focus inside a turning leaf is never moved by the turn; the leaf is a visual layer over static DOM order | Same |
| Active | n/a | n/a |
| Scrolled-past | Flat, read | Flat, read |
| Disabled | Transform disabled → stack fallback | Same |

#### 6.2 v2 — Breakpoint behaviour

≥1200px: −18°, 50vh zone, 1600px perspective. 768–1199px: −14°, 44vh,
1300px. <768px: −10°, 36vh, 1100px, and the bend gradient simplifies to
two stops.

#### 6.2 v2 — Edge cases & failure modes

Jump scroll (anchor link, find-in-page): leaf snaps flat in 120ms, no
turn is owed. Very long chapter: the turn belongs to the bound only;
length changes nothing. Short chapter (<60vh content): zones of
adjacent bounds must not overlap — the later bound's zone starts only
after the earlier leaf is flat; if they would overlap, the earlier turn
shortens to 30vh. Low-power device (<40fps in the shared loop): turns
degrade to the reduced-motion gap for the rest of the session.

#### 6.2 v2 — Accessibility spec

Purely visual: the turning layer is `aria-hidden`, DOM reading order is
the chapter order, and no content exists only on a turned leaf. Focus
is never trapped or moved. The effect respects `prefers-reduced-motion`
with the gap variant. Contrast is unaffected — text never rotates with
the leaf's shading layer (shading is on `::after`, above the ground,
below nothing textual: text sits on the *next* chapter, revealed flat).

#### 6.2 v2 — Tokens consumed

`--paper, --paper-deep, --paper-shade, --rule, --ease-leaf, --dur-leaf`,
`--leaf-angle` (−18/−14/−10°), `--turn-zone` (50/44/36vh).

### 6.3 Row-by-row tide tables

- **What & why.** The theme's data heart: ruled tables of tides (or,
  where tides do not apply, moon/planting tables) whose rows fill one
  by one as the table enters — the table being ruled and written in
  front of the reader, in the order it will be read.
- **Structure.** A real `<table>`: caption naming place and month,
  column heads with units stated once (Time, Height m, and where
  supplied, Range), body rows in DOM order. The head rule and foot rule
  are 1.5px `--rule`; row hairlines `--rule-hair`. Fill animation is an
  opacity + clip treatment on row groups applied by JS only; the
  printed table is the default state.
- **Motion spec.** On entry at the 78% line: head rule draws left→right
  600ms `--ease-rule`; then rows fill at 60ms stagger, each row 220ms
  `--ease-settle` (opacity 0→1, its hairline drawing with it), capped
  at 14 animated rows — rows 15+ are present instantly. Heights that
  are also §6.8 counters roll within their cells on the same beat.
  High-water rows carry a gold tick in the margin column of the table
  itself; low-water rows carry none — the table's own emphasis, printed.
- **States.** *Rest:* complete printed table. *Entering:* per above,
  top-down, never bottom-up. *Hover:* §6.10 thumb mark. *Scrolled-past:*
  complete; re-entry does not re-fill (the table has been written).
- **Content merge.** The rows are the data. There is no decorative
  table anywhere in the theme.
- **Failure fallback.** JS off or IO unsupported: the complete table,
  ruled, from first paint. A 1000ms watchdog fills any row still
  unfilled. Slow network: the table is HTML, not fetched — it cannot
  arrive late; client-fetched tide data uses §6.12's skeleton and, on
  failure, prints the moon table instead with a footnote saying so.
- **Reduced-motion variant.** Complete table on entry; head rule
  printed. No stagger, no roll.
- **Performance budget & mobile variant.** ≤14 concurrent row
  animations, transform/opacity only. Mobile: rows become 44px,
  the Range column (if any) is dropped first, then the table scrolls
  horizontally inside its ruled frame only if it still cannot fit —
  a table is never shrunk below 14px text.

#### 6.3 v2 — Choreography timeline

| Beat (from 78% entry) | What happens |
|---|---|
| 0ms | Table frame and caption visible; head rule begins draw |
| 0–600ms | Head rule draws; column heads fade in at 300ms |
| 300ms | Row 1 begins fill |
| 300 + n×60ms | Row n fills (220ms each, overlapping) |
| Row 14 cap | Remaining rows present instantly at their stagger beat |
| Last row + 100ms | Foot rule draws (400ms); table is complete |

#### 6.3 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Printed table | Printed table, 44px rows |
| Hover (row) | §6.10 thumb mark + row ground warms 3% | n/a |
| Focus (row/cell link) | 2px madder outline inside the row, thumb mark also appears | Same outline |
| Active | n/a | n/a |
| Scrolled-past | Complete, no re-fill | Complete |
| Disabled | A datum the publisher could not supply prints as “—” with a footnote, never as 0 | Same |

#### 6.3 v2 — Breakpoint behaviour

≥1200px: full columns, margin ticks visible. 768–1199px: Range column
dropped, ticks move to the table's first column. <768px: two-column
minimum (Time, Height) guaranteed; additional columns stack beneath
the row as a sub-line at 13.5px rather than truncating.

#### 6.3 v2 — Edge cases & failure modes

A month table with 62 rows (two tides a day): the 14-row cap keeps
entry under 1.2s; the rest is simply there. A table with 3 rows fills
without ceremony (stagger shortens to 40ms). Missing datum: em-dash +
footnote, per matrix. Conflicting source data: the publisher's footnote
names the source and year; the theme never silently averages two
sources. Content longer than the design (a named storm note): prints
as a full-width row in italic caption style, breaking the grid openly
rather than overflowing a cell.

#### 6.3 v2 — Accessibility spec

Real table semantics: `<caption>`, `<th scope="col">`, row headers
where the day is the key. The fill animation is `aria-hidden` in
effect only — rows are in the accessibility tree complete from first
paint (animation is opacity on present DOM). Gold ticks have a text
equivalent: high-water rows carry “(high water)” in a visually-hidden
span and the column head explains the tick once. Contrast: cell text
14.6:1, secondary 8.9:1, hairlines are decoration.

#### 6.3 v2 — Tokens consumed

`--paper, --ink, --ink-soft, --gold, --rule, --rule-hair, --ease-rule,
--ease-settle, --dur-row, --dur-rule`, `--row-h` (40px / 44px touch).

### 6.4 Pinned month spread

- **What & why.** The month's opening spread — woodcut, month name,
  date line, the corner moon — pins for 120vh while the month's daily
  tables scroll beneath its lower edge, the moon waxing above them all.
  The month stays present while its days are read, exactly as a held
  almanac's cover spread stays in the other hand.
- **Structure.** A `position: sticky` spread inside a 220vh section
  (100vh spread + 120vh pin travel). The daily tables live in a
  following container that translates up beneath the spread's bottom
  rule; the spread casts a `--paper-shade` shadow onto them. The moon
  (§6.1) lives inside the pinned spread and keeps scrubbing.
- **Motion spec.** Pin engages when the spread's top reaches the
  viewport top; releases after 120vh of travel, when the spread scrolls
  away with a final 300ms `--ease-leaf` settle. Tables beneath move at
  natural scroll speed (no counter-parallax — they are being read).
  The spread's own content does not animate during the pin except the
  moon and the §6.9 temperature drift.
- **States.** *Approach:* spread assembles per §5 sequence. *Pinned:*
  static except moon/drift. *Released:* scrolls away; its shadow lifts
  over 200ms. *Scrolled-past:* gone; the month name persists only in
  the running head of later chapters.
- **Content merge.** The pinned object is the month's cover and
  calendar; the tables scrolling beneath are its own days. The pin is
  the reading structure, not a hero trick.
- **Failure fallback.** No sticky support: spread and tables stack
  normally; nothing is lost. Pin disables itself under 600px viewport
  height (a short window cannot spare the room) and the spread simply
  heads the page.
- **Reduced-motion variant.** No pin. The spread heads the page and
  the tables follow; the moon is static at tonight's phase.
- **Performance budget & mobile variant.** The pin is compositor
  sticky; the only per-frame work is the shared loop's moon/drift.
  Mobile <768px: no pin (a phone's spread is its whole screen; pinning
  it would leave no room for the days).

#### 6.4 v2 — Choreography timeline

| Scroll beat | What happens |
|---|---|
| Spread top hits viewport top | Pin engages; shadow appears over 200ms |
| Pin travel 0–120vh | Daily tables scroll beneath; moon scrubs +0 to +2 days within this section alone |
| Travel 120vh | Release: spread scrolls away, 300ms settle, shadow lifts |
| Re-entry from below | Spread returns unpinned until its top re-reaches the top |

#### 6.4 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Spread at page head | Spread at page head, unpinned |
| Hover | Instruments behave per their own specs (§6.1, §6.5) | n/a |
| Focus | Focusable content inside the pinned spread remains reachable in DOM order throughout the pin | n/a (no pin) |
| Active | n/a | n/a |
| Scrolled-past | Released, gone | Scrolled normally |
| Disabled | Sticky unsupported → stacked fallback | Stacked |

#### 6.4 v2 — Breakpoint behaviour

≥1200px: pin 120vh. 768–1199px: pin shortens to 80vh (smaller windows
spend less time under the spread). <768px: no pin. Viewport height
<600px at any width: no pin.

#### 6.4 v2 — Edge cases & failure modes

Daily tables shorter than the pin travel: travel shortens to the
tables' height — the spread never pins over emptiness. Tables longer:
they continue after release as ordinary chapters. Jump scroll past the
section: no pin state is owed; the spread is simply past. Scroll-back:
the pin re-engages symmetrically. A second month on the same page
(archive index) never pins — one pin per page, by law (§5).

#### 6.4 v2 — Accessibility spec

Sticky positioning does not change DOM or focus order; the tables are
after the spread in reading order whether pinned or not. The shadow is
decorative. Under reduced motion the layout is the fallback layout —
identical content, identical order. No content is only visible during
the pin.

#### 6.4 v2 — Tokens consumed

`--paper, --paper-shade, --ink, --ease-leaf`, `--pin-travel`
(120vh / 80vh / 0), `--spread-h: 100vh` (min 640px).


### 6.5 Zodiac ring + moon draw

- **What & why.** In the hero spread, the zodiac ring — twelve signs in
  a circle, tonight's sign marked in gold — and the moon's outline draw
  themselves in SVG, in the order the spread was printed: woodcut first,
  tables second, ring and moon last. The draw is the book being made in
  front of the reader, once.
- **Structure.** One inline SVG (viewBox 0 0 200 200): outer ring
  circle, twelve sign glyphs placed by rotation transforms at 30°
  intervals, an inner circle, and a pointer line to tonight's sign.
  Tonight's sign is computed from the local date by the standard
  tropical date ranges printed in §12's table — a date claim, so it
  follows the one law: the ranges are stated, the computation is shown
  in the caption (“The sun in Scorpio — to 21 Nov”). The moon outline
  is §6.1's SVG, drawn on the same beat.
- **Motion spec.** Draw: ring circles by dashoffset 1000ms
  `--ease-rule`; sign glyphs fade in at 60ms stagger starting at 500ms,
  in zodiac order from tonight's sign (the ring assembles around
  today); pointer line draws 300ms at 900ms; tonight's sign fills gold
  at 1100ms. Moon outline draws simultaneously per §6.1. Once per
  session; revisits show the ring printed.
- **States.** *Rest:* printed ring, tonight's sign gold, pointer set.
  *Hover (a sign):* that sign's dates print beneath the ring (150ms) —
  the ring is a working diagram. *Scrolled-past:* printed. *Focus:* the
  ring is an image with a text equivalent (below), not a control.
- **Content merge.** The ring diagrams the same date the date line
  prints. Its caption and the date line cannot disagree — both derive
  from the one date computation.
- **Failure fallback.** No SVG animation support: ring appears printed.
  Watchdog 1200ms forces the drawn state. If the date is unavailable,
  no sign is gilded and the caption omits the sun line — never a
  guessed sign.
- **Reduced-motion variant.** Ring printed complete, tonight's sign
  gold. No draw, no stagger.
- **Performance budget & mobile variant.** One dashoffset animation +
  twelve fades, once. Mobile: ring shrinks to 120px, sign glyphs remain
  (they are the content), hover dates become a printed line under the
  ring for tonight's sign only.

#### 6.5 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| 0ms | Ring present as light printed outline (fallback state) |
| Hero sequence +500ms | Circles begin draw (1000ms) |
| +1000ms | Glyphs stagger in from tonight's sign, 60ms apart |
| +1400ms | Pointer line draws (300ms) |
| +1800ms | Tonight's sign fills gold; caption's sun line fades in |

#### 6.5 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Printed ring, gold sign | Printed ring, gold sign |
| Hover | Hovered sign's date range prints beneath (150ms) | n/a — tonight's range is printed by default |
| Focus | Not focusable; text equivalent follows in DOM | Same |
| Active | n/a | n/a |
| Scrolled-past | Printed | Printed |
| Disabled | Date unknown → no gilding, no sun line | Same |

#### 6.5 v2 — Breakpoint behaviour

≥1200px: 200px ring in the spread. 768–1199px: 160px. <768px: 120px,
centred above the date line; the hover-dates line is replaced by
tonight's range printed permanently.

#### 6.5 v2 — Edge cases & failure modes

Date on a sign cusp (e.g. 21 Nov): the printed ranges in §12 decide,
and the caption names the end date so the claim is checkable. Southern
hemisphere: the tropical signs are date conventions, not seasons — the
theme prints signs, and any seasonal copy must be localised by the
publisher, never auto-flipped. Session revisit: no re-draw. Slow
fonts: glyphs are SVG paths/text in Fraunces — if the font is late,
the draw waits for `document.fonts.ready` up to 300ms, then proceeds
(the ring must not draw in a fallback face).

#### 6.5 v2 — Accessibility spec

`role="img"` with `aria-label` “Zodiac ring. The sun in Scorpio, to
21 November.” The same sentence is the visible caption. Gold sign on
paper is 2.5:1 — acceptable only because the sign is also identified
by the pointer line and the caption text; colour is never the sole
carrier. Glyphs are decorative duplicates of the caption's claim.

#### 6.5 v2 — Tokens consumed

`--ink, --gold, --gold-deep, --ink-soft, --ease-rule, --dur-draw`,
`--ring-size` (200/160/120px).

### 6.6 Zodiac-man tap

- **What & why.** The zodiac man — the theme's recurring figure, signs
  mapped to the body — stands beside today's date, and when the date
  first enters the viewport his pointing hand taps once against
  tonight's sign. Once. The figure indicates today, the way he has
  indicated the governing sign in almanacs for five centuries, and then
  he holds still, because he is printed.
- **Structure.** An inline SVG figure (simplified woodcut-style body,
  twelve sign labels at their traditional body stations, one articulated
  arm group rotated from the shoulder). The arm's target angle is set
  from tonight's sign's station. The figure is ~180px tall on desktop,
  standing in the margin or beside the date line.
- **Motion spec.** On the date line's first entry: arm rotates −8° from
  rest to the pointing pose over 200ms `--ease-tap` (the theme's only
  overshoot), holds, and settles to the exact pointing angle by 320ms.
  Never repeats within a session; scroll-back does not re-tap. If the
  date line is in view at load, the tap waits 600ms after the hero
  sequence so it is seen, not spent during assembly.
- **States.** *Rest:* arm pointing at tonight's sign (the end state is
  the printed state). *Entering:* the single tap. *Scrolled-past:*
  pointing. *Hover:* the sign at the pointing hand prints its dates
  beneath the figure (150ms), sharing §6.5's data.
- **Content merge.** The figure stands beside the date he indicates;
  his hand, the sign and the date are one statement in three forms.
- **Failure fallback.** The figure is printed already pointing — the
  tap is an overlay on the correct final pose, so any failure leaves
  the truth standing. Date unknown: arm rests along the body, no sign
  indicated.
- **Reduced-motion variant.** No tap. The figure is printed pointing.
- **Performance budget & mobile variant.** One 320ms transform, once.
  Mobile: figure shrinks to 120px and moves above the date line; the
  tap is retained (it is small and once) unless reduced motion is set.

#### 6.6 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| Date line enters (78% line) or load +600ms after hero | Arm lifts −8° off the pointing pose (instant set, hidden by the figure's entry fade) |
| +0–200ms | Arm taps to the sign, `--ease-tap` overshoot |
| +200–320ms | Settles to exact pointing angle |
| Thereafter | Printed. No repeat this session |

#### 6.6 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Pointing at tonight's sign | Pointing, above date line |
| Hover | Sign's dates print beneath figure | n/a |
| Focus | Not focusable; equivalent text is the date line + §6.5 caption | Same |
| Active | n/a | n/a |
| Scrolled-past | Pointing | Pointing |
| Disabled | Date unknown → arm at rest along body | Same |

#### 6.6 v2 — Breakpoint behaviour

≥1200px: 180px, in the margin beside the date. 768–1199px: 150px,
inline at the date line's left. <768px: 120px, centred above the date
line; labels at body stations reduce to tonight's sign only (11px law,
§3 — the other eleven would fall below it).

#### 6.6 v2 — Edge cases & failure modes

Two dates on one page (today + an archive date): the man indicates
*today* only, beside the date line; archive spreads print him at rest
with no indication, captioned with the archive year. Sign station
angles are fixed in the build (twelve stated angles), never computed
from text length. If the figure's SVG fails to load (inline, so only
if markup is stripped), the date line and ring still carry the claim.

#### 6.6 v2 — Accessibility spec

Decorative-with-equivalent: `aria-hidden` on the figure, because every
fact he carries (today's sign, its dates) is printed in §6.5's caption
and the date line. The tap is not announced. Under reduced motion he
is static. No focus, no interaction.

#### 6.6 v2 — Tokens consumed

`--ink, --gold, --madder` (the pointing hand is printed madder — the
one place the figure uses red), `--ease-tap, --dur-tap`,
`--man-h` (180/150/120px).

### 6.7 Tide-line progress

- **What & why.** In the outer margin, a vertical tide-line rises
  scrubbed with reading depth: a ruled channel with printed tide ticks
  (the month's actual high/low marks, where the page carries tide data)
  and a water line whose surface wavers slightly as it rises. At a
  high-water tick the line pauses — the scroll must pass the tick's
  printed depth before the water resumes. Reading, measured in water.
- **Structure.** A fixed-position margin instrument: 2px channel rule
  full viewport height, an SVG water surface (a 24px-wide path with a
  2px-amplitude wave), tick marks positioned at fractions of the page
  corresponding to the tables' positions, each tick labelled with its
  real value (e.g. “HW 4.8m”) in data-label type rotated 0° — labels
  are never rotated; the margin is wide enough (§4).
- **Motion spec.** Water height = lerped page scroll progress mapped
  to the channel, `--ease-wax` linear, updated in the shared loop.
  Surface wave: the path's control point oscillates ±2px over 2400ms,
  paused when the tab is hidden or the line is off-screen. Pause at
  ticks: within ±0.6% of a tick's progress, the water's rise is damped
  to 25% speed, creating the felt pause without ever blocking scroll.
  At 100% the line rests at the top tick and the surface stills.
- **States.** *Rest (top):* water at the channel foot, first tick
  labelled. *Reading:* rising per above. *At footer:* full, still, the
  final tick's label inked in `--gold-deep`. *Scrolled-back:* falls
  exactly with progress — tides go out.
- **Content merge.** The ticks are the page's own tables' high waters,
  at the tables' own depths. The instrument measures this page, not a
  generic percentage wearing a costume.
- **Failure fallback.** No JS: the margin prints the ticks alone as a
  static index of the tables (still useful, still true). If the page
  carries no tide data, ticks are chapter marks instead (chapter name
  at each bound) — the line never invents a height.
- **Reduced-motion variant.** No water, no wave: tick labels ink from
  `--ink-soft` to `--ink` as their tables pass. Position is conveyed
  by the inked ticks, statically.
- **Performance budget & mobile variant.** One path attribute update
  per frame ≤0.3ms. Mobile <768px: the margin is abolished — the line
  becomes a 2px tide rule across the top of the viewport under the
  masthead, rising left→right, ticks as unlabelled notches (labels
  would crowd), wave off.

#### 6.7 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| Load | Channel and ticks print; water at foot |
| Scroll (continuous) | Water rises with lerped progress; wave oscillates 2400ms |
| Tick approach (±0.6%) | Rise damps to 25% — the pause at high water |
| Tick pass | Tick label inks to full `--ink` (200ms) |
| 100% | Surface stills; final tick inks `--gold-deep` |

#### 6.7 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Ticks printed, water at foot | Top rule at 0%, notches printed |
| Hover | Hovering a tick prints its table's title in the margin (150ms) | n/a |
| Focus | Not focusable; progress is also conveyed by the running head (§6.13) | Same |
| Active | n/a | n/a |
| Scrolled-past | Full, still | Rule complete |
| Disabled | No tide data → chapter-mark mode (above) | Chapter notches |

#### 6.7 v2 — Breakpoint behaviour

≥1200px: full margin instrument with labels. 768–1199px: 56px margin —
line and ticks survive, labels shorten to values only (“4.8m”).
<768px: top rule mode, no labels, no wave.

#### 6.7 v2 — Edge cases & failure modes

Very long page: tick positions are fractions of total height computed
after layout and recomputed on resize (debounced 200ms) and on
`document.fonts.ready`. Very short page (<150vh): the line is retired
— a tide needs room to rise; chapter ticks in the running head carry
progress instead. Scroll-back past a tick: its label stays inked
(it has been read; tides remember). Print: the instrument is removed
by the print stylesheet (§10).

#### 6.7 v2 — Accessibility spec

Progress is ambient and duplicated: the running head (§6.13) prints
the current chapter as text, so no information is exclusive to the
line. The instrument is `aria-hidden`. Tick labels are real text for
their index value in the no-JS fallback only; in the JS build they are
visual duplicates of the tables' own values. Contrast of labels:
`--ink-soft` 8.9:1, inked state 14.6:1.

#### 6.7 v2 — Tokens consumed

`--ink, --ink-soft, --gold-deep, --rule, --ease-wax`, `--tide-w`
(24px channel), `--wave-period: 2400ms`.

### 6.8 Real-data rolls

- **What & why.** Moon age, tide heights and planting-day counts roll
  — odometer digits, 800ms — to tonight's real values when their
  figures enter. The roll says: this number was computed for you,
  today; it is not the number that was here last month.
- **Structure.** Each figure is a set of digit columns (`0–9` strips in
  clipped 1em windows) generated by JS from the printed final value;
  the printed final value is the DOM default and the no-JS state. The
  value's source is one of exactly two: (a) computed — moon age and
  illumination from §6.1's formula; (b) counted — planting days counted
  from the planting table's marked rows present in the DOM, tide
  extremes read from the tide table's cells. The build states each
  figure's source in a `data-source` attribute and the caption names
  it in words (“14 planting days, counted from the table below”).
- **Motion spec.** On entry at the 78% line, once: each digit column
  translates to its final digit over 800ms `--ease-settle`, columns
  staggered 40ms right-to-left (units settle first — the count lands
  on its unit, as a mechanical counter does). Decimal points and units
  never roll. A figure already at its value (age 0.0 on a new-moon
  day) does not roll; it prints.
- **States.** *Rest:* true final value. *Entering:* the roll, once.
  *Scrolled-past:* final value. *Re-entry:* no re-roll.
- **Content merge.** The figures are the page's data, given a small
  ceremony at the moment they are first read.
- **Failure fallback.** JS off: printed values. Computation failure:
  the figure prints the fallback value from the build (dated in its
  caption, “at printing”) — a dated truth, never a blank and never a
  guess. Watchdog: any column not settled by 1200ms snaps to final.
- **Reduced-motion variant.** Values print. No roll, ever.
- **Performance budget & mobile variant.** ≤6 figures per page, ≤4
  columns each; transform-only. Mobile: identical, stagger shortens
  to 25ms.

#### 6.8 v2 — Choreography timeline

| Beat (from entry) | What happens |
|---|---|
| 0ms | Figure visible at a neutral start (columns at 0) only if JS armed it pre-entry |
| 0–800ms | Units column rolls to final digit |
| +40ms per column leftward | Tens, hundreds follow |
| +840ms | Full figure settled; caption's source line fades in (150ms) |
| Scroll-back / re-entry | Nothing. Settled is settled |

#### 6.8 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Final true value | Final true value |
| Hover | Source line underlines (the figure offers its provenance) | n/a |
| Focus | Figures are text; if inside a link, standard link focus (§11) | Same |
| Active | n/a | n/a |
| Scrolled-past | Final value | Final value |
| Disabled | Source unavailable → dated print value + “at printing” caption | Same |

#### 6.8 v2 — Breakpoint behaviour

Identical at all widths; figures never shrink below table-figure size
(15px) — a figure that cannot fit wraps its caption below it instead.

#### 6.8 v2 — Edge cases & failure modes

Midnight rollover while open: figures recompute with §6.1's 60s check;
a changed figure re-rolls once (600ms) — the day genuinely changed.
Counted figure whose table is paginated/client-fetched: the count is
taken after §6.12's fill completes; until then the figure prints “—”.
Negative or zero counts print without rolling. A figure whose computed
and printed (build-time) values disagree after rollover: computed
wins, caption updates its date.

#### 6.8 v2 — Accessibility spec

The rolling columns are `aria-hidden`; an adjacent visually-hidden
span carries the final value as plain text from first paint, so a
screen reader never hears a count mid-roll. Final values use tabular
figures. Contrast as §6.3. The roll is suppressed under reduced motion.

#### 6.8 v2 — Tokens consumed

`--ink, --ink-soft, --ease-settle, --dur-roll`, `--col-w: 0.62em`
(tabular digit width in Source Serif 4).


### 6.9 Moonlight temperature drift + harvest dust

- **What & why.** As the visitor reads down the month, the page's light
  warms and cools almost imperceptibly — ±3% warmth, tied to scroll
  depth — as if the light over the kitchen table were changing, and in
  the hero a few harvest-dust motes drift through that light. This is
  the theme's only atmosphere, and it is rationed to almost-nothing:
  if a visitor can *describe* the drift unprompted, it is too strong
  and §9 has been breached.
- **Structure.** A full-spread overlay gradient using `--moonlit`,
  composited above the ground and below the text's contrast threshold:
  implemented as a `background` blend on a spread-level `::before` with
  `pointer-events: none`, its warmth driven by a CSS variable
  `--warmth` (−1…+1) set from the shared loop. Dust: a single hero
  canvas, ≤14 seeded motes (deterministic seeds, same book every
  visit), each 1–2px, ≤30% opacity, drifting on 9–16s periods.
- **Motion spec.** Warmth = sin of lerped page progress × 2 full cycles
  across the page, mapped to a ±3% shift in the overlay's gold alpha
  (0.13–0.19) — scrubbed, `--ease-wax`, never looped on its own. Dust
  runs only while the hero is in view, pauses off-screen and when the
  tab hides. No dust outside the hero, ever.
- **States.** *Rest:* warmth at the top-of-page value. *Reading:*
  drifting per above. *Footer:* warmth returns to neutral — the book
  closes in the same light it opened.
- **Content merge.** The light falls on the spread being read; it is
  the moon's light (§6.1's moon is its source in the fiction) and the
  dust is the harvest's, in harvest months' hero woodcut air.
- **Failure fallback.** No canvas: the drift alone remains. No JS: a
  static, neutral overlay — i.e. nothing, which is the correct amount
  of nothing.
- **Reduced-motion variant.** Both off. The overlay is removed, not
  frozen mid-warmth.
- **Performance budget & mobile variant.** One CSS variable write per
  frame; canvas ≤14 particles, ≤0.6ms/frame. Mobile: dust off (small
  screens, small air), drift retained at ±2%.

#### 6.9 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| Hero entry | Dust fades in over 1200ms to ≤30% opacity |
| Scroll (continuous) | `--warmth` follows lerped progress, 2 cycles per page |
| Hero leaves view | Dust pauses within one frame; drift continues (it belongs to every spread) |
| Footer entry | Warmth eases back to 0 over the footer's first 30vh |

#### 6.9 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Neutral warmth, dust in hero only | Neutral, no dust |
| Hover | n/a | n/a |
| Focus | n/a — overlay never intercepts | n/a |
| Active | n/a | n/a |
| Scrolled-past | Drift continues; dust paused off-screen | Drift at ±2% |
| Disabled | Canvas unavailable → drift only; both off under reduced motion | Drift only / off |

#### 6.9 v2 — Breakpoint behaviour

≥1200px: drift ±3%, dust on. 768–1199px: drift ±3%, dust ≤10 motes.
<768px: drift ±2%, dust off.

#### 6.9 v2 — Edge cases & failure modes

Contrast guard: the overlay's maximum alpha is capped so body text
contrast never drops below 12:1 (from 14.6:1) at any warmth value —
verified in §10 by measuring at both extremes. Long pages: the 2-cycle
mapping is by progress fraction, not pixels, so length changes only
the drift's slowness. `save-data`: dust off. Low-power (<40fps loop):
drift steps in 0.5 increments instead of continuously — still
imperceptible, cheaper.

#### 6.9 v2 — Accessibility spec

Purely ambient, `aria-hidden`, no information carried. Removed under
reduced motion. The contrast cap above is the accessibility spec's
core: atmosphere may never tax reading.

#### 6.9 v2 — Tokens consumed

`--moonlit, --gold, --ease-wax`, `--warmth` (−1…+1), `--dust-n`
(14/10/0).

### 6.10 Thumb-mark hover

- **What & why.** Hovering a tide-table row prints a madder-red thumb
  mark in the margin beside it — a smudged thumbprint oval, as if a
  reader had marked the row they mean to use. It is how this book's
  readers have always saved their place.
- **Structure.** An SVG thumbprint (concentric arc paths, deliberately
  imperfect) in the table's margin column, one instance per table,
  repositioned to the hovered row. The smudge is a 2px horizontal blur
  on the mark's trailing edge, baked into the path — not a filter.
- **Motion spec.** On row hover (after 80ms dwell, so passing the
  pointer across the table does not print a row of thumbs): mark fades
  in 200ms `--ease-tap` with a 1px downward settle — the thumb pressing.
  On leave: fades out over 260ms, slower than it came, like ink drying
  off attention. Row ground warms 3% while marked.
- **States.** *Rest:* no mark. *Hover:* per above, one mark per table
  at a time. *Focus (keyboard):* a row reached by focus shows the same
  mark — marking is not a pointer privilege. *Scrolled-past:* marks do
  not persist; the book does not remember hover.
- **Content merge.** The mark sits beside the row it marks, in the
  margin the book provides for exactly this.
- **Failure fallback.** No hover (touch): a row tap marks it until
  another row is tapped — same mark, same meaning, and tapping a row
  never navigates (rows are data, not links, unless a cell contains a
  real link, which keeps its own behaviour).
- **Reduced-motion variant.** Mark appears/disappears instantly at the
  same dwell; the settle is removed.
- **Performance budget & mobile variant.** One reused SVG per table;
  opacity/transform only. Mobile: margin abolished — the mark prints
  at the row's left inside edge, 18px, and the table's first column
  gains 22px padding to house it.

#### 6.10 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| Pointer enters row | 80ms dwell begins; no visual change yet |
| +80ms | Thumb mark fades/settles in (200ms); row warms 3% |
| Pointer leaves | 260ms fade out; warmth releases with it |
| Rapid row-to-row move | Mark repositions without fading out (120ms move) — the thumb slides |

#### 6.10 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | No mark | No mark |
| Hover | Mark after 80ms dwell | n/a |
| Focus | Mark on focused row + madder outline (§6.3) | Mark on tap/focus |
| Active | Row tap (touch) toggles mark | Tap marks; second tap elsewhere moves it |
| Scrolled-past | No persistence | No persistence |
| Disabled | Rows that are “—” (missing data) take no mark — nothing to save | Same |

#### 6.10 v2 — Breakpoint behaviour

≥1200px: mark in outer margin, 22px. 768–1199px: mark in the table's
first (tick) column. <768px: inside left edge, 18px, per above.

#### 6.10 v2 — Edge cases & failure modes

Pointer crossing the table diagonally: dwell prevents a smear of
marks. Two tables in one viewport: one mark per table, independently.
A row taller than 44px (storm-note rows, §6.3): the mark centres on
the row's first line. Keyboard focus leaving the table: mark fades
with focus.

#### 6.10 v2 — Accessibility spec

The mark is decoration duplicating focus/hover state; `aria-hidden`.
The row's own content is untouched. Focus outline (2px `--madder-deep`,
6.9:1) is the accessible carrier; the mark is its paper echo. Touch
target: the row itself is 44px on touch (§6.3).

#### 6.10 v2 — Tokens consumed

`--madder, --madder-deep, --ease-tap, --dur-mark`, `--thumb-w`
(22/18px).

### 6.11 Footnote-unfold click

- **What & why.** Each prognostication may carry a folded footnote —
  most are factual (a tide's source, a planting note), exactly one per
  month is absurd (“Beware of geese near the 14th” gets its explanation).
  Clicking the prognostication's marker unfolds the note beneath it.
  The unfold is the reader turning to the small print the almanac
  always kept at the foot of the page.
- **Structure.** A `<button class="fn-mark">` (the marker is a real
  button: “Note on the 14th †”) controlling a region below the
  prognostication, `aria-expanded` wired. The note is set in caption
  italic if absurd, roman if factual (§3's code). Content is in the
  DOM from first paint, hidden by the folded state only when JS arms it.
- **Motion spec.** Unfold: height 0→auto over 350ms `--ease-settle`
  with the note's first line fading in at 120ms; a hairline rule above
  the note draws 200ms as it opens — the note is ruled off like a
  table. Fold (second click): 260ms, rule first. Only one note open
  per prognostication column; opening another folds the first (both
  animations run concurrently, neither waits).
- **States.** *Rest:* folded, marker shows † and the note's kind word
  (“Note”, or for the absurd one, still just “Note” — the joke is not
  labelled). *Open:* note printed, marker becomes “Close note”.
  *Scrolled-past:* open notes stay open (the reader left it open).
- **Content merge.** The note belongs to its prognostication and prints
  directly beneath it, in its column — not in a tooltip, modal or
  toast, none of which exist in a book.
- **Failure fallback.** No JS: all notes print open, beneath their
  prognostications, in reading order. The page is longer and entirely
  correct.
- **Reduced-motion variant.** Notes open/close instantly; the rule is
  printed.
- **Performance budget & mobile variant.** Height animation on one
  region at a time per column; layout cost is one reflow, accepted and
  capped (notes ≤6 lines; longer notes print open from the start and
  carry no fold). Mobile: identical, notes full column width.

#### 6.11 v2 — Choreography timeline

| Beat (from click) | What happens |
|---|---|
| 0ms | `aria-expanded` flips; region begins height animation |
| 0–200ms | Hairline rule draws above the note |
| 120ms | Note's first line fades in; remaining lines ride the height |
| 350ms | Fully open; focus stays on the button (never moved into the note) |
| Second click | Rule fades 100ms, height folds 260ms |

#### 6.11 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Folded, † marker | Folded, † marker, 44px target |
| Hover | Marker underlines in madder (150ms) | n/a |
| Focus | 2px `--madder-deep` outline on the button | Same |
| Active | Pressed: marker inks darker 120ms, then unfold | Same |
| Scrolled-past | Open state persists | Persists |
| Disabled | Notes over 6 lines have no fold — no button, printed open | Same |

#### 6.11 v2 — Breakpoint behaviour

Identical mechanics at all widths; at <768px the note's text is 14px
(caption law relaxes by 0.5px on the smallest leaves, §3) and the
marker button spans the prognostication's full line for touch.

#### 6.11 v2 — Edge cases & failure modes

Print: all notes print open (§10 print check). Deep link to a
prognostication (`#prog-14`): its note opens instantly on load if the
hash targets it. Multiple rapid clicks: the animation reverses from
its current height (WAAPI currentTime), never queues. A note whose
content was wrong (it happens, in almanacs): it is corrected by a
*second* note appended beneath, dated — the book never silently
rewrites its small print (§12's corrections voice).

#### 6.11 v2 — Accessibility spec

Real button, `aria-expanded`, `aria-controls`; region has
`role="region"` and an aria-label naming its prognostication (“Note on
the prognostication for the 14th”). Focus never moves on toggle.
Touch target ≥44px. Marker text (“Note on the 14th †”) is explicit —
the † alone would fail.

#### 6.11 v2 — Tokens consumed

`--ink, --ink-soft, --madder-deep, --rule-hair, --ease-settle,
--dur-unfold`.

### 6.12 Ruled-table skeleton + leaf-flip transition

- **What & why.** Two states of the book, one element each. Loading:
  a ruled but empty table — caption, column heads, hairlines, no
  figures — that fills row by row when its data (client-fetched tides,
  a month archive) arrives. Navigation: a stiff leaf flip with bend
  shading, 450ms, the same physics as §6.2 at reading speed.
- **Structure.** Skeleton: the real table markup with figure cells
  holding a ruled blank (a 40%-width hairline where the figure will
  sit), `aria-busy="true"` on the table. Transition: a full-viewport
  leaf layer (`--paper-deep` ground, bend gradient as §6.2) above the
  outgoing page, rotating −12° and off, revealing the incoming page
  already rendered beneath.
- **Motion spec.** Skeleton: minimum display 300ms (a faster fill is a
  flash, not a table); rows then fill per §6.3's stagger, but at 40ms
  (the data has arrived; the ceremony is shorter). Sheen: none — paper
  does not shimmer; a single 600ms warmth pass (§6.9's overlay at 50%
  strength) crosses the filling table once. Transition: leaf covers
  (200ms `--ease-leaf`), navigation swaps at full cover, leaf lifts
  away (250ms) with the bend gradient sweeping; total 450ms. Back/
  forward: the leaf comes from the opposite edge.
- **States.** *Skeleton rest:* ruled blanks, caption present (the
  reader knows which table is coming). *Filled:* §6.3's table.
  *Failure:* after 4s without data, the skeleton prints its footnote —
  “The figures for this month had not arrived at printing” — and, where
  a moon table can substitute, offers it as a real link. *Transition
  active:* outgoing page inert.
- **Content merge.** The skeleton is the table's own ruling; the
  transition leaf is the book's own leaf. Neither is a generic loader
  in costume.
- **Failure fallback.** No JS: no skeleton (server tables are simply
  present) and navigation is a plain page load. Transition disarms on
  slow connections (`save-data`, ≤3g effective type) and after any
  transition failure — the next navigation is instant rather than
  broken.
- **Reduced-motion variant.** Skeleton fills instantly when data
  lands; transitions become a 150ms crossfade of the paper ground.
- **Performance budget & mobile variant.** Skeleton is DOM, no canvas.
  Transition: one transform on one layer, 450ms, and it must never
  delay LCP — it arms only for in-site navigations after first paint.
  Mobile: leaf angle −8°, total 380ms.

#### 6.12 v2 — Choreography timeline

| Beat | Skeleton | Transition |
|---|---|---|
| 0ms | Ruled table prints, `aria-busy` set | Leaf begins cover (200ms) |
| Data lands / cover complete | Fill waits to 300ms minimum | Swap at full cover; incoming page live beneath |
| Fill | Rows at 40ms stagger; warmth pass once | Leaf lifts 250ms, bend sweeping |
| Done | `aria-busy` removed; “Table complete” announced politely | Focus to incoming h1; leaf removed from DOM |

#### 6.12 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Ruled blanks + caption | Same |
| Hover | n/a | n/a |
| Focus | Links inside a skeleton table are not present until filled | Same |
| Active | n/a | n/a |
| Scrolled-past | Filled table, §6.3 rules | Same |
| Disabled | 4s failure → footnote + substitute link (above) | Same |

#### 6.12 v2 — Breakpoint behaviour

Identical table behaviour at all widths (columns per §6.3);
transition angle/duration per §6.2's scaling: −12°/450ms desktop,
−10°/420ms tablet, −8°/380ms mobile.

#### 6.12 v2 — Edge cases & failure modes

Data arriving in parts (two tide stations): each table fills
independently; one table's failure never blocks another's fill.
Navigation during a fill: the fill is abandoned, the table prints
complete on return (data is cached by the fetch layer). Rapid double
navigation: the second cancels the first leaf mid-flight and snaps to
the newest target. A transition interrupted by tab hide: on return,
the leaf is gone and the target page is shown — never a stuck cover.

#### 6.12 v2 — Accessibility spec

Skeleton table carries `aria-busy` and a visually-hidden status
(“Loading the November tide table”); completion is announced once via
a polite live region. Transition moves focus to the destination's h1
and announces the page title. Reduced-motion and slow-connection
variants above are the accessible defaults, not exceptions.

#### 6.12 v2 — Tokens consumed

`--paper, --paper-deep, --paper-shade, --rule, --rule-hair, --ink-soft,
--ease-leaf, --ease-settle`, `--flip-dur` (450/420/380ms).


### 6.13 Month navigation + running head (page family: navigation)

- **What & why.** The book's furniture: a masthead carrying the
  almanac's name, the year, and the month index (twelve months as a
  ruled row, the current month inked, past months present, future
  months present but lighter — an almanac prints the whole year at
  once); and, once the visitor scrolls, a running head: the current
  chapter's name and the month, in data-label type, with the corner
  moon (§6.1) carried into it at small size.
- **Structure.** `<header>` with the name in Fraunces 560, a full rule,
  the month row as a real `<nav>` list of twelve links, and a second
  hairline. Running head: a sticky bar (56px) that appears after the
  masthead scrolls off, holding chapter name left, month + moon right.
- **Motion spec.** Masthead is static (a book's title page does not
  animate). Running head: fades/slides 8px over 220ms `--ease-settle`
  when it engages; chapter name crossfades 160ms at chapter bounds —
  the only text change in the theme that animates, and it is a
  crossfade, not a roll. Month links: hover inks a madder underline
  (draw 180ms); the current month's underline is printed, gold.
- **States.** *Rest:* masthead printed. *Scrolled:* running head with
  live chapter. *Hover/focus (month link):* madder underline; focus
  adds the 2px outline. *Current month:* gold underline + `aria-current`.
- **Content merge.** The month row is the site's actual archive
  navigation; the running head names the chapter being read. No
  decorative chrome exists.
- **Failure fallback.** No JS/sticky: masthead only, months still a
  working nav. The running head is an enhancement; its absence loses
  orientation, never content.
- **Reduced-motion variant.** Running head appears without slide;
  chapter changes swap instantly.
- **Performance budget & mobile variant.** Sticky + opacity only.
  Mobile: month row becomes a horizontally scrollable ruled strip
  (current month scrolled into view on load), running head keeps
  chapter name and drops the moon (the date line's moon, §6.1, is
  already on screen at the top).

#### 6.13 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| Load | Masthead printed; current month's gold underline present |
| Masthead leaves viewport | Running head engages (220ms) |
| Chapter bound crossed | Chapter name crossfades (160ms); §6.7 tick state agrees |
| Return to top | Running head releases; masthead resumes |

#### 6.13 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Printed masthead | Masthead + scrollable month strip |
| Hover | Month link: madder underline draws | n/a |
| Focus | Underline + 2px outline | Outline on strip links |
| Active | Link presses: ink deepens 120ms, then §6.12 flip | Same |
| Scrolled-past | Running head state | Running head, no moon |
| Disabled | A month with no published spread prints as text, not a link (“March — not yet printed”) | Same |

#### 6.13 v2 — Breakpoint behaviour

≥1200px: full masthead + 12-month row. 768–1199px: month row wraps to
two ruled lines of six. <768px: scrollable strip; running head 48px.

#### 6.13 v2 — Edge cases & failure modes

Year boundary (a December page linking January of the next annual):
the link is labelled with its year and the flip (§6.12) still applies.
Archive years: the masthead year changes, the month row lists that
year's months. A chapter name longer than the head: it truncates with
an ellipsis at 40 characters — the chapter's own head on the page is
never truncated.

#### 6.13 v2 — Accessibility spec

Nav landmarks labelled (“Months of the 2027 almanac”); `aria-current=
"page"` on the current month; running head is `aria-hidden` (it
duplicates the chapter heads in the text). Focus order: masthead nav
before content; the sticky head never enters focus order. Contrast:
month links 14.6:1, lighter future months use `--ink-soft` 8.9:1 —
“lighter” is weight, never a contrast cut below AA.

#### 6.13 v2 — Tokens consumed

`--paper, --ink, --ink-soft, --madder, --gold, --rule, --ease-settle`.

### 6.14 The month's opening spread (page family: hero)

- **What & why.** The hero is the month's opening spread, whole: left
  leaf a woodcut of the month's work (the harvest, the boats in, the
  first frost), right leaf the month name, the date line, tonight's
  key figures (§6.8), the zodiac ring (§6.5) and the corner moon
  (§6.1), with the zodiac man (§6.6) beside the date. It assembles in
  printed order and then, per §6.4, pins while the days scroll beneath.
- **Structure.** A two-leaf grid (7fr woodcut / 5fr instruments at
  ≥1200px). Woodcut: inline SVG or a duotone-treated image in a ruled
  frame with a printed caption (“The November woodcut: bringing in the
  mangolds”). Instruments column: month name (Display 1), date line,
  figures row, ring, and the first prognostication as a taster — set as
  body text, folded footnote and all (§6.11), because the hero should
  demonstrate the book's voice, not just its furniture.
- **Motion spec.** Assembly sequence, once: woodcut scales-in-frame
  (700ms `--ease-settle`, blur licensed per §5) at 0ms; month name and
  date line print (opacity, 300ms) at 200ms; figures roll (§6.8) at
  500ms; ring + moon draw (§6.5/§6.1) at 700–1700ms; zodiac tap
  (§6.6) at +600ms after assembly; dust (§6.9) fades in last. Total
  ceremony ≤2.3s, and every element's end state is its printed state.
- **States.** *Rest:* the complete spread. *Assembling:* per above.
  *Scrolled:* pins per §6.4. *Return visit (session):* printed
  complete, no assembly — the book is already open.
- **Content merge.** Every hero element is a working instrument or the
  month's actual first content. There is no hero-only decoration.
- **Failure fallback.** No JS: the complete printed spread. Any single
  instrument's failure leaves the others standing (§6.x fallbacks are
  independent). The 1200ms global watchdog forces all hero elements to
  printed state.
- **Reduced-motion variant.** Printed spread, true moon, no assembly,
  no pin, no dust.
- **Performance budget & mobile variant.** Hero assets ≤180KB (woodcut
  SVG preferred; a raster woodcut must be ≤120KB and duotone).
  Mobile: leaves stack — woodcut (cropped to its upper two-thirds,
  caption intact), then month, date, figures; ring and man per their
  mobile rules; assembly shortens to a single 400ms print fade.

#### 6.14 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| 0ms | Printed spread is the DOM default; JS arms assembly pre-states |
| 0–700ms | Woodcut scales-in-frame, sharpens |
| 200ms | Month name + date line print |
| 500ms | Key figures roll to tonight's values (§6.8) |
| 700–1700ms | Ring and moon draw (§6.5, §6.1) |
| +600ms after assembly | Zodiac man taps (§6.6); dust fades in (§6.9) |
| Scroll | Pin engages (§6.4); days begin beneath |

#### 6.14 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Complete spread | Stacked complete spread |
| Hover | Instruments per their own specs | n/a |
| Focus | First focusable element is the taster prognostication's note button (§6.11) — the hero offers reading before navigation repeats | Same |
| Active | Per element | Per element |
| Scrolled-past | Released pin; spread gone; running head carries month | Scrolled away |
| Disabled | Any instrument disabled per its own §6.x rule; spread never blocks | Same |

#### 6.14 v2 — Breakpoint behaviour

≥1200px: 7/5 two-leaf grid, pin on. 768–1199px: 6/6 grid, pin 80vh.
<768px: stacked, no pin, assembly shortened (above).

#### 6.14 v2 — Edge cases & failure modes

A month with no woodcut commissioned: the left leaf becomes the
month's full tide/moon table (a working leaf, not an empty frame) —
the spread is asymmetric in the other direction and the layout grid
holds. A very long month name (September is the test): Display 1
steps down to 56px before it may wrap. Hero figures whose data is
unavailable print dated (§6.8), never blank.

#### 6.14 v2 — Accessibility spec

Reading order: month name (h1), date line, figures (as text), woodcut
with its caption as `figcaption` / alt describing the scene, ring per
§6.5, taster prognostication. The assembly animation never reorders
DOM. Landmarks and heading structure are the printed book's.

#### 6.14 v2 — Tokens consumed

All §6.1/6.5/6.6/6.8/6.9 tokens plus `--paper, --ink, --rule,
--ease-settle`, `--hero-woodcut-max: 120KB`.

### 6.15 Prognostication & day cards (page family: cards)

- **What & why.** Where the site lists — a month index, a run of days,
  a set of prognostications — each entry is a card cut from the
  almanac's own paper: a ruled frame, the date as its head, the entry's
  first line as its body, and a woodcut thumbnail where the entry has
  one. Cards are leaves in miniature, not tiles on a background.
- **Structure.** `article.card` in a ruled frame (1.5px `--rule`, no
  radius — paper is cut square), date head in data-label type, body in
  body serif, thumbnail (if any) in its own inner ruled frame at 4:3.
  A card is a link only if the whole entry exists beyond it; otherwise
  it is printed matter and carries §6.11's note button where relevant.
- **Motion spec.** Entry: cards impress with their section — opacity +
  4px rise, 380ms `--ease-settle`, 70ms stagger, capped at 6 animating.
  Woodcut thumbnails scale-in-frame per §5. Hover: the plate tilts
  like a leaf lifted — rotateX 2° toward the reader, 240ms, with the
  frame's shadow lengthening 2px; the card itself does not lift (paper
  lies flat; only a leaf's edge rises).
- **States.** *Rest:* printed card. *Hover:* plate tilt + date head
  inks madder-deep. *Focus:* 2px outline + the same tilt (focus is a
  reader's hand too). *Scrolled-past:* printed. *Out of season:* a
  past month's card prints on `--paper-deep` — the turned leaf — with
  its figures struck through only if superseded (a correction, §12),
  never merely for being past.
- **Content merge.** The card's date, line and picture are the entry's
  own. A card with its animation removed is the entry's index card,
  complete.
- **Failure fallback.** Static ruled grid. Thumbnails failing to load
  print the frame with the entry's first initial as a woodcut-style
  drop cap — a filled frame, never a broken image icon.
- **Reduced-motion variant.** Cards printed; tilt off; hover/focus
  keep the ink change only.
- **Performance budget & mobile variant.** ≤6 concurrent entry
  animations; thumbnails `content-visibility: auto` below the fold.
  Mobile: one column, tilt off, thumbnails 3:2 (the crop tightens on
  the woodcut's subject, stated per image in markup).

#### 6.15 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| Section entry | Cards begin impress, 70ms stagger, ≤6 |
| Each card +380ms | Printed; thumbnail scale-in-frame completes with it |
| Hover/focus | Plate tilts 240ms; date inks |
| Leave/blur | Tilt releases 260ms; ink stays while focus remains |

#### 6.15 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Printed card | Printed card |
| Hover | Plate tilt 2°, date madder-deep | n/a |
| Focus | Outline + tilt + ink | Outline + ink (no tilt) |
| Active | Pressed: frame shadow shortens 120ms (the leaf pressed flat) | Same |
| Scrolled-past | Printed | Printed |
| Disabled | Entry not yet published → card prints date + “Not yet printed”, no link | Same |

#### 6.15 v2 — Breakpoint behaviour

≥1200px: 3 per row. 768–1199px: 2 per row. <768px: 1 per row,
thumbnails 3:2, stagger removed (cards impress with their section).

#### 6.15 v2 — Edge cases & failure modes

An entry with a very long first line: the card prints two lines and
ellipsises the third — the full line lives on the entry's page, and
the card says so with a printed “continued” in caption italic. A run
of 31 day cards (a whole month): the grid is the month; entry
animation caps mean most cards are simply present. Mixed media (some
cards woodcut, some not): frames keep one height; the pictureless
card's frame holds its drop-cap initial at Display 2 size.

#### 6.15 v2 — Accessibility spec

Link cards: the link wraps the date head only, with an aria-label
naming the full entry (“14 November — tides, planting, and the
prognostication”) so a list of links is navigable by ear. Tilt is
`transform` on the image only; text never moves. Contrast per §2.

#### 6.15 v2 — Tokens consumed

`--paper, --paper-deep, --ink, --madder-deep, --rule, --ease-settle`.

### 6.16 The annual order form (page family: forms / conversion)

- **What & why.** The almanac's one transaction: ordering next year's
  annual (or subscribing to the monthly sheets). In the printed book
  this was the order leaf bound at the back, filled in by hand and
  posted. The form keeps that shape: one leaf, ruled lines for fields,
  the price printed beside each choice, and a confirmation that reads
  as an entry in the publisher's ledger.
- **Structure.** Single column at 58ch inside a ruled frame. Fields are
  leader lines (label above in data-label type, input on a hairline,
  entry in Source Serif 4 17.5px). Edition choices are stamp-choice
  radios: printed squares the chosen one fills with a madder stamp
  (“POST” mark). The submit is a full-width ruled plate labelled with
  the plain verb: “Order the 2027 Almanack”. Price arithmetic is
  printed and updates as text (never as a rolling counter — money in
  this book is stated, not performed).
- **Motion spec.** Focus: the field's hairline inks hairline→full
  `--ink` 200ms and its label takes the data-label's full weight.
  Error: the line turns `--madder-deep` and a correction note prints
  in the margin in the editor's voice (§12), drawn in 250ms — errors
  are errata, and errata are printed, dated and kept. Submit: the
  plate presses (ink +8%, 120ms), the whole leaf takes a slight
  impression (shadow deepens 300ms) while sending. Success: the leaf
  is replaced by the ledger entry — order number in tabular figures,
  what was ordered, when it will be posted (“Posted in the first week
  of December, with the winter sheets”), in body serif.
- **States.** *Rest:* hairlines light, labels soft. *Focus:* per
  above. *Filled:* line stays at 60% ink. *Error:* madder line +
  margin note, persistent until corrected (printed errata do not time
  out). *Submitting:* leaf impressed, inputs disabled. *Success:*
  ledger entry, permanent for the session.
- **Content merge.** The form is the book's own order leaf; its
  confirmation is the publisher's ledger line. The transaction's paper
  trail is styled as the paper itself.
- **Failure fallback.** A plain HTML form with native validation
  printing the same notes as text; every enhancement is CSS/JS over
  it. No-JS keeps the transaction entire.
- **Reduced-motion variant.** Focus/error states apply instantly;
  submit shows a static “Entering it in the ledger…” line.
- **Performance budget & mobile variant.** No loops; transitions on
  focus/error only. Mobile: leaf full-bleed (frame becomes top/bottom
  rules), inputs 17.5px (also prevents iOS zoom), margin notes move
  beneath their fields (a phone leaf has no margin).

#### 6.16 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| Field focus | Hairline inks 200ms; label weights up |
| Edition stamp-choice | Stamp fills 180ms `--ease-tap` (the one tap outside §6.6 — a hand stamping) |
| Submit click | Plate presses 120ms; leaf impression deepens 300ms |
| Response | Success: leaf content crossfades 200ms to the ledger entry; order number prints (no roll) |
| Error response | Offending lines turn madder; notes draw in 250ms; focus moves to the first error's field |

#### 6.16 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Light hairlines | Light hairlines, 44px fields |
| Hover | Field's label inks 150ms | n/a |
| Focus | Hairline full ink; label full weight | Same |
| Active | Submit press per timeline | Same |
| Scrolled-past | n/a — a form is used where it stands | n/a |
| Disabled | An edition sold out prints struck, labelled “The printing is full”, radio disabled with the reason as text | Same |

#### 6.16 v2 — Breakpoint behaviour

≥1200px: 58ch leaf, margin notes in a real margin. 768–1199px: 52ch,
notes beneath fields. <768px: full-bleed leaf, notes beneath, stamp
radios at 44px.

#### 6.16 v2 — Edge cases & failure modes

A price that changes between print and order (the annual's price
rose): the form prints the current price with a dated erratum note
(§12) — the book corrects itself openly. Double submit: the plate
disables after first press; a second order is a new leaf. Session
expiry mid-form: entries persist in the DOM; the error note says what
happened in the editor's voice and nothing is lost. Zero editions
available: the form is replaced by the waiting-list leaf (one field:
an address, one promise, dated).

#### 6.16 v2 — Accessibility spec

Native inputs with visible labels (never placeholder-only); errors
linked by `aria-describedby` and announced; focus order follows the
leaf top→bottom; the ledger confirmation is a heading + text, focused
on arrival. Stamp radios are real radios with 44px targets. Contrast:
labels `--ink-soft` 8.9:1 minimum, errors `--madder-deep` 6.9:1 plus
the line colour change (never colour alone — the note's text states
the error).

#### 6.16 v2 — Tokens consumed

`--paper, --ink, --ink-soft, --madder, --madder-deep, --rule,
--rule-hair, --ease-settle, --ease-tap`.

### 6.17 Colophon footer (page family: footer)

- **What & why.** The footer is the almanac's colophon and closing
  leaf: what the book was set in, who printed it, the next new moon's
  date (computed, §6.1's formula — the book always ends by pointing at
  the next month), the publisher's legal line, and a fleuron that
  draws itself as the footer enters. The last page tells the truth
  about the book and the date of the next one.
- **Structure.** Centred column at 62ch: fleuron SVG; colophon lines
  in caption roman (“Set in Fraunces & Source Serif 4 · Printed on
  the reader's own screen, which weighs nothing and keeps no harvest”);
  the next-moon line in body serif (“The next new moon falls on
  20 December, at 04:14 — the December spread opens with it” — time
  computed to the visitor's zone, or date-only where the build cannot
  state the time honestly); legal line and three text links with
  madder-underline hover (§6.13's treatment).
- **Motion spec.** The footer leaf impresses with its section (§6.15's
  entry). The fleuron draws 600ms `--ease-rule` as it enters. The
  next-moon line does not animate. Nothing loops; the end of the book
  is the stillest part of it.
- **States.** *Rest:* printed colophon. *Hover (links):* madder
  underline draws. *Scrolled-past:* n/a — it is the end.
- **Content merge.** The colophon is content: type credits, the
  computed next moon, the legal line. Its one ornament is the book's
  own printer's flower.
- **Failure fallback.** Static centred text; fleuron printed. If the
  next-moon computation fails, the line prints the date from the build
  with “at printing” — dated truth, per the law.
- **Reduced-motion variant.** Fleuron printed; footer pre-impressed.
- **Performance budget & mobile variant.** One 600ms draw, once.
  Mobile: unchanged column (it was always narrow); next-moon line
  wraps to two lines before it may shrink.

#### 6.17 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| Footer entry (78% line) | Leaf impresses 380ms with its section |
| +100ms | Fleuron begins draw (600ms) |
| +700ms | Colophon complete; nothing else moves, ever |

#### 6.17 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Printed colophon | Printed colophon |
| Hover | Links: madder underline draws 180ms | n/a |
| Focus | Underline + 2px outline | Outline |
| Active | Link press inks 120ms, then §6.12 flip if in-site | Same |
| Scrolled-past | n/a | n/a |
| Disabled | Next-moon time unstateable → date-only line (above) | Same |

#### 6.17 v2 — Breakpoint behaviour

Identical at all widths except line wrapping (above); fleuron 28px
at every size — a printer's flower does not scale with screens.

#### 6.17 v2 — Edge cases & failure modes

December's footer: the next new moon may fall in the *next annual* —
the line says so and links the new annual's order leaf (§6.16), which
is the book's oldest joke and its business model in one sentence.
Timezone edge: a next-moon time within 2 hours of midnight prints
date-only, because the honest day differs by zone and the book does
not pretend otherwise.

#### 6.17 v2 — Accessibility spec

Footer landmark; the next-moon line is plain text, computed values
identical in text and any visual treatment. Links are plain links
with the theme's standard focus. Contrast per §2.

#### 6.17 v2 — Tokens consumed

`--paper, --ink, --ink-soft, --madder, --rule, --ease-rule,
--ease-settle`.

### 6.18 The missing leaf (page family: 404 / empty states)

- **What & why.** A missing page in an almanac is a leaf that was never
  bound, or a month not yet printed. The 404 is a ruled blank leaf:
  the month grid with one leaf shown blank, the statement in deadpan
  body serif (“This leaf was not bound into this copy”), and the way
  back printed as the two nearest real leaves (this month's spread,
  the month index). Empty states across the site use the same grammar:
  a table with no rows yet prints its ruling and a dated note.
- **Structure.** The blank leaf: a `--paper-deep` leaf outline at
  spread size (or stacked, mobile), containing the statement, the
  computed tonight moon small in its corner (the book still knows
  tonight, even lost), and two real links set as a small table of
  “Leaves that are bound in”. Search-with-no-results and
  not-yet-printed months reuse the leaf at section size.
- **Motion spec.** The leaf impresses on entry per §6.15. Its corner
  moon draws per §6.1's timeline (shortened: 600ms). Nothing else
  moves — a blank leaf is quiet.
- **States.** *Rest:* printed blank leaf with its statement and links.
  *Hover/focus:* links per §6.17.
- **Content merge.** The error is expressed in the book's own
  material: an unbound leaf, not a mascot with a spanner.
- **Failure fallback.** The leaf is static HTML; it cannot fail to
  render its statement and links.
- **Reduced-motion variant.** Moon printed; no draw.
- **Performance budget & mobile variant.** Negligible. Mobile: leaf
  stacks, moon at the date line per §6.1 mobile.

#### 6.18 v2 — Choreography timeline

| Beat | What happens |
|---|---|
| Load/entry | Leaf impresses 380ms |
| +200ms | Corner moon draws (600ms) or prints (reduced motion) |
| Thereafter | Still |

#### 6.18 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Blank leaf, statement, two links | Stacked leaf |
| Hover | Link underlines per §6.17 | n/a |
| Focus | Standard outline; first link is the month spread | Same |
| Active | Link press + §6.12 flip | Same |
| Scrolled-past | n/a (a 404 is the page) | n/a |
| Disabled | A not-yet-printed month (disabled state reuse) prints its expected date: “March will be printed on 1 February” | Same |

#### 6.18 v2 — Breakpoint behaviour

≥1200px: spread-size leaf. 768–1199px: single-leaf size. <768px:
stacked, statement first, moon in the date row.

#### 6.18 v2 — Edge cases & failure modes

A URL for a real but unpublished month must use the disabled variant
(expected date printed), not the 404 leaf — the book distinguishes
“not yet” from “never was”, and so does its status code (the build
serves a real 404 only for the never-was). A search with results in
another month links that month's leaf rather than printing blank.

#### 6.18 v2 — Accessibility spec

The statement is the page's h1. Links are descriptive (“This month's
spread”, “The index of months”). The moon per §6.1. Status semantics
are the server's, not the theme's, concern — the theme only insists
the two cases are not conflated visually.

#### 6.18 v2 — Tokens consumed

`--paper, --paper-deep, --ink, --ink-soft, --rule, --ease-settle,
--ease-rule`.

---

## 7. Page application map

- **Home (this year's annual).** Hero = the *current* month's opening
  spread (§6.14) — the home page is never a cover with a slogan; it is
  the book open at today. Below: the remaining months as §6.15 cards
  in year order, past months on `--paper-deep`, the order leaf (§6.16)
  as the closing spread before the colophon.
- **Month page.** §6.14 spread, §6.4 pin, daily tables (§6.3),
  prognostications with §6.11 notes, planting table, colophon. The
  moon scrubs +6 days across the page (§6.1).
- **Listing (month index / archive years).** §6.15 cards ruled as a
  table of contents; years as chapters with §6.2 leaf turns between
  them; no pin.
- **Detail (a day, a tide station, a single prognostication).** The
  entry prints as one leaf: date line, its table or text, its notes
  open (detail pages do not fold their own subject's note), zodiac man
  only if the entry is *today*.
- **About (the annual itself).** The book's history told in chapters
  with leaf turns; the colophon (§6.17) promoted to a full spread;
  past covers as §6.15 cards with drop-cap fallbacks.
- **Order / subscribe.** §6.16's leaf, alone on its page with the
  masthead; no cross-sell intrudes on the order leaf — the printed
  book never interrupted its own order form.
- **404 / empty.** §6.18's missing leaf.

---

## 8. Worked examples

### 8.1 The hero — a seed merchant's November spread

**Setting.** “Harrowgate Seeds” opens its site at November's spread.
Left leaf: an SVG woodcut of mangolds being lifted, caption printed.
Right leaf: “November” (Display 1), date line “Tuesday 11 November”,
figures row — Moon age 11.3 days (computed), High water 4.8m at 06:12
(from the harbour table below), 14 planting days (counted from the
planting table's marked rows). Ring with the sun in Scorpio; the man
beside the date, hand on Scorpio's station (the loins, as tradition
dictates and the caption does not discuss).

**Scroll timeline.** 0ms printed DOM → woodcut scales in (700ms) →
name and date print (200ms) → figures roll (500–1300ms, §6.8) → ring
and moon draw (700–1700ms) → tap at assembly +600ms → dust fades in →
visitor scrolls: pin engages (§6.4), November's daily tables rise
beneath the spread, the moon scrubs from 11.3 toward 13.3 days across
the pin, its caption gaining “by month's end” only after the pin
releases and the month's own pages take the scrub to +6.

**What the visitor feels.** The book opened at the right month, by
itself, and the month is passing in their hand.

### 8.2 Mid-page — the tide table and the marked row

**Setting.** Halfway down November: “Tides at Harboursmouth —
November”, a 60-row table (two tides a day), preceded by the
prognostication for the 14th: “A fair wind for those who mend nets.
Beware of geese near the 14th.” with its folded note.

**Scroll timeline.** Table enters at the 78% line: head rule draws
(600ms), 14 rows fill at 60ms stagger, the remaining 46 are simply
there; high-water rows carry their gold ticks. The visitor hovers the
06:12 row for Saturday — after 80ms the thumb mark prints beside it
(§6.10). They click the 14th's note marker: the rule draws, the note
unfolds (350ms) in italic: the geese explanation, which blames a
specific goose. In the margin, the tide-line (§6.7) has risen past the
06:12 tick and paused there as they read.

**What the visitor feels.** A table they can use, a mark where their
thumb is, and one joke, told straight.

### 8.3 Conversion — ordering the 2027 annual

**Setting.** The closing spread: §6.16's order leaf. Editions: Paper
(£9), Cloth (£16, struck through — “The printing is full”), and the
Monthly Sheets by post (£24). The Paper stamp is chosen; the total
prints beneath in tabular figures as a statement, not a counter.

**Interaction timeline.** Focus enters the name field: hairline inks
(200ms). The address's second line is left empty and the form is
submitted: that line turns madder, and the margin prints, in the
editor's voice, “The second line of the address is wanting. Even the
geese are directed better.” (the error is factual, the voice is the
book's). The visitor corrects it; the line returns to ink at 60% —
the erratum is not erased from the leaf's behaviour, it is resolved.
Second submit: plate presses, leaf impresses, and the ledger entry
replaces it: “No. 0417 — The 2027 Almanack, Paper. Posted in the first
week of December, with the winter sheets.”

**What the visitor feels.** They filled in a form in a book, and the
book wrote them into its ledger.

---

## 9. Anti-slop — what makes THIS theme look cheap

1. **A decorative moon.** A crescent chosen from clip-art, at a phase
   tonight does not have. *Cure:* §6.1's computation or the dated
   static fallback. There is no third option.
2. **Invented tides.** Plausible-looking heights generated to fill a
   table. *Cure:* publisher data or the moon-table substitution with
   its printed footnote (§6.3). One fabricated height fails §10.
3. **Sepia everything.** A brown filter over a modern layout calling
   itself an almanac. *Cure:* the palette is four inks on paper, the
   layout is spreads and ruled tables — the theme is a structure, not
   a colour grade.
4. **Page-curl theatrics.** Leaves rotating −90°, curling corners,
   drop shadows like a lifted sticker. *Cure:* −18° maximum, bend
   shading, stiffness (§6.2). Paper in this book is stiff.
5. **Wacky prognostications.** Every line a joke, exclamation marks,
   “zany” weather lore. *Cure:* one absurd note per month, deadpan,
   italic (§12). The other prognostications are straight — that is
   what makes the one land.
6. **Gold confetti.** Gold buttons, gold badges, gold dividers.
   *Cure:* gold is 4% and belongs to the moon, the ring and the
   high-water tick (§2 discipline).
7. **Counters counting nothing.** Animated numbers whose targets were
   typed by the designer. *Cure:* computed or DOM-counted, captioned
   with their source (§6.8).
8. **A zodiac man as clip-art mascot.** Enlarged, waving, selling.
   *Cure:* he stands beside the date at 180px, taps once, and holds
   still (§6.6). He is a diagram, not a character.
9. **Tables as cards.** Tide data broken into floating tiles with
   shadows. *Cure:* real tables, ruled, dense (§6.3). The card form
   (§6.15) is for index entries, never for data.
10. **Atmosphere you can see.** A visible warmth filter, drifting
    dust everywhere, “ambience”. *Cure:* §6.9's cap — if it can be
    described unprompted, it is cut in half.
11. **Rotated text for charm.** Vertical labels, angled captions.
    *Cure:* nothing textual rotates except the ring's glyphs, which
    are a diagram (§6.5). Tide labels stand upright (§6.7).
12. **The joke labelled.** “(Yes, really!)” after the geese.
    *Cure:* §12's voice law — the book never laughs at its own joke.

---

## 10. Quality gate

**Blocking — all must pass.**

1. **Moon truth test:** on three stated dates (a new moon, a full
   moon, a quarter — dates chosen by the reviewer), the corner moon's
   computed age is within 0.5 day of the ephemeris value and the
   caption's phase name matches the age's division.
2. **Data provenance audit:** every figure on the page traces to
   §6.1's formula, a DOM count, or a publisher-supplied table whose
   source footnote prints on the page. One untraceable figure fails.
3. **JS-off test:** every page complete and readable, tables printed,
   notes open, moon shown as the dated static fallback.
4. **Fallback test:** with IO/animation triggers broken, the 1200ms
   watchdog leaves no element in a pre-state on any page.
5. **Reduced-motion test:** no scrub, turn, roll, draw or drift;
   the moon is at tonight's phase; all information present.
6. **Contrast at drift extremes:** body text ≥12:1 at both §6.9
   warmth extremes; all text pairings meet §2's stated ratios.
7. **Pin discipline:** at most one pin (§6.4), disabled <768px,
   <600px height, and under reduced motion.
8. **Cursor & cover audit:** system cursor unchanged; no animated
   layer overlaps text at five scroll depths on month and detail pages.

**Standard — at least 10 of 12.**

9. Assembly ceremony ≤2.3s on the hero; no element animates twice in
   a session.
10. Table entry ≤1.2s for a 62-row table (14-row cap honoured).
11. One shared rAF loop; no frame over 20ms attributable to theme
    code during a full-page scroll on a mid-range Android device.
12. Scrubbed values (moon, tide-line) reverse exactly on scroll-back.
13. The absurd note count is exactly one per month page; it is
    italic, unlabelled, and its prognostication is otherwise straight.
14. Madder ≤8% and gold ≤6% of pixels on a full-page screenshot at rest.
15. Print stylesheet: instruments, dust, drift and transitions are
    removed; tables print complete with their source footnotes; the
    spread prints as a clean sheet.
16. Zodiac ranges printed in §12 match the gilded sign on three
    reviewer-chosen dates, including one cusp date.
17. Counters land on their computed/counted values, tabular, once,
    upward in reading order of their digits' settling (units first).
18. The order form works fully without JS, keeps inputs ≥16px on
    mobile effective size, and its success prints a ledger entry with
    a real order reference from the system (never a styled “#0000”).
19. Tide-line ticks correspond to the page's tables (positions and
    values) on a spot check of three ticks.
20. The five-second test: a first-time viewer describes the page as
    *an almanac open at this month* — not “vintage”, not “rustic”,
    not “a farm theme”.

**Minimum bar, in one line:** a build whose moon is right and whose
numbers can all be traced has earned the right to be judged on charm;
anything less is a harvest costume, and it goes back to the printer.

---

## 11. Component inventory

Every component a real site in this theme needs, with its treatment.
Components the theme refuses are listed with their replacement —
a builder must not reintroduce them.

| Component | Almanack treatment |
|---|---|
| Primary button | The order plate (§6.16): full-width ruled block, plain verb label. One per leaf. |
| Secondary button | A ruled outline block, label in body serif; never filled. |
| Text link | Body-serif link, madder underline drawing on hover (§6.13); visited links ink `--ink-soft` (the leaf has been turned). |
| Inputs | Leader-line fields (§6.16). No boxes. |
| Selects | A printed list that opens as a ruled table of options (one column, hairlines); the chosen option gains a thumb mark. |
| Checkboxes / radios | Stamp choices (§6.16): printed squares, madder stamp fill. Checkboxes are square — paper has no round corners. |
| Tables | §6.3, the theme's core component; see its spec. |
| Badges | Refused. A fact worth marking is a tick in the table or a thumb mark in the margin. |
| Alerts | Errata slips: a ruled strip above the content it corrects, dated, in the editor's voice (§12); never auto-dismissing — print does not disappear. |
| Pagination | Month order: “October” / “December” as ruled links with the leaf flip (§6.12); numbered pagination is refused (a book's index is §6.13's month row). |
| Modal | Refused. Anything important enough to interrupt is printed as its own leaf (a detail page). |
| Toast | Refused. Confirmations are ledger entries (§6.16) or errata slips. |
| Tabs | Refused as tabs. Parallel tables (two harbours) print as two tables under one chapter head, in sequence — the reader turns, not switches. |
| Accordion | The footnote fold (§6.11) is the theme's only disclosure, and it belongs to prognostications. Generic accordions are refused. |
| Search | A “finding leaf”: one leader-line field; results print as a §6.15 card index with the searched term's occurrences thumb-marked. |
| Breadcrumbs | The running head (§6.13) plus the date line. No breadcrumb trail exists in a book. |
| Progress | Moon + tide-line (§6.1, §6.7). No bar, no spinner, no percentage — except a table's own figures. |
| Cards | §6.15 index leaves. |
| Tooltip | Refused. A fact is printed beside its subject (ring dates §6.5, tick titles §6.7) or not at all. |
| Divider | A full rule, or the fleuron (§6.17) at a book's end. No gradient hairlines. |
| Image frame | Ruled frame, caption printed beneath, always (§6.14/§6.15). |
| Date display | The date line (§3): weekday, day, month — the almanac's order. Machine formats (2027-11-11) appear only in data attributes. |
| Price display | Tabular figures, stated once, with its date if it has changed (§6.16's erratum rule). |
| 404 / empty | §6.18's missing leaf. |

---

## 12. Content & copywriting voice

**The voice is the editor's:** thirty years on the book, dry, exact,
kind underneath. Two registers exist — the *printed voice* (tables,
prognostications, statements: factual, terse, no adjectives that
cannot be checked) and the *editor's voice* (footnotes, errors,
corrections: first person plural “we”, dry, occasionally — once a
month — funny).

**Headline style.** A headline names its thing and its time: “Tides at
Harboursmouth — November”, “Planting in the Last Quarter”. Never a
benefit claim, never a question, never a pun in a headline — puns, on
the one occasion they occur, occur in footnotes.

**Label style.** Data labels are nouns with their units or places:
“Moon age”, “High water”, “Planting days (from the table)”. A label
that could sit on any website (“Learn more”, “Explore”) is rewritten
until it could only sit in this book (“The December spread”, “Order
the 2027 Almanack”).

**Prognostication voice.** Straight, specific, dated. ✓ “A fair wind
for those who mend nets. Frost on low ground after the 18th.”
✓ “Beware of geese near the 14th.” (the month's one absurdity, set
exactly as flat as the frost.) ✗ “Watch out, goose chaos incoming!!”
✗ “Mercury is in retrograde, besties.” The form is three centuries
old; the site does not improve it by winking.

**Error voice (editor's).** Factual first, dry second, never
apologetic beyond one clause. ✓ “The second line of the address is
wanting.” ✓ “We printed 4.8 where the harbourmaster's table says 4.6.
The table below is corrected; the error was ours.” (errata are dated
and kept, §6.11/§6.16.) ✗ “Oops! Something went wrong.” ✗ “Invalid
input.”

**Empty-state voice.** ✓ “March will be printed on 1 February.”
✓ “No days are marked for planting in the dark of this moon. The table
says why.” ✗ “Nothing here yet 👀”.

**Success voice.** A ledger line, past tense, with its reference and
its date (§8.3). ✓ “No. 0417 — entered. Posted in the first week of
December.” ✗ “Awesome! You're in!”

**Banned words.** “vibes”, “zany”, “wacky”, “rustic charm” (as copy),
“oops”, “supercharge”, “unlock”, any exclamation mark in a
prognostication, and the word “content” anywhere a reader can see it.

**Fixed strings (verbatim, do not paraphrase).** The moon caption
form: “Moon age {n} days · {Phase name}”. The table source form:
“Figures from {source}, {year}.” The erratum form: “For ‘{wrong}’
read: {right}.” The 404 statement: “This leaf was not bound into
this copy.”

**Zodiac date ranges (the §6.5 computation, printed for audit).**
Aries 21 Mar–19 Apr · Taurus 20 Apr–20 May · Gemini 21 May–20 Jun ·
Cancer 21 Jun–22 Jul · Leo 23 Jul–22 Aug · Virgo 23 Aug–22 Sep ·
Libra 23 Sep–22 Oct · Scorpio 23 Oct–21 Nov · Sagittarius 22 Nov–21 Dec ·
Capricorn 22 Dec–19 Jan · Aquarius 20 Jan–18 Feb · Pisces 19 Feb–20 Mar.
Cusp dates belong to the *later* sign from 12:00 local; before 12:00,
the earlier — the caption's “to {date}” form keeps the claim checkable
without pretending to the hour of the sun's ingress, which the book
does not compute.

---

## 13. Full-page scroll choreography map

A month page, top to footer. One pin, two scrubbed instruments, every
beat in order.

| Beat | Scroll zone | What the visitor sees and feels |
|---|---|---|
| 1 | Load | The spread assembles in printed order (§6.14): woodcut, name, figures, ring and moon, the tap. The book opens at the right month. |
| 2 | Hero, first scroll | The pin engages (§6.4); the month stays in hand. |
| 3 | Pin travel | Daily tables rise beneath the spread; the moon waxes a little; the light warms almost imperceptibly. Time passing inside the month. |
| 4 | Pin release | The spread lets go with a settle; the month's own chapters begin. |
| 5 | First chapter bound | A stiff leaf turns (§6.2). The book's physics declares itself. |
| 6 | Tide table entry | Rules draw, rows fill, gold ticks stand (§6.3); the tide-line in the margin reaches the first tick and pauses. |
| 7 | Prognostications | Frames open; the straight predictions read as fact; one folded note waits. |
| 8 | Planting table | Counts roll to the counted total (§6.8); the moon, by now, is visibly nearer its next quarter in the corner. |
| 9 | Later chapter bounds | Leaf turns repeat, identical physics, no escalation — the book does not perform harder as it goes. |
| 10 | Order spread | The leaf, the stamps, the ledger promise (§6.16). The tone stays level; commerce is a page of the book. |
| 11 | Footer | The fleuron draws; the next new moon is named (§6.17). The book closes by pointing at the next one. |

**Emotional arc, stated once:** arrival at the right month →
confidence in the tables → one laugh, told straight → the feeling of
time having passed in the hand → a dated reason to return.

**Catch-up behaviour.** Jump scrolls skip ceremonies, never content:
elements below the landing point are printed complete; the moon and
tide-line take their true positions for the landing depth within one
lerp cycle (≤300ms).

---

## 14. Whole-page performance budget

| Budget | Limit |
|---|---|
| Initial HTML + CSS + JS | ≤ 210KB (woodcut SVGs inline-counted) |
| Hero woodcut | ≤120KB raster or inline SVG; total page images ≤600KB |
| Fonts | Fraunces (2 optical/weight cuts) + Source Serif 4 (regular, semibold, italic) ≤ 150KB, subset to Latin + figures |
| JS | ≤ 38KB gz — the moon computation, the shared loop, IO triggers, the fold and the form. There is no framework in this theme. |
| Per-frame (shared loop) | ≤1.2ms total: moon mask (only on ≥0.02-day change), tide-line path, warmth variable, ≤2 parallax plates |
| Long tasks | None over 50ms; the phase computation is arithmetic, the counts are DOM reads capped at 500 nodes |
| LCP | The spread's printed state (no JS) ≤2.0s on a mid-range Android over 4G; assembly animation must never delay it |
| CLS | ≤0.02 — tables are fully laid out before they fill; the skeleton reserves exact row heights |

**Cut order when the budget is exceeded (in order; the book is cut
from its ornaments inward, never from its data):**
1. Harvest dust (§6.9).
2. Temperature drift's smoothness (stepped mode, §6.9).
3. Woodcut parallax.
4. Leaf-turn angle (−18°→−10°) before the turn itself.
5. Card entry stagger.
6. The zodiac draw (ring prints instead).

**Never cut:** the moon's correctness, any table's completeness, the
fallbacks and watchdogs, the reduced-motion variants, the one absurd
note.

---

## 15. Build-order checklist

1. Print the book first: full HTML for every page type with complete
   tables, open notes, dated static moon — passing §10 items 2, 3
   with no JavaScript written yet.
2. Palette, type scale and ruled-table CSS; verify §2 ratios by
   measurement, including the drift-extreme contrast check (§10.6)
   with the overlay at both caps.
3. The date/moon module: §6.1's formula with unit tests on the three
   §10.1 dates plus a cusp date; the zodiac ranges from §12.
4. Static instruments: corner moon (computed), ring (gilded),
   zodiac man (pointing) — all correct with animation still absent.
5. The shared rAF loop and the scrubbed instruments (moon wax,
   tide-line, warmth, parallax), with exact scroll-back reversal.
6. Entry ceremonies: spread assembly, table fills, figure rolls —
   each with its watchdog wired before its animation is enabled.
7. Leaf turns and the single pin, with jump-scroll snap behaviour.
8. Interactions: thumb mark, footnote folds, plate tilt — dwell and
   focus parity included.
9. Skeleton + leaf-flip transition; slow-connection disarm.
10. The order leaf: native form first, enhancements second, ledger
    confirmation from the real system.
11. Reduced-motion pass: every §6 variant verified as a complete
    reading experience, not a diminished one.
12. Print stylesheet and the §10 print check.
13. Dark (lamplight) scheme, woodcuts restyled — or the scheme is
    removed, per §2.
14. Full §10 gate run with evidence: three moon dates, three
    tide-line ticks, three zodiac dates, one full-page screenshot
    for the madder/gold ration.
15. The five-second test (§10.20) with a viewer who has not seen
    the build before.

