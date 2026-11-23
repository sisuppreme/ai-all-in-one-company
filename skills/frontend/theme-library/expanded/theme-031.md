# 31. Basalt Cathedral — Expanded (v1 + v2)

> Expansion of theme #31 from `themes-026-050.md`, written directly to
> the full standard: the v1 10-part structure plus the v2 deepening
> layers (per-element choreography timelines, state matrices, breakpoint
> behaviour, edge cases, accessibility specs and token lists; per-theme
> component inventory, copywriting voice, three worked examples, scroll
> choreography map, performance budget, build-order checklist).
> Identity preserved exactly: the same concept, the same five palette
> anchors, the same two typefaces, the same nine signature elements —
> deepened, never redesigned — plus three signature-grade elements drawn
> from the original motion system and six page-family elements.

## 1. Concept & world

A cooling lava flow does not ask permission to become architecture. As
the surface of a thick basalt flow contracts, it cracks into hexagonal
columns — five, six, seven sides, fitted together with no mortar and no
waste — and those columns stand for tens of millions of years. This
theme takes that literally: **the page is a columnar cliff, and the
layout grid is the columns themselves.** Content does not sit *on* a
background decorated with hexagons; each content block *is* a basalt
pillar, hexagonal in cap, staggered in height against its neighbours,
separated by the hairline joints where the stone cracked as it cooled.
Sections are strata — horizontal bands of differing depth that shear
slowly past one another as the visitor descends. The footer is bedrock:
the one block on the page that never moves, never parallaxes, never
performs, because bedrock is what everything else stands on.

The page moves at geological speed, and that is a system, not a mood.
Every motion in this theme is either **scrubbed to the visitor's own
scroll** (the fissure widening, the strata shearing, the rust light
creeping down the column edge — the visitor's hand does the work, the
stone merely responds) or **slower than 600ms** (the 2s column rise, the
600ms glow seep, the 1.4s hexagon draw). Nothing springs, nothing
bounces, nothing overshoots. Weight is performed by the shared scroll
loop's heavy lerp (0.08 — the heaviest in the library): rendered values
lag the visitor's scroll the way a heavy thing lags a push, slow to
start and slower to stop.

**The theme's one law: weight is truth.** Every element that moves
must move like stone — and the law has exactly one exception, written
into §6.2: **fracture.** Stone does one fast thing, and that is crack.
The 90ms snap that closes the headline's fractured joints is the only
sub-600ms, hard-eased motion permitted anywhere in the theme. A build
containing a spring easing, an ease-out-back, a bounce, or a second
fast snap has not bent the theme; it has broken the only physical
promise the theme makes, and the quality gate (§10) fails it by grep.
Everything else in this document is craft. That one is physics.

**The figures are geology too.** Where the page states ages, depths
and counts — and this theme loves stating them, in chiselled numerals
(§6.11) — they are the subject's real published figures: the real age
of the formation, the real depth of the borehole, the real number of
columns in the organ. A counter that counts to an invented number is a
lie told slowly, which this theme considers worse than a lie told
quickly. The gate audits figure provenance (§10).

**Best-fit sites and audiences.**

- Geology made public: geological surveys, natural-history museums,
  national-park and geopark sites, quarry and stone-industry firms —
  anywhere columnar basalt, strata and deep time are the literal
  subject and the grid can be the outcrop.
- Institutions that want to feel old and load-bearing: universities,
  archives, foundations, law and engineering firms with a century
  behind them — organisations whose claim is *we were here before you
  and will be here after*, stated in stone rather than in a tagline.
- Heavy industry presented honestly: mining, tunnelling, dam and
  infrastructure engineering, where mass and permanence are the
  product and a fast, springy interface would be a category error.
- Long-form deep-time storytelling: essays and exhibits about
  extinction, ice ages, continental drift — reading experiences where
  a 150vh pinned gallery and a 2s entrance are the correct pace.
- Memorial and commemorative sites, where slowness is respect and the
  bedrock footer's absolute stillness is the right final statement.

**When NOT to use it.**

- For anything urgent, live or perishable. A cliff does not do breaking
  news; a page whose content expires in hours cannot keep strata
  honest.
- For task-first tools and dashboards. The theme's fastest permitted
  motion (outside fracture) is 600ms and its scroll values lag by
  design; a user trying to *operate* something will feel buried.
- For playful, youthful or high-energy brands. There is no setting of
  this theme that is fun in that sense; rust and bone do not grin.
- For content that is mostly bright photography. The palette is a dark
  cliff face; images survive only inside stone frames as treated
  plates (§6.12). A fashion lookbook will suffocate here.
- On pages that must feel instant on low-end hardware. The rise, the
  pin and the parallax are all affordable (§14), but the *felt* pace
  is deliberate — if the brief says "snappy", choose another theme.

## 2. Palette

Five anchors, all quarried from the cliff itself. The page is dark by
nature — a basalt face is dark at every hour — so there is **no light
mode and no inversion**: relief is provided inside the page by the
calcite stratum (§4), a single bone-ground band permitted once per
page, never by flipping the scheme. Measured contrasts below are
computed, not estimated.

| Token | Hex | Role | Usage ratio | Pairing / contrast notes |
|---|---|---|---|---|
| `--basalt` | `#0E0D0B` | The cliff face: page ground, column faces, bedrock | ~55% | Ground for `--bone` text (10.28:1 ✓) and `--ash-light` (6.28:1 ✓) |
| `--wet` | `#2A2723` | Wet stone: raised columns, cards, frames, the seam form's field insets | ~25% | Ground for `--bone` (7.87:1 ✓) and `--bone-dim` (5.37:1 ✓); never carries `--ash` text (2.46:1 ✗) |
| `--bone` | `#C8BBA6` | Bone: primary text, active captions, drawn diagram lines | ~12% | Text on `--basalt` 10.28:1 ✓, on `--wet` 7.87:1 ✓; as text on `--rust` 3.54:1 — large only, discouraged |
| `--ash` | `#6B6156` | Ash taupe: joints, hairlines, captions at display size, inactive strata labels | ~5% | On `--basalt` 3.21:1 — **display/large text and lines only, never body text**; on `--wet` 2.46:1 — decoration only |
| `--rust` | `#8C4A2F` | Iron rust: the fissure light, glow seep, the bedrock rule, active markers | ~3% | On `--basalt` 2.90:1 — **light and line only, never text**; on `--bone` 3.54:1 — large labels only |

Derived tokens (a closed list — no others may be introduced):

| Token | Hex | Derivation / role | Contrast |
|---|---|---|---|
| `--bone-dim` | `#A79A83` | Bone weathered: secondary text, captions, table data | On `--basalt` 7.02:1 ✓; on `--wet` 5.37:1 ✓ |
| `--ash-light` | `#9C9182` | Ash lifted: small text on the cliff face only (labels, folios, apparatus) | On `--basalt` 6.28:1 ✓; on `--wet` 4.80:1 ✓ (≥13px only) |
| `--rust-bright` | `#B26A44` | Rust oxidised further: the one text-grade rust, for the active stratum name and form errors on `--basalt` | On `--basalt` 4.66:1 ✓ (≥14px); on `--wet` 3.57:1 — large only |
| `--rust-pale` | `#C08A66` | Rust at the fissure's lit edge: the progress light's hot core (§6.10), glow peak | On `--basalt` 6.54:1 ✓; used as light, not text |
| `--joint` | `#1B1916` | The crack between columns: 1px joint lines, darker than any face | n/a — line only |
| `--calcite` | `#C8BBA6` | The bone stratum's ground (= `--bone` as a ground, §4) | Carries `--basalt` text 10.28:1 ✓ and `--wet` text 7.87:1 ✓; `--rust` labels large only (3.54:1) |

**Pairing laws.** (1) Body text is `--bone` or `--bone-dim` on
`--basalt` or `--wet`; there is no third option. (2) `--ash` never sets
text below 20px and never on `--wet`. (3) `--rust` is light, line and
marker — it is never a text colour below 20px, and on `--basalt` the
text-grade substitute is always `--rust-bright`. (4) At most one
calcite stratum per page (§4); its text is `--basalt`/`--wet` only.
(5) The fissure (§6.3) and the progress light (§6.10) are the only two
places `--rust-pale` appears — the cliff has exactly two lit cracks.

**Dark-mode behaviour.** None, by documented refusal: the cliff face
does not invert at night because it was never lit by the screen's
scheme to begin with. `prefers-color-scheme: light` receives the same
page. Forced-colors mode is honoured structurally: joint lines and
column boundaries are real borders (not box-shadows), so Windows High
Contrast can re-draw the grid; the fissure and glow are opacity layers
that forced-colors may drop without losing any content (§6.3, §6.8).

## 3. Typography

Two typefaces, both load-bearing. **Fraunces** (variable, opsz axis
engaged) is the stone: heavy, tight, high-contrast letterforms that
read as cut rather than printed. **Archivo** is the apparatus: the
surveyor's hand — labels, data, captions, the text that measures the
stone rather than being it.

| Role | Font | Size / line-height | Tracking | Rules |
|---|---|---|---|---|
| Display (hero headline) | Fraunces, wght 850, opsz 144 | 76px / 0.98 (≥1200px); 54px (<768px) | −0.02em | Sentence case; carries the fracture offset until §6.2's snap; never italic, never underlined |
| H2 (stratum titles) | Fraunces, wght 800, opsz 72 | 38px / 1.08 | −0.015em | One per stratum; sits on the stratum's top joint line |
| H3 (column heads) | Fraunces, wght 700, opsz 36 | 25px / 1.16 | −0.01em | Heads a single column's content; never spans columns |
| Chiselled numerals | Fraunces, wght 800, tabular | 44–64px / 1.0 | 0 | Ages, depths, counts (§6.11); tabular figures mandatory so the count does not jitter the stone |
| Body | Archivo, wght 400 | 17px / 1.68 | 0 | Measure 56–64ch inside a column; `--bone` or `--bone-dim` only |
| Strong / lead | Archivo, wght 600 | 17px / 1.68 | 0 | Used for the first sentence of a stratum's text and for data values |
| Caption / apparatus | Archivo, wght 500, uppercase | 12.5px / 1.5 | +0.14em | Stratum labels, folios, the depth readout; `--ash-light` or `--bone-dim` |
| Data / tables | Archivo, wght 400–600, tabular-nums | 14.5px / 1.55 | 0 | Survey tables (§11); figures right-aligned, units in apparatus style |
| Form labels | Archivo, wght 600, uppercase | 12px / 1.4 | +0.12em | Chiselled above their field (§6.15); errors in `--rust-bright` sentence case |

**Type laws.** (1) Fraunces never sets body text and Archivo never
sets a headline — the stone and the surveyor do not swap jobs.
(2) No exclamation marks anywhere on the page (§12). (3) Numerals in
prose are written as figures when they are measurements ("the flow is
61 m thick") and as words when they are rhetoric ("one flow, one
cooling"). (4) The display headline is the only text permitted the
fracture offset (§6.2); no other letter on the page is ever misaligned
by even 1px — fracture is rationed to one event. (5) Uppercase is
reserved for apparatus (≤12.5px, tracked); a headline in all caps is a
shout, and cathedrals do not shout.

## 4. Layout language

**The column grid.** The page's master grid is a row of basalt columns:
vertical prisms whose caps are hexagonal. In CSS the columns are grid
tracks of three widths — **narrow 1fr, standard 2fr, organ 3fr** — on a
12-unit row at ≥1200px, separated by **10px joints** (`--joint` gaps
with a 1px inset hairline on each face, so a joint reads as a crack
with two lit edges, not a gutter). Each column's cap is a hexagon
rendered by an SVG or clip-path headpiece: a point-up hexagon whose
width equals the column's, height = width × 0.28, filled one shade
above the face (`--wet` on a `--basalt` column) so the cap catches the
light the face does not. Columns are **staggered**: within a row, each
column's top is offset downward by its depth rank × 28px (back columns
stand highest, front columns lowest — the cliff face recedes as it
approaches). A column's height is its content's height; the stagger is
in the tops, never in ragged bottoms — the row stands on a common
stratum line.

**Strata.** Below the hero cliff, the page proceeds in strata:
full-width horizontal bands, each a single geological layer with its
own ground (`--basalt`, `--wet`, or — once only — `--calcite`), its
own depth rate for parallax (§6.4), and a top joint: a 10px band of
`--joint` with the stratum's name lettered in apparatus type at the
left ("STRATUM II — THE ORGAN"). A stratum's interior uses the column
grid at reduced drama: columns without caps, joints at 8px, stagger
14px. Density rule: a stratum holds at most one idea — one gallery,
one table, one argument. Two ideas in one stratum is two strata.

**Whitespace as overburden.** The rock above a seam is called
overburden, and here whitespace does that work: strata are separated
by 96–144px of bare `--basalt` cliff with nothing in it but the joint
lines of the columns passing through — the emptiness is load-bearing,
it is what makes the next stratum feel *reached*. Within a stratum,
spacing follows an 8px rhythm with column padding of 28px (≥1200px),
20px (768–1199px), 16px (<768px). Nothing on the page is centred
except the cross-section diagram (§6.7) and the 404 block (§6.17);
the cliff is left-aligned, like a survey.

**The calcite stratum.** Once per page, one stratum may be bone-ground
(`--calcite`): a pale layer in the dark face, used for the page's most
human content — testimony, the form (§6.15), the people. It is a
rationed event: two calcite strata and the cliff reads as striped,
which is a different, cheaper theme.

**The bedrock.** The footer (§6.9) is a full-width `--basalt` block,
taller than any stratum (min 320px), with no caps, no stagger, no
joints — one unbroken block, its top edge ruled by a single rust line.
It is the only element whose top edge is perfectly level with the
viewport's rhythm: everything above it settles; it does not.

## 5. Full motion system

Five named easings, all geological. Any other easing on the page is a
gate failure (§10).

| Token | Curve | Character | Used by |
|---|---|---|---|
| `--ease-uplift` | `cubic-bezier(0.16, 1, 0.3, 1)` (easeOutExpo) | A mass rising: fast commitment, very long settle | Column rise (§6.1), image settle (§6.12) |
| `--ease-settle` | `cubic-bezier(0.25, 0.6, 0.2, 1)` | Stone coming to rest; counters; draws | Hex draw (§6.7), counters (§6.11), accordions (§6.18) |
| `--ease-fracture` | `cubic-bezier(0.86, 0, 0.07, 1)` | The crack: near-instant, hard stop, no overshoot | Headline snap (§6.2) — **the only fast motion in the theme** |
| `--ease-seep` | `cubic-bezier(0.33, 0, 0.2, 1)` | Liquid in a crack: slow in, slower out | Fissure-glow (§6.8), button release (§11) |
| `--ease-drift` | `cubic-bezier(0.45, 0, 0.55, 1)` | Ash on still air | Ash fall sway (§6.6), skeleton veil (§6.16) |

**The shared loop.** One `requestAnimationFrame` loop drives every
scrubbed value — fissure width/length (§6.3), strata offsets (§6.4),
organ-pipe brightening (§6.5), progress light (§6.10), image settle
(§6.12), magnetic button pull (§11) — with a single lerp factor of
**0.08**, the library's heaviest: at 60fps a rendered value closes
8% of its remaining distance per frame, so a hard flick of the scroll
wheel takes ~700ms to fully arrive in the stone. Native scroll is
never hijacked; the *document* scrolls at the visitor's speed and the
*stone's values* lag behind it, which is where the weight is felt.
The loop sleeps when no tracked value is more than 0.1px from target
and when the tab is hidden.

