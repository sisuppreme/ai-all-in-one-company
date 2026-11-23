# 47. Fjord Stillness — Expanded (v1 + v2)

> Expansion of theme #47 from `themes-026-050.md`, written directly to
> the full standard: the v1 10-part structure plus the v2 deepening
> layers (per-element choreography timelines, state matrices, breakpoint
> behaviour, edge cases, accessibility specs and token lists; per-theme
> component inventory, copywriting voice, three worked examples, scroll
> choreography map, performance budget, build-order checklist).
> Identity preserved exactly: the same concept, the same five palette
> anchors, the same two typefaces, the same nine signature elements —
> deepened, never redesigned — plus nine page-family elements.

## 1. Concept & world

A fjord does not sparkle. Below a cliff of wet rock, the water is black
and green at once, and it moves so little that movement itself becomes
an event: one ring from one stone, widening for a long time, then the
surface closed again. This theme builds a website out of that water.
The page is a single body of cold dark water. Content does not appear
on it — content **surfaces** in it, rising 40px on a heavy buoyant ease
(§6.3), trailing a faint reflection that sharpens only as the section
comes to rest (§6.4). Between chapters there is nothing: long pauses of
empty dark water (§4), and once, a whole pinned screen holding a single
line of copy (§6.7). The only instrument on the page is a plumb line in
the margin (§6.6), descending as you read, printing your depth in
metres — the sailor's gauge, not the browser's scrollbar dressed up.

It is not Scandinavian-minimal. Minimalism is an absence; this is a
presence — depth, cold, and time. A minimal page is empty because
nothing was put there. A Fjord Stillness page is empty the way a fjord
is empty between two headlands: the emptiness is measured, it has a
depth figure attached, and something is rising through it. The theme's
whole craft is the difference between those two emptinesses, and every
rule below exists to defend it.

**The theme's one law: the depth is measured, or the depth is not
printed.** Every metre figure on the page is computed from two declared
numbers — the page's total depth in metres, fixed in the build survey
from the real place the site is about (the fjord arm below the Quiet
House at Fjellstrand is 214 m deep, and the home page's plumb line
therefore runs 0–214 m), and the visitor's actual scroll fraction.
Depth = round(total metres × scroll fraction), computed once in the
shared loop and printed identically by the plumb line (§6.6), the depth
figures (§6.15) and the footer's final sounding (§6.16) — three
printings of one measurement, and a disagreement between any two of
them is a blocking defect. The silence figure obeys the same law from
the other direction: it is the visitor's real elapsed dwell, counted
only while the tab is visible, never typed, never rounded up. A build
that invents a depth, a temperature or a duration has not decorated the
page; it has lied in the page's only instrument, and §10's gate fails
it. A second, smaller law rides with it: **one ripple per cause.** The
surface breaks once on load (§6.1) and once per deliberate click
(§6.9), and at no other time. Ambient ripple loops are the exact moment
this theme becomes a screensaver.

**Best-fit sites.** Places and practices whose product is genuinely
stillness or depth: a fjord-side retreat house or sauna; a cold-water
swimming club; a freediving school (its depth figures are real by
profession); a small observatory or dark-sky reserve; a grief
counsellor's single-practitioner site; a tea house; a watchmaker who
makes one watch a year; a deep backlist publisher; a research station
publishing one long report. The common trait: the offer improves when
nothing competes with it, and the numbers the site prints — depths,
durations, temperatures, distances — are facts of the place, available
to be measured rather than invented.

**When NOT to use it.** Anything that must feel fast, abundant or
urgent: marketplaces, news, sales events, dashboards, social products,
children's products, any page whose conversion depends on comparison.
Do not use it for a brand that merely wants to look calm while behaving
loudly — the theme will expose the mismatch, because its pauses are
long enough for a visitor to notice a pop-up-shaped hole in them (§6.7
forbids overlays outright). Do not use it where content must be scanned
quickly: surfacing is a ceremony of 1400ms (§6.3), and a visitor in a
hurry experiences this theme as a locked door. And do not use it on a
site with nothing true to measure — a Fjord Stillness page with
invented depths is worse than a loud page, because it is quiet about a
lie.

**The world, kept.** The site's furniture is nautical and spare: a
waterline, a plumb line, soundings, chapters named like reaches of the
fjord, figures in metres and minutes. Nothing on the page is decorated.
The two licensed ornaments are the reflection beneath a headline (§6.4)
— which is the headline's own, not an addition — and the sheen on the
water (§5), which is the light the place actually has. Everything else
that moves is either surfacing, sounding, or the single ripple.

## 2. Palette

Five anchors, all taken from the original entry, plus a closed derived
list. The dark grounds are the page; the light tones exist only as
type, hairlines and reflections on that water, and — once — as the
printed page of §6.18's inverse ruling and the print stylesheet. There
is no light mode. A fjord at noon is still black water; the theme's
answer to brightness is the snow line, used as type, not as ground.

| Token | Hex | Role | Usage ratio |
|---|---|---|---|
| `--fjord` | `#0C1417` | Fjord black-green. The deep ground: hero panel, pauses, footer bottom, every chapter's rest state | ~62% of page area |
| `--deep` | `#1E2E33` | Deep water. Raised grounds: cards, form sheet, nav band, skeleton blocks, the pause's single-line field | ~26% |
| `--mist` | `#5A737C` | Slate mist. Hairlines, waterline motif, reflections' blur colour, apparatus at display size, disabled states | ~6% |
| `--ice` | `#C7D3D6` | Ice light. Body text on dark grounds, secondary apparatus, plumb line and its figures | ~4% |
| `--snow` | `#E8EDEE` | Snow line. Headlines, the current depth figure, the pause's single line, focus rings | ~2% |

**Derived tokens (closed list — no others may be introduced):**

| Token | Value | Derived for |
|---|---|---|
| `--mist-light` | `#84A0AB` | Secondary text on dark grounds where `--mist` fails: 6.73:1 on `--fjord`, 5.09:1 on `--deep` (measured) |
| `--slate-deep` | `#3E545E` | Text on light grounds (print sheet, §6.18 inverse block): 6.75:1 on `--snow`, 5.21:1 on `--ice` (measured) |
| `--waterline` | `--mist` at 38% | The waterline hairline (§6.5): present, never structural-looking |
| `--reflection` | `--ice` at 16% | Reflection fill at full sharpness (§6.4); begins at 7% |
| `--sheen` | `--snow` at 5% | The ambient surface sheen (§5); never above 6% |
| `--ring` | `--ice` at 55% | The ripple ring at birth (§6.1, §6.9), fading to 0 |

**Measured contrast (computed for this expansion, WCAG ratio):**

| Pairing | Ratio | Ruling |
|---|---|---|
| `--snow` on `--fjord` | 15.76:1 | Headlines, the pause line, current depth |
| `--ice` on `--fjord` | 12.16:1 | Body text, primary ground pairing |
| `--ice` on `--deep` | 9.18:1 | Body text on raised grounds |
| `--snow` on `--deep` | 11.90:1 | Card titles, form headings |
| `--mist-light` on `--fjord` | 6.73:1 | Captions, apparatus, meta lines |
| `--mist-light` on `--deep` | 5.09:1 | Captions on raised grounds |
| `--mist` on `--fjord` | 3.70:1 | **Never body text.** Display ≥28px, hairlines, reflection colour, disabled labels only |
| `--mist` on `--deep` | 2.80:1 | **Graphical only** — lines and fills, never characters |
| `--fjord` on `--snow` | 15.76:1 | Print stylesheet and §6.18's inverse block |
| `--slate-deep` on `--snow` | 6.75:1 | Body text wherever a light ground is unavoidable |

**Pairing law.** Text is `--snow` or `--ice` on dark grounds, full
stop; `--mist-light` is the only permitted third voice, and it speaks
only in captions and apparatus. `--mist` never carries a sentence on
either dark ground — at 3.70:1 and 2.80:1 it is a colour for lines,
not letters, and the gate (§10) greps for it. Reflections are exempt
from contrast law because they are not content: the headline they
mirror passes at 15.76:1, and §6.4's accessibility spec forbids the
reflection from entering the accessibility tree at all.

**Dark-mode behaviour.** There is none, and that is a ruling, not an
omission: the page is already the dark. `prefers-color-scheme: light`
changes nothing — the fjord does not invert at the visitor's request,
and a light version of this theme would be a different theme (a lake
in summer, which this library does not contain). What the theme offers
instead is the print stylesheet: on paper, the page prints as
`--fjord` text on `--snow`, reflections and ripples absent, the plumb
line's final depth printed as a sentence in the colophon. A printed
sounding is the theme's only light surface, and it is earned by
leaving the screen.


## 3. Typography

Two faces, as the original entry fixes them: **Spectral** (ExtraLight
200 for display, Light 300 for headings) and **Inter** (Light 300 for
body, Regular 400 for apparatus figures where light strokes would
vanish at small sizes). No third face, no italic display, no bold
anywhere on the page — the theme's emphasis is position and depth,
never weight. A word that needs stress is moved, given water around
it, or set in `--snow` against the body's `--ice`; it is never
thickened.

**Type scale (desktop ≥1200px; root 16px):**

| Role | Face / weight | Size | Line-height | Tracking | Colour |
|---|---|---|---|---|---|
| Display (hero headline) | Spectral 200 | 64px | 1.08 | −0.01em | `--snow` |
| Chapter headline | Spectral 200 | 44px | 1.14 | −0.005em | `--snow` |
| Section heading | Spectral 300 | 28px | 1.25 | 0 | `--snow` |
| Standfirst / lead | Spectral 300 | 21px | 1.55 | 0 | `--ice` |
| Body | Inter 300 | 17px | 1.78 | 0 | `--ice` |
| Caption / meta | Inter 300 | 13.5px | 1.6 | 0.01em | `--mist-light` |
| Apparatus (labels, nav, buttons) | Inter 400 | 12px | 1.5 | 0.14em, uppercase | `--mist-light` |
| Sounding figures (depth, metres) | Inter 400 | 13px | 1.5 | 0.06em, tabular | `--ice`; current depth `--snow` |
| The pause line (§6.7) | Spectral 200 | 30px | 1.4 | 0 | `--snow` |

**Type laws.**

1. **Light is the weight.** Display never exceeds Spectral 300; body
   never exceeds Inter 300 except apparatus and figures at 400, whose
   strokes must survive 12–13px. A build that reaches for SemiBold
   has shouted in a quiet room.
2. **Leading is depth.** Body line-height 1.78 is not generosity, it
   is the medium: lines of text sit in water, and water takes room.
   Below 1.65 the page becomes a document; above 1.9 it becomes a
   poster. Headings tighten as they grow (1.08 at display) because a
   large light face carries its own air.
3. **Figures are tabular and unhurried.** All sounding figures use
   `font-variant-numeric: tabular-nums`; a depth readout whose digits
   change width would jitter, and jitter is noise. Figures never
   animate by rolling or flipping — they crossfade (§6.15), the only
   number-change this theme permits besides §6.8's slow count.
4. **One headline per chapter, one reflection per headline.** The
   reflection (§6.4) belongs to chapter headlines and the hero only.
   Section headings (28px) do not reflect; a page where everything
   reflects is a funfair mirror hall, not a fjord.
5. **Silence is set in Spectral.** The pause line (§6.7), the 404's
   heading (§6.18) and empty-state lines are Spectral 200 at 30px —
   the theme's sentences of consequence are few, and they are all
   set in the display face at reading size, never in apparatus
   capitals. Apparatus shouts in this theme's terms; consequence
   speaks quietly.

**Breakpoint type behaviour.** 768–1199px: display 52px, chapter
headline 38px, body 17px/1.75. <768px: display 40px, chapter headline
32px, standfirst 19px, body 16.5px/1.72, apparatus 11.5px. The pause
line holds 26px on mobile — a sentence that shrinks below reading
size to fit a phone has been edited by the viewport, which this theme
does not permit; instead its measure narrows (§4).

## 4. Layout language

**The water column.** Content lives in a single centred column,
max-width 680px for prose chapters and 1080px for the card and figure
chapters, on an unbroken `--fjord` ground. There are no section
background alternations, no bands, no containers with borders: the
page is one body of water, and a chapter is a reach of it. Raised
grounds (`--deep`) exist only where an object must be handled — a
card, a form, a nav band — never as scenery.

**The pauses are the grid.** Vertical rhythm is not a spacing scale;
it is a sounding chart. Within a chapter, elements breathe at 24px /
48px. Between chapters, the page holds **30–45vh of empty dark
water** — no hairline, no ornament, nothing but depth accumulating on
the plumb line. This is the layout signature and it is non-negotiable:
a build that tightens the inter-chapter pause below 24vh to "fit more
above the fold" has removed the theme's content, because in this
theme the pause *is* content (§6.7 is merely its largest instance).
Density falls with depth: the first chapter may carry a standfirst, a
figure row and a card trio; the last chapters carry one idea each.

**The waterline.** A 1px hairline in `--waterline` recurs at chapter
heads, drawn across the content column only (never full-bleed — a
full-bleed line is a horizon, and horizons belong to §42). It sits
24px above each chapter headline, with the chapter's sounding — its
depth at entry, computed, §6.15's grammar — printed at its right end
in apparatus. The waterline is the surface the chapter broke; §6.5
animates its lift, but its resting presence is typographic, not
decorative.

