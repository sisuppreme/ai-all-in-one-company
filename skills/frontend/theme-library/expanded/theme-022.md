# 22. Dust Jacket — Expanded (v1 + v2)

*Expansion written to `EXPANSION-STANDARD.md` v1 + the v2 deepening pass
(50x standard), ordered 2026-11-23. This file is the complete, buildable
specification of theme #22. The original library entry's identity is
preserved exactly — the two-act structure, the jacket that comes off at
the midpoint, the four palette anchors, Playfair Display + Lora — and
deepened, never redesigned. Where this file and the short library entry
disagree, this file governs.*

**The one law of the theme, stated before everything else:** there is
only ever one book. The jacket is not a theme laid over the site and the
cloth is not a second site underneath it — the jacket is *this book's*
jacket, printed with this book's title, this author's photograph, this
edition's price, and the cloth beneath is *this book's* binding, opening
at *this book's* first chapter. A jacket that could wrap any book, or a
cloth act that could be any site's dark section, is a costume. Every
element below traces to the specific book the page is selling, launching
or celebrating; the moment an element would work unchanged for a
different book, it has failed.

---

## 1. Concept & world

A hardback book lives two lives. The first is loud and perishable: the
dust jacket — glossy, blurbed, priced, barcoded, printed to be handled
in a shop for ninety seconds and judged. The second is quiet and
permanent: the cloth binding underneath, gilt on the page edges, built
to be kept for decades after the jacket is torn, lost or thrown away.
Every reader knows the small ceremony of sliding the jacket off a new
book to see what colour the boards are. Dust Jacket builds a website
out of that ceremony. **The site wears its dust jacket for the first
half of the page, and takes it off at the midpoint.** Act one sells.
Act two is the thing itself.

The world is the physical book as an object with anatomy: front cover,
spine, back cover, front flap, back flap, endpapers, boards, cloth,
gilt edges, colophon. The page borrows that anatomy as its layout
vocabulary — not as illustration, but as structure. The front flap is
where the price lives because that is where prices live. The spine pins
at the left edge because that is where a held book's spine stays. The
back cover carries the praise because praise is printed on back covers.
Nothing on the page is *shaped like* a book part for charm; each part
does the job its real counterpart does.

**Mood.** Act one: bright, confident, faintly salesy — the register of
a great jacket, which is allowed to boast because boasting is its job.
Act two: hushed, woven, unhurried — the register of a reading room. The
emotional arc of the page is the arc of buying a book and taking it
home: the noise of the shop falls away at the midpoint, and what is
left is the object and the text. The midpoint is not a section break;
it is the page's plot turn, and the copy knows it — the last line of
the jacket act and the first line of the cloth act are written as a
pair (§12).

**Why the slide-off works (the physical ground).** Removing a jacket is
a real gesture with a real direction: the jacket slides *along* the
book, sideways, off the fore-edge, while the book stays exactly where
it was. The theme honours that physics literally — the jacket layer
translates −105% on X over 900ms and the cloth beneath does not move a
single pixel during the set piece (§6.1). The cloth site is fully built
and fully laid out from the first paint, *under* the jacket; the
visitor is never waiting for act two to load, because act two was
always there, the way the boards were always under the paper. This is
also why the fallback matters more here than in any other theme: a
visitor who never triggers the slide-off must still be able to reach
the book — by button, by anchor, by keyboard — because a book you
cannot open is not a book (§6.1 edge cases).

**Best-fit sites and audiences.**

- Authors and book launches: one book, one page, the page *is* the
  book's own packaging — the strongest possible claim a launch page can
  make.
- Publishing houses and imprints presenting a lead title or a season's
  flagship, where the house's colophon and print-run data are real
  content, not decoration.
- Literary festivals and reading series built around a single featured
  work or a small, curated list treated as editions.
- Reissues, anniversary editions and facsimiles, where the contrast
  between the new jacket and the classic cloth beneath is literally the
  product story.
- Bookbinders, fine-press printers and booksellers of collectible
  editions, whose customers already perform the jacket-removal gesture
  and will recognise it instantly.

**When NOT to use it.**

- Catalogues of many books. The theme spends half a page on one book's
  jacket; a grid of forty titles each demanding a slide-off is forty
  interruptions. (A catalogue may use the *cloth act alone* as a quiet
  listing skin — but that is a different, lesser build and must not
  pretend to the full theme.)
- E-book and audiobook products with no physical edition. The theme's
  every gesture cites paper, cloth and gilt; applied to a file download
  it becomes a lie about the product.
- News, blogs and anything updated daily. Jackets are printed once, for
  an edition; a surface that changes hourly breaks the metaphor and the
  print-run counters (§6.11) become fiction.
- Sites that need their conversion in the first viewport. Act one is a
  cover: it shows the title, the author, one line of praise. The price
  is on the flap, one click in — exactly as on a real book, and just as
  deliberately.

---

## 2. Palette

Four anchors, inherited from the original entry, plus derived tokens
that exist to keep the anchors honest at text sizes and in the dark.

| Token | Hex | Role | Ratio | Pairing & contrast |
|---|---|---|---|---|
| `--jacket` | `#F4EFE3` | Jacket cream; the jacket act's ground, cover and flap surfaces | ≈46% of the page (all of act one) | Ground for `--ink` text (13.1:1) and `--red` (5.2:1) |
| `--red` | `#B3372C` | Publisher's red; jacket display accents, the spine's band, price, stamps, act-one links | ≈5% | On `--jacket` 5.2:1 — display and large text freely; body text uses `--red-deep` |
| `--cloth` | `#274435` | Cloth green; the binding — act two's ground, boards, chapter sections | ≈44% of the page (all of act two) | `--jacket`-cream text on it 9.3:1; gilt on it 4.4:1 |
| `--gilt` | `#C9A227` | Gilt; page edges, cloth-act display titles, the colophon line, foil details | ≈3% | On `--cloth` 4.4:1 — display sizes only (≥24px); on `--jacket` 2.1:1, so gilt never carries text on the jacket |
| `--ink` | `#2A2620` | Derived: the book's text ink; body copy in both acts | within both acts | On `--jacket` 13.1:1; on `--cloth` it is never used (act two sets text in `--paper-text`) |
| `--paper-text` | `#EFE7D2` | Derived: warm paper-white; act two's body text on cloth | within the 44% | On `--cloth` 8.7:1 |
| `--red-deep` | `#9A2B22` | Derived: the red taken one register down for small text on cream | within the 5% | On `--jacket` 6.7:1 — links, captions, error text in act one |
| `--gilt-bright` | `#D9B84A` | Derived: gilt under light; the page-edge strip at full brighten (§6.8), cloth-act hover gilt | within the 3% | On `--cloth` 5.6:1; on the dark ground 7.4:1 |
| `--cloth-deep` | `#1C2E24` | Derived: the boards in shadow; act-two section troughs, footer ground, dark-scheme ground | — | `--paper-text` on it 12.5:1; `--gilt-bright` on it 7.4:1 |
| `--flap-shade` | `#E7DFCB` | Derived: the flap's underside and the back cover's slightly handled tone | — | One step behind `--jacket`; carries `--ink` at 11.4:1 |
| `--gloss` | `rgba(255,255,255,.55)` | The laminate sheen gradient stop (§6.2, §6.7) | — | Only ever a moving gradient over the jacket; never a surface colour; does not exist in act two |
| `--weave` | `rgba(244,239,227,.05)` | The cloth weave's light thread (§4) | — | A repeating 3px texture over `--cloth`; texture, not colour |

**Usage discipline.** The two acts keep separate books. Red belongs to
the jacket: it appears in act two exactly once, as the bookmark
ribbon's tail (§6.8), because a ribbon is the one piece of the
*purchase* that stays inside the book. Gilt belongs to the cloth: on
the jacket it may appear only as the foil-stamped title treatment on
the front cover (§6.14), printed-foil style, never as a UI colour. Any
red button in act two or gilt link in act one means the two designs
have leaked into each other — §9 failure. Combined gilt above 5% of any
viewport is gilding, not gilt.

**Dark-mode behaviour.** There is no inverted jacket. Under
`prefers-color-scheme: dark`, act one stays exactly as printed — a
jacket does not change colour because the room darkened — but it is
presented *on* `--cloth-deep`, the shelf it sits on: the page surround
darkens, the jacket sheet itself keeps `--jacket`. Act two deepens:
grounds drop from `--cloth` to `--cloth-deep`, text stays
`--paper-text`, gilt shifts to `--gilt-bright` (7.4:1 on the deep
ground) — lamplight on a binding. The gloss (§6.7) dims to
`rgba(255,255,255,.32)`: gloss in a dark room is a suggestion, not a
shine. A build that inverts the jacket to black has misunderstood the
object; the gate (§10) checks the jacket sheet's computed colour in
both schemes.

---

## 3. Typography

Two faces, inherited: **Playfair Display** sells, **Lora** reads. The
typographic voice changes with the surface — that change is the theme's
type law, stated once here and enforced everywhere: **on the jacket,
Playfair Display sets anything the size of a claim; on the cloth, Lora
sets everything, and Playfair survives only as the gilt chapter
numerals' companion in drop-cap initials (§6.14 note, §11).** A page
where the cloth act is still shouting in Playfair has not taken its
jacket off.

| Role | Face | Size / line-height | Tracking | Where |
|---|---|---|---|---|
| Cover title | Playfair Display 800 | clamp(56px, 9vw, 118px) / 0.98 | −0.01em | Front cover only (§6.14); once per page |
| Jacket display | Playfair Display 700 | clamp(34px, 4.6vw, 54px) / 1.05 | −0.005em | Act-one section heads, the spine title at 20px rotated |
| Blurb quote | Playfair Display italic 500 | 21–26px / 1.35 | 0 | Back-cover praise (§6.4, §6.15) |
| Jacket body / flap copy | Lora 400 | 17px / 1.55 | 0 | Flap copy, cover standfirst, act-one body |
| Price & edition data | Lora 600 | 15px / 1.4, tabular figures | 0.01em | The flap's price block (§6.6), counters (§6.11) |
| Cloth chapter head | Lora 600 | clamp(28px, 3.4vw, 40px) / 1.15 | 0 | Act-two section heads, gilt when display (§2 rules) |
| Cloth body | Lora 400 | 18px / 1.7 | 0 | Act-two reading text — the book's own measure |
| Drop cap | Playfair Display 700 | 3.4em, gilt | — | Chapter openings only; one per chapter, never per section |
| Caption / colophon | Lora 400 italic | 13.5px / 1.5 | 0.01em | Photo credits, the colophon (§6.17), barcode caption |
| Data strip (barcode, ISBN) | Lora 600 | 12px / 1.3, tabular | 0.08em, uppercase | The flap's barcode block (§6.6) |

**Per-role rules.**

- **Display.** The cover title is set once, at cover size, and never
  repeated at display size anywhere else on the page — a book has one
  front cover. Act-one section heads are a full register smaller; if a
  section head competes with the cover title, the cover loses and the
  theme fails (§9).
- **The spine title** is set vertically (writing-mode:
  vertical-rl), Playfair 700 at 20px, reading bottom-to-top as on a
  shelved book in the British convention, with the publisher's device
  (§6.10) at its foot. It is real text, never an image — screen readers
  meet the book's title on its spine (§6.3 accessibility).
- **Body.** Act one's measure is 62ch; act two's is 58ch and its
  line-height opens to 1.7 — the cloth act is *read*, and its text
  block is set like a book page, justified never, hyphenation on at
  <768px only.
