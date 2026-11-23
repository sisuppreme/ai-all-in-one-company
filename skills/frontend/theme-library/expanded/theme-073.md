# Theme 073 — The Instrument Maker's Bench (50x Expansion)

*A calibration bench at dawn: oscilloscopes, dial gauges and a maker's hands. The site treats every claim like a measurement — tolerances stated, instruments named, nothing asserted without a reading. The hero number is believed because the needle arrived at it honestly, overshoot and all.*

---

## 1. Concept & world

An instrument maker's bench is a place where numbers are not typed but *taken*. A gauge comes in off a customer's compressor, a ship's engine room, a hospital plant room; it is mounted on the test rig beside the bench's own reference standard; pressure is raised slowly by deadweight and hand pump; and the maker watches the needle the way a doctor watches a pulse — not for the number it shows first, but for how it arrives: whether it creeps or sticks, overshoots or drags, and where it finally, honestly settles. The Instrument Maker's Bench builds a website inside that discipline. The page is a lateral bench — a long graph-paper bench mat under a fixed centre loupe — and its sections are the instruments that live on it: a reference test gauge, a VU meter, a vernier caliper, an oscilloscope, a dial indicator, and one workshop gauge that is deliberately, visibly, 2% out of calibration with a red tag tied to its bezel. Scrolling slides the bench under the loupe. Every claim the site makes is presented the way the bench presents everything: as a reading, on a named instrument, with its accuracy class and its last-calibration date printed beside it.

The mood is dawn-quiet, exact, and faintly stubborn. This is not a steampunk skin and it is not an industrial-grunge template. Nothing here is rusted for fashion, nothing glows, no gear rotates decoratively. The beauty on offer is the beauty of a measurement that can be checked: the hero gauge's needle settles on 142.6 psi because the bench record (§6.17) says the rig stood at 142.6 psi, the tolerance readout beside it corrects itself from +0.02% to NOMINAL in step with the needle's own oscillations, and the calibration curve in the spec section plots the flagship's five test points from the same record — including the one point that sits off the curve, tagged, with the copy explaining exactly what was wrong and what was done about it. A metrologically literate visitor can audit this page, and the theme is designed to survive the audit.

**The theme's one law: nothing is asserted without a reading.** Every number that appears anywhere on the page — a pressure, a count, a date, a price, a percentage — must trace to the one bench record (§6.17): the declared object holding the rig pressure, each instrument's range, class, calibration dates and true reading, the book's totals, and the ticket sequence. Every claim prints its tolerance or its provenance beside it (a reading without a class and a date is an opinion, and this bench does not publish opinions). Every animated needle is driven to the record's value by the spring physics of §5 — a needle may overshoot, tremble, and take its time, but it may never land anywhere except on the truth, and if the physics cannot run, the value is printed as a figure beside the dial instead. And the bench's honesty is structural, not decorative: the one instrument that is wrong is shown wrong, tagged, in its place on the bench, because a bench that hides its faulty gauge would make every other reading on the page a lie by omission.

**Best-fit sites and audiences.** Instrument makers and gauge manufacturers whose product story is accuracy; calibration and metrology laboratories selling traceable certification; watch and clock repair ateliers (the bench discipline is identical — tolerances, loupes, tagged faults); precision machining and inspection services; restoration workshops for scientific instruments, aircraft gauges, and marine chronometers; test-equipment rental with calibration included; a technical brand whose entire pitch is "we measure it, here is the reading" — emissions testing, torque services, pressure safety-valve testing. The audience is exact and patient: engineers, technicians, quality managers, and serious hobbyists — people who read accuracy classes, who will notice that the tagged gauge's indicated 88.4 is exactly 2% above its true 86.7, and who distrust any number printed without a tolerance.

**When NOT to use it.** Not for anything that must feel fast, loud, or fashionable — the bench's quickest honest event is a 700ms needle flick, and its whole posture is a held breath. Not for brands whose numbers are marketing estimates ("up to 10x faster!") — the law requires every figure to be a reading with a provenance, and a growth-hacker homepage will suffocate. Not for dense consumer catalogues; the bench holds six instruments, not six hundred SKUs (the bench book, §6.13, caps at a bench-book page of rows). Not where the client will demand decorative dial clip-art, spinning gears, or a "precision™" badge with no class and no date — those are exactly the counterfeits the law forbids. Not for content with no measurements in it at all: if the site cannot honestly name its instruments and print its tolerances, the bench has nothing to calibrate and another theme should be chosen.

