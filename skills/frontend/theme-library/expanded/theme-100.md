# 100. The Velvet Note — Expanded (v1 + v2)

**Identity (preserved from the original entry, deepened — never
redesigned).** A 1920s jazz basement club that never had a website —
velvet, brass, cigarette-haze light and a band that tunes up as you
arrive. Not deco-poster pastiche: the *room itself*, low-lit and
close. Palette anchors: club dark `#0D0B09`, velvet curtain red
`#7E1E24`, muted brass `#C9A227`, smoke-lit cream `#E6DCC8`,
absinthe green `#31473B` (accent only). Type: Italiana (display —
thin, elegant, period) + Jost (body — geometric, Futura-era). The
page is a room, not a document: darkness first, one spotlight cone,
tables (sections) approached through haze layers at three depths;
the bandstand pins for the headline set while the evening's bill
changes beside it; progress is the set list by the door, its songs
checked off in pencil. The drinks list carries the house rule,
kept verbatim from the original entry: *"No requests after
midnight. The band knows what you need."*

## 1. Concept & world

The Velvet Note is a basement club in 1927 that has been handed a
website it never asked for. The site does not illustrate the club
with deco clip-art, saxophone silhouettes or gold-foil gradients;
it *admits* the visitor to the room. You come down the stairs
(the page loads in darkness), the house lights settle to club
level, one spotlight finds the bandstand, and the evening is
served to you the way the room serves it: a bill placed on your
table, a candle that brightens when you lean in, a card that
flips to RESERVED under a brass seal when the table is yours.
Reading the page is the night unfolding — first set, interlude,
second set, last orders — and the scroll position is quite
literally how far through the evening you are.

**The theme's one law: the dark is a dimmer, never a curtain.**
Darkness in this theme is a lighting state, not a hiding place.
Every element's lowest light state keeps its content fully
legible at the contrast floors in §2; the darkness overlay is a
lighting layer laid over a page that is *already completely
composed beneath it*, and it may thin, warm or travel — it may
never conceal. Two corollaries follow. First: **the house-lights-up
fallback is a designed state, not an error state** — if any part
of the lighting rig fails, the room simply puts its lights up
and the page reads as a plain, handsome, low-contrast-free
document. Second: **every number in the room is a real number** —
set times, the house count, table capacities, prices and the
reservation entry number all trace to data printed on the page
itself (§6.16, §6.15); the room never invents a figure for
atmosphere, because a club that lies about its bill is a club
nobody trusts twice.

**Best-fit sites and audiences.** Jazz clubs and live-music
venues whose product is the room as much as the music; cocktail
bars with a house band or a listening-room ethos; supper clubs;
vintage and period events (a 1920s wedding, a prohibition-era
fundraiser); small theatres and cabaret rooms; a record label's
roster page for a jazz catalogue, where each artist is a table
and each release a set. The audience is a night audience:
booking a table for Friday, checking who plays, reading a drinks
list by low light. The theme rewards businesses whose real
evening genuinely divides into sets, sittings and last orders —
the page's structure *is* that division, so a business without
an evening rhythm has nothing for the structure to carry.

**When NOT to use it.** Not for daytime businesses, family
venues, or anything that must read at a glance in bright
conditions — the room's authority depends on the visitor
accepting low light, and a children's party venue in club dark
is a category error. Not for high-density data (a festival's
400-act schedule, a ticketing marketplace) — the room seats
dozens, not thousands, and the set list by the door cannot
honestly list four hundred songs. Not for brands that need
photographic brightness: product photography dies in this light
(§6.13 rules the imagery treatment), so an e-commerce catalogue
belongs elsewhere. Not for accessibility-critical public services
whose users cannot be asked to read by candlelight at all — the
theme meets its contrast floors (§2), but its *mood* is a low
ceiling of light, and a benefits office should not have a mood.
And never as deco pastiche: if the design wants gold chevrons,
sunbursts and Gatsby lettering, it wants a poster, and this
theme is a room.

**The room's fixed geography.** Five places exist on every
Velvet Note page, in this order, and §13's choreography walks
them in sequence: **the stairs** (the load — house lights in
reverse, §6.1), **the door** (navigation and the set list,
§6.12, §6.9), **the bandstand** (the pinned hero, §6.11, lit by
the travelling spotlight, §6.2), **the tables** (the evening's
content sections, each with its candle, §6.7), and **the bar**
(the drinks list and the ledger, §6.14, §6.15), before **last
orders** close the night (§6.18). A page that reorders the room
— bar before bandstand, ledger before tables — has left the
theme, however dark its background is.

## 2. Palette

Five anchors from the original entry, seven derived tokens. Every
contrast figure below was **measured for this expansion** (WCAG
relative-luminance formula), not estimated. The room is a dark
theme only: there is no light mode, because a jazz basement at
noon is not the same club with the lights on — it is a different
business. The "bright" state of this theme is the
house-lights-up fallback (§6.1), which raises the *lighting*, not
the palette: surfaces stay club dark, and every text token
already passes on it.

| Token | Hex | Role | Usage ratio | Pairing & contrast (measured) |
|---|---|---|---|---|
| `--club` | `#0D0B09` | The room — page ground, every section's floor | ~62% | Ground for all text tokens below |
| `--velvet` | `#7E1E24` | Curtain red — bandstand curtain, table velvet, the reserved card's face | ~14% | On `--club` 1.96:1 — **surface only, never text, never a text ground at small sizes**; carries `--cream` at 7.36:1 |
| `--brass` | `#C9A227` | Muted brass — numerals, rules, the seal, rails, lit edges | ~9% | On `--club` 8.12:1 — text-grade; on `--velvet` 4.14:1 — large numerals (≥18px) only |
| `--cream` | `#E6DCC8` | Smoke-lit cream — all primary text, the bill card's face | ~9% | On `--club` 14.44:1; on `--velvet` 7.36:1; on `--velvet-deep` 9.78:1 |
| `--absinthe` | `#31473B` | Absinthe green — accent only: the one green thing in the room (a bottle, a door lamp, the available-table mark) | ≤2% | On `--club` 1.96:1 — **never text, never a sole indicator**; always paired with a word or a shape (§6.13) |
| `--club-deep` | `#060505` | Corridor black — dip-to-black transitions, the stairs before the dim | ~2% | `--cream` on it 14.96:1; used as a *held* colour, never a text ground mid-transition |
| `--velvet-deep` | `#5C151B` | Velvet in shadow — hover-deepened velvet, the curtain's fold side | ~2% | Carries `--cream` at 9.78:1 — the text-bearing velvet |
| `--brass-bright` | `#E4C566` | Brass catching light — glints, the spotlight's warm edge, the seal at the stamp instant | <1% | On `--club` 11.67:1; on `--velvet` 5.95:1 |
| `--candle` | `#E8B34B` | Candlelight — the candle glow's core, the flame's colour in every table candle | <1% | On `--club` 10.27:1; a light *source* colour — glows are drawn around it, text never sits on the glow |
| `--cream-dim` | `#B9AE97` | Cream at half light — secondary text, captions, the bill's small print | ~3% | On `--club` 8.95:1 — text-grade at all sizes |
| `--smoke` | `#8A8172` | Haze grey — the haze layers' body, hairlines in low light | ~2% | On `--club` 5.11:1 — captions and large text only; haze itself is drawn at low alpha over `--club` |
| `--pencil` | `#9A917E` | Pencil — the set list's check marks, hand-kept annotations, the ledger's ruled lines | <1% | On `--club` 6.29:1 — annotation-grade; never body text |

**Pairing rules (hard).** (1) Text is `--cream` or `--cream-dim`
on `--club` or `--velvet-deep`; `--brass` text is reserved for
numerals, labels in tracked capitals ≥11px, and the seal.
(2) `--velvet` and `--absinthe` are surfaces and signals, never
ink. (3) `--brass` on `--velvet` is permitted only for numerals
≥18px (4.14:1) — a price on the curtain, never a sentence.
(4) `--club` on `--brass` (8.12:1) is the seal's and the reserved
stamp's only reversed pairing. (5) The spotlight's light is
`--cream` warmed toward `--candle` — a radial gradient from
`#F4E9CF` at the cone's heart to transparent; it is a lighting
layer, and §6.2's contrast rule (text inside the cone is the
printed `--cream`, unchanged) means the cone never *creates*
legibility, it only directs attention. (6) Absinthe appears at
most twice on any page (the door lamp and the available mark,
§6.13) — a third green object breaks the room's colour story
and fails the gate's census (§10).

**Dark-mode behaviour.** The theme *is* the dark mode.
`prefers-color-scheme: light` does not invert it; instead the
build offers the house-lights-up state (§6.1) as the user's
manual override — a "house lights" control in the door (§6.12)
that lifts every lighting layer to its rest state and holds it,
persisted per visitor. Forced-colors mode: all glows, cones and
haze are removed, velvet and club map to Canvas, brass to
Highlight, and the page reads as its own fallback — tested as a
gate item (§10), because a room that cannot survive the lights
being put up by the *system* has broken the law in §1.

**The light budget.** Light is rationed like the room's
electricity: at any scroll position, exactly one spotlight cone
(§6.2), at most one brightened candle (§6.7), and the door lamp
may be lit. Everything else sits at rest light. A page where
three things glow at once reads as a fairground, not a basement
— the gate counts lit sources per viewport (§10).

## 3. Typography

Two faces, both period, neither a costume. **Italiana** — one
weight only (400), thin-stroked, wide and calm — carries the
club's name, headlines and the bill's headings; its single weight
is a discipline, not a limitation: emphasis in this room is done
with light and scale, never with bold. **Jost** (300/400/500)
carries everything else — body, labels, forms, the ledger — its
geometric letterforms are Futura's era and its tabular figures
keep the set times honest. Numerals are **always Jost**, never
Italiana: Italiana has no tabular figures, and a set time that
changes width as it counts is a drunk clock (§6.16).

| Role | Face / weight | Size (≥1200px) | Line-height | Tracking | Notes |
|---|---|---|---|---|---|
| Club name (sign) | Italiana 400 | 64px | 1.0 | +0.14em, uppercase | The warming sign (§6.4); per-letter spans, aria-label whole |
| Display (bandstand headline) | Italiana 400 | 54px | 1.08 | +0.06em | One line preferred; two lines maximum, second line smaller by design (§6.11) |
| Section heading (a set, a table) | Italiana 400 | 34px | 1.15 | +0.05em | Always preceded by its set number in brass Jost |
| Bill heading | Italiana 400 | 22px | 1.2 | +0.08em, uppercase | On the cream bill card, in club dark |
| Body | Jost 400 | 17px | 1.65 | 0 | `--cream`; measure 34–52ch — a basement measure, narrower than daylight's |
| Body small / standfirst | Jost 300 | 15px | 1.6 | +0.01em | `--cream-dim` permitted |
| Label / eyebrow | Jost 500 | 11px | 1.4 | +0.22em, uppercase | `--brass`; the room whispers its labels |
| Data (times, counts, prices) | Jost 500 | 15–28px by rank | 1.2 | +0.04em | `--brass` or `--candle`; tabular figures mandatory |
| Caption / fine print | Jost 300 | 12.5px | 1.55 | +0.01em | `--cream-dim`; the house rule (§6.14) sets here |
| Hand (pencil annotations) | Jost 400 italic | 13px | 1.5 | 0 | `--pencil`; the set list's checks and the ledger's marginalia — italic Jost stands in for the pencil; a script face is refused (§9) |

