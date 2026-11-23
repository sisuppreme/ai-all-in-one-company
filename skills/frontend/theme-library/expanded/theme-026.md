# 26. Movable Type Chaos — Expanded (v1 + v2)

**Identity (preserved from the original entry, deepened — never redesigned):**
a California job case — the wooden tray where every letter lives in its own
compartment — exploded into a layout engine. The page is composed of
compartments, and type keeps being sorted back into them. Palette anchors:
Case wood `#8A5A33`, paper `#F2ECDC`, sort black `#23211C`, divider red
`#A83B2A`. Type: Fraunces Black (the sorts / display) + Space Grotesk
(labels, data). The anti-slop signature: compartment sizes follow real
English letter frequency — 'e' gets the biggest box — a fact every type
nerd will check and find correct.

---

## 1. Concept & world

A job case is not a metaphor in this theme; it is the page's literal
construction. Every section of the site is a region of one enormous
California job case: headings are composed out of the tray letter by
letter, body copy lives inside wide compartment blocks divided by wood,
images sit in the tray as printer's blocks, and the visitor ends the page
by setting a word of their own in the footer composing stick. The world
is the printer's workshop floor at the moment of cheerful disorder —
type spilled, type flying home, type being re-set — but the disorder is
choreographed over a grid that is more rigorous than most "clean" sites:
the compartment sizes are computed from real English letter frequency
(§4), so the chaos has a census underneath it.

The emotional register is *skilled hands, mid-task*. Nothing on the page
is still for long, but nothing moves without a job to do: a glyph flies
because it is being sorted, a heading disassembles because the next one
is being composed, a compartment glows because its letter is about to be
used. The theme's one law: **every moving letter is either being sorted,
being composed, or being read — there is no decorative flight.** A glyph
that flies nowhere, to no compartment, for no heading, is a failed build.

**Best-fit sites.** Type foundries and letterpress studios (the obvious
home); design-tool and publishing-tool marketing pages whose product is
literally about arranging text; editorial platforms and writing tools;
museum and exhibition sites about print history; a children's literacy
product where letters are physical objects; conference sites for design/
typography events; any brand whose product is *assembly from parts*
(kits, modular furniture, recipe boxes) and wants the assembly performed,
not described. Audiences: type and design nerds first (they will audit
the case — §10 makes that audit pass), then general visitors who read
the tray as a toy they can touch (§6.7).

**When NOT to use it.** (1) Content that must feel calm, solemn or
clinical — a case mid-sort is the opposite of stillness; use The
Obituaries Page or Vellum & Wax. (2) Data-dense dashboards: compartments
are a reading grid, not a 200-row table grid; the frequency ledger
(§6.13) tops out at ~40 rows. (3) Sites whose alphabet is not Latin:
the case is sized by *English* frequency; a Devanagari or Arabic build
needs its own case computed from that script's frequency table — do not
reskin the English tray. (4) Checkout-critical flows where any motion
near the payment button is a liability — the composing-stick form (§6.12)
is for signup/order intent, not card capture. (5) Brands that cannot
tolerate a single playful note: this theme's restraint is in its
arithmetic, not its temperament.

**The frequency covenant.** The case is the theme's claim to honesty.
Lowercase 'e' occupies the largest compartment (≈3× a rare-letter cell,
§4); 'z' and 'q' get the smallest; the header case-map (§6.5) fills from
the page's *actual* headings; the counters (§5) count glyphs that
actually flew. If a build fakes any of these — uniform compartments, a
pre-filled case-map, counters that count to a round marketing number —
it has broken the covenant and fails the gate (§10, items B1–B3).

---

## 2. Palette

Four anchors from the original entry, plus a closed list of derived
tokens. Nothing else may be introduced; a fifth hue is a build error.

| Token | Hex | Role | Usage ratio | Pairing / contrast notes |
|---|---|---|---|---|
| `--paper` | `#F2ECDC` | Page ground; compartment floor; sort face highlight | ~55% of pixels | Ground for `--ink` text (13.4:1) and `--red` (5.9:1) |
| `--ink` | `#23211C` | Sort black: glyphs, body text, filled compartments | ~25% | On `--paper` 13.4:1 (AAA body); on `--wood` 3.1:1 — never text on wood |
| `--wood` | `#8A5A33` | Case wood: dividers, tray frame, compartment walls | ~15% | Decorative + large shapes only; `--paper` on it 4.9:1 (large text ≥24px only) |
| `--red` | `#A83B2A` | Divider red: active rims, case-map ink-in-progress, errors, the one accent | ≤5% | On `--paper` 5.9:1 (AA body, AAA large); never a fill behind body text |
| `--wood-deep` | `#54371E` | Derived: divider shadow side, tray outer frame, footer ground | as needed | `--paper` on it 9.8:1 (AAA); the only dark ground text may sit on besides `--ink` |
| `--wood-lit` | `#A9743F` | Derived: divider lit edge, hover glow base | as needed | Decorative only (3.4:1 on paper) — never text, never a state signal alone |
| `--paper-deep` | `#E7DEC6` | Derived: compartment floor shadow, skeleton blocks, card alt rows | as needed | `--ink` on it 11.6:1 |
| `--paper-bright` | `#FAF6E9` | Derived: lifted sort face, composing-stick well, input fields | as needed | `--ink` on it 14.1:1 |
| `--ink-soft` | `#3A372F` | Derived: secondary text, captions on paper | as needed | On `--paper` 10.2:1 |
| `--red-deep` | `#8C2E20` | Derived: error text, pressed/active red states | as needed | On `--paper` 7.6:1 (AAA) — the error-text red |
| `--red-bright` | `#C0503C` | Derived: glow rim peak during composition lift only | transient | Decorative transient only; never a resting state |

**Pairing rules.** (1) Body text is `--ink` on `--paper` or
`--paper-deep`, full stop. (2) `--red` marks *the letter in play* — the
rim of a compartment whose sort is lifting, the case-map cell currently
inking, an error's slip — and nothing else; a page where red appears in
more than ~5% of pixels has spent the accent. (3) Wood is structure,
never a text ground: labels that sit on dividers are set on small
`--paper` plaques inset into the wood (the way a printer pencils a label
and pastes it on the case). (4) Filled (used) case-map cells are `--ink`
on `--paper`; the cell being filled animates through `--red`.

**Dark mode — "lamplight", not inversion.** The case does not invert;
the workshop lights go down and one lamp stays on. `--paper` →
`#EFE4C6` (lamplit paper, text `#262219` on it, 12.1:1), page surround
`--wood-deep` darkens to `#241708`, compartment floors `#EFE4C6` at full
value inside tray regions (the lamp is *on the tray*), dividers keep
`--wood` lit from one side (`--wood-lit` edge becomes the top edge
only). Sorts stay black on paper — a sort under lamplight is still a
black letter on a pale face. Red warms one step to `#C0503C` for rims
(transient) while error text uses `#E8A08E` on the dark surround
(7.2:1). The media query is `prefers-color-scheme: dark`; there is no
manual toggle in this theme — a workshop has a lamp, not a settings
panel.

---

## 3. Typography

Two families, cast in fixed roles. **Fraunces** (opsz axis, wght 900 —
"Fraunces Black") is the sorts themselves and all display type: a
headline in this theme is not *styled like* type, it *is* type, set from
the case. **Space Grotesk** (400/500/700) is everything a printer would
pencil, stamp or tabulate: labels, captions, data, counters, body copy.

| Role | Font | Size / line-height | Tracking | Notes |
|---|---|---|---|---|
| Sort glyph (in compartment) | Fraunces 900 | 0.9 × cell height, centred | 0 | One glyph per compartment; lowercase in the lower case, capitals in the upper case (§4) |
| Display / H1 | Fraunces 900 | 56px / 1.02 (≥1200), 44px (<1200), 34px (<768) | −0.01em | Composed by §6.2; the DOM text is real from first paint |
| H2 (section heading) | Fraunces 900 | 38px / 1.08 | −0.005em | Composed by §6.3 rain-and-recompose |
| H3 (compartment head) | Fraunces 900 | 24px / 1.15 | 0 | Set statically — H3s live inside compartments and do not fly |
| Body | Space Grotesk 400 | 17px / 1.55 | 0 | Measure 52–68ch inside wide compartments |
| Compartment label | Space Grotesk 500 | 11px / 1.3 | +0.14em, UPPERCASE | On `--paper` plaques inset in dividers; names the compartment's contents ("E — 12.7%") |
| Data / counters | Space Grotesk 700 | 20px / 1.2, tabular | +0.02em | `font-variant-numeric: tabular-nums`; counters count real events (§5) |
| Caption / apparatus | Space Grotesk 400 | 13px / 1.45 | +0.01em | `--ink-soft`; states provenance ("Set from the case below") |
| Composing-stick word | Fraunces 900 | 30px / 1.1 | +0.01em | The visitor's word (§6.7) is display type — they set it, it honours them |