**Every motion term, translated.** Scroll-triggered reveals: the rise
(§6.1) and the hex draw (§6.7) — entrances are geological events, used
twice per page at most. Scroll-driven/scrubbed: fissure, strata shear,
progress light, image settle. Pinned sections: exactly one — the organ
pipes (§6.5), 150vh. Parallax: three strata rates (§6.4), capped
±48px. Masked reveals: the headline's vertical clip split along a
column joint (§6.2). Blur-to-sharp: **refused** — stone does not
defocus; the refusal is the theme's, stated here so no builder imports
it from another theme. Animated counters: chiselled numerals (§6.11),
2400ms, never faster. Progress indicator: the fissure of light
(§6.10) — a progress *bar* is refused (§11). Marquee: **refused** —
nothing on a cliff crawls sideways. Kinetic typography: refused,
except the fracture snap. Ambient loops: ash fall (§6.6) only, capped
and pausable. Micro-interactions: glow seep (§6.8), magnetic pull with
geological weight and the thunk press (§11) — pull capped at 6px,
lerp 0.06, the heaviest micro-interaction in the library. Page
transitions: the strata wipe (§6.16), three bands at the strata rates,
1400ms total. Reduced motion: every element carries its variant; the
theme under reduced motion is a still cliff with all content present —
which, for this theme, is barely a compromise.

## 6. Signature elements

### 6.1 Column rise

- **What & why.** The hero's entrance and the theme's thesis performed
  once, at the door: the cliff assembles itself. The hero's columns —
  the actual containers of the headline, the standfirst, the image
  plate and the call to action — rise from below the viewport's edge
  in depth order, back columns first, front columns last, over a full
  two seconds. It belongs here because a cathedral of stone cannot
  fade in; it can only be *raised*. The visitor watches the layout
  itself being built by the force the whole page is about, and every
  later stratum is read in the knowledge that the grid is geology.
- **Structure.** The hero is a `.cliff` section containing 3–5
  `.column` elements on the master grid (§4). Each column carries a
  `data-depth` rank (0 = back … n = front), a hexagonal cap headpiece,
  and its content in normal flow. The pre-rise state exists **only**
  as a JS-applied class (`.is-unrisen`) set before first paint by an
  inline script when JS and motion are both available: columns are
  translated downward by their depth offset (back 12vh, mid 16vh,
  front 20vh) and the section clips overflow. Without that class —
  no-JS, reduced motion, watchdog — the columns stand at rest.
- **Motion spec.** Trigger: page load, after fonts (watchdog below).
  Each column: `translateY(depth offset) → 0` over **2000ms
  `--ease-uplift`**, staggered **120ms by depth rank** (back first).
  Total ceremony: 2000 + 120 × (ranks − 1) ≈ 2.4s for four ranks. The
  rise is transform-only; the caps, joints and content ride their
  column. Nothing else on the page moves during the rise except the
  ash (§6.6), which is already falling — the cliff rises through its
  own weather.
- **Choreography timeline (v2).** t+0: page paints with columns at
  rest in the DOM (pre-state JS-applied only) → t+150ms: JS arms
  `.is-unrisen` (columns drop to offsets, no visible flash because the
  arm happens before the rise class in the same frame) → t+300ms:
  back column begins rising → t+420ms: second rank → +120ms per rank
  → t+300+2000ms: back column at rest → t≈+2.7s: front column settles;
  §6.2's fracture snap fires 150ms later → the hero is a cliff.
- **State matrix (v2).** *Rest (pre-arm / no-JS):* columns standing,
  content fully readable — the designed default. *Rising:* 2s per
  column, non-interactive but content legible throughout (columns are
  translated, never faded — text is readable mid-rise, merely lower).
  *Settled (terminal):* the cliff at rest; identical on desktop and
  touch. *Hover/focus:* no effect; the hero's controls (CTA) are live
  from first paint, rising or not. *Scrolled-past:* columns scroll
  away as ordinary content; the rise never replays. *Disabled:* with
  JS off the `.is-unrisen` class is never applied — there is no
  disabled state distinct from rest.
- **Content merge.** The rising objects are the content containers
  themselves — headline, image and CTA arrive standing on their own
  stone. Remove the rise and the hero is a finished cliff, poorer in
  ceremony and identical in content.
- **Failure fallback.** The standing 1200ms law of the original entry:
  a watchdog forces `.is-risen` (all transforms cleared) at **1200ms**
  after load if the rise has not begun (fonts stalled, loop failed),
  and any column still translated at 3600ms is snapped to rest by the
  same watchdog. Because the pre-state is JS-applied, a JS failure
  before arming leaves the finished cliff. `transitionend` is never
  trusted.
- **Reduced-motion variant.** No rise. Columns stand at rest from
  first paint; §6.2's snap is likewise pre-closed. The hero loses its
  ceremony and keeps its cliff.
- **Breakpoints (v2).** ≥1200px: full spec, 3–5 columns, offsets
  12/16/20vh by rank. 768–1199px: 2–3 columns, offsets 10/14vh,
  stagger 100ms, duration 1800ms. <768px: columns stack to a single
  file (§4); the rise becomes a single-column lift of 8vh over
  1600ms — a phone cliff rises as one face, not as ranks.
- **Edge cases & failure modes (v2).** *Return visit mid-scroll
  (browser scroll restoration):* if the restored scroll position is
  below the hero, the rise is skipped entirely — a cliff the visitor
  has already passed is not re-raised behind them. *Very tall hero
  content:* column offsets are vh-based, so a column taller than the
  viewport rises the same distance; its foot may start on-screen,
  which is correct — the face is emerging, not teleporting. *Slow
  network / fonts late:* the rise waits for `fonts.ready` or the
  1200ms watchdog, whichever first; it never rises in a fallback font
  and then re-rises. *Tab hidden during rise:* CSS transitions pause
  with the tab; on return the watchdog's 3600ms ceiling has passed
  and columns are at rest — the visitor never returns to a half-risen
  cliff.
- **Accessibility spec (v2).** The rise is a transform on containers;
  DOM and reading order are the cliff's reading order at all times.
  Focus is never moved. A keyboard visitor can tab into the hero CTA
  during the rise — focus outline rides the column, which is moving
  slowly enough (≤20vh over 2s) to remain trackable. Contrast is
  unaffected: columns are opaque throughout (no fade), so text meets
  §2 ratios at every frame of the rise.
- **Performance budget & mobile variant.** Transform-only animation on
  ≤5 elements; no layout, no paint beyond compositing. `will-change`
  is applied to rising columns only and removed at settle. Mobile:
  the single-lift variant above; cost is one transform.
- **Tokens consumed (v2).** `--basalt`, `--wet`, `--joint`,
  `--ease-uplift`, `--rise-dur` (2000ms), `--rise-stagger` (120ms),
  `--rise-back` (12vh), `--rise-front` (20vh), `--watchdog-rise`
  (1200ms).

### 6.2 Fractured headline snap

- **What & why.** The theme's signature in a single gesture, and the
  one fast thing stone is allowed to do. The display headline's
  letters stand with a barely visible **1px vertical fracture
  offset** — alternate letters displaced ±1px, as if the type itself
  were columnar-jointed stone, its face cracked along the joints.
  150ms after the last hero column settles (§6.1), the fractures
  **snap shut in 90ms**: the letters align, and the headline becomes
  one readable stone face. It belongs here because it is the theme's
  anti-slop detail promoted to an event — the crack closing is the
  moment the cliff becomes a cathedral, and it teaches the visitor
  the law (§1) without a word of explanation: everything here is
  slow, except fracture.
- **Structure.** The headline is real text in an `<h1>`. JS wraps each
  letter in a `<span class="glyph">` (the full text stays in the
  accessibility tree via `aria-label` on the h1 and `aria-hidden` on
  the wrapper spans). Each glyph carries `transform: translateY(±1px)`
  alternating by index, applied only under the JS-armed class
  `.is-fractured`. Before the snap, the h1 is also revealed by the
  original entry's masked entrance: a vertical clip that splits along
  the column joint beside the headline's column, the two halves of
  the mask parting over 900ms `--ease-uplift` as the column rises —
  the headline is uncovered by its own joint opening.
- **Motion spec.** Trigger: 150ms after §6.1's final column settles
  (or at load +600ms if the rise was skipped). The snap: every
  glyph's translateY → 0 over **90ms `--ease-fracture`**, all letters
  simultaneously — a crack closes along its whole length at once, not
  in a wave. It fires **once** per page load. It never re-fractures
  on scroll-back, hover, or resize.
- **Choreography timeline (v2).** t+0 (§6.1 settles): headline stands
  fractured, readable but jointed — the offset is 1px, so the text is
  legible throughout; fracture is texture, not a lock → t+150ms: snap
  begins → t+240ms: face aligned, `.is-fractured` removed → terminal.
  The visitor who blinked has missed the event and lost nothing but
  the theme's signature — which is why the *static* fractured state
  must never persist (see fallback).
- **State matrix (v2).** *Fractured (armed, pre-snap):* glyphs at
  ±1px, ≤240ms duration in practice. *Snapping:* 90ms. *Aligned
  (terminal):* ordinary headline. *Hover/focus:* no state — letters
  do not perform. *Scrolled-past:* aligned. *Disabled (no-JS):* the
  headline is never wrapped or offset — plain aligned text, which is
  the correct failure: an unwrapped headline, not a stuck fracture.
  Touch is identical to desktop in all states.
- **Content merge.** The fracture is in the headline's own letters —
  the type is the stone. Remove the effect and the headline remains,
  word for word; keep it and the page's most important sentence is
  made of the page's material.
- **Failure fallback.** Two watchdogs: if the snap has not fired by
  load +4000ms, JS removes `.is-fractured` instantly (aligned, no
  animation — a late snap would be a jump scare). If letter-wrapping
  itself fails (empty headline, unsupported), the h1 is untouched.
  The permanent-fracture state — headline left offset forever — is
  the one unforgivable failure of this element and is what the
  watchdog exists to prevent.
- **Reduced-motion variant.** The headline is never fractured. It
  stands aligned from first paint; the clip mask is also removed
  (the headline is simply present). The theme's law is honoured in
  reverse: no fracture, no snap.