- **Data.** Print-run, edition and price figures always tabular, always
  in Lora 600, always labelled in words ("Second printing", "Edition
  of 1,500") — a bare numeral on a flap is a price tag, and this theme
  is not a shop (§12).
- **Gilt text** is display-only: chapter heads and the colophon line,
  ≥24px, on `--cloth` or `--cloth-deep`. Gilt body text is the single
  most common way this theme goes cheap (§9) and the gate measures it.

---

## 4. Layout language

**The sheet and the book.** Act one is laid out as one physical jacket
unfolded flat, in the order a bookseller handles it: front flap →
front cover → spine → back cover → back flap, mapped onto a vertical
page as: the cover block (full-viewport), the spine pinned at the left
edge throughout, the praise spread, then the flap block. The visitor
scrolls *around* the book. Act two is laid out as the book open: a
centred reading column (max 58ch) flanked by margin space that holds
the gilt page-edge strip at the right viewport edge (§6.8) and chapter
 furniture — numerals, running heads — in the margins, the way a
typeset page carries its furniture outside the text block.

**Grid.** 12 columns, 24px gutters, content max-width 1240px in act
one (the jacket is a wide object) and 1080px in act two (the book is a
narrower one — the page visibly *narrows its stance* after the
midpoint, one of the quietest signals that the object has changed).
The spine occupies a fixed 56px rail at the left in act one, inside
the grid's first column span, and the content grid is offset by it —
content never slides under the spine.

**Spacing rhythm.** Base unit 8px. Act one breathes in 64px and 96px
section gaps — jacket space, display space. Act two tightens to 56px
and 80px with 1.7 line-height doing the spaciousness work instead:
cloth-act air comes from leading, not from gaps. The midpoint zone
(§6.9) is a full-viewport band with no content column at all — the
gutter of the book, given a whole screen to happen in.

**Density rules.** Act one: one claim per viewport, maximum. A cover,
a praise spread, a flap — each gets its own screen the way each gets
its own panel of card. Act two: density rises to reading density —
full paragraphs, chapter furniture, a contents list (§6.13) — but
never to dashboard density; if a cloth-act section needs a grid of
cards, the cards are set as a *contents page* (§6.15), in type, not in
boxes.

**Texture as material.** Three textures, each rationed: the jacket's
gloss (a gradient, only in motion or under the pointer, §6.7); the
cloth weave (a 3px repeating cross-hatch at 5% paper-white over
`--cloth`, static, always on in act two — matte is its point); the
marbled endpaper (an SVG turbulence pattern, visible only inside the
midpoint zone and on the endpaper leaves of §6.12's transition — the
rarest texture on the page, because endpapers are seen for a moment).

**Placed imperfections.** Exactly two are licensed: the back cover's
`--flap-shade` tone (a handled copy, §2) and one praise quote set 1°
off-axis on the back cover (§6.15), as if the blurb sticker was placed
by hand. Any third imperfection is wear, and wear is damage (§9).

---

## 5. Full motion system

Every motion term, in this theme's own language. Named easings first —
they are the theme's handwriting and no element may invent its own:

| Token | Curve | Character |
|---|---|---|
| `--ease-whisper` | cubic-bezier(.22,.9,.28,1) | Paper sliding on paper: the slide-off, the flap, long and frictionless at the end |
| `--ease-shelf` | cubic-bezier(.2,.7,.3,1) | A book settling onto a shelf: assembly pieces arriving and stopping dead |
| `--ease-press` | cubic-bezier(.16,1,.3,1) | Print contact: quotes and marks landing, quick in, no bounce |
| `--ease-gilt` | linear scrub | The page-edge brightening is scroll itself; no easing may intervene |
| `--ease-leaf` | cubic-bezier(.45,0,.2,1) | A page turning: slow lift, quick settle (act-two transitions) |

Duration tokens: `--dur-stamp` 500ms · `--dur-flap` 500ms ·
`--dur-quote` 450ms · `--dur-slide` 900ms · `--dur-sheen` 1000ms ·
`--dur-draw` 500ms · `--dur-count` 800ms · `--dur-turn` 500ms ·
`--dur-close` 600ms (act-one page transition).

**Scroll-triggered reveals.** Act one reveals are *placements*: quotes
are set down (§6.4), the colophon mark is printed (§6.10) — things are
put on the jacket, not faded up from nothing. Act two reveals are
*readings*: chapter heads and paragraphs arrive with a 12px rise and
opacity over 500ms `--ease-press` as they cross 78% of the viewport —
the eye arriving, not the page performing. Both acts: every reveal has
a 1000ms watchdog (§6.12's law) after which the element is forced to
its final state; the final state is the CSS default, so a reveal can
only ever *delay* content, never withhold it.

**Parallax.** Act one only: front cover, spine and blurbs travel as
separate sheets — cover at 0.92× scroll, praise spread at 1.0×, the
flap block at 1.06× — a ±14px maximum spread, computed in the shared
loop. The layers are the jacket's own panels, so the parallax reads as
paper thickness, not depth-effect. Act two has **no parallax**: a book
being read does not slide against itself. The single permitted
act-two scroll motion is the gilt edge (§6.8), which is a progress
instrument, not a layer effect.

**Pinned scenes.** One pin per act. Act one: the spine (§6.3), pinned
for the act's full length — it is a held book's spine, and pinning is
what "held" means. Act two: no pin except the page-edge strip, which
is `position: fixed` instrumentation rather than a scene. The
midpoint set piece (§6.1) is a triggered transformation, never a pin:
the visitor must be able to scroll *past* a jacket that has already
come off.

**Masked line reveals.** The cover title's standfirst and the cloth
act's chapter epigraphs reveal line-by-line behind overflow masks,
each line rising 100% → 0 over 550ms `--ease-press`, 70ms stagger —
type being uncovered as the sheet is lifted. Masked reveals are
rationed to these two places; body text never masks (a paragraph you
must wait to read is a paragraph withheld).

**Blur-to-sharp.** Used once, deliberately: the author photograph
inside its die-cut (§6.5) resolves from 6px blur as the cover settles —
a face coming into focus on a cover being examined. Nowhere else. The
cloth act is matte and sharp from first paint; blur in act two reads
as a screen effect and breaks the object (§9).

**Animated counters.** The flap's print-run and edition figures
(§6.11), counting once, upward, to the true figures, tabular, 800ms.
Counters exist only where a real book prints numbers: the flap. There
are no counters in act two — books do not count their readers.

**Progress indicators.** Two, one per act, never both visible: act one
uses the spine's gilt band filling downward (§6.3 state) plus the
sheet-parallax as implicit progress; act two uses the gilt page-edge
strip and the descending bookmark ribbon (§6.8). No generic progress
bar exists in this theme (§11 refusals).

**Marquees.** Refused. A jacket does not crawl and a book does not
tickertape. The one horizontal motion licensed is the slide-off
itself. Praise quotes are a printed spread, read in place (§6.4).

**Ambient loops.** Two, one per act, never simultaneous. Act one: the
gloss sheen idles across the jacket every 9s (§6.2). Act two: nothing
loops — the original entry's ruling stands: *the quiet is the
ambience.* The weave is static, the gilt moves only with scroll. An
act-two ambient loop is a §9 failure by definition.

**Micro-interactions.** The flap-unfold click (§6.6), the
press-harder hover vocabulary (§6.7 for the cover; §6.15 for praise
cards), the remove-the-jacket button (§6.1), the contents-list chapter
hover in act two (§6.13: the chapter's page-leaf gilt edge lights).
Every micro-interaction is a book-handling gesture: lift, unfold,
turn, shelve. There are no button ripples in a bookshop.

**Hover physics.** Pointer-follow gloss with 120ms lerp and a ≤3°
cover tilt (§6.7); praise cards lift 3px with a hard offset shadow
(the sticker being touched, §6.15); act-two links take a gilt
underline drawn left-to-right at 220ms. Hover never scales anything
above 1.02 and never rotates anything except the cover and the one
licensed off-axis quote settling straight (§6.15).

**Page transitions.** Dual-mode, the theme's signature systems piece
(§6.12): before the midpoint, a cover close-open (600ms); after it, a
page turn (500ms `--ease-leaf`). The mode is a property of where the
visitor *is in the book*, and the transition announces the act change
when a route crosses the midpoint.

**Image treatments.** Jacket images sit in printed frames with the
die-cut oval reserved for the author (§6.5); cloth-act images are
chapter plates: full-measure, gilt-ruled above and below, caption in
italic Lora beneath, scale-in-frame 1.04 → 1 over 700ms on entry in
both acts. No image is ever rounded, shadowed with a soft UI shadow,
or filtered — print is print.

---

## 6. Signature elements

### 6.1 The jacket slide-off (midpoint set piece)

- **What & why.** The theme's plot turn and its reason to exist. At the
  scroll midpoint, the entire jacket layer — front cover, pinned spine,
  back-cover blurbs, gloss — slides off sideways, `translateX −105%`
  over 900ms on `--ease-whisper`, trailing a faint edge shadow, and
  reveals the cloth-bound book beneath: fully built, already
  mid-chapter, its first chapter head and drop cap waiting. Nothing
  loads, nothing fades in. The book was always there; the visitor has
  simply taken its jacket off, the way every reader eventually does.
- **Structure.** The jacket act is one `<div class="jacket-layer">`
  containing the cover, spine rail, praise spread and flap block,
  positioned over the page's first half; the cloth act is ordinary
  document flow beneath it in the same scroll. The slide is a transform
  on the jacket layer only. A "Remove the jacket" button (§6.13) sits
  in the jacket navigation as the alternate trigger, and a session
  flag records that the jacket is off so in-page navigation never
  re-dresses the book.
- **Motion spec.** Trigger: the midpoint marker (the endpaper zone,
  §6.9) crossing 50% of viewport height, or the button. The layer
  translates 0 → −105% over `--dur-slide` 900ms `--ease-whisper`; its
  edge shadow (a 24px linear gradient at the layer's right edge) fades
  in over the first 200ms and out over the last 300ms. The cloth
  beneath does not move, scale or brighten — 0px, by law. Once off,
  the layer is `visibility: hidden` and removed from the tab order.
- **Choreography timeline (v2).** Midpoint marker crosses 50% →
  +0ms: the endpaper swirl (§6.9) begins in the gutter the jacket is
  about to vacate → +120ms: the jacket layer begins translating; the
  spine (§6.3) travels with it, unpinning in the same frame → +450ms:
  layer at −52%, the cloth chapter head fully exposed, swirl at peak
  → +900ms: layer at −105%, shadow gone → +950ms: layer hidden, focus
  is *not* moved (the visitor's scroll position is untouched), the
  act-two progress instruments (§6.8) fade in over 300ms → total
  visitor time ≈1.25s, during which they may keep scrolling; the
  slide is scroll-independent once triggered and never traps the
  scroll position.
- **State matrix (v2).** *Rest (before midpoint):* jacket on, fully
  interactive. *Hover:* n/a (the layer is not a control; its children
  keep their own hovers). *Focus:* elements inside the jacket remain
  focusable until the slide completes, then are inerted. *Active
  (sliding):* jacket children inert from +0ms so nothing can be
  clicked mid-gesture. *Scrolled-past:* jacket gone; scrolling back
  above the midpoint does **not** re-dress the book — removal is
  one-way, like the real gesture; a "Replace the jacket" text link in
  the colophon (§6.17) is the only way back, and it resets the layer
  without animation. *Disabled (no JS):* the jacket layer is never
  positioned over the cloth; both acts render as a normal stacked
  page, jacket sections first, cloth sections after — the designed
  disabled state, fully readable.
- **Content merge.** The jacket is the site's own cover and its removal
  is the narrative's turn — the surface and the story are the same
  object. The cloth revealed is not a teaser or a landing page; it is
  chapter one, mid-argument. Remove the animation and the page is a
  book presented jacket-then-cloth, poorer in ceremony, never in
  content.
- **Failure fallback.** Three independent guarantees: the button
  trigger; an anchor ("Begin the book") in the jacket navigation that
  jumps past the midpoint, which fires the trigger by scroll position
  alone; and the no-JS stacked layout. If the slide's JS fails
  mid-gesture, a 1200ms watchdog forces the layer to its final state
  (off, hidden) — a jacket may never be left hanging half-off the book.
- **Reduced-motion variant.** No slide. At the midpoint the jacket
  sections are simply *ended* — the page presents jacket and binding
  side by side in the endpaper zone (the original entry's ruling: both
  designs visible, no slide-off), and the cloth act follows in flow.
  The button becomes a plain anchor to the cloth act.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: slide
  distance −108% (the layer is narrower than the viewport's overscan),
  duration 800ms. <768px: the jacket layer is full-bleed; slide −110%
  over 700ms; the edge shadow is dropped (mobile GPUs pay for large
  gradient shadows) and the swirl (§6.9) is halved in opacity.
- **Edge cases & failure modes (v2).** *Fast fling past the midpoint:*
  the trigger fires on position, not on dwell — the slide plays even
  if the visitor is moving fast, and completes behind them; the cloth
  is simply there when they land. *Midpoint reached via find-in-page
  or anchor jump:* same position trigger; if the jump lands deep in
  act two, the slide is skipped entirely (session flag set silently) —
  never play a set piece to an empty room. *Short page (content ends
  before a true midpoint):* the trigger binds to the endpaper zone's
  position, not to 50% of document height — the zone is authored, so
  the turn always exists. *Back-button return with the flag set:*
  jacket stays off; the colophon link offers replacement.
- **Accessibility spec (v2).** The slide is decorative: the cloth
  content is in the accessibility tree from first paint, in document
  order after the jacket content. At slide completion the jacket layer
  gets `aria-hidden` + `inert`. The button is a real `<button>`
  labelled "Remove the jacket" with `aria-controls` pointing at the
  cloth act's first section. No focus movement is forced at any point.
  The midpoint is also a heading boundary: act two opens with its own
  `<h2>` so heading navigation crosses the turn without the animation.
- **Performance budget & mobile variant.** One transform on one layer;
  the layer's will-change is armed 200ms before the expected trigger
  (when the endpaper zone enters the viewport) and released at
  +950ms. No layout is touched. Mobile: the 700ms/−110% variant above;
  layer children keep their own budgets.
- **Tokens consumed (v2).** `--jacket`, `--cloth`, `--ease-whisper`,
  `--dur-slide`, `--weave`, `--cloth-deep`.

### 6.2 Jacket assembly entrance

- **What & why.** The page arrives the way a book is handed to you:
  whole, but perceptibly assembled — front cover first, spine settling
  at the left edge, back-cover blurbs last, and a single gloss sheen
  sweep across the finished cover to say *laminated, new, just
  unwrapped.* It is the only entrance choreography in act one; after
  it, the jacket is a printed object and printed objects do not
  animate in.
- **Structure.** The cover (§6.14), spine (§6.3) and praise spread
  (§6.15) are ordinary sections; JS arms their pre-states (translated
  18px, opacity 0) only after first paint confirms the loop is alive.
  The sheen is a `::after` gradient on the cover block, translated
  across and removed.
- **Motion spec.** Load → cover slides in from +18px X over 600ms
  `--ease-shelf` → spine settles at the left edge (from −56px, 500ms,
  overlapping the cover by 150ms) → blurbs fade in (opacity, 400ms,
  `--ease-press`) → sheen sweep: gradient −20% → 120% across the
  cover over `--dur-sheen` 1000ms, once. Total ≈1.9s. The idle sheen
  then repeats every 9s at 40% opacity (§5 ambient law) until the
  midpoint, and never again after it.
- **Choreography timeline (v2).** Fonts ready or 300ms cap → +0ms
  cover begins → +450ms spine begins (150ms overlap) → +700ms author
  die-cut (§6.5) starts resolving inside the arriving cover → +950ms
  blurbs begin → +1350ms sheen begins → +1900ms (approx.) page at
  rest; all pre-states cleared, transforms removed from the DOM nodes
  so the printed state is literally the un-animated state.
- **State matrix (v2).** *Rest:* assembled jacket, static. *Hover /
  focus / active:* the assembly has no interactive states; children
  keep theirs. *Scrolled-past:* nothing replays on scroll-back — the
  assembly is a load event, not a scroll event; a session flag
  suppresses it on repeat in-session navigations (the §6.12 transition
  replaces it). *Disabled:* no pre-states are armed; the jacket is
  simply there — the designed disabled state.
- **Content merge.** The pieces assembling are the actual jacket
  wrapped around this book; the sheen crosses the actual cover with
  the actual title on it. Nothing decorative is added to make the
  entrance busier.
- **Failure fallback.** The 1000ms watchdog (§6.12): any piece not
  arrived by then is forced to final state in one frame. If
  `fonts.ready` never resolves, the 300ms cap starts the sequence
  anyway — a jacket in a fallback face is still a jacket.
- **Reduced-motion variant.** No assembly, no sheen, no idle loop: the
  jacket is printed and present at first paint.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: travel halves
  (9px), sheen 800ms. <768px: only the cover fades in (400ms); spine
  and blurbs are present statically — a phone screen is a small book
  and small books are not performed at you.
- **Edge cases & failure modes (v2).** *Slow network / late hero
  image:* the sequence is gated on fonts, not images; the die-cut
  photo (§6.5) resolves whenever it arrives, inside its frame, with
  no layout shift (frame is aspect-locked). *Visitor scrolls during
  assembly:* the sequence continues but the sheen is cancelled if the
  cover is <30% visible when the sheen beat arrives — never shine an
  empty room. *Re-entry via back button:* session flag → static
  jacket.
- **Accessibility spec (v2).** All jacket content is in the DOM in
  reading order from first paint; pre-states are visual only
  (`aria-hidden` is never applied to content). The sheen is a gradient
  on a pseudo-element: nothing for a screen reader to meet. Focus is
  never moved by the assembly.
- **Performance budget & mobile variant.** Three transforms + one
  gradient sweep, all compositor-only; loop cost shared with §5's
  single rAF loop. Mobile: the fade-only variant above.
- **Tokens consumed (v2).** `--jacket`, `--gloss`, `--ease-shelf`,
  `--ease-press`, `--dur-sheen`.

### 6.3 Pinned spine

- **What & why.** For the whole of act one, a 56px spine pins along
  the left edge: the book's title set vertically, the publisher's
  device at its foot, one gilt band near the head. It is where a held
  book's spine stays, and it does three jobs no other element can: it
  tells the visitor, at every scroll depth, *which book this is*; it
  carries act one's progress (the gilt band fills downward); and its
  departure — sliding off with the jacket at the midpoint — is the
  loudest quiet signal that the object has changed.
- **Structure.** A `<aside class="spine">`, `position: sticky` inside
  the jacket layer's full-height rail, 56px wide, ground `--red` at
  the band and `--cloth` below it (a publisher's spine: cloth with a
  red label — the two anchors shaking hands on the one element that
  belongs to both acts). Title in vertical writing-mode; device as
  inline SVG at the foot.
- **Motion spec.** The spine itself does not animate; it *persists*.
  Its gilt band fills downward scrubbed to act-one progress (linear,
  `--ease-gilt` discipline). At the midpoint it leaves as part of the
  jacket layer (§6.1), unpinning in the same frame the slide begins.
- **Choreography timeline (v2).** Load: settles with the assembly
  (§6.2) → act-one scroll: band fills 0 → 100% across the act's full
  scroll length → midpoint trigger: spine translates with the layer,
  gone by +900ms → act two: absent; the page-edge strip (§6.8) has
  taken over the progress job on the opposite edge — progress crosses
  the book at the turn, spine (left, jacket) to page edge (right,
  cloth), and the choreography map (§13) records the hand-over.
- **State matrix (v2).** *Rest:* pinned, band at current fill. *Hover:*
  the spine is not a control; no hover state. *Focus:* contains no
  focusable elements (the device is a mark, not a link — the imprint
  link lives in the colophon, §6.17). *Active:* n/a. *Scrolled-past
  (act two):* absent from layout and tab order. *Disabled:* renders
  as a static rail at the top of the stacked page (no-JS), title
  horizontal above the cover.
- **Content merge.** The spine carries the book's real title and the
  publisher's real device — it is identification, not decoration. A
  spine printed with a different book's title would be a defect a
  bookseller would catch; the gate (§10) checks title agreement
  across cover, spine and colophon.
- **Failure fallback.** If sticky positioning is unsupported, the
  spine renders as a static rail above the cover — identification
  survives, persistence doesn't, content is untouched.
- **Reduced-motion variant.** Identical (the spine never moved); the
  gilt band fills in 10% steps instead of scrubbing.
- **Breakpoints (v2).** ≥1200px: 56px rail as specced. 768–1199px:
  44px rail, title 17px. <768px: the rail retires — a phone is held in
  one hand and has no shelf edge; the title moves into the cover block
  as a horizontal red band, and act-one progress is carried by the
  §6.13 navigation's underline instead. The spine's departure at the
  midpoint is then the cover band leaving with the layer.
- **Edge cases & failure modes (v2).** *Very long title:* the spine
  title truncates with an ellipsis at the rail's height minus the
  device — a real spine does the same; the full title is one viewport
  away on the cover. *Zoom 200%:* the rail scales with layout; if the
  content column would fall below 320px, the rail retires as at
  <768px. *Print:* the spine is removed by the print stylesheet — you
  cannot print a spine on a sheet.
- **Accessibility spec (v2).** The vertical title is real text in a
  `<p>`, reading order first in the jacket layer; `aria-label` gives
  it horizontally ("Spine: [Title], by [Author]"). The gilt band is
  `aria-hidden` decoration; progress is announced by the act's heading
  structure, not by the band. Contrast: `--jacket` title text on
  `--cloth` 9.3:1; the device in `--gilt` is graphic-only.
- **Performance budget & mobile variant.** One sticky element, one
  scrubbed fill in the shared loop (≤0.2ms/frame). Mobile: retired,
  per above — the cheapest variant is absence.
- **Tokens consumed (v2).** `--cloth`, `--red`, `--jacket`, `--gilt`,
  `--ease-gilt`.

### 6.4 "Praise for" stagger

- **What & why.** The back cover's review quotes arrive the way praise
  is read on a real back cover: in review order, top billing first,
  each set down — not floated up — 150ms apart. The stagger is a
  printing order, not a flourish: the *Guardian* quote lands before
  the blog quote because that is the hierarchy the publisher chose,
  and the motion respects the masthead hierarchy it prints.
- **Structure.** A `<ul class="praise">` on the back-cover section
  (`--flap-shade` ground — a handled copy, §4). Each `<li>`: quote in
  Playfair italic, source in Lora 600 small caps beneath. JS arms
  pre-states (opacity 0, translateY 6px) per item.
- **Motion spec.** On the section crossing 70% of the viewport, items
  land one by one: opacity 0 → 1 and 6px → 0 over `--dur-quote`
  450ms `--ease-press`, 150ms stagger, in DOM order (= review order —
  the DOM is the billing). Once landed, items are static forever;
  scroll-back never un-lands them.
- **Choreography timeline (v2).** Section at 70% viewport → +0ms first
  quote begins → +150ms second → +300ms third → each completes 450ms
  after its start → last quote (of a typical five) at rest by
  ≈+1500ms → the colophon mark (§6.10) begins drawing 200ms after the
  final quote lands, lower on the same cover — praise first, then the
  house signs its work.
- **State matrix (v2).** *Rest:* printed quotes. *Hover:* §6.15's card
  treatment where quotes are presented as cards; in the plain spread,
  no hover. *Focus:* quotes are not focusable; their sources may be
  links to the full reviews, taking the standard act-one link
  treatment (red-deep underline draw, 220ms). *Active:* n/a.
  *Scrolled-past:* landed, static. *Disabled:* all quotes visible at
  first paint — praise is content, and content is never armed away
  without JS.
- **Content merge.** The quotes are printed on the back cover being
  shown; the stagger performs the cover's own reading order. Remove
  the motion and the back cover is complete — the stagger is the
  difference between a cover handed to you and a cover already on the
  table.
- **Failure fallback.** The 1000ms watchdog per item: any quote not
  landed within 1000ms of its stagger beat is forced visible. If the
  section is jumped past (anchor, find-in-page), all quotes are set
  landed instantly — hierarchy is preserved in print, not in delay.
- **Reduced-motion variant.** All quotes present at first paint, in
  order. Nothing staggers.
- **Breakpoints (v2).** ≥1200px: two-column spread, stagger runs
  left column then right (DOM order is column order — the build must
  keep DOM and billing in agreement). 768–1199px: one column, same
  stagger. <768px: stagger gap shortens to 90ms and rise to 4px — a
  small cover is read faster.
- **Edge cases & failure modes (v2).** *More praise than fits:* the
  spread caps at six quotes; a seventh belongs on the flap (§6.6's
  territory) or nowhere — a back cover crowded with praise reads as
  desperation (§9). *A quote longer than 40 words:* it is set at the
  smaller 19px size and lands last regardless of source rank — print
  hierarchy yields to fit, as on real covers; the content rule is
  recorded in §12. *Duplicate sources:* forbidden by content rule —
  one quote per masthead, ever.
- **Accessibility spec (v2).** The list is a real `<ul>`; stagger never
  reorders the DOM. Quotes use `<blockquote>` with `<cite>` for the
  source. No aria-live — printed praise does not announce itself.
  Contrast: `--ink` on `--flap-shade` 11.4:1; source lines in
  `--red-deep` 6.7:1 at 13px — passes because sources are set in 600
  weight small caps, and the gate verifies the pairing.
- **Performance budget & mobile variant.** ≤6 items, opacity/transform
  only, no loop cost after landing. Mobile: the 90ms variant above.
- **Tokens consumed (v2).** `--flap-shade`, `--ink`, `--red-deep`,
  `--ease-press`, `--dur-quote`.

### 6.5 Die-cut author photo

- **What & why.** The author photograph is not placed *on* the front
  cover; it is behind it, showing through the jacket's die-cut oval —
  the window the publisher cut in the card. As the cover settles, the
  oval expands and the face resolves from a soft blur to sharp: a
  portrait coming into focus while you hold the book up to look at it.
  It is the theme's single licensed blur-to-sharp (§5), spent on the
  one face the book is about.
- **Structure.** The cover block (§6.14) carries a figure with
  `clip-path: ellipse()` on the image wrapper; the `<img>` is the real
  portrait with full alt text ("Portrait of [Author], photographed by
  [credit]"). The clip animates the ellipse radii; the blur is a
  filter on the image, removed at completion.
- **Motion spec.** In the assembly sequence (§6.2), at +700ms: ellipse
  radii grow 38% → 50%/62% over 700ms `--ease-shelf` while blur goes
  6px → 0 across the same span. At completion both clip and filter are
  dropped to their static values (full oval, no filter) — the resting
  cover carries no live filter.
- **Choreography timeline (v2).** Cover begins arriving +0ms → +700ms
  oval begins opening, face at 6px blur → +1050ms oval at 80%, blur
  2px, features findable → +1400ms oval full, blur 0, filter removed →
  the photo credit caption (italic Lora, beneath the oval) fades in
  over 300ms — credit follows the face, never precedes it.
- **State matrix (v2).** *Rest:* sharp portrait in a full oval. *Hover:*
  the cover's gloss (§6.7) passes over the oval like over any part of
  the laminated cover — the photo is under the laminate too. *Focus:*
  the figure is not focusable; if the portrait links to the author's
  page, the link wraps the cover block's author name, not the image.
  *Active:* n/a. *Scrolled-past:* static sharp. *Disabled:* full oval,
  sharp, at first paint — the die-cut is a shape, not an animation,
  and the shape is pure CSS.
- **Content merge.** The photo is behind the jacket's actual die-cut
  window; the reveal performs the physical fact that the face was
  always there, covered by card. An author photo placed in a rounded
  rectangle "card" would be a website wearing a book costume (§9).
- **Failure fallback.** Image fails to load: the oval shows the
  author's initials set in Playfair at cover size on `--flap-shade` —
  the placeholder a publisher would use on a proof — with the credit
  line intact. The clip animation is skipped; nothing else in the
  assembly waits for the image.
- **Reduced-motion variant.** Full oval, sharp, static from first
  paint.
- **Breakpoints (v2).** ≥1200px: oval at the cover's right third, as
  specced. 768–1199px: oval centred above the title block. <768px:
  oval smaller (radii 42%/54%), blur span shortened to 4px → 0 over
  500ms — small screens resolve faster and cheaper.
- **Edge cases & failure modes (v2).** *Portrait orientation image:*
  the frame is aspect-locked 4:5; `object-fit: cover` with
  `object-position` set per-image at build time so the face sits in
  the oval's upper two-thirds (content rule, gate-checked). *No author
  photo exists* (a press, an anthology): the die-cut shows the
  colophon mark (§6.10) at cover size instead — the window never shows
  a stock face. *Dark scheme:* the portrait is not filtered or
  darkened; faces do not change with room light (§2).
- **Accessibility spec (v2).** Real alt text as above; the clip and
  blur are visual only. The credit line is plain text, not part of the
  image. Focus order: the portrait sits in DOM order where the cover
  presents it — after the title, before the standfirst.
- **Performance budget & mobile variant.** One filter animation on one
  image, removed at rest; image ≤ 180KB (the oval crops, so serve at
  1.5× display size). Mobile: the shortened variant above.
- **Tokens consumed (v2).** `--jacket`, `--flap-shade`, `--ease-shelf`.

### 6.6 Flap-unfold click

- **What & why.** The front flap is the jacket's working part: outside,
  it carries the author's biography in brief; inside — the part you
  only see when you unfold it — the price, the barcode, the edition
  line. Clicking the flap unfolds it from its spine fold to show that
  underside. It is the theme's conversion gesture disguised as book
  handling: the price is revealed by the exact motion a browser in a
  bookshop makes, and the barcode's digits encode the publication
  date — the original entry's anti-slop signature, kept and specified.
- **Structure.** A `<section class="flap">` with two faces: `.flap-out`
  (biography, author note) and `.flap-in` (price block, barcode,
  edition line, the buy/order actions of §6.16's family in miniature),
  rotating on a `rotateY` hinge at the flap's left (spine-side) edge,
  `perspective` on the parent. The barcode is real DOM: CSS-gradient
  bars over a digit line — the digits are the publication date in
  DDMMYYYY, captioned as such (§12). The flap is a `<button>`-wrapped
  region? No — the flap face carries a real button, "Price and
  edition", because a whole-card click target with nested links inside
  is an accessibility failure; the button toggles, the faces contain
  their own links.
- **Motion spec.** Toggle: rotateY 0 → −180° over `--dur-flap` 500ms
  `--ease-whisper`, faces backface-hidden, the underside pre-rotated.
  A soft shadow sweeps the gutter as the flap lifts (opacity peak at
  90°, gone at rest). Refold reverses identically. On first unfold,
  the flap counters (§6.11) fire.
- **Choreography timeline (v2).** Click → +0ms button state flips,
  `aria-expanded` true → +0–250ms flap lifts to −90°, gutter shadow at
  peak, out-face unreadable by −60° (by design — a turning flap is
  illegible mid-turn, as paper is) → +500ms underside flat, shadow
  gone → +550ms the price block's own tiny settle (2px, 150ms) — the
  underside was printed, not animated in; only the paper moved.
- **State matrix (v2).** *Rest:* folded, biography out. *Hover:* the
  flap's free edge lifts 2px and its shadow deepens slightly — paper
  responding to a hand approaching (desktop, fine pointer only).
  *Focus:* the toggle button takes a 2px `--red-deep` outline offset
  3px; the flap does not move on focus alone. *Active:* during the
  500ms turn, the button is disabled against double-toggles; a second
  click queues the refold after landing. *Scrolled-past:* state
  persists — a flap left open stays open for the session. *Disabled
  (no JS):* both faces render stacked, biography then price block,
  under their own headings — the underside is content, and content is
  never hidden behind a script.
- **Content merge.** The flap is the jacket's real flap and its
  underside carries the book's real price block — price, ISBN,
  barcode, edition. The unfold is not a reveal effect applied to a
  pricing card; it is the pricing card's physical form.
- **Failure fallback.** 3D transforms unsupported: the toggle becomes
  a crossfade (200ms) between faces. Watchdog: if `transitionend` is
  lost, a 600ms timer forces the end state and face visibility.
- **Reduced-motion variant.** No rotation: the faces crossfade in
  150ms, or — at the visitor's stronger setting — both faces simply
  stack as in the no-JS state. The price is never gated behind motion.
- **Breakpoints (v2).** ≥1200px: flap at the cover block's right,
  width 340px, hinge vertical. 768–1199px: flap below the cover,
  width 100%, hinge still vertical (it is a flap, not an accordion).
  <768px: the rotateY is replaced by the crossfade variant at all
  motion settings — a full-screen 3D flap on a phone reads as a UI
  card trick, not paper; the gutter shadow is dropped.
- **Edge cases & failure modes (v2).** *Long biography:* the out-face
  scrolls internally never — flap copy is rationed at build time
  (§12: 90 words out, the price block in); overflow is a content bug
  the gate catches, not a runtime state. *Price changes between
  printings:* the underside carries the edition line with the price,
  so a stale price is visibly a *first-edition* price — the theme's
  honesty mechanism; the buy actions (§6.16) always show the live
  price adjacent, and a mismatch between flap price and buy price is
  a §10 gate failure. *Barcode digits:* if the publication date is
  unconfirmed at build time, the barcode is omitted entirely — an
  invented date in the barcode is exactly the fabrication the theme
  exists to refuse.
- **Accessibility spec (v2).** Button labelled "Price and edition —
  unfold the flap", `aria-expanded`, `aria-controls` to the underside
  region; the underside is `hidden` until expanded (and present in the
  no-JS stack). The barcode is `aria-hidden` with the ISBN and price
  as real text beside it. Touch target: the button is a full-width
  strip ≥48px tall on the flap's free edge. Contrast: price in
  `--ink` on `--flap-shade` 11.4:1; the date caption in `--red-deep`
  6.7:1.
- **Performance budget & mobile variant.** One rotateY on one element;
  shadow is a gradient, not a filter. Mobile: crossfade variant, zero
  3D cost.
- **Tokens consumed (v2).** `--flap-shade`, `--jacket`, `--ink`,
  `--red-deep`, `--ease-whisper`, `--dur-flap`.

---

### 6.7 Gloss-follow hover

- **What & why.** A laminated jacket answers the light. On the front
  cover, a gloss light spot follows the pointer — lerped, never glued
  — and the whole cover tilts up to 3°, like a book lifted and angled
  for inspection. It is act one's only pointer-physics element, and it
  lives exclusively on the cover: gloss is a property of the jacket's
  surface, so the moment the jacket comes off, gloss leaves the site
  forever (§5's act discipline).
- **Structure.** The cover block (§6.14) carries a `::before` radial
  gradient (`--gloss`, 340px diameter, centred on custom properties
  `--gx`/`--gy`) and the block itself takes a `rotateX/rotateY` pair
  from the same pointer handler. Pointer position is recorded by a
  passive listener and consumed in the shared rAF loop — the handler
  never writes styles directly.
- **Motion spec.** Light spot: lerp 120ms behind the pointer (loop
  factor ≈0.14/frame at 60fps). Tilt: rotateY = (x − 0.5) × 6° max
  ±3°, rotateX inverse, same lerp; on leave, both ease home over
  400ms `--ease-shelf`. The gloss opacity is 0.55 at rest-over, fading
  to 0 over 300ms after the pointer leaves — laminate does not switch
  off.
- **Choreography timeline (v2).** Pointer enters cover → +0ms gloss
  begins fading in at the entry point → +120ms gloss centred under
  pointer (lerped), tilt at ≈60% → +250ms tilt settled at pointer's
  angle → pointer crosses the die-cut oval: the gloss passes *over*
  the photograph (it is under the same laminate, §6.5) → pointer
  leaves → +400ms tilt home, gloss out by +300ms → cover at printed
  rest.
- **State matrix (v2).** *Rest:* no gloss, no tilt — the printed
  cover. *Hover:* as specced, fine pointers only. *Focus:* keyboard
  focus on any cover child (title link, author link) brings the gloss
  to that element's centre at 60% opacity with no tilt — keyboard
  visitors get the light, not the lift. *Active:* pointer-down presses
  the tilt to 0 and the gloss brightens 10% for 120ms — the book
  pressed flat under a hand. *Scrolled-past:* handler detached when
  the cover is off-screen (IntersectionObserver), loop cost zero.
  *Disabled / touch:* no gloss, no tilt — touch has no hover and a
  tapped book does not gleam; the cover is its printed self.
- **Content merge.** The gloss is on the jacket's own laminated
  surface and moves the way light moves on a real cover the visitor is
  tilting. It decorates nothing: remove it and the cover loses a
  physical property, not an ornament.
- **Failure fallback.** Pointer events unsupported or the loop
  stalled: the cover is static and complete. The gloss is a
  pseudo-element — it can fail without taking any content with it.
- **Reduced-motion variant.** No tilt; the gloss appears statically at
  the cover's upper third (where the assembly sheen came to rest,
  §6.2) at 30% opacity, or is omitted entirely — both pass the gate;
  a *moving* gloss under reduced motion does not.
- **Breakpoints (v2).** ≥1200px: full spec, 340px spot. 768–1199px:
  tilt ≤2°, spot 280px. <768px: no tilt, no follow — the idle sheen
  (§6.2) is act one's only gloss on phones.
- **Edge cases & failure modes (v2).** *Pointer over the flap button:*
  the gloss yields — opacity halves while the pointer is over any
  interactive child, so light never competes with a control's focus or
  hover state. *Fast pointer exit and re-entry:* the lerp state is
  continuous; no snap. *The midpoint fires while hovering:* the whole
  cover is leaving with the layer (§6.1); the handler detaches at
  slide start — gloss never chases a departing jacket.
- **Accessibility spec (v2).** Purely visual; the gradient is a
  pseudo-element, the tilt never moves content out of its layout box
  (transform only, ≤3° — text remains legible at all angles, verified
  at the gate). No information is carried by the gloss. Focus-visible
  outlines render above the gloss layer (z-order rule, §10).
- **Performance budget & mobile variant.** One gradient + one
  transform, compositor-only, ≤0.3ms/frame while hovering, zero at
  rest. Mobile: absent, per breakpoints.
- **Tokens consumed (v2).** `--gloss`, `--ease-shelf`, `--jacket`.

### 6.8 Gilt page-edge progress

- **What & why.** Act two's progress instrument, and the theme's
  second thesis: reading a book is measured in leaves. A gilt
  page-edge strip fixed at the viewport's right edge brightens and
  fills downward, scrubbed to cloth-act progress, while a bookmark
  ribbon descends the margin beside it. The gilt is not a progress
  bar wearing gold paint — it is the book's page edges, which really
  are gilt, brightening as more of them have been turned past.
- **Structure.** A fixed 10px rail at the right viewport edge
  (act two only): a track in `--cloth-deep`, a fill in `--gilt`
  brightening to `--gilt-bright` at its leading edge, height scrubbed.
  The ribbon is a 22px-wide `--red` strip (the one licensed red in act
  two, §2) descending inside the margin column, its V-cut tail at its
  foot; its length marks chapters passed. Both are `aria-hidden`
  instruments; progress is conveyed to AT by the heading structure.
- **Motion spec.** Pure scrub, `--ease-gilt` discipline: fill height =
  cloth-act scroll progress, computed in the shared loop with the
  theme's standard lerp (0.14) — smooth, never stepped, never eased
  ahead of the visitor's hand. Brightness: the fill's top 48px
  gradient runs `--gilt` → `--gilt-bright` — the edge you are
  currently turning past catches the light. The ribbon descends in
  chapter increments: at each chapter head crossing viewport centre,
  it extends by one chapter-share over 400ms `--ease-leaf`.
- **Choreography timeline (v2).** Midpoint (§6.1) completes → +950ms
  the rail fades in over 300ms at 0% fill, ribbon at chapter zero →
  act-two scroll: fill scrubs continuously → each chapter head at
  viewport centre: ribbon extends (400ms) and the chapter numeral in
  the margin (§6.13) gilds — instrument and furniture agreeing → final
  chapter: fill reaches 100%, the whole edge holds `--gilt-bright`
  for the colophon (§6.17) — the book finished, its edges fully lit.
- **State matrix (v2).** *Rest (act one):* absent entirely — act one
  has the spine's band (§6.3); the two instruments never coexist.
  *Hover / focus:* none; not controls. *Active:* n/a. *Scrolled-past
  (above act two, jacket replaced via colophon link):* rail unmounts
  with the act. *Disabled:* absent; the chapters' own headings carry
  position, as in any book.
- **Content merge.** The strip is the book's page edges and the ribbon
  is the book's bookmark — both are parts of the object being read,
  reporting on the reading. A generic gold progress bar pasted on a
  non-book site would be §9; here the instrument and the object are
  one.
- **Failure fallback.** If the shared loop stalls, a scroll listener
  fallback sets the fill from raw scroll position at most every
  100ms (steppier, still true). If JS is absent, see Disabled.
- **Reduced-motion variant.** Fill jumps in 5% steps at scroll rest;
  ribbon extends instantly at chapter boundaries. The instruments
  still report; they no longer flow.
- **Breakpoints (v2).** ≥1200px: rail + ribbon as specced, ribbon in
  the margin column. 768–1199px: rail only, 8px; the ribbon retires
  (the margin is too narrow to hold it honestly). <768px: rail thins
  to 4px at the edge; ribbon absent; chapter numerals carry progress
  alone.
- **Edge cases & failure modes (v2).** *Short cloth act (one
  chapter):* the ribbon is omitted — a bookmark in a one-chapter book
  is a prop; the rail still reports. *Scroll-back:* fill retreats
  exactly with position — gilt does not stay lit for pages un-read;
  the ribbon, however, keeps its longest reach (a bookmark stays
  where you left it) — the asymmetry is deliberate and documented
  here so no builder "fixes" it. *Zoom:* the rail is viewport-fixed
  and unaffected by layout zoom.
- **Accessibility spec (v2).** Both instruments `aria-hidden="true"`.
  A visually-hidden progress text ("Chapter 3 of 7") sits in the
  act-two nav (§6.13) for AT — the honest channel. The rail never
  overlaps content: act two's layout reserves a 26px right gutter for
  it at every breakpoint where it exists.
- **Performance budget & mobile variant.** One height + one gradient
  position per frame, ≤0.2ms. Mobile: the 4px rail variant.
- **Tokens consumed (v2).** `--gilt`, `--gilt-bright`, `--cloth-deep`,
  `--red`, `--ease-gilt`, `--ease-leaf`.

### 6.9 Endpaper swirl transition zone

- **What & why.** When a jacket comes off a real book, the first thing
  exposed is not a chapter — it is the endpaper, the marbled sheet
  pasted inside the boards. The theme gives that moment a full
  viewport: at the midpoint, a marbled endpaper band whose grain
  swirls faintly for three seconds as the jacket leaves. It is the
  hinge of the page, decorated exactly as the hinge of a book is
  decorated — and it is the rarest texture on the site (§4), because
  endpapers are glimpsed, not stared at.
- **Structure.** A full-viewport `<section class="endpapers">` between
  the acts: an SVG turbulence marbling pattern (two feTurbulence
  layers, comb-stroked paths in `--cloth`, `--gilt` at 12%, and
  `--red` at 6% — the book's own colours, marbled) over `--cloth-deep`.
  Centred on it, one line of Lora italic — the last line of the jacket
  act (§12's paired line) — and nothing else. No navigation, no
  controls except the §6.1 button repeated as a text link for
  keyboard users who arrive here by heading.
- **Motion spec.** As the zone enters, the turbulence baseFrequency
  drifts 0.012 → 0.009 over 3s (`--ease-whisper` timing) — a swirl
  settling, like ink in water slowing. At the slide-off (§6.1), the
  swirl peaks (a second 1.2s drift) in the gutter the jacket vacates.
  After the zone is passed, the pattern is static forever.
- **Choreography timeline (v2).** Zone at 40% viewport → swirl drift
  begins → midpoint marker at 50% → slide-off fires (§6.1) → swirl
  peak overlaps the slide's first 450ms → zone exits → pattern frozen
  → the cloth act's first chapter head rises (§5) as the zone's top
  leaves the viewport — the book opens as its endpapers close.
- **State matrix (v2).** *Rest:* static marbling, the paired line.
  *Hover / focus:* no interactive states except the text link
  (standard gilt underline). *Active:* n/a. *Scrolled-past:* frozen
  pattern. *Disabled:* static marbling (pure SVG, no JS needed for
  the pattern itself — only the drift is scripted).
- **Content merge.** The swirl is on the book's own endpapers, visible
  exactly when endpapers are visible — during the removal, in the
  gutter. It is not a decorative divider pasted between sections; it
  is the physical sheet the narrative passes through.
- **Failure fallback.** SVG filters unsupported: the zone falls back
  to a flat `--cloth-deep` band with a printed gilt rule — the
  endpaper of a cheaper binding, still a real endpaper. The paired
  line and the turn are unaffected.
- **Reduced-motion variant.** Static marbling, no drift, no peak. The
  zone still performs its narrative job (it is a place, not only an
  animation).
- **Breakpoints (v2).** ≥1200px: full-viewport band. 768–1199px: 80vh
  band. <768px: 70vh, swirl opacity halved (§6.1's mobile ruling), the
  paired line at 19px.
- **Edge cases & failure modes (v2).** *The visitor never scrolls
  here* (arrives via a deep link into act two): the zone is simply
  above them in the document, static — correct; endpapers sit inside
  the front board whether or not you looked at them. *Filter cost on
  low-power devices:* the turbulence renders once to a static bitmap
  (canvas snapshot at first paint); only the pre-rendered drift on a
  transform is animated — if the snapshot fails, the flat fallback
  above ships instead.
- **Accessibility spec (v2).** The marbling is `aria-hidden`; the
  paired line is a real paragraph, in reading order — it is the last
  line of act one's copy and must make sense read aloud between the
  flap and chapter one. Contrast: `--paper-text` on `--cloth-deep`
  12.5:1.
- **Performance budget & mobile variant.** One static SVG + one
  transform drift; no per-frame filter animation (the snapshot rule
  above is a hard budget, not a suggestion). Mobile: halved-opacity
  variant.
- **Tokens consumed (v2).** `--cloth`, `--cloth-deep`, `--gilt`,
  `--red`, `--paper-text`, `--ease-whisper`.

### 6.10 Colophon-mark draw

- **What & why.** On the back cover, low and centred, the publisher's
  colophon mark — the house's device — draws itself in SVG strokes as
  the cover enters. A colophon mark is how a printing house signs its
  work; having it *print itself* on arrival is the theme's smallest
  signature and its most publisherly: the house does not decorate the
  cover, it signs it, last, after the praise (§6.4's choreography
  hands it the final beat).
- **Structure.** Inline SVG of the house device (a real mark supplied
  by the publisher — paths, not a font glyph), stroke `--red-deep` on
  the back cover's `--flap-shade`, sized 44px. Draw via
  stroke-dashoffset; at completion the stroke is filled at 12% red —
  a printed mark, slightly inked.
- **Motion spec.** Trigger: the back cover at 75% viewport, *and*
  200ms after the final praise quote lands (§6.4). Duration
  `--dur-draw` 500ms `--ease-press`, strokes in the mark's own path
  order. Once only; the mark is printed, and print does not repeat.
- **Choreography timeline (v2).** Final quote lands → +200ms first
  stroke begins → strokes sequence across 500ms → +700ms fill fades
  in over 200ms → mark at rest: a printed device. Scroll-back: stays
  drawn.
- **State matrix (v2).** *Rest:* drawn mark. *Hover / focus / active:*
  none — the mark is not a link (the imprint link lives in §6.17's
  colophon; a logo-link here would duplicate it). *Scrolled-past:*
  drawn. *Disabled:* the SVG renders fully stroked at first paint —
  dash pre-states are JS-armed only.
- **Content merge.** The mark brands the cover it is printed on; its
  draw is the signing of this specific book by this specific house.
  The same device appears at the spine's foot (§6.3) and in the cloth
  colophon (§6.17) — one house, one mark, three printings, each in its
  place.
- **Failure fallback.** Path-length measurement fails: the mark fades
  in over 300ms instead. SVG unsupported: a text device (the house
  initials in Playfair) stands in — a mark, still.
- **Reduced-motion variant.** Mark present, fully drawn, at first
  paint of the cover.
- **Breakpoints (v2).** All: 44px. <768px: 36px — a small cover signs
  smaller.
- **Edge cases & failure modes (v2).** *House has no device:* the
  element is omitted and the spine's foot carries the house name in
  type instead — never invent a mark for a real publisher; a drawn
  monogram of initials is permitted only if the house actually uses
  one. *Mark reused across the publisher's other sites:* expected and
  correct — it is a house mark, not a page decoration.
- **Accessibility spec (v2).** `role="img"` with `aria-label`
  "Colophon of [Publisher]". Decorative duplicates (spine foot) are
  `aria-hidden`. Contrast: `--red-deep` on `--flap-shade` ≈6.3:1 for
  a graphic mark — ample.
- **Performance budget & mobile variant.** One dashoffset animation,
  ≤4 paths. Negligible. Mobile: the 36px variant.
- **Tokens consumed (v2).** `--red-deep`, `--flap-shade`,
  `--ease-press`, `--dur-draw`.

### 6.11 Flap counters

- **What & why.** On the front flap, among the edition data, two
  figures count up once: the print run ("Printed in a run of 2,500")
  and the edition size ("Edition of 1,500"). They count because a
  flap's numbers are the book's vital statistics, and watching them
  arrive is watching the edition declare itself. They are also the
  theme's honesty test: these figures must be the book's real figures,
  supplied by the publisher — an invented print run is precisely the
  fabrication this theme refuses (§1's law), and §10's gate audits
  them against the edition line printed beside them.
- **Structure.** Two `<p class="flap-stat">` lines on the flap's
  out-face (§6.6): label in words, figure in Lora 600 tabular. The
  final figures are the DOM text; JS counts *toward* them from 62% of
  value (a run filling, not a slot machine from zero).
- **Motion spec.** Trigger: the flap first entering the viewport at
  70%, or its first unfold (§6.6) — whichever is earlier; once only.
  Duration `--dur-count` 800ms, `--ease-press`, figures rounded to
  whole copies, formatted with the locale's thousands separator at
  every step (a run of 2,500 never displays as "1873" mid-count
  without its comma — typeset at every frame).
- **Choreography timeline (v2).** Trigger → +0ms both figures begin
  together (an edition declares itself all at once) → +800ms both
  land on the true figures → the edition line beneath them (static
  text: "Second edition · [Month Year]") is revealed by proximity,
  not animated — it was always printed under the numbers.
- **State matrix (v2).** *Rest:* true figures, static. *Hover /
  focus:* none — statistics are not controls. *Active:* n/a.
  *Scrolled-past:* landed figures. *Disabled:* true figures at first
  paint (they are the DOM text; counting is an enhancement over
  them).
- **Content merge.** The figures are the flap's own edition data,
  printed where flaps print them. They are not site metrics wearing a
  book costume — no visitor counts, no sales claims; a print run is a
  fact about the object, verifiable against the edition line.
- **Failure fallback.** Counting interrupted (tab hidden mid-count):
  on return, figures snap to truth — a flap never shows a stale
  half-count. Any JS failure: DOM truth stands.
- **Reduced-motion variant.** Figures present at truth from first
  paint; no count.
- **Breakpoints (v2).** Identical at all sizes; on <768px the two
  stats stack (run above edition) in the flap's narrowed column.
- **Edge cases & failure modes (v2).** *Figures not yet confirmed*
  (pre-publication page): the stats are omitted entirely and the flap
  carries "Edition details at publication" — a promise, not a number.
  *Reprint while the page lives:* the figures and the edition line
  update together in one edit; a page showing run-of-2,500 under a
  "Third edition" line fails §10. *Very large runs:* format holds to
  six figures; beyond that, words ("over a million copies") — flaps
  speak in words past a point, and so does this theme (§12).
- **Accessibility spec (v2).** The counting span is `aria-hidden`; a
  visually-hidden sibling carries the final figure for AT from first
  paint, so no screen reader ever hears a number mid-count. Contrast:
  `--ink` on `--flap-shade` 11.4:1.
- **Performance budget & mobile variant.** Two text updates per frame
  for 800ms, once per session. Negligible. Mobile: identical.
- **Tokens consumed (v2).** `--ink`, `--flap-shade`, `--ease-press`,
  `--dur-count`.

### 6.12 Dual-mode transitions + jacket skeleton (loader)

- **What & why.** The theme knows which object the visitor is
  holding, and its page transitions say so. Before the midpoint,
  navigation is a **cover close-open**: the jacket closes over the
  page and reopens on the new one — you are still handling the
  packaged book. After the midpoint, navigation is a **page turn**
  inside the book. Loading, likewise, shows the book's own skeleton:
  blank cover blocks that gain their blurbs — a jacket at the printer,
  not a grey UI shimmer. One systems piece, three expressions, all of
  them the same fact: transitions respect the object.
- **Structure.** Transitions: a full-viewport overlay leaf — jacket
  side: `--jacket` with the spine band at its left; cloth side:
  marbled endpaper (§6.9's pattern) — animated per mode. Skeleton:
  the cover block's layout rendered in `--flap-shade` blocks (title
  block, oval, blurb lines) with the colophon mark's outline at the
  foot; content swaps in block by block as it arrives, each block's
  blurb fading in over 250ms — "gaining their blurbs", per the
  original entry.
- **Motion spec.** Cover close-open: overlay slides in from the right
  over 300ms `--ease-whisper`, holds while the route swaps, slides
  out left over 300ms — total `--dur-close` 600ms. Page turn: the
  leaf rotates from the right edge (rotateY 0 → −12° with a travelling
  shadow) and sweeps across over `--dur-turn` 500ms `--ease-leaf`,
  content swapped at the covered moment (+250ms). Mode is chosen by
  the *destination's* act if a route crosses the midpoint, else the
  current act. Skeleton: minimum display 300ms (shorter reads as a
  flicker, not a printing), blocks resolve top-down in cover order.
- **Choreography timeline (v2).** Nav click → +0ms overlay begins →
  +300ms page covered, route swaps beneath → +350ms new page's first
  elements arm (assembly §6.2 is *not* replayed; the new jacket is
  already printed — only the §6.12 overlay performed) → +600ms overlay
  gone, focus moved to the new page's `<h1>` → skeleton path: route
  data pending → blocks shown → each block resolves on arrival →
  +300ms after last block, skeleton unmounts.
- **State matrix (v2).** *Rest:* no overlay. *Hover / focus:* nav
  links keep their act treatments during transitions. *Active
  (transition running):* the overlay is inert and `aria-hidden`; a
  second navigation during a transition snaps the overlay to the
  newest target (latest instruction wins; the leaf never queues).
  *Scrolled-past:* n/a. *Disabled:* plain navigation, instant — the
  browser's own behaviour is the fallback, and every route works
  without the overlay because links are real links.
- **Content merge.** The transition *is* the book being handled —
  closed and reopened, or a page turned — and the skeleton is the
  book at the printer. Neither is a loading spinner wearing a theme;
  both are the object's own states.
- **Failure fallback.** Transition JS fails: navigation proceeds
  without it (the overlay is an enhancement layered over real links,
  never a router). Skeleton data fails: the blocks give way to a
  printed error line in the cover's own voice (§12) with a retry
  link — a misprint notice, not an error toast. Watchdog: any overlay
  still covering the page at +1200ms is removed by force — a leaf may
  never strand a reader.
- **Reduced-motion variant.** Both modes become a 150ms crossfade;
  the skeleton is static blocks resolving instantly as data arrives.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: close-open
  500ms total. <768px: page turn loses its rotateY (a sweep + shadow
  only, 400ms) — small leaves do not lift in 3D; close-open 450ms.
- **Edge cases & failure modes (v2).** *Slow connection (≤3G or
  save-data):* transitions disarm entirely — instant navigation; a
  performed transition on a slow route is a delay wearing a costume.
  *Crossing the midpoint by link* (jacket nav's "Begin the book"):
  the close-open plays, and the destination arms act two — the
  slide-off (§6.1) does not *also* play; one ceremony per turn.
  *Back/forward:* the turn reverses direction (leaf sweeps from the
  left) — the browser's history and the book's leaves agree about
  which way is back.
- **Accessibility spec (v2).** Overlay `aria-hidden`, focus moved to
  the destination `<h1>` (tabindex −1) at +600ms and announced via
  the route's own title change; skeleton blocks carry `aria-busy` on
  their region with a visually-hidden "The book is being printed…"
  — replaced by content, never by a completion announcement.
- **Performance budget & mobile variant.** One overlay transform;
  skeleton is static layout (no shimmer animation — shimmer is a UI
  habit, and this skeleton's motion is the *arrival of content*).
  Mobile: the sweep variants above.
- **Tokens consumed (v2).** `--jacket`, `--cloth-deep`, `--ease-whisper`,
  `--ease-leaf`, `--dur-close`, `--dur-turn`, `--flap-shade`.

---

### 6.13 Jacket & contents navigation (page-family: navigation)

- **What & why.** The site has two navigations because the book has
  two tables of direction. In act one, the navigation is the jacket's
  own furniture: a slim bar across the cover's head carrying the
  imprint name, the book's sections named as a jacket names them
  (Cover, Praise, The Flap), and the "Remove the jacket" button
  (§6.1) — the one control that changes the object itself. In act
  two, the navigation is the book's **contents page**: chapter titles
  with dotted leaders and page-leaf numbers, set in Lora, the current
  chapter gilt. A visitor should be able to tell which act they are
  in from the navigation alone.
- **Structure.** Act one: `<nav class="jacket-nav">`, `--jacket`
  ground, hairline rule beneath, links in Lora 600 14px uppercase,
  current section marked by a `--red` rule above its link. Act two:
  `<nav class="contents">`, a contents list — each row: chapter
  numeral (gilt), title, dotted leader (border-bottom dotted
  `--paper-text` at 40%), leaf number. On ≥1200px the contents sits
  in act two's left margin as a sticky rail; below that it is a
  section at the act's head.
- **Motion spec.** Act-one links: red rule draws in from the left
  over 220ms on hover/focus. Act-two rows: on hover, the row's leaf
  number gilds (`--gilt` → `--gilt-bright`, 200ms) and the leader
  dots darken — the chapter being considered lights its edge (§6.8's
  vocabulary, miniaturised). Sticky rail: no motion of its own.
  Act change: the jacket nav leaves with the layer (§6.1); the
  contents rail fades in at +950ms with the other act-two instruments.
- **Choreography timeline (v2).** Load: jacket nav present from first
  paint (it is print, not animation) → midpoint: nav exits with the
  layer → +950ms contents rail fades in (300ms), current chapter
  already gilt — the contents opens knowing where you are → chapter
  scroll: the gilt current-marker moves at chapter boundaries,
  crossfading 200ms, in step with the ribbon (§6.8).
- **State matrix (v2).** *Rest:* current section/chapter marked.
  *Hover:* as specced. *Focus:* 2px outline (`--red-deep` in act one,
  `--gilt-bright` in act two), offset 3px. *Active:* the "Remove the
  jacket" button presses (translateY 1px, 100ms) — the only nav
  control with an active state, because it is the only one that does
  something physical. *Scrolled-past:* act-one nav scrolls away with
  the cover (it is not sticky — a jacket's head is not a website
  header); the contents rail is sticky in act two. *Disabled:* both
  navs are plain link lists; the contents' leaders are CSS borders
  and survive.
- **Content merge.** The navigations are the object's own direction
  furniture — jacket furniture and contents page — not a website
  header wearing either costume. Their labels are the book's real
  divisions.
- **Failure fallback.** Sticky unsupported: the contents becomes a
  head-of-act section; all links remain. The "Remove the jacket"
  button degrades to the anchor fallback (§6.1).
- **Reduced-motion variant.** Rule draws and gilding apply instantly;
  no fades.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: contents
  rail becomes a horizontal contents strip above chapter one (leaders
  dropped — a strip has no room for leaders to lead anywhere).
  <768px: act-one nav collapses to imprint + "Remove the jacket" +
  a "Sections" disclosure (native `<details>`, styled as print);
  act-two contents is a full section, rows at 48px touch height.
- **Edge cases & failure modes (v2).** *Many chapters (>9):* the
  contents rail caps at the chapters of this book — a real contents
  lists them all; if the rail would exceed viewport height it scrolls
  internally, gilt current row kept in view. *A page that is all act
  one* (a teaser page): the contents nav never exists; the jacket nav
  carries an "About the book" anchor into the flap instead — the
  theme does not fake a second act.
- **Accessibility spec (v2).** Two `<nav>` landmarks with distinct
  labels ("Jacket", "Contents"). Current location via
  `aria-current`. The visually-hidden progress text ("Chapter 3 of
  7") lives in the contents nav (§6.8's honest channel). Touch
  targets ≥44px in the mobile variants. Contrast: act-one links
  `--ink` on `--jacket` 13.1:1; contents titles `--paper-text` on
  `--cloth` 8.7:1, leaders decorative.
- **Performance budget & mobile variant.** Static bars; hover
  transitions are opacity/colour only. Mobile: the disclosure variant
  — zero JS required (native details).
- **Tokens consumed (v2).** `--jacket`, `--red`, `--red-deep`,
  `--cloth`, `--paper-text`, `--gilt`, `--gilt-bright`.

### 6.14 Front-cover hero composition (page-family: hero)

- **What & why.** The hero is not *like* a front cover; laid out by
  this spec, it *is* the front cover, at full viewport: the title at
  cover size in Playfair, the author's name above it in spaced caps
  (as covers print the name before the title when the name sells the
  book — the order is a content decision, §12), the die-cut portrait
  (§6.5) at the right third, one line of praise at the foot in place
  of a cover quote, and the publisher's name at the very foot, where
  publishers print it. Everything a browser decides from a cover, this
  hero must survive being decided from.
- **Structure.** `<section class="cover">` on `--jacket`, inside the
  jacket layer: author line, `<h1>` title, standfirst (masked line
  reveal, §5), the die-cut figure, the cover-quote line (the single
  strongest praise quote, repeated in full on the back cover — covers
  excerpt, backs print whole), publisher line. The foil treatment:
  the title's key word may carry a gilt gradient text fill — printed
  foil, the one licensed gilt on the jacket (§2) — applied to one
  word, never the whole title.
- **Motion spec.** The assembly (§6.2) delivers the cover; within it:
  standfirst lines mask-reveal at +500ms (550ms per line, 70ms
  stagger, §5); the cover quote fades in last, +1500ms, 400ms
  `--ease-press`. The gloss (§6.7) owns the cover thereafter. No other
  motion: a cover at rest is print.
- **Choreography timeline (v2).** Assembly beats (§6.2) → standfirst
  lines uncover → die-cut resolves (+700–1400ms) → cover quote lands
  → sheen sweep (+1350ms) passes over the *complete* cover — title,
  face, quote — because the laminate covers all of it → rest.
- **State matrix (v2).** *Rest:* the printed cover. *Hover:* §6.7's
  gloss and tilt (the hero is the gloss's home). *Focus:* first
  tab stop is the author link or the title's edition link if present;
  focus brings the gloss to the element (§6.7). *Active:* n/a.
  *Scrolled-past:* cover parallax at 0.92× (§5) carries it gently out
  — the cover leaves slightly slower than the page, the way a held
  cover lags the turning hand. *Disabled:* complete static cover.
- **Content merge.** Total: every element of the hero is an element of
  a real front cover, in its real position, doing its real job. There
  is no hero "content" separate from the cover to merge with.
- **Failure fallback.** The assembly's watchdog (§6.2); the cover is
  complete in the DOM before any motion arms.
- **Reduced-motion variant.** Static cover, standfirst printed, no
  sheen.
- **Breakpoints (v2).** ≥1200px: cover grid — text left 7 columns,
  portrait right 4. 768–1199px: portrait above the title, centred,
  title at 64px floor. <768px: title clamp floor 44px (never below —
  a cover title that whispers is a failed cover), portrait oval at
  §6.5's mobile size, publisher line retained (small covers still
  print the house name).
- **Edge cases & failure modes (v2).** *Very long title (>9 words):*
  the title steps down one register (floor 40px at ≥1200px) and the
  standfirst is cut to one line — the cover absorbs length by
  hierarchy, never by shrinking below presence. *No cover quote yet*
  (pre-review launch): the foot carries the publication date line
  instead — a cover may announce its date; it may not invent praise.
  *Author name order:* name-above-title vs title-first is set once
  per book at build time from the publisher's actual cover; the
  builder does not improvise it.
- **Accessibility spec (v2).** The `<h1>` is the book's title — the
  page's single h1. The foil gradient word keeps a solid-colour
  fallback for forced-colours mode (`--red` text). Reading order:
  author, title, standfirst, portrait + credit, quote, publisher.
  Contrast: title `--ink` on `--jacket` 13.1:1 (the foil word is
  decoration over a title whose full text is also in the DOM as
  text — gradient text remains text, and in forced-colours it
  resolves to the fallback).
- **Performance budget & mobile variant.** The hero's costs are its
  children's (§6.2, §6.5, §6.7). Parallax is one transform in the
  shared loop. Mobile: stacked composition above.
- **Tokens consumed (v2).** `--jacket`, `--ink`, `--gilt`, `--red`,
  `--ease-press`.

### 6.15 Praise & edition cards (page-family: cards)

- **What & why.** Where the theme needs cards — more praise than the
  back cover holds, other editions, the festival's other titles —
  they are set as a **contents-and-blurbs page**, not a card grid:
  praise entries as printed blurb blocks with hairline rules, edition
  entries as flap-style data blocks. The one licensed imperfection
  lives here: a single praise entry set 1° off-axis, the hand-placed
  blurb sticker (§4). Cards in this theme are print blocks that
  happen to repeat, and their motion is a bookseller's hand setting
  them down.
- **Structure.** `<ul class="blurb-list">`: each entry a block with
  top hairline rule, quote (Playfair italic 20px), source line, and —
  for edition entries — the data row (format, pages, price) in Lora
  600 tabular. Entries are separated by rules, never by boxes or
  shadows at rest.
- **Motion spec.** Entry: blocks land with §6.4's treatment when in
  the praise spread; in later lists, a 12px rise + fade, 450ms
  `--ease-press`, 90ms stagger. Hover (fine pointer): the block lifts
  3px with a hard 3px offset shadow in `--ink` at 18% — paper picked
  up by its edge; the off-axis entry, on hover, settles to 0° (you
  straighten the sticker you touch) and returns to 1° on leave.
  Click: whole entry is a link only for edition entries (to that
  edition's page, via §6.12's turn); praise entries are not links —
  praise is print, not navigation.
- **Choreography timeline (v2).** List at 70% viewport → entries land
  in DOM order, 90ms apart → off-axis entry lands last in its row
  with its rotation already set (it does not rotate in — it was
  placed crooked before you arrived) → hover beats as specced →
  scrolled-past: static print.
- **State matrix (v2).** *Rest:* ruled blocks. *Hover:* lift +
  shadow; off-axis straightens. *Focus:* edition links take the
  act-appropriate outline (§6.13). *Active:* lift releases to 1px for
  120ms (paper pressed). *Scrolled-past:* static. *Disabled:* full
  list at first paint.
- **Content merge.** The entries are the back cover's overflow and the
  editions' flap data — print matter in print form. The lift is a
  hand's, the rules are a printer's.
- **Failure fallback.** Watchdog per §6.4's law; hover shadow is
  decorative CSS, its absence changes nothing.
- **Reduced-motion variant.** Entries printed; hover lift becomes an
  instant rule-darkening; the off-axis entry stays at 1° (it is a
  placement, not a motion).
- **Breakpoints (v2).** ≥1200px: two columns. 768–1199px: two
  columns, quote 19px. <768px: one column; lift disabled (touch);
  the off-axis entry keeps its 1° — crooked is a property, not an
  effect.
- **Edge cases & failure modes (v2).** *An edition out of print:* its
  block carries a "Out of print" line in `--red-deep` where the price
  stood, and is not a link — the theme does not sell what the
  publisher cannot ship. *Festival variant (other titles):* entries
  carry cover-thumbnails in printed frames (§5 image treatment) —
  never the die-cut oval; the oval belongs to this book's author
  alone.
- **Accessibility spec (v2).** Real list semantics; edition links
  labelled with format + price in the link text's accessible name.
  The 1° rotation never applies to text below 16px (legibility rule).
  Contrast per §6.4's pairings.
- **Performance budget & mobile variant.** Transform/opacity only,
  ≤12 entries animating per list. Mobile: static-entry variant.
- **Tokens consumed (v2).** `--jacket`, `--flap-shade`, `--ink`,
  `--red-deep`, `--ease-press`.

### 6.16 The order form — "From the publisher" (page-family: form / conversion)

- **What & why.** The conversion section is set as the order slip a
  publisher prints at the back of a catalogue: in act one it sits on
  the back flap; in act two — where most orders will actually happen —
  it is a colophon-styled slip at the book's end, "From the
  publisher", with the edition's real price, format choices set as
  printed options, and a submit that behaves like posting the slip.
  The form's theatre is paper; its behaviour is a real checkout
  handoff, and the theme never lets the theatre touch the transaction.
- **Structure.** `<form class="order-slip">`: fields for format
  (radio group styled as printed options with gilt markers in act
  two, red in act one), quantity, email (for the publisher's
  confirmation), and the submit — a full-width block reading "Order
  from the publisher". Price summary updates as real text. Errors are
  printed beneath their fields in the errata voice (§12) — a
  correction, in red-deep, never a shake or a toast.
- **Motion spec.** Field focus: the field's bottom rule inks from
  hairline to full `--ink` (act one) / `--gilt` (act two) over 200ms.
  Format select: the marker prints (opacity + 1px settle, 150ms
  `--ease-press`). Submit: the slip takes a full impression — its
  ground deepens one step and the colophon mark (§6.10's device)
  stamps at its foot (scale 1.15 → 1, 200ms) — while the order sends;
  success replaces the slip with the publisher's confirmation block:
  order reference in tabular figures, what happens next, in the
  colophon voice. The stamp is 200ms of theatre after the real work
  is already submitted — never a gate on it.
- **Choreography timeline (v2).** Form enters → fields at rest (rules
  hairline) → focus beats per field → submit pressed → +0ms form
  disables, impression begins → server confirms → stamp lands at
  +200ms → confirmation block crossfades in (250ms) with the
  reference already in the DOM for AT → the act-two ribbon (§6.8)
  extends once, finally — the publisher's own bookmark placed in your
  copy.
- **State matrix (v2).** *Rest:* printed slip. *Hover:* submit block
  deepens one step (200ms). *Focus:* rule-inking + visible outline on
  radios/checkboxes (2px, offset 2px). *Active:* submit presses 1px.
  *Error:* field rule turns `--red-deep`, correction line prints
  beneath (static, persistent until fixed — print does not time out).
  *Submitting:* slip impressed, fields disabled. *Success:*
  confirmation block, permanent. *Disabled (no JS):* a plain working
  form posting to the same endpoint, errors returned as printed
  lines by the server render — the slip was always a form.
- **Content merge.** The slip is the publisher's actual order
  instrument, printed in the book's back matter where such slips
  live. Its price is the live price; its formats are the real
  editions (§6.6's gate keeps flap and form in agreement).
- **Failure fallback.** Submission fails: the slip un-impresses, a
  correction line prints at its head ("The order could not be sent —
  nothing was charged. Try again, or write to [publisher email]."),
  fields retain their values. No data is ever lost to the theatre.
- **Reduced-motion variant.** All states apply instantly; the stamp
  appears without scale; confirmation replaces without fade.
- **Breakpoints (v2).** ≥1200px: slip at 58ch in the act's column,
  two-column field pairs for name/quantity. 768–1199px: single
  column, 100% of the measure. <768px: full-bleed slip, inputs at
  17px (no iOS zoom), submit sticky to the slip's own foot — never
  to the viewport.
- **Edge cases & failure modes (v2).** *Pre-orders:* the submit reads
  "Reserve from the publisher" and the confirmation promises a
  publication-date email — the slip's voice changes with the book's
  state (§12), and the price block carries "Price at publication"
  when no final price exists. *Sold out:* the form is replaced by the
  reprint notice + a notify-me email field (same slip styling) — the
  theme never shows a dead form. *Multiple formats, one out of
  stock:* that radio is disabled with its reason printed beside it
  ("Hardback — reprinting"), never silently absent.
- **Accessibility spec (v2).** Native inputs throughout; labels are
  real `<label>`s set as slip apparatus; error lines linked via
  `aria-describedby`; the confirmation is a `role="status"` region
  whose text exists before the stamp animation plays. Touch targets
  ≥44px; radio markers never the only indicator (the option's text
  bolds when chosen). Contrast: `--ink` on `--jacket` 13.1:1 (act
  one slip), `--paper-text` on `--cloth` 8.7:1 (act two slip), error
  `--red-deep` 6.7:1 on cream / on cloth, errors use `--gilt-bright`
  5.6:1 with an accompanying "Correction:" prefix — colour never
  carries the error alone.
- **Performance budget & mobile variant.** No loops; transitions on
  state change only. Mobile: the full-bleed variant above.
- **Tokens consumed (v2).** `--jacket`, `--cloth`, `--ink`,
  `--paper-text`, `--red-deep`, `--gilt`, `--gilt-bright`,
  `--ease-press`.

### 6.17 Colophon footer (page-family: footer)

- **What & why.** The footer is the book's colophon — the page at the
  back where the publisher tells the truth about the object: what it
  was set in, when this edition was printed, who holds the rights,
  and — in this theme — the one door back to the jacket. It closes
  both acts' accounts: the house's device, the type credits
  (Playfair Display and Lora, named — a colophon names its types),
  the edition line, and the "Replace the jacket" link for the visitor
  who wants the shop again.
- **Structure.** `<footer class="colophon">` on `--cloth-deep`:
  centred apparatus column — device (§6.10's mark, static), the
  setting line ("Set in Playfair Display & Lora · Printed on the web
  in [year]"), the edition line (matching §6.11's figures exactly —
  the gate checks), legal line, and three text links (Imprint, Terms,
  Replace the jacket). Above it, act two's last chapter rule: a gilt
  hairline, full measure.
- **Motion spec.** The colophon arrives with §5's act-two reveal (12px
  rise, 500ms). The gilt hairline draws left-to-right over 600ms as
  it enters — the final gilt on the page, spent on the rule above the
  truth. Nothing else moves; the back of the book is the stillest
  part of it.
- **Choreography timeline (v2).** Footer at 80% viewport → rule draws
  (600ms) → colophon block rises (500ms, overlapping the draw by
  200ms) → rest. The §6.8 edge, at 100% since the last chapter, holds
  `--gilt-bright` throughout — the book is finished; its edges stay
  lit while you read the colophon.
- **State matrix (v2).** *Rest:* printed colophon. *Hover:* links
  take the gilt underline draw (220ms). *Focus:* `--gilt-bright`
  outline. *Active:* n/a beyond link press. *Scrolled-past:* n/a —
  it is the end. *Disabled:* static block, all links live.
- **Content merge.** The colophon is content — type credits, edition
  truth, rights — in the exact form books print it. "Replace the
  jacket" is the theme's own reset, phrased as the object's own
  action.
- **Failure fallback.** Static centred block; the rule is a border,
  drawn or not.
- **Reduced-motion variant.** Rule pre-drawn; block pre-risen.
- **Breakpoints (v2).** All sizes: the centred column holds (it was
  always narrow). <768px: the setting and edition lines stack with
  8px gaps; links at 44px touch height.
- **Edge cases & failure modes (v2).** *Edition figures change:*
  §6.11's rule applies — colophon, flap and form update in one edit
  or the build fails its gate. *Multi-book publisher page:* the
  colophon carries the house's line only; per-book edition lines
  belong to per-book pages — a colophon that lists six books is a
  catalogue wearing a colophon's clothes.
- **Accessibility spec (v2).** `<footer>` landmark; the device
  `aria-hidden` here (its labelled instance is §6.10's). Contrast:
  `--paper-text` on `--cloth-deep` 12.5:1; gilt line graphic-only.
- **Performance budget & mobile variant.** One border draw. Mobile:
  the stacked variant.
- **Tokens consumed (v2).** `--cloth-deep`, `--paper-text`, `--gilt`,
  `--gilt-bright`, `--ease-press`.

### 6.18 The misbound page (page-family: 404 / empty states)

- **What & why.** Every print run has a misbound copy — leaves
  gathered wrong, a gathering missing. The 404 is that copy: the
  visitor is told, in the theme's own grammar, that this leaf is
  missing from this binding, and is handed the contents (§6.13) to
  find their place again. It matters because error pages are where
  themed sites usually drop the object and show a website's apology;
  this one stays inside the book.
- **Structure.** A cloth-act page (a missing leaf is a matter of the
  book, not the jacket): `--cloth` ground, a chapter head reading
  "A missing leaf", one paragraph in the colophon voice, the contents
  list as the recovery instrument, and the gilt edge (§6.8) present
  but at 0% — no reading has happened here. Empty search/catalogue
  states reuse the grammar: "No copies of that title are bound in
  this edition." with the contents as the way back.
- **Motion spec.** None beyond the standard act-two reveal. A missing
  leaf does not perform.
- **Choreography timeline (v2).** Load → static page, contents gilt
  marker on no chapter (none is current — the honest state) → visitor
  chooses a chapter → §6.12's page turn carries them back into the
  book.
- **State matrix (v2).** *Rest:* the notice. *Hover / focus:* contents
  rows per §6.13. *Active:* n/a. *Disabled:* identical — the page is
  static by design.
- **Content merge.** The error is expressed entirely in the object's
  own terms and its recovery instrument is the book's own contents.
  No illustration of a broken book, no mascot — print grammar only.
- **Failure fallback.** The page *is* a fallback; its own fallback is
  that the contents links are real links on a static page.
- **Reduced-motion variant.** Identical.
- **Breakpoints (v2).** As §6.13's contents at each size.
- **Edge cases & failure modes (v2).** *A URL that exists in act one
  only* (jacket sections deep-linked after the jacket is off): the
  jacket is not re-dressed; the visitor lands at the endpaper zone
  with a line noting the jacket has been removed and a contents
  route onward — state honesty over state theatre.
- **Accessibility spec (v2).** The `<h1>` states the situation plainly
  ("This page is missing") before the themed line — AT users get the
  fact first, the grammar second. Contrast per act two.
- **Performance budget & mobile variant.** Static. Mobile: contents
  section variant.
- **Tokens consumed (v2).** `--cloth`, `--paper-text`, `--gilt`.

---

## 7. Page application map

- **Home (the book's page).** The full two-act structure as specced:
  jacket (nav, cover, spine, praise, flap) → endpapers → cloth
  (contents, chapters, plates, order slip, colophon). This is the
  only page type that performs the slide-off; every other page type
  *inherits an act* instead.
- **Listing (the publisher's list / festival programme).** Cloth-act
  skin only: a contents-page listing (§6.15's edition blocks) under a
  quiet cloth head with the house device. No jackets per title — a
  list is a bound thing already. Each entry links via page turn
  (§6.12) to its book page, where that book wears its own jacket.
- **Detail (a chapter, an essay, a review).** Opens inside the book:
  cloth ground, chapter furniture, drop cap if it opens a chapter,
  gilt edge running. Jacket-act detail pages do not exist — detail is
  read, and reading happens in the cloth.
- **About (the author / the house).** Author about: act two, with the
  portrait reprinted as a chapter plate (§5 image treatment) — never
  in a second die-cut oval; the oval happened once, on the cover.
  House about: the colophon expanded to a full page (§6.17's grammar
  at length) — a publisher's about page *is* its colophon, enlarged.
- **Contact / checkout equivalents.** The order slip (§6.16) is the
  conversion page; contact is a "Write to the publisher" leaf in the
  same slip form-family, cloth act, with the house's real postal
  address printed — publishers have addresses; contact forms that
  hide them are websites, not publishers.
- **Launch/teaser page (pre-publication).** Jacket act only, ending
  at the endpaper zone with a reserve slip (§6.16's pre-order
  variant) where the cloth would begin, and the line "The book itself
  arrives on [date]." The theme does not fake a second act it does
  not yet have (§6.13's edge case).

---

## 8. Worked examples

### 8.1 The hero — a novel's front cover, end to end

*The book: "The Salt Meridian" by A. Okafor, second edition, Hartley &
Vine.* The page loads. Fonts resolve within the 300ms cap; the
assembly (§6.2) arms. The cover slides in from +18px on `--ease-shelf`
— cream ground, the author line "A. OKAFOR" in spaced Lora caps at the
head (the publisher's real cover puts the name first), then the title
in Playfair 800 at 104px, its middle word "Meridian" carrying the one
foil-gilt word (§6.14). At +450ms the spine settles at the left edge —
cloth green, red label band, the title vertical, the house device at
its foot. At +500ms the standfirst's two lines uncover behind their
masks. At +700ms the die-cut oval at the cover's right third begins
opening; the author's face resolves from 6px blur as the ellipse
reaches full at +1400ms, credit line fading in beneath. The praise
spread is still below the fold; on the cover itself, the foot carries
the single cover quote — "A first novel of uncommon assurance." —
*The Review of Books*, landing at +1500ms, and at +1350ms the sheen
sweep has already crossed the whole cover once, laminate over title,
face and quote alike. The publisher's name sits at the foot: HARTLEY
& VINE. The visitor scrolls: the cover parallaxes at 0.92× against
the praise spread's 1.0×, the spine's gilt band begins filling. They
have not clicked anything. They have been handed a book and read its
cover — which is all a cover has ever asked.

### 8.2 Mid-page — the turn itself, beat by beat

The visitor has read the praise (six quotes, landed in billing order,
§6.4), unfolded the flap (price £20.00, barcode digits 14032026 — the
14 March 2026 publication date, captioned; print run counted to
2,500, §6.11), and folded it back. Scrolling on, the sections narrow:
the page's stance tightens from 1240px toward the book's 1080px. The
endpaper zone enters — marbled, cloth-deep, one italic line: *"The
jacket has done its work."* (§12's paired line, first half.) The
swirl drifts, settling. The zone's midpoint crosses the viewport's
middle: the jacket layer — cover, spine, praise, flap, gloss and all
— begins its 900ms slide on `--ease-whisper`, edge shadow blooming
and dying, the swirl peaking in the vacated gutter. The spine's gilt
band, at 100%, leaves with it. Beneath: nothing moves. Chapter One is
already there — gilt chapter head, a Playfair drop cap on the first
paragraph, the contents rail fading in at the left margin, the
page-edge strip at the right at 0%, about to begin its long
brightening. The second half of the paired line is the chapter's
epigraph: *"Now the book."* The visitor's scroll never paused; the
turn took 1.25 seconds and no input. They are no longer shopping.
They are reading — and the page's typography has changed its voice
(§3's law) to prove it.

### 8.3 Conversion — ordering from the cloth act

Deep in act two, after chapter three, the order slip (§6.16) sits in
the reading column like a publisher's insert. It shows the live
price — £20.00, agreeing with the flap's printed price (the gate's
agreement check made that true at build; if a reprint changes the
price, both change in one edit). The visitor chooses Hardback (the
radio's gilt marker prints in, 150ms), quantity 2 — the summary line
recomputes as plain text: "2 copies · Hardback · £40.00". Email
field: focus inks its rule gilt over 200ms; a mistyped address draws
the errata line beneath in the correction voice — "For 'gmial' read:
the address as you meant it — please check the spelling." — static,
patient, unshaken. Corrected, they press "Order from the publisher".
The slip impresses; the order sends; on confirmation the house device
stamps at the slip's foot and the confirmation block is already in the
DOM for their screen reader: "Order H&V-2214. Two copies of The Salt
Meridian, hardback. A confirmation is on its way to your address; the
books follow within three working days." In the margin, unnoticed
until later, the bookmark ribbon has extended one final notch — the
publisher has placed a marker in the visitor's copy. The transaction
was a web form. The memory is of posting a slip to a publisher.

---

## 9. Anti-slop — what makes THIS theme look cheap

1. **The jacket and the cloth are the same design in two colours.**
   Symptom: act two is act one with a green background. Cause: the
   builder themed a palette swap instead of an object change. Cure:
   §3's type law, §4's stance narrowing, §5's act discipline (no
   parallax, no gloss, no loops in act two) — if removing the
  slide-off leaves two interchangeable halves, rebuild the cloth act
   as a book, not a section.
2. **Gilt body text.** Symptom: paragraphs in gold on green. Cause:
   gilt mistaken for a brand colour. Cure: gilt is display-only,
   ≥24px, rationed to ≈3% (§2, §3); body is `--paper-text` at 8.7:1.
3. **An invented print run.** Symptom: "Printed in a run of 10,000"
   because it sounded impressive. Cause: counters treated as
   decoration. Cure: §6.11's law — real figures or no figures; the
   gate audits them against the edition line.
4. **A barcode with random digits.** Symptom: a barcode graphic from a
   stock set. Cause: the flap's signature detail done as clip-art.
   Cure: the digits encode the publication date, captioned (§6.6);
   no confirmed date, no barcode.
5. **Praise inflation.** Symptom: nine quotes, two from the author's
   friends, one from a source that reviewed a different book. Cause:
   the back cover treated as a testimonial wall. Cure: six maximum,
   one per masthead, billing order is editorial order (§6.4, §12).
6. **The slide-off reveals a landing page.** Symptom: under the jacket
   sits a hero, three feature cards and a logo cloud. Cause: act two
   built as marketing, not as the book. Cure: the cloth opens
   mid-chapter (§6.1) — chapter head, drop cap, text. If it could be
   any product's dark section, it fails §1's law.
7. **Gloss everywhere.** Symptom: sheen on buttons, cards, the cloth
   act. Cause: a nice gradient looking for work. Cure: gloss is the
   jacket laminate's property — cover only, act one only (§6.7).
8. **Rounded corners and soft shadows.** Symptom: the "book" looks
   like a SaaS dashboard in cream. Cause: UI defaults leaking into a
   print object. Cure: square corners, hairline rules, hard offset
   shadows only (§6.15); print is print (§5 image treatments).
9. **The jacket re-dresses itself.** Symptom: scrolling up replays
   the whole first act. Cause: reveals and the set piece built as
   scroll-symmetric effects. Cure: removal is one-way (§6.1); quotes
   stay landed (§6.4); the only way back is the colophon's deliberate
   link.
10. **Two books' furniture mixed.** Symptom: the spine title, cover
    title and colophon disagree in wording or edition. Cause: content
    assembled from different sources. Cure: §10's agreement check —
    one book, one title, one edition, everywhere it is named.

---

## 10. Quality gate

Blocking items — all must pass; standard items — at least 9 of 11.

**Blocking.**

1. **JS-off test:** with JavaScript disabled, the full page reads in
   order — jacket sections stacked, then cloth sections; the flap
   shows both faces; the form posts; no content is missing.
2. **Turn reachability:** the cloth act is reachable by the button,
   by the anchor, and by keyboard focus order, with the slide
   animation disabled in each case.
3. **One-way & watchdog:** the slide-off never replays on scroll-back;
   a forced JS failure mid-slide leaves the jacket fully on or fully
   off within 1200ms, never half-off.
4. **Truth audit:** print run, edition size, price, publication date
   (incl. the barcode digits) and edition line agree across flap,
   form, skeleton and colophon, and trace to publisher-supplied data.
5. **Act discipline:** no gloss, parallax or ambient loop exists in
   act two (DOM/CSS audit); no red in act two except the ribbon; no
   gilt body text anywhere (computed-size audit: gilt text ≥24px
   only).
6. **Title agreement:** cover title, spine title, contents and
   colophon name the same book and edition, character for character.
7. **Cursor & cover audit:** system cursor unchanged; no animated
   element overlaps text at five scroll depths in either act.
8. **Contrast audit:** the §2 pairings hold at every state, incl.
   `--red-deep` sources at small sizes and gilt-bright errors on
   cloth (§6.16).

**Standard.**

9. Assembly completes ≤2s on a mid-range connection; sheen cancelled
   if the cover is <30% visible at its beat.
10. Slide-off: cloth layer moves 0px during the set piece (measured).
11. Counters land on the true figures, formatted at every frame,
    exactly once per session.
12. Gilt edge and ribbon agree with the contents' current-chapter
    marker at all times.
13. Page transitions ≤600ms (act one) / ≤500ms (act two), disarmed on
    ≤3G/save-data, latest-navigation-wins.
14. Skeleton minimum display 300ms; error state uses the printed
    misprint line, never a toast.
15. Dark scheme: jacket sheet's computed ground is still `--jacket`;
    act two deepens to `--cloth-deep` tokens only.
16. The five-second test, jacket edition: a first-time viewer says
    "it's the book's own cover" — not "a book-themed website".
17. The five-second test, cloth edition: after the turn, the same
    viewer says "now I'm inside the book".
18. Print stylesheet: `@media print` removes gloss, spine rail, gilt
    edge and overlays; the cloth act prints as clean pages — the
    theme's final proof the paper was real.
19. Forced-colours mode: the foil title word resolves to solid
    `--red`; the die-cut oval remains a visible frame.

**Minimum bar, in one line:** a build that passes the blocking eight
has earned the right to be judged as a book; anything less is a
book-themed website, and it goes back to the binder.

---

## 11. Component inventory

Every component a real site in this theme needs, with its treatment.
Components the theme refuses are listed with their replacement —
refusals are part of the inventory.

- **Buttons.** Act one: printed blocks — `--red` ground, `--jacket`
  text, square corners, press = 1px translate + ink deepening (never
  a ripple). Act two: gilt-outlined blocks on cloth, fill on hover.
  One primary per view; the "Remove the jacket" button is act one's
  primary by definition.
- **Text inputs.** Slip fields (§6.16): transparent ground, hairline
  bottom rule that inks on focus, label set as apparatus above.
  No floating labels, no filled boxes — a slip is lines on paper.
- **Selects.** Native `<select>` restyled as a printed line with a
  gilt marker; where options are few (formats), radios replace it
  (§6.16).
- **Radios / checkboxes.** Radios are printed options: a square
  marker that fills with the act's accent when chosen, the option
  text bolding with it (never colour alone). Checkboxes (gift wrap,
  notify-me) are tick boxes drawn as slip squares, tick in the
  editor's hand style — no, in print: a filled square. Print does not
  have a hand; the tick is a filled square and §12's voice covers the
  warmth.
- **Tables.** Contents tables and edition data: ruled rows, dotted
  leaders where a number must be led to (§6.13), tabular Lora
  figures, no zebra striping — books rule their tables, they do not
  shade them.
- **Badges.** One only: the edition badge ("Second edition") set as a
  printed band across the cover's corner — a band, not a pill. Stock
  states are lines of type ("Reprinting"), never badges.
- **Alerts.** Printed correction lines (§6.16's errata voice) placed
  at the head of the region they correct. Toasts are **refused** —
  books do not interrupt; corrections wait on the page to be read.
- **Pagination.** Chapter-to-chapter: "Next leaf →" / "← Previous
  leaf" links with leaf numbers, via §6.12's turn. Numbered page
  pills are refused; a book's pagination is its contents (§6.13).
- **Modals.** Refused in act two entirely. In act one, the flap
  (§6.6) is the theme's only overlay-like gesture, and it is a part
  of the object, not a dialog. Anything that would be a modal becomes
  a leaf (a dedicated page reached by turn) or a flap.
- **Tabs.** Refused. A book has no tabs; parallel matter is a
  contents list, and editions are §6.15 blocks.
- **Accordions.** The contents' part-groupings may collapse on mobile
  via native `<details>` (§6.13) — the one licensed accordion, styled
  as print, because a contents page folding is a physical act.
- **Search.** A "Find in this book" leaf: slip-styled input, results
  as contents rows with leaf numbers (§6.13 grammar). No search
  overlay.
- **Progress.** Act instruments only (§6.3 band, §6.8 edge/ribbon).
  A generic progress bar is refused — the book already owns two
  better ones.
- **Tooltips.** Refused. A term needing explanation gets a footnote —
  set small, beneath a hairline, in the margin: the book's own
  apparatus for exactly this.
- **Dividers.** Hairline rules (act one), gilt hairlines (act two,
  rationed), torn nothing — this book is new; its dividers are
  printer's rules.
- **Images / plates.** §5's treatments: printed frames in act one,
  gilt-ruled plates in act two, the die-cut oval reserved (§6.5).
- **Loader.** §6.12's blank-cover skeleton; a spinner is refused in
  both acts.
- **Breadcrumbs.** Refused. Position in a book is given by the
  contents and the running head; act two sections carry a running
  head line ("The Salt Meridian · Chapter Three") in place of a
  breadcrumb trail.

---

## 12. Content & copywriting voice

The theme has two voices, one per surface, and §3's law applies to
words as to type: **the jacket sells, the cloth reads.**

**Jacket voice (act one).** Confident, compressed, present-tense.
Cover and flap copy is written like real jacket copy: short
declarative sentences, specific nouns, no adjectives the book cannot
cash. Headlines are claims the text will keep. Praise is quoted
exactly as published, attributed exactly, never trimmed into a
different opinion (§6.4's content rules are voice rules).

- ✓ "A first novel of uncommon assurance." — *The Review of Books*
- ✗ "An absolutely stunning, must-read masterpiece!!!"
- ✓ Flap: "A. Okafor was born in Enugu and lives in London. This is
  her second book."
- ✗ Flap: "Meet the incredible author behind this game-changing
  literary phenomenon!"

**Cloth voice (act two).** Unhurried, exact, warm at reading distance.
Chapter heads are titles, not hooks. The colophon and confirmation
voices are the publisher speaking plainly: what was made, what will
happen next, by when.

- ✓ Confirmation: "Order H&V-2214. Two copies, hardback. The books
  follow within three working days."
- ✗ Confirmation: "Yay! Your order is in! 🎉 Get excited!"
- ✓ Error: "For 'gmial' read: the address as you meant it — please
  check the spelling."
- ✗ Error: "Oops! That email looks wrong 😬"

**The paired line.** The theme's signature sentence-pair, written per
book, never templated: the endpaper zone's line closes the jacket's
argument, and the first chapter's epigraph answers it (§8.2's
example: *"The jacket has done its work." / "Now the book."*). Rules:
each half ≤7 words; the first half must be true of the jacket, the
second must be an opening, not a slogan; neither may mention the
website.

**Labels & fixed strings.** Buttons say what the object does:
"Remove the jacket", "Order from the publisher", "Reserve from the
publisher", "Replace the jacket". Banned words across both acts:
*stunning, masterpiece, game-changing, dive in, unlock, content,
users, leverage, exciting* (as filler). Owned words: *leaf, edition,
printing, cloth, jacket, colophon, from the publisher*. Numbers are
figures with words around them ("Second printing", "Edition of
1,500") — never bare metrics (§3's data rule).

**Empty states.** In the object's grammar (§6.18): "No copies of that
title are bound in this edition." — followed by the way back. An
empty state that apologises like a web app ("Oops, nothing here!")
has left the book.

---

## 13. Full-page scroll choreography map

The home page, top to footer, in order. (J = jacket act, E =
endpapers, C = cloth act.)

1. **Load (J).** Assembly (§6.2): cover in, spine settles, die-cut
   resolves, cover quote lands, sheen sweeps once. Jacket nav
   present; spine band at 0%.
2. **Cover dwell (J).** Gloss idles (9s loop, 40%); pointer brings
   §6.7's light and tilt. Parallax armed: cover 0.92×.
3. **Praise spread (J).** Quotes land in billing order (§6.4);
   colophon mark draws itself 200ms after the last (§6.10). Spine
   band ≈40%.
4. **The flap (J).** Counters count on first sight (§6.11). The
   visitor may unfold (§6.6) — price, barcode, edition — and refold.
   Spine band ≈85%.
5. **Last jacket line (J→E).** The endpaper zone enters; swirl
   drifts (§6.9); the paired line's first half is read. Spine band
   at 100%.
6. **The turn (E).** Midpoint crosses: slide-off, 900ms (§6.1);
   swirl peaks in the gutter; jacket instruments leave with the
   layer.
7. **The opening (C).** Contents rail fades in (+950ms), current
   chapter gilt; gilt edge at 0% on the right; chapter one: gilt
   head, drop cap, epigraph — the paired line's second half.
8. **Reading (C).** Chapters pass: ribbon extends per chapter
   (§6.8), contents marker crossfades in step, plates scale-in-frame,
   gilt edge brightens continuously. No parallax, no loops — quiet.
9. **The slip (C).** Order form (§6.16) in the reading column; its
   beats are interaction beats, not scroll beats.
10. **The colophon (C).** Final gilt rule draws; colophon rises
    (§6.17); the edge holds full gilt-bright. The book is finished;
    "Replace the jacket" waits at the foot for anyone who wants the
    shop again.

**Reverse pass.** Scrolling up through act two: the gilt edge
retreats with position; the ribbon keeps its longest reach (§6.8's
documented asymmetry). At the endpapers, the jacket does **not**
return (one-way law); the zone sits static, its line still true —
the jacket *has* done its work.

**Jump-scroll catch-up.** Landing deep in act two (anchor, find,
restored position): the slide is skipped silently, quotes and
counters are set landed/true, instruments read current position —
the page is always found in its true state, never mid-ceremony.

---

## 14. Whole-page performance budget

- **Asset ceilings.** Total page ≤ 1.1MB: fonts ≤ 120KB (Playfair
  Display 700/800 + italic 500, Lora 400/600 + italic — subset to the
  book's character set where the platform allows), author portrait
  ≤ 180KB, endpaper SVG ≤ 30KB (it is one pattern, reused), JS
  ≤ 25KB gz, CSS ≤ 30KB gz. The jacket layer adds no image of its
  own — a jacket is type and one photograph.
- **Frame budget.** One shared rAF loop owns: sheet parallax (act
  one), spine band, gilt edge, ribbon, gloss lerp. Combined theme
  cost ≤ 2.5ms/frame on a mid-range Android; at most 3 transforms
  composited per frame in act one, 2 in act two. Sustained <40fps
  over 2s triggers the degradation ladder.
- **Long-task limits.** No task > 50ms after load; the assembly's
  work is split across its beats by design. Counters and draws never
  run in the same frame as a scroll scrub update if the frame budget
  is exceeded — scroll wins; print waits a frame, as print can.
- **Cut order (when the budget is exceeded).** 1. Idle sheen loop.
  2. Sheet parallax (layers lock to 1.0×). 3. Gloss tilt (gloss
  becomes static). 4. Endpaper swirl drift (pattern static). 5.
  Counters set instantly. **Never cut:** the slide-off's completion
  guarantee, the watchdogs, content visibility, the form's function,
  the gilt edge's truth (it may step, never lie).
- **Load metrics.** LCP = the cover title block (text, not image):
  ≤ 2.0s on 4G. CLS ≤ 0.02 — the jacket layer is sized by the cover's
  own aspect before assembly arms. INP ≤ 200ms; the flap toggle
  responds within one frame.

---

## 15. Build-order checklist

1. Static page first: both acts in document order, fully readable
   with no JS and no CSS animations — pass §10 items 1–2 before any
   motion exists.
2. Tokens and type: palette (§2), type scale and the act law (§3),
   layout stances (§4).
3. The cover (§6.14) and spine (§6.3) as print: no motion, checked
   against a photograph of a real jacket for proportion.
4. Praise spread (§6.4/§6.15) and the colophon mark (§6.10), static.
5. The flap (§6.6) with both faces and the no-JS stack; barcode digits
   verified against the publication date.
6. Counters (§6.11) wired to the publisher's real figures; edition
   agreement across flap/form/colophon checked (§10 item 4).
7. Cloth act: contents (§6.13), chapters, plates, gilt edge (§6.8)
   scrub — the book must read beautifully before its jacket can come
   off.
8. The endpaper zone (§6.9) and the slide-off (§6.1) with its three
   reachability guarantees and watchdog.
9. Assembly (§6.2), gloss (§6.7), parallax — act one's life, added
   last to act one, in that order.
10. Transitions and skeleton (§6.12), dual-mode, with slow-network
    disarm.
11. The order slip (§6.16) end-to-end against the real endpoint,
    including the printed error path.
12. Colophon (§6.17), 404 (§6.18), dark scheme (§2), print
    stylesheet.
13. Reduced-motion pass: every element's variant exercised, one by
    one, against §6.
14. Full §10 gate run with evidence (JS-off load, forced-failure
    slide, screenshot pixel audit for gilt/red ration).

*End of theme #22 — Dust Jacket, expanded to the v1 + v2 standard.*
