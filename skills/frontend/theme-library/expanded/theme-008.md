# Theme 8 — The Index Card Library (Expanded, v1 + v2)

> Expansion of theme #8 from `themes-001-025.md`, written directly to the
> full standard: the 10-part structure of `EXPANSION-STANDARD.md` plus the
> v2 deepening layers (per-element choreography timelines, state matrices,
> breakpoint behaviour, edge cases, accessibility specs and token lists;
> per-theme component inventory, copywriting voice, three worked examples,
> scroll choreography map, whole-page performance budget, build order).
> Identity is preserved exactly: concept, palette anchors, fonts and all 12
> original signature elements are deepened, never redesigned. Where the
> living demos and this document disagree, this document is the build target.

## 1. Concept & world

The site is a card catalogue you can walk through. Knowledge is filed as
physical cards in oak drawers — each card slightly imperfect, thumb-worn,
typed on a machine whose ribbon was never quite new. Scrolling does not
scroll a page; it flips a deck. Sections are drawers. Chapters are cards
pulled forward out of a drawer, read, and tucked visibly behind the stack.
The cabinet is not a metaphor laid over the content: the catalogue **is**
the navigation, the index, and the content, all three at once.

The world has rules, and the rules are the design system:

- **Everything is filed.** Every piece of content lives on a card, in a
  drawer, under a subject tab. There is no content that floats outside the
  filing system — no hero banners, no feature grids, no floating CTAs.
- **Cards are handled, not displayed.** They are pulled forward, lifted by a
  fingertip, snapped into reading position, riffled past. The visitor's
  scroll is a thumb on the drawer.
- **Imperfection is rationed and specific.** Exactly one card per drawer is
  handwritten. Exactly one card per drawer is deliberately misfiled, with
  its note. A second handwritten card, or a second misfile, is not charm —
  it is noise, and it fails the quality gate (§10).
- **The furniture is real.** Brass label holders carry real typed labels.
  Thumb-tabs mark real places. The drawer that opens contains the actual
  section it labels. Furniture that labels nothing is banned (§9).

**Mood.** Quiet, lamplit, faintly dusty; the pleasure of a well-kept index
and of finding something you were not looking for because it was filed next
to what you were. Serendipity is a feature of the world, engineered by the
misfiled card and by adjacent-card peeks in the stack — never by randomness.

**Best-fit sites and audiences.** Research tools and personal knowledge
bases; wikis and documentation with a browsable (not just searchable)
structure; recipe archives; glossaries, field guides, species/record
collections, discographies, bibliographies; museum and archive collection
pages; any product whose content is genuinely a *collection of discrete,
titled, classifiable entries* and whose audience enjoys browsing. The theme
rewards archives of 30–3,000 entries with real subject classification.

