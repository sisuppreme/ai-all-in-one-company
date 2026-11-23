# 2. Marginalia — Expanded (20x Standard)

> Source identity preserved from `themes-001-025.md`, theme #2. This expansion deepens that exact theme — same concept, same palette, same two typefaces, same twelve signature elements — to full build-spec depth. Nothing here is interchangeable with another theme: every number, colour and gesture belongs to a much-loved, argued-with book.

---

## 1. Concept & world

**The world.** Marginalia is a second-hand book that was loved hard by exactly one previous reader. The printed text (the "book") is calm, authoritative EB Garamond. Living alongside it, in a wide right-hand margin, is the Annotator — a specific, opinionated person who read with a pencil and later a blue pen, and who *argues back*: "he never actually said this — see p.41", "yes!! this", "no. too easy." The site is the collision of those two voices. The printed voice never moves, never performs. The Annotator's voice arrives late, leans in, darkens under attention, and occasionally loses an argument (a note crossed out by a second, bluer note).

**The emotional contract.** A visitor should feel they have borrowed someone's personal copy — slightly guilty, completely charmed, and smarter for the second voice. Warmth comes from evidence of use: one coffee ring per chapter, deckled page edges, visible paper fibres, exactly one foxing spot per screen, graphite dust in the hero margin. Nothing is pristine; nothing is dirty. Wear is *placed*, never scattered.

**The one rule that defines the theme.** Annotations are content, not decoration. Every margin note must comment on, explain, date, dispute or endorse the *specific paragraph it sits beside*. If a note could sit beside any paragraph, it is deleted. Removing all animation must leave a page that still reads as an annotated book — notes pre-written, underlines drawn, rings present.

**Best-fit sites and audiences.**

| Fit | Why this theme serves it |
|---|---|
| Authors, essayists, newsletter writers with a backlist | The Annotator becomes the author's present-day self commenting on their older work — the margin is a built-in "director's commentary" |
| Book clubs and reading communities | Notes model discussion; members' picks can be "annotated" editions |
| Tutoring, study-guide and education brands | Worked explanations live exactly where students get stuck — beside the paragraph, not in a separate solutions page |
| Publishers selling annotated / anniversary editions | The page itself demonstrates the product: this is what the annotated edition feels like |
| Memoir, letters and archive projects | A second voice (editor, descendant, historian) can correct and date the primary text in place |
| Slow, long-form product storytelling (craft, heritage goods) | The maker's pencil notes beside the specification read as workshop honesty |

**When NOT to use Marginalia.**

