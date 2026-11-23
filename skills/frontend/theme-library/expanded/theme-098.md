# 98. Tales by the Hearth — Expanded (v1 + v2)

**Identity (preserved from the original entry, deepened — never
redesigned).** Folklore told the way it was earned — seated around
a fire. The page is a dark cottage interior; stories are embers
that brighten as they are told, in woodcut illustration and
fireside pacing. Palette anchors: soot `#160F0A`, candlelit
parchment `#E8D9B8`, ember orange `#D97B2B`, hearth brick
`#7A2E1D`, moss green `#5A6650`. Type: Pirata One (tale titles,
sparingly — storybook blackletter) + Cormorant Garamond (the
tales themselves). A hearth glow breathes from below the
viewport; tales kindle as they near the glow zone; woodcuts carve
themselves stroke by stroke; chapter turns curl like a heavy
storybook leaf; progress is a log in the corner burning down;
between tales sits one empty chair, captioned only: *"For
whoever is telling it next."* No custom cursor — the original
entry's rule, kept.

## 1. Concept & world

Tales by the Hearth is the website of people who keep stories
the way cottages keep fires: banked, tended, and never left to
go cold. The world it performs is one room at night — a stone
hearth, a mantel with its objects, chairs drawn close, a heavy
storybook open on a knee — and the page's whole physics is the
physics of that room. Nothing on a Hearth page is revealed by
*appearing*. It is revealed by *warming*. A tale arrives the way
a tale arrives in a dark room: a voice begins, faces turn toward
it, and the story gathers light as it is told. Text begins
ash-grey and warms to candlelit parchment as it crosses into the
glow zone; the fire that lights it is stoked by the reader's own
first scroll, so arrival on this page is an act of hospitality —
the visitor lights the room the stories need, and the room, in
return, keeps every told tale warm behind them.

That warmth is the theme's entire economy, and it is spent
under discipline. The fire is at the bottom of the viewport and
it serves the reading line, which sits at 62% of the viewport
height: whatever is being read is fully candlelit — colour
temperature complete, embers settled, no flicker across the
words. Ahead of the reading line, tales wait in ash, dim but
printed, their titles visible as shapes in the dark the way
spines are visible on a shelf at night. Behind the reading line,
told tales stay warm; the page never takes light back from a
story that has been told. The hearth itself breathes — a radial
glow, slow and irregular, built from three layered cycles whose
periods (5.3s, 7.3s, 11.9s) never align into a visible loop,
because a fire that pulses on a beat is a screensaver and a
fire that breathes out of rhythm is a fire.

**The theme's one law: nothing glows that is not being read.**
Two clauses, both audited by the gate. (1) *Warmth follows the
reading position, and only the reading position.* The brightest
thing on the page at any moment is the text at the reading line
or the hearth that lights it. No decoration, badge, button or
background may out-glow the tale being read; ambient firelight
is capped at the `--glow-ambient-max` ceiling (§2) everywhere
except inside the hearth hero's scrubbed stoke (§6.1), and
every kindled state is JS-armed over complete printed content
with a watchdog that snaps it lit (§6.2), so a Hearth page with
dead JavaScript, a stalled loop or a flung scroll is a fully
lit, fully readable page — merely untold. A build in which any
sentence can be caught still ash-grey at the moment its reader
arrives has let darkness perform, and fails. (2) *Every ember
is accounted.* Ember particles are emitted from exactly two
sources — the hearth bed and the edges of a tale currently
being read, hovered or chosen — and their count is a finite
budget (§14), never a decorative weather system. An ember that
rises from nowhere, over a footer, a form field or a price, is
confetti in a cottage, and confetti is this theme's unforgivable
slop.

**Best-fit sites and audiences.** Folklore and fairy-tale
publishers first, literally: story collections, myth and legend
archives, oral-history projects. Children's story platforms that
want a bedtime register rather than a playground one — the
parent reading aloud is the audience, the child is the listener,
and the page's pace is a reading-aloud pace. Cultural heritage
and tourism: the storyteller's cottage, the village museum, the
ghost-walk and the fireside evening that can be booked. Fantasy
authors and world-builders whose books are told, not marketed.
A whisky distillery's tales page, a winter hotel's evening
programme, a storytelling festival. The common thread is a
business whose truth is *a voice in a dark room, and people
staying to listen*.

**When NOT to use it.** Never for anything that must be scanned
fast: documentation, dashboards, comparison tables, checkout
funnels where the visitor is in a hurry — the theme's pace is a
told pace, and hurrying it is a category error. Never for
daylight brands, clinical or corporate voices, or any site whose
content is primarily data: carved numerals and kindling text
will make a pricing grid feel like a séance. Never where the
audience reads in bright sun on a phone at noon — the palette
is a night palette and its contrast is engineered for dim
rooms (§2 states the bright-room ruling honestly). And never as
a skin over content that has no tales in it: if the site cannot
name its stories, the hearth is a fireplace showroom and the
theme will know.

**The evening is the unit.** A Hearth page is not a document,
it is one evening: the fire is lit (hero), tales are told
(sections), the log burns down (progress), chairs are taken and
one is left empty (the invitation), and at the end the fire is
banked for the night (footer). Every structural decision in
this expansion serves that arc, and §13 maps it beat by beat.

## 2. Palette

Five anchors from the original entry, seven derived tokens.
Contrast values below are measured (WCAG relative luminance)
for this expansion, not estimated.

| Token | Hex | Role | Ratio / pairing ruling |
|---|---|---|---|
| `--soot` | `#160F0A` | The room. Page ground, cottage dark. | Ground for all text below. |
| `--parchment` | `#E8D9B8` | Candlelit text, fully kindled tale body. | 13.60:1 on `--soot` — the body-text pairing, always. |
| `--ember` | `#D97B2B` | Firelight, lit letters, tallies, the log's burning edge. | 6.16:1 on `--soot` — text only ≥20px or bold; below that, accent only. |
| `--brick` | `#7A2E1D` | Hearth brick, card backs, washes, the form's hearth-stone panel. | 2.02:1 on `--soot` — **never text on soot**; a surface only. Takes `--parchment` text at 6.73:1. |
| `--moss` | `#5A6650` | The green outside the window: secondary panels, the chair's cushion, badges. | 3.12:1 on `--soot` — never text under 24px on soot; surfaces and large shapes only. |
| `--soot-deep` | `#0C0805` | The unlit corners. Footer bank, page-edge vignette, modal scrim base. | `--parchment` on it: 14.30:1. |
| `--parchment-cream` | `#F4EAD0` | Lit peaks: the hottest letter of a title mid-kindling, focus text on brick. | 15.83:1 on `--soot` — peaks only; a full paragraph in cream reads as glare. |
| `--parchment-dim` | `#B3A284` | Captions, standfirsts, secondary text, the empty chair's caption. | 7.61:1 on `--soot` — the smallest text allowed anywhere is dim, never ash. |
| `--ember-hot` | `#F2A950` | The glow's core colour, hover peaks, the log's lit tip. | 9.55:1 on `--soot` — may carry short labels ≥14px bold. |
| `--brick-deep` | `#4A1C10` | Hearth shadow, the inside of the fireplace, card-edge shade. | Surface only; never a text colour. |
| `--moss-pale` | `#9AA78D` | Text-safe moss: links and labels that must live in the green register. | 7.49:1 on `--soot` — the only moss that may set text on soot. |
| `--ash` | `#7A6C5C` | Unkindled text — the pre-read state, JS-armed only. | 3.73:1 on `--soot` — **forbidden at the reading line**; exists only ahead of it, over printed parchment (§6.2). |
| `--smoke` | `#241A12` | Haze layers, skeleton bars, the unlit chair's silhouette fill. | Surface only. |
| `--beam` | `#2A1A0E` | Mantel wood: nav shelf, footer beam, table frames. | Surface; takes `--parchment-dim` text. |
| `--iron` | `#3B2C1E` | Rules, borders, poker-lines, input underlines. | Hairlines only — 1px at ≥60% opacity reads as forged iron, thicker reads as mud. |

**Usage ratios.** Soot and soot-deep together hold ~78% of any
viewport — the room is dark or it is not this theme. Parchment
(text and lit surfaces) ~12%. Ember and ember-hot together are
capped at ~5% of pixels at rest: firelight is precious because
it is rationed, and a page that is 30% orange is a bonfire, not
a hearth. Brick ~3% (the hearth surround, panel backs). Moss
~2% — it is the colour of *outside*, and it enters the room
only in carried things: a cushion, a sprig on the mantel, the
green of a tale card's edge. Smoke and beam divide the rest.

**The glow is a colour, not an effect.** The hearth glow is a
radial gradient with three printed stops — `--ember-hot` at
18% opacity at the core, `--ember` at 10%, `--brick` at 5%,
fading to transparent — composited *under* the content layer,
never over text. Its resting intensity is capped by
`--glow-ambient-max: 0.55` (the gradient layer's opacity
ceiling outside the hero). Any build whose glow layer sits
above a text node, or whose resting opacity exceeds the cap,
has made a lamp out of a fire and fails the gate (§10).

**Dark-mode behaviour.** The theme *is* the dark mode; there is
no light scheme, and the expansion forbids inventing one — a
"candlelit parchment page" inversion (parchment ground, soot
text) is a different theme (a storybook, not a fireside) and
may be built separately, never toggled into. What the theme
does honour: `prefers-contrast: more` raises `--parchment-dim`
text to `--parchment`, freezes the glow at its cap's lower
third, and removes the ash pre-state entirely (tales ship lit).
The bright-room ruling, stated honestly in §9: on a phone in
full sun the page remains legible (13.60:1 body contrast is
not the problem) but the *mood* is lost; the theme accepts
this rather than lying about it with a light mode.

**Forbidden pairings.** Ember text on parchment (2.21:1 —
firelight does not print); brick text on soot (2.02:1); moss
text on soot under 24px (3.12:1); ash anywhere at or behind
the reading line; cream for body paragraphs (glare); any
colour outside this table — a blue link or a white button is
a window left open in winter, and the room notices.

## 3. Typography

Two families, as the original entry rules — no third family is
admitted, because a cottage has the voices it has. **Pirata
One** (400 only) is the storybook blackletter: tale titles, the
site's name on the mantel, chapter marks. **Cormorant Garamond**
(300, 400, 500, 600, 700 + italics) is everything else — the
tales themselves, and the room's working text. Cormorant's
old-style figures, carved (§6.10), are the theme's numerals;
there is no mono and no sans anywhere on the page, and tabular
data (the tally table, the seat count) is set in Cormorant 600
with `font-variant-numeric: tabular-nums` so columns hold.

**The scale** (root 16px; the fireside measure is narrow and
the type is large for reading aloud):

| Role | Font | Size / line-height | Tracking | Notes |
|---|---|---|---|---|
| Tale title (hero) | Pirata One | clamp(3rem, 8vw, 5.5rem) / 1.04 | 0.01em | One tale only — the evening's first. |
| Tale title | Pirata One | clamp(2.25rem, 5vw, 3.5rem) / 1.08 | 0.01em | Never below 2rem; blackletter under that is mush. |
| Chapter mark | Pirata One | 1.5rem / 1 | 0.04em | "The Second Tale", carved drop-caps pair with it. |
| Standfirst | Cormorant Garamond italic 500 | 1.375rem / 1.55 | 0 | `--parchment-dim`; the teller clearing their throat. |
| Tale body | Cormorant Garamond 400 | 1.25rem / 1.75 | 0.005em | The reading size. Measure 34–40ch (§4). |
| Listener text (UI, forms, nav) | Cormorant Garamond 500 | 1.0625rem / 1.5 | 0.01em | Labels, buttons, captions of the room. |
| Caption / colophon | Cormorant Garamond 500 | 0.9375rem / 1.5 | 0.02em | `--parchment-dim`; smallest text on the page. |
| Carved numeral | Cormorant Garamond 600 | role-sized / 1 | 0.03em | Ember-lit, knife-shadowed (§6.10). |
| Drop capital | Pirata One | 4.2em float / 0.78 | — | Opens each tale's first paragraph; carved, ember-rimmed. |

**Type laws.** (1) *Pirata One is rationed like firewood:* at
most three blackletter settings per viewport — the site name,
one tale title, one chapter mark. A page of blackletter
headings is a fancy-dress shop, not a cottage. (2) *Kindling
never moves type:* the warm-up (§6.2) animates colour and a
≤0.4px text-shadow bloom only — no size, weight, spacing or
position change, so a kindling paragraph has zero layout shift
and can be read mid-warm if the reader is quick. (3) *The
blackletter is never the only carrier:* every Pirata One title
is paired with a Cormorant standfirst that says what the tale
is, because blackletter at a glance is atmosphere, not
information — screen readers get the title as plain text
regardless (it is text, never an image). (4) *Italics are the
teller's aside:* Cormorant italic is reserved for standfirsts,
captions and quoted speech inside tales — never for buttons,
errors or prices; the room does not whisper its instructions.
(5) *Line-height is breathing room:* body at 1.75 because tales
are read slowly and often aloud; UI text at 1.5; nothing on the
page sets below 1.04, and that only in Pirata One display.

**Carved treatment.** Carved text (numerals, the mantel name,
chapter marks) carries a two-part shadow: a 1px `--soot-deep`
cut below-left and a 0.5px `--ember` rim above-right at 40% —
the letter looks knife-cut into wood and lit from the fire
side. The treatment is a token (`--carve`) applied by class,
never hand-tuned per element, and it is removed — flat
`--parchment` — under `prefers-contrast: more`.

## 4. Layout language

**The room is the grid.** The page is a cottage interior drawn
in layout: a hearth zone fixed to the bottom of the viewport
(the glow layer and, in the hero, the fireplace itself), a
mantel shelf across the top (the navigation, §6.11), and
between them the circle of chairs — the content column, centred,
narrow, and warm. Everything outside the column is room:
soot, vignette, the occasional mantel object or smoke layer at
parallax depth (§5). A Hearth page never fills the viewport
edge to edge with content; the dark around the text is the
room the reader is sitting in, and it is load-bearing.

**Measures and rhythm.** The tale column is 38ch maximum
(≈640px at the body size) — a storybook leaf, not a web page.
Listing and archive pages widen to a two-chair arrangement:
two columns of chapbook cards (§6.12) at ≥1200px, one at
<768px, never three — three chairs abreast is a waiting room.
Vertical rhythm is a 9px base unit; section spacing is 16
units (144px) on desktop — the pause between tales, long
enough for the teller to take a breath and the listener to
watch the fire — and 10 units (90px) on mobile. Within a tale,
paragraphs breathe at 1.75 line-height with 0.9em gaps; the
drop capital (§3) opens each tale and is the only float in the
theme.

