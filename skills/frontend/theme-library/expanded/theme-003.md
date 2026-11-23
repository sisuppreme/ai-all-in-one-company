# Theme 003 — Redacted Archive (Expanded)

**Reference implementation:** `demos/redacted-archive.html` — the living demo this expansion is aligned to, element for element. Where this document and the demo disagree, this document is the build target and the demo is updated to match.

---

## 1. Concept & world

**The world.** A records office at 2 a.m. One desk lamp. A single case file — manila folder, punched holes, a chain-of-custody sheet clipped to the inside cover — has just been cleared for release, and the visitor is the person it was released *to*. The site is not *about* a dossier; the site **is** the dossier. Every page is a sheet inside one folder, every section is an exhibit, and reading is a bureaucratic act with physical consequences: bars lift, stamps land, counters increment, custody changes hands.

**The core mechanic, and why it is the whole theme.** Black redaction bars are the design system. Content is not hidden *behind* the design — the sensitive sentences of the actual copy are covered by bars, and the bars lift only when a sentence reaches reading position. Scrolling is therefore not navigation; scrolling is the **clearance process**. The visitor earns the document line by line, in document order, and the interface keeps the paperwork of that earning: a clearance dial in the rail (LVL 0–5), a header pill counting DOCUMENTS RELEASED, a rail counter counting PAGES FREED, and a rubber stamp that certifies each sheet only after it has actually been read. Trust is the product being demonstrated, and it is demonstrated procedurally: the site withholds, releases, and certifies in the open.

**Mood.** Dry, procedural, faintly paranoid, completely humourless on the surface — and therefore quietly funny and deeply confident underneath. Nothing on the page winks. The single joke the theme allows itself is restraint: one bar, in the finale, never lifts, and its tooltip says so. The emotional arc across one page is: *suspicion* (a fully redacted hero) → *procedure* (bars lifting in order, stamps landing) → *earned intimacy* (the custody chain complete, the file signed over) → *respect* (one thing stays classified, because a bureau that releases everything is not trustworthy either).

**Best-fit sites and audiences.**

- **Cybersecurity firms and security auditors** — the file *is* an audit report; findings are literally released as the prospect reads. The mechanic performs the firm's own value: we find what was hidden, we show our working.
- **Privacy tools (VPN, encrypted storage, secure messaging)** — the visitor's own data is the withheld material in every other product's fine print; here, withholding is honest, visible, and reversed in front of them.
- **Investigative podcasts, documentary series, long-form journalism projects** — episodes as exhibits, sources protected by bars that lift only for material actually cleared for broadcast.
- **Whistleblower-support and digital-rights organisations** — chain-of-custody is their literal daily work; the theme speaks their paperwork as a first language.
- **FOIA / transparency data projects** — released-document archives where the release status of each record is real metadata, not decoration.

**When NOT to use it.**

- Anything that needs warmth at first contact: consumer food, childcare, weddings, wellness retail. The theme's first screen is a wall of black bars; that is a deliberate act of withholding and it will read as hostility where trust is supposed to be instant.
- High-frequency transactional UI (checkout-dense e-commerce, trading dashboards). The clearance mechanic is a *reading* mechanic; it taxes every revisit. A user who returns daily to do one quick task must never be made to re-earn a document.
- Sites whose content cannot honestly be "released" in sequence — if there is no real withheld-then-shown structure in the material (findings, evidence, episodes, records), the bars become costume, and costume is exactly the slop this theme exists to refuse.
- Any build that cannot guarantee the fallbacks in §6. A redaction theme whose bars can fail shut is the one unforgivable version of this design; if the fallback budget isn't there, pick another theme.

**The one-sentence test.** If a visitor screenshots any single sheet, a stranger should be able to say "that is a page from a declassified file" without seeing the logo — from the paper, the type, the bars, and the stamp alone.

---

## 2. Palette

Four anchor inks, exactly as specified for this theme. Every other token below is a *derived* token — a shade, edge, or shadow of one of the four anchors — and is labelled as such. No fifth hue ever enters the theme. In particular: no red (red is the colour of every cheap "TOP SECRET" cliché, and this archive does not use it), no blue links, no white paper. The paper is manila; the ink is carbon; the only colour event in the entire theme is stamp green.

| Token | Hex | Role | Usage ratio | Pairing & contrast | Dark-mode behaviour |
|---|---|---|---|---|---|
| `--manila` (anchor) | `#D8C49A` | Sheet paper — the background of every document surface | ~62% of viewport | Carries `--ink` body text at ≈7.4:1 (passes AA for body, AAA for large). The default ground; everything else is printed on it. | Sheets do **not** invert. At night the archive dims the lamp, not the paper: `--manila` steps to its derived `--manila-dim` (below) and the desk darkens. Paper stays paper. |
| `--carbon` (anchor) | `#17171A` | Redaction bars at rest, brand marks, the desk's shadow side, stamp-pad black | ~18% | On `--manila` ≈9.8:1 — used as a *field*, never as small text on manila (typewriter ink does that job; carbon text looks photocopied-to-death). | Unchanged. Carbon is carbon in both modes; bars must read as the same physical object. |
| `--ink` (anchor) | `#33302B` | Typewriter ink — all document body text, file numbers, captions, form fields | ~14% | On `--manila` ≈7.4:1. The only colour body text may ever be. Never set smaller than 0.875rem — below that the warm grey goes muddy on manila. | On `--manila-dim` ≈6.1:1 — still AA for body. Ink does not lighten; the paper darkens less than the desk so the ratio holds. |
| `--stamp` (anchor) | `#2E5E3A` | Release-stamp green — stamps, the dial arc, cleared ticks, the one allowed accent | ~3% | On `--manila` ≈4.6:1 — stamps and large display only, never body text, never smaller than 0.75rem bold. Scarcity is the meaning: green appears only where something has been *certified*. | Unchanged hex, but stamps gain the derived `--stamp-bleed` halo (below) so the ink reads as wet on dimmer paper. |
| `--manila-deep` (derived) | `#B39B6B` | Sheet edges, folder tabs, the underside of a lifting bar, rail background | ~2% | Edge colour only; never a text ground. Pairs against `--manila` as a 1.3:1 tonal step — enough to read as a paper edge, not a stripe. | Becomes the sheet colour's shadow side; sheets keep `--manila-dim` faces with `--manila-deep` edges. |
| `--manila-pale` (derived) | `#EADFC0` | The lamp pool on the hero sheet, highlight side of a tilted folder, skeleton paper under an unopened evidence sleeve | <1% | Highlight only, applied as a radial gradient pool, never a flat panel. | The lamp pool is the *only* place pale survives at night — it is lamplight, and it follows the lamp logic in §6.13. |
| `--manila-dim` (derived) | `#C4AC7E` | Dark-mode sheet paper | replaces `--manila` | Keeps `--ink` at ≈6.1:1. | — (this *is* the dark-mode token) |
| `--desk` (derived) | `#4A4033` | The desk surface beneath the stack; page background outside sheets | ~3% (gutters/edges) | Frames the stack. Text never sits directly on it except the footer's custody block, which uses `--manila-pale` at ≈5.9:1. | Deepens to `#2E2820`. The stack floats darker; sheet edges pick up a longer shadow. |
| `--bar-edge` (derived) | `#26262B` | The 1px lit edge on a redaction bar as it lifts; bar hover state | <1% | One pixel only. It is the light catching the marker stroke's edge — the difference between a bar that is a flat rectangle and a bar that is a physical stroke being peeled. | Unchanged. |
| `--ink-faded` (derived) | `#6E675C` | Superseded text: struck-through draft lines, "previously released" duplicates, disabled form labels | <1% | On `--manila` ≈3.9:1 — large or decorative text only; anything a user must read is re-set in `--ink`. Fading is a *statement* (this text is old), never a readability shortcut. | On `--manila-dim` ≈3.2:1 — display use only. |
| `--stamp-bleed` (derived) | `rgba(46,94,58,.28)` | The soft halo under a fresh stamp for its first 900ms; dark-mode stamp presence | <1% | Never a fill. It is wet ink soaking into manila fibres, and it dries (fades to 0) on a timer. | Permanent at 40% strength under stamps — at night the ink never fully dries. |

**Palette laws.**

1. **Green is earned.** `--stamp` may only appear on: a stamp that has landed, the dial arc at or below the visitor's current clearance level, a cleared tick on a custody step already read, and the submit state of the request form *after* filing. A green button that has certified nothing is a palette violation.
2. **Bars are carbon, not black-by-default.** A bar set in pure `#000` reads as a rendering error; `--carbon` at `#17171A` with a `--bar-edge` lit pixel reads as a marker stroke. The 6% difference is the whole effect.
3. **No colour carries information alone.** Every green certification is doubled by a word (DECLASSIFIED / CLEARED / RELEASED) set in the stamp itself; every redaction is doubled by position (the bar sits on a sentence). Colour-blind visitors lose nothing.
4. **Ratios are budgets, not suggestions.** If a layout pushes manila below ~55% of the viewport, the desk is winning and the file is losing — re-stack the sheets.

---

## 3. Typography

Two families, no exceptions, no third voice. **Courier Prime** is the file: every word that is *in* the document — body, captions, file numbers, form fields, counters, the custody chain — is typewritten. **Archivo Expanded** (font-stretch 125%, via `Archivo:wdth,wght` variable axes or the pre-stretched Expanded cut) is the bureau: labels, brand, headings, stamp lettering — the voice of the office that processed the file, not the file itself. The tension between the two is the theme's typographic plot: the bureau speaks in wide, stamped capitals; the evidence speaks in monospaced typewriter lines.

| Role | Font | Size | Weight / stretch | Line-height | Tracking | Rules |
|---|---|---|---|---|---|---|
| File title (hero cover) | Archivo Expanded | `clamp(2.75rem, 6.5vw, 4.75rem)` | 800 / 125% | 0.98 | +0.01em | All caps. Never more than 3 lines. The title is the case name stamped on the cover, not a headline competing with it. |
| Sheet heading (H2) | Archivo Expanded | `clamp(1.75rem, 3.4vw, 2.5rem)` | 700 / 125% | 1.05 | +0.015em | All caps. Always preceded by its exhibit label (see below) — a heading without an exhibit number is an unfiled page. |
| Exhibit label | Archivo Expanded | 0.75rem | 700 / 125% | 1.2 | +0.22em | All caps, `--ink`. Format: `EXHIBIT B — CUSTODY TRANSFER, DAY 14`. This is the filing system speaking; keep it ruthlessly literal. |
| Stamp lettering | Archivo Expanded | 1.5–2.25rem (hero stamp 2.25rem) | 800 / 125% | 1 | +0.08em | `--stamp` only, rotated with its stamp, double-border frame. Never typeset a stamp word in Courier — stamps are not typed, they are *struck*. |
| Document body | Courier Prime | 1rem (16px) | 400 | 1.65 | 0 | The file's voice. Measure 58–68ch — a typewriter page is narrow. Paragraphs separated by a full blank line (1.65em), never indented; typewriters don't indent, they return the carriage. |
| Document body, dense (custody entries, tables of findings) | Courier Prime | 0.9375rem (15px) | 400 | 1.55 | 0 | Only inside exhibits. Never below 0.875rem anywhere (§2, ink law). |
| File numbers / counters / data | Courier Prime | inherits role size | 700 | inherits | +0.04em | `font-variant-numeric: tabular-nums` is mandatory — the PAGES FREED counter must not jitter sideways as digits change width. File numbers follow the pattern `FILE 114-K / EXHIBIT B / PAGE 03`. |
| Caption (evidence sleeves) | Courier Prime | 0.875rem | 400 italic | 1.5 | 0 | Courier Prime Italic is the *only* italic in the theme — the handwriting-adjacent voice of whoever annotated the evidence. One caption per sleeve, max 2 lines. |
| Tooltip (the permanent bar) | Courier Prime | 0.8125rem | 400 | 1.4 | 0 | Set on `--carbon`, text `--manila-pale`. The single place light text appears on a dark field inside a sheet. |
| Footer custody block | Courier Prime | 0.8125rem | 400 | 1.6 | +0.02em | On `--desk`, `--manila-pale` text (§2). The footer is the desk, not a sheet — the one place the file admits the desk exists. |

**Typographic laws.**

1. **Courier never justifies.** Left-aligned, ragged right, `hyphens: none`. A justified typewriter column is a lie about the machine.
2. **No bold inside document body.** Emphasis inside the file is achieved the typewriter way: underlining (`text-decoration-thickness: 1px; text-underline-offset: 3px`) or a second strike (the same word re-set with a 0.5px offset shadow in `--ink-faded` — used at most once per sheet, for the sentence that matters most).
3. **Headings are filed, not decorated.** Every H2 carries its exhibit label above it and its page number at the sheet's foot (`PAGE 03 / 06`). A sheet missing either is a quality-gate failure (§10).
4. **The caret is a character.** The typewriter caret (§6.3) is a 0.6em × 1.1em `--carbon` block, blink period 1060ms (530ms on / 530ms off, `steps(1)` — a real caret does not fade).
5. **Fallback stack honesty.** If Courier Prime fails to load, the fallback is `ui-monospace, "Courier New", monospace` and the layout must not reflow by more than 2% — Courier Prime's advance width is close to Courier New's by design of this pairing. Archivo Expanded falls back to `Archivo, "Arial Narrow Bold", sans-serif` with `letter-spacing` raised to +0.04em to fake the width. Both fallbacks are gate-checked (§10).

---

## 4. Layout language

**The stack.** The page is a stack of manila sheets on a desk, inside one folder. Three fixed pieces of furniture frame every page:

- **The top bar** (56px, `--manila-deep` edge below, `--manila` face): brand left (Archivo Expanded, 1rem, +0.22em tracking), the DOCUMENTS RELEASED pill right (§6.7). It is the folder's cover strip — it never gains a shadow, a blur, or a background gradient. Bureau furniture is flat.
- **The left rail** (fixed, 72px wide on desktop): a `--manila-deep` strip punched with binder holes — 10px circles, `--desk` fill, spaced 96px apart, offset 28px from the top — carrying the clearance dial (§6.6) centred at 38% of viewport height and the PAGES FREED counter (§6.7) beneath it, rotated 0°. The rail is the folder's spine; content never slides under it.
- **The desk** (`--desk`): visible only as a 24–40px margin around the stack and behind sheet shadows. If the desk is the most visible thing on screen, the stack is too small (§2, law 4).

**The sheets.** Each section is one sheet: `--manila`, max-width 880px, margin-left offset by the rail (72px) plus a 40px gutter, padding 56px 64px 72px, and a rotation drawn from a fixed per-sheet table — sheet 1: −0.3°, sheet 2: +0.2°, sheet 3: −0.15°, sheet 4: +0.3°, sheet 5: −0.2°, sheet 6: +0.1° — never random, never regenerated per load (a file does not re-shuffle itself between visits). Rotation is about the sheet's top-left punched corner, so sheets fan microscopically from the spine like a real stack. Sheet shadow: `0 1px 0 rgba(23,23,26,.18), 0 18px 34px -18px rgba(23,23,26,.45)` — a contact line plus a soft drop; the shadow is what sells the paper, so it is the one place softness is allowed.

**Grid and rhythm.** Inside a sheet, a single column rules: the document column is 58–68ch (§3) centred in the sheet's padding box. Exhibits that need a second column (evidence sleeves, folder cards) use a 2-up grid, `grid-template-columns: 1fr 1fr; gap: 40px 48px`, collapsing to 1-up below 720px. Vertical rhythm is the typewriter's: the base unit is one body line (1.65 × 16px = 26.4px, rounded to a 26px rhythm token `--line`); section-internal spacing is always a whole number of lines (1, 2, 3, or 5 lines), so every sheet reads as if its blocks were typed onto a grid of lines. Sheet-to-sheet gap: 64px of desk.

**Section choreography.** Sheets arrive in strict document order and are read in strict document order — the theme has no "skip around" layout patterns (no tabs, no accordions, no carousels; a file is linear). The sequence per page: cover sheet (hero) → findings/exhibits in numbered order → chain of custody → service folders → release note (finale). The choreography rule that matters: **a sheet's release sequence (§6.1, §6.2) may only begin when the sheet's top edge crosses 62% of viewport height** — the reading position. Sheets below the fold sit fully redacted and still; the archive never performs for an empty room.