**The world, concretely.** The bench has: a bench mat (graph paper — the page ground), a test rig at its left end (the hero), the instruments in bench order (the traverse), a fixed loupe at centre-bench (the instrument of inspection), a vernier scale along the bench's front edge (progress), a bench book (the ledger of every instrument, its class, its dates), a red tag (the admitted fault), chalk annotations on the slate board at the bench's back (asides, notes, the day's figures), and a maker's plate screwed to the bench's front (the masthead). Every element specified in §6 is one of these things. Nothing enters from outside the world: no generic toast, no spinner, no badge pill; §11 gives each ordinary component its bench treatment or refuses it outright.

---

## 2. Palette

Five anchors, taken unchanged from the theme's original entry. The ground of the page is enamel cream — the painted enamel of instrument cases and dial faces, warm and faintly aged. Dial black is the text colour and the colour of dial faces themselves. Bench steel is the material of bezels, bench frame, and rules: structure, never body text (2.65:1 on cream, measured below). Needle orange is the colour of exactly one moving thing per instrument — its needle — and of nothing else except the light that crawls the knurling at dawn. Chalk on slate is the bench's second voice: the annotation board at the back of the bench, where the maker chalks the day's figures; it is a panel material, never the page ground.

| Token | Hex | Role | Usage ratio | Pairing / contrast ruling |
|---|---|---|---|---|
| `--cream` | `#F0EBDD` | Page ground (the bench mat's paper); dial faces; card enamel | ~52% of surface | Ground for `--dial` text: **14.04:1** — the page's default text pairing |
| `--dial` | `#1C1E20` | All body text; dial faces (dark instruments); needle hubs; engraved lettering | ~20% | On `--cream` 14.04:1 (AAA); on `--cream-lit` 15.08:1; on `--steel` 5.30:1 — dial-face inscriptions only, ≥12px |
| `--steel` | `#8A9299` | Bezels, bench frame, rules, graph-paper majors, loupe ring | ~16% | On `--cream`: **2.65:1** — graphics and large furniture only, never text; `--dial` on `--steel` 5.30:1 permitted for engraved plate lettering ≥12px |
| `--needle` | `#E86A17` | Needles (one per instrument), the live vernier index, the dawn light crawl | ≤4% | On `--dial`: **5.18:1** — needle against dark dial faces; on `--cream`: **2.71:1** — graphic only, never text; a needle on a cream dial is drawn with a `--dial` edge (see §3 law 4) |
| `--slate` | `#39424A` | The chalk board panels; the footer's bench-back; code/aside blocks | ~8% | With `--chalk`: **10.23:1** — the chalk pairing; on `--cream` 8.59:1 — slate panel edges and large furniture |
| `--chalk` | `#FFFFFF` | Chalk lettering on slate panels only | within slate | On `--slate` 10.23:1 (AAA) |
| `--cream-lit` | `#F7F3E8` | Raised enamel: card faces, the form leaf, the confirmation ticket | derived | With `--dial`: 15.08:1 |
| `--cream-deep` | `#E2DCC8` | Recessed enamel: bench-mat shading, ledger row alternation, skeleton dials' paper | derived | With `--dial`: 12.19:1 |
| `--steel-deep` | `#6E767D` | Graph-paper minor lines' darker pass, pressed steel, caption furniture | derived | On `--cream`: 3.87:1 — ≥18px labels and graphics only, never body text; on `--cream-deep` 3.36:1 — **forbidden pairing** for text |
| `--steel-lit` | `#A7AFB5` | Lit steel: dial-face furniture lettering on dark faces, loupe glints | derived | On `--dial`: 7.52:1 — small inscriptions on dark dial faces permitted |
| `--orange-deep` | `#C2530F` | Pressed needle-orange states, the crawl's shadow ridge | derived | On `--cream` 3.89:1 and on `--dial` 3.61:1 — graphics only, never text anywhere |
| `--tag` | `#B3352B` | The red tag, error text, the off-curve point — the bench's admitted-fault red | ≤1% | On `--cream`: **5.09:1** — error text permitted; `--chalk` on `--tag` 6.07:1 — the tag's own lettering; on `--dial` 2.76:1 — **forbidden**: the tag never sits on a dial face, it hangs on the bezel over cream |
| `--night-bench` | `#141619` | Dark-scheme ground (see below) | scheme only | With `--cream` text: 15.22:1; `--needle` on it 5.61:1 |

**Contrast method.** Ratios above are computed from the hex values by the WCAG relative-luminance formula for this expansion, not estimated. The load-bearing rulings are checked in the quality gate (§10): `--steel` text on `--cream` (2.65:1, fails — steel is a material, not an ink), `--needle` text on `--cream` (2.71:1, fails — orange is a needle, not a letter), `--steel-deep` on `--cream-deep` (3.36:1, fails), and `--tag` on `--dial` (2.76:1, fails). A builder who sets a caption in bench steel has broken the theme even if the page "looks industrial."

**Dark behaviour — "the bench after hours," not an inversion.** Under `prefers-color-scheme: dark`, the workshop lights go down; the bench does not. The page ground becomes `--night-bench`; body text becomes `--cream` on it (15.22:1). The instruments themselves stay exactly as they are — cream dial faces, dial-black lettering, orange needles — because a gauge is a lit object on the bench, read by the bench lamp, the way the slate board stays slate. Slate panels keep their hex and their chalk. Cards remain `--cream-lit` leaves resting on the dark ground rather than becoming dark cards: in this theme, content is always printed on enamel. There is no fully-dark content surface anywhere in the theme, in either scheme. The knurled light crawl (§6.10) runs slightly brighter after hours (its `--needle` at full value against the dark ground, 5.61:1) — dawn comes later to a dark workshop, and the crawl is the lamp left on.

**Colour discipline.** Needle orange is rationed to moving truth: one needle per instrument, the vernier's live index, and the dawn crawl — a page-wide census (§10) fails a build with orange buttons, orange links, or an orange logo. Tag red is rationed harder: it exists for the one tagged gauge, the one off-curve point that is that story's kin, and error text — three licensed roles, and a viewport showing a fourth red thing is a build error. Steel is a material, not a wash: it appears where metal would be — bezels, the bench frame, the loupe ring, rules — and a section background in flat steel is forbidden. Cream is the default state of every surface the visitor reads; slate is a board you walk to the back of the bench to read, used for asides and the footer, never as a hero ground.

---

## 3. Typography

Three families, exactly as the original entry specifies — Oswald for the engraved plate, IBM Plex Sans for the bench's prose, IBM Plex Mono for every readout. No fourth family is added; chalk annotations are Plex Sans at a slight rotate on slate, not a novelty handwriting font (a maker's chalk hand is a working hand, and legibility is the bench's religion).

- **Oswald** — display. Engraved-plate lettering: condensed, upright, cut like the lettering stamped into a maker's plate and the numerals around a dial. Used for headlines, instrument names, dial numerals, and the masthead plate. Oswald's condensed caps at large sizes read as *stamped metal*, which is the bench's display voice.
- **IBM Plex Sans** — body, labels, prose. A technical sans with an instrument-maker's neutrality; carries body text, card bodies, the bench book's prose columns, and form labels.
- **IBM Plex Mono** — readouts. Every measured value, tolerance, date, ticket number, and vernier reading: anything the bench *reports* is mono, tabular, and unhurried.

**The type scale** (root 16px):

| Role | Size / line-height | Family & settings | Used for |
|---|---|---|---|
| Display 1 | 58px / 1.04, +0.005em | Oswald 560, uppercase | Hero headline beside the hero gauge — the claim being measured |
| Display 2 | 40px / 1.1 | Oswald 520, uppercase | Section (instrument) titles |
| Display 3 | 27px / 1.16 | Oswald 500, uppercase | Card titles, the form's heading, footer plate title |
| Heading | 20px / 1.32 | Plex Sans 600 | Sub-heads inside sections, ledger group heads |
| Body | 17px / 1.62 | Plex Sans 400 | All reading text; measure capped at 64ch |
| Body small | 15px / 1.58 | Plex Sans 400 | Secondary text, card bodies |
| Caption | 13px / 1.5 | Plex Sans 400 | Instrument captions, figure notes, calibration labels |
| Readout | 15px / 1.5, tabular-nums | Plex Mono 500 | Measured values, tolerances, vernier readings, ticket numbers |
| Readout large | 24px / 1.3, tabular-nums | Plex Mono 500 | The hero tolerance readout (§6.5), the vernier's main reading (§6.7) |
| Plate inscription | 12px / 1.4, +0.12em, uppercase | Plex Mono 500 | Accuracy class + cal-date labels, dial furniture, the masthead's small lettering — the stamped register |
| Dial numerals | per-dial, +0.02em | Oswald 500 | Numerals printed around dial faces — set by the dial's own scale, never by the page's type scale |

**Type laws.**
1. **Readings are mono, claims are Oswald, explanations are Sans.** A visitor should be able to tell, from the letterforms alone, whether a line is a measurement, a claim, or prose. The three registers never swap jobs: no headline in mono, no reading in Oswald, no prose in either.
2. **Every reading carries its unit and its tolerance or its provenance.** `142.6 PSI` never prints as `142.6`; a deviation prints as `DEV +0.02% OF SPAN · TOL ±0.25%`; a date prints with its instrument (`CAL 2026-10-14 · No. 1`). A naked number on this bench is a defect, and §10 greps for them.
3. **Numerals are tabular everywhere.** Plex Mono is tabular by nature; Oswald dial numerals are set on fixed advance by the dial's geometry. A readout that changes width as it counts makes the bench look nervous — counters and readouts reserve their boxes (§6.18).
4. **A needle is drawn, never typed, and never outlined in type's clothing.** On cream dials the orange needle carries a 1px `--dial` edge so it reads at 5.18:1-equivalent against its face; on dark dials it is bare orange on black (5.18:1). No text is ever set in `--needle` to "match" a needle.
5. **Type never trembles, creeps, or sticks.** The needle's micro-tremor (§5) moves needles only. A headline that jitters is a broken instrument, and this bench repairs its instruments — it does not ship them trembling. (The one tagged fault trembles because it is *faulty*, §6.8, and it is a needle, not a letter.)

---

## 4. Layout language

**The bench is lateral, and the loupe does not move.** The defining layout fact, from the original entry: the page's main act is a horizontal bench — a graph-paper bench mat carrying the instruments in bench order — traversed under a loupe ring pinned at centre-bench. On desktop (≥1200px) the instruments section pins for a declared scroll length and the bench track translates laterally, scrubbed to scroll (§6.2), each instrument passing in turn beneath the fixed loupe (§6.3), where alone its vernier and fine print become legible. The hero stands at the bench's left end, where the test rig is: the hero gauge (§6.1) at rig size, its tolerance readout (§6.5) on the slate board behind it. Below the traverse, the page returns to vertical reading — the calibration curve (§6.6) drawn across the mat's graph paper, the bench book (§6.13) as a ledger, the form (§6.14) as a bench ticket pinned at the bench's right end — because a real bench is worked along its length and then written up in its book. The vernier scale (§6.7) runs along the bench's front edge for the page's whole length: a fixed bottom rail on desktop, the page's progress stated as a bench measurement.

**Grid and rhythm.** A 12-column grid at ≥1200px (max width 1440px, gutters 32px), 8 columns at 768–1199px, 4 below 768px. The bench mat is graph paper: minor grid 8px, major grid 40px, drawn in `--steel` at 18% (minors) and 32% (majors) over `--cream-deep` — the mat is a *material*, present under every section, not a hero-only texture. Vertical rhythm is the *bench rhythm*: sections are separated by a steel bench rule and 88px of mat on desktop, 64px tablet, 48px mobile — the elbow room a maker leaves between instruments. Whitespace here is bench space: it is where hands go, and it is never filled with decoration. The slate board is a place, not a style: slate panels appear only where the maker would chalk — behind the rig (the tolerance readout's board), as aside panels in prose sections, and across the footer's bench-back.

**Density rules.** Six instruments on the bench, no more — the record (§6.17) declares them, and a page may not invent a seventh instrument to fill a gap; a longer page adds *unsounded* bench length (prose, the book, the curve) rather than new instruments. One hero gauge. One tagged fault. Cards (§6.12) come in rows of three at most. The bench book (§6.13) caps at 12 rows per page of the book. Every gauge on the page — in the traverse, in cards, in the book's miniatures — carries its accuracy class and last-calibration date in the plate-inscription register; an unlabelled gauge is a build failure (§10), not a style choice.

**Section choreography (summary; full map in §13).** Arrival: the bench fades up at dawn, the hero needle performs its settle, the tolerance readout corrects itself to NOMINAL. Then the traverse: the visitor slides the bench and inspects each instrument under the loupe, their own scroll velocity reading on the VU meter as they go. Then the evidence: the calibration curve plots itself across the graph paper, the off-curve point stamps in tagged. Then the book: the ledger of all six instruments, the counters settling on the book's totals. Then the ticket: the booking form, whose confirmation is a bench ticket with a number taken from the book. The footer is the bench at rest — needles on their rest pins, the day's totals chalked, the maker's plate screwed to the front edge.

---

## 5. Full motion system

All motion on the bench is one of the physical behaviours of instruments and hands: a needle settling under spring physics, a heavy drawer sliding, a line being drawn by a plotter, a tag swinging on its string, a light crawling across knurling at dawn. There is no generic "fade-up" anywhere in the theme: things *settle, slide, plot, swing,* or *crawl* — the five things a bench actually does.

**Named easings.**
- `--ease-drawer` — `cubic-bezier(0.7, 0, 0.2, 1)`: the heavy bench drawer — a slow breakaway against friction, a long even glide, a firm arrival. Used for the bench traverse's snap-to-instrument, bench fades, and section furniture.
- `--ease-engrave` — `cubic-bezier(0.55, 0, 0.1, 1)`: a line being cut or plotted — even pressure, decisive end. Used for the calibration curve's plot, chalk underlines, link underlines.
- `--ease-swing` — `cubic-bezier(0.45, 0, 0.55, 1)`: the tag's pendulum ease for its *initiating* nudge only; the swing itself is physics (§6.8).
- `--ease-crawl` — `linear`: the dawn light travels at constant speed; light does not ease.
- The needle spring is **not an easing**: it is an integrated damped spring (§6.1), specified by stiffness and damping, because a needle's overshoot must be *physics the visitor can feel*, not a curve an animator faked.

**The needle spring (the bench's core physics).** Every needle on the page is a rigid pointer on a jewelled pivot, simulated by semi-implicit Euler integration at 240Hz substeps inside the shared loop: acceleration = −k·(θ − θ_target) − c·θ̇, with the hero spring at **k = 182.25 (ωn = 13.5 rad/s), c = 4.32 (ζ = 0.16)** — underdamped, so a displaced needle overshoots, oscillates about three visible times with decaying amplitude, and settles. Smaller instruments use the same ζ with ωn scaled by dial size (a small needle is a quicker needle: ωn 18–22 rad/s). Each needle additionally carries a *stiction band* of ±0.15% of span: inside the band, static friction holds the needle unless the drive exceeds it — the bench's needles can *creep and stick* by a hair, like real ones, and the flick (§6.9) exists to free them. Micro-tremor at rest is a seeded noise torque of ±0.06% of span — present on every healthy needle, and doubled on the tagged gauge (§6.8), where it is a symptom.

**The one loop.** Every scroll-scrubbed or continuous value — bench traverse position, vernier reading, VU target, tag swing phase, crawl phase — is driven by a single `requestAnimationFrame` loop that lerps each registered value toward its target at **0.14** per frame (the drawer's weight) and integrates the needle springs at fixed substeps. No scroll handler writes a style. The loop sleeps when the tab is hidden, and when every registered value is within tolerance and no ambient behaviour is armed; ambient behaviours (tremor, crawl, tag swing) keep it awake only while their instrument is within one viewport of the reader.

**Motion terms, in the bench's language.**
- *Scroll-triggered reveals:* instruments do not reveal — they are **inspected**. Content is printed on the mat from the start; what scroll arms is the *instrument behaviour* (a needle taking its reading, a curve plotting), never text opacity from zero.
- *Scroll-driven / scrub animation:* the bench traverse (§6.2) and the vernier (§6.7) are scrubbed to scroll; the calibration curve's plot (§6.6) is scrubbed to its section's passage.
- *Parallax:* three bench depths only — chalk annotations on the slate board at 0.94×, instruments at 1.0×, the loupe ring and its glint at 1.04×. The mat never parallaxes; a bench mat is the reference plane everything else is measured against.
- *Pinned sections:* the traverse pins (§6.2) with the loupe fixed at centre-bench; the vernier rail pins along the front edge for the whole page (§6.7).
- *Smooth scrolling:* native, with the loop's 0.14 lerp supplying the felt weight of the drawer; `scroll-behavior: smooth` for bench-rail jumps (§6.11).
- *Progress indicator:* the vernier scale (§6.7) — progress stated as a bench position in millimetres, to a stated resolution.
- *Staggered + masked reveals:* the hero's instruments stagger in bench order, left to right (140ms apart, §6.1); captions *engrave* — a clip mask widens left-to-right at `--ease-engrave` as if cut into the plate, 600ms, once.
- *Kinetic typography:* refused, with one exception — the readouts count (§6.5, §6.18), because a readout changing is an instrument working. Headlines do not move; engraved lettering is still by definition.
- *Marquee:* **refused.** Nothing on a bench travels sideways forever. The bench book is a table; the traverse is scrubbed, not looped.
- *Counters:* readings settle under spring physics (§6.18) — they arrive the way needles arrive, overshoot and all, and land on the record's exact figures.
- *SVG line-draw:* the calibration curve (§6.6) plots; chalk underlines draw (§6.16); the oscilloscope's trace (§6.12's card / §6.17's record) is a live-drawn sine with the bench hum's true harmonic content.
- *Image scale-in-frame:* photographs (the maker's hands, the workshop) scale 1.05 → 1.0 inside enamel instrument bezels (§6.12) — an image seating itself in its bezel, not a zoom.
- *Hover / micro-interactions:* hovering is the loupe (§6.3) — magnification is positional; bezels tilt toward the light by at most 3° (§6.12); clicking a gauge flicks its needle (§6.9).
- *Custom cursor:* **refused** — normal system cursor only, per standing rule; the visitor's inspection instrument is the loupe, which is positional, not pointer-shaped.
- *Skeleton loading:* unmarked dial faces (§6.15) — dials print with their faces blank and gain their scales in shimmer, the way a restored dial looks before its numerals are re-enamelled.
- *Page transitions:* the bench slides laterally (§6.15), rolling the next instrument set into the loupe — the site's pages are positions along one bench.
- *Reduced motion:* §6 passim — the bench at rest: every needle printed on its true reading, every value a figure beside its dial, the traverse a vertical stack, the curve pre-plotted. Nothing is lost; the bench is quieter, not emptier.

**Ambient loops — exactly three licensed.** The needles' micro-tremor, the red tag's swing (§6.8), and the knurled light crawl (§6.10). All pause off-screen, all die under reduced motion, and no fourth loop may be added: a bench with four things moving is a machine shop, and this is a maker's bench at dawn.

---

## 6. Signature elements

The ten original signature elements (§6.1–§6.10) are deepened, never redesigned. §6.11–§6.18 are the page-family elements the original layout implies — the maker's plate navigation, the instrument cards, the bench book, the bench-ticket form, the unmarked-dial transition, the resting footer, the bench record itself, and the settling counters. All eighteen read every value from the one bench record (§6.17); where a number appears in an element's spec — a pressure, a class, a date, a count — it is the number that element ships with, and §10 audits the agreement.


### 6.1 The damped-spring hero gauge

**What & why.** A large analogue test gauge — the bench's reference standard, No. 1 — dominates the hero, mounted on the test rig at the bench's left end. On load its needle sweeps from its rest pin, overshoots the headline's key number by ~8% of span, oscillates three visible times under true damped-spring physics, and settles exactly on **142.6 psi** — the rig pressure in the bench record (§6.17), and the number inside the headline's claim. This is the theme's thesis in one gesture: the headline is not asserted, it is *measured*, in front of the visitor, by an instrument whose arrival behaviour (the overshoot, the decaying oscillation, the honest settle) is the proof. It merges with content because the gauge and the headline are one statement: remove the gauge and the claim is marketing; remove the headline and the gauge is a screensaver.

**Structure.** An SVG dial (420px at desktop) drawn from the record's scale data: 270° arc, 0–200 psi, major ticks every 20 psi with Oswald numerals, minor ticks every 2 psi, the class inscription `CLASS 0.25 · EN 837-1` and the maker's name engraved on the face, a `--dial` hub, and the `--needle` pointer (with its 1px `--dial` edge, Type law 4) as the only animated part. The spring state (θ, θ̇) lives in the shared loop (§5); the needle is a `<g>` rotated by θ. Beside the gauge, the headline (Display 1) with the key number set in the readout register inline, and beneath, the gauge's label plate: `No. 1 · REFERENCE TEST GAUGE · 0–200 PSI · CLASS 0.25 · CAL 2026-10-14 · DUE 2027-10-14` — every gauge on the page carries this plate; the hero's is simply the first. The printed fallback (see Fallback) is a static rendering of the same dial with the needle at 142.6 and the reading printed beside it.

**Motion spec.** Two stages. *Stage 1 — the approach (0–480ms):* the needle leaves the rest pin and covers rest → 92% of deflection under `--ease-drawer` (the hand-pump raising pressure: a heavy, even climb). *Stage 2 — the spring (480–1900ms):* control hands to the integrated spring (k = 182.25, ζ = 0.16) with the approach's terminal velocity as its initial condition; the needle overshoots to target +8.0% of span at ≈710ms, swings back to −2.7% at ≈940ms, +0.9% at ≈1170ms — three visible oscillations — and settles within ±0.1% of span by 1900ms, where the stiction band takes it and it stops *dead*, the way a real needle stops. The tolerance readout (§6.5) corrects in step with the spring's zero-crossings. The headline's caption engraves at 1500–2100ms (§5). Trigger: first paint + 200ms, once per session; a `sessionStorage` flag replays only the short form on repeat visits (approach compressed to 300ms, spring unchanged — physics is not shortened, only the pump stroke).

**Choreography timeline** (from first paint; the spring's own clock starts at the 200ms trigger). 0ms bench faded up (§6.15's arrival state) · 200ms needle leaves the rest pin · 680ms approach ends, spring takes the needle · 910ms first overshoot peak (+8.0%) — the readout (§6.5) prints `DEV +0.02%` · 1140ms first undershoot (−2.7%) · 1370ms second overshoot (+0.9%) — readout prints `DEV +0.01%` · 1500ms caption begins engraving · 2100ms needle inside the stiction band at 142.6, readout prints `NOMINAL` · tremor (±0.06%) arms.

**State matrix.** *Rest (pre-trigger):* needle on its rest pin, headline printed, reading printed beside the dial as a figure — the page is complete in this state. *Sweeping:* as above; the dial is not focusable and pointer events pass to the text around it; the needle's motion never blocks reading. *Settled:* tremor armed; hover hands over to §6.3's loupe behaviour and §6.9's flick is armed. *Scrolled-past:* the spring never replays; the needle holds 142.6 with tremor. *Disabled (no JS / no rAF):* the static dial, needle at 142.6, reading printed. *Touch:* identical — the settle is time-triggered, never gesture-triggered, on every device.

**Content-merge.** The gauge measures the headline's number on the bench's rig from the record's rig pressure; its label plate is the provenance the law (§1) demands, printed in the same register as every other instrument's. The hero is the bench's method performed once, at full size, before the visitor is asked to believe anything else on the page.

**Breakpoints.** ≥1200px: dial 420px, headline to its right, readout board behind. 768–1199px: dial 320px, headline below the gauge (the claim follows its measurement down the bench). <768px: dial 78vw (max 340px), headline below, spring identical (physics does not shrink with the dial; ωn rises to 15 rad/s so the settle still lands ≈1900ms at the smaller radius — the *time* is the spec, not the angle).

**Edge cases & failure modes.** Slow device: if the first 30 frames average >24ms, substeps drop 240Hz → 120Hz and ζ is recomputed to hold the same settle envelope (the oscillation count is the spec; the integration rate is an implementation detail). Tab hidden mid-settle: the loop sleeps; on return, if elapsed >2600ms the needle snaps to 142.6 (watchdog state) rather than resuming a stale swing. Headline longer than the copy cap (§12: three lines): a fourth line flows *below* the gauge, never across the dial. Rig pressure changed in the record: the dial's target, the readout's figures, and §8.1's example all re-derive — a builder who hard-codes "142.6" anywhere has failed §10's one-record audit.

**Fallback & watchdog.** The static dial (needle at 142.6, reading printed) is in the DOM beneath the animated SVG from first paint; the animated needle only covers it once the spring runs. **Watchdog: 2600ms** — if |θ − 142.6| > 0.1% of span at 2600ms, the needle snaps to the reading, the readout prints `NOMINAL`, and the tremor arms. If SVG fails entirely, the label plate and the printed reading remain: the claim survives the instrument.

**Reduced motion.** No sweep, no spring: the needle is printed at 142.6, the readout prints its final state, and the hero is a photograph of a measurement already taken. The claim loses its performance and none of its truth.

**Accessibility.** The animated dial is `aria-hidden="true"`; its meaning is carried by real text — the headline's inline readout and the label plate. The gauge's figure is never the only carrier of the number 142.6 (it appears in the headline, the plate, and §6.17's record printings). Focus order is untouched by the rig. Contrast: dial lettering on the cream face 14.04:1; the needle's orange reads by its `--dial` edge, not by hue alone.

**Performance & mobile variant.** One SVG, one rotating `<g>`: the spring costs ≤0.15ms/frame at 240Hz substeps (four substeps of arithmetic per frame at 60fps). Mobile: identical physics, dial at 78vw, caption engraving cut first under §14's cut order. No canvas, no WebGL, anywhere in this element.

**Tokens.** `--cream`, `--dial`, `--steel`, `--needle`, `--spring-k: 182.25`, `--spring-zeta: 0.16`, `--settle-dur: 1900ms`, `--watchdog-hero: 2600ms`, `--ease-drawer`, `--tremor-amp: 0.06%`.

### 6.2 Horizontal bench traverse

**What & why.** The instruments section pins, and the bench itself slides laterally under the fixed loupe (§6.3), scrubbed to scroll: the six instruments of the record (§6.17) — reference gauge No. 1 again at bench scale, VU meter No. 7, vernier caliper No. 12, oscilloscope No. 19, dial indicator No. 23, and the tagged gauge No. 31, last, where the maker keeps it — pass beneath the glass in bench order. This is the theme's navigation made physical: the visitor does not scroll *past* the product range, they slide the bench and inspect each instrument where it sits, at the speed of their own hand, with the drawer's resistance in the scroll. It merges with content because the bench *is* the catalogue: each instrument under the loupe is that instrument's full section — its reading, its class, its dates, its story — not a thumbnail of content held elsewhere.

**Structure.** A pinned section of declared height (600vh at desktop: 100vh per instrument) containing a sticky viewport; inside it, a horizontal track (the bench) carrying six instrument stations on the graph-paper mat, each station 100vw-equivalent of bench length (the record's bench is 2400mm long; §6.7's vernier reads the same traverse). Scroll progress through the pin maps to a target bench offset; the shared loop lerps the actual offset toward it at 0.14 — the drawer's weight — and the track transforms by the lerped value. Each station's DOM is a complete section (heading, instrument, prose, label plate); the pin is an enhancement over a document that reads vertically without it (see Fallback). Station boundaries carry a soft detent: within the central 30% of a station's travel, the lerp target biases 12% toward the station's centred position — the drawer *settles* each instrument under the loupe the way a detent seats, without ever trapping the scroll.

**Motion spec.** Scrubbed, not timed: bench offset is a pure function of (lerped) scroll progress. Instruments respond as they travel: needles take their stations' readings as their station crosses the loupe (§6.3), the VU meter reads the traverse's own velocity (§6.4), the tag swings from the bench's acceleration (§6.8). At the pin's end, the bench releases with the last instrument centred and the section un-pins into the curve section below — the drawer reaches the end of its runners and stops; there is no bounce, no overshoot past No. 31 (a bench ends). Reverse scroll runs the traverse backwards exactly; the detent is symmetric.

**Choreography timeline** (per station, relative to its travel). 0% (station entering right): instrument at rest, needles on rest pins or idle states. 30%: station approaching the loupe; its needle begins its take (spring armed). 50% (station centred under the loupe): magnification full (§6.3), needle settled on the station's reading, label plate fully legible, detent seated. 70%: station leaving; needle holds its reading (a reading, once taken, stays taken). 100%: next station at 30%. The vernier (§6.7) reads continuously throughout: bench position = progress × 2400mm.

**State matrix.** *Rest (before the pin):* first station centred, loupe over No. 1. *Traversing:* as above; prose in the centred station is selectable and readable throughout — the bench moves, the words never blur or fade. *Station centred:* detent seated; the station's interactive elements (flick §6.9, loupe hover §6.3) armed. *Scrolled-past (below the pin):* bench holds its final position if re-entered from below; no replay state. *Disabled (no JS):* the pin never forms; stations stack vertically in bench order on the mat (the fallback layout, which is also the tablet/mobile layout). *Touch:* the traverse is scroll-scrubbed identically; there is no separate swipe gesture — one input, the page scroll, so the bench can never fight the reader's thumb.

**Content-merge.** The traverse is the catalogue's order made spatial: bench order is the record's order (reference first, the tagged fault last and admitted), and each station's prose is that instrument's own — its use, its class, its story. The loupe's magnification (§6.3) reveals each station's fine print *in place*: nothing is a teaser for content elsewhere.

**Breakpoints.** ≥1200px: pinned traverse as specified, stations 100vw of bench each, detent on. 768–1199px: **no pin** — the bench becomes a horizontal scroll-snap rail inside the section (native `overflow-x`, snap to stations), because a pinned scrub on a tablet's shorter scroll fights the reader; the loupe becomes a fixed-centre frame over the rail with the same magnification rule. <768px: stations stack vertically on the mat in bench order; the loupe is retired (its job — fine print legibility — is done by the stack's full-size plates); the vernier (§6.7) still reads page progress.

**Edge cases & failure modes.** Content longer than a station expects: a station's prose column is capped (§12); overflow flows *below* the instrument within the station, lengthening the bench visually but not the pin's declared 600vh (the pin maps stations, not pixels — extra prose is read after un-pin in the station's continuation block, printed in the fallback stack). Scrolling back up through the pin: exact reverse; needles hold readings (they do not un-take them). Jump scroll into the middle of the pin (restoration, anchor): the bench lands on the nearest station, centred, needles settled — no traverse is owed to a reader who teleported. Low-power device: detent and loupe magnification are the first cuts (§14); the scrub itself never degrades into steps.

**Fallback & watchdog.** Without JS, or if the pin's measurements fail, the section is the vertical stack (the same DOM, unpinned) — **the fallback is a layout, not an error state**, and it is the layout two of three breakpoints ship anyway. **Watchdog: 900ms** after entering the pin — if the track's transform has not tracked scroll (loop stalled), the pin releases and the stack takes over for the session. No station's content is ever reachable *only* through the traverse.

**Reduced motion.** No pin, no traverse: the vertical stack at every breakpoint, instruments at rest on their readings. The bench is walked, not slid.

**Accessibility.** The stacked fallback is the DOM order, so screen-reader and keyboard order is bench order regardless of the visual traverse. In the pinned build, focus within a station scrolls the *page* (the pin follows focus: when a station's element receives focus, the traverse target sets that station centred — a keyboard user inspects by tabbing, and the bench comes to them). The pin adds no focusable elements of its own. Station headings are real `<h2>`s; the traverse is `aria-hidden` as a *mechanism* only — its content is the document.

**Performance & mobile variant.** One transformed track (compositor-only `transform`), six stations' needles integrated only while their station is within one viewport of travel. Traverse cost ≤0.4ms/frame desktop. Mobile ships the stack: zero traverse cost.

**Tokens.** `--bench-length: 2400mm`, `--pin-length: 600vh`, `--lerp-bench: 0.14`, `--detent-bias: 12%`, `--ease-drawer`, `--mat-minor: 8px`, `--mat-major: 40px`.

### 6.3 The fixed loupe

**What & why.** A loupe ring — a steel-rimmed magnifying glass on a short stand — pins at centre-bench for the whole traverse, and whatever passes beneath it is magnified ~1.35×, its vernier enlarged and its fine print legible only there. On a real bench, detail exists where the glass is; the loupe makes inspection *positional* on the page: the visitor learns, bodily, that to read an instrument's fine print they must bring it to the glass. It merges with content because the magnification is not a zoom effect on decoration — it reveals the actual second layer of each instrument's content: the vernier's subdivisions, the dial's minor ticks, the label plate's small lettering, the curve's point tags — content that is printed at bench scale and *resolved* at loupe scale, exactly as enamel fine print is printed small and read under glass.

**Structure.** A fixed ring (280px diameter at desktop) centred in the traverse viewport: a `--steel` rim (10px), an inner shadow ring, and a lens disc. The magnification is implemented as a *second rendering* of the bench track inside the lens: a clipped copy of the track, scaled 1.35×, whose transform is the bench transform recomputed for the lens geometry (lens centre fixed; the copy's offset = −(bench offset + station position − lens centre) × 1.35 + lens centre). Both copies are the same DOM cloned once at build (the clone is `aria-hidden`, presentational); text inside the lens is real rendered text at 1.35×, not a bitmap zoom — it stays crisp, because a loupe shows the thing itself, larger. The lens carries a faint `--steel-lit` glint arc that crawls with §6.10's light. Outside the traverse (hero, curve, book), the loupe appears once more, parked at the bench's right end over the form (§6.14) — no: the loupe belongs to the traverse; elsewhere the bench trusts the naked eye. (This sentence's correction is deliberate in the spec: builders kept parking loupes everywhere; the rule is one loupe, one job.)

**Motion spec.** The lens copy's transform updates in the same shared loop as the bench (same lerp 0.14) — the magnification must never lag or lead the bench by a frame, or the glass feels like a video effect instead of optics. Magnification is constant 1.35× (a loupe does not zoom); the *detent* (§6.2) does the apparent breathing as stations seat. The glint arc crawls at §6.10's rate. When a station is centred, its vernier (§6.17's caliper station) is specified to fall inside the lens — the layout guarantees it: the vernier sits at each station's centre-bench height, so centring the station centres the fine print under the glass.

**Choreography timeline.** Continuous with §6.2's traverse: as a station travels 30% → 50%, its fine print crosses the lens edge (slight refraction offset at the rim, 2px, applied to the lens copy only at the rim band) and resolves at centre; 50% → 70% it crosses out. No timeline of its own — the loupe is optics, and optics are instantaneous; any easing inside the lens is a build failure.

**State matrix.** *Rest:* lens over the first station, fine print resolved. *Traversing:* as above; the lens copy and the bench never disagree by more than one frame (the loop writes both transforms in the same pass). *Station centred:* full magnification; the station's label plate small lettering (12px plate inscription → 16.2px effective) legible. *Scrolled-past:* the loupe leaves with the pin; nothing of it persists into later sections. *Disabled (no JS):* no lens copy; all fine print is *also* printed at full size in each station's plate (see Fallback) — the loupe is a pleasure, never a gate. *Touch:* in the tablet rail build, the lens sits over the rail's centre and magnifies the snapped station; in the mobile stack, retired (§6.2).

**Content-merge.** The lens reveals the instruments' own second layer — vernier subdivisions, minor ticks, point tags, plate small print — all of which is content authored per station (§6.17's record carries each instrument's fine-print lines). A station with nothing to magnify is a station whose content is too thin, and §10 checks that every station ships at least two loupe-resolved details.

**Breakpoints.** ≥1200px: 280px lens over the pinned traverse, as specified. 768–1199px: 220px lens fixed over the scroll-snap rail's centre; magnification 1.25× (the rail's stations are smaller). <768px: retired; fine print prints at full size in the stack (the fallback becomes the design).

**Edge cases & failure modes.** Clone drift: if the lens copy's content can diverge from the bench's (dynamic values — the VU reading, the vernier), the clone is re-synced by the loop from the same state object, never from the DOM — one source of truth, two renderings. Performance degradation: the lens copy is the §14 cut-order's second item (the bench loses its glass before it loses its needles). Very long fine print: the lens shows what is under it; lines longer than the lens diameter are set in the plate at a size that resolves in two passes of the glass — stated here so two builders set the same measure. Browser without `clip-path: circle()`: the lens falls back to a rounded-rectangle ring (a watchmaker's rectangular loupe — in-world, and specified so the fallback is designed, not accidental).

**Fallback & watchdog.** Every loupe-resolved detail is duplicated at full size in the station's label plate in the DOM (visually the plate's "under glass" lines print small on the bench and full-size in the plate's expanded block, which is present without JS). **Watchdog: one frame** — the loop asserts lens and bench transforms are written in the same pass; if the lens copy fails to initialise, it is removed and the plates carry the content alone. With JS disabled, there is simply no loupe, and nothing is missing.

**Reduced motion.** The loupe still magnifies (it is optics, not motion) in the tablet rail build; in the desktop build reduced motion retires the traverse (§6.2), so the loupe retires with it and the plates carry everything.

**Accessibility.** The lens clone is `aria-hidden="true"` and never focusable; all magnified content exists once in the accessible DOM at full size in the plates. Magnification is a visual aid layered over content that already meets contrast and size floors without it — the bench never uses the loupe to excuse 8px text (plate inscription floor is 12px, §3). Keyboard users get the centred-station behaviour of §6.2; the lens follows the same state.

**Performance & mobile variant.** The lens copy doubles the traverse's paint cost inside a 280px circle: clip-path confines repaint to the disc; cost ≤0.5ms/frame desktop, and it is cut before the traverse itself under §14. Mobile: retired, zero cost.

**Tokens.** `--loupe-size: 280px`, `--loupe-mag: 1.35`, `--loupe-rim: 10px`, `--steel`, `--steel-lit`, `--lerp-bench: 0.14`.

### 6.4 Velocity VU meter

**What & why.** On the bench, third in the traverse's heart and again small in the vernier rail, a VU meter — No. 7 — whose needle is driven by the visitor's own scroll velocity: deflection mapped from px/s, with its own spring lag, idling at rest with the faint bench-hum tremor. It is the bench measuring the reader: your hand, sliding the bench, is a signal, and the bench's meter reads it and shows it to you. It merges with content because it closes the bench's loop — every other instrument measures the site's claims; this one measures the visit itself, and its presence teaches the visitor how every other needle on the page will behave (spring lag, overshoot, tremor) before they are asked to trust the hero's settle.

**Structure.** A cream-faced VU dial (the classic −20…+3 VU scale, yellowed-cream face being the one place the theme lets the enamel read warmer — specified as `--cream` with the scale's traditional red sector above 0 VU drawn in `--tag` at 40% — the meter's own factory printing, not a theme accent; this is the tag red's *fourth* licensed appearance and it is licensed because it is the instrument's real face, audited as such in §10). Needle driven by the shared spring at ωn = 18 rad/s, ζ = 0.21 (a VU meter's ballistics are a real standard — the needle must reach 99% of a 0 VU step in 300ms with 1–1.5% overshoot; the spec adopts the standard's numbers, and the spring is tuned to them). Input: scroll velocity sampled by the loop (px/s, low-passed at 120ms), mapped: 0 px/s → rest; 2600 px/s → 0 VU; clamped at +3 VU. The idle state is not zero: the bench hum (the oscilloscope's §6.17 trace is the same hum, seen) drives a ±0.4 VU tremor around −19.6 VU.

**Motion spec.** Continuous, not triggered. Velocity steps (a flick of the scroll) swing the needle with true VU ballistics: 300ms to 99%, overshoot ≤1.5%, settle by 600ms. Sustained scrolling holds a deflection proportional to velocity — the needle *leans* into a long traverse and falls back as the reader slows at a station, which makes the detent (§6.2) something the visitor can watch themselves do. At rest for >2s, the needle decays to the hum idle. During the hero (§6.1), before any scroll, the meter idles — its tremor is the first motion on the page and it starts at first paint.

**Choreography timeline.** 0ms (first paint): needle at −20 rest pin. +400ms: hum tremor arms (needle lifts to −19.6 and breathes ±0.4 VU at the hum's seeded rhythm). First scroll: deflection within one frame of velocity; the spring's lag means the needle *announces* speed changes ~120ms late, like a real meter. Scroll stop: overshoot ≤1.5%, settle to idle by +2600ms. No other beats — the meter is an instrument, not a performance.

**State matrix.** *Rest:* hum idle at −19.6 ± 0.4 VU. *Reading:* deflection ∝ velocity, spring-lagged. *Scrolled-past / section out of view:* the loop stops integrating it (frozen at its last reading, printed); the rail miniature (see Content-merge) continues. *Disabled:* the meter prints at its idle reading with the figure `SCROLL VELOCITY — READ LIVE` replaced by the honest static caption in the plate. *Touch:* scroll velocity is scroll velocity — touch scrolling drives it identically; fling gestures peg it briefly to +3, which is correct behaviour for a meter and a small delight the spec protects (do not clamp the fling spike away; a meter that never pegs is a liar).

**Content-merge.** The meter's station in the traverse (§6.2) is its own full section — the copy there is about measurement of motion (the workshop's vibration work), and the meter the visitor has been watching since the hero is the instrument that section describes. A miniature of the same meter lives in the vernier rail (§6.7) so the reading persists after the traverse; both renderings read the one velocity state.

**Breakpoints.** ≥1200px: full dial 300px at its station; rail miniature 120px. 768–1199px: dial 240px at its station in the rail layout; miniature retired (the station is reachable by the rail's own scroll). <768px: dial 64vw in the stack; no miniature; ballistics identical.

**Edge cases & failure modes.** Velocity noise (trackpad jitter) is low-passed at 120ms so the needle reads the hand, not the sensor. Scroll containers: velocity is measured on the page scroll only; nested scrollers (the bench book's table on mobile) do not drive it — stated so two builders meter the same hand. Reader uses keyboard: velocity derives from scroll position deltas, so keyboard scrolling reads too — a Page Down is a honest deflection. If scroll events stall (loop degraded), the needle decays to idle rather than freezing mid-deflection — a meter falls back to rest, never to a stale claim.

**Fallback & watchdog.** The meter's plate prints its scale, class, and dates; without JS the dial prints at idle with the caption `AT REST — THE METER READS YOUR SCROLL WHEN THE BENCH IS LIVE`. **Watchdog: 2000ms** of loop silence decays the needle to the hum idle. No content depends on the meter's reading — it is the bench's mirror, not its evidence.

**Reduced motion.** The needle prints at idle and does not read velocity; the caption changes to the at-rest form. The visitor loses the mirror, keeps every fact.

**Accessibility.** Pure ambience with a text equivalent: the meter is `aria-hidden`, and its station's prose carries the section's content. Nothing is communicated by the needle that is not in the plate. The red sector is the instrument's factory face — it is never used as an error signal anywhere in the UI (§11 errors are text in `--tag` on cream, a different, licensed role).

**Performance & mobile variant.** One spring, one needle: ≤0.05ms/frame. The rail miniature shares the state, costing a transform. Mobile: the single stack dial, same cost.

**Tokens.** `--vu-rest: -19.6`, `--vu-tremor: 0.4`, `--vu-full-scale-pxs: 2600`, `--spring-vu-k: 324` (ωn = 18), `--spring-vu-zeta: 0.21`, `--cream`, `--dial`, `--needle`.


### 6.5 Self-correcting tolerance readout

**What & why.** Beside the hero gauge, chalked-and-mono on the slate board behind the rig, a readout that counts and corrects itself in step with the needle's settling: `DEV +0.02% OF SPAN` at the first overshoot, `DEV +0.01%` at the second, then `DEV 0.00% · NOMINAL · TOL ±0.25%` as the needle enters its stiction band at 142.6 psi. Every other site on earth prints the claim and hides the error; this bench prints the claim *and* its error, and performs the correction — the deviation shrinking under the visitor's eye until the instrument can honestly say NOMINAL. It merges with content because it is the hero's second half: the gauge shows the value, the readout shows the value's *trustworthiness*, and the headline is only fully stated when both have settled.

**Structure.** A slate panel (`--slate`, chalk register) mounted behind the rig, carrying three mono lines (Readout large, §3): the deviation line, the tolerance line (`TOL ±0.25% OF SPAN · CLASS 0.25`), and the rig line (`RIG 142.6 PSI · DEADWEIGHT No. 4`). The deviation value is a text node updated by the same spring state that drives §6.1's needle — deviation = (θ_indicated − θ_true) expressed as % of span, rounded to the bench's reporting resolution of 0.01% — so readout and needle can never disagree: they are two printings of one state. During the approach it prints `DEV ———` (the bench does not report a deviation it has not measured yet; dashes, not a fake zero).

**Motion spec.** The deviation line updates at the spring's zero-crossings and threshold crossings, not per frame — a readout that flickers digits is a nervous instrument; this one *steps*: `———` (approach) → `+0.02%` at the first overshoot peak (≈910ms from first paint, the deviation's maximum honest reading, sampled and held) → `+0.01%` at the second overshoot (≈1370ms) → `0.00% · NOMINAL` at settle (2100ms), where the word NOMINAL engraves (clip widening, 300ms, `--ease-engrave`) — the only typographic event in the element, reserved for the moment the bench signs its own work. Held values are sampled at the peaks because that is what a calibration engineer records: the worst deviation seen, then the next, then the settled truth.

**Choreography timeline.** 0ms: `DEV ———`, rig and tolerance lines printed. 200–680ms: approach — no deviation reported. ≈910ms: `+0.02%` steps in (no animation; a digit change is an event, not a transition). ≈1370ms: `+0.01%`. 2100ms: `0.00%`, NOMINAL engraves over the next 300ms. Thereafter the line holds; if the visitor flicks the hero needle (§6.9), the readout re-opens (`DEV` live during the flick's swing, re-settling to NOMINAL) — the readout belongs to the gauge, not to the page load.

**State matrix.** *Rest (pre-trigger):* the final state printed — `DEV 0.00% · NOMINAL · TOL ±0.25%` — because without the performance, the bench still signs the reading. *Correcting:* the stepped sequence above. *Settled:* NOMINAL held; tremor does not move the digits (the deviation of a settled needle inside its stiction band is 0.00 by the bench's reporting rule, stated here so no builder prints a flickering ±0.00/0.01). *Re-opened (flick):* live deviation during the swing, peaks re-sampled, NOMINAL re-earned. *Disabled:* final state printed, as Rest. *Touch:* identical; the readout has no pointer behaviour of its own.

**Content-merge.** The readout is the headline's tolerance, which §1's law requires to be printed beside the claim — not in a footnote, not in a spec PDF, but on the board behind the rig, in the same viewport, at readout size. Its three lines (deviation, tolerance, rig) are the provenance chain of the hero number: what the error was, what it was allowed to be, and what produced the pressure.

**Breakpoints.** ≥1200px: slate board behind the rig, Readout large 24px. 768–1199px: board below the gauge, 20px. <768px: board below the gauge at 17px, the rig line wraps under the tolerance line; the stepped sequence is unchanged (a small bench reports just as carefully).

**Edge cases & failure modes.** If the spring degrades (slow device), the readout follows the *actual* spring state — its steps arrive late with the needle, never on a fixed clock: the readout is slaved to the physics, so a slow bench shows a slow correction, honestly. Record changed: all three lines re-derive from §6.17 (rig pressure, class tolerance, deadweight identity). Rounding: deviations report at 0.01% resolution, rounded half-to-even — a metrology bench states its rounding rule, and §10 checks the printed peaks against the spring's telemetry in the gate's drill.

**Fallback & watchdog.** Printed final state is the DOM default; JS *replaces* it with the live sequence (dashes first) only when the spring arms. **Watchdog: 2600ms** (shared with §6.1) — if the spring has not settled, the readout prints the deviation actually measured at that moment and the word `SETTLING` instead of NOMINAL — the bench never prints NOMINAL it has not earned, even in failure. That rule is the element's soul; §10 drills it.

**Reduced motion.** Final state printed; no sequence. The signature is there; the signing is not performed.

**Accessibility.** The slate panel is real text in reading order after the headline. Live updates are *not* in a live region — a screen reader must not be read a deviation ticker; the settled state is what assistive tech receives (the DOM ends at NOMINAL, and the intermediate steps are `aria-hidden` duplicates of the same line). Contrast: chalk on slate 10.23:1 at every state; NOMINAL's engraving never reduces opacity below the printed value.

**Performance & mobile variant.** Three text nodes, updated on threshold crossings only: effectively zero per-frame cost. Mobile: identical, smaller type.

**Tokens.** `--slate`, `--chalk`, `--readout-res: 0.01%`, `--tol-class-025: ±0.25%`, `--ease-engrave`, `--watchdog-hero: 2600ms`.

### 6.6 Calibration curve plot

**What & why.** In the spec section, across the bench mat's graph paper, the flagship's calibration curve plots itself as an SVG line: indicated against true pressure for the Model 9's as-left test points — 0 → 0.0, 50 → 50.1, 100 → 99.9, 150 → 150.2, 200 → 199.8 — with each measured point stamping in as the line passes it. And one point sits visibly off the curve: the as-found repeat at true 125, which indicated 126.9 (+1.9 psi), plotted in tag red with its tag — `Pt 6 · +1.9 · RE-TEST BOOKED` — beside its re-test point at 125 → 125.1, plotted in needle orange, on the curve. The section's copy tells that story: a sticking pivot, found because the bench plots its repeats, freed, re-tested, passed. This is the theme's evidence section: the graph is drawn from the bench's own measurements (§6.17), and its most important feature is the point that is wrong — because a calibration curve with no honest outlier is a curve nobody measured.

**Structure.** An SVG plot (720×440 at desktop) on the mat: axes in `--steel-deep`, gridlines on the mat's own major grid (the graph paper *is* the plot's grid — the plot area aligns to the mat so the curve is drawn on the bench, not pasted over it), the ideal line (indicated = true) drawn dashed in `--steel`, the measured curve as a smooth path through the five as-left points in `--dial` (2.5px), points as stamped circles (r6) with mono labels, the off-curve point in `--tag` with a leader line to its tag, the re-test point in `--needle` with a `--dial` edge. Axis titles in the plate-inscription register: `TRUE PSI (DEADWEIGHT No. 4)` / `INDICATED PSI (MODEL 9, No. 1 LINEAGE)`. The full data table of all seven points is in the DOM as a visually-hidden-until-needed table beside the plot (and is §6.13's kin) — the plot is a rendering of a table, never the only copy of the data.

**Motion spec.** The plot is scrubbed to the section's passage through the viewport's middle 60%: path drawn by stroke-dashoffset over the scrub (felt duration ≈1600ms at reading speed, `--ease-engrave` on the dash), points stamp in as the line's head passes their x — a stamp is a 120ms scale 1.6 → 1.0 with a 1-frame `--tag`-free thud (no bounce; stamps land). The off-curve point stamps last, out of x-order, after a 300ms beat — the plotter pauses at the anomaly, the way a maker's pen would. If the visitor scrolls fast, the plot completes by the section's centre regardless (the scrub maps to section progress, not to time, so the evidence is never skipped by speed). Scrolling back up: the plot stays plotted (evidence, once drawn, is not undrawn); only the stamp of Pt 6 replays if the visitor returns to the section's top — no, it does not: drawn is drawn. (The spec states this twice because builders kept adding replay: a calibration record does not un-happen.)

**Choreography timeline** (relative to section progress). 0%: axes and ideal line printed (they are the bench's furniture). 10%: measured path begins drawing from (0, 0). 25%: Pt 1 (50, 50.1) stamps. 45%: Pt 2 (100, 99.9) stamps. 60%: the re-test point (125, 125.1) stamps in orange as the line passes. 70%: Pt 3 (150, 150.2) stamps. 88%: Pt 4 (200, 199.8) stamps; line complete. 100% + 300ms beat: Pt 6 (125, 126.9) stamps in tag red above the curve, its leader line draws (200ms), its tag engraves. The copy's paragraph about the sticking pivot sits directly beneath, aligned to Pt 6's x.

**State matrix.** *Rest (pre-trigger):* the fully plotted curve with all seven points and tags — the printed record. *Plotting:* as above; the data table beside it is complete from the start (the plot performs; the table *is*). *Scrolled-past:* plotted, static; the section's hover (below) still works. *Hover/focus on a point:* the point enlarges to r9 and its full record line prints in the readout register beneath the plot (`Pt 3 · TRUE 150 · INDICATED 150.2 · DEV +0.2 PSI · +0.10% OF SPAN`) — the plot's loupe, done in text. *Disabled:* fully plotted static SVG (the rest state). *Touch:* tap = hover; the record line prints identically.

**Content-merge.** The curve is the flagship product's actual calibration evidence, drawn on the bench mat's own grid, from the record's point set; the section's prose is the story of Pt 6. Remove the story and the red point is a blemish; remove the point and the story is a claim without evidence — the law (§1) requires both, together, which is why they are one element.

**Breakpoints.** ≥1200px: plot 720×440 beside its copy column. 768–1199px: plot 560×380 above the copy. <768px: plot at 92vw wide, 300px tall, point labels reduced to numerals (the full labels live in the data table and the focus line); the scrub maps to the same section progress.

**Edge cases & failure modes.** Points changed in the record: the path, stamps, tags, data table, and §8.2's example all re-derive from §6.17's point set — §10's audit samples the SVG path against the record's points (≥98% agreement at the stamped coordinates). A point set with no outlier: the theme *requires* the honest anomaly for this section's story; if a real client's data has none, the section plots the worst point (largest |deviation|) with its true tag — the bench never invents a fault, and never hides the worst truth it has. Long labels: Pt 6's tag is the only long tag; it is positioned in the plot's empty upper-left field by the layout rules, never overlapping the curve.

**Fallback & watchdog.** The static, fully-plotted SVG is the DOM default; JS arms the draw-on by setting the dash array only when the section approaches. **Watchdog: 2000ms** after the section centres — if the dash has not completed (loop stalled), the plot snaps to fully drawn. With JS disabled, the record stands plotted. The data table is unaffected by every failure mode above.

**Reduced motion.** Fully plotted from the start; point focus still prints its record line (that is interaction, not motion).

**Accessibility.** The SVG is `role="img"` with a `<title>` naming the curve and its verdict (`Calibration curve, Model 9: five points within ±0.2 psi; one as-found point at +1.9 psi, re-tested to +0.1`); the complete data table follows in the DOM for assistive tech and is the plot's equal, not its alt text. Points are focusable in the enhanced build, with visible focus (a `--dial` ring at r11) and the record line as their description. Contrast: the measured path `--dial` on `--cream-deep` mat 12.19:1; the tag point reads by its tag text (5.09:1), never by redness alone.

**Performance & mobile variant.** One SVG path draw (compositor-friendly dash animation on a single path), seven stamps: ≤0.2ms/frame during the plot. Mobile: same SVG scaled, labels reduced, identical data.

**Tokens.** `--cream-deep`, `--dial`, `--steel-deep`, `--needle`, `--tag`, `--plot-dur: 1600ms`, `--ease-engrave`, `--watchdog-plot: 2000ms`, `--mat-major: 40px`.

### 6.7 Vernier progress

**What & why.** Progress on this bench is not a bar; it is a vernier scale reading along the bench's front edge: a main scale (0–2400mm, the bench's length) with a sliding vernier plate whose index travels with scroll, and a mono readout stating the bench position to the vernier's resolution — `BENCH 1184.36 MM · OF 2400`. How far you have read is a measurement here, stated like everything else: as a reading, with a resolution, on an instrument. It merges with content because the number is not a metaphor — the traverse (§6.2) physically moves the bench through the same 2400mm the vernier reads, so the progress rail and the catalogue are two printings of one position.

**Structure.** A fixed bottom rail (44px desktop) in `--steel` with an engraved main scale (ticks every 100mm of bench, numbered every 400mm in plate inscription), a sliding vernier plate (`--cream-lit`, 120px wide) carrying the vernier's subdivisions (10 divisions spanning 9 main divisions — a true 0.02mm-resolution geometry at bench scale, drawn honestly even though the eye reads it as texture) and the live index line in `--needle`. The readout (Readout, §3) sits at the rail's right end. During the traverse pin, bench position = traverse offset; elsewhere on the page, bench position = page scroll fraction × 2400mm — one continuous quantity from hero to footer, so the vernier never jumps at the pin's boundaries (the pin's entry sets its local mapping to meet the page mapping at 600mm — the traverse occupies bench 600–1800mm of the page's full 2400mm run; the record §6.17 declares the mapping, and §13's map prints it).

**Motion spec.** The vernier plate's position is a registered value in the shared loop, lerped at 0.14 toward the scroll-derived target — the plate *slides* with the drawer's weight and settles a hair after the scroll stops, like a real vernier being slid and released. The readout updates at most every 50ms and always lands on the exact settled figure when motion stops (tabular mono, fixed-width box: `BENCH 0000.00 MM` is the widest state and the box is sized to it). No other animation: a vernier does not perform; it is read.

**Choreography timeline.** Continuous. Scroll start: plate moves within one frame. Scroll stop: plate settles within ≈300ms (lerp tail), readout lands on the exact figure at settle. Pin entry/exit: no beat, no jump — the mapping is continuous by construction (§6.17). First paint: plate at 0.00, readout `BENCH 0.00 MM · OF 2400`.

**State matrix.** *Rest:* at the current position, exact figure printed. *Sliding:* plate lerping, readout stepping at 50ms intervals. *Settled:* exact figure held. *Scrolled-past:* not applicable — the rail is fixed for the whole page; at the footer it reads 2400.00 and stops (the bench ends; the plate rests against the end stop, drawn 2px proud of the final tick — a vernier at its limit, specified so builders do not let it slide off the scale). *Disabled (no JS):* the rail prints as a static scale with the readout replaced by the section-independent line `THE BENCH IS 2400 MM LONG` — honest furniture, no fake position. *Touch:* identical; the rail is never a touch target (it is read, not operated).

**Content-merge.** The rail's scale is the bench's own length and its reading is the visitor's true position on the bench the page is built from; the traverse, the loupe, and the vernier are one mechanism viewed three ways. The rail also carries the VU miniature (§6.4) at its left end and the still-the-bench toggle (§11) at its right — the bench's front edge is where the maker keeps the instruments of the visit itself.

**Breakpoints.** ≥1200px: full rail, 44px, scale numbered every 400mm, VU miniature present. 768–1199px: rail 38px, numbering every 800mm, no miniature. <768px: rail 34px; the scale's numbering retires (ticks only) and the readout remains — position is still stated, because a small bench still measures; the rail never hides on small screens, since progress-as-reading is the theme's signature, not a desktop luxury.

**Edge cases & failure modes.** Page shorter than a viewport (huge text zoom): scroll fraction is degenerate; the vernier reads by *section* instead (each section owns a declared bench interval in §6.17; the plate rests at the reading section's interval start) — a deterministic rule, stated so two builders land on the same figure. Resize mid-scroll: the mapping recomputes from the same record; the plate lerps to the corrected position (never snaps, except under the jump rule: a teleport >50% of the bench snaps, as §6.2's jump rule). Print: the rail prints static at the reader's position — a printed page keeps its reading.

**Fallback & watchdog.** The rail is DOM furniture from first paint; JS only moves the plate. **Watchdog: 1500ms** — if the loop stalls, the plate snaps to the true scroll position (a vernier that lags forever is a wrong reading; a snapped one is a right reading arrived rudely — the bench prefers rude and right). Without JS, the static form above.

**Reduced motion.** The plate *cuts* to position on scroll (no lerp tail) and the readout updates on scroll end. Position is information, not motion; it is never removed, only stilled.

**Accessibility.** The rail is `aria-hidden` as decoration *except* the readout, which is exposed as a `role="status"` text updated on settle only (never per 50ms step — screen readers get landings, not flybys): `Bench position 1184 of 2400 millimetres`. The rail consumes no focus and no tab stops. Contrast: engraved numbering `--dial` on `--steel` 5.30:1 at 12px plate inscription — permitted by §2's ruling for engraved plate lettering; the readout itself is `--dial` on `--cream-lit` 15.08:1.

**Performance & mobile variant.** One transformed plate + one text node: ≤0.05ms/frame. Mobile: same, thinner rail.

**Tokens.** `--bench-length: 2400mm`, `--vernier-res: 0.02mm`, `--rail-h: 44px`, `--steel`, `--cream-lit`, `--needle`, `--lerp-bench: 0.14`, `--watchdog-vernier: 1500ms`.

### 6.8 The red-tagged gauge

**What & why.** Last on the bench, where the maker keeps it in sight, stands No. 31 — a 0–100 psi workshop gauge that reads 2% high: at a true 86.7 psi it indicates 88.4, its needle trembling slightly at the error, and tied to its bezel with string is a red tag, printed in chalk-white lettering: `OUT OF CAL — DO NOT USE · CAL WAS 2024-03-02`. It is never hidden, never fixed mid-page, never played for laughs. It is the bench's credibility made visible: a workshop that shows you its one faulty instrument, labelled, in place, is a workshop whose other five readings you can believe. The anti-slop heart of the original entry, deepened into the theme's moral centre — §1's law exists because this gauge exists.

**Structure.** A full instrument station in the traverse (§6.2) and a row in the bench book (§6.13): cream dial 0–100 psi, Class 1.6 plate (`CLASS 1.6 · CAL 2024-03-02 · DUE 2025-03-02 · OVERDUE`), the needle driven by a spring whose target is the *indicated* value 88.4 (the gauge is wrong, and the page's physics honestly simulates the wrong instrument — the record §6.17 holds both `true: 86.7` and `indicated: 88.4`, and the station's copy prints both: `TRUE 86.7 PSI (DEADWEIGHT No. 4) · INDICATED 88.4 · ERROR +2.0%`). The tag is an SVG card (86×52) hung from the bezel's 4-o'clock lug by a string path, rotating about the lug point. Its tremor is the healthy tremor (§5) doubled in amplitude and narrowed in bandwidth — a *nervous* needle, visibly different in character from the bench's calm tremor, specified as ±0.13% of span at 7–9Hz against the healthy ±0.06% broadband.

**Motion spec.** The tag swings as a pendulum (length 64px from lug to tag centroid; period ≈0.51s by T = 2π√(L/g) at the page's declared scale gravity — the spec uses the true formula with L in metres at the bench's 1:1 drawing scale, g = 9.81, giving the period above; builders implement the integrated pendulum, not a sine tween). Excitation: the bench's motion — traverse acceleration (§6.2) and page-scroll stops — injects angular impulse; the swing decays with damping ratio 0.08, so a hard bench slide sets it swinging for ≈6s, and at rest it hangs still. It never swings on a loop timer: a tag that swings in an empty room is a ghost story, not a workshop. The needle's take: when the station centres, the needle springs to 88.4 with the small-dial spring (ωn = 20, ζ = 0.16) — overshooting its *wrong* value and settling on it, trembling. The wrongness is in the target, not the physics: the gauge is a good spring attached to a bent truth, which is exactly what a real out-of-cal gauge is.

**Choreography timeline.** Station travel 0–30%: gauge at rest, tag hanging. Traverse acceleration peaks: tag impulse, swing begins. 50% (centred): needle takes 88.4 (≈700ms settle), tremor arms at the doubled rate, tag decaying. Station prose prints the two values and the story (below). Scrolled-past: needle holds 88.4 — the gauge does not heal when unobserved. Any later traverse pass re-excites the tag from the bench's motion alone.

**State matrix.** *Rest:* needle at 88.4 (if taken) or rest pin (if never centred), tag still. *Centring:* needle takes its wrong reading with honest physics. *Centred:* tremor at the fault rate; the tag's swing decaying; the station's `DO NOT USE` line is plain text, always printed, never revealed. *Hover/focus:* §6.9's flick is **refused on this gauge** — clicking it prints, in the readout register beneath the dial, `No. 31 IS TAGGED OUT — THE BENCH DOES NOT TAP A FAULTY GAUGE BACK TO LIFE.` (the flick's one refusal, and the theme's favourite sentence). *Disabled:* dial printed at 88.4, both values in the plate, tag printed hanging straight. *Touch:* identical; the refusal line answers taps too.

**Content-merge.** The station's copy is the workshop's calibration policy told through its one failure: what 2% high means on a customer's compressor, why the gauge is benched rather than binned (it awaits its slot on the rig; the book §6.13 shows its re-test as the queue's first line), and why it stays on the bench in view. The gauge is not a mascot and never a joke — §12 fixes its copy register: plain, unembarrassed, exact.

**Breakpoints.** ≥1200px: full station in the traverse, dial 300px, tag at natural size. 768–1199px: dial 240px in the rail build; tag swings from the same lug geometry. <768px: stack build; dial 64vw; the tag hangs (swing excited by scroll-stop impulses only — the stack still has a bench, it is just walked); the refusal line and both values print identically.

**Edge cases & failure modes.** The pendulum's excitation depends on traverse acceleration telemetry; if the loop degrades, the tag simply hangs — a still tag is a correct tag. If the record's error changes (a client gauge at +3.5%), indicated re-derives as true × 1.035 and every printing (dial target, plate, book row, §8's text) follows — §10's audit recomputes indicated from true and the stated error and fails any printing that disagrees by >0.05 psi. The tag's text is fixed by §12 verbatim and is never localised into vagueness: translations must keep `DO NOT USE` at full force.

**Fallback & watchdog.** Static print (dial at 88.4, tag hanging, both values, the refusal line) is the DOM default. **Watchdog: 2000ms** — if the needle has not taken its (wrong) reading after centring, it snaps to 88.4: even the faulty gauge's fault is reported on time. No watchdog may ever "correct" the gauge to 86.7; a build in which No. 31 reads true has failed the theme, and §10 tests for exactly that.

**Reduced motion.** Needle printed at 88.4, tag hanging still, tremor off. The fault is a fact, not an animation; reduced motion loses none of it.

**Accessibility.** The station's meaning is entirely in text: both values, the error, the dates, and the `DO NOT USE` line are DOM prose in reading order; the swinging tag is `aria-hidden` (its text is duplicated in the plate). The tag's chalk-on-tag contrast is 6.07:1. The gauge is never the page's only carrier of the calibration policy — §6.13's book row repeats its status in the ledger.

**Performance & mobile variant.** One spring, one pendulum integration: ≤0.08ms/frame while its station is near. Mobile: identical physics in the stack.

**Tokens.** `--tag`, `--chalk`, `--error-no31: +2.0%`, `--true-no31: 86.7`, `--indicated-no31: 88.4`, `--pendulum-l: 64px`, `--tremor-fault: 0.13%`, `--watchdog-gauge: 2000ms`.


### 6.9 Needle-flick click

**What & why.** Tapping the glass is the bench's oldest gesture: a fingertip flicked against a dial to free a sticking needle and prove the movement is alive. Clicking any healthy gauge on the page flicks its needle — an impulse drives it to +15% of span, it taps once against its own momentum, and the spring resettles it onto its true reading in ≈700ms, the readout re-printing as it lands. It merges with content because the flick is not a toy: it is the visitor performing the bench's own test on the bench's own claim — *tap it, watch it come back to the same number* — and the number it returns to is the record's, every time, which is the whole argument of the site compressed into one click.

**Structure.** Every gauge element (hero §6.1, traverse stations §6.2, cards §6.12, book miniatures excluded — a ledger thumbnail is not tapped, §6.13) carries a flick handler on its dial face: a real `<button>` overlay (transparent, dial-sized, `aria-label` naming the instrument and the gesture) so the flick is keyboard-operable, not a div with a click handler. The impulse is physical: on activation, the needle's spring state receives θ̇ += impulse (impulse sized to peak the needle at +15% of span from its current reading), plus a stiction break — the flick first frees the needle from its ±0.15% band, which is why a flicked needle's resettle re-earns the exact reading rather than returning to a stuck offset. The dial's paired readout (§6.5's pattern, or the station's figure line) re-opens during the swing and re-prints the settled value.

**Motion spec.** Impulse at 0ms; needle peaks at +15% of span at ≈140ms; one overshoot tap against the return (a −3% undershoot at ≈380ms — the "tap" the original describes, the needle kissing past its reading once); settled within ±0.1% by ≈700ms (small dials, ωn = 20) or ≈900ms (the hero dial, ωn = 13.5 — a big needle is a slower needle, and the spec keeps the hero's dignity). The glass answers too: a 60ms, 1px bezel shiver at the impulse (the tap lands on the *glass*, and the case feels it) — the only non-needle motion, capped at 1px so it reads as a tap, not a wobble. No sound is simulated visually beyond this; the bench does not add fake clicks.

**Choreography timeline.** 0ms activation: stiction breaks, impulse applied, bezel shiver (60ms). ≈140ms: peak +15%. ≈380ms: return tap −3%. ≈700/900ms: settled; readout re-prints the true value (and §6.5, if it is the hero, re-engraves NOMINAL over 300ms). Cooldown: a second flick during a swing *adds* its impulse to the live state (physics, not a queue) — a visitor who taps twice gets a bigger swing and the same landing.

**State matrix.** *Rest:* flick armed on every healthy gauge; cursor is the normal system pointer (the dial is a button and says so by its focus ring, not by a hand cursor — bench rule: the pointer stays the pointer; §11 buttons carry the affordance). *Swinging:* as above; further input accepted (impulse adds). *Settled:* readout re-printed; flick re-armed. *Refused (No. 31):* §6.8's refusal line prints instead — the one gauge that may not be flicked, and the refusal is content, not an error. *Disabled (no JS):* the button overlay is absent from the DOM (it is JS-inserted over the printed dial); the dial and its reading print statically. *Touch:* tap = click; the 44px minimum target is the whole dial, always satisfied.

**Content-merge.** The flick tests the very reading the gauge is currently asserting — hero pressure, a station's reading, a card's instrument — so the interaction's result is always a re-proof of that section's claim. A gauge whose flick landed anywhere but its printed reading would be a bug the theme treats as fatal (§10 drills flicks on every gauge and compares landings to the record).

**Breakpoints.** Identical at all breakpoints; dial sizes change, physics scales by §5's ωn rule. On <768px the button overlay remains dial-sized (never a small tap target glued onto a big dial).

**Edge cases & failure modes.** Rapid repeated flicks: impulses sum but the spring's target never changes — amplitude is capped by the dial's mechanical stop at +118% of span (the needle hits its upper stop pin and the spring absorbs it; a real gauge has stops, and hitting one is modelled, not clipped). Flick during the hero's initial settle: the impulse adds to the live state; the watchdog (§6.1) still guarantees the 2600ms landing. Focus-visible users: the flick fires on Enter/Space with the same physics; the bezel shiver is suppressed for keyboard activation (no glass was tapped).

**Fallback & watchdog.** Without JS there is no flick and nothing is missing — the readings print. **Watchdog: 1400ms** after any flick — if the needle has not re-settled within ±0.1% (loop degraded), it snaps to the record's reading and the readout re-prints. A snapped needle is a right reading arrived rudely (§6.7's principle).

**Reduced motion.** The flick does not animate: activation prints, in the readout line, the instrument's reading with the line `TAPPED — SETTLES AT 142.6 PSI` (value from the record) — the *result* of the test without the performance of it. The refusal on No. 31 prints identically.

**Accessibility.** The overlay is a real button with a descriptive label (`Flick the needle — Reference test gauge No. 1, currently reading 142.6 psi`); its label updates with the reading. The swing is `aria-hidden` (the SVG is already hidden; §6.1); the settled re-print is the accessible outcome and is *not* live-announced (a tap's result is the same number it started from — announcing it would be noise; the readout line is readable on demand). Focus ring: a 2px `--dial` ring on the bezel, visible against cream and steel.

**Performance & mobile variant.** The flick reuses the needle's existing spring: zero added per-frame cost beyond §6.1/§6.2's integration. Mobile identical.

**Tokens.** `--flick-peak: +15%`, `--flick-settle: 700ms`, `--stop-pin: 118%`, `--watchdog-flick: 1400ms`, `--dial`.

### 6.10 Knurled light crawl

**What & why.** Dawn comes to the bench before it comes to the workshop: a slow travelling light catches the knurled-metal edges — the cross-hatched rims of bezels, the bench trim, the loupe's ring — glinting ridge by ridge as it crosses, on a ~12s loop. It is the theme's one purely atmospheric element, and it earns its place by being *about* the concept: the original entry's bench is a bench *at dawn*, and the crawl is the dawn, arriving on schedule across the maker's tools. It merges with content because it only ever lights the instruments' own metal — it draws no shapes, highlights no text, and points at nothing; it is weather on the bench, and weather is part of the world.

**Structure.** Each knurled edge is an SVG/CSS pattern strip (a repeating 6px cross-hatch in `--steel-deep` over `--steel`) carrying a highlight mask: a linear gradient (transparent → `--needle` at 65% → transparent, 90px wide) whose background-position is driven by the shared loop's crawl phase — one phase for the whole page, so the light crosses every edge *coherently*, left to right across the bench as one dawn, not a dozen unrelated shimmers. The hero bezel, the traverse's bench trim, the loupe ring (§6.3), and the masthead plate's screws (§6.11) carry the pattern; prose sections' rules do not (dawn lights metal, not paper).

**Motion spec.** One pass per 12s: the gradient travels its strip's full width plus its own width (so it fully enters and fully leaves) at constant speed (`--ease-crawl`, linear — light does not ease), then rests off-strip for the remainder of the cycle if the strip is short: the *phase* is global (cycle 12000ms), and each strip shows the light when the phase's position crosses it — strips at the bench's left (the rig) are lit early in the cycle, the bench's right end (the ticket, §6.14) last, so the dawn literally travels the bench's length in bench order. Intensity peaks at the gradient's centre ridge-lines only (the cross-hatch mask means the light catches ridges, not the valleys — the glint is discontinuous, ridge by ridge, as the original specifies).

**Choreography timeline.** Cycle 0ms: light enters the rig's bezel. ≈3s: crossing the traverse's trim. ≈6s: the loupe ring glints. ≈9s: the masthead screws and the bench's right trim. 12s: cycle ends; 0ms: next dawn (the loop is a working morning, repeated; §5 licenses exactly this one as an ambient loop). No interaction alters it; scroll does not scrub it (dawn does not care where you are reading).

**State matrix.** *Rest:* mid-cycle wherever the phase is; on first paint the phase starts at the rig (every page load is a new dawn — a deliberate, stated choice). *Scrolled-past:* strips outside the viewport are not painted (the loop skips off-screen strips; the phase continues, so a strip re-entered shows the light wherever the dawn currently is — coherent, never restarted). *Disabled:* the knurling prints as static pattern, unlit. *Touch:* identical; the crawl has no pointer behaviour. *Dark scheme:* the same crawl at full `--needle` value (§2's after-hours ruling) — the one element that gets *stronger* in the dark, because it is the lamp.

**Content-merge.** The crawl lights only the instruments' and furniture's real knurled edges, in bench order, from one phase: it is the bench's time-of-day, shared by every element it touches. It never highlights content, never indicates state, and never competes with a needle — if a strip and a needle are in the same viewport, the needle is the orange that matters and the crawl's 65% ceiling keeps it second.

**Breakpoints.** ≥1200px: all strips as specified. 768–1199px: trim strips only (card bezels lose the crawl — fewer dawns on a smaller bench). <768px: the hero bezel and the loupe-less stack's trim only; cycle unchanged (dawn is not faster on a small bench).

**Edge cases & failure modes.** If the shared loop degrades, the crawl freezes mid-strip — a frozen gradient reads as a lit edge, which is acceptable for exactly one frame longer than the §14 cut order allows: the crawl is cut *first* when the budget tightens (it is the bench's luxury). Pattern rendering: the cross-hatch is a repeating gradient, not an image — no asset, no load failure mode. Reduced-motion visitors never see it (below).

**Fallback & watchdog.** Static knurling is the DOM default; the gradient mask is JS/compositor-applied. **Watchdog: none of its own** — the crawl is licensed to fail silently (it is weather), and §10's gate checks only that its absence is graceful and its phase coherence holds when present. No content, state, or meaning ever rides on the crawl.

**Reduced motion.** Off. The knurling prints unlit. The bench at dawn, held still, is still the bench at dawn — the copy says so, the light need not prove it.

**Accessibility.** Pure decoration: `aria-hidden`, no text, no state, no information. Its orange is capped at 65% and confined to metal edges, so it cannot be mistaken for a needle or an error by a low-vision reader; it does not flash (one 12s pass is far below any photosensitivity threshold, and the gradient's edges are soft).

**Performance & mobile variant.** Compositor-only background-position on a handful of strips: ≤0.05ms/frame, zero layout. It is §14's first cut on constrained devices, and mobile ships it only on the hero bezel.

**Tokens.** `--crawl-cycle: 12000ms`, `--crawl-width: 90px`, `--crawl-peak: 65%`, `--ease-crawl`, `--steel`, `--steel-deep`, `--needle`.

### 6.11 The maker's plate (masthead & bench-rail navigation)

**What & why.** Screwed to the bench's front edge is the maker's plate — a steel plate, engraved: `MARLOW INSTRUMENTS · EST. 1968 · CALIBRATION & REPAIR`. The masthead is that plate, and navigation is the bench rail beneath it: the site's pages named as the bench's stations (`THE BENCH`, `THE CURVE`, `THE BOOK`, `BOOK A CALIBRATION`), each with the bench position (in millimetres, from §6.17's mapping) at which it sits. A visitor navigating this site is walking a bench they have already been given the measure of; the nav's bench positions agree with the vernier (§6.7) when they arrive. It merges with content because the plate is the workshop's actual identity object — the thing screwed to real benches — and the rail's positions are the page map of §13 stated in the bench's own unit.

**Structure.** Header: the plate (a `--steel` panel, engraved lettering in `--dial` at 5.30:1, four screw heads with §6.10's knurl glint) carrying the wordmark in Oswald and the est. line in plate inscription; beneath it, the rail: text links in the inscription register, each suffixed with its bench position (`THE BOOK · BENCH 1800 MM`). The current page's link carries a vernier index mark (a `--needle` tick, 2px — the nav's one orange, licensed as the vernier's index, not as a highlight colour). A compact variant (below 1200px) keeps the plate and folds the rail into a `<details>`-style bench drawer that slides with `--ease-drawer`.

**Motion spec.** Page transitions route through §6.15 (the bench slides laterally). Within the header: the drawer opens over 380ms `--ease-drawer`; link underlines engrave left-to-right 240ms `--ease-engrave` on hover/focus; the index tick *cuts* to the active link on navigation (a vernier index does not glide between pages — it is set). The plate itself never animates; screwed-down things do not perform.

**Choreography timeline.** Page load: plate printed, rail printed, index on the current station — no entrance beats (the bench was here before the visitor). Drawer: 0ms breakaway, 380ms seated. Navigation click: §6.15 takes over.

**State matrix.** *Rest:* as printed. *Hover/focus:* underline engraves; the link's bench position is unchanged (positions are facts). *Active (current page):* index tick present; link in `--dial` full weight, others in `--steel-deep` at ≥18px-equivalent register (the inscription register at 12px uses `--dial` at 60% — no: steel-deep text is ruled graphics-only in §2; inactive links print in `--dial` at full contrast and the *index* alone distinguishes the current one — stated here because builders kept greying links into illegibility; on this bench, inactive is not the same as dim). *Disabled:* the plate and rail are plain HTML links — the header needs no JS at all, ever. *Touch:* drawer pattern; targets ≥44px.

**Content-merge.** The rail's stations are the page's actual sections/pages with their true bench positions from the record's mapping; the plate's est. date (1968) is the same 1968 the counters (§6.18) derive the bench's 58 years from. The header is the bench's nameplate, not a logo bar with a menu glued on.

**Breakpoints.** ≥1200px: plate + full rail. 768–1199px: plate + drawer. <768px: plate condensed (wordmark + est. line wraps), drawer; the bench positions retire from the rail's suffixes (they remain in §13's map and the vernier's readout).

**Edge cases & failure modes.** A page added to the site must be assigned a bench position in the record before it may appear in the rail — a nav item with no position is a build failure (§10), because an unmeasured station is exactly what this bench does not have. Long site names: the plate's wordmark is capped at two lines by §12; the plate grows taller, never wider than the bench.

**Fallback & watchdog.** None needed and none specified: the header is static HTML/CSS with zero JS dependencies — the only element in §6 with no watchdog, stated proudly, because a nameplate cannot break.

**Reduced motion.** The drawer cuts open; underlines appear without engraving. The plate, as ever, does nothing.

**Accessibility.** A real `<header>` with a real `<nav>`; the current page marked with `aria-current="page"` (the index tick is its visual twin). Drawer button is a real button with `aria-expanded`; focus order is document order. Contrast: plate lettering `--dial` on `--steel` 5.30:1 (≥12px engraved ruling, §2); rail links `--dial` on `--cream` 14.04:1.

**Performance & mobile variant.** Static; the screw glints share §6.10's phase at zero marginal cost. Mobile: the condensed plate.

**Tokens.** `--steel`, `--dial`, `--needle`, `--ease-drawer`, `--ease-engrave`, `--plate-screws: 4`.

### 6.12 Instrument cards

**What & why.** Below the traverse, the range is carded: each instrument of the record gets an enamel card — its photograph seated in an enamel instrument bezel, its name in Oswald, its reading, class, and dates in the registers, and its one-line truth. The cards are the bench for visitors who arrive mid-page (from search, from a link) and for the listing pages of §7: the same instruments, at reading size, without the traverse's ceremony. They merge with content because a card here is not a teaser tile — it carries the instrument's complete label plate and its live reading (its needle, at card scale, takes the record's value as the card enters), so the card *is* the instrument at bench scale, not an advertisement for it.

**Structure.** Cards in rows of ≤3 on the mat: an enamel face (`--cream-lit`, 1px `--steel` bezel rule, the bezel's knurled top edge where §6.10's crawl passes on desktop), a photograph in a bezel frame (aspect 4:3, reserved), a miniature dial (SVG, 120px) for instruments whose reading is a needle — VU, gauges, indicator — or a miniature trace/vernier for the others, drawn from the same record data as the traverse stations, and the label plate (name, range, class, cal, due) in plate inscription, closing with the instrument's truth line in Body small. No. 31's card carries its red tag at miniature and its `DO NOT USE` line in `--tag` text (5.09:1) — the fault is carded as faithfully as it is benched.

**Motion spec.** Cards enter with the bench fade (opacity is *not* used from zero — cards print fully and the mat's light settles; §5's rule: reveals arm instruments, not text). As a card enters the viewport's middle, its miniature needle takes its reading under the small-dial spring (ωn = 20, ζ = 0.16, settle ≈700ms) — the same take as §6.9's landing, so a card's gauge and its station's gauge agree in behaviour as well as value. Photographs scale 1.05 → 1.0 inside their bezels over 800ms `--ease-drawer` as they enter (an image seating itself). Bezels tilt toward the light on hover: max 3°, 300ms `--ease-drawer`, transform-origin at the bezel's bottom edge — a gauge tilted in the hand, never a card trick. §6.9's flick works on card dials identically.

**Choreography timeline** (per card, on entry). 0%: card printed, needle on rest pin, photograph at 1.05 unseated. +100ms: needle's spring arms. ≈800ms: needle settled on the record's reading; photograph seated. Hover: bezel tilts (300ms), the loupe does *not* appear (one loupe, one job, §6.3). Leave: tilt returns (300ms), needle holds its reading.

**State matrix.** *Rest (pre-entry):* printed, needle at rest. *Entered:* needle taken, photograph seated. *Hover/focus:* tilt 3°; the card's link (to the instrument's detail page, §7) underlines by engraving. *Scrolled-past:* needle holds its reading (readings stay taken). *Disabled:* cards print with needles *at their readings* in the static SVG (the fallback dial is drawn at value, as §6.1's) and photographs unseated-scale 1.0. *Touch:* no tilt (no hover); tap on the dial flicks (§6.9), tap elsewhere follows the card's link — the dial overlay button and the link are separate targets, never nested.

**Content-merge.** Every datum on the card is the record's: reading, class, dates, truth line. The card row's order is bench order. A card for an instrument not in the record cannot be built — §11's listing rules and §10's audit both enforce it — so the catalogue can never drift from the bench it describes.

**Breakpoints.** ≥1200px: 3 per row, dial 120px. 768–1199px: 2 per row, dial 104px. <768px: 1 per row (cards become a walked bench), dial 96px, tilt retired (stack rules), needle takes unchanged.

**Edge cases & failure modes.** An instrument with no photograph: its bezel holds its *dial at large size* instead (an instrument's face is its portrait — in-world, and specified so no builder reaches for a stock photo of a generic gauge). Long truth lines: capped by §12 at 90 characters; overflow truncates in the *copy*, never by CSS ellipsis on a measurement. A reading that changes in the record re-derives the card's dial target, plate, and §8's figures together.

**Fallback & watchdog.** Static cards with at-value dials are the DOM default. **Watchdog: 1400ms** per card after entry — an untaken needle snaps to its reading (§6.9's principle: rude and right). Photographs that fail to load leave the bezel with the instrument's engraved name — a labelled empty bezel, never a broken-image icon.

**Reduced motion.** Cards print with needles at readings, photographs seated, no tilt. The catalogue is complete and still.

**Accessibility.** Each card is an `<article>` with its heading; the miniature dial is `aria-hidden` with the reading in the plate as text; the flick button and the detail link are distinct, labelled targets ≥44px. Contrast per §2: plate inscription `--dial` on `--cream-lit` 15.08:1; No. 31's line in `--tag` 5.09:1, always accompanied by the words, never by colour alone.

**Performance & mobile variant.** Miniature springs integrate only while their card is within one viewport: ≤0.05ms/frame per live card, capped at 3 live cards. Images ≤90KB each, lazy below the fold. Mobile: single column, same budget per card.

**Tokens.** `--cream-lit`, `--steel`, `--dial`, `--tag`, `--card-dial: 120px`, `--tilt-max: 3deg`, `--ease-drawer`, `--watchdog-card: 1400ms`.


### 6.13 The bench book (calibration ledger table)

**What & why.** Every bench keeps a book: the ledger in which each instrument is entered with its number, its range, its accuracy class, the date it was last calibrated, the date it is due, and its state. The bench book section is that ledger as a table — all six instruments of the record, plus the book's totals line (`47 ON THE BOOK · 46 IN CAL · 1 TAGGED OUT` — the six on this bench being the page's instruments; the book holds the workshop's whole 47, of which the bench shows its six, a relationship the section's copy states plainly so the totals never look like they contradict the six rows). It merges with content because the book is the site's evidence in its most literal form: the traverse *performs* the instruments, the curve *plots* one, and the book *accounts* for all of them — and §6.14's ticket number is taken from this book's count, so the ledger is load-bearing for the conversion section too.

**Structure.** A ledger table on a `--cream-lit` leaf: columns `No. · INSTRUMENT · RANGE · CLASS · LAST CAL · DUE · STATE`, numeric and date columns in Plex Mono tabular, the state column in plate inscription (`IN CAL`, `IN CAL`, …, and for No. 31, `TAGGED OUT — DO NOT USE` in `--tag`). Row alternation in `--cream-deep`. The header row pins inside the section on scroll (the book is read down its length with its headings held, like a thumb on the ledger's top edge). Beneath the table, the totals line in Readout, and the queue line: `NEXT ON THE RIG: No. 31 — RE-TEST (BOOKED WITH §6.6's Pt 6)` — the book's forward entry, tying the tagged gauge's story to its scheduled redemption. The table is real HTML table markup with a `<caption>` naming the book and its date of account.

**Motion spec.** The book does not perform. Rows print; the header pins (position: sticky — no JS, no loop). The one motion: as the totals line enters, the counters (§6.18) settle on 47 / 46 / 1 — the book's numbers arriving by needle-law, because they are readings of the book. Row hover: the row's leaf warms from `--cream-lit` to `--cream` (200ms) and, for gauge rows, nothing else — the book has no flick (a ledger entry is not tapped, §6.9's exclusion, stated in the book's own footnote line: `THE BOOK IS NOT TAPPED. ENTRIES ARE READ.`).

**Choreography timeline.** Section entry: table printed in full (it is never revealed row by row — a ledger with hidden rows is a lie of omission). Totals line entry: counters settle over ≈900ms (spring, §6.18). Header pin: engages at the table's top, releases at its foot. No other beats.

**State matrix.** *Rest:* complete table, totals printed at final values (the counters' performance is an enhancement over printed totals). *Counting:* §6.18 settles the totals. *Hover/focus (row):* leaf warms; rows are not links (the instrument's detail is reached from its card §6.12 and station §6.2; the book is a record, and records are not navigation). *Disabled:* identical — the book is the most static element on the page by design. *Touch:* identical; the table scrolls horizontally inside its leaf on narrow screens with the `No.` column pinned (a ledger's index column is never scrolled away).

**Content-merge.** Every cell is the record's: numbers, ranges, classes, dates, states — §10's audit diffs the rendered table against §6.17 cell by cell. The totals are the sums of the book's states, and the queue line is Pt 6's story (§6.6) arriving at its appointment.

**Breakpoints.** ≥1200px: full seven columns. 768–1199px: `RANGE` and `CLASS` combine into one column (`0–100 PSI · CL 1.6`). <768px: the table becomes a horizontal scroll inside its leaf with `No.` pinned, all columns preserved — the book never drops a column to fit; a ledger that omits the DUE column on mobile would be hiding the very dates the theme exists to print.

**Edge cases & failure modes.** More instruments in a real client's book: the table paginates as *book pages* (§11 pagination, `PAGE 1 OF 3 · 12 TO A PAGE`), never by infinite scroll — a book has pages. A due date in the past for any row other than No. 31: the state column must print `OVERDUE` in `--tag` automatically from the record's dates — the book flags its own lapses without being told to, and §10 tests it with a synthetic overdue row. Dates print ISO (`2026-10-14`) everywhere, always — the bench does not write "last October" (§12).

**Fallback & watchdog.** No JS is involved in the book at all; the counters (§6.18) carry their own fallback. **Watchdog: none** — like the maker's plate (§6.11), the book cannot break, and the spec says so rather than inventing one.

**Reduced motion.** Identical, except the totals print without counting. The book is the reduced-motion variant of itself.

**Accessibility.** Real table semantics: `<th scope="col">`, the caption, and state text that never relies on colour (No. 31's state is words). The pinned header never overlaps row content for zoom users (sticky within the leaf only). Contrast: body `--dial` on `--cream-lit` 15.08:1, alternation rows 12.19:1, state red 5.09:1.

**Performance & mobile variant.** Static HTML; the sticky header is compositor-handled. Zero loop cost. Mobile: the pinned-column scroll, same markup.

**Tokens.** `--cream-lit`, `--cream-deep`, `--cream`, `--dial`, `--tag`, `--book-page: 12`.

### 6.14 Book a calibration (the bench-ticket form)

**What & why.** The conversion section is a bench ticket: the visitor books a calibration the way the workshop books one — a paper ticket pinned at the bench's right end, filled in with the instrument's type, its serial, and its last calibration date, and stamped with the next number in the bench book. On submit, the confirmation is the ticket itself, stamped: `TICKET № 48` — the book (§6.13) holds 47, so the visitor's instrument is № 48, a number *derived from the printed count*, not generated from a void — with its due date computed and printed as a reading (`LAST CAL 2025-06-14 + 12 MO = DUE 2026-06-14`) and its place in the queue stated. It merges with content because the form is the bench's own paperwork, obeying the bench's law: every figure on the ticket (the number, the due date, the queue position) traces to the record and to the visitor's own entered facts, shown with their arithmetic.

**Structure.** A `--cream-lit` ticket leaf with a perforated left edge (the stub stays with the bench) and the loupe *not* present (§6.3's rule). Fields (§11's bench inputs): instrument type (native `<select>` — gauge / meter / caliper / indicator / scope / other), serial number (text), last calibration date (date), service (radios: `CALIBRATION` / `CALIBRATION + CERTIFICATE` / `REPAIR — DESCRIBE BELOW`), a notes field, name and email. The submit is the **bench stamp button** (§11): a steel key whose press brings the stamp down. The confirmation replaces the leaf in place: the stamped ticket with `№ 48` in Readout large, the entered facts re-printed as the ticket's lines, the computed due date, the queue line (`POSITION 3 ON THE RIG — AFTER No. 31's RE-TEST`), and the bench's closing line (§12's fixed string). The stub (left of the perforation) keeps the number after the visitor "tears off" their copy — modelled as the confirmation's persistent header on return visits within the session.

**Motion spec.** Field focus: the field's underline draws in `--needle` (the one licensed orange in the form — it is the bench's pencil line being drawn under the visitor's writing; rationed to the single focused field). Submit: the stamp button presses (translateY 2px, 120ms), the state line prints `STAMPING…` for the request's duration (truthful to the request; a 500ms minimum so the stamp can land), then the stamp itself: `TICKET № 48` scales 1.25 → 1.0 with a 90ms `--ease-drawer` thud and a 1-frame perforation shiver — the stamp *hits the paper*. The due date's readout counts from the entered last-cal date to the computed due date over 600ms (§6.18's settle, without overshoot — a date is computed, not measured; the counters' spring is for readings, and the spec keeps the distinction). Error path: the stamp does not fall; the offending field's line prints in `--tag` with the bench's error voice (§12), all fields preserved.

**Choreography timeline** (submit). 0ms: stamp press begins; `STAMPING…`. Request resolves (≥500ms): stamp lands (90ms), ticket number prints, perforation shiver (1 frame). +200ms: due-date count (600ms). +500ms: queue line engraves. +800ms: closing line prints; the bench book's totals (§6.13, off-screen above) have incremented in the record's session state — scroll back up and the book holds 48, its queue advanced, ready to be believed (§10 reconciles this).

**State matrix.** *Rest:* empty ticket, all labels printed, the next-number line visible *before* submit (`NEXT TICKET: № 48 — THE BOOK HOLDS 47`): the visitor sees where their number will come from before they ask for it. *Filling:* focus lines draw; no validation until blur or submit (the bench does not nag mid-writing). *Submitting:* stamp state; fields disabled *except* they retain their values visibly. *Confirmed:* the stamped ticket (a document, §11's rule — outcomes are documents, not toasts). *Error:* fields preserved, error lines in place, stamp unfallen, focus moved to the first error with its message as the field's description. *Disabled (no JS):* the form posts to its server path and returns the same stamped ticket as a server-rendered page — number, due date, and queue computed server-side from the same book. *Touch:* identical; targets ≥44px; the date field is the native control.

**Content-merge.** The ticket's number is the book's count + 1; its due date is the visitor's date + the record's 12-month interval; its queue position is the book's queue (§6.13) + 1. Nothing on the confirmation exists that did not exist, as a fact, before the submit — the form *adds the visitor's instrument to the bench's own records*, which is what booking a calibration actually is.

**Breakpoints.** ≥1200px: ticket at the bench's right end, two-column fields (type/serial, date/service). 768–1199px: one column, ticket full section width. <768px: one column, the perforation becomes a top edge (the stub is above on a small bench), stamp button full width.

**Edge cases & failure modes.** Last-cal date in the future: the bench's error — `THAT DATE IS IN THE FUTURE — THE BENCH CANNOT CALIBRATE BACKWARDS.` (§12's voice: exact, dry, kind). A date more than one interval past: no error — instead the ticket prints `OVERDUE BY N MONTHS` in the due line (the bench books overdue instruments every day; it does not refuse them). Double submit: the stamp is idempotent per session token — a second press prints `ALREADY ON THE BOOK — TICKET № 48` rather than minting № 49 (§10 tests it). Network failure: `THE STAMP DIDN'T FALL — YOUR DETAILS ARE STILL ON THE TICKET. TRY AGAIN.` with every field intact.

**Fallback & watchdog.** The form is fully functional without JS (server path). **Watchdog: 4000ms** on the stamping state — if the request has not resolved, the stamp lifts, the network error line prints, and no number is consumed (the book's count is only incremented by a *confirmed* ticket, client or server — a phantom booking must not move the book, and §10's reconciliation drill kills the request mid-flight to prove it).

**Reduced motion.** No stamp thud, no shiver, no count: the confirmation prints complete. The ticket is a document; documents do not need to fall.

**Accessibility.** Native form controls with real `<label>`s; errors are text linked by `aria-describedby`, never colour alone (`--tag` text at 5.09:1 accompanies the words). The stamping state sets `aria-busy` on the form; the confirmation is a heading + region that receives focus on arrival. The perforation and stamp are decorative over a confirmation whose every fact is text.

**Performance & mobile variant.** The form is static HTML/CSS with a submit handler: no loop cost, no canvas. The stamp animation is two transforms. Mobile: same, one column.

**Tokens.** `--cream-lit`, `--dial`, `--needle`, `--tag`, `--stamp-dur: 90ms`, `--watchdog-stamp: 4000ms`, `--interval-months: 12`, `--ease-drawer`.

### 6.15 Unmarked dials (loader & page transition)

**What & why.** When the bench loads — first arrival, or a page change — the dials arrive *unmarked*: clean enamel faces with hubs and needles but no scales, the way a restored dial looks on the bench before its numerals are re-enamelled. Then the scales gain themselves in shimmer, station by station, and the needles take their readings. Between pages, the bench slides laterally (§5), rolling the next instrument set into the loupe's position. Loading on this bench is not a spinner and not a skeleton grey: it is the bench's own before-state, honest about what has not yet been *made ready* — a dial without a scale reads nothing, and the page shows exactly that until the scale exists.

**Structure.** Every dial in the page ships its SVG in two layers: the face layer (enamel, hub, needle) in the DOM from first paint, and the scale layer (ticks, numerals, inscriptions) present but masked. The unmarked state is a *class on the bench root*, applied only by JS at arm time (never in the shipped HTML — see Fallback): scale layers masked, needles at rest pins. The page transition reuses §6.2's track mechanics at page scope: on navigation, the current page's bench translates laterally by one bench-width under `--ease-drawer` (520ms) as the incoming page's bench arrives from the same side — pages are positions along one bench (§6.11's rail gives their bench positions, and the slide direction follows the positions' order: navigating to a higher bench position slides left, always).

**Motion spec.** *Initial load:* scales shimmer in over 700ms per dial, staggered in bench order (120ms apart): the mask sweeps and the ticks/numerals resolve from a 2px blur with `--steel` shimmer to full `--dial` — *enamelled*, not faded (opacity never drops the face; the face was always there, unmarked). As each dial's scale completes, its needle takes its reading (§6.1's spring for the hero, small springs elsewhere). Total ceremony ≤1600ms for the hero view; below-fold dials arm on approach, not on load. *Page transition:* 520ms lateral slide; the incoming page's hero dial arrives unmarked and gains its scale during the slide's last 300ms, needle taking its reading as the bench seats. *Skeleton use:* the same unmarked state serves as the loading skeleton for any late-arriving instrument data (a detail page's readings) — the dial waits unmarked, and a dial that waits >3000ms prints its plate with the line `READING NOT YET TAKEN` rather than shimmering forever.

**Choreography timeline** (first load). 0ms: bench printed, dials marked (the no-JS truth). JS arms (≤100ms): scales mask, needles rest — the visitor who blinked missed nothing; the ceremony replays from the armed state. +150ms: hero scale shimmers (700ms). +270ms: readout board's scales. Hero needle's settle runs §6.1's timeline concurrently (its scale completes at 850ms, before the needle's 1900ms settle — the needle must never arrive at a numeral that does not yet exist; this ordering is specified and gated in §10). Traverse stations arm on approach.

**State matrix.** *Rest (shipped):* fully marked bench — the complete page. *Arming:* masked scales, resting needles, all text and plates fully printed (only dial *scales* mask; no text ever waits for enamel). *Gaining:* staggered shimmer, needles taking. *Settled:* §6.1–§6.14's states. *Transitioning:* lateral slide; the outgoing page remains fully readable until it leaves (a bench sliding away is still a bench). *Disabled:* the shipped state *is* the final state — no arming, no masking, no ceremony. *Touch:* identical.

**Content-merge.** The loader is the instruments' own manufacturing state and the transition is the bench's own geometry (pages as bench positions from §6.11/§6.17) — neither is a generic overlay wearing the theme's colours. The shimmer's order (bench order) and the slide's direction (bench order) both teach the visitor the bench's layout while they wait.

**Breakpoints.** ≥1200px: as specified. 768–1199px: transition slide retained; load stagger compressed (80ms apart). <768px: no lateral page transition (a small bench is walked, §6.2's rule — page changes are cuts, with the incoming hero dial still gaining its scale over 500ms); load stagger 60ms.

**Edge cases & failure modes.** Slow data for a detail page: the unmarked dial + `READING NOT YET TAKEN` at 3000ms, replaced by the reading when it lands — the bench prints its ignorance with a date-line, never a spinner. Transition interrupted (user navigates again mid-slide): the slide completes to the *latest* target bench position from wherever the bench currently is (positions are absolute; the bench never gets lost between pages). Prefetch/prerender: an armed page in a hidden tab does not run its ceremony until visible (the loop sleeps hidden, §5).

**Fallback & watchdog.** The shipped DOM is complete and marked; arming is JS-only and reversible. **Watchdog: 3000ms** — any dial still masked at 3000ms unmasks instantly (a dial that cannot gain its scale prints it plainly; ceremony never outranks legibility). Page transitions degrade to cuts if the slide's first frame cannot be produced.

**Reduced motion.** No masking ceremony, no slide: pages cut, dials arrive marked, needles printed at readings. The bench simply *is* — which, under reduced motion, is the whole aesthetic (§5).

**Accessibility.** The masked state never masks text, plates, or the data tables — only dial scale *graphics* inside `aria-hidden` SVGs, whose readings are always available as text (§6.1's rule). Transitions preserve focus: on arrival, focus moves to the incoming page's `<h1>` (with `tabindex="-1"`) and the bench position is announced by the vernier's status text (§6.7). No content is ever unreachable because a slide is in progress (input is never blocked by the transition).

**Performance & mobile variant.** The shimmer is a mask/gradient pass on existing SVGs: ≤0.2ms/frame during ceremonies, zero at rest. Mobile: cuts + single-dial ceremony, near-zero cost.

**Tokens.** `--enamel-dur: 700ms`, `--stagger-bench: 120ms`, `--slide-dur: 520ms`, `--watchdog-dial: 3000ms`, `--ease-drawer`, `--steel`, `--dial`.

### 6.16 The bench at rest (footer)

**What & why.** The footer is the bench at the end of the day: the instruments at rest along the back of the mat, the day's totals chalked on the slate board, and the maker's plate screwed to the front edge one last time. It is the third printing of the book's totals (§6.13's second, §6.17's record the first) — `47 ON THE BOOK · 46 IN CAL · 1 TAGGED OUT` — chalked this time, in the bench's hand, with the day's last line: the next instrument due (`NEXT DUE: No. 7 · VU METER · 2027-09-02`, the earliest due date in the record, computed, not chosen). A footer on this bench is not a sitemap with a logo; it is the workshop closing up, and its facts are the day's facts.

**Structure.** A slate bench-back panel (`--slate`, full width): the chalk totals in Plex Sans on slate (chalk register, 10.23:1), the next-due line, the workshop's practical facts (address, hours — `BENCH HOURS: MON–FRI 08:00–17:00 · THE RIG IS BOOKED THROUGH §6.14`), and the footer links as a chalk list. Below it, the front-edge strip: the maker's plate repeated at small size (§6.11's plate, the same screws) and the colophon line in plate inscription: `EVERY READING ON THIS PAGE WAS TAKEN ON THIS BENCH · RECORD §6.17` — the theme's law, signed at the foot of the page. Miniature dials of the six instruments print along the bench-back's top edge at rest (needles on rest pins) — the day ended; nothing is being measured now.

**Motion spec.** Almost none, deliberately. As the footer enters, one chalk underline draws beneath the totals (600ms, `--ease-engrave`) — the maker underlining the day's figures before hanging up the chalk. The miniature needles do not take readings (they are at rest, and a footer that re-performs the bench would be a lie about the day being over). §6.10's crawl passes the plate screws once per cycle, as everywhere.

**Choreography timeline.** Footer entry: underline draws (600ms). Nothing else, ever. The stillness is the spec: §10 checks that the footer contains no loop but the crawl's pass.

**State matrix.** *Rest:* complete, printed, still. *After a booking (§6.14):* the chalk totals show the session's updated book (48 on the book) — the day's figures include the visitor's instrument, chalked like any other. *Disabled:* identical. *Touch:* identical.

**Content-merge.** The footer's totals are the book's totals; its next-due is the record's earliest due date; its hours are the form's booking reality (§6.14's queue assumes them). The colophon states the law that the whole page has been obeying — placed at the foot, where a maker signs.

**Breakpoints.** ≥1200px: bench-back in two columns (totals left, facts right). 768–1199px: one column, totals first. <768px: one column; the miniature dial row reduces to three (Nos. 1, 7, 31 — the standard, the mirror, and the fault: the bench's three characters, a stated selection).

**Edge cases & failure modes.** If the record's earliest due date passes (a real site, a real calendar): the line prints `NEXT DUE: No. 7 · OVERDUE — THE BOOK FLAGS ITS OWN LAPSES` — the footer applies §6.13's overdue rule to itself. Session bookings change the totals only within the session (the printed book of record is the server's; §6.14's reconciliation governs).

**Fallback & watchdog.** Static HTML; **watchdog: none** — the third element, with the plate and the book, that cannot break. The underline's draw is the only enhancement and its absence is invisible.

**Reduced motion.** The underline prints drawn. Everything else was already still.

**Accessibility.** A real `<footer>`; chalk text at 10.23:1; the miniature dials are `aria-hidden` (their instruments' facts are in the totals and the book). Links are a list, focusable in order, underlines present without the draw.

**Performance & mobile variant.** Static; the underline is one SVG path. Zero loop cost beyond the crawl's pass.

**Tokens.** `--slate`, `--chalk`, `--steel`, `--dial`, `--ease-engrave`, `--underline-dur: 600ms`.

### 6.17 The bench record (the one data object)

**What & why.** Every number in this theme — every needle's target, every plate's dates, the curve's points, the book's totals, the ticket's number, the footer's next-due — is a printing of this one declared object: the bench record. It exists as a spec element because the theme's law (§1) needs a single throat to choke: if a value is not in the record, it may not appear on the page; if it is in the record, every printing of it must agree. This section *is* the record for the reference build (Marlow Instruments), printed in full, so two builders — or a builder and an auditor — work from the same bench.

**Structure.** A single data object (authored as JSON in the build, printed here as the spec's tables). **The rig:** `rigPressure: 142.6 psi`, produced by `deadweight: No. 4`, hero deviation peaks `+0.02% / +0.01% of span`, hero tolerance `±0.25% (Class 0.25)`. **The bench:** `benchLength: 2400mm`; page mapping — hero/rig `0–600mm`, traverse `600–1800mm`, curve & book `1800–2100mm`, ticket `2100–2400mm`. **The book:** `onTheBook: 47`, `inCal: 46`, `taggedOut: 1`, `intervalMonths: 12`, `nextTicket: 48`, `est: 1968`, `yearsAtTheBench: 58` (2026 − 1968, recomputed annually by the build, never typed). **The instruments:**

| No. | Instrument | Range | Class | Last cal | Due | True reading | State |
|---|---|---|---|---|---|---|---|
| 1 | Reference test gauge (the Standard) | 0–200 psi | 0.25 | 2026-10-14 | 2027-10-14 | 142.6 psi (rig) | IN CAL |
| 7 | VU meter | −20…+3 VU | 1.5 | 2026-09-02 | 2027-09-02 | scroll velocity (§6.4) | IN CAL |
| 12 | Vernier caliper | 0–150 mm | res. 0.02mm | 2026-11-03 | 2027-11-03 | bench position (§6.7) | IN CAL |
| 19 | Oscilloscope | 20 MHz | — (see note) | 2026-08-19 | 2027-08-19 | bench hum trace | IN CAL |
| 23 | Dial indicator | 0–10 mm | 1.0 | 2026-10-30 | 2027-10-30 | 0.00 mm at rest | IN CAL |
| 31 | Workshop gauge | 0–100 psi | 1.6 | 2024-03-02 | 2025-03-02 | true 86.7 psi · indicated 88.4 · error +2.0% | TAGGED OUT |

(The scope's class cell prints `CLASS — SELF-TEST` in the book: an oscilloscope's calibration is a self-test against the bench's reference, and the book says so rather than inventing a class — the record models honesty about its own categories.) **The curve's point set (§6.6):** as-left `(0, 0.0) (50, 50.1) (100, 99.9) (150, 150.2) (200, 199.8)`; as-found repeat `(125, 126.9)` tagged; re-test `(125, 125.1)`. **The queue:** `1 · No. 31 RE-TEST · 2 · Pt 6 LINEAGE CHECK` — §6.14's visitor ticket takes position 3.

**Motion spec.** The record does not move. It *drives* motion: every spring target, counter landing, and readout in §6 is a read from this object at build time (static printings) or from its session twin at runtime (the book's count after a booking, §6.14).

**Choreography timeline.** None. The record's only timeline is the workshop's year: calibration dates fall due, the book flags them (§6.13's overdue rule), and `yearsAtTheBench` increments each January — the build recomputes derived values on every deploy, and §10's audit fails a deploy whose printed derivations are stale.

**State matrix.** *As authored:* the tables above. *Session state (after §6.14):* `onTheBook: 48`, `nextTicket: 49`, queue position advanced — held in the session twin, printed by §6.13/§6.16 within the session, never written back into the authored record by client code. *Disabled:* the record is build-time data; there is no disabled state. *Touch:* n/a.

**Content-merge.** The record is not *merged with* the content; it *is* the content, once, with §6.1–§6.16 as its printings. That inversion is the theme's whole engineering argument: build the record first (§15), print it many times, audit the printings (§10).

**Breakpoints.** The record is breakpoint-invariant. (Its printings adapt; the bench's facts do not shrink on a small screen.)

**Edge cases & failure modes.** A client whose real data contradicts the story structure (no tagged instrument): the record still declares one `state: TAGGED OUT` entry *only if it is true*; if nothing is out of cal, §6.8's station is replaced by the book's honest line `NOTHING ON THIS BENCH IS OUT OF CALIBRATION — AS OF [date]` in the same station — the bench never fabricates a fault to keep a pretty section (§6.6's rule, generalised). Missing data for a field: the field prints `NOT RECORDED` — the record admits its gaps in the same register as its facts.

**Fallback & watchdog.** The record is the fallback: every element's static printing is generated from it. **Watchdog: the §10 audits** — one-record grep, cell-by-cell book diff, curve sampling, flick landings — are this element's enforcement, run at build and at gate.

**Reduced motion.** Unaffected; the record has no motion to reduce.

**Accessibility.** The record's printings carry the accessibility duties (§6 passim); the record itself insists on one: no value may exist *only* as a needle position, a point on a curve, or a colour — every record value has at least one text printing on the page. §10 audits that too.

**Performance & mobile variant.** One small object; its cost is the discipline it imposes, which is the point.

**Tokens.** `--record-rig: 142.6`, `--record-bench: 2400`, `--record-book: 47`, `--record-next-ticket: 48`, `--record-est: 1968`, `--interval-months: 12`.

### 6.18 Readings that settle (spring counters)

**What & why.** The bench's counters — the book's totals where they appear (§6.13, §6.16), the years at the bench, the counts in prose sections — do not spin up from zero like a slot machine and do not tween linearly like a progress bar. They *settle*: driven by the same spring law as the needles (they are, mechanically, numerical needles), travelling from the previous true value, overshooting by a hair, and landing on the record's exact figure. A counter that starts at zero is a small lie (the book did not hold nothing before you looked at it); a counter that lands on a rounded figure is a bigger one. This element is the bench's counting discipline, specified once so every count on the page behaves like an instrument.

**Structure.** Any element with `data-reading` (value + unit + provenance from the record) is a counter: a mono text node (tabular, fixed-width box sized to its widest state) whose displayed value is a registered state in the shared loop, integrated with the counter spring (ωn = 9 rad/s, ζ = 0.24 — a heavier, deader spring than the needles': numbers should arrive with one small overshoot, ≈1 unit on a two-digit count, never a carnival spin). Values are formatted by the bench's rules: integers whole (`47`), measurements at their record precision (`142.6`), always with units in the line (Type law 2). Dates never count (a date is stated, not approached — §6.14's due-date count is the one licensed exception, and it counts *dates as day-numbers* between two true dates, which is arithmetic being shown, not a date being performed).

**Motion spec.** Trigger: the counter's line entering the viewport's middle. Travel: from the *previous true value* — for a first view, from the value the record held at the page's last printing (in practice: from 88% of the target for totals — no: from the *stated prior figure* where one exists in the copy ("last year the book held 44"), else from the target minus one reporting unit, so the visible travel is a *correction*, not a creation). Settle ≈900ms; the final value is the record's, exactly, and the node then holds it against tremor (counters do not tremble — Type law 5's numeric form). Re-entry: a settled counter does not recount on scroll-back; it recounts only if the record's session value has changed (post-booking totals travel 47 → 48 when their line is next seen — a small, true event).

**Choreography timeline.** Entry: spring arms. ≈450ms: overshoot peak (+1 unit typical). ≈900ms: settled on the exact figure; the unit and provenance line (already printed) now agree with the digits — the line reads whole. No stagger across counters in the same line: the book's three totals settle together, as one reading of one book.

**State matrix.** *Rest (pre-trigger):* the exact figure printed — the counter's performance is an enhancement over its own truth. *Settling:* as above. *Settled:* held, exact. *Changed (session):* re-travels between the two true values when next seen. *Disabled:* printed exact. *Touch:* identical.

**Content-merge.** Every counter's value, unit, and provenance are the record's (§6.17); the totals are the book's, the years are the est. date's arithmetic, and a count that cannot name its record field is not built (§10 greps `data-reading` values against the record).

**Breakpoints.** Identical at all breakpoints; only the spring's ωn rises slightly on mobile (10 rad/s) so settles land within the shorter attention of a small screen — the *figures* never change with the viewport.

**Edge cases & failure modes.** Large counts (a real book of 1,200 instruments): travel is logarithmic in *display* (the spring acts on the value's log for counts >999) so the settle still lands ≈900ms — stated so two builders' big benches count alike. A value of zero, when true (a queue emptied): the counter settles on 0 from 1 — the one licensed arrival *at* zero, from a true previous value, which is the opposite of spinning up from it. Loop degradation: counters snap to exact (rude and right, §6.7).

**Fallback & watchdog.** Printed exact values are the DOM default; JS re-arms them to their prior figure only when the counter approaches. **Watchdog: 1400ms** after arming — unsettled counters snap to the record's figure.

**Reduced motion.** Values print exact; no travel, no overshoot. A changed total simply reads new.

**Accessibility.** Counters are text; the settled value is the DOM's final state and the only state assistive tech is exposed to (intermediate values are `aria-hidden` swaps of the same node — implemented as a presentational span inside a static accessible line: `ON THE BOOK: <span>47</span>` where the span's animation is hidden and the line's `aria-label` carries the final figure). Contrast: mono `--dial` on its leaf, ≥12.19:1 in all printings.

**Performance & mobile variant.** A handful of integrated scalars: ≤0.05ms/frame total. Mobile identical.

**Tokens.** `--counter-k: 81` (ωn = 9), `--counter-zeta: 0.24`, `--counter-settle: 900ms`, `--watchdog-counter: 1400ms`, `--lerp-heavy: 0.08`.

---

## 7. Page application map

**Home (the bench itself).** The full bench: hero rig (§6.1 + §6.5), traverse (§6.2–§6.4, §6.8), curve (§6.6), cards (§6.12), book (§6.13), ticket (§6.14), resting footer (§6.16), vernier throughout (§6.7). This is the reference build §8 walks through.

**Listing page (the range / all instruments).** The bench un-pinned: cards (§6.12) in bench order on the mat, the book (§6.13) above them as the listing's own index, filters as §11's bench select and folds. No traverse, no loupe — a listing is the bench walked, not slid; every card still carries its live miniature reading, because a carded instrument is still an instrument.

**Detail page (one instrument).** The instrument at rig size: its dial as the page's hero (its own spring settle on arrival, §6.15's short ceremony), its full label plate, its calibration history as a small curve (§6.6's plot pattern with its own point set from the record), its book row reproduced as its record card, and the ticket (§6.14) pre-set to its type. Related instruments are cards (§6.12). No. 31's detail page prints its refusal line where its flick would be, and its re-test booking as the page's conversion — the fault's page sells honesty and a rig slot, in that order.

**About (the workshop / the makers).** An unmeasured page by default — prose on the mat, photographs of hands and benches in enamel bezels (§6.12's image treatment), the slate board for the workshop's story in chalk asides. One measured bed is permitted: the bench's own totals (§6.18) where the workshop's history is told in figures (est. 1968, 58 years, the book's 47) — numbers the record holds, counted the bench's way.

**Contact / visit (the bench door).** The ticket system (§11 inputs) on a cream leaf; the practical facts (hours, address, the rig's booking state from the record); no dial heroics — a visitor asking the way is answered plainly. Calibration booking lives in §6.14, not here; this page answers letters.

**Checkout (payment for a booked service).** **Routed out of the bench's theatre**, as the garden routed its checkout out of its own: payment is a plain cream-leaf surface (§11 buttons/inputs at their calmest), no dials, no springs, no stamp — the bench does not perform while a visitor is paying. The confirmation, however, returns to the bench: it prints the §6.14 ticket (number, due date, queue), because a confirmation is a document of the bench, and documents are where the theme is strongest.

**The unmarked hook (404/500).** §11's empty state in bench form: an empty bench hook on the mat, its plate reading `NO INSTRUMENT ON THIS HOOK`, the nearest true things offered (the bench, the book, the ticket) — and a real 404. The hook is empty because the instrument is not here; the bench says so and points at what *is* here.

---

## 8. Worked examples

### 8.1 The hero — "Measured, not claimed" (the rig, bench 0mm)

**The bed.** Marlow Instruments' homepage hero. The mat at dawn; at the bench's left end, the test rig: the reference gauge No. 1 at 420px, its needle on the rest pin; beside it the headline "Measured, not claimed." with the claim's number inline in the readout register — `142.6 PSI` — and beneath, the gauge's label plate in full. Behind the rig, the slate board carries the tolerance readout at its shipped state: `DEV 0.00% · NOMINAL · TOL ±0.25%` over `RIG 142.6 PSI · DEADWEIGHT No. 4`.

**Scroll timeline.** 0ms: first paint — the complete hero, static dial at 142.6, NOMINAL printed (the no-JS truth). JS arms (≤100ms): the scale masks for §6.15's ceremony, the needle returns to its rest pin, the readout's deviation line re-prints `DEV ———`. +150ms: the hero scale enamels in (700ms). +200ms: the needle leaves the rest pin (approach, `--ease-drawer`). +680ms: spring takes the needle (the scale completed at 850ms — wait: the ordering rule of §6.15 requires the scale complete before the needle *settles*, not before it moves; the needle's approach crosses bare enamel while the numerals enamel around it, which is the ceremony's poetry and its rule — the needle may travel an unmarked dial, it may not *report* on one; the readout holds `———` until the scale completes). +910ms: first overshoot peak (+8.0%); the readout steps to `DEV +0.02%`. +1140ms: undershoot. +1370ms: second overshoot; readout `DEV +0.01%`. +1500ms: the caption under the headline begins engraving. +2100ms: needle in its stiction band at 142.6; readout prints `0.00%` and NOMINAL engraves (300ms). Tremor arms. The visitor scrolls: the vernier plate begins to slide (`BENCH 12.40 MM…`), the VU miniature in the rail lifts off its idle — the bench is awake.

**Build notes.** Everything here is §6.1 + §6.5 + §6.15 composed; the hero-specific decisions are the headline's three-line cap and the board's placement behind the rig. If the spring cannot run, this hero is pixel-for-pixel the static composition: dial at 142.6, NOMINAL printed, plate complete.

### 8.2 Mid-page — the curve and Pt 6 (bench ≈1900mm)

**The bed.** The spec section for the flagship Model 9: copy about how the bench tests, the plot (§6.6) on the mat's grid, the data table beside it, and the paragraph about the sticking pivot aligned beneath Pt 6's x-position.

**Scroll timeline.** The visitor leaves the traverse (the bench released at No. 31, the tag's swing decaying behind them). The curve section enters: axes and the dashed ideal line are already printed. At section progress 10% the measured path begins to draw; points stamp at 25/45/60/70/88% — the re-test point (125, 125.1) stamping in orange as the line passes 125, *before* the visitor knows there is another point coming at that same x. At 100% + a 300ms beat: Pt 6 stamps above the curve in tag red — (125, 126.9) — its leader line draws, its tag engraves: `Pt 6 · +1.9 · RE-TEST BOOKED`. The copy beneath reads: "On the repeat run at 125, the needle stuck at 126.9 — a pivot fouling, found because we plot our repeats. Freed, re-tested: 125.1. The red point stays on the curve. It is the most useful point we own." The visitor hovers the red point: the record line prints `Pt 6 · TRUE 125 · INDICATED 126.9 · DEV +1.9 PSI · +0.95% OF SPAN · AS-FOUND, REPEAT RUN`.

**Build notes.** The plot, the table, the hover line, and this copy all read §6.17's point set; a builder who hard-codes "126.9" anywhere has failed §10's one-record audit. The 300ms beat before Pt 6 is the section's whole rhetoric — do not let a fast scroll compress it away: the scrub maps the *draw* to progress, but the beat is timed from the draw's completion, so a fast reader still gets the pause before the anomaly.

### 8.3 Conversion — "Book a calibration" (bench 2100–2400mm)

**The bed.** The ticket (§6.14) pinned at the bench's right end. Above it, the book section has already printed the totals — 47 on the book — and the ticket's own pre-submit line reads `NEXT TICKET: № 48 — THE BOOK HOLDS 47`.

**Scroll/submit timeline.** The visitor — a facilities engineer with a compressor gauge — selects `GAUGE`, types serial `BW-4417`, sets last calibration `2025-06-14`, chooses `CALIBRATION + CERTIFICATE`. Each focused field draws its orange pencil line. Submit: the stamp presses; `STAMPING…` holds 500ms; the stamp lands — `TICKET № 48` — with its thud and the perforation's single-frame shiver. The due date counts its arithmetic in the open: `LAST CAL 2025-06-14 + 12 MO → DUE 2026-06-14`, and beneath it, because 2026-06-14 is past at the visit's date, the honest line `OVERDUE BY 5 MONTHS — THE BENCH BOOKS OVERDUE INSTRUMENTS EVERY DAY.` The queue line engraves: `POSITION 3 ON THE RIG — AFTER No. 31's RE-TEST`. The closing line prints (§12's fixed string): "Your instrument is on the book. Bring it to the bench — we will tell you what it reads, and what it should." Scrolling back up, the book now holds 48 and its queue has advanced — the session record agrees everywhere, as §10's reconciliation drill will verify.

**Build notes.** The no-JS path posts and returns this same ticket server-rendered, number and all. The overdue computation is date arithmetic on the visitor's own fact — the bench never invents a date to make the ticket prettier, and the error path (a future last-cal date) preserves every field, per §6.14.

---

## 9. Anti-slop — what makes THIS theme look cheap

1. **A drawn needle that lies.** A gauge rendered as a pretty SVG whose needle points wherever the layout wanted, with a caption number that does not match the needle's angle. *Cure:* every needle's angle is computed from the record's value on the dial's scale; §10's audit reads the angles back. A dial whose needle and caption disagree fails the build on sight.
2. **Decorative dial clip-art.** Stock gauges, gear borders, "precision" badges with no class and no date — the clip-art of engineering. *Cure:* the law (§1): no instrument appears without its plate (range, class, cal, due), and §10 greps for unplated dials.
3. **Steampunk drift.** Brass-and-copper cosplay, rivets as confetti, sepia grunge, Victorian type — a costume, not a bench. *Cure:* §2's materials are enamel, steel, slate, and chalk; Oswald is engraved plate, not circus lettering; nothing is aged that the record does not date.
4. **Counters from zero and rounded totals.** "50+ instruments!" spinning up from 0 under a counter. *Cure:* §6.18 — counters travel between true values and land exact; totals are the record's sums of printed things.
5. **A fault that heals.** The tagged gauge quietly reading true in a card, a footer, or a reduced-motion variant — or worse, its tag used as a cute mascot with a smiley. *Cure:* §6.8's rule enforced by §10's dedicated test: No. 31 indicates 88.4 in *every* printing, and its copy register is plain and unembarrassed (§12).
6. **Spring theatre.** Needles that bounce like cartoon speedometers — huge overshoots, wobbling for seconds, tremor you can see across the room. *Cure:* §5's physics is specified (ζ = 0.16, three oscillations, settle 1900ms; tremor ±0.06%) and §10 measures it from telemetry. Premium here is *restraint that is visibly physical*.
7. **The loupe as a zoom toy.** Magnification applied to body text, hero headlines, or anything that is not an instrument's fine print — or fine print set at 8px "because the loupe will fix it." *Cure:* §6.3 — one loupe, one job, 12px floor on everything it magnifies, and every magnified line duplicated at full size in the plate.
8. **Orange everywhere.** Needle orange spent on buttons, links, and logos until the needles stop meaning "the moving truth." *Cure:* §2's census — orange is needles, the vernier index, the focused field's pencil line, and the crawl; §10 counts appearances per viewport.
9. **Progress-bar thinking.** A linear bar, a percentage, a "Step 2 of 3" — SaaS furniture on a bench. *Cure:* progress is the vernier (§6.7), a position in millimetres on the bench the visitor is actually traversing.
10. **A form that says "Submit" and a toast that says "Success!"** *Cure:* §6.14's stamp and ticket; §11's refusals (no toast, no spinner) with their bench replacements.
11. **Graph paper as wallpaper.** The mat's grid pasted behind everything including photographs and forms, until it reads as a texture pack. *Cure:* §4 — the mat is the bench surface; things *on* the bench (cards, tickets, plates) have their own enamel and paper, and the grid never shows through a face.
12. **Hidden tolerances.** The claim printed large, its class and dates in a footnote, a tooltip, or a PDF. *Cure:* Type law 2 and §6.1's plate: tolerance and provenance sit beside the claim, at readout size, in the same viewport — or the claim does not ship.

## 10. Quality gate

The build may not ship unless **every** blocking check passes. A non-builder signs the gate.

1. **Needle-truth audit.** For every dial on the page, a script reads the needle's settled angle, converts it through the dial's scale, and compares it to the record's value: agreement within ±0.1% of span required. No. 31 must read 88.4 (its indicated), and a build in which No. 31 reads 86.7 fails here specifically.
2. **One-record audit.** Grep the build for value literals (`142.6`, `88.4`, `2400`, `1968`, the cal dates) outside the bench record and its generated printings: zero strays. Plates, book cells, curve tags, ticket lines, and footer totals all print the record's values exactly.
3. **Plate completeness.** Every dial, gauge image, and instrument illustration on the page carries range, class, last-cal, and due in the plate register. One unplated instrument fails the build.
4. **Settle test.** At three scroll speeds and on a throttled CPU, the hero needle settles within ±0.1% by 2600ms (watchdog state acceptable, `SETTLING` rule of §6.5 verified: NOMINAL is never printed unearned — the drill stalls the loop and checks the readout's honesty).
5. **No-JS pass.** With JavaScript disabled: hero dial at value with NOMINAL printed, traverse as the stack, curve fully plotted with its data table, book complete, ticket form submittable to its server path, vernier in its static form.
6. **Reduced-motion pass.** With `prefers-reduced-motion`: no springs, no traverse, no crawl, no swing, no counts; every value printed at its record figure; No. 31 still at 88.4 with its tag and refusal line.
7. **Orange & red census.** Per viewport at any scroll position: orange only in licensed roles (needles, vernier index, focus pencil, crawl); red only in its roles (No. 31's tag and state lines, Pt 6, error text, the VU face's factory sector). Any other appearance fails.
8. **Contrast audit.** Body text `--dial` on `--cream` ≥14:1 measured; no steel or orange text anywhere; slate panels chalk-on-slate ≥10:1; error text `--tag` on cream ≥5:1.
9. **Flick drill.** Every healthy gauge is flicked (pointer and keyboard): landings within ±0.1% of the record's reading, every time; No. 31 refuses with its line. Overshoot peaks within the +15% ± 2% band.
10. **Watchdog drill.** With the loop artificially stalled: hero snaps by 2600ms, curve by 2000ms, dials unmask by 3000ms, counters snap by 1400ms — and every readout stays truthful throughout (no NOMINAL, no stale vernier).
11. **Ticket reconciliation.** After a test booking: ticket number = book count + 1, due date = entered date + 12 months, queue position advanced, book and footer session totals incremented — and a killed mid-flight request consumes *no* number and moves *no* total.
12. **Performance budget (§14) verified** on a mid-tier Android over throttled 4G: LCP ≤2.5s, per-frame loop ≤1.6ms, no long task >50ms during the hero settle or the traverse.

## 11. Component inventory

Every ordinary component, with its bench treatment — or its refusal and replacement.

| Component | Treatment in this theme |
|---|---|
| Primary button | The **bench stamp**: a steel key (`--steel` face, `--dial` engraved label), lit top edge, presses 2px with a 120ms settle; used once per view (the ticket's "Stamp my ticket", a section's main action) |
| Secondary button | Enamel key: `--cream-lit` face, 1px `--steel` edge, `--dial` label; hover seats it 1px |
| Text link | Dial-black, underline engraves left-to-right 240ms; visited links deepen to `--slate` (a read path on the bench is a walked path) |
| Inputs (text/email/date) | Cream-leaf fields, 1px `--steel` rule beneath, label above in Plex Sans 600; focus: the rule redraws in `--needle` (the pencil line, §6.14) |
| Select | Native `<select>` in a cream field with a steel chevron (the ticket's instrument picker) — never a custom listbox |
| Radios / checkboxes | **Bench radios**: full-width rows with the service stated in inscription register and a square enamel indicator that fills with a stamped tick (160ms); checkboxes likewise |
| Tabs | **Station tabs** (listing filters): plate-inscription labels on a steel rule, the active station carrying the vernier index tick (§6.11's mark); content swaps by cut |
| Accordion | **Bench folds**: a section that opens like a drawer — content prints downward as the drawer front slides (380ms `--ease-drawer`); one open at a time; headings are real buttons |
| Table | §6.13's bench book is the pattern for all tables: cream-lit leaf, mono numeric columns, sticky header in-section |
| Cards | §6.12 instrument cards |
| Badge / tag | **Refused as pills.** A status is a plate-inscription line (`IN CAL`, `TAGGED OUT — DO NOT USE`) printed in ink or `--tag` text — never a coloured chip. (The one physical tag in the theme is §6.8's, and it is an instrument's, not a component's.) |
| Alert / banner | A **chalk notice**: a slate strip with the message in chalk register for announcements; errors are `--tag` text lines in place (§6.14), never a red fill |
| Toast | **Refused.** Transient messages have no home on a bench; outcomes are documents (the stamped ticket) or chalk notices that persist until dismissed |
| Modal | The **loupe modal**: a centred cream leaf under a `--slate` scrim at 88% (the bench-back, dimmed — the workshop lights lowered around one task); one modal maximum; Esc and scrim-click close; focus trapped and returned |
| Tooltip | A small plate-inscription label above its element after 400ms hover/focus — tooltips carry data (an instrument's due date), never instructions |
| Pagination | Printed pagination: `BOOK PAGE 1 OF 3 · 12 TO A PAGE` as text links (§6.13) — a book has pages |
| Progress bar | **Refused as a bar.** Progress is the vernier (§6.7); a fill exists only inside the stamp button's stamping state, as a steel shading truthful to the request's elapsed time |
| Spinner | **Refused.** Waiting is an unmarked dial (§6.15) |
| Skeleton | §6.15's unmarked dials and unruled mat leaves |
| Breadcrumbs | The **bench line**: `BENCH / THE BOOK / No. 31` in plate inscription at a detail page's head, with bench positions — the path along the bench, walked in order |
| Search | A cream field in the bench drawer (§6.11); results are instrument cards + book rows (the bench's two content shapes), each with its plate |
| Toggle ("Still the bench") | A labelled enamel switch: kills tremor, crawl, and tag swing for the session; state persists; `aria-pressed` |
| Empty state | The **empty hook** (§7's 404 pattern): `NO INSTRUMENT ON THIS HOOK` on a plate, the nearest true things offered |
| 404 | §7, the unmarked hook |
| Footer | §6.16, the bench at rest |

## 12. Copywriting voice

Two registers, one bench.

**The Maker's register** (headlines, section titles, the ticket's closing line, error sentences): the voice of the person who runs this bench — plain, exact, dry, and incapable of hype. Sentence case for prose; headlines name the measured thing and its verdict: "Measured, not claimed." / "The gauge that reads 2% high, and why it stays on the bench." / "Book a calibration." Numbers always with units, tolerances always stated, dates always ISO. *Not:* "Precision you can trust!!" (exclamation marks are banned from the bench entirely — a workshop does not shout), not "Industry-leading accuracy" (leading *whom*, measured *how* — the bench would print the class instead), not "Cutting-edge calibration solutions" (nothing here is a solution; things are instruments, and they are calibrated).

**The Plate register** (labels, plates, readouts, table heads, the factual lines of errors): uppercase, letterspaced, mono — lettering stamped into a plate. `CLASS 0.25 · CAL 2026-10-14 · DUE 2027-10-14` · `TRUE 86.7 PSI · INDICATED 88.4 · ERROR +2.0%` · `NO INSTRUMENT ON THIS HOOK`. Errors are written in the Maker's voice for the sentence and the Plate register for the fact: "That date is in the future — the bench cannot calibrate backwards. · LAST CAL MUST BE TODAY OR EARLIER."

**Fixed strings (verbatim, do not paraphrase).**
- The colophon: "Every reading on this page was taken on this bench."
- The ticket's closing line: "Your instrument is on the book. Bring it to the bench — we will tell you what it reads, and what it should."
- The flick refusal: "No. 31 IS TAGGED OUT — THE BENCH DOES NOT TAP A FAULTY GAUGE BACK TO LIFE."
- The network error: "The stamp didn't fall — your details are still on the ticket. Try again."
- The 404 label: "No instrument on this hook."
- The still-toggle: "Still the bench."

**Error voice.** Specific, dry, and preserving: name the field and the fact ("The serial is empty — the bench books instruments by their serials."), never blame, never clear the form. **Empty-state voice.** A true sentence about the bench's state plus the next true thing: an empty search → "Nothing on the bench answers to that." plus the nearest instruments; an emptied queue → the rig's next free date, computed. **Label style.** Buttons are verbs from the world: "Stamp my ticket", "Read the curve", "Walk the bench" — never "Submit", "Click here", "Learn more" (say what will be learned: "Read Pt 6's story").

## 13. Scroll choreography map

The whole bench, hero to footer, in order. Bench positions are §6.17's mapping; the vernier (§6.7) reads continuously underneath all of it.

1. **Arrival (bench 0mm).** The complete printed bench (static dial at 142.6, NOMINAL). JS arms §6.15: scales mask, needle rests. The VU miniature idles at −19.6 — the bench hum is the first motion.
2. **The settle (0–600mm).** Hero scale enamels (700ms); needle approach and spring (§6.1's timeline: overshoot +8.0% at ≈910ms from arm, readout stepping +0.02 → +0.01); caption engraves; NOMINAL signs at ≈2100ms; tremor arms. The claim has been *taken*.
3. **The traverse (600–1800mm).** The pin engages; the bench slides under the loupe. Station by station: No. 1 at bench scale (its needle already true), No. 7 the VU meter leaning with the visitor's own scroll velocity, No. 12 the caliper whose vernier the loupe resolves, No. 19 the scope's hum trace drawing, No. 23 the indicator, and last No. 31 — needle taking its wrong 88.4, tag swinging from the bench's motion, refusal line printed. The detent seats each station; the vernier plate slides along the front edge the whole way.
4. **The curve (1800–1950mm).** The bench releases. The plot draws across the mat's grid; five points stamp; the orange re-test point; the beat; Pt 6 in red with its tag; the copy aligned beneath it.
5. **The cards & the book (1950–2100mm).** Card needles take their readings as the rows enter; photographs seat in their bezels. The book prints whole; its totals settle (47 / 46 / 1) as the totals line arrives; the queue line points forward to No. 31's re-test.
6. **The ticket (2100–2400mm).** The form at the bench's right end: next-ticket line already stating № 48. Focus draws pencil lines; submit stamps; the due date shows its arithmetic; the queue line engraves; the closing line prints. The book above, revisited, holds 48.
7. **The footer (2400mm).** The bench at rest: chalk totals underlined once, miniature dials on their rest pins, the next-due line, the colophon. The vernier plate rests against its end stop at 2400.00. Stillness.

**Reverse pass.** Every beat runs backwards faithfully where it is a *position* (traverse, vernier, loupe) and never where it is a *record* (the plotted curve stays plotted, NOMINAL stays signed, settled counters stay settled, a stamped ticket stays stamped). Needles hold readings once taken — scrolling up does not un-measure the bench. **Jump scroll.** Teleporting across the pin lands on the nearest station, centred, needles settled; teleporting past the curve lands with the plot complete; the vernier snaps per its jump rule. No beat is owed to a reader who teleported, and no reading is ever wrong because of how the reader arrived.

## 14. Whole-page performance budget

| Budget | Limit | Notes |
|---|---|---|
| Total page weight (home) | ≤ 720KB | Fonts ≤ 130KB (Oswald + Plex Sans + Plex Mono subsets, `font-display: swap`); instrument photographs ≤ 90KB each, ≤ 3 above the fold; all dials are inline SVG (no image dials, ever) |
| Needle physics | ≤ 0.9ms/frame all live needles | 240Hz substeps, arithmetic only, zero allocation in the loop; ≤ 6 needles live at once (hero + traverse station + cards in view) |
| Shared loop | One rAF; sleeps when settled & no ambient armed | Long tasks: none > 50ms during the settle or the traverse; traverse + loupe transforms are compositor-only |
| Loupe copy | ≤ 0.5ms/frame while the pin is active | Clip-confined repaint (§6.3); cut second under pressure |
| Ambient cost | Tremor ≈0.1ms/frame; crawl compositor-only; tag pendulum ≈0.05ms | All suspend off-screen / hidden tab |
| LCP | ≤ 2.5s on throttled 4G, mid-tier Android | The hero is DOM + static SVG at first paint — the spring never gates LCP |
| CLS | 0.00 target | Readout boxes reserved (§6.5, §6.18); bezels reserve aspect ratios; the vernier rail's height is fixed |

**Cut order when the budget is exceeded** (in this order, never silently): 1) the knurled light crawl (§6.10 — the bench's luxury), 2) the loupe lens copy (plates carry the fine print), 3) bezel tilts on cards, 4) needle substeps 240Hz → 120Hz with ζ recomputed (settle envelope held), 5) card needle takes (cards print at-value), 6) the traverse detent. **Never cut:** the hero spring's settle envelope, any printed value, any plate, the curve's point set, the ticket's honesty machinery (watchdog, preserved fields, idempotent stamp), any reduced-motion variant. A bench that must choose between its dawn light and its truth keeps its truth.

## 15. Build-order checklist

1. **The record first.** Author §6.17's bench record; generate every static printing (plates, book, curve data, footer totals) from it; write the one-record audit (§10.2) before any dial ships.
2. **Print the bench.** Static HTML/CSS: hero dial at value with NOMINAL, the traverse as its vertical stack, curve fully plotted with its data table, cards at-value, book, ticket (server path), footer. Verify the no-JS pass (§10.5) — the bench at rest is the foundation, not a fallback afterthought.
3. **Typography & palette tokens** exactly as §2–§3; run the contrast audit (§10.8) and the orange/red census (§10.7).
4. **The spring engine.** The shared loop with needle integration (240Hz substeps, §5's constants), stiction, tremor; the hero settle (§6.1) with its watchdog and the readout slaved to it (§6.5); the flick (§6.9) and its drill.
5. **The traverse.** Pin, detent, loupe copy (§6.2, §6.3) with the one-frame coherence rule; the tablet rail and mobile stack transformations.
6. **The instruments' behaviours.** VU ballistics (§6.4), the tagged gauge and its pendulum (§6.8), the curve's scrubbed plot (§6.6), the vernier (§6.7) with its page/pin mapping.
7. **Counters** (§6.18) wired to the book and footer totals.
8. **Ambient.** The crawl (§6.10) with its global phase; the "Still the bench" toggle (§11).
9. **Cards & book furniture** (§6.12, §6.13) with the overdue-state derivation tested.
10. **The ticket.** §6.14 end-to-end: pre-submit next-number line, stamping watchdog, idempotent stamp, overdue arithmetic, session reconciliation with book and footer; test the no-JS POST path.
11. **Ceremonies.** Unmarked dials & page transitions (§6.15) with the scale-before-settle ordering rule.
12. **Reduced-motion variants** for every element; run §10.6.
13. **Mobile transformations**: stack traverse, rail retirement rules, book's pinned-column scroll, ticket's top perforation.
14. **Performance pass** against §14 on real mid-tier hardware; apply the cut order if needed.
15. **The gate.** §10 signed by a non-builder — needle-truth, one-record, plate completeness, NOMINAL-honesty drill, flick drill, ticket reconciliation — before the theme may be used in a build.

---

*End of Theme 073 — The Instrument Maker's Bench (50x expansion). Identity preserved from the original entry: same concept, same five palette anchors, same three type families, all ten original signature elements deepened, and the theme's anti-slop heart kept intact — every gauge labelled with its accuracy class and last-calibration date, and one gauge deliberately shown 2% out of calibration with a red tag tied to it, because nothing on this bench is asserted without a reading.*
