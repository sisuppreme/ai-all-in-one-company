# 24. Tabloid Confessional — Expanded (v1 + v2)

*Expansion of theme #24 from `themes-001-025.md`, written directly to the
full standard: the 10-part v1 structure plus the v2 deepening layers
(EXPANSION-STANDARD.md). Identity preserved exactly — the agony-aunt column
as an interface, the same four inks (Newsprint pink `#F3E3D3`, Ink
`#262019`, Lipstick red `#B02E35`, Tea-ring brown `#9A7B4F`), the same two
hands (Caveat for the readers, Cormorant Garamond for the aunt), all 12
original signature elements deepened, not redesigned.*

---

## 1. Concept & world

The page is a morning's post at an agony aunt's desk, typeset. Every section
is one piece of correspondence: a reader's letter — raw, handwritten, on
lined notebook paper — and the aunt's answer beneath it, in calm serif on
smooth stock, written as if the ink were still wet. The visitor does not
"scroll a feed"; they sit across the desk while the aunt opens the post in
order. The next reader's letter waits half out of its envelope at the bottom
edge of the screen the whole way down, because there is always another
letter. The margin keeps the morning's evidence: a tea-ring stain that
darkens ring by ring for every letter answered, and a pinned portrait of the
aunt herself beside the column for the middle act — she is present while she
works, then she steps away.

The emotional register is specific and narrow: vulnerability handled with
composure. The readers are exposed (handwriting, feelings, no surnames); the
aunt is unhurried (serif, full sentences, no exclamation marks in her own
voice). The design's job is to hold that asymmetry still — never to make the
letters look designed, and never to make the answers look casual.

**The one law.** Anonymity is the authenticity. Readers are signed the way
real readers sign — "— Worried, of Walsall", "— Sleepless, of Leeds" — a
feeling and a town, never a full name, never an initial-and-surname. Any
build that puts a full name, a photograph of a "reader", a testimonial-style
star rating, or a social handle on a letter has broken the theme's founding
rule and fails the quality gate (§10, blocking). The aunt, by contrast, is
named and pictured: she is the professional; they are protected.

**Best fits.** Advice and coaching brands whose real content is questions
and considered answers; relationship and wellbeing podcasts built around
listener letters; community Q&A products where the questions are personal
and the answers are editorial (not forum threads); a counsellor's or
columnist's own site; a book or newsletter launch structured as
correspondence. The theme earns its keep wherever the Q&A *is* the product
and the askers must stay anonymous.

**When NOT to use it.** Never for content where the asker must be
identified and accountable (support tickets, bug reports, legal or medical
intake — anonymity there is a defect, not a charm). Never for high-volume
feeds: the column answers a morning's post, roughly 5–9 letters per page;
at 40 items the desk metaphor collapses and the tea-ring becomes a lie.
Never for breaking news or anything time-critical — ink that is still
wet is the opposite of urgent. Never for a brand whose voice is brisk,
irreverent, or loud: the aunt does not do brisk. And never where the
"letters" would be fabricated marketing copy dressed as readers — the theme
depends on correspondence that reads as real; invented letters in Caveat
are the fastest route to the anti-slop list (§9.1).

