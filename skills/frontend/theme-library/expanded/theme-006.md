# Theme 6 — Palimpsest (Expanded, v1 + v2)

Written directly to the full standard: the 10-part structure and per-element
build specs (v1), plus the 50x deepening layers (v2) — per-element
choreography timelines, state matrices, breakpoint behaviour, edge cases,
accessibility specs and token lists; per-theme component inventory,
copywriting voice, three worked examples, a full-page scroll choreography
map, a whole-page performance budget, and a build-order checklist.

The theme's one law, from which everything else follows: **the ghost layer is
real alternate copy** — an older tagline, a founder's first draft, last
decade's catalogue text — never lorem, never texture. If a client cannot
supply genuine earlier text, this theme must not be used (§1, §10).

---

## 1. Concept & world

A palimpsest is a manuscript leaf that was scraped with pumice and a knife,
washed, and written on again — sometimes four or five times across six
centuries. The scraping was never perfect. Under raking light, and now under
multispectral imaging, the erased under-text rises again: a tenth-century
copy of Archimedes beneath a thirteenth-century prayer book, a monastery's
first rule beneath its third. The leaf remembers every version of itself.

This site is that leaf. The surface text is the brand as it speaks today —
clean, current, set with care. Beneath it, at a scribe's slight angle of
−1.5°, lies the under-text: what the brand said before. The founder's
first-draft tagline under the polished one. The 1998 catalogue description
under the 2026 product story. The headmaster's original motto under the
university's rebrand. The visitor reads the present; the visitor who lingers
recovers the past. Attention is the lamp: passages you merely pass stay
quiet, passages you dwell on give up their ghosts.

**The mood** is hush and detective work. Nothing on this leaf shouts. The
pleasure is scholarly — the small electric moment when the grey-violet
under-text sharpens under your gaze and you realise the sentence underneath
is *better* than the one that replaced it, or rawer, or funnier, or the one
the founder wrote at 2 a.m. before the agency arrived. The site trusts the
visitor to lean in.

**Best-fit sites and audiences:**

- **Universities and colleges** with genuine archival depth — a motto that
  changed in 1962, a founding charter, prospectus copy across centuries.
  The audience (alumni, applicants, donors) already believes the past is
  the product.
- **Heritage fashion and craft houses** — labels, mills, and ateliers whose
  old catalogue copy, care instructions, and pattern names survive. The
  under-text is the previous generation's voice selling the same coat.
- **Historical-fiction authors and small literary presses** — the author's
  own earlier drafts beneath the published opening line; the novel's first
  paragraph as it was written before the editor's pencil.
- **Rare-book dealers, archives, and manuscript libraries** — the theme is
  literally their object; a dealer's description of a leaf can carry the
  leaf's own recovered text.
- **Estates, vineyards, and houses with dated documents** — labels and
  ledgers across vintages, provided the documents are real and quoted
  verbatim.

**When NOT to use it:**

- **The client has no earlier text.** This is the fatal one. No old tagline,
  no first draft, no previous catalogue — no theme. Invented "old" copy is
  fraud in this theme's own language, and visitors can smell it (§9.1).
- **Anything that must be scanned at speed** — dashboards, checkout
  funnels, pricing comparison, support documentation. The leaf rewards
  lingering; a visitor in a hurry is being taxed, not served.
- **High-density data** — timetables, specifications, financial tables.
  Strata geometry needs air; dense grids crush the ghost layer into noise.
- **Brands younger than their own website.** A two-year-old startup has no
  under-text. Use a forward-looking theme instead.
- **Regulated content where wording is legally fixed** (medical, financial
  disclosures): alternate historical wording beneath current wording is a
  compliance hazard, not a charm.

**Content prerequisite (blocking):** before design begins, the client
delivers a *strata file*: for every ghosted passage, the surface text and
its genuine under-text, with a date or provenance note ("first draft,
March 2019", "catalogue copy, Autumn 1998"). No strata file, no build.
Roughly one passage in three earns a ghost; a leaf where everything is
ghosted is a leaf where nothing is (§9.3).

---

## 2. Palette

Four anchor inks from the original theme, plus derived tokens — each marked
**derived** — mixed only from the anchors, and one gilt token for the flecks
the original motion system already specifies. Nothing else may be
introduced; a fifth hue is a different theme.

| Token | Hex | Role | Usage ratio | Pairing & contrast |
|---|---|---|---|---|
| `--parchment` | `#E4D5B2` | The leaf itself — page surface, card ground | ~62% of pixels | Ground for `--ink` (7.5:1, AAA) and `--rubric` (5.6:1, AA) |
| `--parchment-deep` *(derived)* | `#D8C69C` | Leaf edges, arch frame fills, skeleton leaves, table row bands | ~14% | Under `--ink` 5.9:1 — apparatus and large text only |
| `--ink` | `#4A3A28` | Surface text — the current voice, headings and body | ~13% | On `--parchment` 7.5:1 (AAA body); on `--parchment-deep` 5.9:1 (AA) |
| `--ink-soft` *(derived)* | `#6B5A44` | Captions, folios, secondary apparatus | ~4% | On `--parchment` 4.5:1 — AA for normal text at ≥15px, never below |
| `--rubric` | `#8E2F22` | Rubrication — initials, seals, the one accent gesture per leaf | ≤5% | On `--parchment` 5.6:1 — initials and short labels; never body text |
| `--rubric-bright` *(derived)* | `#A93B28` | The flare peak of a rubric initial mid-animation; seal hover | <1%, transient | Animation state only; never a resting colour |
| `--ghost` | `#7A7285` | Under-text ink — ghosts only, nothing else | ~2% effective (low opacity) | 3.2:1 at full strength on parchment — deliberately sub-AA: ghost text is recovered artefact, never essential content (§6 accessibility law) |
| `--ghost-strong` *(derived)* | `#655C73` | Ghost ink at linger peak, where the under-text must be *readable as a quotation* | <1% | At 0.55 opacity over parchment ≈ 2.6:1 effective — still artefact-grade; any ghost passage a visitor must read is *also* available as surface text in the transcription panel (§6.17) |
| `--gold` | `#B08D3E` | Gilt — progress flecks, arch keystones, hairline rules | <1% | Decorative only; never text |
| `--gold-bright` *(derived)* | `#D9B45C` | Fleck twinkle peak as the raking light passes | <1%, transient | Animation state only |

**Usage law.** Parchment and ink do the work; rubric is rationed to one
gesture per leaf (an initial, a seal, a stamp — pick one); ghost-violet
appears *only* as under-text, so its colour alone signals "this is the
past"; gold appears only in the margin apparatus. A visitor should be able
to identify the theme from a screenshot with all text removed: warm leaf,
brown ink, one red gesture, violet ghosts at an angle.

**Dark-mode behaviour — the candlelit reading room.** A palimpsest does not
invert; it is read by different light. Under `prefers-color-scheme: dark`
the tokens remap, they do not flip: `--parchment` → `#251C11` (a leaf in a
dark room), `--parchment-deep` → `#171208`, `--ink` → `#E4D5B2` (the
surface text takes the parchment's own colour, as lamplight makes the leaf
the lightest thing present), `--ink-soft` → `#B8A67F`, `--rubric` →
`#C05A44` (5.1:1 on the dark leaf), `--ghost` → `#8E86A0`, `--gold`
unchanged. The raking light (§6.2) becomes warmer and narrower — a lamp,
not a window. Sites that cannot maintain the remap may ship light-only, but
must then declare `color-scheme: light` honestly rather than letting the
browser force-darken the leaf into mud.

**Texture.** The parchment grain is CSS, not an image: two layered
`repeating-linear-gradient` fibres at 0.03 opacity plus an inline SVG
`feTurbulence` data-URI at 0.05 — total texture cost under 2KB, no network
request. Foxing spots and edge darkening are radial-gradients baked into
the leaf component, never per-section hand-placed images.

---

## 3. Typography

Two faces, both from the original theme, and a third role played by the
first face in italic. No sans anywhere on the leaf — a sans-serif caption on
a palimpsest is a Post-it note on a cathedral door.

- **IM Fell English** — display, headings, rubricated initials, the ghost
  layer's display lines. Its period irregularities (uneven baseline energy,
  old-style letterforms) are the theme's handwriting; never substitute a
  cleaner old-style face. Load the regular and italic; the SC (small caps)
  cut is used for running titles and folio labels.
- **EB Garamond** — body, captions, apparatus. Garamond runs small: the
  scale below is set ~2px larger than a modern-serif system at every role.
- **The ghost layer uses the same two faces.** The under-text was written by
  the same institution, earlier. A different typeface for ghosts is the
  single most common way this theme dies (§9.2). Ghost display lines are IM
  Fell English; ghost body is EB Garamond; both rotated −1.5° (range
  −1° to −2° per leaf, fixed per leaf, never animated), letter-spacing
  +0.01em wider than surface (ink spread on old parchment), line-height
  +0.04 looser.

