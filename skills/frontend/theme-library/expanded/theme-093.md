# 93. Marginalia — Expanded (v1 + v2)

A site built inside someone's diary. The main text is set like printed entries —
calm, composed, already decided — but the real story lives in the margins:
handwritten corrections, crossed-out confessions, coffee rings and pressed
flowers. The visitor does not read a finished life; they read a life being
revised in real time, by a hand that is always one thought behind the print.

This expansion deepens the original entry without redesigning it: same diary,
same five palette anchors, same two typefaces (EB Garamond for the print,
Caveat for the hand), all ten original signature elements carried to full
build depth, plus eight page-family elements (opening entry, margin
navigation, entry cards, pressed-flower dividers, the margin-letter form, the
page-turn transition, the tally leaf footer, the torn-page 404) — **18
elements** in total, each with a complete v1 build spec and the full v2
deepening layers.

**The theme's one law: the hand annotates, the print carries — and the strike
never deletes.** Every word that matters ships in the printed layer, complete
and legible, before any hand touches the page. Handwriting may correct,
circle, underline and confess over the print, but it is never the only copy of
anything; and a struck word stays faintly legible forever (its printed
opacity never falls below 0.38), because in this diary a revision is shown,
not hidden. Any build in which a note, a strike or a circle is load-bearing
for comprehension has broken the law and fails the gate in §10.

---

## 1. Concept & world

### The world

The page is a leaf from a kept diary — ruled paper, a wide right margin
reserved for handwriting, entries dated and set in a serif that behaves like
letterpress. The diary's keeper is present only as a hand: red pencil for
editing, ballpoint blue for afterthoughts and dates, pencil-grey for the
bookkeeping tallies. The keeper has opinions about their own text. They
circle the phrase that turned out to be true, strike the sentence that was a
lie they told themselves, and write the honest version larger beside it. A
coffee ring at the corner says the book was lived in before the visitor
arrived, and is still being lived in while they read.

The emotional register is intimacy with a delay. Print is the public self —
composed, punctuated, safe. The margin is the private self — fragmentary,
present-tense, a beat late. Every device in the theme serves that gap: notes
arrive ~600ms after the paragraph they annotate, as if the thought occurred
while reading; corrections bleed rather than swap, because changing your
mind about your own life is a material act, not an opacity change.

### Best-fit sites and audiences

- **Memoirists and authors** — a book site where the excerpts carry the
  author's own later corrections; the margin is where the memoir continues.
- **Journaling and diary apps** — the product's own metaphor made literal:
  printed structure (prompts, dates, streaks) annotated by a living hand.
- **Literary magazines** — essays and poems with an editor's margin: the
  issue's pieces annotated across the issue by one recurring hand, giving a
  magazine a single recognisable reader-in-residence.
- **Wedding-story sites** — the couple's printed story (how we met, the
  proposal) corrected in two hands in the margin; the corrections are the
  romance.
- **Personal blogs with a long memory** — old posts re-read and annotated by
  their older author; the margin is the years between.

### When NOT to use it

- **Anything transactional at speed.** Checkout, booking and dashboards need
  the hand gone; a form that behaves like a diary entry will cost
  conversions and trust. (The one form the theme licenses, §6.15, is a
  letter, not a checkout.)
- **Reference content people search within.** Documentation, specs and
  support articles must be scannable and stable; a margin that performs
  thoughts is noise over a lookup task.
- **Multi-author or anonymous content.** The margin is one person's hand.
  The moment two unlabelled hands annotate, or a brand team fakes one, the
  theme becomes a costume — see the anti-slop list, §9.4.
- **Legally or medically precise text.** Corrections that bleed and strikes
  that stay legible are a literary device; over terms, dosages or safety
  instructions they read as doubt about the facts themselves.
- **Very long reference pages.** The diary leaf has a natural length (see
  §4 density rules); a 9,000-word page breaks the fiction of a leaf and the
  margin's stamina with it.

### The keeper's three inks (a world rule the build must honour)

