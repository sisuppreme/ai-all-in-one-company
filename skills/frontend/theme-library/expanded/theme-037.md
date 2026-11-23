# 37. Glacier Confession — Expanded (v1 + v2)

> Expansion of theme #37 from `themes-026-050.md`, written directly to
> the full standard: the v1 10-part structure plus the v2 deepening
> layers (per-element choreography timelines, state matrices, breakpoint
> behaviour, edge cases, accessibility specs and token lists; per-theme
> component inventory, copywriting voice, three worked examples, scroll
> choreography map, performance budget, build-order checklist).
> Identity preserved exactly: the same concept, the same five palette
> anchors, the same two typefaces, the same nine signature elements —
> deepened, never redesigned — plus nine page-family elements.

## 1. Concept & world

Most websites are read at the speed of the visitor's impatience. This
theme is built at the speed of ice. The page is **a core sample drilled
out of a glacier and laid on the reading table**: ten thousand years
compressed into one scroll, each section an era in the ice, and the act
of scrolling is the act of descending — surface snow at the top, ice
older than agriculture at the bottom. The glacier is not a metaphor the
page wears; it is the page's physics. Things here are slow because ice
is slow. Things here are compressed because pressure compresses. Things
here are preserved because that is what ice does to what it holds — and
the theme's name is its thesis: **the ice confesses**. What was trapped
in each era — air, ash, pollen, a summer's warmth, a civilisation's
smoke — is released, in order, as the visitor drills down.

The world is the ice core as a complete interface vocabulary. The page
has a **surface** (the hero, bright snow glare, the present day), a
**firn zone** (young sections, still partly air, pale and loose), the
**deep ice** (old sections, dense, dark, blue), a **depth/age readout**
(the spine: a fixed gauge that converts the visitor's scroll position
into metres below surface and years before present, on one declared
scale), **strata** (the era panels themselves, pinned and crossfading
like core segments passing under a lamp), **bubbles** (the trapped air
of each era — the page's bullet points, shrinking and compressing with
depth exactly as real core bubbles do under pressure), and **bedrock**
(the footer, where the drill stops). Nothing on the page is decoration
that happens to look glacial; every animated thing is either the ice,
the drilling, or the instruments that read the core.

**The theme's one law: every age on this page is computed from one
declared scale, or it is not printed.** The readout's years, the era
labels' date ranges, the bubble sizes, the panel densities — all of
them derive from the single depth–age model the page declares in its
colophon (§6.17): depth in metres mapped to age by the stated function
(§6.2), era boundaries at stated depths. A Glacier Confession build
that types "8,000 years" under a section because the copy needed a
rounder number has not bent the theme; it has falsified a core sample,
and the quality gate (§10) fails it on sight. The confession must be
true, or the theme is a screensaver.

**What the ice confesses, era by era.** The confession is not a mood;
it is a contents list, and each stratum confesses a different category
of thing. The surface confesses the present: today's weather, today's
date, the party currently standing on the ice. The firn confesses the
industrial centuries — soot, lead, the first artificial warmth in the
air. The melt zone confesses the agricultural millennia: pollen,
methane from the first herds, ash from named volcanoes in named years.
The crevasse zone confesses the early civilisations — smoke from the
first smelting, dust from the first ploughed deserts. The deep ice
confesses the ice age itself: air from a colder world, when the
planet's breath was different. And the abyss confesses the oldest
sentence on the page, whatever the build's subject was doing 12,000
years ago — which is why §4 starves it of company. A build choosing
this theme should be able to write, for each of its eras, the one
sentence that era confesses; an era with no sentence is a coloured
band, and coloured bands are §9's first failure.

**Descent is the interaction model.** Because reading is drilling, the
visitor's acts are a glaciologist's acts: they thaw specimens into
legibility (§6.4), they warm a panel with attention and watch its frost
edge retreat (§6.8), they crack a hairline into a specimen card to mark
it (§6.9), and their depth is always known (§6.2). The site does not
have scrollers; it has a drilling party of one, going down.

**Best-fit sites and audiences.**

- Climate and earth-science storytelling: ice-core research programmes,
  polar institutes, glacier monitoring services, museum exhibitions on
  deep time — content that already thinks in strata, ages and samples.
- Long-form history told as deep time: a civilisation's timeline, an
  archive's centuries, a brand's founding-to-present descent where each
  era is genuinely dated.
- Slow luxury and preservation brands: archives, cellars, libraries,
  conservation workshops — anything whose promise is "we keep things,
  carefully, for a very long time."
- Memorial and record pages: a life, a regiment, a newspaper's run —
  content whose sections are eras and whose tone is solemn patience.
- Annual reports and institutional histories structured by era, where
  the dates are audited facts the publisher will print in the colophon.

**When NOT to use it.**

- For anything urgent, transactional or time-sensitive. The theme's
  fastest ceremony is a 900ms thaw; its hero takes 2.5s to become
  legible. A visitor trying to buy, book or bail out will feel buried.
- For content without real chronology. If the sections are not eras —
  if the dates would be invented to fill the readout — the confession
  is fabricated and the gate (§10) refuses the build.
- For dense data products. Deep sections are low-density by law (§4);
  a 40-row table cannot be pressed into the abyss layer.
- For audiences in a hurry or on entry-level hardware as the *only*
  audience: the pinned strata and scrubbed readout are honest work for
  a phone GPU, and §14's cut order exists, but a build whose readers
  are mostly on 2016 Android should choose a lighter theme.
- For cheerful, high-energy subjects. The register is solemn by
  physics; a glacier theme wrapped around a soft-drink launch is a
  costume, and §9 names it.

## 2. Palette

Five anchors, inherited unchanged. The palette is a core laid
horizontally on a white table under laboratory light: snow glare at the
surface end, melt blue in the firn, crevasse blue where the ice first
darkens, deep ice in the old layers, abyss at the bedrock end. Nothing
else is admitted; every other colour on the page is one of these five,
tinted toward snow or shaded toward abyss, or set at an opacity over
its own stratum.

| Token | Hex | Role | Usage ratio | Pairing & contrast notes |
|---|---|---|---|---|
| `--snow` | `#EDF3F2` | Snow glare: the surface ground, the hero field, light panels, text ground in the firn | ~34% of pixels | Abyss on it **14.49:1** (AAA); deep ice on it **9.48:1** (AAA) — the only two inks body text may use on snow. Melt blue on it is **1.36:1** — a wash, never text, never a line that carries meaning. |
| `--melt` | `#B9D6DE` | Melt blue: firn panels, young strata, bubble fills, the thaw sheen | ~26% of pixels | Abyss on it **10.64:1**; deep ice on it **6.96:1** (AA) — body text in the firn is set in deep ice or abyss only. Crevasse on it is **2.21:1** — never text, never the sole carrier of a datum. |
| `--crevasse` | `#5E93A8` | Crevasse blue: mid-depth panels, the readout's needle, hairlines, strata boundaries | ~14% of pixels | On snow **3.01:1** and on deep ice **3.15:1** — graphical and large-display use only (≥24px, or non-text line-work ≥2px). Its darkened derivative `--crevasse-deep` (see below) is the only form in which this hue may set text. |
| `--deep` | `#1D4258` | Deep ice: old strata panels, the readout body, headings in the light zones | ~16% of pixels | On snow 9.48:1, on melt 6.96:1 — a full text ink in the upper half. As a ground it carries snow text at 9.48:1 and melt-blue display text only. |
| `--abyss` | `#0B2233` | The abyss: the deepest panels, bedrock footer, body ink everywhere | ~10% of pixels | On snow 14.49:1, on melt 10.64:1, on crevasse **4.81:1** (AA, large text and short labels only on crevasse grounds). Abyss on deep is **1.53:1** — forbidden pairing; deep panels take snow or melt text, never abyss text. |

**Derived tokens (closed list — no others may be coined).**
`--crevasse-deep #35657C` (crevasse shaded toward abyss until it
reaches **5.9:1 on snow** and **4.6:1 on melt**; the text-grade form of
the crevasse hue, used for era labels and readout figures in the firn);
`--firn #DCE9EC` (snow and melt mixed 55/45; the second stratum's
ground); `--ice-line #FFFFFF` at 55% over its stratum (the frost edge
of §6.8 and the hairline of §6.9, never a text colour); `--sheen
#FFFFFF` at 18% (the melt sheen of §6.8 only). Every derived token is a
mix of two anchors or one anchor at an opacity — a build that
introduces a sixth hue has left the glacier.

**The strata sequence (the palette in order of descent).** Grounds
and inks per stratum, generated from the anchors — a builder never
chooses a panel colour freely; the depth chooses it.

| Stratum | Depth band (default model) | Panel ground | Body ink | Era-label ink | Bubble size (§6.5) |
|---|---|---|---|---|---|
| Surface | 0–6.7m | `--snow` | `--abyss` (14.49:1) | `--crevasse-deep` | 14px |
| Firn | 6.7–15.3m | `--firn` | `--abyss` | `--crevasse-deep` | 11px |
| Melt | 15.3–60m | `--melt` | `--deep` (6.96:1) or `--abyss` (10.64:1) | `--crevasse-deep` | 9px |
| Crevasse | 60–140m | `--crevasse` at 38% over `--melt` | `--abyss` (4.81:1 on full crevasse; the 38% tint audits higher — measure the built tint, §10 gate 6) | `--abyss` | 7px |
| Deep | 140–240m | `--deep` | `--snow` (9.48:1) | `--melt` | 6px |
| Abyss | 240–300m | `--abyss` | `--snow` (14.49:1) | `--melt` | 5px |

Two rulings ride on this table. First, the crevasse stratum is the
only tinted ground on the page, and its tint percentage is fixed at
38% — a builder who deepens it to taste has changed the stratum's
depth without moving its label, which is falsification by colour.
Second, the ink flips from dark-on-light to light-on-dark exactly
once, between the crevasse and deep strata; a build that flips twice
has two glaciers.

**Dark-mode behaviour: the page does not invert; it descends.** A
`prefers-color-scheme: dark` visitor is not given a "dark theme"; they
are given the same core read under the night shift's lamp — the strata
sequence starts one step deeper (the hero ground is `--firn`, not
`--snow`), panel grounds shift one stratum down the scale, and every
text pairing is re-audited against the shifted ground (§10, gate 6).
The readout, the bubbles and the bedrock are unchanged: the
instruments do not care what time the laboratory clock says.

## 3. Typography

Two typefaces, inherited unchanged. **Spectral** — light weights, wide
tracking — is the voice of the ice itself: display, headings, era
labels, the readout's ages. **Inter** is the voice of the laboratory:
body text, data, captions, the apparatus. The casting law: *Spectral
speaks for the glacier; Inter speaks for the people measuring it.* A
headline in Inter or a data table in Spectral is a miscasting, caught
at the gate (§10).

| Role | Face / weight | Size (≥1200px) | Line-height | Tracking | Notes |
|---|---|---|---|---|---|
| Display (hero headline) | Spectral 300 | clamp(44px, 6.2vw, 84px) | 1.04 | 0.12em → 0.06em (thaws, §6.1) | The only text on the page whose tracking is animated; the tightening is the theme's signature. |
| Era heading (H2) | Spectral 300 | 34px | 1.12 | 0.08em | Always paired with its era label (§6.3); never set without its date range. |
| Section heading (H3) | Spectral 400 | 22px | 1.2 | 0.04em | Inside-era structure only. |
| Era label / readout age | Spectral 500 | 15px | 1.3 | 0.14em, uppercase | Set in `--crevasse-deep` on light strata, `--melt` on deep strata. |
| Body | Inter 400 | 17px | 1.65 | 0 | Measure 62ch maximum (§4); 16px below 768px. |
| Data / figures | Inter 500, tabular | 15px | 1.45 | 0.01em | All counted or measured values; tabular figures are law, not taste. |
| Caption / apparatus | Inter 400 | 13px | 1.5 | 0.02em | Sample numbers, depths, provenance lines. |

**Type laws.**

1. **Light is the display weight.** Spectral above 400 weight appears
   only in the era label and nowhere in display sizes; a bold glacier
   headline is a different theme's headline.
2. **Every era heading carries its dates.** An H2 without its
   "1,850 – 1,204 years before present" label line is unfinished, the
   way a core segment without a depth tag is scrap.
3. **Figures are tabular and Inter.** Ages, depths, counts and
   measurements never set in Spectral, never in proportional figures —
   a readout whose digits change width as they tick is a broken
   instrument.
4. **Tracking tightens only once.** The 0.12em → 0.06em tightening
   belongs to the hero thaw (§6.1) alone; no other text on the page
   animates its letter-spacing.
5. **No italics in the ice.** Spectral italic is refused throughout;
   emphasis inside body text is weight (Inter 600) or the crevasse-deep
   colour. Ice does not lean.