**Type laws.** (1) **A headline is a census.** The letters of every H1/H2
must exist in the case in sufficient count — a heading needing four 'z's
cannot be composed from a case that holds one; the build either rewords
the heading or visibly borrows (a borrowed sort arrives from the footer
tray, §6.7's stock). This is checked at the gate (§10, B2). (2) Fraunces
is never set below 20px — below that, sorts are illegible as objects and
Space Grotesk takes over. (3) Space Grotesk is never set above 28px —
labels that shout stop being labels. (4) Italic is banned: a sort has no
italic (the case would need a second tray); emphasis is weight or red.
(5) Underlining is banned except link hover, where the underline is a
1px `--red` rule — a compositor's mark, not a browser default.

---

## 4. Layout language

**The case grid.** The hero is a full-viewport California job case: a CSS
grid whose compartments are sized by real English letter frequency
(standard corpus percentages — e 12.7, t 9.1, a 8.2, o 7.5, i 7.0, n 6.7,
s 6.3, h 6.1, r 6.0, d 4.3, l 4.0, u 2.8, c 2.8, m 2.4, w 2.4, f 2.2,
g 2.0, y 2.0, p 1.9, b 1.5, v 1.0, k 0.8, j 0.15, x 0.15, q 0.10, z 0.07).
Raw ratios (e:z ≈ 180:1) cannot be drawn, so the case uses the
printer's own compression — three size classes on a base unit of one
rare-letter cell (56×56px at ≥1200px):

| Class | Letters | Cell span | Rationale |
|---|---|---|---|
| Large | e, t, a, o, i, n, s, h, r (≥6.0%) | 3 cols × 2 rows for **e**; 2 × 2 for the rest | e is the case's biggest box ≈3× a rare cell in width, as the original entry demands |
| Medium | d, l, u, c, m, w, f, g, y, p (1.9–4.3%) | 2 cols × 1 row | The working middle of the alphabet |
| Small | b, v, k, j, x, q, z (≤1.5%) | 1 × 1 | Rare sorts live small — checkable against any printed job-case diagram |
| Capitals | A–Z | 1 × 1 each, upper-case bank | Capitals share one bank above the lowercase case, all small — printers reach up rarely |
| Figures & points | 0–9, . , ' — & | 1 × 1 | One row along the case's right edge |
| Spaces (quads) | (blank compartment) | 3 cols × 1 row, no glyph | The widest *empty* box in the case — word spaces are spent constantly |

Total hero case: 26 lowercase + 26 capitals + 10 figures + 6 points +
1 quad compartment = 69 compartments. The grid is declared once with
`grid-template-areas` so the tray's geography is readable in the source —
a type nerd viewing source should find the case *correct*, not merely
plausible.

**Below the hero**, the case relaxes into the page's section rhythm:
content sits in wide compartment blocks (max 1240px at ≥1200) separated
by wood divider bands 14px tall with inset shadow (2px `--wood-deep`
below, 1px `--wood-lit` above — the divider is a *wall seen in raking
light*). Every block carries a compartment label plaque (§3) naming its
region of the case ("LOWER CASE — E THROUGH R"). Density rule: no more
than one wide block per viewport height; the case needs air between its
compartments or it reads as a spreadsheet. Whitespace in this theme is
not empty — it is *the tray's floor*, `--paper-deep` with the faintest
wood-grain gradient (≤3% contrast) so the eye always knows it is looking
into a box.

**Spacing rhythm.** Base unit 8px; divider bands at 14px break the
rhythm deliberately (wood is not on the type grid). Compartment padding
20px (≥1200), 16px (768–1199), 12px (<768). The composing stick (§6.12)
and word tray (§6.7) share a 64px height everywhere they appear — the
visitor's hands learn one tool size.

**Responsive geography.** ≥1200px: full 69-compartment case as specced.
768–1199px: capitals bank folds to a single scrolling row above the
lowercase case; large cells become 2×2 (e stays largest at 3×2 → 2×2
plus a doubled quad — no: e keeps 3 cols by borrowing the quad row's
height; the covenant is that e is visibly the biggest box at every
breakpoint). <768px: the case becomes a *drawer view* — one size class
per horizontal swipe row (Large row, Medium row, Small + figures row),
each row a native horizontal scroll-snap strip; compartments never
shrink below 44px, because a sort you cannot tap is a sort you cannot
pick (§6.7).

---

## 5. Full motion system

Five named easings, cast like type and reused everywhere — an unnamed
easing in a build is a gate failure.

| Token | Curve | Used by |
|---|---|---|
| `--ease-sort` | `cubic-bezier(0.16, 1, 0.3, 1)` (easeOutExpo equivalent) | Sorts flying home (§6.1), FLIP flights (§6.7) |
| `--ease-settle` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | The tiny individual bounce as a sort lands in a compartment or a headline letter settles (§6.1, §6.2) — overshoot ≤4%, ≤180ms |
| `--ease-rain` | `cubic-bezier(0.55, 0, 1, 0.45)` (accelerating) | Heading glyphs falling into the case (§6.3) — gravity, not glide |
| `--ease-door` | `cubic-bezier(0.22, 1, 0.36, 1)` (easeOutCubic equivalent) | Compartment-door reveals (§6.6), divider draw (§6.9) |
| `--ease-lift` | `cubic-bezier(0.33, 1, 0.68, 1)` | Composition lift (§6.2), hover lifts (§6.10 hover state) |

**Every motion term, translated into the case's language:**

- **Scroll-triggered reveals** — compartment doors (§6.6): blocks open
  from their bottom edge as they enter; headings rain-and-recompose
  (§6.3) at section boundaries.
- **Scroll-scrubbed sequence** — the hero sorting sequence (§6.1/§6.2):
  through 160vh of pinned scroll, glyphs fly to compartments in
  proportion to scroll progress, then the headline composes. Scrub
  values pass through the shared rAF loop, lerp 0.12.
- **Parallax** — three depths inside the case only: wood grain at 0.92,
  compartment floors at 1.0, flying sorts and labels at 1.06. Parallax
  never applies to body text blocks below the hero (reading copy sits
  still in its compartment).
- **Pinned scenes** — the hero case pins for 160vh (≥1200) / 120vh
  (768–1199); below 768 there is no pin — the drawer rows scroll
  natively and composition happens on entry instead (§6.2 breakpoints).
- **Masked reveals** — the compartment-door clip-path (§6.6) and the
  headline's per-letter rise from behind the tray's front edge (§6.2).
- **Blur-to-sharp — REFUSED.** A wooden sort is never out of focus; it
  is either in the hand or in the box. Blurred type reads as a screen
  effect, not a physical one, and this theme's whole claim is physical.
  Arrivals land with a 1px overshoot and a shadow, never a blur.
- **Kinetic typography** — the headline composition (§6.2) *is* the
  kinetic type: letters travel from their compartments to the title
  line. No other text on the page moves as text.
- **Marquee — REFUSED.** Type in a case does not travel sideways in a
  loop; a marquee would be a conveyor belt in a hand workshop. The
  ambient life slot is given to the restless sort (§6.4) instead.
- **Animated counters** — "SORTS SET" and "WORDS COMPOSED" (§6.5's
  companions in the header rail): each counts only events that actually
  occurred (a glyph landed; a heading finished composing), tabular
  Space Grotesk, 120ms per increment, no easing theatre.
- **Progress indicator** — the case-map (§6.5): scroll progress drawn
  as the page's own alphabet usage, plus the tide of ink in the current
  compartment rim.
- **Ambient loops** — exactly two: the restless sort (§6.4, one hop per
  ~9s) and the wood-grain light shift (a 26s warm gradient drift across
  dividers, ±3% luminance — felt, not seen). Two is the cap; a third
  ambient loop makes the workshop feel haunted, not alive.
- **Micro-interactions** — hover lifts a compartment's sort 6px with a
  rim glow (§6.10); click picks it (§6.7); buttons are wood plaques
  that press 2px into the tray with a shadow collapse (§11).
- **Hover physics** — the case tilt carry (§6.8): the whole tray tilts
  ≤1° toward the pointer quadrant over 800ms; shadows shift opposite.
- **Page transitions** — the case-lid (§6.16): a wood lid slides over
  the viewport from the tray's top edge (420ms), route swaps at full
  cover, lid lifts. Browser back/forward is never intercepted.
- **Image treatment** — images are printer's *blocks*: mounted in
  compartments at type height, wood-framed, scaling 1.06→1 inside
  their compartment as they cross the viewport centre (§6.11).

**The shared loop law.** One `requestAnimationFrame` loop drives every
scrubbed value (hero sort flight progress, parallax depths, tilt,
case-map ink). It lerps at 0.12, writes only `transform`/`opacity`/
CSS variables, idles to zero work when nothing is in flight, and is
the only loop: per-element `setInterval` animation is a build error
(the restless sort's 9s timer *schedules* a hop; the hop itself runs
in the shared loop).

---

## 6. Signature elements

### 6.1 The sorting spill

- **What & why.** On load, ~60 loose glyphs lie scattered and rotated
  across the hero case — type spilled on the tray — and fly to their
  exact compartments over 1.4–2.2s, staggered in frequency order (e
  first, z last). It is the theme's thesis in one gesture: this page's
  raw material is letters, and its first act is putting them away. The
  spill is not an intro animation pasted over the hero; the glyphs land
  *in* the compartments the visitor will use for the rest of the page
  (§6.5, §6.7 read their state from these same cells).
- **Structure.** The hero case grid (§4) renders complete in HTML: every
  compartment holds its real sort (a Fraunces glyph on a `--paper-bright`
  face with a 2px `--ink` keyline). A JS-only clone layer
  (`aria-hidden`, absolutely positioned, `pointer-events:none`) carries
  the 60 scattered glyphs at pre-computed spill transforms (rotation
  −38°…+41°, offsets within the tray). Each clone knows its home
  compartment's rect; flight is a FLIP transform from spill position to
  home rect, after which the clone fades (60ms) exactly as the real sort
  beneath it is revealed — the swap is invisible because both glyphs are
  the same letter at the same size.
- **Motion spec.** Trigger: load, after fonts ready or 300ms, whichever
  first (a glyph in the wrong font flying home would land as a stranger).
  Duration per glyph: 1400ms (e) increasing by frequency rank to 2200ms
  (z, q, j, x) — rare letters travel from further away in a real spill.
  Easing `--ease-sort`; landing settle `--ease-settle` 140ms with a 1px
  overshoot and a shadow that collapses from 8px to 2px. Stagger: glyphs
  depart in frequency order, 24ms apart within a class, classes
  overlapping by 40%. Total sequence ≤3.4s; a "skip" is implicit — any
  scroll input fast-forwards all remaining glyphs to landed within
  200ms.
- **Choreography timeline (v2).** t₀ = fonts-ready/300ms. t₀+0: e lifts
  (shadow grows) and departs. t₀+24ms×n: each next glyph departs in
  frequency order. t₀+1400: e lands, settle bounce, its compartment rim
  flashes `--red` for 300ms (the case acknowledging receipt).
  t₀+2200–3400: last rare glyphs land; spill layer empties. t₀+3500:
  clone layer removed from DOM; §6.2's composition may begin (it waits
  for an empty spill layer or a scroll trigger, whichever first).
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest (pre-flight) | Glyphs scattered, real sorts hidden beneath clones | Same, spill count cut to 36 |
  | Flying | Per-glyph FLIP, staggered by frequency | Same, durations ×0.85 |
  | Landed | Clone gone; real sort at rest in its compartment | Same |
  | Hover | n/a (flight is not interactive) | n/a |
  | Focus | The case region is not focusable during flight | Same |
  | Scrolled-past / skipped | All glyphs landed instantly (200ms settle-all) | Same |
  | Disabled / no-JS | No clone layer exists; the case stands full and sorted | Same |

- **Content-merge.** The spill *is* the hero's raw material and the case
  is the page's layout grid. The 60 glyphs are drawn from the page's own
  headline letters first (every H1 letter flies home before any filler
  sort), so the opening literally inventories the title.
- **Failure fallback.** The DOM case is complete and sorted without JS.
  The clone layer is inserted only by JS after first paint; if the
  flight engine throws, a 1000ms watchdog (the theme's standing 1s law)
  removes the clone layer and the sorted case simply stands there. If
  fonts fail, flight still runs — glyphs land in the fallback serif and
  swap when/if Fraunces arrives (no re-flight).
- **Reduced-motion variant.** No spill, no flight. The case loads sorted;
  the headline (§6.2) is already composed. One still detail survives:
  the 'e' compartment rim carries a resting 1px `--red` keyline — the
  mark of the most-used box.
- **Breakpoints (v2).** ≥1200px: 60 glyphs, full case. 768–1199px: 48
  glyphs; capitals bank is a row, and capital clones fly vertically
  (shorter arcs). <768px: 36 glyphs, drawer-row geography (§4); flights
  are horizontal within a row where possible; total sequence ≤2.6s.
- **Edge cases & failure modes (v2).** *Slow network:* if Fraunces has
  not loaded by 900ms, fly in the metric-matched fallback and swap
  faces on `document.fonts.ready` — never hold the page hostage to a
  font. *Resize mid-flight:* targets are recomputed on the next frame
  (rects are read live, not cached at departure); a glyph in flight
  bends its path, never teleports. *Tab hidden mid-flight:* rAF pauses;
  on visibility return, a 400ms settle-all completes the sort (the
  printer finished while you were out). *User prefers data saver:*
  spill count halves; the case is unchanged.
- **Accessibility spec (v2).** The clone layer is `aria-hidden`; the real
  case is a `<ul>` of compartments each labelled "Letter e — 12.7 percent
  of English text" so a screen reader meets a census, not a puzzle.
  Flight is never announced (it is atmosphere over content that is
  already fully present as text). Focus order is untouched — nothing in
  the hero case is focusable until §6.7 makes sorts pickable, and that
  happens after the spill completes.
- **Performance budget & mobile variant.** ≤60 simultaneous transforms,
  all on the compositor; clone layer ≤180KB of DOM. Flight math ≤0.6ms
  per frame inside the shared loop. Mobile: 36 glyphs, and the clone
  layer uses `will-change` on at most 12 glyphs at once (rolling window
  by departure order).
- **Tokens consumed (v2).** `--paper`, `--paper-bright`, `--ink`,
  `--red`, `--wood`, `--ease-sort`, `--ease-settle`, `--spill-count`
  (60), `--spill-min` (1400ms), `--spill-max` (2200ms), `--stagger-sort`
  (24ms), `--watchdog` (1000ms).

### 6.2 Headline composition lift

- **What & why.** After the sort, the hero headline is *composed*: the
  compartments holding the headline's letters glow divider-red at their
  rims, their sorts rise 18px out of the tray, fly to the title line
  above the case, and settle letter by letter into the H1. The visitor
  learns the page's central mechanic — headings here are not printed,
  they are *set* — by watching the first one happen. Every later heading
  (§6.3) is a variation they already understand.
- **Structure.** The H1 is real DOM text from first paint (SEO, no-JS,
  and screen readers all meet the finished headline). Above it, a
  JS-only clone layer: for each headline character, a sort clone is
  lifted from its compartment (rect read live), flown along a shallow
  arc to the character's position in the H1, and faded at arrival as the
  real character — initially rendered in `--ink-soft` at 92% ink —
  deepens to full `--ink`. Spaces in the headline come from the quad
  compartment: no glyph flies, but the quad cell glows and the gap in
  the title line widens from 0.2em to its true width as its neighbours
  land. Duplicate letters consume multiple sorts: the case holds a
  stated stock per letter (§3 type law 1); the second 'e' in a headline
  lifts from the *same* e compartment 90ms later (the printer dips back
  into the box).
- **Motion spec.** Trigger: hero pin scrub — composition progress maps
  to scroll through the first 60% of the 160vh pin (≥1200px). Each
  letter's flight: 520ms `--ease-sort`, rise 18px in the first 80ms,
  arc peak +26px above the straight line, settle `--ease-settle` 160ms
  on landing. Letters fly in reading order, one per 6% of scrub range.
  Rim glow: compartment rim `--red` at 0→100% over 120ms as its letter
  lifts, holding until landing, then fading over 400ms. Scrolling back
  up reverses the composition symmetrically — letters return to the
  tray; the headline is a pure function of scroll position inside the
  pin, never latched.
- **Choreography timeline (v2).** Scrub p = 0→0.6 across the pin.
  p=0.02: first letter's rim glows. p=0.05: it lifts (18px, 80ms).
  p=0.05–0.11: flight + settle; real character deepens. Each subsequent
  letter repeats at +0.06 p. p=0.6: last letter landed; all rims faded;
  H1 at full ink. p=0.6–1.0: pin holds the composed headline over the
  full case for one reading beat, then releases into §6.3 territory.
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest (p=0) | Headline in soft ink above a sorted case; rims dark | Same; headline composed on entry instead (no pin) |
  | Composing | Letters in flight per scrub | n/a — entry-triggered, 520ms per letter, reading order, total ≤2.8s |
  | Composed | Full-ink H1; case at rest below | Same |
  | Hover | Hovering a landed headline letter highlights its home compartment rim (the census made visible) | n/a |
  | Focus | H1 focusable as heading only; no letter-level focus | Same |
  | Scrolled-past | Composed; scrolling back into the pin de-composes symmetrically | Static composed |
  | Disabled / no-JS | Full-ink H1 above a sorted case | Same |

- **Content-merge.** The flying objects are the headline's own letters,
  sourced from the compartments that genuinely hold them; the glow marks
  real inventory. Remove the animation and the page loses a lesson, not
  a word.
- **Failure fallback.** H1 is full text in the DOM at full ink by
  default; JS *dims* it to 92% only when the composition engine is armed
  and the pin is measured. Any failure (no IntersectionObserver, loop
  stall >800ms) restores full ink and removes clones — the standing
  fallback of the original entry ("1s fallback hides the clone layer")
  applies verbatim.
- **Reduced-motion variant.** No pin, no flight: the H1 stands composed
  at full ink above the case; the case-map (§6.5) still fills as the
  visitor scrolls, so the census idea survives without the journey.
- **Breakpoints (v2).** ≥1200px: scrub composition in the 160vh pin.
  768–1199px: pin shortens to 120vh, scrub range 0→0.75. <768px: no pin;
  composition runs once on hero entry (520ms/letter, capped 2.8s total
  by overlapping flights 40%), and is skipped entirely if the hero is
  entered already scrolled past (deep link) — the headline simply
  stands composed.
- **Edge cases & failure modes (v2).** *Headline longer than the case's
  stock:* §3 law 1 — reword, or borrow: the borrowed sort flies a longer
  arc from the footer word tray (§6.7) with a `--red` rim on the *tray*,
  and the caption notes "one sort borrowed from the tray below" —
  borrowing is shown, never hidden. *Fast scroll through the pin:* the
  lerp settles p to its true value; letters land in order at up to
  3-per-frame; none stick mid-air (a 300ms settle timer after scroll
  rest forces exact final states). *Very long H1 (>9 words):* compose
  only the first line by flight; remaining lines deepen from soft ink —
  a full-paragraph flight is a parade, not a composition.
- **Accessibility spec (v2).** One H1, real text, correct reading order;
  clones `aria-hidden`. The dim-to-full ink change never drops contrast
  below 7:1 (92% ink on paper ≈ 9.4:1 — the "dim" state is still AAA).
  Keyboard visitors meet the composed headline; the pin adds no focus
  traps (pin is a scroll region, not a modal). Touch targets: headline
  letters are not targets.
- **Performance budget & mobile variant.** ≤14 concurrent letter flights;
  clone layer shares §6.1's budget. On <768px the arc flattens (peak
  +12px) and rise is 10px — small tray, small gestures.