**Depth.** Three depths, no more. Depth 0: the room (soot
ground, vignette, smoke at 0.3 parallax). Depth 1: the fire
(the glow layer, ember canvas, the hearth in the hero — 0.55
parallax, always *below* the reading line). Depth 2: the book
(content column, cards, forms — parallax 1.0, the only depth
that may hold text). Animated layers are `pointer-events:
none` and live at depths 0–1; nothing animated ever overlays
the book. The mantel nav is pinned to the top of the glass
(depth 3, the room's furniture) and is the only fixed element
besides the burning log (§6.6), which sits in the bottom-right
corner at depth 3 — inside the room, out of the book.

**Section choreography.** Sections alternate *tale* and
*room-beat*: tale, woodcut, tale, chair, tale, tallies. A
room-beat section (the chair, the tallies, the empty chair) is
shorter, darker at its edges, and holds no body text longer
than a standfirst — it is the pause in the telling, and its
emptiness is composed, not missing. The pinned chair scene
(§6.7) is the page's one long breath: 300vh of scroll at
desktop during which the room holds still and three tales pass
through the seat.

**Density rules.** One tale per section; one idea per card;
one form per page. Whitespace here is *darkness*, used as a
material: the gap between tales is where the fire is watched.
Any layout that needs a divider line has failed — tales are
separated by darkness and a carved chapter mark, never by a
rule. `--iron` hairlines appear only inside components (table
rows, input underlines, the log's bark edge), never as section
separators.

## 5. Full motion system

Every motion term from the standard list, in this theme's own
language. One shared rAF loop drives all scrubbed values with
lerp **0.085** — deliberately heavier than a typical 0.12,
because firelit drift is slow and a Hearth page that snaps is a
room with the door slammed. The loop owns: glow radius and
intensity, per-tale kindle progress, log burn length, parallax
offsets (three depths), chair-pin tale crossfades, curl
progress. Event-driven motion (hover, click, form) runs on CSS
transitions/animations off the loop. The loop sleeps when the
tab is hidden and when nothing is within 1.5 viewports of
motion; a watchdog (§6.2) guarantees final states if it stalls.

**Named easings** (tokens, used by every element — no element
invents its own curve):

- `--ease-kindle: cubic-bezier(0.22, 0.61, 0.21, 1)` — a slow
  gather, the way colour comes into cheeks near a fire.
- `--ease-stoke: cubic-bezier(0.16, 0.84, 0.3, 1)` — the
  scrubbed stoke; mostly superseded by the lerp, used for the
  hero's non-scrubbed beats.
- `--ease-curl: cubic-bezier(0.7, 0, 0.2, 1)` — heavy start,
  long settle: a thick leaf leaving the hand.
- `--ease-thunk: cubic-bezier(0.3, 1.6, 0.5, 1)` — the log
  jolt: 90ms, 4px, one overshoot, no bounce chain.
- `--ease-settle: cubic-bezier(0.34, 1.15, 0.4, 1)` — embers
  and stirred things coming to rest.
- `--ease-drift: cubic-bezier(0.4, 0.1, 0.6, 0.9)` — smoke:
  slow in, slower out, never symmetric.
- `--ease-bank: cubic-bezier(0.6, 0.05, 0.3, 1)` — banking:
  the long dim at the evening's end.
- `--ease-carve: cubic-bezier(0.5, 0, 0.15, 1)` — woodcut
  strokes: committed, unhurried, no reversal.

**The terms, applied:**

- **Scroll-triggered reveals** — kindling (§6.2): tales warm as
  they cross toward the reading line at 62% viewport height;
  full kindle over the 38% of viewport travel before the line.
- **Scroll-driven / scrubbed animation** — the stoked hearth
  (§6.1): the first 120vh of scroll *is* the stoking; glow
  radius, ember rate and headline warmth are functions of
  scroll position, reversible until the fire catches at 1.0.
- **Parallax** — three depths (§4): smoke 0.3, fire 0.55, book
  1.0; mantel objects in the hero drift at 0.7. Nothing textual
  parallaxes except the book itself, which does not.
- **Pinned sections** — the storyteller's chair (§6.7): the
  scene pins for 300vh while three tale summaries are told.
- **Masked reveals** — chapter turns (§6.5) reveal through a
  page-curl clip-path; tale cards (§6.12) kindle under a
  soft-edged radial mask centred on the hearth side.
- **Blur-to-sharp** — refused for text (a blurred tale is an
  untold one); used once, on woodcut plates (§6.4), where the
  deepest cuts resolve from 2px blur as they finish carving.
- **Staggered reveals** — ember-lit title letters (§6.3): 55ms
  stagger with ±18ms irregularity, lit along the line like
  embers catching one by one — a perfect metronome stagger is
  a machine, and the fire is not one.
- **Kinetic typography** — title letters warm individually
  (§6.3); the tallies' numerals roll carved (§6.10). No other
  type moves. Kinetic type anywhere else is a tale shouting.
- **Marquee** — refused. Nothing in a cottage scrolls sideways
  forever; the one horizontal motion allowed is smoke drift.
  A client who needs a ticker needs a different theme.
- **Counters** — carved tallies (§6.10): tales told since the
  last frost, listeners this winter, seats remaining — counted
  in the room's own arithmetic, from printed source values.
- **Progress indicator** — the burning log (§6.6): scroll
  progress as a log burning down, its lit length the reader's
  place in the evening.
- **SVG line-draw** — woodcuts (§6.4): strokes carve in order —
  outlines, hatching, deepest cuts — `stroke-dashoffset` on the
  shared loop's cousin, an IntersectionObserver trigger.
- **Image scale-in-frame** — refused for woodcuts (a carving
  does not zoom); chapbook card plates settle 1.04→1.0 over
  900ms `--ease-settle` as their card kindles — the one
  licensed scale, small enough to read as settling, not zooming.
- **Hover micro-interactions** — ember-stir (§6.8): tales and
  cards brighten +6% and lift 6–10 embers at their edges.
- **Magnetic / tilt** — refused. Objects in a cottage are heavy
  and stay where they are put; the one pointer response is the
  ember-stir and the glow's slight lean toward a hovered tale
  (≤24px gradient shift, `--ease-drift` 600ms).
- **Custom cursor** — refused by the original entry and by the
  standing rules. The system cursor, always.
- **Skeleton loading** — unlit shapes (§6.17): pending content
  is a `--smoke` silhouette of the thing coming — a chair shape
  for a tale card, a log shape for tallies — never a grey
  shimmer, which is daylight behaviour.
- **Page transitions** — smoke and a leaf (§6.17): a 500ms
  smoke drift across, the leaf turns, the new page kindles from
  its hero. Total ceiling 1200ms, abortable by any input.
- **Ambient loops** — exactly two: the fire's breathing (three
  layered cycles, §1) and rising embers from the hearth bed
  (canvas, §6.1). Both are capped, both pause off-screen, both
  die under reduced motion. A third ambient loop is slop.
- **Reduced motion** — the fire becomes a steady warm glow at
  resting intensity; no flicker, no rising embers, no curl, no
  stagger; tales ship lit; the chair scene unpins into a stack.
  The page loses its performance and keeps its meaning —
  §6 gives the variant per element, without exception.

## 6. Signature elements

### 6.1 The stoked hearth

- **What & why.** The hero opens on a cold hearth: a stone
  fireplace drawn at the bottom of the viewport, unlit, the
  room at `--soot-deep` near-black, the evening's first tale
  title printed above it in ash. The visitor's first scroll
  stokes the fire — ember particles begin to rise, the glow
  radial warms and widens, the title kindles (§6.3) — scrubbed
  to scroll position across the first 120vh, until at 1.0 the
  fire has *caught* and burns on its own breathing cycle for
  the rest of the page. It belongs because it makes the reader
  perform the theme's founding act: you do not arrive at a
  fireside, you light it. Every later element spends the warmth
  this one earns.
- **Structure.** A real `<h1>` (Pirata One) and standfirst,
  complete in the DOM at full `--parchment` contrast — the
  printed layer. The hearth is an inline SVG fireplace (stone
  surround in `--brick`/`--brick-deep`, iron grate in `--iron`,
  log shapes in `--beam`) seated in a hero section of 190vh
  whose inner stage is sticky for the first 120vh of travel.
  Above the printed layer sit two JS-armed overlays
  (`aria-hidden`, `pointer-events: none`): the *cold veil*, a
  `--soot-deep` field at 88% whose opacity is the stoke
  function's inverse, carrying a duplicate of the title in
  `--ash`; and the glow layer (§2's three-stop radial) fixed at
  depth 1. Embers are one `<canvas>` at depth 1, full-viewport,
  behind the book. No `backdrop-filter` anywhere: the cold is a
  duplicate, never a blur over live text.
- **Motion spec.** Scrubbed, not triggered: stoke progress
  `s = clamp(scrollY / (1.2 × viewportH), 0, 1)`, lerped at
  0.085 on the shared loop. Glow radius 30vmax→62vmax and glow
  opacity 0→`--glow-ambient-max` follow `s` on an ease-in curve
  (`s^1.4` — a fire is slow to catch, then generous). Ember
  emission rate 0→26/s follows `s^2`. The title's letters begin
  their ember-lit stagger (§6.3) at `s ≥ 0.55`. At `s = 1` the
  veil is removed from the DOM, the stage unsticks, and the
  breathing cycle (three layered periods 5.3s/7.3s/11.9s,
  ±6% radius, ±9% opacity, never synchronised) takes over the
  glow from the scrub — the handover is a 900ms `--ease-bank`
  blend so there is no visible seam between *stoking* and
  *burning*. Scrolling back above the hero before `s = 1`
  reverses the stoke honestly (an unstoked fire cools); after
  the catch, scroll position no longer affects the fire — a
  caught fire does not go out because the reader looked back.
- **States.** Cold (s=0, JS-armed only) → stoking (0<s<1) →
  caught (rest; breathing). Hover/focus: none — the hero is not
  a control. Focus entering the hero at any `s` completes the
  catch instantly (a keyboard visitor is never asked to stoke).
  Returning visitor (`sessionStorage` flag): the fire is
  already lit, breathing, veil absent — hospitality remembers.
- **Content merge.** The stoke lights the page's actual first
  tale title and standfirst — the hero *is* the evening's first
  story, not an intro screen before it. The fireplace SVG sits
  below the title in the same section, so the fire the reader
  lights is visibly the fire that lights the words.
- **Failure fallback.** Watchdog at 3000ms from
  DOMContentLoaded: if `s` has not reached 1 and the loop has
  not ticked, the veil is removed, the glow snaps to resting,
  embers start at base rate — the room is lit, merely unstoked
  by hand. No JS: the veil and canvas are never inserted; the
  glow layer ships at resting intensity as a static gradient;
  the title is simply the title. Slow network: hero is
  HTML-first; the stoke script is deferred and the watchdog
  runs from DOMContentLoaded, not from script arrival.
- **Reduced-motion variant.** No stoke, no scrub, no breathing,
  no rising embers. The hearth ships lit at resting glow — the
  original entry's rule: fire becomes a steady warm glow. The
  hero is 100vh, unstuck, complete.
- **Performance budget & mobile variant.** Canvas embers ≤90
  live particles desktop, each a 2–4px radial sprite drawn from
  one offscreen stamp (no per-particle gradients); glow is one
  composited layer animating `transform: scale` + `opacity`
  only. Hero JS ≤14KB. Mobile (<768px): stage 150vh, stoke
  distance 0.9 × viewportH, embers ≤36, glow radius cap 48vmax —
  the gesture reads at arm's length or it is cut, and here it
  reads.
- **Choreography timeline (v2).** t=0 (first paint): printed
  title at full contrast beneath the armed veil → scroll begins
  → s=0.15 first ember lifts from the grate → s=0.4 glow edge
  reaches the title's baseline → s=0.55 letter stagger arms
  (§6.3) → s=0.8 standfirst warms from ash (its own kindle,
  §6.2 curve) → s=1.0 veil removed, breathing handover 900ms →
  scroll continues into the first tale, already lit. Watchdog
  ceiling 3000ms cancels the ceremony, never the content.
- **State matrix (v2).** *Rest (caught):* breathing glow, base
  embers 8/s idle rate. *Hover:* none. *Focus:* focus within
  completes the catch. *Active:* n/a. *Scrolled-past:* fire
  stays caught; the hero left behind is lit. *Disabled /
  no-JS:* printed lit hero, static glow. *Touch:* identical
  scrub — touch scroll is the stoking hand; a fling that jumps
  past 120vh lands at s=1 via the lerp's catch-up cap (max
  0.34 progress per frame) and still reads as a catch, not a
  teleport.
- **Breakpoints (v2).** ≥1200px: hero 190vh, title 5.5rem,
  glow to 62vmax, embers ≤90. 768–1199px: 175vh, title 4.25rem,
  glow 54vmax, embers ≤60. <768px: 150vh stage, title 3rem,
  glow 48vmax, embers ≤36, fireplace SVG simplified (stones
  merge from 14 paths to 6 — the carving budget is spent on the
  tales, not the masonry).
- **Edge cases & failure modes (v2).** *Canvas unavailable:*
  embers fall back to 12 CSS-animated dots inside the hearth
  SVG itself — fewer, but the fire still rises. *Tab hidden
  mid-stoke:* rAF pauses; on return, wall-clock is ignored and
  the scrub resumes from scroll position (the fire waited).
  *Very tall viewport (>1100px):* stoke distance scales with
  viewportH, capped at 1320px of travel so the ceremony cannot
  become a chore. *Title edited in a CMS to two lines:* the
  veil's duplicate is generated from the live `<h1>` text at
  runtime, never authored separately — it cannot drift.
- **Accessibility spec (v2).** The `<h1>` is complete in the
  accessibility tree from first paint; veil, glow and canvas
  are `aria-hidden`. The stoke is never announced. Contrast is
  the printed layer's at all times — 13.60:1 — because the
  readable title is beneath, whole. The hero contains no
  focusable element until its standfirst link, which is
  reachable without stoking (focus completes the catch, above).
- **Tokens consumed (v2).** `--soot`, `--soot-deep`,
  `--parchment`, `--ash`, `--ember`, `--ember-hot`, `--brick`,
  `--brick-deep`, `--beam`, `--iron`, `--glow-ambient-max`,
  `--ease-stoke`, `--ease-bank`, `--dur-watchdog-hero`
  (3000ms), `--lerp` (0.085).

### 6.2 Kindling tales

- **What & why.** Every tale section kindles as it approaches
  the reading line: its text warms from `--ash` to `--parchment`
  — a colour-temperature journey through `--parchment-dim` —
  while a soft ember bloom gathers at its lower edge, nearest
  the fire. Kindling is the theme's reveal verb, the way
  *condensing* belongs to fog or *carving* to the woodcut: a
  story does not pop in, it catches. It belongs on every tale,
  card and standfirst on the page, and nowhere else — kindling
  is for stories, and a kindled button is a toy.
- **Structure.** The tale is printed complete at `--parchment`
  in the DOM. Over it, JS arms a *kindle overlay state* only:
  the section gets `data-kindle="0"` and a CSS custom property
  `--k` (0→1); colour is computed as a three-stop mix
  (`--ash` → `--parchment-dim` at k=0.55 → `--parchment` at
  k=1) via `color-mix`, with a duplicate-free structure — the
  text itself is tinted, never covered, so selection, find-in-
  page and screen readers meet the real words at every k. The
  ember bloom is a pseudo-element radial at the section's lower
  edge, opacity `k × 0.5`, `pointer-events: none`.
- **Motion spec.** Scrubbed on the shared loop:
  `k = clamp((readingLine − taleTop) / (0.38 × viewportH), 0, 1)`
  where readingLine sits at 62% viewport height — a tale is
  fully lit 38% of a viewport before its first line reaches the
  line, so the reader never watches the sentence they are
  reading change colour; they arrive at warmth. Lerp 0.085
  smooths flings; a jump-scroll that lands a tale past the line
  sets k=1 directly (the loop's catch-up: any tale whose top is
  above the line is lit, unconditionally, each frame). Once
  k=1 the tale is *told*: the property locks, the observer
  unobserves, and scrolling back up never un-kindles — warmth
  is kept (§13's ratchet). Duration is therefore positional,
  but at a reading scroll of ~55vh/s the warm-up spans ≈1400ms
  `--ease-kindle` equivalent — stated as `--dur-kindle` for the
  non-scrubbed fallbacks (focus, watchdog, reduced-motion-off
  toggles), which run the same journey in 1400ms.
- **States.** Unkindled (k=0, JS-armed only, ahead of the line)
  → kindling (0<k<1) → told (k=1, rest, locked). Hover: none of
  its own (§6.8 stirs embers around a told tale; an unkindled
  tale does not stir — it is not yet in the room). Focus: any
  focus landing inside an unkindled tale snaps it to k=1 in
  1400ms `--ease-kindle` (keyboard readers read lit text).
  Scrolled-past: told, forever.
- **Content merge.** Kindling is not applied *to* the tale from
  outside; the tale's own ink warms. The first tale on the page
  kindles inside the hero's stoke (§6.1); later tales kindle on
  the standard curve. Standfirsts kindle 120ms of k behind
  their title — the voice clears its throat after the face is
  lit — implemented as a k-offset, not a second system.
- **Failure fallback.** Watchdog: every armed tale carries a
  1600ms timer from when its top crosses 85% viewport height;
  if k has not reached 1 by then (loop stalled, observer
  unsupported), the timer forces k=1 and locks it. No JS:
  `data-kindle` is never set; every tale ships at `--parchment`.
  IntersectionObserver absent: the scroll handler's per-frame
  positional check (same formula) is the fallback path — the
  formula, not the observer, is the spec.
- **Reduced-motion variant.** No warming journey: tales enter
  at k=1. The theme keeps a *static* temperature geography
  instead — tales above the fold print parchment, and that is
  all; nothing ahead of the reader is ever left ash under
  reduced motion, because an unmoving ash state would strand
  content, which the law forbids twice over.
- **Performance budget & mobile variant.** One custom property
  per tale, composited colour only — no layout, no paint of
  anything but the tinted text itself. ≤6 tales armed at once
  (observer window); told tales cost zero. Mobile (<768px):
  reading line at 58%, kindle span 30% of viewport — a shorter
  room, a quicker catch — and the ember bloom pseudo-element is
  dropped (the tint alone carries it) to keep the paint budget.
- **Choreography timeline (v2).** Tale top at 100% viewport →
  k=0 → top crosses 85% → watchdog arms (1600ms) → top crosses
  the kindle span start (reading line + 38%vh) → k rises on the
  loop, title first (its own §6.3 stagger begins at the title's
  k≥0.5) → k=0.55 colour passes `--parchment-dim` (the tale is
  legible from here in an emergency — the watchdog's snap uses
  this as its floor check) → first line reaches the reading
  line at k=1 → lock, unobserve, bloom settles to rest 0.18.
- **State matrix (v2).** *Rest (told):* parchment, bloom 0.18.
  *Rest (unkindled):* ash tint over printed parchment —
  reachable only ahead of the reading line. *Hover:* §6.8.
  *Focus:* snap-kindle 1400ms. *Active:* n/a. *Scrolled-past:*
  told. *Disabled / no-JS:* printed lit. *Touch:* identical;
  touch flings use the same catch-up rule.
- **Breakpoints (v2).** ≥1200px: line 62%, span 38%vh, bloom
  on. 768–1199px: line 60%, span 34%vh, bloom on at 0.4 cap.
  <768px: line 58%, span 30%vh, bloom off.
- **Edge cases & failure modes (v2).** *A tale shorter than
  the kindle span* (a two-line tale): k is computed from its
  first line only; it kindles fast and that is correct — a
  short tale is a quick story. *A tale longer than 3 viewports:*
  kindling is per-section but the lock is per-section too — a
  very long tale's tail enters already warm because its head
  was told; this is intended (one telling, one fire). *Content
  injected late* (infinite scroll, CMS hydration): new tales
  arm on insertion via MutationObserver with the same formula;
  a tale inserted *above* the reading line ships told.
  *Reader at 200% zoom:* viewport-relative maths holds; the
  span shrinks in CSS pixels and kindles feel quicker — noted,
  accepted, never blocked.
- **Accessibility spec (v2).** Colour is the only animated
  property; the text is real text at every k, in the
  accessibility tree, unannounced (kindling is not an event a
  listener needs narrated). The ash state at 3.73:1 is a
  *pre-read* state only — the gate (§10) tests that no tale
  can rest at k<1 within the reading zone; told text is
  13.60:1. Under `prefers-contrast: more`, kindling is disabled
  and all tales print parchment (§2).
- **Tokens consumed (v2).** `--ash`, `--parchment-dim`,
  `--parchment`, `--ember`, `--ease-kindle`, `--dur-kindle`
  (1400ms), `--dur-watchdog-kindle` (1600ms), `--lerp` (0.085),
  `--reading-line` (0.62).

### 6.3 Ember-lit titles

- **What & why.** A tale's title lights letter by letter, as if
  a line of embers were catching along the baseline: each glyph
  warms from `--ash` through `--ember` to `--parchment-cream`
  at its peak, then settles back to `--parchment` as the next
  letter catches — the title is lit the way a row of candles is
  lit from one flame, in reading order, with the slight
  irregularity of real catching. It belongs because Pirata One
  blackletter is the theme's most precious material (§3 rations
  it), and precious things are lit ceremonially. The settled
  title is plain parchment — the ceremony leaves no residue.
- **Structure.** The `<h2>`/`<h1>` holds plain text. JS splits
  it into per-letter `<span aria-hidden="true">`s inside a
  wrapper that carries the whole title as its `aria-label` —
  the unsplit text remains the accessible title, and the split
  is rebuilt from the live DOM text at runtime (a CMS edit
  cannot desynchronise it). Spaces are preserved as normal
  spaces (words must still wrap and be selectable across the
  split; `display: inline-block` is refused on the spans —
  colour animates on inline boxes, so copy/paste stays whole).
  Peak glow is a text-shadow bloom (`0 0 18px --ember` at 55%),
  never a filter.
- **Motion spec.** Trigger: the title's tale reaches k≥0.5
  (§6.2), or the hero stoke reaches s≥0.55 (§6.1). Per letter:
  620ms `--ease-kindle` colour journey ash→ember (40%)→cream
  peak (62%)→parchment settle (100%), with the ember text-
  shadow swelling at the peak and dying by settle. Stagger
  55ms per letter ±18ms of seeded irregularity (seeded by the
  letter's index × 37 mod 41, so the pattern is stable across
  reloads — random flicker reads as a fault, patterned
  irregularity reads as fire). A 24-letter title completes in
  ≈2.0s. The sequence runs once per tale, ever; a told title
  never re-lights.
- **States.** Unlit (ash, JS-armed, only inside an unkindled
  tale) → lighting (the stagger running) → lit (rest,
  parchment, no shadow). Hover: none — titles are not controls;
  §6.8's stir answers hovering the *tale*. Focus: a title
  containing a link (archive cards, §6.12) lights instantly on
  focus — no keyboard visitor waits for a ceremony.
  Scrolled-past: lit.
- **Content merge.** The letters lit are the tale's actual
  name; the lighting order is the reading order, so the
  animation *teaches* the title as it performs it. On the
  archive page the same treatment marks the one featured tale —
  the rest of the shelf stays dim (§6.12) — so the ceremony
  also carries the page's hierarchy.
- **Failure fallback.** Watchdog 2600ms from trigger: any
  letter not yet settled snaps to parchment. No JS: no split,
  the title prints parchment like every heading. If the split
  itself throws (exotic glyphs, emoji in a title), the builder
  falls back to whole-title kindling (§6.2's tint) — the tale
  loses its ceremony, never its title.
- **Reduced-motion variant.** No stagger, no peaks: the title
  arrives with its tale at full parchment (which, under reduced
  motion, is immediately — §6.2). The ember peak is the first
  thing cut; it is pure ceremony.
- **Performance budget & mobile variant.** Colour + text-shadow
  on ≤28 inline spans per title, ≤3 titles lighting
  concurrently (a queue; the fire lights one row at a time).
  Mobile (<768px): stagger 42ms, peak shadow 12px — the same
  ceremony at arm's length. Titles over 28 characters are
  refused the split at build (§12) and kindle whole — a
  paragraph is not a row of candles.
- **Choreography timeline (v2).** Trigger (k≥0.5) → t=0 letter
  1 warms → each +55±18ms the next → a mid-title letter peaks
  cream at its 62% while its neighbours are ember and ash — the
  lit front travels → last letter settles → t≈2.0s title at
  rest parchment, shadows dead → the tale's standfirst begins
  its kindle (§6.2 offset). Watchdog ceiling 2600ms.
- **State matrix (v2).** *Rest:* lit parchment. *Hover:* none.
  *Focus (linked titles):* instant lit. *Active:* n/a.
  *Scrolled-past:* lit. *Disabled / no-JS:* printed parchment,
  unsplit. *Touch:* identical; no hover pre-state exists to
  stick.
- **Breakpoints (v2).** ≥1200px: stagger 55ms, peak blur 18px.
  768–1199px: stagger 50ms, blur 15px. <768px: stagger 42ms,
  blur 12px, and hero title capped at 3rem so 28 characters
  still fit the ceremony.
- **Edge cases & failure modes (v2).** *Title with a ligature
  or combining mark:* splitting is by grapheme cluster
  (`Intl.Segmenter`), never by code unit — a split that breaks
  a glyph breaks the tale's name, the one unforgivable typo.
  *Right-to-left titles:* the stagger follows reading order
  (logical order), so an RTL title lights right-to-left.
  *Title edited after split (live CMS preview):* the wrapper
  re-splits on mutation or not at all — a half-split title is
  worse than an unsplit one, so the observer rebuilds whole or
  leaves whole.
- **Accessibility spec (v2).** The accessible name is the
  unsplit title (`aria-label` on the wrapper, letters
  `aria-hidden`); screen-reader users hear the title once,
  whole, immediately — the ceremony is visual only. Colour
  contrast during the journey is irrelevant to conformance
  because the printed layer beneath the tint is the tale's
  real heading at 13.60:1 in the DOM order — no, precisely:
  the spans *are* the text, so the journey's worst moment (ash
  at 3.73:1) is transient, positional, and covered by the same
  reading-line guarantee as §6.2: a title never rests unlit
  where it can be read.
- **Tokens consumed (v2).** `--ash`, `--ember`,
  `--parchment-cream`, `--parchment`, `--ease-kindle`,
  `--dur-letter` (620ms), `--stagger-letter` (55ms),
  `--dur-watchdog-title` (2600ms).

### 6.4 Woodcut build-up

- **What & why.** Each tale's illustration is a woodcut, and it
  is carved in front of the reader: the SVG's strokes appear in
  the order a carver cuts them — the outline first, then the
  hatching that builds shadow, then the deepest cuts that hold
  the black. A finished woodcut is a printed plate in two
  colours (`--parchment-dim` line on `--soot`, deepest cuts in
  `--brick-deep` filled shapes) sitting in the tale column like
  a plate in a storybook. It belongs because the theme's images
  must be *made of the same night* as its text: a photograph in
  a Hearth page is a window left open. Carving is also the only
  image reveal whose process is the content — you watch the
  picture being earned.
- **Structure.** One inline `<svg>` per plate, authored in
  three stroke groups with classes `.cut-outline`, `.cut-hatch`,
  `.cut-deep`, each path carrying `pathLength="1"` so carving
  progress is a uniform `stroke-dashoffset` 1→0 per group. Deep
  cuts are filled paths whose fill fades in as their outline
  completes. The plate sits in a `<figure>` with a Cormorant
  italic caption (`--parchment-dim`) that names the scene —
  the caption is content, printed, never carved. The complete
  illustration is the DOM state: dashoffsets are JS-armed
  pre-states, so a no-JS page shows finished woodcuts.
- **Motion spec.** Trigger: the plate's figure crosses 70%
  viewport height (IntersectionObserver), once. Carving runs
  group by group: outlines 900ms `--ease-carve`, a 120ms held
  breath, hatching 1400ms `--ease-carve` (strokes within the
  group staggered 24ms in carving order — top-left to the
  fire side), a 120ms breath, deepest cuts 700ms with their
  fills rising over the final 300ms. As the deep cuts land, the
  whole plate resolves from a 2px blur to sharp (§5's one
  licensed blur) over 400ms. Total ≈3.5s. The carve is
  fire-and-forget: scrolling away does not pause it (a carver
  does not stop because you looked at the fire), and it never
  repeats.
- **States.** Uncarved (JS-armed dashoffset state, only ahead
  of the reading zone) → carving → printed (rest). Hover: the
  printed plate warms +4% brightness and its caption kindles —
  plates are looked at, not used. Focus: plates are not
  focusable unless they illustrate a linked tale (§6.12), where
  focus prints the plate instantly. Scrolled-past: printed.
- **Content merge.** The woodcut illustrates *its* tale — the
  wolf at the door of this story, this story's cottage — placed
  inside the tale's column between the paragraphs it depicts,
  never in a gallery. A plate with no tale is a decoration and
  is refused at build: every figure's caption names its scene
  in its tale (§12's caption rule).
- **Failure fallback.** Watchdog 4000ms from trigger: offsets
  snap to 0, blur removed — the plate stands printed. No JS:
  offsets never armed; finished woodcuts. Malformed SVG (a path
  without `pathLength`): that path ships visible and the rest
  carve around it — a flaw in the block, not a missing picture.
- **Reduced-motion variant.** The plate arrives printed, whole,
  with its tale. No carve, no blur. (A static woodcut is still
  a woodcut; the ceremony was the carving, not the image.)
- **Performance budget & mobile variant.** ≤24KB inline SVG
  per plate, ≤5 plates per page, ≤220 paths total across the
  page — the carving budget is a page budget. Dashoffset
  animation is compositor-cheap; the blur resolve is one layer
  for 400ms. Mobile (<768px): hatch group compresses to 1000ms
  and plates cap at 3 per page; a plate whose SVG exceeds 24KB
  is simplified at build, never shipped heavy.
- **Choreography timeline (v2).** Figure at 70% viewport →
  t=0 outlines begin → t=900 outlines complete, breath 120ms →
  t=1020 hatching begins, strokes staggered 24ms → t=2420
  hatching complete, breath 120ms → t=2540 deep cuts →
  t=3240 fills risen, blur resolve begins → t=3640 plate
  printed, caption kindles (its own §6.2). Watchdog ceiling
  4000ms.
- **State matrix (v2).** *Rest:* printed plate, caption lit.
  *Hover:* +4% warm, caption kindled. *Focus (linked):*
  instant print. *Active:* n/a. *Scrolled-past:* printed.
  *Disabled / no-JS:* printed. *Touch:* identical; no hover
  state exists to stick.
- **Breakpoints (v2).** ≥1200px: plate up to 560px wide inside
  the 38ch column (plates may break out to 720px centred — the
  one licensed column break, because a plate is a held-up
  picture). 768–1199px: plate ≤ column, no breakout. <768px:
  plate full column width, hatch 1000ms, no breakout, captions
  0.9375rem.
- **Edge cases & failure modes (v2).** *Plate taller than the
  viewport:* trigger uses the figure's top at 70%, so a tall
  plate begins carving before its foot is visible — correct:
  you watch the top of the picture being cut while its bottom
  is still off the page, like a block on a bench. *Two plates
  triggering together* (dense archive page): carves queue —
  max one carving at a time, second waits ≤ its watchdog; two
  simultaneous carves is a workshop, not a telling. *Print
  stylesheet:* plates print whole (offsets are screen-only
  state) — a printed Hearth page is a storybook, and storybooks
  do not print half-carved.
- **Accessibility spec (v2).** Each plate is `role="img"` with
  an `aria-label` describing the scene in one sentence (§12
  writes them); decorative repetition of the tale's own
  drop-cap motif is `aria-hidden`. The carve is never
  announced. Caption text is ordinary text at 7.61:1.
- **Tokens consumed (v2).** `--parchment-dim`, `--brick-deep`,
  `--soot`, `--ease-carve`, `--dur-carve-outline` (900ms),
  `--dur-carve-hatch` (1400ms), `--dur-carve-deep` (700ms),
  `--dur-watchdog-carve` (4000ms).

### 6.5 Page-curl chapter turns

- **What & why.** Between chapters — and between the page's
  great movements (tales → tallies, tallies → the chair) — the
  leaf turns: a page-curl sweeps from the bottom-right corner,
  the current section's lower edge lifting with a travelling
  shadow, revealing the chapter mark of what comes next beneath
  the curl's peak before the leaf settles. It belongs because
  the page is a heavy storybook (§4) and turning its leaf
  should be *felt* — 700ms of weight — at the exact moments the
  book itself would turn: chapter boundaries, never mid-tale.
- **Structure.** A full-viewport overlay leaf (`aria-hidden`,
  `pointer-events: none`) exists only during a turn: a
  `--beam`-backed panel clipped by an animated `clip-path`
  polygon whose corner point travels the diagonal, with a
  two-stop shadow gradient riding the clip edge (the curl's
  shade) and the *next* chapter's mark (Pirata One, §3) printed
  on the page beneath, revealed as the leaf lifts. The content
  itself never moves, clips or transforms — the leaf passes
  *over* the book's face at depth 3, below the mantel. Without
  JS the overlay is never created and chapters follow chapters
  in plain dark, separated by their marks.
- **Motion spec.** Trigger: a chapter boundary crossing the
  reading line, or a chapter-nav click (§6.11), whichever first
  — and only for boundaries the reader actually crosses (a jump
  to the footer fires no curl; the book does not turn pages you
  skipped). The curl: 700ms `--ease-curl` — clip corner travels
  from bottom-right (100%,100%) to top-left exit, the shade
  gradient peaking at 45% travel (shadow width 34vmin → 0),
  the revealed chapter mark kindling beneath from the moment
  the leaf's edge passes it. One curl per boundary, ever, per
  session: re-crossing a boundary upward fires a *reverse* curl
  (top-left entry, 560ms — a leaf turned back is lighter) once,
  then the boundary is spent both ways.
- **States.** At rest: no leaf in the DOM. Turning: overlay
  present, input unaffected (the page beneath remains
  scrollable and clickable — a slow reader is never locked out
  by weather). After: overlay removed at settle, not faded —
  a lingering leaf is a compositing cost and a lie (§6.1's
  rule, inherited). Focus during a turn: the turn completes
  instantly (focus is never asked to wait for paper).
- **Content merge.** The curl reveals the next chapter's real
  mark and first line — the turn is the book's own furniture,
  timed to the book's own joints. It never fires over a tale's
  body, a form, or the chair scene (§6.7 pins its own time);
  boundaries are declared in markup (`data-chapter`), so the
  book's joints are authored, not guessed by a script counting
  sections.
- **Failure fallback.** Watchdog 1100ms: a stalled clip
  animation removes the overlay. No JS: no leaf, chapters in
  sequence. `clip-path` unsupported: the turn degrades to a
  300ms `--smoke` crossfade at the boundary — the joint is
  still marked, in the theme's lesser ceremony.
- **Reduced-motion variant.** No leaf. The chapter mark simply
  stands at its boundary (it was always printed there); under
  reduced motion the mark gains a carved fleuron (§11) so the
  joint is still *visible as a joint* without motion.
- **Performance budget & mobile variant.** One overlay, one
  animated clip-path, one gradient — ≤0.6ms/frame, alive for
  700ms per boundary, ≤6 boundaries per page by build rule.
  Mobile (<768px): the curl travels from bottom-centre (a leaf
  turned by a thumb), 600ms, shadow 22vmin; on screens <380px
  wide the curl is replaced by the smoke crossfade — a small
  page cannot hold a big leaf honestly.
- **Choreography timeline (v2).** Boundary at reading line →
  t=0 leaf corner enters, shade at 0 → t=180 leaf edge passes
  the chapter mark; mark begins kindling beneath → t=315 shade
  peaks 34vmin → t=520 the next section's first line is clear
  of the leaf → t=700 leaf exits top-left, overlay removed →
  the new chapter's title begins its §6.3 stagger if armed.
  Watchdog ceiling 1100ms.
- **State matrix (v2).** *Rest:* no overlay. *Hover:* n/a (not
  a control). *Focus:* completes instantly. *Active:* n/a.
  *Scrolled-past:* boundary spent; no re-fire. *Disabled /
  no-JS:* no leaf ever. *Touch:* identical; a boundary crossed
  by fling still fires (the leaf turns fast or not at all —
  if the fling crosses two boundaries in <700ms, only the
  last curls; skipped joints stay silent).
- **Breakpoints (v2).** ≥1200px: corner curl, 700ms, shade
  34vmin. 768–1199px: corner curl, 650ms, shade 28vmin.
  <768px: bottom-centre curl 600ms, shade 22vmin; <380px:
  smoke crossfade 300ms.
- **Edge cases & failure modes (v2).** *Reader scrolls back
  and forth across a boundary hunting:* one forward + one
  reverse curl per session, then silence — the book does not
  flap. *Boundary inside the pinned chair range:* suppressed
  — §6.7 owns that scroll territory and its tales change by
  crossfade, not by leaf. *Print:* overlays are screen-only;
  the printed book has its real pages.
- **Accessibility spec (v2).** The leaf is `aria-hidden` and
  never announced; chapter marks are real headings in the
  outline at all times (the curl reveals visually what the
  document structure already states). Keyboard chapter
  navigation (§6.11) moves focus to the chapter heading
  *after* any curl completes — or instantly, per the focus
  rule — so focus is never placed under a moving leaf.
- **Tokens consumed (v2).** `--beam`, `--smoke`, `--parchment`,
  `--ease-curl`, `--dur-curl` (700ms), `--dur-curl-back`
  (560ms), `--dur-watchdog-curl` (1100ms).

### 6.6 The burning log progress

- **What & why.** In the bottom-right corner of the glass sits
  a log — a small horizontal cylinder of `--beam` with bark
  rings — and it burns down with the reader's progress through
  the page: a lit edge of `--ember-hot` creeps along its length
  from left to right, embers occasionally lifting from the
  burning point, until at the footer's bank the log is a line
  of settled ash with one warm heart. It belongs because this
  theme's progress is not a percentage, it is *the evening
  passing*: the fire you lit in the hero is the same fire, and
  it is finite, like all good evenings. A scroll bar would be
  a lie about what is being spent.
- **Structure.** A fixed `<div>` (depth 3, §4) holding an
  inline SVG log ~148×22px: bark path in `--beam`/`--iron`,
  end-grain rings at the unburnt end, and a burn mask whose
  lit length is a custom property `--burn` (0→1) driving three
  things in lockstep — the ember edge's position, the ash
  gradient's extent (burnt wood greys to `--ash` tones behind
  the edge), and the ember emission point for its occasional
  lifts. Beneath the log, in Cormorant 500 0.8125rem
  `--parchment-dim`, a printed label names the evening's
  fraction in the room's words — *The evening is young* /
  *Mid-evening* / *The fire is low* — three fixed strings (§12),
  never a percentage. The whole widget is `aria-hidden` as
  decoration, paired with a visually-hidden `role="progressbar"`
  carrying the real value for assistive tech.
- **Motion spec.** Scrubbed on the shared loop:
  `--burn = scrollY / (docHeight − viewportH)`, lerped 0.085,
  so the log burns with the same heavy drift as everything
  else and — the ratchet again — it never un-burns: the loop
  keeps `max(burn)` per session, because a fire does not
  regrow when you re-read a page; scrolling up leaves the log
  at its furthest burn, and the label with it. Ember lifts from
  the burning point: 1 per 2.8s average (seeded irregularity),
  3px rise-fade over 1400ms `--ease-drift`, drawn on the shared
  canvas (§6.1) at the log's screen position — the log's embers
  are part of the accounted budget (§14), sourced from the
  reading position's progress, which is the law's second clause
  made literal.
- **States.** Unburnt (top of page) → burning → ash (at the
  footer bank, §6.16, where the log's last heart pulses once —
  no: settles, §5 forbids a pulse; it *rests* at `--ember`
  40%). Hover: the label warms to `--parchment` and the log
  lifts 2px — an invitation, because the log is a control:
  clicking it returns to the top (the evening restarts; §6.16's
  "stoke the fire" is the same act in the footer). Focus:
  visible carved outline (§11's focus treatment), Enter/Space
  returns to top and the log resets — the one place the ratchet
  releases, because the reader chose a new evening. Scrolled-
  past: n/a (it is fixed; it *is* the scroll state).
- **Content merge.** The log measures *this page's* reading —
  its length is calibrated to the document, its label names the
  evening the reader is actually in, and its ash state is the
  trigger condition the footer (§6.16) reads to bank the fire.
  It is the page's clock, not a widget pasted into a corner.
- **Failure fallback.** No JS: the log renders at a neutral
  half-burn with the label *Mid-evening* — or, on pages short
  enough to need no progress (≤1.5 viewports), the log is not
  rendered at all: a one-tale page has no evening to measure.
  Loop stalled: the watchdog (§6.2's) also snaps `--burn` to
  the true scroll fraction — the clock may be still, never
  wrong.
- **Reduced-motion variant.** The log still burns (position is
  information, not motion), but nothing lifts from it, the lerp
  becomes a direct set, and the label changes are instant. The
  fire is steady; the evening still passes.
- **Performance budget & mobile variant.** One SVG, one custom
  property, ≤4 canvas embers attributable at any moment.
  Mobile (<768px): the log shrinks to 96×16px and its label is
  hidden (the log alone, bottom-right, clear of the thumb
  zone's centre) — on <380px it hides entirely once the form
  (§6.14) is on screen, because a chair being taken matters
  more than the clock.
- **Choreography timeline (v2).** Page top: log whole, label
  *The evening is young* → 33% scroll: label crossfades 400ms
  to *Mid-evening*, first third ash → 66%: ash two-thirds →
  92%: label *The fire is low* → footer bank reached (§6.16):
  the edge's last ember lifts, the heart settles to rest. Each
  label change is a 400ms `--ease-kindle` colour crossfade, the
  only scheduled beats in an otherwise continuous scrub.
- **State matrix (v2).** *Rest:* burning at true fraction.
  *Hover:* label warms, log +2px. *Focus:* carved outline;
  activation returns to top, resets. *Active (pressed):* log
  dips 1px, one ember puffs (§6.9's vocabulary). *Scrolled-
  past:* n/a. *Disabled / no-JS:* static half-burn or absent
  (short pages). *Touch:* tap = activation; no hover state.
- **Breakpoints (v2).** ≥1200px: 148×22px + label. 768–1199px:
  128×20px + label. <768px: 96×16px, no label; <380px: hides
  while §6.14 is in view.
- **Edge cases & failure modes (v2).** *Document grows after
  load* (late tales injected): `--burn` recomputes against the
  new height but the ratchet holds the max *fraction* reached,
  so injected content cannot visibly un-burn the log — the ash
  line may slow, never retreat. *Reader jumps to the footer by
  keyboard:* focus at the bank fires the ash state directly
  (the log reads focus position as well as scroll — §6.16's
  trigger is shared). *Print:* the log does not print; an
  evening is not paper.
- **Accessibility spec (v2).** The visible log is decorative
  (`aria-hidden`); the real progress is a visually-hidden
  `role="progressbar"` with `aria-valuemin/max/now` updated at
  most once per second (a chattier progressbar is a narrator
  who will not stop talking). As a button it has a real label
  — "Back to the top of the evening" — a 44×44px minimum hit
  area (the visible log is smaller than its target; the target
  is the honest size), and §11's focus ring.
- **Tokens consumed (v2).** `--beam`, `--iron`, `--ash`,
  `--ember`, `--ember-hot`, `--parchment`, `--parchment-dim`,
  `--ease-kindle`, `--ease-drift`, `--dur-label-fade` (400ms),
  `--lerp` (0.085).

### 6.7 The pinned storyteller's chair

- **What & why.** Mid-page, the room holds still: a scene pins
  — the storyteller's chair beside the hearth, drawn in woodcut
  line (§6.4's plate language, larger) with the fire's glow
  breathing at its side — while three tale summaries are told
  beside it in sequence, each fading up in Cormorant as its
  third of the pinned range passes, each carrying its carved
  number. The chair stays; the tales change. It belongs because
  every storytelling tradition has this furniture: the seat
  that outlasts the stories, the constant the evening turns
  around. It is the page's one long breath (§4), and the only
  pinned scene the theme allows.
- **Structure.** A section of 300vh (desktop) with a sticky
  stage of 100vh: left, the chair plate (inline SVG, pre-carved
  — it ships printed; §6.4's ceremony belongs to tales, and the
  chair was carved before the reader arrived); right, a stack
  of three summary blocks in the tale column, each a real
  heading + two-sentence summary + link to its full tale, all
  present in the DOM in order. Crossfade state is a custom
  property `--tale` (0→3 continuous) on the stage; each summary's
  opacity/colour is a function of its distance from `--tale`'s
  current integer — the active summary at full `--parchment`,
  its neighbours at `--parchment-dim` 55%, never below
  legibility-as-print because all three are real content that a
  no-JS reader reads stacked.
- **Motion spec.** Scrubbed on the shared loop across the
  pinned range: each tale owns one third; crossfades run over
  the middle 40% of each third (the ends are held — a tale is
  *told*, then there is a pause in which only the fire moves).
  As a summary becomes active, its carved number (§6.10's
  treatment) warms from dim to ember and its first line kindles
  (§6.2's curve, compressed). The chair does not move. The glow
  at the chair's side breathes on the global cycle (§5) and
  leans +4% intensity toward whichever summary is active — the
  fire listens. Total pinned travel 300vh; the stage unsticks
  into §6.5's chapter turn (the boundary after the chair is a
  declared chapter joint).
- **States.** Approaching: stage enters, first summary active.
  Telling (rest state of the pin): one summary full, others
  dim. Leaving: third summary holds full until the stage's foot
  leaves, then the section behind is an ordinary stacked
  section — the pin leaves no residue in layout or tab order.
  Hover: summaries warm per §6.8. Focus: a summary receiving
  focus becomes the active one — the scrub yields to the
  keyboard, `--tale` snaps to that summary's index over 600ms
  `--ease-kindle`, and scroll position is *not* hijacked (the
  pin's range simply shows the focused tale until scroll
  resumes authority at the range's edges). Scrolled-past: the
  section rests as three told summaries, all at full parchment
  (the ratchet: behind the reader, everything is lit).
- **Content merge.** The three summaries are three real tales
  of the site — on a publisher's page, the evening's three
  featured stories with links; on a heritage page, the three
  tales the cottage is known for. The chair is empty in the
  plate (the teller is the page itself; §6.13's occupied-chair
  variant is a different, deliberate statement and the two
  never mix on one page).
- **Failure fallback.** No JS: no pin; the section is a normal
  stacked section, chair plate above three full summaries —
  complete, merely unperformed. Loop stalled: watchdog sets
  `--tale` from raw scroll fraction (the scrub formula, §6.2's
  fallback doctrine) and all summaries read at ≥55% — none can
  be stranded invisible because their floor is dim print, not
  transparency: opacity never drops below 0.55 for any summary,
  armed or not.
- **Reduced-motion variant.** The pin is abolished: the section
  renders as the no-JS stack (chair plate, then three summaries
  at full parchment, 100vh total). Pinned scrubbing is the
  theme's most theatrical device and the first to go; the tales
  lose nothing but their stage.
- **Performance budget & mobile variant.** One sticky stage,
  three opacity/colour functions, one pre-carved SVG ≤30KB.
  Mobile (<768px): pin shortens to 220vh and the layout stacks
  — chair plate as a 34vh header band above the summaries,
  which crossfade in place; <380px or `prefers-reduced-motion`:
  the stack, unpinned. The chair scene is desktop theatre and
  the expansion says so rather than shrinking it into a gimmick.
- **Choreography timeline (v2).** Stage top reaches viewport
  top → pin → tale 1 full (its number warms) → 33% range: tale
  1 dims to 55% across the crossfade window, tale 2 rises →
  held pause (fire only) → 66%: tale 3 rises likewise → final
  hold → stage releases → §6.5 curl at the declared boundary →
  section behind rests fully lit. Each crossfade ≈120vh of
  scroll travel ≈2.4s at reading pace — a told pace, not a
  carousel's.
- **State matrix (v2).** *Rest (in pin):* one tale full, two
  at 55% dim print. *Hover:* §6.8 stir on the hovered summary.
  *Focus:* focused tale becomes active (600ms). *Active:* n/a.
  *Scrolled-past:* all three full parchment, unpinned.
  *Disabled / no-JS:* stacked, full. *Touch:* identical scrub;
  no hover; flings across the range land on the nearest tale
  (the lerp's catch-up) rather than mid-crossfade.
- **Breakpoints (v2).** ≥1200px: 300vh pin, chair left /
  summaries right (46/54 split). 768–1199px: 260vh pin, split
  40/60, chair plate ≤340px. <768px: 220vh pin, stacked layout;
  <380px: unpinned stack.
- **Edge cases & failure modes (v2).** *A summary longer than
  the stage* (a verbose tale): summaries are capped at build —
  heading + 2 sentences + link (§12 enforces the count); a
  summary that overflows its third is a build failure, not a
  runtime state. *Reader resizes mid-pin:* the stage recomputes
  its range from live geometry each frame (the loop reads, it
  does not cache), so rotation or a dragged window re-seats the
  tales without a jump. *Only two tales available:* the scene
  runs with two (range splits in halves) — never pad with a
  dummy third tale; an empty third slot is §6.13's chair, a
  different element, and conflating them is slop.
- **Accessibility spec (v2).** All three summaries are in the
  accessibility tree, in order, at all times — dimming is
  visual only (opacity floor 0.55 keeps dim summaries at
  ≥4.6:1 effective contrast, and the *active* summary is
  13.60:1). The pin creates no focus trap and no scroll
  hijack; `aria-current` is not used (nothing here is a
  carousel and it must not be announced as one). The chair
  plate is `role="img"` with §12's label.
- **Tokens consumed (v2).** `--parchment`, `--parchment-dim`,
  `--ember`, `--soot`, `--ease-kindle`, `--dur-focus-snap`
  (600ms), `--lerp` (0.085), `--pin-range` (300vh).

### 6.8 Hover ember-stir

- **What & why.** Hovering a told tale — or a tale card, a
  summary, a tally — brightens it slightly and stirs the embers
  at its edges: six to ten small embers lift from the element's
  lower edge, drift up a few centimetres, and resettle. It is
  the theme's one hover language, and it belongs because it is
  what attention does in a fireside room: looking closely at a
  story warms it. The stir is small, brief and sourced — the
  embers come *from the tale*, per the law's second clause —
  and when the pointer leaves, the tale settles back to its
  told warmth, unchanged.
- **Structure.** A class-driven state on the tale element:
  `--stir` (0→1) drives a brightness lift (colour steps one
  stop toward cream on the title only; body text does not
  brighten — reading text that pulses under a cursor is a
  hazard, so the lift lives in the title, the card's plate and
  the element's ember-bloom pseudo-element from §6.2). The
  lifted embers are canvas particles (§6.1's shared canvas)
  spawned at the element's lower-edge coordinates — the
  element emits, the canvas draws; no per-element particle DOM.
- **Motion spec.** Pointer enter: `--stir` rises over 350ms
  `--ease-settle`; 6–10 embers spawn across the first 500ms,
  each rising 40–90px over 1200–1800ms `--ease-drift` with a
  6px sway, fading at the top of its rise. Pointer leave: no
  new spawns; live embers finish their rise (embers are not
  recalled — a stirred fire settles on its own schedule), the
  lift decays over 600ms `--ease-bank`. Re-entering during
  decay resumes from the current value; the spawn budget is
  per-element per-2s (≤10), so a pointer jittering across a
  tale cannot strip-mine the ember budget (§14).
- **States.** Rest: told warmth, bloom 0.18 (§6.2). Hover:
  stirred, as above. Focus: identical to hover (keyboard
  attention is attention) — a focused tale stirs, once, at
  focus-in, and settles while focus remains (the stir is a
  greeting, not a held state; the *focus ring* is §11's and is
  held). Active: §6.9's thunk answers the press. Scrolled-past:
  told tales behind the reader still stir — the room is alive
  in every direction. Disabled: a tale mid-load (§6.17's unlit
  shape) does not stir; there is nothing there yet to warm.
- **Content merge.** The stir happens on the tale itself — its
  own edges, its own title warming — never on chrome around it.
  On cards (§6.12) the stir lifts embers from the card's plate;
  on tallies (§6.10) from the numeral's base. One vocabulary,
  each element's own fire.
- **Failure fallback.** Canvas unavailable: the lift alone
  carries the state (title warms, bloom rises) — the greeting
  survives without its sparks. No JS: no stir; hover still gets
  the CSS-only title warm (a `:hover` colour step needs no
  script), so the room is not dead for scriptless readers.
- **Reduced-motion variant.** No embers lift. The title still
  warms one step on hover/focus (a colour change, not a motion)
  — attention is acknowledged without anything rising.
- **Performance budget & mobile variant.** ≤10 particles per
  stir, drawn on the shared canvas; the lift is colour-only.
  Touch: there is no hover — the stir fires once on tap-down
  before §6.9's thunk, so touch readers get the same greeting
  in sequence (stir 200ms compressed, then the thunk's puff).
- **Choreography timeline (v2).** t=0 pointer enter → t=0–350
  lift rises, bloom to 0.5 → t=80 first ember lifts → t=80–580
  remaining embers spawn staggered 40–70ms → t≈1300–1900 embers
  fade at rise-top → pointer leave (any t): spawns stop, lift
  decays 600ms, last ember lands by t_leave+1800. Watchdog:
  none needed — every state decays to rest unaided.
- **State matrix (v2).** *Rest:* bloom 0.18. *Hover:* stirred.
  *Focus:* stir once at focus-in, then rest warmth + ring.
  *Active:* §6.9. *Scrolled-past:* stirs normally. *Disabled
  (unlit/loading):* no stir. *Touch:* tap-down stir 200ms,
  then §6.9.
- **Breakpoints (v2).** ≥1200px: 6–10 embers, rise 40–90px.
  768–1199px: 5–8 embers, rise 36–72px. <768px: touch-only —
  4–6 embers, rise 30–54px, spawn on tap-down only.
- **Edge cases & failure modes (v2).** *Pointer crosses many
  tales quickly* (skimming the archive): each element's budget
  is its own, but the canvas's global cap (§14) throttles
  spawns page-wide — the room gets lively, never a bonfire.
  *Element partially off-screen:* embers spawn only from the
  visible portion of the lower edge (coordinates clamped to the
  viewport) — no embers from nowhere below the fold.
  *Hover during the tale's own kindling:* the stir waits —
  kindling owns the element until k=1 (§6.2); a tale catches
  before it can be stirred.
- **Accessibility spec (v2).** The stir is decorative and
  `aria-hidden` (canvas); the title's warm step keeps contrast
  ≥13.60:1 throughout (cream is brighter, never dimmer). Focus
  stir never replaces or delays the visible focus ring, which
  renders on the same frame as focus-in, stir or no stir.
- **Tokens consumed (v2).** `--parchment-cream`, `--ember`,
  `--ember-hot`, `--ease-settle`, `--ease-drift`,
  `--ease-bank`, `--dur-stir` (350ms), `--dur-stir-decay`
  (600ms).

### 6.9 Log-thunk click

- **What & why.** Choosing a tale — clicking its title, its
  card, its summary link — answers with the room: a small jolt
  through the element, like a log shifted in the grate, and a
  brief puff of sparks from the hearth side of the page. The
  thunk is the theme's click confirmation: choosing a story
  shifts the fire. It belongs because on a Hearth page a click
  is not an interface event, it is a physical one — you have
  reached for a book, and the room noticed. The navigation
  itself then proceeds by §6.17's smoke-and-leaf, a beat later,
  so cause and effect stay legible: thunk (choice) → leaf
  (journey).
- **Structure.** A class (`is-thunked`) applied to the chosen
  element for 480ms: `transform: translateY(0→4px→0)` on the
  element's inner wrapper (the element's own box never moves —
  layout does not jump for a sound effect), plus a spark puff
  of 8–14 particles from the shared canvas, spawned at the
  hearth-side edge of the element (its lower-left in LTR) with
  short, fast trajectories — a puff, not a rise: 300–600ms
  lives, outward drift, quick fade. No audio: the thunk is
  visual and tactile (a `navigator.vibrate(8)` on supporting
  touch devices, once, is the licensed sound of this theme —
  off by default where the platform requires a settings grant).
- **Motion spec.** Click/tap/Enter: t=0 the wrapper dips 4px
  over 90ms `--ease-thunk` (the overshoot curve gives the
  settle its weight) → t=90–240 the wrapper returns, overshoot
  +1px at ≈180ms, rest at 240ms → sparks puff at t=40 (the dip
  *causes* the puff — 40ms of causality) and are gone by
  t=640 → at t=160 the page transition (§6.17) begins if the
  click navigates; if the click only expands in place (an
  accordion tale, §11), the expansion begins at t=240 as the
  wrapper settles. Total felt event ≈0.5s; the reader is never
  held longer than that by feedback.
- **States.** Rest: nothing. Pressed (`:active`): the dip is
  the active state — no separate colour change (a pressed tale
  does not flash; it *thunks*). After: the element returns to
  told warmth; a visited tale gains a permanent, subtle mark —
  its chapter fleuron (§11) fills with `--brick` — the book
  remembers where the reader has been. Disabled links (a tale
  not yet published, §6.15's banking tale): no thunk, no puff;
  the element sits at dim print with its "banking" label —
  you cannot shift a log that is not in the grate.
- **Content merge.** The jolt runs through the tale chosen, and
  the sparks come from its own hearth-side edge — the feedback
  is located in the content, not in a toast corner. The one
  exception is form submission (§6.14), where the puff rises
  from the form's hearth-stone panel: same vocabulary, the
  room answering a different act.
- **Failure fallback.** Canvas unavailable: the dip alone
  confirms (it was always the primary signal). No JS: links
  simply navigate — the thunk is an enhancement layered on a
  working book, never a gate in front of it. Transition
  (§6.17) unavailable or aborted: navigation proceeds plainly;
  the thunk already happened and needs no completion.
- **Reduced-motion variant.** No dip, no puff. Confirmation is
  a 200ms colour step on the element's title (parchment →
  cream → parchment) — the room nods instead of shifting.
- **Performance budget & mobile variant.** ≤14 particles,
  ≤640ms lives; the dip is one transform on one wrapper.
  Mobile: identical (tap fires the same sequence; the dip is
  3px under 380px — a small screen, a smaller log).
- **Choreography timeline (v2).** t=0 press → t=0–90 dip 4px →
  t=40 sparks spawn → t=160 transition begins (if navigating)
  → t=180 overshoot +1px → t=240 wrapper at rest → t=640 last
  spark fades → (in-place actions begin their work at t=240).
  Watchdog: the class self-removes at 480ms by timer, so a
  lost `animationend` cannot leave an element dipped.
- **State matrix (v2).** *Rest:* told warmth. *Hover:* §6.8's
  stir precedes. *Focus:* ring (§11); Enter fires the thunk
  identically to click. *Active:* the dip itself. *Scrolled-
  past:* n/a. *Disabled:* no thunk; dim print + label.
  *Touch:* tap = full sequence; long-press does nothing
  special (no context theatre).
- **Breakpoints (v2).** ≥1200px: dip 4px, sparks 8–14.
  768–1199px: dip 4px, sparks 7–12. <768px: dip 3px, sparks
  6–10; <380px dip 3px, vibration off (a small phone in a hand
  is already tactile enough).
- **Edge cases & failure modes (v2).** *Double-click / impatient
  double-tap:* the second press within 480ms restarts the dip
  but not the puff (spark budget), and navigation is debounced
  by the transition layer, never by the thunk — the feedback
  must never become a lock. *Click on a tale while its section
  is mid-curl* (§6.5 overlay passing): the overlay is
  `pointer-events: none`, the click lands, the thunk fires —
  paper passing overhead does not eat choices. *Right-click /
  cmd-click (new tab):* no thunk, no transition — the reader
  took the book to another room; this page says nothing.
- **Accessibility spec (v2).** The thunk is never the only
  confirmation: navigation and expansion proceed by their real
  mechanisms, and in-place expansions use `aria-expanded`
  correctly. The dip is 4px maximum — below vestibular concern
  and removed entirely under reduced motion. Focus is never
  moved by the thunk.
- **Tokens consumed (v2).** `--ease-thunk`, `--dur-thunk`
  (480ms), `--ember`, `--ember-hot`, `--parchment-cream`,
  `--brick`.

### 6.10 Carved tallies

- **What & why.** The cottage keeps count the way cottages do —
  notched, not dashboarded. "Tales told since the last frost",
  "Listeners this winter", "Chairs taken for Thursday": each is
  a numeral in Cormorant 600 with the carved treatment (§3) —
  knife shadow below, ember rim on the fire side — set into a
  `--beam` tally board, and each counts up as its section is
  told. It belongs because numbers in this theme are *kept*,
  not displayed: a tally is a physical record cut into wood,
  and the count-up is the cutting. Every tally traces to a
  printed source line beside it ("counted from the winter
  book, p. 3") — the law's arithmetic clause, in the room's
  furniture.
- **Structure.** A `<dl>` tally board: term in Cormorant 500
  `--parchment-dim` ("Tales told since the last frost"),
  definition holding the numeral (`--ember`, carved) and,
  beneath it in caption size, its source line. The numeral's
  final value is the printed DOM text; counting is a JS
  text-content walk over the printed value (parsed, stepped,
  restored) — no `data-` shadow values, so the number on the
  page is the only number there is. Notch marks (small `--iron`
  strokes in groups of five, the fifth diagonal — a real tally)
  decorate the board's edge at a count equal to the numeral's
  tens: decoration that is also arithmetic, checked by the gate.
- **Motion spec.** Trigger: the board kindles (k=1, §6.2).
  Each numeral counts from `max(0, final − 12)` — a tally is
  *finished*, not started; counting from zero would claim the
  winter began when the reader arrived — over 1100ms
  `--ease-kindle`, in whole steps at the numeral's own
  precision, landing exactly on the printed figure. Numerals
  on one board stagger 160ms apart (the keeper cuts one notch
  at a time). A seat tally (§6.14's form) that changes because
  the visitor took a chair re-counts by one notch: the numeral
  steps ±1 over 300ms and a fresh notch darkens on the edge —
  the board is live wood, not a screenshot.
- **States.** Rest (told): final figures, carved, ember rim
  lit. Pre-trigger: printed final figures (the board is never
  blank or zeroed in the DOM). Hover: §6.8's stir at the
  numeral's base + the source line warms to `--parchment`.
  Focus: tallies are not interactive unless the board is a link
  (the archive's board is not). Scrolled-past: told figures,
  resting.
- **Content merge.** The tallies count the site's real things —
  its tales, its listeners, its chairs — and their source lines
  name the real record (the winter book, the guest book, the
  booking ledger). A tally without a source line is a dashboard
  wearing a costume and is refused at build.
- **Failure fallback.** No JS: the printed figures stand — the
  board reads complete. Counting interrupted (tab hidden):
  on return, numerals snap to final; a half-cut notch is
  finished, not left hanging. Malformed printed figure
  (non-numeric in the DOM): the walk skips it and the figure
  simply stands — the keeper does not carve what he cannot read.
- **Reduced-motion variant.** No count-up: figures stand at
  final value. The ±1 step on a taken chair becomes an instant
  change with a 200ms colour nod (§6.9's reduced vocabulary).
- **Performance budget & mobile variant.** Text-content writes
  ≤3 numerals × ~20 steps; zero layout (tabular-nums holds the
  column). Mobile: the board stacks (term above numeral),
  notches cap at 40 drawn strokes — beyond that the edge shows
  grouped bundles (§11's tally component rule), because a
  thousand notches is a fence, not a tally.
- **Choreography timeline (v2).** Board at k=1 → t=0 numeral 1
  begins its walk (final−12 → final, 1100ms) → t=160 numeral 2
  → t=320 numeral 3 → t≈1420 board at rest, source lines
  kindle → (later, if a chair is taken, §6.14) t=0 the seat
  numeral steps, t=300 notch darkens, done. Watchdog: any
  numeral mid-walk at 1800ms snaps to its printed figure.
- **State matrix (v2).** *Rest:* final, carved. *Hover:* stir
  + source warms. *Focus:* n/a (non-interactive) or §11 ring
  where the board links. *Active:* n/a. *Scrolled-past:*
  final. *Disabled / no-JS:* printed final. *Touch:* no hover;
  the board counts on kindle as on desktop.
- **Breakpoints (v2).** ≥1200px: board horizontal, up to 3
  tallies abreast. 768–1199px: 2 abreast, third wraps.
  <768px: stacked single column, numerals 2rem, notches ≤40.
- **Edge cases & failure modes (v2).** *A tally of zero* (no
  tales yet this winter): the board prints 0 and does not
  count — and §12's empty-state line stands beside it ("The
  winter book opens with the first tale"), because a bare 0 on
  a tally board reads as a bug, not a beginning. *Huge counts*
  (a heritage archive's 12,408 tales): the walk shortens to
  the last 40 (1100ms regardless — the duration is the
  ceremony, the range is arithmetic) and the figure sets with
  its thousands separator as printed. *Live seat tally racing
  the form:* the board and the form read one printed value
  (§6.14 owns the arithmetic); two carvers on one board is a
  build error the gate catches.
- **Accessibility spec (v2).** Each numeral has a
  visually-hidden twin holding the final value for the whole
  walk (AT never hears a number mid-cut), and the `<dl>`
  structure keeps term and figure paired. Carved shadow never
  reduces contrast: the numeral's face is `--ember` at 6.16:1
  minimum, and tallies that function as text (seat counts in
  the form) use `--ember-hot` at 9.55:1.
- **Tokens consumed (v2).** `--ember`, `--ember-hot`,
  `--parchment`, `--parchment-dim`, `--beam`, `--iron`,
  `--carve`, `--ease-kindle`, `--dur-tally` (1100ms),
  `--dur-notch` (300ms).

### 6.11 Mantel navigation

- **What & why.** The navigation is the mantel shelf: a
  `--beam` bar across the top of the glass carrying the site's
  name in Pirata One at its left (carved, §3) and the sections
  as objects set on the shelf — Tales, The Chair, Tallies, Take
  a Seat — each a Cormorant 500 label with a small carved
  fleuron. The current section's object is *lit*: a candle-dot
  of `--ember-hot` burns above its label, the one flame on the
  shelf. It belongs because a cottage's wayfinding is its
  furniture: you find things by where they sit on the mantel,
  and the lit candle marks where in the evening you are.
- **Structure.** A real `<nav>` with a real list of anchor
  links, sticky at depth 3 (§4), 64px tall on desktop, over a
  `--soot` backdrop that deepens from 72% to 94% opacity as the
  page scrolls past the hero (the room darkens behind the
  shelf as the fire becomes the light). The candle-dot is a
  6px radial disc positioned above the active label, moved by
  transform between items. `aria-current="true"` rides the
  active link. Below 768px the shelf becomes a *mantel drawer*:
  a "The Mantel" button opening a full-width panel under the
  shelf with the same links stacked — objects taken down and
  shown, not a hamburger abstraction.
- **Motion spec.** Scrollspy on the shared loop: the active
  section is the one whose heading last crossed the reading
  line (§6.2's line, so nav, kindling and the log all agree
  about where the reader is — one room, one clock). The candle
  travels between items over 500ms `--ease-kindle`, with a
  120ms dip in its glow at the midpoint (a carried flame gutters
  as it moves) and a small ember lift (§6.8's vocabulary, 3
  embers) on arrival. Link hover: the label warms dim→parchment
  250ms and its fleuron warms to `--brick`-lit; the candle does
  not move on hover (the flame marks where you *are*, not where
  you are looking). Click: §6.9's thunk, then smooth scroll
  (lerped, the shared loop drives a scroll-to over ≈900ms) to
  the chapter — during which §6.5's curl fires if a boundary is
  crossed.
- **States.** Rest: candle over the current section. Hover: as
  above. Focus: the focused link takes §11's carved focus ring;
  focus does not move the candle (focus is attention, §6.7's
  doctrine) but Enter does. Active page (the section being
  read): candle lit, label at `--parchment`, others at
  `--parchment-dim`. Drawer (mobile): closed / open (panel
  kindles its links in stagger 40ms as it opens, 350ms
  `--ease-kindle`). Scrolled-past: n/a — the shelf is the room's
  constant.
- **Content merge.** The shelf's objects are the page's actual
  sections, named in the room's words ("Take a Seat" is the
  form, §6.14; "The Chair" is §6.7). On multi-page sites the
  shelf carries pages the same way, and the candle marks the
  page — the furniture is the sitemap, drawn to scale.
- **Failure fallback.** No JS: the shelf is a static bar of
  anchor links at 94% backdrop; anchors jump plainly; no candle
  (the candle is a JS courtesy — `aria-current` in the static
  HTML marks the home item honestly). Scrollspy dead: the
  candle parks over the first item rather than wandering.
- **Reduced-motion variant.** The candle changes item
  instantly; no dip, no lift, no stagger in the drawer (links
  appear as a list). Smooth scroll becomes an instant jump.
- **Performance budget & mobile variant.** One transform on one
  6px disc; scrollspy reads the loop's existing positions —
  zero extra observers. Mobile (<768px): shelf 56px, name
  truncated to its carved initial + wordmark short form (build
  supplies both), drawer panel as above; the candle becomes a
  left-edge ember bar inside the drawer (a flame in a drawer
  is a fire risk and a layout bug — the metaphor yields to the
  medium, §9 notes the ruling).
- **Choreography timeline (v2).** Section heading crosses the
  reading line → t=0 candle begins travel → t=250 midpoint dip
  (glow 100%→55%) → t=500 arrival, 3 embers lift → t=1900 embers
  settled. Drawer open: t=0 panel unrolls (height 0→auto via
  grid-rows trick, 350ms) → links kindle staggered 40ms →
  t≈550 shelf fully shown. Watchdog: none — the candle's worst
  failure is parking, which is designed.
- **State matrix (v2).** *Rest:* candle at current section.
  *Hover:* label + fleuron warm. *Focus:* ring; candle unmoved.
  *Active:* candle here, label parchment. *Scrolled-past:*
  n/a. *Disabled / no-JS:* static links, no candle. *Touch:*
  drawer pattern; tap = thunk + scroll.
- **Breakpoints (v2).** ≥1200px: full shelf, 64px, all objects
  visible (≤6 by build rule — a mantel holds six things).
  768–1199px: 60px, labels may shorten (build supplies short
  labels). <768px: 56px + drawer.
- **Edge cases & failure modes (v2).** *More than six sections:*
  the shelf refuses a seventh object — overflow sections group
  under "More Tales" (a shelf object that opens the drawer
  pattern even on desktop). A crowded mantel is a mantel you
  cannot dust. *A page with one section:* no candle, no spy —
  the shelf is a name and a chair link only. *Sticky shelf over
  the pinned chair:* the shelf stays (it is furniture, depth 3)
  and the candle holds on "The Chair" for the whole pin — the
  spy reads the section, not the sub-tales.
- **Accessibility spec (v2).** Landmark `<nav>` with
  `aria-label="The mantel"`; `aria-current` on the active link,
  updated with the candle; drawer button carries
  `aria-expanded`/`aria-controls`, closes on Esc, and returns
  focus to the button. All targets ≥44px tall. The candle is
  `aria-hidden` — position is announced by `aria-current`, not
  by a flame.
- **Tokens consumed (v2).** `--beam`, `--soot`, `--parchment`,
  `--parchment-dim`, `--ember-hot`, `--brick`, `--carve`,
  `--ease-kindle`, `--dur-candle` (500ms), `--dur-drawer`
  (350ms).

### 6.12 Chapbook tale cards

- **What & why.** On listing and archive pages, tales are
  chapbooks on a shelf: a card the proportions of a cheap
  printed pamphlet (3:4.2), its cover a woodcut plate (§6.4,
  pre-carved or carving on entry), its title in Pirata One, a
  Cormorant standfirst of one line, and at its foot the tale's
  measure in the room's units — its length in logs ("a two-log
  tale", §11's badge) and its teller. Cards kindle like tales
  (§6.2) because on this page they *are* the tales, in covers.
  It belongs because a folklore archive browsed as a grid of
  identical SaaS cards has already lost; a shelf of chapbooks
  can be browsed the way chapbooks were — by their covers, in
  the firelight.
- **Structure.** An `<article>` per card inside a two-column
  shelf (≥1200px; §4's two-chair rule), each card a single
  `<a>` wrapping plate, title, standfirst and measure — one
  link, whole cover, no nested interactives. Card ground is
  `--brick-deep` at the spine edge grading to `--beam` — the
  cover is darker than the room's text surfaces, so the plate
  (parchment line) and title read as print on a cover. The
  featured tale (first, or editor's mark) spans both columns
  with a larger plate — the evening's first tale, told biggest.
- **Motion spec.** Entry: the card kindles on §6.2's curve
  (its k drives cover warmth and title colour together), its
  plate carves if uncarved (§6.4, queued), and the card settles
  from scale 1.04 to 1.0 over 900ms `--ease-settle` as k passes
  0.7 (§5's one licensed scale — the chapbook is set down on
  the shelf). Hover/focus: §6.8's stir from the plate's lower
  edge + the title warms to cream. Click: §6.9's thunk, then
  §6.17's transition to the tale. Cards behind the reading line
  rest told; cards ahead wait at ash — a shelf receding into a
  dark room, which is what shelves do.
- **States.** Unkindled → kindling → told (rest). Hover/focus:
  stirred. Active (pressed): thunk dip. Visited: the card's
  fleuron fills `--brick` (§6.9's memory) and its measure line
  gains "· told" — the shelf remembers. Disabled (a tale still
  banking, unpublished): cover at dim print, no plate (a
  silhouette shape, §6.17), label "Banking — told on Thursday"
  (§12's string), not a link.
- **Content merge.** Every field on the cover is the tale's
  own: its plate illustrates it, its measure is its real
  length (reading minutes ÷ 12, rounded to the half-log,
  printed beside the minute count — the arithmetic is shown,
  §6.10's doctrine), its teller is its author. A card with a
  stock plate or an invented length is a chapbook with someone
  else's story in it.
- **Failure fallback.** No JS: covers print lit, plates whole,
  shelf complete. Carve queue stalled: §6.4's watchdog prints
  plates. A missing plate (asset failed): the cover carries
  the tale's drop capital in Pirata One at plate size — the
  chapbook is letterpress-only that evening, and still a book.
- **Reduced-motion variant.** Covers arrive lit and printed;
  no settle, no carve, no stir. The shelf is a shelf.
- **Performance budget & mobile variant.** Plates count toward
  §6.4's page budget (≤5 carving plates; further covers ship
  pre-carved). Mobile (<768px): one column, cards at 4:4.6
  (a squarer chapbook for a smaller hand), featured card spans
  the single column with plate at 16:10 — the shelf becomes a
  stack, read top to bottom like tales told in order.
- **Choreography timeline (v2).** Card top enters kindle span
  → k rises (§6.2) → k=0.5 title stagger may fire if the card
  is featured (§6.3's ceremony is rationed to one per page on
  listing pages — the featured tale) → k=0.7 settle begins
  (900ms) → plate carve runs its §6.4 timeline in queue →
  k=1 card told, measure line kindles last (the count is the
  cover's colophon). Watchdogs: §6.2's 1600ms, §6.4's 4000ms.
- **State matrix (v2).** *Rest:* told cover. *Hover:* stir +
  title cream. *Focus:* stir + §11 ring; the whole card is the
  target (≥44px, in practice ~300px). *Active:* thunk.
  *Scrolled-past:* told, visited marks persist. *Disabled:*
  banking card, dim, unlinked. *Touch:* tap-down stir, then
  thunk (§6.8/§6.9 sequence).
- **Breakpoints (v2).** ≥1200px: two columns, featured spans
  two. 768–1199px: two columns, featured spans two, plates
  smaller. <768px: one column, featured plate 16:10.
- **Edge cases & failure modes (v2).** *An archive of 60
  tales:* pagination is by shelf (§11's leaf pagination), 8
  covers per shelf-page — an endless scroll of chapbooks is a
  warehouse, and the carve/kindle budgets are per-page by
  design. *Titles of very different lengths:* covers fix the
  title zone at 3 lines (Pirata One, clamped) so the shelf's
  rhythm holds; a title needing a fourth line is shortened at
  build, never shrunk (§3's floor). *A tale with no teller
  credited:* the measure line reads "an old tale" — anonymous
  is a credit in folklore, not a gap.
- **Accessibility spec (v2).** One link per card with a
  composed accessible name: title + standfirst + measure ("The
  Wolf at the Door — a two-log tale, told by Maren — 24
  minutes"). Plates are `aria-hidden` inside the link (the
  name carries the tale). Banking cards are text, not disabled
  links — nothing focusable that does nothing.
- **Tokens consumed (v2).** `--brick-deep`, `--beam`,
  `--parchment`, `--parchment-dim`, `--ash`, `--brick`,
  `--ease-settle`, `--dur-settle-card` (900ms), plus §6.2/§6.4
  token sets inherited.

### 6.13 The empty chair

- **What & why.** Between tale groups — after the third tale,
  before the tallies — the page sets one empty chair by the
  fire: the chair plate (woodcut line, §6.4's language) drawn
  at tale-column width, unoccupied, lit by the glow, with a
  single caption beneath in `--parchment-dim`: *"For whoever
  is telling it next."* Nothing else. No button on the chair
  itself; below the caption, one quiet Cormorant link — "Tell
  one" — leads to submissions. This is the original entry's
  anti-slop detail promoted to a full element, because it is
  the theme's thesis in furniture: the tradition continues
  because a seat is kept. It belongs exactly once per page,
  between tales, where a lesser theme would put a banner.
- **Structure.** A `<figure>` in the tale column: the chair
  SVG (pre-carved, ships printed — the chair was in the room
  before the reader arrived, like §6.7's), a cushion shape in
  `--moss` — the green of outside, carried in (§2's ratio made
  literal: the next teller comes from outdoors) — and the
  `<figcaption>` with the verbatim caption and the "Tell one"
  link. The figure's section is a room-beat (§4): short, dark
  at the edges, no other content. The caption is never
  translated into marketing copy; §12 fixes the string.
- **Motion spec.** Almost none, by design — the chair's power
  is stillness in a page of warming things. As the section
  crosses the reading line, the glow behind the chair rises
  +8% over 1400ms `--ease-kindle` (the fire makes room) and one
  ember — exactly one — lifts from the hearth side and settles
  on the chair's arm over 2100ms `--ease-drift`, then rests
  there, dim, for as long as the section is in view. That is
  the entire choreography. A chair that bounces, glows in a
  loop or grows a pulsing CTA has been understood by no one.
- **States.** Rest: chair lit, ember resting on the arm.
  Hover (on the link only): the link warms per §11; the chair
  does not stir (§6.8 is for tales; the chair is not a tale,
  it is an invitation, and invitations do not fidget). Focus:
  the link's ring; the ember stays. Scrolled-past: the section
  rests as it was — the ember on the arm remains while the
  page lives (a per-session state; on reload the chair is
  empty again, as chairs are each morning).
- **Content merge.** The chair is the submissions CTA wearing
  the theme's own meaning: "Tell one" goes to the real
  contribute page, and the caption is the reason to go. On
  sites without submissions (a single-author blog), the link
  becomes "Hear the next one" to the newsletter (§6.14) — the
  chair still points at the tradition continuing, by listening
  if not by telling. A chair that links to a shop is a chair
  for sale, and the page would rather have no chair.
- **Failure fallback.** No JS: chair printed, caption printed,
  ember absent (the ember is JS-drawn; its absence costs the
  scene nothing). Canvas unavailable: no ember; the glow rise
  is CSS and still happens. Nothing in this element can strand:
  it has no pre-state at all — the only element in the theme
  that ships exactly as it rests.
- **Reduced-motion variant.** Identical, minus the ember's
  journey: the ember is simply present on the arm (drawn in
  the SVG) — the stillest element gets stiller by one ember's
  walk.
- **Performance budget & mobile variant.** One pre-carved SVG
  ≤18KB, one glow opacity, ≤1 particle. Mobile: the chair
  scales to the column; the section's dark edges narrow; the
  caption stays 0.9375rem — some things are not responsive,
  and a caption's size is one of them (it wraps to two lines
  instead, centred).
- **Choreography timeline (v2).** Section approaches → reading
  line crosses the chair's seat → t=0 glow +8% begins (1400ms)
  → t=600 the single ember lifts from the hearth side →
  t=2700 ember settles on the arm → rest. Scrolling away and
  back: nothing replays; the ember is where it landed.
  Watchdog: none — there is no state to rescue.
- **State matrix (v2).** *Rest:* lit chair, ember on arm.
  *Hover:* link warms only. *Focus:* link ring. *Active:* the
  link's §6.9 thunk (small — even here, choosing answers).
  *Scrolled-past:* unchanged. *Disabled / no-JS:* printed
  chair, no ember. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: chair plate 480px, section
  padding 144px. 768–1199px: 400px, 112px. <768px: column
  width (≤340px), 90px, caption wraps centred.
- **Edge cases & failure modes (v2).** *Two empty chairs on
  one page* (a long archive): forbidden at build — one chair
  is an invitation; two is a furniture shop. Long pages place
  it once, after the third tale group, and later groups end
  with §6.15 instead. *The chair beside §6.7's pinned chair:*
  never adjacent — §6.7's chair is the teller's (a presence),
  §6.13's is the guest's (an absence); the page keeps at least
  one tale section between them so the two statements do not
  blur. *Caption edited by a client:* the string is fixed in
  §12 and the gate greps for it verbatim.
- **Accessibility spec (v2).** The plate is `role="img"`,
  labelled "An empty chair by the fire, its cushion green,
  waiting." The caption is plain text at 7.61:1. The link's
  accessible name is "Tell one — send in a tale of your own"
  (the visible text stays "Tell one"; the name carries the
  errand).
- **Tokens consumed (v2).** `--moss`, `--parchment-dim`,
  `--ember`, `--ease-kindle`, `--ease-drift`, `--dur-chair-glow`
  (1400ms), `--dur-chair-ember` (2100ms).

### 6.14 The take-a-seat form

- **What & why.** The conversion section is a fireside
  invitation, not a funnel: "Pull up a chair." A guest-book
  form set on a hearth-stone panel (`--brick` ground,
  `--parchment` text at 6.73:1) — name, email, and the evening
  chosen (a select styled as the guest book's ruled lines) —
  with the chair tally (§6.10) printed at the panel's head:
  "Fourteen chairs. Three still by the fire." Submitting takes
  a chair: the tally steps down by one, a notch darkens, and
  the confirmation is spoken in the teller's voice (§12). It
  belongs because in this theme conversion is *hospitality
  accepted* — the visitor is not captured, they are seated.
- **Structure.** A real `<form>` with real labels (Cormorant
  500, above their fields — a guest book is signed in the open),
  inputs as ruled lines: transparent ground, a 1px `--iron`
  underline on the panel's brick (printed as parchment-dim at
  rest on brick — contrast ruled below), focus brings a candle
  to the line: the underline warms to `--ember-hot` and a soft
  glow gathers at the field's left edge, as if light were
  brought near to write by. The submit is the theme's primary
  button (§11): an iron-bound `--beam` block, carved label "Take
  your seat". The seat tally at the panel head is a live region
  (`aria-live="polite"`) — it is the form's own arithmetic,
  printed, per §6.10's doctrine: chairs total, chairs taken,
  chairs remaining, all three printed, the subtraction shown.
- **Motion spec.** Field focus: underline + glow over 300ms
  `--ease-kindle`; blur: glow banks over 500ms `--ease-bank`
  (light is taken away more slowly than it is brought — the
  room is reluctant). Error: the field's line turns `--ember`
  (never red — there is no red in a cottage) and the message
  appears beneath in the teller's voice (§12's strings), with a
  single small ember-shake: the line translates 3px twice over
  180ms — a head shaken once, gently. Submit: §6.9's thunk on
  the button, a spark puff from the panel's hearth side, then
  the panel's content crossfades 600ms to the confirmation: a
  carved seat number ("Your chair is the eleventh"), the tally
  stepping (§6.10's ±1), and the evening's details restated.
  The form never spinner-loads longer than 1200ms; beyond that
  the button's label becomes "The kettle is on…" (§12) — a
  wait acknowledged in the room's words, capped at a further
  8000ms before an honest error.
- **States.** Rest: panel lit, tally printed, fields empty
  lines. Focus: candle brought. Filled: the line stays warm at
  50% (a written line keeps some light). Invalid: ember line +
  voice message; the entered text is never cleared by an error
  — a guest book does not eat signatures. Submitting: button
  dipped, label held. Success: confirmation state (the form is
  replaced, not hidden — `hidden` attribute swapped, focus
  moved to the confirmation heading). Full (0 chairs): the form
  is replaced at build/render by the banking state — "The
  chairs are all taken for Thursday. The next telling is
  Sunday." + a waitlist field — never a disabled form sitting
  like a locked door.
- **Content merge.** Every string is the event's own: the
  evenings in the select are real tellings with real dates;
  the tally is the real chair count of the real room; the seat
  number in the confirmation is the tally's own arithmetic
  (taken + 1). A demo form with lorem evenings seats no one.
- **Failure fallback.** No JS: the form posts plainly to its
  endpoint and the confirmation is a page (§6.17's transition
  absent, the page simply loads, lit). JS validation never
  replaces server validation; with JS dead, native validation
  + the server's error page (styled by §11's alert) carry it.
  Submission failure (network): the entered values persist in
  place, the error is §12's honest string, and nothing about
  the tally changes — no chair is taken by a failed knock.
- **Reduced-motion variant.** No shake, no puff, no crossfade:
  states change instantly; the focus candle becomes a static
  warm underline. The confirmation still arrives and focus
  still moves to it.
- **Performance budget & mobile variant.** The form is HTML +
  ≤6KB JS (validation + tally). Mobile (<768px): the panel
  goes full-column, fields stack, the tally wraps above the
  first field, submit is full-width ≥52px tall — a chair taken
  one-handed, in the dark, by a person holding a cup.
- **Choreography timeline (v2).** Panel kindles with its
  section (§6.2) → tally counts (§6.10's timeline) → focus:
  candle 300ms → submit press: thunk t=0, puff t=40 (§6.9) →
  response ≤1200ms (or kettle label) → t=resp confirmation
  crossfade 600ms, seat numeral steps at +200ms, notch darkens
  at +500ms → focus lands on the confirmation heading at fade
  end. Watchdog: 9200ms total → honest error state, values
  intact.
- **State matrix (v2).** *Rest:* as above. *Hover:* fields'
  lines warm 20% (a hand hovering over the book). *Focus:*
  candle full. *Active:* button dip. *Scrolled-past:* the
  panel rests told; a completed form stays completed behind
  the reader. *Disabled:* only the full-house banking state
  replaces the form — individual fields are never disabled
  mid-flow. *Touch:* focus candle on tap-in; targets ≥48px.
- **Breakpoints (v2).** ≥1200px: panel 640px, two fields abreast
  (name/email), evening select full width. 768–1199px: panel
  560px, fields stack. <768px: panel full column, all stacked,
  submit 52px.
- **Edge cases & failure modes (v2).** *Two visitors take the
  last chair at once:* the server's count rules; the loser
  gets the banking state with §12's string and a waitlist
  offer — the page never confirms a chair it does not have
  (the tally is arithmetic, not theatre). *Long names / RTL
  names:* ruled lines grow to two lines gracefully; the candle
  glow anchors to the writing side (logical properties
  throughout). *Autofill:* filled fields take the warm state
  on input events, so an autofilled book looks signed, not
  haunted. *The select's evenings sell out while the page is
  open:* on submit the server re-offers; the page re-renders
  the select with the taken evening struck through in dim —
  the guest book shows the full page, crossings-out and all.
- **Accessibility spec (v2).** Labels are visible, persistent,
  and programmatically bound; errors are tied by
  `aria-describedby` and announced once; the tally live region
  is `polite` and speaks only the remaining count ("Two chairs
  still by the fire"). Contrast: parchment on brick 6.73:1 for
  text; input text is `--parchment-cream` on brick-deep field
  wells (the fields sit in shallow `--brick-deep` wells,
  9.1:1) — ruled lines alone were tested and rejected for text
  entry contrast; the wells are the ruling. Focus ring: §11's,
  doubled on the panel (a ring on brick needs the cream offset).
- **Tokens consumed (v2).** `--brick`, `--brick-deep`,
  `--parchment`, `--parchment-cream`, `--parchment-dim`,
  `--ember`, `--ember-hot`, `--iron`, `--beam`, `--ease-kindle`,
  `--ease-bank`, `--dur-candle-field` (300ms),
  `--dur-form-fade` (600ms).

### 6.15 The banked next tale

- **What & why.** At a tale's end, the page banks the fire and
  points onward: a closing block — the tale's fleuron, its last
  line restated as a carved colophon, and the next tale offered
  as a chapbook spine (§6.12's cover language, laid horizontal):
  plate thumb, title, measure. As the block nears the reading
  line the next tale's title begins to warm — not its §6.3
  ceremony, only a pre-kindle to `--parchment-dim` — because
  the next story is already catching a little of this one's
  light. It belongs because a fireside evening never ends with
  a void and a footer: the teller says "and after that, there
  is the one about…" and the room stays.
- **Structure.** A `<footer>` inside the tale's `<article>`:
  fleuron rule (§11), the colophon line ("So ends the tale of
  the Wolf at the Door — told in two logs"), then the next-tale
  link as a horizontal card. If there is no next tale (the last
  of the evening), the block offers §6.13's chair instead — the
  evening ends with the invitation, never with a dead end or a
  "related posts" grid. The block is printed complete; only the
  pre-kindle tint is JS-armed.
- **Motion spec.** The colophon kindles with its section
  (§6.2). The next title's pre-kindle: scrubbed like §6.2 but
  capped at k=0.55 (dim) — full kindling is earned on its own
  page. Hover/focus on the card: §6.8's stir + the title warms
  past its cap to full cream (attention completes what
  proximity began). Click: §6.9's thunk, §6.17's transition.
  The fleuron draws itself (§11's fleuron spec: stem, two
  scrolls, ember heart) over 600ms `--ease-carve` as the block
  kindles — the evening's punctuation, carved.
- **States.** Rest: colophon lit, next title dim-warm.
  Hover/focus: stirred, title cream. Active: thunk.
  Scrolled-past: rests told. Disabled: if the next tale is
  banking (unpublished), the card shows its silhouette + date
  (§6.12's banking treatment) and is not a link — the teller
  may promise a tale for Thursday, and the promise is the
  content.
- **Content merge.** The colophon restates *this* tale's own
  last line and measure; the card is the actual next tale in
  the collection's order — never an algorithmic "you may also
  like". A storytelling page that recommends by engagement has
  mistaken the room for a feed.
- **Failure fallback.** No JS: block printed, next title at
  full parchment (the pre-kindle cap is a JS state; without it
  the title simply prints lit — slightly less theatre, no lost
  meaning). Fleuron ships drawn.
- **Reduced-motion variant.** Fleuron printed whole; pre-kindle
  absent (title prints parchment); hover warm retained (colour,
  not motion).
- **Performance budget & mobile variant.** One small SVG, one
  capped kindle. Mobile: the horizontal card stacks (plate
  above title), the colophon centres — an ending read on a
  phone is still an ending.
- **Choreography timeline (v2).** Block enters kindle span →
  colophon warms (§6.2) → fleuron carves 600ms at k≥0.4 →
  next title pre-kindles to its 0.55 cap as the block crosses
  the line → rest. Watchdog: §6.2's 1600ms covers the block.
- **State matrix (v2).** *Rest:* as above. *Hover:* stir +
  title cream. *Focus:* same + ring. *Active:* thunk.
  *Scrolled-past:* told. *Disabled:* banking card, unlinked.
  *Touch:* tap-down stir, then thunk.
- **Breakpoints (v2).** ≥1200px: horizontal card, plate 120px.
  768–1199px: horizontal, plate 96px. <768px: stacked card.
- **Edge cases & failure modes (v2).** *The next tale is the
  reader's current tale* (a one-tale collection): the block
  falls back to the chair (§6.13) — never link a tale to
  itself. *Series order changed in the CMS:* the block reads
  the collection's declared order at render; it computes
  nothing at runtime, so it cannot recommend a tale that was
  removed — a removed next tale renders the chair.
- **Accessibility spec (v2).** The card is one link with the
  composed name (§6.12's pattern: "Next tale — The Miller's
  Daughter, a one-log tale"). The colophon is a paragraph, not
  a heading — the tale's heading outline ends clean.
- **Tokens consumed (v2).** `--parchment`, `--parchment-dim`,
  `--parchment-cream`, `--ember`, `--ease-carve`,
  `--ease-kindle`, `--dur-fleuron` (600ms), plus §6.2's set.

### 6.16 The banked-fire footer

- **What & why.** The page ends the way the evening ends: the
  fire is banked. The footer is a `--beam` mantel-beam band over
  `--soot-deep`: the site's colophon carved into the beam
  ("Tales by the Hearth — kept by the Winter Book Society"),
  the room's links as a quiet row, and beneath, the glow at its
  lowest — the ember bed at rest, a wide, dim radial that
  breathes at half the page's amplitude. Reaching the footer is
  what tells §6.6's log to settle into ash. And the footer holds
  the way back: "Stoke the fire" — a link that returns to the
  top and, on arrival, re-stokes the hero's glow in a brief
  900ms swell (the one licensed replay of §6.1's warmth, at
  resting scale). It belongs because a Hearth page must *end*,
  not stop: banking the fire is a promise that it will be lit
  again.
- **Structure.** A real `<footer>`: colophon line, nav row
  (the mantel's objects again, unlit — the shelf seen from
  across the room), a small-print line (copyright in the room's
  words, §12), and the stoke link as a §11 secondary button.
  The ember-bed glow is a dedicated layer at depth 1 behind the
  beam, opacity keyed to the footer's own visibility. All
  content prints; the banking is a lighting state, JS-armed.
- **Motion spec.** As the footer crosses 40% viewport height:
  the page's main glow (§6.1's layer) banks — opacity eases to
  40% of resting over 1600ms `--ease-bank` — while the footer's
  own ember bed rises to its rest level over the same span;
  the log (§6.6) completes its ash state. The breathing
  continues in the bed at half amplitude (±3%) — a banked fire
  is alive, only quiet. Scrolling back up un-banks symmetrically
  (this one state is *not* ratcheted: banking is about where
  the reader is, not what they have earned — the tales behind
  them stay told; only the room's light dims at its end).
  Stoke link: smooth return (§6.11's scroll) + on arrival the
  hero glow swells +20% and settles over 900ms `--ease-kindle`.
- **States.** Rest (mid-page): footer unlit-dark, bed at 0.
  Banked (footer in view): as above. Hover/focus on links:
  standard warm (§11). The stoke link focused: its ring; Enter
  performs the return. Scrolled-past: n/a — there is no past
  the footer.
- **Content merge.** The colophon names the site's real keeper
  and the small print is the real legal line — banking is a
  lighting change over real furniture, not a mood pasted under
  the page. The stoke link's target is the page's own top,
  where the hero's fire is: the gesture closes the evening's
  circle (§13's map ends where it began, banked).
- **Failure fallback.** No JS: footer prints lit at resting
  glow (the banking never arms); links are links. The stoke
  link is a plain `#top` anchor without JS.
- **Reduced-motion variant.** No banking journey: the footer
  zone simply uses the bed's rest level as its static lighting
  (a printed difference, not an animated one). The stoke return
  is an instant jump, no swell.
- **Performance budget & mobile variant.** Two opacity
  animations on existing layers; nothing new is built.
  Mobile: the beam stacks (colophon, links in two columns,
  small print), the stoke button full-width — the way home is
  easy to find in the dark.
- **Choreography timeline (v2).** Footer at 40% viewport →
  t=0 banking begins (1600ms, both layers) → log's ash state
  completes at the same t=1600 (the loop drives all three from
  one fraction, so they cannot disagree) → bed breathing at
  half amplitude → (stoke clicked) scroll ≈900ms → arrival
  swell 900ms → rest. Watchdog: §6.2's loop watchdog snaps
  banking to the footer's true visibility fraction.
- **State matrix (v2).** *Rest:* unbanked page, dark footer.
  *Hover:* link warms. *Focus:* rings per §11. *Active:* stoke
  thunk (§6.9). *Scrolled-past:* n/a. *Disabled / no-JS:*
  printed lit footer. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: beam in one row (colophon
  left, links right). 768–1199px: two rows. <768px: stacked,
  links two columns, stoke full-width.
- **Edge cases & failure modes (v2).** *A short page* (footer
  visible at load): the page ships banked — correct: a one-tale
  evening is already at its end, and §6.6's log is not rendered
  (§6.6's rule), so nothing disagrees. *Footer taller than the
  viewport* (a fat footer): banking triggers on its top at 40%,
  not its foot — the room dims as the end *begins*. *Print:*
  the footer prints as small print on white-free paper stock —
  glows and beds are screen-only states.
- **Accessibility spec (v2).** Footer landmark with the colophon
  as text; banking never drops any footer text below
  `--parchment-dim` on `--soot-deep` (7.9:1 — dim's ratio on the
  deeper ground, recomputed, not assumed). The stoke link's
  name is "Stoke the fire — back to the top".
- **Tokens consumed (v2).** `--beam`, `--soot-deep`,
  `--parchment`, `--parchment-dim`, `--ember`, `--ease-bank`,
  `--ease-kindle`, `--dur-bank` (1600ms), `--dur-stoke-swell`
  (900ms).

### 6.17 Smoke transition & the first-spark loader

- **What & why.** Moving between pages of the cottage passes
  through smoke and a turning leaf: a haze of `--smoke` drifts
  across the glass (500ms), the leaf turns (§6.5's language,
  faster, as a door between rooms), and the new page kindles
  from its hero. First load has its own small ceremony — the
  *first spark*: before the hero's cold hearth stands ready, a
  single spark point glows at the hearth's centre and the room
  assembles around it. It belongs because in a cottage you do
  not teleport between evenings; you pass through the smoke of
  the doorway. Both ceremonies are ceilings, not floors: the
  transition aborts on any input, and the loader may never hold
  content hostage — the DOM is server-rendered and complete
  beneath both.
- **Structure.** Transition: one fixed overlay (`aria-hidden`,
  `pointer-events: none`) with two layers — a smoke layer
  (two `--smoke` radial fields drifting in opposition, blur
  30px, opacity to 88%) and the leaf (§6.5's clip panel,
  compressed timing). Loader: a hearth-centre spark (a 10px
  radial disc, `--ember-hot` core) inside the hero's fireplace
  SVG position, present only while `document.readyState` is
  incomplete *and* the hero's own content is not yet painted —
  in practice a sub-second state on any real connection; the
  spark is inline in the hero HTML so it exists from first
  paint without JS. Skeleton states for in-page loads (archive
  filtering, §11) use unlit silhouettes: `--smoke` shapes of
  the thing coming (card-shaped, tally-shaped), no shimmer.
- **Motion spec.** Transition out: smoke rises 0→88% over
  300ms `--ease-drift`, leaf turns 380ms `--ease-curl` at the
  smoke's peak; navigation swaps beneath; transition in: the
  new page's hero is at its cold/armed state, smoke clears
  88→0 over 400ms `--ease-drift` as the stoke (§6.1) takes
  authority. Total ≤1200ms, and any click, keypress or scroll
  during it cuts straight to the cleared state. Loader spark:
  the disc swells 6→14px and its glow gathers over 700ms
  `--ease-kindle`, then holds steady (a spark does not pulse);
  when the hero paints, the spark becomes the hearth's first
  ember — the same disc, handed to §6.1's canvas as its first
  particle — and the ceremony is over, typically before it was
  noticed.
- **States.** Idle: no overlay. Leaving / arriving: as above.
  Aborted: cleared instantly, destination page fully lit (an
  aborted ceremony never leaves smoke over content — the law).
  Loader: sparking → handed over → absent. Skeleton: unlit
  shape → content kindles in (§6.2) — skeletons never fade out
  over a fade-in; the shape is *replaced* by the lit thing.
- **Content merge.** The smoke is the site's own weather (the
  hearth's smoke, §5's drift vocabulary) and the leaf is the
  book's own furniture — the transition is built from the
  room's materials, not a branded wipe. The loader spark sits
  in the actual hearth of the actual hero it precedes.
- **Failure fallback.** No JS: plain navigation, no overlay,
  no spark (the spark without JS is a static ember in the
  grate — printed as part of the fireplace SVG's cold state,
  unlit: a drawn spark, grey). Transition script dead mid-route:
  the overlay has a 1400ms self-clear timer independent of the
  router. Slow network on the destination: the new page's own
  spark + skeletons hold the room; the transition layer never
  re-engages to cover a slow page twice.
- **Reduced-motion variant.** No smoke, no leaf, no swell:
  navigation is instant; the spark is a steady small ember;
  skeletons are static shapes. Moving between rooms is a cut,
  and the rooms themselves carry the theme.
- **Performance budget & mobile variant.** Overlay layers are
  pre-built and reused (one DOM node for the site's life);
  blur is on the overlay only, 680ms maximum. Mobile: the leaf
  is dropped (smoke only, 700ms total) — a small screen's
  doorway has no room for a turning leaf, and §6.5's mobile
  doctrine agrees.
- **Choreography timeline (v2).** Click (§6.9 thunk at t=0) →
  t=160 smoke begins → t=460 smoke at peak, leaf turns (380ms)
  → t≈620 route swaps beneath → new page: smoke clears
  t=620–1020 while hero arms its stoke → t=1200 ceiling: all
  layers removed. Loader: first paint (spark at 6px) → swell
  700ms → hero painted → spark handed to canvas → gone.
  Watchdog: overlay self-clears at 1400ms, unconditionally.
- **State matrix (v2).** *Rest:* no overlay. *Hover:* n/a.
  *Focus:* any focus change during transition aborts it.
  *Active:* input aborts. *Scrolled-past:* n/a. *Disabled /
  no-JS:* plain navigation. *Touch:* identical, minus the leaf
  under 768px.
- **Breakpoints (v2).** ≥1200px: smoke + leaf, ≤1200ms.
  768–1199px: smoke + leaf, ≤1100ms. <768px: smoke only,
  ≤700ms.
- **Edge cases & failure modes (v2).** *Back button:* the
  transition does not fire on history navigation (the reader
  stepped back through the doorway themselves; the room does
  not perform for it) — pages restore from cache in their told
  state (tales told stay told within the session). *Prefetch
  hover:* links prefetch on hover where the platform allows,
  so the transition's swap is usually instant and the ceremony
  is mostly smoke — the budget is spent on atmosphere, never
  on waiting. *A route that errors:* the smoke clears onto
  §6.18's cold hearth, which handles its own lighting.
- **Accessibility spec (v2).** The overlay is `aria-hidden` and
  never traps focus; route changes move focus to the new
  page's `<h1>` (or the skip target) after the swap, and the
  change is announced by the title, not by the smoke.
  `aria-busy` is set on the main landmark only during skeleton
  states, and cleared on replacement.
- **Tokens consumed (v2).** `--smoke`, `--ember-hot`,
  `--beam`, `--ease-drift`, `--ease-curl`, `--dur-smoke-out`
  (300ms), `--dur-leaf-route` (380ms), `--dur-smoke-in`
  (400ms), `--dur-spark` (700ms), `--dur-watchdog-route`
  (1400ms).

### 6.18 The cold hearth (404)

- **What & why.** A wrong turning in the cottage leads to a
  room with a cold hearth: the page is the cottage at its
  darkest — an unlit fireplace, one chair, the tale that was
  sought named and not found ("The tale of the Miller's
  Daughter is not in this room"). In the grate sits a single
  unlit match's worth of hope: a button, "Strike a light",
  which kindles a small warm radius around the room's real
  ways back — the shelf of tales, the chair, the home hearth —
  presented as three lit links. It belongs because even the
  error page is a room in this house, and its job is the
  theme's job in miniature: someone is in the dark; bring
  light; offer a seat. The comedy is gentle and the help is
  real — the sought slug is echoed, and the nearest real tales
  (by the site's own catalogue order, §6.15's doctrine) are the
  links.
- **Structure.** A complete page, not an overlay: hero-less,
  the cold fireplace SVG (§6.1's hearth, unlit variant — stones
  in `--smoke` tones, no glow layer armed), the not-found
  statement in Cormorant at full `--parchment` (the *message*
  is never cold — only the room is), the strike button (§11
  primary), and the three way-back links present in the DOM
  from first paint inside a region whose *lighting* is armed:
  the links print at `--parchment-dim` (7.61:1 — readable
  before any strike; the strike adds warmth, never access).
- **Motion spec.** Strike: the button thunks (§6.9, small);
  a match-flare radial (a dedicated small glow layer, 30vmax
  cap — a match lights a corner, not a room) gathers over
  600ms `--ease-kindle` centred on the links region; each link
  kindles in stagger 120ms and its fleuron warms; 3 embers
  lift from the struck point and settle. The light *stays*
  (no fade-back — a struck match here lights the lamp, and the
  lamp stays lit while the visitor chooses). A second strike
  does nothing (the lamp is lit; the button's label becomes
  "The lamp is lit" and it disables honestly).
- **States.** Cold (armed lighting, links dim-readable) →
  struck (lamp lit, links warm). No-JS: the page ships in the
  struck state (lamp pre-lit as a static gradient) — a
  scriptless visitor in a dark room gets the light first and
  the ceremony never. Reduced motion: ships struck, like no-JS.
  Hover/focus on links: §11's warms; focus does not require the
  strike — keyboard visitors find lit-enough links (7.61:1)
  and may strike or not as they please.
- **Content merge.** The not-found statement names the actual
  requested path in the room's words; the three links are the
  site's real nearest tales and its real home — computed at
  render from the catalogue, never a generic "helpful links"
  box. The cold hearth is §6.1's own fireplace, unlit: the
  error is *in* the world, not pasted over it.
- **Failure fallback.** The page is static-complete by
  construction: every failure mode above degrades toward
  *more* light, never less. If the glow layer fails, links
  remain dim-readable; if the button's script dies, the strike
  is a form post that reloads the page in its struck state
  (server-set), so the ceremony has a no-JS twin.
- **Reduced-motion variant.** Ships struck (above). The button
  remains for parity but reports the lamp already lit.
- **Performance budget & mobile variant.** The lightest page
  on the site: one SVG, one small glow, ≤3 particles. Mobile:
  the room stacks (hearth, statement, button, links full
  width) — a small dark room is still a room.
- **Choreography timeline (v2).** Page load: cold room, dim
  links → strike at t=0: thunk → t=40 one spark → t=0–600
  match-glow gathers → links kindle at t=200/320/440 →
  t=900 lamp at rest, embers settled → choice made at leisure.
  Watchdog: none — every state is a resting state.
- **State matrix (v2).** *Rest (cold):* dim-readable links.
  *Hover:* link warms (independent of strike). *Focus:* ring;
  strike optional. *Active:* thunk. *Scrolled-past:* n/a.
  *Disabled / no-JS:* ships struck. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: room centred, hearth 560px,
  links in a row of three. 768–1199px: hearth 440px, links
  row. <768px: stacked, links full-width rows.
- **Edge cases & failure modes (v2).** *A 404 for an asset*
  (missing image): the server returns this page only for
  document routes; assets fail plainly — a broken plate in a
  tale renders §6.12's drop-capital fallback, not a whole cold
  room for one picture. *The sought tale exists but moved:*
  that is a redirect, not a 404 — the cottage does not send
  guests to the cold room when the tale is two doors down.
  *Repeated strikes / refresh:* the struck state is per-page-
  load, not stored — each arrival is a fresh cold room, because
  the ceremony is short and the honesty is the point.
- **Accessibility spec (v2).** The not-found statement is the
  `<h1>` ("That tale is not in this room"), at 13.60:1 from
  first paint — the one thing on the page that is never dim.
  The strike button is a real button with a real label; links
  are links with composed names (§6.12's pattern). HTTP status
  is a true 404 — the theme performs many things, but never a
  soft-404.
- **Tokens consumed (v2).** `--smoke`, `--soot-deep`,
  `--parchment`, `--parchment-dim`, `--ember-hot`, `--ease-kindle`,
  `--dur-strike` (600ms).

## 7. Page application map

**Home (the evening's opening).** The full arc: stoked hearth
hero (§6.1) whose title is the evening's first tale → that tale
kindles in full (§6.2) with its woodcut (§6.4) → the pinned
chair with three featured tales (§6.7) → the empty chair
(§6.13) → the tally board (§6.10) → the take-a-seat form for
the next telling (§6.14) → the banked footer (§6.16). One curl
(§6.5) at the chapter joint before the chair, one before the
tallies. This is the only page type that runs the whole room.

**Tale page (a single story).** No hero stoke — the tale
begins at a lit hearth (the session's fire is already caught;
§6.1's returning rule) with the title's ember-lit ceremony
(§6.3) as the page's one flourish. The tale kindles section by
section if long (§6.2), its plates carve (§6.4), the log burns
(§6.6), and it ends at §6.15's banked next tale. The form does
not appear on tale pages — you do not pass a guest book during
a story.

**Archive / listing (the shelf).** Chapbook cards (§6.12) in
the two-chair shelf, one featured tale with the §6.3 ceremony,
leaf pagination (§11) between shelves, the tally board as the
archive's head ("Tales in the winter book: 212 — counted from
the shelf itself"). No chair scene, no empty chair (the shelf
is a working room, not an evening), no stoke — returning
readers are already by the fire.

**About (the keeper's page).** The cottage's own tale: who
keeps the fire, told as a tale — kindling text, one woodcut
(the keeper's cottage), the tallies as the society's record.
The empty chair belongs here if the society takes tellers;
§6.13's link rules apply unchanged.

**Booking / contact (take a seat).** §6.14's form is the page:
a short kindling standfirst, the hearth-stone panel, the
tallies of chairs. Nothing else competes — no chair scene, no
cards. The confirmation is a page state, not a modal (§11
refuses modals for confirmations; a seat taken is a place, not
a popup).

**Search (the candle in the archive).** A search field styled
as §11's input with a candle-focus; results are chapbook rows
(§6.12's language, horizontal) that kindle as they arrive;
the empty result is §12's line — "No tale in the book answers
to that name. Try the teller's own words." — with the shelf
link. Search never kindles per keystroke (a candle does not
flicker at typing); results kindle once, on arrival.

**The cold hearth (404).** §6.18, whole and unchanged on every
site in this theme.

## 8. Worked examples

### 8.1 The hero — "The Wolf at the Door", a folklore publisher's home

The site is *Hearthside Tales*, a small folklore publisher.
The home hero is §6.1 built exactly as specced. The fireplace
SVG sits at the hero's foot: stone surround in `--brick` with
`--brick-deep` mortar shadow, an `--iron` grate, two `--beam`
logs. Above it, the standfirst in Cormorant italic
(`--parchment-dim`): *"Stories told the way they were earned —
seated, and by firelight."* Above that, the `<h1>` in Pirata
One at 5.5rem: **The Wolf at the Door** — the evening's first
tale, whose opening lines stand beneath the standfirst as the
hero's third tier, so the stoke lights a story, not a slogan.

Scroll timeline: the visitor's first scroll begins the stoke.
At s=0.15 the first ember lifts from the grate. At s=0.4 the
glow's edge (radius now ≈44vmax) reaches the title's baseline
and the standfirst warms through `--parchment-dim`. At s=0.55
the title's letters begin their §6.3 stagger — *T-h-e W-o-l-f…*
catching left to right, 55±18ms a letter, each peaking
`--parchment-cream` before settling — while the hero's opening
lines kindle on §6.2's curve beneath. At s=1 (120vh scrolled)
the cold veil is removed, the breathing takes over on its
three unsynchronised cycles, and the reader is simply *reading
a lit tale* — the ceremony has dissolved into the evening.
A returning visitor that session finds the fire caught and the
tale lit, and a keyboard visitor's first Tab completes the
catch without a pixel of scroll. Word count of the hero's
copy: 41. The publisher's name appears once, carved on the
mantel (§6.11), not in the hero — the tale is the hero.

### 8.2 Mid-page — the three tales by the chair, a heritage cottage site

The site is a storytelling cottage in a heritage village; the
home page's middle is §6.7. The chair plate (pre-carved
woodcut, 30KB SVG: a high-backed chair, cushion in `--moss`,
the hearth's edge at frame-left) pins at stage-left while
three summaries tell at stage-right, each a real tale from the
cottage's repertoire: *The Miller's Daughter* (a one-log
tale), *Why the Sea Is Salt* (two logs), *The Thirteenth
Guest* (three logs, the long one, told last — the order is a
programme, shortest first, because the evening warms up).

Scroll timeline: the stage pins as its top reaches the
viewport top. Tale 1 stands full `--parchment`, its carved
number warm; tales 2 and 3 rest at 55% dim print — readable
shapes, honestly present. Through the first third the fire
breathes and nothing else moves: the held pause is the point.
Across the crossfade window (the middle 40% of the second
third, ≈120vh of travel) tale 1 dims as tale 2 rises and its
number warms; the glow leans +4% toward the active side. The
third tale rises the same way, and in the final hold the
stage's only motion is the fire. The stage releases into
§6.5's curl — the declared chapter joint — and behind the
reader the section rests with all three summaries lit, a told
programme. On a phone the same content is a 220vh pin with
the chair as a band above the summaries; under reduced motion
it is a stack, and the cottage has lost a stage trick and no
stories.

### 8.3 The conversion section — "Thursday's Telling", seats for the evening

The cottage takes bookings for its Thursday telling. §6.14's
panel stands on `--brick`: at its head, the tally in carved
numerals — **Fourteen chairs. Ten taken. Four still by the
fire.** — the arithmetic printed, sourced ("from the guest
book, this week"). The evenings select offers *Thursday's
Telling — The Thirteenth Guest* and *Sunday's Telling — Why
the Sea Is Salt*; the select's lines are the guest book's
ruled lines. A visitor, Maren, writes her name (the field's
candle gathers at the line's left), her email, chooses
Thursday. On submit: the button thunks, a puff of sparks
rises from the panel's hearth side, and within the response
the panel crossfades to the confirmation — *"Your chair is
the eleventh, Maren. Come when the light goes; the first tale
is at seven."* — while the tally at the panel's head steps:
ten taken becomes eleven, four remaining becomes three, and a
fresh notch darkens on the board's edge. If Thursday fills,
the panel is replaced at render by the banking state and
Sunday is offered with a waitlist line for Thursday — never a
greyed form. Every number Maren saw was the room's real count;
the confirmation's seat number is the tally's own sum, and
§10's gate recounts it.

## 9. Anti-slop — what makes THIS theme look cheap

1. **The pulsing fire.** A glow that breathes on one tidy
   sine — 4s up, 4s down — is a lava lamp. *Cure:* the three
   incommensurate cycles (§5); if the breathing can be counted,
   it is wrong.
2. **Ember confetti.** Particles everywhere — over the footer,
   the form, the prices — pretty, meaningless, and a breach of
   the law's second clause. *Cure:* two sources only (hearth,
   attended tales), a page budget (§14), and the gate's ember
   census.
3. **Ash that strands.** A reveal that leaves a tale grey
   because a trigger was missed is this theme's version of the
   invisible-heading defect: darkness as a bug. *Cure:* printed
   parchment beneath every tint, watchdogs everywhere (§6.2),
   and the reading-line test in §10.
4. **Blackletter everywhere.** Pirata One on buttons, nav,
   body headings — the fancy-dress shop. *Cure:* §3's ration
   (three settings per viewport) and the gate's census.
5. **The Halloween drift.** Orange + black + spooky type
   sliding toward a haunted-house theme: cobweb corners,
   gothic clip-art, purple accents. *Cure:* the palette is a
   *warm room at night* — brick, moss, beam and parchment are
   the majority experience; the moment the page reads "spooky"
   instead of "hospitable", saturation of `--ember` is the
   first suspect (§2's 5% cap).
6. **A crowded mantel.** Nine nav items, three badges, a
   search box and a bell on the shelf. *Cure:* six objects
   (§6.11); the rest goes in the drawer.
7. **Dashboard tallies.** Counts without source lines, counting
   from zero, in a sans. *Cure:* §6.10 entire — carved,
   sourced, finished not started.
8. **The fake-old skin.** Parchment textures, torn edges and
   sepia photographs pasted over a generic layout. *Cure:*
   the theme has no textures at all — its age is in its
   *physics* (kindling, carving, burning), not in clip-art
   ageing. If removing the motion leaves a themed template,
   the build was a skin.
9. **Curl spam.** Page-curls on every section boundary, hover,
   click. *Cure:* declared chapter joints only, ≤6 per page,
   spent once each way (§6.5).
10. **The bright-room lie.** Shipping a "light mode" toggle
    that inverts to parchment-and-soot and calling it the same
    theme. *Cure:* §2's ruling — there is no light scheme; the
    honest answer to noon sun is the contrast, which holds,
    and the mood, which is frankly lost.
11. **A chair with a button on it.** The empty chair (§6.13)
    given a pulsing "Submit your story!" CTA. *Cure:* the
    caption, verbatim, and one quiet link below it. The gate
    greps the caption.
12. **Sound.** Crackling-fire audio, autoplayed or toggled.
    *Cure:* refused entirely — the theme is silent; the one
    licensed vibration is §6.9's 8ms, off where platforms gate
    it. A website that crackles is a website that gets closed.

## 10. Quality gate

Blocking — every item must pass before this theme ships in a
build:

1. **Reading-line test.** At three scroll speeds (slow read,
   reading pace, fling), no sentence is ever caught at k<1
   within the reading zone; jump-scroll to any anchor lands on
   fully lit text. (§6.2)
2. **No-JS test.** With JavaScript disabled the page is
   complete: every tale at full parchment, woodcuts printed,
   form submittable, 404 pre-lit. (§6 passim)
3. **Ember census.** Particles originate only from the hearth
   bed and attended tales; live count never exceeds §14's cap;
   zero embers over the form panel except §6.14's own puff.
4. **Glow audit.** The glow layer is under all text; resting
   opacity ≤ `--glow-ambient-max`; ember+ember-hot ≤ ~5% of
   pixels at rest (screenshot histogram at three scroll
   positions).
5. **Blackletter census.** ≤3 Pirata One settings per viewport
   at every scroll position; none below 1.5rem; none on a
   control.
6. **Tally audit.** Every tally's source line present; the
   notch count on each board's edge equals its numeral's tens;
   §6.14's seat arithmetic recounts by hand from the printed
   figures.
7. **Caption verbatim.** §6.13's caption greps exactly:
   *"For whoever is telling it next."* — one empty chair per
   page, no button on it.
8. **Watchdog drill.** With the rAF loop artificially stalled,
   every armed element reaches its final state inside its
   watchdog ceiling (hero 3000ms, kindle 1600ms, carve 4000ms,
   curl 1100ms, route 1400ms).
9. **Reduced-motion pass.** `prefers-reduced-motion` yields:
   steady glow, no embers rising, no curl, no pin, no stagger —
   and every tale lit, every plate printed, the chair section
   stacked.
10. **Contrast pass.** Body 13.60:1; captions ≥7.61:1; form
    text on brick ≥6.73:1 and field text ≥9:1 in its wells;
    no text in `--brick`, `--moss` (under 24px) or `--ash`
    anywhere it can be read.
11. **Focus pass.** Every interactive element reachable and
    ringed (§11) without waiting for any ceremony: focus
    completes the hero's catch, kindles its tale, prints its
    plate, and never lands under the curl.
12. **Performance pass.** §14's budgets measured on a mid-tier
    phone: frame cost, page weight, long tasks — and the cut
    order applied in rehearsal (kill the third ambient system
    first — there must not be one to kill).

Non-blocking but recorded: the breathing must not be countable
(§9.1 — a human watches 30s and cannot name the period); the
chair scene's held pauses must feel held (a reviewer reads
tale 1's summary twice in its third).

## 11. Component inventory

Every component a real Hearth site needs, with its treatment.
Components not listed do not exist in this theme — inventing
one requires a reason the room would understand.

- **Primary button** ("Take your seat", "Strike a light"):
  `--beam` block, 1px `--iron` edge, carved Cormorant 600 label
  in `--parchment`; hover warms the edge to `--brick`; active
  is §6.9's thunk dip. Min height 48px (52px in the form).
- **Secondary button / text link:** Cormorant 500
  `--parchment-dim` with a carved fleuron before it; hover →
  `--parchment` + fleuron warms to `--ember`. The "Tell one"
  and "Stoke the fire" links live here.
- **Focus ring (all components):** a 2px `--ember-hot` outline
  offset 3px, with a 1px `--soot-deep` outer cut — the ring
  reads as a line of firelight around the thing held. Never
  removed, never replaced by a colour change alone.
- **Inputs & textarea:** §6.14's ruled lines in `--brick-deep`
  wells; Cormorant 500 `--parchment-cream` text; candle-focus
  (underline → `--ember-hot`, glow at the writing edge);
  labels above, always visible.
- **Select:** the guest book's ruled page — a well like the
  inputs, its options a native list restyled only in colour
  (the theme does not fake a dropdown's menu; a guest book
  opens, it does not pop).
- **Checkbox / radio:** a small carved box / a round ember-pot;
  checked state fills with `--ember` and a parchment mark —
  drawn in SVG, 24px targets minimum, 44px hit area.
- **Tale-length badge:** the *log badge* — a small `--beam`
  lozenge, carved numeral + "log" / "logs" ("a two-log tale"),
  the reading minutes printed beside it in dim (the arithmetic
  shown, §6.12). Never a clock icon; the room measures in wood.
- **Tally board:** §6.10 entire, as a component: `<dl>`, carved
  numerals, notch edge, source lines.
- **Table (the shelf list / programme):** rows ruled with
  `--iron` hairlines, Cormorant 500; the row being read warms
  (its own kindle); no zebra striping — a ledger is ruled, not
  striped. Numbers right-aligned in tabular figures.
- **Alert / notice:** a hearthstone — a `--brick` panel strip
  with an ember left edge; the teller's voice (§12), never an
  icon font; errors use §6.14's ember line, never red.
- **Toast:** refused as a pattern. Confirmations happen in
  place (§6.14) or not at all; a message that floats over the
  fire and vanishes is a spark with pretensions. (The one
  exception: a *saved tale* confirmation on authoring tools,
  rendered as a notch darkening on a tally — in place, by
  definition.)
- **Modal:** one licensed use — the *storyteller's note* (a
  tale's provenance, a long caption): a `--beam` panel rising
  from the hearth side over a `--soot-deep` scrim at 72%, the
  room's glow dimming behind it; Esc and scrim-click close;
  focus trapped politely and returned. Confirmations are never
  modals (§7).
- **Tabs:** *By the fire / By the window* — tale collections
  split by register (told tales / read tales): tab labels on a
  `--beam` rule, the active tab carrying the candle-dot (§6.11's
  flame, reused — one flame vocabulary per page); panels
  crossfade by kindling, never slide.
- **Accordion:** *Questions from the listeners* (FAQ): each
  question a tale-line; opening is §6.9's in-place expansion
  (the answer kindles beneath over 500ms); the marker is a
  fleuron that rotates 90° — a poker turned in the grate.
- **Pagination:** *turn the leaf* — prev/next as leaf-turn
  links (§6.5's language, unpinned) with the shelf numbers as
  carved numerals between; "Shelf 2 of 9". No infinite scroll
  (§6.12).
- **Breadcrumbs:** *the path to the cottage* — a dim Cormorant
  chain separated by carved fleurons, the current room at
  `--parchment`; used on archive depth only, never on the home
  evening.
- **Fleuron (the theme's ornament):** one SVG — a stem, two
  scrolls, an ember heart — drawn by §6.15's carve where it
  punctuates, printed where it merely separates. It is the
  only ornament; a second ornament is a second theme knocking.
- **Audio player ("Hear it told"):** where tales are recorded,
  a `--beam` bar: play as a carved triangle in an ember ring,
  progress as a small log (§6.6's language at component scale),
  time in carved numerals. The fire does not react to audio —
  the law's census is not spent on playback.
- **Skeleton:** §6.17's unlit silhouettes — `--smoke` shapes of
  the coming thing, labelled for AT with `aria-busy` on the
  region.

## 12. Content & copywriting voice

**The voice is the teller's:** seated, unhurried, second
person when inviting, never first-person-plural corporate.
Sentences are short at the joints and long in the tales.
Hearth vocabulary is used only where it is *true* — chairs,
logs, frost, the guest book — and never as decoration over
ordinary web actions (a delete is not "cast into the fire";
a password is not "the word at the door").

**Headline style.** Tale titles are the tales' real names,
in Pirata One, ≤28 characters for the lit ceremony (§6.3).
Page headlines that are not tales are Cormorant, plain-spoken:
✓ "Thursday's telling" · ✗ "Experience an unforgettable
evening of magical storytelling!" — exclamation marks are
banned from the theme's own copy entirely (a fireside does
not shout); the one exception is quoted speech inside a tale's
text, which is the tale's business.

**Labels.** Buttons are acts in the room: "Take your seat",
"Strike a light", "Tell one", "Hear it told". ✗ "Submit",
"Sign up now", "Get started". Form labels are the guest book's
questions: "Your name", "Where shall the word reach you?"
(email) — the second is the licensed flourish; a third
flourish in one form is showing off.

**Fixed strings (verbatim, grepped by the gate).**
- The empty chair's caption: *"For whoever is telling it
  next."*
- The log's labels: *"The evening is young"* / *"Mid-evening"*
  / *"The fire is low"*.
- Form confirmation: *"Your chair is the {nth}, {name}. Come
  when the light goes; the first tale is at seven."*
- Full house: *"The chairs are all taken for {evening}. The
  next telling is {next}."*
- The slow wait: *"The kettle is on…"* (§6.14).

**Error voice.** Errors are the teller pausing, not a system
objecting: ✓ "That direction won't reach anyone — check the
writing of it." (email) · ✓ "The guest book needs a name to
keep your chair by." · ✗ "Invalid email format." · ✗ "Error:
field required." Errors name the remedy in the same breath
and never blame; the word "invalid" is banned (a guest is not
invalid).

**Empty states.** ✓ "No tale in the book answers to that
name. Try the teller's own words." (search) · ✓ "The winter
book opens with the first tale." (zero tally) · ✗ "No results
found." ✗ "Nothing here yet!" — emptiness by the fire is a
kept seat, not a failure state, and is written that way.

**Numbers.** Always with their source or their arithmetic
(§6.10/§6.14): "Four still by the fire" follows "Fourteen
chairs. Ten taken." A bare number on a Hearth page is a log
with no tree named.

**Alt text & aria labels** are written in the same voice but
plainly — a label is a description, not a performance:
"An empty chair by the fire, its cushion green, waiting."

## 13. Full-page scroll choreography map

The home evening, top to footer, in order. (Tale pages and the
shelf abbreviate per §7; the map's *rules* hold everywhere.)

1. **The cold room.** First paint: printed hero beneath the
   armed cold veil; mantel shelf above, candle parked on the
   first object; log whole in the corner. Nothing has happened
   yet, and everything is readable — the evening before the
   first guest moves.
2. **The stoking (0–120vh).** The reader's scroll lights the
   room (§6.1): embers rise, glow widens, the first tale's
   title catches letter by letter, its opening lines kindle.
3. **The first tale (told).** The hero tale reads at full
   warmth; its woodcut carves as it arrives (§6.4); the log's
   edge begins its creep. Behind the reader: told, warm,
   ratcheted.
4. **The turn.** The declared chapter joint curls (§6.5) — the
   book acknowledging its own weight.
5. **The chair (300vh pin).** The room holds; three tales pass
   through the seat (§6.7); held pauses where only the fire
   moves. The candle on the mantel sits on "The Chair" for the
   whole pin.
6. **The second turn,** into the evening's second movement.
7. **More tales,** kindling one by one (§6.2), each with its
   plate; hover stirs (§6.8) answer attention anywhere in the
   told region.
8. **The empty chair.** Stillness (§6.13): one ember walks to
   the chair's arm; the caption; the quiet link. The map's
   only near-stop, placed where a banner would go.
9. **The tallies.** The winter book opens (§6.10): numerals
   finish their counts, notches stand along the board's edge.
10. **The invitation.** The hearth-stone form (§6.14); the log
    by now reads *The fire is low*; a chair taken here steps
    the tally in §6.10's board *and* §6.14's panel — one
    arithmetic, two printings.
11. **The banking.** The footer crosses; the room's glow banks
    to the ember bed (§6.16); the log settles to ash with its
    warm heart.
12. **The way back.** "Stoke the fire" returns the reader to
    the top, where the caught fire swells once, briefly — the
    evening can begin again because it was ended properly.

**Reverse-pass rules.** Scrolling up: nothing un-kindles,
nothing un-carves, the log does not un-burn, told titles stay
lit (the ratchet, §6.2/§6.6). Two things *do* reverse: the
hero's stoke, only before the catch (§6.1 — an unstoked fire
cools), and the footer's banking (§6.16 — light follows the
reader's place, warmth follows their history; the map keeps
the two apart deliberately). The curl fires once back (§6.5)
and then the joints are silent.

**Jump rules.** Anchor jumps, find-in-page landings and
restored scroll positions land on the *final* states of
everything above the landing point and the armed states of
what is below — a reader who arrives mid-evening by a jump is
treated as having been told everything before, which, in the
only sense the page can know, they have.

## 14. Whole-page performance budget

- **Page weight.** HTML+CSS+JS ≤ 190KB gzipped for the home
  evening (the heaviest page type); tale pages ≤ 140KB; the
  404 ≤ 40KB. Fonts: Pirata One (subset to Latin + the theme's
  punctuation, ≤18KB woff2) + Cormorant Garamond (400/500/600 +
  italic 500, subset, ≤64KB total) — font budget 82KB, and the
  hero's stoke is gated on `fonts.ready` raced at 800ms (§6.1's
  doctrine inherited page-wide: no ceremony in a fallback face).
- **Inline SVG.** Woodcuts ≤24KB each, ≤5 per page (§6.4);
  chair plates ≤30KB (§6.7/§6.13); furniture SVGs (hearth, log,
  fleuron) ≤20KB combined. Total inline SVG ≤ 150KB.
- **Animation frame budget.** The shared loop's per-frame cost
  ≤1.6ms on a mid-tier phone (Moto G class): scrubbed property
  writes only (colour, opacity, transform, custom properties),
  zero layout reads inside the loop (geometry is cached on
  resize/intersection, never measured per frame). Canvas
  embers ≤0.7ms/frame at cap.
- **Particle budget.** Live embers ≤90 page-wide (desktop),
  ≤36 mobile — one pool for hearth, stirs, puffs, the log and
  the chair's single ember, allocated by §6's rules; the pool
  is the law's second clause expressed as a number.
- **Long tasks.** None >50ms after first paint; the title
  split (§6.3) and woodcut arming (§6.4) are chunked across
  frames at build-of-page time. Carve + kindle + stoke running
  simultaneously must still hold the frame budget — rehearsed
  in §10's performance pass.
- **Cut order** (when a build exceeds budget, cut in this
  order, and record the cut): (1) the hero stoke's ember rate
  halves; (2) hover stirs lose their particles (the warm
  remains); (3) the curl becomes the smoke crossfade at all
  widths; (4) woodcut hatch groups compress (1400→900ms) and
  plates per page drop to 3; (5) the chair pin shortens to
  220vh at desktop. **Never cut:** the printed fallbacks, the
  watchdogs, the reading-line guarantee, the focus behaviours,
  or the tallies' source lines — the budget is spent on
  ceremony first because the meaning is not ceremony-shaped.

## 15. Build-order checklist

1. Print the page with no JS and no motion: soot ground,
   parchment text, woodcuts whole, form working, footer lit.
   If this page is not already handsome, stop — the theme is
   built on the print, and no ceremony rescues a plain room.
2. Set the tokens (§2) and type (§3) exactly; run the contrast
   pairs (§10.10) as unit checks.
3. Lay out the room (§4): column, depths, mantel, log corner.
4. Build the shared rAF loop (lerp 0.085) and its watchdog
   *before* any element consumes it.
5. Kindling (§6.2) — the reveal verb; everything else arms
   against it.
6. The hero stoke (§6.1) and title ceremony (§6.3).
7. Woodcuts (§6.4) with the carve queue.
8. The log (§6.6) and the mantel (§6.11) — the room's two
   clocks, agreeing on the reading line.
9. The chair pin (§6.7), then the curl joints (§6.5) at their
   declared boundaries.
10. Hover stir (§6.8) and thunk (§6.9) — the interaction
    vocabulary, once the reading vocabulary stands.
11. Tallies (§6.10) with their source lines and notch audit.
12. Cards (§6.12), the empty chair (§6.13) with its verbatim
    caption, the next-tale block (§6.15).
13. The form (§6.14) with its live tally wired to §6.10's one
    arithmetic; the banking state built, not improvised.
14. Footer banking (§6.16), transitions (§6.17), the cold
    hearth (§6.18).
15. Reduced-motion and `prefers-contrast` passes as *builds*,
    not toggles: walk both end to end.
16. Run §10's gate in full — including the watchdog drill and
    the ember census — and have it signed by someone who did
    not build the page. The teller does not grade their own
    evening.
