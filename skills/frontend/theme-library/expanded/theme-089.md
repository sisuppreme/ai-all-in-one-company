# 89. Custodian of the Orbit — Expanded (v1 + v2)

> Space debris tracked like a night janitor's rounds — 34,000 dead
> objects, one ledger, one person who knows where every one of them
> is. Orbital hygiene given a face, a clipboard, and a flashlight.
> The page is not a dashboard. It is a round: a walk through zones,
> in order, with a checklist that fills in by hand as the walk
> proceeds, and a beam that does its patrol whether or not anyone
> is watching.

**The theme's one law: the ledger never rounds, and nothing stays
in the dark.** Every total printed anywhere on the page traces to
one declared catalogue record (§6.4) and stops at its exact,
unrounded figure — 34,127, never "34K". And the flashlight beam is
a courtesy, never a curtain: the board ships fully lit and fully
printed, and every dark or hidden state is an enhancement the
script arms over finished content, each with a named watchdog. A
build that rounds a total, or that leaves an object invisible
because an animation did not run, has broken the law twice.

---

## 1. Concept & world

There are more than thirty-four thousand dead objects in Earth
orbit — spent rocket bodies, silent satellites, fragments of
collisions nobody witnessed — and somebody has to know where all
of them are. Not a control room. Not a wall of screens. In this
theme's world, that somebody is a custodian: one person, one
clipboard, one flashlight, walking the same round every night,
checking each zone against the ledger, ticking items off in
pencil, and writing "RE-CHECK TOMORROW" beside the ones the data
won't settle. The page adopts his working surfaces wholesale: the
clipboard (buff board, clip at the top, ring-holes down the side,
carbon-paper duplicates under every note), the dark field he
shines his light into (a near-black sky of tiny tracked points),
and the pencil (graphite strokes, self-drawing check marks, notes
in a typewriter face because the ledger predates the database).

The emotional register is quiet competence at 3 a.m. Nothing on
the page shouts. The hazard colour appears the way it appears on
a real round — as a stripe on a step edge, a tag on a watch item —
never as a theme colour. The all-clear green is a stamp, pressed
once, not a palette. The page's drama is procedural: zones light
as the round reaches them, checks draw themselves as work is
done, totals count to figures that refuse to be rounded, and
exactly one object — the argued-about object — is never resolved,
because real ledgers have one of those too and pretending
otherwise would be the theme's only lie.

**Best-fit sites and audiences.**

- **Space sustainability and SSA firms** whose product is, at
  bottom, a catalogue and a promise to keep it honest — the theme
  turns their tracking list into a nightly human ritual instead of
  a SaaS dashboard.
- **Satellite operators** publishing conjunction and stewardship
  reporting to regulators and the public: the checklist *is* the
  compliance artefact, and its unrounded totals read as care.
- **Advocacy campaigns** against orbital debris, where the
  audience must feel the scale (34,127 individual objects, each
  with an ID) without being lectured — the custodian's round makes
  scale walkable.
- **Museum, planetarium and science-press features** on the
  debris problem, where one narrator-guide carries the visitor
  through zones of orbit the way he carries them through rooms.

**When NOT to use it.**

- **Real-time operations consoles.** If the visitor's job is to
  act on a conjunction warning in the next ninety seconds, they
  need density, alarms and zero theatre. This theme's beam patrols
  at walking pace on purpose; do not put it between an operator
  and a manoeuvre decision.
- **E-commerce or catalogue retail.** The clipboard here is a
  working ledger, not a rustic skin; the moment the "checklist"
  becomes a cart, the metaphor collapses into kitsch.
- **Anything that needs to feel fast, young or loud.** The theme's
  authority is slowness and exactness. A launch-hype page in
  clipboard buff will read as a fancy-dress costume.
- **Data the publisher cannot actually stand behind.** The law —
  never round, always trace — is a promise. If the underlying
  catalogue is estimated, modelled loosely, or marketing copy, the
  theme will expose it: every figure on the page invites the
  visitor to check the working.

**The custodian is a character, not a mascot.** He never appears
as an illustration, a cartoon, or a name with a face. He exists
only as handwriting-pressure in the pencil strokes, as the beam's
patrol path, and as the notes' voice ("Still up there." / "Checked
twice — holding."). The moment he becomes clip-art, the ledger
becomes a storybook and the data stops being believed.

---

## 2. Palette

Five anchors from the original entry, unchanged, plus seven
derived tokens. Every contrast figure below was **computed from
the hex values for this expansion** (WCAG relative luminance), not
estimated. The palette's discipline: buff and ink do the reading;
beam is light, not a colour; hazard and clear are *signals with
jobs*, rationed by rule, never decoration.

| Token | Hex | Role | Usage ratio | Pairing / contrast ruling |
|---|---|---|---|---|
| `--buff` | `#E7DFC9` | Clipboard buff — the board, cards, notes | ~55% of lit surface | Ground for `--ink` text: **11.56:1** — the page's reading pair |
| `--ink` | `#22252A` | Night-orbit ink — text on buff; the field's base tone | ~25% | On `--buff` 11.56:1; `--beam` text on it 12.72:1 |
| `--beam` | `#F5E9C8` | Flashlight beam — lit pools, card faces in the dark, focus light | ~10% | On `--ink` 12.72:1; never a text ground for `--hazard` (1.86:1, forbidden) |
| `--hazard` | `#D9A441` | Hazard stripe — watch tags, stripe edges, the refusal flag | ≤3% | On `--ink` 6.83:1 (text legal); on `--buff` **1.69:1 — forbidden pairing**, stripe only over ink or as a border on buff |
| `--clear` | `#3E6B48` | All-clear green — the stamp, resolved states | ≤2% | On `--buff` 4.64:1 (stamp/large text only); on `--ink` **2.49:1 — forbidden as text**, stamp fill only |
| `--ink-deep` | `#17191D` | The unlit field — hero sky, dark zones before the round reaches them | field ground | Points and beam read against it; no text sits directly on it except `--beam` |
| `--buff-dim` | `#D8CFB2` | Carbon paper — the duplicate sheet under every note | under-layer | Never a text ground; exists to be seen at edges and in ghosts |
| `--pencil` | `#55534B` | Graphite — check strokes, pencil notes' rules, sketch arcs | strokes only | On `--buff` 5.80:1 — legal for note text at ≥14px |
| `--pencil-soft` | `#6E6A5E` | Worn graphite — secondary annotations, timestamps | small areas | On `--buff` 4.06:1 — **large text and labels only, never body** |
| `--faded` | `#8A8474` | Carbon ghost tone — duplicate text, yesterday's entries | ghost layer | On `--buff` 2.80:1 — **never live text**; ghosts and struck history only |
| `--tape` | `#B9B09A` | Tape — polaroid corners, clip pads, mended edges | small patches | On `--ink` 7.13:1; a material, not a text colour |
| `--beam-hot` | `#FFF6DC` | Beam centre — the pool's hot core, glint peaks | inside beam only | Never a surface; a gradient stop |

**Dark behaviour — there is no dark-mode inversion.** The theme
is already a night scene with a lit board. `prefers-color-scheme:
dark` changes nothing structurally; instead the theme defines a
**"lights-up" state** (§6.16): when the visitor's system requests
reduced data or the page is printed, the whole page renders as the
board under full light — buff everywhere, ink text, beam and field
removed, every check printed as a finished stroke. Print
stylesheet = lights-up state, exactly: a ledger is meant to be
photocopied.

**Rationing rules (enforced by the quality gate, §10).**

- Hazard appears at most **once per zone** as a tag, plus the
  stripe edging on the conjunction tag (§6.13). A page-wide hazard
  census above 8 instances fails the gate.
- The all-clear stamp (§6.15) is the only large area of `--clear`
  permitted anywhere; green is never a button colour, a link
  colour, or a success toast.
- Beam pools may not sit under body text at rest: text in the dark
  field lives on buff cards the beam *visits*, so when the beam is
  elsewhere the card is dimmed to 55% ink-on-buff legibility — no,
  the card keeps its buff ground at full contrast; only its
  *glint* depends on the beam. (See §6.1: cards are readable in
  the dark; the beam adds the flip, not the legibility.)

---

## 3. Typography

Three faces, three jobs, no fourth voice. **Libre Franklin** is
the printed form — the ledger's official hand, used for display
and headings. **Special Elite** is the typewriter the custodian
types his notes on — annotations, stamps' lettering, card notes;
it is a *hand*, never a headline face. **IBM Plex Mono** is the
catalogue — object IDs, totals, timestamps, table data; anything
that must not round is set in mono so its digits align and can be
audited column by column.

| Role | Face / weight | Size | Line-height | Tracking | Rules |
|---|---|---|---|---|---|
| Display (hero) | Libre Franklin 800 | `clamp(2.75rem, 6.2vw, 4.75rem)` | 1.02 | −0.01em | Sentence case, never all-caps; the headline is a ledger title, not a shout |
| Heading (zone) | Libre Franklin 700 | `clamp(1.6rem, 3vw, 2.25rem)` | 1.1 | 0 | Prefixed by the zone letter in mono (`ZONE C —`) |
| Sub-head / card title | Libre Franklin 600 | 1.125rem | 1.25 | 0 | Object names and section labels |
| Body | Libre Franklin 400 | 1.0625rem (17px) | 1.55 | 0 | Max measure 62ch on the board; body never sits on the dark field |
| Clipboard note | Special Elite 400 | 0.9375rem | 1.45 | 0.01em | The custodian's voice; slightly uneven baseline is the font's own — never add rotation to fake it |
| Object ID / data | IBM Plex Mono 500 | 0.875rem | 1.4 | 0 | Tabular by nature; IDs never wrap mid-string (`white-space: nowrap` with shrink-to-fit at <768px) |
| Total / counter | IBM Plex Mono 600 | `clamp(1.5rem, 3.4vw, 2.5rem)` | 1.1 | 0 | Digits only ever count to exact values (§6.4) |
| Stamp lettering | Special Elite 400 | 0.8125rem | 1 | 0.14em, uppercase | ALL CLEAR / RE-CHECK TOMORROW — the only all-caps text on the page |

**Type laws.**

1. **Numerals are mono, always.** A total set in Franklin is a
   rounding waiting to happen — proportional figures hide a digit
   change; mono figures confess it.
2. **Special Elite never exceeds 1.25rem.** The typewriter is a
   note in the margin. At display size it becomes a costume.
3. **The word "approximately" is banned from data contexts.** The
   ledger writes the figure or writes "not yet counted" (§12).
4. **Strike-through is a typographic state, not deletion.**
   Corrected entries stay legible under a pencil strike (§6.6) —
   the ledger's history is part of its evidence.
5. **Zone letters are mono and literal** — A through F for the
   six zones of the standard round. A site with more zones letters
   them G, H…; it never invents names like "Sector Alpha".

---

## 4. Layout language

The page is a **clipboard laid over a night sky**. The board —
buff, with a steel clip rendered at its top edge and three
ring-holes punched down its left margin — carries all reading
matter. Behind and around it, visible at the hero and in the
gutters of wide screens, is the field: `--ink-deep` darkness
seeded with tiny tracked points (2px, buff at 40–70% opacity,
each one a real catalogue entry in the data record, §6.12). The
board never covers the whole viewport on ≥1200px screens; the
dark margin is where the beam patrols and where the polaroids are
taped.

**Grid and rhythm.**

- Board column: max 1180px, centred, with a 72px left margin
  channel inside the board for the ring-holes and the pinned
  checklist rail (§6.11) to live in.
- Baseline rhythm: 8px grid; ledger rules (the horizontal lines
  of the board) every 32px on note surfaces, drawn as 1px
  `--buff-dim` lines — content sits *on* the lines like writing.
- Zones are the page's chapters. Each zone is a sheet on the
  clipboard: full board width, separated by a torn-edge rule (an
  SVG mask, 6px amplitude) and a zone header strip — zone letter
  in mono, zone name in Franklin, item count in mono at the right
  edge ("8 ITEMS — 7 TICKED, 1 TO RE-CHECK").
- Density: the board is *paperwork-dense* — tables, cards and
  checklists at 16–24px gaps — while the field stays empty. The
  contrast between a full clipboard and an empty sky is the
  theme's central spatial fact: everything known is on the board;
  everything else is dark.

**Section choreography.** The round walks downhill: hero (the
field, the beam, the headline card), the totals strip (§6.4), then
zones A–F in order, the argued-about object's sheet (§6.5) after
the zone it belongs to (Zone C in the standard round), the
all-clear zone (§6.15) wherever a zone genuinely has nothing on
it, the sighting form (§6.14) on the board's last sheet, and the
handover footer (§6.17) as the board's back page. The checklist
rail (§6.11) pins at the board's left edge from the totals strip
to the footer — the visitor is never more than a glance from
knowing where the round stands.

**Whitespace.** On the board, whitespace is *blank ledger lines* —
unruled space reads as a mistake, so empty board areas keep their
32px rules. In the field, emptiness is the content: never fill
the sky with decorative stars that are not catalogue points. A
point that is not in the record is a lie the size of a pixel, and
the theme does not tell it (§9).

---

## 5. Full motion system

Motion in this theme is **work being done at walking pace**. The
beam patrols, the pencil ticks, the cards flip when the light
reaches them. Nothing bounces, nothing springs for joy; the one
overshoot in the system is the stamp press (§6.15), because a
stamp lands hard. Every scrubbed value runs through **one shared
rAF loop** (`--loop-lerp: 0.12`) — beam position, check-stroke
progress, wobble amplitude, counter values and parallax offsets
are all lerped there, never written by raw scroll handlers.

**Named easings (the only ones the theme uses).**

| Token | Curve | Used by |
|---|---|---|
| `--ease-patrol` | `cubic-bezier(0.45, 0.05, 0.25, 1)` | Beam sweep and lean — a walked path, steady with soft turns |
| `--ease-pencil` | `cubic-bezier(0.3, 0.7, 0.4, 1)` | Check strokes, strike-throughs — a hand accelerating into the stroke |
| `--ease-flip` | `cubic-bezier(0.25, 0.8, 0.35, 1)` | Catalogue card flips — paper turning, no bounce |
| `--ease-stamp` | `cubic-bezier(0.2, 1.3, 0.4, 1)` | The all-clear stamp press — the system's one overshoot |
| `--ease-settle` | `cubic-bezier(0.25, 0.6, 0.3, 1)` | Reveals, sheet changes, the lights-dip — everything else |

**The motion terms, in this theme's language.**

- **Scroll-triggered reveals** — zones *light up* as the round
  reaches them: the zone sheet's lamp pool (§6.1's ground light,
  not the hero beam) fades in over 600ms `--ease-settle` at 25%
  viewport entry. Content is fully visible before, during and
  after; the light is a change of warmth, never of opacity below
  0.85.
- **Scroll-driven / scrubbed animation** — pencil checks draw in
  proportion to scroll through their checklist (§6.2), stroke
  progress = clamp of the item's viewport passage, lerped at 0.12.
  Scroll back up and the check *stays drawn* — work done is not
  undone by walking backwards; the scrub applies only to the
  not-yet-ticked frontier item.
- **Parallax** — three depths, all inside the field: points layer
  at 0.96× scroll, polaroid layer at 1.02×, beam glow at 1.0×.
  The board itself never parallaxes — paper on a clipboard does
  not drift.
- **Pinned sections** — the checklist rail (§6.11) pins for the
  length of the round; the zone header strip pins within its zone
  (sticky, 48px) so a long zone never loses its name.
- **Masked line reveals** — the hero headline card rises into a
  clip mask over 700ms `--ease-settle` as the beam's first sweep
  crosses it (§6.1); lines stagger 90ms. Text is in the DOM and
  readable from first paint; the mask is JS-armed only.
- **Blur-to-sharp** — *refused, with a reason:* a ledger is either
  legible or it is not yet lit; blur reads as eyesight failing.
  The theme's equivalent is the beam's focus pool sharpening a
  card's *glint*, never its text.
- **Kinetic typography** — *refused:* type on a ledger does not
  move. The only moving letterforms are digits (§6.4) and the
  pencil strokes.