- **Breakpoints (v2).** ≥1200px: full spec, 1px offset at 76px type.
  768–1199px: offset 1px at 54–64px type. <768px: offset remains 1px
  (at 44–54px type it is proportionally larger, still sub-legibility-
  threatening); the clip-split entrance is dropped — the headline
  arrives with its column (§6.1's single lift).
- **Edge cases & failure modes (v2).** *Multi-line headline:* the
  offset alternates continuously across lines (index-based, not
  per-line), and the snap closes all lines at once. *Headline with
  mixed scripts / ligatures:* wrapping is per grapheme cluster, never
  splitting a combining sequence; if the grapheme segmentation API
  is unavailable, wrap by code point and skip combining marks.
  *Very long headline (>90 glyphs):* the wrap cost is one pass; the
  snap is a single class change — cost does not scale visibly.
  *Font swap after wrap:* glyph spans inherit the family; a late
  Fraunces load re-flows the spans but the ±1px offsets are
  font-independent, so the fracture survives the swap and the snap
  still fires on schedule.
- **Accessibility spec (v2).** The h1 carries `aria-label` with the
  exact headline text; glyph spans are `aria-hidden`. Screen readers
  meet one headline, once, in order. The 1px offset never affects the
  accessible rendering. Focus: the h1 is not focusable (unless it is
  the page's skip target, tabindex −1, in which case focus lands on
  the whole headline, offsets irrelevant). Contrast at every state:
  bone on basalt, 10.28:1 ✓.
- **Performance budget & mobile variant.** One-time DOM wrap (≤~90
  spans), one 90ms transform transition on those spans, then static.
  Negligible. Mobile: as breakpoints; the wrap is skipped entirely
  below 360px wide if the headline exceeds 120 glyphs (cost/benefit).
- **Tokens consumed (v2).** `--bone`, `--basalt`, `--ease-fracture`,
  `--ease-uplift`, `--snap-dur` (90ms), `--fracture-offset` (1px),
  `--snap-delay` (150ms).

### 6.3 Scroll fissure

- **What & why.** Down the face of the hero's tallest column runs a
  hairline fissure. As the visitor scrolls through the first chapter,
  the fissure **widens from 1px to 5px and lengthens** down the
  column, scrubbed to their scroll: the cliff is splitting as they
  descend, at exactly the speed of their own reading. It belongs here
  because it makes the first chapter's scroll *consequential* — the
  visitor is not moving a camera past a picture of stone; their
  descent is opening the stone. The fissure also carries the hero
  column's own story: it runs through the column the visitor is
  reading beside, and at full width a hair of `--rust-pale` light
  shows at its deepest point (§2's first lit crack).
- **Structure.** An SVG path inside the hero column, absolutely
  positioned over the column face, `pointer-events: none`,
  `aria-hidden`. The path is a hand-authored jagged polyline (7–11
  segments, angles between 8° and 22° off vertical — a crack is not a
  crack if it is straight) drawn twice: a `--joint`-dark under-path
  whose stroke-width is the scrubbed width (1→5px), and, above 3.5px
  width, a 1px `--rust-pale` core line at 0.55 opacity. Length is
  scrubbed by `stroke-dashoffset` against the path's measured length.
  The column's content is laid out to keep a 24px clear channel down
  the fissure's line — the crack never crosses text (see edge cases).
- **Motion spec.** Trigger: continuous scroll through the hero + first
  stratum (≈150vh of travel). Progress `p` (0→1 across that range)
  maps: length 0→100% of the path, width 1px→5px, both driven by the
  shared loop (lerp 0.08). The rust core fades in across p 0.7→0.9.
  Fully reversible: scrolling back up narrows and shortens the
  fissure symmetrically — a crack the visitor can un-open by
  retreating, because the scrub is a pure function of position.
- **Choreography timeline (v2).** Spatial, not clocked: p=0 — hairline
  12% long, 1px, at the column cap → p=0.25 — 38% long, 1.8px →
  p=0.5 — 63% long, 2.9px, joints of the crack visibly stepping →
  p=0.75 — 84% long, 4.1px → p=0.9 — rust core lit → p=1 — full
  length, 5px, the fissure reaches the stratum joint below and stops:
  cracks end at bedding planes.
- **State matrix (v2).** *Rest (top):* hairline at 12%/1px — present
  from first paint as a static crack, so the no-JS cliff is already
  fissured (see fallback). *Scrubbing:* width/length follow the loop.
  *Fully open (p=1):* terminal for that scroll position; holds.
  *Hover/focus:* none — the fissure is not a control. *Scrolled-past:*
  holds at full width behind the visitor; it is found open on
  scroll-back until p decreases. *Disabled (no-JS):* the static
  hairline at 12% — a crack, unopened. Touch: identical scrub.
- **Content merge.** The fissure runs through the hero column's own
  face, in a channel its layout reserved; the rust at its depth is
  the same rust the progress light (§6.10) is made of — the cliff's
  interior, glimpsed twice. Remove the scrub and a static crack
  remains in the stone; nothing was ever pasted on.
- **Failure fallback.** If the loop stalls, the fissure freezes at its
  current width — a crack mid-opening is still a crack, and no
  content is hidden behind it at any width (the 24px channel law).
  If SVG is unavailable, a CSS fallback draws the hairline as a 1px
  `--joint` border segment on the column; the scrub is lost, the
  crack remains.
- **Reduced-motion variant.** The fissure is static at 40% length,
  2px wide, no rust core — a crack at rest, present from first paint.
  Scroll changes nothing.
- **Breakpoints (v2).** ≥1200px: full spec (1→5px, full column
  length). 768–1199px: width 1→4px, scrub range 130vh. <768px: the
  hero is a single column (§6.1); the fissure runs at its left edge
  instead of mid-face (a phone-width face has no spare channel),
  width 1→3px, scrub range 110vh.
- **Edge cases & failure modes (v2).** *Content reflow (image loads
  late, column grows):* the path is positioned in % of the column and
  its length re-measured on resize; the scrub re-maps — the crack
  never detaches from its column. *Jump scroll to mid-page:* the
  loop's lerp settles p within ~700ms; the fissure is never seen in a
  state inconsistent with the final scroll position for longer than
  that. *Forced-colors mode:* the SVG may be recoloured or dropped
  by the UA — acceptable, the crack is atmosphere; the column's text
  is untouched. *Print:* the fissure prints at its static 12%/1px
  state (the pre-JS paint), which is the honest paper version.
- **Accessibility spec (v2).** Purely visual, `aria-hidden`, no
  information rides on the fissure's width — the same progress is
  available as text in the navigation's stratum readout (§6.13).
  The 24px clear channel guarantees the widening crack never reduces
  text contrast or touches a glyph at any p.
- **Performance budget & mobile variant.** One stroke-width and one
  dashoffset write per frame while scrubbing, inside the shared loop.
  Mobile: the edge variant above; path segments reduced to 6.
- **Tokens consumed (v2).** `--joint`, `--rust-pale`, `--basalt`,
  `--loop-lerp` (0.08), `--fissure-w0` (1px), `--fissure-w1` (5px),
  `--fissure-range` (150vh).

### 6.4 Strata parallax

- **What & why.** The page's strata (§4) do not scroll as one sheet.
  They shear: near strata move at **1.08×**, the reading stratum at
  **1.0×**, far strata at **0.92×** — so as the visitor descends, the
  layers of the cliff visibly slide past one another along their
  joints, exactly as strata in a road cutting separate when you walk
  its length. It belongs here because depth in this theme is not a
  background photograph's blur; it is the content layers themselves
  moving at their own rates. The shear is also the theme's depth
  cue for the whole page: by the second stratum, the visitor *feels*
  the page is a face they are descending, not a document they are
  scrolling.
- **Structure.** Each `.stratum` carries `data-depth="far|mid|near"`.
  The parallax applies to an inner `.stratum-body` wrapper (never to
  the stratum's joint band or its heading, which stay locked to the
  document so anchors and reading order stay true). Each body has
  **12% vertical bleed**: it is rendered 12% taller than its slot
  (extra cliff texture and joint lines, no content in the bleed) so
  the ±48px travel can never expose an edge. Offsets are written by
  the shared loop as `translateY`, computed from the stratum's
  viewport position × its rate deviation.
- **Motion spec.** Trigger: continuous scroll. Offset = clamp(
  (stratum centre − viewport centre) × (rate − 1) × 0.14, −48px,
  +48px ), lerped at 0.08 in the shared loop. Rates: far 0.92, mid
  1.0 (offset always 0 — the reading layer is the reference), near
  1.08. A page has at most one near stratum (the one carrying the
  organ pipes, §6.5) and far strata are the minority; a page of all
  near strata is a landslide, not a cliff.
- **Choreography timeline (v2).** Spatial: as a far stratum enters
  from below, its body sits +48px low (lagging) and rises through 0
  at viewport centre to −48px as it leaves — the layer is overtaken
  by the reader. A near stratum does the mirror journey, sliding
  down past the reader. The shear between two adjacent strata at a
  joint peaks at ~30px of relative displacement mid-transit — enough
  to see, never enough to misalign a joint line by more than the
  joint's own 10px band can absorb visually (the joint band itself
  does not move; the bodies shear *behind* it).
- **State matrix (v2).** *Rest (any scroll position, loop settled):*
  offsets at their mapped values; the page is a valid static cliff
  at every position. *Scrolling:* offsets chase their targets at
  lerp 0.08. *Hover/focus:* unaffected; interactive content inside a
  body moves with it — a button under the pointer moves at most
  48px over a full viewport transit, far slower than any aiming
  correction. *Scrolled-past:* offsets hold at their exit values
  until the stratum leaves the tracked band (±1 viewport), then the
  loop stops writing it. *Disabled (no-JS):* all offsets 0 — the
  strata stack flush, fully readable. Touch: identical, lerp 0.08.
- **Content merge.** The moving layers are the content strata
  themselves — their text, tables and images shear with their band.
  There is no decorative background layer anywhere in this theme;
  §6.4 is the proof: remove the content and there is nothing left to
  parallax.
- **Failure fallback.** Offsets default to 0 in markup; JS writes
  them. A loop failure leaves strata flush at 0 — the page loses its
  depth and keeps everything else. The bleed guarantees that even a
  stuck mid-travel offset (±48px) can never expose the page ground
  at a stratum's edge.
- **Reduced-motion variant.** No parallax. All rates become 1.0,
  offsets 0, permanently. The strata still differ by ground and joint
  — depth is then told by the §4 stagger alone.
- **Breakpoints (v2).** ≥1200px: full spec (±48px, three rates).
  768–1199px: travel capped at ±32px, rates 0.95/1.0/1.05.
  <768px: travel ±18px, rates 0.97/1.0/1.03 — a phone's strata shear
  subtly; more would make reading swim. Below 360px: parallax off
  (offsets 0), the cliff is still.
- **Edge cases & failure modes (v2).** *Anchor jump into a stratum:*
  offsets snap-settle via the lerp within ~700ms of arrival; the
  anchored heading is in the un-moved joint band, so the target
  never drifts from where the browser placed it. *Find-in-page:*
  the browser scrolls to a match inside a moving body; the body's
  residual offset (≤48px) cannot push the match off-screen because
  the loop's target at that scroll position is computed from the
  same position the browser used. *Very long strata (>300vh):*
  offset is a function of centre-distance, clamped — a long stratum
  sits at its clamp for most of its length, which reads as the layer
  holding while the reader crosses it: correct. *Resize / rotate:*
  bleed and clamps recompute; no stratum can be caught mid-frame
  with an exposed edge because bleed (12%) exceeds max travel at
  every breakpoint.
- **Accessibility spec (v2).** Parallax moves containers, never
  reading order. Focus targets inside a body: if a focused element
  is inside a stratum that is still settling (post-jump), the
  browser's scroll-into-view and the loop use the same scroll
  position, so focus is never chased off-screen. Visitors with
  vestibular sensitivity are served by the reduced-motion variant
  and by the small travel caps — 48px over a full viewport transit
  is the library's gentlest parallax, by design.
- **Performance budget & mobile variant.** One transform write per
  visible stratum per frame (≤4 strata tracked), inside the shared
  loop; bodies are composited layers only while on-screen.
  Mobile: the capped variant above.
- **Tokens consumed (v2).** `--loop-lerp` (0.08), `--rate-far`
  (0.92), `--rate-mid` (1.0), `--rate-near` (1.08),
  `--parallax-max` (48px), `--stratum-bleed` (12%).

### 6.5 Organ-pipe gallery pin

- **What & why.** The theme's one pinned scene, rationed to exactly
  one per page. A row of tall pillar images — the organ pipes — pins
  for **150vh** while their captions file past one by one in the
  reading column beside them; as each caption is read, its pillar
  **brightens from wet stone to bone**, as if the light in the
  cathedral had moved to the pipe being sounded. It belongs here
  because a columnar organ is the theme's namesake made visible, and
  because the pin performs the theme's core exchange: the visitor
  gives the page time, and the page gives them sequence — five
  pillars, five captions, one at a time, in order, at reading pace.
- **Structure.** A `.organ` section: a sticky stage (100vh) holding a
  row of 4–6 `.pipe` figures (images inside stone frames, §6.12,
  heights staggered 62–92vh by their real proportions in the subject)
  and a caption rail. The section's scroll length is 150vh of travel
  beyond the stage. Progress `q` (0→1 across the pin) is divided into
  equal caption beats; the active caption is set in `--bone` at full
  size in the rail, inactive captions in `--bone-dim` at 92% — all
  captions are in the DOM, in order, from first paint. Brightening is
  a `--bone` overlay on each pipe at scrubbed opacity 0→0.16 plus a
  1px `--ash-light` edge light on the pipe's left joint.
- **Motion spec.** Trigger: scroll through the pinned range. `q` is
  driven by the shared loop (lerp 0.08). Caption beats: caption *i*
  is active while `q ∈ [i/n, (i+1)/n)`; its pipe's brightening ramps
  across the middle 60% of its beat and holds. Caption change is a
  crossfade of colour/weight only (300ms `--ease-settle`) — captions
  never slide, scale or re-flow; a filing system, not a carousel.
  At q=1 the stage unpins and the whole organ scrolls away as one
  stratum.
- **Choreography timeline (v2).** q=0: organ pinned, pipe 1 at 40%
  brightening, caption 1 active → each beat boundary: outgoing
  caption dims over 300ms as the next pipe's light ramps → mid-beat:
  one pipe lit, its caption read → q=1: last pipe lit, all captions
  have filed; the stage releases and the organ joins the strata
  shear (§6.4) as it leaves.
- **State matrix (v2).** *Approaching:* organ in flow, pipe 1
  pre-lit at 40% (its resting state in markup). *Pinned/reading:*
  beats advance with scroll; scrolling back reverses the filing
  exactly — caption and light are pure functions of q. *Released:*
  organ scrolls as a normal stratum. *Hover (on a pipe):* that pipe
  brightens +0.06 overlay — a touch on the stone — without changing
  the active caption; focus (a pipe figure is not focusable; its
  caption link, if any, is) behaves as hover on keyboard focus.
  *Disabled (no-JS):* no pin; the organ is a static row with all
  captions printed beneath their pipes at full `--bone` — the
  gallery as a plate page. Touch: the pin becomes a horizontal
  sequence (§breakpoints).
- **Content merge.** The pipes are the gallery's images and the
  captions are the gallery's text; the pin exists only to sequence
  *them*. Brightening a pipe lights the photograph the visitor is
  reading about — attention made visible on the content itself.
- **Failure fallback.** The pin is `position: sticky` — if sticky
  fails or JS is absent, the section is a long stratum with pipes
  and captions in flow; nothing is hidden at any q because every
  caption is rendered. If images fail, pipes stand as stone frames
  with their captions (alt text in place) — the organ reads as a
  diagram of itself.
- **Reduced-motion variant.** No pin. Pipes in a row, captions
  beneath each at full contrast, no brightening scrub (all pipes at
  the 40% resting light). Sequence is preserved by layout, not by
  scroll.
- **Breakpoints (v2).** ≥1200px: full spec (side-by-side pipes +
  caption rail, 150vh pin). 768–1199px: pipes above, caption rail
  below the stage, pin 130vh, 4 pipes max. <768px: **no pin** —
  pipes stack vertically, each followed by its caption at full
  contrast (a phone organ is played one pipe at a time by ordinary
  scrolling); brightening is dropped, edge light kept.
- **Edge cases & failure modes (v2).** *More captions than pipes or
  vice versa:* a build error — the gate (§10) requires pipes =
  captions, 4–6 each. *Fast scroll through the pin:* q is positional;
  the loop settles within ~700ms and intermediate captions are
  simply passed — filing is not a queue, nothing backlogs.
  *Browser find landing inside a caption mid-pin:* the caption is in
  the rail at a fixed stage position, so the match stays in view for
  the whole beat range that contains it. *Images of very different
  aspect:* pipe heights are set from the subjects' real proportions
  (stated in the caption data), capped 62–92vh; a pipe that would
  exceed the cap is cropped by its stone frame (§6.12), never
  stretched.
- **Accessibility spec (v2).** Reading order: pipe 1 image (alt),
  caption 1, pipe 2, caption 2… in the DOM — the sticky stage is a
  visual rearrangement of a correctly ordered list. The brightening
  is decorative; active-caption state is conveyed by the rail's
  `aria-current` on the active caption for AT users who navigate by
  it. All captions meet §2 contrast in both states (`--bone-dim` on
  `--basalt` 7.02:1 ✓ even when "inactive" — dimming here is
  relative, never below AA).
- **Performance budget & mobile variant.** One sticky stage, ≤6
  overlay opacity writes per frame in the loop; pipe images are the
  page's heaviest assets and are budgeted in §14 (≤90KB each,
  treated plates). Mobile: the stacked variant — zero pin cost.
- **Tokens consumed (v2).** `--wet`, `--bone`, `--bone-dim`,
  `--ash-light`, `--ease-settle`, `--loop-lerp` (0.08), `--pin-range`
  (150vh), `--pipe-glow` (0.16).

### 6.6 Ash fall

- **What & why.** The theme's only ambient loop: fine ash motes drift
  downward over the cliff, endlessly, at 8–16px per second — the
  volcano is not dead, merely patient, and its weather settles over
  everything the visitor reads. It belongs here because it is the one
  motion that makes the page feel *inhabited by its subject* between
  the visitor's own actions: the fissure and the strata answer the
  scroll, but the ash answers nothing — it was falling before the
  visitor arrived. Density is depth's cue: ash is densest over the
  hero and thins as the page descends, the way fall-out thins with
  distance from the vent.
- **Structure.** A single `<canvas class="ashfall">` fixed over the
  page (`pointer-events: none`, `aria-hidden`, z-index above strata,
  below the navigation bar), sized to the viewport, devicePixelRatio
  capped at 1.5. Motes: **≤40 on desktop, ≤16 on mobile**, each 1.5–
  3px, `--ash`/`--bone-dim` at 0.25–0.5 opacity, velocity 8–16px/s
  downward with a sinusoidal sway of ±6px over a 6–11s period
  (`--ease-drift` character). Density field: spawn probability is
  weighted to the top of the page — motes recycle to the top with a
  per-mote lifespan, and the *rendered* density is scaled by a global
  factor that decreases with total scroll progress (1.0 at the hero →
  0.35 at the footer), implemented by parking a fraction of motes
  off-canvas.
- **Motion spec.** Trigger: time (ambient), from first paint +800ms
  (ash does not fall during the rise — the cliff assembles first).
  Continuous; pauses when the tab is hidden (`visibilitychange`),
  when the canvas is the only thing on screen during a §6.16
  transition (it is covered), and under reduced motion (never
  starts). Frame cost: one canvas draw of ≤40 rects — no loop of its
  own; it rides the shared rAF and skips frames when the loop sleeps
  only if no mote is mid-viewport… in practice the ash keeps the loop
  at a low idle cadence of 30fps (throttled from 60) to halve its
  battery cost.
- **Choreography timeline (v2).** t+800ms: first motes fade in at
  their spawn points (opacity ramp 600ms — ash thickens, it does not
  switch on) → steady state: continuous fall, sway, recycle →
  scroll: density factor follows total progress → tab hidden: frozen
  mid-air, resumes on return without a jump (timestamps, not frame
  counts, drive positions).
- **State matrix (v2).** *Falling:* as specced. *Paused (tab
  hidden):* frozen, invisible cost zero. *Thinned (deep scroll):*
  35% density. *Hover/focus:* no interaction, ever. *Disabled:*
  canvas absent (no-JS) or empty (reduced motion) — the page loses
  weather and nothing else. Touch: identical, 16 motes.
- **Content merge.** The ash falls *over the content columns
  themselves* — over the headline, the strata, the organ — because
  that is where ash falls: on the world, not in a decorative header
  strip. Its opacity ceiling (0.5, ≤3px) is set so it can never
  reduce any text's contrast below its §2 ratio at any frame (a 3px
  mote at 0.5 over a glyph is a speck, not a veil).
- **Failure fallback.** Canvas unsupported or context creation fails:
  no ash, no error, no substitute — the theme's fallback for weather
  is a clear day. The canvas is created by JS only; its absence is
  the no-JS state.
- **Reduced-motion variant.** No ash. The canvas is never created.
  This element has the strictest reduced-motion ruling in the theme
  because it is the only purely ambient one.
- **Breakpoints (v2).** ≥1200px: 40 motes. 768–1199px: 28 motes,
  DPR cap 1.25. <768px: 16 motes, sway ±4px, velocity 6–12px/s,
  density floor 0.5 (a small screen needs fewer, slightly more
  visible motes to read as weather).
