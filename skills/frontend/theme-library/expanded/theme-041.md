# 41. Kintsugi — Expanded (v1 + v2)

> Expansion of theme #41 from `themes-026-050.md`, written directly to
> the full standard: the v1 10-part structure plus the v2 deepening
> layers (per-element choreography timelines, state matrices, breakpoint
> behaviour, edge cases, accessibility specs and token lists; per-theme
> component inventory, copywriting voice, three worked examples, scroll
> choreography map, performance budget, build-order checklist).
> Identity preserved exactly: the same concept, the same five palette
> anchors, the same typefaces, the same twelve signature elements —
> deepened, never redesigned — plus six page-family elements. One
> arithmetic correction is made and recorded: the original entry says
> "13 tiny fissures" but lists 7 + 2+2+1 + 2 + 1, which is fifteen; the
> list is the identity, so this expansion specifies **fifteen** fissures
> and the quality gate audits that count.

## 1. Concept & world

A kintsugi page is a vessel that has been dropped. It does not open
whole and it does not pretend to be new: it opens **broken** — a
shattered composition of offset fragments, sections sitting a few
pixels and a few degrees out of register, cracks open and dark — and
it **repairs itself with gold as you scroll**, until the final section
stands whole but proudly seamed. The gold is never decoration applied
to an intact surface. Every gold line on the page is the scar of a
specific break the visitor watched happen or watched heal, and the
scars persist: they become the section's permanent ornament, its
dividers, its progress record. The page's argument and the page's
layout are the same act — *broken things mend, and the mend is the
most valuable part* — performed on the content itself, not illustrated
beside it.

**The theme's one law: gold only where something broke, and every
break keeps its name.** Three consequences, all auditable. (1) No gold
element may exist on the page that does not trace a break in a real
content object — no gold rules, gold bullets, gold headings or gold
"accents" anywhere; if a builder wants a gold line, something must
break first. (2) Every seam carries a mend note in the markup
(`data-mend="dropped, March 2023 — studio shelf"`) naming what broke;
the footer (§6.17) prints the mend record from those notes, so a seam
without a note is a gate failure. (3) Gold once laid is never taken
back: within a session, mending is one-way. Scrolling up never
re-breaks a healed vessel, never un-draws a seam, never un-counts the
ledger. The visitor's journey down the page is the repair; there is
no undo in a kiln.

**The world.** A working repair atelier: lacquer (urushi) that cures
slowly and is poisonous until it does, gold powder dusted onto wet
seams, vessels resting in a humidity cabinet (muro) between stages,
shards wrapped in rice paper and labelled by hand. The page borrows
the atelier's time signature — nothing in kintsugi is instant, so
nothing on this page snaps; things settle, cure, and hold. It also
borrows the atelier's honesty: a mend is dated, signed, and priced by
the number of pieces, and a vessel too far gone is refused, kindly,
in writing.

**Best-fit sites and audiences.** Repair and restoration studios
(the literal case); ceramics, glass and furniture workshops; jewellery
and watch repair; conservation and archive services; counselling,
physiotherapy and rehabilitation practices whose honest pitch is
*not new — mended, and stronger at the seam*; publishers of memoir and
recovery writing; any brand whose founding story includes a failure
it survived and can name. The audience is a visitor who distrusts
polish: the theme converts sceptics precisely because it shows the
crack before the gold.

**When NOT to use it.** Never for a brand that must read as flawless
and unbroken — luxury launches, precision instruments, sterile medical
or aviation safety surfaces — because the theme's first screen is
deliberately damaged goods. Never where gold-as-scar would trivialise
the content: bereavement services, trauma support, and memorial pages
must not turn a visitor's grief into a page effect (the testimonial
crack, §6.11, is opt-in play on a *story*, never on a person's pain).
Never for dense data products: the fracture choreography needs
breathing room, and a 400-row table cannot heal centre-screen. Never
when the client will not supply real breakage to name — a studio with
no mend notes to write cannot pass law (2), and the theme collapses
into exactly the gold-foil slop it exists to refuse.

## 2. Palette

Five anchors, inherited exactly. Two grounds (charcoal ceramic, rice
paper), one breakage colour (shard grey-blue), one mend colour (gold),
one action colour (lacquer red, rationed to CTAs and the visitor's own
crack). The page lives mostly on charcoal — the kiln-dark workshop —
with rice-paper sections where the atelier writes things down (forms,
the ledger, the mend record).

| Token | Hex | Role | Usage ratio | Pairing & contrast (measured) |
|---|---|---|---|---|
| `--charcoal` | `#20222B` | Primary ground: hero, vessel sections, footer | ~55% | Rice on charcoal **13.10:1** (body text). Gold on charcoal **7.54:1** — gold may carry apparatus text on charcoal only, never body copy |
| `--shard` | `#3A3F4A` | Shard faces, unhealed fragments, skeleton fills, card grounds | ~15% | Rice on shard **8.72:1** (text safe). Shard on charcoal is **1.50:1** — a shard edge on charcoal is therefore always defined by its `--paper` bevel (§6.1), never by the shard colour alone |
| `--gold` | `#D4AF37` | Seams, the margin vein, mend ornament — mend material only, per the law | ~4% | On rice paper gold is **1.74:1** — never text, never a lone line: on light grounds every seam sits on a 1px charcoal hairline underlay (§4) so the crack reads before the gold does |
| `--paper` | `#EFE9DC` | Light ground: form, ledger, mend record; bevel light on shard edges | ~24% | Charcoal on paper **13.10:1** (body text). Lacquer on paper **8.50:1** |
| `--lacquer` | `#7A1F1F` | CTAs only; the visitor's crack (§6.11); error rules in the form (§6.14) | ~2% | Lacquer on charcoal is **1.54:1** — a lacquer button never sits directly on charcoal; it carries a 1px rice keyline, or sits on paper/shard. Rice text on lacquer **8.50:1** |

**Derived tokens (closed list — no others may be introduced):**
`--gold-bright #E9CE7A` (seam glow and runner light; on charcoal
**10.24:1**, still never text), `--gold-deep #8A6D1F` (the only gold
that may touch text on paper — **4.05:1**, apparatus and large labels
≥18px only, never body), `--paper-dim #B9B2A2` (secondary text on
charcoal, **7.51:1**), `--shard-light #6E7686` (hairlines and disabled
apparatus on charcoal, **3.47:1**, graphical only), `--crack #101116`
(the open, unhealed crack — darker than the ground so a break reads as
a void, not a shadow), `--lacquer-bright #9A2A24` (CTA hover on paper).

**Dark-mode behaviour.** There is no inverted scheme: charcoal *is*
the dark scheme, and paper sections are the atelier's lit desk, not a
"light mode". Under `prefers-color-scheme: dark`, paper sections move
to `--shard` grounds with rice text (8.72:1) and gold-deep apparatus is
replaced by `--gold` (7.54:1 on charcoal; on shard, gold measures
5.02:1 — apparatus only). The form keeps a paper ground in both
schemes: forms are paperwork, and paperwork is filled in under the
lamp. Seams, dust and runners are identical in both schemes — gold
does not change with the hour.

**Gold rationing.** Gold is measured like the material: a page may
carry at most the seams of its real breaks plus the margin vein.
The §10 gate weighs it: gold pixels at rest (excluding the vein)
must stay under 1.5% of the viewport at any scroll position. A design
that needs more gold needs more breakage, honestly introduced — or a
different theme.

## 3. Typography

