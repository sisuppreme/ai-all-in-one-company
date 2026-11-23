# 38. Paper Mulberry — Expanded (v1 + v2)

> Expansion of theme #38 from `themes-026-050.md`, written directly to
> the full standard: the v1 10-part structure plus the v2 deepening
> layers (per-element choreography timelines, state matrices, breakpoint
> behaviour, edge cases, accessibility specs and token lists; per-theme
> component inventory, copywriting voice, three worked examples, scroll
> choreography map, performance budget, build-order checklist).
> Identity preserved exactly: the same concept, the same five palette
> anchors, the same two typefaces, the same nine signature elements —
> deepened, never redesigned — plus nine page-family elements.

## 1. Concept & world

Most websites pretend to be screens. This theme admits it is a sheet.
The site feels like **a sheet of handmade kozo paper being turned by
hand on a mill table** — deckled edges that were torn, not cut;
visible fibres suspended in the sheet; content printed slightly
imperfectly, the way letterpress prints, with one deliberate misprint
in the hero that registers itself into alignment while the visitor
watches. Every section is a sheet. Turning to the next section is
turning the sheet. The fibres in the background are not a texture
applied to the page; they are the page's substance, and one of them —
noticeably longer than the rest, crossing three whole sections — is
a maker's flaw the mill left in on purpose and confesses in the
colophon (§6.16).

The world is the paper mill, treated as a complete interface
vocabulary rather than a rustic skin. The page has **sheets** (every
section, each with its deckled top edge), **fibres** (the long kozo
strands suspended in the sheet, one of them famous), **the deckle**
(the torn edge itself, and the side strip it forms), **ink** (sumi,
absorbed unevenly, wicking along fibres — never a flat fill), **the
press** (the letterpress that prints every headline with a visible
impression), and **the branch** (the mulberry itself, drawn in the
colophon, the plant every sheet on the page was made from). Nothing
on the page is decoration that happens to look papery; the paper is
the page's structure, and every animated thing on it is either the
sheet settling, the press printing, a sheet turning, or a fibre
moving in the sheet it belongs to.

**The theme's one law: every figure is a sheet property, and every
flaw is declared.** A grammage printed on the page (128 g/m²) is the
real grammage of the paper the content describes, or of the sheet
the section is named for. A fibre length, a sheet count, an edition
number — each traces to the mill's records or the publisher's stated
data, and §6.18's counters only ever count those. The long fibre
(§6.5) is the law's emblem: a flaw that is *more* visible than the
perfections around it, named in the colophon with its measured
length. A Paper Mulberry build that invents a grammage because a
spec table "needed one more row", or that airbrushes its misprint
(§6.3) into a generic fade-in, has not bent the theme; it has lied
about a sheet of paper, and the quality gate (§10) fails it on
sight. Everything else in this theme is craft. That one is the
mill's honesty.

**Paper is the interaction model.** Because the visitor is handling
sheets, their acts are a handler's acts: they settle a sheet flat
(§6.1), they watch the press print on it (§6.2, §6.3), they turn it
(§6.4), they lift a card's corner to see whether it wants turning
(§6.8), they press it and feel the impression (§6.9). The site does
not have users; it has readers handling paper. That is why the theme
fits makers of physical things — paper, print, cloth, food, craft —
whose material can be stated in numbers and whose process is the
story, and why it curdles around anything weightless: a SaaS
dashboard has no grammage, and pretending it does is costume.

**Best-fit sites and audiences.**

- Paper and print makers: washi and handmade-paper mills, letterpress
  studios, bookbinders, print shops — anywhere grammage, fibre and
  edition size are facts the maker will state in writing.
- Craft and material brands with a stated substance: natural-fibre
  textiles, woodwork, ceramics, small-batch food — one material,
  honestly measured, as the site's spine.
- Publishers and editions: small-press books, art prints, journals —
  content issued in numbered sheets and editions (§6.18).
- Process storytelling: a maker's method told sheet by sheet, from
  bark to finished paper, where each stage is a real stage with real
  figures.
- Portfolios of physical work: each project a sheet, its materials
  and dimensions in the figure line, its photograph a plate printed
  on the sheet (§6.12).

**When NOT to use it.**

- For content with no material. If nothing on the page has a weight,
  a fibre or a dimension, the deckle is a costume on a database.
- For anything urgent or transactional at speed. The theme's pace is
  a handler's pace — sheets settle over 900ms, sections turn at
  their boundaries, the press prints line by line. A visitor trying
  to check out in ninety seconds will feel they are handling wet
  paper, because they are.
- Where figures would be theatre. If the publisher will not commit
  real grammages, sheet sizes and edition counts to the page, the
  counters (§6.18) become fiction with good typography; use another
  theme.
- For dense data products. A sheet carries a reading measure and a
  handful of figures (§4); tables of forty rows belong in §6.13's
  ledger grammar at most, and usually in another theme entirely.
- For audiences who must never see an imperfection. The misprint
  (§6.3) and the long fibre (§6.5) are the theme's thesis, not its
  accidents; a brand that cannot show a flaw correcting itself
  should not borrow a theme built on exactly that.

## 2. Palette

Five anchors, inherited unchanged. The palette is a sheet of kozo on
a mill table: two colours of the paper itself, one ink, one bark,
one leaf. Nothing else is admitted; every other colour on the page
is one of these five, tinted, shaded or set at an opacity over kozo
white.

| Token | Hex | Role | Usage ratio | Pairing & contrast notes |
|---|---|---|---|---|
| `--kozo` | `#F6F1E6` | The sheet: every page background, every section surface | ~76% of pixels | Warm handmade white, never swapped for `#FFFFFF` anywhere, including form fields and the offcut page (§6.17). Sumi ink on it: 12.4:1. |
| `--fibre-shadow` | `#E4DCC8` | The sheet's depth: deckle shadow, sheet separation, card grounds, the unprinted skeleton | ~13% of pixels | On kozo only **1.24:1** — a shadow and a ground, never text, never a line that carries meaning alone. Sumi ink on it: 10.6:1, so ink may letter a card ground. |
| `--sumi` | `#33302A` | The ink: body text, headlines, the ink strip (§6.6), printed figures | ~6% of pixels | On kozo 12.4:1 (AAA); on fibre shadow 10.6:1 (AAA). The only colour body text may be set in on a sheet. |
| `--bark` | `#9C6644` | The bark: deckle edges, rules, hover warmth, the branch's stem (§6.7) | ~3% of pixels | On kozo **3.63:1** — graphical and large-display use only (≥24px or non-text line-work). Its darkened derivative `--bark-deep` (5.1:1) is the only form in which this hue may set text on kozo. |
| `--leaf` | `#5B7553` | The mulberry leaf: the branch's leaves (§6.7), the seal of freshness, success states, one accent per sheet at most | ~2% of pixels | On kozo **4.94:1** — AA at all sizes, so leaf may letter small text where bark may not; rationed anyway (§9) because a sheet is mostly paper and ink. |

**Derived tokens** (computed from the anchors; never new hues):

| Token | Derivation | Use |
|---|---|---|
| `--kozo-deep` | `#EFE7D3` (kozo darkened ~4%) | The sheet's underside: the turning sheet's back (§6.4), the card curl's underside (§6.8). Sumi on it 11.3:1. |
| `--bark-deep` | `#7E4F30` (bark darkened ~22%) | The text-grade form of the bark hue: captions, form labels, figure-line words on kozo. On kozo 5.1:1 — AA at all sizes. |
| `--leaf-deep` | `#47603F` (leaf darkened ~18%) | Leaf at small sizes and in the dark scheme; on kozo 6.8:1. |
| `--sumi-soft` | `--sumi` at 62% over `--kozo` | The misprint's ghost copy (§6.3) at rest before registration, secondary apparatus. Never body text — a ghost is a printing state, not a reading colour. |
| `--fibre-line` | `--bark` at 34% over `--kozo` | Background fibre strokes at rest (§4 density law). Raised to 55% for the one long fibre (§6.5) — the flaw is darker than the field, by law. |
| `--wick` | `--sumi` at 88% with a 1px fibre-shadow fringe | The ink strip's fill edge (§6.6): ink wicking into fibres is never a straight line. |
| `--hairline` | `--sumi` at 16% over `--kozo` | Ruled lines on the order sheet (§6.14), ledger rules (§6.13). Decorative only. |

**Dark-mode behaviour.** The sheet does not invert; **the mill works
by lamplight.** Under `prefers-color-scheme: dark` (or the lamp
toggle, §11) the page moves to the night-mill scheme: ground
`#2B2620` (dark table), sheets `#3A332A` (kozo under lamplight,
modelled as a warm dark, never a grey), text `#EDE4CF` (11.9:1 on the
night sheet), fibre lines bark at 40%, leaf lightened to `#8FAE86`
(6.2:1). The ink strip (§6.6) fills with the night text colour —
lamp-lit ink is pale because the strip is read by its edge, and the
spec says so. The transition between schemes is a 600ms
`--ease-press` crossfade of background and line colours, fired once,
never animated per scroll.

## 3. Typography

Two typefaces, inherited unchanged. **Shippori Mincho** (500 / 700)
is the voice of the printed word: display, headlines, the letterpress
lines — a Mincho's fine horizontals and strong verticals are the
closest screen relative of a letterpress impression in Japanese
type. **Zen Kaku Gothic New** (400 / 500 / 700) is the voice of the
mill's record: body text, figures, labels, the apparatus — the hand
that writes the grammage in the ledger. Shippori Mincho is never
used for a paragraph; Zen Kaku is never used for a headline. The
casting is the theme's first quality check (§10).

| Role | Face & setting | Size / line-height / tracking | Rules |
|---|---|---|---|
| Display (hero headline) | Shippori Mincho 700 | 56px / 1.18 / +0.01em, max 3 lines | Prints line by line (§6.2); one word carries the misprint (§6.3). Never centred — a sheet's headline sits at its head, left, where the press put it. |
| Section headline | Shippori Mincho 700 | 34px / 1.25 / +0.01em | One per sheet. Arrives with its sheet's turn (§6.4), printed, never faded. |
| Sheet title (apparatus) | Zen Kaku Gothic New 700, small caps effect via tracking | 13px / 1.5 / +0.12em | The sheet's furniture: "SHEET 3 OF 7 · KOZO, LONG FIBRE". Set in `--bark-deep` on kozo (5.1:1). |
| Body | Zen Kaku Gothic New 400 | 17px / 1.75 / 0 | Measure 56–64ch, resting on the sheet (§4). Line-height is generous because fibres pass beneath (§4 clearance law). |
| Figure line (data) | Zen Kaku Gothic New 500, tabular figures | 15px / 1.55 / +0.01em | Grammages, dimensions, counts: "128 G/M² · 640 × 970 MM · EDITION OF 300". Tabular lining figures always — a counting figure (§6.18) must never change width. |
| Caption / colophon | Zen Kaku Gothic New 400 | 13.5px / 1.6 / +0.01em | The maker's notes, incl. the confession of the long fibre (§6.16). Set in sumi at 88% — a note, not a shout. |
| Form label | Zen Kaku Gothic New 700 | 13px / 1.45 / +0.09em, uppercase | Set in `--bark-deep` on kozo (5.1:1) — the one place the bark hue letters text, in its darkened form only. |

**Type laws.**

1. **Mincho prints; Gothic records.** A paragraph in Shippori Mincho
   or a headline in Zen Kaku Gothic New is a casting error the gate
   checks by class, not by eye (§10).
2. **Figures are always tabular and always carry their unit.** "128"
   alone is unfinished typesetting; the sheet prints "128 G/M²". A
   dimension without "MM", a count without its noun ("300 SHEETS"),
   is a broken figure under the one law (§1).
3. **Headlines are printed, never displayed.** No headline in this
   theme fades, slides or scales in as screen type; it prints
   (§6.2) — opacity plus impression offset, or it is simply there.
   A fade-in headline is a screen habit wearing paper's clothes.
4. **Titles are short enough to print in one pull.** Display ≤ 8
   words, section headlines ≤ 6. A headline that needs a fourth
   line is two sheets wearing one deckle.
5. **The misprint word is chosen, never random.** Exactly one word
   in the hero headline carries §6.3 — the word the maker most
   wants read twice (the material, the place, the name). The build
   names it in the data (`data-misprint`), and the gate counts
   exactly one per page (§10).

## 4. Layout language

**The sheet.** The page is a stack of sheets, max width 1180px, on a
`--kozo` ground that extends to the viewport edges — the table is
the same paper, further away. There is no card floating on a
different-coloured desk; there are sheets, and sheets beneath them.
Sheet furniture (sheet number, paper name, grammage) sits in the top
margin of each sheet in the apparatus setting, like a mill's pencil
note on a finished sheet.

**The deckle.** Every sheet's top edge is deckled: an SVG mask path
with 14–22 irregular teeth over the sheet's width, amplitude 6–11px,
generated per sheet from a seeded variation so no two sheets share
an edge — torn paper never repeats. The deckle is geometry, not an
image: the same path drives the sheet's mask, its turn (§6.4) and
its shadow. A sheet's bottom edge is straight (the sheet was laid
down, not torn twice) except the last sheet on the page, whose
bottom edge is deckled too — the stack ends the way it began.

**Fibre field.** Each sheet carries a background fibre layer: 26–40
long, slightly curved strokes (quadratic SVG paths, 180–420px long,
1–1.5px, `--fibre-line`), laid at shallow angles (mostly within ±9°
of horizontal, the direction kozo fibres settle in the mould),
distributed by a seeded field so density is even and no fibre
crosses the reading measure at full strength. **Fibre clearance:**
where a fibre would pass behind a text block it drops to 16%
opacity for that span — decided at build time in the generated
paths, never left to overlap and hope. One fibre (§6.5) breaks
every one of these rules on purpose, and is the only one allowed to.

**Spacing rhythm.** A 4px base unit; sheet padding 88px top / 80px
bottom on desktop (handling paper is unhurried); blocks within a
sheet separated by 36px; figure lines sit 10px under the text they
measure. Sheets overlap by exactly the deckle amplitude: the next
sheet's deckled top slides *beneath* the previous sheet's bottom
edge by 8px, so the stack reads as a stack at every scroll position.

**Density rules.** At most one pinned moment per page (the hero
settle is timed, not pinned; §6.4's boundary pins are brief and
counted — at most 4 per page, §6.4); at most one leaf-green element
per sheet; at most 5 cards in any sheet (§6.12); at most one long
fibre per page (§6.5). A page that needs more sheets is more sheets
— the furniture says so ("SHEET 3 OF 7" is content, §6.10).

**Whitespace is the unprinted sheet.** The calm inside a sheet is
not empty space to be filled; it is paper that was made and not
printed on, which is most of any good sheet. Sections end with at
least 56px of unprinted sheet before the next deckle rises.

## 5. Full motion system

The theme's motion is papermaking and printing: things settle, are
pressed, turn, wick, or sway in the sheet. Nothing bounces for joy,
nothing spins, and the fastest event on the page (an impression
click, §6.9) is over in 300ms while the slowest (the long fibre's
sway, §6.5) takes 14s to cross 4px. Five named easings carry the
whole system:

| Token | Curve | Used by |
|---|---|---|
| `--ease-settle` | `cubic-bezier(0.22, 1, 0.36, 1)` | The sheet landing: settle (§6.1), card arrivals (§6.12), skeleton resolve (§6.15) |
| `--ease-press` | `cubic-bezier(0.55, 0, 0.35, 1)` | The press acting: headline printing (§6.2), impression click (§6.9), scheme crossfade |
| `--ease-turn` | `cubic-bezier(0.65, 0, 0.35, 1)` | Sheet turning (§6.4) and the next-sheet transition (§6.15) |
| `--ease-wick` | `cubic-bezier(0.45, 0, 0.2, 1)` | Ink moving into fibre: the ink strip (§6.6), branch draw (§6.7) |
| `--ease-sway` | `cubic-bezier(0.45, 0, 0.55, 1)` | The long fibre's sway (§6.5), corner curl growth (§6.8) |