**When NOT to use it.** (1) Checkout- or transaction-first products — the
deck-flip reading rhythm fights fast task completion; a store gets the
filing *form* only in its catalogue section, never at checkout (§7).
(2) Real-time or streaming data (dashboards, live feeds) — cards are filed
at rest; a card that updates itself breaks the fiction and the flip timing.
(3) Long-form continuous prose (essays, reports) — the card is a unit of
~90–140 words; prose that needs 2,000 unbroken words belongs in Marginalia
(#2) or The Colophon (#5). (4) Sites whose audience is primarily scanning
for one known fact under time pressure (support triage, status pages) —
serendipity is a cost there, not a delight. (5) Any build that cannot
commit to real classification: if the content has no subjects, drawers are
lies.

## 2. Palette

Four anchor inks/stocks from the original theme, plus derived tokens —
each derived token is labelled and is a shade, tint or mix of an anchor,
never a new hue. The palette is a physical materials list: paper, wood,
ink, and one red.

| Token | Value | Role | Usage ratio | Pairing & contrast |
|---|---|---|---|---|
| `--card-stock` | `#F3EBD7` | Card faces; the page's ground wherever a card is read | ~62% of pixels | Ground for `--ink` (12.6:1) and `--tab-red` (4.7:1) |
| `--drawer-oak` | `#7A5230` | Drawer fronts, cabinet frame, label-holder surrounds | ~24% | Ground for `--card-stock` labels (5.8:1 at ≥13px semibold); never body-text ground |
| `--typed-ink` | `#2E2A26` | All card text; chrome text on stock | ~9% | On `--card-stock` 12.6:1 (AAA body); on `--oak-pale` 9.1:1 |
| `--tab-red` | `#B3402E` | Subject tabs, the ruled line's ink, focus rings, the misfiled note's stamp, error voice | ~3% | On `--card-stock` 4.7:1 — large text, tabs, UI marks and ≥700-weight labels only, never body copy |
| `--card-shade` (derived) | `#E9DCC0` | Card edges, the stack's side faces, tucked-behind cards | ~2% | A 6% darken of stock; edge definition only, carries no text |
| `--oak-deep` (derived) | `#5C3B21` | Cabinet shadow side, drawer interior, footer ground | with oak | Ground for `--card-stock` (8.3:1) and `--brass` (4.9:1) |
| `--oak-pale` (derived) | `#A97C50` | Drawer front highlights, hover wash on oak, disabled chrome | small | Ground for `--typed-ink` (4.6:1, large/labels only) |
| `--brass` (derived) | `#B08D46` | Brass label holders, thumb-tab face, drawer pulls | <1% | On `--oak-deep` 4.9:1 — hardware only, never text |
| `--ink-soft` (derived) | `#5A5348` | Secondary card text: filing data, dates, cross-references | small | On `--card-stock` 7.4:1 (AA body) |
| `--rule-red` (derived) | `#C96A55` | The ruled line near the top of every card | hairlines | `--tab-red` mixed 45% toward stock; a printed rule, carries no text |

**Pairing laws.** Ink on stock is the only body-text pairing. Red is rationed
to ~3%: if a screenshot shows red competing with the headline, the build is
wrong. Oak never sits directly against oak-deep without a brass or stock
edge between them (wood on wood reads as mud at small sizes). Brass is
hardware — it frames labels, it is never a fill behind text.

**Dark-mode behaviour.** The theme does not invert. A card catalogue lives
in a reading room; after hours the room is lamplit, not black. Under
`prefers-color-scheme: dark` (or a host-forced dark mode) the *lamplight
variant* applies: `--card-stock` → `#E8DCC2` (stock under tungsten light),
`--drawer-oak` → `#664326`, `--oak-deep` → `#422A15`, `--typed-ink`
unchanged (ink is ink), `--tab-red` → `#C0503C` (a 6% lift so the tab keeps
4.6:1 on lamplit stock), and every card gains a warm radial wash
(`--lamp-wash: radial-gradient(120% 90% at 50% 0%, rgba(255,196,110,0.10), transparent 60%)`)
at its top edge. Motion is unchanged; the shimmer (§6.10) warms to the same
amber. A true black-background variant is refused by design — products that
require one are directed away in §1.

## 3. Typography

Two families from the original theme, plus one rationed hand. Nothing else
may be loaded.

| Role | Font | Size / line-height | Tracking / case | Rules |
|---|---|---|---|---|
| Card title (display) | Special Elite | 40px / 1.15 (hero card), 30px / 1.2 (chapter cards) | 0; sentence case as typed | The title is typed, not set: no uppercase transforms, no tightening. A title longer than 2 lines is re-filed (shortened), never shrunk below 26px |
| Card heading | Special Elite | 22px / 1.3 | 0 | One per card section; followed by the ruled line, never preceded by it |
| Card body | Special Elite | 17px / 1.65 | 0 | The reading voice. Measure 52–62ch. Paragraphs separated by a blank typed line (0.8em), never by indent |
| Card small / filing data | Special Elite | 14.5px / 1.5 | 0 | Dates, card numbers, cross-references ("see also: …"), filed-under lines |
| Handwritten card | Caveat | 21px / 1.35 | natural hand | ONLY the one handwritten card per drawer and the misfiled note. Never UI, never a heading elsewhere |
| Drawer label | Libre Franklin 700 | 13px / 1.2 | +0.14em, uppercase | Set into the brass holder; the label is the drawer's real subject range ("HISTORY — A–M") |
| Chrome / nav | Libre Franklin 600 | 14px / 1.4 | +0.02em | Cabinet chrome only: nav, buttons, form labels. Franklin never appears on a card face |
| Buttons | Libre Franklin 700 | 13.5px | +0.08em, uppercase | Chrome voice; see §11 |
| Counters / stats | Special Elite | 30px / 1.1 | tabular figures inherent to the face | Counted in §6.9; figures are the catalogue's own counts |
| Caption (pasted photos) | Special Elite | 13.5px / 1.45 | 0 | Typed under the photo, inside the card's border; never overlaid on the image |

**Type laws.** (1) The card/chrome split is absolute: Special Elite (and
Caveat) live on card stock; Libre Franklin lives on wood and brass. A
Franklin word on a card face, or a typewriter word on a drawer front, is a
defect (§9). (2) Special Elite has one weight — emphasis on cards is by
underline (typed underscore rule, §11) or by the red, never by faux-bold;
synthetic bold on Special Elite is banned (it smears the typewriter
texture). (3) Typewriter text is left-aligned, always — centred type is a
poster, not a card. (4) Line-height never drops below 1.5 for card body at
any breakpoint; density comes from the deck, not from crowding the card.

## 4. Layout language

**The cabinet.** The page is a cabinet seen from the front, slightly above:
a fixed back layer of oak drawer fronts (the cabinet) behind a single
reading column (the deck). The cabinet is `position: fixed`, full-viewport,
`z-index: 0`; the deck scrolls above it at `z-index: 1`. Drawer fronts on
the cabinet carry the site's real section labels in brass holders — the
cabinet is the page's table of contents rendered as furniture, and its
visible drawers are the sections above and below the one being read.

**Grid and measures.** Reading column: max-width 760px, centred, with a
28px thumb-tab rail reserved on its right edge (the rail is layout space,
not an overlay). The card ratio is the catalogue standard 5:3 (125 × 75mm):
a full reading card is 760 × 456px at desktop; grid cards (§6.14) are
360 × 216px. Drawer chapters are full-viewport scenes: the open drawer
occupies the column, its mouth at the column's top edge. Spacing rhythm is
the **card unit**: 8px base, card padding 28px top (below the ruled line's
18px offset) / 32px sides / 30px bottom; gaps between stacked cards 14px
(the thickness of a small stack, so the deck reads as stacked stock, not as
floating panels).

**Section choreography.** The page alternates: *drawer scenes* (pinned,
one drawer open, cards flipped through — §6.2, §6.3) and *shelf scenes*
(unpinned, card grids dealt in — §6.14). No two pinned scenes are adjacent;
a shelf scene always separates drawers so the visitor's thumb rests. The
hero is a drawer scene (§6.1); the footer is the cabinet's base drawer,
shut (§6.17).

**Density rules.** One reading card in focus at a time inside a drawer
scene; the stack behind it shows at most 3 card edges (more reads as a
graphic, not a deck). Shelf scenes deal at most 6 cards per row-group.
Whitespace in this theme is *drawer space*: the oak and shade around cards
is the material, and it is never filled with decoration — an empty stretch
of cabinet is a shut drawer, which is a true statement about the archive.

**The two imperfections, placed.** Per drawer: the handwritten card is
filed at a fixed position — the 3rd card of the drawer, or the drawer's
last card if the drawer holds fewer than 4. The misfiled card is filed
exactly one position out of its correct order, carries its note (§12), and
is *findable*: it appears in search results under its correct subject with
the note attached (§6.15). Placement is content data (`data-handwritten`,
`data-misfiled` attributes in the source), never chosen by script at
runtime — serendipity that changes between visits is a bug, not a feature.

## 5. Full motion system

The governing law: **motion is handling.** Nothing in this theme moves
unless a hand could move it — cards are pulled, flipped, riffled, lifted,
snapped; drawers slide on runners; labels are typed. There is no motion
that exists to decorate empty space. Easings are named from the drawer:

- `drawer` = `cubic-bezier(0.25, 0.8, 0.25, 1)` — a drawer on wooden
  runners: quick release, long glide, soft arrival.
- `flick` = `cubic-bezier(0.34, 1.2, 0.4, 1)` — a card flipped by a thumb:
  fast travel, a 2% overshoot as the card slaps the stack, settle.
- `snap` = `cubic-bezier(0.7, 0, 0.2, 1)` — the paper snap of selection:
  near-instant attack, no overshoot.
- `settle` = `cubic-bezier(0.22, 0.61, 0.21, 1)` — paper settling onto a
  stack under its own weight.
- `riffle` = `linear` — scrubbed motion is the visitor's own thumb; easing
  scrubbed motion lies about the hand's position.

| Motion term | The Index Card Library's version | Duration / easing | Trigger |
|---|---|---|---|
| Scroll-triggered reveals | Cards deal forward from the drawer mouth (§6.14) or flip into reading position (§6.2); shelf cards deal in one by one, 60ms stagger | 420ms `flick` (flip); 380ms `settle` (deal) | Card crosses 20% into viewport (IO threshold 0.2, rootMargin bottom −6%) |
| Parallax layers | The cabinet back layer is fixed; drawer fronts and brass holders inside the hero scene drift at 0.92× scroll speed (max 18px travel), cards at 1.0× — the cabinet is behind the deck, and the depth cue is the gap | scrubbed, rAF-lerped 0.14 | Scroll |
| Pinned scenes | Drawer chapters pin for ~150vh while their cards are riffled and flipped (§6.3, §6.2); the hero drawer pins for its opening beat only (100vh) | pin via `position: sticky`; inner scrub rAF-lerped 0.14 | Scroll position |
| Masked line reveals | Card faces reveal through the drawer mouth: `clip-path: inset(0 0 100% 0)` → `inset(0)` from the drawer's front edge — the card comes *out of* the drawer | 460ms `drawer` | Card arrival in a drawer scene |
| Blur-to-sharp reveals | Focus-settle: a card pulled forward starts at `blur(1.2px)` + 97% scale-equivalent softness and sharpens as it lands — the eye focusing on the card the hand just pulled. The only blur in the theme; capped at 1.2px so text is never unreadable mid-flight | within the 420ms flip, blur clears by 70% of travel | Flip / deal |
| Animated counters | Catalogue counters (§6.9): typewriter figures count in visible typed steps | 900ms, stepped (12 steps), `settle` | Scroll entry of the stats card |
| Progress indicators | Thumb-tab travelling the drawer edge + the brass label's typed "cards seen: n" line (§6.4) | tab scrubbed rAF-lerped 0.14; label updates discretely per flip | Scroll + flip events |
| Marquees | Not used. A catalogue has no ticker; the theme's horizontal-motion budget is spent on the riffle (§6.3) and the shimmer (§6.10). Stated plainly so no builder adds one | — | — |
| Ambient loops | Exactly one: the riffling edge shimmer (§6.10), every ~9s, plus the hero drawer's breathing *stillness* — nothing else loops | 1.2s sweep per pass | Time (paused off-screen, §6.10) |
| Micro-interactions | Paper-snap click (§6.8, 180ms), tab press (tab flexes 1px, 120ms), label-holder glint on nav hover (200ms) | as stated | Click / hover |
| Hover physics | Fingertip lift (§6.7): near edge rotateX 3°, shadow lengthens 200ms; quadrant tilt to 4°, rAF-lerped 0.18 | 200ms `settle` | Pointer hover (fine pointers only) |
| Page transitions | Drawer-shut (§6.11): current drawer shuts (400ms), destination drawer opens and fans | 400ms out + 800ms in `drawer` | Route change |
| Image treatments | Pasted photos scale-in-frame inside the card's printed border: frame fixed, photo settles 104%→100% | 520ms `settle` | Scroll entry |

**Global motion safety.** The static render is the final state: every card
is fully visible, in reading position, in the server/static HTML. JavaScript
adds pre-states (`data-filed="away"`) only to cards below the fold, only
after the flip machinery has initialised, and a **global deal-out timer**
(1,200ms after first paint, and 1,200ms after any route change) forces every
card to its final state regardless of observer, scroll or rAF state. An
unflipped card in the stack is rendered legible (rotated ≤4°, full ink) —
flipping is emphasis, never access. All scrubbed values (riffle, tab,
parallax) run through **one shared rAF loop** with lerp factor 0.14; there
is exactly one scroll listener for the whole theme. `prefers-reduced-motion`
collapses the system to the stacked list (§6 passim): no pinning, no flips,
no scrub — every card in a simple readable stack, in order.

## 6. Signature elements

Each element carries the full v1 build spec — what & why, structure, motion
spec, states, content-merge, failure fallback, reduced-motion variant,
performance budget and mobile variant — plus the v2 deepening layers:
a millisecond choreography timeline, a full state matrix, breakpoint
behaviour, edge cases, an accessibility spec, and the exact tokens it
consumes. Token names are defined in §2 and §3; motion tokens
(`--ease-drawer`, `--ease-flick`, `--ease-snap`, `--ease-settle`) are the
named easings of §5.

### 6.1 Opening hero drawer

- **What & why.** On load, the hero drawer slides open toward the visitor
  and its cards fan upward; the handwritten misfiled card pops last. It
  belongs because the catalogue's front door is a drawer: the first thing
  the site does is open the drawer that contains the visitor's business
  here, and the fan shows the drawer's real contents, not a hero graphic.
- **Structure.** `<section class="drawer-scene" data-drawer="hero">`
  containing `<div class="drawer-box">` (oak front with brass holder +
  typed label, §6.13's holder component) and `<div class="deck">` of 4–6
  `<article class="card">` children. Perspective lives on the scene
  (`perspective: 1200px`); the box translates on Z toward the visitor, the
  cards fan inside it. The H1 is the first card's title — the drawer
  contains the page's actual headline, intro and primary action (as a
  chrome button pinned to the drawer front, §11, because buttons are
  chrome, not card content).
- **Motion spec.** Load-triggered (starts on `DOMContentLoaded` + 80ms;
  never waits for images). Drawer box: translateZ −120px→0 + translateY
  24px→0, 800ms `drawer`. Cards fan: each rotateX −4°→0 and translateY
  18px→0, 380ms `settle`, staggered 40ms in filing order; the handwritten
  card goes last regardless of its filed position in the fan order, lifts
  4px higher (§6.6), 520ms `settle`. Total sequence ≈ 800 + 5×40 + 520 ≈
  1,520ms; the scene is interactive from 0ms (no input lock).
- **States.** *Pre-JS / static:* drawer open, cards fanned, all readable.
  *Opening:* as timeline. *Settled:* drawer open, first card in reading
  position; the scene unpins after its 100vh and becomes the first drawer
  chapter. *Revisit (SPA back):* no replay — a drawer you left open is
  open; session flag `heroOpened`.
- **Content-merge.** The fan *is* the hero: headline card, intro card,
  and the drawer's first content cards. Remove the animation and the hero
  is byte-identical.
- **Failure fallback.** Pre-states are JS-applied only, after init; any
  failure leaves the open, fanned, readable hero. The 1,200ms deal-out
  timer (§5) forces final state if the stagger chain breaks.
- **Reduced-motion variant.** No slide, no fan. The drawer is open and the
  first card is in reading position from first paint.
- **Performance budget.** Transform/opacity only; ≤7 nodes animating;
  perspective on one scene. No assets. Must not delay LCP: the H1 card is
  in first paint at full ink (the fan animates position, never opacity
  below 1). **Mobile variant:** fan stagger tightens to 28ms, drawer
  travel halves (translateZ −60px), card count in the fan caps at 4 —
  extra cards start already fanned.
- **Choreography timeline (ms, from `DOMContentLoaded`).** 0–80: static
  open drawer (first paint). 80: box starts. 80–880: box glide (`drawer`).
  300: first card starts fanning (box is 40% open — cards never fan from
  a shut drawer). 300/340/380/420: cards 2–4 fan (`settle`, 380ms each).
  460: handwritten card pops (520ms, +4px). 880: box lands; a 60ms, 1px
  overshoot settle is built into the `drawer` curve's tail — no separate
  thunk animation. 980: handwritten card settles. 1,520: sequence
  complete; scene hands scroll control to §6.3 if the hero drawer is a
  browse drawer, else rests open.
- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest (settled) | Drawer open, card 1 in reading position, tab at top | Same |
  | Hover | No hero-level hover; cards inside use §6.7 | n/a |
  | Focus | Focus enters card 1's first link directly; no focus is spent on the drawer box (it is `aria-hidden` furniture) | Same |
  | Active | n/a (not an activatable element) | n/a |
  | Scrolled-past | Drawer remains open behind the deck; its front parallaxes at 0.92× (§5) | Same, parallax halved |
  | Disabled | If JS is off or init fails: the static open state *is* the element | Same |

- **Breakpoint behaviour.** ≥1200px: as spec'd; cabinet drawers flank the
  column on both sides. 768–1199px: fan angle reduces (rotateX −3°),
  perspective 1000px, flanking drawers crop to one side. <768px: the
  drawer fills the column width; fan becomes a vertical deal (translateY
  only, no rotateX — small screens tip cards into illegibility); stagger
  28ms; the brass label truncates with ellipsis rather than wrapping.
- **Edge cases.** *Slow network:* the sequence is asset-free and starts on
  DOMContentLoaded; webfont swap mid-fan is acceptable (FOUT on cards is
  in-fiction — a card re-typed), but layout must not shift: card boxes are
  sized by the card ratio, not by text. *Very few cards (1–2):* the fan
  still runs, stagger collapses to the cards present; a 1-card drawer
  skips the fan and only the box glides. *Back-navigation mid-animation:*
  session flag prevents replay; state restores settled. *User scrolls
  during the opening:* the sequence is not scroll-locked; scrolling moves
  the scene away and the fan finishes off-screen harmlessly (transforms
  only, no scroll hijack, ever).
- **Accessibility spec.** The scene is a `<section>` with
  `aria-labelledby` pointing at the H1 card's title. The drawer box and
  cabinet are `aria-hidden="true"` (furniture; the same sections are
  announced by the nav, §6.13). Focus order is DOM order: H1 card links →
  drawer-front primary action → next section. No focusable element is ever
  inside a card that is mid-fan in a way that changes its position under
  the focus ring — the ring is drawn on the card's final box, and focus
  only becomes available on cards at rest (fan is 1.5s and non-blocking;
  keyboard users tabbing during it land on settled geometry because
  pre-states are removed from the tab order via `visibility` management
  only for the fan's 380ms per card — simpler and safer: cards are never
  removed from tab order, and the fan's transforms do not apply to a card
  while it or a descendant holds focus).
- **Tokens consumed.** `--card-stock`, `--card-shade`, `--drawer-oak`,
  `--oak-deep`, `--brass`, `--typed-ink`, `--ease-drawer`, `--ease-settle`,
  `--drawer-perspective: 1200px`, `--fan-stagger: 40ms`.

### 6.2 Deck-flip section changes

- **What & why.** The theme's core reading mechanic: at a chapter
  boundary, the current card flicks forward and tucks visibly behind the
  stack as the next card pulls into reading position. One flip per
  chapter. It belongs because flipping is how a deck is read — there is
  no page beneath the cards, so the transition between sections must be a
  card gesture, not a scroll fade.
- **Structure.** Inside a drawer scene, `<div class="deck">` holds the
  chapter's cards as siblings. The reading card is `data-state="reading"`;
  flipped cards get `data-state="filed"` and stack behind with 3px/6px
  offsets and `--card-shade` edges, max 3 visible edges (§4). Flip is
  `rotateX` on the card with `transform-origin: 50% 100%` (the card tips
  toward the visitor over its bottom edge, like a card flicked forward by
  its top). Chapter boundaries are `<h2>`-headed cards; the flip triggers
  when the next chapter card's heading crosses 55% viewport height.
- **Motion spec.** Outgoing card: rotateX 0→−14° + translateY 10px→26px
  as it tucks, 420ms `flick`. Incoming card: from the stack (rotateX −4°,
  blur 1.2px focus-settle, §5) to reading position, 420ms `flick`,
  starting 90ms after the outgoing card (they overlap like a real flip —
  sequential flips read as a slideshow and fail review). Scroll is never
  locked or hijacked: the flip is a response to scroll position, driven
  by the shared rAF loop reading chapter offsets, not by wheel events.
- **States.** *Reading:* full ink, flat, focusable. *Flipping out:*
  mid-rotate, still legible (never below 92% scale-equivalent). *Filed:*
  tucked, edge visible, content present in DOM and in the accessibility
  tree (a filed card is read already, not hidden). *Un-flipping (scroll
  back up):* the reverse flip runs at the same 420ms — the deck is
  reversible at every boundary, no one-way doors.
- **Content-merge.** Sections are the cards. The flip carries the actual
  chapter content; there is no separate transition layer.
- **Failure fallback.** Default state: all cards stacked in reading
  order, each fully visible in normal flow (the deck is a styled list
  until JS enhances it). If the rAF loop dies, cards remain wherever they
  are — every position is a legible one by design.
- **Reduced-motion variant.** No flips, no pinning: the drawer scene
  becomes a vertical stack of cards in order, separated by 14px stack
  gaps. Chapter boundaries are ordinary scroll.
- **Performance budget.** ≤2 cards animating at once, transform + filter
  (blur ≤1.2px on one card) only; `will-change: transform` applied to the
  two flipping cards at flip start and removed at end — never standing.
  **Mobile variant:** flip angle reduces to −10°, blur is dropped
  (focus-settle is desktop-only; small GPUs pay too much for it), overlap
  tightens to 60ms.
- **Choreography timeline (ms, from boundary trigger).** 0: next chapter
  heading crosses 55% line; flip arms. 0–420: outgoing card rotates to
  −14° and tucks (its top edge clears the reading frame by ~55% at 200ms,
  the moment of maximum overlap). 90–510: incoming card pulls forward,
  blur 1.2px→0 by 385ms (70% of its travel). 420: outgoing card files
  (state change, edge offset applies with a 120ms `settle` micro-move).
  510: incoming card lands; §6.5's ruled line draws (350ms) starting at
  480 (overlapping the landing's last 30ms — the card is ruled as it is
  laid down). 830: flip fully complete; §6.4's counter increments at the
  landing beat (510).
- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest (reading) | Flat, full ink, in tab order | Same |
  | Hover | Reading card uses §6.7 fingertip lift | n/a — no hover on touch |
  | Focus | Focus ring on the reading card's focused element; flipping never starts while focus is inside the outgoing card — the flip waits for the boundary + focus-exit, or runs and focus is moved to the incoming card's heading (programmatic, announced, §A11y) | Same |
  | Active | Click on the reading card = §6.8 snap (already forward: a 60ms confirmatory settle only) | Tap = same |
  | Scrolled-past | Card is filed, edge visible, content in AT | Same |
  | Disabled | Reduced-motion / no-JS: static stack, no states | Same |

- **Breakpoint behaviour.** ≥1200px: as spec'd. 768–1199px: stack offsets
  halve (2px/4px), flip angle −12°. <768px: flip becomes a deal-forward
  (translateY 16px + fade of *position only*, no rotateX — tipped cards
  at phone width clip their own text against the column edge), duration
  340ms `settle`; the pinned scene shortens (§6.3).
- **Edge cases.** *Fast scrolling:* if two boundaries cross within one
  flip, flips queue-collapse — intermediate cards file instantly and only
  the final flip animates (a fast scroller is riffling, §6.3's fiction
  covers it). *Scrolling back up mid-flip:* the flip reverses from its
  current angle (the rAF loop is state-driven, not tween-driven, so
  reversal is free of pops). *A chapter longer than the scene:* the card
  unpins and scrolls internally as a normal long card (§6.3 edge case) —
  flipping never truncates content. *Print:* all cards print in order,
  unrotated (print stylesheet flattens the deck).
- **Accessibility spec.** Chapter cards are `<section>`s with headings;
  the flip is presentational. `aria-live` is NOT used for flips (too
  chatty); instead each chapter heading is reachable by heading
  navigation and by the drawer index (§6.13). Focus management: if focus
  sits inside a card that is about to file, the flip is deferred until
  focus leaves, up to the point where the card would leave the viewport,
  at which point focus moves to the incoming card's heading and a
  visually-hidden status line ("Card 7 of 12: [title]") updates
  (`aria-live="polite"`, throttled to flip landings). Contrast: filed
  cards' visible edges carry no text. Touch targets on cards: the whole
  reading card is the §6.8 target (≥44px in every dimension by
  construction).
- **Tokens consumed.** `--card-stock`, `--card-shade`, `--typed-ink`,
  `--ease-flick`, `--ease-settle`, `--flip-angle: -14deg`,
  `--stack-offset: 3px`, `--focus-blur: 1.2px`.

### 6.3 Riffle-browse scrub

- **What & why.** Inside a pinned drawer chapter (~150vh of scroll), the
  visitor browses before reading: card edges flick past in direct
  proportion to scroll, like a thumb riffling a drawer to see what's
  filed. It belongs because browsing-by-riffle is the catalogue's native
  search — you fan the drawer to sense its contents before you commit to
  a card.
- **Structure.** A pinned `<section class="riffle-scene">` (sticky inner,
  150vh track) containing `<div class="riffle-deck">`: a stack of card-top
  edges — the top 46px of each card in the drawer (its tab, title line and
  ruled line, real DOM, real text) — offset in a fan. Scroll progress
  through the track maps to an index across the edges; the current edge is
  raised 8px and fully inked, neighbours sit at graded shade. At the end
  of the track, the deck resolves into the drawer's first reading card
  and §6.2 takes over. The edges are the actual cards' headers (the same
  nodes, re-parented by layout, not duplicated content — the card bodies
  live in the deck below and are revealed as cards are chosen; for the
  no-JS state see fallback).
- **Motion spec.** Fully scrubbed, `linear`, via the shared rAF loop
  (lerp 0.14). One card edge per 26px of scroll travel within the track.
  Edge raise: translateY −8px over the 26px interval, `--card-shade` →
  `--card-stock` background crossfade on the same interval. No easing, no
  autoplay: if the visitor stops scrolling, the riffle stops mid-edge,
  stable.
- **States.** *Rest (track start):* edge 1 raised. *Browsing:* edges pass
  at thumb speed — the visitor's speed, not a fixed rate. *Resolved:*
  final edge lands, deck opens into §6.2's first flip. *Reversed:*
  scrolling up riffles backward through the same edges, symmetric.
- **Content-merge.** The edges are the drawer's real card titles — the
  riffle shows the actual index of the actual drawer. A drawer with
  generic edges ("Card 1, Card 2…") is a §9 failure.
- **Failure fallback.** No JS / no sticky support: the scene renders as
  the drawer's cards in a normal stack (the riffle is an enhancement of
  the stack, applied by JS adding the track height and sticky classes).
- **Reduced-motion variant.** No pin, no scrub: the drawer opens as a
  titled index list (each card's title line as a list item linking to its
  card below), followed by the cards in order.