- **Marquee** — *refused:* nothing on a clipboard scrolls
  sideways. The conjunction tag (§6.13) is pinned and still; a
  ticker would make a warning into wallpaper.
- **Counters** — §6.4: quantised mono digit rolls to exact values
  over 1200ms, landing dead on the figure, with the printed figure
  present in the DOM from first paint for no-JS and AT.
- **SVG line-draw** — pencil checks (§6.2), the refusal arc
  (§6.3), strike-throughs (§6.6): all single-path strokes with
  `pathLength=100`, drawn by the shared loop.
- **Image scale-in-frame** — polaroids (§6.9) scale 1.06→1.0
  inside fixed taped frames over 800ms on entry; the frame and
  tape never move.
- **Hover / magnetic / tilt micro-interactions** — magnetic and
  tilt are refused (paper does not lean toward a hand); the
  theme's hover is the **beam-lean** (§6.7): the patrol path bends
  toward the hovered object and its card half-flips. Buttons get
  a 120ms pencil-underline draw. Focus is a beam-pool outline:
  2px `--beam` ring on dark, 2px `--ink` ring on buff.
- **Custom cursor** — *refused, standing rule.* The beam is
  autonomous; a cursor effect would fight it for the visitor's
  eye.
- **Skeleton loading** — the lights-up board (§6.16): content
  areas print as unruled buff sheets with a printed "ROUND NOT
  YET BEGUN" note; hard ceiling 2400ms before the watchdog lights
  the board regardless.
- **Page transitions** — the lights-dip (§6.16): 260ms dip to
  `--ink-deep` and back as sheets change, content swapped at the
  dip's floor; aborted at 1200ms by watchdog.
- **Ambient loops** — exactly two are licensed: the beam patrol
  (§6.1, 26s cycle) and the argued-about object's arc wobble
  (§6.5, scroll-velocity-fed, decaying to a 1px rest tremor). Both
  pause when the tab is hidden and when their section is
  off-screen.
- **Progress indicator** — the checklist itself (§6.11): zones
  ticked, items counted, running total exact. There is no
  separate progress bar anywhere in the theme.
- **Reduced motion** — §10's global ruling: board fully lit, beam
  parked and off, every check printed as a finished stroke, every
  card face-up, totals printed at their exact figures, wobble at
  rest state drawn statically. The reduced page is the *completed
  round*, not a stripped one.

---

## 6. Signature elements

### 6.1 The autonomous flashlight sweep

- **What & why.** A cone of light patrols the hero's dark field on
  its own path — a slow Lissajous patrol across the tracked
  points, period 26s — never following the pointer. As the beam's
  pool crosses a tracked point, the point glints (a 300ms
  brightness peak) and its catalogue card, taped to the field's
  edge, flips up for 2.4s showing the object's ID and status line:
  "OBJ 1998-067A — DEAD SINCE 2004 — STILL UP THERE." It belongs
  because the custodian works whether you watch or not; the hero
  is his round, not the visitor's toy, and an autonomous beam is
  the theme's thesis stated in one gesture: this catalogue is
  *tended*.