**Anatomy of an era label (worked example).** Every era label is one
line with four fields in a fixed order — era name, calendar span, age
span, depth span — set in Spectral 500 at 0.14em, fields separated by
a middle dot in the stratum's hairline colour: `THE FIRN · 1,850 –
1,950 CE · 76 – 174 YEARS BP · DEPTH 6.7 – 15.3 M`. All four fields
are computed from §6.2's model (check: 6.7m × 11.4 = 76 years; 15.3m ×
11.4 = 174 years — the label is the model, printed). A label missing
its depth field, or carrying an age the model does not produce at
that depth, fails §10's gate 1 without discussion. Calendar spans use
CE/BCE for the firn and above, and years BP alone below the melt —
nobody alive can picture "8,000 BCE" as a date, and the label does
not pretend otherwise; the switch happens at the stratum where the
calendar stops being a human instrument, which the colophon's scale
statement (§6.17) declares. Numerals in labels are lining figures,
en-dashes carry no spaces on their inner sides, and the era name is
the only field permitted a definite article.

## 4. Layout language

**The core is vertical and the page is the core.** One column of strata
descends the viewport; the readout (§6.2) is fixed at the left edge on
≥1200px (a 92px rail), at the top edge below 1200px. Content never sits
in a multi-column grid in the deep half: pressure narrows the world,
and below the firn the measure narrows with it — 68ch at the surface,
62ch in the firn, 54ch in the deep ice, 46ch in the abyss layer. The
narrowing is the layout's confession that the deeper ice holds less
air and less room.

**Strata geometry.** Each era is a panel of at least 100vh in the
pinned sequence (§6.3), full-bleed in its stratum colour, its content
held in the centred measure. Panel grounds descend the palette in
order — snow, firn, melt, crevasse-tinted melt, deep, abyss — and the
sequence may not skip or repeat a step: a build whose third panel is
darker than its fifth has drilled into the wrong glacier. Between
pinned eras, unpinned "core break" spacers of 24vh in the *deeper*
panel's colour mark the saw cuts where one segment ends and the next
was laid beside it.

**Density law.** Surface sections may run to 9 elements in the
viewport; firn sections 7; deep sections 5; the abyss section at most
3 — a heading, a paragraph, one specimen. Whitespace is not emptiness
here; it is the ice between the evidence, and the deep page is mostly
ice. Any build that fills the abyss layer with cards has not
understood what depth means.

**The working margin.** On ≥1200px the left rail carries, top to
bottom: the readout (§6.2), the era index (§6.13) as a column of depth
ticks, and nothing else. The margin is an instrument panel, not a
sidebar; no navigation, advertising or social furniture may be bolted
to it.

**Inside a panel.** Each era panel is internally built like a segment
on the light table, in a fixed order that never varies down the page:
the era label first (dates before claims, always), the era heading,
the confession paragraph — the one sentence of §1 written out in full,
with its evidence — then the era's specimens (§6.15) or its single
statement (in the deep strata), and finally the apparatus line at the
panel's foot: the depth band restated, the sample count, the name of
whoever logged the segment. The apparatus line is the panel's
signature; a panel without one is an unsigned segment and §10's audit
treats it as unlogged data. Internal vertical rhythm follows the
segment joint (96px) between these blocks, halved in the firn and
doubled in the abyss — the deeper the ice, the more space its few
sentences are given, because at 240m a paragraph is an event.

**Spacing rhythm.** A 12px base unit, but vertical gaps between strata
are measured in the theme's own unit: one **core break** = 24vh, one
**segment joint** = 96px inside a panel, one **sample gap** = 36px
between specimens in a list. Radii: panels are square-cornered (ice is
cut, not rounded); specimen cards (§6.15) carry a 2px radius — the
saw's tolerance, nothing more.

## 5. Full motion system

Five named easings, used everywhere and nowhere else:
`--ease-thaw` `cubic-bezier(0.22, 0.61, 0.21, 1)` (the long resolve —
thaws, tracking, frost retreats); `--ease-settle`
`cubic-bezier(0.33, 1, 0.68, 1)` (panels coming to rest, strata
crossfades' second half); `--ease-crack` `cubic-bezier(0.85, 0, 0.15, 1)`
(the hairline's fast draw, 250ms and under only); `--ease-drift`
`linear` (bubble rise, the only linear motion on the page — air does
not ease); `--ease-press` `cubic-bezier(0.55, 0.06, 0.35, 0.95)` (the
slow compression of the readout's logarithmic scale).

**Every motion term, translated or refused.**

- *Scroll-triggered reveals* → the thaw (§6.4): blur 4px → 0 over 900ms
  as a section centres. Nothing on this page fades up, slides up, or
  pops; ice does not perform entrances, it becomes legible.
- *Scroll scrubbing* → the descent itself: readout (§6.2), strata
  crossfades (§6.3), bubble compression is pre-computed per stratum
  (§6.5) rather than scrubbed — pressure is a property of depth, not
  of the visitor's hand speed.
- *Pinned scenes* → the era stack (§6.3): one pinned stage, eras
  crossfading across 480vh of scroll.
- *Parallax* → rationed to exactly two layers: bubble trails inside
  panels drift at 0.92× scroll rate (§6.6); everything else moves at
  1.0×. A glacier has no depth-of-field theatre.
- *Masked reveals* → the hero melt-line (§6.10): one horizontal mask
  wiping the hero image clear top to bottom, once.
- *Blur-to-sharp* → the theme's central act (§6.1, §6.4) — licensed
  here more heavily than in any other theme, and therefore governed
  hardest: every blur carries a hard timer (§6.1's 2500ms law, §6.4's
  900ms + watchdog) after which legibility is forced.
- *Kinetic typography* → refused, except the hero tracking tightening
  (§6.1). Letters in ice do not dance; one tightening, once, is the
  whole vocabulary.
- *Marquee* → refused permanently. Nothing in a glacier travels
  sideways forever.
- *Animated counters* → the readout (§6.2) and the sample counts
  (§6.11): figures derived from the declared scale or counted from the
  DOM, stepped, never eased into theatre.
- *Progress indicator* → the readout (§6.2) is the progress indicator;
  no bar, ring or percentage exists anywhere on the page.
- *Ambient loops* → rising bubbles (§6.6) only, at 6–10px/s, capped at
  14 bubbles per panel and 40 per page.
- *Micro-interactions* → frost-melt hover (§6.8), hairline crack click
  (§6.9), the seal-press submit (§6.16).
- *Page transitions* → the refreeze (§6.12): a frost veil descends,
  the new page stands beneath it already thawed.
- *Smooth scrolling* → glacial inertia: where a build smooths scroll
  at all, it smooths it heavily — the shared loop's 0.10 lerp *is*
  the smoothing, and no second smoothing layer may be stacked on it.
  The descent should feel like it has mass: slow to start, slower to
  stop, impossible to hurry. A build that adds a buttery third-party
  smoother on top of the lerp gets seasick ice (§9), and a build that
  hijacks the wheel outright is refused at the gate — the visitor's
  hand stays on the drill.
- *Reduced motion* → the printed core: all eras static in sequence,
  the age scale printed as a fixed ruler beside them (§6.2's variant),
  no blur anywhere, bubbles printed at their stratum sizes.

**The durations ledger.** Every duration on the page, in one place —
a build whose CSS contains a duration not in this ledger (or in an
element's own spec) has imported a warmer theme's reflexes.

| Duration | Owner | Act |
|---|---|---|
| 2500ms | §6.1 | Headline thaw (hard law) |
| 2000ms | §6.10 | Hero veil watchdog |
| 1800ms | §6.10 | Melt-line wipe |
| 1200ms | §6.4 / §6.18 | Section-thaw watchdog / 404 thaw |
| 1100ms | §6.11 | Counter run, 40ms steps |
| 900ms | §6.4 / §6.8 | Section thaw / refreeze on leave |
| 800ms | §6.17 | Bedrock hairline draw |
| 700ms | §6.15 | Specimen image settle |
| 600ms | §6.8 | Frost melt on hover |
| 500ms | §6.3 / §6.16 | Era-label slide / form covering sheet |
| 420 / 520ms | §6.12 | Veil down / veil up |
| 300ms | §6.7 / §6.13 | Diagram band outline / log tick fill |
| 250ms | §6.9 | Hairline crack draw |
| 200ms | §6.2 / §6.16 | Era-name swap / field-rule warm |
| 160ms | §6.7 / §6.16 | Band stagger / seal press |

Nothing on the page animates faster than 160ms except the crack's
easing curve itself, and nothing the visitor must *read through*
lasts longer than 2500ms. Between those two numbers is the theme's
whole tempo: the tempo of a substance that moves metres per year and
is being watched for seconds.

**The shared loop law.** One `requestAnimationFrame` loop, lerp 0.10
(the library's slowest but one — ice is patient), drives every
scrubbed value: readout, strata crossfade weights, bubble-trail
parallax, frost states. No element owns a scroll listener. The loop
sleeps when the tab is hidden and when no tracked value is within
1.5 viewports of the screen.

---

## 6. Signature elements

### 6.1 Headline thaw

- **What & why.** The hero headline begins frozen: blurred 8px and
  refracted, as if seen through the ice block the whole page is cut
  from, and thaws into focus over 2.5s while its letter-tracking
  tightens from 0.12em to 0.06em — the letters compressing as warming
  ice compresses. It is the theme's thesis in one gesture: everything
  on this page was locked in ice, and reading frees it. The title is
  the first specimen thawed.
- **Structure.** The `<h1>` in the DOM at full legibility (sharp,
  0.06em). JS arms the frozen state only after first paint: a wrapper
  carries `filter: blur(8px)` and a refraction layer (an SVG
  `feDisplacementMap` over a duplicate of the headline's own text,
  scale 6 → 0), both removed at the thaw's end. The tracking animates
  on the real element, never on a clone.
- **Motion spec.** Trigger: page load, after `fonts.ready` or a 600ms
  race, whichever first. Duration **2500ms `--ease-thaw`**: blur 8px →
  0 (front-loaded: 8 → 2px by t=1400ms, 2 → 0 by 2500ms), displacement
  scale 6 → 0 across the full span, tracking 0.12em → 0.06em linear
  within the same easing. **The 2500ms law: a hard timer forces the
  final state at 2500ms regardless of animation state, tab focus or
  loop health.** The thaw runs once per page view; it never replays
  on scroll-back.
- **States.** Frozen (JS-armed only) → thawing → thawed (terminal).
  Hover/focus: none — the headline is not a control and does not
  respond to attention; the ice thaws on its own schedule.
- **Content merge.** The blurred thing is the headline itself, the
  page's actual title, freed by the page's central act. Remove the
  thaw and the hero is a headline on snow — poorer, never broken.
- **Failure fallback.** No JS: the headline ships thawed. JS armed but
  loop dead: the 2500ms law fires. Fonts late: the thaw waits for the
  600ms race, then thaws in whatever face is standing — a thaw in a
  fallback face is still a thaw.
- **Reduced-motion variant.** No blur, no refraction, tracking at
  0.06em from first paint. The headline is simply there, the way it is
  printed in the core log.
- **Performance budget & mobile variant.** One filter animation on one
  element for 2.5s; the displacement layer is composited, ≤ 900KB
  total hero assets. Mobile (<768px): blur starts at 6px (small type
  blurs cheaper and reads sooner), duration 2000ms, displacement layer
  omitted — tracking and blur alone carry the thaw.
- **Choreography timeline (v2).** t=0 first paint (sharp, for one
  frame at most) → t≈16ms JS arms frozen state before the visitor can
  register the swap (armed in the same task as the head script's class)
  → t=600ms (or fonts.ready) thaw begins → t=1400ms blur at 2px, the
  words findable → t=2500ms sharp, tracking 0.06em, layers removed
  from the DOM → the era label beneath (§6.3) begins its stagger at
  t=2100ms, overlapping the thaw's last 400ms.
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest (pre-thaw) | Frozen, JS-armed only | Frozen at 6px blur |
  | Thawing | 2500ms `--ease-thaw` | 2000ms |
  | Thawed | Terminal; plain headline | Same |
  | Hover | No change | n/a |
  | Focus | Headline is not focusable; no change | Same |
  | Scrolled-past | Thawed | Thawed |
  | Disabled / no-JS | Thawed at first paint | Same |

- **Breakpoint behaviour (v2).** ≥1200px: full spec, 8px start blur.
  768–1199px: start blur 7px, duration 2300ms. <768px: 6px, 2000ms, no
  displacement layer, tracking range 0.10em → 0.05em.
- **Edge cases & failure modes (v2).** *Return visit in the same
  session:* the thaw replays — each page view is a fresh core face.
  *Headline longer than 3 lines:* the thaw is cancelled and the
  headline ships thawed; a 4-line blur field is a fog bank, not a
  specimen. *`filter` unsupported:* tracking-only thaw. *Tab hidden
  mid-thaw:* the 2500ms law is wall-clock, so the headline is thawed
  when the visitor returns.
- **Accessibility spec (v2).** The headline is real text, first in DOM
  order, readable by AT at all times — the blur is a visual filter
  only and is `aria-hidden` in its duplicate layer. No content is
  announced late; nothing about the thaw is announced at all.
- **Tokens consumed (v2).** `--snow`, `--abyss`, `--ease-thaw`,
  `--dur-thaw` (2500ms), `--track-wide` (0.12em), `--track-set`
  (0.06em).

### 6.2 Age readout descent (the spine)

- **What & why.** A fixed readout converts scroll position into the
  two numbers the whole page is organised by: **depth** (metres below
  surface) and **age** (years before present). It ticks from "Surface ·
  0 years" through "800 CE" territory to "12,000 years" at bedrock,
  easing slower as ages grow — a logarithmic feel, because the declared
  scale is logarithmic in its deep half: the first 10m of core hold a
  decade, the last 10m hold a millennium. It belongs because progress
  on this page *is* geological time; the gauge and the content's eras
  are one scale, printed once, used everywhere.
- **Structure.** A `<div class="readout" role="img">` in the left rail
  (≥1200px) or top bar (<1200px): three lines — `DEPTH 142.6 M`,
  `AGE 8,314 YEARS BP`, and the current era's name in Spectral. The
  numbers are real DOM text (updated by the loop), with a visually
  hidden static twin stating the full scale for AT ("This page descends
  from the surface to ice 12,000 years old"). The scale is declared in
  markup: `data-depth-max="300"`, `data-age-max="12000"`, and the
  mapping function named in §12's colophon — depth maps to scroll
  progress across the pinned sequence plus the unpinned sections'
  measured heights; age = the declared piecewise function of depth
  (linear 0–40m: 11.4 years/m; 40–300m: logarithmic, fitted so 300m =
  12,000 years exactly).
- **Motion spec.** Scrubbed by the shared loop (lerp 0.10). Depth
  updates every frame the loop runs; age is recomputed from depth by
  the declared function — never interpolated independently, so the two
  figures can never disagree. Display rounding: depth to 0.1m, age to
  whole years under 1,000 and to the nearest 10 above (an instrument
  does not pretend to yearly precision at 9,000 BP). The era name
  swaps at era boundaries with a 200ms `--ease-settle` crossfade.
- **States.** At surface (0.0m / 0 years) → descending (live) → at
  bedrock (300.0m / 12,000 years, terminal; the readout adds the line
  `BEDROCK` in `--crevasse-deep`). Scrolling up reverses exactly — the
  readout is a pure function of scroll position, nothing latched.
- **Content merge.** The readout's numbers are the eras' own depths:
  each era panel carries `data-depth-from` / `data-depth-to` on the
  same scale, and the readout enters an era's band exactly when that
  era is on stage. Gauge and content are two printings of one record.
- **Failure fallback.** No JS: the readout renders as the printed
  ruler of the reduced-motion variant (below). Loop dead: a 1200ms
  watchdog snaps the readout to the true scroll-derived values.
- **Reduced-motion variant.** The readout becomes a **fixed printed
  ruler**: a vertical scale in the rail listing each era with its
  depth band and age range, static, complete — the core log's index.
  The live numbers do not run.
- **Performance budget & mobile variant.** Two text writes per frame
  worst case, throttled to when the rounded values change. Mobile:
  the readout is a 44px top bar — depth and age on one line, era name
  dropped (the era headings carry it).
- **Choreography timeline (v2).** Scrubbed map, not a clock: progress
  0 → depth 0.0m, age 0 → first era boundary (progress ≈0.14) → depth
  40m, age ≈456 years, scale switches to its logarithmic leg → bedrock
  (progress 1) → depth 300.0m, age 12,000, `BEDROCK` line appears.
- **The declared model, checkpointed (v2).** The default model's
  fitted values, printed here so any builder's implementation can be
  audited against them without re-deriving the fit. Linear leg:
  age = 11.4 × depth (0–40m). Logarithmic leg: age = 456 + 5,729 ×
  ln(depth ÷ 40) (40–300m), fitted so 300m = 12,000 years exactly.

  | Depth | Age (years BP) | | Depth | Age (years BP) |
  |---|---|---|---|---|
  | 0m | 0 | | 60m | ≈ 2,779 |
  | 10m | 114 | | 100m | ≈ 5,705 |
  | 20m | 228 | | 140m | ≈ 7,633 |
  | 40m | 456 | | 200m | ≈ 9,675 |
  | | | | 300m | 12,000 exactly |

  A build that redeclares its maxima refits both legs by the same
  method (linear to 13% of max depth, logarithmic below, exact at
  bedrock) and prints its own checkpoint table in the build log; the
  readout's figures are then tested against that table at §10's gate
  1, at the six depths above. An implementation whose age at 100m is
  "about 5,000" because the easing *felt* right has failed the theme,
  however smooth the scroll.
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Surface | 0.0m / 0 years | Same, top bar |
  | Descending | Live, lerped 0.10 | Live |
  | Era swap | Name crossfades 200ms | Name swaps instantly (bar has no room for a fade) |
  | Bedrock | Terminal + `BEDROCK` line | Terminal |
  | Hover / focus | Not interactive; no state | Same |
  | Disabled / no-JS | Printed ruler | Printed ruler above the first era |

- **Breakpoint behaviour (v2).** ≥1200px: 92px left rail, three lines.
  768–1199px: top bar 52px, depth + age + era name on one line.
  <768px: top bar 44px, depth + age only.
- **Edge cases & failure modes (v2).** *Page shorter than the model*
  (a build with fewer eras): depth-max and age-max are redeclared in
  markup and the function refits — the readout must reach bedrock
  exactly at the footer's top, never before, never after. *Anchor
  jump to the footer:* the readout snaps on the next frame; no
  catch-up sweep (instruments do not perform). *Resize:* depths are
  recomputed from section offsets; the function is unchanged.
- **Accessibility spec (v2).** The live readout is `aria-hidden` (a
  scrubbed number stream is noise to AT); the hidden static twin and
  each era's own printed date label carry the information in reading
  order. The printed ruler (reduced motion / no-JS) is ordinary text.
- **Tokens consumed (v2).** `--deep`, `--crevasse-deep`, `--melt`,
  `--ease-settle`, `--loop-lerp` (0.10).

### 6.3 Era crossfades (the pinned strata)

- **What & why.** The eras are core segments: pinned on one stage,
  they crossfade as strata boundaries pass — opacity plus a 12px rise —
  each older layer visibly denser and darker, melt blue descending to
  abyss. It belongs because the sections *are* the core's layers;
  reading down is drilling down, and the crossfade is the lamp passing
  from one segment to the next on the core table.
- **Structure.** A 480vh scroll section holding a 100vh sticky stage.
  Era panels are absolutely stacked in the stage in DOM order (oldest
  last), each full-bleed in its stratum colour, content in the centred
  measure. The base (no-JS) layout is a normal vertical stack of the
  same panels — the pin is a JS/CSS enhancement laid over a printed
  core, never the only way the eras exist.
- **Motion spec.** Scrubbed: panel *n*'s crossfade occupies the middle
  60% of its 80vh scroll band; opacity of the outgoing panel 1 → 0,
  incoming 0 → 1, with the incoming rising 12px → 0 on
  `--ease-settle`'s curve, all weights written by the shared loop
  (lerp 0.10). One panel is fully opaque at every band boundary — the
  visitor is never between specimens at a resting scroll position for
  longer than the band's middle. Era labels (the H2's date line)
  stagger down the stage's left edge like core segments laid in a row:
  as each era takes the stage, its label slides 24px → 0 over 500ms
  `--ease-settle`.
- **States.** Active era (opaque, at rest) → crossfading (paired with
  its neighbour) → passed (opacity 0, `visibility:hidden` after the
  fade completes). Scrolling up reverses symmetrically. Focus inside a
  fading panel forces that panel to full opacity instantly (a reader
  who tabs into an era is *in* that era).
- **Content merge.** The panels are the content sections themselves —
  heading, text, specimens — not backgrounds behind content. The
  density gradient is the sections' own grounds descending §2's scale.
- **Failure fallback.** No JS or no sticky support: the static stack.
  Loop dead mid-fade: a 1000ms watchdog completes the fade to the
  nearer panel. A panel can never be stranded at partial opacity by a
  stalled loop.
- **Reduced-motion variant.** No pin, no crossfade: the eras stand in
  a static vertical sequence, each on its stratum ground, with the
  printed ruler (§6.2) beside them.
- **Performance budget & mobile variant.** At most two panels
  composited at once; passed panels are `visibility:hidden`. Mobile:
  the pin shortens to 320vh total, crossfade rise 8px, and eras with
  more than 5 viewport elements (§4's density law) shed their
  bubble-trail layer first (§14's cut order).
- **Band allocation (v2).** The 480vh pin divides by era, and the
  division is by *depth band*, not by equal shares — an era that spans
  200 years of firn does not get the scroll length of an era spanning
  4,000 years of deep ice. Each era's band = 60vh base + its share of
  the remaining 120vh in proportion to its age span's logarithm,
  normalised across the pinned eras, with a floor of 70vh and a cap of
  110vh per era; the build log prints the allocation table it
  computed. The crossfade occupies the middle 60% of each era's own
  band (above), so a long era is not a long fade — it is a long
  *stay*, which is the correct geology: most of a core is one stratum
  being read, and the boundaries are the brief events between stays.
  A build that divides the pin equally has made every era the same
  age, and §10's scale audit catches it at the second boundary.
- **Choreography timeline (v2).** Per boundary (t = scroll through the
  band): band start → outgoing at 1.0, incoming at 0 → band 20% →
  incoming label begins its 500ms slide → band 50% → both at ≈0.5,
  incoming risen 6px → band 80% → incoming at 1.0, outgoing hidden →
  the readout's era name swaps (§6.2) at band 50%.
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Active | Opaque, at rest | Same |
  | Crossfading | Paired opacities, 12px rise | 8px rise |
  | Passed | Hidden | Hidden |
  | Focus-within | Snaps to fully opaque | Same |
  | Hover | No change (panels are not controls) | n/a |
  | Disabled / no-JS | Static stack | Static stack |

- **Breakpoint behaviour (v2).** ≥1200px: 480vh pin, full spec.
  768–1199px: 400vh, rise 10px. <768px: 320vh, rise 8px, label slide
  16px.
- **Edge cases & failure modes (v2).** *Fast fling through three
  eras:* the loop's lerp settles weights to the true band; a settle
  timer forces exact end-state opacities within 300ms of scroll rest.
  *An era taller than the stage:* era content is capped by §4's
  density law; overflow content moves to the unpinned sections after
  the strata (§7), never scrolls inside a panel. *Print:* all panels
  print in sequence at full opacity (print stylesheet unstacks them).
- **Accessibility spec (v2).** DOM order is reading order (surface →
  bedrock) at all times; stacked panels are `visibility:hidden` when
  passed, so AT and keyboard meet exactly one era at a time in order.
  The stage carries `aria-label` naming the descent. Focus forcing
  (above) guarantees a keyboard visitor never reads a half-faded era.
- **Tokens consumed (v2).** The five anchors in sequence, `--ease-settle`,
  `--pin-length` (480vh), `--rise` (12px), `--loop-lerp` (0.10).

### 6.4 Thaw-into-focus sections

- **What & why.** Every unpinned section below the strata enters
  blurred 4px and resolves over 900ms as it centres — each era must be
  thawed before it can be read. It is §6.1's act repeated at section
  scale, the theme's central ceremony distributed down the page: the
  visitor does not *reveal* content, they free it.
- **Structure.** Sections ship sharp. An IntersectionObserver arms the
  blur (`filter: blur(4px)`) only on sections below the fold that the
  loop will actually drive, and only once per section. The thaw runs
  when the section's centre crosses 62% of viewport height.
- **Motion spec.** Trigger: centre crossing. **900ms `--ease-thaw`**,
  blur 4px → 0 (4 → 1px by 500ms, 1 → 0 by 900ms). One-shot: a thawed
  section never re-blurs. A **1200ms watchdog** per section forces
  blur 0 if the animation is interrupted for any reason.
- **States.** Sharp (default / above fold) → armed (below fold, JS
  only) → thawing → thawed (terminal).
- **Content merge.** The blur is on the section's own text and
  specimens — the era itself is frozen, not a veil over it. The
  section's heading, dates and body thaw together, as one specimen.
- **Failure fallback.** No JS: no blur is ever armed. Observer
  unsupported: sections ship sharp. The default state of every section
  in the DOM is legible; blur is only ever a temporary, JS-owned
  condition with two independent exits (animation end, watchdog).
- **Reduced-motion variant.** No blur, ever. Sections are read as
  printed.
- **Performance budget & mobile variant.** One filter per thawing
  section, ≤ 2 thawing concurrently (the observer queues the rest,
  nearest first). Mobile: start blur 3px, duration 750ms.
- **Choreography timeline (v2).** Section centre crosses 62% vh →
  t=0 thaw starts → t=500ms blur 1px, text findable → t=900ms sharp →
  the section's own elements (core diagram §6.7, counters §6.11) take
  their triggers from the thaw's end, not from scroll.
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest (above fold / passed) | Sharp | Sharp |
  | Armed | Blurred 4px, below fold only | Blurred 3px |
  | Thawing | 900ms | 750ms |
  | Thawed | Terminal | Terminal |
  | Focus-within while armed | Thaws instantly — focus is never asked to read fog | Same |
  | Disabled / no-JS | Sharp | Sharp |

- **Breakpoint behaviour (v2).** ≥1200px: 4px / 900ms. 768–1199px:
  3.5px / 850ms. <768px: 3px / 750ms, concurrency cap 1.
- **Edge cases & failure modes (v2).** *Anchor jump landing mid-page:*
  sections above the landing point are thawed instantly on arrival;
  the landing section thaws on the next frame. *Very long section:*
  the thaw triggers on the section's first viewport of content, not
  its centroid — a 300vh section must not stay blurred while its top
  is read. *Scroll-back:* no re-blur (one-shot law).
- **Accessibility spec (v2).** AT reads the DOM, which is never
  blurred in any assistive sense; the filter is visual only. Focus
  forcing (state matrix) is the keyboard guarantee. Contrast is
  audited at the thawed state; the 900ms mid-thaw is a transition,
  not a reading state.
- **Tokens consumed (v2).** `--ease-thaw`, `--dur-thaw-section`
  (900ms), `--watchdog-section` (1200ms).

### 6.5 Compressing bubble bullets

- **What & why.** Bullet points in this theme are the era's trapped
  air: circles that shrink and compress with depth — 14px diameter
  with 12px gaps in the surface lists, 5px with 5px gaps in the abyss
  lists — because that is what pressure does to bubbles in real ice,
  and because the original entry's anti-slop detail is the theme's
  fingerprint: *the list furniture itself carries the physics of the
  ice it lists facts about.* A build that uses ordinary disc bullets
  has removed the theme's most-checkable fact.
- **Structure.** Real `<ul>`/`<li>` lists; the marker is a CSS circle
  (border 1.5px in the stratum's ink, fill at 30% melt) sized by a
  per-stratum custom property set on the section: `--bubble-d` and
  `--bubble-gap` from the declared table — surface 14px/12px, firn
  11px/10px, melt 9px/8px, crevasse 7px/7px, deep 6px/6px, abyss
  5px/5px. Sizes are computed from the section's depth band by the
  same declared scale as §6.2 (diameter ≈ 14 × (1 − depth/300) + 5 ×
  (depth/300), rounded to the table) — the table is printed in §12 so
  two builders produce the same bubbles.
- **Motion spec.** None, and that is specified: bubble size is a
  static property of the stratum, set at build. The *impression* of
  compression accumulates as the visitor descends through lists. (A
  scrubbed resize was considered and refused: a bullet that shrinks
  while being read is a bullet that moves the text it marks.)
- **States.** One state per stratum. Lists inside a thawing section
  thaw with their section (§6.4); the bubbles have no independent
  states, hover or animation.
- **Content merge.** The bubbles mark the era's actual list items —
  findings, specimens, dates. They are the list's own punctuation
  undergoing the list's own subject.
- **Failure fallback.** Without CSS custom properties (no modern
  browser lacks them; the fallback is for print): markers print as
  8px circles at every depth — the compression is a screen refinement,
  and print keeps the lists.
- **Reduced-motion variant.** Identical — there is no motion to
  reduce. (Stated explicitly because the gate checks it.)
- **Performance budget & mobile variant.** Zero runtime cost. Mobile:
  sizes hold (the table is the theme's fact at every width); gaps
  tighten by 1px below 768px to protect the measure.
- **Choreography timeline (v2).** None — static per stratum. The
  "timeline" is the descent itself: surface list 14px → abyss list
  5px across the page's full scroll.
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Any list, surface → abyss | 14px → 5px per the table | Same, gaps −1px |
  | Hover / focus | No change | No change |
  | Disabled / print | 8px uniform | n/a |

- **Breakpoint behaviour (v2).** All breakpoints: the depth table
  unchanged. <768px: gap column −1px per row of the table.
- **Edge cases & failure modes (v2).** *A list in the wrong stratum*
  (a surface-styled list pasted into the deep section): the bubbles
  take the *section's* depth, always — size follows the ice the list
  sits in, never the list's own styling. *Nested lists:* sub-items
  compress one step further than their parent list (they are deeper
  in the same ice), floor 4px. *A list with one item:* still bubbled —
  a single trapped bubble is still evidence.
- **Accessibility spec (v2).** Real list semantics; the markers are
  CSS-generated and ignored by AT. Item text carries all meaning;
  bubble size is never the sole signal of depth (the era label states
  the depth in words).
- **Tokens consumed (v2).** `--bubble-d`, `--bubble-gap`, `--melt`,
  the stratum ink token.

### 6.6 Rising panel bubbles

- **What & why.** Inside the translucent panels, tiny air bubbles rise
  very slowly — 6–10px/s — sparse and continuous: the panels are ice
  samples, and their trapped air is visibly escaping as the visitor
  reads. It is the page's only ambient loop, and its slowness is the
  spec: a visitor should notice it the way one notices dust in a
  sunbeam, on the second look, not the first.
- **Structure.** Each translucent panel (the specimen panels of §6.15
  and the strata panels' margin zones) carries a bubble layer: ≤ 14
  `<span>` bubbles per panel, 2–5px, positioned in the panel's margin
  columns and gutter zones — **never in the text measure**. The layer
  is `aria-hidden`, `pointer-events: none`, created by JS; the DOM
  ships without it.
- **Motion spec.** Each bubble rises at its own rate in the 6–10px/s
  band (assigned by hash of its index, so panels never sync), on
  `--ease-drift` (linear), looping from the panel's base to its top
  over the panel's full height, with a ±3px horizontal sway on a 7s
  sine. Bubbles pause when their panel is off-screen
  (IntersectionObserver) and when the tab is hidden. The loop writes
  transforms only.
- **States.** Rising (panel in view) → paused (off-screen / hidden
  tab) → rising. No other states; bubbles ignore hover and focus
  entirely.
- **Content merge.** The bubbles live *in* the panel's ice — its
  margins and gutters, the panel's own substance — and a panel without
  the layer is complete. They are the specimen's trapped air, not a
  screensaver laid over the page.
- **Failure fallback.** No JS: no bubbles, nothing missing. Loop dead:
  bubbles freeze mid-rise — a still bubble in ice is physically
  correct, so even the failure state is in-fiction.
- **Reduced-motion variant.** No rising. Each panel prints with its
  bubbles static at their seeded positions — trapped air, held.
- **Performance budget & mobile variant.** Hard caps: 14 per panel,
  40 per page, transforms only, one shared loop. Mobile: 8 per panel,
  24 per page, sway removed.
- **Choreography timeline (v2).** Continuous: bubble spawns at panel
  base at its seeded offset → rises at 6–10px/s → exits at panel top →
  respawns at base after a seeded 2–9s gap. No synchronisation
  between bubbles, panels or pages is permitted.
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Panel in view | Rising, ≤14 | Rising, ≤8 |
  | Panel off-screen | Paused | Paused |
  | Hover / focus | No change | n/a |
  | Disabled / no-JS | Absent (or static under reduced motion) | Same |

- **Breakpoint behaviour (v2).** ≥1200px: full caps. 768–1199px: 10
  per panel. <768px: 8 per panel, no sway, rates 6–8px/s.
- **Seeding specification (v2).** Bubble positions, sizes and rates
  are seeded deterministically from the panel's sample number: size =
  2 + (seed × 7 mod 4) px within the 2–5px range, rate = 6 + (seed ×
  13 mod 5) px/s within the 6–10px/s band, horizontal seed offset =
  (seed × 37 mod 89)% of the margin column's width. Two builders
  seeding the same specimen produce the same air — the bubbles are
  part of the specimen's record, not a random garnish rolled at
  runtime — and a returning visitor meets the same bubbles rising in
  the same panel, the way a returning glaciologist meets the same
  core in the same cold store. Runtime randomness in this layer is a
  build defect: it makes the specimen different on every visit, which
  is precisely what a preserved sample must never be.
- **Edge cases & failure modes (v2).** *Panel shorter than 200px:*
  no bubble layer — a bubble crossing a short panel reads as a bug,
  not as air. *Low-power device (loop measuring <40fps sustained):*
  the layer is the first cut (§14) — bubbles freeze at seeded
  positions. *Photosensitivity:* 6–10px/s drift is far below any
  flash or vection threshold; the layer never covers text.
- **Accessibility spec (v2).** Purely decorative, `aria-hidden`,
  absent from the accessibility tree. It carries no information,
  state or affordance.
- **Tokens consumed (v2).** `--melt` at 40–70%, `--rise-rate`
  (6–10px/s), `--bubble-cap-panel` (14), `--bubble-cap-page` (40).

### 6.7 Core diagram draw

- **What & why.** In the science section, a core-sample diagram draws
  itself: a vertical core, band by band, each stratum band filling in
  its era colour in descent order, each band labelled with the depth
  and age the visitor has already passed. It belongs because the
  diagram is a map of the page the visitor has just descended through
  — the one place the whole confession is visible at once, drawn as
  they arrive at the section that explains it.
- **Structure.** One inline SVG: a core column (width 120px at
  ≥1200px) divided into bands whose heights are proportional to the
  eras' depth bands on §6.2's declared scale (not equal bands — the
  firn is thin, the deep ice is most of the core, and the diagram must
  not lie about that). Band fills are the five anchors in sequence;
  labels sit right of the column in Inter 13px with Spectral era
  names. The fully drawn diagram is the shipped state; JS arms the
  undrawn state only when the section is below the fold.
- **Motion spec.** Trigger: the science section's thaw completes
  (§6.4). Bands draw top to bottom: each band's outline strokes in
  300ms `--ease-settle`, then its fill fades in over 400ms, staggered
  160ms per band in descent order; labels fade in with their band.
  Total for six bands ≈ 2.5s. Draws once.
- **States.** Undrawn (JS-armed only) → drawing → drawn (terminal).
  Hover on a band: the band's label warms to full ink and the band
  outline thickens 1px → 2px (the diagram's one interaction: find an
  era on the map). Focus (bands are links to their eras, §6.13):
  same as hover, plus the focus ring.
- **Content merge.** Every band is an era the visitor has read, at its
  true proportional depth, in its true colour, with its true dates.
  The diagram is the page's table of contents drawn as the object the
  page is about.
- **Failure fallback.** Ships drawn. Watchdog 1500ms after trigger
  forces the drawn state if the stagger stalls.
- **Reduced-motion variant.** Drawn, statically, with labels — the
  printed figure in the core log.
- **Performance budget & mobile variant.** One SVG, six bands, stroke
  + opacity only. Mobile: the column narrows to 72px, labels move
  beneath their bands, stagger compresses to 100ms.
- **Choreography timeline (v2).** t=0 section thaw ends → t=0–300ms
  band 1 outline → t=160ms band 2 outline begins (stagger) → fills
  trail outlines by 400ms each → t≈2500ms all bands drawn, labels at
  full ink → the diagram is thereafter still, except hover/focus.
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Drawn | Drawn |
  | Drawing | 2.5s stagger | 1.9s stagger |
  | Hover (band) | Label warms, outline 2px | n/a |
  | Focus (band link) | As hover + ring | Same |
  | Scrolled-past | Drawn | Drawn |
  | Disabled / no-JS | Drawn | Drawn |

- **Breakpoint behaviour (v2).** ≥1200px: 120px column, side labels.
  768–1199px: 96px column. <768px: 72px column, labels beneath bands.
- **Edge cases & failure modes (v2).** *An era added or removed:* the
  diagram is generated from the same era data as §6.3/§6.13 — bands,
  heights and labels cannot drift from the page's eras. *A band too
  thin to label (the firn at true proportion is 9px):* minimum band
  height 14px with the distortion declared in the caption ("firn band
  enlarged ×1.6 to carry its label") — declared distortion is
  cartography; silent distortion is lying.
- **Accessibility spec (v2).** The SVG carries `role="img"` and a
  text alternative listing the eras with depths and ages in order;
  band links are real links with era names as their labels. The draw
  is never announced.
- **Tokens consumed (v2).** The five anchors, `--ease-settle`,
  `--draw-band` (300ms), `--stagger-band` (160ms).

### 6.8 Frost-melt hover

- **What & why.** Hovering a panel warms it: its frosted edge — a 10px
  inner border of `--ice-line` blur — melts back 4px and a melt-blue
  sheen spreads across the panel's surface over 600ms. Attention is
  warmth applied to the specimen being examined; the visitor's hand
  thaws what it touches, a few pixels' worth, and the ice takes it
  back when the hand leaves.
- **Structure.** Panels carry a frost layer: an inset box-shadow /
  border-image of `--ice-line` at 10px, plus a sheen layer (`--sheen`
  gradient, opacity 0). Both are the panel's own surface layers,
  `pointer-events: none`, present in the shipped CSS — hover is pure
  CSS; JS is not involved except that the sheen's spread is eased by a
  CSS transition, not the loop.
- **Motion spec.** Pointer enter: frost retreats 10px → 6px and sheen
  opacity 0 → 1 over **600ms `--ease-thaw`**. Pointer leave: frost
  returns over 900ms (refreezing is slower than melting — the theme's
  small physical honesty), sheen fades over 700ms. Focus-within gets
  the identical treatment (keyboard warmth is warmth).
- **States.** Frozen (rest) → warming (600ms) → warmed (held while
  hovered) → refreezing (900ms) → frozen. On touch: the first tap on a
  panel warms it (and does not activate); a tap elsewhere refreezes.
- **Content merge.** The frost is the panel's own edge and the sheen
  is meltwater on its own surface; the text beneath never moves,
  never changes contrast below its audited pairing (the sheen is
  capped at 18% white and is excluded from the text measure's central
  60% by gradient stops).
- **Failure fallback.** No hover capability: panels rest frozen, fully
  legible — the frost edge is translucent and never covers text at
  rest (it lives in the panel's padding zone).
- **Reduced-motion variant.** No melt, no sheen: hover/focus changes
  the panel's outline to 2px `--crevasse-deep`. The affordance
  survives; the weather rests.
- **Performance budget & mobile variant.** Two CSS transitions per
  panel, composited. Mobile: tap-to-warm as above; sheen omitted
  (small panels have no spare surface), frost retreat only.
- **Choreography timeline (v2).** t=0 pointer enter → t=0–600ms frost
  10 → 6px, sheen 0 → 1 → hold → pointer leave → t=0–900ms frost
  returns, sheen gone by 700ms.
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Frost 10px, no sheen | Same |
  | Hover | Warmed at 600ms | n/a |
  | Focus-within | Warmed | Same (external keyboard) |
  | Active | Warmed + §6.9 may fire on cards | First tap warms |
  | Scrolled-past | Frozen (hover states cleared by the loop on exit) | Frozen |
  | Disabled panel | No frost response; panel carries its disabled ruling (§11) | Same |

- **Breakpoint behaviour (v2).** ≥1200px: full spec. 768–1199px: frost
  8px → 5px. <768px: frost 6px → 4px, no sheen.
- **Edge cases & failure modes (v2).** *Pointer skimming a grid of
  specimens:* a 90ms intent delay before warming, so a diagonal path
  doesn't thaw six panels in passing. *Panel containing a form:*
  frost-melt applies to the panel frame only; fields never warm (a
  melting input is a broken input). *Contrast mid-melt:* audited —
  the sheen's gradient excludes the text zone (above).
- **Accessibility spec (v2).** Decorative response; the panel's
  interactive children keep their own focus rings, which are never
  replaced by the frost state. Nothing is conveyed by the melt that
  is not also in the text.
- **Tokens consumed (v2).** `--ice-line`, `--sheen`, `--ease-thaw`,
  `--dur-melt` (600ms), `--dur-refreeze` (900ms).

### 6.9 Hairline crack click

- **What & why.** Clicking a specimen card cracks one fine hairline
  across its corner — an SVG stroke drawing in 250ms and staying.
  Selection feedback as ice responding to pressure: the mark is left
  on the sample itself, not on a UI layer beside it. A cracked card is
  a *marked* card — the glaciologist's pencil tick, in the ice's own
  language.
- **Structure.** Each specimen card (§6.15) carries one hidden SVG
  hairline path across its top-right corner (a 3-segment jagged line,
  authored per card from a seed so no two cracks are identical, each
  ≤ 64px long, confined to the corner's padding zone — a crack may
  never cross text). The path ships undrawn (`stroke-dashoffset` full)
  only under the JS-armed class; without JS the card's selected state
  is its stamped label (below).
- **Motion spec.** Trigger: click/tap on the card's mark control (the
  whole card is not the target; §6.15 defines the control). Draw:
  **250ms `--ease-crack`**, dashoffset → 0. The crack stays for the
  session; clicking again does not crack further (one mark per
  specimen — a card cracked twice is a card destroyed, and the theme
  is about preservation). Marking also stamps the card's apparatus
  line: `MARKED — SAMPLE 214` in Inter 13px.
- **States.** Unmarked → cracking (250ms) → marked (terminal for the
  session; persists in `sessionStorage` so a reload keeps the party's
  marks). Disabled card (a withdrawn specimen): no crack; its ruling
  is §6.15's.
- **Content merge.** The crack is on the specimen, in its corner, and
  the apparatus line it stamps is the specimen's own catalogue entry.
  The state (marked) is content the visitor created about the content.
- **Failure fallback.** No JS: the mark control is a real checkbox-
  styled button whose checked state shows the `MARKED` stamp without
  the crack; the crack is the enhancement, the stamp is the record.
- **Reduced-motion variant.** The crack appears fully drawn instantly,
  with the stamp. The mark survives; the fracture rests.
- **Performance budget & mobile variant.** One stroke animation per
  click — free. Mobile: identical; the corner zone is 56px so the
  crack stays clear of the card's title at phone widths.
- **Choreography timeline (v2).** t=0 click → t=0–250ms hairline draws
  corner-inward → t=250ms stamp fades in (150ms) → the marked count in
  the section's apparatus line (§6.11's family) increments.
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Unmarked | No crack, control at rest | Same |
  | Hover (control) | §6.8 warms the card | n/a |
  | Focus (control) | Ring + card warms | Same |
  | Active (click) | 250ms draw | 250ms draw |
  | Marked | Crack + stamp, terminal | Same |
  | Disabled | No crack; withdrawn ruling | Same |

- **Breakpoint behaviour (v2).** All breakpoints: full spec; crack
  length scales 64px / 56px / 48px down the breakpoints.
- **Edge cases & failure modes (v2).** *Rapid double-click:* the
  second click is ignored while cracking and after marked (one-mark
  law enforced in the handler, not by hope). *Card re-rendered by a
  filter (§6.15):* marked state is keyed by sample number, so a marked
  specimen returns marked. *Print:* cracks do not print; the `MARKED`
  stamp does.
- **Accessibility spec (v2).** The control is a real `<button>`
  with `aria-pressed` and the label "Mark sample 214"; the crack is
  `aria-hidden` decoration; the stamp is real text. State is never
  carried by the crack alone.
- **Tokens consumed (v2).** `--ice-line`, `--ease-crack`,
  `--dur-crack` (250ms), `--crevasse-deep` (stamp ink on light cards).

---

### Page-family elements

### 6.10 Melt-line hero image

- **What & why.** The hero's image — the glacier's face, the crevasse
  field, the core on its table — is revealed by a horizontal melt-line
  mask wiping clear from top to bottom: the image thaws downward, the
  way a frozen face clears from its sunlit top. It is the page's one
  masked reveal, paired with §6.1 so the hero's words and picture are
  freed by the same weather.
- **Structure.** The hero `<img>` (real `alt`, real content) under a
  mask layer: a `--snow` veil with a 24px melt-edge gradient at its
  lower boundary, clipped by an inset that JS arms (veil height 100%
  → 0). Without JS there is no veil.
- **Motion spec.** Trigger: §6.1's thaw start. **1800ms
  `--ease-thaw`**, the veil's inset animating top-down; the melt-edge
  leads, the image sharp beneath it from first exposure (the image
  itself never blurs — §6.1 owns the hero's blur). A 2000ms watchdog
  removes the veil outright.
- **States.** Veiled (JS-armed only) → melting → clear (terminal,
  veil removed from the DOM).
- **Content merge.** The veil is snow on the image's own face; the
  melt-line is the image's own thaw, synchronised with the headline's.
- **Failure fallback.** No JS / watchdog: image fully visible. The
  image is never `opacity: 0` in any shipped state.
- **Reduced-motion variant.** No veil; the image stands clear.
- **Performance budget & mobile variant.** One clip animation.
  Mobile: duration 1400ms, melt-edge 16px.
- **Choreography timeline (v2).** t=0 thaw starts → veil inset begins
  → t=900ms the image's upper half clear → t=1800ms fully clear, veil
  removed → §6.1 completes at 2500ms; the picture thaws faster than
  the words, as faces do.
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Clear (shipped) | Clear |
  | Melting | 1800ms | 1400ms |
  | Clear | Terminal | Terminal |
  | Hover / focus | No change | n/a |
  | Disabled / no-JS | Clear | Clear |

- **Breakpoint behaviour (v2).** ≥1200px: 1800ms, 24px edge.
  768–1199px: 1600ms, 20px. <768px: 1400ms, 16px.
- **Edge cases & failure modes (v2).** *Slow image load:* the veil
  waits for the image's `load` or the 2000ms watchdog, whichever
  first — a melt-line over an empty frame is a white page lying about
  weather. *Image fails:* the hero's fallback ground (`--firn` with
  the headline) stands; no veil is armed.
- **Accessibility spec (v2).** The image's `alt` is available from
  first paint; the veil is a visual mask only, `aria-hidden`.
- **Tokens consumed (v2).** `--snow`, `--ease-thaw`, `--dur-meltline`
  (1800ms), `--watchdog-hero` (2000ms).

### 6.11 Sample counters

- **What & why.** Where the page counts — samples catalogued, metres
  drilled, bubbles measured — the figures count in Inter tabular when
  their section thaws, and every figure is either counted from the DOM
  or supplied by the publisher as data. The glacier does not invent
  its inventory: a counter that performs a number nobody measured is
  the theme's one unforgivable prop.
- **Structure.** Counter elements carry `data-count-source="dom"` (the
  loop counts matching specimens in the section) or
  `data-count-value` with a `data-count-unit` (publisher data, stated
  in the section's apparatus line). The final figure is the shipped
  text; JS rewinds to 0 only on sections below the fold it will drive.
- **Motion spec.** Trigger: the section's thaw (§6.4) completes.
  Count over **1100ms**, in 40ms stepped increments (an instrument
  ticks; it does not sweep), easing out via `--ease-settle` applied to
  the step sizes. No overshoot, ever — a glacier counter that bounces
  past its true value has lied twice.
- **States.** Final figure (shipped) → rewound (JS-armed, below fold)
  → counting → final (terminal).
- **Content merge.** The figures are the section's own data — its
  specimens, its metres — counted where they stand.
- **Failure fallback.** Shipped figures stand. Watchdog 1400ms forces
  the final figure.
- **Reduced-motion variant.** Figures stand at final values.
- **Performance budget & mobile variant.** Text writes at 40ms steps
  only while counting. Mobile: identical.
- **Choreography timeline (v2).** Thaw ends → t=0 count starts →
  steps at 40ms, growing then shrinking increments → t=1100ms exact
  final figure → still.
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Final figure | Final figure |
  | Counting | 1100ms stepped | Same |
  | Done | Terminal | Terminal |
  | Hover / focus | No change | n/a |
  | Disabled / no-JS | Final figure | Final figure |

- **Breakpoint behaviour (v2).** All breakpoints identical.
- **Edge cases & failure modes (v2).** *DOM count changes after a
  filter (§6.15):* counters recount on filter change, instantly (no
  ceremony for a correction). *A `data-count-value` with no apparatus
  source line:* build error, gate failure (§10) — unsourced figures
  are refused at build, not at runtime.
- **Accessibility spec (v2).** The counting is visual only; the
  element's accessible text is the final figure at all times (the
  rewind is `aria-hidden` theatre over a visually-hidden true value,
  or the element is `aria-hidden` with a static twin — builder picks
  one pattern per build, consistently).
- **Tokens consumed (v2).** `--ease-settle`, `--dur-count` (1100ms),
  `--step-count` (40ms).

### 6.12 Refreeze page transition + skeleton

- **What & why.** Leaving a page in this theme is a refreeze: a frost
  veil descends over the viewport — snow glare at 92% with the
  melt-edge at its hem — the route changes beneath it, and the new
  page stands already thawed under the lifting veil. Loading is the
  veil held: a frosted panel with the new page's era skeleton in
  `--melt` blocks. Both rituals are the theme's own weather doing the
  two jobs every site must do; a spinner would be a foreign object
  from a warmer climate.
- **Structure.** A fixed `.refreeze` veil (snow ground, 24px melt-edge
  gradient at its bottom, the destination's era label in Spectral at
  its centre). Skeleton: the destination's panel geometry in `--melt`
  at 40% — stratum blocks, a heading bar, text bars at the measure —
  shown only inside a client-side navigation that owns its watchdog.
- **Motion spec.** Veil descends **420ms `--ease-thaw`**, route swaps
  at full cover, veil lifts **520ms `--ease-thaw`** (refreezing is
  quicker to arrive than to leave). Hard abort at **2500ms**: any veil
  still covering at 2500ms is removed and the destination shown
  plainly. Skeleton panels hold a 1600ms `--ease-drift` opacity breath
  (40% → 55%) while loading; any panel unresolved at 2000ms flattens
  to plain `--firn` — no picture stays abstract if the machinery
  fails.
- **States.** Idle → covering → covered (swap) → lifting → idle.
  Skeleton: loading → flattening (2000ms watchdog) → resolved.
  Browser back/forward: no veil (the browser's gesture rules).
- **Content merge.** The veil is the page's own snow; the skeleton is
  the destination's own strata geometry — layout shift is zero by
  construction, and the era label on the veil is the destination's
  real name.
- **Failure fallback.** Plain navigation. The veil enhances links it
  can intercept and never breaks one it can't (modified clicks,
  new-tab, external links bypass it entirely). Server-rendered pages
  ship resolved; skeletons exist only inside owned client fetches.
- **Reduced-motion variant.** No veil: instant navigation with the
  destination's era label flashed in the rail for 600ms — the change
  of stratum is marked, not performed.
- **Performance budget & mobile variant.** One fixed layer, transforms
  only. Mobile: descend 360ms, lift 440ms, melt-edge 16px.
- **Choreography timeline (v2).** t=0 link activation → veil descends
  → t=420ms full cover, route swaps, destination at scroll top,
  already thawed → t=940ms veil lifted, focus moved to the
  destination's `<h1>` → t=2500ms abort watchdog (normally never
  reached).
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Idle | No veil | No veil |
  | Transitioning | 420 + 520ms | 360 + 440ms |
  | Loading (skeleton) | Melt blocks, 1600ms breath | Same |
  | Hover | Link hovers per §11; veil has none | n/a |
  | Focus | Keyboard activation fires the same veil; focus lands on destination H1 | Same |
  | Disabled / no-JS | Plain navigation | Same |

- **Breakpoint behaviour (v2).** ≥1200px: full spec. 768–1199px:
  400/500ms. <768px: 360/440ms, edge 16px.
- **Edge cases & failure modes (v2).** *Slow destination:* the veil
  holds at full cover with its era label joined by the line "THE ICE
  IS THICK HERE — STILL DRILLING" after 3000ms (the theme's loading
  voice, §12), and the abort law still applies at the router's own
  timeout — the theme never traps a visitor inside weather. *Same-page
  anchors:* no veil; anchors jump (instant under reduced motion,
  smooth otherwise per §5).
- **Accessibility spec (v2).** During the veil the outgoing page is
  `inert`; on lift, focus moves to the destination `<h1>`
  (tabindex −1) with a polite announcement "Descended to: [era/page
  name]". Skeletons carry `aria-busy="true"` until resolved.
- **Tokens consumed (v2).** `--snow`, `--melt`, `--firn`,
  `--ease-thaw`, `--dur-veil-down` (420ms), `--dur-veil-up` (520ms),
  `--abort-veil` (2500ms).

### 6.13 Era index navigation (the core log)

- **What & why.** Navigation in this theme is the core log: the rail's
  column of depth ticks, one per era, each tick a link lettered with
  the era's name, its depth band and its age range — the log a
  glaciologist keeps beside the core. It belongs because a glacier
  site is not navigated by a menu; it is consulted by depth.
- **Structure.** A `<nav class="core-log">` in the left rail (≥1200px)
  or a horizontal strip under the top bar (<1200px): items generated
  from the same era data as §6.3/§6.7 (name, `data-depth-from/to`, age
  range), each a real anchor to its era's section. The current era's
  tick fills with its stratum colour and its lettering takes the
  stratum's audited ink — currentness is shown by ice, never by a
  pill.
- **Motion spec.** Scrollspy (shared IntersectionObserver): the
  current tick's fill sweeps in over 300ms `--ease-settle` as its era
  takes the stage. Hover/focus: the tick's depth figures warm to
  `--crevasse-deep` (light rail) over 180ms. Clicking a tick scrolls
  to the era (smooth, or instant under reduced motion) — the readout
  (§6.2) follows the scroll, so the instrument and the log agree at
  every moment.
- **States.** Items: rest → hover/focus (figures warm) → current
  (stratum fill). The log as a whole inherits the readout's states.
- **Content merge.** The items are the page's real eras with their
  real depths — generated from era data, so adding an era adds a tick,
  because the log *is* the page's index, not a marketing menu.
- **Failure fallback.** Plain anchor list; the scrollspy is the only
  JS behaviour and its absence leaves the first tick marked current by
  the server where known.
- **Reduced-motion variant.** Fills and warms are instant.
- **Performance budget & mobile variant.** Observer-driven, free.
  Mobile: the strip scrolls horizontally; ticks keep name + age range
  (depth figures move into the era headings, which carry them anyway).
- **Choreography timeline (v2).** Era takes the stage → outgoing
  tick's fill drains (300ms) as the incoming tick's fill sweeps —
  the two overlap for one beat, like passes of the lamp.
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Ink ticks, hollow | In the strip |
  | Hover | Figures warm 180ms | n/a |
  | Focus | As hover + ring | Same |
  | Current | Stratum fill, audited ink | Same |
  | Scrolled-past | Log scrolls with the rail's fixed position; ticks for passed eras stay filled at 40% (the drilled part of the log) | Same |
  | Disabled | An era with no content is absent — never a greyed tick | Same |

- **Breakpoint behaviour (v2).** ≥1200px: rail column. 768–1199px:
  top strip, two rows if needed. <768px: one-row horizontal strip,
  scrollable, current tick scrolled into view by the spy.
- **Edge cases & failure modes (v2).** *More than 9 eras:* the log
  groups unpinned sections under their nearest era tick — a log with
  20 ticks is a spreadsheet, not a core log. *Era names longer than
  22ch:* truncate in the rail with the full name in `aria-label` and
  in the era's own heading.
- **Accessibility spec (v2).** Real `<nav aria-label="Eras in this
  core">`; current tick carries `aria-current="true"` (updated on era
  change only). Tick targets ≥ 44px tall on touch, ≥ 28px on desktop.