- **Edge cases & failure modes (v2).** *Long pages:* the density
  factor is a function of total progress, so a 10-stratum page thins
  gradually; a short page may never thin below 0.8 — correct, a short
  visit stays near the vent. *Performance pressure:* if the shared
  loop measures sustained <45fps, ash is the first cut (§14): mote
  count halves, then the canvas is removed. *Print:* canvas does not
  print. *Motes over the calcite stratum:* ash is drawn in `--ash`
  tones that read on bone ground as grey specks — visible, correct,
  and still under the contrast ceiling because calcite text is
  `--basalt` at 10.28:1 before the speck.
- **Accessibility spec (v2).** `aria-hidden`, no information, no
  focus, no announcement. Fully disabled under reduced motion.
  Photosensitivity: motes are small, slow (≤16px/s), low-contrast —
  far below any flash or motion-sickness threshold; the sway period
  (≥6s) is slower than the vestibular concern band.
- **Performance budget & mobile variant.** ≤40 rects/frame at 30fps
  idle cadence; canvas memory negligible; first on the §14 cut list.
  Mobile: 16 motes as specced.
- **Tokens consumed (v2).** `--ash`, `--bone-dim`, `--ease-drift`,
  `--ash-count` (40), `--ash-speed` (8–16px/s), `--ash-density-floor`
  (0.35).

### 6.7 Hexagon cross-section draw

- **What & why.** In the geology stratum, an SVG cross-section of the
  cliff — the column tops seen from above, a field of fitted
  hexagons with the section line marked — **draws itself** when it
  enters: each hexagon's outline strokes in over 1.4s, in the order
  the columns cooled, centre outward. It belongs here because the
  diagram explains the very grid the visitor has been reading inside
  since the hero: the page pauses, mid-descent, to show its own
  plan. A cross-section that simply appeared would be an illustration;
  one that draws is the survey being made in front of the reader.
- **Structure.** An inline `<svg class="section-plan">`, viewBox
  square, containing 19–37 hexagon paths (a hex field 5–7 across,
  irregular edge — a real outcrop plan is not a rectangle), each a
  closed path in `--ash-light` stroke 1.5px on `--basalt`, with 3–5
  hexagons filled `--wet` to mark the columns the page's own grid
  uses, and a `--rust` section line (the page's second and last use
  of rust as line, §2) cutting the field diagonally, labelled in
  apparatus type. Each hexagon's path length is normalised with
  `pathLength="100"`; the draw is `stroke-dashoffset` 100→0. All
  hexagons are fully drawn in markup; JS arms the undrawn state only
  for hexagons in a section that is below the fold at load.
- **Motion spec.** Trigger: the diagram's stratum crossing 55%
  viewport. Per hexagon: dashoffset 100→0 over **1400ms
  `--ease-settle`**, staggered **60ms per hexagon in cooling order**
  (centre hexagon first, then its ring, outward — the order is
  authored as `data-cool` ranks, not computed from geometry, because
  cooling order is a fact about the subject). Total ceremony: 1400 +
  60 × (n−1) ≈ 3.4s for 31 hexagons — the slowest draw in the theme,
  deliberately. The section line draws last, 900ms, after the field
  it cuts exists. Fires once; scroll-back does not redraw.
- **Choreography timeline (v2).** t+0 (55% crossing): centre hexagon
  begins → +60ms × rank: each ring starts → t+1400ms: centre
  complete → rolling completion outward → t≈+3.2s: field complete →
  +200ms: section line draws (900ms) → t≈+4.3s: labels fade in
  (opacity, 400ms `--ease-settle`) → terminal: a finished plan.
- **State matrix (v2).** *Undrawn (armed, below fold):* only under
  JS; the SVG space is reserved (aspect-ratio in markup) so nothing
  shifts. *Drawing:* as specced. *Drawn (terminal):* the plan at
  rest. *Hover (on a filled hexagon):* its fill lifts `--wet` →
  `#38322B` over 300ms — the plan acknowledges its columns; on touch,
  tap does the same until another tap. *Focus:* the SVG is a figure
  with a `<figcaption>`; it is not itself focusable. *Scrolled-past:*
  drawn. *Disabled (no-JS):* fully drawn from first paint.
- **Content merge.** The diagram is the page's own grid, drawn: the
  filled hexagons are the columns carrying the content above and
  below this stratum. It is the one place the theme explains itself,
  and it explains with the subject's own evidence.
- **Failure fallback.** A watchdog at stratum-entry +5000ms forces
  all dashoffsets to 0 (finished plan) if the stagger has stalled —
  the plan may never be left half-surveyed. If `pathLength` is
  unsupported (legacy), hexagons appear whole in cooling order at
  the same stagger (opacity-free, just present) — order survives
  even when the stroke cannot.
- **Reduced-motion variant.** The plan is present, fully drawn, from
  first paint. No draw, no stagger. The section line and labels are
  simply there.
- **Breakpoints (v2).** ≥1200px: 31–37 hexagons, diagram at 640px
  wide in its own centred column (the page's one centred element,
  §4). 768–1199px: 19–25 hexagons, 480px. <768px: 12–19 hexagons
  (outer ring dropped — the plan is abridged, not shrunk to
  illegibility), stagger 45ms, draw 1100ms.
- **Edge cases & failure modes (v2).** *Diagram in the first
  viewport (short hero):* if the stratum is visible at load, the
  draw begins at load +1000ms (after the rise), still once.
  *Authored cooling order disputed by the subject's literature:*
  the order is content, reviewed like text; the mechanism does not
  care. *Resize during draw:* dashoffset is length-normalised
  (`pathLength`), so scaling cannot desync the draw.
- **Accessibility spec (v2).** The figure carries a real
  `<figcaption>` stating what the plan shows and the one fact it
  proves ("The columns fit without mortar; the grid of this page is
  their plan"). The SVG itself is `role="img"` with an `aria-label`
  summarising the field; the draw is decorative sequencing — the
  finished plan is the content, and it is fully present to AT from
  first paint (undrawn state is visual only, via dashoffset on
  rendered paths).
- **Performance budget & mobile variant.** ≤37 stroke animations,
  CSS-driven from one class; zero per-frame JS. Mobile: the abridged
  field above.
- **Tokens consumed (v2).** `--ash-light`, `--wet`, `--rust`,
  `--basalt`, `--ease-settle`, `--draw-dur` (1400ms), `--draw-stagger`
  (60ms), `--watchdog-draw` (5000ms).

### 6.8 Fissure-glow hover

- **What & why.** Every card and column block in the strata carries
  hairline fissures in its own face (§6.14). When the visitor's
  pointer rests on one, **rust light seeps from its fissures** —
  opacity 0 → 0.7 over 600ms, a slow exhale back over 900ms when the
  pointer leaves. It belongs here because it makes attention
  geological: to look closely at this stone is to see its interior
  heat. The glow lives in the card's own cracks — never as a halo,
  never as a shadow, never around the border — because a lit outline
  is UI chrome and a lit crack is the stone's inside made visible by
  being examined.
- **Structure.** Each fissured block carries an inline SVG (or a
  CSS-masked background) of 2–4 hairline crack paths authored per
  block type (three crack plates are authored once and reused by
  class — cracks repeat in nature; unique-per-card cracks are
  waste). The glow layer is the crack paths stroked in `--rust` at
  1px with a 3px `--rust` blur copy beneath at 0.35, both inside the
  block, clipped to it, `pointer-events: none`, `aria-hidden`. The
  rest state is opacity 0 — **the cracks themselves** (the unlit
  `--joint` hairlines) are always visible; only the light is hover's.
- **Motion spec.** Trigger: pointerenter / focus-within on the block.
  In: opacity 0→0.7 over **600ms `--ease-seep`**, with a 120ms delay
  per crack path in authored order (the seep travels the crack
  network, it does not switch on). Out: 0.7→0 over **900ms
  `--ease-seep`** on leave — stone holds heat longer than it takes
  it, so the exhale is slower than the inhale. On touch: a tap that
  focuses the block's link seeps the glow for the duration of the
  press (§6.14's tap law), then exhales.
- **Choreography timeline (v2).** t+0 (enter): first crack begins →
  +120ms × path: network lights in order → t+600–960ms: full seep
  (0.7) → hold while hovered → leave: exhale begins → t+900ms: dark.
  Focus-within follows the same timeline — keyboard visitors get the
  full seep, not a lesser state.
- **State matrix (v2).** *Rest:* cracks visible, unlit. *Seeping:*
  600ms in. *Lit (hover held):* 0.7 steady — it does not pulse;
  pulsing heat is a game effect. *Exhaling:* 900ms out. *Active
  (press on the block's link):* glow holds at 0.7 through the press
  and the §11 thunk; navigation follows. *Scrolled-past:* unlit;
  seep never runs off-screen. *Disabled block (a card whose content
  is unavailable, §6.14):* no fissures, no glow — dead stone does not
  seep.
- **Content merge.** The light comes from the block's own fissures,
  which are part of its face in every state. The glow is information:
  it marks exactly the block being examined, in the block's own
  material. Remove the cracks and there is nowhere for the light to
  live — the effect cannot be pasted onto a smooth card.
- **Failure fallback.** If SVG/CSS filters are unavailable, the glow
  layer is simply absent; the hover state falls back to the block's
  border lifting `--joint` → `--ash` (a plain, honest hover). The
  unlit cracks and all content are unaffected in every failure.
- **Reduced-motion variant.** No seep animation: on hover/focus the
  glow is present at 0.5 instantly (a state, not a motion), and
  leaves instantly. The information — *this block is being examined*
  — survives; the travelling light rests.
- **Breakpoints (v2).** ≥1200px: full spec (2–4 cracks per block).
  768–1199px: 2–3 cracks, seep 500ms in / 800ms out. <768px: hover
  does not exist; the tap-press seep is instant-on at 0.5 for the
  press duration (as reduced-motion), 2 cracks per block.
- **Edge cases & failure modes (v2).** *Pointer skimming a grid of
  cards:* a 90ms intent delay before the seep starts, so a diagonal
  pass doesn't light six blocks in sequence; leaving within the
  delay cancels cleanly. *Glow over text:* crack plates are authored
  to run through the block's margins and image zones, never across
  its text measure — and at 0.7 over `--basalt`, a 1px rust line
  behind a glyph could not drop contrast below 7:1 in any case; the
  plate law makes it moot. *Many blocks lit in sequence (keyboard
  tabbing through cards):* each block's exhale is independent;
  overlapping exhales are fine — the strata cool one by one.
- **Accessibility spec (v2).** The glow is a supplement to, never a
  replacement for, the block link's focus ring (2px `--ash-light`
  outline, offset 3px — visible against the glow). The seep is not
  announced. Touch targets are the blocks' own links (≥44px).
  Contrast of the lit state: decorative light only; no text changes
  colour.
- **Performance budget & mobile variant.** One opacity transition per
  block, composited; crack SVGs are shared plates (3 authored,
  reused). Mobile: the instant tap variant above.
- **Tokens consumed (v2).** `--rust`, `--joint`, `--ash`, `--ash-light`,
  `--ease-seep`, `--seep-in` (600ms), `--seep-out` (900ms),
  `--glow-peak` (0.7).

### 6.9 Bedrock footer stillness

- **What & why.** The footer is bedrock: a full-width, unbroken
  `--basalt` block that **never moves** — zero parallax, zero entrance
  animation, zero ambient motion — while everything above it rises,
  shears, seeps and settles. Its single event is a **rust line drawing
  across its top edge** when it first enters, 1200ms, and then the
  block simply *is there*, holding the colophon, the strata index and
  the edition line. It belongs here because the contrast is the
  theme's final content statement: after a page of slow movement, the
  visitor arrives at the thing that does not move at all, and feels
  the whole cliff come to rest on it. A footer that also performed
  would spend the theme's last word on nothing.
- **Structure.** A `<footer class="bedrock">`, min-height 320px,
  `--basalt` ground, no caps, no joints, no stagger — its top edge is
  one straight rule: an SVG line 2px in `--rust` spanning the full
  width, drawn by dashoffset. Inside: three columns of apparatus —
  the strata index (links to every stratum, in order), the colophon
  (who made this, from what stone, in what year), and the edition
  line with the page's real figures restated (§6.11's counters at
  rest). The footer is explicitly excluded from §6.4's parallax
  registry and from every reveal system: no `data-depth`, no armed
  classes, ever.
- **Motion spec.** The rust rule: trigger — footer top crossing 85%
  viewport; dashoffset → 0 over **1200ms `--ease-settle`**, once.
  Everything else: none, specified as a positive requirement, not an
  omission — the footer's computed transforms must be `none` at every
  scroll position (gate-checked, §10). Even the ash (§6.6) thins to
  its 0.35 floor above the bedrock and does not fall *inside* the
  footer's first 120px — the weather stops at the bedrock's edge.
- **Choreography timeline (v2).** t+0 (85% crossing): rule begins
  drawing left→right (the direction of reading) → t+1200ms: rule
  complete → thereafter: nothing, for as long as the visitor stays.
  The stillness is the timeline.
- **State matrix (v2).** *Approaching:* plain block entering, rule
  undrawn (armed state, JS only). *Rule drawing:* 1200ms. *At rest
  (terminal, all other states):* the block, its text, its links —
  hover on footer links is the §11 link treatment (underline draw,
  300ms) and nothing more. *Scrolled-past / focus / touch:* identical
  to rest. *Disabled (no-JS):* the rule is fully drawn in markup; the
  block is complete.
- **Content merge.** The bedrock carries the site's foundation
  content — index, colophon, edition figures — in the one block whose
  behaviour *is* its meaning. The stillness is not the absence of an
  effect; it is the effect, and it is made of the footer's own
  refusal to join the systems above it.
- **Failure fallback.** There is almost nothing to fail: no JS is
  required for any footer state except the rule's draw, whose
  fallback is the drawn rule. If the draw's watchdog (entry +3000ms)
  fires, the rule completes instantly.
- **Reduced-motion variant.** Identical to the standard footer except
  the rule is pre-drawn. This is the one element whose reduced-motion
  variant is its own portrait: the theme at rest looks like its
  footer everywhere.
- **Breakpoints (v2).** ≥1200px: three apparatus columns, min-height
  320px. 768–1199px: two columns (index + colophon; edition line full
  width beneath), 280px. <768px: one column, stacked in reading
  order (index, colophon, edition), 240px; the rule still draws full
  width.
- **Edge cases & failure modes (v2).** *Short page (footer in first
  viewport):* the rule draws at load +1200ms (after the rise), once.
  *A builder adds a reveal to the footer "for consistency":* the
  gate (§10) greps the footer for armed/reveal classes and fails the
  build — consistency with the theme means the footer is exempt.
  *Sticky elements above overlapping the bedrock:* nothing on the
  page is sticky except the organ stage (§6.5) and the nav (§6.13),
  both of which release before the bedrock.
- **Accessibility spec (v2).** A real `<footer>` with the index as a
  `<nav aria-label="Strata index">`; links in reading order; the
  rule is `aria-hidden`. Contrast: apparatus text `--ash-light` on
  `--basalt` 6.28:1 ✓; colophon body `--bone-dim` 7.02:1 ✓.
- **Performance budget & mobile variant.** One 1200ms stroke
  animation per page; otherwise zero. The cheapest element in the
  theme, by law.
- **Tokens consumed (v2).** `--basalt`, `--rust`, `--ash-light`,
  `--bone-dim`, `--ease-settle`, `--rule-dur` (1200ms).

### 6.10 Fissure-of-light progress

- **What & why.** The theme's progress indicator, made of the theme's
  own material: a **fissure of rust light creeping down the left edge
  of the leftmost column** as total page progress grows — a lit crack
  lengthening down the cliff face the visitor is descending, its hot
  core in `--rust-pale`, its body in `--rust`. It belongs here because
  progress on this page is depth, and depth is drawn in the cliff's
  own substance: there is no bar (§11 refuses the progress bar by
  name), there is only the crack of light showing how far down the
  face the reading has reached. Beside its tip, in the navigation
  (§6.13), the current stratum's name is lettered — the light says
  *how far*, the apparatus says *where*.
- **Structure.** A fixed rail at the viewport's left edge, 4px wide,
  full height, on the page's margin (outside the column grid, over
  `--basalt`), containing an SVG vertical path — a slightly irregular
  line (the same crack hand as §6.3, gentler: angles ≤10°) whose
  drawn length is scrubbed by `stroke-dashoffset`. Two strokes: the
  body (`--rust`, 3px, opacity 0.85) and the core (`--rust-pale`,
  1px) drawn over the body's leading 40%. The rail is `aria-hidden`;
  its information is duplicated as text in §6.13.
