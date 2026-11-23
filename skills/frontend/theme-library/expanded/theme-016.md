# 16. Vellum & Wax — Expanded (v1 + v2)

The site is a bundle of sealed letters tied with a silk ribbon, and reading
it is opening it: wax seals crack, folds unfold, signatures warm into the
page last, the way they were written last. The first letter opens with full
ceremony; every letter after it opens with the same ritual, abbreviated —
because ceremony, once established, becomes manners. This document is the
complete build specification. Where it disagrees with the short library
entry, this document is the build target.

---

## 1. Concept & world

**The story.** Before email, important words travelled folded, sealed, and
tied. A bundle of letters was an object with a front (the address panel), a
fastening (the ribbon), and a lock (the wax). Vellum & Wax rebuilds the web
page as that object. The page's navigation is the address panel on the
bundle's face. The scroll progress is the ribbon itself, unwinding down the
margin as the bundle is read, its loose end curling further the deeper you
go. Every section is a letter: dated, postmarked from a town that matters
to its story, written on laid paper whose chain lines you can see, and
gated by a wax seal bearing a monogram that draws itself as the letter is
presented. The hero — the first letter — is opened in full ceremony: the
seal cracks into two halves with a scatter of wax shards, and the sheet
unfolds in two panel turns to reveal the hero text, which was there all
along, fully written, merely folded. Later letters fold down in a single
panel turn. Postscripts and signatures arrive after the body, warming from
pale brown to full ink as they land, because in a real letter they were
written last and in a different moment of the writer's attention.

**The mood.** Unhurried, tactile, faintly candlelit. Nothing on the page
hurries and nothing sparkles; the most extravagant event is a seal cracking,
and it happens once. Warmth is the theme's emotional currency: light breathes
over the paper, handwriting darkens where the reader's attention lingers,
signatures warm as they arrive. The emotional arc of a page is fixed:
*sealed → entrusted → opened → read → signed.* A visitor should feel that
the words were meant for someone — and that the someone, for the length of
the page, is them.

**Best-fit sites and audiences.**
- Wedding and event invitations: the invitation letter is the hero, the
  details are the following letters, the RSVP is the reply form (§6.16) —
  the ceremony of opening *is* the product.
- Luxury gifting and concierge brands: a gift announcement, a provenance
  letter, a founder's note — correspondence where the seal carries the
  brand's monogram and the unboxing begins on the page.
- Personal-brand storytellers, memoirists, and letter-form newsletters:
  essays published as dated letters, each postmarked from where it was
  written, signed in a hand.
- Heritage and craft brands (paper, ink, perfume, tailoring) whose product
  already ships folded, wrapped, and sealed.
- Anniversary, memorial, and family-history pages: a small bundle of real
  letters, each with its true date and town, presented in order.

**When NOT to use it.**
- When there are no letters. The theme's authority comes from genuine
  dated correspondence: a real writer, a real date, a real town in every
  postmark. A SaaS feature list dressed as "letters" with invented dates
  is a costume, and §9 names it as the first slop mode. If the content is
  not epistolary — no sender, no recipient, no occasion — refuse the theme.
- For anything urgent or transactional at scale: checkout, banking,
  dashboards, search results. The ceremony costs the visitor about two
  seconds once; a page that must be scanned in five seconds, fifty times a
  day, cannot pay it. The reply form (§6.16) is the only transactional
  surface the theme permits, and it is a single letter back, not a flow.
- For content that must be corrected or updated silently. A letter cannot
  be edited after it is sealed; pages in this theme carry their dates
  permanently. Fast-changing data (prices, stock, schedules) belongs in
  the postmark line only if it is genuinely re-issued as a new letter.
- For audiences who must not be slowed: the first-opening ceremony is
  skippable in one gesture and never gates content (§6.1), but if even a
  skippable ritual is wrong for the audience, use another theme.

**The one law.** *Every letter is real, dated, and sealed exactly once.*
Each letter on the page carries a true date and a postmark town that
belongs to its story; each seal cracks at most once per page view and is
never re-cracked as a loop or a lure; and the text of every letter is fully
written and readable before any fold moves — the fold is presentation,
never a container that content depends on. A postmark invented for
decoration, or a seal that re-seals itself to beg a second click, breaks
the theme's contract (§10, blocking gates 1 and 4).

---

## 2. Palette

Four anchors from the library entry, unchanged. Everything else is a
derived tone with a named job; no other colour may appear. Wax red is the
theme's ceremony colour and is rationed like it: seals, the crack, the
press, and nothing else — a page where wax red is used for links or badges
has spent its ceremony on furniture (§9).

| Token | Hex | Role | Usage ratio | Pairing & contrast |
|---|---|---|---|---|
| `--paper` | `#F1EAD8` | Laid paper — every letter sheet, the page ground of the bundle itself | ~62% of pixels | Ground for `--ink` (11.17:1), `--wax` (8.32:1), `--ribbon` (8.50:1) |
| `--ink` | `#3B2C20` | Ink brown — letter text, headings, all reading matter | ~18% | On `--paper` 11.17:1 (AAA at all sizes); on `--paper-deep` 9.39:1 |
| `--wax` | `#7E1F1F` | Sealing-wax red — seals, crack shards, the press, the one CTA's seal-button | ~3% | On `--paper` 8.32:1; `--paper` text on `--wax` 8.32:1 — the seal-button's label is lawful |
| `--ribbon` | `#2F4356` | Ribbon blue — the margin ribbon, address panel rules, postmarks, links | ~9% | On `--paper` 8.50:1; `--paper` on `--ribbon` 8.50:1 (address panel text) |
| `--paper-deep` | `#E3D7BC` | Shadowed laid paper — folded-under panels, the envelope front at rest, skeleton sheets | ~6% | `--ink` on it 9.39:1; `--wax` on it 7.00:1 |
| `--paper-edge` | `#D8C9A3` | The deckle and the sheet edge — 1px sheet borders, fold creases at rest | <1% | Decorative only; never carries text or a state |
| `--ink-pale` | `#8A7460` | Unwarmed ink — signatures and postscripts in their first 200ms, the writer's pencil-light hand | <1% | On `--paper` 3.69:1 — **transient only**: a signature may pass through it but may never rest in it (§6.4) |
| `--wax-bright` | `#A83A32` | The seal's lit face — the specular highlight's core, the press flare | <1% | On `--paper` 5.28:1; decorative, inside the seal only |
| `--wax-deep` | `#5C1414` | The seal's shadowed face — crack faces, the underside of the two halves | <1% | Inside the seal only; the crack reads by this against `--wax` |
| `--ribbon-faded` | `#7C8B99` | The ribbon at distance — the unwound tail's far curl, postmark ink at 60% | <1% | On `--paper` 2.91:1 — graphic only, never text; postmark *text* is always full `--ribbon` |
| `--candle` | `#F7C873` | Candle-warm light — the breathing radial (§6.6), the hover warmth's tint | overlay only | Never a fill behind text; applied as a gradient at ≤8% opacity over `--paper` |

**Dark-mode behaviour — the candlelit desk.** Dark mode does not invert
the letters: a letter is a physical sheet and stays `--paper` with `--ink`
text, exactly as a sheet of laid paper stays pale on a dark desk at night.
What darkens is everything that is *not* paper: the desk around the bundle
becomes `--desk` `#241A12`, the address panel deepens to a leather-toned
`#2C2015` with `--paper` text (14.21:1), and the breathing light (§6.6)
strengthens — its gradient opacity range rises from ±3% to ±5% and the
dust motes (§6.6) become visible a stop longer, because at night the
candle is the light source, not an ambience. Seals, ribbon, and postmarks
keep their hexes; wax on the dark desk is lit by `--wax-bright` at the
same specular angle. A build that inverts the letter sheets to dark paper
with pale ink has made a different theme and fails §10.

**Chain lines.** The laid paper's chain lines are not a colour but a
texture: vertical lines every 26px at `rgba(59,44,32,0.045)` and horizontal
laid lines every 4px at `rgba(59,44,32,0.028)`, drawn as a repeating
gradient layer *beneath* every sheet (§4). They are part of `--paper`'s
definition — flat `#F1EAD8` without chain lines is card stock, not laid
paper, and fails the gate.

---

## 3. Typography

Two voices and one clerk. The letter voice writes everything the visitor
came to read; the hand signs it; the clerk (mono) stamps dates and towns
and never writes a sentence.