- **Tokens consumed (v2).** The five anchors, `--crevasse-deep`,
  `--ease-settle`, `--dur-tick` (300ms).

### 6.14 The surface (hero composition)

- **What & why.** §6.1 and §6.10 specify the hero's two thaws; this
  element specifies the composition they happen in: the first screen
  is the surface of the glacier — snow glare field, the headline, its
  era label ("SURFACE — THE PRESENT DAY"), the hero image below the
  fold line of the first screen's lower third, and the readout at its
  zero. The composition's job is altitude: the visitor must feel they
  are standing *on* the ice, at the top of time, before the descent
  begins.
- **Structure.** First viewport: `--snow` ground; the readout rail at
  0.0m; headline in the measure, left-aligned at the rail's edge; era
  label above it; the standfirst (Inter, 19px) beneath; the hero
  image's top edge just visible at the first screen's foot — the
  crevasse field waiting below the surface, which is the composition's
  one invitation to scroll. No buttons on the surface: the descent is
  the call to action, and it is made by scrolling, not clicking.
- **Motion spec.** §6.1 (headline) and §6.10 (image) run their
  ceremonies; the standfirst thaws with §6.4's grammar at 700ms
  (it is near the centre at load); nothing else moves. The surface's
  stillness after the thaw is specified — a surface that fidgets is a
  billboard.