- **Motion spec.** Trigger: continuous scroll; drawn length = total
  document progress (0→1 maps to rail top→bottom), driven by the
  shared loop (lerp 0.08 — the light lags the scroll like everything
  stone). Unlike §6.3's fissure, the light **ratchets**: scrolling up
  does not un-draw it. Light that has entered the crack does not
  leave; the drawn length is the maximum progress reached this
  session. (The stratum readout in §6.13, being information, follows
  the current position honestly in both directions.)
- **Choreography timeline (v2).** Spatial: 0% — rail dark, a hairline
  joint only → first scroll: the light strikes at the top and begins
  its creep → mid-page: light at the mapped depth, tip glowing
  `--rust-pale` → 100%: rail fully lit; on first reaching the bottom
  the tip brightens once (opacity pulse 0.85→1 over 600ms
  `--ease-seep`) and rests — the descent is complete, the crack is
  lit to the bedrock.
- **State matrix (v2).** *Top:* dark rail. *Descending:* length =
  max progress, tip lit. *Scrolling up:* length holds (ratchet);
  tip stays at the deepest point reached. *At bottom:* full rail,
  tip pulse fired once. *Hover/focus:* none — the rail is not
  interactive. *Disabled (no-JS):* no rail (it is JS-armed); the
  §6.13 readout still reports the current stratum from scroll
  position… without JS there is no readout either — the strata's own
  joint bands (§4) carry their names in flow, so orientation never
  depended on the rail. Touch: identical.
- **Content merge.** The light runs down the edge of the very column
  the visitor is reading beside, in the cliff's own rust. It measures
  the page's own strata — its length is the page's depth, drawn on
  the page's face.
- **Failure fallback.** JS off: no rail, nothing missing — progress
  chrome is the theme's garnish, and the joint bands name every
  stratum in the document itself. Loop failure mid-page: the light
  freezes at its last length; a frozen crack of light is still a
  crack of light.
- **Reduced-motion variant.** The light is drawn instantly to the
  mapped length per scroll position (it is a scrubbed state, not an
  animation), and the ratchet still applies; the bottom pulse does
  not fire.
- **Breakpoints (v2).** ≥1200px: 4px rail at the left margin.
  768–1199px: 3px rail. <768px: rail hidden — a phone cliff has no
  margin for a second edge; progress is carried by the §6.13 compact
  bar's stratum name alone.
- **Edge cases & failure modes (v2).** *Short page (one screen):*
  progress maps across the little scroll there is; a page with no
  scroll shows the rail fully lit at load (the whole face is visible;
  the crack is lit because there is nothing left to descend).
  *Anchor jump to the footer:* the light settles to full within the
  lerp (~700ms) — no catch-up sweep; light does not perform for
  teleporting visitors. *Resize:* rail height re-measures, length
  re-maps proportionally.
- **Accessibility spec (v2).** `aria-hidden` decoration. The
  information it visualises — current stratum, of how many — is real
  text in §6.13's navigation and in each stratum's own joint band.
  The rust tones are never the sole carrier of any state.
- **Performance budget & mobile variant.** One dashoffset write per
  frame in the shared loop. Mobile: hidden, per breakpoints.
- **Tokens consumed (v2).** `--rust`, `--rust-pale`, `--basalt`,
  `--ease-seep`, `--loop-lerp` (0.08), `--rail-w` (4px).

### 6.11 Chiselled counters

- **What & why.** Where the page states its great figures — the age
  of the flow in years, the depth of the section in metres, the
  count of columns in the organ — the figures **count up in chiselled
  numerals** when their stratum enters: Fraunces tabular numerals,
  rising over 2400ms with the patience of a man carving them. It
  belongs here because in this theme numbers are not data decoration;
  they are the subject's scale, and scale deserves ceremony. A figure
  of 187,000,000 years that simply appears is a statistic; the same
  figure *arriving*, digit by digit, over 2.4 seconds, is deep time
  being given its weight. The count is a replay between two true
  values — from the figure's stated floor (often the previous
  survey's figure, named in the caption) to the current figure —
  never from an invented zero unless zero is the honest floor.
- **Structure.** A `.figure` block: the numeral in Fraunces 800
  tabular at 44–64px, its unit and name in apparatus type beneath
  ("MILLION YEARS — AGE OF THE UPPER FLOW"), and a caption line
  stating the figure's provenance ("County survey, 2019; recounted
  2024"). The final value is the DOM text; JS animates a textContent
  interpolation between floor and final with tabular figures and
  locale grouping (187,000,000 — grouping is part of legibility at
  this scale). Each figure counts **once**, when its stratum crosses
  55% viewport.
- **Motion spec.** Trigger: stratum entry (55%). Duration **2400ms
  `--ease-settle`** — the slowest counter in the library; the easing
  means the count moves briskly through its early range and
  *labours* into its final digits, the way carving slows at the
  detail. Values are rounded to the figure's stated precision at
  every frame (a figure stated to 3 significant digits never shows
  9 during the count). Counting is textContent writes throttled to
  every other frame — 30 writes/sec is plenty for stone.
- **Choreography timeline (v2).** t+0 (55% crossing): figure at its
  floor value → t+0–2400ms: count runs, ease-settle curve → t+2400ms:
  final value; the caption's provenance line fades in (400ms) — the
  figure is believed once its source arrives → terminal. Scroll-back
  never recounts; a counted figure is a carved figure.
- **State matrix (v2).** *Uncounted (below fold):* the floor value is
  printed in the DOM — which, by the content law, is itself a true
  figure (the earlier survey's), so even the uncounted state is
  honest. *Counting:* 2400ms. *Counted (terminal):* final value +
  provenance. *Hover/focus:* none. *Scrolled-past:* counted.
  *Disabled (no-JS):* the final value is… the DOM ships the **final**
  value and JS *sets* the floor when arming — so no-JS shows the
  current figure, and the armed floor exists only where the count
  will actually run. Touch: identical.
- **Content merge.** The figures are the stratum's own measurements —
  the age of the very flow whose columns carry the page, the depth
  of the very section in §6.7's plan. The count's floor and final are
  both the subject's real published numbers (two surveys), so the
  animation is a small history of the measurement itself.
- **Failure fallback.** If the loop or IO fails, figures stand at
  their DOM (final) values. If JS arms the floor but the count never
  triggers (stratum skipped by a jump), a 1500ms watchdog after the
  stratum is first *passed* sets the final value — a figure may
  never be left at its floor by a fast scroll.
- **Reduced-motion variant.** No count. The final value stands, with
  its provenance line, from first paint.
- **Breakpoints (v2).** ≥1200px: numerals 56–64px. 768–1199px:
  48px. <768px: 40px, count duration 2000ms (a shorter ceremony for
  a smaller stone, still never fast).
- **Edge cases & failure modes (v2).** *Figure with no honest floor*
  (a count of things, where the floor would be a lie): the count
  runs from the figure's own stated starting point in its caption
  ("columns standing in 1900: 41 → today: 63") or does not run at
  all — a figure without a true floor is printed static, which the
  theme prefers to a theatrical zero. *Huge figures (10⁹):* grouping
  and precision laws hold; duration stays 2400ms — the count is a
  gesture, not an odometer. *Multiple figures in one stratum:* they
  count in reading order, staggered 200ms, never simultaneously —
  one carving at a time.
- **Accessibility spec (v2).** The figure block is `aria-live="off"`
  during the count and the final value is the accessible text from
  first paint in the DOM order (the visual interpolation is
  `aria-hidden` on a clone span; the real value sits in a
  visually-hidden sibling — no: simpler and binding: the count
  writes to the real node, and the node carries
  `aria-label="187 million years"` in full words throughout, so AT
  never hears a half-counted number). Contrast: numerals `--bone`
  on their stratum ground, ≥7.87:1 ✓.
- **Performance budget & mobile variant.** ≤3 figures per page,
  textContent writes only, throttled. Mobile: 2000ms variant above.
- **Tokens consumed (v2).** `--bone`, `--bone-dim`, `--ease-settle`,
  `--count-dur` (2400ms), `--count-stagger` (200ms).

### 6.12 Stone-frame image settle

- **What & why.** Every photograph on the page lives in a **stone
  frame** — a 10px `--wet` border with a hexagonal cap notch at its
  top centre — and as it travels through the viewport it **settles:
  scale 1.08 → 1.0**, scrubbed, as if the plate were being lowered
  into its frame and coming to rest at reading distance. It belongs
  here because images in this theme are specimens *of* the cliff —
  outcrop photographs, section plates, portraits of the stone — and a
  specimen is placed, not pasted. The settle is the placing. The
  frame never moves; the picture comes to rest inside it, and the
  8% of travel is the difference between a picture being carried past
  and a picture being *hung*.
- **Structure.** A `<figure class="plate">`: the stone frame (border
  + cap notch via an SVG corner piece), an inner `.plate-window`
  with `overflow: hidden` and the plate's true `aspect-ratio`
  reserved, and the `<img>` at 1.08 base scale inside. Images are
  treated plates: duotone-leaning, contrast held so the darkest
  tone sits at `--wet` not black (a photograph's blacks are never
  deeper than the cliff's own stone). The caption sits beneath the
  frame in apparatus type with the plate's number ("PLATE IV — THE
  ORGAN FROM THE NORTH").
- **Motion spec.** Trigger: continuous scroll. A per-image settle
  value `s` maps the image's transit (frame top at 92% vh → frame
  centre at 52% vh) to scale 1.08→1.0, driven by the shared loop
  (lerp 0.08). Unlike a reveal, the settle is **symmetric**: scrolling
  back up un-settles the plate toward 1.08 as it leaves downward —
  plates are at rest only while being read. Images carry 10% bleed
  in the asset (sized 1.1× the window) so the 1.08 state never
  exposes an unprinted edge.
- **Choreography timeline (v2).** Spatial: frame top at 92% vh —
  scale 1.08 → centre approach — 1.04 → centre at 52% vh — 1.0, at
  rest → read → exits upward — stays 1.0 while above centre (a read
  plate does not unsettle behind the visitor; the symmetry applies
  only below centre) → re-entering from below replays the settle.
- **State matrix (v2).** *Approaching:* 1.08→1.0 scrubbed. *At rest
  (centre band):* 1.0. *Scrolled-past:* 1.0, loop stops writing it.
  *Hover:* nothing — plates do not perform; §6.8's seep belongs to
  fissured blocks, and a plate's frame has no fissures. *Focus (if
  the plate is a link):* settles instantly to 1.0 — a focused plate
  is a read plate. *Disabled (no-JS):* all plates at 1.0 (markup
  default; JS arms the 1.08 only for plates below the fold it will
  drive). Touch: identical scrub.
- **Content merge.** The settle happens inside the plate's own stone
  frame, on the plate's own image. The frame is the page's furniture
  for *this* picture; the motion is the hanging of it.
- **Failure fallback.** Plates render at 1.0 by default; a 1200ms
  watchdog per plate forces scale 1.0 if the loop stalls while the
  plate is in the centre band. Broken image: the frame stands with
  its alt text lettered inside in apparatus type — a labelled empty
  frame, never a torn-image icon.
- **Reduced-motion variant.** All plates at 1.0 at all times. The
  frames and captions — the content — are untouched.
- **Breakpoints (v2).** ≥1200px: full range 1.08→1, frame 10px.
  768–1199px: 1.06→1, frame 8px. <768px: 1.04→1, frame 6px, cap
  notch dropped (a phone frame is a frame, not a monument).
- **Edge cases & failure modes (v2).** *Plate inside the organ pin
  (§6.5):* pipes use their own brightening; the settle is disabled
  inside the organ (two scrubs on one image would fight — the pin
  owns its plates). *Very wide plates (panoramas):* the settle range
  narrows to 1.05→1 so the crop travel stays inside the bleed.
  *Layout shift:* aspect-ratio is reserved from the plate's real
  dimensions; the settle is transform-only — CLS is 0 by
  construction.
- **Accessibility spec (v2).** Real `alt` on every plate; the scale
  never crops content the alt describes as essential (plates are
  composed with their subject inside the central 80%). The settle is
  unannounced, decorative motion on announced content.
- **Performance budget & mobile variant.** Transform writes only for
  plates within ±1 viewport (≤4 active), inside the shared loop.
  Plate assets ≤90KB each (§14). Mobile: the 1.04 variant above.
- **Tokens consumed (v2).** `--wet`, `--joint`, `--loop-lerp` (0.08),
  `--settle-unset` (1.08), `--frame-w` (10px), `--watchdog-img`
  (1200ms).

### Page-family elements

### 6.13 Column-joint navigation (page family: navigation)

- **What & why.** Navigation in this theme is the cliff's own
  carpentry: a bar of `--basalt` pinned to the top, its links
  separated by **hexagon joints** — small point-up hexagon glyphs,
  the column caps in miniature — and at its right end, the **stratum
  readout**: the name of the stratum currently being read, lettered
  in apparatus type ("STRATUM III — THE SECTION"), which is §6.10's
  progress light translated into words. It belongs here because a
  cliff is navigated by its layers: the visitor is never "on a page",
  they are *in a stratum*, and the navigation's job is to say which
  one and to offer the others as joints to travel along.
- **Structure.** A `<header class="cap-bar">`, sticky, 56px,
  `--basalt` at 96% with a 1px `--joint` bottom rule. Contents: the
  site's mark (a single hexagon + wordmark in Fraunces 700), the
  `<nav>` of stratum links (each preceded by its hexagon joint,
  drawn as inline SVG), and the readout `<p class="stratum-now">`.
  On mobile the nav collapses behind a "STRATA" button opening a
  full-width panel of joints (the §11 strata panel). The current
  stratum's link carries `--rust-bright` text and its hexagon filled
  `--rust` — the only filled hexagon in the bar.
- **Motion spec.** The bar itself never animates its position (sticky
  is a state, not a motion). Readout changes: when the current
  stratum changes (its joint band crossing 45% viewport), the readout
  text crossfades 200ms `--ease-settle` and the nav's filled hexagon
  moves (the fill is a class change, no travelling element — joints
  do not slide, they are re-cut). Link hover: the link's hexagon
  rotates 30° over 400ms `--ease-settle` (a hexagon turning from
  point-up to flat-top — the joint settling into its socket) and the
  link text lifts `--bone-dim` → `--bone`.