**Every motion term, translated into this theme's language:**

- **Scroll-triggered reveals** → sheets turning (§6.4) and the
  branch drawing (§6.7): content arrives the way paper behaves —
  the next sheet comes from beneath the last, or the plant grows
  in the colophon when the reader reaches the confession.
- **Scroll-driven / scrubbed animation** → the page-turn curl
  (§6.4), the ink strip's fill (§6.6), fibre parallax (§6.5's
  field). All scrubbed values run through the one shared rAF loop
  at lerp **0.12** (§14); there is no second loop.
- **Parallax** → fibre layers only: background fibres drift at
  sheet speed minus a hair (0.96×) beneath the printed layer, so
  the sheet's substance lags its print by the thickness of the
  paper. Text never parallaxes against its own sheet — print is
  *in* the paper.
- **Pinned sections** → brief boundary pins only (§6.4): a sheet
  pins for the 30vh in which its successor slides beneath it. No
  long pinned scenes; paper is turned, not staged.
- **Smooth scrolling** → *paper-drag*: native scroll, with every
  scrubbed value lerped by the shared loop so sheets glide rather
  than step. Scroll position itself is never hijacked or re-mapped.
- **Progress indicator** → the ink strip (§6.6): sumi wicking down
  the deckled side strip. Percentages are forbidden anywhere on
  the sheet (§9); progress is ink absorbed, or a sheet count.
- **Staggered reveals** → headline lines printing at 140ms (§6.2),
  branch leaves at 120ms (§6.7), cards in reading order (§6.12).
  Stagger always follows a real order — press order, growth order,
  reading order — never decoration order.
- **Masked reveals** → the deckle mask (§4): a sheet's own torn
  edge is the mask its turn (§6.4) is clipped by, so the mask is
  the paper.
- **Blur-to-sharp** → refused. Print is either impressed or not yet
  impressed; blur is a screen effect, and this theme's substitute
  is the impression offset (§6.2): the line arrives 2px deep and
  settles to the surface — sharp throughout.
- **Animated counters** → ink numerals (§6.18): sheet counts,
  grammages and edition numbers count in tabular figures as their
  sheets arrive — replays between two true values, never invented
  motion between fake ones.
- **Marquee** → refused. A sheet does not slide sideways. The
  mill's notices are a static apparatus line in the sheet margin,
  set at build time; they change between sheets, never during
  reading.
- **Ambient loops** → exactly two: the long fibre's sway (§6.5)
  and the fibre-grain shadow play (§6.5's field note) — a slow
  light shift across the sheet's grain over 26s. A third ambient
  loop is a gate failure — a mill room is quiet.
- **Kinetic typography** → refused, except the two licensed acts:
  the headline printing (§6.2) and the misprint registering
  (§6.3). Type on a sheet is printed once and stays printed.
- **Micro-interactions** → the corner curl (§6.8) and the
  impression (§6.9): touching the page touches paper — a corner
  lifts, or the press comes down where the finger did.
- **Hover physics** → no magnetic pull, no tilt. A sheet lies flat
  on the table; the pointer's approach is answered by the corner
  curl (§6.8) and a 1px deepening of the sheet's edge shadow —
  the paper's edge, not the sheet leaning.
- **Image treatments** → plates (photographs of paper, process,
  product) scale 1.05 → 1 inside their printed frames as they
  cross the viewport centre (§6.12). The frame never moves; the
  plate settles into it like a print laid on the sheet.
- **Page transitions** → the next-sheet transition (§6.15): the
  current sheet lifts at its deckle and the new sheet slides
  beneath, 520ms, once per navigation, never on back/forward.
- **Skeleton loading** → the unprinted sheet (§6.15): deckle and
  fibre field at rest with blank measures — a sheet before the
  press reaches it, resolving as content lands, with a hard
  1200ms law.
- **Custom cursor** → refused (standing rule). The system cursor
  is the reader's fingertip; it is not themed.

## 6. Signature elements

### 6.1 Sheet settle — the page lands on the table

- **What & why.** The theme's opening act. On load, the hero sheet
  settles: it scales 1.02 → 1 over 900ms while a soft shadow sweep
  passes across it, like a sheet of handmade paper flexing flat onto
  the table under its own weight. It belongs because the whole page
  is one sheet landing — every later element prints onto a sheet
  that has already arrived, and the visitor should feel the paper
  land before they are asked to read it. A sheet that simply appears
  was never handled; this one was laid down.
- **Structure.** The hero `<section class="sheet sheet--hero">`
  carries its deckle mask (§4) and fibre field (§4) as background
  layers; the settle is a single transform on the sheet plus one
  shadow layer (a `--fibre-shadow` gradient band, 34% of sheet
  height, `pointer-events: none`, `aria-hidden`) whose translateX
  sweep is the flex. The pre-settle state exists only under a
  JS-armed class on the root; the server-rendered sheet is settled,
  full-size, fully readable.
- **Motion spec.** Trigger: page load, gated on `fonts.ready` (a
  sheet must not flex before its print is set, or the headline
  reflows mid-flex). Scale 1.02 → 1, 900ms `--ease-settle`. Shadow
  sweep: band travels −40% → 110% of sheet width across the same
  900ms, opacity peaking 0.5 at mid-travel. The sweep is the shadow
  of the sheet's own flexing edge — it darkens nothing but the sheet
  itself, and text contrast never drops below 10:1 at any frame
  (the band passes *behind* the printed layer).
- **Choreography timeline (v2).** t+0: hero paints settled (no-JS
  state) → fonts ready → t+60ms: JS arms the unset state (scale
  1.02, band parked left) → t+60–960ms: scale settles, band sweeps →
  t+500ms: the headline's first line begins printing (§6.2) while
  the sheet is still flexing — print lands on moving paper, as it
  does on a real press bed → t+960ms: sheet at rest, band removed
  from the DOM → t+1400ms watchdog: any unsettled transform is
  snapped to rest instantly.
- **State matrix (v2).** *Rest:* settled sheet — the permanent
  state, and the no-JS state. *Settling:* 900ms, non-interactive,
  identical on desktop and touch. *Hover / focus:* no effect — the
  sheet is furniture, not a control. *Scrolled-past:* settled; the
  settle never replays on scroll-back (a laid sheet is not re-laid).
  *Disabled:* reduced-motion and no-JS both rest (below).
- **Content merge.** The settling object is the hero sheet itself —
  its headline, standfirst and figure line all ride the same
  transform. Remove the content and there is no sheet to settle;
  remove the settle and the hero is complete, merely unannounced.
- **Failure fallback.** If `fonts.ready` has not resolved by 900ms,
  the settle fires anyway on the laid-out sheet. If the transform
  layer fails to build, the hero stands as the static sheet — the
  watchdog is structural: the settle is an armed state on a complete
  sheet, and its absence is the fallback.
- **Reduced-motion variant.** No settle, no sweep. The hero is the
  printed sheet from first paint — the sheet as it would lie in the
  mill's sample book.
- **Breakpoints (v2).** ≥1200px: full spec, scale from 1.02.
  768–1199px: scale from 1.015, sweep band 28% of width. <768px:
  scale from 1.01, duration 700ms, no shadow band — a phone's sheet
  is small and a long landing delays reading.
- **Edge cases & failure modes (v2).** *Return visit in the same
  session:* the settle fires again — it is load behaviour, not a
  ceremony; but on bfcache restore it does not (the sheet was never
  lifted). *Hero taller than the viewport:* the sweep still crosses
  the sheet's width, not the viewport's. *Slow device:* if the first
  frame measures >32ms, the band is dropped and the scale completes
  alone at 600ms.
- **Accessibility spec (v2).** Purely presentational; nothing is
  announced, nothing is focusable, and the headline is ordinary DOM
  text readable from first paint — the settle never masks it (the
  band passes behind the printed layer by construction). The 2%
  scale travel is far below any vestibular concern threshold.
- **Performance budget & mobile variant.** One transform + one
  gradient band, compositor-only; ≤0.3ms script per frame. Mobile:
  the bandless 700ms variant above; the band layer is built lazily
  after first paint so it never competes with the hero's text.
- **Tokens consumed (v2).** `--kozo`, `--fibre-shadow`, `--sumi`,
  `--ease-settle`, `--settle-dur` (900ms), `--settle-scale` (1.02).

### 6.2 Letterpress headline — the press prints the title

- **What & why.** The hero headline does not fade in. It *prints*:
  each line arrives with full opacity and a 2px impression offset —
  as if the type had been pressed into the sheet and the line sits
  a hair deep — then the offset settles to 0 as the impression
  relaxes. It belongs because the title's arrival should mimic the
  press the paper was made to meet: ink, pressure, release. A faded
  headline is a screen showing a picture of print; an impressed
  headline is print.
- **Structure.** Each headline line is a `<span class="press-line">`
  (lines are real line breaks in the markup, set by the copy, not
  split by JS at runtime — the press prints the lines the
  compositor set). Each line carries a duplicate impression layer:
  the same text in `--sumi-soft` at translateY +2px behind the true
  line, removed when the line settles. The pre-print state exists
  only under a JS-armed class; server-rendered lines are printed,
  offset 0, impression layer absent.
- **Motion spec.** Trigger: load, first line at the settle's t+500ms
  (§6.1), or at t+120ms if the settle was skipped. Per line: the
  impression layer and true line appear together at offset 2px,
  then offset relaxes 2px → 0 over 420ms `--ease-press`, stagger
  140ms per line in reading order. A 3-line headline completes at
  ~500 + 2×140 + 420 = 1200ms from load. Lines never move again:
  no hover state, no replay.
- **Choreography timeline (v2).** t+0: headline painted printed
  (no-JS state) → t+120ms: JS arms line 1's impression (offset 2px)
  → t+120–540ms: line 1 settles → t+260ms: line 2 arms → t+400ms:
  line 3 arms → t+820ms: last line settled, all impression layers
  removed → t+1200ms watchdog: any line still offset is snapped to
  0 and its impression layer deleted.
- **State matrix (v2).** *Rest:* printed headline — the permanent
  and no-JS state. *Printing:* 420ms per line, staggered; touch
  identical. *Hover:* none — headlines do not perform for pointers.
  *Focus:* the h1 is not focusable; heading navigation lands on
  printed text at any moment (a mid-print line is at offset ≤2px
  and fully legible throughout). *Scrolled-past / back:* printed,
  always. *Disabled:* JS off = printed; the impression never arms.
- **Content merge.** The impression is the headline's own depth in
  its own sheet — the offset is measured in the paper's thickness,
  not in screen space. Remove the headline and there is nothing to
  print; the animation is inseparable from the words it delivers.
- **Failure fallback.** The printed headline is the DOM default; JS
  adds the impression only when it can animate it, and the 1200ms
  watchdog guarantees rest. If arming fails partway, armed lines
  are disarmed (offset 0, layers removed) — the code path is
  delete-and-show, never repair-and-hope.
- **Reduced-motion variant.** No impression, no stagger. The
  headline is simply printed — which is what reduced motion asks
  every element in this theme to become.
- **Breakpoints (v2).** ≥1200px: as specced, offset 2px.
  768–1199px: offset 2px, stagger 120ms. <768px: offset 1.5px,
  stagger 100ms, and headlines over 3 lines print in two pulls
  (lines 1–2, then 3+) 160ms apart so the ceremony stays under
  ~1s.
- **Edge cases & failure modes (v2).** *Very long headline:* §3
  law 4 caps display at 8 words / 3 lines; a set headline beyond
  that cancels the print for that build — a minute of printing is
  a press jam, and the gate (§10) treats the over-long headline
  as a copy error. *Fonts late:* printing waits for the §6.1 fonts
  gate (900ms cap), because Mincho and its fallback have different
  line breaks and the press prints final lines only. *The misprint
  word (§6.3) sits in a printing line:* its line prints normally;
  the misprint's own timeline starts when its line settles (§6.3).
- **Accessibility spec (v2).** The headline is one `<h1>` with its
  full text in the accessibility tree once, from first paint; line
  spans are presentational wrappers (`aria-hidden` duplicates are
  never used — the impression layer is a shadow element with empty
  text, drawn via CSS, so nothing is announced twice). Contrast:
  sumi on kozo, 12.4:1, at every point of the settle; the
  impression layer at `--sumi-soft` is decoration behind opaque
  text, never the text itself.
- **Performance budget & mobile variant.** ≤3 transformed spans +
  ≤3 shadow layers, compositor-only, no layout after arming.
  Mobile: the two-pull variant above; arming is skipped on devices
  reporting ≤2GB RAM via `deviceMemory` where available — the
  headline simply stands printed.
- **Tokens consumed (v2).** `--sumi`, `--sumi-soft`, `--ease-press`,
  `--print-dur` (420ms), `--print-stagger` (140ms),
  `--impression` (2px).

### 6.3 Misprint registration — the flaw corrects itself

- **What & why.** One word in the hero headline prints wrong, on
  purpose: a ghost copy of the word sits at +3px, 40% opacity —
  the press struck twice and the second strike missed. Then, over
  700ms, the ghost registers: it slides into alignment with the
  true word and dissolves into it, leaving one clean impression.
  It belongs because it is the theme's thesis performed on its
  most-read word (§3 law 5): handmade work contains flaws, shows
  them, and corrects them in the open. A theme about honest paper
  that hid its only flaw would be lying in its headline.
- **Structure.** The chosen word is a `<span class="misprint"
  data-misprint>` in the headline markup. Inside it: the true word
  (real text) and a ghost layer — an `aria-hidden` duplicate of the
  word, absolutely positioned, in `--sumi-soft`. At rest (and in
  the no-JS DOM) the ghost sits at opacity 0, offset 0: the printed
  word, clean. JS arms the misprint state (ghost at +3px / 40%)
  only after the word's line has printed (§6.2).
- **Motion spec.** Trigger: the host line's print settle (§6.2)
  completing, +80ms. The ghost holds misregistered for a 260ms
  beat — long enough to be *seen* as wrong, the honesty beat —
  then registers: translateX 3px → 0 and opacity 0.40 → 0 over
  700ms `--ease-press`, the true word's own impression deepening
  by 0.5px at the ghost's arrival, as if the second strike finally
  landed true. Total ceremony ≈ 80 + 260 + 700 = 1040ms after its
  line prints. It happens exactly once per page load; never on
  scroll, never on hover, never again.
- **Choreography timeline (v2).** t+0: host line settled (§6.2) →
  t+80ms: ghost arms at +3px / 40% → t+80–340ms: the honesty beat,
  ghost held, fully visible → t+340ms: registration begins →
  t+690ms: ghost at +1px / 18%, true word's impression at its
  deepest → t+1040ms: ghost at 0 / 0%, removed from the DOM →
  t+1500ms watchdog: any surviving ghost is deleted instantly.
- **State matrix (v2).** *Rest:* one clean word — the permanent,
  no-JS and post-ceremony state. *Misregistered:* 260ms, the ghost
  visibly doubled. *Registering:* 700ms slide-and-dissolve; touch
  identical. *Hover:* none — the flaw does not perform on request.
  *Focus:* the word is inside the h1; not separately focusable.
  *Scrolled-past:* if the visitor scrolls away mid-ceremony, it
  completes off-screen; scrolling back finds the clean word.
  *Disabled:* JS off = the clean word; the ghost never arms.
- **Content merge.** The ghost is the word's own second impression
  — same glyphs, same ink, wrong by 3px. It exists only because
  this word was printed by this press on this sheet. Remove the
  word and the effect has nothing to act on; that is the test
  every element in this theme must pass.
- **Failure fallback.** The clean word is the DOM default. If the
  ghost layer fails to build or the ceremony is interrupted
  (hidden tab, stalled rAF), the 1500ms watchdog deletes the
  ghost. There is no state in which the headline's key word is
  left doubled for a reader who arrived late — late readers get
  the corrected sheet, which is also true to the fiction: the
  mill corrects its misprints before the edition ships (§6.18).
- **Reduced-motion variant.** No ghost, ever. The word prints
  clean with its line (§6.2's reduced variant). The theme's
  honesty survives without the motion: the colophon (§6.16) still
  names the edition's corrections in words.
- **Breakpoints (v2).** ≥1200px: offset 3px as specced.
  768–1199px: offset 3px, honesty beat 220ms. <768px: offset 2px
  (a phone's headline is smaller; a 3px ghost at 30px type reads
  as a blur, not a misprint), beat 200ms, registration 600ms.
- **Edge cases & failure modes (v2).** *Two words marked
  `data-misprint`:* a build error — §3 law 5 allows exactly one;
  the runtime registers only the first and the gate (§10) fails
  the build. *The word wraps across lines:* the misprint is
  cancelled for that build (a wrapped word cannot carry an inline
  ghost cleanly) and the gate flags the headline's length.
  *Session repeat visits:* the ceremony replays on each fresh
  load — every printed sheet in the edition carries the same
  corrected misprint, which is how editions work.
- **Accessibility spec (v2).** The ghost is `aria-hidden` and
  pointer-events none; the accessible headline contains the word
  once, spelled correctly, from first paint — a screen reader
  never meets the flaw, because the flaw is a visual printing
  state, not content. The 260ms doubled state is a transform +
  opacity on a duplicate layer; the true word never moves, so
  legibility of the real text is uninterrupted. Contrast of the
  true word: 12.4:1 throughout.
- **Performance budget & mobile variant.** One duplicate span, one
  transform + opacity, compositor-only; the ghost is removed from
  the DOM at ceremony end so it costs nothing thereafter. Mobile:
  the 2px variant above.
- **Tokens consumed (v2).** `--sumi`, `--sumi-soft`, `--ease-press`,
  `--misprint-offset` (3px), `--misprint-beat` (260ms),
  `--register-dur` (700ms).

### 6.4 Page-turn sections — turning the sheet

- **What & why.** Sections in this theme are not revealed; they are
  *turned to*. As the visitor scrolls across a sheet boundary, the
  outgoing sheet's top edge — its deckle — curls (rotateX 0 → −18°)
  while the next sheet slides up beneath it, and the boundary pins
  briefly while the turn completes. It belongs because it is the
  theme's central act: reading a stack of handmade sheets *is*
  turning them, and the turn is performed by the sheet the content
  is printed on, not by a transition laid over it.
- **Structure.** Each `<section class="sheet">` is a 3D scene:
  `perspective: 1400px` on the stack container; the sheet's deckled
  top strip (the top 120px, clipped by the sheet's own deckle path,
  §4) is a separate layer (`.sheet-curl`) with `transform-origin:
  top`, `backface-visibility: hidden`, its back face painted
  `--kozo-deep`. The sheet's body never transforms — only the
  deckled edge curls, so text is never distorted. The incoming
  sheet is the next sibling in normal flow, translated up by the
  deckle overlap (§4) as the turn progresses. All curl states are
  written by the shared rAF loop from scroll position; the DOM
  default is flat sheets in a stack.
- **Motion spec.** Scrubbed, not triggered: as a boundary crosses
  the viewport's 62% line, a 30vh scrub range drives it. Curl:
  rotateX 0 → −18° across the first 60% of the range, easing
  `--ease-turn` applied to the scrub value (the value is lerped
  at 0.12 by the shared loop). Incoming sheet: translateY from
  +8px (its resting overlap) to 0 across the full range. Pin: the
  outgoing sheet's container is `position: sticky` for exactly
  the scrub range (30vh), then releases — a brief pin, counted:
  at most 4 pinned boundaries per page (§4). At range end the
  curl rests at −18° while the sheet is above the reading line
  and relaxes to 0 over 300ms when it leaves the viewport — a
  turned sheet lies flat in the stack behind.
- **Choreography timeline (v2).** Scrubbed, so the timeline is a
  map: boundary at 62% line → curl 0°, incoming at +8px →
  boundary crosses 47% line → curl ≈ −9°, the deckle's shadow
  deepening on the incoming sheet → boundary at 32% line → curl
  −18°, incoming at 0, pin releases → outgoing sheet exits top →
  its curl relaxes flat over 300ms. Scrolling up reverses the
  map exactly — sheets can be turned back, because the state is
  a pure function of scroll position.
- **State matrix (v2).** *Rest (below boundary):* flat sheet,
  deckle uncurled. *Turning:* scrubbed curl + slide, desktop and
  touch identical. *Turned (scrolled-past):* sheet flat in the
  stack, curl relaxed; its content remains fully readable to a
  scroll-back. *Hover:* none — sheets do not respond to pointers;
  cards inside them do (§6.8). *Focus:* a focus jump to an element
  in the incoming sheet snaps that boundary to its end state
  instantly (no scrubbed turn may delay focus). *Disabled
  (no-JS):* flat stack, all sheets readable in flow.
- **Content merge.** The curling layer is the outgoing sheet's own
  deckled edge and the sliding layer is the incoming sheet's own
  body. The turn *is* the navigation between the two sections'
  contents; remove either section and there is nothing to turn.
- **Failure fallback.** The standing 800ms law, inherited from the
  original entry: if scroll position becomes unreadable, the loop
  stalls 800ms, or a boundary's geometry cannot be measured, all
  curls snap flat and pins release — the page becomes the static
  stack, which is the no-JS state. A watchdog owns this;
  `transitionend` never does.
- **Reduced-motion variant.** No curl, no pin, no slide. Sheets
  stack in flow with their deckle shadows only — the sample-book
  presentation. Every section boundary is a deckled edge and a
  furniture line (§6.10); nothing is hidden or delayed.
- **Breakpoints (v2).** ≥1200px: full spec, curl −18°, pin 30vh.
  768–1199px: curl −14°, pin 24vh. <768px: curl −10° on the top
  80px strip only, pin 16vh, and at most 2 pinned boundaries per
  page — a phone's thumb scroll is fast and a long pin taxes it;
  sheets beyond the second boundary turn by deckle shadow alone.
- **Edge cases & failure modes (v2).** *Fast fling across two
  boundaries:* both turns resolve to their mapped end states; the
  loop's lerp settles within 300ms of scroll rest and no curl is
  left mid-angle (the settle rule). *Short sheet (<40vh):* its
  boundary's scrub range compresses to 60% of the sheet's height
  so the turn completes inside its own sheet. *Anchor jump into
  sheet 5:* all earlier boundaries snap to turned state on the
  first frame — the reader arrives at a stack already turned.
  *Print:* all sheets flat, in order, deckles as printed edges.
- **Accessibility spec (v2).** The curl layer is `aria-hidden`
  decoration cloned from no content (it is the sheet's edge, not
  its text); DOM order is document order at all times and heading
  navigation is unaffected by pin or curl. Focus is never moved
  by a turn. The 3D transform applies only to the empty deckle
  strip — no text is ever rendered on a rotated plane, so no
  reader ever reads tilted type.
- **Performance budget & mobile variant.** One transform per
  boundary in the watch band (≤2 boundaries live at once),
  compositor-only; the sticky pin is a class toggle, not a
  per-frame write. Loop cost ≤0.8ms/frame for this element.
  Mobile: the reduced curl/pin variant above.
- **Tokens consumed (v2).** `--kozo`, `--kozo-deep`, `--ease-turn`,
  `--curl-max` (−18°), `--pin-range` (30vh), `--loop-lerp` (0.12).

### 6.5 The long fibre — the maker's flaw, spanning three sheets

- **What & why.** One fibre in the page's fibre field breaks every
  rule the others obey: it is noticeably longer (it crosses three
  whole sections), darker (`--fibre-line` at 55% instead of 34%),
  and it *sways* — ±2px in a slow 14s loop, almost imperceptible,
  endless. It belongs because it is the theme made visible: a real
  sheet of handmade paper contains exactly such accidents, and
  this theme's law (§1) is that the accident is left in, measured,
  and confessed (§6.16 prints its length). Every other fibre on
  the page exists partly to make this one findable.
- **Structure.** One SVG path in a page-level fibre layer that sits
  behind sheets 2–4 (its span is defined by content, not by the
  viewport): a single quadratic curve, ~1900–2400px of rendered
  length at desktop width, stroke 1.5px, generated with a fixed
  seed so it is the *same* fibre for every visitor and every
  builder — the flaw is an edition constant. Its sway is a
  translateX on the path's layer, written by the shared loop. The
  ordinary fibre field (§4) is per-sheet and static; this layer is
  per-page and is the field's one licensed exception.
- **Motion spec.** Two motions, both scrubbed or ambient, never
  triggered. *Parallax:* the layer drifts at 0.96× sheet speed
  (§5) via the shared loop, lerp 0.12 — it lags the print by the
  paper's thickness, like every fibre. *Sway:* translateX follows
  a 14s sine, amplitude ±2px, `--ease-sway` shaping; it pauses
  when the fibre's span is fully off-screen (IntersectionObserver
  on the layer) and when the tab is hidden. The sway is the
  theme's first ambient loop (§5 ration: two, this and §6.5's
  grain note below). *Grain shadow play (the second ambient
  loop):* a `--fibre-shadow` gradient across the whole stack
  shifts 14px over 26s, alternate — light moving across grain,
  so slow it is felt before it is seen.