**The morning's shape.** A page in this theme is one sitting: header (the
aunt's nameplate and tallies), the hero letter from the slot, 4–7 further
letters with the aunt pinned beside the middle three, the write-in form
(the visitor's own envelope), and a footer that is the desk at day's end —
rings complete, postbag empty, kettle off. Longer archives live on listing
pages (§7), one morning per page.

---

## 2. Palette

Four anchor inks, fixed. Everything else is a labelled derivation — paper
getting older, ink getting thinner, a stain getting darker — never a new
hue. Lipstick red is rationed harder than in any sibling theme: it exists
for exactly three jobs (the key-sentence underline, the one kiss mark, the
postmark in the header) and is measured on the page (§10).

| Token | Hex | Role | Usage ratio | Pairing / contrast notes |
|---|---|---|---|---|
| `--newsprint` | `#F3E3D3` | The page ground — the newspaper's pink sheet | ~55% of pixels | Ground for the column and header; ink on it ≈ 12.4:1 |
| `--ink` | `#262019` | All print: answers, headings, UI text | ~18% | On `--newsprint` ≈ 12.4:1; on `--smooth` ≈ 13.1:1; on `--lined` ≈ 12.8:1 — AAA everywhere it carries text |
| `--lipstick` | `#B02E35` | The rationed red: underline, kiss, postmark | ≤1% of pixels, ever | On `--newsprint` ≈ 5.1:1 — graphics and large marks only; never body text, never a button fill |
| `--tea` | `#9A7B4F` | Tea-ring brown: rings, tape tint, hairlines on kraft | ~4% | Decorative only; ≈ 3.4:1 on newsprint — never carries text or meaning alone |

**Derived tokens (labelled, closed list — no others may be invented):**

| Token | Derivation | Used for |
|---|---|---|
| `--lined` | `#F8EDDD` — newsprint lightened one step | The notebook stock of the questions; must read as a *different paper*, not a different colour |
| `--smooth` | `#FAF3E6` — newsprint lightened two steps, desaturated | The answer stock; the calmest surface on the page |
| `--envelope` | `#DCC19E` — kraft, newsprint darkened toward tea | Envelopes, the slot surround, the peek letter's envelope |
| `--envelope-deep` | `#C3A276` — envelope darkened one step | Envelope flap shadow, slot interior edge |
| `--rule-line` | `#B7C0BC` — blue-grey, the biro rule of notebook paper | The horizontal rules on `--lined` stock only; never on smooth stock |
| `--margin-line` | `#D89A93` — lipstick washed to 38% over lined | The notebook's vertical margin line — a *print* pink, exempt from the red ration because it is paper, not a mark |
| `--ink-soft` | `#5A4F42` — ink at 62% over newsprint | Captions, datelines, the aunt's small print; ≈ 5.9:1 on newsprint — AA for text ≥ 13px |
| `--ink-faint` | `#8A7B68` — ink at 40% | Fold shadows' colour source, disabled text on paper (≈ 3.1:1 — disabled/large only) |
| `--tea-deep` | `#77572F` — tea darkened one step | The final (oldest) tea ring, the footer's hairline |
| `--tape` | `#EFE0BE` at 82% opacity — dried glue tint | Tape strips on photo frames; always translucent, always over a photo corner |

**Hard pairing rules.**
- Readers' handwriting (Caveat) is set in `--ink` only. A reader never
  writes in red; a reader's pen is a biro, and the biro is ink.
- The aunt's answers are `--ink` on `--smooth`, always. Her one red act is
  the underline (§6.10).
- `--lipstick` never fills a shape larger than the kiss mark (≈ 54 × 40px),
  never colours a whole word of body text, and never appears in the form —
  errors there are the aunt's voice in ink, with a tea-brown rule (§6.15).
- Tea is a stain, not a brand colour: no tea-coloured headings, buttons, or
  links, anywhere.

**Lamplight (dark) behaviour.** There is no inverted dark mode; there is
the desk under the evening lamp. `--newsprint` → `#2A2019`, `--lined` →
`#332820`, `--smooth` → `#382C21`, `--envelope` → `#4A3826`, `--ink` →
`#F0E4D2` (on lamplight newsprint ≈ 11.8:1), `--lipstick` → `#D96A6E`
(brightened one step so the rationed marks still read as marks, ≈ 4.6:1 —
graphics only, as in light mode), `--tea` → `#B08D55`, `--rule-line` →
`#5A6660`. The stocks must still read as three different papers under the
lamp — if lined and smooth collapse into one surface, the lamplight mapping
has failed and the build goes back. The tea rings darken *less* per letter
in lamplight (they are already in shadow; §6.5).

---

## 3. Typography

Two hands, never swapped. This is the theme's type law, and it is stricter
than a font pairing: it is a casting decision. **Caveat is the readers.**
**Cormorant Garamond is the aunt.** A headline in Caveat claims a reader
wrote it; a label in Cormorant claims the aunt stands behind it. UI chrome
(buttons, form labels, navigation) belongs to the aunt's office, so it is
set in Cormorant small caps — the column's printed furniture — never in
Caveat, because the interface is not a reader.

| Role | Face / weight | Size / line-height | Tracking | Rules |
|---|---|---|---|---|
| Letter body (the question) | Caveat 500 | 24px / 1.45 (31px+ on the lined stock's rule pitch, §4) | 0 | Set on the notebook lines: line-height locks to the rule pitch (28px at desktop) so handwriting sits *on* the lines, not between them |
| Letter salutation & signature | Caveat 700 | 26px / 1.3 | 0 | Signature format is law: "— [Feeling], of [Town]" (§1); the flourish is drawn, the words are text |
| Aunt's answer body | Cormorant Garamond 500 | 20px / 1.55 | 0 | The reading voice of the page; max measure 58ch |
| Aunt's answer lead line | Cormorant Garamond 600 | 21px / 1.5 | 0 | The first line of each answer carries the counsel's weight; it is also where the key sentence usually lives (§6.10) |
| Column nameplate | Cormorant Garamond 600, small caps | 34px / 1.1 | +0.14em | The aunt's name and column title; the only display type on the page |
| Section heads (the aunt's furniture) | Cormorant Garamond 600, small caps | 15px / 1.3 | +0.18em | "From this morning's post", "Write to the column" — printed furniture, never handwritten |
| Datelines & postmarks | Cormorant Garamond 500 italic | 13.5px / 1.4 | +0.02em | "Received Tuesday, by the second post" — dates are real or omitted (§12) |
| Form labels & buttons | Cormorant Garamond 600, small caps | 14px / 1.3 | +0.16em | The office voice; the visitor's own typing inside the form is Caveat 22px — they are writing a letter now |
| Captions under photos | Cormorant Garamond 500 italic | 14.5px / 1.45 | 0 | In `--ink-soft`; the aunt annotating, never the reader |

**Type laws.**
1. **No third face.** No sans for UI, no mono for data. The tallies in the
   header are Cormorant tabular figures; the desk has no machine type.
2. **Caveat never sets a word the aunt is responsible for** — no Caveat
   buttons, errors, prices, or navigation. The moment handwriting gives an
   instruction, the fiction tears.
3. **The aunt never exclaims.** Her display settings carry no exclamation
   marks (§12); her emphasis is the underline and the italic, in that order.
4. **Handwriting sizes are floor-bound.** Caveat below 20px becomes
   illegible and precious; letter body never drops under 21px at any
   breakpoint (§6 breakpoint tables hold this even on <768px, where the
   measure narrows instead).
5. **Signatures are text, not images** — screen readers must be able to
   read "— Worried, of Walsall"; only the flourish stroke is drawn (§6.4).

---

## 4. Layout language

**The desk, not the grid.** The page is a desk surface (`--newsprint`)
with papers laid on it in one column of correspondence. A faint underlying
12-column grid exists for alignment discipline, but nothing on the page may
*look* gridded: letters sit at slight, deterministic rotations (the laid
paper angles, §4 table below), stocks overlap at edges, and the margin is a
working margin — it holds the tea rings, the pinned aunt, and nothing else.

**Geometry.**
- **Letters column:** max 680px, centred-left at ≥1200px so the right
  margin (min 300px) can hold the pinned aunt and the rings; centred at
  768–1199px; full-bleed with 20px desk margins at <768px.
- **The slot:** a full-width bar at the very top of the hero, 14px tall,
  `--envelope-deep` with a 2px `--ink` slit line — the envelope slot the
  hero letter comes through (§6.1). It is part of the header furniture and
  scrolls away; it is not fixed.
- **Stocks:** each letter is two papers. The question paper (`--lined`,
  ruled at a 28px pitch with the `--margin-line` vertical at 44px from its
  left edge) lies first, rotated −0.4°; the answer paper (`--smooth`,
  unruled, 24px padding) overlaps the question's foot by 18px and is
  rotated +0.3° — counsel laid over the question, the way the aunt places
  her reply on top of the letter she has just read. Rotations alternate
  sign per letter by index parity (deterministic, never random) and are
  capped at ±0.6°: paper laid by a careful person, not scattered.
- **Vertical rhythm:** letters are separated by 72px of bare desk
  (the pause while the aunt reaches for the next envelope); inside a
  letter, question-to-answer gap is −18px (the overlap), answer-to-
  signature 20px.
- **The margin:** right of the column at ≥1200px. The tea-ring cluster
  (§6.5) sits at the margin's top, beside the first letter; the pinned
  aunt (§6.6) occupies the margin for the middle act. The margin never
  holds ads, related links, or a newsletter box — it is her desk, and
  clutter there is anti-slop (§9.6).
- **The foot of the screen:** the peek letter's envelope (§6.3) is fixed
  to the viewport's bottom edge, height 46px visible — paper and envelope
  lip only. It is the one fixed element on the page, and it must never
  cover a line of the letter being read: the letters column carries a
  bottom padding equal to the peek height + 24px at all times.

**Density rules.** One letter per viewport, roughly: a letter (question +
answer) should occupy 85–110vh at desktop sizes, so the reader is always
*with* one correspondent. Whitespace is desk, not emptiness — bare
`--newsprint` between letters is where the morning breathes, and it is
never filled with dividers, banners, or "keep reading" furniture.

---

## 5. Full motion system

Motion in this theme is postal and domestic: paper slides, unfolds, is
drawn out, is laid down; ink flows and dries; a stain darkens. Nothing
bounces, nothing spins, nothing glows. Every duration below is a token;
every easing is named for the desk action it imitates.

**Named easings (the theme's five):**
- `--ease-post` — `cubic-bezier(.22,.9,.28,1)`: paper sliding through a
  slot or out of an envelope; fast start, long friction settle.
- `--ease-unfold` — `cubic-bezier(.3,.7,.2,1)`: a fold opening; slow at
  the crease, then flat.
- `--ease-ink` — `cubic-bezier(.4,0,.2,1)`: ink arriving line by line;
  even, unhurried, no overshoot.
- `--ease-lay` — `cubic-bezier(.2,.8,.3,1)`: paper laid down and picked
  up; the hover/tilt easing.
- `--ease-draw` — `cubic-bezier(.5,0,.15,1)`: a pen stroke being drawn —
  underline, flourish, kiss; starts deliberate, finishes in one motion.

**Duration tokens:** `--dur-slide: 600ms` (slot/envelope travel),
`--dur-unfold: 550ms`, `--dur-line: 400ms` (one ink-flow line),
`--dur-stagger: 120ms`, `--dur-draw: 300ms` (underline) / `500ms`
(flourish) / `800ms` (the kiss), `--dur-lift: 240ms`, `--dur-count: 700ms`,
`--dur-transition: 450ms`, `--dur-fallback: 1200ms` (the write-out law).

**Every motion term, in this theme's language:**

| Term | The theme's translation | Spec |
|---|---|---|
| Scroll-triggered reveals | A letter is *opened* when its envelope reaches the reading line (62% viewport height) | Question settles flat, then the answer flows (§6.2); trigger once per letter |
| Parallax | The lined question stock drifts slower than the smooth answer stock laid over it — two papers, two weights | Question layer at 0.92× scroll rate, answer at 1.0×, via the shared lerp loop; total differential ≤ 10px per letter so the overlap never separates |
| Pinned scenes | The aunt pins beside the column for the middle act (§6.6); no other pin exists on the page | Pin spans letters 3–5 of the morning; release is a lay-down, not a jump |
| Masked line reveals | Answers arrive through the letter-slit (§6.8) — a clip-path widening, the envelope's mouth | `clip-path: inset(0 46% 0 46%)` → `inset(0 0 0 0)`, 500ms `--ease-unfold` |
| Blur-to-sharp | Refused as a reveal. Ink does not blur; it *flows* — opacity and saturation per line (§6.2). The only blur on the page is the fold shadow's own softness | — |
| Kinetic typography | Refused. Handwriting that moves letter by letter is a cartoon; the signature flourish (§6.4) is the theme's single drawn-text event, and it is a stroke, not type | — |
| Animated counters | The header tallies (§6.11): letters answered, cups of tea | 700ms `--ease-ink`, tabular Cormorant, counted from the DOM (§6.11 law) |
| Progress indicator | The tea-ring (§6.5): rings darken per letter read; there is no bar, no percentage | One ring arc per completed letter, each ≈ 70% opacity of the previous |
| Marquee | Refused. Nothing on a desk scrolls sideways forever. The postbag index (§6.18) is a still list | — |
| Ambient loops | Two, both barely: the peek letter's rustle (§6.3, ≤1px, ~7s period) and the lined-paper grain breathing (opacity ±3%, 9s) | Both pause off-screen, both die under reduced motion and `save-data` |
| Micro-interactions | Envelope-lift hover (§6.9), key-sentence underline (§6.10), tape-photo scale-in (§6.12) | All ≤ 300ms except the kiss |
| Page transitions | Letters travel: current letter slides back into its envelope, next is drawn out (§6.12) | 450ms `--ease-post`, out then in, never simultaneous |
| Image treatment | Photos live in taped frames (§6.12); they scale-in-frame 1.05 → 1 as the frame enters | 600ms `--ease-lay`; the tape never moves |

**Global motion laws.**
1. **The write-out law.** Writing is a replay over complete text. Every
   letter and answer exists in full in the DOM at load; any element still
   mid-flow 1200ms after its trigger is forced to its final state in one
   frame. No reader ever waits for ink.
2. **One hand at a time.** Ink events serialise: a signature never draws
   while its answer is still flowing; the kiss never draws while anything
   else on that letter moves. A simple queue per letter enforces it.
3. **The red budget is a motion budget too.** The kiss draws once per
   page, ever (§6.7); the underline draws once per answer (§6.10).
   Re-scrolling never replays either.
4. **Scroll is lerp-smoothed.** One shared `requestAnimationFrame` loop,
   lerp 0.12, drives the peek scrub, the stock parallax, and the pin.
   Direct scroll-linked writes outside the loop are a gate failure.
5. **Reduced motion = the post already read.** Letters flat and fully
   written, peek letter static at its half-out rest, no pin (the aunt
   sits above the middle letters instead), rings pre-darkened to the
   reader's position on load. Same information, no theatre.

---

## 6. Signature elements

### 6.1 Envelope-slot hero letter

- **What & why.** The hero is the first letter of the morning, and it
  arrives the way letters arrive: through the slot. An envelope slot bar
  caps the hero; on load the first question paper slides down out of it,
  a fold shadow sweeping ahead of the paper's leading edge, and settles
  flat as the page's opening content. It exists because this theme's hero
  cannot be a headline and a stock photo — the correspondence *is* the
  hero, and its entrance is the site's whole premise in 600ms.
- **Structure.** `header.slot` (the 14px bar, §4) + `article.letter.hero`
  containing `section.question` on `--lined` stock. The paper is a normal
  in-flow element; JS arms a pre-state (`transform: translateY(-72%)`,
  clipped by the hero's `overflow: hidden` slot mask) before first paint.
  The fold shadow is a `::before` gradient strip (height 34px, `--ink` at
  18% → transparent) riding the paper's leading edge.
- **Motion spec.** Trigger: load, gated on `document.fonts.ready` with a
  300ms cap (Caveat must be the hand that arrives). Paper slides down
  600ms `--ease-post`; the fold shadow sweeps 120ms ahead of the paper's
  edge and fades as the paper flattens; the paper's rotation eases from
  −1.1° to its laid −0.4° over the final 200ms. At rest the transform is
  removed entirely — the letter is just paper on the desk.
- **States.** *Rest:* flat, fully readable. *Settling:* the 600ms travel.
  There is no hover or active state — the hero letter is read, not used.
- **Content merge.** The letter is the hero content: salutation, question,
  and (below it) the first answer. Remove the slide and the page loses
  nothing but the arrival.
- **Failure fallback.** No JS → no pre-state is ever armed; the letter
  sits flat under the slot bar. Fonts blocked → the 300ms cap fires the
  slide in the fallback hand rather than waiting.
- **Reduced-motion variant.** The letter is simply there, flat, under the
  slot. The slot bar remains as furniture.
- **Performance budget & mobile variant.** One transform on one element;
  no layout thrash (the hero reserves the letter's full height from CSS,
  so the slide causes zero CLS). Mobile: identical, travel distance
  scales to the paper's height; nothing is cut — this is the theme's
  signature and it is cheap.

**v2 — Choreography timeline** (t = fonts-ready or 300ms cap, whichever first):

| Beat | Time | What happens |
|---|---|---|
| Arm | t −∞ (head script) | Pre-state applied before first paint; slot mask clips the paper |
| Release | t + 0ms | Paper begins translateY −72% → 0, rotation −1.1° |
| Shadow lead | t + 0–480ms | Fold shadow rides 12px ahead of the leading edge, opacity 18% → 8% |
| Flatten | t + 400–600ms | Rotation eases to −0.4°; shadow fades to 0 |
| Settle | t + 600ms | Transform removed; letter is static paper; answer's slit reveal (§6.8) is queued |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Flat letter under the slot | Same |
| Hover | No change (not interactive) | n/a |
| Focus | The letter's links/underline targets take the standard focus ring (§6.10 a11y); the paper does not move | Same |
| Active | n/a | n/a |
| Scrolled-past | Static paper; never replays on scroll-back | Same |
| Disabled | n/a — no disabled state exists for a letter | n/a |

**v2 — Breakpoint behaviour.** ≥1200px: full travel, column 680px with
margin. 768–1199px: column centred, travel unchanged. <768px: column
full-bleed at 20px desk margins, travel distance = paper height (shorter
in px), rotation reduced to −0.2° laid (small paper wobbles less).

**v2 — Edge cases & failure modes.** Very long hero question (> 9 lines):
the paper is taller than the slot mask's travel — travel is defined as a
percentage of the paper's own height, so it still emerges fully; the
answer waits below the fold, correctly. Very short question (2 lines):
minimum paper height 220px (an envelope's worth of paper) so the slide
still reads as arrival, not a twitch. Slow network with fonts pending:
the 300ms cap rules. Scroll during the 600ms: the hero is in-flow, it
simply scrolls with the page — no pin, no conflict.

**v2 — Accessibility spec.** The slide is decorative: the letter is a
normal `<article>` with its heading in DOM order; screen readers meet the
text, not the travel. No focus is moved on load. The slot bar is
`aria-hidden` furniture. Contrast: Caveat ink on lined ≈ 12.8:1 at rest
and at every frame of the slide (the paper's colours don't change, only
its position).

**v2 — Tokens consumed.** `--newsprint`, `--lined`, `--envelope-deep`,
`--ink`, `--ease-post`, `--dur-slide`, `--dur-fallback`.

### 6.2 Ink-flow answers

- **What & why.** The aunt's answer writes itself — not letter by letter
  (that is a typewriter cartoon, refused in §5) but line by line, the way
  ink actually arrives from a pen that is thinking: each printed line
  rises in opacity with a slight saturation bloom, in reading order, as
  if the ink were still wet when laid. It is the theme's central act of
  counsel: the answer is composed in front of the reader, in response to
  the question directly above it.
- **Structure.** `section.answer` on `--smooth` stock; JS wraps each
  rendered line? No — line-wrapping is layout-dependent and fragile.
  Instead the answer is authored in short paragraph blocks, and the flow
  runs per *block-line group*: the block is split by the browser into
  visual lines only for the stagger count via `Range` measurement at
  trigger time, and the reveal itself is a top-to-bottom ink mask — a
  `linear-gradient` mask whose wet edge travels down the block at line
  pitch, so lines bloom in true reading order at any width, with no DOM
  splitting. Below the mask threshold a block is simply fully inked.
- **Motion spec.** Trigger: the answer's letter is opened (§5 reading
  line), strictly after its question has settled. Per line: 400ms
  `--ease-ink`, stagger 120ms between line starts; the wet edge carries a
  6px band where saturation blooms +18% and opacity runs 55% → 100%,
  drying to flat ink behind it. A 6-line answer completes in ≈ 400 +
  5 × 120 = 1000ms — inside the write-out law's 1200ms with room to
  spare; longer answers are capped: stagger compresses to
  `min(120ms, (1200 − 400) / (lines − 1))` so no answer ever exceeds the
  law.
- **States.** *Rest (unopened):* fully inked in the DOM; the mask is a
  JS-armed pre-state only. *Flowing:* the wet edge travels. *Written:*
  mask removed, plain serif. *Scrolled-past:* written; never re-flows.
- **Content merge.** The flow is in the answer's own serif, on its own
  stock, in the column's real sequence — it is the counsel being given,
  not an effect applied to it.
- **Failure fallback.** The write-out law (§5.1): at trigger + 1200ms any
  answer still masked is unmasked in one frame. No JS → no mask is ever
  armed; every answer is simply printed.
- **Reduced-motion variant.** Answers are printed. Full stop.
- **Performance budget & mobile variant.** The mask is a composited
  gradient on one element per answer, one answer flowing at a time (the
  §5.2 queue); cost is one repaint region per frame. Mobile: identical —
  the mask is width-agnostic, which is precisely why it was chosen over
  line-splitting. On `save-data` / low-power signals the flow is skipped
  and answers print instantly (the information is identical).

**v2 — Choreography timeline** (t = letter opened):

| Beat | Time | What happens |
|---|---|---|
| Question settle | t + 0ms | Question paper finishes its lay-down (§6.9 rest state) |
| Slit opens | t + 60ms | §6.8 clip widens, 500ms |
| First line | t + 160ms | Line 1 blooms (400ms `--ease-ink`) |
| Lines 2…n | +120ms stagger (compressed if needed) | Each line blooms in reading order; wet band 6px |
| Dry | last line + 400ms | Mask removed; answer is flat print |
| Signature queue | after dry | If this letter's signature (§6.4) belongs to the question above, it has already signed before the answer began — order per letter: question → signature → slit → flow |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (unopened) | Printed (pre-state is JS-armed only at trigger approach) | Same |
| Flowing | Wet edge travelling; text selectable throughout (the mask never blocks selection of already-dry lines) | Same |
| Hover | No change — answers are read, not hovered; only the key sentence (§6.10) is interactive | n/a |
| Focus | Key sentence focusable (§6.10); focusing it while unopened opens the letter instantly (skip the flow) | Same |
| Scrolled-past | Written, static | Same |
| Disabled | n/a | n/a |

**v2 — Breakpoint behaviour.** ≥1200px: as specced. 768–1199px: same,
measure narrows to ≤ 58ch. <768px: line pitch shortens (20px/1.5), the
stagger compresses by the same formula; the wet band stays 6px. At no
breakpoint does Caveat/serif size drop below the §3 floors.

**v2 — Edge cases & failure modes.** Answer longer than the design
expects (12+ lines): stagger compression holds the 1200ms law; the flow
reads faster, never longer. Answer of one line: a single 400ms bloom —
still an arrival, not a flash. User scrolls away mid-flow: the flow
completes off-screen (it is cheap) so scroll-back finds written text.
User scrolls *fast* through three letters: the queue (§5.2) writes them
in order, each capped, total worst case bounded by the fallback timers.
Font swap mid-flow: the mask is gradient-based, immune to reflow — lines
may re-wrap under the new font, the wet edge simply continues.

**v2 — Accessibility spec.** The full answer text is in the DOM and
exposed to assistive tech from load — the mask is visual only
(`aria-hidden` on the mask layer; the text node itself is never
`visibility: hidden`). Focus order: question → key sentence (if marked
interactive) → answer's links. Contrast during the bloom: the wet band's
55% opacity floor is transient (< 400ms per line) and the *resting*
contrast is 13.1:1; the band never carries the only copy of anything —
the DOM text is complete beneath it.

**v2 — Tokens consumed.** `--smooth`, `--ink`, `--ease-ink`, `--dur-line`,
`--dur-stagger`, `--dur-fallback`.

### 6.3 The ever-peeking next letter

- **What & why.** At the bottom edge of the viewport, in its envelope,
  sits the next reader's letter — half out, the whole way down. As the
  visitor reads through the current letter, the next one slides further
  out, scrubbed to their progress through the current letter; when the
  current letter is finished, the peeked letter is the one that arrives.
  It makes the reading order physical and promises, truthfully, that
  there is more post. It is the theme's progress cue and its cliffhanger
  in one object.
- **Structure.** A fixed `div.peek` at the viewport foot: an envelope
  (`--envelope`, flap edge in `--envelope-deep`) holding a paper top
  strip showing the *actual next letter's* salutation line in Caveat
  ("Dear Aunt…") — real content, duplicated. The duplicate is
  `aria-hidden="true"` and `inert`; the real letter lives in the flow.
  The column's bottom padding (§4) guarantees the peek never covers the
  line being read.
- **Motion spec.** Scrubbed, via the shared lerp loop (0.12): progress
  through the current letter (0 → 1 between its open and its answer's
  end) maps to paper emergence 18% → 46% of the paper strip's height.
  It never emerges past halfway while fixed — "half out of its envelope"
  is the law; full emergence happens only when the letter itself scrolls
  into the flow. Ambient rustle: a ±1px, 7s-period micro-shift of the
  paper, paused when the tab is hidden or the element is the *last*
  letter (no next letter → no peek; the desk is empty and says so).
- **States.** *Rest (letter start):* 18% out. *Reading:* scrubbed to
  46%. *Between letters:* the peeked paper is now the current letter in
  flow; the fixed peek swaps (instantly, during the scroll, masked by
  the envelope lip) to the following letter at 18%. *Last letter:* the
  peek is absent entirely — an empty envelope would be a lie.
- **Content merge.** The peeking letter is the actual next section: its
  salutation is the next letter's real first line. It is a preview with
  a body, not a "next" button in costume.
- **Failure fallback.** No JS → the fixed peek is not rendered at all
  (it is JS-built); the letters follow each other in the flow, complete.
  Nothing is *only* in the peek.
- **Reduced-motion variant.** No peek. The next letter simply follows in
  the flow; a small printed line at each letter's foot — "Another letter
  follows ↓" in the aunt's furniture voice — carries the same promise
  statically.
- **Performance budget & mobile variant.** One fixed element, one
  transform, updated in the shared loop; the rustle is a transform on the
  paper strip only. Mobile: peek height 38px, emergence range 14% → 40%
  (smaller screens keep more reading room); the salutation truncates to
  "Dear Aunt…" plus the writer's town. On <768px landscape (short
  viewports < 500px tall) the peek hides entirely — reading room wins.

**v2 — Choreography timeline** (continuous, scrubbed; beats at letter boundaries):

| Beat | Scroll position | What happens |
|---|---|---|
| Letter n opens | Reading line crosses letter n | Peek shows letter n+1 at 18% |
| Reading n | Progress 0 → 1 through letter n | Paper emerges 18% → 46%, lerped |
| Letter n completes | Answer n dries | Peek holds 46%; tea ring for n lands (§6.5) |
| Letter n+1 opens | Reading line crosses n+1 | Peek swaps to n+2 at 18% during the same scroll; no visible jump (swap happens behind the envelope lip at the boundary frame) |
| Last letter opens | — | Peek fades its paper down into the envelope over 300ms and the fixed element is removed from the tab order and the DOM |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | 18% out, rustling ≤1px | Same, rustle off (touch devices rarely hover a foot element; stillness is calmer) |
| Hover | Paper rises +3px (a reader's fingers on the envelope) — the only hover | n/a |
| Focus | Not focusable (decorative duplicate, `inert`) | Same |
| Active | Click/tap scrolls to the next letter (progressive enhancement on the visible strip; the element is a duplicate, so this is a convenience, never the only route) | Tap = same |
| Scrolled-past | n/a (fixed) | n/a |
| Disabled | On the last letter: removed, not greyed | Same |

**v2 — Breakpoint behaviour.** ≥1200px: 46px visible, emergence 18–46%.
768–1199px: 42px visible, 16–44%. <768px: 38px, 14–40%, salutation
truncated; viewport height < 500px at any width: hidden.

**v2 — Edge cases & failure modes.** A morning of one letter (short
page): no peek at all — §6.3's last-letter rule applies from the start.
Extremely long current letter: progress is normalised to the letter, so
emergence still completes exactly at its end. Scroll-back up: emergence
reverses with progress (scrubbed, both directions — unlike the tea ring,
the peek is a position, not a record). Browser chrome resizing the
viewport (mobile URL bar): emergence is %-of-paper based, immune.

**v2 — Accessibility spec.** `aria-hidden`, `inert`, no focus, no live
region: assistive tech meets each letter once, in the flow, in order.
The reduced-motion static line ("Another letter follows") is real text
in the flow. The peek never overlaps content (§4 padding law), so no
contrast-under-overlay case exists.

**v2 — Tokens consumed.** `--envelope`, `--envelope-deep`, `--lined`,
`--ink`, `--ease-post`.

### 6.4 Handwritten signature flourish

- **What & why.** Every letter closes with its signature — "— Worried, of
  Walsall" — and the signature *signs itself*: after the letter body has
  landed, a pen flourish (a single underline sweep with a tail curl, the
  way a hand finishes a signature) draws beneath the name. The words are
  real text (§3.5); only the flourish is drawn. It is the moment the
  letter becomes a person's.
- **Structure.** `p.signature` (Caveat 700 text) + an inline SVG flourish
  path positioned under the name, its length measured from the rendered
  name's width at build/trigger time. `pathLength="100"` normalises the
  draw; `stroke-dasharray` animates the reveal. Stroke: `--ink`, 2px,
  round cap — a biro line, never red.
- **Motion spec.** Trigger: the letter's question has fully landed
  (after §6.1/§6.9 settle), before the answer's flow begins (§6.2 queue).
  Draw: 500ms `--ease-draw`, dashoffset 100 → 0, with the final curl
  (last 18% of path) easing into a 60ms hold — the pen lifts. Once drawn,
  permanent: re-scrolling never redraws a signature.
- **States.** *Unsigned (pre-trigger):* the flourish path is absent
  (dashoffset 100) but the signature *text* is fully present — a letter
  is never unsigned in content, only un-flourished in decoration.
  *Signing:* 500ms draw. *Signed:* static biro line.
- **Content merge.** The flourish underlines the actual signature of the
  actual letter; it is part of the letter's paper, positioned by the
  name's real rendered width.
- **Failure fallback.** No JS → flourish renders fully drawn (the armed
  dashoffset is JS-only). Font swap changes the name's width → the path
  re-measures on `document.fonts.ready` and on resize (debounced 200ms)
  before its trigger; if it has already drawn, it stays (a signature
  doesn't move).
- **Reduced-motion variant.** Flourish present, fully drawn, from load.
- **Performance budget & mobile variant.** One SVG path per letter,
  drawn once; negligible. Mobile: identical; the flourish scales with
  the name (Caveat floor sizes hold, §3.4).

**v2 — Choreography timeline** (t = question settled):

| Beat | Time | What happens |
|---|---|---|
| Queue | t + 0ms | Signature waits for the §5.2 one-hand queue |
| Pen down | t + 80ms | Draw begins (80ms after settle — the hand moves to the signature) |
| Sweep | t + 80–500ms | Dashoffset 100 → 18 (the underline sweep) |
| Curl & lift | t + 500–580ms | Final 18% draws with the tail curl; pen-lift hold |
| Done | t + 580ms | Static; answer's slit (§6.8) may now open |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (drawn) | Static biro flourish | Same |
| Hover | No change | n/a |
| Focus | The signature is not interactive; focus passes to the answer's key sentence next | Same |
| Active | n/a | n/a |
| Scrolled-past | Drawn, static; never redraws | Same |
| Disabled | n/a | n/a |

**v2 — Breakpoint behaviour.** All breakpoints: identical behaviour; the
path is measured from the live name width at each size, so the flourish
always spans exactly its name (±4px tail). <768px: stroke 1.8px (finer
paper, finer pen).

**v2 — Edge cases & failure modes.** Long signature ("— At My Wits' End,
of Stoke-on-Trent"): path measures the full two-line wrap? Signatures are
authored to one line (§12); if one wraps, the flourish draws under the
*last* line only — the hand finishes where the name ends. Missing SVG
support: the flourish is dropped, the text stands (progressive
enhancement, no content loss). Print: flourish prints as a static stroke.

**v2 — Accessibility spec.** The SVG is `aria-hidden`, `focusable="false"`.
The signature text is a normal paragraph, read in order. No information
is carried by the stroke. Contrast: `--ink` on `--lined` ≈ 12.8:1.

**v2 — Tokens consumed.** `--ink`, `--ease-draw`, `--dur-draw` (500ms
variant).

### 6.5 Tea-ring progress

- **What & why.** In the margin beside the letters, a tea-ring stain
  darkens — ring by ring — for every letter the visitor finishes. By the
  footer, the margin carries the column's whole morning: this is the
  progress indicator, told as the aunt's desk tells it. A new ring arc
  lands at roughly 70% of the previous ring's opacity, slightly offset,
  slightly larger — rings from a cup set down again and again in nearly
  the same place while she reads.
- **Structure.** An SVG cluster in the margin (§4), one `<circle>` per
  letter in the morning (authored count = the page's real letter count),
  r ≈ 34–44px varying deterministically by index, stroke `--tea` widths
  3–5px with a broken arc (dash gap at a per-ring angle — a ring is a
  stain, not a perfect circle). Rings start at 0 opacity; the *first*
  ring is faintest (the first cup), each subsequent ring darker: ring n
  opacity = 0.16 + 0.09n, capped at 0.78 — the accumulation reads as one
  deepening stain, not n separate badges.
- **Motion spec.** Trigger: a letter is *completed* — its answer has
  dried and the reading line has passed the answer's end. The ring fades
  in over 900ms `--ease-ink` (a stain soaking in, not appearing), with a
  2% scale settle. Rings never un-darken on scroll-back: the stain is a
  record, not a position (contrast §6.3, which is positional and does
  reverse).
- **States.** *Morning start:* no rings (clean desk, first cup not yet
  down). *Reading:* rings accumulate. *Morning complete:* full cluster;
  the footer echoes it (§6.16). *Scrolled-past/back:* unchanged — stains
  don't lift.
- **Content merge.** The rings sit beside the letters that caused them,
  in the margin of the desk the letters are read on; the count *is* the
  letters count, derived from the DOM, never authored separately.
- **Failure fallback.** No JS → all rings render at final opacity (the
  morning read as complete — the honest static state of a printed page).
  If JS runs but the reader jumps to the footer (anchor), rings for
  letters passed are set instantly — position is truth, animation is
  ceremony.
- **Reduced-motion variant.** Rings appear instantly at their earned
  opacity as letters complete; on load with a restored scroll position,
  pre-darkened to match (§5.5).
- **Performance budget & mobile variant.** One SVG, ≤ 9 circles, one
  opacity transition per letter. Mobile (<768px): the margin is gone, so
  the rings move to a slim desk strip above the footer — a horizontal
  cluster, smaller (r ≈ 22–28px), same accumulation law. The progress
  information is never lost, only relocated. Lamplight: per-ring opacity
  increments halve (§2) — shadow hides stains.

**v2 — Choreography timeline** (t = letter completed):

| Beat | Time | What happens |
|---|---|---|
| Complete | t + 0ms | Answer dried + reading line passed its end |
| Soak | t + 0–900ms | Ring n fades 0 → its earned opacity, scale 1.02 → 1 |
| Counter sync | t + 200ms | §6.11 letters-answered tally steps (the ring and the tally are one event, two records) |
| Settle | t + 900ms | Static stain; never animates again |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Earned rings visible at earned opacity | Same (relocated strip <768px) |
| Hover | No change — a stain is not a control | n/a |
| Focus | Not focusable; the *count* is available as text in the header tally (§6.11) | Same |
| Active | n/a | n/a |
| Scrolled-past | Unchanged (record, not position) | Same |
| Disabled | n/a | n/a |

**v2 — Breakpoint behaviour.** ≥1200px: margin cluster beside letter 1,
r 34–44px. 768–1199px: margin narrows; cluster sits above the column's
first letter, r 28–36px. <768px: footer strip, r 22–28px, rings in a row
with the same per-ring offsets compressed horizontally.

**v2 — Edge cases & failure modes.** Morning of 9 letters (max): the
cluster stays legible — ring radii vary so arcs don't align into a
target. Morning of 2 letters: two rings, honestly sparse. Reader
finishes a letter out of order (anchor jump): rings land for every
letter passed, instantly, per the fallback rule. Reader never finishes
the last letter: its ring never lands — correct; the cup is still in
her hand.

**v2 — Accessibility spec.** Decorative record; `aria-hidden`. The same
information ("3 of 7 letters answered") is carried as real text by the
header tally (§6.11), which is where assistive tech meets it. The rings
never carry meaning alone (§2: tea never carries text or meaning alone).

**v2 — Tokens consumed.** `--tea`, `--tea-deep`, `--ease-ink`.

### 6.6 Pinned aunt

- **What & why.** For the middle act of the morning — letters 3 to 5 —
  the aunt herself pins beside the column: her portrait in a taped frame
  and her standing advice (the one piece of counsel she gives everyone,
  printed under her picture) stay in the margin while three letters pass.
  Then she releases and the column finishes the morning alone. She is
  present for the letters she is answering; she is not a mascot glued to
  the whole page.
- **Structure.** `aside.aunt` in the margin (§4): portrait (taped photo
  frame, §6.12 treatment), her name in the nameplate setting, and the
  standing advice in Cormorant italic — real content, authored once.
  Pinning is `position: sticky` within a margin track whose height spans
  letters 3–5 — CSS does the pin; JS only observes the act's boundaries
  for the release lay-down.
- **Motion spec.** Pin: sticky, no animation (she is simply *there* when
  the act begins — a fade would be a ghost, not a presence). Release: at
  the act's end the aside takes a 300ms `--ease-lay` settle — a 4px
  downward lay and the tape's shadow relaxing — as it unsticks and
  scrolls away with the page. The portrait's photo scale-in (§6.12) runs
  once, when the aside first enters, before the pin.
- **States.** *Before the act:* the aside sits in the margin at letter
  3's head, static. *Pinned:* fixed in the margin viewport-relative,
  portrait and advice fully readable. *Released:* scrolls away with the
  desk. *Scrolled-back:* re-pins naturally (sticky is positional) but
  the portrait never re-animates.
- **Content merge.** The pinned content is the columnist and her actual
  standing advice — the page's one piece of evergreen counsel, placed
  where she does her answering.
- **Failure fallback.** No JS → sticky still works (pure CSS); the
  release settle is skipped, nothing else changes. No sticky support
  (ancient): the aside simply sits at letter 3's head in the margin —
  the act reads as an introduction instead of a presence; content
  identical.
- **Reduced-motion variant.** No pin: the aside is placed above letter 3
  in the margin (or above the column at <1200px) and the middle letters
  follow it (§5.5). Presence without the trick.
- **Performance budget & mobile variant.** Sticky is compositor-cheap;
  the settle is one transform. <1200px: there is no margin, so the pin
  never engages — the aside becomes a full-width desk card above letter
  3 (portrait left, advice right; stacked at <480px). The middle-act
  framing survives as placement, not pinning.

**v2 — Choreography timeline** (scroll-driven; beats at act boundaries):

| Beat | Scroll position | What happens |
|---|---|---|
| Approach | Aside enters viewport (before letter 3) | Portrait scale-in runs once (§6.12) |
| Pin | Aside's top reaches 96px from viewport top | Sticky engages; no animation |
| The act | Letters 3, 4, 5 pass | Aside stationary; tea rings accumulate in the same margin below her (§6.5 cluster is above, she is below — the margin's geography is fixed) |
| Release | Letter 5's answer dries | 300ms lay-down settle; sticky releases at the track's end |
| After | Letters 6+ | Margin empty but for rings; the column finishes alone |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (pre-act) | Static in margin | Desk card above letter 3 |
| Pinned | Sticky, fully readable | n/a (no pin <1200px) |
| Hover | No change (her advice is read; the portrait is not a link unless it leads to her about page — if linked, the tape frame lifts per §6.9's physics at half strength) | n/a |
| Focus | If the portrait links anywhere, focus ring is the standard ink ring on the frame | Same |
| Scrolled-past | Released, scrolls with the desk | Static card, scrolled past |
| Disabled | n/a | n/a |

**v2 — Breakpoint behaviour.** ≥1200px: pinned act as specced.
768–1199px: desk card above letter 3, no pin. <768px: desk card stacked
(portrait above advice), placed after letter 2 — on a phone the reader
meets her before the middle letters, since she cannot sit beside them.

**v2 — Edge cases & failure modes.** Morning shorter than 5 letters: the
act compresses — pin spans from letter 3 to the last letter; a morning
of ≤ 2 letters has no act and no pin (she is in the header; that is
enough of her). Very tall viewport (≥ 1400px): pin offset stays 96px;
her advice must never pin *above* the letter being read. Portrait fails
to load: the frame holds her name and the advice — presence survives
the photo (§6.12 fallback).

**v2 — Accessibility spec.** The aside is a `<aside aria-label="About
the aunt">` in DOM order at letter 3 — screen readers meet her where
she stands, not where she pins. The standing advice is plain text.
Portrait `alt` is her name and role ("Margaret Hale, the column's
aunt") — she is a real, named person in the fiction (§1 law protects
readers, not her).

**v2 — Tokens consumed.** `--smooth`, `--ink`, `--ink-soft`, `--tape`,
`--ease-lay`.

---

### 6.7 The single kiss mark

- **What & why.** Exactly once on the whole page, beside one particular
  letter, a lipstick kiss mark draws itself — a reader's gesture,
  pressed to the paper before posting, preserved in the column. It is
  never explained, never captioned, never repeated. Its power is
  entirely in its singularity and its silence: a second kiss anywhere on
  the page turns it into clip-art, and a caption turns it into a joke.
- **Structure.** An inline SVG lip-print path (two lip arcs with the
  centre parting line, drawn as 3 strokes) placed in the letter's margin
  area on the question stock, rotated −8°, sized ≈ 54 × 40px, stroke
  `--lipstick` at 88% opacity with a slight double-strike offset (a
  second path at 22% opacity, translated 1px — a real kiss is not a
  stamp). Which letter carries it is an editorial decision, authored
  once per page via a single `data-kiss` attribute; the build fails if
  more than one exists (§10, blocking).
- **Motion spec.** Trigger: that letter's question has landed and its
  signature has signed (§5.2 queue — the kiss is the last event on its
  letter). Draw: strokes in sequence, 800ms total `--ease-draw`
  (upper lip 0–340ms, lower lip 300–640ms, parting line 600–800ms),
  opacity blooming 60% → 88% as each stroke lands — lipstick laid, not
  printed. Once drawn: permanent, inert, never redrawn.
- **States.** *Absent (every other letter):* nothing — the mark's absence
  elsewhere is part of the spec. *Drawing:* 800ms, once. *Drawn:* static
  mark on the paper. No hover, no focus, no click — it is not a control
  and must never behave like one.
- **Content merge.** The mark is *on that letter's paper*, placed where
  a reader's lips would land — beside the signature, not in the margin
  furniture. It belongs to the correspondence, not the chrome.
- **Failure fallback.** No JS → the mark renders fully drawn (the armed
  dashoffset is JS-only). It is decoration on a complete letter; its
  absence (SVG unsupported) loses nothing the reader needs.
- **Reduced-motion variant.** Present, fully drawn, from the moment its
  letter is reached — the mark without the drawing.
- **Performance budget & mobile variant.** Three SVG paths, once.
  Mobile: identical placement relative to the signature; size 46 × 34px
  (smaller paper). Never moved to a "better" spot — where the reader
  kissed the page is where it stays.

**v2 — Choreography timeline** (t = its letter's signature complete):

| Beat | Time | What happens |
|---|---|---|
| Queue clear | t + 0ms | Signature done; nothing else on the letter is moving (§5.2) |
| Upper lip | t + 120–460ms | First stroke draws (120ms pause first — the lean-in) |
| Lower lip | t + 420–760ms | Second stroke, overlapping the first's tail |
| Parting line | t + 720–920ms | Centre stroke; opacity settles at 88% |
| Still | after | Permanent; the page's one kiss |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (drawn) | Static mark on the paper | Same |
| Hover | No change, no cursor change, no tooltip — ever | n/a |
| Focus | Not focusable | Same |
| Active | Not clickable | Same |
| Scrolled-past | Drawn, static | Same |
| Disabled | n/a | n/a |

**v2 — Breakpoint behaviour.** ≥1200px and 768–1199px: 54 × 40px beside
the signature. <768px: 46 × 34px; if the signature line is full-width,
the mark sits at the signature's right end, overlapping the paper's edge
by 6px — kissed at the corner of the page.

**v2 — Edge cases & failure modes.** Page with no letter marked: a valid
build (some mornings have no kiss) — the gate checks *at most one*, not
exactly one. Template reuse across pages: the `data-kiss` must be
re-authored per page; a layout that auto-applies it to every page's
third letter is a gate failure (§9.4). Print: the mark prints, drawn.

**v2 — Accessibility spec.** `aria-hidden="true"`, no role, no label.
It is never announced, never described in alt text, never explained to
any reader in any modality. That is the spec, not an oversight: the
theme's one unexplained thing stays unexplained.

**v2 — Tokens consumed.** `--lipstick`, `--ease-draw`, `--dur-draw`
(800ms variant).

### 6.8 Letter-slit answer reveal

- **What & why.** Before an answer flows (§6.2), it is *drawn out*: the
  answer paper reveals through a horizontal letter-slit — a clip-path
  that starts as the narrow mouth of an envelope and widens as the paper
  comes out. The slit is the envelope the reply arrived in; the widening
  is the reply being taken out and opened on the desk. It precedes the
  ink-flow by a breath, so the reader sees paper first, then writing.
- **Structure.** `section.answer` with a JS-armed pre-state
  `clip-path: inset(0 46% 0 46%)` — wait, a letter-slit is horizontal:
  the clip is `inset(42% 0 42% 0)` at arm (a horizontal slit across the
  paper's middle), widening to `inset(0 0 0 0)`. The paper's shadow
  deepens at the slit edges during the widen (two 1px `--envelope-deep`
  rules at the clip boundary, fading as it opens). In the DOM and in
  layout the answer always occupies its full height — the clip is
  visual only, so nothing reflows.
- **Motion spec.** Trigger: letter opened, after the question settles
  and the signature signs (§6.2 timeline). Widen: 500ms `--ease-unfold`.
  The ink-flow's first line starts at +160ms into the widen, so writing
  begins while the paper is still emerging — the aunt starts before the
  page is fully flat, as a person does.
- **States.** *Armed:* slit at 42% inset (JS-only pre-state). *Opening:*
  500ms widen. *Open:* clip removed entirely (not left at inset 0 — a
  permanent clip-path on text is a selection/rendering hazard). *Re-entry:*
  never re-arms; an opened envelope stays open.
- **Content merge.** The slit belongs to the answer's own envelope-paper
  relationship; the paper revealed is the answer itself, on its smooth
  stock, in its place under the question.
- **Failure fallback.** No JS → no clip is armed; answers are printed
  whole. If the flow (§6.2) is skipped by a low-power signal, the slit
  still opens (it is cheaper than the flow) — paper before print, always
  in that order.
- **Reduced-motion variant.** No slit: the answer is simply present
  under its question.
- **Performance budget & mobile variant.** `clip-path` inset animation
  is compositor-friendly on a single element; one at a time via the
  queue. Mobile: identical; slit arm inset is 38% (a shorter paper
  needs a relatively wider mouth to read as a slit).

**v2 — Choreography timeline** (t = letter opened, question settled, signature signed):

| Beat | Time | What happens |
|---|---|---|
| Arm | before t | Clip armed as the letter approaches the reading line |
| Widen | t + 0–500ms | Inset 42% → 0, `--ease-unfold`; slit-edge rules fade 300–500ms |
| Ink begins | t + 160ms | §6.2 first line blooms while the paper still widens |
| Open | t + 500ms | Clip-path removed; answer is plain paper |
| Dry | per §6.2 | Flow completes; letter fully arrived |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (opened) | Full paper, no clip | Same |
| Opening | 500ms widen; text beneath is real and selectable once its region un-clips | Same |
| Hover | No change | n/a |
| Focus | Focusing the key sentence inside an unopened answer opens the slit instantly (skip ceremony) | Same |
| Scrolled-past | Open, static | Same |
| Disabled | n/a | n/a |

**v2 — Breakpoint behaviour.** All breakpoints identical except the arm
inset (<768px: 38%). The widen duration never changes — 500ms is the
aunt's pace, not a responsive variable.

**v2 — Edge cases & failure modes.** Very tall answer (12+ lines): the
slit widens over the full height — the clip is proportional (inset %),
so tall paper opens as gracefully as short. Answer re-opened by a
focus jump (§6.2 focus rule): instant open, no widen. Browser without
clip-path animation support: the clip steps (arm → none) — the paper
appears whole; acceptable degradation, content untouched.

**v2 — Accessibility spec.** The clip is visual only; the answer text is
in the accessibility tree in full from load (clip-path does not remove
content from AT). No aria state changes are announced — an answer
arriving is not an interruption. Contrast is the resting 13.1:1
throughout (the clip hides by geometry, never by fading text).

**v2 — Tokens consumed.** `--smooth`, `--envelope-deep`, `--ease-unfold`.

### 6.9 Envelope-lift hover

- **What & why.** Hovering a letter lifts it a few millimetres further
  from its envelope and tilts it, like paper picked up between finger
  and thumb to be read more closely. It is the theme's one piece of
  hover physics, and it acts on the letter *and its envelope together* —
  the paper and the thing it came in move as one object in the hand.
- **Structure.** The letter article (question stock + answer stock +
  its envelope tab at the foot) transforms as a unit: `translateY(-4px)
  rotate(±0.5°)` from its laid rotation toward 2° total tilt ceiling,
  with the fold shadow beneath deepening (the `::after` desk shadow:
  blur 14px → 22px, opacity 14% → 22%, offset +6px). Transform origin:
  bottom-left — the corner a thumb would hold.
- **Motion spec.** In: 240ms `--ease-lay`. Out: 320ms `--ease-lay` (paper
  settles slower than it lifts — gravity is patient). Tilt direction
  follows the letter's laid-rotation sign, so each letter picks up in
  its own direction. Only one letter lifts at a time; moving directly
  between letters hands the lift over with no double-shadow frame.
- **States.** *Rest:* laid rotation (±0.3–0.6°), resting shadow.
  *Hover:* lifted −4px, tilted toward 2°, deepened shadow. *Focus-within:*
  the same lift at half strength (−2px) — keyboard readers get the
  paper-in-hand signal too. *Active (pressing a link inside):* lift
  holds; the link's own press is §6.10/§6.13 behaviour.
  *Scrolled-past:* rest.
- **Content merge.** The lift acts on the letter itself — its paper, its
  envelope tab, its shadow. Nothing decorative is lifted; the content is
  the object.
- **Failure fallback.** Transforms are enhancement: no JS is required
  (pure CSS `:hover`/`:focus-within`), and if transforms are
  unavailable the letter simply doesn't lift. Content never depends on
  it.
- **Reduced-motion variant.** No lift, no tilt. Hover instead deepens
  the letter's hairline edge by one step (`--ink-faint` border) — a
  static acknowledgment.
- **Performance budget & mobile variant.** One transform + one shadow
  per letter, hover-only. Touch: no hover — a tap on the letter's
  envelope tab gives the lift for 240ms as a press acknowledgment
  (the paper is picked up when touched, which is honest), links inside
  still work on their own targets; the lift never swallows a tap.

**v2 — Choreography timeline** (t = pointer enters the letter):

| Beat | Time | What happens |
|---|---|---|
| Lift | t + 0–240ms | translateY 0 → −4px, rotation toward 2° ceiling, `--ease-lay` |
| Shadow | t + 40–280ms | Desk shadow deepens and drops +6px (lags the paper 40ms — shadows follow) |
| Hold | while hovered | Static lifted state; §6.10 targets inside remain live |
| Release | pointer leaves, 320ms | Paper lays back to its authored rotation and shadow |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Laid, resting shadow | Same |
| Hover | Lifted −4px, tilt ≤2°, deep shadow | n/a |
| Focus | `:focus-within` lift at −2px | Same (keyboard/switch) |
| Active | Lift holds during press | Tap on envelope tab: 240ms lift pulse |
| Scrolled-past | Rest (no lift retained) | Same |
| Disabled | n/a — a letter is never disabled | n/a |

**v2 — Breakpoint behaviour.** ≥1200px: as specced. 768–1199px: lift
−3px, tilt ≤1.5°. <768px: no hover lift (touch rules above); the
focus-within half-lift remains for switch/keyboard users.

**v2 — Edge cases & failure modes.** Pointer skims across three letters
quickly: lifts queue-cancel — a letter whose hover ends before 240ms
releases from its current position (CSS transitions handle this
natively; no JS state). Letter taller than the viewport: origin
bottom-left keeps the lift from shifting the top (salutation) line the
reader is on — the paper pivots at the thumb corner. Reduced-data /
low-power: lift retained (it is two composited properties, cheaper
than the ambient loops that *are* cut first, §14).

**v2 — Accessibility spec.** Hover never reveals content — everything
readable lifted is readable laid. Focus-within lift ensures the
keyboard user's current letter is visually identified. Tilt ceiling
2° keeps text within comfortable reading angles; contrast is unchanged
at every frame (colours don't move, positions do). Touch targets
inside the letter are unaffected (transform doesn't change hit areas
in CSS — the browser maps them correctly).

**v2 — Tokens consumed.** `--ink`, `--ease-lay`, `--dur-lift`.

### 6.10 Key-sentence underline click

- **What & why.** Every answer has one key sentence — the sentence the
  aunt would underline if she were marking her own counsel. Clicking the
  answer underlines that sentence in lipstick red: a pen stroke drawn
  beneath the words. It is the theme's single call-to-attention, and the
  red's second licensed job (§2). Readers use it to find the point; the
  aunt uses it to make one.
- **Structure.** The key sentence is authored markup: `<span
  class="key" tabindex="0" role="button" aria-pressed="false">` inside
  the answer (one per answer, exactly one — §10 checks). The underline
  is an SVG-free drawn stroke: a `background-image` linear-gradient in
  `--lipstick` won't draw; so the stroke is a `::after` bar with a
  hand-drawn SVG mask (a slightly wobbling 3px line, path authored once,
  stretched to the sentence's width via `background-size: 100% 100%`),
  revealed by a `clip-path` left-to-right draw. Multi-line key sentences
  (they wrap) use `box-decoration-break` underlines per line, drawn in
  reading order — the mask repeats per line box.
- **Motion spec.** Trigger: click / tap / Enter / Space on the key
  sentence. Draw: 300ms `--ease-draw`, left to right, stroke opacity
  92%. The mark is toggleable: a second activation rubs it out (a 200ms
  fade — erasing is quicker than marking, and less certain: a faint 12%
  ghost of the stroke remains, because pencil-and-lipstick marks never
  fully leave paper). Re-marking restores full 92% over the ghost.
- **States.** *Unmarked:* plain sentence; on hover/focus the sentence
  takes a 6% `--lipstick` wash (the pen hovering — the only hint it is
  markable). *Marking:* 300ms draw. *Marked:* `aria-pressed="true"`,
  stroke at 92%, persistent for the session (and across scroll — the
  aunt does not un-mark because you looked away). *Rubbed out:* 12%
  ghost, `aria-pressed="false"`.
- **Content merge.** The underline is on the answer's own sentence, in
  the answer's own red ration — it marks content, it is not a button
  styled as one.
- **Failure fallback.** No JS → the key sentence renders pre-underlined
  (the static truth of a printed column: the aunt already marked it).
  The toggle is the enhancement; the mark is the content.
- **Reduced-motion variant.** The underline appears/disappears instantly
  (no draw); the ghost rule still applies.
- **Performance budget & mobile variant.** One pseudo-element per
  answer. Mobile: tap target is the sentence itself (min height 32px
  via its line box; if the sentence is short, its tap area extends to
  the full line width — a sentence is marked by tapping its line, §6.10
  a11y). The 6% hover wash has no touch equivalent; a first tap marks
  (no hover-dependency for the affordance: the sentence carries a
  dotted `--ink-faint` baseline hint on touch layouts — the pencil
  guideline under the sentence she means).

**v2 — Choreography timeline** (t = activation):

| Beat | Time | What happens |
|---|---|---|
| Press | t + 0ms | Wash deepens to 10% (the pen touches) |
| Draw | t + 0–300ms | Stroke clips in left → right, `--ease-draw` |
| Settle | t + 300ms | Stroke at 92%; `aria-pressed` flips at draw end, not start (the state is the finished mark) |
| Rub out (2nd activation) | 200ms | Fade to 12% ghost |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (unmarked) | Plain; hover wash 6% | Dotted guideline hint under the sentence |
| Hover | Wash 6%, cursor stays the normal text cursor (it is a sentence, not a link — the wash is the affordance) | n/a |
| Focus | Wash 8% + standard focus ring on the sentence box | Same |
| Active | Draw runs (300ms) | Same on tap |
| Marked | Stroke 92%, persistent | Same |
| Disabled | n/a — every answer's key sentence is always markable | n/a |

**v2 — Breakpoint behaviour.** Identical at all breakpoints; the stroke
mask stretches to the sentence's rendered width at each size and
re-stretches on resize (the mark follows its words). <768px: stroke
2.6px (finer paper).

**v2 — Edge cases & failure modes.** Key sentence wraps to 3 lines:
per-line strokes draw in sequence within the same 300ms (100ms per
line). Answer with no authored key sentence: a build error, not a
runtime state (§10 blocking — every answer has exactly one). Visitor
marks every sentence on the page: allowed; the red ration is measured
on *authored* red (kiss + postmark + unmarked state), and reader-made
marks are the reader's own — but §9.7 names the design-side version of
this failure (pre-marking everything) as slop. Print: marked state
prints as marked.

**v2 — Accessibility spec.** Real button semantics on a span is a
compromise; preferred build: the sentence inside a `<button
class="key">` styled to inherit the serif — same visuals, native
semantics. Either way: `aria-pressed` reflects the mark, the accessible
name is the sentence text + ", key sentence — press to underline".
Focus visible: ring in `--ink` (never lipstick — focus is furniture,
not a mark). Contrast: the sentence text is `--ink` at 13.1:1 in every
state; the stroke is decoration under text, exempt from text contrast
but held at 92% opacity so it reads as a mark at a glance. Touch target
≥ 32px tall via the line box rule above.

**v2 — Tokens consumed.** `--lipstick`, `--ink`, `--ink-faint`,
`--ease-draw`, `--dur-draw` (300ms variant).

### 6.11 Aunt's header counters

- **What & why.** In the aunt's header, two tallies keep the morning's
  accounts: **letters answered** and **cups of tea**. They count up as
  letters complete — the column's own bookkeeping, in her nameplate's
  furniture. Both numbers are *derived, never authored*: letters
  answered is the count of letters the visitor has actually finished on
  this page; cups of tea is a deterministic function of it (below). An
  invented tally is a gate failure (§10) — the desk does not lie about
  its own morning.
- **Structure.** `header` nameplate block: two `dl`-style tally pairs in
  Cormorant tabular figures, `--ink-soft`, 15px small caps labels
  ("Letters answered", "Cups of tea") with 22px figures. The figures are
  live text nodes updated by the completion event (§6.5's sync beat).
  The derivation law: `cups = 1 + floor(answered / 3)` once
  `answered ≥ 1`, else `cups = 1` (the first cup is poured before the
  first letter — the morning starts with tea). The law is stated here so
  two builders produce the same header.
- **Motion spec.** Trigger: a letter completes (§6.5). The changed
  figure counts up over 700ms `--ease-ink` — for letters, +1 is a single
  step-flip at 350ms (numbers on a desk tally do not odometer-roll
  through fractions; the figure fades 40% → 100% as it changes, a pen
  amending a ledger). Cups changes only when the derivation crosses a
  multiple of 3, with the same treatment.
- **States.** *Morning start:* "Letters answered 0 · Cups of tea 1".
  *Counting:* the 700ms amendment. *Morning complete:* final figures,
  echoed in the footer (§6.16). *Scrolled-past:* the header is gone;
  the tallies' truth lives on in the rings (§6.5) and footer.
- **Content merge.** The tallies measure this column's actual
  correspondence, in the column's own header — bookkeeping, not a stats
  widget.
- **Failure fallback.** No JS → the header prints the morning's *full*
  figures (total letters on the page; cups by the same derivation from
  the total) — the printed column's end-of-day accounts. With JS, they
  start at the visitor's true position (0, or restored from scroll).
- **Reduced-motion variant.** Figures change instantly at completion
  events.
- **Performance budget & mobile variant.** Two text nodes. Mobile: the
  tallies sit under the nameplate in one line, 13.5px labels; nothing
  is cut — the accounts are small.

**v2 — Choreography timeline** (t = letter completes):

| Beat | Time | What happens |
|---|---|---|
| Ring sync | t + 200ms | §6.5 ring begins its soak (same event) |
| Figure amend | t + 200–900ms | Letters figure fades to 40%, new value, back to 100% (700ms `--ease-ink`) |
| Cups check | t + 900ms | If derivation crossed a multiple of 3, cups figure amends the same way, 200ms later |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Current true figures | Same |
| Hover | No change | n/a |
| Focus | Not interactive | Same |
| Active | n/a | n/a |
| Scrolled-past | Header gone; truth persists in rings/footer | Same |
| Disabled | n/a | n/a |

**v2 — Breakpoint behaviour.** ≥1200px: tallies right of the nameplate.
768–1199px: tallies right, labels shorten to "Letters" / "Cups" only if
space forces (never below 13.5px). <768px: one line under the nameplate.

**v2 — Edge cases & failure modes.** Restored scroll mid-page: figures
initialise to the true count of letters above the reading line,
instantly (no count-up theatre for history). Anchor jump to footer:
all letters passed count as answered (§6.5's rule) and the tallies
agree with the rings — the two records must never disagree; a
disagreement is a bug the gate hunts (§10). Page with 1 letter:
"Letters answered" goes 0 → 1; cups stays 1.

**v2 — Accessibility spec.** The tallies are plain text, read in order.
They are NOT a live region — a tally changing is not worth interrupting
a screen-reader user mid-letter; the values are simply correct whenever
the header is read. Figures use tabular Cormorant so the header doesn't
reflow as digits change. Contrast `--ink-soft` on newsprint ≈ 5.9:1.

**v2 — Tokens consumed.** `--ink-soft`, `--ink`, `--ease-ink`,
`--dur-count`.

### 6.12 Taped-photo frames + envelope transitions

- **What & why.** Two duties, one paper logic. (a) Photographs on the
  page — the aunt's portrait, a reader's enclosed snapshot (described,
  never of an identifiable reader, §1), the office view — live in taped
  frames: the photo sits in a plain border with two strips of tape at
  its top corners, and scales in-frame as it enters. (b) Movement
  between pages travels by post: on navigation the current letter slides
  back into its envelope, and the next page's first letter is drawn out
  of the slot — loading states are blank lined skeleton envelopes
  waiting for their letters.
- **Structure.** (a) `figure.taped`: photo + two `span.tape` strips
  (`--tape` at 82%, 64 × 22px, rotated −4°/+3°, torn-edge via clip-path
  polygon with 6 points — tape is torn, not cut). The photo is clipped
  by the frame; scale applies to the photo only. (b) A route-change
  overlay is *not* used: the transition animates the leaving page's
  hero letter back up into a slot bar rendered at the page head
  (450ms), then the new page loads with its own §6.1 arrival — the
  post travels between real pages, not inside a fake one. Skeleton:
  `div.skeleton-envelope` — an envelope outline holding blank `--lined`
  paper with 5 rule lines and no handwriting (a letter not yet
  received cannot have writing on it — §9.8).
- **Motion spec.** (a) Scale-in-frame: photo 1.05 → 1, 600ms
  `--ease-lay`, triggered at the frame's entry (30% visible); tape
  never moves; frame shadow settles with the photo. (b) Out: hero
  letter slides up into the slot, 450ms `--ease-post`, rotation to
  −1.1° (the reverse of §6.1 — same paper, same slot, opposite
  direction); navigation proceeds at slide end. Skeleton envelopes
  show only for genuine waits > 300ms and receive their letters with
  the §6.1 slide when content lands.
- **States.** (a) *Rest:* photo still, tape still. *Entering:* the one
  scale-in. *Scrolled-past:* still — photos do not keep performing.
  (b) *Leaving:* slide-up. *Loading:* skeleton envelope, static (a
  waiting envelope does not shimmer — §9.8). *Arrived:* §6.1.
- **Content merge.** The tape is on the photo's own corners; the
  transition moves the page's actual hero letter. Both are the site's
  transport and memorabilia, not decoration.
- **Failure fallback.** (a) No JS → photos simply present in their
  frames. (b) Transition is progressive enhancement over plain links:
  if the slide cannot run (prefetch, middle-click, JS off), navigation
  is instant and normal. Skeleton only ever replaces a *loading*
  region, never authored content.
- **Reduced-motion variant.** (a) Photos present, no scale. (b) No
  slide; navigation is instant; a skeleton shows the word "Receiving…"
  in the furniture voice if a wait exceeds 300ms (information, not
  theatre).
- **Performance budget & mobile variant.** (a) One transform per photo,
  ≤ 3 photos per page in this theme (the desk is not a gallery).
  (b) The slide is one transform on an existing element. Mobile:
  identical; tape strips 52 × 18px.

**v2 — Choreography timeline** (b, t = navigation activated):

| Beat | Time | What happens |
|---|---|---|
| Commit | t + 0ms | Leaving page's hero letter begins slide-up (450ms `--ease-post`), rotation → −1.1° |
| Travel | t + 450ms | Navigation fires; browser loads the next page |
| Arrival | next page | §6.1 timeline runs (or skeleton if content is genuinely pending > 300ms) |

(a) timeline: frame 30% visible → photo scale 1.05 → 1 over 600ms, shadow settles at +500ms.

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Photo still in taped frame | Same |
| Hover | Frame lifts at half §6.9 strength if the photo is a link; otherwise none | n/a |
| Focus | Linked photo: standard ring on the frame | Same |
| Active | Navigation begins the slide-up | Same |
| Scrolled-past | Still | Same |
| Disabled | n/a | n/a |

**v2 — Breakpoint behaviour.** All breakpoints: same behaviours; tape
and frame scale per §6.12 mobile note. The transition's slot bar is
rendered at every size (it is header furniture, §4).

**v2 — Edge cases & failure modes.** Photo fails to load: the frame
holds its caption and a `--lined` blank with the furniture-voice line
"Photograph to follow" — a missing photo is acknowledged in the
fiction, never a broken-image icon. Slow route (> 300ms): skeleton
envelope appears in the *destination* region only after the wait is
real. Back button: the browser's own history wins; no slide is forced
on a popstate the user didn't choose from this page. Print: tape
prints as its translucent tint; transitions/skeletons never print.

**v2 — Accessibility spec.** Photos carry real `alt` (the aunt's
portrait: §6.6; a reader's snapshot: described by its content, never a
name). Tape is `aria-hidden`. The transition never traps focus: focus
moves to the new page's heading on arrival (standard route behaviour),
and the slide is skipped entirely for users with reduced motion or
when the navigation is programmatic. Skeleton regions use
`aria-busy="true"` on the region they stand in for, released on
arrival.

**v2 — Tokens consumed.** `--tape`, `--lined`, `--envelope-deep`,
`--ink-soft`, `--ease-lay`, `--ease-post`, `--dur-transition`,
`--dur-slide`.

---

### 6.13 Postbag navigation (page family: navigation)

- **What & why.** The site's navigation is the column's postbag: a slim
  header under the nameplate listing the column's departments as
  destinations on envelopes — *This Morning*, *Past Mornings* (the
  archive), *About the Aunt*, *Write In*. The current department's
  envelope sits open (flap up, paper edge showing); the others are
  sealed. Navigation by postbag keeps the fiction at the one place
  themes usually abandon it — the chrome.
- **Structure.** `nav.postbag`: a row of envelope tabs (`--envelope`
  stock, 44px tall), label in furniture small caps (§3), the current
  one open: flap (a `--envelope-deep` triangle) rotated up, a 6px
  `--smooth` paper edge visible at its mouth. A postmark stamp at the
  row's right end — `--lipstick`, the red's third licensed job — carries
  the column's town and the real month ("Walsall · November"), rotated
  −6°, printed (static) texture.
- **Motion spec.** On load, the current envelope's flap settles open
  over 300ms `--ease-unfold` (it was already open; the settle is the
  page arriving at the desk). Hover on a sealed envelope: its paper
  edge rises 3px inside the mouth (240ms `--ease-post`) — the letter
  inside, waiting. Route change runs §6.12(b).
- **States.** *Current:* open, paper showing, `aria-current="page"`.
  *Sealed (others):* flat. *Hover:* paper edge +3px. *Focus:* ink ring
  on the envelope. *Scrolled:* the postbag scrolls away with the header
  — the desk's chrome is not sticky; the peek letter (§6.3) is the
  page's only fixed object.
- **Content merge.** The tabs are the site's real sections, labelled as
  the column's own departments; the postmark carries real place/date
  information (the column's home town, the current month — computed,
  not invented).
- **Failure fallback.** Plain list of links without JS; the open/sealed
  states are CSS classes from the server/router, not JS guesses.
- **Reduced-motion variant.** Flap static open; hover rise replaced by
  the paper edge simply being visible at 2px on hover/focus.
- **Performance budget & mobile variant.** CSS-only. <768px: the
  postbag wraps to two rows of two envelopes; the postmark moves to the
  nameplate line. Labels never shrink below 13.5px.

**v2 — Choreography timeline.** Load: flap settle 0–300ms, then still.
Hover: paper edge 0–240ms in, 200ms out. Nothing else ever moves here.

**v2 — State matrix.** Rest: current open, others sealed (both
modalities). Hover: edge +3px (desktop). Focus: ring + edge shown.
Active: §6.12(b) slide begins. Scrolled-past: gone with the header.
Disabled: a department with no letters yet is *not* disabled-styled —
it links to its empty state (§6.17), because an empty postbag is a
page, not a grey button.

**v2 — Breakpoint behaviour.** ≥1200px: one row, postmark right.
768–1199px: one row, postmark shrinks to town only. <768px: 2 × 2 wrap,
postmark beside the nameplate.

**v2 — Edge cases & failure modes.** Long department names ("Letters
From the Night Shift"): envelopes grow, labels wrap to two lines at
13.5px floor — the row wraps before any label truncates. More than 5
departments: the theme refuses more than 5 (a column has a handful of
departments; a 9-tab postbag is a sitemap in costume — split the site).

**v2 — Accessibility spec.** Real `<nav>` with a list; `aria-current`
on the open envelope; the flap/paper visuals are `aria-hidden`. Focus
order follows the visual order. Contrast: labels `--ink` on
`--envelope` ≈ 8.9:1; the postmark is decorative text at 15px italic —
its information (town, month) is duplicated in the About page's real
text.

**v2 — Tokens consumed.** `--envelope`, `--envelope-deep`, `--smooth`,
`--lipstick`, `--ink`, `--ease-unfold`, `--ease-post`.

### 6.14 Letter cards — the past mornings index (page family: cards)

- **What & why.** On listing pages (Past Mornings, topic shelves), each
  past letter is a card shaped as what it is: the top of its envelope,
  showing the salutation's first line in Caveat, its signature
  ("— Worried, of Walsall"), its topic in the furniture voice, and the
  date it was answered. Cards are envelopes in a postbag rack — filed,
  not tiled.
- **Structure.** `article.letter-card`: `--envelope` stock, flap line
  across the top third, Caveat excerpt (2 lines max, the letter's real
  opening), signature line, furniture footer row (topic · date ·
  "Answered" with a small tea ring glyph echoing §6.5 when the visitor
  has read it — the read-state ring is drawn from the same record).
- **Motion spec.** Entry: cards are dealt from the postbag — each
  slides up 14px and settles, 380ms `--ease-post`, stagger 70ms, max 6
  animating at once. Hover: §6.9's lift at full strength (these are
  letters; the lift law applies). The read-ring draws (300ms
  `--ease-draw`) when a card's letter is completed elsewhere.
- **States.** *Unread:* plain envelope. *Read:* tea-ring glyph present
  beside "Answered". *Hover/focus-within:* lifted. *Current morning's
  letters:* not cards — the home page shows letters in full (§6.1–6.11);
  cards are for the archive only.
- **Content merge.** Every field on the card is the letter's own data:
  its real opening line, its real signature, its real date.
- **Failure fallback.** Static envelopes in a list; entry animation is
  JS-armed only.
- **Reduced-motion variant.** Cards present; read-rings appear
  instantly.
- **Performance budget & mobile variant.** Transforms only. <768px:
  one column of full-width envelopes; stagger reduced to 40ms (a
  shorter rack).

**v2 — Choreography timeline.** Entry (t = card 30% visible): slide
+14px → 0 over 380ms, stagger 70ms by index within the visible batch.
Read-ring: on the completion event, 300ms draw, once.

**v2 — State matrix.** Rest: filed envelope. Hover: lifted (desktop).
Focus: lift at half + ring. Active: navigates (with §6.12(b) where the
destination is a letter page). Scrolled-past: filed, static. Disabled:
n/a — an unanswered letter (see §6.17) shows "Awaiting the aunt" in the
footer row instead of a date; it still links to its page.

**v2 — Breakpoint behaviour.** ≥1200px: 3 per row in the rack.
768–1199px: 2 per row. <768px: 1 per row, excerpt 3 lines (narrower
paper shows more of the letter, honestly).

**v2 — Edge cases & failure modes.** Letter with a very long opening
line: excerpt truncates at 2 lines with an ellipsis *in Caveat* (the
hand trails off) — never a furniture-voice "Read more" on the card
face; the whole card is the link. Missing date: the footer shows the
postmark month only; a card never invents a date (§12).

**v2 — Accessibility spec.** The card is one link (the letter's
heading), not five; the accessible name is "Letter from Worried, of
Walsall — answered [date]". Read-state is conveyed in text ("Answered")
not by the ring glyph alone. Contrast: Caveat `--ink` on `--envelope`
≈ 9.7:1.

**v2 — Tokens consumed.** `--envelope`, `--envelope-deep`, `--ink`,
`--ink-soft`, `--tea`, `--ease-post`, `--ease-draw`.

### 6.15 Write to the aunt (page family: forms / conversion)

- **What & why.** The conversion is a letter, written by the visitor:
  the form is a sheet of the lined stock with three fields — your
  letter (the body), how you will sign it (feeling + town, per the
  law), and an email for her reply (kept off the page, as real replies
  are). Submitting is *posting*: the sheet slides into an envelope and
  the envelope into the slot. The form is where the theme's fiction
  becomes the visitor's own act, so it is built with more care than
  any other element here.
- **Structure.** `form.write-in` on `--lined` stock inside an envelope
  surround. Fields are ruled lines on the paper (the visitor types in
  Caveat 22px — they are handwriting now, §3). The letter field is a
  textarea whose line-height matches the 28px rule pitch, so typed
  lines sit on the printed rules. Signature field is two short inputs
  ("—" printed before the first, ", of" between them — the format is
  furniture, the words are the visitor's). Submit is a furniture-voice
  button styled as a postmark-edged slip: "Post my letter".
- **Motion spec.** Focus: the field's rule line inks from `--rule-line`
  to `--ink` (200ms) — the line she will read along. Submit: the sheet
  folds (top third folds down, 300ms `--ease-unfold`), slides into the
  envelope (400ms `--ease-post`), the envelope rises into a slot bar at
  the form's head (300ms), and the confirmation replaces the form: a
  smooth-stock note in the aunt's voice (§12) with a real reference
  ("Received as letter № 214 of this morning's post" — the number is
  the real submission count from the backend, or the line is omitted;
  never invented). Error: the sheet does not fold; the offending field's
  rule turns `--tea-deep` and the aunt's note appears in the margin in
  Cormorant italic ("The column needs a way to write back — may we have
  the email again?") — errors are counsel, not alarms, and never red.
- **States.** *Rest:* blank ruled sheet. *Writing:* rules ink per
  field. *Error:* tea rule + margin note, focus moved to the field,
  persistent until corrected. *Posting:* the fold/slot sequence,
  fields inert. *Posted:* confirmation note, permanent for the visit;
  the peek letter (§6.3) is absent on this page — the visitor's letter
  is the next letter now, and the fiction does not double it.
- **Content merge.** The form *is* the product's conversion (a letter
  to the column / a coaching enquiry / a podcast submission); its
  fields are the real data, its posting is the real submission.
- **Failure fallback.** A plain HTML form on paper styling: labels,
  inputs, native validation messages re-voiced server-side in her
  voice. No JS → submit is a normal POST; the confirmation is a real
  page. The fold is ceremony over a working form.
- **Reduced-motion variant.** No fold, no slide: on submit, the form
  is replaced by the confirmation with a 150ms fade. Errors identical
  (they were never motion).
- **Performance budget & mobile variant.** The fold/slide is three
  transforms on one sheet, once per submission. <768px: the signature
  pair stacks ("—" and ", of" furniture stays inline); the textarea
  pitch stays 28px (the rules are the point); inputs are ≥ 16px
  computed (Caveat 22px satisfies this) so iOS does not zoom.

**v2 — Choreography timeline** (t = submit activated, validation passed):

| Beat | Time | What happens |
|---|---|---|
| Fold | t + 0–300ms | Sheet's top third folds down (`--ease-unfold`) |
| Tuck | t + 300–700ms | Folded sheet slides into the envelope (`--ease-post`) |
| Post | t + 700–1000ms | Envelope rises into the form-head slot; a soft paper sound is *not* played (the theme is silent) |
| Reply | t + 1000ms (or on server response, whichever is later) | Confirmation note settles flat (§6.9 rest physics in reverse: it is laid, 240ms) |
| Error path | instead of Fold | Tea rule + margin note at t + 120ms; focus to the field at t + 150ms |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Blank ruled sheet | Same |
| Focus | Active rule inks to `--ink` | Same |
| Filled | Rule stays at 60% ink (a written line is darker than a blank one) | Same |
| Error | Tea-deep rule + italic margin note | Note moves *under* its field (no margin on a phone) |
| Submitting | Fold/slot sequence; fields inert | Same |
| Disabled | Submit is disabled only while a submission is in flight — styled as a sealed envelope (furniture), never greyed-out red | Same |

**v2 — Breakpoint behaviour.** ≥1200px: form in the letters column,
margin notes in the right margin. 768–1199px: margin notes under
fields. <768px: as mobile variant above; the envelope surround loses
its side flaps (top flap only) to give the sheet the full width.

**v2 — Edge cases & failure modes.** Very long letter (the textarea
grows by ruled lines — the sheet gets longer, the rules continue;
never a scrollable box within the paper: paper doesn't scroll, it
extends). Signature left blank: the aunt's note asks once ("Sign as
you feel, and your town — that is all the column ever prints"); if
still blank on second submit, the letter posts signed "— A Reader, of
—" and the confirmation says so (anonymity protects the reluctant
too). Server failure: the sheet unfolds back (reverse, 300ms) with
the note "The post has failed us, not you — your letter is still
here, try the slot again" and the text intact. Nothing the visitor
wrote is ever lost to an error state.

**v2 — Accessibility spec.** Real `<label>`s (furniture voice),
`aria-describedby` ties each field to its margin/under-field note;
errors use `role="alert"` once (the note), not per keystroke. The
signature furniture ("—", ", of") is `aria-hidden` decoration around
labelled inputs ("How you feel", "Your town"). Focus order: letter →
feeling → town → email → post. Contrast: Caveat input text `--ink` on
`--lined` ≈ 12.8:1; labels `--ink` small caps ≈ 12.4:1 on newsprint.
Touch targets: fields ≥ 44px tall via the rule pitch (28px line +
padding), submit ≥ 48px.

**v2 — Tokens consumed.** `--lined`, `--rule-line`, `--margin-line`,
`--ink`, `--tea-deep`, `--smooth`, `--envelope`, `--ease-unfold`,
`--ease-post`.

### 6.16 Tea-tray footer (page family: footer)

- **What & why.** The footer is the desk at the end of the morning: the
  full tea-ring cluster (the morning's whole record, echoing §6.5 at
  its final state), the column's colophon — set in what, answered from
  where, since when — the final tallies (agreeing with the header's,
  §6.11), and a printed line: "The postbag is empty. The kettle is
  off." It closes the sitting the way the header opened it.
- **Structure.** `footer` on `--newsprint` deepened one step (the desk
  in later light — a derived shade, `--newsprint` toward `--tea` at
  6%): ring cluster left (or the mobile strip, §6.5), colophon centre
  in furniture small caps, tallies right, legal line in `--ink-soft`.
- **Motion spec.** The footer is still. The ring cluster arrives at
  whatever state the reader earned (§6.5) — reaching the footer does
  not complete rings for unread letters; the record is honest to the
  last element. One exception: the final ring, if earned while the
  footer is in view, soaks in per §6.5.
- **States.** *Rest:* the day's end, static. No hover states except
  links (furniture underline draw, 200ms).
- **Content merge.** The colophon is content: the column's real
  credits, real tallies, real legal line.
- **Failure fallback.** Static block; with no JS the cluster shows the
  full morning (§6.5 fallback) and the tallies the totals (§6.11).
- **Reduced-motion variant.** Identical (it never moved).
- **Performance budget & mobile variant.** Nothing animates. <768px:
  cluster becomes the strip above the colophon; tallies inline.

**v2 — Choreography timeline.** None — the footer's stillness is its
spec. (If the last ring is earned in view: §6.5's 900ms soak.)

**v2 — State matrix.** Rest: static (both modalities). Hover: links
only. Focus: standard ring. Scrolled-past: it is the end. Disabled:
n/a.

**v2 — Breakpoint behaviour.** ≥1200px: three-column desk.
768–1199px: two columns (cluster + colophon; tallies under).
<768px: stacked, strip first.

**v2 — Edge cases & failure modes.** Morning unfinished (reader jumped
to the footer): cluster and tallies show the true partial record, and
the printed line changes to the honest variant — "Letters remain in
the bag." The footer never claims a finished morning that didn't
happen.

**v2 — Accessibility spec.** `<footer>` with the colophon as text;
cluster `aria-hidden` (its record is duplicated by the tallies' text).
Contrast `--ink-soft` on the deepened ground ≈ 5.4:1 — AA for the
small print sizes used (≥ 13.5px).

**v2 — Tokens consumed.** `--newsprint`, `--tea`, `--tea-deep`,
`--ink`, `--ink-soft`, `--ease-ink`.

### 6.17 The empty postbag (page family: empty states & 404)

- **What & why.** An empty department, a search with no letters, a 404
  — all are the same desk fact: the bag is empty. The empty state is an
  open, empty envelope on the desk with one line in the aunt's voice
  and a way back to the morning. A 404 in this theme is a misdirected
  letter: "This letter reached us, but it is not addressed to anyone
  here." It returns the visitor to the postbag (§6.13) rather than to
  a homepage they didn't ask for.
- **Structure.** Centred envelope (`--envelope`, flap open, interior
  `--envelope-deep` empty), the line in Cormorant italic 20px, one
  furniture link ("To this morning's post"). No illustration beyond
  the envelope; no Caveat (no reader wrote this).
- **Motion spec.** None on arrival. The envelope is open and still —
  an empty bag does not perform. (The §6.12(b) arrival slide still
  runs for the *page*, if the 404 is a routed page; the empty state
  itself is static within it.)
- **States.** *Rest:* open, empty, explained. That is all.
- **Content merge.** The state's message is real information (what was
  sought, that it isn't here, where the letters are) in the column's
  voice.
- **Failure fallback.** It is the fallback.
- **Reduced-motion variant.** Identical.
- **Performance budget & mobile variant.** Nothing. Mobile: envelope
  scales to 72% width.

**v2 — Choreography timeline.** None by design.

**v2 — State matrix.** Rest only, both modalities. The return link
takes standard hover/focus.

**v2 — Breakpoint behaviour.** Identical at all sizes except envelope
scale (<768px: 72%).

**v2 — Edge cases & failure modes.** Search empty state adds the
sought phrase in the aunt's line ("Nothing in the bag about
'landlords' — try 'neighbours', or write in") only when a suggestion
genuinely exists; otherwise the plain line. Never a list of "popular
letters" dumped under an empty result (§9.6).

**v2 — Accessibility spec.** The heading states the fact ("An empty
postbag"), the line explains, the link is labelled with its
destination. `role="status"` is NOT used (a page load is not an
announcement).

**v2 — Tokens consumed.** `--envelope`, `--envelope-deep`, `--ink`,
`--ink-soft`.

### 6.18 Postbag index & topic shelves (page family: search & index)

- **What & why.** Finding a past letter works the way finding a letter
  in a column office works: by the shelves the aunt keeps — topics in
  her words ("Neighbours", "Money lent to family", "The night shift")
  and a simple search across salutations, signatures, and topics. The
  index is a printed list on smooth stock; results are §6.14 cards.
  There is no filter chrome, no facet rail: a column office has
  shelves, not a control panel.
- **Structure.** `section.index`: topic list (furniture small caps,
  two columns at ≥768px, each with its real letter count in tabular
  Cormorant), then a search field styled as a ruled line on lined
  stock ("Look in the postbag…") whose results replace the topic list
  region with §6.14 cards.
- **Motion spec.** Topic counts never animate. Search results deal in
  per §6.14's stagger. Clearing the search restores the shelves with a
  200ms fade of the region (the only fade in the theme — a list being
  re-filed).
- **States.** *Shelves:* the resting index. *Searching:* results
  region `aria-busy`. *No results:* §6.17 with the sought phrase.
  *Hover/focus:* topic rows take the §6.9 half-lift's static variant
  (edge deepening) — rows are paper slips, not buttons.
- **Content merge.** Topics and counts are the archive's real
  contents; search searches the letters' real text.
- **Failure fallback.** The topic shelves are server-rendered links —
  the index fully works without JS; search degrades to a GET form
  returning a results page of the same cards.
- **Reduced-motion variant.** No stagger, no fade; results replace.
- **Performance budget & mobile variant.** List rendering only.
  <768px: topics one column; search line full width.

**v2 — Choreography timeline.** Search submit → region busy → cards
deal (380ms, 70ms stagger, §6.14) → busy released. Clear → 200ms fade
→ shelves.

**v2 — State matrix.** Rest: shelves. Hover: slip edge (desktop).
Focus: ring on the topic link / search field rule inks (§6.15 focus
law). Active: navigation or search run. Scrolled-past: static.
Disabled: a topic with zero letters is omitted from the shelves
entirely — an empty shelf is not listed (§6.17 covers arriving there
by URL).

**v2 — Breakpoint behaviour.** ≥1200px: topics in two columns beside
the search line. 768–1199px: topics two columns below the search.
<768px: one column.

**v2 — Edge cases & failure modes.** Search matches a letter's
*answer* only: the card still shows the question's opening (cards are
envelopes, §6.14) with the matched topic in its footer — the match is
honest about where it was found ("Answered under Money lent to
family"). Very large archives (500+ letters): shelves paginate by
morning (§7), never infinite scroll — paper is paginated by the
postbag, and the theme's refusal is stated so a builder doesn't
"modernise" it.

**v2 — Accessibility spec.** Search is a labelled form
(`role="search"`), results region announces count via a visually
hidden status ("6 letters in the bag") — the one sanctioned live
announcement in the theme, because search results are otherwise
invisible to AT. Topic counts are text, not badges.

**v2 — Tokens consumed.** `--smooth`, `--lined`, `--ink`, `--ink-soft`,
`--ease-post`.

---

## 7. Page application map

- **Home — This Morning.** The full sitting: nameplate + tallies
  (§6.11), postbag (§6.13), hero letter from the slot (§6.1), 4–7
  letters (§6.2–6.10 in sequence), aunt pinned for the middle act
  (§6.6), the kiss on exactly one letter (§6.7), tea rings in the
  margin (§6.5), write-in form (§6.15) after the last letter, tea-tray
  footer (§6.16). The peek (§6.3) runs throughout.
- **Listing — Past Mornings.** One page per morning: a furniture head
  ("The post of Tuesday the 12th"), that morning's letters as §6.14
  cards (the morning is over; its letters are filed, not re-opened),
  pagination as printed page furniture ("Earlier mornings →"). A
  morning's own page never re-runs the home sitting.
- **Detail — a single letter.** The letter in full (question, answer,
  signature, its kiss if it carries the page's one — on a detail page
  the letter *is* the page, so its kiss may live here instead of a
  listing), its topic shelf link, and the two neighbouring letters as
  cards ("From the same morning"). No peek (there is no "next" in a
  single letter; the neighbours are the way on).
- **About — the Aunt.** Her portrait large (taped, §6.12), her standing
  advice in full, how the column works (the anonymity law, §1, stated
  to readers plainly), the postmark facts (town, since when). This is
  the one page where Cormorant display type may headline — she is the
  subject.
- **Write In — the form page.** §6.15 at full width of the letters
  column, preceded by three furniture lines of guidance (what makes a
  letter answerable: one problem, the facts in order, sign as you
  feel). The guidance is counsel, not instructions.
- **Topics — the shelves.** §6.18 with §6.14 results.
- **404 — the misdirected letter.** §6.17.

## 8. Worked examples

### 8.1 The hero — a coaching column's first letter

*Site: "Dear Margaret" — a relationships column run by a counsellor.*
Load: the nameplate sits under the slot bar; tallies read "Letters
answered 0 · Cups of tea 1"; the postbag shows *This Morning* open.
Fonts ready at ~210ms → the hero letter slides from the slot (600ms,
§6.1): "Dear Margaret, I am writing because my sister has not spoken
to me since our father's funeral…" in Caveat on lined stock, fold
shadow sweeping ahead. It settles at −0.4°. The signature — "—
Estranged, of York" — signs at +580ms (§6.4). The answer's slit opens
(§6.8); the counsel flows line by line (§6.2): "Dear Estranged, A
funeral is a poor place to mend anything…" — 7 lines, stagger
compressed to 114ms, dry at ≈ 1240ms from the letter's open, inside
the law. The peek at the foot already shows the next salutation at
18%. Scroll timeline: as the reader moves through the hero, the peek
emerges to 46%; the question stock drifts 8px slower than the answer
stock over the letter's length; at the answer's end, ring 1 soaks into
the margin (900ms) and the tally amends to 1.

### 8.2 Mid-page — the pinned act and the kiss

Letter 4 of 7, the morning's hardest: "— Sleepless, of Leeds" on
night-shift marriages. The aunt has been pinned since letter 3 (§6.6)
— portrait and standing advice ("Say the true thing kindly, or wait
until you can.") steady in the margin. This letter carries the page's
`data-kiss`. Sequence on open: question settles; signature signs;
then, 120ms later, the kiss draws beside the signature over 920ms
(§6.7) — the reader who wrote at 3 a.m. kissed the page before
posting, and the column says nothing about it. The answer flows; its
key sentence — "You cannot mend a marriage in the hours you are both
asleep." — is the one the visitor clicks; the lipstick stroke draws
under it in 300ms (§6.10). Ring 4 lands at completion; cups stays 2
(derivation: 1 + ⌊4/3⌋). At letter 5's end she releases with the
300ms lay-down, and letters 6–7 are read alone with her — which is
the point of the act structure.

### 8.3 Conversion — writing in about a landlord

After letter 7, the write-in sheet (§6.15). The visitor types in
Caveat on the rules: a long letter about a deposit (the sheet extends
by ruled lines as they write — paper extending, not a scrolling box).
They sign "— Nervous" and "Leicester" in the furniture'd signature
pair, add an email. First submit: the email field is malformed → no
fold; the email rule turns tea-deep and the margin (below the field
at this width) notes, in her italic: "The column needs a way to write
back — may we have the email again?" Focus moves to the field. They
correct it; second submit: fold (300ms), tuck (400ms), post (300ms);
the confirmation settles: "Thank you. Your letter is in the bag for
tomorrow's post." — no reference number, because this deployment has
no numbering system and the theme does not invent one (§6.15). The
peek letter is absent on this page (§6.15 states why).

## 9. Anti-slop — what makes THIS theme look cheap

1. **Fabricated-feeling letters.** Letters written by a copywriter in
   "quirky" voice — too witty, too neat, arcs too tidy. *Cure:* letters
   are edited real correspondence or written to §12's reader voice
   (one problem, facts out of order, a detail too many); a letter that
   reads as an ad fails review.
2. **Full names and headshots.** "Sarah M., 34, loved the advice!" —
   testimonial furniture on a letter. *Cure:* the §1 law; gate-checked
   (§10 blocking).
3. **Caveat everywhere.** Handwriting on buttons, nav, prices — the
   fiction tears and legibility dies. *Cure:* §3.2; Caveat is readers
   and readers only.
4. **Kiss inflation.** A kiss per letter, a kiss logo, a kiss favicon.
   *Cure:* §6.7's at-most-one rule, gate-checked by counting
   `data-kiss` in the page source.
5. **Red creep.** Lipstick buttons, red links, red errors. *Cure:* the
   three licensed jobs (§2); errors are tea and italics (§6.15);
   measured red coverage ≤ 1.5% of a full-page screenshot.
6. **Desk clutter.** Related-links rails, ad slots, newsletter boxes
   in the margin. *Cure:* the margin holds rings and the aunt, only
   (§4); a newsletter ask lives on its own page or not at all.
7. **Everything pre-marked.** Answers shipped with every sentence
   underlined, tallies pre-counted, rings pre-darkened in the static
   build (outside the no-JS fallback, where the printed state is
   honest). *Cure:* marks are earned by events (§6.5, §6.10, §6.11);
   the JS build starts the morning at 0.
8. **Shimmering skeletons and fake handwriting loaders.** A skeleton
   with wobbling Caveat-shaped squiggles pretends a letter exists
   before it arrives. *Cure:* §6.12's blank lined envelopes — unwritten
   paper, no imitation writing.
9. **Typewriter answers.** Letter-by-letter counsel with a caret.
   *Cure:* §6.2's line-flow; kinetic type is refused (§5).
10. **The aunt as influencer.** Portrait retouched to glamour,
    exclamation marks, "Hey lovelies". *Cure:* §12's aunt voice and a
    portrait that looks like a person at a desk; if she could sell
    skincare, reshoot.

## 10. Quality gate

**Blocking — all must pass.**
1. **Anonymity audit:** every signature on the page matches "—
   [Feeling], of [Town]"; no full names, reader photos, handles, or
   ratings anywhere in letters or cards.
2. **Kiss count:** `data-kiss` occurs at most once in the page source.
3. **Red audit:** lipstick appears only as underline strokes, the kiss,
   and the postmark; screenshot red coverage ≤ 1.5%.
4. **Truth audit:** tallies derive from the DOM per §6.11's law; rings
   count = letters count; no invented dates, numbers, or reference
   codes anywhere.
5. **JS-off test:** the whole morning reads, in order, fully written,
   with tallies at totals and marks in their printed states (§6.10,
   §6.11 fallbacks).
6. **Write-out law:** with triggers sabotaged, every answer is fully
   inked within 1200ms of its trigger point.
7. **Peek clearance:** at 5 scroll depths, the peek never overlaps a
   text line (§4 padding law measured, not eyeballed).
8. **Two-hands audit:** Caveat appears only in reader content and the
   form's input text; Cormorant carries everything the aunt owns.

**Standard — at least 9 of 11.**
9. One shared rAF loop (lerp 0.12) drives peek, parallax, pin
   observation; no scroll handlers write styles directly.
10. Ink-flow stagger compression keeps the longest answer ≤ 1200ms.
11. Stock differential never separates the question/answer overlap by
    more than 2px at any scroll position.
12. Signatures are real text; flourishes re-measure on font load.
13. Reduced-motion build: flat letters, no peek, aunt unpinned above
    letter 3, form posts with the fade — same information throughout.
14. Lamplight: the three stocks still read as three papers (§2 test).
15. Form: no letter text is lost on any error path (§6.15 test —
    submit with a server 500 and read the letter back).
16. Print stylesheet: letters print flat, fully written, peek and
    rustle gone — the column as it would appear in the paper.
17. The five-second test: a first-time viewer says "letters to an
    agony aunt" — not "a cute blog theme", not "vintage stationery".

## 11. Component inventory

Every component a real site in this theme needs, with its treatment.
Anything not listed does not get invented in this theme's furniture.

| Component | Themed treatment |
|---|---|
| Primary button | A postmark-edged slip in furniture small caps ("Post my letter", "To this morning's post") on `--smooth` with an ink hairline; press = §6.10's wash deepen; never lipstick-filled |
| Secondary button | Plain furniture text with the underline draw (200ms, ink) — a printed direction, not a box |
| Text input | A ruled line on `--lined` (§6.15); Caveat 22px input text; focus inks the rule |
| Textarea | The letter sheet itself (§6.15): ruled pitch, extends by lines |
| Select | Refused. A column office has no dropdowns; choices are printed lists of furniture links (topics, departments) |
| Checkbox / radio | A small square in ink hairline; the mark is a pencilled tick drawn in `--ink` (200ms) — the aunt's pencil, not a UI check |
| Toggle | Refused. Settings in this world are stated in sentences with furniture links ("The column arrives weekly — change to monthly") |
| Table | Correspondence ledgers only (archive by morning): furniture heads, ink hairlines, tabular Cormorant figures; no striping — paper doesn't stripe |
| Badge | The postmark (§6.13) is the only badge-like object; counts live in text ("6 letters"), never in pill badges |
| Alert | A margin note in the aunt's italic (§6.15 error voice) with a tea-deep rule; never a banner, never red |
| Pagination | Printed furniture: "Earlier mornings →" / "← Later mornings" at the rack's foot (§7) |
| Modal | Refused on letter pages. The one permitted overlay is the photo at full size (taped frame enlarged, §6.12) — paper on the desk, dismissed by laying it back down |
| Toast | Refused. News in this theme is a note on the desk (confirmation, §6.15), not a popup |
| Tabs | The postbag (§6.13) is the tab system — envelopes, not tabs |
| Accordion | Archive mornings expand as envelopes opening (§6.14 cards deal out under their morning's head); one open at a time, like letters |
| Search | §6.18 — a ruled line and shelves |
| Progress | §6.5 rings (reading) and §6.11 tallies (accounts); no bars anywhere |
| Tooltip | Refused. Anything worth saying is said in the margin, in her voice |
| Breadcrumbs | A single furniture line: "Past Mornings · Tuesday the 12th" — the filing path, printed |
| Card | §6.14 envelope cards |
| Divider | Bare desk (§4) or a single ink hairline; never an ornament row |
| Skeleton | §6.12 blank lined envelopes |
| Avatar | Only the aunt has a face (§6.6). Readers are signatures, never avatars |

## 12. Content & copywriting voice

Two voices, cast like the type (§3): **the reader** and **the aunt**.

**The reader's voice** (Caveat; letters, signatures, form input).
- Headline/opening style: the problem, plainly, in the first line —
  "Dear Aunt, my husband reads my diary." No throat-clearing, no
  compliments to the column.
- Facts arrive slightly out of order; one unnecessary detail is
  allowed (it is the truest thing in the letter). Length 60–140 words.
- Signatures: "— [Feeling], of [Town]" — feelings are specific
  ("Ashamed", "At my wits' end"), towns are real-scale places.
  *✓ "— Ashamed, of Truro"* · *✗ "— Sarah M."* · *✗ "— Devastated
  Diva xx"*

**The aunt's voice** (Cormorant; answers, furniture, errors, empty
states).
- Answers open by naming the reader as signed: "Dear Ashamed," — then
  one sentence of pure acknowledgment before any counsel. Counsel is
  concrete, sequenced, and finite: she gives the reader two or three
  things, not a framework.
- No exclamation marks. No "just". No therapy jargon ("boundaries" is
  permitted once per morning; "self-care" never). Emphasis by italic,
  once per answer at most.
- Labels (furniture): noun phrases from the office — "This morning's
  post", "Past mornings", "Write to the column". *✗ "Latest drops",
  "Join the community".*
- Error voice: counsel, addressed kindly, owning the system's part —
  *✓ "The column needs a way to write back — may we have the email
  again?"* · *✗ "Invalid email address!"*
- Empty-state voice: *✓ "The postbag is empty. The kettle is off."* ·
  *✗ "Nothing here yet — check back soon!"*
- Confirmation voice: *✓ "Thank you. Your letter is in the bag for
  tomorrow's post."* · *✗ "Submission received! 🎉"*
- Dates are real or omitted: "Answered on Tuesday the 12th" only when
  true; otherwise the postmark month alone.

**Banned words (aunt's voice):** journey, hack, tribe, lovelies,
amazing, just (as a minimiser), !!!, emoji of any kind. **Owned
words:** post, bag, morning, desk, kettle, in the bag, write back.

## 13. Full-page scroll choreography map

Home page, top to footer. (Letters 1–7; the aunt's act is letters 3–5.)

| # | Beat | What the visitor sees and feels |
|---|---|---|
| 1 | Load | Slot, nameplate, tallies at 0/1, postbag settles open |
| 2 | Hero arrival | Letter 1 slides from the slot; fold shadow; settle (§6.1) |
| 3 | First counsel | Signature signs; slit opens; answer flows and dries (§6.4, §6.8, §6.2) |
| 4 | The promise | Peek shows letter 2 at 18%, emerging as letter 1 is read (§6.3) |
| 5 | First ring | Letter 1 completes: ring 1 soaks in; tally amends to 1 (§6.5, §6.11) |
| 6 | Letter 2 | Opens as letter 1 did, minus the slot (it was the peek); its photo (a taped snapshot) scales in-frame (§6.12) |
| 7 | She arrives | Letter 3 approaches; the aunt's portrait has scaled in; at letter 3 she pins (§6.6) |
| 8 | The act | Letters 3–5 pass with her beside them; rings 3–5 land under her gaze; cups reaches 2 at letter 3, 3 at letter 6's completion — the tally is ahead of the act, honestly derived |
| 9 | The kiss | On letter 4, after its signature: the draw, 920ms, unexplained (§6.7) |
| 10 | A mark made | The visitor clicks letter 4's key sentence; the red stroke draws (§6.10) |
| 11 | Release | Letter 5 dries; she lays down and scrolls away (§6.6) |
| 12 | Alone again | Letters 6–7 read without her; the margin holds only rings — the morning is nearly done and feels it |
| 13 | Your turn | The write-in sheet (§6.15); the peek is gone — the next letter is the visitor's |
| 14 | Day's end | Footer: full ring cluster, final tallies agreeing with the header, "The postbag is empty. The kettle is off." (§6.16) |

Reverse pass: scrolling back up, the peek retreats (positional), the
aunt re-pins (sticky), but rings, signatures, the kiss, and any marks
stay made — the morning, once read, stays read.

## 14. Whole-page performance budget

- **Assets:** ≤ 420KB initial (fonts dominate: Caveat + Cormorant
  subsets ≈ 120KB woff2; the portrait is the only hero image, ≤ 90KB;
  taped photos ≤ 60KB each, ≤ 3 per page). No framework JS: the
  theme's whole runtime (loop, queue, flows, counters) ≤ 14KB gz.
- **Frame budget:** the shared loop does ≤ 3 style writes per frame
  (peek transform, two stock transforms); ink flows and draws are CSS
  transitions/animations, not JS per-frame work. No frame over 20ms
  attributable to theme code during a full scroll on a mid-range
  Android.
- **Long tasks:** none over 50ms; line measurement (§6.2) happens once
  per answer at arm time, never during scroll.
- **CLS:** hero height reserved in CSS (§6.1); letters are in-flow;
  target CLS ≤ 0.02. LCP is the hero letter's first line — it must not
  wait for the slide; the slide is transform-only over laid-out text.
- **Cut order when the budget is exceeded:** (1) paper-grain breathing,
  (2) peek rustle, (3) stock parallax differential, (4) photo scale-in
  (photos arrive still), (5) ink-flow becomes instant print. **Never
  cut:** the write-out law, the anonymity furniture, the form's error
  behaviour, any content.

## 15. Build-order checklist

1. Static desk first: nameplate, postbag, all letters fully written,
   tallies at totals, footer — the JS-off page (§10.5) passes before
   any motion exists.
2. Stocks and layout: lined/smooth papers, rotations, overlap, margin
   geography, peek clearance padding (§4).
3. Type: the two-hands casting, rule-pitch line-height lock for
   Caveat, signature format lint (a build-time regex for "— …, of …"
   catches §1 violations early).
4. Header tallies + ring cluster as pure records (events defined:
   letter-completed; derivation law unit-checked, §6.11).
5. The shared rAF loop (peek scrub, parallax, pin observation).
6. Hero slot arrival (§6.1) with fonts gate and fallback timer.
7. Per-letter sequence queue: settle → signature (§6.4) → slit
   (§6.8) → ink-flow (§6.2) → completion event; write-out law wired to
   every step.
8. The kiss (§6.7) — placed once, counted in CI.
9. Pinned aunt (§6.6) + taped photos (§6.12a).
10. Underline marks (§6.10) with no-JS pre-marked rendering.
11. Peek letter (§6.3) — built last among scroll elements; clearance
    re-measured after it exists.
12. Cards, index, empty states (§6.14, §6.18, §6.17).
13. The form (§6.15): native-first, error paths tested before the
    fold ceremony is added; then the ceremony.
14. Transitions (§6.12b) and skeletons.
15. Reduced-motion build and lamplight mapping; print stylesheet.
16. The §10 gate, in order, with screenshots for items 3 and 7.

---