**Type scale** (root 19px; ratio ≈ 1.28, a manuscript's modest ladder):

| Role | Face | Size / line-height | Tracking | Notes |
|---|---|---|---|---|
| Display | IM Fell English | 54px / 60px | −0.005em | Hero headline only; its ghost twin sits beneath at identical size |
| H1 | IM Fell English | 42px / 48px | −0.005em | Page titles; rubricated initial where a leaf opens a major passage |
| H2 | IM Fell English | 31px / 38px | 0 | Leaf headings; small-caps running-title style for repeated sections |
| H3 | IM Fell English italic | 24px / 32px | 0 | Sub-passages, plate titles |
| Body | EB Garamond | 19px / 30px (1.58) | +0.002em | The reading voice; measure 58–66ch, never wider |
| Body small | EB Garamond | 17px / 27px | +0.002em | Card body, form help |
| Caption / apparatus | EB Garamond | 15px / 22px | +0.01em | Folios, provenance notes, plate captions — `--ink-soft` |
| Provenance label | IM Fell English SC | 13px / 18px | +0.14em | "RECOVERED LAYER · AUTUMN 1998" — the archive's stamp voice |
| Data / folio numerals | EB Garamond (tabular via `font-variant-numeric`) | 15px | +0.02em | Counts, folios, dates — old-style figures prohibited here; lining tabular only |

**Per-role rules.**

- *Rubricated initial:* the first letter of a ghosted or major passage, set
  in IM Fell English at 3.1× the body size, floated into the text block,
  `--rubric`. It is the passage's own letter — the build wraps it, content
  never hand-codes it. One rubricated initial per leaf maximum.
- *Surface text is never set below 15px and never in `--ghost`.* If it
  matters, it is surface; if it is violet, it is artefact.
- *Headlines never track out.* Fell's irregularity is the texture; letterspaced
  Fell looks like a film poster (§9.7).
- *Italics are for the past.* Surface voice speaks in roman; quotations of
  the under-text — when surfaced in the transcription panel (§6.17) — are
  set in italic, the typographic equivalent of a raised eyebrow.
- *Numbers in prose are words* ("the third scraping"), numbers in apparatus
  are figures ("Layer III of IV"). The theme is a book, not a dashboard.

**Font loading.** Subset to Latin + Latin Extended (the Fell faces carry
period ligatures worth keeping); `font-display: swap` with a Georgia
fallback stack whose metrics are matched via `size-adjust` (102% EB
Garamond fallback, 98% Fell fallback) so a late font never reflows the
strata — reflow under a rotated ghost layer is visible as a tear (§6.3 edge
cases). Total font budget: 4 files, ≤120KB woff2 (§14).

---

## 4. Layout language

**The leaf.** Every section is a leaf: a parchment surface inset from the
viewport edges by the margin apparatus. The reading column is centred,
max-width 68ch of surface measure (≈ 720px at the body size), flanked by two
margins that are *working margins* — the left carries the gold-fleck
progress line (§6.8) and the wormhole trail (§6.9); the right carries
provenance labels, folio marks, and the wax-seal landing zone (§6.11). On
wide screens the margins are where the theme lives; the column is where the
content lives.

**Strata geometry.** Each ghosted passage is a `.strata` block:
`position: relative`. The parchment stratum is the block's own background
(texture §2). The ghost stratum is an absolutely positioned layer,
`inset: 0`, `transform: rotate(-1.5deg) translate(6px, 10px)`, `z-index: 1`,
containing the under-text set in the same measure. The surface stratum is
`position: relative; z-index: 2`. The ghost layer is offset down-right —
the under-text sits slightly *below* the surface lines, as scraped text
survives in the troughs between the new lines, never exactly beneath them
(exact registration reads as a printing error; offset reads as archaeology).

**Grid.** A 12-column grid exists only to place the margins and the arch
frames; the reading column occupies columns 4–9 at ≥1200px, 3–10 at
768–1199px, and the full width below 768px with margins folded into a top
apparatus bar (§6 breakpoint rules). Images (illuminations) break the
column deliberately: an arch frame may occupy columns 3–10, because a
miniature in a manuscript is wider than its text block.

**Spacing rhythm.** Base unit 8px; leaf padding 96px top / 80px bottom at
desktop (the leaf breathes like a page, not a section of a landing page);
passage gap 40px; the gap *between* leaves is 0 — leaves are separated by
the vine rule (§6.9) drawn in the shared margin, so the page reads as one
continuous codex, not stacked cards. Whitespace here is parchment: it is
the material the text was scraped *from*, and it is never filled with
decoration. An empty margin is a scraped margin; it is allowed to be empty.

**Density rules.** Maximum one ghosted passage per leaf; maximum one pinned
sequence (§6.4) per page; maximum three illuminations per page. The theme's
premium register is restraint — a real codex has one miniature per several
leaves, and the rarity is the luxury.

**Alignment.** Surface text is left-aligned (ragged right — justified text
with Fell's irregularity produces rivers that read as damage). Centred text
is reserved for the title leaf (§8.1) and the colophon footer (§6.16),
where a manuscript itself centres.

---

## 5. Full motion system

All motion runs through **one shared requestAnimationFrame loop** (the
"lamp loop") with per-effect lerp factors; there is exactly one scroll
listener for the whole theme. Named easings, defined once as tokens and
used by every element:

| Token | Curve | Character | Used by |
|---|---|---|---|
| `--ease-lamp` | `cubic-bezier(0.22, 0.61, 0.21, 1)` | Light arriving — quick to arrive, slow to leave | Raking light, ghost-ups, arch reveals |
| `--ease-settle` | `cubic-bezier(0.16, 1, 0.3, 1)` | A leaf settling flat | Surface entrances, card settles |
| `--ease-scrape` | `cubic-bezier(0.7, 0, 0.2, 1)` | Resistance, then release — a knife stroke | Page transitions, seal press |
| `--ease-flare` | `cubic-bezier(0.34, 1.25, 0.4, 1)` | A brief overshoot — pigment catching light | Rubric flares, fleck twinkles |
| `--ease-drift` | `linear` | Procession pace — no arrival, no departure | §6.18 procession, ambient twinkle phase |

**The motion vocabulary, translated into the leaf's language** — every term
present, each with its duration, easing, and trigger. Terms this theme
refuses are refused *in the table*, with the reason, so no later builder
"fixes" the gap:

| Motion term | Palimpsest translation | Spec |
|---|---|---|
| Scroll-triggered reveal | Surface passages settle: 6px rise + ink density 82%→100% | 550ms `--ease-settle`, IntersectionObserver 0.2 |
| Parallax | Three-strata shear (§6.3): surface 1.0×, ghost 0.92×, parchment 0.85× | Scrubbed in the lamp loop, lerp 0.1 |
| Pinned scene | The pinned passage, three versions (§6.4) | ~200vh pin, versions cross-lit in thirds |
| Masked line reveal | Headline lines unmask upward from behind a parchment rule | 700ms `--ease-lamp`, 90ms line stagger |
| Blur-to-sharp | Ghost sharpening under linger: blur 1.4px→0 as opacity rises (§6.10) | 600ms dwell-in, `--ease-lamp` |
| Animated counters | Folio and "layers recovered" counts (§6.8, §6.13) | Discrete ticks at leaf boundaries, 240ms crossfade |
| Progress indicator | Gold-fleck margin line (§6.8) | Scrubbed brightening, fleck by fleck |
| Marquee | The procession of recovered leaves (§6.18) — a 90s horizontal drift of fragments | `--ease-drift`, pauses on hover/focus; the theme's only marquee, deliberately funereal in pace |
| Ambient loop | Gold flecks twinkle as the light passes (§6.2/§6.8); parchment grain does **not** move | 3.2s twinkle cycle, randomised phase |
| Micro-interactions | Rubric underline draw on links (280ms), seal-press on click (§6.11), folio tick | Per §11 component specs |
| Hover physics | Miniature tilt toward the lamp (§6.7): rotateX/rotateY ≤5°, spring return | Spring stiffness 170, damping 19 (JS spring in the lamp loop) |
| Page transition | Scraped-leaf wipe (§6.12) | 500ms `--ease-scrape` |
| Image treatment | Illuminations scale-in-frame 1.06→1 inside the arch (§6.7), parchment grade (sepia 0.18, contrast 0.94) | 900ms `--ease-lamp` |
| Kinetic type | **Refused.** Letters do not dance on a leaf that took six centuries to write. The contested word (§6.5) is the single exception, and it is an argument about spelling, not choreography | — |
| Custom cursor | **Refused** (standing rule). The system cursor is the reader's finger on the page | — |

**Global fallback law (applies to every element below).** Every animated
state is an enhancement layered on a complete static page. Each reveal
carries a **1.5s scroll-independent fallback timer**: any element whose
trigger has not fired within 1.5s of entering the viewport settles to its
resting state anyway. With JavaScript disabled, the page is the finished
leaf: surface text at full density, ghost layer visible statically at
0.30 opacity, light fixed at its mid-leaf position. `prefers-reduced-motion`
selects that same static leaf, live (§10 gate items 4–6).

---

## 6. Signature elements

Each element carries the full build spec (what & why, structure, motion
spec, content-merge, failure fallback, reduced-motion variant, performance
budget, mobile variant) **and** the v2 deepening layers: a millisecond
choreography timeline, a complete state matrix, breakpoint behaviour, edge
cases and failure modes, an accessibility spec, and the exact tokens it
consumes.

### 6.1 Idle ghost-up (hero signature)

- **What & why.** The hero's surface headline stands clean and alone for two
  full seconds — the brand as it speaks today, given the first word. Then,
  unhurried, the erased under-text ghosts up beneath it at −1.5°: the
  founder's first-draft tagline, in the same Fell hand, grey-violet, saying
  the same thing less politely. It is the theme's thesis performed in four
  seconds: *we have been saying this for longer than this sentence.* No
  other element may be understood before this one is felt.
- **Structure.** `<header class="leaf leaf--title">` containing one `.strata`
  block: `<div class="stratum stratum--ghost" aria-hidden="true">` holding a
  `<p class="ghost-line">` (the under-text, duplicated copy for the visual
  layer only), and `<h1 class="stratum stratum--surface">`. The ghost is a
  *visual echo*: the same under-text is available as real, readable content
  in the transcription panel (§6.17) and in a visually hidden paragraph
  after the H1 for assistive tech ("Earlier version, 2019: …"). The ghost
  div itself is `aria-hidden` and `pointer-events: none`.
- **Motion spec.** Trigger: time — 2,000ms after the hero's surface entrance
  completes (not after `load`; after the entrance timeline in §8.1 ends).
  Ghost opacity 0→0.38 over 1,600ms `--ease-lamp`, with a simultaneous
  sharpening blur 2px→0.9px (under-text is never fully sharp — it was
  scraped, not printed). The ghost never exceeds 0.38 resting opacity in the
  hero; its job is presence, not legibility.
- **Choreography timeline (v2).** t=0ms surface H1 unmask begins (§5 masked
  line reveal) → t=700ms H1 settled, rubric initial flares (§6.6) →
  t=2,000ms idle confirmed (no scroll > 24px, no pointer-down since t=0;
  any interaction skips the wait and starts the ghost-up immediately at
  next frame) → t=2,000–3,600ms ghost rises 0→0.38 with blur 2→0.9px →
  t=3,600ms ghost at rest; the gold flecks in the margin (§6.8) give one
  twinkle pass as if the light noticed → t≥3,600ms the raking-light system
  (§6.2) takes custody of the ghost.
- **State matrix (v2).** *Rest (pre-trigger):* surface only, ghost at 0 —
  the page is complete and honest in this state forever if need be.
  *Rising:* as timeline. *Settled:* ghost 0.38, blur 0.9px. *Hover:* none —
  the hero ghost does not respond to hover; §6.10 owns lingering, and two
  competing ghost gestures in one block is noise. *Focus:* keyboard focus
  entering the hero (e.g. tabbing to the hero CTA) triggers the ghost-up
  immediately if it has not happened — focus is attention, and attention is
  the lamp. *Active:* n/a. *Scrolled-past:* ghost returns to §6.2's custody;
  scrolling back up does not replay the rise. *Disabled:* n/a (not a
  control). *Touch:* no hover exists; the idle trigger is the primary path,
  which is why the trigger is time, not pointer.
- **Breakpoint behaviour (v2).** ≥1200px: as spec. 768–1199px: ghost angle
  −1.25°, offset (5px, 8px) — the narrower leaf crowds the strata.
  <768px: ghost angle −1°, offset (4px, 7px), resting opacity 0.34; the
  under-text is set one size step down (ghost display 44px vs surface 40px
  mobile scale) so the two lines never collide on a 360px leaf.
- **Edge cases & failure modes (v2).** *Very long under-text* (wraps to 3
  lines where surface wraps to 2): the ghost block is allowed its own line
  count; strata height = max(surface, ghost) so nothing clips — clipping a
  ghost mid-word reads as damage, and damage is §9.9's slop, not charm.
  *Visitor scrolls within the first 2s:* ghost-up fires immediately at
  reduced duration (800ms) as the hero leaves — the past gets one glimpse,
  not a chase. *Fonts late:* the ghost-up timer starts only after
  `document.fonts.ready` OR 900ms, whichever first, so the ghost never
  rises in fallback type and then jumps faces. *Second visit (SPA return):*
  ghost starts at rest 0.38 — the reader has met this leaf before.
- **Accessibility spec (v2).** Ghost layer `aria-hidden="true"`; the
  under-text's content is present once, semantically, in the visually
  hidden provenance paragraph and in §6.17's panel. Surface H1 contrast
  7.5:1 at all times (the ghost beneath it is decoration over parchment and
  never reduces the H1's effective contrast below 6.8:1 — verified at ghost
  peak 0.38 in the §10 gate). No focusable elements inside the ghost layer.
  The ghost-up is not announced (`aria-live` off): it is atmosphere, and
  announcing atmosphere is noise.
- **Content-merge.** The ghost is the headline's own earlier draft, supplied
  in the strata file with its date. It occupies the same leaf, the same
  measure, the same point size. Remove it and the hero still works; read it
  and the hero means more. That is the merge test every element here passes.
- **Failure fallback.** If the timer chain or rAF fails, the global 1.5s
  fallback (§5) settles the ghost to 0.30 static. No-JS: ghost is present in
  the static page at 0.30 from first paint — a printed ghost, no rise.
- **Reduced-motion variant.** No rise, no blur change: ghost static at
  0.30, exactly the no-JS leaf.
- **Performance budget & mobile variant.** One opacity/blur transition on
  one layer; blur is the only expensive property and it is confined to a
  single headline block for 1.6s, then removed (`filter: none` at rest —
  a resting blur filter on a large text block forces repaint on every
  scroll frame and is forbidden). Mobile: blur range reduced to 1.2→0.6px,
  duration 1,400ms.
- **Tokens.** `--parchment`, `--ink`, `--ghost`, `--ease-lamp`,
  `--ghost-angle` (−1.5deg), `--ghost-rest-opacity` (0.38), `--dur-ghost-up`
  (1600ms), `--idle-ghost-delay` (2000ms).

### 6.2 Raking-light ghost sweep

- **What & why.** Scholars recover under-text by tilting the leaf under a
  lamp until the scraped strokes catch the light. This element is that lamp:
  a diagonal band of warmth that travels across each leaf as you scroll,
  and ghost passages brighten — up to 0.5 opacity — only while the band is
  over them, then sink as it passes. Reading becomes an act of recovery,
  and the scroll itself becomes the instrument.
- **Structure.** Per leaf: a `.raking-light` overlay div (`position:
  absolute; inset: -10% -20%`, a `linear-gradient(105deg, transparent 42%,
  rgba(255, 244, 214, 0.16) 50%, transparent 58%)`, `mix-blend-mode:
  soft-light` over parchment, `pointer-events: none`, `z-index: 3` — above
  surface text, since light falls *on* the leaf). Ghost passages inside the
  leaf carry `data-ghost` and receive a per-passage `--lit` custom property
  (0→1) computed in the lamp loop from the band's current position vs the
  passage's centre; ghost opacity = base + `--lit` × lift.
- **Motion spec.** Scrubbed, never time-based: the band's position maps to
  the leaf's progress through the viewport (leaf top at 85% viewport →
  band at −20%; leaf bottom at 15% → band at 120%). Ghost lift: opacity
  +0.20 and blur −0.5px at `--lit` = 1. All values through the lamp loop
  with lerp 0.12, so the light has the slight lag of a hand moving a lamp.
  The band crosses a passage in ≈ 40vh of scroll travel — slow enough to
  read the ghost as it brightens.
- **Choreography timeline (v2).** Continuous, position-keyed rather than
  time-keyed: leaf enters at viewport bottom → band approaches from the
  leaf's top-left → first ghost passage reaches `--lit` 0.5 at ≈ 12% leaf
  progress → peak `--lit` 1.0 at the passage's centre → passage sinks over
  the next ≈ 15% progress → band exits bottom-right as the leaf leaves.
  Beats are relative to each passage, so a leaf with two ghost passages
  lights them in reading order, never simultaneously (two lit ghosts at
  once = a floodlight, §9.5).
- **State matrix (v2).** *Rest (leaf off-screen):* band parked off-leaf,
  ghosts at base opacity. *Lit:* as above. *Hover:* hovering a ghost
  passage does not move the lamp — §6.10's linger raises the ghost locally;
  the lamp is scroll's instrument only. Keeping the two systems from
  fighting is a design decision, not an omission. *Focus:* a focused
  element inside a ghosted passage raises that passage to `--lit` 0.7
  equivalent (keyboard readers get lamplight too). *Scrolled-past:* band
  gone, ghosts at base. *Touch:* identical — the system is scroll-driven,
  so it is natively touch-complete.
- **Breakpoint behaviour (v2).** ≥1200px: band angle 105°, width 16% of leaf.
  768–1199px: width 20%. <768px: width 26%, gradient stops softened (peak
  alpha 0.12) — on a narrow leaf a strong band reads as a glare stripe, not
  lamplight; ghost lift reduced to +0.16.
- **Edge cases & failure modes (v2).** *Fast scrolling:* lerp 0.12 means
  the band trails; ghosts may never peak during a fling — acceptable, the
  fallback timer (§5) guarantees base legibility, and a fling is skimming,
  not reading. *Leaf taller than 200vh:* the band maps to the leaf's full
  height, so mid-leaf ghosts still get their pass; leaves are capped at
  160vh by §4 density rules to keep the pass timely. *`mix-blend-mode`
  unsupported:* the overlay falls back to a plain low-alpha gradient (no
  blend) — slightly flatter light, same information. *Dark scheme:* band
  warms (rgba(255, 196, 120, 0.14)) and narrows to 12% — candle, not
  window (§2).
- **Accessibility spec (v2).** The light is pure decoration: `aria-hidden`,
  no content, no state conveyed that is not also in the DOM (ghost text is
  always in the accessibility tree via §6.17's provisions). Brightness
  change is luminance-only on an overlay; surface text contrast never drops
  below 6.5:1 at band peak (the gradient is capped for exactly this reason;
  verified in §10). No flashing: the band moves at scroll speed, well under
  any photosensitivity threshold.
- **Content-merge.** The light falls on the leaf's own passages and lifts
  the leaf's own under-text. It animates nothing that is not the content's
  history becoming visible.
- **Failure fallback.** Lamp loop dead → `--lit` stays 0, ghosts rest at
  base opacity, page fully readable; the overlay div is `display: none`
  without JS (it is JS-injected).
- **Reduced-motion variant.** Band fixed at the leaf's vertical centre,
  static; ghosts at a flat 0.34; no scrubbing.
- **Performance budget & mobile variant.** One gradient layer per *visible*
  leaf only (off-screen leaves' overlays are `content-visibility` culled);
  the loop writes one custom property per visible ghost passage per frame —
  budget ≤ 6 property writes/frame. Mobile: blend mode dropped (GPU cost),
  plain gradient, lerp 0.15.
- **Tokens.** `--gold-bright` (band tint derives from it), `--ease-lamp`
  (lerp character), `--ghost-lift` (0.20), `--lamp-angle` (105deg),
  `--lamp-lerp` (0.12).

### 6.3 Three-strata shear parallax

- **What & why.** A palimpsest's layers were never perfectly registered —
  scraped skins shift. As the leaf scrolls, its three strata move at three
  rates: surface text at 1.0×, ghost under-text at 0.92×, parchment ground
  at 0.85×. Over a viewport of travel the ghost drifts a few pixels against
  the surface, and the visitor *feels* the layers separate — the scraping
  made visible as relative motion. It is the theme's signature sensation
  and its most rationed: shear is applied to ghosted passages only, never
  to whole pages (a whole page shearing is a funfair ride, §9.6).
- **Structure.** Inside each `.strata` block: the parchment stratum is the
  block's background layer, implemented as a `::before` with the texture
  (§2) sized 104% and translated by the loop; the ghost stratum (§6.1
  structure) gets `translateY` offsets; the surface stratum is untouched
  (it defines the scroll truth — the current text never moves against the
  reader's eye, only the past drifts). Maximum ghost drift: ±14px over a
  full viewport pass; parchment drift: ±22px, clipped by the block's
  `overflow: hidden` with 24px of texture bleed on all sides.
- **Motion spec.** Scrubbed in the lamp loop: for each visible `.strata`,
  progress p = (viewport centre − block centre) / viewport height, clamped
  [−1, 1]. Ghost translateY = p × −14px (on top of its static offset);
  parchment translateY = p × −22px. Lerp 0.1. No easing curve — scrubbed
  motion takes the scroll's own easing; adding one is how shear turns to
  jelly (§9.6).
- **Choreography timeline (v2).** Position-keyed: block enters → p = −1,
  ghost sits 14px high against its rest position → p = 0 at centre,
  strata at designed registration (the offset of §4) → p = +1 leaving,
  ghost 14px low. The visitor perceives a slow 28px disagreement across
  the whole pass — felt, not noticed. That ratio (28px per viewport) is
  the premium setting; 40px+ reads as a bug, 10px reads as nothing.
- **State matrix (v2).** *Rest:* p = 0 registration. *Scrolling:* as spec.
  *Hover/focus/active:* no change — shear is the scroll's voice only.
  *Scrolled-past:* values clamp; no accumulation (the transform is a pure
  function of position, so there is no state to corrupt). *Touch:*
  identical, driven by the same scroll position.
- **Breakpoint behaviour (v2).** ≥1200px: full ±14/±22px. 768–1199px:
  ±10/±16px. <768px: shear reduced to ±6px ghost, parchment static —
  small leaves, short travel, and mobile GPUs repaint rotated layers
  expensively; the ghost's static angle still carries the theme.
- **Edge cases & failure modes (v2).** *Font swap reflow:* if the strata
  re-measure after fonts arrive, offsets recompute from the same pure
  function — no jump, because there is no stored state. *Very short
  passages* (< 3 lines): shear is disabled (drift would exceed the text
  height and the ghost would detach from its surface — a ghost must haunt
  its own paragraph, §9.4). *Browser without `transform` on the ghost
  layer's rotation composition:* rotation and translation are combined in
  one `transform` string by the loop, never two competing properties.
  *Scroll restoration mid-page:* first frame computes from actual scroll
  position — correct registration instantly, no sweep from zero.
- **Accessibility spec (v2).** Motion is sub-perceptual drift of a
  decorative layer; the surface stratum — all actual content — never
  moves. Vestibular safety: total drift 28px per viewport at scroll speed
  is far below parallax risk thresholds, and reduced-motion removes it
  entirely. Ghost remains `aria-hidden` per §6.1.
- **Content-merge.** The strata are the passage's own three physical
  layers; the shear is their physical relationship, animated. Nothing
  decorative is introduced — remove the effect and the archaeology is
  still drawn; keep it and the archaeology breathes.
- **Failure fallback.** Loop failure → transforms never written → strata
  sit at designed registration (the CSS default), which is the intended
  static composition.
- **Reduced-motion variant.** No shear. Strata at registration, ghost at
  flat opacity — the printed leaf.
- **Performance budget & mobile variant.** Transform-only writes, ≤ 2 per
  visible strata per frame, compositor-cheap. Rotated layers are the cost:
  cap simultaneously shearing strata at 3 (nearest to viewport centre win;
  others hold last value). Mobile: 1 stratum, ±6px, as above.
- **Tokens.** `--ghost-angle`, `--shear-ghost` (14px), `--shear-parchment`
  (22px), `--lamp-lerp` (0.1 for this system), `--ghost` (layer identity).

---

### 6.4 Pinned passage, three versions

- **What & why.** The theme's one piece of theatre, rationed to once per
  page (§4): a passage the institution is known for — the motto, the famous
  opening line, the founder's sentence — pins in place for ~200vh while its
  three historical versions scroll beneath it, each catching the raking
  light and reaching full ghost presence in turn. The current wording holds
  the lectern; its ancestors file past underneath and are, one by one,
  illuminated. It stages textual history as a ceremony, and it only works
  because the versions are real.
- **Structure.** `<section class="pinned-passage">` with a sticky stage
  (`position: sticky; top: 0; height: 100vh`) containing: the surface
  passage centred (the lectern text, real DOM, always readable), and three
  `.version` ghost layers stacked in the same strata geometry, each
  labelled with a provenance label ("VERSION I · 1962", "VERSION II ·
  1987", "VERSION III · 2011" — IM Fell SC, §3). The section's own height
  (300vh total: 100vh stage + 200vh travel) drives progress. Version labels
  are surface apparatus (real text, `--ink-soft`), never ghosted — the
  visitor must always know *which* past they are looking at.
- **Motion spec.** Scroll-scrubbed through the lamp loop: progress q ∈
  [0, 1] across the 200vh travel divides into thirds. In each third, that
  third's version rises: opacity 0.10 → 0.55, blur 1.6px → 0.4px, and the
  raking-light band (§6.2) parks over it. At third boundaries the outgoing
  version sinks to 0.10 over the first 15% of the next third while the
  incoming rises — a 0.05q overlap, never two versions strong at once
  (three strong ghosts = soup, §9.5). The surface passage never moves,
  never dims, never blurs. A "layers recovered" counter (§6.8) ticks I →
  II → III at each third.
- **Choreography timeline (v2).** q=0.00: stage pins; Version I at 0.10,
  label I fades in (300ms). q=0.05–0.28: Version I rises to 0.55 peak at
  q≈0.18, light parked. q=0.28–0.38: I sinks, II rises, counter ticks at
  q=0.33. q=0.38–0.61: Version II's reign, peak q≈0.50. q=0.61–0.71: II
  sinks, III rises, counter ticks q=0.66. q=0.71–0.95: Version III's reign.
  q=0.95–1.00: all versions settle to 0.30 (the whole history visible at
  once, faintly — the only moment of simultaneity, earned at the end),
  stage unpins, the leaf continues.
- **State matrix (v2).** *Rest (before pin):* surface + Version I at 0.10.
  *Pinned:* as timeline. *Hover:* none — ceremony does not take requests.
  *Focus:* if focus enters the stage (a link within the surface passage),
  the sequence pauses its sink/rise for the focused third and holds that
  version at 0.5 until focus leaves — a keyboard reader must never chase a
  fading text. *Scrolled-past:* all versions at 0.30 static (the end-state
  composition). *Scrolled back up:* the sequence reverses purely from q —
  no stored state, no replay glitches. *Touch:* identical (scroll-driven).
- **Breakpoint behaviour (v2).** ≥1200px: as spec. 768–1199px: travel
  170vh, version peaks 0.50. <768px: **the pin is removed** — travel
  becomes a simple stacked sequence: surface passage, then each version as
  its own ghosted block revealed on entry (§5 reveal spec), labels intact.
  Sticky 100vh stages on small screens trap short viewports and murder
  scroll rhythm; the story survives demotion, the trap does not (§9.10).
- **Edge cases & failure modes (v2).** *A version longer than the stage:*
  versions are capped at 5 lines by content rule (§12); longer drafts are
  excerpted with an ellipsis and the full text lives in §6.17's panel —
  never shrink type to fit the stage. *Sticky unsupported / broken by an
  ancestor's overflow:* detect pin failure (stage top never sticks for
  100px of scroll) and fall back to the mobile stacked sequence at any
  viewport. *Reduced data / slow device:* the sequence is transform/opacity
  only; no assets. *Visitor scrolls fast through:* q is a pure function —
  they land wherever they land, mid-ceremony, correctly composed.
- **Accessibility spec (v2).** All three versions are real text in the DOM
  in reading order (surface, then I, II, III each with its provenance label
  as a heading-level caption), so a screen reader reads the ceremony as a
  list — the visual pinning is `aria`-silent. Ghost styling is visual only;
  the versions' text is *not* aria-hidden here (unlike §6.1's echo) because
  in this element the versions ARE the content. Contrast: versions at peak
  0.55 in `--ghost-strong` ≈ 2.6:1 — artefact grade; therefore each version
  is *also* printed in the transcription panel (§6.17) at full contrast,
  and the stage carries a surface-text link "Read all versions" to it.
  Focus-hold behaviour per the state matrix. Touch targets: the link is
  ≥44px.
- **Content-merge.** The pinned text is the institution's most-quoted
  passage and the three under-texts are its documented earlier wordings
  from the strata file. The ceremony has no content of its own — it *is*
  the content, given duration.
- **Failure fallback.** No JS: the section renders as the stacked sequence
  (surface, then three labelled versions at 0.34 static) — which is also
  the mobile and reduced-motion form. The pin is an enhancement of a
  complete static composition, never its replacement.
- **Reduced-motion variant.** The stacked sequence, static, all versions at
  0.34, labels in place. No pin, no scrub.
- **Performance budget & mobile variant.** One sticky stage, ≤ 4 opacity
  writes/frame. The stage's layers are `will-change: opacity` only during
  the pin (class toggled at pin start/end) to avoid permanent layer cost.
  Mobile: stacked sequence per breakpoints — zero pinning cost.
- **Tokens.** `--ghost`, `--ghost-strong`, `--ink-soft`, `--ease-lamp`,
  `--pin-travel` (200vh), `--version-peak` (0.55), `--gold` (counter).

### 6.5 Contested-word flicker

- **What & why.** Somewhere in the leaf, two centuries disagree about one
  word — "shew" vs "show", "oeconomy" vs "economy", the founder's "make"
  vs the rebrand's "craft". When that passage enters, the contested word
  flickers between its two historical spellings — three cross-swaps over
  900ms — then settles on the modern spelling, with the old spelling
  subsiding into the ghost layer beneath it. The argument is preserved,
  dated, and resolved in favour of the present, exactly as the manuscript
  resolved it. One contested word per page; a second is a gimmick (§9.8).
- **Structure.** `<span class="contested" data-old="shew">show</span>` in
  the surface text. The old spelling is generated as a ghost-layer twin
  positioned over the word's own box (measured once at layout, re-measured
  on resize/font-load), plus a visually hidden note "(earlier spelling:
  shew)" for assistive tech. The word's surface text in the DOM is always
  the modern spelling — flicker never mutates content, only cross-fades
  two stacked renderings of it.
- **Motion spec.** Trigger: passage entry (IntersectionObserver 0.35, once
  only — an argument does not restart every time you look at it). Three
  cross-swaps: modern→old→modern→old→modern, each swap a 150ms opacity
  crossfade, total 900ms, `--ease-lamp`. Between swaps, 0ms dwell — the
  rhythm is a flicker, not a slideshow. Settles: modern at full ink, old
  spelling sinking to ghost rest (0.30, offset per §4 geometry, as a
  one-word strata).
- **Choreography timeline (v2).** t=0 passage crosses 0.35 visibility →
  t=120ms first swap begins (a breath — the eye must land first) →
  swaps at 120/270/420/570/720ms (five crossfades = three old-spelling
  appearances) → t=870ms final crossfade to modern completes → t=870–
  1,470ms old spelling sinks from overlay position to ghost offset
  (translate 6px/10px, opacity →0.30, blur →1px) → rest. Total event
  1,470ms, fires once per page load.
- **State matrix (v2).** *Rest (pre-entry):* modern spelling, old at ghost
  rest already visible faintly beneath (the strata is honest before the
  argument starts). *Flickering:* as timeline. *Settled:* modern full,
  old at ghost rest — visually identical to pre-entry except the visitor
  now knows the story. *Hover:* hovering the settled word raises the old
  spelling to 0.5 (a one-word §6.10) — the curious can re-interrogate it.
  *Focus:* the word is not focusable (it is not a control); a footnote
  marker beside it IS focusable and opens §6.17 with this word's entry.
  *Scrolled-past / back:* never re-flickers. *Touch:* tap = the hover
  raise (first tap raises, second tap follows any link — the word itself
  is not a link, so tap simply raises and releases on scroll).
- **Breakpoint behaviour (v2).** Identical at all sizes; at <768px the
  sink offset reduces to (4px, 7px) per §6.1's mobile geometry.
- **Edge cases & failure modes (v2).** *Word wraps across lines after a
  resize mid-flicker:* the twin re-measures at each swap boundary; worst
  case the flicker aborts to settled state (abort is always safe — settled
  is the honest end state). *Old spelling longer than modern* ("oeconomy"
  over "economy"): the twin overflows its box symmetrically; the surface
  line never reflows because the twin is absolutely positioned — a
  one-letter width difference must never push the paragraph around.
  *Fonts late:* flicker waits for the same fonts gate as §6.1.
- **Accessibility spec (v2).** The flicker is 3 swaps in 900ms of a single
  word at partial opacity — luminance change is small and local; still,
  it is disabled entirely under reduced motion. Screen readers get the
  modern spelling plus the hidden note, once, in reading order. The
  footnote marker is a real `<button>` (44px target via padding, visual
  size 18px) labelled "About the word 'show' — earlier spelling".
- **Content-merge.** The flicker happens inside a real word of real copy,
  over a documented spelling change from the strata file. It annotates the
  text; it is not applied to the text from outside.
- **Failure fallback.** No JS: modern spelling in the text, old spelling
  present as a static one-word ghost beneath — the argument visible, the
  flicker absent. Nothing is ever hidden by the failure.
- **Reduced-motion variant.** No flicker. Old spelling at ghost rest from
  first paint.
- **Performance budget & mobile variant.** One word, two layers, 1.5s —
  negligible; the only cost is the measurement pass (one `getBoundingClientRect`
  per swap, cached). Mobile: identical.
- **Tokens.** `--ink`, `--ghost`, `--ease-lamp`, `--dur-flicker` (900ms),
  `--ghost-rest-opacity` (0.30 for micro-strata).

### 6.6 Rubric flare stagger

- **What & why.** In the manuscript, a scribe went back through the
  finished leaf with red pigment and rubricated the initials — the red was
  added last, by a second hand, as an act of emphasis. On this leaf, when a
  passage enters, its rubricated initial flares from dull brown (its
  un-rubricated state) to full iron-red, and where a leaf holds several
  passages, the flares stagger 120ms apart — the rubricator walking down
  the page. It is how the leaf says *here, and here, and here* without a
  single arrow or icon.
- **Structure.** The initial is a `<span class="rubric-initial">` wrapping
  the passage's first letter (build-generated, §3), floated at 3.1× body
  size. Colour is driven by a `--rubrication` custom property (0→1)
  interpolating `color` between `--ink` and `--rubric` via `color-mix`;
  engines without `color-mix` step through three pre-computed classes.
  The initial's letter is part of the surface text node flow for
  assistive tech (the span is transparent to readers).
- **Motion spec.** Trigger: passage entry (IntersectionObserver 0.25).
  Flare: `--rubrication` 0→1 over 450ms `--ease-flare` (peak overshoot
  touches `--rubric-bright` at 70% of the curve, then settles to
  `--rubric`). Stagger: initials within the same leaf offset 120ms in
  DOM order. Once flared, an initial stays rubricated — the pigment does
  not un-apply when you scroll away.
- **Choreography timeline (v2).** Per passage: t=0 entry → t=80ms the
  passage's surface settle (§5) begins → t=200ms flare begins (the text
  must exist before it is emphasised — rubrication was a second pass) →
  t=650ms flare complete, initial at full `--rubric`. Per leaf with three
  passages entering together: flares at 200 / 320 / 440ms starts. The
  120ms stagger at 450ms duration means flares overlap like a hand moving
  — sequential, not metronomic.
