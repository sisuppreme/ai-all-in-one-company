# 30. First Edition — Expanded (v1 + v2)

> Expansion of theme #30 from `themes-026-050.md`, written directly to
> the full standard: the v1 10-part structure plus the v2 deepening
> layers (per-element choreography timelines, state matrices, breakpoint
> behaviour, edge cases, accessibility specs and token lists; per-theme
> component inventory, copywriting voice, three worked examples, scroll
> choreography map, performance budget, build-order checklist).
> Identity preserved exactly: the same concept, the same four palette
> anchors, the same two typefaces, the same nine signature elements —
> deepened, never redesigned — plus nine page-family elements.

## 1. Concept & world

Most websites are printouts: infinitely reproducible, identical for
every visitor, owned by no one. This theme is the opposite wager. The
site behaves like **copy No. 1 of 500** — a numbered artefact from a
limited edition, bound in buckram, gilt on its edges, with a bookplate
inside the front cover and an edition statement at the back that says
exactly how many copies exist and how this one came to be yours. Every
visitor's copy is *theirs*, numbered at the door: the bookplate stamps
in on arrival, the number types itself into the blank, and when the
visitor returns, the site greets the same copy — "Copy No. 212, again.
The dog-ear is where you left it."

The world is the fine-press book, treated as a complete interface
vocabulary rather than a skin. The page has a **spine** (a raised-band
rail pinned down the left for the whole reading), **leaves** (pages
turn, they do not navigate), **gatherings** (chapters, each opening
with an illuminated drop cap and closing with the printer's ornament),
**plates** (images live in gilt frames and are called plates, with
captions), **endpapers** (marbled paper is the divider material
between gatherings), and a **colophon** (the footer is an edition
statement, not a sitemap with a logo). Progress through the site is
not a percentage; it is the gilt on the page-edge filling downward and
a folio in the margin that reads "leaf 7 of 23" — depth in a volume,
measured the way a reader's thumb measures it.

**The theme's one law: the number is real, or the number is absent.**
The copy number is per-visitor state, drawn once, stored locally,
stable across visits (§6.1). The copies-remaining figure in the
colophon is either a true figure supplied by the publisher or it is
not printed at all (§6.8). A First Edition build that invents scarcity
— a random "only 3 left" generated in the browser, a copy number that
changes between visits — has not bent the theme; it has broken the
only promise the theme makes, and the quality gate (§10) fails it on
sight. Everything else in this theme is craft. That one is ethics.

**Numbering is the interaction model.** Because the copy is numbered,
everything the visitor does is done *to their copy*: the dog-ear they
fold stays folded (§6.4), the chapters they finish are gilt on the
edge (§6.6), the copy they reserve carries their number (§6.14). The
site does not have users; it has owners of copies. That is why the
theme fits offers that are genuinely limited, genuinely authored, or
genuinely kept — and why it curdles instantly around anything mass,
urgent or disposable.

**Best-fit sites and audiences.**

- Limited and numbered editions of anything: small-batch physical
  goods with real edition sizes, fine-press and print-on-demand books,
  numbered art prints, small-run vinyl, allocated wines and whiskies —
  anywhere the edition size is a fact the maker will state in writing.
- Authors, studios and ateliers presenting a body of work as a volume:
  a portfolio structured as chapters, a studio's collected projects
  with an edition statement instead of an "about us" blurb.
- Memberships and courses sold as a fixed cohort ("the 2027 printing,
  200 places") where the cohort size is real and the material is
  organised as chapters with plates.
- Anniversary and commemorative sites: a firm's fiftieth year, a
  journal's hundredth issue — one volume, made once, kept.
- Long-form reading products: essays, serialised fiction, research
  reports — anywhere "leaf n of N" is a truer progress measure than a
  scroll percentage and a dog-ear is a truer bookmark than a database
  row.

**When NOT to use it.**

- For anything whose scarcity would be theatre. If the edition is not
  actually limited, the bookplate is a lie with good typography; use
  another theme.
- For high-churn, high-volume commerce: catalogues that update daily,
  marketplaces, price-comparison. A book is finished when it is bound;
  content that changes hourly cannot keep an edition statement honest.
- For dashboards, tools and anything task-first. The theme's pace is a
  reader's pace — furniture assembles, leaves turn in 650ms, ornaments
  draw. A user trying to *do* something in a hurry will feel bound in
  buckram.
- For breaking news or anything urgent. "Finis" is the last word of a
  finished thing; nothing about this theme can say "just in."
- Where the audience cannot be assumed to return. Half the theme's
  value — the same number, the kept dog-ear, the greeting — accrues on
  the second visit. A one-visit landing page gets the costume without
  the covenant.

## 2. Palette

Four anchors, inherited unchanged. The palette is a bound volume seen
from across a desk: maroon buckram, cream endpaper, gilt, ink. Nothing
else is admitted; every other colour on the page is one of these four,
tinted, shaded or woven into the marble (§6.7).

| Token | Hex | Role | Usage ratio | Pairing & contrast notes |
|---|---|---|---|---|
| `--buckram` | `#5E2126` | The binding: spine rail, covers, chapter-title blocks, buttons, the order form's frame | ~9% of pixels | On cream 10.27:1 — passes AAA for text; cream on buckram likewise 10.27:1, so the rail may carry cream lettering at any size. The only saturated ground the page allows itself. |
| `--cream` | `#F3EBD8` | The leaf: every page background, every reading surface | ~84% of pixels | Endpaper cream — warm, matte, never swapped for `#FFFFFF` anywhere, including form fields and the 404 leaf. Ink on it: 14.07:1. |
| `--gilt` | `#C2A14D` | The gilding: page-edge fill, drop-cap illumination, plate frames, ornament strokes, light-catch | ≤4% of pixels, hard ration (§9) | On cream only **2.08:1** — decorative metal, never text on cream at any size. On buckram 4.94:1 (AA at all sizes) and gilt-bright on buckram 6.89:1 — so gilt lettering is legal *only* on the binding. A gilt word on a cream leaf is a gate failure (§10). |
| `--ink` | `#221D18` | The text: body, headings on cream, folios, rules at full strength | ~3% of pixels | On cream 14.07:1; on cream-deep 12.62:1. The only colour body text may be set in. Warm black, never pure `#000`. |

**Derived tokens** (computed from the anchors; never new hues):

| Token | Derivation | Use |
|---|---|---|
| `--buckram-deep` | `#4A1A1E` (buckram darkened ~18%) | The spine rail's shadow edge and raised-band shading; button pressed state. On cream 12.13:1. |
| `--gilt-bright` | `#DCC078` (gilt lightened toward the light) | The specular end of every gilt gradient: light-catch (§6.3), the page-edge flash (§6.9), the illuminated cap at full rise (§6.2). On buckram 6.89:1. |
| `--gilt-deep` | `#8A6D2F` (gilt darkened toward ink) | The shadow end of gilt gradients and the drop cap's unlit base. On cream 4.10:1 — AA for large text only, which is all it is ever used for (caps ≥56px). |
| `--cream-deep` | `#EADFC6` (cream darkened ~4%) | Endpaper shadow: card grounds, the errata slip (§6.16), the tissue guard's tint (§6.12), skeleton leaves (§6.18). Ink on it 12.62:1. |
| `--hairline` | `--ink` at 16% over `--cream` | Ruled lines, leader dots (§6.13), plate-frame inner rule. Decorative only. |
| `--marble-vein` | `--buckram` at 34% over `--cream` | The dominant vein colour in the marbled endpaper (§6.7). |
| `--marble-gilt` | `--gilt` at 42% over `--cream` | The fine vein colour in the marble; the only place gilt appears as a field rather than a line. |

**Dark-mode behaviour — the lamplight ruling.** A book does not
invert at night; its page gets warmer and dimmer under a lamp, and
that is all that happens here. Under `prefers-color-scheme: dark`:
`--cream` steps to `#E9DCBE` (ink on it still 12.29:1), `--buckram`
deepens to `--buckram-deep` `#4A1A1E`, gilt brightens one step toward
`--gilt-bright` so the edge still catches, and the marble veins deepen
by the same proportion. The page stays a light page — a visitor
reading in the dark gets a lamp, not a black book. A build that ships
a true dark theme (dark ground, light text) has rebound the book in
the wrong material and fails §10.

**Selection.** Text selection is gilt at 30% over cream with ink text
— the reader's thumb has brushed the gilding. The spine rail and
colophon invert the pairing: cream selection on buckram.


## 3. Typography

Two faces, inherited: **Playfair Display** for titles and display,
**Source Serif 4** for everything else — text, apparatus, forms,
figures. No third face is admitted. There is no sans anywhere in the
book: no sans for buttons, no sans for "UI", no mono for numbers. A
fine edition is set in the faces it is set in, and the interface
inherits them.

| Role | Face & settings | Size / leading | Notes |
|---|---|---|---|
| Title-page title | Playfair Display 700, title case, tracking −0.01em | clamp(2.6rem, 6vw, 4.4rem) / 1.04 | The largest type on the site; set once per volume, on the title page (§6.11) only. |
| Chapter title | Playfair Display 600 | clamp(1.9rem, 3.4vw, 2.7rem) / 1.12 | Always preceded by its chapter numeral in gilt-on-buckram or small caps (§6.17). |
| Drop cap | Playfair Display 700, gilt over ink (§6.2) | 4.35em, spanning exactly 3 lines of body | Real text, never an image, never an SVG letter (§9). |
| Section head within a chapter | Source Serif 4 600, small caps, tracking 0.08em | 1.05rem / 1.3 | The book's internal furniture is serif small caps — the "apparatus voice." |
| Body | Source Serif 4 400 | 1.125rem (18px) / 1.78 | Measure capped at 38rem (§4). Old-style figures in prose. |
| Plate caption | Source Serif 4 italic 400 | 0.94rem / 1.5 | Always begins "Plate n." (§6.12); the caption is part of the plate. |
| Folio & running head | Source Serif 4 500, small caps, tracking 0.1em | 0.8rem | "Leaf 7 of 23" — words, never "7/23", never a percentage (§6.17). |
| Edition statement | Source Serif 4 400, centred, small caps for its fixed lines | 0.95rem / 1.9 | The colophon's voice (§6.15): bibliographic, declarative, no marketing verbs. |
| Figures (counters, numbers) | Source Serif 4 500, old-style figures | inherits context | The copy number and copies-remaining count (§§6.1, 6.8) are set in old-style figures — the book's own numerals, never tabular, never mono. |

**Type laws.**

1. **Gilt is never a text colour on cream.** Gilt appears as type
   only as the drop cap's illumination over its ink underlay (§6.2)
   and as lettering on buckram (4.94:1). Any other gilt word is set in
   ink and given a gilt rule, not gilt ink.
2. **Numerals are words where the book would use words.** "Copy No.
   212", "leaf seven of twenty-three" in prose contexts; figures only
   inside the apparatus (folios, counters, the edition statement's
   counts). Percentages do not exist in this theme.
3. **"Finis" is set once, in Playfair italic, at the foot of the final
   chapter** (§6.5) — nowhere else, in no other context, including
   buttons, footers and empty states. A "Finis" in the footer of every
   page is a gate failure.
4. **Small caps are real small caps** (`font-variant-caps:
   all-small-caps` or the face's `smcp`), never uppercase text with
   tracking faked over it, in the apparatus voice: running heads,
   folios, labels, the edition statement's fixed lines.
5. **Italics are for the book's asides**: plate captions, the greeting
   line ("Copy No. 212, again…"), errata-slip corrections (§6.16),
   foreign words. Buttons and labels are never italic — a binder does
   not italicise an instruction.

## 4. Layout language

**The leaf and its margins.** The page is a leaf from a bound volume,
and its geometry is a book's geometry, not a grid system's. On desktop
the composition is deliberately asymmetric: a **72px spine rail**
pinned at the left for the entire scroll (§6.10), the reading column
centred in the remaining width at a **38rem measure**, a wide
fore-edge margin to the right of the text that carries the folios
(§6.17), the dog-ear corner (§6.4) and the reader's thumb-room, and a
**10px gilt page-edge strip** fixed at the viewport's right edge
(§6.6). The margins are not leftover space; in a book the margin is
where the apparatus lives, and here it works for its living.

**Gatherings, not sections.** Content is organised in chapters
("gatherings" in the binding sense — the folded sheets sewn together).
Each gathering has the same anatomy, and the rhythm of the page is the
rhythm of that anatomy repeating: a chapter opening (numeral, title,
illuminated drop cap), the text with its plates, a closing ornament
(§6.5), and — between gatherings — a marbled endpaper divider (§6.7),
the only full-bleed surface on the page. A build that varies the
anatomy per chapter for "visual interest" has unbound the book; the
variety lives in the content, the plates and the illumination, never
in the furniture.

**Spacing rhythm.** A 8px base unit, but the meaningful rhythm is
typographic: vertical space is counted in body lines (1.78 leading =
32px). Chapter openings take 4 lines above the numeral; the ornament
sits 3 lines below the last paragraph; endpaper dividers are 38vh —
tall enough to be a leaf turned, short enough not to be a wall.
Horizontal rules are hairlines (`--hairline`) at full measure, or gilt
at 64px and never longer: a long gilt rule is a gate failure (§9).

**Density.** Low, and proudly. One plate per chapter at most on
listing pages; detail pages may carry one plate per major section. The
cream needs room to be cream — a First Edition page that fills its
margins with widgets has confused a book with a dashboard. The single
exception is the contents leaf (§6.10), which is dense the way a
contents page is dense: lines, leaders, folios.

**The spine rail is furniture, not a sidebar.** It carries the raised
bands, the contents (§6.10) and nothing else — no logo lockups beyond
the volume's title set vertically or in small caps, no social icons,
no search box. Search, where a build needs it, lives on the contents
leaf as "Index" — books are searched by their index, at the back.

**Responsive geometry.** ≥1200px: as above. 768–1199px: the rail
narrows to 56px, the measure stays 38rem, the fore-edge margin shrinks
to 48px and folios move inline (§6.17). <768px: the rail leaves the
left edge and becomes a 44px spine strip across the top (§6.10), the
measure becomes the viewport minus 40px, the page-edge strip narrows
to 6px, and the dog-ear grows to a 48px touch target. The book gets
smaller; it does not become a different object.


## 5. Full motion system

Every motion term from the library's vocabulary, translated into the
vocabulary of the bindery. Named easings first; they are the only four
the theme owns, and every duration below is fixed, not a range a
builder may improvise inside.

| Token | Curve | Character |
|---|---|---|
| `--ease-press` | `cubic-bezier(0.2, 0.7, 0.2, 1)` | The bookplate stamp and the press: a fast arrival, a firm settle, no bounce — paper under a platen does not bounce. |
| `--ease-leaf` | `cubic-bezier(0.5, 0, 0.15, 1)` | A leaf turning: slow lift from the fore-edge, a quickening fall onto the next leaf. Page transitions (§6.9), dog-ear (§6.4). |
| `--ease-gilt` | `cubic-bezier(0.3, 0.6, 0.4, 1)` | Light moving across gold leaf: even, unhurried, one direction only. Light-catch (§6.3), ornament draw (§6.5). |
| `--ease-type` | `steps(1, end)` at 55ms per character | The typewriter of the bindery office: the copy number typing into the bookplate (§6.1). The only stepped motion in the theme. |

The shared scroll loop runs at `--lerp: 0.1` and drives exactly four
things: drop-cap illumination (§6.2), the page-edge fill (§6.6), the
three-layer parallax, and the running-head chapter tracking (§6.17).
Everything else is trigger-and-transition. If the loop is removed, the
book loses its gilding-in-progress and nothing else.

- **Scroll-triggered reveals** — chapter furniture assembles on entry:
  the chapter numeral fades 400ms `--ease-press`, the title follows at
  +80ms, the drop cap is present from first paint (its illumination is
  the scroll's work, §6.2), the first paragraph at +160ms. Trigger line:
  chapter head at 78% of viewport height. Once per chapter per
  page-load; scrolling back does not re-assemble furniture.
- **Parallax** — three layers, three speeds, all from the one loop:
  marbled endpaper dividers drift at **0.3×** scroll speed, the spine
  rail is fixed (0× — it is the binding), the text column moves at 1×,
  and the gilt edge strip's *sheen* (not its fill) shifts at 1.15×.
  Total displacement of any layer never exceeds 24px within a divider;
  parallax exists here to give the endpaper depth against the leaf,
  not to make text swim. Text itself never parallaxes against its own
  background.
- **Pinned scenes** — two: the spine rail pins for the whole page (it
  is the book's spine; a spine that scrolls away is a broken binding),
  and each chapter opening pins briefly — the numeral-and-title block
  holds for 30vh while the drop cap's first illumination begins beneath
  it, then releases. No other pinning; a book does not freeze its text.
- **Masked reveals** — one device, used twice: the frontispiece
  reveals inside its gilt frame through a `clip-path: inset()` opening
  from the frame's centre line outward (§6.12), and the errata slip
  slides from beneath the leaf it corrects (§6.16). Masks here are
  frames and leaves, never arbitrary shapes.
- **Blur-to-sharp reveals** — refused as a device. Print does not
  unblur; it is *illuminated*. The theme's equivalent is the drop cap's
  gilt rising through the letter (§6.2) and the frontispiece's tissue
  guard lifting (§6.12). No element uses a CSS blur filter at any size.
- **Animated counters** — two, both bibliographic: the copy number
  typing into the bookplate (§6.1) and the copies-remaining count in
  the colophon (§6.8), set in old-style serif figures over 1200ms. No
  other number on the page ever animates; a statistic that counts up
  in a chapter is a gate failure.
- **Progress indicators** — the gilt page-edge filling downward
  (§6.6) plus "leaf n of N" in the fore-edge margin (§6.17). The two
  agree: the folio's N is the page's leaf count, the edge's fill is
  the same fraction. Percentages and bars are forbidden by the theme's
  founding law and grepped at the gate.
- **Marquees** — refused, in writing. A book has no moving text except
  the number being typed into its bookplate. If a build seems to need
  a ticker, it needs a contents leaf (§6.10) and a shorter page.
- **Kinetic typography** — two instances: the copy number typing
  (§6.1) and "Finis" fading in beneath the final ornament (§6.5) —
  the book's first mark and its last word. Titles never assemble
  letter by letter; the light-catch (§6.3) moves light across set
  type, it does not move the type.
- **Ambient loops** — one: the marble drift (§6.7), a few px over 20s
  at chapter ends. There is no second loop. The book's ambience is
  paper.
- **Micro-interactions** — hover catches gilt light at the pointer's
  angle (§6.3); click folds the dog-ear (§6.4), presses the stamp
  (§6.14). Nothing scales, bounces or depresses elastically; a press
  in this theme is a platen: down 1px, held, released.
- **Page transitions** — the leaf-turn (§6.9): 650ms, the leaf rotates
  from the spine rail, the gilt edge flashes once at the turn's
  midpoint. Browser back/forward is never intercepted.
- **Image treatments** — plates only (§6.12): always inside a gilt
  double-rule frame, always captioned, scale-in-frame capped at 1.04
  during the tissue-guard lift and never again. Images are never
  cropped by layout after the frame; the frame is chosen per plate at
  content time.
- **Skeleton loading** — the half-title (§6.18): the volume's title
  alone on a cream leaf, with ruled lines where the text will be —
  the book waiting to be opened, in its own furniture.
- **Scroll smoothing** — the shared rAF loop at `--lerp: 0.1`. All
  scrubbed values (illumination, edge fill, sheen, parallax offsets)
  are pure functions of scroll position: reversible, unlatched, and
  identical on the way back up, because a reader may turn back a leaf.


## 6. Signature elements

### 6.1 Bookplate stamping — "Ex Libris — Copy No. ___"

- **What & why.** The theme's signature and its covenant performed in
  the first second. On first load a bookplate stamps into the hero —
  a rectangular plate in buckram and gilt, lettered "Ex Libris" —
  and the visitor's own copy number types into the blank after "Copy
  No.", character by character. Numbering the copy is the hero's first
  content act: before the title page has finished assembling (§6.11),
  this instance of the site has an owner. Every later element in the
  theme — the dog-ear, the greeting, the reservation — keys off this
  number, which is why it is specified first and most strictly.
- **Structure.** A `<div class="bookplate">` inside the title-page
  hero (§6.11), sized 300×190px desktop, set at a deliberate 1.2°
  rotation (a plate pasted by hand is never perfectly square — the
  rotation is fixed in CSS, identical for every visitor, so it reads
  as the binder's habit, not randomness). Double-rule border: outer
  gilt 2px, inner ink hairline, "EX LIBRIS" in Playfair small caps at
  its head, a fleuron, then "Copy No." followed by `<span
  class="copy-no">` — the number as real text in the DOM. The number
  itself: drawn once per visitor as a stable integer in 1..edition
  size (§6.8's figure), stored under the localStorage key
  `fe.copyNo`; the printed fallback "Copy No. 1" is what the server
  renders in that span, and it is what remains if storage is denied.
- **Motion spec.** Trigger: page load, after fonts (watchdog below).
  The stamp: the plate scales **1.25 → 1** and darkens (ink overlay
  opacity 0.25 → 0) over **200ms `--ease-press`**, arriving with the
  slight overshoot-free thud of a platen — no bounce, ever. At +260ms
  the typing begins: characters appear at **55ms per character**
  `--ease-type`, with the blank's underline hairline pulsing once at
  the first character. A 3-digit number is fully typed by ~+430ms.
  On return visits the stamp still lands (the plate is the hero's
  furniture), the number is already present — it does not re-type;
  instead the greeting line (§6.11) fades in beneath the plate at
  +400ms.
- **Choreography timeline (v2).** t+0: hero leaf paints, plate present
  at final state in the DOM (pre-state is JS-applied only) → t+120ms:
  JS arms the stamp (scale 1.25, overlay 0.25) → t+120–320ms: stamp
  lands → t+380ms: first character types → 55ms/char until the number
  completes → t+completion+200ms: the title page's remaining lines
  begin their bibliographic stagger (§6.11) — the copy is numbered
  before the book is titled; ownership precedes contents.
- **State matrix (v2).** *Rest (first visit, pre-load):* server-rendered
  plate reading "Copy No. 1" — the honest fallback state. *Stamping:*
  200ms, non-interactive. *Numbered (terminal):* plate at rest,
  number set — identical on desktop and touch. *Hover:* the plate is
  not a control; hover does nothing except the gilt border's
  light-catch (§6.3) if the pointer crosses it. *Focus:* not
  focusable. *Scrolled-past:* the plate scrolls away with the title
  page; it does not pin. *Disabled (no JS / no storage):* the printed
  "Copy No. 1" plate, static — a complete, honourable state; the
  greeting line never appears.
- **Content merge.** The plate carries the copy's identity — the one
  piece of content no other element can state. It sits inside the
  front cover of the book the visitor is reading; remove it and the
  theme's premise (this copy is yours) has no anchor anywhere else on
  the page.
- **Failure fallback.** The standing law, inherited from the original
  entry: **the copy number is local state with a printed "Copy No. 1"
  fallback.** If localStorage throws (private mode, quota, policy),
  the fallback stands and no error is shown — a bookplate that cannot
  be numbered is still a bookplate. If fonts have not loaded by
  900ms, the stamp fires anyway in fallback serif; a watchdog at
  1400ms forces the plate to its rest state regardless of animation
  state. The number is **never sent to any server** — it is the
  reader's mark in their own copy, and transmitting it would make it
  a tracking ID wearing a costume (§9).
- **Reduced-motion variant.** No stamp, no typing. The plate is
  present at rest with the number already set (drawn and stored as
  usual — state is not motion). The greeting line on return visits is
  simply present.
- **Breakpoints (v2).** ≥1200px: 300×190px, rotation 1.2°. 768–1199px:
  264×168px, rotation 1.2°. <768px: 232×148px, rotation 0.8°, stamp
  scale travel reduced to 1.15 → 1 (a phone screen is closer; the
  thud is smaller).
- **Edge cases & failure modes (v2).** *Edition size changed by the
  publisher after numbers were drawn:* stored numbers above the new
  size are kept — a copy numbered 480 of an edition later stated as
  400 is a bibliographic curiosity, and quietly renumbering a
  visitor's copy is the one unforgivable act; the colophon (§6.15)
  states the current edition size and the discrepancy is left to be
  what it is. *Storage cleared:* a new number is drawn and the
  greeting does not appear — the site treats it as a new copy, which
  it is. *Two tabs:* last-writer-wins on the key; both tabs show a
  valid plate. *Number drawn but tab closed before typing finished:*
  the number is stored before the first character types, so the
  return visit is consistent.
- **Accessibility spec (v2).** The plate's text is real DOM text in
  reading order: "Ex Libris. Copy No. 212." The typing is visual only
  — the full number is in the accessibility tree from first paint
  (the span's text is set complete; the type effect masks characters
  visually with a clip, never by withholding text). The stamp is
  decorative motion around announced content and is not itself
  announced. Contrast: buckram plate lettering in cream on buckram,
  10.27:1 ✓; the number in ink on the plate's cream field, 14.07:1 ✓.
- **Performance budget & mobile variant.** The plate is DOM + CSS —
  no image, no canvas. Cost: one transform/opacity animation, one
  stepped text reveal. Mobile: as breakpoints; typing interval
  unchanged (55ms is a rhythm, not a size).
- **Tokens consumed (v2).** `--buckram`, `--cream`, `--gilt`, `--ink`,
  `--ease-press`, `--ease-type`, `--stamp-dur` (200ms), `--type-step`
  (55ms).

### 6.2 Drop-cap illumination

- **What & why.** Each chapter opens with a drop cap, and the cap is
  *illuminated* — gilt rises through the letter as the reader reads
  the chapter, scrubbed to scroll through that chapter alone. It
  belongs here because illumination is what a fine edition does to its
  initials, and because it makes chapter progress a property of the
  chapter's own first letter: the gold filling the initial **is** the
  reading, made visible on the furniture itself. When the cap is fully
  gilt, the chapter has been read; the ornament (§6.5) is near.
- **Structure.** The cap is the chapter's real first letter, set as a
  `<span class="dropcap" aria-hidden="true">` duplicating the first
  character, with the paragraph's own first letter visually clipped
  (the standard accessible drop-cap pattern: the paragraph text is
  complete in the DOM; the decorative cap is its enlarged twin). Two
  stacked layers: an **ink underlay** (the letter in `--ink`,
  complete, always fully visible) and a **gilt overlay** (the same
  letter in a `--gilt-deep → --gilt → --gilt-bright` vertical
  gradient, clipped by a mask whose height is the illumination
  value). The gilt never replaces the ink; it rises *through* it, so
  at every illumination value the letter is fully legible.
- **Motion spec.** Scrubbed, from the shared loop (`--lerp: 0.1`).
  Per chapter, progress `p` maps the chapter body's scroll pass:
  `p = 0` when the chapter's first line crosses 85% of viewport
  height, `p = 1` when its last paragraph crosses 35%. The gilt mask
  height = `p × 100%` of the cap's height, rising from the baseline
  upward — gold fills a letter from its foot, as leaf is laid from
  the bottom of the stroke. No easing curve; the scroll is the
  timeline. Scrolling back lowers the gilt symmetrically — a reader
  re-reading a chapter watches its initial un-gild, which is correct:
  the illumination measures *position in the chapter*, not a trophy
  earned.
- **Choreography timeline (v2).** Spatial, per chapter: chapter head
  assembles (§5) with the cap at `p = 0` (ink letter, gilt absent) →
  first lines read: gilt foot appears at the letter's base → chapter
  midpoint: gilt at ~50%, the gradient's bright band at the waterline
  → final paragraphs: gilt completes, the bright band reaches the
  cap's crown → ornament beat (§6.5) begins with the cap fully gilt —
  the two events are sequenced by the same scroll, never by timers.
- **State matrix (v2).** *Rest (chapter unentered):* ink cap, no gilt
  — the printed default, identical with JS off. *Illuminating:*
  scrubbed per frame, desktop and touch identical. *Fully gilt:*
  gradient at 100%, loop stops writing this cap until it re-enters
  the active band. *Hover:* none — the cap is not a control. *Focus:*
  not focusable. *Scrolled-past:* retains the `p` its position
  dictates (above the viewport, `p = 1`; the letter stays gilt —
  position is the state). *Disabled (no JS):* **the cap is fully gilt
  by default** — the original entry's safety rule: illumination is an
  overlay replayed on a finished letter, never the letter's only
  state.
- **Content merge.** The cap is the chapter's first letter and the
  gilt is laid on that letter. Nothing is decorated that is not also
  the content's own initial; a chapter with a one-letter first word
  still illuminates exactly that letter.
- **Failure fallback.** Fully gilt by default in markup; JS *removes*
  gilt only for chapters below the fold it will actually drive. If
  the loop stalls for 900ms, a watchdog sets every cap in the active
  chapter to full gilt. If `background-clip: text` or masking is
  unsupported, the overlay is hidden and the ink cap stands — the
  chapter loses its illumination and keeps its initial.
- **Reduced-motion variant.** The cap is fully gilt at all times, on
  every chapter. The reader gets the finished manuscript page; the
  illumination-as-progress is conveyed by the folio (§6.17) alone.
- **Breakpoints (v2).** ≥1200px: cap 4.35em spanning 3 lines, as §3.
  768–1199px: same (type scale holds). <768px: cap 3.6em spanning 3
  lines of the narrower measure; the gradient loses its bright band
  (two stops instead of three) to keep the smaller letter clean.
- **Edge cases & failure modes (v2).** *Very short chapter* (body
  shorter than the scrub range): `p` is computed against the range
  actually available, min 60vh, so a short chapter still illuminates
  fully by its ornament. *Chapter beginning with a quotation mark or
  a numeral:* the cap is the first *letter*; an opening quote is set
  hanging in the margin at cap size in ink, unilluminated — the gilt
  belongs to the letter. *Chapter beginning with "I" or "A":* the
  narrow letter illuminates normally; the mask is proportional, not
  pixel-based, so no special case. *Print:* caps print fully gilt —
  the stylesheet sets the overlay to 100% and the loop does not run.
- **Accessibility spec (v2).** The decorative cap is `aria-hidden`;
  the paragraph's real first letter is read in place, so a screen
  reader hears the chapter's first word whole, once. The illumination
  is never announced and carries no information the folio doesn't
  carry in words. Legibility: the ink underlay guarantees the letter
  at 14.07:1 in every state; gilt-deep at cap size (≥56px) on cream
  is 4.10:1, passing AA for large text, and it is never the sole
  carrier — the ink is beneath it at all times.
- **Performance budget & mobile variant.** One masked layer per
  chapter, transform/mask writes only while the chapter is within one
  viewport of the active band; cap: 2 caps actively scrubbing at
  once. Mobile: as breakpoints; loop cost for this element ≤0.5ms per
  frame.
- **Tokens consumed (v2).** `--ink`, `--gilt`, `--gilt-deep`,
  `--gilt-bright`, `--lerp` (0.1), `--cap-lines` (3).

### 6.3 Gilt light-catch

- **What & why.** Gold leaf is not a colour; it is a surface that
  answers light. This element is the theme's proof of material: once,
  on load, light sweeps the hero title left to right; thereafter, any
  gilt element the pointer crosses brightens **at the pointer's
  angle** — the highlight sits where a real light, held where the
  reader's hand is, would put it. It belongs here because a flat gold
  gradient is the theme's cheapest possible fake (§9), and the
  difference between gilt and gold-coloured is precisely that gilt
  responds.
- **Structure.** Each gilt-bearing element (hero title, plate frames
  §6.12, ornament strokes §6.5, the page-edge strip §6.6, chapter
  numerals) carries a specular layer: a linear-gradient overlay whose
  angle and position are driven by two CSS variables, `--lx` (light
  position across the element, 0–1) and `--la` (angle, deg), written
  by pointermove on the element itself — no global listener, no
  loop. The hero title implements it as a background-clip:text
  gradient over the ink title; frames and rules implement it as an
  overlay gradient on the gilt stroke.
- **Motion spec.** *The once-sweep:* on title-page assembly (§6.11),
  after the title line lands, `--lx` animates 0 → 1 over **1200ms
  `--ease-gilt`**, once per page-load, never again — light passes
  across a bound book's title when it is first opened; it does not
  keep passing. *Hover catch:* on pointerenter of a gilt element, the
  specular layer fades in over 180ms; on pointermove, `--lx`/`--la`
  track the pointer's position across the element's box (angle =
  atan2 of pointer offset from centre, clamped to ±35° so the light
  stays plausible); on leave, the layer fades out over 320ms. Peak
  specular: `--gilt-bright` at 65% over the gilt base.
- **Choreography timeline (v2).** Hero: title lands (§6.11 beat) →
  t+150ms: sweep begins at the title's left → t+1350ms: sweep
  completes at the right; the title rests in flat gilt-and-ink →
  never repeats this page-load. Hover: enter → 180ms fade-in at the
  entry point's `--lx` → move: highlight follows with a 90ms trailing
  transition on the variables (light has a little weight) → leave:
  320ms fade.
- **State matrix (v2).** *Rest:* flat gilt, no specular — the default
  and the no-JS state. *Sweeping (hero, once):* 1200ms. *Hover:*
  specular live at pointer angle — desktop only. *Focus:* a gilt
  element that is also a control (chapter numeral links §6.10,
  plate-card titles §6.13) shows the catch at its centre on
  focus-visible, so keyboard visitors get the material too. *Active:*
  specular pinned at centre, full strength, for the press duration.
  *Scrolled-past:* rest. *Touch:* no hover catch — touch gilt
  elements show a single gentle sweep (600ms, `--lx` 0→1) the first
  time they cross the viewport centre, then rest; the material is
  demonstrated, not chased.
- **Content merge.** The light moves across the title's own letters
  and the frames' own gilt. It is a property of the metal the content
  is made of, applied to nothing the content does not already wear.
- **Failure fallback.** Flat gilt is the complete resting state; if
  CSS variables or pointer events are unavailable, every element is
  simply gilt. The sweep is an animation of a variable — if it never
  runs, nothing is missing and nothing is hidden.
- **Reduced-motion variant.** No sweep, no touch demonstration. Hover
  catch becomes a static brighten (gilt → gilt-bright at 40% mix,
  instant) — the acknowledgement without the movement.
- **Breakpoints (v2).** Identical behaviour at all sizes; <768px the
  specular peak drops to 50% (smaller elements, closer screen,
  subtler light) and the trailing transition shortens to 60ms.
- **Edge cases & failure modes (v2).** *Pointer moving fast across
  many gilt elements:* listeners are per-element and passive; the
  90ms variable transition smooths jitter; no rAF loop is involved,
  so there is nothing to stall. *Gilt element inside the pinned
  spine rail:* the catch works identically; angle clamps keep the
  highlight on the narrow rail plausible. *The once-sweep interrupted
  by navigation:* it is per-page-load and unrepeatable by design; a
  visitor who leaves mid-sweep has simply closed the book early.
- **Accessibility spec (v2).** Purely decorative; the specular layers
  are overlays with `aria-hidden` where they are separate elements,
  and background layers where they are not. Focus-visible parity
  (state matrix) ensures the effect is not pointer-exclusive. The
  brightened gilt never carries meaning — gilt on buckram at rest is
  already 4.94:1, and the catch only adds.
- **Performance budget & mobile variant.** Variable writes on
  pointermove for the hovered element only — effectively free; no
  paint of anything larger than the element itself. Mobile: touch
  demonstration as above; no pointermove listeners are registered on
  coarse pointers at all.
- **Tokens consumed (v2).** `--gilt`, `--gilt-bright`, `--ease-gilt`,
  `--sweep-dur` (1200ms), `--catch-in` (180ms), `--catch-out` (320ms).


### 6.4 Dog-ear memory

- **What & why.** A reader marks a place in a book by folding the
  leaf's corner. Here, clicking a chapter's fore-edge corner folds a
  dog-ear — a real triangle of the leaf turned down, with its shadow
  — and the fold **persists**: stored locally, already folded when
  the copy is next opened, greeted in the colophon and the title-page
  line ("The dog-ear is where you left it"). It belongs here because
  it is the theme's bookmark with the database removed: the mark is
  on the content itself, in the copy the visitor owns, and it is the
  single most persuasive proof that the numbering (§6.1) is not
  theatre — the book remembers being read.
- **Structure.** Each chapter sheet carries a `<button class="dogear">`
  at its top fore-edge corner (44×44px hit area; the visible fold is
  a 34px triangle). The fold is two CSS triangles: the turned-down
  corner (cream-deep, with the leaf's underside showing a mirrored
  hairline of the chapter's first rule) and a soft shadow triangle
  beneath it on the leaf. State lives in localStorage under
  `fe.dogears` as an array of chapter ids. Multiple chapters may be
  folded — a reader dog-ears many places — but the greeting line
  (§6.11) names the *last folded* chapter.
- **Motion spec.** Click: the corner folds over **300ms
  `--ease-leaf`** — a `clip-path` polygon morph on the corner element
  plus the shadow fading in over the same span, so the triangle grows
  from the corner as a real fold does, rather than appearing. Unfold
  (second click): the reverse, 240ms. The fold is a state change,
  not a flourish: no overshoot, no bounce.
- **Choreography timeline (v2).** t+0: click lands on the corner →
  t+0–300ms: fold polygon sweeps from corner point to full triangle;
  shadow reaches full at t+220ms (the fold lands before its shadow
  settles) → t+300ms: state written to storage; the button's label
  flips to "Remove the dog-ear from Chapter 3" → the contents leaf
  (§6.10) gains its folded-corner mark on that chapter's line at the
  same beat (no separate animation — the contents is a record, it is
  simply true now).
- **State matrix (v2).** *Rest (unfolded):* corner flat; a hairline
  diagonal at 12% ink hints the fold line — the leaf shows where it
  *would* fold, as paper does after a first reading. *Hover:* the
  hint line deepens to 30% and the corner lifts 2px (the triangle's
  tip separates from the leaf) — desktop only. *Focus:* same lift,
  plus the theme focus ring on the hit area. *Active/folding:* 300ms
  per spec. *Folded (terminal per chapter):* triangle down, shadow
  set; hover on a folded ear shows the underside brightening slightly
  (cream-deep → cream) — the fold can be lifted again. *Scrolled-past:*
  unchanged; folds are state, not scroll effects. *Touch:* no hover
  states; tap folds; the hit area is the full 44px corner.
  *Disabled (no JS/storage):* the button is not rendered — a paper
  book without the reader's hand has no dog-ears, and a non-functional
  fold control is worse than none.
- **Content merge.** The fold is on the chapter's own corner, and the
  contents leaf records it against that chapter's line. The mark,
  the chapter and the record are one fact in three places.
- **Failure fallback.** If storage is unavailable, folds work for the
  session in memory and the button still renders (the failure is
  persistence, not function); the greeting line (§6.11) only ever
  claims a dog-ear that storage confirms. If the stored array is
  corrupt, it is discarded silently and the copy starts unfolded —
  never an error state on a chapter corner.
- **Reduced-motion variant.** The fold appears/disappears instantly
  (opacity swap of the two triangles, 0ms). The state, the contents
  mark and the greeting are unchanged — memory is not motion.
- **Breakpoints (v2).** ≥1200px: fold on the chapter sheet's corner
  in the fore-edge margin, 34px triangle. 768–1199px: same position,
  margin is narrower — the triangle overhangs the text column's edge
  by up to 8px and must never cover a glyph (chapters carry 12px
  corner clearance in their first line, §4). <768px: 30px triangle,
  48px hit area, positioned on the sheet corner inside the viewport
  edge.
- **Edge cases & failure modes (v2).** *Chapter removed or renamed
  between visits:* stored ids that no longer resolve are pruned on
  load; if the greeted chapter is gone, the greeting names the most
  recent surviving fold, or does not appear. *Fold during the
  leaf-turn (§6.9):* the corner button is inert while a turn is in
  flight (the whole leaf is). *Print:* folded ears print as their
  shadow triangle only — the stylesheet flattens the fold to its
  mark, so a printed chapter shows where it was kept.
- **Accessibility spec (v2).** A real `<button>` with a specific label
  ("Fold a dog-ear on Chapter 3 — The Long Binding") and
  `aria-pressed` carrying the state. Focus order: the ear is the
  chapter's last tab stop (a reader finishes a chapter, then marks
  it). The fold is announced only via the pressed state; the greeting
  line is ordinary text. Hit area ≥44px at every breakpoint.
- **Performance budget & mobile variant.** Two CSS triangles and a
  clip-path morph per chapter; storage writes are single small JSON
  arrays. Cost negligible. Mobile: as breakpoints.
- **Tokens consumed (v2).** `--cream`, `--cream-deep`, `--ink`,
  `--ease-leaf`, `--fold-dur` (300ms), `--ear-size` (34px).

### 6.5 Printer's ornament draw + "Finis"

- **What & why.** Every chapter closes with the printer's ornament —
  a fleuron, the leaf-and-scroll device printers have set at chapter
  ends for five centuries — and it **draws itself** as the reader
  arrives at the chapter's end. Only the final chapter's ornament is
  followed by the word "Finis". It belongs here because the ornament
  is the book's full stop: furniture that marks an ending the way the
  drop cap (§6.2) marks a beginning, and its drawing is paced like a
  hand setting it — the reader watches the chapter be *finished*, not
  merely ended. The rationing of "Finis" is the theme's discipline in
  miniature: the word means the volume is over, so it appears once,
  at the volume's end, and any second appearance is a defect (§10).
- **Structure.** One inline SVG per chapter end: a symmetric fleuron
  (central stem, two scrolls, two leaves — a fixed path set, total
  path length ~640 units), stroke `--gilt-deep` 1.5px on cream, width
  120px, centred on the measure, sitting 3 lines below the chapter's
  last paragraph. The draw is `stroke-dashoffset` driven by
  `getTotalLength()` per path. "Finis" is a `<p class="finis">` in
  Playfair italic 1.3rem, present in the DOM only in the final
  chapter's ornament block.
- **Motion spec.** Trigger: the ornament's centre crosses 62% of
  viewport height. Duration **800ms `--ease-gilt`**, paths staggered
  by construction: the stem draws 0–300ms, the scrolls 200–600ms,
  the leaves 450–800ms — the device grows from its stem outward, as
  drawn, not as a uniform wipe. Once per chapter per page-load;
  scrolling back does not undraw it (an ending, once reached, stays
  reached — unlike the illumination, this one *is* a trophy, because
  chapters end once). In the final chapter, "Finis" fades in at
  t+850ms over 600ms `--ease-press`, and nothing on the page moves
  after it.
- **Choreography timeline (v2).** t+0: trigger line crossed → stem
  begins → t+200ms: scrolls begin → t+450ms: leaves begin → t+800ms:
  device complete, dash removed, ornament rests as plain gilt line
  work → (final chapter only) t+850–1450ms: "Finis" fades → the
  colophon (§6.15) is the next thing the reader meets; the sequence
  ornament → Finis → colophon is the volume's closing cadence and is
  never interrupted by a pop-up, banner or related-content rail (§9).
- **State matrix (v2).** *Rest (pre-trigger):* the ornament is fully
  drawn in the DOM — the pre-state (dash offset full) is applied by
  JS only when the draw will actually run. *Drawing:* 800ms.
  *Drawn (terminal):* plain SVG line work. *Hover/focus:* the
  ornament is not interactive; no states. *Scrolled-past:* drawn.
  *Disabled (no JS):* fully drawn — the printed state.
- **Content merge.** The ornament sits where the chapter's text ends
  and is the chapter's closing furniture; its drawing is triggered by
  arrival at that ending. It decorates nothing but the boundary it
  marks.
- **Failure fallback.** Fully drawn by default; JS adds the dash
  state only on arming. A watchdog at trigger+1100ms sets any
  mid-draw ornament to drawn. If SVG is unavailable (ancient engine),
  a text fleuron "❦" in gilt-deep is the server-rendered fallback
  inside the same block — the furniture survives its technology.
- **Reduced-motion variant.** The ornament is present, drawn. "Finis"
  is present. No fade — the closing cadence becomes purely spatial:
  text, ornament, word, colophon.
- **Breakpoints (v2).** ≥1200px: 120px wide. 768–1199px: 104px.
  <768px: 88px and durations compress to 650ms (a smaller device,
  drawn a little faster, the stagger proportions kept).
- **Edge cases & failure modes (v2).** *Chapter so short its opening
  and ornament are on screen together:* the draw still waits for its
  own trigger; a one-screen chapter gets its full closing ceremony.
  *Two ornaments triggering in one fast scroll:* draws queue in
  reading order, max 1 drawing at once; the second starts when the
  first completes or is set drawn instantly if the reader has already
  passed it. *"Finis" creep:* builds are grepped — the string appears
  in exactly one block (§10); a template that includes it per-chapter
  fails the gate even if CSS hides the extras.
- **Accessibility spec (v2).** The ornament is `aria-hidden`
  decoration; the chapter's end is conveyed structurally (heading
  order, the next chapter's numeral). "Finis" is real text and is
  read — correctly, as the volume's last word. Gilt-deep stroke on
  cream at 1.5px is a graphic, not text; its 4.10:1 is noted and
  accepted because the ink chapter furniture around it carries all
  meaning.
- **Performance budget & mobile variant.** One small SVG per chapter;
  dash animation on ≤3 paths. Negligible. Mobile: as breakpoints.
- **Tokens consumed (v2).** `--gilt-deep`, `--gilt`, `--ease-gilt`,
  `--ease-press`, `--draw-dur` (800ms).

### 6.6 Gilt page-edge fill

- **What & why.** A bound book's leaves are gilt on the fore-edge;
  the deeper into the volume, the more of that edge the reader's
  thumb has travelled. This element makes the page's right edge that
  edge: a 10px gilt strip fixed at the viewport's right, whose filled
  height is scrubbed to reading progress — brightening as each new
  chapter opens. It belongs here because progress in this theme is
  depth in a physical volume, and the edge states it continuously,
  in the margin, without a single digit. Together with the folio
  (§6.17) it is the theme's entire progress system, and the two are
  specified to agree exactly.
- **Structure.** A fixed `<div class="page-edge">` at the viewport's
  right edge, full height, 10px wide, `aria-hidden`, composed of: a
  track (the un-gilt edge: cream-deep with fine horizontal striations
  — the leaf edges, drawn as a repeating-linear-gradient at 3px
  pitch) and a fill (the gilt: `--gilt-deep → --gilt → --gilt-bright`
  vertical gradient) whose height is set by the shared loop as a
  `--read` fraction. At each chapter boundary the fill carries a
  slightly wider bright tick (the gilt catches at a new gathering's
  thicker leaf).
- **Motion spec.** Scrubbed, shared loop (`--lerp: 0.1`): `--read` =
  scrolled fraction of the *volume* (the page's full reading length,
  excluding the colophon — the colophon is after the end). At each
  chapter opening crossing, the fill's leading edge brightens
  (gilt-bright at 80%) for 600ms `--ease-gilt` and relaxes — the
  brightening is a pulse of the gradient's top stop, not a flash of
  the whole strip. The sheen layer (§5) shifts at 1.15× against the
  fill, so the metal has depth as it grows.
- **Choreography timeline (v2).** Continuous and spatial: title page
  → `--read` 0, strip all leaf-edge → each chapter: fill grows
  through it, bright tick at its first leaf → final ornament (§6.5)
  → `--read` 1 exactly as "Finis" fades; the strip is fully gilt for
  the colophon, and stays so — the volume is read.
- **State matrix (v2).** *Rest:* fill at the position scroll dictates
  — including on load mid-page (a restored scroll position shows a
  partly gilt edge immediately; the state is a pure function of
  position). *Hover/focus/active:* none — the edge is not a control
  and must never become one (a clickable progress edge is a scrollbar
  wearing gilt; §9). *Scrolled-past:* n/a. *Disabled (no JS):* the
  strip renders as the un-gilt leaf edge for its full height — the
  book ungilt reads as a plain edge, which is honest: without the
  loop there is no reading being measured.
- **Content merge.** The fill measures this page's reading and the
  ticks sit at this page's chapter boundaries. It is the volume's own
  edge; on a page with one chapter it fills across that chapter
  alone, and on the contents leaf it stays at the fraction the
  contents occupies — it never borrows another page's progress.
- **Failure fallback.** If the loop stalls, the fill freezes at its
  last true value (never resets to 0 — a frozen true fraction is
  honest, a reset is a lie); the 900ms watchdog marks the strip
  `data-stalled` and stops the sheen. If the page's height changes
  (late images), the fraction recomputes on the next frame from
  cached measurements refreshed on resize.
- **Reduced-motion variant.** The fill still tracks position (it is
  information, not ornament) but updates without lerp — set directly
  on scroll, throttled to animation frames — and the chapter
  brightening pulse is removed.
- **Breakpoints (v2).** ≥1200px: 10px. 768–1199px: 8px. <768px: 6px,
  striation pitch 2px, bright ticks removed (at 6px a tick is noise;
  the folio carries chapter position alone).
- **Edge cases & failure modes (v2).** *Page shorter than the
  viewport:* `--read` is 1 from load; the strip is fully gilt and the
  folio reads "leaf 1 of 1" — a pamphlet is a complete small book.
  *Horizontal scrollbars / overlay scrollbars:* the strip is fixed to
  the visual viewport's right and sits above the leaf striations but
  below any modal layer; on platforms with classic scrollbars it
  offsets by the scrollbar width so it never paints over the bar.
  *Zoom:* the strip is viewport-fixed and unaffected — correct; an
  edge belongs to the book, not the zoom level.
- **Accessibility spec (v2).** `aria-hidden="true"`; progress is
  available in words from the folio ("leaf n of N", §6.17) which is
  real text in the reading order. The strip must never be the sole
  carrier of progress information — that is the folio's job, and the
  gate checks both exist.
- **Performance budget & mobile variant.** One fixed element, one
  height write per frame from the shared loop. Negligible. Mobile:
  as breakpoints.
- **Tokens consumed (v2).** `--gilt`, `--gilt-deep`, `--gilt-bright`,
  `--cream-deep`, `--lerp` (0.1), `--edge-w` (10px).


### 6.7 Marble drift

- **What & why.** Between gatherings, the divider is marbled endpaper
  — the swirled, veined paper pasted inside a binding's covers — and
  it is *barely* alive: the swirls drift a few px over 20 seconds,
  almost imperceptibly. It belongs here because the endpaper is the
  book's threshold material: it is what a reader sees in the pause
  between the cover and the title, between one gathering and the
  next. Its slow life separates chapters without a single piece of UI
  chrome — no "next chapter" banner, no progress toast — just paper
  that is not quite still, the way real marbling catches light
  differently as the leaf settles.
- **Structure.** A full-bleed `<div class="endpaper">` 38vh tall
  between gatherings (§4), containing one inline SVG (≤12KB) of
  marbling: layered `<feTurbulence>`/displacement swirls in
  `--marble-vein` and `--marble-gilt` over cream, generated once and
  reused identically at every divider in the volume (the endpaper
  stock is one paper throughout the book — varying it per chapter is
  a §9 failure). The drift animates a 6px background-position range
  on a slightly oversized (calc(100% + 12px)) rendering, so no edge
  ever shows. The divider also carries the next chapter's numeral,
  set large in buckram at its centre — the endpaper announces what it
  precedes.
- **Motion spec.** Ambient loop: position drifts 0 → 6px → 0 over
  **20s, linear, infinite alternate**, phase-offset per divider by
  its index (divider n starts at phase n × 3.7s) so two dividers on
  screen never breathe together. Parallax: the marble layer also
  translates at 0.3× scroll (§5) within its 12px allowance — the two
  motions compose; total displacement never exceeds 12px in any
  direction. The loop pauses off-screen (IntersectionObserver) and
  on hidden tabs.
- **Choreography timeline (v2).** Continuous: divider enters → drift
  already mid-cycle at its phase (never restarting at 0 — paper does
  not reset) → parallax carries it slowly against the scroll →
  divider exits → loop pauses at its current phase → re-entry resumes
  from the same phase.
- **State matrix (v2).** *Rest:* the marbled leaf, static — the
  no-JS and reduced-motion state, complete in itself. *Drifting:*
  in viewport, motion allowed. *Hover/focus:* the numeral is a link
  to the next chapter (§6.10's contents logic); hovering the divider
  does not speed, brighten or otherwise perform the marble — paper
  does not respond to being looked at. *Scrolled-past:* paused.
  *Disabled:* static marble.
- **Content merge.** The divider is the chapter boundary and carries
  the next chapter's numeral — the one piece of information a reader
  needs in the pause. Remove the drift and the boundary remains,
  fully functional; the motion is the paper's life, not its message.
- **Failure fallback.** If SVG filters are unsupported, the divider
  falls back to a flat two-vein gradient in the same tokens (specified
  in CSS, no JS involved) — a plainer endpaper, still an endpaper.
  If the SVG fails to load (it is inline; failure means a broken
  build), the divider is cream-deep with the numeral — the gate
  catches it, but the page never shows a hole between chapters.
- **Reduced-motion variant.** No drift, no parallax. The static
  marbled leaf with its numeral — the divider exactly as a printed
  endpaper is.
- **Breakpoints (v2).** ≥1200px: 38vh. 768–1199px: 32vh. <768px:
  26vh, numeral one step smaller, drift range 4px.
- **Edge cases & failure modes (v2).** *Performance on low-power
  devices:* feTurbulence is rendered once to a static bitmap by the
  browser; the drift moves the bitmap, it does not re-run the filter
  — if a device still struggles (measured via the §14 frame budget),
  the drift is the first cut and the parallax keeps the depth.
  *Two dividers adjacent* (a very short chapter): phases differ by
  construction; if both are on screen, the nearer-to-centre keeps
  drifting and the other pauses — two breathing papers is one too
  many. *Print:* dividers print as the static marble at phase 0.
- **Accessibility spec (v2).** The marble is `aria-hidden`; the
  numeral is a real link with a real label ("Chapter 4 — The Long
  Binding") and a 44px+ target. The drift is below any photosensitivity
  threshold (6px over 20s, no luminance alternation) and is fully off
  under reduced motion.
- **Performance budget & mobile variant.** One inline SVG reused via
  `<use>`; rendered once, composited cheaply. The drift is a
  transform on one layer per visible divider, cap 1 active. Mobile:
  as breakpoints.
- **Tokens consumed (v2).** `--cream`, `--cream-deep`,
  `--marble-vein`, `--marble-gilt`, `--buckram`, `--drift-dur` (20s).

### 6.8 Copies-remaining count

- **What & why.** In the colophon (§6.15), beside the edition size,
  the number of copies remaining counts to its true figure as the
  colophon enters — set in old-style serif figures, in the edition
  statement's own lines, where a bibliographer would record it. It
  belongs here because scarcity in this theme is a *bibliographic
  fact*, stated once, in the back of the book, in the same breath as
  the edition size and the printer's name — never as a banner, never
  with an exclamation, never anywhere else on the page. The count's
  placement is its honesty: a fact in a colophon is a record; the
  same number in a hero is a sales tactic, and this theme prints
  records.
- **Structure.** A line in the colophon block: "Of five hundred
  copies, [n] remain." The figure `n` is server-rendered from the
  publisher's real data (a `data-remaining` attribute on the colophon
  carries the same figure for the count animation). If the publisher
  supplies no figure, the line reads "This edition is limited to
  five hundred copies." and **no number is animated, estimated or
  invented** — the absent figure is the specified state, not a
  missing feature.
- **Motion spec.** Trigger: the colophon crosses 70% of viewport
  height. The figure counts from the edition size down to the
  remaining figure — down, because copies leave an edition; a count
  that climbs toward scarcity is theatre — over **1200ms
  `--ease-press`**, in whole figures, old-style numerals, tabular
  alignment via `font-variant-numeric: tabular-nums` *within this
  line only* (the one place the book uses tabular figures, so the
  line's width does not shift as it counts). Once per page-load.
- **Choreography timeline (v2).** t+0: colophon enters → edition
  statement lines fade in bibliographic order (§6.15) → the count
  line's turn comes at its line's fade → t+0–1200ms: figures descend
  500 → n → t+1200ms: the line rests; nothing else on the page has
  moved in response — no badge appears, no button changes. The fact
  has been stated; the book does not applaud it.
- **State matrix (v2).** *Rest (pre-trigger):* the true figure,
  printed — the animation starts from a JS-applied pre-state (edition
  size) only when the count will run. *Counting:* 1200ms.
  *Counted (terminal):* the true figure. *Hover/focus:* the line is
  text, not a control. *Scrolled-past:* counted. *Disabled (no JS):*
  the true figure, printed. *No data:* the no-figure line, in every
  state, forever.
- **Content merge.** The count is a line of the edition statement
  itself — the same sentence a printed colophon would carry. It is
  not a widget placed near the footer; it is the footer's own text,
  animated once as it is first read.
- **Failure fallback.** If the data attribute and the rendered figure
  disagree, the rendered figure wins and the animation is skipped
  (the server's print outranks the browser's arithmetic). If the
  figure is stale (cached page), it is exactly as stale as every
  other fact on the page — the colophon carries the edition's
  statement as of printing, which is what colophons do; builds that
  need live stock must server-render per request, and the spec says
  so rather than pretending a browser count is live.
- **Reduced-motion variant.** The true figure, printed. No count.
- **Breakpoints (v2).** Identical at all sizes — a line of the
  colophon does not responsive-design itself.
- **Edge cases & failure modes (v2).** *Remaining = 0:* the line
  reads "Of five hundred copies, none remain." and the order form
  (§6.14) is replaced by its waiting-list state — the count and the
  form must agree; a form still selling a exhausted edition is a
  §10 failure. *Remaining > edition size* (data error): the line
  prints the no-figure form and the discrepancy is a build bug the
  gate greps for (`data-remaining` ≤ edition size, enforced in
  review). *Very small editions* (n of 12): the count is short and
  that is fine — 1200ms regardless; the ceremony is the same size
  for every edition.
- **Accessibility spec (v2).** The full sentence is in the
  accessibility tree at its final value from first paint (the count
  masks figures visually in place, like §6.1's typing). The count is
  never announced mid-flight. The sentence is plain text at 0.95rem,
  ink on cream, 14.07:1 ✓.
- **Performance budget & mobile variant.** One numeric interpolation
  on the shared loop for 1200ms. Negligible at every size.
- **Tokens consumed (v2).** `--ink`, `--ease-press`, `--count-dur`
  (1200ms).

### 6.9 Leaf-turn transition

- **What & why.** Leaving a page turns a leaf: the current leaf
  rotates away from the spine rail, its gilt edge flashing once as
  it turns, and the new leaf settles beneath it. It belongs here
  because navigation is the one act every visitor performs, and in
  this theme it must be performed in the book's mechanics — a fade
  or a slide would be a screen pretending; a leaf turning from the
  spine is the volume doing what volumes do. The gilt flash is not
  decoration: it is §6.6's edge, seen edge-on for one instant as the
  leaf passes vertical.
- **Structure.** A fixed `.leaf-turn` layer above the page, holding a
  full-viewport leaf (cream, with the outgoing page's spine shadow
  at its left and a 3px gilt strip at its right edge), parked
  off-canvas as a 0-width sliver at the spine. On internal
  navigation it rotates in 3D (`rotateY`, `transform-origin: left`,
  `perspective: 1800px` on the layer) across the viewport; the route
  swaps at full coverage; the leaf completes its turn and is removed.
  It enhances real `<a>` navigation in SPA builds and intercepts
  nothing in plain multi-page builds (where it is simply absent —
  see fallback).
- **Motion spec.** Total **650ms `--ease-leaf`**: 300ms covering
  (leaf rotates 0 → ~82°, its face darkening 6% as it leaves the
  light), swap at coverage, 350ms revealing (the leaf's underside —
  cream-deep — rotates away to the right and fades in its last 80ms
  rather than slamming to a stop). The gilt edge strip flashes to
  `--gilt-bright` at the swap instant for 120ms. Pointer is locked
  out during the turn; a second activation during a turn is queued
  as the destination only if it differs, never stacked.
- **Choreography timeline (v2).** t+0: internal link activated →
  leaf lifts from the spine → t+300ms: full coverage; route swaps;
  new page at its top (or at its remembered leaf, for returns) →
  gilt flash → t+300–650ms: underside turns away → t+650ms: layer
  removed, focus moves to the new page's title-page or chapter head
  (§6.11/§6.17 a11y) → t+900ms: watchdog — any turn not completed is
  torn down and the destination shown plainly.
- **State matrix (v2).** *Idle:* no layer in the DOM (it is created
  on activation, removed on completion — a parked full-screen leaf
  is a permanent accident waiting). *Covering / revealing:* per spec.
  *Hover/focus:* links behave as links; the turn decorates activation
  only — keyboard Enter fires the same turn. *Disabled (no JS /
  MPA build):* ordinary navigation; the turn is absent and nothing
  references it.
- **Content merge.** The leaf that turns is the page being left —
  its spine shadow is the rail the reader has seen all page, its
  edge is the gilt edge they have watched fill. The transition is
  made of the page's own furniture, not an overlay branded on top.
- **Failure fallback.** The turn never owns navigation: it enhances
  clicks it can intercept and bypasses middle-click, new-tab,
  modified clicks and external links entirely. If the destination
  takes >3s to be ready, the leaf holds at coverage with the
  bookplate's fleuron pulsing gently on it (the bindery is working)
  — up to 6s, after which the turn aborts, the leaf retreats in
  200ms, and native loading proceeds. The theme never traps a
  visitor inside a turned leaf.
- **Reduced-motion variant.** No rotation. A 150ms crossfade through
  cream — out through paper, in through paper — with the gilt edge
  flashing once at the swap. The book still turns; it turns the way
  a careful reader turns, without the flourish.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: 580ms,
  perspective 1400px. <768px: 500ms, the leaf rotates from the *top*
  spine strip (§6.10's mobile rail) — origin top, `rotateX` — so the
  turn follows the binding wherever the binding is.
- **Edge cases & failure modes (v2).** *Same-page anchor links:* no
  turn — anchors are movements within a leaf. *Back/forward:* never
  intercepted; the browser's gesture rules. *Slow device:* if the
  turn's frame rate measures <30fps during covering, the rotation
  simplifies to the reduced-motion crossfade for that turn — the
  book chooses legibility over ceremony per-instance. *Prefetch:*
  hovered internal links may prefetch; the turn still runs its full
  650ms — the ritual is the point, not the wait.
- **Accessibility spec (v2).** During the turn the outgoing page is
  `inert`; at completion, focus moves to the destination's main
  heading (`tabindex="-1"`) and a polite announcement names the new
  leaf ("Turned to: Chapter 4 — The Long Binding"). Screen-reader
  navigation that manages its own focus skips the turn entirely.
  The turning leaf is `aria-hidden`.
- **Performance budget & mobile variant.** One fixed layer, one 3D
  transform, created and destroyed per navigation. Mobile: as
  breakpoints.
- **Tokens consumed (v2).** `--cream`, `--cream-deep`, `--gilt`,
  `--gilt-bright`, `--ease-leaf`, `--turn-dur` (650ms).


### Page-family elements

### 6.10 Spine-rail contents (page family: navigation)

- **What & why.** Navigation in this theme is the book's contents,
  and it lives where a hand finds a book's structure: on the spine.
  The pinned left rail carries five raised bands — the horizontal
  ribs on a bound spine — and between them the volume's title and a
  contents toggle; the full contents opens as a **contents leaf**: a
  cream panel sliding from the spine listing every chapter with its
  folio, joined by dotted leaders, exactly as a contents page joins
  title to leaf number. It belongs here because a book is not
  navigated by a hamburger; it is opened at its contents, and the
  leaders are the oldest wayfinding line in print.
- **Structure.** `<nav class="spine">` fixed left, 72px, buckram with
  buckram-deep band shading: five raised bands (12px tall, gradient
  shaded) dividing the rail; the volume title set in cream small caps
  reading downward between bands two and three; a "Contents" button
  (cream, ≥44px target) at the rail's foot. The contents leaf:
  `<div class="contents-leaf">` 340px, cream, sliding from the rail,
  listing chapters as §6.13-style lines (numeral, title, leader,
  folio), the current chapter gilt-underlined, dog-eared chapters
  (§6.4) marked with a folded-corner glyph at their line's end.
- **Motion spec.** The leaf opens with the §6.9 grammar at panel
  scale: slides from the spine over **300ms `--ease-leaf`** with its
  fore-edge gilt hairline leading; closes in 240ms. Scrollspy: as
  chapters pass, the current chapter's band-adjacent tick on the rail
  gilds (opacity 200ms) — position on the spine, readable at a
  glance, the way a thumb finds a raised band. The leaf never fades;
  leaves slide or they do not move.
- **Choreography timeline (v2).** t+0: Contents pressed → t+0–300ms:
  leaf slides out, its lines stagger 30ms in reading order (they are
  being *revealed by the leaf's travel*, so the stagger follows the
  slide, not a separate animation) → t+300ms: leaf rests, focus on
  the current chapter's line → Esc or outside click: 240ms close,
  focus returns to the Contents button.
- **State matrix (v2).** *Rail rest:* buckram, title, bands, one gilt
  tick at the current chapter. *Hover (rail):* bands do nothing; the
  Contents button's gilt rule draws under its label (120ms). *Focus:*
  Contents button ringed in gilt-bright on buckram (6.89:1 ✓).
  *Leaf open:* page behind is inert; the rail stays live (it is the
  leaf's hinge). *Scrolled-past:* the rail is pinned — there is no
  scrolled-past for a spine. *Touch:* the rail's strip variant (below)
  carries a Contents button of 48px; the leaf opens full-width.
  *Disabled (no JS):* the contents leaf renders as a static contents
  section at the page's head — a book's contents page is a page, and
  the no-JS book simply opens with it.
- **Content merge.** The contents lists the volume's real chapters
  with their real folios (§6.17's leaf numbers); it is generated from
  the chapters themselves, so a chapter added is a line added — the
  nav cannot drift from the book it binds.
- **Failure fallback.** Plain anchor list in the static contents
  section (no-JS state). Scrollspy is the only JS behaviour on the
  rail; without it the server marks the first chapter current.
- **Reduced-motion variant.** The leaf opens instantly (no slide);
  scrollspy ticks change without transition.
- **Breakpoints (v2).** ≥1200px: 72px rail as specced. 768–1199px:
  56px rail, title shortened to the volume's initials in a gilt
  cartouche. <768px: the rail becomes a 44px **spine strip** across
  the top (bands run vertically, title horizontal small caps,
  Contents button at its right); the contents leaf opens full-width
  below it.
- **Edge cases & failure modes (v2).** *More chapters than the leaf
  holds (>14):* the leaf scrolls internally, its own gilt edge (§6.6
  grammar at leaf scale) showing position — a long contents is a
  directory problem solved by grouping into parts ("Part the First"),
  which the contents shows as part headings. *Volume with one
  chapter:* the Contents button is omitted; a one-chapter book has
  no contents page. *Very long chapter titles:* truncate at 26ch in
  the leaf with the full title in the link's accessible name; the
  chapter's own head is never truncated.
- **Accessibility spec (v2).** Real `<nav aria-label="Contents of
  this volume">`; current chapter carries `aria-current="true"`,
  updated on section change only. The toggle is a `<button
  aria-expanded>`; Esc closes and returns focus. All lines are links,
  ≥40px rows on desktop, ≥48px on touch. Cream on buckram 10.27:1 ✓;
  gilt ticks are decoration beside real text.
- **Performance budget & mobile variant.** Scrollspy on the shared
  IntersectionObserver; the leaf is one transform. Negligible.
  Mobile: the top-strip variant above.
- **Tokens consumed (v2).** `--buckram`, `--buckram-deep`, `--cream`,
  `--gilt`, `--gilt-bright`, `--ease-leaf`, `--leaf-slide` (300ms).

### 6.11 Title-page assembly (page family: hero)

- **What & why.** The home page opens as a book opens: not with a
  hero banner but with a **title page**, assembled in bibliographic
  order — the sequence in which a title page has presented itself for
  centuries: author, title, ornament, imprint. The bookplate (§6.1)
  stamps inside this assembly, because the front cover's inside and
  the title page are the two leaves a reader sees first, in that
  order. It belongs here because the theme's first screen must make
  the volume's claim — *this is a made thing, with a maker, an
  edition and a number, and one of them is yours* — before it sells
  anything, and the title page is the form that makes exactly that
  claim and no other.
- **Structure.** A full-viewport leaf, cream, centred composition on
  the measure: the bookplate (§6.1) at the leaf's upper third, offset
  left of centre as a pasted plate is; then the assembly lines, each
  a real element in reading order: author line (Source Serif small
  caps, tracking 0.14em), a 64px gilt rule, the title (Playfair,
  §3's title size), the subtitle in italic serif where the volume has
  one, the fleuron ornament (static here — the drawn ornament belongs
  to chapter ends, §6.5; the title page's is printed), and at the
  leaf's foot the imprint line: publisher and place, small caps. On
  return visits, the greeting line fades in beneath the bookplate:
  "Copy No. 212, again. The dog-ear is where you left it." — set in
  italic, naming the last folded chapter (§6.4) when one exists.
- **Motion spec.** Lines stagger in bibliographic order at **120ms
  intervals**, each fading/rising 8px over **500ms `--ease-press`**:
  author → rule (draws 64px over 300ms) → title → subtitle → ornament
  → imprint. The bookplate's stamp (§6.1) fires *before* the title
  line — ownership precedes contents (§6.1's timeline). The title's
  light-catch sweep (§6.3) runs once, 150ms after the title lands.
  Total assembly: ~1.9s, and every line is in the DOM, visible, if JS
  never runs.
- **Choreography timeline (v2).** t+0: leaf paints complete (no-JS
  state) → t+120ms: JS arms pre-states → stamp lands (§6.1,
  t+120–320ms) → number types (t+380ms →) → author line +500ms →
  rule draws → title lands → t+150ms: light-catch sweep 1200ms →
  subtitle, ornament, imprint complete the stagger → (return visits)
  greeting fades at t+400ms after the plate → the leaf rests; the
  first endpaper divider (§6.7) waits below the fold.
- **State matrix (v2).** *Rest:* the complete title page — also the
  no-JS state, pixel-identical in content. *Assembling:* 1.9s,
  non-interactive lines (the Contents button on the rail is live
  throughout; assembly never locks the book). *Hover:* the plate's
  gilt border may catch light (§6.3); lines are inert. *Focus:* the
  leaf's only focusable element is the "Begin reading" line at its
  foot (a real link to Chapter 1), ringed per theme. *Scrolled-past:*
  the title page scrolls away whole; it does not pin (the spine
  pins; the title page is a leaf). *Touch:* identical, stagger
  intervals compressed to 90ms.
- **Content merge.** Every line is the volume's real bibliographic
  data — author, title, imprint are the content, presented in the
  order books present them. The assembly animates the arrival of the
  facts, never a decoration in front of them.
- **Failure fallback.** Server-rendered complete. JS arms pre-states
  (opacity/offset) only on elements it will animate, with a 1600ms
  watchdog that restores all lines if the stagger stalls — the title
  page can never be caught half-assembled.
- **Reduced-motion variant.** The complete title page, present. The
  stamp and typing follow §6.1's variant; the greeting is present.
  Nothing is lost but the ceremony of arrival.
- **Breakpoints (v2).** ≥1200px: as specced, plate offset 8% left of
  centre. 768–1199px: plate centred above the author line. <768px:
  title at the clamp's floor, imprint line wraps to two lines, plate
  per §6.1's mobile size; total assembly shortens (90ms staggers).
- **Edge cases & failure modes (v2).** *Volume without an author*
  (anonymous/institutional): the author line is omitted and the
  stagger closes up — the order is bibliographic, and an absent line
  is simply absent, never replaced with a tagline (§9: a marketing
  strapline on a title page is a category error). *Very long title:*
  the clamp and a 3-line cap govern; the title page does not shrink
  the imprint off the leaf — the subtitle is what yields. *First
  visit with storage denied:* plate shows "Copy No. 1", no greeting,
  assembly unchanged.
- **Accessibility spec (v2).** The title is the page's `<h1>`; the
  author line precedes it in the DOM as a `<p>` (title pages are read
  author-first; the heading hierarchy is served by the h1, the order
  by the document). The stagger is visual only — assistive technology
  reads the finished page in order, immediately. All lines ink on
  cream 14.07:1 ✓, imprint in ink at 0.95rem small caps ✓.
- **Performance budget & mobile variant.** DOM + CSS only; the
  assembly is six small transitions. Mobile: as breakpoints.
- **Tokens consumed (v2).** `--cream`, `--ink`, `--gilt`,
  `--ease-press`, `--stagger-bib` (120ms), `--line-rise` (500ms).

### 6.12 Frontispiece plate (page family: image / plate)

- **What & why.** A fine edition's principal image is a frontispiece:
  a plate printed separately, guarded by a sheet of tissue, facing
  the title page, captioned simply "Frontispiece." This element is
  the theme's image treatment in its fullest form — every image in
  the volume is a plate (§5), but the frontispiece is the plate of
  plates: gilt-framed, tissue-guarded, revealed as the guard lifts.
  It belongs here because it gives the volume's most important image
  the ceremony the material affords, and because the tissue guard —
  a translucent leaf whose whole job is to protect and then reveal —
  is the theme's native answer to the image reveal: not a fade, not
  a zoom, a guard lifted by the reader's arrival.
- **Structure.** A `<figure class="plate frontispiece">` facing the
  title page (on desktop, the leaf after the title page; the two are
  a spread). The image — always the real image, real `alt`, in the
  DOM from first paint — sits in a **double-rule gilt frame** (outer
  3px gilt, 6px cream mat, inner 1px gilt-deep), aspect chosen per
  plate at content time. Over it, the **tissue guard**: an absolutely
  positioned cream layer at 38% opacity with the plate's title set on
  it in italic, which lifts (below). Beneath the frame, the caption:
  "Frontispiece." followed by the plate's description in italic
  (§3). A plate number ("Plate I") sits at the frame's top-right in
  small caps.
- **Motion spec.** Trigger: the plate's centre crosses 60% of
  viewport height. The guard lifts over **900ms `--ease-leaf`**: it
  translates up 12px while its opacity falls 0.38 → 0 — a sheet
  being drawn back, not a fade-out in place — and the image beneath
  scales **1.04 → 1** within the frame across the same span (the
  plate settles into its frame as it is uncovered). Simultaneously
  the frame's gilt catches light once (§6.3's grammar, 900ms sweep
  across the frame's top rule). Once per page-load; the guard never
  re-lowers.
- **Choreography timeline (v2).** t+0: trigger → guard begins to
  lift, image at 1.04 → t+450ms: guard at half opacity, the plate's
  subject legible through it — the tissue moment, the image arriving
  *through* paper → t+900ms: guard gone (removed from the tree, not
  merely transparent), image at 1.0, frame sweep completes → caption
  fades in 400ms — the plate is read after it is seen, in that order.
- **State matrix (v2).** *Rest (pre-trigger):* the image present
  under the guard — visible, softened, never hidden; the guard is a
  veil, not a curtain, and the plate can be identified through it.
  *Lifting:* 900ms. *Revealed (terminal):* the framed plate, guard
  absent. *Hover:* after reveal, the frame's gilt catches light at
  the pointer's angle (§6.3). *Focus:* if the plate is a link (to
  its chapter), focus lifts the guard instantly if it has not lifted
  — a focused plate is a read plate. *Scrolled-past:* revealed.
  *Touch:* the lift triggers at the same viewport line; no hover
  states. *Disabled (no JS):* **no guard is rendered** — the guard
  exists only as a JS-applied layer over a complete plate, because a
  guard that can never lift is a defect, not a default.
- **Content merge.** The guard carries the plate's title; the frame
  is the plate's own binding; the caption is the plate's
  description. Every moving part is the plate's furniture.
- **Failure fallback.** If the image has not loaded by the trigger,
  the guard holds (the plate is genuinely not ready) up to a 2000ms
  watchdog, after which the guard lifts anyway onto whatever has
  arrived — an empty frame is never guarded for long, and the alt
  text stands in the frame's mat area as interim caption. If the
  image 404s, the frame holds the caption and a fleuron — a plate
  that failed to print is recorded as such, never swapped for stock.
- **Reduced-motion variant.** No guard, no scale. The plate stands
  framed with its caption — the guard is a motion ceremony, and
  reduced motion is the state where the book is simply open.
- **Breakpoints (v2).** ≥1200px: plate up to 560px wide, facing the
  title page. 768–1199px: 480px, below the title page. <768px:
  full-measure width, guard lift shortens to 700ms, scale range
  1.03 → 1.
- **Edge cases & failure modes (v2).** *Plate image is a portrait
  (tall):* the frame's aspect follows the plate; the guard's title
  sits at the frame's lower third so it never veils a face at rest —
  a content rule, checked at the gate. *Multiple plates in one
  chapter (detail pages):* only the first is a frontispiece with a
  guard; subsequent plates are plain §5 plates (frame + caption +
  scale-in capped at 1.02) — one guard per volume section, or the
  ceremony becomes a curtain call. *Plate inside the contents leaf
  or cards:* never — plates live on leaves, thumbnails in §6.13 are
  numerals, not pictures.
- **Accessibility spec (v2).** The `alt` is the plate's full
  description; the visible caption repeats it in prose, so where the
  caption is complete the image may be `alt=""` — choose per build,
  consistently. The guard is `aria-hidden` and its title duplicates
  the caption's first words. Focus behaviour per state matrix.
  Caption 0.94rem italic ink on cream, 14.07:1 ✓.
- **Performance budget & mobile variant.** One image (≤180KB,
  responsive sizes), one overlay layer, one transform. The guard is
  removed from the tree after lifting — it costs nothing at rest.
  Mobile: as breakpoints.
- **Tokens consumed (v2).** `--gilt`, `--gilt-deep`, `--cream`,
  `--ink`, `--ease-leaf`, `--guard-lift` (900ms).


### 6.13 Chapter cards — "Bound with this volume" (page family: cards / listing)

- **What & why.** The listing unit in this theme is not a card with a
  thumbnail; it is a **contents line that has been given room** — a
  chapter entry set the way the contents leaf (§6.10) sets it, at
  reading size: roman numeral, title, a standfirst in the chapter's
  own first sentence, dotted leaders to the folio, and — where the
  reader has been — the gilt of a finished illumination or the fold
  of a dog-ear. It belongs here because a volume's parts are listed
  the way the volume lists them; importing a grid of image cards
  would paste a bookshop's shelf-talker onto a contents page. The
  list *is* the contents, promoted to a page.
- **Structure.** An `<ol class="chapter-list">` of `<li>` entries,
  each a single link wrapping: the numeral (Playfair, gilt-deep, at
  1.6rem), the title (Playfair 600, 1.35rem, ink), the standfirst
  (Source Serif, 2 lines max, the chapter's real opening sentence —
  never lorem, never a marketing paraphrase), the leader (dotted
  `--hairline` flex line), and the folio ("leaf 12", small caps).
  State furniture at the line's right: a miniature gilt bar showing
  the chapter's illumination fraction (§6.2's `p`, as a 28px gilt
  rule filling) for chapters in progress, a folded-corner mark for
  dog-eared chapters (§6.4), and nothing at all for unread chapters —
  an untouched line is the honest default.
- **Motion spec.** Entry: lines fade/rise in reading order as the
  list crosses the trigger (each 400ms `--ease-press`, 60ms stagger,
  capped: beyond 8 lines the rest arrive together — a long contents
  does not perform itself line by line for a full second). Hover:
  the numeral catches gilt light (§6.3) and the leader dots draw
  from title toward folio (background sweep, 200ms) — the eye is led
  down the line the way a finger runs a contents page. The
  illumination mini-bar is set from stored scroll state on render;
  it does not animate on the listing page (records do not perform).
- **Choreography timeline (v2).** List enters at 78% vh → lines
  arrive 60ms apart to the 8-line cap → rest. Hover: t+0 leader sweep
  begins → t+200ms leader complete, numeral lit → leave: leader
  relaxes 240ms. Nothing else ever moves on the line.
- **State matrix (v2).** *Rest:* printed contents line. *Hover:*
  leader draw + numeral catch. *Focus:* same as hover, plus ring on
  the link — keyboard readers run the same finger down the same line.
  *Active:* the title inks to buckram for the press (120ms) — the
  chapter is being opened. *Visited/in-progress:* mini-bar at its
  true fraction; *dog-eared:* corner mark. *Scrolled-past:* printed.
  *Touch:* no hover; the line is a 56px row, tap goes through to the
  leaf-turn (§6.9). *Disabled (no JS):* the full list, printed, with
  mini-bars at their server-known state (usually absent — the list
  is complete without them).
- **Content merge.** Every element of the line is the chapter's own
  data: its numeral, its title, its first sentence, its folio, its
  reading state. There is no decoration on the line that is not the
  chapter describing itself.
- **Failure fallback.** A static contents list. The mini-bar and
  corner marks are enhancements layered on a complete line; their
  absence changes nothing about the list's legibility or order.
- **Reduced-motion variant.** No entry stagger, no leader draw: the
  list is printed, hover changes only the numeral's colour mix
  (gilt-deep → gilt, instant).
- **Breakpoints (v2).** ≥1200px: lines at full measure, standfirst
  beside the title in a two-column line (title left 55%, standfirst
  right). 768–1199px: standfirst drops beneath the title. <768px:
  folio moves to the line's second row with the standfirst; leaders
  shorten to a minimum 24px and wrap rather than squeeze.
- **Edge cases & failure modes (v2).** *Chapter without a standfirst:*
  its first sentence is extracted at build time; a chapter whose
  first sentence exceeds 30 words is excerpted at the first clause —
  the rule is mechanical so no editor invents a teaser (§9).
  *Folio unknown* (chapter not yet paginated — a serialised volume):
  the folio reads "in preparation" in italic — a real bibliographic
  state, used honestly, never a fake number. *List of one:* renders
  as a single line without the list's head — the contents of a
  one-chapter volume is its title page's job (§6.11).
- **Accessibility spec (v2).** One link per line, named by numeral +
  title ("Chapter 3 — The Long Binding"); the standfirst is inside
  the link's text and read as part of it — keep standfirsts short for
  this reason. The mini-bar is `aria-hidden` with the state stated
  in words for in-progress chapters ("partly read") appended
  visually-hidden to the link name. Leaders are CSS, invisible to
  AT. Rows ≥48px on touch.
- **Performance budget & mobile variant.** Pure DOM/CSS; the entry
  stagger is capped at 8 lines. Negligible. Mobile: as breakpoints.
- **Tokens consumed (v2).** `--ink`, `--gilt`, `--gilt-deep`,
  `--hairline`, `--ease-press`, `--leader-draw` (200ms).

### 6.14 The binder's order form (page family: forms / conversion)

- **What & why.** Every limited edition ends with an order leaf — the
  subscription form bound at the back, to be filled in and returned
  to the binder. This theme's conversion form is that leaf: ruled
  lines to write on, the edition's terms stated in the edition
  statement's voice, and a submit that does not say "Success!" — it
  **stamps a second bookplate** with the reservation and the
  visitor's own copy number. It belongs here because conversion in a
  book is an act of inscription: the reader writes their name in the
  volume's records, and the volume answers with a plate. A funnel
  would be a foreign object; an order leaf is the same object as
  everything else in the book, doing the book's business.
- **Structure.** A `<form class="order-leaf">` on a cream-deep leaf,
  framed by a buckram double rule: a head line in small caps ("Order
  leaf — to reserve a copy"), fields as bottom-ruled inputs
  (transparent ground, 2px ink bottom rule, labels above in the
  apparatus voice), the edition terms as three short lines of edition
  statement prose (edition size, what a reservation holds, when it
  lapses — real terms, supplied by the publisher), one consent line
  with a square checkbox drawn as a small gilt frame that fills with
  a fleuron when checked, and the submit: a buckram button, cream
  small caps, "Reserve this copy". On success the form is replaced
  by the **reservation plate**: a bookplate (§6.1's furniture) reading
  "Reserved — Copy No. 212" with the reserving name beneath, stamped
  in.
- **Motion spec.** Entry: the leaf's frame draws (its rules, 400ms
  `--ease-gilt`) as it enters; fields never animate individually.
  Focus: the field's rule thickens 2px → 3px and a gilt line slides
  beneath it from the left (200ms `--ease-press`) — the line being
  written on is underlined by the binder. Error: the rule turns
  buckram (the theme's only error colour — gilt is precious, ink is
  neutral, buckram is the binding saying *no*), and the error text
  appears beneath in the errata voice (§6.16, §12) with a 300ms fade.
  Submit press: the button presses 1px (platen grammar, §5). On
  success: the reservation plate stamps in per §6.1 (scale 1.25 → 1,
  200ms `--ease-press`) and the form leaf fades to the plate over
  300ms — the leaf is replaced by its own record.
- **Choreography timeline (v2).** t+0: submit → button press, form
  validates locally → errors (if any) appear in errata voice, focus
  moves to the first error field → clean: form submits → t+response:
  plate stamp 200ms → t+500ms: the stamped plate rests with the
  reservation line beneath it ("A confirmation has been sent to the
  address on this leaf.") — a statement of fact the build must make
  true, or not print (§10).
- **State matrix (v2).** *Rest:* the ruled leaf, terms printed.
  *Focus (field):* rule thickens, gilt underline slides. *Error
  (field):* buckram rule, errata line beneath, `aria-invalid` set.
  *Submitting:* button pressed state held, fields inert, no spinner
  — a small "The binder is writing…" line in italic at the leaf's
  foot (the theme's only loading text). *Success:* the reservation
  plate (terminal). *Edition exhausted:* the form is replaced at
  render by the waiting-list leaf ("This edition is fully reserved.
  Leave a name for the next printing.") — one field, same furniture
  (§6.8's agreement law). *Touch:* fields ≥48px tall, the gilt
  underline still runs. *Disabled (no JS):* a plain working form —
  server validation, server-rendered errors in the same voice; the
  stamp is the only casualty.
- **Content merge.** The form's terms are the edition's real terms;
  the plate it stamps carries the visitor's real copy number (§6.1)
  and the name they entered. The conversion's reward is a piece of
  the book itself, inscribed — not a confetti event.
- **Failure fallback.** Server 500 or network failure: the leaf
  stays, the visitor's entries intact (never cleared), with an
  errata line at its head: "Erratum — this leaf could not be sent.
  Your entries are kept above; try again." (§12's error voice,
  verbatim pattern.) Double-submit is impossible: the button
  disables on first activation until a response or a 6s timeout
  returns it with the errata line.
- **Reduced-motion variant.** No frame draw, no stamp: the success
  plate appears with a 150ms fade. Focus underlines are instant.
  All states and copy unchanged.
- **Breakpoints (v2).** ≥1200px: leaf at 34rem, centred, terms in a
  right column beside the fields. 768–1199px: terms above the fields.
  <768px: leaf full-measure, fields single column, the plate at
  §6.1's mobile size.
- **Edge cases & failure modes (v2).** *Visitor without a copy
  number* (storage denied): the plate reads "Reserved — Copy No. 1"
  per §6.1's fallback, and the confirmation does not claim a number
  was recorded server-side — the reservation is keyed to the order,
  not the browser's number; the copy keeps them consistent only in
  the visitor's own copy, which is the theme's honest scope.
  *Reservation for someone else (gift):* the name field is "Name for
  the bookplate" — the plate prints the name entered, which is the
  point of a bookplate. *Autofill:* ruled fields accept it; the gilt
  underline treats autofilled as focused-then-rested, no animation
  storm on page load.
- **Accessibility spec (v2).** Labels are real `<label>`s in the
  apparatus voice; errors are text, linked by `aria-describedby`,
  never colour-alone (the buckram rule is a supplement to the words).
  The success plate's text is real text and is announced via a polite
  live region ("Reserved — Copy No. 212"). Focus order follows the
  leaf top to bottom; the terms column is read before the fields it
  governs. Buckram button, cream text 10.27:1 ✓.
- **Performance budget & mobile variant.** The form is DOM/CSS; the
  stamp reuses §6.1's keyframes. Negligible. Mobile: as breakpoints.
- **Tokens consumed (v2).** `--cream`, `--cream-deep`, `--buckram`,
  `--ink`, `--gilt`, `--ease-press`, `--ease-gilt`, `--stamp-dur`
  (200ms).

### 6.15 Colophon footer (page family: footer)

- **What & why.** The footer of a fine edition is its colophon: the
  statement, set at the very end, of how the book was made — the
  edition's size, the type it was set in, who printed it, and the
  number of this copy. This theme's footer is that block, and nothing
  else wearing a footer's clothes: the edition statement, the
  copies-remaining line (§6.8), the copy's own number repeated ("This
  copy: No. 212"), the printer's ornament, and — set as a contents
  list, not a link farm — the volume's chapters for the reader who
  arrived at the end and wants the beginning. It belongs here because
  a colophon is the one part of a book whose entire job is honest
  accounting, and a footer that accounts honestly for the edition is
  worth more than any trust badge.
- **Structure.** A centred block on cream, max-width 40rem, after the
  final chapter (or at any page's foot, in its short form — see
  states): a gilt rule 64px; the edition statement in Source Serif
  small caps and regular, centred, lines in bibliographic order —
  edition size and limitation, the type line ("Set in Playfair
  Display and Source Serif 4"), the making line (publisher, place,
  year), the copies-remaining line (§6.8), "This copy: No. [n]" (the
  §6.1 number, repeated as text); the printer's ornament (static);
  then the contents list (§6.13's lines at footer density) under the
  head "Contents of this volume"; finally the legal line in 0.8rem —
  the one place small print is allowed, because colophons have
  always carried it.
- **Motion spec.** On entry, the statement's lines fade in
  bibliographic order, 90ms stagger, 500ms `--ease-press` each — the
  same grammar as the title page (§6.11), closing the volume with
  the gesture that opened it. The copies-remaining count runs inside
  its line (§6.8). Nothing else moves; a colophon does not perform
  beyond its statement.
- **Choreography timeline (v2).** Final ornament drawn (§6.5) →
  "Finis" faded → reader scrolls the last screen → gilt rule →
  statement lines stagger → count descends within its line → ornament
  (static) → contents lines (no stagger; records) → legal line. The
  volume ends in this order, always.
- **State matrix (v2).** *Full form* (end of the volume / home page):
  as specced. *Short form* (interior pages): edition line + "This
  copy: No. n" + contents link to the contents leaf — a running
  colophon, three lines, no stagger, no count (the count lives at
  the volume's end only; repeating scarcity per page is §9).
  *Hover/focus:* contents lines behave per §6.13. *Scrolled-past:*
  n/a — the colophon is the past. *Disabled (no JS):* the full
  statement, printed, count at its true figure (§6.8).
- **Content merge.** Every line is a fact about this edition: its
  size, its type, its maker, its remaining copies, this copy's
  number. The footer contains no marketing copy whatsoever — if a
  line could appear on any other site's footer, it does not belong
  in a colophon (§9).
- **Failure fallback.** Static text. The only dynamic values are the
  count (§6.8's rules) and the copy number (§6.1's fallback: "No. 1"
  printed). A colophon with JS disabled is a colophon.
- **Reduced-motion variant.** The statement is present; the count is
  printed at its figure. No stagger.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: contents at
  footer density in two columns. <768px: single column, statement
  lines wrap centred, legal line left-aligned for legibility.
- **Edge cases & failure modes (v2).** *Copy number unavailable:*
  "This copy: No. 1" per §6.1 — stated plainly, never hidden (hiding
  the line would admit the number was decoration). *Edition statement
  facts change* (a second impression): the colophon is updated and
  gains a line — "Second impression, [year]" — because colophons
  record impressions; the copy number does not change (§6.1's law).
  *Page that is not part of the volume* (checkout, account): short
  form only, and "This copy" still appears — the copy follows the
  reader through the bindery's business pages.
- **Accessibility spec (v2).** A real `<footer>`; the statement is
  ordinary text in order; the contents list is a `<nav>` labelled
  "Contents of this volume". Small caps via §3's law. Legal line at
  0.8rem in ink (14.07:1 ✓ — small print is a size, never a contrast
  dodge).
- **Performance budget & mobile variant.** Text and one static SVG.
  Negligible. Mobile: as breakpoints.
- **Tokens consumed (v2).** `--cream`, `--ink`, `--gilt`,
  `--ease-press`, `--stagger-bib` (90ms here).


### 6.16 Errata slip (page family: alerts / notices)

- **What & why.** Books that are wrong get errata slips — small
  printed slips tipped in at the relevant page, saying what was
  wrong and what should stand instead. This theme's alert is that
  slip: a small cream-deep leaf, pasted at the head of the content it
  corrects, carrying corrections, warnings and notices in the errata
  voice ("Erratum — … For … read …"). It belongs here because it
  gives the theme an honest alert grammar: a notice in a book is not
  an interruption shouted over the page; it is a slip pasted into it,
  by the publisher, admitting something. Toasts are refused (§11) —
  a toast is a shout that vanishes; an errata slip stays until the
  reader removes it, because a correction the reader missed is a
  correction never made.
- **Structure.** A `<div class="errata-slip" role="note">` (or
  `role="alert"` for the rare urgent correction), max-width 30rem,
  cream-deep with a deckled fore-edge (a 3px irregular border-image
  of torn paper in cream-deep tones), pasted at a fixed −0.6°
  rotation, with a paste shadow at its head edge. Its text: the
  erratum in italic serif, one correction per slip, and where the
  correction is actionable, one link set in the slip's own line
  ("Read the corrected leaf"). A small "Remove slip" button (×, in
  the slip's corner, 32px target minimum, labelled in words for AT)
  dismisses it; dismissal is remembered per slip id in localStorage
  (`fe.errata`), so a corrected reader is not re-corrected.
- **Motion spec.** Appearance: the slip slides from beneath the leaf
  it corrects — translateY(−8px) → 0 with opacity, **300ms
  `--ease-press`** — as if slipped in from the top edge; it never
  drops, bounces or slides from a screen corner. Dismissal: it
  slides back up 240ms and is removed; a faint paste shadow (a
  cream-deep smudge at 40%) remains at its place for the rest of the
  page-load — the mark where a slip was, which is what a removed
  slip leaves in a real book.
- **Choreography timeline (v2).** Page renders → slip present in DOM
  at final position (pre-state JS-applied) → if the slip is new to
  this copy: t+600ms after the leaf settles (never during the
  title-page assembly or a leaf-turn) the slip slides in 300ms →
  rests until dismissed or the leaf is left → dismissal: 240ms out,
  paste shadow remains.
- **State matrix (v2).** *Rest (undismissed):* the slip, legible,
  part of the leaf's furniture. *Hover:* none (the slip is paper;
  its button has the theme's focus/hover ring). *Focus:* the Remove
  button and any link are the leaf's first tab stops when the slip
  is present — a correction is read before the text it corrects.
  *Dismissed:* gone, paste shadow for the session, id stored.
  *Scrolled-past:* the slip scrolls with its leaf — it is tipped
  *in*, not floating. *Touch:* identical; targets per spec.
  *Disabled (no JS):* the slip is simply present, with a working
  server-side dismiss link (a GET that sets the record) or, where
  that is impossible, present permanently — an undismissable
  printed slip is still a valid book object.
- **Content merge.** The slip corrects *this leaf's* content and
  sits on this leaf. A site-wide notice (maintenance, a general
  warning) is not an erratum — it belongs on the title page's imprint
  line or nowhere; the gate rejects slips whose text is not a
  correction of, or a notice about, the page they are pasted into.
- **Failure fallback.** The slip is content, rendered by the server;
  its animation is the only JS. If storage fails, dismissal lasts
  the session. If two slips target one leaf, they stack with 12px
  offset — never more than two; a third waits for a dismissal (a
  leaf with three slips pasted on it is a publisher's emergency, and
  the build should fix the leaf instead).
- **Reduced-motion variant.** The slip is present; dismissal is
  instant; no paste shadow (a motionless smudge reads as a stain,
  and the shadow's meaning is the memory of the slide).
- **Breakpoints (v2).** ≥1200px: 30rem, in the fore-edge margin's
  column at the leaf's head. 768–1199px: full measure width at the
  leaf's head. <768px: full width, rotation 0° (a small screen's
  slip is pasted straight; the charm is rationed by the space).
- **Edge cases & failure modes (v2).** *Urgent correction* (a wrong
  price in the edition terms, a wrong date): `role="alert"`, the
  slip's head carries a buckram rule, and it is pasted on every leaf
  the error touches until the leaf itself is corrected — then the
  slip is withdrawn by the publisher, not by expiry timers.
  *Slip correcting the order form:* pasted directly above the form
  leaf (§6.14), and the form's own error voice borrows the errata
  pattern for consistency. *Stale slip* (the correction no longer
  true): withdrawn at publish time; slips carry no client-side
  expiry logic — a book does not unpaste its own errata.
- **Accessibility spec (v2).** `role="note"` by default (not
  announced aggressively); `role="alert"` only for the urgent class.
  The slip's text is italic ink on cream-deep (12.62:1 ✓) at ≥0.95rem.
  The Remove button's accessible name is "Remove this errata slip";
  the × is decoration beside it. Dismissal never moves focus into
  the void: focus passes to the leaf's heading.
- **Performance budget & mobile variant.** One small element, two
  short transitions. Negligible. Mobile: as breakpoints.
- **Tokens consumed (v2).** `--cream-deep`, `--ink`, `--buckram`,
  `--ease-press`, `--slip-in` (300ms).

### 6.17 Running heads & folios (page family: page furniture / header)

- **What & why.** A book's pages carry furniture: a running head
  naming the volume and the chapter, and a folio — the leaf number —
  in the margin. This element is that furniture for the reading page:
  the running head at the text column's top naming the current
  chapter, and in the fore-edge margin the folio, "leaf 7 of 23",
  updating as chapters pass. It belongs here because it is the
  theme's *verbal* progress system — the gilt edge (§6.6) shows
  progress to the eye; the folio states it in words, in the margin
  where a reader's thumb rests, in the book's own units. The two are
  specified to agree (§6.6), and the folio is the one assistive
  technology can read.
- **Structure.** A `<div class="running-head">` at the head of the
  reading column (not fixed — it is furniture printed on each
  chapter's first leaf, repeated per chapter, plus a slim fixed
  variant on long chapters — see states): left, the volume title in
  small caps; right, the current chapter's short title, small caps;
  a hairline beneath. The folio: `<p class="folio">` positioned in
  the fore-edge margin at the current chapter's vertical position —
  in practice, a fixed margin element whose text updates: "Leaf 7 of
  23", with the chapter's roman numeral beneath ("Chapter III") at
  0.75rem in gilt-deep. Leaf numbers are computed from the volume's
  chapter map: each chapter occupies a stated number of leaves (its
  reading length in screens, set at build time), and the folio
  interpolates within the chapter by scroll fraction — leaf 7 *of
  the chapter's span*, honestly derived from the map, never a raw
  scroll percentage wearing words.
- **Motion spec.** Chapter change: the running head's chapter title
  crossfades (opacity, **200ms `--ease-press`**) and the folio's
  figures swap at the same beat — furniture changes when the leaf
  turns, not continuously. Within a chapter, the folio's leaf number
  steps at the chapter-map's leaf boundaries (each ~100vh of reading)
  with the same 200ms fade. No sliding, no counting — a folio is
  printed per leaf, and print changes in steps.
- **Choreography timeline (v2).** Continuous and stepped: chapter
  boundary crossed → head title and folio fade out 100ms → swap →
  fade in 100ms → the gilt edge's chapter tick brightens at the same
  moment (§6.6) — the eye's system and the word's system tick
  together, by specification.
- **State matrix (v2).** *Rest:* current chapter's furniture,
  printed. *Chapter change:* 200ms crossfade. *Hover/focus:* the
  furniture is not interactive. *Scrolled-past:* n/a. *Long chapter
  (>4 leaves):* a slim fixed variant of the running head (volume
  title + chapter, 36px, cream at 92% with a hairline) appears after
  the chapter's first leaf and leaves at its ornament — the book's
  answer to a sticky header, admitted only where a chapter is long
  enough to lose the reader. *Disabled (no JS):* each chapter's own
  printed running head stands at its head with its opening folio
  ("Leaf 7" — the chapter's first leaf, no "of 23" interpolation);
  the fixed variant and the stepping are the JS layer.
- **Content merge.** The furniture names this volume and this
  chapter and counts this page's leaves from the volume's real map.
  It is generated from the same chapter data as the contents (§6.10)
  — the three records (contents, folio, edge) cannot disagree,
  because they are one record printed three ways.
- **Failure fallback.** Per-chapter printed heads (the no-JS state)
  are the designed default; the fixed variant and stepping enhance
  them. If the chapter map is missing for a page, the folio is
  omitted rather than guessed — an absent folio is a plainer leaf; a
  wrong folio is a broken book.
- **Reduced-motion variant.** Furniture swaps instantly, no
  crossfade. The fixed variant still appears (it is position, not
  motion) but without its fade-in.
- **Breakpoints (v2).** ≥1200px: folio in the fore-edge margin as
  specced. 768–1199px: folio moves inline at the running head's right,
  beneath the chapter title ("Leaf 7 of 23" at 0.75rem). <768px: the
  running head compresses to chapter title only (the volume title is
  on the spine strip, §6.10) and the folio sits inline after it,
  separated by a fleuron.
- **Edge cases & failure modes (v2).** *Chapter with a very long
  title:* the running head uses the chapter's stated short title
  (a build-time field; if absent, the title truncates at 34ch with
  an ellipsis — the only ellipsis allowed in the theme's furniture).
  *Non-chapter pages* (order leaf, contents leaf): their running
  head names the part ("The Order Leaf") and the folio reads the
  part's place ("After Chapter XII" / "At the end of the volume") —
  books have front and back matter, and the furniture says so rather
  than forcing a chapter number. *Leaf count changes between builds*
  (a chapter lengthened): the map is regenerated at build; stored
  dog-ears key on chapter ids, not leaf numbers, so nothing the
  reader marked moves.
- **Accessibility spec (v2).** The running head is `aria-hidden` in
  its fixed variant (it duplicates the chapter heading); the printed
  per-chapter heads are part of the chapter's heading group. The
  folio is real text, *not* aria-hidden — it is the accessible
  progress statement — placed in the DOM at the chapter head so it
  is read in position, and its fixed updates are **not** live-region
  announced (a folio that speaks every leaf is a torment; it is
  there to be asked, not to interrupt).
- **Performance budget & mobile variant.** Text swaps on section
  change from the shared observer. Negligible. Mobile: as
  breakpoints.
- **Tokens consumed (v2).** `--ink`, `--gilt-deep`, `--hairline`,
  `--ease-press`, `--furniture-fade` (200ms).

### 6.18 Half-title skeleton + the unbound leaf (page family: loader / 404)

- **What & why.** Two states every site has and most themes improvise:
  waiting, and not-found. Here both are book objects. Loading shows
  the **half-title** — the leaf before the title page that carries
  the book's title alone — with ruled lines where the text will be:
  the volume, present but not yet open. A missing page is **the
  unbound leaf**: a single loose sheet, not attached to the spine,
  stating plainly that this leaf was never bound into this volume,
  and offering the contents as the way back into the book. They
  belong together and here because they are the theme's two honest
  admissions — *not yet* and *not here* — made in the book's own
  furniture instead of a spinner and a cartoon.
- **Structure.** *Skeleton:* a cream leaf at the reading measure:
  the volume's title in Playfair at title-page size (the real title,
  server-rendered), a 64px gilt rule, then ruled lines (hairline
  bars at body measure, widths 100/92/100/64% per paragraph block)
  and a plate frame (cream-deep, gilt double rule) where a plate
  will stand. Chapter skeletons repeat the anatomy: numeral bar,
  title bar, cap-sized gilt-deep square at the first line's head.
  *Unbound leaf:* a cream sheet rendered *without* the spine rail's
  attachment — on the 404 page the rail is present but the leaf sits
  24px proud of it with a loose shadow, visibly unsewn; its text:
  "This leaf was never bound." in Playfair, then in the edition
  voice: the address the reader sought, stated as a citation ("The
  leaf called /chapter-13 was not bound into this copy."), the
  contents list (§6.13 lines) as "The volume contains:", and the
  title page offered as the way home.
- **Motion spec.** *Skeleton:* the ruled lines carry a gilt sheen
  passing left to right over **1600ms `--ease-gilt`**, looping while
  content loads — the half-title under a moving light, the theme's
  only sanctioned shimmer, because it moves across *furniture*, not
  text. Content arrival: each block replaces its ruled lines with a
  240ms fade, in reading order, no stagger theatre. Hard cap: any
  block still ruled at **2500ms** loses its sheen and stands as plain
  ruled lines (the book waits without performing), and at 6000ms the
  skeleton yields to an errata line ("This leaf is slow to arrive —
  it is still being gathered.") with a retry link. *Unbound leaf:*
  static; its one motion is arrival — it settles 6px with a 300ms
  `--ease-leaf` as the page loads, a loose sheet laid on the desk.
- **Choreography timeline (v2).** Skeleton: t+0 half-title paints
  (server-rendered, so first paint is already the book) → sheen
  loops → blocks land in reading order, 240ms fades → the leaf is
  the page; the skeleton never "completes" with a flourish.
  Unbound: t+0 leaf settles 300ms → rest; the contents lines are
  live immediately.
- **State matrix (v2).** *Skeleton loading / degraded (2500ms) /
  stalled (6000ms, errata + retry):* as specced. *Skeleton disabled
  (no JS):* server-rendered pages ship content, not skeletons —
  skeletons exist only inside client fetches that own their timers.
  *Unbound rest:* static sheet. *Hover/focus:* contents lines per
  §6.13. *Touch:* identical.
- **Content merge.** The skeleton is the page's own anatomy in ruled
  form — same measure, same furniture positions, zero layout shift
  by construction. The unbound leaf's contents list is the volume's
  real contents; its citation names the real missing address.
- **Failure fallback.** A fetch error inside a skeleton block
  resolves that block into an errata slip (§6.16) in place — the
  leaf admits its gap in the book's voice rather than spinning. The
  404 leaf has no failure mode of its own; it *is* the failure mode,
  designed.
- **Reduced-motion variant.** Skeleton: ruled lines without sheen;
  blocks appear. Unbound leaf: no settle. Both states lose nothing
  but light.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: skeleton
  measure follows §4. <768px: the unbound leaf sits flush (the 24px
  proud offset becomes 10px and its shadow softens — a small screen
  shows looseness subtly), contents lines full width.
- **Edge cases & failure modes (v2).** *404 for a leaf that exists
  under another address* (moved chapter): the citation adds the
  errata pattern — "For /chapter-13 read /chapter-12" with the link
  — a redirect performed as a correction, in the open. *Skeleton for
  the order form:* the form leaf skeleton keeps its frame and rules;
  fields are never skeletonised into fake inputs a visitor might
  type into early — ruled lines only, and the real form replaces
  them whole. *Search engines:* the unbound leaf is served with a
  true 404 status; its charm does not extend to lying to crawlers.
- **Accessibility spec (v2).** Skeleton regions carry
  `aria-busy="true"` and one polite announcement ("The volume is
  being gathered") — once, not per block. Ruled lines are
  `aria-hidden`. The unbound leaf's heading is the page's `<h1>` and
  its citation is plain text; the contents list is a labelled nav.
  All text ink on cream ✓.
- **Performance budget & mobile variant.** The skeleton is CSS bars
  and one sheen gradient — no assets. The unbound leaf is one page
  of DOM. Negligible. Mobile: as breakpoints.
- **Tokens consumed (v2).** `--cream`, `--cream-deep`, `--ink`,
  `--gilt`, `--hairline`, `--ease-gilt`, `--ease-leaf`,
  `--sheen-dur` (1600ms), `--skeleton-cap` (2500ms).


## 7. Page application map

**Home — the volume itself.** Title page (§6.11) with bookplate
(§6.1), frontispiece (§6.12), then the chapters in order with their
full anatomy, endpaper dividers (§6.7) between gatherings, and the
colophon (§6.15) at the foot. The home page *is* the book; a build
that gives the home page a different, more "marketing" structure than
the reading pages has bound two books in one cover.

**Listing — the contents leaf as a page.** A part-title ("Contents of
this volume"), then §6.13's chapter lines at full density, grouped by
parts where the volume has them. Filters, where a build truly needs
them, are an **index** (by subject, by plate, by part) set as index
entries at the list's head — books are filtered by their indexes, and
the index is a text object, not a toolbar. No grid view exists; a
toggle between "contents" and "grid" is a §9 failure.

**Detail — a single chapter.** The full chapter anatomy at reading
length: running head and folio (§6.17), illuminated cap (§6.2),
plates (§6.12 grammar at plain-plate scale), ornament close (§6.5),
and at its foot the endpaper divider carrying the *next* chapter's
numeral — the detail page ends by turning toward the next leaf, never
with a "related items" rail. Cross-references within the text are set
as marginal notes in the fore-edge margin (small caps head, italic
note), the book's native aside.

**About — the edition statement page.** The maker's page is set as an
expanded colophon: how this volume came to be, who made it, the
edition's history and impressions, with a plate of the maker as its
frontispiece (§6.12). An About page in this theme that reads like a
startup's — values cards, team grid — has left the book; the colophon
form carries the same facts with the theme's authority instead.

**Contact / order — the order leaf.** §6.14, reached as back matter:
the running head names it "The Order Leaf", the folio reads "At the
end of the volume" (§6.17), and the colophon short form closes the
page. Checkout beyond reservation (payment) keeps the leaf's
furniture and voice; the payment fields are ruled lines like any
other, and the confirmation is the stamped plate (§6.14) — there is
no separate "success page" design language.

**Contents / index pages.** The contents leaf (§6.10) as a full page
for long volumes; the index, where built, as two-column small-type
entries with leaf references — the densest page in the book, and the
one place small type is a virtue.

**404 — the unbound leaf** (§6.18). **Search results — index
entries**: query stated as a citation ("Leaves mentioning *gilt*"),
results as index lines with leaf references, ordered by leaf, never
by "relevance score" shown to the reader.

## 8. Worked examples

### 8.1 The hero — a copy is numbered

The volume: *The Long Binding*, a binder's collected essays, edition
of 500. First visit, desktop.

- **t+0** — the leaf paints: spine rail in buckram at the left with
  its five bands, cream leaf, the title page complete in the DOM —
  author line, rule, title, ornament, imprint — and the bookplate
  reading "Copy No. 1" (the printed fallback). Nothing is invisible;
  a visitor on a dead connection has a title page.
- **t+120ms** — JS arms the assembly. The bookplate lifts to its
  stamp pre-state (scale 1.25, ink overlay 0.25); the title-page
  lines step back to their pre-states (opacity 0, +8px) — all within
  one frame, before first paint in practice, so the visitor sees the
  ceremony, not the arming.
- **t+120–320ms** — the stamp lands: `--ease-press`, the plate
  settles at its 1.2° with the ink-darkening thud. The number has
  already been drawn (say 212) and stored under `fe.copyNo` *before*
  the stamp lands — state first, ceremony second.
- **t+380ms → ~+545ms** — "212" types into the blank at 55ms per
  character. The blank's hairline pulses once at the first keystroke.
- **t+500ms onward** — the title page assembles in bibliographic
  order at 120ms staggers: the author line ("E. M. Hartley"), the
  gilt rule drawing to its 64px, then the title — and 150ms after
  the title lands, light crosses it once, left to right, 1200ms
  (§6.3). Subtitle, ornament, imprint. By ~t+1.9s the volume is open.
- **The reader scrolls.** The frontispiece (§6.12) faces them: at
  60% viewport its tissue guard lifts over 900ms, the binder's
  portrait settling into its gilt frame as the guard's italic title
  fades. Below, Chapter I's numeral and title assemble; its drop cap
  stands in ink, gilt at its foot — `p` has just begun.
- **Return visit, next week.** The stamp lands; "212" is already in
  the blank; beneath the plate, the greeting fades in: *"Copy No.
  212, again. The dog-ear is where you left it."* — and in Chapter
  III, the corner is folded, exactly where they left it.

### 8.2 Mid-page — the end of Chapter II, the beginning of Chapter III

The reader is deep in the volume; the shared loop is running at
`--lerp: 0.1`.

- **Chapter II's last paragraphs** cross the reading position. Its
  drop cap, chapters behind, sits fully gilt (`p = 1` by position).
  The gilt edge at the viewport's right (§6.6) stands at the fraction
  Chapter II's end represents; the folio in the fore-edge margin
  reads "Leaf 9 of 23 — Chapter II".
- **The ornament's centre crosses 62% vh.** Chapter II's fleuron
  draws: stem 0–300ms, scrolls joining at 200ms, leaves completing
  at 800ms, gilt-deep on cream. It is *not* followed by "Finis" —
  the volume is not over, and the absence is the discipline.
- **The endpaper divider arrives.** Marbled cream, buckram and gilt
  veins, drifting almost imperceptibly at its phase (this is divider
  2; its phase is 7.4s into the 20s cycle), parallaxing at 0.3×
  against the text. At its centre, "III" in buckram — the next
  chapter announced by the paper that precedes it. The reader's
  pause here is the design's pause: no button, no banner, just the
  endpaper and the numeral.
- **Chapter III's head crosses 78% vh.** The brief pin takes the
  numeral-and-title block for 30vh while, beneath it, the drop cap's
  first gilt appears at the letter's foot — illumination and
  furniture arriving together, sequenced by the same scroll. The
  running head crossfades to Chapter III's short title; the folio
  steps to "Leaf 10 of 23"; at the same beat, the gilt edge's bright
  tick pulses at the new gathering's boundary and relaxes over
  600ms. Three records, one fact, no disagreement.
- **The reader folds the corner.** Mid-chapter, they click the
  fore-edge corner: the dog-ear folds in 300ms, the contents leaf
  gains its mark (they will see it when they next open the contents),
  and the state is written. If they close the tab now, §8.1's
  greeting is already true.

### 8.3 Conversion — reserving this copy

The reader reaches the back of the volume: the order leaf (§6.14).

- **Arrival.** The running head reads "The Order Leaf"; the folio,
  "At the end of the volume". The leaf's buckram frame draws its
  rules over 400ms as it enters. Its terms stand beside the fields
  in the edition voice: "This edition is limited to five hundred
  copies. A reservation holds one copy, in the reserver's name, for
  fourteen days." — the publisher's real terms, or the leaf does not
  ship (§10).
- **Filling.** The reader tabs into "Name for the bookplate": the
  field's rule thickens, the gilt underline slides beneath it in
  200ms. They type the name — the plate will carry it verbatim; this
  is inscription, not data entry, and the label says so. Email next;
  an incomplete address draws the errata line beneath the field in
  italic: "Erratum — the address leaf is incomplete; the binder
  cannot write to it." Focus stays; nothing is cleared; the rule
  turns buckram until the address is whole.
- **The press.** "Reserve this copy" presses 1px. The foot line
  appears: "The binder is writing…" No spinner turns. The response
  returns: the form leaf fades 300ms and the reservation plate
  stamps in — scale 1.25 → 1, 200ms, the platen thud — reading
  "Reserved — Copy No. 212" with the entered name beneath, and under
  it, in the edition voice: "A confirmation has been sent to the
  address on this leaf." The live region speaks the same sentence.
- **The colophon agrees.** Below the leaf, the short-form colophon
  still reads "This copy: No. 212" — the reservation, the plate and
  the colophon are one number in three places. If the edition had
  been exhausted, the reader would have met the waiting-list leaf
  instead of the form (§6.14), and §6.8's "none remain" would have
  been printed in the colophon behind them. The book does not sell
  what it does not have.


## 9. Anti-slop — what makes THIS theme look cheap

Each failure below is specific to a book that is pretending. The cure
is stated with it; §10 turns the worst into gates.

1. **Theatrical scarcity.** A "copies remaining" figure generated in
   the browser, randomised, or different per visit. *Cure:* §6.8's
   law — server-supplied truth or the no-figure line. This is the
   theme's one unforgivable failure; everything else is taste, this
   is fraud.
2. **A copy number that changes.** New number per visit, per tab, or
   after clearing an unrelated key. *Cure:* §6.1 — drawn once,
   stored under its own key, written before it is displayed, never
   renumbered even when the edition statement changes.
3. **Gilt as a colour.** Flat `#C2A14D` fills on buttons, badges and
   headings; gilt text on cream (2.08:1 — illegible *and* cheap).
   *Cure:* gilt is a gradient with a light source (§6.3), rationed
   to ≤4% of pixels, and lettering only on buckram.
4. **The drop cap as an image.** A PNG initial, an SVG letter, a
   webfont swapped for a picture. *Cure:* §6.2 — real text, ink
   underlay, gilt overlay; it must survive copy-paste and a screen
   reader's indifference.
5. **"Finis" everywhere.** In footers, at every chapter end, on the
   empty state. *Cure:* once, in the final chapter, grepped (§10).
   A book that keeps ending has never started.
6. **The dog-ear as a bookmark icon.** A ribbon SVG, a "Saved!"
   toast, a count in a header. *Cure:* §6.4 — a fold on the chapter's
   own corner, a mark in the contents, a sentence in the greeting.
   The mark is physical or it is nothing.
7. **Marble as wallpaper.** The endpaper texture tiled behind
   everything, or a different marble per chapter. *Cure:* §6.7 —
   one stock, dividers and endpapers only; the reading leaves are
   plain cream, because text leaves in a marbled book would be
   unreadable and unbookish.
8. **The spine rail as a sidebar.** Logo, search, socials, a
   "newsletter" box stacked down the rail. *Cure:* §6.10 — bands,
   title, contents. The spine carries the book's structure and
   nothing else.
9. **A marketing strapline on the title page.** "The #1 solution
   for…" beneath the title. *Cure:* §6.11 — the title page carries
   bibliographic facts; persuasion lives in the chapters.
10. **Progress in percentages.** "73% read", a thin bar under a
    header. *Cure:* §6.6 + §6.17 — gilt edge and folio, agreeing.
    The grep for "%" in reading UI is a gate, not a preference.
11. **The colophon as a link farm.** Four columns of SEO links and a
    logo. *Cure:* §6.15 — an edition statement and a contents list.
    If a line could appear on any site's footer, it is not a
    colophon line.
12. **Ceremony without fallback.** Illumination that leaves caps
    invisible without JS, a guard that never lifts, a leaf-turn that
    traps. *Cure:* the standing law — every pre-state is JS-applied
    over a complete printed page, every animation owns a watchdog.
    A First Edition that needs JavaScript to be *readable* has
    confused a book with an app, and books are the older, hardier
    technology.

## 10. Quality gate

**Blocking** — the theme may not ship with any of these failing:

1. **Number persistence test.** Load, record the copy number, reload
   five times including one in a new tab: the number is identical,
   and the greeting appears from the second visit. Clear `fe.copyNo`:
   a new number is drawn and *no greeting appears*.
2. **Scarcity audit.** `data-remaining` traces to a publisher-supplied
   figure in the source data, or the no-figure line (§6.8) is
   rendered. Any client-side generation, decrement or randomisation
   of the figure fails the build on sight.
3. **"Finis" count.** The string appears in exactly one block in the
   entire build, inside the final chapter's ornament block (§6.5).
4. **JS-off read.** With JavaScript disabled, every page is complete:
   title page assembled, caps fully gilt, plates unguarded, contents
   present as a static section, colophon printed with its true
   figure. No content is missing, hidden or clipped.
5. **Gilt discipline.** No gilt text on cream anywhere (automated
   contrast pass over computed styles); gilt coverage ≤4% of pixels
   on a representative chapter page; every gilt gradient has its
   bright and deep stops (no flat gilt fills above 4px in any
   dimension).
6. **The three records agree.** On any chapter page, the contents
   leaf's current line, the folio's leaf number and the gilt edge's
   fraction describe the same position. Checked at three scroll
   depths on two page types.
7. **Dog-ear persistence.** Fold two chapters, reload: both folds
   stand, the contents shows both marks, the greeting names the
   later fold. Unfold one: the mark and the fold clear together.
8. **Leaf-turn never traps.** Throttled to a 3s destination: the
   turn holds with its fleuron, aborts at 6s, and native navigation
   completes. Middle-click and modified clicks bypass the turn
   entirely.
9. **Reduced-motion read.** With `prefers-reduced-motion`, the whole
   volume is the printed book: no stamp, no typing animation, caps
   gilt, guards absent, marble still, turns as crossfades — and the
   copy number, dog-ears and greeting all still work (state is not
   motion).
10. **The exhausted-edition agreement.** With remaining set to 0:
    the colophon prints "none remain", and the order leaf renders
    its waiting-list state. A live order form against a 0 figure
    fails.

**Standard** — expected, reviewed by eye:

11. The stamp's rotation is 1.2° and identical across loads (the
    binder's habit, not randomness); the type step is 55ms and the
    number is stored before the first character appears.
12. Illumination is reversible: scrolling back up a chapter lowers
    its gilt symmetrically; the ornament, by contrast, never undraws.
13. The marble is one stock across every divider, phases offset, and
    never appears behind text.
14. Chapter anatomy is identical across chapters: numeral, title,
    cap, text, plates, ornament — variety in content only.
15. The order leaf's terms are the publisher's real terms (edition
    size, hold period, lapse), and the confirmation sentence is
    printed only if the confirmation is actually sent.
16. Folio leaf counts derive from the build-time chapter map; no
    folio is a scroll percentage restated, and no "%" appears in any
    reading furniture.
17. Focus is visible everywhere it lands: gilt-bright ring on
    buckram (6.89:1), ink ring on cream, and the dog-ear is every
    chapter's last tab stop.
18. Print stylesheet: caps print gilt, ornaments drawn, dog-ears as
    their shadow marks, the spine rail and page edge absent, the
    colophon complete — the volume prints as a book.


## 11. Component inventory

Every component a real site in this theme needs, with its treatment.
Components the theme refuses are listed with their in-book
replacement — a refusal without a replacement is a gap, not a
position.

| Component | Treatment in this theme |
|---|---|
| Primary button | Buckram ground, cream small caps, 1px gilt rule beneath the label that draws on hover (§6.3 grammar). Press: 1px platen dip. "Reserve this copy", "Begin reading" — verbs of the book, never "Submit" or "Get started". |
| Secondary button | Cream ground, ink 1.5px rule, ink small caps; hover fills cream-deep. |
| Text link (in prose) | Ink, gilt underline drawing left→right on hover (200ms); visited links take buckram — a read leaf is a marked leaf. |
| Inputs | Ruled leaves (§6.14): transparent ground, 2px ink bottom rule, apparatus-voice label above, gilt underline on focus, buckram rule + errata line on error. No boxes, no fills, no floating labels. |
| Textarea | A ruled leaf with 4 ruled lines; the writing surface of the order leaf's "note for the binder" field. |
| Checkbox | A 20px gilt frame square; checked = a fleuron fills it (§6.14). The label is a sentence, not a fragment. |
| Radio group | "Impressions" — options set as a short contents list, the chosen one gilt-underlined. Used for edition/format choices only. |
| Select | **Refused.** A book has no dropdowns. Replacement: a contents-style list (§6.13) for ≤12 options, an index page (§7) beyond that. |
| Tables | Edition tables: contents-style rules (hairline row rules, no verticals, no zebra), small caps heads, old-style figures, a fleuron under the final row. Used for edition/impression records and shipping terms. |
| Badges | **Refused as chips.** Replacement: an **impression slip** — a small cream-deep slip (§6.16's furniture at badge scale) pasted beside the title: "Second impression", "With a new preface". States are bibliographic facts, set as slips. |
| Alerts | The errata slip (§6.16). No banners, no bars under the header. |
| Toasts | **Refused.** A toast vanishes; a book's notices stay until removed. Replacement: errata slip (§6.16); for pure confirmations, the stamped plate (§6.14) or a line in the colophon voice — confirmations in this theme are inscriptions, not notifications. |
| Modal | **Refused as an overlay pattern.** Replacement: the **plate leaf** — a full leaf that turns in (§6.9 grammar) carrying the modal's content as a plate with its caption, dismissed by turning back. Used for plate enlargements and the licence/terms leaf. Nothing floats above a book; leaves turn within it. |
| Tabs | **Refused.** Replacement: chapters and parts (§6.10's contents). Tabbed content in this theme is a volume trying to be a filing cabinet. |
| Accordion | Admitted, translated: **gatherings** — a part heading (small caps + ornament) whose chapters unfold beneath it on the contents page, 300ms `--ease-leaf`, one part open at a time, all parts printed open with JS off. |
| Pagination | Leaf furniture: "← The previous leaf" / "The next leaf →" as contents lines with folios (§6.17), plus the contents leaf for jumps. Numbered page buttons are refused — a reader does not press "4"; they turn to leaf 4 from the contents. |
| Search | The **Index**: an index page (§7) with entries and leaf references; the search field is a ruled line on that page, results are index entries. No search overlay, no ⌘K palette. |
| Breadcrumbs | **Refused.** Replacement: the running head (§6.17) — volume, chapter — which is what a breadcrumb wishes it were. |
| Progress | Gilt edge (§6.6) + folio (§6.17) only. Bars, rings and percentages are refused everywhere, including uploads (an upload reports in words: "The plate is being sent — leaf 2 of 3"). |
| Loading | The half-title skeleton (§6.18). Spinners are refused in all forms — nothing in a bindery spins except the sewing frame, and it is not a UI element. |
| Empty state | A blank leaf with its furniture: "This gathering is not yet bound." + the contents (§6.18's voice). Never an illustration of a mascot. |
| Tooltip | **Refused.** Marginal notes instead: the gloss sits in the fore-edge margin (§7, detail pages) at the line it glosses — print solved this in the margin centuries ago. On <768px the note becomes an errata-style slip beneath the paragraph. |
| Focus ring | 2px gilt-bright outline offset 2px on buckram; 2px ink outline with a gilt outer hairline on cream. Never `outline: none` without its replacement — the gate checks tab order through a full chapter. |
| Skip link | "To the text" — set as the volume's first line, appearing on focus at the leaf's head, jumping past the rail and furniture to the chapter's first paragraph. |

## 12. Content & copywriting voice

The voice is **bibliographic**: the site speaks as the book's own
apparatus — title page, contents, edition statement, errata — speaks.
It states facts about the volume and the copy; it never sells, urges
or exclaims. Two registers: the **statement** (edition statement,
terms, colophon — declarative, small caps for its fixed lines) and
the **aside** (greeting, captions, errata — italic, personal, the
binder leaning in). Headlines are titles; labels are apparatus;
errors are errata; confirmations are inscriptions.

**Headline style.** Titles, in title case, naming the thing as a
chapter would: ✓ "Chapter III — The Long Binding" · ✓ "The Order
Leaf" · ✗ "You Won't Believe What's Inside Chapter 3!" · ✗ "Our
Amazing Products". A headline that could run on a landing page fails;
a headline that could be set on a contents page passes.

**Label style.** Small caps, nouns of the book: ✓ "Contents",
"Errata", "Imprint", "Leaf 7 of 23", "Name for the bookplate" ·
✗ "Menu", "Notifications", "Page 7/23", "Your name". Buttons are
verbs of the book: ✓ "Reserve this copy", "Begin reading", "Turn to
the contents" · ✗ "Submit", "Click here", "Get started".

**The greeting** (verbatim pattern, §6.11): "Copy No. 212, again.
The dog-ear is where you left it." — the second sentence names the
folded chapter instead when one is folded ("You left a dog-ear on
Chapter III — The Long Binding."). First visits get no greeting;
the book does not pretend to know a new reader.

**Error voice — errata.** Every error is a correction the publisher
prints against itself: ✓ "Erratum — the address leaf is incomplete;
the binder cannot write to it." · ✓ "Erratum — this leaf could not
be sent. Your entries are kept above; try again." · ✗ "Oops!
Something went wrong." · ✗ "Invalid input". The pattern is fixed:
"Erratum —" + what is wrong, in the book's terms + what stands
instead or what to do. The visitor's text is never "invalid"; a leaf
is incomplete, a line is wanting.

**Empty-state voice.** ✓ "This gathering is not yet bound." (a
section with nothing yet) · ✓ "No leaves answer to that name in this
volume." (index search, no results) · ✗ "Nothing here yet 👀" ·
✗ "No results found". Emptiness is a binding state, stated plainly,
with the contents offered as the way onward.

**Confirmation voice — inscription.** ✓ "Reserved — Copy No. 212."
+ "A confirmation has been sent to the address on this leaf." ·
✗ "Success! 🎉 You're in!" Confirmations name the copy, the act and
the fact; they never celebrate, because a bookplate does not
celebrate — it records.

**Banned words** (greppable, §10-adjacent): *hurry, limited-time,
don't miss out, exclusive offer, unlock, free!!!*, any exclamation
mark in the statement register, any percentage in reading furniture,
the word "user" (the book has readers and owners of copies).

**Owned words**: *copy, leaf, gathering, bound, impression, plate,
folio, errata, colophon, finis* — used precisely, never decoratively.
"Impression" means a printing; "plate" means an image the volume
chose; a build that calls a blog post a "leaf" without the folio
system to back it is borrowing the costume (§9).

## 13. Full-page scroll choreography map

A chapter page (the volume's typical long page), top to bottom.
Every beat names what the visitor sees and what it is for.

| Beat | Scroll position | What happens | What it feels like |
|---|---|---|---|
| 0 | Load | Bookplate stamps; number types (§6.1); title page assembles (§6.11); light crosses the title once (§6.3) | A copy is numbered and opened |
| 1 | Title page → frontispiece | Tissue guard lifts 900ms; portrait settles into its gilt frame (§6.12) | The book's face is uncovered |
| 2 | Chapter I head | Numeral, title assemble; brief pin; cap's gilt begins at the letter's foot (§6.2) | A chapter begins the way chapters begin |
| 3 | Chapter I body | Cap illuminates with position; folio steps leaf by leaf (§6.17); gilt edge grows (§6.6) | Reading, measured in gold |
| 4 | A plate mid-chapter | Guard-less plate: frame catches light on hover, scale settles (§6.12 plain grammar) | An illustration, regarded |
| 5 | Chapter I end | Ornament draws stem→scrolls→leaves, 800ms (§6.5). No "Finis" | A full stop, set by hand |
| 6 | Endpaper divider | Marble drifts at its phase, parallax 0.3×; "II" in buckram (§6.7) | The pause between gatherings |
| 7 | Chapter II | Beats 2–5 repeat with Chapter II's own cap, plates, ornament — identical anatomy, different content | The book's rhythm, trusted |
| 8 | The reader folds a corner | Dog-ear folds 300ms; contents gains its mark (§6.4) | A place kept |
| 9 | Final chapter's end | Ornament draws; at +850ms "Finis" fades beneath it (§6.5) | The volume ends — once |
| 10 | Colophon | Gilt rule; statement lines stagger; copies count down to their figure (§6.8); "This copy: No. 212"; contents of the volume | The accounting, honestly printed |
| 11 | (Any page) Navigation | Leaf turns from the spine, gilt edge flashing (§6.9) | Another leaf of the same book |

Reverse pass: beats 2–7 are pure functions of position and run
symmetrically backward (illumination lowers, edge retreats, folios
step back) — except the ornaments, which stay drawn, and the
dog-ears, which stay folded. State earned is kept; position is
re-read. Jump-scroll ( scrollbar drag, End key): the loop settles
every scrubbed value to its true position within 300ms of scroll
rest; furniture fades are skipped for jumps over one chapter (the
correct furniture simply stands).

## 14. Whole-page performance budget

Budgets for a representative chapter page; exceeding any line starts
the cut order, in order, until the page fits.

| Budget | Limit |
|---|---|
| Total page weight (first load, compressed) | ≤ 820KB |
| Fonts | Playfair Display + Source Serif 4, subset to Latin + figures + the fleuron range, ≤ 120KB total, `font-display: swap` with the §6.1 stamp watchdog covering late arrival |
| Images | Frontispiece ≤ 180KB; chapter plates ≤ 140KB each, ≤ 3 per chapter page; responsive sizes mandatory |
| Inline SVG | Marble stock ≤ 12KB (one, reused via `<use>`); ornaments ≤ 2KB each |
| JavaScript | ≤ 45KB compressed for the entire theme runtime (loop, storage, observers, turn) — the book's machinery is small because the book is old |
| Shared loop cost | ≤ 1.5ms per frame total; scrubbed writes only for elements within ±1 viewport |
| Long tasks | None over 50ms during scroll; the stamp and typing run on load, never during a scroll |
| Layout shift | 0 by construction — skeleton anatomy (§6.18) reserves every block's geometry; plates carry their aspect in markup |

**Cut order** (first → last): 1. Marble drift (keep the static
marble and its parallax). 2. The sheen layer on the gilt edge (keep
the fill). 3. Hover light-catch trailing transition (catch becomes
instant). 4. Title-page stagger (lines appear together; stamp and
typing stay). 5. The brief chapter-head pin (heads simply assemble).
6. Frontispiece scale settle (guard lift alone remains).

**Never cut:** the copy-number state and its persistence; the
illumination's fully-gilt default and watchdog; the folio; the
leaf-turn's abort path; any fallback that keeps the page readable
without JS. A build that cuts a never-cut item to meet a budget has
misread the budget's purpose.

## 15. Build-order checklist

In sequence; each step leaves a readable page.

1. **The printed book first.** Static HTML/CSS: palette, type scale,
   layout geometry (rail, measure, margins, edge strip as un-gilt
   leaf edge), all pages complete and readable with no JS. This is
   the deliverable every later step enhances.
2. **Chapter anatomy.** Numeral/title/cap/ornament/colophon blocks as
   reusable components; verify anatomy identical across three test
   chapters (§10.14).
3. **Copy-number state.** Draw, store (`fe.copyNo`), print fallback;
   run gate 1 (persistence) before any animation is added.
4. **Contents & folio records.** Chapter map (ids, short titles, leaf
   spans) generated at build; contents leaf (§6.10) and per-chapter
   running heads/folios (§6.17) reading from the one map.
5. **The shared loop.** rAF lerp 0.1, cached measurements, resize
   refresh; drive nothing yet — prove ≤1.5ms/frame idle cost.
6. **Illumination + edge.** Caps (§6.2) and gilt edge (§6.6) onto the
   loop, fully-gilt defaults and 900ms watchdogs in place; verify
   the three-records agreement (gate 6).
7. **Ornaments + Finis.** Draw on trigger (§6.5); grep "Finis"
   (gate 3) wired into the build.
8. **Dog-ears.** Fold UI, `fe.dogears`, contents marks, greeting
   logic (§6.4); gate 7.
9. **Entrance ceremony.** Stamp, typing, title-page stagger,
   light-catch (§§6.1, 6.11, 6.3) — in that order, each with its
   watchdog; JS-off read (gate 4) re-run after this step, because
   this is the step that breaks it when it breaks.
10. **Plates.** Frontispiece guard (§6.12), plain-plate grammar,
    chapter cards (§6.13).
11. **Endpapers.** Marble stock (one SVG), drift + parallax (§6.7).
12. **Order leaf.** Form, errata-voice errors, reservation plate
    (§6.14); exhausted-edition state wired to the same figure as the
    colophon (gate 10); scarcity audit (gate 2).
13. **Colophon.** Statement, count (§6.8), short form for interior
    pages (§6.15).
14. **Leaf-turn + errata slips + skeletons.** (§§6.9, 6.16, 6.18);
    turn-abort test (gate 8).
15. **The passes.** Reduced-motion pass (gate 9), lamplight
    (dark-scheme) pass, print stylesheet, focus-order walk, and the
    full §10 gate, blocking items first.