- **Tokens consumed (v2).** `--ink`, `--ink-soft`, `--red`, `--paper`,
  `--ease-sort`, `--ease-settle`, `--ease-lift`, `--flight-letter`
  (520ms), `--rise-sort` (18px), `--pin-hero` (160vh), `--loop-lerp`
  (0.12).

### 6.3 Heading rain-and-recompose

- **What & why.** At each section boundary, the outgoing H2's glyphs
  detach, rain down into their compartments (600–900ms, slight
  rotation), and the next heading's sorts lift and compose in its
  place. It is the section transition itself — content changes by being
  re-typeset — and it teaches the visitor, at every boundary, that the
  page's stock of letters is finite and shared: the 'e' that leaves one
  heading is the 'e' that arrives in the next.
- **Structure.** Each H2 is real DOM text. A shared clone layer (the
  same mechanism as §6.2, one layer for the whole page) animates glyph
  clones: outgoing clones are spawned at the old heading's character
  rects and flown *down* to their home compartments; incoming clones
  lift from compartments to the new heading's rects, where the real
  heading — pre-rendered at 92% ink like §6.2 — deepens per letter on
  landing. The two headings never animate simultaneously in the same
  viewport region: rain completes (or is ≥80% landed) before compose
  begins, enforced by the shared loop's serial queue.
- **Motion spec.** Trigger: the boundary between sections crossing
  55% of viewport height (scroll). Rain: per glyph 600ms (short fall,
  near compartment) to 900ms (long fall), `--ease-rain`, rotation
  settling from ±14° to 0, landing settle 120ms. Compose: §6.2's
  grammar at H2 scale — 460ms flights, reading order, 50ms stagger.
  Total boundary event ≤1.6s. Scrolling back up across the boundary
  runs the event in reverse (the previous heading re-composes; the
  current one rains home) — the queue is symmetric and interruptible:
  a new boundary crossing cancels in-flight glyphs to their nearest
  end state within 150ms rather than queueing a backlog.
- **Choreography timeline (v2).** t₀ = boundary at 55% vh. t₀+0: old
  heading's first glyph detaches (its real character dims to a ghost
  outline at 30% ink — the word stays legible as a *memory* while its
  letters leave; it never vanishes). t₀+40ms×n: glyphs detach in
  reading order. t₀+600–900: glyphs land in compartments; rims flash.
  t₀+950: new heading's first sort lifts. t₀+950+50×n: compose
  stagger. t₀+1600: event complete; old heading removed from the
  accessibility tree only when fully scrolled past (it remains a
  normal heading in the DOM until then — the *visual* clone layer is
  the only theatre).
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Heading composed at full ink | Same |
  | Raining | Glyphs falling; ghost outline holds legibility | Same, falls shorten (≤700ms) |
  | Composing | Sorts lifting into the new heading | Same |
  | Hover | n/a | n/a |
  | Focus | Heading is a normal heading; focus never moves due to the event | Same |
  | Scrolled-past | Fully composed, event will reverse on return | Same |
  | Disabled / no-JS | Headings stand composed; boundaries are plain scroll | Same |

- **Content-merge.** The transition *is* the content change: the same
  finite stock of sorts leaves one heading and forms the next. The
  compartments that receive the rain are the ones §6.5 inks and §6.7
  picks from — one inventory, three witnesses.
- **Failure fallback.** Real headings are always in the DOM at readable
  ink (the ghost state is 30% *clone-layer* dimming over a heading that
  itself never drops below full contrast in the accessibility tree and
  never below 92% visually for more than the event's 1.6s). Loop stall
  >800ms: clones removed, both headings at full ink, boundary treated
  as plain scroll.
- **Reduced-motion variant.** No rain, no compose: headings crossfade
  ink depth only (92%→100% over 200ms) as they enter — a compositor's
  nod, not a performance.
- **Breakpoints (v2).** ≥1200px: full spec. 768–1199px: falls capped
  800ms, stagger 40ms. <768px: rain only for the *first* boundary per
  page session (the lesson taught once); later boundaries use the
  reduced grammar (ink deepen) — a phone page with six raining
  headings is a slot machine.
- **Edge cases & failure modes (v2).** *Two boundaries in one viewport
  (short sections):* the queue merges them — the middle heading
  composes and rains within one event, total ≤2.2s, or is skipped to
  static if a third boundary is already queued. *Heading edited by CMS
  to need unavailable sorts:* §6.2's borrow rule applies, from the
  tray. *Print:* headings print composed; the clone layer is
  `display:none` in print CSS.
- **Accessibility spec (v2).** Heading order and text are never altered
  in the DOM; clones are `aria-hidden`; the event is not announced.
  A heading that is raining is still the heading a screen reader
  lands on — visual theatre never removes the landmark.
- **Performance budget & mobile variant.** One shared clone layer,
  ≤28 glyphs in flight across the whole page at any moment (rain +
  compose combined); if a boundary event would exceed it, stagger
  compresses. Mobile variant as per breakpoints.
- **Tokens consumed (v2).** `--ink`, `--red`, `--ease-rain`,
  `--ease-sort`, `--ease-settle`, `--rain-min` (600ms), `--rain-max`
  (900ms), `--compose-h2` (460ms), `--stagger-heading` (50ms),
  `--boundary-line` (55% vh).

### 6.4 The restless sort

- **What & why.** One sort in the case is restless: every ~9s it hops
  to a neighbouring compartment (120ms hop, small squash on landing),
  sits in the wrong box for a beat, then hops home. It is the theme's
  single ambient life-sign — the apprentice's misfiled letter — and it
  keeps the case visibly *in use* inside the content grid the visitor
  is reading, without a marquee, a carousel, or any second ambient
  loop (§5 caps ambient at two, and the other is the wood light).
- **Structure.** A clone of one real sort (chosen at runtime from the
  medium class — never 'e', whose box is a landmark, and never a sort
  currently committed to a heading or the visitor's word). The clone
  lives in the hero case's clone layer; the hop is a 120ms transform
  along a 10px arc to the adjacent compartment, a 90ms squash
  (`scaleY 0.92`) on landing, a 2.4–3.2s wrong-box sit (the clone sits
  *in front of* the resident sort, slightly askew at 3°), then the
  return hop. Which sort is restless rotates: after three round trips,
  a different medium-class sort takes over, so repeat visitors can't
  memorise the trick.
- **Motion spec.** Trigger: time — a 9s±1.5s (jittered) scheduler, only
  while the hero case is within one viewport of the reading position
  and the tab is visible. Hop 120ms `--ease-settle`; arc height 10px;
  squash 90ms. Total excursion ≤3.6s; the case is still ≥60% of every
  9s cycle. If §6.1/§6.2/§6.3 has glyphs in flight, the hop waits — the
  restless sort never competes with real work.
- **Choreography timeline (v2).** t₀ = scheduler fires. t₀+0: clone
  lifts 4px. t₀+120: lands in neighbour box, squash. t₀+210: settled,
  askew 3°. t₀+2400–3200: return hop (120ms), squash, clone fades 80ms
  over the real sort (which never moved). Next cycle ≥9s later.
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Sort in its box; indistinguishable from stock | Same |
  | Hopping | 120ms arc to neighbour | Same (case visible in drawer rows) |
  | Misfiled sit | Askew in the wrong box 2.4–3.2s | Same |
  | Hover (on the case) | Scheduler pauses — attention freezes the apprentice | n/a |
  | Focus (in the case) | Scheduler pauses while focus is inside the case | Same |
  | Scrolled-past | Scheduler off; no hops off-screen | Same |
  | Disabled / no-JS | No clone; the case is simply correct | Same |

- **Content-merge.** The hop happens inside the working case, between
  real compartments, using a real letter — it is a story about the
  inventory, told by the inventory. It never overlays text blocks.
- **Failure fallback.** Pure enhancement: if the clone layer is absent
  or the loop is down, nothing is missing — a correct case is the
  fallback. The scheduler is the first thing cut under the §14
  performance ladder.
- **Reduced-motion variant.** None. The restless sort sits still; the
  case is correct and complete.
- **Breakpoints (v2).** All breakpoints: same grammar; on <768px the
  hop is within the visible drawer row only (a hop to an off-screen row
  is a rumour, not an event).
- **Edge cases & failure modes (v2).** *Neighbour box is the quad
  (space) compartment:* allowed — a letter sitting in the spaces box
  is the funniest version and harms nothing. *The chosen sort gets
  picked by the visitor (§6.7) mid-sit:* the clone completes its return
  hop immediately (150ms) and restlessness rotates to another sort;
  the pick uses the real sort, never the clone. *Battery saver / long
  task pressure:* scheduler interval stretches to 20s, then off (§14).
- **Accessibility spec (v2).** Clone is `aria-hidden`; nothing is
  announced; the real sort never leaves the accessibility tree. The
  hop is ≤120ms and small — below vestibular concern, and fully off
  under reduced motion.
- **Performance budget & mobile variant.** One clone, two 120ms
  transforms per ~9s — the cheapest element in the theme. No mobile
  change beyond the drawer-row rule.
- **Tokens consumed (v2).** `--ease-settle`, `--hop` (120ms),
  `--hop-interval` (9s ±1.5s), `--squash` (90ms), `--misfile-tilt` (3°).

### 6.5 Case-map progress

- **What & why.** A miniature case in the header inks each compartment
  (wood → sort black fill) the first time its letter is used in a
  composed heading. It is the scroll progress indicator, drawn from the
  page's own alphabet usage: the visitor doesn't just learn "60%
  through", they learn "this page has used 19 of its 26 letters" —
  progress as census. Beside it, the counters "SORTS SET n · WORDS
  COMPOSED n" (§5) tally the same events in figures.
- **Structure.** A 26-cell mini-grid (lowercase only — the header is
  44px tall; capitals and figures are omitted and the omission is
  stated in its label plaque: "LOWER CASE — AS USED"). Each cell is a
  10×10px (≥1200) square with a 1px wood keyline, its letter in 7px
  Space Grotesk. A cell inks by filling `--ink` from its bottom edge
  (height 0→100%, 300ms `--ease-door`) the moment a heading containing
  that letter finishes composing (§6.2/§6.3 fire the event; the map
  counts *composed* letters, never scrolled-past ones). The cell
  currently inking passes through `--red` at 50% fill. The counters sit
  right of the map in the header rail, tabular figures.
- **Motion spec.** Trigger: heading-composed events. Fill 300ms per
  cell; multiple letters from one heading stagger 30ms in the order
  they first appear in that heading. A letter already inked does not
  re-animate — the map is a ledger, not a light show. At 26/26 the map
  performs its one flourish: all rims flash `--red` in frequency order
  over 600ms and the label changes to "FULL CASE — EVERY LETTER USED"
  (a pangrammatic page is an achievement worth stamping).
- **Choreography timeline (v2).** t₀ = heading composed. t₀+0: first
  new letter's cell starts filling through red. t₀+30ms×n: subsequent
  new letters. t₀+300: cells at full ink; counters increment in step
  (SORTS SET += glyphs landed this heading; WORDS COMPOSED += words in
  the heading). Pangram beat (if applicable): +600ms rim cascade.
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest (unused letter) | Wood-tone cell, letter visible in `--wood-deep` | Same |
  | Inking | 300ms fill through red | Same |
  | Inked | `--ink` fill, letter in `--paper` | Same |
  | Hover | Cell tooltip-free: the header label line names the hovered letter and its count ("E — USED IN 4 HEADINGS") | n/a |
  | Focus | Map is not focusable as a whole; it is a progress readout | Same |
  | Scrolled-past | Ledger persists — ink never drains | Same |
  | Disabled / no-JS | Map renders empty (no headings have been "composed" without the engine) with label "THE CASE, AS USED — SET BY HAND TO READ" and counters hidden rather than fake | Same |

- **Content-merge.** The map's data is the page's real heading text,
  counted live. It cannot drift from the content because it is derived
  from it at the moment of composition — the anti-fake rule is
  structural, not editorial.
- **Failure fallback.** If the composition engine fails, §6.2/§6.3
  fallbacks fire and no letters ink; the map then shows the honest
  empty state above — never a pre-filled or scroll-faked map. Counters
  that cannot count are hidden, not zeroed (a printed "SORTS SET 0"
  would be a lie about work not done).
- **Reduced-motion variant.** Cells ink instantly (no fill animation);
  the pangram cascade becomes a static `--red` rim on the whole map.
  The ledger function is untouched.
- **Breakpoints (v2).** ≥1200px: full map + counters in the header.
  768–1199px: map only (counters move to the footer, §6.17). <768px:
  the map collapses to a 26-cell strip 6px tall under the header —
  cells still ink individually; counters in the footer.
- **Edge cases & failure modes (v2).** *Page with a pangram by
  accident:* the flourish is earned, let it fire. *Headings edited
  live (SPA route change):* the map resets per route — a new page is
  a new case, and the label states the page title's first heading as
  its starting census. *Letter used in a heading that was skipped
  (fast scroll):* §6.3's settle rule still counts it — the heading
  *was* composed, just quickly.
- **Accessibility spec (v2).** The map is `role="progressbar"` with
  `aria-valuemin 0`, `aria-valuemax 26`, `aria-valuenow` = letters
  used, and `aria-label` "Letters of the case used in this page's
  headings". Updates are not live-announced (a progressbar polled by
  the user, not a siren). Cell letters are real text, readable at
  200% zoom — the map scales with the header's rem sizing.
- **Performance budget & mobile variant.** 26 tiny fills, event-driven,
  zero per-frame cost. Mobile strip variant uses the same fills at 6px.
- **Tokens consumed (v2).** `--wood`, `--wood-deep`, `--ink`, `--red`,
  `--paper`, `--ease-door`, `--ink-fill` (300ms), `--stagger-map`
  (30ms), `--cell-map` (10px).

### 6.6 Compartment-door reveals

- **What & why.** Body blocks appear through a clip-path that opens
  like a compartment's front edge dropping — the block's bottom edge
  swings down (inset clip from bottom, 500ms) so the content is
  revealed as if taken *out of* its compartment. Every paragraph
  literally comes out of the case it belongs to. This is the theme's
  workhorse reveal: it carries all body copy, cards' text, and ledger
  rows that don't have a more specific entrance.
- **Structure.** Each revealable block sits inside its compartment
  block (§4) in the DOM, fully rendered. JS arms the pre-state only on
  blocks below the fold: `clip-path: inset(0 0 100% 0)` plus a 14px
  wood "door" bar rendered at the block's bottom edge (a pseudo-element
  with the divider treatment). On entry (IntersectionObserver, root
  margin −12% bottom), the clip animates to `inset(0 0 0% 0)` and the
  door bar rotates 8° and fades as it "drops". Content inside never
  transforms — only the clip moves, so text is never distorted.