**Density rules.** One idea per sheet. One stamp per sheet (the finale's watermark sweep is atmosphere, not a second stamp — §6.12). At most 9 redacted sentences per sheet: beyond that the sheet reads as a black rectangle and the mechanic stops meaning "withheld" and starts meaning "broken". Whitespace is the margin of the document — wide, deliberate, and *typed in*: margins carry the exhibit labels, the stamps, and the page numbers, so the whitespace is the filing system, not emptiness.

**Mobile layout (≤760px).** The rail leaves the left edge and becomes a 48px bottom bar: punched holes become a horizontal row of 5 dots, the dial becomes a linear clearance gauge (§6.6 mobile variant), PAGES FREED stays. Sheets go full-bleed width minus 16px desk margins, rotation halves (±0.15° max), padding drops to 32px 22px 48px. The top bar keeps the pill — the counter is load-bearing on every viewport.

---

## 5. Full motion system

Every motion term below is stated in this theme's own language, with its numbers. The shared easing vocabulary is defined once, here, and referenced by name in §6:

- `--ease-flick` — `cubic-bezier(.2,.9,.25,1)` — the dry paper flick: fast lift, no bounce, a hair of overshoot in rotation only.
- `--ease-thud` — `cubic-bezier(.16,1.24,.36,1)` — the stamp: falls fast, overshoots scale, settles once. Never used for anything that is not struck.
- `--ease-file` — `cubic-bezier(.7,0,.2,1)` — the folder swing: heavy start, heavy end, the weight of card stock.
- `--ease-bureau` — `cubic-bezier(.4,0,.2,1)` — the office standard: labels, pills, hovers. Deliberately boring.
- Scrubbed motion (dial, evidence line, watermark) is **linear by definition** — it is bound to scroll position, not to time.

All scroll-driven values pass through one shared requestAnimationFrame loop with lerp factor 0.16 per frame (the demo's proven value): raw scroll position is never written to the DOM directly. At 60fps the lerp settles within ~1px of target in ≈180ms — close enough to feel attached, loose enough to feel like paper sliding, not a machine tracking.

| Motion term | In this theme's language | Duration / easing | Trigger |
|---|---|---|---|
| Scroll-triggered reveals | Redaction bars lift as their sentence reaches reading position (§6.1); stamps slam at sheet end (§6.2) | Bar lift 380ms `--ease-flick`; stamp 320ms `--ease-thud` | IntersectionObserver, sheet top at 62% viewport height; bars within a sheet stagger 90ms in document order |
| Parallax layers | Three depths: binder-hole rail and staple shadows on the deepest layer (0.92× scroll speed), sheets at 1.0×, the photocopy noise field at 1.04× — the copy of the copy drifts slightly against the original | Continuous, lerp 0.16 | Scroll (scrubbed) |
| Pinned scenes | The dossier cover (hero sheet) pins for the first 120vh while Exhibit A slides up beneath it — the file is opened before it is read | Pin length 120vh; under-sheet travels at 1.0× | Scroll (scrubbed) |
| Masked line reveals | Custody entries are uncovered by a ruler-mask: a `--manila-deep` straight-edge bar slides down the entry as it enters, text visible only below the edge — as if a ruler were drawn down the page | 520ms `--ease-file` per entry, 120ms stagger | Scroll entry per entry |
| Blur-to-sharp reveals | Evidence photographs resolve from photocopy blur (blur 6px, contrast 0.92) to sharp as the viewing slit widens (§6.5) — a copy coming into focus under the lamp | 640ms `--ease-bureau`, synchronised with the slit's clip-path | Scroll entry per sleeve |
| Animated counters | DOCUMENTS RELEASED and PAGES FREED count up by exactly 1 per certified sheet — never animated over time, incremented by event (§6.7) | Digit change: 120ms `--ease-bureau` vertical tick (old digit slides up, new digit takes its place) | Stamp-land events only |
| Progress indicators | The clearance dial (§6.6) and the self-drawing evidence line (§6.8) *are* the progress indicators; there is no progress bar anywhere in this theme | Scrubbed, linear, lerp 0.16 | Scroll depth / section progress |
| Marquees | The classification strip: along the top edge of each cleared sheet, a repeating Archivo Expanded legend — `DECLASSIFIED · RELEASED UNDER REQUEST 114-K · ` — translates left at 24px/s, printed in `--ink-faded`. It moves like a teletype ticker, and only on sheets already cleared: the strip is the sheet's release header being re-printed, endlessly, by a machine that does not know the file is finished | Linear, 24px/s, seamless loop (two copies of the strip, translateX −50%) | Sheet cleared (stamp landed); pauses when the sheet is off-screen |
| Ambient loops | Photocopy noise crawling in discrete steps; dust motes rising in the hero's lamp pool (§6.9) | Noise: `steps(6)` position jumps, 900ms cycle; dust: 9–14s rise per mote, individual delays | Time; both pause off-screen and under `prefers-reduced-data` |
| Micro-interactions | Un-lifted bars shiver on hover with light on the edge (§6.1); folder cards tilt (§6.10); the permanent bar's tooltip (§6.12); pill tick (§6.7) | Shiver 160ms; tilt spring-back 420ms; tooltip fade 140ms `--ease-bureau` | Hover / focus / click / keyboard |
| Hover physics | Folder tilt is a spring, not a tween: corner-lift rotation follows the pointer with stiffness 170, damping 19 (slightly under-damped — one visible overshoot of ≤0.4°, then rest) | Spring (rAF), settle ≈420ms | Pointer move over card; disabled on touch |
| Page transitions | The folder-gate: two manila panels swing shut, the jump happens behind them, they reopen (§6.11) | 380ms close + 380ms open, `--ease-file` | Nav click / in-page anchor |
| Image treatments | Evidence photos: slit reveal + blur-to-sharp + in-frame scale from 1.12 → 1.0 (the photo settles into its sleeve as the slit opens) (§6.5) | 640ms `--ease-bureau` | Scroll entry per sleeve |

**Motion laws.**

1. **Nothing moves before it is read.** Ambient loops are the only free-running motion, and they are atmosphere (noise, dust), never content. Every content motion is bound to reading position, a stamp event, or a deliberate visitor action.
2. **Order is sacred.** Within a sheet, bars lift in document order, top to bottom, no exceptions — a bar that lifts before the sentence above it breaks the clearance fiction and the reading itself.
3. **Motion is paper-physical.** Everything that moves is paper, card, ink, or light. Nothing fades in from nowhere, nothing scales from a dot, nothing slides in from off-canvas except sheets sliding under the pinned cover. Opacity-only reveals are banned except the tooltip and the stamp-bleed dry-out.
4. **One rAF loop.** Dial, evidence line, parallax, watermark, and tilt all read from the single shared scroll/pointer loop. A second loop is a performance defect, not a style choice.

---

## 6. Signature elements

Each element below is a full build spec. "Fallback" always means the same thing in this theme: **the content is fully present and readable with the animation absent, failed, or disabled** — redaction is an overlay on a complete document, never a gate in front of one.

### 6.1 Peeling redaction bars

- **What & why.** Black bars (`.bar` overlays on `.rx` spans) cover the file's sensitive sentences and lift as the visitor reads. This is the theme's founding element: the bars are not decoration on the copy, they *are* the copy's clearance state. A bar belongs to this theme because the archive's whole promise — "we show you what was hidden, in order, on the record" — is performed by this one mechanic and no other.
- **Structure.** Inline: each redacted sentence is a `<span class="rx">sentence text<span class="bar" aria-hidden="true"></span></span>`. The `.bar` is absolutely positioned over its span (inset −2px vertical, −4px horizontal, so the stroke slightly overhangs the words like a real marker), background `--carbon`, border-radius 1px (a marker tip is not square, not round). Multi-line sentences wrap: the bar is painted per line-box using `box-decoration-break: clone` on the span with the bar as a background-layer pseudo-element per fragment — implement as one `.bar` per line fragment at build time for sentences known to wrap at desktop measure; at mobile measure the fragment count changes, so the production approach is `background-image: linear-gradient(--carbon, --carbon)` sized to the span with the lift performed on a cloned overlay. Keep it simple and robust: bars are generated per-sentence by a small script that wraps each line fragment; if that script does not run, see Fallback. The lift is a 3D peel: `transform: perspective(600px) rotateX(0→−72deg)` with `transform-origin: 50% 0%` (hinged at the top edge, peeling *up and back* like a strip of tape), the underside revealed as `--manila-deep` via a backface gradient, ending at opacity 0 for the final 15% so no ghost strip remains.
- **Motion spec.** Hero: first bar at 450ms after load, then 210ms stagger, strict document order. Section sheets: the sheet's IntersectionObserver fires at reading position (sheet top at 62% viewport height); its bars lift in document order with 90ms stagger. Each lift: 380ms, `--ease-flick`, with a 24ms edge-light pre-flash (the `--bar-edge` 1px line brightens as the peel begins — light catching the marker's edge before it moves). Hover on an un-lifted bar: shiver — `translateX` ±0.6px at 160ms steps for 2 cycles plus edge-light on; the bar is nervous, not playful.
- **States.** *Rest (un-lifted):* flat `--carbon`, 1px `--bar-edge` on the bottom edge only. *Hover/focus-within:* shiver + edge light. *Lifting:* peel in progress, underside visible. *Lifted:* removed from layout paint entirely (`visibility: hidden` after the animation, so screen readers and find-in-page meet only the text). *Scrolled-past:* identical to lifted — a released sentence never re-redacts.
- **Content-merge.** The bars sit on the audit's real findings, the podcast's real cleared quotes, the tool's real data practices — the sentences the organisation would actually have to think twice about publishing. If a sentence is not worth redacting, it is not redacted; bars rationed to genuine tension are what make the lift feel like release.
- **Failure fallback.** Three layers, all mandatory: (1) a hard 800ms timer per scheduled lift — if the animation has not completed, the bar is force-lifted (class swap, no transition); (2) a 7s global safety sweep after load that lifts every bar except §6.12's permanent one, whatever state the sequences are in; (3) with JavaScript disabled, bars are never applied in the first place — the redaction spans render as plain text with a `<noscript>` style that also underlines them in `--ink-faded` so the *idea* of prior redaction survives without the mechanic.
- **Reduced-motion variant.** All bars pre-lifted on load except the permanent bar (§6.12). No peel, no shiver, no stagger. The document simply arrives released, with stamps already landed (§6.2).
- **Performance budget & mobile.** Bars animate `transform` and `opacity` only; ≤40 bars per page total (rationing law, §4); `will-change` is applied to a bar only during its 380ms lift and removed on completion. Cost: negligible — one composited layer per lifting bar, never more than 3 lifting simultaneously (stagger guarantees it). Mobile variant: identical, except the peel hinge flips to the bottom edge (`transform-origin: 50% 100%`, rotateX +72deg) — on a narrow column the upward peel can cover the line above mid-animation; the downward peel uncovers into the line gap instead. Shiver disabled on touch (no hover), replaced by the edge-light flash alone on first tap before the lift.

### 6.2 Slamming rubber stamps

- **What & why.** The certification event. The hero's DECLASSIFIED stamp lands after the hero bars finish; each sheet ends with its own CLEARED stamp; evidence captions earn mini RELEASED stamps (§6.5). A bureaucracy that releases paper without stamping it has not released it — the stamp is the moment a sheet changes legal state, and the whole counter system (§6.7) is keyed to its landing.
- **Structure.** A `<div class="stamp">` per stamp: Archivo Expanded 800, all caps, `--stamp`, double border (3px outer, 1px inner, 6px apart, border-radius 3px — rubber stamps have slightly soft corners), padding 10px 18px, mix-blend-mode: multiply so the ink sits *in* the paper rather than on it, and a subtle ink-texture mask (an SVG feTurbulence data-URI at 4% opacity) so the strike is uneven like real rubber on rough manila. Resting rotation is fixed per stamp from a table (−8° hero, then −5°, +3°, −6°, +4°, −3° down the sheets) — never random per load. The stamp lives in the sheet's margin space reserved for it in the layout (§4): it overlaps the document column's right edge by ~18px, the way a real stamp overruns the text block.
- **Motion spec.** The slam: from `scale(1.6) rotate(rest − 4deg) translateY(−10px)`, opacity 0→1 in the first 60ms, to rest state in 320ms `--ease-thud` — overshoot is in the easing (1.24 control point), landing with a 90ms `stamp-bleed` halo (§2) that dries over 900ms. Synchronised sheet response: the sheet itself dips `scale(0.99)` for 120ms on impact (the thud travels into the paper) and returns with `--ease-file`. Hero stamp fires 260ms after the last hero bar completes its lift. Sheet stamps fire when the sheet's last bar lifts, +180ms. The sound of the theme is this timing: *flick… flick… flick… THUD.*
- **States.** *Un-struck:* absent (the reserved margin space is empty — an unstamped sheet is visibly unfinished, which is the point). *Striking:* the 320ms slam. *Struck (rest):* multiply-blended ink, bleed dried. *Scrolled-past:* unchanged; stamps never un-strike.
- **Content-merge.** The stamp certifies the exact sheet beneath it and nothing else: its word matches the sheet's state (DECLASSIFIED on the cover, CLEARED on findings, RELEASED on evidence). Counters (§6.7) increment only on stamp-land events, so the paperwork and the certification can never disagree.
- **Failure fallback.** If the animation pipeline fails, stamps render pre-struck at rest state (they are plain styled divs; the slam is a class-triggered transition). If JS is disabled, stamps are present in the static render — a no-JS visitor gets a fully released, fully stamped file.
- **Reduced-motion variant.** Stamps pre-struck, no slam, no sheet dip, bleed halo at its dried state (invisible in light mode). The certification reads statically, which suits the variant: the file arrives already processed.
- **Performance budget & mobile.** One stamp animating at a time by construction; transform/opacity only; the texture mask is a static data-URI (zero network). Mobile: stamp size scales to 0.8×, hero stamp word may wrap to two lines (DECLASS- / IFIED is forbidden — instead reduce font to 1.5rem and let the stamp widen to 78% of sheet width). Sheet dip retained (it is the cheapest, most physical 120ms on the page).

### 6.3 Typewriter dossier line

- **What & why.** The hero cover's subject line — `SUBJECT: WHAT WE FOUND IN YOUR NETWORK IN 30 DAYS` or the site's equivalent — is typed onto the cover character by character, with a blinking block caret. It belongs because the cover sheet is not printed, it is *prepared*: someone in the bureau is typing this file up for release, and the visitor arrives mid-typing.
- **Structure.** A `<p class="typer">` containing a text node typed by script, plus a `<span class="caret">` (0.6em × 1.1em `--carbon` block, §3 law 4). The full line is present in the HTML; the script replaces it progressively. `aria-label` carries the complete line; the typed text node is `aria-hidden` so screen readers hear the line once, whole, not letter by letter.
- **Motion spec.** Typing begins 300ms after load (before the first bar lift at 450ms — the subject is typed, then the release begins). Per-character interval: 34–58ms, randomised per character from a seeded pattern (key strikes are uneven; a metronome is a giveaway), with a 190ms pause at each comma and a 320ms pause before the final word. Caret blinks at 1060ms `steps(1)` throughout. 1.6s after the final character, the caret fades (opacity, 300ms `--ease-bureau`) — the typist has stopped; the file is now the visitor's.
- **States.** *Waiting:* empty line, caret blinking (max 300ms). *Typing:* characters landing, each with a 1-frame 0.5px vertical jitter (the typebar strike). *Done:* full line, caret blinking. *Abandoned:* caret faded, line static forever.
- **Content-merge.** The typed line is the file's actual subject header — the real case name of whatever the page documents. It is set in the document column at body size +2px, exactly where a typed subject line sits on a real cover sheet, preceded by `SUBJECT:` in the same line.
- **Failure fallback.** The line is whole in the HTML; if the script never runs, the whole line is simply there and the caret span is hidden by the no-JS style. If the script errors mid-type, a 2.5s watchdog completes the line instantly.
- **Reduced-motion variant.** Full line present from first paint; no caret (or a static, non-blinking caret removed after 0s — choose removed; a frozen caret reads as a rendering bug).
- **Performance budget & mobile.** One timer chain, ≤60 characters; cost is nil. Mobile: identical, but the subject line may run to 3 lines — typing proceeds across line breaks without pause inflation (the 190/320ms pauses apply to punctuation, not wraps).

### 6.4 Jittered DECLASSIFIED lettering

- **What & why.** Above the hero stamp, the word DECLASSIFIED is itself typed — letter by letter, each letter landing with ±1px typewriter jitter and uneven timing, in Archivo Expanded. The bureau's mark is struck by the same imperfect machine as the file: authority, but human authority. It is the brand signature of the cover sheet.
- **Structure.** The word split into per-letter `<span class="dl">` elements inside an Archivo Expanded 800 line at 2.25rem, `--ink` (the lettering is typed in ink; the *stamp* below it is the green object — do not make the letters green, or lettering and stamp collapse into one gesture). Letters begin at opacity 0, translateY(2px).
- **Motion spec.** Sequenced inside the hero timeline: begins after the subject line finishes (§6.3) and overlaps the last hero bars. Per letter: 90–160ms uneven intervals (seeded pattern, never uniform), landing at 140ms `--ease-thud` at micro scale (this is the one place `--ease-thud` is used below stamp size — a typebar is a small stamp), jitter ±1px horizontal, ±0.5px vertical, rotation ±0.6°. The completed word sits 140ms, *then* the stamp slams (§6.2) — lettering is the inhale, stamp is the blow.
- **States.** *Untyped:* invisible (but see Fallback). *Typing:* partial word — during this ~1.4s the cover reads as a file being prepared, which is the intended first impression. *Complete:* static; the word never animates again.
- **Content-merge.** The lettering is part of the cover sheet's release marking, positioned in the cover's header block between the file number and the stamp. It is not a logo and never appears on inner sheets — inner sheets get stamps only; the full ceremony is reserved for the cover.
- **Failure fallback.** Letters are opacity-0 only via a JS-added class (`js` on `<html>`); without JS the word renders whole. A 3s watchdog after load forces completion of any unlanded letters.
- **Reduced-motion variant.** Word present whole at first paint.
- **Performance budget & mobile.** 12 letters, transform/opacity only, one-shot. Mobile: size drops to 1.75rem; jitter halves (±0.5px) so the word stays legible on small screens.

### 6.5 Censored evidence photographs

- **What & why.** The exhibits' photographs begin as black-bar skeleton placeholders inside manila evidence sleeves, then reveal through a widening viewing slit — as if the photo were slid under the archive lamp — resolving from photocopy blur to sharp, scaling into its frame. On Exhibit B, the censor bar over the subject's eyes lifts *last of all*, after the photo is fully visible: identity is the most sensitive thing in the file, and the theme's sequencing says so.
- **Structure.** `<figure class="sleeve">`: a `--manila-deep` sleeve frame (padding 14px, tab at top-left carrying the exhibit number), inside it the photo in a `--carbon` matte. The photo is clipped by an animated `clip-path: inset(46% 0 46% 0)` → `inset(0 0 0 0)` (a horizontal slit opening from the middle line — the lamp slit). The censor bar over the eyes is a separate `.bar` (§6.1 component) positioned over the photo, plus skeleton bars (static `--carbon` blocks at 88% / 64% / 92% widths) in the caption area that dissolve as the real caption types in. Caption below in Courier italic (§3), then the mini RELEASED stamp (§6.2 at 0.55× scale) in the sleeve's bottom-right margin.
- **Motion spec.** On scroll entry (sleeve centre crossing 58% viewport height): slit opens over 640ms `--ease-bureau`; simultaneously the photo goes blur(6px)→blur(0), contrast .92→1, scale 1.12→1.0 (all 640ms, same easing — one physical event, three properties). Caption skeleton bars dissolve at 480ms. The eye-bar lifts at +520ms (after the photo is essentially open) using the §6.1 peel at 300ms. Mini RELEASED stamp slams at +700ms — the demo-proven delay; the sleeve is certified only after its most sensitive element is released.
- **States.** *Sealed:* slit closed, skeleton bars present, sleeve reads as a black matte in a folder. *Opening:* the 640ms event. *Open, censored:* photo visible, eye-bar still down (a deliberate, readable state — some sleeves may be authored to *stay* in this state; see below). *Released:* eye-bar lifted, stamp landed. *Scrolled-past:* final state persists.
- **Content-merge.** The photographs are the evidence the sheet's text cites — the screenshot of the breach log, the product's actual interface, the podcast's subject. The caption is the evidence's chain label (what it is, when captured, who released it). An author may keep a specific sleeve's eye-bar down permanently — that is §6.12's restraint expressed inside an exhibit, and the caption must then say why ("Subject declined identification. Bar retained.").
- **Failure fallback.** The photo is a normal `<img>` under the clip; no-JS and failure states set `clip-path: none`, no blur, eye-bar rendered as a static bar *beside* the caption's explanation rather than over the photo (with JS off, nothing may cover evidence). The 800ms/7s safety system (§6.1) covers the eye-bar.
- **Reduced-motion variant.** Sleeves arrive open and sharp; eye-bar either lifted (default) or statically placed per authoring; no slit, no blur transition; stamp pre-struck.
- **Performance budget & mobile.** `clip-path` + filter on one image at a time; images are `loading="lazy"`, sized ≤1200px wide, and the blur filter is removed from the element after the transition ends (a lingering filter layer is a scrolling tax). Budget: no more than 2 sleeves animating concurrently, ever. Mobile: the slit opens vertically instead (inset from left/right edges → a portrait photo in a narrow column reads better through a vertical lamp slit), durations unchanged; eye-bar peel uses the §6.1 mobile hinge.

### 6.6 Scroll-scrubbed clearance dial

- **What & why.** In the punched-hole rail, a semicircular gauge whose green arc fills and whose needle sweeps as the visitor's clearance grows with scroll depth; the level label steps LVL 0 → LVL 5 as sheets are certified. It is the theme's progress indicator, and it belongs because progress in an archive is not "34% of page" — it is a *clearance level*, granted by the bureau as the file is read.
- **Structure.** Inline SVG, 56×34px viewBox: a semicircle track (stroke `--ink-faded`, 3px), the progress arc (stroke `--stamp`, 3px, round cap) driven by `stroke-dashoffset`, a needle (1.5px `--carbon` line) rotated about the dial centre, five tick marks, and below it an Archivo Expanded label `LVL n` at 0.6875rem +0.22em tracking, plus the word `CLEARANCE` at 0.5625rem in `--ink-faded`. The dial sits between two punched holes in the rail; the holes are part of its frame.
- **Motion spec.** Pure scrub: arc offset and needle angle are functions of certified progress — defined precisely as *(sheets stamped) + (current sheet's bars lifted fraction)*, mapped onto 0–1 — not raw scroll position. This distinction is the element's soul: scrolling fast without reading (bars unlifted because their sheet never reached reading position… in practice bars lift on entry, so the practical proxy is sheets entered) must not grant clearance the file hasn't given. Values pass through the shared rAF lerp (0.16). The LVL label steps discretely at thresholds 0 / .05 / .25 / .45 / .65 / .85 → LVL 0–5, each step with a 120ms tick (§6.7's digit motion at label scale). Needle has a 1px mechanical tremor at rest (±0.4° sine at 0.7Hz) — a gauge needle is alive; the tremor stops while the value is changing.
- **States.** *LVL 0:* empty arc, needle at rest left, label LVL 0. *In progress:* arc/needle scrubbing, label stepping. *LVL 5:* full arc, needle at right stop, label LVL 5, and the dial's tick at the right stop turns `--stamp` — full clearance is a certified state. *Reduced data / no JS:* see Fallback.
- **Content-merge.** The dial measures this file's release, in the file's own spine. Its denominator is the actual sheet count of the page; on a 4-sheet page LVL 5 still means *this file, fully read*.
- **Failure fallback.** Without JS, the dial renders at LVL 5 with full arc and a static needle, captioned `CLEARANCE — FULL FILE BELOW`: the no-JS document is fully released (§6.1 fallback), so the gauge honestly reports full clearance.
- **Reduced-motion variant.** The dial still updates (it is information, not ornament) but without lerp smoothing — values step — and the needle tremor is removed.
- **Performance budget & mobile.** Two SVG property writes per frame from the shared loop; effectively free. Mobile: the dial becomes a linear gauge in the bottom rail-bar (§4) — a 3px `--stamp` fill bar across the bar's top edge with the `LVL n` label at its right end; same value, same thresholds, no needle.

---

### 6.7 Released-documents counters

- **What & why.** Two counters keep the file's books: the header pill — Archivo Expanded, `DOCUMENTS RELEASED n / 6` — and the rail counter — Courier, `PAGES FREED n`. They exist because a release process that doesn't keep count is theatre; the counters make the visitor's progress an official record, and the two counters deliberately count the same event in the bureau's two voices (the pill is the bureau announcing; the rail is the file noting).
- **Structure.** Pill: `--carbon` field, `--manila-pale` text, border-radius 999px, padding 6px 14px, in the top bar right. Rail counter: plain Courier 700 text under the dial, tabular-nums (§3), with the word `PAGES FREED` in Archivo Expanded 0.5625rem above the digit. The denominator is computed from the actual number of stampable sheets in the DOM at init — hardcoding "6" is a defect; a 4-sheet page must read / 4.
- **Motion spec.** Increment is event-driven only: when a stamp lands (§6.2 impact frame), both counters tick — the digit performs a 120ms `--ease-bureau` vertical slide (old digit exits up, new digit enters from below, clipped by a 1em-high mask) and the pill gives a single 1px `--stamp` outline pulse (outline fades over 400ms). No count-up-over-time, no easing through intermediate numbers: the count changes because a stamp fell, instantly and on the record.
- **States.** *0:* both read zero; the pill is present from first paint (an empty ledger is still a ledger). *Counting:* per stamp. *Complete:* n = denominator; the pill's field turns `--stamp` with `--manila-pale` text — the only place the pill changes colour, and it means the file is fully released. It stays that way; there is no celebration animation. The bureau does not celebrate; it files.
- **Content-merge.** The counters count the very sheets on screen being freed. They are the page's own bookkeeping, rendered in the page's own furniture (top bar, rail) — not a gamification overlay.
- **Failure fallback.** Without JS the counters render complete (`n / n`, pill in `--stamp`): the static file is fully released, so the books honestly show it closed.
- **Reduced-motion variant.** Digits swap instantly, no slide, no pulse. Counts remain exact.
- **Performance budget & mobile.** Two tiny DOM writes per stamp event. Mobile: the pill stays in the top bar (it is load-bearing, §4); the rail counter moves into the bottom rail-bar beside the linear gauge (§6.6 mobile).

### 6.8 Self-drawing evidence line

- **What & why.** In the Chain of Custody sheet, an SVG line draws itself down the punched-hole spine of the sheet, connecting the custody steps — Day 0, Day 3, Day 14, Day 30 — as each is read. The line is the chain: custody is a sequence of handovers, and the line physically links the entries it describes, in the order they happened, at the speed they are read.
- **Structure.** An SVG absolutely positioned along the sheet's left inside margin (the sheet carries a mini-spine of punched holes echoing the rail), one vertical path with small circles at each custody step's baseline. Path drawn via `stroke-dasharray/offset`; stroke `--stamp` 2px — the chain is certified ink, the one continuous green object inside a sheet. Each custody entry is a `.custody` block: day label (Archivo Expanded 0.75rem), entry text (Courier), and the receiving officer's initials in a 28px bordered box (the sign-off).
- **Motion spec.** Scrubbed to the section's own scroll progress: as the sheet's custody block travels from 70% → 30% viewport height, the path's drawn length goes 0 → 100%, linear, through the shared lerp (0.16). Each step's circle fills (`--stamp`) at the moment the line reaches it, with the entry itself uncovered by the ruler-mask reveal (§5) 120ms later — line first, then the entry it points to. Scrolling back up un-draws the line (custody can be re-inspected), but the circles, once filled, stay filled: the record of having read a step is permanent even if the line retreats.
- **States.** *Undrawn:* path invisible, circles hollow (`--ink-faded` stroke). *Drawing:* partial path, circles filling in sequence. *Complete:* full path, all circles filled, the final circle double-ringed (the chain is closed). *Re-scrolled:* path retreats, circles stay filled.
- **Content-merge.** The line is drawn *through* the punched holes of the sheet's own spine and terminates at each entry's sign-off box. It is not a timeline graphic placed near the text; it is the binding of the text.
- **Failure fallback.** No JS: the path renders fully drawn, all circles filled — the static chain is complete, as the static file is complete.
- **Reduced-motion variant.** Path appears in full when the sheet reaches reading position (no scrub); circles fill in sequence at 150ms intervals as their entries are revealed by the static variant of the mask (entries simply present).
- **Performance budget & mobile.** One `stroke-dashoffset` write per frame from the shared loop. Mobile: the spine moves from the sheet's left margin to a 2px line directly left of the entries (margin shrinks); circles 8px; scrub mapping identical.

### 6.9 Crawling photocopy noise + drifting dust

- **What & why.** Two ambient layers give the archive its air. (a) A full-viewport photocopy-noise field — the grain of a much-copied document — crawls in discrete steps, almost imperceptibly. (b) Dust motes drift upward inside the hero, in the pool of the archive lamp. The noise is the texture of the sheets themselves; the dust hangs only where the lamp is. Together they make the page feel *stored* — paper that sat in a box for thirty years.
- **Structure.** Noise: a fixed `::before` layer on the sheet stack container, a repeating 180×180px SVG feTurbulence noise tile at 3.5% opacity, `mix-blend-mode: multiply`, pointer-events none, z-index above paper but below stamps (stamps are struck *over* the grain — the grain is in the paper, the ink is on it; getting this order wrong makes stamps look printed by the same copier, a subtle slop tell). Dust: 14 `<i class="mote">` elements inside the hero sheet's lamp pool (a radial `--manila-pale` gradient region, §2), each 2–3px, `--ink` at 18–30% opacity.
- **Motion spec.** Noise crawl: `background-position` jumps in `steps(6)` every 900ms through a 6-position cycle (offsets of 0–14px) — the grain *shifts* like a copier re-scanning, it never flows smoothly; smooth noise is video static and belongs to another theme. Dust: each mote rises 60–120px over 9–14s, drifting ±10px horizontally on a sine, opacity fading in the first 15% and out in the last 20%, `animation-delay` spread across −14s so the field is mid-life at load. Both layers pause (`animation-play-state`) when their region is off-screen (IntersectionObserver) and the noise respects `prefers-reduced-data` by becoming static.
- **States.** *Running:* as above. *Paused:* off-screen or document hidden. *Static:* reduced-data / reduced-motion fallback states.
- **Content-merge.** The noise layer is clipped to the sheet stack — it does not crawl over the desk or the top bar's brand block; grain belongs to paper. The dust exists only inside the hero's lamp pool. Atmosphere that leaks onto the chrome stops being the file's air and becomes the site's wallpaper.
- **Failure fallback.** Both layers are pure CSS/decorative (`aria-hidden`); if they never render, the document is complete without them. This is the one element family whose total failure is acceptable — which is precisely why it must never be load-bearing.
- **Reduced-motion variant.** Noise static (a still grain field at 3% — the paper texture remains, the crawl stops). Dust removed entirely (drifting particles are the canonical reduced-motion hazard; a static mote is a dirt spot, so they go).
- **Performance budget & mobile.** Noise: one composited fixed layer, transform-free (background-position steps on a small tile are cheap, but cap the layer to the stack's bounding box, not the full viewport, on mobile). Dust: 14 CSS animations, transform/opacity only — the cheapest element on the page. Mobile: mote count drops to 8, rise distance halves; noise tile drops to 120×120px.

### 6.10 Click-to-stamp folders

- **What & why.** Three manila folder cards — the bureau's service files (in the demo: Audit / Watch / Briefing; in production, the organisation's actual three offerings) — tilt on hover like folders lifted by one corner, and on click or Enter the visitor stamps them personally: their own CLEARED stamp slams onto the folder. The visitor performs the site's core ritual on its actual offerings; choosing a service becomes an act of clearance, done by hand.
- **Structure.** `<button class="folder">` (a real button — the whole card is the control) with a folder tab (top-left, `--manila-deep`, carrying the service code `SVC-01`), the service name in Archivo Expanded, a 2-line Courier description, and a reserved stamp zone at bottom-right. Card face `--manila`, edge `--manila-deep`, the same sheet shadow (§4) at half depth. Each folder carries its own stamp instance (§6.2 component at 0.7×) in its stamp zone, initially un-struck. A folder's stamp is *personal*: it reads `CLEARED — BY VISITOR` in the demo's wording; in production, `CLEARED` alone. Once stamped, the folder's link/action activates (the card is a link styled as a folder; stamping is the hover/focus ceremony, activation is the click — do not make stamping a required extra click before navigation; the stamp fires *on* the activating click, 0ms before the folder-gate transition (§6.11) begins, so the sequence reads: stamp → file closes → new sheet).
- **Motion spec.** Hover tilt: the card rotates about its bottom-left corner — the corner a hand would *not* lift — rising at the top-right: rotate −1.2° with a 3px lift of the top-right corner via `transform: perspective(900px) rotateX(2deg) rotateY(−3deg)`, spring-driven (stiffness 170, damping 19, §5) so it settles with one ≤0.4° overshoot. Stamp on activation: §6.2's slam at 320ms `--ease-thud` + card dip scale 0.99 for 120ms. On keyboard focus, the tilt is replaced by a 2px `--stamp` outline (focus must be *more* visible than hover, not a simulation of it).
- **States.** *Rest:* flat in the grid, tab visible. *Hover:* tilted, shadow deepening on the lifted side. *Focus:* outlined, flat. *Stamped:* stamp struck, tab's service code gains a `--stamp` tick. *Active/pressed:* dip mid-stamp. A stamped folder stays stamped for the session (sessionStorage flag) — the visitor's paperwork persists while they browse the file.
- **Content-merge.** The folders are the services. Their descriptions are the real offering copy, their codes are the real service codes, and stamping one is the first step of engaging it. Three folders, never four or six: a bureau offers what it can certify.
- **Failure fallback.** Without JS the cards are ordinary links in manila styling, stamps pre-struck (the file is complete; the services are simply listed, stamped by the bureau instead of the visitor).
- **Reduced-motion variant.** No tilt (cards static), stamp pre-struck on the *selected* folder only after activation with no slam; focus outline unchanged.
- **Performance budget & mobile.** Spring runs on the shared rAF loop, only while a card is hovered. Three cards max. Mobile/touch: no tilt; tap = stamp + gate transition; cards stack 1-up with the tab row becoming a top strip.

### 6.11 Folder-gate page transition

- **What & why.** Moving through the site is moving through one dossier: on a nav click, the file closes — two manila panels swing shut over the current sheet — the destination sheet is brought to the top behind them, and the panels reopen. The transition exists so that navigation never breaks the fiction that there is only one object here, a folder, being handled.
- **Structure.** Two fixed panels, each 50vw × 100vh, `--manila` with a `--manila-deep` inner edge and a punched-hole column along the meeting edge (the folder's spine appears at the centre when closed), hinged at the outer screen edges (`transform-origin: left center` / `right center`). The left panel carries the file number; the right panel carries the classification strip (§5 marquee, static while closed). Panels sit at the top z-layer below the top bar — the bar is the desk's furniture and stays visible; the folder closes *under* it.
- **Motion spec.** Close: 380ms `--ease-file`, panels rotateY from ∓8° (ajar, at rest they are open flat against the screen edges, i.e., invisible) to 0° meeting at centre, with a 60ms overlap where both are moving. At full close: the scroll jump / route change happens (single-page: `scrollTo` the target sheet instantly; multi-page: this transition wraps the navigation and the open phase plays on the new page's load, panels starting closed). Open: 380ms `--ease-file`, reverse. Total ceremony 760ms + jump — the ceiling for a transition the visitor triggers deliberately; anything longer is the bureau wasting the visitor's time.
- **States.** *Open (rest):* panels flat at edges, invisible, `pointer-events: none`. *Closing / closed / opening:* as above; during closed, the centre spine shows the file number and a `RE-FILING…` Archivo label at 0.75rem — 380ms is long enough to read three syllables, no more. *Interrupted:* a second nav click during the ceremony jumps the queue — close completes instantly (80ms), jump, open.
- **Content-merge.** The panels are the folder's covers — same manila, same file number as the cover sheet, the left panel's inside face shows the chain-of-custody mini-list (§6.8's steps as a checklist). The visitor sees the file's own paperwork while the file is closed.
- **Failure fallback.** If the transition script fails or is absent, navigation is a plain anchor jump — instant, unstyled, correct. The gate is a ceremony layered on a working link, never a dependency of it.
- **Reduced-motion variant.** Disabled entirely. Navigation is instant. (A 760ms full-screen swing is exactly what the variant exists to remove.)
- **Performance budget & mobile.** Two transform-only panels; will-change applied only during the 760ms ceremony. Mobile: panels become a single sheet sliding from the bottom (the folder pulled up over the page) — close 300ms, open 300ms, `--ease-file`; the two-panel swing reads as fussy on a narrow screen, and a single pulled sheet keeps the fiction with half the machinery.

### 6.12 The bar that never lifts + finale watermark sweep

- **What & why.** In the finale sheet — the release note — one redaction bar never lifts. Hovering or focusing it shows the tooltip: **"Still classified. Some things stay ours."** Behind the final sheet, as it enters, a giant outlined DECLASSIFIED watermark sweeps across once. This is the theme's closing argument: an archive that releases *everything* is not trustworthy, it is careless. The permanent bar is a real sentence in the release note that stays withheld — restraint as brand voice, placed inside the copy itself, not in a footnote about the copy.
- **Structure.** The permanent bar is a standard `.rx` span whose `.bar` carries the class `.perm` — excluded by name from every lift sequence, the fallback timers, and the 7s safety sweep (§6.1's fallback code must special-case `.perm`; this exclusion is a named, tested line of the build, not an accident of omission). Its sentence underneath is real copy, present in the DOM (screen readers read it — with an `aria-label` on the span announcing "(withheld)" after the sentence, so the withholding is honest to assistive tech too; visual visitors see the bar, AT visitors hear the sentence and its status — both are told the truth in their medium). Tooltip: a `--carbon` box, `--manila-pale` Courier 0.8125rem text (§3), appearing above the bar. Watermark: an Archivo Expanded 800 word DECLASSIFIED at ~18vw, transparent fill, 1px `--ink` stroke at 14% opacity, positioned behind the finale sheet (z-index below the sheet, above the desk), width 140% of the sheet.
- **Motion spec.** Tooltip: fade + 4px rise, 140ms `--ease-bureau`, on hover after a 250ms dwell (a passing cursor must not flash it) and instantly on keyboard focus; dismisses on leave/blur with a 100ms fade. Watermark sweep: as the finale sheet reaches reading position, the watermark translates from −12% to +4% of its width over 1600ms `--ease-file`, once, and rests at +4% — it is a draught moving the light across the desk, not a banner. It never repeats, never loops, and does not re-run on re-scroll.
- **States.** *Bar:* permanently at rest (§6.1's rest state) — hover gives it the edge-light only, pointedly *without* the shiver: this bar is not nervous, it is certain. *Tooltip:* hidden / shown. *Watermark:* pre-sweep / swept (resting).
- **Content-merge.** The withheld sentence sits mid-paragraph in the release note, grammatically load-bearing — the paragraph is written so the missing sentence is *felt* ("…and the name of the engineer who found it stays with us:" — the bar follows the colon). The watermark is the cover's stamp-word at architectural scale, behind the last sheet: the file ends inside its own certification.
- **Failure fallback.** The bar needs no fallback — it is the fallback state of every other bar, worn deliberately. The tooltip is a `title`-attribute-backed custom tooltip: if the custom one fails, the native `title` (same text) still delivers the line. The watermark is decorative; its absence changes nothing.
- **Reduced-motion variant.** Bar unchanged (it is stillness itself). Tooltip appears instantly, no fade. Watermark pre-swept at its resting position, static.
- **Performance budget & mobile.** Tooltip: one opacity/transform transition. Watermark: one transform on one element, once. Mobile: the tooltip triggers on tap (first tap shows the tooltip and does not follow any link — the bar is not a link — second tap dismisses); watermark size caps at 26vw type so the word stays inside the desk margins.

---

### Page-family elements

The six elements every page needs, built in this theme's materials. Same spec discipline as the signature elements.

### 6.13 Navigation — the file index

- **What & why.** Navigation in an archive is a file index: the list of exhibits, in order, with their release state. The primary nav lives in the top bar (section names, Archivo Expanded 0.8125rem, +0.18em) and is doubled by an index strip at the foot of the cover sheet listing every exhibit with its page number — the table of contents a real file carries inside its cover.
- **Structure.** Top bar: brand left; centre-left nav links (max 5 — a file with 9 exhibits is two files); the DOCUMENTS RELEASED pill (§6.7) right. Each nav link carries its exhibit number as a prefix (`02 FINDINGS`). The cover index: a Courier ruled list, one line per sheet — exhibit label, dotted leader, page number — each line a link. The current sheet's index line is underlined (typewriter emphasis, §3 law 2) and its page number is stamped `--stamp` once that sheet is certified.
- **Motion spec.** Nav clicks fire the folder-gate (§6.11). Link hover: a 1px `--carbon` underline draws left-to-right over 180ms `--ease-bureau` — a pencil line being ruled, not a fade. Index lines on the cover reveal with the ruler-mask (§5) as the cover is read. No dropdowns: a file index is flat; sub-navigation, where unavoidable, is a second index block on the relevant sheet, never a flyout.
- **States.** *Rest / hover / focus:* focus ring is a 2px `--stamp` outline offset 2px (consistent across the theme). *Current:* underlined + stamped page number. *Visited sheet:* its index page number stays stamped for the session.
- **Content-merge.** The nav *is* the file's own index — the same exhibit numbers, the same order, the same page numbers as the sheets themselves. If the nav and the sheets could disagree, the build is wrong (§10 gate).
- **Failure fallback.** Plain anchor links; the gate (§6.11) is layered on top and its absence changes nothing.
- **Reduced-motion variant.** Underline appears instantly; gate disabled (§6.11); index lines present without mask reveals.
- **Performance budget & mobile.** Negligible. Mobile: top-bar nav collapses behind a single `INDEX` toggle that opens the cover index as a full sheet sliding from the top (300ms `--ease-file`) — the index is a page of the file, so opening it is turning to the contents page, not opening a "menu".

### 6.14 Hero — the cover sheet

- **What & why.** The hero is the dossier's cover sheet, and it runs the theme's full opening ceremony in miniature: a fully redacted sheet that declassifies itself in the first seconds — subject typed, letters struck, bars peeling in order, stamp slamming — while the visitor watches the file they are about to read being prepared for them. It is the only auto-playing sequence in the theme, and it earns that right by being the thesis of the whole site performed once, up front.
- **Structure.** One sheet (§4), pinned for the first 120vh (§5). Top block: file number line (Courier 700: `FILE 114-K — RELEASE COPY`) and the classification strip (§5 marquee, static until cleared). Title (Archivo Expanded, §3). The typed subject line (§6.3). The jittered DECLASSIFIED lettering (§6.4) above the reserved stamp zone; the stamp (§6.2). Body: 3–5 short Courier paragraphs carrying 4–6 redaction bars (§6.1) — the cover's own summary, partly withheld. Foot: the cover index (§6.13) begins below the fold line of the pinned region, and the lamp pool (radial `--manila-pale` gradient, top-right, 55% of sheet width) carries the dust (§6.9). Scroll cue: not an arrow — the bottom edge of Exhibit A's sheet visible 24px below the cover, sliding up as the pin releases; the next sheet *is* the cue.
- **Motion spec (the full timeline).** t=0: cover lands fully redacted, noise and dust already alive. t=300ms: typing begins (§6.3, ≈2.2s for a typical subject line). t=450ms: first bar lifts; bars lift at 210ms stagger through the typing. Typing ends → DECLASSIFIED letters strike (≈1.4s, §6.4). +260ms after the last bar: the stamp slams (§6.2), sheet dips, counters tick to 1/6, the classification strip starts its marquee. Total ceremony ≈5.5s, but the cover is fully *readable* by ≈2.5s (bars over body text lift early in the order; the lettering and stamp are ceremony layered over an already-legible sheet). Scroll during the ceremony: the pin holds; the ceremony is not scroll-jacked — if the visitor scrolls hard, the pin releases at 120vh regardless and any unfinished ceremony steps complete instantly (bars force-lifted by their timers, stamp struck) — the file never holds the visitor hostage to its own theatre.
- **States.** *Sealed* (first paint) → *releasing* (ceremony running) → *released* (stamp struck, strip running) → *scrolled-past* (cover pinned-then-released, Exhibit A over it; the cover's final state remains visible in the stack beneath).
- **Content-merge.** Every ceremony element operates on the cover's real content: the subject is the case, the bars cover the summary's real sensitive claims, the stamp certifies this cover. There is no decorative layer in the hero at all — remove the file's content and the hero is an empty sheet of manila.
- **Failure fallback.** The full §6.1 fallback stack applies; additionally the ceremony's watchdog: at 7s the global sweep leaves the cover fully released and stamped, whatever happened. No-JS: the complete, released cover, statically.
- **Reduced-motion variant.** No ceremony: cover arrives released and stamped, subject line whole, letters whole, strip static (printed, not scrolling — a static classification strip is still correct bureau furniture), dust absent, noise static. The pin is also disabled — the cover scrolls away naturally; pinning is a motion effect and the variant does not argue.
- **Performance budget & mobile.** The ceremony runs ≤3 concurrent animations by construction (typing timer + one bar lift + ambient). The pin uses `position: sticky`, not JS scroll-locking. Mobile: ceremony identical but the pin shortens to 60vh and the lamp pool shrinks to 40% width; the stamp follows §6.2's mobile sizing. On `prefers-reduced-data`, the noise tile is served at half resolution and dust motes drop to 6.

### 6.15 Cards — exhibit finding cards

- **What & why.** Within findings sheets, individual findings are cards — but a card in an archive is a *evidence slip*: a smaller sheet pinned to the exhibit page, carrying one finding, its severity as a stamped rating, and its own miniature redaction state. (Service offerings use folder cards, §6.10; findings use slips. Two card species, two jobs, never interchanged.)
- **Structure.** Slip: `--manila-pale` face (a slip is newer paper than the sheet it is pinned to — the one place pale is a flat fill, signalling "added later, by the auditor"), `--manila-deep` edge, padding 22px 24px, a pin: an 10px `--carbon` circle with a 2px highlight at top-centre casting a 6px soft shadow. Header row: finding code (Courier 700, `F-03`) + severity stamp (mini stamp component, §6.2 at 0.45×, words: `SEV-2` etc., in `--stamp` only if the finding is *remediated* — an open finding's severity stamp is `--carbon`, because green is earned, §2 law 1; an open SEV stamp in green is a palette violation and a lie). Body: 2–3 Courier lines, the sensitive clause (the vulnerable endpoint, the exposed bucket name) under a §6.1 bar that lifts when the slip reaches reading position.
- **Motion spec.** Slips enter with the ruler-mask reveal (§5) staggered 120ms. Their bars follow §6.1 exactly (380ms `--ease-flick`, 800ms fallback). Pin shadow shifts 1px as the slip's sheet scrolls (parallax at 0.98× — the slip is *on* the sheet, so it moves almost with it; the 2% differential is the pin's looseness). Hover: the slip lifts 2px at the bottom edge only (rotateX 1.5°, origin top — it flexes against its pin) on the §5 spring.
- **States.** *Pinned (rest) / hover-flexed / focused* (2px `--stamp` outline) */ released* (bar lifted) */ remediated* (severity stamp green + a `REMEDIATED` mini-stamp appears at the slip's foot — a slip can be stamped twice across its life, and both stamps stay: the record accumulates).
- **Content-merge.** A slip *is* a finding — code, severity, description, and the withheld technical detail are the finding's real fields. A findings sheet with no real findings has no slips; the component never appears as a generic "feature card" with an icon and lorem copy. Icons are banned on slips: a finding does not have an icon, it has a code.
- **Failure fallback.** Slips render complete, bars pre-lifted per §6.1's stack; the pin is a CSS circle, decorative, its absence invisible.
- **Reduced-motion variant.** No mask reveal, no flex, bars pre-lifted; stamps static.
- **Performance budget & mobile.** Slips per sheet ≤6 (density law, §4). Transforms only. Mobile: slips go 1-up full column width; the pin centres; hover flex is absent (touch), replaced by nothing — a slip on mobile is a still document, which is correct.

### 6.16 Forms — the file request form

- **What & why.** The contact/conversion form is a FOIA-style request form typed onto a sheet: the visitor fills in a bureaucratic document, and submitting it *files* it — the form's own stamp lands on it. For a security firm this is the demo-request; for a podcast, the source-tip form (where the form's promise — "what you type here is handled like evidence" — is the entire point); for a privacy tool, the waitlist. The form performs the theme's trust contract at the exact moment the visitor is asked to trust.
- **Structure.** A sheet (or sheet-section) ruled like a typed form: each field is a label (Archivo Expanded 0.6875rem, +0.2em, e.g. `REQUESTER NAME`) above a Courier input on a ruled line (border-bottom 1px `--ink` at 40%), the input text in Courier Prime 1rem — the visitor types *in the file's own typeface*, so their words enter the document visually. Fields: name, organisation, email, and a `NATURE OF REQUEST` textarea ruled with 3 lines. Required markers are exhibit-style: `(REQUIRED — EXHIBIT A)`. The submit control is a wide Archivo Expanded button styled as an unstamped form box: `FILE THIS REQUEST`.
- **Motion spec.** Focus: the ruled line thickens to 2px `--carbon` and a caret block (§6.3's caret, 0.5em) appears at the field's start — the bureau's typewriter is now taking dictation. Error: the field's label gains a carbon mini-stamp `INCOMPLETE` (struck at §6.2 timing, 0.4× scale) and the line turns `--carbon` dashed — errors are filed, not flashed; no red, ever (§2). Submit: the button disables, a `FILING…` state types out (3 characters per 90ms), then the whole form sheet receives the `REQUEST FILED` stamp (§6.2 full slam at the form's top-right margin) and the submit box re-sets to a static `FILED — REF 114-K-221` line in `--stamp`. The reference number is real (generated from the submission id) or the line reads `FILED` alone — an invented reference format that maps to nothing is a Real Content violation.
- **States.** *Blank / focused / filled* (filled fields keep a 1.5px line — the ink is on the form) */ error* (per-field, as above; errors summarised in a Courier block at the form's head, phrased as a bureau memo: `MEMO: TWO FIELDS REQUIRE COMPLETION BEFORE FILING.`) */ filing / filed* (terminal; the form becomes a read-only copy of itself, values set as text, with a `COPY — YOUR RECORD` note: the visitor is shown their filed request exactly as the bureau holds it).
- **Content-merge.** The form is a document in the same file, ruled with the same lines, stamped by the same stamp. Its fields are the real intake questions; its filed state is the real confirmation. Nothing about it is a skin over a generic form — the confirmation reference, the memo phrasing, and the copy-for-your-record are the theme doing the form's actual jobs in the theme's own voice.
- **Failure fallback.** A plain HTML form with the same labels posts without JS; the filed state is then the server's confirmation page styled as a filed sheet (static stamp). Validation errors render server-side in the same memo format.
- **Reduced-motion variant.** No typing-out of `FILING…` (static text swap), stamp pre-struck on the filed state, caret static while focused (a blinking caret in a focused field is system behaviour and may remain if the OS allows it; the theme adds no blink of its own).
- **Performance budget & mobile.** All states are class swaps; zero continuous animation. Mobile: labels stack above fields full-width; the stamp lands at the form's top-right at 0.7×; textarea rules remain 3 lines; the submit box is full-width, min-height 52px.

### 6.17 Footer — the custody sign-off

- **What & why.** The footer is the back of the file: the chain-of-custody sign-off block printed on the desk side of the last sheet. It records who released the file, who holds it now (the visitor), and where the rest of the bureau lives (the ordinary footer links, filed as cross-references). A site in this theme does not end with a marketing footer; the file is *signed over*.
- **Structure.** On `--desk` (§2), `--manila-pale` Courier text. Three blocks: (1) `RELEASED BY` — the organisation's name, the release date (the site's real last-updated date), and a signature line: the founder's name set in Courier italic — the only signature the theme permits. (2) `RECEIVED BY` — `THE VISITOR`, with the PAGES FREED total for the session set from §6.7's counter (the footer reads the same ledger). (3) Cross-references: the standard footer links (legal, contact, socials) set as a Courier index with exhibit-style numbering, plus the colophon line: `SET IN COURIER PRIME & ARCHIVO EXPANDED — FILE 114-K`. A final `END OF FILE` stamp (static, `--stamp`, −4°) closes the block, right-aligned, overlapping the desk edge of the last sheet by 12px so it strikes across the boundary between paper and desk — the one stamp allowed to land half-off a sheet, because it seals the whole file shut.
- **Motion spec.** Almost none, deliberately: the footer is where motion stops. The `RECEIVED BY` count types in (§6.3 mechanics, 24 characters max) when the footer first reaches reading position — the last typing in the file is the visitor's own receipt being prepared. The `END OF FILE` stamp is static. Everything else is still. After 100 sheets of ceremony, stillness is the ending.
- **States.** *Unsigned* (before reading position: RECEIVED BY line blank) → *signed* (count typed, stamp present). No other states.
- **Content-merge.** Every line is real: the release date is real, the holder count is the session's real ledger, the links are the real links, the colophon names the real typefaces. The footer's fiction is only its framing; its facts are the site's facts.
- **Failure fallback.** Static complete block, count rendered as the full denominator (`RECEIVED BY — THE VISITOR — 6 / 6 PAGES`).
- **Reduced-motion variant.** Count present statically; all else identical.
- **Performance budget & mobile.** One small typing timer, once. Mobile: blocks stack; the END OF FILE stamp centres and no longer overlaps the sheet edge (overlap needs the desk margin mobile doesn't have) — it sits fully on the desk, still sealing the file, just tidier.

### 6.18 Loader — retrieving the file

- **What & why.** Between requesting a page and receiving it, the bureau is *retrieving the file*. The loader is a closed folder cover on the desk with a typewriter line counting the retrieval. It exists for genuine waits only (route loads, heavy exhibit media) — a loader shown for a fast page is a bureau lying about its own slowness.
- **Structure.** Full-desk (`--desk`) field; centred, a closed folder: a `--manila-deep` rectangle (min(420px, 84vw) × 260px) with a tab carrying the file number, its front face `--manila` at the folder's resting −0.3°. On the face: `RETRIEVING FILE 114-K` (Archivo Expanded 0.875rem, +0.2em) and below it the counting line in Courier: `SHEETS RETRIEVED: n` with the §6.3 caret. A thin `--stamp` progress line under the folder — the *only* linear progress bar in the theme, permitted here because retrieval is a machine process, not a reading process.
- **Motion spec.** The count increments as real assets/sheets resolve (the loader counts actual loaded resources mapped to sheet count — never a fake percentage timer; if progress is unknowable, the line reads `RETRIEVING FILE…` with the caret and no number: honest ignorance over fake precision). Folder breathes almost imperceptibly: rotate −0.3° → −0.1° over 2.4s `--ease-bureau` alternate — a folder being held, not an object spinning. No spinner exists in this theme; a rotating loader would be the one generic element the archive refuses to file. Exit: the folder opens — front face rotates up (rotateX −38°, origin bottom, 420ms `--ease-file`) revealing the first sheet beneath, which is the actual page fading in beneath it (opacity 200ms). Total exit ceremony ≤620ms.
- **States.** *Retrieving* (counting) → *opening* (exit ceremony) → *gone*. *Stalled* (>6s): the line gains a memo under it — `RETRIEVAL DELAYED — THE ARCHIVE IS DEEP.` — and at >12s a plain text link `OPEN THE FILE ANYWAY` that forces entry with whatever has loaded (the file opens incomplete rather than never; missing sheets show their §6.5 sealed state and load in place).
- **Content-merge.** The loader is the file's own cover, counting the file's own sheets. Its file number is the page's file number.
- **Failure fallback.** The loader is JS-rendered over a server-rendered page: if JS fails, there is no loader and the page is simply there. The loader can never be the thing that prevents reading.
- **Reduced-motion variant.** No breathing, no opening ceremony: loader fades (opacity 150ms) when ready. The count still counts (it is information).
- **Performance budget & mobile.** One timer + resource observers; the folder is two divs and text. Mobile: folder scales to 84vw; the progress line and count unchanged.

---

## 7. Page application map

The file metaphor survives every page type because every page type *is* a kind of document. The mapping below is prescriptive: a page built outside its row's pattern is off-theme.

**Home — the released file.** The full ceremony (§6.14): cover sheet, findings exhibits, chain of custody, service folders, release note. This is the only page that runs the complete clearance arc LVL 0→5, because it is the only page that is a *complete file*. Sheet budget: 5–6. The home page is the reference implementation of the theme; every other page is an excerpt discipline.

**Listing page (services index, episode index, findings register) — the file index, expanded.** Opens with an index sheet: the cover index (§6.13) grown into the page's main content — each entry a ruled line that expands into an exhibit slip (§6.15) or folder (§6.10) as it reaches reading position. No cover ceremony (no typed subject, no lettering — those belong to covers); entries are pre-released except each entry's single most sensitive line, which carries a bar. A listing page where nothing is withheld reads as a catalogue, not an index — keep one bar per entry. Filters, if the list genuinely needs them, are styled as index tabs (manila tabs along the sheet's top edge, `--manila-deep`, the active tab `--manila` and raised 2px) — never a sidebar of checkboxes; archives are browsed by tab, not faceted by algorithm.

**Detail page (one service, one episode, one finding) — a single exhibit, pulled from the file.** The page is one exhibit sheet at full width with its evidence sleeves (§6.5), its custody block (§6.8 mechanics at small scale: *this* item's history), and its own stamp. The rail dial reads this exhibit's release only. A detail page must answer "why is this in the file?" in its first sheet — a `REASON FOR INCLUSION` Courier block under the heading, written like a filing note. Cross-links at the foot are `SEE ALSO: EXHIBIT C` references, filed-style, never "You may also like".

**About page — the bureau itself.** The one page allowed to step outside the file and describe the office: staff as `OFFICERS OF THE BUREAU` with dossier-style entries (photo in an evidence sleeve, §6.5, with the eye-bar treatment *reversed* — officers are identified, so their photos arrive uncensored but their *personal* lines (direct emails, histories) carry bars that lift on reading: the bureau redacts itself by the same rules it applies to evidence). The About page's stamp is `ESTABLISHED` + the real founding year.

**Contact / checkout equivalent — the request form.** §6.16 is the page. For commerce-flavoured conversions (booking an audit, buying a report), the form gains a `FEE SCHEDULE` exhibit: a ruled Courier table of the real prices, each price line unredacted (an archive that redacts its prices is a scam wearing this theme as a costume — §9). Payment, where it exists, happens on the provider's own sheet (an embedded payment element styled as a clipped-on annex sheet, rotated +0.3°, labelled `ANNEX — PAYMENT, HANDLED BY [PROVIDER]`): the theme admits the annex is foreign paper rather than faking the whole checkout in manila.

**404 / error pages — the misfiled sheet.** A single sheet, mostly empty, stamped `MISFILED` in carbon (not green — nothing is certified here), with the line `THE REQUESTED SHEET IS NOT IN THIS FILE.` and the index (§6.13) below. The humour is procedural and dry, and the exit is the index, not a search box.

**Long-form article / episode page — a transcript.** Sheets are transcript pages; quoted material that was cleared for broadcast lifts its bars on reading; material still under embargo keeps `.perm` bars (§6.12) with a custody note. Audio, if present, is an annex clip (§7, contact annex pattern) labelled with its recording date.

---

## 8. Worked example — Exhibit B, "The Custody Transfer", end to end

One complete section, as it would actually be built, on a cybersecurity firm's home page. The firm audits networks; Exhibit B documents how a client's leaked credential store changed hands before the firm contained it. Every number below is the build number.

**The sheet.** Sheet 3 of 6, rotation −0.15°, resting on the desk 64px below Exhibit A. Top of sheet: exhibit label `EXHIBIT B — CUSTODY TRANSFER, DAY 14` (Archivo Expanded 0.75rem, +0.22em), then H2 `HOW THE KEYS CHANGED HANDS` (Archivo Expanded 700, clamp(1.75rem, 3.4vw, 2.5rem)). Right margin: the reserved stamp zone, empty. The classification strip is present but static — this sheet is not yet cleared.

**The document column.** Three Courier paragraphs (16px/1.65, 62ch measure). Paragraph 1 is plain: how the store was found. Paragraph 2 carries two bars: one over the sentence naming the exact bucket (`the archive sat in a public bucket named [BAR]` — the bar covers the bucket's real name, which the firm has agreed with the client never to print; the bar is honest because the *sentence around it* says exactly what kind of thing is withheld), one over the count of affected accounts (a real number, withheld until reading position because it is the paragraph's payload). Paragraph 3 carries one bar over the containment timestamp. Total bars on the sheet: 3 in body + 1 eye-bar in the sleeve = 4, inside the §4 density budget.

**The evidence sleeve.** Below paragraph 2, right column of the 2-up grid: the screenshot of the bucket's public listing, in its sleeve (§6.5), exhibit tab `B-1`. The subject's account name in the screenshot is eye-barred. Caption, Courier italic: *"Listing as captured, Day 14, 03:12 PKT. Released by the client, Day 21."*

**The custody block.** Left column: three custody entries (Day 0 — store created; Day 14 — found public; Day 21 — contained and rotated), each with initials box, bound by the self-drawing line (§6.8) down the sheet's mini-spine.

**The sequence, as the visitor scrolls.** Sheet top crosses 62% viewport height → the ruler-mask uncovers the exhibit label and H2 (520ms). Paragraph 1 is simply read. Paragraph 2 enters → its two bars lift in document order, 90ms apart, 380ms `--ease-flick` each, edge-light flashing first. The sleeve's centre crosses 58% → slit opens 640ms, screenshot resolving blur-to-sharp, scaling 1.12→1.0 into its matte; at +520ms the eye-bar peels (mobile hinge); at +700ms the mini RELEASED stamp slams at 0.55×. The custody line scrubs down as the block travels 70%→30% viewport height, circles filling Day 0, Day 14, Day 21, each entry ruler-uncovered 120ms after its circle fills. Paragraph 3's bar lifts at reading position. Last bar lifted +180ms → the sheet's CLEARED stamp slams into the right margin (−6° rotation, 320ms `--ease-thud`), the sheet dips to scale 0.99 for 120ms, the header pill ticks to `DOCUMENTS RELEASED 3 / 6` with its 400ms green outline pulse, the rail counter ticks `PAGES FREED 3`, the dial — which has been scrubbing on the strength of sheets 1–2 plus this sheet's lifted fraction — steps its label to LVL 3, and the classification strip along this sheet's top edge begins its 24px/s marquee: this sheet is now, officially, released paper.

**If anything fails.** JS dies mid-sequence: the 800ms timers force the remaining bars, the 7s sweep finishes the sheet, the stamp renders struck, counters render 3/6 statically. The visitor reads the whole exhibit. The ceremony is expendable; the document is not.

---

## 9. Anti-slop — how this theme goes cheap, and the cure

1. **The Halloween version.** Red "TOP SECRET" stamps, coffee-stain PNGs, grunge textures, a typewriter font from a free-fonts site with no tabular figures. *Cure:* the palette has no red and no stains (§2); stamps are green, double-bordered, multiply-blended with an ink-texture mask (§6.2); grain is a 3.5% multiply field, not a texture pack (§6.9). If it looks like a party invitation, it has failed.
2. **Bars as decoration.** Redaction bars sprinkled over text that was never sensitive — bars over adjectives, bars in the nav, a bar as a logo. *Cure:* the rationing laws (§4: ≤9 per sheet; §6.1: a sentence that isn't worth redacting isn't redacted). Every bar must be answerable: *what is under this, and why was it withheld?*
3. **The bar that eats the page.** Bars that never lift because the IntersectionObserver threshold was set for a taller viewport, or a lift animation that throws and strands them. This is the theme's one unforgivable failure. *Cure:* the three-layer fallback (§6.1) is not optional garnish; §10 gates on it with JS disabled, with the observer broken, and with animations throttled.
4. **Everything lifts at once.** A "reveal all" on load that turns the mechanic into a loading animation. *Cure:* reading position (62%) and document order are law (§4, §5 law 2). If the visitor didn't scroll to it, it hasn't been released.
5. **Generic SaaS underneath.** The manila skin over a standard hero-features-pricing template: three icon cards, a logo wall, a gradient CTA. *Cure:* §7's page map and §6.15's icon ban. The structure itself must be documentary — exhibits, custody, index — or the theme is a costume.
6. **Green everywhere.** Stamp green used for links, buttons, and accents until it means nothing. *Cure:* §2 law 1 — green is earned, ~3% of the viewport, and every instance certifies something specific.
7. **The wobbling stack.** Random per-load rotations, sheets at ±2°, parallax that makes text swim. *Cure:* the fixed rotation table (§4), ±0.3° maximum, lerp 0.16 on everything scrubbed. Paper is heavy; heavy things barely move.
8. **Sound-effect thinking.** Whooshes, stamps that bounce like cartoon logos, counters that spin like slot machines. *Cure:* the motion laws (§5) — one thud, one settle, counters tick by event. The bureau is dry. Dry is the style.
9. **The permanent bar as a gimmick.** A `.perm` bar over a sentence that doesn't matter, or three of them. *Cure:* exactly one per page (§6.12), grammatically load-bearing, with the tooltip line verbatim. Restraint only reads as restraint when it costs the copy something.

---

## 10. Quality gate — Redacted Archive

A build may not ship in this theme unless every line passes. Minimum bar: **all** items — this gate has no partial credit, because the theme's failures are trust failures.

**Document integrity**
- [ ] With JavaScript disabled, the entire page reads top to bottom; every stamp is present; counters read complete; no bar covers any text.
- [ ] With the IntersectionObserver deliberately broken, the 800ms per-bar timers and the 7s global sweep still release every non-`.perm` bar.
- [ ] Exactly one `.perm` bar on the page; its tooltip reads verbatim: "Still classified. Some things stay ours."; its underlying sentence is real, load-bearing copy, and its span carries the "(withheld)" aria announcement.
- [ ] Find-in-page finds text under lifted bars; screen reader pass hears each redacted sentence once, in order.

**The mechanic**
- [ ] Bars lift only at reading position (sheet top at 62% viewport height) and only in document order within each sheet — verified by slow scroll and by jump-scroll to mid-page (jump-scroll releases only sheets actually passed through reading position or already above it, in order, without a visible pile-up: force-lift stagger collapses to 30ms for catch-up).
- [ ] Counters' denominator equals the real stampable-sheet count in the DOM; counters change only on stamp-land frames.
- [ ] Dial value derives from sheets stamped + current sheet's lifted fraction, not raw scroll percentage — verified by scrolling to the bottom with a middle sheet's bars artificially held: LVL must not read 5.

**Craft**
- [ ] Rotations match the fixed table; no per-load randomness anywhere (reload the page 3×: rotations, stamp angles, and jitter patterns are identical).
- [ ] `--stamp` green appears only on certifications (§2 law 1) — audit every green pixel on the page and name what it certifies.
- [ ] Stamp texture, multiply blend, and bleed dry-out present; stamps overlap the text block margin as specified, never cover a word a visitor must read.
- [ ] Type check: Courier Prime tabular figures in both counters (digits do not shift width when ticking); no bold inside document body; every H2 carries an exhibit label above and a page number at its sheet's foot.

**Motion & performance**
- [ ] Single shared rAF loop drives dial, line, parallax, watermark, and tilt (inspect: no second loop exists).
- [ ] All animations are transform/opacity/clip-path only; a 4× CPU-throttled scroll through the full page holds 50fps+ with no long task >100ms attributable to theme code.
- [ ] `prefers-reduced-motion` pass: bars pre-lifted (except `.perm`), stamps pre-struck, gate transition and hero pin disabled, dust absent, noise static, dial stepping without lerp.
- [ ] Mobile (≤760px) pass: bottom rail-bar with linear gauge, sheets at ±0.15°, bars peel on the bottom hinge, folder cards untitled by hover, tooltip tap-to-show works, no horizontal scroll from the watermark.

**Honesty**
- [ ] Every withheld sentence is genuinely the kind of thing the organisation would deliberate over; every released number is a real number; the form's filed reference maps to a real submission or the line reads `FILED` alone.
- [ ] Screenshot test (§1): a stranger shown one sheet identifies it as a page from a declassified file without seeing the brand.

*End of Theme 003 — Redacted Archive (Expanded).*

---

## Part II — Deepening (50x standard)

Part I defines what this theme is and how each element behaves. Part II removes the remaining degrees of freedom. For every element in §6 it pins: the choreography to the millisecond, the complete state matrix on desktop and touch, the behaviour at three breakpoint bands, the edge cases and failure modes a builder will actually meet, the accessibility contract, and the exact tokens consumed — so two builders, working separately from this document alone, produce the same file. Per-theme layers follow: the full component inventory (§12), the copywriting voice (§13), three worked examples with scroll timelines (§14), the full-page scroll choreography map (§15), the whole-page performance budget (§16), and the build-order checklist (§17). Where Part II and Part I disagree on a number, Part II wins — it is the later, finer ruling. Nothing in Part II redesigns anything in Part I.

**Breakpoint bands used throughout Part II.** ≥1200px = the full desk (rail, stack, margins as §4). 768–1199px = the narrow desk (rail narrows, sheets widen relative to viewport, 2-up grids hold but tighten). <768px = the carried file (bottom rail-bar per §4's ≤760px rules, which live inside this band; where §4 said ≤760px, read <768px). Motion intensity is stated per band per element; "full" means Part I timings unchanged, "reduced" means the stated trims, never a different character.

---

## 11. Per-element deepening

### 11.1 Peeling redaction bars (§6.1)

**Choreography timeline** — relative to the sheet's reading-position trigger (T0 = sheet top crosses 62% viewport height), for a sheet whose first redacted sentence is in its first paragraph:

| Beat | Time | What happens |
|---|---|---|
| T0 | 0ms | Sheet's IntersectionObserver fires; the sheet's bar queue is armed in document order. No bar moves yet. |
| T0+40ms | 40ms | Bar 1's `--bar-edge` pre-flash: the 1px bottom edge brightens over 24ms (the flash *is* the first 24ms of this window; the remaining 16ms is the marker "gripping"). |
| T0+64ms | 64ms | Bar 1 peel begins: `rotateX 0→−72deg`, origin top, 380ms `--ease-flick`. Underside (`--manila-deep` backface gradient) visible from ~30% of the rotation. |
| T0+154ms | 154ms | Bar 2 pre-flash (90ms stagger from bar 1's peel start). Bars overlap in flight by design — the queue reads as a hand moving down the page, not a turn-taking machine. |
| T0+444ms | 444ms | Bar 1 peel completes; final 15% (last 57ms) fades opacity 1→0; at completion the bar is set `visibility: hidden` and `will-change` is removed. |
| T0+90ms×n | per bar | Bar *n* follows the same pattern at 90ms stagger (hero: 210ms stagger, first bar at load+450ms per §6.1). |
| Hard stop | trigger+800ms per bar | Any bar whose peel has not *completed* by 800ms after its own scheduled start is force-lifted (class swap, transition killed). The timeline above is the ceremony; this line is the law. |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (un-lifted) | Flat `--carbon`, `--bar-edge` bottom pixel, sentence unreadable, cursor: text (the bar is over text, not a control) | Identical; no shiver available |
| Hover | Shiver: `translateX` ±0.6px, 160ms steps, 2 cycles, + edge-light; does not lift the bar early — hovering is curiosity, not clearance | — (no hover) |
| Focus | Bars are not focusable. `focus-within` on the `.rx` span (when the sentence contains a link) gives the bar edge-light only, no shiver | Same via `:focus-visible` on contained links |
| Active | Not an interactive element; no active state exists, by design | First tap on an un-lifted bar fires edge-light flash alone (120ms), then the scheduled lift proceeds — tap never force-lifts out of order |
| Lifting | Peel in progress (see timeline) | Peel on the bottom hinge (`origin 50% 100%`, `rotateX +72deg`) per §6.1 mobile variant |
| Lifted / scrolled-past | `visibility: hidden`; text fully present to find-in-page, selection, and AT. Permanent — never re-redacts | Identical |
| Disabled | No disabled state — a bar is not a control and cannot be disabled; a build that greys a bar has invented a state | Same |

**Breakpoints.** ≥1200: as Part I — peel origin top, ≤40 bars/page, ≤3 lifting concurrently. 768–1199: identical motion; bar overhang trims to −3px horizontal (narrower measure, tighter margins); stagger stays 90ms. <768: bottom-hinge peel; shiver removed; edge-flash on tap retained; stagger compresses to 70ms (shorter columns, faster reading pace); the per-line-fragment bar generation re-runs on orientation change — fragments are rebuilt, mid-lift bars complete instantly rather than re-peeling on the new measure.

**Edge cases & failure modes.** *Slow network / fonts late:* bars are sized from the text they cover — if Courier Prime arrives late and text reflows, bars re-measure on `document.fonts.ready` and on a 300ms-debounced resize; a bar that finds its sentence moved repositions without animating (a jumping bar is worse than a still one). *No canvas/WebGL:* bars never used either — pure CSS 3D transforms; unaffected. *Low-power device:* if the shared loop detects sustained <40fps, peels degrade to a 120ms opacity+`clip-path: inset` wipe (same direction, no 3D layer) — the release still reads as uncovering, and the fallback timers are unchanged. *Content longer than designed:* a sentence wrapping to 4+ lines gets per-fragment bars that lift as one unit (one queue slot, one stagger step) — never four separate peels for one sentence. *Content shorter:* a one-word redaction is still a full bar (overhang −4px makes it a stroke, not a dash). *Scrolling back up:* lifted bars stay lifted (§6.1); bars not yet lifted stay armed — scrolling up never triggers lifts out of order, and fast jump-scroll catch-up collapses stagger to 30ms per §10.

**Accessibility spec.** The sentence text is in the DOM at all times; the bar is `aria-hidden="true"` and purely visual — screen readers read the sentence once, in order, with no announcement of its redaction (the one exception is §6.12's `.perm`, §11.12). Focus order is document order; bars add no tab stops. Contrast: covered text has no contrast requirement (it is not presented); the *bar itself* on `--manila` is ≈9.8:1, so its presence is perceivable to low-vision visitors. Lifted text is `--ink` on `--manila` at 7.4:1. No information is carried by the bar's motion — a visitor who never perceives the peel loses nothing. Touch: bars are not targets; no minimum size applies, but the tap-flash region is the sentence's full line box.

**Tokens consumed.** `--carbon`, `--bar-edge`, `--manila-deep` (peel underside), `--ink` (revealed text), `--ease-flick`, `--line` (fragment rhythm). Element-scoped: `--bar-peel-angle: -72deg` (desktop) / `72deg` (touch band), `--bar-lift-dur: 380ms`, `--bar-stagger: 90ms` (hero `210ms`).

### 11.2 Slamming rubber stamps (§6.2)

**Choreography timeline** — relative to the trigger (hero: last hero bar completes; sheet: last bar of the sheet completes):

| Beat | Time | What happens |
|---|---|---|
| T−260ms→T0 | (hero only) | The reserved margin zone is empty and *reads* empty — the unstamped margin is part of the choreography; do not pre-render a ghost outline of the stamp. |
| T0 | 0ms | Stamp enters at `scale(1.6) rotate(rest−4deg) translateY(−10px)`, opacity 0. |
| T0+60ms | 60ms | Opacity reaches 1 — the stamp is fully visible before it lands; a stamp that fades in *on* the paper reads as printed, not struck. |
| T0+320ms | 320ms | Slam completes (`--ease-thud`, overshoot in the easing's 1.24 control point): stamp at rest rotation/scale. The `--stamp-bleed` halo is at full strength (28% alpha) at this frame. |
| T0+320→440ms | 120ms | Sheet dip: sheet `scale(1→0.99)` over the first 60ms, returns over the next 60ms (`--ease-file`). Impact frame = T0+320; the dip starts on the impact frame, never before. |
| T0+320ms | same frame | Counters tick (§11.7) and, on the cover, the classification marquee starts (§5). All consequences hang off the impact frame, not the animation start. |
| T0+320→1220ms | 900ms | Bleed halo dries: alpha .28→0, linear. In dark mode it dries only to the permanent 40%-strength floor (§2). |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Un-struck | Absent; reserved margin space empty | Identical |
| Hover | Stamps are not controls: no hover state. (A struck stamp inside a link — none exist by design; stamps never sit inside anchors.) | — |
| Focus | Not focusable; no focus state | Same |
| Striking | The 320ms slam (timeline above) | Identical; dip retained |
| Struck (rest) | Multiply-blended ink, texture mask, dried bleed; permanent | Identical |
| Scrolled-past | Unchanged — stamps never un-strike, fade, or re-animate on re-entry | Identical |
| Disabled | No disabled state for sheet stamps. The form's pre-filing stamp zone (§6.16) is simply un-struck — absence, not disability | Same |

**Breakpoints.** ≥1200: stamp 1.5–2.25rem per §3, overlap of the document column ≈18px. 768–1199: stamp scales 0.9×, overlap trims to 10px (the margin is narrower; the stamp must never cover a word — §10 gate). <768: 0.8× per §6.2; hero stamp font floor 1.5rem with width up to 78% of sheet; dip retained at `scale(0.992)` (a full 1% dip on a narrow sheet shifts text visibly — half-depth keeps the thud, loses the wobble).

**Edge cases & failure modes.** *Slow network:* the stamp is a styled div + a data-URI texture — zero network dependency; it can strike before fonts load, but if Archivo Expanded has not arrived the strike waits for `document.fonts.ready` up to a 500ms cap, then strikes in the fallback face (a stamp in the wrong typeface is worse than a stamp 300ms late; a stamp 3s late is worse than either — hence the cap). *No canvas/WebGL:* not used. *Low-power:* slam degrades to a 140ms scale 1.15→1 with no overshoot and no sheet dip; bleed halo skipped (it is a filter-adjacent paint cost). *Content longer/shorter:* a sheet with zero bars (fully open copy) still gets its stamp — fired at reading position +400ms, since there is no last bar to key from; a sheet whose stamp word is long (e.g. `RELEASED — ANNEX`) wraps inside the stamp frame to two lines at 1.25rem rather than shrinking below the §3 floor. *Scrolling back up:* no effect; struck is terminal.

**Accessibility spec.** A stamp is a status announcement and must exist for AT: each stamp carries visually-hidden text or an `aria-label` on its sheet region — the sheet's section has `aria-label` suffix "— cleared" once struck (e.g. the exhibit region is labelled "Exhibit B — Custody Transfer, Day 14 — cleared"). The stamp div itself is `aria-hidden` (the word is visible text; the label carries it to AT without double-reading). Contrast: `--stamp` on `--manila` ≈4.6:1 — stamps are large display text (≥1.5rem bold), passing AA-large; the stamp word is never the sole carrier of the state (the counters and the sheet label double it, §2 law 3). No focus interaction. The slam is never accompanied by sound.

**Tokens consumed.** `--stamp`, `--stamp-bleed`, `--carbon` (mini error stamps, §6.16), `--manila` (stamp sits on paper), `--ease-thud`, `--ease-file` (sheet dip). Element-scoped: `--stamp-dur: 320ms`, `--stamp-dip-dur: 120ms`, `--stamp-bleed-dry: 900ms`, `--stamp-rot` (per-stamp value from the §6.2 fixed table).

### 11.3 Typewriter dossier line (§6.3)

**Choreography timeline** — relative to page load (L0 = load event; the cover ceremony master clock):

| Beat | Time | What happens |
|---|---|---|
| L0 | 0ms | Line renders empty; caret present, blinking (1060ms `steps(1)`). The `SUBJECT:` prefix is static HTML — it is never typed; the bureau pre-prints its form labels. |
| L0+300ms | 300ms | First character lands with its 1-frame 0.5px strike jitter. Typing is the first motion in the file. |
| per char | 34–58ms | Seeded uneven intervals (§6.3). Spaces take the short end (34–40ms) — a typist crosses spaces fast; capitals take the long end (50–58ms) — the shift key costs time. |
| punctuation | +190ms | Added pause after each comma or colon inside the line. |
| final word | +320ms | Pause before the last word begins — the typist reads the line back before finishing it. |
| last char | ≈L0+2.2s typical | For a 45-character subject line: 300 + (45 × ~46ms avg) + pauses ≈ 2.4s worst case. The 2.5s watchdog (§6.3) is calibrated to this: it fires only on genuine stall, never in a healthy run. |
| last char +1.6s | +1600ms | Caret fade begins (300ms, `--ease-bureau`). At fade end the caret is `visibility: hidden`, not removed — layout must not shift by the caret's 0.6em. |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Waiting (0–300ms) | Empty line, caret blinking | Identical |
| Typing | Characters landing with strike jitter; caret blinking at the typing head | Identical; jitter retained (it is sub-pixel and cheap) |
| Hover / focus | The line is not interactive; no states. Selection of typed text is allowed and behaves as normal text selection | Same; long-press selection works on landed characters |
| Done | Full line, caret blinking | Identical |
| Abandoned | Caret faded at +1.6s; line static forever | Identical |
| Scrolled-past | Unchanged; the line never re-types on re-entry | Identical |
| Disabled | No disabled state. If JS is disabled the state is "Done" from first paint (fallback, §6.3) | Same |

**Breakpoints.** ≥1200 and 768–1199: identical. <768: the line may wrap to 3 lines; typing proceeds across wraps with no added pause; per-character jitter halves to 0.25px (on a 360px column a 0.5px strike on a wrapped line reads as blur, not impact); the final-word pause still applies.

**Edge cases & failure modes.** *Slow network:* the line is HTML text — it types even before fonts arrive, but if Courier Prime is pending the typing waits for `document.fonts.ready` with a 600ms cap (typing in the fallback face then reflowing mid-word is the one unacceptable version; past the cap, type in fallback — Courier New's advance width is within 2%, §3 law 5, so the reflow when the real face lands is a ≤2% nudge, absorbed by the ragged-right column). *No canvas/WebGL:* not used. *Low-power:* typing interval flattens to a uniform 40ms and jitter is dropped (timer cost is identical; the saving is paint, not CPU — keep expectations honest). *Content longer than designed:* subject lines are capped at 72 characters at authoring (§13); a longer line truncates the *typing* at 72 and the remainder appears instantly with the last batch — a 6-second typing performance is a defect, not thoroughness. *Shorter:* a line under 20 characters still gets the 320ms final-word pause — brevity does not rush the bureau. *Scrolling back up / re-entry:* no re-type, ever; the hero ceremony is a once-per-load event.

**Accessibility spec.** `aria-label` on the `.typer` carries the complete line; the typed node is `aria-hidden="true"` (§6.3) — AT hears the subject once, whole, at its document position. The caret is `aria-hidden`, decorative. Typing is never the only way the line arrives: the 2.5s watchdog and the no-JS render both deliver it whole. Contrast: `--ink` on `--manila` 7.4:1 at 18px (body +2px per §6.3) — AA and AAA-large. No focus order impact (no tab stop). Under `prefers-reduced-motion` the line is whole at first paint and the caret never renders (§6.3).

**Tokens consumed.** `--ink`, `--carbon` (caret block), `--ease-bureau` (caret fade). Element-scoped: `--type-interval-min: 34ms`, `--type-interval-max: 58ms`, `--caret-period: 1060ms`.

### 11.4 Jittered DECLASSIFIED lettering (§6.4)

**Choreography timeline** — relative to the typewriter line's completion (W0 = last subject character lands):

| Beat | Time | What happens |
|---|---|---|
| W0 | 0ms | The lettering line is invisible (letters at opacity 0 via the `js` gate). The stamp zone below it is empty. The cover's last bars may still be lifting — the lettering overlaps them by design (§6.4). |
| W0+120ms | 120ms | Letter 1 (D) lands: 140ms `--ease-thud` at micro scale, jitter settles at its seeded offset (±1px / ±0.5px / ±0.6°). |
| per letter | 90–160ms | Seeded uneven intervals. The two S's in DECLASSIFIED strike faster (90–100ms — the typist has found the key); the F–I–E–D tail slows (140–160ms — the word is being finished carefully). This rhythm is authored in the seed table, not randomised per load (§10: reload-identical). |
| W0+≈1.4s | ≈1400ms | Letter 12 (D) lands. The word is whole. |
| +140ms | word +140ms | Held beat — the completed word sits (§6.4). |
| next frame | — | The hero stamp slams (§11.2 timeline takes over). Lettering and stamp are one gesture in two acts; nothing else on the cover animates during the held beat. |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Untyped | Invisible (JS-gated); whole word without JS | Identical |
| Typing | Partial word landing letter by letter | Identical |
| Hover / focus / active | Not interactive; no states. Text selection behaves normally once landed | Same |
| Complete | Static forever; never re-strikes | Identical |
| Scrolled-past | Unchanged | Identical |
| Disabled | No disabled state; reduced-motion and no-JS both resolve to "Complete" at first paint | Same |

**Breakpoints.** ≥1200: 2.25rem, jitter full (±1px). 768–1199: 2rem, jitter full. <768: 1.75rem per §6.4, jitter halves (±0.5px / ±0.25px / ±0.3°); intervals unchanged — the ceremony's rhythm is the same at every size; only its amplitude shrinks.

**Edge cases & failure modes.** *Slow network:* letters are spans of text — if Archivo Expanded is late, the strike waits for `document.fonts.ready` (500ms cap, shared with §11.2's stamp rule; lettering and stamp share one font gate so the ceremony never splits across two typefaces). *No canvas/WebGL:* not used. *Low-power:* jitter offsets are pre-computed transforms — the cost is 12 one-shot transitions; no degradation needed or applied. *Content longer/shorter:* the word is fixed (DECLASSIFIED, 12 letters) — a localisation that changes the word re-seeds the interval table proportionally (total strike time stays ≈1.4s ±10%) and never exceeds 16 letters at this size; beyond that, drop to the next type-scale step rather than wrapping. *Scrolling back up:* complete is terminal. *Watchdog:* 3s after load, any unlanded letter is forced landed (§6.4).

**Accessibility spec.** The word is real text in one `<span>` sequence inside a single element with `aria-label="DECLASSIFIED"` — AT reads the word once, not twelve letters. Per-letter spans are `aria-hidden` with the label on the parent. Contrast: `--ink` on `--manila` 7.4:1 at 2.25rem/800 — passes AAA-large. The lettering is never the only place the release state is announced (the stamp and counters double it). No focus, no target size. Reduced-motion: whole at first paint.

**Tokens consumed.** `--ink`, `--ease-thud`. Element-scoped: `--letter-strike-dur: 140ms`, `--letter-jitter-x: 1px`, `--letter-jitter-rot: 0.6deg`.

### 11.5 Censored evidence photographs (§6.5)

**Choreography timeline** — relative to sleeve trigger (S0 = sleeve centre crosses 58% viewport height):

| Beat | Time | What happens |
|---|---|---|
| S0 | 0ms | Slit begins: `clip-path: inset(46% 0 46% 0)` → `inset(0 0 0 0)`, 640ms `--ease-bureau`. Simultaneously blur 6px→0, contrast .92→1, scale 1.12→1.0 — one event, three properties, same easing, same duration (§6.5). |
| S0+0→480ms | 480ms | Caption skeleton bars (88% / 64% / 92% widths) dissolve over 480ms `--ease-bureau`; the real caption is beneath them and is revealed by the dissolve, not typed. |
| S0+520ms | 520ms | Eye-bar peel begins (§11.1 mechanics at 300ms duration, expedited stagger of one). The photo is 81% open at this frame — identity is released into a nearly-complete picture, never into the slit. |
| S0+640ms | 640ms | Slit fully open; blur filter is *removed* from the element at this frame (not left at blur(0) — a resident filter layer taxes every subsequent scroll frame, §6.5). |
| S0+700ms | 700ms | Mini RELEASED stamp slams (0.55× §11.2 timeline: 320ms slam scaled, bleed halo at half alpha). |
| S0+1020ms | 1020ms | Sleeve fully released and at rest. Total event ≈1.02s — the longest single-element ceremony in the theme, rationed to exhibits. |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Sealed | Slit closed; black matte in sleeve; skeleton bars over caption; eye-bar down | Identical |
| Hover | No hover state on the sleeve itself; the eye-bar, if un-lifted, shows §11.1's shiver on hover | — |
| Focus | The sleeve figure is not focusable; a sleeve containing a link (to the full exhibit) shows the theme focus ring on the link only | Same |
| Opening | The 640ms event (timeline above) | Vertical slit variant (below) |
| Open, censored | Photo visible, eye-bar down — a deliberate authored state for retained bars (§6.5); caption must state why | Identical |
| Released | Eye-bar lifted, mini stamp struck | Identical |
| Scrolled-past | Final state persists; no re-sealing | Identical |
| Disabled | No disabled state; an image that fails to load shows its alt text in the matte with the slit pre-opened (see edge cases) | Same |

**Breakpoints.** ≥1200: horizontal slit, sleeves in the 2-up grid (§4). 768–1199: horizontal slit retained; sleeve padding trims 14px→10px; the eye-bar peel keeps the top hinge. <768: slit opens vertically (inset from left/right edges) per §6.5; sleeves 1-up; eye-bar uses the bottom hinge (§11.1 touch rule); the mini stamp scales 0.5× and sits inside the sleeve's bottom edge rather than overlapping the matte (no margin to overlap into).

**Edge cases & failure modes.** *Slow network:* the image is `loading="lazy"`; the slit does not begin until the image's `load` event *or* 1200ms after S0, whichever first — if the image is still in flight at 1200ms, the slit opens onto the matte with the caption's skeleton bars held, and the photo fades in (opacity 200ms) when it arrives; an exhibit that performs its ceremony at an empty frame is slop. *Broken image:* alt text renders in Courier italic inside the matte, slit pre-opened, eye-bar omitted entirely (nothing to censor), stamp still lands — the custody record of a missing photograph is still a record. *No canvas/WebGL:* not used (clip-path + filter only). *Low-power:* blur is the expensive property — on the shared loop's <40fps signal, the reveal degrades to clip-path + scale only, blur held at 0 throughout (a sharp photo through a widening slit loses little). *Content longer/shorter:* a portrait photo in a landscape matte is `object-fit: cover` with `object-position` authored per sleeve — never `contain` (letterboxed evidence looks like a screenshot, not a photograph); a sleeve with no photo (a document facsimile instead) uses the same slit with the blur at 3px (paper resolves faster than film). *Scrolling back up:* sleeves never re-seal; scrolling up mid-opening lets the event finish (interrupting a 640ms reveal to reverse it is the jitter §5 law 4 exists to prevent).

**Accessibility spec.** The `<img>` carries real alt text describing the evidence ("Screenshot of the public bucket listing, Day 14 — account name withheld") — alt text states the withholding where the eye-bar performs it. The figure's `figcaption` is the custody caption (§6.5) and is associated via `figure` semantics natively. The eye-bar is `aria-hidden`; the *caption* states retention where authored ("Subject declined identification. Bar retained."). Contrast: caption `--ink` italic on `--manila-deep` sleeve — the caption sits on the sleeve's tab strip in `--ink` at 15px italic; measured on `--manila` portion of the sleeve ≥7:1 (captions are set on the sleeve's manila inner slip, never directly on `--manila-deep`, where `--ink` would fall to ≈2.4:1 — this placement is a gate item). Focus: none added. Touch targets: a sleeve is not a target; if the whole sleeve links to a detail page, the link wraps the figure and its target is the full sleeve (≥120×120px in practice, well above minimums).

**Tokens consumed.** `--manila-deep` (sleeve), `--carbon` (matte, eye-bar via §11.1), `--ink` (caption), `--stamp` (mini stamp via §11.2), `--ease-bureau`. Element-scoped: `--slit-dur: 640ms`, `--photo-blur-from: 6px`, `--photo-scale-from: 1.12`.

### 11.6 Scroll-scrubbed clearance dial (§6.6)

**Choreography timeline** — the dial is scrubbed, so its timeline is a value map, not a clock. Beats are defined on the certified-progress value *p* = (sheets stamped + current sheet's lifted fraction) / total sheets (§6.6):

| Beat | Value | What happens |
|---|---|---|
| p = 0 | LVL 0 | Arc empty, needle at left stop, tremor running (±0.4°, 0.7Hz sine). |
| p crosses .05 | LVL 1 | Label tick: 120ms digit motion (§11.7 mechanics at label scale). Tremor pauses for 300ms around the step — the gauge "registers" the new level. |
| p crosses .25 / .45 / .65 | LVL 2 / 3 / 4 | Same tick + tremor pause per step. Arc and needle move continuously between steps (lerp 0.16); only the *label* is discrete. |
| p crosses .85 | LVL 5 | Label ticks to 5; the right-stop tick mark turns `--stamp` (the dial's only colour event besides the arc). |
| p = 1.0 | Full | Needle rests against the right stop; tremor stops permanently — a fully granted clearance is still. The dial is done; nothing on it ever moves again this page. |
| Any frame | — | Arc `stroke-dashoffset` and needle rotation are written once per rAF frame from the shared loop, only when *p* has changed by >0.0005 since the last write — an idle dial costs zero DOM writes. |

**State matrix.**

| State | Desktop | Touch (linear gauge, §6.6 mobile) |
|---|---|---|
| Rest (LVL 0) | Empty arc, needle left, tremor on | Empty 3px track, `LVL 0` label at right |
| Hover | The dial is not a control; hovering the rail does nothing to it. (A tooltip naming the current sheet — "CLEARANCE — EXHIBIT B IN REVIEW" — appears after 600ms dwell on the dial itself; it is the rail's only tooltip.) | — |
| Focus | Not focusable; the dial is a status readout, exposed to AT as text (see accessibility) | Same |
| Active | No active state | Same |
| Scrubbing | Arc/needle lerping toward *p*; tremor off while Δp > 0 per frame | Fill bar width lerps identically; label steps at the same thresholds |
| Complete (LVL 5) | Full arc, needle at right stop, right tick green, tremor off | Fill full `--stamp`, label `LVL 5` |
| Scrolled-past / back up | *p* derives from stamps + lifted fraction, both monotonic — scrolling up never lowers the dial. (Contrast §6.8's line, which does retreat: the line is a path being re-inspected; clearance, once granted, is not revoked by looking away.) | Identical |
| Disabled | No disabled state. No-JS renders the terminal state (LVL 5, full arc — §6.6 fallback) | No-JS: full fill, `LVL 5` |

**Breakpoints.** ≥1200: full SVG dial (56×34) in the rail at 38% viewport height (§4). 768–1199: dial shrinks to 44×27 viewBox units rendered at 44px wide; tick labels (the five tick marks) remain, numerals were never present; tremor amplitude halves (±0.2°) — a smaller needle trembling at full amplitude reads as vibration, not life. <768: linear gauge per §6.6 — 3px `--stamp` fill across the bottom rail-bar's top edge, `LVL n` at its right end in Archivo Expanded 0.625rem; the fill is the arc unrolled, same value, same thresholds, same label tick (the label slides 120ms on step).

**Edge cases & failure modes.** *Slow network:* the dial is inline SVG — present at first paint; its value inits from the DOM's stampable-sheet count (§6.7), so a page whose images are still loading already has a correct gauge. *No canvas/WebGL:* not used. *Low-power:* lerp is dropped first (values step per §6.6's reduced-motion treatment) — the dial is the cheapest scrubbed element and the last to degrade; tremor is cut before lerp (a sine write per frame for ±0.4° is the definition of dispensable). *Content longer/shorter:* sheet count is read from the DOM, so a 9-sheet investigation page and a 3-sheet landing page both map LVL 5 to *their* full file; thresholds are fractions, not sheet counts, so they never need re-authoring. *A sheet with no stamp* (authoring error): the dial's denominator excludes it only if it also lacks the stamp zone — the build lints this (§17), because a denominator that can never reach 1.0 strands the dial at LVL 4 forever, the gauge equivalent of a bar that never lifts. *Scrolling back up:* monotonic, above.

**Accessibility spec.** The dial is a `role="meter"` element with `aria-label="Clearance level"`, `aria-valuemin="0"`, `aria-valuemax="5"`, and `aria-valuenow` updated **only at LVL steps** (not per frame — a scrubbing aria value is announcement spam). `aria-valuetext` reads "Level 3 of 5 — Exhibit C in review". The visible `LVL n` text is `aria-hidden` (the meter carries it). Contrast: arc `--stamp` on `--manila-deep` rail ≈2.9:1 — acceptable for a non-text graphic whose state is doubled by the text label (WCAG non-text contrast is met via the label + needle position; the needle `--carbon` on `--manila-deep` is the high-contrast carrier at ≈4.1:1 against the rail's deep tone… measured honestly: the dial sits on the rail's `--manila-deep` strip; the SVG's own background disc is `--manila`, restoring the §2 ratios — arc 4.6:1, needle 9.8:1 — the disc is mandatory, not decorative). Touch: the gauge is not a target. Focus: none.

**Tokens consumed.** `--stamp` (arc, right tick), `--ink-faded` (track), `--carbon` (needle), `--manila` (dial disc), `--manila-deep` (rail), `--ease-bureau` (label tick via §11.7). Element-scoped: `--dial-lerp: 0.16`, `--dial-tremor: 0.4deg`, `--lvl-thresholds: 0 .05 .25 .45 .65 .85`.

### 11.7 Released-documents counters (§6.7)

**Choreography timeline** — relative to a stamp's impact frame (F0 = §11.2 T0+320ms):

| Beat | Time | What happens |
|---|---|---|
| F0 | 0ms | Stamp lands. In the same frame, both counters begin their tick — the paperwork is simultaneous with the act it records; a counter that ticks *after* the stamp reads as a score, not a record. |
| F0→F0+120ms | 120ms | Digit slide: old digit exits upward, new digit enters from below, clipped by the 1em mask, `--ease-bureau`. Both counters (pill and rail) tick in the same 120ms window. |
| F0→F0+400ms | 400ms | Pill outline pulse: 1px `--stamp` outline fades in by F0+80ms, out by F0+400ms. The rail counter has no pulse — the file notes; the bureau announces (§6.7). |
| Final stamp | F0 | On the tick that reaches the denominator: pill field turns `--stamp`, text stays `--manila-pale`. No pulse, no extra motion — the colour change *is* the event, and it is permanent. |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Zero | Pill present, `DOCUMENTS RELEASED 0 / n`; rail `PAGES FREED 0` | Pill in top bar; rail counter in bottom bar beside the gauge (§6.7 mobile) |
| Hover / focus | Counters are not controls; no states. The pill is never a link (a counter that navigates is a scoreboard, not a ledger) | Same |
| Active | None | Same |
| Ticking | The 120ms digit slide (above) | Identical |
| Complete | Pill green field; rail digit at denominator | Identical |
| Scrolled-past | Unchanged; counters are page-global furniture, identical from every sheet | Identical |
| Disabled | No disabled state. No-JS: both render complete (`n / n`, pill green) per §6.7 fallback | Same |

**Breakpoints.** ≥1200: pill in top bar right; rail counter under the dial. 768–1199: pill text shortens — the words `DOCUMENTS RELEASED` hold (they are the meaning) but tracking tightens to +0.14em and size to 0.6875rem; if the top bar still overflows, the brand's file number (not the counter) is what truncates. <768: pill stays (load-bearing, §4) at 0.625rem; rail counter sits in the bottom bar right of the gauge label; the two counters remain synchronised to the same event — mobile never shows one ticked and the other not.

**Edge cases & failure modes.** *Slow network:* counters are text; they render at first paint with denominator computed at DOMContentLoaded from the stampable-sheet count — before images, before fonts (digits in fallback mono are tabular enough not to embarrass). *No canvas/WebGL:* not used. *Low-power:* digit slide degrades to an instant swap (the §6.7 reduced-motion treatment) before anything else on the page degrades — counters are information, and their cheapest form is their clearest. *Content longer/shorter:* denominator from DOM (§6.7) — a page that gains a sheet via CMS gains the count automatically; a hardcoded denominator is a §10 gate failure. *Double-fire:* stamp-land events are idempotent per sheet (a sheet's stamp event carries its sheet id; a second event for the same id is ignored) — re-entry, re-render, or a hydration remount must never double-count; the ledger is the one place a duplicate is a lie. *Scrolling back up:* counts never decrease.

**Accessibility spec.** The pill is `role="status"` with `aria-live="polite"` — but announcements are throttled: the live region announces only the *completed-file* state ("All 6 documents released") and nothing per tick; per-tick announcements would interrupt reading six times a page. The rail counter is `aria-hidden` (a duplicate of the pill's information in the file's other voice — AT gets one ledger, not two). Visible text contrast: pill `--manila-pale` on `--carbon` ≈9.1:1; complete state `--manila-pale` on `--stamp` ≈4.9:1 at 0.75rem bold — AA for large/bold text; the rail digit `--ink` on `--manila-deep`… the rail counter sits on the rail strip; §11.6's disc rule applies in spirit: the counter's text is `--ink` set on a `--manila` chip inset in the rail (the file's label pasted on the spine), restoring 7.4:1. Tabular numerals are mandatory (§3) so the tick never shifts the pill's width — a layout shift on every stamp is a visible defect at the top of every viewport.

**Tokens consumed.** `--carbon` (pill field), `--manila-pale` (pill text), `--stamp` (pulse, complete field), `--ink` (rail digit), `--manila` (rail chip), `--ease-bureau`. Element-scoped: `--tick-dur: 120ms`, `--pulse-dur: 400ms`.

### 11.8 Self-drawing evidence line (§6.8)

**Choreography timeline** — scrubbed to the custody block's travel; beats are positions, not times (block top crossing viewport percentages):

| Beat | Position | What happens |
|---|---|---|
| Block top at 78% vh | Pre-arm | Path at 0%, circles hollow. Nothing has happened yet — the chain is below the reading zone. (Part I §6.8 arms the scrub at 70%; the 78% beat is where the *first circle* becomes visible, 8 points before the draw begins, so the visitor sees the destination before the journey — a chain whose head is invisible reads as a decoration loading.) |
| Block top at 70% vh | Draw start | Path begins extending from the first punched hole, linear with scroll, through the shared lerp (0.16). |
| Line reaches step *k*'s baseline | Fill + uncover | Step *k*'s circle fills `--stamp` (single frame, no transition — ink is ink). 120ms later the entry's ruler-mask begins (§5: 520ms `--ease-file`). Line first, entry second — always. |
| Block top at 30% vh | Draw complete | Path at 100%; final circle double-ringed (the second ring is drawn in the last 4% of travel, not stamped — it closes as the line arrives). |
| Scroll back up | Retreat | Path un-draws at the same scrub rate; circles stay filled (§6.8); entries stay uncovered (a read entry never re-covers — only the line retreats, because the line is the *inspection*, the entries are the *record*). |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Undrawn | Path invisible, circles hollow `--ink-faded` stroke | Identical (line at entries' left, §6.8 mobile) |
| Hover | Entries are text; no hover state. A custody entry containing a link uses the standard link treatment | Same |
| Focus | The line is not focusable; entries' sign-off boxes are not controls | Same |
| Drawing | Partial path; circles filling in sequence; entries uncovering 120ms behind their circles | Identical scrub |
| Complete | Full path, all circles filled, final circle double-ringed | Identical |
| Re-scrolled | Path retreated (possibly to 0), circles filled, entries open | Identical |
| Disabled | No disabled state. No-JS: path fully drawn, circles filled (§6.8 fallback) | Same |

**Breakpoints.** ≥1200: line in the sheet's left inside margin over the mini-spine holes (§6.8). 768–1199: margin narrows; line moves 12px closer to the entries; circles 9px (from 10px); scrub window unchanged (70%→30% — viewport-relative, so it self-adjusts). <768: line sits 2px left of the entries (§6.8 mobile), circles 8px; the double-ring on the final circle becomes a filled centre dot inside the ring (at 8px a double ring is mud); scrub window widens to 75%→25% because a phone viewport shows less of the block at once — the chain needs more travel to tell the same story.

**Edge cases & failure modes.** *Slow network:* the line is inline SVG; no dependency. *No canvas/WebGL:* not used. *Low-power:* the line is one `stroke-dashoffset` write per frame — the last scrubbed element to degrade; if the loop sheds load, the line's updates quantise to 4% steps (still smooth enough at chain scale) before anything is cut. *Content longer than designed:* more custody steps than the design's four — the path is generated from the entries' actual baselines at init (measured, not hardcoded), so 7 steps draw correctly; beyond 9 steps the sheet should split (§4 density), and the line still works — it just documents a chain that should have been two exhibits. *Shorter:* a 2-step chain still draws (a handover is a chain of two); a 1-step "chain" is not a chain — the line is omitted at authoring and the entry stands alone with its sign-off box. *Scrolling back up:* retreat behaviour above; note the asymmetry is deliberate and is the element's thesis (§6.8).

**Accessibility spec.** The SVG is `aria-hidden` — the chain's sequence is carried by the entries themselves, which are a real ordered list (`<ol>`) in the DOM; AT receives Day 0 → Day 3 → Day 14 → Day 30 as list semantics, which is the line's entire information content in a better form. Circle fills are never announced. Contrast: the drawn line `--stamp` on `--manila` 4.6:1 (non-text graphic, doubled by list order); hollow circles `--ink-faded` stroke 3.9:1 — decorative until filled, and their state is doubled by the entries' revealed text. Focus: none added by the line; entry links keep document order. Touch: no targets.

**Tokens consumed.** `--stamp` (path, fills), `--ink-faded` (hollow circles), `--manila-deep` (mini-spine holes), `--ease-file` (entry masks, via §5). Element-scoped: `--chain-scrub-from: 70%`, `--chain-scrub-to: 30%`, `--chain-stroke: 2px`.

### 11.9 Crawling photocopy noise + drifting dust (§6.9)

**Choreography timeline** — ambient, so the timeline is a cycle spec, not a sequence:

| Beat | Time | What happens |
|---|---|---|
| First paint | 0ms | Noise field is present and *static* for the first 900ms — the page opens as a still document; the first crawl step lands only after the eye has settled. A grain that moves on the first frame reads as a loading glitch. |
| Every 900ms | cycle | Noise `background-position` jumps to the next of 6 authored offsets (0–14px range) via `steps(6)` — discrete re-scans, never a glide (§6.9). The cycle is a CSS animation; it is not driven by the shared rAF loop (a 900ms step does not need a 60fps loop, and keeping it out of the loop is part of §16's frame budget). |
| Load −14s→0 | pre-roll | Dust motes carry negative delays spread across their full 9–14s durations, so at first paint the field is mid-life: some motes near the pool's floor, some near its ceiling, none all starting at the bottom in a row. |
| Per mote | 9–14s loop | Rise 60–120px, ±10px sine drift, opacity in over the first 15%, out over the last 20%, then reset to the pool floor invisibly (opacity 0 at both ends of the loop — a mote that pops is a defect). |
| Region exit | event | Both layers pause (`animation-play-state: paused` via IntersectionObserver on the hero / stack container) within one frame of leaving the viewport, and — for noise — whenever `document.hidden` is true. |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Running | Noise stepping, dust rising (hero only) | Running; motes 8, rise halved (§6.9 mobile) |
| Hover / focus / active | None — the layers are `pointer-events: none` and unfocusable by construction | Same |
| Paused | Off-screen or tab hidden: both layers frozen mid-state | Same |
| Static | `prefers-reduced-data`: noise frozen at cycle position 0; dust still runs (data preference is not a motion preference — do not conflate them) | Same |
| Scrolled-past | Hero dust pauses when the hero leaves; noise continues only while the stack is on screen | Same |
| Disabled | `prefers-reduced-motion`: noise static at 3%, dust removed entirely (§6.9). Total failure of either layer is acceptable (§6.9) — the document is complete without air | Same |

**Breakpoints.** ≥1200: noise tile 180×180 at 3.5% over the stack's bounding box; 14 motes. 768–1199: tile 150×150; motes 10. <768: tile 120×120 (§6.9), layer clipped to the stack box (never full-viewport on mobile — the fixed layer's paint cost is the one place this element can hurt), motes 8, rise distance halved, drift ±6px.

**Edge cases & failure modes.** *Slow network:* the noise tile is an inline SVG data-URI — zero requests; dust is DOM/CSS — zero requests. This element must be fully alive on a page whose images have not arrived; atmosphere that waits for the network is a loading screen in disguise. *No canvas/WebGL:* not used. *Low-power:* noise is the first thing frozen (static grain, §16 cut order) and dust the second (count halved, then removed) — both are declared expendable in §6.9 and Part II spends them first. *Content longer/shorter:* the noise layer sizes to the stack container, so a 9-sheet page grains all 9 sheets and the desk stays clean (§6.9 content-merge); a very short page (one sheet) still gets its pool and motes — the lamp pool is positioned on the hero sheet, not the page. *Scrolling back up:* returning to the hero resumes the dust from its paused positions (CSS animations resume, they do not restart — a field that resets on re-entry betrays the pause).

**Accessibility spec.** Both layers are `aria-hidden`, `pointer-events: none`, and carry no information — there is nothing to label. The noise's 3.5% multiply must not drop any text below its §2 ratio: the ratios in §2 are measured *with the grain on* (grain over `--manila` lightens carbon fields by <2% luminance — the 7.4:1 body ratio is post-grain; a build that measures without the grain and ships 7.35:1 effective has still passed, but one whose grain pushes `--ink-faded` display text under 3:1 has not — the gate measures the rendered page, §10). Dust motes never cross the document column's text (the pool is positioned in the sheet's margin/lamp region, §6.14) — moving objects over reading text are a vestibular and legibility hazard, and the pool's placement is the fix, not a preference.

**Tokens consumed.** `--manila-pale` (lamp pool gradient), `--ink` (motes, at 18–30% opacity), `--carbon` (grain is a multiply field — its effective tone derives from the paper + grain, no colour token; stated here so a builder does not invent one). Element-scoped: `--noise-opacity: .035`, `--noise-cycle: 900ms`, `--mote-count: 14`, `--mote-rise: 9s–14s`.

### 11.10 Click-to-stamp folders (§6.10)

**Choreography timeline** — two timelines: the hover spring (desktop) and the activation sequence (both platforms). Activation, relative to the click/Enter (A0):

| Beat | Time | What happens |
|---|---|---|
| A0 | 0ms | The folder's own stamp begins its slam (§11.2 at 0.7×: enter at scale 1.42 relative, 320ms `--ease-thud`). Simultaneously the card dip begins its anticipation: nothing yet — the dip starts at impact, as always. |
| A0+320ms | 320ms | Stamp impact: card dips `scale(0.99)` for 120ms (§11.2 pattern); the tab's service code gains its `--stamp` tick in the same frame. |
| A0+320ms | same frame | The folder-gate (§11.11) begins closing. The visitor's last sight of the services sheet is their own stamp landing on the folder they chose — stamp, then file closes, then new sheet (§6.10). |
| Return visit | session | If the visitor navigates back this session, the folder is already stamped (sessionStorage, §6.10): no slam replays; the stamp is simply there, dried. |

Hover spring (desktop, pointer-driven, no fixed clock): pointer enter → spring (stiffness 170, damping 19) drives `perspective(900px) rotateX(2deg) rotateY(−3deg)` + shadow deepen; one overshoot ≤0.4°; settle ≈420ms. Pointer leave → spring returns to flat on the same constants (a return with different constants feels like a different material).

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Flat in grid, tab visible, stamp zone empty (or stamped, if session flag set) | Identical |
| Hover | Tilted spring state (above), shadow deepening on the lifted (top-right) side | — (no hover; first tap *is* activation) |
| Focus | Flat, 2px `--stamp` outline offset 2px — focus is *more* visible than hover and never simulated tilt (§6.10) | Focus via switch/keyboard: same outline |
| Active / pressed | Dip mid-stamp (A0+320ms window); before impact, a 60ms `scale(0.995)` press anticipation | Tap: stamp + gate, no tilt, no anticipation dip (the stamp's own dip suffices) |
| Stamped | Stamp struck at rest, tab code ticked green; persists for the session | Identical |
| Scrolled-past | Unchanged by scroll; a folder entering the viewport gets no entrance motion beyond its sheet's own reveals | Identical |
| Disabled | A folder whose service is unavailable is not rendered as a disabled button — it is rendered as a folder *without* a link, its stamp zone carrying a carbon mini-stamp `FILE CLOSED` and its description stating why (§13 voice). A greyed-out folder button is SaaS, not archive | Same |

**Breakpoints.** ≥1200: 3 folders in the sheet's 2-up-plus grid per §4 (3 across at full desk width inside the sheet's padding — the sheet is 880px max, so in practice 3 folders sit in one row of thirds at ≥1200 viewport, two-plus-one at the narrow band). 768–1199: folders go 1-up stacked at full column width (a 400px folder in a 600px column wastes the sheet; a full-width folder reads as a file pulled from the drawer — better fiction, better target). Tilt retained (pointer assumed). <768: 1-up, tab becomes a top strip (§6.10 mobile), no tilt, stamp 0.65×, card min-height ensures the stamp zone never collides with the description (description clamps at 3 lines in this band).

**Edge cases & failure modes.** *Slow network:* folders are styled anchors — they navigate with zero JS; the stamp ceremony layers on top (§6.10 fallback) and its absence changes nothing about the link. *No canvas/WebGL:* not used. *Low-power:* the tilt spring is the cost — on the loop's <40fps signal the spring is replaced by a 120ms `--ease-bureau` tween to the same end pose (same destination, cheaper road); the stamp slam never degrades here (it is the theme's core event, §11.2's degradation rules apply instead). *Content longer than designed:* a service description over 3 lines clamps with the ruled fade (last line fades to `--manila` over its final 3ch — a typed page running out of room, not an ellipsis in a sans font; `…` set in Courier is also acceptable and simpler — choose the ellipsis: the fade is a photographic effect in a typewriter world). *Shorter:* a one-line description leaves the stamp zone where it is (bottom-right, fixed) — folders in a row keep equal heights so their stamp zones align like files in a drawer. *Scrolling back up:* no state change; stamped folders stay stamped. *sessionStorage unavailable* (private mode): the flag falls back to a JS variable — stamps persist for the page's life, not the session; acceptable degradation, never an error state.

**Accessibility spec.** Each folder is a real `<button>` or `<a>` (link, since it navigates — §6.10: a real button was specified for the demo's in-page action; production folders navigate, so they are links styled as folders, with the stamp ceremony on click; if a build uses them as in-page actions, buttons — the rule is: the element matches the semantics, the costume matches the theme). Accessible name: "Audit — SVC-01" plus, once stamped, the name gains "— cleared by you" via `aria-describedby` to a visually-hidden status span (the stamp is `aria-hidden`; the state must exist in text). Focus ring: 2px `--stamp` at 4.6:1 on `--manila` — AA for non-text; offset 2px so it clears the card edge. Target size: the whole card (min 44px height is trivially exceeded — cards are ≥150px tall). The tilt never moves the card's hit area (transforms do not affect hit-testing geometry in the visitor's favour — the *visual* card tilts within its layout box, and the box is the target; the tilt amplitude (≤3°) keeps the visual inside the box's neighbourhood so what you tap is what you see).

**Tokens consumed.** `--manila` (face), `--manila-deep` (tab, edge), `--ink` (description), `--stamp` (own stamp via §11.2, tab tick, focus ring), `--carbon` (`FILE CLOSED` mini-stamp), `--ease-thud`, `--ease-bureau` (degraded tilt). Element-scoped: `--folder-spring-k: 170`, `--folder-spring-d: 19`, `--folder-tilt-x: 2deg`, `--folder-tilt-y: -3deg`.

### 11.11 Folder-gate page transition (§6.11)

**Choreography timeline** — relative to nav activation (G0):

| Beat | Time | What happens |
|---|---|---|
| G0 | 0ms | Panels begin closing from their ajar rest (rotateY ∓8° at the screen edges) — 380ms `--ease-file`. If the activation came from a folder (§11.10), G0 is that stamp's impact frame: the gate's first 320ms overlap the stamp's ceremony on the sheet being left. |
| G0+320ms | 320ms | Panels at ~92% closed; the centre spine (punched holes + file number) becomes legible. The `RE-FILING…` label fades in over the last 60ms of this window (opacity, `--ease-bureau`) — it is readable only once the file is nearly shut. |
| G0+380ms | 380ms | Fully closed. The jump executes in this frame: route change, or `scrollTo` the target sheet (instant, `behavior: auto` — a smooth scroll behind closed covers would still be running when they open). |
| G0+380→760ms | 380ms | Panels reopen (`--ease-file`, reverse path). The new sheet is revealed already at rest — its own entrance ceremonies (bars, stamps) are *not* re-run for sheets already released this session; an unreleased target sheet begins its release sequence only after the panels clear its reading position (panels fully open +100ms). |
| Interrupt | any | A second nav activation during the ceremony: close completes in 80ms (`--ease-file` at 4.75× rate), jump, open at full 380ms. Queue depth is 1 — a third click replaces the second's destination; the bureau does not stack filings. |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Open (rest) | Panels flat at edges, invisible, `pointer-events: none` | Single sheet parked below the viewport (§6.11 mobile), invisible |
| Hover / focus | Panels are not interactive; no states. Nav links that trigger the gate keep §11.13's states | Same |
| Closing | 380ms swing; page beneath is inert (`inert` on the main stack) | 300ms bottom-sheet rise; stack inert |
| Closed | Spine + file number + `RE-FILING…` visible for the jump frame(s) | Sheet covers the page; file number visible |
| Opening | 380ms swing reverse | 300ms fall |
| Interrupted | 80ms snap-close, jump, open (above) | 80ms snap, jump, open 300ms |
| Scrolled-past | N/A — the gate is an event, not a region | Same |
| Disabled | JS absent or transition failed → plain anchor jump (§6.11 fallback). `prefers-reduced-motion` → disabled entirely, always | Same |

**Breakpoints.** ≥1200: two-panel swing as Part I. 768–1199: two-panel swing retained, but panel width is 50vw of a narrower desk — the spine's punched-hole column drops from 5 holes to 3 (the centre detail simplifies before the mechanism does). <768: single bottom sheet (§6.11), 300ms each way; the sheet's face carries the file number and the custody mini-list (§6.11) in one column — on the two-panel version the mini-list is on the left panel's inside face; on mobile it is the *only* inside face, so nothing is lost, just stacked.

**Edge cases & failure modes.** *Slow network (multi-page):* the close plays on the source page; if the destination document takes >380ms to arrive, the panels stay closed on the *new* page's loader state (§6.18) — the gate hands off to retrieval rather than holding a fake close; if the destination fails entirely, the browser's own error surface replaces everything (the theme does not theme browser errors). *No canvas/WebGL:* not used. *Low-power:* panels are two transforms — cheap; on the <40fps signal the swing becomes a 200ms crossfade of a full-desk manila field with the spine static at centre (the fiction survives as "the file was closed", the machinery is hidden). *Content longer/shorter:* the gate is content-independent; on a one-page site with only anchor navigation, the gate still fires for index jumps beyond 150vh of scroll distance — for shorter jumps (<150vh) it does *not* fire (a 760ms ceremony to move two sheets down is the bureau wasting time, §6.11); plain smooth scroll (600ms `--ease-file` equivalent) serves short hops. *Scrolling back up:* the gate is nav-triggered only; the back button / history navigation does *not* replay the gate on the destination (the browser restores scroll instantly; a gate over a restored page reads as a malfunction) — except that panels always start open on any page load, so a mid-ceremony unload can never strand the next page behind closed panels: panel state is never persisted, in any storage, ever.

**Accessibility spec.** During the ceremony the underlying stack is `inert`; focus is moved to the destination sheet's heading (with `tabindex="-1"`) at the jump frame, so AT and keyboard users land where sighted users land. The ceremony is announced by nothing — `aria-live` stays silent (a 760ms transition needs no narration; the heading focus *is* the announcement). The `RE-FILING…` label is `aria-hidden`. Focus is never left on a nav link that the gate has covered. Reduced-motion: gate disabled (§6.11) — focus behaviour is unchanged (heading focus on jump is an accessibility feature, not a motion effect). The panels never trap focus: they contain no focusable elements.

**Tokens consumed.** `--manila` (panel faces), `--manila-deep` (inner edges), `--desk` (revealed at the meeting line's shadow), `--ink` (file number, `RE-FILING…`), `--ink-faded` (classification strip on the right panel, static while closed), `--ease-file`, `--ease-bureau` (label fade). Element-scoped: `--gate-dur: 380ms`, `--gate-ajar: 8deg`, `--gate-interrupt-dur: 80ms`.

### 11.12 The bar that never lifts + finale watermark sweep (§6.12)

**Choreography timeline** — two independent objects; the bar has no timeline (that is its point), so its beats are the *absences* around other events, plus the tooltip's clock. Watermark relative to finale trigger (F0 = finale sheet top crosses 62% vh):

| Beat | Time | What happens |
|---|---|---|
| Finale sequence | — | Every other bar in the finale sheet lifts on the standard §11.1 timeline. The `.perm` bar is skipped by the queue, by the 800ms timers, and by the 7s sweep — three separate exclusions, each named in the build (§6.12), because any one of them "helpfully" releasing it destroys the theme's closing argument. |
| Hover dwell | 250ms | Pointer rests on the bar for 250ms before anything happens — a passing cursor must not flash the tooltip (§6.12). |
| Tooltip in | 140ms | Fade + 4px rise, `--ease-bureau`. Text verbatim: "Still classified. Some things stay ours." |
| Tooltip out | 100ms | Fade on leave/blur. No rise reversal theatrics. |
| F0 (watermark) | 0ms | Finale sheet reaches reading position; watermark begins its single sweep: translateX from −12% to +4% of its own width, 1600ms `--ease-file`. |
| F0+1600ms | 1600ms | Watermark rests at +4% permanently. It never loops, never re-runs on re-scroll, never animates again (§6.12). |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Bar — rest | Permanent §11.1 rest state; edge-light on hover, pointedly *without* the shiver (§6.12) | Rest; tap = tooltip (below) |
| Bar — hover | Edge-light + tooltip after 250ms dwell | — |
| Bar — focus | The bar's span is focusable (`tabindex="0"`) — the one bar that *is* a focus target, because its tooltip is content a keyboard visitor must be able to reach. Tooltip shows instantly on focus (no dwell), focus ring is the `--bar-edge` brightening + 1px `--manila-pale` outline on the bar itself | Focus via assistive touch: same |
| Bar — active | No active state; the bar does nothing when clicked — doing nothing, explained by the tooltip, is the interaction | First tap: tooltip shows, nothing else happens (the bar is not a link; there is nothing to suppress). Second tap or tap elsewhere: dismisses |
| Bar — scrolled-past | Unchanged forever | Identical |
| Bar — disabled | No disabled state — it is already the terminal state of every bar | Same |
| Watermark — pre-sweep / swept | Behind the finale sheet; pre-sweep at −12%, swept resting at +4%; never interactive | Same; type capped at 26vw (§6.12 mobile) |

**Breakpoints.** ≥1200: watermark type ~18vw, width 140% of the sheet. 768–1199: type scales with the sheet (the word is sized to the sheet, not the viewport, in this band: width 130% of sheet) — the watermark belongs to the file, and at desk widths the two are near enough that Part I's vw sizing holds; in the narrow band the sheet-relative rule prevents the word from spilling onto the desk. <768: sheet-relative, capped at 26vw type (§6.12); the sweep distance halves (−6%→+2%) — a 1600ms sweep across a phone screen is a weather event, not a draught; duration trims to 1100ms.

**Edge cases & failure modes.** *The catastrophic one:* the `.perm` exclusion failing — a refactor of the lift queue that stops special-casing `.perm` ships a build where the bar lifts like any other. This is guarded three ways: the exclusion is by class check in the queue builder, the timers, and the sweep (three code paths, §6.12); the §10 gate tests it explicitly; and §17's build order puts the `.perm` test before any styling polish. *Slow network / no canvas / low-power:* the bar and watermark are DOM/CSS; the watermark's single transform is the cheapest animation on the page and is never degraded — if the loop is shedding load, the sweep still runs (it is one element, once). *Content longer/shorter:* exactly one `.perm` per page (§9.9) — a page whose copy cannot support a load-bearing withheld sentence does not get a finale `.perm` at all; the watermark still sweeps (the closing argument needs the bar; the watermark is only its weather). A second `.perm` anywhere on the page is an authoring error the build lints (§17). *Scrolling back up:* the tooltip still works; the watermark does not re-sweep; the bar, obviously, does not lift.

**Accessibility spec.** The withheld sentence is in the DOM; its span carries an `aria-label` that appends "(withheld)" after the sentence (§6.12) — AT visitors hear the sentence and its status; visual visitors see the bar and the tooltip. Both are told the truth in their medium. The tooltip is `role="tooltip"` associated via `aria-describedby` on the focusable span; it is reachable by keyboard (focus), by hover, and by tap — three paths, one text, verbatim. Tooltip contrast: `--manila-pale` on `--carbon` ≈9.1:1 at 0.8125rem — AA and AAA. The watermark is `aria-hidden`, decorative, and positioned *behind* the sheet so it can never reduce text contrast (it is visible only on the desk margins around the finale sheet — if a layout lets it pass under text, that is a §10 failure, not a style choice).

**Tokens consumed.** Bar: `--carbon`, `--bar-edge` (via §11.1). Tooltip: `--carbon` (field), `--manila-pale` (text), `--ease-bureau`. Watermark: `--ink` at 14% (stroke). Element-scoped: `--perm-tooltip-dwell: 250ms`, `--perm-tooltip-dur: 140ms`, `--watermark-dur: 1600ms`, `--watermark-travel: -12%→4%`.

### 11.13 Navigation — the file index (§6.13)

**Choreography timeline** — nav interactions are micro; the index reveal on the cover follows the cover's own clock:

| Beat | Time | What happens |
|---|---|---|
| Hover/focus on a top-bar link | 0→180ms | Underline draws left→right, 1px `--carbon`, 180ms `--ease-bureau` — a ruled pencil line (§6.13). On leave it does not un-draw; it vanishes (a line that retracts reads as a progress bar; a ruled line simply stops being emphasised). |
| Cover index line reaches reading position | per line | Ruler-mask uncover, 520ms `--ease-file` (§5), staggered by the mask queue at 120ms per line — the contents page is typed onto the cover as it is read. |
| A sheet is certified | stamp frame | Its index line's page number turns `--stamp` in the same frame as the sheet's stamp (§11.2 F0) — the index and the file agree at every instant (§6.13 content-merge). |
| Nav activation | click | §11.11 gate timeline takes over. |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Archivo Expanded 0.8125rem, exhibit-number prefix, no underline | Same (top bar); index lines full-width rows |
| Hover | Underline draws (180ms) | — |
| Focus | 2px `--stamp` outline offset 2px + underline drawn instantly (focus never waits for a draw animation) | Same |
| Active | Underline thickens to 2px for the press duration | Same on tap |
| Current sheet | Underlined permanently + page number stamped once certified | Same; in the bottom-bar era the top bar still marks current |
| Visited (certified) | Index page number `--stamp` for the session | Same |
| Scrolled-past | N/A (furniture) | Same |
| Disabled | A nav item for a sheet that does not exist is never rendered disabled — it is not rendered (§11.10's rule: absence, not disability, is the archive's way) | Same |

**Breakpoints.** ≥1200: top bar holds brand + up to 5 links + pill (§6.13). 768–1199: links cap at 4 visible; the 5th moves into the cover index only (the index is complete at every band — it is the top bar that trims, never the record). Link size holds 0.8125rem; tracking tightens to +0.14em before any link is dropped. <768: top-bar links collapse behind the `INDEX` toggle (§6.13 mobile): the toggle is a real button, `aria-expanded`, opening the index as a full sheet from the top (300ms `--ease-file`); index lines are 48px rows (touch target law); the sheet closes on selection (gate fires) or on a second toggle press (300ms reverse, no gate — closing a contents page is not a filing).

**Edge cases & failure modes.** *Slow network:* nav is HTML; the index's page numbers and exhibit labels are static text — correct before any script runs. *No canvas/WebGL:* not used. *Low-power:* the underline draw is one transition; nothing to degrade. *Content longer than designed:* more than 5 sections — the top bar caps at 5 and the index carries the rest (§6.13: a file with 9 exhibits is two files — the nav enforces the theme's information architecture by refusing to grow; a build that needs 7 top links has a structure problem the theme will not paper over). *Shorter:* a 2-section page still gets the index (2 lines) — the ritual scales down, it does not vanish. *Scrolling back up:* current-sheet marking follows the sheet in reading position in both directions (the index reflects where the visitor *is*, unlike the dial, which reflects what they have *earned* — the two instruments measure different things and must not be unified). *Index/sheet disagreement:* impossible by construction — the index is generated from the sheets' own exhibit labels at build/init; a hand-maintained duplicate index is a §17 lint failure.

**Accessibility spec.** Landmarks: the top bar nav is `<nav aria-label="File index">`; the cover index is a `<nav aria-label="Contents of this file">` containing an ordered list — exhibit order is list order. Current sheet: `aria-current="true"` on the matching link in both navs. Focus ring: 2px `--stamp`, 4.6:1 on `--manila`, offset 2px (§6.13). Link text is the exhibit label itself ("02 FINDINGS") — descriptive without added labels. The mobile `INDEX` toggle: `aria-expanded` + `aria-controls`, focus moves into the opened index's first line, Esc closes and returns focus to the toggle. Touch targets: top-bar links have 44px effective height (padding inside the 56px bar); index rows 48px in the mobile band, 34px on desktop (pointer precision assumed; keyboard focus is the guarantee, and 34px exceeds the 24px AA minimum for non-touch).

**Tokens consumed.** `--manila` (bar face), `--manila-deep` (bar edge), `--ink` (link text), `--carbon` (underline), `--stamp` (focus ring, certified page numbers), `--ease-bureau` (underline), `--ease-file` (mobile index sheet). Element-scoped: `--nav-underline-dur: 180ms`, `--index-row-h: 34px` (mobile `48px`).

### 11.14 Hero — the cover sheet (§6.14)

**Choreography timeline** — the full ceremony on one clock (L0 = load; consolidates §11.1–§11.4, §11.7):

| Beat | Time | What happens |
|---|---|---|
| L0 | 0ms | Cover lands fully redacted and pinned (sticky, 120vh). Noise static-first-frame (§11.9), dust mid-life. Counters read 0. Dial LVL 0. |
| L0+300ms | 300ms | Typewriter begins the subject line (§11.3). |
| L0+450ms | 450ms | First hero bar pre-flash; peel begins at +474ms; hero bars follow at 210ms stagger (§11.1). Typing and peeling run concurrently — the file is being prepared and released at once, by two different hands of the same bureau. |
| ≈L0+2.4s | ≈2.4s | Typing completes (typical 45-char line). Cover is fully *readable* by ≈2.5s — every body bar has lifted; what remains is ceremony (lettering, stamp) layered over a legible sheet. |
| W0+120ms→+1.4s | — | DECLASSIFIED letters strike (§11.4). |
| +140ms after word | — | Hero stamp slams (§11.2); sheet dips; counters tick to 1/n; pill pulses; classification marquee starts on the cover; dial steps toward LVL 1 (its first tick when *p* crosses .05 — on a 6-sheet page the cover's certification alone is p≈0.167, so LVL 1 lands with the stamp). |
| ≈L0+5.5s | ≈5.5s | Ceremony complete. The cover is a released sheet. Nothing on it moves except dust, noise, and the marquee. |
| Scroll 0→120vh | scrubbed | Cover pinned; Exhibit A's sheet slides up beneath it, its top edge visible from the first pixels of scroll (the 24px cue, §6.14). At 120vh the pin releases; the cover scrolls away as the top sheet of the stack. |
| Hard scroll during ceremony | any | If the visitor scrolls past the pin before the ceremony completes: unfinished steps complete instantly (bars force-lifted by their timers, stamp struck without slam, lettering whole) — the file never holds the visitor hostage (§6.14). |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Sealed (first paint) | Fully redacted cover, counters 0 | Identical |
| Releasing | Ceremony running (timeline above) | Identical; pin 60vh |
| Hover / focus | Cover elements keep their own states (§11.1–§11.4); the sheet itself has no hover/focus state | Same |
| Released | Stamp struck, strip running, dust/noise ambient | Identical |
| Scrolled-past | Cover in the stack beneath Exhibit A; its final state persists if scrolled back to | Identical |
| Disabled | No disabled state. No-JS / reduced-motion: the cover arrives in "Released" state statically (§6.14) — released is the hero's fallback, not a lesser version | Same |

**Breakpoints.** ≥1200: pin 120vh, lamp pool 55% of sheet width, stamp 2.25rem word. 768–1199: pin trims to 90vh (the under-sheet reveal needs less travel on a shorter desk); lamp pool 48%; ceremony timings unchanged. <768: pin 60vh (§6.14), pool 40%, stamp per §11.2 mobile, lettering 1.75rem (§11.4); the typing/peeling overlap compresses — first bar at load+380ms (mobile readers scroll sooner; the ceremony front-loads) — but no beat is *cut*: the full ceremony still plays, 15% faster.

**Edge cases & failure modes.** *Slow network:* the cover is HTML/CSS/text — the ceremony runs on a page whose images are still loading (Exhibit A's sleeve waits per §11.5; the cover has no image dependency). Fonts gate the lettering/stamp per §11.4's shared 500ms cap. *No canvas/WebGL:* not used anywhere in the hero. *Low-power:* the pin is `position: sticky` (compositor-cheap); on the <40fps signal the dust halves and the noise freezes (§11.9) before any ceremony beat is touched — the ceremony is the thesis and degrades last; final degradation (before reduced-motion's full static) is bars peeling via the §11.1 clip wipe. *Content longer than designed:* cover body over 5 paragraphs or bars over 6 — the ceremony stretches past 5.5s and the readability deadline (≈2.5s) breaks; authoring law (§13) caps the cover at 5 paragraphs / 6 bars, and §17 lints it. *Shorter:* a 3-paragraph cover with 3 bars finishes its ceremony in ≈4s — correct; the timeline is event-chained, not fixed-duration, so short covers end early rather than idling. *Scrolling back up:* the pin re-engages (sticky) but the ceremony never replays; Exhibit A slides back down over the released cover — the stack re-stacks.

**Accessibility spec.** The ceremony is visual theatre over a document that is fully present in the DOM from first paint: AT users receive the cover's complete text, in order, immediately — they are never made to wait for typing or peeling (§11.1, §11.3 carry the mechanics: bars `aria-hidden`, typer labelled whole). Landmark: the cover is the page's `<header>`-equivalent section with the H1 as the file title. The pin is a layout effect with no focus implications; focus order is document order straight through the cover into Exhibit A. The classification marquee is `aria-hidden` (a repeating legend is noise to AT; its text exists once, statically, in the sheet's release header for AT). Contrast: all cover text per §2 ratios, measured post-grain (§11.9). Reduced-motion: no pin, no ceremony, static strip (§6.14).

**Tokens consumed.** All of §11.1–§11.4, §11.7, §11.9 (the hero is their composition), plus `--manila-pale` (lamp pool), `--manila` (sheet), `--desk` (surround). Element-scoped: `--pin-length: 120vh` (90vh narrow, 60vh mobile), `--ceremony-readability-deadline: 2500ms`.

### 11.15 Cards — exhibit finding slips (§6.15)

**Choreography timeline** — relative to slip trigger (C0 = slip's top crosses 68% viewport height; slips enter slightly earlier than sheets' reading position because they are *on* a sheet already being read):

| Beat | Time | What happens |
|---|---|---|
| C0 | 0ms | Ruler-mask begins on the slip (520ms `--ease-file`, §5), staggered 120ms per slip within the sheet's slip queue. |
| C0+520ms | 520ms | Slip fully uncovered; pin shadow present at its rest offset. |
| On mask completion | +0ms | If the slip's sensitive clause carries a bar, the bar's queue slot is armed; it lifts per §11.1 when the clause reaches reading position (usually already true — the peel follows the mask by one stagger step, 90ms). |
| Continuous | scrubbed | Pin shadow shifts 1px across the slip's travel (parallax 0.98×, §6.15) — one transform write per frame from the shared loop, slips only while their sheet is on screen. |
| Remediation event | external | If a finding is remediated while the visitor is on the page (a live register), the `REMEDIATED` mini-stamp slams at the slip's foot (§11.2 at 0.45×) and the severity stamp's colour flips to `--stamp` in the same frame. In static builds this state is authored, not animated — both are correct; the animated version is for registers that are genuinely live. |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Pinned (rest) | Flat on the sheet, pin at top-centre, bar per its own state | Identical |
| Hover | Bottom-edge flex: `rotateX 1.5deg`, origin top, §5 spring (170/19) — the slip bends against its pin | — |
| Focus | 2px `--stamp` outline (the slip itself is focusable only if it is or contains a link to the finding detail; a non-link slip is not a tab stop) | Same |
| Active | Pressed slip: flex deepens to 2.2deg for the press (link slips only) | Tap: no flex; navigation is the feedback |
| Released | Bar lifted (clause readable) | Identical |
| Remediated | Severity stamp green + `REMEDIATED` mini-stamp at foot; both stamps permanent | Identical |
| Scrolled-past | Final states persist; mask never re-covers | Identical |
| Disabled | No disabled state; a withdrawn finding is rendered with a carbon `WITHDRAWN` mini-stamp and its clause bar converted to `.perm` (§11.12 mechanics) with the caption "Withdrawn by the auditor, [date]. Record retained." — the register keeps its history | Same |

**Breakpoints.** ≥1200: slips 2-up in the sheet grid (§4), ≤6 per sheet. 768–1199: 2-up holds but gap trims to 32px; pin shadow travel stays 1px. <768: 1-up full column (§6.15 mobile), pin centred, no flex; the severity stamp scales 0.45×→0.5× relative (a bigger stamp on a narrower slip keeps the word legible — the ratio inverts because the slip widened to full column).

**Edge cases & failure modes.** *Slow network:* slips are text; nothing to wait for. *No canvas/WebGL:* not used. *Low-power:* the pin-shadow parallax is the first slip behaviour cut (a static shadow loses nothing but a 2% differential); the flex spring degrades per §11.10's rule. *Content longer than designed:* a finding description over 3 lines — the slip grows (slips are not fixed-height; the grid row stretches and the pin stays top-centre); a sheet with more than 6 findings splits into two exhibits (§4 density) rather than shrinking slips. *Shorter:* a one-line finding still gets a full slip (code, severity, clause) — a finding is a record, and records do not come in "compact" sizes in this theme. *Scrolling back up:* masks and bars never reverse (§11.8's asymmetry applies: records stay read).

**Accessibility spec.** A slip is an `<article>` with `aria-labelledby` pointing at its finding code + title line ("F-03 — Public bucket, client archive"). The severity stamp is `aria-hidden` with the severity stated in the article's visually-hidden lead-in ("Severity 2, open.") — colour and stamp are doubled by text (§2 law 3). The bar over the clause follows §11.1 (text in DOM). Contrast: slip face is `--manila-pale`; body `--ink` on `--manila-pale` ≈8.6:1 — the pale slip is the highest-contrast surface in the theme, appropriate for the densest data. Pin is decorative, `aria-hidden`. Focus (link slips): the whole slip is the link's visible body; target = full slip (≥44px in both dimensions by an order of magnitude).

**Tokens consumed.** `--manila-pale` (face), `--manila-deep` (edge), `--carbon` (pin, open severity stamp), `--stamp` (remediated severity, REMEDIATED stamp, focus ring), `--ink` (body), `--ease-file` (mask), via §11.1 (clause bar) and §11.2 (mini stamps). Element-scoped: `--slip-mask-dur: 520ms`, `--slip-stagger: 120ms`, `--slip-flex: 1.5deg`.

### 11.16 Forms — the file request form (§6.16)

**Choreography timeline** — focus, error, and filing sequences. Filing, relative to submit activation (S0):

| Beat | Time | What happens |
|---|---|---|
| Focus (any field) | 0→120ms | Ruled line thickens 1px→2px `--carbon` (120ms `--ease-bureau`); caret block appears at the field's start (opacity 0→1 in 60ms — the typewriter is positioned). |
| Blur with content | 0ms | Line settles at 1.5px (the ink is on the form, §6.16) — a filled field is visibly heavier than a blank one (1px) and lighter than the focused one (2px): the form's three line weights are its state language. |
| Validation error (on submit or blur-after-first-submit-attempt) | 0→320ms | Per field: the `INCOMPLETE` carbon mini-stamp strikes (0.4× §11.2, 320ms `--ease-thud`), the line goes `--carbon` dashed. The memo summary (§6.16) types in at the form's head at §11.3 mechanics (24 chars ≈ 1.1s) — errors are *filed*, at filing speed. Focus moves to the first incomplete field at S0+320ms (after the stamps land, so the visitor sees the verdict before being moved). |
| S0 (valid submit) | 0ms | Submit box disables (text swaps to `FILING…` — typed at 3 chars per 90ms, §6.16, ≈270ms for the word plus ellipsis). Fields lock (read-only, not greyed — ink does not grey). |
| Server confirms | event | The `REQUEST FILED` stamp slams at the form's top-right (§11.2 full size, 320ms + dip); the submit box re-sets to the static filed line (`FILED — REF …` in `--stamp`, §6.16). The form becomes its own read-only copy with the `COPY — YOUR RECORD` note. |
| Server silent | +8s | If no confirmation by 8s: the submit box re-sets to `FILING DELAYED — DO NOT RE-FILE` and a memo line appears: the request may already be held; re-filing creates a duplicate record. At +20s it becomes `FILING UNCONFIRMED` with a plain retry control. Honest states, in the memo voice (§13) — never a spinner into the void. |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Blank | 1px ruled line at 40% `--ink`, label above | Identical; fields full-width stacked (§6.16 mobile) |
| Hover | Line warms to 60% `--ink` (a hand hovering over the form) — the only hover state on the form | — |
| Focus | 2px `--carbon` line + caret block; label gains a left exhibit tick (2px `--carbon` bar) | Same; the on-screen keyboard opening must not scroll the stamp zone over the field — the form sheet is not pinned, it scrolls naturally |
| Filled | 1.5px line | Identical |
| Error | Dashed line + `INCOMPLETE` mini-stamp + memo summary at head; error text in Courier under the field, `--ink` (never colour-coded — the stamp and the words carry it) | Identical |
| Filing | Fields read-only, submit shows `FILING…` | Identical |
| Filed | Read-only copy, `REQUEST FILED` stamp, filed reference line, `COPY — YOUR RECORD` | Identical |
| Disabled | The submit box is disabled only during Filing (native `disabled`, styled as an un-struck form box at 60% — a form box awaiting its stamp is the one legitimate "disabled" visual in the theme, because the fiction has a word for it: *pending*) | Same |

**Breakpoints.** ≥1200: form sheet at the standard 880px, fields in the document column; `NATURE OF REQUEST` textarea ruled at 3 lines. 768–1199: identical layout; the stamp zone reserves the top-right 220px so the `REQUEST FILED` stamp never overlaps the first field's label. <768: labels stack above fields full-width (§6.16 mobile), stamp at 0.7× top-right, submit full-width min-height 52px, textarea still 3 ruled lines (a request's nature does not shrink with the screen).

**Edge cases & failure modes.** *Slow network:* the form posts as a plain HTML form without JS (§6.16 fallback); with JS, the 8s/20s states above govern silence. A submission that succeeds server-side but whose response is lost shows `FILING UNCONFIRMED` — and the copy tells the visitor the bureau will confirm by email rather than inviting a duplicate (§13). *No canvas/WebGL:* not used. *Low-power:* all form motion is class swaps and one stamp; the memo typing is the only timer and degrades to an instant text swap. *Content longer than designed:* more than 6 fields — the form splits into two sheets (`REQUEST — PAGE 1 OF 2`) with the gate (§11.11) between them only on explicit `CONTINUE` (a form is the one place the gate fires on a button other than nav); fewer than 3 fields is a slip, not a form — use §6.15's slip with a single field, not a whole sheet of furniture around two inputs. *Autofill:* browser autofill background (usually a blue/yellow wash) is overridden with `box-shadow: inset 0 0 0 100px var(--manila)` on `-webkit-autofill` — an archive form that flashes browser-blue has broken its own fiction at the moment of maximum trust. *Scrolling back up:* the filed state persists (it is a record); an unsubmitted form keeps its values and its line weights — the visitor's ink stays on the form.

**Accessibility spec.** Real `<label>` elements (the Archivo labels *are* the labels, associated by `for`/`id` — not placeholders-as-labels; placeholders, where used, are Courier italic examples and never the only name). Error text is linked via `aria-describedby`; the memo summary is `role="alert"` on first appearance only (subsequent edits re-validate silently per field). Required markers "(REQUIRED — EXHIBIT A)" are text, not asterisks (§6.16). Focus order = visual order = document order; the filed stamp is `aria-hidden` with the filed state announced by the submit box's new text (`FILED — REF …`, a real text change AT can read) plus `role="status"` on the filed line. Contrast: labels `--ink` on `--manila` 7.4:1 at 0.6875rem bold — small text at 7.4:1 passes AA; input text 7.4:1; the 40%-alpha ruled line is decorative (the field's boundaries are also given by label position and the caret). Touch targets: inputs ≥48px tall in the mobile band (line + label zone), submit ≥52px.

**Tokens consumed.** `--ink` (lines at 40/60/100%, labels, text), `--carbon` (focus line, error stamp, dashed error line), `--stamp` (filed stamp, filed line), `--manila` (sheet, autofill wash), `--ease-bureau`, `--ease-thud` (via §11.2). Element-scoped: `--field-line-rest: 1px`, `--field-line-filled: 1.5px`, `--field-line-focus: 2px`, `--filing-timeout-1: 8s`, `--filing-timeout-2: 20s`.

### 11.17 Footer — the custody sign-off (§6.17)

**Choreography timeline** — the footer is where motion stops (§6.17); its single event, relative to footer trigger (B0 = footer top crosses 70% viewport height):

| Beat | Time | What happens |
|---|---|---|
| B0 | 0ms | The `RECEIVED BY` line begins typing (§11.3 mechanics): `THE VISITOR — n / n PAGES` at ~46ms/char, ≤24 characters ≈ 1.1s. This is the last typing in the file (§6.17). |
| B0+≈1.1s | ≈1100ms | Typing completes; no caret fade choreography — the caret simply stops (it is removed at typing end +0ms; the footer's stillness begins immediately, not after a fade). |
| Everything else | never | The `END OF FILE` stamp is static from first paint of the footer. The release date, the signature, the cross-references: still. If the visitor idles on the footer for a minute, the only motion on screen is the noise field — and the footer sits on the desk, outside the stack, so even the grain does not crawl there (§11.9 content-merge). Total stillness is the ending (§6.17). |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Unsigned | Before B0: `RECEIVED BY` line blank (its label present) | Identical |
| Hover / focus | Cross-reference links take §11.13's underline/focus treatments, in `--manila-pale` on `--desk` | Same |
| Signing | The typing beat (above) | Identical |
| Signed | Count typed, stamp present — terminal | Identical |
| Scrolled-past / back up | Signed state persists; typing never replays | Identical |
| Disabled | No disabled state. No-JS: the block renders complete statically (§6.17 fallback) | Same |

**Breakpoints.** ≥1200: three blocks side by side on the desk (Released by / Received by / Cross-references). 768–1199: two blocks + cross-references wrapping beneath at full width. <768: stacked (§6.17 mobile); `END OF FILE` stamp centred, fully on the desk (no sheet-edge overlap — §6.17 mobile rule); the signature line and release date keep their Courier italic/regular distinction at every band.

**Edge cases & failure modes.** *Slow network:* footer is static text + one timer; the count it types is read from §6.7's ledger at B0 — if the visitor jump-scrolled to the footer with sheets unreleased, the count honestly types the *current* ledger (e.g. `2 / 6 PAGES`) — and if they then scroll up and release more, returning to the footer updates the typed line instantly (no re-typing; the receipt is corrected, not re-performed). This is the one place a "final" state revises, because a receipt that disagrees with the ledger is a §6.7 lie. *No canvas/WebGL:* not used. *Low-power:* typing degrades to instant text. *Content longer/shorter:* a footer whose organisation has no named releaser signs with the bureau name alone (never an invented person's name — Real Content); the cross-reference index caps at 8 lines, beyond which the overflow goes to a `FULL INDEX` line linking the index sheet. *Scrolling back up:* nothing reverses.

**Accessibility spec.** The footer is `<footer>` (contentinfo). The typed count is `aria-hidden` as it types; a visually-hidden static line carries the final text ("Received by the visitor — n of n pages") so AT gets the receipt whole, once. Cross-reference links are a list with exhibit-style numbering visible and list semantics intact. Contrast: `--manila-pale` on `--desk` ≈5.9:1 (§2) at 0.8125rem — AA for normal text; in dark mode the desk deepens to `#2E2820` and the ratio rises to ≈7.6:1 (the footer is the one surface that gets *more* legible at night). The `END OF FILE` stamp: `--stamp` on `--desk` ≈2.2:1 — it is a large display object doubled by its own words being readable at size (2.25rem bold, AA-large needs 3:1 — 2.2:1 *fails* AA-large; the ruling: the stamp's desk portion is decorative overlap, and the stamp must be positioned so its *word* sits on the sheet's manila edge (4.6:1) with only its border crossing onto the desk — §6.17's overlap is of the stamp's frame, never of its lettering. A build whose stamp word sits on the desk fails §10.)

**Tokens consumed.** `--desk` (ground), `--manila-pale` (text), `--stamp` (`END OF FILE` stamp), `--ink` (typing via §11.3 mechanics, in pale — the typing consumes `--manila-pale` here, the footer's one substitution, recorded so a builder does not "fix" it to `--ink`, which on `--desk` would be ≈1.9:1 and unreadable). Element-scoped: `--footer-type-dur: ≈1100ms`.

### 11.18 Loader — retrieving the file (§6.18)

**Choreography timeline** — relative to loader appearance (R0 = navigation/route request):

| Beat | Time | What happens |
|---|---|---|
| R0 | 0ms | The closed folder is present. If the wait will be under ~300ms the loader never appears at all — it is rendered only when the route's ready signal has not arrived by R0+300ms (a loader flashed for 120ms is a glitch wearing a costume; the 300ms threshold is the loader's own honesty rule). |
| R0+300ms | 300ms | Folder fades/rises in: opacity 0→1 over 150ms `--ease-bureau`, at its resting −0.3°. The count line reads `SHEETS RETRIEVED: 0` or, if progress is unknowable, the numberless line (§6.18). |
| Per resource | event | Count increments as real sheets/assets resolve (§6.18) — event-driven like §11.7, digit swap instant (no slide: retrieval is a machine process, its numbers do not perform). The `--stamp` progress line under the folder extends proportionally in the same frame. |
| Breathing | 2.4s cycle | Folder rotate −0.3°→−0.1° alternate `--ease-bureau` (§6.18) — begins only after the loader has been visible 1.2s (a folder that breathes immediately is alive; a folder that breathes after a wait is *held*). |
| R0+6s | 6s | Stall memo appears beneath the folder: `RETRIEVAL DELAYED — THE ARCHIVE IS DEEP.` (fade 200ms). The count keeps counting if events arrive. |
| R0+12s | 12s | `OPEN THE FILE ANYWAY` text link appears (§6.18) — a real link, focusable, styled as a Courier underlined line. Activating it forces entry with loaded sheets; unloaded sheets show their §11.5 sealed state and load in place. |
| Ready | event | Exit: folder front rotates up (rotateX −38°, origin bottom, 420ms `--ease-file`) revealing the page's first sheet beneath, which fades in over 200ms concurrently (the sheet is *under* the folder face — the reveal is spatial, not a crossfade of two screens). Loader removed from the DOM at exit+420ms. Total exit ≤620ms (§6.18). |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Absent (fast load) | Never rendered (<300ms waits) | Identical |
| Retrieving | Folder + counting line + progress line; page beneath is not yet interactive | Identical; folder at 84vw (§6.18 mobile) |
| Hover / focus | The folder is not interactive; the only control is `OPEN THE FILE ANYWAY` (after 12s): standard link states (§11.13 underline/focus) | Same |
| Stalled | Memo line present (>6s); force-entry link added (>12s) | Same |
| Opening | The 420ms exit ceremony | Identical |
| Gone | Removed from DOM; the page is the state | Identical |
| Disabled | JS absent → no loader exists (§6.18 fallback). Reduced-motion → no breathing, no opening ceremony; loader fades 150ms when ready (§6.18) | Same |

**Breakpoints.** ≥1200: folder min(420px, 84vw) × 260px centred on the desk. 768–1199: 380px wide; the progress line and count unchanged. <768: 84vw, height 220px; the stall memo and force-entry link stack beneath the folder with 48px touch height for the link; breathing amplitude halves (±0.1°) — a breathing folder on a small screen competes with the count, which is the information.

**Edge cases & failure modes.** *Slow network* is the loader's home case — governed by the 6s/12s beats above; a retrieval that completes between 300ms and 6s is the normal case and shows no memo. *Progress unknowable* (opaque response): the numberless line + caret, and the progress line becomes indeterminate — a 25%-wide segment sliding along the track at 1.2s `--ease-bureau` alternate (the theme permits this one machine-like motion because retrieval *is* a machine process, §6.18; it is the only indeterminate indicator in the theme). *No canvas/WebGL:* not used. *Low-power:* breathing is cut first, then the progress line's slide (static track), the count never degrades (information). *Content longer/shorter:* the count's denominator is the route's real sheet/asset count from the manifest the router provides; a route that cannot enumerate its sheets uses the numberless line — never an estimated denominator (a count of "3 of about 6" is fake precision, §6.18). *Back button during retrieval:* the loader is destroyed with the page; no state persists; returning re-retrieves. *The loader itself failing to load:* impossible by construction — it is inline in the initial HTML/CSS, rendered by the server over the server-rendered page (§6.18); a loader that needs loading is a paradox the build does not contain.

**Accessibility spec.** The loader region is `role="status"` with an `aria-label` "Retrieving the file"; the counting line's *number* is announced at most every 2s (polite) and the stall/force-entry states are announced once each (`role="alert"` for the 12s state only — it carries an action). The force-entry link is a real `<a>` with a descriptive name ("Open the file anyway — some sheets may still be sealed"). Focus is never moved into the loader except onto the force-entry link when it appears *and* the visitor has been idle on the loader for the full 12s (focus theft is justified exactly once: the link is the only way forward). Contrast: folder text `--ink` on `--manila` 7.4:1; memo `--manila-pale` on `--desk` 5.9:1. Reduced-motion per §6.18. The exit ceremony never delays interactivity past its 620ms: the page beneath is focusable from the jump frame, with the folder face `pointer-events: none` from exit start.

**Tokens consumed.** `--desk` (field), `--manila-deep` (folder body/tab), `--manila` (folder face), `--ink` (retrieval text), `--stamp` (progress line), `--manila-pale` (memo on desk), `--ease-file` (exit), `--ease-bureau` (fade, breathing). Element-scoped: `--loader-threshold: 300ms`, `--loader-stall-1: 6s`, `--loader-stall-2: 12s`, `--loader-exit-dur: 420ms`.

---

## 12. Component inventory — every component, in the file's materials

A real site needs more than §6's elements. Every standard component below has exactly one themed form. Where the theme refuses a component, the refusal and its substitute are the specification — a builder who imports the generic version has failed this section.

**Primary button — the form box.** An unstamped form box awaiting its stamp: Archivo Expanded 700, all caps, 1rem, +0.12em, `--ink` text, 2px `--carbon` border (double rule 3px/1px at hero scale), `--manila` face, padding 14px 28px, min-height 52px. Hover: the box's border inks darker (border to full `--carbon` from 70%) over 120ms. Active: the §11.2 dip at button scale (`scale(0.99)`, 120ms) — pressing a primary button is a small stamp strike; on successful completion of its action, a real stamp may land on or beside it (form §11.16). Focus: 2px `--stamp` outline offset 2px. There is at most **one** primary button per sheet — a sheet with two primary actions is two sheets.

**Secondary button — the ruled box.** Same geometry, 1px `--ink` border at 60%, text 0.875rem. It is the primary's clerk: present, official, unhurried. Never filled, never green (§2 law 1 — a green button certifies nothing).

**Text link — the ruled line.** Courier or Archivo per context, 1px underline drawn on hover (§11.13, 180ms `--ease-bureau`), `--ink` always — no blue, no green, visited links take `--ink-faded` (a consulted reference is a faded one — visited state as ageing, the theme's one use of the browser's memory).

**Text input / textarea.** §11.16 in full: ruled lines, three line-weights as state language, Archivo labels, Courier input text, caret block on focus, autofill wash override.

**Select — the index drawer.** A native `<select>` is unstyleable into this world, so the themed select is a ruled field (§11.16) whose value line ends with a typed glyph `▾` set in Courier; activating it opens an **index sheet**: a `--manila` panel sliding from beneath the field (240ms `--ease-file`) listing options as index lines (§11.13 rows, 40px), the current option underlined, selection closing the sheet and re-typing the field's value (§11.3 mechanics at 24ms/char — the bureau writes the choice in). Keyboard: full listbox semantics (`role="listbox"`, arrow keys, type-ahead). Fallback: without JS it *is* a native select wearing the ruled line — the custom drawer is an enhancement layered on a real control, never a replacement for one.

**Checkbox — the exhibit tick box.** A 20px square, 1.5px `--carbon` border, empty. Checking it strikes a tick: an SVG path draws in 140ms `--ease-flick` in `--ink` (the visitor's own hand ticks in ink, not stamp green — ticking a box certifies nothing, it *records* a choice). The label is Courier 1rem with a 44px total row height. Indeterminate state: a horizontal ink stroke (a dash, as a clerk marks "partly").

**Radio — the custody choice.** A 20px circle, same border; selection fills it with a 10px `--carbon` disc that scales in at 120ms `--ease-thud` at micro scale (a small struck mark). Radio groups are introduced by an exhibit label ("SELECT ONE — EXHIBIT C").

**Toggle — refused as a switch; replaced by the stamp choice.** There are no sliding switches in a paper office. A binary setting is two mini form boxes side by side — e.g. `FILE OPEN` / `FILE CLOSED` — the active one carrying a carbon mini-stamp of its own word. State changes are instantaneous and textual. (Settings that are genuinely preferences, e.g. email frequency, use radios.)

**Search — consulting the index.** The search field is a ruled field (§11.16) labelled `CONSULT THE INDEX`; results render as index lines (§11.13) on the same sheet, each with its exhibit number and page; a query with no results returns the misfiled line (§13 empty voice) plus the nearest exhibit headings as `NEAREST ENTRIES`. Search never leaves the file metaphor for a results *page* unless the corpus is genuinely an archive (§7 listing pattern).

**Table — the ruled register.** Courier throughout; header row Archivo Expanded 0.6875rem +0.2em; rows ruled with 1px `--ink` at 25%; row height = 2 lines (52px) — a register is written in, not rendered; numeric columns tabular-nums, right-aligned like a ledger; a totals row is double-ruled (the accountant's line) and its figure may carry a mini-stamp if it is a certified total (fee schedule §7 — prices never redacted, totals stamped only when they are contractual). Zebra striping is banned (registers are ruled, not shaded); hover on a row inks its rule to 60%.

**Badge — the mini stamp.** Status is expressed as mini stamps (§11.2 at 0.45×): `CLEARED`, `OPEN` (carbon), `REMEDIATED` (green, earned), `WITHDRAWN` (carbon). A "badge" that is a rounded pill in a pastel colour does not exist here. Counts ("3 new") are ledger figures in the pill (§11.7), never badges.

**Alert — the memo block.** A Courier block at the head of its sheet, introduced by `MEMO:` and ruled top and bottom, stating the fact and the required action in the memo voice (§13). Errors use the carbon `INCOMPLETE` stamp (§11.16); confirmations use a green mini-stamp. There is no red alert, no yellow warning — the bureau has two registers: *noted* (memo) and *certified/refused* (stamp). Dismissible alerts carry a `FILED — DISMISS` text control; dismissing files the memo (it collapses with the ruler-mask in reverse, 300ms).

**Toast — the filed slip.** A small `--manila-pale` slip (§11.15's paper) slides from behind the rail's bottom edge (300ms `--ease-file`), bearing one Courier line and, where relevant, a mini stamp; it stays 5s, then is *filed* — it slides down into the footer's custody block region and is gone (toasts in this theme are not dismissed into the void; they are put in the file). Maximum one visible; a second queues until the first is filed. Toasts announce events ("REQUEST FILED — REF 114-K-221"), never marketing.

**Modal — the annex sheet.** A modal is a sheet pulled from the file and laid over it: the stack dims to `--desk` at 60% (the desk darkens because the lamp moved), and a single `--manila` sheet (max-width 640px, rotation −0.2°) scales from 0.98 + fades in over 240ms `--ease-file`. It has an exhibit label, a heading, content, and a `RETURN TO FILE` ruled control; its top-right carries a paper-clip drawn in SVG (the annex is *clipped on*, §7's annex pattern). Focus is trapped inside while open; Esc returns it to the file; the sheet it covers is `inert`. Image enlargement (§11.5 sleeves) uses the annex sheet at 880px with the photo at full resolution — the "lightbox" is an evidence sheet, not a black void.

**Pagination — page turns.** At a listing's foot: `PAGE 02 / 06` in Courier with two ruled controls, `← PREVIOUS SHEET` and `NEXT SHEET →`, each a §11.13 index line. Numbered page links, where the corpus needs them, are page numbers in the index style (current underlined, certified-visited in `--stamp`). Infinite scroll is refused — a file has pages, and the visitor turns them deliberately; load-more buttons are refused for the same reason (the substitute is pagination).

**Tabs — index tabs, listings only.** §7's manila tabs along a sheet's top edge (`--manila-deep`, active tab `--manila` raised 2px) exist solely as listing filters. They are real tabs semantically (`role="tablist"`, arrow-key navigation) and they filter a register; they never switch document content on a sheet (§4's linearity law).

**Accordion — refused on sheets; the index expansion substitutes.** A document does not fold. On listing pages, an index line may expand in place to reveal its exhibit slip (§11.15) — expansion downward in document order, 300ms `--ease-file` height animation, one open at a time — which gives the accordion's space economy without its hide-and-seek. FAQ content, where a site genuinely has it, is a transcript sheet (§7): questions as exhibit headings, answers as document paragraphs, all open. An FAQ that must be clicked open one question at a time is a file that will not release its contents — off-theme by definition.

**Breadcrumbs — the custody trail.** `FILE 114-K / EXHIBIT B / PAGE 03` set in Courier 0.8125rem at a sheet's head, each segment a link (§11.13 treatment), the final segment unlinked and underlined. The trail is the document's own address inside the file — it appears on detail pages (§7), not on the home file (you cannot be inside a path you are holding whole).

**Tooltip — the carbon tooltip.** §11.12's component generalised: `--carbon` field, `--manila-pale` Courier 0.8125rem text, 250ms dwell, 140ms fade, `role="tooltip"`, keyboard-reachable wherever its host is focusable. One line preferred; two maximum. Tooltips explain *status* ("Still classified…", "Stamped when this sheet is fully read"), never label icons — this theme has no icon-only controls to label.

**Progress bar — one licensed instance.** Only the loader's (§11.18). Everywhere else, progress is the dial (§11.6), the line (§11.8), or the counters (§11.7). A generic top-of-page scroll progress bar is banned — it would compete with three better instruments that mean more.

**Skeleton — skeleton leaves.** Loading placeholders are §6.1/§6.5's skeleton bars and §6.14's sealed sheets: content-shaped `--carbon` blocks at authored widths on `--manila`, static (a skeleton that shimmers is a screen effect; a skeleton *leaf* is blank paper in the file — stillness is correct). A skeleton that persists >3s gains the §11.18 stall memo treatment.

**Avatar — the officer's sleeve.** People appear only as evidence: a portrait inside an evidence sleeve (§11.5), uncensored for officers of the bureau (§7 about pattern), captioned with name, role, and custody line. Round avatar crops do not exist in this theme; photographs are rectangular evidence or they are not shown.

**Divider — the ruled exhibit rule.** Between blocks inside a sheet: a 1px `--ink` rule at 40% spanning the document column, optionally centred with a typed ornament — three Courier hyphens separated by spaces (`- - -`) — never an SVG flourish, never a gradient fade (rules are drawn with a straight edge; they do not dissolve).

**Consent / notice banner — the clipped annex slip.** Where law requires a notice, it arrives as a small sheet clipped to the foot of the cover (paper-clip, annex pattern), stating the notice in Courier and offering two mini form boxes (`NOTED` / `NOTED — WITH RESERVATIONS` is theatre; the real pattern is the notice + one `FILED` acknowledgement box that stamps itself on activation, §11.10 mechanics). It never floats over content as a bar; it is *in* the file, at the file's foot, and it stays until acknowledged because the bureau does not pretend a notice was seen.

---

## 13. Content & copywriting voice

The bureau writes everything. Two voices, strictly separated (§3): the **bureau** (Archivo Expanded, caps, labels, stamps, buttons) gives orders and certifications; the **file** (Courier, sentence case) gives evidence. Copy that mixes the registers — a Courier headline, an Archivo paragraph — is a voice defect on sight.

**Voice principles.**

1. **Literal before clever.** Every label names the thing it labels. `EXHIBIT B — CUSTODY TRANSFER, DAY 14`, not "The plot thickens".
2. **Numbers are exact or absent.** "30 days", "14 findings", "REF 114-K-221" — or the sentence is rewritten without a number. Never "countless", "numerous", "world-class".
3. **The bureau never exclaims.** Exclamation marks are banned site-wide — zero, not "sparingly". Emphasis is underline, second strike (§3 law 2), or a stamp.
4. **Withholding is stated, never teased.** Where content is withheld, the copy says what kind of thing it is and why ("the bucket's name is withheld under the client's release terms"), never "you won't believe what we found".
5. **Past tense for findings, present tense for state, imperative for actions.** "We found the store public on Day 14." / "This sheet is cleared." / "File this request."
6. **The one joke is restraint.** §6.12's tooltip line, verbatim, once per page. No other line on the site attempts humour; dryness everywhere else is what makes the one line land.

**Headline style.** File titles and sheet headings are case names: noun phrases, all caps (Archivo), no verbs of marketing, no questions. Good: `HOW THE KEYS CHANGED HANDS` / `THE CHAIN OF CUSTODY` / `WHAT WE RELEASE, WHAT WE KEEP`. Bad: `Unlock Next-Level Security Today` / `You Won't Believe What Hackers Found` / `Security, But Make It Simple`. A headline may be *dry* ("FINDINGS, IN ORDER") but never cute.

**Exhibit labels.** Format is law: `EXHIBIT [letter] — [literal subject], [day/date or qualifier]`. Letters run A, B, C… in document order and match the index (§11.13) character-for-character. File references follow `FILE 114-K / EXHIBIT B / PAGE 03` — the file number is the site's real project/client code pattern, fixed at build, used identically in the loader, the gate, the footer, and every reference line.

**Body voice (the file).** Sentences report; they do not sell. Findings are written as an auditor writes: observation, evidence, consequence. Example, as authored in §8: "On Day 14 the archive was found in a public bucket. The bucket's name is withheld under the client's release terms. 41,208 accounts were listed." Marketing copy forced into this theme is rewritten into findings or cut — a paragraph that cannot survive being typed in Courier does not belong in the file.

**Button & action labels.** Verbs of filing, in Archivo caps: `FILE THIS REQUEST`, `CONSULT THE INDEX`, `OPEN THE FILE ANYWAY`, `RETURN TO FILE`, `REQUEST THE FULL FILE`. Banned: `Submit` (the bureau does not submit, it files), `Get started`, `Learn more` (say what will be learned: `READ THE FINDINGS`), `Click here`, `Buy now` (commerce in this theme is `FILE AN ORDER` with the fee schedule open beside it, §7).

**Error voice — the memo.** Errors are memoranda: factual, addressed, actionable, unemotional. Format: `MEMO: [what is missing/wrong]. [What to do].` Examples: "MEMO: TWO FIELDS REQUIRE COMPLETION BEFORE FILING." / "MEMO: THIS ADDRESS DOES NOT ACCEPT MAIL. CHECK THE SPELLING AND RE-FILE." / "MEMO: THE REQUEST WAS RECEIVED TWICE. THE SECOND COPY HAS BEEN SHREDDED." Never: "Oops!", "Uh oh", "Something went wrong" (something specific always went wrong; name it), never an apology in the bureau's voice — the bureau corrects the record instead ("THE DATE IN EXHIBIT A WAS INCORRECT. IT HAS BEEN CORRECTED AND THE CORRECTION NOTED.").

**Empty-state voice — the misfiled line.** Empty states state the file's condition and offer the index: "THE REQUESTED SHEET IS NOT IN THIS FILE." / "NO ENTRIES UNDER THIS TAB. THE REGISTER HOLDS 14 ENTRIES UNDER ALL TABS." / search: "NO ENTRY MATCHES 'backup'. NEAREST ENTRIES: EXHIBIT B, EXHIBIT D." An empty state never says "nothing here yet" (yet = a promise the bureau has not made) and never illustrates itself with a mascot.

**Success voice — the stamp and the receipt.** Success is a stamp word plus a reference: `REQUEST FILED — REF 114-K-221`, with the copy-for-your-record (§11.16). No "Awesome!", no confetti logic in words. Where a reference cannot be real, the line is `FILED` alone (§6.16's Real Content rule).

**Dates, times, numbers.** Relative case days ("Day 14") inside a case narrative; calendar dates in the file's real chronology are written `14 MARCH 2026` in bureau contexts and `14 Mar 2026, 03:12 PKT` in evidence captions (the demo's proven format). Counts always carry denominators where a whole exists ("3 / 6"). Percentages are avoided in findings (a percentage is a summary; the file gives the figures: "41,208 of 41,208 accounts" — the bureau lets the visitor do the arithmetic of alarm).

**Microcopy specifics.** Field hints are filing instructions: "AS IT APPEARS ON THE REQUEST" / "THE ADDRESS THAT RECEIVES THE FILE". Placeholders, when used, are Courier italic examples of real format, never instructions ("e.g. REF 114-K-…" is banned — a placeholder that teaches format uses a plausible complete example: "114-K-221"). The classification strip's legend is fixed: `DECLASSIFIED · RELEASED UNDER REQUEST [file number] · `. The loader's lines are §11.18's verbatim set. The `RE-FILING…` gate label is verbatim. These strings are part of the design system; a build that paraphrases them has forked the theme.

---

## 14. Three worked examples, end to end

The same cybersecurity firm as §8 (file 114-K). §8 worked Exhibit B; these three work the cover, the custody sheet, and the conversion sheet — the page's opening, middle, and ask.

### 14.1 Worked example — the hero (cover sheet)

**The artefact.** The home page's cover sheet. Content, as authored: file line `FILE 114-K — RELEASE COPY`; title `WHAT WE FOUND IN YOUR NETWORK` (Archivo Expanded, 3 lines at desktop); subject line typed: `SUBJECT: A 30-DAY AUDIT OF THE MERIDIAN LOGISTICS NETWORK` (58 characters — inside §11.3's 72-char cap); four Courier paragraphs of cover summary carrying 5 bars: ¶1 plain (who the firm is, in findings voice); ¶2 two bars (the headline finding's count, and the exposure window); ¶3 two bars (the containment claim and its timestamp); ¶4 one bar (the sentence that names what the firm will *not* publish — the cover's own small act of restraint, foreshadowing §6.12). Then the lettering, the stamp zone, and the head of the cover index (§11.13) below the pin's fold.

**Layout numbers.** Sheet 1, rotation −0.3°, padding 56/64/72px; title at `clamp(2.75rem, 6.5vw, 4.75rem)`; lamp pool top-right, 55% width; stamp zone reserved at the title block's right margin, stamp rotation −8° (the §6.2 table's hero value); pin 120vh.

**Timeline — load phase (L0 = load) and scroll phase (scroll % of the pin's 120vh travel):**

| When | Beat |
|---|---|
| L0 | Cover sealed; counters 0/6; dial LVL 0; noise static; dust mid-life in the pool. |
| L0+300ms | Typing begins (§11.3). |
| L0+450ms | Bar 1 (¶2's count) pre-flash; peel at +474ms. Hero stagger 210ms: bars at ≈474 / 684 / 894 / 1104 / 1314ms peel starts, each 380ms — last bar done ≈1694ms. |
| ≈L0+2.9s | Typing completes (58 chars ≈ 300 + 58×46ms + comma/final-word pauses ≈ 3.0s — slightly over §11.3's typical; the readability deadline is set by the bars, not the typing, and holds: body fully readable at ≈1.7s, ahead of the ≈2.5s deadline). |
| +120ms after typing | Letters strike (§11.4), ≈1.4s → word whole ≈L0+4.4s. |
| +140ms | DECLASSIFIED stamp slams (§11.2); sheet dips; counters tick 1/6; pill pulses; dial crosses .05 → LVL 1 (cover certification alone is p = 1/6 ≈ .167); marquee starts on the cover. Ceremony complete ≈L0+4.9s — inside the ≈5.5s budget because the bars finished early. |
| Scroll 0–15% of pin | Exhibit A's top edge (the 24px cue) grows to ~90px visible beneath the cover; the cover's shadow deepens fractionally (the stack separating). Nothing on the cover animates. |
| Scroll 15–85% | Exhibit A slides up beneath the pinned cover; as A's own top crosses 62% vh *under* the pin's end, A's release sequence arms but does not fire until the pin releases (a sheet may not release while covered — its bars' reading position is computed against the *visible* stack, and the cover still occupies the reading zone). |
| Scroll 100% (120vh) | Pin releases. The cover scrolls away as the stack's top sheet; Exhibit A, now at reading position, fires its sequence (§8's pattern). The visitor has been handed from ceremony to document without a seam. |

**Failure rehearsal.** Kill JS at L0+1s (mid-ceremony): bars freeze mid-peel for 800ms, then force-lift; stamp renders struck; lettering whole (watchdog 3s); the pin never engages (sticky is CSS — it *does* engage; correct the rehearsal: with JS dead the pin still holds because `position: sticky` is not script — and that is fine, because the cover it pins is fully released and readable; the pin is choreography, not a gate).

### 14.2 Worked example — mid-page section (Exhibit C, the Chain of Custody sheet)

**The artefact.** Sheet 4 of 6, rotation +0.3°. Exhibit label `EXHIBIT C — CHAIN OF CUSTODY, DAYS 0–30`; H2 `EVERY HAND THAT HELD THE KEYS`. Content: one plain Courier paragraph (why custody matters, findings voice); the custody block — four entries (Day 0 — store created by a deployment script; Day 3 — access widened by a contractor, initials box `R.V.`; Day 14 — found public by the firm's scanner, initials `A.K.`; Day 30 — contained, keys rotated, initials `A.K.` countersigned `M.O.`) bound by the self-drawing line (§11.8); one evidence sleeve (C-1: the access-policy diff, a document facsimile — §11.5's 3px-blur document variant) whose sensitive clause (the contractor's company name) is barred; the sheet's stamp word is `CLEARED`. Bars on the sheet: 1 (sleeve clause) + 0 in body = the lightest sheet on the page by design — the custody sheet's drama is the line, not the bars; density is varied per sheet so the mechanic's rhythm changes across the file (a page where every sheet has 5 bars is a metronome; §4's ≤9 is a ceiling, not a quota).

**Scroll timeline** (viewport-height beats; sheet top position measured against vh):

| Scroll beat | What fires |
|---|---|
| Sheet top at 100% vh (enters) | Sheet still; sleeve sealed; line at 0%; the sheet reads as an unopened exhibit — correct. |
| Sheet top at 78% vh | First custody circle becomes visible (§11.8 pre-arm beat). |
| Sheet top at 70% vh | Line draw begins (scrub window opens). Entry 1 (Day 0) is above this line in the block and is already uncovered — the first entry of a chain is the chain's origin and is never masked: custody begins from a known state. (Authoring rule this example establishes: the mask sequence starts at entry 2.) |
| Block travelling 70%→30% | Line scrubs down; circles fill at Day 3, Day 14, Day 30 baselines; each entry's ruler-mask starts 120ms after its circle fills (520ms `--ease-file`). The Day 14 entry is the longest (three lines) — its mask duration is unchanged; the line's scrub is scroll-bound, so a slow reader gets a slow chain and a fast scroller gets the whole chain drawn in one pass, circles filling in sequence at whatever rate the scroll dictates — order is preserved at every speed, which is the entire point. |
| Sleeve centre at 58% vh | Sleeve event (§11.5): slit 640ms, facsimile resolving from 3px blur, clause bar peels at +520ms (300ms), mini RELEASED stamp at +700ms. |
| Last element resolved +180ms | The sheet's CLEARED stamp slams (−6°, §6.2 table); counters 4/6; dial — sheets 1–3 certified plus this sheet's completion — crosses .65 → LVL 4 during this sheet's travel (p reaches .667 at the stamp). |
| Sheet top past 0% (scrolled beyond) | Line fully drawn, final circle double-ringed; scrolling back re-inspects (line retreats, circles stay, §11.8). |

**Failure rehearsal.** Break the scrub (JS loop halted): line renders fully drawn on the fallback pass, circles filled, entries uncovered — the chain reads complete statically; the visitor loses the drawing, keeps the custody.

### 14.3 Worked example — the conversion section (the request form sheet)

**The artefact.** Sheet 6 of 6 (the finale sheet carries both the release note and the form — §7's contact pattern at home-page scale): exhibit label `EXHIBIT F — REQUEST FOR AUDIT`; H2 `FILE A REQUEST`; the release-note paragraph with the page's single `.perm` bar (§11.12) sits *above* the form — the visitor reads what the bureau will not release immediately before being asked to trust it with their own details; that juxtaposition is the conversion argument, made structurally. The form (§11.16): fields `REQUESTER NAME`, `ORGANISATION`, `CONTACT ADDRESS` (email), `NATURE OF REQUEST` (3-line textarea); required markers on name and email; submit box `FILE THIS REQUEST`. The watermark (§11.12) sweeps behind this sheet.

**Scroll + interaction timeline:**

| Beat | What fires |
|---|---|
| Sheet top at 62% vh | Finale trigger (F0): watermark sweep begins (1600ms, §11.12). The release note's ordinary bars (2) lift per §11.1; the `.perm` bar is skipped by the queue — visibly skipped, in sequence, which a returning visitor who knows the mechanic will *notice*: the queue's silence at that slot is the loudest beat on the page. |
| F0+≈900ms | The note's bars done; the form is at reading position, blank, lines at rest weight. No stamp yet — this sheet stamps only when the *form* completes, not when it is read. (Authoring ruling: the finale sheet's stamp is the `REQUEST FILED` stamp itself; the sheet carries no CLEARED stamp. One sheet, one stamp — §4's law — and the finale's stamp belongs to the visitor's act, not the bureau's reading. The counters' denominator counts this sheet as stamped when a request is filed; a visitor who reads but does not file leaves the count at 5/6 and the dial at LVL 5 anyway — LVL thresholds are fractions, and .85 was crossed at sheet 5's stamp: p = 5/6 ≈ .833… — correction, made honestly here because a builder will hit it: .833 < .85, so the dial reads LVL 4 for a non-filing visitor. That is *correct* and even thematic — full clearance is granted when the file's business is concluded — but the §6.6 claim "LVL 5 = this file, fully read" then needs the denominator to be *readable* sheets: the finale counts toward the dial when its note is read (bars resolved), and toward the counters only when stamped. Two instruments, two denominators, each defined: dial denominator = sheets; dial numerator = sheets whose release sequence has completed (finale included, on read-completion); counter denominator = stampable sheets; counter numerator = stamps landed. On this page both denominators are 6; the numerators diverge by design at the finale. §11.6/§11.7's simpler definitions hold for every sheet except a conversion finale, where this ruling governs.) |
| Visitor focuses field 1 | §11.16 focus beat: line to 2px, caret block in. |
| Visitor submits with email malformed | Memo types at the form head: "MEMO: THE CONTACT ADDRESS DOES NOT ACCEPT MAIL. CHECK THE SPELLING AND RE-FILE." The email field gains its `INCOMPLETE` mini-stamp and dashed line; focus moves to it at +320ms. No other field is disturbed; the visitor's typed name and request keep their 1.5px filled lines — an error never erases ink. |
| Visitor corrects, submits | Submit box → `FILING…` (typed, ≈270ms). Fields lock read-only. |
| Server confirms (+640ms in this rehearsal) | `REQUEST FILED` stamp slams at the form's top-right (full §11.2: 320ms, dip, bleed); submit box re-sets to `FILED — REF 114-K-238` in `--stamp`; counters tick 6/6 and the pill turns green (§11.7's completion frame) — the file is closed by the visitor's own act; a filed slip toast (§12) confirms from the rail: "REQUEST FILED — REF 114-K-238". The `COPY — YOUR RECORD` rendering replaces the form. |
| Visitor scrolls to footer | The custody sign-off (§11.17) types `THE VISITOR — 6 / 6 PAGES`. The ledger agrees with the pill, the dial, and the toast — four instruments, one set of books. |

**Failure rehearsal.** Server never responds: +8s `FILING DELAYED — DO NOT RE-FILE` + memo; +20s `FILING UNCONFIRMED` + retry (§11.16). The stamp never lands on an unconfirmed filing — a stamp the server didn't earn is the form's version of a bar that never lifts: the theme's one unforgivable lie, in either direction.

---

## 15. Full-page scroll choreography map — the home page, top to footer

One page, one file, read once through. Every beat in order; instruments = dial (§11.6) and counters (§11.7). The emotional arc is §1's: suspicion → procedure → earned intimacy → respect.

| Scroll band | On screen | Beats that fire | Instruments | What the visitor feels |
|---|---|---|---|---|
| Load, no scroll | Cover sheet, sealed | Ceremony: typing (300ms), bars (450ms→), lettering, DECLASSIFIED stamp (≈4.9s, §14.1) | Counters 0→1/6 at the stamp; dial LVL 0→1 | Suspicion, then the first surprise: the file *opens itself for them* — withholding that reverses in the open |
| Pin travel (0–120vh) | Cover pinned; Exhibit A rising beneath | A's sequence arms under the pin; cover's marquee running; dust in the lamp pool | Dial scrubbing on the cover's certified fraction | Procedure begins; the visitor learns the rule of the world: reading is clearance |
| Exhibit A (findings) at reading position | Findings sheet, slips | Sheet bars in order (90ms stagger); slips' masks (120ms stagger), clause bars; sheet CLEARED stamp | Counters 2/6; dial crosses .25 → LVL 2 mid-sheet | Competence: the mechanic is now fluent; the findings themselves carry the weight |
| Exhibit B (custody transfer) | §8's sheet | Sleeve event (slit, eye-bar last, mini stamp); 3 body bars; CLEARED stamp | Counters 3/6; dial → LVL 3 at the stamp | The file's story darkens (the keys changed hands); the procedure stays calm — the contrast is the brand |
| Exhibit C (chain of custody) | §14.2's sheet | Evidence line scrubs 70%→30%; circles fill; entries uncover; sleeve facsimile; CLEARED stamp | Counters 4/6; dial crosses .65 → LVL 4 | Earned intimacy: the visitor is now *inside* the chain, watching custody pass hand to hand at their own reading speed |
| Exhibit E (service folders) | Three folders | Folder springs on hover; the sheet's own stamp is absent by design — this sheet certifies nothing; it *offers*. (Its counter slot: the folders sheet is counted in the dial's denominator as read on sequence completion — its bars (2, in the intro paragraph) resolving — and is not a stampable sheet for the counters. Denominators per §14.3's ruling: dial 6 sheets; counters /5 stampable… — no. Correct the books here, finally and completely: **counters' denominator counts stampable sheets. On this page the stampable sheets are 1 (cover), 2, 3, 4, and 6 (finale, on filing) = 5 until the finale files, when the finale joins as the 5th stamp.** A denominator that changes when the finale files is unacceptable — so the ruling is: the finale is stampable from the start (its stamp is the filing stamp), the denominator is 5 for the counters and 6 for the dial, and both instruments are *labelled* accordingly: the pill reads `DOCUMENTS RELEASED n / 5` (documents = stamped sheets) while PAGES FREED counts *pages* — sheets whose release sequence completed, finale included on read — `n / 6`. The two counters were always counting two different things (§6.7: the bureau announces documents; the file notes pages); Part II fixes their denominators to match their names. §6.7's "/6" examples were written before this ruling; this paragraph supersedes them.) | Earned intimacy, continued: the ask is near, and the file has spent four sheets proving it deserves one |
| Exhibit F (finale: release note + form) | §14.3's sheet | Watermark sweep; note's bars lift, `.perm` skipped in sequence; form interaction; on filing: stamp, pill turns green | On filing: documents 5/5, pill green; pages 6/6; dial LVL 5 (crossed .85 during this sheet's read) | Respect: one thing stays classified (§6.12), and the visitor's own act closes the file |
| Footer (desk) | Custody sign-off | `RECEIVED BY` typing — the last motion in the file; then stillness | The typed count agrees with both counters | The file is theirs now; the bureau has signed it over and stopped talking |

**Map laws.** (1) No beat fires before its band — a visitor who jump-scrolls to the finale triggers catch-up per §10 (force-lift stagger 30ms, sequences in document order, no pile-up) and the map still reads in order. (2) Exactly one sheet's sequence is *performing* at any moment; scrubbed instruments (dial, line) are continuous and exempt. (3) The map is the test script: §17's final pass scrolls the page at three speeds (slow read, steady scroll, jump) and verifies every row.

---

## 16. Whole-page performance budget

The theme is heavy with ceremony and light with machinery; the budget keeps it that way. All figures are ceilings for the home page (the heaviest page type); other page types inherit them as outer bounds.

**Asset weight.**
- Fonts: Courier Prime 400 + 700 + Italic and Archivo (variable, wdth+wght) — woff2, subset to Latin + the theme's glyph extras (—, ·, ▾, ✓): **≤120KB total**, `font-display: swap` with the §3 law-5 fallbacks (a FOUT that reflows >2% fails §10). Preload the two faces the cover uses (Courier Prime 400, Archivo 800) only.
- CSS: **≤30KB gzipped** for the theme layer. JS: **≤45KB gzipped** — the shared loop, observers, ceremony timers, and form logic; no animation library (every motion here is CSS transitions/animations or the one rAF loop; a tween library is 20KB spent re-implementing §5's four easings).
- Data-URI assets: noise tile ≤2KB, stamp texture ≤1.5KB — inline, zero requests.
- Images: evidence sleeves only; each ≤1200px wide, WebP/AVIF, **≤180KB each, ≤4 sleeves per page, ≤700KB total**, all `loading="lazy"` except a sleeve inside the cover's first viewport (the cover carries none by design, §14.1 — so in practice all sleeves lazy-load).
- **Initial load (cover + furniture): ≤450KB. Full page, all sleeves loaded: ≤1.2MB.**

**Frame budget.** The shared rAF loop performs **≤8 style writes per frame** in the worst case (dial 2, evidence line 1, parallax 3 layers, watermark 1 while sweeping, folder tilt 1) and zero layout reads — all geometry (sheet offsets, scrub windows, entry baselines) is measured at init and on debounced resize, cached, and read from the cache. All animated properties are composited (`transform`, `opacity`, `clip-path`, `stroke-dashoffset`); `filter` appears only inside §11.5's 640ms event and is removed at its end. **No long task >50ms** may be attributable to theme code during scroll or ceremony (§10's 100ms is the failure line; 50ms is the budget — a build between the two passes the gate and fails this budget, and is optimised before ship). Click-to-first-frame for the folder stamp and the form's filing state: **<100ms** (INP budget for theme interactions: <200ms worst, <100ms typical).

**Concurrency budget.** At most **3 ceremony animations** (a peel, a slam, a mask) plus **2 ambient layers** (noise, dust) at any instant — the staggers in §11 exist partly to enforce this; a scroll speed that would queue more collapses stagger to 30ms rather than overlapping more.

**Cut order — when the budget is exceeded** (sustained <40fps on the reference mid-tier device, or long-task violations), degrade in exactly this order, re-measuring after each step; stop as soon as the budget holds:
1. Freeze the noise crawl (static grain — §11.9).
2. Halve the dust, then remove it.
3. Kill the dial needle tremor.
4. Drop parallax layers: noise-field layer first, then staple-shadow layer (sheets' own 1.0× is not a layer and never drops).
5. Folder tilt: spring → 120ms tween (§11.10).
6. Sleeve reveal: drop the blur property (§11.5).
7. Quantise dial/line scrub updates to 4% steps (§11.8).
8. Marquee: pause except when its sheet is centred.
**Never cut, at any step:** bars and their fallback stack, stamps, counters, the gate's fallback (plain navigation), the form's function, or any reduced-motion behaviour. Ceremony degrades; the document and its paperwork do not.

**Measurement protocol.** Reference device profile: 4× CPU throttle + Moto G-class viewport in the browser's device emulation, plus one real mid-tier Android pass before ship. Scroll pass at steady speed top→footer: record fps floor, long tasks, and per-frame write counts against the caps above. The §10 gate's throttled-scroll check (50fps+, no >100ms task) is run on the same pass — one rehearsal, two verdicts.

---

## 17. Build-order checklist

Build in this order. Each step leaves the page shippable-in-principle (the static document exists from step 2 and is never broken by later steps — enhancements layer onto it, per the fallback architecture).

1. **Tokens & type.** Define every §2 token and §11 element-scoped token; load the two families with their §3 fallback stacks; verify the ≤2% reflow rule with fonts blocked.
2. **The static document.** Sheets, exhibit labels, page numbers, full text with redaction spans as plain text; the index **generated from the sheets** (never hand-written, §11.13); counters and dial in their complete static states. Gate: §10's no-JS checks pass *now*, before any motion exists.
3. **Furniture.** Top bar, rail (dial SVG + counter chip), bottom rail-bar for the mobile band; footer custody block complete and static.
4. **Bars.** The `.rx`/`.bar` structure, per-fragment generation, the lift queue (document order, reading position), the 800ms per-bar timers, the 7s sweep — and the `.perm` exclusion implemented and **tested in all three code paths** (§11.12) before proceeding. Tests: JS off; observer broken; mid-lift JS kill.
5. **Stamps & counters.** Stamp component (all scales), stamp-land events (idempotent per sheet, §11.7), counters wired with their §15 denominators (pill = stampable sheets, rail = pages), dial numerator rules incl. the finale ruling (§14.3).
6. **The one rAF loop.** Dial scrub, evidence line, parallax layers, watermark sweep — all four on the single loop with lerp 0.16; verify no second loop exists (§10). Cache all geometry here.
7. **The cover ceremony.** Typer, lettering (seeded tables), hero timeline chaining (§14.1), sticky pin, hard-scroll completion. Verify readability deadline ≈2.5s.
8. **Exhibits.** Sleeves (slit + blur + eye-bar + mini stamp), slips (mask, pin, severity logic), custody block masks.
9. **Folders, gate, loader, annex.** Folder springs + session stamps; gate with its 150vh rule and interrupt; loader with its 300ms/6s/12s beats; annex-sheet modal + select drawer (§12).
10. **The form.** Three line-weights, memo errors, filing timeouts (8s/20s), filed state with real reference, autofill wash.
11. **Finale & footer.** `.perm` tooltip (verbatim string), watermark, footer typing + ledger agreement check (footer vs pill vs rail vs dial — four instruments, one set of books, §14.3).
12. **Ambient, last.** Noise + dust, with their pause rules. (Atmosphere is fitted to a finished document, never used to make an unfinished one feel alive.)
13. **Reduced-motion pass.** Run the entire page under `prefers-reduced-motion` against §6's per-element variants and §11's matrices — every element's static form verified, not assumed.
14. **Breakpoint passes.** Full read-throughs at ≥1200, 768–1199, and <768 against §11's per-element band rules (hinges, gauges, grids, stamp placements — including the footer's stamp-word-on-manila check, §11.17).
15. **Lints (automatable, all must pass).** Exactly one `.perm` per page · bars ≤9/sheet, ≤40/page · cover ≤5 paragraphs, ≤6 bars · denominators computed from DOM (grep finds no hardcoded totals) · index generated, not duplicated · every `--stamp` usage maps to a certification (green audit, §10) · stamp words never over `--desk` · no exclamation mark in any copy string (§13) · banned labels absent (`Submit`, `Learn more`, `Click here`).
16. **The choreography rehearsal.** §15's map scrolled at three speeds (slow read / steady / jump-scroll); §16's measurement pass; §10's quality gate in full. Ship requires: gate all-pass **and** budget within §16 — both, not either.

*End of Part II — Deepening (50x standard). End of Theme 003 — Redacted Archive (Expanded).*