- **Performance budget.** Only transforms/background on ≤14 visible edge
  nodes; edges beyond 14 are virtualised (the drawer shows a "+ n more
  filed" edge, which is honest furniture). One rAF loop, shared. **Mobile
  variant:** track shortens to 110vh, one edge per 20px, max 10 edges.
- **Choreography timeline.** Scrubbed, so the timeline is positional:
  0–8% of track: edge 1 raised, drawer label (§6.4) types "browsing…".
  8–88%: edges pass at 26px each; the thumb-tab (§6.4) travels the rail
  in sync (same progress value, no separate animation). 88–96%: the last
  edge raises and holds (a 20px dead zone so the landing is felt, not
  rushed). 96–100%: edges settle into the stack (120ms `settle` offsets)
  and the first reading card pulls forward per §6.2's incoming beat.
- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Edge 1 raised; scene is keyboard-focusable as a region with instructions (§A11y) | Same; touch scroll drives it identically |
  | Hover | Hovering an edge raises it +2px extra and shows its full title if truncated | n/a |
  | Focus | Edges are NOT individually focusable (14 tab stops to browse is a trap); one stop for the scene, arrow keys move the raised edge, Enter files to that card | Same with on-screen keys / swipe within a focused scene is NOT hijacked — page scroll only |
  | Active | Clicking an edge jumps the deck to that card (scroll position maps to the card's chapter; native scroll, animated by the browser's own smooth scroll only if the user has not requested reduced motion) | Tap = same |
  | Scrolled-past | Deck resolved into §6.2; the riffle scene is behind | Same |
  | Disabled | Reduced-motion: index list (above) | Same |

- **Breakpoint behaviour.** ≥1200px: 150vh track, 14 edges. 768–1199px:
  130vh, 12 edges, edge height 42px. <768px: 110vh, 10 edges, edge
  height 38px, titles truncate at 24ch with the full title available on
  the card itself.
- **Edge cases.** *Drawer with 1–3 cards:* no riffle (nothing to browse);
  the scene is skipped and §6.2 opens the drawer directly — building a
  riffle for 2 cards is theatre without content. *Drawer with 60+ cards:*
  virtualised edges + the "+ n filed" edge; the scrub maps across all 60
  (edges represent ranges, labelled by their first card's title + count —
  honest furniture, stated in the label). *Scroll-up re-entry:* the
  riffle re-forms from the resolved deck symmetrically. *Low-power
  device:* if the shared rAF loop detects sustained <40fps for 2s, the
  riffle degrades to stepped updates (edges change at 3 discrete
  positions per card instead of continuously) — the index stays truthful,
  the smoothness is what is spent.
- **Accessibility spec.** The scene is `role="region"`,
  `aria-label="Browse the [subject] drawer"`, with visually-hidden
  instructions ("Use arrow keys to browse cards; Enter to open the raised
  card"). The raised edge's title is mirrored into an `aria-live="polite"`
  status, throttled to one announcement per 300ms. All cards remain
  reachable without the riffle: the index-list fallback is also present
  in the DOM as the drawer's `<nav>` for AT that prefers lists
  (`aria-hidden` on the visual riffle for screen-reader users is wrong —
  instead the riffle edges are `aria-hidden` and the list is the AT
  interface to the same cards; both open the same card nodes). Contrast:
  raised edge title in `--typed-ink` on `--card-stock` (12.6:1); unraised
  edges use `--ink-soft` (7.4:1) — never below AA, because an unreadable
  index is a broken index.
- **Tokens consumed.** `--card-stock`, `--card-shade`, `--typed-ink`,
  `--ink-soft`, `--tab-red` (raised-edge tab), `--rule-red`,
  `--riffle-track: 150vh`, `--edge-step: 26px`, `--ease-settle`.

### 6.4 Thumb-tab progress + cards-seen label

- **What & why.** Progress in this theme is a place in a drawer, so the
  progress indicator is drawer furniture: a thumb-tab that travels down
  the drawer edge, scrubbed to page progress, while the brass label
  holder's typed line updates — "cards seen: n" — as each card is flipped
  past. It belongs because a catalogue user asks "how far through this
  drawer am I, and how many cards have I seen?" — furniture questions,
  answered by furniture.
- **Structure.** `<div class="tab-rail">` fixed in the column's reserved
  28px right rail (§4), containing `<div class="thumb-tab">` (tab-red
  face, the current drawer's initial letter typed on it) and, at the
  rail's top, the `<div class="brass-label">` holder with two typed
  lines: the drawer range ("HISTORY — A–M") and the counter line
  ("CARDS SEEN: 07 / 42"). The counter is a real count of flipped cards,
  incremented on §6.2 landings and §6.3 resolution, stored in a JS counter
  whose value is derived from the deck's state, never from scroll
  percentage — the label must never claim a card was seen that wasn't.
- **Motion spec.** Tab travel: scrubbed via the shared rAF loop, lerp
  0.14, mapped to *drawer-local* progress inside drawer scenes and to
  page progress in shelf scenes (the tab belongs to the current drawer;
  between drawers it rides to the next drawer's top during §6.11).
  Counter updates are discrete: the changed digit re-types (opacity
  steps 0.2→1 in 3 steps of 40ms — a typewriter strike, not a fade).
  Drawer change: the range line clears and re-types at 24ms per
  character.
- **States.** *Rest:* tab at current position, counter current. *In a
  riffle (§6.3):* the counter line reads "BROWSING — [drawer]" instead of
  a count (you have seen edges, not cards; the label does not lie).
  *Drawer complete:* the counter line adds a red typed tick "✓ FILED"
  after the count for 1.6s, then rests. *Page end:* tab at rail bottom,
  counter at total.
- **Content-merge.** The tab and label are the drawer's own furniture and
  their content is the drawer's real range and the real seen-count.
- **Failure fallback.** No JS: the rail renders the drawer range and the
  total count only ("42 CARDS IN THIS DRAWER"), static — still true,
  still useful. The travelling tab is not rendered (a static tab at top
  would lie about position).
- **Reduced-motion variant.** The tab still travels (it is information)
  but jumps drawer-to-drawer discretely at chapter boundaries instead of
  scrubbing; digit re-typing becomes an instant swap.
- **Performance budget.** One transform on the tab + text updates on flip
  events only; zero per-frame DOM writes except the tab transform in the
  shared loop. **Mobile variant:** the rail narrows to 20px, the brass
  label moves to a slim bar atop the column (holder becomes a strip), the
  counter line shortens to "07 / 42".
- **Choreography timeline.** Continuous (tab) + event beats: on a §6.2
  landing (t=0): counter increments at t=0; digit strike runs t=0–120ms
  (3 × 40ms steps); if the landing completes a drawer, the "✓ FILED" tick
  types at t=200–680ms (24ms × 6 chars incl. space), holds to t=2,280ms,
  then the line re-types to the next drawer's range during §6.11.
- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Tab at true position; label current | Same |
  | Hover | Rail hover (fine pointer): the label holder glints (brass gradient sweep, 200ms) and the tab shows a tooltip-free enlargement of the counter (scale 1.15 on the tab only) | n/a |
  | Focus | The rail is not focusable (it is a progress readout); its information is exposed via `role="progressbar"` (§A11y) | Same |
  | Active | Clicking the rail jumps to the drawer's first unseen card (native scroll to that chapter) — the one interaction furniture earns | Tap = same; rail tap target is the full 28px rail width, ≥44px tall segments per drawer |
  | Scrolled-past | Tab reflects the drawer now current, never the one left | Same |
  | Disabled | No-JS static label (above) | Same |

- **Breakpoint behaviour.** ≥1200px: 28px rail, full two-line label.
  768–1199px: 24px rail, label holder narrows, range line truncates to
  the subject word only. <768px: rail 20px; label becomes the top strip
  variant; the tab's letter is hidden (a plain red tab) under 360px.
- **Edge cases.** *Single-drawer page:* the tab maps to the whole page;
  the range line shows the page's only range. *Cards added by client-side
  loading:* totals re-derive from the DOM on mutation (the counter counts
  cards, not a hard-coded number). *Scroll-up:* "cards seen" never
  decreases — seen is a fact, not a position; the tab, being positional,
  does travel back up. The distinction is stated in the label's wording:
  the counter says SEEN, the tab shows WHERE.
- **Accessibility spec.** The rail container carries
  `role="progressbar"`, `aria-label="Reading progress"`,
  `aria-valuemin="0"`, `aria-valuemax` = total cards,
  `aria-valuenow` = cards seen, `aria-valuetext="7 of 42 cards seen,
  drawer: History A–M"`. Updates are not live-announced per card (the
  §6.2 status line covers chapter changes). The tab's red on oak meets
  3:1 non-text contrast against `--oak-deep` (4.1:1 measured pairing for
  the tab face against the rail's oak) — and position is never the only
  signal: the counter line states the same progress as text.
- **Tokens consumed.** `--tab-red`, `--brass`, `--drawer-oak`,
  `--oak-deep`, `--card-stock`, `--typed-ink`, `--rail-width: 28px`,
  `--ease-settle`.

### 6.5 Self-drawing ruled red line

- **What & why.** Every catalogue card carries a ruled red line near its
  top; when a card comes forward, its line draws itself left to right —
  the card being ruled at the moment it is laid down. It belongs because
  the rule is printed on the stock itself: drawing it is the smallest,
  most frequent motion in the theme, and it is the deck's heartbeat — if
  the lines stop drawing, the catalogue feels dead.
- **Structure.** An inline SVG per card: `<svg class="rule" viewBox="0 0 100 2" preserveAspectRatio="none"><path d="M0 1 H100"/></svg>`
  positioned 18px below the card's top edge, full content width, stroke
  `--rule-red`, stroke-width 2 (in viewBox units, rendering ≈1.5px). Draw
  via `stroke-dasharray/dashoffset`. The line sits above the title —
  content order on the card is: tab + filing line, rule, title, body.
- **Motion spec.** Trigger: the card's arrival (flip landing §6.2, deal
  §6.14, drawer fan §6.1). Duration 350ms `settle`, delay = arrival
  landing minus 30ms (the draw overlaps the landing's tail, §6.2
  timeline). One draw per arrival; a card re-arriving after being filed
  and re-flipped does NOT redraw (a printed line does not re-print) —
  redraw happens only on first arrival per session.
- **States.** *Undrawn (pre-arrival, JS only):* dashoffset full — but the
  line's absence is invisible as a defect because the card is not yet the
  reading card. *Drawing:* left→right. *Drawn:* static for the session.
  *Filed cards:* their lines stay drawn (edges in the stack show drawn
  rules — correct, they were read).
- **Content-merge.** The line is part of the card's printed furniture and
  it separates the card's filing data from its title — a real typographic
  function, drawn.
- **Failure fallback.** Default CSS: line fully drawn. JS sets the
  undrawn state only on cards below the fold at setup. No-JS = all lines
  printed, which is simply correct.
- **Reduced-motion variant.** Lines are printed (fully drawn) at all
  times; the draw never runs.
- **Performance budget.** One SVG path per card, dash animation is
  compositor-friendly; ≤3 concurrent draws (the §6.2/§6.14 arrival caps
  make this natural). **Mobile variant:** identical; stroke renders 1px.
- **Choreography timeline (ms, from card landing t=0).** −30: draw starts
  (tail of the landing). 0: card lands. 0–320: dashoffset runs to 0
  (`settle` — fast start, the last 15% of the line slows like a ruler
  being lifted). 320: line complete; nothing else fires — the draw is a
  beat, not a trigger.
- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest (drawn) | Static printed line | Same |
  | Hover / Focus / Active | No response — the line is print, not a control | Same |
  | Scrolled-past | Remains drawn on the filed card | Same |
  | Disabled | Printed statically | Same |

- **Breakpoint behaviour.** Identical at all sizes; at <768px the line's
  top offset tightens to 14px with the card's padding (§4 rhythm holds:
  the rule's offset is part of the card unit, scaled once, everywhere).
- **Edge cases.** *Card arriving via search jump (§6.15):* the line draws
  on arrival like any other — the beat is the arrival, not the route.
  *Cards in grids (§6.14):* lines draw on deal, staggered with the deal
  (60ms), so a grid's rules ripple left-to-right, top-to-bottom — the
  ripple is a consequence of deal order, not a separate effect. *Print:*
  lines print as drawn.
- **Accessibility spec.** Purely decorative: `aria-hidden="true"`,
  `focusable="false"`. It carries no information that is not also in the
  filing line's text. Contrast: `--rule-red` on stock is a graphic accent
  (2.9:1) — acceptable only because it is non-essential decoration; this
  is stated so no builder "fixes" it by darkening the rule into a second
  tab-red competing with the tabs (§2's red ration).
- **Tokens consumed.** `--rule-red`, `--card-stock`, `--ease-settle`,
  `--rule-offset: 18px`, `--rule-draw: 350ms`.

### 6.6 Handwritten card pop

- **What & why.** One card in every drawer is handwritten (Caveat on card
  stock) — a human filed this one, in pen, probably years ago. When its
  drawer opens, it lifts 4px higher than the typed cards and settles with
  a softer ease. It belongs because the pop is how the eye finds the
  human trace in a typed system; the lift is small because the card is
  not more important — it is more *personal*.
- **Structure.** `<article class="card card--hand" data-handwritten>` —
  identical card geometry; content set in Caveat 21px; a faint ruled
  guide (the same §6.5 line, in `--rule-red` at 60% — the writer ruled
  their own card lightly) and a filing line in Franklin chrome at the
  card's foot ("filed by hand — E.M., 1998" style attribution is content,
  written per §12's voice, never generated). The card's subject tab is
  the standard tab, typed label — the system filed the hand card like any
  other.
- **Motion spec.** Trigger: drawer open (§6.1 fan or §6.11 arrival) and
  scroll entry in shelf scenes. Lift: translateY −4px beyond the typed
  cards' fan offset, 520ms `settle` (vs 380ms for typed cards — the
  softness is duration + the extra distance, no bounce). Settle includes
  a 0.4° rotation easing to 0.15° rest rotation — the hand card sits
  *very slightly* crooked forever; 0.15° is felt, not seen.
- **States.** *Rest:* in the deck, 0.15° rotation, otherwise identical.
  *Lifted (arrival beat):* +4px, rotation 0.4°→0.15°. *Reading:* when
  flipped forward (§6.2) it behaves exactly as a typed card — the pop is
  an arrival courtesy, not a reading difference. *Hover:* §6.7 applies,
  with the lift starting from its crooked rest (the fingertip finds it
  where it lies).
- **Content-merge.** The handwriting is the card's actual content — a
  marginal note promoted to a card, a correction, a personal
  recommendation. Content that is merely *styled* handwritten (a typed
  announcement in Caveat) is a §9 failure.
- **Failure fallback.** Static: the card sits in the deck at 0.15°, fully
  readable. Nothing about its content depends on the pop.
- **Reduced-motion variant.** No lift; the card keeps its 0.15° rest
  rotation and hand face — identity without motion.
- **Performance budget.** One transform on one card per drawer.
  **Mobile variant:** lift reduces to +3px; rotation kept (it is the
  identity, and it costs nothing).
- **Choreography timeline (ms, within a §6.1 fan, fan start t=0).** The
  hand card is always the fan's last beat regardless of filed position:
  typed cards fan at 0/40/80/120 (380ms each). t=200: hand card starts
  (after the last typed card's start + 80ms gap — a breath). 200–720:
  lift + settle (520ms `settle`), rotation 0.4°→0.15° across 200–600.
  720: at rest; the drawer's §6.5 lines have all drawn by ~500, so the
  hand card's lighter line drawing at 200–550 sits inside the same beat.
- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Crooked 0.15°, in deck | Same |
  | Hover | §6.7 fingertip lift from crooked rest | n/a |
  | Focus | Standard card focus (§6.7/§6.8); rotation does not move the focus ring's box (ring drawn on unrotated box, card straightens to 0° while focus is within — a wobbling ring is unusable) | Same |
  | Active | §6.8 snap; straightens on selection like any card | Tap = same |
  | Scrolled-past | Filed with its rotation; its edge in the stack is the crooked one — findable | Same |
  | Disabled | Static crooked card | Same |

- **Breakpoint behaviour.** Identical at ≥768px. <768px: Caveat size
  holds at 20px (handwriting shrinks worse than type — below 20px it
  becomes illegible texture, so the card grows taller instead; card ratio
  is allowed to break for the hand card only, max +18% height).
- **Edge cases.** *Drawer with a hand card as its ONLY card:* it still
  pops (the drawer opens for a person, fine). *Two hand cards in source
  data:* the build must flag it — content lint (§10 gate) counts
  `data-handwritten` per drawer; >1 fails the gate, because the second
  one is a costume. *Long hand content:* Caveat at 21px fits ~15% fewer
  words per card; the card unit rule (§1: 90–140 words) tightens to
  70–110 for hand cards — content is edited to fit, the card never
  scrolls internally.
- **Accessibility spec.** Caveat is the theme's least legible face; the
  spec compensates: 21px minimum (20px mobile floor), line-height 1.35,
  ink at full `--typed-ink` (12.6:1), and the hand card's text is never
  the sole carrier of critical information (prices, dates, safety) — it
  is a note, a voice, a recommendation; the facts it mentions also exist
  on a typed card or in the filing line. Screen readers receive the text
  as normal text (it is text, not an image of writing — handwriting as
  image is banned outright).
- **Tokens consumed.** `--card-stock`, `--typed-ink`, `--rule-red`,
  `--ease-settle`, `--hand-lift: 4px`, `--hand-tilt: 0.15deg`,
  `--font-hand: "Caveat"`.

### 6.7 Fingertip-lift hover

- **What & why.** Hovering a card lifts its near edge — rotateX 3° toward
  the visitor, shadow lengthening — like a fingertip sliding under the
  card to pick it up; the card also tilts by pointer quadrant, up to 4°.
  It belongs because hover in a catalogue is *touch*: the visitor is
  handling the stock, and the card answers at the point of contact.
- **Structure.** The card is a single element with a pseudo-element shadow
  layer (`::after`, blurred radial in `--oak-deep` at 35%). Tilt is
  driven by CSS custom properties `--tilt-x/--tilt-y` set from the shared
  pointer handler (one listener per deck, coordinates normalised to the
  card's box); the transform composes `rotateX(calc(3deg + var(--tilt-x)))
  rotateY(var(--tilt-y))` inside the scene's perspective. Shadow length
  is a function of lift: `box-shadow` interpolates between the rest
  shadow (0 2px 6px rgba(46,42,38,0.18)) and the lifted shadow
  (0 14px 28px rgba(46,42,38,0.22), offset toward the light).
- **Motion spec.** Lift-in 200ms `settle`; tilt follows the pointer via
  the shared rAF loop, lerp 0.18 (the card feels held, not glued to the
  cursor — lerp above 0.3 reads as a toy). Release: 260ms `settle` back
  to rest (slightly slower than the lift: paper settles slower than it
  lifts). Quadrant tilt caps: rotateY ±4°, additional rotateX ±2° beyond
  the base 3° lift.
- **States.** *Rest:* flat, rest shadow. *Hover (fine pointer):* lifted +
  tilted. *Focus (keyboard):* the SAME lift, without tilt, triggered by
  `:focus-within` — keyboard users get the handling cue too, at 200ms,
  and it is the theme's focus affordance alongside the ring (§A11y).
  *Active (pressed):* lift collapses to 1° for 90ms (the fingertip
  presses before the snap, §6.8). *Scrolled-past / filed:* no hover —
  filed cards' edges are not interactive.
- **Content-merge.** The lift is the card itself responding; there is no
  hover overlay, tooltip card, or shadow-only ghost.
- **Failure fallback.** No JS: `:hover` still applies the lift via pure
  CSS (the tilt is the only JS part; without JS, hover = lift only, which
  is 80% of the effect at 0% of the risk).
- **Reduced-motion variant.** No lift, no tilt. Hover/focus state is
  shown by the card's tab edge thickening (border-top of the tab 2px→3px
  in `--tab-red`) — a state change with zero movement.
- **Performance budget.** Transform + shadow on one card at a time;
  shadow animation is the expensive part, so the shadow is rendered on
  the pseudo-element with `opacity`/`transform` doing the apparent
  lengthening (the blur itself never animates). **Mobile variant:** none
  — touch has no hover; tap goes straight to §6.8. (A long-press lift was
  considered and rejected: it delays the tap's snap and teaches a gesture
  no other surface honours.)
- **Choreography timeline (ms, pointer enters card t=0).** 0: lift
  starts. 0–200: rotateX 0→3°, shadow pseudo scales/offsets to lifted
  state. 60: tilt begins responding (a 60ms dead time so a pointer merely
  crossing the card doesn't twitch it). Continuous: tilt lerps behind the
  pointer (0.18). Pointer leaves (t=L): 40ms hold (a fingertip doesn't
  vanish), then L+40–L+300: release settle to rest.
- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Flat | Flat |
  | Hover | Lift 3° + tilt ≤4° | n/a |
  | Focus | Lift 3°, no tilt, + focus ring | Lift on focus via keyboard/switch: same |
  | Active | Press to 1° (90ms), then §6.8 | Press state from tap: §6.8 handles it |
  | Scrolled-past | Filed edges: inert | Inert |
  | Disabled | Reduced-motion: tab-edge thickening only | Same |

- **Breakpoint behaviour.** Identical ≥768px. <768px: cards are
  full-width; hover doesn't exist on the primary input, and on hybrid
  devices the lift caps at 2° (a wide card tipping 3° clips its shadow
  into the column edge).
- **Edge cases.** *Pointer crossing many cards quickly:* the 60ms tilt
  dead time + lerp means crossed cards lift and release without queueing
  animations (state-driven, not tween-queued). *Card inside a pinned
  scene while the scene is scrubbing:* hover lift is suppressed during
  §6.3's riffle (the thumb is busy) and enabled in reading position.
  *Nested interactive elements:* links inside the card do not lift
  independently — the card lifts as one object; the link's own state is
  its underline (§11).
- **Accessibility spec.** Lift/tilt are never the only state signal:
  focus adds the 2px `--tab-red` ring (offset 3px, on the card's
  unrotated box). Motion is suppressed under `prefers-reduced-motion`
  (above) and the tilt respects a per-theme `data-tilt="off"` content
  flag for cards whose content is a form (a tilting form is unusable —
  §6.16's form card never tilts). Touch targets inside cards are ≥44px.
- **Tokens consumed.** `--card-stock`, `--oak-deep`, `--tab-red`,
  `--ease-settle`, `--lift-angle: 3deg`, `--tilt-max: 4deg`,
  `--shadow-rest`, `--shadow-lifted`.

### 6.8 Paper-snap click

- **What & why.** Clicking a card snaps it fully forward — a quick
  scale-settle 0.98→1 with the deck behind shifting 2px — making it the
  reading card. Selection in a catalogue is physical: the chosen card
  comes out of the drawer, and the snap is the soundless *thock* of card
  stock landing flat.
- **Structure.** Any `.card` not in reading position is a button-equivalent:
  the card element itself carries the interaction (`role="button"` is
  wrong for a card that contains links — instead the card's *tab strip*
  is the activatable element: a real `<button class="card-tab">` spanning
  the card's top 44px, labelled "Bring forward: [card title]"). The snap
  animates the card; the deck shift animates the `.deck` container's
  translateY by 2px and back.
- **Motion spec.** 180ms total, `snap` easing: scale dips to 0.98 in the
  first 60ms (the press), releases to 1.0 by 180ms with the `flick`
  overshoot's tail (the composed curve is `snap` for scale, `settle` for
  the deck's 2px shift at 220ms). If the card was in a grid (§6.14), the
  snap is followed by the deck/scroll bringing it to reading position —
  the snap confirms the grab, then §6.2's flip completes the journey
  (snap 180ms, flip starts at 150ms, overlapping).
- **States.** *Rest (not reading):* in deck/grid, tab button available.
  *Pressed:* scale 0.98 at 60ms. *Snapping:* as timeline. *Reading:*
  the card is the deck's `data-state="reading"`; its tab button becomes
  disabled-labelled ("In reading position") and is removed from tab
  order (you cannot bring forward what is forward). *Filed after
  reading:* returns to the stack via §6.2.
- **Content-merge.** The snap moves the actual card with its actual
  content into reading position — it is selection, not a preview modal.
  (A modal preview of a card is banned: the catalogue has no photocopies.)
- **Failure fallback.** No JS: every card is already in normal flow and
  readable; the tab buttons are not rendered (they would promise a
  motion that cannot happen) — anchor links in the drawer index (§6.13)
  provide the navigation instead.
- **Reduced-motion variant.** No snap: clicking the tab scrolls the card
  into view (instant, `behavior: auto`) and it is simply the first fully
  visible card. State (reading) still applies for §6.4's counter.
- **Performance budget.** One card transform + one container transform,
  180–220ms. Negligible. **Mobile variant:** identical; the tab strip is
  48px tall for touch.
- **Choreography timeline (ms, click t=0).** 0: press registers; card
  scale →0.98 begins. 60: scale bottoms; deck shift begins (2px, 220ms
  `settle`). 60–180: scale releases 0.98→1.0. 150: if a flip is needed,
  §6.2's flip starts (card already in hand). 180: snap complete; §6.5's
  line is already drawn for a previously-seen card (no redraw) or draws
  now if this is a first arrival via click. 280: deck shift settled.
  300: §6.4 counter increments if this card is newly seen.
- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Tab button at rest; card shows §6.7 on hover | Tab strip at rest |
  | Hover | §6.7 lift; the tab strip's label underlines (typed underscore) | n/a |
  | Focus | Tab button focused: card lifts (§6.7 focus lift) + ring on the strip | Same |
  | Active | Press dip 60ms → snap | Tap: dip renders if the tap is ≥90ms, else snap only — never delay the snap to show the dip |
  | Scrolled-past (filed) | Tab button available again (re-reading a filed card is normal) | Same |
  | Disabled | Reading card's tab: disabled, removed from tab order, `aria-disabled` pattern not needed — it is a native `disabled` button | Same |

- **Breakpoint behaviour.** Identical at all sizes; <768px the flip after
  a grid snap uses the mobile deal-forward (§6.2 mobile variant).
- **Edge cases.** *Double-click / rapid re-click:* the second click
  during a snap is ignored (state flag until 300ms) — a card cannot be
  grabbed twice. *Clicking the currently-reading card's body (not tab):*
  nothing (body clicks are for text selection and links; only the tab
  strip activates). *Card whose content includes a form (§6.16):* the
  form card is never snapped from a grid — it lives in reading position
  in its drawer; its tab is informational only.
- **Accessibility spec.** The tab strip is a native `<button>` with a
  label naming the card and the action; activation moves no focus (focus
  stays on the button, which becomes the reading card's disabled tab —
  focus is transferred to the card's heading with `tabindex="-1"` at snap
  completion, because the button the user was on ceases to exist as an
  action). This transfer is announced by the §6.2 status line. Touch
  target: full card width × 44px (48px mobile). Keyboard: Enter/Space
  native; the snap is identical.
- **Tokens consumed.** `--card-stock`, `--typed-ink`, `--tab-red`,
  `--ease-snap`, `--ease-settle`, `--ease-flick`, `--tab-height: 44px`.

### 6.9 Catalogue counters

- **What & why.** "Cards filed / drawers / subjects" count up in Special
  Elite typewriter figures when the catalogue's stats card enters. The
  numbers describe this catalogue — its real size — typed on a card like
  everything else. A catalogue that knows its own extent is trustworthy;
  the count-up is the clerk typing the totals onto the stats card as you
  reach it.
- **Structure.** `<article class="card stats-card">` with three
  `<p class="stat">` lines, each: Franklin-free, all Special Elite —
  a typed label ("CARDS FILED") and a `<span class="count" data-count="1284">`
  figure. Counts come from the catalogue's data (server-rendered final
  values in the HTML; JS animates from ~70% of the value — never from 0:
  a catalogue of 1,284 cards did not start empty this morning, and
  counting from zero is a slot machine, §9).
- **Motion spec.** Trigger: stats card scroll entry (IO 0.3). 900ms,
  12 discrete steps (`settle` pacing — steps ease out), each step
  rendering the interpolated value with tabular figures. The three stats
  count in filing order, staggered 120ms. Final values land exactly on
  the data values.
- **States.** *Pre-entry (JS):* figures show 70% values, fully legible.
  *Counting:* stepping. *Counted:* final values; observer unobserves —
  never recounts on re-entry (the totals were typed once). *No-JS:*
  final values, printed.
- **Content-merge.** The stats are the catalogue's real extent, rendered
  on a card in the deck (typically the hero drawer's last card or a shelf
  scene's first). Invented round numbers ("10,000+ cards!") on a stats
  card whose drawer holds 40 is a §9 failure and a lie.
- **Failure fallback.** Final values are the HTML; JS only animates a
  span's text. Any failure = correct numbers, statically.
- **Reduced-motion variant.** No count: final values from first paint.
- **Performance budget.** Text updates on one span ×3, 12 steps each —
  trivial. **Mobile variant:** identical; figures at 26px.
- **Choreography timeline (ms, entry t=0).** 0: card deals in (§6.14,
  380ms). 200: stat 1 starts stepping (12 steps × 75ms = 900ms).
  320: stat 2 starts. 440: stat 3 starts. 1,100–1,340: stats land in
  order. 1,340: the stats card's §6.5 line — drawn at deal time, not
  here — is already complete; the last beat is the third figure's final
  strike, rendered with a 40ms full-ink emphasis (the typewriter key
  hits hardest on the last digit — implemented as a one-frame
  `font-variation` none; simply the final step holding 40ms longer).
- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest (counted) | Final figures, static | Same |
  | Hover / Focus | No response — the stats card is a card; §6.7 lift applies if it sits in a grid | Same |
  | Active | n/a | n/a |
  | Scrolled-past | Final figures | Same |
  | Disabled | Static final figures | Same |

- **Breakpoint behaviour.** Identical; <768px the three stats stack
  vertically (they are typed lines; stacking is their natural form).
- **Edge cases.** *Small catalogues (<30 cards):* counting 70%→100% of
  24 is 17→24 — the steps still read (7 steps used, values rounded to
  integers at every step; a step that doesn't change the integer is
  skipped, so tiny counts use fewer, honest steps). *Live catalogues
  (cards added while the page lives):* the stats card's values are
  re-derived on mutation and updated without animation (a typed
  correction, with the corrected figure underlined in `--rule-red` for
  2s — the theme's way of showing an edit).
- **Accessibility spec.** The counting span is `aria-hidden="true"`
  during the count; a visually-hidden sibling carries the final values
  from the start, so AT users get the totals immediately, once. Figures
  use tabular alignment so the line doesn't jitter for low-vision
  readers tracking it. Contrast: `--typed-ink` on stock, 12.6:1.
- **Tokens consumed.** `--card-stock`, `--typed-ink`, `--ink-soft`,
  `--rule-red`, `--ease-settle`, `--count-duration: 900ms`.

### 6.10 Riffling edge shimmer

- **What & why.** Every ~9 seconds, a soft light shimmer crosses the card
  edges of the currently open drawer, 1.2s, as if someone nearby is
  browsing another part of the same drawer. It is the theme's only
  ambient loop, and it belongs because a real reading room is shared: the
  catalogue feels inhabited, not staged. Its rarity is the point — a
  shimmer every 2s is a casino; every 9s is a colleague.
- **Structure.** A gradient layer on the open drawer's edge stack:
  `<div class="edge-shimmer">` absolutely positioned over the visible
  card edges (the top edges of the deck's filed stack + the reading
  card's top edge), background a 120deg linear gradient
  (transparent → `--card-stock` at +8% lightness via `color-mix` →
  transparent), background-position animated across. Pointer-events none;
  z-index above edges, below card faces' text (it crosses edges, never
  faces).
- **Motion spec.** Period: every 9s ± 1.5s jitter (a metronome is a
  machine; jitter is a person), sweep 1.2s `settle`. Only the *currently
  open* drawer's edges shimmer; only while the drawer is in the viewport
  (IO-gated); paused entirely when the tab is hidden
  (`visibilitychange`). Under lamplight (dark variant, §2) the shimmer
  warms to the amber wash colour.
- **States.** *Idle:* invisible. *Sweeping:* gradient crosses left→right
  (the direction a thumb riffles this drawer's filing order; a
  right-to-left sweep would contradict §6.3's direction and is a defect).
  *Suppressed:* during any flip (§6.2), riffle (§6.3), or drawer
  transition (§6.11) — ambient motion never competes with handled
  motion; the timer simply waits for a quiet window.
- **Content-merge.** The shimmer moves across the edges of the actual
  cards in the open drawer — it is light on the content's own edges.
- **Failure fallback.** No fallback needed: absence of shimmer is
  indistinguishable from a quiet room. If the layer fails to render, the
  page is unchanged.
- **Reduced-motion variant.** No shimmer, ever. The loop is the first
  thing the reduced-motion variant cuts, before any other element's
  variant applies.
- **Performance budget.** One gradient position animation on one layer,
  1.2s per ~9s; the layer is `will-change: background-position` only
  during the sweep. Battery rule: on `navigator.getBattery()` discharging
  + <20%, or on `Save-Data`, the period stretches to 24s. **Mobile
  variant:** period 14s (a phone's reading room is more private), sweep
  1s.
- **Choreography timeline (per sweep, t=0 at sweep start).** 0–150ms:
  gradient enters the first edge (opacity ramp of the highlight band
  0→0.5 — the band never exceeds 0.5 alpha; a brighter shimmer is a
  glare). 150–1,050ms: band crosses the edge stack at constant `settle`
  pace. 1,050–1,200ms: band exits, alpha →0. Then idle until the next
  jittered period.
- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest (idle) | Invisible | Invisible |
  | Hover / Focus / Active | No response; suppressed while the user is handling cards (§6.7/§6.8 active states pause the timer) | Same |
  | Scrolled-past | The drawer left behind stops shimmering; the newly open drawer adopts the loop after a full period's delay | Same |
  | Disabled | Reduced-motion / hidden tab / battery rule: off or stretched | Same |

- **Breakpoint behaviour.** Identical at all sizes; at <768px the band
  narrows (edges are shorter) — gradient angle steepens to 100deg so the
  crossing still takes the full 1s.
- **Edge cases.** *Drawer with no filed stack visible (first card):* the
  shimmer crosses the reading card's top edge and the drawer mouth's
  edge only — still truthful. *Multiple drawers on screen (shelf scenes
  show drawer fronts):* only the open drawer shimmers; shut drawers are
  shut. *User has been idle 60s+:* the shimmer continues (it is the room,
  not a nudge) but never escalates — no sound, no badge, no "still
  there?" — the catalogue does not want attention, it has it.
- **Accessibility spec.** Pure ambience: `aria-hidden`, no information,
  no focus interaction. It is the canonical example in this theme of
  motion that must be cut first under any motion sensitivity — and it
  is, by the reduced-motion variant and by a theme-level
  `data-ambience="off"` host flag.
- **Tokens consumed.** `--card-stock`, `--card-shade`, `--lamp-wash`
  (dark variant), `--ease-settle`, `--shimmer-period: 9s`,
  `--shimmer-sweep: 1.2s`.

### 6.11 Drawer-shut transition

- **What & why.** Navigation in a catalogue is moving drawers: the
  current drawer shuts — slide with a soft thunk settle — and the
  destination section's drawer slides open with its cards fanning
  (§6.1's fan, at navigation scale). It belongs because route change is
  the one moment every SPA gets to declare its world, and this world's
  declaration is: *same cabinet, different drawer.*
- **Structure.** A transition wrapper around the routed view:
  `<div class="cabinet-view">`. The outgoing view is wrapped in a
  drawer-box frame (its drawer front + label); on navigation the frame
  shuts (the view slides down/behind the front, the front rises to
  cover), then the incoming view's frame opens. Implementation: two
  absolutely-stacked layers inside the cabinet column during the
  transition only; at rest, a single static layer (no standing cost).
  The drawer label during transit shows the destination's range — you
  see which drawer is arriving before it opens.
- **Motion spec.** Out: view translateY 0→18px + drawer front slides to
  shut over 400ms `drawer`, ending with a 2-frame settle (a 1px
  overshoot at 380ms, gone by 400 — the thunk, visual only). Hold shut:
  80ms (a drawer is shut for a beat; instant re-open reads as a glitch).
  In: destination front opens 800ms `drawer` with its cards fanning per
  §6.1 (stagger 40ms; at navigation the fan caps at 4 cards). Total
  ≈ 1,280ms. The browser's own scroll restoration is suppressed during
  transit and applied at the shut beat (scroll jumps happen while the
  drawer is shut — never watched).
- **States.** *Rest:* one view, no frames visible (frames are the
  cabinet's own edges). *Shutting / shut / opening:* as timeline.
  *Interrupted (user navigates again mid-transit):* the transit
  fast-forwards to shut (120ms), then opens the newest destination —
  destinations never queue more than one deep.
- **Content-merge.** The drawers that shut and open are the sections'
  own drawers, labelled with their real ranges; the transition is the
  navigation model (§6.13) made visible.
- **Failure fallback.** If the transition machinery fails or JS is off:
  plain route change, instant, content complete. The transition is an
  enhancement layered on a normal router (or on full page loads, where
  only the §6.1 opening plays on arrival).
- **Reduced-motion variant.** No shut/open: a 120ms crossfade of the
  view at full opacity range 0.25→1 (never to 0 — the cabinet never
  blinks), or instant swap if the host prefers.
- **Performance budget.** Two layers animating transforms for ≤1.3s per
  navigation; layers are created on demand and released at rest.
  **Mobile variant:** out-travel halves (9px), fan caps at 3 cards,
  total ≈ 1,050ms.
- **Choreography timeline (ms, navigation t=0).** 0: click/route event;
  destination drawer label is set on the transit frame. 0–400: shut
  (`drawer`); at 380 the 1px thunk overshoot; at 400 scroll restoration
  applies (hidden by the shut front). 400–480: shut hold; the §6.4 tab
  rides to the destination drawer's rail position during this hold.
  480–1,280: open + fan (§6.1 beats compressed: box 480–1,280, cards
  from 740, stagger 40, hand card last if the destination drawer leads
  with it in fan order). 1,280: transit layers released; focus moves to
  the new view's heading (§A11y).
- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Single view | Same |
  | Hover / Focus | Nav items use §6.13 states; focus is never inside the outgoing view after t=0 (focus moves to the transit frame's label, then to the new heading at 1,280) | Same |
  | Active | The clicked nav item shows its pressed state until the shut beat, then the destination item shows current | Same |
  | Scrolled-past | n/a (route-level) | n/a |
  | Disabled | Instant route change | Same |

- **Breakpoint behaviour.** ≥1200px: as spec'd. 768–1199px: fan caps at
  3. <768px: the drawer front is the top strip (§6.4 mobile label); the
  shut is a 10px slide of the strip + view; total ≈ 900ms.
- **Edge cases.** *Same-drawer navigation (anchor within the section):*
  no transition — the drawer is already open; §6.2/§6.8 handle movement
  inside it. *Browser back/forward:* the transition plays in reverse
  order of drawers (the drawer you came from shuts) — direction is
  metadata, the motion is identical. *Slow route data:* if the
  destination's data isn't ready by the shut beat, the shut drawer
  *waits shut* with §6.12's blank cards visible through its mouth crack
  (a 12px opening) — never re-open the old drawer as a loading state.
- **Accessibility spec.** During transit the outgoing view is
  `inert`; the transit frame carries `role="status"` text "Opening
  drawer: [range]" (visually the brass label, available to AT as text).
  At completion, focus lands on the new page's `<h1>` (`tabindex="-1"`),
  and the document title has already updated at t=0. The 1px thunk
  overshoot is visual only; there is no audio anywhere in this theme.
- **Tokens consumed.** `--drawer-oak`, `--oak-deep`, `--brass`,
  `--card-stock`, `--typed-ink`, `--ease-drawer`, `--ease-settle`,
  `--transit-shut: 400ms`, `--transit-open: 800ms`.

### 6.12 Blank-card skeleton loading

- **What & why.** Loading shows blank ruled skeleton cards in the drawer;
  as content arrives, the cards type in — Special Elite, line by line.
  It belongs because a catalogue's loading state is an unfilled card:
  the stock is there, the typing hasn't happened yet. A spinner in a
  card catalogue is a foreign object; a blank card is furniture.
- **Structure.** `<article class="card card--blank" aria-hidden="true">`
  replicas of the expected card geometry (same ratio, same ruled line
  printed — a blank card is still ruled stock), with 3–5 blank line
  blocks (`--card-shade` bars at text widths, never grey rectangles at
  random widths: the bars follow the card's real line lengths — title
  bar 62%, body bars 100/94/88%). On arrival, each real card replaces
  its blank and its content types in: lines appear at 24ms per character
  for the title, body lines reveal line-by-line at 90ms per line (body
  text does NOT type character-by-character — a full card at 24ms/char
  would take 20s; the typing fiction is rationed to titles and short
  lines, stated here so no builder types a paragraph).
- **Motion spec.** Blank state: static, except a single §6.10-style
  shimmer across the blank cards' edges every 4s while loading persists
  (loading is the one state where the room sounds busier — someone is
  fetching). Type-in: title 24ms/char `steps(1)` per character; body
  lines 90ms/line with a 60ms `settle` density ramp per line (55%→100%,
  the card being inked). A card's total type-in caps at 900ms regardless
  of length (long titles truncate the per-char rate to fit the cap).
- **States.** *Blank:* ruled, empty, honest. *Typing:* as above.
  *Filled:* becomes the real card (all §6 states apply from here).
  *Failed load:* the blank card is replaced by the §6.18 misfiled/error
  card pattern — an error written on a card, in the error voice (§12),
  with a retry chrome button on the drawer front. A blank card that
  stays blank forever is the failure this state design exists to
  prevent: any card still blank after 8s self-replaces with the error
  card even if the request hasn't technically failed.
- **Content-merge.** The skeleton has the real cards' geometry and the
  real drawer's position; when content lands there is zero layout shift
  (CLS 0 by construction — the blank *is* the card's box).
- **Failure fallback.** If JS is off, there are no blanks: content is
  server-rendered or the page is a normal document load. Blanks exist
  only in client-side fetching.
- **Reduced-motion variant.** Blanks are static (no shimmer); arriving
  content appears whole, no type-in.
- **Performance budget.** Bars are static backgrounds; type-in is text
  insertion on ≤6 cards. **Mobile variant:** identical; blanks cap at 3
  per drawer on small screens (the rest of the drawer loads as a simple
  "filing…" chrome line).
- **Choreography timeline (per card, content arrival t=0).** 0: blank's
  bars fade to stock in 120ms (the card is picked up). 120: title starts
  typing (24ms/char). Title end +0: body line 1 ramps (60ms). Lines
  follow at 90ms intervals. Last line +60ms: card is filled; its §6.5
  rule — printed on the blank already — does not redraw (it was always
  there; blanks are ruled stock). If the card is the drawer's hand card,
  §6.6's pop fires at last line +100ms.
- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest (blank) | Ruled blank, edge shimmer 4s | Same |
  | Hover / Focus | Blanks are inert and unfocusable | Same |
  | Active | n/a | n/a |
  | Scrolled-past | Blanks above the fold continue loading; content replaces in place | Same |
  | Disabled | No-JS: no blanks exist | Same |

- **Breakpoint behaviour.** Identical; <768px blank cap 3 (above).
- **Edge cases.** *Instant cache hit (<120ms):* if content arrives
  before the blank has been painted for 120ms, the blank never shows
  (no flash of skeleton for fast loads — blanks render only after a
  120ms fetch delay threshold). *Partial arrival:* cards fill
  individually in arrival order, not filing order — with the deck
  re-sorting (a 200ms `settle` shift of filled cards into filing
  position) once all arrive; a half-filled drawer is a true picture of
  a fetch in progress. *Very long load:* after 8s, error cards (above);
  the drawer's other content remains usable.
- **Accessibility spec.** The loading region carries `aria-busy="true"`
  and a visually-hidden `role="status"` line: "Filing cards…" then
  "Drawer ready: [n] cards" on completion — announced once, not per
  card. Blank cards are `aria-hidden`. The 8s error card is a real card
  with a real heading and a focusable retry button.
- **Tokens consumed.** `--card-stock`, `--card-shade`, `--rule-red`,
  `--typed-ink`, `--ink-soft`, `--ease-settle`, `--type-char: 24ms`,
  `--blank-cap: 6`.

### Page-family elements

The six elements below are the theme's furniture for real sites —
navigation, content cards, search, forms, footer, and the empty/error
state. Each carries the same full spec (v1 + v2 layers) as the signature
elements.

### 6.13 Cabinet navigation (drawer fronts & brass label holders)

- **What & why.** Primary navigation is the cabinet itself: a row (or,
  in the hero scene, the visible fronts) of drawer fronts, each with a
  brass label holder carrying its section's typed range. To navigate is
  to choose a drawer. It belongs because the catalogue's index of drawers
  is its top-level structure — a conventional top-bar menu pasted over a
  cabinet would be two organisations fighting.
- **Structure.** `<nav class="cabinet-nav" aria-label="Drawers">`: a
  horizontal strip of `<a class="drawer-front">` items (oak front, brass
  holder, Franklin label), the current section's front rendered *open*
  (its holder lit, front lowered 4px, a card edge visible at its top).
  On mobile it becomes a single "DRAWERS" front that opens a full list
  (the cabinet index, a plain list of fronts in a sheet). Secondary nav
  (within-section) is the drawer index: the card title list of §6.3's
  fallback, rendered as a contents card.
- **Motion spec.** Hover: holder glint — a brass gradient sweep across
  the holder, 200ms `settle`, plus the front's card edge rising 2px
  (the drawer is about to be pulled). Active press: front lowers 2px,
  90ms `snap`. Route change hands off to §6.11. The current front's
  open state is static (no loop — the §6.10 shimmer never touches
  chrome).
- **States.** *Rest:* fronts shut, labels readable. *Current:* open
  front as above, `aria-current="page"`. *Hover/focus:* glint + edge
  rise; focus adds the standard ring on the front (oak-appropriate:
  ring in `--card-stock` with an `--oak-deep` outline — the red is
  rationed to cards). *Disabled (a drawer with no published cards):*
  the front renders with its holder empty — a typed label "EMPTY —
  BEING FILED" only if the section is genuinely forthcoming; a
  permanently empty drawer is removed, not labelled.
- **Content-merge.** Labels are the sections' real subject ranges,
  derived from the same data as the drawers themselves; renaming a
  section renames its front. There is no nav item that is not a drawer.
- **Failure fallback.** No JS: plain list of links in fronts' clothing —
  fully functional. The open/close theatre is §6.11's, not the nav's.
- **Reduced-motion variant.** No glint sweep (holder brightens
  instantly), no edge rise; state shown by the label's ink deepening.
- **Performance budget.** Static chrome; one gradient sweep on hover.
  **Mobile variant:** the single-front + index sheet pattern (above);
  the sheet is a plain `<div>` panel, not a modal — it is a drawer
  pulled all the way out, and it closes by choosing or by its close
  front.
- **Choreography timeline (hover, t=0).** 0–200: glint sweeps the
  holder. 40–200: card edge rises 2px (`settle`). Leave: edge settles
  back 160ms; glint does not reverse (light doesn't un-sweep; it fades
  120ms). Press: 90ms lower; release fires navigation.
- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Shut fronts; current open | Index front shut |
  | Hover | Glint + edge rise | n/a |
  | Focus | Ring + glint (instant) + edge rise | Same via keyboard |
  | Active | Press lower 90ms → §6.11 | Tap = press → §6.11 |
  | Scrolled-past | Nav is fixed chrome (the cabinet's top row); it does not scroll away — a catalogue's cabinet doesn't leave the room | Same, as the top strip |
  | Disabled | Empty-holder front, not focusable | Same |

- **Breakpoint behaviour.** ≥1200px: full front row (up to 7 fronts;
  more sections group into a "MORE DRAWERS" front opening the index).
  768–1199px: fronts compress (labels shorten to subject word; ranges
  move to the index). <768px: single-front + sheet.
- **Edge cases.** *One-section site:* no nav row at all — a one-drawer
  cabinet needs no index; the hero drawer is the site. *Very long
  labels:* truncate in the holder with ellipsis; the full range lives
  in the index and in §6.4's label. *Sticky behaviour:* the nav strip
  sticks at the cabinet top; its oak is the cabinet's oak, so sticking
  is invisible — no shadow appears (a shadow would admit the strip is
  an overlay).
- **Accessibility spec.** Landmark `<nav>` with a distinct label per
  instance ("Drawers", "In this drawer"). Fronts are links with full
  text labels (never letter-only). `aria-current` on the open front.
  The mobile sheet is focus-managed (focus to first item on open,
  return focus on close, Esc closes). Touch targets: fronts ≥48px
  tall. Contrast: Franklin labels in `--card-stock` on `--drawer-oak`
  5.8:1 at 13px/700 — permitted as large-equivalent bold small text;
  the same label in the index sheet sits on stock in ink at 12.6:1.
- **Tokens consumed.** `--drawer-oak`, `--oak-deep`, `--oak-pale`,
  `--brass`, `--card-stock`, `--typed-ink`, `--ease-settle`,
  `--ease-snap`, `--front-height: 56px`.

### 6.14 Entry cards (the standard content card)

- **What & why.** The unit of all content in shelf scenes and listings:
  a catalogue card carrying one entry — tab with subject, filing line,
  ruled line (§6.5), title, body excerpt, filing data, and an optional
  pasted photo. If §6.2's reading card is the deck's focus, §6.14 is the
  stock the deck is made of; every list, grid, search result and related
  rail in the theme is these cards, dealt.
- **Structure.** `<article class="card entry-card">`: `<div class="card-tab">`
  (subject tab, tab-red edge + typed subject), `<p class="filing-line">`
  (card number · date filed · drawer), the §6.5 SVG rule, `<h3>` title,
  body excerpt (≤ 40 words in listings), optional `<figure class="pasted-photo">`
  (photo inside a printed border, caption typed beneath), footer line
  with cross-references ("see also: …" as real links). Whole-card
  interaction via §6.8's tab-strip button (top 44px); body links remain
  individually focusable.
- **Motion spec.** Deal-in on scroll entry: from the drawer mouth mask
  (§5) + translateY 14px, 380ms `settle`, stagger 60ms in reading order
  (left→right, top→bottom). Pasted photo scales-in-frame 104%→100%,
  520ms `settle`, starting when the card lands. Hover/focus/click:
  §6.7/§6.8 unchanged.
- **States.** *In deck:* dealt, at rest. *Dealing:* as timeline.
  *Reading (after §6.8):* leaves the grid — the grid closes the gap
  with a 200ms `settle` shift of following cards (the shelf re-shelves);
  a shade placeholder edge remains in the grid marking where the card
  lives ("OUT — being read", typed on the edge) so the visitor can
  find the gap again; when the card is filed back, it returns to the
  same slot. *Filed/past:* normal.
- **Content-merge.** The card IS the entry — title, excerpt and data are
  the entry's real metadata. A card whose excerpt is marketing copy
  instead of the entry's actual opening is a §9 failure.
- **Failure fallback.** Static grid of fully readable cards; deal-in is
  JS-applied pre-states only.
- **Reduced-motion variant.** Cards appear in place (no deal, no mask);
  grid gap-closing on read is instant.
- **Performance budget.** Deal animations cap at 6 concurrent; photos
  lazy-load with reserved boxes (the printed border is the reservation —
  zero CLS). **Mobile variant:** single column; deal stagger 40ms;
  photo border insets shrink (8px).
- **Choreography timeline (grid of 6, first card enters t=0).** Cards
  start at 0/60/120/180/240/300 (380ms each) — the ripple completes at
  680ms. Each card's rule draws at its landing −30ms (§6.5). Photos
  begin their scale-settle at their card's landing, complete +520ms.
  A second row entering later deals independently (stagger restarts per
  row-group, so a long grid never builds a 3s backlog).
- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Dealt, flat | Same |
  | Hover | §6.7 lift + tilt | n/a |
  | Focus | §6.7 focus lift + ring | Same |
  | Active | §6.8 snap → reading | Tap tab strip → reading |
  | Scrolled-past | Remains dealt (deals never reverse) | Same |
  | Disabled | n/a (cards aren't disableable; an entry under embargo renders as a card with a typed "NOT YET FILED" line and no tab button — its content is genuinely absent, not greyed) | Same |

- **Breakpoint behaviour.** ≥1200px: 3 per row at 360px. 768–1199px:
  2 per row. <768px: 1 per row, card ratio relaxes (height by content,
  min 216px) — the 5:3 ratio governs *listing* cards; a phone column of
  rigid 5:3 cards wastes the drawer.
- **Edge cases.** *Entries with no photo:* the card's photo area
  collapses — cards in a row keep a shared baseline for titles (ragged
  bottoms are fine; ragged titles are not). *Very long titles:* 2-line
  clamp with the full title on the reading card; the clamp is CSS, the
  data is whole. *Mixed drawers in one listing (search across
  subjects):* each card keeps its own drawer's tab colour-language —
  tabs are subject-coloured only by the single `--tab-red`; the drawer
  is named in the filing line instead (colour-coding drawers would
  break the palette's red ration).
- **Accessibility spec.** Cards are `<article>`s with real headings;
  the tab-strip button's label is "Bring forward: [title]". Photo alt
  text is the caption's responsibility — the caption and alt are
  written from the same source line so they cannot drift. The "OUT"
  placeholder edge is `aria-hidden`; the reading card's location is
  announced by §6.2's status line. Contrast per §2 pairings; the filing
  line uses `--ink-soft` (7.4:1).
- **Tokens consumed.** `--card-stock`, `--card-shade`, `--typed-ink`,
  `--ink-soft`, `--tab-red`, `--rule-red`, `--ease-settle`,
  `--card-w: 360px`, `--deal-stagger: 60ms`.

### 6.15 Catalogue search & subject tabs

- **What & why.** Search in a catalogue is asking the clerk for a
  drawer: a chrome search field (Franklin, on oak) plus subject tabs
  that pull drawers. Results are §6.14 cards dealt from the relevant
  drawers — including the misfiled card, findable under its *correct*
  subject with its note attached (§4). It belongs because findability
  is the catalogue's promise; browse (§6.3) is serendipity, search is
  intent, and the theme serves both without confusing them.
- **Structure.** `<form class="catalogue-search" role="search">` on a
  drawer-front strip: Franklin label "SEARCH THE CATALOGUE", text
  input styled as a typed request slip (stock background, ink text,
  red rule under the field — the slip is paper pinned to the drawer),
  submit = chrome button "PULL DRAWER". Below, subject tabs
  (`<div class="subject-tabs">`): one tab per drawer, styled as card
  tabs, acting as filters (toggle buttons, `aria-pressed`). Results
  region: a shelf scene of §6.14 cards with a results filing line
  ("14 CARDS — DRAWERS: HISTORY, RECIPES").
- **Motion spec.** Submit: the relevant drawer fronts' edges rise 2px
  (§6.13 hover beat, 200ms) as if pulled, results deal per §6.14
  (stagger 60ms). Tab toggle: the tab slides 3px out of its slot
  (120ms `snap`) when pressed-in; results re-deal. No spinner: a search
  slower than 300ms shows §6.12 blanks in the results shelf.
- **States.** *Idle:* empty slip, all tabs out. *Filtering:* ≥1 tab in.
  *Results:* filing line + dealt cards. *No results:* §6.18's empty
  drawer card (never a bare "no results" line). *Error:* the request
  slip gains a red typed correction line (§12's error voice) — the
  clerk writes back on the slip.
- **Content-merge.** Search searches the catalogue's real index (titles,
  subjects, filing data, full card text); the tabs are the real
  drawers. A search that searches a different corpus than the drawers
  contain is a §9 failure.
- **Failure fallback.** No JS: the form submits to a server results
  page built from the same §6.14 cards; tabs become links to drawer
  pages. All functionality survives; only the deal is lost.
- **Reduced-motion variant.** Results appear without dealing; tabs
  toggle without sliding (pressed state = tab ink deepens + a red
  underline rule).
- **Performance budget.** Deal caps per §6.14; search input never
  triggers per-keystroke deals on large catalogues — submit-driven,
  with an optional live mode only under 200 total cards (stated so a
  builder doesn't wire a 3,000-card catalogue to keystrokes).
  **Mobile variant:** the slip stacks above the tabs; tabs scroll
  horizontally as a tab strip (they are tabs — a scrolling tab strip
  is in-fiction).
- **Choreography timeline (submit, t=0).** 0: button press (90ms).
  0–200: matching fronts' edges rise. 150: results region's old cards
  file away (a single 180ms `settle` stack-down — results don't flip
  individually; the shelf is re-dealt). 200–880: new results deal
  (§6.14 ripple). Filing line types its count at 24ms/char starting
  300, capped 600ms.
- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Slip empty, tabs out | Same, stacked |
  | Hover | Front-edge rise on the search strip; tabs use card hover (§6.7 lite: 2° lift — tabs are small; full card physics on a 30px tab is clownish) | n/a |
  | Focus | Input: red rule thickens 1.5→2.5px + ring on the slip; tabs: ring | Same |
  | Active | Tab press slides 3px; submit presses 90ms | Same |
  | Scrolled-past | The search strip sticks with the cabinet top (it is chrome on the cabinet, §6.13's stick rule) | Same |
  | Disabled | A drawer under embargo (§6.14) has its tab disabled with the "NOT YET FILED" label | Same |

- **Breakpoint behaviour.** ≥1200px: slip + tabs on one strip.
  768–1199px: tabs wrap to a second row. <768px: stacked, tab strip
  scrolls horizontally.
- **Edge cases.** *Query matching the misfiled card's correct subject:*
  it appears, with its note and a filing line showing where it actually
  lives ("found in: COOKERY — filed under HISTORY, see note") —
  cross-reference honesty is the catalogue's soul. *Query matching
  nothing in a small catalogue:* §6.18 suggests the nearest drawers by
  subject name (real suggestions from the index, never generated
  text). *Very large result sets:* paginate by drawer handfuls —
  "NEXT HANDFUL" deals 12 more; infinite scroll is banned (a drawer
  you can never finish riffling is a broken drawer).
- **Accessibility spec.** `role="search"`, labelled input, results
  region `aria-live="polite"` announcing the filing line's count text
  once per search ("14 cards found in History and Recipes"). Tabs are
  `<button aria-pressed>` in a labelled group. The red rule focus cue
  is never the only cue (ring too). All targets ≥44px.
- **Tokens consumed.** `--card-stock`, `--drawer-oak`, `--oak-deep`,
  `--typed-ink`, `--tab-red`, `--rule-red`, `--ease-snap`,
  `--ease-settle`, `--slip-rule: 1.5px`.

### 6.16 The filing form (request / signup / contact)

- **What & why.** The conversion surface of a catalogue is a request
  slip: to subscribe, request a card, or ask the librarian, the visitor
  fills a slip that gets filed. The form lives on an oversized card in
  reading position inside its own drawer ("REQUESTS"), fields typed
  lines on the stock. It belongs because every catalogue has a request
  desk; a generic web form dropped into the cabinet would break the
  world at exactly the moment of trust.
- **Structure.** `<form class="filing-form">` on `<article class="card
  form-card" data-tilt="off">` (§6.7: form cards never tilt). Fields:
  Franklin labels *above* each field (chrome labels the desk's
  furniture), inputs as typed lines — transparent background, bottom
  rule in `--ink-soft`, Special Elite input text (the visitor types on
  the slip). The submit is a chrome button on the card's foot: "FILE
  THIS REQUEST". Errors appear as red typed corrections *under* the
  field, in the clerk's voice (§12). Success: the slip is stamped —
  a tab-red typed stamp "FILED — [date]" rotates in at −6° with a
  180ms `snap` (the theme's one stamp; it is §6.10's cousin and the
  only place a stamp exists), and the card files itself (§6.2 flip)
  into the drawer after 1.2s, leaving the §6.18-style confirmation
  card ("Your request is filed under REQUESTS — № 118").
- **Motion spec.** Field focus: the field's rule draws in `--tab-red`
  left→right 240ms `settle` (the §6.5 draw, repurposed — the clerk
  underlines the line you're writing on). Submit press: 90ms. Stamp:
  scale 1.3→1 + rotate −8°→−6°, 180ms `snap`, with a 40ms card shake of
  1px (the desk absorbs the stamp). File-away at +1,200ms per §6.2.
- **States.** *Rest:* blank slip, rules in ink-soft. *Focus:* red rule
  draw + label deepens. *Filled-valid:* rule rests in ink (the line is
  written). *Error:* red correction line types in (24ms/char, capped
  500ms) + the field's rule stays red. *Submitting:* button label
  types "FILING…" and the card's edges show §6.12's shimmer at 4s —
  busy, in-fiction. *Success:* stamp + file-away + confirmation card.
  *Disabled (submit until valid):* the button is NOT disabled —
  catalogue desks accept the slip and correct it; validation is on
  submit, corrections are the service. (Disabled-submit is a §9
  failure in this theme.)
- **Content-merge.** The slip is the form; its fields are the real
  request's fields. The filed number in the confirmation is the real
  submission's reference.
- **Failure fallback.** No JS: standard form post, errors rendered
  server-side in the same correction style, success = a confirmation
  page built as the confirmation card. Network failure on submit: the
  slip stays filled (never cleared), a correction line in the error
  voice offers retry.
- **Reduced-motion variant.** No stamp animation (stamp appears
  printed), no file-away flip (confirmation replaces instantly), rule
  focus = instant red.
- **Performance budget.** Negligible motion; the form must never wait
  on animation to submit (submit fires at press, animations are
  commentary). **Mobile variant:** the form card is full-width; the
  stamp lands at −4° (smaller card, smaller gesture).
- **Choreography timeline (submit, t=0).** 0: press. 0–90: button
  press; label → "FILING…". Async gap: shimmer at 4s period if waiting.
  On success (t=S): S–S+180: stamp lands (card shake S+120–S+160).
  S+200: confirmation number types onto the stamp line (24ms/char).
  S+1,200: card files (§6.2 flip, 420ms). S+1,620: confirmation card in
  reading position; focus moves to its heading (§A11y).
- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Blank slip | Same |
  | Hover | Fields: rule warms to ink (200ms); button: §11 chrome hover | n/a |
  | Focus | Red rule draw 240ms + label deepen | Same (focus on tap) |
  | Active | Submit press 90ms | Same |
  | Scrolled-past | The form drawer stays a normal drawer; a half-filled slip persists (form state is kept per session — a desk doesn't clear your slip because you browsed) | Same |
  | Disabled | Submit never disabled (above); individual fields may be `readonly` when pre-filed from the visitor's data — rendered as already-typed lines with a Franklin note "from your reader's card" | Same |

- **Breakpoint behaviour.** ≥1200px: form card at reading width
  (760px), two short fields may share a typed line (name + date).
  768–1199px: single column fields. <768px: full-width card, fields
  stack, input font holds 17px (also prevents iOS zoom — under 16px
  inputs trigger it; 17px typed is both in-fiction and safe).
- **Edge cases.** *Long forms (>8 fields):* the slip becomes two cards
  in one drawer ("SLIP 1 OF 2"), flipped per §6.2 — never a scrolling
  mega-card. *Autofill:* autofilled values render in ink-soft with a
  typed note "filled by your browser" — the fiction survives by
  acknowledging the machine's hand, and the visitor can edit (values
  deepen to ink on edit). *Error summary:* multiple errors list on a
  correction card dealt on top of the form card, each linking to its
  field.
- **Accessibility spec.** Native labels (Franklin is styling, the
  `<label>` is real), errors linked via `aria-describedby`, error
  summary `role="alert"` on submit only, focus moves to the first
  error field. The stamp is decorative (`aria-hidden`); success is
  announced by the confirmation card's heading + a `role="status"`
  line. Contrast: correction text `--tab-red` on stock 4.7:1 at
  14.5px/600-equivalent — Special Elite has no weights; corrections
  are set at 15.5px to meet large-text equivalence, and always paired
  with the field's red rule (not colour alone).
- **Tokens consumed.** `--card-stock`, `--typed-ink`, `--ink-soft`,
  `--tab-red`, `--rule-red`, `--ease-settle`, `--ease-snap`,
  `--stamp-angle: -6deg`, `--type-char: 24ms`.

### 6.17 Cabinet footer (the base drawer)

- **What & why.** The footer is the cabinet's base drawer, shut: a deep
  oak band carrying the colophon of the catalogue — who keeps it, when
  it was last filed, the drawer index repeated as plain links, and the
  catalogue's totals (§6.9's numbers, at rest). It belongs because a
  cabinet stands on its base; a website footer pasted under a cabinet
  would be a rug under furniture.
- **Structure.** `<footer class="cabinet-footer">` on `--oak-deep`: a
  brass holder with the catalogue's name; columns of Franklin links on
  oak (the drawer index, the house links — about, requests, visit);
  a final typed line on a narrow stock strip (the footer's one card):
  "This catalogue holds [n] cards in [m] drawers. Last filed:
  [date]. Kept by [name]." — real data, updated by the build/CMS, in
  Special Elite on stock (the split law of §3 holds even here: the
  typed line sits on its strip of stock, never directly on oak).
- **Motion spec.** Entry: the base drawer does not open; its holder
  glints once as it enters (200ms, §6.13's glint) — the cabinet
  acknowledging you've reached the bottom. The typed line's numbers
  do not count (they are at rest; §6.9 counted them upstairs). Links
  hover per §11.
- **States.** *Rest:* shut, complete. *Hover/focus:* per link. No
  other states — a footer that performs is a §9 failure.
- **Content-merge.** The footer's index is the cabinet's real index;
  its totals are §6.9's real totals. No newsletter form lives here
  (that is §6.16's drawer); no social icons (a card catalogue has
  brass, not badges — contact routes are typed lines in the index).
- **Failure fallback.** Static footer; nothing to fail.
- **Reduced-motion variant.** Identical (the glint is instant).
- **Performance budget.** Zero standing cost. **Mobile variant:**
  columns stack as drawer fronts in a single column of oak.
- **Choreography timeline.** Single beat: footer crosses 30% viewport
  → holder glint 200ms at +100ms. Nothing before, nothing after.
- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Shut base drawer | Stacked |
  | Hover | Link underline (§11); holder glint on footer hover once per entry | n/a |
  | Focus | Stock ring on links (per §6.13's chrome ring) | Same |
  | Active | Link press: 90ms deepen | Same |
  | Scrolled-past | n/a — it is the bottom | n/a |
  | Disabled | n/a | n/a |

- **Breakpoint behaviour.** ≥1200px: 3–4 columns. 768–1199px: 2
  columns. <768px: single column; the typed strip wraps to two lines
  (the data is never truncated — a truncated total is a wrong total).
- **Edge cases.** *Short pages (footer visible at load):* the glint
  does not fire at load (it is an arrival beat; at load nothing has
  arrived). *Catalogue totals changing between §6.9 and the footer:*
  both render from the same data source in the same build — a page
  whose stats card and footer disagree fails §10.
- **Accessibility spec.** `<footer>` landmark; link lists are real
  lists with headings ("Drawers", "The house"). Contrast: Franklin in
  `--card-stock` on `--oak-deep` 8.3:1; the typed strip is ink on
  stock 12.6:1.
- **Tokens consumed.** `--oak-deep`, `--drawer-oak`, `--brass`,
  `--card-stock`, `--typed-ink`, `--ease-settle`.

### 6.18 The misfiled card (empty states, 404, error cards)

- **What & why.** Every empty state in this theme is a drawer state,
  and the theme's emblem is the misfiled card: a card filed one slot
  out of order, carrying its typed note — "Misfiled since 1998. It
  lives here now." Empty search results, an empty drawer, a 404, and
  load errors (§6.12) all speak through cards: the empty drawer card
  ("This drawer is empty. Its cards are being typed."), the 404 card
  (a card whose filing line reads "NOT IN THIS CATALOGUE" and whose
  body, in the catalogue's voice, directs the visitor to the nearest
  real drawers). It belongs because absence in an archive is a filing
  fact, not a void — the catalogue always answers, even when the answer
  is "not here".
- **Structure.** Variants of §6.14's card with `data-state="misfiled" |
  "empty" | "missing"`: standard tab and rule; the misfiled variant
  sits at its 0.4° rest tilt (double the hand card's 0.15° — wrongness
  is more visible than handwriting) with the note typed in
  `--ink-soft` at the card's foot and a `--tab-red` typed stamp
  "MISFILED" at −6° (sharing §6.16's stamp language). The 404 variant
  adds the three nearest real drawer fronts (§6.13) as its actions.
- **Motion spec.** Arrival: deals in like any card (§6.14) but lands
  with a 120ms hesitation at 90% travel — the card almost doesn't fit
  its slot — then settles at its tilt. The stamp lands at +260ms
  (§6.16's stamp beat). No loops.
- **States.** *Rest:* present, tilted, stamped. *Hover/focus:* §6.7
  applies but the card straightens only to 0.2° (it never fully
  straightens — it is misfiled; straightening it would be filing it).
  *Active:* the card itself is inert; its actions are its links/fronts.
- **Content-merge.** The misfiled card in a *content* drawer (§4) is a
  real card with real content, filed wrong on purpose by the editors.
  The *state* variants carry real state information (what was sought,
  where it might live). Neither is decorative.
- **Failure fallback.** These cards are the fallback — they must
  render with zero JS, server-side wherever possible (404 always).
- **Reduced-motion variant.** Card appears in place, stamp printed.
- **Performance budget.** Negligible. **Mobile variant:** tilt holds
  (identity), stamp −4°.
- **Choreography timeline (arrival, t=0).** 0–340: deal (380ms §6.14
  deal with the hesitation inserted at 300–420: travel pauses at 90%
  for 120ms). 420: lands at 0.4°. 680: stamp lands (180ms `snap`).
  860: at rest. The hesitation is the whole performance — nothing else
  moves.
- **State matrix.**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Tilted 0.4°, stamped | Same |
  | Hover | §6.7 lift, straighten to 0.2° max | n/a |
  | Focus | Lift + ring; straighten to 0.2° | Same |
  | Active | Links/fronts only | Same |
  | Scrolled-past | Remains as filed | Same |
  | Disabled | n/a | n/a |

- **Breakpoint behaviour.** Identical at all sizes.
- **Edge cases.** *A drawer that is genuinely empty in production:*
  the empty card renders, and the drawer's tab in §6.13 shows the
  empty-holder treatment — the two must agree. *Search with zero
  results in a drawer the user filtered to:* the empty card names the
  filters ("No cards in RECIPES match 'truffle'") and offers the
  unfiltered drawer — the correction is one click, on the card.
  *Repeated 404s from a broken external link:* the card is static
  content; nothing escalates.
- **Accessibility spec.** State cards carry real headings ("Not in
  this catalogue", "This drawer is empty") — never just an
  illustration of a card. The stamp is `aria-hidden` (its information
  is in the filing line's text). Tilt never reduces text contrast or
  clips text at any size (card padding absorbs the rotation: 0.4°
  across 360px ≈ 2.5px corner travel, inside the 32px padding).
- **Tokens consumed.** `--card-stock`, `--typed-ink`, `--ink-soft`,
  `--tab-red`, `--rule-red`, `--ease-settle`, `--ease-snap`,
  `--misfiled-tilt: 0.4deg`, `--stamp-angle: -6deg`.

## 7. Page application map

- **Home.** Hero drawer (§6.1) over the cabinet; a riffle scene (§6.3)
  for the featured drawer; shelf scenes of §6.14 cards for the newest
  filings; the stats card (§6.9) dealt as the last card of the second
  shelf; the base drawer (§6.17). The home page's job is to prove the
  catalogue is real, browsable and inhabited — in that order.
- **Listing / drawer page.** The drawer IS the page: its riffle (§6.3)
  opens, §6.2 flips carry the drawer's chapter cards, §6.14 grids hold
  its entries, §6.15 tabs switch drawers without leaving the cabinet.
  Pagination is "next handful" (§6.15), never numbered pages — drawers
  don't have page numbers, they have depth.
- **Detail / entry page.** The entry is one card in reading position,
  full size, with its drawer's stack visible behind it (the previous
  and next entries as filed edges — prev/next navigation is flipping,
  §6.2). Related entries are a dealt handful (§6.14) labelled
  "FILED NEARBY" — adjacency in the drawer, which is the catalogue's
  honest recommendation engine.
- **About / the house.** The keeping of the catalogue, told on cards:
  the house's history as a drawer of dated cards; the keepers as
  handwritten-adjacent content (the about drawer's hand card is the
  keeper's note — the one place the hand card's content is a person
  speaking). Stats (§6.9) recur here as the house's ledger.
- **Contact / request / signup.** §6.16's filing form in the REQUESTS
  drawer. Checkout-shaped flows (payment, booking) do NOT wear the
  theme: hand off to the processor's plain pages from the form's
  confirmation, per §1 — the catalogue files the request; it does not
  pretend to be a bank.
- **Search results.** §6.15's shelf: filing line, dealt cards,
  cross-drawer results with honest filing lines (§6.15's misfiled
  handling).
- **404 / empty / error.** §6.18, always a card, always with the
  nearest real drawers as the way forward.

## 8. Worked examples (v2: three, end-to-end)

### 8.1 The hero — a recipe archive's front drawer

*Setting.* "The Winter Kitchen", a recipe archive: 1,284 recipes in 9
drawers. Home page hero drawer labelled "COOKERY — WINTER".

*Build.* Cabinet fixed behind (§4); hero scene 100vh pinned. Drawer
front: oak, brass holder, Franklin label "COOKERY — WINTER". Deck of
5 cards: (1) H1 card — title "The Winter Kitchen", body: two typed
lines ("Recipes for the cold months, filed by the cooks who kept
them."), filing line "CATALOGUE № 1 · EST. 2016"; (2) intro card —
what the archive is, 96 words; (3) a recipe card (the drawer's
showcase entry, §6.14 at reading size — "Brown Bread, Baked in a
Dutch Oven", with pasted photo); (4) the handwritten card — the
founder's note on why winter recipes matter (84 words, Caveat);
(5) the stats card (§6.9). Primary action "Browse the drawers" is a
chrome button on the drawer front (§11) — it scrolls to the riffle
scene, it does not navigate away.

*Scroll timeline.* Load: §6.1's timeline runs (0–1,520ms), hand card
popping last at 200–720ms within the fan. Scroll 0–100vh (scene pin):
the drawer stays; the deck's cards 2–5 flip past per §6.2 as their
chapter marks cross (the hero drawer is a shallow drawer — its flips
are the intro). At 100vh the scene unpins; the §6.4 tab has travelled
the hero drawer's rail segment; the counter reads "CARDS SEEN: 05 /
1284" (the counter is catalogue-global; the range line reads the
current drawer). The riffle scene of the featured drawer (PRESERVES)
begins.

### 8.2 Mid-page section — the PRESERVES riffle and its chapter cards

*Setting.* Same page, featured drawer: PRESERVES, 64 cards.

*Build.* §6.3 riffle scene, 150vh track, 14 virtualised edges + the
"+ 50 more filed" edge (64 cards > 14: edges 1–13 are the drawer's
first 13 cards, edge 14 is the range edge labelled "MARMALADE —
QUINCE · + 50 MORE"). Below the scene, the drawer's chapter cards in
§6.2 deck form: "On Sugar", "On Jars", "On Sealing", then §6.14
grids of the preserve entries in handfuls of 12.

*Scroll timeline.* 0–8% of track: edge 1 ("Apple Butter — Filed
October") raised; §6.4 label switches to "BROWSING — PRESERVES".
8–88%: edges pass at 26px each; tab travels in sync. A visitor who
clicks edge 7 ("Quince Jelly") at 40% is scrolled natively to that
card's grid position, dealt and snapped (§6.8). 88–96%: the range
edge holds. 96–100%: deck resolves; "On Sugar" flips in (§6.2
timeline: flip 0–510ms of scroll-driven time, its rule drawing at
480–830). Chapters flip at their boundaries; the "On Jars" chapter
contains the drawer's handwritten card (a 1974 note on sterilising,
popping per §6.6 as the chapter opens) and its misfiled card (a
chutney filed among the jams, note attached). Counters: each landing
increments §6.4.

### 8.3 Conversion section — the REQUESTS drawer (subscribe slip)

*Setting.* The archive's subscribe flow: a monthly letter, "The
Filing", sent to readers.

*Build.* A drawer scene labelled "REQUESTS — THE FILING". One card in
reading position: §6.16's form card. Fields: NAME (typed line),
EMAIL (typed line), and a subject choice rendered as three card tabs
(ALL DRAWERS / COOKERY / PRESERVES — §6.15 tab pattern, one pressed).
Submit: "FILE THIS REQUEST". The drawer's hand card sits behind the
form card in the stack — the editor's note ("I read every request
myself. — E.M.") visible as the stack's top edge, revealed fully if
the visitor flips back after filing.

*Scroll timeline.* Arrival via §6.11 from the footer link "The
Filing": shut 0–400, hold, open 480–1,280, form card in reading
position at landing (no fan — a desk is already open when you reach
it; the fan is for drawers, the request desk is furniture in use).
Focus NAME at 1,280 (focus moves to the form's first field on
form-drawer arrival — the one place this theme auto-focuses, because
the visitor's stated intent was the form). Field focus draws the red
rule (240ms). Submit: §6.16 timeline — stamp at success, file-away
at +1,200, confirmation card ("Your request is filed under REQUESTS
— № 118. The next Filing leaves on the first Sunday.") in reading
position at +1,620, focus to its heading. The §6.4 counter does not
increment for the form card (it is a desk, not a card seen — the
counter counts reading, and the label's honesty is the brand).

## 9. Anti-slop — what makes THIS theme look cheap, and the cure

1. **Cards as generic rounded rectangles with drop shadows.** The
   single most likely failure: a builder makes "cards" that are just
   divs. *Cure:* the card unit is non-negotiable — tab, filing line,
   drawn red rule (§6.5), 5:3 proportion in listings, stock texture
   via the shade edge. A card missing its rule or its filing line is
   not a card in this theme.
2. **Typewriter font as costume.** Special Elite pasted over a normal
   marketing layout (centred hero, feature grid, logo cloud). *Cure:*
   the layout laws of §4 — if the underlying layout could wear any
   other theme unchanged, the build is a costume, whatever font it
   wears. Layout first, faces second.
3. **Too many handwritten cards.** Caveat everywhere because it
   "feels personal". *Cure:* the ration is one per drawer, enforced
   by content lint (§10); the second handwritten card halves the
   first one's meaning.
4. **Counters counting from zero, or to invented numbers.** *Cure:*
   §6.9 — from 70%, to the catalogue's real totals, same numbers in
   the footer (§6.17).
5. **Flips that hide content.** A flip implementation where an
   unflipped or mid-flip card is unreadable, or where content exists
   only after its animation. *Cure:* §5's global safety — static
   render is final; the deal-out timer; legibility at every angle.
6. **Wood texture stock photos.** A photographic oak background makes
   the cabinet a pub menu. *Cure:* oak is flat colour + geometry
   (fronts, holders, shade edges) — the cabinet is drawn, never
   photographed. Same for paper: stock is a colour and a shade edge,
   not a scanned-paper image.
7. **Red creep.** Tab red leaking into body links, buttons, headings
   until the page shouts. *Cure:* §2's 3% ration, audited by
   screenshot: red appears at tabs, rules, focus, stamps, errors —
   and nowhere else.
8. **Serendipity spam.** Random "you might also like" rails wearing
   card clothes. *Cure:* adjacency only (§7 detail page) — "FILED
   NEARBY" is a drawer fact; algorithmic rails are banned.
9. **The drawer that contains nothing.** Nav fronts or hero drawers
   whose contents are decorative cards ("Welcome!", stock photos).
   *Cure:* furniture must label real contents (§1); the hero drawer
   holds the page's actual headline and first content (§6.1).
10. **Sound effects.** Paper-rustle audio on flips. *Cure:* banned
    outright — the reading room is silent; the theme's fiction is a
    place people are trying to read.

## 10. Quality gate — minimum bar before this theme may be used in a build

No partial credit on items marked ◆.

- ◆ Static render (JS off) shows every card fully, in order, readable;
  the 1,200ms deal-out timer is implemented and tested by killing the
  rAF loop mid-flip.
- ◆ Every card carries tab, filing line and ruled line; the rule draws
  on first arrival only (§6.5).
- ◆ Per drawer: exactly ≤1 `data-handwritten` card and ≤1
  `data-misfiled` card (content lint output attached to the build).
- ◆ Red ration: a full-page screenshot audit shows `--tab-red` (and
  derivatives) at ≤5% of pixels, in the sanctioned places only (§9.7).
- ◆ Counters (§6.9), footer totals (§6.17) and §6.4's label derive
  from one data source; a test changes the catalogue size and all
  three move together.
- ◆ The flip (§6.2) is reversible at every boundary and never locks
  or hijacks scroll; fast-scroll queue-collapse is demonstrated.
- ◆ Focus is never inside a card that files (§6.2 focus rule); the
  polite status line announces chapter landings.
- ◆ Reduced-motion build reviewed side-by-side: stacked list, no
  pinning, no scrub, no shimmer — and still unmistakably this theme
  (cards, rules, tabs, furniture all present).
- Motion: one shared rAF loop; ≤2 cards animating per flip; no
  standing `will-change`.
- The riffle (§6.3) is absent for drawers of <4 cards and virtualised
  beyond 14 edges, with honest range edges.
- Type split (§3) audited: no Franklin on a card face, no Special
  Elite on a drawer front, no synthetic bold anywhere.
- Performance: §14's budget met on a mid-tier Android over throttled
  4G; CLS = 0 on deal-in and search re-deal.
- The misfiled card is findable via search under its correct subject
  (§6.15 test).

## 11. Component inventory (v2) — every component, themed

Chrome components are Libre Franklin on oak/brass; card components are
Special Elite on stock. The split (§3) governs every row.

| Component | Themed treatment |
|---|---|
| Primary button | Chrome: oak-deep ground, stock text, brass 1px edge; hover = holder-glint sweep across its top edge (200ms); press = 2px lower, 90ms `snap`. Label is a verb of the desk ("FILE THIS REQUEST", "PULL DRAWER") |
| Secondary button | Chrome outline on oak (stock 1px border, transparent ground); hover fills `--oak-pale` at 30% |
| Text link (on card) | Typed underscore: a 1px ink underline that draws to `--tab-red` on hover (240ms, §6.5's draw at link scale); visited links' underlines rest in `--ink-soft` (the pencil of a previous reader) |
| Text input | §6.16 typed line: transparent, ink-soft bottom rule, red rule draws on focus; Franklin label above |
| Select / dropdown | A small drawer: the closed field is a mini drawer front; opening slides a card list down (`drawer` 300ms) whose options are typed lines; the chosen option files into the field |
| Checkbox / radio | A typed box `[ ]` / `[×]` in Special Elite — the mark is a typed ×, appearing with a 120ms strike (opacity steps, §6.4's digit strike); Franklin label beside |
| Toggle | A subject tab (§6.15) sliding in/out of its slot — toggles in this theme are always *filing choices*, labelled as such; a bare on/off switch is off-world and banned |
| Tabs | §6.15 subject tabs (card tabs) — the theme's native tab; no other tab style exists |
| Accordion | A card that pulls 18px forward and unfolds its lower half (rotateX on the fold line at the rule, 320ms `settle`); the accordion header is the card's tab strip (§6.8 button pattern) |
| Modal / dialog | A card pulled fully out and laid on the cabinet top: overlay is `--oak-deep` at 72%, the dialog is a reading-position card, its close is "FILE BACK" (a chrome button). Focus trapped per §6.11's inert pattern; Esc files it back with a §6.2 flip |
| Toast | A small card dealt onto the foot of the current drawer (bottom-left of the column), typed line + optional action; auto-files after 6s with a flip; never more than 2 stacked (a desk with 5 loose slips is a mess — the third waits) |
| Alert / banner | A correction card (§6.18 pattern, red rule doubled) dealt at the top of the relevant drawer — page-level alerts are cards in the deck, never bars across the cabinet |
| Badge / tag | The subject tab in miniature: stock ground, red top edge, typed subject at 12px. Counts inside badges are banned (a badge is a subject, not a metric) |
| Table | A ledger card: the table is typed on a wide card — header row Franklin small caps is *wrong* (Franklin never touches a card); header is Special Elite underlined by the drawn rule; row lines are hairline `--card-shade` rules; numeric columns right-aligned, tabular |
| Pagination | "NEXT HANDFUL →" as a chrome button + a filing line "CARDS 1–12 OF 64" (§6.15). Numbered page links do not exist in a drawer |
| Breadcrumbs | The filing path typed as a filing line: "CATALOGUE › COOKERY › PRESERVES › QUINCE JELLY" in ink-soft, each segment a link — it sits where a filing line sits, because it is one |
| Progress bar | Only §6.4 (tab + label). A horizontal bar anywhere is a foreign object |
| Skeleton | §6.12 blank cards only. Grey pulsing rectangles are banned |
| Tooltip | A tiny typed card (stock, rule, one typed line ≤ 12 words) appearing above the element after 600ms hover, `settle` 160ms; on focus it appears immediately. Tooltips explain furniture ("This tab marks your place in the drawer"), never content |
| Avatar / byline | A keeper's line, typed: "Filed by E.M." — no avatar circles in a catalogue; people are initials and dates |
| Divider | The drawn rule (§6.5) at section scale, or a drawer edge (oak strip with a brass holder, used between shelf scenes). A bare `<hr>` styled grey is banned |
| Search input | §6.15's request slip |
| Empty state | §6.18 |
| Error state | §6.16 corrections / §6.18 error card |
| Price / data figure | Typed like everything on a card; large figures use §6.9's counter face at rest. Prices never wear red (red is rationed; a red price is a sale poster) |

## 12. Content & copywriting voice (v2)

The catalogue speaks like a good clerk: brief, exact, dry, kind. Two
voices only — the **typed voice** (Special Elite, on cards) and the
**chrome voice** (Franklin, on furniture) — and they never swap jobs.

- **Headlines (card titles)** are index entries, not slogans: noun-first,
  specific, filed alphabetically by their first significant word.
  ✓ "Quince Jelly, Sealed with Wax" · ✗ "You Won't Believe This
  Jelly!" · ✗ "Welcome to Our Wonderful Archive".
- **Filing lines** follow the pattern `№ · DATE · DRAWER` and are
  never abbreviated into meaninglessness: "№ 214 · FILED OCT 1974 ·
  PRESERVES". Dates are real; "recently" is banned.
- **Labels (chrome)** are ranges and imperatives: "COOKERY — WINTER",
  "PULL DRAWER", "FILE THIS REQUEST". Sentence case never appears on
  chrome; chrome is stamped, not written.
- **Buttons** are desk verbs (§11). "Submit", "Click here", "Learn
  more" are banned — the desk files, pulls, opens, shelves.
- **Error voice** is a clerk's correction, written on the slip, never
  an accusation and never a joke: ✓ "This line wants an email address
  — the kind with an @ in it." · ✓ "Nothing was filed. The drawer
  jammed; your slip is still filled in. Try the filing again."
  ✗ "Oops! Something went wrong!!" · ✗ "Invalid input."
- **Empty-state voice** states the filing fact and the way forward:
  ✓ "This drawer is empty. Its cards are being typed." · ✓ "Not in
  this catalogue. The nearest drawers are COOKERY and PRESERVES."
- **The handwritten voice** (the one hand card) is a person, allowed
  warmth the typed voice is not: "I read every request myself, usually
  on Sunday. — E.M." One per drawer (§4); it never sells.
- **Numbers** are exact and sourced from the catalogue (§6.9):
  "1,284 cards", never "1,000s of cards!!".
- **The misfiled note** is fixed in form: "Misfiled since [year]. It
  lives here now." The year is part of the fiction's history and is
  set by the editors, once.

## 13. Full-page scroll choreography map (v2)

The home page, top to footer, in order. (Drawer pages substitute §8.2's
riffle block for beats 3–5 per drawer.)

| # | Beat | What the visitor sees & feels |
|---|---|---|
| 1 | Load | §6.1: the hero drawer glides open (80–880ms), cards fan, the founder's hand card pops last. The room opens |
| 2 | First scroll | Hero cards flip past (§6.2) as the scene's 100vh plays out; §6.4's tab starts its travel; counter at 05 |
| 3 | Featured drawer | §6.3 riffle: the thumb browses PRESERVES — edges flicking at the visitor's own speed; the label admits "BROWSING" |
| 4 | Resolution | The riffle lands; "On Sugar" flips in, its rule draws as it lands (§6.2/§6.5 overlap) |
| 5 | Chapters | Flips at each chapter boundary; the hand card pops inside "On Jars"; the misfiled chutney sits crooked among the jams |
| 6 | Rest | A shelf scene (unnpinned): newest filings deal in, 60ms ripple (§6.14) — the thumb rests |
| 7 | Stats | The stats card deals; totals type up from 70% (§6.9) — the catalogue states its extent |
| 8 | Second drawer | §6.11 in miniature: a drawer-front strip shuts/opens as the page's second drawer scene begins (page-internal, no route change — the front at the scene's head performs the same shut/open at 60% scale) |
| 9 | Ambient | Throughout quiet stretches, §6.10's shimmer crosses the open drawer's edges every ~9s — the room is inhabited |
| 10 | Requests | The REQUESTS drawer front (a shelf-scene card-front) invites the form (§8.3 lives on its own route; from home it is §6.11 away) |
| 11 | Footer | §6.17: the base drawer, holder glinting once; totals at rest; the typed strip closes the catalogue |

Feeling arc: *arrival* (the drawer opens for you) → *browsing* (your
thumb, your speed) → *reading* (flips you cause) → *rest* (dealt
shelves) → *trust* (real totals, a kept catalogue) → *the desk* (a
request, filed). Any build whose page cannot be mapped onto these
beats has added a scene the theme doesn't have.

## 14. Whole-page performance budget (v2)

- **Assets.** Fonts: Special Elite (1 weight), Libre Franklin (600/700
  only), Caveat (1 weight) — subsetted, `font-display: swap`, total
  ≤ 90KB woff2. Images: pasted photos only, AVIF/WebP, ≤ 60KB each at
  listing size, lazy below the first shelf. Zero icon fonts, zero
  stock-texture images (§9.6). Total initial payload target ≤ 450KB.
- **Animation frame budget.** One shared rAF loop; per frame ≤ 4ms of
  JS on a mid-tier Android; animated properties are transform/opacity
  (+ the single capped 1.2px blur on one flipping card, desktop only).
  Standing `will-change`: none. Concurrent animations: ≤ 2 flips +
  ≤ 6 deals + 1 shimmer layer, hard caps enforced by the arrival
  queues (§6.3/§6.14).
- **Long tasks.** No task > 50ms during scroll; the riffle's edge
  virtualisation is computed once per drawer, not per frame.
- **CLS.** 0 by construction: blanks reserve card boxes (§6.12),
  photo borders reserve image boxes (§6.14), the folio-style counters
  are fixed-width.
- **Cut order when the budget is exceeded.** (1) §6.10 shimmer
  period stretches, then the loop is cut. (2) Focus-settle blur goes.
  (3) Parallax travel halves, then goes. (4) Deal stagger compresses
  to 30ms. Never cut: flip legibility, the deal-out timer, reduced-
  motion behaviour, or any content. Motion is spent before meaning,
  always.

## 15. Build-order checklist (v2)

1. Tokens (§2/§3) and the card unit (§4, §6.14 geometry) — nothing
   else exists until a card can sit still and be a card.
2. Static deck: all cards in normal flow, fully readable, JS off.
   (This is the fallback; building it first makes §5's safety free.)
3. Cabinet + navigation (§6.13) and footer (§6.17) — the room.
4. The shared rAF loop + deal-out timer (§5) — the machinery, before
   any single effect.
5. §6.5 rule draw + §6.14 deal-in (the heartbeat and the shelf).
6. §6.2 flips + §6.4 tab/label (the reading mechanic + its furniture,
   together — the counter must count real flips).
7. §6.1 hero drawer (the fan reuses §6.2/§6.5 machinery).
8. §6.3 riffle scenes (after flips exist for the resolution to land
   in).
9. §6.7/§6.8 handling (hover, snap) and §6.9 counters.
10. §6.15 search/tabs, §6.16 form, §6.18 state cards, §6.12 blanks.
11. §6.11 route transitions (last of the motion — it wraps everything
    else).
12. §6.10 shimmer (the ambience is built last and cut first, §14).
13. Reduced-motion pass over every element; lamplight variant (§2);
    print stylesheet (deck flattened, §6.2).
14. §10 gate, run in full, evidence recorded.