- **Motion spec.** Trigger: block's top crosses 88% of viewport.
  Duration 500ms `--ease-door`; blocks in the same compartment region
  stagger 70ms in reading order, capped at 3 animating concurrently —
  the fourth and later blocks in a fast scroll appear already open
  (the printer doesn't perform for a visitor who isn't watching).
  Re-entry: doors never re-close; a revealed block stays revealed
  (scrolling back up shows an open case, which is correct — you don't
  un-take a letter from its box by looking away).
- **Choreography timeline (v2).** t₀ = trigger. t₀+0: clip starts
  opening from the bottom edge; door bar begins its drop. t₀+250:
  clip at ~78% open (easeOutCubic front-loads); door at full 8° tilt.
  t₀+500: clip removed entirely (set to `none` — a finished reveal
  leaves no clip on the element), door bar removed from layout.
  t₀+1200 watchdog: any block whose reveal stalled is force-opened
  and unclipped.
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest (below fold, armed) | Clipped shut, door bar visible at the compartment's edge | Same |
  | Opening | 500ms clip + door drop | Same, 420ms |
  | Open | No clip, no bar — plain content in its compartment | Same |
  | Hover | n/a (reveals are not interactive) | n/a |
  | Focus | A focusable element inside a shut block forces its door open instantly before focus lands | Same |
  | Scrolled-past | Open | Open |
  | Disabled / no-JS | No pre-state is ever set in HTML; all blocks stand open | Same |

- **Content-merge.** The door is the compartment's own front edge and
  the block is the compartment's contents — the reveal is the act of
  taking the content out of the box it lives in. Nothing overlays
  neighbouring content; the clip is confined to the block's own box.
- **Failure fallback.** Pre-states are JS-armed only, on below-fold
  blocks only, and every armed block carries the 1200ms watchdog plus
  an IO fallback timer. No-JS and JS-failure both yield a fully open
  page. This element is where the standing rule "no reveal may strand
  content" is enforced most strictly, because it touches the most
  content.
- **Reduced-motion variant.** Blocks appear whole (opacity 0→1 over
  120ms only if JS is present; otherwise simply present). No clip, no
  door.
- **Breakpoints (v2).** ≥1200px: 500ms, stagger 70ms. 768–1199px:
  460ms. <768px: 420ms, stagger 50ms, concurrency cap 2.
- **Edge cases & failure modes (v2).** *Block taller than the
  viewport:* the door opens when its top crosses 88% vh regardless of
  height; the clip reveals progressively as the visitor scrolls (the
  clip is on the block, the block is long — the bottom arrives when it
  arrives; a `max-height` trap is never set). *Content injected after
  load (CMS/SPA):* the arming observer watches the compartment regions,
  not a static node list; injected blocks arm on insertion if below
  fold, open immediately if in view. *Print:* all blocks print open;
  armed clips are stripped in print CSS.
- **Accessibility spec (v2).** Clipped content remains in the
  accessibility tree in reading order (clip-path does not remove it
  from AT, and focus-into-shut-block forces it open per the state
  matrix). Reveal is never announced. Contrast is unaffected — the
  door bar is decorative and `aria-hidden`.
- **Performance budget & mobile variant.** Clip-path animation on ≤3
  blocks concurrently; no layout writes (clip is compositor-friendly
  on block-level elements). Mobile: concurrency 2, duration 420ms.
- **Tokens consumed (v2).** `--ease-door`, `--door` (500ms),
  `--stagger-block` (70ms), `--wood`, `--wood-deep`, `--paper-deep`,
  `--watchdog-reveal` (1200ms).

### 6.7 The visitor word tray

- **What & why.** Clicking any compartment's sort sends a clone flying
  (FLIP, 650ms) to the footer composing stick, appending the letter to
  a word the visitor is building; a counter tallies "YOUR SORTS: n".
  The footer becomes the visitor's own typesetting, built from the
  page's inventory. It is the theme's handshake: the case was not a
  picture, it was a tool, and it works. The finished word can be
  "set" (the stick locks, the word is stamped into the footer's
  colophon line as "Set by a visitor: —") or cleared back into the
  case letter by letter.