- **Choreography timeline (v2).** Continuous, so the timeline is
  a map: page load → fibre at rest position, sway at phase 0 →
  scroll: the layer lags sheets by 4% of travel, so the fibre
  appears to slide *inside* the paper as sheets pass over it →
  sway crosses 0 at 3.5s, +2px at 7s, 0 at 10.5s, −2px at 14s,
  loop → the fibre's span exits the viewport → sway and parallax
  writes stop; it resumes, phase-preserved, on re-entry.
- **State matrix (v2).** *Rest:* fibre present at mapped position
  — including no-JS (the path is in the static SVG; only the sway
  is JS). *Swaying:* ±2px, 14s, desktop and touch identical.
  *Hover / focus:* none — the fibre is not a control and is never
  highlighted on demand; a flaw that performs is a feature, and
  this is a flaw. *Scrolled-past:* the fibre stays where the
  sheets left it; it does not follow the reader. *Disabled:*
  no-JS = the printed fibre, still and present.
- **Content merge.** The fibre runs *beneath the content it
  crosses* — under three sections' text, inside their sheets. It
  is not beside the content or above it; it is in the paper the
  content is printed on, and the colophon (§6.16) names the
  sections it crosses. Remove those sections and the fibre's span
  is re-measured to the new stack — the flaw belongs to the page,
  not to a decoration layer.
- **Failure fallback.** The fibre is static SVG in the base
  markup; if the loop or observer fails, the page keeps its fibre,
  unmoving. There is no state in which the flaw is missing — a
  missing flaw would be the one dishonest outcome this element
  exists to prevent.
- **Reduced-motion variant.** No sway, no parallax lag (the layer
  scrolls at 1.0× with the page), no grain play. The fibre is
  printed, present, and still — its length and darkness, not its
  motion, are its meaning, and both survive.
- **Breakpoints (v2).** ≥1200px: full span, three sections,
  amplitude ±2px. 768–1199px: span compresses with the narrower
  stack (the path re-renders to the sheet width; its *measured*
  length in the colophon is computed at build for the reference
  width and labelled as such, §12). <768px: the fibre crosses two
  sections (a phone stack is shorter; a three-section span would
  cross half the page and stop reading as an accident), amplitude
  ±1.5px, sway period 16s.
- **Edge cases & failure modes (v2).** *A section in the span is
  removed by the CMS:* the path's span is regenerated at build
  from the sections carrying `data-fibre-span`; a span of fewer
  than two sections is a gate failure (§10) — the flaw must cross
  content, or it is wallpaper. *Text collision:* the fibre is the
  one fibre exempt from §4's clearance fade, but it is still
  capped: where it crosses a text block it may not exceed 55%
  opacity, and its path is routed at build to cross measures at
  shallow angles between lines where the generator can manage it.
  *Battery saver:* the sway is the first thing the §14 cut order
  suspends under sustained <40fps; the fibre remains.
- **Accessibility spec (v2).** The layer is `aria-hidden`,
  pointer-events none, and carries no information — its meaning
  is carried in words by the colophon (§6.16), which is the
  accessible form of the flaw. Sway amplitude (±2px at 0.07Hz) is
  far below any photosensitivity or vestibular threshold, and is
  removed entirely under reduced motion.
- **Performance budget & mobile variant.** One path transform per
  frame while in band; the grain gradient is one background
  position write. Total ≤0.2ms/frame. Mobile: the two-section
  variant above; the sway is cut before the parallax lag in the
  §14 order, because the lag is spatial truth and the sway is
  weather.
- **Tokens consumed (v2).** `--fibre-line`, `--bark`, `--ease-sway`,
  `--sway-amp` (2px), `--sway-period` (14s), `--loop-lerp` (0.12).

### 6.6 Ink strip progress — ink wicking down the deckle

- **What & why.** Down the page's left edge runs a narrow deckled
  strip — the torn margin of the whole stack — and it fills with
  sumi ink as the visitor reads: height scrubbed to page progress,
  its leading edge uneven, feathered, like ink wicking into fibres
  rather than a bar filling in a tube. It belongs because progress
  in this theme must be made of the page's own substances — ink
  and a torn edge — and because wicking has a property no bar has:
  it is irreversible. Ink does not un-wick; the strip records how
  far the reading has *ever* reached, not where the scrollbar sits.
- **Structure.** A fixed rail at the viewport's left edge, 12px
  wide, holding an SVG strip: the deckled silhouette (the stack's
  own deckle geometry, rotated) as a clip path, inside it a fill
  rect whose height is written by the shared loop, topped by a
  wick fringe — 5 short vertical fibre strokes of varying length
  (4–11px) at the fill's leading edge, in `--wick`. Beside the
  fringe, at sheet boundaries only, the apparatus label "SHEET n
  OF N" (rotated −90°, `--bark-deep`) updates. The fill's target
  is `max(progress)` — the high-water mark of the session's
  reading, held in a variable, never decreased by scrolling up.
- **Motion spec.** Scrubbed via the shared loop, lerp 0.12, fill
  height = high-water progress × rail height. The wick fringe
  leads the fill by its longest stroke (11px) — the ink's fingers
  run ahead of its body, as wicking does. At a sheet boundary the
  label swaps instantly (no transition — the count is paperwork,
  §5) and the fringe pulses once: strokes extend +3px over 240ms
  `--ease-wick` and relax — the ink found a loose fibre at the
  sheet's edge. At 100% the fringe dries: its strokes shorten to
  the fill edge over 600ms and the strip is complete.
- **Choreography timeline (v2).** Scrubbed map: 0% → fill 0, label
  "SHEET 1 OF N" → progress p → fill at p (high-water), fringe
  leading → each sheet boundary: label swaps, fringe pulses
  240ms → scroll up: fill *holds* (law), label follows the
  *current* sheet (the label is information and stays honest;
  only the ink is permanent) → 100% first reached: fringe dries
  over 600ms; the strip thereafter is a record, not an indicator.
- **State matrix (v2).** *Rest (top):* empty strip, fringe at top.
  *Reading:* fill at high-water, fringe wet. *Scrolling up:* fill
  held, label current. *Complete:* full strip, fringe dry.
  *Hover / focus:* none — the rail is not interactive. *Touch:*
  identical (the rail is narrower, §breakpoints). *Disabled
  (no-JS):* no rail at all (it is JS-armed); the furniture lines
  (§6.10) still tell the reader which sheet they are on.