- Checkout, pricing or comparison flows where a second, disputing voice would undermine a decision the visitor must make quickly. (Forms borrow the theme's paper and pencil, but the Annotator never argues on a payment step — see §6, element 17.)
- Data-dense dashboards: the 62ch reading column and 240px margin are a deliberate tax on width; tables wider than ~62ch fight the leaf.
- Brands that must appear flawless and corporate: foxing, coffee rings and visible disagreement are the opposite of that promise.
- Short landing pages with under ~600 words of body copy: the Annotator needs real paragraphs to annotate; with nothing to argue with, the margin becomes empty costume.
- Any build that cannot source real annotation copy. Lorem-ipsum margin notes are the single fastest way to make this theme look fake (see §9).

**Voice of the Annotator (write to this, or do not ship).** Lowercase starts are allowed; sentence fragments are allowed; references must be specific ("see p.41", "cf. the 2019 ed.", "mum's copy had this underlined too"). The Annotator is wrong at least once per long page and is corrected in blue. The Annotator never sells, never uses marketing language, and never annotates the footer, the price, or the legal line.

---

## 2. Palette

Base palette is exactly the four source colours. The token table adds only *derived* values (tints, shades and opacities of those four) — no new hues enter the theme, ever. A fifth colour appearing anywhere is a build defect.

| Token | Value | Role | Usage ratio | Pairing & contrast notes |
|---|---|---|---|---|
| `--page` Aged page | `#EFE6D0` | Page ground; the leaf itself | ~62% of any viewport | Ground for all text. Never used as a text colour except on `--ink` chips in the footer colophon |
| `--page-deep` | `#E7DCC2` (Aged page darkened 6%) | Recessed areas: drawer of the chapter list, form field wells, plate mats | ~6% | Always adjacent to `--page`, never to white; the step must read as thicker paper, not a new colour |
| `--page-edge` | `#DCCDA9` (Aged page darkened 12%) | Deckled edge strip, hairline rules at 100% strength, card borders | ~2% | Used at 1px–14px scales only; large areas of `--page-edge` look like dirt, not deckle |
| `--ink` Iron-gall ink | `#2B2620` | All printed body text, headlines, plate captions | ~18% visual weight | On `--page`: contrast 12.4:1 — passes AAA for body at 19px+. The *only* colour body text may be |
| `--ink-soft` | `#2B2620` at 72% opacity | Secondary printed matter: folios, running heads, table-of-contents numerals | ~3% | Never below 72% — at 60% it reaches ~4.6:1 and is reserved for 20px+ display only |
| `--pencil` Pencil | `#8A7F6A` | Margin notes at rest, underline strokes at rest, progress line, dust | ~6% | On `--page`: 3.6:1 — legal *only* because notes are 20–24px Caveat (large text) and are an enhancement layer; every note must ALSO be available in `--ink` via the note-lean hover/focus darkening (element 10) and in the no-JS print state |
| `--pencil-deep` | `#6E6350` (Pencil darkened 18%) | Note text on `--page-deep` backgrounds; tick strokes; the pencilled arrowhead on the progress line | ~1% | Keeps notes legible (4.9:1) when a note overlaps a recessed area |
| `--blue` Annotator's blue | `#33536E` | The second, later hand: corrections, dates, cross-references, form annotations, the one blue note per chapter that wins an argument | ~2% | On `--page`: 7.1:1 — passes AA for normal text, so blue notes may be 18px. Blue is rationed: max 1 blue note per chapter + form annotations + the colophon link colour |
| `--blue-bright` | `#4A7298` (Blue lightened 22%) | Link hover state; the underline beneath a blue note when focused | <1% | Hover/focus only; never a resting colour |
| `--ring` Coffee ring | `#8A7F6A` at 55% opacity, multiply blend | The one coffee ring per chapter | <1% | Rendered as two concentric irregular strokes (see element 7), never a filled circle, never a stock image |
| `--fox` Foxing spot | `#B09A72` at 50% opacity | The single foxing spot per screen | <1% | Radial-gradient blob, 26–44px, irregular edge via two overlapping gradients; exactly one per viewport height — a script enforces max 1 per 900px of page height |

**Pairing rules.**

1. Body text is `--ink` on `--page`. No exceptions, no grey body text.
2. Pencil is a *pressure* colour, not a text colour: it exists on a ramp to `--ink` (hover/focus/darkening) and anything written in pencil must survive being read at its darkest state.
3. Blue never touches the printed book — only the Annotator's later hand, form annotations and links. A blue headline is a defect.
4. Red does not exist in this theme. (Red belongs to The Proofreader's Desk, theme #7. A red underline in Marginalia is a cross-theme leak.)

**Dark-mode behaviour.** Marginalia has **no dark mode**, deliberately: the fiction is a physical leaf under a lamp, and inverting it breaks the paper. Instead, the theme ships a *lamplight* response to `prefers-color-scheme: dark`: the page keeps its colours but the raking reading-light (element 4) warms by shifting its gradient overlay from `#FFFFFF` at 0% to `#FFEDBE` at 10% opacity and the surrounding chrome outside the leaf (browser-level backgrounds, the site header band beyond the page edge) deepens to `#221D16`. The leaf itself never inverts; a visitor in a dark room reads a lit page, exactly like a real book. If a product *requires* a true dark UI, Marginalia is the wrong theme — see §1.

---

## 3. Typography

Two faces only. A third typeface appearing anywhere — including in a form widget or a cookie banner — breaks the fiction and fails the quality gate.

### 3.1 The printed book — EB Garamond

| Role | Size / line-height | Weight | Tracking | Rules |
|---|---|---|---|---|
| Display / chapter title | 54px / 1.04 (mobile 38px / 1.08) | 500 | −0.01em | Sentence case, never uppercase; max 2 lines; the Annotator may underline ONE word of it (element 1) |
| H2 — passage head | 34px / 1.15 | 500 | −0.005em | Numbered with a pencil folio numeral, e.g. a `--pencil` "3." that is part of the heading element, not a separate graphic |
| H3 — sub-head | 24px / 1.25 | 600 | 0 | Used sparingly: max 1 per passage; italic for Latin or titles of works |
| Body | 20px / 1.62 (acceptable range 19–21px; never below 19) | 400 | 0 | Max 62ch; first paragraph of a chapter takes a 3-line drop initial in EB Garamond 500 (not rubricated — red is not in this theme; the initial is `--ink`) |
| Body italic | 20px / 1.62 | 400 italic | 0 | Quotations and the book's own asides; the Annotator never writes in italic |
| Caption (plates) | 15px / 1.45 | 400 | +0.01em | `--ink-soft`; set beneath plates, left-aligned to the plate edge; always includes a plate number ("Plate II.") |
| Folio / running head | 13px / 1 | 500 | +0.18em, uppercase | `--ink-soft`; page furniture only ("MARGINALIA · CH. 3", folio numerals) |
| Data / tallies | 20px EB Garamond, `font-variant-numeric: tabular-nums` | 500 | 0 | Folio counts and "layers" tallies (element 6 spec) count in the book's own face — the book keeps its own records |

### 3.2 The Annotator's hand — Caveat

| Role | Size / line-height | Weight | Rotation | Rules |
|---|---|---|---|---|
| Margin note | 22px / 1.25 (range 20–24px) | 500 | −1° to −3°, assigned per note and fixed (a note's rotation is part of its identity; it never changes between visits) | Max 34 words; max 4 lines; line breaks are authored, not flowed — the note wraps where a hand would lift the pen |
| Margin note, long (the pinned chapter hand) | 24px / 1.3 | 500 | −1.5° fixed | Max 60 words; this is the chapter's keynote annotation (element 5) |
| Blue correction note | 20px / 1.25 | 600 | −1° | The later hand writes slightly smaller and firmer; max 20 words — corrections are terse |
| Underline / circle strokes | SVG stroke 2px, round cap | — | follows the word | Pencil at rest; strokes are paths, never CSS borders (a border cannot wobble) |
| Form annotation | 20px / 1.2 | 500 | −2° | The Annotator's only appearance inside forms: one line per field, written as help, never as an error (see element 17) |
| Tick | SVG stroke 2.5px | — | −4° baseline | The pencilled ✓ (element 11); drawn, never a ✓ glyph in a font |

**Type scale (whole theme).** 13 / 15 / 20 / 22 / 24 / 34 / 54px. Nothing renders at 16, 17, 18 or 28px — off-scale sizes are the most common way this theme quietly turns into a generic blog. Buttons and UI chrome borrow the folio style (13px uppercase tracked) set in EB Garamond; there is no sans-serif anywhere in Marginalia.

**Loading behaviour.** Both faces load with `font-display: swap`; the fallback stack is Georgia, 'Times New Roman', serif for EB Garamond and 'Segoe Print', 'Bradley Hand', cursive for Caveat. During the swap window, margin notes render in the cursive fallback at 96% opacity and cross-fade over 200ms when Caveat arrives — a note may never pop in at full strength, because a hand does not teleport. If Caveat fails entirely, notes fall back to EB Garamond italic 19px in `--pencil-deep` and the scribble-in animation (element 1) is disabled — handwriting that is not handwriting must not pretend to write itself.

---

## 4. Layout language

**The leaf.** The page is one leaf, centred, on a barely-darker surround (`#E3D7BC` at the body level, 8% darker than `--page`, so the leaf reads as paper on a desk, not a card on a screen). Leaf max-width: **1180px** on desktop. Inside the leaf, a CSS grid of three columns:

| Zone | Width | Content |
|---|---|---|
| Left gutter | 64px | Nothing but the deckled edge and, on chapter openers, the drop initial's overshoot. Emptiness here is load-bearing — it is the book's inner margin |
| Reading column | max 62ch (~640px at 20px EB Garamond) | The printed book: body, headings, plates at column width |
| Annotator's margin | min 240px, max 300px, flexible | Margin notes, pinned hand, pencil progress line on its outer edge |

Grid gap between reading column and margin: 48px. The margin notes align to their paragraph's first baseline ±4px — alignment is computed at layout, stored as a per-note offset, and recomputed on resize (debounced 150ms) and on font load.

**Deckled edge.** The leaf's right and bottom edges carry a deckle: a 14px strip where an SVG turbulence-displaced mask eats irregular 1–3px bites from the edge. The left edge is straight (it is the bound edge). The deckle is a mask on the leaf, not a background image, so the surround colour shows through the bites. Top edge: straight, where the leaf was trimmed.

**Spacing rhythm.** Vertical rhythm is the body line: **32.4px** (20px × 1.62). All vertical spacing is a multiple of half-lines (16.2px): paragraphs 1 line apart (32.4px), passage heads 3 lines above / 1 line below, chapter breaks 6 lines. Margin notes sit on the same rhythm so the Annotator appears to write on the same ruled page. Horizontal furniture: hairline rules are 1px `--page-edge` at full strength or `--ink` at 14% opacity for in-text rules.

**Section choreography.** A chapter is: chapter opener (folio + title + drop initial) → 3–7 passages, each a heading (from passage 3 onward), 1–4 paragraphs, 1–3 margin notes, at most 1 plate → chapter close (coffee ring lands near the final note; a hairline rule; the next chapter's folio). Chapters are separated by 6 lines of empty page — whitespace is the chapter break, never a coloured band. There are no full-bleed sections, no coloured background blocks, and no cards on the leaf except plates (element 14) and the chapter-list drawer (element 13). Density rule: at any scroll position, at most **one** animated event may be in progress on screen — the Annotator is one person and cannot scribble in two places at once; the motion queue (§5.0) enforces this.

**Responsive behaviour.**

| Breakpoint | Layout |
|---|---|
| ≥1024px | Full three-zone leaf as above |
| 768–1023px | Margin narrows to 200px; reading column 58ch; note size 20px; pinned hand (element 5) shortens to ~80vh |
| <768px | Single column: the margin collapses INTO the text flow. Each note becomes an indented block directly after its paragraph, set on a `--page-deep` slip with a 2px pencil left rule, still rotated −1°, still Caveat. The pencil progress line moves to the left edge at 8px. Pinned hand is disabled (nothing pins on mobile). Raking light becomes a top-down gradient (element 4 mobile variant) |

The mobile note-slip is not a compromise to hide: it is typeset as a *tipped-in slip*, the way a reader tucks a note into a borrowed book. It carries the same note, same rotation, same darkening behaviour on tap.

---

## 5. Full motion system

### 5.0 Global motion governance (applies to every row below)

- **One-hand rule:** a single global motion queue serialises Annotator events (scribbles, underlines, wiggles, ticks). If two triggers collide, the later one waits until the earlier finishes + 120ms. Book events (paragraph settles, plate reveals) run on a separate, quieter channel and never animate *during* an Annotator event in the same viewport.
- **Scroll engine:** one `requestAnimationFrame` loop with lerp factor **0.12** drives all scrubbed values (light position, progress line, parallax offsets). Raw scroll events never write styles. The loop sleeps when the tab is hidden and when scroll velocity has been 0 for 500ms.
- **Easing library (the only easings in the theme):**
  - `--ease-settle: cubic-bezier(0.22, 1, 0.36, 1)` — the book settling; paragraphs, plates.
  - `--ease-pen: cubic-bezier(0.4, 0, 0.2, 1)` — the hand moving; notes, ticks, underlines.
  - `--ease-lamp: linear` — scrubbed light and progress only; a lamp does not ease.
  - `--ease-page: cubic-bezier(0.65, 0, 0.35, 1)` — page-turn transition only.
- **Duration ceiling:** no single animation exceeds 1600ms except the coffee-ring fade (1400ms) and the hero scribble (≤2100ms for a 12-word note at natural pen speed). Ambient loops are 9000ms+ so they read as stillness, not motion.

### 5.1 The vocabulary, translated into Marginalia's materials

| Motion term | Marginalia's translation | Duration / easing | Trigger |
|---|---|---|---|
| Scroll-triggered reveal | **Paragraph settle** — each paragraph arrives 6px low and 96% ink, settling to 0px / 100% as it crosses 78% viewport height; the eye lands, the line lands | 550ms, `--ease-settle` | IntersectionObserver, threshold at 78% line, once per paragraph |
| Scroll-scrubbed animation | **Raking reading-light** (element 4) and **pencil progress line** (element 6) — both lerped at 0.12 | Continuous, `--ease-lamp` | Scroll position, rAF loop |
| Parallax | **Loose-leaf drift** — margin notes translateY at 0.94× body speed (max offset ±9px), plates at 0.97×, paper-fibre layer at 0.90×; the margin is a loose leaf tucked in, so it lags the bound text | Continuous, lerped 0.12 | Scroll; disabled <768px |
| Pinned section | **Pinned margin hand** (element 5) — the chapter's keynote note pins beside its paragraph for 100–160vh | Pin duration = paragraph height + 40vh | Scroll, `position: sticky` inside a chapter-length margin track |
| Masked line reveal | **Chapter-opener deckle wipe** — chapter titles reveal through a clip-path whose right edge is the deckle mask, sweeping left→right | 800ms, `--ease-settle` | Chapter opener entering at 85% line |
| Blur-to-sharp reveal | **Plate focus** — plates arrive at blur(3px) + scale 1.04 inside their pasted frame and focus to blur(0) / scale 1.00, as if angled into the light | 700ms, `--ease-settle` | Plate entering at 80% line |
| Staggered reveal | **The Annotator arrives second** — every note staggers exactly 500ms behind its paragraph's settle (element 2); chapter furniture staggers folio → rule → title at 120ms beats | 500ms fixed delay; 120ms beats | Sequenced after paragraph settle |
| Kinetic typography | **Self-scribbling note** (element 1) and **disputed-word wiggle** (element 3) — the handwriting itself is the kinetic type; printed type NEVER moves kinetically (the book is bound; only the hand is alive) | Per element specs | Load / scroll entry |
| Animated counters | **Folio count-up** — the running folio and the "leaves annotated" tally in the chapter drawer tick in EB Garamond tabular figures, 1 digit roll of 300ms per increment | 300ms per step, `--ease-pen` | Section boundary crossing |
| Progress indicator | **Pencil-line progress** (element 6) — a graphite stroke drawn down the outer margin with 1px hand wobble, ending in a pencilled arrow at the reading position | Scrubbed, `--ease-lamp` | Scroll |
| Marquee | **The binder's strip** — the ONLY marquee: in the footer colophon, a slow horizontal crawl of the book's imprint line ("set in eb garamond · annotated in pencil · printed on digital vellum ·") at 18px/s, pausing on hover. A marquee anywhere else in Marginalia is slop | 18px/s linear, infinite | Time; footer in view only |
| Ambient loop | **Pencil-dust drift** (element 9) in the hero margin; **paper-fibre shift** — the fibre layer's background-position drifts 0→6px over 24s and back, only while the raking light moves | 9000–14000ms loops; 24s | Time / light movement |
| Micro-interactions | **Note-lean hover** (element 10), **pencilled-tick click** (element 11), plate tilt-to-light (element 14) | 200–300ms, `--ease-pen` | Hover / click |
| Hover physics | Notes lean with spring overshoot: rotate toward pointer by up to 2°, spring stiffness 180, damping 14 (implemented as a 300ms cubic-bezier(0.34, 1.56, 0.64, 1) approximation — the one sanctioned overshoot in the theme, because a loose leaf wobbles) | ~300ms settle | Pointer over note |
| Page transition | **Page-turn** (element 12) — corner lift + leaf sweep | 450ms, `--ease-page` | Route change / in-book navigation |
| Image treatment | **Pasted-plate treatment** — plates sit in a `--page-deep` mat with a 6px inner border of `--page`, a 1px `--page-edge` keyline, and the focus reveal above; images are NEVER full-bleed, never borderless, never rounded (a pasted plate has square corners; border-radius on a plate fails the gate) | 700ms focus | Scroll entry |
| Skeleton loading | **Unwritten leaf** — skeleton is the leaf itself: hairline rules where lines will sit, an empty margin with one faint pencil dot where the first note will land; content inks in book-first, notes 500ms later, exactly as in live reading | Sheen sweep 1800ms, `--ease-pen` | Load state |
| Scroll-driven light (theme signature) | **Raking reading-light** (element 4) — a 35° diagonal gradient, 420px band, scrubbed so its centre tracks 55% of viewport height + scroll; fibres and foxing brighten inside the band | Continuous | Scroll |

### 5.2 Reduced-motion system (summary — per-element variants are in §6)

With `prefers-reduced-motion: reduce`: the book arrives pre-annotated. Notes are present, fully drawn, beside their paragraphs; underlines and circles are complete strokes; the light is fixed at a gentle 40° wash; parallax, pinning, scribbling, wiggle, dust and the page-turn are all off; the page-turn becomes an instant change with a 120ms opacity fade of the leaf only. Nothing about the *content* differs — a reduced-motion reader gets the same annotated book, already annotated. Implementation: a single `data-motion="reduced"` attribute on the leaf, set from the media query before first paint, and every animation in §6 checks it; CSS-only fallbacks use a media-query block that forces final states.

---

## 6. Signature elements — full build specs

Elements 1–12 are the theme's signature elements, deepened from the source entry. Elements 13–18 are the page-family elements (navigation, hero, cards, forms, footer, loader/transition), built in the same world. Every spec follows the same fields: what & why · structure · motion spec · states · content-merge · failure fallback · reduced-motion variant · performance budget & mobile variant.

---

### Element 1 — Self-scribbling margin note

**What & why.** Beside the hero headline (and once per chapter opener), a Caveat note writes itself stroke by stroke, then underlines one chosen word of the headline with a double pencil stroke. It is the theme's thesis in one gesture: someone has read this, by hand, and had a thought. If a build can only afford one Annotator moment, it is this one.

**Structure.** Inline SVG per note, authored at build time: the note text is converted to stroke paths (handwriting path font or hand-authored paths for hero notes; chapter notes may use a stroke-animatable Caveat subset). DOM: `<aside class="note note--hero">` containing `<svg class="note__hand" viewBox="…">` with one `<path>` per word, plus a sibling visually-hidden `<p>` carrying the note text for assistive tech and no-JS. The underline is a separate SVG absolutely positioned over the headline word it underlines (two paths, second stroke offset +3px, 60% opacity).

**Motion spec.** Pen speed: **90ms per word average with ±30% per-word variation** (long words slower; the pen "lifts" 60ms between words). A 10-word note ≈ 960ms + lifts ≈ 1500ms total; hard cap 2100ms — notes longer than 14 words in the hero are split, never sped up (a rushed hand looks fake). Stroke draw via `stroke-dasharray`/`stroke-dashoffset`, `--ease-pen`. The underline follows 250ms after the last word: first stroke 320ms, second stroke 260ms. Trigger: **600ms after the hero headline's settle completes** on load; chapter-opener variants trigger when the opener crosses the 80% line.

**States.** *Rest (pre-trigger):* note area empty but space reserved (no layout shift — the aside has fixed min-height from the authored line count). *Writing:* strokes partial; a 2px pencil-dot "nib" leads the active stroke (an SVG circle r=2 in `--pencil`, positioned at the path's current point via `getPointAtLength`). *Complete:* nib fades 150ms; note rests at its assigned rotation. *Scrolled-past:* static; never replays on scroll-back (the hand writes once — replays break the fiction; only a route return re-arms it).

**Content-merge.** The note comments on the headline's actual claim and the underlined word is a word *in that headline*. The underline's geometry is measured from the real word's bounding box at layout time, so editing the headline re-targets the underline. This is not a sticker near a headline; it is an annotation *of* it.

**Failure fallback.** Every stroke path has a **1400ms fill-timeout**: a watchdog (and a CSS animation fallback) forces `stroke-dashoffset: 0` if the draw has not completed, so a note can never be left half-written. If SVG or JS fails entirely, the visually-hidden text paragraph is revealed by the no-JS stylesheet in Caveat/`--pencil-deep` — the note reads as pre-written. Headline and page are fully legible with the note entirely absent.

**Reduced-motion variant.** Note appears pre-written (final stroke state) with a 200ms opacity fade only; no nib, no underline draw (underline present, complete).

**Performance budget & mobile.** Budget: ≤12 path elements per hero note, total path length ≤6000 units; draw runs on the compositor via CSS animations on `stroke-dashoffset` where possible; JS only sequences. Cost ceiling: 0 long tasks >50ms during the write. Mobile (<768px): the hero note becomes the tipped-in slip under the headline and is **pre-written** (scribble is a desktop-margin behaviour); chapter notes never scribble on mobile.

---

### Element 2 — Half-second-late annotations

**What & why.** Every ordinary margin note arrives exactly **500ms after its paragraph settles** — the delay of a reader catching up. This single timing rule creates the theme's breathing rhythm across the whole page: text, pause, thought. It is the most-repeated behaviour in Marginalia and the one visitors describe afterwards.

**Structure.** Each note is an `<aside class="note">` in the margin grid cell aligned to its paragraph, containing rendered Caveat text (real text, not SVG — only hero/chapter notes are stroke-drawn) plus an optional underline/circle SVG (element 8). Notes carry `data-anchor` = paragraph id; alignment via the layout pass in §4.

**Motion spec.** Entry: `translateX(18px) → 0` (from the page edge inward) + opacity 0→1, **500ms, `--ease-pen`**, starting exactly 500ms after the anchored paragraph's settle animation *ends* (not starts). Rotation is constant throughout (the note's assigned −1° to −3°). If the paragraph settled while off-screen (fast scroll), the note uses a shortened 250ms delay — the reader was skimming, the Annotator keeps up.

**States.** *Rest:* fully present at rotation, `--pencil`. *Entering:* as above. *Scrolled-past:* static. *Re-entry from below (scrolling up):* notes are already present — they never re-animate upward; the Annotator has already been here.

**Content-merge.** Each note is anchored to one paragraph and written against it: explanation, dispute, date, cross-reference or endorsement. The 500ms delay is meaningful only because the note is *about* the text that just landed.

**Failure fallback.** Notes are real DOM text with default state **visible**. Animation is applied via a `.will-animate` class added by JS only when the observer is armed, plus a 1200ms force-visible watchdog per note. No-JS: notes simply sit beside their paragraphs — the intended static book.

**Reduced-motion variant.** Notes appear with their paragraph (no delay, no slide) at full opacity — the 500ms beat is a motion courtesy, not information, so it is the first thing reduced motion removes.

**Performance budget & mobile.** Budget: transforms/opacity only; max 1 note animating at once (global queue, §5.0); each note ≤4 lines of text. Mobile: notes become tipped-in slips after their paragraph (§4); entry is a 300ms fade + 8px rise, delay reduced to 200ms; the queue still serialises them.

---

### Element 3 — Disputed-word underline wiggle

**What & why.** Where the Annotator disagrees with a specific word ("he never *actually* said this — see p.41"), that word's pencil underline wiggles — a tiny shake of disbelief — when it enters, then rests. It localises argument to a single word: the smallest possible unit of marginalia, animated.

**Structure.** The disputed word is a `<span class="disputed">` in the body text with an inline SVG underline path beneath it (path with a hand-drawn 1px irregularity, drawn by element 8's system). The wiggle animates the SVG group only, never the word itself — printed type does not move in this theme (§5.1); the *pencil mark* moves.

**Motion spec.** On entry: rotation oscillation **±1.2°**, 3 full oscillations, **450ms total**, decaying amplitude (1.2° → 0.7° → 0.3°), `--ease-pen`, transform-origin at the underline's left end (the pen's starting point). Paired margin note arrives on the normal 500ms-late schedule and names the dispute.

**States.** *Rest:* underline still, `--pencil`. *Wiggling:* as above, once only. *Hover on the word:* underline darkens to `--pencil-deep` over 200ms and the paired note leans (element 10 behaviour) — connecting word and argument. *Scrolled-past:* still forever; the wiggle never repeats within a session.

**Content-merge.** The wiggle exists only where the copy genuinely contains a disputable claim and the note supplies the counter-evidence. A wiggle on a word nobody disputes is decoration and is cut in review.

**Failure fallback.** The underline is a complete SVG path in the DOM by default; the wiggle is a class-triggered animation. Failure = a still underline, which loses nothing. Word and note are plain text, always readable.

**Reduced-motion variant.** No wiggle. The underline is present; the note is present. Disagreement survives intact — only the shake is gone.

**Performance budget & mobile.** Budget: one SVG path ≤120 units, transform-only animation, negligible. Mobile: identical (the slip note sits below, the underline still wiggles once on entry if motion is allowed).

---

### Element 4 — Raking reading-light

**What & why.** A soft diagonal light, as from a desk lamp at the reader's left, is scrubbed to scroll position and sweeps down the leaf as you read — brightening paper fibres, the foxing spot and plate surfaces inside its band. It is the theme's scroll-scrubbed signature: reading *takes time and a lamp*, and the light is the proof. It also quietly solves a real problem: it gives scroll a felt, physical feedback without moving any content.

**Structure.** One absolutely-positioned overlay div covering the leaf, `pointer-events: none`, `mix-blend-mode: overlay` at low strength, background: `linear-gradient(215deg, transparent 0%, rgba(255,252,240,0.55) 42%, rgba(255,252,240,0.0) 58%, rgba(43,38,32,0.10) 78%, transparent 100%)` — a 420px bright band with a soft shadow trailing below it. The fibre layer and foxing spot are separate low-opacity layers whose opacity is modulated by proximity to the band centre (computed in the same rAF loop: `boost = clamp(1 − |elementCentre − bandCentre| / 300)`).

**Motion spec.** Band centre target = scroll progress mapped so the band sits at **55% of viewport height** relative to the leaf; lerped at **0.12** per frame (§5.0) — the light lags scroll by a breath, like a lamp being re-angled. Fibre opacity inside band: 0.05 → 0.13; foxing spot: 0.30 → 0.50 opacity. No easing curve — `--ease-lamp` (linear scrub, smoothed by lerp only).

**States.** *Rest (no scroll for 500ms):* light holds position; fibre boost decays to base over 800ms. *Scrolling:* as above. *Scrolled-past / top:* band parks above the leaf's top edge so the hero is lit by element 9's ambient state instead. *Focus mode (keyboard navigation):* the band additionally centres on the focused element within 300ms — the lamp follows the reader's place, whoever is driving.

**Content-merge.** The light acts on the page's own materials — fibres in the paper, foxing in the leaf, the surfaces of plates — never on a decorative overlay scene. Margin notes catch the light **120ms after** body text at the same height (their parallax lag, §5.1), so the lamp unifies book and margin as one physical surface.

**Failure fallback.** The overlay is pure enhancement: without JS it is absent (or rendered as a static, barely-visible gradient by CSS at a fixed 40° wash) and the page is a normally lit leaf. All text contrast is calculated *without* the light — the light may only add, never carry, legibility. If blend-mode is unsupported, the overlay is dropped entirely (feature-detected), not approximated with a white box.

**Reduced-motion variant.** Light fixed at the 40° static wash; no scrubbing, no fibre modulation. `prefers-color-scheme: dark` triggers the warmed lamplight tint from §2 instead of movement.

**Performance budget & mobile.** Budget: one full-leaf overlay repaint per frame max, transform-only movement (`translate3d` on the oversized gradient layer, never background-position animation); fibre modulation writes opacity on ≤3 elements per frame. Must hold 60fps on a mid-range laptop with the full page; if frame time exceeds 20ms sustained, the loop degrades gracefully: fibre modulation off first, then band lerp coarsens to 0.08 steps. Mobile: band becomes a **vertical top-down gradient** (light from above, no diagonal — a phone is read upright), band height 300px, fibre modulation off; overlay cost is a single static-position layer translated on Y only.

---

### Element 5 — Pinned margin hand

**What & why.** Each chapter has one keynote annotation — the longest, most personal note (≤60 words, 24px). It pins in the margin beside the reading column for the length of its paragraph and travels with the reader, the way you'd hold a thought while reading a long passage. It is the theme's pinned-section moment, done at the scale of a margin rather than a viewport takeover.

**Structure.** The margin column contains a chapter-length track (`position: relative`); the keynote note is `position: sticky; top: 18vh` inside it. The note is real Caveat text with one underlined phrase (element 8). A faint pencil bracket (SVG, 2px) runs down the reading column beside the exact paragraph span the note covers, drawn when the pin engages.

**Motion spec.** Pin engages when the covered paragraph's first line crosses **60% viewport height**; the note slides the final 12px into its pinned offset over **400ms, `--ease-settle`**, and the paragraph bracket draws over **600ms, `--ease-pen`**. Pin persists for the paragraph's scroll length (**~100–160vh** depending on paragraph length — set by content, never padded to reach 160vh). On release, the note fades to 60% and un-pins over 300ms as the next chapter's hand takes over the track; two keynote notes are never pinned simultaneously.

**States.** *Approaching:* note sits at its natural margin position. *Pinned:* full `--pencil`→ slightly deepened (`--pencil-deep` for its underlined phrase only), bracket present. *Released:* 60% opacity rest state in place. *Scrolled-past chapter:* all keynote notes rest static in the margin flow.

**Content-merge.** The pinned note is a sustained commentary on one specific long passage — an extended objection, a memory the passage triggers, a worked example. Its bracket marks the exact lines it covers. Pinning a short or generic note is forbidden: if a chapter has no passage that earns 60 words, the chapter has no pinned hand (see §9).

**Failure fallback.** Without JS/sticky support, the note is simply a margin note in flow at its paragraph — the design's static state. Sticky is native CSS; the JS only adds the bracket draw and fade choreography, both with the standard 1200ms force-final watchdog.

**Reduced-motion variant.** No pinning. The keynote note sits in flow beside its paragraph, bracket pre-drawn. On mobile (<768px) pinning is likewise disabled and the note becomes a tipped-in slip (§4).

**Performance budget & mobile.** Budget: native `position: sticky` (no scroll JS for the pin itself); bracket is one SVG path ≤400 units. Mobile variant: slip form, no bracket (the slip's pencil left rule does the bracket's job).

---

### Element 6 — Pencil-line progress

**What & why.** Reading progress is drawn, by the Annotator, as a graphite line down the outer margin, lengthening as you read and ending in a small pencilled arrow at your current position — "you are here, in pencil, because you'll move." It replaces every conventional progress bar in the theme; a UI progress bar in Marginalia is slop.

**Structure.** A fixed-height SVG pinned to the margin's outer edge (desktop: right edge of the leaf margin, 24px wide, full leaf height). The line path is pre-authored with **1px hand wobble** (a path with micro-deviations every ~40px, generated once at build, not randomised per load — the wobble is the Annotator's hand, and it is the same hand every visit). Draw via `stroke-dashoffset` scrubbed to progress. The arrowhead is a separate 14px path at the line's live end. A tally in the chapter drawer header ("leaf 3 of 9 · annotated") updates at chapter boundaries.

**Motion spec.** Scrubbed, `--ease-lamp`, lerp 0.12 (§5.0). The arrowhead redraws its position each frame from the same progress value (no independent animation). At chapter boundaries, the line gets a small pencilled cross-tick (drawn 200ms, `--ease-pen`) — the Annotator marks chapters off as they pass.

**States.** *Rest:* line at current progress, arrow present. *Scrolling:* extends/retracts with direction — scrolling up shortens the line (the Annotator erases nothing; the line simply reflects position — but note the cross-ticks, once drawn at a chapter, remain: you cannot un-read a chapter). *End of page:* arrow lands, and beneath it a tiny pencilled "fin." appears (opacity fade 400ms) — the only place the theme says "fin."

**Content-merge.** The line lives in the same margin, in the same pencil, as the annotations, and its cross-ticks correspond to the chapters the Annotator has actually annotated. It is the margin's own record of the reading.

**Failure fallback.** Without JS, the SVG renders at 0% (empty margin) and the chapter drawer tally is replaced by the static folio furniture ("CH. 3") — no false progress is ever shown. Progress is a nicety; its absence must never look like a bug, so the empty margin is the designed no-JS state.

**Reduced-motion variant.** The line still scrubs (progress is information, and scrubbing is user-driven, not autonomous motion) but the lerp is removed — it tracks 1:1 — and cross-ticks appear instantly. If the user has reduced motion AND the line still distracts, the arrow becomes a simple dot. (This is the theme's one considered exception: user-controlled scrub is retained, smoothed autonomy is removed.)

**Performance budget & mobile.** Budget: one path, `stroke-dashoffset` writes throttled to the shared rAF loop; path length ~leaf height (≤12000 units). Mobile: line moves to the leaf's left edge at 8px width, wobble reduced to 0.5px, arrowhead 10px, "fin." retained.

---

### Element 7 — Coffee-ring fade

**What & why.** Exactly one coffee ring per chapter, fading in last — after the chapter's final note has landed — near that note, slightly overlapping the text block's edge. It is the theme's signature imperfection: proof a human sat here a while. Its power is rationing: one per chapter, always earned by a long chapter's end, never in the hero, never on a form page.

**Structure.** An SVG group of two concentric irregular circles (radii ~46px and ~52px, paths with hand-authored irregularities — a real ring is darker where the cup sat longest, so the stroke has a 40° arc segment at 80% opacity and the rest at 35%), `mix-blend-mode: multiply`, colour `--ring`. Positioned absolutely within the chapter's final passage block, overlapping the reading column's right edge by 12–20px, rotated per chapter from a fixed seed set (7°, −4°, 11°…) so no two chapters share a ring.

**Motion spec.** Fade: opacity 0 → 0.55 over **1400ms**, `--ease-pen`, starting **800ms after the chapter's last margin note completes its entry** — the ring is the last thing to happen in a chapter, the cup set down after the reading. No scale, no draw — a ring does not draw itself; it *develops*, like a stain soaking in. A subtle second phase: the darker arc segment deepens from 70%→80% over the following 3000ms.

**States.** *Absent:* before the chapter's notes complete. *Developing:* fade in progress. *Rest:* permanent for the session; scrolling away and back changes nothing. *Scrolled-past:* unchanged — stains do not animate.

**Content-merge.** The ring sits on the page the reader was actually reading, placed by the layout beside the chapter's final note — the Annotator's cup, next to the Annotator's last word on the chapter. It overlaps the text block edge but is audited to never cover a glyph's x-height zone: placement keeps text legible at 100% zoom with the ring at full strength (multiply on `--page` behind `--ink` text keeps contrast ≥10:1).

**Failure fallback.** The ring is an SVG with default opacity 0.55 in the DOM; the fade is an enhancement applied by adding a `.will-fade` class from JS. No-JS or failure = the ring is simply there, which is its natural state anyway. If the SVG fails to load (inline, so it cannot 404), nothing is missing that content depends on.

**Reduced-motion variant.** Ring present at full rest opacity from the moment the chapter enters; no development phase.

**Performance budget & mobile.** Budget: 2 paths, one opacity animation, zero ongoing cost. Mobile: ring shrinks to ~34px radius and moves to overlap the chapter's closing hairline rule instead of body text (narrow columns cannot spare the overlap).

---

### Element 8 — Self-drawing underlines and circles

**What & why.** The Annotator's basic vocabulary: pencil underlines beneath key phrases and one circled word per section, drawn as real strokes when the paragraph enters. These marks are how the margin's opinions attach to the text — the underline says "this", the circle says "*this* one". One circle per section is a hard ration: circling everything circles nothing.

**Structure.** Inline SVG overlay per paragraph, absolutely positioned, sized to the paragraph box; underline paths are generated at layout from the target phrase's `Range.getClientRects()` (one path per line if the phrase wraps — a wrapped phrase gets a continuous underline per line, each with its own slight sag). Circle: a single elliptical path around the word, drawn with a deliberate 8% overshoot where the pen closes the loop. Stroke: 2px, round caps, `--pencil`, path with 0.6px authored wobble.

**Motion spec.** Draw: `stroke-dashoffset` over **500–800ms** (scaled by path length at ~900 units/second — pen speed, consistent with element 1), `--ease-pen`, triggered when the paragraph crosses the 78% line, sequenced *before* its margin note (the mark lands, then the thought about the mark arrives 500ms later). Circle draws in 650ms with the overshoot segment in the final 15%.

**States.** *Rest:* complete strokes at `--pencil`. *Drawing:* partial stroke with the 2px nib dot leading (shared with element 1's system). *Hover on the phrase:* stroke darkens to `--pencil-deep`, 200ms. *Scrolled-past:* complete and still, forever.

**Content-merge.** The marks are on the words themselves; the phrases chosen are the paragraph's actual load-bearing claims (chosen in copy review, marked in the source as `<mark data-annotator="underline|circle">`). Removing a mark changes what the page emphasises — that is the test of a real annotation.

**Failure fallback.** Paths are complete in the DOM; drawing is a JS-applied dash animation with the standard watchdog (any stroke not finished within 1000ms of trigger snaps to complete). If rect measurement fails (e.g. font swap mid-layout), measurement retries once after `document.fonts.ready`; if it still fails, the underline renders as a straight path under the phrase's first line — an acceptable pencil line, never a missing one.

**Reduced-motion variant.** All marks present, complete, instantly. The nib never appears.

**Performance budget & mobile.** Budget: ≤6 marked phrases per paragraph, ≤14 paths per viewport; rect measurement batched in one layout pass per chapter (no per-paragraph reflow); redraw on resize debounced 200ms and only for the current chapter. Mobile: identical system (marks are in-flow with the text); circle ration unchanged.

---

### Element 9 — Pencil-dust drift

**What & why.** Fine graphite dust motes drift in the hero margin — the air above a desk where someone has been writing and erasing. It is the theme's ambient loop, and it is deliberately *near-imperceptible*: visitors should feel the hero is alive without ever being able to say why. If a visitor notices the dust as an "effect", it is too strong and fails review.

**Structure.** A canvas (or 12–16 absolutely-positioned 2–3px divs — canvas preferred) confined to the hero margin box only (the 240–300px margin column, hero height). Particles: graphite grey `--pencil` at 18–35% opacity, sizes 1.5–3px, soft-edged (radial gradient sprite). No dust exists anywhere else on the page.

**Motion spec.** Each mote: slow drift loop **9000–14000ms** (per-particle period from a fixed seed set), path = gentle sine wander ±14px horizontal, −20px rise then reset, opacity breathing ±8%. No two motes share a period. The system pauses entirely when the hero is off-screen (IntersectionObserver) and when the tab is hidden.

**States.** *Active:* hero in view, motion allowed. *Paused:* hero off-screen or tab hidden — canvas stops drawing (not just visually hidden). *Scrolled-past:* stays paused; returning to the hero resumes.

**Content-merge.** The dust lives only in the margin air above the notes — the Annotator's workspace. It is the by-product of elements 1 and 8 (writing makes dust). Putting dust over the printed text would be a page-wide filter; confining it to the margin keeps it *situated*.

**Failure fallback.** Canvas failure = no dust, nothing else changes. The margin is designed to look complete empty. No-JS: no dust (CSS cannot do this honestly, and a CSS approximation with blurred dots is banned — it reads as dirt on the lens).

**Reduced-motion variant.** Dust removed entirely. This is the first element reduced motion kills, and the hero must be art-directed to feel complete without it.

**Performance budget & mobile.** Budget: one canvas ≤300×700px, ≤16 particles, single rAF shared with §5.0 loop, pixel ratio capped at 1.5. Total frame cost target <0.5ms. Mobile: **disabled** — the margin is collapsed on mobile, so the dust's home does not exist; the tipped-in slip hero note carries the hero alone.

---

### Element 10 — Note-lean hover

**What & why.** Hovering a margin note leans it 2° toward the pointer and darkens its strokes from pencil to ink over 250ms — as if the reader pressed harder on the page, or leaned in to read the hand. It is the theme's primary micro-interaction and the accessibility bridge for pencil contrast (§2): attention literally makes the note legible-dark.

**Structure.** The note element (real text) with a CSS transform (rotate from its assigned base rotation toward the pointer side by up to 2°) and a colour transition on the text and its SVG strokes from `--pencil` to `--ink`. Pointer direction from the note's centre: lean sign = pointer on left/right half. On touch devices, a tap toggles the same state.

**Motion spec.** Lean: **300ms, cubic-bezier(0.34, 1.56, 0.64, 1)** (the sanctioned overshoot, §5.1 — a loose leaf wobbling on its edge). Darkening: **250ms, `--ease-pen`**, colour + stroke colour in sync. Release (pointer leave): 350ms return, same curves — slightly slower out than in, like paper settling back. Focus (keyboard) triggers the identical state without the lean (a focused note darkens and gains a 1px `--blue` underline — blue is the later hand saying "here").

**States.** *Rest:* assigned rotation, `--pencil`. *Hover/tap:* leaned +2° toward pointer, `--ink`. *Focus:* no lean, `--ink`, blue underline. *Active (while tapped on the tick target):* handled by element 11. *Scrolled-past:* rest state; hover still works — old notes can still be leaned on.

**Content-merge.** The response happens in the note's own handwriting pressure — colour and lean of the note itself, no tooltip, no popup card, no elevation shadow (paper does not cast UI shadows; a drop-shadow on hover is slop in this theme).

**Failure fallback.** Pure CSS `:hover`/`:focus-within` implementation — no JS required, so failure mode is "note doesn't lean", which is invisible as a defect. Colour darkening is also CSS. The note is readable (if lighter) without it, and the no-JS/print state uses `--pencil-deep` for all notes to compensate.

**Reduced-motion variant.** Darkening only (250ms colour), no lean, no overshoot.

**Performance budget & mobile.** Budget: transform + colour on one element; zero layout impact (rotation is transform-only, notes have reserved space for the +2° swing — 4px clearance each side). Mobile: tap toggles lean+darken; a second tap elsewhere releases. The tipped-in slip leans within its slip (rotation to −0.5° from −1° base, subtler, because the slip is narrower).

---

### Element 11 — Pencilled-tick click

**What & why.** Clicking a note or a plate draws a small pencilled ✓ beside it — "read, and agreed" — and the tick is **cumulative**: it stays, like a real reader's marks stay. Across a long page, the trail of ticks becomes the visitor's own marginalia; the book gains a third reader. A small tally in the chapter drawer ("your ticks: n") acknowledges the trail without gamifying it.

**Structure.** Per note/plate, an SVG tick slot (18×14px) in the margin immediately left of the note's first line (on plates: bottom-right of the mat). Tick path: two strokes (down-stroke 7px, up-stroke 12px) with the hand's −4° baseline slant. State persisted per session in `sessionStorage` keyed by note id (not localStorage — a borrowed book is returned; ticks are for this reading). The drawer tally is EB Garamond tabular (element per §3.1 data role).

**Motion spec.** Draw: **200ms, `--ease-pen`**, down-stroke 80ms then up-stroke 120ms with the nib dot leading (shared nib system). Tally increments with a 300ms digit roll (the counter vocabulary, §5.1). Clicking a ticked note does **not** untick (a real tick is not erased by touching it) — instead the note leans (element 10) as acknowledgement. A "return the book" reset exists only in the footer colophon ("rub out your ticks" link, which clears sessionStorage and fades all ticks over 400ms — the one eraser in the theme).

**States.** *Unticked:* empty slot (no placeholder outline — an empty box would be a checkbox, and this is not a form). *Drawing:* partial tick. *Ticked:* full tick at `--pencil-deep`. *Session return:* ticks restored instantly at full state, no draw animation (they were already drawn — by you).

**Content-merge.** The tick lands in the margin beside the exact content it endorses, in the same pencil as the Annotator's marks but in *your* hand (slightly different slant, −4° vs the Annotator's note rotations) — the page distinguishes its readers by handwriting, not by UI chrome.

**Failure fallback.** The tick is SVG + class state; failure = no tick, and the click still leans the note (element 10's CSS), so the click never feels dead. Without JS, notes/plates are not clickable and nothing suggests they are (no pointer cursor — the system cursor stays `default` over notes; `pointer` is reserved for links and buttons, per the theme's honesty about what is interactive).

**Reduced-motion variant.** Tick appears complete (150ms fade), tally updates instantly.

**Performance budget & mobile.** Budget: 2 paths per tick, negligible; sessionStorage writes debounced. Mobile: tap target is the whole slip; the tick draws at the slip's top-left; tally lives in the chapter drawer, opened from the folio bar.

---

### Element 12 — Page-turn transition

**What & why.** Navigation inside the book (chapter to chapter, leaf to leaf) turns a page: the leaf's bottom-right corner lifts, and the leaf sweeps across to reveal the next chapter — whose body typesets first and whose notes arrive on their normal half-second-late schedule. It is the theme's page transition, and it obeys the book's own order of events even mid-transition.

**Structure.** A transition overlay cloning the current leaf's visual (screenshot-free: the overlay is a `--page` panel with the deckle mask and a corner-lift gradient, not a bitmap). Corner lift: a triangular clip-path at the bottom-right with a soft shadow gradient suggesting the curl, max lift 120px. The incoming route renders beneath; the sweep is the overlay translating/rotating away leftward like a turned leaf.

**Motion spec.** Total **450ms, `--ease-page`**: corner lift 0→120px over 150ms, leaf sweep (translateX 0→−102% with rotateY hint −6° via perspective on the leaf container) over 300ms, exit shadow fading with it. Trigger: in-book navigation clicks (chapter list, next-chapter link, folio navigation). External links and form submissions never page-turn — leaving the book is not turning its page. The destination's own entrance choreography (settle, notes at +500ms) begins only after the sweep completes.

**States.** *Idle:* no overlay. *Turning:* input on the old leaf is frozen (pointer-events none) for the 450ms; the browser back button during a turn cancels cleanly (overlay removed, no state corruption). *Complete:* overlay removed from DOM (not just hidden).

**Content-merge.** The transition is the book's own leaf turning — the surface that sweeps away *is* the page you were reading (same paper, same deckle), and what it reveals is the next leaf of the same book. No logos, no loaders-as-branding, no unrelated wipe.

**Failure fallback.** If the transition JS fails or the route changes by any other means (back button, deep link), navigation happens instantly with no overlay — a missing page-turn is never a broken page. A hard 600ms watchdog removes the overlay unconditionally, so it can never strand the visitor under a paper panel.

**Reduced-motion variant.** No turn. A 120ms opacity fade of the leaf only (or instant, if the OS asks for no motion at all).

**Performance budget & mobile.** Budget: overlay is transform/opacity only, one element, ≤450ms; the perspective container exists only during the turn (created and destroyed per navigation) so no permanent compositing layer is held. Mobile: the turn becomes a gentler **leaf slide** — the panel slides left over 350ms with the corner lift reduced to 40px (a phone leaf is small; a full curl looks like a bug at 360px wide).

---

### Element 13 — Navigation: the folio bar & chapter drawer

**What & why.** Navigation in a book is not a menu bar; it is the running head, the folio, and the table of contents you flip to. Marginalia's navigation is therefore: a slim **folio bar** at the leaf's top (running head left, current folio centre, "Contents" right) and a **chapter drawer** — the contents list presented as a tipped-in sheet — that opens from it. There is no hamburger, no mega-menu, no sticky glass navbar; chrome that looks like software breaks the leaf.

**Structure.** Folio bar: 48px tall, hairline rule beneath (`--ink` 14%), containing EB Garamond folio-style items (13px uppercase, +0.18em tracking): left = book title / running head; centre = "CH. 3 · LEAF 12" (live, from scroll position); right = "Contents" button + the tick tally (element 11). Chapter drawer: a `--page-deep` sheet, max-width 560px, sliding from the top of the leaf, listing chapters with pencil folio numerals, each chapter row showing its annotation count ("9 notes, 1 ring") in Caveat 20px `--pencil`. The drawer is a `<nav>` with real links; the current chapter's row carries a pencil underline (element 8 stroke, pre-drawn).

**Motion spec.** Drawer open: sheet translates Y −8px→0 + opacity, **350ms, `--ease-settle`**, with its bottom deckle edge visible; chapter rows stagger in at **40ms beats** (folio numeral first, title 20ms later — the contents typeset, then are numbered). Drawer close: 250ms reverse. Folio centre text updates at chapter boundaries with the 200ms crossfade (folio vocabulary). The bar itself never moves, shrinks or gains a shadow on scroll — a running head does not chase you down the page. Trigger: Contents click/tap; Esc closes; focus is trapped in the drawer while open and returned to the Contents button on close.

**States.** *Closed:* bar only. *Open:* drawer sheet over the leaf's top (leaf content dims 8% — paper under a sheet, not a modal scrim; no black overlay anywhere in this theme). *Scrolled:* identical bar; only the centre folio text changes. *Current chapter row:* pencil-underlined; hovered row: title darkens + its folio numeral leans 2° (the hand pointing).

**Content-merge.** The drawer lists the book's actual chapters with the Annotator's own census of them (note counts, the ring's chapter) — navigation that is also a description of the copy. The folio bar's centre is the reader's real position in this book, not a generic breadcrumb.

**Failure fallback.** The drawer is progressive: without JS, the Contents button is an anchor to a contents section at the foot of the leaf (a real contents leaf, element 18's neighbour) listing the same links. The folio bar without JS shows the book title and a static "Contents" link — position text is omitted rather than faked.

**Reduced-motion variant.** Drawer appears with a 150ms fade, no slide, no stagger (rows present). Folio text swaps instantly.

**Performance budget & mobile.** Budget: drawer ≤ 20 rows, transform/opacity only; bar is static layout (no scroll listeners — the folio text updates from the shared chapter-boundary observer). Mobile: the folio bar compresses (running head truncates to the book's short title; centre folio retained — position matters more than branding); the drawer becomes full-leaf-width; tap targets ≥44px (chapter rows are 52px tall — a contents list you flip through with a thumb).

---

### Element 14 — Cards: pasted plates

**What & why.** Marginalia's only card is the **plate**: an image (or a featured excerpt) pasted into the book on a mat, the way photographs were tipped into older books. Plates are the card family — used for gallery items, featured essays with an image, product-as-artifact shots, team portraits in an about leaf. A grid of identical rounded rectangles with drop shadows is the anti-pattern this element exists to prevent.

**Structure.** `<figure class="plate">`: outer mat `--page-deep`, padding 14px; inner image with 6px `--page` inner border and 1px `--page-edge` keyline; square corners everywhere (border-radius: 0 — enforced). Caption beneath in 15px `--ink-soft` with a plate number ("Plate II. The workshop, before the move."). One corner of the mat carries a faint pencil note (Caveat 20px, rotated −2°) — the Annotator has an opinion about most plates. In a grid, plates sit on the §4 rhythm with **alternating mat widths** (full column / 82% column, offset right) so the grid reads as pasted, not tiled.

**Motion spec.** Entry: **plate focus** (§5.1) — blur(3px)+scale(1.04) → sharp/1.00 over **700ms, `--ease-settle`**, at the 80% line; the corner pencil note arrives on the standard +500ms annotation schedule. Hover: **tilt-to-light** — the plate rotates ≤1.2° toward the pointer (rotateX/rotateY from pointer quadrant) over 300ms with the raking-light gradient on its surface shifting in sync, like a page angled to a lamp; caption stays put (only the mat tilts). Click (when the plate is a link): a soft press — scale 0.99, 120ms — then navigation (with element 12's turn if in-book).

**States.** *Rest:* sharp, flat, mat still. *Entering:* focusing. *Hover:* tilted ≤1.2°, surface light shifted. *Focus (keyboard):* keyline darkens to `--pencil-deep` 2px — a pencil box around the plate, never a blue outline (the theme's focus indicator is a drawn box; it must still meet 3:1 contrast against `--page`, which `--pencil-deep` at 2px does at 4.9:1). *Scrolled-past:* rest.

**Content-merge.** A plate is *in* the text flow, numbered in the book's plate sequence, captioned in the book's voice, and annotated by the hand. Its image is evidence for the surrounding passage — the passage refers to it ("see Plate II") and the caption answers. A plate no paragraph refers to is decoration and is cut.

**Failure fallback.** The plate is a plain `<figure><img><figcaption>` — with no JS it is a correctly captioned image on a mat (mat and borders are CSS). The focus reveal is JS/CSS-applied from a pre-blur class; a 1000ms watchdog forces the sharp state, and if the image itself fails to load, the mat remains with the caption and a pencilled "plate missing" note in Caveat — an honest hole, never a broken-image icon.

**Reduced-motion variant.** Plates arrive sharp; hover tilt off (surface light static); corner note pre-written.

**Performance budget & mobile.** Budget: tilt is transform-only on the mat; the light shift is a gradient layer opacity, not a filter; max 6 plates animating focus per page (queue). Images: responsive `srcset`, lazy below the first viewport, aspect-ratio reserved (no layout shift — a pasted plate never jumps). Mobile: plates go full column width (the 82% variant becomes 100%), tilt disabled (no hover), corner note becomes a caption-adjacent line under the caption in Caveat 20px.

---

### Element 15 — Hero: the opening leaf

**What & why.** The hero is the book's opening leaf: the moment a borrowed book falls open at its most-read page. It assembles in the order a reader takes in a page — printed headline first, settling; then the Annotator arrives (element 1's scribble); then the room itself (dust, light). Nothing bounces, nothing shouts. The hero's job is to establish, within 3 seconds, that this page has *two voices* and one of them is alive.

**Structure.** Full first viewport of the leaf: folio bar (element 13) → chapter folio line ("CHAPTER ONE · LEAF 1") → display headline (54px EB Garamond, ≤2 lines, one word pre-marked for element 1's double underline) → first paragraph (the lead, 20px, max 62ch) → hero margin note (element 1, in the margin beside the headline) → optionally one plate (element 14) below the lead paragraph, never beside it (the opening leaf is text-first; an image-led hero is a different theme). Pencil-dust canvas (element 9) lives in the hero margin. A pencilled "begin ↓" — the word "begin" in Caveat with a hand-drawn arrow — sits at the leaf's bottom-right margin edge; it is the scroll cue, and it is the Annotator's, not the UI's.

**Motion spec (the full entrance sequence, timed).**

| Beat | t (ms) | Event |
|---|---|---|
| 0 | 0 | Leaf renders fully readable in static state (no FOUC tricks; animation layers arm) |
| 1 | 120 | Folio bar hairline draws left→right, 400ms, `--ease-pen` (an SVG rule, not a border) |
| 2 | 250 | Headline settles (6px rise + ink 96%→100%), 550ms, `--ease-settle` |
| 3 | 450 | Lead paragraph settles, 550ms |
| 4 | 850 | Hero margin note begins scribbling (element 1: ~90ms/word + lifts; ≤2100ms cap) |
| 5 | note end +250 | Double underline draws beneath the chosen headline word (320ms + 260ms) |
| 6 | 1400 | Pencil dust fades in over 1200ms (element 9) |
| 7 | first scroll | Raking light (element 4) takes over from the hero's static wash |

If the visitor scrolls before beat 4, the scribble triggers immediately on a compressed schedule (pen speed ×1.4, cap 1200ms) — the Annotator hurries, but still writes. If the visitor has already visited this session, beats compress: the note is pre-written (they have seen it written; the book remembers being read).

**States.** *Loading:* element 16's unwritten leaf. *Assembled:* all beats complete; hero is static except dust and light. *Scrolled away/back:* no replay (per element 1); the "begin" arrow fades out permanently after the first scroll past 100px.

**Content-merge.** The hero IS the first page of the content — headline, lead paragraph and annotation are the site's real opening copy, not a marketing banner above the content. There is no separate "hero copy" and "page copy"; a build that writes two openings has misunderstood the theme.

**Failure fallback.** The static state (beat 0) is the complete hero: headline, paragraph, pre-written note, plate. Every beat is an enhancement layered by JS; any failure leaves a composed opening leaf. Watchdogs per element apply.

**Reduced-motion variant.** Beat 0 is the final state: note pre-written, underline drawn, dust absent, light as static wash. The "begin" arrow is present, still.

**Performance budget & mobile.** Budget: total hero animation work ≤ 2.6s wall-clock, no long task >50ms; LCP is the headline text (never an image) and must paint in its final position before beat 2's transform applies (transform-only, no layout shift; CLS = 0 from all hero beats — space for the note is reserved per §4). Mobile: headline 38px; the hero note is the tipped-in slip, pre-written, appearing at beat 3 with a 300ms fade; dust off; the "begin" cue becomes a centred pencilled arrow under the lead paragraph.

---

### Element 16 — Loader: the unwritten leaf

**What & why.** While content loads, Marginalia shows the leaf before writing: the page's own skeleton as an *unwritten leaf* — hairline rules where lines will sit, an empty margin with one faint pencil dot where the first note will land. It is a skeleton screen that belongs to this book instead of to a UI kit, and it teaches the visitor the page's structure (text column, margin) before a single word arrives.

**Structure.** The leaf grid (§4) rendered with: reading column = rows of 1px `--page-edge` rules at the 32.4px rhythm, lengths varying 92% / 100% / 84% / 96% / 61% (a paragraph's silhouette, authored per template, not randomised); margin = one 3px pencil dot at the first note's anchor + two faint 40%-length Caveat-height blank slips; folio bar present in full (navigation is never skeleton — you can always leave a loading book). A slow graphite sheen sweeps the rules: a 120px gradient band moving down the column over **1800ms, `--ease-pen`**, looping with a 600ms rest — like light passing over a blank page, not a shimmer advertisement.

**Motion spec.** Entry: skeleton fades in at 150ms if content is not ready (content arriving faster than 150ms never shows the skeleton — no flash). Content arrival: **book first** — real text replaces rules in one 300ms crossfade per block, top-down at 60ms beats; margin notes then arrive on their live rules (+500ms, element 2) — the skeleton honours the same reading order as the finished page. Maximum skeleton display: if content has not arrived in 4000ms, the sheen stops and a Caveat note fades in in the margin: "the rest of this leaf is still being written…" — an honest loading message in the theme's voice, shown once.

**States.** *Waiting:* sheen looping. *Resolving:* block-by-block ink-in. *Stalled (>4s):* sheen off, margin note shown. *Error:* skeleton is replaced by the error leaf — a real paragraph in EB Garamond explaining the failure + the Annotator's note ("not you. the binding, i think.") + a retry link styled as a folio item. No generic error illustration exists in this theme.

**Content-merge.** The skeleton is the same leaf, same grid, same rhythm — it is the page *before* its content, not a placeholder product. The 4-second note and the error leaf are written in the two voices, so even failure states stay inside the book.

**Failure fallback.** The skeleton is itself the fallback layer; its own failure (JS down) means the server-rendered content simply arrives as HTML — the skeleton is a client-side enhancement for client-fetched content only, and server-rendered pages never depend on it.

**Reduced-motion variant.** Static rules, no sheen; content crossfades at 150ms; the 4-second note still applies.

**Performance budget & mobile.** Budget: skeleton is pure CSS/DOM (≤40 elements), sheen is one transform animation; it must never delay content — content blocks replace skeleton blocks independently as each resolves (no "all or nothing" gate). Mobile: margin column of the skeleton collapses like the live layout (slip silhouettes under paragraph blocks).

---

### Element 17 — Forms: the annotated form

**What & why.** Forms are where borrowed-book warmth usually dies. In Marginalia, a form is a leaf someone must write *in* — so the Annotator switches roles: from critic to the helpful previous reader who left guidance in the margin of the form itself ("use the name on the certificate — they check"). Fields are ruled lines, not boxes; the visitor's own typing is set in EB Garamond, and the Annotator's help is in Caveat beside each field. Crucially, per §1: **the Annotator never argues on a form** — no disputes, no wiggles, no coffee rings. On a form, the hand only helps.

**Structure.** Each field: label in folio style (13px uppercase EB Garamond) above a ruled input — transparent background, no box, a 1px `--ink` 30% bottom rule that is an SVG line (so it can be *drawn*); the visitor's text 20px EB Garamond `--ink`. Help text: one Caveat line (20px, −2°, `--pencil-deep` — deep, not light pencil, because form help must pass contrast) in the margin beside the field on desktop, or directly under the rule on mobile. Validation states: a correctly completed field gets a small pencilled tick (element 11's tick, drawn 200ms) at the rule's right end; an error gets the rule redrawn in `--blue` (never red — §2) with a blue Caveat note stating the fix plainly ("the date wants dd/mm — like 04/11"). The submit control is a folio-style button with a 1px `--ink` border and, on hover, a pencil underline draw (240ms).

**Motion spec.** Field focus: the rule draws itself left→right over **300ms, `--ease-pen`** (from 30% to a full `--ink` line with a 2px nib dot leading) — the line is being ruled for you to write on. Tick on valid: element 11 spec (200ms). Error: rule redraws in blue over 300ms and the blue note slides in on the annotation timing (300ms fade + 8px, not the 500ms literary delay — forms are work, the help is prompt). Submit: the button's text gains a pencilled underline (240ms) and the whole form leaf gets element 12's page-turn only if submission navigates within the book; otherwise a margin note appears: "sent. i've noted the date in the back." (only when true — the note is wired to the real success state).

**States.** *Empty:* 30% rule, help note present. *Focused:* rule drawn full, nib gone, help note darkens to `--ink`. *Filled-valid:* tick present. *Error:* blue rule + blue note; the error is also announced via `aria-live` and the field carries `aria-invalid` — the theme's charm never substitutes for semantics. *Disabled:* rule at 12%, label `--ink-soft`, no help note (a note about a field you cannot use is mockery).

**Content-merge.** The help notes are written against each field's real failure modes (gathered from the form's actual support history or testing), in the margin where a previous user's guidance would be. The tick that confirms your entry is the same tick the reader leaves on passages — one gesture language across reading and writing.

**Failure fallback.** Without JS: standard inputs with visible labels, help text as plain paragraphs, native validation — fully functional, merely un-ruled (rules render as static 1px borders via CSS). All animation is enhancement; no field depends on a drawn state to be usable; error text is server-renderable.

**Reduced-motion variant.** Rules are full lines instantly; ticks and notes fade at 150ms; no nib.

**Performance budget & mobile.** Budget: one SVG line per field, ≤12 fields per leaf without pagination of the form itself; draw animations transform/dash only. Mobile: fields full-width; help notes under rules (20px Caveat, `--pencil-deep`); tap targets: the input's hit area is 52px tall though the rule is 1px (the writing line is generous to thumbs); the tick sits at the rule's right end, 18px.

---

### Element 18 — Footer: the colophon leaf

**What & why.** Every real book ends by telling you how it was made. Marginalia's footer is a **colophon leaf**: the imprint, the setting note, the Annotator's last word, and the binder's strip marquee (§5.1) — plus the practical furniture (links, legal) set as back-matter apparatus, not as a dark software footer. The footer is where the theme proves it was a book all along.

**Structure.** Separated from the last chapter by 6 lines of page and a fleuron rule (a centred pencil-drawn ornament: a short rule, a diamond, a short rule — SVG, draws on entry per element 8's system, 650ms). Then, in one centred column (max 56ch): the colophon paragraph in EB Garamond italic ("Set in EB Garamond and annotated in Caveat. This copy was read once, carefully, and argued with throughout."); the apparatus list (links) in folio style, two columns on desktop; the "rub out your ticks" reset (element 11) as a Caveat line; the legal line in 13px `--ink-soft`; and at the very bottom, the binder's strip — the imprint marquee at 18px/s. The Annotator's final note sits in the margin beside the colophon: the only footer note allowed, and it is the same on every page of a site ("you read the colophon. nobody reads the colophon. — noted, with respect.") — a fixed signature, like a real reader who always signs the back page.

**Motion spec.** Entry: fleuron draws (650ms); colophon paragraph settles (550ms); the final margin note arrives at +500ms (element 2 timing — even at the end, the Annotator is half a second late); marquee runs only while the footer is in view (IntersectionObserver), 18px/s, pausing on hover and when the tab is hidden. Nothing in the footer pins, parallaxes or scrubs — the back page is still.

**States.** *Rest:* complete colophon. *Marquee hover:* paused (a reader stopping the strip with a finger). *Ticks present:* the reset line shows the count ("rub out your 4 ticks"); *no ticks:* the reset line is absent (never offer to erase nothing).

**Content-merge.** The colophon's facts are the site's real facts — the actual typefaces, the actual maker, the actual year — and the final note's joke only works because the visitor really did reach the back page. Legal and links are present in full; charm is layered on apparatus, never instead of it.

**Failure fallback.** Plain semantic `<footer>` with the same text and links; marquee content renders as a static centred line without JS; fleuron is a pre-drawn SVG in the DOM (draw is enhancement, watchdog per element 8).

**Reduced-motion variant.** Marquee static (single centred imprint line, duplicated text removed); fleuron pre-drawn; note present.

**Performance budget & mobile.** Budget: marquee is one translated element, GPU-composited, paused off-screen; footer total ≤ 30 DOM elements beyond links. Mobile: apparatus list single column; marquee speed unchanged (18px/s is already gentle); final note becomes a slip beneath the colophon paragraph.

---

## 7. Page application map

How Marginalia plays out per page type. The system never changes; the *casting* does — which elements lead, which rest.

| Page type | Lead elements | Supporting | Deliberately absent | Notes |
|---|---|---|---|---|
| **Home** | Hero opening leaf (15), self-scribbling note (1), pinned hand in ch. 1 (5) | Full system: light (4), progress (6), dust (9), plates (14) | Forms; more than 3 chapters on the home leaf itself | Home is the book's first chapter, not a brochure above the book. Long home content continues as chapters 2–3 on the same leaf; deeper content links via the chapter drawer (13) with page-turns (12) |
| **Listing / index** (essays, books, recipes, catalogue) | Chapter drawer pattern reused as the index leaf; each listing entry is a passage: title (H2), 2-line printed excerpt, margin note from the Annotator ("start here if you're new") | Folio count-up as entries pass; one plate per 3–4 entries (14); pencil progress (6) | Pinned hand (nothing to sustain); coffee rings except on the final entry's chapter | Entries are never cards in a grid. Filtering, if needed, is a contents-style index ("show: essays · letters · all") set in folio style — the Annotator adds one note explaining the filter ("i've starred the three i'd lend you") and starred entries carry a pencilled asterisk. Sorting changes the leaf, with a 300ms fade of the column only |
| **Detail / article** | The full reading system at maximum density: annotations (2), underlines & circles (8), disputed wiggle (3) where earned, pinned hand (5) per chapter | Light (4), progress (6), one ring per chapter (7), plates (14) inline | Dust (hero margin only — detail pages have no hero margin); marquee except in footer | This is the theme's home turf; a detail page is where the §10 gate is applied most strictly. Author byline is set as printed matter; the Annotator's relationship to the author must be established in the first chapter's notes (fan? editor? the author, older?) and stay consistent site-wide |
| **About** | The Annotator annotates the *author's own claims* — this is where the second voice earns its keep ("'award-winning' — one award. it was a nice one though.") | Hero leaf with a portrait plate (14); idle extra: the about leaf carries TWO rings (the one sanctioned exception — people linger over about pages, and the fiction says the Annotator did too; the second ring is fainter, 0.35, and smaller) | Disputed wiggle (about pages are not where you fact-fight the host; blue corrections only, and gentle) | If the site is a person's, the Annotator's identity should be hinted here and nowhere explained outright — a note like "— and yes, i'll keep writing in your margins. you knew that when you lent me the book." |
| **Contact / checkout equivalent** | Annotated form (17) on a quiet leaf | Folio bar (13); colophon footer (18) | Rings, dust, wiggle, pinned hand, disputes (§1) | The Annotator helps only. Checkout-length flows keep the leaf narrow (reading column only, margin used solely for field help). Confirmation pages get the success margin note from element 17 and a page-turn back into the book |
| **404 / error leaf** | A short printed apology as a chapter fragment ("Leaf not found — it may have been torn out, or never bound in.") + the Annotator's note ("i've checked the margins. it isn't hiding there either.") | Chapter drawer (13) for recovery; skeleton's error pattern (16) shares this voice | Everything animated except the note's +500ms arrival | The error leaf still has folios, the colophon footer, and working navigation — a lost reader is still inside the book |

**Cross-page consistencies (break these and the book falls apart).** The Annotator's handwriting (Caveat weight, rotation habits, vocabulary) is one person across the whole site. The folio numbering is continuous across pages of a site where feasible (a site is one book). The pencil is the same pencil: progress line wobble, underline wobble and tick slant are generated from one seed set per site, so the hand is recognisably the same hand on every leaf.

---

## 8. Worked example — one complete section, end to end

**The section:** Chapter 2 of an author's site, "On Keeping a Commonplace Book" — a passage cluster about why the author copies passages by hand. Built exactly as a builder agent should build it.

**Copy (printed voice, EB Garamond).**
- Folio line: "CHAPTER TWO · LEAF 7"
- H2: "2. On keeping a commonplace book" (the "2." in `--pencil` per §3.1)
- ¶1: "I copy passages by hand because typing lets me pretend I have understood them. The hand is slower than the eye, and in that slowness the sentence has time to object." — the phrase **"the hand is slower than the eye"** is marked `data-annotator="underline"`; the word **"object"** is the section's one circled word.
- ¶2: "A commonplace book is not a diary. Nothing in mine is mine. It is a room I have furnished entirely with other people's chairs, and yet it is the most personal book I own." — the word **"mine"** (second sentence) is the disputed word; its underline is element 3's.
- ¶3: "Keep it ugly. The moment I bought a beautiful notebook I began performing for it, and the entries turned to theatre within a week." — short passage-ender.
- Plate II after ¶2: a photograph of the author's actual commonplace book, captioned "Plate II. The commonplace book, 2019–present. The elastic gave up in 2022."

**Annotations (Annotator's voice, Caveat), anchored and timed.**
- Note A (¶1, right margin, rotation −2°): "this is the whole essay in one line, really. the rest is furniture." — arrives +500ms after ¶1 settles; its author also chose ¶1's underlined phrase (the note and the underline are one thought).
- Note B (¶2, the dispute, rotation −1°): beside the wiggle: "not *nothing* — you wrote the shopping list on p.112. but i take the point." — the Annotator concedes while disputing; the wiggle fires when ¶2 enters, note B lands +500ms later.
- Note C (¶3, blue, rotation −1°, the chapter's one blue note): "the beautiful notebook was the green one. march 2021. i checked." — a factual correction from the later hand, winning quietly.
- Pinned hand: none in this chapter — ¶2 is long but Note B already carries it; per §9, pinning here would duplicate. The chapter *earns* its absence.
- Coffee ring: lands beside Note C, 800ms after Note C completes, overlapping the column edge by 16px, rotation seed 7° — the chapter's last event.

**Sequence on scroll (desktop, motion allowed).** Chapter opener crosses 85% → deckle wipe on the H2 (800ms). ¶1 crosses 78% → settle 550ms → underline draws 620ms → +500ms Note A slides in 500ms. ¶2 enters → settle → circle draws around "object" (from ¶1's marks batch? No — circle belongs to ¶1's sentence; it draws with ¶1's marks, 650ms, sequenced after the underline by the one-hand queue +120ms) → ¶2's disputed underline wiggles 450ms → +500ms Note B. Plate II enters at 80% → focus 700ms → its corner note ("the elastic! a whole era.") +500ms. ¶3 settles → Note C (blue) +500ms → +800ms ring develops 1400ms. Throughout: light band tracks at 55% viewport, lerped 0.12; progress line extends down the outer margin; at the chapter boundary the folio ticks to LEAF 8 and the progress line gets its cross-tick.

**Numbers audit for this section.** Animated events total: 11, never more than 1 at a time (queue). Total SVG paths: 9 (folio rule, 1 underline ×1 line, circle, disputed underline, plate keyline is CSS, fleuron not in this section, tick slots excluded). Long tasks: 0. CLS: 0 (note space reserved; plate aspect-ratio reserved). Words: printed 118, annotations 41 — ratio 0.35, inside the healthy band (§10, item 9).

**Reduced-motion rendering of the same section.** Everything above is present in final state on entry: underlines drawn, circle closed, Notes A–C beside their paragraphs in `--pencil` (with the print/no-JS deepening not needed — screen reduced-motion keeps pencil but the notes are 22px large text), ring at 0.55, plate sharp. The section reads identically; it simply does not perform.

---

## 9. Anti-slop — what makes THIS theme look cheap, and the cure

| # | Cheap failure | Why it happens | The cure (enforceable) |
|---|---|---|---|
| 1 | Margin notes that say nothing ("great point!", "interesting!") | Notes written as decoration after the copy was finished | Every note must pass the *anchor test*: it names, quotes, dates or disputes something in its own paragraph. Notes are written in the same pass as the copy, by the same author, or cut |
| 2 | Notes in a handwriting *font* used as body text, everywhere, at 16px | Caveat treated as a brand font instead of a hand | Caveat appears ONLY as annotations, form help, ticks' companions and the colophon's final note; never below 20px; never for printed content (§3) |
| 3 | Coffee rings sprinkled per section, foxing everywhere, "distressed" texture overlays | Wear used as wallpaper | Hard rations: 1 ring per chapter (About leaf: 2, one faint), 1 foxing spot per 900px, fibres only visible inside the light band. Wear is placed by the layout at chapter ends, never randomised |
| 4 | A red pen | Red imported from generic "editor" imagery | Red does not exist in Marginalia (§2, rule 4). Corrections are blue; emphasis is pencil. Any `#FF0000`-family value in the build fails the gate |
| 5 | Drop shadows and rounded cards "for polish" | UI-kit instincts | Plates are square-cornered mats (§6.14); notes have no shadows; depth comes only from the raking light and paper tones. `border-radius` > 0 on leaf furniture = defect |
| 6 | The wiggle/scribble/tick on *every* element, all the time | Signature moments repeated until they are noise | Rations: 1 circle per section, 1 dispute per chapter max, scribble only hero + chapter openers, pinned hand only where a 60-word note is earned. The queue (§5.0) caps simultaneous events at 1 |
| 7 | A pinned note pinned beside the wrong paragraph, or pinned "because the template pins" | Pin implemented as a section effect, not an annotation | The pin's bracket must mark the exact span the note discusses (§6.5); chapters without an earnable passage ship without a pin (§8 shows an earned absence) |
| 8 | Progress bar styled as a UI component (rounded, gradient, %) | Default component library leaking in | Progress is only ever the pencil line + folio (elements 6, 13). A percentage numeral anywhere in chrome fails the gate |
| 9 | Notes rotated randomly per load, or all at the same −2° | Rotation treated as noise or as a constant | Each note has an authored, fixed rotation in [−3°, −1°] stored in markup; identical rotation on 3+ consecutive notes is flagged in review — a real hand varies, but consistently |
| 10 | The Annotator annotating the price, the checkout or the legal line | The voice applied without judgement | §1 and §6.17 forbid it. On transactional leaves the hand helps or is silent |
| 11 | Generic stock "old paper" background image, different on every page | Texture outsourced | Paper is built from colour + fibre layer + deckle mask (§4), identical on every leaf of a site. A photographic paper texture is banned — it never matches the light system |
| 12 | Animation that hides content when it fails (notes stuck at opacity 0) | Reveal patterns copied from generic sites | The theme's contract: default state is visible; JS adds `.will-animate`; every animation has a named watchdog (§6, per element). A build review must include a JS-disabled pass (§10) |

---

## 10. Quality gate — Marginalia checklist

A build may not use Marginalia until every item passes. Items are checkable, not vibes.

**Identity & palette**
1. Only the §2 tokens (and their stated derivations) appear in the build; zero red-family values; zero new hues.
2. Body text is `--ink` `#2B2620` on `--page` `#EFE6D0` at ≥19px EB Garamond; no sans-serif anywhere, including widgets and banners.
3. Blue appears only as: ≤1 blue note per chapter, form annotations/errors, link hover/focus, focus underline. Counted per page.

**Typography & layout**
4. Type sizes used ⊆ {13, 15, 20, 22, 24, 34, 54}px (plus the 38px mobile display). Reading column ≤62ch; desktop margin ≥240px.
5. Every note's rotation is authored in markup, within −3°…−1°, and no 3 consecutive notes share a rotation.
6. Plates: square corners, mat + keyline present, plate number in caption, and a body paragraph references each plate ("see Plate N").

**Annotations (the soul)**
7. 100% of notes pass the anchor test (§9.1) — sampled by a human reader who did not write them.
8. The Annotator is wrong or corrected at least once per long page (blue note or self-correction present), and never annotates price/checkout/legal.
9. Annotation word count is 20–45% of printed word count per chapter. Below 20% the margin is empty costume; above 45% the hand is shouting over the book.
10. Rations hold: ≤1 circle per section, ≤1 dispute per chapter, 1 ring per chapter (About exception per §7), ≤1 foxing spot per 900px.

**Motion**
11. The one-hand queue is enforced: no two Annotator events animate simultaneously anywhere in the build (test: fast scroll through a full chapter).
12. Every scrubbed value (light, progress, parallax) runs through the single lerped rAF loop (0.12); no scroll listener writes styles directly.
13. Note delay is 500ms after paragraph settle (250ms skim variant); scribble pen speed ≈90ms/word and never exceeds the 2100ms cap.
14. No animation exceeds its §6 duration; total hero sequence ≤2.6s; zero long tasks >50ms during the hero on a mid-range laptop.

**Safety & access (standing rules)**
15. JS disabled: the entire page — text, notes (pre-written), underlines, rings, plates, navigation (via contents leaf) — is present and readable. Verified by an actual JS-off pass, not assumed.
16. Every animated element's watchdog fires: with animations artificially frozen mid-state, all content reaches final state within its named timeout (≤1400ms).
17. `prefers-reduced-motion`: scribble, wiggle, dust, pin, parallax and page-turn are off; notes/marks present in final state; verified with the OS setting on.
18. Keyboard: all interactive elements reachable; focus state is the drawn pencil box / blue underline at ≥3:1; the chapter drawer traps and returns focus; Esc closes it.
19. Pencil text never stands alone below contrast: notes are ≥20px Caveat (large text) at rest, darken to `--ink` on hover/focus, and form help uses `--pencil-deep`.

**Performance**
20. CLS = 0 across load and scroll (note space and plate aspect-ratios reserved). LCP is the headline text.
21. Dust canvas, light overlay and progress line together cost <1ms/frame average; dust pauses off-screen; the rAF loop sleeps at zero scroll velocity.
22. Mobile (<768px): notes are tipped-in slips after their paragraphs; pin, dust and diagonal light are off (vertical light variant on); tap targets ≥44px; the theme still passes items 7–10 in slip form.

**Minimum bar.** Items 1–3, 7, 15–17 are *blocking*: any failure means the build is not Marginalia, whatever it looks like in a screenshot. All other items: at most 2 may be marked "fix scheduled" at ship, and never the same item twice across consecutive releases.

---

*End of expanded theme #2 — Marginalia. Standing rules reminder: normal system cursor only throughout; no reveal may ever hide content permanently; `prefers-reduced-motion` honoured per element; every element above merges with the content it annotates — remove the content and the element must have nothing left to do.*


---

## Part II — Deepening (50x standard)

Part I defined Marginalia: what every element is, how it moves, how it fails safe. Part II does not change a single decision in Part I — same four inks, same two faces, same Annotator. It deepens every element to buildable, testable precision: the millisecond choreography, the full state matrix on desktop and touch, behaviour at each breakpoint, the edge cases a real site will hit, an accessibility spec per element, and the exact tokens each element consumes. Then it completes the theme around the elements: the full component inventory, the copywriting voice, three worked examples with scroll timelines, the full-page choreography map, the page performance budget, and the build order.

Where Part II and Part I could be read as disagreeing, Part II is the refinement and Part I is the intent; a builder implements Part II's numbers.

---

### II.1 Per-element deepening

Each element below adds the same six layers to its Part I spec (§6.1–§6.18): **choreography timeline · state matrix · breakpoints · edge cases & failure modes · accessibility spec · tokens consumed**.

---

#### Element 1 — Self-scribbling margin note (§6.1)

**Choreography timeline** (T0 = hero headline settle completes; a 10-word note shown, per-word times scale with the authored word count):

| Beat | t (ms) | What happens |
|---|---|---|
| T0 − 600 | −600 | Headline settle begins (550ms, `--ease-settle`); note aside already occupies its reserved box at opacity 0 |
| T0 | 0 | Nib dot (r=2, `--pencil`) fades in at the first path's start point, 80ms |
| T0 + 80 | 80 | Word 1 stroke draws, ~90ms ±30% by word length |
| per word | +90 avg | Each following word: 60ms pen-lift gap (nib fades to 40% opacity, lifts 2px), then its stroke at ~90ms/word; long words (>7 letters) +15ms per extra letter |
| T0 + ~1500 | ~1500 | Last word completes (hard cap 2100ms — longer hero notes are split at authoring, never sped up) |
| +150 | ~1650 | Nib fades out over 150ms |
| +250 | ~1750 | Underline stroke 1 draws under the chosen headline word, 320ms, `--ease-pen` |
| +40 | ~1790 | Underline stroke 2 (offset +3px, 60% opacity) draws, 260ms — overlaps stroke 1's tail by 280ms |
| +0 | ~2050 | Note is at rest: rotation fixed, `--pencil`; element hands the viewport to the motion queue (§5.0) |

If the visitor scrolls before T0, the whole timeline compresses: pen speed ×1.4, lift gaps 40ms, cap 1200ms. On a repeat visit in the same session, the timeline is skipped entirely — the note renders pre-written at T0 with a 200ms fade.

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (pre-trigger) | Reserved box, empty; headline fully readable | Same; on <768px the box is the tipped-in slip under the headline |
| Writing | Strokes partial, nib leading; not interactive | Never writes on touch viewports <768px — arrives pre-written (Part I mobile rule) |
| Hover | No hover state of its own; once complete, the note inherits element 10 (lean + darken) | Tap = element 10's toggled lean/darken |
| Focus | The note is not focusable (it is an aside, not a control); its text is reachable by screen reader as static text | Same |
| Active | n/a — no press state; clicking the completed note draws element 11's tick | Same via tap |
| Scrolled-past | Final state, static; never replays on scroll-back | Same |
| Disabled | With JS off or SVG unsupported: the visually-hidden text paragraph is unhidden by the no-JS stylesheet in Caveat, `--pencil-deep` — the note reads as pre-written | Same |

**Breakpoints.** ≥1200px: margin 300px, note 24px Caveat, full scribble. 768–1199px: margin 200–240px, note 22px, scribble retained but path count capped at 10 words per note (split longer notes into two stacked notes, second one pre-written). <768px: slip form, pre-written, no nib, underline pre-drawn; the double underline still targets the real headline word, measured after layout.

**Edge cases & failure modes.** *Slow network / late Caveat:* the scribble does not start until `document.fonts.ready` resolves OR 1200ms elapse, whichever first — if Caveat failed, the note renders in the §3 fallback (EB Garamond italic 19px, `--pencil-deep`) and never scribbles. *Font swap mid-write:* the write is cancelled at the current word boundary and all remaining strokes snap complete — a half-font-swapped word is worse than a finished one. *Headline edited after build:* underline geometry is re-measured on resize and on `fonts.ready`; if the target word no longer exists, the underline is omitted and the note still writes (a note without its underline is a lesser note, not a broken one). *Content shorter than expected:* if the hero has no headline word marked, element 1 does not fire at all — no scribble without something to annotate. *Scroll-back:* no replay, ever (Part I). *Low-power device:* if the device reports `hardwareConcurrency ≤ 2` or frame time during the write exceeds 24ms twice, the write degrades to a 400ms fade of the complete note.

**Accessibility spec.** The SVG is `aria-hidden="true"`; the sibling visually-hidden `<p>` carries the note text and sits in DOM order immediately after the headline it annotates, so a screen-reader user gets headline → annotation in reading order. The note text at rest is `--pencil` at 24px (large text, 3.6:1 — legal only as an enhancement layer); the accessible text is not the SVG, and the print/no-JS state uses `--pencil-deep` (4.9:1). The writing animation is decorative: nothing is communicated by the strokes that is not in the hidden paragraph. No focus interaction; no touch target (the completed note's tick target belongs to element 11, ≥44px).

**Tokens consumed.** `--page`, `--pencil`, `--pencil-deep`, `--ink` (underline rest state after darken), `--ease-pen`, `--pen-speed: 90ms`, `--pen-lift: 60ms`, `--scribble-cap: 2100ms`, `--scribble-cap-fast: 1200ms`, `--nib-r: 2px`, `--note-hero-size: 24px`, `--note-rotate` (authored per note, −1°…−3°), `--watchdog-note: 1400ms`.

---

#### Element 2 — Half-second-late annotations (§6.2)

**Choreography timeline** (T0 = anchored paragraph's settle animation ENDS):

| Beat | t (ms) | What happens |
|---|---|---|
| T0 − 550 | −550 | Paragraph settle runs (550ms, `--ease-settle`); note held at `translateX(18px)`, opacity 0, only if it carries `.will-animate` |
| T0 | 0 | Settle completes; the 500ms reader's pause begins — nothing moves; this stillness is the beat |
| T0 + 500 | 500 | Note entry begins: `translateX(18px) → 0`, opacity 0→1, 500ms, `--ease-pen`; rotation constant at its authored value throughout |
| T0 + 1000 | 1000 | Note at rest in `--pencil`; queue releases (+120ms before any other Annotator event may start) |

Skim variant: if the paragraph settled off-screen (fast scroll), T0 is backdated to when it crossed the 78% line and the delay is 250ms, entry 400ms. If two paragraphs settle within 500ms of each other, their notes do NOT overlap: the queue serialises them, second note's delay extends to first note's completion + 120ms — the Annotator still writes one note at a time.

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (pre-entry) | Visible by default; `.will-animate` state (offset, transparent) exists only after JS arms the observer | Same |
| Entering | Slide + fade per timeline | Slip form: 300ms fade + 8px rise, delay 200ms |
| Hover | Element 10 lean/darken | Tap toggles element 10 state |
| Focus | Notes are not focusable unless tickable (element 11 gives the note `tabindex="0"` + button semantics — then focus = darken to `--ink` + 1px `--blue` underline) | Same |
| Active | n/a (tick handled by element 11) | Same |
| Scrolled-past | Present, static; scrolling up never re-animates | Same |
| Disabled | JS off: note sits beside its paragraph at full opacity — the designed static book | Same |

**Breakpoints.** ≥1200px: margin notes, delay 500ms, entry 500ms. 768–1199px: notes 20px, margin 200px at the low end; delay unchanged (the pause is the theme's rhythm, not a size feature). <768px: tipped-in slips after their paragraph; delay 200ms, entry 300ms fade + 8px rise; slips never slide horizontally (no margin to slide from).

**Edge cases & failure modes.** *Paragraph taller than the viewport:* the note anchors to the paragraph's first baseline and enters when the paragraph's TOP crosses 78% — it does not wait for a 300vh paragraph to "settle"; settle is capped: tall paragraphs are treated as settled 550ms after entry regardless. *Note longer than its paragraph:* the note may extend below the paragraph's last line but must keep a 16.2px (half-line) gap before the next note; if it would collide, the following note's anchor shifts down and its delay counts from its own paragraph — notes never overlap, even if that breaks baseline alignment for one pair. *Content shorter than expected:* a chapter with a single paragraph still gets its note at +500ms; the delay is not shortened for short pages. *Scrolling back up:* notes already entered stay; notes not yet entered (below) arm normally when reached. *Resize during entry:* the entry transform is cancelled and the note snaps to rest — a note caught mid-slide by a rotation/resize looks broken, a snapped note looks intentional. *Slow network:* notes are DOM text rendered with the paragraph; font fallback behaviour per §3 (96% opacity cross-fade, 200ms).

**Accessibility spec.** Notes are `<aside>` elements with `aria-label` only where the note's relationship isn't obvious from position; DOM order places each note immediately after its paragraph so screen-reader order = reading order. Rest contrast: `--pencil` 3.6:1 at 20–24px Caveat = large-text enhancement layer; the same note darkens to `--ink` (12.4:1) on hover/focus, is `--pencil-deep` (4.9:1) in print and no-JS states, and blue corrections are `--blue` (7.1:1) at 20px. The 500ms delay never withholds content from assistive tech — the note is in the accessibility tree from first render, animation or not. Touch target: the note itself is not a target; its tick (element 11) is ≥44px.

**Tokens consumed.** `--pencil`, `--pencil-deep`, `--blue`, `--ink`, `--ease-pen`, `--note-delay: 500ms`, `--note-delay-skim: 250ms`, `--note-delay-mobile: 200ms`, `--note-enter-x: 18px`, `--note-enter-dur: 500ms`, `--queue-gap: 120ms`, `--note-size: 22px`, `--note-gap-min: 16.2px`, `--watchdog-note: 1200ms`.


---

#### Element 3 — Disputed-word underline wiggle (§6.3)

**Choreography timeline** (T0 = the disputed word's paragraph crosses the 78% line):

| Beat | t (ms) | What happens |
|---|---|---|
| T0 | 0 | Paragraph settle begins (550ms); the underline is already a complete path beneath the word |
| T0 + 200 | 200 | Wiggle begins (mid-settle — the disagreement is noticed while the line is still landing): rotation oscillation around the underline's left end |
| T0 + 200–350 | 150 | Oscillation 1: +1.2° → −1.2° |
| T0 + 350–500 | 150 | Oscillation 2: +0.7° → −0.7° |
| T0 + 500–650 | 150 | Oscillation 3: +0.3° → 0°; underline at rest |
| T0 + 1050 | 1050 | Paired margin note lands on element 2's schedule (paragraph settle end + 500ms) and names the dispute |

Total wiggle: 450ms, 3 decaying oscillations, once per session per word. The word itself never moves — only the pencil mark (Part I law).

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Underline still, `--pencil` 2px | Same |
| Wiggling | 450ms decaying oscillation, once | Same (entry-triggered, not hover-triggered) |
| Hover (on the word) | Underline darkens to `--pencil-deep` over 200ms; paired note leans (element 10) | Tap on the word: same darken + paired slip highlights (its left rule deepens to `--pencil-deep`) |
| Focus (word is inside a link or the note is focused) | Darken as hover; focus indicator belongs to the link/note, not the underline | Same |
| Active | n/a | n/a |
| Scrolled-past | Still forever; the session flag prevents any repeat | Same |
| Disabled | Reduced motion or JS off: complete still underline — disagreement fully preserved, shake gone | Same |

**Breakpoints.** ≥1200px and 768–1199px: identical — amplitude ±1.2° is sized for a 20px body word and does not scale. <768px: identical wiggle; the paired note is the slip below the paragraph, and its highlight on tap replaces the lean.

**Edge cases & failure modes.** *The disputed word wraps across lines:* the underline follows the word's line fragment only (element 8's per-line path rule); the wiggle applies to the fragment carrying the word's first syllable. *Two disputed words in one paragraph:* forbidden by the §9 ration (≤1 dispute per chapter, and never two in one paragraph) — if markup contains two, only the first wiggles; the second keeps a still underline and review is flagged. *Word edited out in a CMS update:* no span, no wiggle, no error — the note beside it must be re-anchored in the same edit or it fails §10 item 7 at review. *Scroll-back:* never re-wiggles. *Low-power:* the wiggle is one transform on one path; it is never degraded — cutting it would save nothing measurable.

**Accessibility spec.** Purely decorative emphasis: the dispute's meaning lives in the paired margin note's text, which is in the accessibility tree. The underline SVG is `aria-hidden`. The word is ordinary body text (`--ink`, 12.4:1) in all states; the underline at rest is `--pencil` (3.6:1) as a graphic — it is not the sole carrier of any information, so no contrast obligation attaches, and on hover/focus of the paired note it deepens to `--pencil-deep` (4.9:1). No focus target, no touch target on the word itself.

**Tokens consumed.** `--pencil`, `--pencil-deep`, `--ease-pen`, `--wiggle-amp: 1.2deg`, `--wiggle-dur: 450ms`, `--wiggle-start: 200ms`, `--stroke-w: 2px`.

---

#### Element 4 — Raking reading-light (§6.4)

**Choreography timeline** (continuous scrub — beats are scroll-relative, T0 = scroll start):

| Beat | Timing | What happens |
|---|---|---|
| Scroll begins | frame 0 | rAF loop wakes (it sleeps at 500ms of zero velocity); band target recomputed from scroll position: band centre → 55% of viewport height over the leaf |
| Each frame | ~16ms | Band position lerps toward target at 0.12/frame — the lamp visibly lags a fast scroll by ~8 frames (~130ms) and settles after it; fibre opacity boost recomputed for the ≤3 modulated layers: `boost = clamp(1 − |centre − band| / 300)` |
| Notes in band | +120ms behind body | Margin notes at the same height brighten 120ms after the body text — their §5.1 parallax lag expressed in light |
| Scroll stops | +0ms | Band continues lerping to its final position (~200ms of travel after the last scroll event) |
| Idle | +500ms velocity = 0 | Fibre boost decays to base (0.05) over 800ms; loop sleeps; band holds |
| Keyboard focus moves | ≤300ms | Band re-centres on the focused element (focus mode), overriding the scroll target until the next scroll |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (idle) | Band parked at last position; fibres at base opacity 0.05; foxing at 0.30 | Vertical top-down variant parked; no fibre modulation |
| Scrolling | Band scrubbing, lerped 0.12; fibres to 0.13, foxing to 0.50 inside band | Band translates on Y only, 300px tall |
| Hover | No hover state — the lamp does not respond to the pointer | n/a |
| Focus (keyboard) | Band centres on focused element within 300ms | Same when an external keyboard is used; on-screen keyboard opening re-centres on the focused field |
| Active | n/a | n/a |
| Scrolled-past / at top | Band parks above the leaf's top edge; hero lit by its static wash instead | Same |
| Disabled | No blend-mode support → overlay dropped entirely (feature-detected); reduced motion → fixed 40° wash, no scrub | Same |

**Breakpoints.** ≥1200px: 420px diagonal band at 215°, full fibre + foxing modulation. 768–1199px: band 360px, foxing modulation retained, fibre modulation retained (≤2 layers). <768px: vertical top-down gradient, 300px band, fibre modulation OFF, foxing modulation retained at half strength (0.30 → 0.40).

**Edge cases & failure modes.** *No blend-mode / old browser:* overlay removed, page is a normally lit leaf — legibility never depended on the light (Part I). *Low-power device:* the Part I degradation ladder, made exact — sustained frame time >20ms over 60 frames: step 1, fibre modulation off; step 2, lerp coarsens (band updates every 2nd frame); step 3, band becomes static at the 40° wash (the reduced-motion rendering) until the tab is hidden and reshown. *Very long leaf (book-length article):* the band is positioned relative to the viewport, not the leaf — cost is constant regardless of page length. *Content shorter than one viewport:* band parks centred at 55% and never moves; the page reads as lamp-lit, which is correct. *Scroll-back up:* identical behaviour in reverse; the light has no memory and no direction state. *Print:* overlay excluded from print styles entirely.

**Accessibility spec.** The overlay is `aria-hidden`, `pointer-events: none`, and excluded from the accessibility tree. It may only ADD brightness: every text/background pair on the leaf meets its Part I contrast ratio with the overlay at opacity 0 — verified at gate (§10 item 19 extended: contrast is measured with the light disabled). Focus mode's re-centring is the one functional behaviour: it never moves content, only light, so it cannot disturb focus order or cause motion sickness; under `prefers-reduced-motion` focus re-centring is instant (no 300ms travel). No touch target.

**Tokens consumed.** `--ease-lamp`, `--lerp: 0.12`, `--light-band: 420px` (360px / 300px per breakpoint), `--light-angle: 215deg`, `--light-pos: 55%`, `--light-boost-range: 300px`, `--fibre-base: 0.05`, `--fibre-lit: 0.13`, `--fox-base: 0.30`, `--fox-lit: 0.50`, `--lamp-warm: #FFEDBE` (dark-scheme tint, §2).

---

#### Element 5 — Pinned margin hand (§6.5)

**Choreography timeline** (T0 = covered paragraph's first line crosses 60% viewport height):

| Beat | t (ms) | What happens |
|---|---|---|
| T0 − 400 | −400 | Note sits at its natural margin position, approaching |
| T0 | 0 | Pin engages: note begins its final 12px slide into pinned offset, 400ms, `--ease-settle` |
| T0 + 100 | 100 | Paragraph bracket begins drawing down the reading column beside the covered span, 600ms, `--ease-pen` |
| T0 + 400 | 400 | Note pinned (`position: sticky; top: 18vh`); its underlined phrase deepens to `--pencil-deep` over 200ms |
| Scroll through span | ~100–160vh | Note travels with the reader; bracket fully drawn; no further animation — the pin is a held thought, not a show |
| Span end | 0 | Release: note fades to 60% over 300ms and un-pins as the track ends; bracket fades with it over the same 300ms |
| Next chapter | — | Next keynote note pins only inside its own chapter track; two pins never coexist |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (approaching) | Note in margin flow at its paragraph | Note is a slip in flow (no pin exists <768px) |
| Pinned | Sticky at 18vh, full `--pencil`, underlined phrase `--pencil-deep`, bracket drawn | n/a — pinning disabled |
| Hover | Element 10 lean/darken applies to the pinned note as to any note | n/a |
| Focus | If tickable, focus state per element 11; pinning does not change focus order — the note's DOM position stays at its paragraph | Same (slip form) |
| Active | n/a | n/a |
| Released / scrolled-past | 60% opacity rest state in flow; bracket gone | Slip at full opacity (the 60% released state is a pin artefact; slips don't need it) |
| Disabled | No sticky support / JS off: note in flow beside its paragraph, bracket pre-drawn by CSS state | Same |

**Breakpoints.** ≥1200px: pin as specced, track = the covered span, sticky top 18vh. 768–1199px: pin retained, sticky top 14vh, pin length shortens naturally with the narrower measure (Part I: ~80vh at 768–1023px); bracket 2px retained. <768px: no pin, no bracket — the slip's 2px pencil left rule does the bracket's job.

**Edge cases & failure modes.** *Covered span shorter than 60vh:* the pin still engages but the travel is short — never pad the span or the copy to reach a pin length (Part I forbids it); a short pin reads as a held breath, which is fine. *Covered span extremely long (>200vh):* the note releases at 200vh regardless and re-pins 400ms later if the span continues — a note pinned for an entire screen-length chapter section becomes invisible furniture; the re-pin re-earns attention. *Two chapters' tracks adjacent:* release (300ms fade) completes before the next track's engage line can trigger; the queue enforces a 120ms gap. *Scroll-back up into a released span:* the note re-pins (pinning is positional, not a one-shot animation) but the bracket does NOT redraw — it fades in at 200ms, already complete. *Resize to <768px mid-pin:* sticky is removed by the breakpoint CSS; the note lands in flow at its paragraph with no animation. *Low-power:* sticky is native and free; only the bracket draw is JS/CSS — degradable to pre-drawn with zero loss.

**Accessibility spec.** Pinning is visual only: DOM order never changes, so screen-reader and keyboard order follow the text, not the pin. The bracket SVG is `aria-hidden`. The note is 24px Caveat at `--pencil` (3.6:1, large-text enhancement) with the standard bridges: `--pencil-deep` underlined phrase, darken-to-`--ink` on hover/focus, `--pencil-deep` in print/no-JS. The 60% released state drops the note to ~2.4:1 — permitted only because a released note is past content already passed at full contrast, and it returns to full `--pencil` on hover/focus; a released note must never be the ONLY copy of information (it never is — it annotates adjacent text). No touch target beyond element 11's tick (≥44px).

**Tokens consumed.** `--pencil`, `--pencil-deep`, `--ease-settle`, `--ease-pen`, `--pin-top: 18vh` (14vh mid), `--pin-engage-line: 60%`, `--pin-slide: 12px`, `--pin-slide-dur: 400ms`, `--bracket-draw: 600ms`, `--bracket-w: 2px`, `--pin-release-fade: 300ms`, `--pin-released-opacity: 0.6`, `--pin-max-travel: 200vh`.


---

#### Element 6 — Pencil-line progress (§6.6)

**Choreography timeline** (continuous scrub; beats at chapter boundaries):

| Beat | Timing | What happens |
|---|---|---|
| Every frame (scrolling) | ~16ms | `stroke-dashoffset` written from lerped progress (0.12); arrowhead path repositioned to the line's live end in the same frame — line and arrow are one value, never two animations |
| Chapter boundary crossed | 0ms | Cross-tick draw begins at the line's current end: 200ms, `--ease-pen` |
| +200ms | 200 | Cross-tick complete; chapter-drawer tally ("leaf 3 of 9 · annotated") increments with the §5.1 counter roll, 300ms per digit |
| Scroll up across a boundary | — | Line shortens; cross-ticks already drawn REMAIN (you cannot un-read a chapter); tally does not decrement |
| 100% (leaf end) | 0ms | Arrow lands at the line's foot; "fin." fades in beneath it, 400ms, `--ease-pen` |
| Idle 500ms | — | rAF loop sleeps; line holds |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Line at current progress, arrowhead present, in the margin's outer edge | Line at the leaf's left edge, 8px wide, arrowhead 10px |
| Scrolling | Extends/retracts with direction; ticks persist | Same |
| Hover | None — the line is not a control and shows no pointer affordance (cursor stays `default`) | n/a |
| Focus | Not focusable; reading position is conveyed accessibly by the folio bar text (element 13) | Same |
| Active | n/a | n/a |
| Scrolled-past (at foot) | Line complete, cross-ticks at every chapter, "fin." present | Same |
| Disabled | JS off: SVG renders at 0% — an empty margin is the designed no-JS state; no fake progress is ever painted | Same |

**Breakpoints.** ≥1200px: line in the margin's outer edge, 24px-wide SVG, wobble 1px, arrowhead 14px. 768–1199px: same placement, wobble 0.8px. <768px: line moves to the leaf's left edge at 8px width, wobble 0.5px, arrowhead 10px, "fin." retained at the foot; cross-ticks shorten to 6px (from 10px) to fit the narrower rail.

**Edge cases & failure modes.** *Page shorter than one viewport:* progress is 100% on load; the line renders complete with "fin." — a one-leaf site is a finished book, not a bug. *Content grows after load (lazy chapters appended):* total length is recomputed on the layout pass; the line rescales without a jump cut by re-lerping to the new offset over 300ms. *Scroll-back to top:* line retracts to 0 but chapter cross-ticks remain floating at their positions — deliberate: they read as the Annotator's marks in the margin, and the tally keeps the true count. *Browser find-in-page jumps:* progress snaps via the normal lerp within ~200ms; no special case. *Low-power:* the line is one `stroke-dashoffset` write per frame inside the shared loop — it is the last scrubbed system ever degraded (progress is information); if the loop degrades (element 4 ladder step 2), the line updates every 2nd frame with lerp removed, tracking 1:1.

**Accessibility spec.** The SVG is `aria-hidden="true"`. Reading position is available as real text in two places: the folio bar centre ("CH. 3 · LEAF 12", element 13) and the chapter-drawer tally — both plain text in the accessibility tree, updated at chapter boundaries only (never per-frame, so no live-region chatter; neither is a live region). The line's `--pencil` (3.6:1) is a graphic carrying no unique information. No focus, no touch target.

**Tokens consumed.** `--pencil`, `--pencil-deep` (cross-ticks), `--ease-lamp`, `--ease-pen`, `--lerp: 0.12`, `--progress-wobble: 1px` (0.5px mobile), `--progress-rail-w: 24px` (8px mobile), `--arrow-len: 14px` (10px mobile), `--tick-cross-len: 10px` (6px mobile), `--tick-cross-dur: 200ms`, `--fin-fade: 400ms`.

---

#### Element 7 — Coffee-ring fade (§6.7)

**Choreography timeline** (T0 = the chapter's LAST margin note completes its entry):

| Beat | t (ms) | What happens |
|---|---|---|
| T0 | 0 | Chapter's annotation work is done; the ring is still absent (opacity 0) |
| T0 + 800 | 800 | The pause — the reader finishes the chapter, sets the cup down. Ring fade begins: opacity 0 → 0.55 over 1400ms, `--ease-pen` |
| T0 + 2200 | 2200 | Ring at rest opacity; second phase begins: the 40° dark arc segment deepens 70% → 80% over 3000ms |
| T0 + 5200 | 5200 | Ring fully developed; permanent for the session. Nothing about it ever moves again |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (absent) | Before T0 + 800: not rendered visible (SVG present at opacity 0 only when `.will-fade` is armed) | Same |
| Developing | 1400ms fade + 3000ms arc deepening | Same |
| Hover | No hover state — a stain does not respond | n/a |
| Focus | Not focusable; not in tab order | Same |
| Active | n/a | n/a |
| Scrolled-past | Unchanged, permanent | Same |
| Disabled | JS off: ring present at full rest opacity (its natural state — the fade is the enhancement) | Same |

**Breakpoints.** ≥1200px: radii ~46/52px, overlapping the reading column's right edge by 12–20px, per-chapter rotation from the fixed seed set (7°, −4°, 11°…). 768–1199px: radii scale to ~40/45px, overlap 10–14px. <768px: radius ~34px, repositioned to overlap the chapter's closing hairline rule instead of body text; rotation seeds unchanged.

**Edge cases & failure modes.** *Chapter with no margin notes:* no ring — the ring is earned by the chapter's annotation completing; a note-less chapter has no cup. *Chapter's last note is the pinned hand:* T0 is the pin's RELEASE, not its entry; the ring lands after the release fade (+300ms), i.e. T0 = release end. *Very short chapter (one paragraph):* ring still earned if the chapter has ≥1 note; placement falls back to beside that note. *About leaf exception:* the second ring (0.35 opacity, smaller) follows the same timeline offset by +600ms after the first ring's fade begins, beside the about leaf's final note. *Scroll-back:* stains don't animate; nothing changes. *Text legibility audit:* at every breakpoint the ring's overlap is checked against the text block — multiply blend behind `--ink` text keeps glyph contrast ≥10:1; if a layout change moves text under the ring's dark arc, the ring shifts to the next clear position in its placement set rather than covering the arc over glyphs. *Low-power:* one opacity transition on two paths; never degraded.

**Accessibility spec.** Decorative, `aria-hidden`, no text alternative — the ring communicates nothing (it is evidence of presence, not information). It never reduces text contrast below 10:1 (see edge cases), so it creates no accessibility state to manage. No focus, no target, no motion under reduced-motion (present at rest opacity from chapter entry).

**Tokens consumed.** `--ring` (`#8A7F6A` at 55%, multiply), `--ease-pen`, `--ring-r1: 46px`, `--ring-r2: 52px` (34px mobile), `--ring-opacity: 0.55`, `--ring-delay: 800ms`, `--ring-fade: 1400ms`, `--ring-arc-deepen: 3000ms`, `--ring-overlap: 12–20px`.

---

#### Element 8 — Self-drawing underlines and circles (§6.8)

**Choreography timeline** (T0 = paragraph crosses the 78% line; multiple marks in one paragraph serialise through the §5.0 queue):

| Beat | t (ms) | What happens |
|---|---|---|
| T0 | 0 | Paragraph settle begins; marks are complete paths in the DOM, dash-armed only if JS is live |
| T0 + 550 | 550 | Settle ends; first mark begins drawing: nib dot leads, stroke draws at ~900 units/sec (a 300-unit underline = ~330ms; the 500–800ms band covers typical phrase lengths) |
| Mark end | +0 | Nib pauses at the path end for 60ms (the pen checks its work) |
| +120 | — | Queue gap; next mark in the paragraph begins |
| Circle (when present) | its slot | 650ms total; the final 15% (~100ms) draws the 8% overshoot where the pen closes the loop, slightly faster — the flourish |
| Last mark + 500 | — | The paragraph's margin note arrives (element 2) — mark first, thought second, always |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Complete strokes, `--pencil` 2px | Same |
| Drawing | Partial stroke, nib leading | Same |
| Hover (on the marked phrase) | Stroke darkens to `--pencil-deep`, 200ms | Tap on the phrase: same darken, held 600ms then released (no hover to sustain it) |
| Focus (phrase inside a focused link/note) | Darken as hover | Same |
| Active | n/a | n/a |
| Scrolled-past | Complete and still, forever | Same |
| Disabled | Watchdog: any stroke unfinished 1000ms after trigger snaps complete; JS off = complete strokes | Same |

**Breakpoints.** ≥1200px and 768–1199px: identical system, 2px stroke. <768px: identical; stroke stays 2px (a pencil line does not thin because the page narrowed); circle ration unchanged (≤1 per section at every size).

**Edge cases & failure modes.** *Phrase wraps to 3+ lines:* one path per line, drawn in reading order, each at pen speed, serialised — a 3-line underline takes ~3× a single line and that is correct (the hand really travels). *Font swap after measurement:* rects are re-measured once after `document.fonts.ready`; paths regenerate; if a mark was mid-draw, it snaps complete first, then the new path replaces it whole. *Measurement fails twice:* straight-path fallback under the phrase's first line (Part I) — an acceptable pencil line, never a missing one. *Content longer than expected (a paragraph with 8 marked phrases):* the §6 budget caps at 6 marks per paragraph; marks 7–8 render complete and undrawn (present, not performed) — the ration protects the queue. *Scroll-back:* marks never redraw. *Zoom to 200%:* rects re-measure on resize (debounced 200ms, current chapter only); strokes redraw instantly in final state — zooming is reading, not a performance trigger.

**Accessibility spec.** Marks are `aria-hidden` graphics; the marked phrases are ordinary `--ink` text (12.4:1). Emphasis is never carried by the stroke alone: a circled or underlined phrase that matters is also referred to by its margin note's text. Rest stroke `--pencil` 3.6:1 is a non-text graphic duplicating text emphasis — permitted; on hover/focus it reaches `--pencil-deep` 4.9:1. No focus or touch targets on the marks themselves.

**Tokens consumed.** `--pencil`, `--pencil-deep`, `--ease-pen`, `--stroke-w: 2px`, `--draw-speed: 900 units/s`, `--mark-dur-min: 500ms`, `--mark-dur-max: 800ms`, `--circle-dur: 650ms`, `--circle-overshoot: 8%`, `--stroke-wobble: 0.6px`, `--nib-r: 2px`, `--watchdog-mark: 1000ms`, `--marks-per-para-max: 6`.


---

#### Element 9 — Pencil-dust drift (§6.9)

**Choreography timeline** (ambient — beats are lifecycle events, not a sequence):

| Beat | Timing | What happens |
|---|---|---|
| Hero assembled | beat 6 of element 15 (~1400ms after load) | Dust fades in over 1200ms, motes starting at seeded positions mid-wander (never all at origin — the air was already dusty) |
| Per mote | 9000–14000ms loop | Sine wander ±14px horizontal, −20px rise, reset to base; opacity breathes ±8% around its 18–35% base; no two motes share a period |
| Hero leaves viewport | immediate | Drawing pauses (IntersectionObserver) — canvas stops, not merely hidden |
| Tab hidden | immediate | Paused via the shared loop's visibility handling |
| Hero re-enters | +300ms | Resumes from the exact frozen positions — dust does not restart its life because you scrolled back |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (active) | Drifting in the hero margin box only (240–300px wide, hero height) | Disabled entirely — the margin the dust lives in is collapsed (Part I) |
| Paused | Hero off-screen or tab hidden: canvas frozen, zero draw cost | n/a |
| Hover | None — dust ignores the pointer | n/a |
| Focus | None | n/a |
| Active | n/a | n/a |
| Scrolled-past | Stays paused; resumes on return | n/a |
| Disabled | Canvas unsupported or JS off: no dust, and no substitute — a CSS approximation is banned (Part I: it reads as dirt on the lens) | n/a |

**Breakpoints.** ≥1200px: 16 motes, canvas ≤300×700px, pixel ratio capped 1.5. 768–1199px: 12 motes, canvas = the 200px margin width; wander shrinks to ±10px. <768px: disabled.

**Edge cases & failure modes.** *Low-power device:* dust is the FIRST system cut in the element 4 degradation ladder's spirit — if sustained frame time exceeds 20ms, dust is removed before the light degrades (dust is atmosphere; the light is feedback). *Hero shorter than expected (small laptop, 100vh hero at 640px height):* canvas height clamps to the hero box; mote count scales to 10. *The near-imperceptibility test:* if a reviewer can point at the dust and name it as an effect within 5 seconds of looking at the hero, opacity drops by a third and it is re-tested (§9's standard, enforced as a number: mote opacity ceiling 35%, size ceiling 3px). *Scroll-back:* resumes frozen, per timeline. *Reduced motion:* removed entirely — and the hero is art-directed to feel complete without it (element 15's budget assumes its absence).

**Accessibility spec.** `aria-hidden` canvas, no information, no interaction. It is the theme's most expendable motion: killed first by reduced-motion, first by the performance ladder. Its subtlety is also its accessibility defence — at ≤35% opacity and ≤3px it sits below the threshold of visual-distraction concern for attention-related sensitivities, and it never crosses the reading column.

**Tokens consumed.** `--pencil` (mote colour), `--dust-count: 16` (12 mid / 0 mobile), `--dust-size-max: 3px`, `--dust-opacity-max: 0.35`, `--dust-period-min: 9000ms`, `--dust-period-max: 14000ms`, `--dust-wander-x: 14px`, `--dust-rise: 20px`, `--dust-fade-in: 1200ms`.

---

#### Element 10 — Note-lean hover (§6.10)

**Choreography timeline** (T0 = pointer enters the note / tap / focus):

| Beat | t (ms) | What happens |
|---|---|---|
| T0 | 0 | Lean begins: rotation moves from the note's authored base (−1°…−3°) toward the pointer side by up to +2°, 300ms, `cubic-bezier(0.34, 1.56, 0.64, 1)` — the sanctioned overshoot: the leaf wobbles ~0.3° past its target at ~210ms and settles by 300ms |
| T0 | 0 (parallel) | Darkening begins: text and strokes `--pencil` → `--ink`, 250ms, `--ease-pen` — colour lands 50ms before the lean finishes, so the note is readable-dark just as it stops moving |
| Pointer leaves | 0 | Release: 350ms return on both channels — slower out than in, paper settling back |
| Focus (keyboard) | 0 | Darkening only (250ms) + 1px `--blue` underline fades in under the note's first line, 150ms; no lean (a keyboard reader has no pointer side to lean toward) |
| Tap (touch) | 0 | Lean + darken toggle on; a tap anywhere else, or on another note, releases the previous note (350ms) before the new one leans (300ms) — only one note leans at a time |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Authored rotation, `--pencil` | Same |
| Hover | Leaning ±2° toward pointer half, `--ink` | n/a (no hover) |
| Tap-held | — | Leaning (slip form: rotation eases from −1° base toward −0.5°, subtler in the narrow slip) + `--ink`, until released |
| Focus | `--ink` + 1px `--blue` underline, no lean | Same with external keyboard |
| Active (mid-tap on a tickable note) | Element 11's tick draw runs inside the leaned state | Same |
| Scrolled-past | Rest; hover/focus/tap still fully work on old notes | Same |
| Disabled | No-JS: lean and darken are pure CSS (`:hover`/`:focus-within`) — they survive JS failure; without CSS animation support the colour change is instant, the lean absent | Tap toggle needs JS; without it, notes rest — and the no-JS stylesheet pre-darkens all notes to `--pencil-deep` to compensate |

**Breakpoints.** ≥1200px: full ±2° lean. 768–1199px: lean ±1.5° (the 200px margin gives the swing less clearance; the 4px side clearance rule still holds). <768px: slip lean is a rotation *reduction* (base −1° → −0.5°) + darken; slips never rotate past 0° (a slip tipping forward out of the book reads as a bug at small sizes).

**Edge cases & failure modes.** *Note near the leaf edge:* lean direction is clamped — a note whose swing would cross the leaf edge leans only inward, at half amplitude. *Rapid pointer sweeping across many notes:* each note's release (350ms) is independent; no queue applies (leans are CSS, not Annotator events) — but darkening is capped by the browser to elements actually hovered, so a sweep leaves a fading trail of darkening notes, which reads as a hand brushing the margin and is acceptable. *Two notes leaned at once (touch):* impossible by the toggle rule. *Content longer than expected:* lean clearance (4px each side) is part of the note's reserved box at every length. *Scroll while leaning:* the note scrolls with the page; hover state persists until the pointer exits the moved element — browsers handle this natively; no JS correction is applied (chasing it causes flicker).

**Accessibility spec.** This element IS an accessibility mechanism: it is the bridge that takes `--pencil` notes (3.6:1, large-text) to `--ink` (12.4:1) under attention. Focus state: `--ink` text + 1px `--blue` underline — the underline at `--blue` on `--page` is 7.1:1, well above the 3:1 non-text focus-indicator floor, and the note's text itself is at full body contrast while focused. Keyboard focus reaches tickable notes (element 11) in DOM order; non-tickable notes are not focusable (nothing to do there). The lean is transform-only and vestibular-safe at 2°/300ms; reduced-motion removes it, keeping the 250ms darken (colour change is not motion-sickness relevant, and it carries the legibility function).

**Tokens consumed.** `--pencil`, `--ink`, `--blue`, `--ease-pen`, `--ease-lean: cubic-bezier(0.34, 1.56, 0.64, 1)`, `--lean-angle: 2deg` (1.5deg mid / slip variant −0.5deg), `--lean-dur: 300ms`, `--lean-release: 350ms`, `--darken-dur: 250ms`, `--focus-underline-w: 1px`, `--lean-clearance: 4px`.

---

#### Element 11 — Pencilled-tick click (§6.11)

**Choreography timeline** (T0 = click/tap/Enter on a tickable note or plate):

| Beat | t (ms) | What happens |
|---|---|---|
| T0 | 0 | Nib dot appears at the tick slot (margin, left of the note's first line; plates: mat's bottom-right) |
| T0 + 0–80 | 80 | Down-stroke draws (7px), `--ease-pen` |
| T0 + 80–200 | 120 | Up-stroke draws (12px), nib leading; tick complete at `--pencil-deep`, −4° baseline slant |
| T0 + 200 | 200 | Drawer tally increments: digit roll 300ms (§5.1 counter) — the tally finishes at ~500ms, after the tick itself, so the eye sees cause then record |
| Session write | +0 | `sessionStorage` write (debounced 250ms with any other ticks) keyed by note id |
| Click on a ticked note | — | No un-tick. The note leans (element 10) as acknowledgement; nothing else |
| "Rub out your ticks" (footer) | 0 | All ticks fade over 400ms together; tally rolls back to 0 over 300ms; storage cleared |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (unticked) | Empty slot — no outline, no placeholder (an empty box would be a checkbox) | Same |
| Drawing | Partial tick, nib leading, 200ms | Same |
| Ticked | Full tick at `--pencil-deep`, permanent for the session | Same |
| Hover (unticked note) | Element 10 lean/darken; cursor stays `default` over the note body — `pointer` is reserved for links/buttons (Part I honesty rule); the tick affordance is discovered by the lean + the drawer's tally label, not by a cursor lie | Tap = tick |
| Focus | Note darkens + blue underline (element 10 focus); Enter/Space draws the tick | Same (external keyboard) |
| Active | Mid-draw state above | Same |
| Scrolled-past | Ticks persist and remain visible at rest contrast | Same |
| Disabled | JS off: notes are not clickable and nothing suggests they are; no ticks, no tally (the drawer shows the static folio instead) | Same |

**Breakpoints.** ≥1200px and 768–1199px: tick slot 18×14px in the margin. <768px: the whole slip is the tap target (≥44px tall by construction); the tick draws at the slip's top-left; tally lives in the chapter drawer opened from the folio bar.

**Edge cases & failure modes.** *Session restore:* ticks return instantly at full state with NO draw animation (you drew them; the book remembers) — including after a page-turn navigation within the session. *Storage unavailable (private mode quota/blocked):* ticks still draw and persist for the page view in memory; the tally works; nothing errors visibly — a borrowed book that forgets between leaves is a lesser experience, not a broken one. *Rapid clicking:* the 200ms draw is not interruptible; extra clicks during a draw are ignored (the queue treats the tick as one Annotator event). *Content edited (note ids change):* orphaned stored ticks are ignored silently; the tally counts only ticks whose ids exist on the current page. *Very long page (60+ tickable notes):* tally format stays "your ticks: n" in EB Garamond tabular; no cap, no badge, no celebration state — gamification is slop here (§9). *Scroll-back:* ticks are state, not animation; nothing replays.

**Accessibility spec.** Tickable notes carry button semantics without visual change: `role="button"`, `tabindex="0"`, `aria-pressed` (false → true), `aria-label` naming the action and its object ("Mark this note as read: 'he never actually said this'"). The tick SVG is `aria-hidden` (the state is in `aria-pressed`). Focus visible: element 10's focus state (`--ink` + 1px `--blue` underline, 7.1:1). Touch target: the note's full box on desktop (min-height enforced 44px for tickable notes, even if the note is one line — the extra space is margin air, invisible); on mobile the whole slip. Tally text is plain text, updated at most once per tick (not a live region — it would announce over the reader; a screen-reader user queries it when they open the drawer).

**Tokens consumed.** `--pencil-deep`, `--ease-pen`, `--tick-w: 18px`, `--tick-h: 14px`, `--tick-dur: 200ms`, `--tick-down: 80ms`, `--tick-up: 120ms`, `--tick-slant: -4deg`, `--tally-roll: 300ms`, `--tick-fade-out: 400ms`, `--target-min: 44px`.


---

#### Element 12 — Page-turn transition (§6.12)

**Choreography timeline** (T0 = in-book navigation activated):

| Beat | t (ms) | What happens |
|---|---|---|
| T0 | 0 | Input on the old leaf freezes (`pointer-events: none`); the overlay — a `--page` panel carrying the deckle mask — is created over the current leaf |
| T0 + 0–150 | 150 | Corner lift: bottom-right triangular clip grows to 120px, curl shadow gradient deepening with it, `--ease-page` |
| T0 + 150–450 | 300 | Leaf sweep: overlay translates X 0 → −102% with a rotateY hint to −6° (perspective on the leaf container, created for the turn only); the destination leaf is already rendered beneath, static |
| T0 + 450 | 450 | Overlay removed from the DOM; input unfreezes; destination's own choreography begins (its hero/chapter beats run from their T0) |
| Watchdog | 600 | If anything above has not completed, the overlay is removed unconditionally — a paper panel can never strand the visitor |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (idle) | No overlay in the DOM | Same |
| Turning | Lift + sweep as above; back button cancels cleanly (overlay removed, no state corruption) | Leaf slide: panel slides left over 350ms, corner lift 40px |
| Hover | n/a (input frozen during the 450ms) | n/a |
| Focus | Focus moves to the destination leaf's heading at T0 + 450 (not during the sweep — announcing a page that is still covered is a lie) | Same |
| Active | n/a | n/a |
| Scrolled-past | n/a — transitions have no scroll state | n/a |
| Disabled | JS off / transition failure / external navigation: instant route change, no overlay | Same |

**Breakpoints.** ≥1200px: full turn, lift 120px, sweep 450ms. 768–1199px: lift 80px, sweep 400ms. <768px: leaf slide 350ms, lift 40px, no rotateY (at 360px wide a curl reads as a rendering bug, Part I).

**Edge cases & failure modes.** *Slow network (destination not ready):* the turn does not begin until the destination leaf can render — the old leaf stays live and readable; if the wait exceeds 1000ms, element 16's unwritten leaf appears on the DESTINATION side after a plain instant navigation (never hold a frozen leaf hostage to a slow route). *Back/forward during a turn:* turn cancels, overlay removed, browser state wins. *Rapid double navigation (two chapter clicks 100ms apart):* the second click is ignored until the first turn completes — turns are single-flight. *Deep link / refresh:* no turn (there is no leaf to turn from). *Form submission:* never page-turns (Part I — leaving the book is not turning its page); in-book confirmation navigation may turn. *Low-power:* the turn is one composited element for ≤450ms; if the degradation ladder is at step 3, turns degrade to the reduced-motion fade (120ms).

**Accessibility spec.** During the turn, the destination container carries `aria-busy="true"`; at completion, a visually-hidden live region (`aria-live="polite"`) announces the arrival in the book's terms: "Leaf 12. Chapter Three." Focus lands on the destination's chapter heading (`tabindex="-1"`), never left on a removed element. The sweep is decorative — no information is in the moving panel (it is a blank leaf surface, deliberately not a screenshot of the old page, so nothing readable is dragged across the screen). Reduced motion: 120ms leaf fade or instant. The 450ms duration is below vestibular concern thresholds and the motion is a single lateral sweep with no parallax inside it.

**Tokens consumed.** `--page`, `--page-edge` (deckle mask), `--ease-page`, `--turn-dur: 450ms` (400ms mid / 350ms mobile slide), `--lift-h: 120px` (80px mid / 40px mobile), `--lift-dur: 150ms`, `--sweep-dur: 300ms`, `--turn-tilt: -6deg`, `--watchdog-turn: 600ms`.

---

#### Element 13 — Navigation: folio bar & chapter drawer (§6.13)

**Choreography timeline** (T0 = Contents activated; folio updates are boundary events):

| Beat | t (ms) | What happens |
|---|---|---|
| T0 | 0 | Drawer sheet begins: translateY −8px → 0 + opacity 0 → 1, 350ms, `--ease-settle`; leaf content dims 8% (paper under a sheet, never a black scrim) |
| T0 + 40 × n | per row | Chapter rows stagger at 40ms beats: pencil folio numeral first, title 20ms after the numeral — the contents typeset, then are numbered |
| T0 + ~350 + 40 × rows | — | Last row in; focus is inside the drawer (moved at T0 to the drawer's heading); current chapter row's pencil underline is already drawn (it never animates — it was always there) |
| Close (Esc / Contents / leaf click) | 0 | Reverse at 250ms; focus returns to the Contents button at close end |
| Chapter boundary (reading) | 0 | Folio bar centre text crossfades 200ms ("CH. 2 · LEAF 7" → "CH. 3 · LEAF 8"); nothing else in the bar moves, ever |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (closed) | 48px folio bar: running head left, live folio centre, Contents + tick tally right; hairline rule beneath | Bar compresses: short title left, folio centre retained, Contents right (tally moves into the drawer) |
| Open | Drawer sheet over the leaf top, ≤560px wide, `--page-deep`, deckle bottom edge; rows 52px | Drawer full leaf width; rows 52px |
| Hover (row) | Title darkens to full `--ink`; its folio numeral leans 2° (the hand pointing) | n/a |
| Focus (row) | Pencil box (element 14's focus language): 2px `--pencil-deep` outline drawn around the row, 4.9:1 | Same |
| Active (row press) | 120ms press (opacity 0.85), then element 12's page-turn | Same |
| Scrolled (bar) | Identical bar at every scroll position — no shrink, no shadow, no chasing | Same |
| Disabled | JS off: Contents is an anchor to the contents leaf at the page foot (element 18's neighbour) with the same links; folio centre shows the static chapter title, never a faked position | Same |

**Breakpoints.** ≥1200px: full bar, drawer 560px. 768–1199px: bar full; drawer 480px; running head may truncate to the short title below 900px. <768px: compressed bar per matrix; drawer full-width; the centre folio is the last element ever cut — position matters more than branding (Part I).

**Edge cases & failure modes.** *Very long book (40+ chapters):* the drawer scrolls internally (its own leaf-overflow, styled scrollbar as a thin `--page-edge` rule) — rows beyond the fold are reachable by scroll and by keyboard; the current chapter row is scrolled into view on open. *Chapter with no annotations:* its row shows "0 notes" only if true — the census is real data (Part I); a row never invents a count. *Folio position unknown (JS off / observer failure):* centre shows the chapter title only. A wrong leaf number is worse than none. *Drawer open + page-turn link clicked:* drawer closes instantly (no 250ms reverse) and the turn proceeds — two animations never stack. *Resize across a breakpoint with the drawer open:* drawer re-lays out in place; focus stays on the same row. *Low-power:* drawer is transform/opacity on ≤20 rows; never degraded.

**Accessibility spec.** The bar is a `<header>`-level `<nav aria-label="Book navigation">`; the drawer is `role="dialog"` with `aria-label="Contents"`, focus trapped while open, Esc closes, focus returned (Part I). Chapter rows are real links in a list — keyboard order = visual order. Current chapter row carries `aria-current="page"`. The pencil-box focus indicator is 2px `--pencil-deep` at 4.9:1 (≥3:1 non-text requirement met with margin). Folio centre text is plain text, updated at boundaries only, NOT a live region (position changes would announce over reading). Touch targets: rows 52px, Contents button ≥44px tall.

**Tokens consumed.** `--page`, `--page-deep`, `--page-edge`, `--ink`, `--ink-soft`, `--pencil`, `--pencil-deep`, `--ease-settle`, `--ease-pen`, `--bar-h: 48px`, `--drawer-w: 560px` (480px mid / 100% mobile), `--drawer-dur: 350ms`, `--drawer-close: 250ms`, `--row-h: 52px`, `--row-stagger: 40ms`, `--leaf-dim: 8%`, `--folio-crossfade: 200ms`.

---

#### Element 14 — Cards: pasted plates (§6.14)

**Choreography timeline** (T0 = plate crosses the 80% line):

| Beat | t (ms) | What happens |
|---|---|---|
| T0 | 0 | Plate focus begins: blur(3px) + scale(1.04) inside its mat → blur(0) / scale(1.00), 700ms, `--ease-settle` — the plate angled into the light |
| T0 + 700 | 700 | Plate sharp and flat; queue slot frees |
| T0 + 1200 | 1200 | Corner pencil note arrives (element 2's +500ms after the plate's settle completes at 700) |
| Hover | 0 | Tilt-to-light: mat rotates ≤1.2° toward the pointer quadrant over 300ms; the surface-light gradient shifts in sync; caption stays put |
| Press (linked plate) | 0 | Scale 0.99, 120ms, then navigation (element 12 turn if in-book) |

Focus queue: at most 6 plates may be mid-focus on a page; a 7th plate entering renders sharp immediately (the queue protects frame budget, not the effect's vanity).

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Sharp, flat, on its mat (`--page-deep` 14px, 6px `--page` inner border, 1px `--page-edge` keyline, square corners) | Same, full column width |
| Entering | Focusing (blur/scale) per timeline | Same |
| Hover | Tilt ≤1.2° + surface light shift, 300ms | n/a — tilt disabled (no hover) |
| Focus (keyboard, linked plate) | Keyline darkens to 2px `--pencil-deep` (4.9:1) — a drawn pencil box, never a blue outline | Same |
| Active | Press scale 0.99, 120ms | Same on tap |
| Scrolled-past | Rest | Same |
| Disabled | Image failed: mat + caption remain, a pencilled "plate missing" Caveat note in the mat — an honest hole, never a broken-image icon. JS off: plain captioned figure on the mat | Same |

**Breakpoints.** ≥1200px: plates at column width or the 82% offset-right variant, alternating in grids. 768–1199px: 82% variant becomes 90%; tilt retained. <768px: full column width (82% variant → 100%), tilt off, corner note moves to a caption-adjacent Caveat line under the caption.

**Edge cases & failure modes.** *Slow network / lazy image:* the mat renders at the reserved aspect-ratio from first paint (CLS = 0); the focus animation waits for the image's `load` — a plate never focuses an empty mat; if load exceeds 3000ms, the plate renders sharp when it arrives (no focus performance for a late plate). *Image is portrait vs the mat's landscape reserve:* aspect-ratio is authored per plate in markup, never assumed — a wrong reserve is a build defect caught by the CLS gate. *Content longer than expected (a gallery leaf of 20 plates):* focus queue caps concurrent animation; corner notes keep the +500ms rule but serialise through the queue — a gallery takes its time, plate by plate, like pasting. *Plate no paragraph references:* cut at review (§10 item 6) — the element's failure mode is editorial, and the spec names it. *Scroll-back:* plates never re-focus. *Low-power:* tilt is the first plate behaviour cut (transform on a large element); focus blur is second (blur filters are the expensive part) — plates then arrive sharp with a 300ms fade.

**Accessibility spec.** Plates are `<figure>` with `<figcaption>` carrying the plate number and description; the `<img>` alt text describes the image content (the caption is visible description, alt is the accessible equivalent — they may differ in wording, never in facts). Linked plates: the link wraps the figure with an accessible name from the caption ("Plate II. The workshop, before the move."). Focus indicator: 2px `--pencil-deep` at 4.9:1 (≥3:1). The tilt and focus animations are decorative; the corner note is a real `<aside>` in DOM order after the figure. Touch target for linked plates: the whole mat (≥44px in both dimensions by construction).

**Tokens consumed.** `--page`, `--page-deep`, `--page-edge`, `--ink-soft` (caption), `--pencil-deep` (focus keyline), `--ease-settle`, `--plate-mat: 14px`, `--plate-inner: 6px`, `--plate-focus-dur: 700ms`, `--plate-blur: 3px`, `--plate-scale-from: 1.04`, `--tilt-max: 1.2deg`, `--tilt-dur: 300ms`, `--press-scale: 0.99`, `--plate-queue-max: 6`.


---

#### Element 15 — Hero: the opening leaf (§6.15)

**Choreography timeline** (Part I's beat table, completed with the sub-beats it implies; T0 = first paint of the static leaf):

| Beat | t (ms) | What happens |
|---|---|---|
| 0 | 0 | Leaf renders fully readable in static state; animation layers arm; LCP (the headline) paints in its final position |
| 1 | 120 | Folio bar hairline (SVG rule) draws left → right, 400ms, `--ease-pen` |
| 2 | 250 | Headline settles: 6px rise + ink 96% → 100%, 550ms, `--ease-settle` |
| 3 | 450 | Lead paragraph settles, 550ms (overlaps beat 2's tail by 350ms — book channel, permitted; the one-hand rule binds Annotator events, not the book's own settling) |
| 4 | 850 | Hero note begins scribbling (element 1 timeline: ~90ms/word + 60ms lifts, cap 2100ms) |
| 5 | note end + 250 | Double underline draws under the chosen headline word (320ms + 260ms, overlapping per element 1) |
| 6 | 1400 | Pencil dust fades in over 1200ms (element 9) — starts while the note may still be writing; dust is air, not an Annotator event, so the queue does not bind it |
| 7 | first scroll | Raking light takes over from the static wash; the "begin ↓" cue fades permanently after scroll passes 100px |
| End | ≤2600 | Total wall-clock of all hero animation ≤2.6s; no long task >50ms anywhere in the sequence |

Early scroll compresses beats 4–5 (pen ×1.4, cap 1200ms). Session return compresses everything: note pre-written, underline drawn, beats 1–3 kept (the book still settles — it is the *hand* that doesn't repeat itself).

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (assembled) | Static except dust + light; note written, underline drawn | Assembled with slip note pre-written; no dust |
| Loading | Element 16's unwritten leaf | Same |
| Hover | Per-element (note → element 10; plate if present → element 14) | Tap equivalents |
| Focus | First focusable element is the folio bar's Contents (element 13); the light re-centres on focus (element 4 focus mode) | Same |
| Active | n/a at hero level | n/a |
| Scrolled-past | No replay of any beat on return | Same |
| Disabled | Beat 0 IS the disabled state: headline, lead, pre-written note, plate — the complete hero with zero animation | Same |

**Breakpoints.** ≥1200px: as Part I — 54px display, margin note scribbles, dust on. 768–1199px: display 46px (interpolated between the 54/38 anchors — the one sanctioned off-scale size, display only), note 22px scribbles with the 10-word cap (element 1), dust at 12 motes. <768px: display 38px/1.08, slip note pre-written appearing at beat 3 with a 300ms fade, dust off, "begin" cue centred under the lead paragraph.

**Edge cases & failure modes.** *Slow network (fonts late):* beat 2's settle is transform/opacity on rendered text — it runs on the fallback serif if Garamond is late, and does NOT re-run when the real face swaps (a headline that settles twice looks haunted); the note's scribble waits per element 1's font rule. *Hero copy longer than expected (headline 3 lines):* the headline is capped at 2 lines by the §3 rule — a 3-line display headline is a copy defect, fixed in copy, never by shrinking type below 54/38. *No plate in the hero:* correct and common (Part I: the opening leaf is text-first) — beats are unchanged. *Visitor lands mid-page (anchor deep link):* hero beats are skipped entirely; the note renders pre-written — you do not perform an entrance for someone who arrived in the middle of the book. *Low-power:* beats 1, 4, 5 degrade in order: hairline pre-drawn, note fades complete (400ms), underline pre-drawn; beats 2–3 (cheap transforms) always run unless reduced-motion. *Scroll-back to top:* light returns; nothing replays.

**Accessibility spec.** Reading order is DOM order: folio bar → folio line → headline (the page's single `<h1>`) → lead → note (visually-hidden text sibling per element 1) → plate if present. The "begin ↓" cue is a real anchor link to the first chapter (`href="#chapter-1"`) with the accessible name "Begin reading" — the pencilled arrow is its decoration, `aria-hidden`. All hero text meets Part I contrast without any animation state: headline `--ink` 12.4:1, note per element 1's bridges. No autoplaying motion exceeds 2.6s except the sub-threshold dust; reduced-motion renders beat 0 as final (Part I).

**Tokens consumed.** `--page`, `--ink`, `--pencil`, `--ease-settle`, `--ease-pen`, `--display-size: 54px` (46px mid / 38px mobile), `--hero-beat-1: 120ms`, `--hero-beat-2: 250ms`, `--hero-beat-3: 450ms`, `--hero-beat-4: 850ms`, `--settle-dur: 550ms`, `--settle-rise: 6px`, `--hero-budget: 2600ms`, plus element 1's and element 9's tokens for beats 4–6.

---

#### Element 16 — Loader: the unwritten leaf (§6.16)

**Choreography timeline** (T0 = navigation start / content request):

| Beat | t (ms) | What happens |
|---|---|---|
| T0 + 150 | 150 | If content is not ready, skeleton fades in (150ms). Content arriving before 150ms never shows the skeleton — no flash |
| Waiting | loop | Graphite sheen: a 120px gradient band sweeps down the rule column over 1800ms, `--ease-pen`, then rests 600ms, loops |
| Block resolves | per block | Real content replaces its rules: 300ms crossfade per block, top-down at 60ms beats — book first |
| Notes resolve | +500 after their block | Margin notes arrive on element 2's live rules (the skeleton honours the reading order) |
| T0 + 4000 | 4000 | Stall threshold: sheen stops; a Caveat note fades into the margin (300ms): "the rest of this leaf is still being written…" — once, in a polite live region |
| Error | on failure | Error leaf replaces the skeleton whole (no crossfade — a failure is not a reveal): printed apology paragraph + Annotator's note + retry link |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (waiting) | Leaf grid with ruled lines at the 32.4px rhythm (lengths 92/100/84/96/61%), margin pencil dot at the first note's anchor, folio bar fully live | Margin column collapsed: slip silhouettes under paragraph blocks |
| Resolving | Block-by-block ink-in per timeline | Same |
| Stalled (>4s) | Sheen off, margin Caveat note shown | Note becomes a slip under the first block |
| Hover | Folio bar links fully interactive during load — you can always leave a loading book | Same |
| Focus | Focus is never placed inside the skeleton; if the user tabs, focus goes to the folio bar only | Same |
| Active | n/a | n/a |
| Disabled | JS off / server-rendered page: the skeleton never appears — content arrives as HTML (Part I: the skeleton is a client-fetch enhancement only) | Same |

**Breakpoints.** ≥1200px: full three-zone skeleton. 768–1199px: margin column 200px, dot retained. <768px: single-column skeleton with slip silhouettes; sheen band narrows to 80px.

**Edge cases & failure modes.** *Content arrives in one block after 3.9s:* normal resolution — the stall note never appears (it arms at 4000ms, not before). *Partial failure (text loads, plates fail):* blocks resolve independently; failed plates resolve to element 14's "plate missing" state — the skeleton never waits for images. *Retry after error:* the error leaf's retry re-enters this element's timeline from T0, with the stall note re-armed. *Very fast repeat navigation (cached leaf):* content < 150ms, skeleton never paints — correct. *Low-power:* the sheen is the only loop; on the degradation ladder it stops at step 1 and the rules sit static (a still blank leaf is honest). *Scroll during load:* the skeleton is one leaf tall per pending route; there is nothing to scroll into — the folio bar and footer contents link remain the exits.

**Accessibility spec.** The pending leaf container carries `aria-busy="true"`; the skeleton rules are `aria-hidden` (they are not content and must not be read as lines). The stall note and the error leaf ARE content: the stall note is announced via `aria-live="polite"` once; the error leaf is a real heading + paragraph + link, focus moved to its heading on appearance (`tabindex="-1"`). No focusable element exists inside the skeleton. The sheen is low-contrast graphite on `--page` and stops under reduced-motion (static rules, 150ms content crossfades).

**Tokens consumed.** `--page`, `--page-deep`, `--page-edge`, `--pencil`, `--ink`, `--ease-pen`, `--rhythm: 32.4px`, `--skeleton-in: 150ms`, `--sheen-dur: 1800ms`, `--sheen-rest: 600ms`, `--sheen-w: 120px` (80px mobile), `--ink-in-dur: 300ms`, `--ink-in-beat: 60ms`, `--stall-note-at: 4000ms`.

---

#### Element 17 — Forms: the annotated form (§6.17)

**Choreography timeline** (per field; T0 = field focus):

| Beat | t (ms) | What happens |
|---|---|---|
| T0 | 0 | Rule draw begins: the field's SVG rule draws left → right, 300ms, `--ease-pen`, 2px nib dot leading; rule goes from 30% `--ink` to a full line |
| T0 + 300 | 300 | Rule full; nib gone; the field's help note darkens `--pencil-deep` → `--ink` (200ms overlap tail) |
| Blur with valid value | 0 | Tick draws at the rule's right end (element 11: 80ms + 120ms = 200ms) |
| Blur/submit with error | 0 | Rule redraws in `--blue` over 300ms; blue Caveat note slides in: 300ms fade + 8px rise (prompt — forms are work, not literature; no 500ms delay here); error announced via `aria-live` |
| Correction | 0 | On the first input that makes the value valid: blue rule redraws to `--ink` (300ms), blue note fades out (200ms), tick draws (200ms) — the fix is acknowledged in the same gesture language |
| Submit success | 0 | Button gains its pencilled underline (240ms); if navigation stays in-book, element 12's turn; the success margin note appears wired to the REAL success state: "sent. i've noted the date in the back." |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (empty) | 30% rule, label above (13px folio), help note in the margin at `--pencil-deep` | Help note under the rule; hit area 52px |
| Focus | Rule drawn full (300ms), help note at `--ink` | Same; on-screen keyboard does not shift the rule (the field's box is reserved) |
| Filled-valid | Pencilled tick at the rule's right end | Same |
| Error | `--blue` rule + blue Caveat note with the fix stated plainly; `aria-invalid="true"` | Same |
| Hover (submit) | Pencilled underline draws under the button text, 240ms | n/a |
| Active (submit press) | Button press 120ms (opacity 0.85) + underline completes instantly | Same |
| Scrolled-past | Field states persist (a form is a workspace, not a performance) | Same |
| Disabled (field) | Rule at 12%, label `--ink-soft`, NO help note (Part I: a note about an unusable field is mockery); form-level disabled (submitting): button label gains a pencilled "…" and all fields lock for the request's duration | Same |

**Breakpoints.** ≥1200px: help notes in the margin beside their fields (the margin's one form job). 768–1199px: margin notes retained to 900px; below 900px help notes move under their rules (the 200px margin cannot hold a 20px Caveat line beside a field and stay legible). <768px: notes under rules; fields full-width; tick at the rule's right end, 18px.

**Edge cases & failure modes.** *Slow network (submission hangs):* at 4000ms a margin note appears — "still sending. the post is slow today." — honest, wired to the pending state; at failure, the error pattern (blue note at the form's head: what happened + what to do), and NO entered data is lost. *Server-side errors on fields the client passed:* they render identically to client errors (blue rule + note) and focus moves to the first error field with its note read via `aria-describedby`. *Autofill:* autofilled fields render filled-valid WITHOUT the tick draw (the tick is for the visitor's own writing; a browser's fill gets a static tick if valid). *Content longer than expected (a 20-field form):* the §6 budget caps a leaf at 12 fields — beyond that, the form paginates as separate leaves with page-turns between them, each leaf keeping its own margin help. *Scroll-back / revisit:* values and ticks persist (form state is state, not animation); rules render at their final states instantly. *No JS:* native inputs, visible labels, help as plain paragraphs, native + server validation — fully functional, un-ruled (rules are static 1px CSS borders).

**Accessibility spec.** Every field: a real `<label>` (the folio-styled label IS the label element, not a div), help note connected by `aria-describedby`, error note added to the description and announced `aria-live="polite"`, `aria-invalid` on error. Contrast: visitor text `--ink` 12.4:1; help notes `--pencil-deep` 4.9:1 at 20px (passes AA for normal text — form help is information, so the large-text pencil exemption does NOT apply here; that is why form notes are deep, per Part I); error notes `--blue` 7.1:1. Focus visible: the drawn rule is the focus indicator — a full `--ink` 1px→2px rule under the field plus the nib's absence; measured against `--page` it exceeds 3:1 (12.4:1). Touch targets: input hit area 52px tall though the rule is 1px; the submit button ≥48px tall. Error identification never relies on the blue colour alone — the note's text states the problem and the fix.

**Tokens consumed.** `--ink`, `--ink-soft`, `--pencil-deep`, `--blue`, `--page-deep` (field wells where used), `--ease-pen`, `--rule-rest-opacity: 30%`, `--rule-disabled-opacity: 12%`, `--rule-draw: 300ms`, `--error-note-dur: 300ms`, `--submit-underline: 240ms`, `--field-hit: 52px`, `--fields-per-leaf-max: 12`, plus element 11's tick tokens.

---

#### Element 18 — Footer: the colophon leaf (§6.18)

**Choreography timeline** (T0 = footer crosses the 85% line):

| Beat | t (ms) | What happens |
|---|---|---|
| T0 | 0 | Fleuron rule begins drawing (element 8's system): rule — diamond — rule, 650ms, `--ease-pen` |
| T0 + 200 | 200 | Colophon paragraph settles, 550ms, `--ease-settle` (book channel; overlaps the fleuron's tail) |
| T0 + 750 | 750 | Apparatus list (links) settles in two columns, 400ms, one beat — back matter does not stagger theatrically |
| T0 + 1150 | 1150 | The Annotator's final note arrives at +500ms after the colophon's settle (element 2 timing — even at the end, the hand is half a second late) |
| In view | continuous | Binder's strip marquee runs at 18px/s, only while the footer is in view (IntersectionObserver); pauses on hover and when the tab is hidden |
| Ticks exist | — | The "rub out your ticks" line shows the true count; clicked: all ticks fade over 400ms (element 11) |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Complete colophon: imprint paragraph, apparatus, legal line, marquee | Single-column apparatus; final note as a slip beneath the colophon paragraph |
| Hover (marquee) | Marquee pauses — a finger stopping the strip | Tap pauses/resumes |
| Hover (apparatus link) | Link darkens + `--blue-bright` underline (the one place blue-bright rests in chrome) | n/a |
| Focus (link) | Drawn pencil box, 2px `--pencil-deep` (element 14's focus language) | Same |
| Active | Link press: 120ms opacity 0.85 | Same |
| Scrolled-past | Nothing changes — the back page is still (no pin, no scrub, no parallax in the footer, Part I) | Same |
| Disabled | JS off: marquee content renders as one static centred imprint line; fleuron pre-drawn; note present; all links plain | Same |

**Breakpoints.** ≥1200px: colophon column max 56ch centred; apparatus two columns. 768–1199px: apparatus two columns to 900px, one column below. <768px: single column; marquee speed unchanged (18px/s is already gentle); final note as slip.

**Edge cases & failure modes.** *No ticks this session:* the reset line is ABSENT — never offer to erase nothing (Part I). *Very long apparatus (a big site's footer links):* the list caps at two columns of 8; beyond that, links move to a dedicated contents leaf — the colophon is a page of back matter, not a sitemap dump. *Marquee text too short to loop seamlessly:* the imprint line repeats to at least 2× the strip width before looping; if the imprint is genuinely short, the strip renders static-centred instead (a marquee that stutters is worse than a still line). *Scroll-back into the footer:* marquee resumes from its paused offset; fleuron and note never redraw. *Low-power:* the marquee is one composited translated element, paused off-screen; it is cut to static at degradation step 2. *Print:* the footer prints as a real colophon — marquee prints as its static line; the reset line and final note print (the note in `--pencil-deep`).

**Accessibility spec.** Semantic `<footer>`; apparatus links are a real list with descriptive names (never "click here" — the colophon voice rules in §II.3 apply). The marquee is `aria-hidden` with its full imprint text available as a visually-hidden static line (motion never carries the only copy). The final note is an `<aside>` in DOM order after the colophon paragraph. Focus indicators per element 14's pencil box (2px `--pencil-deep`, 4.9:1). Contrast: legal line `--ink-soft` at 13px is the theme's tightest text — it is held at the 72% opacity floor (≈7:1 at 13px per §2's derivation rules, verified at gate) and never set lighter. Touch targets: apparatus links ≥44px tall rows.

**Tokens consumed.** `--page`, `--ink`, `--ink-soft`, `--pencil`, `--pencil-deep`, `--blue-bright`, `--ease-pen`, `--ease-settle`, `--fleuron-dur: 650ms`, `--colophon-settle: 550ms`, `--marquee-speed: 18px/s`, `--final-note-delay: 500ms`, `--colophon-measure: 56ch`.


---

### II.2 Component inventory — every component, in Marginalia's materials

Part I specced the theme's signature and page-family elements. A real site needs the whole furniture set. Every component below is built from the leaf's own materials — EB Garamond, Caveat, pencil strokes, hairline rules, `--page-deep` recesses. Any component that arrives looking like a UI kit (rounded, shadowed, sans-serif, blue-gradient) fails §10 item 2. The Annotator's presence in components follows one law: **the hand annotates content and helps in forms; it never decorates chrome.**

| Component | Marginalia treatment |
|---|---|
| **Primary button** | Folio style: EB Garamond 13px uppercase, +0.18em tracking, 1px `--ink` border, transparent ground, padding 14px 22px, min-height 48px, square corners. Hover: a pencil underline draws beneath the label (240ms, element 8 stroke). Active: opacity 0.85, 120ms. It reads as a printed instruction on the leaf, not a software control |
| **Secondary / quiet button** | Same folio type, border `--ink` at 30%; hover draws the underline and deepens the border to full `--ink`. Used for "return to contents", "rub out your ticks" (that one is set in Caveat 20px instead — it is the reader's own action, in a hand) |
| **Text link (in body)** | `--ink` with a 1px `--pencil` underline at rest; hover: underline deepens to `--pencil-deep` and the link text stays `--ink`. Visited: underline becomes dashed (a line you have already followed, re-ruled loosely). Links are never blue in body text — blue is the later hand, not the book's apparatus |
| **Text input** | Element 17's ruled field: transparent, 1px rule (30% → drawn full on focus, 300ms), visitor text 20px EB Garamond, hit area 52px |
| **Textarea** | A ruled *area*: 4–6 hairline rules at the 32.4px rhythm on `--page-deep` at 40% — the visitor writes on lined paper. The line count is fixed by the field's expected length; text never scrolls inside a lined area (it grows by adding leaves = the area expands one rhythm line at a time, 200ms) |
| **Select / dropdown** | The closed field is a ruled line with a small pencilled caret (a drawn ∨, SVG, never a glyph). Open: a tipped-in slip (`--page-deep`, deckle bottom edge) listing options in 20px EB Garamond, 44px rows; the chosen option carries a pencilled tick; opens with the drawer's 350ms `--ease-settle` settle, never a pop |
| **Checkbox** | A small pencilled square (14px, 2px stroke, hand-wobble corners — an actual drawn box, because in this book you tick boxes by hand). Checked: element 11's tick draws inside it (200ms). The box is drawn, never a native square with an accent colour |
| **Radio** | A pencilled circle (14px) with a filled pencil dot (a scribbled-in centre, 150ms) when chosen. Groups are set as a contents list — one option per line, folio numerals |
| **Toggle / switch** | Does not exist. A book has no switches. Binary settings are a checkbox (above) or a two-line contents choice ("annotations: shown / hidden") set in folio type with the current state pencil-underlined |
| **Search** | A ruled field (input treatment) labelled "Search this book" with results delivered as a contents leaf: each result is a passage entry (title, folio reference "Ch. 3 · Leaf 12", one-line excerpt with the matched phrase pencil-underlined). No result cards, no thumbnails except a plate where the result IS a plate |
| **Data table** | Set as the book's own tables: EB Garamond 20px, tabular numerals, hairline row rules (`--ink` 14%), header row in folio style (13px uppercase), no zebra striping (paper does not stripe), no boxes. Numbers right-align; the Annotator may add ONE Caveat note to a table's margin if a figure needs a caveat — and only then. Tables wider than 62ch break the theme (§1): redesign the data, not the leaf |
| **Badge / tag** | A pencilled asterisk or a small folio-style label: 13px uppercase in a 1px `--pencil` hand-drawn-rectangle (slightly irregular corners). Used for "annotated", "new leaf", "2nd edition". Never a filled pill; a filled pill is software |
| **Alert — information** | A tipped-in slip at the point of relevance (`--page-deep`, 2px pencil left rule): printed text in EB Garamond + optionally one Caveat line. No icon — the slip's placement is the signal |
| **Alert — success** | Slip + a pencilled tick at its left (element 11). The tick is the whole iconography |
| **Alert — warning** | Slip with the left rule doubled (two pencil strokes) and the key sentence pencil-underlined. Still no colour change — urgency in Marginalia is emphasis, not hue |
| **Alert — error (page level)** | Slip with a `--blue` left rule and a blue Caveat line stating the fix (blue is the correcting hand; §2). Red never appears (Part I §2 rule 4). Form-level errors use element 17 |
| **Pagination** | Folio turns: "← Leaf 11 · **Leaf 12 of 30** · Leaf 13 →" in folio type at the column foot, with element 12's page-turn on navigation. Numbered folios up to 7 shown; beyond that, first / current / last with pencilled ellipses. Never a row of boxed numbers |
| **Modal / dialog** | A tipped-in sheet: `--page-deep` sheet centred on the leaf, deckle bottom edge, leaf dims 8% behind it (element 13's dim — never a black scrim). Settles 350ms `--ease-settle`. Contents set as a short leaf: heading, body, folio-style buttons. Focus trapped; Esc closes; the sheet is the drawer's sibling, not a window |
| **Toast** | A pencilled slip at the leaf's bottom-left margin edge: Caveat 20px, one line ("saved. noted in the back."), arrives on annotation timing (300ms fade + 8px), stays 4000ms, fades 400ms. One at a time; a second toast replaces the first (the hand writes one note at a time). Never top-right, never stacked, never with an icon |
| **Tabs** | A contents index: folio-style labels in a row with a hairline rule beneath; the active tab carries a pencil underline (pre-drawn stroke). Switching crossfades the panel column only (300ms). Tabs are for chapters/sections of one leaf, never for app views |
| **Accordion** | Folded leaves: each item is a passage head with a pencilled + (drawn, rotates to × over 250ms as two strokes — it is a pen mark, not an icon font). Opening: the content settles (550ms) as if the leaf unfolded; only one chapter open at a time in contents contexts |
| **Tooltip** | A margin note in miniature: Caveat 20px on a `--page-deep` slip, appearing 400ms after hover/focus beside the term it glosses — because in Marginalia a tooltip IS an annotation. It never appears on touch (tap the term → the slip inserts in flow). If the gloss matters, it should have been a margin note; tooltips are for terms, not content |
| **Breadcrumb** | The folio line itself: "THE BOOK · CH. 3 · LEAF 12" — position furniture (element 13), not a separate component. A second breadcrumb trail anywhere is duplication |
| **Author / byline block** | Printed matter: name in EB Garamond 20px 500, role/date in folio style beneath, portrait (if any) as a plate (element 14) at 82% width. The Annotator may add one line — on an About leaf, this is where their relationship to the author is hinted (§7) |
| **Blockquote / pull-quote** | Set in EB Garamond italic 24px/1.4 in the reading column with a pencilled bracket down its left side (element 5's bracket, drawn 600ms on entry). Pull-quotes are not enlarged display text with giant quote marks — the bracket is the whole treatment |
| **Code / pre** | Set in the margin's spirit: EB Garamond cannot carry code, so code is set as a *transcription* — a `--page-deep` recessed block, 15px, in the book's mono… Marginalia has no mono face (§3: two faces only). Code blocks are therefore set in EB Garamond 15px with preserved spacing, framed as a pasted transcription slip, and the Annotator's note explains it in words. A site whose content is mostly code should not choose Marginalia (§1) |
| **Horizontal rule / divider** | The fleuron (element 18): rule — diamond — rule, drawn 650ms. Between passages within a chapter: 3 lines of empty page and nothing else (Part I §4) |
| **Lists** | Printed lists: EB Garamond, markers are pencilled folio numerals or a drawn dash; the Annotator's starred items carry a pencilled asterisk in the margin. Nested lists indent by the 48px grid gap, never by bullet-size steps |
| **Video / media embed** | Treated as a plate (element 14): mat, keyline, caption with a plate number, focus reveal on entry; the player chrome inside is the embed's own, but the mat frames it as pasted evidence. Autoplay is banned; a video that moves before it is asked to breaks the leaf's stillness |
| **Skip link** | "Skip to the reading" — visually hidden until focused, then a folio-style button at the leaf's top-left. The theme's accessibility furniture is printed like everything else |
| **Back-to-top** | Does not exist as a floating button. The folio bar is always present and the chapter drawer is one click away; a long leaf's foot carries "↑ to the opening leaf" as a folio-style link with element 12's turn in reverse |
| **Cookie / consent notice** | A tipped-in slip at the leaf foot (toast's sibling, but persistent until answered): one printed sentence + two folio buttons ("understood" / "the details" → a contents leaf). No banner across the top — the opening leaf is never covered |

---

### II.3 Content & copywriting voice rules

Marginalia has two voices and they never swap jobs. **The printed voice** (EB Garamond) is the site itself: calm, literate, first-person where the site is a person's, and it never performs excitement. **The Annotator** (Caveat) is a reader, not a marketer: they explain, date, dispute, endorse and confess — in that order of frequency. Part I §1 gives the Annotator's character; this section gives the enforceable rules for both.

**Headline style (printed voice).**
- Sentence case, always; never uppercase, never title-case-every-word. A headline is a sentence a person wrote, not a banner.
- It makes a claim the margin can react to. If no honest annotation could attach to a headline, the headline is too vague to ship.
- Length: ≤ 12 words for display, ≤ 8 for passage heads. Numbers are written as the book would: folios and counts in figures ("Leaf 12"), quantities in prose as words under ten ("three printings").
- *Do:* "I copy passages by hand because typing lets me pretend I understood them." *Don't:* "Unlock the Power of Handwriting Today!" — exclamation marks do not exist in the printed voice. (The Annotator may use them, sparingly: "yes!! this" is allowed once per chapter at most.)

**Label & button style.**
- Folio labels: 13px uppercase, tracked — but the WORDS are plain and verb-first: "Contents", "Begin reading", "Send the letter". Never "Submit", never "Click here", never "Learn more →" (the arrow is a drawn mark or nothing).
- Button labels state the outcome in the book's terms: "Reserve my copy", "Join the reading list", "Turn to chapter three".
- *Do:* "Save my place" (for a bookmark action — the theme's own metaphor, honestly used). *Don't:* "Save 🚀" — emoji do not exist in this theme, in either voice.

**The Annotator's microcopy (margin voice).**
- Lowercase starts and fragments are allowed; references must be specific ("see p.41", "cf. the march draft"); opinions must be owned ("i think", "no — too easy").
- The Annotator is wrong or corrected at least once per long page (§10 item 8) and concedes gracefully in blue: "not *nothing* — you wrote the shopping list on p.112. but i take the point."
- The Annotator never sells, never writes a call to action, never annotates price, checkout or legal (§1). The closest they come to commerce is testimony: "mum's copy had this underlined too."
- Rationing: annotations run 20–45% of the printed word count per chapter (§10 item 9). A note that could sit beside any paragraph is deleted (§1 anchor test).

**Error voice.** Two registers, by surface:
- *Form errors* (blue hand, element 17): the fix stated plainly, in the second person, with an example. *Do:* "the date wants dd/mm — like 04/11." *Don't:* "Invalid input." / "Error 422." / anything apologising theatrically ("Oops!").
- *Page errors* (printed voice + one note): the book apologises as a book. 404: "Leaf not found — it may have been torn out, or never bound in." + the Annotator: "i've checked the margins. it isn't hiding there either." Load failure: element 16's error leaf ("not you. the binding, i think.").

**Empty-state voice.** An empty state is an unwritten part of the book, and says so in the printed voice with the Annotator's practical line:
- Empty reading list: "No leaves yet. When you save a passage, it will be pressed here." + note: "start with ch. 2. everyone does."
- Empty search: "Nothing in this book matches 'xyz'." + note: "try the word the author would use, not the word the subject uses."
- Empty comments/annotations: "No one has written in this margin yet." + (no Annotator line — the absence IS the point; the hand does not annotate its own absence).

**Success voice.** Printed voice confirms the fact; the Annotator may add one dated, specific line — wired to the real state, never decorative: form sent → "sent. i've noted the date in the back." Saved → "pressed between leaves 12 and 13." (with the true folios). A success message that could appear without the action having happened is banned — every confirmation string is bound to its real success event.

**Loading voice.** Element 16's stall note is the template: "the rest of this leaf is still being written…" — honest, in-voice, shown once at 4000ms, never a spinner with a marketing line.

**Words that do not exist in Marginalia** (either voice): "Oops", "Awesome", "Unlock", "Supercharge", "Seamless", "Leverage" (as a verb), "Solutions", "Delve", any emoji, any exclamation in the printed voice, "Lorem ipsum" anywhere including margin notes (§9 item 1). Finding one in a build is a §10 failure.


---

### II.4 Three worked examples, end to end

One site throughout: an essayist's home and leaves — the same book Part I §8 began. Each example gives the build, then its scroll timeline: what fires, in what order, as the visitor actually moves.

#### Example A — The hero (home leaf, opening)

**Build.** Folio bar (element 13): running head "THE COMMONPLACE BOOKS" left, "LEAF 1" centre, "Contents" + empty tally right. Folio line: "CHAPTER ONE · LEAF 1". Headline (54px): "Essays, read twice — once by me, once by my reader." with the word **"twice"** marked for element 1's double underline. Lead paragraph (118 words printed): why the author republishes old essays with a friend's marginalia intact. Hero note (element 1, 11 words): "he means me. i read them first, with a pencil." One plate below the lead (Plate I — the desk), dust in the margin, "begin ↓" at the bottom-right margin edge.

**Scroll timeline.**

| Scroll | t / trigger | What the visitor sees and feels |
|---|---|---|
| 0% (load) | 0–120ms | The leaf is simply there, readable (beat 0). No spinner, no blank |
| 0% | 120–520ms | The folio hairline draws itself — the book being opened flat |
| 0% | 250–800ms | Headline rises 6px and darkens to full ink; the lead follows at 450ms. Print settling, like a page under a hand |
| 0% | 850–~2300ms | In the margin, the note writes itself word by word, nib leading; then the double underline draws under "twice". The visitor's eye is pulled to the margin and back to the word — the theme's whole argument in one glance-exchange |
| 0% | 1400–2600ms | Dust fades into the margin air; the hero is complete. Total motion 2.6s, none of it blocking reading |
| 0–8% | first scroll | The light takes over from the static wash and begins tracking at 55% viewport; "begin ↓" fades away for good; the progress line puts down its first graphite |
| ~12% | Plate I crosses 80% | The plate focuses (blur → sharp, 700ms); its corner note lands at +500ms ("the desk, before the lamp broke.") — the visitor learns plates behave like paragraphs: evidence first, opinion half a second later |

**Failure rendering.** JS off: headline, lead, the note pre-written in `--pencil-deep`, underline drawn, plate captioned — the same opening leaf, still. Reduced motion: identical, minus dust and the write-in.

#### Example B — Mid-page section (essay leaf, the pinned passage)

**Build.** Chapter 3 of an essay, "What the Pencil Remembers". The chapter's long central passage (¶4, ~340 words) argues that handwriting preserves false starts that typing deletes. It earns the chapter's pinned hand (element 5): a 58-word keynote note — a memory of the author's father crossing out a letter three times — bracketed to ¶4's exact span. ¶5 carries the chapter's one circled word ("erasure") and one underlined phrase; ¶6 ends the chapter and earns its coffee ring. The light, progress line and drawer tally run throughout.

**Scroll timeline.**

| Scroll position | Trigger | What happens |
|---|---|---|
| Chapter opener crosses 85% | deckle wipe | The chapter title reveals through the deckle mask, 800ms; folio bar centre crossfades to "CH. 3 · LEAF 9" (200ms); progress line draws its chapter cross-tick (200ms) |
| ¶1–¶3 pass 78% | settles + notes | Each paragraph settles (550ms); its note lands +500ms; one underline draws in ¶2 (620ms). Rhythm established: text, pause, thought — three times, so the visitor trusts it |
| ¶4 first line crosses 60% | pin engages | The keynote note slides its final 12px (400ms) and pins at 18vh; the bracket draws down ¶4's span (600ms); its underlined phrase deepens. The page's pace changes: now something is *accompanying* the reader |
| ¶4 scrolls (~140vh of travel) | pin holds | The note travels; the light band crosses it 120ms after the text at the same height; no other Annotator event fires in this span — the queue holds notes for ¶4's sub-paragraphs until the pin releases, because one hand cannot hold a thought and scribble simultaneously |
| ¶4 span ends | release | Note fades to 60% and un-pins (300ms); bracket fades with it. A small silence in the margin |
| ¶5 crosses 78% | marks | Settle; the circle draws around "erasure" (650ms, overshoot flourish in the last 100ms); the underlined phrase draws (540ms), queued +120ms; ¶5's note lands +500ms after settle |
| ¶6 (chapter end) settles; its note lands | +800ms | The coffee ring develops beside ¶6's note over 1400ms, arc deepening for 3000ms more. The chapter exhales. Six lines of empty page; the next chapter's folio |

**Numbers audit.** Annotator events in the chapter: 9, never two at once. Pin travel 140vh (inside the 100–160vh band, set by the passage, not padded). Annotation ratio: 212 annotation words / 690 printed = 0.31 ✓ (§10 item 9). Long tasks: 0. The pin's absence of competition is the section's premium quality — restraint, scheduled.

#### Example C — Conversion section (the reading-list leaf)

**Build.** The site's one conversion: "The Sunday Margin" — a weekly letter. The leaf is element 17's annotated form on a quiet page (§7 contact casting): folio bar, a short printed introduction (3 paragraphs, ONE margin note total — the hand is restrained near a decision), then the form: name, email, and a select ("how you read: print / screen / both"), 3 fields, well under the 12-field leaf cap. Help notes: name → "the name you'd want on a bookplate."; email → "one letter a week. the address is never lent on."; select → no note (a note about a preference is noise). Submit: "Join the reading list". Below: the colophon footer (element 18). No rings, no dust, no wiggle, no disputes (§1, §9 item 10).

**Scroll & interaction timeline.**

| Step | Trigger | What happens |
|---|---|---|
| Leaf loads | — | Form renders in its no-JS-complete state first: labels, static rules, help as text. JS then arms the drawn states. Nothing about the form waits for animation |
| Intro ¶ crosses 78% | settle | Printed paragraphs settle; the single margin note lands at +500ms: "i read mine with coffee. you have been warned." — warmth, once, then the hand withdraws |
| Visitor reaches the form | form enters view | Fields at rest: 30% rules, help notes at `--pencil-deep` (4.9:1 — form help is information). The light does not scrub inside the form leaf's field area — a lamp that moves while you write is a distraction; the wash is static here (element 4's focus-mode exception: it centres on the focused field, once, ≤300ms) |
| Focus: email field | T0 | Rule draws full (300ms, nib leading); help note darkens to `--ink`; the field is ready to be written in |
| Types, blurs with "name@exampl" | blur | Rule redraws `--blue` (300ms); blue note slides in (300ms): "that address looks a letter short — like name@example.com?" (the example is generated from the input's shape, never echoing a full address back); `aria-invalid` set; the error is announced politely |
| Corrects and blurs | input valid | Blue redraws to `--ink` (300ms), note fades (200ms), tick draws at the rule's end (200ms). The correction is acknowledged in the same pencil as everything else |
| Submit | press | Button underlines (240ms) and presses; fields lock; if the request hangs past 4000ms, a margin note appears: "still sending. the post is slow today." |
| Success | real response | Page-turn (element 12) to the confirmation leaf: printed "You're on the list." + the wired success note: "sent. i've noted the date in the back." + a pencilled tick beside the confirmation's folio line. If the response is a failure, NO turn: the error leaf pattern, data intact, retry as a folio link |

**Numbers audit.** Fields: 3 (cap 12). Annotator appearances on the whole leaf: 3 (intro note, 2 help notes) + error/success notes when earned. Motion events available to distract from the decision: zero ambient systems run on this leaf (no dust, no marquee until the footer, light static in the field area). The conversion leaf is the theme at its quietest — by design, and measurably so.


---

### II.5 Full-page scroll choreography map

One leaf, top to footer — the home leaf of §II.4's site (hero + two chapters + the reading-list invitation + colophon). Every motion beat in order, with the governing rule: **at most one Annotator event at a time, anywhere, ever (§5.0); the book's settles run on their own quieter channel; the light and the progress line scrub continuously underneath everything.**

| # | Scroll zone | Beat | Visitor sees / feels |
|---|---|---|---|
| 1 | 0% — load | Hero beats 0–6 (element 15) | The book opens: hairline, headline, lead, the hand writing, dust. 2.6s, then stillness |
| 2 | 0–10% | Light takes over; progress line starts; "begin" cue dismisses itself | Scroll acquires a lamp and a pencil — feedback without a single UI widget |
| 3 | ~10% | Plate I focuses; corner note +500ms | Evidence, then opinion — the rhythm taught early |
| 4 | Ch. 1 passages | Settles at 78%, notes at +500ms, one underline drawn | The rhythm repeats until it is trusted: text, pause, thought |
| 5 | Ch. 1 mid | Pinned hand engages at 60% line, bracket draws | Companionship: a long thought held beside a long passage |
| 6 | Ch. 1 end | Pin releases (60% fade); final note lands; +800ms the coffee ring develops (1400ms) | The chapter exhales; a cup set down |
| 7 | Boundary | Progress cross-tick (200ms); folio centre crossfades to LEAF 5; drawer tally rolls | The book keeps its own records, quietly |
| 8 | Ch. 2 opener at 85% | Deckle wipe on the title (800ms) | A new leaf of the same book — the wipe is the page's edge, not a transition effect |
| 9 | Ch. 2 passages | Settles, notes, the chapter's one dispute: underline wiggles (450ms), note concedes in the margin | The argument the theme promised in the hero, delivered mid-book |
| 10 | Ch. 2 plate | Focus (700ms) + corner note | Plates keep passage manners |
| 11 | Ch. 2 end | Blue correction note (the chapter's one blue win); ring develops | The later hand has the last word on the chapter — as established, once |
| 12 | Invitation leaf | The reading-list form, quiet casting (Example C): one intro note, then the hand withdraws; fields rule themselves on focus | The book asks something of the reader, politely, in pencil |
| 13 | Footer at 85% | Fleuron draws (650ms); colophon settles; final note at +500ms; marquee runs only in view | The back page: how the book was made, and the reader who signs it |
| 14 | 100% | Progress arrow lands; "fin." fades in (400ms) | The margin's own full stop |

**Reverse pass (scrolling back to the top).** Nothing replays, nothing un-draws: ticks stay, rings stay, notes rest, the pin re-engages positionally with its bracket fading in complete (element 5), the light and line simply track back. The return journey feels like re-walking a read book — everything is where the reading left it. That asymmetry (performed down, settled up) is the map's most important property.

---

### II.6 Whole-page performance budget

Marginalia's effects are cheap by construction (strokes, gradients, one small canvas); this budget keeps them that way and names what dies first.

**Asset weight (per leaf, compressed).**

| Asset | Budget | Notes |
|---|---|---|
| EB Garamond (400/500/600 + italic, subset) | ≤ 90 KB total | `font-display: swap`; the book must never wait for its own voice |
| Caveat (500/600, subset) | ≤ 45 KB | If Caveat fails, §3's fallback rules apply and scribbles disable — budgeted as a failure mode, not an afterthought |
| CSS (whole theme) | ≤ 28 KB | Includes all §II.2 components |
| JS (whole theme) | ≤ 22 KB | The motion queue, the one rAF loop, observers, tick storage. No framework is required or permitted for the theme layer |
| Hero image (Plate I) | ≤ 120 KB | Responsive `srcset`; plates below the fold lazy, ≤ 90 KB each |
| Total first leaf | ≤ 320 KB | Excluding below-fold plates |

**Frame & task budget.**

| Metric | Budget |
|---|---|
| Animation frame cost (all systems together: light + progress + parallax + dust) | < 1ms average per frame; dust alone < 0.5ms |
| Long tasks during load & hero sequence | 0 tasks > 50ms |
| LCP | The headline text, ≤ 2.0s on a mid-range laptop / Fast 4G; the headline paints in final position before any transform (CLS-safe) |
| CLS | 0 across load, font swap, and scroll (note boxes and plate aspect-ratios reserved, §4/§6.14) |
| INP | ≤ 200ms; the tick draw and lean must never block the main thread (all stroke animation is compositor/CSS or dash-offset writes inside the shared loop) |
| Scroll behaviour | 60fps sustained on a mid-range laptop with the full page; the single lerped rAF loop (0.12) is the only scroll-driven writer |

**Cut order when the budget is exceeded** (the degradation ladder, applied in this order, each step logged in the build's QA notes):
1. Pencil dust (element 9) — removed. Atmosphere dies first.
2. Fibre modulation in the light (element 4) — foxing modulation stays (it is one element).
3. Light lerp coarsens — band updates every 2nd frame; progress line unaffected (information outranks ambience).
4. Plate tilt (element 14) — transform on large elements goes.
5. Plate focus blur — plates arrive sharp with a 300ms fade (blur filters are the cost).
6. Parallax (loose-leaf drift) — notes scroll at 1.0× with the text.
7. Never cut, at any step: the note delays, the scribble, the underlines, the tick, the page-turn, the progress line, any fallback or watchdog. Those are the theme; everything above them on this list is weather.

---

### II.7 Build-order checklist

Build Marginalia in this order. Each step leaves the leaf in a shippable state; motion is layered onto a book that already works.

1. **Tokens first.** Declare every token in Part I §2–§3 and Part II's per-element token lists as CSS variables, including easings (`--ease-settle/-pen/-lamp/-page/-lean`) and durations. Two builders given this file must produce the same values — that is the tokens' job.
2. **The leaf.** Grid (gutter / 62ch column / margin), deckle mask, surround, rhythm (32.4px). Verify the leaf at all three breakpoints with dummy text before anything else exists.
3. **The printed book, static.** Typography, folio bar (element 13 without the drawer), chapters, plates as plain figures, colophon footer as plain text and links. **Gate check: with CSS animations and JS off, this is already a handsome annotated book** — notes pre-written in the margin in `--pencil-deep`, underlines as complete SVG paths.
4. **The Annotator, static.** All notes, marks, rings, ticks' slots placed; rotations authored in markup; the anchor test (§9.1) and rations (§10 items 7–10) reviewed by a human who didn't write them.
5. **Forms.** Element 17 + §II.2 form components, fully functional server-side, native validation — before any rule is drawn by JS.
6. **The motion core.** The §5.0 queue, the single lerped rAF loop, the IntersectionObserver set (78% / 80% / 85% / 60% lines), the watchdog utility (every later element registers its force-final timeout here).
7. **Book-channel motion.** Paragraph settles, plate focus, deckle wipes, folio crossfades.
8. **Annotator motion, in dependency order.** Underlines/circles (8) → half-second-late notes (2) → scribble (1) → wiggle (3) → tick (11) → lean (10) → pinned hand (5) → coffee ring (7). Each with its watchdog wired before the next is started.
9. **Scrubbed systems.** Raking light (4) with its degradation ladder → progress line (6) → parallax drift → dust (9) last, because it is cut first.
10. **Navigation performance.** Chapter drawer (13) → page-turn (12) → loader (16) for client-fetched leaves.
11. **Reduced-motion pass.** `data-motion="reduced"` rendering verified per element: the pre-annotated book, complete. Then the JS-disabled pass (§10 item 15) and the frozen-animation watchdog pass (item 16) — all three are separate, actual test passes, not assumptions.
12. **Accessibility pass.** Focus order walk (folio → content → drawer), focus indicators measured (≥3:1), contrast measured with the light disabled, tick targets measured (≥44px), screen-reader pass over one full chapter (headline → note order, tick `aria-pressed`, drawer dialog behaviour).
13. **Performance pass.** §II.6 budgets measured on a mid-range laptop: asset weights, frame cost with all systems live, CLS across load + full scroll, hero long-task check. Apply the cut ladder if needed and record what was cut.
14. **The §10 gate.** All 22 items, blocking items first. Only now may the theme be used in a build.

---

*End of Part II — the 50x deepening of theme #2, Marginalia. Every v2 layer is present: for all 18 elements — millisecond choreography timelines, full state matrices (desktop + touch), behaviour at ≥1200px / 768–1199px / <768px, edge cases and failure modes, per-element accessibility specs, and the exact tokens consumed; and for the theme — the complete component inventory (§II.2), copywriting voice rules with examples (§II.3), three worked examples with scroll timelines (§II.4), the full-page scroll choreography map (§II.5), the whole-page performance budget with its cut order (§II.6), and the build-order checklist (§II.7). Nothing was redesigned; the book is the same book, specified to the last pencil stroke.*