- **Structure.** Every compartment sort in the hero case (and the
  mini-case in §6.10's navigation drawer) is a real `<button>` wrapping
  its glyph, labelled "Pick the letter e". The footer composing stick
  is a 64px-tall `--paper-bright` well with a wood base rail, holding
  the visitor's sorts as Fraunces glyphs on individual sort faces
  (28px). Picking clones the sort (the original stays — the case holds
  stock, §3 law 1 applies to visitors too: a letter can be picked at
  most as many times as its stated stock, default stock = its size
  class ×2: large 6, medium 4, small 2; a depleted letter's button
  disables with the label "E — OUT OF SORTS" — the printer's own term
  for an empty box, and the theme's favourite joke is a technical
  term). Space picks come from the quad compartment and insert a true
  gap. Backspace returns the last sort to its compartment (reverse
  FLIP); "CLEAR" returns all, staggered 40ms.
- **Motion spec.** Trigger: click/tap/keyboard activation on a sort
  button. Flight 650ms `--ease-sort` along a shallow arc (peak +30px),
  landing settle `--ease-settle` 150ms into the stick's next slot;
  the stick's existing sorts shuffle left 40ms each to make room only
  when the word wraps to a second line (words ≤14 sorts stay one
  line). Return flights 500ms. The pick also flashes the source
  compartment's rim `--red` 200ms — the case acknowledging the loan.
- **Choreography timeline (v2).** t₀ = pick. t₀+0: rim flash starts;
  clone lifts 6px. t₀+90: clone at arc peak. t₀+650: lands in stick;
  settle; counter increments ("YOUR SORTS: n" — counts sorts in the
  stick, read from the DOM, never a stored variable that can drift).
  t₀+700: if the word now spells a word in the page's own glossary
  (the build ships a small dictionary of the site's key terms), the
  stick's rail stamps it: letters deepen to full ink and a "SET"
  plaque lights — recognition, not a game reward.
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest (sort in case) | Glyph at rest in its compartment; button focusable | Same; targets ≥44px via compartment padding |
  | Hover | Sort lifts 6px, rim glows `--wood-lit` (§6.8's tilt permitting) | n/a |
  | Focus | 2px `--red` outline offset 2px + lift — keyboard picks are first-class | Same |
  | Active (picked) | Clone flies; source rim flashes | Same |
  | Depleted | Button disabled, label "OUT OF SORTS", glyph at 45% ink | Same |
  | Scrolled-past | The stick persists in the footer; picks remain available in the nav mini-case | Same |
  | Disabled / no-JS | Buttons are inert `<button>`s beside a printed line in the footer: "The tray is live when the press is running (JavaScript on)" — the case still reads as a case | Same |

- **Content-merge.** The word is built from the page's actual inventory,
  with real stock limits, and lands in the footer colophon — the
  visitor's typesetting joins the page's own apparatus. Nothing about
  it is a floating widget: the stick is the footer's first element and
  the case is the hero.
- **Failure fallback.** If FLIP fails mid-flight (element removed,
  route change), the letter is appended to the stick instantly without
  the flight — the *word* is the content; the flight is its courier.
  State lives in the DOM (the stick's children), so a loop crash loses
  animation, never letters.
- **Reduced-motion variant.** Picks append instantly (120ms ink
  deepen); returns likewise. Stock limits, counter, and the SET stamp
  all still work — the tool functions, the courier walks instead of
  flying.
- **Breakpoints (v2).** ≥1200px: picks from the hero case + nav
  mini-case. 768–1199px: same; stick glyph size 24px. <768px: picks
  from the drawer-row case (§4); flights are shorter (≤480ms) and the
  stick sticks to the viewport bottom while the footer is off-screen
  *only after the first pick* (before that, no sticky bar — the page
  does not nag).
- **Edge cases & failure modes (v2).** *Word longer than 14 sorts:*
  the stick wraps to a second line (max 28 sorts); at 28 the case
  buttons disable with the stick label "STICK FULL — SET IT OR CLEAR
  IT". *Visitor spells something profane:* it is their typesetting on
  their screen; nothing is transmitted or stored server-side; the SET
  stamp simply doesn't light for non-glossary words. *Persistence:*
  the word is session-only (sessionStorage) — a returning visitor
  starts with an empty stick and a full case, which is the correct
  workshop etiquette.
- **Accessibility spec (v2).** Buttons carry letter labels; the stick
  is a `role="status"` region whose text ("Your word so far: T Y P E")
  updates politely, letter-spaced for screen readers. Depleted and
  full states are conveyed in the button labels, not by colour alone.
  All picks are keyboard-operable in case reading order (the tab order
  *is* the alphabet — a small delight that costs nothing).
- **Performance budget & mobile variant.** One clone per pick, flights
  never concurrent (a pick during a flight queues 120ms or appends
  instantly if the queue exceeds 2). Mobile: flight ≤480ms, arc peak
  +16px.
- **Tokens consumed (v2).** `--ease-sort`, `--ease-settle`, `--red`,
  `--paper-bright`, `--wood`, `--flight-pick` (650ms), `--stick-h`
  (64px), `--stock-large` (6), `--stock-medium` (4), `--stock-small`
  (2), `--word-max` (28).

### 6.8 Case tilt carry

- **What & why.** On desktop, the whole hero case tilts a maximum of
  1° toward the pointer's quadrant with a slow 800ms ease, compartment
  shadows shifting opposite — the layout itself is the tactile object,
  and text inside tilts with its tray, never separately. One degree is
  the whole point: a tray on a workbench shifts under your hands by
  almost nothing, and almost-nothing is what makes it feel like wood
  instead of a screen effect.
- **Structure.** The hero case wrapper gets a `transform: perspective
  (1600px) rotateX/rotateY` driven by the shared loop from pointer
  position over the hero (quadrants computed from the case's centre).
  Compartment inset shadows are CSS variables (`--sh-x`, `--sh-y`)
  written by the same loop, moving opposite the tilt by up to 3px, so
  the compartments' depth sells the tray's movement. Body sections
  below the hero never tilt — the tray is the hero object; the page
  beneath is the bench it sits on.
- **Motion spec.** Trigger: pointer move over the hero (desktop,
  fine-pointer only). Tilt range ±1° on both axes, eased by the loop's
  lerp (0.06 for this channel — heavier than the standard 0.12; wood
  is slow) with an 800ms settle character. On pointer leave, the tray
  returns to level over 900ms. Tilt pauses while §6.1/§6.2 has glyphs
  in flight (their rects are read live, so tilt *could* coexist — but
  a moving tray under flying type reads as seasickness; the loop
  serialises: flights first, tilt resumes 300ms after the last
  landing).
- **Choreography timeline (v2).** Continuous: pointer enters quadrant
  → target tilt set → loop lerps tray over ~800ms → shadows counter-
  shift over the same span → pointer leaves → 900ms return to level.
  No discrete beats; the timeline is the lerp itself, and the spec's
  numbers are the lerp rate and the caps.
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Level tray, shadows centred | Level (no tilt channel exists) |
  | Hover (pointer over hero) | Tilting toward quadrant, ≤1° | n/a — coarse pointers never arm the channel |
  | Focus | Keyboard focus inside the case levels the tray (a reader aiming at a letter gets a still tray) | Same |
  | Active (flight in progress) | Tilt frozen at current angle, resumes after | n/a |
  | Scrolled-past | Hero off-screen: channel idle, tray level | Same |
  | Disabled / no-JS | Level tray (the only state HTML knows) | Same |

- **Content-merge.** The tilting object is the layout grid itself —
  compartments, sorts, and labels move as one physical tray because
  they are one element subtree. Nothing is tilted *over* content.
- **Failure fallback.** Transform on one wrapper; if the loop dies,
  the last written transform is cleared by the watchdog to `none` —
  a permanently 1°-tilted page would be a bug you can see from across
  the room.
- **Reduced-motion variant.** No tilt, no shadow shift. The tray is a
  tray, level on the bench.
- **Breakpoints (v2).** ≥1200px: full spec. 768–1199px: tilt cap 0.6°,
  shadow shift 2px (smaller tray, smaller gesture). <768px: channel
  does not exist (drawer rows scroll natively; tilting a scrolling
  row is a carnival ride).
- **Edge cases & failure modes (v2).** *Pointer at the case's exact
  centre:* dead zone of 40px radius — no jitter around level.
  *Window blur mid-tilt:* return-to-level fires on blur. *Text
  selection drag across the hero:* tilt freezes while the mouse is
  down (selecting type on a moving tray is a cruelty).
- **Accessibility spec (v2).** Tilt is pointer decoration with zero
  information content; it never moves a focus target by more than the
  1° geometry (≤3px at the tray's edge) and freezes on focus-within.
  Fully off for coarse pointers and reduced motion.
- **Performance budget & mobile variant.** One transform + two CSS
  variable writes per frame, only while the pointer is over the hero.
  No mobile variant (channel absent).
- **Tokens consumed (v2).** `--tilt-max` (1deg), `--tilt-lerp` (0.06),
  `--tilt-settle` (800ms), `--shadow-shift` (3px), `--paper`,
  `--wood-deep`.

### 6.9 Divider draw-in

- **What & why.** The case's red divider lines SVG-draw themselves
  (stroke-dashoffset, 700ms) when a new case region enters — the drawn
  lines are the actual grid borders of the content compartments, so
  the page's structure is *ruled in* as the visitor reaches it, the
  way a compositor rules a forme before locking it up.
- **Structure.** Each divider band (§4) carries an inline SVG line
  (2px, `--red`) laid over the wood band's centre, drawn via
  `stroke-dasharray` equal to its length. The wood band itself is
  always fully rendered (structure never waits for decoration); the
  red rule is the band's *scoring* — in a real case the divider lines
  a printer checks are the red-leaded strips between compartments.
  Draw direction alternates by region index (left→right, then
  right→left) following the reading serpentine of the case.
- **Motion spec.** Trigger: band's top crosses 85% of viewport.
  Duration 700ms `--ease-door`, one band at a time (bands queue 90ms
  apart if several enter together). The draw happens once per band
  per page load; scrolling back shows drawn rules.
- **Choreography timeline (v2).** t₀ = trigger. t₀+0: dash offset at
  full length. t₀+350: ~72% drawn (easeOutCubic front-loads). t₀+700:
  offset 0; the line is simply *there* — dash properties removed so
  the resting state has no animation residue.
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest (below fold) | Wood band present, red rule undrawn | Same |
  | Drawing | 700ms stroke draw | Same, 560ms |
  | Drawn | Plain red rule on wood | Same |
  | Hover | n/a | n/a |
  | Focus | n/a (decorative) | n/a |
  | Scrolled-past | Drawn | Drawn |
  | Disabled / no-JS | Rule renders fully drawn (SVG default state is drawn; JS sets the undrawn state) | Same |

- **Content-merge.** The line being drawn is the compartment border
  itself — structure arriving, not ornament appearing. A build where
  the red rule is a separate decorative stripe beside the real border
  has missed the element entirely.
- **Failure fallback.** The SVG's default state is fully drawn; JS
  arms the dash state only for below-fold bands, with the §6.6
  watchdog family (1200ms) forcing completion.
- **Reduced-motion variant.** Rules are simply present.
- **Breakpoints (v2).** All: same; <768px duration 560ms and bands in
  drawer rows draw horizontally per row on first row entry.
- **Edge cases & failure modes (v2).** *Band wider than the SVG's
  viewBox after resize:* the SVG uses `preserveAspectRatio="none"`
  with a vector-effect-free 2px stroke set in px via CSS — the rule
  is exactly as long as the band, always, because it is drawn in the
  band's own coordinate space. *Many bands entering at once (jump
  scroll):* all draw instantly (queue cap: >3 pending = all instant).
- **Accessibility spec (v2).** Purely decorative; the SVG is
  `aria-hidden`, `focusable="false"`. The compartment structure it
  marks is conveyed by the regions' labels (§4 plaques), not by the
  line.
- **Performance budget & mobile variant.** Stroke animation on ≤1
  band at a time; negligible. Mobile duration 560ms.
- **Tokens consumed (v2).** `--red`, `--wood`, `--ease-door`,
  `--draw-divider` (700ms), `--stagger-divider` (90ms).

### 6.10 Case-strip navigation (page family: navigation)

- **What & why.** Navigation is a shallow drawer pulled from the case:
  a horizontal strip under the header styled as the case's top row —
  each destination is a compartment containing its section's *initial
  sort* (the first letter, set large in Fraunces) beside its label in
  Space Grotesk. The current section's compartment is inked (its cell
  fills `--ink`, label in `--paper`); the strip also carries the
  case-map (§6.5) at its right end, so progress and wayfinding share
  one piece of furniture, as they do on a real case's labelled edge.
- **Structure.** A `<nav>` of compartment cells, each an `<a>` with a
  sort glyph + label; the current page's cell carries `aria-current`.
  A "FULL CASE" button at the strip's end opens the navigation drawer:
  a full mini-case (all 69 compartments at 28px) where letters that
  begin section names are live links and the rest are the working
  pick-stock for §6.7 — the drawer is both sitemap and toolbox.
- **Motion spec.** Strip cells: hover lifts the cell's sort 6px
  (`--ease-lift`, 160ms) with a `--wood-lit` rim; the inked current
  cell never lifts (it is set, not loose). Drawer: opens by sliding
  down from the header like a pulled drawer (360ms `--ease-door`) with
  its compartments' divider rules drawing in miniature (§6.9 grammar,
  300ms, staggered by row). Route change: the destination's cell inks
  over 300ms as the old cell drains to wood — ink moves house, it does
  not blink.
- **Choreography timeline (v2).** Drawer open: t₀ click → t₀+360
  drawer seated → rows draw t₀+90×row → focus lands on the drawer's
  first link at t₀+360. Cell ink transfer on navigation: old cell
  drains 0–200ms, new cell fills 100–300ms (overlap, like passes of a
  press).
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Cells at rest; current cell inked | Same; strip scrolls horizontally |
  | Hover | Sort lifts 6px, rim glows | n/a |
  | Focus | Lift + 2px `--red` outline on the cell | Same |
  | Active | Cell presses 2px into the tray (shadow collapse 120ms) | Same |
  | Scrolled-past | Strip is in the sticky header; ink state persists | Same |
  | Disabled | A destination with no page is absent — never a greyed cell | Same |

- **Content-merge.** The nav's compartments are the same case the hero
  uses — same sizes for the initial letters (an 'E' section gets the
  big cell), same stock. The drawer doubles as §6.7's pick source away
  from the hero, so navigation furniture does two real jobs.
- **Failure fallback.** Plain horizontal link list with the current
  page marked; the drawer degrades to a `<details>`-style disclosure
  that works without JS (button + hidden panel in HTML, JS only adds
  the slide).
- **Reduced-motion variant.** Drawer opens instantly; ink transfers
  are instant; no lifts.
- **Breakpoints (v2).** ≥1200px: full strip + case-map + counters.
  768–1199px: strip without counters (they move to §6.17). <768px:
  strip shows logo-cell + current-cell + "FULL CASE" button; the
  drawer becomes the primary nav, opening as a full-screen case.
- **Edge cases & failure modes (v2).** *More than 8 sections:* the
  strip shows the first-level sections only; sub-sections live in the
  drawer under their initial's row. *Two sections sharing an initial:*
  both cells show the same sort — the labels disambiguate, exactly as
  two 'S' compartments would in a real case (the case allows it; so
  do we). *Long labels:* truncate at 14ch in the strip, full in the
  drawer and in `aria-label`.
- **Accessibility spec (v2).** Real `<nav aria-label="Sections of the
  case">`; `aria-current="page"` on the inked cell (ink alone never
  carries currentness). Drawer button is `aria-expanded`; Esc closes
  and returns focus. Targets ≥44px on touch (cell padding, not glyph
  size, provides it).
- **Performance budget & mobile variant.** Drawer DOM is built once,
  hidden with `visibility` (not re-created per open). Mobile drawer is
  the same DOM at full-screen size.
- **Tokens consumed (v2).** `--ink`, `--paper`, `--wood`, `--wood-lit`,
  `--red`, `--ease-lift`, `--ease-door`, `--drawer-open` (360ms),
  `--ink-transfer` (300ms).

### 6.11 Compartment cards (page family: cards)

- **What & why.** Listing and related-content cards are compartments:
  each card is one wide cell with wood walls, a label plaque naming
  its contents, the item's image as a printer's block, its title set
  in Fraunces, and its standfirst in Space Grotesk. A grid of cards is
  a *sub-case* — a region of the tray given over to one kind of
  content — so a listing page reads as the case reorganised, not a
  new design language arriving mid-site.
- **Structure.** `<article>` cells in a grid that borrows §4's size
  classes: a featured card spans a Large cell (2×2), standard cards
  Medium (2×1), compact items Small (1×1, title + plaque only). The
  image block sits in the cell at type height with a 3px wood mount;
  the whole card is one link (stretched over the title) unless it
  carries a second action.
- **Motion spec.** Entry: §6.6 compartment doors at card scale.
  Image: scale-in-frame — the block scales 1.06→1 scrubbed as the
  card crosses the viewport centre band (shared loop), the only
  scroll-scrub below the hero. Hover: the card's front wall shadow
  deepens and the title's first sort lifts 3px (a nod to §6.2 at
  furniture scale — the title is *almost* picked up). Active: press
  2px. The featured card's image additionally parallaxes within its
  mount by 6px (the block is loose in its cell by exactly that much).
- **Choreography timeline (v2).** Entry per §6.6. Hover: t₀ enter →
  shadow deepens 0–180ms, sort lift at t₀+60 (120ms) → leave reverses
  over 240ms. Centre-band scrub is continuous (no beats).
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Cell at rest, image at 1.06 if below centre band | Same |
  | Hover | Wall shadow deepens; first sort lifts 3px | n/a |
  | Focus | Same as hover + focus ring on the title link | Same |
  | Active | 2px press | Tap: straight to §6.16 transition |
  | Scrolled-past | Image settled at 1.0 above the band, returns toward 1.06 below it (symmetric scrub) | Same |
  | Disabled | A card for unavailable content becomes an *empty compartment* (§6.18) with a plaque explaining — never a greyed card | Same |

- **Content-merge.** Every part of the card is the item it lists, and
  its size class is its editorial weight — featured items literally
  get the big box. The image treatment (block in a mount) is the
  theme's way of holding a picture, not a filter applied to it.
- **Failure fallback.** Static cells, image at scale 1 — the no-JS
  card is the finished card.
- **Reduced-motion variant.** No scrub, no lift: hover deepens the
  wall shadow only; images at scale 1.
- **Breakpoints (v2).** ≥1200px: mixed spans per §4 classes.
  768–1199px: two-up uniform Medium. <768px: one-up; compact cards
  join the flow as full-width Small rows; image scrub range 1.03→1.
- **Edge cases & failure modes (v2).** *Missing image:* the cell
  holds a *sort block* instead — a large Fraunces ampersand block,
  the printer's ornament — never a grey box or a silent stock photo.
  *Title longer than the cell:* clamps at 2 lines (Large/Medium) or
  1 line (Small) with the full title in the link's accessible name.
  *Odd card counts:* the last row's empty cells render as genuine
  empty compartments (§6.18) so the sub-case never shows a broken
  grid edge.
- **Accessibility spec (v2).** One link per card (the title), image
  `alt=""` when the title names the item, real alt when the image is
  the content. Focus ring 2px `--red` offset 3px, visible against
  both paper and wood.
- **Performance budget & mobile variant.** Image scrub tracked only
  for cards within ±1 viewport, cap 6 concurrent. Mobile: scrub range
  narrows, featured parallax off.
- **Tokens consumed (v2).** `--wood`, `--wood-deep`, `--paper`,
  `--paper-deep`, `--ink`, `--red`, `--ease-lift`, `--scale-block`
  (1.06), `--lift-sort-sm` (3px).

### 6.12 The composing-stick form (page family: forms / conversion)

- **What & why.** The conversion form is a composing stick: the long
  metal hand-tool a compositor fills line by line. Fields are set one
  line at a time into the stick — label as a pencilled plaque, input
  as a ruled line in the stick's well — and submitting is *locking up
  the forme*: the stick's lines are squared, a wedge (quoin) taps in,
  and the form is stamped with a job number. Conversion in this theme
  is the visitor setting their own details in type, which is why the
  form's honesty rules are strict: no pre-ticked boxes (a compositor
  sets only what you hand him), no hidden fields.
- **Structure.** A `<form>` inside a wide compartment: a stick well
  (`--paper-bright`, wood base rail, 64px row rhythm §4) holding up to
  5 field-lines; each line = plaque label + bottom-ruled input (2px
  `--ink` rule, Fraunces for display fields like a name, Space Grotesk
  for data fields). The submit is a wood plaque button "LOCK IT UP —
  [action]" (e.g. "LOCK IT UP — SEND THE PROOF"). Success replaces the
  stick with the locked forme: the visitor's entries re-set as
  composed lines, a job number ("JOB Nº 214 — SET FROM YOUR DETAILS")
  stamped in `--red`, and the line "Your details, set in type. Nothing
  else was taken." when that is true.
- **Motion spec.** Field focus: the line's rule thickens 2→3px and a
  sort of the field's initial letter slides into the stick's left
  margin (200ms `--ease-lift`) — the compositor has picked up the
  first letter of your answer. Error: the line's rule turns
  `--red-deep`, the offending sort *pieds* — tips 12° and slides 6px
  out of line (180ms) — and the error message sets itself beneath the
  line letter-spaced in the error voice (§12), never as a popup.
  Submit: lines square up (each shifts to flush left over 120ms,
  staggered 40ms), the quoin wedge draws in from the right (§6.9
  grammar, 300ms), the job stamp lands (scale 1.3→1, 160ms), total
  ≤700ms before the confirmation state.
- **Choreography timeline (v2).** Submit t₀: t₀+0 lines begin
  squaring (40ms stagger). t₀+280: quoin draws. t₀+580: stamp lands.
  t₀+700: confirmation apparatus (job number, what-happens-next line)
  fades in; focus moves to the confirmation heading.
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Ruled lines in the stick well | Same |
  | Hover (field) | Rule warms to `--wood` tone | n/a |
  | Focus | Rule 3px, initial sort slides in | Same |
  | Active (submit) | Squaring + quoin + stamp sequence | Same |
  | Error | Pied sort, red-deep rule, set error line beneath | Same |
  | Disabled | A form that cannot submit (e.g. list closed) renders as an empty stick with a plaque: why, and the alternative | Same |
  | Scrolled-past | State persists; no re-animation | Same |

- **Content-merge.** The stick holds the visitor's actual entries;
  the locked forme *is* the confirmation — there is no separate
  success illustration. The job number is the server's real reference
  or a locally generated sequential number labelled as local.
- **Failure fallback.** A plain, fully usable form: stick styling is
  CSS on a standard form; without JS every behaviour (focus, error,
  submit) is native, errors come from the server rendered in the same
  lines. A failed submission never clears the visitor's entries —
  pied type is re-set, not swept away.
- **Reduced-motion variant.** No squaring, no stamp scale: the quoin
  and stamp appear; pied sorts tip without sliding. Errors identical
  (they are content, not motion).
- **Breakpoints (v2).** ≥1200px: stick up to 640px wide inside its
  compartment, two short fields may share a line. 768–1199px: one
  field per line. <768px: full-width stick, 56px rows, submit plaque
  full width.
- **Edge cases & failure modes (v2).** *Long forms (>5 fields):* the
  stick is filled in two passes — pass 1 lines lock and slide up into
  a "set lines" stack above the well (miniature, legible), pass 2
  fills the well; a form needing a third pass is two forms and should
  be split. *Autofill:* autofilled lines get their initial sort
  pre-slid (the compositor acknowledges machine help honestly).
  *Server 500:* the forme unlocks (stamp fades), entries intact, and
  the error line reads in the §12 voice with the retry plaque.
- **Accessibility spec (v2).** Real `<label>`s (the plaques *are* the
  labels, associated by `for`), errors linked by `aria-describedby`,
  error summary at the stick's head on submit failure with focus
  moved to it. The stamp and quoin are `aria-hidden`. Targets ≥44px;
  the ruled inputs are 48px tall at every breakpoint.
- **Performance budget & mobile variant.** All motion is ≤8 small
  transforms; the form has no scroll-driven behaviour. Mobile: stamp
  scale reduces (1.15→1).
- **Tokens consumed (v2).** `--paper-bright`, `--ink`, `--red`,
  `--red-deep`, `--wood`, `--ease-lift`, `--ease-door`, `--stick-h`
  (64px), `--square-line` (120ms), `--stamp` (160ms).

### 6.13 The frequency ledger (page family: data table)

- **What & why.** Data tables are ledgers ruled like a case plan: each
  row is a shallow compartment, its first cell holding the row's key
  as a sort, its figures in tabular Space Grotesk. The ledger's party
  trick is earned: a "BY THE CASE" view re-sorts the table's rows into
  compartment size classes by their key letter's frequency — the data
  is literally filed into the case. It exists because every real site
  in this theme eventually shows a table, and a table that arrives in
  a foreign design language breaks the workshop spell.
- **Structure.** A semantic `<table>` (never divs) inside a wide
  compartment; header row as a wood band with `--paper` plaque labels;
  row height 52px; zebra by `--paper-deep` on alternate rows (the
  tray's floor shadow, not a grey). Sortable columns are plaques with
  a small sort glyph showing direction (an 'A' sort upright = ascending,
  inverted = descending — the glyph is the indicator, not an arrow
  icon).
- **Motion spec.** Entry: rows open via §6.6 doors at row scale (300ms,
  stagger 30ms, cap 8 animating; a 40-row ledger never performs all
  40). Sort: rows FLIP to their new order (450ms `--ease-sort`,
  stagger 12ms, cap 20 rows animating — beyond that, instant reorder
  with a 120ms ink flash on the moved keys). "BY THE CASE" toggle:
  rows first pied gently (tilt ±1.5°, 150ms) then fly to their size
  classes (600ms) — the one theatrical moment a table is allowed.
- **Choreography timeline (v2).** Sort t₀: header sort glyph flips
  (120ms) → rows FLIP t₀+60, 12ms stagger → t₀+510 settled; the
  caption line updates: "Filed by frequency — E's row is the big box"
  or "Filed A–Z".
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Ruled rows, tabular figures | Same; table scrolls horizontally inside its compartment |
  | Hover (row) | Row's key sort lifts 2px | n/a |
  | Focus | Cell focus visible (2px red outline inset) | Same |
  | Active (sorting) | FLIP reorder | Same |
  | Scrolled-past | Rows open, static | Same |
  | Disabled | An empty ledger renders §6.18's empty compartment with the ledger's own empty voice (§12) | Same |

- **Content-merge.** The rows are the data; the case filing is a real
  re-ordering of that data by a stated rule. Nothing is drawn on top.
- **Failure fallback.** A plain, correct, sortable-by-server table.
  All enhancements are client-side re-orderings of real DOM rows.
- **Reduced-motion variant.** Sorts are instant with the ink flash;
  "BY THE CASE" switches order instantly; entry doors off.
- **Breakpoints (v2).** ≥1200px: full columns. 768–1199px: lowest-
  priority column folds into a row-expansion (a compartment drawer,
  §6.15). <768px: horizontal scroll inside the compartment with the
  key column pinned — the tray slides, the labels stay.
- **Edge cases & failure modes (v2).** *>40 rows:* paginate by
  compartment regions ("LOWER CASE A–M / N–Z") rather than infinite
  scroll — a ledger has pages. *Figures that don't fit:* tabular
  figures never shrink; the cell scrolls its own overflow, stated in
  the build (shrinking data is falsifying data).
- **Accessibility spec (v2).** Real table semantics, `aria-sort` on
  sortable headers, scope attributes set. The BY THE CASE order is
  announced via the caption line (a polite status), because a visual
  re-sort a screen reader can't perceive must still be a stated fact.
- **Performance budget & mobile variant.** FLIP capped at 20 rows;
  beyond that, instant. Mobile: FLIP cap 10.
- **Tokens consumed (v2).** `--paper`, `--paper-deep`, `--wood`,
  `--ink`, `--red`, `--ease-sort`, `--ease-door`, `--flip-row`
  (450ms), `--row-h` (52px).

### 6.14 Pied-type notices (page family: alerts / toasts)

- **What & why.** "Pied type" is the printer's disaster: a forme
  dropped, its sorts in a heap. This theme's alerts are exactly that —
  a notice arrives as a small heap of pied sorts at the compartment's
  edge which the apprentice (the interface) visibly re-sets into the
  message line. Errors pied and re-set; confirmations arrive already
  set with a stamp. There are no toasts: a toast is a notification
  from an operating system, and this site has a workshop, not an OS.
  Notices live *in* the compartment they concern.
- **Structure.** An inline region at the head of the relevant
  compartment: a 36px line whose left end holds a 28px sort showing
  the notice kind (! for error, ✓-equivalent — the theme uses a set
  '¶' pilcrow for information and a stamped job tick for success —
  never emoji). Error text in `--red-deep`, information in `--ink`,
  success in `--ink` with a `--red` stamp glyph.
- **Motion spec.** Error arrival: the line's sorts pied — each glyph
  clone tips to a random ±10° and drops 4px (150ms `--ease-rain`) —
  then re-sets in reading order (300ms, 24ms stagger, `--ease-settle`
  landings). Success: no pied; the line slides in via §6.6 door at
  300ms and the tick stamps (160ms). Dismissal: the line's sorts are
  picked back into the case (reverse §6.7 flight, 400ms) — notices
  leave by being put away, not by fading like ghosts.
- **Choreography timeline (v2).** Error t₀: pied drop t₀+0–150 →
  still heap 120ms (the disaster is *seen*) → re-set t₀+270–570 →
  line readable, focus/announcement at t₀+570.
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | No notice region (absent, not hidden) | Same |
  | Arriving (error) | Pied → re-set sequence | Same |
  | Arriving (success/info) | Door slide + stamp | Same |
  | Hover | n/a | n/a |
  | Focus | Dismiss button (a real "PUT IT AWAY" plaque) focusable when present | Same |
  | Scrolled-past | Notices persist until dismissed or their cause resolves | Same |
  | Disabled / no-JS | Notices render fully set, server-side | Same |

- **Content-merge.** The notice is typeset from the same sorts as
  everything else and sits inside the compartment whose content it
  concerns — a form error appears in the form's stick (§6.12 uses
  this element's grammar), a ledger notice in the ledger.
- **Failure fallback.** Static set line, server-rendered. The pied
  sequence is a JS retelling of an arrival, never the arrival itself.
- **Reduced-motion variant.** Notices appear fully set (120ms fade);
  dismissal is instant removal. The *wording* carries the urgency,
  not the tumble.
- **Breakpoints (v2).** Identical grammar at all sizes; on <768px the
  heap drops 3px and tips ±7° (smaller tray, smaller disaster).
- **Edge cases & failure modes (v2).** *Two errors at once:* they
  queue 200ms apart — simultaneous pied heaps read as one accident.
  *Error text longer than the line:* wraps to a second set line; the
  pied sequence applies to the first line only. *Auto-dismiss:* never
  for errors; successes may be put away by the system after 6s only
  if they carry no reference number the visitor needs.
- **Accessibility spec (v2).** Errors use `role="alert"` (announced
  once, after the re-set completes — announcing mid-tumble would read
  a heap); successes use `role="status"`. Dismiss targets ≥44px.
  Kind is conveyed by the sort glyph *and* the first word of the text
  ("Error —", "Set —"), never by colour alone.
- **Performance budget & mobile variant.** ≤24 glyph clones per
  notice; two notices animating at once is the cap. Mobile: heap
  geometry reduced as above.
- **Tokens consumed (v2).** `--red-deep`, `--ink`, `--red`,
  `--ease-rain`, `--ease-settle`, `--pied` (150ms), `--reset-line`
  (300ms), `--stamp` (160ms).

### 6.15 Drawer compartments (page family: accordion / FAQ)

- **What & why.** Accordions are drawers under the case: each question
  is a shallow drawer with a wood front and a plaque; opening it pulls
  the drawer toward the visitor and the answer — set on a paper slip
  inside — comes with it. It belongs because FAQ content in this theme
  is *stored* material: the visitor is looking something up in the
  cabinet the workshop keeps its references in.
- **Structure.** A stack of drawer fronts (56px) in a wide
  compartment; each is a `<button>` (the question, Space Grotesk 500)
  with a brass-less wood pull (a routed slot, pure CSS). The panel is
  the drawer's interior: `--paper-deep` floor, answer in body type,
  max-height animated via grid-template-rows (0fr→1fr) so the drawer
  opens at its content's true size. One drawer open at a time per
  stack (a cabinet with every drawer open is a spill waiting to
  happen) — except FAQ stacks flagged `data-multi`, where the build
  states why.
- **Motion spec.** Open: 380ms `--ease-door` — the front translates
  down 6px and the interior reveals from the top (the drawer tips
  toward you); the pull's shadow deepens. Close: 300ms, front rises
  back. The previously open drawer closes in the same beat (its 300ms
  overlaps the new drawer's 380ms by 100ms — hands overlap on a real
  cabinet).
- **Choreography timeline (v2).** t₀ click: old drawer starts closing
  (if any). t₀+100: new drawer front drops. t₀+480: new drawer fully
  open; focus stays on its button (content is read by scrolling, not
  by focus theft).
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest (closed) | Wood front, plaque question | Same |
  | Hover | Front warms (`--wood-lit` edge brightens) | n/a |
  | Focus | Red outline on the front | Same |
  | Active (opening) | 380ms pull | Same |
  | Open | Interior visible; front at dropped position | Same |
  | Scrolled-past | Open state persists | Same |
  | Disabled | A drawer whose answer is unavailable is absent from the stack | Same |

- **Content-merge.** The answer is physically inside the thing you
  opened; the drawer front carries the question in the same type the
  answer is set in. No iconography beyond the pull slot.
- **Failure fallback.** Buttons + panels with the panel visible by
  default in HTML and hidden only by JS arming (`hidden` attribute
  set by JS, removed by the watchdog if the engine fails) — a no-JS
  page shows an open cabinet with all answers readable.
- **Reduced-motion variant.** Open/close are 120ms fades of the
  interior; fronts do not translate.
- **Breakpoints (v2).** ≥1200px: drawers at 640px measure inside
  their compartment. <768px: fronts 52px, question truncates at 2
  lines rather than shrinking type.
- **Edge cases & failure modes (v2).** *Answer longer than ~40
  lines:* the drawer is the wrong furniture — split the answer into
  two drawers or promote it to a compartment block; the spec caps
  drawer content at 600px open height, beyond which the panel gets
  its own internal scroll, stated in the build. *Deep link to a
  drawer:* opens on load, instantly, scrolled into view by the
  browser's anchor — no animation for a visitor who arrived with a
  purpose.
- **Accessibility spec (v2).** Button + `aria-expanded` +
  `aria-controls`; panel `role="region"` labelled by the button.
  Keyboard: standard accordion pattern, arrow keys optional, Enter/
  Space native. The open state is never conveyed by shadow alone —
  the front's dropped position plus `aria-expanded` carry it.
- **Performance budget & mobile variant.** Grid-rows animation on
  one drawer at a time; no other cost. No mobile change beyond front
  height.
- **Tokens consumed (v2).** `--wood`, `--wood-lit`, `--wood-deep`,
  `--paper-deep`, `--ink`, `--red`, `--ease-door`, `--drawer-pull`
  (380ms), `--drawer-front` (56px).

### 6.16 Sort skeleton + case-lid transition (page family: loader / transition)

- **What & why.** Two state-change rituals sharing one material.
  **Loading** shows the compartment with its sorts *face-down*: bone-
  pale blank sort backs in the cell shapes of the content to come,
  which flip face-up (rotateY, staggered by frequency order) as real
  content lands — the page is being set, and you can see the setter's
  progress. **Navigation** closes the case-lid: a wood lid slides
  over the viewport, the route swaps beneath it, the lid lifts on a
  freshly sorted page. A spinner would be a machine part in a hand
  workshop; a blank sort is this world's honest "not yet".
- **Structure.** Skeleton: the real compartment markup with a
  `.is-setting` class — text replaced by sort-back blocks (rounded
  2px, `--paper-deep` with a 1px `--wood` keyline) at the content's
  true sizes; layout never shifts because the blocks *are* the
  layout's placeholders at real dimensions. Lid: a fixed full-
  viewport wood panel (grain gradient, one red rule at its lower
  third, a small plaque reading the destination's name) parked above
  the viewport.
- **Motion spec.** Skeleton flip: per block, rotateY 90°→0 over
  260ms `--ease-settle`, staggered in the compartment's letter-
  frequency order (the e-block flips first — the setter reaches for
  e first, always), content crossfading in during the flip's second
  half. Hard cap: any block still face-down at 1200ms flips instantly
  or, if content has failed, resolves into §6.14's notice grammar.
  Lid: 420ms `--ease-door` down, swap at full cover, 420ms up; the
  incoming page arrives *set* (its §6.6 doors do not re-run after a
  lid transition — a turned page is a finished page).
- **Choreography timeline (v2).** Lid t₀ = internal link activation:
  t₀+0 lid descends → t₀+420 full cover, route swaps, scroll resets →
  t₀+840 lid lifted, destination's masthead plaque already readable
  during the lift's last 100ms. Skeleton per block: t₀ = content
  landed → flip 260ms → content at full ink by t₀+260.
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Loading (skeleton) | Face-down sort backs at true sizes | Same |
  | Resolving | Frequency-order flips | Same |
  | Loaded | Normal compartment behaviour | Same |
  | Transitioning (lid) | 840ms total, pointer locked out | 720ms total |
  | Hover | Lid has no hover state; links keep §6.10 hover | n/a |
  | Focus | Keyboard-activated links fire the same lid; focus lands on the destination H1 at lift | Same |
  | Disabled / no-JS | No skeletons rendered unresolved; plain navigation | Same |

- **Content-merge.** The skeleton is the compartment's own unset
  self; the lid is the case's own lid. Both rituals are performed by
  the furniture the visitor has already met.
- **Failure fallback.** Skeletons exist only inside client fetches
  that own their 1200ms watchdog; server-rendered pages ship set.
  The lid enhances link clicks it can intercept and never breaks one
  it can't (modified clicks, new tab, external links bypass it
  entirely).
- **Reduced-motion variant.** Skeleton blocks are plain `--paper-deep`
  with a 120ms fade to content. Lid: no slide — instant navigation
  with the destination plaque flashing in the header for 600ms.
- **Breakpoints (v2).** ≥1200px: full spec. <768px: lid 360ms each
  way, its red rule and plaque kept (the ritual compresses, the
  furniture doesn't change).
- **Edge cases & failure modes (v2).** *Slow destination:* the lid
  holds at full cover with its plaque updating to the §12 waiting
  line ("Setting the next page — the e's are done, the z's are
  travelling") for up to 3s, then retreats (250ms) and the browser's
  native load proceeds — the theme never traps a visitor under a
  lid. *Content error in a skeleton block:* resolves to §6.14's
  pied notice inside that compartment. *Prefetch:* hovered internal
  links may prefetch; the lid still runs its full measure — the
  ritual is the point, not the wait.
- **Accessibility spec (v2).** During a lid transition the outgoing
  page is `inert` from t₀ and the destination is live at lift with
  focus on its H1 (`tabindex="-1"`) and a polite announcement
  "Turned to: [page]". Skeleton regions carry `aria-busy` until
  resolved. The lid is skipped for reduced-motion and for
  router-managed focus.
- **Performance budget & mobile variant.** One transform (lid) and
  per-block rotateY on transform-only layers; skeleton blocks are
  pure CSS. Mobile: lid timing as above; skeleton flips cap 12
  concurrent.
- **Tokens consumed (v2).** `--wood`, `--wood-deep`, `--red`,
  `--paper-deep`, `--ease-door`, `--ease-settle`, `--lid` (420ms),
  `--flip-sort` (260ms), `--fallback-set` (1200ms).

### 6.17 The case bottom (page family: footer)

- **What & why.** The footer is the bottom of the case: the composing
  stick (§6.7) sits at its head, beneath it the colophon is set as a
  printer's imprint — publisher, place, the case's own statistics
  (SORTS SET and WORDS COMPOSED for this page, read from §6.5's
  counters), and the visitor's set word stamped into the imprint
  line when they made one. A footer in this theme is not a sitemap
  with a logo; it is the imprint page every real book ends with.
- **Structure.** A `--wood-deep` ground band: stick well first, then
  three compartment columns (Imprint / The Case — nav repeated as
  compartments / Stock — contact and legal as set lines), then the
  imprint line itself in 12px Space Grotesk: "Set from the case of
  [site] · [n] sorts set on this page · Your word: [word or '— not
  yet set']".
- **Motion spec.** Entry: the footer's divider draws (§6.9) as it
  enters; the stick's sorts, if the visitor set a word, stamp in
  sequence (80ms stagger, `--ease-settle`) when the footer first
  enters — the word is *printed* at the bottom of its page. Counters
  in the imprint count up to their true values over 600ms when the
  imprint line enters (they count real events from the session —
  §6.5's ledger — so the count is short and honest).
- **Choreography timeline (v2).** t₀ = footer enters: divider draws
  0–700ms → stick word stamps t₀+300, 80ms/sort → imprint counters
  run t₀+500–1100 → still.
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Imprint set, counters at true values | Same |
  | Hover (stick sort) | Sort lifts 3px (it remembers being picked) | n/a |
  | Focus | Footer links carry the standard red ring | Same |
  | Active | n/a | n/a |
  | Scrolled-past | Final state persists | Same |
  | Disabled / no-JS | Imprint prints with counters omitted (not zeroed — §6.5's honesty rule) and the stick replaced by its printed line | Same |

- **Content-merge.** Every number in the imprint was counted from
  this page's real events; the visitor's word is their own work,
  given the imprint's place of honour. The footer *reports* the page
  rather than decorating its end.
- **Failure fallback.** Static imprint on `--wood-deep`; the stick
  degrades per §6.7.
- **Reduced-motion variant.** No stamping sequence; the word stands
  set; counters show final values.
- **Breakpoints (v2).** ≥1200px: three columns. 768–1199px: two
  columns, imprint full width below. <768px: one column; the stick
  stays first (the visitor's work outranks the sitemap).
- **Edge cases & failure modes (v2).** *No word set:* the imprint
  line reads "Your word: — the stick is above, the case is open" —
  an invitation, not a blank. *Counters from a page where composition
  failed:* omitted, per the honesty rule.
- **Accessibility spec (v2).** A real `<footer>` with labelled nav;
  the imprint is plain text in reading order. The stick's status
  region (§6.7) is not duplicated here.
- **Performance budget & mobile variant.** Entry animations are
  one-shot transforms on ≤28 sorts. No mobile change beyond columns.
- **Tokens consumed (v2).** `--wood-deep`, `--paper`, `--red`,
  `--ease-settle`, `--ease-door`, `--stamp-word` (80ms stagger),
  `--count-imprint` (600ms).

### 6.18 The empty compartment (page family: empty states / 404)

- **What & why.** Every case has a compartment that is empty — and in
  a printer's shop an empty compartment is information: either the
  sort is *out being set* (it exists, it's elsewhere) or it was
  *never cast* (it doesn't exist). The theme's empty states and 404
  honour that distinction, which most sites blur: a page not yet
  published shows a compartment with a pencilled plaque "OUT BEING
  SET — BACK SOON"; a page that never existed shows a bare
  compartment, dust-floor visible, plaque "NEVER CAST — NO SUCH
  SORT", with the nearest real compartments (closest matching pages)
  offered as live cells beside it.
- **Structure.** One Large compartment centred in a quiet region of
  tray floor: interior `--paper-deep` with a faint dust gradient,
  plaque label, one line of §12-voice copy, and up to three
  neighbouring live compartments (real links, §6.11 card grammar at
  Small size). For in-page empty states (empty ledger, empty
  search), the same compartment at Medium size inside the region that
  is empty.
- **Motion spec.** Entry: the compartment's door (§6.6) opens onto
  emptiness — 500ms — and one beat later (200ms) a single sort of the
  region's initial letter hops *out* of a neighbouring compartment,
  looks in (pause 300ms at the empty cell's rim), and hops back
  (§6.4 grammar): the case checking its own inventory. That is the
  only motion; an empty page that performs is mocking the visitor.
- **Choreography timeline (v2).** t₀ = region enters: door 0–500ms →
  neighbour sort lifts t₀+700 → rim pause t₀+820–1120 → returns
  t₀+1240 → still.
- **State matrix (v2).**

  | State | Desktop | Touch |
  |---|---|---|
  | Rest | Bare compartment, plaque, neighbours | Same |
  | Hover (neighbour cell) | Standard §6.11 hover | n/a |
  | Focus | Neighbour links focusable, red ring | Same |
  | Active | n/a | n/a |
  | Scrolled-past | Still | Still |
  | Disabled / no-JS | Static compartment, neighbours as plain links, no hop | Same |

- **Content-merge.** The emptiness is the content — the compartment
  is empty *because* the thing is missing, and its plaque states
  which kind of missing it is. The neighbours are real pages.
- **Failure fallback.** Static by construction; the hop is a clone
  and its absence changes nothing.
- **Reduced-motion variant.** No hop. The compartment stands open.
- **Breakpoints (v2).** All sizes: same composition, compartment at
  min(480px, 90vw).
- **Edge cases & failure modes (v2).** *Search with zero results:*
  the plaque reads "NOT IN THIS CASE" and the search term's first
  letter's compartment is shown *with its sort present* — "the
  letter exists; the word isn't set yet" — plus the closest matches.
  *A region that is empty because of an error:* never this element —
  errors use §6.14; an empty compartment must never launder a failure
  into a shrug.
- **Accessibility spec (v2).** The 404 page's H1 is the plaque's
  message in real text ("Never cast — no such page"); neighbours are
  a labelled list of links. The hop is `aria-hidden`.
- **Performance budget & mobile variant.** One clone hop; negligible.
- **Tokens consumed (v2).** `--paper-deep`, `--wood`, `--ink`,
  `--ink-soft`, `--ease-door`, `--ease-settle`, `--hop` (120ms).

---

## 7. Page application map

- **Home.** The full performance: hero case with spill (§6.1),
  composition (§6.2), rain boundaries (§6.3) between the 3–5 sections,
  compartment cards (§6.11) for featured content, the stick form
  (§6.12) if the page converts, case bottom (§6.17). The home page is
  the only page that gets the spill — a returning interior page that
  re-spills is a shop that tidies by throwing things.
- **Listing / index.** No hero case; the sub-case of cards (§6.11) is
  the page. A shallow case strip (one row: the alphabet as filter —
  clicking a letter files the listing to items under that initial,
  §6.13's BY THE CASE grammar) sits above the grid. Rain boundaries
  are off; doors (§6.6) carry all reveals.
- **Detail / article.** The article is one wide compartment; its H1
  composes once on entry (§6.2 grammar, unpinned, ≤2.8s); pull-quotes
  are set as Large compartments interrupting the measure; the ledger
  (§6.13) serves any data; the footer stick invites the reader to set
  the article's key word (the glossary word is pre-suggested on the
  stick's plaque: "Try setting: [keyword]").
- **About / studio.** The case is photographed, not simulated: image
  blocks (§6.11) of the real workshop/team; the frequency ledger
  becomes the studio's own census ("letters we set this year" — real
  job counts or the table does not ship).
- **Contact / signup / checkout-equivalent.** The composing-stick form
  (§6.12) is the whole page's centre; pied notices (§6.14) handle its
  errors; no rain, no spill — a visitor with a purpose gets a quiet
  bench and a sharp tool.
- **Search.** Results file into compartments by initial (§6.13);
  zero results is §6.18's "NOT IN THIS CASE" state.
- **404 / empty.** §6.18, with the out-being-set vs never-cast
  distinction enforced by routing: known-but-unpublished URLs get the
  first, unknown URLs the second.

## 8. Worked examples

### 8.1 The hero — a type foundry opens its case

*Build: home page for a fictional foundry, "Hartwell & Sort".*
Scroll timeline: the visitor lands on a full-viewport case (§4,
69 compartments) lying spilled (§6.1): 60 glyphs scattered, e already
flying by the time the eye lands (t₀ = fonts-ready, ≤300ms). By
t₀+1.4s e is home and its rim has flashed; by t₀+3.4s the case stands
sorted and the spill layer is gone. The visitor scrolls: the case
pins (160vh) and the headline "WE CAST LETTERS." composes (§6.2) —
W from the capitals bank, E twice from the big box (second dip 90ms
later, exactly as a compositor would), the full stop from the points
row. At p=0.6 the headline stands at full ink over the sorted case;
the case-map in the header has inked W, E, C, A, S, T, L, R, O, U —
ten cells — and SORTS SET reads 15. The pin releases into the first
section, whose H2 "The lower case" will rain-and-recompose at its
boundary. A visitor who never scrolls still saw: a spill, a sort, a
composed headline — the whole thesis in the first screen.

### 8.2 Mid-page — the specimen ledger

*Build: a specimen/pricing section on the same page.* The section
lives in a wide compartment labelled "LOWER CASE — THE WORKING
LETTERS". Its H2 "Prices, by the sort" rains in (§6.3): the previous
heading's letters fall home (the S from "Sections" lands in the
s-box the visitor just watched fill), then P, R, I, C, E, S lift and
compose. Below, the frequency ledger (§6.13) lists 12 typefaces with
real prices; its rows door-open (§6.6) in reading order. The visitor
clicks "BY THE CASE": the rows pied for 150ms and re-file so the
row whose name starts with E sits in a Large row-band, Q's row in a
Small one — and the caption states the rule aloud. Hovering a row
lifts its key sort 2px. Nothing on the section is decoration: the
table is the price list, the filing is the sorting the foundry sells.

### 8.3 Conversion — setting your details

*Build: "Order a specimen" at the page's foot.* The composing-stick
form (§6.12) holds three lines: NAME (Fraunces field), EMAIL,
SPECIMEN (a select rendered as a row of three pickable plaques —
radio sorts). Focusing EMAIL slides an 'e' sort into the margin —
the most common letter, doing its most common job. The visitor
submits with a malformed email: the line's sort pieds 12°, the rule
turns `--red-deep`, and beneath the line the error sets itself:
"That address won't set — the @ sort is missing from the line."
They fix it, resubmit: lines square (120ms stagger), the quoin
draws, the stamp lands — "JOB Nº 214" — and the forme shows their
details re-set as composed lines with the line "Your details, set in
type. Nothing else was taken." The footer imprint below (§6.17)
records SORTS SET for the page; the visitor's own word in the stick
— they set "QUOIN" while scrolling, because the case taught them the
word — stamps into the imprint as they reach it.

## 9. Anti-slop — what makes THIS theme look cheap

1. **Uniform compartments.** A case with equal boxes is a spreadsheet
   in a wood frame. Cure: §4's frequency classes, audited (gate B1).
2. **Letters flying nowhere.** Glyphs that drift, float or orbit as
   ambience break the one law (§1). Cure: every flight has a source
   compartment, a destination, and a reason; the restless sort (§6.4)
   is the single licensed exception and it flies *between boxes*.
3. **Fake counters.** "10,000 letters set!" counting nothing. Cure:
   counters read DOM events (§6.5, §6.17); if the engine is off, the
   counters are absent, not zero.
4. **A pre-filled case-map.** Progress that fills by scroll percentage
   instead of by letters used. Cure: the map inks only on
   heading-composed events (§6.5).
5. **Blur-to-sharp type.** Screen-effect type in a wood-and-metal
   world. Cure: refused in §5; arrivals land with overshoot + shadow.
6. **Marquee tickers of words.** Conveyor-belt text. Cure: refused in
   §5; ambient life is the restless sort and the wood light only.
7. **Red everywhere.** Red buttons, red links, red badges — the accent
   spent into wallpaper. Cure: §2's ≤5% rule; red marks the letter in
   play, errors, and the divider rules only.
8. **Headings the case can't set.** An H1 needing five z's, silently
   cloned. Cure: §3 law 1 — reword or visibly borrow from the tray.
9. **Wood texture as a stock photo background.** A photographic wood
   image behind glassmorphism cards. Cure: wood here is flat token
   colour + gradient grain on *structural* dividers; cards are
   compartments, not panels floating over a picture.
10. **The spill on every page.** The opening trick repeated until it
    is a screensaver. Cure: §7 — spill is home-page, first-visit-of-
    session only; interior pages open on a sorted case.
11. **Pied notices for good news.** Tumbling a success message makes
    success feel like an accident. Cure: §6.14 — only errors pied;
    success arrives set and stamped.
12. **Tilting body text.** The tray tilts (§6.8); paragraphs below the
    hero never do. A page whose reading copy sways is a page asking
    to be closed.

## 10. Quality gate

**Blocking (must all pass):**
- **B1 — Frequency audit.** Compartment spans match §4's classes; 'e'
  is the largest box at every breakpoint; spot-check three letters
  against a printed California job-case diagram.
- **B2 — Census audit.** Every H1/H2's letter multiset is settable
  from stated stock, or borrowing is visibly performed (§6.2).
- **B3 — Counter truth.** SORTS SET / WORDS COMPOSED / case-map state
  are derived from real composition events; disable JS and confirm
  counters vanish rather than lie.
- **B4 — No stranded content.** With JS disabled, and again with the
  animation loop killed mid-page, every heading and block is fully
  readable; all watchdogs (1000–1200ms) fire.
- **B5 — Reduced motion.** With `prefers-reduced-motion`, the page is
  a sorted case with composed headings: no flights, no pin, no tilt,
  no hop; forms, notices and the stick still fully function.
- **B6 — Red budget.** Sample five viewports: `--red` family ≤5% of
  pixels in each, excluding divider rules.
- **B7 — Stock honesty.** §6.7's pick stock matches the stated class
  numbers; "OUT OF SORTS" occurs exactly when the DOM stock is spent.
- **B8 — Focus survival.** Keyboard-only pass: every interactive
  element reachable, focus visible on wood and paper, no focus ever
  inside a clipped-shut block (§6.6 forces it open first).

**Standard (should all pass):**
- S1 — Five-second test: a first-time viewer can say "it's a box of
  letters, and the letters make the headings" after one screen.
- S2 — Flight discipline: no frame of a screen recording shows a
  glyph in flight without a visible destination compartment.
- S3 — Ambient count: exactly two ambient loops (§6.4 + wood light).
- S4 — The pangram flourish (§6.5) fires on a test pangram page and
  only there.
- S5 — Print stylesheet: the page prints as a sorted case with
  composed headings and a set imprint; no clone layers, no lids.
- S6 — Performance: §14's budget verified on a mid-tier Android over
  4G; the spill holds 50fps or degrades per the cut order.

---

## 11. Component inventory

Every component a real site needs, in the case's furniture. Components
the theme refuses are listed with their in-theme replacement — a
refusal without a replacement is a gap, not a stance.

| Component | Themed treatment |
|---|---|
| Primary button | Wood plaque (`--wood` ground, `--paper` label on an inset paper chip), presses 2px into the tray on active; label is a verb + object ("SET THE WORD", "SEND THE PROOF") |
| Secondary button | Paper plaque with 2px `--ink` keyline; hover lifts its first letter's sort 2px |
| Text input | A ruled line in a stick well (§6.12): bottom rule, plaque label, initial-sort focus marker |
| Select | A row of pickable sort plaques (radio sorts); >5 options become a drawer (§6.15) of plaques — a native dropdown's OS chrome is refused |
| Checkbox | A small compartment that fills with a set sort (the field's initial) when checked; the empty box is visibly a box |
| Radio group | Sorts in a shallow row of compartments; the chosen sort inks, others stay paper |
| Toggle | **Refused.** A workshop has no toggles; binary choices are two plaques, one inked (state is a physical position, not a pill) |
| Table | The frequency ledger (§6.13) |
| Badge / tag | A small paper plaque pinned to a compartment rim, Space Grotesk caps; counts on badges are real counts or the badge does not ship |
| Alert / notice | Pied-type notices (§6.14) — inline, in the compartment concerned |
| Toast | **Refused** — replaced by §6.14 (notices live in their compartment, never float over the page) |
| Modal | A pulled drawer at case scale: a full compartment slides up from the tray's bottom edge (420ms `--ease-door`) with a scrim of `--wood-deep` at 60%; the modal's content is set as a compartment block; Esc returns it to the tray. Modals are for confirmations and the nav drawer (§6.10) only — never for content that deserves a page |
| Tabs | A row of compartment fronts (§6.15 fronts laid horizontally); the active tab's front is dropped/open, its panel a compartment below. Tab panels never animate letters — tabs switch stored material |
| Accordion | Drawer compartments (§6.15) |
| Pagination | "NEXT LEAF" plaques + a case-map-style strip of page cells that ink as pages are visited; numbered, always — infinite scroll is refused for ledgers and listings (a case has edges) |
| Breadcrumbs | A line of small sorts: the initials of the path's sections, each a link, separated by quad spaces — "H · S · P" reads as the route set in type |
| Search input | A stick well (§6.12 grammar) whose results file by initial (§6.13); the input's plaque reads "FIND A SORT OF THING" |
| Progress bar | **Refused as a bar** — replaced by the case-map (§6.5) for reading progress and by inking compartments for task progress |
| Spinner | **Refused** — replaced by face-down sorts (§6.16) |
| Tooltip | A pencilled plaque that appears above the element on hover/focus (200ms fade), set in label caps; tooltips carry at most 8 words and never essential content |
| Avatar / image | A printer's block in a wood mount (§6.11); people are blocks with captions naming them, never circles — the case has no round compartments |
| Divider | The wood band + red rule (§6.9) — the only divider the theme owns |
| Footer | The case bottom (§6.17) |
| 404 / empty | The empty compartment (§6.18) |

## 12. Content & copywriting voice

Two registers, never swapped. **The Case speaks** (labels, plaques,
apparatus): terse, factual, in caps, stating what a thing is and what
it contains — "LOWER CASE — E THROUGH R", "OUT OF SORTS", "SET FROM
THE CASE BELOW". **The Compositor speaks** (headings' standfirsts,
errors, empty states, confirmations): first person plural of the
workshop, plain sentences, dry wit that is always a technical term
used correctly — the joke is never pasted on, it is the trade's own
vocabulary ("pied", "out of sorts", "mind your p's and q's" — which
is a compositor's warning about two sorts that mirror each other,
and may be used exactly once per site, in the footer).

- **Headlines:** settable (§3 law 1), concrete nouns over adjectives.
  ✓ "We cast letters." ✗ "Typography, reimagined for the modern age."
- **Labels:** contents + census. ✓ "E — 12.7% OF ENGLISH TEXT".
  ✗ "Popular letter".
- **Errors (compositor, kind, specific, with the fix):**
  ✓ "That address won't set — the @ sort is missing from the line."
  ✗ "Invalid input." / "Oops! Something went wrong."
- **Empty states:** which kind of empty (§6.18).
  ✓ "Never cast — no such sort." ✗ "Nothing here yet!"
- **Confirmations:** what was set, and the job number.
  ✓ "Set. Job Nº 214 — your specimen leaves with Friday's post."
  ✗ "Success! Your request has been received."
- **Waiting (§6.16 lid):** ✓ "Setting the next page — the e's are
  done, the z's are travelling." ✗ "Loading, please wait…"
- **Banned words:** "revolutionary", "seamless", "delve", "in today's
  fast-paced world", any use of "literally" for emphasis, and "chaos"
  as a compliment for the site's own disorder — the chaos is the
  *material*, the craft is the order underneath it; copy that calls
  the page chaotic has misunderstood the theme.
- **Owned words:** sort, case, pied, out of sorts, compose, lock up,
  forme, quoin, quad, imprint, leaf, cast (as a verb for letters).

## 13. Full-page scroll choreography map

Home page, top to footer — every beat in order. (Interior pages use
the subset §7 assigns them.)

| # | Scroll position | Beat | What the visitor sees / feels |
|---|---|---|---|
| 1 | Load (0%) | Spill (§6.1) | 60 sorts fly home in frequency order; the case becomes orderly under their eyes — *this place works* |
| 2 | 0–60% of hero pin | Composition (§6.2) | The headline's letters rise from their boxes and set themselves; the case-map begins inking — *the page is made of these letters* |
| 3 | 60–100% of pin | Hold | Composed headline over the full case; one quiet beat; the restless sort may hop — *the workshop is alive* |
| 4 | First boundary | Rain-and-recompose (§6.3) | Section 1's heading dissolves home; section 2's composes from the same stock — *the letters are shared, finite, real* |
| 5 | Each section | Doors + dividers (§6.6, §6.9) | Blocks come out of their compartments; red rules draw the structure in — *everything here is stored, then taken out to be read* |
| 6 | Mid-page listing | Cards + ledger (§6.11, §6.13) | The sub-case of content; a table that files itself by frequency on request — *even the data lives in the case* |
| 7 | Throughout | Case-map fills (§6.5) | The header census grows heading by heading — progress they can *read*, not just see |
| 8 | Conversion section | The stick (§6.12) | The visitor's own details are set in type; errors pied and re-set; the job is stamped — *my words, handled like type* |
| 9 | Footer approach | Case bottom (§6.17) | Their picked word stamps into the imprint; the page's true counts are read out — *the page accounts for itself* |
| 10 | Exit (any internal link) | The lid (§6.16) | The case closes and reopens on the next page — *one workshop, many pages* |

**Reverse pass:** scrolling back up, beats reverse honestly — headings
de-compose and re-compose (§6.3 is symmetric), doors stay open (§6.6
never re-closes), the case-map never drains (§6.5 is a ledger), the
spill never re-spills (§6.1 is a first entrance only). **Jump-scroll
catch-up:** a jump to mid-page sets every passed beat to its finished
state instantly (headings composed, map inked to the correct census
for the headings actually above, doors open) — the page is always
truthful at the position it is read from.

## 14. Whole-page performance budget

| Budget | Cap |
|---|---|
| Fonts | Fraunces (900, opsz) + Space Grotesk (400/500/700), subset to Latin + the case's glyph set: ≤140KB total woff2 |
| JS (animation engine) | ≤38KB gz — one shared loop, one clone layer, no framework for motion |
| Images | Blocks are lazy-loaded below the fold; hero case is pure DOM/CSS/SVG (0KB of imagery) |
| Concurrent transforms | ≤60 (spill peak), ≤28 (boundary events), ≤14 (composition) — enforced caps in §6 |
| Frame budget | Shared loop ≤1.4ms/frame average on a mid-tier Android; lerp writes are transform/opacity/CSS-var only |
| Long tasks | No task >50ms during scroll; census counting is O(letters in heading) |
| Layout shift | CLS ≤0.02 — skeletons hold true sizes (§6.16), compartments are grid-placed before any flight |

**Cut order when the budget is exceeded** (cut in this order, never
skip ahead): 1) restless sort scheduler (§6.4) off; 2) wood-light
ambient off; 3) tilt channel (§6.8) off; 4) spill count 60→36→0
(case opens sorted); 5) rain grammar (§6.3) reduced to ink-deepen
past the first boundary; 6) card image scrub (§6.11) off. **Never
cut:** compartment doors' fallbacks and watchdogs, the case-map's
truthfulness, form and notice function, reduced-motion variants,
focus behaviour. A slower page may be plainer; it may never be
dishonest or unreadable.

## 15. Build-order checklist

1. Static case first: the full 69-compartment grid (§4) with real
   sorts, composed headings, open blocks — the complete no-JS page.
   Verify it reads perfectly with scripts off.
2. Palette/type tokens (§2, §3) and the frequency table as a single
   source constant (grid spans, stock, census all derive from it).
3. Divider bands + plaques (§4) and the header strip with nav
   (§6.10) and an empty case-map (§6.5).
4. Compartment doors (§6.6) with watchdogs — the reveal layer every
   block depends on.
5. The shared rAF loop (lerp 0.12) and the clone layer; then the
   spill (§6.1).
6. Composition (§6.2) + case-map inking events (§6.5) + counters.
7. Rain-and-recompose (§6.3) with the serial queue and settle timers.
8. The word tray (§6.7): pick flights, stock, stick, session state.
9. Tilt (§6.8) and restless sort (§6.4) — the two garnish channels,
   built last among hero systems, cut first under pressure (§14).
10. Cards (§6.11), ledger (§6.13), drawers (§6.15) — content furniture.
11. The stick form (§6.12) + pied notices (§6.14), wired to real
    validation and the real job-number source.
12. Skeleton + lid (§6.16), footer imprint (§6.17), empty
    compartment (§6.18).
13. Lamplight dark scheme (§2) and print stylesheet.
14. Reduced-motion pass: every element's variant verified, not
    assumed.
15. Run the §10 gate — blocking items first; a failure loops back to
    the step that owns it, never to a patch at the end.