- **Content merge.** The strip is the stack's own torn edge and
  the ink is the ink the page is printed with; its length is
  exactly the reading the visitor has done. It measures the
  content, in the content's material, on the content's margin.
- **Failure fallback.** JS off: no rail, nothing lost (see
  disabled state). Loop stall: the fill freezes at its last
  written height — a half-wicked strip is a true record of a
  stalled read, and the stall rule (§14) restarts the loop
  without animating a catch-up.
- **Reduced-motion variant.** The fill is drawn to the high-water
  length instantly per scroll position (it is a scrubbed state,
  not an animation); the fringe is always dry; the boundary pulse
  does not run. The record remains; the wicking rests.
- **Breakpoints (v2).** ≥1200px: rail 12px, rotated label beside
  the fringe. 768–1199px: rail 9px, label horizontal at the
  rail's foot. <768px: rail 6px, **label hidden** — a phone sheet
  has no margin for paperwork; the furniture (§6.10) carries the
  sheet count in the flow instead.
- **Edge cases & failure modes (v2).** *Short page (one sheet):*
  the strip still maps 0→1 across the single sheet; the label
  reads "SHEET 1 OF 1" and is hidden — a one-sheet page does not
  number itself. *Anchor jump to the footer:* the high-water
  mark jumps honestly (the reader *has* reached the footer) —
  the fill snaps on the next frame; ink does not perform a
  catch-up for teleporting readers. *Resize:* rail height
  re-measures; fill re-maps proportionally; high-water fraction
  is stored, not pixels. *Print:* rail absent.
- **Accessibility spec (v2).** The rail is `aria-hidden`; the
  sheet count, being information, is also present as real text
  in each sheet's furniture (§6.10) and in the colophon's edition
  line (§6.16), so nothing is lost by hiding the rail from AT.
  The fill's colour is never the only carrier of any fact.
- **Performance budget & mobile variant.** One rect height + one
  fringe transform per frame in the shared loop; the SVG is ~30
  path points. Mobile: the 6px label-less variant above.
- **Tokens consumed (v2).** `--sumi`, `--wick`, `--bark-deep`,
  `--ease-wick`, `--loop-lerp` (0.12), `--wick-pulse` (240ms).

### 6.7 Mulberry branch draw — the plant the sheets came from

- **What & why.** In the colophon, a mulberry branch draws itself:
  stem first, then its leaves in growth order, 1.6s of line-work in
  bark and leaf. It belongs because the colophon (§6.16) is where
  the page explains its own substance — and the explanation should
  be grown, not pasted: the drawing performs the paper's origin at
  the exact place the text states it. It is also the page's only
  botanical drawing, rationed to the one place it is *about*
  something (§9).
- **Structure.** One inline SVG (viewBox 300×210) in the colophon:
  a stem path (bark, 2px), 5 leaf paths (leaf, 1.5px outline with
  a `--leaf` fill at 14%), each leaf's vein as a separate short
  path. Every path carries `pathLength="100"`; the drawn state is
  dashoffset 0, and the undrawn state exists only under a JS-armed
  class. Beside the SVG, the colophon text (§6.16) — the drawing
  illustrates the sentence next to it, in reading order.
- **Motion spec.** Trigger: the colophon entering the viewport at
  30% visibility, once. Stem: dashoffset 100 → 0 over 620ms
  `--ease-wick`. Leaves: in growth order (lowest first — a branch
  leafs from its base), each 340ms, stagger 120ms, starting at
  t+380ms (the stem must exist before it leafs). Veins draw with
  their leaves at +60ms each, 180ms. Leaf fills fade in over the
  final 200ms of each leaf's draw. Total: 380 + 4×120 + 340 ≈
  1200ms of drawing inside a 1600ms envelope. Draws once; never
  redraws on scroll-back.
- **Choreography timeline (v2).** t+0: colophon at 30% visible →
  t+0–620ms: stem grows upward → t+380ms: leaf 1 begins (stem at
  ~70%) → t+500 / 620 / 740 / 860ms: leaves 2–5 begin → t+1200ms:
  last leaf's fill settled → branch complete; it is thereafter
  furniture — printed, still, part of the colophon.
- **State matrix (v2).** *Rest (pre-trigger / no-JS):* branch
  fully drawn — the printed colophon. *Drawing:* 1.6s envelope,
  desktop and touch identical. *Drawn:* permanent. *Hover:* none.
  *Focus:* none (the SVG is decorative beside real text).
  *Scrolled-past:* drawn; arriving via a footer anchor jump finds
  it drawn (the trigger resolves instantly for content already
  passed). *Disabled:* JS off = drawn.
- **Content merge.** The branch is the subject of the colophon
  text it stands beside: the sentence names the plant, the
  drawing grows it. It is not a logo and appears nowhere else on
  the page — a branch in the header would be a brand mark; a
  branch in the colophon is an explanation.
- **Failure fallback.** The drawn branch is the DOM default; JS
  arms the undrawn state only when the colophon is below the
  fold and the observer is live. If anything fails, the colophon
  simply has its branch, printed. A 1400ms watchdog completes any
  interrupted draw instantly.
- **Reduced-motion variant.** No draw. The branch stands complete
  in the colophon from first paint — a printed botanical plate,
  which is what the reduced-motion sheet always is.
- **Breakpoints (v2).** ≥1200px: full 300×210 plate beside the
  colophon text. 768–1199px: 240×168, above the text. <768px:
  200×140, above the text, veins omitted (at phone width a vein
  is a hair, not information) — leaves and stem remain.
- **Edge cases & failure modes (v2).** *Colophon above the fold*
  (a very short page): the draw fires on load after the hero
  settle (§6.1), sequenced, never concurrent — two ceremonies at
  once is a parade, not a mill. *Colophon revisited via anchor:*
  drawn state; no replay. *SVG unsupported (ancient engine):* the
  colophon text stands alone; the branch's absence is invisible
  because its meaning is duplicated in words (§6.16).
- **Accessibility spec (v2).** The SVG is `aria-hidden` with the
  colophon's text carrying the full statement ("Paper mulberry —
  kozo — the bark this sheet was beaten from" is text, not image
  alt). The draw is stroke-only, no flashing, no luminance
  alternation; under reduced motion it does not run.
- **Performance budget & mobile variant.** 11 short paths, one
  dashoffset write each per frame during a 1.6s window, then
  zero cost forever. Mobile: the veinless variant above.
- **Tokens consumed (v2).** `--bark`, `--leaf`, `--ease-wick`,
  `--draw-stem` (620ms), `--draw-leaf` (340ms),
  `--draw-stagger` (120ms).

### 6.8 Corner-curl hover — the card invites turning

- **What & why.** Hovering a card grows a curl at its top-right
  corner: a small triangle of the card's own underside
  (`--kozo-deep`) folding over, its shadow deepening as it grows.
  It belongs because a card in this theme is a small sheet, and a
  sheet's affordance is its corner — the place a hand takes it.
  The curl says "this can be turned, lifted, read" in the page's
  own material, instead of a chrome hover state borrowed from a
  screen UI.
- **Structure.** Each `.sheet-card` (§6.12) carries a `.curl`
  layer at its top-right: a right triangle (clip-path polygon)
  sized 0 → 34px, filled with a `--kozo-deep` → `--fibre-shadow`
  gradient (the underside shading as it catches light), plus a
  soft shadow element beneath the fold line whose blur and
  opacity grow with the curl. The fold line sits at 45° — the
  geometry of a real corner fold, so the triangle's legs are
  equal. The curl is driven by a per-card spring in the shared
  loop (stiffness 0.18, damping 0.72) — paper has a slight
  overshoot, ≤2px, as the fibre resists then yields.
- **Motion spec.** Trigger: pointerenter / focus-within on the
  card. Curl grows 0 → 34px over ~240ms with the spring's single
  overshoot to 36px at t≈180ms, settling at 240ms. Shadow:
  opacity 0 → 0.35, blur 2 → 6px, tracking the curl's size. On
  leave: the corner settles back over 200ms `--ease-sway` — no
  overshoot on the way down; paper released falls flat, it does
  not bounce. Only one card on the page curls at a time; entering
  a second card flattens the first instantly.
- **Choreography timeline (v2).** t+0: pointer enters → t+0–180ms:
  triangle grows to 36px, shadow deepening → t+240ms: curl at
  34px, held while hover/focus lasts → the card's title (§6.12)
  does not move; the curl occupies only the corner's own 34px,
  over the card's margin, never over text (cards reserve a 40px
  corner zone, §6.12) → leave: t+0–200ms settle flat.
- **State matrix (v2).** *Rest:* flat card. *Hover (desktop):*
  curled 34px, shadow deep. *Focus-within:* curled identically —
  keyboard readers get the same invitation. *Active (press):*
  the curl yields to §6.9's impression (curl flattens to 12px as
  the press lands — a pressed sheet's corner is held down).
  *Scrolled-past:* flat; curls never run off-screen. *Touch:*
  first tap curls (and does not activate); second tap activates
  — the two-tap grammar of §6.9. *Disabled card* (a sold-out
  edition, §6.12): curls to 16px only — old paper, stiff corner —
  and its state is also stated in text, never by curl alone.
- **Content merge.** The curling surface is the card's own
  underside — the same sheet, other side. It reveals nothing but
  the card's material, which is the point: the affordance is the
  object itself, not an icon on it.
- **Failure fallback.** JS off: cards are flat, fully legible,
  their links plain. The curl is a JS-armed layer; its absence
  changes nothing about the card's content or action.
- **Reduced-motion variant.** No growth animation: on hover/
  focus the curl appears instantly at 22px (a smaller, static
  fold) — the invitation survives, the physics rests. Touch
  two-tap grammar unchanged (it is interaction, not motion).
- **Breakpoints (v2).** ≥1200px: curl 34px as specced.
  768–1199px: curl 28px. <768px: hover does not exist — the curl
  is tap-driven (first tap 24px), and the first card in each
  sheet carries a persistent 10px curl as a standing hint that
  corners lift here.
- **Edge cases & failure modes (v2).** *Pointer skims a card
  grid:* a 60ms intent delay before growth, so a diagonal path
  doesn't flutter five corners; leaving within the delay cancels
  cleanly. *Card near the viewport edge:* the curl grows inward
  (it is inside the card by construction) — it can never clip.
  *Rapid re-entry:* the spring restarts from its current size;
  no queue, no stuck corner (a 600ms watchdog flattens any curl
  whose card is neither hovered nor focused).
- **Accessibility spec (v2).** The curl layer is `aria-hidden`;
  the card's link carries its full accessible name regardless of
  curl state. Focus-within parity is mandatory (see state
  matrix). The curl never covers the card's focus outline: the
  outline is drawn on the card's border, the curl inside its
  corner zone. Touch targets: the whole card, ≥44px by
  construction (smallest card ≥148px wide).
- **Performance budget & mobile variant.** One clip-path +
  shadow on one card at a time, inside the shared loop; ≤0.2ms
  per frame. Mobile: the tap-driven variant above.
- **Tokens consumed (v2).** `--kozo-deep`, `--fibre-shadow`,
  `--ease-sway`, `--curl-size` (34px), `--curl-dur` (240ms).

### 6.9 Impression click — the press answers the finger

- **What & why.** Clicking a card presses it: the whole card
  scales to 0.99 while an inset shadow deepens around its edges —
  the letterpress impression, the sheet taking pressure and
  showing it — then releases over 300ms. It belongs because
  feedback in this theme is the press acting on the sheet the
  visitor touched: the click is answered by the same force that
  printed the page. A ripple or a colour flash would be screen
  feedback on a paper object; an impression is the object
  responding in kind.
- **Structure.** The press is a class-driven transition on the
  card itself (`transform: scale`, `box-shadow: inset`), computed
  inside the shared loop's spring so it never gates the click's
  action (navigation or filing proceeds immediately; the
  impression is the acknowledgement, not a toll). The inset
  shadow is deepest at the card's deckled edge (§4) — pressure
  shows where the paper is thinnest, which is the kind of detail
  this theme exists to keep.
- **Motion spec.** Trigger: pointerdown / keyboard activation on
  the card or its link. Press-in: scale 1 → 0.99 and inset shadow
  0 → 10px over 90ms `--ease-press` (pressure is fast — a press
  does not drift down). Hold: while the pointer holds, up to a
  400ms cap. Release: 300ms `--ease-settle`, shadow relaxing
  last (the paper keeps the impression a beat after the pressure
  leaves — at t+300ms the shadow is at 15%, gone at t+380ms).
  The action itself fires on the platform's normal click; the
  impression never delays it by a millisecond.
- **Choreography timeline (v2).** t+0: pointerdown → t+90ms:
  full impression (scale 0.99, inset 10px, curl flattened to
  12px per §6.8) → hold ≤400ms → release: t+0–300ms scale
  returns, shadow lags → t+380ms: card at rest, impression gone
  — unless the click navigated, in which case the impression is
  the last thing seen on the old sheet (§6.15).
- **State matrix (v2).** *Rest:* flat, unpressed. *Hover:*
  §6.8's curl, no impression. *Focus:* the card's ring (§6.12)
  plus §6.8's curl; Enter/Space fires the full impression —
  keyboard presses are presses. *Active:* as specced.
  *Scrolled-past:* at rest. *Touch:* tap = press (the first tap
  curls per §6.8; the activating second tap presses). *Disabled
  card:* no impression — a withdrawn sheet is not pressed; its
  press attempt returns nothing, and its state is stated in text
  (§6.12), not by silence alone: the card carries
  `aria-disabled` and its reason in the figure line.
- **Content merge.** The pressed object is the card — its paper,
  its deckle, its print. The impression is deepest at its own
  thinnest edge. Remove the card and there is nothing to press;
  the feedback cannot be detached and reused, which is correct.
- **Failure fallback.** JS off: clicks are plain clicks; cards
  navigate. The impression is an enhancement layer on a working
  action — its absence is undetectable in function.
- **Reduced-motion variant.** No scale, no shadow travel: the
  card's border inks to `--bark-deep` for 160ms on activation —
  acknowledgement by ink, the print-native way — then returns.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: inset
  8px. <768px: scale 0.995, inset 6px — a phone card is small and
  a full 1% press shifts its neighbours' shadows visibly; the
  acknowledgement stays, the drama halves.
- **Edge cases & failure modes (v2).** *Click-and-drag off the
  card:* the release runs from wherever the press had reached;
  no stuck impression (the 600ms watchdog of §6.8's family
  applies). *Double-click:* two impressions, each complete; no
  queue builds. *Press during the card's entry (§6.12):* the
  entry completes first (≤300ms) and the impression is applied
  to the settled card — a sheet is not pressed while it is still
  being laid down.
- **Accessibility spec (v2).** The impression is decorative
  feedback on an action whose state is conveyed by the action's
  own result (navigation, filing, the §6.14 form's ledger line).
  It is never the only signal: focus is the ring, activation is
  the outcome, the impression is the paper agreeing. Keyboard
  parity is mandatory (see state matrix).
- **Performance budget & mobile variant.** One transform + one
  shadow on one element; zero layout. Mobile: the halved variant
  above.
- **Tokens consumed (v2).** `--fibre-shadow`, `--bark-deep`,
  `--ease-press`, `--ease-settle`, `--press-scale` (0.99),
  `--press-dur` (300ms).

### 6.10 Sheet furniture & stack navigation — the running head

- **What & why.** Navigation in this theme is the stack's own
  furniture: a running head at the page top listing the sheets as
  a mill hand would pencil them — sheet name, paper, grammage —
  and each sheet's own furniture line (§4) marking where in the
  stack the reader stands. It belongs because a stack of sheets
  is navigated by its edges and its pencil notes, not by a menu
  bar borrowed from an app; the furniture *is* the table of
  contents, printed on the sheets themselves.
- **Structure.** A `<nav class="running-head">` in the first
  sheet's head: items in stack order, each an `<a>` with the
  sheet's name (Mincho 500) and its figure line (paper ·
  grammage, §3). The current sheet's item is printed in sumi at
  full weight with a short bark rule beneath; others sit in
  `--bark-deep`. Each sheet section carries its own furniture
  line (§4) — "SHEET 3 OF 7 · KOZO, LONG FIBRE · 128 G/M²" — as
  its first element, generated from the same data as the nav, so
  the two can never disagree. On mobile the running head becomes
  a "The stack" toggle opening a sheet list (§11 grammar).