Two voices, inherited: **Zen Old Mincho** for display — a Mincho's
calm, slightly archaic authority, the voice of the vessel and the
atelier's name — and **Noto Sans JP / Inter** for body and apparatus
(Noto Sans JP first in the stack: the theme's labels borrow the
atelier's Japanese terms, and they must set in a face that has them).

| Role | Face | Size / line-height | Tracking | Rules |
|---|---|---|---|---|
| Display (hero title, vessel names) | Zen Old Mincho 600 | 56px / 1.15 desktop, 38px mobile | −0.01em | Never uppercase. Headline letters begin offset along the crack (§5) and click into alignment as the seam fills |
| Heading | Zen Old Mincho 600 | 32px / 1.25 | 0 | One heading per vessel section; the heading sits on the section's main seam line, not above it |
| Sub-heading / service name | Inter 600 (Noto Sans JP for terms) | 19px / 1.4 | 0.01em | Sentence case |
| Body | Inter 400 (Noto Sans JP fallback) | 17px / 1.65 | 0 | Measure 58–66ch on paper, 52–60ch on charcoal (the dark reads narrower) |
| Apparatus (labels, seam notes, counts) | Inter 600 | 11.5px / 1.5 | 0.14em, uppercase | The atelier's handwriting-on-the-label voice: `MEND Nº 214 · 4 PIECES · GOLD` |
| Data (ledger figures) | Inter 500, tabular numerals | 34px / 1.1 | 0 | Figures count (§6.10); the unit is apparatus, set after, never before |
| Caption / mend note | Inter 400 italic | 14px / 1.55 | 0 | Every caption attached to a vessel is its mend note: what broke, when, in how many pieces |

**Type laws.** (1) **No word is ever set in gold below 18px**, and no
body text is gold at any size — gold is a material, not an ink; the
single exception is apparatus on charcoal (§2). (2) **Italics are
mend notes only** — the theme has no other italics, so an italic line
anywhere on the page is read as provenance. (3) **The crack runs
through type, never around it**: the hero headline's letters offset
along the crack path (§5), and the testimonial's seam interrupts its
text (§6.11) — type that politely avoids the breakage is off-theme.
(4) Numerals in the ledger are always tabular and always DOM-derived
(§6.10); a typed-in round number is a gate failure. (5) Japanese
terms (金継ぎ, 漆, 室) appear at most once per section, always with
their reading given in apparatus on first use — the theme respects
the craft's language; it does not wear it as costume.

## 4. Layout language

**Sections are vessels.** The page is a shelf of vessels in a column:
each section is one vessel — a bounded object with a rim (its heading
on the seam line), a belly (its content), and a foot (its mend note
and the seam that divides it from the next vessel). Sections never
bleed into each other; between vessels sits a shelf gap of 96px
charcoal (64px mobile) in which nothing lives but the margin vein's
branch (§6.13). Within a vessel, content is arranged as the vessel's
own geometry: centred, symmetric around the vessel's vertical axis,
maximum width 1080px — a bowl does not have a sidebar.

**The fracture geometry.** Each vessel enters fractured into 3–4
clip-pieces (§6.8). The fracture plan is authored per vessel, not
generated: the master crack runs through the vessel's most important
content boundary (between the testimonial's two halves, across the
hero bowl's belly), and secondary cracks branch at 30–60°. Pieces
offset by 6–22px and rotate 0.4–1.6° at rest-broken; offsets are
transforms of the complete section — the DOM is whole, only the
paint is displaced. Crack paths are drawn once as SVG in the vessel's
own coordinate box and reused by the seam (§6.2), the fissures (§6.3),
the glow mask (§6.7) and the runner (§6.6), so every system agrees
about where the break is.

**The margin vein.** A gold vein runs down the left margin (x = 28px
at ≥1200px, inside the gutter at smaller sizes, §6.13), extending as
vessels mend and branching into each healed section like a root or a
river system. The vein is the page's spine and its progress record;
it is the only gold allowed outside a vessel.

**Seams as dividers.** There are no horizontal rules in this theme.
Where another theme would rule a line, this theme draws the vessel's
foot seam — the crack the vessel arrived with, now gold. On paper
grounds, every seam is drawn as a 1px `--crack` hairline with the gold
centred on it (§2's contrast law), so the divider reads as a mended
break, not a gold stripe.

**Density.** One vessel per viewport, always: a section's min-height
is 100vh at ≥1200px (the pin, §5, needs the room), 92svh on mobile.
Whites of the page — the shelf gaps — are kiln-dark and empty on
purpose; the eye rests between vessels the way a hand rests between
pieces. Density inside a vessel is low: one idea, one object, one
mend. A vessel that needs two columns of text is two vessels.

**Grid.** A quiet 12-column grid lives inside each vessel for placing
the shards' contents, but nothing on the finished page aligns to a
visible grid — a mended bowl shows seams, not scaffolding. Spacing
rhythm is 8px, with vessel-internal padding 64px desktop / 28px
mobile, and the mend note always 24px below the foot seam.

## 5. Full motion system

Every motion term, in this theme's language. Five named easings, used
nowhere else and for nothing else:

- `--ease-lock: cubic-bezier(.2,1.3,.3,1)` — the shard lock: a piece
  travels home and *clicks* past its seat by 1.5% before settling.
  The overshoot is ceramic, not elastic: one overshoot, no bounce.
- `--ease-settle: cubic-bezier(.3,.7,.3,1)` — the soundless settle:
  vessels, cards and the whole bowl dipping 1.6px as lacquer takes
  the weight.
- `--ease-draw: cubic-bezier(.45,.05,.35,1)` — the base curve under
  the seam's stepped bursts (§6.2) and the vein's growth.
- `--ease-glow: cubic-bezier(.2,.6,.3,1)` — light arriving and leaving
  gold: runners, pointer glow, sheen fades.
- `--ease-cure: cubic-bezier(.55,.06,.35,1)` — the slowest curve, for
  things that harden: lacquer sheen, the footer vessel's rest state.

Durations are tokens: `--dur-lock` 640ms, `--dur-settle` 550ms,
`--dur-glow` 900ms, `--dur-sheen` 1400ms, `--dur-runner` measured per
path (§6.6). One shared `requestAnimationFrame` loop with lerp 0.12
drives every scrubbed value on the page — fracture convergence, vein
extension, shard parallax drift, card tilt — and nothing else may
read scroll position.

**Scroll-triggered reveals** are fracture→heal (§6.8): sections enter
broken and mend as they centre. **Scroll-driven scrub** is the same
gesture: pin + scrub, the vessel held centre-screen while its pieces
converge and its seams draw with stepped bursts (§6.2). **Parallax**
is shard drift: a broken vessel's layers sit at slightly different
offsets (factors 0.94 / 1.0 / 1.06) and drift *into register* as the
scrub proceeds — parallax here is not depth decoration, it is the
misalignment itself resolving. **Pinned scenes**: each vessel pins
for 130vh of scroll (100vh stage + 30vh of mend travel) at ≥1200px;
the pin is the workbench — the vessel stays in the hand while it is
repaired.

**Masked line reveals** belong to the headline: letters start offset
along the crack vector, masked by the crack's own clip, and click
into alignment letter by letter as the seam fill passes them
(§6.1's choreography covers the hero; §6.8 applies the same to
section headings at 40ms per letter, capped at 24 letters).
**Blur-to-sharp is refused**: a blurred shard reads as a photograph
out of focus, and this theme's damage is geometric, never optical —
the refusal is recorded here so no builder reintroduces it.
**Counters** are the mending ledger (§6.10), counting *up* only,
because mending is one-way. **Progress** is the margin vein (§6.13):
a growing, branching gold root — there is no progress bar, and
percentages are banned from the theme's progress language (§12).
**Marquees are refused**: nothing in an atelier scrolls sideways
forever; the only loops are the seam runners (§6.6) and the footer
vessel (§6.12), both of which are cycles of the craft, not tickers.
**Ambient loops**: the runner light travelling finished seams, gold
dust settling (§6.4), the footer vessel's break–mend cycle.
**Micro-interactions**: seam glow under the pointer (§6.7), the
sheen's return sweep (§6.5), card tilt (§6.9), the click that lays a
crack (§6.11). **Hover physics**: pieces settle together under the
hand with `--ease-lock`; nothing springs, nothing bounces twice —
ceramic is heavy and the hand is careful. **Page transitions** are
the shard pass (§6.15): the leaving page cracks along its master
vein and the arriving page enters already mending. **Image
treatments**: every vessel image is presented as a vessel — clipped
to its fracture plan while broken, whole with seams when healed; no
image on the page is ever a rectangle with a filter.

**Safety timings (theme-wide, from the original entry, binding):**
the hero mend is forced complete by 1200ms and final by 4000ms;
fracture→heal sections are force-healed by 6000–7000ms after first
entry; every element below carries its own watchdog, and the page
ships in the healed state — broken states are JS-armed only.

## 6. Signature elements

### 6.1 Hero bowl mend

- **What & why.** The hero is a single great bowl — the atelier's
  showcase piece — arriving in 4 shards and mending itself on load.
  It is the theme's whole argument in one object, performed before a
  word is read: the brand's craft, done to the brand's own vessel.
  The bowl carries the hero: the headline sets across its belly, the
  standfirst beneath its foot, the CTA at its rim.
- **Structure.** An inline SVG bowl (viewBox 0 0 640 480) clipped
  into 4 shard groups by the authored fracture plan (§4). Each shard
  is filled with its own angled linear gradient — light falls
  differently per fragment, so the breakage reads in the shading
  before it reads in the gaps — and stroked with a faint paper-coloured
  bevel edge (1.5px `--paper` at 55%) on its broken sides only: the
  bevel is the unglazed ceramic core showing where the piece snapped.
  The 3 main seam paths live in a separate `<g class="seams">` above
  the shards; the crack state is the same paths stroked `--crack` at
  3px. Headline letters are individual spans positioned over the
  bowl's belly band. All shards are transforms of the whole bowl —
  with JS off, the bowl stands mended and gold.
- **Motion spec.** Trigger: load, gated on `document.fonts.ready`
  raced against a 500ms timer. Shards slide in from mismatched
  positions (offsets 18–42px, rotations 1.2–2.4°, largest shard
  first), each locking with `--ease-lock` over `--dur-lock` 640ms,
  staggered 140ms. As each shard locks, the seam segment adjoining it
  begins its stepped draw (§6.2). On the final lock, the whole bowl
  performs one soundless settle dip: translateY +1.6px and back over
  `--dur-settle` 550ms `--ease-settle`, the lacquer-red CTA fading in
  at the dip's bottom. Forced complete by 1200ms (any shard not home
  snaps to register); final state guaranteed by 4000ms.
- **States.** Broken (JS-armed, ≤1200ms) → mending → mended (rest) →
  lit (pointer over the bowl: §6.5 sheen + §6.7 glow armed).
  Scrolled-past: mended, still, runners running (§6.6).
- **Content merge.** The bowl is not an illustration beside the hero
  copy — the headline is set *on* it, the offer is its mend note
  ("Dropped from the studio shelf, March 2023. Four pieces. Gold."),
  and the primary CTA is the commission action (§6.14). Remove the
  bowl and the hero has no content left; that is the test it passes.
- **Failure fallback.** No JS: whole bowl, gold seams, headline
  aligned, CTA present. Watchdogs: shards forced home at 1200ms;
  a 4000ms final watchdog sets the mended state regardless of loop
  health; if SVG fails to parse, an authored `<img>` of the mended
  bowl (same viewBox, seams gold) replaces it — the hero never
  depends on script or vector support.
- **Reduced-motion variant.** The bowl arrives mended. No slide, no
  dip; the sheen (§6.5) is a static gradient already laid on the
  glaze. The mend note still tells the story the motion would have.
- **Performance budget & mobile variant.** 4 transformed SVG groups +
  3 seam paths; zero raster images; ≤9KB inline. Mobile (<768px):
  the bowl scales to 92vw, shard offsets halve (9–21px), stagger
  tightens to 100ms, and the settle dip is cut — small screens get
  the mend without the ceremony's weight.
- **Choreography timeline (v2).** t=0 fonts ready (or 500ms race
  lost) → t=0–640 shard 1 (largest, the base) locks → t=140 pieces
  2 locks at t=780 → t=280 piece 3 locks at t=920 → t=420 piece 4
  locks at t=1060, its seam burst-run begins → t=1060–1610 settle
  dip, CTA fades at t≈1330 → t=1610 bowl mended; §6.2 finishes the
  last seam by ≈1900 → t=1900 sheen sweep (§6.5) → runners arm
  (§6.6). Hard ceiling: everything forced by t=4000.
- **State matrix (v2).** *Rest:* mended bowl, seams gold, runners
  lit. *Hover:* sheen re-sweeps (§6.5); seams glow near the pointer
  (§6.7). *Focus:* the bowl itself is not focusable; the CTA inside
  the hero takes the §11 focus ring, and focus triggers the same
  sheen as hover (keyboard visitors get the finished-surface proof
  too). *Active:* CTA press — the bowl dips 1.6px (`--ease-settle`,
  180ms) as if set down firmly. *Scrolled-past:* mended; runners
  continue; never re-breaks (the law). *Disabled:* n/a to the bowl;
  a disabled CTA greys to `--shard-light` and the bowl does not dip.
  *Touch:* no hover — the sheen plays once automatically 600ms after
  the mend completes, so touch visitors see the lacquer proof.
- **Breakpoints (v2).** ≥1200px: bowl 640px wide in a 100vh hero,
  headline 56px across the belly. 768–1199px: bowl 520px, headline
  44px, shard offsets ×0.75. <768px: bowl 92vw, headline 38px set
  below the bowl instead of across it (letters on a 340px belly
  would crowd), offsets ×0.5, dip cut.
- **Edge cases & failure modes (v2).** *Headline longer than the
  belly:* the headline band wraps to two lines and the crack vector
  (§5) is re-derived from the wrapped line box — letters offset
  along the actual break, never a stored path. *Visitor scrolls
  during the mend:* the mend is time-based, not scroll-based; it
  completes off-screen and the bowl is simply whole when met again.
  *Slow device:* if the shared loop's frame time exceeds 24ms
  twice, shard stagger collapses to 0 and locks become 300ms fades —
  the mend still reads, the choreography thins. *Return visit:*
  `sessionStorage` marks the hero mended; the bowl arrives whole
  (the law — gold is not taken back, even between pages).
- **Accessibility spec (v2).** The SVG is `role="img"` with
  `aria-label` carrying the mend note verbatim. The headline is a
  real `<h1>` in DOM order — letter spans are `aria-hidden` except
  one visually-hidden full-text copy, so the heading reads once,
  correctly. Shard motion is decorative: nothing about the offer
  exists only in the animation. Contrast: headline rice on charcoal
  13.10:1; the CTA is rice on lacquer 8.50:1 with the §2 keyline.
- **Tokens consumed (v2).** `--charcoal`, `--shard`, `--gold`,
  `--gold-bright`, `--paper`, `--crack`, `--lacquer`, `--ease-lock`,
  `--ease-settle`, `--dur-lock` (640ms), `--dur-settle` (550ms),
  `--stagger-shard` (140ms), `--mend-hero-force` (1200ms).

### 6.2 Stepped crack propagation (`growCrack`)

- **What & why.** Gold seams in this theme do **not** draw smoothly.
  Each seam advances the way a real fracture runs and the way gold
  is actually laid into a moving crack: in randomised bursts of
  5–13% of its length, a held breath of 50–180ms, then another burst.
  The irregular rhythm is the single most important detail in the
  theme — a smooth dash-draw reads as a loading bar; the burst-and-
  breathe reads as a physical event happening to a real object.
- **Structure.** Each seam is an SVG path whose true length is
  measured at build-in (`getTotalLength()`), never estimated. The
  seam is drawn as two stacked strokes: the `--crack` underlay (3px
  on charcoal, 1px + gold centre on paper per §4) and the gold fill
  (2.5px `--gold`), its `stroke-dasharray` set to the measured
  length and its offset driven by the burst engine. The engine is a
  per-seam state machine inside the shared loop: {position, phase:
  burst | breath, nextAt}. Burst sizes and breath lengths are drawn
  from a seeded RNG (seed = seam index × 7919) so every visitor gets
  the same "random" fracture the designer approved — unseeded
  randomness cannot be quality-gated.
- **Motion spec.** Trigger: a vessel's heal (load for the hero,
  scroll-scrub for sections, §6.8). During a burst, the front
  advances its 5–13% over 90–160ms on `--ease-draw`; during a
  breath, it holds dead still — the stillness is the spec, not a
  stall. Average front speed is tuned so a hero seam (~380px)
  completes in ≈1400ms and a section seam (~240px) in ≈900ms.
  Scrubbed seams (§6.8) map scroll progress to a *target* position;
  the burst engine chases the target, so scrubbing fast makes the
  bursts longer, never smoother.
- **States.** Open crack (gold 0%) → running (burst/breath) → wet
  (complete, §6.4 dust active, seam at `--gold`) → cured (after
  2400ms, seam settles to its rest gold and §6.6 runners may use
  it). Scrolled-past: cured. A seam never returns to an earlier
  state (the law).
- **Content merge.** The seam *is* the vessel's scar forming, drawn
  on the content object itself along its authored fracture plan
  (§4). It decorates nothing; it repairs something specific, and its
  mend note (§1 law 2) names the break it is closing.
- **Failure fallback.** No JS: seams render fully drawn (dashoffset
  0 is the DOM default; the engine only ever *withholds* gold via
  JS-armed pre-states). Watchdog: any seam whose engine has not
  completed 5000ms after its trigger is set complete in one frame —
  a stuck burst must never leave a vessel half-mended. If
  `getTotalLength` throws (exotic SVG), the seam falls back to a
  plain 800ms opacity fade of the pre-drawn gold path.
- **Reduced-motion variant.** Seams are drawn, full stop. The
  fracture story is told by the mend note and the still-open crack
  is never shown: reduced-motion visitors meet vessels already
  mended, per the theme's standing rule.
- **Performance budget & mobile variant.** One dashoffset write per
  active seam per frame; at most 3 seams run concurrently (the
  scheduler queues the rest — a page never bursts everywhere at
  once). Mobile: burst range widens to 8–16% and breaths shorten
  to 40–120ms, so seams complete in ≈70% of the desktop time on
  the smaller paths.
- **Choreography timeline (v2).** Per seam, relative to trigger:
  t=0 first burst (seeded 5–13%) over 90–160ms → breath 50–180ms →
  bursts repeat; fissure anchors (§6.3) fire as the front passes
  them; dust (§6.4) sheds from the front throughout → final burst
  lands the front at 100% → wet phase 2400ms (dust settles, seam at
  full `--gold`) → cured; runner eligibility begins.
- **State matrix (v2).** *Rest (cured):* seam gold, still. *Hover:*
  no change to the seam itself — hover light is §6.7's job, and a
  seam that also brightened wholesale would double the effect.
  *Focus:* seams are never focusable. *Active:* n/a. *Scrolled-
  past:* cured, unchanged. *Disabled:* a seam whose vessel section
  was removed from the page is removed with it — the engine never
  runs an orphaned seam. *Touch:* identical engine; touch changes
  triggers (tap-to-heal on cards, §6.9), never the burst rhythm.
- **Breakpoints (v2).** ≥1200px: as specified. 768–1199px: seam
  stroke 2.25px, concurrency cap 2. <768px: stroke 2px, bursts
  8–16%, concurrency cap 2, and section seams complete before their
  vessel's pieces finish converging (small screens read the gold
  first, the geometry second).
- **Edge cases & failure modes (v2).** *Very short seam (<40px):*
  bursts collapse to a single 120ms draw — a 5% burst of a 30px
  seam is sub-pixel theatre. *Visitor scrubs back up mid-run:* the
  target freezes at its highest reached value; the engine finishes
  to that target and holds (one-way law). *Tab hidden mid-burst:*
  the loop pauses; on return, the breath timer is re-based so the
  seam resumes its rhythm instead of jumping. *Two seams sharing an
  anchor point:* the later seam's first burst is delayed until the
  earlier front passes the junction, so gold never crosses gold
  mid-air.
- **Accessibility spec (v2).** Seams are decorative SVG
  (`aria-hidden="true"`); the information "this vessel was broken
  and mended" is carried by the mend note text, not the line. The
  burst rhythm is visual only — no audio, no haptics. Seams never
  carry links or text. On paper grounds the crack underlay
  guarantees the seam's *location* is perceivable at 1.74:1-gold
  plus the charcoal hairline's 13.10:1 edge.
- **Tokens consumed (v2).** `--gold`, `--crack`, `--ease-draw`,
  `--burst-min` (5%), `--burst-max` (13%), `--breath-min` (50ms),
  `--breath-max` (180ms), `--seam-wet` (2400ms), `--seam-force`
  (5000ms).

### 6.3 Secondary fissures

- **What & why.** Real breakage is not one clean line: around every
  main crack, fine fissures branch off. Fifteen tiny fissures live
  across the page — 7 on the hero bowl, 5 across the three
  service-card vessels (2+2+1), 2 in the footer, 1 on the final
  mini-bowl (§6.17) — each anchored to a point on its parent seam,
  sprouting the moment the growing front passes its anchor. They are
  the detail that separates a drawn crack from a *break*: damage
  with a blast radius.
- **Structure.** Each fissure is a short SVG path (18–46px, one or
  two segments, branching at 30–60° from the parent seam per §4)
  stored in the parent vessel's SVG with `data-anchor` = the
  normalised position (0–1) along the parent seam where it roots.
  Fissures draw in `--crack` first (they are damage) and gild only
  when the parent seam's wet phase reaches them — a fissure's gold
  always lags its parent's front by the fissure's own length, so
  gold appears to *wick* into the branches.
- **Motion spec.** Trigger: driven entirely by §6.2's front
  position. When the front passes an anchor, the fissure draws its
  crack over 180ms `--ease-draw` (a quick, single burst — fissures
  are too small for the burst engine), sheds one small dust puff
  (§6.4), and begins gilding 120ms later over 300ms. Total
  fissure event: ≈600ms, fully determined by the parent's progress;
  no fissure has its own timer.
- **States.** Latent (invisible, part of the unbroken surface) →
  cracked (dark hairline) → gilding → mended (gold hairline,
  1.25px). Scrolled-past: mended. Fissures never un-crack.
- **Content merge.** Each fissure belongs to its vessel's own crack
  system, positioned on the object's real stress points — rim,
  handle root, foot ring — the places a potter would predict. A
  fissure floating on background or text is a build error the §10
  gate rejects by inspection.
- **Failure fallback.** No JS: fissures render mended (gold, drawn)
  with their vessels. If the parent seam's engine falls back to the
  opacity fade (§6.2), fissures fade with it in the same frame. No
  watchdog of their own is needed: a fissure's state is a pure
  function of its parent's front position, recomputed each frame,
  so it cannot be stranded.
- **Reduced-motion variant.** Fissures are present and gold in the
  static mended state. Nothing sprouts.