**Type laws.** (1) *Italiana never sets a sentence.* It names
things — the club, the sets, the acts — and the moment a headline
needs a verb, it is rewritten until it is a name again ("The
Marlowe Quartet", never "The Marlowe Quartet Plays Tonight").
(2) *No bold exists in this theme.* Jost 500 is the heaviest
stroke on the page; hierarchy is scale, light and position.
(3) *Letterspacing is the room's formality:* display +0.06em,
labels +0.22em, body 0 — a page that letterspaces its body text
has confused the club with a fashion house. (4) *Type never
dims.* Lighting layers move over type; the type itself is always
printed at full token contrast (the §1 law applied to ink).
(5) *The sign is the only kinetic type* (§6.4); headlines reveal
by light (§6.2), never by per-letter animation — one warming
sign per club.

**Scale at breakpoints.** ≥1200px as tabled. 768–1199px: sign
48px, display 42px, section 28px, body 16.5px. <768px: sign
36px, display 32px, section 25px, body 16px, bill heading 19px;
labels hold at 11px (they are already the floor). Line-heights
hold at every size — the room's air does not compress.

## 4. Layout language

**A room, not a page.** The layout is the club's floor plan read
top to bottom: stairs (load), door (nav + set list), bandstand
(pinned hero), tables (sections), bar (list + ledger), last
orders (footer). Sections are *tables in a room*: each sits in
its own pool of relative dark, separated not by rules or bands
but by **unlit floor** — 120–160px of bare `--club` between
tables at ≥1200px (88px at 768–1199, 64px below 768) — so
scrolling feels like walking between tables in the dark, and the
travelling spotlight (§6.2) has darkness to cross. Alternating
background bands are refused: the room has one floor.

**The bandstand and the rail.** The hero is a stage: a pinned
bandstand (§6.11) occupying 100vh (≥1200px) whose floor line —
a brass rail, 1px `--brass` at 55% with a worn highlight — sits
at 78% of the stage height. Content below the rail is the
audience (the bill, the standfirst); above it, the band (the
headline set). A fixed **margin rail** runs down the page's left
edge at ≥1200px: 72px wide, holding the set list by the door
(§6.9) and nothing else — the page's one persistent furniture.
Below 1200px the rail folds away and the set list becomes a
compact strip in the door (§6.9's breakpoints).

**Grid and measure.** Content column: max 1120px, centred, with
the reading measure inside it held to 34–52ch for prose; the
tables grid (§6.13) and the drinks list (§6.14) may use the full
1120px because lists are furniture, not prose. The bill card
(§6.3) is deliberately narrow — 340px, the size of a card a
waiter can carry — and sits at the bandstand's right, against
the rail. Asymmetry is the room's grammar: the bandstand is
centred (a stage is), the tables are not (a room isn't) —
sections alternate their candle side (§6.7) and their column
offset by ±48px at ≥1200px, a rhythm the eye reads as furniture
placement, never as a broken grid.

**Density and darkness ratios.** Per viewport at rest: ~62%
unlit floor (`--club`), ~14% velvet, ~9% brass-and-cream light
combined. A section that fills its viewport edge-to-edge with
cards has turned the club into a canteen; the tables grid caps
at 3 across (≥1200px) precisely so each table keeps dark around
it. Whitespace here is *darkness*, and it is spent like a
material: generously between tables, tightly inside them (a
table's own padding is 20–28px — people at a table sit close).

**Section choreography (the evening's running order).** Every
page follows the night: **Doors** (the bill + the count, §6.3,
§6.16) → **First set** (the primary content) → **Interlude**
(the trumpet line, §6.6 — exactly one per page, placed at the
page's midpoint) → **Second set** (secondary content, the
tables, the list) → **The ledger** (conversion, §6.15) →
**Last orders** (§6.18). A short page may drop the second set;
it may not move the interlude, duplicate it, or put the ledger
before the tables — a club that takes your money before you've
sat down has misunderstood its own evening (§13 maps the full
scroll).

## 5. Full motion system

Five named easings, defined once, used everywhere; an element
that invents a sixth fails the gate's grep. The room moves at
the speed of a band that is in no hurry: nothing in this theme
is faster than a stamp (140ms) except a glint, and nothing
ambient is faster than a breath.

| Easing token | Curve | Character | Used by |
|---|---|---|---|
| `--ease-dim` | `cubic-bezier(.6,.02,.3,1)` | House lights going down — a long, reluctant settle | House lights in reverse (§6.1), dip-to-black (§6.10), last-orders brightening (§6.18) |
| `--ease-swing` | `cubic-bezier(.45,.05,.35,1)` | Laid-back swing — behind the beat, arriving sure | Travelling spotlight (§6.2), candle brightening (§6.7), set-list checks (§6.9) |
| `--ease-glide` | `cubic-bezier(.22,.9,.28,1)` | A card placed on a table — low glide, soft stop, no bounce | The bill (§6.3), the door's menu (§6.12), the house note (§6.11's toast ruling in §11) |
| `--ease-stamp` | `cubic-bezier(.16,1,.3,1)` | The seal coming down — committed, instant, final | Reserved stamp (§6.8), ledger confirmation (§6.15), bookplate (§11) |
| `--ease-haze` | `cubic-bezier(.45,.02,.55,.98)` | Near-sinusoidal drift — smoke at smoke's speed | Haze layers (§6.5), velvet grain breath (§5), candle glow pulse (§6.7) |

**Durations ledger** (the theme's complete vocabulary; an
element may combine but not invent): house dim 1800ms; sign
warm-up 90–160ms per letter, irregular, ~1400ms total; spotlight
swing between bandstand positions 900ms; bill glide 620ms +
items at 70ms stagger; cone widen on the hero 1400ms; haze drift
38s / 57s / 84s by depth; trumpet line draw 2400ms; candle
brighten 450ms, deepen 600ms; card flip 520ms; seal stamp 140ms
press + 180ms settle; set-list check draw 300ms; door tally
count 1200ms; dip-to-black 300ms down, 300ms held dark, 500ms
up; tuning-up shimmer 1600ms cycle; last-orders brighten 1600ms;
watchdogs 2600ms (entrance), 3000ms (transitions and loader),
1200ms (reveals), 4000ms (pinned bandstand).

**The one shared loop.** Every scrubbed value in the room — the
spotlight's position, the cone's width, haze parallax offsets,
the bandstand's pin progress, the set list's position — is
driven by a single `requestAnimationFrame` loop lerping toward
scroll targets at **0.12** (the spotlight's swing eases its own
target at 0.09; a lighting desk does not snap). No scroll handler
writes a style. The loop sleeps when the tab is hidden and when
nothing is within 0.1px / 0.001 of its target; a page at rest
costs no frames. Time-based motion (haze drift, grain breath,
the candle's pulse) shares the same loop's clock — there is one
clock in the room, as there is one band.

**Every motion term, translated or refused.**
- *Scroll-triggered reveals* — sections are **lit**, not faded:
  a table enters the spotlight's path and its candle takes over
  (§6.7). The trigger is position; the reveal is illumination.
  Nothing fades up from below anywhere in the theme.
- *Scroll-scrubbed animation* — the travelling spotlight (§6.2),
  the bandstand's set change (§6.11), haze parallax (§6.5), the
  set list (§6.9): all scrubbed from the shared loop.
- *Parallax* — haze at three depths only: back wall 0.94×,
  mid-room 0.97×, near 1.0× with the content — atmosphere
  parallaxes, furniture does not. Capped ±26px, clamped so a
  haze edge never opens a seam at a section boundary.
- *Pinned sections* — exactly one: the bandstand (§6.11), for
  the headline set. A second pin is a second stage, and the
  club has one.
- *Masked reveals* — the spotlight cone is itself a soft clip
  mask widening over the hero (§6.11); elsewhere, masks are
  refused — light, not masks, does the revealing here.
- *Blur-to-sharp* — refused. Haze is a layer *between* the
  reader and the room, never a filter on the content; blurring
  the content itself would break the §1 law (the printed layer
  is never degraded). The single licensed blur is inside the
  haze layers' own rendering.
- *Kinetic typography* — the sign only (§6.4). One warming sign
  per club; headlines never move letter by letter.
- *Marquee* — refused. Nothing in a basement club scrolls
  sideways forever; the evening's acts are listed on the bill
  (§6.3), which stands still and is read.
- *Counters* — the door tally (§6.16) and the ledger's entry
  number (§6.15): brass Jost numerals, counted once, landing
  exactly on the printed figure.
- *Progress indicator* — the set list by the door (§6.9): songs
  checked in pencil. There is no progress *bar* in the room.
- *Ambient loops* — three licensed: haze drift (§6.5), the
  crushed-velvet grain breathing at 4% opacity over 9s, and one
  candle's glow pulse (§6.7) — and only while its table is in
  view. A fourth loop fails the gate.
- *Micro-interactions* — candle brighten (§6.7), brass rail
  glint on focus, the seal's stamp (§6.8): small, warm, and
  always answering a real action.
- *Hover physics* — pointer-tracked candle glow (§6.7) lerped
  at 0.18 in the shared loop; magnetic effects refused (a
  candle does not lean toward your hand; its light simply
  reaches you).
- *Page transitions* — dip-to-black (§6.10): the corridor
  between rooms.
- *Image treatment* — photography is admitted only as
  duotone-in-the-dark (§6.13): crushed blacks, cream highlights,
  never full colour — a colour photograph is daylight in the
  room.
- *Skeleton loading* — the band tuning up (§6.17): unlit shapes
  in low light, never grey daylight blocks.
- *Custom cursor* — refused, per the original entry and the
  standing rule. The normal system cursor; the room provides
  the atmosphere, the visitor keeps their own hand.

## 6. Signature elements

### 6.1 House lights in reverse

- **What & why.** The page opens the way the club opens: the
  world dims *down* into the room. A warm overlay at full
  daylight-neutral brightness settles over 1800ms to club level
  — lights going down in reverse, the evening beginning — and
  only then does the spotlight find the headline (§6.11). It
  belongs because arrival is the theme's first transaction: the
  visitor has come in from the street, and the page performs
  their eyes adjusting. Every later element happens inside the
  light this one sets.
- **Structure.** The page ships complete and fully composed in
  the DOM at club light — the printed room. JS alone inserts
  the dim layer: a fixed, `aria-hidden`, `pointer-events: none`
  overlay in a warm street-bright gradient (`#F2EAD6` at 92%
  over the room), whose opacity and warmth are custom properties
  (`--dim`, 1→0) driven from the shared loop. The layer sits
  above the room and below nothing interactive; it carries no
  content, no text, no logo — it is purely the street leaving.
  A `sessionStorage` flag records that this visitor has come
  down these stairs before.
- **Motion spec.** Trigger: load, once per session, gated on
  `document.fonts.ready` raced against 800ms (dimming over a
  fallback face would make the room lurch when Italiana lands).
  t=0: `--dim` at 1 (street-bright). 0–1800ms `--ease-dim`: the
  overlay thins and warms to nothing; at ~60% the room's own
  colours read true. At 1800ms the overlay is *removed from the
  DOM* — a lingering full-screen layer is a compositing cost
  and a lie about what the page is. The spotlight's first swing
  (§6.2) arms at 1500ms, overlapping the dim's tail by 300ms so
  the room never sits unlit and unmoving. Returning visitors
  (session flag set) skip the dim entirely: the room is simply
  lit, the way a regular walks in.
- **States.** Street-bright (JS-armed only, pre-dim) → dimming
  → club level (rest; overlay absent). Hover/focus: none — the
  dim is weather, not a control. Focus entering the page during
  the dim (a keyboard visitor tabbing in) completes the dim
  instantly: nobody is asked to wait in the stairwell. Scrolled
  during the dim: impossible to strand — the dim is
  time-based, not scroll-based, and completes on its own clock.
- **Content merge.** The dim reveals nothing and hides nothing;
  it changes the *light on the room's real first screen* — the
  bandstand, the bill, the door — which are all present beneath
  it from first paint. It is the page's own arrival, not an
  intro panel in front of the page.
- **Failure fallback.** Watchdog at 2600ms: if the dim has not
  completed (loop stalled, tab throttled), the overlay is
  removed and the room stands at club level. No JS: the overlay
  is never inserted; the page is simply the club, lit. Slow
  network: the room is HTML-first and fully readable before the
  dim script (deferred) even arrives. House-lights-up override
  (§6.12) skips the dim on every visit while it is on.
- **Reduced-motion variant.** No dim. The page opens at club
  level, steady — the original entry's rule: *steady low light*.
  The arrival is conveyed by the printed room alone.
- **Performance budget & mobile variant.** One fixed layer,
  opacity/gradient only, compositor-driven, removed at 1800ms;
  ≤2KB CSS. Mobile (<768px): identical, dim shortened to
  1400ms — a smaller room settles faster, and a phone visitor's
  patience is the budget that matters.
- **Choreography timeline (v2).** t=0 fonts ready (or the 800ms
  race lost → room ships lit, ceremony skipped) → t=0 `--dim`=1
  → t=0–1800 dim settles `--ease-dim` → t=1500 spotlight arms
  (§6.2) → t=1650 sign begins warming (§6.4) → t=1800 overlay
  removed → t=1900 bill glides in (§6.3). Watchdog ceiling
  2600ms cancels the overlay outright if the dim stalls.
- **State matrix (v2).** *Rest:* overlay absent, room lit.
  *Hover:* none. *Focus:* focus-in completes the dim instantly.
  *Active:* n/a. *Scrolled-past:* n/a (time-based).
  *Disabled / no-JS:* printed lit at first paint. *Touch:*
  identical; first touch completes a running dim (a hand on
  the rail — you are in).
- **Breakpoints (v2).** ≥1200px: dim 1800ms. 768–1199px:
  1600ms. <768px: 1400ms. The gradient and end-state are
  identical at every size — only the settle time breathes.
- **Edge cases & failure modes (v2).** *Tab hidden mid-dim:*
  rAF pauses; on return, wall-clock past 2600ms fires the
  watchdog and the overlay is removed. *Back/forward cache:*
  the page restores lit; the dim never replays from bfcache.
  *House-lights override on:* the dim is skipped entirely,
  every visit. *Fonts slow:* the 800ms race ships the room lit
  rather than dim in the wrong face.
- **Accessibility spec (v2).** The overlay is `aria-hidden` and
  never intercepts pointer or focus. The content beneath is in
  the accessibility tree, at full contrast, from first paint —
  contrast is the printed tokens' at all times (§2), because
  the overlay only ever *adds* street light above the room; it
  never darkens the printed layer below its rest state. The dim
  is never announced. A visitor with low vision is offered the
  house-lights control (§6.12) in the first tab order position
  after the skip link.
- **Tokens consumed (v2).** `--club`, `--cream`, `--ease-dim`,
  `--dur-dim` (1800ms), `--dur-watchdog-entrance` (2600ms).

### 6.2 The travelling spotlight

- **What & why.** One cone of warm light travels across the
  bandstand and down the room as the visitor scrolls, catching
  each section — each instrument, each table — in order, the
  way a lighting desk follows a set. It belongs because it is
  the theme's whole theory of attention made visible: in a dark
  room, what is lit is what is playing, and the reader's place
  in the evening is shown by where the light is. The cone is
  the original entry's centrepiece and the element every other
  element defers to — nothing else in the room is fully lit
  while the cone is elsewhere (§2's light budget).
- **Structure.** A fixed lighting layer (`aria-hidden`,
  `pointer-events: none`) holding one radial-gradient cone: an
  ellipse ~130% of viewport width at its widest, centred on a
  custom property pair (`--spot-x`, `--spot-y`) with its warmth
  `--spot-warm` (cream heart `#F4E9CF` → candle mid-tones →
  transparent), composited in `screen`-like soft light over the
  room but *under* nothing — the layer order is: printed room,
  haze (§6.5), cone, candle glows (§6.7). The cone never
  restyles content; it only lights the layer stack. Its target
  position is computed from scroll: each section registers its
  light position (the bandstand's three beats, then each
  table's candle point) and the shared loop swings the cone
  between them.
- **Motion spec.** Trigger: scroll, scrubbed, continuous. The
  cone's target is the light position of the section occupying
  the viewport's middle third; when the target changes, the
  cone swings 900ms `--ease-swing` (its target itself lerped at
  0.09 in the shared loop, so fast scrolling makes the cone
  *follow*, never teleport). Within the bandstand (§6.11) the
  cone is scrubbed directly across the headline set by pin
  progress — horn, piano, drums catch light in order. The
  cone's width breathes ±4% over 11s (`--ease-haze`) — a real
  beam in haze is never perfectly steady. Scrolling back up
  swings the light back: the desk follows the reader both ways,
  at the same 900ms, no favouritism.
- **States.** Rest (page still): cone parked on the current
  section's light point, breathing ±4%. In swing: cone in
  transit, sections at its edges at half light — designed, not
  a gap: half light in this room is still full contrast (§1),
  because the cone adds light, it never removes the printed
  layer's own. Scrolled-past sections return to rest light,
  which is club level, not darkness. Focus: keyboard focus
  moving to an off-cone element swings the cone to it (focus is
  a request for light). Disabled: no JS, no cone — the room at
  club level throughout.
- **Content merge.** The cone lights the page's *actual*
  sections in their actual order — the set list (§6.9) checks
  its songs by the cone's position, the bill (§6.3) is placed
  inside the cone's first resting place, and the trumpet line
  (§6.6) draws when the cone reaches the interlude. Remove the
  cone and the page still reads perfectly; keep it and the page
  is *conducted*.
- **Failure fallback.** Watchdog: if the shared loop stalls
  (no frame for 1200ms while a swing is pending), the cone
  layer is removed and the room stands at club level. No JS:
  the layer is never inserted. Low-power device (the loop's
  frame budget missed twice, §14): the cone parks permanently
  on the bandstand and the page continues as a lit room — the
  desk's operator has gone home, the house lights remain.
- **Reduced-motion variant.** No travelling cone. Each section
  carries its own steady pool of light (a static radial wash at
  its candle point, §6.7's rest state) — the original entry's
  *steady low light* ruling: the room is lit room by room, and
  nothing moves.
- **Performance budget & mobile variant.** One fixed gradient
  layer, transform/opacity only, no repaint of content; the
  gradient is rendered once and translated, never re-rasterised
  per frame (a build constraint, §15). Mobile (<768px): the
  cone narrows to 110% width, swings shorten to 700ms, and the
  breath is cut — a small room, a steadier beam.
- **Choreography timeline (v2).** Entrance: t=1500 (inside
  §6.1's dim tail) cone fades up parked on the headline →
  bandstand pin: cone scrubs horn→piano→drums across the pin →
  pin release: cone swings 900ms to the bill's table → each
  section boundary thereafter: 900ms swing to the next light
  point → interlude: cone rests on the staff line's start and
  follows its draw (§6.6) → ledger: cone parks on the form's
  seal point → footer: cone lifts and widens into the
  last-orders brighten (§6.18).
- **State matrix (v2).** *Rest:* parked, breathing. *Hover:*
  none (the cone does not follow the pointer — it follows the
  evening; pointer light is the candle's job, §6.7). *Focus:*
  swings to the focused element's section. *Active:* n/a.
  *Scrolled-past:* section returns to club level. *Disabled:*
  layer absent. *Touch:* identical — scroll is the input at
  every size.
- **Breakpoints (v2).** ≥1200px: cone 130% width, swing 900ms,
  light points at each section's candle. 768–1199px: 120%,
  800ms. <768px: 110%, 700ms, breath cut, light points at
  section headings (a phone's room is read from its titles).
- **Edge cases & failure modes (v2).** *Jump scroll* (anchor,
  scrollbar drag, find-in-page): the cone does not chase — it
  fades out at the old point and fades in at the new one over
  300ms; a swing across six sections would be a searchlight,
  not a follow spot. *Very long section:* the cone parks at
  its candle and waits; it never creeps. *Very short sections:*
  adjacent light points merge — the cone rests between them
  rather than flickering. *Resize mid-swing:* targets recompute
  on the next frame; the swing continues from the cone's
  current position.
- **Accessibility spec (v2).** Purely presentational:
  `aria-hidden`, no focus, no announcements. It never carries
  meaning alone — the set list (§6.9) states progress in text,
  the current section is `aria-current` in the door (§6.12),
  and every contrast floor is met by the printed layer without
  the cone (§2). Vestibular safety: the cone's motion is slow
  (900ms) and scroll-answerable, and it is wholly removed under
  reduced motion.
- **Tokens consumed (v2).** `--cream`, `--candle`, `--smoke`,
  `--ease-swing`, `--ease-haze`, `--dur-spot-swing` (900ms),
  `--loop-lerp` (0.12), `--spot-lerp` (0.09).

### 6.3 The bill placed on the table

- **What & why.** The evening's bill — tonight's acts, set
  times, the doors time — arrives the way a waiter serves it: a
  cream card gliding in low from the bandstand's edge and
  settling on the table with a soft stop, its items staggering
  in as if written down one by one. It belongs because it is
  the room's information manners made into motion: in this club
  nothing is *displayed*, things are *brought to you*. The bill
  is also the page's data anchor — its printed times and acts
  are the source the set list (§6.9), the tally (§6.16) and the
  ledger (§6.15) all read from.
- **Structure.** An `<aside>` card, 340px, `--cream` face,
  club-dark ink, slight physical tilt at rest (−0.6°, a card on
  a table is never squared to the room) straightening to 0° on
  hover/focus. Contents: the date line, acts with set times in
  tabular Jost, the doors time, and one line of the house's own
  small print. The card is real HTML in the DOM at the
  bandstand's right (§4) from first paint; JS arms only its
  entrance transform. Items are list items; the stagger is a
  per-item custom property (`--i`).
- **Motion spec.** Trigger: load, after the spotlight parks
  (t=1900 in §6.1's timeline). The card glides 620ms
  `--ease-glide` from 26px right and 8px low, rotating −2.2°→
  −0.6°, with its shadow growing as it lands (a card nearing a
  table throws more shadow). Items then fade-and-settle at
  70ms stagger, 260ms each `--ease-glide` — written down, one
  by one. On later visits in the session, the card is simply
  there: a regular's table already has its bill. The card never
  re-enters on scroll; it was placed once, at the start of the
  night.
- **States.** Rest: on the table, −0.6°, full contrast (cream
  on club is the room's brightest object, deliberately — the
  bill is meant to be read). Hover/focus-within: straightens to
  0° over 300ms `--ease-swing`, shadow lifts 2px — picked up.
  Active (a set time tapped): the item presses 120ms and the
  page scrolls to that set's section — the bill is a working
  index, not a poster. Scrolled-past: the card scrolls away
  with the bandstand; a compact echo of tonight's *next* set
  remains in the door (§6.12) so the information is never lost
  with the card.
- **Content merge.** The bill *is* the page's programme: its
  acts are the page's sections, its times are §6.16's tally
  source, its items link to their sets. It is not a decorative
  card near the content — it is the content's own table of
  contents, served.
- **Failure fallback.** Watchdog 1200ms: card snaps to rest
  (transform cleared) if the glide stalls. No JS: the card sits
  printed on the table from first paint — entrance transforms
  are JS-armed only. If the evening's data is missing (an
  unpublished night), the card prints "The bill is being
  written" in the house voice (§12) — an honest empty state,
  never a fabricated line-up.
- **Reduced-motion variant.** The card is present at rest, items
  printed, no glide, no stagger. Picked-up straightening on
  hover is also removed (a transform is motion).
- **Performance budget & mobile variant.** One card, transform
  + shadow only, ≤3KB CSS beyond the shared sheet. Mobile
  (<768px): the card goes full-width under the headline (a
  small table holds one card), tilt 0° (small screens forgive
  no rotation), glide shortens to 420ms vertical-only.
- **Choreography timeline (v2).** t=1900 card begins glide →
  t=2520 card lands, shadow settles → t=2560–3100 items settle
  at 70ms stagger → t=3200 the first set time's brass dot
  glints once (400ms) — the evening's first note. Session
  return visits: all beats skipped, card at rest.
- **State matrix (v2).** *Rest:* −0.6°, printed. *Hover:*
  straightens, shadow lifts. *Focus-within:* as hover, plus a
  brass outline on the focused item. *Active:* item press
  120ms → scroll to set. *Scrolled-past:* door echo (§6.12)
  carries the next set. *Disabled / no-JS:* printed at rest.
  *Touch:* no hover straighten; tap on an item acts directly.
- **Breakpoints (v2).** ≥1200px: 340px at the bandstand's
  right, −0.6°. 768–1199px: 300px, −0.4°, tucked under the
  rail. <768px: full-width, 0°, below the headline, glide
  420ms.
- **Edge cases & failure modes (v2).** *Long bill* (a festival
  night, 9+ acts): the card caps at 7 items with a printed
  "…and the late set, on the door" line linking to the full
  listing — a card a waiter can carry has a size, and the
  theme keeps it (§1's when-not-to-use covers true festivals).
  *One-act night:* the card prints the single act and the
  doors time; the stagger still runs, briefly. *Times change
  after print (a late band):* the card is data-driven — it
  reprints its items without re-running the entrance.
- **Accessibility spec (v2).** The card is a labelled `<aside>`
  ("Tonight's bill"); items are links with full text ("Second
  set — The Marlowe Quartet, 23:00"), never time-only. Contrast:
  club ink on `--cream` 14.44:1. The tilt is visual only; focus
  order follows the list. Touch targets: items ≥44px tall.
- **Tokens consumed (v2).** `--cream`, `--club`, `--brass`,
  `--candle`, `--ease-glide`, `--ease-swing`, `--dur-bill`
  (620ms), `--dur-item-stagger` (70ms).

### 6.4 Sign warming letter by letter

- **What & why.** The club's name — the page's `<h1>` in the
  door and the bandstand's sign — catches light letter by
  letter with slight irregular timing, like an old electric
  sign warming up: a letter flickers half-lit, holds, joins the
  word. It belongs because the name is the one piece of
  electricity the room is proud of, and its warm-up is the
  night officially starting. It is the theme's only kinetic
  type (§3 law 5) — the exclusivity is what makes it an event
  rather than a treatment.
- **Structure.** The name is one `<h1>` (or the door's wordmark,
  §6.12 — the same component at two sizes, never two warm-ups on
  one page: the bandstand sign is the one that warms; the door's
  mark is printed lit). JS splits the bandstand instance into
  per-letter spans (`aria-hidden`), keeping the whole name as
  the heading's accessible text via `aria-label`. Each letter
  carries a warm state driven by a custom property (`--lit`,
  0→1) colouring it from `--smoke` through `--candle` to
  `--brass-bright`, with a soft text-shadow glow that exists
  only while `--lit` is between 0.15 and 1 and is removed at
  rest (a permanent glow is a permanent compositing layer).
- **Motion spec.** Trigger: load, inside §6.1's timeline
  (t=1650), once per session. Letters warm left to right at
  irregular intervals — 90–160ms apart, seeded per letter from
  its index (deterministic: the same name warms the same way
  every night; randomness would make two builders' signs
  differ). Each letter: flicker phase 180ms (two dips to 40%
  `--lit`, `--ease-haze` steps) then a 320ms `--ease-swing`
  settle to full. Total for a 10-letter name ≈1400ms. One
  letter — the name's middle letter — warms *last* regardless
  of position on one night in seven (a deterministic
  date-seeded quirk, the sign's known faulty letter; §12's
  voice never mentions it — the regulars just know).
- **States.** Rest: fully lit, glow removed, letters at
  `--brass-bright` over the bandstand (on `--club` 11.67:1).
  Warming: transient only. Hover/focus: none — the sign is not
  a control. Scrolled-past: unchanged; the sign does not
  re-warm for anyone, ever, within a session.
- **Content merge.** The sign *is* the page's title and the
  business's name — the warm-up is the headline arriving, not a
  logo sting before it. The standfirst beneath waits for the
  final letter (its own entrance, §6.11, keys off the sign's
  completion, not a timer).
- **Failure fallback.** Watchdog at 2600ms shared with §6.1: any
  letter not yet lit is set to `--lit: 1` instantly. No JS: the
  name prints fully lit — the split and the warm states are
  JS-armed only; the DOM ships one whole, lit `<h1>`.
- **Reduced-motion variant.** The name prints lit. No flicker,
  no settle — a sign that is simply on.
- **Performance budget & mobile variant.** ≤12 letter spans,
  colour/shadow transitions only; the glow's text-shadow is
  dropped below 768px (small signs read by colour alone) and
  the warm-up shortens to 110ms per letter — the gesture at
  arm's length.
- **Choreography timeline (v2).** t=1650 first letter flickers
  → letters at +90–160ms irregular → flicker 180ms + settle
  320ms each → final letter ≈t=3050 → glow shadows removed at
  +200ms → §6.11's standfirst arms on completion. Watchdog
  2600ms forces any laggard lit (the ceremony yields to the
  evening).
- **State matrix (v2).** *Rest:* lit, no glow layer. *Hover:*
  none. *Focus:* none (not a control). *Active:* n/a.
  *Scrolled-past:* lit, unchanged. *Disabled / no-JS:* printed
  lit. *Touch:* identical; no touch interaction.
- **Breakpoints (v2).** ≥1200px: 64px, full glow during warm.
  768–1199px: 48px, glow at 60% blur radius. <768px: 36px, no
  text-shadow, warm 110ms/letter, flicker reduced to one dip —
  a small sign warms quicker and simpler.
- **Edge cases & failure modes (v2).** *Long names* (>16
  letters): the per-letter interval compresses to a 1200ms
  total budget — the evening may not wait for a long name.
  *Name edited in a CMS:* the split is programmatic on text
  content; spaces and punctuation are spans that never warm
  (they were never wired). *Italiana missing (font failure):*
  the 800ms font race in §6.1 ships the sign lit in the
  fallback face rather than warming in the wrong letterforms.
- **Accessibility spec (v2).** Screen readers get the whole name
  once, from the `<h1>`'s `aria-label`; the flicker is never
  announced and produces no live-region traffic. Photosensitivity:
  the flicker is two shallow dips (to 40%, never to black) at
  under 3Hz per letter — inside safe limits, and removed
  entirely under reduced motion. Contrast at rest 11.67:1;
  mid-warm letters are transient decoration over a name that is
  simultaneously available in the accessibility tree.
- **Tokens consumed (v2).** `--brass-bright`, `--candle`,
  `--smoke`, `--ease-haze`, `--ease-swing`, `--dur-letter-warm`
  (90–160ms), `--dur-watchdog-entrance` (2600ms).

### 6.5 Haze layers

- **What & why.** Cigarette-haze hangs in the room at three
  depths — against the back wall, mid-room, and near the
  reader — drifting slowly through the spotlight and
  parallaxing as the reader moves between tables. It belongs
  because depth in this theme is atmosphere, not geometry (§4):
  the haze is what makes a flat page feel like a low room with
  air in it. It is also the theme's licensed ambient life —
  with the velvet grain (§5) it is the only thing that moves
  when nobody is doing anything, and it moves at smoke's speed
  or not at all.
- **Structure.** Three fixed layers (`aria-hidden`,
  `pointer-events: none`), each a pair of large, soft radial
  gradients in `--smoke` at 5–9% alpha over transparent,
  rendered as background images on oversized (140% × 120%)
  divs so drift never exposes an edge. Layer order: back haze
  above the printed room, mid haze above back haze, the
  spotlight cone (§6.2) above both, near haze above the cone
  (smoke crosses the beam — that crossing is the whole effect)
  and below the candle glows (§6.7). No canvas, no WebGL, no
  per-particle anything: three gradients, translated. The haze
  never sits over a *reading line* at more than 9% alpha — the
  §1 law in atmospheric form: haze may cross the room, it may
  not settle on the page's text.
- **Motion spec.** Two motions share the layers. *Drift*
  (time-based): back layer translates ±18px over 84s, mid ±26px
  over 57s, near ±34px over 38s, all `--ease-haze`, alternate
  direction, forever — periods chosen co-prime so the three
  never sync into a visible loop point. *Parallax* (scroll,
  shared loop): back 0.94×, mid 0.97×, near 1.0× — the room's
  air lags the room. Drift amplitude halves while the spotlight
  is mid-swing (§6.2) — smoke in a moving beam is stirred, and
  the stir is shown by *less* drift, oddly, because the eye is
  following the light.
- **States.** Rest: drifting, parallaxing. In the spotlight's
  path: the near layer brightens locally (its gradient is
  warmed by the cone layer beneath it — a composite effect, no
  extra code). Scrolled-past / any state: unchanged — haze has
  no per-section states; it is the room's weather, indifferent
  to the programme. Disabled: layers absent; the room is clear
  air, which is also a true state of the club (early, before
  the first set).
- **Content merge.** The haze is the medium the spotlight and
  candles shine *through* — remove it and §6.2's cone has
  nothing to be visible in, §6.7's glow has nothing to bloom
  into. It carries no content and covers none: at 9% alpha over
  `--club`, printed `--cream` text beneath it still measures
  above 12:1 effective contrast.
- **Failure fallback.** The layers are pure decoration with a
  delete key: if the shared loop stalls, they freeze (a still
  room is a fine room); if gradients are unsupported, they
  simply don't render. No watchdog is needed because nothing
  depends on them — the fallback *is* their absence, and no JS
  means no layers at all.
- **Reduced-motion variant.** All three layers removed. The
  room's depth is then carried by the printed pools of light
  (§6.2's variant) alone — the original entry's *no haze drift*
  ruling, taken one step further: no haze at all, because a
  static smoke layer reads as dirt on the screen.
- **Performance budget & mobile variant.** Three gradient
  layers, transform-only animation, no repaints (gradients are
  pre-rendered at 1.5× and translated). Budget: ≤6KB CSS, zero
  JS beyond the shared loop. Mobile (<768px): two layers (back
  + near), drift periods lengthened ×1.5, parallax capped
  ±14px — a phone's room is smaller and its battery is the
  house's electricity bill.
- **Choreography timeline (v2).** Continuous from t=0: drift
  cycles 84s/57s/38s running from load (offset per layer so the
  room is never caught at a sync point) → parallax bound to
  scroll throughout → drift halves during each spotlight swing
  (900ms) → at last orders (§6.18) all drift slows ×2 over
  1600ms as the room empties. No completion beat: haze does not
  finish.
- **State matrix (v2).** *Rest:* drifting. *Hover:* none.
  *Focus:* none. *Active:* n/a. *Scrolled-past:* parallax only.
  *Disabled / no-JS:* absent. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: 3 layers, drift as specced,
  parallax ±26px. 768–1199px: 3 layers, drift amplitude ×0.8,
  parallax ±20px. <768px: 2 layers, drift ×1.5 period,
  parallax ±14px.
- **Edge cases & failure modes (v2).** *Long pages:* the layers
  are fixed, so length costs nothing. *Overscroll (rubber-band):*
  parallax clamps at the page ends — haze never tears away from
  the room's edges. *High-contrast / forced-colors:* layers
  removed (§2). *A visitor who finds haze reads as fog on a
  dirty screen:* the house-lights override (§6.12) removes the
  layers too — the override is a full lighting reset, not a
  dimmer tweak.
- **Accessibility spec (v2).** `aria-hidden`, unfocusable, no
  meaning. The 9% alpha ceiling over text is a *contrast* spec,
  verified at the gate (§10) by sampling effective contrast of
  body text under the near layer at its densest point: must
  remain ≥7:1. Motion sensitivity: drift is slow (≤34px over
  38s ≈ 0.9px/s) and removed under reduced motion.
- **Tokens consumed (v2).** `--smoke`, `--club`, `--ease-haze`,
  `--dur-haze-back` (84s), `--dur-haze-mid` (57s),
  `--dur-haze-near` (38s), `--loop-lerp` (0.12).

### 6.6 Trumpet line interlude

- **What & why.** At the page's midpoint — the interlude
  between sets — a trumpet's melodic line draws itself as a
  single golden staff line across the section: an SVG path that
  rises, hesitates, and lands, the solo made visible. It is the
  page's only notation, placed like a solo: one instrument,
  once, in the quiet between the sets. It belongs because every
  evening has a moment where the room stops talking and listens,
  and the page needs exactly one moment that is *only* music —
  no act to book, no table to sell, just the line.
- **Structure.** One inline SVG, full content-column width,
  120px tall: a single path (the melody) in `--brass` 2px with
  a `--brass-bright` core, over five hairline staff rules in
  `--smoke` at 30%. The path is drawn with
  `stroke-dasharray/offset` from the shared loop's clock. The
  section around it carries the interlude's real content — the
  interval drinks note, the second set's standfirst (§8's
  worked example) — set *beneath* the staff, so the line plays
  over the room's actual pause. The completed path is printed
  in the DOM as a full stroke: the dash treatment is JS-armed
  only.
- **Motion spec.** Trigger: the section's top crossing 65% of
  the viewport, once. Draw: 2400ms `--ease-swing`, the path's
  tempo following its own shape — fast over the rising run,
  slow over the held note (implemented as path-length easing
  segments, not a linear dash: the draw's speed is the
  melody's). The spotlight (§6.2) rests at the line's start and
  follows the draw head. At completion, one small brass note
  head — the final note — settles onto the line's end with a
  180ms `--ease-stamp` press. The line never redraws; a solo is
  not repeated because you scrolled back.
- **States.** Rest (pre-trigger): staff rules printed, the
  melody path present but un-drawn — visually, the staff waits
  empty, which is itself a true picture of an interlude not yet
  begun. Drawing: transient. Complete: the full line, printed,
  permanent for the session. Scrolled-past and returned: the
  line stands complete. Focus: the section is reachable and
  readable throughout; the draw is never a gate on its text.
- **Content merge.** The line is drawn *through* the interlude
  section's real content block — its caption names the soloist
  and the tune from the bill (§6.3's data), and the section's
  text is the interval's actual information. It is the page's
  ornament exactly once, and it ornaments the room's own pause,
  not a gap in the layout.
- **Failure fallback.** Watchdog 1200ms after trigger: if the
  draw has not started or stalls, the dash is cleared and the
  line stands printed whole. No JS: the line is printed whole
  from first paint. If the bill names no soloist (a night
  without an interlude act), the section and its line are
  omitted entirely — the theme never draws a solo nobody
  played.
- **Reduced-motion variant.** The line stands printed whole; no
  draw, no following spotlight (the cone parks at the section,
  per §6.2's variant).
- **Performance budget & mobile variant.** One SVG path, dash
  animation on the compositor where possible; ≤4KB. Mobile
  (<768px): the staff shortens to 72px tall, draw 1800ms, the
  note-head settle kept (it is the section's full stop).
- **Choreography timeline (v2).** Section top at 65% viewport →
  t=0 spotlight arrives at line start (900ms swing, §6.2) →
  t=200 draw begins → t=200–2600 draw at the melody's own tempo
  → t=2600 final note settles (180ms `--ease-stamp`) → t=2900
  the second set's heading candle arms (§6.7). Watchdog 1200ms
  from trigger covers a draw that never begins.
- **State matrix (v2).** *Rest:* staff empty, line un-drawn.
  *Hover:* none. *Focus:* none on the line itself; the
  section's links behave normally. *Active:* n/a.
  *Scrolled-past:* line complete. *Disabled / no-JS:* line
  printed whole. *Touch:* identical; trigger is scroll
  position.
- **Breakpoints (v2).** ≥1200px: 120px staff, draw 2400ms.
  768–1199px: 96px, 2200ms. <768px: 72px, 1800ms, staff rules
  reduce to three (a small staff is a child's copybook — three
  lines keep it a sketch, five at small size is a grid).
- **Edge cases & failure modes (v2).** *Path edited (a
  different soloist's line per night):* the draw is
  path-length-generic; any single-path melody works, and the
  tempo segments are proportional, not absolute. *Section
  near the page foot (short page):* the 65% trigger still
  fires on load if already met — the solo plays as the room
  opens, which the choreography accepts (§13). *Two interludes
  in data:* refused at build — §4's running order allows one;
  a second solo section uses the tables treatment instead.
- **Accessibility spec (v2).** The SVG is `role="img"` with a
  text alternative naming what it is ("The interlude solo,
  drawn as a single line — Marlowe's trumpet, 'Blue Hour'"),
  sourced from the same bill data as its caption. The draw is
  never announced live. Contrast: `--brass` on `--club` 8.12:1
  for the line; the staff rules are decoration and exempt, but
  sit at 30% `--smoke` so they never compete with text.
- **Tokens consumed (v2).** `--brass`, `--brass-bright`,
  `--smoke`, `--ease-swing`, `--ease-stamp`, `--dur-solo`
  (2400ms), `--dur-watchdog-reveal` (1200ms).

### 6.7 Candle-brightening hover

- **What & why.** Every table (section) in the room has a
  candle — a small warm glow at its corner. Leaning in
  (hover, focus, or the section arriving at reading position)
  brightens its candle: the glow grows, the velvet behind the
  section deepens, and the table feels attended. It belongs
  because it is the theme's unit of attention: in a dark room
  you do not highlight a thing, you bring a candle closer to
  it. It is also the theme's scroll-reveal — a section is
  *lit by its own candle* as it takes the reader's attention,
  which is how the room avoids both fade-ups and pop-ins.
- **Structure.** Each section carries a candle component: a
  10px `--candle` core dot with two radial glow shells (36px
  and 84px, `--candle` at 14% and 5%), positioned at the
  section heading's side (alternating per §4), plus a
  velvet-deepening layer behind the section's surface
  (`--velvet` → `--velvet-deep` blend driven by the same
  property). One custom property, `--lean` (0→1), drives glow
  scale, glow alpha, and velvet depth together, lerped at 0.18
  in the shared loop toward a target set by hover, focus, or
  the section's scroll position. The candle is `aria-hidden`;
  the section's heading is its accessible name.
- **Motion spec.** Brighten: 450ms `--ease-swing` (driven by
  the `--lean` lerp, so it is interruptible mid-glow without a
  jump). Deepen (on leave): 600ms — the room lets go slower
  than it leans in. Scroll- triggered: as a section's heading
  crosses the viewport's middle third, its candle takes `--lean`
  to 0.7 (attended, not leaned-on); hover/focus raises it to
  1.0. At rest in view, the candle's glow pulses ±6% over 7s
  (`--ease-haze`) — a flame is alive, but barely: the pulse is
  the theme's third licensed ambient loop (§5) and it runs only
  for the candle currently attended.
- **States.** *Rest (out of view):* `--lean` 0, glow at ember
  (core lit, shells at 30%) — a candle in this room is never
  fully out. *Attended (in reading position):* 0.7. *Leaned
  (hover/focus):* 1.0, velvet fully deepened. *Scrolled-past:*
  returns to ember over 600ms as the next table's candle takes
  over — §2's light budget enforced by the loop: only one
  candle above 0.7 at a time; a new lean steals the light
  politely, the old candle deepening as the new one brightens.
- **Content merge.** The candle sits on the section's own
  heading furniture and its light falls on the section's own
  content; the velvet it deepens is the section's own surface.
  It is not a decoration near the content — it is the content's
  lamp, and the section's readability rhythm (ember → attended
  → leaned) *is* the page's reading rhythm.
- **Failure fallback.** No JS: candles print at attended level
  (0.7 glow, static) — every table evenly lit, the room at its
  printed state. Loop stall: candles freeze at current `--lean`;
  nothing is hidden at any value of `--lean`, because the glow
  only adds light (§1). Watchdog is unnecessary by construction
  and the spec says so — a fallback that cannot fail does not
  get a timer.
- **Reduced-motion variant.** Candles print at attended level,
  static; hover/focus change nothing (no brighten, no deepen) —
  focus is shown by the brass outline alone (§11). The flame
  pulse is removed.
- **Performance budget & mobile variant.** Per candle: one dot
  + two gradient shells, transform/opacity only; a page caps
  at 8 candles (a room with more tables than that is a hall).
  Mobile (<768px): no hover exists — candles go to attended
  (0.7) on scroll position only, glow shells shrink to 28/64px,
  and the pulse is cut (battery, and a flame you cannot lean
  toward should not flicker for attention).
- **Choreography timeline (v2).** Heading crosses middle third
  → `--lean` target 0.7, reached ≈450ms → hover/focus: target
  1.0 ≈450ms → leave: target back to scroll state, 600ms →
  section exits middle third: target 0, ember at ≈600ms, next
  candle's rise overlapping by the loop's single-light rule.
- **State matrix (v2).** *Rest:* ember. *Hover:* leaned 1.0.
  *Focus:* leaned 1.0 (keyboard attention is attention).
  *Active:* n/a. *Scrolled-past:* ember. *Disabled / no-JS:*
  attended 0.7 static. *Touch:* scroll-attended only; a tap on
  the heading's controls does not lean the candle (the tap has
  its own feedback).
- **Breakpoints (v2).** ≥1200px: shells 36/84px, candle at the
  heading's outer side, alternating. 768–1199px: shells 32/72px.
  <768px: shells 28/64px, candle always at the heading's left
  (alternation needs width to read as furniture placement; in a
  narrow room it reads as inconsistency).
- **Edge cases & failure modes (v2).** *Two sections in the
  middle third at once (short sections):* the higher one holds
  the light; the loop's single-light rule arbitrates, no
  flicker — targets change only when the leader changes by a
  full heading height. *Section taller than the viewport:* its
  candle stays attended for its whole travel — a long set keeps
  its light. *Candle count over cap:* sections beyond the
  eighth share the last candle's treatment statically (printed
  attended, no loop binding).
- **Accessibility spec (v2).** The candle is decoration
  (`aria-hidden`); attention is never *only* candlelight — the
  current section is marked in the door and set list (§6.9,
  §6.12) in text. Focus-visible is a brass outline, not the
  glow. The glow never reduces contrast: it adds `--candle`
  light behind headings whose text is `--cream` on `--club`
  (14.44:1) at every `--lean` value, since the shells peak at
  14% alpha.
- **Tokens consumed (v2).** `--candle`, `--velvet`,
  `--velvet-deep`, `--ease-swing`, `--ease-haze`, `--dur-lean`
  (450ms), `--dur-release` (600ms), `--loop-lerp` (0.12).

### 6.8 Reserved-card click

- **What & why.** A table's card, clicked, flips over to its
  reserved face — deep velvet, the word RESERVED in cream, and
  the house seal stamped in brass at the flip's end. It is the
  room's booking ritual compressed into one gesture: a card, a
  seal, a table kept. It belongs because conversion in this
  theme is never a cart or a checkout — it is the house keeping
  a table for you, and the flip makes that promise physical:
  the card you were reading is now the card that waits for you.
- **Structure.** A `<button>`-wrapped card (§6.13 supplies the
  grid it lives in) with two faces in a 3D flip container: the
  front (the table's facts — its name, seats, position, its
  candle §6.7) and the back (`--velvet-deep` face, RESERVED in
  Italiana, the reservation's printed details, and the seal —
  an inline SVG roundel: the club's initials in a brass ring,
  club-dark on brass at the stamp instant, settling to brass
  line on velvet). State lives in `aria-pressed` and a
  `data-state` attribute; the flip is a `rotateY` on the inner
  container. A reservation made here is *held*, not paid: the
  card's back prints "Held until 21:30 — the ledger (§6.15)
  confirms", keeping the ritual honest about what a click does.
- **Motion spec.** Trigger: click / Enter / Space. Flip: 520ms
  `--ease-swing` `rotateY` 0→180°, the card lifting 6px at
  mid-flip (a card picked up turns easier). At 470ms — the back
  face nearly flat — the seal stamps: scale 1.6→1 in 140ms
  `--ease-stamp` with a 1px brass shock ring expanding and
  fading over 300ms; the stamp is the gesture's full stop.
  Un-reserving (click again) flips back at 420ms with no stamp
  — the house does not make a ceremony of letting go. Focus is
  held on the card throughout; the flip never moves focus.
- **States.** *Front / available:* facts face, absinthe mark lit
  (§6.13) if the table is free tonight. *Front / held by
  another:* the card prints "Kept" in pencil and does not flip
  — disabled, with the reason in text, not just grey. *Back /
  reserved:* seal stamped, details printed, the candle (§6.7)
  at attended. *Pending (the hold request in flight):* the flip
  pauses at 90° — card edge-on, a held breath — for at most
  1200ms, then completes or falls back to the front with the
  house note (§11) explaining.
- **Content merge.** The card being flipped is the table's own
  listing entry — its facts on the front, its reservation on
  the back; nothing is decorated, the object *is* the
  transaction. The seal it stamps is the same seal the ledger
  (§6.15) uses to confirm, so the two ends of the booking tell
  one story.
- **Failure fallback.** If the hold fails (network, a race for
  the last table), the card returns to its front over 420ms and
  the house note (§11) says so in the house voice ("That table
  was kept a breath before yours — the bar rail is open, or
  §6.15's ledger can write to the house"). No JS: the card is a
  link to the ledger with the table pre-chosen — the flip is an
  enhancement of a working booking path, never the path itself.
  Watchdog: a flip that has not settled in 1200ms is snapped to
  its target face, seal included or omitted by state.
- **Reduced-motion variant.** No flip, no stamp animation: the
  card cross-fades 120ms between faces (a state change, plainly
  shown), the seal present at rest on the back. `aria-pressed`
  carries the state as before.
- **Performance budget & mobile variant.** One 3D transform per
  card, `will-change` only during the flip; the seal is a
  static SVG ≤2KB. Mobile (<768px): the flip becomes a vertical
  turn (`rotateX`) — a card on a narrow table turns toward you,
  not sideways into the next table — and the lift is cut.
- **Choreography timeline (v2).** t=0 click → t=0–520 flip,
  lift peaking t=260 → t=470 seal stamps (140ms press) →
  t=610 shock ring fades → t=650 the card's candle takes
  attended (§6.7) → the door tally's held count (§6.16)
  reprints from the DOM's real reserved states.
- **State matrix (v2).** *Rest:* front, facts. *Hover:* candle
  leans (§6.7), card shadow warms 2px. *Focus:* brass outline,
  candle leans. *Active (press):* card dips 1px at 90ms.
  *Scrolled-past:* state persists (a reserved table stays
  reserved). *Disabled:* "Kept" tables — no flip, reason
  printed. *Touch:* tap flips; no hover states are required to
  understand the card.
- **Breakpoints (v2).** ≥1200px: `rotateY` flip, 520ms, lift
  6px. 768–1199px: `rotateY`, 480ms, lift 4px. <768px:
  `rotateX`, 440ms, no lift, seal at 80% size.
- **Edge cases & failure modes (v2).** *Double-click / impatient
  visitor:* the second click queues until the flip settles —
  the card never reverses mid-air. *Two visitors, one table:*
  the pending state's 1200ms ceiling, then the honest fallback
  above. *Reserved, then the page is left and returned:*
  session state restores the card's back — the house remembers
  within the evening (sessionStorage), and says so ("Held for
  you since 20:14").
- **Accessibility spec (v2).** A real `<button>` semantics via
  `aria-pressed` on the card's control, labelled with table and
  state ("Table 4, by the bandstand, seats four — reserve").
  The flip is visual; the state change is announced by a polite
  live region ("Table 4 is kept for you"). Contrast: cream on
  `--velvet-deep` 9.78:1 on the back; the seal's brass on velvet
  is decoration around text, never the text itself. Target:
  the whole card, ≥64px in its smallest dimension.
- **Tokens consumed (v2).** `--velvet-deep`, `--velvet`,
  `--cream`, `--brass`, `--brass-bright`, `--absinthe`,
  `--ease-swing`, `--ease-stamp`, `--dur-flip` (520ms),
  `--dur-stamp` (140ms).

### 6.9 Set-list progress

- **What & why.** By the door hangs the evening's set list —
  the acts and songs in running order — and as the visitor
  passes each section of the page, its song is checked off in
  pencil. Progress in this room is not a bar filling; it is the
  evening unfolding, kept by hand by someone at the door. It
  belongs because it makes the page's length *mean* something:
  you are as far through the page as the band is through the
  night, and the last check, at the footer, is last orders
  itself.
- **Structure.** A `<nav>`-adjacent `<ol>` in the left margin
  rail (§4) at ≥1200px: the evening's items (from the bill's
  data, §6.3 — one source), each a row: set number in brass,
  the act/song name in Jost, and a check space at the row's
  right. The check is a small SVG path (a pencil tick, slightly
  irregular — two strokes, the second shorter) in `--pencil`,
  drawn by dash-offset when its section passes. The current
  item carries a candle dot (§6.7's ember, reused at 8px).
  Below 1200px the list folds into the door (§6.12) as a
  compact strip: "Second set · 3 of 5" in text with a pencil
  underline that grows by item.
- **Motion spec.** Trigger: a section's heading crossing the
  viewport's upper third (the song has *started*). The tick
  draws in 300ms `--ease-swing` — a hand checking a list is
  quick and unceremonious. The current item's name warms from
  `--cream-dim` to `--cream` over 450ms as its candle dot takes
  ember. Scrolling back up un-checks nothing: the evening does
  not unhappen — but the *current* marker retreats honestly to
  the item the reader has returned to. (The checks record the
  furthest reach of the night; the candle records the present.)
- **States.** *Upcoming:* name at `--cream-dim`, check space
  empty. *Current:* name lit, candle dot at ember, no check
  yet (the song is playing). *Played:* pencil check drawn,
  name at full `--cream` with the check beside it. *The last
  item (last orders):* its check is drawn by §6.18 as the
  footer arrives — the only check drawn by a different element,
  and §13's map says so.
- **Content merge.** The list is the page's own sections in
  their own order, named by the bill's data — it is a table of
  contents that behaves like an evening. Its items are links:
  clicking one takes you to that set (the room lets you skip a
  song; the pencil will catch up).
- **Failure fallback.** No JS: the list prints as a plain table
  of contents, all items at full contrast, no checks — a set
  list on a night when nobody is keeping score. Loop stall:
  checks freeze; the current marker is also printed as text
  ("You are here" in the compact strip's wording, §12), so
  progress is never *only* a drawing.
- **Reduced-motion variant.** Checks appear whole (no draw),
  the current item marked by its candle dot and text; nothing
  animates.
- **Performance budget & mobile variant.** ≤9 rows, one small
  SVG path each, dash animation only. Mobile (<768px): the
  rail is gone; the door strip (§6.12) carries progress as
  text + growing pencil underline (a single 2px div, width by
  the shared loop) — the full list lives in the door's opened
  menu for anyone who wants the evening whole.
- **Choreography timeline (v2).** Section heading crosses upper
  third → previous item's tick draws (300ms) as the new item
  warms (450ms) and takes the candle → at the interlude (§6.6)
  the list shows its printed gap — the interval is a line
  space in the list, not an item → footer arrival: §6.18 draws
  the final check.
- **State matrix (v2).** *Rest:* per-item states above. *Hover:*
  a row warms its name to `--cream` (a finger running down the
  list). *Focus:* as hover + brass outline; Enter jumps to the
  set. *Active:* n/a. *Scrolled-past:* checks persist (furthest
  reach). *Disabled / no-JS:* printed contents, no checks.
  *Touch:* rows are ≥44px tap targets in the door menu.
- **Breakpoints (v2).** ≥1200px: full rail list. 768–1199px:
  rail list at 7 items max, names truncated with the full name
  in the door strip. <768px: door strip only (text + pencil
  underline); full list inside the door menu.
- **Edge cases & failure modes (v2).** *More sets than rows
  (a long page):* the list caps at 9; beyond that, items group
  ("Second set" spans its subsections) — the door's list is
  the evening's shape, not an index of headings. *Jump scroll
  to the footer:* all intermediate checks draw at once,
  staggered 60ms — the pencil catches up in one pass, honestly
  showing it is catching up. *A section removed from the page:*
  the list is data-driven from the bill; a set not on the bill
  is not in the list and not a section (§4's running order is
  enforced by the data, not by hope).
- **Accessibility spec (v2).** The list is a `<nav>` with
  `aria-label="Tonight's sets"`; the current item carries
  `aria-current="true"` and a visually hidden "(now playing)";
  played items carry "(played)" in hidden text — progress is
  fully available without seeing a single tick. Contrast:
  `--pencil` checks are decoration beside text; names meet
  §2 floors at every state (`--cream-dim` 8.95:1 at their
  dimmest).
- **Tokens consumed (v2).** `--pencil`, `--brass`, `--cream`,
  `--cream-dim`, `--candle`, `--ease-swing`, `--dur-check`
  (300ms), `--dur-warm` (450ms).

### 6.10 Dip-to-black transitions

- **What & why.** Moving between pages dips the room to
  near-black, holds a beat of bass — about 300ms of almost
  nothing — and lights the new room. It belongs because a club
  is entered room by room through dark corridors, and a hard
  cut to a bright new page would be a door thrown open onto
  daylight. The dip is also the theme's honesty about loading:
  the dark *is* the wait, furnished.
- **Structure.** A fixed `--club-deep` overlay (`aria-hidden`,
  `pointer-events: none` at rest, intercepting only during the
  dip's first 300ms to prevent a double navigation). On the
  destination page, §6.1's dim layer runs in miniature: the new
  room starts dipped and settles up. The overlay is the same
  element reused across both ends (out-dip on the old page,
  in-settle on the new), so the corridor has one door, not two.
  Links that leave the site, open documents, or trigger
  downloads never dip — the corridor is only between the club's
  own rooms.
- **Motion spec.** Trigger: an internal navigation the build
  has enhanced (progressive enhancement over real links; the
  href always works bare). Out: overlay to full `--club-deep`
  in 300ms `--ease-dim`. Hold: 300ms of near-black — during
  which, if the destination is not ready, a single candle dot
  (§6.7's ember at 10px) breathes at the screen's centre: the
  corridor has one light, and it is the house's, not a spinner.
  In: the new page settles from dipped over 500ms `--ease-dim`
  (a shorter, shallower cousin of §6.1 — you are already
  inside; only the room changes). Total ceremony ≤1100ms when
  the destination is instant; the hold extends only while
  loading is real.
- **States.** *Rest:* overlay absent (removed, not transparent —
  a resident overlay eats clicks and frames). *Dipping /
  holding / settling:* transient. *Aborted (visitor hits back
  mid-dip):* the overlay clears in 150ms and the current room
  stands — the corridor never traps anyone. *Failed navigation:*
  the overlay clears, the house note (§11) speaks, the visitor
  is exactly where they were.
- **Content merge.** The dip is between the site's own pages —
  its duration is the real load, its candle is the house's
  mark, and the destination's settle lands on that page's real
  bandstand. It decorates nothing; it *is* the site's
  architecture of rooms.
- **Failure fallback.** Watchdog 3000ms: any dip state older
  than that is cleared unconditionally — a corridor that never
  ends is the one unforgivable state in this theme, and the
  timer is the theme's most-tested line of code. No JS: plain
  navigation, no overlay, pages load as pages. Slow network:
  the candle breathes; at 3000ms the overlay clears to the
  *destination's own* loading state (§6.17) rather than holding
  the visitor in the dark.
- **Reduced-motion variant.** No dip: navigation is instant,
  the destination opens at club level. The corridor is a
  courtesy, not a requirement, and it is the first ceremony the
  theme surrenders.
- **Performance budget & mobile variant.** One overlay div +
  one dot; the transition is opacity only. Mobile: identical,
  hold shortened to 200ms (a phone corridor is shorter) and the
  candle at 8px.
- **Choreography timeline (v2).** t=0 navigation → t=0–300 dip
  to `--club-deep` → t=300 hold begins; candle breathes if load
  is real → destination ready → t=+0–500 settle up on the new
  room → new page's §6.3-equivalent beats arm (its bill, its
  sign already lit — §6.4 warms once per session, not per room).
- **State matrix (v2).** *Rest:* absent. *Hover/focus:* n/a.
  *Active:* the dip itself. *Scrolled-past:* n/a. *Disabled /
  no-JS:* absent; plain links. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: as
  specced. <768px: hold 200ms, settle 420ms. The dip's colour
  and the watchdog never change with size.
- **Edge cases & failure modes (v2).** *Hash links within a
  page:* no dip — you are moving within the room; the spotlight
  swings instead (§6.2). *Form submission (§6.15):* no dip; the
  ledger confirms in place — leaving the room to book a table
  in it would be absurd. *Prefetch:* a prefetched destination
  makes the hold 0ms; the dip still runs (300+500) because the
  corridor is also a breath, but a same-page-prefetch may not
  extend it. *Browser back/forward:* the dip plays in reverse
  order (settle first, no hold) — returning to a room is
  quicker than finding a new one.
- **Accessibility spec (v2).** The overlay is `aria-hidden`;
  during the hold, the destination's title is announced by the
  router's live region once loaded ("The drinks list — The
  Velvet Note"). Focus lands on the destination's heading on
  arrival, never left on a removed element. The candle is
  decoration; a screen-reader visitor experiences a normal,
  fast navigation.
- **Tokens consumed (v2).** `--club-deep`, `--candle`,
  `--ease-dim`, `--dur-dip` (300ms), `--dur-hold` (300ms),
  `--dur-settle` (500ms), `--dur-watchdog-transition` (3000ms).

### 6.11 The bandstand hero

- **What & why.** The hero is the bandstand itself: a pinned
  stage where the headline set plays — the club's name warming
  above (§6.4), the evening's headline act in Italiana under a
  spotlight cone that *is* a widening clip of light, the bill
  placed at its right (§6.3), the brass rail at its foot. It
  belongs because the first screen of a club's site should be
  the moment the band starts: not a photograph of a stage, but
  the stage, occupied. The pin holds the visitor in that moment
  for exactly one extra breath of scroll while the set changes
  beside the headline — then lets the evening proceed.
- **Structure.** A `<section>` of 100vh pinned for an additional
  60vh of scroll (≥1200px; §6.11's breakpoints scale it down).
  Inside: the curtain — two `--velvet` fields at the stage's
  edges, drawn as layered gradients with a fold rhythm, framing
  never covering; the sign (§6.4) top-centre; the headline act
  (Italiana 54px) centre-stage on the rail line (§4); the
  cone — a soft clip mask over a lit duplicate of the headline
  block, its width a custom property (`--cone`, 18%→100%)
  scrubbed by pin progress, over the printed headline at rest
  light beneath (the duplicate structure of §6.2's law: the
  printed layer is never the animated layer); the bill (§6.3)
  at right; the standfirst and doors line below the rail. The
  pin is JS-armed (a `position: sticky` stage inside a 160vh
  track); without JS the stage is a normal 100vh section.
- **Motion spec.** Entrance (after §6.1/§6.4): the cone widens
  over the headline 1400ms `--ease-swing`, the brass rail glints
  once as the cone crosses it (a 600ms `--brass-bright` sweep
  along the rail, once). Pin scrub: across the 60vh pin, the
  cone travels the headline set — horn, piano, drums (the
  headline act's line-up, printed as three names at the rail)
  catch light in order (§6.2 conducts), and the evening's
  *second* headline fact (the late set's act) cross-lights at
  the pin's end: the bill changes beside the bandstand, as the
  original entry promises. Release: the stage unpins and the
  room's first table (§6.7) takes the light. Scrolling back up
  replays the scrub in reverse — the set un-plays as honestly
  as it played.
- **States.** *Pre-entrance:* printed stage, headline at rest
  light (readable — §1). *Entrance:* cone widening, rail glint.
  *Pinned:* scrub state by progress. *Released:* the stage
  scrolls away as a normal section, its cone parked at rest
  width (62% — the stage stays lit after you leave it; a club
  does not darken its bandstand because one guest walked to
  their table). *Focus within:* any focus into the stage during
  the pin completes the scrub instantly to the focused beat.
- **Content merge.** Every object on the stage is content: the
  name, the act, the line-up, the bill, the doors line — the
  pin's scrub moves *between the page's real headline facts*.
  There is no decorative layer on the bandstand at all; the
  curtain frames the stage's edges and carries the club's name
  embroidered small at its foot (a credit line, §12).
- **Failure fallback.** Watchdog 4000ms on the pin: if the
  scrub loop stalls, the pin releases (track collapses to
  100vh) and the stage stands lit at rest width. No JS: a
  100vh stage, fully lit, bill printed — the hero as a poster
  of itself, complete. If the evening has no headline act (a
  dark night — the club is closed Mondays), the stage prints
  the house's closed-night bill (§12's voice) instead of an
  empty stage: an unlit, unoccupied bandstand is the one image
  this theme refuses to ship.
- **Reduced-motion variant.** No pin, no cone travel: the stage
  is a static 100vh section, cone at rest width, both headline
  facts printed in sequence. The bandstand as a photograph of
  itself — composed, lit, still.
- **Performance budget & mobile variant.** The pin track +
  sticky stage cost one composited layer; the cone mask
  animates a registered custom property (compositor-driven).
  Budget: ≤10KB CSS/SVG (curtain gradients, no images).
  Mobile (<768px): **the pin is abolished** — a phone's stage
  is one screen, no extra scroll; the cone sits at rest width,
  the two headline facts stack (act, then late set beneath the
  rail), the bill goes full-width below (§6.3). Tablet
  (768–1199px): pin shortens to +35vh, cone travel compressed
  to two beats.
- **Choreography timeline (v2).** t=0 (page timeline) dim
  (§6.1) → sign warms (§6.4) → cone widens 1400ms → rail glint
  at cone's crossing ≈t=3400 → bill glides (§6.3, t=1900
  overlapping) → scroll: pin scrubs horn→piano→drums, ~20vh per
  beat → pin end: late-set fact cross-lights 600ms → release:
  spotlight swings to the first table (900ms, §6.2).
- **State matrix (v2).** *Rest:* stage lit, cone 62%. *Hover:*
  the rail glints under a pointer crossing it (once per
  crossing, 400ms — the brass is touchable, the stage is not).
  *Focus:* completes scrub to the focused beat. *Active:* n/a.
  *Scrolled-past:* stage lit at rest, bill's echo in the door
  (§6.12). *Disabled / no-JS:* static lit stage. *Touch:* no
  pin below 768px; tablet pin scrubs by touch scroll as by
  wheel.
- **Breakpoints (v2).** ≥1200px: 100vh + 60vh pin, cone travel
  full, bill at right. 768–1199px: +35vh pin, two-beat travel,
  bill tucked under the rail. <768px: no pin, stacked facts,
  bill full-width below.
- **Edge cases & failure modes (v2).** *Short viewport (landscape
  phone, 360px tall):* the stage min-height is content-driven,
  never 100vh-forced — the bandstand may be taller than the
  screen rather than cropped. *Headline act name very long:*
  Italiana drops to 42px at ≥1200px by a printed size step (a
  data attribute set at build from character count) — the stage
  never shrinks type mid-flight. *Visitor scrolls fast through
  the pin:* the scrub is position-bound, so speed costs
  nothing; the beats are states, not animations that can be
  missed.
- **Accessibility spec (v2).** The stage is a `<section>` with
  the `<h1>` sign; the lit duplicate is `aria-hidden`, the
  printed headline is the accessible one. The pin never traps
  scroll or focus: it is a sticky visual, and keyboard travel
  through the stage's links proceeds at natural document pace
  (focus completes the scrub, above, so a focused element is
  never left unlit). Contrast: headline `--cream` on `--club`
  14.44:1 at rest light — the cone adds warmth, never legibility.
- **Tokens consumed (v2).** `--velvet`, `--club`, `--cream`,
  `--brass`, `--brass-bright`, `--ease-swing`, `--dur-cone`
  (1400ms), `--dur-watchdog-pin` (4000ms), `--loop-lerp` (0.12).

### 6.12 The door & coat-check navigation

- **What & why.** Navigation is the club's door: a narrow top
  bar carrying the name plate (printed lit — §6.4's door
  ruling), the evening's rooms as links, a brass door number,
  and the two house controls — the house-lights override (§2)
  and, below 1200px, the set-list strip (§6.9). It belongs
  because in this theme you do not "use a navbar"; you are let
  in, your coat is taken, and the door is where the evening's
  shape is first told. The coat-check conceit is functional:
  each room-link carries a small brass ticket number — the
  order of the evening — so the nav teaches the running order
  (§4) while it navigates.
- **Structure.** A `<header>` bar, 64px, `--club` with a 1px
  brass rule beneath at 40%. Left: the name plate (Italiana
  22px, `--cream`, printed lit). Centre/right: room links in
  Jost labels (§3) each prefixed by its ticket numeral in
  `--brass`. Right: the house-lights toggle (a real `<button>`
  with `aria-pressed`, labelled "House lights") and the
  tonight strip — the next set's name and time from the bill's
  data (§6.3) — which is the bill's echo promised in §6.3.
  Mobile: the bar holds the plate, the strip, and a "The door"
  menu button opening a full-height panel (the door opens
  inward) with the links at 56px rows and the full set list
  (§6.9) beneath them.
- **Motion spec.** The bar is calm: on scroll down past 300px
  it settles 6px shorter (64→58px, 300ms `--ease-swing`) and
  its brass rule warms to 60% — the door lowers its voice once
  you're in. The menu panel glides in 380ms `--ease-glide`
  from the right with the room dipping 20% behind it (a
  lighting change, not a grey overlay). The tonight strip
  updates its set name with a 200ms cross-fade when the bill's
  data rolls to the next set — the door keeps the evening's
  time so the visitor doesn't have to. Ticket numerals glint
  (400ms `--brass-bright` sweep) on hover/focus of their link —
  brass under a thumb.
- **States.** *Top of page:* full height, rule at 40%. *Scrolled:*
  settled height, rule at 60%, the current room's link carries
  its candle dot (§6.9's marker, shared). *Menu open:* panel
  in, room dipped, focus trapped in the panel, Esc or the door
  button closes. *House lights on:* the toggle shows pressed,
  and the whole page's lighting layers are at rest (§6.1, §6.5
  removed) — the door is where the room's light is *controlled*,
  so the control lives here.
- **Content merge.** The door's links are the site's real rooms
  in the evening's real order; its strip is the bill's real
  next set; its toggle runs the page's real lighting rig. It
  is the one element present on every page, and it is the
  theme's thesis in miniature: admission, order, light.
- **Failure fallback.** No JS: the bar is a plain header with
  working links; the menu panel's contents print inline as a
  wrapped second row (the panel is JS-folded, not JS-created);
  the house-lights toggle is absent (there is no rig to
  override) and the strip prints tonight's full bill link
  instead of the live next set. Sticky behaviour is CSS
  (`position: sticky`) — no scroll JS can strand it.
- **Reduced-motion variant.** The bar never settles (fixed
  64px), the panel appears without glide (150ms fade), glints
  are removed; the strip's cross-fade becomes an instant swap.
- **Performance budget & mobile variant.** ≤4KB CSS; the bar is
  one sticky layer. Mobile (<768px): bar 56px, plate 19px,
  strip truncated to the set name only (the time lives in the
  panel), menu rows 56px.
- **Choreography timeline (v2).** Page load: bar printed with
  the room (it dims with §6.1 like everything — the door is in
  the room) → scroll 300px: settle 300ms → menu open: dip
  200ms, panel glide 380ms → set roll (bill data): strip
  cross-fade 200ms → house-lights toggle: all layers settle to
  rest over 600ms `--ease-dim` (the room putting its lights up
  is a dim in reverse, and it takes its time).
- **State matrix (v2).** *Rest:* as specced. *Hover:* link
  numeral glints, link name warms to `--cream`. *Focus:* brass
  outline + glint. *Active:* link presses 1px, 90ms.
  *Scrolled-past:* settled bar. *Disabled / no-JS:* printed
  header, inline panel contents. *Touch:* rows ≥56px in the
  panel; bar links ≥44px tall via padding.
- **Breakpoints (v2).** ≥1200px: full bar + rail set list
  (§6.9) separate. 768–1199px: bar + strip; set list folds to
  the strip's compact form. <768px: 56px bar, menu panel
  carries links + full set list.
- **Edge cases & failure modes (v2).** *Many rooms (8+ links):*
  links beyond six move into the door panel at every width —
  a door with nine handles is a wall. *Very long room names:*
  labels truncate at 14ch with the full name in the panel;
  the ticket numerals never truncate (the numbers are the
  order). *House-lights persisted:* the toggle's state is in
  localStorage; a first-time visitor always meets the room as
  designed (lights down), the regular's preference after.
- **Accessibility spec (v2).** Landmark `<header>` + `<nav
  aria-label="The rooms">`; the current room carries
  `aria-current="page"`. The menu button is `aria-expanded` /
  `aria-controls` correct; the panel traps focus while open
  and returns it to the button on close. The toggle's label
  and pressed state are text, not icon-only. Contrast: plate
  14.44:1, labels `--cream-dim` 8.95:1, numerals `--brass`
  8.12:1 — all on `--club`.
- **Tokens consumed (v2).** `--club`, `--cream`, `--cream-dim`,
  `--brass`, `--brass-bright`, `--ease-swing`, `--ease-glide`,
  `--ease-dim`, `--dur-bar-settle` (300ms), `--dur-panel`
  (380ms).

### 6.13 Tonight's tables

- **What & why.** The listing at the room's heart: the tables
  that can be kept tonight, each a card (§6.8's flip lives
  here) with its candle (§6.7), its name, its seats, its place
  in the room ("by the bandstand", "the alcove", "the rail"),
  and its state. It belongs because a club's inventory is not
  SKUs — it is furniture in a room, each piece with a position
  and a mood — and the grid's job is to let a visitor choose
  *where in the evening* they want to sit. This is the theme's
  listing page pattern, and §7 maps it onto every listing the
  site will ever need.
- **Structure.** A grid of table cards (§6.8), max 3 across
  (§4's density law), each card 4:3-ish, its surface a
  `--velvet` field at rest with the table's photograph admitted
  only as duotone-in-the-dark (§5): a CSS-filtered image
  (grayscale, crushed blacks via `contrast(1.15)
  brightness(0.82)`, warmed by a `--velvet` multiply overlay at
  22%) so every photograph sits in the room's light, never
  daylight's. The card's facts are printed: name (Italiana
  22px), seats and position (Jost), the state line — the
  absinthe mark (a 10px door-lamp dot) *plus the word* "Free
  tonight" when available (§2's never-sole-indicator rule),
  "Kept" in `--pencil` when not. The candle (§6.7) sits at the
  card's top corner — the card *is* a table, and tables have
  candles.
- **Motion spec.** Cards enter the light as the grid scrolls
  in: not a stagger-fade (refused, §5) but the spotlight's
  pass — the cone (§6.2) crosses the grid and each card's
  candle takes attended level as the light reaches it, 120ms
  apart by position, a *consequence* of the light's travel, not
  a choreographed entrance. Hover: the candle leans (§6.7) and
  the photograph's overlay thins 22%→14% (the picture warms as
  you look). The flip is §6.8's. Filtering (by seats, by
  position — §11's chips) re-lays the grid with a 240ms
  `--ease-glide` settle per card; the candle states recompute
  after, never during.
- **States.** *Available:* absinthe dot lit + "Free tonight".
  *Kept:* pencil "Kept", candle at ember, card unflippable
  (§6.8). *Reserved by you:* the flipped, sealed face (§6.8).
  *Attended / leaned:* per §6.7. *Filtered out:* the card is
  removed from the grid (not dimmed — a table that seats two
  is not a dimmer version of a table that seats six).
- **Content merge.** The cards are the inventory, the grid is
  the room's floor, and the candle/spotlight system that lights
  them is the same one that lit the bandstand — the listing is
  not a component dropped into the theme; it is the theme's
  middle act (§4's second set).
- **Failure fallback.** No JS: all cards printed front-face at
  attended light, photographs duotoned by CSS alone (the
  filter is CSS, not JS), states printed as text; reserving
  goes by the ledger link on each card (§6.8). A table with no
  photograph prints its name large on velvet — a card without
  a picture is a table in a dark corner, still bookable, never
  a broken-image icon.
- **Reduced-motion variant.** Cards printed at attended light;
  the spotlight pass does not animate candles (they are simply
  at attended level); filtering swaps instantly.
- **Performance budget & mobile variant.** Images: duotone via
  CSS filter costs no extra bytes; each card image ≤60KB
  (they are dark and small — the format forgives), lazy-loaded
  below the first row. Grid ≤9 tables per page (the room's
  size, §1). Mobile (<768px): one card per row at full width,
  photograph as a 16:7 crop at the card's head, candle at the
  heading's left (§6.7's mobile ruling).
- **Choreography timeline (v2).** Grid top enters → cone swings
  to the grid (900ms, §6.2) → candles take attended in light
  order, 120ms apart → hover: candle leans 450ms, overlay
  thins → click: §6.8's flip (520ms) + seal (140ms) → the door
  tally (§6.16) reprints its held count from the DOM.
- **State matrix (v2).** *Rest:* front face, state printed.
  *Hover:* candle lean, overlay 14%. *Focus:* as hover + brass
  outline on the card's control. *Active:* §6.8's press.
  *Scrolled-past:* candle to ember. *Disabled:* kept tables —
  printed reason, no flip. *Touch:* tap = §6.8; the overlay
  thinning is hover-only and its absence costs nothing (the
  facts are text, not image).
- **Breakpoints (v2).** ≥1200px: 3 across, gap 28px (dark
  between tables). 768–1199px: 2 across, gap 22px. <768px: 1
  across, gap 18px, image crop 16:7.
- **Edge cases & failure modes (v2).** *A night with every
  table kept:* the grid prints the kept state honestly and the
  section's head line offers the rail ("The tables are kept
  tonight — the rail is open, and the ledger (§6.15) takes
  names for tomorrow") — an empty state in the house voice,
  never a blank grid. *One table only:* the grid centres a
  single card at 420px — a room with one table is a private
  room, and the layout says so. *Image fails to load:* the
  velvet name-card fallback above; the layout never depends on
  the photograph.
- **Accessibility spec (v2).** The grid is a list (`<ul>`) of
  articles; each card's control is labelled with name, seats,
  position, state (§6.8). State is never colour alone: the
  absinthe dot accompanies the words "Free tonight" (§2).
  Photographs carry alt text describing the table's position
  ("The alcove table, two seats, beside the curtain"), not
  decoration-empty alts — the picture *is* information here.
  Contrast per §2 throughout; kept cards' pencil text 6.29:1
  (annotation-grade, and it annotates a state also carried by
  the card's unflippability and label).
- **Tokens consumed (v2).** `--velvet`, `--velvet-deep`,
  `--absinthe`, `--candle`, `--pencil`, `--cream`, `--brass`,
  `--ease-glide`, `--dur-card-settle` (240ms).

### 6.14 The drinks list

- **What & why.** The bar's printed list: drinks in two
  columns of ruled lines, names in Jost, prices in brass
  tabular numerals, and — in fine print at the foot, verbatim
  from the original entry — the house rule: *"No requests
  after midnight. The band knows what you need."* It belongs
  because every club page eventually lists something with
  prices (drinks, tickets, covers), and this is the theme's
  answer to the price list: a document the room prints, lit by
  a candle, ruled like a ledger. It is §7's pattern for menus,
  tariffs and cover charges alike.
- **Structure.** A `<section>` styled as the bar's list: a
  cream card (the list is *printed paper*, like the bill §6.3,
  but wider — 720px max, two columns at ≥1200px) in club ink,
  entries as definition rows: name + dotted leader + price,
  the leader a real dotted border (the print does the work, no
  SVG). Section heads within the list ("From the bar", "The
  green bottle" — the absinthe's one section, its entries the
  only place `--absinthe` may appear as a *printed* colour, in
  the section head's rule) in Italiana. The house rule sits at
  the foot in 12.5px fine print, preceded by a brass fleuron.
  The list's candle (§6.7) is fixed at its top-left — the bar
  has one candle and it is on the list.
- **Motion spec.** The list is nearly still — a printed thing
  does not perform. Its one motion: as it enters the light, its
  cream face warms (a `--candle` wash at 0→6% over 900ms
  `--ease-swing`, keyed to the spotlight's arrival §6.2) — the
  paper catching the room's light. Entry rows never animate.
  Prices never count, tick or flash: a price that moves is a
  price you don't trust (§9). Hover on a row: the leader dots
  warm to `--brass` over 200ms — a fingertip running down the
  list.
- **States.** *Rest:* printed, cool cream. *In the light:*
  warmed 6%. *Hovered row:* brass leader. *Scrolled-past:*
  the wash stays (paper keeps the light it caught — a printed
  list has no off state). *The midnight state:* after 00:00
  visitor-local time, the house rule's line takes a pencil
  underline (drawn, 300ms, §6.9's pencil) — the rule is now in
  force, and the list quietly says so. A build may disable
  this; it may not fake it (the time is the visitor's real
  clock or the line is never underlined).
- **Content merge.** The list is the bar's real drinks and real
  prices — the prices are data (§1's law: the tally and the
  ledger read the same figures), and the house rule is the
  room's actual policy in its actual words. Nothing here is a
  styled placeholder.
- **Failure fallback.** No JS: the list prints cool and
  complete; the midnight underline is a garnish that never
  gates content. If the drinks data is empty (a dry night —
  the bar is closed), the card prints the house's closed line
  (§12) and the evening's bill (§6.3) instead — a list card is
  never shipped empty.
- **Reduced-motion variant.** The wash is present at rest
  (paper pre-warmed), the leader hover is instant, the midnight
  underline prints whole.
- **Performance budget & mobile variant.** Pure CSS/print
  styling, ≤3KB; no images. Mobile (<768px): one column, the
  card full-width, prices right-aligned without leaders below
  380px (a leader needs width to lead).
- **Choreography timeline (v2).** Section enters → spotlight
  arrives (900ms) → wash warms 900ms overlapping the swing →
  rest. Midnight (if crossed while reading): underline draws
  300ms once.
- **State matrix (v2).** *Rest:* printed. *Hover:* row leader
  warms. *Focus:* a row's link (where entries link to a detail)
  gets the brass outline; leader warms as hover. *Active:* n/a.
  *Scrolled-past:* wash held. *Disabled / no-JS:* printed cool.
  *Touch:* no leader hover; rows are text, fully legible.
- **Breakpoints (v2).** ≥1200px: two columns, 720px card.
  768–1199px: two columns at 640px, entries tighten (name
  15px). <768px: one column, full-width card, leaders kept to
  380px then dropped.
- **Edge cases & failure modes (v2).** *Long drink names:*
  the name wraps to two lines and the price stays on the
  first line's baseline — the leader shortens, never the price.
  *A price changes:* data-driven reprint, no motion — prices
  change in print, silently, like a re-inked card. *Currency
  with long symbols:* tabular Jost holds alignment; the column
  is sized for the widest real price in the data at build.
- **Accessibility spec (v2).** The list is a `<dl>`-structured
  list with prices as text ("— twelve") readable in order;
  leaders are CSS borders, invisible to AT and never missed.
  Contrast: club ink on `--cream` 14.44:1; prices in a deep
  brass-ink `#7A5E14` on cream (7.1:1, measured at build) —
  the bright `--brass` is for dark grounds only, and the list
  is a light ground: the palette inverts its ink, never its
  standards.
- **Tokens consumed (v2).** `--cream`, `--club`, `--brass`,
  `--candle`, `--pencil`, `--absinthe`, `--ease-swing`,
  `--dur-wash` (900ms).

### 6.15 The reservation ledger

- **What & why.** The conversion form, kept as the house
  ledger: a ruled book at the bar where the evening's
  reservations are written in a hand — name, party, table,
  time — and confirmed with the house seal and an entry number
  counted from the ledger's own printed entries. It belongs
  because it is where the room's rituals become a transaction:
  §6.8's card flip *holds* a table; the ledger *writes it
  down*, and what is written in the ledger is the booking.
  Every Velvet Note conversion — a table, a ticket, a private
  night — is a ledger entry wearing different column heads.
- **Structure.** A `<form>` on a `--velvet-deep` panel ruled
  with `--pencil` lines: fields as ledger rows (label in
  tracked Jost capitals, input as a writing line — bottom rule
  only, transparent ground, `--cream` text in Jost 17px).
  Fields: name, party size (a stepper of tally marks, §11),
  table (a select listing tonight's tables from §6.13's data,
  pre-chosen if arrived from a card), time (tonight's set
  times from §6.3's data — the form cannot invent a time the
  band isn't playing). The confirmation replaces the form *in
  place*: the entry written out in the ledger's hand (Jost
  italic), the seal (§6.8's SVG) stamped beside it, and the
  entry number — "Entry № 214" — derived from the count of
  entries already printed in the ledger's sample page + 1,
  the same derive-from-the-DOM discipline as §6.8's tally.
- **Motion spec.** Focus: the field's rule warms to `--brass`
  (200ms) and the row's candle-dot (each row carries a 6px
  ember) brightens — you write by candlelight. Error: the row
  shakes *once*, 120ms, 3px — a clerk's headshake, never a
  buzzer — and the message prints beneath in the house voice
  (§12). Submit: the seal stamps (140ms `--ease-stamp` +
  ring, §6.8's gesture) *before* the request resolves — the
  house commits first — and the form's rows settle 40ms apart
  as if pressed under the seal. Success: the entry writes
  itself — the confirmation lines fade-and-rule in at 90ms
  stagger, 300ms each; the entry number counts from the
  previous entry's number to its own (a count of one or two —
  honest arithmetic, §6.16's rule).
- **States.** *Rest:* ruled, empty, the first field's ember
  lit (the book is open). *Focus:* per row above. *Error:*
  message printed, field's rule in `--velvet` bright
  (`#A52A32`, the room's only error colour — a red pencil,
  fitting the ledger) with the message in `--cream` text (the
  colour assists, the words carry). *Submitting:* fields
  disabled, seal stamped, a pencil line draws under "Writing…"
  (§12's word — never "Processing"). *Confirmed:* the entry,
  the seal, the number, and one line: "The table is kept. A
  note is on its way to {the name given}." *Failed:* the form
  restored with every value intact — the ledger never eats
  what was written in it.
- **Content merge.** The ledger's tables and times are the
  page's own data (§6.13, §6.3); its seal is §6.8's seal; its
  entry number counts the page's own printed entries. The form
  is the room's book, not a webform in costume — remove the
  theme and the fields, options and arithmetic all still have
  to exist, because they *are* the business's.
- **Failure fallback.** No JS: a plain, working form (real
  submit, server confirmation page styled as a ledger leaf) —
  the writing-in animation is an enhancement. Validation is
  server-mirrored; the client voice (§12) never contradicts
  the server's facts. Watchdog: a submission unresolved at
  4000ms returns the form to its filled state with the house
  note (§11) — the seal unstamps (fades 200ms): the house does
  not keep a seal on an entry it could not write.
- **Reduced-motion variant.** No write-in stagger, no shake
  (errors print plainly), the seal present at rest on the
  confirmation. Focus warmth is instant.
- **Performance budget & mobile variant.** Form styling ≤5KB;
  the seal SVG is §6.8's, reused (one seal per house). Mobile
  (<768px): single column (it already is), inputs at 17px
  (no iOS zoom), the stepper's tally marks at 44px targets,
  the panel full-width with its ruling intact.
- **Choreography timeline (v2).** Arrival: spotlight parks on
  the seal point (§6.2) → first field ember lit → focus: rule
  warms 200ms → submit: seal stamps 140ms → rows settle 40ms
  stagger → resolve: confirmation lines at 90ms stagger →
  entry number counts (≤800ms) → the set list (§6.9) does not
  change (a booking is not a set) but the door tally's held
  count (§6.16) reprints.
- **State matrix (v2).** *Rest:* open book. *Hover:* a row's
  ember warms. *Focus:* rule to brass, ember bright. *Active:*
  submit press — the stamp. *Scrolled-past:* a half-filled
  ledger keeps its values (the book stays open on the bar).
  *Disabled:* during submit only, values preserved. *Touch:*
  steppers and selects at 44px+; no hover dependence.
- **Breakpoints (v2).** ≥1200px: panel 560px, two fields side
  by side where a row pairs naturally (party + time).
  768–1199px: 520px, paired rows kept. <768px: full-width,
  all rows single, paired rows stack.
- **Edge cases & failure modes (v2).** *The chosen table is
  taken between flip and submit:* the ledger says so in the
  house voice and offers the nearest table by position — the
  error is a concierge, not a dead end. *Party larger than any
  table:* the stepper caps at the largest table's seats with
  the note printed beside it ("For more than eight, write to
  the house" + the contact link) — the form never silently
  accepts what the room cannot seat. *Midnight crossing
  mid-booking:* times are tonight's data; if the night rolls
  over, the form reprints its times and keeps the name — the
  book does not close in a guest's hands.
- **Accessibility spec (v2).** Real `<label>`s, `aria-describedby`
  for the house-voice hints, errors in `role="alert"` text
  (never colour-only: the red pencil underlines, the words
  explain). The confirmation is a polite live region. Contrast:
  `--cream` on `--velvet-deep` 9.78:1 for inputs and text;
  labels `--brass` on velvet-deep measured at build (≥4.5:1
  required, else labels go `--cream-dim` on the panel's club
  strip — the build chooses by measurement, not hope).
  Focus order follows the ledger's rows; the seal is
  decoration beside a text confirmation.
- **Tokens consumed (v2).** `--velvet-deep`, `--pencil`,
  `--brass`, `--cream`, `--cream-dim`, `--candle`,
  `--ease-stamp`, `--ease-glide`, `--dur-stamp` (140ms),
  `--dur-write-stagger` (90ms).

### 6.16 The door tally

- **What & why.** By the door, the evening's figures are kept
  in brass numerals: tonight's house count, the tables kept,
  the sets played — counted up once as the bandstand settles,
  and reprinted whenever the room's real state changes. It
  belongs because a club's door is where the night is measured
  (the doorman's clicker is the original analytics), and because
  it is the theme's data conscience: every figure here traces
  to the page's own printed data — the bill's sets (§6.3), the
  tables' states (§6.13) — so the tally is where §1's
  every-number-is-real law is audited in public.
- **Structure.** A row of three to four figures in the
  bandstand's foot (and echoed, static, in the door panel
  §6.12): each a brass Jost numeral (28px, tabular) over a
  tracked label ("IN THE HOUSE", "TABLES KEPT", "SETS PLAYED").
  The numerals are printed in the DOM at their true values;
  JS arms only the count-up, starting each from the figure's
  own *previous* printed value where one exists in the data
  (doors-open count for the house) or from 60% of the figure —
  never from zero: a club does not count its crowd from an
  empty room it never had. (The one honest zero: "TABLES KEPT
  0" before any reservation — printed as a true zero, counted
  not at all.)
- **Motion spec.** Trigger: the bandstand's entrance completing
  (§6.11), once. Count: 1200ms `--ease-swing`, in quantised
  steps at each figure's own precision (whole people, whole
  tables), landing *exactly* on the printed figure — a count
  that overshoots or eases past its number is a lie with good
  easing. Reprints (a reservation made, a set played): the
  changed figure alone re-counts from its old value to its new
  one, ≤800ms, while a pencil tick appears beside it (§6.9's
  pencil — the doorman marks the change by hand).
- **States.** *Printed:* true values, static — the state every
  visitor gets with no JS, and the state screen readers always
  get (the count is visual only; the figure's text is final
  from first paint, with the animated numeral `aria-hidden`
  and a visually-hidden true-value twin, the Fog-Harvest-proven
  pattern). *Counting:* transient. *Reprinting:* per change.
  *Night over (after last orders, §6.18):* the tally freezes —
  the door stops counting when the room closes.
- **Content merge.** The figures are the page's own facts
  counted from the page's own DOM — house count from the
  evening's data, tables kept from §6.13's live states, sets
  played from §6.9's checks. Change the data and the tally
  changes; there is no other way for it to move.
- **Failure fallback.** No JS: printed figures, full stop.
  Count interrupted (tab hidden): the numeral snaps to the
  printed figure on return — a count abandoned mid-way
  resolves to the truth, never to a stopped lie. If a data
  source is absent (no tables on this page), its figure is
  absent too — the tally shows fewer figures, never a filler.
- **Reduced-motion variant.** Figures print at value; reprints
  swap instantly with the pencil tick printed whole.
- **Performance budget & mobile variant.** ≤4 numerals, one
  shared rAF count in the main loop. Mobile (<768px): two
  figures per row, numerals 22px, the count shortened to
  900ms.
- **Choreography timeline (v2).** Bandstand entrance completes
  → t=0 figures count, staggered 120ms by rank (house first —
  the doorman counts people before furniture) → t=1200 all
  landed → thereafter event-driven: reservation → TABLES KEPT
  re-counts ≤800ms + pencil tick → set played → SETS PLAYED
  likewise → last orders: freeze.
- **State matrix (v2).** *Rest:* printed true values. *Hover:*
  none (figures are read, not touched). *Focus:* n/a (not
  interactive). *Active:* n/a. *Scrolled-past:* values persist;
  no recount on return. *Disabled / no-JS:* printed. *Touch:*
  identical.
- **Breakpoints (v2).** ≥1200px: one row, 28px numerals.
  768–1199px: one row, 24px. <768px: two-by-two, 22px, count
  900ms.
- **Edge cases & failure modes (v2).** *A figure decreases*
  (a reservation released): it counts *down* with the same
  honesty — the doorman's clicker goes both ways in this
  house, and the pencil tick becomes a pencil stroke-through
  that fades. *Huge figures* (a festival night, 1,200 in the
  house): tabular Jost holds; the count steps coarsen (by 10s
  above 500) so the duration stays 1200ms — the precision rule
  is the figure's own, and a crowd's own precision is the ten.
  *Data disagreement* (bill says 3 sets, set list shows 4):
  the tally prints the *bill's* figure and the build fails the
  gate (§10) — the room's books must agree before the doors
  open.
- **Accessibility spec (v2).** As specced under States: the
  true figure is always the accessible text; animated numerals
  are `aria-hidden` with visually-hidden twins. The tally is a
  `<dl>` — label and figure paired for AT. Contrast: `--brass`
  on `--club` 8.12:1; labels `--cream-dim` 8.95:1.
- **Tokens consumed (v2).** `--brass`, `--cream-dim`,
  `--pencil`, `--ease-swing`, `--dur-count` (1200ms),
  `--dur-recount` (800ms).

### 6.17 Tuning up

- **What & why.** While a page or a heavy section loads, the
  band tunes up: the unlit shapes of the coming content stand
  in low light — a headline's silhouette, a card's outline —
  warmed by a slow shimmer that passes like a single tuning
  note held and adjusted. It belongs because waiting in this
  club is never a spinner in a void; it is the sound of the
  evening preparing, and the shapes you wait behind are the
  room's own furniture, unlit. It is the theme's skeleton
  state, and its law is the room's: the shapes are the *real*
  layout, so when the lights come up, nothing moves.
- **Structure.** Skeleton blocks are the real components with
  their content swapped for shaped placeholders at build/render
  time (never a separate skeleton page): text becomes ruled
  bars in `--smoke` at 18% on the component's own ground,
  images become their duotone frames (§6.13) empty, the bill
  becomes its card at rest tilt, unlit. One shimmer: a
  `--candle` gradient sweep across the block, 1600ms cycle,
  travelling left to right like a tuner walking the band. The
  bandstand's skeleton carries one extra truthful detail: the
  words "The band is tuning" in pencil (§12) at the rail —
  the only skeleton in the theme allowed words, because a
  guest standing in a dark room deserves one sentence.
- **Motion spec.** Trigger: any content region unresolved at
  first paint or during a §6.10 hold that outlasts its corridor.
  Shimmer: 1600ms `--ease-haze` cycle per block, phase-offset
  by the block's position (the tuning walks the room, it does
  not pulse in unison). Resolution: as each block's content
  arrives, its lights come up — 400ms `--ease-dim` from unlit
  to club level, block by block in arrival order; the shimmer
  dies with the first light. Ceiling: at 3000ms unresolved, the
  block gives up tuning and prints the house's apology line
  (§12) with a retry — the band does not tune forever.
- **States.** *Tuning:* shimmering silhouettes. *Resolving:*
  per-block light-up. *Resolved:* the real component, skeleton
  gone (removed from the DOM — a skeleton left under content
  is a ghost the room doesn't need). *Failed:* the apology +
  retry, in the component's own shape. *Never:* a skeleton for
  content that was already in the HTML — server-rendered rooms
  open lit (§6.1); tuning is only for what genuinely arrives
  late.
- **Content merge.** The skeleton *is* the content's shape —
  same boxes, same measure, same candle positions — so the
  merge is identity: nothing shifts when the lights come up,
  and the visitor has been reading the room's layout the whole
  time. CLS from a resolving block is a gate failure (§10),
  not a shrug.
- **Failure fallback.** The 3000ms ceiling above, plus: no JS
  means no skeleton states are ever armed (content is either
  in the HTML or the page says so in words). A block whose
  content fails permanently keeps its shape and its apology —
  the room acknowledges the missing chair rather than hiding
  the gap.
- **Reduced-motion variant.** No shimmer: unlit shapes, static,
  with "The band is tuning" printed; resolution is instant
  (no light-up fade).
- **Performance budget & mobile variant.** Skeletons are the
  components' own CSS + one gradient; ≤2KB incremental.
  Mobile (<768px): the shimmer sweep shortens to the block's
  width (it already is) and the cycle lengthens to 2000ms —
  fewer sweeps, less battery, same patience.
- **Choreography timeline (v2).** t=0 region unresolved →
  shimmer cycles (1600ms, phase-walking) → content arrives per
  block → each block lights up 400ms in arrival order →
  last block lit: skeleton layer removed → §6.2's cone, if it
  was parked on the region, resumes its programme. Ceiling
  3000ms per block → apology state.
- **State matrix (v2).** *Rest:* n/a (transient only). *Hover:*
  none — you cannot lean toward furniture that isn't there.
  *Focus:* focus is never placed inside a tuning block; the
  region is `aria-busy="true"` until resolved. *Active:* the
  retry button, in the failed state only. *Scrolled-past:*
  tuning continues off-screen (cheaply — shimmer pauses for
  off-screen blocks via the shared loop's visibility check).
  *Disabled / no-JS:* never armed. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: full-shape skeletons.
  768–1199px: same shapes, shimmer 1800ms. <768px: text bars
  reduce to two per block (a small room tunes quietly), cycle
  2000ms.
- **Edge cases & failure modes (v2).** *Instant content (cache):*
  if resolution beats the first shimmer frame, no skeleton is
  shown at all — a flash of tuning is worse than none (the
  150ms rule: skeletons arm only for waits longer than 150ms).
  *Partial failure (3 of 4 cards arrive):* the three light up;
  the fourth tunes to its ceiling and apologises alone — the
  room opens with one chair missing and says so. *Retry loop:*
  two failed retries replace the button with the house's
  direct line (§12) — the band stops tuning and the manager
  comes out.
- **Accessibility spec (v2).** Regions are `aria-busy` while
  tuning and announce once on resolution ("Tonight's tables
  are ready") via a polite live region — never per block.
  The skeleton bars are `aria-hidden`. The apology state is
  real text with a real button, ≥44px. Contrast of the tuning
  words: `--pencil` on `--club` 6.29:1.
- **Tokens consumed (v2).** `--smoke`, `--candle`, `--pencil`,
  `--club`, `--ease-haze`, `--ease-dim`, `--dur-shimmer`
  (1600ms), `--dur-lightup` (400ms), `--dur-watchdog-load`
  (3000ms).

### 6.18 Last orders

- **What & why.** The footer is the night ending: the house
  lights come *up* a fraction — the room brightens just enough
  to find your coat by — the final set-list check is drawn
  (§6.9), the evening's credits are read out (who played, who
  poured, who keeps the house), and the closing line is printed
  in the house's own words. It belongs because a Velvet Note
  page must *end* the way the evening ends: not with a sitemap
  in a grey band, but with the lights changing and the room
  saying goodnight. It is also the theme's proof of §4's
  running order — the page that began in darkness ends in
  slightly kinder light.
- **Structure.** A `<footer>` on `--club` with its lighting
  raised: a `--cream` wash at 4% and the velvet at its
  brightest printed state, so the footer is measurably (not
  dramatically) lighter than the room above it. Contents: the
  credits (acts from the bill's data §6.3, the house's staff
  lines, the site's colophon — built with the theme, one
  line), the practical tail (address, hours, the way home —
  real information, set plainly), the legal line in fine
  print, and the closing line in Italiana 22px: *"The Velvet
  Note keeps its own hours."* (§12's fixed string — on a real
  build, the house's own name replaces the theme's.) The final
  set-list check (§6.9) is drawn by this section's arrival.
- **Motion spec.** Trigger: the footer's top entering the
  viewport. The brighten: 1600ms `--ease-dim` in reverse — the
  wash fades in, the haze drift slows ×2 (§6.5), the spotlight
  lifts and widens until it is no longer a cone but the room's
  general light, and parks. The final check draws (300ms,
  §6.9). The tally (§6.16) freezes. Nothing else moves: last
  orders is the stillest moment on the page, and its stillness
  is the point — the band has stopped.
- **States.** *Before arrival:* the room at club level, footer
  unlit like everything else. *Arrived:* brightened state,
  held. *Scrolled back up:* the brighten *stays* (you cannot
  un-end the evening by walking back to your table — but the
  spotlight resumes its programme for the sections above; the
  footer's own wash is permanent for the visit). *Subsequent
  pages:* each page has its own last orders; the ceremony is
  per-page, not per-session.
- **Content merge.** The credits are the evening's real data
  (the bill's acts), the practical tail is the business's real
  facts, and the brighten is the room's own lighting rig
  (§6.2's cone, §6.5's haze) performing its final state — the
  footer is the choreography's last beat, not an appendix
  after it.
- **Failure fallback.** No JS: the footer prints in its
  brightened state (the wash is a printed gradient the JS only
  *animates in*) — the page ends kindly lit regardless. Loop
  stall: the wash snaps in via the 1200ms reveal watchdog; the
  final check prints whole.
- **Reduced-motion variant.** The footer prints brightened; no
  lift, no slow-down, the final check whole. The evening ends
  by simply being at its end.
- **Performance budget & mobile variant.** One gradient wash +
  state changes on existing layers; ≤1KB incremental. Mobile
  (<768px): brighten 1200ms, credits stack, the closing line
  at 19px.
- **Choreography timeline (v2).** Footer top enters → t=0
  brighten begins (1600ms) + haze slows → t=300 final check
  draws → t=800 cone fully widened to room light → t=1600
  brighten lands; tally frozen; the room rests — the page's
  last motion is §5's grain breath, which continues, because
  the building itself is still warm.
- **State matrix (v2).** *Rest (unvisited):* unlit footer.
  *Hover:* links warm per §11; nothing else. *Focus:* brass
  outlines; the brighten does not depend on focus. *Active:*
  n/a. *Scrolled-past:* n/a (it is the end). *Disabled /
  no-JS:* printed brightened. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: credits in three columns,
  closing line 22px. 768–1199px: two columns. <768px: one
  column, brighten 1200ms, closing line 19px.
- **Edge cases & failure modes (v2).** *Short page (footer
  visible at load):* the brighten plays once as part of the
  entrance (the evening was short; it still ends properly) —
  §13's map notes the merged beat. *No bill data (a dark
  night):* credits print the house lines only; the closing
  line remains — a closed club still says goodnight on its
  door. *Footer links many:* the practical tail caps at two
  columns of links; the sitemap belongs to a utility page,
  not to last orders (§11 refuses the mega-footer).
- **Accessibility spec (v2).** `<footer>` landmark; credits as
  a list; the closing line is text, not an image. The brighten
  never drops contrast: text is `--cream`/`--cream-dim` on
  `--club` throughout, and the wash *raises* effective
  background lightness by 4% — re-measured at the gate (§10) to
  confirm every footer pairing still clears its §2 floor.
- **Tokens consumed (v2).** `--cream`, `--cream-dim`, `--club`,
  `--velvet`, `--pencil`, `--ease-dim`, `--dur-brighten`
  (1600ms), `--dur-check` (300ms).

## 7. Page application map

**Home (the full evening).** The complete running order (§4):
door (§6.12) → bandstand (§6.11) with the bill (§6.3), the sign
(§6.4) and the tally (§6.16) → first set (the house's story, its
candles §6.7) → interlude (§6.6) → second set: tonight's tables
(§6.13) and the drinks list (§6.14) → the ledger (§6.15) → last
orders (§6.18). All 18 elements appear; the home page is the
theme's reference build, and §13 maps its scroll beat by beat.

**Listing (a season of nights, a roster of acts).** The tables
grid (§6.13) generalises: each entry is a card with a candle, a
state and a seal-able action. A season page lists nights the way
the home lists tables — the bill (§6.3) becomes the *next*
night's bill, pinned beside the bandstand; the set list (§6.9)
becomes the season's running order (months as sets). Filters
are the door's chips (§11). The interlude (§6.6) appears once,
at the list's midpoint, only if the data names a featured act —
otherwise the listing omits it rather than decorating a gap.

**Detail (one act, one night, one table).** The bandstand
(§6.11) shrinks to a half-stage (60vh, pin +30vh) headlining the
single act; the cone's travel crosses the act's own line-up.
The bill becomes *that night's* bill. The ledger (§6.15) is
pre-chosen to the act's night. The trumpet line (§6.6) is
permitted here only for the act's own signature tune — a detail
page for the drummer does not get the trumpeter's solo (§9).

**About (the house's history).** The room at its most printed:
haze (§6.5) and candles (§6.7) carry the atmosphere; the
spotlight (§6.2) travels slowly between eras (sections named
for decades, each with its candle). No ledger — a history page
that sells has misunderstood itself — but the door (§6.12) and
last orders (§6.18) hold, and the credits in the footer name
the founders as the evening's first act.

**Contact / the house's door (utility).** The ledger's pattern
(§6.15) without the booking data: name, subject as a select of
the house's real departments, the writing line. The page is
short; §6.18's brighten may be visible at load (§6.18's merged
beat) and that is correct — a utility page is all last orders.

**Checkout equivalent.** There is none, deliberately: the
ledger (§6.15) *is* the conversion, and anything beyond it
(payment for a private hire) leaves the theme's room for a
plain, bright, trustworthy payment page linked from the ledger
— the club takes your name at the bar; the bank does its
business in daylight. A build that themes a card-payment form
as a candlelit ledger has put atmosphere where trust should be
(§9, §10).

## 8. Worked examples

### 8.1 The hero — "Friday at the Velvet Note" (the bandstand)

The build's first screen, end to end. The club is fictional but
plausible: **The Velvet Note**, a basement room; tonight's
headline act is the **Marlowe Quartet**; the late set is
**Adaeze Cole, piano, from midnight**; doors 20:00; sets 21:30
and 00:15. The DOM ships complete: door (§6.12) with the plate
"THE VELVET NOTE" and tonight's strip reading "First set ·
Marlowe Quartet · 21:30"; the bandstand (§6.11) with the sign
(§6.4) as `<h1>`, the headline "THE MARLOWE QUARTET" printed at
rest light, the line-up at the rail — HORNE · PIANO · DRUMS
(the quartet's three named chairs plus the leader, printed as
the house prints them), the standfirst ("A basement room, a
standing band, and the last of the summer's cherries in the
bar") and the doors line. The bill (§6.3) sits at the rail's
right with tonight's five items; the tally (§6.16) prints IN
THE HOUSE 96 · TABLES KEPT 5 · SETS PLAYED 0.

*Scroll timeline.* Load: §6.1's dim settles 1800ms; the sign
warms from t=1650 (≈1400ms); the cone widens over the headline
1400ms and glints the rail; the bill glides at t=1900; the
tally counts at entrance-complete (1200ms, house first). First
scroll: the pin's 60vh scrubs the cone horn→piano→drums, 20vh
a beat; at the pin's end the late set's line cross-lights in
the bill's position — the evening's second fact. Release: the
spotlight swings 900ms down to the first table of the story
section, whose candle takes attended (§6.7), and the set list
(§6.9) warms "First set". A keyboard visitor tabs from the door
straight to the bill's first item; the scrub completes to that
beat instantly, and nothing in the sequence was ever between
them and the words.

### 8.2 Mid-page — the interlude and the second set's opening

The page's midpoint, where lesser themes put a testimonial
carousel. Here: the interlude section. Its printed content is
the interval's real business — "The bar pours through the
interval. The second set begins at 00:15." — and the drinks
list's green-bottle note. Above the text, the staff: five
`--smoke` rules and Marlowe's line for "Blue Hour", the tune
the bill (§6.3) names as the interlude solo — one data source,
three appearances (bill, caption, tally of sets), all agreeing.

*Scroll timeline.* The first set's last table scrolls past;
its candle deepens to ember (600ms) as the cone leaves it. The
interlude's top crosses 65%: the cone swings 900ms to the
staff's start and rests. 200ms later the line draws — 2400ms
at the melody's own tempo, the cone's heart following the draw
head — and the final note settles with the 180ms stamp. Below,
the interval text was readable the whole time (it never waited
for the music). Scrolling on: the cone leaves the line standing
complete, swings to the tables grid (§6.13), and the grid's
candles take attended in light order, 120ms apart, as the set
list checks "Interlude" — no, it does not: the interlude is a
line space in the list (§6.9), and the next check drawn is the
second set's, when its heading crosses the upper third. The
distinction is the theme in miniature: the pencil records
sets; the solo was between them, and the list's gap is its
record.

### 8.3 Conversion — keeping Table 4 (the ledger)

The visitor has flipped Table 4's card (§6.8) — "Table 4, the
alcove, seats four" — and the card's back reads "Held until
21:30 — the ledger confirms." The ledger (§6.15) sits below
the grid, pre-chosen: Table = Table 4 (from the card), Time =
the set list's remaining sets (21:30 is past its hold logic;
the form offers 00:15, the late set — a held table is held for
the *next* set, and the form's options are tonight's data, so
it cannot offer a set that has played). The visitor writes a
name — "R. Okafor" — and a party of four on the tally stepper.
One error on the way: the party stepper is bumped to nine; the
row prints, in the house voice, "The alcove seats four — for
more, the ledger can write two tables together" and offers the
pairing as a button, not a dead end (§12's error law).

*Scroll/submit timeline.* Arrival at the ledger: the cone parks
on the seal point; the first field's ember is lit. Focus warms
each rule in turn. Submit: the seal stamps (140ms) before the
request resolves; rows settle at 40ms; the confirmation writes
in at 90ms stagger — "Entry № 214" (the ledger's printed sample
page ends at № 213; the number is counted, not generated), the
entry in full, and the line "The table is kept. A note is on
its way to R. Okafor." Above, without any scroll, Table 4's
card shows its sealed back and the tally's TABLES KEPT
re-counts 5→6 with a pencil tick. If the request had failed,
the seal would have faded at 4000ms and the form stood filled,
with the house note (§11) doing the apologising — the guest is
never the one who pays for the house's mistakes.

## 9. Anti-slop — what makes THIS theme look cheap

1. **Deco pastiche.** Gold chevrons, sunburst clip-art, Gatsby
   lettering, a saxophone silhouette in the hero. *Cure:* the
   theme is a room, not a poster (§1). The only ornaments
   permitted are the house's own: the seal, the fleuron on the
   drinks list, the curtain's folds. If an element could hang
   in a themed party shop, it fails.
2. **The whiteout's dark twin — the blackout.** Sections left
   genuinely unreadable "for mood": text at 40% opacity, images
   crushed to silhouettes, the cone as the *only* light. *Cure:*
   §1's law with §2's measured floors — the printed layer is
   always fully legible; light is added, never withheld. Test:
   disable every lighting layer; the page must read perfectly.
3. **Neon-sign kitsch.** The warming sign (§6.4) pushed into
   pink-and-cyan neon, buzzing flicker, glow everywhere.
   *Cure:* the sign warms in brass and candle only, flickers
   twice at most per letter, and its glow is removed at rest.
   This club's electricity is old and warm, not Vegas.
4. **Everything glowing at once.** Three candles leaned, two
   cones, a lit tally, a glinting rail — the fairground failure.
   *Cure:* §2's light budget, enforced by §6.7's single-light
   rule and counted at the gate (§10): one cone, one leaned
   candle, the door lamp. Restraint is the luxury.
5. **Invented numbers.** A house count typed for atmosphere, a
   "№ 214" hardcoded, set times that disagree between the bill
   and the list. *Cure:* §1's second law — every figure traces
   to printed data; §6.16 exists to audit it, and §10's
   figure-truth check compares the bill, the list, the tally
   and the ledger mechanically.
6. **Prices that perform.** Counting, ticking or flashing
   prices in the drinks list. *Cure:* §6.14 — print is still;
   a price that moves is a price you don't trust.
7. **The script-font pencil.** Set-list checks and ledger
   marginalia set in a handwriting font, all curls and
   classroom. *Cure:* §3 — italic Jost in `--pencil` stands in
   for the hand; the *marks* (ticks, rules) carry the
   hand-kept feeling, the letterforms stay the house's.
8. **A second solo.** Trumpet lines on three sections, a staff
   behind the footer, notation as wallpaper. *Cure:* §6.6 is
   once per page, at the interlude, naming a real soloist from
   the bill. Music used as texture is the theme lying about
   what it values.
9. **Costume copy.** "Step into the roaring twenties, old
   sport!" — pastiche prose in a fake period voice. *Cure:*
   §12's registers: the Host is warm, brief and modern-grammared;
   the period lives in the room's objects, not in thee-and-thou
   copywriting.
10. **The themed payment form.** Card details taken by
    candlelight in a "ledger". *Cure:* §7 — payment leaves the
    room for a plain bright page. Atmosphere ends where other
    people's money begins.
11. **Haze as dirt.** Haze layers at 20% alpha, grey and flat,
    reading as a dirty screen over the text. *Cure:* §6.5's 9%
    ceiling over any reading line, warmth in the gradient, and
    total removal under reduced motion and house-lights.
12. **The endless dip.** Dip-to-black on every link including
    anchors and downloads, holds stretching past the load.
    *Cure:* §6.10's rulings — internal rooms only, the 3000ms
    watchdog, the candle instead of a spinner, and instant
    navigation under reduced motion.

## 10. Quality gate

Blocking checks — the theme may not ship with any one failed:

1. **Lights-up test.** All lighting layers (dim, cone, haze,
   glows) disabled: the page is complete and fully legible,
   every pairing at its §2 floor. (The §1 law, mechanically
   checked.)
2. **Figure-truth audit.** Bill (§6.3), set list (§6.9), tally
   (§6.16), ledger options (§6.15) and table states (§6.13)
   agree exactly — sets, times, counts, entry numbers derived
   from the DOM, none hardcoded twice.
3. **Light census.** At five sampled scroll positions: exactly
   one cone, at most one candle above `--lean` 0.7, absinthe
   objects ≤2 per page (§2).
4. **Contrast at rest and in motion.** §2's pairings verified
   at rest, mid-dim (§6.1), mid-swing (§6.2) and in the footer's
   brightened state (§6.18) — no frame of any animation may
   drop a text pairing below its floor.
5. **Watchdog drill.** Loop frozen by hand: hero dim clears
   ≤2600ms, pin releases ≤4000ms, any dip clears ≤3000ms,
   skeletons apologise ≤3000ms — the room always returns to a
   readable state unassisted.
6. **No-JS pass.** The whole evening readable and bookable
   (via §6.15's plain form) with JavaScript off; skeletons
   never armed; the sign lit; the bill placed.
7. **Reduced-motion pass.** `prefers-reduced-motion` yields
   the finished, lit, static room: no dim, no travel, no flip,
   no shimmer, no dip — and no content missing that motion
   would have brought.
8. **Easing census.** Grep: only the five named easings
   (§5) appear; durations only from the §5 ledger.
9. **Interlude discipline.** Exactly one trumpet line (§6.6),
   at the midpoint, naming a soloist who is on the bill; the
   sign (§6.4) is the only kinetic type; marquees: zero.
10. **CLS & frame budget.** Resolving skeletons shift nothing
    (§6.17); the shared loop holds 60fps with cone + haze +
    one candle active on a mid-range phone; page weight inside
    §14's budget.
11. **Forced-colors pass.** In forced-colors mode the page
    reads as its own fallback (§2): no glow, cone or haze
    survives, and no information was carried by them.
12. **The regular's test.** A second visit in the session: no
    dim, no warm-up, no bill glide — the room simply lit, the
    reserved card (§6.8) still sealed. A theme that performs
    its entrance at a regular has misunderstood hospitality.

## 11. Component inventory

Every component a real Velvet Note site needs, with its themed
treatment — or its refusal and the in-theme replacement.

- **Buttons.** Primary: a brass plate — `--brass` ground,
  `--club` text (8.12:1), Jost 500 tracked capitals, 2px radius
  (brass is stamped, not rounded); press dips 1px with the
  `--ease-stamp` snap. Secondary: a ghost rule — transparent,
  `--cream` text, 1px `--brass` underline that warms on hover.
  There is no third button style; the house pours two measures.
- **Inputs.** Ledger lines (§6.15): bottom rule only, `--cream`
  text, rule warms to `--brass` on focus. A boxed input is a
  form from an office; the house writes in a book.
- **Selects.** The ledger's select (§6.15) styled as a ledger
  row; its open list is a cream card (the bill's paper) with
  club ink — dropdowns in this room are printed slips.
- **Steppers.** Party size by tally marks (§6.15): groups of
  five, the fifth struck through, in `--pencil`; +/− are 44px
  brass-text buttons ("one more", "one fewer" in the aria-label,
  never bare glyphs alone).
- **Cards.** The table card (§6.13/§6.8) is the only card
  pattern. Generic content cards are refused — a section is a
  table with a candle (§6.7), not a card in a grid.
- **Tables (data).** The drinks list (§6.14) is the pattern:
  ruled rows, dotted leaders, brass-ink prices on cream, or —
  on dark grounds — `--cream` rows with `--brass` numerals and
  pencil rules. Zebra striping is refused (the ruling is the
  rhythm).
- **Badges.** One only: the state word on a table card ("Free
  tonight" / "Kept", §6.13) as plain text with its lamp dot.
  Pill badges are refused — the house does not pin labels on
  its furniture.
- **Alerts / the house note.** A note from the house: a small
  cream slip (the bill's paper) gliding in at the screen's foot
  (380ms `--ease-glide`), the message in the Host's voice
  (§12), dismissed by a brass "Very well" or by its own 6s
  timer for non-critical notes; critical notes (a failed
  booking) stay until answered. This is the toast's replacement
  — same contract, the room's paper.
- **Modals.** Refused as a pattern. The one permitted overlay
  is the door panel (§6.12) — a place, not a dialog. A
  confirmation that would be a modal becomes a ledger state
  (§6.15) in place.
- **Tabs.** Refused. A page with two evenings (tonight /
  tomorrow) prints two bills, one under the other — the room
  does not hide a night behind a tab.
- **Accordions.** Permitted once, for the house's questions
  (FAQ): rows ruled like the list (§6.14), opening at 320ms
  `--ease-swing` with the answer's candle (a 6px ember) lit
  while open. Anywhere else, refused — content in this room is
  on the tables, not folded inside them.
- **Pagination.** "The earlier sets" / "The later sets" as two
  ghost-rule links (§11 buttons) with the evening's position in
  words ("Sets 4–6 of 11"). Numbered page pills are refused —
  nobody in a basement asks for page three.
- **Breadcrumbs.** Refused. The door (§6.12) and the set list
  (§6.9) already say where you are; a third wayfinding system
  is a corridor with three signs.
- **Progress bars.** Refused (§6.9 is the progress). A bar may
  appear only inside the ledger's submit as the pencil line
  (§6.15) — a drawn line, not a filled track.
- **Spinners.** Refused absolutely. Waiting is the dip's candle
  (§6.10) or the tuning band (§6.17).
- **Tooltips.** A small cream slip, the bill's paper, appearing
  300ms after hover/focus, club ink, one line, gone on leave.
  Used for the seal's meaning ("The house seal — a kept table
  is a kept promise") and nowhere frivolous.
- **The bookplate (image plate).** Photographs sit in brass
  frames with a printed caption plate beneath (name + one line,
  §6.13's alt discipline) — the frame is 1px `--brass` at 60%
  with a worn corner highlight; a frameless photo is a photo
  from daylight.
- **Divider.** The brass rail (§4) or the fleuron (on cream
  paper only, §6.14). Gradient hairlines are refused — the
  room's lines are metal or print.
- **The house-lights toggle.** §6.12's button: the inventory
  lists it because every build needs it — labelled in words,
  `aria-pressed`, persisted, and honoured by every lighting
  element without exception.

## 12. Content & copywriting voice

Two registers, kept apart as strictly as the bar and the
bandstand.

**The Host** — spoken warmth: confirmations, errors, empty
states, the house note. Warm, brief, unhurried; modern grammar
with period *manners*; never costume slang, never "old sport".
The Host speaks in short sentences and takes responsibility in
the first person plural — the house, not the system.
- ✓ "That table was kept a breath before yours. The rail is
  open, or the ledger can write to the house for tomorrow."
- ✗ "Oops! Table unavailable. Please try again later."
- ✓ "The alcove seats four — for more, the ledger can write
  two tables together."
- ✗ "Error: party size exceeds maximum capacity for selection."

**The Bill** — printed matter: headings, labels, the list, the
set list. Names, not sentences (§3 law 1); times in 24-hour
tabular; prices without apology or decoration.
- ✓ "Second set — Adaeze Cole, piano · 00:15"
- ✗ "Don't miss the amazing second set starting at 12:15 AM!!!"
- ✓ "Doors 20:00 · First set 21:30"
- ✗ "Doors open at 8 PM and the show will begin around 9:30!"

**Error law.** An error names the fact, offers the nearest
true alternative, and never blames the guest. If no alternative
exists, it offers the house itself (a way to write to a human).

**Empty-state law.** An empty thing in this room is a *quiet*
thing, stated plainly: the unbooked night ("No tables are kept
yet — the evening is young"), the dark night ("The house is
dark on Mondays. The bill returns Tuesday."), the failed search
("No table seats six tonight — the ledger can write to the
house"). Never an illustration of emptiness; the room is the
illustration.

**Fixed strings (verbatim, never paraphrased).**
- The house rule, on the drinks list (§6.14): *"No requests
  after midnight. The band knows what you need."*
- The closing line (§6.18): *"The Velvet Note keeps its own
  hours."* (On a real build the house's own name stands in the
  theme's place; the sentence's shape does not change.)
- The seal's promise (§6.8's tooltip, §11): *"A kept table is
  a kept promise."*
- The tuning line (§6.17): *"The band is tuning."*
- The ledger's writing state (§6.15): *"Writing…"* — never
  "Processing", never "Please wait".

**Headline law.** Headlines are the names of acts, sets and
rooms (§3 law 1). If a page cannot name its sections, it has
not decided what its evening is — fix the evening, not the
type.

## 13. Full-page scroll choreography map

The home page (§7), top to footer — every beat in order, what
the visitor sees and feels. All scrubbed beats ride the one
shared loop (§5); all timed beats carry §6's watchdogs.

1. **The stairs.** The street-bright dim settles 1800ms
   (§6.1); the room assembles beneath it, complete from the
   first frame. *Feels like:* coming in out of the light.
2. **The name warms.** The sign catches letter by letter
   (§6.4) as the dim's tail overlaps; the cone widens over the
   headline (§6.11) and glints the rail. *Feels like:* the
   band seeing you arrive.
3. **The bill is placed.** The card glides in at the rail's
   right (§6.3); its items settle one by one; the first set's
   dot glints. The tally counts (§6.16) as the entrance
   completes. *Feels like:* being handed the evening.
4. **The set plays.** Scroll pins the bandstand for 60vh; the
   cone crosses horn, piano, drums (§6.11/§6.2); the late
   set's fact cross-lights at the pin's end. *Feels like:*
   staying for one more song than you meant to.
5. **To the tables.** Release; the cone swings 900ms to the
   first story section; its candle takes attended (§6.7); the
   set list warms "First set" (§6.9). Unlit floor passes
   beneath — the walk between tables (§4). *Feels like:*
   being shown to your seat.
6. **The first set.** Story sections pass candle to candle,
   one light at a time (§6.7's rule); haze crosses the beam
   (§6.5); the set list's first check is drawn as the second
   section's heading crosses the upper third. *Feels like:*
   the evening underway, kept by hand at the door.
7. **The interlude.** The cone rests; the trumpet line draws
   at its own tempo (§6.6); the interval's text is read by its
   light. A line space in the set list. *Feels like:* the room
   listening.
8. **The second set.** The tables grid (§6.13): candles take
   attended in the cone's order; a card flips and seals (§6.8)
   if the visitor chooses; the tally's TABLES KEPT re-counts
   with a pencil tick (§6.16). Then the drinks list (§6.14),
   its paper warming as the cone arrives; after midnight, the
   house rule's pencil underline. *Feels like:* deciding, and
   the room approving of the decision.
9. **The ledger.** The cone parks on the seal point (§6.15);
   the visitor writes; the seal stamps; the entry number
   counts its honest one or two; the confirmation stands in
   the book. *Feels like:* a promise made in writing.
10. **Last orders.** The footer's brighten lifts the room
    (§6.18); the haze slows; the cone widens into general
    light; the final check is drawn (§6.9); the credits are
    read by kinder light. *Feels like:* finding your coat,
    unhurried, while the band's last note is still in the air.

**Reverse pass.** Scrolling up: candles release in reverse
order, the cone follows back at the same 900ms, checks stay
drawn (the evening does not unhappen, §6.9), the bandstand
re-pins and un-plays its scrub honestly. Nothing on the way up
is a different animation from the way down — the room has one
set of manners.

**Jump scroll.** Anchor, scrollbar drag or find-in-page: the
cone cross-fades between points (300ms, §6.2), pending checks
draw in one 60ms-staggered pass (§6.9), candles settle at
their position-true states — the room composes itself at the
new position without pretending you walked there.

**Short page.** If the footer is visible at load, beats 3–10
compress: the entrance runs (1–3), the interlude draws if its
trigger is met, and last orders' brighten plays at the
entrance's end (§6.18's merged beat). The evening is short;
it is still an evening.

## 14. Whole-page performance budget

**Asset weight (home page, first load).** HTML + inline SVG
≤70KB (the seal, the staff path, the fleuron — all inline, no
icon font); CSS ≤38KB (the theme's full sheet, §11 included);
JS ≤30KB (the shared loop, the lighting rig, the ledger's
enhancements — no framework is admitted to a basement);
fonts: Italiana (1 weight) + Jost (3 weights), subset, ≤90KB
total, `font-display: swap` with §6.1's 800ms race as the
guard; images: duotone photographs ≤60KB each, ≤6 above the
fold's first scroll, the rest lazy (§6.13). **Page total
≤780KB**, of which the room (HTML/CSS/JS) is ≤140KB — the
photographs are the furniture, and even they are small, dark
and few.

**Frame budget.** The shared loop's per-frame work: ≤1.6ms
script, transforms/opacity only, zero layout reads inside the
loop (light points are cached on resize and on content change).
Cone + haze (3 layers) + one leaned candle + grain must hold
60fps on a mid-range phone (2021 class); two consecutive missed
frame budgets trigger §6.2's low-power ruling (cone parks, haze
drops to two layers, grain stops) — the room sheds atmosphere
before it sheds smoothness.

**Long tasks.** No task >50ms after load; the sign's split
(§6.4) and the tally's counts are the largest jobs and both are
sub-5ms. The ledger's submit path never blocks on animation:
the stamp is a transform, not a gate (§6.15).

**Cut order** (when the budget is exceeded, cut in this order,
never out of it): (1) the velvet grain breath; (2) the near
haze layer; (3) the candle pulse; (4) the cone's breath; (5)
photographs beyond the third (their velvet name-cards stand in,
§6.13); (6) the bandstand pin's travel (pin holds, scrub
becomes two beats). **Never cut:** the printed layer's
completeness, the watchdogs, the reduced-motion variants, the
house-lights override, the seal, the set list's text state, or
any contrast floor. Atmosphere is negotiable; the §1 law is not.

## 15. Build-order checklist

1. Print the room first: full DOM, all content, all data
   (bill, tables, list) from one source — no JS. Verify the
   lights-up test (§10.1) on this build before any lighting
   exists.
2. Tokens and type: §2's table as CSS custom properties, §3's
   scale and laws; the five easings and the durations ledger
   (§5) as tokens. Grep-gate them now, while there's nothing
   to cheat with.
3. The floor plan: §4's geography (door, rail, bandstand,
   tables, bar, last orders) and the unlit-floor spacing.
4. The door (§6.12) with the house-lights toggle wired to a
   stub lighting layer — the override must exist before the
   rig it overrides.
5. The bill (§6.3) and the data discipline: every later figure
   reads from it. Then the set list (§6.9) in its printed
   (no-JS) form.
6. The shared loop (§5) with its sleep/wake and low-power
   rulings, driving nothing yet.
7. The bandstand (§6.11) static; then its pin; then the cone
   (§6.2) parked; then the cone's travel. Watchdog 4000ms
   before the travel is allowed to be beautiful.
8. The entrance: dim (§6.1) and sign (§6.4) with their shared
   watchdog and the session flag; verify the regular's test
   (§10.12) immediately.
9. Candles (§6.7) with the single-light rule; sections become
   tables. Then haze (§6.5) — atmosphere last among the lights,
   because it is the easiest to overdo.
10. The interlude (§6.6), placed by the data, once.
11. The tables grid (§6.13) and the reserved card (§6.8);
    the no-JS ledger link path first, the flip second.
12. The drinks list (§6.14) with the house rule verbatim; the
    midnight underline last and optional.
13. The ledger (§6.15): plain working form first, then the
    seal, the write-in, the derived entry number. Then the
    tally (§6.16) wired to the real DOM states.
14. Tuning-up skeletons (§6.17) for genuinely-late regions
    only; dip-to-black (§6.10) between rooms, watchdog first;
    last orders (§6.18) as the choreography's final beat.
15. The full gate (§10), all twelve checks, signed by someone
    who did not build the page — the house's manager walks the
    room before the doors open, and it is never the band.
