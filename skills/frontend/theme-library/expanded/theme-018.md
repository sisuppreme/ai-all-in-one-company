# 18. Manicule & Catchword — Expanded (v1 + v2)

The site is a Renaissance manuscript that is still being read the way its
scribe intended: not by scrolling a feed, but by following a hand. In the
left margin a drawn manicule — the little pointing hand medieval readers
inked beside passages that mattered — travels down the page level with the
paragraph being read, swivelling when the reader's own attention wanders.
Chapters turn as leaves turn, bending in proportion to the reader's scroll.
Every page foot carries a catchword: the first word of the next gathering,
copied there by the binder so the quires could be assembled in order. This
document is the complete build specification. Where it disagrees with the
short library entry, this document is the build target.

---

## 1. Concept & world

**The story.** Before the bookmark, before the highlighter, there was the
manicule. From the twelfth century onward, readers drew small hands in the
margins of manuscripts — index finger extended, cuff at the wrist — to mark
the sentence they would need again. Scribes adopted the device into the
apparatus of the book itself: manicules for finding, catchwords for
ordering, rubricated initials for beginning, prickings — the pin-holes down
the margin — for ruling the lines before a word was written. Manicule &
Catchword rebuilds that apparatus as a navigation system. The page is a
quire of vellum. The margin is wide because margins were where reading
*happened*. The gold in the initials is real gold leaf in the fiction and
behaves like it: it does not glow, it catches light when the leaf moves.
The fiction is load-bearing. Remove the manicule and the visitor has lost
their guide, not a decoration; remove the catchword and the page foot has
lost its promise of what comes next.

**The mood.** Candle-steady, unhurried, faintly playful. The scribe is
competent and a little mischievous: once in a while his hand points not at
the text but at his own marginal doodle — a snail, a flower — with a caption
in his own voice (§9, rule 1, governs how rarely). Nothing on the page
hurries. The fastest motion in the theme is a stamp landing; the slowest is
gold deciding to glint. A visitor should feel *accompanied* — read with,
not scrolled past.

**Best-fit sites and audiences.**
- Book publishers and literary imprints: a forthcoming-title site where each
  chapter excerpt is a leaf, the manicule guides the reading, and the
  catchword at each foot is the next chapter's real first word.
- Calligraphers, illuminators, bookbinders and heritage craftspeople selling
  commissions: the portfolio is a quire, each miniature a plate, the order
  form a commissioning slip (§6.16).
- Fantasy and historical-fiction authors: world bibles, chapter previews,
  bestiaries — anywhere the book-object is part of the fiction.
- Fantasy games with lore codices: patch-note chronicles, bestiary entries,
  quest journals presented as gatherings of a codex.
- Museums, libraries and manuscript collections: exhibition microsites
  where the digital leaf teaches visitors how a real leaf was read.
- Wedding and event stationers working in a heritage register: the
  invitation suite presented as an illuminated opening.

**When NOT to use it.**
- For anything that must be scanned fast. The theme's reading speed is a
  manuscript's reading speed; dashboards, documentation, pricing tables and
  support content fight it at every line. Data-dense product UI in vellum
  and Fell type is a costume, and §9 names it as such.
- For brands whose voice is clinical, minimal or futuristic. The scribe's
  hand cannot be made neutral; if the client flinches at a snail in the
  margin, they want a different theme.
- Where the content has no chapter structure. The apparatus — catchwords,
  quire counts, chapter initials — numbers and orders *gatherings*. A
  one-screen landing page has nothing for the apparatus to count, and the
  devices curdle into ornament.
- For text the publisher cannot supply in full. Catchwords must be the next
  section's *actual* first word and miniatures must illustrate the chapter
  they open; stock imagery in arched frames fails the truth rule (§10,
  blocking item 4).

**The one law.** Every device on the page must do the job it did in the
manuscript. The manicule finds, the catchword continues, the initial
begins, the prickings rule, the folio counts. A device that has stopped
doing its job — a catchword that is not the next word, a manicule pointing
at nothing — is removed, not restyled.

---

## 2. Palette

Four pigments, all mineral or organic in the fiction: vellum (the ground),
rubric red (the scribe's second ink, for beginnings and marks), lapis (the
expensive blue, rationed like the pigment was), and gold (leaf, never
paint, never text). Iron-gall ink is a derived token — the original entry
implies it; the scribe's writing colour is specified here so two builders
produce the same page.

| Token | Hex | Role | Usage ratio | Pairing & contrast |
|---|---|---|---|---|
| `--vellum` | `#EADFC0` | Page ground; the leaf itself | ~78% of any viewport | Ground for all text tokens |
| `--vellum-deep` | `#D9C69A` | Unwritten margin bands, quire edges, skeleton leaves, the leaf beneath a curl | ~10% | Under `--ink` 8.72:1; under `--lapis` 5.95:1 |
| `--ink` | `#33261A` | Iron-gall body ink; all reading text | ~7% | On `--vellum` 11.04:1 (AAA) |
| `--ink-soft` | `#5C4A33` | Captions, catchwords at rest, apparatus small print | ~2% | On `--vellum` ≈5.9:1 — captions and apparatus only, never body |
| `--rubric` | `#9C2B1B` | Rubricated headings, pilcrows, the manicule's cuff band, marks of correction | ~2% | On `--vellum` 5.70:1 — headings and apparatus; body-size rubric only ≥16px bold-equivalent |
| `--lapis` | `#27436B` | Links, the vine, miniature skies, interactive emphasis | ~1.5% | On `--vellum` 7.53:1 (AA at all sizes); `--vellum` on `--lapis` 7.53:1 for filled controls |
| `--gold` | `#B98A2F` | Gold leaf in initials, flecks, finial rules | <0.5% | On `--vellum` 2.35:1 — **decorative only, never text, never an essential indicator** |
| `--gold-pale` | `#D9B96A` | The glint's highlight pass (§6.7) | fleeting | Never a resting colour; exists only mid-glint |

**Pairing laws.**
1. Gold never carries information. Anything the visitor must read, count or
   act on is set in `--ink`, `--rubric` or `--lapis`. The glint (§6.7) may
   cross a word but may never *be* the word's only emphasis.
2. Lapis is rationed to one interactive family per view: links *or* the
   vine *or* a filled control — never all three competing. The pigment was
   worth more than gold; the page spends it like it remembers that.
3. Rubric marks beginnings and corrections only: chapter headings, the
   pilcrow stamp, the cuff band. A rubric price, button or error is a
   category error — errors are lapis (§12), prices are ink.
4. `--vellum-deep` is the colour of *unwritten* page: margins before the
   vine grows, the underside of a curling leaf, skeleton leaves. Content
   never sits on it at body size except the catchword, which is set in
   `--ink-soft` at apparatus size by design (§6.5).

**Dark mode — the candlelit reading.** Dark mode is not an inversion; it
is the same manuscript read at night. The vellum darkens to a deep umber
ground and the inks lighten to their candlelit values; gold, being leaf,
gains contrast at night instead of losing it.

| Token | Night value | Contrast on `--vellum-night` `#241B12` |
|---|---|---|
| `--vellum-night` | `#241B12` | — (ground) |
| `--vellum-night-deep` | `#171009` | unwritten bands, curl underside |
| `--ink-night` | `#E8DCC2` | 12.45:1 (AAA) |
| `--rubric-night` | `#C4503A` | 3.67:1 — **display sizes only (≥24px)**; small rubric apparatus at night is set in `--ink-night` with a rubric pilcrow, never in rubric alone |
| `--lapis-night` | `#7E9CC4` | 6.00:1 (AA) |
| `--gold-night` | `#D9A94E` | 7.85:1 — still decorative by law 1; the number is recorded so nobody "fixes" the law with it |

The glint (§6.7) warms at night: its sweep gradient picks up a candle
flicker amplitude of ±4% brightness at 0.11Hz, the only place in the theme
where light itself is allowed to move. Everything else about the night
manuscript is the day manuscript, dimmed by rule, not by filter: no
`invert()`, no global opacity tricks.

---

## 3. Typography

Two faces, both period-true and both on Google Fonts: **IM Fell English**
for display — the Fell types, cut in the 1670s from Dutch originals, carry
the slight irregularity of hand-set type — and **EB Garamond** for body,
whose old-style figures and long s-adjacent calm suit a reading column.
IM Fell English SC is used for exactly one thing: the catchword and quire
signatures, where small caps are the manuscript's own convention.

| Role | Face | Size / line-height | Tracking | Rules |
|---|---|---|---|---|
| Display (hero headline) | IM Fell English | 56px / 1.04 (≥1200px); 44px (768–1199); 34px (<768) | −0.01em | Never below 34px at any width; the historiated initial (§6.1) is part of this line, not an image before it |
| Chapter heading | IM Fell English | 34px / 1.12 | 0 | Rubricated (`--rubric`); opens with its chapter initial (§6.6) or a 34px Fell initial in ink |
| Section heading | IM Fell English | 24px / 1.2 | 0 | Ink; rubric only when the section *begins* something (a gathering, a part) |
| Body | EB Garamond | 19px / 1.62 | 0.002em | Measure 58–66ch; first paragraph of a chapter takes the initial, following paragraphs are indented 1.5em with no blank line — the manuscript's paragraphing, not the web's |
| Lead paragraph | EB Garamond | 21px / 1.58 | 0.002em | First paragraph after a chapter heading only |
| Caption (miniatures) | EB Garamond italic | 16px / 1.45 | 0.004em | `--ink-soft`; names what the miniature shows and which leaf it illustrates |
| Catchword | IM Fell English SC | 17px | 0.06em | Right-aligned at the page foot, preceded by the quire signature (§6.5) |
| Apparatus (folios, quire counts) | EB Garamond, tabular old-style | 15px | 0.08em, uppercase | Roman numerals only (§6.8); Arabic numerals on a folio are a §10 failure |
| Data (prices, dates, editions) | EB Garamond | 17px / 1.5 | 0.01em | Ink; dates written out ("the xii. day of October") in display contexts, ISO in forms and metadata |
| Hand (scribe's asides) | — | — | — | **There is no handwriting font in this theme.** The scribe's doodle captions (§9) are set in EB Garamond italic. A script face would impersonate a hand the theme never claims to have; the manicule is drawn, not typed |

**Type laws.**
1. The initial is type, not image. Historiated initials are inline SVG
   built around a live Fell glyph (§6.1), so the headline reads correctly
   to a screen reader, a search engine, and a visitor with images off.
2. Rubrication is structural: a heading is red because it begins, not
   because it is important. Marketing emphasis inside body copy is the
   manicule's job (§6.2), never a red word.
3. Old-style figures everywhere in prose; lining figures only inside the
   commissioning form's quantity and price fields (§6.16), where a sum
   must be checked at a glance.
4. No letterspaced lowercase. Tracking is applied to uppercase and small
   caps only; spaced lowercase Garamond reads as a typesetting error in
   this register.

---

## 4. Layout language

**The quire grid.** The page is a leaf, and a leaf has fixed proportions
of margin to text block that five centuries settled: the text block sits
high and toward the spine, the outer and lower margins are the generous
ones. At ≥1200px the layout is a 12-column grid of which the reading
column takes columns 4–9 (measure 58–66ch), the **manicule margin** takes
columns 2–3 (a 148px band holding the travelling hand, the pinned chapter
initial, and the vine), and columns 10–11 form the outer margin where
miniatures, captions and the scribe's asides live. Column 1 and 12 are the
leaf's edge — prickings (§4, below) and nothing else. The asymmetry is the
point: a centred, symmetric layout is a screen habit, not a book habit,
and §9 lists symmetry as a slop tell.

**Prickings.** Down both leaf edges runs a column of prick-holes: 3px
dots in `--vellum-deep` shadowed to read as punctures, spaced at the
body line-height (30.8px) so the ruling system is visible in the margin.
They are the slowest parallax layer (§5) and the skeleton leaf's only
decoration (§6.12). Prickings never appear inside the text block.

**Spacing rhythm.** All vertical spacing is a multiple of the body
line-height unit, `--leading: 30.8px` (19px × 1.62). Sections begin on a
fresh gathering: a chapter turn (§6.4) plus `6 × --leading` of unwritten
vellum before the rubricated heading — the manuscript's blank space is
structural, not leftover. Within a chapter, paragraphs flow with the
1.5em indent rule (§3); a miniature breaks the column only at a paragraph
boundary, never mid-paragraph.

**Density rules.** One miniature per chapter, one doodle per quire
(§9 rule 1), one pinned initial per chapter. The margin apparatus — hand,
vine, pinned initial, catchword — is four devices maximum in any viewport;
if a fifth device wants in, it waits for a later chapter. Whitespace is
the theme's luxury material: a page that feels crowded has failed even if
every element is individually correct.

**The leaf edge.** The page ground is `--vellum` edge to edge; there is
no card chrome, no drop shadow announcing a "container". At the very foot
of each page (and only there), a hairline in `--gold` at 40% opacity —
the binder's gilt edge — closes the leaf. Elevation in this theme is
expressed by curl and overlap (§6.4), never by shadow stacks.

**Tokens.** `--leading: 30.8px`, `--col-measure: 62ch`,
`--margin-band: 148px`, `--gutter-quire: 24px`, `--leaf-edge: 1px`.

---

## 5. Full motion system

Every motion in the theme is one of the scribe's or binder's physical
acts: a hand travelling, a leaf bending, a word being copied at a page
foot, gold catching light. There are no fades-for-fades'-sake; even the
crossfades that exist (catchword, folios) imitate a reader glancing down
and the eye re-settling. Named easings, defined once and consumed by
every element:

| Token | Curve | Used by |
|---|---|---|
| `--ease-quill` | `cubic-bezier(0.25, 0.9, 0.3, 1)` | Scribal strokes: headline write-on, vine and cuff draw, underline-free marks |
| `--ease-leaf` | `cubic-bezier(0.6, 0.05, 0.3, 0.95)` | Page curls and leaf lifts — slow to commit, fast through the bend, settling |
| `--ease-swivel` | `cubic-bezier(0.34, 1.4, 0.4, 1)` | The manicule's swivel — a slight overshoot, like a wrist turning |
| `--ease-stamp` | `cubic-bezier(0.2, 1.6, 0.35, 0.9)` then hard stop | The pilcrow stamp (§6.10) — overshoot is in the *press*, the landing is absolute |
| `--ease-flare` | `cubic-bezier(0.16, 0.8, 0.3, 1)` | Rubric flares and the glint's specular sweep |
| `--ease-drift` | `linear` | Ambient loops only: glint offsets, vellum grain breath |

**The motion terms, in this theme's language.**

- **Scroll-triggered reveals** — rubricated headings *flare*: the red
  deepens from 70% to full `--rubric` saturation over 500ms
  `--ease-flare` as the heading crosses 78% of the viewport height, in
  quire order (a heading never flares before the chapter it belongs to
  has begun). Miniatures open through their arches (§6.11).
- **Scroll-scrubbed motion** — two devices only, both scrubbed to the
  shared lerp loop (§5, engine): the manicule's travel (§6.2) and the
  chapter page-curls (§6.4). Scrubbing is reserved for things a reader's
  hand physically controls; everything else in the theme is triggered,
  not scrubbed.
- **Parallax** — three layers, all in the margins, never under text:
  prickings and catchwords at 0.92× scroll speed (slowest), rubricated
  apparatus at 1.0×, gold initials at 1.06× — gold *catches up*, arriving
  a breath after the text it opens. Maximum differential 14px over a
  chapter; the layers re-converge at every chapter boundary so drift
  never accumulates.
- **Pinned scenes** — one pin per chapter maximum: the chapter's
  historiated initial pinned in the margin (§6.6). The page-curl is
  *not* a pin; it is a boundary the reader scrubs through.
- **Masked / clip reveals** — miniatures reveal through arched clip-paths
  opening upward (§6.11); the historiated initial's scene paints inside
  the letter's own mask (§6.1). No rectangular wipes anywhere.
- **Blur-to-sharp** — refused as a reveal. Vellum has no blur state; the
  nearest honest equivalent is the skeleton leaf rubricating in (§6.12).
  One exception: the curling leaf's underside carries a 1px softness at
  the bend only, as a lighting effect, never on text.
- **Animated counters** — the roman-numeral apparatus (§6.8): folios and
  quire counts crossfade-tick (200ms) as sections pass. No Arabic
  odometers; a manuscript counts in gatherings.
- **Progress indicators** — progress is a *position*, not a bar: the
  manicule's place in the margin (§6.2) plus the catchword naming what
  comes next (§6.5). There is no progress bar in this theme, at any
  viewport, ever (§9, rule 6).
- **Marquees** — refused. Nothing in a manuscript moves sideways forever.
  The binder's one horizontal device is the quire signature strip in the
  navigation (§6.13), which is static.
- **Ambient loops** — two, both rationed: the gold glint (§6.7, 6s
  offset loops, only while an initial is in view) and the vellum grain
  breath (a 14s `--ease-drift` opacity cycle between 0.5% and 0.9% on
  the grain layer — felt, not seen).
- **Micro-interactions** — the pilcrow stamp (§6.10, 160ms), the
  manicule's swivel to a hovered paragraph (§6.3, 250ms), miniature
  medallions tilting ≤4° toward the light (§6.11).
- **Hover physics** — no springs on content. The only overshoot in the
  theme belongs to the wrist (`--ease-swivel`) and the stamp
  (`--ease-stamp`); everything else lands exactly.
- **Page transitions** — a full page-curl wipe, 600ms `--ease-leaf`
  (§6.12), the leaf bending across to the next quire; disabled on slow
  connections and replaced by a 200ms crossfade.
- **Image treatments** — miniatures are duotone-mapped to the palette
  (lapis shadows, vellum highlights, rubric reserved for the one detail
  the caption names) and scale-in-frame 1.04 → 1 over 900ms
  `--ease-flare` inside their pricked margins as they reveal.

**The engine.** One shared `requestAnimationFrame` loop drives the
manicule, the curls, the parallax layers and the glint. Scroll position
is lerped at 0.12 per frame toward the true scroll offset; scrubbed
devices read the lerped value, triggered devices read IntersectionObserver
thresholds. Frame budget: the whole loop must cost ≤1.2ms per frame on a
mid-range Android device; the curl (§6.4) is the only element allowed to
approach that budget alone, and only inside its 60vh turn zone.

---

## 6. Signature elements

### 6.1 The painting historiated initial

- **What & why.** The hero's headline begins the way a great manuscript
  begins: its first letter is a small painting. Inside the bowl and stem
  of the initial, a scene from the book's own first chapter is painted —
  sky, hill, figure, gold ground — in the order a illuminator would lay
  the pigments down, while the rest of the headline writes on beside it in
  scribal strokes. If the visitor watches nothing else, they have learned
  the site's whole proposition: this text was *made*, by hand, in order.
- **Structure.** An `<h1>` of live text. The first letter is wrapped in
  `<span class="hist-initial" aria-hidden="true">` containing an inline
  SVG: the Fell glyph as a `<text>` element clipped by its own outline
  path, with four painted layers inside the clip — lapis sky, ink hill
  silhouette, a rubric figure, and a `--gold` ground field behind. The
  full headline, initial included, is the h1's accessible text; the SVG
  is decorative duplication and is `aria-hidden`. The scene's subject is
  authored per site from the first chapter's content (§10, blocking
  item 4): a publisher's initial shows its opening scene, a binder's
  shows the workshop.