- **Motion spec.** Hover/focus on an item: its bark rule draws
  in from the name toward the figure line (background-position
  sweep, 180ms `--ease-press`). Current-sheet tracking: as the
  reader crosses a sheet boundary (§6.4), the outgoing item's
  rule relaxes (240ms) and the incoming item inks to full sumi
  over 200ms — a scrollspy performed as pencilling, not a
  sliding pill. The mobile list opens with the §6.4 turn grammar
  at panel scale (rotateX −8°, 260ms) — a small sheet lifting.
- **Choreography timeline (v2).** Hover: t+0 rule sweep begins →
  t+180ms rule full, figure line warms to sumi → leave: rule
  relaxes 240ms. Boundary change: t+0 outgoing inks down →
  t+200ms incoming at full sumi with its rule drawn — the two
  overlap for one beat, like a hand moving down a list.
- **State matrix (v2).** *Rest:* current item inked + ruled,
  others bark-deep. *Hover / focus:* rule draws, figure warms —
  identical for keyboard. *Active / current:* as rest-current,
  with `aria-current="true"`. *Scrolled-past:* the head scrolls
  away with the first sheet — no sticky nav ever appears; the
  furniture lines in each sheet carry orientation from there.
  *Touch:* items are ≥44px rows in the mobile list. *Disabled:*
  a sheet with no content is absent from the head — never a
  greyed item; an empty sheet is not listed, it is not made.
- **Content merge.** The items are the page's real sheets with
  their real papers and grammages — generated from the sheets
  themselves. Add a sheet and the head gains a line, because the
  head *is* the stack's contents, not a marketing menu.
- **Failure fallback.** Plain anchor list in the first sheet;
  rules are CSS and survive without JS; the scrollspy is the
  only JS behaviour, and its absence leaves the first item
  marked current by the server where known, and every furniture
  line still correct.
- **Reduced-motion variant.** No rule draw (rules appear at
  full), no panel turn (instant open), scrollspy ink changes
  instant.
- **Breakpoints (v2).** ≥1200px: horizontal running head inside
  the first sheet. 768–1199px: wraps to two rows; figure lines
  shorten to grammage only. <768px: "The stack" toggle + panel
  list, two-line items (name, then figures), ≥44px rows.
- **Edge cases & failure modes (v2).** *More sheets than the
  head holds (>7):* the head lists first-level sheets only;
  sub-sheets live in their parent sheet's furniture. A contents
  of 15 lines is a catalogue, not a stack. *Very long sheet
  names:* truncate at 24ch in the head, full in the mobile list
  and in `aria-label`. *Single-sheet page:* the running head is
  omitted — a one-sheet page has no stack to list.
- **Accessibility spec (v2).** A real `<nav>` with
  `aria-label="Sheets in this stack"`; current item carries
  `aria-current="true"` (updated on boundary changes only).
  Rules are CSS, invisible to AT. Focus order = stack order.
  The mobile toggle is a `<button aria-expanded>`; Esc closes
  it and returns focus to the toggle.
- **Performance budget & mobile variant.** Scrollspy runs on the
  shared IntersectionObserver — free. Mobile: the toggle/panel
  variant above.
- **Tokens consumed (v2).** `--sumi`, `--bark`, `--bark-deep`,
  `--ease-press`, `--rule-draw` (180ms), `--spy-fade` (200ms).

### 6.11 The first sheet — hero composition

- **What & why.** §6.1 specifies how the hero sheet lands; this
  element specifies what is composed on it before it lands: one
  sheet, fully printed — headline (§6.2, with its misprint word,
  §6.3), standfirst, the sheet's figure line, one plate (a
  photograph of the paper or process, printed in a bark-ruled
  frame), and the sheet's single action, lettered as a line of
  the sheet's own text. The composition's job is the sample
  sheet a mill sends out: everything the visitor needs to judge
  the paper is on this one sheet, including its flaw.