- **Choreography timeline (v2).** t=0 load → t≈600ms thaws begin →
  t=1800ms image clear → t=2500ms headline thawed → the surface is
  still; the first scroll starts the descent (§13).
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest (post-thaw) | Still surface | Same |
  | Hover | §6.8 may warm the image panel | n/a |
  | Focus | First tab stop is the era index's first tick (§6.13) | Same |
  | Scrolled-past | The surface is gone; the descent owns the page | Same |
  | Disabled / no-JS | Thawed surface, image clear | Same |

- **Content merge.** Everything on the surface is the present day's
  own: today's date in the era label's apparatus line, the headline of
  the descent to come, the glacier's face in the image. The hero sells
  nothing but the core itself.
- **Failure fallback.** The disabled state: a printed surface.
- **Reduced-motion variant.** Static surface, readout as ruler.
- **Breakpoint behaviour (v2).** ≥1200px: as specced. 768–1199px: the
  image's visible sliver at the foot grows to 20vh (tablet surfaces
  are shorter). <768px: the image moves fully below the fold; the
  surface is headline + standfirst + readout bar only.
- **Edge cases & failure modes (v2).** *Short viewport (<600px
  height):* the standfirst is cut from the first screen (it follows
  immediately below) rather than shrinking the headline — the title's
  size is law (§3), the standfirst's position is not.