- **Performance budget & mobile variant.** Fifteen short paths,
  transform/opacity-free (dashoffset only, and only while their
  parent runs). Mobile: fissure count per vessel is unchanged
  (they are identity, not garnish), but the dust puff is cut below
  768px (§6.4's budget rule).
- **Choreography timeline (v2).** Relative to parent front: front
  reaches anchor → +0ms crack draw begins → +180ms crack complete,
  dust puff → +300ms gild begins → +600ms fissure mended. Across a
  vessel, fissures fire in anchor order, which is rim-to-foot —
  damage appears to spread the way the break actually ran.
- **State matrix (v2).** *Rest:* mended gold hairline. *Hover:*
  fissures catch §6.7's glow with their parent seam (same mask).
  *Focus:* never focusable. *Active:* n/a. *Scrolled-past:*
  mended. *Disabled:* n/a — a fissure has no behaviour to disable.
  *Touch:* identical; no touch-specific state.
- **Breakpoints (v2).** ≥1200px: full lengths. 768–1199px: lengths
  ×0.85 (vessels are smaller; fissures scale with their object,
  never independently). <768px: ×0.7, stroke 1px, dust puff cut.
- **Edge cases & failure modes (v2).** *Anchor beyond a scrubbed
  seam's target:* the fissure waits — it fires when the front
  actually passes, even if that is on a later scroll-down (front
  position is monotonic per the law). *Fissure crossing text:* the
  fracture plan (§4) forbids fissure paths over text boxes; the
  gate checks path bounding boxes against text bounding boxes in
  the reference build. *Parent vessel removed:* fissures are in
  the vessel's SVG and leave with it.
- **Accessibility spec (v2).** Fully decorative, `aria-hidden`.
  Fissures are 1–1.25px hairlines: they are never the sole carrier
  of any distinction (a fissured vs unfissured vessel is told apart
  by its mend note's piece count, in text).
- **Tokens consumed (v2).** `--crack`, `--gold`, `--ease-draw`,
  `--dur-fissure` (180ms), `--dur-fissure-gild` (300ms),
  `--fissure-count` (15).

### 6.4 Gold dust at the join

- **What & why.** While a seam is wet, its growth front sheds tiny
  gold specks — the powder the mender dusts onto fresh lacquer,
  visible only where work is actively happening. Dust is the theme's
  proof of *present-tense* repair: a seam with dust is being mended
  now; a seam without it is history. Two gold tones, randomised
  size and drift, twinkle, settle downward, fade.
- **Structure.** A per-vessel `<canvas>` overlay (hero bowl, three
  card vessels, footer vessel — five canvases page-wide, the only
  canvases in the theme), absolutely positioned over the vessel's
  SVG box, `pointer-events: none`. Particles are emitted from the
  current front position reported by §6.2's engine (and from
  fissure anchors during §6.3 events). Each particle: size
  1–2.5px, colour `--gold` or `--gold-bright`, life 700–1300ms,
  drift −6..+6px horizontal, settle +10..+22px vertical under a
  light gravity curve, alpha twinkle via a sine on its own phase.
- **Motion spec.** Emission rate: 26 particles/second per active
  front, only while the front is in a burst phase (breaths shed
  nothing — dust falls when the crack *moves*). Fissure puff: 7
  particles in one 120ms emission. Particle motion runs in the
  shared loop; a canvas with no live particles stops being cleared
  and redrawn (it idles at zero cost). Dust ceases the frame the
  seam's wet phase ends (§6.2) — the last particles settle and the
  join is clean.
- **States.** Shedding (front bursting) → settling (front in breath
  or wet phase ending; existing particles finish their fall) →
  absent (cured seam; canvas empty). No other states; dust has no
  rest state of its own.
- **Content merge.** The dust is the repair material itself, emitted
  from the exact millimetre being repaired on the content object.
  It never appears over text, never on backgrounds, never as
  ambience — if no seam is running, the page has no dust, and that
  absence is itself information.
- **Failure fallback.** No canvas support or no JS: no dust, and
  nothing is missing — the seams and their wet sheen carry the
  repair alone. Canvas failure is detected once at init
  (`getContext` null) and the subsystem disables itself silently.
  Watchdog: particle count is hard-capped per canvas (140); the
  emitter drops particles rather than exceed it.
- **Reduced-motion variant.** No dust. Wet seams are indicated by
  the seam's brighter gold during what would be the wet phase —
  but under reduced motion seams arrive cured (§6.2), so even that
  is moot: the variant is simply a clean, mended page.
- **Performance budget & mobile variant.** Five small canvases,
  ≤140 particles each, drawn only while a seam runs; particle
  update is arithmetic in the shared loop, ≤0.3ms/frame total.
  Mobile: emission 16/second, cap 80 per canvas, fissure puffs
  cut (§6.3), footer canvas removed (the footer vessel keeps its
  loop, §6.12, without dust).
- **Choreography timeline (v2).** Front enters burst → emission
  begins same frame → particles twinkle/settle over 700–1300ms
  each → front enters breath → emission stops, stragglers settle →
  seam completes → final particles land by +1300ms → canvas idle.
  The dust's whole life is slaved to §6.2's state machine; it has
  no independent timeline to drift out of sync.
- **State matrix (v2).** *Rest:* absent. *Hover:* dust does not
  respond to hover — the pointer is not a mender's hand; §6.7's
  glow is the hover system. *Focus:* no response. *Active:* n/a.
  *Scrolled-past:* absent (all seams cured). *Disabled:* the whole
  subsystem disables on canvas failure or `prefers-reduced-motion`,
  cleanly and permanently for the session. *Touch:* identical
  emission; touch triggers seams (§6.9), dust follows.
- **Breakpoints (v2).** ≥1200px: full rates. 768–1199px: emission
  20/second, cap 110. <768px: mobile variant above; canvases match
  their (smaller) vessel boxes exactly, re-measured on resize.
- **Edge cases & failure modes (v2).** *Resize mid-mend:* canvas
  boxes re-measure on the loop's next frame; in-flight particles
  keep their coordinates (a 1-second drift is invisible). *Many
  seams queued:* the §6.2 concurrency cap (3) bounds total
  emission to ≈78/second page-wide. *DevicePixelRatio > 2:*
  canvas backing store caps at 2× — dust is soft-edged by design,
  so the cap is invisible.
- **Accessibility spec (v2).** Pure decoration: canvases are
  `aria-hidden`, outside the accessibility tree's content path,
  and carry no information (a seam's wet state is also announced
  by its mend note's status word — "mending" → "mended" — in
  §6.17's record). Dust never flashes above 3Hz: twinkle period
  per particle is ≥700ms and alpha range is 0.35–1, inside
  photosensitivity limits.
- **Tokens consumed (v2).** `--gold`, `--gold-bright`,
  `--dust-rate` (26/s), `--dust-cap` (140), `--dust-life-min`
  (700ms), `--dust-life-max` (1300ms).

### 6.5 Lacquer sheen sweep

- **What & why.** When the hero bowl's mending completes, a clipped
  skewed sheen band sweeps across its glaze once — the light test a
  mender runs over finished lacquer to prove the surface is sealed.
  It re-sweeps whenever the pointer returns to the bowl. The sheen
  is the theme's certificate of completion, and it lives on the
  vessel's surface, never on the page behind it.
- **Structure.** A `::after` band on the bowl's container: a 34%-
  width linear-gradient (transparent → `--paper` at 14% → transparent),
  skewed −18°, clipped to the bowl's silhouette by the same SVG
  clipPath the shards use, translated from −60% to +160% of the
  bowl's width. On other vessels the sheen exists only where §6.9
  grants it (card vessels, on settle) — the hero's is the full
  version; the mini-bowl (§6.17) gets a 900ms version.
- **Motion spec.** Trigger: hero mend completion (§6.1 t≈1900) and
  pointer re-entry to the bowl after ≥4000ms away (a returning
  hand re-tests the surface; hovering continuously does not
  retrigger). One pass over `--dur-sheen` 1400ms `--ease-sweep`,
  no loop, no idle shimmer — lacquer does not sparkle on its own.
- **States.** Absent (before mend, and at rest) → sweeping →
  absent. There is no persistent sheen state; a permanently glossy
  overlay is exactly the slop this element refuses.
- **Content merge.** The sweep proves a property of the content
  object — its glaze is finished — and is clipped to that object's
  silhouette. It cannot drift onto the headline or the ground: the
  clip is the vessel.
- **Failure fallback.** No JS: no sweep (the bowl stands mended;
  the sheen is a light effect, and its absence removes nothing).
  If the mend was forced by watchdog (§6.1), the completion sweep
  still fires once — the certificate is issued even when the
  ceremony was cut short.
- **Reduced-motion variant.** No sweep. A static 6% `--paper`
  gradient rests on the bowl's upper-left glaze in the mended
  state, suggesting the sealed surface without moving light.
- **Performance budget & mobile variant.** One composited transform
  on one clipped layer, 1400ms, at most a few times per session.
  Mobile: the sweep still fires on completion (touch has no hover
  to re-trigger it — §6.1's state matrix grants the auto-play);
  re-trigger on tap of the bowl.
- **Choreography timeline (v2).** Mend completes → +120ms (one
  breath after the last dust settles) → band enters at −60% →
  crosses the belly at ≈700ms → exits +160% at 1400ms → layer
  removed from the compositor (transform reset, `will-change`
  dropped). Re-trigger path: pointer leaves bowl → 4000ms absence
  timer → pointer re-enters → sweep.
- **State matrix (v2).** *Rest:* absent. *Hover:* triggers per the
  re-entry rule; continuous hover = one sweep only. *Focus:*
  keyboard focus entering the hero (CTA or link) triggers one
  sweep, same as §6.1's focus ruling. *Active:* suppressed during
  the CTA's press dip (two motions on one object never overlap).
  *Scrolled-past:* no sweeps off-screen; the re-entry timer only
  runs while the bowl is in the viewport. *Disabled:* n/a.
  *Touch:* completion auto-play + tap re-trigger.
- **Breakpoints (v2).** ≥1200px: band 34% width, skew −18°.
  768–1199px: 30%, −16°. <768px: 42% (the bowl is relatively
  larger on screen), duration 1100ms.
- **Edge cases & failure modes (v2).** *Pointer skims the bowl
  corner:* the re-entry rule requires the pointer to cross the
  bowl's inner 70% box — a corner graze is not a returning hand.
  *Mend forced instantly (return visit):* the bowl arrives whole
  and the sweep plays once at load +600ms, so the certificate is
  still witnessed. *Sheen over the headline:* the headline sits
  above the bowl layer (z-order authored in §4); the clip keeps
  the band inside the silhouette regardless.
- **Accessibility spec (v2).** Decorative; `aria-hidden` by virtue
  of being a pseudo-element on an already-labelled figure. The
  sweep's peak alpha (14% white over ≤34% of one object, 1400ms,
  non-repeating) is far inside flash limits. It never coincides
  with text changes, so nothing needs announcing.
- **Tokens consumed (v2).** `--paper`, `--ease-sweep`,
  `--dur-sheen` (1400ms), `--sheen-alpha` (0.14), `--sheen-rearm`
  (4000ms).

### 6.6 Travelling seam light (runners)

- **What & why.** After a vessel is whole, a highlight runs slowly
  along its main seams — finished gold catching light as the room's
  light moves. The runner is the scar kept alive: proof the mend is
  not a printed line but a metal inlay with a surface. It runs on
  the hero bowl's 3 main seams, each card's main seam, the
  mini-bowl, and the footer crack; the hero title's seam runs a 7s
  linear loop.
- **Structure.** For each seam, a second stroke overlaid on the gold:
  `--gold-bright`, 3.5px, with `stroke-dasharray` set from the
  path's measured length — a bright segment of 12% of the length
  followed by 88% gap — and the offset animated so the segment
  travels the path. Duration is *derived*: JS measures each path's
  real length and sets duration = length / 90 px-per-second (hero
  seams ≈380px → ≈4.2s), so light travels at one physical speed on
  every seam on the page, long or short. The hero title seam is the
  exception by the original design: a fixed 7s linear loop.
- **Motion spec.** Trigger: a seam reaching cured state (§6.2).
  Travel is linear (light does not ease), direction rim→foot on
  bowls, left→right on section seams. Loops are offset per seam
  (index × 1.7s) with a 2600ms dark interval between passes — at
  most 2 runners are lit on screen at any moment; the scheduler
  enforces it. Off-screen runners pause (IntersectionObserver);
  the light does not travel where no one can see it.
- **States.** Unlit (seam not yet cured) → running (segment
  travelling, then dark interval) → resting whole (between passes
  the seam is plain gold). Scrolled-past: still running if in
  view — a healed page keeps its quiet life.
- **Content merge.** The light runs *in* the crack paths of the
  content objects — the same authored geometry as §6.2/§6.3 — so
  the ambient life of the page is located exactly on its scars.
  There is no ambient effect anywhere else in the theme.
- **Failure fallback.** No JS: no runners; seams are static gold,
  which is the state the whole theme is built to remain legible
  in. If path measurement fails for a seam, that seam simply never
  runs — a dark seam is a valid seam.
- **Reduced-motion variant.** Runners do not run. One static
  brightening remains: the first 12% of each main seam is rendered
  in `--gold-bright` in the mended state, a frozen suggestion of
  caught light.
- **Performance budget & mobile variant.** One dashoffset animation
  per lit seam, compositor-friendly; ≤2 concurrent. Mobile:
  travel speed 110px/s (smaller paths, same perceived pace),
  dark interval 3200ms, and card seams do not run below 768px —
  the hero and footer keep the page's ambient signature.
- **Choreography timeline (v2).** Seam cures → +800ms → first pass
  begins (the mend is allowed one quiet moment before its light
  show) → pass duration = length/90s → dark 2600ms → repeat,
  phase-offset by seam index. The footer crack's runner is synced
  to §6.12's loop: it lights only during that vessel's whole rest
  phase.
- **State matrix (v2).** *Rest:* running on schedule. *Hover:* the
  hovered vessel's runner accelerates ×1.6 while §6.7's glow is
  active (attention quickens the light), returning to 90px/s on
  leave. *Focus:* a focused card (§6.9) gets the same ×1.6.
  *Active:* n/a. *Scrolled-past:* running if visible. *Disabled:*
  a seam in a removed section stops cleanly. *Touch:* no hover
  acceleration; runners run at base speed.
- **Breakpoints (v2).** ≥1200px: full system. 768–1199px: speed
  100px/s, ≤2 lit. <768px: hero + footer only, dark interval
  3200ms, ≤1 lit at a time besides the footer.
- **Edge cases & failure modes (v2).** *Very long seam (>900px,
  the margin vein is excluded — §6.13 has its own light rule):*
  duration caps at 9s; light on a metre of gold should cross in a
  breath, not a minute. *Tab hidden:* all runners pause; phases
  resume without jumps. *Many vessels cured at once (jump-scroll):*
  first passes stagger by the index offset so the page never
  flashes in chorus.
- **Accessibility spec (v2).** Decorative (`aria-hidden`). Runner
  brightness peaks at `--gold-bright` on `--gold` — a luminance
  ratio under 1.4:1 across a 3.5px line — no flash risk, no
  information carried. Motion-sensitive visitors get the static
  variant above.
- **Tokens consumed (v2).** `--gold`, `--gold-bright`,
  `--runner-speed` (90px/s), `--runner-gap` (2600ms),
  `--runner-segment` (12%), `--ease-glow`.

### 6.7 Pointer-local seam glow

- **What & why.** Moving the pointer near a finished seam makes the
  gold glow *at that spot only* — attention polishing the exact
  millimetre of scar being looked at. The normal cursor is untouched
  (theme standing rule); the feedback lives inside the crack itself.
  It is the theme's most intimate interaction: the visitor's gaze,
  given weight.
- **Structure.** Per vessel, an SVG `<radialGradient>` highlight
  stroke layered over each main seam, masked to the crack paths
  themselves — hand-built mask in the hero SVG; per-card masks built
  in JS from the same path data (§4's single geometry source). The
  glow is a 90px-diameter radial of `--gold-bright` at up to 85%
  alpha, centred on the pointer's projection onto the nearest seam
  point (computed against the path's sampled points, 24 samples per
  seam, cached at build-in). On the hero, the glow is gated: it arms
  only once the bowl is lit (mended + first sheen, §6.5) — you
  cannot polish a seam that does not exist yet.
- **Motion spec.** Trigger: pointer proximity within 46px of a seam
  path. Glow centre follows the pointer's seam-projection through
  the shared loop (lerp 0.12 — the light trails a breath behind the
  hand, like heat). Fade in 240ms `--ease-glow` on entering range,
  fade out 480ms on leaving. Alpha peaks at the projection point
  and falls to zero at 45px along the seam in both directions: a
  lit *spot*, never a lit seam.
- **States.** Cold (no pointer near) → warming (fading in) → lit
  (tracking) → cooling (fading out) → cold. Scrolled-past: fully
  functional — healed seams anywhere on the page accept the glow.
- **Content merge.** The glow exists only inside the crack geometry
  of real vessels; the mask guarantees not one pixel of light lands
  on glaze, text or ground. Attention is paid to the content's own
  scar, nowhere else.
- **Failure fallback.** No JS: no glow; seams are gold and still.
  If mask construction fails for a vessel (path data error), that
  vessel's glow disables itself — the failure mode is *less light*,
  never light in the wrong place.
- **Reduced-motion variant.** No tracking glow. Keyboard and
  reduced-motion visitors get a static equivalent: a focused or
  hovered vessel's main seam brightens uniformly to `--gold-bright`
  at 40% for as long as the focus/hover holds — the information
  "this seam is attended" without the travelling light.
- **Performance budget & mobile variant.** One gradient position
  update per vessel per frame, only while a pointer is in range;
  sample caches are built once (≤24 points × ≤9 seams). Mobile:
  **no pointer, no glow** — touch uses §6.6's acceleration and
  §6.9's settle instead. The subsystem does not initialise on
  coarse pointers.
- **Choreography timeline (v2).** Pointer crosses 46px threshold →
  nearest-seam projection computed → glow fades in 240ms at that
  point → tracks with 0.12 lerp while in range → pointer leaves →
  480ms cooling fade → cold. On the hero, add the gate: bowl cured
  + sheen witnessed, else the timeline never starts.
- **State matrix (v2).** *Rest:* cold. *Hover:* lit and tracking
  (this element *is* the hover state of every seam). *Focus:* the
  reduced static brightening (above) — keyboard focus must not be
  a lesser way to attend. *Active:* while a card is pressed
  (§6.9), its glow freezes at the press point for the press
  duration. *Scrolled-past:* lit on hover, as at rest. *Disabled:*
  seams of a disabled/unavailable service card (§6.9) stay cold —
  you cannot polish what is not offered. *Touch:* not initialised.
- **Breakpoints (v2).** ≥1200px: radius 90px, range 46px.
  768–1199px: radius 76px, range 40px. <768px: not initialised
  (coarse pointer assumed; a fine-pointer small screen — rare —
  gets the 768 values).
- **Edge cases & failure modes (v2).** *Pointer exactly between
  two seams:* the nearer projection wins; ties hold the previous
  seam until the difference exceeds 6px (hysteresis — the light
  must not flicker between two scars). *Fast pointer:* the lerp
  trail stretches the glow along the seam briefly — acceptable,
  physical; alpha caps so it never reads as a comet. *Seam under
  a pinned section boundary:* projections are computed in the
  vessel's local coordinates, so pinning transforms cannot offset
  the light.
- **Accessibility spec (v2).** Decorative; the glow annotates
  nothing and gates nothing. It never reduces text contrast (mask
  excludes text boxes, §6.3's gate rule) and never appears without
  the seam's static gold beneath it, so low-vision visitors lose
  nothing by ignoring it. Focus parity is specified above.
- **Tokens consumed (v2).** `--gold-bright`, `--ease-glow`,
  `--glow-radius` (90px), `--glow-range` (46px), `--dur-glow-in`
  (240ms), `--dur-glow-out` (480ms).

### 6.8 Fracture→heal sections

- **What & why.** The theme's core scroll gesture: the craft steps,
  the stats, the testimonial — every content section — starts as
  offset, rotated fractured blocks and converges into register as
  it centres on screen, gold step-seams drawing as it heals. The
  page's argument is applied to its own layout: nothing on this
  page gets to be whole without first being seen broken.
- **Structure.** Each section is a vessel (§4): its content blocks
  are wrapped in 3–4 clip-piece containers whose fracture plan is
  authored per section. Pieces carry JS-armed transforms (offset
  6–22px, rotation 0.4–1.6°, per-piece parallax factors 0.94/1.0/
  1.06). The section's seams are SVG paths across the piece
  boundaries, run by §6.2's engine. The section pins (≥1200px) for
  130vh while a scrub value q (0→1) drives convergence; below the
  pin breakpoints, an IntersectionObserver trigger runs the same
  heal as a timed sequence.
- **Motion spec.** Trigger: section's top crosses 78% of the
  viewport (pin engages) or 65% (unpinned fallback). Convergence
  is scrubbed to q through the shared loop (lerp 0.12): piece
  offsets scale by (1−q), rotations likewise; at q=0.55 the seams'
  burst engine targets q-mapped positions (§6.2); at q=1 the
  pieces lock the last 4% with `--ease-lock` (a scrub that ends in
  a click) and the section performs the 1.6px settle dip
  (`--ease-settle`, 550ms). Forced heal: any section not healed
  6000ms after first entry heals over 600ms regardless of scroll;
  the theme-wide ceiling is 7000ms (§5).
- **States.** Broken (entered, q=0) → mending (0<q<1) → healed
  (rest; seams cured, §6.13's vein branch drawn) → scrolled-past
  (healed, unchanged — the law). A section the visitor jumps past
  heals instantly in the jump (§13's catch-up rule).
- **Content merge.** The fracture runs through the content's own
  boundaries — the testimonial splits between its two voices, the
  craft steps split between step 2 and 3 — never through a word.
  The blocks are the section's real blocks; the pieces are their
  transforms. Read with JS off, every section is whole and ordered.
- **Failure fallback.** No JS: all sections whole, seams gold, in
  document order — the page is a shelf of mended vessels.
  Watchdogs: per-section 6000ms force-heal; a global 7000ms sweep
  heals anything left; if the shared loop dies, a CSS-only fallback
  class (applied by a 1500ms heartbeat check) removes all armed
  transforms in one frame.
- **Reduced-motion variant.** Sections arrive whole. The *story* of
  their breakage is carried by each section's mend note and its
  still-visible gold seams — reduced motion removes the event,
  never the evidence.
- **Performance budget & mobile variant.** Per section: ≤4
  transformed wrappers + ≤3 seam paths; only the pinning section
  and its neighbours are live in the loop. Mobile (<768px): no
  pin; heal runs as a 900ms timed sequence on entry (pieces
  converge with `--ease-settle`, seams burst-run at §6.2's mobile
  rates), offsets halve, rotations cap at 0.8°.
- **Choreography timeline (v2).** Section top crosses 78% → pin
  engages (desktop) → q scrubs 0→0.55 across 65vh of scroll:
  pieces drift toward register, parallax factors converging →
  q 0.55→1 across the next 65vh: seams burst toward their targets,
  fissures sprout (§6.3) → q=1: lock click (last 4%, 180ms),
  settle dip 550ms → vein branch draws (§6.13, 700ms) → section
  healed; pin releases at 130vh. Unpinned: the same beats
  compressed into 900–1400ms of time.
- **State matrix (v2).** *Rest:* healed, seams gold. *Hover:*
  section-level hover does nothing (hover belongs to seams,
  §6.7, and cards, §6.9 — a whole section that reacts to a pointer
  is a billboard). *Focus:* focus entering a broken-but-entered
  section fast-forwards its heal to q=1 over 300ms — keyboard
  visitors never read through a fracture. *Active:* n/a.
  *Scrolled-past:* healed. *Disabled:* n/a. *Touch:* timed heal
  variant; a section also heals if the visitor taps it while
  broken (the tap is a hand steadying the vessel).
- **Breakpoints (v2).** ≥1200px: pinned scrub as specified.
  768–1199px: pin shortens to 115vh, offsets ×0.75. <768px:
  unpinned timed heal, offsets ×0.5, one section heals at a time
  (queue by entry order).
- **Edge cases & failure modes (v2).** *Very tall section
  (>160vh of content):* the vessel splits at its authored mid-seam
  into two vessels at build time — a bowl too big for the bench is
  two bowls; the gate rejects a single vessel taller than 160vh.
  *Visitor scrolls up into a mending section:* q holds its maximum
  (one-way law); pieces never re-scatter. *Anchor link into a
  broken section:* the target section heals instantly on arrival.
  *Print:* all sections print healed (print stylesheet forces the
  rest state).
- **Accessibility spec (v2).** DOM order is reading order at all
  times — transforms never reorder content for assistive tech.
  Headings are reachable and legible in the broken state (offsets
  are ≤22px; no text is clipped by its own piece at any q — the
  fracture plan keeps 8px of clear margin inside each clip).
  Focus fast-forward (above) guarantees keyboard parity. Section
  contrast follows §2 in both broken and healed states (shard
  faces carry rice text at 8.72:1).
- **Tokens consumed (v2).** `--shard`, `--paper`, `--gold`,
  `--ease-lock`, `--ease-settle`, `--dur-settle` (550ms),
  `--pin-travel` (130vh), `--heal-force` (6000ms),
  `--heal-ceiling` (7000ms).

### 6.9 Reassembling vessel cards

- **What & why.** The service list is a shelf of vessels: each
  service card carries its own small vessel, sitting in separated
  shards. Hovering the card settles the shards together while its
  crack gilds and glows, and the card tilts in 3D like a bowl
  turned in the hand. Interacting with a service *means handling
  its pot* — the visitor rehearses the commission before reading
  a word of the pitch.
- **Structure.** A card = vessel SVG (3 shards, 1 main seam, its
  2/2/1 fissures per §6.3) + service name, mend note, price line
  ("from £180 — 4 pieces, gold") and a text link. Card ground is
  `--shard` on charcoal shelves, `--paper` on the paper shelf
  (§7). The vessel's shards rest separated by 5–9px — visibly
  broken at rest, unlike sections: a service vessel is *awaiting*
  its mend, and the hover is the promise. On first arrival in the
  viewport, a grey shard-skeleton shimmer gilds across the card
  once (900ms) to announce it as a mendable object.
- **Motion spec.** Trigger: hover/focus (desktop) or first tap
  (touch). Shards settle together over 800ms `--ease-lock`
  (stagger 70ms, rim shard last — a bowl is finished at its rim),
  the main seam burst-runs (§6.2, ≈500ms at card scale), its
  fissures sprout, and the card tilts toward the pointer: rotateX/
  rotateY capped at 5°, driven by the shared loop (lerp 0.12),
  pivot at the card's foot so it tips like a vessel on a bench,
  never floats. On leave: tilt eases home over 600ms
  `--ease-settle`; the shards **stay settled** and the seam stays
  gold (the law — a handled vessel does not re-break because the
  hand left).
- **States.** Awaiting (shards apart, seam dark) → settling →
  mended (rest after first interaction; runner arms, §6.6) →
  tilted (hover) → mended. Scrolled-past: whatever state touch
  left it in. A card never returns to Awaiting within the session.
- **Content merge.** The vessel is the service: its piece count is
  the service's typical job ("Wedding bowls — usually 3–5 pieces"),
  its mend note is a real past job. The price line prices *that
  vessel's* repair. Nothing on the card is decoration; the tilt
  turns the product in the hand.
- **Failure fallback.** No JS: cards show mended vessels (the
  awaiting state is JS-armed) with full text and working links.
  Watchdog: a settle interrupted by pointer leave mid-flight
  completes over 200ms rather than freezing mid-air.
- **Reduced-motion variant.** Vessels arrive mended; no tilt, no
  shimmer. Hover/focus still warms the seam to `--gold-bright`
  (§6.7's static ruling) so the affordance survives.
- **Performance budget & mobile variant.** 3 cards per shelf row;
  per card 3 transforms + 1 seam + tilt — trivially cheap; the
  shimmer is one gradient pass. Mobile: no hover — first tap
  settles the vessel (800ms), second tap follows the link; tilt
  is cut entirely below 768px (a tipping card under a thumb reads
  as a bug, not a bowl).
- **Choreography timeline (v2).** Card enters viewport → shimmer
  gild 900ms (once) → idle Awaiting → pointer enters → t=0 tilt
  begins (loop), shards start → t=70/140 staggers → seam bursts
  from t=100 → fissures at their anchors → t=800 rim shard locks,
  card gives the 1.6px settle dip → runner arms at t=1600 →
  pointer leaves → tilt home 600ms; vessel stays mended.
- **State matrix (v2).** *Rest (unvisited):* Awaiting. *Rest
  (visited):* Mended. *Hover:* settling/tilted per above. *Focus:*
  identical to hover (settle + seam warm; tilt reduced to 2° —
  keyboard focus should not swing the shelf). *Active:* press
  dips the card 1.6px (`--ease-settle` 180ms). *Scrolled-past:*
  state persists. *Disabled:* an unavailable service ("Studio
  closed to new commissions until March") shows its vessel
  wrapped — shards bound with a paper band, seam dark, no settle
  on hover, link replaced by the apparatus note. *Touch:*
  tap-to-settle, tap-to-follow.
- **Breakpoints (v2).** ≥1200px: 3 cards per row, vessel 220px.
  768–1199px: 2 per row, vessel 190px, tilt cap 4°. <768px: 1 per
  row, vessel 168px, no tilt, shimmer cut.
- **Edge cases & failure modes (v2).** *Pointer races across the
  shelf:* settles queue per card but tilt follows only the current
  card; a card whose settle was triggered always completes it
  (leaving never strands a half-settled vessel — the 200ms
  completion rule). *Card content taller than the vessel:* the
  vessel sits above the text, never behind it, below 1200px (on
  wide screens it may sit left of the text at ≥1200px only).
  *A service with no vessel photograph/SVG:* the card uses the
  generic bowl outline with its own fracture plan — a card is
  never shipped vessel-less.
- **Accessibility spec (v2).** The whole card is one link (name +
  "— mend this vessel" in the accessible name); the vessel SVG is
  `aria-hidden` (its story is the mend note text). Focus ring:
  2px `--gold` outline offset 3px on charcoal (7.54:1), `--gold-deep`
  on paper. Tilt never moves the link's hit area (transform on a
  wrapper inside the link). Touch targets ≥48px.
- **Tokens consumed (v2).** `--shard`, `--paper`, `--gold`,
  `--gold-bright`, `--crack`, `--ease-lock`, `--ease-settle`,
  `--dur-card-settle` (800ms), `--tilt-max` (5°), `--stagger-shard`
  (140ms, card instance 70ms).

### 6.10 Mending ledger

- **What & why.** The stats section is a ledger, not a dashboard:
  three figures — **214 pieces repaired / 38 repair circles / 1,200
  cups of tea** — counting up as the ledger enters, separated by
  jagged gold crack dividers that draw as it arrives. Even the
  numbers are broken-and-mended objects; the dividers are cracks,
  not rules. The third figure is the theme's humanity: mending is
  slow, and the tea is counted as honestly as the gold.
- **Structure.** A paper-ground vessel (§4: the ledger is paperwork)
  with three figure blocks in a row (stacked on mobile), each =
  tabular figure (§3 data role) + apparatus unit label + one-line
  record note ("pieces" = every shard ever seated, counted from the
  studio book). Dividers are two short seam paths (vertical on
  desktop, horizontal stacked) run by §6.2's engine at ledger scale.
  Figures are `data-count` targets in markup; the printed DOM value
  is the final figure — counters only ever *arrive at* the truth.
- **Motion spec.** Trigger: ledger vessel heals (§6.8). Dividers
  burst-draw first (≈700ms), then figures count up over 1400ms on
  `--ease-settle`, in 40ms steps, staggered 160ms left to right —
  counting is stepped, never smooth, because a ledger is written
  entry by entry. Figures count **up only**, once, and hold. The
  tea figure's note ("the kettle is part of the studio") fades in
  at its count's end — the joke lands after the number, in writing.
- **States.** Unentered (figures at final values in DOM; JS arms
  them to 0 only in view of the trigger) → counting → recorded
  (rest). Scrolled-past: recorded. Re-entry never recounts (the
  law applies to numbers too).
- **Content merge.** The figures are the studio's real book, and
  the build rule is §1's: every figure must trace to the client's
  records or be replaced by one that does. The crack dividers are
  the section's own seams — the ledger vessel arrived broken like
  everything else.
- **Failure fallback.** No JS: figures stand at their final values,
  dividers drawn gold. Watchdog: a count interrupted (tab switch)
  completes to final on return — a ledger never shows a half-written
  number as fact.
- **Reduced-motion variant.** Figures printed at final values,
  dividers drawn. No counting.
- **Performance budget & mobile variant.** Three text updates per
  40ms tick for 1400ms — negligible. Mobile: figures stack; each
  counts as it individually centres (the row trigger becomes
  per-figure), dividers rotate to horizontal seams.
- **Choreography timeline (v2).** Ledger heals (q=1) → dividers
  burst 0–700ms → t=500 figure 1 counts (1400ms, done ≈1900) →
  t=660 figure 2 → t=820 figure 3 → tea note fades at ≈2300 →
  ledger recorded; §6.13's vein branch completes the section.
- **State matrix (v2).** *Rest:* recorded figures. *Hover:* no
  response (ledgers do not perform). *Focus:* a figure block is
  not focusable; the section's link ("Read the studio book") takes
  the standard ring. *Active:* n/a. *Scrolled-past:* recorded.
  *Disabled:* n/a. *Touch:* identical counts, per-figure trigger
  on mobile as above.
- **Breakpoints (v2).** ≥1200px: three across, figures 34px.
  768–1199px: three across, figures 28px, notes wrap to two lines.
  <768px: stacked, figures 30px (the stack gives them room back),
  horizontal seam dividers.
- **Edge cases & failure modes (v2).** *A figure with decimals or
  currency:* the ledger counts integers of things; money and
  measures belong to §6.16's shelf, and a build that needs a
  decimal here must re-voice it as a count ("1,200 cups", never
  "1.2k"). *Figure longer than its block (7+ digits):* apparatus
  label drops below the figure; the count duration stretches to
  1800ms so digit velocity stays readable. *Zero as a true figure*
  ("0 pieces refused this year" is not true of any real studio):
  the gate challenges any 0 in the ledger — zeroes are usually
  missing data wearing a number's clothes.
- **Accessibility spec (v2).** Figures are text; during counting
  they are `aria-hidden` duplicates, with the final value present
  once in a visually-hidden span — screen readers hear "214 pieces
  repaired" once, never a stutter of passing numbers. Dividers are
  decorative SVG. Contrast: charcoal figures on paper 13.10:1;
  apparatus labels `--gold-deep` on paper at apparatus size only
  (4.05:1, §3 law 1).
- **Tokens consumed (v2).** `--paper`, `--charcoal`, `--gold`,
  `--gold-deep`, `--ease-settle`, `--dur-count` (1400ms),
  `--count-step` (40ms).

### 6.11 Testimonial seam + visitor crack

- **What & why.** The testimonial is deliberately interrupted by a
  gold seam — the quote sits across a mend, its text broken by gold
  — and clicking it lays a hairline crack of the visitor's own
  across the story, which draws itself in lacquer-red and stays
  for the session. The anti-slop placement (a quote across a seam)
  becomes participatory: the visitor performs a break, and the page
  keeps it, unrepaired, as the one honest unrepaired thing.
- **Structure.** A paper vessel containing the quote in two blocks
  (before / after the seam) with the seam path crossing between
  and slightly into both — the fracture plan routes the seam
  through the paragraph gap and one line's word-space, never
  through glyphs (§6.8's rule). The visitor crack is a second,
  hidden SVG path across the quote's lower third, authored per
  testimonial, stroked `--lacquer` at 1.25px. A small apparatus
  invitation sits at the vessel's foot: "Touch the story — leave
  your own crack." The crack state persists in `sessionStorage`.
- **Motion spec.** Trigger: click/tap on the vessel (or its
  invitation button — the whole vessel is the target, the button
  is the keyboard path). The crack draws over 620ms: not burst-
  stepped (it is a fresh hairline, not a mend) but a single
  `--ease-draw` run with two micro-branches (300ms, delayed 200ms)
  — a break is quick; only mending is slow. It does **not** gild.
  It stays lacquer-red and open for the rest of the session: the
  visitor's damage is theirs, and the atelier does not presume to
  mend what it did not break.
- **States.** Whole-across-a-seam (rest) → cracking (620ms) →
  visitor-cracked (session-persistent rest). Scrolled-past: as
  left. A second click does nothing — one crack per visitor; the
  invitation's text changes to the apparatus note "Your crack,
  kept." once laid.
- **Content merge.** The seam interrupts the *story* — the quote is
  about the client's own broken bowl and its return — so the gold
  crosses the exact sentence where the bowl breaks ("…it slipped,
  ‖ and I heard it go…"). The visitor's crack lands on the same
  object they just read about: participation on the content, not
  on chrome.
- **Failure fallback.** No JS: the testimonial stands whole across
  its (drawn, gold) seam; the invitation line is omitted from the
  no-JS render (a promise the page cannot keep is not printed).
  Storage unavailable: the crack still draws; it simply does not
  persist past the page view.
- **Reduced-motion variant.** The crack appears fully drawn in one
  frame on click (the *act* is the visitor's; only its travel is
  removed). The seam is gold from the start, as everywhere.
- **Performance budget & mobile variant.** Two short paths; trivial.
  Mobile: tap target is the whole vessel (≥180px tall); the crack
  path shortens to the quote's width at that size (paths are
  authored per breakpoint in the fracture plan).
- **Choreography timeline (v2).** Click → t=0 hairline starts at
  the click's x-position projected on the path (the crack begins
  where the hand struck) → t=200 micro-branches → t=620 crack
  complete → invitation text crossfades to "Your crack, kept."
  (300ms) → session flag written. No settle dip: the vessel does
  not celebrate being broken.
- **State matrix (v2).** *Rest:* whole-across-seam, invitation
  showing. *Hover:* the vessel's seam warms (§6.7 static ruling on
  paper: `--gold-deep` edge brightens) and the cursor stays the
  normal pointer — the theme never changes the cursor, even here.
  *Focus:* the invitation button takes the ring; Enter lays the
  crack identically. *Active:* the button presses 1px; the vessel
  does not dip. *Scrolled-past:* state as left. *Disabled:* after
  the crack is laid, the button disables itself (one crack per
  visitor) with its text as the reason. *Touch:* tap = click;
  no hover warm.
- **Breakpoints (v2).** ≥1200px: quote 24px Mincho italic-free
  (§3 law 2 — the quote is prose, the *mend note* beneath it is
  the italic). 768–1199px: 21px. <768px: 19px, seam crosses at the
  paragraph gap only (narrow measures leave no safe word-space
  crossing).
- **Edge cases & failure modes (v2).** *A testimonial whose break
  sentence sits at the very start:* the seam crosses the first
  paragraph gap instead — the plan needs a gap, and the gate
  rejects a seam with no honest crossing point. *Visitor clicks
  during the section's own heal:* the crack queues until q=1
  (you cannot break what is still mending) — in practice a
  ≤1400ms wait, with the invitation pulsing once to acknowledge
  the intent. *Multiple testimonials:* only the designated one
  carries the visitor crack; others sit across seams without the
  invitation (one participatory object per page).
- **Accessibility spec (v2).** The quote is one continuous text for
  assistive tech (the seam is an SVG overlay; DOM text is
  unbroken, with the seam position marked only visually). The
  invitation is a real `<button>` with `aria-pressed` once laid.
  The crack is decorative; its existence is conveyed by the
  button's state and text change. Contrast: quote charcoal on
  paper 13.10:1; lacquer crack on paper is graphical (the crack
  carries no text).
- **Tokens consumed (v2).** `--paper`, `--charcoal`, `--gold`,
  `--gold-deep`, `--lacquer`, `--ease-draw`, `--dur-crack`
  (620ms).

### 6.12 Footer vessel loop

- **What & why.** A small vessel outline in the footer endlessly
  performs the whole craft in miniature: it draws itself, cracks
  (with fissures and a puff of dust), fills with gold, rests whole
  with its runner lit, then quietly re-breaks. The page's last
  content restates its argument as a cycle — mending is not an
  event, it is the studio's permanent condition.
- **Structure.** A 120px inline SVG at the footer's centre-left:
  vessel outline path, one main crack with 2 fissures (§6.3's
  footer pair), a mini dust canvas (desktop only, §6.4). The loop
  is a state machine in the shared loop with five phases; phase
  timings are tokens so the cycle can be tuned as one rhythm.
  The footer vessel is the *only* object on the page allowed to
  re-break — the law's single licensed exception, because it is a
  demonstration, not a record: its mend note reads "The practice
  piece. It breaks so the others don't have to."
- **Motion spec.** Cycle 14000ms: draw outline 1600ms
  (`--ease-draw`) → whole rest 2400ms → crack runs 500ms + fissures
  300ms + dust puff → broken rest 1800ms (the pause matters — the
  visitor must sit with it broken) → gold fills in burst-steps
  (§6.2 at miniature scale, ≈1200ms) → whole rest 3400ms with the
  runner lit (§6.6) → outline fades to 30% over 800ms and the
  cycle restarts. The loop runs only while the footer is in view.
- **States.** The five phases above, cycling. Scrolled-past =
  out of view = paused mid-phase, resuming exactly where it
  stopped (a kiln does not reset because you left the room).
- **Content merge.** The loop is the colophon's illustration,
  placed inside the footer's mend record (§6.17): it demonstrates
  the cycle the record documents. It is not a loading spinner, a
  logo animation, or a decoration — it is the footer *showing its
  work*.
- **Failure fallback.** No JS: the vessel stands drawn and whole,
  seams gold, beside the record. Any loop fault freezes it whole —
  the state machine's error path always resolves to the mended
  phase, never to a frozen crack.
- **Reduced-motion variant.** Static whole vessel, gold seams,
  runner frozen per §6.6's variant. The cycle is described in its
  mend note instead of performed.
- **Performance budget & mobile variant.** One small SVG + optional
  canvas; phase changes are the only writes when idle. Mobile:
  the loop runs without the dust canvas (§6.4), cycle lengthens
  to 16000ms (slower on smaller screens reads calmer), vessel
  96px.
- **Choreography timeline (v2).** t=0 outline draw → 1600 whole →
  4000 crack + fissures + puff → 4800 broken rest → 6600 gold
  fill (bursts) → 7800 whole rest, runner lit → 11200 fade to
  30% → 12000–14000 dark pause → t=14000 cycle restarts. The dark
  pause is specified: the loop must have a held breath, or it
  reads as a screensaver.
- **State matrix (v2).** *Rest:* cycling (in view). *Hover:* the
  cycle pauses on the current phase while hovered (a hand near
  the piece stills it) and the vessel's mend note tooltip-line
  (§11's in-theme replacement: a caption line beneath, always in
  the DOM) underlines in gold-deep. *Focus:* the footer vessel is
  not focusable; the record's links behave per §6.17. *Active:*
  n/a. *Scrolled-past:* paused. *Disabled:* n/a. *Touch:* no
  hover-pause; the cycle runs while in view.
- **Breakpoints (v2).** ≥1200px: 120px vessel, full cycle with
  dust. 768–1199px: 108px, dust kept. <768px: 96px, no dust,
  16000ms cycle.
- **Edge cases & failure modes (v2).** *Footer in view at load
  (short page):* the cycle starts at the whole-rest phase, not
  the draw — a visitor who lands at the foot meets a mended
  vessel first. *Long session:* the loop is phase-based on the
  shared rAF clock, so it cannot drift or accumulate error.
  *Multiple footers (page fragments):* only the instance with
  `data-practice-piece` runs; duplicates render static-whole.
- **Accessibility spec (v2).** `aria-hidden` (the cycle is a
  demonstration; its content — the mend cycle — is stated in the
  adjacent record text). It never flashes: the crack phase is a
  500ms draw, the fade 800ms, both single events per 14s. It sits
  outside the tab order and never moves layout (fixed box).
- **Tokens consumed (v2).** `--gold`, `--gold-bright`, `--crack`,
  `--ease-draw`, `--ease-cure`, `--cycle-footer` (14000ms),
  `--dur-crack` (620ms, footer instance 500ms).

### Page-family elements

### 6.13 The margin vein (page family: navigation / progress)

- **What & why.** A gold vein runs down the left margin, extending
  as vessels mend and branching into each healed section. It is
  simultaneously the page's navigation spine, its progress record,
  and its root system — the one gold line allowed outside a vessel
  (§4), because it is the record of all the vessels. Each branch is
  a link: the vein is how you travel a page whose sections are
  objects.
- **Structure.** A fixed SVG rail (width 56px at ≥1200px) holding
  one vertical path (the trunk) and one branch path per section,
  each branch ending at a small vessel-glyph node labelled in
  apparatus with the section's name (rotated labels are refused —
  labels sit horizontally in the rail's expanded state, §below).
  Trunk length maps to healed progress: its drawn length = the
  fraction of sections healed × the rail height, computed from the
  heal registry (§6.8 reports each heal), never from raw scroll
  pixels — the vein records *mending*, not scrolling. Branches
  draw when their section heals.
- **Motion spec.** Trunk extension is scrubbed through the shared
  loop toward the registry's target (lerp 0.12), drawn with
  `--ease-draw` character (it grows like a root: steady, with the
  §6.2 burst rhythm at 3× scale — bursts of 15–30% of the pending
  length). Branch draw: 700ms `--ease-draw` at the moment of heal,
  ending in the node glyph fading in (240ms). The current section's
  node carries a slow runner (§6.6 rules, vein instance: speed
  60px/s).
- **States.** Growing (sections unhealed below) → complete (all
  healed; trunk reaches the footer's root knot, §6.17) → the
  current-section node is lit as the visitor reads. Scrolled-past
  sections keep their branches — the vein is a record, and records
  do not unwrite.
- **Content merge.** The vein's branches *are* the sections' heal
  events and its nodes are their links: navigation, progress and
  ornament are one object grown from the page's actual repair
  history. A page where nothing has healed yet shows a short vein
  and an honest emptiness below it.
- **Failure fallback.** No JS: the vein renders complete with all
  branches and nodes (the mended state is the default), functioning
  as a plain anchor nav. Watchdog: if the heal registry stalls
  (a section's heal fault), the vein extends to that section
  anyway at its force-heal moment (§6.8) — the record follows the
  fallback, not the ideal.
- **Reduced-motion variant.** The vein is drawn complete from the
  start, branches present; the current-section node still lights
  (a state, not a motion).
- **Performance budget & mobile variant.** One path's dashoffset in
  the shared loop + ≤8 branch paths. Mobile (<768px): the rail
  leaves the margin and becomes a **top seam**: a 3px horizontal
  vein under the header whose length is the healed fraction, with
  node ticks; tapping the seam opens the nav as a paper sheet
  (§11's dialog replacement) listing sections with their heal
  states in apparatus.
- **Choreography timeline (v2).** Page load → trunk draws to the
  hero's node (600ms; the hero is vessel one) → hero heals → branch
  1 draws (700ms) → each subsequent heal extends the trunk in
  bursts toward the next node, branch on arrival → final heal →
  trunk completes into the footer's root knot (§6.17) with a
  300ms settle brightening.
- **State matrix (v2).** *Rest:* as grown. *Hover (node):* the
  node's label appears (rail expands 56→148px locally, 220ms
  `--ease-glow`) and the branch warms to `--gold-bright`. *Focus:*
  nodes are real links; focus shows the label identically and
  takes the §11 ring. *Active:* navigation runs the shard pass
  (§6.15) on same-page jumps over 2 sections, else a plain scroll.
  *Scrolled-past:* branches persist. *Disabled:* a section removed
  from the page removes its node; the trunk re-maps. *Touch:* top
  seam variant; nodes are ≥44px targets in the opened sheet.
- **Breakpoints (v2).** ≥1200px: left rail 56px, vein at x=28px.
  768–1199px: rail narrows to 40px, vein at x=20px, labels only on
  hover/focus (no expansion — the rail overlays the shelf gap,
  never content). <768px: top seam variant.
- **Edge cases & failure modes (v2).** *A page with two sections:*
  the vein still runs (one branch is a poor root, but the record
  is the record). *A page with twelve:* node labels abbreviate to
  apparatus short forms authored in markup; the trunk mapping is
  registry-based, so count changes need no code change. *Visitor
  heals sections out of order (anchor jump):* the trunk draws
  continuously to the furthest healed node, with unhealed gaps
  shown as `--crack` hairline pending segments — the vein is
  honest about the gap instead of pretending a root grew through
  air.
- **Accessibility spec (v2).** The rail is a `<nav>` with a list of
  links; each link's name includes its state ("Craft — mended" /
  "Craft — unvisited") via visually-hidden text, updated at heal.
  The SVG vein itself is `aria-hidden`. Focus order = document
  order of sections. On mobile the seam button is
  `aria-expanded`-controlled and the sheet is labelled.
- **Tokens consumed (v2).** `--gold`, `--gold-bright`, `--crack`,
  `--ease-draw`, `--ease-glow`, `--vein-x` (28px),
  `--dur-branch` (700ms).

### 6.14 The commission form (page family: forms / conversion)

- **What & why.** The conversion is a repair commission: the
  visitor describes their broken thing and sends it to the
  atelier. The form is a paper vessel (§4) — paperwork on the lit
  desk — and its grammar is the studio's: you do not "submit", you
  *send a piece in*. Its success state is not a tick; it is the
  piece's intake label, printed.
- **Structure.** A paper-ground vessel containing: your name; your
  direction (email); what broke (select refused, §11 — a ruled
  radio list: a bowl / a cup or mug / a plate / a vase / something
  else, written in); how many pieces (a stepper drawn as shard
  glyphs, 1–12+); the story of the break (textarea, ruled lines
  every 29px = the body line unit ×1.7); and the lacquer CTA
  "Send the piece in". On success the form is replaced by the
  intake label: apparatus text — `RECEIVED · MEND Nº <next from
  the ledger sequence> · <piece count> PIECES · GOLD` — above the
  studio's reply promise in prose, and the label's own hairline
  seam, pre-drawn gold (this label was never broken; it is a
  receipt).
- **Motion spec.** Field focus: the field's rule inks from
  `--shard-light` to `--gold-deep` over 240ms `--ease-glow` (on
  paper, gold-deep is the text-safe gold, §2). The piece-count
  stepper: each added shard glyph locks in with a 200ms
  `--ease-lock` miniature of §6.1. Submit: the CTA dips the whole
  vessel 1.6px (`--ease-settle`), the form's own seam (the vessel
  arrived fractured like all vessels, §6.8) completes its final
  burst if somehow unhealed, and the intake label replaces the
  form with a 450ms crossfade + the label seam drawing (600ms,
  smooth — receipts do not burst; they print).
- **States.** Rest → field states (focus inks, error rules in
  `--lacquer` with the §12 error voice beneath, in prose) →
  sending (CTA disabled, text "Sending…", 1 shard glyph rotating
  slowly — the theme's only spinner-shaped object, a shard, never
  a ring) → received (intake label). Disabled CTA at rest is
  refused: the button is always pressable; validation speaks
  (§12), it does not lock doors.
- **Content merge.** Every field is a fact the atelier needs to
  price the mend; the piece count drives the quote logic the
  studio actually uses ("gold is priced by the piece", §12). The
  form's vessel fractured and healed on entry like the page's
  other content — the ask undergoes the theme too.
- **Failure fallback.** The form is a real `<form>` posting to a
  real endpoint; no JS: it submits natively, validation is
  server-side, and the success page is the intake label as a
  document. JS failure mid-submit leaves the native path intact.
  A failed send keeps every field's content and prints the §12
  failure line above the form — words are never thrown away by a
  network.
- **Reduced-motion variant.** No dips, no shard locks, no crossfade
  (instant swap to the label). Focus inking is instant. All states
  and copy identical.
- **Performance budget & mobile variant.** Form logic ≤6KB; the
  only animation is token transitions. Mobile: single column,
  radio list rows ≥48px, the shard stepper wraps at 6 per row,
  CTA full-width at the vessel's foot.
- **Choreography timeline (v2).** Vessel heals on entry (§6.8) →
  fields rest → focus: rule inks 240ms → pieces stepped: glyph
  locks 200ms each → submit pressed → vessel dip 550ms, CTA text
  swaps at t=180 → response → crossfade 450ms → label seam draws
  600ms → label rests; §6.13's vein gains the form's branch if
  unhealed. Error path: offending rules lacquer in 240ms, error
  prose fades 300ms, focus moves to the first error.
- **State matrix (v2).** *Rest:* paper vessel, rules shard-light.
  *Hover:* CTA warms to `--lacquer-bright`; fields do not hover-
  react (paper does not notice a hand above it). *Focus:* rule
  inks gold-deep; radio rows show their seam-line (§11). *Active:*
  CTA press = the vessel dip. *Scrolled-past:* form state is
  untouched by scroll. *Disabled:* only the sending state disables
  the CTA, for the request's duration, with `aria-disabled` and
  the reason in its text. *Touch:* radio rows and stepper are
  full-width tap targets; focus inking follows tap focus.
- **Breakpoints (v2).** ≥1200px: two-column fields (name/direction
  side by side), vessel 880px. 768–1199px: single column, vessel
  full width. <768px: single column, textarea rows 5, CTA sticky
  at the vessel's foot while the form is in view (the send must
  never scroll away from a half-written story).
- **Edge cases & failure modes (v2).** *"Something else, written
  in":* selecting it opens a one-line field (height animation
  300ms) — the list admits its own incompleteness. *Piece count
  12+:* the stepper caps at "12+" and the story field's label
  gains "(twelve or more pieces — tell it fully)" — pricing
  honesty starts here. *Very long story:* the textarea grows to
  12 rows then scrolls; the ruled lines are a background that
  scrolls with the text (misaligned rules are a gate failure).
  *Double submit:* the sending state swallows repeats; the intake
  number is requested once.
- **Accessibility spec (v2).** Real labels, `aria-describedby` for
  errors, errors in prose (§12) linked to fields, focus moved to
  the first error on failed submit and to the intake label's
  heading on success. Radio list is a real `radiogroup`. Contrast:
  charcoal on paper 13.10:1; error text lacquer on paper 8.50:1;
  focus inking gold-deep is decorative reinforcement — focus is
  *also* shown by the §11 ring, never by colour alone.
- **Tokens consumed (v2).** `--paper`, `--charcoal`, `--gold-deep`,
  `--lacquer`, `--lacquer-bright`, `--shard-light`, `--ease-glow`,
  `--ease-lock`, `--ease-settle`, `--dur-ink` (240ms).

### 6.15 Shard-pass transition + skeleton (page family: loader / transition)

- **What & why.** Moving between pages in this theme: the leaving
  page cracks along its master seam and the arriving page enters
  already mending. And while a page loads, its skeleton is not grey
  bars — it is the vessel's shards, wrapped: unlabelled shard
  shapes resting on the shelf, which the real content replaces
  piece by piece. Waiting, in an atelier, is pieces on the bench.
- **Structure.** Transition: a full-viewport overlay holding the
  leaving page's master seam path (reused geometry, §4); the seam
  opens (crack widens to 6px `--crack` over 260ms), the two halves
  part by 10px, and the arriving page is revealed beneath already
  at §6.8's q=0.3 — mid-mend — completing as the visitor begins to
  scroll. Skeleton: per-section shard placeholders (the vessel's
  actual clip-pieces filled `--shard` at 60%, each with its paper
  bevel), labelled in apparatus "ON THE BENCH". Skeleton pieces are
  replaced in fracture order as content arrives.
- **Motion spec.** Transition total ≤700ms: crack open 260ms
  `--ease-draw` → part 180ms `--ease-settle` → reveal + overlay
  fade 260ms. Skeleton: pieces rest still (a wrapped shard does
  not shimmer — the theme refuses the shimmer cliché; stillness is
  the loading state), replaced with a 300ms `--ease-settle` fade
  per piece as real content lands, in rim-to-foot order.
- **States.** Idle → cracking → parting → revealed → idle.
  Skeleton: benched → replacing → content. A transition
  interrupted (back button mid-pass) resolves instantly to the
  target page at its current heal state.
- **Content merge.** The transition uses *this page's own* master
  seam — you leave through the break you arrived by. The skeleton
  is the arriving vessel's own fracture plan: the placeholder is
  the content's shape, not a generic wireframe.
- **Failure fallback.** Any fault (history API edge, missing seam
  data) → plain navigation, instantly. The transition is an
  enhancement layered on real links; it can never strand a visitor
  between pages. Skeleton timeout: 4000ms per section, after which
  whatever content exists renders and the remaining shards are
  replaced by the §12 bench note ("This piece is still being
  looked for.").
- **Reduced-motion variant.** No crack, no parting: a 160ms
  crossfade between pages; skeletons are static and replaced
  instantly.
- **Performance budget & mobile variant.** Overlay = 1 SVG path +
  transforms; skeleton pieces are CSS shapes of the clip-paths
  already authored. Mobile: the parting distance drops to 6px and
  total to 560ms; skeletons show at most 2 vessels' worth of
  shards (below-fold vessels bench lazily).
- **Choreography timeline (v2).** Link activated → 0ms overlay
  mounts (page still readable beneath) → seam cracks 0–260 →
  halves part 260–440 → new page revealed at q=0.3, overlay fades
  440–700 → control returns; the new page's heal continues under
  the visitor's own scroll. Skeleton path: bench → per-piece
  300ms replacements → vessel whole → §6.8 takes over if the
  section is in view.
- **State matrix (v2).** *Rest:* idle / content shown. *Hover:*
  links do not pre-crack on hover (a threat of breakage on hover
  is menace, not craft). *Focus:* keyboard navigation triggers
  the same pass; focus lands on the target page's heading at
  reveal. *Active:* the pass itself. *Scrolled-past:* n/a.
  *Disabled:* prefetch-disabled or Save-Data connections skip the
  pass entirely (plain navigation) — the ceremony costs bytes of
  attention the visitor asked not to spend. *Touch:* same pass,
  mobile timings.
- **Breakpoints (v2).** ≥1200px: as specified. 768–1199px: parting
  8px, total 640ms. <768px: parting 6px, total 560ms, skeleton
  cap 2 vessels.
- **Edge cases & failure modes (v2).** *Same-page anchor over 2
  sections:* §6.13's rule applies the pass; under 2 sections, a
  plain scroll (the pass is for journeys, not steps). *Slow
  target page:* the crack opens and *holds* at parted (the bench
  state) until the target's first vessel is ready, capped at
  2500ms, then reveals whatever exists. *Print/back-forward
  cache:* pages restored from bfcache skip the pass and restore
  their exact heal registry (gold is not taken back, even by the
  browser).
- **Accessibility spec (v2).** During the pass, `aria-busy` on the
  root; the pass is ≤700ms and never blocks screen-reader
  announcement of the new page's title/heading, which fires at
  reveal. Skeleton regions carry `aria-label="Loading"` once per
  page, not per shard. Focus management per the matrix.
- **Tokens consumed (v2).** `--crack`, `--shard`, `--paper`,
  `--ease-draw`, `--ease-settle`, `--dur-pass` (700ms),
  `--dur-bench` (4000ms).

### 6.16 The kiln shelf (page family: listing / detail)

- **What & why.** The gallery of finished work and pieces for sale
  or adoption: a shelf of mended vessels, each photographed as an
  object, each with its mend note and its price — where price is
  stated the atelier's way, by the work: pieces, gold, hours. A
  listing page in this theme is a shelf you walk along, and every
  object on it is whole-but-seamed.
- **Structure.** A charcoal shelf section: rows of vessel objects
  (image clipped to the vessel silhouette, §5's image rule) on
  `--shard` plinths, name in Mincho, mend note in italic (§3 law
  2), apparatus line (`4 PIECES · GOLD · 11 HOURS`), price. The
  detail view is the same vessel at hero scale (§6.1's geometry
  reused, arriving mended) with its full mend record (§6.17) and
  the commission CTA (§6.14's voice: "Commission one like it").
  Filters are seam-lines (§11): by vessel kind, by piece count.
- **Motion spec.** Shelf rows heal via §6.8 as sections (each row
  is a low vessel, fracture of 2 pieces only — a shelf row is a
  shallow bowl). Vessel images settle 1.04→1 over 700ms
  `--ease-settle` as their row heals. Hover on an object: its main
  seam takes §6.7's glow (the shelf's vessels are finished, so the
  glow is their hover language) and the object lifts 2px — no
  tilt here; shelf objects are behind glass, §6.9's handling is
  reserved for services.
- **States.** Row broken → healed (rest). Object rest → attended
  (glow + lift) → detail. Sold objects: the plinth carries a paper
  band ("GONE TO ITS HOME") and the vessel renders at 70% — sold
  is a state with dignity, not a grey-out.
- **Content merge.** Each object's seam pattern is its own real
  mend (the photograph shows the actual gold; the SVG seam overlay
  is traced from the same piece's fracture plan). The apparatus
  line is the object's true record. Nothing on the shelf is a
  stock photo of an unbroken pot.
- **Failure fallback.** No JS: shelf whole, images plain (still
  silhouette-clipped by CSS), filters become a GET form. Images
  failing to load: the vessel's SVG outline + mend note stand in
  the silhouette — the record remains when the photograph doesn't.
- **Reduced-motion variant.** Rows arrive whole; settle and lift
  removed; glow becomes §6.7's static brightening.
- **Performance budget & mobile variant.** Images ≤90KB each,
  lazy below the first row; seam overlays are the existing paths.
  Mobile: one object per row, plinth full-width, apparatus wraps
  under the note.
- **Choreography timeline (v2).** Row enters → fracture heal per
  §6.8 (2-piece, ≈700ms) → images settle staggered 90ms per object
  → row rests → hover: glow 240ms in, lift concurrent → detail
  navigation via §6.15's pass → detail vessel stands mended with
  its runner lit (§6.6).
- **State matrix (v2).** *Rest:* healed shelf. *Hover:* glow +
  2px lift. *Focus:* identical, ring on the object's link.
  *Active:* press settles the lift (0px, 120ms). *Scrolled-past:*
  healed. *Disabled:* sold objects' links disable with the paper
  band as the reason; the object still glows on hover (it can be
  admired, not bought). *Touch:* tap = detail; glow plays as a
  600ms pulse on tap-down.
- **Breakpoints (v2).** ≥1200px: 3 objects per row. 768–1199px:
  2 per row. <768px: 1 per row, image 84vw, lift cut (glow stays).
- **Edge cases & failure modes (v2).** *An object with 1 piece*
  (a crack, never separated): its seam is a hairline and the
  apparatus reads `1 CRACK · GOLD · 3 HOURS` — the vocabulary
  distinguishes cracks from pieces everywhere (§12 owns this).
  *Shelf with 40+ objects:* pagination is §11's "Older shelves"
  seam-link, never numbered pages; each shelf page heals
  independently. *Duplicate mend notes:* the gate flags them —
  two vessels with the same story is a data error, not a style.
- **Accessibility spec (v2).** Each object is a link whose name =
  vessel name + piece count ("River bowl — 4 pieces, gold").
  Images carry alt = the mend note. Filters are labelled
  controls with counts. Sold state is text, not opacity alone.
  Contrast per §2 on both grounds.
- **Tokens consumed (v2).** `--charcoal`, `--shard`, `--paper`,
  `--gold`, `--gold-bright`, `--ease-settle`, `--ease-glow`,
  `--dur-settle` (550ms).

### 6.17 The unbroken colophon (page family: footer)

- **What & why.** The footer is the one vessel on the page that
  was never broken: a calm paper band carrying the studio's
  record — the full mend record printed from every seam's
  `data-mend` note (§1 law 2), the practice piece (§6.12) cycling
  at its heart, the mini-bowl, and the margin vein arriving into
  its root knot. After a page of breakage, the footer is the
  atelier's ledger desk: everything accounted for, in writing.
- **Structure.** Paper ground. Three columns: (1) the mend record —
  a list generated from the page's seams: vessel name, break,
  pieces, state ("mended" / "your crack, kept" for §6.11); (2) the
  practice piece (§6.12) with its note; (3) the mini-bowl (a 160px
  vessel with 1 fissure, §6.3) above the ordinary footer links,
  which are set as seam-lines (§11) — charcoal hairlines that gild
  on hover. The vein's trunk (§6.13) terminates at the footer's
  top-left in a root knot: three short branch paths curling into
  the paper. A single apparatus line closes the page: `SET IN
  MINCHO & INTER · MENDED BY HAND · <year, computed>`.
- **Motion spec.** The footer does not fracture (it is the record
  of fractures; the ledger does not break). On entry: the root
  knot draws (700ms `--ease-draw`) as the vein completes, the
  record list's rows fade in staggered 60ms, the mini-bowl's
  sheen (§6.5's variant, 900ms) plays once. The practice piece
  runs its cycle (§6.12). Link hover: the seam-line gilds over
  300ms `--ease-glow` (a hairline of gold draws under the word —
  the only gold a link may earn is by being chosen).
- **States.** Rest (record printed) → knot drawing on first entry
  → resting. Scrolled-past = out of view; the practice piece
  pauses (§6.12). The record's states update live: if §6.11's
  crack is laid after the footer was rendered, its row changes to
  "your crack, kept" when next seen.
- **Content merge.** The record is *generated from the page's
  actual seams* — it cannot drift from the page it closes, and a
  seam added without a mend note appears in the record as
  "UNRECORDED — " in lacquer, which is the gate's tripwire made
  visible (§10). The footer is the theme's audit, printed.
- **Failure fallback.** No JS: the record is server-rendered from
  the same data (the build emits it statically); the knot is
  drawn; the practice piece stands whole. If generation fails,
  the footer falls back to a static colophon without the record —
  links and legal lines never depend on the record's success.
- **Reduced-motion variant.** Knot drawn, rows printed, practice
  piece static-whole, link gilding instant.
- **Performance budget & mobile variant.** The record is DOM text;
  the knot is 3 short paths. Mobile: columns stack (record,
  practice piece, links), the vein's top-seam variant (§6.13)
  terminates in a horizontal root line instead of the knot.
- **Choreography timeline (v2).** Footer top crosses 80% → root
  knot draws 0–700ms (if the vein is complete; if sections remain
  unhealed above, the knot waits — the record closes only when
  the page does) → record rows stagger 60ms → mini-bowl sheen at
  +500ms → practice piece begins its cycle at its whole-rest
  phase → footer rests.
- **State matrix (v2).** *Rest:* record printed, cycle running.
  *Hover:* link seam-lines gild; practice piece pauses (§6.12).
  *Focus:* links take the ring (gold-deep on paper); the record
  is plain text. *Active:* link press — the gild completes
  instantly (the choice is made). *Scrolled-past:* cycle pauses.
  *Disabled:* a removed section's record row is struck through in
  apparatus ("WITHDRAWN") rather than deleted — records are
  corrected, not erased. *Touch:* no hover gild; links gild on
  tap-down.
- **Breakpoints (v2).** ≥1200px: three columns as specified.
  768–1199px: two columns (record + piece; links below).
  <768px: stacked; the record collapses to vessels actually
  healed + a count of the rest ("…and 2 vessels you passed
  unmended") — the footer never lies about what the visitor did.
- **Edge cases & failure modes (v2).** *Visitor healed nothing
  (landed at the footer via anchor):* the record prints each
  vessel as "unvisited" and the knot does not draw — an empty
  record is the honest footer for an unread page. *A seam's mend
  note is empty:* the UNRECORDED tripwire (above) renders, and
  the §10 gate fails the build on sight of it. *Very long record
  (12+ vessels):* the list caps at 8 rows + "…and N more, in the
  studio book" — the footer is a summary of the record, not the
  book itself.
- **Accessibility spec (v2).** The record is a real list with a
  heading ("The mend record of this page"). Links are links with
  text names; gilding is decoration. The practice piece is
  `aria-hidden` (§6.12). Contrast: charcoal on paper 13.10:1;
  the UNRECORDED flag is lacquer on paper 8.50:1 — an audit
  warning must be readable, not tasteful.
- **Tokens consumed (v2).** `--paper`, `--charcoal`, `--gold`,
  `--gold-deep`, `--lacquer`, `--ease-draw`, `--ease-glow`,
  `--dur-branch` (700ms).

### 6.18 The broken page (page family: 404 / empty state)

- **What & why.** The 404 is built into the theme from the
  original entry: a vessel that broke beyond the shelf — "This
  piece broke. We keep the gold ready." The error page is the one
  place the theme shows a break it cannot mend for you, and turns
  it into the invitation: the gold is ready; bring us to the piece
  you meant to find.
- **Structure.** A charcoal page: one large vessel in 5 shards
  that do **not** assemble (they rest in a gentle arc, as pieces
  laid out on the bench for assessment), its seams open `--crack`.
  Headline in Mincho: "This piece broke." Standfirst in prose:
  what likely happened, in §12's error voice. Two seam-line links
  (§11): "To the shelf" (home) and "Send us the pieces" (§6.14 —
  the commission form, pre-addressed with the missing path in its
  story field: "I was looking for /the-old-address"). The margin
  vein (§6.13) renders as a single root ending mid-air — the one
  page where the vein is honestly unfinished.
- **Motion spec.** On load, the shards settle into their bench arc
  (offsets from a common centre, 800ms `--ease-settle`, stagger
  90ms) — an arrangement, not an assembly: gaps remain. One seam
  — the shortest — begins a §6.2 burst-run every 9000ms and stops
  at 34%: the gold is *ready*, visibly, perpetually almost
  offered, never completed. Hovering the commission link completes
  that seam to 100% over 600ms (choosing the mend finishes the
  gesture); leaving lets it return to 34% over 1200ms — the only
  seam on the site allowed to un-gild, because it was never a
  mend, only a readiness.
- **States.** Resting-broken (rest) → seam-offered (34% cycle) →
  seam-completed (commission link hovered/focused) → navigation.
  No healed state exists on this page.
- **Content merge.** The broken vessel is the missing page itself,
  named in the standfirst ("the page at /the-old-address"); the
  commission link carries the path into the form, so the error
  becomes a repair job with the paperwork started. The 404 is a
  funnel into the atelier's actual work.
- **Failure fallback.** No JS: shards rest in the arc (transforms
  are CSS in the static build for this page — the one page whose
  broken state is its *rest* state and needs no arming), the seam
  stands at 34% drawn, links work. The page must be a static
  document first: error pages are served when everything else has
  already gone wrong once.
- **Reduced-motion variant.** Shards rest in the arc; the seam
  stands at 34%; no cycle, no hover completion (the link's text
  carries the offer).
- **Performance budget & mobile variant.** One SVG, one seam
  animation on a 9s cycle — the cheapest page on the site, as an
  error page must be. Mobile: vessel 88vw, shards' arc compresses,
  links stack full-width.
- **Choreography timeline (v2).** Load → shards settle 0–800ms →
  first seam offer begins at 2000ms (34% in ≈500ms of bursts) →
  holds → re-offers every 9000ms → hover/focus on the commission
  link: seam completes 600ms → click: §6.15 pass to the form.
  Home link: no seam interaction (leaving is not a mend).
- **State matrix (v2).** *Rest:* broken, seam at 34% or cycling.
  *Hover:* per link, as specified (commission completes the seam;
  home does nothing — the asymmetry is the meaning). *Focus:*
  identical to hover for both links, ring per §11. *Active:*
  navigation. *Scrolled-past:* the page is one screen; n/a.
  *Disabled:* n/a. *Touch:* tap-and-hold is not required — the
  seam completes on the commission link's tap-down, before
  navigation, in the same 600ms the pass takes to open (§6.15),
  so touch visitors see the completion inside the transition.
- **Breakpoints (v2).** ≥1200px: vessel 560px, headline 44px.
  768–1199px: 480px. <768px: 88vw, headline 34px, arc compresses
  (shard gaps 60% of desktop), seam cycle 11000ms.
- **Edge cases & failure modes (v2).** *The missing path is very
  long or hostile-looking:* it is printed truncated at 48 chars
  in the standfirst (full path only inside the form field, as
  text, escaped — the 404 never renders the URL as HTML).
  *Genuinely empty search results* reuse this page's vessel at
  200px with the §12 empty voice ("Nothing on this shelf — the
  gold is ready if you bring the pieces") and no seam cycle: an
  empty shelf is not a breakage, and the theme does not perform
  damage it does not have.
- **Accessibility spec (v2).** The page is a proper error document:
  `<h1>` first, status 404, links named by destination. The
  vessel is `role="img"` labelled "A vessel in five pieces, laid
  out for assessment". The seam's offer cycle is decorative and
  pauses under reduced motion (above). Contrast: rice on charcoal
  13.10:1 throughout.
- **Tokens consumed (v2).** `--charcoal`, `--shard`, `--crack`,
  `--gold`, `--paper`, `--ease-settle`, `--ease-draw`,
  `--seam-offer` (34%), `--cycle-offer` (9000ms).

## 7. Page application map

| Page type | How the theme plays out |
|---|---|
| **Home** | The full shelf: hero bowl (§6.1), craft-steps vessel (§6.8), service cards (§6.9), ledger (§6.10), testimonial (§6.11), shelf preview (§6.16), commission form (§6.14), colophon (§6.17). The vein (§6.13) grows the whole way. This is the reference build every other page is audited against. |
| **Listing (the shelf)** | §6.16 at full length: filter seam-lines, rows healing as shallow vessels, sold bands. The hero is a single mended vessel with the shelf's name — no fracture ceremony; a working shelf does not perform for browsers. |
| **Detail (one vessel)** | §6.1's geometry at reading scale, arriving mended; the full mend record for that piece; its seams take §6.7's glow and §6.6's runner; the commission CTA is "Commission one like it" into §6.14 with the piece named. The fracture plan of the photographed piece is traced, not invented (§6.16). |
| **About (the atelier)** | The studio's own story told as vessels: the founder's first broken bowl is the hero (a real object, with its real mend note); the timeline is a vein (§6.13's geometry laid horizontally) whose branches are years; team portraits are refused — hands and vessels only, this theme does not put faces in bowls. |
| **Contact / commission** | §6.14 is the page; the hero vessel is an *unmended* bowl whose pieces settle (§6.9's awaiting state at hero scale) as the visitor writes — the form's completion is the visitor's own mend rehearsed. Success = the intake label. |
| **404** | §6.18, verbatim. Never a generic error template in this theme. |
| **Print** | Every page prints healed: vessels whole, seams gold, the record (§6.17) appended. A printed fracture is a lie about a finished object. |

## 8. Worked examples

### 8.1 The hero — the bowl that was dropped in March

The atelier's home hero, end to end. **Content:** the showcase
bowl (a real piece: celadon, dropped from the studio shelf in
March 2023, four pieces, gold), headline "Mended, not replaced.",
standfirst "We repair ceramics the slow way — lacquer, gold, and
time — and we sign every seam.", CTA "Send us your broken thing"
(§6.14). **Build order inside the hero:** bowl SVG with its
authored fracture plan (master crack across the belly, two
branches; 7 fissures at rim, handle-side stress point and foot);
headline letters as spans over the belly band, offset along the
master crack vector; mend note as the figure caption.
**Scroll/timing timeline:** t=0 fonts race → shards lock largest-
first (§6.1: complete by 1060ms, settle dip to 1610ms) → seams
burst-run (§6.2: hero seams done ≈1900ms) with fissures sprouting
at their anchors and dust shedding at each front (§§6.3–6.4) →
sheen sweep at ≈2000ms (§6.5) → letters click into alignment as
the belly seam passes them (last letter at ≈1850ms) → CTA fades
at the dip's bottom → runners arm at +800ms after cure (§6.6) →
the vein draws its first branch (§6.13). **What the visitor
feels:** something precious was broken here, and these people
put it back together while I watched — carefully, and in no
hurry. **Failure rehearsal:** with JS off, the same screen stands
mended and readable; with the loop killed, watchdogs deliver the
same end state by 4000ms.

### 8.2 Mid-page — the testimonial across the seam

**Content:** a client's story in two voices — the break ("It
slipped on the stairs and I heard it go before I saw it.") and
the return ("It came back heavier. The gold holds the light at
breakfast.") — set as one quote in a paper vessel (§6.11), the
seam crossing the paragraph gap between the voices and one
word-space inside the break sentence. **Build:** the quote's DOM
text is continuous; the seam is an SVG overlay in the vessel's
box; the visitor-crack path is authored along the lower third;
the invitation button sits at the foot. **Scroll timeline:**
the vessel enters fractured (§6.8: two pieces, split exactly at
the seam) → pin engages → q scrubs: pieces converge, the seam
burst-runs as they meet — the gold literally joins the two
halves of the story as the visitor reads down → q=1 lock + dip →
the invitation fades in (it is not shown while the vessel is
still mending; you cannot be invited to break a thing that is
not yet whole) → click: the visitor's lacquer crack draws in
620ms from the click point (§6.11) → the record (§6.17) will
show this vessel as "your crack, kept". **What the visitor
feels:** the story's two halves were apart, and are not; and
their own mark is allowed to stay.

### 8.3 Conversion — sending a piece in

**Content:** §6.14's form, reached from the hero CTA. **Build:**
paper vessel, radio list of vessel kinds, shard-glyph stepper,
ruled textarea, lacquer CTA; the intake-label template with the
mend number sequence continuing from the ledger's count (the
form's first issued number must be 215 if the ledger says 214 —
the gate checks the arithmetic, §10). **Scroll/interaction
timeline:** the form vessel heals on entry (§6.8) → visitor
focuses "What broke": rule inks gold-deep 240ms → selects "a
bowl" (seam-line inks) → steps pieces to 4 (four shard glyphs
lock, 200ms each) → writes the story (the ruled lines scroll
with the text) → presses send: vessel dips, CTA reads "Sending…"
with its turning shard → intake label crossfades in, its seam
draws smooth in 600ms: `RECEIVED · MEND Nº 215 · 4 PIECES ·
GOLD` → prose beneath: "Keep the pieces wrapped and dry. We
write within two working days — lacquer keeps its own calendar,
but letters keep ours." **Error rehearsal:** submit with the
direction malformed: the rule lacquers, §12's error prints —
"The direction will not carry — check the address, and we will
carry the rest." — and every written word is still there.

## 9. Anti-slop — what makes THIS theme look cheap

1. **Smooth seam draws.** A seam that draws like a loading bar
   kills the theme in one gesture. Cure: §6.2's burst-and-breathe
   engine, seeded, always; the gate scrubs a seam at 0.25× speed
   and listens for the rhythm.
2. **Gold as accent.** Gold headings, gold bullets, a gold
   "premium" badge — the law (§1) broken. Cure: gold exists only
   as seams, the vein, and glow inside cracks; the gate weighs
   gold pixels (§2's 1.5% rule).
3. **Random cracks.** Procedurally generated fracture noise looks
   like a screen-crack phone prank. Cure: fracture plans are
   authored per vessel (§4), routed through content boundaries,
   never through glyphs; ≤4 pieces per vessel.
4. **Bounce.** Any elastic overshoot beyond §6.1's single 1.5%
   lock click — ceramic does not bounce. Cure: the five easings
   are the only curves; `--ease-lock`'s overshoot is capped and
   singular per lock.
5. **Re-breaking on scroll-up.** A page that shatters again when
   you scroll back reads as a toy, and breaks the law. Cure: heal
   state is a one-way registry (§6.13 consumes it); the gate
   scrolls the full page up and down twice and diffs the states.
6. **Dust everywhere.** Gold particles as ambient page glitter.
   Cure: §6.4 emits only from a live front, only during bursts;
   a cured page has zero particles, and the gate counts them.
7. **The crack through the words.** A seam crossing glyphs is
   illegible and smug. Cure: §4/§6.8 routing rule + the gate's
   bounding-box check (§6.3).
8. **Fake mend notes.** "Broken with love in 2024" on a stock
   bowl. Cure: every note names a break the client can document;
   the record (§6.17) prints UNRECORDED in lacquer when a note is
   missing — the theme shames its own gaps in public.
9. **A shimmering skeleton.** Grey shimmer bars are another
   theme's waiting room. Cure: §6.15's still, wrapped shards.
10. **The testimonial crack that gilds itself.** If the visitor's
    crack politely turns gold, the participation was fake. Cure:
    §6.11 — lacquer-red, open, kept; the one unrepaired thing on
    the page.
11. **Percentages and progress bars.** "87% mended" is a bar's
    language in a kiln. Cure: §12 bans them; progress is the vein
    and the counts.
12. **Faces in bowls, stock serenity.** Spa photography and
    wabi-sabi mood-board imagery. Cure: §7's about-page rule —
    hands and vessels only, and every vessel a real, noted piece.

## 10. Quality gate

Blocking unless marked otherwise. A build that fails any blocking
item does not ship in this theme.

1. **Law audit.** Every gold element on the page traces to a
   break in a real content object; every seam carries a non-empty
   `data-mend` note; the footer's record (§6.17) shows no
   UNRECORDED row.
2. **Gold weight.** Gold pixels at rest ≤1.5% of the viewport at
   five sampled scroll positions (vein excluded).
3. **Fissure count.** Exactly 15 fissures: 7 hero, 2+2+1 cards,
   2 footer, 1 mini-bowl — counted in the DOM.
4. **Burst rhythm.** Three sampled seams show burst sizes within
   5–13% and breaths within 50–180ms at 0.25× playback; no seam
   draws smoothly.
5. **Forced-heal timings.** Hero complete ≤1200ms (final ≤4000ms);
   every section healed ≤7000ms after entry with the loop
   disabled; JS-off render is fully whole and readable.
6. **One-way registry.** Full scroll down, up, down: heal states,
   ledger figures and vein length never decrease.
7. **Runner physics.** Every runner's duration = measured length
   ÷ 90px/s (±5%); ≤2 runners lit simultaneously; hero title seam
   = 7s.
8. **Ledger arithmetic.** The form's first intake number = the
   ledger's pieces figure + 1; all figures DOM-derived (§6.10).
9. **Crack routing.** No seam or fissure path's bounding box
   intersects a text glyph box in the reference build (§6.3).
10. **Reduced motion.** With `prefers-reduced-motion`, the page
    arrives whole: no fracture, no runners, no dust, no cycle —
    and every mend note still present.
11. **Contrast.** §2's measured pairings verified in both colour
    schemes; no gold text under 18px anywhere; lacquer never sits
    on charcoal without its keyline.
12. **Visitor crack.** §6.11's crack persists across in-session
    navigation, never gilds, and disables its invitation after
    one use. (Non-blocking: the 404's seam returns to 34% on
    leave — checked, but a stuck-at-100% offer seam is a blemish,
    not a lie.)

## 11. Component inventory

Every component a real Kintsugi site needs, with its themed
treatment. Components the theme refuses are listed with their
in-vessel replacement — a refusal without a replacement is a gap,
not a stance.

| Component | Themed treatment |
|---|---|
| Primary button | The lacquer block: `--lacquer` ground, rice label, 1px rice keyline when on charcoal (§2); presses with the 1.6px vessel dip (`--ease-settle`, 180ms). Reserved for the commission action and its kin — one per vessel at most. |
| Secondary button | Seam-line button: transparent, charcoal hairline beneath the label that gilds on hover/focus (§6.17's link behaviour). On charcoal, the hairline is `--shard-light` and the gild is `--gold`. |
| Text input | Ruled line (§6.14): apparatus label above, 1px rule below, no box; focus inks the rule `--gold-deep` on paper. |
| Textarea | Ruled sheet (§6.14): lines every 29px scrolling with the text. |
| Select | Refused. A dropdown is a cupboard door; choices in an atelier are laid out: a ruled radio list (§6.14), the chosen line's rule inked gold-deep with a seam tick. |
| Checkbox | Shard box: an unfilled square shard outline; checked = the shard fills gold — a checkbox in this theme is a tiny piece, seated. |
| Radio | Seam line: the chosen option's rule inks gold-deep and gains a 6px gold seam segment at its left end. |
| Toggle / switch | Refused. Vessels are whole or broken; they do not toggle. Paired states are two seam lines as radios. |
| Card | Vessel card (§6.9) for services; shelf object (§6.16) for pieces. No other card exists. |
| Table | The mend record (§6.17): real table on paper, apparatus headers, rows ruled with hairlines — a table in this theme is a page of the studio book, its row rules the only hairlines allowed besides seams. |
| Tabs | Refused. A vessel has an inside and an outside, not tabs; collections are shelves (§6.16) walked by scrolling or the vein (§6.13). |
| Accordion | The opening shard: a section whose lower piece slides down 300ms `--ease-settle` along its seam, the seam gilding as it opens — an accordion here is a vessel being opened along its mend. |
| Modal / dialog | The bench sheet: a paper sheet (§6.13's mobile nav, confirmations) that settles onto the page with the 1.6px dip; its top edge is a drawn seam. One at a time; Esc lifts it. |
| Toast | Refused. News in an atelier is written down: transient confirmations become a one-line entry in the nearest vessel's mend-note position, in apparatus, and stay until the page changes. |
| Tooltip | Refused. Explanation lives in mend notes and captions; an object that needs a tooltip needs a better note. (The practice piece's note, §6.12, is always-visible text, not a tooltip.) |
| Badge | The paper band: a small rice-paper strip across a vessel's plinth ("GONE TO ITS HOME", §6.16) or bound around a wrapped vessel (§6.9's disabled state). Badges state facts about objects, never marketing ("NEW" is banned, §12). |
| Alert | The lacquer rule: a band in the current vessel, lacquer hairline above, message in §12's error voice, persistent until resolved. |
| Pagination | "Older shelves" / "Newer shelves" seam-links (§6.16) — a shelf is walked, not numbered. |
| Progress bar | Refused. Progress is the vein (§6.13) and the ledger's counts (§6.10). |
| Spinner | Refused, with one licensed exception: §6.14's sending shard, a single shard glyph turning slowly — a piece being examined, not a ring being waited on. Waiting elsewhere is the bench (§6.15). |
| Skeleton | Wrapped shards on the bench (§6.15). |
| Search | The bench search: one ruled line in the shelf header; results are shelf objects (§6.16) grouped by vessel kind, each with its mend note — search results in this theme are objects, not links. |
| Breadcrumbs | Replaced by the vein (§6.13): where you are is how much has mended, plus the current vessel's apparatus name in the header. |
| Skip link | "Skip to the first vessel" — a plain rice link on charcoal appearing on first focus. |
| Focus ring | 2px `--gold` outline offset 3px on charcoal (7.54:1); 2px `--gold-deep` on paper, always paired with the element's own state change (inking, gilding) — never colour alone. |
| Divider | A vessel's foot seam (§4). Hairlines exist only inside tables and forms. Wavy or dotted dividers are refused — the theme has one line language: the crack. |

## 12. Content & copywriting voice

Two voices, like the type. **The Mender** writes prose: standfirsts,
stories, errors, confirmations — Inter, sentence case, unhurried,
the voice of someone whose hands are busy and whose words are few
and exact. **The Label** writes apparatus: mend notes, counts,
prices-by-the-piece — uppercase, tracked, every figure sourced.
The voices never swap: apparatus never sentences, prose never
shouts.

**Headline style.** Short statements of fact about breakage and
repair. ✓ "Mended, not replaced." / "Four pieces. Gold. Signed."
✗ "We turn your broken dreams into golden masterpieces!" —
exclamation, metaphor inflation, and a promise no atelier can
sign. Exclamation marks are banned theme-wide; lacquer does not
shout either.

**Label style.** Object + break + material. ✓ "RIVER BOWL — 4
PIECES · GOLD", "MEND Nº 215 · RECEIVED". ✗ "Item #215 (Premium
Service)" — "premium" is banned; the gold is the premium, and it
is never an adjective.

**Mend-note style** (the theme's signature sentence). ✓ "Dropped
from the studio shelf, March 2023. Four pieces. Gold." ✓ "A crack,
never separated. Her grandmother's, then hers." ✗ "Beautifully
restored to its former glory!" — nothing here returns to former
glory; it goes forward, seamed.

**Error voice.** A fact, the consequence, the way back — in the
Mender's prose. ✓ "The direction will not carry — check the
address, and we will carry the rest." ✓ "This piece is still
being looked for." ✗ "Oops! Something went wrong 😞" — the
atelier has no "oops", and no emoji survives the kiln.

**Empty-state voice.** ✓ "Nothing on this shelf — the gold is
ready if you bring the pieces." ✓ "This piece broke. We keep the
gold ready." (§6.18, verbatim). ✗ "No results found. Try again?"
— the shelf does not blame the visitor for its emptiness.

**Confirmation voice.** ✓ the intake label (§6.14): "RECEIVED ·
MEND Nº 215 · 4 PIECES · GOLD", then prose: "Keep the pieces
wrapped and dry. We write within two working days." ✗ "Success!
🎉 Your submission has been received!" — a confirmation is a
receipt, not a celebration.

**Pricing voice.** By the work, never by the tier. ✓ "from £180 —
4 pieces, gold, eleven hours at the bench". ✗ "Gold Package —
£180" (there are no packages; there are pieces). Piece counts
distinguish **pieces** (separated) from **cracks** (never
separated) everywhere, including prices (§6.16's rule).

**Banned words:** premium, seamless (the theme is *seamed* — the
ban is doctrinal), flawless, brand-new, revolutionary, oops,
unlock, elevate, masterpiece (except in a client's own quoted
words), percentages for progress, "just" in instructions.
**Owned words:** mended, seam, piece, crack (as the noun of fact),
gold (as material, never adjective), bench, shelf, kept, signed,
wrapped, received.

**Fixed strings (verbatim, do not paraphrase):** the 404 heading —
"This piece broke."; its standfirst close — "We keep the gold
ready."; the testimonial invitation — "Touch the story — leave
your own crack." and its spent state — "Your crack, kept."; the
practice piece's note — "The practice piece. It breaks so the
others don't have to."; the form's failure head — "Not sent —
the lacquer refused. Your words are kept above."

## 13. Full-page scroll choreography map

The home page, top to bottom. Every beat in order; instruments run
continuously beneath the beats (the shared loop; the vein §6.13
growing; runners §6.6 on cured seams).

| Beat | Scroll zone | What happens | What the visitor feels |
|---|---|---|---|
| 1 | Load | Hero bowl mends (§6.1); seams burst (§6.2); sheen (§6.5) | The craft, witnessed |
| 2 | Hero in view | Runners arm; vein draws branch 1 (§6.13) | The record opens |
| 3 | Craft vessel enters | Fracture→heal (§6.8): the steps converge, step-seams gild | Method, mended |
| 4 | Cards shelf enters | Shimmer gilds (§6.9); vessels await handling | A shelf of promises |
| 5 | First card handled | Settle + gild + tilt (§6.9) | The rehearsal of a commission |
| 6 | Ledger enters | Dividers burst; figures count (§6.10) | The book, kept honestly |
| 7 | Testimonial centres | Two voices join across the seam (§6.11/§8.2) | A story made whole |
| 8 | Visitor clicks | Their crack draws, lacquer, kept (§6.11) | A mark of their own |
| 9 | Shelf preview | Rows heal shallow (§6.16); objects settle | Finished work, resting |
| 10 | Form vessel | Heals on entry (§6.14); fields rest on paper | The ask, on the lit desk |
| 11 | Form sent | Dip; intake label prints its seam (§6.14) | A receipt with a number |
| 12 | Footer enters | Root knot draws; record prints (§6.17); practice piece cycles (§6.12) | Everything accounted for |

**Reverse pass.** Scrolling up: nothing re-breaks, nothing
un-counts, the vein does not shrink (the law, §1). Runners keep
their schedule; card vessels stay mended; the testimonial keeps
the visitor's crack. The only upward change is attention: §6.7's
glow works on every healed seam in both directions.

**Jump-scroll catch-up.** Anchor jumps, flings, and find-in-page:
every vessel passed heals instantly in entry order (stagger 60ms,
so the eye catches a rapid ripple of gold, not a pop), the ledger
stands counted, the vein draws continuously to the furthest
healed node with `--crack` pending segments for gaps (§6.13), and
the target vessel heals by the focus rule (§6.8). No ceremony is
owed to a teleport — but no vessel is left broken by one either.

## 14. Whole-page performance budget

| Budget | Limit |
|---|---|
| Total page weight (home) | ≤ 640KB, of which images ≤ 360KB |
| Fonts | Zen Old Mincho (1 weight) + Inter (3 weights) + Noto Sans JP (subset, terms only) ≤ 130KB, `font-display: swap` |
| JS | ≤ 55KB gzipped (one shared loop, burst engine, heal registry, glow, form) |
| SVG | All vessels inline or sprite ≤ 60KB total; fracture plans are data, not duplicate artwork |
| Shared-loop cost | ≤ 1.5ms/frame average; writes only transform / opacity / dashoffset / custom properties |
| Long tasks | None > 50ms after load; shard locks are staggered, never batched |
| Heal latency | Any entered section healed ≤ 1000ms after its pin completes, or force-healed by §6.8's watchdogs |
| Concurrent animation | ≤ 3 seams bursting, ≤ 2 runners lit, ≤ 5 dust canvases live — enforced by the schedulers, not by hope |

**Cut order when the budget is exceeded** (cut in this order,
record each cut in the build notes):

1. Gold dust (§6.4) — gone entirely; wet seams read by their
   brighter gold alone.
2. Runner acceleration on hover (§6.6) — runners keep base speed.
3. Shard parallax drift (§5) — pieces converge without the
   0.94/1.06 spread.
4. The shard pass (§6.15) — navigation becomes a 160ms crossfade.
5. Card tilt (§6.9) — cards settle and gild without tipping.
6. The sheen's re-trigger (§6.5) — the completion sweep stays;
   the returning-hand sweep goes.

**Never cut:** the burst engine (§6.2 — it *is* the theme), the
forced-heal watchdogs, the vein, the mend record, the form's
error-keeping, any reduced-motion variant. A build that cuts the
honesty to keep the sparkle has inverted the theme.

## 15. Build-order checklist

1. Gather the real breakage: the vessels, their photographs, and
   a documented mend note for every seam that will exist. No
   notes, no build — the law (§1) is a content dependency.
2. Author the fracture plans (§4): per vessel, the master crack
   through its content boundary, branches at 30–60°, ≤4 pieces,
   fissure anchors on real stress points. One geometry source per
   vessel, consumed by §§6.2, 6.3, 6.6, 6.7.
3. Build the static shelf: all vessels whole and gold, all
   content readable, form posting, record printed — with no JS.
   This is the site; the rest is the breaking of it.
4. Set the palette tokens and pairing law (§2); audit contrast on
   both grounds and in the dark-scheme ruling before any motion.
5. Set the type scale and the §3 laws (no gold body text; italics
   are mend notes only).
6. Build the shared loop (lerp 0.12) and the heal registry;
   verify the registry's one-way property in isolation.
7. Arm the hero (§6.1) with its 1200/4000ms watchdogs; test with
   the loop killed.
8. Implement the burst engine (§6.2) with the seeded RNG; verify
   burst/breath ranges at 0.25× speed against §10 item 4.
9. Add fissures (§6.3) and dust (§6.4) as pure functions of the
   front position; verify the 15-count in the DOM.
10. Add fracture→heal (§6.8) with pin, scrub, focus fast-forward
    and the 6000/7000ms force-heals; rehearse jump-scroll
    catch-up (§13).
11. Add the instruments: vein (§6.13) from the registry, ledger
    (§6.10) from real figures, record (§6.17) generated from
    `data-mend` attributes; check the §10 arithmetic item.
12. Add the attentions: runners (§6.6) with measured durations,
    glow (§6.7) with its hero gate, sheen (§6.5), card handling
    (§6.9).
13. Add the participations: testimonial crack (§6.11) with
    session persistence; footer cycle (§6.12); 404 (§6.18).
14. Wire transitions and skeletons (§6.15); rehearse bfcache
    restore and Save-Data behaviour.
15. Run the §10 gate end to end, including the scroll-up/down
    state diff and the reduced-motion pass, with the gate signed
    by someone who did not build the page.
