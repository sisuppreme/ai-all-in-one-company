# 53. Moon Garden — Expanded (v1 + v2)

> Identity preserved exactly from the original entry: a garden planted
> to be seen at night — white flowers, silver foliage, a site that only
> fully "blooms" in its dark sections, scent treated as a design
> material; the same five palette anchors — Night soil `#10131A`,
> Shadow leaf `#232A38`, Silver foliage `#8E9AAF`, Moonflower white
> `#F2F0E4`, Moth gold `#D9C98A`; Cormorant + Alegreya Sans; all 10
> original signature elements deepened, not redesigned (moonrise hero,
> petal-mask flower panels, the two moths, deepening night, waxing
> progress moon, self-drawing moonflower vine, petal-opening headline,
> hover bloom, pollen puff click, first-light footer), plus 8
> page-family elements to reach 18. Original ~1,050 words → this file.

## 1. Concept & world

A Moon Garden site is an evening that happens to be a web page. The
visitor arrives at dusk, walks a garden planted for the dark — white
flowers that open at night, silver foliage that exists to catch
moonlight — and leaves at first light. Scroll is not navigation here;
scroll is *the evening passing*. The page begins at the garden gate at
19:40 and ends at midnight, and everything the visitor sees — the
grounds darkening bed by bed, the moon climbing its vine arc and
waxing as it climbs, the printed programme times beside each section —
is that one evening, told four ways at once.

The concept only works because the garden is real in the copy. The
canonical build is a venue that genuinely opens after dark: a
botanical garden's evening programme, a historic house with night
tours, a wedding venue whose selling hour is twilight, a perfumery
whose ingredients bloom at night, an observatory with a planted
approach. The flowers named on the page are the flowers planted in
the beds; the moths cross the section about night pollinators because
that is where moths are; the fragrance number on each section is the
scent that section's planting actually carries. A Moon Garden built
over content that has no night in it is a screensaver with a booking
form, and §9 names it as the theme's first failure mode.

**The one law: one night, one moon, every figure from a declared
function.** Three declared functions generate every number and every
light value on the page, and they are printed in §4 where any builder
or auditor can read them:

- `nightAt(p)` — page progress `p ∈ [0,1]` drives the grounds: each
  section's background is a declared interpolation between `--leaf`
  and `--soil` across that section's own scroll window. No section
  darkens by hand, by overlay, or by mood.
- `moonAt(p)` — the same `p` gives the progress moon its height on
  the vine arc and its phase (illumination fraction = `p`, named at
  declared thresholds). The moon that measures the page is one moon.
- `eveningTime(p)` = 19:40 + `p` × 260 minutes — every printed
  programme time is this function evaluated at its section's centre.
  The evening is 260 minutes long, gates to midnight, on every page,
  and the footer prints the function so a visitor can check the
  arithmetic.
- `phaseOn(date)` — the *sky's* moon, used only where a real date is
  at stake (the booking confirmation, §6.15): synodic age from the
  declared epoch 2000-01-06 18:14 UTC, period 29.53059 days,
  illumination `(1 − cos(2π · age / 29.53059)) / 2`. Two moons are
  never drawn at once: the progress moon measures *the page*, the
  booking moon measures *the sky*, and the copy never confuses them.

An invented hour, a hand-placed shadow, a phase typed into a caption,
or a bloom count that no bed's planting sums to is a blocking gate
failure (§10). The theme's confidence — labelling sections with what
they would smell like, on a medium that cannot carry scent — is only
charming while every checkable fact on the page checks out.

**Best fit.** Evening-opening venues (gardens, houses, observatories);
night-blooming product lines (perfume, candles, evening teas) whose
ingredients are genuinely nocturnal; wedding and event venues selling
the twilight hour; a spa or retreat whose programme runs after dark;
a single-artist or single-exhibition site staged as one night.

**When NOT to use it.** Anything whose visitor arrives in a hurry:
daylight commerce, comparison shopping, dense dashboards, support
documentation, checkout-first funnels. A page that must be skimmed at
noon in a bright office is fighting this theme's ground, its type
contrast plan and its pacing all at once — use a daylight theme and
link to the evening, don't fake the evening. Also refused: any site
whose content has no real night programme to describe (see above),
and any build unwilling to print its functions — a Moon Garden that
will not declare `eveningTime` is asking for atmosphere without
arithmetic, which is precisely the slop this expansion exists to
prevent.

## 2. Palette

Five anchors, inherited unchanged. The derived list is **closed**:
builders may not invent intermediate night colours; depth is expressed
by moving a section's ground between the declared stops under
`nightAt(p)`, never by tinting ad hoc or by laying a dark overlay over
finished artwork.

| Token | Hex | Role | Usage ratio | Pairing / contrast (measured for this expansion) |
|---|---|---|---|---|
| `--soil` | `#10131A` | Night soil: the deepest ground, late-evening sections, the pin, footer surround | ~34% | Ground for `--moonflower` (16.25:1), `--moth` (11.21:1), `--silver` (6.54:1) |
| `--leaf` | `#232A38` | Shadow leaf: early-evening ground, cards, raised beds on soil | ~26% | Ground for `--moonflower` (12.58:1), `--moth` (8.68:1), `--silver` (5.06:1) |
| `--silver` | `#8E9AAF` | Silver foliage: body text on dark grounds, parallax foliage, the vine, speckle, rules | ~22% | On `--soil` 6.54:1 — licensed body text; on `--leaf` 5.06:1 — licensed body text; on `--firstlight` 4.40:1 — large text only |
| `--moonflower` | `#F2F0E4` | Moonflower white: headlines, the moon disc, open flowers, primary text at emphasis | ~13% | On `--soil` 16.25:1; on `--leaf` 12.58:1; on `--firstlight` 10.94:1 — the footer's text colour |
| `--moth` | `#D9C98A` | Moth gold: the two moths, fragrance numbers, the moon's lit limb tint, scarce accents | ~5% | On `--soil` 11.21:1; on `--leaf` 8.68:1 — always licensed, always rationed (see gold law) |

Derived tokens (the complete list):

| Token | Value | Role |
|---|---|---|
| `--silver-pale` | `#B9C2D0` | Open-flower highlights, the moon's bright limb, hover states of silver text; 10.34:1 on `--soil`, 8.01:1 on `--leaf` |
| `--silver-deep` | `#6B788F` | Captions and disabled states on `--soil` only (4.17:1 — large text and graphical use; never body copy, never on `--leaf` at 3.23:1) |
| `--gold-deep` | `#B3A05E` | Moth gold's pressed/active state and the fragrance number in the first-light band; 7.17:1 on `--soil` |
| `--firstlight` | `#3A3230` | The footer band and the 404's ground — the barely-warmer horizon; carries `--moonflower` text (10.94:1) only |
| `--bed` | `#181D27` | Card ground resting on `--soil` sections (a raised bed is one step up from the soil it sits in); `--silver` on it measures 5.94:1, `--moonflower` 14.76:1 |

**Contrast law (blocking).** The night deepens by *section grounds
moving between declared stops*, never by dimming text. Text colour is
chosen by ground, not by gradient: on `--soil` and `--leaf`, body text
is `--silver` or `--moonflower`; on `--firstlight`, body text is
`--moonflower` only. At the deepest stop, at the fastest scroll, in
the pinned section, every visible text element must still pass WCAG
AA — §10 audits three scroll depths by screenshot. The original
entry's promise is kept verbatim as a build rule: **all copy is
legible in the first-light state by default** — if the scrub, the
masks and the moon were all deleted, the remaining page (grounds at
their lightest declared stops, flowers open, moon risen) must read
perfectly. Darkness is choreography laid over a legible page, never
a precondition for reading it.

**Gold law.** `--moth` is rationed to four jobs: the two moths
themselves, fragrance numbers, the lit limb of the progress moon,
and the pollen motes of §6.9 (which are spent, not displayed — they
fade in 1200ms). Gold body text, gold buttons and gold borders are
refused: gold on this page is a living thing or a number, never a
trim. §10 greps for it.

**Dark mode.** There is no inverted mode and no day mode. Under
`prefers-color-scheme: light`, the visitor gets the **first-light
edition**: grounds rest at their lightest declared stops (`--leaf`
sections, `--firstlight` footer), the moon is shown risen and full,
flowers ship open, and the deepening scrub (§6.4) is disarmed — the
page is the same garden photographed at dawn, not a different garden
painted white. The print stylesheet is the second light surface: it
prints the first-light edition on white, moon drawn as an outline
disc, phases printed as their names.

## 3. Typography