- **State matrix (v2).** *Rest (pre-entry):* initial in `--ink` — a
  complete, handsome un-rubricated state. *Flaring:* as spec. *Settled:*
  `--rubric` permanently. *Hover:* hovering the initial deepens it to
  `--rubric-bright` over 200ms (a fingertip on the pigment) and back over
  300ms. *Focus:* passages are not focusable; no focus state. *Scrolled-
  past:* stays flared. *Touch:* no hover deepen; the flare is entry-driven
  and therefore touch-complete.
- **Breakpoint behaviour (v2).** Identical at all breakpoints; initial size
  scales with the type scale (3.1× the local body size at each breakpoint).
- **Edge cases & failure modes (v2).** *Passage whose first letter is a
  quotation mark or numeral:* the build rubricates the first *letter*,
  skipping leading punctuation — hand-wrapped initials in content are a
  build error the §10 gate checks for. *`color-mix` unsupported:* the
  three-step class fallback (33/66/100%) — slightly stepped, same outcome.
  *A leaf with 6+ passages entering at once* (long page, fast scroll):
  stagger compresses to 60ms so the rubricator is never still working a
  full second behind the reader.
- **Accessibility spec (v2).** Pure colour change on a letter that remains
  text throughout; contrast at rest (`--ink` 7.5:1) and settled (`--rubric`
  5.6:1, large-text AA at initial size) both pass. No information is
  carried by the flare — it emphasises what the heading structure already
  says. Reduced motion removes it (below).
- **Content-merge.** The flaring letter is the passage's own first letter.
  The emphasis is applied to content, by the content's own entry.
- **Failure fallback.** No JS / observer failure: initials render in
  `--rubric` statically (the CSS default is rubricated; JS sets the
  un-rubricated start state only for below-fold passages at setup). The
  fallback direction is deliberate: a failed flare leaves a finished leaf,
  never an unfinished one.
- **Reduced-motion variant.** Initials static in `--rubric` from first
  paint — the printed state.
- **Performance budget & mobile variant.** Colour transitions on ≤ 6
  letters per leaf; negligible paint cost. Mobile: identical.
- **Tokens.** `--rubric`, `--rubric-bright`, `--ink`, `--ease-flare`,
  `--dur-flare` (450ms), `--stagger-rubric` (120ms).

---

### 6.7 Gothic-arch illumination reveal