- **Accessibility spec (v2).** Landmarks: the era index is the
  `<nav>`, the surface is `<main>`'s first `<section>`; the headline
  is the page's `<h1>`; DOM order is label → headline → standfirst →
  image.
- **Performance budget & mobile variant.** Hero assets ≤ 900KB total
  (§14). Mobile: the single-column surface above.
- **Tokens consumed (v2).** `--snow`, `--abyss`, `--crevasse-deep`.

### 6.15 Specimen cards

- **What & why.** The card in this theme is a cut specimen: a segment
  of core on the light table — stratum-tinted ground, its sample
  number and depth in the apparatus line, a Spectral title, an Inter
  standfirst, and one action (mark it, §6.9, or read it). Cards are
  how eras present their evidence in sets; they belong in specimen
  form because in this world there are no floating tiles, only samples
  that were drilled, cut, numbered and laid out for examination.
- **Structure.** `<article class="specimen">`: header apparatus row
  (sample number, depth band — both real), title, standfirst (≤ 2
  lines), optional duotone image (§6.10's grammar at card scale:
  scale-in-frame 1.05 → 1 on entry, no veil), footer row with the mark
  control (§6.9) and the read link. Cards sit in their era's panel, in
  the era's measure; a card never migrates strata.
- **Motion spec.** Entry: the card thaws with its section (§6.4) — no
  separate entrance. Hover: §6.8's frost-melt on the card's frame.
  The image settles 1.05 → 1 over 700ms `--ease-settle` as the card
  centres, once.