Two families, inherited: **Cormorant** for display (its italics are
the theme's flowers — see law 1) and **Alegreya Sans** for everything
that must be read, counted, tapped or trusted.

| Role | Face / weight | Size (≥1200px) | Line-height | Tracking | Rules |
|---|---|---|---|---|---|
| Display (hero headline) | Cormorant 500, italic line permitted | 84px | 0.96 | −0.015em | The italic line unfurls letter by letter (§6.7); roman line is set still |
| Section headline | Cormorant 500 | 46px | 1.04 | −0.01em | Never uppercase; a garden does not shout after dark |
| Fragrance number + scent note | Alegreya Sans 700 / 400 italic | 13px / 15px | 1.3 | 0.16em (number) | The number is data (§6.12); the note is a caption in the Gardener's voice (§12) |
| Standfirst / lead | Alegreya Sans 400 | 20px | 1.55 | 0 | Max 36ch in early sections, 44ch in deep sections (the eye slows as the light goes) |
| Body | Alegreya Sans 400 | 17px | 1.65 → 1.78 | 0 | Line-height loosens with depth (law 5); measure 56–64ch |
| Data (times, counts, phases) | Alegreya Sans 700 | 13px | 1.2 | 0.12em, uppercase | Always tabular; always produced by a §1 function or a DOM count — never typed |
| Button / label | Alegreya Sans 700 | 14px | 1 | 0.1em, uppercase | Sentence rhythm inside the caps: "Book the evening" not "BOOK NOW" |
| Caption | Alegreya Sans 400 italic | 14px | 1.5 | 0 | Flower names in captions take Cormorant italic (law 1) inside an Alegreya sentence |

**Five type laws.**
1. **Italics are flowers.** Cormorant italic is rationed to three
   jobs: the hero headline's opening line (§6.7), flower names
   wherever they appear in prose, and the footer's closing line.
   An italic paragraph, an italic button or an italic price is a
   weed — §9 names it. The ration is what makes the headline's
   unfurling legible as an event.
2. **Fragrance numbers are data, not decoration.** Every section
   head carries `№ n` in Alegreya Sans tabular, assigned in DOM
   order, counted — never styled in Cormorant, never skipped, never
   reordered for looks. A page whose numbers run 1, 2, 4 has a
   missing bed, and §10 treats it as one.
3. **Times are computed, then set.** Programme times come from
   `eveningTime(p)` (§1) and are written by the formatter as
   `21:10` — 24-hour, no "9ish", no "at dusk" standing in for a
   time the function could have produced. "Dusk" is a place in the
   copy, not a time in the data.
4. **No headline may promise a flower the page does not show.** If
   the headline says the jasmine is open, a jasmine panel (§6.2)
   exists below it with its scent note. Cormorant's elegance is not
   a licence to inventory flowers the garden doesn't grow.
5. **Line-height loosens as the night deepens** (1.65 in `--leaf`
   sections → 1.78 in `--soil` sections): reading slows as the
   light goes, and the leading admits it instead of pretending the
   last bed is read like the first.

## 4. Layout language

**Beds, not blocks.** The page is a sequence of planted beds. Each
section is one bed: a ground (its `nightAt` stop), a fragrance number
(§6.12), a planting (its content), and a path edge — the 1px
`--silver` rule at 24% opacity that separates beds the way a brick
edge separates soil. Sections are never cards floating on a shared
background; the ground itself changes at each bed, because the ground
*is* the time of evening (§1). A builder who reaches for a card grid
on a shared grey field has built a different theme (§9.2).

**The declared night (the functions, printed in full).** All
scrubbed values on the page are read from these, and from nothing
else:

- **Progress.** `p = scrollY / (docHeight − viewportHeight)`,
  computed once per frame by the shared loop (§5) from un-lerped
  scroll, then lerped at 0.10 for cosmetic values. Instruments that
  print numbers (times, the moon's phase name) read the **un-lerped**
  `p`, so a printed time is always exactly true even while a cosmetic
  layer is still settling toward it.
- **`nightAt(p)`.** Each bed declares `data-night-from` and
  `data-night-to` as stops on the `--leaf` → `--soil` axis (0 =
  `--leaf`, 1 = `--soil`) and a scroll window `[w0, w1]` in page
  progress. Ground = the sRGB interpolation of the two anchors at
  the bed's local progress, clamped. Page-level defaults: the gate
  bed sits at 0, the footer bed at 0.55 (it warms instead — §6.10),
  and no bed may declare a window that takes it *lighter* as `p`
  grows. The night only deepens; §10 samples five scroll positions
  and checks monotonicity.
- **`moonAt(p)`.** The progress moon (§6.5) rides the vine arc in
  the margin rail: arc height = `p` mapped along the arc's path;
  illumination = `p`; phase names at declared thresholds — `p <
  0.22` "waxing crescent", 0.22–0.48 "first quarter", 0.48–0.78
  "waxing gibbous", 0.78–0.97 "nearly full", `p ≥ 0.97` "full". The
  name printed beside the moon is this table and nothing else.
- **`eveningTime(p)`** = 19:40 + `p` × 260 min, formatted `HH:MM`.
  Gate bed prints 19:40 at its centre by construction (its centre
  sits at `p ≈ 0`); the last programme bed's centre must fall at or
  before 23:20 so the footer owns the approach to midnight. A bed
  whose printed time contradicts its position is a gate failure.
- **`phaseOn(date)`** (booking only, §6.15): age = (date − epoch)
  mod 29.53059 d, epoch 2000-01-06 18:14 UTC; illumination =
  `(1 − cos(2π · age / 29.53059)) / 2`; named by the same threshold
  table as `moonAt`, with "new" below 0.03 and "full" above 0.97.
  The formula is printed in the footer (§6.10) — the sky rule is
  part of the page's public record.

**The margin rail.** On ≥1200px the page carries a 72px left rail —
the garden path. In it, top to bottom: the self-drawing vine (§6.6),
the progress moon riding its arc (§6.5), and the current bed's
fragrance number, set vertically. The rail is the page's only
instrument panel; nothing else is fixed. At 768–1199px the rail
narrows to 48px and the vine simplifies (§6.6); below 768px the rail
is gone and the moon becomes a 28px disc in the sticky header
(§6.11), because a phone has no margin to plant in and the spec
admits it rather than squeezing the path into the text.

**Density falls with darkness.** Early beds (before `p` 0.4) may run
two-column plantings and card rows; deep beds (`p` past 0.7) are
single-column, measure narrowed to 52–58ch, one idea per bed. The
garden thins as it darkens — a visitor deep in the night is reading
by moonlight, and the layout behaves as if it knows.

**Whitespace is unlit ground.** Space on this page is not empty; it
is soil the moon hasn't reached. Generous vertical spacing between
beds (≥18vh at desktop) is the path between plantings, and it is
never filled with banners, badges or cross-sell blocks. A bed that
needs more room takes it from the path, never by shrinking its type.

**The one pin.** Exactly one section pins: the pollinator bed
(§6.3), at 200vh on desktop. A second pin is refused — a garden has
one moment where you stop walking and stand still, and it is the
moths'. Every other section scrolls at document speed, its layers
parallaxing inside it (§5).

## 5. Full motion system

Five named easings, used everywhere and nowhere else:

| Token | Curve | Character | Used by |
|---|---|---|---|
| `--ease-bloom` | `cubic-bezier(0.22, 1.4, 0.36, 1)` | Opens past its mark and settles back — a petal overshooting as it unfurls | Petal masks (§6.2), hover bloom (§6.8), headline unfurl (§6.7) |
| `--ease-rise` | `cubic-bezier(0.16, 1, 0.3, 1)` | Long, slow lift with a soft arrival | Moonrise (§6.1), card leaf-tilt return (§6.13), footer warming (§6.10) |
| `--ease-drift` | `cubic-bezier(0.45, 0, 0.55, 1)` | Even, unhurried travel; no arrival emphasis | Moths (§6.3), foliage parallax smoothing, speckle fade (§6.17) |
| `--ease-draw` | `cubic-bezier(0.65, 0, 0.35, 1)` | Steady stroke progress, plant-paced | Vine (§6.6), rules, underline draws |
| `--ease-settle` | `cubic-bezier(0.3, 1.2, 0.4, 1)` | Small press-and-rest for physical things | Pollen release (§6.9), stamps, button presses |

**Every motion term, translated or refused:**

- **Scroll-triggered reveals** → petal masks (§6.2): content is
  revealed by a flower opening, because on this page a reveal *is* a
  bloom. Generic fade-ups are refused (§9.4).
- **Scroll-driven / scrubbed animation** → the deepening night
  (§6.4), the vine (§6.6), the moon's climb (§6.5) — all read from
  the §4 functions through the one shared loop.
- **Parallax** → silver-foliage layers at 0.3× scroll speed ("moth
  speed" — the original entry's term, kept): foliage drifts slower
  than the path because it is rooted. Two layers maximum per bed
  (0.3× and 0.55×); a third layer is a screensaver (§9.3).
- **Pinned sections** → exactly one: the moth crossing (§6.3).
- **Masked reveals** → the 8-petal radial mask (§6.2). Clip-path
  wipes and curtain lifts are refused; nothing in a garden is a
  curtain.
- **Blur-to-sharp** → **refused, by name.** Night does not sharpen;
  it brightens. Flowers arrive by brightness (0.55 → 1.0 under the
  moon, §6.1/§6.2), never by focus. A blurred photograph on this page
  reads as a broken photograph, not as dusk.
- **Animated counters** → bloom counts and the evening's figures
  (§6.14), counted from the planting data, rolling once, upward
  only, and only between two true values.
- **Progress indicators** → the waxing moon (§6.5). Progress bars,
  percentage readouts and scroll spinners are refused: the night
  does not do percentages.
- **Marquee** → **refused.** Nothing in a night garden hurries in a
  line. The footer's record (§6.10) is a printed table, not a ticker.
- **Kinetic typography** → refused beyond the one licensed event:
  the headline's italic letters unfurling (§6.7). Letters elsewhere
  are planted, not performed.
- **Ambient loops** → rationed to three, each with a census in §10:
  the two moths (§6.3), the speckle twinkle (§6.17, ≤40 points,
  never synchronised), the silver grain shimmer (§6.17, two layers,
  uneven by construction). A fourth ambient loop is a gate failure.
- **Micro-interactions** → hover bloom (§6.8), pollen puff (§6.9),
  leaf-tilt (§6.13), the moon's limb brightening on the rail. Each
  is the plant responding to attention, in the plant's own material.
- **Page transitions** → a cloud passes across the moon: the page
  dims to 40% over 600ms, swaps, re-brightens over 900ms (§6.16).
  The moon is the page's light source, so a transition is weather.
- **Image treatments** → moonlight brightening by distance (§6.1)
  and the petal mask (§6.2). Filters beyond brightness are refused;
  a sepia or blue "night filter" over photography is §9.1's slop.

**The shared loop.** One `requestAnimationFrame` loop drives every
scrubbed value: grounds (§6.4), vine draw (§6.6), moon position and
phase (§6.5), foliage parallax, grain (§6.17). Lerp factor 0.10 for
grounds and moon (the night does not hurry), 0.14 for parallax,
0.18 for the grain. The loop sleeps when the tab is hidden and when
no subscribed value is more than 0.001 from its target. Scroll
handlers never write styles; they record `scrollY` and the loop
does the rest. Time-based ambient motion (moths, twinkle) runs on
the same loop's clock but is **not** scroll-scrubbed — a moth does
not speed up because the visitor scrolled fast (§6.3).

**Durations ledger (the complete list; no other durations exist).**
Moonrise 4000ms; headline unfurl 90ms/letter stagger, ≤1400ms total;
petal mask open 1200ms; hover bloom +8% over 400ms, settle 800ms;
moth crossing ~14000ms per pass; vine draw scrubbed (no fixed
duration — it is `p`); portrait/flower brightening 900ms per step at
150ms distance stagger; counters 1600ms; cloud transition 600ms dim
+ 900ms brighten; pollen motes 1200ms life; twinkle cycle 2600–
5400ms per point, randomised; grain shimmer 9000ms per layer cycle.
Any duration a builder needs that is not on this ledger gets added
to the ledger in review, or the motion does not ship.

## 6. Signature elements

### 6.1 Moonrise hero

- **What & why.** On load, a pale moon disc (~38vmin, radial gradient
  from `--moonflower` to transparent at 72%) rises behind the hero
  headline over 4000ms, and as its light "reaches" each flower image
  in the hero, that image brightens from 0.55 to 1.0. It belongs
  because the whole theme is the claim that this garden is lit by one
  moon; the hero is where that claim is made, in view, before any
  copy asks to be believed. The moon is not a logo and not a backdrop
  photograph — it is the page's declared light source (§1 law), and
  every later brightness on the page is consistent with it.
- **Structure.** One absolutely-positioned disc element inside the
  hero bed, `aria-hidden`, behind the headline (z-order: ground →
  foliage layer → disc → text). Flower images are real `<img>`
  elements in the hero's planting row, each carrying
  `data-light-distance` (its authored distance step from the disc,
  0–5). Brightness is applied as a CSS `filter: brightness()` custom
  property per image, driven by the shared loop; the unlit value
  0.55 is set by JS only (see fallback).
- **Motion spec.** Trigger: load, gated on `document.fonts.ready`
  raced against a 900ms timer. Disc translates from 12vmin below its
  rest position to rest over 4000ms `--ease-rise`, opacity 0 → 1 in
  the first 1200ms. Each flower image brightens 0.55 → 1.0 over
  900ms `--ease-rise`, starting at `600 + distance × 150ms` — the
  light visibly travels outward from the disc. Runs once per page
  load; never replays on resize or scroll return.
- **States.** Unrisen (JS-armed only, pre-trigger) → rising →
  risen-and-resting (the disc stays as the hero's light for the
  whole visit; it does not set until the footer, §6.10). Session
  return: a `sessionStorage` flag paints the moon risen and the
  flowers lit from first paint — a returning visitor is not made to
  wait for dusk twice.
- **Content merge.** The moon lights the actual product: the hero's
  flower images are the night-blooming stock the venue sells
  evenings with (moonflower, night-scented stock, evening primrose),
  each captioned with its name and its opening hour from
  `eveningTime`. Remove the disc and the images' brightening has no
  cause; remove the images and the disc is a screensaver. Neither
  survives alone, which is the test every element in this theme must
  pass.
- **Failure fallback.** Watchdog: if the rise has not completed by
  5200ms after trigger, disc and images snap to their final states.
  No JS: the disc ships at rest position at full opacity and images
  ship at brightness 1.0 in the HTML; JS arms the unrisen/unlit
  states only after first paint confirms the loop is alive. A slow
  font can delay the trigger by at most the 900ms race.
- **Reduced-motion variant.** The moon is shown risen, the flowers
  lit, from first paint. The hero is complete and still; the fact of
  moonlight is kept, the rising is not performed.
- **Performance budget & mobile variant.** One gradient disc (no
  image asset), ≤6 hero images ≤70 KB each, brightness filters on
  transform-isolated layers. Frame cost inside the shared loop:
  negligible (≤8 style writes during the rise only). Mobile
  (<768px): disc shrinks to 30vmin, rise shortens to 2600ms, the
  planting row stacks to one column and the distance stagger caps at
  3 steps — the light travels a shorter garden.
- **Choreography timeline (v2).** t=0 fonts ready (or 900ms race
  lost) → t=0–1200 disc fades in while beginning its rise →
  t=600 first (nearest) flower begins brightening → t=750, 900,
  1050… further flowers at 150ms distance steps → t=4000 disc at
  rest → t≈3900–4800 last flower finishes → hero at rest; the
  headline's unfurl (§6.7) begins at t=1400, inside the rise — the
  name blooms while the moon is still climbing, as the real flowers
  open before the moon is fully up.
- **State matrix (v2).** *Rest:* disc at rest, flowers lit.
  *Hover:* none — the disc is not a control; hero images carry their
  own hover via §6.8 when they are panels. *Focus:* none. *Active:*
  n/a. *Scrolled-past:* disc parallaxes at 0.55× within the hero
  only, then leaves with it; it never follows the visitor down the
  page (the progress moon, §6.5, is a different, smaller moon — the
  rail instrument — and §9.6 names confusing the two as slop).
  *Disabled / no-JS:* risen and lit at first paint. *Touch:*
  identical; no touch behaviour of its own.
- **Breakpoints (v2).** ≥1200px: 38vmin disc, full 4000ms rise, up
  to 6 distance steps. 768–1199px: 34vmin disc, rise 3200ms, ≤4
  steps. <768px: 30vmin disc, rise 2600ms, ≤3 steps, planting row
  single-column.
- **Edge cases & failure modes (v2).** *Tab hidden mid-rise:* rAF
  pauses; on return, if elapsed wall time > 5200ms the watchdog
  completes the rise instantly. *Hero images slow to load:* an image
  that has not decoded when its brighten step fires brightens on
  decode instead — the stagger is by distance, not by load order.
  *Very tall hero:* the disc's rest position is anchored to the
  headline's baseline, measured at trigger time, never hard-coded.
  *Session return:* painted risen (see States).
- **Accessibility spec (v2).** The disc is `aria-hidden="true"` and
  never receives focus. Flower images carry real alt text naming the
  flower and its opening hour; the brightening is decorative
  emphasis on content that is fully legible at 0.55 (silver captions
  on soil measure 6.54:1 regardless of image brightness). No
  information is carried by brightness alone.
- **Tokens consumed (v2).** `--moonflower`, `--silver-pale`,
  `--soil`, `--ease-rise`, `--dur-moonrise` (4000ms),
  `--dur-fallback-moonrise` (5200ms), `--disc-size` (38vmin).

### 6.2 Petal-mask flower panels

- **What & why.** Each flower panel — a photograph of one of the
  garden's night bloomers, with its name, scent note and opening
  hour — is revealed through an 8-petal radial mask that scales and
  rotates open over 1200ms as the panel crosses viewport centre. It
  belongs because on this page a reveal is a bloom (§5): the panel
  *is* a flower, and opening it is the content arriving, not a
  curtain being pulled off the content. This is the theme's primary
  reveal grammar; every photographic reveal on the page uses it or
  is refused.
- **Structure.** The panel is a `<figure>` with the `<img>`, a
  `<figcaption>` (name in Cormorant italic, scent note, opening
  hour from `eveningTime` at the panel's bed centre). The mask is an
  inline SVG 8-petal radial mask referenced by `mask-image`, its
  scale/rotation driven by a `--petal` custom property (0 = closed,
  1 = open) written by the shared loop from the panel's viewport
  position. The caption is never masked — only the photograph blooms;
  the words are planted, not performed (§3, law 1's spirit).
- **Motion spec.** Trigger: the panel's centre crossing the
  viewport's centre band (±18% of viewport height) while scrolling,
  in either direction, once. `--petal` animates 0 → 1 over 1200ms
  `--ease-bloom`; simultaneously the photograph's brightness goes
  0.7 → 1.0 (it opens into moonlight). Scrolled past quickly (centre
  band crossed in <300ms of scroll), the panel opens at 2× speed —
  the garden does not punish a fast walker by leaving flowers shut.
- **States.** Closed (JS-armed only) → opening → open (terminal; a
  flower that has opened for a visitor does not close again on
  scroll-up — the evening does not unbloom). *Hover/focus:* §6.8
  extends the opening a further ~8%. *Scrolled-past:* open.
  *Disabled:* the mask is inert; photograph fully visible.
- **Content merge.** The mask's petals are the pictured flower's own
  petal count where the species allows: moonflower panels use the
  8-petal standard, jasmine panels a 5-petal variant, stock a
  4-petal cross — the mask is drawn from the flower in the
  photograph, so the reveal is the plant's own geometry. The
  caption's opening hour is the hour that species actually opens,
  printed from the bed's `eveningTime` value so panel and programme
  can never disagree.
- **Failure fallback.** The original entry's 1.5s law, kept and
  hardened: an IntersectionObserver fallback **and** a 1500ms
  watchdog per panel — if `--petal` has not reached 1 within 1500ms
  of the panel entering the viewport by any path (observer miss,
  loop stall, fling scroll), the mask is removed entirely. No JS:
  no mask is applied in the HTML at all; JS arms masks only on
  panels below the fold after first paint.
- **Reduced-motion variant.** Panels ship open, brightness 1.0. The
  photograph and caption are simply there, the way a pressed flower
  is there — the bloom is not performed, the flower is not withheld.
- **Performance budget & mobile variant.** Mask is one SVG per petal
  count (3 masks shared by all panels, not one per panel); the
  `--petal` write is transform/opacity-class only, no layout.
  Panels ≤90 KB per image, lazy below the first bed. Mobile
  (<768px): mask simplifies to a 6-petal radial at 900ms; panels
  stack single-column and the centre band widens to ±26% so a thumb
  scroll still triggers blooms reliably.
- **Choreography timeline (v2).** Panel centre enters the band →
  t=0 mask begins (petals at 12% scale, rotated −14°) → t=0–1200
  petals scale to 100% and rotate to 0° on `--ease-bloom`, the
  overshoot peaking at t≈780 (petals at 106%) → brightness tracks
  0.7 → 1.0 across the same window → t=1200 panel open, mask
  retired to `none` (the flower stays open by removal of the mask,
  not by holding a value) → caption was readable from t=0.
- **State matrix (v2).** *Rest (open):* photograph full, mask none.
  *Hover:* §6.8's +8% petal expansion and +6% brightness (desktop,
  pointer-fine). *Focus:* identical to hover — focus is attention,
  and attention is moonlight (§6.8). *Active:* n/a (panel is not a
  control unless it links to a bed detail, §7). *Scrolled-past:*
  open. *Disabled / no-JS:* unmasked, fully visible. *Touch:* no
  hover state; a tap on a linked panel navigates — the bloom on tap
  is not faked.
- **Breakpoints (v2).** ≥1200px: species-true petal counts, 1200ms,
  centre band ±18%. 768–1199px: petal counts kept, 1050ms, band
  ±22%. <768px: 6-petal standard mask regardless of species (the
  species truth moves to the caption, which names the petal count
  in words), 900ms, band ±26%.
- **Edge cases & failure modes (v2).** *Anchor jump directly to a
  panel:* it is found open (jump = already visited; the watchdog's
  viewport test resolves it instantly). *Panel taller than the
  viewport:* trigger falls back to top-edge crossing 30% line.
  *Image fails to load:* the panel shows its caption and a
  `--bed`-ground plate with the flower's name set in Cormorant
  italic — a labelled empty bed, never a broken-image icon (§9.8).
  *Many panels in one bed:* stagger 90ms apart in DOM order, capped
  at 4 concurrent openings.
- **Accessibility spec (v2).** The mask is presentational; the
  `<img>` alt names the flower, and the caption is never masked,
  clipped or delayed. Panels that link are real links with a 44px
  minimum target and a visible focus ring in `--silver-pale`
  (10.34:1 on soil). The opening animation is not announced; screen
  readers meet the finished flower.
- **Tokens consumed (v2).** `--petal`, `--ease-bloom`,
  `--dur-petal` (1200ms), `--dur-fallback-petal` (1500ms),
  `--moonflower`, `--bed`.

### 6.3 The two moths

- **What & why.** In one pinned section — the pollinator bed — two
  small moth-gold moths (14px and 18px) drift on slow sine paths and
  cross the bed once, unhurried, over ~14 seconds. They belong
  because they are the venue's actual evening inhabitants, placed in
  the section whose copy is about night pollinators: the animation
  is the exhibit, not an ornament near it. There are exactly two.
  A third moth is a gate failure (§10 census), because a garden at
  night has the moths it has, not a particle system.
- **Structure.** Two inline SVG moths (body + two wing pairs), wings
  fluttering by `scaleY` at 9Hz — the original entry's figure, kept:
  9Hz is a real moth's wingbeat neighbourhood, and the flutter is
  the only fast motion on the page, spent on the smallest thing on
  it. Paths are two authored sine curves across the pinned stage,
  computed in the shared loop from elapsed *visible* time, not from
  scroll. The moths are `aria-hidden`, `pointer-events: none`, and
  fly in the stage's air layer — above the ground, below nothing
  textual: their paths are authored to cross the bed's open ground
  and its photograph, never its text column.
- **Motion spec.** Trigger: the pollinator bed entering its pin.
  The stage pins for 200vh of scroll; while pinned and visible, the
  moths fly: moth A left→right, moth B right→left at 0.8× speed,
  vertical sine amplitude 6vh, one crossing ≈14000ms. When the pin
  releases, flight pauses mid-path (the moths hang in the section's
  air, wings still, if the visitor scrolls back — they do not reset
  and they do not chase). Flight time accumulates only while the
  stage is in view and the tab is visible: a moth does not cross a
  garden nobody is watching.
- **States.** Waiting (before first pin) → crossing → crossed
  (resting at path ends, wings folding to rest over 600ms
  `--ease-settle`) → on re-entry after a full page revisit, they
  cross back the other way — the return is a new crossing, not a
  replay. *Hover:* none; the moths ignore the pointer completely
  (they are not the cursor's pets, §9.5). *Disabled:* absent.
- **Content merge.** The bed's copy names the species the drawings
  follow (the larger is a hummingbird hawk-moth at 18px — drawn at
  its true relative size against the 14px white-shouldered moth),
  and the bed's planting list is the plants those species visit.
  The moths cross *that* planting's photograph. If the build's
  pollinator copy changes species, the drawings change with it —
  the census in §10 checks drawing against copy.
- **Failure fallback.** If the loop stalls or the pin fails (CSS
  `position: sticky` unsupported), the section simply scrolls
  unpinned and the moths rest at their path starts beside the
  photograph — present, still, honest. No JS: the moths are printed
  at rest at their starting positions as part of the bed's
  illustration; the crossing is an enhancement, never a container
  for content.
- **Reduced-motion variant.** Moths absent — the original entry's
  ruling, kept verbatim. The bed's photograph carries a printed
  caption naming the two species, so the information survives the
  motion's removal.
- **Performance budget & mobile variant.** Two SVGs <2 KB total; the
  flight is two transform writes per frame inside the shared loop,
  paused off-screen. Mobile (<768px): **the pin is cut** (a 200vh
  pin under a thumb is a trap, not a pause) — the bed scrolls
  normally and the moths make one slow pass across the photograph
  only if the bed rests in view for 3s, else they stay at rest.
  Tablet keeps the pin at 150vh with amplitude 4vh.
- **Choreography timeline (v2).** Bed reaches pin → t=0 stage locks,
  moths at path starts, wings unfold (300ms) → t=800 flight begins
  (the pause is deliberate: the visitor settles first) → t≈7000 the
  crossing's midpoint, the two paths intersect over the photograph's
  moonflowers → t≈14800 moth A arrives, B at t≈18300 (0.8× speed) →
  wings fold over 600ms → pin releases at 200vh scroll regardless of
  flight state; unfinished flight resumes on re-entry from where it
  hung.
- **State matrix (v2).** *Rest (pre-pin):* moths at starts, wings
  folded. *Hover:* none — explicitly no reaction. *Focus:* none;
  never focusable. *Active:* n/a. *Scrolled-past:* resting at path
  ends or hung mid-path if the visitor flung past (flight time only
  accrues in view, so a fling leaves them near their starts — the
  garden does not pretend a crossing happened unwatched).
  *Disabled / no-JS:* printed at rest. *Touch:* identical flight;
  no touch interaction.
- **Breakpoints (v2).** ≥1200px: 200vh pin, amplitude 6vh, sizes
  14/18px. 768–1199px: 150vh pin, amplitude 4vh. <768px: no pin;
  conditional single pass over the photograph (see budget).
- **Edge cases & failure modes (v2).** *Visitor parks on the pin
  for minutes:* after one full crossing each way, the moths rest —
  they do not loop patrol the section; a looped moth is a
  screensaver (§9.5). *Hidden tab:* flight clock pauses (visible
  time only). *Resize mid-pin:* paths recompute from stage geometry;
  flight progress (0–1 per moth) is preserved, positions re-derive.
  *Sticky unsupported:* fallback per above.
- **Accessibility spec (v2).** `aria-hidden="true"`, no focus, no
  information carried. The species facts live in the bed's copy and
  captions (§12), readable without the flight. Motion is confined
  to a decorative layer and honours the global reduced-motion
  absence above.
- **Tokens consumed (v2).** `--moth`, `--gold-deep`, `--ease-drift`,
  `--ease-settle`, `--dur-moth-cross` (14000ms), `--pin-pollinator`
  (200vh).

### 6.4 Deepening night

- **What & why.** As the reader descends, each bed's ground scrubs
  from `--leaf` toward `--soil` under `nightAt(p)` (§4), while
  silver-foliage layers inside the beds parallax at 0.3×. It
  belongs because it is the theme's central sentence — later
  sections are literally later in the evening — told by the ground
  itself rather than by a caption saying "imagine it's getting
  darker". The deepening is the programme's clock made visible.
- **Structure.** Each bed is a `<section>` with `data-night-from`,
  `data-night-to` and its window declared in markup (auditable —
  §10 reads the declarations, not the pixels). The loop computes
  the bed's ground colour per frame and writes it as a background
  on the section; foliage layers are absolutely-positioned SVG
  foliage silhouettes in `--silver` at 6–10% opacity, transformed by
  the same loop at 0.3× (near layer) and 0.55× (far layer).
- **Motion spec.** Trigger: scroll, continuous. Grounds interpolate
  in sRGB between the two anchors across the bed's window, lerped
  at 0.10 so the night settles rather than snaps when the visitor
  pauses. Foliage parallax is unbounded within the bed (layers are
  authored 12% taller than the bed and clamp at its edges). Scrolling
  up lightens symmetrically — the night is scrubbed, not latched:
  going back up the page is walking back toward dusk, and the ground
  admits it. (Contrast §6.5: the moon does not un-wax, because the
  moon measures the visit, not the hour. The two instruments are
  different on purpose and §12's copy never confuses them.)
- **States.** Each bed: at its `from` stop (before window) →
  deepening (inside window) → at its `to` stop (past window).
  *Hover/focus:* none. *Disabled:* grounds rest at their `from`
  stops — the first-light state (§2), fully legible.
- **Content merge.** The stops are assigned by the programme, not by
  a gradient fetish: the gate bed and the tea bed stay near `--leaf`
  (early evening, people arriving), the pollinator and deep beds go
  to full `--soil`, the footer refuses the axis entirely and warms
  (§6.10). A bed's `data-night-to` is an editorial decision about
  what hour that content belongs to, reviewed like one (§15).
- **Failure fallback.** No JS: grounds are their `from` stops in
  CSS; the page is the first-light edition and loses nothing but the
  deepening. Loop stall: grounds freeze at their current values —
  every stop on the axis passes the §2 contrast law, so a frozen
  night is still a legible night at any point. There is no state of
  this element that can strand text.
- **Reduced-motion variant.** The scrub is disarmed; grounds rest at
  `from` stops for the whole page. The evening's *order* still reads
  (fragrance numbers, printed times), but the light does not move.
- **Performance budget & mobile variant.** Background-colour writes
  on ≤12 sections + ≤2 transform writes per bed per frame, batched
  in the one loop; no gradients repainted per frame (the colour is
  flat by design). Mobile: foliage layers reduce to one (0.3×) and
  the interpolation steps quantise to 32 levels to save fill cost
  on low-end GPUs — the night deepens in small steps a phone can
  afford, invisibly at arm's length.
- **Choreography timeline (v2).** Continuous, not beat-based: as
  `p` crosses each bed's window, that bed's ground travels its
  declared axis over the window's scroll length (typically 60–120vh
  of scroll), foliage drifting throughout; the page's midpoint
  (`p` 0.5) is authored so roughly half the beds have reached full
  `--soil` — the middle of the page is the middle of the night.
- **State matrix (v2).** *Rest:* ground at the stop for current `p`.
  *Hover:* none. *Focus:* none — grounds never react to focus; a bed
  does not lighten because a keyboard arrived (its text was already
  AA at its stop, §2 law). *Active:* n/a. *Scrolled-past:* at `to`
  stop; re-enters symmetrically on scroll-up. *Disabled / no-JS:*
  `from` stops throughout. *Touch:* identical scrub; no
  touch-specific behaviour.
- **Breakpoints (v2).** ≥1200px: two foliage layers per bed.
  768–1199px: two layers, amplitude halved. <768px: one layer,
  quantised steps (see budget).
- **Edge cases & failure modes (v2).** *Jump scroll to footer:*
  grounds resolve to their positional values in one frame (the
  function is positional, not cumulative). *Content added late
  (CMS):* a bed without declarations defaults to `from 0 / to 0.35`
  — it may be shallow, never unlawfully dark. *Print:* grounds
  print at `from` stops (first-light edition, §2).
- **Accessibility spec (v2).** Backgrounds are never the sole carrier
  of the time information: every bed prints its `eveningTime` (§6.12)
  in text. Contrast is audited at both stops and at the window
  midpoint for every bed (§10). The foliage layers are
  `aria-hidden` and stay under 10% opacity so they can never
  masquerade as text or obscure it.
- **Tokens consumed (v2).** `--leaf`, `--soil`, `--silver`,
  `--lerp-night` (0.10), `data-night-from/to` declarations.

### 6.5 Waxing progress moon

- **What & why.** In the margin rail, a small moon (34px) climbs a
  drawn vine arc (§6.6's arc) and waxes — crescent → quarter →
  gibbous → full — across the page's length, its phase computed from
  scroll progress by `moonAt(p)` (§4). It belongs because progress
  on this page is not a percentage; it is the night advancing, and
  the moon is the night's own clock. Full moon at the footer means
  the evening is complete; the visitor has been somewhere, not
  merely scrolled something.
- **Structure.** An SVG moon in the rail: a `--moonflower` disc with
  a shadow circle offset by the phase geometry (the shadow is the
  ground colour of the current bed, so the moon's dark limb is
  literally the night it hangs in), riding the vine arc's path via
  `offset-path` or computed transform from the loop. Beside it, the
  phase name in the §3 data style, printed from the `moonAt`
  threshold table, plus the current bed's `eveningTime` — the two
  instruments share the rail and the function family.
- **Motion spec.** Trigger: scroll, continuous. Height and phase are
  pure functions of un-lerped `p` for their *values*; the disc's
  rendered position lerps at 0.10 toward the computed point so the
  climb is smooth under a jagged scroll. Phase is rendered in 24
  discrete steps (not a continuous smear) — a moon changes by
  nights, and 24 steps across one evening reads as phases, not as a
  loading spinner. The moon never wanes on scroll-up: position
  follows `p` both ways (it is where the visitor is), but the phase
  holds the **maximum** illumination reached this visit — the moon
  measures the visit's furthest point, the way the evening's memory
  does. §12's copy states this once, plainly, in the rail's caption:
  "The moon keeps the furthest you have come."
- **States.** Rising-and-waxing (normal) → full (at `p ≥ 0.97`,
  held) → setting (in the footer bed, §6.10 takes custody and sets
  it below the horizon line). *Hover:* the lit limb brightens 10%
  and the phase name + time print at full opacity (they rest at
  80%). *Focus:* the rail moon is not focusable; its data is
  duplicated in each bed's printed time (§6.12). *Disabled:* moon
  shown full at the arc's top — the finished state.
- **Content merge.** The moon rides the vine (§6.6) that is also the
  page's index: the instrument of progress is physically the same
  drawing as the table of contents. Its phase thresholds gate real
  copy — the deep beds' standfirsts may reference "by full moon"
  only if their window ends past `p` 0.97's approach… no: copy
  references are checked against `moonAt` at the bed's centre in
  §10's audit (a bed at `p` 0.5 may not claim a full moon).
- **Failure fallback.** No JS: the moon ships full at the arc top
  with the caption "FULL — THE EVENING, WHOLE" and every bed prints
  its own time, so progress information survives as text. Loop
  stall: moon freezes; its printed phase name freezes with it (they
  are written by the same frame's computation, so they can never
  disagree mid-stall).
- **Reduced-motion variant.** The moon is shown full at the arc's
  top from first paint, phase name printed as "FULL". Scroll does
  not move it. The rail still carries the vine index (§6.11) — the
  instrument retires, the index remains.
- **Performance budget & mobile variant.** One SVG, one transform +
  one shadow-offset write per frame. Mobile (<768px): the rail moon
  becomes a 28px disc in the sticky header (§6.11), phase rendered
  the same 24 steps, name replaced by the current bed's time only —
  a phone rail has room for the hour, not the lecture.
- **Choreography timeline (v2).** Continuous: at `p` 0 the moon sits
  at the arc's foot as a crescent; each bed boundary (§6.6's blooms)
  passes beneath it as it climbs; at `p` 0.48–0.78 it is gibbous
  over the deep beds; at `p ≥ 0.97` full, it hands over to the
  footer (§6.10), which sets it as the visitor arrives — the last
  beat of the page is the moon leaving, full, having done its work.
- **State matrix (v2).** *Rest:* at computed height/phase for `p`.
  *Hover:* limb +10%, data at full opacity (pointer-fine only).
  *Focus:* n/a. *Active:* n/a. *Scrolled-past:* n/a (it is the
  measure of scrolled-past). *Disabled / no-JS:* full at arc top.
  *Touch:* identical values; no hover brightening.
- **Breakpoints (v2).** ≥1200px: 34px disc in the 72px rail, phase
  name + time printed. 768–1199px: 28px disc in the 48px rail, name
  printed, time moves into the bed heads (§6.12). <768px: header
  disc per budget.
- **Edge cases & failure modes (v2).** *Short page (a listing, §7):*
  the arc compresses; phase still spans crescent→full across the
  page's real length — the moon serves the page it is on. *Phase
  vs. position on scroll-up:* position retraces, phase holds max
  (see Motion spec) — an auditor checking "phase = f(p)" must check
  against max-`p`-this-visit, which the footer record prints.
  *Footer reached without scrolling (anchor):* moon arrives full
  and sets normally.
- **Accessibility spec (v2).** The moon graphic is `aria-hidden`;
  its information content — phase name and current time — is real
  text in the rail, and duplicated per-bed (§6.12), so no visitor
  depends on the rail. The 24-step phase rendering means the graphic
  never contradicts its own caption by a sub-step.
- **Tokens consumed (v2).** `--moonflower`, `--silver-pale`,
  `--moth` (lit limb tint), `--ease-drift`, `--lerp-night` (0.10),
  `--moon-size` (34px).

### 6.6 Self-drawing moonflower vine

- **What & why.** An SVG vine — stem, leaves, and two moonflowers —
  strokes itself up the margin rail in step with scroll, and a
  flower blooms (petal mask, §6.2's grammar at rail scale) at each
  section boundary. It belongs because it is the page's index grown
  rather than listed: the plant climbs the same margin the visitor
  reads down, and its flowers mark the beds the way the real vine's
  flowers would mark a path. It is also the arc the progress moon
  rides (§6.5) — one drawing, three jobs (index, arc, ornament in
  that order of importance).
- **Structure.** One inline SVG in the rail, authored to the page's
  bed map: stem path with `pathLength` normalised, leaf pairs at
  authored intervals, and one flower head per bed boundary
  positioned at that bed's proportional height. Flower heads are
  small 8-petal groups (§6.2 mask at 22px scale) whose open state is
  a class, not a mask — at rail size, open = petals drawn + filled
  `--silver-pale`, closed = outline only. Bed names sit beside their
  flowers as the rail's text (§6.11 shares this structure).
- **Motion spec.** Trigger: scroll scrub. Stem `stroke-dashoffset`
  is a pure function of `p` (the vine has grown exactly as far as
  the visitor has come), written by the loop with the 0.10 lerp for
  smoothness. A bed's flower blooms when `p` crosses that bed's
  start: petals fill over 600ms `--ease-bloom`. Scrolling up, the
  stem un-draws (position is positional) but opened flowers stay
  open — the vine's growth retraces, its blooms are events, and the
  distinction is the same one §6.4/§6.5 draw between hour and
  memory.
- **States.** Growing (normal) → fully grown with all flowers open
  (at footer). *Hover on a flower:* it brightens and its bed name
  prints at full opacity (names rest at 70%). *Focus:* flowers are
  the rail navigation's links (§6.11) — focus opens the flower if
  not yet open (focus is a visit). *Scrolled-past:* grown to `p`,
  flowers open behind. *Disabled:* fully drawn, all flowers open.
- **Content merge.** The vine's flowers are not decorative repeats:
  there is exactly one per bed, at that bed's true proportional
  height, labelled with that bed's name and fragrance number — the
  drawing is a scale map of the page. A build that adds a decorative
  extra flower has added a bed that doesn't exist, and §10 counts
  flowers against beds.
- **Failure fallback.** No JS: the vine ships fully drawn, flowers
  open, names printed — the index works as a static list with a
  drawing beside it. Loop stall: the stem freezes mid-growth; the
  bed names remain printed and linked (§6.11), so navigation never
  depends on the drawing finishing.
- **Reduced-motion variant.** Vine fully drawn, flowers open, from
  first paint. It is a map in this edition, not a growth.
- **Performance budget & mobile variant.** One SVG ≤6 KB; one
  dashoffset write per frame. Tablet (48px rail): leaves are cut,
  stem + flowers only — the map keeps its facts and drops its
  foliage. Mobile: the vine is gone with the rail (§4); its index
  job moves to the header moon + the bed heads themselves (§6.11,
  §6.12).
- **Choreography timeline (v2).** Continuous against `p`: stem tip
  travels the rail's full height across the page's scroll length;
  at each bed boundary the flower there blooms (600ms) as the tip
  passes — growth first, flower second, in the plant's own order;
  the progress moon (§6.5) rides ~4% of arc behind the stem tip, so
  the moon follows the growth up the page.
- **State matrix (v2).** *Rest:* drawn to `p`, flowers open to the
  current bed. *Hover:* per-flower brightening + name to full
  opacity. *Focus:* flower opens if closed; focus ring
  `--silver-pale` on the link. *Active:* link press — flower pulses
  once (scale 1.15, 200ms `--ease-settle`) before navigation.
  *Scrolled-past:* grown, open. *Disabled / no-JS:* fully drawn.
  *Touch:* tap = the link; no hover brightening.
- **Breakpoints (v2).** ≥1200px: full vine, leaves + flowers, 72px
  rail. 768–1199px: stem + flowers, 48px rail, names abbreviated to
  fragrance numbers with full names on focus/hover. <768px: absent
  (see budget).
- **Edge cases & failure modes (v2).** *Very long page:* stem path
  is generated from the bed map at build time; a page with >14 beds
  is refused at review (split the evening, §7) rather than letting
  the vine crowd. *Bed added by CMS:* the vine regenerates from the
  same bed map the fragrance numbers use (§6.12) — one source, so
  vine, numbers and moon arc can never disagree about how many beds
  the night has.
- **Accessibility spec (v2).** The SVG is `aria-hidden`; the index
  function is carried by real links with real text (§6.11) in DOM
  order matching bed order. Flower open/closed state is never the
  sole indicator of the current bed — the current link carries
  `aria-current` and full-opacity text.
- **Tokens consumed (v2).** `--silver`, `--silver-pale`, `--moth`
  (flower centres), `--ease-draw`, `--ease-bloom`, `--dur-vine-bloom`
  (600ms).

### 6.7 Petal-opening headline

- **What & why.** The hero headline's italic line starts with its
  letters rotated 6° and dimmed to 45%, then unfurls one by one —
  90ms stagger, each letter rotating to 0° and brightening to full
  as it opens, like petals. It belongs because the venue's name is
  the first flower of the evening: the typography behaves as the
  garden does, once, at the door. This is the theme's single
  licensed piece of kinetic typography (§5); its licence is that it
  happens once, on one line, and means something.
- **Structure.** The italic line's letters are wrapped in spans by JS
  (the HTML ships the line as plain text — see fallback), each span
  carrying `--i` (its index). Rotation is around the letter's bottom
  centre (the petal's hinge is its base). The roman line of the
  headline is never wrapped, never animated — it is the stem the
  italic line blooms from.
- **Motion spec.** Trigger: t=1400ms inside the moonrise (§6.1's
  timeline) — the name opens as the light reaches it. Per letter:
  rotate 6° → 0° and brightness 0.45 → 1.0 over 700ms
  `--ease-bloom`, staggered 90ms. Cap: lines longer than 16 letters
  compress the stagger to fit a 1400ms total (stagger =
  min(90, 700/letters)) — a long name opens faster per letter, never
  longer overall. Runs once; never replays.
- **States.** Closed (JS-armed only) → unfurling → open (terminal).
  *Hover:* none — the name is not a toy. *Focus:* none.
  *Scrolled-past:* open. *Disabled:* printed open. *Session
  return:* open from first paint (with §6.1's risen moon).
- **Content merge.** The line that unfurls is the line that names
  the garden or its night ("The garden, after dark" — the italic
  promise), and the letters' hinge-at-base rotation is the petal
  geometry of §6.2's masks at type scale. If a build unfurls a
  marketing slogan instead of the name, §9.7 names it: the bloom is
  for what the place is, not for what it is selling this week.
- **Failure fallback.** No JS: the line is plain, open, full
  brightness text — the wrapping is JS-only and the pre-state
  (rotated/dimmed) is applied by JS at arm time, never in CSS that
  ships. Watchdog: if the unfurl has not completed by t=3400ms, all
  letters snap open. A stalled unfurl can therefore never leave the
  venue's name half-shut.
- **Reduced-motion variant.** The line prints open. The name is
  simply there, in italic, at full brightness — the flower pressed,
  not performed (§6.2's ruling, shared).
- **Performance budget & mobile variant.** ≤16 transformed spans for
  ≤1400ms; negligible. Mobile: the italic line wraps to two lines on
  narrow screens — letters unfurl in reading order across the wrap,
  hinge geometry unchanged; stagger compresses per the cap rule.
- **Choreography timeline (v2).** t=1400 (inside moonrise) first
  letter begins → letters open left to right at 90ms (or compressed)
  stagger, each 700ms → last letter settles at ≤t=2800 → t=3400
  watchdog deadline passes unused → the headline rests, and never
  moves again for the rest of the visit.
- **State matrix (v2).** *Rest:* open, full brightness. *Hover:*
  none. *Focus:* none. *Active:* n/a. *Scrolled-past:* open.
  *Disabled / no-JS:* open as printed text. *Touch:* identical
  timing; no touch behaviour.
- **Breakpoints (v2).** ≥1200px: 84px display size, full stagger.
  768–1199px: 64px, stagger cap 1200ms total. <768px: 46px, two-line
  wrap permitted, total ≤1100ms.
- **Edge cases & failure modes (v2).** *Letters with descenders or
  accents:* rotation origin at bottom centre keeps descenders from
  sweeping the line below; accented letters rotate as one glyph
  (wrapping is by grapheme cluster, never by code unit — a build
  that splits a combining mark has broken the name, §10 checks a
  name with an accent in the fixture). *Very long venue names:*
  the roman line takes the name; the italic line is the short
  promise — editorial rule, enforced in §15's copy pass.
- **Accessibility spec (v2).** The headline is one `<h1>` with its
  full text intact for assistive technology (spans are
  `aria-hidden` duplicates are **not** used — the spans themselves
  carry the letters, and the h1's text content reads whole). Screen
  readers meet the name, not the unfurl. Contrast at the dimmest
  armed state is irrelevant to AT and the state lasts ≤1400ms for
  sighted visitors with the watchdog behind it.
- **Tokens consumed (v2).** `--moonflower`, `--ease-bloom`,
  `--dur-unfurl-letter` (700ms), `--stagger-unfurl` (90ms),
  `--dur-fallback-unfurl` (3400ms).

### 6.8 Hover bloom

- **What & why.** Hovering (or focusing) a flower panel (§6.2)
  expands its petal mask a further ~8% and brightens the flower 6%
  over 400ms; leaving lets it settle back over 800ms. It belongs
  because attention is moonlight in this theme's physics: the flower
  responds to being looked at the way the real ones respond to the
  moon — by opening a little more. It is the theme's signature
  micro-interaction, and its asymmetry (400ms open, 800ms settle) is
  the point: opening is eagerness, closing is reluctance.
- **Structure.** The panel's `--petal` property (§6.2) gains a
  `--petal-hover` offset written by pointer/focus handlers through
  the shared loop (never direct style writes from events); the mask
  scale = `--petal` × (1 + 0.08 × hover-progress), brightness =
  base × (1 + 0.06 × hover-progress), hover-progress lerped at 0.18
  so the response has the plant's slight delay — instant response
  would read as a button, not a flower.
- **Motion spec.** Trigger: pointerenter / focusin on an open panel.
  In: 400ms `--ease-bloom` to +8% mask, +6% brightness. Out: 800ms
  `--ease-rise` back to rest. A panel still mid-opening (§6.2) does
  not take hover bloom until it has opened — the bloom completes
  first, then attention may add its 8%.
- **States.** Rest (open, no offset) → blooming (hover/focus) →
  settling (pointer left) → rest. *Active:* n/a. *Scrolled-past:*
  rest. *Disabled:* no offset ever. *Touch:* no hover bloom; a tap
  is a navigation or nothing (§6.2) — the theme refuses to fake a
  hover state on a medium that has no hover.
- **Content merge.** The 8% is not arbitrary: it is the difference
  between the flower as photographed at opening and the same flower
  fully open an hour later — the hover shows the visitor the
  flower's *next* state, the one the programme's later hour (§6.12's
  printed time) promises. The caption's opening hour and the hover's
  extra opening are the same fact at two scales.
- **Failure fallback.** If the loop is stalled, hover-progress never
  writes and the panel simply rests open — the failure mode is a
  still flower, which is a complete experience. No watchdog is
  needed because no state of this element can hide content: the
  offset only ever *adds* opening beyond the fully-open rest state.
- **Reduced-motion variant.** No mask expansion; a 6% brightness
  step applies instantly on hover/focus (a state change, not a
  motion), and the focus ring carries the interaction for keyboard
  visitors.
- **Performance budget & mobile variant.** One lerped value per
  hovered panel; the mask is the shared SVG (§6.2). Mobile/touch:
  element absent (see States); nothing is budgeted for it below
  768px or on coarse pointers.
- **Choreography timeline (v2).** Pointer enters → 60ms intent delay
  (a passing pointer does not stir the garden) → t=60–460 mask
  +8%, brightness +6% → hold while attended → pointer leaves →
  t=0–800 settle to rest. Focus follows the same beats without the
  intent delay — a keyboard's arrival is never a passing glance.
- **State matrix (v2).** *Rest:* open, no offset. *Hover:* +8%/+6%
  as above. *Focus:* identical to hover, no intent delay.
  *Active:* n/a. *Scrolled-past:* rest. *Disabled:* rest.
  *Touch:* rest; taps navigate if linked.
- **Breakpoints (v2).** ≥1200px and 768–1199px: full behaviour on
  pointer-fine devices. <768px or pointer-coarse at any size:
  absent.
- **Edge cases & failure modes (v2).** *Pointer skims a row of
  panels:* the 60ms intent delay + lerp means a skim stirs nothing
  visibly — deliberate; a garden that flinches at every passer-by is
  a toy shop. *Panel leaves viewport while hovered (scroll):*
  hover-progress decays to 0 with the settle curve; no stuck bloom.
  *Focus moves panel-to-panel by keyboard:* each focus gets the full
  bloom without delay; the previous panel settles behind — the
  garden attends to one visitor at a time.
- **Accessibility spec (v2).** Focus parity is exact (same values,
  faster trigger). The bloom is decorative emphasis on an already
  legible panel; nothing is revealed by hover that is not in the
  caption. Focus ring: 2px `--silver-pale` outline, offset 3px,
  visible against both grounds (10.34:1 / 8.01:1).
- **Tokens consumed (v2).** `--petal`, `--ease-bloom`, `--ease-rise`,
  `--dur-bloom-in` (400ms), `--dur-bloom-out` (800ms),
  `--lerp-attention` (0.18).

### 6.9 Pollen puff click

- **What & why.** Clicking a venue/programme card (§6.13) releases
  10–14 pale pollen motes from the click point that drift up and
  outward and fade over ~1200ms. It belongs because the card sheds
  the garden's own material as its feedback: the visitor touched a
  plant, and the plant answered in pollen. It is the theme's only
  particle effect, rationed to clicks — pollen is spent on a
  decision, never ambient (§5's ambient census does not include it,
  because it is not ambient; it is a receipt).
- **Structure.** A per-page mote layer (one fixed, `pointer-events:
  none`, `aria-hidden` canvas-free DOM layer of ≤14 reusable mote
  divs, 3–5px, `--moonflower` at 70% → 0 opacity, slight `--moth`
  tint on every third mote). Motes are pooled and reused; a click
  while a previous puff is mid-flight reuses the pool from the new
  point — motes are never accumulated beyond 14 live at once.
- **Motion spec.** Trigger: click/activation on a §6.13 card (and
  only there — buttons and links keep their own grammar; a page
  that puffs pollen from every control is a sneeze, §9.9). Each
  mote: initial velocity outward-up biased (pollen rises on night
  air), travel 40–90px over 1200ms `--ease-drift` with a 200ms
  `--ease-settle` release at birth, opacity 0.7 → 0 across the last
  60% of life. Physics is authored per-mote from a seeded spread —
  same click point, same puff shape family, never a firework burst
  (radially uniform = firework; upward-biased = pollen).
- **States.** Idle (pool empty) → puffing (≤1200ms) → idle.
  *Hover:* none. *Focus:* keyboard activation of a card triggers
  the puff from the card's centre — the receipt is not
  pointer-only. *Disabled:* no puff; the card's navigation still
  happens.
- **Content merge.** The motes come from the card's flower: a card
  whose photograph is the jasmine sheds from the jasmine's position
  on the card (the click point, which is on the plant the visitor
  touched). The count (10–14) is the original entry's figure, kept;
  the colour is the pictured flower's pollen colour family
  (moonflower-white family for all the garden's pale bloomers).
- **Failure fallback.** If the mote layer fails to initialise, clicks
  simply navigate — the puff is a receipt, not a confirmation, and
  no state depends on it. The card's own pressed state (§6.13)
  carries the feedback alone, completely.
- **Reduced-motion variant.** No motes. The card's pressed state and
  a one-line confirmation in the card ("Added to your evening" where
  the card is a booking action) carry the feedback in words.
- **Performance budget & mobile variant.** ≤14 tiny divs, transforms
  + opacity only, pooled; zero allocation per click after pool
  creation. Mobile: identical (taps are clicks here), mote count
  8–10, travel 30–60px — a smaller garden shed.
- **Choreography timeline (v2).** Click → t=0 card press begins
  (§6.13) → t=80 motes release (the press lands first; the plant
  answers the touch, not the approach) → t=80–280 release ease →
  t=280–1280 drift and fade → t=1280 pool idle. Navigation (if the
  card links) begins at t=150 under the puff, so the puff is seen
  against the card, not against the destination page.
- **State matrix (v2).** *Rest:* no motes. *Hover:* none. *Focus:*
  no puff until activation. *Active (click/Enter/Space):* puff as
  above. *Scrolled-past:* n/a. *Disabled:* no puff, navigation
  intact. *Touch:* tap = click, same beats.
- **Breakpoints (v2).** All sizes: behaviour identical; counts and
  travel scale per budget above at <768px.
- **Edge cases & failure modes (v2).** *Rapid repeat clicks:* pool
  caps at 14 live motes; extra clicks restart the oldest motes from
  the new point — the garden sheds what it has. *Click near
  viewport edge:* motes clamp inside the viewport (pollen does not
  leave the garden through a wall). *Card inside the pinned bed:*
  motes render in the stage's air layer, above the ground, below
  the moths' dignity — z-order under §6.3's layer.
- **Accessibility spec (v2).** `aria-hidden`, no focus, no
  information. The action the puff receipts is announced by the
  card's own semantics (link text, or the confirmation line in the
  reduced-motion variant which is also present visually for all
  users on booking cards).
- **Tokens consumed (v2).** `--moonflower`, `--moth`, `--ease-drift`,
  `--ease-settle`, `--dur-pollen` (1200ms), `--mote-max` (14).

### 6.10 First-light footer

- **What & why.** The footer is a `--firstlight` band — a barely
  warmer horizon (`#232A38` → `#3A3230` at its baseline in the
  original entry's terms; the shipped token is `--firstlight`
  itself) — that warms by a further few percent as it centres, while
  the progress moon (§6.5) sets below its top edge. It belongs
  because the page must end the way the night does: not with a
  boilerplate block but with dawn arriving at the bottom of the
  evening. The footer is the night's conclusion, and its contents —
  the evening's record (§6.14's figures, restated), the sky rule
  (`phaseOn`, printed in full), the gate times — are the logbook of
  the visit just made.
- **Structure.** A `<footer>` bed on `--firstlight`, excluded from
  the `nightAt` axis (§6.4): instead of a leaf→soil interpolation it
  carries a warmth property `--warm` (0 → 1) driven by the loop as
  the band crosses the viewport's lower half. Contents: the horizon
  rule (1px `--moonflower` at 18%) along its top edge — the line the
  moon sets below; the evening's record table (beds visited by
  fragrance number, the full-moon time, the counts from §6.14);
  the printed `phaseOn` formula and epoch; gate hours (19:40 –
  00:00, from `eveningTime`'s endpoints); the closing line in
  Cormorant italic (§3, law 1's third licensed use): the garden's
  goodnight.
- **Motion spec.** Trigger: scroll scrub. `--warm` 0 → 1 across the
  band's travel through the viewport's lower 60%, lerped 0.10; the
  ground warms from `--firstlight` toward a 6%-warmer mix (toward
  `#463C34` — a derived endpoint declared here, used nowhere else).
  The moon: as `p` passes 0.97, §6.5 hands custody to the footer;
  the disc translates down 34px and fades to 0 across the band's
  first 30vh of entry — it sets *into* the horizon rule. Both are
  one-way in effect: scrolling back up un-warms and un-sets
  symmetrically (dawn, like dusk, is scrubbed; only the phase was
  latched, §6.5).
- **States.** Approaching (moon full, band cool) → warming →
  dawned (moon set, record printed). *Hover:* the record table's
  rows take the standard text-hover (§11). *Focus:* links standard.
  *Disabled:* band at full warmth, moon shown already set (absent),
  record printed — the finished state.
- **Content merge.** The record table is generated from the same
  sources as everything it restates: bed list from the §6.12 bed
  map, counts from §6.14's data object, the full-moon time from
  `eveningTime(0.97)`. A footer figure that disagrees with its
  source anywhere above it is §10's three-printings failure. The
  printed sky rule is not decoration: it is the formula §6.15's
  confirmations are computed by, published where a visitor can
  check tonight's promised phase against the sky.
- **Failure fallback.** No JS: band ships at full warmth, no moon
  (it has set — the honest finished state), record printed from the
  build-time bed map and counts. Nothing in the footer is
  JS-dependent for its facts.
- **Reduced-motion variant.** Band at full warmth from first paint;
  no moon in the footer (set already); record printed. The dawn is
  a state in this edition, not an event.
- **Performance budget & mobile variant.** One background
  interpolation + one disc transform, inside the loop. Mobile: the
  record table stacks to a definition list; the moon's set is cut
  (the header moon, §6.11, simply leaves at the footer boundary) —
  the dawn survives as warmth + record, which are its substance.
- **Choreography timeline (v2).** Footer top enters viewport →
  moon begins its 34px descent → band warms across its lower-half
  travel → moon crosses the horizon rule and is gone at band-entry
  +30vh → record rows fade in as one block (600ms `--ease-rise`,
  no stagger — a logbook opens, it does not perform) → the closing
  italic line is the last thing to reach full brightness.
- **State matrix (v2).** *Rest:* per scroll position (cool →
  dawned). *Hover:* table rows standard. *Focus:* standard links,
  ring `--moonflower`. *Active:* n/a. *Scrolled-past:* n/a (it is
  the end). *Disabled / no-JS:* dawned state. *Touch:* identical;
  no pin or hover dependence.
- **Breakpoints (v2).** ≥1200px: record as a 3-column table.
  768–1199px: 2 columns. <768px: definition list; moon-set cut (see
  budget).
- **Edge cases & failure modes (v2).** *Anchor jump straight to
  footer:* moon arrives already set (its `p`-positional state),
  band at the warmth for its position — positional functions do not
  need the journey to have happened. *Short page:* the footer may
  be visible at load; it ships dawned in that case, correctly — a
  one-bed evening is all dawn. *The record's counts vs. §6.14:* one
  data object (§6.14); a disagreement is impossible by construction
  and audited anyway (§10).
- **Accessibility spec (v2).** Footer text is `--moonflower` on
  `--firstlight` (10.94:1) at every warmth value — the warm endpoint
  `#463C34` is checked too (9.38:1, computed for this expansion).
  The setting moon is `aria-hidden`; the record is a real `<table>`
  with a caption naming it as the evening's record.
- **Tokens consumed (v2).** `--firstlight`, `--moonflower`,
  `--silver`, `--warm`, `--ease-rise`, `--lerp-night` (0.10).

### 6.11 Vine-rail navigation (page family: navigation)

- **What & why.** The page's navigation lives in the margin rail,
  grown along the vine (§6.6): each bed is a link at its flower,
  named with its fragrance number and title, the current bed's
  flower open and its name at full opacity. It belongs because a
  garden's index is a path, not a menu bar: the visitor is *in* the
  garden, and the rail shows where along it they stand. A top
  navigation bar is refused on the home page (interior pages keep a
  slim gate bar — §7); the rail is the navigation, the progress
  instrument and the index in one drawing.
- **Structure.** A `<nav>` in the rail containing an ordered list in
  bed order: each item a link with `№ n`, the bed name, and its
  flower (from §6.6's SVG, the link and the flower are the same
  element's parts). The current item carries `aria-current="true"`,
  written by the loop from the same bed-window computation §6.4
  uses — one source for "which bed am I in" across ground, vine and
  nav. Below the list: the gate link ("Plan a visit" → §6.15) set
  as a pressed flower — a bordered label, the rail's only box.
- **Motion spec.** Current-bed changes crossfade the names' opacity
  (70% → 100%) over 300ms `--ease-drift`; the flower at the newly
  current bed blooms (§6.6's 600ms) if it has not yet. No sliding
  indicators, no animated underlines — a path does not have a
  sliding indicator; the flower is the indicator. Navigation clicks
  run the cloud transition (§6.16) for page changes, or a smooth
  scroll (900ms, loop-driven) for same-page bed anchors.
- **States.** Per link: upcoming (name 70%, flower closed) → current
  (name 100%, flower open, `aria-current`) → visited (name 85%,
  flower open). *Hover:* name to 100% + flower brightens. *Focus:*
  as hover, plus the §6.6 focus-opens rule. *Active:* §6.6's pulse.
  *Disabled:* a bed not yet planted (a programme page for a future
  month) renders as text without a link, flower drawn as a bud —
  the rail admits the season hasn't reached it.
- **Content merge.** The rail's order, numbers and names are the
  bed map itself (§6.12 generates all three from one source); the
  nav cannot drift from the page it indexes because it is drawn
  from the same declarations. The gate link's label carries the
  real gate time ("Plan a visit — gates 19:40") from
  `eveningTime(0)`.
- **Failure fallback.** No JS: all names at full opacity, flowers
  open, links plain anchors — a static index beside a drawn vine.
  The current-bed indication is an enhancement; the list loses
  nothing structural without it.
- **Reduced-motion variant.** Names at full opacity; current bed
  indicated by `aria-current` + a `--moth` fragrance number (the
  number carries the state in data, not in motion).
- **Performance budget & mobile variant.** Opacity writes only on
  bed change (rare), inside the loop's frame. Mobile: the rail is
  gone (§4); navigation becomes the sticky header — the 28px phase
  moon (§6.5), the garden name, and a "Beds" disclosure listing the
  same links in the same order. The index survives the rail's loss;
  the vine does not pretend to fit a phone.
- **Choreography timeline (v2).** On bed change: t=0 previous name
  begins fading to 85% (visited) → t=0–300 new name to 100% → its
  flower blooms t=100–700 → `aria-current` moves at t=0 (state is
  instant for AT; only the paint is gradual). On gate-link click:
  §6.16's cloud takes the page.
- **State matrix (v2).** *Rest:* per position (above). *Hover:*
  name 100%, flower brightens 10%. *Focus:* as hover + focus-opens
  + ring. *Active:* pulse (§6.6). *Scrolled-past:* visited state.
  *Disabled:* bud rendering, no link. *Touch:* tap navigates; the
  current state is the only feedback before the transition.
- **Breakpoints (v2).** ≥1200px: full rail nav. 768–1199px: numbers
  + abbreviated names (full name on hover/focus, and always in the
  bed head itself, §6.12). <768px: header disclosure (see budget).
- **Edge cases & failure modes (v2).** *Bed added/removed:* the nav
  regenerates from the bed map; a nav item without a bed (or a bed
  without an item) fails §10's census. *Deep-link to a late bed:*
  states resolve positionally — earlier beds show visited, flowers
  open, without playing their blooms.
- **Accessibility spec (v2).** A real `<nav>` with an ordered list;
  link text is the bed's full name + number at every breakpoint
  (abbreviation is visual only, via CSS clipping with the full text
  in the accessible name). `aria-current` on exactly one item.
  Targets ≥44px tall in the rail (the rail is 72px wide; rows are
  48px).
- **Tokens consumed (v2).** `--silver`, `--silver-pale`, `--moth`,
  `--ease-drift`, `--dur-nav-fade` (300ms).

### 6.12 Fragrance-numbered section heads (page family: section furniture)

- **What & why.** Every bed opens with the same furniture: its
  fragrance number (`№ 3`), its scent note ("jasmine, after rain"),
  its printed programme time (from `eveningTime` at the bed's
  centre), and its headline. It belongs because the scent note is
  the theme's founding confidence — the original entry's anti-slop
  detail, promoted here to a system: every section is labelled with
  what it would smell like, in the same type, in the same place,
  with a number that is counted and a time that is computed. The
  furniture is the page's honesty made visible at every bed.
- **Structure.** A `<header>` per bed: the number and time in the §3
  data style on one line (number left, time right, a hairline
  `--silver` rule at 24% between the bed's path edge and the pair),
  the headline in Cormorant, the scent note in Alegreya Sans italic
  directly beneath it, prefixed by an em dash in `--moth`. Numbers
  are assigned by DOM order at build; the time is written by the
  formatter from the bed's declared centre `p`.
- **Motion spec.** The head is the one piece of furniture that does
  **not** bloom: it prints. On the bed's first entry, the hairline
  rule draws left→right over 500ms `--ease-draw` and the number +
  time crossfade from 60% to 100% (300ms) — a label being pinned to
  a bed, nothing more. Everything else about the head is stillness;
  a page whose every label performs has no labels, only acts.
- **States.** Unpinned (pre-entry, JS-armed: rule undrawn, data at
  60%) → pinned (terminal). *Hover:* none. *Focus:* none (the head
  contains no controls). *Scrolled-past:* pinned. *Disabled:*
  printed complete.
- **Content merge.** The scent note must name a planting in the bed
  below it: "jasmine, after rain" heads the bed whose panels
  (§6.2) are jasmine. A note that describes nothing in its bed is
  §9.10's failure — scent as wallpaper. The note's second half
  ("after rain", "on warm stone", "at first dark") is the
  condition, and the bed's copy must honour it (the after-rain bed
  is the one after the tea bed in the programme's logic — editorial,
  checked in §15's copy pass).
- **Failure fallback.** No JS: rule drawn, data at full opacity —
  the head ships complete; JS arms the undrawn state only for beds
  below the fold. Watchdog: 1200ms after a bed's entry by any path,
  its head is pinned regardless of the draw's state.
- **Reduced-motion variant.** Heads print complete; no draw, no
  fade. The furniture is information in this edition.
- **Performance budget & mobile variant.** One rule draw per bed,
  once. Mobile: number and time stack (number above time, both
  left-aligned) — the pair is a label, not a table row, on a narrow
  path.
- **Choreography timeline (v2).** Bed top crosses the 78% line →
  t=0 rule begins drawing → t=0–300 number/time to full → t=500 rule
  complete → head at rest, forever. The bed's first panel (§6.2)
  may begin its bloom at t=300 — label first, flower second, in the
  garden's own order.
- **State matrix (v2).** *Rest:* pinned, complete. *Hover:* none.
  *Focus:* none. *Active:* n/a. *Scrolled-past:* pinned.
  *Disabled / no-JS:* complete. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px and 768–1199px: number/time on one
  line. <768px: stacked (see budget). Type sizes hold; the data
  style never drops below 12px.
- **Edge cases & failure modes (v2).** *A bed with no scent
  (the gate, the booking bed):* the note reads the planting that is
  there — "cut grass, cooling" for the gate lawn, "paper, lamp oil"
  is refused (a form does not smell of lamp oil; the booking bed's
  honest note is "night air, through the gate"). A bed may not omit
  the note; §10's census counts notes against beds. *Renumbered
  beds after a CMS edit:* numbers are DOM-derived, so the census
  re-runs clean or fails loudly — never silently wrong.
- **Accessibility spec (v2).** The number + note + time are plain
  text in reading order before the headline's bed content; the
  `№` is read as "number" by the accessible name ("Number 3,
  jasmine, after rain, 21:10"). The hairline is decorative.
  Contrast: data style in `--silver` on either ground passes AA
  (6.54:1 / 5.06:1).
- **Tokens consumed (v2).** `--silver`, `--moth`, `--ease-draw`,
  `--dur-rule-draw` (500ms).

### 6.13 Venue cards — leaves turning (page family: cards / listing)

- **What & why.** Programme and venue cards (an evening tour, a
  tasting, a bed's open hours) tilt like leaves turning toward
  moonlight — max 3°, toward the pointer, with their shadow
  lengthening on the side away from the light. It belongs because a
  card on this page is a leaf on the planting it describes: it
  answers attention by turning, the way the bed's leaves turn. The
  3° cap is the original entry's figure and it is a cap, not a
  starting point — a card that tilts 10° is a toy, and §9 names it.
- **Structure.** Cards are `<article>` elements on `--bed` (in soil
  beds) or `--leaf` (in leaf beds), each with a photograph (petal
  grammar does not apply — cards are leaves, not flowers; their
  images use §6.2's brightness only), a Cormorant title, the facts
  in data style (time from `eveningTime`, places remaining as a
  count from the booking data), and one action. Tilt is a transform
  on the card driven by the loop from pointer position within the
  card, lerped at 0.18 (§6.8's attention lerp — one attention
  physics for the whole page).
- **Motion spec.** Trigger: pointermove over the card (pointer-fine
  only). Tilt: rotateX/rotateY toward the pointer, max 3° on either
  axis, shadow offset counter-moving ≤6px; return on leave over
  600ms `--ease-rise` (a leaf settles slower than it turns).
  Click/activation: the card presses 1px (`--ease-settle`, 120ms)
  and sheds its pollen (§6.9) before navigating or confirming.
- **States.** Rest (flat) → turning (pointer over) → settling →
  rest. *Focus:* a focused card tilts a fixed 1.5° toward the
  page's moon side (top-right) — keyboard attention gets the leaf's
  answer without a pointer to aim it. *Active:* press (above).
  *Scrolled-past:* rest. *Disabled:* a sold-out evening's card does
  not tilt, does not puff, and prints "The bed is full" in the
  Gate's voice (§12) — a full evening is a fact, not a grey button.
- **Content merge.** The tilt's light source is the page's moon:
  cards turn toward the *rail side* (the moon's side), not
  arbitrarily toward the pointer's quadrant — pointer position
  modulates the amount (0–3°), the direction's bias is always
  moonward. The card is a leaf in a garden lit from one side (§1's
  law, at card scale).
- **Failure fallback.** No JS / loop stall: cards are flat, fully
  legible, fully clickable. The tilt carries nothing.
- **Reduced-motion variant.** No tilt. Hover/focus raise the card's
  photograph brightness 6% instantly (state, not motion), focus ring
  standard.
- **Performance budget & mobile variant.** One transform per hovered
  card; shadows are a single static-spread `box-shadow` whose offset
  is the only animated part. Touch/coarse pointers: no tilt (a tap
  is a press + puff, §6.9). Cards stack single-column <768px.
- **Choreography timeline (v2).** Pointer enters → tilt begins
  within one frame, lerping to the pointer's value (reached in
  ~250ms of steady pointer) → pointer moves: tilt follows at the
  0.18 lerp, always a beat behind the hand, like a leaf in air →
  pointer leaves → 600ms settle to flat → click at any point: press
  (120ms) → pollen (t=80, §6.9) → navigation at t=150.
- **State matrix (v2).** *Rest:* flat. *Hover:* tilt ≤3° moonward,
  shadow counter-moved. *Focus:* fixed 1.5° moonward tilt.
  *Active:* 1px press + pollen. *Scrolled-past:* rest.
  *Disabled (full):* flat, no puff, fact printed. *Touch:* press +
  puff only.
- **Breakpoints (v2).** ≥1200px: cards in rows of 3 within a bed.
  768–1199px: rows of 2. <768px: single column, tilt absent.
- **Edge cases & failure modes (v2).** *Pointer at card corner:*
  tilt clamps at 3° per axis — the clamp is in the value function,
  not in a CSS hope. *Card taller than wide (portrait programme
  cards):* rotateX cap halves to 1.5° (a tall leaf tips, it does
  not fold). *Rapid card-to-card pointer travel:* each card's tilt
  is independent; the settle of the last card overlaps the turn of
  the next without jank because both run in the one loop.
- **Accessibility spec (v2).** The whole card is **not** one giant
  link: the action is a real link/button with a 44px target, the
  title is text, the facts are text. Tilt never moves the target by
  more than the 3° geometry (≤4px at the corner) and never during
  focus. Focus ring `--silver-pale`, offset 3px.
- **Tokens consumed (v2).** `--bed`, `--leaf`, `--silver-pale`,
  `--ease-rise`, `--ease-settle`, `--tilt-max` (3deg),
  `--lerp-attention` (0.18).

### 6.14 Bloom counters & the evening's figures (page family: data / counters)

- **What & why.** The evening's numbers — flowers open tonight,
  moths recorded this season, evenings remaining — count up once
  when their bed enters, over 1600ms, from the value's own lower
  neighbour to the true figure. It belongs because a garden keeps
  records, and the counting is the record being read aloud once.
  Every figure traces to one `GARDEN` data object (the planting
  record): the bloom total is the sum of the beds' planted counts,
  which are printed on the beds themselves — three printings of one
  record (beds, figures band, footer, §6.10), and a disagreement
  between any two is a gate failure, not a rounding choice.
- **Structure.** A figures band inside the records bed: each figure
  is a `<dl>` pair — term in the §3 data style ("FLOWERS OPEN
  TONIGHT"), value in Alegreya Sans 700 tabular at 34px, and a
  source line in caption size naming where the number comes from
  ("counted from the beds, № 1–7"). The source line is mandatory:
  a figure without a stated source does not ship (§9.11). Values
  are written by the formatter from the `GARDEN` object; the HTML
  ships the true values (see fallback).
- **Motion spec.** Trigger: the band's centre crossing the viewport
  centre, once. Count: 1600ms `--ease-drift` (an even count — the
  drift easing, because a count is a walk through the numbers, not
  a bloom), from `max(0, value − 12% of value)` rounded down to the
  formatter's precision, upward only, landing exactly on the true
  figure and stopping. Figures stagger 120ms in DOM order. A figure
  of 0 counts from 0 to 0 — it prints, honestly still.
- **States.** Uncounted (JS-armed: at the start value) → counting →
  counted (terminal; scroll-up never recounts or uncounts — the
  record, once read, stays read). *Hover:* none. *Focus:* none.
  *Disabled:* true values printed.
- **Content merge.** The figures are the garden's own census, and
  their terms are the garden's own categories: flowers open
  (tonight, from the beds), moths recorded (this season, from the
  pollinator bed's log), evenings left (in the season, from the
  programme calendar). A build that counts "happy visitors" or
  "five-star reviews" has imported a dashboard into a garden —
  §9.11 names it. If the venue does not keep a count, the figure
  does not appear; the band may ship with two figures.
- **Failure fallback.** No JS: true values in the HTML. Watchdog:
  2200ms after trigger, any figure not landed is set to its true
  value instantly. The count is a reading-aloud; the record itself
  is never behind the animation.
- **Reduced-motion variant.** True values, printed. No count.
- **Performance budget & mobile variant.** ≤5 figures, one text
  write per figure per frame during 1600ms. Mobile: figures stack
  2-per-row; count duration 1200ms (a shorter walk for a smaller
  garden view).
- **Choreography timeline (v2).** Band centre crosses → t=0 first
  figure begins → t=120ms, 240… siblings begin → each lands at its
  own t=1600+offset and stops dead (no overshoot — a count that
  overshoots its true value has lied, briefly, in public) → band
  at rest with the record read.
- **State matrix (v2).** *Rest:* true values. *Hover:* none.
  *Focus:* none. *Active:* n/a. *Scrolled-past:* counted, true.
  *Disabled / no-JS:* true values. *Touch:* same trigger and count.
- **Breakpoints (v2).** ≥1200px: figures in one row (≤5).
  768–1199px: one row, 28px values. <768px: 2-per-row grid, 26px
  values.
- **Edge cases & failure modes (v2).** *Figure updates between
  visits (a flower count changes with the season):* the `GARDEN`
  object is build/CMS data; beds, band and footer read the same
  object, so an update propagates to all three printings or the
  build fails its own census (§10). *Very large counts:* formatted
  with the locale's grouping (12,400), counted in the same grouped
  format at every frame — a digit-width change mid-count is a
  formatter bug, caught by the tabular rule (§3, data style).
- **Accessibility spec (v2).** The counting span is `aria-hidden`;
  a visually-hidden sibling carries the true value from the start,
  so AT never hears a number that is on its way somewhere. The
  source line is real text, associated by proximity in the `<dl>`.
- **Tokens consumed (v2).** `--silver`, `--moonflower`, `--moth`
  (source line's dash), `--ease-drift`, `--dur-count` (1600ms),
  `--dur-fallback-count` (2200ms).

### 6.15 The evening booking form (page family: forms / conversion)

- **What & why.** The conversion bed: booking a night visit — date,
  party size, names, the gate it is. Its signature act is the
  confirmation: when a date is chosen, the form states the moon
  that evening will actually have, computed by `phaseOn(date)` (§4)
  — "Saturday 14 June — the moon will be waxing gibbous, 78% lit"
  — because a moon garden's booking form can answer the one question
  its visitors are really asking. It belongs because the form is
  where the theme's arithmetic becomes a promise to a specific
  person about a specific night, and the promise is checkable
  against the sky.
- **Structure.** A `<form>` on `--bed` in the booking bed (which
  sits late in the page at `--leaf`-ward stops — people book in the
  light there is). Fields in bed order: date (native date input,
  styled), party size (stepper, 1–12), name, email, and the evening
  choice (radio list of that date's programme items, from the
  programme data). The phase line lives under the date field as a
  live region's visual twin: it updates on date change. Submit is
  "Book the evening". Errors are margin notes in the Gate's voice
  (§12) beside the field, in `--silver-pale` with a `--moth`
  hairline — never red; there is no red in this garden.
- **Motion spec.** Field focus: the field's underline draws
  left→right 260ms `--ease-draw` in `--silver-pale` (the dive-line
  grammar of a label being pinned, §6.12). Phase line: on date
  change, the old line fades 150ms, the new line's moon glyph
  (a 20px phase disc rendered by the same 24-step geometry as
  §6.5) draws 400ms `--ease-draw`, text crossfades in. Submit: the
  button presses (§11 grammar), then the form is replaced by the
  confirmation over a 600ms `--ease-rise` rise — the confirmation
  is a card (§6.13's shape) carrying the booking's facts and the
  phase line, restated as a promise: "…and the moon, waxing
  gibbous, will be up by 21:10" — the rise time also from
  `phaseOn`'s age (declared approximation: moonrise ≈ 06:00 +
  age × 50 min, modulo the day, printed in the footer beside the
  formula, §6.10 — an approximation that labels itself).
- **States.** Per field: rest / focused (underline drawn) / filled
  (underline rests at 40%) / error (margin note shown, underline in
  `--moth`). Form: editing → submitting (button disabled, label
  "Booking…", 700ms simulated minimum so the state is readable) →
  confirmed (form replaced; the confirmation carries a "Change the
  booking" link that restores the form with values kept). *Disabled
  submit:* never pre-disabled — the form explains itself on submit
  rather than refusing in advance (§12's error voice).
- **Content merge.** The phase promise is the theme's whole argument
  in one line: the garden sells nights, and the form tells you
  which night you are buying — moon, programme, gate time — all
  three from the declared functions and data, none from copywriting.
  A build that drops the phase line to save space has removed the
  reason the form is in this theme at all; §14's cut order protects
  it explicitly.
- **Failure fallback.** No JS: the form is a working native form;
  the phase line is absent (not faked — a static line prints
  instead: "The moon's phase for your date is worked out in the
  confirmation letter", which the server's letter then honours).
  Validation errors are server-renderable in the same margin-note
  pattern. Nothing about booking depends on the animation layer.
- **Reduced-motion variant.** Underline applies instantly; phase
  line swaps without fades; confirmation replaces the form
  instantly. All facts identical.
- **Performance budget & mobile variant.** The phase computation is
  arithmetic (<1ms). Mobile: single column, the phase line moves
  above the date field's hint (it is the field's point), stepper
  targets 48px.
- **Choreography timeline (v2).** Date chosen → t=0 old phase line
  fades (150ms) → t=100 new disc draws (400ms) → t=300 text lands →
  line at rest. Submit → press (120ms) → "Booking…" (≥700ms) →
  form fades 200ms → confirmation rises 600ms `--ease-rise` → its
  phase disc is already drawn (the promise does not re-perform).
- **State matrix (v2).** *Rest:* fields quiet, phase line showing
  the default date (the next open evening, from the programme data
  — never today by assumption; a garden closed tonight says so).
  *Hover:* fields take a 1px `--silver` border lift. *Focus:*
  underline draw + label to `--moonflower`. *Active:* button press.
  *Scrolled-past:* n/a. *Disabled:* the date field disables closed
  dates natively (min/max + programme data); a date with no evening
  is selectable in no way and the calendar says why in the hint.
  *Touch:* native pickers; phase line updates on change, same beats.
- **Breakpoints (v2).** ≥1200px: two-column fields (date+party,
  name+email), programme radios full width. 768–1199px: two-column
  for the short fields only. <768px: single column.
- **Edge cases & failure modes (v2).** *A date beyond the season:*
  the hint states the season's last evening (from data) and the
  phase line offers it ("The last evening is 28 September — nearly
  full"). *Party of 12+:* the form routes to the Gate's group line
  in copy, not a bigger number — the stepper caps at 12 and says
  why. *Double submit:* the submitting state is a real disabled
  state after first activation; the confirmation is idempotent.
  *Phase at the extremes:* a new-moon date prints the fact without
  apology — "the moon will be new; the garden is at its darkest,
  and the stock is at its sweetest" (§12's owned line) — the theme
  never talks a visitor out of a dark night.
- **Accessibility spec (v2).** Labels always visible above fields;
  errors are text beside the field, linked by `aria-describedby`,
  focus moves to the first error on failed submit. The phase line
  is a polite live region (it changes on the user's own input, and
  its text — never the glyph alone — is the announcement). Targets
  ≥44px; focus ring `--silver-pale` offset 2px on the `--bed`
  ground (10.34:1 family contrast).
- **Tokens consumed (v2).** `--bed`, `--silver`, `--silver-pale`,
  `--moth`, `--moonflower`, `--ease-draw`, `--ease-rise`,
  `--dur-field-rule` (260ms).

### 6.16 Night-soil skeleton & the cloud-pass transition (page family: loader / transition)

- **What & why.** Loading wears the garden's own dark: skeleton beds
  in `--soil` with a faint silver shimmer passing unevenly, and page
  transitions pass a cloud across the moon — the page dims, swaps,
  and re-brightens. It belongs because the moon is the page's light
  source (§1), so a change of page is weather moving across that
  light; and a loading state in a bright grey would be daylight
  leaking into the night. The skeleton is a bed not yet planted, drawn
  in the bed's own ground.
- **Structure.** Skeleton: the incoming page's bed structure rendered
  as `--leaf` blocks on `--soil` (headline bar at the Cormorant
  measure, text bars, a panel plate where a flower will be), with
  the shimmer as a `--silver` gradient at 8% travelling the blocks
  (§6.17's grain grammar at load scale). Transition: a full-viewport
  overlay in `--soil` at variable opacity + the rail moon (§6.5)
  dimmed behind a soft-edged cloud disc (a blurred `--soil` circle
  crossing the moon's position) — in practice the overlay's dim is
  the cloud; the disc is drawn only in the rail, where the moon is.
- **Motion spec.** Skeleton shimmer: one pass per 2400ms, uneven
  (the pass eases in patches — two gradient stops at different
  speeds, §6.17's unevenness rule), only while content is genuinely
  pending. Transition (internal navigation): dim to 40% brightness
  over 600ms `--ease-drift` → swap at full dim → re-brighten over
  900ms `--ease-rise`. A navigation that resolves before the dim
  completes skips the swap beat and re-brightens from wherever it
  reached — the cloud does not hold a finished page hostage.
  Watchdog: 3000ms at full dim forces the swap-or-abort.
- **States.** Idle → dimming → swapped → brightening → idle.
  Skeleton: pending → resolving (blocks replaced bed by bed in DOM
  order, 150ms stagger — the garden is planted bed by bed, not
  unveiled). *Disabled:* instant swaps, no skeleton (content renders
  server-side wherever possible; the skeleton is for genuinely
  client-fetched beds only).
- **Content merge.** The skeleton's blocks are the real beds'
  silhouettes (same heights from the bed map), so the page does not
  reflow as it plants — the shimmer walks the exact ground the
  content will occupy. The cloud transition's moon is the rail moon,
  not a second moon (§1's law survives navigation).
- **Failure fallback.** If the transition layer fails, navigation is
  instant and unadorned. If a fetch fails under a skeleton, the bed
  resolves to its error state in the Gate's voice (§12) inside the
  same silhouette — a bed that could not be planted says so, in
  place, without collapsing the page's shape.
- **Reduced-motion variant.** No shimmer (static `--leaf` blocks),
  no cloud (instant navigation). Loading is still night-soil — the
  colours are the theme; only the weather is cut.
- **Performance budget & mobile variant.** The overlay is one
  opacity/brightness animation on a composited layer. Mobile:
  identical; the rail-moon cloud disc is drawn in the header (§6.11)
  instead.
- **Choreography timeline (v2).** Click → t=0 dim begins → t=600
  full dim, swap → t=600–1500 re-brighten → destination's own
  entrances (its §6.12 head pin, any §6.2 blooms) begin only after
  t=1500 — the new page's evening starts once the cloud has passed.
  Skeleton: bed resolves → its blocks fade 200ms as the real bed
  paints beneath → next bed at +150ms.
- **State matrix (v2).** *Rest:* no overlay. *Hover:* none.
  *Focus:* focus is moved to the destination's `<h1>` (or bed head)
  at the swap beat, never left on a removed element. *Active:* the
  triggering link's press precedes the dim by its own 120ms.
  *Scrolled-past:* n/a. *Disabled / no-JS:* plain navigation.
  *Touch:* identical.
- **Breakpoints (v2).** All sizes: same beats; the cloud disc's home
  follows the moon (rail ≥768px, header <768px).
- **Edge cases & failure modes (v2).** *Modified clicks (new tab,
  middle click):* the transition never intercepts them — native
  behaviour wins, always. *Back/forward:* the cloud plays in
  reverse order (brighten-then-dim reads as the cloud retreating)
  only if the navigation is same-session; a cold back-navigation is
  a plain load. *Prefetch:* hovered rail links prefetch, so most
  clouds pass over an already-planted garden and shorten to the
  brighten beat alone.
- **Accessibility spec (v2).** During the dim, the outgoing page is
  `inert`; the destination is announced by its heading via focus
  (see matrix). The dim never drops text contrast below the §2 law
  for content that remains interactive — and nothing remains
  interactive while dimmed, which is the point of `inert`.
- **Tokens consumed (v2).** `--soil`, `--leaf`, `--silver`,
  `--ease-drift`, `--ease-rise`, `--dur-cloud-dim` (600ms),
  `--dur-cloud-brighten` (900ms).

### 6.17 Silver speckle & grain (page family: ambient layer)

- **What & why.** Two ambient textures, rationed as one element
  because they share a census: silver speckle that twinkles at
  random points like night-scented stock (you smell it in patches,
  never everywhere at once), and a fine silver grain that shimmers
  unevenly across the grounds. They belong because night air in a
  garden is not uniform — scent arrives in drifts and light in
  patches — and *unevenness* is the entire design: a uniform twinkle
  is a starfield screensaver, and §9.3 refuses it by name.
- **Structure.** Speckle: ≤40 points per viewport, generated per bed
  from a seeded layout (positions authored against the bed's foliage
  layer, sizes 1–2px, `--silver-pale`), each with its own twinkle
  period drawn from 2600–5400ms and its own phase — no two points
  share a period, so synchrony is impossible by construction. Grain:
  two SVG-turbulence layers at different scales (180px and 420px
  tiles), `--silver` at 4% and 3%, drifting against each other at
  9000ms cycles via the loop's 0.18 lerp channel. Both layers are
  `aria-hidden`, `pointer-events: none`, and clipped to their beds.
- **Motion spec.** Speckle points fade 0 → 0.9 → 0 on their own
  periods (`--ease-drift`), never more than ~30% of points lit at
  once (the period/phase distribution guarantees it; §10 samples
  it). Grain layers translate slowly (±6px across a cycle) and
  counter-phase, so the shimmer has weather, not a pulse. Both pause
  when their bed is off-screen and when the tab is hidden.
- **States.** Active (bed in view) → paused (off-screen/hidden).
  *Hover:* none. *Focus:* none. *Disabled:* absent — the grounds
  are flat colour, which this theme considers a perfectly good
  night.
- **Content merge.** Speckle lives on the foliage layer of beds
  whose planting is night-scented stock — the twinkle *is* the
  scent made visible, placed where the scented plants are, and
  beds without scented planting (the gate, the booking bed) get no
  speckle. The grain is in the soil of every bed equally — it is
  the ground's texture, not an effect laid over content, and it
  never sits on photographs (a flower's image is lit, not grained).
- **Failure fallback.** Absence is the fallback: if either layer
  fails to initialise, nothing is missing that anything else refers
  to. No watchdog is required because no state depends on them —
  the only ambient elements in the theme allowed that luxury,
  because they carry no information at all.
- **Reduced-motion variant.** Both layers absent. (Not frozen —
  absent. A frozen twinkle is a fly-speck; the edition simply has
  clear air.)
- **Performance budget & mobile variant.** Speckle: ≤40 opacity
  writes, throttled to every third frame (twinkle at 20Hz is
  indistinguishable and cheaper). Grain: two tiled backgrounds,
  transform-only drift. Mobile: speckle caps at 20 points, grain
  keeps one layer (420px tile) — half the weather for a smaller sky.
- **Choreography timeline (v2).** Continuous and deliberately
  unchoreographed at the beat level: the spec fixes periods,
  phases, caps and placement rules, and forbids aligning any
  twinkle to a scroll beat or an entrance — the moment a twinkle is
  synchronised to content, it becomes a highlight effect and leaves
  this element's licence.
- **State matrix (v2).** *Rest:* drifting/twinkling per bed in view.
  *Hover:* none. *Focus:* none. *Active:* n/a. *Scrolled-past:*
  paused off-screen. *Disabled:* absent. *Touch:* identical; no
  touch behaviour.
- **Breakpoints (v2).** ≥1200px: 40-point cap, two grain layers.
  768–1199px: 28 points, two layers. <768px: 20 points, one layer.
- **Edge cases & failure modes (v2).** *Low-power device:* if the
  loop's frame cost exceeds budget (§14), this element is cut
  **first** (it heads the §14 cut order) — the night loses its
  shimmer before it loses anything structural. *Long beds:* speckle
  density is per-viewport, not per-bed-length — points regenerate
  against the visible foliage, never accumulate down a long bed.
- **Accessibility spec (v2).** Purely decorative, `aria-hidden`, no
  focus, no information. Twinkle peaks at 0.9 opacity on 1–2px
  points cannot trigger photosensitivity concerns (no flashes above
  threshold size/rate; the pattern is slow fades, never strobes).
- **Tokens consumed (v2).** `--silver`, `--silver-pale`,
  `--ease-drift`, `--speckle-max` (40), `--grain-cycle` (9000ms).

### 6.18 The first-light page (page family: 404 / empty state)

- **What & why.** The 404 and the empty states wear the garden at
  dawn: a `--firstlight` ground, the moon already set, one unplanted
  bed drawn in outline, and the plain fact stated first. It belongs
  because a wrong turning in a garden at night ends at the fence at
  first light — the theme has a native place for "not here", and it
  is the morning. An empty bed is also the honest shape of every
  empty state this theme serves (no evenings in a month, a search
  with no flowers): the bed is real, it is simply not planted.
- **Structure.** A single bed on `--firstlight`: the fact in
  Alegreya Sans ("This page is not planted here."), the garden's
  line in Cormorant italic ("The garden you are looking for is
  further up the path."), an outline-drawn empty bed (a `--silver`
  rectangle at 40% with its path edge), the fragrance number it
  *would* have carried left blank — the number space prints as
  "№ —" — and three real ways back: the gate (home), the beds
  index, and the current month's programme. Search-empty and
  month-empty variants reuse the bed with their own facts ("No
  flower in the garden answers to that name." / "No evenings are
  planted in February. The garden rests.").
- **Motion spec.** One licensed motion: on entry, the horizon rule
  (§6.10's line) draws across the top over 800ms `--ease-draw` and
  the bed outline settles from 60% to 40% opacity — dawn arriving,
  once. Nothing else moves. The moon does not rise to rescue the
  visitor; it has set, and the page admits the hour.
- **States.** Rest only. *Hover/focus:* the three ways back take
  standard link states. *Disabled:* identical, minus the rule draw.
- **Content merge.** The blank "№ —" is the merge: the missing page
  is placed inside the page's own numbering system as a gap in it,
  the way a missing plant leaves a gap in a bed with its label
  still in the soil. The ways back are the garden's real structure
  (gate, index, programme), not a sitemap dump.
- **Failure fallback.** This element *is* a fallback; its own
  failure mode is a server-default 404, which the build must style
  with at minimum the `--firstlight` ground and the fact line —
  declared here so even the unstyled-by-accident case is on-theme.
- **Reduced-motion variant.** Identical, minus the rule draw.
- **Performance budget & mobile variant.** One rule draw; the
  lightest page in the theme. Mobile: the three ways back stack;
  the bed outline narrows to the measure.
- **Choreography timeline (v2).** t=0 fact visible (the fact never
  waits for choreography) → t=0–800 horizon rule draws → bed
  outline settles by t=800 → page at rest. The garden's line fades
  in across t=200–600 — comfort after fact, in that order.
- **State matrix (v2).** *Rest:* as built. *Hover:* link states
  only. *Focus:* standard rings (`--moonflower` on `--firstlight`).
  *Active:* n/a. *Scrolled-past:* n/a (single bed). *Disabled:*
  static. *Touch:* identical.
- **Breakpoints (v2).** All sizes: single bed, measure ≤52ch; the
  outline bed scales to the measure.
- **Edge cases & failure modes (v2).** *A URL that almost matches a
  bed (a mistyped bed name):* the page may offer that bed as the
  first way back ("Did the path mean № 4 — the jasmine bed?") —
  offered as a question, never as a redirect; a garden does not
  move its visitors without asking. *Search with results in a
  closed month:* the empty state names the month the flower *does*
  open in, from the planting data.
- **Accessibility spec (v2).** The fact is the `<h1>`; the three
  ways back are a real list of links; the decorative outline is
  `aria-hidden`. Contrast: `--moonflower` on `--firstlight`
  10.94:1 throughout.
- **Tokens consumed (v2).** `--firstlight`, `--moonflower`,
  `--silver`, `--ease-draw`, `--dur-rule-draw` (500ms; the horizon
  uses 800ms, declared in §5's ledger as this element's variant).

## 7. Page application map

- **Home — the full night.** The canonical page: gate bed → hero
  (§6.1, §6.7) → beds in programme order (§6.2 panels, §6.3's pin at
  the pollinator bed, §6.14's records) → booking bed (§6.15) →
  first-light footer (§6.10). All 18 elements available; the §13
  choreography map is written against this page.
- **Listing — the beds index.** A shallower night: the page is one
  leaf-stop shallower throughout (grounds declared 0 → 0.45), the
  moon still spans crescent → full across the page's real length
  (§6.5's short-page rule), and the listing's rows are §6.13 cards
  without photographs — a list of plantings with their hours. The
  pin is refused here; a list is walked, not stood in.
- **Detail — one bed, deep.** A single flower/bed page goes to full
  `--soil` by its second section and stays: the detail page is the
  deep end of the garden. §6.2's panel grammar carries the
  photography; §6.15's form narrows to that bed's evenings. The
  progress moon spans the page as usual — a short page still has a
  whole evening in it.
- **About — the gardener.** The maker's page is set at the tea bed's
  hour (grounds 0 → 0.3, never full dark): the gardener is met in
  the garden's social light, not its depths. Portrait treatment is
  §6.1's brightening (the moon reaches a face the same way it
  reaches a flower); the fragrance furniture (§6.12) still heads
  each section — the gardener's sections smell of what grows beside
  them.
- **Programme / month — the calendar as a bed.** A month's evenings
  listed as plantings: each evening a §6.13 card whose facts include
  its `phaseOn` phase name (computed per date — the calendar is
  where the sky's moon does its public work). A month with no
  evenings is §6.18's unplanted bed, verbatim.
- **Contact / the gate.** The gate page keeps gate hours: grounds at
  their lightest stops, the form in §6.15's grammar minus the phase
  line (a question to the gate is not a booking), and the answer
  promised in the Gate's voice with a real timeframe from the
  venue's practice — never "we'll get back to you" (§12).
- **Journal — evening notes.** Dated entries as beds in reverse
  programme order (latest evening first); each entry's head (§6.12)
  carries the *actual* date and the moon that entry's evening had,
  from `phaseOn` — the journal is the one page where the sky's moon
  outranks the page's moon, because the journal is history, and
  history's phases are facts, not progress.

## 8. Worked examples

The canonical build used below: **Wrenmoor** — a walled garden in
the Welsh Marches, open after dark on Wednesdays and Saturdays,
April to October, seven beds, gates 19:40, last entry 23:20. The
worked dates are June 2025, and every phase quoted below is
`phaseOn` computed for that date — the examples obey the law they
illustrate. Its beds: № 1 the gate lawn ("cut
grass, cooling"), № 2 the moonflower wall ("moonflower, green and
sweet"), № 3 the jasmine court ("jasmine, after rain"), № 4 the
stock beds ("night-scented stock, honeyed"), № 5 the pollinator
meadow ("meadow grass, moth-winged"), № 6 the primrose hollow
("evening primrose, lemon"), № 7 the records and tea ("woodsmoke,
from the bothy").

### 8.1 The hero (gate bed, № 1)

*Scroll timeline.* t=0 (load): the page is at first light by default
— grounds at `--leaf`, the headline whole, the moonflower
photographs lit — for exactly one frame of honesty; then JS arms
the night. The moonrise (§6.1) runs its 4000ms: the disc climbs
behind "Wrenmoor" (Cormorant roman, 84px), and the three hero
photographs — the moonflower wall at dusk, the gate, the jasmine
court — brighten at distance steps 0, 2, 4 (600ms, 900ms, 1200ms
starts). At t=1400 the italic line beneath the name — *"the garden,
after dark"* — unfurls (§6.7): 18 letters, past the 16-letter cap,
so the stagger compresses to 39ms and the whole line is open by
t≈2800, inside the 1400ms total the cap guarantees. The bed head (§6.12) has already printed: "№ 1 — cut grass,
cooling — 19:40" (the gate bed's centre sits at `p` 0.02;
`eveningTime` gives 19:45, and the head prints 19:45 — the *gate
sign* in the copy says gates open 19:40, the bed's time is when the
visitor reaches its centre; the two numbers are different facts and
the copy keeps them straight). The rail shows the vine at its first
leaf, the moon a crescent at the arc's foot, phase name "WAXING
CRESCENT", and the standfirst: "Seven beds, planted for the dark.
The moonflowers open at nine." — a promise §6.2's № 2 panel keeps
two beds later, at its printed 21:10.

### 8.2 Mid-page: the pollinator meadow (№ 5, the pin)

*Scroll timeline.* The visitor arrives from № 4 (stock beds, ground
reaching full `--soil` at its window's end) into № 5's head:
"№ 5 — meadow grass, moth-winged — 22:05". The bed's ground is
`--soil` throughout (its window is behind it). The pin engages:
200vh of held ground — the meadow photograph full-bleed at the
bed's heart, the copy column beside it naming the two moth species
and the planting they work. 800ms into the pin, the moths (§6.3)
begin: the hawk-moth (18px) left→right, the white-shouldered (14px)
right→left at 0.8×, crossing over the photograph's moonflowers at
≈7s. The rail moon is gibbous, high on the vine; the vine's № 5
flower bloomed as the bed began. A visitor who flings past gets the
bed unpinned, moths at rest beside the photograph, copy complete —
the census (§10) counts the crossing as *offered*, not *seen*, and
the theme is content with that: a garden does not chase its
visitors with its moths. Below the pin, the bed's figures (§6.14):
"MOTHS RECORDED THIS SEASON — 212 — counted from the meadow log",
the log being the bed's own table further down — the figure's
source line names it, and the footer will restate the same 212 from
the same object.

### 8.3 Conversion: booking the jasmine court's evening

*Scroll timeline.* The booking bed follows № 7 (the page's order is
programme, then records, then the gate's business — you book after
you have walked). Its head: "№ 8 — night air, through the gate —
23:20" (the booking bed is the eighth bed; the census counts it).
The form (§6.15) rests at its defaults: date = the next open
evening (Saturday 7 June, from the programme data), phase line
already printed: a 20px gibbous disc and "Saturday 7 June — the
moon will be waxing gibbous, 82% lit" — computed: age 10.64 days
from the 2000-01-06 epoch mod 29.53059, illumination by the
declared cosine rule, both printed in the footer for checking. The
visitor changes the date to Wednesday 11 June: the line fades
(150ms), the disc redraws to the full phase (400ms), text lands:
"Wednesday 11 June — the moon will be full, and up before the
gates open" (age 14.64 days; moonrise by the declared
approximation ≈ 18:12, labelled as an approximation in the
footer). Party 2, name, email, the jasmine court's 21:30 sitting
chosen from the programme radios.
Submit: press, "Booking…" for 700ms, then the confirmation rises —
a card restating the evening and ending with the promise kept in
the Gate's plain words: "Two places, the jasmine court, Wednesday
11 June at 21:30. The moon will be full. Gates at 19:40 — come
early and walk the wall first." Every number in that paragraph came
from the form's own fields, the programme data, or `phaseOn`. None
came from a copywriter.

## 9. Anti-slop — what makes THIS theme look cheap

1. **The purple gradient night.** A violet-blue gradient sky with a
   stock moon clip-art is the theme's death: the grounds here are
   two flat declared stops and a disc with a geometry, and §2's
   closed token list exists to make the gradient impossible to
   reach for. *Cure:* flat grounds, `nightAt` interpolation, no
   sky imagery anywhere.
2. **Cards on a grey field.** A component library's card grid laid
   over a dark background ignores that the ground is the clock.
   *Cure:* beds (§4) — the ground changes per section, cards sit
   *in* beds on `--bed`, and a listing page is shallower by
   declaration, not by accident.
3. **The starfield screensaver.** Uniform twinkle, hundreds of
   points, synchronised shimmer: §6.17's census (≤40 points, no
   shared periods, ≤30% lit) exists because this is the first thing
   a lazy build does. *Cure:* the census, the seeded placement on
   scented beds only, and the cut-order that sacrifices the layer
   first.
4. **Fade-up everything.** Generic reveal-on-scroll applied to text,
   heads and furniture flattens the theme's grammar into the
   internet's default. *Cure:* reveals are blooms (§6.2) for
   photographs, prints (§6.12) for furniture, and stillness for
   copy. Text never performs.
5. **Moth spam / cursor moths.** Moths as ambient decoration across
   the whole page, or a moth that follows the pointer. *Cure:*
   exactly two, in one bed, ignoring the pointer completely
   (§6.3) — the census counts them.
6. **Two moons competing.** A decorative moon in the hero artwork, a
   logo moon, a moon in the footer illustration — each one breaks
   §1's law in spirit. *Cure:* the moons are the hero disc (§6.1),
   the rail instrument (§6.5) and the booking glyph (§6.15), each
   declared; any other moon in any asset fails review.
7. **Unfurling the slogan.** Kinetic type spent on marketing copy
   instead of the name (§6.7's licence is one line, once).
   *Cure:* the licence is written into the element; anything else
   that moves letter-by-letter is cut in review.
8. **The broken-image bed.** A failed photograph showing the
   browser's torn icon in a theme about care. *Cure:* §6.2's
   labelled empty bed — name in Cormorant italic on `--bed`,
   treated as a planting that didn't come up, with the caption
   intact.
9. **Pollen everywhere.** The puff (§6.9) attached to every button
   and link turns a receipt into a sneeze. *Cure:* cards only; the
   element's licence names its one host.
10. **Scent as wallpaper.** Fragrance notes that describe nothing in
    their bed, or notes on some sections and not others. *Cure:*
    §6.12's census — every bed, a note, and the note's planting
    present in the bed. A note without a plant is cut, and the bed
    is replanted or renumbered.
11. **Dashboard figures.** Counting stars, likes or "happy
    visitors" in the figures band. *Cure:* §6.14's rule — the
    garden's own census only, each with a printed source line; a
    figure the venue doesn't actually keep does not appear.
12. **Gold trim.** Gold borders, gold buttons, gold dividers —
    §2's gold law broken for sparkle. *Cure:* the grep in §10;
    gold is a living thing or a number, never a trim.

## 10. Quality gate

Blocking items — all must pass before the theme may be used in a
build. The gate is signed by someone who did not build the page.

1. **One-light audit.** Every brightness value on the page traces
   to §6.1's disc, §6.2's opening, or a declared element spec; no
   ad-hoc filters or shadows implying a second light source.
2. **Three-printings agreement.** Pick three figures at random
   (a bed count, a programme time, a footer figure): each must
   agree across its printings (bed / figures band / footer) and
   recompute from its declared function or data object.
3. **Phase honesty.** Copy references to the moon ("by full moon",
   "at first quarter") checked against `moonAt` at that bed's
   centre; booking promises recomputed from `phaseOn` for three
   sample dates, including one new moon.
4. **Contrast floors.** Screenshots at `p` = 0.25 / 0.6 / 1.0: every
   visible text element passes WCAG AA at its ground's current
   interpolated value, not just at the stops.
5. **Census.** Exactly 2 moths; ≤40 speckle points per viewport with
   no shared twinkle period; fragrance notes = beds, numbered in
   DOM order without gaps; vine flowers = beds; gold confined to
   §2's four jobs (grep + visual pass).
6. **No-JS completeness.** With JavaScript disabled: moon risen,
   flowers open, grounds at first-light stops, all copy legible,
   form submittable, footer dawned. Nothing invisible, nothing
   missing.
7. **Watchdog drill.** With the loop artificially stalled: petal
   masks open by their 1500ms fallback, headline open by 3400ms,
   moonrise complete by 5200ms, counters landed by 2200ms.
8. **Reduced-motion edition.** With `prefers-reduced-motion`: the
   finished static night — no pin, no moths, no twinkle, no unfurl,
   moon full, all information present in the same order.
9. **Night monotonicity.** Sampled grounds across scroll: no bed
   grows lighter as `p` increases (footer excepted, by its declared
   warmth axis); printed times increase monotonically down the page.
10. **The five-second test.** A first-time visitor, five seconds at
    the hero, can say: what this place is, that it opens at night,
    and when the gates open. If they say "pretty dark website", the
    build fails regardless of the other nine.

## 11. Component inventory

Every component a real site in this theme needs, with its treatment.
Components not listed do not get invented ad hoc; if a build needs
one, it is added here first.

- **Buttons.** Primary: `--moonflower` ground, `--soil` text,
  Alegreya Sans 700 caps; hover brightens the ground 6% (moonlight,
  not a colour change); active presses 1px with `--ease-settle`;
  focus 2px `--silver-pale` outline offset 2px. Secondary: 1px
  `--silver` outline, `--silver` text, hover fills at 12%. Buttons
  are never gold (§2 law) and never pill-shaped — a button is a
  gate, rectangular and honest.
- **Links (body).** `--silver-pale` with a 1px underline at 40% that
  draws to full on hover (§6.12's draw grammar at text scale);
  visited links rest at `--silver` — a path already walked is a
  little dimmer.
- **Inputs / textarea / select.** §6.15 verbatim: `--bed` ground,
  underline grammar, labels always above, errors as Gate-voice
  margin notes. No floating labels (a label that moves is a label
  that hides).
- **Cards.** §6.13 verbatim. No other card style exists.
- **Badges / stamps.** Text-only, in the §3 data style: "FULL",
  "LAST PLACES", "CLOSED FOR THE SEASON" — a badge on this page is
  a gate notice, never a coloured chip. "LAST PLACES" must be
  computed from the booking data; a badge that cries scarcity
  without the count behind it is refused and §10 checks one.
- **Tables.** The footer's record (§6.10) is the pattern: row rules
  `--silver` at 24%, terms in data style, values tabular, no zebra
  (the beds are the striping).
- **Pagination.** Refused as numbered pages. A journal or programme
  archive paginates as *seasons* — "Autumn evenings" is a bed, not
  a pager (§7).
- **Modal / dialog.** One pattern: the bed quick-view from a listing
  — a panel that rises like a gate opening (400ms `--ease-rise`)
  from the viewport's lower edge on `--bed`, holding the bed's
  panel photograph, scent note, hours and booking link. It never
  dims the page below the §6.16 cloud's 40% floor, and it closes by
  sinking. No other modal exists.
- **Toast.** Refused. Confirmations happen in place (§6.15) or in
  the footer record; nothing in a garden pops up from the soil
  uninvited.
- **Tabs.** Refused. A programme's months are beds in sequence
  (§7), travelled by scroll; switching is for dashboards.
- **Accordion.** The journal index only: entry rows open downward
  over 350ms `--ease-rise`, one at a time, each row headed by its
  date and its `phaseOn` phase name (§7) — the accordion's grammar
  is a bed opening, not a drawer.
- **Alerts.** In-band margin notes in §12's voices, `--silver-pale`
  text + `--moth` hairline. Never red — there is no red in this
  palette; an error is a gate that will not open, stated plainly,
  not an alarm bell in a garden.
- **Loader.** §6.16's night-soil skeleton. Spinners are banned —
  nothing in the garden spins.
- **Tooltip.** Refused. Anything worth saying is printed (the scent
  note is the model: say it in the open, in the furniture).
- **Breadcrumb.** Refused; the rail (§6.11) + the bed head (§6.12)
  already answer "where am I" in the theme's own terms: a number, a
  scent, a time.
- **Price display.** Alegreya Sans tabular, unit always present,
  set in the facts line — never in Cormorant, never gold, never
  struck-through beside a "real" price (a garden does not haggle).
- **Image frame.** Photographs sit directly on the bed's ground
  with a 1px `--silver` rule at 24% — the path edge (§4). No
  shadows, no rounded corners beyond 2px; the petal mask (§6.2) is
  the only shaped frame, and it belongs to flowers.

## 12. Content & copywriting voice

Two registers. **The Gardener** speaks for the garden itself:
sensory, specific, unhurried — names the plant, the hour, the
condition. **The Gate** speaks for the venue's business: times,
prices, places, plainly and without pressure. Neither register uses
exclamation marks, the word "magical", or the phrase "hidden gem".

- **Headlines.** Cormorant, a place or a planting, never a pitch.
  ✓ "The jasmine court" / "Seven beds, planted for the dark".
  ✗ "Experience the Magic of the Night!" / "Unlock Your Evening".
- **Scent notes.** The §6.12 furniture: plant, comma, condition.
  ✓ "jasmine, after rain" / "stock, on warm stone" / "cut grass,
  cooling". ✗ "a symphony of floral notes" / "nature's perfume" —
  a note that could head any bed heads none (§9.10).
- **Labels & data.** Computed or counted, formatted by §3's rules.
  ✓ "№ 5 — 22:05" / "212, counted from the meadow log".
  ✗ "later that evening" where a time could be printed; "lots of
  moths" where a count exists.
- **Buttons.** The act, in the evening's terms. ✓ "Book the
  evening" / "Walk the beds" / "See June's evenings". ✗ "Submit" /
  "Buy now" / "Get started".
- **Errors (Gate voice).** A direction that will not carry, stated
  with the correction. ✓ "That email will not reach the gate — the
  part after the @ is missing." / "Choose an evening the garden is
  open — the season ends 28 September." ✗ "Invalid input." /
  "Oops! Something went wrong."
- **Empty states (Gardener voice).** A bed not planted, stated as a
  season fact. ✓ "No evenings are planted in February. The garden
  rests." / "No flower in the garden answers to that name."
  ✗ "Nothing here… yet!" / "Stay tuned!"
- **The dark-night line (owned, verbatim where used).** For a
  new-moon date in §6.15: "The moon will be new; the garden is at
  its darkest, and the stock is at its sweetest." The theme never
  apologises for darkness.
- **Banned words.** magical, enchanting (as a claim about the
  site itself), hidden gem, oasis, unlock, elevate, curated
  experience, vibes. **Owned words.** bed, gate, hour, phase,
  planted, open (of flowers and of gates), recorded, counted,
  up (of the moon: "the moon is up by nine").
- **The rail caption (verbatim, once, §6.5).** "The moon keeps the
  furthest you have come." — the one place the page explains its
  own instrument; everywhere else the instrument is simply used.

## 13. Full-page scroll choreography map

The home night, top to bottom (progress = page `p`, §4):

1. **p 0.00 — the gate.** Rail in place: vine at its foot, moon a
   crescent. Moonrise (§6.1) runs; the name unfurls (§6.7); № 1's
   head prints "19:45". *Feels like:* arriving as the light goes.
2. **p 0.02–0.14 — the moonflower wall (№ 2).** First petal panels
   (§6.2) bloom at centre; grounds begin their slide from `--leaf`;
   the vine's second flower opens. *Feels like:* the first flowers
   opening as you reach them.
3. **p 0.14–0.30 — jasmine and stock (№ 3–4).** Panels in beds of
   two columns; speckle (§6.17) starts on the stock bed; grounds
   reach full `--soil` at № 4's end. *Feels like:* the garden
   getting darker and sweeter at once.
4. **p 0.30–0.52 — the meadow approach.** Single column now (§4's
   density law); the moon passes first quarter on the rail; № 5's
   head prints "22:05". *Feels like:* the path narrowing, the
   night deepening, one thing at a time.
5. **p 0.52–0.66 — the pin (№ 5).** The stage holds 200vh; the two
   moths cross (§6.3); the figures band below counts the season
   (§6.14). *Feels like:* standing still in the meadow while the
   garden's inhabitants go about their work.
6. **p 0.66–0.80 — primrose and records (№ 6–7).** The deepest
   grounds; line-height at its loosest; the tea bed's woodsmoke
   note; the moon gibbous, high. *Feels like:* the far end of the
   garden, where it is darkest and quietest.
7. **p 0.80–0.92 — the booking bed (№ 8).** Ground steps back
   toward `--leaf` stops (declared: the booking bed's window runs
   shallower — business is done in the light there is); the form
   (§6.15) with its phase line. *Feels like:* returning toward the
   gate with a decision to make.
8. **p 0.92–1.00 — first light.** The footer (§6.10): the moon,
   full since p 0.97, sets into the horizon rule; the band warms;
   the record prints the evening just walked. *Feels like:* the
   walk ending at dawn, logbook open.

**Reverse pass.** Scrolling up retraces every scrubbed value
(grounds, vine stem, moon position, footer warmth) exactly; every
*completed* event stays completed (blooms, unfurl, counts, the
moon's phase at its maximum). The garden remembers what has opened;
the hour alone runs backwards.

**Jump scroll.** Any jump lands positionally correct in one frame:
grounds, moon and vine at their `p` values; panels and heads
between the old and new positions resolve to their finished states
via their watchdogs without playing. A visitor who jumps to the
booking bed meets a garden already open, not a film fast-forwarded.

**Timing contract.** At a natural reading pace the full night takes
3–5 minutes: roughly a minute in the first three beds, 30–45
seconds held in the meadow (the pin at reading speed), a minute in
the deep beds, and the booking taken at the visitor's own pace. A
build whose page is so short that full moon arrives in under 30
seconds of scrolling has planted a window box and called it a
garden — lengthen the beds before launch. Conversely, past ~4,500
words of body copy before the pin, the evening outstays its
welcome: move a bed after the records or cut copy — the night is
260 declared minutes and the page must feel like them.

## 14. Whole-page performance budget

- **Total page weight:** ≤950 KB (home night), of which hero images
  ≤70 KB each (≤6), panel images ≤90 KB each and lazy below the
  first bed, card images ≤60 KB, fonts ≤120 KB (Cormorant 500 +
  italic subset; Alegreya Sans 400/700), JS ≤50 KB, CSS ≤40 KB.
  The vine + moon + moth SVGs together ≤10 KB. No other imagery
  ships without a budget line here.
- **Frame budget:** the single loop does ≤1.4ms of work per frame
  (one `p` computation, one lerp pass over ≤16 subscribed values,
  batched style writes); no layout reads inside the loop (bed
  windows are measured on resize only). Long tasks: none over 50ms
  after load; the §6.7 letter-wrapping is the largest single task
  and is capped by the 16-letter compression rule.
- **Paint discipline:** scrubbed values are transform, opacity,
  background-colour (flat, per bed) only; masks animate via a
  custom property on shared SVG masks (§6.2), never by repainting
  photographs; speckle writes are throttled to every third frame
  (§6.17).
- **Cut order when over budget:** (1) §6.17 speckle & grain (the
  night loses its shimmer first); (2) foliage parallax second layer
  (keep 0.3×); (3) §6.16 cloud transition (instant navigation);
  (4) panel distance-stagger in the hero (all flowers brighten
  together); (5) moth flight on tablet (rest at the photograph).
- **Never cut:** the §1 functions and their single source, the
  watchdogs, the no-JS completeness, the fragrance furniture, the
  §6.15 phase line. A build that ships without these is not a
  cheaper Moon Garden; it is a dark page with flowers on it.
- **Measurement method (named, so two builders get the same
  numbers).** Frame cost is measured on the loop's own
  instrumentation: per-frame execution time into a ring buffer,
  95th percentile over a full descent + return on a mid-tier
  Android device (the library's reference handset class), with a
  4× CPU-throttled devtools pass as cross-check. Page weight is
  transferred bytes on a cold cache, fonts included, from the
  production build. A budget dispute is settled by these two
  measurements and no others; "it feels smooth on my machine" is
  not evidence at the gate.

## 15. Build-order checklist

1. **Static first light first.** Build the whole page as the no-JS
   edition: grounds at first-light stops, moon risen and full,
   flowers open, vine drawn, form working, footer dawned. Gate
   §10.6 passes here, before any motion exists.
2. **The functions.** Implement §4's `nightAt`, `moonAt`,
   `eveningTime`, `phaseOn` + the formatters; unit-check them
   against three hand-computed values each (including a new-moon
   date and the gate time) before they touch the page.
3. **The bed map.** Declare every bed's number, scent note, night
   window and centre `p` in one source; generate §6.6's vine,
   §6.11's nav and §6.12's heads from it. Census (§10.5) runs here
   in miniature.
4. **The shared loop.** One rAF loop, lerp channels, sleep rules,
   the instrumentation ring buffer (§14). Nothing animates outside
   it from this step on.
5. **Grounds and rail.** §6.4's deepening, §6.6's vine draw, §6.5's
   moon — the scrubbed skeleton of the night, in that order.
6. **The hero.** §6.1's moonrise + §6.7's unfurl, with watchdogs
   wired before the animations are tuned.
7. **Panels and furniture.** §6.2's masks (+ the 1500ms fallback),
   §6.12's head pin, §6.8's hover bloom.
8. **The pin.** §6.3's stage and moths, with the sticky-failure and
   mobile no-pin paths built, not promised.
9. **Cards, figures, form.** §6.13, §6.14 (against the `GARDEN`
   object), §6.15 (phase line wired to `phaseOn`, errors in the
   Gate's voice).
10. **Footer and dawn.** §6.10's warmth axis + moon custody, the
    record generated from sources, the sky rule printed.
11. **Ambient and transitions.** §6.17's speckle/grain (census
    armed), §6.16's skeleton + cloud, §6.9's pollen.
12. **The first-light page.** §6.18 + the `prefers-color-scheme:
    light` edition + print stylesheet.
13. **Reduced-motion pass.** Every element's variant verified
    against its spec, in order, on a real device setting — not a
    devtools toggle alone.
14. **Copy pass.** §12's voices read aloud; scent notes checked
    against plantings; every moon reference checked against
    `moonAt`/`phaseOn`; banned words grepped.
15. **The gate.** §10 run end-to-end and signed by a non-builder;
    the five-second test done with a stranger, not the team.