- **What & why.** The miniatures in a manuscript sit in arched frames —
  the Gothic arch is the period's window shape, and the miniature is a
  window into a scene. On this leaf, illuminations (the theme's images:
  a portrait of the founder, the house's garden, the manuscript itself)
  reveal through an arched clip-path that opens upward like a shuttered
  window being unlatched, then the image scales gently within its frame —
  the scene settling behind glass. Images in this theme are *plates*, few
  and precious (§4 caps three per page), and the reveal treats them so.
- **Structure.** `<figure class="illumination">` with an arch mask: an SVG
  clipPath (arch = rectangle with a semicircle-plus-point top, defined once
  in a hidden SVG defs block and referenced by every illumination) applied
  to a wrapper; inside, the `<img>` at scale 1.06; `<figcaption>` below in
  caption apparatus style (§3) with the plate's provenance ("Plate II —
  the founder in the bindery, 1962"). The arch reveal animates the clip
  wrapper's inner window: a second, inset arch clip that grows from 62%
  height (bottom-anchored) to 100%.
- **Motion spec.** Trigger: entry (IntersectionObserver 0.3). Arch opens:
  clip inset animates over 800ms `--ease-lamp`. Image scale 1.06→1.0 over
  900ms `--ease-settle`, starting 100ms after the arch begins (the window
  opens, then the scene settles). A parchment-grade filter (sepia 0.18,
  contrast 0.94, saturate 0.88) is constant, not animated — the image
  always lives on this leaf's terms. Tilt-on-linger (§5 hover physics) is
  available after reveal completes.
- **Choreography timeline (v2).** t=0 entry → t=0–800ms arch window grows
  upward → t=100–1,000ms image scales 1.06→1.0 → t=600ms the caption's
  provenance label fades in (200ms) — the label arrives while the scene is
  still settling, as a cataloguer would speak → t=1,000ms rest; tilt
  physics armed. Scrolling away mid-reveal: the reveal completes anyway
  (reveals in this theme never reverse; a window once opened stays open).
- **State matrix (v2).** *Rest (pre-entry):* the full image visible inside
  the *closed-but-complete* arch at scale 1.0 — pre-entry state is the
  finished plate, because the clip animation is JS-applied only to
  below-fold figures at setup (the standing no-hidden-content law).
  *Revealing:* as timeline. *Settled:* scale 1.0, tilt armed. *Hover:*
  the miniature tilts like a leaf angled to a lamp — rotateX/rotateY ≤ 5°
  toward the pointer, with the raking-light gradient (§6.2's band,
  localised) following across the image; spring return (stiffness 170,
  damping 19) on leave. *Focus:* figure focus (the image may be a link to
  its detail leaf) triggers the same light-follow at reduced angle (2°)
  and a `--rubric` outline drawn as an arch — the focus ring follows the
  frame's shape, never a rectangle around a Gothic window. *Active:*
  press dips scale to 0.99 (the leaf yields under the finger). *Scrolled-
  past:* unchanged. *Touch:* no tilt; tap follows the link if any; the
  reveal is entry-driven and touch-complete.
- **Breakpoint behaviour (v2).** ≥1200px: arch frames up to 10 columns
  wide (§4). 768–1199px: up to 8 columns; tilt capped at 3.5°. <768px:
  full-column width, tilt disabled (a phone is already a moving hand;
  tilting a tilting image is seasickness), arch open duration 650ms.
- **Edge cases & failure modes (v2).** *Image fails to load:* the arch
  frame remains, filled with `--parchment-deep` and the plate's
  provenance caption plus a rubricated initial of the plate's title — a
  missing miniature becomes a described miniature, the way a catalogue
  handles a leaf lost to damp; never a broken-image icon on the leaf.
  *Very tall images:* arch aspect is fixed 3:4 by the frame; `object-fit:
  cover` with `object-position` set per-plate in content (the cataloguer
  chooses the crop, the CSS never guesses a face). *clipPath unsupported
  (legacy):* figures render unclipped rectangles with the parchment grade
  — plainer, complete.
- **Accessibility spec (v2).** Real `<img>` with real alt text (the plate's
  subject, not "image of"); the clip and tilt are visual only. Focus
  outline per state matrix (arch-shaped, 2px `--rubric`, offset 3px —
  contrast of rubric on parchment 5.6:1 passes non-text AA). Tilt is
  disabled for `prefers-reduced-motion` and for any user whose pointer is
  coarse. Caption is associated via `aria-describedby` when the figure is
  a link.
- **Content-merge.** The arch is the miniature's own manuscript frame; the
  image inside is the site's real photography, graded onto the leaf. The
  reveal opens the window the content lives behind.
- **Failure fallback.** No JS: plates fully visible in their arches at
  scale 1.0 from first paint (the JS-set start states never exist).
  Observer failure → the 1.5s global fallback (§5) settles all plates.
- **Reduced-motion variant.** No arch animation, no scale, no tilt: the
  finished plate, statically framed.
- **Performance budget & mobile variant.** Clip-path animation on ≤ 3
  figures/page; the animated clip is on the wrapper (compositor-friendly
  in modern engines when the clip is an inset — the arch growth is
  implemented as an inset-rectangle *within* the arch mask, not an
  animated path `d`, which would repaint every frame). Tilt writes 2
  transform values/frame for the hovered figure only. Mobile: no tilt,
  per breakpoints.
- **Tokens.** `--parchment-deep`, `--rubric`, `--ease-lamp`,
  `--ease-settle`, `--dur-arch` (800ms), `--grade-sepia` (0.18),
  `--tilt-max` (5deg).

### 6.8 Gold-fleck progress line

- **What & why.** A manuscript's margin was gilt by hand, fleck by fleck.
  Down this leaf's left margin runs a line of gold flecks — one per leaf of
  the page — and as the visitor reads, the flecks brighten in order, each
  catching the raking light as its leaf is reached, twinkling slowly while
  the light is near. It is the page's progress indicator drawn in the
  page's own material: not a bar that fills, but gilt that wakes. At the
  foot of the margin, the apparatus counts what has been recovered:
  "Layer II of IV" (§6.13's counter shares this element's machinery).
- **Structure.** `<div class="fleck-line" aria-hidden="true">` fixed in
  the left margin (≥1200px) / in the top apparatus bar (<1200px, §6.13),
  containing N fleck spans (N = the page's leaf count, derived from the
  DOM, never hard-coded) positioned along a hairline track in `--gold` at
  0.35 opacity. Each fleck is a 5px rotated square (a fleck, not a dot —
  gilt is hammered, not printed). Brightening = opacity → 1.0 +
  `--gold-bright` + a 1px glow shadow. A visually hidden progress text
  ("Leaf 2 of 5") lives in each leaf header for assistive tech; the fleck
  line itself is decorative.
- **Motion spec.** Scrubbed in the lamp loop: overall page progress maps
  to flecks in sequence — fleck *k* begins brightening when leaf *k*'s
  header crosses 55% viewport height, completes over the next 12% of
  scroll. Twinkle: a lit fleck's brightness oscillates ±12% on a 3.2s
  `--ease-drift` cycle with per-fleck random phase, *only while the
  raking-light band (§6.2) is within the same leaf* — flecks twinkle when
  the lamp is near, not everywhere always (ambient motion with a cause).
- **Choreography timeline (v2).** Position-keyed: leaf *k* header crosses
  55% → fleck *k* brightens over ≈ 300ms of scroll travel → if the lamp
  band is in leaf *k*, twinkle begins → band leaves → twinkle damps out
  over 1s → fleck rests lit. Final leaf: the last fleck brightens and the
  margin gives one slow collective shimmer (all flecks +8% over 900ms) —
  the codex acknowledging its own completion, once, quietly.
- **State matrix (v2).** *Rest:* flecks up to current leaf lit, rest dim.
  *Hover:* hovering the fleck line (desktop) enlarges the nearest fleck
  and shows its leaf's title as a margin tooltip in apparatus style — the
  line doubles as a contents index. *Focus:* the line is not focusable;
  its information is duplicated in leaf headers and §6.15's contents.
  *Active:* clicking a fleck (they are buttons in the ≥1200px margin,
  28px hit area around a 5px fleck) scrolls to that leaf (smooth,
  600ms, or instant under reduced motion). *Scrolled-past:* all lit.
  *Touch:* flecks are not interactive on touch (28px targets in a margin
  a thumb scrolls through = mis-taps); contents duties pass to §6.15.
- **Breakpoint behaviour (v2).** ≥1200px: left margin, vertical, flecks
  interactive. 768–1199px: horizontal, in the top apparatus bar under the
  running title, non-interactive. <768px: same horizontal bar, flecks
  shrink to 4px, count text ("Leaf 2 of 5") appears beside them in
  apparatus type — on the smallest leaf the number does the work.
- **Edge cases & failure modes (v2).** *Single-leaf page:* the line
  renders with one fleck, lit — or is omitted entirely if the page has
  one leaf and no scroll (a progress indicator for no journey is clutter;
  the build omits it when document height ≤ 110vh). *Leaf count changes
  (dynamic content):* flecks rebuild from the DOM on mutation of
  `[data-leaf]` — the apparatus must never lie about the page it margins.
  *Print:* the line prints as a static gilt rule, all flecks at 0.6.
- **Accessibility spec (v2).** Decorative (`aria-hidden`); progress is
  conveyed semantically by leaf headers ("Leaf II of V") and landmarks.
  Fleck buttons (desktop) are real `<button>`s with labels ("Go to leaf
  II — The Versions"), visible focus = fleck glow + 2px `--rubric`
  outline. Colour is never the only signal: lit flecks are also 1px
  larger and carry the glow — a shape change, not just a hue change.
- **Content-merge.** The flecks count the page's actual leaves and light
  as the actual reading advances. It is the margin of *this* codex, gilt
  in proportion to *this* visit.
- **Failure fallback.** No JS: fleck line renders statically with all
  flecks at 0.6 — a gilt margin, no progress claim. (A static line that
  implied progress would be lying apparatus, §9.11.)
- **Reduced-motion variant.** Flecks still update (progress is
  information) but instantly at leaf boundaries — no brightening ramp, no
  twinkle, no completion shimmer.
- **Performance budget & mobile variant.** One scrubbed property set per
  frame (≤ N fleck opacities, N ≤ 12 by §4 density); twinkle runs on the
  same loop, no separate timers. Mobile: horizontal bar per breakpoints,
  twinkle disabled (battery + the lamp logic is desktop-margin theatre).
- **Tokens.** `--gold`, `--gold-bright`, `--rubric` (focus), `--ink-soft`
  (count text), `--ease-drift`, `--fleck-size` (5px).

### 6.9 Wormhole & vine SVG draw

- **What & why.** Real leaves carry their centuries on them: a worm's
  patient tunnel through the margin, a vine the illuminator grew along a
  section break. At this leaf's section boundaries, both draw themselves:
  the wormhole trail — a dotted wandering path with three small round
  holes — and the marginal vine, a stem with leaves that unfurls across
  the margin. They are the leaf's damage and its decoration, arriving at
  the pace of the reading, in the margin where the centuries put them.
- **Structure.** Two inline SVGs per boundary, defined once as `<symbol>`s
  and `<use>`d per boundary with per-instance path lengths: `.vine-rule`
  (a 220×24px horizontal stem-and-leaf path, stroke `--ink-soft`, leaves
  in `--gold` at 0.5) drawn via `stroke-dasharray/offset`; `.worm-trail`
  (a 60×140px vertical wandering dotted path in the left margin, holes as
  three `<circle>`s filled with the page background colour *behind* the
  leaf — holes must show the desk through the page, never black). Both
  `aria-hidden`, `pointer-events: none`.
- **Motion spec.** Trigger: boundary entry (IntersectionObserver 0.4 of
  the boundary rule). Vine: dashoffset animates over 800ms `--ease-lamp`,
  stem first, leaves fade in at 60% of the draw (they grow once the stem
  exists). Worm trail: dots appear sequentially along the path over
  1,100ms (the worm is slower than the vine — it is eating), holes fade in
  last, 200ms each. Draws fire once; scrolling back shows the finished
  margin.
- **Choreography timeline (v2).** t=0 boundary enters → t=0–800ms vine
  stem draws left→right (direction alternates per boundary — vines grow
  toward the light, and alternating keeps the margin from becoming a
  conveyor) → t=480–800ms vine leaves fade → t=300ms (overlapping) worm
  dots begin in the margin above the boundary → t=1,400ms third hole
  fades in → rest. The overlap is deliberate: margin life is concurrent,
  not queued.
- **State matrix (v2).** *Rest (pre-entry):* margin empty at that boundary
  (the undrawn state is clean parchment — absence, not a greyed preview).
  *Drawing:* as timeline. *Settled:* full ornament at rest opacities
  (vine 0.75, trail 0.6 — margin life is quieter than text). *Hover/
  focus/active:* none — the margin does not take input. *Scrolled-past:*
  settled. *Touch:* identical (entry-driven).
- **Breakpoint behaviour (v2).** ≥1200px: both ornaments, full size.
  768–1199px: vine only (the worm trail needs the wide left margin; in the
  folded margin it would collide with the fleck bar). <768px: vine only,
  scaled to 160×18px, worm trail omitted — small leaves have small
  margins, and a squeezed worm is a smudge (§9.9).
- **Edge cases & failure modes (v2).** *Path length mis-measured*
  (font/SVG scaling differences): lengths are set from `getTotalLength()`
  at setup, never hard-coded — a guessed dasharray leaves a half-drawn
  vine, the margin equivalent of a stranded reveal. *Many boundaries
  entering at once* (fast scroll to mid-page): draws queue at most 2
  concurrent; the rest settle instantly to drawn state. *Dark scheme:*
  worm holes fill with the dark-scheme page background token — the desk
  changes with the light (§2).
- **Accessibility spec (v2).** Fully decorative, `aria-hidden="true"`, no
  text alternative (a screen reader announcing "wormhole ornament" at
  every section break is vandalism). No motion sensitivity concerns
  beyond the global reduced-motion rule.
- **Content-merge.** The vine *is* the section divider — remove it and
  the leaves lose their separation; the worm trail lives in the margin
  the reading passes. Ornament here is structural punctuation, drawn in
  the leaf's own damage-and-gilt vocabulary.
- **Failure fallback.** No JS: both ornaments render fully drawn (SVG in
  its natural state; JS sets the undrawn dashoffset only for below-fold
  boundaries at setup).
- **Reduced-motion variant.** Fully drawn, static, from first paint.
- **Performance budget & mobile variant.** Stroke animation on ≤ 2
  boundaries concurrently; paths are short (< 600 units) so dash
  animation is paint-cheap. Mobile: vine only, per breakpoints.
- **Tokens.** `--ink-soft` (vine stem), `--gold` (vine leaves), `--ease-lamp`,
  `--dur-vine` (800ms), `--dur-worm` (1100ms).

---

### 6.10 Linger-to-raise-ghost hover (the core gesture)

- **What & why.** The theme's defining interaction, and the one every other
  ghost behaviour defers to: rest your attention on a paragraph — pointer
  held over it for a 400ms dwell — and its buried under-text rises:
  opacity to 0.55, blur from 1.4px to 0, the grey-violet sharpening into
  near-legibility, as if your gaze were the lamp held still. Move away and
  it sinks back over 600ms, unhurried, the way a memory releases. Attention
  is the instrument of recovery; this gesture is the whole theme in one
  paragraph.
- **Structure.** Each ghosted paragraph is a `.strata` (§6.3) whose ghost
  layer receives `--linger` (0→1) from a dwell controller: `pointerenter`
  starts a 400ms timer; timer completion (or continuous presence past
  400ms with < 4px pointer movement tolerance — a resting hand, not a
  passing one) ramps `--linger` in the lamp loop; `pointerleave` cancels
  or reverses. Ghost opacity = base(0.30) + `--linger` × 0.25; blur =
  1.4px × (1 − `--linger`). Keyboard path: the paragraph's footnote marker
  (§6.5 pattern) or the paragraph itself with `tabindex="0"` where the
  passage is a designated "reading passage" — focus raises the ghost
  identically (focus *is* lingering, for a keyboard reader).
- **Motion spec.** Dwell 400ms → rise 500ms `--ease-lamp` to 0.55 / blur 0
  → hold while lingered → release: sink 600ms `--ease-lamp` (slower than
  the rise: the past is quicker to summon than to dismiss). A 120ms
  grace period on pointerleave tolerates the pointer crossing the
  paragraph's own ghost overhang (the rotated layer extends ~10px beyond
  the surface box; leaving the *surface* box into the ghost's overhang
  must not cancel the linger).
- **Choreography timeline (v2).** t=0 pointer rests → t=400ms dwell
  confirmed; the passage's rubric initial (§6.6) gives a 6% brightness
  premonition (the leaf notices being read) → t=400–900ms ghost rises and
  sharpens → t=900ms full raise; if the passage has a contested word
  (§6.5), its old spelling rises with the layer → hold → pointer leaves →
  120ms grace → 600ms sink → base. Rapid re-entry within 300ms of a sink
  resumes from the current opacity (no restart from base — the lamp was
  only lowered).
- **State matrix (v2).** *Rest:* ghost 0.30, blur 1.4px. *Dwell-pending:*
  no visual change before 400ms (a passing pointer must never flicker a
  ghost — flickering ghosts are §9.4's slop). *Raised:* 0.55, blur 0.
  *Hover (short):* nothing — deliberately; the theme rewards staying, not
  brushing. *Focus:* raise on focus, sink on blur, same timings.
  *Active (pointer down on the passage):* raise locks at current value
  (a reader pressing the page flat) until pointer-up. *Scrolled-past:*
  if the passage scrolls out mid-raise, the raise completes and sinks —
  no stuck 0.55 layers off-screen. *Disabled:* passages under a modal
  (§11) ignore dwell. *Touch:* **long-press 450ms raises the ghost** and
  holds it until the next tap elsewhere or a scroll > 40px; a normal tap
  does nothing to the ghost (taps are for controls). This is specified,
  not improvised, because touch has no hover and the core gesture must
  survive the translation.
- **Breakpoint behaviour (v2).** ≥1200px and 768–1199px: as spec.
  <768px: dwell shortens to 350ms (thumbs rest less precisely), peak
  opacity 0.52, blur floor 0.2px (small-size ghost text at full sharpness
  competes with surface text in a narrow column).
- **Edge cases & failure modes (v2).** *Pointer resting while the page
  scrolls under it* (keyboard scroll with a parked mouse): if scroll
  moves the passage > 30px during dwell, the dwell restarts — the hand
  did not choose this paragraph, the page moved it there. *Two passages
  overlapped by the rotated ghost layer:* dwell is credited to the
  *surface* box only (hit-testing on the surface stratum), so ghosts can
  never raise each other. *Long-press on touch triggering text selection:*
  ghosted passages set `-webkit-touch-callout: none` on the ghost layer
  only — surface text remains selectable (readers copy quotations; the
  theme serves readers).
- **Accessibility spec (v2).** The raise is an enhancement of content that
  is fully available elsewhere (§6.17 panel + hidden provenance text);
  nothing is *only* reachable by lingering. Focus-raise parity per the
  state matrix; the raised state is not announced (atmosphere). Contrast
  at peak: ghost 0.55 in `--ghost-strong` ≈ 2.6:1 — artefact grade by
  design, with the full-contrast transcription one click away (§6.17),
  which is the theme's standing answer to ghost contrast everywhere.
  Motion: opacity/blur only, no positional movement — vestibular-safe.
- **Content-merge.** The gesture acts on the paragraph's own buried text.
  There is no widget, no overlay panel, no tooltip — the paragraph itself
  deepens. This element is the merge test's purest case.
- **Failure fallback.** No JS / no pointer events: ghost rests at 0.30,
  readable-as-artefact, with §6.17 carrying full legibility. The page
  loses a gesture, never a meaning.
- **Reduced-motion variant.** The raise becomes instant on dwell-confirm
  (opacity steps to 0.5, no blur change — blur stays 0.8px static). The
  *gesture* survives; the *animation* does not. This distinction is the
  theme's reduced-motion philosophy throughout: keep the meaning, remove
  the movement.
- **Performance budget & mobile variant.** One property (`--linger`) per
  lingered passage; at most one passage lingers at a time by construction.
  Blur is confined to the single raised ghost layer and released
  (`filter: none`) at sink end. Mobile: long-press path per state matrix;
  blur range halved.
- **Tokens.** `--ghost`, `--ghost-strong`, `--ease-lamp`, `--dwell-ghost`
  (400ms), `--dur-ghost-rise` (500ms), `--dur-ghost-sink` (600ms),
  `--ghost-peak` (0.55), `--ghost-blur` (1.4px).

### 6.11 Wax-seal click

- **What & why.** Readers of manuscripts marked what mattered — a seal
  pressed beside the passage they authenticated. Clicking a ghosted (or
  any markable) passage presses a wax seal in its right margin: a
  rubric-red bloom that scales from 0.96 with a soft squash, darkens at
  its centre where the signet struck, and stays — the passage is *noted*.
  Sealed passages are collected in the contents leaf (§6.15) as the
  visitor's own marginalia: "Your sealed passages." It is the theme's
  bookmark, made of the theme's material, and its click feedback, made of
  its physics — wax yields, it does not bounce.
- **Structure.** Markable passages carry `data-sealable` and a margin
  landing zone (the right margin at ≥1200px; an inline slot at the
  passage's head below that). The seal is an inline SVG (a 44px irregular
  wax circle — path with 2% radius noise, a stamped initial letter of the
  *site's* name in Fell, ring text none) rendered in `--rubric` with a
  radial gradient (centre `--rubric-bright` → edge `--rubric` darkened
  12%). State persists per-visitor in `localStorage` (passage IDs), and
  the seal button is a real `<button class="seal-btn">` (the visible wax
  is its background) with `aria-pressed`.
- **Motion spec.** Press: scale 0.96→1.0 with a squash (scaleY 0.94 at
  40% of the curve) over 320ms `--ease-scrape` — resistance, then the wax
  takes the stamp. A 1px darker ring blooms outward from the strike point
  and settles (opacity 0.5→0.18). Unsealing (second click): the seal
  *cracks* — a 180ms scale to 0.98 with a 1px split line drawn across it,
  then fades to a faint rubric ghost of itself (0.15) for the session
  (broken wax is evidence too), and is removed on next visit.
- **Choreography timeline (v2).** t=0 click → t=0–130ms squash phase
  (scale 0.96, scaleY 0.94, centre darkens) → t=130–320ms release to
  scale 1.0, ring bloom peaks at t=200ms → t=320ms seal at rest;
  the contents leaf count (§6.15) ticks +1 at t=320ms (the collection
  acknowledges after the press completes, not during). Keyboard: Enter/
  Space fire the same timeline (no squash distinction — the press is the
  press).
- **State matrix (v2).** *Rest (unsealed):* margin shows a faint seal
  *outline* on hover/focus only (a 1px `--rubric` circle at 0.35 — the
  invitation). *Hover:* outline at 0.6 + cursor pointer (system). *Focus:*
  outline at full + 2px offset ring. *Pressed/held:* squash mid-state.
  *Sealed:* wax at rest, `aria-pressed="true"`. *Sealed + hover:* wax
  lifts 4% brightness (touching the seal). *Disabled:* passages already
  sealed by an editorial "house seal" (the institution's own marked
  passages) render sealed and non-interactive, `aria-pressed` absent,
  labelled "Sealed by the house" — two kinds of authority, never confused.
  *Touch:* tap = click, identical timeline; target 44px.
- **Breakpoint behaviour (v2).** ≥1200px: seal in the right margin, 44px.
  768–1199px: seal shrinks to 36px, still marginal. <768px: no margin —
  the seal slot moves inline, right-aligned on the passage's head line,
  32px visual with a 44px touch target via padding.
- **Edge cases & failure modes (v2).** *localStorage unavailable*
  (private mode): seals persist for the session only, and the contents
  leaf says so in apparatus voice ("Seals kept for this visit only") —
  the theme never silently pretends permanence. *Passage edited between
  visits* (ID gone): orphan seals are dropped silently at load; the
  collection count derives from live DOM + storage intersection.
  *Seal spam* (a visitor sealing everything): allowed — it is their
  codex — but the contents leaf groups beyond 12 seals under "and N
  further passages", because a list, like a margin, has a size.
- **Accessibility spec (v2).** Real button, `aria-pressed`, label pattern
  "Seal this passage — [passage's first words]…" / "Remove your seal
  from…". Focus visible per state matrix. The seal's meaning is never
  colour-only: sealed state is also announced in the contents leaf list
  with the passage's title in text. Contrast: rubric on parchment 5.6:1
  for the wax's stamped initial (a graphic; the button's label carries
  the meaning).
- **Content-merge.** The seal lands beside the passage it authenticates
  and collects that passage into the visitor's own index. It marks
  content; it decorates nothing.
- **Failure fallback.** No JS: no seal buttons (they are JS-injected);
  passages carry their static provenance labels as usual. Nothing about
  the reading depends on sealing.
- **Reduced-motion variant.** Seal appears at rest scale instantly (a
  120ms opacity fade is permitted — wax without squash is still wax);
  unseal crack becomes an instant swap to the faint state.
- **Performance budget & mobile variant.** One SVG reused via `<use>`;
  press animation is transform-only on a 44px element. Storage writes are
  debounced to press-end. Mobile: inline slot per breakpoints.
- **Tokens.** `--rubric`, `--rubric-bright`, `--ease-scrape`,
  `--dur-seal` (320ms), `--seal-size` (44px).

### 6.12 Scraped-leaf transition + skeleton leaves

- **What & why.** Moving between pages of this site is moving between
  leaves of one codex, and the codex's own verb for a new page is
  *scraping*: a pale vellum wipe crosses the screen — pumice across
  parchment — clearing the old text as the new leaf's surface text arrives
  first and its ghosts settle after, exactly as a rewritten leaf was made.
  While a leaf loads, its skeleton shows the same order: pale umber
  skeleton leaves (the scraped surface, text-shaped) that gain surface
  text first, ghosts last. Even the plumbing of the site obeys the
  metaphor, so there is no moment where the visitor leaves the world.
- **Structure.** Transition: a fixed `.scrape` overlay (parchment texture,
  `--parchment-deep` leading edge with a 2px `--ink-soft` knife line),
  translated across on route change in SPA builds; in MPA builds it is a
  view-transition named element with the same keyframes. Skeleton: leaf
  components render `.skeleton-leaf` — parchment-deep blocks shaped like
  the real leaf (title bar, text lines at 92%/100%/84% widths, an arch
  outline where a plate will sit), never grey rectangles (§9.12): the
  skeleton is a *scraped leaf*, so its shapes are the content's shapes in
  umber.
- **Motion spec.** Transition: wipe in 260ms `--ease-scrape` (fast, with
  resistance), hold 60ms while the new route mounts, wipe out 240ms
  revealing the new leaf's surface text already at full density; the new
  leaf's ghosts then rise per §6.1/§6.2 rules (never during the wipe).
  Total ≤ 560ms. Skeleton: a slow light pass (§6.2's band at 30% strength)
  crosses the skeleton leaf every 2.4s — the lamp waiting; surface content
  replaces skeleton regions in DOM order as data arrives (title → body →
  plates → ghosts), each region fading 200ms as it lands.
- **Choreography timeline (v2).** Navigation t=0 click → t=0–260ms scrape
  covers → t=260–320ms route swap under cover → t=320–560ms scrape
  clears from the opposite edge (a knife does not retrace) → t=560ms new
  leaf live; its hero ghost-up (§6.1) starts its own clock from here.
  Back-navigation: the scrape reverses direction (the knife returns) —
  direction encodes history, a detail visitors feel without naming.
  Skeleton: t=0 leaf shell paints → regions land in order as resolved →
  last region + 200ms → skeleton retires; if all data resolves < 300ms,
  the skeleton never appears (a leaf that arrives instantly was never
  scraped).
- **State matrix (v2).** *Idle:* overlay parked off-screen. *Covering /
  covered / clearing:* as timeline. *Interrupted* (user clicks another
  link mid-wipe): the current wipe completes its cover phase (≤260ms)
  then retargets — never reverses mid-stroke (a knife lifted mid-scrape
  tears the leaf). *Focus:* focus moves to the new page's H1 at the
  covered moment (t=260ms), announced via the route announcer — the wipe
  is visual, the navigation is semantic, and they are synchronised at
  the covered beat. *Disabled:* links during the covered window are
  inert (the covered page is not there to click). *Touch:* identical;
  swipe-back gestures use the platform's own transition, not the scrape
  (never fight the OS gesture).
- **Breakpoint behaviour (v2).** Identical at all sizes; at <768px the
  knife line softens (1px, `--ink-soft` at 0.6) — a full knife edge on a
  small leaf reads as a glitch bar.
- **Edge cases & failure modes (v2).** *Slow route (> 1.2s under cover):*
  the covered state grows a skeleton leaf beneath the scrape's trailing
  edge as it begins clearing at 1.2s regardless — the visitor is never
  stared at by a blank covered screen; the scrape becomes the skeleton's
  introduction. *View Transitions API unsupported:* fall back to a 200ms
  parchment fade (the scrape's polite cousin) — never to no transition,
  and never to a spinner. *Prefetch:* hover/focus on a link prefetches
  the route so the covered window stays ≤ 320ms in the common case.
- **Accessibility spec (v2).** Route changes are announced by a visually
  hidden `aria-live="polite"` announcer ("Leaf: The Versions") at the
  covered beat; focus management per state matrix. The wipe is a
  full-screen motion — under `prefers-reduced-motion` it is replaced by
  an instant swap with a 120ms fade (below). Skeleton regions carry
  `aria-busy` on the leaf container, released when the last region lands.
- **Content-merge.** The transition is the codex's own material action
  and the skeleton is the incoming leaf's own shape. Neither is a branded
  overlay pasted over the experience; both are the book being a book.
- **Failure fallback.** Transition failure (JS error mid-wipe): the
  overlay has a hard 900ms self-retire timer — it can never trap the
  visitor under parchment. No-JS MPA: plain navigation, no wipe, and the
  site loses nothing but a gesture.
- **Reduced-motion variant.** No scrape: instant route swap with a 120ms
  crossfade; skeletons static (no lamp pass).
- **Performance budget & mobile variant.** The overlay is one fixed
  layer, transform-only; the wipe must never delay the route's LCP —
  the new leaf paints *under* the clearing scrape, so perceived and
  actual readiness coincide. Mobile: identical timings.
- **Tokens.** `--parchment`, `--parchment-deep`, `--ink-soft`,
  `--ease-scrape`, `--dur-scrape-in` (260ms), `--dur-scrape-out` (240ms).

---

### Page-family elements

### 6.13 Running-title navigation

- **What & why.** A manuscript's navigation is its running title — the
  book's name repeated at the head of every leaf — and its foliation. This
  site's header is that: the house name in IM Fell SC as a running title,
  the current leaf's name beside it as the chapter heading, and folio-style
  links ("The House", "The Versions", "The Plates", "Correspondence") set
  as a contents line, not a menu bar. On scroll the header does not shrink
  or transform into a pill; it *rests* — a hairline vine rule (§6.9)
  draws beneath it and the parchment behind it deepens one step, the way a
  held page settles in the hand.
- **Structure.** `<header class="running-head">`: left, the running title
  (site name, Fell SC 15px, letterspaced 0.14em); centre/right, the nav
  as an inline list of text links with §11's rubric underline draw; the
  current leaf's link carries a small rubricated pilcrow (¶) before it —
  the apparatus marks where you are in the codex. A `data-leaf` header
  inside each leaf ("Leaf II of V — The Versions") mirrors the navigation
  semantically for assistive tech and print. Mobile: the contents line
  collapses behind a "Contents" button opening §6.15 as an overlay leaf.
- **Motion spec.** On first scroll past 120px: the vine rule under the
  header draws over 800ms `--ease-lamp` (once), header background gains
  `--parchment-deep` at 0.55 over 300ms. Link underlines: rubric line
  draws left→right 280ms `--ease-lamp` on hover/focus. The current-leaf
  pilcrow flares once (§6.6 spec) when its leaf is entered. Nothing else
  moves — a running title's dignity is stillness.
- **Choreography timeline (v2).** Page load: header present from first
  paint (it is surface apparatus, never animated in). First scroll >
  120px → rule draw 800ms + background settle overlapping → rest. Leaf
  change (scroll): pilcrow migrates — old pilcrow fades 150ms, new
  leaf's pilcrow flares 450ms at the moment the leaf's header crosses
  40% viewport. Route change: header persists through the scrape (§6.12)
  — it is the codex's head, common to all leaves.
- **State matrix (v2).** *Rest:* as spec. *Hover (link):* underline draw.
  *Focus:* underline draw + 2px `--rubric` outline offset 3px. *Active
  (current leaf):* pilcrow + `--ink` full weight; other links
  `--ink-soft` until hovered. *Scrolled-past:* the settled state (rule
  drawn, background deepened). *Disabled:* n/a. *Touch:* links are 44px
  tall hit rows in the contents overlay; inline header shows running
  title + Contents button only.
- **Breakpoint behaviour (v2).** ≥1200px: full contents line inline.
  768–1199px: contents line inline but provenance labels drop from leaf
  headers to save width. <768px: running title + Contents button;
  §6.8's fleck line moves into the bar beneath (§6.8 breakpoints).
- **Edge cases & failure modes (v2).** *Long house names / long leaf
  titles:* the running title truncates with an ellipsis at 40vw — the
  full name lives in the footer colophon (§6.16); a wrapped two-line
  running head is forbidden (it breaks the leaf's top margin rhythm).
  *Sticky header + pinned passage (§6.4):* the header is `z-index` below
  the pinned stage's own apparatus but above leaves; during the pin it
  rests in settled state — no double ceremony.
- **Accessibility spec (v2).** Real `<nav>` with `aria-label="Contents of
  the codex"`; current leaf marked `aria-current="page"` (the pilcrow is
  its visual twin — state never carried by ornament alone). Skip link is
  styled as the first line of the contents leaf ("Pass to the text").
  Focus order: skip → running title (home link) → contents links.
- **Content-merge.** The header is the codex's own furniture, naming the
  actual book and its actual leaves. Its one animation (the vine rule)
  is §6.9's ornament doing structural duty as the head rule.
- **Failure fallback.** No JS: full header, contents inline at all sizes
  (the overlay behaviour is JS-added; without JS the contents list simply
  sits open under the running title on mobile — longer, complete).
- **Reduced-motion variant.** No rule draw (rule present statically), no
  pilcrow flare; background settle instant.
- **Performance budget & mobile variant.** Header is static DOM; the
  scroll listener is the shared lamp loop; zero per-frame writes except
  during the one-time draw. Mobile: overlay contents per §6.15.
- **Tokens.** `--parchment-deep`, `--ink`, `--ink-soft`, `--rubric`,
  `--ease-lamp`, `--dur-underline` (280ms).

### 6.14 Plate cards (recovered-leaf cards)

- **What & why.** Where the site lists things — the archive's leaves, the
  house's garments, the author's books — each entry is a *plate card*: a
  small leaf of its own, carrying the entry's plate (image in a shallow
  arch, §6.7's frame at card scale), its surface title and description,
  and — the theme's signature — the entry's *earlier* description ghosted
  beneath the current one, one line of it, angled, waiting for a linger
  (§6.10). A listing in this theme is a row of small palimpsests: every
  object shows its present face and admits its past.
- **Structure.** `<article class="plate-card">`: arch-clipped plate image
  (aspect 4:3, shallower arch than §6.7), `<h3>` surface title, surface
  description (2 lines), a one-line `.strata` mini-block whose ghost line
  is the entry's earlier description (from the strata file), and a
  provenance label ("Previously described · 2016 catalogue"). The whole
  card is one link (stretched-link pattern) except the seal button
  (§6.11) where the entry is sealable.
- **Motion spec.** Entry: cards settle in reading order, 70ms stagger,
  450ms `--ease-settle`, ink density 85%→100%. Plate inside: scale
  1.05→1, 700ms. Hover: the card's leaf lifts — shadow deepens (a leaf
  raised off the desk: `box-shadow` from 0 1px 2px to 0 14px 28px in
  `--ink` at 0.16 alpha) over 260ms, and the mini-ghost rises to 0.45
  (a half-linger, §6.10's spec at reduced peak — the card invites, the
  passage commits). The arch's keystone fleck (§6.8 gold) brightens.
- **Choreography timeline (v2).** Grid enters → cards settle staggered
  (70ms × index-in-row) → plates scale within → rest. Hover: t=0 shadow
  begins → t=180ms ghost reaches 0.45 → t=260ms shadow full. Leave:
  ghost sinks 400ms, shadow 300ms. A grid of 12 cards entering at once
  caps the stagger at index 6 (later cards share the last beat — a
  rubricator does not fall behind the reader, §6.6's rule).
- **State matrix (v2).** *Rest:* flat on the desk, ghost at 0.30.
  *Hover:* lifted, ghost 0.45. *Focus-within:* same lift as hover +
  arch-shaped focus outline on the card. *Active (press):* shadow
  collapses to 0 4px 10px (the leaf pressed back to the desk) 120ms.
  *Scrolled-past:* settled, no change. *Disabled (entry unavailable /
  out of the collection):* the card is *scraped* — plate desaturated to
  parchment tones, surface text in `--ink-soft`, a rubric "Withdrawn"
  stamp (§11 badge) across the arch; it remains readable history, never
  a greyed-out afterthought. *Touch:* no hover lift; the mini-ghost is
  raised by the card's long-press (§6.10 touch rule) or not at all —
  cards are for tapping through.
- **Breakpoint behaviour (v2).** ≥1200px: 3 cards per row in the margins
  grid. 768–1199px: 2 per row. <768px: 1 per row, plate aspect 16:10
  (a wide small leaf), mini-ghost line truncates to the earlier
  description's first 9 words + ellipsis (the full line lives on the
  detail leaf).
- **Edge cases & failure modes (v2).** *Entry with no earlier
  description:* no ghost line and no fake one (§9.1) — the card carries a
  provenance label "First described here" instead; absence is honest
  apparatus. *Missing plate image:* §6.7's described-miniature fallback
  (parchment-deep arch + rubricated initial). *Very long titles:* clamp
  at 2 lines with ellipsis; the card grid's row height is set by the
  tallest card so lifts never shift neighbours.
- **Accessibility spec (v2).** One link per card with a single accessible
  name (title + provenance); the ghost line is `aria-hidden` with its
  text available on the detail leaf. Focus outline arch-shaped, 2px
  `--rubric`. The lift is shadow-only (no positional transform), so
  vestibular risk is nil and layout never shifts. Touch target: the
  whole card, ≥ 44px in every dimension by construction.
- **Content-merge.** The card's ghost is the entry's own earlier
  description; its plate is the entry's own image in the theme's frame;
  its lift is the leaf it is made of. A plate card is a miniature of the
  whole theme, which is exactly what a listing should be.
- **Failure fallback.** No JS: cards static, fully inked, ghosts at
  0.30, links live. Nothing about navigation depends on the settle.
- **Reduced-motion variant.** No settle, no lift, no ghost rise on hover
  (focus still outlines). Cards are printed plates.
- **Performance budget & mobile variant.** Shadow transitions on ≤ 12
  cards; image loading lazy below the fold with aspect reserved (no
  layout shift — a shifting grid on a parchment ground reads as the desk
  moving). Mobile: per breakpoints; stagger reduced to 40ms.
- **Tokens.** `--parchment`, `--parchment-deep`, `--ink`, `--ink-soft`,
  `--ghost`, `--gold`, `--rubric`, `--ease-settle`, `--ease-lamp`.

### 6.15 Contents-of-the-codex leaf (index & sealed passages)

- **What & why.** Every codex opens with its contents; this site's
  contents leaf is a page (and an overlay on mobile) listing the codex's
  leaves with their folios — and, uniquely, the visitor's own chapter:
  "Your sealed passages", the passages they marked with §6.11's wax,
  listed by their titles with their provenance. It is navigation as the
  book understands it, and it closes the seal system's loop: marking
  passages builds a personal contents that brings the reader back to
  them. A contents page that only lists sections is furniture; one that
  lists *your* seals is a reason to return.
- **Structure.** `<section class="contents-leaf">`: two lists. (1) The
  codex: each leaf as a row — folio numeral (EB Garamond tabular), title
  (Fell), a one-line surface description, and the leaf's ghost count in
  apparatus ("3 recovered layers") where > 0. (2) Your seals: rows of
  sealed passage titles + their leaf names, each row a link landing on
  the passage (with a one-time ghost raise on arrival, §6.10 fired
  programmatically). Empty state per §12's voice. As a mobile overlay:
  the same leaf, full-screen, opened from §6.13's Contents button,
  closed by its own rubricated "Finis" link at the foot.
- **Motion spec.** Rows settle on entry, 50ms stagger, §5 reveal spec.
  Row hover: the row's folio numeral rubricates (§6.6 flare at 200ms —
  faster than passage flares; apparatus responds briskly) and a vine
  tick (§6.9) draws at the row's left. Arrival-from-seal-list: the target
  passage's leaf scrolls into view (smooth 700ms or instant), then its
  ghost raises once (§6.10 timeline compressed: dwell waived, rise
  500ms) — the contents leaf *shows you what you sealed*, it doesn't
  just point.
- **Choreography timeline (v2).** Entry → rows settle (50ms stagger) →
  the seals list (if any) settles last, 150ms after the codex list (your
  chapter is the contents' final entry, as a colophon follows a text).
  Seal-arrival: click row → scrape-lite (a 300ms parchment fade, not the
  full §6.12 wipe — same-page travel is a leaf-turn, not a re-scraping)
  → scroll → ghost raise → a seal pulse (§6.11 wax brightens 6% once).
- **State matrix (v2).** *Rest:* lists settled. *Hover/focus (row):*
  numeral rubricates, vine tick, row background `--parchment-deep` at
  0.4. *Active:* the current page's row carries the pilcrow (§6.13).
  *Empty (no seals):* the seals chapter shows its empty-state text (§12)
  and a single line of guidance — never a blank chapter. *Disabled:*
  leaves that are withdrawn (§6.14) appear struck through in
  `--ink-soft` with "withdrawn" apparatus, unlinked — a contents records
  what the codex held, including its losses. *Touch:* rows are 52px —
  contents are tapped, not hovered.
- **Breakpoint behaviour (v2).** ≥1200px: a page leaf in the standard
  column; the two lists side by side (codex 7 cols, seals 5 cols).
  768–1199px: stacked, codex first. <768px: primarily the overlay form;
  as a page it stacks with 52px rows.
- **Edge cases & failure modes (v2).** *Seal storage unavailable:*
  session-only seals per §6.11, and the chapter head says so. *A sealed
  passage on a leaf that has since been withdrawn:* the row remains,
  marked withdrawn, linking to the leaf's withdrawal note — the reader's
  history is not rewritten by the house's. *Very large codices (> 24
  leaves):* the codex list groups by part with Fell SC part-titles;
  seals never group (they are few by nature, §6.11's cap display at 12).
- **Accessibility spec (v2).** Two `<nav>`/list landmarks with headings
  ("Contents of the codex", "Your sealed passages"); rows are links with
  full names (title + leaf + provenance in the name where needed).
  The ghost-count apparatus is text, not icon. Focus order follows the
  visual order; the overlay form traps focus politely and returns it to
  the Contents button on close, `Esc` closes.
- **Content-merge.** The contents lists the site's real leaves and the
  visitor's real seals; its ornaments (folio numerals, vine ticks) are
  the apparatus of the lists themselves.
- **Failure fallback.** No JS: a static contents page with both lists
  (seals chapter shows its session note — without JS there are no seals,
  and the chapter says exactly that, in voice, §12).
- **Reduced-motion variant.** Rows pre-settled; seal-arrival scrolls
  instantly and raises the ghost instantly (§6.10's reduced rule).
- **Performance budget & mobile variant.** Lists are DOM-light; the
  arrival sequence reuses §6.10/§6.12 machinery. Mobile: overlay form
  per breakpoints.
- **Tokens.** `--ink`, `--ink-soft`, `--rubric`, `--parchment-deep`,
  `--gold`, `--ease-settle`, `--ease-lamp`.

---

### 6.16 Colophon-of-layers footer

- **What & why.** A manuscript ends with a colophon: the scribe's own
  note — who wrote this, where, from what exemplars. This site's footer
  is that colophon, and in this theme it lists the *layers*: the house's
  current imprint line, and beneath it — ghosted, angled, at rest
  opacity — the imprint lines of its earlier selves (the old address,
  the founding name, the previous motto). The footer is the one place
  every visitor reaches the bottom of the leaf, and the theme spends its
  last moment on its thesis: even the small print has a past. Practical
  apparatus (contact, legal, social) sits in the colophon's margins in
  apparatus type — a colophon is a working note, not a billboard.
- **Structure.** `<footer class="colophon">`: centred (the theme's one
  centred block besides the title leaf, §4): the house mark (rubricated
  initial of the house name), the current imprint (Fell, surface), the
  strata of earlier imprints (ghost layers, §4 geometry, static), a
  hairline vine rule (§6.9, pre-drawn), then the apparatus row: contact
  link, legal links, and the layer count of the whole site ("This codex:
  14 leaves · 31 recovered layers") computed from the DOM.
- **Motion spec.** Entry: the current imprint settles (§5); the earlier
  imprints are *already there* at rest opacity — the footer does not
  perform its ghosts (a colophon is read, not staged), with one
  exception: the final gold fleck of §6.8's line sits at the colophon's
  head and gives its completion shimmer as the footer enters. Apparatus
  links use §11's underline draw.
- **Choreography timeline (v2).** Footer enters → fleck shimmer (900ms,
  §6.8) → imprint settle overlaps at t=150ms → rest. That is all. The
  restraint is the spec: after §6.4's ceremony, the footer's stillness
  is the cadence.
- **State matrix (v2).** *Rest:* complete and static. *Hover/focus
  (links):* underline draw / outline per §6.13. *Hover (earlier
  imprints):* each earlier imprint is a linger target (§6.10 at reduced
  peak 0.45) — the curious may raise the old address. *Active:* n/a.
  *Scrolled-past:* n/a (it is the end). *Touch:* long-press raises
  imprints per §6.10's touch rule.
- **Breakpoint behaviour (v2).** ≥1200px: as spec, apparatus in one row.
  768–1199px: apparatus wraps to two rows. <768px: centred stack;
  earlier imprints' angle reduces to −1° (§6.1 mobile geometry).
- **Edge cases & failure modes (v2).** *A house with no earlier
  imprints:* the footer is a plain colophon (mark, imprint, apparatus)
  — no invented predecessors (§9.1 applies to footers too, especially to
  footers). *Legal links must never be ghosted:* law is surface text,
  always, at full contrast — the §10 gate checks this by selector.
- **Accessibility spec (v2).** `<footer>` landmark; earlier imprints are
  `aria-hidden` visual layers whose text is duplicated in a visually
  hidden list ("Earlier imprints: …") — or, where an earlier imprint is
  content the visitor may need (an old address for returns), it is
  surface text in the apparatus row, never only a ghost. Links ≥ 44px
  touch height on mobile via padding.
- **Content-merge.** The footer's ghosts are the house's documented
  earlier imprints from the strata file — the same law as every ghost on
  the leaf.
- **Failure fallback.** No JS: identical (the footer has no JS-dependent
  state beyond the shimmer).
- **Reduced-motion variant.** No shimmer. The colophon is print.
- **Performance budget & mobile variant.** Negligible; the layer count
  is one DOM query at build/load. Mobile: per breakpoints.
- **Tokens.** `--ink`, `--ink-soft`, `--ghost`, `--rubric`, `--gold`,
  `--ease-settle`.

### 6.17 The transcription panel (the reading room)

- **What & why.** Every ghost on this leaf is artefact-grade contrast by
  design (§2) — which creates a debt: a visitor who wants to actually
  *read* the under-text, all of it, comfortably, must be given a way.
  Scholars publish transcriptions beside facsimiles; this panel is the
  transcription. A surface-text control — "Read the under-text" — present
  on every leaf that carries ghosts, opens a panel (a leaf laid over the
  leaf) listing every ghost passage on the page at full ink contrast, in
  reading order, each with its provenance label and its surface twin
  beneath it in italic. It is the theme's accessibility keystone and,
  not coincidentally, one of its most-loved features: many visitors
  read the whole page twice — once on the leaf, once in the transcription.
- **Structure.** `<button class="transcribe-btn">` in the leaf's apparatus
  (and in §6.4's stage) + `<div class="transcription" role="dialog"
  aria-modal="false">` as a right-side leaf (desktop) / full-screen leaf
  (mobile): entries generated from the page's strata data (the same
  source the ghost layers render from — one source of truth, so the
  transcription can never drift from the ghosts). Each entry: provenance
  label (Fell SC), under-text (EB Garamond 19px, `--ink`, full
  contrast), surface text (italic, `--ink-soft`).
- **Motion spec.** Open: the panel leaf slides from the right margin
  over 380ms `--ease-settle` with its own faint scrape edge (§6.12's
  knife line at 40% strength) — a leaf laid across a leaf. Entries
  settle in order, 40ms stagger. Close reverses (300ms). While open, the
  underlying leaf's ghosts rise slightly (to 0.4) so the eye can pair
  panel entries with their places on the leaf — the facsimile and its
  transcription illuminate each other.
- **Choreography timeline (v2).** t=0 activate → t=0–380ms panel slides
  → t=120ms first entry settles → entries stagger 40ms → t≈600ms panel
  complete; focus lands on the panel's heading. Pairing hover: hovering
  an entry raises its ghost on the leaf to 0.55 (§6.10 peak) and scrolls
  the leaf to it if needed (smooth, 500ms). Close: focus returns to the
  invoking button.
- **State matrix (v2).** *Closed:* button at rest (apparatus style,
  rubric underline on hover). *Open:* as spec; the leaf behind remains
  scrollable on desktop (non-modal — it is a reading aid, not a task).
  *Focus:* panel is a labelled region; `Esc` closes from anywhere inside
  it. *Empty:* a leaf with no ghosts has no button — the control's
  absence is the honest signal. *Disabled:* n/a. *Touch:* full-screen
  form; entries 19px; close button 44px at the panel's head.
- **Breakpoint behaviour (v2).** ≥1200px: panel 420px from the right,
  leaf visible beside it (pairing works). 768–1199px: panel 60vw.
  <768px: full-screen; pairing hover becomes pairing *tap* which closes
  the panel and raises the ghost on the leaf (§6.10 touch raise) — on a
  small screen you cannot look at both, so the panel hands you over.
- **Edge cases & failure modes (v2).** *Strata data missing for a
  rendered ghost* (build error): the panel lists the passage as
  "Transcription wanting" in apparatus voice and the §10 gate fails the
  build — a ghost without a transcription is a defect, not a mystery.
  *Very many ghosts on one leaf:* §4 caps ghosted passages at one per
  leaf section; a long page may still yield 8+ entries — the panel
  scrolls internally, entries grouped by leaf with folio heads.
- **Accessibility spec (v2).** This element *is* the accessibility spec
  for the theme's ghost system: full-contrast (7.5:1) renderings of all
  under-text, in reading order, reachable by keyboard in ≤ 2 stops from
  any ghosted passage (the footnote markers of §6.5/§6.10 deep-link
  here). Dialog semantics without modal trapping (desktop), labelled
  "Transcription — the under-text of this leaf". Screen-reader users
  may never need it (ghosts' content is also in hidden provenance text),
  but low-vision sighted users do — it exists for them first.
- **Content-merge.** The panel contains nothing but the page's own
  under-texts and their surface twins. It is the leaf, transcribed.
- **Failure fallback.** No JS: the button is absent and instead each
  ghosted passage carries its transcription as a static, full-contrast
  blockquote beneath it in the no-JS stylesheet — heavier, complete,
  honest. (The no-JS leaf is a scholarly edition with footnotes; the JS
  leaf is the facsimile.)
- **Reduced-motion variant.** Panel appears with a 120ms fade; no slide,
  no stagger; pairing raise is instant per §6.10's reduced rule.
- **Performance budget & mobile variant.** Panel DOM is built once per
  page from strata data (≤ 12 entries typical); slide is transform-only.
  Mobile: full-screen form per breakpoints.
- **Tokens.** `--parchment`, `--ink`, `--ink-soft`, `--rubric`,
  `--ghost-strong`, `--ease-settle`, `--ease-scrape` (edge), 
  `--dur-panel` (380ms).

### 6.18 Procession of recovered leaves

- **What & why.** On listing and archive leaves, a slow horizontal band
  carries the collection's recovered fragments past the reader — plate
  thumbnails, a line of under-text, a dated label — drifting at the pace
  of a procession, not a ticker: 90 seconds for a full pass. It is the
  theme's only marquee (§5), and it exists because an archive's wealth is
  cumulative: the band says *there is more in the vault than this page
  can hold*, in the vault's own objects. Each fragment in the band is a
  real entry and a real link; the procession is a shelf, moving slowly
  enough to browse.
- **Structure.** `<div class="procession">` containing a duplicated track
  of `.fragment` items (plate thumb in a shallow arch §6.14, one ghost
  line, provenance label), `animation: procession 90s linear infinite`
  on the track with `translateX` −50% loop; the duplication is marked
  `aria-hidden` on the second copy and the first copy's items are the
  real links. Pause conditions: hover, focus-within, and
  `prefers-reduced-motion` (static, scrollable horizontally instead).
- **Motion spec.** Drift: 90s per full track pass, `--ease-drift`
  (linear — a procession does not ease). Fragments' ghost lines sit at
  0.34; a fragment under the raking light's fixed mid-band lamp position
  brightens to 0.5 as it passes the band's centre — the vault's lamp is
  stationary; the treasures move. Pause on hover/focus is instant (a
  hand on the shelf).
- **Choreography timeline (v2).** Continuous: fragment enters right →
  crosses centre (brightens over its 6s central window) → exits left →
  loops. On pause: drift halts within one frame; on resume, continues
  from the same offset (no jump — the shelf was held, not reset).
- **State matrix (v2).** *Rest:* drifting. *Hover:* paused; the hovered
  fragment lifts per §6.14's card hover. *Focus-within:* paused for as
  long as focus remains in the band (a keyboard reader browses a still
  shelf). *Active:* fragment links behave as §6.14 cards. *Scrolled-
  past:* the band's animation is paused off-screen (IntersectionObserver
  toggles `animation-play-state`) — a procession nobody watches does not
  march (battery law). *Touch:* drift continues; swipe on the band
  scrolls it manually and drift resumes after 4s idle.
- **Breakpoint behaviour (v2).** ≥1200px: band height 190px, fragments
  150px wide. 768–1199px: 170px / 132px. <768px: 150px / 118px, drift
  slows to 110s (smaller shelf, same dignity — faster relative motion on
  a small screen reads as a ticker, §9.13).
- **Edge cases & failure modes (v2).** *Fewer than 6 fragments:* the
  band does not loop (a procession of three is a queue) — it renders as
  a static shelf. *Fragment without a plate:* its ghost line and label
  carry the fragment (text fragments are first-class in an archive).
  *Duplicate-track seam:* track width is exactly 2× the set; the loop
  point is measured from the rendered set width at setup and on resize,
  never assumed.
- **Accessibility spec (v2).** First-copy fragments are ordinary links
  in a list (the track is a `<ul>`); the duplicate is `aria-hidden` and
  focus-stripped (`tabindex="-1"` on its links — or better, the
  duplicate's items are non-interactive spans). Drift pauses on
  focus-within (above) and is fully replaced by a scrollable static
  shelf under reduced motion. No fragment's information exists only in
  the band — each is a §6.14 card elsewhere on the listing leaf.
- **Content-merge.** The band's fragments are the collection's actual
  entries with their actual ghost lines. It is the listing, in motion,
  not a decorative ticker of slogans.
- **Failure fallback.** No JS/CSS-animation: a static, horizontally
  scrollable shelf of the same fragments — complete, browsable, still.
- **Reduced-motion variant.** The static scrollable shelf. No drift,
  ever, under any setting.
- **Performance budget & mobile variant.** One animated transform on
  one track; thumbnails are the page's smallest image derivative
  (≤ 30KB each, lazy). Off-screen pause per state matrix. Mobile: per
  breakpoints.
- **Tokens.** `--gold`, `--ghost`, `--ink-soft`, `--parchment-deep`,
  `--dur-procession` (90s), `--ease-drift`.

### 6.19 The correspondence leaf (form)

- **What & why.** The theme's conversion moment — booking a viewing,
  requesting a transcription, writing to the house — is a letter, not a
  form funnel: a single leaf of ruled lines on which the visitor writes,
  in the house's own understanding that correspondence is slow and meant.
  Fields are ruled parchment lines with Fell SC labels above them (never
  floating labels — a letter does not animate its address lines); the
  submit is a wax seal (§6.11's material) labelled with the act ("Seal
  & send"); errors are written in the margin by the house's archivist,
  in rubric, beside the line they concern — marginalia with a duty of
  care. For a heritage house this leaf converts *because* it is slow:
  it filters for the visitors the house actually wants.
- **Structure.** `<form class="correspondence">`: label-above fields
  (name, email, the matter — a `<select>` styled as a ruled line with a
  rubric pilcrow marker, message as a multi-line ruled leaf), each field
  a `.field` with an adjacent `.margin-note` slot for its error/success
  note. The submit button is §11's seal-button. A provenance line under
  the head states the terms of correspondence in voice (§12): "Letters
  are answered within three working days, in the order they were
  sealed." Honeypot and timing traps are invisible apparatus, never
  themed theatre.
- **Motion spec.** Focus: the field's ruled line rubricates — a 1px
  `--rubric` line draws under the field over 280ms (§6.13's underline)
  and the label small-caps deepens to `--ink`. Error arrival: the margin
  note writes in — opacity + a 2px settle, 240ms `--ease-settle`, with
  its rubric pilcrow flaring (§6.6 at 200ms). Submit: the seal-button
  performs §6.11's press (320ms squash), the leaf gives one scrape-lite
  shimmer (§6.15's 300ms fade) and the success leaf replaces the form:
  a sealed confirmation with the visitor's own reference ("Your letter
  is № 214 in the book") — the number is the real submission ID,
  formatted, never invented (§12).
- **Choreography timeline (v2).** Field focus → line draw 280ms →
  typing (no motion — writing is the visitor's) → blur with error →
  note writes in at +120ms after blur (the archivist reads first) →
  submit press 320ms → 300ms fade → success leaf settles 450ms with its
  seal already pressed (it was pressed by the act) and its reference
  ticking in via §6.8's counter machinery (discrete, 240ms).
- **State matrix (v2).** *Rest:* ruled lines in `--ink-soft`, labels
  apparatus. *Focus:* per motion spec; focus is never colour-only (the
  drawn line is a shape). *Filled:* the line returns to ink; a small
  gold fleck marks completed fields in the margin (the apparatus keeps
  the tally). *Error:* rubric margin note + the field's line in
  `--rubric` at 60%; the note names the repair, not the fault (§12).
  *Disabled (submitting):* the seal is mid-press; fields inert; a
  second submit is impossible (the letter is being sealed). *Success:*
  the success leaf (below). *Touch:* fields are 52px rows; the margin
  note moves *below* its field (there is no margin on a phone — the
  archivist writes under the line instead, same voice).
- **Breakpoint behaviour (v2).** ≥1200px: margin notes in the right
  margin (the leaf's working margin, §4). 768–1199px: notes below
  fields. <768px: notes below fields, form column full width, seal
  button full-width at 52px — a letter sealed with the whole thumb.
- **Edge cases & failure modes (v2).** *Submission failure (network):*
  the success leaf never appears; instead the archivist's note appears
  at the form's head: the letter could not be sealed, it is kept
  (values intact), try again — and the draft is stored locally so a
  dead connection never eats a written letter. *Validation on submit
  with multiple errors:* notes arrive staggered 90ms apart in field
  order (the archivist works down the page), focus moves to the first
  error's field. *Long messages:* the message leaf grows (auto-resize
  capped at 40vh with internal scroll) — ruled lines continue; the
  leaf does not sprout a grey scrollbar aesthetic, the rules simply
  continue.
- **Accessibility spec (v2).** Labels are real `<label>`s, always
  visible; errors are `aria-describedby`-linked and announced via a
  polite live region at the form head summarising count ("Two notes
  from the archivist — see the margins"). Required fields marked in
  text ("required" in the label's apparatus line), never by colour or
  asterisk alone. Focus order is field order; the success leaf's
  heading receives focus on arrival. Contrast: notes in `--rubric`
  5.6:1 pass AA at 15px+; field text `--ink` 7.5:1.
- **Content-merge.** The form's every behaviour is the letter's own:
  ruled lines are written on, the seal sends it, the margin corrects
  it, the reference numbers it in the house's book. Remove the theme
  and the form is unbuildable — that is the merge test at its strictest.
- **Failure fallback.** No JS: a plain, fully working form (standard
  submit, server-rendered errors in the same margin-note positions via
  the no-JS stylesheet). The correspondence never depends on the
  animation layer to arrive.
- **Reduced-motion variant.** Line draws instant, notes fade at 120ms,
  seal press per §6.11's reduced rule, success leaf swaps without the
  shimmer.
- **Performance budget & mobile variant.** The lightest element on the
  leaf: no loops, no observers beyond focus. Draft storage is one
  debounced `localStorage` write. Mobile: per breakpoints.
- **Tokens.** `--ink`, `--ink-soft`, `--rubric`, `--gold`, `--parchment`,
  `--ease-lamp`, `--ease-settle`, `--ease-scrape`, `--dur-seal` (320ms).

---

## 7. Page application map

How the theme plays out across the page types of a real site. The strata
file (§1) is prepared per page; not every page ghosts equally — the map
rations the theme's effects so no two pages feel alike and no page feels
like all of them.

| Page type | Lead elements | Ghost policy | Notes |
|---|---|---|---|
| **Home** | §6.1 hero ghost-up, §6.2 lamp, §6.4 pinned passage (the page's one ceremony), §6.14 cards, §6.16 footer | Hero headline + pinned passage + one body passage ghosted; cards carry mini-ghosts | The full argument, once. The pinned passage is the institution's most famous sentence. |
| **Listing / collection** (archive, garments, books) | §6.14 plate cards, §6.18 procession, §6.8 fleck line | Card mini-ghosts only; no body-passage ghosts — a listing is a shelf, not a reading | Filters are apparatus (Fell SC labels, rubric active state); sorting is "by leaf" / "by layer recovered". |
| **Detail** (one work, garment, leaf) | §6.7 illumination (the object's plate), §6.10 linger passages, §6.5 contested word (if the object's history has one), §6.17 panel | The object's own description ghosted with its earliest catalogue entry — the richest strata file on the site | Provenance table (§11) is surface text throughout: facts are never ghosts. |
| **About / the house** | §6.4 variant (unpinned: the three versions as stacked leaves), §6.9 ornaments | The brand's own history is the content: founding text vs today's, in full | The one page where ghost density may reach one passage in two — it is a page *about* layers. |
| **Correspondence / booking** | §6.19 form, §6.16 footer | No ghosts on the form leaf itself (writing needs a clean leaf); the page's intro line may carry one | Conversion pages stay quiet; the theme persuades by tone, not by haunting the checkout. |
| **Article / journal** | §6.2 lamp, §6.6 rubric initials per section, §6.10 on pull-passages | Ghosts only where the article quotes or revises earlier published text — with dates | Long-form's home ground; the fleck line (§6.8) earns its keep here. |
| **404 — the lost leaf** | §6.12 skeleton language, one arch frame, empty | A page that was scraped too hard: "This leaf has not survived" (§12), the worm trail (§6.9) leading to the contents link | The theme's humour, used once, gently; the way back is §6.15. |
| **Search / index results** | §6.14 cards in list form, apparatus labels | No ghosts in results (speed of scanning wins); ghost counts shown as apparatus ("2 recovered layers") | Results are apparatus, and apparatus is surface. |

**Cross-page laws.** The pinned ceremony (§6.4) appears on exactly one
page of the site (usually Home; for an author site, the book's page). The
contested word (§6.5) appears on exactly one page. The transcription
control (§6.17) appears on every page that carries a ghost. The footer
(§6.16) is identical everywhere — a colophon does not vary by chapter.

---

## 8. Worked examples (v2: hero, mid-page, conversion)

### 8.1 The hero — a heritage university's home leaf, end to end

**The build.** The university ("the College") opens on its title leaf
(§4). Surface H1, IM Fell English 54px: *"Learned in the light of older
fires."* — the current motto line, adopted 2019. Beneath it, in the ghost
stratum at −1.5°, the under-text from the strata file: *"By candle and by
lamp we learn."* — the motto as drafted by the founder in 1897, recovered
from the first minute book. A provenance label in the right margin, Fell
SC: "RECOVERED LAYER · MINUTE BOOK, 1897". Below the headline, the
surface standfirst (EB Garamond 19px), then the hero's one arch
illumination (§6.7): the reading room, 1962 plate. The gold-fleck line
(§6.8) stands in the left margin, first fleck lit.

**The scroll/load timeline.** t=0 first paint: surface headline masked
behind its parchment rule, standfirst at 82% density — the leaf is
already handsome and complete. t=0–700ms: headline lines unmask upward
(§5, 90ms stagger). t=550ms: the initial "L" of "Learned" — rubricated,
as the leaf's opening letter — begins its flare (§6.6), full rubric by
t=1,000ms. t=700–1,600ms: the plate's arch opens (§6.7 timeline). t=2,000ms
idle confirmed: the ghost-up (§6.1) begins; by t=3,600ms the 1897 motto
rests at 0.38 beneath the 2019 one, and a visitor who has read both has
understood the entire institution before scrolling once. First scroll:
the raking lamp (§6.2) takes the ghost; the strata shear (§6.3) begins
its 28px disagreement; the fleck line's second fleck warms as Leaf II
approaches.

**Why it works.** Nothing in the hero is decoration: the ghost is the
motto's real ancestor, the plate is the real reading room, the fleck is
the real progress. A prospective student feels "this place is old and
knows it"; an alumnus feels recognised. Both feelings are the admissions
strategy, performed by typography.

### 8.2 Mid-page — the pinned passage on the same leaf

**The build.** Leaf III of the home page is §6.4's ceremony, given to the
College's most-quoted sentence — the founder's charge to the first
scholars. Surface (the lectern text, from the current charter): *"Go
out and be useful."* The three versions beneath, from the strata file:
Version I · 1897, the founder's notebook: *"Go out & be of use to
somebody."* Version II · 1934, the printed charter: *"Go forth and be
useful in the world."* Version III · 1988, the centenary revision: *"Go
out and be useful to others."* Labels in Fell SC at the stage's margin;
the "Read all versions" link (§6.17) under the stage.

**The scroll timeline.** The stage pins at viewport top (q=0): Version I
at 0.10, its label lit. q=0.05–0.28: the notebook draft rises to 0.55 —
handwriting-era spelling and all ("&" intact; the transcription preserves
ampersands, §12) — while the lamp parks over it. q=0.33: the counter
ticks to II; the 1934 printing rises through q=0.61, all formality.
q=0.66: III rises — 1988's small kindness, "to others", arriving last and
reading, after its ancestors, like an edit made by a century. q=0.95:
all three settle together at 0.30 under the surface line; the stage
releases; Leaf IV (the plate cards of the colleges) settles in below.
Total visitor time in the ceremony at natural scroll: ~9 seconds. It is
the page's most-remembered nine seconds, and it is made of four real
sentences.

### 8.3 Conversion — the correspondence leaf (book a reading-room visit)

**The build.** The College's archive takes visit requests through §6.19.
The leaf's head: surface H2 *"Write to the reading room"* and the terms
line in voice (§12): "Letters are answered within three working days, in
the order they were sealed." Fields: name, email, the matter (select:
"See a manuscript", "Book the reading room", "Ask about a layer",
"Other"), the letter (message), and the seal-button: "Seal & send". The
right margin is empty parchment — the archivist's space.

**The interaction timeline.** The visitor focuses *Name*: the ruled line
rubricates over 280ms. They tab through; the *Matter* select's pilcrow
marker turns rubric on selection. They submit with the email line
malformed: the seal press begins, stops at its squash midpoint (the wax
refuses — a 120ms hold the theme uses only here), and the archivist's
note writes into the email field's margin at +120ms: "The address line
wants another look — a letter needs somewhere to go." (§12's voice:
repair, not fault.) Focus moves to the email field. Corrected, the
press completes (320ms), the 300ms fade, and the success leaf: a pressed
seal, "Your letter is № 214 in the book", and beneath — the leaf's one
ghost, earned at last — the reading room's original 1911 visitor-book
heading, ghosted at rest: *"Visitors will oblige by writing plainly."*
The conversion completes inside the fiction, and the fiction was the
reason the visitor wrote at all.

---

## 9. Anti-slop — how THIS theme goes cheap, and the cure

Each failure below is specific to Palimpsest. The cure is stated as a
build rule, not a taste preference; several are enforced by the §10 gate.

1. **Lorem ghosts.** The under-text is invented filler, Latin, or the
   same sentence repeated. The theme's entire claim collapses — a
   palimpsest with fake under-text is a printed T-shirt that says
   "vintage". *Cure:* the strata file (§1) is a blocking deliverable;
   every ghost passage carries a provenance label with a date; the gate
   greps ghost content against the strata file.
2. **Ghost in a different typeface.** Under-text set in a "distressed"
   or handwriting font to signal oldness. Real under-text is the same
   hand, earlier. *Cure:* §3's law — ghosts use IM Fell English / EB
   Garamond only. A handwriting font anywhere on the leaf fails the gate.
3. **Everything ghosted.** Every paragraph has an under-text; the page
   becomes double-exposed noise and nothing reads as past because
   nothing reads as present. *Cure:* §4's density law — one ghosted
   passage per leaf, roughly one passage in three; the strata file
   marks the chosen passages, and unchosen passages are *proudly* clean.
4. **Ghosts that detach.** Shear or rotation pushes the under-text away
   from its own paragraph until it haunts the wrong text. *Cure:* §6.3's
   caps (±14px, disabled under 3 lines) and §4's registration geometry;
   a ghost must always overlap its own surface passage by ≥ 70%.
5. **Floodlighting.** Two or more ghosts at peak opacity simultaneously
   (lamp + linger + pinned version stacking). The leaf turns to soup.
   *Cure:* the systems are mutually exclusive by design — §6.2 yields to
   §6.10's linger, §6.4 allows one strong version at a time; the lamp
   loop enforces a global "one strong ghost" budget.
6. **Jelly shear.** Easing applied to scrubbed parallax, or drift beyond
   ±20px, until the leaf sloshes. *Cure:* §6.3 — scrubbed values take
   the scroll's own easing, lerp 0.1, hard caps; if a tester can *see*
   the parchment move, it is too much.
7. **Film-poster Fell.** Headlines letterspaced, uppercased, or set in
   Fell at grotesque sizes with tight leading until it reads as a movie
   title. *Cure:* §3's rules — no tracking on display, small-caps only
   in apparatus, display capped at 54px.
8. **Contested-word confetti.** Flickering words in every paragraph.
   The argument becomes a slot machine. *Cure:* one contested word per
   page (§6.5), chosen for a documented spelling change.
9. **Damage cosplay.** Coffee stains, torn edges, burn marks, heavy
   grunge textures layered on until the leaf looks distressed rather
   than old. Age in a real codex is *information* (wormholes where the
   worm went, foxing at the edges), not a filter. *Cure:* the only
   permitted damage is §6.9's worm trail and §2's baked edge gradients;
   any raster grunge texture fails the gate.
10. **The mobile pin trap.** §6.4's sticky ceremony shipped to small
    screens, trapping the scroll. *Cure:* §6.4's breakpoint demotion to
    the stacked sequence — non-negotiable, gate-checked at 360px.
11. **Lying apparatus.** Progress lines, counters, or layer counts that
    are hard-coded, decorative, or wrong ("Layer 3 of 5" on a 4-leaf
    page). Apparatus is the theme's claim to scholarship; a lying folio
    is worse than none. *Cure:* all counts derive from the DOM (§6.8,
    §6.13, §6.16); the gate changes a leaf count in test content and
    verifies the apparatus follows.
12. **Grey-box skeletons.** Loading states as generic grey rectangles.
    *Cure:* §6.12 — skeletons are scraped leaves in `--parchment-deep`,
    shaped like the incoming content.
13. **Ticker procession.** §6.18 sped up until fragments fly past like
    news. *Cure:* 90s minimum pass (110s mobile); if it can be read
    only by chasing it, it is too fast.
14. **Rubric inflation.** Red everywhere — links, buttons, headings,
    prices — until rubrication means nothing. *Cure:* §2's ration (≤5%,
    one gesture per leaf); rubric is a second hand's emphasis, and a
    hand that underlines everything underlines nothing.

---

## 10. Quality gate — minimum bar before this theme may be used in a build

All items must pass; items marked ◆ are blocking (a single failure stops
the build).

**Content & strata**
1. ◆ A strata file exists; every ghost passage on every page maps to a
   real earlier text in it, with a date or provenance note.
2. ◆ No ghost text is lorem, repeated, or invented; a random sample of
   five ghosts is verified against client-supplied sources.
3. Ghost density within §4's law (≤ 1 ghosted passage per leaf; pinned
   ceremony on exactly one page; contested word on exactly one page).

**Legibility & the standing rules**
4. ◆ With JavaScript disabled, every page is complete: surface text at
   full density, ghosts static at rest opacity, all navigation and the
   form functional.
5. ◆ No reveal can strand content: kill the lamp loop mid-page (test
   hook) and confirm every element settles via the 1.5s fallback.
6. ◆ `prefers-reduced-motion` produces the static leaf: no shear, no
   scrub, no flicker, no drift — and the linger *gesture* still raises
   ghosts instantly (§6.10's reduced rule).
7. Surface body text ≥ 7:1 contrast on its parchment at every animation
   state, including raking-light peak (§6.2's cap verified with a
   contrast probe at band centre).
8. Legal, pricing, and safety text is surface text only — a selector
   audit confirms none of it sits in a ghost layer.

**Ghost system integrity**
9. ◆ Every rendered ghost has a transcription entry in §6.17's panel,
   generated from the same strata source (build fails on a missing
   entry).
10. Ghosts use only the theme's two typefaces; ghost rotation per leaf
    is within −1°…−2° and never animated.
11. The "one strong ghost" budget holds: scripted scroll through the
    longest page never shows two ghosts above 0.5 simultaneously
    (outside §6.4's scripted overlaps).

**Motion & performance**
12. One scroll listener, one rAF loop; a frame profile of the longest
    page shows no long task > 50ms attributable to the theme (§14).
13. §6.4's pin is absent at 360px width and present at 1280px (or the
    stacked fallback engages cleanly when sticky is broken by an
    ancestor).
14. Page weight within §14's budget; LCP is the hero's surface headline
    (never a plate, never a ghost).

**Accessibility**
15. ◆ Full keyboard pass: every ghost reachable in ≤ 2 stops via focus
    raise or §6.17; focus visible on every interactive element,
    arch-shaped where the element is an arch.
16. Screen-reader pass: ghosts do not double-read (echoes are
    `aria-hidden`; §6.4's versions read once, in order, with labels).
17. Touch pass at 360px: seal targets ≥ 44px, long-press raise works,
    no hover-only meaning anywhere.

**The screenshot test**
18. A screenshot with all text removed is recognisably this theme
    (warm leaf, one red gesture, violet ghosts at an angle, gilt
    margin) — and a screenshot *with* text, shown to a first-time
    visitor for five seconds, leaves them able to say what the site is
    and what it used to say. If they can only say the first, the ghosts
    are too weak; only the second, too strong.

---

## 11. Component inventory (v2)

Every UI component a real site in this theme needs, with its themed
treatment. Components not listed here do not get invented ad hoc; if a
build needs one, it is designed from the nearest relative below and added
to this inventory. Shared tokens: `--ink`, `--ink-soft`, `--rubric`,
`--parchment`, `--parchment-deep`, `--gold`, `--ease-lamp`,
`--ease-settle`.

- **Primary button — the seal-button.** A rubric ground (`--rubric`,
  parchment text) with the wax physics of §6.11: press = 320ms squash
  `--ease-scrape`. Label in EB Garamond 17px, sentence case, a verb of
  correspondence ("Seal & send", "Request the leaf"). One per view —
  the primary action is a sealing, and a page is sealed once. Focus:
  2px parchment outline inside a 2px `--ink` outer ring. Disabled: the
  wax un-pressed — `--parchment-deep` ground, `--ink-soft` text, no
  press.
- **Secondary button — the ruled button.** Transparent ground, 1px
  `--ink` rule on all sides (a ruled box on the leaf), `--ink` text;
  hover fills `--parchment-deep` at 0.5 over 200ms. It is the pencil
  to the seal's wax: present, quieter, erasable.
- **Text link.** `--ink` with §6.13's rubric underline draw (280ms).
  Visited links deepen to a *used* ink (`--ink` at 88% + 0.02em
  letterspacing — a line that has been read sits slightly wider).
  External links carry a small gold fleck after the text — the margin
  marks what leaves the codex.
- **Input (text/email).** §6.19's ruled line: label above in Fell SC
  13px, field as a bottom rule only, text EB Garamond 19px. Focus draws
  the rubric line; error adds the margin note. No boxes, no fills —
  one writes *on* a leaf.
- **Textarea — the ruled leaf.** As input, with rules every 30px
  (the line-height) drawn as background lines that continue as the
  field grows (§6.19's edge case).
- **Select — the matter line.** A ruled line with a rubric pilcrow (¶)
  as its marker; the open list is a small leaf (`--parchment`, hairline
  vine rule at its head) whose options are 44px rows; the chosen
  option carries a gold fleck.
- **Checkbox / radio — the wax dot.** A 20px circle outline (`--ink`);
  checked = filled with `--rubric` and a 160ms press (scale 0.92→1,
  §6.11 physics at component scale). Radio groups are "hands" — only
  one wax dot pressed per group. Focus ring per seal-button.
- **Table — the folio table.** No boxes: a head row in Fell SC over a
  double hairline (the manuscript's table rule), body rows separated by
  single hairlines at `--ink-soft` 0.35, numerals tabular (§3), row
  hover = `--parchment-deep` at 0.35. Wide tables scroll horizontally
  inside a leaf with the first column held — a table too wide for its
  leaf is a fold-out, and fold-outs announce themselves with a rubric
  edge marker.
- **Badge / stamp.** Small Fell SC labels in a 1px rule: neutral
  (`--ink-soft`), notice (`--gold` fleck + ink text), withdrawn
  (`--rubric`, rotated −2° — the one component allowed the ghost's
  angle, because a stamp is struck, not set). Badges never fill with
  colour; the leaf does not wear stickers.
- **Alert — the archivist's note.** A margin-style block: hairline left
  rule in the alert's colour (rubric for error, gold for notice, ink
  for information), text in body voice (§12), a pilcrow lead. Alerts
  appear with §6.19's write-in (240ms) and are dismissible only when
  they are notices — errors persist until repaired.
- **Pagination — folio turns.** "Leaf II of V" as apparatus text with
  previous/next as ruled buttons labelled by their leaves' titles
  ("← The Versions", "The Plates →" never bare arrows — a contents
  names its destinations). Numbered pagination, where unavoidable, uses
  Roman numerals in the folio style.
- **Modal — the laid leaf.** A leaf (§6.17's panel at centre) over a
  dimmed desk (`--ink` at 0.45, no blur — blur is the ghost's property,
  not the interface's), entering with the 380ms settle + scrape edge.
  One modal at a time; its head is a running title; its close is a
  rubricated "Finis" or a plain × in apparatus — choose per build,
  never both.
- **Toast — the vellum slip.** A small slip (max 340px) that settles
  at the foot's margin for 5s: one line of voice (§12) + an optional
  action link. Slips do not stack beyond two; a third waits — the desk
  is not a noticeboard.
- **Tabs — codex parts.** A contents line (§6.13's pattern): part
  titles in Fell SC, the active part rubricated with its pilcrow, a
  vine rule beneath the row that redraws (§6.9, 500ms) under the newly
  active part. Panels swap with the 200ms parchment fade.
- **Accordion — folded leaves.** Each item a leaf-fold: head row with
  folio numeral + title; opening unfolds — max-height + the fold's
  shadow line deepening — over 350ms `--ease-settle`; the open item's
  numeral rubricates. Only one fold open per group (a codex opens at
  one place).
- **Breadcrumb — the running path.** Apparatus text: "Codex › The
  Versions › Version II" in `--ink-soft`, separators as middle dots,
  current leaf in `--ink`. It sits inside the leaf head, never in the
  header.
- **Search — the index lookup.** An input (ruled line) labelled
  "Search the index"; results are §6.14 cards in list form (§7);
  the empty result is §12's empty voice with the index's own
  suggestion ("Nothing under that word — the index also keeps…").
  Search never ghosts: finding is apparatus work.
- **Tooltip — the gloss.** Medieval manuscripts gloss hard words in the
  margin; tooltips here are glosses: a small parchment slip above the
  term, apparatus type, appearing on hover (600ms dwell — glosses are
  for the lingering, §6.10's philosophy) and on focus immediately.
  Max 24 words; a longer explanation is a footnote, not a gloss.
- **Avatar / person image.** Set in a shallow arch (§6.14's frame) at
  parchment grade — people in this theme are plates, with a caption
  naming them and their years ("The founder, 1962") where known.
- **Divider — the vine rule.** §6.9's drawn vine (or its static form)
  is the only divider. A plain `<hr>` renders as the double hairline;
  no other divider exists.
- **Empty state.** A scraped-clean leaf: the arch outline empty, one
  line of §12's voice, one ruled button for the way onward. Emptiness
  in this theme is a *prepared* surface — the next text has somewhere
  to be written.
- **Success state.** The pressed seal + the reference (§6.19): success
  is always *recorded*, never merely celebrated — no confetti exists
  in a codex.
- **Error state (page-level).** §7's lost-leaf pattern: the archivist
  apologises, names what is known, and points to the contents.

---

## 12. Content & copywriting voice (v2)

**The voice.** The house speaks as its own archivist: unhurried, exact,
dryly fond of its past. Sentences are complete; fragments are for
apparatus labels only. The present tense is the surface voice; the past
is quoted, never impersonated. Numbers in prose are words; dates are
given in full ("Autumn 1998", never "the nineties"). Nothing is "seamless",
"cutting-edge", or "revolutionary" — a house with a palimpsest has
outlived several revolutions and says so by not mentioning them.

**Headline style.** Surface headlines are statements in the present
voice, Fell, sentence case, ≤ 9 words: *"Learned in the light of older
fires."* / *"The coat, as it was described in 1974."* Ghost headlines
(the under-texts) are the *actual earlier lines*, unedited — including
their ampersands, their dated spellings, their slightly embarrassing
confidence. Editing a ghost to make the past look better is §9.1 fraud
with a thesaurus.

**Label style.** Apparatus labels are Fell SC, terse, factual, dated:
"RECOVERED LAYER · AUTUMN 1998" / "LEAF III OF V" / "FIRST DESCRIBED
HERE". Labels never editorialize ("amazing vintage find!") — the
archive does not exclaim. Exclamation marks are banned from the theme
entirely; the loudest mark permitted is the pilcrow.

**Error-message voice.** The archivist apologises, names the repair,
never blames the writer: "The address line wants another look — a
letter needs somewhere to go." / "That date has not survived checking;
the book keeps it as written, but the visit cannot." Errors are
*marginalia*: specific, beside the line, in rubric, kind.

**Empty-state voice.** Absence is described as a state of the material,
with the way onward: "This shelf of the archive is scraped clean.
Nothing has been written here yet — begin with the contents." / (No
seals yet:) "No passage has your seal. When one earns it, press the
wax beside it, and it will be kept here."

**Success voice.** Recorded, numbered, quiet: "Your letter is № 214 in
the book. Expect an answer within three working days." Success always
cites the record; a success without a reference number is a rumour.

**CTA voice.** Verbs of reading and correspondence, never of marketing:
"Read what came before" / "See the versions" / "Write to the reading
room" / "Seal & send". Banned: "Get started", "Learn more" (say what
will be learned), "Submit" (letters are sealed, not submitted),
"Unlock" (nothing here is locked; some things are merely earlier).

**Provenance writing.** Every ghost's label follows the pattern
*[source], [date]*: "Minute book, 1897" / "Catalogue copy, Autumn
1974" / "First draft, March 2019". Where the source is uncertain, the
label says so — "Attributed to the founder's hand, undated" — because
an archive that guesses at provenance will guess at anything.

---

## 13. Full-page scroll choreography map (v2)

The home leaf (§7's fullest page), beat by beat, top to footer. "Feel"
is specified because choreography that cannot be felt in order is a pile
of effects.

| Beat | Scroll position | What happens | What the visitor feels |
|---|---|---|---|
| 1 | Load, 0% | Title leaf paints complete; headline unmasks (§8.1, 700ms); initial flares by 1,000ms | A page that was always here, being opened |
| 2 | Idle, 0% | t=2,000ms: the 1897 motto ghosts up beneath the current one (§6.1) | The past arriving uninvited, politely |
| 3 | 0–12% | Raking lamp takes the hero ghost; strata begin their shear (§6.2/§6.3); fleck II warms (§6.8) | The leaf responding to being read |
| 4 | 12–30% | Leaf II settles; its rubric initial flares at entry (§6.6); the vine rule draws at the boundary (§6.9) | The codex's punctuation, drawn live |
| 5 | 30–38% | The hero plate's arch is long settled; Leaf II's passage offers the first linger — visitors who dwell see its ghost sharpen (§6.10) | A reward for slowness, discovered, not announced |
| 6 | 38–62% | **The pinned ceremony** (§6.4/§8.2): three versions rise and sink in turn under the held sentence; counter ticks I → II → III | Nine seconds of held breath; the page's centre of gravity |
| 7 | 62–64% | The pin releases; all three versions rest together at 0.30 for one viewport — the whole history visible at once | Exhale; the argument complete |
| 8 | 64–82% | Plate cards settle in staggered rows (§6.14); mini-ghosts ride at 0.30; the procession (§6.18) drifts at the band's edge if this leaf carries one | The shelf; browsing pace returns |
| 9 | 82–92% | The correspondence invitation leaf: intro line, then the form's ruled lines at rest (§6.19) — deliberately the quietest beat on the page | An invitation, not a funnel |
| 10 | 92–100% | The colophon (§6.16): final fleck shimmers, earlier imprints rest beneath the current one | The book signing itself; the last word belongs to the past |
| — | Any | The transcription control (§6.17) is present from beat 1; the lamp never lights two ghosts strongly at once (§9.5) | Throughout: one lamp, one reader, one leaf |

**Choreography laws.** Beats never overlap their *peaks* (a flare may
begin while a settle ends, but two climaxes never share a viewport).
Ceremony (beat 6) is surrounded by quiet on both sides — contrast is
what makes it ceremony. If a page type omits the pin (§7), beats 6–7
collapse into a single stacked-versions leaf and the map shortens;
nothing else is promoted to fill the gap.

---

## 14. Whole-page performance budget (v2)

The theme's effects are deliberately cheap (opacity, colour, transforms
on few layers); the budget exists so they stay that way under real
content.

| Budget line | Limit | Enforcement |
|---|---|---|
| Total page weight (home, first load) | ≤ 900KB, of which images ≤ 550KB | Plates are the only heavy asset; derivatives: plate 1200w (≤ 220KB), card 800w (≤ 120KB), fragment 400w (≤ 30KB), WebP/AVIF with parchment-grade applied at build, not by CSS filter on the fly where avoidable |
| Fonts | ≤ 120KB woff2 total (4 files, subset) | §3's loading spec; `size-adjust` fallbacks prevent strata reflow |
| CSS + JS for the theme layer | ≤ 60KB gzipped combined | One lamp loop, no animation library — GSAP-class tooling is unnecessary weight for scrubbed values and is not used |
| Animation frame budget | ≤ 8 style writes per frame across all systems; transform/opacity/colour only; no layout reads inside the loop (measurements cached, refreshed on resize/font-load) | §6 budgets per element sum under this cap by construction (lamp 6 + shear 2 worst case, never simultaneous on > 3 strata) |
| Long tasks | None > 50ms attributable to theme JS; the loop's per-frame work ≤ 2ms on a mid-tier phone | Profiled in the §10 gate (item 12) |
| INP / interaction latency | Seal press and linger responses begin within 100ms of the gesture | Dwell timers and press handlers are on the main thread but trivially small |
| LCP | The hero surface headline (text) — never a plate or ghost | Fonts + headline prioritised; plates lazy below the fold except the hero plate, which is `fetchpriority="high"` but still loses to the headline by design of the paint order |

**Cut order when the budget is exceeded** (cut in this order, never
randomly): 1) fleck twinkle (§6.8 ambient) → 2) parchment shear layer
(§6.3 keeps ghost shear) → 3) procession drift becomes the static shelf
(§6.18) → 4) arch clip animation becomes a fade (plates stay) → 5) lamp
scrub becomes entry-triggered static light positions. **Never cut:**
the transcription panel (§6.17), the fallbacks (§5's law), the
reduced-motion variants, or surface legibility. A budget crisis costs
ornament, never meaning.

**Low-power / save-data.** `Save-Data` header or `navigator.connection`
slow-2g: plates serve the card derivative at all sizes, the procession
is the static shelf, shear is off. Battery-saver heuristics (reduced
motion at OS level) arrive via `prefers-reduced-motion` and are honoured
wholesale.

---

## 15. Build-order checklist (v2)

The sequence in which this theme is implemented. Later steps assume
earlier ones; the order is chosen so the page is *complete and honest at
every stage* — if the build stopped after any step, what exists would
not lie.

1. **Strata file first.** Collect and verify the client's real earlier
   texts with provenance (§1). No strata file, no build — this step is
   content work, not design work, and it gates everything.
2. **Tokens.** Implement §2's palette (incl. the candlelit remap) and
   §5's easing/duration tokens as CSS custom properties.
3. **Typography.** Load §3's faces subsetted; set the scale, the ghost
   type rules, and the `size-adjust` fallbacks; verify no reflow tear
   on font swap.
4. **The static leaf.** Build all pages with surface content only, plus
   ghosts as *static* layers at rest opacity, plus the no-JS
   transcription blocks (§6.17 fallback). This is the shippable floor:
   complete, readable, honest. (If the project died here, the site
   would still be a good site.)
5. **Apparatus.** Running head (§6.13), fleck line with DOM-derived
   counts (§6.8), contents leaf (§6.15), colophon (§6.16) — the
   furniture that must never lie.
6. **Entry systems.** Surface settles, rubric flares (§6.6), arch
   reveals (§6.7), vine/worm draws (§6.9) — with the 1.5s fallback
   timers wired from the start, not retrofitted.
7. **The lamp.** Raking light (§6.2) + shear (§6.3) in the single lamp
   loop; enforce the one-strong-ghost budget (§9.5).
8. **The gestures.** Linger (§6.10), seal (§6.11) + storage, contested
   word (§6.5), transcription panel (§6.17) from the same strata source.
9. **The ceremony.** Pinned passage (§6.4) with its sticky-failure
   detection and mobile demotion.
10. **Transitions & skeletons.** Scrape (§6.12), procession (§6.18),
    card systems (§6.14), the correspondence leaf (§6.19) with its
    margin-note errors.
11. **Reduced-motion & dark passes.** Verify every element's static
    variant and the candlelit remap as *designed states*, not
    afterthoughts.
12. **The gate.** Run §10 in full — including the JS-disabled pass, the
    killed-loop pass, the 360px pass, and the five-second screenshot
    test — before the theme is signed off for the build.

---