- **Motion spec.** Paint order follows the illuminator's order, total
  1600ms: gold ground lays first (opacity 0→1, 300ms `--ease-flare`) —
  the gesso before the colour — then lapis sky (clip-path inset from the
  letter's top, 400ms), ink hill (inset from the base, 350ms), rubric
  figure last (a 2px-stroke draw, 450ms `--ease-quill`, overlapping the
  hill by 100ms). Simultaneously the remaining headline letters write on:
  each glyph's stroke-dashoffset animates at 28ms per letter,
  `--ease-quill`, beginning at t=200ms so the painting leads the writing
  by a breath. On completion all dashoffsets and clips are removed; the
  headline is plain live text with a painted initial.
- **Choreography timeline (v2).** t=0 hero painted, initial unpainted
  outline, headline letters at dashoffset full → t=0–300ms gold ground
  lays → t=200ms write-on begins (28ms/letter) → t=300–700ms lapis sky
  insets down → t=550–900ms ink hill insets up → t=800–1250ms rubric
  figure draws → t≈1250–1600ms write-on completes, attributes cleaned,
  the manicule (§6.2) makes its first travel step. Total ≈1.6s, once per
  page load, never on repeat in-page navigation.
- **State matrix (v2).** *Rest (pre-trigger):* initial as outline,
  headline complete in the DOM and readable — desktop and touch
  identical. *Hover:* none; the initial is not interactive. *Focus:* the
  h1 is not focusable; nothing changes. *Active:* none. *Scrolled-past:*
  fully painted state, static. *Disabled:* JS off or fallback fired —
  the initial renders fully painted from first paint (the SVG layers
  ship in their final state in the markup; JS only *rewinds* them to
  animate). That inversion — markup is the finished painting — is the
  theme's standing construction rule for every painted element.
- **Content merge.** The painting is inside the headline's own first
  letter; the scene illustrates the chapter the headline announces.
  Remove the animation and the hero still opens with a painted initial —
  the device *is* the typography.
- **Failure fallback.** The 1s law (§10): a watchdog started at first
  paint forces all layers to final state at t=1000ms if the choreography
  has not begun (font swap pending, tab inactive), and any layer not
  complete by t=2600ms snaps to final. The headline text is never
  dashoffset-hidden in markup, so a total JS failure still shows the
  full headline — the write-on is applied by JS, removed by JS or by
  the watchdog, never required by the content.
- **Reduced-motion variant.** No painting sequence, no write-on: the
  initial ships painted, the headline plain. Identical information,
  identical order.
- **Breakpoints (v2).** ≥1200px: as specced at 56px display. 768–1199px:
  44px display; paint order unchanged, write-on at 22ms/letter. <768px:
  the scene simplifies to two layers (gold ground + figure) — a 34px
  letter cannot hold four legible layers — and the write-on is cut
  entirely; the headline simply appears, painted initial in place.
- **Edge cases & failure modes (v2).** *Headline begins with a letter
  whose bowl holds no scene* (I, J, or a numeral): the scene moves to
  the first *paintable* letter and the true first letter is rubricated
  instead — the rule is authored per headline at build time, never
  improvised. *Very long headline (>14 words):* write-on caps at 40
  letters; the remainder appears with the last batch — a headline is not
  a paragraph and may not take 4s to arrive. *Font fails to load:* the
  initial falls back to the EB Garamond glyph and the paint proceeds;
  a headline never waits on a display face (§10, item 9 analogue).
- **Accessibility spec (v2).** The h1's accessible name is the full
  headline text, initial's letter included exactly once. The SVG scene
  is `aria-hidden`. The painting is never the sole carrier of meaning:
  the scene illustrates, the words state. Contrast of the headline text
  itself is `--ink` on `--vellum`, 11.04:1, at every frame — the paint
  layers live *inside* the glyph outline and never wash over the
  remaining letters.
- **Performance budget & mobile variant.** One SVG, four layer
  animations, ≤40 dashoffset updates: ≤0.4ms/frame during the 1.6s
  sequence, zero thereafter. Mobile variant: the two-layer simplification
  above; cost halves.
- **Tokens consumed (v2).** `--vellum`, `--ink`, `--rubric`, `--lapis`,
  `--gold`, `--ease-quill`, `--ease-flare`, `--dur-paint: 1600ms`,
  `--dur-letter: 28ms`.

### 6.2 The travelling manicule guide

- **What & why.** The theme's guide and its progress indicator in one
  body: a drawn manicule — pointing hand, cuff at the wrist, a small
  rubric band on the cuff — travels down the left margin scrubbed to
  scroll, always level with the paragraph currently being read, its
  pointing angle rotating to match each section's posture. It does the
  exact job its medieval original did: it shows the reader where they
  are and what matters here. Everything else in the margin is in
  support of, or in deference to, the hand.
- **Structure.** An inline SVG (hand path, cuff, rubric cuff-band) inside
  `<div class="manicule" aria-hidden="true">`, absolutely positioned in
  the margin band (§4) and translated by the shared lerp loop. The hand
  is 54px wide at ≥1200px. A visually-hidden live region
  (`aria-live="polite"`, updated at section changes only) carries the
  hand's information for assistive tech: current section name and its
  folio (§6.8). Per-section posture angles are authored as data
  attributes on each section (`data-posture="-14"` etc., range ±20°).
- **Motion spec.** Travel: the hand's Y is a scrubbed function of lerped
  scroll — it sits level with the vertical centre of the paragraph whose
  top has most recently crossed the viewport's 38% line (the reading
  line). Between paragraphs it glides; it never jumps except at a
  chapter turn, where it lifts (translateX −6px, a small hop out of the
  text's way) while the leaf curls (§6.4) and lands beside the new
  chapter's first paragraph. Posture: rotation interpolates toward the
  current section's `data-posture` across the section's first 20vh of
  travel, `--ease-swivel` easing on the interpolation. Cuff ornament
  (§6.9) draws once when the hand first enters each quire.
- **Choreography timeline (v2).** Continuous, beat-free by design: each
  frame, hand Y = lerp(current, target paragraph centre, 0.12) →
  rotation = slerp toward section posture weighted by progress through
  the section's first 20vh → at chapter boundary crossing, hop begins
  (−6px over 120ms) → curl zone entered (§6.4) → at curl completion the
  hand lands beside the new first paragraph (+6px back over 180ms
  `--ease-swivel`) and the catchword (§6.5) ticks. No timeline exists
  outside the reader's own scroll; the hand's speed *is* the reader's.
- **State matrix (v2).** *Rest:* level with the current paragraph,
  posture matched. *Hover:* delegated to §6.3 — a hovered paragraph
  swivels the hand away from the scroll position. *Focus:* when focus
  moves by keyboard to a paragraph or heading, the hand travels to it
  (same glide) — the guide serves keyboard readers identically.
  *Active:* none. *Scrolled-past:* the hand never points backward; at
  the page foot it comes to rest beside the catchword, finger level
  with it — its final duty is pointing at what comes next. *Disabled:*
  JS off — the hand is present in markup beside the *first* paragraph,
  static, still doing a reduced version of its job; with reduced motion
  it updates on click/section change only (§6.2 reduced variant).
  *Touch:* identical to desktop; the hand responds to scroll, not to
  touch position.
- **Content merge.** The hand points at the actual paragraph being read
  — its target list is the document's own paragraphs, computed from the
  DOM, not a decorative track. If a page has no paragraphs (a pure
  listing), the hand does not appear; §6.13's navigation carries the
  wayfinding instead.
- **Failure fallback.** If the lerp loop fails or is absent, the hand
  renders statically beside the first paragraph (its markup position).
  If any target computation throws, the hand parks at the current
  chapter heading rather than vanishing — a guide that disappears has
  failed worse than a guide that waits.
- **Reduced-motion variant.** The hand does not travel. It rests beside
  the current chapter heading and updates its position discretely when
  the reader clicks a heading or a navigation link, and at chapter
  boundaries via the live region. Same information, no glide.
- **Breakpoints (v2).** ≥1200px: full travel in the 148px band, 54px
  hand. 768–1199px: band narrows to 96px, hand 44px, posture range
  compresses to ±12° (less margin, less theatre). <768px: the margin
  band collapses — the hand shrinks to 30px and travels in a 44px
  gutter at the leaf's left edge, pointing at paragraph *starts* rather
  than centres, and the pinned initial (§6.6) yields its place to it
  (never both competing in a phone's margin).
- **Edge cases & failure modes (v2).** *Paragraph taller than the
  viewport* (a long legal or scholarly passage): the hand tracks the
  reading line itself through the paragraph instead of waiting at its
  centre — the target becomes the 38% line's position within the
  paragraph. *Reader scrolls back up:* the hand retraces exactly; its
  posture re-interpolates toward the earlier section. There is no
  hysteresis and no "already visited" state — a finding-aid does not
  judge. *Very fast scroll:* the lerp lets the hand trail by up to
  ~120px and catch up within ~400ms of the scroll stopping; it never
  teleports mid-gesture. *Print:* the hand prints beside the first
  paragraph of each chapter (CSS `@media print` repositions per
  chapter) — the one place the theme spends effort on paper.
- **Accessibility spec (v2).** The SVG is `aria-hidden`; its information
  is duplicated in the polite live region (section name + folio, updated
  at most once per section change, never per scroll frame). The hand is
  never focusable and never the only indicator of position — the folio
  (§6.8) and catchword (§6.5) carry the same facts in text. Touch
  target: none required (non-interactive). Contrast: the hand is drawn
  in `--ink` with a `--rubric` cuff band on `--vellum` — its outline
  holds 11.04:1; the gold flecks on its cuff (§6.7) are decorative and
  excluded from the contrast claim.
- **Performance budget & mobile variant.** One transform + one rotation
  per frame from the shared loop: ≤0.15ms/frame. Mobile variant: the
  30px gutter form above; rotation updates at half rate (every second
  frame) — posture is a nuance a phone margin cannot show anyway.
- **Tokens consumed (v2).** `--ink`, `--rubric`, `--gold`,
  `--margin-band`, `--ease-swivel`, `--lerp: 0.12`, `--hand-w: 54px`,
  `--reading-line: 38%`.

### 6.3 The manicule swivel (hover & focus)

- **What & why.** The guide notices the reader. Hovering — or
  keyboard-focusing — any paragraph swivels the manicule away from the
  scroll-current paragraph to point at the attended one instead, with a
  slight hop toward the text, as if the scribe leaned in. It is the
  theme's acknowledgement that attention and scroll position are not
  the same thing, and it is the only element that lets the reader
  *direct* the apparatus.
- **Structure.** No new DOM: a behaviour layered on §6.2's hand.
  Paragraphs carry `data-attend` listeners (pointerenter/focusin,
  delegated at the article level). The hand's transform gains a
  swivel-target override that outranks the scroll target until
  pointerleave/focusout clears it.
- **Motion spec.** Swivel: rotation to the attended paragraph's implied
  posture (its section posture + up to 6° toward the paragraph) and a
  translateX hop of +8px toward the text, over 250ms `--ease-swivel`
  (the wrist overshoot lives here). Dwell rule: the override engages
  only after the pointer has rested on the paragraph for 120ms — a
  reader skimming the page with the mouse must not set the hand
  dancing. Return: on leave, the hand glides back to the scroll target
  over 350ms `--ease-quill` — returning is calmer than arriving.
- **Choreography timeline (v2).** t=0 pointer enters paragraph →
  t=120ms dwell satisfied, override engages → t=120–370ms swivel + hop
  → hold while attended → pointer leaves → t=+0–350ms glide back to
  scroll target and section posture. Focus path identical, dwell 0ms —
  a keyboard focus is never a skim.
- **State matrix (v2).** *Rest:* no override; §6.2 governs. *Hover:*
  as specced, desktop pointer only (`pointer: fine` media query gates
  the listener). *Focus:* focusin on any focusable element inside a
  paragraph — or the paragraph itself when reached via heading
  navigation — engages with 0ms dwell. *Active:* a click during hover
  adds §6.10's pilcrow if the target is a heading; on a paragraph, no
  change. *Scrolled-past:* if the reader scrolls while hovering (wheel
  over a still mouse), the scroll target wins after 600ms — the page
  is moving, the hand follows the page. *Disabled:* reduced-motion or
  touch — no swivel; on touch, a tap on a paragraph moves the hand
  discretely (the §6.2 reduced behaviour) since touch has no hover to
  borrow.
- **Content merge.** The hand points at the paragraph the reader is
  actually attending to — the override target is a real paragraph in
  the reading column, and the swivel angle is computed from its real
  position relative to the hand.
- **Failure fallback.** If listeners fail, §6.2's scroll behaviour is
  untouched — the swivel is pure addition. No content depends on it.
- **Reduced-motion variant.** No swivel, no hop: on dwell, the hand
  relocates discretely to the attended paragraph (same rule as §6.2's
  reduced travel).
- **Breakpoints (v2).** ≥1200px and 768–1199px: as specced (hop +8px /
  +5px in the narrower band). <768px: swivel rotation only, no hop —
  the 44px gutter has no room for the hand to lean.
- **Edge cases & failure modes (v2).** *Pointer resting in the margin
  while reading:* no paragraph is hovered; nothing engages — the hand
  stays with the scroll. *Rapid paragraph-to-paragraph movement:*
  each new dwell restarts the 120ms timer; the hand moves at most
  once per settled attention. *Hover during a page-curl (§6.4):* the
  curl owns the hand; overrides queue and apply after the landing hop.
- **Accessibility spec (v2).** The swivel is silent: the live region
  (§6.2) does not announce hover-driven moves (they would chatter);
  focus-driven moves into a *new section* announce via the section
  change as usual. The hand remains `aria-hidden` throughout. No
  information is hover-only: everything the hand indicates is also in
  the folio/catchword text apparatus.
- **Performance budget & mobile variant.** Listener delegation + one
  transform override in the shared loop: ≤0.05ms/frame, and only while
  an override is active. Mobile variant: tap-to-move, discrete (§6.2).
- **Tokens consumed (v2).** `--ease-swivel`, `--ease-quill`,
  `--dur-swivel: 250ms`, `--dur-return: 350ms`, `--dwell-hover: 120ms`.

### 6.4 Scrubbed page-curl chapter turns

- **What & why.** Chapters in a manuscript do not fade in; the leaf
  turns. At each chapter boundary a page-curl is scrubbed to scroll
  through a ~60vh turn zone: the current leaf bends from its outer
  corner, its underside (`--vellum-deep`, carrying the chapter's last
  catchword) rolling over to reveal the next chapter already printed
  beneath. Scroll faster, the leaf turns faster; scroll back, it
  un-turns. It is the theme's largest gesture and its strictest test:
  the text beneath is never masked for longer than the turn itself.
- **Structure.** Each chapter is a `<section class="chapter">` in
  normal flow — the document scrolls ordinarily and is fully readable
  with no JS at all. The curl is an overlay leaf: a
  `<div class="curl-leaf" aria-hidden="true">` duplicating *no text* —
  it carries only the vellum surface, the underside catchword (real
  text, duplicated from §6.5's data), and a gradient shading computed
  from curl geometry. The bend is rendered with a CSS 3D transform
  (rotateY on a hinged wrapper with a moving clip-path polygon), not
  WebGL: a leaf is paper, and paper's maths is a fold, not a shader.
- **Motion spec.** Turn zone: the 60vh of scroll straddling the chapter
  boundary (30vh before, 30vh after). Curl radius maps linearly to
  lerped scroll progress through the zone: at zone entry the leaf is
  flat; at midpoint the bend's apex crosses the reading column; at
  zone exit the leaf has rolled fully to the spine and fades its last
  2% as it settles behind the margin. The revealed chapter beneath is
  live and scrollable throughout — its first paragraph is readable
  from the moment the bend uncovers it, which is the entire point of
  scrubbing rather than animating.
- **Choreography timeline (v2).** Zone entry (progress 0): leaf flat,
  manicule hops out of the way (§6.2, −6px, 120ms) → progress 0–0.5:
  corner lifts, underside catchword becomes legible at ≈0.3 →
  progress 0.5: apex crosses the column, shading gradient at maximum
  contrast → progress 0.5–1: leaf rolls toward the spine, next
  chapter's rubricated heading flares as it is uncovered (§5) →
  progress 1: leaf settled, overlay released, manicule lands beside
  the new first paragraph, catchword ticks (§6.5), folio ticks (§6.8).
  Reverse scroll runs the film backward exactly, including the ticks.
- **State matrix (v2).** *Rest:* outside turn zones, no overlay exists
  in the layout (it is `visibility: hidden` and out of the a11y tree).
  *Hover/focus:* no interaction; the curl is scroll's, not the
  pointer's. *Active:* none. *Scrolled-past:* completed turns leave no
  residue — the previous chapter is ordinary scrolled content.
  *Disabled:* JS off — there is no curl and no need of one; chapters
  follow each other in flow with their 6-leading gap (§4). Reduced
  motion: §6.4 variant below. *Touch:* identical scrubbing; touch
  scroll *is* the reader's hand on the leaf, which suits the device
  better than the mouse does.
- **Content merge.** The curling surface is the chapter's own leaf and
  the text revealed is the next chapter's own first page — the overlay
  carries no content of its own except the underside catchword, which
  is the boundary's real catchword (§6.5).
- **Failure fallback.** The 1s flatten law: if the lerp loop stalls
  (tab backgrounded mid-turn, JS error), a watchdog flattens any
  in-progress curl to its nearest completed state within 1000ms —
  the overlay hides, both chapters stand in plain flow. Text is never
  masked by a *stuck* curl; a curl may only ever be *moving*.
- **Reduced-motion variant.** No bend. At the boundary, the previous
  chapter's foot crossfades (200ms) to the next chapter's head as the
  reader crosses — the reduced manuscript still turns its leaves, it
  just doesn't bend them.
- **Breakpoints (v2).** ≥1200px: full curl from the outer (right)
  corner, 60vh zone. 768–1199px: curl from the bottom-right, zone
  50vh — a narrower leaf bends from its corner, not its edge.
  <768px: the curl becomes a *lift*: the leaf translates up and fades
  its underside over a 40vh zone with no 3D bend — phone GPUs and
  phone readers both prefer the simpler honesty, and the catchword on
  the underside remains legible throughout, which the bend could not
  promise at 30px type.
- **Edge cases & failure modes (v2).** *Reader jumps via anchor or
  find-in-page across a boundary:* no curl — the hand and apparatus
  re-seat at the destination chapter discretely; curls are for
  *reading* through, not for teleporting. *Two boundaries close
  together* (a very short chapter < 60vh): turn zones merge; the
  single curl serves both, and the short chapter is read on the
  revealed leaf between the two halves of the zone — authored minimum
  chapter length is one full viewport (§9, rule 7). *Scroll-back at
  the exact midpoint:* the geometry is a pure function of scroll
  position, so there is no state to corrupt; the leaf simply bends
  the other way. *Low-power device:* if the shared loop's frame cost
  exceeds budget for 30 consecutive frames inside a zone, the curl
  degrades to the <768px lift behaviour for the rest of the page
  (§14 cut order, step 2).
- **Accessibility spec (v2).** The overlay leaf is `aria-hidden` and
  `pointer-events: none` at all times; the chapters beneath are in
  normal reading order and reachable by keyboard without crossing
  any trap — focus is never inside the curl. The underside catchword
  duplicates §6.5's text and is hidden from AT for the same reason.
  A chapter change is announced by §6.8's live region, not by the
  visual bend.
- **Performance budget & mobile variant.** The theme's most expensive
  element: one clip-path polygon + one transform + one gradient
  recomputed per frame *inside the zone only* — ≤1.0ms/frame in-zone,
  0 out of zone. Mobile variant: the lift described above, ≤0.3ms.
- **Tokens consumed (v2).** `--vellum`, `--vellum-deep`, `--gold`,
  `--ease-leaf`, `--turn-zone: 60vh`, `--lerp: 0.12`.

### 6.5 Catchword updates

- **What & why.** At the foot of every page the binder copied the first
  word of the next gathering, so loose quires could be assembled in
  order. Here, each section's foot carries its catchword — the next
  section's actual first word, set in small caps at the right of the
  foot, beside the quire signature — and it updates as the reader
  crosses into the next section. It is a promise the page makes and
  keeps in the reader's peripheral vision: *this is what comes next,
  and it is really next.*
- **Structure.** A `<footer class="leaf-foot">` per section containing
  the quire signature (`<span class="quire-sig">Quire III</span>`, left)
  and the catchword (`<span class="catchword">` containing the next
  section's first word as live text, right). The catchword's value is
  computed at build time from the actual document — a build script (or
  the CMS template) extracts each section's first word; it is never
  hand-typed, because a hand-typed catchword eventually lies.
- **Motion spec.** On section change the catchword crossfades: old word
  out (140ms), new word in (160ms), `--ease-flare`, with a 1px
  translateY settle — the eye glancing down finds the new word already
  resting. No crossfade on first load: the first catchword is simply
  there, as it is on a real first leaf.
- **Choreography timeline (v2).** Section boundary crossed (shared
  loop) → t=0 folio tick begins (§6.8) → t=60ms catchword fade-out
  starts → t=200ms old word gone → t=200–360ms new word fades in and
  settles → t=360ms foot is quiet. The catchword deliberately ticks
  *after* the folio: the reader's eye goes to the number first, the
  promise second.
- **State matrix (v2).** *Rest:* current section's catchword displayed.
  *Hover:* the catchword is a link to the next section (its one
  interactive duty) — hover underlines it with a 1px lapis rule drawn
  left-to-right over 200ms `--ease-quill`. *Focus:* visible focus ring
  (§6.5 a11y) and the same underline, drawn instantly. *Active:* click
  scrolls smoothly to the next section head (or jumps, under reduced
  motion). *Scrolled-past:* feet already passed keep the catchword of
  their own section — each foot is a historical record of its leaf,
  not a live ticker; only the *current* foot updates, which is the one
  in or near the viewport. *Disabled:* JS off — every foot shows its
  own section's correct catchword from markup; nothing to update,
  nothing broken.
- **Content merge.** The catchword is the next section's real first
  word and a working link to it. It is the manuscript's continuity
  device performing continuity.
- **Failure fallback.** If the build-time extraction is missing for a
  section, the catchword position renders the quire signature only —
  an absent catchword is honest; a wrong one is a §10 blocking
  failure. Runtime JS failure changes nothing (see Disabled).
- **Reduced-motion variant.** The word swaps instantly at the boundary;
  the link behaviour is unchanged.
- **Breakpoints (v2).** ≥1200px and 768–1199px: as specced. <768px: the
  leaf-foot stacks — quire signature above, catchword below, both
  left-aligned; the catchword's tap target grows to 44px height.
- **Edge cases & failure modes (v2).** *Next section begins with a
  numeral, a name, or a word in another language:* the catchword is
  still that word, exactly as printed, accents and all — the binder
  copied what was there. *Final section of the page:* its catchword is
  the first word of whatever the site itself says comes next — the
  next page's first word if the template knows it, else the colophon's
  first word ("Explicit" is the traditional choice, and §6.17 uses it
  honestly: the colophon really does begin with it). *One-word
  section:* its catchword is the following section's first word; the
  chain never skips.
- **Accessibility spec (v2).** The catchword link's accessible name is
  "Next: [section title]" — the word alone would be meaningless to a
  screen reader, so the link carries `aria-label` with the destination
  while the visible text stays the bare word. Focus ring: 2px
  `--lapis` outline, offset 3px, on `--vellum` (7.53:1). Touch target
  ≥44×44px on all breakpoints (padding, not font size, grows).
- **Performance budget & mobile variant.** One opacity/transform
  transition per section change; effectively free. Mobile: the stacked
  foot above.
- **Tokens consumed (v2).** `--ink-soft`, `--lapis`, `--ease-flare`,
  `--ease-quill`, `--dur-catch: 300ms`.

### 6.6 The pinned historiated initial

- **What & why.** A chapter's opening initial does not scroll away and
  abandon its text. It pins in the margin — the manicule's band,
  yielding pride of place — for the length of its chapter, shimmering
  faintly, while the chapter's paragraphs scroll beside it. It is a
  bookmark made of the chapter's own first letter, and it tells the
  reader at a glance *which* beginning they are still inside.
- **Structure.** Each chapter's first paragraph opens with a drop
  initial: a live Fell glyph in an inline SVG frame (60×60px at
  ≥1200px), painted with the chapter's miniature scene in the same
  four-layer technique as §6.1 (simplified to two layers — gold ground
  + one scene colour — at chapter scale). The initial begins in flow
  at the paragraph's head; when the paragraph's top scrolls past the
  margin's anchor line, the initial's *margin double* — a second,
  smaller rendering — takes its place pinned in the band, and the
  in-flow initial scrolls on with its paragraph. One letter, two
  duties, handed over invisibly.
- **Motion spec.** The initial paints on chapter entry with §6.1's
  order compressed to 900ms. The handover to the pinned double is a
  200ms crossfade at the anchor line — no travelling, no scaling; a
  letter does not commute. While pinned, the gold ground carries
  §6.7's glint at its slowest offset. On chapter exit (the next
  chapter's turn, §6.4) the pinned initial fades in 200ms as the leaf
  bends — it leaves with its leaf.
- **Choreography timeline (v2).** Chapter entered → t=0–900ms initial
  paints in flow (gold 0–200, scene 200–700, figure 600–900) → reader
  scrolls; paragraph top crosses anchor → t=0–200ms crossfade to
  pinned double → pinned duration: glint cycle (§6.7) → chapter exit
  begins → t=0–200ms pinned initial fades as the curl starts.
- **State matrix (v2).** *Rest:* in flow, painted. *Hover:* the pinned
  initial is a link back to the chapter head — hover tilts it ≤3°
  toward the light (§6.11's medallion physics, shared). *Focus:*
  lapis ring (§6.5 pattern) and the tilt applies instantly. *Active:*
  click returns the reader to the chapter head (smooth scroll, or
  jump under reduced motion). *Scrolled-past:* chapter exited — the
  initial is gone from the margin; the manicule (§6.2) resumes the
  band. *Disabled:* JS off — no pinning exists; initials stay in flow
  at their paragraph heads, fully painted, which is simply how
  manuscripts look. *Touch:* tap = the click behaviour; no tilt.
- **Content merge.** The pinned letter is the chapter's actual first
  letter, painted with the chapter's actual opening scene. It is not
  a generic ornament: a different chapter pins a different letter.
- **Failure fallback.** If pinning fails (no IntersectionObserver,
  JS error), initials remain in flow — the designed disabled state.
  The margin double never appears without its in-flow original having
  painted first, so a half-painted letter can never pin.
- **Reduced-motion variant.** No pinning and no handover: the initial
  stays in flow (manuscripts managed). The chapter's identity in the
  margin is carried by §6.8's apparatus text instead.
- **Breakpoints (v2).** ≥1200px: as specced, 60px initial, 44px pinned
  double. 768–1199px: 52px / 38px. <768px: **the pin yields to the
  manicule** (§6.2) — the phone margin holds one device, and the guide
  outranks the bookmark; initials remain in flow only.
- **Edge cases & failure modes (v2).** *Chapter shorter than one
  viewport:* the initial never pins (its paragraph never leaves) —
  correct; a one-screen chapter needs no bookmark. *Chapter begins
  with a paintable-letter problem* (I, J, numeral): §6.1's rule
  applies — first paintable letter carries the scene, true first
  letter is rubricated in flow, and the *rubricated* letter is what
  pins (a pinned plain letter is still a bookmark). *Reader jumps
  mid-chapter via anchor:* the correct chapter's initial pins
  immediately in its painted state; no paint sequence replays.
- **Accessibility spec (v2).** The in-flow initial's letter is part of
  the paragraph's text (the SVG is `aria-hidden`, the letter present
  in the DOM text exactly once — the word must read whole: "Once",
  never "O" + "nce" to a screen reader). The pinned double is a link
  with `aria-label="Back to the head of [chapter title]"`. Tilt and
  glint are decorative. Focus order: the pinned link sits in the tab
  order at its chapter's position, not at the page top.
- **Performance budget & mobile variant.** Painting reuses §6.1's
  machinery at half cost; the pin itself is one sticky-positioned
  element (compositor-only). Mobile: in-flow only, as specced.
- **Tokens consumed (v2).** `--gold`, `--gold-pale`, `--rubric`,
  `--lapis`, `--ease-flare`, `--dur-paint-chapter: 900ms`,
  `--initial-size: 60px`.

---

### 6.7 Gold-fleck glint

- **What & why.** Gold leaf does not shine; it *answers* light. Across
  the gold grounds of the initials (§6.1, §6.6) and the flecks on the
  manicule's cuff, a slow specular sweep passes — a brightening that
  travels like a candle carried past the leaf — on offset 6s loops, so
  no two initials ever glint in step. It is the theme's one purely
  atmospheric device, and it is rationed accordingly: it exists to
  make the gold feel like metal, and for no other reason.
- **Structure.** A gradient overlay inside each gold field's SVG: a
  `--gold-pale` linear gradient at 18% peak opacity, its position
  animated by the shared loop, masked to the gold shapes only. No
  overlay ever touches text or the vellum ground.
- **Motion spec.** Each gold field runs a 6s cycle: 4.2s still, then a
  1.8s sweep (`--ease-flare`) in which the gradient crosses the field
  at a 24° angle — the candle's path. Cycles are offset per element by
  its index × 1.7s. At night (§2) the sweep gains the ±4% candle
  flicker at 0.11Hz. The sweep runs only while the element is within
  the viewport (IntersectionObserver gate); off-screen gold is still.
- **Choreography timeline (v2).** Per field, repeating: t=0–4.2s rest
  (gradient parked off-field) → t=4.2–6.0s sweep crosses → t=6.0s
  cycle restarts with the element's offset applied globally. There is
  no trigger choreography beyond the viewport gate; ambient time is
  the trigger.
- **State matrix (v2).** *Rest:* between sweeps, plain gold. *Hover:*
  hovering an initial (§6.6) calls one immediate sweep — the reader
  tilting the leaf to the light — then the cycle resumes. *Focus:*
  same single sweep, no loop change. *Active:* none. *Scrolled-past:*
  gate closes, gold rests. *Disabled:* JS off or reduced motion — the
  gradient is absent from markup application (JS-applied only); gold
  is flat leaf, which is historically accurate anyway.
- **Content merge.** The glint lives inside the gold of the initials
  themselves; it decorates nothing that is not already gold, and gold
  (§2, law 1) never carries information — so the glint can never make
  content harder or easier to read.
- **Failure fallback.** Absence is the fallback: if the loop or the
  gradient fails, gold fields render flat. Nothing else references
  the glint's state.
- **Reduced-motion variant.** No sweeps, no flicker. Flat gold.
- **Breakpoints (v2).** All breakpoints: as specced. <768px: sweep
  duration shortens to 1.2s within the same 6s cycle (smaller fields
  cross faster), and the night flicker is cut — a phone's candle is
  steady (§14 cut order, step 1).
- **Edge cases & failure modes (v2).** *Many initials in view* (a
  contents page of chapter openings, §6.13): at most three fields
  sweep concurrently; the rest queue by offset — a page of gold all
  flashing in rotation reads as a slot machine, not a scriptorium.
  *Battery saver / `save-data`:* the loop does not start. *Tab
  hidden:* the shared loop pauses globally; on return, cycles resume
  from their offsets without a synchronised flash.
- **Accessibility spec (v2).** Purely decorative, `aria-hidden` by
  construction (inside the hidden SVGs). The sweep's peak luminance
  change is ≤18% opacity of a pale gradient — far below any flash
  threshold; it never strobes (one sweep per 6s per field, maximum).
  No contrast claim anywhere depends on gold (§2, law 1).
- **Performance budget & mobile variant.** Gradient position updates
  inside the shared loop: ≤0.05ms/frame for all fields combined;
  fields off-screen cost zero. Mobile: the shortened sweep above.
- **Tokens consumed (v2).** `--gold`, `--gold-pale`, `--ease-flare`,
  `--dur-glint: 6s`, `--glint-offset: 1.7s`.

### 6.8 The roman-numeral apparatus

- **What & why.** The manuscript counts itself. In the outer margin of
  each section, the apparatus records the folio (leaf number) and the
  quire (gathering number), in roman numerals, advancing as sections
  pass: *fol. xxiij · quire III*. It is the theme's textual progress
  system — precise, diegetic, and honest, because the numbers are
  computed from the document's real structure: one folio per section,
  one quire per four folios, by the binder's arithmetic.
- **Structure.** A `<div class="apparatus">` in the outer margin per
  section: folio line, quire line, and — once per quire — the quire's
  catchword signature repeated small. Numerals are generated at build
  time from section order (a build helper converts 1→j, 2→ij, 3→iij,
  4→iiij, 5→v… using the medieval convention of final *j* for the
  last *i* — a detail §12's voice rules protect). A single
  visually-hidden live region (§6.2) announces "Leaf xxiij, quire III,
  [section title]" at section changes.
- **Motion spec.** On section change, the incoming section's apparatus
  crossfade-ticks: old folio out / new folio in, 200ms `--ease-flare`,
  staggered 60ms after §6.5's catchword begins its own tick — the
  apparatus of a leaf settles as a set, never in unison, never in
  competition.
- **Choreography timeline (v2).** Boundary crossed → t=0 catchword
  starts (§6.5) → t=60ms apparatus fade-out (90ms) → t=150ms numeral
  swaps in DOM → t=150–350ms fade-in → t=350ms live region updates
  (the announcement lands after the visual, so sighted and non-sighted
  readers are told at the same moment).
- **State matrix (v2).** *Rest:* current folio/quire displayed.
  *Hover/focus/active:* the apparatus is not interactive; no states.
  *Scrolled-past:* each section's own apparatus remains by its section
  (like §6.5's feet, they are records, not tickers) — the *live*
  reading is the one in view. *Disabled:* JS off — all apparatus is
  static markup, complete and correct; the tick is an enhancement on
  a finished system. *Touch:* identical.
- **Content merge.** The numbers are the document's real leaf and
  gathering counts. A template that hard-codes "fol. j" beside the
  ninth section has failed the truth rule (§10, blocking item 4).
- **Failure fallback.** Build-time generation means there is no
  runtime to fail; a section missing its generated apparatus renders
  without it, and the §10 gate catches the omission before ship.
- **Reduced-motion variant.** Numerals swap instantly; the live-region
  announcement is unchanged.
- **Breakpoints (v2).** ≥1200px: outer margin, two lines. 768–1199px:
  one line ("fol. xxiij · III") to fit the narrower outer margin.
  <768px: the apparatus moves inline — a single apparatus line above
  each section heading, left-aligned with the text block (the phone
  leaf has no outer margin to spare).
- **Edge cases & failure modes (v2).** *Long documents (>39 folios):*
  numerals follow standard subtractive form from xl onward; the
  final-j convention applies only to terminal i-runs (xxxviiij is
  correct; xxxix is the modern form and §12 allows it from xl —
  consistency within a page is the gate, not pedantry). *Sections
  added by the CMS after build:* the generator runs in the template
  on every render, never as a one-off script — apparatus is a
  function of the document, or it is a lie waiting to happen.
- **Accessibility spec (v2).** Numerals are text, read by AT as
  written; the live region speaks the section title with the folio
  so the announcement is useful ("Leaf 23, quire 3, The Binding").
  The visible apparatus is set in `--ink-soft` at 15px (≈5.9:1) —
  apparatus-grade information, duplicated in the announcement and in
  the navigation (§6.13), so its contrast tier is lawful.
- **Performance budget & mobile variant.** Static text plus one 200ms
  transition per boundary. Free. Mobile: the inline line above.
- **Tokens consumed (v2).** `--ink-soft`, `--ease-flare`,
  `--dur-tick: 200ms`.

### 6.9 Cuff-and-vine SVG draw

- **What & why.** The scribe decorates his own guide. When the
  manicule first enters a new quire, the ornament on its cuff — a
  small interlace — and a marginal vine that runs beside the hand's
  path draw themselves in stroke, leafing as they go: stem first, then
  leaves alternating, then one lapis berry-cluster per quire. The vine
  is the margin's memory of where the hand has been: it grows through
  the quire and stops at the quire's end.
- **Structure.** Two inline SVGs: the cuff interlace (part of §6.2's
  hand SVG, a `<path>` with dasharray animation) and the vine (a
  per-quire `<svg class="vine">` absolutely positioned in the margin
  band, height equal to the quire's sections, paths for stem, leaves
  and berries drawn in `--ink`, `--rubric` and `--lapis`
  respectively). Vine geometry is authored per template (a gentle
  S-curve the layout reserves), not generated from content — it is
  the margin's furniture, drawn once per quire.
- **Motion spec.** On quire entry: cuff interlace draws in 600ms
  `--ease-quill`. The vine draws progressively *with* the hand's
  travel: stem dashoffset is scrubbed to the hand's progress through
  the quire (the vine grows because the hand passes), leaves pop
  (scale 0→1, 150ms `--ease-flare`) as the stem's draw passes their
  attachment points, berries fill last, when the quire's final
  section is entered.
- **Choreography timeline (v2).** Quire boundary crossed → t=0–600ms
  cuff draws → hand descends: stem scrubbed continuously (no fixed
  timeline; it is a function of the hand's Y) → leaf thresholds
  crossed: each leaf pops within its 150ms → final section entered →
  berries fill over 400ms `--ease-flare` → quire complete: vine
  static for the rest of the page. Scrolling back un-grows nothing —
  a drawn vine stays drawn (the scribe does not erase); only the
  stem's *undrawn* portion responds to position.
- **State matrix (v2).** *Rest:* vine drawn to the hand's furthest
  reach in this quire. *Hover/focus/active:* none — the vine is not
  interactive. *Scrolled-past:* fully drawn vines remain in their
  margins as records. *Disabled:* JS off — vines render fully drawn
  in markup (finished-state construction, §6.1's rule); the growth is
  the enhancement. *Touch:* identical scrubbing via scroll.
- **Content merge.** The vine grows along the path the hand actually
  travels, in the margin the hand serves, and its berries mark the
  quire's completion — ornament with a bookkeeping duty. It never
  enters the text block or crosses a miniature.
- **Failure fallback.** Fully-drawn markup state (above). A scrub
  failure leaves a partially drawn vine that still reads as a vine;
  the §6.4 watchdog's flatten also completes any in-progress cuff
  draw.
- **Reduced-motion variant.** Vines ship drawn; the cuff ships drawn.
  Nothing grows.
- **Breakpoints (v2).** ≥1200px: full vine in the 148px band.
  768–1199px: stem + leaves, berries cut (the 96px band cannot hold
  the cluster legibly). <768px: vine cut entirely — the 44px gutter
  carries the hand alone (§14 cut order, step 3); the cuff interlace
  remains, as part of the hand itself.
- **Edge cases & failure modes (v2).** *Short quire (one section):*
  stem draws with the section's entry in a fixed 600ms (there is no
  travel to scrub to) and berries fill immediately — a one-leaf
  gathering still gets its vine. *Reader enters mid-quire by anchor:*
  the vine renders drawn up to the entry section; growth resumes
  from there. *Repeated quires:* each quire's vine is a fresh SVG
  with the same path — repetition of *furniture* is period-correct
  (the scribe had one vine style), and §9 distinguishes this from
  repeated content.
- **Accessibility spec (v2).** Both SVGs `aria-hidden`. The vine's
  one fact — quire progress — is carried in text by §6.8. No focus,
  no interaction, no contrast dependency (drawn in `--ink`/`--rubric`
  on `--vellum`, both AA+ at these stroke widths).
- **Performance budget & mobile variant.** One dashoffset update in
  the shared loop while a quire is active: ≤0.05ms/frame. Mobile:
  cut, as specced.
- **Tokens consumed (v2).** `--ink`, `--rubric`, `--lapis`,
  `--ease-quill`, `--ease-flare`, `--dur-cuff: 600ms`,
  `--margin-band`.

### 6.10 Pilcrow-stamp click

- **What & why.** Clicking a heading stamps a small red pilcrow (¶)
  beside it — the scribe's mark for "here, this paragraph, remember
  this one" — with the press-and-thud of a seal landing. It is the
  reader's one mark-making power in the theme: a personal finding-aid
  they place themselves, answering §6.2's hand with a mark of their
  own. Stamped headings are remembered for the session, and the
  navigation (§6.13) lists them as the reader's own apparatus.
- **Structure.** Headings are `<button class="stampable">`-wrapped or
  carry a real `<button>` affordance in their margin slot (44px
  target, invisible until hover/focus on desktop, always available to
  keyboard). The pilcrow is a `<span class="pilcrow">¶</span>` in
  `--rubric`, positioned in the heading's left margin space, initially
  absent. Stamps persist in `sessionStorage` (per page, per session —
  a reader's marks in a borrowed book are not the library's business
  across sessions).
- **Motion spec.** Stamp: the pilcrow scales 1.3→1 with
  `--ease-stamp`'s hard stop over 160ms, rotating from −8° to its
  resting −2° (a hand-struck mark is never perfectly upright), with a
  60ms ink-bleed: the glyph's text-shadow blooms 0→1px and settles —
  wet ink finding the vellum's tooth. Un-stamp (second click): the
  pilcrow fades in 200ms, no reverse thud — removing a mark is
  quieter than making one.
- **Choreography timeline (v2).** t=0 click → t=0–160ms pilcrow
  presses (scale/rotate) → t=100–160ms bleed blooms and settles →
  t=160ms the navigation's "your marks" count (§6.13) ticks +1 and
  the live region (§6.8) speaks "Marked: [heading]" (polite, once).
  Total 160ms of motion; the mark then rests for the session.
- **State matrix (v2).** *Rest (unstamped):* no pilcrow; the button
  affordance is visually silent on desktop until hover/focus, and
  fully described to AT at all times. *Hover:* the margin slot shows
  a ghost pilcrow at 25% rubric — the mark you *would* make.
  *Focus:* ghost at 50% + lapis focus ring on the button. *Active:*
  the stamp fires (above). *Scrolled-past:* stamped headings keep
  their pilcrows — they are the reader's trail through the text.
  *Disabled:* JS off — no stamping exists; headings are headings.
  The feature degrades to nothing, and nothing depends on it.
  *Touch:* tap on the heading's margin slot stamps; the ghost state
  does not exist on touch, so the slot carries a permanent 18%
  ghost — touch readers are told the power exists.
- **Content merge.** The mark lands in the heading's own margin and
  refers to that heading's section; the navigation's mark list is
  built from the real headings stamped. It is a bookmarking system
  wearing its historical original.
- **Failure fallback.** If storage is unavailable, stamps last for
  the page view only (in-memory set) — the interaction still works;
  persistence is the enhancement. If the stamp animation is
  interrupted, the pilcrow's resting state is its markup state, so
  it can never be left mid-scale.
- **Reduced-motion variant.** The pilcrow appears instantly at its
  resting rotation, no bleed. The announcement is unchanged.
- **Breakpoints (v2).** ≥1200px / 768–1199px: as specced. <768px: the
  margin slot moves above the heading (inline-start of the heading
  line) since the gutter cannot hold it; target stays 44px.
- **Edge cases & failure modes (v2).** *Stamping the h1:* allowed —
  the founding heading takes a mark like any other; §6.1's painting
  is unaffected (the pilcrow lives in the margin slot, outside the
  glyph). *Many stamps:* no cap; a reader who marks everything has
  marked nothing, but that is their editorial judgement, not the
  theme's to police. The nav list (§6.13) scrolls. *Shared devices:*
  sessionStorage scope is the honest limit and §12's copy says so
  ("your marks last while you read").
- **Accessibility spec (v2).** The button's accessible name is
  "Mark this section: [heading]" / "Remove your mark from
  [heading]"; `aria-pressed` carries the state. The pilcrow glyph
  itself is `aria-hidden` (its fact is the button's state). Focus
  ring: 2px `--lapis`, offset 3px. Target 44×44px at all breakpoints.
  The stamp is fully keyboard-operable — a mouse-only mark would
  fail the theme's own guide logic (§6.3's focus parity).
- **Performance budget & mobile variant.** One 160ms transform on
  click; a sessionStorage write. Negligible. Mobile: the repositioned
  slot above.
- **Tokens consumed (v2).** `--rubric`, `--lapis`, `--ease-stamp`,
  `--dur-stamp: 160ms`, `--stamp-rot: -2deg`.

### 6.11 Arched miniature reveals

- **What & why.** Each chapter's miniature — its painted plate —
  reveals the way a reader finds it on the leaf: through its arch.
  The miniature sits in a pricked margin frame; as it enters, an
  arched clip-path opens upward from the frame's base, the image
  scaling gently in-frame as the arch completes, and the caption
  below names what it shows. The arch is not a style: it is the
  shape of the window cut into the manuscript's page for its picture.
- **Structure.** A `<figure class="miniature">` in the outer margin
  (≥1200px) or breaking the column at a paragraph boundary (smaller
  widths): an arched container (`border-radius: 50% 50% 0 0 / 38%
  38% 0 0` refined by clip-path for the true Gothic point at
  ≥1200px — a trefoil arch is authored per template), the image
  duotone-mapped per §5, and a `<figcaption>` in italic `--ink-soft`.
  A thin `--gold` keyline (1px, 60%) traces the arch — the burnished
  edge of the miniature's window.
- **Motion spec.** Reveal at 30% visibility: clip-path inset animates
  from `inset(100% 0 0 0)` following the arch curve (implemented as a
  two-keyframe path morph on the clip polygon) over 700ms
  `--ease-leaf`; simultaneously the image scales 1.04→1 over 900ms
  `--ease-flare` (it settles *into* its frame as the window opens).
  The gold keyline draws around the arch in 500ms `--ease-quill`
  starting at t=200ms. Caption fades in last, 200ms at t=600ms.
- **Choreography timeline (v2).** t=0 figure crosses 30% → t=0–700ms
  arch opens upward → t=0–900ms image scales in-frame → t=200–700ms
  keyline draws → t=600–800ms caption fades → t=900ms figure at rest,
  all clips removed (final state is unclipped markup).
- **State matrix (v2).** *Rest:* revealed, static. *Hover:* the
  medallion tilt — the whole figure tilts ≤4° toward the pointer's
  side (rotateX/rotateY from pointer position, 200ms `--ease-swivel`
  to engage, 300ms to release) *like a leaf angled to the light*;
  the gold keyline brightens to 100% during the tilt. *Focus:* (the
  figure is focusable only when it is a link to the full plate,
  §6.15) tilt applies at 2° instantly + lapis ring. *Active:* press
  settles the tilt to 0° over 100ms — the leaf laid flat to be
  carried away (navigation follows). *Scrolled-past:* static; the
  arch never re-opens within a page view. *Disabled:* JS off — the
  figure is fully visible in markup (clips are JS-applied); images
  lazy-load natively.
- **Content merge.** The miniature illustrates the chapter it sits
  beside; its caption names the scene and the leaf. The arch is its
  frame *in* the page, not a card laid on it.
- **Failure fallback.** Clips and scales are JS-applied enhancements;
  any failure leaves a visible, framed miniature. A failed *image*
  shows the arch with its `--vellum-deep` ground and the caption
  gains the line "the miniature is wanting" — the manuscript's own
  phrase for a plate never painted, and an honest one (§12).
- **Reduced-motion variant.** No arch opening, no scale, no tilt: the
  miniature is present, keyline drawn, caption set.
- **Breakpoints (v2).** ≥1200px: outer-margin figure, pointed arch.
  768–1199px: the figure breaks the column full-measure at a
  paragraph boundary; arch becomes a round arch (the pointed clip is
  illegible at column width). <768px: full-bleed within the leaf's
  padding, round arch, tilt cut (touch), keyline static.
- **Edge cases & failure modes (v2).** *Slow network:* the arch does
  not open onto an unloaded image — reveal waits for the image's
  `load` or 1200ms, whichever first; at 1200ms it opens onto the
  alt-text plate (vellum-deep ground + the alt set as a caption
  line) and the image fades in when it arrives. An arch opening on
  emptiness is a §9 slop mode. *Very tall miniatures:* aspect is
  capped at 3:4 (arch geometry assumes it); taller source art is
  cropped by the frame, and the full plate lives at §6.15's detail
  view. *Chapter without a miniature:* lawful (§4 density) — the
  margin holds apparatus instead; no empty arch is ever rendered.
- **Accessibility spec (v2).** The image carries real alt text
  describing the scene ("The binder's workshop: a press, two
  apprentices, a quire under weights") — never "miniature" or the
  file name. The caption is the figure's accessible description via
  `aria-describedby` where the figure is a link. Tilt is decorative
  and disabled for `prefers-reduced-motion` and for keyboard focus
  beyond the instant 2°. Contrast: caption `--ink-soft` on
  `--vellum` ≈5.9:1 at 16px italic — caption tier, lawful; the
  keyline is decorative.
- **Performance budget & mobile variant.** One clip-path animation +
  one transform per reveal, ≤0.3ms/frame during 900ms; images are
  `loading="lazy"` below the first chapter. Mobile: the simplified
  arch above.
- **Tokens consumed (v2).** `--gold`, `--lapis`, `--ink-soft`,
  `--vellum-deep`, `--ease-leaf`, `--ease-flare`, `--ease-quill`,
  `--dur-arch: 700ms`.

### 6.12 Skeleton leaves + full-curl transition

- **What & why.** Loading and navigation are states of the manuscript,
  not interruptions of it. While a page loads, the visitor sees a
  skeleton leaf: pricked margins, the ruling lines, grey ghost text
  where the writing will be — a leaf prepared by the rubricator but
  not yet written on. As content arrives, the leaf *rubricates in*:
  headings flare red, then ink fills the text lines. Moving to
  another page is a full page-curl wipe: the whole leaf bends across
  to the next quire.
- **Structure.** Skeleton: a `<div class="leaf-skeleton" aria-hidden>`
  mirroring the target layout — pricking columns (§4), a rubric
  heading bar, and text-line bars in `--vellum-deep` at the body's
  exact line-height rhythm. Transition: §6.4's curl machinery at
  whole-page scale — an overlay leaf (surface + underside) hinged at
  the spine edge, driven by a 600ms timed animation (not scrubbed:
  navigation is an act, not a read).
- **Motion spec.** Rubrication-in: when real content swaps in, the
  skeleton's heading bar flares to `--rubric` (200ms), text bars fill
  to `--ink` at 85% (staggered 30ms per line, 250ms total), then the
  skeleton crossfades to the real leaf over 200ms — total ≤650ms
  from content-ready. Curl transition: the leaf bends across in
  600ms `--ease-leaf` (corner lift 0–200ms, apex crossing at
  ≈350ms, settle by 600ms), the new page revealed beneath from the
  midpoint, fully interactive at 600ms.
- **Choreography timeline (v2).** *Load:* t=0 skeleton leaf shown
  (only if content is not ready within 150ms — a fast load never
  shows a skeleton) → content ready → t=0–200ms rubric flare →
  t=50–300ms ink fill stagger → t=300–500ms crossfade to real leaf →
  §6.1's painting begins at t=500ms if this is a hero page.
  *Navigation:* t=0 click → t=0–600ms curl across (new page loads
  beneath from t=200ms) → t=600ms new leaf at rest, its own
  apparatus seated (§6.8's anchor rule: no replays).
- **State matrix (v2).** *Rest:* real leaf, no overlay. *Hover/focus:*
  links behave normally during rest; during the 600ms transition,
  pointer events are held by the overlay (it is a turning leaf) but
  focus is never moved or trapped — keyboard focus lands on the new
  page's first heading at completion, per standard SPA practice.
  *Active:* the click that starts the transition. *Scrolled-past:*
  n/a. *Disabled:* JS off — no skeleton (content renders
  server-side), no curl (links navigate plainly). *Touch:* the curl
  transition is identical; swipe gestures are the browser's, never
  hijacked.
- **Content merge.** The skeleton is the target page's own layout in
  its unwritten state; the curl turns the actual leaf the reader was
  reading. Neither state introduces a foreign visual system (no
  spinners, no progress bars — §5's refusal holds even here).
- **Failure fallback.** If content takes >4s, the skeleton gains one
  line of honest apparatus text — "the leaf is still being copied" —
  and a plain link to retry; it never spins forever. If the curl
  animation fails mid-transition, the watchdog (§6.4's 1s flatten)
  completes the navigation instantly: arriving is non-negotiable,
  bending is optional.
- **Reduced-motion variant.** No skeleton choreography (content
  simply appears, with the rubric flare only if the wait exceeded
  1s), and the transition becomes a 200ms crossfade.
- **Breakpoints (v2).** All breakpoints: skeleton mirrors the local
  layout (margin band collapses per §6.2's rules). <768px: the curl
  transition becomes the §6.4 mobile lift at page scale (translate +
  fade, 350ms) — a phone leaf lifts; it does not bend.
- **Edge cases & failure modes (v2).** *Slow connection (effective
  type 2G/3G or `save-data`):* transitions are crossfades (200ms)
  and skeletons appear only after 400ms — the theme spends no
  theatre on a reader who is paying for bytes. *Back/forward
  navigation:* no curl (the browser's own gesture owns history);
  apparatus re-seats instantly. *Prefetched page:* if the target is
  already loaded, the curl still plays its 600ms — the turn is the
  theme's punctuation — unless the reader has reduced motion or has
  turned twice in 5s, in which case the third turn is a crossfade
  (the scribe does not perform for its own sake).
- **Accessibility spec (v2).** The skeleton is `aria-hidden` and the
  real content, when swapped, is announced by the route change's
  standard heading focus — no live-region chatter about loading.
  During the transition the overlay is `aria-hidden`; the new page
  is in the accessibility tree from t=200ms (beneath the bend) so
  AT users are never locked out by a visual effect. Reduced-motion
  and vestibular safety: the curl is the theme's largest motion and
  is the first thing the reduced variant removes (§14).
- **Performance budget & mobile variant.** Skeleton: static bars, one
  staggered fill — negligible. Curl: §6.4's machinery at page scale,
  ≤1.0ms/frame for 600ms, and only on navigation. Mobile: the lift.
- **Tokens consumed (v2).** `--vellum`, `--vellum-deep`, `--rubric`,
  `--ink`, `--ease-leaf`, `--dur-curl-page: 600ms`,
  `--dur-rubricate: 650ms`.

---

### 6.13 Quire navigation (page family: navigation)

- **What & why.** The site's navigation is the manuscript's table of
  gatherings: a contents leaf listing each quire (section) with its
  folio range and its catchword, ruled like a medieval *tabula*. It
  sits at the head of the first leaf and is reachable from a slim
  running head on every page. A reader navigates this site the way a
  fifteenth-century reader navigated a codex: by gatherings, folios
  and first words — and by their own pilcrow marks (§6.10), which the
  tabula collects.
- **Structure.** A `<nav class="tabula">`: a table-like list, one row
  per quire — quire signature (roman, `--ink-soft`), title (Fell,
  ink, a real link), folio range (apparatus), catchword (small caps,
  right). The current quire's row is rubricated at its signature only
  — the scribe marked where the book is open. A second block, "Your
  marks", lists the reader's stamped headings (§6.10) as links, or
  the honest empty line (§12). The running head on later pages is one
  line: site title (left), current quire (centre, apparatus), a
  "Tabula" link (right).
- **Motion spec.** The tabula is nearly still, by design: rows take
  §6.10's ghost-pilcrow logic in reverse — hovering a row draws a 1px
  lapis rule under its title (200ms `--ease-quill`). Opening the
  tabula from the running head on mobile is a leaf-lift (§6.12's
  mobile motion, 300ms), never a slide-in drawer — drawers are
  furniture this house does not own. The "Your marks" count ticks
  (§6.8's 200ms crossfade) when a stamp lands.
- **Choreography timeline (v2).** Page load: tabula present, current
  row marked — no entrance animation (a contents leaf does not
  perform). Stamp lands (§6.10) → t=160ms the marks count ticks →
  the stamped heading's row in "Your marks" fades in (200ms) if the
  tabula is on screen; if not, it is simply there when opened.
- **State matrix (v2).** *Rest:* current quire marked. *Hover:* lapis
  rule draws under the title. *Focus:* ring (§6.5 pattern) + rule
  drawn instantly. *Active:* §6.12's transition (or its fallbacks).
  *Scrolled-past:* the running head persists (it is `position:
  sticky` within the leaf head, and retires at the colophon —
  apparatus does not follow the reader into the colophon, §6.17).
  *Disabled:* JS off — the tabula is a list of links; complete.
  *Touch:* rows are 48px; no hover rule; the current-quire mark
  carries the state.
- **Content merge.** The tabula's rows are the site's real sections
  with their real folios and catchwords — generated by the same
  build step as §6.5/§6.8, so the three can never disagree.
- **Failure fallback.** Static list (above). A section missing from
  the tabula is a §10 gate failure, caught at build.
- **Reduced-motion variant.** Rules and ticks apply instantly; the
  mobile tabula opens without the lift.
- **Breakpoints (v2).** ≥1200px: full tabula on the opening leaf;
  running head thereafter. 768–1199px: folio ranges drop (signature,
  title, catchword remain). <768px: the tabula is a full-leaf overlay
  reached from the running head; rows stack signature above title.
- **Edge cases & failure modes (v2).** *Many quires (>12):* the
  tabula paginates by volume — group rows under volume heads (Part
  the First, Part the Second) rather than shrinking type; a codex
  with forty gatherings has volumes, and so does its site.
  *Reader's marks list long:* it scrolls within its block at 6
  entries, with the count always visible. *A section renamed:* the
  tabula, catchword chain and apparatus regenerate together (one
  build source, §6.8) — a stale title in any one is a build bug,
  not an editorial choice.
- **Accessibility spec (v2).** A real `<nav>` with a list; the
  current quire carries `aria-current="page"` (or `"location"` on
  single-page builds). Rows are links with full titles as their
  names — the signature and catchword are presentational within the
  link, not substitutes for its name. Focus order: running head →
  tabula rows → marks. All targets ≥44px.
- **Performance budget & mobile variant.** Static markup + one rule
  transition. Negligible. Mobile: the overlay form above.
- **Tokens consumed (v2).** `--ink`, `--ink-soft`, `--rubric`,
  `--lapis`, `--ease-quill`, `--dur-rule: 200ms`.

### 6.14 Opening-leaf hero composition (page family: hero)

- **What & why.** The hero is the manuscript's opening leaf, composed
  as openings were composed: the painted initial and its headline
  (§6.1) high on the leaf, a lead paragraph in larger Garamond, one
  miniature (§6.11) in the outer margin if the opening chapter has
  one, the manicule already at its post, and — at the foot — the
  first catchword (§6.5) promising the next gathering. Nothing else
  is on the leaf. A hero that needs a sub-headline, three bullets and
  a badge row is a landing page wearing a costume (§9, rule 3).
- **Structure.** A `<header class="opening">` in the §4 grid: h1 with
  §6.1's initial, lead paragraph (21px, §3), optional figure (§6.11),
  and one — at most one — action, set as a rubricated line of text
  with a lapis rule (§6.16's button treatment is reserved for forms;
  the opening's action is a *reading* action: "Begin the first
  quire", a link styled as the scribe's own direction to the reader).
  The leaf-foot (§6.5) closes the composition.
- **Motion spec.** The hero's motion is exactly §6.1's painting +
  §6.2's first travel + the action line's rule drawing (300ms
  `--ease-quill` at t=1400ms, as the painting completes). No other
  element animates. The composition is still by the time a landing
  page would still be staggering its third card in.
- **Choreography timeline (v2).** §6.1's timeline governs t=0–1600ms
  → t=1400–1700ms action rule draws → t=1600ms manicule's first glide
  (§6.2) → hero at rest. Total theatre: 1.7s, once.
- **State matrix (v2).** *Rest:* the composed leaf. *Hover:* the
  action line's rule thickens to 2px lapis; the miniature tilts if
  present (§6.11). *Focus:* ring on the action link. *Active:*
  §6.12's transition into the first quire. *Scrolled-past:* the
  opening scrolls away whole; nothing pins (the pin budget belongs
  to chapter initials, §6.6). *Disabled:* the leaf renders composed
  and static — it loses nothing but the painting's sequence.
  *Touch:* identical, minus tilts.
- **Content merge.** Every element of the composition is one of the
  theme's working devices doing its job on the site's real opening
  content. There is no hero-specific decoration.
- **Failure fallback.** §6.1's watchdog governs the painting; the
  rest of the leaf is static markup.
- **Reduced-motion variant.** The composed leaf, painted, still.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: miniature
  moves below the lead paragraph (column break, §6.11). <768px:
  initial at 34px (§6.1), lead at 19px, miniature (if any) after the
  action line; the catchword foot remains — the promise survives
  every viewport.
- **Edge cases & failure modes (v2).** *Site with no chapters yet*
  (a single forthcoming book): the opening's catchword is the first
  word of the announcement leaf that follows — the chain (§6.5)
  always has a next word, even if the next thing is a colophon.
  *Headline too long for the display size:* §6.1's 40-letter cap;
  beyond that, the opening takes a shorter display title and the
  full title moves to the tabula (§6.13) — composed leaves are not
  stretched.
- **Accessibility spec (v2).** Landmark order: running head → h1 →
  lead → action → foot. The h1 is the page's single h1. The action
  link's name is its full direction ("Begin the first quire: The
  Binding"), not "Begin". Contrast throughout per §2/§3.
- **Performance budget & mobile variant.** §6.1's budget + static
  layout; the hero's LCP element is the headline text (a font, not
  an image) — the theme's openings are fast because manuscripts are
  mostly type. Mobile: the stacked composition above.
- **Tokens consumed (v2).** `--ease-quill`, `--lapis`, `--rubric`,
  plus §6.1/§6.5's tokens by reference.

### 6.15 Miniature plate cards (page family: cards)

- **What & why.** Where the site lists its works — a publisher's
  titles, a binder's portfolio, a game's bestiary — each entry is a
  plate: the work's miniature (§6.11's arch, at card scale) above its
  title in Fell, one line of description in Garamond, and its
  apparatus (folio, format, price or date) in the apparatus hand.
  The grid of plates is a *gallery leaf*: plates hung in the quire's
  grid, each in its pricked frame, none floating on shadow.
- **Structure.** A `<ul class="plates">` of `<li><article
  class="plate">` — arch figure (§6.11, simplified keyline), h3
  title (Fell 24px, a link to the detail leaf), one-line description
  (17px, ≤90 characters — a plate caption, not a paragraph), and an
  apparatus row (folio · format · price/date). The whole plate is
  not a link; the title is — card-wide click targets are a screen
  habit that makes every mis-tap a navigation.
- **Motion spec.** Plates reveal with §6.11's arch at 60ms stagger
  per plate within a row (the illuminator's bench works left to
  right), capped at 4 staggered per viewport entry — beyond that,
  plates arrive revealed. Hover: the medallion tilt (§6.11, ≤3° at
  card scale) on the figure only; the title takes a lapis rule
  (§6.13's draw). No lift, no shadow growth: plates are *in* the
  leaf.
- **Choreography timeline (v2).** Row enters → t=0 plate 1 arch
  opens (700ms, §6.11) → t=60/120/180ms plates 2–4 begin → all
  settled by t≈1000ms → captions fade with their figures (§6.11's
  t=600ms offset per plate).
- **State matrix (v2).** *Rest:* revealed plate. *Hover:* figure
  tilt + title rule. *Focus:* title link ring; figure tilt at 2°
  instant. *Active:* §6.12 transition to the detail leaf.
  *Scrolled-past:* static. *Disabled:* all plates visible, arches
  open (markup state). *Sold out / out of print:* the plate's
  apparatus row gains the rubric line "the edition is exhausted"
  (§12's voice) and the miniature desaturates to its lapis duotone
  at 60% — stated in the apparatus, never as a diagonal banner.
  *Touch:* no tilt; tap = title link.
- **Content merge.** A plate *is* the work's catalogue entry — its
  miniature is the work's own image, its apparatus the work's real
  folio in the site's order. The gallery leaf is the listing page,
  not a decoration of it.
- **Failure fallback.** §6.11's image fallback applies per plate
  ("the miniature is wanting"). Layout never depends on the reveal.
- **Reduced-motion variant.** Plates present, arches open, no
  stagger, no tilt.
- **Breakpoints (v2).** ≥1200px: 3 plates per row in the full grid
  (columns 3–11), outer-margin column retired (the gallery uses the
  leaf's whole width — a gallery leaf is a different gathering, and
  §4's reading grid yields to it deliberately). 768–1199px: 2 per
  row. <768px: 1 per row, arch round (§6.11), apparatus stacks.
- **Edge cases & failure modes (v2).** *Long titles:* two lines
  maximum, then the title is shortened editorially — plates align by
  their arch tops, and a ragged gallery is a §9 tell; equal visual
  weight is achieved by the frame, not by forcing equal text.
  *Missing miniature:* the arch holds the work's initial (§6.6's
  technique, unpainted gold ground + letter) — a plate without a
  painting is still a plate. *Filtering/sorting:* plates re-lay
  instantly (no FLIP theatre); the apparatus row of each plate
  states its folio in the *current* order, regenerated per §6.8's
  rule.
- **Accessibility spec (v2).** List semantics preserved; each
  plate's title link names the work fully. The figure's alt follows
  §6.11. The exhausted-edition state is text in the apparatus, not
  colour alone. Focus order follows DOM order, row by row.
- **Performance budget & mobile variant.** Reveal cost = §6.11's,
  amortised by the 4-plate stagger cap; images lazy-loaded.
  Mobile: the single column above.
- **Tokens consumed (v2).** `--gold`, `--lapis`, `--rubric`,
  `--ink-soft`, `--ease-flare`, `--dur-arch: 700ms`,
  `--stagger-plate: 60ms`.

### 6.16 The commissioning slip (page family: forms / conversion)

- **What & why.** The theme's conversion act is a commission: the
  reader writes to the scribe. The form is a commissioning slip — a
  single leaf on which the patron states what they want made (a
  book, a binding, an illumination, a place on the course) and where
  to send word back. Fields are ruled lines on the slip, in the
  manuscript's own hand-spacing; the submit is not a button but the
  slip's rubricated direction: *Send this to the scriptorium.* The
  confirmation is a colophon (§6.17's voice) written for this patron:
  what was asked, when it was received, what happens next — dated
  and numbered like an entry in the workshop's day-book.
- **Structure.** A `<form class="slip">` in a pricked frame (§4):
  fields as label + ruled-line input (transparent ground, 1px
  `--ink-soft` bottom rule at rest, the visitor's entry in EB
  Garamond 19px on the line). Required fields carry a rubric
  pilcrow (¶) after the label — the scribe's own mark for "this
  line must be filled". The commission choices (what is being
  commissioned) are a radio group styled as a short tabula
  (§6.13's rows, selectable). The submit is a full-width rubricated
  text block with a lapis rule — the form's one filled element is
  reserved for its confirmation state, not its button (§2, law 2:
  lapis is spent once).
- **Motion spec.** Focus: the field's ruled line draws to full
  `--ink` (200ms `--ease-quill`) and a small manicule — the form's
  own, 22px, distinct from the margin guide — fades in beside the
  label pointing at the line: the scribe attends to where you are
  writing. (This is the one place a second hand appears; it is a
  *different* hand — no cuff, no gold — a clerk's pointer, and §9
  guards the distinction.) Error: the line turns lapis (never
  rubric — §2 law 3) and the error note appears in the margin in
  italic Garamond, written as an instruction (§12). Submit: the
  whole slip takes a 1px-deep impression (scale 0.995, 120ms
  `--ease-stamp`) — the slip pressed into the day-book — then the
  confirmation colophon replaces it (300ms crossfade).
- **Choreography timeline (v2).** Focus → t=0–200ms line draws,
  clerk's pointer fades t=100–250ms → blur: line settles to 60% ink
  (a filled line is darker than an untouched one) → error (on
  submit/blur per field rules): t=0 line to lapis (150ms), margin
  note fades t=100–300ms → submit valid → t=0–120ms impression →
  t=120–420ms crossfade to confirmation → confirmation's entry
  number counts in apparatus style (§6.8's tick).
- **State matrix (v2).** *Rest:* lines at 30% ink, labels ink.
  *Hover:* line at 50% (the slip senses the pen near). *Focus:* as
  specced; focus ring is the drawn line at full ink + a 2px lapis
  outline on the field's line box (visible against vellum, 7.53:1).
  *Active:* submit impression. *Disabled (submitting):* fields
  readonly, the direction line reads "It is being copied…" — the
  slip never shows a spinner (§5's refusal extends to forms).
  *Error:* per-field lapis state, persistent until corrected
  (errors on a written slip do not time out). *Success:* the
  confirmation colophon, permanent for the page view. *Touch:*
  identical; inputs at 19px prevent iOS zoom; the clerk's pointer
  appears on focus as on desktop.
- **Content merge.** The slip is the workshop's actual order paper:
  its fields are the commission's real terms (work, materials,
  inscription text, delivery), its confirmation the real day-book
  entry with a real reference number from the site's own sequence.
- **Failure fallback.** A plain HTML form: labels, inputs, a submit
  button, server validation re-rendering the same margin notes as
  text beside the fields. Every enhancement is CSS/JS over that
  form. No-JS patrons lose the theatre and keep the transaction —
  and the confirmation page is a real page, not a JS state.
- **Reduced-motion variant.** Line states apply instantly; no
  impression; the confirmation appears without crossfade.
- **Breakpoints (v2).** ≥1200px: slip at 62ch in the reading column,
  margin notes in the outer margin. 768–1199px: same, notes move
  under their fields (the outer margin is spoken for). <768px: slip
  full-measure; the pricked frame becomes top/bottom rules only (a
  slip torn to width); margin notes under fields; radio tabula rows
  stack.
- **Edge cases & failure modes (v2).** *Long inscription text* (the
  patron's requested wording): the field is a ruled textarea whose
  lines multiply — ruled every 30.8px (`--leading`) so writing stays
  on the ruling; beyond 6 lines it scrolls *within* its ruling,
  which the margin note explains (§12). *Paste from elsewhere:*
  pasted text takes the field's type instantly; no typewriter
  theatre on paste, ever. *Validation on submit with three errors:*
  notes appear per field, focus moves to the first error, and the
  slip's head gains one line — "Three lines want mending" — in the
  editor's voice (§12), because a patron should be told the count
  before the details.
- **Accessibility spec (v2).** Every field has a real `<label>`;
  errors are linked via `aria-describedby` and announced by an
  `aria-live="polite"` summary ("Three lines want mending: the
  date, the direction, the inscription"). The clerk's pointer is
  `aria-hidden`. The radio tabula uses native radios with visible
  focus on the row. Contrast: entries `--ink` on `--vellum`
  11.04:1; error text `--lapis` 7.53:1 — errors are the one place
  lapis carries prose, by §2's reservation. Targets ≥44px.
- **Performance budget & mobile variant.** Transitions on focus and
  error only; no loops. Negligible. Mobile: the torn-slip form
  above.
- **Tokens consumed (v2).** `--ink`, `--ink-soft`, `--rubric`,
  `--lapis`, `--ease-quill`, `--ease-stamp`, `--leading`,
  `--dur-line: 200ms`.

### 6.17 Colophon footer (page family: footer)

- **What & why.** A manuscript ends by telling the truth about
  itself: who copied it, where, in what year, and that it is
  finished. The footer is that colophon — *Here ends the [work].
  Copied by the scriptorium of [site], in the year [year]. The
  reader's marks (§6.10) are their own; the rest is the book's.* —
  followed by the final catchword line: the word *Explicit*, the
  traditional last word of a manuscript, set where §6.5's chain
  promised it would be. Plus the site's legal line and two or three
  plain links, in apparatus type. Nothing in the colophon sells.
- **Structure.** A `<footer class="colophon">`: a centred apparatus
  column — line 1, the colophon proper (three short lines, Fell for
  the first); line 2, the reader's summary ("Your marks: iij" or
  the honest none, §12); line 3, legal + links (Imprint, Terms,
  Write to the scriptorium) with §6.13's lapis rule hover; the gilt
  edge (§4) closes beneath. The manicule does not appear in the
  colophon — the guide's work is done; §6.2 rests it at the last
  catchword above.
- **Motion spec.** The colophon is the stillest element on the page:
  it takes §5's heading flare only if it carries a heading (it
  usually does not). The reader's-marks count is live text, ticking
  per §6.8 if a stamp lands while the colophon is in view. That is
  all. The end of the book is quiet on purpose.
- **Choreography timeline (v2).** None of its own; it inherits
  §6.8's tick timing when the count changes (t=60–350ms pattern).
- **State matrix (v2).** *Rest:* the colophon. *Hover/focus:* link
  rules and rings per §6.13. *Active:* plain navigation (no curl —
  §6.12's transition is for quires; the colophon's links to legal
  leaves crossfade, 200ms). *Scrolled-past:* n/a — it is the end.
  *Disabled:* static text; complete. *Touch:* links at 44px.
- **Content merge.** The colophon's facts are the site's real facts:
  the year is the real year (computed, not typed — a colophon that
  says last year is a §10 truth failure), the named maker is the
  real publisher, the marks count is the reader's real count.
- **Failure fallback.** Static markup. There is nothing to fall back
  from.
- **Reduced-motion variant.** Identical (the element is already
  still).
- **Breakpoints (v2).** All: the centred apparatus column holds;
  <768px the legal links stack at 44px targets.
- **Edge cases & failure modes (v2).** *Colophon on the 404 leaf
  (§6.18):* it appears there too, unmodified — a book's colophon
  does not panic because a leaf is missing. *Year boundary:* the
  computed year handles it; a build that hard-codes the year fails
  §10's truth audit at the next New Year, silently, which is why
  the rule exists.
- **Accessibility spec (v2).** A real `<footer>` (contentinfo);
  links fully named; the marks summary is text, not a badge.
  Contrast: apparatus on vellum per §2 (ink-soft ≈5.9:1 for the
  summary tier; the colophon's first line is `--ink` at Fell 19px).
- **Performance budget & mobile variant.** Zero motion cost.
  Mobile: stacked links.
- **Tokens consumed (v2).** `--ink`, `--ink-soft`, `--gold`,
  `--lapis`, `--ease-quill`.

### 6.18 The unfinished leaf (page family: 404)

- **What & why.** The 404 page is a leaf the scribe never finished:
  the prickings are ruled, the rubricated heading begun — "Here
  should follow…" — and the text block is empty vellum, because in
  real manuscripts gatherings went missing and everyone who has used
  an old book has met the gap. On the empty leaf, one thing is
  present: the manicule, resting in the margin, pointing at the
  place where the text should be — and beneath, the honest
  apparatus: what the reader sought (the URL, in apparatus type),
  and the three likeliest gatherings it might belong to, as
  §6.13-style rows. The theme's error page does not joke about the
  loss; it catalogues it.
- **Structure.** A normal leaf (§4 grid) with: rubricated heading
  ("Here should follow the leaf you sought"), the sought direction
  in apparatus type, an empty ruled text block (prickings + three
  faint ruling lines, no ghost text — the leaf is *unwritten*, not
  redacted), the resting manicule (§6.2's markup, static), three
  suggested-gathering rows, and a line to the tabula (§6.13). The
  colophon (§6.17) closes the leaf as usual.
- **Motion spec.** Nearly none: on load, the rubric heading flares
  once (§5's flare, 500ms) and the manicule makes one slow swivel
  from the heading to the empty block (600ms `--ease-swivel`) — the
  guide showing the reader the gap. Then stillness. No curl, no
  painting, no glint loop (the gold on this leaf does not perform).
- **Choreography timeline (v2).** t=0 leaf renders → t=200–700ms
  heading flares → t=500–1100ms the hand swivels to the empty block
  → rest.
- **State matrix (v2).** *Rest:* as specced. *Hover/focus:* the
  suggestion rows take §6.13's states. *Active:* plain navigation
  (crossfade). *Scrolled-past:* n/a (the leaf is one viewport by
  design; if content forces a scroll, the hand stays with the empty
  block). *Disabled:* fully static; the swivel is JS-applied.
  *Touch:* identical.
- **Content merge.** The suggestions are the site's real nearest
  gatherings (by URL structure or search index, computed by the
  server/CMS — never three generic "popular pages" unless they are
  genuinely the likeliest, and §12's copy says which they are).
- **Failure fallback.** If suggestion computation is unavailable,
  the leaf shows the tabula line alone — an honest shorter page.
- **Reduced-motion variant.** No flare, no swivel: the hand rests by
  the empty block from first paint.
- **Breakpoints (v2).** ≥1200px: full composition. 768–1199px:
  empty block narrows with the column. <768px: the hand moves above
  the empty block (the gutter rule, §6.2) pointing down at it.
- **Edge cases & failure modes (v2).** *The sought URL is offensive
  or absurd* (crawlers probe strange strings): the apparatus line
  truncates at 80 characters with an ellipsis — the catalogue does
  not amplify. *Repeated 404s in a session:* the leaf is the same
  leaf; no escalation, no humour counter. *Soft 404 discipline:*
  the page returns a real 404 status — a pretty leaf does not
  excuse a wrong status code (§10).
- **Accessibility spec (v2).** The heading is the page's h1 and
  states the situation plainly; the sought direction is text; the
  hand is `aria-hidden` (its fact — "the text is missing here" —
  is the heading's). Focus lands on the h1 via the route's standard
  practice. Contrast per §2 throughout.
- **Performance budget & mobile variant.** One flare + one swivel
  on load; nothing else. The cheapest page on the site, as an
  error page should be.
- **Tokens consumed (v2).** `--rubric`, `--ink-soft`,
  `--vellum-deep`, `--ease-flare`, `--ease-swivel`.

---

## 7. Page application map

**Home — the opening gathering.** §6.14's opening leaf, then the
site's chapters in quire order, each with its §6.4 turn, §6.6 initial
and §6.5 foot. The tabula (§6.13) follows the opening leaf (a contents
comes after the first opening, as in the books). The home page is the
only page where §6.1's full painting plays; interior pages open with
§6.6's chapter-scale painting.

**Listing — the gallery leaf.** §6.15's plates in the gallery grid.
The manicule does not travel a gallery (there are no paragraphs to
guide); instead the tabula's current-quire mark and the apparatus
carry wayfinding, and §6.8 counts the plates' folios in the order
shown. Filters, where they exist, are tabula rows (§6.16's radio
treatment) above the plates — never a toolbar.

**Detail — a chapter leaf.** One work, read as a chapter: its initial
(§6.6, painted with the work's own scene), its text in the reading
column, its miniature (§6.11) in the outer margin, specifications in
the apparatus hand (folio, format, materials, price — data per §3).
The conversion act, if the detail sells, is a single rubricated line
leading to §6.16's slip with the work pre-named — the detail leaf
itself carries no form. The foot's catchword is the next work's first
word in the listing order: the catalogue reads as a book.

**About — the scriptorium leaf.** The maker's own gathering: written
in the first person plural of the workshop (§12), with a miniature of
the workshop itself (§6.11) and the apparatus recording the founding
year in roman numerals. The manicule's doodle (§9, rule 1) is
permitted on this leaf if it is permitted anywhere — the scribe may
sign his own page.

**Contact / commission — the slip leaf.** §6.16's commissioning slip
as the page's whole content, preceded by one paragraph of direction
(what a commission involves, in §12's voice) and followed by the
colophon. No map, no office photograph in an arch (the workshop's
miniature belongs to About), no chat widget — a scriptorium answers
letters.

**Colophon leaves (legal, imprint, terms).** Plain leaves: apparatus
headings, reading column, no miniatures, no doodles, manicule at
rest beside the first paragraph (§6.2 reduced behaviour even with
full motion enabled — legal text gets a still guide). The theme's
restraint here is a feature a client can be shown.

**The unfinished leaf (404).** §6.18.

---

## 8. Worked examples

### 8.1 The hero — a publisher's opening leaf

*Setting.* A small literary press launches "The Salt Hours", a novel
in nine chapters. The home page opens on the novel's first gathering.

*Build.* The h1 reads "The Salt Hours" — but §6.1 requires the initial
to carry the first chapter's scene, so the display line is the
chapter's opening phrase, set as the hero headline per the theme's
convention for book sites: the *book's* first line is the headline.
The line is "Winter came to the harbour early that year." The initial
W is paintable: inside it, the SVG scene — gold ground, lapis sky
(the harbour water in this site's reading of the layers: sky above,
water below, both lapis at two values), ink hill as the harbour wall
silhouette, and the rubric figure a single small lighthouse keeper.
The tabula (§6.13) sits below the opening leaf with the nine chapters
as quires I–III (three chapters to a quire, §6.8's arithmetic). The
opening's action line reads "Begin the first quire: Winter" and the
leaf-foot's catchword is "Winter" — chapter one's actual first word,
so the promise and the action agree.

*Scroll timeline.* t=0 load: gold ground lays (0–300ms) while the
headline writes on from t=200ms at 28ms/letter, capped well under the
40-letter rule (the line is 44 characters; the cap trims the write-on
to the first 40 and the last four letters arrive with the final
batch). Sky insets 300–700ms, harbour wall 550–900ms, keeper draws
800–1250ms. At t≈1400ms the action line's lapis rule draws (300ms);
at t=1600ms the manicule glides from its markup rest beside the
headline to the lead paragraph. The reader scrolls: the hand tracks
the lead, then chapter one's first paragraphs; at the chapter
boundary the leaf curls over 60vh (§6.4), the underside showing the
catchword "Winter" already read above — the binder's promise, kept
visibly. Chapter one's initial (a painted W of its own, two-layer
at chapter scale) pins at the anchor and stays for the chapter.

*What the visitor feels.* A book opening, not a page loading: gold
first, then colour, then the words — and a hand that stays with
them.

### 8.2 Mid-page — the third chapter, with a miniature and a doodle

*Setting.* The same novel, chapter three ("The Binding of the
Nets"), mid-scroll. This is the quire where §9's one doodle lives.

*Build.* The chapter opens with its painted initial T (§6.6,
two-layer: gold ground + the nets' ink lattice). In the outer margin
at the chapter's second paragraph sits its miniature (§6.11): the
net-mending yard at dusk, duotone lapis/vellum with the one rubric
detail the caption names — "the master's red float, centre". The
apparatus by the chapter head reads *fol. vij · quire II*. Halfway
down the chapter, in the margin beside a paragraph about patience,
is the doodle: a small drawn snail, captioned in italic Garamond —
"the binder's apprentice, on the same paragraph since Michaelmas."
It appears on this chapter only, nowhere else on the site.

*Scroll timeline.* The reader crosses into the chapter: catchword
ticks to "The" (chapter four's first word is already waiting at this
chapter's foot — no: the foot of *this* chapter carries chapter
four's first word; the tick the reader sees at entry is the
*previous* chapter's apparatus settling, §6.8's stagger). The initial
paints over 900ms as it enters; the reader scrolls, it crossfades to
its pinned double at the anchor (200ms) and glints at its slow
offset. The miniature's arch opens at 30% visibility (700ms), image
settling by 900ms, caption at 600–800ms. Passing the doodle's
paragraph, the manicule — for this one paragraph — swivels not to
the paragraph but to the snail (§6.3's override, authored:
`data-attend="doodle"` on that paragraph), holds while the reader
hovers or reads, and returns to duty. It happens once. A reader who
misses it has missed a snail, not a feature.

*What the visitor feels.* Company. The book has a personality that
shows itself once a quire and then gets back to work.

### 8.3 Conversion — commissioning a binding

*Setting.* The press also binds. From a detail leaf for the
"Harbour Binding" (a §6.15 plate: cloth, gilt, £180), the
rubricated line "Commission this binding" leads to the slip leaf.

*Build.* §6.16's slip, pre-named: the commission radio tabula has
"A binding, after the Harbour pattern" already chosen (a real
default from the referring plate, stated on the slip — never a
hidden pre-selection). Fields: the patron's name, their direction
(email, in the theme's word — §12), the inscription they want tooled
on the spine (ruled textarea, 3 lines shown), the date they need it
by. The date field's margin note, authored in advance per §12,
reads: "Bindings want six weeks; if your day is nearer, write it
anyway and we shall tell you truly." The submit line: "Send this to
the scriptorium."

*Scroll/interaction timeline.* The slip leaf has no scroll theatre —
forms are read standing still. Focus on the name field: line draws
to ink (200ms), the clerk's pointer fades in (100–250ms). The patron
enters a date three weeks out and submits: the date field's line
turns lapis (150ms), its margin note fades in (100–300ms) — not an
error of form but of fact, and §12's voice handles it as counsel,
not scolding: the note *is* the six-weeks line above, and the slip's
head adds "One line wants mending." The patron amends (or keeps the
date and adds a note — the field accepts either; the workshop
decides, the slip records). Second submit: impression (120ms),
crossfade (300ms) to the confirmation colophon: "Received, and
entered in the day-book as № 41. We write back within two working
days, in the direction you gave. — The scriptorium." The entry
number ticks in per §6.8.

*What the visitor feels.* They have not filled in a form; they have
left an order on the workshop's spike, and the workshop has written
back.

---

## 9. Anti-slop — what makes THIS theme look cheap

1. **The doodle everywhere.** The snail (§8.2) works because it
   appears once per quire at most — one doodle per site is the
   default ration, and it must sit beside a paragraph it comments
   on. A doodle per section is a sticker pack. *Cure:* the build
   gate counts doodles; >1 per quire fails §10.
2. **The manicule as cursor.** The instant the hand follows the
   mouse as a pointer replacement, the theme has broken its first
   law and the standing rules. *Cure:* the hand answers scroll,
   focus and dwell (§6.2/§6.3) — never raw pointer position. Any
   build where the hand tracks the cursor fails §10 outright.
3. **Hero furniture.** Sub-headlines, badge rows, star ratings,
   logo strips on the opening leaf. *Cure:* §6.14's composition is
   closed — initial, headline, lead, one action, catchword. A
   client request for more is met by moving the content to the
   second leaf, not by furnishing the first.
4. **Gold text and gold buttons.** Gold at 2.35:1 is leaf, not ink
   (§2, law 1). *Cure:* gold exists only inside SVG gold fields and
   the gilt edge. A gold CTA is an automatic §10 failure.
5. **Texture slop.** Vellum grain at visible opacity, coffee stains,
   burnt edges, torn corners. The real leaf is *clean*; age is
   shown by the apparatus, not by distressing. *Cure:* grain breath
   stays in its 0.5–0.9% band (§5); any stain asset in the build
   fails review.
6. **A progress bar.** Or a percentage, or "scroll" chevrons.
   *Cure:* progress is the hand's position and the catchword's
   word (§5). The devices exist; a bar admits they failed.
7. **Chapters too short to turn.** A "chapter" of three lines makes
   the curl (§6.4) a tic. *Cure:* minimum chapter length one
   viewport (§6.4); shorter content is grouped into gatherings
   until it earns a turn.
8. **Fell type for UI chrome.** Buttons, form labels and navigation
   set in IM Fell read as costume. *Cure:* §3's roles are fixed —
   Fell is for the book's voice (headings, titles), Garamond for
   everything the visitor must *operate*.
9. **Latin filler.** Lorem ipsum in a manuscript theme is doubly
   dead: the register exposes it instantly. *Cure:* all copy is the
   site's real copy from the first build (§12); a leaf awaiting
   copy ships with its structure and the apparatus line "the text
   is still being copied" (§6.12's honest phrase), never with
   pseudo-Latin.
10. **The curl as screensaver.** Auto-playing curls, curl on every
    section (not just chapters), curl on hover. *Cure:* curls
    belong to chapter boundaries and route changes only, scrubbed
    or 600ms-timed, never ambient.

---

## 10. Quality gate

A build may not ship in this theme until every **blocking** item
passes and at least 9 of the 11 **standard** items pass. The
reviewer checks evidence — a JS-off load, a reduced-motion load, a
slow-network load, the build's catchword extraction log — not
intentions.

**Blocking — all must pass.**

1. **JS-off test:** with JavaScript disabled, every page shows all
   content in final state: initials painted, vines drawn, catchwords
   correct per section, the form (§6.16) submits, the tabula
   (§6.13) navigates.
2. **Fallback test:** with animation triggers deliberately broken,
   the 1s laws (§6.1, §6.4) fire: no headline is left unstruck by
   its painting half-done, no curl is left bent, no content is
   masked by any overlay at any scroll position.
3. **Reduced-motion test:** with `prefers-reduced-motion` set: no
   travel, no curl, no glint, no painting sequence; the manicule
   rests by the current heading; all information — folios,
   catchwords, marks — is present and correct.
4. **Truth audit:** every catchword equals its next section's real
   first word (checked against the extraction log); every folio
   and quire number equals the document's real counts; the
   colophon's year is the current year; every miniature illustrates
   the chapter its caption claims. One invented or stale figure
   fails the build.
5. **Guide audit:** the manicule never tracks raw pointer position;
   it points at a real paragraph, heading or authored doodle at all
   times; with keyboard navigation alone, the hand follows focus
   (§6.2).
6. **Gold audit:** no text, control or essential indicator is set
   in `--gold` or `--gold-pale` anywhere, including hover states
   and the night palette.
7. **Cursor & cover audit:** the system cursor is unchanged
   everywhere; no animated element overlaps text at any scroll
   depth (checked at 5 depths on a chapter leaf and the gallery
   leaf).
8. **Doodle ration:** ≤1 doodle per quire, each authored beside the
   paragraph it comments on, each with `data-attend` behaviour per
   §8.2 or none.

**Standard — at least 9 of 11.**

9. Headline painting completes ≤1.6s after first paint (≥1200px);
   no headline ever paints in a fallback font and then re-paints.
10. One shared rAF loop drives hand, curls, parallax and glint;
    full-page scroll holds 60fps on a mid-range Android (no frame
    >20ms attributable to theme code outside a turn zone; ≤1.0ms
    loop cost inside one).
11. The curl is a pure function of scroll position: scrubbing back
    and forth across a boundary 20 times leaves geometry, ticks
    and apparatus in exactly the state of a single crossing.
12. Catchword and folio ticks never announce more than once per
    section change to the live region; hover-driven hand moves
    never announce.
13. Night palette: rubric appears at small sizes only as pilcrow +
    ink text (§2); gold's night contrast is never used to justify
    gold information.
14. Print stylesheet: `@media print` renders each chapter with its
    initial in flow and the manicule beside its first paragraph;
    no overlays, no grain, no gilt — the leaf prints as a leaf.
15. The commissioning slip works fully without JS; its error notes
    are text beside the fields on the server-rendered response;
    no field's error is conveyed by colour alone.
16. Type scale unmodified: display appears once per page; Fell is
    absent from form labels, buttons and navigation rows (§9,
    rule 8).
17. Images: every miniature has scene-describing alt; the arch
    never opens onto an unloaded image (§6.11's 1200ms rule).
18. The five-second test (§1): a first-time viewer describes the
    page as *a book being read with them* — not "medieval", not
    "fantasy", not "a parchment theme".
19. Doodle captions are in §12's voice (the scribe's, dry, once) —
    a caption that winks twice is rewritten.

**Minimum bar, in one line:** a build that passes the blocking eight
has earned the right to be judged on premiumness; a build whose
hand a reader trusts — that points truly, turns leaves honestly,
and keeps its one joke to once a quire — is a Manicule & Catchword.
Anything less is a parchment costume, and it goes back to the
scriptorium.

---

## 11. Component inventory

Every UI component a real site in this theme needs, with its themed
treatment. Components not listed here do not appear; a component that
cannot be given a treatment in the manuscript's own terms is a sign
the feature does not belong in this theme.

- **Buttons (actions).** Not filled rectangles. A primary action is a
  rubricated text line with a lapis rule beneath (§6.14/§6.16) — the
  scribe's direction, underlined in the expensive ink. A secondary
  action is the same line in ink with an `--ink-soft` rule. Disabled:
  the line in `--ink-soft`, rule absent, `aria-disabled` — a
  direction the scribe has not yet written. Focus: 2px lapis outline.
- **Inputs.** Ruled lines (§6.16): transparent ground, bottom rule
  only, Garamond entries. No boxes, no filled fields, no floating
  labels — labels sit above their lines in the apparatus hand.
- **Selects.** A native `<select>` restyled to the ruled line, its
  closed face showing the chosen gathering; the open list is the
  browser's (the theme does not counterfeit native menus).
- **Checkboxes & radios.** Checkboxes are empty rubric squares that
  take a pilcrow-tick in ink when chosen (the reader marking a
  list). Radios are the tabula-row treatment (§6.16): the chosen
  row's signature rubricates. Native inputs, visually composed,
  never replaced by divs.
- **Tables.** Ruled like a tabula: header row in apparatus caps, a
  rubric hairline beneath it, row rules in `--vellum-deep`, figures
  in old-style numerals (§3) except sums (§3, law 3). No zebra
  striping — the ruling is the rhythm.
- **Badges / labels.** Quire signatures: small-caps apparatus text,
  never pill-shaped. A "new" badge is forbidden; novelty is stated
  in the apparatus line ("entered this week") or not at all.
- **Alerts.** A margin note (§6.16's error pattern generalised):
  italic Garamond in the margin beside the thing it concerns,
  lapis for instruction, ink for information. Rubric is never an
  alert colour (§2, law 3). No banners across the leaf; a
  site-wide notice, if unavoidable, is a slip pinned above the
  colophon position on the affected leaf only.
- **Pagination.** The catchword itself (§6.5): "Next gathering"
  is a catchword link with the folio range in apparatus. Numbered
  pagination, where a listing truly needs it, is roman numerals in
  the tabula style. "Load more" is a catchword line: *More
  gatherings follow* + the first word of the next plate's title.
- **Modals.** A modal is a tipped-in leaf: a smaller leaf laid over
  the current one, pricked frame, its own catchword-less foot (a
  tipped-in leaf has no gathering), closed by a rubric "Return to
  the leaf" line. Focus trapped per standard practice; the leaf
  beneath dims to `--vellum-deep` at 60%. One modal at a time; a
  modal that opens another is a design failure, not a flow.
- **Toasts.** None. Transient messages are margin notes that stay
  where they were put (§6.16) or they are not sent. A message too
  unimportant to keep is too unimportant to interrupt a reader
  with.
- **Tabs.** Gatherings: a row of quire signatures; the open
  gathering's signature rubricates and its leaf shows below. Tabs
  never scroll horizontally; more than six gatherings is a volume
  structure (§6.13), not a longer tab row.
- **Accordions.** "Opening a leaf": the summary line is a section
  heading (§3) with a pilcrow that rotates 90° on open (160ms
  `--ease-stamp` without the thud's overshoot — a quiet cousin of
  §6.10); the body opens with the §6.11 arch's vertical half (clip
  opening downward, 350ms `--ease-leaf`). Native
  `<details>` underneath, enhanced.
- **Search.** A single ruled line (§6.16's field) labelled "Seek a
  word or a leaf"; results are a tabula (§6.13) whose rows add the
  found word's line, set with the word itself rubricated *in
  context* — the one lawful body-text rubrication, because a found
  word is a beginning of reading (§3, law 2, applied honestly).
- **Progress (tasks).** For a genuine multi-step task (a commission
  with stages), progress is the apparatus line: *Leaf ij of iiij*
  with the steps named as gatherings. No bar (§5).
- **Tooltips.** Margin glosses: a dotted lapis underline on the
  glossed word; the gloss appears in the margin (desktop) or as a
  footnote line beneath the paragraph (mobile) in italic Garamond
  — where glosses have lived for eight hundred years. Never a
  floating bubble.
- **Dividers.** A fleuron line: a hairline in `--gold` at 40% with
  a centred fleuron glyph in ink — used between gatherings on
  single-page builds where no curl (§6.4) separates them. Inside a
  chapter, paragraphs are divided by the indent rule (§3), never
  by ornaments.
- **Breadcrumbs.** The apparatus itself: *Quire II · fol. vij · The
  Binding of the Nets* (§6.8), set as one line above the heading.
  A separate breadcrumb component would duplicate it.

---

## 12. Content & copywriting voice

The site speaks in two voices, and they never swap coats.

**The book's voice** (headlines, chapter text, plate descriptions):
the work's own authorial voice — the theme does not impose a tone on
the content it carries. The theme's rules for it are structural
only: headlines are lines, not slogans (a headline that could end in
an exclamation mark is rewritten); the first word of every section
is chosen knowing it will serve as a catchword (§6.5) — a section
that begins "The" spends its catchword cheaply, and editors should
know it.

**The scribe's voice** (apparatus, directions, errors, empty
states, the doodle): dry, brief, in the present tense, fond of the
reader and never familiar with them. The scribe states facts and
gives directions; he does not enthuse, apologise at length, or
perform whimsy. His sentences end. Examples, in his hand:

- **Direction (button/link):** ✓ "Begin the first quire" · ✓ "Send
  this to the scriptorium" · ✗ "Start your journey today!" · ✗
  "Let's go →"
- **Error:** ✓ "The direction you gave is incomplete — the part
  after the @ is wanting." · ✓ "Three lines want mending." · ✗
  "Oops! That email looks wrong." · ✗ "Invalid input."
- **Empty state:** ✓ "No gathering answers to that word. The
  tabula (§6.13) lists all that the book holds." · ✓ "Your marks:
  none yet. Headings take a mark when clicked." · ✗ "Nothing
  here… yet 👀"
- **Success:** ✓ "Received, and entered in the day-book as № 41."
  · ✗ "Awesome! You're on the list!"
- **Loading / waiting:** ✓ "The leaf is still being copied." · ✗
  "Hold tight, magic is happening."
- **The missing plate:** ✓ "The miniature is wanting." (the
  manuscript's own term, and the scribe does not elaborate).
- **Doodle caption:** ✓ "the binder's apprentice, on the same
  paragraph since Michaelmas." · ✗ anything with a second joke in
  it.

**Voice laws.**
1. Roman numerals in the apparatus are written the manuscript way
   (final *j*: vij, xxiij) in display, and standard form is
   acceptable in metadata; the two never mix on one leaf (§6.8).
2. Dates in display copy are written out ("the xii. day of
   October"); in forms and data they are ISO. Never "Oct 12th".
3. The scribe never says "medieval", "ye olde", or uses thee/thou.
   The theme is a working scriptorium, not a renaissance fair; fake
   archaism is the fastest §9 tell there is.
4. Second person is used plainly and rarely ("your marks", "the
   direction you gave"). The reader is a colleague in the reading,
   not a "user" and not a "friend".
5. Numbers that the apparatus states are always real (§10, item
   4). The scribe's credibility is the theme's credibility.

---

## 13. Full-page scroll choreography map

A chapter leaf, top to foot, in order. (The opening leaf substitutes
§8.1's timeline for beats 1–3.)

1. **The running head** (§6.13) sits over the leaf's head: title,
   current quire, Tabula. Still.
2. **The chapter heading** enters: its rubric flares 70%→100% over
   500ms as it crosses the 78% line (§5); its apparatus line
   (§6.8/§11 breadcrumbs) is already correct above it.
3. **The initial paints** in flow (§6.6, 900ms, gold → scene →
   figure) as the first paragraph arrives; the manicule (§6.2)
   glides to the first paragraph and takes the chapter's posture.
4. **Reading beats.** Paragraph by paragraph: the hand tracks the
   reading line (38%); the initial crossfades to its pinned double
   at the anchor (200ms) and glints on its 6s offset (§6.7); the
   vine's stem grows with the hand (§6.9), leaves popping as it
   passes their points.
5. **The miniature's arch opens** (§6.11) when the figure crosses
   30% visibility — 700ms up, image settling to 900ms, caption at
   600ms. If the chapter holds the quire's one doodle, the hand's
   single swivel to it (§8.2) happens in this stretch.
6. **Attention beats.** Any hover/focus borrows the hand (§6.3,
   250ms swivel, 350ms return); any heading click lands its
   pilcrow (§6.10, 160ms) and ticks the marks apparatus.
7. **Chapter end.** The hand comes to rest beside the leaf-foot;
   the catchword (§6.5) is showing the next chapter's first word;
   the folio (§6.8) is the chapter's own.
8. **The turn.** 60vh of scrubbed curl (§6.4): the hand hops aside
   (120ms), the underside catchword passes, the next heading
   flares as it is uncovered, the pinned initial fades with its
   leaf (200ms).
9. **Next chapter.** Beats 2–8 repeat with the new chapter's own
   letter, posture, miniature and quire arithmetic. At a quire
   boundary, §6.9's berries fill (400ms) as the old quire closes
   and the new cuff draws (600ms).
10. **The colophon** (§6.17): the hand does not enter. The marks
    summary, the maker's lines, *Explicit*. Stillness. The gilt
    edge closes the leaf.

Emotional arc: *arrival* (the flare and the painting) → *company*
(the hand, the vine, the one joke) → *the turn* (the book's weight,
felt once per chapter) → *the truth at the end* (the colophon). Any
beat that calls attention to itself outside this arc is cut.

---

## 14. Whole-page performance budget

**Asset budget (per page, compressed).**
- HTML + inline SVG apparatus: ≤ 90KB. The initials' SVGs are the
  weight; each painted initial ≤ 6KB, and a page carries at most
  one hero initial (§6.1) + one chapter initial (§6.6) painted, the
  rest in their resting state.
- CSS: ≤ 28KB. JS: ≤ 22KB gz — the shared loop, the observers, the
  stamp storage; the theme has no other scripts.
- Fonts: IM Fell English (1 weight + italic) + EB Garamond (400,
  500, italic) subset to Latin + the pilcrow and fleuron glyphs:
  ≤ 110KB total, `font-display: swap` with the §6.1 rule that a
  headline never re-paints after a swap.
- Images: miniatures ≤ 120KB each (duotone-compressed), at most 3
  loaded per page before lazy-loading takes over; the gallery leaf
  (§6.15) lazy-loads everything below the first row.

**Frame budget.** The shared rAF loop: ≤1.2ms/frame total on a
mid-range Android; per-element ceilings live in §6 (curl ≤1.0ms
in-zone, hand ≤0.15ms, everything else ≤0.05ms each). Long tasks:
none over 50ms attributable to theme code; the painting sequences
are CSS/SVG-driven precisely so the main thread is free during
them. CLS: 0 — every animated element occupies its final layout
box from first paint (markup is the finished state, §6.1's rule).

**Cut order — when the budget is exceeded, cut in this order, and
record the cut in the build notes:**
1. The night-mode candle flicker (§6.7) and the glint on chapter
   initials (hero initial keeps its glint).
2. The curl degrades to the lift (§6.4) on devices whose loop cost
   stays over budget.
3. The vine (§6.9) below 1200px (it is already cut <768px).
4. Parallax differentials (§5) flatten to 1.0× — the layers move as
   one; the hand and the curls are untouched.
5. The grain breath (§5) stops; grain renders static at 0.7%.
Never cut: the manicule's travel, the catchword/folio apparatus,
the fallbacks, or the reduced-motion variants. A page that keeps
its guide and its apparatus and loses its weather is still this
theme; the reverse is not.

---

## 15. Build-order checklist

1. **The static leaf first.** Build every page with zero JS:
   initials painted in markup, vines drawn, catchwords and
   apparatus generated and correct, the form submittable. Run
   §10's blocking items 1 and 4 against this build. Nothing else
   proceeds until the silent manuscript is complete — it is the
   fallback for everything that follows.
2. **The generation step.** Catchword extraction, folio/quire
   arithmetic, tabula generation from one source (§6.5/§6.8/
   §6.13). Verify the extraction log by hand on one full page.
3. **Typography and grid.** §3's scale, §4's quire grid, prickings,
   the gilt edge. Check the measure (58–66ch) at all three
   breakpoints.
4. **The shared loop.** rAF + lerp + IntersectionObserver
   scaffolding, with the §6.4 watchdog and the 1s laws wired
   before any device uses them.
5. **The manicule.** §6.2's travel and posture; then §6.3's swivel;
   then the focus-parity path. Guide audit (§10, item 5) by
   keyboard alone.
6. **The apparatus ticks.** §6.5 + §6.8 with the live region;
   verify announcement discipline (§10, item 12).
7. **The turns.** §6.4's curl + §6.12's transition on top of it;
   the 20-crossing purity check (§10, item 11).
8. **The paintings.** §6.1, then §6.6's chapter scale + pin
   handover; then §6.11's arches.
9. **The small devices.** §6.7 glint, §6.9 vine, §6.10 stamps +
   storage, §6.13 tabula behaviours.
10. **The slip.** §6.16 with server validation rendering the same
    notes; no-JS submission end-to-end.
11. **The quiet pages.** §6.17 colophon (computed year), §6.18
    unfinished leaf (real 404 status).
12. **Night and print.** §2's candlelit palette, §10 item 14's
    print stylesheet.
13. **The full gate.** §10 end to end, on a mid-range Android and
    a desktop, with the doodle count and the gold audit done by a
    reviewer who did not build the page.