- **Choreography timeline (v2).** Scroll: stratum joint crosses 45%
  → readout fades out (100ms) → text swaps → fades in (100ms) →
  hexagon fill moves. Hover: t+0 rotation begins → t+400ms joint
  seated. The mobile panel opens with the strata wipe at half scale
  (350ms down, §6.16's grammar at panel size).
- **State matrix (v2).** *Rest:* bar pinned, readout = current
  stratum. *Hover (link):* hexagon rotated, text lit. *Focus:* same
  as hover + the §11 focus ring. *Active/current:* filled hexagon +
  `--rust-bright` name. *Scrolled-past:* the bar is always present
  (it is the pinned cap of the cliff). *Disabled:* a stratum with no
  content is absent from the nav — never a greyed joint. Touch:
  readout present; panel via the STRATA button (≥44px target).
- **Content merge.** The nav's links are the page's actual strata, in
  order, generated from the strata's own joint-band names — add a
  stratum and the nav gains a joint, because the nav *is* the cliff's
  table of layers. The readout is the same fact §6.10 draws in light.
- **Failure fallback.** Without JS: the bar is a static header with
  anchor links and the readout shows the first stratum's name (or is
  omitted by the server where unknown); anchors carry
  `scroll-margin-top: 72px` so targets land below the bar. The
  scrollspy is the only JS behaviour; its absence costs the readout,
  nothing else.
- **Reduced-motion variant.** Readout swaps instantly; hexagons do
  not rotate (hover lifts text colour only); the mobile panel opens
  instantly.
- **Breakpoints (v2).** ≥1200px: full bar, all joints visible.
  768–1199px: joints for the first-level strata only; readout kept.
  <768px: mark + readout (truncated to the stratum numeral, "III")
  + STRATA button and panel.
- **Edge cases & failure modes (v2).** *More strata than the bar
  holds (>6):* the bar shows the current stratum's neighbours ±2 and
  the panel holds the full index — a bar of nine joints is a
  honeycomb, not a navigation. *Long stratum names:* readout
  truncates at 26ch with the full name in the joint band itself
  (§4), which the visitor can always scroll to. *Single-stratum
  page:* the readout and joints are omitted — a single layer needs
  no index.
- **Accessibility spec (v2).** `<nav aria-label="Strata">`; current
  link carries `aria-current="true"`, updated only on stratum change
  (throttled). Hexagons are `aria-hidden` SVG. Focus order = stratum
  order. Contrast: readout `--ash-light` on `--basalt` 6.28:1 ✓;
  current name `--rust-bright` 4.66:1 ✓ at 14px+.
- **Performance budget & mobile variant.** Scrollspy on the shared
  IntersectionObserver; readout writes throttled to changes. Mobile:
  the panel variant above.
- **Tokens consumed (v2).** `--basalt`, `--joint`, `--rust`,
  `--rust-bright`, `--bone`, `--bone-dim`, `--ash-light`,
  `--ease-settle`, `--bar-h` (56px).

### 6.14 Strata cards (page family: cards / listing)