**The margin instruments.** At ≥1200px the left margin (the column's
1080px field centred, instruments in the outer 160px) carries the
plumb line (§6.6) and nothing else. The right margin is empty by law:
one instrument, one margin. At 768–1199px the plumb line retires to a
compact header sounding (§6.6's breakpoint ruling); below 768px the
margin ceases to exist and the depth lives only in the header figure
and the footer.

**Alignment.** Everything is left-aligned to the column. Centred text
is refused except the pause line (§6.7), which is centred because it
is alone on its screen — centring is the typography of solitude in
this theme, and spending it on a hero headline or a button makes it
worthless where it matters. Buttons and links align left with their
chapters; the form (§6.13) is a left-aligned sheet, not a centred
card.

**Images.** Photographs appear only inside matte black frames (§6.17)
— a `--fjord` mat of 24px (16px mobile) around the image, no border,
no shadow, the image's own reflection beneath it inside the mat.
Images never bleed, never sit edge-to-edge, never carry captions
outside the mat: the caption is printed inside the mat's lower edge,
in `--mist-light`, like a plate line in a book of soundings.

## 5. Full motion system

Five named easings, one shared loop, and a durations ledger that every
element in §6 obeys. Motion in this theme is buoyancy and settling —
nothing snaps, nothing bounces twice, nothing loops except the sheen.

| Token | Curve | Used by |
|---|---|---|
| `--ease-surface` | `cubic-bezier(0.19, 1.08, 0.32, 1)` | Surfacing (§6.2, §6.3): a slow start against depth, a long rise, one soft overshoot of 2px — the bob as a thing breaks the surface — then rest |
| `--ease-settle` | `cubic-bezier(0.33, 1, 0.44, 1)` | Settling: reflection sharpening (§6.4), count-ups (§6.8), card rest (§6.12) |
| `--ease-lift` | `cubic-bezier(0.7, 0, 0.28, 1)` | The waterline lift (§6.5): held, then gone — a mask leaving a surface |
| `--ease-ring` | `cubic-bezier(0.12, 0.58, 0.26, 1)` | Ripple expansion (§6.1, §6.9): fast birth, very long decay |
| `--ease-drift` | `cubic-bezier(0.45, 0.05, 0.55, 0.95)` | The sheen's drift (§5 ambient) and the mirrored underline's brighten (§6.10) |

**The shared loop.** One `requestAnimationFrame` loop, lerp factor
**0.08** — the slowest whole-page settle in the library (only §42's
single approach instrument runs slower, and it drives one object, not
a page). The loop owns: scroll position (smoothed), plumb-line length
and depth figure (§6.6), reflection sharpness values (§6.4), card tilt
(§6.12), sheen phase (§5), and every scrubbed value in §6. No element
runs its own scroll handler; no element writes a style outside the
loop except one-shot transitions (surfacing, lifts, ripples), which
are CSS transitions/animations triggered by class, never by scroll
arithmetic. When the smoothed scroll is within 0.1px of target and no
one-shot is running, the loop sleeps; a fjord at rest spends no
cycles.

**Vocabulary — every motion term, translated or refused:**

- *Scroll-triggered reveals* → surfacing (§6.3): 40px rise, 1400ms,
  one element at a time, 220ms minimum interval between siblings.
- *Scroll-driven / scrubbed animation* → reflection sharpening (§6.4)
  and the plumb line (§6.6): values are pure functions of smoothed
  scroll, reversible without hysteresis, except the depth figure,
  which is a measurement and therefore exact at every frame.
- *Parallax* → one licensed instance: the hero water panel's sheen
  and the frame reflections (§6.17) drift at 0.94× against content.
  Chapter-to-chapter parallax is refused — layers sliding against
  each other is weather, and this water has no weather.
- *Pinned sections* → the long pause (§6.7), 100vh of pin, one line.
  The only pin in the theme.
- *Smooth scrolling* → the loop's 0.08 lerp applied to native scroll
  read-out (the theme never hijacks the wheel; it smooths what it
  *reports and scrubs*, not the visitor's own hand — hijacked scroll
  is a current, and this water is still).
- *Progress indicator* → the plumb line (§6.6). Progress bars are
  refused (§11): a bar fills; a line sounds.
- *Staggered reveals* → surfacing stagger (§6.3), minimum interval
  220ms — the library's slowest stagger, deliberately: things rise
  from depth one at a time because the water lets them.
- *Masked reveals* → the waterline lift (§6.5): a mask leaving, not a
  curtain opening.
- *Blur-to-sharp* → reflection sharpening only (§6.4), blur 6px→2px,
  never on the content itself. Blurring content to sharpen it later
  is a fog machine; this theme's blur lives only in reflections,
  where blur is physically true.
- *Kinetic typography* → refused, with one exception already in the
  theme: headline letters surface in sequence (§6.2's letter rule),
  each trailing its reflection. Letters that dance, stretch or chase
  the cursor are refused by name.
- *Marquee* → refused. Nothing in a fjord travels sideways forever.
  The footer's colophon is still (§6.16).
- *Counters* → §6.8's slow count-ups (3–4s) and §6.15's depth
  figures, crossfaded, never rolled.
- *SVG line-draw* → the plumb line's own extension is a scrubbed
  length, not a draw; the one true draw is the waterline at chapter
  heads on first surface (600ms, §6.5's rest state covers no-JS).
- *Image scale-in-frame* → §6.17: images settle 1.04→1 inside their
  mats over 1200ms `--ease-settle`, reflections scaling in mirror
  beneath.
- *Hover / magnetic / tilt micro-interactions* → mirrored underline
  brighten (§6.10) and card tilt ≤1.2° (§6.12). Magnetic pull is
  refused: nothing in still water pulls.
- *Custom cursor* → refused, per standing rules and per theme: the
  normal system cursor is the only visitor on the surface.
- *Skeleton loading* → §6.14's un-surfaced blocks.
- *Page transitions* → §6.14's surface crossing: a waterline sweep,
  500ms, latest-wins.
- *Ambient loops* → exactly one: the sheen (§5 below). A second
  ambient loop is a second ripple by another name and breaks the
  one-ripple law.
- *Reduced motion* → §6 passim: everything ships surfaced, reflections
  printed at 2px, ripples absent, the pause unpinned. The static
  page is not a lesser page; it is the fjord on a windless morning,
  which is the theme's home weather anyway.

**Ambient: the sheen.** A radial gradient in `--sheen` (never above
5% opacity), roughly 70vw across, drifts across the hero panel and
the pause on a 26s `--ease-drift` cycle, travelling 3vw in x and 1vh
in y, pausing off-screen via the loop's visibility gate. It is light
on water, not a spotlight: it never centres on content, never follows
the pointer, and dies entirely under reduced motion. It is the only
element on the page allowed to move without being asked.

**Durations ledger (theme-wide, binding on §6):** ripple 3000ms
(load) / 2000ms (click); headline surface 1600ms; section surface
1400ms; letter interval 90ms; waterline lift 1200ms; reflection
sharpen scrub window 60vh; count-up 3000–4000ms by magnitude (§6.8);
card tilt settle 900ms; underline brighten 600ms; transition 500ms;
**fallback hard cap 2000ms** — the most patient fallback in the set,
per the original entry, and still a cap: any surfacing not complete
by 2000ms after trigger is set to rest instantly, by watchdog, in
every element that surfaces.


## 6. Signature elements

### 6.1 The single ripple

- **What & why.** On load, one ripple ring expands once from the
  centre of the hero water panel — 0 to 60vw over 3000ms, fading as
  it goes — and never repeats. It belongs because it is the page's
  only announcement: before any content surfaces, the water itself
  acknowledges the visitor's arrival, once, the way a fjord answers
  one dropped stone. Every later stillness on the page is measured
  against this ring; remove it and the quiet has no beginning.
- **Structure.** A single absolutely-positioned `<div class="ripple">`
  inside the hero panel (§6.11), a 2px-bordered circle in `--ring`,
  `border-radius: 50%`, centred on the panel's optical centre (50% /
  42%), `pointer-events: none`, scaled by transform. It ships absent:
  JS creates it after first paint, so no-JS and reduced-motion pages
  never contain the node at all. One node, reused by §6.9 with a
  different origin and duration — the theme owns exactly one ring
  element, as it owns exactly one ripple per cause.
- **Motion spec.** Trigger: load, gated on first paint + 200ms (the
  ring must not race the font swap). Scale 0→1 mapped to 0→60vw
  diameter, 3000ms `--ease-ring`; opacity 0.55→0 across the same
  window, with the fade weighted to the last 60% so the ring reads
  as a ring, not a disc, for most of its life. Border width thins
  2px→1px past 70% progress. It runs once per page load — not per
  session: a reload is a new arrival and earns a new ring; a bfcache
  restore does not re-fire it (the visitor never left).
- **States.** Unborn (no-JS / reduced motion: node absent) → expanding
  → dissolved (node removed from DOM at completion, not merely
  hidden — a hidden ring in the tree is a ripple waiting to be found
  by a screen reader's browse mode or a future bug).
- **Content merge.** The ring expands across the hero panel's own
  surface and passes *behind* the surfacing headline (§6.2 starts at
  t=600ms, while the ring is young) — the announcement and the title
  share one body of water. It carries no content and pretends to
  none; its merge is temporal: it is the reason the headline's
  surfacing reads as a response rather than an entrance.
- **Failure fallback.** If the loop is not alive by first paint +
  1200ms, the ring is never created — a late ripple is worse than
  none, because it would announce an arrival that already happened.
  If the animation is interrupted (tab hidden), it completes on
  return only if elapsed < 3000ms; otherwise the node is removed
  silently. Content is never gated on the ring: the headline
  surfaces on its own clock regardless.
- **Reduced-motion variant.** No ring. The hero opens already still,
  which under reduced motion is not a loss but the correct first
  state: the visitor asked for no disturbance, and the page makes
  none.
- **Performance budget & mobile variant.** One transformed node,
  ≤0.1ms/frame, no layout. Mobile (<768px): diameter caps at 92vw,
  duration 2400ms — a phone's fjord is narrower and the ring reaches
  its shore sooner; the theme admits the smaller water rather than
  letting the ring clip against the panel edge, which would read as
  a UI spinner's rim.
- **Choreography timeline (v2).** t=0 first paint → t=200 ring born
  at panel centre, opacity 0.55 → t=600 headline begins surfacing
  (§6.2) beneath the ring's first third → t=1800 ring at ~44vw,
  border thins → t=3000 ring at 60vw, opacity 0, node removed →
  t=3000+ the surface is closed; the sheen (§5) is the only motion
  left alive.
- **State matrix (v2).** *Rest:* absent. *Hover:* none — the ring is
  not a control and ignores the pointer entirely. *Focus:* none.
  *Active:* none. *Scrolled-past:* if the visitor scrolls before
  t=3000, the ring continues (it belongs to the panel, not the
  viewport) and dissolves on schedule. *Disabled:* n/a. *Touch:*
  identical; touch does not create rings — only §6.9's deliberate
  click does, and a tap on the hero panel is a click (§6.9 rules
  apply, origin at the tap point).
- **Breakpoints (v2).** ≥1200px: 60vw / 3000ms. 768–1199px: 72vw /
  2700ms. <768px: 92vw / 2400ms. Origin follows the panel's optical
  centre at each size (42% height desktop, 38% mobile, where the
  headline block sits higher).
- **Edge cases & failure modes (v2).** *Slow network:* the hero
  panel is DOM and CSS only; the ring waits for first paint, not for
  images (§6.17's frames surface independently). *bfcache:* no
  re-fire (see Motion spec). *Very wide screens (>1920px):* diameter
  caps at 1150px — a ring wider than the water column reads as a
  target, not a ripple. *Panel shorter than 60vw diameter:* the ring
  is clipped by the panel's overflow, which is correct — ripples
  stop at shores.
- **Accessibility spec (v2).** The ring is `aria-hidden`, present in
  no accessibility tree, announced never. It conveys no information:
  everything it "says" (you have arrived) is said by the headline
  itself. Under `prefers-reduced-motion` it does not exist.
- **Tokens consumed (v2).** `--ring`, `--ease-ring`, `--dur-ripple`
  (3000ms), `--ripple-max` (60vw, capped 1150px).

### 6.2 Headline surfacing

- **What & why.** The hero headline rises 40px on `--ease-surface`
  over 1600ms while its faint reflection fades in beneath it (§6.4
  governs the reflection's later sharpening). It belongs because the
  title must come from the same water the whole page is made of — a
  headline that simply *appears* at the top of a fjord page is a sign
  nailed to a cliff. Surfacing is the theme's grammar of arrival,
  and the headline is its first sentence.
- **Structure.** The `<h1>` in final DOM position inside the hero
  panel (§6.11), followed by its reflection node (§6.4's structure).
  The headline ships at rest — translated 0, fully opaque. JS, after
  the loop's first live frame, arms the pre-state
  (`transform: translateY(40px); opacity: 0` via a class on `<html>`)
  and immediately releases it into the transition. Letters: the
  headline's text is wrapped per-letter in `<span aria-hidden>`
  inside an `aria-label`-carrying h1 only when the headline is
  ≤48 characters (the §5 letter rule); longer headlines surface as a
  single body — lettering a long title makes it a parade.
- **Motion spec.** Trigger: load, t=600ms (inside the ripple's first
  third, §6.1). Rise: translateY 40px→0, 1600ms `--ease-surface`,
  including the easing's built-in 2px overshoot at ~82% — the bob.
  Opacity 0→1 across the first 900ms (a thing rising through black
  water is visible before it arrives). Lettered variant: letters
  rise in sequence at 90ms intervals, each letter's own rise 1100ms,
  each trailing a fading reflection copy (§6.4's hero instance);
  total window for a 24-letter headline ≈ 1100 + 23×90 ≈ 3170ms,
  hard-capped by the §5 fallback law at the *element* level: if the
  sequence would exceed 3600ms, the interval compresses to fit —
  the cap is computed, not hoped for. Reflection fade-in: opacity
  0→1 (§6.4's `--reflection` at 7% strength) over the rise's last
  800ms.
- **States.** Submerged (JS-armed pre-state only) → rising → bob
  (overshoot beat) → rested, reflection present at rest sharpness.
  Scrolled-past: the hero is the page top; a visitor who loads and
  immediately scrolls down finds the headline completed instantly on
  return (the surfacing does not perform for an empty room — if the
  hero leaves the viewport mid-rise, the transition is cancelled to
  rest).
- **Content merge.** The headline is the page's actual title — the
  retreat's name and claim, not a slogan layered over a photograph.
  Its reflection is generated from its own text (§6.4), so the
  ornament cannot drift from the content: change the headline and
  the reflection changes, letter for letter.
- **Failure fallback.** Watchdog at trigger + 2000ms (§5's hard cap):
  if the headline is not at rest, classes are removed and it stands
  at rest instantly. No JS: at rest from first paint. Font failure:
  the rise is transform-only and proceeds in the fallback face; the
  fixed hero panel height (§6.11) absorbs the metrics difference.
- **Reduced-motion variant.** The headline stands at rest, reflection
  printed beneath it at its final 2px blur (§6.4's reduced ruling).
  The apparatus line under the standfirst records the state the
  ceremony would have shown only if the build's survey calls for it
  — default: no record line; stillness needs no caption.
- **Performance budget & mobile variant.** One transformed element
  (+ ≤48 letter spans in the lettered variant), compositor-only.
  Mobile: rise shortens to 32px and 1300ms; lettering is cut above
  20 characters (a phone headline wraps, and a wrapped letter
  sequence staggers across lines like dropped stones — the theme
  declines the effect rather than perform it badly).
- **Choreography timeline (v2).** t=0 first paint (headline at rest,
  unarmed) → t=200 ripple born (§6.1) → t=350 loop confirmed alive,
  pre-state armed → t=600 rise begins, opacity leading → t=1500
  opacity complete → t=1850 bob overshoot (+2px) → t=2200 rested;
  reflection at rest sharpness by t=2400 (§6.4). Lettered variant:
  letters begin t=600 at 90ms intervals, reflections trailing each
  by 150ms.
- **State matrix (v2).** *Rest:* at surface, reflection beneath.
  *Hover:* none (the h1 is not a control; if the build makes the
  title a home link, §6.10's underline grammar applies to it, and
  the rise is unaffected). *Focus:* focus landing on the headline
  (tabindex −1 skip target) completes the rise instantly. *Active:*
  n/a. *Scrolled-past:* completed to rest (see States). *Disabled:*
  n/a. *Touch:* identical; first touch anywhere does not interrupt —
  this theme does not punish a hand for arriving early.
- **Breakpoints (v2).** ≥1200px: 40px / 1600ms, lettering ≤48 chars.
  768–1199px: 36px / 1450ms, lettering ≤36 chars. <768px: 32px /
  1300ms, lettering ≤20 chars, reflection gap tightens (§6.4).
- **Edge cases & failure modes (v2).** *Headline longer than the
  cap:* surfaces whole, no letters (see Structure). *Two-line
  headline:* rises as one body; the reflection mirrors both lines.
  *Tab hidden mid-rise:* on return, if elapsed > 2000ms the watchdog
  has already rested it. *Reload mid-rise:* a fresh load is a fresh
  arrival; the ceremony replays in full.
- **Accessibility spec (v2).** The h1 is in the tree at full text
  from first paint; letter spans are `aria-hidden` duplicates inside
  an h1 carrying the full string as its accessible name, so a screen
  reader hears the title once, whole, immediately — never letter by
  letter, never delayed by the rise. The rise is never announced.
  Focus is never moved by the ceremony.
- **Tokens consumed (v2).** `--snow`, `--ease-surface`, `--dur-rise-
  hero` (1600ms), `--rise-hero` (40px), `--dur-fallback` (2000ms).

### 6.3 Buoyant section surfacing

- **What & why.** Every chapter and major section rises 40px into
  place on the same buoyant ease as it enters the viewport,
  staggered one element at a time with long intervals. It belongs
  because it is the theme's verb: content does not appear, it
  surfaces. Reading a Fjord Stillness page is watching things rise
  from depth at the water's pace, and if sections popped, snapped or
  slid, the page would be a document with a dark background, not a
  fjord.
- **Structure.** Each `[data-surface]` element — chapter heads,
  standfirsts, figure rows, card groups, the form — ships at rest in
  final DOM position. An IntersectionObserver (rootMargin −12% top /
  −18% bottom, so surfacing begins as a section genuinely arrives,
  not while it is still a rumour at the screen's edge) arms the
  pre-state and releases it in the same frame the loop confirms; the
  transition is CSS, driven by class, never by scroll arithmetic.
  Within a chapter, surfacing candidates are queued: the chapter
  head first, then its children in DOM order, minimum interval
  220ms, maximum concurrent rises 2.
- **Motion spec.** Rise: translateY 40px→0, 1400ms `--ease-surface`
  (the 2px bob included), opacity 0→1 over the first 800ms. Trigger:
  element's top crosses 82% of viewport height. A section already
  above that line at load (the first chapter below the hero)
  surfaces on the load clock, queued behind the headline (§6.2),
  beginning no earlier than t=1800ms. Scrolling back up never
  re-submerges: surfaced is a permanent state, because a thing that
  has risen from a fjord does not sink when you look away — the
  reverse pass is stillness, and §13's map states it.
- **States.** Unsurfaced-at-rest (no-JS / pre-trigger, fully visible
  — the pre-state exists only between arming and release, a single
  frame's width) → rising → rested. *Scrolled-past:* a section
  flung past at high velocity surfaces instantly without the rise
  (the loop detects target-vs-actual scroll divergence > 40vh in one
  frame and rests everything in the skipped span — a fling is not a
  reading, and the page does not perform ceremonies for water nobody
  watched). *Re-entry:* no replay, ever.
- **Content merge.** The rising element *is* the content — a chapter
  head, a paragraph block, a card — in its final typographic form.
  There is no wrapper, no placeholder, no skeleton shown in its
  place during a normal read (§6.14's skeleton is for load states
  only). The 40px it travels is the depth it rose from; the merge is
  that the animation's distance is the theme's unit of depth at
  section scale, the same unit the plumb line (§6.6) measures at
  page scale.
- **Failure fallback.** Watchdog per element at trigger + 2000ms
  (§5's cap, the most patient in the library and still absolute):
  not rested → rested instantly, class removed. Observer failure
  (very old browser): a scroll listener fallback checks positions
  at loop rate; if that too is absent, everything simply stands at
  rest, which is the shipped state. The design's failure mode is the
  page itself, finished.
- **Reduced-motion variant.** No arming, no rise: everything stands
  surfaced from first paint. Nothing is labelled or apologised for;
  the page is simply already at the surface, which is where reduced
  motion asked to be.
- **Performance budget & mobile variant.** ≤2 concurrent transforms,
  compositor-only, ≤0.3ms/frame loop overhead for the queue. Mobile:
  rise 28px / 1150ms, interval 160ms, concurrent rises 1 — a phone's
  water is shallower and its processor warmer; the ceremony shortens
  rather than stutters. On devices reporting ≤4GB RAM or a
  `save-data` hint, the rise applies to chapter heads only; body
  blocks stand at rest (recorded as a budget cut, §14).
- **Choreography timeline (v2).** Per element: t=0 top crosses 82%
  line → t=0 arm + release (same frame) → t=0–800 opacity completes
  → t≈1150 bob overshoot → t=1400 rested → next queued sibling may
  begin at t≥220. Chapter head's reflection begins sharpening at
  t=1400 (§6.4's window opens as the rise closes).
- **State matrix (v2).** *Rest:* surfaced, still. *Hover:* surfacing
  confers no hover state; the element's own hover grammar (§6.10 /
  §6.12) applies after rest, and a hover during the rise is honoured
  but does not alter the rise. *Focus:* an element receiving focus
  mid-rise (keyboard arrival) completes its rise instantly — focus
  is never asked to chase a moving target. *Active:* n/a.
  *Scrolled-past:* instant rest (see States). *Disabled:* form
  fields surface with their sheet (§6.13) and are focusable
  throughout; the rise never disables input. *Touch:* identical
  triggers; touch scroll velocity feeds the same fling rule.
- **Breakpoints (v2).** ≥1200px: 40px / 1400ms / interval 220ms /
  2 concurrent. 768–1199px: 34px / 1250ms / 190ms / 2. <768px: 28px /
  1150ms / 160ms / 1.
- **Edge cases & failure modes (v2).** *Content taller than the
  design expects:* surfacing candidates are capped at the chapter's
  first six elements; the rest stand at rest — a long chapter
  surfaces its head and its opening, then simply is there, like a
  long reach of water. *Content shorter:* a chapter with one element
  surfaces it alone; the queue never invents intervals. *Anchor
  jump:* the target chapter rests instantly; the loop's fling rule
  covers the span between. *Print:* all at rest (§2's print ruling).
- **Accessibility spec (v2).** Surfacing never removes content from
  the accessibility tree, never changes tab order, and is never
  announced. Pre-state opacity is visual only and lasts one frame
  before release; a screen reader encounters the finished chapter.
  Focus-visible outlines (§11) render above the rise transform.
  Contrast is at rest values from the first frame — opacity animates
  the element as a whole over a ground it already matches, and the
  800ms opacity window is the theme's accepted transit, stated here
  so no builder "fixes" it by fading text over a lighter ground.
- **Tokens consumed (v2).** `--ease-surface`, `--dur-rise` (1400ms),
  `--rise` (40px), `--surface-interval` (220ms), `--dur-fallback`
  (2000ms).


### 6.4 Reflection sharpening

- **What & why.** Beneath every chapter headline (and the hero's,
  §6.2) sits its reflection: the same words, mirrored, blurred,
  faint. As the section settles, the reflection sharpens — blur 6px
  to 2px, scrubbed to scroll. It belongs because it is the theme's
  one licensed ornament and it is physically honest: a reflection
  sharpens as water stills, and the section's settling *is* the
  water stilling. Clarity is earned by rest, and the visitor watches
  it being earned.
- **Structure.** A `<span class="reflection" aria-hidden="true">`
  inside the headline's wrapper, containing a text-identical copy of
  the headline, transformed `scaleY(-1)`, positioned directly beneath
  the headline with a 6px gap (4px mobile), masked by a linear
  gradient (opaque at its top edge — nearest the headline — fading
  to transparent at 72% of cap height, so the reflection drowns
  downward as real reflections do). Fill is `--reflection` (ice at
  16% at full sharpness, 7% at rest-blur). The copy is generated from
  the headline's own text node at build time — never hand-typed, so
  it can never disagree with its headline.
- **Motion spec.** Sharpness is a pure function of smoothed scroll:
  when the parent section completes its rise (§6.3), a 60vh scrub
  window opens; across it, blur goes 6px→2px and fill 7%→16% via the
  shared loop. Fully reversible: scroll back up and the reflection
  softens again — the only element in the theme besides §6.6's line
  that un-happens, because a reflection is a state of the water, not
  an achievement of the reader. At window end it rests at 2px, never
  0: a perfectly sharp reflection is a duplicate headline, and the
  2px floor is what keeps it water.
- **States.** *At load (hero):* fades in at 7% / 6px during §6.2's
  rise, sharpening across the first 60vh of scroll. *Settling:*
  scrubbed values live. *Rested:* 2px / 16%. *Scrolled-past:* rests
  at full sharpness while its section is above the viewport (the
  water behind the reader is still). *Re-entry from below:* softens
  back through the window in reverse, exactly retracing.
- **Content merge.** The reflection is the headline's own text,
  mirrored — it cannot be removed without removing the headline's
  shadow-self, and it cannot be edited separately because it is
  generated. It occupies the headline's own line box territory (the
  wrapper reserves the reflection's height in layout), so it never
  overlays the paragraph that follows: the gap between headline and
  standfirst is the reflection's water, designed in §4's rhythm.
- **Failure fallback.** No JS / loop dead: reflections print at their
  reduced-motion state — 2px blur, 16% — from the stylesheet alone
  (the scrub's *end* state is the CSS default; JS arms the softer
  start). A reflection that never softens is a finished page; a
  reflection that never sharpens would be a smudge, so the default
  is the sharp end.
- **Reduced-motion variant.** Printed at 2px / 16% permanently. The
  scrub is motion, and it is refused; the reflection remains, because
  it is part of the headline's identity, not an animation.
- **Performance budget & mobile variant.** Filter blur on a
  headline-sized layer is the theme's most expensive regular paint;
  budget ≤0.8ms/frame for one live reflection, and the loop only
  scrubs the reflection whose window is open — all others are static
  layers. Mobile: the scrub window shortens to 45vh, blur range
  5px→2px (small screens resolve less blur before it reads as
  damage), and reflections are cut entirely on ≤4GB devices (the
  headline stands alone; recorded in §14's cut order, never silently).
- **Choreography timeline (v2).** Relative to section rest (§6.3
  t=1400): t=1400 window opens at blur 6px / 7% → across the next
  60vh of smoothed scroll, blur and fill interpolate linearly with
  scroll fraction (the loop's lerp smooths the hand, not the
  mapping) → window close: 2px / 16%, layer released to static.
  Hero instance: window opens at load + 2400ms (§6.2's rest).
- **State matrix (v2).** *Rest:* 2px / 16%. *Hover:* none — hovering
  a headline does not touch its reflection (attention is not wind).
  *Focus:* a focused headline (skip-target) sets its reflection to
  rest sharpness instantly — a keyboard visitor is owed the settled
  state, not a scrub they cannot perform. *Active:* n/a.
  *Scrolled-past:* rest sharpness. *Disabled:* n/a. *Touch:*
  scrubbed by touch scroll identically; no touch-specific state.
- **Breakpoints (v2).** ≥1200px: window 60vh, gap 6px, blur 6→2px.
  768–1199px: window 52vh, gap 5px, blur 5.5→2px. <768px: window
  45vh, gap 4px, blur 5→2px; reflection height capped at one line —
  a two-line headline on mobile reflects its first line only, the
  mask drowning the rest (stated here so no builder centres a
  two-line mirror and calls it a pond).
- **Edge cases & failure modes (v2).** *Headline edited in CMS:*
  the reflection regenerates from the text node at build/render;
  a stale reflection is a build error the gate greps for (§10).
  *Very long headline (3 lines):* reflection shows the first two
  lines, mask-drowned — the cap is by line count in CSS, not by
  character surgery. *Filter unsupported (ancient browser):* the
  reflection renders at 16% with no blur — fainter water, still
  water; the page does not fall back to hiding it.
- **Accessibility spec (v2).** `aria-hidden="true"`, `user-select:
  none`, never focusable, never in the reading order. It is exempt
  from contrast law as a duplicate of text that passes at 15.76:1
  (§2's ruling). Screen readers hear the headline once.
- **Tokens consumed (v2).** `--reflection`, `--mist`, `--ease-settle`
  (release easing), `--blur-far` (6px), `--blur-near` (2px),
  `--reflect-gap` (6px).

### 6.5 Waterline lift

- **What & why.** As each section surfaces, a horizontal waterline
  mask lifts off it — the surface line crossing the content and
  rising away over 1200ms, like something breaking the surface of
  the water it was under. It belongs because surfacing (§6.3) moves
  the content; the lift is what the content moves *through*. Without
  it, sections rise in a void; with it, every arrival has a surface
  to break, and the theme's central physical fact — there is a top
  to this water, and things come up through it — is performed once
  per chapter.
- **Structure.** A `<div class="waterline-mask">` overlaying the
  section's box, ground `--fjord` (matching the page, so the mask
  reads as water, not as a panel), with its bottom edge carrying the
  1px `--waterline` hairline. It ships translated −100% (already
  lifted — the finished state is the DOM state). JS arms it to
  translateY(0) only in the same frame it arms the section's
  surfacing pre-state (§6.3), so the mask and the rise are one
  gesture. `pointer-events: none` always.
- **Motion spec.** Trigger: the section's surfacing trigger (§6.3).
  The mask holds for the rise's first 300ms (the section is still
  deep), then lifts: translateY 0→−100% of section height over
  1200ms `--ease-lift`, the hairline edge leading. The lift finishes
  100ms after the rise (1400ms) completes — the surface leaves last,
  as it should: first the thing, then the water closing over where
  it was is wrong way round; the line lingers a breath after the
  section rests, then goes. One lift per section per page load;
  never on re-entry.
- **States.** Lifted (default, invisible) → armed (covering, one
  frame) → holding (300ms) → lifting (1200ms) → lifted (removed
  from the layer tree; the node remains but translated out and
  `visibility: hidden` after transition end, so it can never
  repaint). *Scrolled-past at speed:* fling rule (§6.3) lifts it
  instantly with its section.
- **Content merge.** The mask is the section's own water: it covers
  exactly the section's box, its hairline is §4's waterline motif at
  the section's head, and its colour is the page ground itself. It
  is not a curtain with branding on it; it carries the chapter's
  sounding at its right end in apparatus (the same computed figure
  §6.15 prints), so even the mask is an instrument while it lasts.
- **Failure fallback.** The mask ships lifted. If JS arms it and
  then dies, the §6.3 watchdog's rest also forces the mask's lift
  class — one watchdog guards both, stated here so no builder wires
  them separately and strands a covered section. Hard cap: mask
  fully lifted by trigger + 2000ms, unconditionally.
- **Reduced-motion variant.** The mask is never armed. Sections
  stand surfaced (§6.3's ruling) and the waterline exists only as
  §4's resting hairline at chapter heads — the motif without the
  gesture.
- **Performance budget & mobile variant.** One transform on a
  section-sized layer, ≤0.4ms/frame, ≤1 lifting at a time (the
  surfacing queue serialises it). Mobile: lift duration 950ms, hold
  200ms; on ≤4GB devices the mask is cut with §6.3's body-block
  ruling — chapter heads keep it, inner blocks never had it.
- **Choreography timeline (v2).** t=0 section trigger → t=0 mask
  armed (covering) + rise armed → t=0–300 hold (rise underway
  beneath) → t=300–1500 mask lifts, hairline leading → t=1400 rise
  rests → t=1500 mask gone, layer released → the section's
  reflection window (§6.4) is already 100ms into its scrub.
- **State matrix (v2).** *Rest:* lifted, invisible. *Hover:* none —
  the mask ignores the pointer (`pointer-events: none`) and a hover
  during the lift changes nothing. *Focus:* focus entering the
  section lifts the mask instantly with the rise (§6.3's focus
  rule). *Active:* n/a. *Scrolled-past:* lifted instantly.
  *Disabled:* n/a. *Touch:* identical timing; a touch-scroll fling
  triggers the instant path.
- **Breakpoints (v2).** ≥1200px: 1200ms lift, 300ms hold.
  768–1199px: 1050ms / 250ms. <768px: 950ms / 200ms; the mask covers
  the content column only (full-bleed masks on a phone read as page
  loads, not water).
- **Edge cases & failure modes (v2).** *Section taller than 200vh:*
  the mask covers the section's first 100vh only — a mask the size
  of a whole long chapter would lift like a garage door; the ruling
  is that the surface belongs to the chapter's head, and the rest of
  the chapter rises beneath it (§6.3). *Nested surfacing children:*
  the mask belongs to the chapter wrapper, never to children —
  double masks double the waterline and halve the meaning.
  *Reflow mid-lift (rotation, resize):* the lift recomputes its
  −100% from the new height at the next frame; worst case it
  completes 100ms early, which no visitor can see.
- **Accessibility spec (v2).** The mask is `aria-hidden`, never
  focusable, and never removes content from the tree — the section
  beneath it is fully present to assistive technology from first
  paint, covered only visually and only for 1500ms. The sounding it
  carries duplicates §6.15's figure in real text elsewhere; the
  mask's copy is `aria-hidden` with it.
- **Tokens consumed (v2).** `--fjord`, `--waterline`, `--ease-lift`,
  `--dur-lift` (1200ms), `--dur-fallback` (2000ms).

### 6.6 Plumb line progress

- **What & why.** In the left margin, a plumb line descends as the
  visitor reads: a vertical hairline extending scrubbed to scroll,
  metre marks along it, and the current depth printed in light
  figures at its foot. It belongs because it is the theme's only
  gauge and its thesis in instrument form — progress on this page is
  not completion of a bar but depth under a keel, measured the
  sailor's way, in metres, against a total that is a real property
  of the place (§1's law). Every other element in §6 performs
  stillness; this one performs measurement, and the page needs both.
- **Structure.** A fixed-position `<div class="plumb">` in the left
  margin (≥1200px only, §4), containing: an SVG track the full
  viewport height with metre ticks drawn every (total-metres /
  viewport-height) interval, major ticks each 50m with figure
  labels; the descending line itself, a 1px `--ice` at 55% stroke
  whose drawn length is the scrubbed value; a lead weight — a 7px
  circle in `--mist` — at the line's foot; and the readout
  `<output class="plumb-depth">` printing "−NNN m" in sounding
  figures (§3). The total metres come from the build survey
  (`data-total-metres` on `<body>`, rendered into the page, never
  hard-coded in the script).
- **Motion spec.** Line length = smoothed scroll fraction × track
  height, written by the shared loop each frame (lerp 0.08 — the
  line visibly trails the hand by a breath, which is correct: a real
  plumb line swings a moment before it settles). Depth figure =
  round(total metres × *actual* scroll fraction) — the figure is a
  measurement and uses the un-lerped value, so the number is always
  exactly true even while the line is still settling; figure updates
  crossfade 120ms when the value changes (§3 law 3: no rolling
  digits). Metre ticks are static geometry; the weight passes them,
  it does not trigger them. At scroll fraction 1.0 the line reaches
  the track's foot and the readout holds the total — the bottom,
  sounded.
- **States.** *Rest (top):* line at 0, readout "−0 m". *Descending:*
  scrubbed live. *At bottom:* full length, readout at total, weight
  resting on the track's foot tick; a 600ms `--ease-settle` stilling
  of the weight's last swing (a 1px lateral sway, the theme's
  smallest motion, licensed here because a plumb line that stops
  dead has been grabbed, not settled). *Scrolled back up:* the line
  shortens exactly retracing — a sounding is re-taken, not un-taken,
  and the readout stays true at every frame. *Focus:* the readout is
  a live region at `aria-live="off"` by default (§Accessibility) —
  no state change.
- **Content merge.** The line measures *this page's* chapters: each
  chapter's entry depth (§6.15) is the same function's value at that
  chapter's offset, printed at its waterline (§6.5) and in the
  figures band. The instrument and the content share one arithmetic;
  lengthen the page in the CMS and every sounding on it — line,
  waterlines, figures, footer — re-derives. That is the merge: the
  gauge is not beside the content, it is the content's own depth,
  drawn in the margin.
- **Failure fallback.** No JS: the plumb renders at full length with
  the readout printing the total and the apparatus label "FULL
  SOUNDING" — the instrument shows the whole depth of the page it
  sits beside, which is true, static, and honest. Loop dead: same
  state via the watchdog (the line is set to full, never left at a
  false partial depth — a stuck gauge is a lying gauge, and §1's law
  prefers a static truth to a live falsehood).
- **Reduced-motion variant.** The line still descends — scroll-linked
  position is information, not animation — but it steps by chapter
  instead of scrubbing: at each chapter boundary the length and
  figure set instantly to that chapter's sounding. No sway, no
  crossfade. The measurement survives; the water's motion rests.
- **Performance budget & mobile variant.** One SVG length write +
  one text write per frame, ≤0.2ms/frame. Below 1200px the margin
  instrument retires (§4): the readout alone moves into the header
  (§6.10) as a compact sounding — "−NNN m" — updated by the same
  loop from the same function; the line, ticks and weight are not
  rendered at all (a plumb line squeezed into a phone's margin
  would be a progress bar in costume, and the theme refuses the
  costume).
- **Choreography timeline (v2).** Continuous, not beat-based: every
  loop frame — read actual scroll fraction → compute figure (exact)
  → lerp line length toward fraction × track height at 0.08 → write
  length; if figure changed, crossfade readout 120ms. At fraction
  1.0: t=0 weight reaches foot → t=0–600 sway settles → footer
  sounding (§6.16) confirms the same total.
- **State matrix (v2).** *Rest:* per scroll position, exact.
  *Hover:* hovering the plumb shows the chapter soundings as tick
  labels brightening to `--ice` (the major ticks already carry
  figures; hover raises the minor chapter ticks' labels) — the only
  hover the instrument has, and it reveals data, not decoration.
  *Focus:* the plumb is not focusable; the readout sits in the
  header's accessibility order at ≥1200px as a labelled status
  ("Depth, NNN metres") updated at most once per chapter crossing
  for AT (see Accessibility). *Active:* n/a. *Scrolled-past:* n/a —
  it *is* the scrolled state. *Disabled:* n/a. *Touch:* identical;
  touch scroll feeds the same fraction.
- **Breakpoints (v2).** ≥1200px: full instrument in the left margin.
  768–1199px: header sounding only, figure + "OF NNN M" total.
  <768px: header sounding, figure only; the total lives in the
  footer (§6.16). Track height at ≥1200px = 100vh minus header and
  a 48px foot clearance.
- **Edge cases & failure modes (v2).** *Page shorter than one
  viewport (a single-chapter page):* the line rests at full length
  and the readout shows the total — a page with no depth to descend
  sounds itself honestly at 1.0 rather than sitting at a fake 0.
  *Total metres missing from the survey:* the instrument does not
  render and §10's gate fails the build — no total, no gauge; the
  theme would rather have no instrument than an unmeasured one.
  *Resize:* track and tick geometry recompute on the loop's next
  frame; the figure never flickers because it derives from fraction,
  not pixels. *Overscroll (rubber-band):* fraction clamps 0–1; the
  line never descends past the bottom it has sounded.
- **Accessibility spec (v2).** The SVG is `aria-hidden`. The readout
  is exposed as a `role="status"` text in the header order, updated
  for AT only at chapter crossings (a per-frame live region would be
  a depth announcement machine — noise, in a theme whose law is
  quiet). Touch target: none (not interactive). The figure's
  contrast: `--snow` on `--fjord`, 15.76:1 (§2). Keyboard visitors
  scrolling by key see the same scrub; the figure is exact for them
  too, because it derives from the fraction, not the input device.
- **Tokens consumed (v2).** `--ice`, `--mist`, `--snow`,
  `--ease-settle`, `--dur-figure-fade` (120ms), loop lerp 0.08.


### 6.7 The long pause

- **What & why.** Once per page — once, and the gate counts — a
  pinned, almost-empty dark screen holds a single line of copy for
  100vh of scroll, and nothing else moves. It belongs because it is
  the theme's thesis delivered as an experience instead of a claim:
  a site that sells stillness must at some point *be* still in the
  visitor's hands, at full screen, for a measured duration, with the
  plumb line (§6.6) still descending beside the emptiness so the
  visitor feels the pause as depth, not as a loading failure. Every
  other element gestures at quiet; this one enforces it.
- **Structure.** A `<section class="pause">` of 200vh: a sticky inner
  screen of 100vh, ground `--fjord`, containing one `<p>` — Spectral
  200, 30px, centred (the theme's only centred text, §4's ruling) —
  and nothing else. No hairline, no figure, no ornament, no scroll
  hint: a scroll hint in the pause would be the page apologising for
  itself. The line is real copy chosen per build from the site's own
  matter (the Quiet House's is: "The fjord was here before the
  house. It will be here after."). The sticky screen ships unpinned
  in normal flow; JS adds the pin behaviour via `position: sticky`
  already in CSS — sticky is the mechanism, so no-JS pages get the
  same screen for its natural height and lose only the hold.
- **Motion spec.** Pin duration: exactly 100vh of scroll travel
  (200vh section, 100vh sticky child). During the pin: the line is
  motionless for the first 70vh; across the final 30vh it fades to
  38% opacity — not out, down: the line dims like something sinking
  as the next chapter's waterline approaches, so the pause releases
  the visitor instead of ejecting them. The plumb line continues its
  scrub throughout (it is outside the section). The sheen (§5) is
  suspended while the pause is pinned — the one ambient loop yields
  to the one held breath; two stillnesses would be a texture.
- **States.** *Approach:* the preceding chapter's end; the screen
  arrives empty — its line is already present (the line does not
  surface; §6.3 does not apply inside the pause, because a line that
  rises has already broken the silence it is meant to keep).
  *Pinned:* stillness, 70vh. *Release:* dimming, 30vh. *Passed:*
  ordinary flow above the viewport. *Re-entry upward:* the pin
  re-engages in reverse, line re-brightening across the same 30vh —
  the pause is a place, and places are the same from both directions.
- **Content merge.** The line is the chapter it interrupts: placed
  by the survey at the page's argumentative hinge (after the rooms,
  before the crossing form, on the Quiet House home page), it says
  the one thing the surrounding chapters have been implying. It is
  set in the display face at reading size (§3 law 5) because it is a
  sentence of consequence, not a slogan — a build that puts a
  marketing claim in the pause has put a billboard in a church, and
  §9 names it.
- **Failure fallback.** No JS: the section is a 100vh empty screen
  with its line (the section's height collapses to the child's,
  since the extra 100vh exists only to serve the pin's travel) —
  still a pause, merely a shorter one. Sticky unsupported: same.
  The fallback loses duration, never content, and never shows a
  mechanism.
- **Reduced-motion variant.** Unpinned: a 100vh screen, line at full
  opacity throughout, no dimming. The pause remains a pause — reduced
  motion removes the hold, not the silence.
- **Performance budget & mobile variant.** Zero per-frame cost (one
  opacity write across the release window, from the loop). Mobile:
  pin travel shortens to 70vh (section 170vh) — a phone visitor's
  thumb travels less far per gesture, and 100vh of held emptiness on
  a small screen reads as a frozen app rather than a held breath;
  the theme shortens the breath rather than lose the visitor. Line
  26px, measure narrowed to 84vw.
- **Choreography timeline (v2).** Scroll-relative: pin engages at
  section top = viewport top → 0–70vh of travel: nothing moves
  anywhere on the page except the plumb line → 70–100vh: line fades
  100%→38% scrubbed → at 100vh the sticky releases, the next
  chapter's waterline (§6.5) enters at the viewport foot → the sheen
  resumes its cycle 2000ms after release (it does not restart
  mid-pause's echo).
- **State matrix (v2).** *Rest:* line at full opacity, still.
  *Hover:* none — there is nothing in the pause to hover, by design.
  *Focus:* the pause contains no focusable element; a keyboard
  visitor tabs from the chapter before to the chapter after, and the
  pause is traversed by scroll keys like any water. *Active:* n/a.
  *Scrolled-past:* ordinary section. *Disabled:* n/a. *Touch:*
  identical hold; the pin travel is the mobile-ruled 70vh.
- **Breakpoints (v2).** ≥1200px: 100vh pin, line 30px. 768–1199px:
  85vh pin, line 28px. <768px: 70vh pin, line 26px, measure 84vw.
- **Edge cases & failure modes (v2).** *Two pauses in one page:*
  forbidden — the gate (§10) counts `.pause` sections and fails the
  build at 2. A second silence devalues the first. *Pause as the
  first screen:* forbidden by the survey rule — the visitor must
  have been given something before being given nothing; the pause
  sits between 40% and 70% of the page's depth. *Visitor stops
  mid-pause and leaves the tab:* nothing accumulates, nothing times
  out; the silence figure (§6.15) counts the dwell honestly, which
  is the pause working as designed. *Overlays, modals, cookie
  notices during the pause:* the theme's refusal is structural —
  §11 provides no modal or toast in this theme at all, so nothing
  exists that could interrupt it.
- **Accessibility spec (v2).** The line is a normal paragraph in
  reading order — a screen reader meets it as a sentence among
  sentences, which is correct: the pause is long in *time*, not in
  content. No `aria-live`, no role. Its contrast is 15.76:1 (§2).
  Keyboard and switch users traverse it by ordinary scrolling; the
  pin adds travel, not a trap — focus is never inside it to be
  trapped.
- **Tokens consumed (v2).** `--fjord`, `--snow`, `--dur-pause-pin`
  (100vh scroll), Spectral 200 30px (§3).

### 6.8 Slow count-ups

- **What & why.** The theme's figures of magnitude — a fjord's depth,
  a silence's duration, a crossing's length in minutes — count up
  very slowly when their sections surface: 3–4 seconds, on
  `--ease-settle`, arriving the way a sounding arrives, by paying out
  line. It belongs because numbers in this theme are measurements,
  and a measurement that snaps to its value in 400ms is a score, not
  a sounding. The slowness is the honesty: the visitor watches the
  figure being *taken*.
- **Structure.** A `<span class="count" data-count-to="214"
  data-count-unit=" m">` inside a figure (§6.15's anatomy or in-copy,
  wherever a magnitude lives). The final value is the element's text
  content in the shipped HTML — the count is an animation *of* the
  printed figure, never the source of it. JS arms the start value
  (0, or for durations the measured floor) only when the loop is
  alive, and only once per element per page load.
- **Motion spec.** Trigger: the figure's section completing its
  surface (§6.3 rest). Duration by magnitude: values ≤60 count over
  3000ms; ≤1000 over 3500ms; above 1000 over 4000ms — the ledger in
  §5, computed from the value, not chosen per element by hand.
  Easing `--ease-settle` applied to the *displayed* value, which is
  rounded at each frame to the unit's precision (metres: integer;
  minutes: integer; degrees: one decimal). Digits crossfade per
  §3 law 3 only in the plumb readout (§6.6); here the numeral itself
  changes — tabular figures (§3 law 3) keep the width still while
  the value climbs. The count runs once; scrolling away and back
  does not restart it — a sounding retaken is the same depth.
- **States.** *Printed (default):* final value in the DOM. *Counting:*
  armed and running. *Counted:* final value, indistinguishable from
  printed — by design. *Scrolled-past mid-count:* the count
  completes instantly (a figure left mid-climb by a fling would be
  a false measurement displayed to whoever lands below; §1's law
  forbids it). *Re-entry:* no replay.
- **Content merge.** The figures are the content's own claims — the
  fjord's depth at the house, the minutes of the crossing, the
  degrees of the water in February — each carrying its source in its
  caption (§6.15's grammar: figure, unit, source line). The count-up
  is the act of measuring performed on the number the page prints;
  remove the animation and the page loses a ceremony, never a fact.
- **Failure fallback.** No JS: the printed final value, full stop —
  this is why the value ships in the DOM. Watchdog: any count not
  complete by trigger + 4000ms is set to final instantly (the
  duration ledger's maximum is the cap; §5's 2000ms surfacing cap
  does not apply here because nothing is hidden — a mid-count figure
  is a smaller true-ish number on its way to a true one, and the
  failure that matters, a *wrong* final value, cannot occur since
  the final value is the shipped text).
- **Reduced-motion variant.** No count. The figure stands at its
  final value. A reduced-motion visitor is owed the measurement
  without the taking of it.
- **Performance budget & mobile variant.** ≤3 concurrent counts,
  one text write per frame each, ≤0.3ms/frame total. Mobile:
  durations shorten by 500ms (3000→2500 floor) — the ceremony is
  shorter where the screen is, and the gate accepts the mobile
  ledger as the same honesty at a smaller scale. On `save-data` or
  ≤4GB devices, counts are cut (§14) and figures print final.
- **Choreography timeline (v2).** t=0 section rests (§6.3) → t=150
  count begins (a breath after rest, so the eye has landed) → value
  climbs on `--ease-settle` — fast enough at first to register as
  movement, decelerating across the back half so the final value
  arrives like a line going taut → t=3000/3500/4000 (by magnitude)
  final value set → the figure's source line surfaces (§6.3 queue)
  as the count completes, so the claim and its provenance land
  together.
- **State matrix (v2).** *Rest:* final value. *Hover:* none.
  *Focus:* a figure receiving focus (it is not focusable by default;
  if a build makes a figure a link, §6.10 governs) completes its
  count instantly. *Active:* n/a. *Scrolled-past:* completed
  instantly. *Disabled:* n/a. *Touch:* identical triggers.
- **Breakpoints (v2).** ≥1200px: ledger durations as above.
  768–1199px: −250ms per band. <768px: −500ms per band, and values
  above 10000 are abbreviated in the count's early frames (counting
  214 is a ceremony; counting 41,000 frame by frame is a vigil —
  the count eases through orders of magnitude and only the last
  1000 units render individually).
- **Edge cases & failure modes (v2).** *Value of 0 or 1:* no count —
  the figure prints; counting to one is theatre without an audience.
  *Negative values (depths below a datum):* the count climbs in
  magnitude and the sign is printed throughout ("−41 m" counts
  0→41 under a standing minus) — a sign that appears at the end
  would change the claim mid-ceremony. *Figure updated by CMS
  between builds:* the count target is read from the DOM text at
  arm time, so the animation can never disagree with the printed
  page it animates. *Decimal units:* precision from `data-count-
  precision`, defaulting to the unit's rule above.
- **Accessibility spec (v2).** The counting span is `aria-hidden`
  while counting, with a visually-hidden sibling holding the final
  value — assistive technology receives the measurement once, whole,
  immediately, and never a stutter of climbing numbers. At count
  completion the hidden sibling is removed and the span unhidden
  (one DOM swap, no announcement). Contrast per §2 at every frame:
  the figure's colour never animates, only its value.
- **Tokens consumed (v2).** `--ice`, `--snow`, `--ease-settle`,
  `--dur-count-sm` (3000ms), `--dur-count-md` (3500ms),
  `--dur-count-lg` (4000ms).

### 6.9 Click ripple

- **What & why.** Clicking anywhere on the water — a card, a link, a
  bare chapter ground — sends one ripple ring out from the click
  point: 0 to 34vw over 2000ms, fading. It belongs because it is the
  visitor's only possible disturbance, and the theme gives it back to
  them in the theme's own single gesture: you touched the water; the
  water answered, once, exactly where you touched it. It is also the
  theme's click feedback — in a page with no button fills, no scale
  pops and no colour flashes, the ring is how an action acknowledges
  itself.
- **Structure.** The same single ring node as §6.1 (the theme owns
  one), repositioned to the click point within the clicked section's
  positioned ancestor, so the ring belongs to the water it was made
  in and scrolls with it. If a ring is already alive (from §6.1 or a
  previous click), the new click does not spawn a second: the living
  ring is left to finish (one ripple per cause, and a second cause
  arriving mid-ring waits — in practice the ring's 2000ms life and
  human click spacing make the queue invisible; rapid clicking on a
  card produces one ring, which is the correct census of the
  visitor's disturbance).
- **Motion spec.** Trigger: `click` (pointer or keyboard-activated
  click on a focusable element — the ring centres on the element's
  centre in that case, since there is no point). Diameter 0→34vw
  (cap 640px), 2000ms `--ease-ring`, opacity 0.5→0 weighted to the
  last 55%. The underlying action (navigation, §6.14's transition,
  a card's link) proceeds on its own clock, un-delayed: the ring is
  a response, never a gate. On form submit (§6.13) the ring centres
  on the submit line and the confirmation follows its own grammar.
- **States.** Absent → expanding (from the click point) → dissolved
  (node removed). *During §6.7's pause:* clicks inside the pause do
  not ripple — the pause contains nothing to click, and a ring made
  on bare pause water would be the visitor shouting in the held
  breath; the theme declines, silently. *During a page transition
  (§6.14):* clicks are already inert; no ring.
- **Content merge.** The ring is centred on the thing touched — the
  card, the link, the word — so the feedback is located on the
  content, not sprayed across the viewport. Its size (34vw) is
  calibrated to cross the content column and die inside the chapter's
  water: the disturbance is local, the way a real ring dies in a
  real fjord's fetch.
- **Failure fallback.** If the loop is dead, no ring — clicks still
  work, because the ring is a response layered on actions, never a
  dependency of them. Node creation failure (detached ancestor) is
  caught and the click proceeds ringless. There is no state in which
  a missing ripple blocks anything.
- **Reduced-motion variant.** No ring. Click feedback is carried by
  the focus/active states in §11 (underline brighten, apparatus
  colour step) — the information (your touch registered) survives
  without the disturbance.
- **Performance budget & mobile variant.** Shares §6.1's budget
  (one node, ≤0.1ms/frame). Mobile: diameter caps at 70vw / 340px,
  duration 1600ms — a tap's ring on a phone should reach the
  column's edges and stop, not flood the small water.
- **Choreography timeline (v2).** t=0 click → t=0 ring born at the
  point, opacity 0.5 → t=0 the action's own feedback begins
  (underline, tilt, navigation) in parallel → t≈900 ring at ~24vw,
  border thinning → t=2000 opacity 0, node removed → the surface is
  closed again; total disturbance, two seconds, once.
- **State matrix (v2).** *Rest:* absent. *Hover:* no ring on hover —
  hovering is looking, not touching, and the water does not answer
  a look. *Focus:* keyboard focus alone makes no ring; the
  *activation* (Enter/Space click event) does, centred on the
  element. *Active:* the ring *is* the active feedback; the
  element's own :active state (§11) runs beneath it. *Scrolled-
  past:* n/a. *Disabled:* clicks on disabled controls make no ring —
  the water does not answer a touch on a locked door. *Touch:* a tap
  is a click; the ring centres on the tap point; long-press makes
  no ring (it is not a click, and the theme does not reward holding
  the water down).
- **Breakpoints (v2).** ≥1200px: 34vw cap 640px / 2000ms.
  768–1199px: 44vw cap 520px / 1800ms. <768px: 70vw cap 340px /
  1600ms.
- **Edge cases & failure modes (v2).** *Click near a section edge:*
  the ring clips at the section's box (overflow hidden on the
  positioned ancestor) — rings stop at shores (§6.1's ruling).
  *Click on the plumb line:* the plumb is margin furniture, not
  water; no ring, and §6.6's hover grammar is the only response.
  *Double-click / text selection:* the second click finds the ring
  alive and adds none; selection proceeds undisturbed. *Click
  during §6.1's load ring:* the load ring finishes; the click's
  action proceeds; no second ring — arrival outranks touch in the
  first three seconds, and the visitor's click is still honoured by
  its action.
- **Accessibility spec (v2).** `aria-hidden`, never announced, no
  information carried. Keyboard activation produces the same ring,
  so the feedback is parity-equal across input modes; under
  reduced motion both modes lose the ring and keep §11's states.
- **Tokens consumed (v2).** `--ring`, `--ease-ring`, `--dur-ripple-
  click` (2000ms), `--ripple-click-max` (34vw, capped 640px).

### Page-family elements


### 6.10 Sounding navigation (page family: navigation)

- **What & why.** The site's navigation is a still band at the head
  of the water: the house name in Spectral, chapter links in
  apparatus, each link carrying a mirrored underline that brightens
  on hover — the theme's one link gesture — and, below 1200px, the
  compact depth sounding that inherits the plumb line's duty (§6.6).
  It belongs because navigation in this theme cannot be a toolbar;
  it is the surface from which the descent begins, and it must be as
  quiet as the water it floats on.
- **Structure.** A `<header>` in normal flow (never fixed — a fixed
  bar would follow the visitor down like a boat, and nothing follows
  you into a fjord), ground `--fjord`, a `--waterline` hairline at
  its foot. Contents: wordmark (Spectral 300, 20px, `--snow`), nav
  list (apparatus, §3), and the sounding output (`<output
  class="sounding">`, rendered ≥1200px too but visually the plumb
  readout §6.6 carries the margin there; the header sounding shows
  <1200px only). Current chapter link carries `aria-current` and a
  standing brightened underline.
- **Motion spec.** Nav surfaces with the page (it is the first
  element of §6.3's queue, rising 24px — less than chapters; the
  surface itself barely moves). Mirrored underline: a 1px line under
  the link text with its 1px reflection beneath at 30% — hover/focus
  brightens line + reflection from `--mist` to `--ice` over 600ms
  `--ease-drift`; the brighten is the whole gesture (no shift, no
  weight change, no background). Current-chapter migration on scroll:
  the underline's standing state moves between links with a 600ms
  crossfade as chapters pass the viewport's middle — driven by the
  loop, not by click, because the visitor's position is a sounding,
  not a selection. Header sounding (<1200px): §6.6's figure, same
  function, crossfade 120ms on change.
- **States.** *Rest:* wordmark and links at apparatus colour,
  current chapter underlined. *Hover:* underline brightens (desktop
  pointer only). *Focus:* identical brighten plus the §11 focus
  ring — focus must be at least as visible as hover in a dark theme,
  and here it is brighter. *Active:* §6.9's ring on click, centred
  on the link. *Scrolled-past:* the header is gone (not fixed); the
  plumb line and chapter waterlines carry orientation from there.
  *Disabled:* n/a. *Touch:* no hover brighten; tap = click ring +
  navigation.
- **Content merge.** The nav's chapters are the page's actual reaches
  — the links are the chapters' names, and the current-chapter
  underline is computed from the same offsets that drive the plumb
  line's chapter ticks (§6.6). Rename a chapter and the nav, the
  ticks and the waterlines all take the new name from the one
  heading. There is no separate nav content to drift.
- **Failure fallback.** No JS: all links stand at rest colour, the
  current chapter is the one the server marked (first, or by URL),
  the header sounding prints the total depth with the label "FULL
  SOUNDING" (§6.6's static ruling). Every link works — navigation
  in this theme has no JS dependency at all.
- **Reduced-motion variant.** Underline states apply instantly;
  current-chapter migration steps without crossfade; sounding
  updates by chapter (§6.6's reduced ruling). Nothing else changes:
  the nav was already still.
- **Performance budget & mobile variant.** One crossfade at a time,
  negligible loop cost. Mobile: the nav wraps to two lines (wordmark
  line, links line, apparatus 11.5px, horizontally scrollable if
  the chapter names overflow — a sounding chart scrolls, it does
  not hamburger; the theme refuses the hamburger menu because a
  hidden chart is a lost chart), hairline retained, sounding at the
  links line's right end.
- **Choreography timeline (v2).** t=0 load → header rises 24px over
  1200ms `--ease-surface` (queued first, §6.3) → ripple (§6.1) and
  headline (§6.2) proceed beneath it. On scroll: chapter crossing
  viewport middle → 600ms underline crossfade to the new chapter.
  On click: §6.9 ring + §6.14 transition (500ms) → new page's header
  stands at rest (transitions do not replay the rise on internal
  navigation — you do not re-arrive at a fjord you are already on).
- **State matrix (v2).** Covered in States above for rest / hover /
  focus / active / scrolled-past / touch; *disabled* state exists
  only for a link to the current page rendered as a span — it takes
  the standing underline and `--mist-light`, never a greyed
  "disabled link" treatment.
- **Breakpoints (v2).** ≥1200px: single line, sounding hidden
  (plumb carries it). 768–1199px: single line + sounding shown.
  <768px: two lines, sounding inline, links scrollable horizontally
  with the hairline as their waterline.
- **Edge cases & failure modes (v2).** *Many chapters (8+):* the
  apparatus list wraps at tablet, scrolls at mobile; the theme caps
  a page at 7 chapters in the survey (§7) precisely so the chart
  stays readable — a site needing 12 nav items needs two pages, not
  a smaller font. *Long chapter names:* names are reaches, kept ≤3
  words by §12's voice; overflow truncates with the full name in
  the waterline of its chapter, never with an ellipsis in the nav.
  *Sticky-header requests from stakeholders:* refused in the build
  notes — the refusal is §9 anti-slop, recorded, not negotiated per
  page.
- **Accessibility spec (v2).** Landmark `<header>` + `<nav
  aria-label="Chapters">`; `aria-current="page"` (or `"location"`
  for in-page chapters) migrates with the visual underline — the
  two never disagree, both being set by the same loop branch.
  Focus ring: 2px `--snow` outline, offset 3px (§11). Link contrast
  `--mist-light` on `--fjord` 6.73:1 at rest, `--ice` 12.16:1
  brightened. Touch targets ≥44px tall via padding, though the
  apparatus text is 12px — the water around a link is part of its
  target.
- **Tokens consumed (v2).** `--fjord`, `--waterline`, `--mist`,
  `--mist-light`, `--ice`, `--snow`, `--ease-drift`, `--ease-surface`.

### 6.11 The water panel (page family: hero)

- **What & why.** The hero is a single panel of the fjord itself:
  100vh of `--fjord` water holding the house name, one standfirst,
  one action, and the instruments' zero state — the ripple (§6.1),
  the surfacing headline (§6.2), the sheen (§5), the plumb at −0 m.
  It belongs because the theme's first screen must be the thing
  itself, not a picture of the thing: no photograph, no illustration
  of a fjord — the panel *is* water, and everything the page will do
  is done here first, at the surface, before the descent.
- **Structure.** `<section class="water-panel">`, min-height 100vh
  (100svh mobile), containing in order: the header's flow space
  (§6.10 sits above it in flow), a centred-left column (the §4
  measure) with the eyebrow apparatus line (the place's name and
  coordinates — real coordinates, from the survey; a build without
  real coordinates omits the line rather than inventing some), the
  h1 (§6.2), its reflection (§6.4), the standfirst (Spectral 300,
  21px, ≤2 lines, ≤140 characters by §12's rule), one primary action
  (§11's still button), and at the panel's foot the descent line:
  apparatus text "THE WATER IS 4 DEGREES IN FEBRUARY" — a real
  figure with its source in the survey, or nothing. The panel's
  height is fixed by `min-height`, never by content, so the
  surfacing choreography cannot shift layout.
- **Motion spec.** The panel hosts §6.1 (ripple, t=200), §6.2
  (headline, t=600), §5's sheen (drifting from t=0, pausing when
  the panel leaves the viewport), and a 0.94× parallax on the sheen
  layer only as the panel scrolls away — the light stays a breath
  behind the leaving surface. The standfirst and action surface via
  §6.3's queue at t≥1800, interval 220ms. Nothing else moves. The
  panel does not pin; the descent begins by ordinary scrolling, and
  the first chapter's pause (§4's 30–45vh of water) follows it.
- **States.** *Arrival:* the choreography above. *Rested:* still,
  sheen drifting. *Scrolled-past:* sheen paused, panel ordinary.
  *Return:* no replay of ripple or rise (bfcache and scroll-return
  both find the surface closed and the headline at rest — arrival
  happens once per load, §6.1's ruling).
- **Content merge.** The panel's text is the site's identity and
  offer — name, claim, action — with no imagery to merge into
  because the panel refuses imagery on principle (§9: a stock fjord
  photograph in this hero is the theme's cardinal slop). The
  descent-line figure is content too: the water temperature is the
  retreat's real February figure, the first measurement of the page,
  placed where the descent begins so the visitor's first sounding
  is of the water, not of themselves.
- **Failure fallback.** No JS: the complete panel, headline at rest,
  reflection printed, action live, no ripple node, sheen absent
  (it is JS/loop-driven; its absence costs the page nothing it
  needs). The panel is the fallback — it was designed static-first
  (§15 step 2) and the ceremony is layered onto a finished screen.
- **Reduced-motion variant.** The finished panel: headline surfaced,
  reflection at 2px, no ripple, no sheen, no parallax. Indistinguishable
  from the no-JS panel except the sounding instruments' live state.
- **Performance budget & mobile variant.** The panel is text, one
  gradient layer and one ring node: ≤0.3ms/frame all-in. Mobile:
  100svh, headline 40px (§3), standfirst 19px, the descent line
  holds (it is one line of apparatus — if it must wrap, the survey
  shortens the figure's wording, never the font).
- **Choreography timeline (v2).** t=0 first paint, panel complete →
  t=200 ripple born (§6.1) → t=350 surfacing armed → t=600 headline
  rise (§6.2) → t=1800 standfirst surfaces → t=2020 action surfaces
  → t=2400 headline reflection window opens (§6.4) → t=3200 ripple
  dissolved (§6.1) → panel at rest; only the sheen remains alive.
- **State matrix (v2).** *Rest:* as above. *Hover:* the action's
  §11 hover; nothing else in the panel is hoverable. *Focus:* the
  action is the panel's only focusable element (plus header links
  above it); focus on it completes any running surface instantly
  (§6.3's rule). *Active:* §6.9 ring centred on the action.
  *Scrolled-past:* sheen paused. *Disabled:* n/a. *Touch:* the
  choreography is identical; the first touch does not fast-forward
  anything (contrast §45's dip, which completes on touch — this
  water is not in a hurry to be touched).
- **Breakpoints (v2).** ≥1200px: 100vh, display 64px. 768–1199px:
  96vh, display 52px. <768px: 100svh, display 40px, eyebrow wraps
  to two lines max, descent line retained.
- **Edge cases & failure modes (v2).** *Very tall content (long
  house name + long standfirst):* the standfirst's 140-character
  cap (§12) is the guard; if a build breaks it, the panel grows
  beyond 100vh and the choreography still holds — the ripple's
  centre is the panel's optical centre, recomputed, not a fixed
  42% assumption (the 42% is the *default* the survey may override).
  *No real figure for the descent line:* the line is omitted; an
  empty foot is correct, an invented temperature is a §1 violation.
  *Landscape phones (short viewport):* min-height falls to 92svh so
  the first pause's top shows — a hint of more water is worth more
  than a sealed screen.
- **Accessibility spec (v2).** Landmark order: header (§6.10), then
  the h1 — the panel adds no roles. The eyebrow coordinates are
  plain text. The action is a real link/button with §11's focus
  ring. Colour contrast: standfirst `--ice` on `--fjord` 12.16:1;
  descent line `--mist-light` 6.73:1. The panel's decorative layers
  (sheen, ripple, reflection) are all `aria-hidden`.
- **Tokens consumed (v2).** `--fjord`, `--snow`, `--ice`,
  `--mist-light`, `--sheen`, `--ease-surface`.

### 6.12 Chapter cards (page family: cards / listing)

- **What & why.** Where the site lists things — the Quiet House's
  four rooms, a swimming club's waters, a publisher's backlist —
  they float as chapter cards: `--deep` grounds in the water column,
  each with a title, its own small reflection of the title, three
  lines of fact, and one figure with its source. They tilt almost
  imperceptibly toward the pointer, like something floating that has
  noticed a hand. It belongs because a listing in this theme cannot
  be a grid of boxes shouting for clicks; the rooms are reaches of
  water you drift across, and the card's barely-there tilt is the
  only acknowledgement that you are passing.
- **Structure.** An `<article class="chapter-card">` list, one
  column at desktop within the 1080px field (§4) — cards are wide
  and low (min-height 148px), never a multi-column grid: a fjord has
  one reach at a time. Anatomy: apparatus kicker (the room's number
  and aspect — "ROOM 2 — FACES THE WATER"), Spectral 300 title 28px
  with its §6.4-grammar reflection (cards are the reflection's
  second licensed home; blur rest state only, no scrub — a listing
  is scanned, not settled into), fact lines (Inter 300), the figure
  line (§6.15's grammar: value, unit, source), and the whole card a
  single link (stretched-link pattern, title as the link text).
- **Motion spec.** Cards surface via §6.3 (queue interval 220ms).
  Tilt: pointermove over a card rotates it ≤1.2° on the axis toward
  the pointer and lifts it 2px, written by the shared loop (the
  tilt reads the loop's smoothed pointer, never raw events), settle
  900ms `--ease-settle` on leave, including a 0.3° overshoot — the
  float bobbing once as the hand withdraws. The tilt is deliberately
  below the threshold of showmanship: if a visitor can *describe*
  the tilt, it is too much; the gate's test is that it is felt, not
  seen (§10). Reflection on card titles rests at 3px blur / 10% —
  between §6.4's far and near, because a card is glanced at, not
  settled with.
- **States.** *Rest:* flat, title reflection at rest. *Hover:*
  tilt + title brightens `--ice`→`--snow`, reflection warms to 13%.
  *Focus:* the stretched link's focus ring draws around the card
  (§11); tilt does not apply (focus is not a hand on the water) but
  the brighten does. *Active:* §6.9 ring from the click point; the
  card presses 1px (the only press in the theme — a floating thing
  dips when boarded). *Scrolled-past:* rested, no replay.
  *Disabled:* a card for an unavailable room is not disabled-looking;
  it carries the apparatus line "NOT LET THIS WINTER" and no link —
  absence stated, not greyed (§12's voice). *Touch:* no tilt; tap =
  click.
- **Content merge.** The card's figure is the room's real fact — its
  depth of window, its metres from the water, its capacity — with
  its source ("measured from the jetty"), and the kicker's aspect is
  the room's actual facing. The card is the room's sounding; a build
  that fills cards with marketing adjectives has made a brochure and
  moored it in the wrong water (§9).
- **Failure fallback.** No JS: flat cards, full text, links live.
  Loop dead: same. The tilt is the only JS-dependent property and
  its absence is invisible — nobody can miss a 1.2° tilt that never
  happened.
- **Reduced-motion variant.** No tilt, no press; hover/focus
  brighten applies instantly. Cards surface pre-rested (§6.3).
- **Performance budget & mobile variant.** ≤1 tilting card at a
  time (pointer can only be over one), one transform write/frame.
  Mobile: cards stack full-width, min-height auto, tilt cut
  entirely (touch has no hover and the theme does not fake one),
  reflection retained at rest. On ≤4GB devices the card-title
  reflections are cut with §6.4's mobile ruling.
- **Choreography timeline (v2).** Per card: surfaces per §6.3 →
  rest. Hover: t=0 pointer enters → loop eases tilt toward target
  over ~300ms of frames → steady while held (micro-drift ±0.15°
  from the smoothed pointer is acceptable and human) → leave:
  900ms settle with the 0.3° overshoot at ~70% → flat.
- **State matrix (v2).** Rest / hover / focus / active /
  scrolled-past / disabled / touch as detailed in States above;
  the matrix's one unusual cell: *hover + focus simultaneously*
  (mouse parked, keyboard arrived) — focus ring wins, tilt
  continues, brighten takes the focus value; no state cancels
  another, because on water, two truths float at once.
- **Breakpoints (v2).** ≥1200px: 1080px field, card min-height
  148px, tilt live. 768–1199px: 88vw field, min-height 132px, tilt
  ≤1°. <768px: full column width, no tilt, kicker wraps above the
  title, figure line moves below the facts.
- **Edge cases & failure modes (v2).** *Long room names:* title
  wraps to two lines; the reflection mirrors both at rest blur —
  acceptable on cards (the §6.4 one-line cap is a headline rule,
  not a card rule, because card titles are set smaller and their
  reflections shallower). *Many rooms (a hotel of 30):* the theme
  caps a card chapter at 7 (§7's survey rule); beyond that the
  listing becomes two chapters with a pause between — the water
  decides the pagination, not the inventory. *Missing figure:* the
  figure line is omitted; a card without a sounding is still a
  room, but the survey flags it — three figureless cards in a row
  is a §10 gate conversation.
- **Accessibility spec (v2).** One link per card (the title),
  stretched over the card; the reflection is `aria-hidden`; the
  whole card is not a second link. Focus ring visible at 2px
  `--snow` around the full card. Touch target = the whole card,
  ≥148px tall desktop, ≥96px mobile. Text contrast: facts `--ice`
  on `--deep` 9.18:1; kicker `--mist-light` on `--deep` 5.09:1.
  Tilt is `transform` only — reading order and hit geometry at rest
  are unaffected for AT and switch users.
- **Tokens consumed (v2).** `--deep`, `--snow`, `--ice`,
  `--mist-light`, `--reflection`, `--ease-settle`, `--dur-tilt-
  settle` (900ms).


### 6.13 The crossing form (page family: forms / conversion)

- **What & why.** The conversion — booking the house, joining the
  swim, requesting the crossing — is a sheet on `--deep` water: a
  left-aligned form whose fields are sounding lines, whose submit is
  a single still button, and whose confirmation is a ledger line,
  not a celebration. It belongs because asking is the loudest thing
  a visitor does on a quiet page, and the form must absorb that
  loudness without breaking the water: no modal, no multi-step
  wizard, no urgency apparatus — just the questions the house
  actually needs, in the order it needs them, on one screen.
- **Structure.** A `<form class="crossing-form">` on a `--deep`
  sheet (max-width 620px, left-aligned per §4), fields as
  inscription lines: apparatus label above, a 1px `--mist` rule
  below the input, no boxes, no fills. Field set for the Quiet
  House booking: name, direction (email), the room (a seam list of
  radio lines — §11's radio grammar: each room a ruled line with
  its figure), arrival and departure (native date inputs, restyled
  minimally — the theme does not build a calendar; a fjord house
  takes the platform's), one textarea for "anything the house
  should know" on ruled lines at the body line unit. Submit: §11's
  still button, label "ASK FOR THE ROOM" — the form asks; it does
  not "book now", because the house answers by hand.
- **Motion spec.** The sheet surfaces via §6.3 as one body (its
  fields do not stagger — a form is one object, and staggering its
  questions would make the visitor wait to be asked). Focus: the
  field's rule inks from `--mist` to `--ice` over 400ms
  `--ease-drift`, and a small plumb tick descends 8px beside the
  label — the sounding attention of the form, the only focus
  ornament. Error: the rule steps to the error treatment (§11) and
  the margin note fades in over 300ms; nothing shakes — water does
  not shake, and neither does this form (§9 names the shake as
  slop). Submit: the button's apparatus label crossfades to
  "ASKING…" (the ellipsis is the theme's only loading state;
  §11 refuses spinners), the §6.9 ring centres on the button, and
  the confirmation (§States) replaces the sheet over 600ms
  `--ease-settle`.
- **States.** *Rest:* rules at `--mist`, labels `--mist-light`.
  *Focus:* rule inked, tick descended. *Filled:* the rule holds a
  mid state (`--mist-light`) — a field that has been answered keeps
  a slightly deeper line, so the sheet reads as a sounding already
  partly taken. *Error:* §11's alert grammar inline per field +
  the summary line at the sheet's head on submit failure ("Two
  lines need attention before the house can read this." — counted
  from the actual invalid fields). *Submitting:* fields disabled,
  label "ASKING…", no spinner, no progress — the wait is the
  house's, and it is short. *Success:* the sheet is replaced by the
  confirmation block (§6.16's grammar at form scale): "ASKED. THE
  HOUSE ANSWERS WITHIN A DAY." plus the visitor's own room and
  dates restated from their input — a ledger entry, generated from
  the submission, never a generic thanks. *Failure (network):* the
  sheet persists with every field intact and the fixed failure line
  (§12) at its head; nothing the visitor wrote is ever lost to a
  failed ask.
- **Content merge.** The room radio lines carry §6.12's real figures
  (aspect, metres from the water), so choosing is done on soundings,
  not adjectives; the confirmation restates the visitor's own data;
  the form's questions are the house's actual booking needs from
  the survey — a field the house does not need is not asked, because
  in this theme an unnecessary question is noise, and noise is the
  one pollution the fjord refuses.
- **Failure fallback.** The form is a native form with a real
  `action`; no JS: it submits, and the server returns the
  confirmation as a page (§6.14's transition is an enhancement, not
  a dependency). JS validation failing to load leaves native
  validation. The sheet's static state is complete and submittable
  in every failure mode — the gate rehearses a no-JS submission
  (§10).
- **Reduced-motion variant.** All state changes instant; the ring
  absent (§6.9); the confirmation replaces without the crossfade.
  The form's patience is unchanged — it never had motion worth
  missing.
- **Performance budget & mobile variant.** No animation loop of its
  own; focus transitions are CSS. Mobile: the sheet is full-column,
  radio lines stack with 48px targets, date inputs native, the
  submit button full-width (the one full-width button in the theme —
  a thumb at the bottom of a sheet is a hand on the door).
- **Choreography timeline (v2).** Conversion section: sheet surfaces
  (§6.3) → fields at rest. Focus: t=0 rule ink begins → t=400 rule
  at `--ice`, tick settled at +8px. Submit: t=0 ring (§6.9) + label
  crossfade 200ms → network wait (fields disabled at t=0, the
  sheet's stillness is the loading state) → success: t=0 sheet
  fades 300ms → confirmation surfaces 40px/600ms `--ease-settle`
  (a small rise — confirmations surface like everything else, but
  at half distance: they are near the surface already) → the footer
  confession's tally (§6.16) includes the ask in its count of the
  visit.
- **State matrix (v2).** Per field: *rest / focus / filled / error /
  disabled (submitting)* as in States; per sheet: *rest / submitting
  / success / failed-kept*. *Hover* on the sheet: none (a form is
  not hovered; its controls carry their own §11 hovers). *Touch:*
  focus grammar identical; the tick descends on tap-focus; targets
  ≥48px. *Scrolled-past:* the sheet, once surfaced, is inert to
  scroll — forms do not perform for passers-by.
- **Breakpoints (v2).** ≥1200px: sheet 620px in the 1080px field,
  two-column date pair. 768–1199px: sheet 88vw, dates paired.
  <768px: sheet full column, dates stack, radio figures wrap under
  their room names, submit full-width.
- **Edge cases & failure modes (v2).** *Room fully booked:* its
  radio line carries "NOT LET THIS WINTER" (§6.12's grammar) and is
  not selectable — stated in the list, not discovered at submit.
  *Dates inverted:* the error is the house's voice (§12): "The
  departure is before the arrival. The water cannot be crossed
  backwards." *Very long names / directions:* fields are single
  lines that scroll horizontally natively; the sheet never grows.
  *Double submit:* the disabled submitting state + a submit token;
  the house receives one ask. *Session return mid-form:* the
  browser's own restoration governs; the theme adds no autosave —
  a half-asked question is the visitor's to finish or abandon.
- **Accessibility spec (v2).** Real `<label>` per field, `for`/`id`
  paired; errors linked by `aria-describedby` and the summary
  `role="alert"` on submit failure only (never per keystroke);
  required marked in apparatus ("NEEDED") not by asterisk alone.
  Focus order = visual order = the house's question order. Contrast:
  labels 5.09:1 on `--deep`, input text `--snow` 11.90:1, rules are
  graphical. The "ASKING…" state is `aria-busy` on the form with a
  visually-hidden status. Touch targets ≥48px on all lines.
- **Tokens consumed (v2).** `--deep`, `--mist`, `--mist-light`,
  `--ice`, `--snow`, `--ease-drift`, `--ease-settle`.

### 6.14 Un-surfaced skeleton + surface-crossing transition (page family: loader / transition)

- **What & why.** Two duties, one grammar. The skeleton is what a
  chapter looks like before it surfaces during load: not grey bars,
  but the chapter's own water — a `--deep` block at the chapter's
  true height with its waterline drawn and the apparatus line
  "SOUNDING…" where its sounding will print. The transition is how
  the site moves between pages: a waterline sweep crosses the screen
  once, 500ms, and the new page stands surfaced. It belongs because
  loading and leaving are the two moments a quiet site usually
  shouts (spinners, wipes, logos); here both are done in the
  theme's own medium — depth not yet taken, a surface crossed.
- **Structure.** Skeleton: `<div class="unsurfaced" aria-hidden>`
  blocks generated only while a chapter's content is genuinely
  pending (client-rendered listings, the record search §11) — never
  as a decorative preload on server-rendered pages, which ship
  complete. Each block reserves its chapter's measured height (from
  the survey's anatomy, §15 step 2) so resolution causes no shift.
  Transition: a fixed `<div class="crossing">` — a 1px `--waterline`
  hairline with `--fjord` above it — translating vertically across
  the viewport; beneath it the navigation swaps.
- **Motion spec.** Skeleton resolution: when content arrives, the
  block's chapter surfaces per §6.3 (the skeleton does not fade —
  the chapter rises *through* where it was, one gesture). If
  content has not arrived by 6000ms, the block prints the empty
  line in §12's voice ("Nothing has surfaced here yet.") with a
  retry link — a skeleton that outlives 6s is an empty state
  pretending, and the theme makes it confess. Transition: on
  internal navigation (where the build uses client routing), the
  hairline enters from the top over 500ms `--ease-lift`, the page
  swaps at the line's midpoint (t=250), the line exits at the
  bottom by t=500; latest-wins — a second navigation mid-crossing
  completes the first instantly. Plain full-page loads skip the
  transition entirely: the new page simply stands there (§6.10's
  no-replay ruling).
- **States.** Skeleton: *sounding* (≤6000ms) → *surfaced* (content)
  or *empty* (confessed). Transition: *idle* (off-screen) →
  *crossing* → *idle*. Neither state ever blocks input for more
  than the 500ms crossing, and the crossing is cancellable by the
  browser's own back at any point (history is never trapped by a
  hairline).
- **Content merge.** The skeleton carries the chapter's real
  sounding label and its true reserved height — it is the chapter's
  place held in the water, shaped like the chapter. The transition's
  hairline is §4's waterline motif at page scale: crossing to a new
  page is breaking a new surface, and the motif the chapters wear
  at their heads is the same line the whole page crosses under.
- **Failure fallback.** Routing failure mid-crossing: the line
  completes its exit and the *old* page stands — a failed crossing
  returns you to the shore you left, never to a blank. Skeleton
  data failure: the 6000ms confession with retry (above). No JS:
  neither element exists; pages load whole.
- **Reduced-motion variant.** Skeleton resolves instantly when data
  lands (no rise). Transition: none — navigation is a plain swap;
  the hairline is motion, and it rests.
- **Performance budget & mobile variant.** Skeleton: zero animation
  cost (a static block; the "SOUNDING…" line does not pulse —
  pulsing text is a heartbeat, and this water has none). Transition:
  one transform, 500ms. Mobile: identical; the crossing line is
  1px at all sizes.
- **Choreography timeline (v2).** Transition: t=0 click (§6.9 ring
  fires on the link in parallel) → t=0–250 line descends to
  mid-viewport, old page still beneath → t=250 swap → t=250–500
  line exits at the foot → new page at rest (no surfacing replay;
  its chapters stand surfaced, its plumb at the reader's new 0).
  Skeleton: t=0 block placed → data lands (t=X) → §6.3 rise begins
  t=X → rested t=X+1400; or t=6000 confession prints.
- **State matrix (v2).** *Rest:* both idle/absent. *Hover:* none.
  *Focus:* focus is never inside a skeleton (aria-hidden, inert);
  after a transition, focus moves to the new page's h1
  (`tabindex="-1"`) — announced by the heading itself, not by a
  live region. *Active:* n/a. *Scrolled-past:* skeletons below the
  fold resolve unsurfaced-visible (they surface when scrolled to,
  per §6.3's queue, if data has landed; if not, the sounding block
  is what scrolls into view — honest at every depth). *Disabled:*
  links are disabled only during the 500ms crossing. *Touch:*
  identical.
- **Breakpoints (v2).** All sizes identical in grammar; skeleton
  heights come from each breakpoint's anatomy (§15 step 2 measures
  all three), so a resize mid-load re-reserves correctly.
- **Edge cases & failure modes (v2).** *Slow data on a fast
  scroll:* the visitor may reach a sounding block and wait with it —
  that is the theme working; the 6000ms confession bounds the wait.
  *Data arrives for an off-screen chapter:* it is placed rested, no
  rise (nobody was watching that water). *Back-button during
  crossing:* history wins; the line exits instantly. *Search with
  zero results:* not a skeleton case — §11's search prints the
  empty line directly; skeletons are for pending, not for absent.
- **Accessibility spec (v2).** Skeleton blocks are `aria-hidden`
  with the region carrying `aria-busy="true"` until resolution and
  a visually-hidden status that announces only the confession
  ("Nothing has surfaced here yet") — never a per-block chatter.
  Transition preserves focus discipline (h1 focus, above). The
  crossing line is decorative (`aria-hidden`).
- **Tokens consumed (v2).** `--deep`, `--fjord`, `--waterline`,
  `--mist-light`, `--ease-lift`, `--ease-surface`.

### 6.15 Depth figures (page family: data)

- **What & why.** The page's instruments gathered into a band: the
  figures a Fjord Stillness site is allowed to boast with — the
  fjord's depth at the house, the length of the silence the visitor
  has kept, the water's temperature, the crossing's minutes — each
  printed as figure, unit and source line, each computed or counted
  per §1's law. It belongs because a quiet site's credibility is its
  arithmetic: this band is where the page shows its soundings, and
  it is the element stakeholders most often try to fill with
  invented numbers — which is precisely why it exists as a specified
  element with a law, instead of a stats row.
- **Structure.** A `<dl class="soundings">` of 2–4 figures in the
  1080px field, each `<div class="sounding-fig">` holding: apparatus
  label (dt), the figure (dd, Spectral 300 40px `--snow`, §6.8's
  count grammar where the figure is a magnitude), the unit, and the
  source line (`--mist-light` caption: "sounded at the jetty, 2024"
  / "your visit, counted" / "the harbourmaster's board"). The
  silence figure's value is an `<output>` fed by the dwell counter
  (below). No icons, no sparklines, no deltas — a sounding has no
  trend arrow.
- **Motion spec.** Magnitude figures count per §6.8 when the band
  surfaces. The silence figure is live but unhurried: it counts real
  elapsed visible dwell and updates its printed value once per 10
  seconds (a per-second ticker would be a clock, and a clock is
  noise; the figure prints whole minutes once past 90 seconds —
  "1 MINUTE", "2 MINUTES" — and seconds only below that, because
  the theme's durations are honest at the precision they are
  *felt*). Depth and temperature figures are static after their
  count — they are properties of the place, not of the visit.
- **States.** *Printed (default):* all figures at final values with
  sources — the no-JS state, and note that the silence figure
  without JS prints nothing at all (its line reads "YOUR SILENCE —
  NOT COUNTED WITHOUT THE INSTRUMENT" is forbidden as coy; instead
  the figure is simply absent from the band, and the band holds the
  place's figures only — an instrument that cannot measure does not
  get a dial). *Counting:* §6.8. *Live:* the silence figure stepping
  at its 10s / 1min cadence. *Scrolled-past:* counts complete (§6.8).
- **Content merge.** Every figure is generated from the survey's
  data object (place facts) or the session's one dwell counter —
  the same object that feeds §6.6's total, §6.12's card figures and
  §6.16's footer. The band is the object's public page. A figure
  whose source line cannot be written truthfully is not printed:
  the band ships with 2 figures rather than 4 padded ones, and the
  survey records why.
- **Failure fallback.** Dwell counter dead (loop failure): the
  silence figure is removed from the band at arm time — the band
  never displays a frozen partial silence as if it were the visit's
  measure. Place figures are DOM text; they cannot fail.
- **Reduced-motion variant.** Figures print final; the silence
  figure still counts (it is information, updated at its cadence,
  applied instantly without crossfade).
- **Performance budget & mobile variant.** The dwell counter is one
  accumulator in the shared loop (visibility-gated), ≤0.1ms/frame.
  Mobile: the band stacks 1 figure per row, figure size 34px; the
  silence figure keeps its cadence.
- **Choreography timeline (v2).** Band surfaces (§6.3) → t=+150
  counts begin (§6.8) → source lines surface as each count completes
  → silence figure: t=load dwell counting begins (it does not wait
  for the band — the visit's silence starts at arrival, and the
  figure, when reached, already holds a true number) → updates at
  its cadence for the visit's remainder → at footer, §6.16 prints
  the same counter's final value: the two must agree, and the gate
  checks the agreement in a scripted session (§10).
- **State matrix (v2).** *Rest:* final / live values. *Hover:* none.
  *Focus:* figures are not focusable. *Active:* n/a. *Scrolled-
  past:* complete. *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: one row, ≤4 figures. 768–1199px:
  2×2 grid. <768px: stacked rows, hairline `--waterline` between
  figures (the band's only internal lines — soundings separated by
  surfaces).
- **Edge cases & failure modes (v2).** *Tab hidden:* dwell counting
  pauses (visibility gate) — the silence of an unattended tab is
  not the visitor's silence, and counting it would inflate the one
  figure the visitor can check against their own memory; §1's law
  again. *Very long visits:* the figure prints hours past 90
  minutes ("1 HOUR 12 MINUTES") — precision rules scale, honesty
  doesn't change. *A place figure changes (new sounding):* the
  survey updates the object; the source line's year updates with
  it; the gate's three-printings check re-runs.
- **Accessibility spec (v2).** A real `<dl>`; the silence output is
  NOT a live region (a polite announcement every minute is a
  ticking clock in the ear — refused); its value is available on
  demand in reading order. Figures `--snow` on `--fjord` 15.76:1;
  source lines `--mist-light` 6.73:1. The band's heading, if any,
  is a §3 section heading without reflection (law 4).
- **Tokens consumed (v2).** `--snow`, `--ice`, `--mist-light`,
  `--waterline`, `--ease-settle`.


### 6.16 The bottom (page family: footer)

- **What & why.** The footer is the fjord's bottom, and it behaves
  like one: the ground deepens to `--fjord` at its darkest, the
  plumb line (§6.6) arrives at its total, and the page's last act is
  a final sounding — a colophon that prints the depth reached, the
  silence kept, and the theme's fixed line: "This page makes no
  noise." It belongs because a page about depth must end at a
  measured bottom, not trail off into link farms; the footer is
  where the instruments are read one last time and agree.
- **Structure.** `<footer class="bottom">`: a `--waterline` hairline
  at its head (the last surface), then three quiet columns in the
  1080px field — the house (name, real address, coordinates), the
  chapters (the nav repeated as a plain list, §6.10's links at rest),
  the record (the final sounding block: "DEPTH SOUNDED — 214 M ·
  SILENCE KEPT — 6 MINUTES · THE WATER — 4 DEGREES", each value an
  output fed by the same objects as §6.6/§6.15) — then the colophon
  line: type credits, the year (computed), and the fixed line
  "THIS PAGE MAKES NO NOISE." in apparatus. No social icons (the
  theme has no icons §11), no newsletter form (a footer that asks
  again after the form chapter has asked is a second shout at the
  bottom of a quiet page — refused), no back-to-top button (the
  plumb line is the way back; a button would be a motor on a
  rowboat).
- **Motion spec.** The footer surfaces per §6.3 like any chapter
  (it is the last chapter). The final sounding's values do not count
  up — they are already true, having been measured all the way
  down; they print as the footer rests, crossfading 300ms from
  their apparatus labels' rest state. The depth value is the total
  (scroll fraction 1.0 at the footer's rest is the survey's
  definition of "bottom reached" — if the page's last chapter is
  short, the footer enters before fraction 1.0 and the sounding
  prints the *current* depth figure from §6.6's function with the
  label "DEPTH AT THE BOTTOM" — the instrument reports where the
  bottom actually is, never rounds itself to the total for
  tidiness; §1's law, applied at the last line of the page).
- **States.** *Rest:* printed, still. *Hover:* chapter links take
  §6.10's underline brighten. *Focus:* same + ring. *Active:* §6.9
  ring. *Scrolled-past:* n/a (it is the end). *Disabled:* n/a.
  *Touch:* identical.
- **Content merge.** The sounding block is the visit's record,
  generated: the depth from §6.6's function, the silence from
  §6.15's counter, the temperature from the survey object — three
  systems agreeing in one line, which is the page's closing proof
  that its instruments were real. The fixed line is the theme's
  signature and its promise, printed where promises are kept: at
  the end.
- **Failure fallback.** No JS: the sounding block prints the place
  figures only (total depth from the survey, temperature), the
  silence entry omitted (§6.15's absent-instrument ruling), the
  fixed line present. The footer loses the visit's record, never
  the place's.
- **Reduced-motion variant.** Identical, minus the crossfade. The
  footer was the stillest element already.
- **Performance budget & mobile variant.** Negligible. Mobile: the
  three columns stack in order house / record / chapters (the
  record rises in priority on a small screen — the visit's measure
  matters more than the sitemap), colophon wraps to two lines.
- **Choreography timeline (v2).** Footer top crosses 82% → surfaces
  (§6.3, 1400ms) → at rest, sounding values crossfade in (300ms) →
  plumb weight completes its settle (§6.6) in the same second →
  nothing further moves on the page except the sheen, which does
  not enter the footer (the bottom has no light; §5's sheen is a
  surface phenomenon and the survey forbids it below the last
  chapter).
- **State matrix (v2).** As States above; the one special cell:
  *the silence figure at footer rest* keeps counting while the
  visitor reads the footer (the visit is not over until it is
  over) — its cadence (§6.15) continues, and the figure the visitor
  photographs in memory is the one true at the moment they leave,
  which no static print could promise.
- **Breakpoints (v2).** ≥1200px: three columns. 768–1199px: two
  columns (house+record, chapters below). <768px: stacked per the
  mobile order above.
- **Edge cases & failure modes (v2).** *Footer reached by anchor
  jump:* the sounding prints the jump's true fraction values;
  nothing pretends the descent was read. *A page with no form
  chapter:* the record still prints (depth and silence need no
  conversion to be worth recording). *Year:* computed from the
  visitor's date — a colophon with a stale typed year is a small
  lie of exactly the kind this theme exists to refuse.
- **Accessibility spec (v2).** `<footer>` landmark; the sounding
  block is a `<dl>` like §6.15's; no live regions. Contrast: record
  values `--snow`/`--ice` on `--fjord` (15.76 / 12.16:1), labels
  `--mist-light` 6.73:1. The fixed line is text, not an image —
  it can be read aloud, which is the only sound this page will
  ever make, and it makes it in the visitor's own voice.
- **Tokens consumed (v2).** `--fjord`, `--waterline`, `--snow`,
  `--ice`, `--mist-light`, `--ease-settle`.

### 6.17 Matte-frame images (page family: media)

- **What & why.** Photographs — the house from the water, the room's
  window, the jetty in February — appear only inside matte black
  frames: a deep mat around the image, the image settling into its
  frame as it surfaces, and beneath it, inside the mat, its
  reflection scaling in mirror. It belongs because a fjord site
  needs its few photographs to behave like things seen across water
  — held in blackness, doubled faintly below — and because the
  theme rations images the way it rations ripples: a photograph is
  an event, and events are rare here.
- **Structure.** `<figure class="matte-frame">`: a `--fjord` mat
  (24px sides/top, 40px foot — the foot carries the caption and the
  reflection's water), the `<img>` in a clipped window, the
  reflection layer (a flipped, masked copy of the image at 14%
  opacity, blur 3px, in the mat's foot zone), and `<figcaption>`
  printed in the mat's lower edge in `--mist-light` caption style
  (§4's plate-line ruling). Aspect ratios are surveyed per image
  and reserved in CSS (`aspect-ratio`), so frames never reflow.
  Images are real photographs of the real place — the survey lists
  each with its subject and season; a stock photograph of a
  different fjord is a §1 violation in pictorial form.
- **Motion spec.** On surface (§6.3's queue): the image scales
  1.04→1 inside its window over 1200ms `--ease-settle` (scale-in-
  frame, the image settling into the mat like a print into a
  mount), while the reflection scales in mirror beneath it —
  0.96→1 from the reflection's own anchor — at 10%→14% opacity.
  The mat itself does not move. Parallax: the reflection drifts at
  0.94× against the image across the frame's viewport passage (the
  §5 licensed parallax) — the doubling lags a breath behind the
  thing doubled, as water insists. Hover: nothing (a photograph is
  not brightened by attention in this theme; §6.12's cards own the
  hover grammar). 
- **States.** *Unsurfaced:* frame and caption printed, image at
  rest (the scale arms only with JS). *Settling:* the 1200ms scale
  pair. *Rested:* image at 1.0, reflection at 14% / 3px, parallax
  live while the frame is on screen. *Scrolled-past:* rested;
  parallax continues on re-entry (it is a state of the water, like
  §6.4's sharpening). *Disabled:* n/a.
- **Content merge.** The caption is a sounding in prose: subject,
  season, and the figure the photograph proves ("The jetty, February
  — the water at 4 degrees, as §6.15 prints it"). The reflection is
  generated from the image itself (a flipped copy, never a second
  asset), so the doubling cannot disagree with the doubled. A frame
  whose caption could sit under any photograph is failed by §12's
  voice rules.
- **Failure fallback.** Image fails to load: the mat holds, the
  caption prints, and the window shows `--deep` with the apparatus
  line "THE PHOTOGRAPH DID NOT SURFACE" — the theme's image error
  is a sentence in its own voice, not a broken icon. No JS: image
  and reflection print at rest (reflection is a CSS-transformed
  duplicate in the DOM, not a canvas effect).
- **Reduced-motion variant.** Image at rest scale, reflection
  printed at 14% / 3px, no parallax. The frame remains a frame.
- **Performance budget & mobile variant.** Images are the page's
  weight budget (§14): ≤180KB each, ≤4 per page, `loading="lazy"`
  below the first chapter, decoding async. The reflection is a
  transformed reuse — no second download. Mobile: mat 16px / foot
  32px, parallax cut (small water, small doubling — the reflection
  sits still), scale-settle shortened to 900ms.
- **Choreography timeline (v2).** Frame enters queue (§6.3) →
  frame surfaces (1400ms rise shared with its chapter) → image
  scale-settle runs t=+200 to +1400 within the rise (finishing as
  the frame rests) → reflection mirror-scale completes t=+1500 →
  parallax engages while the frame is between 20% and 80% viewport
  → disengages outside it (loop gate; no writes off-screen).
- **State matrix (v2).** *Rest:* as above. *Hover:* none (see
  Motion spec). *Focus:* frames are not focusable unless the image
  is a link (a build may link the jetty photograph to its chapter;
  then §6.10's brighten applies to the caption and the focus ring
  draws on the mat's outer edge — never on the image, which is not
  a button's face). *Active:* §6.9 ring centred on the frame if
  linked. *Scrolled-past:* rested. *Disabled:* n/a. *Touch:*
  parallax off (it is cut on mobile), settle identical.
- **Breakpoints (v2).** ≥1200px: mat 24/40px, frame max-width
  880px in the field. 768–1199px: mat 20/36px. <768px: mat 16/32px,
  frame full column width, caption 13px.
- **Edge cases & failure modes (v2).** *Portrait photographs:* the
  mat geometry holds (the frame is surveyed per image); the
  reflection's mask shortens — a tall image's reflection drowns
  faster, which is correct optics and stated so no builder
  "balances" it. *Missing aspect ratio in CMS:* the frame reserves
  4:3 and the gate flags it; a reflow in this theme is a dropped
  stone — visible, and counted. *WebP/AVIF failure:* the `<picture>`
  fallback chain is the platform's; the mat and caption are
  format-blind.
- **Accessibility spec (v2).** Real `alt` text describing the
  photograph's subject and season (the caption is not the alt —
  the caption is a sounding, the alt is a description; a screen
  reader deserves both, different). The reflection copy is
  `aria-hidden` and `alt=""`. Contrast: caption 6.73:1 on the mat.
  Images never carry text; a photograph with lettering in it is
  refused at survey.
- **Tokens consumed (v2).** `--fjord`, `--deep`, `--mist-light`,
  `--ease-settle`, `--dur-frame-settle` (1200ms).

### 6.18 The un-surfaced page (page family: 404 / empty state)

- **What & why.** The 404 is a page that never rose: a dark screen,
  the heading "This page has not surfaced." in Spectral at reading
  size (§3 law 5), one line of Record explaining what a sounding
  found instead, the plumb readout printing a dash where the depth
  would go, and the way back — the chapters, listed as reaches to
  return to. It belongs because getting lost in this theme is a
  depth event: the visitor sounded for a page and the line found
  no bottom at that bearing, and the theme reports that honestly
  instead of performing a mascot with a map.
- **Structure.** A full page on the standard scaffold: header
  (§6.10), one chapter containing the heading, the explanation
  ("The direction you gave — /the-old-jetty — is not a reach of
  this water." — the requested path printed from the request, in
  apparatus), a short list of real chapters with their soundings
  (§6.15's grammar), and the footer (§6.16) whose record omits the
  depth line (there is no depth to record) and keeps the fixed
  line. The plumb line (§6.6) does not render; in its margin place,
  at ≥1200px, the readout prints "— M" once, static: the
  instrument, shown honestly idle.
- **Motion spec.** Almost none, and that is the spec: the heading
  does not surface (a page that has not surfaced cannot perform
  surfacing — §6.3 is withheld, the one place the theme refuses its
  own verb). The chapter list stands at rest. One licensed motion:
  the §6.9 click ripple still answers touches, because the water is
  still water even where the page is missing. The sheen does not
  run. The page is the stillest in the theme, and its stillness is
  the message's second sentence.
- **States.** *Rest:* printed, still. *Hover/focus:* chapter links
  per §6.10. *Active:* §6.9 ring. All other states n/a — the page
  has one state, which is the point.
- **Content merge.** The requested path is the visitor's own input,
  printed back; the suggested chapters are the site's real reaches
  with their true soundings; the explanation names the failure in
  the theme's geography rather than in HTTP's ("404" appears once,
  in the apparatus eyebrow, for the record — the theme is honest
  with machines too).
- **Failure fallback.** The 404 is itself a fallback; its own
  fallback is that it is static HTML requiring nothing — if even
  the scaffold fails, the server's plain error is outside the
  theme's jurisdiction, and the survey says so.
- **Reduced-motion variant.** Identical (there was no motion to
  reduce; the click ripple rests per §6.9's ruling).
- **Performance budget & mobile variant.** The lightest page on the
  site; mobile identical in grammar, heading 26px.
- **Choreography timeline (v2).** None — stated as a timeline so no
  builder invents one: t=0 the page stands. The absence is the
  choreography.
- **State matrix (v2).** Rest only, plus link states per §6.10 and
  the ring per §6.9. *Scrolled-past:* the page is one screen; n/a.
  *Disabled:* n/a. *Touch:* ring live, all else still.
- **Breakpoints (v2).** ≥1200px: margin readout "— M" shown.
  768–1199px: header sounding shows "— M". <768px: the dash appears
  in the record line only; heading 26px.
- **Edge cases & failure modes (v2).** *Search empty state* reuses
  this page's grammar in miniature (§11's search): the same
  heading voice, the sought term printed, real alternatives listed
  — one emptiness language across the site. *Soft 404s (a chapter
  with no content):* forbidden by the survey — an empty chapter is
  removed from the nav and the plumb's chart, not dressed as a
  reach. *Path with markup in it:* the printed direction is escaped
  text, always — the theme prints the visitor's words, it does not
  execute them.
- **Accessibility spec (v2).** The heading is the h1; the HTTP
  status is correct (the theme's honesty extends to the server);
  the chapter list is a real list of links with §6.10's focus
  treatment; contrast per §2 throughout. A screen reader hears a
  short, complete page — the emptiness is visual and temporal,
  never informational.
- **Tokens consumed (v2).** `--fjord`, `--snow`, `--ice`,
  `--mist-light`.


## 7. Page application map

| Page type | How the theme plays out |
|---|---|
| **Home** | The full descent: water panel (§6.11), chapters separated by 30–45vh pauses (§4), the long pause (§6.7) between 40% and 70% of depth, figures band (§6.15) late (the visitor must have descended before being shown the soundings), crossing form (§6.13) as the penultimate chapter, the bottom (§6.16). Total depth declared from the place (Quiet House home: 214 m). Chapter cap: 7 (§6.10's ruling). |
| **Listing** (rooms, waters, backlist) | A shallow page by design: panel-less opening (a chapter head at the surface, no second ripple ceremony — §6.1 fires on the home page's load and on direct landings only), card chapter (§6.12) after one short pause, figures band optional and only with true figures. Total depth smaller and declared so (a listing of four rooms might sound 60 m — the metres are the page's own scale from the survey, always the same metres-per-fraction rule per page, never stretched to look deep). |
| **Detail** (one room, one water, one book) | The deepest single-subject page: the subject's matte frame (§6.17) as its hero (no water panel — the subject *is* the surface here), its figures as in-copy soundings (§6.8), one card row of its siblings at the foot ("the neighbouring reaches"), the crossing form pre-set to the subject (§6.13's record grammar). Reflections belong to its one headline only (§3 law 4). |
| **About** (the house, the practice) | A narrative descent: chapters as reaches of a life or a place's history, each with its waterline and sounding; the long pause (§6.7) carries the founding sentence; portraits only in matte frames (§6.17) with season captions. The about page is where the theme's slowness is most defensible and most tested — §9's "pause with nothing in it" failure lives here. |
| **Contact / booking** | The crossing form (§6.13) as the whole page's purpose: a short descent (two chapters: the directions — real directions, with the crossing's minutes as a §6.8 figure — then the form), the bottom (§6.16) with the record. No figures band: a contact page that boasts has misunderstood itself. |
| **404 / empty** | §6.18, the un-surfaced page. Search results and empty listings reuse its grammar in miniature. |

**Cross-page rules.** The ripple ceremony (§6.1) belongs to arrival
from outside; internal navigation arrives by §6.14's crossing and
never re-runs it. The plumb line's total is per page, declared per
page in the survey — the metres are consistent (one metre is one
metre of the place's water everywhere), the totals differ because
pages, like reaches, have different depths. The pause (§6.7) appears
on home and about only, once each.

## 8. Worked examples

The Quiet House at Fjellstrand: four rooms above a fjord arm, run by
two people, let by the week, closed in the dark months. All figures
below are the survey's: the arm below the house sounds 214 m at the
jetty; the water is 4 degrees in February; the crossing from the
railway at Myrdal takes 47 minutes by boat. The examples are the
home page's three load-bearing sections, end to end.

### 8.1 The hero — arrival at the surface

The visitor arrives from a search result at 21:40 on a February
evening — the theme's home hour. First paint (t=0): the finished
panel stands — header (§6.10) at rest, the h1 "The Quiet House" in
Spectral 200 at 64px, its reflection printed beneath at rest
sharpness, the standfirst ("Four rooms above the water at
Fjellstrand. Let by the week. Closed in the dark months."), the
action "ASK FOR A ROOM", and at the panel's foot the descent line:
"THE WATER IS 4 DEGREES IN FEBRUARY." Nothing is hidden; a visitor
whose connection dies here has the whole offer.

Then the ceremony layers onto the finished screen. t=200: the
ripple (§6.1) is born at the panel's centre, ice at 55%, and begins
its 3000ms widening. t=350: the loop confirms alive; the headline's
pre-state arms. t=600: "The Quiet House" begins its rise (§6.2) —
40px, 1600ms, `--ease-surface`, opacity leading — eleven characters,
under the 48-letter cap, so it surfaces whole rather than lettered
(the survey chose whole: a house's name should arrive like a boat,
not like rain). The ripple passes behind it. t=1800: the standfirst
surfaces (§6.3 queue). t=2020: the action surfaces. t=1850: the
headline's 2px bob; t=2200 it rests. t=2400: its reflection's scrub
window (§6.4) opens — as the visitor begins to scroll, the mirrored
name will soften-sharpen through the first 60vh. t=3200: the ripple
is gone, node removed. The plumb (§6.6) stands at −0 m. The sheen
drifts. The surface is closed. Total ceremony, 3.2 seconds, of which
the visitor was free to read for all of it — nothing was ever
covered, gated or delayed; the page performed its arrival *around*
its content, not instead of it. Scroll timeline: the first chapter's
waterline enters after 34vh of empty water (§4's pause), its head —
"The rooms" — surfacing at the 82% line with its sounding, 31 m,
printed at its waterline's right end: the visitor has descended
31 metres to reach the rooms, and the page has told them so three
ways (line, figure, waterline) that all agree.

### 8.2 Mid-page — the rooms and the held breath

The rooms chapter lists four cards (§6.12): ROOM 1 — FACES THE
WATER ("The window is 6 metres from the jetty edge — measured from
the jetty"), ROOM 2 — FACES THE CLIFF, ROOM 3 — THE LONG ROOM,
ROOM 4 — UNDER THE ROOF, each with three fact lines and its figure.
They surface one at a time, 220ms apart, as the chapter arrives. The
visitor hovers Room 1: the card tilts 1.1° toward the pointer — felt,
not seen — its title brightens to snow, its small reflection warms.
They do not click. They scroll on, through 40vh of empty water in
which only the plumb line moves (now passing −88 m), and the long
pause (§6.7) takes the screen: one line, Spectral at 30px, centred,
alone — "The fjord was here before the house. It will be here
after." For 70vh of scroll nothing on the page moves except the
plumb line descending beside the emptiness, −91 m to −118 m: the
silence has a depth, and the visitor watches it deepen. Across the
last 30vh the line dims to 38% — sinking, not vanishing — and the
figures chapter's waterline rises into view. The visitor's dwell
counter (§6.15) has been counting throughout, visibility-gated; by
the pause's end it holds 3 minutes, most of them earned exactly
here. This section is the theme's whole argument in one scroll: a
listing, an emptiness with a gauge beside it, and a sentence that
the emptiness made heavier. Remove the pause and the page is a
quiet brochure; with it, the page has *done* the thing it sells.

### 8.3 Conversion — asking for the room

Below the figures band (214 m sounded at the jetty; 47 minutes the
crossing; 4 degrees the water — each with its source line, §6.15),
the penultimate chapter is the crossing form (§6.13), pre-set from
§8.2's near-click: the survey's rule is that a card's click would
have pre-set its room; hovering did not — the form opens with no
room chosen, because attention is not intent and the theme does not
presume. The visitor picks Room 1 from the radio seam list (its
figure travels with it: "6 metres from the jetty edge"), gives a
name and a direction, sets arrival and departure from the native
date lines, writes one sentence in the ruled textarea ("We would
like the quiet, if the quiet is available."). Focus moves field to
field: each rule inks to ice over 400ms, each plumb tick descends
beside the label. They submit. The §6.9 ring centres on the button;
the label crossfades to "ASKING…"; the sheet holds still — no
spinner, because the wait is the house's and it is short. The answer
returns: the sheet gives way over 600ms to the ledger line —
"ASKED. THE HOUSE ANSWERS WITHIN A DAY." — with their room and
dates restated from their own input. Below it, the bottom (§6.16):
the final sounding prints DEPTH AT THE BOTTOM — 203 M (the page's
fraction where the footer rests — not the rounded total, §6.16's
ruling), SILENCE KEPT — 6 MINUTES (the same counter §6.15 showed,
agreeing), THE WATER — 4 DEGREES. Then the colophon, and the last
line of the page: "THIS PAGE MAKES NO NOISE." The conversion took
one screen, asked four questions and a sentence, and closed by
reading the instruments back to the visitor — the ask, the depth
and the quiet all in one record.


## 9. Anti-slop — what makes THIS theme look cheap

Each failure below is specific to this water; each cure is the rule
that was broken, restated at the point of failure.

1. **The stock fjord photograph in the hero.** A beautiful aerial of
   Geiranger at golden hour behind the headline. It is cheap because
   it is a picture of the thing instead of the thing, and because it
   is somebody else's fjord. *Cure:* §6.11 — the hero is water, not
   a view of water. Photographs live in matte frames (§6.17), of
   the real place, rationed.
2. **Scandi-minimal drift.** The page quietly becomes a white-space
   minimal portfolio with a dark background: sans headlines, tight
   leading, sections stacked efficiently. *Cure:* §3's laws (Spectral
   ExtraLight, leading 1.78) and §4's pauses (30–45vh) are the
   theme's body; a build review that measures "wasted space" has
   brought the wrong instrument.
3. **The second ripple.** An ambient ripple loop on the hero, a
   ripple on every hover, ripples in the footer "for continuity".
   *Cure:* the one-ripple law (§1). One ring on load (§6.1), one per
   click (§6.9), none in the pause (§6.7), no loops. The gate counts
   ring nodes and trigger sites.
4. **Invented depths.** "Descend 500 metres" on a page whose place
   sounds 214; a silence figure typed as "visitors stay 12 minutes"
   in a stats band. *Cure:* §1's law and §6.15's source lines. Every
   figure is computed, counted or sourced — or absent.
5. **A progress bar.** A thin filled bar at the top "because users
   expect progress feedback". *Cure:* §6.6 is the progress, and it
   is a sounding, not a fill. The bar is refused in §11 by name.
6. **Pop-ups in the pause.** A cookie banner, a chat bubble or an
   exit-intent modal arriving during §6.7's held breath. *Cure:*
   the theme has no modal, toast or banner components (§11) — the
   refusal is structural. Consent, where law requires it, is a
   chapter, not an overlay.
7. **Hurried motion.** Surfacing at 500ms "for snappiness", stagger
   at 60ms, count-ups at 800ms. Each is a small vandalism of the
   same kind: the theme's durations are its voice. *Cure:* §5's
   ledger is binding; the gate times the ceremonies in a scripted
   pass.
8. **A marketing line in the pause.** "Book now for 20% off" alone
   on the held screen. The pause is the theme's church; the line in
   it is a sentence of consequence (§6.7, §3 law 5). *Cure:* the
   survey approves the pause line by name, and §12's voice rules
   govern it.
9. **Reflections everywhere.** Mirrored underlines, mirrored cards,
   mirrored body text, a mirrored logo. *Cure:* §3 law 4 — headlines
   and card titles only, generated from their own text, at the
   licensed blurs. A reflection you can read is a duplicate; a
   reflection on everything is a funfair.
10. **Blue water.** The palette drifting toward spa-blue, teal
    accents, a friendly cyan link colour. The fjord is black-green;
    the moment the water turns blue the page is a brochure for a
    resort. *Cure:* §2's closed token list. Links are ice and snow;
    there is no accent colour in this theme, and the absence is the
    brand.
11. **The tilt you can see.** Card tilt at 4–6° "so users notice the
    interactivity". *Cure:* §6.12's 1.2° cap and the felt-not-seen
    gate test. Interactivity in this theme is confirmed by the
    ripple (§6.9), not by gymnastics.
12. **Noise in the copy.** Exclamation marks, "Welcome to our
    website!", a chatbot named after a wave. *Cure:* §12 — the
    Record's voice, the banned list, and the fixed final line. The
    page makes no noise; its sentences don't either.

## 10. Quality gate

Blocking items (all must pass; a single failure holds the build):

1. **Depth-law audit.** Every metre figure on the page is traced to
   the survey's total and the scroll fraction (§1). Scripted check:
   at fractions 0.25 / 0.5 / 0.75 / 1.0, the plumb readout (§6.6),
   the nearest waterline sounding (§6.5) and the figures band
   (§6.15) agree to the metre. Any typed depth anywhere = fail.
2. **Silence-truth test.** In a scripted session with the tab hidden
   for a known interval, the silence figure (§6.15) excludes the
   hidden time, and the footer (§6.16) prints the same value as the
   band at the same moment.
3. **One-ripple census.** Exactly one ring node exists in the code;
   trigger sites are load (§6.1) and click (§6.9) only; the pause
   (§6.7) contains no trigger; no ambient ripple loop exists in any
   stylesheet.
4. **Pause census & placement.** Exactly one `.pause` per eligible
   page (home, about), sitting between 40% and 70% of page depth,
   its line approved in the survey, its screen free of any other
   element, overlay or hint.
5. **Fallback rehearsal.** With JS disabled, the full page reads
   complete: headline at rest, reflections printed at 2px, figures
   final, form submittable, plumb at full sounding. With the loop
   killed mid-session, every armed element rests within its
   watchdog (surfacing ≤2000ms, §5).
6. **Duration audit.** Scripted timings: ripple 3000±100ms, headline
   rise 1600±80ms, section rises 1400±80ms with ≥220ms sibling
   intervals, lift 1200±60ms, count-ups within §6.8's ledger bands.
7. **Contrast audit.** Body text pairings per §2's table; a grep for
   `--mist` in any text-carrying rule fails the build (it is lines,
   not letters); reflections confirmed `aria-hidden`.
8. **Reflection census.** Reflections exist only under chapter/hero
   headlines and card titles (§3 law 4), each generated from its
   own text — an edited headline with a stale reflection = fail.
9. **Tilt test.** Card tilt measured at ≤1.2° in a scripted hover;
   three reviewers asked whether they *saw* it — the pass is "felt
   something, saw nothing much".
10. **Form-keeping rehearsal.** A simulated network failure on
    submit leaves every field's content intact with §12's failure
    line; a no-JS submission completes against the real `action`.
11. **Photograph provenance.** Every image is listed in the survey
    with subject, place and season; captions carry the figure the
    photograph proves (§6.17). A stock image = fail.
12. **Quiet audit.** No autoplay media, no modal/toast/banner
    components in the build, no exclamation mark in the page's copy
    (§12), the fixed final line (§6.16) present and verbatim.


## 11. Component inventory

Every component a real Fjord Stillness site needs, with its themed
treatment. Refusals carry their in-theme replacement — a refusal
without a replacement is a gap, not a stance.

| Component | Themed treatment |
|---|---|
| Primary button | The still button: apparatus label, `--ice` text on transparent ground, a 1px rule beneath with its reflection (§6.10's grammar at button scale); hover brightens rule + text to `--snow` over 600ms `--ease-drift`; active = §6.9's ring + 1px press. No fill, ever — a filled button is a buoy, and this water has none. |
| Secondary button | Ruled text link with the mirrored underline (§6.10), apparatus, left-aligned. |
| Text input | Inscription line (§6.13): apparatus label above, 1px `--mist` rule below, focus inks the rule and descends the plumb tick. No boxes, no fills, no placeholder text (a placeholder is a rumour of a question; the label is the question). |
| Textarea | Ruled sheet (§6.13): lines at the body line unit (17px × 1.78 ≈ 30px), Inter 300. |
| Select | Refused. Choices are seam lists — ruled radio lines carrying each option's figure (§6.13's room list generalised). A fjord house lays its rooms out; it does not hide them in a dropdown. Native date inputs are the one platform control retained, minimally restyled. |
| Checkbox | A small square of `--mist` rule; checked = the square fills with `--ice` at 30% and a plumb tick stands beside it. Label in body text, never apparatus — consent is a sentence, not a label. |
| Radio | Seam line (§6.13): the chosen line's rule inks to `--ice` and its figure prints in `--snow`; the dot is a 5px lead weight (the plumb's weight at pocket size). |
| Toggle / switch | Refused. States of a visit are not switched; use two seam lines as radios ("In the house / On the water"). |
| Card | Chapter card (§6.12): floating, tilt ≤1.2°, title reflection at rest, figure with source. |
| Table | The soundings table: real `<table>` for any genuine matrix (crossing times by season), apparatus headers, no zebra striping — row rules are `--waterline` hairlines; figures tabular (§3). A table in this theme is a tide table or it is not shipped. |
| Tabs | Refused. Depth is not tabbed; content is descended to (§6.3) or listed (§6.12). A build asking for tabs has two chapters arguing — give them a pause and an order. |
| Accordion | The sounding fold: a chapter sub-section whose body surfaces (§6.3 grammar) when its waterline heading is activated; one fold open per chapter; the heading's sounding updates to the fold's depth. Used sparingly — a fold is a reach within a reach. |
| Modal / dialog | Refused, structurally (§6.7, §9). There is no overlay in this theme. Confirmations are inline ledger lines (§6.13); consent, where required, is a chapter with its own waterline. |
| Toast | Refused. News is recorded, not toasted: transient confirmations appear as a line in the record (§6.16's grammar) at the place they concern. |
| Tooltip | Refused. Explanation lives in source lines and captions (§6.15, §6.17); a figure that needs a tooltip needs a better source line. |
| Badge | The sounding chip: apparatus text stating a measured fact only — "214 M AT THE JETTY", "4 DEGREES IN FEBRUARY". Marketing badges ("NEW", "POPULAR") are banned words wearing a component's clothes (§12). |
| Alert | The raised-water band: a `--deep` seam cut into the current ground, `--ice` text, `--waterline` left rule, §12's error voice, persistent until resolved. On the form it is §6.13's summary line. It never overlays, never auto-dismisses — weather on a fjord is waited out, and so is an error. |
| Pagination | Reaches: "Further down the water" / "Back toward the surface" links lettered with the next reach's first chapter name — never numbered pages; the water is continuous and the plumb (§6.6) already numbers the descent in metres. |
| Progress bar | Refused. Progress is the plumb line (§6.6). |
| Spinner | Refused. Waiting is the "ASKING…" apparatus label (§6.13) or the sounding block (§6.14); the water does not spin. |
| Skeleton | §6.14's un-surfaced blocks with "SOUNDING…" and the 6000ms confession. |
| Search | The record search: one inscription line in a late chapter; results return as chapter cards (§6.12) with their soundings; zero results print §6.18's grammar in miniature. Search is a sounding taken across the site's reaches. |
| Breadcrumbs | Replaced by the nav's current-chapter underline (§6.10) plus the plumb readout (§6.6): position here is a depth and a reach, not a trail. |
| Skip link | "Skip to the water" — a plain `--ice` link on first focus above the header. |
| Focus ring | 2px `--snow` outline, offset 3px, everywhere; on cards it draws the card's edge (§6.12). In this dark theme the ring is the brightest object on the page when it shows, which is correct: focus is the visitor's own light. |
| Divider | The waterline (§4): 1px `--waterline` across the content column with a sounding at its right end. Full-bleed dividers and wavy SVG "wave" dividers are refused — waves are another theme's weather; this water's surface is a line, not a frill. |

## 12. Content & copywriting voice

Two voices. **The Instrument** writes apparatus: labels, soundings,
nav, buttons — Inter, uppercase, letter-spaced, terse, every figure
tallied and sourced. **The Record** writes prose: standfirsts,
chapter text, errors, confirmations, the pause line — Spectral for
sentences of consequence, Inter Light for the rest, plain and
unhurried, the voice of someone writing the house's log for whoever
comes next winter. The voices never swap: the Instrument never
sentences, the Record never shouts.

**Headline style.** The place and its fact, stated. ✓ "The Quiet
House" / "Four rooms above the water". ✗ "Escape to Serenity!!!"
(exclamation, a command, and a claim with no fact in it). ✗
"Welcome to Fjellstrand's Premier Wellness Destination" (a brochure
that has wandered into the wrong water). Headlines are short because
they must reflect (§6.4) — a headline too long to mirror is too long
to say.

**Label style.** Apparatus: noun + figure. ✓ "ROOM 1 — FACES THE
WATER", "DEPTH AT THE JETTY — 214 M", "THE CROSSING — 47 MINUTES".
✗ "Room One (Our Most Popular!)", "Depth: lots", "Fast transfer
available". Percentages are banned from labels: a depth is in
metres, a silence in minutes; nothing here is 87% of anything.

**Error voice.** A fact of the water, stated plainly, with the way
back. ✓ "The departure is before the arrival. The water cannot be
crossed backwards." ✓ "THE ASK WAS NOT CARRIED — THE HOUSE COULD
NOT BE REACHED. YOUR WORDS ARE KEPT ABOVE." ✗ "Oops! Something went
wrong 😞" (the fjord has no "oops", and no emoji survives the cold).

**Empty-state voice.** ✓ "This page has not surfaced." / "Nothing
has been found in these reaches by that name." ✗ "No results found.
Try being less specific?" — the Record does not blame the visitor
for the water's gaps.

**Confirmation voice.** ✓ "ASKED. THE HOUSE ANSWERS WITHIN A DAY."
✗ "Success! 🎉 Your booking journey is complete!" — a confirmation
is a sounding read back, not a celebration.

**The pause line** is governed separately: one sentence, true of the
place, no offer in it, approved by name in the survey (§6.7). ✓
"The fjord was here before the house. It will be here after." ✗
"Take a breath. You deserve this." (an instruction to feel, from a
page that has earned the right only to state).

**Banned words:** amazing, stunning, breathtaking, escape (as a
verb of command), unwind, recharge, wellness journey, oops, NEW /
POPULAR (as badges), book now, limited availability, seamless,
vibrant (this water is not vibrant; it is deep).
**Owned words:** surface (verb), sounding, reach, depth, the water,
still, kept (of silence), asked (of bookings), at the bottom,
measured, in February (the theme's figures carry their season).

**Fixed strings (verbatim, do not paraphrase):** the final line —
"THIS PAGE MAKES NO NOISE."; the 404 heading — "This page has not
surfaced."; the skeleton confession — "Nothing has surfaced here
yet."; the form failure line — "THE ASK WAS NOT CARRIED — THE HOUSE
COULD NOT BE REACHED. YOUR WORDS ARE KEPT ABOVE."; the confirmation
— "ASKED. THE HOUSE ANSWERS WITHIN A DAY."


## 13. Full-page scroll choreography map

The home descent, top to bottom. Every beat in order; instruments
run continuously beneath the beats (the plumb line §6.6 sounding,
the dwell counter §6.15 counting visible time, the sheen §5
drifting while the surface chapters live).

| Beat | Scroll zone | What happens | What the visitor feels |
|---|---|---|---|
| 1 | Load | Ripple (§6.1), headline surfaces (§6.2), standfirst + action surface (§6.11) | Arrival on still water |
| 2 | 0–34vh | Empty water; the headline's reflection sharpens through its window (§6.4); plumb passes −12 m | The descent begins, measured |
| 3 | Chapter 1 waterline | "The rooms" head surfaces, its lift (§6.5) breaks, sounding 31 m printed | The first reach |
| 4 | Rooms chapter | Four cards surface one at a time (§6.12); a hover tilts one, felt not seen | Drifting across the rooms |
| 5 | 40vh pause | Nothing but the plumb: −52 m to −88 m | Depth accumulating in silence |
| 6 | The long pause | Pinned screen, one line (§6.7); plumb −91 m → −118 m beside the emptiness; sheen suspended | The held breath |
| 7 | Pause release | The line dims to 38% across 30vh; figures chapter's waterline rises | Released, not ejected |
| 8 | Figures band | Soundings count slowly (§6.8 via §6.15): 214 m, 47 minutes, 4 degrees; the silence figure already holds its true minutes | The page shows its arithmetic |
| 9 | Craft chapter | One matte frame (§6.17): the jetty in February, image settling, reflection doubling | The place, proved |
| 10 | Crossing form | The sheet surfaces whole (§6.13); radio seam lines carry the rooms' figures | The ask, on quiet water |
| 11 | Submit | Ring on the button (§6.9), "ASKING…", the ledger confirmation surfaces at half-rise | Asked, and recorded |
| 12 | The bottom | Footer (§6.16): depth at the bottom 203 m, silence kept 6 minutes, the fixed line | The bottom, sounded |

**Reverse pass.** Scrolling up: reflections soften back through
their windows (§6.4), the plumb shortens exactly retracing (§6.6),
the pause re-pins and its line re-brightens (§6.7) — and nothing
un-surfaces, nothing un-counts, the confirmation does not un-ask.
The page going up is the same water with its states of surface
reversed and its records kept. That asymmetry — water forgets,
the log remembers — is the theme's grammar, stated in §6.3, §6.4
and §6.8 so no builder harmonises it away.

**Jump-scroll catch-up.** Anchor jumps and flings: everything in
the skipped span rests instantly (§6.3's fling rule), counts
complete (§6.8), the plumb figure lands exact (it is a function,
not a traveller), the pause — if landed inside — holds from the
landing point with its line at the opacity its window dictates.
No ceremony is owed to a teleport.

## 14. Whole-page performance budget

| Budget | Limit |
|---|---|
| Total page weight (home) | ≤ 640KB, of which images ≤ 420KB (≤4 matte frames, §6.17) |
| Fonts | Spectral (2 weights) + Inter (2 weights) ≤ 120KB, `font-display: swap` |
| JS | ≤ 55KB gzipped (one loop, two observers, dwell counter, form) |
| Shared-loop cost | ≤ 1.6ms/frame average; writes only transform / opacity / filter on the one live reflection |
| Long tasks | None > 50ms after load; the load ceremony is class-triggered CSS, not scripted frames |
| Surfacing latency | Any triggered rise settled ≤ 2000ms after trigger (the §5 hard cap, watchdog-enforced) |
| Live blurred layers | ≤ 1 (the reflection in its open window, §6.4) — a second window never opens while one is live |
| Concurrent rises | ≤ 2 (§6.3); concurrent counts ≤ 3 (§6.8) |

**Cut order when the budget is exceeded** (cut in this order,
record each cut in the build notes):

1. Card-title reflections (§6.12) — titles stand alone; chapter
   reflections are never cut.
2. The sheen (§5) — to a static 3% gradient in the hero, then gone.
3. Matte-frame parallax (§6.17) — reflections sit still beneath
   their images.
4. Card tilt (§6.12) — cards rest flat; hover keeps the brighten.
5. Body-block surfacing (§6.3's low-power ruling) — chapter heads
   keep the rise; inner blocks stand at rest.
6. The surface-crossing transition (§6.14) — navigation becomes a
   plain swap with the §6.10 header standing.

**Never cut:** the depth law's single function and its three
printings, the watchdogs and the 2000ms cap, the one-ripple census,
the pause, the form's error-keeping, any reduced-motion variant,
the footer's fixed line. A build that cuts the measurement to keep
the mood has made fog, not a fjord.

## 15. Build-order checklist

1. Survey first: fix the place's true figures (the total depth and
   its source, water temperatures by season, crossing times, room
   facts), the chapter list (≤7) with each chapter's sounding rule,
   the pause line by name, and the data object that the plumb,
   waterlines, figures, cards and footer will all render from.
   Write the survey; everything else is generated from it.
2. Build the static water: all chapters surfaced, reflections
   printed at 2px, figures final, form working with no JS. This is
   the site; the rest is weather laid over a finished fjord.
3. Set the palette tokens and the pairing law (§2); audit contrast
   per the measured table, including the `--mist` text ban, before
   any motion exists.
4. Set the type scale and laws (§3); verify every headline fits its
   reflection (law 4) at every breakpoint.
5. Lay the water column and the pauses (§4): measure the
   inter-chapter water at all three breakpoints (30–45vh desktop,
   never below 24vh anywhere).
6. Build the instruments from the data object: plumb line (§6.6),
   header sounding (§6.10), figures band (§6.15), footer record
   (§6.16). Verify the three-printings agreement by scripted
   session before any ceremony is added.
7. Add the shared loop (lerp 0.08); wire reflection scrubbing
   (§6.4) and card tilt (§6.12) with their loop gates.
8. Add surfacing (§6.3) with the queue, the fling rule and the
   2000ms watchdogs; then the waterline lift (§6.5) under the same
   watchdog.
9. Add the ceremonies: ripple (§6.1), headline surfacing (§6.2),
   count-ups (§6.8), click ripple (§6.9) — in that order, each
   rehearsed against its fallback.
10. Pin the pause (§6.7) and verify the census (one), the placement
    (40–70% of depth) and the empty screen by screenshot at three
    scroll positions inside the pin.
11. Build the crossing form (§6.13) with error-keeping rehearsed
    against a simulated network failure and a no-JS submission.
12. Add matte frames (§6.17) with provenance from the survey;
    skeleton and crossing (§6.14); the un-surfaced page (§6.18).
13. Run the full gate (§10) including the hidden-tab silence test
    and the duration audit; sign-off by a non-builder — the person
    who sounds the fjord is never the person who claimed its depth.