- **Structure.** The hero field is a DOM scene, not a canvas: a
  `--ink-deep` section; tracked points are absolutely positioned
  2px buttons (real catalogue entries, §6.12's record) with
  visually-hidden labels; the beam is two nested divs — an outer
  radial-gradient pool (`--beam` at 14% → transparent, 46vmin
  diameter) and a hot core (`--beam-hot` at 22%, 16vmin) —
  composited with `mix-blend-mode: screen`, `pointer-events:
  none`. Cards live in a card rail at the field's foot; a card is
  a buff mini-sheet with a flip transform (§6.12 defines the full
  card; here only the flip face shows). Beam position is computed
  in the shared rAF loop from elapsed time: `x = 50 + 38·sin(t·2π/
  26s)`, `y = 46 + 26·sin(t·2π/17s + 1.3)` (percent of field), so
  the path never exactly repeats inside a visit.
- **Motion spec.** Trigger: time, from page load, hero only.
  Pool and core translate via the shared loop (lerp 0.12 toward
  the parametric target, which smooths the path's corners into
  walked turns) under `--ease-patrol`'s character. Glint: when a
  point enters the pool's inner 40%, its scale peaks 1→2.2→1 over
  300ms and the paired card flips up (`rotateX 88°→0`, 450ms
  `--ease-flip`), holds 2400ms, flips back over 450ms. Only one
  card is up at a time; a second crossing queues behind the first
  card's return. The patrol pauses when the hero is off-screen or
  the tab is hidden (IntersectionObserver + visibilitychange) and
  resumes from the same phase — the custodian does not teleport.
- **States.** Rest (patrolling, no card up) / glinting (point lit,
  card up) / leaned (§6.7 bends the path) / parked (reduced
  motion, data-saver, or hero scrolled past: beam rests at the
  field's lower-left, dimmed to 40%). Points are focusable
  buttons in every state.
- **Content merge.** The beam's itinerary *is* the hero's content:
  every point it visits is a real tracked object with a real card;
  the headline card (§8.1) is the last stop of the first sweep and
  stays raised. Remove the catalogue and the beam has nothing to
  do — it cannot be pasted onto another site's hero.
- **Failure fallback.** Watchdog at 3000ms: if the rAF loop has
  not advanced the beam (blocked script, starved frame budget),
  the beam divs are removed and the hero renders lights-up — all
  points at full opacity, all cards face-up in the rail. No-JS:
  the beam is never inserted (it is JS-built); the field ships
  lit at 85% with cards printed. No object can stay untracked in
  the dark.
- **Reduced-motion variant.** No patrol, no glints, no flips: the
  field is lit flat, points printed at full size with their IDs
  beside the first six, all cards face-up. The custodian has
  finished this round; the board shows the results.
- **Performance budget & mobile variant.** Two gradient divs +
  ≤24 point buttons in the hero; transform/opacity only; the loop
  skips frames when the hero is off-screen (zero cost). Budget:
  ≤0.4ms/frame. Mobile (<768px): patrol path compressed to the
  field's centre band, pool 60vmin, cards stack in a horizontal
  snap-rail at the foot; glint scale peak 1.8.
- **Choreography timeline (v2).** t=0 first paint (field lit 85%,
  cards printed, beam absent) → JS arms → beam fades in at the
  patrol's current phase over 800ms → first crossing ≈t=3.2s:
  point glints (300ms), card flips up (450ms), holds to t≈6s,
  returns → headline card raised at the first sweep's end
  (≈t=9s) and stays → patrol continues 26s/17s dual period →
  watchdog deadline t=3000ms passes unused.
- **State matrix (v2).** *Rest:* patrolling. *Hover:* §6.7 lean
  (path bends ≤12% toward the hovered point). *Focus:* focusing a
  point button leans the beam the same way and raises its card —
  keyboard visitors get the same showing. *Active:* pressing a
  point pins its card up until another point is chosen.
  *Scrolled-past:* patrol parked, beam dimmed at rest position.
  *Disabled:* n/a (points are buttons; a point with no card data
  is not rendered — the record is complete or the point does not
  exist). *Touch:* tap = press (pin card); no hover lean.
- **Breakpoints (v2).** ≥1200px: full field, pool 46vmin, up to
  24 points. 768–1199px: 18 points, pool 52vmin, card rail wraps
  to two rows. <768px: 12 points, pool 60vmin, patrol band
  compressed vertically, card rail becomes a snap-scroll row.
- **Edge cases & failure modes (v2).** *Slow network:* the beam
  and points are DOM/CSS — no asset waits; fonts lagging means
  cards reflow once inside fixed-height shells. *Huge catalogue:*
  the hero shows the 24 nearest-to-manoeuvre points by the
  record's own priority field; it never renders 34,127 DOM nodes
  (the full catalogue is §6.12's paginated index). *Tab hidden
  mid-glint:* timers are phase-based, not frame-counted, so the
  card's hold completes on return or the watchdog settles it
  face-up. *User scrolls fast past the hero:* patrol parks; no
  glint queue survives.
- **Accessibility spec (v2).** Points are `<button>`s with
  aria-labels ("Object 1998-067A, dead payload, tracked"); the
  beam divs are `aria-hidden`. Card flips are announced via a
  visually-hidden live region only when the flip results from
  focus/press, never from the ambient patrol (ambient motion must
  not spam AT). Focus ring: 2px `--beam` outline, offset 3px.
  Touch targets: points are 2px visually but carry a 40×40px
  hit area.
- **Tokens consumed (v2).** `--ink-deep`, `--beam`, `--beam-hot`,
  `--buff`, `--ease-patrol`, `--ease-flip`, `--loop-lerp`,
  `--dur-glint` (300ms), `--dur-cardhold` (2400ms).

### 6.2 Self-drawing pencil checks

- **What & why.** Each checklist item on the round ticks as the
  visitor scrolls past it: a graphite check mark strokes itself
  into the item's box over ~300ms, with a slight hand wobble in
  the path — the stroke is an SVG path whose control points are
  offset by a fixed, seeded jitter so it reads as drawn, not
  rendered. It belongs because progress in this theme is paperwork
  being done by hand; a progress bar would be a machine's summary,
  but a drawn check is a person's.
- **Structure.** Each item is a row: a 22×22px box (1.5px
  `--pencil` border on buff), an inline SVG path
  (`M4 13 L10 18 L20 5`, `pathLength=100`, stroke `--pencil`
  2.5px, round caps), the item label (Franklin), and its status
  note (Special Elite). Stroke progress is driven by the shared
  loop: target = clamp01 of the row's passage through the
  viewport's lower two-thirds, lerped at 0.12; `stroke-dashoffset`
  is the only property written. The wobble is baked into the path
  data at build time (three path variants rotate by item index),
  never randomised at runtime — the custodian's hand is consistent
  within a round.
- **Motion spec.** Trigger: scroll. The frontier item (the first
  unticked item of the zone currently in view) draws as it passes
  the 66% viewport line: stroke 0→100 over 300ms `--ease-pencil`
  once its target passes 0.5, completing even if scroll continues
  (a check, once started, is finished — hands don't half-tick).
  Items far above the viewport (jump scroll, anchor link) are
  drawn instantly at full stroke with no animation. Scrolling back
  up never erases a drawn check.
- **States.** Unticked (empty box, label at full ink) / drawing
  (stroke partial) / ticked (full stroke, label stays full ink —
  ticked work is not greyed out; the custodian still needs to read
  it) / refused (§6.3 — a different state entirely, never a
  partial check).
- **Content merge.** The checklist is the page's progress system
  (§6.11's rail is built from these same rows); the checks are not
  decoration on the content, they are the record of the visitor
  having walked the round — and §6.8 lets the visitor draw one
  themselves.
- **Failure fallback.** Watchdog per zone at 2000ms after the zone
  enters: any item whose stroke is stuck between 1% and 99% snaps
  to its scroll-implied end state. No-JS: all checks are printed
  as finished strokes (the round ships completed on paper; the
  drawing is the enhancement). If SVG is unavailable, a text glyph
  "✓" in Special Elite replaces the path at the same size.
- **Reduced-motion variant.** Checks appear fully drawn the moment
  their item enters the viewport — no stroke animation, no scrub.
  The information (done / not done) is identical; only the hand's
  movement is stilled.
- **Performance budget & mobile variant.** One SVG path per item,
  ≤36 items per round; dash-offset writes only for the frontier
  item (≤1 per frame). Budget ≤0.2ms/frame. Mobile: identical —
  the check is already the cheap variant; box grows to 26×26px
  for touch parity with §6.8.
- **Choreography timeline (v2).** Item crosses 66% line → target
  passes 0.5 at t=0 → stroke draws t=0–300ms (wobble path,
  `--ease-pencil`) → running total in the rail (§6.11) increments
  at t=300ms exactly → next item becomes the frontier → zone
  complete: zone header's count updates ("8 ITEMS — 7 TICKED, 1 TO
  RE-CHECK") at the last item's t=300ms.
- **State matrix (v2).** *Rest:* unticked or ticked as scrolled.
  *Hover:* the box's border deepens to `--ink` (a hand hovering
  over the box) — no stroke change. *Focus:* items are not
  focusable (they are records, not controls) except in §6.8's
  interactive subset, which has its own matrix. *Active:* n/a.
  *Scrolled-past:* ticked, permanent. *Disabled:* n/a. *Touch:*
  identical to desktop; no hover state.
- **Breakpoints (v2).** ≥1200px: 22px box, label 17px.
  768–1199px: same. <768px: 26px box, label 16px, status note
  drops below the label (two-line row) so the stroke's row never
  compresses horizontally.
- **Edge cases & failure modes (v2).** *Very long item labels:*
  wrap to two lines; the box aligns to the first line's cap
  height, the stroke never stretches. *User scrolls up mid-draw:*
  the draw completes (300ms commitment) — reversing a check
  mid-stroke would read as the ledger changing its mind.
  *Anchor-jump to the footer:* all items above resolve instantly
  ticked; the round is treated as walked. *Print:* all checks
  printed drawn (§2 lights-up).
- **Accessibility spec (v2).** Each row carries visually-hidden
  status text ("checked" / "not yet checked" / "to re-check
  tomorrow") so the state survives without sight of the stroke.
  The SVG is `aria-hidden`. Contrast: stroke `--pencil` on
  `--buff` 5.80:1. State is never carried by the stroke alone —
  the zone header's mono count restates it numerically.
- **Tokens consumed (v2).** `--pencil`, `--ink`, `--buff`,
  `--ease-pencil`, `--dur-check` (300ms), `--loop-lerp`.

### 6.3 The item that refuses to tick

- **What & why.** In every zone, exactly one checklist item never
  ticks. Beside its empty box, a dashed predicted-path arc (SVG,
  `--pencil-soft` dashes) wobbles — amplitude fed by scroll
  velocity — and a pencil note in Special Elite reads "RE-CHECK
  TOMORROW". It belongs because a tracking system that claims
  certainty about everything is lying; the refusal is the theme's
  honesty made structural and recurring, one per zone, like a
  signature the custodian signs six times a night.
- **Structure.** The row is §6.2's row with the check path absent
  and an arc SVG (120×36px, a shallow dashed orbital arc with an
  ellipse marker) in a right-hand cell. The arc's path is
  recomputed in the shared loop: a sine perturbation
  `amp = clamp(scrollVelocity · 0.02, 1px, 7px)` added to the
  arc's control point, decaying to a 1px rest tremor when scroll
  stops. The note "RE-CHECK TOMORROW" is printed text, not an
  image. The refusal is declared in the data record
  (`"status": "recheck"`) — the builder never chooses it at
  runtime; which item refuses is an editorial fact of the round.
- **Motion spec.** Trigger: scroll (velocity) + ambient rest
  tremor. Wobble updates through the shared loop (lerp 0.12);
  at rest the tremor period is 3.2s, amplitude 1px — present but
  ignorable, like a draught. When the visitor scrolls fast, the
  arc visibly argues (up to 7px) and settles over ~900ms after
  scroll stops. The empty box never fills, at any scroll depth,
  in any state.
- **States.** Refused (resting tremor) / refused (arguing, scroll
  active) / hovered (the arc stills to its true predicted path for
  as long as hover lasts — the custodian holds the paper flat to
  look) / printed (lights-up: arc drawn at rest amplitude, note
  printed).
- **Content merge.** The refused item is a real catalogue problem
  — an object whose ephemeris disagrees with observation — named
  in the row with its ID and its two candidate fates. It is the
  zone's most informative row, not an Easter egg: §8.2's worked
  example shows a zone's refusal carrying the section's argument.
- **Failure fallback.** If the loop fails, the arc renders at its
  rest path (a static dashed arc) and the note stands — the
  refusal reads perfectly with zero motion. No-JS: identical
  static rendering. The watchdog (§6.2's zone watchdog) treats the
  refused row as complete-by-design and never "fixes" it.
- **Reduced-motion variant.** Arc drawn at rest amplitude,
  statically; the note printed. No tremor, no scroll coupling.
  The refusal is information, and information survives stillness.
- **Performance budget & mobile variant.** One path recompute per
  refused row per frame while its zone is on-screen (≤2 rows
  visible typically); ≤0.15ms/frame. Mobile: arc cell drops below
  the label with the note (same two-line row as §6.2), wobble
  amplitude capped at 5px.
- **Choreography timeline (v2).** Zone enters → refusal row prints
  with the zone's other rows → scroll velocity rises → arc
  amplitude lerps 1px→(velocity-fed, ≤7px) continuously → scroll
  stops → amplitude decays to 1px over ≈900ms → hover: amplitude
  eases to 0 over 200ms and the true path shows → hover ends:
  tremor resumes over 400ms.
- **State matrix (v2).** *Rest:* 1px tremor. *Hover:* stills to
  true path (200ms). *Focus:* the row is focusable as a link to
  the object's catalogue entry (§6.12); focus stills the arc the
  same way and shows the focus ring on the row. *Active:* n/a.
  *Scrolled-past:* unchanged — refusals do not resolve by being
  left behind. *Disabled:* n/a. *Touch:* tap = focus behaviour
  (stills + link). No hover.
- **Breakpoints (v2).** ≥1200px: arc cell 120px at row right.
  768–1199px: arc cell 96px, amplitude cap 6px. <768px: arc moves
  to a full-width second line (160px wide), cap 5px, note wraps
  under the arc.
- **Edge cases & failure modes (v2).** *A zone with genuinely no
  uncertain item:* the theme forbids inventing one — that zone is
  an all-clear zone (§6.15) instead. The refusal must be earned by
  the data. *Two uncertain items in one zone:* the second is
  listed as a normal item whose note reads "watch" in pencil; the
  one-refusal-per-zone ration is a design law, not a data limit.
  *Velocity spikes from scrollbar drags:* amplitude clamps at 7px
  regardless.
- **Accessibility spec (v2).** The row's hidden status text reads
  "not checked — to re-check tomorrow: predicted path uncertain".
  The arc is `aria-hidden` (its information is the note's text).
  The note is `--pencil` on `--buff` at 15px (5.80:1) — the
  refusal is never conveyed by wobble alone.
- **Tokens consumed (v2).** `--pencil`, `--pencil-soft`, `--buff`,
  `--loop-lerp`, `--dur-settle-arc` (900ms).

---

### 6.4 Unrounded totals

- **What & why.** The catalogue's totals, set in IBM Plex Mono,
  count up when they enter view and stop *dead* at their exact
  figures: "34,127 objects tracked. 34,126 predicted. One we argue
  about." No rounding, no "K", no "~". It belongs because
  precision is this theme's personality — a janitor who rounds is
  a janitor who loses things — and because the three numbers
  together are the whole story: everything counted, almost
  everything predicted, one honest exception.
- **Structure.** A totals strip on the board directly under the
  hero: three figures in mono, each with a Franklin caption and a
  Special Elite annotation. The figures live in the page's single
  catalogue record (`data-catalogue` JSON in the DOM: tracked
  34127, predicted 34126, argued 1) — every other printing of
  these numbers on the page (rail §6.11, footer §6.17, form §6.14)
  reads from the same record at build time, so the page cannot
  disagree with itself. The count-up is a quantised digit roll:
  the displayed integer steps through ~40 logarithmically spaced
  values over 1200ms in the shared loop, formatted with the
  locale's thousands separator, and lands exactly.
- **Motion spec.** Trigger: first entry into view (60% line).
  1200ms, `--ease-settle` character, values lerped in the shared
  loop and rounded to integers for display — intermediate values
  are honest integers, never decimals of an object. The third
  figure ("One") does not count: it fades in at the second
  figure's completion, because the argued-about object is not a
  quantity to accumulate but a fact to admit. Re-entering view
  never re-runs the count.
- **States.** Printed (pre-trigger / no-JS / reduced motion: exact
  figures at rest) / counting (≤1200ms) / landed (exact, permanent).
  There is no hover or active state; totals are testimony, not
  controls.
- **Content merge.** The totals are the hero's payload — the
  visitor learns the scale of the problem and the shape of its
  honesty in one strip. The "One we argue about" figure is the
  page's narrative hook, linking directly to §6.5's section.
- **Failure fallback.** The exact figures are the DOM's text
  content from first paint; the count-up *replaces* them only
  while running (JS-armed), and the watchdog (1600ms) restores the
  exact figure if the loop stalls mid-count. A visitor can never
  be left staring at "34,09—" because a frame dropped.
- **Reduced-motion variant.** No count. The figures stand printed
  at their exact values; the third figure is present, not faded.
- **Performance budget & mobile variant.** Three text nodes updated
  ≤40 times over 1200ms; negligible. Mobile: the strip stacks
  vertically, figures at 1.5rem, captions beneath — the numbers
  never shrink below legibility to fit a row.
- **Choreography timeline (v2).** Strip crosses 60% line → t=0
  figure 1 begins its roll → t=1200ms figure 1 lands on 34,127 →
  figure 2 begins at t=150ms (staggered start, overlapping rolls)
  → lands 34,126 at t≈1350ms → "One we argue about." fades in
  300ms at t≈1400ms → watchdog deadline t=1600ms passes with all
  figures landed.
- **State matrix (v2).** *Rest:* printed exact. *Hover:* none.
  *Focus:* the strip is not focusable; the argued figure is a link
  to §6.5 and takes the standard focus ring when tabbed to.
  *Active:* n/a. *Scrolled-past:* landed figures remain.
  *Disabled:* n/a. *Touch:* identical; no count restart on tap.
- **Breakpoints (v2).** ≥1200px: three columns across the board.
  768–1199px: three columns, figures 2rem. <768px: stacked rows,
  figure left, caption right, a ledger rule between rows.
- **Edge cases & failure modes (v2).** *The record changes between
  builds (a new catalogue drop):* every printing updates from the
  one record; the anti-slop gate (§10) greps the built page for
  any hard-coded total that disagrees. *A total of zero argued
  objects:* the third figure prints "None we argue about. A quiet
  night." — the theme permits a resolved ledger; it forbids
  inventing a dispute (§6.5's edge case). *Very large totals
  (7 digits):* mono at the same size; the strip wraps before the
  figure shrinks.
- **Accessibility spec (v2).** During the count, an `aria-hidden`
  duplicate animates while the accessible figure is the final
  exact value from first paint (screen readers never hear a
  number mid-roll). The strip is a `<dl>` — term/caption,
  definition/figure — so the numbers keep their meanings in the
  accessibility tree.
- **Tokens consumed (v2).** `--ink`, `--buff`, `--ease-settle`,
  `--dur-count` (1200ms), `--loop-lerp`.

### 6.5 The argued-about object

- **What & why.** One object in the catalogue — in the standard
  round, OBJ 1998-067A, dead since 2004 — gets its own small sheet
  on the board, between its zone and the next: its predicted-path
  arc wobbles permanently, and its card carries two contradictory
  pencil notes from two different nights: "decaying — down by
  spring." and "checked twice — holding." It is never resolved.
  It belongs because every real tracking operation has this
  object, and giving it a section instead of a footnote is the
  theme's most human decision: uncertainty, given a chair.
- **Structure.** A half-width sheet pinned after Zone C: the
  object's catalogue card (§6.12 pattern, large variant), a wide
  arc SVG (100% × 120px) whose path carries two overlaid predicted
  paths — the two disagreeing ephemerides drawn as two dashed
  arcs diverging by up to 14px at apogee — and the two notes in
  Special Elite, each dated in mono (`NIGHT 214`, `NIGHT 231`).
  The wobble is the divergence itself breathing: the second arc's
  control point oscillates ±3px around its printed path, fed by
  the shared loop with scroll-velocity gain (as §6.3, larger
  amplitude, slower period 4.6s).
- **Motion spec.** Trigger: ambient while on-screen + scroll
  velocity. Rest tremor ±1.5px at 4.6s; scrolling raises the
  divergence wobble to ±5px, decaying over 1200ms. The notes never
  move. Nothing about the section ever resolves, flashes, or
  "updates" — a fake resolution animation would be the theme's
  one unforgivable lie.
- **States.** Argued (resting) / argued (scroll-agitated) /
  hovered (both arcs still to their printed paths — the two
  claims held side by side for inspection) / printed (lights-up:
  both arcs static, notes printed).
- **Content merge.** This is a content section, not a widget: the
  operator's actual hardest object, with its actual data dispute,
  written the way the dispute exists in the real ledger. On an
  advocacy build it is the shareable heart of the page; on an
  operator build it is where the methodology note lives ("why two
  ephemerides can disagree") directly under the arcs.
- **Failure fallback.** Static by default: both arcs printed,
  notes printed, card printed. The wobble is the only enhancement
  and its absence changes nothing readable. No watchdog needed
  beyond the loop's global one (§6.1) — a stalled wobble is a
  still arc, which is a legal state of this element.
- **Reduced-motion variant.** Both arcs at their printed paths,
  no tremor. The disagreement is in the drawing, not the motion.
- **Performance budget & mobile variant.** One path recompute per
  frame while on-screen; ≤0.15ms/frame. Mobile: the sheet goes
  full-width, arc height 88px, divergence cap 10px, the two notes
  stack (earlier night first — chronology is the reading order).
- **Choreography timeline (v2).** Sheet enters → arcs print at
  rest divergence → tremor begins (4.6s period) → visitor scrolls:
  wobble gains to ±5px with velocity → scroll stops → decay to
  tremor over 1200ms → hover: arcs ease to printed paths over
  250ms, hold → hover leaves: tremor resumes over 500ms. No other
  beats exist; the section's stillness is its choreography.
- **State matrix (v2).** *Rest:* tremor. *Hover:* stills (250ms).
  *Focus:* the card's catalogue link stills the arcs identically;
  focus ring on the link. *Active:* n/a. *Scrolled-past:*
  unchanged. *Disabled:* n/a. *Touch:* tap on the card follows its
  link; no still-on-tap (touch has no hover to inspect with — the
  printed paths are already both visible).
- **Breakpoints (v2).** ≥1200px: half-width sheet, arc 120px.
  768–1199px: sheet 60% width. <768px: full width, arc 88px,
  notes stacked, divergence cap 10px.
- **Edge cases & failure modes (v2).** *The dispute resolves in
  reality (the object re-enters, or the ephemerides converge):*
  the section is retired at the next build and the totals' third
  figure changes to the quiet-night line (§6.4) — the theme
  forbids keeping a mascot dispute alive after the data settles
  it. *Two objects genuinely disputed:* the second gets a §6.3
  refusal in its zone, not a second shrine; one argued-about
  object per page is a ration, like hazard. *Long object names:*
  the card title wraps; the arc never does.
- **Accessibility spec (v2).** The two arcs are `aria-hidden`; a
  visually-hidden paragraph states the dispute in words ("Two
  predictions disagree: one has the object decaying by spring,
  the other has it holding. The custodian has not resolved it.").
  Notes are `--pencil` on `--buff` (5.80:1) at 15px.
- **Tokens consumed (v2).** `--pencil`, `--pencil-soft`, `--buff`,
  `--ink`, `--loop-lerp`, `--dur-argue-decay` (1200ms).

### 6.6 Carbon-duplicate notes

- **What & why.** Every note on the clipboard — the custodian's
  annotations, card notes, form receipts — exists in duplicate: a
  fainter copy printed one line below the original, offset 2px
  down and 1px left, in `--faded` on a `--buff-dim` slip, like the
  carbon sheet under the page. During any animation of the
  original, the ghost lags one frame behind. It belongs because
  the paperwork aesthetic must be structural, not decorative: a
  ledger that exists in duplicate can be filed, audited and
  handed over — which is exactly what §6.17's handover does with
  it.
- **Structure.** Each note is a `.note` element containing
  `.note-original` and an `aria-hidden` `.note-carbon` (same text,
  `position: relative; top: 1.05em` on its own slip, or layered
  behind with a 2px offset for short notes). The carbon is real
  DOM text (print shows both), styled `--faded`, on a
  `--buff-dim` background slip with the same torn edge. The
  one-frame lag: when the original is animated by the shared loop
  (a note being struck through, a receipt stamping in), the carbon
  copies the transform with the loop's previous frame value — a
  one-frame delay line in the loop, not a second animation.
- **Motion spec.** Trigger: always (static duplication) + any
  animation of the original (lag). Static state: no motion — the
  ghost simply sits there, slightly misregistered, the way carbon
  copies do. During a strike-through (§6.2's cousin interaction:
  correcting a note) the pencil strike draws on the original over
  300ms `--ease-pencil` and on the carbon one frame later at 92%
  stroke opacity — the copy is always slightly worse; that is its
  truth.
- **States.** Filed (static duplicate) / copying (original in
  motion, ghost one frame behind) / struck (both struck, ghost's
  strike lighter). Notes are text; hover/focus states belong to
  the elements that contain them.
- **Content merge.** The duplicate is not under *some* notes for
  effect — it is under *every* note, by system, including the
  form's receipt (§6.14) and the footer's handover note (§6.17),
  so the visitor learns the rule once and trusts every note after.
  A note without its carbon would read as unofficial — the system
  creates that reading on purpose.
- **Failure fallback.** The carbon is plain DOM text: if CSS
  positioning fails it simply prints below the original as a
  second, fainter paragraph — the ledger still reads. No-JS:
  identical (the lag is the only JS behaviour, and it is
  invisible at rest).
- **Reduced-motion variant.** Identical statics; the lag collapses
  to zero frames (original and copy move together if either is
  animated by a non-motion means, e.g. a strike on click).
- **Performance budget & mobile variant.** Text duplication costs
  bytes, not frames: the lag reads one stored transform per note
  per frame, only for notes currently animating (≤2 typically).
  Mobile: the carbon slip's offset tightens to 1px/0px so narrow
  notes never push the slip past the board's edge.
- **Choreography timeline (v2).** Note prints (with its carbon) at
  its section's reveal → any later correction: strike draws on
  original t=0–300ms → carbon's strike t=16ms–316ms (one frame
  late, 92% opacity) → both rest, struck, legible → handover
  (§6.17) restates the note's *original* text from the carbon —
  the copy outlives the correction, as carbons do.
- **State matrix (v2).** *Rest:* filed duplicate. *Hover:* none of
  its own (the containing element's hover may lift the pair
  together — both sheets, never the original alone). *Focus:*
  none. *Active:* n/a. *Scrolled-past:* unchanged. *Disabled:*
  n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: carbon offset 2px/1px, slip
  extends 6px past the original's right edge. 768–1199px: same.
  <768px: offset 1px/0px, slip flush right — a narrow board cannot
  afford misregistration past its edge.
- **Edge cases & failure modes (v2).** *Long notes (multi-line):*
  the carbon becomes a full second slip below the original, never
  a layered offset (layered ghosts under wrapped text are
  illegible — the theme chooses the filing-cabinet version over
  the smudge). *A note corrected twice:* two strikes, both
  duplicated; a third correction retires the note to the handover
  (§6.17) — the board does not carry palimpsests. *Screen-reader
  duplication:* carbons are `aria-hidden` without exception; the
  gate (§10) greps for a carbon lacking it.
- **Accessibility spec (v2).** Carbons: `aria-hidden`, `--faded`
  (2.80:1) is legal *because* the carbon is decorative duplication
  of adjacent accessible text — the one place in the theme where
  sub-4.5 contrast is permitted, and the gate requires the
  original within the same note element to prove it. Print: both
  copies print (the duplicate is the point of a carbon).
- **Tokens consumed (v2).** `--faded`, `--buff-dim`, `--buff`,
  `--pencil`, `--ease-pencil`, `--loop-lerp`.

---

### 6.7 Beam-lean hover

- **What & why.** When the visitor hovers (or focuses) a tracked
  object in the hero field, the autonomous beam *leans* toward it:
  the patrol path bends — up to 12% of the field's width — in the
  object's direction, and the object's card half-flips (to 40°)
  in anticipation. The beam never surrenders its patrol; it
  acknowledges, the way a colleague points — "that one, look" —
  and then resumes. It belongs because it is the theme's only
  pointer interaction with the beam, and its restraint is the
  point: attention is lent, not seized.
- **Structure.** A lean vector in the shared loop: while a point
  is hovered/focused, the beam's parametric target gains an
  offset toward the point's position, weighted `0.12 · proximity`
  (nearer points bend the path less — the beam is already close;
  the weight peaks mid-field). The card half-flip is §6.1's flip
  transform arrested at 40° (`rotateX(40deg)`), held while hover
  lasts. On unhover, the offset decays over 600ms and the patrol
  resumes its unbent path from wherever the beam actually is —
  no snap back to the parametric line; the lerp (0.12) walks it
  home.
- **Motion spec.** Trigger: hover/focus of a hero point. Lean-in
  over ~500ms (loop-lerped), half-flip 300ms `--ease-flip`.
  Release: 600ms decay of the lean vector, card completes its
  flip back over 300ms. If the hovered point is crossed by the
  unbent patrol anyway, the glint (§6.1) fires as normal — the
  lean never suppresses the round's own business.
- **States.** Patrolling (no lean) / leaning (hover or focus held)
  / releasing (600ms decay) / parked (§6.1's scrolled-past state —
  no lean accepted; a parked beam does not stir for a cursor it
  cannot see).
- **Content merge.** The lean connects the visitor's curiosity to
  the custodian's attention without breaking the fiction that the
  beam is his. It works only on real catalogue points with real
  cards — there is nothing decorative in the field to lean toward.
- **Failure fallback.** If the loop is stalled, hover still
  half-flips the card (a CSS `:hover` transform fallback at the
  same 40°, no beam movement) — the visitor's intent is answered
  by the card alone. No-JS: points are buttons linking to their
  catalogue entries (§6.12); no lean exists and none is missed.
- **Reduced-motion variant.** No lean, no half-flip. Hover/focus
  raises the card fully (instantly, no transition) — the
  information with none of the gesture.
- **Performance budget & mobile variant.** One vector addition per
  frame while leaning; ≤0.1ms/frame. Mobile/touch: **no lean** —
  touch has no hover; tap pins the card per §6.1's matrix. This is
  stated, not silently absent: the field's help note (§12) reads
  the same on all devices because tapping does the showing.
- **Choreography timeline (v2).** Hover begins → t=0–300ms card
  half-flips to 40° → t=0–500ms lean vector lerps to full bend →
  hold while hovered (beam continues patrol on the bent path,
  glints still fire) → unhover → t=0–300ms card returns → lean
  decays t=0–600ms → patrol path fully its own again.
- **State matrix (v2).** *Rest:* no lean. *Hover:* lean + half-
  flip. *Focus:* identical to hover (keyboard parity is a law
  here, §6.1). *Active:* press pins the card (§6.1); the lean
  releases — a pinned card no longer needs pointing at.
  *Scrolled-past:* lean disabled. *Disabled:* n/a. *Touch:* tap =
  pin; no lean, no half-flip.
- **Breakpoints (v2).** ≥1200px: bend cap 12% of field width.
  768–1199px: cap 10%. <768px: element inactive (touch-first
  layout); on a narrow *mouse* device the cap is 8% and the
  half-flip is 30° (the card rail is a snap-row; a full half-flip
  would clip).
- **Edge cases & failure modes (v2).** *Hover jitter across
  adjacent points:* the lean target switches only after 120ms of
  stable hover on the new point — the beam does not tremble
  between two curiosities. *Hover during a glint on another
  point:* the glint's card wins the rail; the leaned card waits at
  40° until the rail frees (≤2.4s) — the round outranks the
  visitor, politely. *Pointer leaves the window mid-lean:* decay
  begins immediately; no stuck bend.
- **Accessibility spec (v2).** Focus triggers the full lean (not a
  lesser version) — parity is specified, not hoped for. The
  half-flip is `aria-hidden` motion; the card's content is
  available in the accessibility tree regardless of flip angle.
  No information is hover-exclusive: every card is reachable by
  tab and by §6.12's index.
- **Tokens consumed (v2).** `--beam`, `--ease-flip`, `--loop-lerp`,
  `--dur-lean` (500ms), `--dur-lean-release` (600ms).

### 6.8 Click-to-check

- **What & why.** In each zone, a small number of checklist items
  (the record marks them `"visitor": true` — never more than two
  per zone) are interactive: clicking one draws its pencil check
  by the visitor's own hand and increments the round's running
  total by exactly one. It belongs because the round is work the
  visitor has been watching; letting them do one item of it —
  honestly counted, honestly limited — turns spectatorship into
  participation without turning the ledger into a game.
- **Structure.** §6.2's row, with the row itself a `<button>`
  (full-row hit area, box + label inside). The check draws with
  §6.2's stroke system (same path, same 300ms `--ease-pencil`).
  The running total lives in the rail (§6.11) and the zone header;
  both read a single `roundState` object in the page — the
  visitor's checks increment `visitorTicked`, and the printed
  totals (§6.4's catalogue figures) are *never* touched: the
  visitor helps with tonight's round, they do not rewrite the
  catalogue. State persists in `sessionStorage` for the visit
  (the round is tonight's; tomorrow it resets — stated in §12's
  copy).
- **Motion spec.** Trigger: click/tap/Enter/Space on the row.
  Stroke draws 0→100 over 300ms `--ease-pencil` → at completion,
  the rail total and zone count increment (digit change is
  instant — totals do not roll for one tick; rolling is §6.4's
  ceremony, reserved for the catalogue). A checked item cannot be
  unchecked: pencil ticks on this ledger are ink-equivalent
  (undo would be §6.6's strike, and the theme does not let
  visitors strike the custodian's book). The button disables
  itself at draw completion.
- **States.** Offered (box empty, row hoverable, a pencil note
  "your call" in Special Elite at the row's right) / drawing
  (300ms) / visitor-ticked (check drawn, note replaced by "ticked
  by a visitor — counted") / disabled-after (button inert, row
  reads as a normal ticked row).
- **Content merge.** The offered items are real checks the round
  genuinely needs — low-risk confirmations ("Zone B — confirm the
  550 km shell count against the board") whose data is on the page
  for the visitor to verify before ticking. The interaction is
  the content's own task, not a quiz pasted onto it.
- **Failure fallback.** No-JS: offered rows render as ordinary
  unticked items with the note "visitor checks need the board's
  script — the custodian will tick these on his round." Nothing
  is lost; the round completes without help. If storage is
  unavailable, checks work for the page view and simply do not
  persist across navigation — the totals on *this* page stay
  internally consistent because they read the same `roundState`.
- **Reduced-motion variant.** The check appears fully drawn on
  click (no stroke animation); totals increment at once.
- **Performance budget & mobile variant.** One stroke animation +
  two text updates per click; negligible. Mobile: full-row tap
  target ≥48px tall (the two-line row layout of §6.2 already
  guarantees it); no other change — a tick is a tick at any width.
- **Choreography timeline (v2).** Click → box border deepens
  (60ms, the hand arriving) → stroke draws t=60–360ms → note swaps
  to "ticked by a visitor — counted" at t=360ms → rail total and
  zone header increment at t=360ms → button disables, row settles
  into the ticked population. If this was the zone's last open
  item, the zone header's line updates in the same beat — and if
  the zone's refusal (§6.3) remains, the header honestly reads
  "…1 TO RE-CHECK" still.
- **State matrix (v2).** *Rest:* offered. *Hover:* border deepens,
  note underlines in pencil. *Focus:* 2px `--ink` ring on the row,
  same note underline. *Active:* drawing. *Scrolled-past:*
  visitor-ticked rows stay ticked (session). *Disabled:* after
  ticking — visually identical to a custodian tick except the
  note's attribution. *Touch:* tap = click; no hover states.
- **Breakpoints (v2).** ≥1200px: note at row right. 768–1199px:
  same. <768px: note drops to the row's second line (with the
  status note's slot, alternating) so the tap target keeps its
  full width.
- **Edge cases & failure modes (v2).** *Double-click / key
  repeat:* the button disables at draw *start* for input purposes
  (aria-disabled at t=60ms) — one item, one tick, one increment;
  the total can never gain +2 from an eager hand. *Visitor ticks,
  then the catalogue record updates mid-session:* catalogue
  totals (§6.4) are build-time; round totals are session-time;
  the two never mix, and §12's copy says so ("tonight's round"
  vs "the catalogue"). *All offered items ticked:* the rail shows
  a pencil line — "Round helped along: N visitor ticks." — the
  help is acknowledged in the book, not gamified with a badge.
- **Accessibility spec (v2).** Real `<button>`, label includes the
  task and its state ("Confirm the 550 km shell count — not yet
  ticked"). On tick, an `aria-live="polite"` announcement: "Ticked.
  Zone B: 6 of 8 ticked." Focus stays on the row after ticking.
  The increment is announced, never only shown.
- **Tokens consumed (v2).** `--pencil`, `--ink`, `--buff`,
  `--ease-pencil`, `--dur-check` (300ms).

### 6.9 Taped polaroid frames

- **What & why.** Photographs in this theme — a tracked rocket
  body's last ground photo, the custodian's predecessor's
  snapshots, a conjunction diagramme printed as a photo — sit in
  white-bordered polaroid frames held to the board by tape at the
  corners: four tape patches, slightly rotated, one of which (on
  exactly one frame per page) is a different buff — a repair,
  where a corner tore and was mended. The image scales gently
  inside the frame as it enters view; the frame never moves. It
  belongs because the archive is maintained by hand and the
  maintenance shows: these are not stock photos in a grid, they
  are prints somebody kept.
- **Structure.** A `<figure>` with a `--beam`-white border (12px,
  28px at the foot for the caption), the image inside an
  overflow-hidden well, four tape divs (semi-opaque `--tape`,
  54×18px, rotated −4°..5° by a seeded per-frame value) at the
  corners, and a caption in Special Elite on the foot border —
  the photo's ledger line: what it is, when it was taken, its
  catalogue ID in mono. The repaired corner's tape uses
  `--buff-dim` with a visible seam line. Frames sit on the board
  or taped into the field's margin on ≥1200px.
- **Motion spec.** Trigger: entry into view (50% line). The image
  scales 1.06→1.0 over 800ms `--ease-settle` (a slow settle, like
  a print being laid flat) — once; re-entry does nothing. The tape
  and frame are static at all times. Hover: the image scales to
  1.02 over 300ms (a lean-in to look) — the frame and tape stay
  put; nothing casts a growing shadow, because paper taped to a
  board does not float.
- **States.** Unentered (image at 1.06, fully visible — the scale
  is an enhancement over a complete picture) / settled (1.0) /
  hovered (1.02) / printed (lights-up: 1.0, tape printed as buff
  patches).
- **Content merge.** Every polaroid is a catalogue artefact: its
  caption carries the object's ID, and clicking the frame goes to
  the object's entry (§6.12). A photo without an ID does not get a
  frame — decoration is refused at the data level.
- **Failure fallback.** The image is a plain `<img>` with alt text
  in a visible frame; if the image fails to load, the frame holds
  its caption and a pencil note "print missing — see catalogue
  entry" with the ID — the frame never collapses or shows a
  broken-image icon. No-JS: image at 1.0, all frames printed.
- **Reduced-motion variant.** No entry scale, no hover scale. The
  print is simply there, taped, captioned.
- **Performance budget & mobile variant.** Images are the page's
  main weight: each polaroid ≤90KB (WebP, sized to its frame),
  lazy-loaded below the fold, `aspect-ratio` reserved so the board
  never reflows. Mobile: frames go full-board-width, tape patches
  shrink to 44×15px, the repaired corner remains (the repair is
  content, not a wide-screen luxury).
- **Choreography timeline (v2).** Frame crosses 50% line → image
  settles 1.06→1.0 over 800ms → caption's pencil line (a 1px rule
  under the caption) draws in over 300ms `--ease-pencil` at
  t=500ms → rest. Hover at any later time: 300ms to 1.02, release
  300ms back to 1.0.
- **State matrix (v2).** *Rest:* settled. *Hover:* image 1.02.
  *Focus:* the frame is a link; focus ring on the frame's outer
  edge (2px `--ink` on buff, `--beam` in the field margin), image
  at 1.02 (focus/hover parity). *Active:* press — no scale change
  (paper doesn't press). *Scrolled-past:* settled. *Disabled:*
  n/a. *Touch:* tap follows the link; no hover scale.
- **Breakpoints (v2).** ≥1200px: frames at 320–420px wide, may sit
  in the field margin taped over the dark. 768–1199px: 280–340px,
  board only. <768px: full board width minus margins, caption
  14px, tape 44×15px.
- **Edge cases & failure modes (v2).** *Portrait vs landscape
  prints:* the well's aspect is per-photo from the record
  (`aspect-ratio` inline), never a forced crop — a polaroid is
  not cropped by its frame. *The repaired corner:* exactly one
  per page, chosen in the record (`"repaired": true`); two
  repairs reads as a style, one reads as a history. *Missing
  caption data:* the frame does not render — see content merge.
- **Accessibility spec (v2).** Alt text describes the photograph
  ("Ground photograph of the Cosmos 3M upper stage, Baikonur,
  1998"), the caption repeats the ID for AT via the link's label.
  Tape divs are `aria-hidden`. Contrast: caption Special Elite
  `--ink` on the frame's white foot — effectively ink on #FBF7EA,
  >11:1.
- **Tokens consumed (v2).** `--tape`, `--buff-dim`, `--ink`,
  `--ease-settle`, `--ease-pencil`, `--dur-settle-img` (800ms).

---

### 6.10 The clipboard masthead & zone navigation

- **What & why.** The site's header is the clipboard's top: a
  steel clip (drawn in CSS/SVG, gripping the board's top edge)
  holding the round's title sheet — the site name in Libre
  Franklin, the night and round number in mono ("ROUND 412 —
  NIGHT OF 14 NOV") — and beneath it the zone navigation: six
  zone tabs (A–F) lettered in mono with their names, each tab a
  punched ring-hole link down the board's left margin. It belongs
  because navigation in this theme is the round's own index: you
  do not browse a ledger, you turn to the zone you are walking.
- **Structure.** A `<header>` on the board: clip graphic centred
  at top (SVG, 120×36px, `--tape`-grey steel with a hazard-free
  plain finish — the clip is hardware, not a signal), title sheet,
  then a `<nav>`: on ≥768px a horizontal strip of zone tabs; each
  tab shows letter, name, and the zone's live state in miniature
  (a 10px check glyph if the zone is complete, a dashed arc glyph
  if its refusal is still open — the nav tells the round's state,
  not just its structure). The current zone's tab is marked by a
  pencil underline, drawn (§6.2's stroke) when the zone becomes
  current.
- **Motion spec.** Trigger: scroll (current-zone tracking via the
  shared loop's scroll position, not a scroll listener). When the
  current zone changes, the pencil underline draws under the new
  tab over 300ms `--ease-pencil` and lifts from the old (fade
  150ms). The clip does not move, ever — hardware is still. Page
  load: the underline starts under Zone A (or the zone of the
  anchor in the URL).
- **States.** Zones: upcoming (plain) / current (pencil-underlined)
  / complete (check glyph) / complete-with-refusal (check glyph +
  dashed arc glyph — a finished zone can still hold its open
  refusal; the nav does not pretend otherwise).
- **Content merge.** The nav is generated from the same zone
  record as the sections and the rail (§6.11): letters, names,
  item counts and states cannot drift from the page they navigate.
  A zone added to the round appears in the nav by construction.
- **Failure fallback.** Plain anchor links in a list — with no JS
  the nav is a table of contents with state glyphs printed at
  their build-time states (the build prints the round's *starting*
  state; the live updates are the enhancement). The header never
  depends on the loop to be usable.
- **Reduced-motion variant.** The underline swaps instantly
  (no draw); glyphs are static.
- **Performance budget & mobile variant.** One SVG + text; the
  current-zone computation is one comparison per frame inside the
  existing loop. Mobile (<768px): the clip shrinks to 84px wide,
  the title sheet stacks, and the nav becomes a horizontal
  snap-scroll strip of letter tabs (names appear for the current
  zone only) pinned under the header while scrolling — the round's
  index stays reachable on a phone without eating the board.
- **Choreography timeline (v2).** Load → underline under the
  starting zone (printed, not drawn — the round begins already
  indexed) → visitor scrolls into Zone B → old underline fades
  (150ms) → new underline draws (300ms) → zone completes → its
  check glyph stamps in beside the letter (120ms, no overshoot —
  stamps are §6.15's alone; this is a print) → refusal zones gain
  the arc glyph at their last item's tick.
- **State matrix (v2).** *Rest:* current zone underlined. *Hover:*
  a tab's background warms to `--beam` at 30% ( lamplight over
  paper). *Focus:* 2px `--ink` ring on the tab; the tab's zone
  name reads in full (mobile strip expands the focused tab).
  *Active:* the tab of the zone being read. *Scrolled-past:* per-
  zone glyphs persist. *Disabled:* a zone with no sheet in this
  build is not rendered as a tab (the record rules). *Touch:* tap
  navigates; the strip snap-scrolls the tapped tab into centre.
- **Breakpoints (v2).** ≥1200px: full strip, names + glyphs.
  768–1199px: names shorten to the zone's short name from the
  record. <768px: letter tabs + current name, snap-scroll, sticky
  under the header at 44px height.
- **Edge cases & failure modes (v2).** *More than 8 zones:* the
  strip wraps to two rows on desktop rather than shrinking type;
  on mobile the snap-strip simply lengthens. *Deep-link to Zone
  E:* the underline starts at E and the rail (§6.11) initialises
  with A–D treated as walked (their checks printed) — arriving
  mid-round is a supported way to do a round. *Very long zone
  names:* short-name field in the record is mandatory for exactly
  this reason (§11).
- **Accessibility spec (v2).** `<nav aria-label="Zones of the
  round">`, `aria-current="true"` on the current tab (kept in
  sync with the underline — the visual and the AT state are the
  same fact). Tabs are links with full names as accessible names
  even when visually shortened. Focus order: header → nav → rail
  → content.
- **Tokens consumed (v2).** `--tape`, `--ink`, `--beam`,
  `--pencil`, `--ease-pencil`, `--dur-check` (300ms).

### 6.11 The pinned round checklist rail

- **What & why.** Down the board's left margin channel, for the
  whole length of the round, a narrow rail pins in place: the
  round's checklist in miniature — zone letters, per-zone tick
  counts, and the running total in mono ("ROUND: 29 / 36 TICKED —
  6 TO RE-CHECK"). It is the theme's progress indicator, and it
  belongs because a round is a thing you can be *partway through*;
  the rail is the custodian's own glance at his clipboard edge,
  given to the visitor for the whole walk.
- **Structure.** A sticky column (72px wide on desktop) inside the
  board's margin channel, `position: sticky; top: 24px`, built
  from the round record: one row per zone (letter, a 14px check
  box mirroring §6.2's stroke at miniature scale, count "7/8"),
  a rule, then the running total and the refusal count. The rail's
  checks are driven by the same `roundState` as §6.2/§6.8 — when a
  zone item ticks, its rail row updates in the same frame. The
  rail never shows items individually; it is a summary edge, not a
  second checklist.
- **Motion spec.** Trigger: §6.2/§6.8 tick events. A rail check
  draws over 200ms `--ease-pencil` (faster than the main
  checklist — the summary is a glance, not the event). The running
  total's digit change is instant. When a zone completes, its rail
  row's letter gains a pencil circle (a 260ms stroke ellipse) —
  the custodian circling a finished zone in his margin.
- **States.** Walking (counts live) / zone-complete (letter
  circled) / round-complete (total reads "36 / 36 — 6 TO RE-CHECK
  TOMORROW", the refusals honestly still open) / parked (footer
  reached: the rail unsticks and prints its final state as the
  handover's first line, §6.17).
- **Content merge.** The rail is the round's own margin — its data
  is the round's data, its completion state is the handover's
  opening fact. It also serves as the page's "you are here" for
  the round as a whole, which the zone nav (§6.10) does per-zone;
  the two never duplicate because one counts and the other names.
- **Failure fallback.** No-JS: the rail prints the round's
  *starting* state (0 ticked, or the build's declared starting
  state) and remains a useful static index with anchor links to
  each zone. If sticky positioning is unsupported, the rail sits
  at the totals strip as a summary card — same content, unpinned.
- **Reduced-motion variant.** Counts and checks update instantly;
  the circle prints complete. Position behaviour (sticky) is
  unchanged — pinning is layout, not motion.
- **Performance budget & mobile variant.** ≤8 rows, text + 8 mini
  strokes; updates only on tick events. Mobile (<768px): the rail
  leaves the margin and becomes a slim sticky bar under the nav
  strip (§6.10): "ROUND 29/36 · 6 TO RE-CHECK" in mono with a
  per-zone letter row — the summary survives the loss of the
  margin, compressed, never hidden behind a toggle.
- **Choreography timeline (v2).** Round begins → rail pins as the
  totals strip passes → each tick: rail check draws (200ms),
  total increments same frame → zone completes: letter circled
  (260ms) → final zone → rail's total line gains the "TO RE-CHECK
  TOMORROW" suffix (printed, 0ms — honesty is not animated in) →
  footer reached → rail parks into the handover.
- **State matrix (v2).** *Rest:* live summary. *Hover:* a zone row
  warms (`--beam` 25%) — rows are links to their zones. *Focus:*
  2px ring on the row-link. *Active:* the row of the zone in view
  carries a pencil dot at its left. *Scrolled-past:* final state
  printed in the footer. *Disabled:* n/a. *Touch:* tap a row =
  jump to the zone; the bar variant keeps 44px rows.
- **Breakpoints (v2).** ≥1200px: 72px margin rail, full counts.
  768–1199px: 56px rail, counts without the word "TICKED"
  ("29/36"). <768px: sticky bar variant (above), 40px tall.
- **Edge cases & failure modes (v2).** *A round longer than the
  viewport height at rail scale (many zones):* the rail caps at
  8 zone rows; beyond that it shows totals + current zone only —
  a margin cannot become a second page. *Visitor checks (§6.8)*
  increment the same totals — the rail is where their help becomes
  visible, in the same beat (§6.8's timeline). *Print:* the rail
  prints its final state at the totals strip (lights-up).
- **Accessibility spec (v2).** The rail is a `<nav
  aria-label="Round progress">` with the total as text ("Round
  progress: 29 of 36 items ticked, 6 to re-check tomorrow") —
  updated via `aria-live="off"` (it changes too often to announce;
  the per-tick announcement lives in §6.8/§6.2's zone headers).
  Mini check SVGs are `aria-hidden`; counts are text.
- **Tokens consumed (v2).** `--pencil`, `--ink`, `--buff`,
  `--beam`, `--ease-pencil`, `--dur-check` (300ms).

### 6.12 Catalogue cards & the zone index

- **What & why.** Every tracked object has a catalogue card: buff
  mini-sheet, object ID in mono at the head, name and status in
  Franklin, a pencil note in Special Elite, and a state glyph
  (ticked / predicted / argued). In the zones, cards appear in the
  field margin and on the board; in the index (the catalogue page
  pattern), they form a filterable grid — filter chips are
  checklist items themselves ("show only: untracked ☐ / argued
  ☐ / decaying ☐"), ticked in pencil to apply. It belongs because
  the card is the theme's atom of content: one object, one record,
  one honest status — the same card serves the hero's flip, the
  zone's margin, and the index's grid without redesign.
- **Structure.** A `<article class="card">` generated from the
  catalogue record (the page's single `data-catalogue` JSON):
  header row (ID mono + state glyph), title, two data rows (orbit
  class, last confirmed — mono values), note (Special Elite, with
  §6.6's carbon under it in the large variant). The flip (§6.1) is
  a wrapper behaviour, not part of the card: the card's back is
  its own data (the object's arc thumbnail + "last three
  observations" in mono). Filters are real checkboxes styled as
  §6.2 boxes; filtering is a DOM display pass over the rendered
  grid with a printed result count in mono ("SHOWING 41 OF 34,127
  — INDEX SAMPLE"), the sample honestly labelled: the web index
  shows a working sample, the full catalogue is a download (§7).
- **Motion spec.** Trigger: filter tick / grid entry. Filtering:
  cards that leave fade to 0 over 180ms and collapse; cards that
  enter print in (opacity 0→1, 220ms, `--ease-settle`, stagger
  24ms, capped at 12 animated — beyond 12, the rest print
  instantly; a grid is not a fireworks show). The count updates at
  the animation's end with the true figure. Card flip (in hero/
  zone contexts): §6.1's 450ms `--ease-flip`.
- **States.** Face-up / flipped (back showing) / filtered-out
  (absent, counted) / argued (the §6.5 card — hazard-free, marked
  by the double-note glyph, never by colour alone).
- **Content merge.** The cards *are* the catalogue; the filters
  are the checklist the visitor already knows how to read. The
  index's honesty rule — sample labelled as sample, full count
  printed — is the theme's law applied to pagination.
- **Failure fallback.** No-JS: the grid prints its first 24 cards
  with a note and the full-catalogue download link; filters are
  `<noscript>`-hidden (a filter that cannot filter is not shown).
  If the record fails to load, the board prints the totals (§6.4)
  and a pencil note "index unavailable — the ledger office has
  the full book" with the contact route: the page degrades to its
  summary, never to a spinner (§6.16's ceiling applies).
- **Reduced-motion variant.** Filtering is instant (no fades, no
  stagger); the count updates immediately. Flips become face swaps.
- **Performance budget & mobile variant.** Grid renders ≤48 cards
  per page of the index (pagination §11); card DOM is light
  (no per-card listeners — one delegated handler). Budget: filter
  pass ≤8ms for 48 cards. Mobile: one card per row, the flip
  becomes a tap-to-expand (the back's data prints below the face —
  a card on a phone is read, not turned over).
- **Choreography timeline (v2).** Filter box ticked → its check
  draws (300ms, §6.2) → leaving cards fade (180ms) → grid reflows
  → entering cards print in (220ms, stagger 24ms × ≤12) → count
  line updates with the exact figure → focus moves to the count
  line's region for AT announcement (visually unchanged).
- **State matrix (v2).** *Rest:* face-up. *Hover:* card lifts 2px
  (a sheet picked up by its edge — translateY only, shadow grows
  10% — paper, not a floating UI card). *Focus:* 2px `--ink` ring;
  the card's link ("full entry") is the focusable element.
  *Active:* in flip contexts, press flips. *Scrolled-past:*
  unchanged. *Disabled:* a card whose object has decayed moves to
  the "re-entered" styling: its note is struck (§6.6) and a new
  note added — history, not removal. *Touch:* tap = open entry;
  flip contexts use the expand variant.
- **Breakpoints (v2).** ≥1200px: index grid 3 columns; zone cards
  300px in the margin. 768–1199px: 2 columns. <768px: 1 column,
  expand-instead-of-flip, filter chips wrap to two rows with
  44px targets.
- **Edge cases & failure modes (v2).** *Filter combination with
  zero results:* §6.15's all-clear pattern in miniature — a buff
  sheet: "Nothing on the board matches. Loosen a tick." with the
  active ticks listed for unticking. Never a blank grid.
  *Duplicate IDs in the record:* the build fails (§10 gate) — the
  catalogue's integrity is checked before the page ships, not
  forgiven at runtime. *Long notes:* card notes clamp to 3 lines
  with the full note in the entry; the clamp is typographic
  (`-webkit-line-clamp`) with the full text in the DOM for AT.
- **Accessibility spec (v2).** Cards are articles with labelled
  headings (object name); state glyphs are `aria-hidden` with the
  state in the heading's hidden text ("— argued"). Filter changes
  announce the new count via `aria-live="polite"`. Grid is a list
  for AT (`role="list"` / list items), reading order = catalogue
  order (by ID), never visual shuffle.
- **Tokens consumed (v2).** `--buff`, `--ink`, `--pencil`,
  `--faded`, `--ease-flip`, `--ease-settle`, `--dur-check` (300ms).

---

### 6.13 The conjunction hazard tag

- **What & why.** When the catalogue holds a predicted close
  approach inside the next 72 hours, a hazard tag is pinned to the
  board under the masthead: a buff tag with a `--hazard` diagonal
  stripe along its top edge (the only place the stripe pattern is
  used), naming the two objects in mono, the miss distance and
  time-to-closest-approach as exact figures, and a pencil line:
  "Watching it. Nobody moves anything yet." It belongs because a
  ledger of dead objects earns its keep at exactly this moment —
  and because the theme rations hazard to this one tag, the tag
  can be alarming in a way a site-wide red theme never could.
- **Structure.** An `<aside role="note">` styled as a physical
  tag: punched hole at left with a string loop (SVG), stripe edge
  (repeating-linear-gradient, `--hazard`/`--ink` at 45°, 12px
  period — the stripe is *edging*, ≤10px tall, never a fill),
  body in Franklin with mono data rows. The tag's data comes from
  the catalogue record's `watch` field; if the field is empty,
  the tag does not render — instead the board carries §6.15's
  all-clear stamp in the same slot. One tag maximum: if two
  conjunctions qualify, the tag names the nearer and a mono line
  adds "+1 MORE — SEE ZONE D" linking to the second's zone.
- **Motion spec.** Trigger: page load (the tag is a fact, not an
  event). Entry: the tag slides down from under the clip over
  400ms `--ease-settle` with a 2° settle rotation to its printed
  1.5° rest angle — a tag hung on its string. It never pulses,
  never flashes, never re-animates; the countdown figure updates
  once per minute (text swap, no animation) from the record's
  epoch. A hazard that moves is a hazard being marketed; this one
  sits and is watched.
- **States.** Posted (rest angle 1.5°, stripe edge) / updated
  (countdown text changes silently each minute) / stood-down
  (closest approach passed without event: the tag is struck
  through in pencil (§6.6) and a new note added "Passed at 412 m.
  Stood down." — it stays on the board for the rest of the round
  as history, it is not deleted in relief).
- **Content merge.** The tag's objects are catalogue entries with
  cards (§6.12) in their zones; the tag links to both. Its data —
  miss distance, epoch, probability as an exact figure — is the
  record's own. The element cannot exist without a live watch
  item; it is the record's most serious row, pinned where the
  round begins.
- **Failure fallback.** Printed statically under the masthead at
  its rest angle — the slide-in is JS-armed only. No-JS: the
  countdown prints as the fixed epoch time ("Closest approach:
  03:12 UTC, 15 NOV") rather than a live countdown — a static
  page tells the time, it does not pretend to tick.
- **Reduced-motion variant.** No slide, no settle: the tag is
  printed at its rest angle. The minute updates continue (text
  facts are not motion).
- **Performance budget & mobile variant.** One element, one
  gradient, one timer at 60s (not in the rAF loop — a minute
  countdown has no business in a frame budget). Mobile: the tag
  goes full-board-width under the masthead, stripe period 10px,
  data rows stack (objects / distance / epoch).
- **Choreography timeline (v2).** Load → t=200ms tag slides from
  under the clip (400ms) → settles at 1.5° (t=600ms) → patrol and
  round begin around it → each minute boundary: countdown text
  swaps → at closest approach +0: if stood down, pencil strike
  draws across the tag's headline (300ms, §6.6) and the stood-down
  note prints below → tag remains, history.
- **State matrix (v2).** *Rest:* posted. *Hover:* the tag lifts
  its rotation to 0° (held flat to read, 200ms). *Focus:* the
  tag's links (two object entries) take standard rings; the tag
  itself flattens as on hover when focus is inside it. *Active:*
  n/a. *Scrolled-past:* the tag stays with the masthead (it is
  not sticky beyond the header — a hazard you have read scrolls
  away like any fact; the rail (§6.11) does not carry it).
  *Disabled:* n/a. *Touch:* tap links; no hover flatten (the tag
  is readable at 1.5°).
- **Breakpoints (v2).** ≥1200px: tag 560px, right-pinned under the
  clip. 768–1199px: 480px. <768px: full width, stacked rows,
  stripe 10px period, rest angle 1°.
- **Edge cases & failure modes (v2).** *Watch data stale (record
  older than 24h):* the tag gains a pencil line "Board updated
  14 NOV, 22:40 UTC — check the office for tonight's figures."
  Staleness is printed, never hidden — a hazard tag with old data
  and no date would break the law. *Miss distance updates across
  the stand-down threshold mid-round:* figures update at the
  minute tick with a pencil note of the change ("412 m, revised
  from 380 m at 01:05") — revisions are ledger entries, not
  silent edits. *No watch item:* §6.15 occupies the slot (above).
- **Accessibility spec (v2).** `role="note"` with an aria-label
  summarising ("Conjunction watch: objects 1998-067A and
  2019-114C, closest approach 412 metres at 03:12 UTC"). Stripe
  is decorative (`aria-hidden` gradient). `--hazard` appears as
  text nowhere on the tag except the word WATCH in a chip whose
  text is `--ink` on `--hazard` at 6.83:1 — legal; on buff it
  would not be (§2's forbidden pairing is enforced here).
- **Tokens consumed (v2).** `--hazard`, `--ink`, `--buff`,
  `--pencil`, `--ease-settle`, `--ease-pencil`, `--dur-tag`
  (400ms).

### 6.14 The report-a-sighting form & its carbon receipt

- **What & why.** The round's conversion sheet: a form on the
  board's last sheet where a visitor — an amateur observer, a
  school astronomy club, another operator — files a sighting of a
  tracked object. Fields are ledger lines (object ID, time in
  UTC, where seen, what it did). On submission the form does not
  show a toast: the custodian *files it* — a receipt sheet prints
  below the form with the sighting restated, a receipt number
  derived from the board's own count ("Sightings filed this
  round: 412" is printed on the sheet; your receipt is № 413),
  and §6.6's carbon duplicate underneath. It belongs because
  conversion in this theme is joining the work, and the proof of
  joining is paperwork you can keep.
- **Structure.** A `<form>` on a buff sheet: four ruled field
  lines (label in Franklin small caps above the line, input as a
  borderless field sitting *on* the ledger rule, mono for ID and
  time), an object-ID helper (a link that opens §6.12's index in
  a sheet overlay to pick the object — the form never asks for an
  ID it won't help you find), and a submit button styled as a
  pencil-outlined box labelled "FILE THIS SIGHTING". Errors print
  in pencil-red — no: errors print in `--pencil` with a hazard
  tick (a 10px `--hazard` square) beside the field and a note in
  the custodian's voice (§12): the theme has no red; a mistake is
  a note in the margin, not an alarm. The receipt is a `.note`
  (§6.6) with a stamp-in (§6.15's press, smaller, in `--pencil`)
  reading "FILED — ROUND 412".
- **Motion spec.** Trigger: submit (valid). The form's sheet dims
  to 70% over 200ms while "filing" (≤900ms real or simulated
  round-trip), the receipt sheet slides up from under the form
  sheet over 450ms `--ease-settle` with its carbon ghost one frame
  behind (§6.6), and the stamp presses at t=500ms (140ms,
  `--ease-stamp`, scale 1.25→1, opacity 0→1). The receipt number
  is computed from the printed count + 1 — never from a random or
  a clock. Invalid submit: no motion except the error notes
  printing in (opacity, 180ms) and focus moving to the first
  error field.
- **States.** Blank (rules empty, helper offered) / filling
  (fields hold text on the rules) / error (per-field pencil notes,
  input preserved — the form never eats a sighting) / filing
  (≤900ms, submit disabled, sheet dimmed) / filed (receipt printed
  with carbon, form replaced by a one-line summary + "File
  another" reset link).
- **Content merge.** The receipt number, the round number and the
  filed-count all read the page's own printed figures — the form
  is the ledger's intake desk, and its paperwork reconciles with
  the board the visitor has just walked. The sightings count also
  appears in the handover (§6.17) — before the visitor files, it
  reads 412; the handover is build-time and does not chase the
  session's filings (§6.8's two-ledgers rule).
- **Failure fallback.** The form is a real form with a real
  action: no-JS submissions post to the endpoint and return a
  printed receipt page (server-rendered, same design, no stamp
  animation). If the endpoint fails, the sheet prints a pencil
  note — "The office line is down. Your sighting is still on this
  sheet — photograph it and send it to the office." — with the
  visitor's entries intact and a mailto route. Data is never lost
  to a network error in silence.
- **Reduced-motion variant.** No slide, no stamp press: the
  receipt prints complete (stamp at rest), the dimming is instant.
  Filing state is a text change ("Filing…") not an animation.
- **Performance budget & mobile variant.** Form is DOM text; the
  receipt adds one note element. Submit handler ≤5ms. Mobile:
  fields stack full-width (they already are lines), the ID helper
  overlay becomes a full-sheet takeover, the receipt prints below
  the form (never beside), stamp 100px wide.
- **Choreography timeline (v2).** Submit → validation (instant) →
  errors print (180ms) *or* filing state (dim 200ms) → response
  ≤900ms → receipt slides up t=0–450ms (carbon 1 frame late) →
  stamp presses t=500–640ms → count line on the sheet updates to
  413 filed (the sheet's own arithmetic, §1's law) → focus moves
  to the receipt's heading for AT.
- **State matrix (v2).** *Rest:* blank or restored. *Hover:*
  fields' rules deepen to `--ink` on hover of their line.
  *Focus:* the field's rule becomes a double rule (the line you
  are writing on is ruled twice — a ledger convention) + standard
  outline for AT parity. *Active:* submit presses (translateY
  1px). *Scrolled-past:* a filed receipt persists for the session.
  *Disabled:* during filing only; a disabled field never loses its
  value. *Touch:* ≥48px field rows; the date/time fields use
  native inputs (the ledger does not fight the platform's clock
  picker).
- **Breakpoints (v2).** ≥1200px: form sheet 640px, receipt beside
  the summary at right. 768–1199px: 560px, receipt below.
  <768px: full board width, helper overlay full-sheet, receipt
  below, stamp smaller.
- **Edge cases & failure modes (v2).** *Object ID not in the
  catalogue:* not an error — the form accepts it and the receipt
  adds a pencil line "Not in tonight's catalogue — the office
  will check it against the master book." An unknown sighting is
  data, not a typo; the theme's law is about the page's numbers,
  not the sky's. *Duplicate sighting (same ID + minute):* the
  receipt notes "Filed already as № 398 — this copy goes under
  it." and files as a carbon of the earlier receipt. *Very long
  "what it did" text:* the receipt's note area grows; the carbon
  follows §6.6's long-note rule.
- **Accessibility spec (v2).** Labels are real `<label>`s; errors
  are `aria-describedby` + `role="alert"` on the summary line
  only (fields are not individually alerted — one voice, the
  custodian's). Required fields are marked in the label text
  ("(needed)"), not by colour or asterisk alone. The receipt's
  arrival is announced via the focus move + an `aria-live`
  summary ("Filed. Your receipt is number 413.").
- **Tokens consumed (v2).** `--buff`, `--ink`, `--pencil`,
  `--hazard`, `--faded`, `--buff-dim`, `--ease-settle`,
  `--ease-stamp`, `--dur-file` (450ms).

### 6.15 The all-clear zone

- **What & why.** Some zones, some nights, have nothing on them:
  every object predicted, every check ticked, no refusal. That
  zone's sheet is mostly empty ledger lines, and across it the
  custodian presses a stamp: "ALL CLEAR — NOTHING ON THIS PART OF
  THE ROUND" in `--clear`, rotated −3°, in Special Elite capitals.
  It belongs because an honest ledger records the quiet zones with
  the same ceremony as the busy ones — and because a page where
  every section shouts with content teaches the visitor that
  emptiness is failure, when in orbital hygiene emptiness is the
  entire goal.
- **Structure.** A zone sheet (§4 pattern) with its header strip
  and count line ("0 ITEMS — ALL PREDICTED"), three to five empty
  ruled item rows (printed rules, no boxes — there is nothing to
  tick), and the stamp: an SVG-bordered double-rule oval-rectangle
  (border 3px `--clear`, inner 1px), text in two lines, pressed
  over the empty rows at the sheet's centre-left, overlapping one
  rule — a stamp lands on the paper, not in a layout slot. The
  stamp's ink is uneven by design (an SVG turbulence mask at 4%
  erosion) — a real stamp never inks evenly, and the unevenness
  is printed, not animated.
- **Motion spec.** Trigger: the sheet's entry into view (55%
  line). The stamp presses: from scale 1.3 / opacity 0 / rotate
  −6° to rest (1 / 1 / −3°) over 220ms `--ease-stamp` (the
  system's one overshoot, §5) with a 60ms paper settle (the sheet
  itself translates Y 1px and back — the desk felt that). Once
  pressed, never repeated. The empty rows do not animate in; they
  were always there.
- **States.** Unpressed (pre-entry: the stamp is *absent* — this
  is the one element whose pre-state is absence rather than a
  printed rest state, because an unpressed stamp is not a thing
  that exists; its fallback below covers the no-JS case by
  printing it) / pressing (220ms) / pressed (permanent).
- **Content merge.** The all-clear is a data state of a real zone,
  declared in the record (`"clear": true`). It cannot be used as
  a decorative divider: a zone with items cannot wear the stamp,
  and the gate (§10) checks the record, not the rendering.
- **Failure fallback.** No-JS and reduced-motion: the stamp prints
  at rest (full opacity, −3°) — the sheet ships complete. JS
  *removes* it at arm time (before first paint of the sheet, via
  the arming class on `<html>`) and presses it on entry; if the
  script dies between arm and entry, the §6.16 watchdog (2400ms
  from arm) re-prints every armed element to its rest state,
  stamp included. The one absence in the theme is watchdogged
  like everything else.
- **Reduced-motion variant.** Stamp printed at rest; no press, no
  paper settle. (Stated above; repeated here because this element
  is the reduced-motion test case the gate uses.)
- **Performance budget & mobile variant.** One SVG + text; the
  press is a single transform. Negligible. Mobile: stamp scales
  to 78% width, rotation −2.5°, still overlapping a rule; the
  empty rows reduce to three (a phone sheet is shorter; the
  quiet is the same size emotionally, smaller physically).
- **Choreography timeline (v2).** Sheet crosses 55% line → rows
  already printed → t=80ms stamp begins (scale 1.3, opacity 0) →
  t=300ms stamp lands (overshoot settles by t=340ms) → paper
  settle t=300–360ms → rest, permanent → the round continues; the
  zone header's count line was already printed "ALL PREDICTED" —
  the stamp confirms the header, it does not inform it.
- **State matrix (v2).** *Rest:* pressed. *Hover:* none (a stamp
  is not a control). *Focus:* the sheet's header link focuses as
  normal; the stamp is `aria-hidden` decoration over a text fact
  (the header's count line states it accessibly). *Active:* n/a.
  *Scrolled-past:* pressed. *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: stamp 340px wide at centre-left.
  768–1199px: 300px. <768px: 78% of sheet width, −2.5°, rows = 3.
- **Edge cases & failure modes (v2).** *A zone becomes non-clear
  in a record update (an object is added):* the stamp is removed
  at build; the sheet gains its item rows; yesterday's all-clear
  is mentioned in the handover (§6.17) — "Zone F, clear last
  night, has one item tonight." Quiet is historical too. *Two
  consecutive clear zones:* both stamp; the second stamp's
  rotation differs (−2°) by record seed — stamps land by hand,
  not by template. *Print:* stamp prints in `--clear` (print CSS
  keeps the colour — it is the sheet's content).
- **Accessibility spec (v2).** The stamp is `aria-hidden`; the
  accessible fact is the header's text ("Zone F — all clear,
  nothing on this part of the round, all objects predicted").
  `--clear` on `--buff` is 4.64:1 — legal for the stamp's large
  (≥14pt bold-equivalent) lettering, and the gate forbids `--clear`
  at smaller sizes anywhere.
- **Tokens consumed (v2).** `--clear`, `--buff`, `--ink`,
  `--ease-stamp`, `--dur-stamp` (220ms).

---

### 6.16 Lights-up skeleton & the lights-dip transition

- **What & why.** Loading in this theme is the board before the
  round begins: unruled buff sheets with a printed pencil note —
  "ROUND NOT YET BEGUN — THE BOARD IS BEING PINNED UP" — and the
  masthead's clip already in place. There is no shimmer (paper
  does not shimmer) and no spinner (a ledger office does not
  spin). Between sheets (client-side navigation in app builds),
  the transition is a lights-dip: the room's light dips to
  `--ink-deep` and returns as the new sheet is pinned. It belongs
  because waiting, in a working building, is a lit room with the
  board not yet up — and because the theme's law (nothing stays in
  the dark) makes the loader a legal problem, solved by making
  the waiting state itself fully legible.
- **Structure.** Skeleton: the real page skeleton (masthead,
  section sheets at their true heights via `min-height` from the
  layout) in `--buff` with rules at 20% opacity and the printed
  note; no fake text bars — the sheets are *blank paper*, sized
  honestly. The watchdog is a plain `setTimeout` at arm: 2400ms
  after arming, any sheet still in skeleton state is force-lit
  (skeleton class removed, real content — which was in the DOM
  all along under the skeleton sheets — revealed). Lights-dip: a
  fixed overlay in `--ink-deep` at 0% → 88% → 0% opacity over
  260+260ms, content swapped at the dip's floor (t=260ms), with a
  hard abort at 1200ms that fades the overlay out over whatever
  content exists.
- **Motion spec.** Trigger: navigation / data wait. Skeleton has
  **no looped animation** — a still board and a printed note; if
  the wait exceeds 4000ms the note gains a second printed line
  ("Still pinning. The office line is slow tonight.") — patience
  acknowledged in pencil, once. Lights-dip: 520ms total
  `--ease-settle`, once per navigation, never chained.
- **States.** Pinning (skeleton, note) / pinning-long (second
  line, >4000ms) / lit (real board) / dipping (transition) /
  aborted-dip (watchdog fade).
- **Content merge.** The skeleton's sheets are the page's own
  layout at its own sizes — the wait shows the visitor the shape
  of the board they are about to read, and the note is written in
  the custodian's voice (§12), not in a design system's
  ("Loading…"). The dip is the building's light, the same light
  the beam (§6.1) works by.
- **Failure fallback.** This element *is* the fallback system: the
  2400ms watchdog guarantees no skeleton outlives its welcome, and
  the content under the skeleton is complete DOM — disabling CSS
  animations, or the stylesheet entirely, leaves a readable page
  with blank sheets between real sections (ugly, legible, legal).
  No-JS: no skeleton is ever inserted (it is JS-armed); the page
  simply arrives.
- **Reduced-motion variant.** No dip (sheets swap instantly with a
  printed "SHEET CHANGED" pencil line at the new sheet's head for
  orientation). Skeleton identical — it never moved.
- **Performance budget & mobile variant.** Skeleton is the layout
  itself; the dip is one overlay opacity animation. Zero ongoing
  cost. Mobile: identical; the dip's floor opacity is 92% (a
  smaller room dips darker — and shorter attention is respected
  with the same 520ms, not a faster cut).
- **Choreography timeline (v2).** Navigation → dip overlay rises
  t=0–260ms → content swaps at t=260ms → overlay falls
  t=260–520ms → new sheet lit, its zone underline (§6.10) already
  correct → watchdog deadline t=1200ms passes. Data wait: skeleton
  prints at t=0 → content arrives → sheets light in one
  300ms `--ease-settle` warmth pass → *or* watchdog fires at
  t=2400ms and lights whatever exists → long-wait line at
  t=4000ms only if still pinning.
- **State matrix (v2).** *Rest:* lit board. *Hover:* none.
  *Focus:* during a dip, focus is held on the document (not moved
  into hidden content); on the new sheet, focus lands on its
  heading (tabindex −1) — announced by the heading itself.
  *Active:* n/a. *Scrolled-past:* n/a. *Disabled:* with JS
  disabled, the element does not exist. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: skeleton sheets at desktop
  heights. 768–1199px / <768px: skeleton mirrors each layout's
  true heights (the skeleton is generated per-breakpoint from the
  same CSS, never a fixed pixel guess).
- **Edge cases & failure modes (v2).** *Back-to-back navigations:*
  dips never queue — a second navigation during a dip cuts the
  dip at its current opacity and starts from there. *The data
  never arrives:* the watchdog lights the board and §6.12's
  unavailable note pattern applies per-sheet ("index unavailable —
  the ledger office has the full book"). *Slow fonts:* the
  skeleton does not wait for fonts; the lit board reflows once
  when they land, inside fixed-height sheets, so the reflow is a
  text swap, not a layout jump.
- **Accessibility spec (v2).** The skeleton region carries
  `aria-busy="true"` until lit, and the note is real text (AT
  reads "Round not yet begun"). The dip overlay is `aria-hidden`;
  sheet changes are announced by the new heading's focus. Nothing
  about the wait is conveyed by animation alone.
- **Tokens consumed (v2).** `--buff`, `--ink-deep`, `--pencil`,
  `--ease-settle`, `--dur-dip` (520ms), `--dur-watchdog` (2400ms).

### 6.17 The shift handover footer

- **What & why.** The board's back page: the handover. Tonight's
  round restated as the next custodian will receive it — the
  catalogue totals (§6.4's figures, third printing), the round's
  outcome ("36 items — 30 ticked, 6 to re-check tomorrow"), the
  argued-about object's status in one line, the sightings filed,
  and a signed note in Special Elite: "Board left as found. The
  beam is on its hook. — C." Below it, the ordinary footer matter
  (organisation, links, small print) set as ledger entries. It
  belongs because a round that does not hand over is a round that
  did not happen; the footer is where the theme's whole fiction of
  tended data becomes an organisational promise.
- **Structure.** A full board sheet, darker at its edges (the back
  of the board: `--buff` shaded to `--buff-dim` at the margins):
  a handover table (mono figures, Franklin labels — the same
  record, build-time printed), the signed note as a §6.6 note
  *with its carbon* (the handover is the one note whose duplicate
  matters most — it is the copy the office files), the rail's
  parked final state (§6.11) as the table's first row, then the
  conventional footer columns styled as a ledger index, and a
  colophon line in mono: "Set in Libre Franklin, Special Elite
  and IBM Plex Mono. Totals unrounded, as found."
- **Motion spec.** Trigger: entry into view. The handover table's
  figures do **not** count up — they are printed, third time, at
  rest (counting is §6.4's ceremony, performed once; a footer
  that re-performs it teaches the visitor the numbers are
  theatre). The signed note's strike-free carbon sits static. The
  only motion: the beam, off-stage since the hero, is *not*
  present; instead the sheet lights with §5's zone warmth at
  entry (600ms). The stillness is the point — the round is over.
- **States.** Printed (always, from first paint) / lit (warmth
  pass done). No interactive states of its own; its links are
  ordinary footer links with §5's pencil-underline hover.
- **Content merge.** Every figure in the handover traces to the
  same catalogue and round records as §6.4 and §6.11 — the gate
  (§10) reconciles all three printings mechanically. The handover
  is the audit that the page's numbers were one set of numbers.
- **Failure fallback.** Static print — there is nothing to fail.
  No-JS: identical. If the session's round state (§6.8) differs
  from build time, the handover prints the *build-time* round
  outcome and a pencil line acknowledges the session: "This copy
  printed at the round's start. Tonight's ticks are on the
  board." — the two-ledgers rule (§6.8) stated at the exact place
  a careful reader would catch it.
- **Reduced-motion variant.** Identical; the warmth pass is
  skipped, the sheet is lit at rest.
- **Performance budget & mobile variant.** Static sheet; nil.
  Mobile: the handover table stacks label-over-figure; the signed
  note keeps its carbon (the duplicate survives every breakpoint —
  it is the point); footer columns stack as ledger entries with
  rules between.
- **Choreography timeline (v2).** Footer sheet enters → warmth
  pass t=0–600ms → rail parks (§6.11's final beat, same moment) →
  nothing else. The absence of further beats is specified so a
  builder does not invent a sign-off animation: the custodian
  does not perform leaving; he leaves the board as found.
- **State matrix (v2).** *Rest:* printed. *Hover:* links underline
  in pencil (120ms draw). *Focus:* standard rings. *Active:* n/a.
  *Scrolled-past:* n/a. *Disabled:* n/a. *Touch:* links at 44px
  rows in the stacked index.
- **Breakpoints (v2).** ≥1200px: table 3 columns, note at right.
  768–1199px: 2 columns. <768px: stacked, note full width with
  carbon below (§6.6's long-note rule).
- **Edge cases & failure modes (v2).** *A round with zero visitor
  ticks:* the handover's sightings/visitor lines print their true
  figures including zero ("Visitor ticks tonight: 0. The round
  was walked alone.") — the theme prints zeroes; it does not omit
  embarrassing rows. *The argued object resolved since §6.5 was
  built:* impossible within one build — the record is one record;
  cross-build changes are §6.5's retirement rule.
- **Accessibility spec (v2).** The handover table is a real
  `<table>` with a caption ("Tonight's handover"). The signature
  "— C." is text. The colophon is text. Contrast throughout is
  the reading pair (11.56:1) and `--pencil` notes (5.80:1).
- **Tokens consumed (v2).** `--buff`, `--buff-dim`, `--ink`,
  `--pencil`, `--faded`, `--ease-settle`.

### 6.18 Object not in the ledger — the 404

- **What & why.** The error page is a blank ledger sheet: a ruled
  page with one line written on it in Special Elite — "Looked.
  It isn't in the book." — the requested ID (echoed in mono, as
  typed) struck through in pencil, and below, the three useful
  doors: the catalogue index (§6.12), the current round (§6.10's
  zones), and the sighting form (§6.14 — "If you have seen it,
  file it: the book grows by sightings."). The dark field borders
  the sheet, and in it, far off, one untracked point glints once
  — the thing that was looked for, not found, still up there. It
  belongs because a 404 in this theme is a ledger lookup that
  failed, and the custodian's response to a failed lookup is a
  procedure, not a joke page.
- **Structure.** The standard board sheet, mostly empty rules; the
  echoed ID in mono inside a §6.2-style box (unticked — it will
  never tick); the pencil strike across the ID; the note; three
  link rows styled as ledger entries with mono counts ("THE
  CATALOGUE — 34,127 ENTRIES" — the record again); the field
  margin with a single point. No beam patrol here: the beam is
  *resting* — a static, dim pool at the sheet's lower corner,
  because on the error page the round is not being walked.
- **Motion spec.** Trigger: load. Choreography is specified as
  *nearly none*: the strike draws once over 300ms `--ease-pencil`
  at t=400ms; the lone point glints once at t=1600ms (300ms,
  §6.1's glint) and does not repeat. Everything else is print. A
  404 that performs is a 404 that is pleased with itself.
- **States.** Printed (with strike drawn) / printed (strike
  undrawn — no-JS and reduced motion ship it drawn; the draw is
  JS-armed only, over a printed struck state: the HTML ships with
  the strike complete, JS *un-draws* it at arm and redraws —
  the §6.15 pattern).
- **Content merge.** The three doors are the site's real recovery
  routes with their real counts; the sighting-form door turns the
  error into the theme's conversion — a visitor who arrived
  looking for an object the book lacks is precisely a person with
  a sighting to file.
- **Failure fallback.** The page is static print with two small
  enhancements; any failure leaves a complete, useful error page.
  The server must return a real 404 status — the theme's honesty
  extends to HTTP.
- **Reduced-motion variant.** Strike printed, no glint. The point
  is printed at rest brightness.
- **Performance budget & mobile variant.** The lightest page in
  the theme (≤40KB total). Mobile: the sheet fills the board; the
  field margin and its point move above the sheet as a 64px
  strip — the glint still happens once, in the strip.
- **Choreography timeline (v2).** t=0 sheet printed, strike
  complete (server state) → JS arms: strike un-draws instantly
  (pre-paint class) → t=400ms strike redraws (300ms) → t=1600ms
  the point glints once (300ms) → rest, permanent. No loop, no
  patrol, no second glint.
- **State matrix (v2).** *Rest:* printed, struck. *Hover:* the
  three doors take §6.17's pencil-underline hover. *Focus:*
  standard rings; focus order is note → doors. *Active:* n/a.
  *Scrolled-past:* n/a (the page rarely scrolls). *Disabled:*
  n/a. *Touch:* doors at 48px rows.
- **Breakpoints (v2).** ≥1200px: sheet centred, field margins
  both sides with the point in the right margin. 768–1199px:
  narrower margins, point kept. <768px: 64px field strip above
  the sheet (above), sheet full width.
- **Edge cases & failure modes (v2).** *The echoed ID is long or
  hostile:* it is echoed as text (escaped, truncated at 40
  characters with a pencil "…" — the ledger writes what fits the
  line), never as HTML. *The ID is *nearly* in the book (one digit
  off a real entry):* the page does **not** guess — no "did you
  mean" — because a ledger that guesses teaches visitors to trust
  near-misses; the catalogue door is the honest route. *A 404 for
  an image/asset:* the server serves this page only for document
  routes; assets fail silently as assets should.
- **Accessibility spec (v2).** The heading is the note itself
  ("Looked. It isn't in the book.") as an `<h1>`; the struck ID
  carries hidden text "(not in the catalogue)". The glint is
  `aria-hidden`. The page works fully with every enhancement off.
- **Tokens consumed (v2).** `--buff`, `--ink`, `--pencil`,
  `--ink-deep`, `--beam`, `--ease-pencil`, `--dur-check` (300ms).

---

## 7. Page application map

| Page type | How the theme plays out |
|---|---|
| **Home — the round** | The full round as specified: hero field + beam (§6.1), totals (§6.4), zones A–F with checks and refusals (§6.2/§6.3), argued object after its zone (§6.5), hazard tag if the record holds one (§6.13), sighting form (§6.14), handover (§6.17). This is the reference build; every other page is a sheet from this clipboard. |
| **Catalogue index** | §6.12 at full size: filter checklist, card grid (48 per page, §11 pagination), sample honestly labelled with the full count, and the complete catalogue as a downloadable ledger file (CSV/JSON) — the theme's answer to "34,127 cards can't be a web page": the book is a file, the page is its reading room. |
| **Object entry (detail)** | One object's full sheet: its large card, its arc (both ephemerides if argued), its observation history as a mono table, its polaroid if one exists (§6.9), its zone's checklist with its own row in context. The beam does not appear; the entry is read under the board's lamp, not searched by torchlight. |
| **About / the custodian** | The method, written as the handover's long form: how the catalogue is kept, where the data comes from (named sources with dates), why totals never round, who "C." is organisationally (a role, not a person — §1's rule). Polaroids of the office, the predecessor's board. No beam; about pages are daytime. |
| **Methodology / data quality** | The refusals, collected: every §6.3 item across zones with its two candidate fates, the argued object's full file, the staleness rules (§6.13) as policy. This page is the theme's honesty, indexed — link it from every totals strip. |
| **Report a sighting (conversion)** | §6.14 as a standalone sheet (same form, same receipt arithmetic, round number from the live board) for deep-linking from partner sites and the 404. |
| **404** | §6.18, exactly as specified. |

Pages the theme **refuses**: checkout/payment (a ledger of other
people's dead satellites takes no money on the board — donations
or subscriptions live on a plain, unthemed utility page linked
from the handover, and §12's voice rules say so plainly), and any
live-operations view (§1's when-NOT-to-use).

---

## 8. Worked examples

One catalogue record serves all three examples — the standard
round: **Round 412, night of 14 Nov.** Catalogue: 34,127 tracked,
34,126 predicted, 1 argued about (OBJ 1998-067A). Round checklist:
36 items across six zones (A: Parking Orbit 6, B: The Busy Belt 8,
C: The Dawn-Dusk Line 5, D: The Southern Pass 7, E: The Graveyard's
Edge 4, F: The High Shelf 6), one refusal per zone. Sightings filed
this round before the visitor arrives: 412. Watch item: OBJ
1998-067A × OBJ 2019-114C, closest approach 412 m at 03:12 UTC.

### 8.1 The hero — the round begins (worked example 1)

The visitor lands on darkness that is not empty. The field
(`--ink-deep`) holds 24 points, each a real object from the
record's priority list, printed at rest with the field lit to 85%
— readable before any script runs. The headline card, a buff sheet
taped at the field's left, carries the round's title in Libre
Franklin 800 at clamp(2.75rem, 6.2vw, 4.75rem): "Everything up
there is somebody's job to watch." Beneath it, Special Elite: "Round
412 — night of 14 Nov. The board is current as of 22:40 UTC." The
hazard tag (§6.13) hangs under the masthead at its 1.5° rest angle:
the 1998-067A conjunction, 412 m, 03:12 UTC, and the pencil line
"Watching it. Nobody moves anything yet."

At t≈800ms the beam fades in on its patrol phase and begins the
26s/17s dual-period walk. Its first crossing (≈t=3.2s) glints OBJ
2006-031B and flips its card: "OBJ 2006-031B — ROCKET BODY —
PREDICTED UNTIL 2041." The visitor scrolls; nothing in the hero
parallaxes except the field's points at 0.96× — the board's edge
is visible at the fold, buff against the dark, and the totals
strip (§6.4) crosses the 60% line: 34,127 rolls in over 1200ms
and stops dead; 34,126 follows; "One we argue about." fades in
last, linked to §6.5's sheet. **Scroll timeline:** hero patrol
(ambient) → tag already posted (t=600ms) → first glint ≈3.2s →
headline card raised by the first sweep ≈9s → totals count at
first scroll → Zone A's sheet lights at 25% entry. Nothing waited
for anything; every beat had a printed state beneath it.

### 8.2 Mid-page — Zone C and the argued object (worked example 2)

Zone C, The Dawn-Dusk Line: five items. The sheet's header reads
"ZONE C — THE DAWN-DUSK LINE · 5 ITEMS — 4 TICKED, 1 TO RE-CHECK"
(the count updates live as the round is walked). Four items tick
as the visitor passes them — §6.2's strokes, 300ms each, the
frontier item drawing as it crosses the 66% line. One item is the
visitor's (§6.8): "Confirm the dawn-dusk shell count against the
board — your call." Below the checklist, the zone's cards sit in
the margin (§6.12), and its refusal (§6.3) is OBJ 2011-052A, whose
dashed arc argues harder as the visitor scrolls fast toward the
next sheet — amplitude to 7px — and settles to its 1px tremor as
they slow to read.

Then the argued-about object's half sheet (§6.5). Two dashed arcs
diverge across 120px of buff: the office ephemeris and the
observer network's, 14px apart at apogee. Two pencil notes, dated
NIGHT 214 and NIGHT 231: "decaying — down by spring." / "checked
twice — holding." Under them, in Franklin, the methodology line:
"Two predictions can disagree because the air up there is weather
nobody can measure directly. The book keeps both until one of
them is wrong in public." The visitor hovers: both arcs still to
their printed paths — the disagreement, held flat for inspection.
**Scroll timeline:** zone lights (600ms warmth) → four checks draw
in passage → refusal wobble couples to scroll velocity → argued
sheet enters, tremor at rest → hover stills the arcs → Zone D's
header strip pins as C's sheet ends.

### 8.3 Conversion — filing a sighting (worked example 3)

The board's last sheet before the handover is the sighting form
(§6.14). The sheet's head prints the round's intake state:
"Sightings filed this round: 412." A school club visitor, who
watched a tumbling rocket body cross at 19:04 UTC, fills the four
lines: object ID (they use the helper overlay and pick OBJ
2006-031B from the index — the same object the hero's beam glinted
in §8.1; the page's objects recur because the catalogue is one
book), time "19:04 UTC", place "Multan — school roof", behaviour
"tumbling — flashes every few seconds". They mistype the time as
"25:04": the field's rule gains a hazard tick and a pencil note —
"That hour isn't on the clock. The UTC time as your clock showed
it will do." — input preserved. Corrected, they submit: the sheet
dims (200ms), and the receipt prints below: the sighting restated,
receipt **№ 413** (= the printed 412 + 1, the law's arithmetic),
the "FILED — ROUND 412" stamp pressed at t=500ms, and the carbon
underneath, one frame late, slightly worse — theirs to keep.
**Scroll timeline:** form sheet lights → helper overlay opens as a
sheet over the board (no modal chrome) → error prints in place →
filing dim ≤900ms → receipt slide 450ms → stamp 140ms → handover
sheet below, already printed with the round's build-time figures
and its honest line about session ticks.

---

## 9. Anti-slop — what makes THIS theme look cheap

1. **The rounded total.** "34K+ objects tracked!" — the theme's
   capital crime. *Cure:* the law (§1). Every total is exact,
   mono, and traced to the record; the gate greps for "K+", "~"
   and "approx" near any figure.
2. **Stars that are not objects.** A decorative starfield
   background turns the catalogue into wallpaper and lies at
   pixel scale. *Cure:* every point in the field is a record
   entry with an ID; if it has no ID, it is not drawn.
3. **The beam as cursor toy.** The moment the flashlight follows
   the mouse, the custodian vanishes and a gimmick remains.
   *Cure:* the beam is autonomous (§6.1); the pointer's only
   power is the lean (§6.7).
4. **Hazard everywhere.** Hazard-striped dividers, hazard buttons,
   a hazard "brand colour" — the signal dies of abundance.
   *Cure:* the §2 ration (one tag per zone maximum, stripe only
   as §6.13's edging); the gate counts instances.
5. **The cartoon custodian.** A mascot with a mop among the
   satellites. *Cure:* §1's rule — he exists as handwriting, a
   patrol path and a voice, never as a figure.
6. **Checks that animate like a game.** Bouncy ticks, particle
   bursts, a "+1!" floater on §6.8. *Cure:* a check is a pencil
   stroke at 300ms with a wobble; the total changes silently.
   Work is not celebrated; it is recorded.
7. **Carbon ghosts as a blur filter.** Faking §6.6 with a blurred
   duplicate or a text-shadow smear. *Cure:* the carbon is real
   text on a real second slip, misregistered by 2px, lagging one
   true frame — mechanism, not effect.
8. **A refusal that resolves.** A "re-check tomorrow" item that
   ticks when the visitor reaches the footer, "for a sense of
   completion". *Cure:* §6.3/§6.5 — refusals resolve between
   builds, when the data does, never within a page view.
9. **Typewriter font as headline.** Special Elite at 40px turns
   the ledger into a themed restaurant menu. *Cure:* §3's type
   law 2 — the hand annotates; Franklin announces.
10. **Fake handwriting fonts for the notes.** A script font
    pretending to be handwriting. *Cure:* the notes are Special
    Elite (a typewriter — the ledger's actual machine) and pencil
    *strokes* are SVG; no script face is loaded, ever.
11. **Dashboard creep.** Sparklines, donut charts and KPI tiles
    sneaking into the zones because "users expect data viz".
    *Cure:* the theme's data forms are the table, the card, the
    arc and the total. A chart that is not one of those is cut at
    review, however good it looks.
12. **The beam hiding content.** A card that can only be read
    while the light is on it. *Cure:* §2's legibility rule — cards
    are buff and readable in the dark; the beam adds the glint
    and the flip, never the legibility. Test: screenshot with the
    beam parked — everything reads.

---

## 10. Quality gate

Blocking checks — all must pass before this theme ships in a
build:

1. **Figure audit.** Every number printed on the page traces to
   the catalogue/round record; a script greps the build for
   totals and compares them to the record. Any hard-coded or
   rounded figure ("34K", "~34,000") fails.
2. **Point census.** Every point in the hero field has an ID in
   the record; decorative points = fail.
3. **Hazard census.** ≤8 hazard instances page-wide; stripe only
   in §6.13's edging and zone tags (§2 ration).
4. **Lights-up test.** JavaScript disabled: the whole page reads
   — beam absent, cards face-up, checks printed, stamp printed,
   totals exact. Any content reachable only via animation = fail.
5. **Watchdog drill.** Block the rAF loop artificially: beam
   removes itself by 3000ms, skeleton lights by 2400ms, counts
   restore exact figures by 1600ms.
6. **Refusal integrity.** Each zone's refusal is declared in the
   record, never ticks in any state, and its note is printed
   text. A zone with no earned refusal wears §6.15's stamp
   instead — inventing a refusal fails the gate as surely as
   hiding one.
7. **Argued-object reconciliation.** §6.4's third figure, §6.5's
   object, and §6.17's handover line name the same object ID.
8. **Three-printings check.** Catalogue totals appear identically
   in §6.4, §6.11's basis, and §6.17 — mechanically diffed.
9. **Reduced-motion pass.** With `prefers-reduced-motion`: the
   completed-round state — board lit, checks printed, arcs at
   rest paths, stamp printed, no patrol, no tremor, no dip.
10. **Contrast audit.** Reading pair 11.56:1; pencil notes
    5.80:1; `--pencil-soft` never under 14px-equivalent large
    text; `--hazard` never as text on `--buff`; `--clear` only at
    stamp sizes; `--faded` only on `aria-hidden` carbons with
    their original adjacent.
11. **Motion budget.** Two ambient loops maximum (patrol, argued
    tremor), both pausing off-screen and on hidden tabs; one rAF
    loop total; no scroll listener writes styles.
12. **Form honesty.** Receipt arithmetic derives from a printed
    count on the same sheet; a receipt number that cannot be
    re-derived by the visitor from the page fails.

Minimum bar: 12/12. This theme's gate is unusually mechanical
because its law is unusually checkable — that is the point of it.

---

## 11. Component inventory

Every component a real site in this theme needs, with its themed
treatment — or its refusal, with the in-theme replacement.

| Component | Treatment in this theme |
|---|---|
| Primary button | A pencil-outlined box on buff ("FILE THIS SIGHTING"), Franklin 600; press = 1px translate; never filled with hazard or clear |
| Secondary button | Plain underlined Franklin text with the 120ms pencil-underline draw on hover |
| Text input | A ledger line: borderless field on a printed rule; focus = double rule (§6.14) |
| Select / picker | The index overlay (§6.14's helper): a sheet of §6.12 cards to pick from — no native dropdown styling fight |
| Checkbox | §6.2's box + self-drawing check — the theme's native control |
| Radio group | Checklist rows with a single tick enforced; the unticked options keep empty boxes |
| Tabs | Zone tabs (§6.10) — the only tabs; content tabs inside a zone are refused (a zone is one sheet, read top to bottom) |
| Accordion | Refused. Ledger sheets do not fold; long content is a longer sheet with a pinned zone header (§4) |
| Modal / dialog | Refused as chrome; the one overlay need (ID picker) is a *sheet over the board* (§6.14) with the board visible at its edges |
| Toast | Refused. Outcomes are filed as receipts (§6.14) or printed as pencil notes in place; nothing floats and vanishes from a ledger |
| Alert / banner | The hazard tag (§6.13) for watch items; pencil notes in place for everything lesser |
| Badge / chip | State glyphs on cards (§6.12) + the mono count lines; coloured pill badges refused — states are glyphs and words |
| Pagination | Ledger folios: "SHEET 3 OF 12" in mono with prev/next as ledger entries; the index's sample labelling (§6.12) applies |
| Table | The handover table (§6.17) pattern: mono figures, Franklin labels, 32px rules, no zebra (zebra is not a paper) |
| Card | §6.12 — the theme's atom |
| Progress bar | Refused; replaced by the checklist rail (§6.11) |
| Spinner | Refused; replaced by the lights-up skeleton (§6.16) |
| Skeleton | §6.16 — blank ruled sheets + printed note, no shimmer |
| Tooltip | A pencil note that prints beside the item on focus/hover (positioned text, never a floating grey box) |
| Breadcrumbs | The zone path as a ledger line: "ROUND 412 › ZONE C › OBJ 1998-067A" in mono at the entry sheet's head |
| Search | The catalogue index with its filter checklist (§6.12); free-text search is a mono input whose results are cards — no search "experience" beyond the book |
| Empty state | §6.15's all-clear pattern (or its miniature in §6.12's zero-results) |
| Error state | §6.18's pattern for pages; §6.14's pencil notes for fields |
| Avatar / identity | Refused — the custodian has no face (§1); organisational identity is the masthead's title sheet |
| Toggle / switch | Refused; binary states on a ledger are ticks in boxes |

---

## 12. Content & copywriting voice

Two registers, kept apart by law. **The printed form** (Libre
Franklin) is the ledger's official voice: plain, complete
sentences, no slang, no exclamation marks anywhere on the page.
**The custodian's notes** (Special Elite) are one working person's
marginalia: short, dry, exact, occasionally wry — never cute.

- **Headlines** (printed form): a statement of fact with the
  number in it where possible. ✓ "34,127 objects. One ledger."
  ✗ "Guardians of the Galaxy's Junkyard!" — exclamation, rounding
  and a joke the data didn't make.
- **Labels** (mono): literal and short. ✓ "LAST CONFIRMED" /
  "ORBIT CLASS" / "TO RE-CHECK". ✗ "Freshness score" / "Risk
  vibes".
- **The custodian's notes**: ✓ "Still up there." / "Checked
  twice — holding." / "Watching it. Nobody moves anything yet."
  ✗ "Oopsie, this one's playing hard to get!" — the custodian is
  tired, not adorable.
- **Error messages** (form): a note in the margin, in his voice,
  saying what would do. ✓ "That hour isn't on the clock. The UTC
  time as your clock showed it will do." ✗ "Invalid input!!".
- **Empty states**: ✓ "Nothing on this part of the round."
  ✗ "All caught up 🎉" — no emoji anywhere in the theme, ever.
- **Numbers**: exact or admitted. ✓ "34,126 predicted." /
  "Not yet counted." ✗ "Over 34,000!" / "≈34.1K".
- **Fixed strings (verbatim, never paraphrased):** the totals
  line "34,127 objects tracked. 34,126 predicted. One we argue
  about." (figures from the record, words fixed); "RE-CHECK
  TOMORROW"; "ALL CLEAR — NOTHING ON THIS PART OF THE ROUND";
  "Board left as found. The beam is on its hook."; the 404 line
  "Looked. It isn't in the book."
- **Dates and times** are UTC, always, with the date printed
  ("03:12 UTC, 15 NOV") — orbit keeps one clock and the page
  says which.

---

## 13. Full-page scroll choreography map

The home page, top to footer, in the order the visitor lives it.
One shared rAF loop (lerp 0.12) drives every scrubbed value;
beats are listed at their trigger points.

1. **First paint.** Board and field ship lit at 85%; masthead,
   clip, hazard tag printed at its rest angle; totals printed
   exact. *Feels like:* arriving at a desk where the paperwork is
   already out.
2. **t≈600ms.** The hazard tag finishes its slide from under the
   clip (§6.13) — the only entrance the page performs unprompted.
3. **t≈800ms.** The beam fades in on patrol (§6.1). First glint
   ≈3.2s; first card flips. *Feels like:* someone is at work
   here, and was before you arrived.
4. **First scroll.** Field points parallax at 0.96×; the beam
   keeps patrolling until the hero leaves, then parks dimmed at
   its rest corner.
5. **Totals strip crosses 60%.** 34,127 counts (1200ms) and stops
   dead; 34,126 follows; "One we argue about." fades in last
   (§6.4). The rail (§6.11) pins as the strip passes.
6. **Zone A sheet enters (25%).** Warmth pass (600ms). Its
   checklist's frontier item draws as it crosses the 66% line
   (§6.2); its refusal's arc trembles at rest (§6.3). Zone header
   pins within the zone; nav underline draws under A (§6.10).
7. **Zones B–F repeat the grammar** — light, ticks in passage,
   one refusal each, zone counts updating in the headers and the
   rail. In Zone B the visitor meets their first offered item
   (§6.8) and may tick it; the rail increments in the same beat.
   Zone F, if the record says so, is the all-clear: the stamp
   presses at 55% entry (§6.15) and the round exhales.
8. **After Zone C: the argued object** (§6.5). Scroll velocity
   feeds its wobble as the visitor arrives fast; it settles to
   its tremor as they slow to read. Hover holds both arcs flat.
9. **Polaroids** settle into their taped frames as they cross 50%
   (§6.9), one repaired corner somewhere on the page.
10. **The sighting form sheet.** The intake count is printed
    ("412 filed"); the visitor may file (§6.14) — receipt, stamp,
    carbon — or simply read past it; the round does not require
    their paperwork.
11. **The handover** (§6.17). Warmth pass; the rail parks into
    the table's first row; totals stand printed for the third
    time, uncounted, at rest. *Feels like:* the end of a shift,
    the board left as found.
12. **Reverse pass.** Scrolling back up: checks stay drawn,
    totals stay landed, the stamp stays pressed, the beam resumes
    its patrol when the hero re-enters (from its parked phase,
    never restarted). Nothing un-happens on this page; the round
    is a record, and records read the same backwards — only the
    frontier was ever in motion.

---

## 14. Whole-page performance budget

| Budget line | Limit | Notes |
|---|---|---|
| Total page weight (home) | ≤ 720KB | Fonts are the floor: three families, subset, ≤ 210KB total |
| Polaroid imagery | ≤ 90KB each, ≤ 5 on home | WebP, sized to frame, lazy below the fold (§6.9) |
| JS (theme system) | ≤ 38KB gz | One loop, one record parser, no framework for the theme layer |
| CSS | ≤ 30KB gz | Gradients and rules do the material work; no image textures except the stamp's SVG mask |
| Frame budget (shared loop) | ≤ 1.6ms/frame | Beam transform, ≤1 stroke, ≤2 path recomputes, counters — all measured in the gate's drill |
| Long tasks | none > 50ms | The catalogue record parses at build time into the DOM; runtime never parses 34,127 rows (index paginates a sample, §6.12) |
| Layout shift | CLS ≤ 0.02 | Sheets have reserved heights; images carry aspect ratios; the tag's slide is transform-only over printed space |
| Time to readable | first paint, JS or not | The page is content-complete in HTML; JS adds patrol, draws and counts — never content |

**Cut order when the budget is exceeded** (cut in this order,
never skip ahead): 1) polaroid count on home (5 → 3); 2) hero
point count (24 → 16); 3) carbon slips' layered variant → stacked
variant (§6.6's long-note form everywhere); 4) the tag's slide
entrance (print it); 5) field parallax (points static). **Never
cut:** the lights-up completeness, the watchdogs, the exact
totals, the refusal rows, the reduced-motion variants, the
receipt's arithmetic. A smaller round is legal; a dishonest or
stranding one is not.

---

## 15. Build-order checklist

1. **The record first.** Author the catalogue/round JSON (totals,
   zones, items, refusals with reasons, argued object, watch
   item, sightings count) and validate it: counts sum, IDs unique,
   every refusal earned. No design work precedes the data — the
   page is the record's printout.
2. **Static lit board.** Build the complete page with no JS:
   masthead, tag printed, totals exact, zones with checks printed
   drawn, stamp printed, form functional, handover reconciled.
   This is the fallback state and it must already be good.
3. **Typography and rules.** Load the three faces subset; set the
   type laws (§3); draw the ledger rules and torn edges.
4. **The field.** Points from the record (census-checked), cards
   in the rail, headline card.
5. **The shared loop.** rAF + lerp 0.12 + phase clock; register
   the beam, strokes, wobbles, counters as loop citizens; add the
   global watchdog (§6.16's 2400ms + per-element deadlines).
6. **The beam.** Patrol path, glints, card flips, park behaviour;
   then §6.7's lean as a loop offset.
7. **Checks and round state.** §6.2's scrubbed frontier, §6.8's
   visitor items, `roundState`, the rail (§6.11) and nav states
   (§6.10) reading from it.
8. **Refusals and the argued object.** §6.3's arcs, §6.5's twin
   arcs, velocity coupling, hover-still.
9. **Carbons.** §6.6 duplication pass over every note; the
   one-frame lag line in the loop.
10. **The tag.** §6.13 slide-in, minute updates, stand-down
    strike; staleness line logic.
11. **The form.** §6.14 validation in the custodian's voice,
    filing state, receipt arithmetic, carbon receipt, stamp.
12. **The stamp and the skeleton.** §6.15's arm-and-press with
    its watchdog path; §6.16's skeleton + dip for app builds.
13. **Handover reconciliation.** Print the third set of figures
    from the record; diff against §6.4/§6.11 mechanically.
14. **Reduced-motion pass.** Implement and walk the
    completed-round state (§5's ruling) element by element.
15. **The gate.** Run §10's twelve checks, including the watchdog
    drill and the beam-parked legibility screenshot (§9.12).
    Sign-off is by someone who did not build the page — the
    custodian's work is checked by the next shift.