- **What & why.** The card in this theme is a **short column**: a
  `--wet` block with a hexagonal cap, its own hairline fissures
  (§6.8's plates), a Fraunces head, an Archivo standfirst, a plate
  (§6.12) where the listed thing has one, and an apparatus foot
  (stratum, figure, date — the listing's real data). Cards are how
  the theme lists: outcrops, sections, specimens, chapters. They
  belong in column form because in this world a list is a row of
  small cliffs standing on a shared stratum — varied in height by
  their content, never a uniform grid of identical boxes, which is
  the one arrangement a cliff never makes.
- **Structure.** An `<article class="strata-card">`: cap headpiece,
  plate (optional, §6.12 settle applies), body (kicker in apparatus,
  H3 head, standfirst ≤3 lines), fissure SVG layer (§6.8), apparatus
  foot. The whole card is one link (stretched-link over the head)
  unless it carries a second action, in which case it is a group
  with two explicit targets. Cards stand in the column grid (§4) at
  mixed spans — a listing row mixes 1fr and 2fr cards by the
  importance of their content, stated in the build, not randomised.
- **Motion spec.** Entry: cards do **not** rise (the rise is the
  hero's alone, §6.1) — a card enters with a 600ms `--ease-settle`
  joint-draw: its cap's outline strokes in (dashoffset, as §6.7 at
  card scale) as the card's stratum enters, and the card is simply
  present. Hover: §6.8's fissure seep (600ms in, 900ms out) plus the
  cap lifting 2px (`--ease-settle`, 300ms) — the cap stone stirring,
  nothing more. Active (press): cap presses back to 0 and the seep
  holds through the §11 thunk timing.
- **Choreography timeline (v2).** Entry: cap outline draws 600ms →
  card at rest. Hover: t+0 seep begins (crack order per §6.8) +
  cap lift → t+600ms full seep, cap at 2px → leave: cap settles
  300ms, seep exhales 900ms.
- **State matrix (v2).** *Rest:* standing card, fissures unlit.
  *Hover:* seep + cap lift. *Focus:* seep + cap lift + focus ring
  on the head link. *Active:* cap pressed, seep held. *Scrolled-past:*
  at rest. *Disabled (the listed thing is unavailable):* the card is
  rendered **without fissures and without a link**, its foot lettered
  with the reason in apparatus ("NOT STANDING — SURVEYED 2019, FELL
  2021") — dead stone, honestly labelled, never a greyed-out live
  card. Touch: tap goes straight through (no first-tap seep tax);
  the seep runs during the press only.
- **Content merge.** Every part of the card is the listed thing's own
  data: its plate, its head, its figure, its fissures in its own
  face. The cap-draw entry manufactures the card in front of the
  reader the way §6.7 manufactures the plan — the listing is built
  of the same stone as the page.
- **Failure fallback.** Static card, cap drawn (markup state),
  fissures unlit. No-JS loses the seep and the draw only.
- **Reduced-motion variant.** No cap draw (caps present), no seep
  travel (hover = instant 0.5 glow per §6.8), no cap lift (hover
  lifts the head's colour `--bone-dim` → `--bone` instead).
- **Breakpoints (v2).** ≥1200px: mixed spans in the 12-unit grid.
  768–1199px: two-up, uniform 1fr pairs allowed (a tablet cliff is
  younger, its columns more even). <768px: one-up stacked, cap kept,
  plate above the head, standfirst 3 lines.
- **Edge cases & failure modes (v2).** *Card with no plate:* the
  cap + a fleuron block in `--wet` relief (a carved hexagon) holds
  the plate's space — never a stock image, never a blank.
  *Very long head:* clamps at 2 lines; the full head is the link's
  accessible name. *A whole listing entering at once:* cap draws
  stagger 90ms in reading order, capped at 8 draws per second — the
  rest appear drawn.
- **Accessibility spec (v2).** One link per card (its head), named
  by the full head text; plate `alt=""` when the head names the
  content, real alt when the plate *is* the content (specimen
  listings) — chosen per build, consistently. The apparatus foot is
  real text in reading order. Focus ring 2px `--ash-light`, offset
  3px, visible over the seep.
- **Performance budget & mobile variant.** Cap draws are CSS from
  one class; seep is §6.8's budget. Plates inherit §6.12's caps.
  Mobile: stacked variant above; seep is press-only.
- **Tokens consumed (v2).** `--wet`, `--basalt`, `--bone`,
  `--bone-dim`, `--joint`, `--ease-settle`, `--seep-in` (600ms),
  `--cap-draw` (600ms).

### 6.15 The seam form (page family: forms / conversion)

- **What & why.** Conversion in this theme happens at a **seam**: the
  one place where two strata meet and something can be joined. The
  form — an enquiry, a booking, a survey request — is set into the
  page's calcite stratum (§4) as a horizontal seam between two stone
  edges: fields chiselled into the pale stone, labels cut above them
  in apparatus type, and on successful submission the seam **closes**:
  the two edges draw together over 800ms and the confirmation is
  lettered along the closed joint, with its reference. It belongs
  here because joining is the theme's only transactional act — the
  visitor is not "converting", they are being *set into the cliff*,
  and the form's honesty (few fields, named purpose, a reference that
  is a real record) is the theme's answer to the funnel.
- **Structure.** A `<form class="seam-form">` inside the calcite
  stratum: an upper stone edge (a `--wet` band with a joint line) and
  a lower edge, with the fields between them on the calcite ground.
  Fields: inset `--basalt` at 6% over calcite (a chiselled hollow),
  1px `--ash` border, `--basalt` text at 17px Archivo, labels above
  in apparatus. One primary action: the §11 thunk button ("SET THE
  REQUEST IN STONE" is too cute — the button says what happens:
  "Send the request"). Errors appear as **fault notes**: a
  `--rust-bright` sentence-case line beneath the field, preceded by
  a small fault glyph (a 12px crack SVG), written in the §12 fault
  voice. Success: the form's fields fade to the calcite (300ms), the
  two edges translate together (upper down 10px, lower up 10px,
  800ms `--ease-settle`), and the confirmation line is lettered along
  the joint: "Set in the seam · Reference SEAM 214 · We answer within
  five working days." — the reference and the promise both real, or
  the line is not printed.
- **Motion spec.** Field focus: the field's border cuts deeper
  (`--ash` → `--basalt`, 200ms) and a 2px `--rust` tick draws at the
  field's left end (200ms `--ease-settle`) — the chisel marks where
  you are cutting. Submit press: §11's thunk (scale 0.97, 120ms,
  release 400ms). Error arrival: the fault note letters in with a
  300ms joint-draw (dashoffset on its crack glyph) — faults appear
  the way faults do, along a line. Success seam-close: as structure,
  800ms, once, irreversible in the session (the form is replaced by
  the closed seam + a "Make another request" text link that re-opens
  a fresh form beneath).
- **Choreography timeline (v2).** Focus: t+0 border deepens, tick
  draws → t+200ms field armed. Submit: t+0 thunk → validation →
  errors: fault notes draw in field order, 300ms each, focus moves
  to the first faulted field → success: t+0 fields fade (300ms) →
  t+300ms edges begin closing → t+1100ms seam closed, confirmation
  lettered (apparatus, fade 400ms) → the seam is part of the cliff.
- **State matrix (v2).** *Rest:* open seam, fields empty, edges
  apart. *Focus:* deepened border + tick. *Filled/valid:* tick
  becomes a full left rule (the cut is true). *Error:* fault note
  present, field border `--rust-bright`. *Submitting:* button in its
  pressed state, fields inert, no spinner (§11 refuses it — the
  button's label changes to "Setting…" in apparatus). *Success:*
  closed seam + confirmation. *Disabled (form closed by the
  operator, e.g. survey season ended):* the seam ships closed with
  its reason lettered along the joint ("The seam is closed until the
  spring survey") — the honest state, not a greyed form. Touch:
  identical; targets ≥48px.
- **Content merge.** The form's fields, its reference and its promise
  are the transaction itself, set in the page's one pale stratum —
  the human layer (§4). The closing seam is not a success animation
  laid over the form; it is the form's own two edges completing the
  act the visitor came for.
- **Failure fallback.** A plain form on the calcite ground with
  standard submit; without JS the seam does not close — the server
  returns a confirmation stratum (a full page state, not a trick).
  A submission that fails server-side reopens the seam with the
  visitor's entries intact and a fault note at the form's head in
  the §12 voice ("The seam did not hold. Your words are kept above;
  try once more.") — entries are never lost to an error.
- **Reduced-motion variant.** No closing animation: on success the
  closed seam + confirmation simply replace the form. Focus tick and
  fault glyphs appear instantly. The states are identical; only the
  joining is not performed.
- **Breakpoints (v2).** ≥1200px: two-column fields inside the seam
  (name/email side by side, message full width). 768–1199px: single
  column, edges 8px travel. <768px: single column, edge travel 6px,
  labels above fields always (no floating labels anywhere in this
  theme, at any size).
- **Edge cases & failure modes (v2).** *Long error text:* fault
  notes wrap to two lines max by copy law (§12) — an error needing
  three lines is two errors or bad copy. *Autofill:* fields accept
  it; the tick state updates on the `input` event autofill fires —
  a pre-filled valid field shows its rule without ceremony.
  *Double submit:* the button inerts itself at first press; the
  reference is issued once, server-side.
- **Accessibility spec (v2).** Labels are real `<label>`s, always
  visible. Errors are `aria-describedby`-linked and announced via a
  polite live region summarising the count ("Two faults to mend")
  before focus moves. The success confirmation is a `role="status"`
  region. Contrast on calcite: text `--basalt` 10.28:1 ✓; fault
  notes use `--rust-bright`… on calcite that pairing is 1.9:1 ✗ —
  therefore on the calcite stratum fault notes are set in
  `--basalt` with the `--rust` crack glyph carrying the colour, and
  the `--rust-bright` text treatment applies only to faults lettered
  on `--basalt` grounds elsewhere (the §11 alert). This pairing law
  is gate-checked (§10).
- **Performance budget & mobile variant.** The seam-close is two
  transforms + one fade, once. No libraries. Mobile: the 6px-travel
  variant above.
- **Tokens consumed (v2).** `--calcite`, `--basalt`, `--wet`,
  `--ash`, `--rust`, `--rust-bright`, `--ease-settle`, `--seam-close`
  (800ms), `--fault-draw` (300ms).

### 6.16 Ash-veil skeleton + strata-wipe transition (page family: loader / transition)

- **What & why.** The theme's two state-change rituals, sharing one
  material. **Loading** shows the stratum's blocks as unrisen stone:
  `--wet` blocks at their true sizes with a slow drift of ash across
  them (a 3.2s `--ease-drift` shimmer of `--ash` at 0.12) — the
  content is *under ash*, not yet excavated. **Navigation** is the
  strata wipe: three full-width bands slide across the viewport at
  the strata rates (far band slowest), meet, and the new page is
  revealed already standing — a cliff face replaced by another cliff
  face, layer by layer. Both belong here because they are the theme's
  own substances (ash, strata) doing the two jobs every site must do;
  a spinner or a fade would be foreign objects on the cliff.
- **Structure.** Skeleton: the real layout rendered with `.is-veiled`
  blocks — true geometry (columns, caps, plates at their reserved
  sizes), interiors as `--wet` with the ash drift as a CSS gradient
  animation. Wipe: a fixed `.strata-wipe` of three stacked bands
  (`--wet`, `--basalt`, `--joint` with a rust hairline on the middle
  band's leading edge), parked off-canvas above; on navigation they
  translate down at staggered rates (total cover 700ms), the route
  swaps at full cover, and the bands continue down and off (700ms) —
  the wipe passes *through*, it does not retreat.
- **Motion spec.** Veil: ash drift 3.2s loop, opacity ≤0.12 — the
  slowest, faintest shimmer permitted; any block still veiled at
  **1200ms** has its veil stripped (blocks become plain `--wet`) and
  receives content plainly when it comes. Wipe: 700ms cover
  (`--ease-settle`, bands staggered 90ms by rate order far→near),
  swap at cover, 700ms reveal; total 1400ms. Incoming page arrives
  *standing* — its hero does not re-rise after a wipe (the rise is
  for first arrival only, §6.1).
- **Choreography timeline (v2).** Wipe: t+0 bands begin (far first)
  → t+700ms full cover, route swaps, scroll to top → t+1400ms bands
  clear below, new cliff standing → t+1500ms watchdog: any wipe not
  completed is torn down and the destination shown plainly.
  Veil: per block, t+0 veiled → content lands: veil fades 300ms →
  block live; t+1200ms: strip law.
- **State matrix (v2).** *Veiled:* blocks at true size, ash drifting.
  *Resolving:* 300ms fade per block. *Live:* normal stratum.
  *Wiping:* covering → covered (swap) → revealing → idle.
  *Hover/focus:* links under a veil are not yet links (the block is
  inert, `aria-busy`). *Disabled (no-JS):* veils are never rendered
  unresolved (server pages ship live); navigation is plain. Touch:
  wipe 1200ms total (600/600).
- **Content merge.** The veil covers the block's own true geometry —
  layout shift is zero by construction, and what is under the ash is
  the stratum itself being excavated. The wipe's bands are strata —
  the page is replaced by its own geology, in its own order.
- **Failure fallback.** Veils exist only inside client fetches that
  own their 1200ms strip watchdog. The wipe decorates links it can
  intercept and never breaks one it can't: modified clicks, new-tab
  and external links bypass it entirely; a slow destination holds at
  full cover with the middle band's rust hairline pulsing once per
  2s (the cliff is being raised) up to 4s, then the wipe aborts,
  bands retreat upward (400ms), and native load proceeds.
- **Reduced-motion variant.** Veil: plain `--wet` blocks, no drift;
  content fades in at 150ms or appears. Wipe: no bands; instant
  navigation with the §6.13 readout naming the destination stratum —
  the change is marked by apparatus, not by theatre.
- **Breakpoints (v2).** ≥1200px: full spec. 768–1199px: wipe 1300ms.
  <768px: wipe 1200ms, two bands (the joint band is dropped — a
  phone cliff has fewer layers to spare).
- **Edge cases & failure modes (v2).** *Same-page anchors:* no wipe
  — anchors scroll (§6.13's scroll-margin applies). *Back/forward:*
  no wipe; the browser's gesture rules. *Content that errors:* the
  veiled block resolves into the §11 fault panel with its note in
  the §12 voice — a stratum reports its own failure in character.
  *Prefetch:* hovered internal links may prefetch; the wipe still
  runs its full 1400ms — the ritual is the point, not the wait.
- **Accessibility spec (v2).** During a wipe the outgoing page is
  `inert` from cover start; at reveal, focus moves to the new page's
  `<h1>` (tabindex −1) with a polite announcement ("Stratum: [page
  name]"). Veiled regions carry `aria-busy="true"` until live, with
  one announcement per region, never per block.
- **Performance budget & mobile variant.** Veil gradients are CSS;
  the wipe is three transforms on fixed bands. Mobile: as
  breakpoints.
- **Tokens consumed (v2).** `--wet`, `--basalt`, `--joint`, `--ash`,
  `--rust`, `--ease-settle`, `--ease-drift`, `--wipe-dur` (1400ms),
  `--veil-strip` (1200ms).

### 6.17 The unquarried block (page family: 404 / empty state)

- **What & why.** A missing page in this theme is a block that was
  never quarried: a single column outline — cap drawn, face empty of
  everything but one line of apparatus and one sentence of copy —
  standing in an otherwise bare cliff. It belongs here because the
  theme's honesty about absence is geological: the page does not
  apologise with a mascot or a joke; it shows the visitor the exact
  shape of what is not there, and the two ways forward (the strata
  index, the last standing stratum). Empty states (a stratum with no
  specimens yet, a search with no outcrops) use the same block at
  stratum scale: an unquarried bay in the row, labelled, with the
  reason it is empty and the date it may be filled.
- **Structure.** A centred `.unquarried` block (the page's second
  permitted centred element, §4): a column outline in `--ash` 1.5px
  (cap + two side joints, no bottom line — the block was never cut
  free), inside it the apparatus line "STRATUM NOT LAID DOWN" and the
  copy (§12's empty voice): "Nothing stands here. The survey records
  no column at this mark." Beneath: two text links — "The strata
  index" (to §6.9's index) and "Return to the last standing stratum"
  (the referring page or home). For empty states, the same outline at
  card size (§6.14) inside the listing grid, its foot lettered with
  the reason.
- **Motion spec.** One motion only: the outline **draws** on entry —
  cap first (500ms), then the two joints descend together (700ms),
  `--ease-settle`, dashoffset as §6.7 — the block is *surveyed* in
  front of the visitor, and the survey finds nothing. It never
  fills. There is no second animation; an empty block that performed
  would be lying about being empty.
- **Choreography timeline (v2).** t+0 (entry): cap draws → t+500ms:
  joints begin → t+1200ms: outline complete, copy fades in (300ms)
  → terminal: the absence, surveyed.
- **State matrix (v2).** *Undrawn (armed):* JS-only pre-state.
  *Drawing:* 1200ms. *Standing empty (terminal):* outline + copy +
  links. *Hover/focus:* the links take the §11 link treatment;
  the block itself has no hover — nothing is there to hover.
  *Disabled:* n/a. Touch: identical.
- **Content merge.** The block's outline is the exact geometry of the
  columns everywhere else on the page — the absence is measured in
  the page's own units. The copy names the survey (the site's own
  record) as the authority for the absence.
- **Failure fallback.** No-JS: the outline is fully drawn in markup;
  the block is complete. The draw is the only JS behaviour.
- **Reduced-motion variant.** Outline present, copy present, no draw.
- **Breakpoints (v2).** ≥1200px: block 420px wide. 768–1199px: 360px.
  <768px: full-width minus margins; the draw shortens to 900ms.
- **Edge cases & failure modes (v2).** *A 404 for a page that existed
  and fell* (removed content): the copy changes by build flag to the
  past tense — "A column stood here. It was taken down in the 2024
  survey." — with the date real or the sentence unprinted (§1's
  figure law). *Search with results:* no block; the block appears
  only at zero results, never as a decorative "no more" footer.
- **Accessibility spec (v2).** The block is the page's `<main>` with
  an `<h1>` ("Stratum not laid down"); links are real links with
  descriptive names. The outline is `aria-hidden`. Contrast: copy
  `--bone` on `--basalt` 10.28:1 ✓; apparatus `--ash-light` 6.28:1 ✓.
- **Performance budget & mobile variant.** One SVG draw, once.
  Negligible.
- **Tokens consumed (v2).** `--ash`, `--ash-light`, `--bone`,
  `--basalt`, `--ease-settle`, `--survey-dur` (1200ms).

### 6.18 Fault-block accordions (page family: accordions / detail)

- **What & why.** Long detail — a stratum's full survey notes, a
  specimen's measurements, an FAQ cut into the cliff — is held in
  **fault blocks**: sections separated by fault lines (the crack
  plates of §6.8, unlit), where opening a block makes it **drop 8px
  along its fault** as its content is revealed — the block has
  slipped down its fracture, the way faulted strata do, and the drop
  is the disclosure. It belongs here because this theme cannot use a
  chevron-and-slide accordion imported from a SaaS kit: its
  expansions must be geological events, and a fault slip is the one
  expansion a cliff performs on itself.
- **Structure.** A `.fault-stack` of `.fault-block`s: a header row
  (Fraunces H3 head + a hexagon toggle glyph) ruled below by its
  fault line, and a body region. Opening: the body is revealed by a
  grid-rows 0fr→1fr transition while the whole block translates down
  8px and its fault line's lower lip (a 4px `--wet` ledge) becomes
  visible — the block now stands *lower* than its neighbours, and
  stays lower while open (the slip is a state, not just a motion).
  Only one block in a stack is open at a time by default (a fault
  slips once); a `data-multi` stack may hold several.
- **Motion spec.** Trigger: click/tap on the header (a real
  `<button aria-expanded>`). Open: body reveal 600ms `--ease-settle`,
  block drop 8px across the same 600ms (the drop and the reveal are
  one event, eased together), hexagon glyph rotates 30° (point-up →
  flat-top, §6.13's seated joint). Close: reverse over 500ms. The
  previously open block in a single-open stack closes in the same
  600ms, its drop recovering — two slips, one moment, like a fault
  system adjusting.
- **Choreography timeline (v2).** t+0 (activation): glyph begins
  rotating; fault line brightens `--joint` → `--ash` → t+0–600ms:
  body reveals, block drops 8px, ledge appears → t+600ms: open
  state; focus stays on the button. Close mirrors at 500ms.
- **State matrix (v2).** *Closed (rest):* header + fault line, block
  flush. *Opening/closing:* 600/500ms. *Open:* block dropped 8px,
  ledge visible, glyph flat-top, `aria-expanded="true"`. *Hover:*
  the fault line lifts to `--ash` and the glyph stirs 6° — the fault
  is live. *Focus:* hover treatment + focus ring on the button.
  *Scrolled-past:* state persists (an open fault stays slipped).
  *Disabled block (a section whose content is not yet surveyed):*
  its header is present without a button, its fault line lettered
  in apparatus "NOT YET SURVEYED" — present, honest, inoperable.
  Touch: identical, header target ≥48px.
- **Content merge.** The blocks are the stratum's own sub-sections;
  the fault lines are their boundaries, and the slip moves the
  block itself — content and mechanism are the same stone. Remove
  the content and the faults separate nothing.
- **Failure fallback.** Without JS, all blocks ship open (bodies in
  flow, blocks flush) — an accordion that hides content without JS
  is a gate failure (§10). The drop is JS/CSS enhancement on a fully
  printed stack.
- **Reduced-motion variant.** No drop, no reveal animation: bodies
  toggle instantly, the ledge and glyph state still change (state
  is not motion), so an open block is still visibly *the open one*
  by its ledge and apparatus.
- **Breakpoints (v2).** ≥1200px: drop 8px, reveal 600ms.
  768–1199px: drop 6px. <768px: drop 5px, reveal 500ms, header head
  at 22px.
- **Edge cases & failure modes (v2).** *Very long body:* the reveal
  is a grid-rows transition — it handles any height without the
  max-height hack and its lies. *Deep link to a closed block:* the
  target block opens instantly on load (no animation) and scrolls
  into view — a cited fault is found slipped. *Print:* all blocks
  print open and flush (print stylesheet forces it).
- **Accessibility spec (v2).** Real buttons, `aria-expanded`,
  `aria-controls`; body regions `role="region"` with
  `aria-labelledby`. Focus is never moved by opening. The drop never
  shifts the button itself (the button is in the header, the drop
  applies below the fault line… precisely: the transform applies to
  the block's body wrapper and ledge, the header row stays put — a
  focus target that moves 8px under the keyboard is a defect this
  spec forbids). Contrast: heads `--bone` ✓; apparatus `--ash-light`
  on `--basalt` 6.28:1 ✓.
- **Performance budget & mobile variant.** One grid-rows + one
  transform transition per toggle. Mobile: the 5px variant above.
- **Tokens consumed (v2).** `--joint`, `--ash`, `--wet`, `--bone`,
  `--ease-settle`, `--slip` (8px), `--fault-open` (600ms).

## 7. Page application map

| Page type | How the theme plays out |
|---|---|
| **Home** | The full cliff: rise (§6.1), snap (§6.2), fissure (§6.3), strata shear (§6.4), the organ pin (§6.5), the cross-section (§6.7), counters (§6.11), one calcite stratum holding the seam form (§6.15), bedrock (§6.9). Every signature appears once; nothing repeats. |
| **Listing** (outcrops / specimens / chapters) | No rise, no pin. A short cliff of two columns (index + filters as a strata panel, §11), then strata cards (§6.14) standing on their stratum; the fissure light (§6.10) still tracks depth. Empty results = the unquarried bay (§6.17) inside the grid. |
| **Detail** (one outcrop / specimen / section) | The subject as a single tall column: plate (§6.12) at its cap, figures as chiselled counters (§6.11), long detail in fault blocks (§6.18), the cross-section (§6.7) if the subject has a plan. Related items are §6.14 cards on the closing stratum. |
| **About / the survey** | The institution as strata of time: one stratum per era, counters for its real ages and counts, the calcite stratum ration spent here on the people (portraits as plates). No organ pin — an about page is read, not performed. |
| **Contact / request** | The seam form's page (§6.15): a short cliff, the calcite stratum near the top (the visitor came to join, not to descend first), fault blocks (§6.18) for the terms and the process. |
| **404 / empty** | The unquarried block (§6.17) alone on the cliff, bedrock below. The shortest page on the site and the most honest. |
| **Print** | The printed cliff: all columns standing, fissure at its static hairline, plan drawn, fault blocks open, ash absent. A page of this theme should print like a survey plate — check it (§10). |

## 8. Worked examples

### 8.1 The hero — a cliff is raised

*Setting: the home page of a geopark — "The Organ Cliffs".* t+0: the
page paints; in the DOM the cliff already stands — headline "Sixty
million winters, standing" in the front column, standfirst and CTA
below it, a plate of the organ in the organ-width column, figures in
the narrow column. JS (present, motion allowed) arms `.is-unrisen`
before the first frame is seen. t+300ms: the back column — the narrow
figure column, carrying "187,000,000 — YEARS SINCE THE FLOW" as
uncounted apparatus — begins its 2s uplift from 12vh. t+420ms: the
plate column rises from 16vh, its photograph settling (§6.12) as it
comes. t+540ms: the front column rises from 20vh, the headline's clip
splitting along its joint as it comes, letters fractured ±1px.
t≈+2.7s: the front column settles. t+2.85s: the **snap** — 90ms, the
fractures close, the headline is one stone face. The ash, which began
at t+800ms, is already falling through the finished cliff. The visitor
scrolls: the fissure in the front column begins to widen (§6.3), the
rust light strikes at the rail's top (§6.10), and the descent the
whole page is built for has begun. *Reduced motion / no-JS:* the same
cliff, standing, at t+0 — the example's every content item present,
only the raising unwitnessed.

### 8.2 Mid-page — the organ is played

*Setting: the home page's third stratum.* The visitor has descended
past the section plan (§6.7, drawn at their passing) and reaches
STRATUM III — THE ORGAN. The stage pins. Five pipes stand in their
stone frames, heights 62–92vh by the real proportions the captions
state. The caption rail reads the first caption — "PIPE I — THE
ELDEST. It cooled first and stands shortest; the survey counts it the
organ's foundation." — in full `--bone`; pipes II–V's captions wait
in `--bone-dim`, all present, all readable. As the visitor scrolls
the 150vh, pipe I's light (§6.5) completes its ramp; at the first
beat boundary caption I dims over 300ms, pipe II begins to brighten,
and the filing continues — one pipe, one caption, one idea, at the
visitor's own pace, reversible to the pixel if they scroll back. At
q=1 the stage releases; the organ, all five pipes lit in sequence
behind them, shears away at its far rate (§6.4) as STRATUM IV arrives
— the visitor has not watched a gallery; they have *played* one, at
reading speed, with their thumb as the organist's hand.

### 8.3 Conversion — a request is set in the seam

*Setting: the geopark's survey-request page.* The calcite stratum sits
high — the visitor came to ask, not to descend. The seam form (§6.15)
lies open between its stone edges: name, email, the outcrop in
question, the request. The visitor tabs to the email field: its border
cuts to `--basalt`, the rust tick draws at its left end (200ms). They
type an address missing its domain; on submit, the button thunks
(§11), and a fault note draws in beneath the field — crack glyph
first, then the sentence, in the fault voice: "This seam is open: the
address ends mid-word. Mend it and set the request again." Focus moves
to the field; nothing they typed elsewhere is lost. They mend it and
resubmit: fields fade (300ms), the two stone edges draw together
(800ms), and along the closed joint the confirmation is lettered:
"Set in the seam · Reference SEAM 214 · We answer within five working
days." The reference is a real record in the survey's system; the
five days are a real promise the office keeps, or — by the law of
§6.15 — neither would be printed.

## 9. Anti-slop — what makes THIS theme look cheap

1. **A spring anywhere.** One `cubic-bezier(0.34, 1.56, …)` and the
   stone turns to jelly; the whole theme is the refusal. *Cure:* the
   five named easings (§5) are the only curves on the page; the gate
   greps for others.
2. **Hexagon wallpaper.** Hexagons as a background pattern behind
   ordinary rectangular content — the theme's grid faked as décor.
   *Cure:* hexagons exist only as column caps, joints and the plan
   (§6.7). If a hexagon carries no content and marks no joint, it is
   deleted.
3. **Fast reveals "for polish".** 300ms fade-ups sprinkled on every
   section make the cliff feel like a template. *Cure:* entrances are
   rationed to the rise, the plan draw and the cap draws; everything
   else is scrubbed or still.
4. **Ash as snow.** Ash falling fast, thick or sideways reads as a
   Christmas effect. *Cure:* §6.6's caps — ≤40 motes, ≤16px/s,
   opacity ≤0.5, thinning with depth — are the difference between
   weather and a screensaver.
5. **Rust as a colour scheme.** Rust buttons, rust headings, rust
   links everywhere: the lit crack stops meaning anything. *Cure:*
   rust is light and line only (§2 law 3); its text-grade use is one
   named token in two named places (nav current, fault notes on dark).
6. **Uniform card grids.** Twelve identical cards in a 4×3 grid is a
   spreadsheet wearing a costume. *Cure:* §6.14's mixed spans and
   content-set heights; a listing row must look surveyed, not tiled.
7. **Invented figures.** A counter counting to a round, plausible,
   made-up age. *Cure:* §1's figure law — provenance in the caption
   (§6.11) or the figure is not printed.
8. **Parallax on everything.** If the footer, the nav and the form
   also drift, nothing is bedrock and the depth cue drowns. *Cure:*
   §6.4 applies to strata bodies only; §6.9's stillness is
   gate-checked by computed style.
9. **The fracture left on.** A headline still offset an hour after
   load (watchdog missing) is the theme's signature turned into a
   typo. *Cure:* §6.2's 4000ms watchdog is blocking-gated.
10. **Two calcite strata.** The pale layer spent twice reads as
    striping, and the form loses its human ground. *Cure:* one per
    page (§4), chosen for the page's most human content.
11. **A progress bar.** A thin rust bar across the top would say the
    same thing as §6.10 in a foreign language. *Cure:* refused in
    §11; the fissure of light or nothing.
12. **Geology words as flavour.** Copy that says "rock-solid
    solutions" and "groundbreaking platform" over a hosting dashboard
    is a costume on the wrong body. *Cure:* §1's fit test — if the
    subject is not heavy, old or load-bearing, this is the wrong
    theme, and no copy pass fixes that.

## 10. Quality gate

**Blocking (any failure = the theme may not ship):**

1. **Easing audit.** Grep the built CSS/JS: only the five §5 easings
   appear; the sole sub-600ms motion is §6.2's 90ms snap; no bounce,
   spring or overshoot curve exists anywhere.
2. **Watchdog test.** With the animation loop disabled, every armed
   element reaches its rest state by its watchdog (rise 1200/3600ms,
   snap 4000ms, plan 5000ms, plates 1200ms, veil 1200ms).
3. **No-JS test.** JavaScript disabled: the full page is readable —
   columns standing, headline aligned, plan drawn, fault blocks open,
   form submittable, footer complete.
4. **Figure-truth audit.** Every age, depth and count on the page
   traces to a stated source in its caption or colophon; invented
   figures = fail (§1).
5. **Bedrock test.** The footer's computed transform is `none` at
   five sampled scroll positions, and the footer contains no
   reveal/armed classes.
6. **Bleed test.** At maximum scroll velocity, no stratum edge or
   page ground is ever exposed by §6.4 (bleed ≥ max travel at every
   breakpoint).
7. **Contrast audit.** §2's laws verified in the build: no `--ash`
   text below 20px, no `--rust` text below 20px, fault notes on
   calcite set in `--basalt` (§6.15's pairing law).
8. **Ash cap test.** Mote count ≤40 (≤16 mobile), ash absent under
   reduced motion, ash paused on hidden tab.

**Standard (should pass; exceptions documented):**

9. One organ pin per page; one calcite stratum per page; pipes =
    captions, 4–6 each.
10. Every scrubbed value driven by the single shared loop at lerp
    0.08; no element runs its own rAF.
11. Reduced-motion pass: the still cliff is complete and loses no
    content, state or meaning.
12. Print pass: the page prints as a survey plate (§7).
13. The headline snap fires exactly once, 150ms after the rise
    settles, and never re-fractures.
14. Counters count once, from a true floor, at stated precision.
15. Five-second test: a first-time visitor can say, unprompted,
    "it's a cliff of stone columns, and it moves slowly" — if they
    say "dark website with hexagons", the grid has been faked (§9.2)
    and the build goes back.

## 11. Component inventory

Every component a real site in this theme needs, with its treatment.
Refusals are decisions, each with its in-theme replacement.

| Component | Basalt treatment |
|---|---|
| **Primary button** | A cut block: `--wet` face, 1px `--ash` edge, Fraunces 700 label. Magnetic pull toward the pointer capped at 6px, lerp 0.06 (the heaviest in the library — the button is *reluctantly* attracted), and on click the **thunk**: scale 0.97 over 120ms `--ease-fracture`-adjacent settle, release over 400ms `--ease-seep`. No pull or thunk under reduced motion or on touch. |
| **Secondary button / text link** | Apparatus text with a joint-draw underline (dashoffset, 300ms `--ease-settle`) on hover/focus; `--bone-dim` → `--bone`. |
| **Inputs** | §6.15's chiselled fields: inset hollow, apparatus label above, rust tick on focus. Never floating labels, never placeholder-as-label. |
| **Select** | **Refused.** A native dropdown is a foreign object mid-cliff. Replaced by a strata panel: the field opens a §6.18-style fault block listing the options as strata lines; the chosen line is lettered back into the field. (Where a true native select is unavoidable for a long list, it is styled as a chiselled field and the refusal is documented.) |
| **Checkbox / radio** | A small hexagon outline (18px) that fills `--rust` when set — the joint filled with ore. Target ≥44px via its label row. |
| **Tabs** | **Refused as tabs.** Replaced by **strata switches**: a row of joint-banded stratum names (§6.13's grammar); switching swaps the band below with the §6.16 veil at panel scale (300ms). |
| **Accordion** | §6.18 fault blocks. |
| **Cards** | §6.14 strata cards. |
| **Table** | A survey table: rows ruled by joint hairlines, figures tabular right-aligned, the header row a `--wet` stratum band with apparatus labels; row hover seeps §6.8's glow at 0.3 along the row's own hairline. No zebra striping — strata are not stripes (§9.10's cousin). |
| **Badge / chip** | A rust chip is permitted only as a *state marker* on a card's cap ("NOT STANDING", §6.14): apparatus text on `--wet`, never a coloured pill. Count badges are refused — counts belong in §6.11 figures or in prose. |
| **Alert / notice** | A **fault panel**: a `--wet` block ruled top and bottom by crack lines, its message in the §12 fault voice, `--rust-bright` apparatus head on dark grounds (on calcite, §6.15's pairing law applies). |
| **Toast** | **Refused.** Nothing on a cliff pops up and vanishes. Replaced by a **seam note**: a line lettered into the nearest joint band ("Set in the seam · Reference SEAM 214"), persistent until the visitor leaves the stratum. |
| **Modal** | **Refused as a floating box.** Replaced by the **opened fault**: a full-width stratum panel that slips down 8px (§6.18's grammar at page scale) between the current stratum and the next, holding the modal's content in flow, closed by its own fault line. Focus is trapped within it while open, by the same law as any dialog. |
| **Pagination** | "Deeper strata" — a single joint-banded link naming the next layer ("Stratum II of the index — 24 further columns"), never numbered page pills; numbered pagination implies the cliff was paginated, and it was surveyed instead. |
| **Progress bar** | **Refused** (§6.10 is the progress). Loading progress inside a stratum is the §6.16 veil. |
| **Spinner** | **Refused.** Waiting is shown by the ash veil (§6.16) or by a button's "Setting…" state (§6.15) — stone does not spin. |
| **Tooltip** | **Refused as a hover bubble.** Replaced by the **caption stone**: a small `--wet` block set into the joint beneath the term, present in flow on focus/tap, dismissed by moving on. Terms needing more than two lines get a fault block (§6.18), not a tooltip. |
| **Search** | The survey index: an input in the cap bar opening a full strata panel of results as §6.14 cards; zero results = the unquarried bay (§6.17) at panel scale. |
| **Breadcrumb** | The stratum path lettered in the joint band ("SURVEY / STRATUM II / THE ORGAN") — the joint bands already name where the visitor is (§4); a second breadcrumb system is refused as duplication. |
| **Hero** | §6.1 + §6.2 (the raised cliff). |
| **Navigation** | §6.13 column-joint navigation. |
| **Footer** | §6.9 bedrock. |
| **Loader / transition** | §6.16 ash veil + strata wipe. |
| **404 / empty** | §6.17 the unquarried block. |
| **Form** | §6.15 the seam form. |

## 12. Content & copywriting voice

The voice is the **surveyor's**: measured, declarative, unimpressed.
Sentences are short and load-bearing; every claim carries its figure
or its source. The theme has two registers — the **Stone** (headlines
and stratum statements: Fraunces, sentence case, the language of the
formation itself) and the **Apparatus** (labels, captions, data: the
surveyor measuring the stone) — and a third, the **Fault voice**, for
errors and failures, which states what is broken in the language of
fractures and how to mend it.

**Headline style (Stone).** Declarative, geological, no exclamation
marks, no questions as headlines. ✓ "Sixty million winters,
standing." ✓ "The flow cooled once. It has not moved since."
✗ "Discover our amazing rock-solid platform!" ✗ "Ready to take your
brand to groundbreaking new heights?"

**Labels (Apparatus).** Uppercase, tracked, factual, numbered where
the page is numbered. ✓ "STRATUM III — THE ORGAN" ✓ "PLATE IV — THE
ORGAN FROM THE NORTH" ✗ "Check this out" ✗ "Gallery vibes".

**Error voice (Fault).** Names the break, locates it, states the
mend; never blames the visitor, never jokes. ✓ "This seam is open:
the address ends mid-word. Mend it and set the request again."
✓ "The seam did not hold. Your words are kept above; try once more."
✗ "Oops! Something went wrong 😬" ✗ "Invalid input."

**Empty-state voice.** The survey records the absence; it does not
apologise for it. ✓ "Nothing stands here. The survey records no
column at this mark." ✓ "No columns have been surveyed in this
stratum yet. The next survey is in spring." ✗ "Nothing here… yet!
🎉" ✗ "No results found."

**Confirmation voice.** Set, referenced, promised — all three real.
✓ "Set in the seam · Reference SEAM 214 · We answer within five
working days." ✗ "Woohoo! You're in!"

**Banned words:** groundbreaking (unless the subject literally breaks
ground, stated as fact), rock-solid, seamless (the theme is made of
seams), cutting-edge, blazing, supercharge, delight, magic, "in
seconds" (nothing here is in seconds except the snap), exclamation
marks. **Owned words:** laid down, stratum, stands, in due course,
surveyed, set, mend, at rest, the record shows.

## 13. Full-page scroll choreography map

The home page, top to bedrock, in order. (Other page types omit their
absent beats; the order never changes.)

1. **The raising** (load): columns rise in depth order (§6.1); the
   headline's clip splits along its joint; ash begins at +800ms.
   *The visitor feels:* the site being built by its own subject.
2. **The snap** (+150ms after settle): the headline's fractures close
   in 90ms (§6.2). *Feels:* the one fast thing — a crack sealing.
3. **First scroll:** the fissure begins to widen in the hero column
   (§6.3); the rust light strikes at the rail's top (§6.10); the
   readout names STRATUM I (§6.13). *Feels:* descent has consequences.
4. **Strata shear:** bands begin sliding at their three rates
   (§6.4) as the hero leaves. *Feels:* the face is deep, not flat.
5. **The plan draws:** the cross-section surveys itself (§6.7) as
   its stratum crosses 55%. *Feels:* the page explains its own grid.
6. **The figures count:** chiselled numerals labour up to their true
   values (§6.11) in the geology stratum. *Feels:* scale, given time.
7. **The organ pins:** 150vh of filing — five pipes, five captions,
   light moving pipe to pipe (§6.5). *Feels:* reading as playing.
8. **Plates settle:** specimen photographs come to rest in their
   stone frames (§6.12) through the listing stratum; cards seep at
   the pointer (§6.8, §6.14). *Feels:* specimens being handled.
9. **The calcite stratum:** the page's one pale layer — the people,
   and the seam form (§6.15). *Feels:* the human layer, reached.
10. **The seam closes** (on submission): edges meet, the reference is
    lettered along the joint. *Feels:* being set into the record.
11. **The bedrock:** the rust rule draws across the footer's top —
    and then nothing moves, at all, for as long as the visitor stays
    (§6.9). The ash has thinned to its floor. *Feels:* arrival at the
    thing everything stands on. The page ends the way a descent
    should: at rest, on stone.

## 14. Whole-page performance budget

| Budget | Limit |
|---|---|
| Total page weight (home, first load) | ≤ 780KB (fonts ≤ 130KB subset variable Fraunces + Archivo; organ plates 5 × ≤90KB; other plates ≤ 60KB each; SVG plates/diagrams ≤ 40KB total; JS ≤ 55KB; CSS ≤ 45KB) |
| Animation frame budget | Shared loop ≤ 2.5ms/frame average while scrolling; ash adds ≤ 0.4ms at its 30fps idle cadence |
| Long tasks | None > 50ms after load; the letter-wrap (§6.2) and hex arming (§6.7) are one-time ≤ 8ms passes |
| Simultaneously animated properties | ≤ 14 (strata offsets ≤ 4, fissure 2, progress 1, plates ≤ 4, ash canvas 1, counters ≤ 1, misc ≤ 1) |
| Layout shift | CLS ≤ 0.02 — all geometry reserved (caps, plates, diagram) in markup |

**Cut order when the budget is exceeded** (cut in this order, never
skip ahead): 1) ash fall (§6.6) — halve motes, then remove; 2) the
near stratum rate (§6.4) — near becomes mid; 3) fissure-glow seep
(§6.8) — hover falls back to the border lift; 4) image settle scrub
(§6.12) — plates snap to 1.0 in the centre band instead of scrubbing;
5) strata parallax travel caps halved. **Never cut:** the rise's
watchdog and rest states, the fissure (§6.3), the progress light
(§6.10), the bedrock's stillness (§6.9), any reduced-motion variant,
any fallback. A Basalt page over budget gets quieter, never falser.

## 15. Build-order checklist

1. **Static cliff first.** Build the full page with no JS: columns
   standing, headline aligned, plan drawn, fault blocks open, form
   submittable, bedrock complete. This is the fallback and it must
   be shippable on its own.
2. **Tokens & type.** §2's palette (closed derived list), §3's scale
   and laws, the five §5 easings as custom properties.
3. **Grid & strata.** The column grid with caps and stagger (§4),
   strata with joint bands and names, the one calcite stratum, the
   bedrock.
4. **The shared loop.** One rAF loop, lerp 0.08, sleep/wake rules,
   the IntersectionObserver registry. Nothing animates before this
   exists.
5. **Scrubbed systems.** Fissure (§6.3), strata shear with bleed
   (§6.4), progress light (§6.10), image settle (§6.12) — in that
   order, each verified against its watchdog.
6. **The organ pin** (§6.5), with its no-pin mobile and reduced-motion
   layouts built as layouts, not as afterthoughts.
7. **Entrance ceremonies.** The rise (§6.1) with its arm-before-paint
   script and watchdogs; the snap (§6.2) wired to the rise's settle;
   the plan draw (§6.7); cap draws (§6.14).
8. **Counters** (§6.11) with provenance captions and the floor-arming
   rule (DOM ships final values).
9. **Interactions.** Fissure seep (§6.8), magnetic thunk buttons
   (§11), fault blocks (§6.18), strata switches and the opened fault
   (§11), the seam form (§6.15) with its fault voice and pairing law.
10. **Ambient.** Ash fall (§6.6) last of the systems — weather is
    added to a finished cliff — with its caps and pause rules.
11. **Transitions & veils** (§6.16), including the abort paths.
12. **Navigation & readout** (§6.13) scrollspy; verify anchors land
    clear of the cap bar.
13. **Reduced-motion pass.** Every element's variant, tested as a
    full page, not as a media-query afterthought.
14. **404 & empty states** (§6.17), including the past-tense build
    flag for fallen pages.
15. **Gate.** Run §10 in order — easing audit and figure-truth audit
    by a builder who did not write the page — then ship.