| Role | Face | Size / line-height | Tracking | Rules |
|---|---|---|---|---|
| Letter display (hero salutation & first line) | Cormorant Garamond 500 | 54px / 1.08 (≥1200px); 42px (768–1199); 34px (<768) | −0.01em | The opening line of the first letter only; set as the letter's own first line, never as a marketing headline above the envelope |
| Letter headings (a letter's internal heads) | Cormorant Garamond 600 | 30px / 1.15 | 0 | Rare — most letters have none; a head inside a letter is a paragraph break with a dateline, not a section banner |
| Letter body | Cormorant Garamond 500 | 21px / 1.58 | 0 | The reading size; measure 34–44ch (§4). Never below 19px at any breakpoint — letters are not shrunk, they are re-folded (§4) |
| Letter body, long letters | Cormorant Garamond 500 | 20px / 1.62 | 0 | Letters over ~900 words drop 1px and gain leading; the fold count rises instead (§6.2) |
| The hand (signatures, postscripts, marginal warmth) | Nanum Pen Script 400 | 30px / 1.2 signatures; 26px postscripts | 0 | Only words the writer "wrote by hand": signatures, postscripts, the date in the letter's own hand when present. Never body text, never UI labels, never more than ~14 words in a row |
| The clerk (postmarks, dates, bundle counts) | Courier Prime 400/700 | 12px / 1.4, uppercase | 0.14em | Postmark towns and dates, "LETTER Nº 3 OF 7", the ribbon's depth marks. The clerk stamps; he does not persuade — no calls to action in mono |
| Address panel (navigation) | Cormorant Garamond 600 | 15px / 1.3, small caps effect via tracking | 0.08em | The bundle's address is set like an address: name, then the letters' titles as the "street lines" (§6.13) |
| Form labels & inputs (§6.16) | Cormorant Garamond 500 / the hand for the reply body | labels 15px; the visitor's reply is typed in 21px Cormorant, their signature in Nanum Pen 30px | 0 | The visitor writes a letter back; the form is a sheet, not a panel of boxes (§6.16) |

**Type laws.**
- **The hand never sets a sentence of body copy.** Nanum Pen Script is a
  signature, not a font choice; the moment it sets a paragraph it becomes
  a costume (§9). Its ration is enforced in §10.
- **Every letter is dated in the clerk's hand, in the same position:**
  top-right of the sheet, town above date, both in `--ribbon` at full
  strength (postmark *rings* may be `--ribbon-faded`; postmark *text*
  never is — 2.91:1 is a graphic, not a stamp).
- **Cormorant's light weights are forbidden below 21px.** Cormorant
  Garamond 500 at 21px/1.58 is the floor of the reading experience; the
  theme has no small print. Legal lines and the colophon (§6.17) are set
  at 15px in the address-panel voice, which is the theme's only concession,
  and they are not letter text.
- **Signatures are names, not logos.** A signature is the writer's name in
  Nanum Pen at 30px, rotated −2° to −4°, placed on the letter's baseline
  grid — never extracted, enlarged, or reused as a brand mark elsewhere
  on the page.

---

## 4. Layout language

**The bundle is the grid.** The page is one bundle lying on a desk, read
top to bottom. Its anatomy, in order: the address panel (the bundle's
face, §6.13) at the top; then the letters, stacked in bundle order, each a
sheet; the ribbon runs down the left margin for the bundle's whole length,
tied at the top, unwinding as you read (§6.3); the bundle ends with the
ribbon knot and the colophon (§6.17). There is no sidebar of widgets, no
card grid, no footer of link columns — a bundle has none of those things.

**Geometry (≥1200px).**
- Page column: max 1080px, centred on the desk. Within it, a margin track
  of 176px on the left carries the ribbon (a 26px silk strip centred in
  the track) and, pinned, the address panel (§6.9); the letter track takes
  the remaining ~840px.
- A letter sheet: padding 64px top, 56px sides, 72px bottom; measure
  34–44ch of 21px Cormorant lands at ~600px of text inside the sheet, the
  rest is the sheet's own margin — letters have wide margins; that width
  is where the warmth hover (§6.7) lives and where a reader's eye rests.
- Sheet separation: 96px of desk between letters, so each letter is an
  object, not a section. The ribbon-line join (§6.10) crosses that gap.
- Fold geometry: every sheet is composed of horizontal panels of
  ~340–420px (the fold lines fall at paragraph boundaries, §6.2). The
  hero letter has two folds (three panels); later letters one fold (two
  panels) unless the letter exceeds ~900 words, when it takes two folds
  and the long-letter type (§3).

**Spacing rhythm.** The unit is the line: 33px (21px × 1.58 ≈ 33.2,
rounded to the sheet's own grid). Vertical spacing inside a letter is in
whole lines — paragraphs separate by exactly one blank line (33px), the
dateline sits two lines above the salutation, the signature three lines
below the last body line, the postscript two lines below the signature.
Between letters, the 96px desk gap is not a multiple of the line and is
not meant to be: it is a different material (desk, not paper).

**Density rules.** One letter per viewport, roughly: a sheet plus its gap
should fill 90–110vh at 1200×800, so reading a letter is an act with a
beginning and an end, and the next letter's seal is just visible at the
fold line — an invitation, not a feed. The theme forbids the infinite
bundle: a page holds 3–9 letters. More correspondence than that is an
archive and gets a directory page (§7), each bundle still 3–9.

**Whitespace as material.** The desk around the bundle is the theme's
whitespace, and it is *warm* emptiness — the breathing light (§6.6) falls
there, and nothing is ever placed in it: no floating badges, no sticky
CTAs, no chat bubble. The only objects on the desk are the bundle and its
shadow: a soft, low shadow under the whole bundle (`0 24px 60px
rgba(36,26,18,0.18)` light mode), which is the page's single depth cue
besides the folds themselves.

**Fold lines.** A fold is drawn as a 1px `--paper-edge` line with a 6px
soft shadow below it (`rgba(59,44,32,0.10)`) when the letter is closed,
and the shadow deepens to 10px during the unfold (§6.1/§6.2) as the panel
lifts. Once open, the fold line remains faintly visible forever — a real
letter keeps its creases. A sheet rendered without crease lines after
opening looks like a web card and fails §9.

---

## 5. Full motion system

Every motion term, in this theme's own language. The theme's motion is
paper physics: panels turn on fold lines, wax cracks once, silk unwinds,
ink warms. There is no bounce, no spring overshoot anywhere except the
single soft wax press (§6.8), and nothing on the page moves that a sheet
of paper, a ribbon, or a candle could not.

**Named easings.**
- `--ease-unfold`: `cubic-bezier(0.22, 0.9, 0.28, 1)` — a panel turn:
  quick to lift, slow to lie flat. Used by §6.1, §6.2, §6.12.
- `--ease-crack`: `cubic-bezier(0.85, 0, 0.9, 0.3)` — the seal's crack:
  strain, then sudden give. Used once per seal (§6.1).
- `--ease-shard`: `cubic-bezier(0.47, 0, 0.74, 0.34)` — gravity taking a
  wax fragment: accelerating fall, no bounce on landing.
- `--ease-press`: `cubic-bezier(0.34, 1.35, 0.44, 1)` — the wax press's
  soft settle; the theme's only overshoot, capped at scale 0.94→1 (§6.8).
- `--ease-warm`: `cubic-bezier(0.4, 0, 0.2, 1)` — ink warming and light
  changes; the standard ease for everything thermal.
- Ribbon scrub (§6.3) and the chain-line parallax use **no easing** — they
  are scrubbed 1:1 to lerped scroll, because silk and paper do not ease
  against a hand pulling them.

**Duration tokens.** `--dur-crack` 500ms · `--dur-shard` 600ms ·
`--dur-unfold` 700ms (per panel) · `--dur-fold` 550ms · `--dur-monogram`
600ms · `--dur-warm-stagger` 200ms (between signature/postscript arrivals)
· `--dur-warm` 450ms (pale → full ink) · `--dur-press` 180ms ·
`--dur-join` 500ms · `--dur-refold` 600ms · `--dur-tilt` 300ms ·
`--breath` 8000ms (one candle breath, §6.6) · the universal fallback timer
is 1200ms (§6.1's law, applied to every fold).

**The terms, translated.**
- **Scroll-triggered reveals** — letters opening at reading position
  (§6.2): a letter's fold triggers when its seal crosses 62% of viewport
  height. Not a fade-up: the letter *opens*.
- **Parallax layers** — three depths only: the desk (static), the chain
  lines beneath each sheet (scrubbed at 0.92× scroll — the paper's grain
  lags a hair behind the sheet it belongs to), and the ribbon tail
  (§6.3, scrubbed 1:1). No element parallax-es across another's content.
- **Pinned scenes** — exactly one pin: the bundle furniture (ribbon +
  address panel, §6.9) pins in the margin while letters are read beneath
  it, releasing at the bundle's end. The hero's opening is *not* pinned —
  ceremony happens at the top of the page, in flow.
- **Masked line reveals** — letter text is revealed by the unfolding
  panels' clip-path (§6.1/§6.2): the mask is the fold itself, so text
  appears exactly where paper has opened, never on a timer of its own.
- **Blur-to-sharp reveals** — refused as a reveal. The only blur in the
  theme is the 0.4px of *unwarmed* handwriting (§6.7) lifting as attention
  warms it — a material state, not an entrance effect. Body text is never
  blurred at any point in any animation.
- **Animated counters** — the clerk counts: "letters in the bundle" and
  the opened-count in the header postmark (§6.3) tick in mono, one digit
  at a time, 90ms per tick, only when a letter actually opens. A counter
  that runs on load, before anything has been opened, is lying (§9).
- **Progress indicators** — the ribbon itself (§6.3): silk length in the
  margin tracks scroll depth exactly; plus the header postmark gaining a
  town per letter opened. There is no progress bar anywhere on the page.
- **Marquees** — refused. Nothing in a bundle of letters scrolls sideways
  begging attention. The closest lawful motion is the ribbon tail's slow
  curl (§6.3), which is scrubbed, not looped.
- **Ambient loops** — two, both barely perceptible: the candle breath
  (§6.6, opacity ±3% over 8s) and dust motes in the hero's light (6–9
  motes, 14–22s drift periods). Both pause off-screen and under
  reduced-motion they are simply absent, not frozen mid-frame.
- **Micro-interactions** — the wax press (§6.8), the letter tilt (§6.7's
  companion: paper lifted toward light, ≤2.5°), link underlines drawn as
  a ribbon thread (§11), the reply form's seal-button press (§6.16).
- **Hover physics** — attention warms handwriting (§6.7): ink darkens
  ~12% and 0.4px of blur lifts inside a 120px radius around the pointer,
  lerped at 0.18 per frame so warmth *spreads*, never snaps.
- **Page transitions** — the refold (§6.12): the current letter refolds
  seal-side out (600ms) and the next envelope slides in from the bundle's
  stack. Client-side only; a hard navigation simply loads the next bundle
  with its first letter's ceremony intact.
- **Image treatments** — portraits are enclosures: they scale-in-frame
  (1.05→1, 700ms `--ease-unfold`) inside deckled frames (§6.11), are
  printed in a warm duotone (`--ink` shadows, `--paper` highlights) so a
  colour photograph never shouts over the letters, and carry a handwritten
  caption in the hand (§3's ration applies: a caption is ≤14 words).

**The one shared loop.** All scroll-driven motion — ribbon scrub, chain-
line parallax, fold triggers, the warmth radius — runs in a single
requestAnimationFrame loop with lerp 0.12 toward the target scroll
position. Animations triggered by events (crack, unfold, press) are CSS
transitions/animations *started* by the loop or by interaction, never
separate rAF chains. The loop sleeps when the tab is hidden and when
scroll has been idle 2s with all values settled.

---

## 6. Signature elements

The twelve signature elements from the library entry (§6.1–§6.12), deepened,
then six page-family elements (§6.13–§6.18). Every element carries the v1
build spec and the v2 layers: choreography timeline, state matrix,
breakpoints, edge cases, accessibility, tokens.

### 6.1 The first opening (full ceremony)

- **What & why.** The hero is a sealed envelope front — the first letter,
  face down in the bundle, its wax seal up. On the visitor's first gesture
  of intent (scroll, click, or keyboard focus — whichever comes first),
  the seal cracks into two halves, shards scatter, and the letter unfolds
  in two panel turns into the full hero. This is the theme's signature and
  its promise: *what you came to read was sealed for you, and now it is
  open.* If this gesture is sloppy, the theme is a costume.
- **Structure.** A `<section class="letter letter--first">` containing the
  complete hero letter as real DOM text in reading order — dateline,
  salutation, body, signature, postscript — folded by CSS: two panel
  wrappers (`.panel--top`, `.panel--mid`) with `transform-origin` on their
  shared fold lines, the sheet itself the third panel. The seal is an
  inline SVG (two half-paths, the monogram group §6.5, a radial-gradient
  specular at 32%/28%) centred on the top fold. The closed state is a
  *presentation* of the open DOM: panels rotated `rotateX(-88deg)` with
  the envelope front (a `--paper-deep` face carrying the address panel's
  summary and the seal) shown. With JS disabled, no panel is rotated —
  the letter renders open and flat, seal pre-cracked beside it (§6.1
  reduced-motion state is the no-JS state).
- **Motion spec.** Trigger: first of {scroll ≥40px, click/tap on the
  letter, focus entering the letter}. Crack: the two seal halves rotate
  apart 12° on `--ease-crack` over `--dur-crack` (500ms), parting along
  the monogram's vertical. Shards: 5–7 wax fragments (SVG polygons,
  3–7px) scatter on `--ease-shard` over `--dur-shard` (600ms), falling
  18–34px, fading to 0 by 85% of travel — wax dust, not confetti. Unfold:
  top panel `rotateX(-88deg → 0)` over `--dur-unfold` (700ms,
  `--ease-unfold`), starting 120ms after the crack begins; mid panel
  follows 160ms later, same duration; the sheet's fold shadows deepen then
  settle (§4). Text is revealed by the panels' own clip — no separate
  text animation exists.
- **Choreography timeline (v2).** t=0 trigger (first gesture) → t=0 crack
  strain begins → t≈310ms wax gives, halves parting → t=120ms (parallel)
  top panel begins its turn → t=500ms crack complete, halves at rest at
  ±12°, resting against the sheet → t=600ms shards gone → t=820ms top
  panel flat → t=280ms mid panel begins → t=980ms mid panel flat → t=980ms
  the letter is fully open; §6.4's signature sequence starts (body already
  visible; signature warms at t≈1180ms) → t=1400ms ceremony complete,
  header postmark stamps the first town (§6.3). Total ≈1.4s, once per
  page view, never replayed.
- **State matrix (v2).** *Rest (pre-trigger):* sealed envelope front,
  seal whole, monogram drawn (§6.5) — identical on desktop and touch.
  *Hover:* the seal's specular brightens 8% (§6.8's press is armed); the
  letter does not tilt pre-opening — a sealed letter is not handled, it
  is presented. *Focus:* focus entering the letter is itself a trigger —
  the ceremony plays for keyboard visitors exactly as for pointers.
  *Active:* click is a trigger; there is no separate active state.
  *Scrolled-past:* if the visitor scrolls past the hero without
  triggering (fast flick), the letter opens anyway when its seal crosses
  62% viewport height — ceremony abbreviated to the unfold only, crack
  pre-played at 0.6× duration — because an unopened hero mid-page is a
  bug, not a mystery (§6.2's rule applies upward). *Disabled:* JS off or
  fallback fired — the open, flat letter with the pre-cracked seal beside
  the dateline; fully designed, fully readable.
- **Content merge.** The letter being opened *is* the hero content — the
  salutation, the announcement, the invitation. There is no headline
  above the envelope and no CTA below it that the ceremony delays: the
  hero's call to action, if any, is the letter's own last line ("The
  reply form is the last letter in this bundle — §6.16"), reached by
  reading.
- **Failure fallback.** The 1200ms law: a watchdog started at the trigger
  force-settles the letter to fully open at t=1200ms if the unfold has
  not completed (jank, interrupted tab, transition killed by a browser
  quirk). The watchdog, not `transitionend`, owns the decision. The seal
  halves snap to their resting ±12° in the same settle. No state exists
  in which the hero text is unreachable.
- **Reduced-motion variant.** The letter renders open and flat from first
  paint; the seal sits pre-cracked beside the dateline (both halves,
  resting angle), shards absent. Identical words, identical order.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: identical
  choreography; the sheet narrows (§4) and the fold panels shorten, so
  the turns read slightly faster at the same 700ms — acceptable, paper
  is smaller. <768px: the ceremony is *kept* — it is the theme's reason
  to exist — but the shard count drops to 4 and the mid panel's stagger
  tightens to 120ms so the whole gesture lands in ≈1.25s on a phone held
  in one hand; the trigger adds `touchstart` on the letter.
- **Edge cases & failure modes (v2).** *Repeat visits:* the ceremony
  plays once per page view; a `sessionStorage` flag does **not** suppress
  it on later pages of the same bundle session — each bundle's first
  letter is its own ceremony — but it never replays within one view,
  including on scroll-back-up. *Scroll-back:* an opened letter never
  refolds on scroll; refolding is navigation's job (§6.12) only.
  *Very long hero letter:* if the hero letter exceeds the two-fold
  geometry, it takes a third panel (§4) and a third 700ms turn at the
  same stagger; the watchdog extends to 1200ms + 700ms per extra panel.
  *Fonts late:* Nanum Pen loading late must not delay the crack — the
  ceremony is transform-only and starts on the gesture; the signature
  warms whenever it lands (§6.4 handles its own timing).
- **Accessibility spec (v2).** The sealed state is presentational: the
  letter's full text is in the DOM in reading order and is *not*
  `aria-hidden` when folded — a screen reader reads the letter without
  any ceremony, which is correct: the ceremony is for eyes. The seal SVG
  is `aria-hidden` with a visually-hidden text equivalent beside the
  dateline: "Sealed with the writer's monogram." Focus is never moved by
  the opening. The trigger-by-focus rule means a keyboard visitor who
  tabs into the letter sees it open as their focus lands — focus outline
  is `--ribbon` 2px offset 3px, visible against both `--paper` and
  `--paper-deep` (8.50:1 / on-deep contrast holds). Touch target: the
  whole letter is the trigger; no small target exists.
- **Performance budget & mobile variant.** Two panel transforms + one SVG
  group transform + ≤7 shard transforms, all compositor-only; ≤0.6ms/frame
  in the shared loop; zero layout after first paint (panels are sized by
  the open layout — CLS 0). Mobile variant: the reduced shard count and
  tighter stagger above; nothing else is cut — this element *is* the
  theme, and the budget is spent here first (§14's cut order protects it).
- **Tokens consumed (v2).** `--paper`, `--paper-deep`, `--paper-edge`,
  `--wax`, `--wax-bright`, `--wax-deep`, `--ink`, `--ease-crack`,
  `--ease-shard`, `--ease-unfold`, `--dur-crack`, `--dur-shard`,
  `--dur-unfold`, `--fold-shadow`.

### 6.2 Fold-down later letters

- **What & why.** Every letter after the first opens with the same ritual,
  abbreviated: a single fold-down as it reaches reading position. The
  abbreviation is the theme's manners — the visitor has been received;
  now the correspondence proceeds. A page where every letter demands the
  full ceremony is a page that never lets you read.
- **Structure.** Same sheet anatomy as §6.1 with one fold: a `.panel--top`
  wrapper over the static remainder. The closed letter shows its top
  panel's face: the dateline, the postmark, the seal (whole, monogram
  drawn §6.5) at the fold — the letter presents its credentials while
  still folded. Body text is in the DOM beneath the fold, revealed by the
  panel's clip as it turns.
- **Motion spec.** Trigger: the letter's seal crosses 62% of viewport
  height in the shared loop. The seal does **not** crack — later letters
  are opened by their fold, their seals sliding with the top panel and
  coming to rest, whole, at the sheet's top-left margin, like a seal on a
  letter that was slit open rather than broken. Panel: `rotateX(-84deg →
  0)` over `--dur-fold` (550ms, `--ease-unfold`). The fold shadow deepens
  mid-turn and settles to the resting crease (§4). On landing, §6.4's
  signature sequence and §6.10's ribbon join fire.
- **Choreography timeline (v2).** t=0 seal crosses 62% line → t=60ms the
  panel begins to lift (a breath between decision and motion, so the eye
  arrives first) → t=330ms panel at −30°, fold shadow at full depth →
  t=610ms panel flat, crease settles → t=610ms signature warm begins
  (§6.4) → t=760ms ribbon-line join draws to this letter (§6.10) →
  t=810ms letter fully at rest, clerk ticks the opened-count (§6.3).
- **State matrix (v2).** *Rest (pre-trigger):* folded, credentials
  showing. *Hover:* the sheet tilts ≤1.5° toward the light (§6.7's tilt,
  reduced — a folded letter is heavier) and the seal's specular warms 6%.
  *Focus:* focus entering a folded letter triggers its fold-down, same as
  §6.1 — keyboard reading opens letters too. *Active:* click anywhere on
  the folded sheet triggers immediately, for impatient readers.
  *Scrolled-past:* a letter flicked past unopened opens instantly at 0ms
  when it leaves the viewport top — the bundle never contains a letter
  the visitor has "missed"; scrolling back up, everything above is open.
  *Disabled:* open and flat, seal whole at the margin.
- **Content merge.** The fold is the letter's own top fold; the dateline
  and postmark on the folded face are the letter's real date and town.
  The abbreviation is honest about the fiction: the first letter was
  sealed *to the visitor*; the rest were sealed once and are being
  unfolded from the bundle.
- **Failure fallback.** The 1200ms law applies per letter: any fold not
  complete 1200ms after its trigger force-settles open. Additionally, an
  IntersectionObserver-independent check in the shared loop force-opens
  any letter whose top is above the viewport's top edge — geometry, not
  events, is the source of truth.
- **Reduced-motion variant.** All letters render open and flat; seals sit
  whole at each sheet's top-left margin. The bundle reads as a spread of
  opened letters — which is what it is.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: identical.
  <768px: the trigger line rises to 70% of viewport height (a phone's
  viewport shows less of the next letter, so it opens a touch later in
  its travel), and the tilt hover state is absent (no hover) — the fold
  itself is unchanged.
- **Edge cases & failure modes (v2).** *Short letter (< one panel):* a
  letter shorter than its fold geometry takes no fold — it presents open
  with its seal at the margin; forcing a fold on a postcard is theatre
  without paper. *Long letter (>900 words):* two folds (§4), two 550ms
  turns staggered 140ms, watchdog 1200ms + 550ms. *Scroll-back:* never
  refolds (§6.1's rule). *Rapid scroll through the whole bundle:* letters
  open in order, each at most once; the loop caps concurrent folds at 2,
  queueing the rest at 90ms intervals so a fast reader sees a ripple of
  openings down the bundle, never a frozen page of half-turned panels.
- **Accessibility spec (v2).** As §6.1: full text in DOM, fold is
  presentational, seal SVG `aria-hidden` with its text equivalent. The
  folded face's dateline/postmark are real text, read in order. Focus
  outline `--ribbon` 2px/3px offset. No focus movement.
- **Performance budget & mobile variant.** One transform per letter, ≤2
  concurrent; ≤0.3ms/frame in the loop. Mobile: unchanged motion, trigger
  line adjusted (above) — the fold is cheap and is never the cut.
- **Tokens consumed (v2).** `--paper`, `--paper-deep`, `--paper-edge`,
  `--ink`, `--ribbon`, `--ease-unfold`, `--dur-fold`, `--fold-shadow`.

### 6.3 Unwinding ribbon progress

- **What & why.** The bundle's silk ribbon is the page's progress: tied at
  the top of the margin, it unwinds down the margin as the visitor reads,
  its loose end curling further with depth, and the header postmark gains
  a new town stamp for every letter opened. Progress here is not a bar
  filling — it is the physical fastening of the object you are reading,
  coming undone in your hands.
- **Structure.** A fixed-height SVG ribbon path in the margin track
  (§4): a vertical silk strip (26px wide, `--ribbon` with a 1px
  `--ribbon-faded` edge line and a centre crease highlight) whose drawn
  length is scrubbed to scroll; below the drawn length, the *unwound
  tail*: a curling path whose curl radius tightens from 26px to 11px
  across the page's full scroll. The header postmark (§6.13) is a ring
  stamp (SVG circle text on a path: town + date) that re-stamps per
  opened letter. Opened-count and bundle-count live in the address panel
  in the clerk's mono: "LETTER Nº 3 OF 7".
- **Motion spec.** Scrubbed 1:1 to lerped scroll in the shared loop — no
  easing, silk does not ease. The tail curl is a path morph parameterised
  by scroll fraction (0→1 over the bundle's full height). Postmark
  re-stamp: on each letter-open event, the ring scales 1.18→1 over
  `--dur-press` (180ms, `--ease-press`) with a 40ms ink-bloom (opacity
  0.55→1, `--ease-warm` 300ms) — a stamp coming down. The clerk's counter
  ticks one digit, 90ms.
- **Choreography timeline (v2).** Continuous: ribbon length = scroll
  fraction × margin height, updated per frame from the lerped value.
  Per letter-open: t=0 letter lands open (§6.2 t=610ms) → t=+40ms
  postmark lifts (scale 1.18, opacity 0.55) → t=+220ms stamp lands,
  counter ticks → t=+340ms bloom settled; the new town is the opened
  letter's own postmark town.
- **State matrix (v2).** *Rest:* at scroll 0, the ribbon shows its knot
  and 0px of unwound length; the postmark shows the first letter's town
  (unstamped state: ring at 60% `--ribbon-faded` — graphic only).
  *Hover:* none — the ribbon is not interactive. *Focus:* none.
  *Active:* none. *Scrolled-past / scroll-back:* the ribbon rewinds
  exactly as it unwound (scrub is symmetric); the postmark does **not**
  un-stamp — letters once opened stay opened, and the clerk's count never
  decreases. That asymmetry is deliberate: silk can be rewound, reading
  cannot be unread. *Disabled:* JS off — the ribbon renders fully drawn
  at a fixed length (the bundle shown tied, §6.9's rest state) and the
  postmark shows the first town statically.
- **Content merge.** The ribbon ties the actual bundle being read; its
  length is the bundle's read length. The postmark towns are the letters'
  real towns, in order — the progress indicator is a catalogue of the
  correspondence itself.
- **Failure fallback.** If the shared loop dies, the ribbon freezes at
  its last length — a cosmetic freeze, never a content gate; the clerk's
  count is DOM text updated by the open events and remains correct.
- **Reduced-motion variant.** The ribbon renders at full drawn length
  statically (the bundle shown read), the tail curled at its final
  radius; postmark shows the last letter's town; counter shows the full
  count. No scrub, no stamp animation.
- **Breakpoints (v2).** ≥1200px: as specced, margin track 176px.
  768–1199px: margin track narrows to 120px, ribbon 22px wide; tail curl
  radius range 22px→10px. <768px: the margin ribbon leaves the margin —
  the bundle goes full-width (§4) and the ribbon becomes a 26px silk
  strip down the sheet's left edge *on the paper itself*, scrubbed the
  same way; the postmark moves into the address panel's compact header
  form (§6.13). Progress is never dropped at any size, only relocated.
- **Edge cases & failure modes (v2).** *Short page (3 letters):* the tail
  curl's radius range compresses proportionally; the effect must still
  read as unwinding, not as a full curl in the first viewport. *Letter
  opened out of order* (anchor jump to letter 5): the postmark stamps
  letter 5's town and the count reads letters *opened*, not letters
  passed — the clerk counts openings, and the address panel's wording
  ("Nº — OF —") is filled from the highest opened letter's number and
  the bundle total, never from scroll position. *Resize:* ribbon length
  recomputes from the same scroll fraction; no jump.
- **Accessibility spec (v2).** The ribbon SVG is `aria-hidden` (it is a
  picture of progress, not the progress). The clerk's count is real text
  in the address panel, updated without a live region — it changes on
  the visitor's own action and is read when they reach it; announcing
  every opening would narrate over the letters. The postmark ring's town
  text duplicates the letter's own visible dateline, so nothing is
  stamp-only information.
- **Performance budget & mobile variant.** One SVG path `stroke-dashoffset`
  (or `d` morph for the tail, precomputed as 24 interpolated frames,
  stepped — not a per-frame path solve) per frame: ≤0.2ms. Mobile: the
  on-paper relocation above; the tail morph is cut on <768px (the tail
  shows its final curl statically while length still scrubs) — the first
  saving in §14's cut order.
- **Tokens consumed (v2).** `--ribbon`, `--ribbon-faded`, `--paper`,
  `--ease-press`, `--ease-warm`, `--dur-press`.

### 6.4 Warm-after signatures

- **What & why.** A letter's body is print-calm Cormorant; its signature
  and postscript are the writer's hand, and they arrive *after* the body —
  staggered, warming from pale brown to full ink as they land. Written
  last, as letters are. The warmth is the theme's thesis in miniature:
  attention and time turn marks into presence.
- **Structure.** The signature is a `<p class="signature">` in Nanum Pen
  Script 30px (§3), rotated −2° to −4°, placed three lines below the last
  body line; postscripts (`<p class="postscript">`, 26px) two lines below
  the signature, prefixed "P.S." in the same hand. Both are real text in
  the DOM in reading order. Their rest state before arrival is
  `--ink-pale` at 0.4px blur — present, legible if looked for, clearly
  not yet *landed*.
- **Motion spec.** Trigger: the owning letter's open landing (§6.1
  t=980ms / §6.2 t=610ms). Signature: colour `--ink-pale → --ink` and blur
  0.4px → 0 over `--dur-warm` (450ms, `--ease-warm`), starting 200ms
  after landing. Each postscript follows at `--dur-warm-stagger` (200ms)
  intervals, same warm. If a letter has two postscripts (the theme's
  maximum), the second warms 200ms after the first. Total sequence ≤
  200 + 450 + 200 + 450 ≈ 1.3s worst case, and it never delays anything
  else — the letter is fully readable from the moment it opens; only the
  hand is still arriving.
- **Choreography timeline (v2).** t=0 letter lands open → t=200ms
  signature begins warming → t=650ms signature at full ink → t=850ms
  first postscript begins → t=1300ms first postscript full → (t=1500ms
  second postscript begins → t=1950ms full, only when present).
- **State matrix (v2).** *Rest (letter unopened):* signature at
  `--ink-pale`, blurred 0.4px — behind the fold, so unseen in practice.
  *Hover:* hovering the signature itself deepens nothing (it is already
  ink); hovering the *body* warms via §6.7, which includes the signature
  in its radius. *Focus:* a signature is never focusable (it is a
  paragraph). *Active:* none. *Scrolled-past:* fully warmed, static —
  warmth never cools on scroll-back; a read letter stays read.
  *Disabled:* rendered at full `--ink`, no blur, from first paint.
- **Content merge.** The signature is the letter's actual sign-off — the
  writer's name on their own words. The postscript carries real content
  (the afterthought, the enclosure note, the reply invitation), never a
  decorative scribble.
- **Failure fallback.** Warmth is a colour transition on DOM text; if it
  never runs, the text sits at `--ink-pale` — which is why `--ink-pale`
  is specified legible (3.69:1 at 26–30px hand sizes is AA for large
  text) and why a 1200ms watchdog per letter force-sets full ink. A
  signature may pass through pale; it may never be stranded there.
- **Reduced-motion variant.** Signatures and postscripts render at full
  `--ink`, unblurred, from first paint.
- **Breakpoints (v2).** All sizes identical, except <768px where the
  signature size holds at 30px (§3 forbids shrinking the hand) and the
  rotation flattens to −2° so a long name cannot clip the sheet edge.
- **Edge cases & failure modes (v2).** *Long signature / two-name
  sign-off:* wraps to a second line in the hand, warming as one unit —
  never letter-by-letter (the hand warms, it does not type). *Letter
  with no signature* (a formal notice in the bundle): no warm sequence;
  the letter closes with its dateline repeated in the clerk's mono —
  the theme permits an unsigned letter but marks it as the clerk's, not
  the writer's. *Font swap:* if Nanum Pen arrives after the warm, the
  warm re-runs once at 200ms so the hand is never seen cold in its true
  face — one re-run maximum, owned by the same watchdog.
- **Accessibility spec (v2).** Signature and postscript are ordinary
  paragraphs in reading order — a screen reader hears the sign-off and
  the P.S. exactly where a reader sees them. The pale phase is visual
  only. Contrast at rest state after warm: 11.17:1. During the 450ms
  transient it passes through 3.69:1 at large sizes — lawful for a
  transition, and the watchdog guarantees it is a transition.
- **Performance budget & mobile variant.** One colour/filter transition
  per element, ≤3 elements per letter, never concurrent across letters
  (the open queue §6.2 serialises them). Cost negligible. Mobile:
  unchanged.
- **Tokens consumed (v2).** `--ink`, `--ink-pale`, `--ease-warm`,
  `--dur-warm`, `--dur-warm-stagger`.

---

### 6.5 Self-drawing seal monogram

- **What & why.** Before a letter can be opened, its seal introduces
  itself: the monogram pressed into the wax draws itself in stroke, once,
  as the letter is first presented. It is the writer's mark arriving
  before their words — and it teaches the visitor, silently, that seals
  are the letters' gates (§6.1/§6.2) before the first one is ever broken.
- **Structure.** Inside each seal's SVG (§6.1), the monogram is a
  `<g class="monogram">` of 2–4 stroke paths (the writer's initials
  intertwined — one monogram per *bundle author*, reused identically on
  every seal in the bundle; a bundle from two writers has two monograms,
  each letter sealed by its own author). Stroke: `--wax-bright` at 1.6px
  on the `--wax` disc, drawn via `stroke-dashoffset`. A soft radial
  specular (`--wax-bright` at 22% → transparent) sits above the monogram
  at 32%/28%, so the drawing reads as light catching a pressed groove.
- **Motion spec.** Trigger: the letter's seal first enters the viewport
  (any part). Draw: each path's dashoffset animates over `--dur-monogram`
  (600ms total, paths staggered 90ms, `--ease-warm`). The specular does
  not move during the draw. Once drawn, a monogram never redraws — scroll
  away and back, it stays drawn.
- **Choreography timeline (v2).** t=0 seal enters viewport → t=80ms
  first path begins (a breath, so the eye finds the seal first) →
  t=170ms second path → t=260ms third (if present) → t=680ms draw
  complete; the seal is now "presented" and §6.1/§6.2's triggers are
  armed (they are armed regardless — the draw never gates the open).
- **State matrix (v2).** *Rest (pre-presentation):* monogram present but
  undrawn — rendered as a faint pressed groove (`--wax-deep` stroke at
  35%), so the seal is never blank. *Hover:* specular +8% (§6.8 arms).
  *Focus:* seals are not focusable; the letter is (§6.1). *Active:* the
  press (§6.8). *Scrolled-past:* drawn, static. *Disabled:* monogram
  rendered fully drawn in `--wax-bright` from first paint.
- **Content merge.** The monogram is the author's actual initials, the
  same mark their real seal would press. On the first letter it is the
  brand mark of the correspondence — the one place the theme permits a
  logo-like device, because a seal *is* a logo that predates logos.
- **Failure fallback.** The groove state (35% `--wax-deep`) is the CSS
  default; JS adds the draw. If the draw never runs, every seal still
  shows its monogram as a pressed groove — quieter, complete.
- **Reduced-motion variant.** Monogram fully drawn from first paint, in
  `--wax-bright`, no groove phase.
- **Breakpoints (v2).** ≥1200px: seal 92px, monogram stroke 1.6px.
  768–1199px: seal 84px. <768px: seal 76px, stroke 1.8px (a smaller seal
  needs a heavier groove to read at arm's length). Draw duration
  unchanged.
- **Edge cases & failure modes (v2).** *Complex monogram (>4 paths):*
  refused at build time — a real seal stamp is cut simply; §10 checks
  path count. *Two authors:* each monogram draws on its own letters
  only; the address panel (§6.13) shows both, drawn. *Seal in the hero:*
  the hero seal's monogram draws on load (it is in the first viewport),
  completing before most first gestures — if the visitor triggers the
  opening mid-draw, the crack (§6.1) interrupts the draw and the halves
  carry partial monograms, exactly as a real cracked seal carries a
  broken mark. This is correct behaviour, not a bug.
- **Accessibility spec (v2).** The monogram is decorative within an
  `aria-hidden` SVG; the author's name is in the letter's dateline and
  signature as text. No information is monogram-only.
- **Performance budget & mobile variant.** One dashoffset animation per
  seal, ≤2 concurrent (the open queue serialises presentation too);
  negligible cost. Mobile: unchanged except seal size (above).
- **Tokens consumed (v2).** `--wax`, `--wax-bright`, `--wax-deep`,
  `--ease-warm`, `--dur-monogram`.

### 6.6 Candle-warm breathing light

- **What & why.** The bundle is read by candlelight, and the candle
  breathes: a warm radial light over the laid paper swells and settles
  almost imperceptibly, and in the hero's light, dust motes drift. This
  is the theme's only pure ambience, and its restraint is the point —
  if a visitor *notices* the breathing, it is too strong (§9).
- **Structure.** A `::before` overlay on the bundle container: a radial
  gradient (`--candle` at 8% → transparent 62%) centred at 68%/12% of
  the bundle (the candle stands to the upper right, off-page), animating
  only its opacity. Dust motes: a single absolutely-positioned canvas in
  the hero letter only, 6–9 motes (1–2px, `--ink` at 10–18% opacity)
  drifting on slow sine paths. The overlay is `pointer-events: none`
  and sits *above* the paper texture but *below* nothing else — text is
  never dimmed by it because the gradient only adds warmth over
  `--paper`, and its darkest swing (−3%) is inside the paper's own
  tonal range.
- **Motion spec.** Breath: opacity oscillates ±3% around its base over
  `--breath` (8000ms, sine in-out, infinite) — in dark mode ±5% (§2).
  Motes: each drifts 14–22s per traverse, rising slightly (candle
  convection), wrapping at the hero's edges with a fade. Both pause when
  off-screen (the breath only matters where paper is) and when the tab
  is hidden.
- **Choreography timeline (v2).** Continuous from first paint; the
  breath's phase starts at its neutral point so there is no visible
  "switching on". Motes fade in over 2000ms after the hero opens (§6.1)
  — dust is seen once the letter is open and the light has somewhere to
  fall.
- **State matrix (v2).** *Rest/hover/focus/active:* unaffected by
  interaction — the candle does not respond to the reader; that
  indifference is what makes it feel like light rather than UI.
  *Scrolled-past:* the breath continues over whichever letters are in
  view (the gradient is bundle-wide). *Disabled:* JS off — the gradient
  renders at its base opacity statically; motes absent (canvas never
  initialises). A static warm wash is the designed disabled state.
- **Content merge.** The light falls on the paper of the letters
  themselves — it is the reading condition of the whole fiction, not a
  decoration applied to one component. Removing it leaves the theme
  intact but colder; §9 lists a *noticeable* breath as slop, and §10
  measures it.
- **Failure fallback.** Static gradient (above). The page loses nothing
  readable.
- **Reduced-motion variant.** Gradient at base opacity, static; no
  motes. In dark mode the static gradient sits at the +2% point of its
  range, so the candlelit desk keeps its warmth without motion.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: gradient centre
  moves to 74%/10% (the narrower bundle sits more of its paper under
  the light). <768px: gradient centre 50%/8%, radius widened — on a
  phone the whole sheet is in the candle's circle; motes reduce to 4.
- **Edge cases & failure modes (v2).** *Low-power device:* if the shared
  loop's frame budget is exceeded for 60 consecutive frames, the breath
  freezes at base opacity and motes stop spawning (§14's cut order,
  step 1 — ambience is always the first cut). *Canvas unavailable:* no
  motes, breath unaffected. *Long pages:* the gradient is one overlay
  on the bundle container — it must be implemented as a background on a
  full-height element with `background-attachment` semantics handled so
  it does not repaint per scroll frame; the loop moves nothing about it
  except its opacity keyframes, which are compositor-driven.
- **Accessibility spec (v2).** Purely decorative; `aria-hidden` canvas,
  overlay not in the accessibility tree. The ±3% opacity swing cannot
  push any text below its contrast floor: worst case, `--ink` on
  `--paper` at the breath's low point still measures ≥10.8:1.
- **Performance budget & mobile variant.** One compositor opacity
  animation + one small canvas (hero only, ≤9 particles): ≤0.3ms/frame.
  Mobile: mote count 4, breath unchanged (it is nearly free).
- **Tokens consumed (v2).** `--candle`, `--paper`, `--ink`, `--breath`.

### 6.7 Attention-warms handwriting hover

- **What & why.** Where the reader's attention lingers, the handwriting
  warms: ink darkens ~12% and a hair of blur lifts within a 120px radius
  of the pointer — as if the reader leaned closer with the candle. It is
  the theme's thesis as an interaction: these words respond to being
  read closely, and to nothing else.
- **Structure.** Applies to the hand-set matter only: signatures,
  postscripts (§6.4), handwritten captions (§6.11), and the reply form's
  signature field (§6.16). Implementation: each warmable element carries
  a `--warm` custom property (0→1); the shared loop computes the
  pointer's distance to each warmable element's centre per frame and
  lerps `--warm` toward the target (1 inside 120px, falling to 0 at
  240px). Colour interpolates `--ink-pale`-ward at rest… no: at rest the
  hand is full `--ink` (§6.4 has already landed it); warmth *deepens* it
  toward a `--ink-warm` `#2A1D13` and lifts a standing 0.4px blur that
  unwarmed handwriting carries at rest. The blur is the tell: handwriting
  at rest is slightly soft, as ink on laid paper is; attention sharpens
  it.
- **Motion spec.** Lerp 0.18/frame toward the distance-derived target —
  warmth spreads over ~250ms and fades over ~600ms when the pointer
  leaves (asymmetric: paper holds heat). Blur 0.4px→0 and colour
  `--ink → --ink-warm` are both driven by the single `--warm` value, so
  they can never disagree. Companion tilt: the letter sheet under the
  pointer tilts ≤2.5° toward the light (`rotateX/rotateY` from pointer
  offset, `--dur-tilt` 300ms ease-out on release) — paper lifted in the
  hand. Tilt and warmth are separate properties; warmth without tilt is
  used inside the form (§6.16) where tilting a sheet you are writing on
  would be absurd.
- **Choreography timeline (v2).** Continuous, pointer-driven: t=0
  pointer enters 240px radius → `--warm` begins rising → t≈250ms full
  warmth at ≤120px → pointer leaves → t≈600ms warmth fully faded, blur
  restored. No discrete beats; the timeline is the lerp.
- **State matrix (v2).** *Rest:* hand at `--ink`, 0.4px blur. *Hover:*
  the warmth field as specced — desktop pointer only. *Focus:* keyboard
  focus on or within a letter sets `--warm: 1` on that letter's hand
  matter instantly (no lerp — focus is a decision, not an approach) and
  holds it while focus remains inside. *Active:* none. *Scrolled-past:*
  `--warm` resets to 0 as elements leave the viewport (the loop stops
  computing them). *Disabled:* JS off — hand renders at `--ink`, **no
  blur**: the standing blur is a JS-armed pre-state like every other in
  this theme, so the no-JS page is fully sharp. *Touch:* no hover —
  instead, a tap on hand matter pulses `--warm` 0→1→0 over 900ms
  (`--ease-warm`), the reader's finger having "touched" the ink.
- **Content merge.** The warmth acts on the ink of the actual words being
  read — the signature, the P.S., the caption under the photograph. It
  never applies to Cormorant body text: print does not warm; hands do.
  That distinction is the theme's typography made interactive (§3).
- **Failure fallback.** If the loop dies, `--warm` freezes wherever it
  is; the watchdog (§6.4's) also sweeps warmable elements, resetting blur
  to 0 if the loop has been dead 1200ms — a frozen half-blur is the only
  failure this element can produce, and it is designed out.
- **Reduced-motion variant.** No warmth, no blur at rest, no tilt: hand
  matter renders at `--ink`, sharp, always. Focus still shows the
  `--ribbon` outline (an outline is information, not motion).
- **Breakpoints (v2).** ≥1200px: radius 120/240px as specced.
  768–1199px: identical. <768px: hover absent; tap-pulse only; tilt cut
  entirely (a phone is already the hand holding the paper — tilting the
  sheet inside it is a doll's-house effect, §9).
- **Edge cases & failure modes (v2).** *Many warmable elements in view*
  (a letter with signature + 2 postscripts + caption): the loop computes
  distance to each — at most 5 warmable elements exist per letter by
  construction (§3's ration), so the per-frame cost is bounded.
  *Pointer moving fast:* the lerp smooths it; warmth trails the pointer
  like heat should. *Pointer leaves the window:* all `--warm` targets
  go to 0. *Warmth during the signature's arrival (§6.4):* §6.4's warm
  (pale → ink) and this warm (ink → ink-warm) compose: the arrival runs
  first; hover warmth applies on top only after landing, so the two
  systems never fight over the same property — §6.4 animates `color`
  via its transition, §6.7 drives `--warm`, and the final colour is
  computed from both.
- **Accessibility spec (v2).** Decorative response to pointer position;
  nothing is revealed by warmth that is not already legible — rest-state
  hand text is `--ink` at 11.17:1 with a 0.4px blur that does not reduce
  measured contrast below AA at hand sizes (26–30px). Keyboard visitors
  get the focus state above. Touch targets are unaffected (warmth has no
  targets of its own).
- **Performance budget & mobile variant.** ≤5 distance computations +
  custom-property writes per frame, and only while the pointer is over
  the bundle: ≤0.2ms/frame. Mobile: tap-pulse only, tilt cut (above).
- **Tokens consumed (v2).** `--ink`, `--ink-warm` `#2A1D13`, `--ribbon`,
  `--ease-warm`, `--dur-tilt`.

### 6.8 Wax-press click

- **What & why.** The click, in this theme, is a wax press: pressing a
  letter's seal stamps it down with a soft scale and a brief flare of its
  specular highlight — the gesture of sealing, answering the gesture of
  opening (§6.1). It is how the visitor *handles* a seal without breaking
  it: on letters already open, on the reply form's seal-button (§6.16),
  and on the address panel's seal-mark (§6.13).
- **Structure.** The seal SVG (§6.1/§6.5) is the press target where it
  appears on an opened letter (resting at the sheet's top-left margin,
  §6.2) — a real `<button class="seal-press">` wrapping the SVG when the
  seal has an action (e.g. "re-read this letter from the top" is *not*
  an action; the seal-button exists only where pressing does something:
  submitting the reply §6.16, confirming the RSVP, stamping the guest
  book §7). A decorative seal is never a button — §9 forbids pressable
  seals that do nothing.
- **Motion spec.** Press: seal scales 1 → 0.94 over 90ms, then settles
  back to 1 over `--dur-press` (180ms total, `--ease-press` — the theme's
  only overshoot, and it is in the *release*, like wax giving under a
  stamp). The specular radial flares: opacity 22% → 40% at the press's
  bottom (t=90ms), settling by t=180ms. A faint ring — the stamp's edge —
  impresses into the paper: a 1px `--wax-deep` circle at the seal's rim
  fades in at t=90ms and remains, very faint, for the rest of the page
  view: you can see where the seal was pressed. Once per seal per view;
  repeat presses re-flare but do not darken the ring.
- **Choreography timeline (v2).** t=0 pointerdown → t=90ms full
  compression, specular at peak, ring impresses → t=180ms settle
  complete; the button's action fires on `click` (pointerup) as normal —
  the press animation never delays the action.
- **State matrix (v2).** *Rest:* seal at rest, specular 22%. *Hover:*
  specular +8% (the stamp is being considered). *Focus:* `--ribbon` 2px
  outline offset 3px around the seal-button; specular +8% as hover.
  *Active:* the press. *Scrolled-past:* the impressed ring persists.
  *Disabled:* a disabled seal-button renders at 55% opacity with its
  specular off and does not press — used by §6.16 while the reply is
  being sent.
- **Content merge.** The press acts on the letter's own seal, and the
  ring it leaves is in the letter's own margin — a handling mark on the
  object handled. On the reply form, the seal-button *is* the submit:
  the visitor seals their reply to send it (§6.16).
- **Failure fallback.** The button is a button: without JS it submits /
  navigates natively; the press is a CSS `:active` transform that needs
  no JS at all. Nothing to fall back *from*.
- **Reduced-motion variant.** No scale, no flare: the ring impresses
  instantly on activation and the action fires. The information (pressed,
  done) survives; the theatre does not.
- **Breakpoints (v2).** All sizes: seal-button minimum target 48×48px
  (the 76px mobile seal §6.5 satisfies this; the address panel's small
  seal-mark is decorative and not a button).
- **Edge cases & failure modes (v2).** *Rapid repeat presses:* the
  animation restarts cleanly (it is a transition, not a queued
  animation); the ring does not stack. *Press during the seal's own
  letter opening (§6.1):* the opening owns the seal until it lands;
  presses during the ceremony are ignored (the button is inert until
  t=1400ms) — you cannot stamp a seal that is currently cracking.
  *Long-press / drag-off:* standard button behaviour; the press visual
  follows `:active`, cancelling on drag-off.
- **Accessibility spec (v2).** Real `<button>`, real label ("Seal and
  send your reply" — §6.16; never "click the seal"). Focus outline as
  above. The ring impression is decorative. The press is announced by
  the button's own state changes, not by the animation.
- **Performance budget & mobile variant.** One transform + one opacity,
  event-driven only. Mobile: identical (the press is *for* touch — it is
  the theme's tap feedback everywhere a seal acts).
- **Tokens consumed (v2).** `--wax`, `--wax-bright`, `--wax-deep`,
  `--ribbon`, `--ease-press`, `--dur-press`.

---

### 6.9 Pinned bundle furniture

- **What & why.** While the letters are read, the bundle's own wrapping
  stays with the reader: the ribbon and the address panel pin in the
  margin, so the visitor always knows whose bundle this is, which letter
  they are in, and how much ribbon is left. It is the theme's single
  pinned scene (§5), and it releases at the bundle's end — the furniture
  is put down when the correspondence is done.
- **Structure.** The margin track (§4) holds a `position: sticky` group:
  the address panel (§6.13 — sender, recipient, the letters' titles as
  address lines, the clerk's count §6.3) above a ribbon segment whose
  drawn length is §6.3's scrub. The group pins at `top: 32px` from the
  moment the first letter's seal passes it, until the last letter's
  bottom fold reaches it, where it un-pins and scrolls away with the
  bundle's end into the colophon (§6.17). Sticky, not fixed: the
  furniture belongs to the bundle's column and can never overlap the
  desk or another bundle on an archive page (§7).
- **Motion spec.** No entrance animation — furniture is simply *there*,
  as it was when the bundle was laid down. Its only motions are §6.3's
  ribbon scrub inside it and the address panel's current-letter line
  updating (the active letter's address line gains a `--ribbon`
  underline drawn left→right, 300ms `--ease-warm`, as each letter
  reaches reading position). Release at the end is plain scroll — no
  farewell animation.
- **Choreography timeline (v2).** Continuous: pin engages when the
  bundle's top reaches 32px from viewport top → per letter-open, the
  address line underline draws (300ms) and the clerk's count ticks
  (§6.3) → pin releases when the colophon (§6.17) enters at the margin's
  height.
- **State matrix (v2).** *Rest:* unpinned at the bundle's head, showing
  letter № 1 as current. *Hover:* address lines that are links warm to
  `--ribbon` (§6.13). *Focus:* the panel is the page's navigation —
  focus order runs through it before the letters (§6.13). *Active:*
  current letter's line carries the drawn underline. *Scrolled-past:*
  after release, the panel sits at the bundle's end in the DOM order it
  visually left — no duplicate panel exists. *Disabled:* JS off — the
  panel is a static block at the bundle's head; sticky CSS still works
  without JS, and where it doesn't, the panel simply heads the page.
  *Touch:* identical (sticky is not hover-dependent).
- **Content merge.** The pinned things are the bundle's own address and
  its own ribbon — the wrapping, held while the contents are read. They
  are not a site chrome borrowed from another fiction: there is no logo
  bar, no menu button, no search field pinned here.
- **Failure fallback.** Sticky is progressive CSS; without it the panel
  heads the page and the letters follow — the bundle read from the top,
  as bundles were for centuries.
- **Reduced-motion variant.** Identical (sticky is layout, not motion);
  the address-line underline appears instantly instead of drawing.
- **Breakpoints (v2).** ≥1200px: margin 176px, panel full (§6.13).
  768–1199px: margin 120px; the panel compresses — sender/recipient and
  the count remain, the letters' address lines shorten to their numbers
  and towns. <768px: **no pin and no margin** — the panel becomes the
  page's head block (full width, §6.13's compact form) and scrolls away
  naturally; the ribbon relocates onto the paper (§6.3). A pinned panel
  on a phone would eat the letter's width, and the letter always wins.
- **Edge cases & failure modes (v2).** *Short bundle (3 letters):* the
  pin may engage and release within two viewports — correct; furniture
  for a short bundle is briefly held. *Very tall viewport (≥1200px
  height):* the panel pins at 32px and the ribbon's visible segment is
  capped at 70vh so the tail (§6.3) never stretches into a stripe.
  *Print:* the panel prints once, at the bundle's head (§14).
- **Accessibility spec (v2).** The panel is a `<nav>` with an
  `aria-label` ("This bundle of letters"); the current letter's line
  carries `aria-current="true"`. Sticky positioning does not change
  focus order: DOM order is panel → letters, which is also the reading
  order. Contrast: panel text `--ink` on `--paper` 11.17:1; address
  lines `--ribbon` 8.50:1.
- **Performance budget & mobile variant.** Sticky + one 300ms underline
  transition per letter-open. Mobile: unpinned head block (above) — the
  cheapest form of the element.
- **Tokens consumed (v2).** `--paper`, `--ink`, `--ribbon`,
  `--ease-warm`.

### 6.10 Ribbon-line SVG joins

- **What & why.** As each new letter opens, a ribbon line draws itself
  between it and the letter before it — stitching the bundle's order.
  The margin ribbon (§6.3) shows *how far*; the joins show *the
  sequence*: this letter follows that one, tied, in the writer's order.
- **Structure.** An inline SVG spanning the 96px desk gap between
  consecutive sheets (§4): a path in `--ribbon` (2px, with the silk's
  centre highlight as a parallel 0.75px `--ribbon-faded` path) that
  leaves the previous letter's bottom-left margin, bows slightly (a
  hanging silk curve, control point 14px below the straight line), and
  enters the next letter's top-left margin at the point where its seal
  will rest. Drawn via `stroke-dashoffset`.
- **Motion spec.** Trigger: the lower letter's fold landing (§6.2
  t=610ms). Draw over `--dur-join` (500ms, `--ease-warm`), starting
  150ms after landing — the letter settles, then the bundle is tied to
  it. Direction is always downward (bundle order); a join never draws
  upward.
- **Choreography timeline (v2).** t=0 lower letter lands → t=150ms draw
  begins at the upper letter's margin → t=300ms the bow's lowest point →
  t=650ms the line reaches the lower letter's margin and stops; the
  lower letter's seal specular (§6.5) warms 6% for 300ms as the line
  arrives — the tie touches the seal.
- **State matrix (v2).** *Rest (lower letter unopened):* no join — the
  gap shows desk. *Hover/focus/active:* none (the join is not
  interactive). *Scrolled-past:* drawn, static; scroll-back never
  undraws it (reading cannot be unread, §6.3's asymmetry). *Disabled:*
  joins render fully drawn between all letters from first paint — the
  bundle shown tied.
- **Content merge.** The line follows the same ribbon that ties the real
  bundle in the margin — it is that ribbon, stepping across the gap
  between sheets. Its endpoints are the letters' own margins, not
  abstract nodes.
- **Failure fallback.** CSS default is drawn; JS arms the undrawn state
  only when it can also run the draw. A join that never draws leaves a
  gap of desk — noticeable, harmless, and impossible by construction
  (the arming rule).
- **Reduced-motion variant.** Joins appear fully drawn as each letter
  opens (instant, at the landing moment).
- **Breakpoints (v2).** ≥1200px and 768–1199px: as specced. <768px: the
  gap between sheets narrows to 64px and the bow flattens (control point
  8px) — same draw, smaller gesture.
- **Edge cases & failure modes (v2).** *Letters opened out of order*
  (anchor jump): the join to the jumped-to letter draws when it opens;
  joins to still-folded letters above it remain undrawn until those
  letters open — the bundle's stitching honestly shows what has been
  read in sequence and what was visited out of turn. *First letter:*
  no join above it; its join downward is drawn by the second letter's
  opening.
- **Accessibility spec (v2).** `aria-hidden` SVG; bundle order is
  carried by DOM order and the clerk's numbering (§6.3), never by the
  line alone.
- **Performance budget & mobile variant.** One dashoffset animation per
  letter-open, never concurrent with another join. Negligible. Mobile:
  flattened bow (above).
- **Tokens consumed (v2).** `--ribbon`, `--ribbon-faded`, `--ease-warm`,
  `--dur-join`.

### 6.11 Deckle-frame portraits

- **What & why.** Letters enclose photographs. A portrait in this theme
  is an enclosure — tucked into the correspondence, in a deckle-edged
  frame, with a handwritten caption — and it scales in-frame as the
  reader reaches it, the way a photograph is drawn out of an envelope
  and settles flat.
- **Structure.** A `<figure class="enclosure">` inside the owning
  letter's sheet (never between letters — an enclosure belongs to a
  letter): the image in a frame whose edge is an SVG deckle mask
  (irregular torn edge, generated once per bundle and reused — a
  family's photographs were cut with the same scissors), a warm duotone
  treatment (§5), and a `<figcaption>` in the hand (Nanum Pen 26px,
  ≤14 words, §3's ration), rotated −1.5°.
- **Motion spec.** Trigger: the figure's top crosses 70% viewport
  height. The image scales 1.05 → 1 inside its frame (frame static,
  image clipped by it) over 700ms `--ease-unfold`, with the duotone's
  warmth deepening in step (`--ease-warm`): at 1.05 the print is
  slightly pale, at 1 it is fully developed. No fade — photographs do
  not fade in; they are taken out and laid down.
- **Choreography timeline (v2).** t=0 figure crosses 70% → t=0 scale
  and warmth begin together → t=700ms image at 1, fully warm → the
  caption is already present (it was under the photograph in the
  envelope; it does not animate separately).
- **State matrix (v2).** *Rest (pre-trigger):* image at 1.05, pale —
  this pre-state is JS-armed only; the CSS default is the settled
  photograph. *Hover:* the figure tilts ≤1.5° (§6.7's tilt, reduced —
  a photograph in a frame is handled gently) and the caption warms
  (§6.7 applies to the hand caption). *Focus:* if the figure is a link
  (to the full enclosure, §7), the frame's edge gains a `--ribbon`
  outline. *Active:* none. *Scrolled-past:* settled. *Disabled:* the
  settled photograph, caption present.
- **Content merge.** The portrait illustrates the letter that encloses
  it — the person the letter is about, the house it describes — and its
  caption is in the writer's hand because the writer captioned it. A
  stock photograph with a typed caption is a §9 failure.
- **Failure fallback.** Image load failure shows the frame with the
  caption and a clerk's line in mono where the print would be:
  "ENCLOSURE MISSING — DESCRIBED IN THE LETTER" — and the letter's text
  must in fact describe it (§10 checks the pairing). The layout reserves
  the frame's aspect box, so a missing print never collapses the sheet.
- **Reduced-motion variant.** The photograph renders settled and warm
  from first paint.
- **Breakpoints (v2).** ≥1200px: enclosures up to 46% of the measure,
  floated into the sheet's margin side, text wrapping — as a photograph
  laid on the letter. 768–1199px: up to 52%, floated. <768px: full
  measure width, in flow, no float — a phone has no margin to tuck a
  photograph into.
- **Edge cases & failure modes (v2).** *Portrait orientation in a
  landscape frame:* the frame's aspect is set per-enclosure from the
  real image; the deckle mask is aspect-agnostic (an edge, not a box).
  *Multiple enclosures in one letter:* maximum two (§9); they trigger
  independently and never animate concurrently — the second waits for
  the first's 700ms. *Colour-critical image* (a product shot that must
  show true colour): the duotone is lifted for that enclosure only,
  declared in its markup — the exception is visible in the code, never
  silent.
- **Accessibility spec (v2).** Real `alt` text (the photograph's
  subject, not "image"); the handwritten caption is real text in the
  DOM (never baked into the image), read after the alt. Contrast of the
  caption: `--ink` on `--paper`, 11.17:1.
- **Performance budget & mobile variant.** One transform on one image;
  images are `loading="lazy"` below the second letter and sized to the
  frame (no 3000px prints in 400px frames — §14). Mobile: in-flow form
  (above).
- **Tokens consumed (v2).** `--paper`, `--paper-edge`, `--ink`,
  `--ribbon`, `--ease-unfold`, `--ease-warm`.

### 6.12 Folded-blank skeleton + refold transition

- **What & why.** The theme's loading and navigation states are the
  correspondence's own handling. While a bundle loads, the visitor sees
  folded blank sheets — the letters, not yet arrived. On navigation, the
  current letter refolds seal-side out and the next envelope slides in
  from the bundle's stack: post coming and going, handled the way post
  is handled.
- **Structure.** Skeleton: sheet-shaped blocks in `--paper-deep` with
  the chain-line texture (§2) and a fold line (§4), one per expected
  letter (count from the bundle manifest; unknown count → 3 sheets),
  each with a blank seal disc (no monogram — an unarrived letter has no
  author yet). Refold: the current page's first letter reverses §6.2's
  fold (panel turns up, seal-side out) while the page cross-slides
  24px toward the bundle's stack edge; the incoming page's first letter
  arrives folded and performs §6.1's ceremony on landing (its own first
  gesture rules apply — the visitor's *first* gesture on the new page
  may be the scroll that is already happening).
- **Motion spec.** Skeleton sheets unfold one panel each as their real
  letter's content arrives (per-letter, `--dur-fold` 550ms,
  `--ease-unfold`), revealing the arrived letter in its closed state,
  which then follows §6.1/§6.2 normally. A skeleton sheet whose content
  has not arrived after 2500ms stops pretending: it unfolds to a clerk's
  note (§12's empty voice) rather than shimmering forever — this theme
  has **no shimmer anywhere**; blank paper does not sparkle. Refold:
  600ms `--dur-refold`, `--ease-unfold` reversed curve, then the slide;
  total transition ≤900ms, and it disables itself on slow connections
  (Save-Data or effectiveType ≤ 2g → instant navigation).
- **Choreography timeline (v2).** Load: t=0 skeleton bundle shown (3–9
  folded sheets, ribbon tied) → per arrival, that sheet unfolds (550ms)
  to the closed letter → bundle interactive when the first letter has
  arrived; later letters may still be arriving below the fold.
  Navigation: t=0 route change requested → t=0–600ms current first
  letter refolds → t=400ms (overlap) page slides → t=900ms new bundle's
  skeleton-or-letter present; if the new content is cached, its first
  letter is already folded and armed for §6.1.
- **State matrix (v2).** *Rest:* n/a (this element *is* the between-
  states element). *Hover/focus/active:* skeleton sheets are inert and
  removed from focus order (`aria-hidden`, `inert` where supported);
  during refold, focus is held on the page's `<main>` and moved to the
  new bundle's address panel on completion — the one place this theme
  moves focus, because the page itself was replaced. *Scrolled-past:*
  n/a. *Disabled:* JS off — no skeleton (server renders real letters),
  no refold (plain navigation). The skeleton exists only in the
  client-rendered path.
- **Content merge.** The skeleton's sheets are the bundle's own letters
  in their unarrived state — same count, same order, same seals' places.
  The refold handles the letter the visitor was actually reading.
- **Failure fallback.** Content arriving out of order unfolds its own
  sheet and leaves the others folded — order on the page never depends
  on arrival order (sheets are placed by the manifest). A failed fetch
  produces the clerk's note in that sheet's place (§12), with a
  ribbon-thread retry link (§11) — never an infinite fold.
- **Reduced-motion variant.** Skeleton sheets are static folded sheets
  (no unfold — content simply replaces them); navigation is instant,
  no refold. The clerk's-note timeout still applies.
- **Breakpoints (v2).** All sizes identical in behaviour; <768px the
  skeleton bundle shows 2 sheets initially (a phone's viewport holds
  about one letter; promising nine folded sheets above the fold is
  clutter).
- **Edge cases & failure modes (v2).** *Back-button during refold:* the
  transition cancels instantly (popstate wins; a half-refolded letter
  force-settles via the 1200ms law's transition sibling — a 300ms
  settle-to-open). *Prefetched next bundle:* its first letter arrives
  folded and does **not** pre-open; ceremony belongs to arrival.
  *Skeleton on repeat visit with warm cache:* if content is available
  in <300ms, the skeleton never paints (a flash of blank paper is
  worse than a flash of nothing — the bundle area shows desk until the
  first letter lands).
- **Accessibility spec (v2).** The skeleton region carries
  `aria-busy="true"` and a visually-hidden "The bundle is being
  delivered" status; the clerk's-note state is real, focusable content.
  Refold completion moves focus as specced above and the new page's
  title is announced by the route change itself.
- **Performance budget & mobile variant.** Skeleton: pure CSS shapes,
  no images. Refold: transforms on one letter + one page slide, ≤900ms,
  disabled on slow connections (above). Mobile: identical, fewer
  skeleton sheets.
- **Tokens consumed (v2).** `--paper`, `--paper-deep`, `--paper-edge`,
  `--ribbon`, `--ease-unfold`, `--dur-fold`, `--dur-refold`.

---

### 6.13 The address panel (page family: navigation)

- **What & why.** A bundle's navigation is its address: the panel on the
  bundle's face that says who sent it, who it is for, and — in the
  letters' titles set as address lines — what is inside. The visitor
  navigates the correspondence the way a recipient reads an address:
  from the known to the particular.
- **Structure.** A `<nav class="address-panel">` (§6.9's pinned group):
  line 1, the recipient ("For —" + the visitor's role or name, Cormorant
  600 small-caps §3); line 2, the sender ("From —" + the writer); then a
  rule in `--ribbon`; then the letters as address lines — each a link:
  "Nº 3 — The Night the Roof Leaked — LISBON" (number and town in the
  clerk's mono, title in the panel voice). At the panel's foot, the
  clerk's count (§6.3) and the bundle's own seal-mark (decorative,
  drawn §6.5). Links to other bundles (the archive, §7) sit below a
  second rule, set as "Further bundles" — the panel never grows a menu.
- **Motion spec.** The current letter's line carries §6.9's drawn
  underline (300ms `--ease-warm`) as letters open. Hover on a line: the
  town in its postmark position warms to full `--ribbon` from
  `--ribbon-faded` text — no: postmark text is never faded (§3); hover
  instead draws a 1px ribbon thread under the title (left→right, 220ms
  `--ease-warm`). Panel entrance: none — it is on the bundle when the
  bundle is laid down.
- **Choreography timeline (v2).** Per letter-open: t=0 letter lands →
  t=+100ms previous line's underline fades (150ms) → t=+100ms new line's
  underline draws (300ms) → t=+400ms count ticks (§6.3). Hover thread:
  220ms in, 150ms out (threads withdraw faster than they arrive).
- **State matrix (v2).** *Rest:* panel at the bundle's head, letter № 1
  current. *Hover:* thread draw (above); on touch, first tap shows the
  thread, second follows — no: the panel's lines are links to letters
  on the same page; a tap scrolls to the letter and triggers its fold
  if folded (§6.2's focus rule, via scroll). One tap, one action.
  *Focus:* `--ribbon` outline on the line, thread drawn. *Active:*
  `aria-current` line underlined. *Scrolled-past:* after §6.9's release,
  static at the bundle's end position. *Disabled:* static head block.
- **Content merge.** The panel's lines *are* the letters — number, title,
  town — the bundle's table of contents written as its address. Remove
  the panel and the bundle is anonymous; remove a letter and its line
  must go (§10 checks the correspondence).
- **Failure fallback.** Plain list of anchor links; works without CSS
  or JS entirely.
- **Reduced-motion variant.** Underline and thread appear instantly.
- **Breakpoints (v2).** ≥1200px: full panel (§6.9). 768–1199px: lines
  shorten to "Nº 3 — LISBON" with the title in the line's `title`
  attribute and in the letter itself. <768px: the panel becomes the
  page head (§6.9): recipient, sender, and a compact line of letter
  links in the clerk's mono ("Nº1 · Nº2 · Nº3 …") — on a phone the
  address is read, not studied.
- **Edge cases & failure modes (v2).** *Long titles:* address lines
  truncate at two lines with the full title in the letter's own heading
  position (its dateline block) — the panel never wraps a line to three.
  *Nine-letter bundle:* the panel's lines are set at 14px (the panel
  voice's floor) rather than scrolling internally — a bundle's address
  never scrolls.
- **Accessibility spec (v2).** `<nav>` labelled "This bundle of letters";
  `aria-current="true"` on the open letter's line, updated on open
  events. Contrast: `--ink` 11.17:1, `--ribbon` 8.50:1 on `--paper`.
  Focus order: the panel precedes the letters (DOM order), matching
  the reading order of an address before its letters.
- **Performance budget & mobile variant.** Static but for two small
  transitions. Mobile: compact head form (above).
- **Tokens consumed (v2).** `--paper`, `--ink`, `--ribbon`,
  `--ribbon-faded`, `--ease-warm`.

### 6.14 The envelope front (page family: hero composition)

- **What & why.** §6.1 specifies the opening gesture; this element
  specifies what the visitor sees *before* it: the composed first screen
  — a sealed envelope front lying on the desk, the bundle's address
  visible, the ribbon's knot at the margin, and nothing else competing.
  The hero composition's job is stillness with intent: one object, one
  invitation.
- **Structure.** First viewport: the desk (`--desk` in dark mode; in
  light mode the page ground is `--paper-deep` at the desk's distance —
  the desk is out-of-focus paper-toned, never a colour of its own), the
  bundle centred slightly left of the ribbon margin (§4), the envelope
  front (the first letter's closed face, §6.1) bearing: the address
  panel's summary (recipient + sender, §6.13's first two lines), the
  postmark of the first letter (ring + town + date, §6.3), and the seal
  (§6.5) centred on the top fold. Below the fold line of the screen, the
  second letter's seal just shows (§4's density rule). No headline, no
  subhead, no button: the envelope is the hero, and the page's only
  above-the-fold text besides the address is the letter's own dateline
  visible at the envelope's edge.
- **Motion spec.** On load: nothing moves until the visitor's first
  gesture, except §6.5's monogram draw and §6.6's breath. The
  composition's stillness is specified, not accidental: a sealed
  envelope that fidgets is a pop-up. The one exception: after 6s without
  a gesture, the seal's specular (§6.5) warms +6% for 1200ms and
  settles — a single glint, once, the candle catching the wax. It never
  repeats.
- **Choreography timeline (v2).** t=0 load → monogram draws (§6.5,
  ≈680ms) → breath runs (§6.6) → t=6000ms (only if no gesture yet) the
  single glint → first gesture → §6.1's ceremony.
- **State matrix (v2).** *Rest:* as composed. *Hover:* §6.5/§6.8's seal
  responses only. *Focus:* tabbing into the page lands on the address
  panel's first link, then the letter (§6.1's focus trigger). *Active:*
  §6.1. *Scrolled-past:* the composition is gone; the opened letter is
  the page's top. *Disabled:* the letter open and flat heads the page,
  address panel above it — the composition becomes a title block, which
  is what an envelope front is, unfolded.
- **Content merge.** Everything on the envelope front is the first
  letter's own: its address, its postmark, its seal, its date. The hero
  sells nothing but the correspondence itself.
- **Failure fallback.** The disabled state above; a slow network shows
  §6.12's skeleton envelope (folded, blank seal) in this composition —
  same stillness, no glint.
- **Reduced-motion variant.** No glint; the composition is static; the
  letter is open (§6.1), so the "envelope front" is the opened letter
  with the address above it.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: the bundle
  centres (margin narrows, §4). <768px: the envelope fills the first
  viewport's width minus 32px of desk; the second letter's seal does
  not peek (the density rule yields to the phone's height) — the
  composition is one envelope, full stop.
- **Edge cases & failure modes (v2).** *Short viewport (<600px
  height):* the envelope scales its padding down (§4's sheet padding
  compresses to 40px) rather than pushing the seal below the fold — the
  seal must be visible in the first screen at any height (§10 checks
  600px). *Returning visitor mid-session:* the ceremony replays per
  page view (§6.1); the composition is identical.
- **Accessibility spec (v2).** The envelope front's text (address,
  postmark) is real text in DOM order before the letter. The seal's
  text equivalent (§6.1) sits beside the dateline. Landmarks: the
  address panel is the `<nav>`, the letter is `<main>`'s first
  `<article>`.
- **Performance budget & mobile variant.** Static composition; the
  glint is one opacity transition. Mobile: the single-envelope form
  (above).
- **Tokens consumed (v2).** `--paper`, `--paper-deep`, `--ink`,
  `--ribbon`, `--wax-bright`, `--ease-warm`.

### 6.15 Enclosure cards (page family: cards)

- **What & why.** Where the site must present a set of comparable things
  — gift options in a gifting bundle, invitation variants, the letters
  of an archive — they are enclosure cards: small stiff cards of the
  kind tucked into a parcel or a bouquet, each with a deckled edge, a
  clerk's heading, and a hand-written line. A card in this theme is an
  enclosure, not a tile: it was *put in* with something.
- **Structure.** A `<ul class="enclosures">` inside a letter (cards live
  in letters, §6.11's rule) — each `<li>` a card: `--paper` face on the
  sheet's `--paper-deep` shadow, deckle edge on one side (the torn
  side; the other three are cut straight, as enclosure cards are),
  heading in the panel voice (§3), facts in the clerk's mono (price,
  date, count — facts are stamped, not styled), one line in the hand
  (≤14 words, §3), and one ribbon-thread link (§6.13's thread) as the
  card's only action.
- **Motion spec.** Entry: cards are revealed by their owning letter's
  opening — they do not animate separately on scroll (a card revealed
  twice, once by the fold and once by a fade, is a card handled twice).
  Within an opened letter, a card's only motion is hover: lift toward
  the light — translateY −3px and the §6.7 tilt at ≤1.5°, 300ms
  `--ease-warm` — and the hand line warms (§6.7) when the pointer is
  over the card.
- **Choreography timeline (v2).** t=0 owning letter lands open → cards
  already in final position (they were inside the letter) → hover
  timeline is §6.7's lerp. No entry beats exist, deliberately.
- **State matrix (v2).** *Rest:* flat in the letter's grid (2 columns
  ≥1200px within the measure, 1 column <768px). *Hover:* lift + hand
  warmth (desktop). *Focus:* the card's link takes `--ribbon` outline;
  the card lifts as hover. *Active:* the link's thread draws fully.
  *Scrolled-past:* flat. *Disabled:* flat, all content present.
  *Sold-out / past-date state* (a gift option gone, an invitation date
  passed): the card's clerk line is stamped "NO LONGER ENCLOSED" in
  `--ribbon`, the hand line is replaced by the clerk's line, and the
  link is removed — a withdrawn enclosure is marked by the clerk, not
  greyed into illegibility.
- **Content merge.** Each card is a real enclosure in a real letter: the
  gift card inside the gift letter, the variant card inside the
  invitation. The grid is the letter's own enclosure pocket, sized by
  the letter — never a page-level product grid wearing deckles.
- **Failure fallback.** A plain list of headed items with links; the
  deckle is an SVG mask that degrades to a straight edge.
- **Reduced-motion variant.** No lift, no tilt; hand lines at full ink.
- **Breakpoints (v2).** ≥1200px: 2 columns in the measure, gap 24px.
  768–1199px: 2 columns, gap 20px. <768px: 1 column; the deckle side
  alternates left/right down the list (a small bundle-of-cards rhythm)
  — the only place the theme permits alternation as ornament, because
  real enclosure cards in a stack do alternate their torn edges.
- **Edge cases & failure modes (v2).** *One card alone:* it sits at the
  measure's start, never centred — a single enclosure is tucked in, not
  showcased. *Long hand line:* the ration (§3) is enforced at build;
  overflow truncates the *clerk's* facts line before the hand line is
  touched — the hand outranks the stamp. *Card with an image:* it
  becomes a §6.11 enclosure portrait on a card — one image per card,
  duotone, deckle frame.
- **Accessibility spec (v2).** List semantics preserved; the whole card
  is never a link (only its thread link is), so screen-reader users get
  heading → facts → hand line → link in order. Contrast: facts in
  `--ribbon` mono 8.50:1; hand line `--ink` 11.17:1.
- **Performance budget & mobile variant.** Hover transforms only.
  Mobile: single column (above).
- **Tokens consumed (v2).** `--paper`, `--paper-deep`, `--paper-edge`,
  `--ink`, `--ribbon`, `--ease-warm`, `--dur-tilt`.

### 6.16 The reply form (page family: forms / conversion)

- **What & why.** Every bundle ends with the means to write back: the
  reply — an RSVP, a gift order's details, a letter to the storyteller.
  The form is itself the bundle's last letter, addressed the other way:
  the visitor writes on a sheet, in the letter voice, and seals it with
  the writer's seal to send. Conversion in this theme is correspondence
  completed, not a funnel exited.
- **Structure.** A final `<section class="letter letter--reply">`, open
  by default (it was never sealed — it is blank stationery, folded once
  at §6.2's geometry but presented open; its "seal" is the submit
  button, unpressed). Fields are ruled lines on the sheet, not boxes:
  label in the panel voice above a 1px `--paper-edge` rule; the input
  is the line itself (transparent background, Cormorant 21px). Fields:
  name (the visitor signs as this), their direction (email — labelled
  "Your direction", the postal word, with the clerk's mono hint
  "FOR THE REPLY"), the reply body (a textarea of ruled lines, the hand
  *not* used — the visitor types; only their signature field renders in
  Nanum Pen as they type, a small courtesy of the fiction), and the
  seal-button (§6.8): a 76px wax seal bearing the *bundle author's*
  monogram, labelled in text beside it: "Seal and send".
- **Motion spec.** Focus: the field's rule inks from `--paper-edge` to
  `--ribbon` (220ms `--ease-warm`) and the label warms to full `--ink`.
  Error: the rule turns `--wax` — the theme's one lawful use of wax red
  outside a seal, because an error on a letter is marked the way a
  correspondent marks it, in red — and a clerk's note appears in mono
  beneath (§12's error voice). Submit: the seal presses (§6.8's full
  press, 180ms), the sheet's fold shadow deepens as if the letter were
  being folded (400ms), and on success the whole reply letter is
  replaced by the writer's answer (§6.17's sibling state): a short
  letter, already in the bundle, beginning "Your letter is in the
  bundle." with the clerk's postmark of *today's real date* and the
  visitor's own town if they gave it. No spinner exists in this theme;
  while sending (≤ the network's patience), the seal sits pressed at
  0.97 and the sheet is inert — sealing takes a moment.
- **Choreography timeline (v2).** Focus: t=0 rule inks (220ms).
  Submit: t=0 press (§6.8) → t=180ms fold shadow deepens (400ms) →
  response → success letter fades its predecessor at the fold line
  (the one lawful fade in the theme: a letter exchanged for a letter,
  300ms `--ease-warm`) → the header postmark stamps (§6.3) with the
  reply's town: "RECEIVED".
- **State matrix (v2).** *Rest:* blank ruled sheet. *Hover:* seal
  specular +8%. *Focus:* rule inks (above); focus outline is the inking
  rule plus a `--ribbon` 2px outline on the seal-button only (inputs
  show focus by their rule — and §10 verifies a visible focus on every
  field at every size). *Active:* the press. *Scrolled-past:* a filled
  but unsubmitted reply stays filled (no state is lost to scrolling).
  *Disabled:* while sending, fields are `disabled` at full contrast
  (labels stay `--ink`; only the seal dims, §6.8) — a disabled field
  that greys its text below AA is a §10 failure. *Error state:*
  per-field, persistent until corrected; errors never auto-dismiss.
- **Content merge.** The form is the bundle's last letter and says so;
  its fields are the reply's own lines (name = signature, direction =
  return address, body = the letter). The success state is a letter
  back, filed in the same bundle — the correspondence, completed, is
  the confirmation page.
- **Failure fallback.** A working HTML form: labels, inputs, submit —
  posts without JS, errors re-render server-side in the same clerk's
  notes. The seal-button is a `<button type="submit">` whose seal is
  decoration around a real text label.
- **Reduced-motion variant.** No press scale, no fold shadow: the seal
  ring impresses instantly (§6.8), the success letter replaces the form
  without the fade.
- **Breakpoints (v2).** ≥1200px: the reply sheet at the bundle's measure;
  fields in one column (letters are one column) with name/direction on
  one shared ruled line-pair at ≥900px sheet width. 768–1199px: one
  column throughout. <768px: inputs at 21px (also prevents iOS zoom —
  the theme's body size already complies), the seal-button grows to
  84px, and "Seal and send" sits beneath it, centred — on a phone the
  seal is pressed with a thumb, and the layout admits it.
- **Edge cases & failure modes (v2).** *Long reply body:* the textarea's
  ruled lines extend with content (background lines every 33px, §4's
  line unit) up to 12 lines, then it scrolls internally — a letter
  longer than its sheet is the one case the fiction yields to function.
  *Failed send (network):* the reply stays written, the seal unpresses,
  and the clerk notes beneath the seal: "NOT SENT — THE POST FAILED.
  YOUR LETTER IS KEPT BELOW." (§12). Nothing the visitor wrote is ever
  cleared by an error. *Double submit:* the pressed state disables the
  seal until resolution.
- **Accessibility spec (v2).** Every field has a real `<label>`; the
  mono hints are `aria-describedby`, not placeholders (there are no
  placeholders — a blank line is the invitation). Error notes are
  linked via `aria-describedby` and announced by a polite live region
  on submit failure only. Contrast: labels `--ink` 11.17:1; error text
  `--wax` on `--paper` 8.32:1; the seal-button's text label `--ink`.
  Touch targets: fields' ruled lines have 48px hit rows; the seal is
  76–84px.
- **Performance budget & mobile variant.** Transitions on focus/submit
  only; no loops. Mobile: the thumb-seal layout (above).
- **Tokens consumed (v2).** `--paper`, `--paper-edge`, `--ink`,
  `--ribbon`, `--wax`, `--wax-bright`, `--wax-deep`, `--ease-warm`,
  `--ease-press`, `--dur-press`, `--fold-shadow`.

### 6.17 The bundle's end (page family: footer)

- **What & why.** A bundle ends the way it was tied: the ribbon, having
  unwound the margin's whole length, finishes in its knot; beneath it,
  the colophon — who wrote these letters, on what paper, in what year —
  set as the last letter's postscript writ small. There are no link
  columns. A bundle has no sitemap; it has a knot and a name.
- **Structure.** After the reply letter (§6.16): the ribbon tail (§6.3)
  resolves into an SVG knot (two loops, `--ribbon`, drawn once when it
  enters), then the colophon block in the address-panel voice (15px,
  §3): the author's name and the bundle's title, "Written at —" + the
  first letter's town, the year, and the legal line. One line of clerk's
  mono closes the page: "END OF THE BUNDLE — Nº OF LETTERS: 7" (the
  true count). A single "Further bundles" link (§6.13) may sit above
  the knot, as the archive's direction.
- **Motion spec.** The knot draws (dashoffset, 600ms `--ease-warm`) as
  it enters at 80% viewport height — the last draw of the page, rhyming
  with the first monogram (§6.5). Nothing else in the footer moves; the
  breath (§6.6) does not extend past the last letter (the candle is
  behind the reader now).
- **Choreography timeline (v2).** t=0 knot enters 80% line → t=0–600ms
  knot draws → colophon is static throughout.
- **State matrix (v2).** *Rest/hover/focus/active:* the "Further
  bundles" link behaves as §6.13's lines (thread draw on hover/focus).
  *Scrolled-past:* n/a — it is the end. *Disabled:* knot rendered drawn.
- **Content merge.** The knot is the ribbon the visitor has been
  following since the first letter — the progress indicator ties itself
  off. The colophon's facts are the bundle's real facts.
- **Failure fallback.** Static knot (SVG rendered drawn by default;
  JS arms the draw), static colophon.
- **Reduced-motion variant.** Knot pre-drawn.
- **Breakpoints (v2).** All sizes: the colophon column matches the
  letter measure; <768px the knot centres above the colophon (the
  ribbon has been on the paper's edge, §6.3, so it ends on the paper).
- **Edge cases & failure modes (v2).** *Bundle without a reply form:*
  the knot follows the last letter directly — the footer never depends
  on §6.16 existing. *Author deceased / archive bundle:* the colophon
  voice adjusts ("Kept by —") per §12; the structure does not change.
- **Accessibility spec (v2).** The knot SVG is `aria-hidden`; the
  colophon is a `<footer>` with real text; the letter count duplicates
  §6.3's clerk count.
- **Performance budget & mobile variant.** One 600ms draw, once.
  Mobile: centred knot (above).
- **Tokens consumed (v2).** `--ribbon`, `--ribbon-faded`, `--ink`,
  `--paper`, `--ease-warm`.

### 6.18 The undelivered letter (page family: 404)

- **What & why.** A wrong address in this theme is an undelivered
  letter: returned to sender, stamped, its address line struck by the
  clerk. The 404 page is a letter that could not be delivered — the one
  letter in the bundle nobody wanted to write.
- **Structure.** A single sheet, presented open (an undelivered letter
  is not sealed — it was opened by the post office of the fiction): the
  clerk's stamp at the top in `--ribbon` mono — "RETURNED TO SENDER —
  NO SUCH ADDRESS" — the requested path set as the letter's address
  line in the panel voice, struck through once in `--wax` (the clerk's
  red, lawfully used: something is being corrected), and beneath, in
  the letter voice, two or three lines from the writer (§12's empty
  voice) and the ribbon-thread link back to the bundle's address panel
  (§6.13) — the way home.
- **Motion spec.** One motion only: on load, the clerk's stamp presses
  (§6.8's press, ring and all, 180ms) beside the address line — the
  letter arrives already returned, and the stamp is its delivery. No
  fold, no crack: this letter's ceremony is refusal.
- **Choreography timeline (v2).** t=0 page painted, stamp parked →
  t=250ms stamp presses → t=430ms settled; the page is still thereafter.
- **State matrix (v2).** *Rest:* stamped, still. *Hover/focus:* the
  home link's thread (§6.13). *Active:* the stamp does not re-press.
  *Scrolled-past:* n/a (one screen). *Disabled:* stamp rendered pressed
  (ring present) statically.
- **Content merge.** The struck address is the actual requested path;
  the stamp's wording is the actual situation. Nothing decorative is
  added — no illustration of a lost letter, no mascot postman (§9).
- **Failure fallback.** It is a static page with a link; there is
  nothing to fail.
- **Reduced-motion variant.** Stamp pre-pressed.
- **Breakpoints (v2).** The sheet takes the standard measure at all
  sizes; <768px the stamp sits above the address line instead of beside
  it.
- **Edge cases & failure modes (v2).** *A path that almost matches a
  letter:* the clerk adds a mono line — "NEAREST IN THIS BUNDLE: Nº 3"
  with its thread link — only when the match is real (slug similarity
  computed server-side); a guessed suggestion is forbidden (§9's
  invented-facts rule).
- **Accessibility spec (v2).** The page's `<h1>` is the writer's line
  ("This letter could not be delivered"), not the stamp — screen
  readers meet the meaning first, the theatre second. The struck path
  is wrapped so it is read as "address attempted:" + path, with the
  strike presentational.
- **Performance budget & mobile variant.** One 180ms press. Mobile:
  stamp repositioned (above).
- **Tokens consumed (v2).** `--paper`, `--ink`, `--ribbon`, `--wax`,
  `--ease-press`, `--dur-press`.

---

## 7. Page application map

**Home — the bundle itself.** The page *is* one bundle: address panel
(§6.13), 3–9 letters (§6.1 first, §6.2 the rest), reply letter last
(§6.16), knot and colophon (§6.17). Most Vellum & Wax sites are a single
bundle deep; depth is added by archives, not by sub-pages of chrome.

**The invitation (wedding/event).** Letter 1: the invitation itself —
names, date, place are the letter's body, the date in the clerk's
postmark from the *venue's* town (the postmark belongs to the letter's
story, §1's law). Letter 2: the order of the day. Letter 3: travel and
lodging, with §6.11 enclosures of the house or the coast. Letter 4:
enclosure cards (§6.15) for the gift list. Last: the reply (§6.16) as
the RSVP — its fields are the RSVP's questions, its seal-button the
acceptance. One bundle per event; a second event is a second bundle.

**The gift announcement / luxury product letter.** Letter 1: the
announcement, sealed with the brand's monogram. Letter 2: provenance —
materials, maker, the workshop's town as postmark. Enclosures: the
product portrait (§6.11, duotone lifted only if colour is the product's
truth, declared per §6.11). The reply form takes the order's details —
it is a letter of commission, and its success state (§6.16) is the
house's letter of acknowledgement with a real date.

**The letter-form journal / newsletter archive.** Each essay is a bundle
of one letter plus its reply (comments are not supported by the fiction;
replies are letters — a moderated selection may be bound as a following
bundle, "Letters in reply"). The archive page is a *post room*: bundles
listed as address panels (§6.13) stacked — each entry shows sender,
recipient, the letter's title-line, its postmark, and its seal drawn —
never a card grid of thumbnails. Entry opens the bundle with §6.12's
refold.

**The storyteller's about page.** One bundle: "How I came to write
letters" — the writer's own story in 3–4 letters, portraits enclosed
(§6.11), the reply form as the contact means. The about page that is not
in this theme's voice (a résumé grid) breaks the site; if the client
needs a résumé, it is enclosed as a clerk's document inside a letter,
framed as such.

**Checkout equivalents.** There is none beyond §6.16. A purchase that
needs a cart, options matrix, or payment form leaves the theme at that
step: hand off to a plainly-designed transactional flow and return to a
Vellum & Wax confirmation letter (the acknowledgement pattern of §6.16).
Pretending a payment form is a letter is the theme's most dangerous
costume (§9).

**The undelivered letter (404).** §6.18, everywhere, unchanged.

---

## 8. Worked examples

### 8.1 The hero — a wedding invitation's first letter

*The commission: a wedding invitation site; the couple write as one
sender. The first letter is the invitation.*

- **The composition (§6.14).** First screen: desk, bundle, envelope
  front. The address reads "For — The Friends and Family of Both Houses"
  / "From — A. & J." The postmark ring: "GRANADA — 14 JUNE" (the venue's
  town, the wedding's date — the letter's own story). The seal bears the
  intertwined A·J monogram (§6.5), which draws over 680ms as the page
  loads. The breath (§6.6) runs at ±3%. At 6s, if the guest has not yet
  touched anything, the seal glints once.
- **The ceremony (§6.1).** The guest scrolls 40px. t=0 crack strains;
  t≈310ms the wax gives; two halves part to ±12°; five shards fall and
  are gone by t=600ms. The top panel began turning at t=120ms; at
  t=820ms it lies flat, revealing the dateline — "Granada, the first of
  May" (the *writing* date, in the letter voice, distinct from the
  postmark's posting date — both real, both shown, §12) — and the
  salutation. The mid panel lands at t=980ms: the body — the invitation
  itself, names, day, hour, place, set in 21px Cormorant at a 38ch
  measure.
- **The close (§6.4).** At t=1180ms the joint signature — both names in
  one hand, 30px Nanum Pen, rotated −3° — warms from pale to full ink by
  t=1630ms. The postscript warms at t=1830–2280ms: "P.S. The reply is
  the last letter in this bundle. We keep them all." The header postmark
  stamps GRANADA at t=1400ms; the clerk reads "LETTER Nº 1 OF 5".
- **Scroll timeline.** 0–40px: the trigger. 40–900px: the guest reads
  letter 1; the ribbon (§6.3) has unwound ~15% of the margin; letter 2's
  seal sits at the screen's foot, its monogram drawing as it enters.
  The pinned panel (§6.9) holds the address at the margin. Nothing else
  moves. The guest who never scrolls has still received the invitation
  entire — the hero letter is complete in the first screen once opened.

### 8.2 Mid-page — the provenance letter of a gifting house

*The commission: a perfume house's gift letter; letter 3 of 5 is
provenance, with two enclosures.*

- **Entry (§6.2).** The letter's folded face shows its credentials:
  dateline "Grasse, the ninth of October", postmark GRASSE, seal whole.
  Its seal crosses the 62% line; at t=60ms the top panel lifts; the seal
  rides the panel and comes to rest, whole, at the sheet's top-left
  margin at t=610ms. The ribbon join from letter 2 draws at t=760–1260ms
  (§6.10).
- **The enclosures (§6.11).** Mid-letter, the first enclosure — the
  still-room photograph, duotone, deckle frame, the writer's caption in
  the hand: "the still room, before the first distillation" — crosses
  the 70% line at scroll ≈55% of the letter; it settles 1.05→1 over
  700ms, warming as it lands. The reader's pointer crosses the caption;
  the caption sharpens (§6.7): blur lifts, ink deepens toward
  `--ink-warm` over ~250ms, and holds while they read it. The second
  enclosure (the harvest) waits until the first has settled — enclosures
  are taken from the envelope one at a time.
- **The close (§6.4, §6.15).** The letter ends with two enclosure cards:
  the two gift formats — clerk's facts (volume, price, "READY BY THE
  FIRST OF DECEMBER") and one hand line each ("for the one who still
  writes letters"). The signature warms last, as always. The clerk ticks
  "LETTER Nº 3 OF 5"; the postmark re-stamps GRASSE.
- **What the visitor feels.** A letter opened without fuss, a photograph
  taken out and looked at closely — the warmth under their pointer is
  the candle leaning in — and the facts, when they want them, stamped
  plainly by the clerk. Nothing on the page asked for attention; two
  things rewarded it.

### 8.3 Conversion — the reply letter (RSVP)

*The commission: §8.1's invitation bundle; its last letter is the reply.*

- **Arrival.** The reply sheet is presented open (§6.16) — blank
  stationery, its heading in the writer's voice: "Write back." The
  fields are ruled lines: the guest's name, their direction, acceptance
  (a clerk's pair of lines — "I WILL COME" / "I CANNOT COME" — chosen
  by filling the line, set as two radio lines in the panel voice, the
  chosen one's rule inking `--ribbon`), number of seats, and the reply
  body on ruled lines.
- **Interaction timeline.** The guest tabs to the name field: its rule
  inks `--paper-edge → --ribbon` over 220ms. They mistype the direction
  (no @): on blur, the rule turns `--wax` and the clerk notes beneath,
  in mono: "THE DIRECTION WILL NOT CARRY — CHECK THE ADDRESS." They
  correct it; the note clears, the rule returns to `--ribbon`. Their
  signature field renders their typed name in Nanum Pen as they type —
  the fiction's courtesy — and warms under their pointer (§6.7) as they
  review it.
- **The sealing.** They press the seal-button (§6.8): t=0 press begins,
  t=90ms full compression, the specular flares, the ring impresses;
  t=180ms settled, the sheet's fold shadow deepening over 400ms as the
  letter "folds". The seal holds at 0.97 while the post goes. At
  response, the reply is exchanged (300ms fade, §6.16) for the couple's
  letter: "Your letter is in the bundle." — postmarked with today's
  real date and the stamp "RECEIVED", signed by both, with a postscript
  naming the seats they asked for. The header postmark stamps RECEIVED;
  the clerk's count closes: "LETTER Nº 5 OF 5 — THE BUNDLE IS COMPLETE".
- **Failure rehearsed.** If the post fails, the guest's letter remains
  on the sheet, word for word; the clerk notes "NOT SENT — THE POST
  FAILED. YOUR LETTER IS KEPT BELOW." and the seal unpresses, ready to
  press again. The guest never re-writes an RSVP because a network
  blinked (§10, blocking gate 7).

---

## 9. Anti-slop — what makes THIS theme look cheap

1. **The costume bundle.** "Letters" that are really feature lists, with
   invented dates and towns the writer never saw. *Cure:* §1's law —
   real sender, real date, real town, or refuse the theme. The postmark
   audit (§10, gate 1) reads every stamp against the content.
2. **Ceremony everywhere.** Every letter cracking a seal, every section
   unfolding twice. The theme's manners are its meaning: full ceremony
   once, fold-downs after (§6.2). *Cure:* one crack per bundle view —
   the first letter's. Later seals stay whole (§10, gate 4).
3. **The re-sealing seal.** A seal that heals and re-cracks on every
   hover or revisit to farm the animation. *Cure:* cracked is a terminal
   state per page view (§6.1); the monogram may glint once (§6.14),
   never re-perform.
4. **Handwriting as a font.** Nanum Pen setting paragraphs, buttons, or
   navigation. *Cure:* §3's ration — signatures, postscripts, captions,
   ≤14 words at a time; the gate counts hand-set words per letter.
5. **Breathing you can see.** A candle breath above ±3% (±5% dark) reads
   as a pulsing overlay — a screensaver on a letter. *Cure:* the
   amplitude is a token, not a taste (§6.6); §10 measures it.
6. **Wax red spent on furniture.** Red links, red badges, red sale
   bursts. Wax is ceremony: seals, the crack, the press ring, the one
   error rule (§6.16). *Cure:* the palette's usage ratios (§2) are
   checked in the gate; wax above ~3% of a screenshot's pixels fails.
7. **Flat paper.** `#F1EAD8` without chain lines is card stock; a
   "letter" without creases after opening is a web card. *Cure:* §2's
   texture is part of the colour's definition; §4's crease lines persist
   after opening.
8. **The fold that hides.** Content that exists only after animation, or
   a ceremony that can be missed and leave a hero sealed forever.
   *Cure:* the 1200ms law and the scrolled-past rules (§6.1/§6.2);
   §10's JS-off and broken-trigger tests.
9. **Counters that lie.** A bundle count that doesn't match the letters,
   a postmark town that isn't the opened letter's, a "letters opened"
   figure that runs on load. *Cure:* the clerk counts events, not
   impressions (§6.3); §10 reconciles the numbers against the DOM.
10. **The doll's-house phone.** Tilt, hover warmth radii, and pinned
    margins shrunk onto a handset. *Cure:* §6.7/§6.9's mobile rulings —
    the phone is the hand holding the paper; the paper does not also
    pretend to be held.
11. **A payment form in a costume.** Checkout fields on ruled lines with
    a seal-button taking card details. *Cure:* §7's handoff rule — the
    theme ends where the transaction begins and resumes at the
    acknowledgement letter.
12. **Dust everywhere.** Motes outside the hero, sparkle on seals,
    shimmer on skeletons. *Cure:* motes live in §6.6's hero light only;
    this theme has no shimmer anywhere (§6.12); wax glints once (§6.14).

---

## 10. Quality gate

A build may not ship in this theme until every **blocking** item passes
and at least 9 of the 11 **standard** items pass. The reviewer checks
evidence — a JS-off load, a broken-trigger simulation, the DOM — not
intentions.

**Blocking — all must pass.**
1. **Postmark truth audit:** every letter carries a real date and a town
   that belongs to its story; every counter figure on the page reconciles
   with the DOM (bundle count = letters present; opened count = letters
   opened). One invented stamp or figure fails the build.
2. **JS-off test:** with JavaScript disabled, every letter renders open
   and flat, fully readable in order, seals pre-cracked (first) or whole
   at margins (later), the reply form submits, the footer count is true.
3. **Broken-trigger test:** with animation triggers disabled, the 1200ms
   watchdog force-opens every letter; no letter remains folded, no
   signature remains stranded at `--ink-pale`, no content is unreachable.
4. **One-ceremony test:** exactly one seal cracks per bundle view (the
   first letter's); no seal re-cracks on scroll-back, hover, or revisit
   within the view; later seals remain whole.
5. **Reduced-motion test:** with `prefers-reduced-motion`, letters are
   open and flat, signatures at full ink, the ribbon static at full
   length, no breath, no motes, no tilt, no press scale — and the page
   loses no information.
6. **Hand ration test:** Nanum Pen Script sets only signatures,
   postscripts, captions, and the reply signature field; no run exceeds
   ~14 words; no body text, label, or navigation is hand-set.
7. **Reply integrity test:** a failed send preserves the visitor's text
   verbatim and shows the clerk's not-sent note; a successful send's
   confirmation carries a real date. The form works with JS disabled.
8. **Cursor & cover audit:** the system cursor is unchanged everywhere;
   no animated element (panel, shard, ribbon tail, tilt) overlaps or
   covers text at any scroll position — checked at five scroll depths.
9. **Contrast audit:** letter text ≥ 11:1 measured; postmark *text* at
   full `--ribbon` (≥8.5:1); `--ink-pale` appears only as a transient
   (≤650ms) or under the watchdog's guarantee; wax-red coverage ≤ ~3%
   of a full-page screenshot.

**Standard — at least 9 of 11.**
10. Ceremony timing: crack → both panels flat within 1.0–1.5s; signature
    warm begins 200ms after landing; total hero sequence ≤2.3s including
    a two-postscript letter.
11. One shared rAF loop (lerp 0.12) drives ribbon, parallax, triggers,
    and warmth; no frame over 20ms attributable to theme code during a
    full-page scroll on a mid-range Android device.
12. Ribbon asymmetry holds: ribbon rewinds on scroll-back; postmark and
    opened-count never decrease.
13. Fold discipline: ≤2 folds concurrent during fast scroll; letters
    open strictly in bundle order; short letters (< one panel) take no
    fold.
14. The breath measures ≤±3% opacity (≤±5% dark mode); motes ≤9, hero
    only, paused off-screen.
15. Chain lines present on every sheet at the §2 opacities; crease lines
    remain visible on every opened letter.
16. The seal is visible in the first screen at a 600px-high viewport;
    Display type appears once (the first letter's opening line).
17. Dark mode darkens the desk, never the letters: sheets measure
    `--paper`/`--ink` in both modes.
18. Print stylesheet: `@media print` renders every letter open and flat
    on white, seals as drawn monograms, no ribbon scrub, no panel —
    the bundle prints as the letters it is.
19. The reply form's fields show a visible focus state at every
    breakpoint, and disabled-while-sending fields keep AA text contrast.
20. The five-second test: a first-time viewer describes the page as
    *a bundle of letters, opened by hand* — not "vintage", not
    "wedding-y", not "a paper theme".

**Minimum bar, in one line:** a build that passes the blocking nine has
earned the right to be judged on ceremony; a build that also clears the
standard list *and* makes a reviewer say the §1 sentence — *sealed,
entrusted, opened, read, signed* — out loud is a Vellum & Wax. Anything
less is stationery clip-art, and it goes back to the desk.

---

## 11. Component inventory

Every component a real site in this theme needs, with its themed
treatment. A component not listed here does not get invented in another
theme's language — it is built from the nearest listed relative.

- **Primary action (the one per bundle):** the seal-button (§6.8/§6.16)
  — a wax seal with a text label beside it. One per page, at the reply.
  There is no other primary button in the theme.
- **Secondary buttons:** there are none as buttons. Secondary actions are
  **ribbon-thread links**: text with a 1px `--ribbon` thread that draws
  under on hover/focus (220ms `--ease-warm`, §6.13). If an action cannot
  be a link or the seal, it does not belong on the page.
- **Text inputs:** ruled lines (§6.16) — label above in the panel voice,
  1px `--paper-edge` rule, Cormorant 21px input text, 48px hit row.
- **Textarea:** ruled lines every 33px (§4's line unit), extending to 12
  lines then scrolling (§6.16).
- **Radio / choice lines:** the reply's choice pairs (§8.3) — panel-voice
  lines; the chosen line's rule inks `--ribbon` and a small clerk's tick
  (mono "✓" is forbidden — the tick is a drawn ribbon stroke, 2px, at the
  line's left) marks it. Checkboxes do not exist; a letter asks one
  question with ruled answers, or it asks in prose.
- **Selects:** forbidden. A bundle never asks a question with more
  answers than fit on ruled lines; if it must (a country list for the
  direction), the field is a text input with the clerk's hint — the
  fiction yields, plainly, rather than dressing a dropdown as paper.
- **Tables:** a letter may contain a *bill of particulars* — an order of
  the day, a price list, a programme. Set as ruled rows on the sheet:
  no boxes, row rules in `--paper-edge`, figures in the clerk's mono
  (tabular), the total row ruled in `--ribbon`. A table never leaves
  its letter.
- **Badges / stamps:** the clerk's stamps — postmarks (§6.3), "RECEIVED",
  "NO LONGER ENCLOSED" (§6.15), "RETURNED TO SENDER" (§6.18). A stamp is
  mono, `--ribbon` (or `--wax` only when something is corrected/refused),
  ringed or ruled, and always *true*: it records an event that happened
  on the page.
- **Alerts:** the clerk's notes (§6.16) — mono lines beneath the thing
  they concern, in the §12 voice. No banners, no toasts: a bundle does
  not interrupt its reader; notes wait where they belong.
- **Toasts:** forbidden. See alerts.
- **Modals:** forbidden. A bundle has no overlays; a needed aside is a
  postscript, a needed confirmation is a letter (§6.16's success).
- **Tabs:** forbidden. Correspondence is sequential; §6.3's ribbon is the
  only "where am I" device.
- **Accordions:** the fold itself (§6.2) is the theme's expansion —
  letters open; nothing else accordions. An FAQ is a bundle of short
  letters, each sealed by its question as its address line.
- **Pagination:** bundles paginate as bundles: the archive (§7) lists
  address panels; within a bundle there is no pagination, only the
  ribbon.
- **Search:** forbidden inside a bundle. An archive large enough to
  search gets a clerk's index page — a plain ruled list with a mono
  input — outside the bundle fiction, labelled as the index it is.
- **Breadcrumbs:** the address panel (§6.13) is the breadcrumb: sender,
  recipient, letter number. No other trail exists.
- **Progress:** the ribbon (§6.3) and the clerk's count. Nothing else.
- **Loading:** folded-blank sheets (§6.12). No spinners, no shimmer.
- **Images:** enclosures (§6.11) — duotone, deckle frame, hand caption.
- **Dividers:** fold lines and ribbon joins (§6.10) divide; a decorative
  horizontal rule that is neither is not permitted.
- **The visitor's signature field:** the one input that renders in the
  hand (§6.16) — typed text displayed in Nanum Pen 30px as it is typed.

---

## 12. Content & copywriting voice

Three voices, matching §3's three hands. Nothing on the page speaks in a
fourth.

**The letter voice (the writer, Cormorant).** Personal, dated, addressed.
Headlines do not exist; letters begin with a dateline and a salutation.
- Dateline: "Granada, the first of May" — place, then date, in words.
  Never "May 1" in the letter voice; the clerk handles numerals.
- Salutation: to the actual reader — "Dear friends of both houses," /
  "My dear Aunty,". A letter that begins "Welcome to our website" has
  failed before its second line.
- Body: full sentences, the writer's own rhythm; one idea per paragraph;
  the letter says *I* and *we* and means specific people.
- Closing: a real closing — "Ever yours," / "With love and wax," — then
  the signature (§6.4). "Regards, The Team" is forbidden: teams do not
  write letters; people do.
- Postscripts carry the afterthought and the invitation: "P.S. The reply
  is the last letter in this bundle. We keep them all."

**The clerk's voice (mono, uppercase, stamped).** Facts only: numbers,
towns, dates, states. The clerk never persuades, never apologises, never
exclaims.
- Counts: "LETTER Nº 3 OF 7" · "THE BUNDLE IS COMPLETE".
- Stamps: "RECEIVED" · "RETURNED TO SENDER — NO SUCH ADDRESS" ·
  "NO LONGER ENCLOSED".
- Hints: "FOR THE REPLY" · "ENCLOSURE MISSING — DESCRIBED IN THE LETTER".

**Error voice (the clerk, correcting).** An error is a direction that
will not carry: state the failure as a postal fact and say what to do,
in one line.
- ✓ "THE DIRECTION WILL NOT CARRY — CHECK THE ADDRESS."
- ✓ "NOT SENT — THE POST FAILED. YOUR LETTER IS KEPT BELOW."
- ✗ "Oops! Please enter a valid email address." (No "oops", no
  exclamation, no "valid" — the clerk is not a form.)
- ✗ "Something went wrong." (The clerk says *what* went wrong.)

**Empty-state voice (the writer, briefly).** An empty bundle, an archive
with nothing in it yet: the writer says so in the letter voice, on a
sheet, dated — "No letters yet. The first is being written." — never a
clerk's stamp (nothing has happened to stamp) and never an illustration
of an empty mailbox.

**Label voice (the panel voice).** Form labels are the letter's own
phrases: "Your name, as you sign it" · "Your direction" · "Your reply".
Buttons: the seal's label is a verb of sealing — "Seal and send" — never
"Submit", never "Send now →" (the clerk does not use arrows; the writer
does not shout).

**Banned words and constructions.** "Welcome to…", "Don't miss out",
"Limited time", "Click here", "Submit", "Oops", exclamation marks
anywhere on the page (a letter may contain one in quoted speech, in the
body, if the writer truly wrote it — the chrome may contain none), and
any date or town that is not true (§1's law).

---

## 13. Full-page scroll choreography map

A home bundle of five letters plus the reply, read top to bottom. Every
beat in order; anything not listed does not move.

1. **Load.** Desk and bundle still. The first letter's monogram draws
   (§6.5, ≈680ms). The breath (§6.6) is running at ±3%. The ribbon shows
   its knot; the clerk reads the bundle's count, opened 0.
2. **First gesture (scroll ≥40px / click / focus).** §6.1's ceremony:
   crack (500ms), shards (600ms), two panels flat by ≈980ms. The candle
   does not react. Dust motes begin their slow fade-in inside the opened
   hero.
3. **The signature lands.** t≈1180–1630ms: the signature warms (§6.4);
   the postscript follows to ≈2280ms worst case. The header postmark
   stamps the first town at t=1400ms (§6.3).
4. **Reading letter 1.** The ribbon unwinds 1:1 with lerped scroll; its
   tail begins to curl. The address panel pins (§6.9) once the bundle's
   top passes 32px. Chain lines lag at 0.92×. The reader's pointer
   crossing the postscript warms it (§6.7).
5. **Letter 2's presentation.** Its seal enters; the monogram draws
   (600ms). The letter sits folded, credentials showing.
6. **Letter 2 opens.** Seal crosses 62%: fold-down lands at ≈610ms
   (§6.2); the ribbon join from letter 1 draws (500ms, §6.10); signature
   warms; postmark re-stamps letter 2's town; clerk ticks Nº 2. Address
   panel's underline moves to line 2.
7. **Letters 3–5 repeat beat 6** with their own content beats: an
   enclosure settles (§6.11) where a letter carries one; enclosure cards
   are simply *there* when their letter opens (§6.15); a letter over 900
   words takes its second fold (two 550ms turns).
8. **The reply letter.** Presented open. Focus inks rules (§6.16); the
   visitor's signature renders in the hand as they type; the seal-button
   waits, specular at rest.
9. **The sealing.** Press (180ms, §6.8), fold shadow deepens (400ms),
   the answer letter is exchanged in (§6.16), postmark stamps RECEIVED,
   clerk closes the count.
10. **The bundle's end.** The ribbon tail, fully unwound, resolves into
    its knot, which draws once (600ms, §6.17). The colophon sits beneath.
    The breath stops at the last letter's foot — below it, the desk is
    still and dark-er by one shade of attention. The page ends the way
    the bundle ends: tied off, signed, counted.

*Scroll-back, at any point:* the ribbon rewinds; nothing else reverses.
Opened letters stay open, stamps stay stamped, warmth stays where it
landed. The map is a ratchet with a silk progress line — which is to say,
it is a record of reading.

---

## 14. Whole-page performance budget

**Asset weight (per bundle page).**
- Fonts: Cormorant Garamond (500, 600 + italics) and Nanum Pen Script
  subset to the bundle's actual hand-set words where the build allows;
  Courier Prime (400, 700). Total font payload ≤ 120KB woff2. The hand's
  subsetting is lawful because §3 rations its words — subsetting body
  text would not be.
- Images: enclosures only, ≤ 160KB each at frame size, ≤ 3 per bundle
  page; total page weight ≤ 900KB on first load.
- JS: the shared loop, fold triggers, and form behaviour ≤ 18KB gz. The
  theme needs no framework on the page to open letters.
- SVG: seals, monograms, joins, knot, deckle masks — inline, ≤ 12KB
  total per page; the deckle mask is generated once and reused (§6.11).

**Frame budget.** One rAF loop (§5), lerp 0.12. Per frame at full
scroll: ribbon dashoffset (1 write), chain-line parallax (≤9 sheet
backgrounds, transform-only via background-position on the texture
layer — or, cheaper, the sheets' texture layers translate as one
composited layer per sheet), warmth (≤5 custom-property writes, only
while the pointer is over the bundle), fold triggers (geometry reads
cached per frame, ≤9 comparisons). Ceiling: 2ms of theme JS per frame;
no frame over 20ms attributable to theme code in a full-page scroll on
a mid-range Android (checked in §10, item 11).

**Long tasks.** None over 50ms after first paint. The ceremony (§6.1) is
compositor transforms; font loading is the only permitted long-task
risk, and it is mitigated by `font-display: swap` with the ceremony
explicitly allowed to start before the hand arrives (§6.1/§6.4).

**Cut order — when the budget is exceeded, cut in this order, and never
skip a step:**
1. Dust motes (§6.6) — gone entirely.
2. The candle breath (§6.6) — frozen at base opacity (static warmth
   kept).
3. The ribbon tail's curl morph (§6.3) — tail shows its final curl;
   length still scrubs.
4. Chain-line parallax — texture locks to the sheets (0.92× → 1×).
5. Letter tilt (§6.7) — warmth remains; sheets stay flat.
6. The §6.14 glint — the seal simply waits.
**Never cut:** any fold or its fallback, the signature warm (it is a
colour transition and costs nothing), the ribbon's length scrub, the
clerk's counts, the reply form's behaviour, or any reduced-motion
variant. Ceremony (§6.1) is cut *last* of all motion and only on
devices that cannot hold its frame budget — and on such a device the
letter opens with the fold alone, crack pre-played, per §6.1's
scrolled-past abbreviation.

**Print.** `@media print`: all letters open and flat, paper white, chain
lines off, seals as drawn monograms in `--wax`, no panel, no ribbon —
the bundle prints as its letters (§10, item 18).

---

## 15. Build-order checklist

Build in this order; each step is checkable before the next begins.

1. **Content first:** collect the real letters — sender, recipient,
   dates, towns, signatures, postscripts. No letter, no build (§1).
   Verify every postmark against its letter's story.
2. **The sheets:** laid-paper texture (chain lines at §2's opacities),
   sheet geometry, fold lines and creases (§4), the desk, the bundle
   shadow. Static, JS-off, fully readable — the theme already works.
3. **Typography:** the three hands at §3's scale and rations; datelines
   and postmarks in place; the hand ration checked by eye and by count.
4. **The address panel & clerk:** navigation (§6.13), counts as real DOM
   text, postmark ring SVG (§6.3) in its unstamped state.
5. **The seals:** seal SVG with specular and groove-state monograms
   (§6.5); monogram path count ≤4 per author; seals placed on every
   letter.
6. **The folds, static-armed:** panels and clip geometry for §6.1 (two
   folds) and §6.2 (one fold), with CSS defaults OPEN; the JS arming
   that closes them only when the loop is alive; the 1200ms watchdog.
7. **The shared loop:** lerp scroll, fold triggers at 62%, the
   scrolled-past force-open rules, the ≤2-concurrent fold queue.
8. **The ceremony:** crack, shards, panel choreography (§6.1) against
   the timeline; then §6.2's fold-down and §6.10's joins.
9. **The warmth systems:** signature warm sequences (§6.4) with their
   watchdog; hover warmth and tilt (§6.7) with the focus and touch
   states; the two systems' composition rule (§6.7) verified.
10. **The ribbon:** length scrub, tail curl, postmark re-stamping,
    clerk ticks on open events (§6.3); scroll-back asymmetry tested.
11. **Ambience:** the breath at measured amplitude, hero motes (§6.6),
    the §6.14 composition and its single glint.
12. **Enclosures & cards:** deckle mask generated once; duotone;
    §6.11 triggers serialised; §6.15 cards inside their letters.
13. **The reply:** ruled fields, focus inking, error notes in the
    clerk's voice, seal-button submit (§6.8/§6.16), the success letter
    with a real date, the failed-send rehearsal.
14. **The end matter:** knot and colophon (§6.17), the 404 (§6.18),
    skeleton and refold (§6.12) if the build is client-rendered.
15. **Dark mode:** the candlelit desk (§2) — desk darkens, letters do
    not; breath at ±5%; contrasts re-measured.
16. **The gate:** §10 in full — JS-off, broken-trigger, one-ceremony,
    postmark truth, hand ration, reply integrity — with evidence, not
    intentions. Then, and only then, the five-second test with a
    first-time viewer.