- **Structure.** `<section class="sheet sheet--hero">`: furniture
  line (§6.10), headline block (≤3 lines, §3), standfirst (≤34
  words, body setting), figure line (paper · grammage · sheet
  size — real figures, §1), the plate (§6.12's frame grammar at
  hero scale, aspect from the plate's real dimensions), and one
  action line — a text link with §6.10's drawn rule, worded as
  the sheet's own sentence ("See the sheets" / "Order a sample
  pack"), never a filled button: a first sheet carries print,
  not chrome.
- **Motion spec.** The composition itself has no independent
  motion: it rides the settle (§6.1), its headline prints (§6.2),
  its word registers (§6.3), its plate settles (§6.12). The one
  compositional rule with a timeline: the plate's settle begins
  only after the headline's last line has printed — the eye
  reads the title before it is offered a picture, as it does on
  a printed sheet.
- **Choreography timeline (v2).** t+0: sheet paints complete
  (no-JS state — this exact composition, readable) → t+60ms:
  settle begins (§6.1) → t+500ms: headline prints (§6.2) →
  t+~1200ms: misprint registers (§6.3) → headline complete →
  plate settle begins (700ms, §6.12) → t+~2000ms: the first
  sheet is at rest, fully printed, fully still.
- **State matrix (v2).** *Rest:* the printed first sheet — the
  permanent and no-JS state. *Arriving:* the §6.1/§6.2/§6.3
  ceremonies, identical on touch. *Hover:* the action line's
  rule (§6.10); the plate does not perform. *Focus:* first
  tab stop is the action line (the furniture nav precedes it in
  DOM where present, §6.10). *Scrolled-past:* the sheet lies
  flat in the stack (§6.4). *Disabled:* the static composition.
- **Content merge.** Everything on the first sheet is the
  offering itself: its headline names it, its figure line
  measures it, its plate shows it. The composition sells nothing
  but the paper and what is printed on it.
- **Failure fallback.** The disabled state above; a slow network
  shows §6.15's unprinted sheet in this composition — same
  layout, blank measures — so the first screen is never a
  spinner over a void.
- **Reduced-motion variant.** The static composition: sheet
  settled, headline printed, word clean, plate flat. Every fact
  present; no ceremony.
- **Breakpoints (v2).** ≥1200px: plate right of the headline
  block at 38% width. 768–1199px: plate below the standfirst,
  62% width. <768px: single column — furniture, headline,
  standfirst, plate full width, figure line, action — in that
  order; the plate's aspect is preserved, never cropped.
- **Edge cases & failure modes (v2).** *No plate exists for the
  offering:* the composition holds without one — headline,
  standfirst and figures widen to the measure; a stock photo of
  somebody else's paper is forbidden (§9). *Very short
  viewport:* the plate shrinks before the headline does (the
  words outrank the picture, §3) but never below 180px tall —
  below that, the plate moves after the action line instead.
- **Accessibility spec (v2).** Landmarks: the sheet is a
  `<section>` with the h1 as its heading; the plate's `alt` is
  real (it is evidence of the paper's surface, so its alt says
  what the surface shows: "Kozo sheet against the light —
  long fibres visible, deckle at top"). The figure line is
  text, read in order. Reading order = DOM order at all sizes.
- **Performance budget & mobile variant.** The plate is the
  hero's only image: ≤120KB, responsive, `fetchpriority="high"`;
  everything else is type and SVG line-work. Mobile: the
  single-column variant above.
- **Tokens consumed (v2).** `--kozo`, `--sumi`, `--bark`,
  `--bark-deep`, `--ease-settle`.

### 6.12 Sheet sample cards — small sheets, honestly measured

- **What & why.** Where the site presents a set of comparable
  things — papers in the mill's range, prints in an edition,
  sheets in a sample pack — they are sample cards: small stiff
  sheets, each deckled at the top, each carrying a plate, a name
  in Mincho, a figure line with its real grammage and dimensions,
  and one line of the maker's prose. A card in this theme is a
  sample of the thing itself, not a tile about it: a visitor
  judges the range the way they would thumb a sample book.
- **Structure.** `<article class="sheet-card">`: deckle strip
  (the card's own miniature of §4's path), plate (photograph,
  duotone-warm via CSS filter over the real image, framed in a
  1px bark rule), name, figure line (grammage · size · stock
  state — a real state, §1), prose line (≤16 words), and one
  thread link ("See this sheet") as the card's only action. The
  top-right 40px is the reserved corner zone (§6.8). The whole
  card is one link via the stretched-link pattern on its name,
  except when it carries the sample-request action (§6.14
  pre-fill), in which case two explicit targets exist and no
  stretched link is used.
- **Motion spec.** Entry: cards are laid down in reading order
  as their sheet (§6.4) arrives — each settles (scale 1.015 →
  1, 380ms `--ease-settle`, stagger 90ms, max 5 per sheet, §4)
  with its deckle shadow arriving first, the way a sample is
  placed before it is seen flat. Plates inside cards settle
  1.05 → 1 over 600ms as they cross the viewport centre (the
  §5 image treatment at card scale). Hover: §6.8's curl.
  Click: §6.9's impression. No other motion exists on a card.
- **Choreography timeline (v2).** Sheet arrival → t+0: card 1's
  shadow lands → t+60ms: card 1 settles → t+150 / 240 / 330 /
  420ms: cards 2–5 follow → each plate settles independently as
  it crosses centre → cards are thereafter furniture: curl on
  approach (§6.8), impression on press (§6.9), nothing else,
  ever.
- **State matrix (v2).** *Rest:* flat sample, plate settled.
  *Hover:* corner curl (§6.8). *Focus:* curl + the name link's
  ring (2px `--bark-deep`, offset 3px). *Active:* impression
  (§6.9). *Scrolled-past:* flat, plate settled. *Touch:* centre-
  transit plate settle only; tap grammar per §6.8/§6.9.
  *Disabled / out of stock:* the card remains — a sample of an
  exhausted paper is still a sample — with its figure line
  stamped in `--bark-deep`: "THIS BATCH IS GONE — THE NEXT IS
  BEATEN IN [MONTH]" (a real month or no stamp; §1), its link
  removed, its curl halved (§6.8).
- **Content merge.** Every part of the card is the sample it
  presents: its plate is the paper's surface, its figures are
  the paper's measures, its deckle is the paper's edge at
  miniature scale. A card for a paper with no photograph uses a
  fibre-field plate (the sheet's own generated field, §4) —
  the grammar holds without inventing imagery.
- **Failure fallback.** Static deckled card, plate at final
  scale — the no-JS card is the finished card. Entry settles are
  JS/CSS enhancements on a complete object.
- **Reduced-motion variant.** No settle, no plate travel: cards
  stand laid; hover/focus gives the static 22px curl (§6.8's
  variant) and the border inks to `--bark-deep`.
- **Breakpoints (v2).** ≥1200px: cards in mixed spans within
  their sheet (never a uniform grid of identical cards — vary
  span or plate aspect, §9). 768–1199px: two-up. <768px: one-up
  stacked, plate aspect preserved, settle stagger 60ms.
- **Edge cases & failure modes (v2).** *Missing plate:* the
  fibre-field plate (above) — never a grey box, never a stock
  photo of another mill's paper. *Long name:* clamps at 2 lines;
  the full name lives in the link's accessible name. *A whole
  sheet of cards entering at once (listing page, §7):* the
  §6.4 boundary cap applies — cards beyond the first sheet's
  five arrive laid, not settling. *Stock state changes
  mid-session:* the stamp updates in place without motion; a
  sample does not celebrate or mourn its batch.
- **Accessibility spec (v2).** One link per card (its name),
  with the full name as its accessible name; the plate is
  decorative (`alt=""`) when the name + figure line carry the
  content, or carries real alt when the surface *is* the
  content (paper samples: the surface is the content — alt
  describes fibre and finish, §6.11's rule). Figure lines are
  real text in reading order. Focus ring as specced, visible
  over the curl (§6.8).
- **Performance budget & mobile variant.** Plates ≤60KB each,
  lazy below the first sheet; settles are compositor-only and
  capped at 5 per sheet. Mobile: one-up variant above.
- **Tokens consumed (v2).** `--kozo`, `--fibre-shadow`, `--sumi`,
  `--bark`, `--bark-deep`, `--ease-settle`, `--card-settle`
  (380ms), `--plate-settle` (600ms).

### 6.13 The grammage ledger — the table as a mill record

- **What & why.** Where figures must be compared — papers by
  grammage, sheets by size, editions by count — the theme's
  table is a ledger page: ruled lines, tabular figures, the
  mill's hand in the header row. It belongs because comparison
  in a mill is done in the record book, and because §1's law
  needs a place where every figure can be audited side by side:
  the ledger is where invented numbers would be caught, so the
  ledger is designed to make catching them easy.
- **Structure.** `<table class="ledger">`: header row in the
  apparatus setting (§3) on `--fibre-shadow`; body rows ruled
  with `--hairline`; figure columns right-aligned, tabular,
  always with units in the header (never repeated per cell —
  "G/M²" is stated once, at the top, like a ledger's column
  head). The first column is the sheet's name (Mincho 500). A
  row for the page's own sheet is marked with a bark rule at
  its left — "the sheet you are standing on" — and a caption
  beneath the table states the figures' source in the
  colophon voice ("Figures from the mill book, [month year]").
- **Motion spec.** The ledger does not animate its rows in.
  Rows are records; records stand. The one motion: the current
  sheet's bark rule draws (scaleX 0 → 1, 300ms `--ease-wick`)
  when the ledger first enters — the hand underlining the row
  the reader came from. Hover on a row warms its rule to
  `--bark-deep` over 160ms. Nothing else moves; a table that
  performs is a table that doubts its figures.
- **Choreography timeline (v2).** t+0: ledger at 40% visible →
  the current row's rule draws 300ms → ledger at rest, forever.
  Hover: rule warms 160ms in, 200ms out. That is the whole
  timeline, deliberately.
- **State matrix (v2).** *Rest:* printed ledger. *Hover:* row
  rule warmed. *Focus:* a focusable row (rows are focusable
  only when they are links to sheets, §6.12's targets) shows
  the §6.12 ring on its name cell. *Active:* §6.9's impression
  at row scale (inset 6px) if the row navigates. *Scrolled-
  past:* printed. *Touch:* no hover; tap navigates where rows
  link. *Disabled:* a row for a gone batch (§6.12) stands in
  the ledger with its stamp in the name cell — records are not
  deleted from ledgers; they are ruled through (a single
  `--bark-deep` line through the row's figures, its name still
  legible — the ledger's way of saying *was*).
- **Content merge.** The ledger's rows are the mill's actual
  range and its figures are §1's figures — the same dataset
  that prints the cards (§6.12) and the furniture (§6.10),
  verified by the §10 dataset-unity gate.
- **Failure fallback.** A plain table. It was always a plain
  table; the rule draw is the only enhancement and its absence
  is invisible.
- **Reduced-motion variant.** The current row's rule stands
  drawn; hover warming is instant. Nothing else changes.
- **Breakpoints (v2).** ≥1200px: full ledger, all columns.
  768–1199px: the prose column (fibre note) drops; figures
  remain. <768px: the ledger becomes a stack of ruled entries
  (name, then its figures in one line each) — a ledger page
  turned sideways is still a ledger; a squeezed table is not.
- **Edge cases & failure modes (v2).** *More rows than a sheet
  holds (>12):* the ledger continues on the next sheet with
  its header row repeated and the furniture updated ("LEDGER,
  CONTINUED") — records continue; they do not scroll inside a
  box. *A figure the mill will not state:* the cell carries an
  em dash and the caption says why ("— NOT YET MEASURED FOR
  THIS BATCH") — a dash with a reason is honest; a plausible
  number is a gate failure (§10).
- **Accessibility spec (v2).** Real `<table>` semantics with
  `<th scope="col">`, a `<caption>` carrying the source line,
  and units in the headers so screen readers announce figures
  with their measures. The ruled-through gone row is conveyed
  in text (its stamp), never by the line alone. Contrast:
  figures sumi on kozo 12.4:1; header labels `--bark-deep`
  5.1:1 minimum.
- **Performance budget & mobile variant.** Zero per-frame cost;
  one 300ms transform per ledger. Mobile: the stacked-entries
  variant above.
- **Tokens consumed (v2).** `--kozo`, `--fibre-shadow`, `--sumi`,
  `--bark`, `--bark-deep`, `--hairline`, `--ease-wick`.

### 6.14 The order sheet — the conversion form

- **What & why.** Every mill takes orders on a sheet: the theme's
  conversion form is a printed order sheet laid on the last
  sheet of the stack — ruled lines to write on, the paper chosen
  from the range as radio rows that are themselves small sheets,
  and a submit that is *pressed*, not clicked. It belongs
  because conversion in a paper world is an order written by
  hand and sent to the mill; the form's honesty (name, address,
  paper, quantity in sheets, one press) is the theme's answer
  to dark-pattern checkout.
- **Structure.** `<form class="order-sheet">` inside its sheet:
  a Mincho headline ("Order sheets / Ask for samples" — the
  build's real act, §12), fields as bottom-ruled inputs
  (transparent ground, 2px sumi bottom rule, body-size input
  text, apparatus labels above in `--bark-deep`), the paper
  choice as radio rows — each row a miniature sheet (deckle
  strip, name, figure line) that takes §6.9's impression when
  chosen and holds a bark rule while selected — a quantity
  field in *sheets* (the mill's unit, with the pack sizes stated
  in the label: "Quantity — in sheets (packs of 25)"), and the
  submit as a wide ruled plate lettered "Press this order" that
  performs §6.9's impression at form scale on activation.
- **Motion spec.** Entry: the order sheet is already laid (it
  arrives with its sheet, §6.4 — a form does not perform an
  entrance). Field focus: the field's rule inks from
  `--hairline` to `--bark-deep` (200ms `--ease-press`) and a
  fibre-shadow plate slides in beneath the rule from the left
  (200ms) — the line being written on is backed by the sheet's
  shadow, as a hand backs paper. Error: the rule turns `--bark`
  at full strength and the error note letters in beneath in the
  ledger voice (§12), word by word at 40ms/word capped at
  600ms — the mill's hand writing the correction. Submit: the
  plate presses (180ms, §6.9 at scale 0.995); on success the
  whole form is *filed*: it settles 4px down into the stack
  (300ms `--ease-settle`) and is replaced in place by the filed
  line — a ledger entry with the order's real reference (§6.18's
  numbering) and the mill's promise with a date (§12).
- **Choreography timeline (v2).** Focus: t+0 rule inks → t+200ms
  plate seated. Error (on blur/submit): t+0 rule barks → t+80ms
  note begins lettering → ≤t+680ms note complete, focus moves
  to the first errored field on submit only. Submit: t+0 press
  → response → success: form settles 4px (300ms) as the filed
  line's rule draws (300ms `--ease-wick`) — the order becomes a
  record in the same motion that files it.
- **State matrix (v2).** *Rest:* blank ruled sheet, papers
  unchosen. *Hover:* radio rows curl at §6.8's grammar (they
  are small sheets). *Focus:* rule inks + plate (fields); ring
  + rule (radio rows, which are real `<input type="radio">`
  under the sheet styling). *Active:* press. *Error:* per-field,
  persistent until corrected — errors never auto-dismiss, and
  correcting a field clears its note with a 160ms fade of the
  note only, plus the mill's acknowledgement word where §12
  provides one. *Scrolled-past:* a filled, unsubmitted form
  stays filled. *Disabled (sending):* fields disabled at full
  contrast while the press is held (≤ the network's patience);
  the plate reads "Pressing…" in the apparatus setting — no
  spinner exists in this theme.
- **Content merge.** The form is an order for the page's own
  papers: its radio rows are §6.12's cards at miniature scale,
  drawn from the same dataset; its quantity unit is the mill's
  unit; its success line is a ledger entry in §6.13's book.
  Nothing in it is generic form chrome wearing a deckle.
- **Failure fallback.** A working HTML form: labels, inputs,
  native validation as the floor, submit posts without JS. The
  sheet styling is CSS over real controls; a JS failure leaves
  a plainer form that still orders paper.
- **Reduced-motion variant.** No press scale, no settle, no
  lettering: error notes appear whole, the filed line replaces
  the form instantly, focus rules ink instantly. The order is
  still taken; the press is implied.
- **Breakpoints (v2).** ≥1200px: form at the sheet's measure,
  radio rows two-up. 768–1199px: one column, rows full width.
  <768px: inputs at 17px (also prevents iOS zoom — the theme's
  body size already complies), radio rows ≥52px tall, the
  submit plate full width and ≥52px — on a phone the press is
  a thumb, and the layout admits it.
- **Edge cases & failure modes (v2).** *A paper goes out of
  stock while the form is open:* its radio row takes §6.12's
  stamp and disables; if it was already chosen, the error
  voice says so plainly and keeps every other field's content.
  *Failed send (network):* the order stays written, the plate
  unpresses, and the ledger note beneath reads per §12 ("NOT
  FILED — THE LINE FAILED. YOUR ORDER IS KEPT ABOVE."). Nothing
  the visitor wrote is ever cleared by an error. *Double
  submit:* the pressed state disables the plate until
  resolution. *Quantity in packs vs sheets:* the field accepts
  sheets only and says so; a "packs" toggle is refused (§11) —
  one unit, stated, is the mill's honesty.
- **Accessibility spec (v2).** Every field has a real `<label>`;
  hints are `aria-describedby`, never placeholders (a blank
  ruled line is the invitation). Error notes are linked via
  `aria-describedby` and announced by a polite live region on
  submit failure only. Contrast: labels `--bark-deep` 5.1:1;
  input text sumi 12.4:1; error text `--bark-deep` (the bark
  hue's dark form — full-strength bark at 3.63:1 never letters
  an error). Touch targets: ruled fields have 48px hit rows;
  radio rows ≥48px (52px on mobile).
- **Performance budget & mobile variant.** Transitions on
  focus/submit only; the lettering note is the only timed text
  and is capped at 600ms. Mobile: the thumb-press variant
  above.
- **Tokens consumed (v2).** `--kozo`, `--fibre-shadow`, `--sumi`,
  `--bark`, `--bark-deep`, `--hairline`, `--ease-press`,
  `--ease-settle`, `--ease-wick`, `--press-dur` (180ms).

### 6.15 The unprinted sheet & the next-sheet transition

- **What & why.** The theme's two state-change rituals, sharing
  one material logic. **Loading** shows the unprinted sheet: the
  real sheet markup with its deckle and fibre field present and
  its measures blank — fibre-shadow blocks where print will land
  — resolving as content arrives: the sheet is at the mill,
  made, not yet printed. **Navigation** is the next-sheet
  transition: the current sheet lifts at its deckle (rotateX to
  −10°, 260ms) while the new sheet slides beneath it, and the
  old sheet is laid aside — the §6.4 turn, performed between
  pages instead of between sections.
- **Structure.** Skeleton: the sheet's real DOM with
  `.is-unprinted` — deckle and fibres real, headline measure a
  fibre-shadow block at the headline's true height, text
  measures as ruled blank lines at the body's true line-height,
  plates as fibre-shadow frames at their true aspect. Content
  swap replaces the blanks in place; the sheet never moves or
  resizes. Transition: a page-level stage holding a clone of the
  outgoing sheet's top 160px (its deckle strip) as the lifting
  layer; the incoming page renders beneath it in the same
  viewport; at the lift's peak the route swaps and the layer
  completes its turn and is removed.
- **Motion spec.** Skeleton resolve: as each measure's content
  lands, its blank is replaced and the content prints (§6.2's
  grammar at measure scale: impression offset 1.5px → 0, 300ms
  `--ease-press`). Hard cap: any measure still blank at
  **1200ms** has its blanks stripped entirely (blocks become
  plain `--kozo`) — no sheet may stay abstract if the machinery
  fails; content then arrives plainly. Transition: 520ms total
  `--ease-turn` — 260ms lift, swap at peak coverage, 260ms
  settle of the new sheet (§6.1 at half scale: 1.01 → 1). The
  incoming page arrives *printed* (its §6.2 headlines do not
  re-print after a transition; a turned-to sheet is a finished
  sheet).
- **Choreography timeline (v2).** Transition, t+0 = link
  activation: outgoing deckle begins lifting → t+260ms: lift at
  −10°, new sheet visible beneath, route swaps, scroll to the
  new sheet's top → t+520ms: new sheet settled, lifting layer
  removed, focus moves to the new page's headline (see a11y) →
  t+900ms watchdog: any transition not completed is torn down
  and the destination shown plainly. Skeleton resolve (per
  measure, t+0 = content landed): blank replaced, impression
  settles over 300ms; the sheet's furniture (§6.10) prints last,
  as a hand pencils it after the sheet is done.
- **State matrix (v2).** *Loading:* unprinted measures inside
  real deckles. *Resolving:* 300ms impression per measure.
  *Loaded:* normal sheet behaviour. *Turning:* 520ms, pointer
  locked out. *Hover:* links show §6.10's rule; the transition
  has no hover state. *Focus:* keyboard activation fires the
  same turn; focus lands on the destination headline at t+520.
  *Touch:* identical, 460ms. *Disabled / no-JS:* no unprinted
  states are ever rendered unresolved (server pages ship
  printed); plain navigation, no lift.
- **Content merge.** The skeleton is the sheet's own unprinted
  self — same deckle, same measures, zero layout shift by
  construction. The transition's lifting layer is the outgoing
  page's own deckled edge; the turn is §6.4's act at page scale.
- **Failure fallback.** Skeleton without JS: the shell must not
  render `.is-unprinted` states it cannot resolve — skeletons
  exist only inside client-side fetches that own their 1200ms
  watchdog. Transition without JS or in a plain multi-page
  build: ordinary navigation; the turn decorates links it can
  intercept and never breaks one it can't (middle-click,
  new-tab and modified clicks bypass it entirely). A navigation
  to a slow page holds the lift at peak for up to 3s with the
  furniture line of the destination pencilling in on the lifted
  strip (the mill is fetching the sheet) — then aborts, lays
  the sheet back (200ms), and lets the native load proceed.
- **Reduced-motion variant.** Skeleton: blanks are plain
  `--kozo` blocks (no fibre field inside them), content appears
  at 120ms opacity or plainly. Transition: no lift; instant
  navigation with a 120ms bark rule flash under the new page's
  furniture to mark the change of sheet.
- **Breakpoints (v2).** ≥1200px: full spec. 768–1199px:
  transition 480ms, lift −8°. <768px: transition 460ms, lift
  −7° on the top 120px; skeleton text measures reduce to two
  ruled lines per block.
- **Edge cases & failure modes (v2).** *Same-page anchor
  links:* no transition — anchors scroll (and §6.4's grammar
  governs what they cross). *External links:* no transition.
  *Content that never arrives (fetch error):* the unprinted
  measure resolves into the sheet's error note (§11) in the
  ledger voice (§12) — a sheet apologises in character rather
  than staying blank. *Prefetch:* hovered internal links may
  prefetch; the turn still runs its full 520ms — the ritual is
  the point, not the wait.
- **Accessibility spec (v2).** During a transition the outgoing
  page is `inert` from t+0 and the destination is made live at
  completion with focus moved to its `<h1>` (tabindex=-1) and
  a polite announcement "Turned to: [page name]". Skeletons:
  loading sheets carry `aria-busy="true"` until resolved; the
  stack announces "This sheet is still at the press" once, not
  per measure. The transition is skipped entirely for
  reduced-motion and where the router manages focus itself.
- **Performance budget & mobile variant.** Skeleton blanks are
  CSS/SVG — no image payload. The transition is one transform
  on one strip plus the incoming page's settle. Mobile: the
  460ms variant above.
- **Tokens consumed (v2).** `--kozo`, `--fibre-shadow`, `--sumi`,
  `--bark-deep`, `--ease-turn`, `--ease-press`, `--turn-page`
  (520ms), `--resolve-measure` (300ms), `--fallback-strip`
  (1200ms).

### 6.16 Colophon footer — the maker's mark & the confession

- **What & why.** A handmade sheet ends with its colophon: who
  made this paper, from what bark, in what run — and, in this
  theme, the confession the whole page has been promising: the
  long fibre (§6.5), named, measured, and owned. The footer is
  the last sheet of the stack, deckled at the bottom (§4), and
  it belongs because a mill signs its work the way a printer
  does — with the facts of the making, including the flaw.
- **Structure.** `<footer class="colophon-sheet">`: the branch
  (§6.7) at its head; the colophon text in the caption setting
  (§3): the maker, the paper's name, the bark's source, the
  run's size and date — all real (§1); then the confession line,
  set as its own paragraph: "One fibre in this sheet runs long
  — [N] mm at the reference width — crossing the [second,
  third and fourth] sheets. We left it in." (N and the sheet
  list computed from §6.5's actual span at build); the legal
  line; and one "Further sheets" link (§6.10's grammar) as the
  stack's only onward direction. There are no link columns: a
  colophon is a statement, not a sitemap.
- **Motion spec.** The branch draws (§6.7) as the footer
  enters. The confession line prints (§6.2's grammar at caption
  scale, impression 1px, 300ms) 200ms after the branch
  completes — the flaw is confessed after the plant is grown,
  in the colophon's own order. Nothing else in the footer
  moves, ever; a signature does not animate.
- **Choreography timeline (v2).** t+0: footer at 30% visible →
  branch draws (§6.7, ~1.6s envelope) → t+branch-complete
  +200ms: confession line prints (300ms) → footer at rest,
  permanently.
- **State matrix (v2).** *Rest:* printed colophon — the no-JS
  state (branch drawn, confession printed). *Arriving:* the
  draw + print sequence, touch identical. *Hover / focus:* the
  "Further sheets" link behaves as §6.10's lines. *Active:*
  §6.15's transition onward. *Scrolled-past:* n/a — it is the
  end. *Disabled:* static colophon, complete.
- **Content merge.** The footer's facts are the page's facts:
  the run it names is the edition the visitor has been reading
  (§6.18), the fibre it confesses is the fibre they scrolled
  past (§6.5), the branch it grows is the bark the sheets were
  beaten from. A footer that could be pasted under another site
  has failed this element's test.
- **Failure fallback.** Static branch, static confession. The
  confession is text in the DOM from first paint — JS may
  delay its *printing*, never its presence to AT or to a
  no-JS reader.
- **Reduced-motion variant.** Branch pre-drawn, confession
  pre-printed. The colophon is a plate and a paragraph.
- **Breakpoints (v2).** ≥1200px: branch left, text right at
  the sheet's measure. 768–1199px: branch above text (§6.7).
  <768px: single column; the confession line is never
  truncated or folded into a details element — on a phone the
  confession takes the room it needs, because it is the point.
- **Edge cases & failure modes (v2).** *The fibre's span
  changed in a rebuild:* the confession's numbers are
  generated from §6.5's span data at build; a hand-edited
  confession that disagrees with the span is a gate failure
  (§10, dataset unity). *A page with no long fibre* (the one
  licensed exception: a single-sheet page, §6.5): the
  confession line is replaced by the true statement "This
  sheet is a single sheet; it carries no long fibre." — the
  colophon confesses absences too, or it is not a colophon.
- **Accessibility spec (v2).** The footer is a real `<footer>`
  with its text in reading order; the branch is `aria-hidden`
  (§6.7). The confession is ordinary text — its emphasis is
  typographic (its own paragraph), never colour alone.
- **Performance budget & mobile variant.** One draw (§6.7) +
  one 300ms print, once per page. Mobile: the single-column
  variant above.
- **Tokens consumed (v2).** `--kozo`, `--sumi`, `--bark`,
  `--leaf`, `--ease-press`, `--ease-wick`.

### 6.17 The offcut — the 404 & empty sheet

- **What & why.** A wrong address in this theme is an offcut:
  the trimmed remainder of a sheet, too small for the edition,
  kept in the mill's offcut bin. The 404 page is an offcut
  sheet — real paper, wrong size — and empty states are
  unprinted sheets (§6.15) with the mill's note pencilled on
  them. It belongs because even the waste in a mill is paper,
  and because an honest offcut ("this was cut from a sheet that
  exists") is the theme's way of saying *nearly* without
  inventing a destination.
- **Structure.** One small sheet (62% of the stack's measure,
  deckled on all four edges — an offcut is torn from every
  side): the requested path set as the sheet's address line in
  Mincho, ruled through once in `--bark-deep` (the mill hand's
  pencil: *not this*), beneath it two or three lines in the
  empty voice (§12) and the thread link back to the stack's
  first sheet. Where a near match is real (slug similarity
  computed server-side), one further line: "CUT FROM THE SAME
  SHEET: [sheet name]" with its link. Empty states reuse the
  sheet at section scale with the note and, where the
  emptiness has a next date, the date (§12).
- **Motion spec.** One motion only: on load, the pencil rule
  through the address line draws (scaleX, 300ms `--ease-wick`)
  at t+250ms — the hand ruling it out as the visitor arrives.
  No deckle theatrics; an offcut's ceremony is its smallness.
- **Choreography timeline (v2).** t+0: offcut painted, rule
  parked → t+250ms: rule draws 300ms → t+550ms: the sheet is
  still thereafter, permanently.
- **State matrix (v2).** *Rest:* ruled, still — and the no-JS
  state has the rule pre-drawn. *Hover / focus:* the home
  link's rule (§6.10). *Active:* §6.15's transition home.
  *Scrolled-past:* n/a (one small sheet). *Touch:* identical.
  *Disabled:* static offcut with its link.
- **Content merge.** The ruled address is the actual requested
  path; the near-match line exists only when the match is
  real. Nothing decorative is added — no illustration of a
  lost sheet, no mascot (§9).
- **Failure fallback.** It is a static sheet with a link;
  there is nothing to fail.
- **Reduced-motion variant.** Rule pre-drawn.
- **Breakpoints (v2).** All sizes: the offcut takes 62% of the
  measure (84% under 768px — a phone offcut is most of a small
  sheet), centred in the stack's column.
- **Edge cases & failure modes (v2).** *A path that matches a
  retired sheet:* the colophon voice names it ("This sheet was
  in the [year] run; the run is finished.") with a link to the
  current sheet that replaced it — only when the replacement
  is real. *Empty search:* the section-scale offcut states the
  query back and the range it was searched in; it does not
  suggest popular sheets it cannot relate to the query.
- **Accessibility spec (v2).** The page's `<h1>` is the empty
  voice's line ("This address is an offcut"), not the path —
  screen readers meet the meaning first. The ruled path is
  wrapped so it reads as "address attempted:" + path, the rule
  presentational. A real 404 status is returned; the offcut is
  a presentation of an error, never a soft-404.
- **Performance budget & mobile variant.** One 300ms draw.
  Mobile: the 84% variant above.
- **Tokens consumed (v2).** `--kozo`, `--sumi`, `--bark-deep`,
  `--ease-wick`, `--rule-draw` (300ms).

### 6.18 Ink numerals — counters that count the mill's records

- **What & why.** The page's figures — sheets in the run,
  grammage, edition size, copies remaining — count up in ink
  numerals as their sheets arrive: tabular Mincho-adjacent
  figures (Zen Kaku tabular, §3) that rise like a hand tallying
  in the ledger. It belongs because counting in this theme is a
  record being made, and because §1's law needs its figures to
  behave like records: they count *between two true values*
  (the previous run's figure and this run's, or zero and the
  count) and land on the true one, audibly final.
- **Structure.** Any figure may carry `data-count` with its
  true final value in the DOM as its text content (the no-JS
  and AT state is the final figure, always). JS, on the
  figure's sheet entering at 40% visibility, replays the count:
  integers in whole steps, grammages in 1 g/m² steps, edition
  remainders counting *down* where the figure is a remainder
  (a remainder that counts up is a lie about scarcity, §9).
  Duration is proportional: 600ms + 12ms per step, capped at
  1400ms; easing `--ease-wick` applied to the step timing (ink
  arrives faster at first, then settles — the hand slows as it
  nears the true number, checking itself).
- **Motion spec.** Trigger: sheet entry, once per figure,
  never re-fired on scroll-back (a tallied figure is not
  un-tallied). Steps are whole increments written as text
  (tabular, width-stable); no decimal shimmer, no blur, no
  rolling digits — a ledger figure is written digit by digit
  only in the sense that its value changes in steps a hand
  could write. The final step lands with a 120ms hold before
  the figure is marked counted (a class AT never sees) — the
  hand's pause after the last digit.
- **Choreography timeline (v2).** t+0: figure's sheet at 40%
  → t+0–600ms+: steps run, interval shrinking per `--ease-wick`
  → final step → 120ms hold → figure at rest, permanently.
  Multiple figures on one sheet stagger 90ms in reading order
  (the hand tallies down the page, not across it randomly).
- **State matrix (v2).** *Rest:* final figure — the DOM, no-JS
  and post-count state. *Counting:* stepped replay, ≤1400ms;
  touch identical. *Hover / focus:* none — figures do not
  perform. *Scrolled-past:* counted figures stay counted;
  figures whose sheets were jumped past (anchor) are set to
  final instantly. *Disabled:* JS off = final figures, which
  is why the DOM ships them.
- **Content merge.** The figures are the sheets' own measures
  (§6.10's furniture, §6.12's cards, §6.16's run size) — one
  dataset (§10 unity gate), counted where it is printed. A
  figure with no true final value does not count; it is not
  printed at all (§1).
- **Failure fallback.** Final figures are the DOM default; a
  stalled count is snapped to final by a watchdog at
  duration + 400ms. There is no state in which a reader is
  left watching a wrong number rest.
- **Reduced-motion variant.** No counting. Figures stand at
  their true values — the ledger already tallied, which is
  what the printed sheet always shows.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px:
  duration cap 1200ms. <768px: duration cap 1000ms and figures
  below the fold count only on entry (never pre-counted during
  a fast thumb scroll past three sheets — those land final).
- **Edge cases & failure modes (v2).** *A figure updates
  mid-session (stock falls):* it re-tallies from the old true
  value to the new true value over 500ms — a correction, in
  the open, like everything else in this theme (§6.3's ethic
  at figure scale). *Huge counts (an edition of 40,000):*
  steps are grouped (the hand tallies in 100s, stated in the
  step pattern: increments of 100 inside the same duration
  cap) — grouping is declared in the build, never silent.
  *Zero:* a true zero prints as "0" and does not count; the
  mill does not perform the arrival of nothing.
- **Accessibility spec (v2).** The figure's final value is in
  the accessibility tree from first paint; the counting
  element is `aria-hidden` during its ≤1400ms replay with a
  visually-hidden twin holding the final value — or, simpler
  and preferred: the count runs only on the visual layer and
  the element's `aria-label` carries the final figure
  throughout. No live region announces a tally; a number
  changing is not news.
- **Performance budget & mobile variant.** Text writes only,
  ≤6 figures counting concurrently, each write width-stable
  (tabular) so no layout follows. Mobile: the capped variant
  above.
- **Tokens consumed (v2).** `--sumi`, `--ease-wick`,
  `--count-base` (600ms), `--count-step` (12ms),
  `--count-cap` (1400ms).

## 7. Page application map

- **Home (the sample stack).** The full stack on one page:
  first sheet (§6.11) → two or three content sheets (§6.4 turns
  between them, the long fibre crossing sheets 2–4, §6.5) → the
  range as sample cards (§6.12) → the grammage ledger (§6.13) →
  the order sheet (§6.14) → colophon with branch and confession
  (§6.16, §6.7). The ink strip rides the whole stack (§6.6).
  This is the reference build; every other page type is a
  contraction of it.
- **Listing (the sample book).** A stack of plates: running head
  (§6.10), a short first sheet naming the range, sample cards
  (§6.12) in mixed spans — one card per paper, its figure line
  carrying grammage and batch state — then the ledger (§6.13)
  and the colophon. No page-turn pins beyond two (the range is
  the list; turning every card's sheet would tax the hand).
- **Detail (one sheet, examined).** A single paper held to the
  light: hero sheet naming it, its fibre field enlarged (the
  §4 field at 1.4× scale as the sheet's ground — the detail
  page is where fibres are looked *at*, not just under), its
  ledger row expanded into prose and figures, its plates, and
  the order sheet (§6.14) pre-set to this paper. The long fibre
  appears if this sheet is within its span (§6.5) — the detail
  page does not summon the flaw; it inherits it or it doesn't.
- **About (the mill).** Sheets for the mill's method, told as
  making: each stage a sheet (bark, beating, mould, press,
  drying), its figure line carrying the stage's real measures
  (beating time, sheet count per day — a figure is a figure,
  §1). The colophon carries the mill's own branch and the
  confession of *this* page's fibre.
- **Contact / order (the order sheet).** §6.14 is the page: a
  short first sheet, the order sheet in the second, the
  colophon as footer. No cards, no ledger — a visitor who has
  arrived to order has finished browsing the sample book.
- **404 / empty.** The offcut (§6.17), at page scale or section
  scale respectively.
- **Print.** The stack prints as sheets: deckles as printed
  edges, fibres at `--fibre-line` rest strength, the long fibre
  present (it is in the paper), all figures printed at final
  values, the ink strip omitted (a printed stack has no reading
  left to record). A Paper Mulberry page that prints badly has
  failed at being paper.

## 8. Worked examples

### 8.1 The hero — a washi mill's first sheet

A kozo paper mill's home stack opens. The furniture reads
"SHEET 1 OF 7 · KOZO, LONG FIBRE · 128 G/M²". The headline,
Shippori Mincho 700 at 56px: "Paper from the mulberry, beaten
by hand" — with `data-misprint` on *mulberry*, the material the
mill most wants read twice. The standfirst: "Kozo bark,
steamed, stripped and beaten in the winter water — the sheet
your hand already knows how to hold." The figure line: "128
G/M² · 640 × 970 MM · WINTER RUN OF 900 SHEETS". The plate: the
sheet held against the light, fibres visible, alt text saying
exactly that (§6.11).

Timeline: t+0 the sheet paints complete — a no-JS visitor reads
this exact hero. With JS: t+60ms the sheet begins its settle
(§6.1), scale 1.02 → 1 over 900ms, the shadow band crossing
behind the print; t+500ms the headline's first line prints
(§6.2), impression 2px relaxing over 420ms, lines following at
140ms; the second line carries *mulberry* — as it settles, its
ghost arms at +3px / 40%, holds the 260ms honesty beat, then
registers over 700ms into one clean impression (§6.3); the
headline complete, the plate settles 1.05 → 1 (§6.12). By
t+~2100ms the first sheet is still, printed, and honest about
having been wrong for one beat. The visitor scrolls; the ink
strip (§6.6) takes its first wick of ink.

### 8.2 Mid-page — the range, thumbed like a sample book

Sheet 4 is the range. Its furniture: "SHEET 4 OF 7 · THE RANGE
· FIVE PAPERS". Five sample cards (§6.12) in mixed spans — the
heavyweight first (its plate is the sheet at raking light, the
fibres standing in relief), then two mid-weights, then the
tissue. As the sheet turns in (§6.4 — curl −18° at its deckle,
the previous sheet's edge lifting as this one slides beneath),
the cards are laid in reading order, 90ms apart, each settling
380ms; their plates settle as they cross the centre. The
visitor hovers the tissue's card: its corner curls 34px (§6.8),
the underside showing — kozo-deep, the colour of the sheet's
other side. Its figure line reads "32 G/M² · BATCH OF [MONTH]
IN THE VAT" — no stamp, because the batch is real and current.
The card beside it, the winter kozo, is stamped "THIS BATCH IS
GONE — THE NEXT IS BEATEN IN FEBRUARY" (§6.12's disabled
state): its curl is halved, its link is gone, its sample
remains. The visitor presses the heavyweight's card (§6.9) —
inset shadow deepening at its deckle — and the sheet turns to
its detail (§7).

### 8.3 Conversion — an order, pressed

The last sheet carries the order sheet (§6.14): "Order sheets
— or ask for the sample pack first." The visitor writes their
name on the first ruled line (the rule inks to `--bark-deep`,
the fibre-shadow plate sliding beneath), chooses the winter
kozo from the radio rows — each row a small sheet with its
figures; the chosen row takes the impression and holds its
bark rule — and enters 50 in the quantity field, whose label
has already told them the unit: "Quantity — in sheets (packs
of 25)". They mistype the email without its ending; on submit,
that field's rule barks and the mill's hand letters beneath:
"THE ADDRESS ENDS MID-WORD — THE MILL'S PARCELS GO BY POST AND
MUST BE COMPLETE." (§12). They fix it; the note clears. They
press "Press this order": the plate dips, holds while the
order crosses, and the form settles 4px into the stack as the
filed line replaces it: "FILED AS ORDER NO. 214 — 50 SHEETS OF
WINTER KOZO. THE MILL WILL WRITE BEFORE THE BARK IS STRIPPED."
The number is the server's sequence; had the same name and
paper been filed before, the line would read "ALREADY FILED
AS ORDER NO. 198" — the mill keeps one open order per hand,
and says so.

## 9. Anti-slop — what makes THIS theme look cheap

1. **A paper texture from a stock site.** A photographed
   crumple tiled behind the content. The sheet here is colour,
   deckle geometry and a generated fibre field (§4); the moment
   a photo carries the paper, the mill is a screensaver. Cure:
   paper is built, never photographed — photographs appear only
   as plates *on* the sheet (§6.12).
2. **Invented grammages.** "120 g/m²" typed because the spec
   table looked thin. This is the one law broken (§1) — the
   theme's capital crime. Cure: figures trace to the mill's
   records or the cell carries a dash with its reason (§6.13).
3. **A fade-in headline.** The press does not fade. Cure: §6.2's
   impression, or the headline simply stands printed.
4. **The misprint as a glitch effect.** RGB splits, jitter,
   distortion — screen damage dressed as print character. Cure:
   §6.3's single ghost at +3px, in ink, registering once. A
   misprint is a second impression, not a malfunction.
5. **Deckles everywhere.** Torn edges on buttons, inputs,
   images, the cursor's feelings. The deckle belongs to sheets
   and their cards (§4, §6.12); a torn button is a costume
   slipping. Cure: chrome inside a sheet is ruled, flat and
   honest (§11).
6. **Fibres crossing text at full strength.** The field left to
   wander behind paragraphs until reading is archaeology. Cure:
   §4's clearance fade, baked into the generated paths; the
   gate samples it.
7. **Percentages and progress bars.** "62% through the stack" —
   the theme measures in ink and sheet counts. Cure: §6.6's
   strip and §6.10's furniture are the only progress; grep for
   "%" in progress contexts.
8. **A dozen flaws.** A misprint, a long fibre, a crooked
   sheet, a coffee ring, a thumbprint — a theme park of
   accidents. Real paper has one or two, owned. Cure: exactly
   one misprint (§6.3), exactly one long fibre (§6.5), and the
   colophon confesses both. A third declared flaw is a gate
   failure.
9. **Leaf green as a brand wash.** Whole sections in mulberry
   green because the branch was pretty. Cure: leaf is rationed
   (§2: ~2%, one element per sheet) — it is the plant, not the
   paper.
10. **The turn as a page-flip plug-in.** A skeuomorphic book
    widget with curling page corners and soundless whooshes,
    applied to content that is not sheets. Cure: §6.4 turns the
    sheet's own deckle by 18° at its own boundary — the
    smallest turn that is true.
11. **Counters counting nothing.** Edition numbers animating
    to invented totals for the pleasure of motion. Cure:
    §6.18 counts only between true values, from the DOM's
    printed final figure.
12. **Uniform card grids.** Nine identical samples in a 3×3
    lattice. Sample books vary; so do the cards (§6.12's mixed
    spans). A lattice is a spreadsheet wearing a deckle.

## 10. Quality gate

**Blocking — a build failing any of these may not ship:**

1. **Figure audit.** Every grammage, dimension, count and date
   on the page traces to the mill's records or the publisher's
   stated data. Sampled by hand against the source; an invented
   figure fails the build, not just the element.
2. **Flaw ration.** Exactly one `data-misprint` word per page;
   exactly one long fibre, spanning ≥2 sections (≥3 at desktop
   reference width); the colophon's confession (§6.16) matches
   the fibre's measured span and the misprint's existence.
3. **Fibre clearance.** No background fibre at full strength
   passes behind a text block (checked by scripted screenshot
   sampling at 5 scroll depths per sheet); the long fibre never
   exceeds its 55% cap where it crosses text.
4. **No-JS completeness.** With JavaScript disabled: every
   sheet flat and readable, headline printed and clean, branch
   drawn, all figures at final values, the form submittable,
   the colophon complete including its confession.
5. **Reduced-motion completeness.** With
   `prefers-reduced-motion`: no settle, no turns, no sway, no
   counts, no draws; every content item reachable and readable;
   the misprint never arms.
6. **Contrast.** Body text sumi on kozo (12.4:1) or the night
   scheme's pairing (11.9:1) only; labels/captions
   `--bark-deep` (5.1:1) minimum; no text ever set in `--bark`
   (3.63:1) or `--fibre-shadow` (1.24:1) — grep + visual pass.
7. **Dataset unity.** Furniture (§6.10), cards (§6.12), ledger
   (§6.13), order rows (§6.14) and counters (§6.18) render
   from one dataset — verified by changing one paper's
   grammage in the data and confirming every view follows.
8. **Turn discipline.** ≤4 pinned boundaries per page (≤2 on
   mobile), ≤2 ambient loops page-wide (§5), the 800ms
   snap-flat law (§6.4) verified by stalling the loop by hand.

**Standard — checked every build:**

9. Shippori Mincho prints headlines only; Zen Kaku Gothic New
   keeps records (§3 law 1).
10. Stagger orders are real orders (press, growth, reading).
11. The settle, print, registration and counts never re-fire
    on scroll-back.
12. Print stylesheet produces the finished stack (§7).
13. The offcut returns a real 404 and names retired sheets
    only when their replacements are real.
14. Watchdogs verified: 800ms turn snap, 1200ms skeleton
    strip, 1400ms headline snap, 1500ms ghost deletion.

## 11. Component inventory

Every component a real site in this theme needs, with its
treatment. Components the theme refuses are named with their
in-world replacement — a refusal without a replacement is a
gap, not a style.

| Component | Treatment in this theme |
|---|---|
| Primary button | The press plate (§6.14): ruled, lettered in the apparatus setting, presses with §6.9's impression at form scale. One per sheet. |
| Secondary button / link | Text link with the drawn rule (§6.10): sumi, rule draws on hover/focus in 180ms `--ease-press`. |
| Text input | Ruled-line field (§6.14): transparent ground, 2px bottom rule, bark-deep focus plate. Never a boxed input — an order sheet has lines, not boxes. |
| Select | **Refused.** Choices of paper are radio rows from the dataset (§6.14); choices of sheet are furniture items (§6.10). A dropdown hides the paper it names. |
| Radio / checkbox | Radio: the paper rows (§6.14) — small sheets that take the impression when chosen. Checkbox: a mill tick-box, a drawn square that takes a hand tick stroke (draws 160ms) when checked. |
| Stepper | The sheet tally (§6.14's quantity grammar): minus/plus as real buttons, the count in tabular figures with its unit ("50 SHEETS"). |
| Table | The grammage ledger (§6.13). |
| Badge / tag | **Refused** as chrome. A paper's state is its figure-line stamp ("THIS BATCH IS GONE", §6.12) or its ledger ruling (§6.13). Pills are not mill furniture. |
| Alert / notice | The mill's note: an apparatus line in the sheet's furniture or at its head, sumi on `--fibre-shadow`, prefixed by its subject ("THE VAT: THE WINTER BATCH IS BEATEN IN FEBRUARY"). Set at build/publish time; never animated in. A blocking alert takes the ledger voice and a double bark rule — still not a coloured banner. |
| Toast | **Refused.** Confirmations are filed lines (§6.14) or colophon records — things that persist where they were made. Nothing at a mill evaporates in 4 seconds. |
| Modal | **Refused.** Detail is a sheet (§7) or a card's own expansion in its sheet. Paper is not covered by its own UI. |
| Tooltip | **Refused.** A paper's detail is its sheet; a symbol's meaning is its furniture line. Hover gives the curl (§6.8), never a floating label. |
| Tabs | **Refused.** Sheets succeed one another (§6.4, §6.15). Parallel hidden panels are unprinted sheets pretending to be printed. |
| Accordion | The batch list (§6.17's grammar at section scale): a batch's detail unfolds downward in its sheet, its deckle shadow deepening as it opens, 300ms `--ease-settle`. One open at a time per sheet. |
| Pagination | Sheet succession: "SHEET 3 OF 7 — THE NEXT SHEET: THE RANGE" as a furniture item at the sheet's foot (§6.10 grammar). Numbered page pills refused. |
| Breadcrumbs | The stack so far, in order, as text ("FIRST SHEET › THE MAKING › —") in the furniture. Only on detail sheets (§7). |
| Progress | The ink strip (§6.6). Progress bars and percentages refused (§9.7). |
| Search | The sheet index: a ruled field (§6.14 grammar) whose results are §6.12 cards; no results is §6.17's offcut at section scale. |
| Card | The sheet sample card (§6.12). |
| Form errors | Ledger-voice notes under barked rules (§6.14, §12). |
| Loading | The unprinted sheet (§6.15). Spinners refused — the mill has no spinning part; the press comes down, it does not rotate. |
| 404 / empty | The offcut (§6.17). |

## 12. Content & copywriting voice

The voice is the mill hand's: plain, measured, exact about
figures and dry about everything else. Two registers — the
**sheet** (headlines, names, the printed word) and the
**ledger** (prose, notes, confirmations) — and the figure
discipline that governs both:

> **Every figure carries its unit and its source.** Grammages
> in g/m², dimensions in mm, counts with their noun ("900
> SHEETS"), dates with their month named. Where a figure comes
> from the mill book, the ledger (§6.13) says which month's
> book. An approximation is stated as a figure with its
> tolerance ("ABOUT 190 MM, BY THE HAND — HANDMADE SHEETS
> VARY") or not stated.

**Headline style.** Shippori Mincho names the paper, the
making, the place — ≤8 words, no verbs of marketing. ✓ "Paper
from the mulberry, beaten by hand" · ✓ "The winter run" ·
✗ "Discover Our Amazing Artisan Paper Journey!" — the sheet
does not exclaim; there are no exclamation marks anywhere on
the page, in any register.

**Label style.** Apparatus caps, short, factual. ✓ "SHEET 3
OF 7" · ✓ "KOZO, LONG FIBRE" · ✗ "Don't miss this batch!" ·
✗ "Limited edition!!" — scarcity, when real, is a figure in
the ledger ("THE RUN IS 900 SHEETS — 214 REMAIN"), never an
adjective.

**Figure style.** ✓ "128 G/M² · 640 × 970 MM" · ✗ "Nice
thick paper" · ✗ "approx. 130-ish gsm" — approximation is a
figure with its tolerance, or silence.

**Error voice (the ledger corrects).** Plain, specific, in
`--bark-deep`. ✓ "THE ADDRESS ENDS MID-WORD — THE MILL'S
PARCELS GO BY POST AND MUST BE COMPLETE." · ✓ "NO PAPER IS
CHOSEN — THE ORDER MUST NAME ITS SHEET." · ✗ "Oops! Something
went wrong 😢" — no oops, no emoji, no vagueness: the note
names the field, the fault, and what to do.

**Empty-state voice.** ✓ "NO SHEETS IN THIS BATCH — THE BARK
IS STILL ON THE TREE. THE NEXT BEATING IS IN FEBRUARY." ·
✗ "Nothing here yet — check back soon!" The offcut states its
reason and its next date, or says it does not know (§6.17).

**Confirmation voice.** ✓ "FILED AS ORDER NO. 214 — THE MILL
WILL WRITE BEFORE THE BARK IS STRIPPED." A confirmation is a
record with a number and a next act with a date. ✗ "Awesome!
Order placed!" — the ledger does not cheer.

**Banned words:** amazing, discover (as an imperative),
artisan™, oops, awesome, journey (as a metaphor for a
purchase), "don't miss", gsm (the sheet prints G/M²).
**Owned words:** beaten, stripped, laid, filed, pressed, the
run, the batch, by hand, in the mill book.

## 13. Full-page scroll choreography map

The home stack (§7), top to colophon. Every beat in order;
"sees" is the visitor's experience, "feels" is the intended
register.

| # | Beat | The visitor sees | Feels |
|---|---|---|---|
| 1 | Load | The first sheet settles; its headline prints; one word registers (§8.1) | Paper arriving in the hand |
| 2 | First reading | The ink strip takes its first wick; the furniture marks SHEET 1 | Being recorded as a reader |
| 3 | First turn | Sheet 1's deckle curls −18°; sheet 2 slides beneath (§6.4) | Turning a real sheet |
| 4 | The making | Sheets of process; figures tally as they arrive (§6.18) | The material earning its claims |
| 5 | The long fibre | Somewhere in sheets 2–4, one fibre runs longer and darker, swaying almost not at all (§6.5) | A flaw, noticed quietly |
| 6 | The range | Cards laid in order; a corner curls under the pointer; one batch is stamped gone (§8.2) | Thumbing a sample book |
| 7 | The ledger | The range again as records; the current row's rule draws (§6.13) | Being handed the means to check |
| 8 | The order sheet | Ruled lines ink under the hand; a paper row takes the impression (§8.3) | Writing to the mill |
| 9 | The filing | The form settles into the stack; a numbered line replaces it (§6.14) | Commitment, recorded |
| 10 | The colophon | The branch grows; the confession prints beneath it (§6.16) | The maker signing — and owning the flaw |

**Reverse pass.** Scrolling up: turns and the ink strip's
*label* retrace (they are functions of position or current
information); the settle, prints, registration, draws, tallies
and filings never un-happen (they are records). The ink fill
itself never retreats — ink does not un-wick (§6.6).

**Jump-scroll catch-up.** Anchor jumps and restored scroll
positions settle every scrubbed value to its mapped state on
the first frame, and every one-shot record for sheets above
the landing point to its completed state — the reader arrives
at a stack already turned, printed and tallied up to where
they stand.

## 14. Whole-page performance budget

**Asset budget (home stack).** HTML + CSS + JS ≤ 200KB
gzipped total; fonts: Shippori Mincho (2 weights, subset to
Latin + figures + the page's Japanese glyphs where used) +
Zen Kaku Gothic New (3 weights, subset) ≤ 110KB woff2;
images: plates only, ≤120KB the hero's, ≤60KB each card's,
≤6 per page, responsive + lazy below the first sheet. **Zero
image assets for paper** — deckles and fibre fields are inline
SVG generated at build time (≤40 paths per sheet, ≤7 sheets ≈
22KB of path data in the HTML, gzip-friendly repeated
geometry).

**Animation frame budget.** The one shared rAF loop (lerp
0.12) writes, per frame, at most: 2 boundary curls (§6.4), 1
fibre-layer transform (§6.5), 1 ink-strip height (§6.6), 1
curl spring (§6.8), 6 figure text writes (§6.18) — ≈ 11 style
writes, all compositor-friendly except the figure text
(tabular, width-stable). Long tasks: none over 50ms; path
generation and dataset rendering happen at build time, never
in the browser. The loop sleeps when the tab is hidden and
when no watched boundary is in band.

**Cut order when the budget is exceeded** (cut in this order,
never skip ahead):
1. The grain shadow play (§6.5) — the second ambient loop goes
   first.
2. The long fibre's sway (§6.5) — the fibre remains, still.
3. Card plate settles (§6.12) — plates stand flat; cards still
   lay down.
4. The shadow band of the settle (§6.1) — the scale remains.
5. Figure counts (§6.18) — figures print directly.
6. Boundary pins (§6.4) — turns remain, unpinned.

**Never cut:** the page-turn curl (§6.4), the misprint
registration (§6.3), the ink strip (§6.6), the branch draw
(§6.7), any fallback or watchdog, any reduced-motion variant.
If the budget still fails after step 6, the build reduces
sheets per page (the stack splits, §4) — it does not cut the
never-cut list.

## 15. Build-order checklist

1. **Dataset first.** Papers, grammages, dimensions, run
   sizes, batch states, the misprint word, the fibre's span —
   one source file. Nothing renders before the data is true
   (§1).
2. **The static stack.** Full page with JS disabled as the
   target: sheets flat, headline printed and clean, branch
   drawn, figures final, form native, colophon complete.
   This is the fallback and the print view in one.
3. **Deckle & fibre generation.** Build-time path generators
   (seeded per sheet) with §4's clearance enforced
   geometrically; the long fibre's span generated from
   `data-fibre-span` sections; verify clearance by the §10
   scripted sampling.
4. **Furniture & running head** (§6.10) from the dataset.
5. **The shared loop.** One rAF loop, lerp 0.12, watch-band
   logic, stall rule. No element ships its own loop.
6. **The opening.** Settle (§6.1), headline print (§6.2),
   misprint (§6.3) — sequenced, watchdogged, exactly-once
   semantics verified.
7. **The turns.** Boundary curls + brief pins (§6.4) with the
   800ms snap-flat law; then the mobile reduced variant.
8. **Progress & records.** Ink strip (§6.6) with its
   high-water law; ink numerals (§6.18) from the DOM's final
   figures.
9. **The range.** Cards (§6.12) with curl (§6.8) and
   impression (§6.9); the ledger (§6.13) from the same
   dataset.
10. **The order sheet.** Form (§6.14) with native-first
    submission, error voice, filing-number handling,
    duplicate rule.
11. **State rituals.** Unprinted skeleton + next-sheet
    transition (§6.15) with all watchdogs; offcut (§6.17).
12. **Colophon.** Branch (§6.7) + confession (§6.16)
    generated from the fibre's real span; night scheme check
    (the colophon reads identically in both schemes).
13. **Reduced-motion pass.** Every element's variant verified
    against §6's specs, one by one.
14. **The gate.** §10 run — figure audit, flaw ration and
    dataset-unity test last, signed by a non-builder.