- **States.** Rest → thawing (with section) → thawed → warmed (hover)
  → marked (§6.9, terminal per session). A withdrawn specimen (its
  data superseded) is not greyed: its apparatus line is stamped
  `SUPERSEDED — SEE SAMPLE n` in `--crevasse-deep` and its read link
  points to the successor; the card remains legible, because the core
  log does not erase.
- **Content merge.** Every field is the specimen's own catalogue data:
  number, depth, title, finding. A card for a specimen with no image
  uses its stratum's bubble-trail panel (§6.6) as its visual — the
  grammar holds without inventing photography.
- **Failure fallback.** Static card, image settled, fully legible.
- **Reduced-motion variant.** No settle, no melt: hover changes the
  frame outline (§6.8's variant).
- **Performance budget & mobile variant.** Cards inherit §6.6's bubble
  caps if they carry the trail visual. Mobile: one column; the mark
  control stays ≥ 44px.
- **Choreography timeline (v2).** Section thaws → card legible →
  card centres → image settles (700ms) → rest. Marking follows §6.9's
  timeline.
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Thawed, frozen edge | Same |
  | Hover | §6.8 warm | n/a |
  | Focus-within | §6.8 warm + child ring | Same |
  | Active (mark) | §6.9 crack | §6.9 crack |
  | Marked | Crack + stamp | Same |
  | Superseded | Stamp + successor link | Same |
  | Disabled / no-JS | Static card | Same |

- **Breakpoint behaviour (v2).** ≥1200px: up to 3 across inside an era
  panel (density law §4 permitting — deep eras: 1 across). 768–1199px:
  2 across. <768px: 1 across.
- **Edge cases & failure modes (v2).** *Missing image:* bubble-trail
  visual (above) — never a grey box, never a stock glacier silently
  substituted. *Long title:* clamps at 2 lines; the full title is the
  read link's accessible name. *Filtering a specimen set:* filtered
  sets recount their §6.11 counters instantly and keep §6.9 marks by
  sample number.
- **Accessibility spec (v2).** One read link per card (its title);
  the mark control is separate and labelled (§6.9). The apparatus row
  is real text in reading order. Image `alt` is the specimen's
  finding, or `alt=""` when the title already states it — chosen per
  build, consistently.
- **Tokens consumed (v2).** The stratum tokens, `--ease-settle`,
  `--crevasse-deep`, `--dur-settle-img` (700ms).

### 6.16 The confession form (conversion)

- **What & why.** Every glacier site in this theme ends by asking the
  visitor to add their own layer: subscribe to the core log, register
  for the expedition, submit a sample. The form is a **fresh snow
  layer** — a `--snow` panel laid over the deep ground at the page's
  foot, its fields ruled like the core log's lines, its submit a seal
  pressed into wax-blue ice. Conversion here is deposition: the
  visitor's layer goes on top of the record, dated today, and the
  confirmation says so.
- **Structure.** `<form class="confession">` on a snow panel: heading
  in Spectral ("Add your layer"), fields as ruled lines (label above
  in the apparatus voice, input on a 1.5px `--crevasse-deep` rule,
  Inter 17px), one consent line set as a log entry with a square
  checkbox that fills `--deep` when checked, and the submit as a
  **seal button**: a 64px circle in `--deep` bearing a snowflake-cut
  core glyph, labelled in text beside it ("Press the seal").
- **Motion spec.** Focus: the field's rule thickens 1.5px → 2.5px and
  warms to `--deep` over 200ms `--ease-settle`. Error: the rule turns
  `--crevasse-deep` dashed and the error note appears beneath in the
  desk voice (§12) — errors in this theme are corrections entered in
  the log, never alarms. Submit: the seal presses (scale 1 → 0.94,
  160ms `--ease-crack`, ring impresses) and holds while sending; on
  success the panel is **covered by its own layer**: a fresh snow
  sheet slides down over the form (500ms `--ease-thaw`) bearing the
  confirmation as a log entry with today's real date and the entry's
  number (server-issued or DOM-counted, §6.11's law).
- **States.** Rest → focus (rule warms) → error (dashed rule + note,
  persistent until corrected) → pressing → covered-by-confirmation.
  A failed send uncovers the form with every field intact and the
  desk note "NOT ENTERED — THE LINE FAILED. YOUR LAYER IS KEPT
  BELOW." (§12).
- **Content merge.** The form is the record's newest layer and says
  so; its fields are the log's columns (name, direction, the layer
  itself). The confirmation is a log entry, not a thank-you page.
- **Failure fallback.** A working HTML form: labels, inputs, submit —
  posts without JS; errors re-render server-side in the same desk
  notes. The seal is decoration around a real text-labelled button.
- **Reduced-motion variant.** No press scale, no covering sheet: the
  confirmation replaces the form instantly, as a log entry appearing
  in the log.
- **Performance budget & mobile variant.** Transitions on focus/submit
  only. Mobile: the seal grows to 76px (a thumb presses it), fields
  full-width, inputs at 17px (no iOS zoom).
- **Choreography timeline (v2).** t=0 submit → seal presses (160ms)
  → response → snow sheet covers (500ms) → confirmation entry's date
  stamp thuds in the §6.11 grammar → the readout (§6.2) gains the line
  `+1 LAYER TODAY` in its apparatus row (the record grew).
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Ruled blank lines | Same |
  | Hover (seal) | Seal sheen +6% | n/a |
  | Focus (field) | Rule thickens/warms 200ms | Same |
  | Error | Dashed rule + desk note | Same |
  | Pressing | Seal at 0.94, fields inert at full contrast | Same |
  | Confirmed | Snow sheet + log entry | Same |
  | Disabled / no-JS | Working form | Same |

- **Breakpoint behaviour (v2).** ≥1200px: panel at the era measure,
  name/direction sharing one ruled line-pair. 768–1199px: one column.
  <768px: 76px seal, centred label beneath.
- **Edge cases & failure modes (v2).** *Double submit:* the pressed
  state disables the seal until resolution. *Long message field:*
  ruled lines extend to 10 lines, then the field scrolls internally —
  a layer thicker than its sheet is where the fiction yields. *The
  visitor's layer must never be lost:* no error path clears a field
  (§10, blocking gate).
- **Accessibility spec (v2).** Real `<label>`s; hints are
  `aria-describedby`, never placeholders (a blank ruled line is the
  invitation). Errors linked via `aria-describedby`, announced by a
  polite live region on submit failure only. Contrast: labels abyss
  on snow 14.49:1; error notes `--crevasse-deep` on snow 5.9:1. Touch
  targets: field rows 48px; seal 64–76px.
- **Tokens consumed (v2).** `--snow`, `--deep`, `--crevasse-deep`,
  `--ease-settle`, `--ease-crack`, `--ease-thaw`, `--dur-press`
  (160ms), `--dur-cover` (500ms).

### 6.17 Bedrock footer (the colophon of the core)

- **What & why.** The descent ends at bedrock: a full-width `--abyss`
  block that never pins, never parallaxes, never thaws — after a page
  of slow weather, bedrock's stillness is the final content statement.
  It carries the colophon: who drilled this core, on what scale, in
  what year — including the **declared depth–age model** (§1's law
  made printable) and the true counts of the page (eras, specimens,
  metres) as the log's closing entry.
- **Structure.** `<footer>` in abyss: the closing line in Spectral
  ("BEDROCK — 300.0 M — 12,000 YEARS"), the colophon in Inter 13px
  (drilled by, published by, the scale statement: "Depth measured from
  the surface of this page. Ages by the model: 11.4 years per metre to
  40 m, logarithmic below, 300 m = 12,000 years BP."), the legal line,
  and one link — "Return to the surface" — which scrolls to the top
  (the ascent is instant under reduced motion, a 1200ms
  `--ease-settle` rise otherwise; the only upward journey the theme
  permits itself).
- **Motion spec.** One motion only: as the footer enters, a single
  hairline (§6.9's grammar, in `--ice-line`) draws across its top edge
  over 800ms `--ease-settle` — the drill's last mark. Nothing else in
  the footer ever moves; §6.6's bubbles do not extend below the last
  era.
- **States.** Rest (still) — the footer has no hover, active or
  scrolled-past theatre; its link behaves as §11's text link.
- **Content merge.** The colophon's facts are the page's real facts —
  the same scale the readout ran on, the same counts the counters
  counted. The footer is where the instrument's calibration is
  published.
- **Failure fallback.** Static footer; the hairline ships drawn
  without JS.
- **Reduced-motion variant.** Hairline pre-drawn; the return link
  jumps instantly.
- **Performance budget & mobile variant.** One 800ms draw, once.
  Mobile: the colophon stacks; the scale statement stays complete
  (it may never be truncated — it is the page's calibration).
- **Choreography timeline (v2).** Footer top enters → hairline draws
  800ms → stillness.
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Still, drawn | Same |
  | Hover / focus (link) | §11 link treatment | Same |
  | Disabled / no-JS | Static | Static |

- **Breakpoint behaviour (v2).** All sizes: colophon at the abyss
  measure (46ch); the closing line scales per §3's H3.
- **Edge cases & failure modes (v2).** *A build whose scale differs:*
  the colophon's statement is generated from the same data attributes
  as §6.2 — the printed calibration cannot drift from the running
  instrument.
- **Accessibility spec (v2).** A real `<footer>`; the closing line is
  text, the hairline `aria-hidden`. Snow on abyss is 14.49:1.
- **Tokens consumed (v2).** `--abyss`, `--snow`, `--melt`,
  `--ice-line`, `--ease-settle`.

### 6.18 The unthawed page (404)

- **What & why.** A wrong address in this theme is a depth with no
  core: the drill went down and found nothing recorded. The 404 is a
  short page at a declared depth — the readout stands at the
  requested path's would-be depth (computed from the path's length on
  the declared scale, and labelled as exactly that conceit) — with the
  log's entry: "NO CORE AT THIS DEPTH."
- **Structure.** One screen: the readout (static, at the computed
  depth), the Spectral line "Nothing is preserved here.", two lines
  in the desk voice (§12's empty voice), and the era index (§6.13) as
  the way back — the log of depths that *do* hold cores.
- **Motion spec.** One motion: on load, the headline thaws (§6.1's
  grammar at 1200ms — even the empty page is freed from ice). Nothing
  else moves.
- **States.** Rest (thawed, still). The index links behave per §6.13.
- **Content merge.** The computed depth is the actual requested path,
  honestly labelled; the index is the site's real eras. No mascot
  penguin, no illustrated crevasse (§9).
- **Failure fallback.** A static page with links; nothing to fail.
- **Reduced-motion variant.** Headline printed sharp.
- **Performance budget & mobile variant.** One 1200ms thaw. Mobile:
  the readout as top bar (§6.2's variant).
- **Choreography timeline (v2).** t=0 load → headline thaw 1200ms →
  still.
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Thawed, still | Same |
  | Hover / focus | §6.13 link treatment | Same |
  | Disabled / no-JS | Static | Static |

- **Breakpoint behaviour (v2).** All sizes: one screen at the abyss
  measure; the index becomes the strip below 1200px (§6.13).
- **Edge cases & failure modes (v2).** *A path that nearly matches an
  era:* the desk adds one line — "NEAREST CORE: [era] — [depth]" with
  its link — only when the match is real (slug similarity computed
  server-side); a guessed suggestion is forbidden (§9's
  invented-facts rule).
- **Accessibility spec (v2).** The `<h1>` is "Nothing is preserved
  here." — meaning first, theatre second. The readout's conceit is
  labelled in its hidden twin ("a depth assigned to this address for
  the log's sake").
- **Tokens consumed (v2).** `--snow`, `--abyss`, `--crevasse-deep`,
  `--ease-thaw`.

---

## 7. Page application map

**Home — the descent itself.** The page *is* one core: surface
(§6.14), the pinned strata (§6.3) for the principal eras, unpinned
sections (§6.4) for supporting material, the science section with the
core diagram (§6.7), the confession form (§6.16) as the final layer,
bedrock (§6.17). Most Glacier Confession sites are one descent deep;
depth is added by drilling *more cores* (sibling descents), never by
bolting on chrome.

**Listing — a tray of specimens.** An index of samples, expeditions or
records is a tray of specimen cards (§6.15) laid in depth order —
never alphabetical, never by popularity: the tray is read down the
core. Filters, where they exist, are log queries (§11) that re-lay the
tray; §6.11 counters recount instantly.

**Detail — one era, full depth.** A single era or specimen at full
measure: its heading with dates (§3's law), its specimens, its own
mini-readout frozen at its depth band (the live readout's static
sibling). The detail page does not re-run the descent; it *is* a
segment, examined on the table.

**About — the drilling party.** The institute, the team, the method:
told as the surface camp — who drills, with what instruments, funded
by whom — in the firn's register, ending with the method's own
colophon (the scale statement belongs here too, not only in §6.17).

**Contact / conversion equivalents.** §6.16 only. A transaction that
needs a cart, a payment matrix or a booking grid leaves the theme at
that step: hand off to a plainly designed transactional flow and
return to a Glacier Confession confirmation layer (§6.16's success
state). Dressing a payment form as an ice layer is the theme's most
dangerous costume (§9).

**The unthawed page (404).** §6.18, everywhere, unchanged.

**Sibling cores.** A site with more material does not lengthen this
descent past §13's length contract; it drills a second core. Sibling
descents share the surface furniture (rail, readout grammar, colophon
scale — redecalred per core if its maxima differ) and are indexed
from the surface as separate cores in the log: "CORE A — THE LONG
RECORD · CORE B — THE VOLCANO YEARS". Each core is a complete descent
with its own bedrock; a visitor never falls out of one core into
another mid-stratum. Cross-references between cores are apparatus
lines on specimens ("the matching layer is Sample 112, Core B"), the
way real core logs cite each other — never a tab bar.

**Print.** The printed core: all eras in sequence at full opacity on
their stratum tints (or white, where the printer's owner prefers —
the dates and depths are the content, the tints are the courtesy),
the ruler printed beside them, bubbles at the uniform 8px (§6.5).

## 8. Worked examples

### 8.1 The hero — a polar institute's surface

*The commission: a national ice-core programme's home page; the
descent runs from today's surface to the 12,000-year bedrock of its
oldest core.*

- **The composition (§6.14).** First screen: snow field, the rail
  readout at `DEPTH 0.0 M · AGE 0 YEARS BP · SURFACE`, the era label
  "SURFACE — THE PRESENT DAY" with today's real date in its apparatus
  line, the headline "What the ice remembers" in Spectral 300 at
  0.12em tracking, the standfirst: "One core, drilled at Dome C,
  holds 12,000 years of air. Scroll to descend through it." The hero
  image's top — the crevasse field at dawn — shows at the screen's
  foot.
- **The ceremonies.** t≈600ms: §6.1's thaw and §6.10's melt-line
  begin together. The image clears by t=2400ms (its melt-line ends at
  1800ms from thaw start); the headline's blur reaches 2px at
  t≈2000ms — the words findable while the picture is already clear,
  faces before words — and completes at t=3100ms wall-clock (600 +
  2500), tracking settled at 0.06em. The standfirst thaws at its
  700ms grammar. By t≈3.2s the surface is still.
- **Scroll timeline.** 0–40px: nothing moves (the surface holds).
  40px onward: the readout leaves zero — depth 0.4m, age 5 years —
  and the strata pin engages. The visitor who never scrolls has still
  received the whole surface: today's date, the promise, the face of
  the glacier.

### 8.2 Mid-page — the firn era and its specimens

*The commission: §8.1's descent, third era — "The Firn, 1850–1950" —
the industrial century, where the bubbles first carry smoke.*

- **Entry (§6.3).** The visitor scrolls through the second boundary
  band: the melt panel crossfades out as the firn-tinted panel rises
  its 12px; at band 50% the readout's era name swaps to "THE FIRN"
  and its age passes 100 years BP. The era label has slid down the
  stage's edge; the H2 stands with its dates: "1,850 – 1,950 CE ·
  76 – 174 YEARS BP · DEPTH 6.7 – 15.3 M" — all three printings of the
  band agreeing, because all three derive from §6.2's scale.
- **The specimens.** Three specimen cards (§6.15) in the firn measure:
  Sample 041 "The first soot", Sample 043 "A summer of ash, 1883",
  Sample 047 "Lead, rising". Their lists use 11px bubbles (§6.5's firn
  row). The section's counter (§6.11) has counted the tray: "3 SAMPLES
  ON THIS TRAY". The visitor hovers Sample 043: its frost edge melts
  back 4px over 600ms (§6.8); they click its mark control: the
  hairline cracks across its corner in 250ms (§6.9) and its apparatus
  line stamps `MARKED — SAMPLE 043`.
- **What the visitor feels.** A century arriving as weather, evidence
  laid out at hand height, and two small physical responses — warmth
  under the pointer, a crack under the click — that make the samples
  feel handled, not browsed.
- **Failure rehearsed.** The same era with the loop killed mid-visit:
  the crossfade's watchdog completes to the firn panel within 1000ms;
  the un-thawed second specimen card forces legibility at its 1200ms
  watchdog; the counter stands at "3 SAMPLES ON THIS TRAY" without
  having counted. The visitor notices, at most, that this era arrived
  plainly. Plainly is always available; fog is never the price of a
  broken loop.

### 8.3 Conversion — the confession form

*The commission: §8.1's page foot — "Receive the core log", a
quarterly letter from the programme.*

- **Arrival.** Below the abyss era, the snow panel of §6.16 lies on
  the deep ground: "Add your layer." Fields: name, direction (email —
  labelled "Your direction", the postal word, with the apparatus hint
  "FOR THE LOG"), and one consent log-line. The seal button, 64px in
  deep ice, labelled "Press the seal".
- **Interaction timeline.** The visitor tabs to the direction field:
  its rule thickens and warms over 200ms. They type an address with
  no @ and tab on: the rule turns dashed crevasse-deep and the desk
  notes beneath, in Inter 13px: "THE DIRECTION WILL NOT CARRY — CHECK
  THE ADDRESS." They correct it; the note clears, the rule re-warms.
  They press the seal: 160ms compression, the ring impresses; the
  post takes a breath; the snow sheet covers the form over 500ms
  bearing the entry: "ENTERED IN THE LOG — No. 1,208 — [today's real
  date]. Your layer lies on the surface. The next letter descends in
  March." The readout gains `+1 LAYER TODAY`.
- **Failure rehearsed.** If the post fails, the sheet never covers;
  the seal unpresses; the desk notes "NOT ENTERED — THE LINE FAILED.
  YOUR LAYER IS KEPT BELOW." and every character the visitor typed is
  still in its field (§10, blocking gate 7).

## 9. Anti-slop — what makes THIS theme look cheap

1. **The screensaver glacier.** Stock ice photography, a parallax
   hero, generic fade-ups, and ages typed as decoration. *Cure:* §1's
   law — one declared scale, computed ages, and the theme's own
   ceremonies (§6.1–§6.9) or nothing.
2. **Blur without a timer.** A thaw that depends on the loop, the
   observer or the visitor's patience, stranding a section in fog.
   *Cure:* the hard timers — 2500ms (§6.1), 1200ms (§6.4) — are
   blocking gates, not suggestions.
3. **Disc bullets in the deep.** Ordinary list markers, or bubbles
   that stay 14px to the bottom. *Cure:* §6.5's table, audited per
   stratum (§10).
4. **Bubbles over text.** The ambient layer drifting through the
   reading measure. *Cure:* margins and gutters only (§6.6), caps
   enforced.
5. **A percentage progress bar.** Any bar, ring or % anywhere.
   *Cure:* the readout is the progress (§6.2); percentages are
   refused by §5.
6. **Invented ages.** "8,000 years" chosen for roundness; era bands
   that disagree between heading, readout and diagram. *Cure:* one
   scale, three printings, the §10 agreement audit.
7. **Fast ice.** 200ms fade-ups, bouncy counters, a marquee of
   partners. *Cure:* §5's durations are floors as much as ceilings;
   the gate times the ceremonies.
8. **The costume checkout.** A payment flow wearing snow. *Cure:*
   §7's hand-off ruling.
9. **Penguins.** Mascots, illustrated crevasses, clip-art cores.
   *Cure:* the theme's imagery is the glacier's face, its specimens
   and its diagram — evidence, not illustration.
10. **Abyss clutter.** Cards, badges and banners filling the deep
    layer. *Cure:* §4's density law — at most 3 elements in the
    abyss viewport.
11. **A bold headline.** Spectral 700 display type. *Cure:* §3's
    first law; light is the display weight.
12. **Refreezing on scroll-back.** Sections re-blurring when the
    visitor returns upward. *Cure:* one-shot thaws (§6.4); the
    ascent is a review, not a second winter.
13. **Two ink flips.** A mid-page light section dropped into the deep
    half for "variety", flipping text polarity a second time.
    *Cure:* §2's strata table — one flip, between crevasse and deep,
    and the sequence never repeats a step.
14. **The chatty readout.** The age readout decorated with messages
    ("You're halfway to the ice age!"). *Cure:* the readout is an
    instrument (§6.2); its only words are depth, age, era and
    `BEDROCK`. Encouragement is a warmer theme's job.

## 10. Quality gate

**Blocking — all must pass.**

1. **Scale agreement audit.** Pick three scroll positions; the
   readout's depth/age, the active era's printed band, and §6.7's
   diagram band for that era agree exactly, all derived from the
   declared model. Any hand-typed age anywhere = fail.
2. **Thaw-timer test.** With the rAF loop artificially stalled, the
   hero headline is legible at 2500ms and every armed section at
   1200ms past its trigger.
3. **JS-off test.** The full page reads top to bedrock with no JS:
   eras stacked, readout as ruler, form working, bubbles at table
   sizes.
4. **Bubble audit.** Measure the bullet diameter in one list per
   stratum against §6.5's table: 14 / 11 / 9 / 7 / 6 / 5px (±0.5px).
5. **No-percentage test.** Grep the build for progress bars, rings
   and % progress readouts: zero.
6. **Contrast audit.** Every text pairing at rest in both colour
   schemes against §2's figures — including abyss text never on deep
   (1.53:1) and crevasse never as text (3.01:1).
7. **Form-loss test.** Force a failed submission: every field's
   content survives, the desk note (§6.16) shows, the seal unpresses.
8. **One-mark test.** A specimen card cannot be cracked twice; marks
   persist across reload (session) and across filtering, keyed by
   sample number.
9. **Density test.** Count elements in the abyss viewport: ≤ 3.
10. **Reduced-motion test.** With `prefers-reduced-motion`, no blur,
    pin, rise or veil exists anywhere; the ruler stands beside the
    eras.

**Standard — should pass; two failures allowed with a note in the
build log.** 11. Ceremony timings within ±10% of §5/§6 (thaw 2500ms,
section thaw 900ms, melt 600ms, crack 250ms). 12. Bubble caps (14 per
panel, 40 per page) verified in the DOM at the deepest scroll point.
13. The readout reaches bedrock exactly at the footer's top edge.
14. Counters' figures trace to DOM counts or apparatus-cited data.
15. The colophon (§6.17) scale statement matches the running model's
data attributes character-for-character in substance. 16. Focus
forcing works: tabbing into a fading or armed element renders it
fully legible instantly. 17. Print renders the full core in sequence.
18. The five-second test: a first-time visitor, shown the surface for
five seconds, can say what the page is (a descent through ice time)
and how to begin (scroll).

## 11. Component inventory

Every component a real site in this theme needs, with its treatment.
Refusals are listed with their in-theme replacements — a refused
component is never simply omitted; the need it served is re-housed.
The inventory's governing principle is the theme's physics: components
that *interrupt* (modals, toasts, popovers) are refused because ice
does not interrupt; components that *accumulate* (logs, trays,
apparatus lines) are native because accumulation is what a core is.
When a product requirement arrives that this inventory does not name,
the builder's test is one question — does it interrupt, or does it
accumulate? Interruptions are re-housed as strata, sections or desk
notes before they are built; accumulations are given a depth, a
sample number and a place in the log. A component that can be neither
re-housed nor accumulated does not belong on a glacier site, and the
honest answer to the requirement is §7's hand-off ruling, not a
costume.

| Component | Treatment in this theme |
|---|---|
| Primary button | The seal (§6.16's grammar at button scale): deep-ice disc or ruled rectangle, press = 160ms `--ease-crack` compression. One per view. |
| Secondary button | A ruled log line: text on a 1.5px rule, hover warms the rule to `--deep` (200ms). Never a filled pill. |
| Text link | Inter, underlined with the stratum's hairline; hover thickens the line; visited links take `--crevasse-deep`. |
| Era navigation | The core log (§6.13). No other nav pattern exists on the page. |
| Breadcrumbs | **Refused.** Replaced by the readout itself: depth and era name state where the visitor is, in the theme's own units. |
| Cards | Specimen cards (§6.15). No other card pattern. |
| Lists | Bubble-bulleted (§6.5) for findings; ruled log lines for indexes. |
| Tables | Core-log tables: Inter tabular, ruled rows in the stratum hairline, depth column always first. Dense tables are refused below the firn (§4). |
| Form fields | Ruled lines (§6.16). Boxed inputs are refused — snow has no boxes. |
| Checkbox / radio | Log-entry squares that fill `--deep`; radios are log lines whose rule warms when chosen. Toggle switches **refused** (a glacier has no switches; a setting is either entered in the log or it is not). |
| Select | **Refused.** Replaced by a short log list of ruled choices (≤ 7) or, beyond 7, by the era-index pattern (§6.13) applied to the choice set. |
| Modal | **Refused.** Replaced by an unpinned section that thaws in place (§6.4) — a specimen examined where it lies. |
| Toast | **Refused.** Replaced by a desk note entered in the nearest apparatus line (§12's voice), persistent until superseded. |
| Tooltip | **Refused.** Replaced by the apparatus line beneath the thing itself — captions in this theme are printed, not hovered into existence. |
| Badge | **Refused.** Status is a stamped apparatus word (`MARKED`, `SUPERSEDED`, `BEDROCK`) in `--crevasse-deep`, never a coloured chip. |
| Pagination | **Refused.** Replaced by depth: "Further down" is a link to the next era (§6.13's pattern); numbered pages belong to warmer themes. |
| Tabs | **Refused.** Eras are sequential by physics; parallel panels of content are re-housed as successive strata. |
| Accordion | **Refused** in the strata. In the firn and above only, a "core break" disclosure: a ruled line that opens the segment beneath it with §6.4's thaw. |
| Alert / error | A desk note (§6.16's error grammar): dashed rule + Inter note in §12's voice. Never red — this theme has no red; error is crevasse-deep, the colour of a crack in the ice. |
| Progress | The readout (§6.2). All other progress UI refused (§10, gate 5). |
| Skeleton / loader | The refreeze skeleton (§6.12). Spinners refused permanently. |
| Search | A log query: a ruled field (§6.16's grammar) whose results re-lay the specimen tray (§7) in depth order. |
| Footer | Bedrock (§6.17). No link columns; a core has a colophon, not a sitemap. |

## 12. Copywriting voice

Two voices, never swapped. **The Glacier** (Spectral) speaks rarely
and only in era names, headlines and the closing line — short,
declarative, unhurried, with dates attached. **The Desk** (Inter) —
the drilling party's log-keeper — speaks everywhere else: labels,
apparatus, errors, confirmations. The Desk is precise, dry, and
never impressed by itself.

**Headline style.** A claim about what the ice holds, with its span
implied or stated. ✓ "What the ice remembers." ✓ "The century the
smoke began." ✗ "Discover our amazing glacial journey!" (exclamation,
breathlessness, no dates). ✗ "Welcome to our website" (the surface
does not welcome; it states).

**Label style.** Apparatus: uppercase, tracked, factual. ✓ "DEPTH
142.6 M" ✓ "SAMPLE 043 — FIRN" ✗ "You're almost there!" (the readout
is an instrument, not a coach).

**Error voice (the Desk, entering a correction).** ✓ "THE DIRECTION
WILL NOT CARRY — CHECK THE ADDRESS." ✓ "NOT ENTERED — THE LINE
FAILED. YOUR LAYER IS KEPT BELOW." ✗ "Oops! Something went wrong."
✗ "Invalid input" (a log does not say "invalid"; it states what will
not carry).

**Empty voice.** ✓ "NO CORE AT THIS DEPTH." ✓ "Nothing is preserved
here." ✗ "Looks like you're lost!" — the visitor is not lost; the
ice is simply empty there, and the log says so.

**Confirmation voice.** A log entry, numbered and dated. ✓ "ENTERED
IN THE LOG — No. 1,208 — [date]. Your layer lies on the surface."
✗ "Awesome! You're in!" 

**Fixed strings (verbatim, do not paraphrase).** The readout's
bedrock line: `BEDROCK`. The form's failure note: "NOT ENTERED — THE
LINE FAILED. YOUR LAYER IS KEPT BELOW." The slow-transition line:
"THE ICE IS THICK HERE — STILL DRILLING". The 404's entry: "NO CORE
AT THIS DEPTH."

**Banned words.** amazing, discover (as a CTA), journey (as a
metaphor for using the site), seamless, dive in, explore (as a CTA),
oops, invalid. **Owned words.** depth, age, before present, sample,
stratum, thaw, entered in the log, preserved, bedrock.

**The bubble table (referenced by §6.5).** Surface (0–6.7m): 14px /
12px gap. Firn (6.7–15.3m): 11px / 10px. Melt (15.3–60m): 9px / 8px.
Crevasse (60–140m): 7px / 7px. Deep (140–240m): 6px / 6px. Abyss
(240–300m): 5px / 5px. Depth bands are the declared model's defaults;
a build that redeclares its maxima re-derives its bands and prints
the new table in its colophon.

## 13. Full-page scroll choreography map

Eleven beats, top to bedrock. The emotional arc: brightness and air
at the surface; gathering density and darkness; stillness at the
bottom.

1. **The surface (0–40px).** Thaws complete (§6.1, §6.10); the page
   is still and bright. The visitor feels altitude.
2. **First drilling (40px–first boundary).** The readout leaves zero;
   the strata pin engages. Motion the visitor caused — the descent is
   theirs.
3. **Era I → II boundary.** First crossfade (§6.3); the ground cools
   from snow to firn. The lamp passes.
4. **The firn.** Bubble lists at 11px; first specimen tray; §6.11
   counters tick. Evidence begins.
5. **Era II → III boundary.** Melt tones; the measure narrows 68 →
   62ch. The world is quietly tightening.
6. **The science section.** §6.7's diagram draws the whole descent so
   far — the visitor sees the core they are inside.
7. **Era III → IV boundary.** Crevasse tones; bubble lists at 7px;
   panels carry §6.6's rising air in their margins.
8. **The deep ice.** Measure 54ch; density 5 elements per viewport;
   hovers melt frost (§6.8) — the visitor's warmth matters more down
   here, against more ice.
9. **Era IV → V boundary.** Deep to abyss; the last crossfade is the
   slowest-feeling because the readout's logarithmic leg makes the
   ages leap while the colours barely change.
10. **The abyss.** 46ch, ≤ 3 elements: a heading, a paragraph, one
    specimen. The confession's oldest sentence, alone in the dark.
11. **Bedrock.** The readout prints `BEDROCK`; §6.17's hairline draws;
    the confession form's snow panel (§6.16) lies just above the
    footer as the final, newest layer — the visitor's, if they
    choose. Stillness.

**Timing across the whole descent.** At a reading pace of roughly
one viewport per 4 seconds, the pinned strata (480vh) take about
80 seconds to drill; the unpinned sections below them, another
60–90 seconds. Total descent: 2½ to 3 minutes — deliberately the
length of a short museum film, because that is the attention this
theme is built for. A build whose descent runs under 90 seconds has
compressed its eras too thin to confess anything (§4's density law
is the usual cause); a build over 5 minutes has buried its form
(§6.16) below the depth at which visitors still have a layer to give.
The choreography map is therefore also a length contract: if a draft
page's beats time out far from these figures, the page is the wrong
length for the theme, and the cure is to cut or add *eras* — never to
speed up the ceremonies, whose durations (§5's ledger) are physics,
not pacing choices.

**Reverse pass.** Scrolling up reverses the readout and crossfades
exactly; thaws, draws, counters and cracks do not replay (one-shot
law). The ascent reads as reviewing the core on the table — the
segments are already cut.

**Jump-scroll catch-up.** An anchor jump or a fast fling lands with:
readout snapped, the landed era fully opaque, everything above
thawed and drawn, counters at final figures. No ceremony is owed to
a visitor who teleports; the instruments simply read true.

## 14. Whole-page performance budget

- **Assets.** Total page ≤ 1.6MB; hero ≤ 900KB (image ≤ 700KB,
  fonts ≤ 120KB subset — Spectral 300/400/500 + Inter 400/500/600);
  the core diagram and all hairlines are inline SVG (≤ 30KB total).
  No JavaScript library is required; the loop, observers and handlers
  are ≤ 18KB minified.
- **Frame budget.** The shared loop's per-frame cost ≤ 2.0ms on a
  mid-range phone: at most two crossfading panels, ≤ 40 bubble
  transforms, two readout text writes (only when rounded values
  change). No layout reads inside the loop — section offsets are
  cached and refreshed on resize only.
- **Long tasks.** No task > 50ms after load; the thaw's filter work
  is compositor-side. Counters and draws are staggered so no two
  ceremonies share a frame budget peak.
- **Cut order (when the budget is exceeded).** 1. §6.6 bubble sway,
  then the bubble layer itself (freeze at seeded positions). 2.
  §6.10's melt-edge gradient (veil becomes a plain inset wipe). 3.
  §6.1's displacement layer (blur + tracking only). 4. §6.3's rise
  (crossfade becomes opacity-only). 5. §6.8's sheen (frost retreat
  only). **Never cut:** the thaw timers, the readout, the era labels'
  dates, the form's loss-protection, any fallback.
- **Mobile budget.** Pin length 320vh (§6.3), bubble caps 24/page,
  hero image ≤ 420KB with a dedicated small source.
- **How the budget is verified.** Frame cost is measured, not
  asserted: a mid-range Android device (the build log names the exact
  handset or throttling profile), CPU throttled 4×, scrolling the
  full descent at a steady fling while the loop's per-frame time is
  sampled over 300 frames — median ≤ 2.0ms, p95 ≤ 3.5ms. The thaw
  ceremonies are measured on the same profile with the performance
  timeline: no long task over 50ms from thaw start to thaw end. A
  build that passes on a desktop and was never measured on the
  throttled profile has an *opinion* about its budget, and §10's gate
  treats it as unmeasured, which is to say unpassed.

## 15. Build-order checklist

1. Print the static core first: all eras stacked on their strata, the
   ruler readout, the form working, bedrock — fully legible, no JS.
2. Declare the scale: depth/age maxima and the mapping function in
   §6.2's data attributes; generate era bands, §6.5's bubble table
   and §6.17's colophon statement from the same data.
3. Set the palette tokens (§2) and type scale (§3); audit pairings.
4. Build the layout: rail, measures per stratum, density per §4.
5. Build the core log (§6.13) from era data; verify anchor order =
   depth order.
6. Build specimen cards (§6.15) and bubble lists (§6.5).
7. Build the confession form (§6.16) with its error and
   loss-protection paths; test the failure path before the success
   path.
8. Add the shared rAF loop (lerp 0.10); wire the live readout (§6.2).
9. Add the pinned strata (§6.3) over the static stack; verify the
   no-JS stack is untouched beneath.
10. Add thaws (§6.1, §6.4, §6.10) with their hard timers; stall-test
    the loop.
11. Add the core diagram draw (§6.7) from era data.
12. Add frost-melt (§6.8) and hairline cracks (§6.9) with session
    persistence.
13. Add counters (§6.11), rising bubbles (§6.6) within caps, and the
    refreeze transition (§6.12).
14. Add the reduced-motion variant end-to-end (ruler, static eras, no
    blur) and the print stylesheet.
15. Run §10's gate — blocking items first, signed by a non-builder —
    and only then let the theme ship.

A note on the order: steps 1–7 build the page a visitor could use
with every later step deleted, and steps 8–14 add weather in the
order the visitor meets it — instruments before ceremonies, ceremonies
before ambience. This is deliberate, and it is the theme in miniature:
the record first, the thaw second, the rising air last. A build that
starts with the bubbles has begun at the decoration and will spend
the rest of its budget defending that choice; a build that starts
with the printed core can stop after any step and still hand over a
glacier — colder at each stop, but whole. That is the deepest sense
in which this theme is honest: its fallback state and its finished
state are the same object at different temperatures, and everything
the motion system adds is weather over a record that was already
true before the weather arrived.