- **Red pencil (#7A1F1F) edits.** Circles, strikes, underlines, corrections
  to the keeper's own claims. Red never decorates; every red mark is an act
  of revision with a target.
- **Ballpoint blue (#33526B) adds.** Dates, afterthoughts, factual margin
  notes, the second thoughts that are information rather than judgement.
- **Pencil (ink black at reduced strength, §2) counts.** Tallies, check-offs,
  the bookkeeping of the diary: days kept, words revised. Pencil never
  argues; it only records.

A build that lets red write a date, or blue strike a sentence, has not
understood the world. The gate checks it (§10, check 9).

---

## 2. Palette

Five anchors from the original entry, unchanged. Seven derived tokens, each
a stated blend or shade of an anchor — no colour enters the theme from
outside the diary's desk.

| Token | Hex | Role | Usage ratio | Notes |
|---|---|---|---|---|
| `--paper` | `#F5EFE2` | Diary paper — the leaf itself | ~62% | The ground of every page. Never used as text. |
| `--ink` | `#2B2620` | Faded ink black — printed entries, body text | ~22% | Contrast on `--paper` **13.08:1** (measured). The print's voice. |
| `--red` | `#7A1F1F` | Editor's red pencil — edits only | ~4% | On paper **8.97:1**. Strikes, circles, underlines, corrections. Never a background, never a button fill. |
| `--blue` | `#33526B` | Ballpoint blue — additions, dates, links | ~6% | On paper **7.16:1**. The only colour a link may wear. |
| `--tape` | `#B99B5F` | Aged tape — photo corners, pasted slips | ~3% | On paper only **2.32:1** — tape is a material, never text and never a text ground. Ink on tape is 5.65:1 and permitted for the short label printed *on* a tape strip (§6.14). |
| `--paper-deep` | `#E9DFC8` | Page edge, leaf shadow side, the desk showing at the gutter | ~2% | Derived: paper darkened one step. Used for the leaf's thickness and the torn stub (§6.18). |
| `--paper-lamp` | `#EFE3CB` | Lamplight paper — the dark-mode leaf | replaces `--paper` | Ink on it **11.79:1**, red **8.09:1**, blue **6.45:1** — all still pass for their roles. |
| `--rule-line` | `#D9CCA9` | The ruled lines of the leaf | hairlines | Derived from tape, lightened. Lines are printed, not borders: 1px, always under text, never boxed. |
| `--pencil` | `#5C554B` | Pencil graphite — tallies, check-offs, skeleton script | ~1% | On paper **6.42:1**. A grey mixed from ink and paper; tallies and ticks only, never body text (it is the weakest legible voice on the page and is rationed to numerals and marks). |
| `--tape-deep` | `#8A7A52` | Tape in shadow, tape edge, pressed-flower stem tone | <1% | On paper 3.68:1 — graphics only, never text. |
| `--desk` | `#262019` | The desk around the leaf (page outside the diary) | surround | Darker than ink by one step; the leaf sits on it. Paper on desk is the leaf edge contrast, not a text pairing. |
| `--flower` | `#A8563C` | Pressed-flower petal — one flower per spread, maximum | <0.5% | The only colour not on the original desk; it is a *found object in the book*, not an ink. Rationed by §6.13's census: at most one pressed flower per spread, never repeated as a motif. |

### Pairing rules (measured, and gated)

- **Text pairings:** ink on paper 13.08:1 (any size), red on paper 8.97:1
  (corrections and strikes — text-bearing, any size), blue on paper 7.16:1
  (dates, notes, links — any size), pencil on paper 6.42:1 (numerals and
  ticks only, ≥13px equivalent).
- **Forbidden pairings:** red on ink **1.46:1** and blue on ink **1.83:1** —
  the hand never writes on a dark ground; there are no dark cards in this
  theme for handwriting to sit on. Tape as a text ground (2.32:1) is
  forbidden except the single printed-on-tape label of §6.14, which is set in
  ink (5.65:1) at caption size or larger.
- **The leaf never inverts.** Dark mode is *lamplight*, not inversion: the
  desk darkens to `--desk`, the leaf warms to `--paper-lamp`, inks stay
  themselves (a diary page does not change its ink at night). All three text
  pairings were re-measured on the lamplight leaf and still pass (above).
- **Red rationing:** red is ~4% of the page by area and appears only where a
  revision happens. A page whose red is decorative has failed before any
  motion runs — §9.2.

---

## 3. Typography

Two typefaces, exactly as the original entry specifies. No third face is
admitted for any purpose — numerals, labels and interface text are set in one
of the two, under the laws below.

- **EB Garamond** — the print. Entries, headings, captions, all interface
  text, all data that must be trusted at a glance. Garamond is the composed
  self: what the keeper was willing to print.
- **Caveat** — the hand. Margin notes, corrections, strikes' replacements,
  dates in the margin, the form's handwriting voice. Caveat is the private
  self: it annotates, it never publishes.

### Type scale (root 16px; the leaf's measure is set in §4)

| Role | Face | Size / line-height | Tracking | Rules |
|---|---|---|---|---|
| Entry title (the day's heading) | Garamond 500 | 40px / 1.1 (clamp 32–44px) | −0.01em | Set like a printed chapter head; the date above it is blue, by hand (§6.11). |
| Section head (within an entry) | Garamond 500 | 27px / 1.2 | 0 | Never underlined by CSS — if a head is underlined, the hand did it (§6.4). |
| Printed entry (body) | Garamond 400 | 19.5px / 1.62 | 0 | The reading size of the diary. Never below 18px on any breakpoint. |
| Caption / photo note | Garamond italic 400 | 15.5px / 1.45 | 0 | Print's whisper: captions, the colophon, the tally leaf's small print. |
| Margin note | Caveat 600 | 21px / 1.25 | 0 | Hand size: large enough to read at arm's length, small enough to be a margin. Rotated −1.2° to +0.8° by seeded value (§5). |
| Correction (replacement word) | Caveat 700 | 1.18× the size of the word it replaces | 0 | The replacement is always *larger* than what it replaces — the honest version gets more room. |
| Confession replacement | Caveat 700 | 26px / 1.3 | 0 | The largest handwriting on the page; reserved for §6.3, once per page at most. |
| Tally numerals | Caveat 600 | 20px | 0.01em | Pencil only (`--pencil`). Tabular by construction: each digit slot is a fixed 0.52em cell so a counting tally never reflows the margin. |
| Date stamp / margin date | Caveat 600 | 19px | 0.02em | Blue, always. A date is an addition, never an edit. |

### The five type laws

1. **The hand never sets a paragraph.** Caveat is rationed to ~14 words per
   note and never carries body copy, navigation labels or form instructions.
   Anything a visitor *must* read to use the site is printed in Garamond.
   (The law of §1 restated in type: handwriting annotates, print carries.)
2. **Numerals are printed, tallies are pencilled.** A number inside an entry
   (a year, a price, a count in prose) is Garamond. A number that is the
   diary counting itself (days kept, words revised) is Caveat in pencil —
   the bookkeeping hand, §6.9.
3. **A strike is a line, not a deletion.** Struck text keeps its Garamond
   (or Caveat) face, keeps its size, and gains a red line at 55% of x-height;
   its colour fades to ink at 0.38 opacity — never lower, never to paper.
4. **Handwriting never justifies, never centres.** Margin notes are ragged,
   left-aligned to their anchor, and rotated by their seeded angle. A centred
   Caveat note is a greeting card, not a diary (§9.7).
5. **Print is calm; only the hand moves.** Garamond text never types, never
   staggers, never reveals word by word — with one licensed exception: the
   opening entry types itself on first load (§6.11), because that is the
   keeper writing today's page, and it happens once.

---

## 4. Layout language

### The leaf and its margin

Every page is one leaf of the diary, centred on the desk (`--desk` shows at
the edges on wide screens; on small screens the leaf is the whole world and
the desk disappears). The leaf is a two-column ruled sheet:

- **The text column** — 62% of the leaf's inner width, max measure 34em of
  Garamond. This is where print lives. Nothing handwritten ever enters it
  except the marks that target printed words (strikes, circles, underlines,
  bleed corrections), which are overlays anchored to their words.
- **The margin column** — the remaining ~38%, separated from the text by the
  leaf's ruled margin line (a single `--rule-line` vertical, printed, full
  height). This is the hand's territory: notes, tallies, the ribbon, taped
  photos that lean in from the margin side. The margin is a *column in the
  layout*, never an absolutely-positioned afterthought — when handwriting is
  removed (no-JS, print stylesheet, reduced data), the margin still holds
  the notes as static Caveat text in flow.
- **The ruled rhythm** — horizontal rules every 31.5px (the body line-height
  × 1.62 ≈ 31.6px, rounded to the printed grid) run under the text column
  only. Text sits on the rules; photos and notes may cross them. The rhythm
  is the leaf's heartbeat and the reason the page reads as paper rather than
  as a cream rectangle (§9.6).

### Spacing and density rules

- Vertical spacing is counted in ruled lines: sections separate by 3 blank
  lines (94.5px), paragraphs by 1 (31.5px). A builder who reaches for a
  random 17px gap has left the diary.
- **One spread, one confession.** Each leaf carries at most one §6.3
  crossed-out confession and at most one §6.7 pinned spread. Density of
  *revision* is rationed like red ink: a page where everything is corrected
  says nothing was ever believed.
- **Margin load limit:** at most one note per paragraph, at most five notes
  per leaf before a new leaf (section break with a §6.13 divider) is
  required. The margin that comments on everything comments on nothing.
- Photos are pasted, not laid out: each taped photo (§6.6) sits at a seeded
  rotation of −2.4° to +2.4°, overlapping the margin line by 12–28px, and no
  two photos on a leaf share a rotation within 0.3°.

### Breakpoint philosophy (detail lives per element in §6)

- **≥1200px:** the full two-column leaf on the desk; margin at full width;
  the pinned spread pins.
- **768–1199px:** the leaf narrows; the margin column compresses to ~30%
  and notes shorten (the build truncates no text — the *content model*
  supplies a short-form note for this band; see §6.1 edge cases). Photos
  shrink to 82% and lean less.
- **<768px:** the leaf becomes a single column and the margin moves *below*
  its paragraph as an indented hand-block (a note under the text it
  annotates, set off by the margin line rotated to horizontal). Nothing is
  hidden; the diary is read top to bottom, print then thought, which on a
  phone is the honest order anyway. The pinned spread does not pin; its
  three annotations stack in sequence.

### Print stylesheet (part of the layout language)

Printing a leaf prints the *finished* diary: entries complete, notes fully
written in static Caveat, strikes shown struck, tallies at their final
values, photos without tape shadows. A visitor who prints the page takes
the diary as it will look when the hand rests — never a half-written note.

---

## 5. Full motion system

Every motion term the theme uses, in the diary's own language. Motion that
the diary cannot say in its own words does not appear: there is no marquee
(the keeper does not shout), no kinetic display type (print is calm, §3 law
5), no magnetic hover (paper does not pull), no custom cursor (the original
entry forbids it; the visitor's hand is their own).

### Named easings (the only five the theme may use)

| Token | Curve | Character | Used by |
|---|---|---|---|
| `--ease-pen` | `cubic-bezier(.45,.02,.35,1)` | Near-linear with a soft landing — a stroke being drawn at hand speed | Note stroke-ins (§6.1), circle scribble (§6.2), underline draw (§6.4) |
| `--ease-thought` | `cubic-bezier(.3,1.25,.4,1)` | Arrives a fraction early and settles — a thought landing | Note fade/settle, tally check-offs, divider flower (§6.13) |
| `--ease-bleed` | `cubic-bezier(.55,.06,.85,.4)` | Slow spread, reluctant start, no bounce — ink in paper fibre | Ink-bleed corrections (§6.5), coffee ring (§6.8), hover ink-darkening |
| `--ease-press` | `cubic-bezier(.25,.9,.3,1.15)` | A press down with the smallest overshoot — tape being smoothed by a thumb | Tape corners settling (§6.6), form slip pasting (§6.15) |
| `--ease-turn` | `cubic-bezier(.65,0,.3,1)` | Heavy start, long glide — a leaf turning, a ribbon sliding | Ribbon (§6.10), page turn (§6.16), pinned spread release (§6.7) |

### The motion terms, translated

- **Scroll-triggered reveals** are *thoughts occurring*: margin notes
  stroke in ~600ms after their paragraph crosses the reading line (§6.1).
  Nothing else "reveals" — print is already there.
- **Scroll-driven / scrubbed animation** exists exactly twice: the red
  underline that grows word-by-word under the confession paragraph at the
  reader's own pace (§6.4), and the ribbon bookmark's slide (§6.10). Both
  are scrubbed through the shared loop (below), never written directly by a
  scroll handler.
- **Parallax** is *pasted things sitting proud of the page*: taped photos
  ride 6–10px above the text layer's scroll (§6.6); nothing else parallaxes.
  Text never parallaxes against text.
- **Pinned sections:** one spread pins while three annotations accumulate
  (§6.7) — the theme's single pinned scene, rationed to once per leaf.
- **Masked reveals:** ink-bleed masks for corrections (§6.5) — the only
  mask in the theme, and it is a material (ink spreading), not a wipe.
- **Staggered reveals:** the entrance sequence (§6.11) and the pinned
  spread's three notes (§6.7) stagger by *thought*, 180–260ms apart, never
  by index-grid.
- **Animated counters:** the pencil tallies (§6.9) count by the events they
  record — a tally increments when its event happens on the page, never on
  a timer and never from zero on a page that is not the diary's first.
- **Progress indicator:** the ribbon bookmark (§6.10) — position in the
  leaf, kept the diary's way, with entries checking off in pencil.
- **Ambient loops:** exactly two, both nearly still — the coffee ring
  darkening across the visit (§6.8) and the ruled lines' faint ink-breath
  on scroll (§6.8's companion rule: a 1.5% opacity oscillation of the rule
  layer while scrolling, settling to rest within 400ms of scroll stop).
  Nothing on the page loops for attention.
- **Hover micro-interactions:** ink darkening (§6.1: a note's Caveat deepens
  from 82% to 100% ink strength over 240ms `--ease-bleed`, as if freshly
  written), tape lift (§6.6: a photo's far corner rises 2px), link
  underlines drawn by hand (§6.12).
- **Page transitions:** the leaf turn (§6.16) — a page edge sweeps, 500ms
  ceiling, content swapped at full cover.
- **Skeleton loading:** ruled lines and pencil ghosts (§6.16) — the page as
  an unwritten leaf, never grey bars.
- **Reduced motion:** the diary at rest — every note fully written, every
  correction already bled, the ribbon placed (not slid) at the right depth,
  tallies at final values. Specified per element in §6; it is a complete
  reading experience, not a degraded one.

### The one shared loop

All scrubbed and ambient values (ribbon depth, underline growth, photo
parallax offsets, ring opacity) are driven by a single `requestAnimationFrame`
loop lerping toward target at **0.12** per frame. Scroll handlers set
targets only; they never write styles. The loop sleeps when no target is
more than 0.05px / 0.001 opacity from its current value, and stops entirely
under `prefers-reduced-motion` (values are placed once, statically).

### Seeded imperfection (a system, not a garnish)

Every hand-made mark carries a rotation or path variation derived from a
seed printed in the DOM (`data-seed`), computed as `((seed × 37) mod 100) /
100` mapped into the element's stated range. The same page built twice has
the same handwriting; a mark whose angle is runtime-random is a failed
build (§9.3) because it means the mark was decoration, not a decision.

---

## 6. Signature elements

### 6.1 The self-writing margin notes

**What & why.** Handwritten notes (Caveat) that stroke themselves in beside
the paragraph they annotate, arriving ~600ms *after* the paragraph passes
the reading line — always a beat late, like a thought occurring. This delay
is the theme's central characterisation: the margin is a second narrator
with human timing, reading over the visitor's shoulder and reacting. A note
that appears exactly with its paragraph is a caption; a note that arrives a
beat late is a person.

**Structure.** Each note is a `<aside class="m-note">` in the margin column,
in DOM order immediately after its paragraph, containing (a) the note as
real Caveat text — the only copy, always in the DOM — and (b) an inline SVG
overlay whose paths trace the same words as stroke paths for the writing
performance. The text layer is present from first paint at full legibility
*under* the performance: the build renders the text at 0% ink strength and
the SVG strokes draw over the same glyphs, so the eye reads handwriting
forming while the DOM never lacks the words. Ink colour by content: blue
for factual afterthoughts, red only when the note corrects its paragraph
(§1's ink law), pencil never (pencil counts, it does not comment).

**Motion spec.** Trigger: the annotated paragraph's last line crosses a
reading line at 62% of viewport height. Delay: 600ms ± seeded 0–120ms.
Stroke phase: paths draw at hand speed, 90–140ms per word, `--ease-pen`,
total capped at 1600ms per note regardless of length (longer notes draw
faster per word, never slower overall). Settle: the SVG overlay fades out
over 200ms `--ease-thought` as the text layer reaches 100% ink strength —
the performance hands over to the real text so seamlessly that the visitor
cannot say when drawing became print. Concurrency: at most one note writes
at a time; a queue forms in reading order.

**Choreography timeline** (t=0 is the paragraph crossing the reading line):
0ms paragraph crosses · 600ms first stroke begins (pen-down) · 600–1900ms
words stroke in reading order · 1750ms text layer begins rising from 82% to
100% ink strength · 1950ms SVG overlay fully faded, removed from the
accessibility tree and the paint tree · note is at rest.

**State matrix.** *Rest:* fully written Caveat at 100% ink, seeded rotation
−1.2° to +0.8°. *Hover:* ink deepens — the note is already at full strength,
so hover instead lifts the note 1px and warms its colour by 4% (freshly
written, §5) over 240ms `--ease-bleed`; on touch, the same state is reached
by tap and released by tapping elsewhere. *Focus:* notes are not focusable
unless they contain a link; a linked note shows the hand-drawn focus rule
(§6.12) under its link only. *Active:* n/a. *Scrolled-past:* written notes
stay written — scrolling back up never un-writes a note (the keeper does
not un-think). *Disabled:* n/a. *Unvisited (below fold):* text present at
0% ink strength in the DOM; a find-in-page or screen-reader pass reads it
normally (see Accessibility).

**Content-merge.** The note *is* content — a second voice with facts,
doubts and jokes the print was too composed to say. It is positioned by its
paragraph, not by the layout: move the paragraph and the note follows in
DOM order. A note that could sit beside any paragraph is decoration and is
cut at the gate (§10, check 4).

**Breakpoints.** ≥1200px: margin column, notes at 21px Caveat, full stroke
performance. 768–1199px: margin compresses (§4); the content model supplies
a short-form note (same thought, fewer words — authored, never truncated by
CSS) and stroke time caps at 1100ms. <768px: the note moves below its
paragraph as an indented hand-block; the stroke performance is replaced by
a 300ms ink-strength rise (82%→100%) — handwriting "drawing itself" in a
narrow column reads as a rendering glitch, so the thought arrives by
presence, not by strokes.

**Edge cases & failure modes.** *SVG path missing or corrupt:* the text
layer rises to full strength on the delay alone (the note "appears" fully
written) — **fallback**: text at 100% by t=800ms regardless. *Watchdog:* if
the stroke animation has not completed by **2400ms** after trigger, the
overlay is removed and the text snaps to full strength. *Long note (>14
words):* violates §3 law 1 — the build splits it into two notes on adjacent
paragraphs or rejects it at content review. *Rapid scrolling:* notes whose
paragraphs pass during a fast scroll (>1.5 viewport/sec) skip the stroke
performance and appear written — the keeper cannot write at that speed
either, and a backlog of writing animations chasing the reader is the
theme's most common cheapness (§9.1). *Scroll-up:* nothing replays.

**Accessibility.** The note is an `<aside>` with `aria-label` unset — its
text is read in flow, in order, as part of the document. The SVG overlay is
`aria-hidden="true"` and `pointer-events: none`. Because the text layer is
in the DOM from first paint, screen readers and find-in-page never wait
for the performance. Contrast: blue notes 7.16:1, red notes 8.97:1 on
paper — both pass at note size. Focus order is document order; the overlay
never intercepts focus or clicks.

**Tokens.** `--blue` / `--red` (ink by content), `--ease-pen`,
`--ease-thought`, `--ease-bleed` (hover), `data-seed` for rotation and
delay jitter. Ink strength is a per-note custom property `--ink-strength`
(0–1) consumed by the text layer's colour mix.

**Performance & mobile variant.** SVG paths are the cost: budget ≤9KB of
path data per note, ≤5 notes per leaf (§4), paths pre-computed at build
time (never traced at runtime). The stroke uses `stroke-dashoffset` only —
a compositor-cheap property. Mobile (<768px) drops the SVG entirely (the
file is not shipped in the mobile payload) and uses the ink-rise variant.

**Reduced motion.** Notes are simply present, fully written, at rest
rotation. The 600ms delay is also removed — a thought that must not move
must not make the reader wait either.

### 6.2 The scribbled red circle

**What & why.** On load, after the opening entry settles, a red-pencil
circle scribbles itself around one chosen phrase in the entry — two
overlapping, imperfect loops, drawn fast, the way a reader circles the
sentence that turned out to be true. It is the page's thesis made visible:
this life is being revised, and here is the line the keeper now believes.

**Structure.** An inline SVG positioned over the circled phrase, containing
two closed paths (loops) whose control points are offset by seeded values
so the circle is imperfect in a fixed, authored way. The phrase itself is a
`<mark class="m-circled">` in the printed text — semantically marked, fully
legible, styled with no background by default; the SVG is pure overlay.
Exactly one circled phrase per leaf (rationed, §4).

**Motion spec.** Trigger: load, after §6.11's entrance completes (or, on
pages without the typing entrance, 500ms after first paint). Duration:
~700ms total — loop 1 draws in 380ms `--ease-pen`, loop 2 in 320ms,
overlapping the first by 60ms, slightly tighter and faster, the way a hand
goes around twice. The pencil line is 2.5px, round-capped, red at 88%
strength (a pencil is never a marker).

**Choreography timeline** (t=0 entrance complete): 0ms pen-down at the
phrase's upper left · 0–380ms loop 1 · 320ms loop 2 begins · 320–640ms loop
2 · 640–700ms a 40ms pressure settle (stroke width 2.5→2.75px at the
overlap point) · rest. The circle never moves again.

**State matrix.** *Rest:* drawn, static. *Hover (on the phrase):* the
circle's stroke deepens 88%→100% over 240ms `--ease-bleed` and the phrase's
margin note (§6.1), if one exists, lifts 1px — the two marks acknowledge
each other. Touch: tap the phrase for the same pairing. *Focus:* if the
phrase is or contains a link, keyboard focus draws a second, *printed*
focus rule beneath (Garamond-weight, §6.12) — the pencil never serves as a
focus indicator. *Scrolled-past / return:* unchanged; the circle is a
fact of the page, not an animation that replays. *Disabled:* n/a.

**Content-merge.** The circled phrase must be the entry's actual turning
point — the sentence the entry exists because of. Circling a headline, a
product name or a call to action is the theme's signature corruption
(§9.5): the keeper circles what is *true*, never what is *for sale*.

**Breakpoints.** ≥1200px and 768–1199px: identical, the SVG scales with
the phrase's box. <768px: the loops are redrawn from the same seed against
the wrapped phrase's (possibly two-line) box; if the phrase wraps to three
lines or more, the circle becomes a red bracket down the left of the lines
— a hand circling a wrapped phrase does exactly that.

**Edge cases & failure modes.** *Font swap after draw:* the SVG is sized
from the phrase's rendered box at draw time and re-fitted once on
`document.fonts.ready`; if the box moves by more than 2px after that
(late image, resize), the circle re-fits instantly without re-drawing.
*Watchdog:* if the draw has not finished by **1600ms**, both loops snap to
fully drawn. *No-JS:* the circle is present as a static SVG in the HTML —
it is part of the finished page (see Reduced motion). *Resize across
breakpoints:* re-fit, never re-animate.

**Accessibility.** The `<mark>` carries the meaning; the SVG is
`aria-hidden`. The circled phrase is announced as marked text by assistive
tech that supports `<mark>`; the build adds no redundant description,
because the circle's meaning ("the keeper believes this") is carried by
the adjacent margin note in any well-authored page. Contrast: the pencil
line is a graphic over text — the text beneath it remains ink on paper at
13.08:1; the line never crosses a glyph's counter in a way that reduces
legibility (paths are fitted to the phrase's padding box, not its glyph
box).

**Tokens.** `--red`, `--ease-pen`, `--ease-bleed` (hover), `data-seed` for
loop imperfection. Stroke width token `--pencil-stroke: 2.5px`.

**Performance & mobile variant.** One SVG, ≤1.2KB of path data. The draw
animates `stroke-dashoffset` only. Mobile keeps the full element (it is
cheap) with the bracket variant for long wraps.

**Reduced motion.** The circle is simply there, fully drawn, from first
paint — as it is in the no-JS page.

### 6.3 The crossed-out confession

**What & why.** One sentence on the page is struck through in red pencil
but remains faintly legible underneath — and it is the most honest sentence
on the page. Beside it (or immediately after it, in the margin's voice) the
replacement writes itself, larger. This is the theme's emotional core:
revision shown, not hidden. The visitor is trusted with what the keeper
first wrote and could not stand behind — and with what they wrote instead.

**Structure.** A `<span class="m-confession">` in the printed entry
containing three layers: the original sentence (real text, printed,
struck), an SVG red strike line fitted to its box, and the replacement as
a Caveat `<ins class="m-replacement">` in the margin aligned to the
sentence's line (on mobile, directly beneath). The original is never
removed from the DOM, never `display:none`, never replaced by an image.

**Motion spec.** Trigger: the sentence crossing the reading line (62%
viewport). Beat 1 — the strike: the red line draws across the sentence in
420ms `--ease-pen`, with a seeded slight sag (the line dips 1.5px at its
middle third — a hand pressing). Simultaneously the original's colour
fades from full ink to its permanent 0.38-opacity struck state over the
same 420ms. Beat 2 — a 350ms pause (the keeper deciding). Beat 3 — the
replacement writes itself (§6.1's stroke system) at 26px Caveat over
700–1000ms, then settles at its larger size. Total performance ≤1900ms.

**Choreography timeline** (t=0 sentence at reading line): 0ms strike
begins · 0–420ms line draws, original fades to 0.38 · 420–770ms pause ·
770ms replacement pen-down · 770–1670ms replacement writes · 1670–1870ms
replacement settles (rotation to its seeded −0.9°, ink to 100%) · rest.
The §6.9 tally increments at t=420ms — the strike is the revision event.

**State matrix.** *Rest:* original legible at 0.38 under a drawn strike;
replacement fully written, larger, at full red strength. *Hover:* the
original's opacity rises 0.38→0.55 over 240ms `--ease-bleed` — leaning
closer to read what was crossed out is a real diary behaviour, and the
page rewards it without ever making the struck text fully "current"
again. Touch: tap-and-hold (or tap) toggles the same lift. *Focus:* the
confession is not interactive; no focus state. *Scrolled-past:* final
state persists; never replays. *Print:* struck at 0.38, replacement
written — the finished page (§4).

**Content-merge.** The confession must be a genuine revision of *feeling or
fact within the entry's own story* — "I told him I was fine" → "I was not
fine, and he knew." It is rationed to one per leaf (§4) and may never be
used on prices, dates, names or anything a visitor acts on: doubt is
literary here, never transactional (§1, when NOT to use).

**Breakpoints.** ≥1200px: replacement in the margin, aligned to the
sentence. 768–1199px: replacement in the margin at 24px (the margin is
narrower; the replacement is still the largest hand on the page).
<768px: replacement directly below the sentence, full width, 25px; the
strike and fade are unchanged.

**Edge cases & failure modes.** *Multi-line sentence:* the strike is drawn
per line (two or three fitted lines, drawn in sequence at 200ms per line)
— a single diagonal slash across a paragraph is a different, angrier mark
and is forbidden. *Watchdog:* strike complete by **1200ms** after trigger
or it snaps drawn; replacement fully written by **2600ms** or it snaps to
static Caveat text. *No-JS:* the finished state ships in the HTML — struck
original at 0.38, strike line as static SVG, replacement as static text.
*Very long original (>24 words):* a confession is a sentence, not a
paragraph; content review rejects it — striking a paragraph reads as
censorship, striking a sentence reads as honesty.

**Accessibility.** Both versions are in the reading order: the original is
a `<del>`-equivalent (the build uses `<s>` styled by the theme, with the
replacement as `<ins>`), so assistive tech that announces edits will
announce this one — which is correct: it *is* an edit. The 0.38 opacity
state measures ~3.4:1 against paper — deliberately below body-text
contrast because the text is *superseded*, but it must remain legible to a
determined reader; the hover/tap lift to 0.55 (~5.1:1) is the accessible
reading state and is also reachable by keyboard: the confession carries
`tabindex="0"` with a visible printed focus rule, and focus applies the
same lift. This is the one element where focus is given to non-interactive
content, and §10 check 6 audits that it works.

**Tokens.** `--red`, `--ink` (original, mixed to 0.38 via
`--struck-strength`), `--ease-pen`, `--ease-bleed`, `data-seed` (strike
sag, replacement rotation).

**Performance & mobile variant.** One small SVG per line of the original;
≤2KB total. The fade is an opacity transition on the text span
(compositor-only). Mobile keeps the full performance — it is the theme's
core — with the replacement repositioned as above.

**Reduced motion.** The finished state from first paint: struck, faded to
0.38, replacement written. The hover/focus lift still works (it is a state
change, not a motion), at 0ms duration.

---

### 6.4 The scrubbed red underline

**What & why.** Beneath one paragraph — the confession paragraph, the one
the entry has been avoiding — a red-pencil underline grows word by word,
scrubbed to the visitor's own scrolling. Emphasis is performed by reading:
the underline exists, at exactly its length, because you went slowly
there. Scroll back and it shortens; the keeper underlines only as far as
you have actually read.

**Structure.** An SVG path layer beneath the paragraph (absolutely
positioned in the text column, `pointer-events: none`), holding one
hand-fitted underline path per line of the paragraph, each with a seeded
1–2px wobble. The paragraph is ordinary printed text in the DOM; the
underline targets are computed from the paragraph's line boxes at build
time and re-fitted on resize/font-load exactly as §6.2's circle.

**Motion spec.** Scrubbed, not triggered: the shared rAF loop (§5) maps the
paragraph's passage through the reading zone (top of paragraph at 78%
viewport → bottom of paragraph at 34% viewport) to an underline fraction
0→1, lerped at 0.12. The drawn length follows the fraction across the
per-line paths in reading order — word by word in effect, line by line in
construction. Stroke: 2.5px `--pencil-stroke`, red at 80% strength (an
underline is a lighter touch than a strike). There is no duration: the
visitor's scroll *is* the duration.

**Choreography timeline.** Continuous, not beat-based: fraction 0 when the
paragraph's first line reaches 78% viewport height · fraction grows
line-by-line as the paragraph traverses the zone · fraction 1 as the last
line passes 34% · scrolling up reverses the same mapping with the same
lerp — the underline un-grows at reading speed, never snaps.

**State matrix.** *Rest (paragraph unentered):* no underline; text plain.
*In zone:* partial underline at the lerped fraction. *Scrolled-past:*
full underline remains (the paragraph has been read; the mark stays).
*Returned-to after passing:* full. *Hover/focus:* none — the underline is
the reader's own act and takes no other input. *Disabled:* n/a. *Touch:*
identical — scrub is scroll, not gesture.

**Content-merge.** One paragraph per leaf may be underlined (rationed like
the confession, and usually the same passage the confession lives in — the
theme's marks cluster where the feeling is). Underlining a heading, a
price or a call to action is forbidden for the same reason as §6.2's
circling rule: the hand emphasises truth, not offers.

**Breakpoints.** ≥1200px / 768–1199px: identical construction, re-fitted
line boxes. <768px: identical, with the reading zone widened (82%→28%) to
compensate for the shorter viewport — the underline must still be able to
complete within one passage of the paragraph.

**Edge cases & failure modes.** *Jump scroll (anchor link, find-in-page,
scroll restore):* if the paragraph is already fully past on load, the
underline is placed at fraction 1 instantly — the reader is deemed to have
read it; if it is unentered, fraction 0. No animation chases a jump.
*Watchdog:* the scrub is loop-driven and cannot strand content — the
underline is an overlay on complete text — but the loop itself is covered
by §5's rule: if the rAF loop dies, the underline freezes at its current
fraction and the text is unaffected (failure is invisible, which is the
correct failure for an emphasis mark). *Paragraph reflows mid-scroll
(late image above):* targets re-fit on the next frame; the fraction is
preserved, so the underline re-maps without jumping in *proportion*.

**Accessibility.** Pure emphasis overlay: `aria-hidden`, no semantics, no
focus. The paragraph reads identically with the underline at 0, partial or
full. Red at 80% over paper measures ~7.4:1 as a graphic — comfortably
visible, and it never carries information the text lacks (the gate checks
this: §10, check 5).

**Tokens.** `--red` (at `--underline-strength: .8`), `--pencil-stroke`,
the shared loop's `--lerp: .12`. No easing token — scrubbed motion is
eased by the lerp itself.

**Performance & mobile variant.** Paths ≤3KB per paragraph; the loop
writes one `stroke-dashoffset` per frame while the paragraph is in the
zone and sleeps outside it. Mobile: full element retained (cheap), zone
widened as above.

**Reduced motion.** The underline is placed at fraction 1 when the
paragraph first enters the viewport — emphasis present, performance
removed. (Placing it at 1 unconditionally would underline text the visitor
may never reach, which the keeper would not do.)

### 6.5 Ink-bleed corrections

**What & why.** Where the keeper corrects a single word in the printed
entry — a wrong name, a wrong year, a kinder adjective than the true one —
the correction happens by ink bleed: the old word blurs and spreads as if
wet, and the new word bleeds in over it, over ~600ms. Editing has a
material in this theme: ink, not opacity. A crossfade says "updated"; a
bleed says "I changed my mind, here, in this word."

**Structure.** A `<span class="m-correct">` wrapping the original word
(real text) and its replacement (`<ins>`, real Caveat text, 1.18× size per
§3), stacked in the same inline box. The bleed is rendered with two
filters on duplicate text layers (an SVG `feGaussianBlur` + displacement
"wet" layer per word, pre-built at build time) — the live DOM text itself
is never filtered, so the words stay selectable, searchable and readable
by assistive tech at every instant of the transition.

**Motion spec.** Trigger: the corrected word crossing the reading line, or
a click/tap on the word (the visitor may re-play a correction deliberately
— diaries are re-read). Duration 600ms `--ease-bleed`: 0–180ms the old
word's wet layer spreads (blur 0→2.2px, scale 1→1.04, opacity 1→0), the
printed layer beneath crossfades in the final 80ms of that span; 140–600ms
the replacement bleeds in in mirror (blur 2.6→0, opacity 0→1) and settles
at full Caveat strength. Each correction increments §6.9's *words revised*
tally at its midpoint (t=300ms) — once per correction per page-load, no
matter how often the visitor replays it.

**Choreography timeline** (t=0 trigger): 0ms old word stills · 0–180ms
old word wets and spreads · 140ms replacement begins bleeding in ·
300ms tally increments · 480ms replacement at 90% strength · 600ms
replacement at rest (seeded rotation −0.6° to +0.6°, ink 100%) · the old
word's layers are removed from the paint tree, its text remaining in the
DOM as the `<del>`-equivalent record.

**State matrix.** *Rest (before trigger):* the original word, printed,
unremarkable — a first-time reader may not notice it will be corrected.
*During:* as above. *Rest (after):* the replacement word, Caveat, slightly
larger, in the ink of its kind (red if the correction is a judgement, blue
if a fact — §1). *Hover (after):* a faint red hairline appears beneath the
replacement (160ms, `--ease-bleed`) and the original word is offered as a
tooltip-free reveal: hovering shows the old word pencilled in the margin
at the same line (desktop); on touch and on keyboard focus, a tap/focus
toggles the same margin ghost. The visitor can always learn what was
changed — the diary hides nothing it has shown. *Scrolled-past:* final
state. *Replay:* click re-runs the 600ms bleed, tally does not
re-increment.

**Content-merge.** Corrections are the diary's facts about itself: wrong
year → right year, "friend" → "brother", "fine" → "furious". Each must be
a word the entry's own story makes meaningful. A build may carry at most
six bleed corrections per leaf (the §8 worked example's leaf carries
five, plus its one confession strike — six revision events in all — and
its tally arithmetic is the audit trail). Correcting a word to a
synonym of identical weight is filler and fails §9.8.

**Breakpoints.** All bands: identical construction (inline, word-sized).
<768px: the margin ghost of the original word appears *below* the line
instead of in the (absent) margin. The 1.18× replacement size may wrap
the line — acceptable and even desired: a correction that pushes the line
is a correction that mattered; the ruled rhythm (§4) absorbs one wrapped
line per paragraph without breaking the grid because the leaf's lines are
a background layer, not a layout constraint on the margin column.

**Edge cases & failure modes.** *Filters unsupported / low-power device:*
the bleed degrades to a 300ms crossfade between the two real text layers
— the correction still reads as ink (both layers are tinted) and never as
a glitch. *Watchdog:* if the transition has not completed by **1500ms**,
both wet layers are removed and the replacement snaps to rest state.
*No-JS:* the replacement ships as the visible word with the original
struck-through in print beside it (the static notation `old → new` set in
Garamond small type) — the correction is content, so the no-JS page must
carry it in full. *Word inside a link:* forbidden at content review — a
bleed inside a link makes the link's destination ambiguous mid-transition.

**Accessibility.** The pair is marked up as `<s>`/`<ins>` equivalents so
the edit is announced as an edit. During the 600ms, the *printed* layer
(the accessible one) presents the replacement from t=140ms — assistive
tech never reads a blurred word, because the blur lives only in the
presentational wet layers (`aria-hidden`). Focus: the corrected word is
focusable (`tabindex="0"`) to reveal the margin ghost (see State matrix),
with the printed focus rule. Touch target for the tap-replay is the word's
line box, min height 31.5px (one ruled line) — the word itself may be
short, the line is the target.

**Tokens.** `--red` / `--blue` (by correction kind), `--ink`, `--ease-bleed`,
`data-seed` (replacement rotation), `--wet-blur: 2.2px`.

**Performance & mobile variant.** Filter layers are the theme's most
expensive paint: ≤6 corrections per leaf, each wet layer is a word-sized
bitmap, filters are pre-rendered to a sprite at build time where the
browser supports it, and the animation runs on `opacity`/`transform` of
the pre-rendered layers — never on a live filter. Mobile: identical, with
the crossfade degradation threshold lowered (devices reporting
`hardwareConcurrency ≤ 4` take the crossfade path directly).

**Reduced motion.** No bleed: the replacement is present at rest, the
original available via the margin ghost on focus/tap exactly as in the
hover state. The tally prints its final value (§6.9).

### 6.6 Taped photos that settle

**What & why.** Photographs in the diary are not embedded in a layout;
they are pasted into a life — held by translucent tape corners, riding on
a layer above the page text, settling with a tiny rotation and press when
they arrive. The photo is evidence: the keeper kept it, carried it, taped
it in. Its slight imperfection (rotation, tape, overlap of the margin
line) is what makes it believed.

**Structure.** A `<figure class="m-photo">` containing the image, a
Garamond italic caption *printed beneath it on the leaf* (captions are
print, not handwriting — the keeper typed the caption when they pasted the
photo in; only later annotations are by hand), and four tape corner
elements (CSS gradients on `--tape` at 55% opacity with a `--tape-deep`
edge) — two corners minimum on small photos, four on large. The figure
sits in flow in the text column and leans across the margin line by
12–28px (§4), at a seeded rotation of −2.4° to +2.4°.

**Motion spec.** Two motions. *Parallax:* the figure rides above the text
layer via the shared loop — offset = scroll progress through the figure's
zone × 6–10px (seeded within that range), lerped at 0.12, so the photo
drifts almost imperceptibly against the print as you read past it.
*Settle:* when the figure first crosses 70% viewport, its rotation eases
from seeded+0.7° to seeded over 500ms `--ease-press` and each tape corner
presses (scale 1.06→1, shadow tightening) staggered 60ms apart in reading
order — a thumb smoothing the tape. The settle plays once.

**Choreography timeline** (t=0 figure at 70% viewport): 0ms settle begins
· 0–500ms rotation eases to seed · 60/120/180/240ms tape corners press in
sequence · 500ms rest; parallax continues independently via the loop for
as long as the figure is on screen.

**State matrix.** *Rest:* photo at seeded rotation, tape flat, caption
printed. *Hover:* the far (bottom-right) corner lifts 2px with its shadow
lengthening 3px over 280ms `--ease-press` — the photo is touchable,
peelable-feeling, but it never peels: lifting is a promise the theme does
not break (§9.9). Touch: the lift is omitted; tap opens nothing (a photo
is not a button unless it is explicitly a link, in which case §6.12's
printed focus/hover rules apply to the whole figure). *Focus (if
linked):* printed focus rule around the figure's box. *Scrolled-past:*
parallax offset returns toward 0 as the zone exits; rotation stays at
seed. *Disabled:* n/a.

**Content-merge.** Every photo must be *of the entry's own story* — the
house in the entry, the letter, the two people — and its caption must add
a fact the entry lacks (a date, a name, "the last summer"). A stock-feel
photo with a decorative caption fails §9.9 and the gate. The tape is the
merge made visible: the photo is attached *to this leaf*, overlapping the
margin line where the hand works.

**Breakpoints.** ≥1200px: full size (up to the text column's width + the
margin lean), four tape corners, parallax 6–10px. 768–1199px: 82% size,
lean reduced to 8–16px, parallax 4–7px. <768px: full text-column width,
no lean (there is no margin to lean into), two tape corners (top pair),
parallax cut to 3px (a phone's short viewport makes larger drift seasick),
settle retained.

**Edge cases & failure modes.** *Image fails to load:* the figure becomes
a taped *empty mount* — the tape corners and a pencilled caption remain
("the photo was here; it has come loose") with the image's alt text
printed in Garamond where the photo was. The diary admits the loss rather
than showing a broken-image icon (§9.9's cure). *Watchdog:* the settle is
a transform transition; if `transitionend` has not fired by **1200ms**,
the figure snaps to its rest rotation. *Slow network:* the figure's box
is reserved at its aspect ratio from first paint (the leaf never
reflows); the photo fades in over 300ms `--ease-bleed` when it arrives —
ink arriving, not a grey box filling. *No-JS:* photo static at seed
rotation, tape present, no parallax — the finished page.

**Accessibility.** The image carries real `alt` text (the photo's content,
not its caption). The figure is not interactive unless linked. Tape
corners are decorative (`aria-hidden`). Parallax is disabled for any
visitor whose device reports a vestibular risk signal the browser exposes,
independently of the full reduced-motion setting — a drifting photo over
text is exactly the pattern that harms.

**Tokens.** `--tape`, `--tape-deep`, `--ease-press`, `--ease-bleed`
(arrival fade), `data-seed` (rotation, lean, parallax range).

**Performance & mobile variant.** Images are the page's weight budget
(§14): each photo ≤120KB served (responsive sizes), lazy-loaded below the
first leaf. Parallax is a single `transform` per figure from the shared
loop — no per-photo listeners. Mobile: sizes and parallax as above;
`content-visibility: auto` on figures below the fold.

**Reduced motion.** No parallax, no settle: the photo is pasted, at seed
rotation, tape flat, from first paint.

---

### 6.7 Pinned spread, three annotations

**What & why.** One spread pins in place while three successive margin
notes annotate the same paragraph in sequence — first agreement, then
doubt, then a pressed flower. A single moment, revisited three times: the
margin thinks in public. This is the theme's one pinned scene and its
slowest, most deliberate passage — the visitor is held with one paragraph
while a mind changes around it.

**Structure.** A `<section class="m-spread">` containing the paragraph (a
full spread's worth of print — the entry's pivotal passage, set slightly
larger at 21px) and three annotation slots in the margin, each an §6.1
note with its own ink and trigger beat, the third slot holding the
pressed flower (§6.13's element, appearing here in its narrative role)
with a two-word pencilled label. The pin is `position: sticky` within a
track of 240vh (desktop); the beats are mapped to the track's progress by
the shared loop.

**Motion spec.** Track progress 0→1 across 240vh of scroll. Beat 1 at
progress 0.18: note one (blue, agreement — "yes. this is how it was.")
strokes in per §6.1 (cap 1200ms). Beat 2 at 0.48: note two (red, doubt —
"or did I invent that?") strokes in; as it completes, note one's ink
strength settles from 100% to 88% — the first thought does not disappear,
it is *succeeded*. Beat 3 at 0.78: the flower fades/presses in over 900ms
`--ease-thought` (a flower is placed, not written) with its pencilled
label beneath. The spread releases at progress 1 with a 400ms
`--ease-turn` unpin glide — the leaf lets go gently.

**Choreography timeline** (by track progress): 0 pin engages · 0.18
note 1 pen-down · ~0.30 note 1 complete · 0.48 note 2 pen-down · ~0.60
note 2 complete, note 1 dims to 88% · 0.78 flower begins · ~0.92 flower
and label at rest · 1.0 release glide 400ms · scroll continues.

**State matrix.** *Rest (before track):* paragraph printed, margin empty
(the thoughts have not happened yet — the DOM still carries all three
annotations as text at 0% ink strength, exactly as §6.1). *In track:*
beats as above; scrolling up reverses the *pin position* but not the
annotations — once a thought has been thought on this visit it stays
written (ink dimming of note 1 also persists). *Scrolled-past:* the
spread rests complete: two notes (one dimmed) and the flower. *Hover:*
each note takes §6.1's hover; the flower's hover shows its label at full
pencil strength. *Focus:* notes follow §6.1; the spread itself is not a
focus target. *Disabled:* n/a.

**Content-merge.** The three beats must be a real sequence of mind about
*this* paragraph: agreement → doubt → the flower (which is the keeper
stopping arguing and keeping the moment instead). Any three random notes
parked in a pin is the theme's most expensive filler (§9.10). The
paragraph must be the entry's pivot — the passage the whole entry turns
on — or the pin is a toll booth on a straight road.

**Breakpoints.** ≥1200px: full pin, 240vh track, beats as specified.
768–1199px: track shortens to 200vh, beats at 0.16 / 0.46 / 0.76 (the
narrower margin makes each note shorter — short-form notes per §6.1's
content rule). <768px: **no pin.** The spread becomes a normal section;
the three annotations stack beneath the paragraph in beat order, each
arriving by §6.1's mobile ink-rise as it crosses the reading line. The
story survives intact; only the holding still is cut, because a pinned
screen on a phone is a trap, not a pause.

**Edge cases & failure modes.** *Sticky unsupported / fails:* the spread
degrades to the mobile stacking behaviour at any width — beats fire on
the reading line instead of track progress. *Watchdog:* each beat's note
is covered by §6.1's 2400ms watchdog; additionally, if track progress
jumps (anchor navigation into the middle of the track), all beats up to
the current progress are placed in their completed states instantly —
the visitor who arrives mid-thought sees the thought so far, never a
half-drawn stroke. *Scroll-up past the track start:* pin disengages,
annotations persist (above). *Very tall paragraph:* if the spread's
content exceeds 92vh at any band, the pin is disabled by the build (a
pinned element taller than the viewport hides its own bottom) and the
stacking behaviour applies.

**Accessibility.** The sticky container must never trap focus: it is a
plain section in DOM order, annotations read in order (paragraph, note 1,
note 2, flower label as figure caption). The pin is presentational
(`position: sticky` does not change reading order). Beat timing never
gates content availability — all text is in the DOM from first paint
(§6.1's rule). The flower's label is real text, not image alt alone.

**Tokens.** `--blue`, `--red`, `--flower`, `--pencil` (flower label),
`--ease-pen`, `--ease-thought`, `--ease-turn`, the shared loop.

**Performance & mobile variant.** The pin is one sticky element; beats
reuse §6.1's stroke system (no new machinery). The flower is one inline
SVG ≤6KB. Mobile: no pin, no sticky, beats by reading line — the cheapest
form of the element, and the one every degraded path falls back to.

**Reduced motion.** No pin (as mobile), all three annotations present and
written from first paint, note 1 at its final 88% strength, flower
placed. The *sequence* is still legible from their order and inks — the
story does not depend on the performance.

### 6.8 The coffee ring that darkens

**What & why.** At one corner of the leaf sits a coffee ring — the trace
of a cup set down on the open diary, again and again. Across the whole
visit it darkens, almost imperceptibly: ~4% opacity over minutes. The
page ages during your visit. The diary was lived in before you, and it is
being lived in still. This is the theme's ambient signature: time,
passing, in the diary's own material.

**Structure.** One inline SVG (two concentric imperfect circle paths with
a soft inner stain gradient) positioned at the leaf's top-right corner,
partly under the margin's top area, never under text — the ring sits on
blank paper at the corner, overlapping the ruled area's edge by design
(a cup does not respect the margin). It is printed in the HTML at its
starting opacity; the darkening is a slow CSS custom-property drift
driven by the shared loop's clock.

**Motion spec.** Opacity from 0.16 to 0.20 (a 4-point rise) across the
visit, eased on a long `--ease-bleed` curve: faster in the first minute
(the cup was recent), asymptoting after ~6 minutes. The rise is tied to
*engaged* time: it pauses when the tab is hidden (`visibilitychange`) —
the keeper does not drink while you are gone. Companion rule (from §5):
while the visitor scrolls, the leaf's ruled lines breathe at ±1.5%
opacity, settling within 400ms of scroll stop; the ring does not breathe
(it is a stain, not a light).

**Choreography timeline.** Continuous: t=0 (first paint) opacity 0.16 ·
t=60s ≈0.182 · t=180s ≈0.194 · t=360s ≈0.199 · asymptote 0.20, held. No
other beats; the ring has no trigger, no completion state, no replay.

**State matrix.** *Rest:* as above. *Hover:* none — hovering a stain does
nothing, and making it react would confess it is an interface element.
*Focus:* never focusable. *Scrolled-past/return:* opacity is a function
of visit time, not scroll; unchanged by navigation within the page.
*Disabled:* n/a.

**Content-merge.** The ring merges by *placement and singularity*: one
ring, at one corner, on the diary's home leaf (and, on multi-leaf sites,
only on leaves the keeper "lives on" — the current entry; archive leaves
carry their ring already at full darkness, printed, because their visits
are over). A ring on every page at the same corner is a logo, and a logo
is slop (§9.11). Its size (92–120px) and corner are seeded per site, then
fixed forever.

**Breakpoints.** All bands: present. <768px: the ring shrinks to 72px and
moves fully inside the corner (the small leaf has no spare paper at its
edge). The darkening curve is identical.

**Edge cases & failure modes.** *Short visit (<10s):* the ring barely
changes — correct; the effect is for readers, not bouncers, and it is
never made faster to be noticed. *Watchdog:* none needed — the ring is a
static SVG with a drifting opacity; if the loop dies, the ring simply
stays at its printed 0.16, which is a complete and valid state. *No-JS:*
printed at 0.18 (mid-visit value) — the finished-page convention of §4.
*Multiple leaves in one session:* the engaged-time clock is per leaf;
each new leaf starts at 0.16 (a fresh cup on a fresh page).

**Accessibility.** `aria-hidden`, no semantics, no alternative text — a
stain is not information. Its opacity range (0.16–0.20) is chosen so it
can never be mistaken for text or reduce the contrast of anything near
it; it is positioned to never underlap text (§10, check 8 verifies the
geometry).

**Tokens.** `--tape-deep` mixed toward `--ink` for the stain colour (a
coffee stain in this palette is read as aged-tape brown at low opacity),
`--ease-bleed` (the long curve), the shared loop's clock.

**Performance & mobile variant.** One SVG ≤1.5KB; the drift writes one
opacity value per second (not per frame) — the loop wakes for it on a
1s tick. Mobile: identical, smaller.

**Reduced motion.** The ring prints at 0.18 and does not drift. (A
darkening stain is motion enough to honour the preference.)

### 6.9 Pencil tallies — days kept, words revised

**What & why.** In the margin, in pencil, the diary keeps score of
itself: **Days kept** — how long this diary has been kept; **Words
revised** — how many corrections the hand has made. The tallies are the
theme's data, and like all data in this theme they must be *true by
construction*: days kept is computed from the diary's printed first-entry
date, and words revised increments only when a correction actually plays
on the page (§6.3's strike, §6.5's bleeds). A counter that performs
counting is a lie in pencil.

**Structure.** A `<div class="m-tallies">` block in the margin, placed
once per leaf at the first margin position, containing two tally rows:
label (Garamond caption, printed — labels are print) and value (Caveat
numerals in `--pencil`, in fixed-width digit cells per §3 law 2). The
block carries the diary's declared record in data attributes:
`data-first-entry="2021-02-14"` and `data-revised-base="1204"` (the
count of revisions made on all previous leaves, printed in the §6.17
tally leaf so any reader can audit the arithmetic).

**Motion spec.** *Days kept* does not animate on scroll: it is computed
at load (today − first-entry date, in days) and printed; on the diary's
home leaf only, it counts up from (value − 30) to value over 1200ms
`--ease-thought` when the tally block first enters view — a keeper
totalling up, not a slot machine. *Words revised* starts each leaf at
base + (corrections already played on this leaf) and increments by
exactly 1 at the midpoint of each §6.3/§6.5 correction performance
(300ms / 420ms marks respectively), each increment a 260ms pencil-write
flicker (the numeral's ink strength dips to 70% and rewrites at the new
value, `--ease-pen`). It never decrements, never counts a replay (§6.5),
and never counts a correction the visitor has not seen play (a
correction below the fold has not happened *for this reader* yet — when
it plays, it counts).

**Choreography timeline.** Days kept: t=0 block enters view · 0–1200ms
count-up (home leaf only) · rest. Words revised: event-driven — each
increment is a 260ms flicker at its correction's midpoint; the final
value a visitor sees equals base + corrections witnessed, and §6.17's
footer restates exactly that figure (the reconciliation the gate audits,
§10 check 3).

**State matrix.** *Rest:* values printed in pencil. *Hover:* the tally
block's label gains a pencilled underline (200ms) and a one-line Garamond
note appears beneath — the audit line: "kept since 14 February 2021 ·
1,204 revisions before this leaf" — provenance on demand. Touch/focus:
tap or keyboard focus on the block (it is focusable as a group,
`tabindex="0"`, with the printed focus rule) shows the same audit line.
*Scrolled-past:* values persist at their current counts. *Disabled:* n/a.

**Content-merge.** The tallies are the diary's own metadata, and they
merge because they are *about this page*: words revised counts this
page's corrections; days kept dates this diary. On sites that are not
literally diaries (an author's book site), the pair translates honestly —
"Years since the first draft" computed from a printed date, "Passages
revised" counted from the page's real corrections — or the element is
omitted. It is never filled with marketing numbers (print runs, readers,
stars): the pencil counts the book's life, not its sales (§9.12).

**Breakpoints.** ≥1200px: margin block as specified. 768–1199px: same,
labels shorten ("Days" / "Revised" — authored short labels, not CSS
clipping). <768px: the tallies move into the leaf's head, as a single
pencil line under the entry title ("day 1,460 · 6 words revised on this
leaf"), updating live as corrections play — on mobile the bookkeeping
rides with the entry, since there is no margin to keep it in.

**Edge cases & failure modes.** *Clock/date issues:* days kept is
computed from the visitor's local date against the printed first-entry
date; if the computed value would be negative or absurd (>100 years),
the build prints the value as of the site's last build date instead and
the audit line says so. *Corrections replayed or skipped by jump
scroll:* jump-scrolled-past corrections (§6.5's jump rule places them
complete) count as played — the reader has "read past" them; corrections
in a leaf the visitor never opens do not count. *Watchdog:* the count-up
is a tween on the shared loop; if interrupted it snaps to the true
computed value by **1800ms** — a tally may never be caught mid-lie.
*No-JS:* both values print at their build-time figures (days kept as of
build date; words revised = base + this leaf's full correction count),
with the audit line present in print.

**Accessibility.** The tally values are text, read in flow. The count-up
and flickers are presentational: assistive tech is given the final
values (the DOM text updates at most once per increment, and the block
is *not* a live region — a screen reader must not be interrupted by
bookkeeping). The audit line is associated via `aria-describedby` on the
focusable block. Pencil contrast 6.42:1 at 20px numerals passes for
large text; the audit note is Garamond ink (13.08:1).

**Tokens.** `--pencil`, `--ink` (labels, audit note), `--ease-thought`
(count-up), `--ease-pen` (increment flicker), `data-first-entry`,
`data-revised-base`.

**Performance & mobile variant.** Negligible: two text nodes and the
shared loop. The date computation is one `Date` diff at load. Mobile:
the single-line variant above; the count-up is cut (values print true)
to keep the entry head calm.

**Reduced motion.** Values print at their true figures; increments
update the numeral instantly with no flicker. The audit line behaves as
in the hover state.

---

### 6.10 Ribbon bookmark progress

**What & why.** A ribbon bookmark — the diary's own sewn-in ribbon —
slides down the margin as the visitor reads, and entries check off in
pencil as they are passed. Progress in this theme is not a percentage or
a bar: it is the reader's place in a book, kept the diary's way. The
ribbon also answers the only progress question a diary reader has: *how
much of this leaf is behind me, and what have I passed?*

**Structure.** A `<div class="m-ribbon">` fixed within the leaf's margin
column: a 14px-wide ribbon strip in `--red` at 82% strength (the one
place red appears without revising — a bookmark ribbon is red by
convention of the object, and §2's rationing counts it inside the 4%),
with a swallow-tail cut at its lower end, sliding inside a faint
pencil-track rule that runs the margin's full height. Beside the track,
each entry/section on the leaf has a pencil check slot (`☐` drawn as a
small SVG box, never an emoji or a font glyph) that ticks as its section
is passed. The whole assembly is `aria-hidden` as graphics, with its
information duplicated in an accessible progress text (see
Accessibility).

**Motion spec.** Scrubbed via the shared loop: ribbon depth = leaf
scroll progress (top of leaf at 90% viewport → bottom of leaf at 40%
viewport maps to track 0→1), lerped at 0.12, `--ease-turn` character in
its glide. Check-offs: when a section's end crosses the reading line,
its box ticks — the tick strokes in over 300ms `--ease-pen` and the
section's margin date (§6.12) deepens from pencil to blue, as if the
keeper noted your passing. No other motion; the ribbon never bounces,
pulses or glows.

**Choreography timeline.** Continuous for the slide (loop-driven, as
§6.4). Per check-off: t=0 section end crosses reading line · 0–300ms
tick strokes · 200ms date deepens · rest. On load mid-leaf (scroll
restoration), ribbon and ticks are placed at their true states instantly
— the keeper kept your place while you were gone, which is what a
bookmark is *for*.

**State matrix.** *Rest (leaf top):* ribbon at track top, no ticks.
*Reading:* ribbon descending, ticks accumulating. *Leaf bottom:* ribbon
at track end, all sections ticked, and the ribbon's tail rests against
the §6.17 tally leaf — the bookmark reaches the bookkeeping. *Hover:*
hovering a tick shows that section's title in Garamond caption (a
printed tooltip on paper, 150ms fade) — the ribbon is also the leaf's
mini-index. Touch: ticks are not touch targets (too small); navigation
belongs to §6.12. *Focus:* the ribbon assembly is not focusable.
*Disabled:* n/a.

**Content-merge.** The ticks are the leaf's real sections, in order,
with their real dates — the ribbon is a table of contents that fills in
as you read. On a leaf with one section, the ribbon still slides (place
in the leaf) but carries no ticks; a ribbon faked over a page with no
structure is a progress bar in a costume (§9.13).

**Breakpoints.** ≥1200px: full assembly in the margin. 768–1199px:
ribbon narrows to 10px, ticks remain (the margin is narrower but the
bookmark is the margin's spine — it is the last thing cut).
<768px: the margin is gone, so the ribbon moves to the leaf's left edge
as a 5px strip with no ticks and no track rule — place-keeping only;
section progress on mobile is carried by §6.12's dated index at the
leaf's head. 

**Edge cases & failure modes.** *Short leaf (less than one viewport of
scroll):* the ribbon is placed at its end state with all ticks ticked —
a one-page entry has been read by being seen. *Watchdog:* loop-driven;
if the loop dies the ribbon freezes mid-track, which misstates progress
— so the ribbon's fallback differs from §6.4's: a 3000ms heartbeat
checks loop liveness, and on failure the ribbon assembly hides itself
entirely (a missing bookmark is honest; a frozen one is a lie). *Print:*
the ribbon does not print (bookmarks are not part of the page); ticks
print as part of §6.12's index instead.

**Accessibility.** The assembly is decorative duplication: an
`role="progressbar"` equivalent is provided as visually-hidden text
("Reading: section 3 of 5, ‘The Garden’") updated at section boundaries
only (not per scroll frame). Keyboard users navigate by headings and by
§6.12's index; the ribbon never holds information they cannot get in
print.

**Tokens.** `--red` (ribbon), `--pencil` (track, ticks), `--blue`
(ticked dates), `--ease-turn`, `--ease-pen`, the shared loop +
heartbeat.

**Performance & mobile variant.** One transform on the ribbon per frame
from the shared loop; ticks are tiny SVG paths drawn once each. Mobile:
the 5px strip variant — a single transform, nothing else.

**Reduced motion.** The ribbon is placed at the true depth for the
current scroll position and updates by step (on section change) rather
than gliding; ticks appear fully drawn. Place is kept; travel is not
performed.

### 6.11 The opening entry (hero)

**What & why.** The leaf opens the way a diary day opens: the date,
written by hand in blue at the top; then the day's entry *types itself*
— calmly, in print, the one licensed exception to §3 law 5 — because
this is the keeper writing today's page in front of you. A red circle
(§6.2) around one phrase and the first margin note (§6.1) complete the
entrance: print, then judgement, then thought, in that order, every
time.

**Structure.** A `<header class="m-opening">` at the leaf's head: the
date line (Caveat, blue, real text), the entry title (Garamond, §3),
the entry's first paragraph (the typing paragraph — its full text in the
DOM from first paint, presented via a per-word reveal mask on two
presentational duplicate layers exactly as §6.5 protects its words), a
primary action set in print (the diary's one invitation — e.g. "Read
from the beginning" / "Yesterday's entry" as Garamond links with
hand-drawn underlines, §6.12), and the margin's first note slot. On
non-home leaves, the opening is shorter: date and title only, no typing
(the keeper writes once a day, not once per page).

**Motion spec.** Entrance sequence, first load of the session only
(a `sessionStorage` flag suppresses replay on later leaves — the day is
written once): date writes in per §6.1's stroke system, 500ms · title
fades/rises 8px over 500ms `--ease-thought` at +200ms · the entry types
at a calm 28–34 words per minute equivalent in *word groups* (the reveal
advances phrase by phrase, 90–140ms per group, never letter-by-letter —
typing letter by letter is a typewriter costume; a hand composing print
thinks in phrases) · at completion, §6.2's circle scribbles around the
chosen phrase · 600ms later the first margin note writes itself (§6.1).
Total entrance ≤4200ms for a 60-word opening paragraph; longer openings
type faster per group, never slower overall.

**Choreography timeline** (t=0 first paint, home leaf): 0ms leaf and
date present (date at 0% ink) · 100–600ms date writes · 300–800ms title
settles · 700ms typing begins · 700–3700ms phrases reveal · 3700ms
typing complete, print at full strength · 3800–4500ms §6.2 circle
scribbles · 5100ms first margin note begins (§6.1's own delay honoured
from the paragraph's completion) · entrance ends; the page is now simply
a diary being read.

**State matrix.** *Rest (returning visitor / later leaves):* everything
present, finished, no performance — the diary opened at today's page.
*During entrance:* actions are live from t=0 (the links work while the
entry types; the performance never blocks input). *Hover/focus:* per
§6.12's link rules. *Scrolled during entrance:* if the visitor scrolls
past the opening before it completes, all remaining beats snap to
finished instantly — nobody is made to watch a page write itself.
*Disabled:* n/a.

**Content-merge.** The opening entry is real content — today's actual
entry, not a hero slogan. Its circled phrase is the day's turning point
(§6.2's law), its first note is the day's first second thought. A build
whose "hero" is a marketing headline wearing a date has inverted the
theme: in a diary, the entry is the hero (§9.14).

**Breakpoints.** ≥1200px: full sequence. 768–1199px: typing cap tightens
to ≤3200ms. <768px: the date and title appear finished; the typing is
replaced by a 400ms phrase-group fade of the whole paragraph (the small
screen gets the day's entry immediately — a phone reader is usually in
a hurry, and the diary respects it). Circle and note proceed as normal.

**Edge cases & failure modes.** *Watchdog:* a **4200ms** hard ceiling —
at 4200ms every layer is in its finished state regardless of beat
progress. *No-JS:* the finished opening ships in the HTML (date written,
entry printed, circle drawn statically). *Slow font load:* typing waits
for `document.fonts.ready` up to 800ms, then proceeds with fallback
metrics and re-fits the circle on font arrival (§6.2's rule). *Session
flag unavailable (private mode):* the entrance plays once per leaf —
acceptable degradation, noted in §14's cut order as the first thing to
simplify if budgets tighten.

**Accessibility.** The full entry text is in the DOM from first paint;
the typing is presentational layering (`aria-hidden` duplicates) over a
visually-masked but AT-available original — screen readers read the
entry once, in full, immediately. The date is text. The entrance is
skipped entirely under reduced motion *and* for any visitor arriving
with a fragment link into the leaf (they came for a passage, not a
performance).

**Tokens.** `--blue` (date), `--ink`, `--red` (circle), `--ease-thought`,
`--ease-pen`, the §6.1/§6.2 systems.

**Performance & mobile variant.** The typing layers are two text
duplicates of one paragraph — cheap. The session flag is one storage
read. Mobile: the fade variant above; no stroke SVG for the date (ink
rise instead), halving the entrance payload.

**Reduced motion.** The finished opening, instantly: date written, entry
printed, circle drawn, note present. Nothing types, nothing scribbles.

### 6.12 Margin navigation — the dated index

**What & why.** A diary is navigated by its dates. The theme's
navigation is the keeper's own index, written inside the front of the
book: a list of entries by date and title, in print, with the current
entry's date circled in red by the hand and a pencilled tick beside
entries the visitor has already read this session. It is navigation that
admits what it is — a contents list in a book — instead of a menu bar
wearing a paper texture.

**Structure.** A `<nav class="m-index">` placed at the leaf's head
(below the opening on the home leaf; at the top of archive leaves)
containing: the site title as a printed bookplate line (Garamond, small
caps by letter-spacing, never a logo image), the entry list (date in
blue Caveat at 17px + title in Garamond, one line each, most recent
first, grouped under printed month rules), the standing pages (About the
keeper, The tally leaf, Write in the margin) set in Garamond as a
printed colophon row, and the current-position marker: the current
entry's date circled by a small static red loop (SVG, drawn at build —
navigation does not perform). Read-state ticks are §6.10's pencil ticks
reused at index scale.

**Motion spec.** Almost none, deliberately: navigation in a diary is a
place, not an event. Link hover: a hand-drawn underline (SVG path,
pre-drawn per link at build) fades in over 180ms `--ease-bleed` — the
keeper underlining where you might go. The index itself never animates
on load. On mobile the index collapses to a "Contents" printed line that
expands (300ms `--ease-turn` height glide) to the same list — same
content, same order, never a hamburger glyph: the word *Contents* is
the button, set in Garamond with a pencilled down-mark.

**Choreography timeline.** No entrance beats. Hover underline: 0–180ms
fade. Mobile expand: 0–300ms glide, links focusable only when expanded
(focus is placed on the first link when opened by keyboard, returned to
the Contents line on close).

**State matrix.** *Rest:* list printed, current date circled. *Hover
(link):* hand underline fades in; the link's date deepens blue 7.16→
full strength. *Focus:* the same underline at full strength plus a
printed 2px focus rule beneath (keyboard visitors get both the hand's
mark and an unambiguous printed indicator). *Active (current page):*
the entry's row is the current one — circled date, title in full ink,
and `aria-current="page"`; it is not a link. *Read entries:* pencilled
tick at 60% pencil strength (session-scoped, honest: it means "read on
this visit", and the index's caption says exactly that). *Disabled:* n/a.

**Content-merge.** The index *is* the site's real structure — every
entry, in the keeper's own order (chronological, because a diary's order
is time). A build that shows only "featured" entries in the index has
made a menu, not an index (§9.13). Long archives group by month with
printed month heads; the grouping is content, authored, not a filter
widget.

**Breakpoints.** ≥1200px: the index sits in the margin column's head
zone on the home leaf, and as a full-width contents leaf on archive
pages. 768–1199px: full-width at the leaf's head, two-column list.
<768px: the collapsed Contents line + expand behaviour above.

**Edge cases & failure modes.** *Very long index (100+ entries):*
grouped by year with printed year heads; years beyond the current are
collapsed as *printed summaries* ("2023 — 41 entries" as a link to that
year's leaf) — the index never becomes an infinite scroll. *No-JS:*
the full list is present and expanded (the mobile collapse is
JS-armed). *Watchdog:* the underline fade is a CSS transition; no
watchdog required — its failure state is "no underline", a valid diary.
*Session ticks unavailable (storage blocked):* ticks simply never
appear; nothing else changes.

**Accessibility.** A real `<nav>` with a real list; `aria-current` on
the present entry; the circled date is decorative duplication of
`aria-current` (SVG `aria-hidden`). Focus order = list order. The
Contents toggle is a `<button>` with `aria-expanded`. All links are
Garamond ink or blue at ≥7.16:1; the hand underline is never the sole
indicator of anything.

**Tokens.** `--ink`, `--blue`, `--red` (current circle), `--pencil`
(ticks), `--ease-bleed`, `--ease-turn`.

**Performance & mobile variant.** Static HTML; the per-link underline
SVGs are one shared path reused by reference (≤0.4KB total). Mobile: the
collapse variant — the only JS the nav owns.

**Reduced motion.** Underlines appear/disappear instantly; the mobile
expand is instant. Content and order unchanged.

---

### 6.13 Pressed-flower dividers

**What & why.** Between the diary's major sections, the keeper has
pressed a flower — a real specimen, flattened, kept from a day the entry
mentions. It is the theme's section divider: not a rule, not an ornament
font, but a kept thing, with a pencilled label naming what it is and when
it was picked. A divider in this diary is a pause the keeper *saved*,
and it earns its place by being specific: this flower, from that day in
the text above.

**Structure.** A `<figure class="m-flower">` spanning the text column at
section boundaries: one inline SVG flower (stem, two leaves, 5–7 petals
in `--flower` at layered opacities 0.85/0.6, drawn pressed-flat — slight
asymmetry, one petal folded, never a symmetrical icon), a hairline of
`--rule-line` passing *behind* it (the flower lies on the page, over its
lines), and a pencilled caption (Caveat, `--pencil`, 17px) beneath:
species and date — "violet, from the garden wall, 3 May". One flower per
spread (§2's census), and different spreads press different flowers.

**Motion spec.** Arrival: as the divider crosses the reading line, the
flower *settles* — opacity 0→1 and a 2px descent over 700ms
`--ease-thought`, as if the page's weight just came onto it — and the
caption writes in by §6.1's ink-rise (mobile form) over 400ms, delayed
200ms. That is all. The flower never sways, spins or blooms; a pressed
flower that moves is a fresh flower, and the fiction breaks.

**Choreography timeline** (t=0 divider at reading line): 0ms flower
begins settle · 0–700ms opacity/descent · 200–600ms caption ink rises ·
700ms rest. On scroll-up return: rest state, no replay.

**State matrix.** *Rest:* flower pressed, caption written. *Hover:* the
caption deepens pencil→ink over 240ms (reading the label closely);
nothing else moves. Touch: same on tap. *Focus:* not focusable; the
caption is plain text in flow. *Scrolled-past:* rest. *Disabled:* n/a.

**Content-merge.** The flower must come from the entry it divides — the
text above mentions the garden, the walk, the bouquet — and the caption's
date must be a date inside the diary's own chronology (it joins §6.9's
audit world: a flower dated before the first entry is a continuity
error the gate catches, §10 check 10). A divider chosen from a clip-art
set, unrelated to the text, is the theme's prettiest slop (§9.15) and is
cut.

**Breakpoints.** ≥1200px: flower at 120–150px tall, centred on the text
column with the margin left empty (the pause is total). 768–1199px:
100px. <768px: 84px, caption beneath at 16px. The hairline spans the
text column only at every band.

**Edge cases & failure modes.** *No authored flower for a boundary:*
the divider degrades to the honest minimum — three blank ruled lines
and a pencilled date alone (a pause the keeper marked but kept nothing
from). Never substitute a generic flower. *Watchdog:* the settle is a
transition; by **1400ms** the flower is at rest regardless. *No-JS:*
flower and caption present at rest.

**Accessibility.** The figure's caption is its text alternative; the SVG
is `aria-hidden` with the caption as the accessible name of the figure.
The flower conveys no information the caption lacks. Colour: `--flower`
on paper is ~3.9:1 — a graphic, not text; the caption is pencil at 17px
(6.42:1 at its size — permitted under §2's rationing for labels, and it
deepens to ink on hover/focus-within for close reading).

**Tokens.** `--flower`, `--pencil`, `--rule-line`, `--tape-deep` (stem),
`--ease-thought`, `data-seed` (which petal folds).

**Performance & mobile variant.** One SVG ≤6KB per divider, ≤2 dividers
per leaf. Mobile: same file, smaller render — no separate asset.

**Reduced motion.** Flower and caption present at rest; no settle.

### 6.14 Entry cards — the archive's pasted slips

**What & why.** On listing pages (the archive of entries), each past
entry is represented the way a diary represents anything kept: a pasted
slip — a small leaf fragment carrying the entry's date, its first printed
line, one taped thumbnail where the entry has a photo, and, on some
slips, the single margin note the keeper later added to that entry. The
card is a *clipping from the book*, and clicking it opens the entry's own
leaf. This is the theme's card: it summarises by excerpting, never by
abstracting into metadata tiles.

**Structure.** An `<article class="m-card">` styled as a cut slip: paper
ground (one shade off the leaf, `--paper-deep` edge on its lower side to
read as thickness), a strip of `--tape` across its top edge printed with
the entry's date in ink (the §2 licensed on-tape label, ink at 5.65:1),
the entry title in Garamond 22px, its first line in Garamond italic, an
optional §6.6-style thumbnail (two tape corners only), an optional single
Caveat note (≤10 words, blue or red by its kind), and a whole-card link
to the entry. Cards sit in a loose grid with seeded rotations of −0.8°
to +0.8° — pasted, not tiled.

**Motion spec.** Entrance: cards arrive as the list scrolls — each
presses in over 450ms `--ease-press` (a 3px descent + rotation to seed)
staggered 70ms apart in reading order, at most 6 animating at once;
beyond that they appear placed. Hover: the card lifts its lower-right
corner (the §6.6 lift, 2px, 280ms) and its tape strip's date deepens.
No other motion: an archive is browsed, not performed.

**Choreography timeline** (per card, t=0 card at 78% viewport): 0ms
press begins · 0–450ms descent/rotation · 450ms rest. List-level: the
stagger is by DOM order, capped as above; jump scroll places all cards
above the fold instantly at rest.

**State matrix.** *Rest:* slip pasted, date on tape. *Hover:* corner
lift + date deepens (above). *Focus:* the card's link shows the printed
focus rule around the whole slip — a card is one link, one focus target.
*Active:* n/a (the current entry does not appear as a card on its own
leaf). *Visited:* a card for an entry read this session carries §6.12's
pencilled tick on its tape strip. *Disabled:* n/a. *Touch:* no hover
states; tap = open.

**Content-merge.** Every field is the entry's own: real date, real first
line (never a written-for-the-card teaser), real note if one exists —
and if an entry has no note and no photo, its slip is plainer, which is
honest: some days the keeper only wrote. Cards that all carry identical
decoration (a note *and* a photo *and* a circle, every time) are a
template showing (§9.16).

**Breakpoints.** ≥1200px: grid of 3 columns across the leaf's full
width (cards may lean across the margin line as photos do). 768–1199px:
2 columns. <768px: 1 column, rotations halved (±0.4° — a narrow screen
makes big tilts look broken, not pasted), thumbnails at card width.

**Edge cases & failure modes.** *Long first lines:* the slip prints the
entry's first *sentence*, authored in the content model — CSS line-clamp
is forbidden (a clamped sentence with an ellipsis is a torn slip, and
not in the good way). *Missing thumbnail:* no placeholder box; the slip
is text-only and slightly narrower in the grid's flow. *Watchdog:* the
press-in is a transition; cards snap to rest by **1000ms** after trigger.
*No-JS:* all cards at rest, fully linked.

**Accessibility.** One link per card with a proper accessible name
(entry title + date). The tape date is real text. Rotation never
reduces readability (≤0.8°). Focus rule contrast: ink on desk/paper
passes; the rule is 2px printed ink.

**Tokens.** `--paper`, `--paper-deep`, `--tape`, `--ink`, `--blue` /
`--red` (note), `--ease-press`, `data-seed` (rotation).

**Performance & mobile variant.** Thumbnails ≤40KB each, lazy; the
press-in is transform/opacity only. Mobile: single column, half
rotations, stagger cut (cards appear placed beyond the first three).

**Reduced motion.** Cards placed at rest; hover lift removed; all
content identical.

### 6.15 The margin-letter form — "Write in the margin"

**What & why.** The theme's one conversion: a visitor may write in the
diary's margin — leave a letter for the keeper (a comment, a
subscription to new entries, a message on a wedding-story site). The
form is a pasted-in slip on the leaf: ruled lines for fields, the
visitor's words set in Caveat as they type (their handwriting, in the
diary), and on sending, the slip is taped into the margin and the keeper
answers with a note. It converts because it *admits the visitor into the
book* — the only honest conversion a diary can offer. It is a letter,
never a checkout (§1).

**Structure.** A `<form class="m-letter">` on its own slip (paper,
seeded rotation −0.5°, two tape corners at its head): fields Name,
Email (or "where the reply should find you"), and Your note — each a
single ruled line (an `<input>`/`<textarea>` with no box: bottom rule in
`--rule-line`, deepening to `--blue` on focus) with printed Garamond
labels above the line. Typed text renders in the fields in Caveat 20px
ink — the visitor writes by hand, in blue. The submit is a printed
Garamond link-styled button, "Leave it in the margin", underlined by
hand (§6.12's underline at rest). Validation messages are written by the
keeper in the margin beside the field, in red pencil Caveat — an editor
correcting a form, kindly.

**Motion spec.** Focus: the field's rule deepens and a faint blue
ink-glow (a 2px `--blue` wash under the line) spreads over 240ms
`--ease-bleed`. Typing: no per-key animation (the hand is the visitor's
own). Error: on submit with a fault, the slip shakes once — 240ms, two
4px oscillations, `--ease-thought` — the keeper tapping the page, and
the red note beside the faulty field writes in per §6.1's stroke system
(cap 800ms). Submit success: the form slip presses (as §6.14, 450ms
`--ease-press`), its tape corners settle (§6.6), the slip slides 12px
into the margin over 500ms `--ease-turn`, and the keeper's reply note
writes itself in the margin beside it over 900ms: "Thank you. I read
every word left here. — M." (the site's own keeper initial and words,
authored per site; the structure is fixed, the words are the site's).

**Choreography timeline** (success path, t=0 submit): 0ms slip press
begins · 0–450ms press + tape settle · 300ms slide into margin begins ·
300–800ms slide · 800ms reply pen-down · 800–1700ms reply writes ·
1700ms rest: the letter is *in the book*, and a printed line beneath
confirms what happened in plain Garamond ("Your note is in the margin.
Replies come by post — usually within the week." — the site's real
reply practice, stated in print, because a promise is print's job).

**State matrix.** *Rest:* empty slip, rules pale. *Focus (field):*
rule deepens, wash spreads. *Filled:* text in Caveat blue; the slip's
rotation straightens by 0.2° (a letter being written on is held flat).
*Error:* shake + red keeper note per faulty field; the visitor's text
is never cleared by an error — a diary does not eat letters.
*Submitting:* the button's underline draws twice (a hand underlining
"wait") for the duration; fields disable at the moment of send only.
*Success:* as choreographed; the form is replaced by the pasted slip +
reply (the slip remains visible for the session, with the visitor's own
words in it). *Failure (network):* the slip stays put, a red margin
note writes: "The post failed. Your words are still here — try again."
with a printed retry link; nothing is lost.

**Content-merge.** The form merges because its product is *an artefact
in the theme's world*: the visitor's note becomes a pasted slip in the
margin, answered by the keeper's hand. The fields are the minimum a
letter needs. Any build that adds marketing fields (company, phone,
"how did you hear about us") has turned the letter into a CRM capture
and broken the world (§9.17).

**Breakpoints.** ≥1200px: the slip sits across the text column leaning
into the margin; success slides it fully into the margin column.
768–1199px: slip full text-column width; success slide is 8px, reply
note beneath the slip. <768px: slip full width, rotation 0 (a letter on
a phone is written straight), success: no slide — the reply note writes
beneath the slip in place.

**Edge cases & failure modes.** *Watchdog:* the success sequence is
capped: if any beat stalls, by **3000ms** the slip and reply are in
their final states (reply as static Caveat text). *No-JS:* the form is
a normal form posting to its endpoint; the success page is a printed
confirmation leaf (the pasted-slip performance is an enhancement, the
letter itself is not). *Spam/honeypot:* invisible and unthemed — the
diary does not discuss its locks. *Long notes:* the textarea grows by
ruled lines (the slip lengthens); beyond ~600 words the printed label
gently notes the margin's size and offers the site's email instead —
in print, before the visitor writes a novel into a margin.

**Accessibility.** Real labels (printed, associated), real validation
(errors as text beside fields *and* in an `aria-describedby` chain; the
shake is never the only signal). The keeper's red notes are Caveat at
20px — red on paper is 8.97:1, passing even in handwriting. Focus order
is field order; after an error, focus moves to the first faulty field.
The success confirmation is a polite live region in print (the
Garamond line), not the handwritten reply (which AT reads as ordinary
text in flow).

**Tokens.** `--paper`, `--tape`, `--rule-line`, `--blue`, `--red`,
`--ink`, `--ease-bleed`, `--ease-press`, `--ease-turn`, `--ease-pen`.

**Performance & mobile variant.** The form owns no heavy assets; its
stroke SVGs (error notes, reply) are generated from the same §6.1 path
system, ≤4KB. Mobile: rotation 0, no slide, reply beneath — the letter
still lands in the book.

**Reduced motion.** No shake (errors are stated, not shaken), no slide:
the success state appears finished — slip taped, reply written — with
the printed confirmation line. Validation notes appear as static
Caveat.

---

### 6.16 The leaf turn — page transition & ruled skeleton

**What & why.** Moving between entries turns a leaf. The transition is
the book's own mechanics: the current leaf's right edge lifts and sweeps
across, the next leaf is beneath it. While a leaf loads, the visitor
sees not grey bars but an *unwritten leaf*: the ruled lines, a pencilled
date ghost, and three faint pencil lines where the entry will be — the
diary before the day is written. Loading in this theme is an empty page,
not a spinner (a diary has no spinner; it has mornings).

**Structure.** Transition: a `<div class="m-turn">` overlay shaped as a
leaf (paper gradient, a darker gutter edge at its left, a soft shadow at
its leading edge) that sweeps right-to-left over the current leaf on
navigation, with the new content swapped beneath at full cover.
Skeleton: the new leaf's own DOM in its unwritten state — printed
rule-lines (the real §4 background), a date line in `--pencil` at 40%
strength, and 3–5 "pencil ghost" bars (rounded 6px bars in `--pencil`
at 18% strength, widths seeded 62–94% of the measure) standing where the
first paragraph will be, plus the margin empty. The skeleton is the real
page's chrome, not a separate mock.

**Motion spec.** Turn: on internal navigation, the leaf sweeps in
260ms `--ease-turn` to full cover; content swaps; the leaf sweeps away
(revealing from the left, as a turned page settles) in 340ms
`--ease-turn`. **Hard ceiling 700ms total**; navigations that cannot
cover within the ceiling (slow fetch) hold at full cover with the
skeleton leaf beneath the covering leaf's edge — the visitor waits
looking at an unwritten page, never at a frozen half-turn. Skeleton
ghosts do not shimmer (paper does not shimmer); they rest, with one
slow pencil-line drawing itself across the first ghost over 2400ms
`--ease-pen`, looping only while loading persists beyond 2400ms.

**Choreography timeline** (t=0 navigation): 0ms turn begins · 260ms
full cover, swap · 260–600ms reveal sweep · 600ms new leaf at rest (its
own entrance rules apply — §6.11 only on the home leaf, and its session
flag usually suppresses it). Skeleton path: 0ms unwritten leaf shown ·
ghost line draws 0–2400ms if loading persists · on content arrival,
ghosts fade 200ms as the real entry prints in beneath them (print
arrives fully formed; it does not type — §3 law 5).

**State matrix.** *Rest:* no overlay; leaf readable. *Turning:* as
above; the current leaf remains interactive until cover passes 60%
(clicks during the first 150ms cancel the turn — a reader who grabs the
page keeps it). *Loading:* skeleton state. *Error (navigation fails):*
the covering leaf retreats the way it came (300ms) and a red margin
note on the *current* leaf states the failure in the keeper's voice
("That page wouldn't turn. Stay here a while.") with a printed retry
link. *Disabled:* n/a.

**Content-merge.** The turn merges because it *is* the site's
information architecture made physical: entries are leaves, moving is
turning. It is licensed only between leaves of the diary — never to an
external site, never out of the §6.15 form's submission (a letter is
posted, not turned to), and never within a leaf (anchor jumps are
instant; the keeper does not turn a page to move down it).

**Breakpoints.** ≥1200px / 768–1199px: full turn. <768px: the sweep
shortens (180ms + 240ms) and the leaf shadow is cut — small screens turn
pages quickly. The skeleton is identical at all bands (it is the page's
own chrome).

**Edge cases & failure modes.** *Watchdog:* a **3000ms** abort — if the
new content has not arrived and swapped by 3000ms, the turn completes
anyway onto the skeleton leaf (which then resolves or errors per its
own rules); a visitor is never held under a covering leaf longer than
3s. *Back/forward & scroll restoration:* browser-native turns are
instant (no sweep) with scroll restored — the keeper does not perform
for the browser's own navigation. *No-JS:* ordinary page loads; the
skeleton never appears (content is server-rendered); the theme's pages
must be fully readable as static leaves (§4). *Prefetch:* likely-next
leaves (the index's neighbours) may prefetch so the turn's ceiling is
rarely tested.

**Accessibility.** The turn is presentational; AT is given the new
page's title via the normal document navigation (in an SPA build, an
`aria-live` announcement of the new entry's title at swap, and focus
moves to the new leaf's heading). The skeleton's ghosts are
`aria-hidden`; a visually-hidden "Loading the next entry" text serves
AT during loads over 600ms. No content is ever *only* under the
covering leaf for AT users.

**Tokens.** `--paper`, `--paper-deep`, `--pencil`, `--rule-line`,
`--ease-turn`, `--ease-pen`.

**Performance & mobile variant.** The overlay is one gradient div +
shadow (compositor transform only). The skeleton costs nothing (it is
the page chrome). Mobile: the shortened sweep above; skeleton ghosts
reduced to 3.

**Reduced motion.** No sweep: navigation swaps instantly (a brief
120ms paper-colour fade is permitted but not required). The skeleton
shows its ghosts statically, the pencil line pre-drawn.

### 6.17 The tally leaf — footer

**What & why.** The diary ends, as diaries do, with the back page where
the keeper keeps the record: the tallies restated in full, the book's
colophon, and the standing information of the site (about the keeper,
contact, the index) set as a printed back page. The footer is the third
printing of the diary's numbers — §6.9's margin tallies and the audit
line are restated here *in print*, as the permanent record, so the
page's arithmetic can be checked end to end.

**Structure.** A `<footer class="m-tallyleaf">` on the same leaf (the
leaf does not end; its last ruled section is the record): a printed
rule, then three columns of Garamond small print — (1) *The record:*
first entry date, days kept (final value for this leaf), words revised
before this leaf (the base), words revised on this leaf (the count of
§6.3/§6.5 corrections), and their sum — the exact figure §6.9's margin
tally must show; (2) *The book:* colophon — who keeps this diary, the
site's standing pages (§6.12's list repeated in print), the year line;
(3) *The desk:* the site's practicalities — contact, the letter form's
link (§6.15), any required legal lines, set plainly in print (legal
text is never handwritten, §1). A final pencilled line closes the leaf:
the keeper's sign-off, in Caveat pencil — e.g. "— kept, so far." — the
only footer handwriting, and it is a signature, not information.

**Motion spec.** None on arrival: the record does not perform. The one
motion: when a correction plays above (§6.3/§6.5) and the footer is on
screen, the "on this leaf" figure updates with §6.9's 260ms pencil
flicker, in sync with the margin tally — two printings of one number,
changing together. Hover on the record column underlines the audit
figures' sources (the dates) with the hand underline (§6.12).

**Choreography timeline.** Event-driven only (the flicker, 260ms, at
each correction's midpoint, shared with §6.9). No entrance beats: a
visitor who scrolls straight to the back page finds the record already
kept, showing this leaf's corrections counted as played-if-passed per
§6.9's jump rule.

**State matrix.** *Rest:* record printed, sums correct. *Updating:*
flicker as above. *Hover:* source underlines. *Focus:* the footer's
links take §6.12's rules; the record figures are not focusable (the
audit line in §6.9 is the interactive provenance). *Disabled:* n/a.

**Content-merge.** The footer merges because it is the diary's own back
page — the record of *this book*, not a sitemap in a paper hat. Its
numbers are this site's real bookkeeping (§6.9), its colophon names the
real keeper, its legal lines are the site's real ones. A footer that
carries a newsletter signup duplicates §6.15 and breaks the world: the
diary has one way to write to it, at the letter slip, not in the back
page.

**Breakpoints.** ≥1200px: three columns. 768–1199px: two columns
(record + book; desk beneath). <768px: one column, record first — the
numbers are the point of the page's end.

**Edge cases & failure modes.** *Arithmetic drift (a bug makes margin
and footer disagree):* the build's gate (§10 check 3) recomputes from
the DOM and fails the build — the footer never ships a sum it cannot
prove. *No corrections on the leaf:* "words revised on this leaf: 0" is
printed as a true zero (an unrevised day is a fact, not an
embarrassment to hide). *No-JS:* all figures at build-time values, sums
correct as printed. *Watchdog:* none — static print with one shared
flicker.

**Accessibility.** Plain semantic footer, headings in print, figures as
text. The flicker is presentational; AT reads final values (not a live
region). The pencilled sign-off is decorative text in flow — harmless,
read as part of the page's end, which is where a signature belongs.

**Tokens.** `--ink`, `--pencil`, `--rule-line`, `--ease-pen` (flicker).

**Performance & mobile variant.** Static text. Mobile: the stacked
variant above.

**Reduced motion.** Figures update instantly, no flicker. All else
identical — the record at rest is the record.

### 6.18 The torn page — 404

**What & why.** A page that does not exist in this diary was *torn
out*: the leaf the visitor reaches shows the stub of the missing page —
a ragged paper edge — the entry before it and the entry after it (the
diary continues on both sides of the loss), and the keeper's note
admitting the gap. A diary's 404 is honest about what a 404 is: something
was here, or was meant to be, and is not. It is the theme's
missing-leaf page, and its choreography is specified as *almost none* —
a torn page does not perform.

**Structure.** A leaf whose text column holds: a printed heading in
Garamond — "This page was torn out." — the stub: a 26px vertical strip
of `--paper-deep` with a seeded ragged edge (SVG path) at the leaf's
gutter side, the keeper's note in blue Caveat in the margin ("I don't
remember tearing this one. — or the address is wrong." — the site's own
words, but the structure admits both possibilities: the page is gone or
the visitor was misdirected), and the two neighbouring entries as
§6.14 slips ("the page before" / "the page after", from the real index
order around the requested path where determinable, else the latest
entry and the first entry). A printed line offers the index (§6.12) and
the home leaf.

**Motion spec.** One beat only: on arrival, the stub's ragged edge
casts its shadow in over 600ms `--ease-bleed` (the page settling after
being turned to, roughly). Nothing else moves, ever. No circle, no
notes writing — the keeper has nothing to say about a page that is not
there, beyond the one blue admission.

**Choreography timeline.** t=0 leaf present complete · 0–600ms stub
shadow settles · rest, permanently.

**State matrix.** *Rest:* as built. *Hover/focus:* the neighbour slips
and index link take §6.14/§6.12 rules. *All other states:* n/a — a
missing page has no lifecycle.

**Content-merge.** The neighbours are real entries from the real index;
the admission is the site's real voice; the stub is the theme's material
honesty about absence. A 404 that jokes with clip-art or hides the loss
behind a search box as the first element has left the diary (§9.18).

**Breakpoints.** All bands: same leaf; <768px the stub strip narrows to
16px and the margin note moves beneath the heading (per §4's mobile
margin rule).

**Edge cases & failure modes.** *Unknown neighbours (deep link from
outside, no referrer structure):* the fallback pair is the most recent
entry and the diary's first entry — labelled as such ("the latest page"
/ "the first page"), never disguised as true neighbours. *Watchdog:*
none (no performance to strand). *No-JS:* identical — the 404 is a
static leaf by design at every layer.

**Accessibility.** The heading states the situation in print, first.
The keeper's note is text. The stub SVG is `aria-hidden`. Status is a
real 404 from the server — the theme never soft-404s a torn page into a
200.

**Tokens.** `--paper-deep`, `--ink`, `--blue`, `--ease-bleed`,
`data-seed` (ragged edge).

**Performance & mobile variant.** The lightest page on the site: one
small SVG, no stroke systems, no loop (the shared loop is not even
started here — a torn page does not need a clock). Mobile: as above.

**Reduced motion.** The shadow is printed settled. Identical otherwise.

---

## 7. Page application map

| Page type | How the theme plays out |
|---|---|
| **Home — today's leaf** | The full diary day: §6.11 opening entry (typing, circle, first note), §6.9 tallies in the margin, §6.10 ribbon tracking the leaf, entries below today's with their §6.1 notes, §6.5 corrections and §6.6 photos as authored; one §6.3 confession and one §6.7 pinned spread at most; §6.8's ring at the corner, darkening; §6.17 closes the leaf. This is the only leaf where the entrance performs. |
| **Entry (detail) — a past leaf** | Same leaf system without the entrance: date and title printed, §6.2 circle where the entry has its turning point, notes/corrections/photos as authored, ribbon tracking, tallies showing the diary's totals with "on this leaf" counts for this entry's corrections, §6.14 slips for the previous/next entries at the foot above §6.17. |
| **Archive (listing) — the index leaves** | §6.12's dated index in full (grouped by month/year) and/or §6.14 pasted slips in their loose grid; no confession, no pin, no typing — an archive is browsed with the hand mostly still; the ring does not appear (archive leaves carry no live ring, §6.8); tallies print as the diary's totals only. |
| **About — the keeper's page** | A leaf written *about* the hand: the keeper's printed account, one §6.6 photo (the desk, the keeper's hands — never a stock portrait), margin notes in the keeper's voice answering the printed claims ("mostly true." / "she exaggerates the garden."), §6.9 tallies given their fullest audit (the first entry reproduced as a §6.14 slip). The page where the fiction explains itself without breaking. |
| **Contact / subscribe — the letter leaf** | §6.15 alone on a leaf: a short printed invitation, the letter slip, and beneath it two or three past letters (with their writers' permission, names as given) pasted as slips with the keeper's replies — social proof in the theme's own material. No other form exists on the site. |
| **404 — the torn page** | §6.18, exactly as specified: stub, admission, neighbours, index. |
| **Search / utility pages** | Not licensed. A diary has no search page; find-in-page and the index serve. Any utility a real site needs (account, settings) leaves the diary and uses a plain printed surface — Garamond on paper, no hand — rather than forcing the margin to annotate a password form (§1, when NOT to use). |

---

## 8. Worked examples

One fictional but fully-audited diary runs through all three examples:
the diary of **M.**, a memoirist, first entry **14 February 2021**
(printed on the tally leaf). "Today" in the examples is **Thursday,
13 February 2025** — the eve of the diary's fourth anniversary. Days
kept, computed: 14 Feb 2021 → 14 Feb 2025 is 1,461 days (365 + 365 +
365 + 366, the leap day of 29 Feb 2024 falling in the last span); one
day earlier, today, is **day 1,460**. Words revised before this leaf:
**1,204** (the printed base). Every figure below traces to these.

### 8.1 The hero — today's opening entry (§6.11, §6.2, §6.1, §6.9)

**The leaf's head.** Blue Caveat date, written on load: *"Thursday, 13
February — the night before the fourth year."* Title in Garamond 40px:
**On Keeping**. The opening paragraph types itself, phrase by phrase:

> "Four years ago tomorrow I bought this book to prove I could keep
> one true thing a day. I have kept every day since — some days only
> just, and some days only the date — but the book has no gaps, and
> neither, on paper, do I."

The circled phrase (§6.2) is **"the book has no gaps"** — the entry's
turning point, because the rest of the entry is about the one day that
nearly was a gap. The first margin note (§6.1, blue, arriving 600ms
after the paragraph settles) reads: *"bought it at the station, of all
places. 2019 prices."* — and the word **2019** in the *printed* text of
the second paragraph is one of the leaf's bleed corrections (§6.5): the
keeper first printed 2019, then bled it to **2021** (blue — a fact).
The margin tallies (§6.9) sit at the first margin position: *Days kept
1,460* (counting up from 1,430 on this home leaf), *Words revised
1,204* — which will not stay 1,204 for long, because this leaf carries
six revision events: five bleeds — 2019→2021 (fact, blue), "the
house"→"the flat" (fact, blue), "soon"→"in March" (fact, blue),
"friend"→"brother" (judgement, red), "angry"→"ashamed" (judgement,
red) — and the one confession strike of §8.2. As each plays, the pencil
numeral flickers upward; a visitor who reads the whole leaf watches it
reach **1,210**, and §8.3's footer prints exactly that sum.

**Scroll timeline:** 0–600ms date writes · title settles · entry types
(≤3,700ms) · circle scribbles (3,800–4,500ms) · first note writes
(~5,100ms) · the reader scrolls; the ribbon (§6.10) begins its descent;
each correction, at its reading-line crossing, performs and increments.

### 8.2 The mid-page section — the confession spread (§6.3, §6.4, §6.7)

**The passage.** Mid-leaf, the entry reaches the day it has been
avoiding — the phone call of the previous spring. The paragraph is the
leaf's scrubbed-underline paragraph (§6.4): as the visitor reads, the
red line grows beneath it at their pace. Inside it sits the leaf's one
confession (§6.3). The printed sentence was:

> "I told him I was fine."

It strikes (420ms), fades to 0.38, holds for 350ms — and the
replacement writes itself in the margin at 26px, the largest hand on
the page: **"I was not fine, and he knew."** The tally flickers:
+1.

**The pinned spread** (§6.7) follows immediately — the same memory,
held. The spread's paragraph is the entry's account of the garden that
afternoon. Beat 1 (progress 0.18), blue, strokes in: *"yes. this is how
it was."* Beat 2 (0.48), red: *"or did I invent that?"* — and the first
note dims to 88%, succeeded, not erased. Beat 3 (0.78): the pressed
flower (§6.13, in its narrative role) settles over 900ms, pencilled
beneath: *"violet, from the garden wall, 3 May."* The date is inside
the diary's chronology (the garden afternoon was that spring), the
flower is the keeper ending the argument by keeping the moment — the
sequence the whole theme exists to tell, in one held screen.

**Scroll timeline:** underline scrubs with the reader · strike at the
reading line, replacement by +1,900ms · pin engages · beats at 0.18 /
0.48 / 0.78 of the 240vh track · release glide 400ms · the leaf
continues to §8.3.

### 8.3 The conversion section — the letter in the margin (§6.15, §6.17)

**The close of the leaf.** After the entry, the printed invitation (one
Garamond sentence, no more): *"This diary is read by strangers and kept
by one person. If a day here was ever your day too, the margin has
room."* Beneath it, the letter slip (§6.15): Name / Where the reply
should find you / Your note — ruled lines, the visitor's words appearing
in blue Caveat as they type. A reader writes three lines about her own
brother. On submit: the slip presses, its tape settles, it slides into
the margin, and the keeper's hand answers over 900ms: **"Thank you. I
read every word left here. — M."** The printed confirmation beneath
states the real practice: *"Your note is in the margin. Replies come by
post — usually within the week."*

**The tally leaf** (§6.17) closes the page, and its record column is
the audit of everything above, printed in full:

| The record | Value | Traces to |
|---|---|---|
| First entry | 14 February 2021 | §6.9 `data-first-entry` |
| Days kept | 1,460 | computed, §8 head |
| Words revised before this leaf | 1,204 | §6.9 `data-revised-base` |
| Words revised on this leaf | 6 | 5 bleeds (§8.1) + 1 strike (§8.2) |
| **Words revised** | **1,210** | 1,204 + 6 — the figure §6.9's margin tally must show |

**Scroll timeline:** invitation prints (no performance) · the form is
used at the visitor's pace · success sequence ≤1,700ms (§6.15) · the
footer is reached at rest, its figures already true.

---

## 9. Anti-slop — what makes THIS theme look cheap

1. **The handwriting backlog.** Notes stroking in late, queuing up
   behind a fast reader, a page still "writing itself" seconds after
   arrival. The delay is 600ms of character, not a loading strategy.
   *Cure:* §6.1's fast-scroll rule — notes passed at speed appear
   written; at most one note writes at a time.
2. **Red as decoration.** Red buttons, red headings, red sale badges.
   Red in this diary is a verb — it edits. *Cure:* §2's rationing and
   §10 check 9: every red mark must name what it revises.
3. **Runtime-random imperfection.** Rotations and wobbles rolled fresh
   on every load. A hand is consistent; randomness is a filter.
   *Cure:* seeded values from `data-seed`, identical on every build
   (§5).
4. **The faked hand.** A brand team setting navigation, prices and
   disclaimers in a handwriting font to seem personal. The margin is
   one keeper, writing about the content — not the content's costume.
   *Cure:* §3 law 1 — the hand never sets anything a visitor must rely
   on.
5. **The circle around the offer.** Circling the price, the headline,
   the call to action. The keeper circles what turned out *true*.
   *Cure:* §6.2's content rule; a circled CTA fails the gate outright.
6. **The cream rectangle.** Paper colour and a serif, but no ruled
   rhythm, no margin column — the notes pasted absolutely over a blog.
   *Cure:* §4 — the margin is a layout column, the rules are the leaf's
   grid, and removing the hand must still leave a structured page.
7. **The greeting card.** Centred Caveat headings, handwriting for
   section titles, a "handwritten" logo. *Cure:* §3 laws 1 and 4 —
   print heads, the hand annotates, nothing handwritten is centred.
8. **The synonym bleed.** Corrections that change nothing ("big" →
   "large") to show off the effect. A bleed is a changed mind.
   *Cure:* §6.5's content rule — every correction must be a fact fixed
   or a judgement revised, and a reviewer must be able to say which.
9. **The stock photo, pasted.** A generic image with tape corners reads
   as a scrapbook sticker, and a photo that "peels" to reveal a
   marketing message is worse. *Cure:* §6.6 — photos are of the entry's
   own story, captions add facts, the lift never peels; a lost photo is
   admitted by the empty mount, never a broken-image icon.
10. **Three strangers in the pin.** A pinned spread whose three notes
    are unrelated decorations. The pin is the theme's most expensive
    device and buys exactly one thing: a mind changing in sequence.
    *Cure:* §6.7 — agreement, doubt, flower, about *this* paragraph, or
    no pin.
11. **The ring as logo.** A coffee ring on every page, same corner,
    full-dark from the first second. *Cure:* §6.8 — one ring, on the
    living leaf, darkening with engaged time; archive leaves carry
    theirs already dark, in print.
12. **Pencil marketing.** Tallies that count readers, copies sold or
    five-star reviews. The pencil counts the book's own life only.
    *Cure:* §6.9 — days from a printed date, revisions from played
    corrections, both auditable on the page.
13. **The menu in a paper hat.** A standard nav bar with a paper
    texture, or a ribbon stretched over a page with no sections to
    check off. *Cure:* §6.12 — the index is the real chronological
    contents; §6.10 — no structure, no ticks.
14. **The slogan hero.** A marketing headline with a Caveat date
    floated above it. *Cure:* §6.11 — the hero is today's actual entry;
    if there is no entry, there is no hero, only a shorter leaf.
15. **The clip-art flower.** A symmetrical flower icon repeated at
    every section break. *Cure:* §6.13 — one flower per spread, drawn
    pressed and imperfect, captioned with a species and a date from
    inside the text, or the honest blank-lines divider instead.
16. **The uniform card.** Every archive slip carrying a photo *and* a
    note *and* identical decoration — the template showing through the
    fiction. *Cure:* §6.14 — a slip carries what its entry actually
    has; plainer slips are honest slips.
17. **The CRM letter.** Marketing fields, a "subscribe for offers"
    checkbox, a success state that upsells. *Cure:* §6.15 — a letter
    needs a name, a reply address and words; the success is a place in
    the book, not a funnel step.
18. **The comedy 404.** A torn page played for laughs, or a search box
    where the admission should be. *Cure:* §6.18 — stub, blue
    admission, real neighbours, in that order, and almost no motion.

---

## 10. Quality gate

All twelve checks are blocking. A build that fails any one is not a
Marginalia build, whatever it resembles.

1. **No-JS completeness.** With JavaScript disabled, every leaf reads
   complete: entries whole, notes written, corrections shown in their
   static notation, tallies at build-time values, footer sums correct.
2. **Legibility floor.** Struck text measures ≥0.38 opacity and is
   liftable to ≥0.55 by hover, tap *and* keyboard focus; pencil appears
   only on numerals, ticks and labels at §2's sizes; tape never grounds
   text except §6.14's ink-on-tape label.
3. **Tally reconciliation.** A DOM audit recomputes the record:
   `data-revised-base` + (correction elements on the leaf) = §6.9's
   final tally = §6.17's printed sum; days kept recomputes from
   `data-first-entry` to the build's stated "today". Any disagreement
   fails the build.
4. **Note specificity.** Every margin note is read against two other
   paragraphs on the leaf; a note that could sit beside either fails
   and is rewritten or cut.
5. **Marks carry no information.** Remove §6.2's circle and §6.4's
   underline in a test build: nothing of meaning is lost. If either
   mark is load-bearing, the content is at fault, not the mark.
6. **Confession mechanics.** The strike draws per line, never as a
   diagonal slash; the replacement is the largest hand on the page;
   exactly one confession per leaf; the focus-lift (§6.3) works by
   keyboard alone.
7. **Watchdog drills.** With animations frozen mid-flight by the
   tester, every element reaches its finished state within its stated
   watchdog: notes 2400ms, circle 1600ms, confession 2600ms, bleeds
   1500ms, entrance 4200ms, leaf turn 3000ms, form success 3000ms.
8. **Ring geometry.** The coffee ring underlaps no text at any
   breakpoint; exactly one live ring exists (home leaf); archive
   leaves print theirs at full darkness with no drift code shipped.
9. **Ink law audit.** Every red element names its revision target;
   every blue element is an addition or a date; every pencil element is
   bookkeeping. A single red decoration fails the build.
10. **Continuity audit.** Flower caption dates fall inside the diary's
    chronology and match a day the text mentions; tally dates agree
    across §6.9, §6.17 and the index; the circled phrase is defensible
    as its entry's turning point to a cold reader.
11. **Reduced-motion completeness.** With `prefers-reduced-motion`, the
    full leaf is readable with zero performances and zero waiting:
    notes written, entrance finished, ribbon placed, tallies true.
12. **Budget verification.** The page ships inside §14's budget,
    measured, not estimated — including the mobile payload, in which
    the note-stroke SVGs are absent.

---

## 11. Component inventory

Every component a real site in this theme needs, with its themed
treatment — or its refusal, with the in-theme replacement. The diary's
rule for components is the theme's law restated: print carries, the hand
annotates; a component that cannot be said in print does not belong on
the leaf.

| Component | Marginalia treatment |
|---|---|
| Primary button | There are no filled buttons on a leaf. The primary action is a Garamond link with the hand-drawn underline at rest (§6.12) — the keeper pointing. Where a real form must submit (§6.15), the same treatment at 20px. |
| Secondary button | A printed Garamond link without the underline; gains it on hover. |
| Text input | A ruled line (§6.15): no box, `--rule-line` beneath, deepening to `--blue` on focus; the visitor's text in Caveat blue. |
| Textarea | Ruled lines that multiply as the letter grows (§6.15). |
| Select / dropdown | **Refused.** A diary offers choices as a short printed list of links (dates, entries) — §6.12's index is the theme's select. |
| Checkbox / radio | **Refused as controls.** The only ticks on a leaf are the pencil's, and they record reading (§6.10), never consent. A real consent need leaves the diary surface (§7, utility pages). |
| Toggle / switch | **Refused.** Nothing in a diary toggles; settings live off-leaf. |
| Tabs | **Refused.** A book does not tab; it groups by date (§6.12's month rules) and turns leaves (§6.16). |
| Accordion | **Refused.** Hidden text contradicts the law (the print ships whole). Long leaves are divided by §6.13 dividers, never collapsed. |
| Modal / dialog | **Refused.** Nothing floats above a diary. The pasted slip (§6.14/§6.15) is the theme's way of adding a surface: in flow, taped, part of the leaf. |
| Toast / snackbar | **Refused.** News from the keeper arrives as a margin note (§6.1) written beside the thing it concerns — or it is not said. |
| Alert / banner | A keeper's note in red at the head of the leaf, written as §6.1 with a printed Garamond line beneath it carrying the same fact in plain text (alerts are facts; facts are print's job). |
| Badge / tag | **Refused.** Entries are dated, not tagged. A category is expressed by the index's grouping (§6.12), never by a pill. |
| Card | The pasted slip (§6.14) — date on tape, real first line, optional real note/photo. |
| Table | A printed table on ruled lines: Garamond, hairline `--rule-line` row rules, no fills, no zebra (paper does not stripe); numerals tabular Garamond. The tally leaf's record (§6.17) is the model. |
| Pagination | "Earlier entries / Later entries" as printed links with their date ranges ("← October – December 2024") — a diary paginates by time (§6.12). Numbered page pills are refused. |
| Breadcrumbs | **Refused.** Position in a diary is a date; the §6.12 index shows the current entry circled. That is the whole breadcrumb. |
| Progress bar | The ribbon bookmark (§6.10). A percentage bar is refused absolutely. |
| Spinner / loader | **Refused.** Loading is the unwritten leaf (§6.16's skeleton). |
| Skeleton | Ruled lines + pencil ghosts (§6.16). |
| Tooltip | A pencilled margin gloss: on hover/focus, a short Caveat note in the margin at the element's line (§6.5's margin ghost is the model). Never a floating dark box. |
| Link | Garamond ink or blue; hand-drawn underline on hover/focus (§6.12). External links are marked in print ("(a letter leaves this diary)") — the keeper notes when you are leaving the book. |
| Heading | Garamond per §3; a heading may be *annotated* by the hand but never *set* by it. |
| List | Printed lists on the ruled rhythm; list markers are Garamond numerals or a printed dash — never pencil (pencil counts events, not items). |
| Image | Only as §6.6 taped photos or §6.13 pressed flowers. A bare `<img>` in a column is a hole in the fiction. |
| Form | The letter slip (§6.15) is the only form pattern on a leaf. |
| Footer | The tally leaf (§6.17). |
| 404 | The torn page (§6.18). |
| Search | **Refused as a page.** Find-in-page and the dated index serve; a site large enough to need search has outgrown the diary (§1). |

## 12. Content & copywriting voice

The diary has two voices, and the whole theme is keeping them apart.

### The Print (Garamond) — the composed self

Past tense, complete sentences, punctuated, calm. Print is what the
keeper was willing to stand behind at the time of writing: entries,
headings, captions, labels, instructions, promises, the legal lines.
Print never performs emotion it has not earned, never uses
exclamation, and never addresses the visitor as a customer.

- Headline style: a title a diarist would write — *"On Keeping"*,
  *"The Garden, That Spring"* — never a benefit claim.
- ✓ "Replies come by post — usually within the week."
- ✗ "Subscribe now and never miss a post!!"

### The Margin (Caveat) — the private self

Present tense, fragments allowed, honest to the point of discomfort.
The margin corrects, doubts, dates and jokes. It is shorter than the
print it annotates (≤14 words, §3 law 1) and it never sells, never
instructs, never carries a fact the visitor needs (facts are repeated
in print if they matter — §11's alert rule is the model).

- ✓ *"or did I invent that?"* (doubt, red, beside the memory it doubts)
- ✓ *"bought it at the station, of all places."* (addition, blue)
- ✗ *"check out my other posts!"* (the hand never markets)
- ✗ *"Note: the meeting is at 3pm."* (a needed fact, hiding in handwriting)

### Error and empty-state voice

- **Form errors** are the keeper editing, kindly, in red: beside an
  empty note field — *"the margin needs the words, not just the name."*
  Beside a malformed address — *"this address won't carry a letter.
  check it once more?"* The printed `aria` text says the same thing
  plainly ("Please add your note before leaving it in the margin").
- **The empty archive** (a month with no entries) prints one Garamond
  line — *"Nothing was kept this month."* — and the margin stays empty:
  the keeper does not annotate an absence.
- **The torn page** speaks as §6.18 specifies: print states, the hand
  admits.

### Fixed strings (verbatim, build-checked)

- Tally labels: **"Days kept"** / **"Words revised"** — never
  reworded, never localised into marketing synonyms.
- The confession's form: original struck, replacement larger — the
  *words* are each site's own; the size relationship is the fixed
  string.
- The keeper's form reply (§6.15) follows the fixed shape: gratitude,
  the reading promise, the initial — *"Thank you. I read every word
  left here. — M."*
- The pencil sign-off (§6.17): *"— kept, so far."*

## 13. Full-page scroll choreography map

The home leaf, top to footer, in the order the visitor lives it.
(Entry leaves drop beats 1–3's performance per §6.11; archive leaves
keep only beats 4, 8 and 10 in their quiet forms.)

| Beat | Where | What the visitor sees and feels |
|---|---|---|
| 1 | Leaf head | The date writes itself in blue; the title settles. The diary opens *today*. |
| 2 | Opening paragraph | The entry types, phrase by phrase — someone is writing this, now, calmly. |
| 3 | Opening paragraph | The red circle scribbles around the true phrase; 600ms later the first note thinks itself into the margin. Print, judgement, thought. |
| 4 | Whole leaf, continuous | The ribbon begins its descent in the margin; the coffee ring starts its minutes-long darkening, unnoticed. The book is alive at the edges of attention. |
| 5 | First corrections | Words bleed — a year, a name — as they cross the reading line; the pencil tally flickers upward. The text is being revised under the reader's eye. |
| 6 | The photo | A taped photograph settles, tape pressing corner by corner, and drifts almost imperceptibly against the print as reading continues. Evidence, kept. |
| 7 | The confession paragraph | The red underline grows at the reader's own pace; the honest sentence strikes, pauses, and its larger replacement writes itself. The leaf's emotional floor. |
| 8 | The pinned spread | Scroll holds. Agreement writes in; doubt succeeds it and dims it; a pressed flower settles the argument. One memory, thought three times. |
| 9 | The invitation | Print offers the margin; the letter slip waits, taped, ruled, empty. The visitor's turn to write. |
| 10 | The tally leaf | The record, in print: the numbers the margin kept, summed and provable. The ribbon comes to rest against it. The book closes itself. |

Reverse pass: scrolling up, nothing un-writes, un-strikes or un-ticks;
the leaf the visitor returns to is the leaf as it has become — which is
the theme's whole argument, performed by its scroll map.

## 14. Whole-page performance budget

| Budget | Limit | Notes |
|---|---|---|
| Total page weight (home leaf) | ≤ 780KB | All-in, fonts included. |
| Fonts | ≤ 120KB | EB Garamond (400/500 + italic) and Caveat (600/700), subset to the site's character set; handwriting is never faked by a variable-weight trick. |
| Images | ≤ 360KB per leaf | §6.6 photos ≤120KB each served responsively; below-fold photos lazy. |
| SVG (all marks, notes, flowers) | ≤ 90KB per leaf | Note stroke paths ≤9KB each (§6.1), ≤5 notes; flowers ≤6KB; the ring ≤1.5KB. |
| JS | ≤ 60KB | The shared loop, the stroke system, the form and the turn — nothing else earns script on a diary. |
| Animation frame budget | ≤ 1.6ms/frame main-thread | One rAF loop, lerp 0.12; scroll handlers write targets only; the loop sleeps at rest (§5). |
| Long tasks | none > 50ms | Stroke setup is build-time; no runtime path tracing, no live filters (§6.5's sprites). |
| Layout stability | CLS = 0 | The leaf's boxes are reserved: photos at aspect ratio, notes in their margin slots, tallies in fixed digit cells. Handwriting arriving must never move print. |

**Cut order when the budget is exceeded** (cut in this order, never
skip ahead): 1. The §6.11 session-flag nicety (entrance replays per
leaf). 2. Photo parallax range halves. 3. The third §6.6 photo on the
leaf is deferred below the fold. 4. The ring's drift tick slows to 5s.
5. §6.7's pin converts to the stacked mobile behaviour at all widths.
**Never cut:** the notes' text, any correction, the tallies' truth, the
reduced-motion variants, the no-JS completeness. A Marginalia page that
is over budget loses performances, never words.

## 15. Build-order checklist

1. **The static leaf first:** print the complete page — entries, notes
   as static Caveat, corrections in their static notation, tallies at
   build values, footer sums correct — with no JavaScript at all.
   Gate §10 check 1 must pass on this build before anything moves.
2. **Tokens and type:** the §2 palette (with its measured pairings),
   the §3 scale and laws, the §4 ruled grid and margin column.
3. **The shared loop:** rAF lerp 0.12 with sleep-at-rest and the §6.10
   heartbeat, before any element consumes it.
4. **The stroke system:** §6.1's note engine (paths, delay, queue,
   watchdog) — every later handwriting element reuses it.
5. **Tallies (§6.9) and the tally leaf (§6.17)** together, with the
   reconciliation audit wired as a build test (§10 check 3).
6. **Corrections:** §6.5 bleeds (with their tally hooks), then §6.3's
   confession (strike, lift, focus), then §6.2's circle and §6.4's
   underline — the revision family, in dependency order.
7. **Photos (§6.6)** with their settle and the empty-mount failure
   state; **dividers (§6.13)**.
8. **The pinned spread (§6.7)**, with its stacked fallback built first
   and the pin layered onto it.
9. **Ribbon (§6.10)** and **index (§6.12)** — place-keeping and
   contents, wired to the same section model.
10. **The opening entrance (§6.11)** — last of the performances, on top
    of a page that already works without it.
11. **The letter form (§6.15)**: fields, keeper-voiced validation, the
    success sequence, the no-JS posting path.
12. **The leaf turn and skeleton (§6.16)**, with the 3000ms abort
    drilled.
13. **The torn page (§6.18)** and the ring (§6.8) — the quiet pages
    and the quiet stain.
14. **Reduced-motion pass:** every element's variant verified against
    §10 check 11 with motion off at the OS level, not just emulated.
15. **The gate, signed by a non-builder:** all twelve §10 checks run
    cold — no-JS, watchdogs frozen mid-flight, tallies recomputed from
    the DOM, ink law and continuity audited by a reader who did not
    write the page. The signature goes in the tally leaf's build
    record, in print.
