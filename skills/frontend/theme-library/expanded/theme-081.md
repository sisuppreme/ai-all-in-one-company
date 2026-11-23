# Theme 081 — Dead Reckoning (50x Expansion)

*Navigation before satellites — chip log, compass, chronometer, and an honest estimate. The site is a ship's reckoning board where every position is "by DR": estimated, initialled, and corrected when a fix is taken. The page never claims to know where it is. It shows its working.*

---

## 1. Concept & world

Dead reckoning is the discipline of knowing where you are by reasoning from where you were: a known departure, a course steered, a speed through the water, and time. It is always wrong by a little, and the navigator's craft is not eliminating the error but **managing it in the open** — plotting the estimate in pencil, taking a fix when the sky allows, inking the correction, and writing the size of the error into the log beside it, initialled. This theme takes that discipline as a complete design language: the page is a chart on a chartroom table, the visitor's scroll is the passage, and every figure on the page carries the method that produced it.

**The theme's one law: no figure without its method.** Every position printed anywhere in this theme is labelled **BY DR** (estimated from course, speed and time) or **BY OBSERVATION** (fixed from something outside the reckoning — a star sight, a landmark bearing, a satellite the theme pretends not to have). The two methods never quite agree, and the size of their disagreement is always printed, never rounded away, never hidden in a tooltip. A page in this theme that printed a single, clean, unlabelled position would be lying in the theme's own terms — that is the failure the whole system is built to prevent.

The world is specific and closed: a chartroom in the last decades before satellite navigation. Oak-dark wood, chart cream paper, plotted pencil grey, fix red reserved for corrections, compass brass for instruments. The instruments are a chip log (speed), a compass (course), a chronometer (time) and a pair of dividers (measurement). Nothing enters the page that could not sit on that table: no glassmorphism, no GPS blue, no satellite iconography, no "live tracking" language. The aesthetic is not nostalgia — it is an epistemology. The theme is for products whose honest story is *we estimate, we check, we correct, and we show you the error*.

**Best fits.** Logistics and fleet platforms that forecast ETAs and would rather show a confidence story than a fake-precise arrival time; maritime tech (passage planning, weather routing, port-call prediction); risk, forecasting and planning products where the estimate/correction rhythm *is* the product; analytics tools that reconcile projected against actual; any brand whose differentiator is candour about uncertainty. The worked examples in this expansion use a passage-planning product — the fictional **Kestrel Passage** service — and one declared day's reckoning (§6.16) as the page's content.

**When NOT to use it.** Anything that genuinely knows: real-time vehicle tracking, emergency response, turn-by-turn navigation, medical or safety monitoring — contexts where the user needs a fact, not an estimate with a pedigree. Anything aimed at children (the register is a professional log, not a storybook). Anything whose brand promise is effortless automation — this theme celebrates skilled human correction, initialled by hand. And never as pirate cosplay: no skulls, no "ahoy", no treasure-map X. The chart is a working document, not a costume.

**The emotional register.** Calm, competent, quietly proud of its own fallibility. The page moves at a pencil's patience. Corrections are not embarrassments; they are the two best moments of the day, and the design gives them the theme's only red.

## 2. Palette

Five anchors from the original entry, preserved exactly, plus six derived tokens. The page is a cream chart on an oak table: light paper, dark surround. There is no dark-mode inversion — a chart is read under the chartroom lamp, and the "dark scheme" is simply more table and less chart (the footer and 404 live on the oak).

| Token | Hex | Role | Usage ratio | Pairing & contrast (measured) |
|---|---|---|---|---|
| `--cream` | `#EFE7D3` | Chart paper — the page's main surface | ~62% | Ground for `--ink` (12.17:1), `--pencil` (6.47:1), `--fix` (4.88:1) |
| `--oak` | `#2A2118` | Chartroom wood — surround, masthead band, footer | ~24% | Ground for `--cream` (12.82:1) and `--brass` (4.30:1, instruments only) |
| `--pencil` | `#55504A` | Plotted estimates — DR figures, the course line, pencil annotations | ~7% | On `--cream` 6.47:1 — AA for all text sizes; the colour of everything not yet confirmed |
| `--ink` | `#2B2620` | Inked fact — observed figures, body prose, corrected values | ~4% | On `--cream` 12.17:1; on `--cream-dim` 9.99:1. Derived token (the original's "inked observed values" made explicit) |
| `--fix` | `#B03A2E` | Fix red — corrections, sight lines, fix moments ONLY | ~1.5% | On `--cream` 4.88:1 (AA normal text); `--cream` on `--fix` 4.88:1 for the BY OBSERVATION chip |
| `--brass` | `#A97E2F` | Compass brass — instruments, rules, the needle, cartouche hairlines | ~1.5% | On `--oak` 4.30:1 — instruments and rules only, **never text**; on `--cream` 2.98:1 — forbidden for text, licensed for hairlines only |

**Derived tokens.** `--oak-deep #1C150E` — the table in shadow: footer ground and the 404's surround (`--cream` on it 14.65:1). `--cream-dim #DFD2B2` — aged chart paper for secondary panels, the reckoning table's banding, card backs (`--ink` on it 9.99:1). `--pencil-soft #7A746B` — the graticule and faint pencil (3.76:1 on cream — **decorative only, never text**; lat/long grid lines, the un-darkened pricked points). `--fix-deep #8E2B21` — fix red pressed: hover/active states of fix controls, the struck-through estimate's replacement at small sizes (6.77:1 on cream). `--brass-lit #C49A45` — the needle's lit edge and the compass rose's north point on oak (6.06:1 — still instruments, never text).

**Rules that keep the palette honest.**
- **Pencil is a claim, ink is a fact.** Any figure in `--pencil` is an estimate and must carry its BY DR label within the same line; any figure promoted to `--ink` must have earned it (a fix, §6.4/§6.7). Colour is the audit trail.
- **Fix red is rationed.** It appears at fix moments, sight lines, correction figures and the BY OBSERVATION chip — a census of licensed surfaces is part of the quality gate (§10). Red is never an error colour in this theme: an error here is a *discrepancy*, printed in pencil with its size, not shouted in red. Form errors (§6.13) are ink text with a ruled underline, not red alerts.
- **Brass never carries words.** It draws rules, rings, the needle, the cartouche's hairline. The moment brass sets a label, the chart turns into a pub sign.
- **The two forbidden pairings** are `--pencil` on `--oak` (1.98:1 — pencil belongs on paper, never on the table) and `--brass` text on `--cream` (2.98:1). Both are gate-checked (§10).

## 3. Typography

Two families only, as the original entry rules: **Cormorant Garamond** for display and prose, **IBM Plex Mono** for every figure, log entry, position, time and label. There is no third voice and no handwriting font — the "hand" of this theme is the pencil *line* (SVG stroke), never a script typeface pretending to be one.

**Type laws.**
1. **Numbers are mono, always.** Positions, times, distances, bearings, errors, speeds — if it can be checked, it is set in IBM Plex Mono with tabular figures. Cormorant never sets a numeral in anger: a display headline may contain a spelled-out number ("Twelve hours by dead reckoning"), never a digit.
2. **Estimates and facts are set alike and coloured apart.** DR and observed figures use the same mono face and size; only the colour (pencil vs ink) and the label differ — so the eye compares values, not typography.
3. **The log voice is uppercase, letterspaced, small.** Log labels, chip labels and margin notes: Plex Mono 11–12px, uppercase, letter-spacing 0.14em. It is the register of a man writing in a book he does not own.
4. **Cormorant is for sentences a person would say.** Headlines, prose, the cartouche title. Never for labels, buttons or data. Buttons are log voice (mono, uppercase).
5. **Positions have one format, everywhere:** `41°46.6′N 012°05.6′W` — degrees, decimal minutes to one place, hemisphere letters, set in mono, never abbreviated, never rounded differently in different places. The footer, the table and the form confirmation print the same string for the same position (the one-record rule, §6.16).

**The scale.**

| Role | Face | Size / line-height | Tracking | Notes |
|---|---|---|---|
| Cartouche title (display) | Cormorant Garamond 500 | 64px / 1.02 (≥1200px); 44px (<768px) | +0.01em | The only display setting; lives inside the cartouche (§6.2) |
| Section heading | Cormorant Garamond 500 | 40px / 1.1 | 0 | Headed by its log time in log voice above it |
| Sub-heading | Cormorant Garamond 600 | 27px / 1.2 | 0 | Rare; mid-section only |
| Prose body | Cormorant Garamond 500 | 20px / 1.52 | 0 | Measure capped at 62ch (§4) |
| Log entry figures | IBM Plex Mono 400/500 | 14px / 1.7 | 0 | Tabular; the page's data register |
| Log labels & chips | IBM Plex Mono 500 | 11.5px / 1.4 | +0.14em, uppercase | BY DR / BY OBSERVATION / margin notes |
| Margin ruler numerals | IBM Plex Mono 400 | 11px / 1.0 | +0.05em | Miles run, printed vertically in the chart margin (§6.15) |
| Footer positions | IBM Plex Mono 500 | 15px / 1.6 | 0 | The dual position (§6.6) — the largest mono on the page |

**Font loading.** Both families subset to Latin + the degree/prime glyphs (° ′ ″ · —); Cormorant 500/600 + italic 500 (prose emphasis only), Plex Mono 400/500. Total ≤ 96KB woff2, `font-display: swap`; the fallback stack (Georgia, 'Times New Roman' / ui-monospace, 'Courier New') is metrically tolerated because all figures live in reserved mono boxes (§4) — a font swap must never move a printed position.

## 4. Layout language

**The chart is the page.** One large cream chart surface sits on the oak surround and carries almost everything: the course line is plotted across it diagonally (a gentle WNW ascent, ~285° made visible), and the day's log entries are arranged along the line in reading order, each entry a ruled log block offset alternately above and below the line like soundings written beside a track. The visitor does not scroll a feed; they travel a plotted line, and the layout makes the scroll *mean* distance.

**Geometry of the chart.** At ≥1200px the chart is a centred sheet, max-width 1240px, with a 64px margin inside its edge — the margin is a working margin: the miles-run ruler (§6.15) lives in the left margin, the compass (§6.5) in the top-right corner of the sheet, and margin notes (set/drift findings, chronometer error) are written in the right margin in log voice, rotated 0° (charts are annotated level, never at jaunty angles). The course line's drawn scale is declared in the margin, because a chart that hides its scale is a picture: **along-track 9.0 px per nautical mile; cross-track error drawn at quarter scale, 2.26 px/nm, as charted** — so the day's 112.8 nm run spans ≈1,015px of line, Fix I's 3.1 nm error shows as a 7px offset, and Fix II's 6.2 nm as the maximum 14px (§6.3). The exaggeration is stated, not smuggled.

**Grid and rhythm.** Inside the chart, content sits on a 12-column grid with a 28px baseline rhythm; log entries are ruled blocks (hairline `--pencil-soft` rules above and below, like a log book's printed lines) spanning 5 columns, offset from the course line by a 48px clear channel so the line never strikes through text. Prose measure caps at 62ch. Sections are not separated by whitespace bands or colour changes — they are separated by *time*: each log entry begins with its hour in log voice, and the passage's rhythm is hourly. Density is log-book density: generous ruled space inside entries, no card shadows anywhere (paper does not cast shadows on paper), separation by rule and position only.

**The oak surround.** Masthead and footer are oak — the table the chart lies on. The transition from oak to cream is a hard edge with a 1px `--brass` hairline (the chart's taped edge, §11). Above the chart, the masthead carries the service name and the log-index navigation (§6.10); below it, the footer (§6.6) prints the day's end position two ways. The chart sheet itself never scrolls internally; the page scrolls, the marker travels (§6.3).

**Density rules.** One developing idea per viewport: at any scroll position the visitor sees at most one log entry in full, the course line, and the margin instruments. The two fixes (§6.4) get a full viewport each — they are the day's events. Nothing competes with a fix while it happens.

**Breakpoints in the layout language.** ≥1200px: as above. 768–1199px: chart margin shrinks to 36px, log entries span 8 columns and sit *below* the line only (the alternation is a wide-chart luxury), drawn scales halve (along-track 4.5px/nm, cross-track 1.13px/nm — re-declared in the margin). <768px: the chart becomes a vertical track — the course line runs down the left third as a ruled channel, entries stack in full-width ruled blocks to its right, the margin ruler moves to the top of the sheet as a horizontal miles-run strip, and the compass shrinks to a 64px instrument in the masthead (§6.5). The dual footer (§6.6) stacks its two positions one above the other, DR first, observation second, the margin between them printed between.

## 5. Full motion system

Every motion in this theme is a navigator's action or an instrument's behaviour. There are exactly five named easings, one shared scroll loop, two licensed ambient behaviours (the needle's tremor, §6.5; the chronometer's tick, §6.17), and nothing else moves without a trigger the visitor gave it.

**Named easings.**
- `--ease-plot` — the pencil's hand: `cubic-bezier(.45,.02,.35,1)`, used with programmed speed variation (§6.1) so the stroke hurries over open water and hesitates at landfalls. For line draws of 1200–2600ms.
- `--ease-snap` — the fix: `cubic-bezier(.2,.9,.25,1)`, 180ms. The fastest motion on the page; correction is decisive.
- `--ease-drift` — the marker's travel: not a CSS easing but the shared loop's lerp factor **0.12** (§6.3); the marker always trails the scroll slightly, as a plotted position trails the ship.
- `--ease-unroll` — paper settling: `cubic-bezier(.3,.7,.2,1)`, 700ms, for the chart unroll (§6.14) and sheet transitions.
- `--ease-ink` — a figure drying from pencil to ink: `cubic-bezier(.4,0,.3,1)`, 450ms, colour and weight only — figures never move when they are inked (§6.7).

**The shared loop.** One `requestAnimationFrame` loop owns every scroll-scrubbed value: the DR marker's position and offset (§6.3), the pricked points' darkening (§6.9), the margin ruler's fill (§6.15), the counters' scroll-driven readings (§6.17) and the footer's live positions (§6.6). Each registers a target (from scroll) and a current value lerped at 0.12 per frame; the loop sleeps when all values settle within 0.1px and no ambient behaviour is armed. No element runs its own scroll listener or its own loop. Scroll is read, never hijacked: no scroll-jacking, no pinned hijack — the two fix scenes use a *hesitation*, not a pin (§6.4).

**Motion terms, translated or refused.**
- *Scroll-triggered reveals* — the plot advancing and entries being "entered up" as the marker reaches them (§6.11): content is printed from the start; scroll *annotates*, it does not reveal. Nothing fades in from nothing.
- *Parallax* — refused as decoration; the only layered motion is the chart's graticule drifting 0.92× against the sheet edge in the hero (§6.15) — the paper breathing on the table, ±6px over the full hero scroll.
- *Pinned scenes* — refused; the fixes use a 240ms hesitation of the marker at the threshold while sight lines draw (§6.4), then release. The reader's scroll is never confiscated.
- *Masked line reveals* — the cartouche border (§6.2) and sight lines (§6.4) draw as strokes; prose is never masked.
- *Blur-to-sharp* — refused: a chart is in focus or it is fog, and fog is the 404's subject (§6.18), not a transition.
- *Animated counters* — the log readings (§6.17): they count because the ship moves, scrubbed to scroll, tabular, never from zero.
- *Progress indicator* — the course line itself + the margin ruler (§6.15). No progress bar exists.
- *Marquee* — refused: nothing on a chart scrolls sideways; the day's entries are a line you travel, not a ticker.
- *Kinetic typography* — refused: the log does not perform. The only type that changes is a figure's colour when inked (§6.7).
- *Hover physics* — the divider ring (§6.8): instruments, not springs. Buttons press 1px (a stamp, §11).
- *Page transitions* — the chart unroll (§6.14).
- *Skeleton loading* — the unplotted chart (§6.14): a blank ruled sheet, graticule printed, awaiting its plot.

**Master timing table.** Plot draw 2400ms (§6.1) · cartouche border 1400ms (§6.2) · marker snap at a fix 180ms (§6.4) · sight lines 620ms (§6.4) · click-to-fix 700ms total (§6.7) · divider ring settle 260ms (§6.8) · unroll 700ms (§6.14) · ink promotion 450ms (§6.7) · needle tremor continuous, ±2°, seeded (§6.5). Nothing else on the page animates longer than 700ms except the entrance plot.

**The one-cause rule.** Every scroll-driven value derives from the marker's single progress value `p` (0 at 0800, 1 at 2000) computed by the shared loop — the ruler, the counters, the pricks and the footer all read `p`, so they can never disagree with each other. If two instruments on the page ever show inconsistent states, the bug is in the wiring, not the design.

## 6. Signature elements

The nine original elements (§6.1–§6.9) deepened, plus nine page-family elements (§6.10–§6.18): navigation, log entries, the reckoning table, the conversion form, the loader/transition, the chart surface, the passage record, the counters, and the 404. Every figure any element prints traces to the one passage record (§6.16).

### 6.1 The pencil plot (entrance)

**What & why.** On load, an SVG course line draws itself across the hero chart in real time — about 2.4 seconds, with a pencil's hand-speed variation — and ends in a small pencil cross labelled `0800 — BY DR`. The page's map is drawn by the act of arriving: the reader watches their position being estimated before they read a word. It merges with content because the line being drawn is the page's actual course line — the same line the marker will travel (§6.3), the entries will hang from (§6.11), and the fixes will correct (§6.4). It is not an intro animation laid over the page; it is the page being plotted.

**Structure.** One inline SVG spanning the hero chart, containing: the graticule (§6.15), the course path (a single `<path>`, stroke `--pencil`, 1.5px, round caps, slight stroke-width variation via two overlaid paths at 1.5px/0.75px for a graphite edge), the departure cross (two 9px strokes), and the `0800 — BY DR` label as real HTML text positioned over the cross (never SVG text — it must be selectable and readable by assistive tech). The draw is `stroke-dasharray`/`stroke-dashoffset` driven by the shared loop's clock, not CSS, so the watchdog can complete it instantly. The full path and all hero content are in the DOM from first paint; the dash offset is the only hidden thing, and it is JS-armed.

**Motion spec.** Total 2400ms, `--ease-plot`, with programmed speed variation: the draw parameter advances at 0.82× through the two "coastal" thirds (the pencil is careful near land) and 1.24× across the open middle — implemented as a piecewise rate on the same easing, not three animations. The cross draws in the final 180ms (two strokes, 90ms each). The label is printed throughout (it is HTML), but its colour settles from `--pencil-soft` to `--pencil` as the cross completes. Trigger: first paint + 200ms, once per session; repeat visits in the same session get the 500ms short form (a single confident stroke).

**Choreography timeline.** 0ms chart sheet settles (§6.14 unroll already complete or skipped) · 200ms plot begins at the departure point · ~900ms first third drawn (slow, coastal) · ~1500ms open-water third (fast) · ~2220ms final third slows · 2400ms cross strokes land · 2580ms cartouche border begins (§6.2). The headline is readable from 0ms — the plot decorates nothing the reader is waiting for.

**State matrix.** *Rest (pre-trigger / no-JS):* the complete line drawn, cross and label printed — the finished chart. *Drawing:* as above; the line behind the pencil point exists, ahead of it does not — the one licensed exception to "content first", because the *content* (text, entries, figures) is all present; only the line's stroke is in progress, and the watchdog bounds it. *Drawn:* hands over to §6.3 (the marker takes the line). *Scrolled-past:* never replays; scrolling back up shows the finished plot. *Disabled:* n/a (not an interactive element). *Touch:* identical — time-triggered on every device.

**Content-merge.** The plotted line is the passage record's course (§6.16) rendered at the declared scale (§4): its shape, its two fix points and its terminus are the record's geometry. Change the record and the hero redraws itself truthfully.

**Breakpoints.** ≥1200px: full 2400ms draw across the 1240px sheet. 768–1199px: 2000ms, scales halved (§4). <768px: the line is the vertical channel (§4); draw shortens to 1400ms top-to-bottom; speed variation kept (it is the element's character, not a luxury).

**Edge cases & failure modes.** Slow first paint: the plot waits for the chart's fonts-or-fallback (it starts on `requestAnimationFrame` after first contentful paint, not on DOMContentLoaded, so it never draws under a blank sheet). Tab hidden mid-draw: the loop sleeps; on return, if elapsed > 4000ms the line snaps complete (watchdog state). Very long course (a record with more legs): the path is still one stroke; draw duration caps at 3000ms by raising the open-water rate, never by cutting the line. Scroll during the draw: permitted; §6.3's marker does not arm until the draw completes or the watchdog fires.

**Fallback & watchdog.** No-JS: the path has no dash offset — the line is simply drawn; the hero is a finished chart. **Watchdog: 4000ms** from trigger — if the draw has not completed, dash offset is set to 0 and the cartouche sequence (§6.2) proceeds. If SVG is unavailable (ancient embed contexts), a pre-rendered PNG of the plotted chart at the record's geometry ships as the hero image with the same alt text.

**Reduced motion.** No draw: the line is printed complete, the cross and label in place. The hero is a chart already plotted — which is, the theme notes, how most charts are met.

**Accessibility.** The SVG is `aria-hidden="true"`; the departure is real text beside it: the label `0800 — BY DR` plus a visually-hidden sentence "The course line is plotted from the 0800 departure fix." Focus order is untouched (the plot is not focusable). The label's contrast is `--pencil` on `--cream`, 6.47:1.

**Performance & mobile variant.** One path, dash-offset writes only — compositor-friendly, ≤0.2ms/frame. Mobile: same path redrawn in the vertical channel; no extra assets. The SVG (graticule + line + cross) is ≤7KB inline.

**Tokens.** `--pencil`, `--pencil-soft`, `--cream`, `--ease-plot`, `--plot-dur: 2400ms`, `--chart-scale-x: 9.0px/nm` (4.5 at ≤1199px), `--chart-scale-cross: 2.26px/nm`.

### 6.2 Cartouche that draws its own border

**What & why.** The headline sits inside a hand-drawn chart cartouche — the ornamental title frame engraved on real charts — whose border strokes itself in *after* the plot completes, corner flourishes last, leaving the title standing inside a finished, surveyed frame. It merges with content because the cartouche is not a banner around the headline; it is the chart's title block, and like a real title block it also carries the chart's small print: the passage name, the scale declaration (§4) and the day's date line, all set in log voice beneath the title inside the frame. The frame finishing is the page saying: *this chart is now in use.*

**Structure.** An SVG rect-with-flourishes path (four corner scrolls drawn as separate short paths so they can land last) absolutely positioned around a normal HTML block: `<h1>` in Cormorant display, and beneath it a log-voice line — `PASSAGE № 214 · MV KESTREL WIND · LISBON — BOSTON, DAY 1` and the scale note — as real text. The border is two strokes: an outer 1.25px `--pencil` rule and an inner 0.75px `--brass` hairline (brass's licensed cartouche use, §2). Corner flourishes are small spiral paths in `--pencil`.

**Motion spec.** Border draw 1400ms total, `--ease-plot`: long edges first (0–900ms, drawn as one continuous path so the hand never lifts), inner brass hairline 700–1200ms, the four corner flourishes 1150–1400ms staggered 60ms apart, drawn in reading order (top-left first). Trigger: §6.1's completion (or its watchdog), +120ms. Once per session; repeat visits show the finished frame.

**Choreography timeline.** Plot done (2580ms from load) · +120ms outer rule begins · ~3500ms outer rule closes · brass hairline completes ~3780ms · flourishes land 3730/3790/3850/3910ms · frame complete 3980ms. The title is fully readable from 0ms throughout — the frame is drawn *around* standing text, never before it.

**State matrix.** *Rest:* finished frame, all text printed. *Drawing:* as above; text selectable, links (none inside) unaffected. *Drawn:* static forever after; the frame does not redraw on scroll, resize (it rescales, see Breakpoints) or revisit within the session. *Scrolled-past:* unchanged. *Disabled:* n/a. *Touch:* identical timing.

**Content-merge.** The cartouche's small print is data from the record (§6.16) — passage number, vessel, route, scale — so the ornament is also the chart's metadata block. A cartouche whose small print disagreed with the record would fail the figure audit (§10).

**Breakpoints.** ≥1200px: frame around the 64px-padded title block, flourishes at full 22px size. 768–1199px: padding 36px, flourishes 16px. <768px: the cartouche simplifies to a double rule (outer pencil + inner brass) with only the top-left and bottom-right flourishes — a small chart's title block is plainer, and the theme says so rather than shrinking the full ornament into mush.

**Edge cases & failure modes.** Long titles: the copy rules (§12) cap the cartouche title at 9 words; the frame is sized by the text block (SVG scales to the container), so a 3-line title gets a taller frame — the draw duration scales ×1.15 for the longer path, capped at 1600ms. Narrow containers: below 320px the flourishes drop entirely (double rule only). If the plot (§6.1) is skipped by reduced motion or watchdog, the cartouche is simply printed — it never waits on a failed predecessor.

**Fallback & watchdog.** No-JS: border fully drawn (no dash offsets in the shipped markup). **Watchdog: 2000ms** after its trigger — the frame snaps complete. The frame can never be the reason a headline looks unfinished.

**Reduced motion.** Printed complete; no draw.

**Accessibility.** SVG `aria-hidden`; the `<h1>` is the page's single H1; the small-print lines are real text at 11.5px log voice, `--pencil` on `--cream` 6.47:1. The frame is decorative and is never the only carrier of the scale declaration — the same scale note appears in §6.15's margin.

**Performance & mobile variant.** Five short paths, dash writes ≤0.1ms/frame during 1400ms. Mobile: two paths (the simplified double rule). Total inline SVG ≤2KB.

**Tokens.** `--pencil`, `--brass`, `--cream`, `--ease-plot`, `--cartouche-dur: 1400ms`, `--cartouche-pad: 64px` (36px / 24px by breakpoint).

### 6.3 The drifting DR marker

**What & why.** A small pencil cross — the DR marker — advances along the course line scrubbed to scroll, and its path is *offset* from the true route by an error that grows with distance run, exactly as real dead reckoning drifts. Between fixes the offset grows at the record's found rate; at each fix (§6.4) it snaps to zero; by the footer it has grown again to the stated residual. This is the theme's thesis as a progress indicator: progress itself is uncertain here, and the page says so geometrically, in pixels the visitor can watch accumulating. It merges with content because the marker's position *is* the visitor's position in the day — the log entry beside the marker is the hour they have reached, and the marker's offset is that hour's printed error (§6.11), drawn.

**Structure.** An SVG group (two 11px pencil strokes forming the cross, plus a 3px centre dot) positioned on the chart layer (§6.15), moved by the shared loop: its along-track coordinate is the record's course path at progress `p`; its cross-track offset is `error(p) × --chart-scale-cross`, applied perpendicular to the local course direction, always to the same side (the record's set side, §6.16 — the drift is systematic, not random wobble). `error(p)` is a piecewise function of the record: 0 at 0800, rising to 3.1 nm at the 1200 fix, snapping to 0, rising to 6.2 nm at 1800, snapping to 0, rising to 2.0 nm at 2000. A faint pencil "shadow track" — the path the marker has actually taken, offsets included — is drawn behind it at 0.5px `--pencil-soft`, so the drift is visible as a diverging line, not just a displaced cross.

**Motion spec.** Continuous via the shared loop: marker target from scroll, current value lerped at `--ease-drift` 0.12/frame. At fix thresholds the offset component is overridden by §6.4's 180ms `--ease-snap`. Scrolling back up: the marker retreats along the same offset path — drift un-grows symmetrically (the *chart* rewinds; the *log's* inked corrections, §6.4/§6.11, do not unwrite — see §13's reverse-pass rule). No idle motion: at rest the marker is still. A still cross is a plotted position; a jittering one would be a lie about the instrument.

**Choreography timeline.** Scroll-driven throughout: marker leaves the departure cross as `p` passes 0.01 · offset reaches 3.5px (1.55 nm) midway to Fix I · Fix I threshold (§6.4) · offset regrows to 14px maximum just before Fix II · snap · regrows to 4.5px (2.0 nm) at the footer, where §6.6 prints the same 2.0 nm as the stated margin — the geometry and the figures agree, by construction from one `p` and one record.

**State matrix.** *Rest (top of page):* marker sits on the departure cross, offset 0 — the one moment of the day the DR is exactly right, because it is the fix the day started from. *Travelling:* as above. *At a fix:* §6.4 owns the marker for 800ms (hesitation + snap). *Scrolled-past (footer):* marker rests at the terminus cross with its 2.0 nm offset visible beside the true terminus — the chart's final, honest picture. *Disabled:* n/a. *Touch:* identical; scrubbing is scroll, not gesture.

**Content-merge.** The marker is the reading position of the whole page: §6.11's entries key their "entered up" state to it, §6.9's pricks darken as it passes, §6.15's ruler and §6.17's counters read the same `p`. Remove the marker and the page loses its narrator.

**Breakpoints.** ≥1200px: offsets at the declared 2.26px/nm (max 14px). 768–1199px: 1.13px/nm (max 7px). <768px: the chart is a vertical channel (§4); the offset becomes a horizontal displacement from the channel line at 1.13px/nm, and the shadow track still draws. The *figures* never change with breakpoint — only their drawing scale, re-declared in the margin (§6.15).

**Edge cases & failure modes.** Fast scrolling / jump scroll: the lerp catches up within ~400ms; if the jump crosses a fix threshold, §6.4's jump rule applies (the fix is shown already-taken, log inked, no snap owed). Scrolling back above a fix: marker offset re-grows in reverse along the shadow track — geometrically consistent at every `p`, because offset is a pure function of `p`, not of history. Record with different errors: `error(p)` is generated from §6.16's fix list, so any passage record produces a truthful marker. If the chart SVG fails to load its path (corrupt inline SVG), the marker hides and the entries still read in order — the page degrades to a log book, never to a broken map.

**Fallback & watchdog.** No-JS: the marker is printed at the terminus with its final offset, and the shadow track is printed complete — the finished day's chart, which is the honest static summary. **Watchdog:** the shared loop's settle rule — if scroll events stop firing (embed contexts), the marker is placed at the `p` implied by `scrollY` on a 1000ms interval poll; it can never be left behind by a dead listener.

**Reduced motion.** The marker still travels (it is the reader's place, and removing it would strand the log's logic), but it travels *on* the true line with offset 0, and the printed error figures (§6.11, §6.6) carry the drift story in words — the reduced page keeps the numbers and drops the geometry. Lerp becomes a direct cut (no trailing).

**Accessibility.** The marker is `aria-hidden`; its information is fully duplicated in text: each log entry prints its own error figure (§6.11) and the footer prints both positions (§6.6). Nothing about the visitor's place in the day is available only visually — a screen-reader user reads the same log in the same order.

**Performance & mobile variant.** One transformed SVG group + one path draw per frame from the shared loop: ≤0.3ms/frame. Mobile: identical, smaller scales. No canvas, no WebGL anywhere in this element.

**Tokens.** `--pencil`, `--pencil-soft`, `--ease-drift: 0.12`, `--ease-snap`, `--chart-scale-cross: 2.26px/nm` (1.13 ≤1199px), `--marker-size: 11px`, `--fix-error-1: 3.1nm`, `--fix-error-2: 6.2nm` (both generated from §6.16).

### 6.4 The two fixes

**What & why.** Twice in the day, the reckoning is corrected from outside itself. At two scroll depths — the 1200 celestial fix and the 1800 landfall fix — sight lines radiate from the DR marker to three star points (1200) or three landmark bearings (1800), the marker **snaps** 180ms onto the true route, and the accumulated error is written into the log beside it in ink: `Error: 3.1 nm, corrected.` — initialled. These are the page's two set-pieces, and they carry the product story of any forecasting tool: estimate → drift → correction, told by the chart itself. They merge with content because the fix sections *are* content sections — each fix is a full log section explaining what was observed (three star sights at noon; three bearings on the headland at dusk), with the geometry performed around the text, not instead of it.

**Structure.** Each fix is a full-viewport section on the chart containing: the entry text (§6.11's ruled block, enlarged), three sight-line SVG paths from the marker's pre-fix position to three plotted points (star points: small four-point star glyphs in `--ink`; bearings: short ruled lines to named headland marks at the chart's edge), the correction line — a log line whose DR figure is struck through in pencil and whose observed figure is set in `--ink` with the `BY OBSERVATION` chip (§11) and the initials `J.M.` — and the error statement in log voice. The snap moves the marker (§6.3); the section's own geometry is drawn by stroke animation from the shared clock.

**Motion spec.** Sequence at the threshold (when `p` crosses the fix point): (1) **hesitation** — the marker's lerp factor drops to 0.03 for 240ms as it nears the point (the navigator pauses; §5's licensed hesitation, not a pin — scroll remains live and the sequence can be scrolled past); (2) sight lines draw, 620ms, `--ease-plot`, staggered 90ms, from marker outward; (3) the marker snaps along the offset vector to the true line, 180ms `--ease-snap`; (4) the correction line inks: strike-through draws 200ms, observed figure cross-fades pencil→ink 450ms `--ease-ink`, initials fade in last at +500ms. Total ≈1.55s if the visitor lingers; every stage is skippable by scrolling on (the end state applies immediately).

**Choreography timeline.** Threshold crossed · +0ms hesitation begins · +240ms first sight line · +330ms / +420ms second and third lines · +860ms all lines drawn · +880ms snap (180ms) · +1060ms strike-through · +1260ms ink promotion · +1560ms initials land; the fix is complete and the marker resumes §6.3 with offset 0.

**State matrix.** *Rest (before):* the section reads as a normal log section with its figures in pencil — the fix is promised by the section's heading (`1200 — A FIX BY OBSERVATION`), not pre-performed. *Performing:* as above. *Taken:* lines remain drawn at 40% pencil (the working stays on the chart), correction inked, marker corrected; this state persists for the rest of the session. *Scrolled-past and back:* the taken state persists — a fix, once taken, is not un-taken by scrolling (the log does not unwrite; §13). *Jump scroll across:* the fix is applied in its taken state instantly, no sequence owed. *Disabled:* n/a. *Touch:* identical; thresholds are scroll positions, not gestures.

**Content-merge.** Each fix section's prose is the observation itself — the three stars named (at 1200: *Sun (lower limb), Venus, Deneb* — a noon-plus-stars conceit the copy must keep plausible: the record's stated method is a meridian altitude + two intercepts, §6.16), the instrument (sextant), the chronometer time with its +4s error allowed. The animation illustrates a paragraph that fully makes sense without it.

**Breakpoints.** ≥1200px: full-viewport fix sections, sight lines span up to 420px. 768–1199px: sections at 80vh, lines to 260px. <768px: the three sight lines draw from the marker in the vertical channel to points in the entry block's margin; the snap distance is 7px max (§6.3) and reads clearly at that scale; the sequence timing is unchanged.

**Edge cases & failure modes.** Visitor scrolls fast through both fixes: both apply in taken state; a session flag records them so the footer (§6.6) and table (§6.12) show corrected figures. Visitor scrolls up and down across a threshold repeatedly: the sequence plays **once**; after that the taken state is static (a fix that re-performs is a fix that wasn't believed). Content longer than the viewport (a long observation note): the sequence triggers at the section's *fix point* (a marked line in the entry), not at section entry, so long text never desyncs the geometry. If the marker (§6.3) is in fallback mode, the fix still inks its correction line on threshold — the text correction never depends on the geometry.

**Fallback & watchdog.** No-JS: both fixes are printed in their taken state — sight lines drawn, corrections inked, errors stated. The static page tells the whole story. **Watchdog: 2500ms** per fix sequence — any stage not completed by then snaps to the taken state. The correction line's inked figures are in the DOM from first paint (in pencil styling); JS only promotes them, so a dead script leaves correct figures in the wrong colour, never wrong figures.

**Reduced motion.** No hesitation, no line draw, no snap: as the threshold crosses, the section is simply in its taken state (lines printed, correction inked). The reduced page still performs both corrections — it performs them instantly and quietly, as a fair-copy log would.

**Accessibility.** The sequence is decorative over complete text: the correction line reads identically in all states ("DR 41°21.7′N 010°18.3′W; observed 41°23.5′N 010°21.7′W; error 3.1 nm, corrected, J.M."). The taken state is announced once via a visually-hidden live region ("Fix taken at 1200. Error 3.1 nautical miles, corrected.") for screen-reader users following the scroll narrative. Contrast: correction figures `--ink` on `--cream` 12.17:1; sight lines are non-text graphics in `--fix` at 4.88:1 against the paper.

**Performance & mobile variant.** Three path draws + one transform per fix, from the shared loop: ≤0.3ms/frame during the 1.55s sequence, zero thereafter. Mobile: same, shorter lines. No assets.

**Tokens.** `--fix`, `--fix-deep`, `--ink`, `--pencil`, `--ease-snap`, `--ease-plot`, `--ease-ink`, `--fix-1-p: 0.333`, `--fix-2-p: 0.833` (progress points generated from §6.16's fix times), `--sight-dur: 620ms`.

### 6.5 The trembling compass needle

**What & why.** In the chart's top-right corner sits a small brass compass whose needle oscillates ±2° around north with a damped, irregular tremor — and never fully settles. Even the instruments admit the world's wobble. It is the theme's one piece of pure character: it carries no data the visitor needs (the course is printed in the log), and that is its job — it sets the epistemic weather of the page before a single figure is read. It merges with content by placement and restraint: it is an instrument *on the chart*, drawn at instrument scale, behaving the way the real instrument behaves on a moving ship — it is not a logo animation and never performs tricks.

**Structure.** An inline SVG, 88px at desktop: an outer brass ring (2px `--brass`, with a `--brass-lit` top arc — one light source, from above), a cream face with a printed rose (N/E/S/W in log voice, 8 minor points as ticks), and the needle — a two-tone lozenge (north half `--fix`? No: north half `--brass-lit`, south half `--pencil` — red is rationed to fixes, §2, and the needle is not a fix) pivoting on a brass centre dot. The tremor is a seeded pseudo-random walk: every 900ms a new target angle within ±2° is drawn from a seeded sequence (seed fixed per build, so every visitor's needle trembles identically and the motion is testable), and the needle lerps toward it at 0.06/frame via the shared loop; the walk's step size decays after each target (damped) then re-excites — irregular, never periodic, never a smooth sine pulse.

**Motion spec.** Continuous ambient, the theme's licensed loop #1 (§5). Needle rotation range ±2.0° hard bound; typical excursion ±1.2°. Target changes every 700–1100ms (seeded intervals). No other property animates — the ring, face and rose are still. The tremor pauses when the tab is hidden or the compass is off-screen (IntersectionObserver), and stills entirely under reduced motion.

**Choreography timeline.** Page load: needle starts at +1.4° (seeded) and begins its walk at first paint +600ms. There is no sequence — the instrument was already alive when the visitor arrived, and it does not acknowledge them.

**State matrix.** *Rest:* trembling (its rest *is* motion — the exception that defines the rule; see Reduced motion for its true rest). *Hover/focus:* nothing — the compass is not interactive and does not react to the pointer; a compass that notices you is a toy. *Scrolled-past:* it sits in the chart's corner; when the chart's top leaves the viewport it leaves with it (it belongs to the sheet, not the viewport — no sticky clone). *Disabled:* n/a. *Touch:* identical, smaller (§4).

**Content-merge.** The rose's north is the chart's north: the course line's 285° is measured from the same north the needle seeks, and §6.12's table prints courses in degrees from that north. The compass is the chart's reference instrument, drawn once, used by everything.

**Breakpoints.** ≥1200px: 88px, in the chart's top-right margin corner. 768–1199px: 72px, same corner. <768px: 64px, moved into the masthead's right end (§4) — on a narrow sheet the corner belongs to the cartouche's neighbours; the instrument relocates to the table's edge rather than crowding the paper.

**Edge cases & failure modes.** Long sessions: the seeded walk is a 512-step cycle (≈8 minutes) that loops — the loop point is chosen where the walk crosses 0° so the repeat is imperceptible. Low-power devices: if the shared loop's frame budget is exceeded (§14), the needle's target rate halves (targets every ~1800ms) before anything else is cut — the tremor slows; it does not stop being irregular. If SVG fails: a static PNG of the compass at north ships in its place.

**Fallback & watchdog.** No-JS: the needle is printed at north (0°) — a still compass, correct and complete. No watchdog needed: the element has no completion state to strand.

**Reduced motion.** The needle is printed at north and never moves. Under reduced motion the compass tells the truth plainly, which is the theme's own joke, kept respectful: the instrument at rest.

**Accessibility.** `aria-hidden="true"` entirely — it carries no information. The course it references is printed in text (§6.11, §6.12). It is never focusable, never labelled, never announced.

**Performance & mobile variant.** One rotation transform per frame from the shared loop: ≤0.05ms/frame — the cheapest element on the page, and still the first in §14's cut order, because character is spent before content. Mobile: 64px, same walk, halved target rate by default.

**Tokens.** `--brass`, `--brass-lit`, `--pencil`, `--cream`, `--needle-range: 2deg`, `--needle-seed: 214` (the passage number — the walk is the voyage's own), `--compass-size: 88px` (72px / 64px by breakpoint).

### 6.6 The dual position footer

**What & why.** The footer — oak, below the chart — always states the ship's position two ways, side by side: **BY DR** and **BY OBSERVATION**, differing by a small, consistent, stated margin. At the foot of the day's page: DR `41°46.6′N 012°05.6′W`; observed `41°47.8′N 012°07.8′W`; and between them, in log voice: `2.0 NM APART — THE RESIDUAL SINCE THE 1800 FIX`. The disagreement is the brand: managed uncertainty, quantified, never hidden. It merges with content because it is the page's conclusion — every section above has been building these two numbers, and the footer's figures are computed from the same `p` and the same record (§6.16) as the marker (§6.3) that ends its travel a few hundred pixels above, offset by exactly this 2.0 nm drawn at exactly the declared scale. Geometry and print agree because they are the same number twice.

**Structure.** An oak band (`--oak-deep` at the very foot) with three columns at desktop: the DR block (label chip `BY DR`, the position in footer mono 15px, beneath it the method line — `FROM THE 1800 FIX: COURSE 285°, LOG 9.4 KN, 2H 00M`), the margin statement (centred, log voice, with a 48px brass rule above it), and the observation block (chip `BY OBSERVATION` in `--fix`, the position in `--ink`-on-oak — set in `--cream` at full weight, since ink does not read on oak; the method line: `EVENING SIGHTS, THREE STARS, CHRONOMETER ALLOWED`). Below, a hairline and the colophon line (§12's fixed string). Both positions **update as you scroll**: the footer is live — at any moment it prints the position at the visitor's current `p`, DR and observed-side-by-side, where "observed" above the first fix means the departure fix carried forward (labelled honestly: before Fix I the observation column prints the 0800 fix and the words `LAST OBSERVED 0800`).

**Motion spec.** The figures update from the shared loop as `p` changes — as text swaps at 100ms quanta (positions print to 0.1′, and update when the computed value crosses a 0.1′ boundary), never as rolling digits. The margin statement updates at the same quanta (`0.4 NM APART` … growing). At a fix (§6.4), the margin statement flashes its correction once: the two figures snap to agreement for one beat (margin `0.0 NM — CORRECTED`) and then resume disagreeing as the new leg's error grows — the footer re-enacts the day's rhythm in miniature. No other motion.

**Choreography timeline.** Continuous with scroll. Fix crossings: +0ms margin reads 0.0, +180ms (snap) both blocks show the fixed position, then DR resumes its drift on the next scroll quantum.

**State matrix.** *Rest (top of page):* both blocks print the 0800 departure fix, margin `0.0 NM — AT THE DEPARTURE FIX`; the only moment of perfect agreement, honestly labelled as such. *Travelling:* as above; the observation block always names its last-fix time. *At fixes:* the correction beat. *End of page:* the 2000 figures and the 2.0 nm residual, as specified. *Disabled:* n/a. *Touch:* identical figures, stacked layout.

**Content-merge.** The footer is the record's final printing (§6.16 lists its printings: chart, table, footer, form). It also carries the site's ordinary footer duties — the service's links and legal line sit *below* the position blocks in smaller oak-side text, subordinate to the reckoning: on this site, even the footer is a log entry first and a footer second.

**Breakpoints.** ≥1200px: three columns as above. 768–1199px: two columns (DR | observation) with the margin statement as a full-width line beneath. <768px: stacked — DR block, margin line, observation block, each full width; figures at 14px. The order never changes: DR first, observation second, margin between — the argument's syntax is fixed.

**Edge cases & failure modes.** Before any fix (top of page), the observation block's honesty label (`LAST OBSERVED 0800`) prevents the footer from implying a fresher observation than exists. A record with no second fix: the margin statement names the single fix and the residual since it. Extremely long page sessions: the figures are pure functions of `p`; there is no accumulated state to corrupt. If the shared loop dies, the footer prints the 2000 end-of-day figures (the finished day) — the static truth, never a blank.

**Fallback & watchdog.** No-JS: the footer prints the 2000 dual position with the 2.0 nm residual — the completed day's footer, correct as a summary of the page above it. **Watchdog:** the loop's settle/poll rule (§6.3) covers updates; the shipped default is the end state, so failure degrades to the summary, not to an error.

**Reduced motion.** Figures still update with scroll (they are readings, not animation), but the fix-correction beat is a cut, not a flash, and updates quantise to 250ms.

**Accessibility.** Both blocks are real text with their method lines; the margin statement is a `<p>`, not a graphic. A visually-hidden sentence gives the disagreement in words: "The two positions differ by 2.0 nautical miles, the residual error since the 1800 fix." Contrast: `--cream` on `--oak-deep` 14.65:1; the `BY OBSERVATION` chip is `--cream` on `--fix` 4.88:1 at 11.5px bold mono — AA for large/bold text, and the chip is a label whose meaning is duplicated in the method line, never carried by colour alone.

**Performance & mobile variant.** Text writes at most 10×/second, only on change: negligible. Mobile: same text, stacked. No assets.

**Tokens.** `--oak-deep`, `--cream`, `--fix`, `--brass`, `--footer-margin-nm` (computed from §6.16 at `p`), `--pos-format` (the §3 position format), `--ease-drift: 0.12`.

### 6.7 Click-to-fix

**What & why.** Clicking any log entry takes a fix on it: sight lines radiate briefly from the entry's position on the course line, and its figures snap from pencil-grey estimates to inked observed values. The reader performs the navigator's correction — interaction as seamanship. It merges with content because the click does not decorate the entry; it *changes its epistemic state*, permanently for the session: an entry you have fixed stays inked, its `BY DR` chip replaced by `BY OBSERVATION — YOUR FIX`, and the reckoning table (§6.12) updates its row to match. The page keeps a small tally in the margin: `FIXES TAKEN BY THE READER: 2` — the reader's own corrections, logged like the navigator's.

**Structure.** Each log entry (§6.11) is a `<article>` whose figure block is a `<button class="fixable">` (a real button — the whole figure group is the control, min target 48px tall) carrying `aria-pressed` state. On activation: three short sight lines (SVG, from the entry's plot point to three points at the chart's local edge — a star, a headland mark, the compass rose), then the ink promotion of the entry's figures. The "observed" values a click reveals are not invented at click time: they are in the record (§6.16) as each hour's *observed* line — the page's fiction is that the day was sailed and logged twice, once by DR and once by observation, and the click chooses which ledger the entry shows. Values therefore exist in the DOM (visually hidden until fixed, available to the no-JS printing as a second line — see Fallback).

**Motion spec.** Total 700ms: sight lines draw 0–380ms (`--ease-plot`, staggered 70ms), a 120ms held beat (the observation is *taken*), figures cross-fade pencil→ink 450ms `--ease-ink` (overlapping the lines' fade to 40%), chip swaps at +500ms, margin tally increments at +650ms. A fixed entry clicked again does nothing (it is already observed; the button's `aria-pressed` is true and its label says so). Keyboard: the button activates on Enter/Space identically; focus ring is a 2px `--fix` outline offset 3px (red's one interactive use — it marks the fix action, §2's census allows it on this control).

**Choreography timeline.** Click · 0ms lines begin · +70/+140ms lines 2, 3 · +380ms lines complete, hold · +500ms chip swaps, ink promotion mid-way · +650ms tally increments · +700ms settled; the entry is inked for the session.

**State matrix.** *Rest (unfixed):* figures in `--pencil`, chip `BY DR`, button label "Take a fix on the 1400 entry". *Fixing:* as above; the button is disabled during its own 700ms only. *Fixed:* figures `--ink`, chip `BY OBSERVATION — YOUR FIX`, button disabled with label "Fixed by observation". *Scrolled-past:* state persists (session). *Disabled:* fixed entries (by design — a taken fix cannot be un-taken; the log does not unwrite). *Touch:* tap = click; no hover prerequisite; the sight lines still draw (they are the feedback).

**Content-merge.** The tally and the table (§6.12) make the reader's fixes part of the day's record: if the reader fixes the 1400 entry, the table's 1400 row inks too, and its error cell fills with the record's 1400 discrepancy. Play and bookkeeping are the same system.

**Breakpoints.** ≥1200px: sight lines to the chart edge (up to 380px). 768–1199px: lines to the entry block's edge (≤200px). <768px: lines draw within the entry's ruled block only (three short rays above the figures) — the correction is local on a small chart; timing unchanged.

**Edge cases & failure modes.** Rapid clicking across many entries: each runs its own 700ms; the tally increments per completed fix; no queue or lock beyond the entry itself. An entry with no observed line in the record (a data error): the button is not rendered — an entry that cannot be fixed does not pretend it can (the record audit, §10, requires every entry to carry both lines). Session restore mid-page: fixed states are session-scoped and re-derive from the record on load if the session flag exists; otherwise all entries start by DR, which is always a true state.

**Fallback & watchdog.** No-JS: every entry prints **both** lines — the DR figures and, beneath in ink, the observed figures with their discrepancy — because without the click, the honest static form is the full ledger. **Watchdog: 1200ms** — if the ink promotion has not completed (interrupted compositor), the end state applies instantly. The figures' *values* never depend on the animation.

**Reduced motion.** No lines, no fade: the click inks the entry instantly and swaps the chip. The correction still happens; it happens the way a fair copy would record it.

**Accessibility.** A real `<button>` with a state-bearing label; `aria-pressed` reflects fixed state; the result is announced in a visually-hidden live region ("1400 entry fixed by observation. DR error 1.8 nautical miles."). Figures in both states meet contrast: pencil 6.47:1, ink 12.17:1 on cream. Target ≥48px. The sight lines are `aria-hidden`.

**Performance & mobile variant.** Per fix: three short path draws + a colour transition — ≤0.2ms/frame for 700ms, then zero. Mobile: same, shorter lines. No assets.

**Tokens.** `--pencil`, `--ink`, `--fix`, `--ease-ink`, `--ease-plot`, `--fix-dur: 700ms`, `--tally-margin` (the margin tally's position, §6.15).

### 6.8 Divider hover ring

**What & why.** Hovering a chart element — a log entry, a table row, a plotted point — centres a faint range ring on it, as if a pair of dividers had been set down on the chart to measure from that spot: one needle point at the element's centre, the ring showing the dividers' span. Inspection on this chart is done with the chart's own instruments. It merges with content because the ring is not a generic hover glow: its radius is *data* — for a log entry, the ring's radius is that hour's DR error drawn at the chart's cross-track scale, so hovering an entry literally draws the size of its uncertainty around it. Hover the 1800 entry and the ring is the day's widest; hover a fix and the ring collapses to a point — the instrument shows you the error by measuring it.

**Structure.** One reusable SVG overlay per chart region (hero chart, table §6.12): a circle (stroke `--pencil` at 55% opacity, 1px, with a 2px centre dot and a short divider-leg line from centre to the ring at 40°) whose radius and centre are set by the shared loop. The target element declares `data-error-nm`; the ring's target radius = `error × --chart-scale-cross × 8` (the ×8 is the dividers' working magnification, declared in the margin note beside the compass: `DIVIDERS DRAW ERRORS AT 8×, FOR THE EYE` — again, exaggeration stated, never smuggled). Entries with zero error (the fixes, the departure) declare 0 and get the point-only state.

**Motion spec.** On hover/focus entry: the ring scales from the centre dot outward, 260ms `--ease-plot`, to the error radius; the leg draws with it. On exit: 160ms fade to 0 (rings are lifted, not left). Moving between elements: the ring travels (centre lerps at 0.18 — dividers are picked up and set down briskly, the one element allowed a faster lerp than the marker's 0.12) and re-radii in the same motion. No ring appears for elements without a declared error — plain text hovers get the theme's standard link treatment (§11), not an instrument.

**Choreography timeline.** Hover · 0ms dot plants · +60ms leg begins · +260ms ring at full radius · dwell: ring still (dividers do not tremble; that is the needle's job, §6.5) · exit: +160ms gone.

**State matrix.** *Rest:* no ring. *Hover/focus:* ring at the element's error radius. *Active (during §6.7's fix):* the ring is superseded by the sight lines and hides. *Scrolled-past:* rings only exist on the live chart regions; scrolled-away regions' overlays sleep. *Disabled:* elements that are disabled (fixed entries, §6.7) still show their ring on hover — with radius now 0 (the point state), because their error has been corrected: the instrument reports the fix. *Touch:* no hover — a long-press (≥350ms) plants the ring until the next tap elsewhere; a normal tap activates the element itself (§6.7), never the ring first.

**Content-merge.** The ring's radius is the entry's own printed error (§6.11) drawn instead of read — the same number, in the chart's other language. If an entry's printed error and its `data-error-nm` ever disagreed, the figure audit (§10) fails the build.

**Breakpoints.** ≥1200px: as above, radii to 112px max (14px × 8). 768–1199px: magnification 6× (the margin note re-declares it), radii to 84px. <768px: rings are cut — the small chart has no room for dividers; hover/focus instead underlines the entry's error figure in `--fix-deep` (the number itself is highlighted). The margin note on mobile declares the substitution.

**Edge cases & failure modes.** Elements near the chart edge: the ring clips at the sheet edge (dividers overhang the paper in life, too) — clipping is by the sheet's `overflow: hidden`, never by the page. Rapid hover sweeps across many entries: the ring's travel lerp smooths the path; it never multiplies (one ring per region, reused). An element whose error exceeds the cap (a record with a 20 nm blunder): radius caps at 112px and the ring's leg carries a break mark (two short parallel ticks — the cartographer's symbol for "off this scale"), with the true figure still printed in the entry.

**Fallback & watchdog.** No-JS: no rings — and nothing is lost, because every radius is a printed figure first. No watchdog: the ring has no completion state; if its script dies mid-hover, a 1000ms CSS transition-less cleanup (opacity fallback on mouseleave at the DOM level) is unnecessary — the overlay is `pointer-events: none` and a stuck ring is removed by the loop's settle sweep; worst case it fades on the next frame the loop runs.

**Reduced motion.** The ring appears at full radius instantly on hover/focus (no draw, no travel) and disappears instantly. The measurement is still offered; the performance of measuring is not.

**Accessibility.** The ring is `aria-hidden` decoration over printed data; focus triggers it identically to hover so keyboard users get the same emphasis; the focused element's own focus ring (§11) is separate and always visible — the divider ring never replaces the focus indicator. Centre dot and ring at 55% pencil are non-text graphics; the information (the error figure) is text at 6.47:1.

**Performance & mobile variant.** One circle + one line, transform/scale writes only: ≤0.1ms/frame while travelling. Mobile: cut entirely (see Breakpoints) — zero cost.

**Tokens.** `--pencil`, `--fix-deep`, `--chart-scale-cross: 2.26px/nm`, `--divider-mag: 8` (6 at ≤1199px, 0 <768px), `--ring-dur: 260ms`.

### 6.9 Pricked plot points

**What & why.** Each log entry's position along the course line is marked with a tiny pricked point — the pinhole a navigator's dividers leave in a real chart — rendered as a small radial dot ring. As the DR marker (§6.3) passes each point, the prick **darkens** from faint pencil-soft to full pencil, permanently for the session. The chart keeps physical evidence of the voyage: progress leaves marks, like a real chart pricked by dividers. It merges with content because the pricks are the entries' addresses on the line — each prick is anchored to its entry block by a hairline, and the darkening is the chart's own record of where the reading has reached, visible at a glance when the visitor scrolls back up: the travelled part of the chart is visibly *used*, the untravelled part still clean.

**Structure.** One SVG circle per entry (13 for the day's 13 entries, §6.16): outer ring 5px diameter stroke `--pencil-soft`, centre dot 1.5px. Darkening is a two-step state: *passed* — stroke steps to `--pencil` and the centre dot fills; driven by the shared loop comparing the marker's `p` to the prick's `pᵢ` (each prick's progress point is generated from its entry's time in the record). A hairline (0.5px `--pencil-soft`) connects each prick to its entry block's rule. The pricks are part of the chart SVG (§6.15), printed faint in the static state.

**Motion spec.** Darkening is a step, not a fade: at the frame the marker's along-track position crosses the prick, the prick's class flips and its stroke colour changes over 120ms (a graphite-darkening, `--ease-ink`) with a 1px→1.5px dot growth — the prick *takes* the graphite. No stagger, no cascade: pricks darken one by one as they are genuinely passed, which over a day's scroll is a slow, earned rhythm. Scrolling back up does **not** lighten them (the chart keeps the evidence; §13's reverse-pass rule) — but the marker's retreat is still visible against the darkened trail.

**Choreography timeline.** Continuous with §6.3: prick *i* darkens within one frame of the marker crossing `pᵢ`, +120ms to full darkness. At the two fixes, the fix pricks are drawn as small crosses instead of dots from the start (§6.4's points) and darken to `--fix` — the chart's two red marks, part of §2's red census.

**State matrix.** *Rest (unpassed):* faint ring, hollow centre. *Passing:* the 120ms darkening. *Passed:* full pencil, filled centre, permanent for the session. *Scrolled-past:* unchanged — the trail persists. *Disabled:* n/a. *Touch:* identical.

**Content-merge.** A prick is not a bullet point: it sits *on* the course line at its entry's true plotted position (its along-track distance = the entry's log distance from §6.16, at the declared scale), so the spacing of pricks along the line is the spacing of the hours at 9.4 knots — even, because the day was steady. A record with a slowed hour would show its pricks closer together: the chart's punctuation is the data's rhythm.

**Breakpoints.** ≥1200px: 5px pricks on the diagonal line. 768–1199px: 4.5px, scales halved. <768px: pricks sit in the vertical channel (§4) at 5px — on the small chart they double as the entries' timeline markers, and their hairlines shorten to 12px.

**Edge cases & failure modes.** Jump scroll to the footer: all pricks above the landing point darken in one frame (the loop applies the state function, not a replay) — the trail is correct instantly. A record with many entries (a 40-entry day): pricks remain legible to ~48 entries; beyond that the record's page map (§7) splits the day across two charts rather than crowding one line. If the marker is in fallback (static) mode, pricks print in their *passed-by-the-finished-day* state — all darkened — since the static page is the completed day.

**Fallback & watchdog.** No-JS: all pricks printed darkened (the finished chart). No watchdog: darkening is a pure function of `p`, recomputed every frame by the loop; there is no state to strand.

**Reduced motion.** Pricks still darken as passed (it is a state change, not a motion), but instantly, without the 120ms graphite step. Under reduced motion with the marker on the true line (§6.3), pricks darken by scroll position alone.

**Accessibility.** `aria-hidden` — each entry's read/unread state is not information a screen-reader user needs, and the entries themselves are all present and readable regardless. The pricks never carry meaning that is not in the text.

**Performance & mobile variant.** Thirteen class flips across a whole page scroll: effectively zero cost. Mobile: identical.

**Tokens.** `--pencil`, `--pencil-soft`, `--fix`, `--ease-ink`, `--prick-size: 5px`, `--prick-count` (generated from §6.16).

### 6.10 Chart-room masthead & log-index navigation

**What & why.** The masthead is the chartroom's oak beam above the sheet: the service name set as a chart's imprint, and beside it the navigation — which in this theme is a **log index**: the day's hours listed in mono (`0800 · 0900 · … · 2000`), each a link that scrolls to its entry, with the two fix hours marked in `--fix`. Navigation here is not a menu of marketing pages; it is the day's index, because on a reckoning board the primary wayfinding is *when are we?* A secondary plain row (Passages, Method, Pricing, About — the product's real pages, §7) sits beneath in smaller log voice. It merges with content because the index is generated from the record (§6.16): the hours, the fix marks and the links cannot disagree with the entries they point to, and the index's current hour — highlighted as the marker (§6.3) passes it — is the visitor's position stated a second way.

**Structure.** An oak band (`--oak`) spanning the page width: left, the imprint — service name in Cormorant 27px `--cream` with a 1px `--brass` rule beneath (the chart's printed imprint line); right, the compass's mobile home (<768px, §6.5). Below the band, on the chart's taped edge, the log index: a horizontal mono list, hairline-separated, the current hour underlined in `--pencil` (a pencil tick, 2px, offset 4px). The index is a `<nav aria-label="The day's log">` of anchor links; the product-pages row is a second `<nav aria-label="Site">`. The masthead is not sticky — a chart's title does not follow you down the sheet; instead §6.15's margin ruler carries progress. (On <768px the index becomes a horizontally scrollable strip — the one licensed sideways scroll, because a log index is a ruler.)

**Motion spec.** Almost none, by design: the room's furniture does not move. Index hour highlight: the pencil tick slides to the current hour via the shared loop (lerp 0.12) as `p` crosses each hour boundary — a 200ms travel at most. Link hover: colour to `--fix-deep` for fix hours, to `--ink` for others (150ms). The imprint never animates. Page load: the masthead is simply there (the unroll, §6.14, happens to the chart below it, not the beam above).

**Choreography timeline.** Load: static. Scroll: tick travels hour to hour in step with §6.3. Index click: native smooth scroll (~600ms typical) to the entry; on arrival the marker and tick agree (same `p`).

**State matrix.** *Rest:* tick under the current hour; that link carries `aria-current="true"`. *Hover/focus:* as above; focus ring 2px `--brass-lit` on oak (visible against the wood, 6.06:1). *Active:* pressed link shifts 1px down (the stamp press, §11). *Scrolled-past:* the masthead scrolls away with the page — by design; progress duties hand to §6.15. *Disabled:* links never disabled. *Touch:* index strip scrolls horizontally; tap targets are the hour cells, ≥44px wide.

**Content-merge.** The index *is* the table of contents of the day, in the day's own units. A page whose record has no fix (a short hop) shows an index with no red — truthfully.

**Breakpoints.** ≥1200px: full band + two nav rows. 768–1199px: the product-pages row folds into a single `SITE` disclosure (native `<details>`, no JS) at the band's right; the log index stays whole. <768px: imprint shrinks to 22px, compass relocates here (§6.5), index becomes the scrollable strip, product row stays a disclosure.

**Edge cases & failure modes.** A record with 25+ hours (a two-day passage page): the index wraps to two lines at desktop rather than shrinking type below 11px — a log index may take two lines; it may not become illegible. Scroll restoration mid-page: tick and marker initialise at the restored `p` (no travel from 0800 — the chart wakes up where it was left). Missing record (build error): the index renders from the static HTML (all hours are in the initial markup; JS only moves the tick).

**Fallback & watchdog.** No-JS: a list of anchor links; no tick; every entry reachable. **Watchdog:** none — links cannot strand content.

**Reduced motion.** The tick jumps by cut at hour boundaries; index clicks scroll instantly.

**Accessibility.** Two labelled landmarks; `aria-current` on the live hour; all targets ≥44px on touch layouts; contrast: `--cream` on `--oak` 12.82:1 for the imprint and index (index hours in `--cream` at 100%); fix hours in the index are `--fix` *deepened for oak* — on oak the fix hours use `--brass-lit` with a red dot marker (a 6px `--fix` dot before the hour), because `--fix` on `--oak` is 2.2:1 and the theme does not print illegible red for symbolism's sake; the dot + the hour's entry carry the meaning, and the hour's text stays cream.

**Performance & mobile variant.** Static HTML + one sliding tick: negligible. Mobile: the strip is native overflow scroll.

**Tokens.** `--oak`, `--cream`, `--brass`, `--brass-lit`, `--fix`, `--pencil`, `--ease-drift: 0.12`, `--index-hour-w: 44px`.

### 6.11 Log entry sections (the page's cards)

**What & why.** The day's content lives in hourly log entries: ruled blocks set along the course line (§4), each one a complete log line made legible — the hour, the log reading, course and speed, the DR position in pencil, the weather and sea note in Cormorant prose, and the entry's error figure. Entries are this theme's cards, and they merge with content structurally: an entry's *position on the page* is its position on the course (its block hangs from its pricked point, §6.9, at its true along-track place), and its *state* (pencilled or inked) is §6.7's fix state. There is no other card system on the page; anything that looks like a card anywhere in the theme is a log entry wearing the same rules.

**Structure.** `<article class="log-entry">`: a top rule with the hour in log voice (`1200`) and the watch name (`AFTERNOON WATCH`); a figure grid in mono — `LOG 1,241.6` · `COURSE 285°` · `SPEED 9.4 KN` · `DR 41°21.7′N 010°18.3′W` with its `BY DR` chip; one or two sentences of Cormorant prose (the human line of the log: *"Wind WNW, fresh. Sea moderate. A steamer crossed ahead at 1130, eastbound."*); and a bottom line carrying the error figure (`ERROR SINCE LAST FIX: 3.1 NM — CORRECTED AT THIS ENTRY` for fix entries; `ERROR GROWING: 1.8 NM BY DR` for ordinary hours) and, where §6.7 applies, the fix button. Entries alternate above/below the line at desktop (§4); the fix entries (1200, 1800) are enlarged variants (§6.4 owns their behaviour; their block layout is this element's).

**Motion spec.** Entries do not animate in. The one motion an entry owns is being **entered up**: when the marker (§6.3) first reaches an entry's prick, the entry's top-rule hour deepens from `--pencil-soft` to `--pencil` and its hairline to the entry block draws (300ms, `--ease-plot`) — the log line is *written* as the voyage reaches it. Everything in the entry was readable before that moment (see Fallback); the entering-up is the chart acknowledging arrival, not a reveal. Ink promotions are §6.7's. No other entry motion exists: entries never slide, fade, stagger or tilt.

**Choreography timeline.** Marker crosses entry *i*'s `pᵢ` · +0ms hour deepens · +300ms hairline complete · entry is "entered" for the session. Fix entries: §6.4's sequence supersedes this beat.

**State matrix.** *Rest (not yet reached):* fully printed, hour in `--pencil-soft` (3.76:1 — used here for a *label*, see Accessibility for the ruling), figures in pencil with BY DR chip. *Entered:* hour in full pencil, hairline drawn. *Fixed (by §6.4 or §6.7):* figures inked, chip swapped, error line replaced by the correction statement. *Scrolled-past:* entered/fixed states persist. *Disabled:* the fix button's states are §6.7's. *Touch:* identical; entering-up is scroll-driven.

**Content-merge.** An entry is the unit of content, of navigation (§6.10's index), of interaction (§6.7) and of the table (§6.12's rows are these entries tabulated). One object, four printings — the one-record rule (§6.16) made visible as a layout system.

**Breakpoints.** ≥1200px: 5-column blocks alternating above/below the line. 768–1199px: 8-column blocks below the line only. <768px: full-width blocks right of the vertical channel; the figure grid stacks to two columns (LOG/COURSE, then SPEED/DR); prose at 19px. The hour and its figures never shrink below the §3 sizes — the small chart is a *condensed* log, not a miniature one.

**Edge cases & failure modes.** A long prose note (a storm hour, 6+ lines): the block grows downward; the course line's channel (§4) is never invaded — the block pushes subsequent spacing, and the prick's hairline lengthens. The layout tolerates it because entries are spaced by *distance along the line*, and a tall entry simply occupies more vertical room on its side. An entry with no prose (a quiet hour): the block is figures only, shorter — the log has laconic hours and the design does not pad them. Missing weather note in the record: the line is omitted, never filled with boilerplate (anti-filler, §9).

**Fallback & watchdog.** No-JS: all entries printed complete, hours in full pencil, both figure lines shown where §6.7 would toggle (§6.7's fallback). **Watchdog:** none needed — entering-up is a class flip driven by the loop's state function; if the loop dies, entries remain in their printed rest state, fully readable.

**Reduced motion.** Entering-up is instant (hour deepens by cut when reached); everything else is unchanged — entries were never motion-dependent.

**Accessibility.** Each entry is an `<article>` with its hour as an `<h3>` (visually the log-voice hour, announced as "1200 hours"). The hour's rest-state colour (`--pencil-soft`, 3.76:1) is a *heading-sized* label at 14px bold mono — it passes AA for large/bold text, and it deepens to 6.47:1 in the entered state; to keep the rest state honest, the hour also carries its watch name in `--pencil` (6.47:1) beside it, so no information rides on the soft colour alone. Figure contrast: pencil 6.47:1, ink 12.17:1. Reading order is DOM order = chronological order, regardless of the above/below alternation (the alternation is pure visual offset; the DOM never reorders).

**Performance & mobile variant.** Static blocks + one class flip each: zero ongoing cost. Mobile: same blocks, stacked grid.

**Tokens.** `--pencil`, `--pencil-soft`, `--ink`, `--cream`, `--cream-dim` (fix entries' banding), `--ease-plot`, `--entry-w: 5col` (8col / 100% by breakpoint), `--rule-c: --pencil-soft`.

### 6.12 The reckoning table

**What & why.** Mid-page, the day is tabulated: the reckoning table — one row per entry, columns for hour, log reading, course, distance run, DR position, observed position (where a fix exists), and the error — set as a ruled mono table on a `--cream-dim` band, the chart's fair-copy summary. It merges with content because it is not a new dataset: it is §6.11's entries in their fourth printing (§6.16), generated from the same record, and it is *live* in one specific way — when the reader takes a fix (§6.7), that hour's row inks in the table too, and when a fix section (§6.4) is passed, its row is already inked. The table is where the day can be audited at a glance, and auditing is this theme's love language.

**Structure.** A `<table>` (real table semantics — this is genuinely tabular data) with a caption in log voice: `THE DAY'S RECKONING — PASSAGE № 214 — ALL FIGURES FROM THE LOG`. Header row in log voice; body rows in mono 13.5px; fix rows banded `--cream` against the table's `--cream-dim` ground with a `--fix` left tick (2px) — red's census includes exactly these two ticks. The error column prints `—` for hours before the first fix comparison exists… no: it prints the growing error by DR (the record carries it per hour, §6.16), and at fix rows it prints the error struck through with the corrected `0.0` beside it. A totals row closes the table: `RUN 112.8 NM · LOG 1,316.8 · GREATEST ERROR 6.2 NM, CORRECTED`.

**Motion spec.** The table itself does not animate on scroll (a fair copy does not perform). Its only motions are inherited: a row's ink promotion when §6.7 fixes its hour (450ms `--ease-ink`, figures and chip together), and §6.8's divider ring on row hover (the table region's overlay). Row hover also deepens the row's band by one step (150ms) — paper under a hand.

**Choreography timeline.** Reader fixes 1400 at its entry · +450ms the table's 1400 row inks (if the table is off-screen, the state simply waits there, correct when reached). Fix sections passed: rows pre-inked.

**State matrix.** *Rest:* rows in pencil, fix rows pre-banded (their fixes are the day's, already taken by the navigator — the table reflects the *voyage*, so §6.4's rows are inked from the start in the table's printing; §6.7's reader-fixes ink additionally). *Hover/focus:* band deepens; §6.8 ring where applicable. *Scrolled-past:* unchanged. *Disabled:* n/a. *Touch:* no hover; rows are ≥44px tall for §6.7's parity (a row tap on the hour cell scrolls to the entry — the table is also an index).

**Content-merge.** The totals row is the record's arithmetic (§6.16: 12 × 9.4 = 112.8; 1,204.0 + 112.8 = 1,316.8) printed where an auditor looks for it. If a row and its entry ever disagreed, §10's figure audit fails — they are generated from one object, so they cannot.

**Breakpoints.** ≥1200px: full 7-column table. 768–1199px: the observed-position column folds into the DR cell as a second line (positions stack, method labels kept). <768px: the table becomes a list of ruled entry summaries (hour, run, error) with a `FULL TABLE` disclosure (native `<details>`) containing the complete table in a horizontally scrollable well — the data is never deleted for small screens, only re-shelved.

**Edge cases & failure modes.** A 25-row record: the table paginates by watch (§11's pagination — four watches, ruled page turns) rather than growing unboundedly. Rounding: all positions print at the §3 format from the record's stored strings — the table never recomputes a position from lat/long floats at render time (a recomputed figure could round differently from its entry twin; the record stores *strings*, §6.16).

**Fallback & watchdog.** No-JS: the complete table, printed, with the navigator's fixes inked and reader-fix rows in pencil (the reader's fixes are the only JS-dependent state, and their absence is a true statement). No watchdog.

**Reduced motion.** Ink promotions are cuts. Everything else is print.

**Accessibility.** Real `<table>` with `<caption>`, `<th scope="col">` and row headers (`<th scope="row">` = the hour). The struck-through error is paired with visually-hidden text "error 6.2, corrected to 0.0" so the correction is audible, not just visual. Contrast: mono ink on `--cream-dim` 9.99:1; pencil rows on `--cream-dim` ≈5.9:1 (pencil on the dimmer ground, measured for this pairing and gate-checked).

**Performance & mobile variant.** One static table: zero cost. Mobile: the list transformation is CSS + the native disclosure; no JS table library ever.

**Tokens.** `--cream-dim`, `--cream`, `--ink`, `--pencil`, `--fix`, `--ease-ink`, `--table-band: --cream-dim`.

### 6.13 Plot your passage (the conversion form)

**What & why.** The conversion section is a reckoning the visitor works themselves: **Plot your passage** — a form in the form of a log page, where the visitor enters a departure, a course, a speed and hours run, and the page *plots their DR position* on a small chart, prints it **BY DR** in pencil — and then, because this theme never lets an estimate stand alone, prints beside it the honest companion: the error the reckoning cannot rule out, grown from the day's own found set and drift, labelled as the estimate it is. For the Kestrel Passage product this is the demo that sells the service ("Send me this reckoning as a passage plan" — the email field and submit). It merges with content because the form is not a web form wearing a costume: its fields are log lines, its result is a plotted position, and its confirmation is entered into the page's own margin as a new log line, initialled with the visitor's given initials.

**Structure.** A ruled log-page panel (`--cream`, hairline rules) with four fields set as log lines — `DEPARTURE` (two text inputs: latitude, longitude, mono, in the §3 position format, with a `USE THE DAY'S DEPARTURE` text button that fills the record's 0800 fix), `COURSE STEERED` (number, degrees, 000–359), `SPEED BY LOG` (number, knots, one decimal), `HOURS RUN` (number) — plus `INITIALS` (2–3 letters, the log's signature) and, below a double rule, the service field: `EMAIL FOR THE FULL PASSAGE PLAN`. The submit is a log-voice button: `PLOT IT`. The result region is a mini-chart (SVG, 100% × 220px) with the visitor's course line and DR cross, and beside it the two printed figures: their DR position (computed by plane sailing from their inputs, printed in the §3 format) and the *unruled error* line. Submission posts to the service; the computation is client-side and instant, the email capture is the conversion.

**Motion spec.** On submit: the mini-chart's line draws 900ms `--ease-plot` (the pencil plots the visitor's course — the entrance plot, §6.1, at parlour scale), the cross lands, the DR figure prints in pencil; then the error line inks in at +1000ms (the honest second beat — the estimate first, its uncertainty immediately after, never before and never omitted). The margin log line (visitor's entry, initialled) is entered up per §6.11's beat. Invalid fields: no shake, no red — the offending log line's rule deepens to `--fix-deep` and an ink sentence appears beneath it in the log's voice (§12): *"Course is written in degrees, 000 to 359. Amend and re-enter."* The correction is an amendment to the log, not an alarm.

**Choreography timeline.** Submit · 0ms line begins · +900ms cross + DR figure · +1000ms error line inks · +1150ms margin entry lands · confirmation state complete. (The email send proceeds in parallel; its success line — *"Entered. The full plan follows by post — allow one working day, as with any chart correction."* — appears beneath the button when the POST returns, or instantly in the no-JS flow's confirmation page.)

**State matrix.** *Rest:* blank log lines, the day's departure offered as a convenience. *Filling:* fields are plain mono inputs; entered values set in `--ink` (the visitor writes in ink; the *result* is pencil — the distinction is the lesson). *Submitting:* button disabled, label `PLOTTING…` for the computation's 1150ms. *Plotted:* result chart + both figures + margin entry; the form stays editable — amending a field and re-plotting strikes the old DR figure (pencil strike, §6.4's grammar) and plots anew. *Error (validation):* per-field amendment lines as above; focus moves to the first offending field. *Disabled:* submit disabled only during plotting. *Touch:* identical; inputs at 16px mono to prevent zoom, targets ≥48px.

**Content-merge.** The error line is computed from the *page's own record*: `unruled error = hours × the day's found drift (1.0 kn toward 305°, §6.16)` — so a visitor plotting 6 hours is told `±6.0 NM UNRULED — THE DAY'S OWN DRIFT AT YOUR RANGE`, tying their experiment to the voyage above it. The form teaches the product's thesis with the visitor's own numbers.

**Breakpoints.** ≥1200px: form and mini-chart side by side (7/5 columns). 768–1199px: stacked, chart below the fields, 180px tall. <768px: single column; the two position inputs stack (latitude over longitude); chart 160px; the email field and button full width.

**Edge cases & failure modes.** Absurd inputs (speed 400 kn, hours 900): the log refuses in voice — *"The log doubts 400 knots. Amend."* — with sane bounds stated in the amendment (speed 1–40, hours 0.5–96). Longitude wrap and hemisphere handling: the plane-sailing computation handles the antimeridian and prints the correct hemisphere letters; a departure in the southern hemisphere flips the chart's cross labels (S/W) — the mini-chart is a computation, not a picture of the North Atlantic. POST failure: the plotted result *stays* (the reckoning was the visitor's), and the email line amends to *"The post failed. Your reckoning stands above; try the address again."* with the address preserved. No-JS: the form posts to a server endpoint that returns a confirmation page with the same computation done server-side and the same two figures printed — the conversion works without a line of client script.

**Fallback & watchdog.** The form is a real `<form>` with a real action; JS enhances it into the in-page plot. **Watchdog: 2500ms** on the plotting sequence — the figures print regardless; a stuck line-draw snaps complete. Field values are never cleared by any failure.

**Reduced motion.** No line draw: the mini-chart prints complete with its cross; the error line appears with the DR figure (same beat — under reduced motion the two beats merge, and the copy order still puts DR first).

**Accessibility.** Every field has a real `<label>` in log voice; the position inputs carry `aria-describedby` pointing at the format hint (`Degrees and decimal minutes — 41°12.0′N`). Validation amendments are `role="alert"` text linked by `aria-describedby`, never colour-only (the deepened rule is a bonus, not the signal). The result figures are in a live region announced once: "Your dead-reckoning position: [position]. Unruled error: 6.2 nautical miles." Contrast: field text `--ink` on `--cream` 12.17:1; amendment text `--fix-deep` 6.77:1.

**Performance & mobile variant.** The computation is ~40 lines of plane-sailing arithmetic; the mini-chart is one SVG path. Zero libraries. Mobile: same, smaller chart.

**Tokens.** `--cream`, `--ink`, `--pencil`, `--fix-deep`, `--ease-plot`, `--ease-ink`, `--form-rule: --pencil-soft`, `--drift-rate: 1.0kn` (from §6.16), `--plot-mini-dur: 900ms`.

### 6.14 Chart unroll (loader & page transition)

**What & why.** Arriving at the site, the chart **unrolls** on the table: the cream sheet scales open from its top edge — a rolled chart flattening — over 700ms, its bottom corners settling last with a paper's small overshoot of *position*, never of content. Between pages, the same unroll in reverse-short form (400ms) re-lays the sheet. It merges with content because what unrolls is the page itself — the chart the visitor is about to read — not a branded splash laid over it; the masthead and footer (the table) are present from the first frame, and the sheet unrolls *between* them. A skeleton state exists for slow loads: the **unplotted chart** — the sheet present, graticule printed, ruled log lines empty — which is this theme's honest loading face: the paper is here, the plot is coming.

**Structure.** The chart sheet (§6.15) is a container whose unroll is a `clip-path: inset()` animation (top-anchored) plus a 1.5°→0° `rotateX` settle at the sheet's own perspective — compositor properties only. The skeleton is the same sheet with its content regions showing printed-but-blank log rules (hairlines, hour labels present — a log book's empty page is not a grey box) and the graticule at full print. No spinner exists in this theme; waiting is represented by the unworked paper.

**Motion spec.** First load: unroll 700ms `--ease-unroll`, beginning at first paint; the §6.1 plot starts at +200ms *within* the unrolling sheet (the pencil starts on the exposed part — the two motions are choreographed as one gesture, §13 beat 1). Page transitions (same-site navigations, where the router supports them): sheet lifts (reverse, 300ms) and the new sheet unrolls 400ms. Skeleton: if content is not ready by 150ms, the unplotted chart shows; when content arrives it is entered up entry by entry (150ms staggers of the §6.11 hour-deepening — the log being written at speed) — capped: if load exceeds 3000ms, all content prints at once (the fair copy arrives).

**Choreography timeline.** 0ms table (masthead/footer) painted · sheet unroll 0–700ms · plot begins +200ms · plot completes ~2600ms (§6.1) · cartouche follows (§6.2). Skeleton path: +150ms unplotted sheet · content arrival → entries enter up ≤ +1200ms total.

**State matrix.** *Rest (loaded):* sheet flat, content printed. *Unrolling:* as above; content beneath the clip is real DOM (selectable once exposed). *Skeleton:* blank ruled sheet, hour labels printed, a single log-voice line in the margin: `AWAITING THE PLOT`. *Transitioning:* lift/unroll as above. *Disabled:* n/a. *Touch:* identical.

**Content-merge.** The transition is the medium: charts are unrolled, not faded. A fade would be a screen's gesture; the unroll is the table's.

**Breakpoints.** ≥1200px: full unroll with the rotateX settle. 768–1199px: unroll without rotateX (mid-tier GPUs keep the clip only). <768px: the sheet simply prints (no unroll on first load — a small chart is unrolled in the hand, off-screen, before it is read; transitions keep the 300ms lift only). Skeleton identical at all sizes.

**Edge cases & failure modes.** Very fast loads (cache): the unroll still plays its 700ms on first visit per session — it is the arrival ritual, not a loading mask — but it never delays interactivity (the sheet is usable mid-unroll; links under the exposed region work). Repeat in-session navigations: 400ms form. If `clip-path` animation is unsupported, the sheet prints (feature-detected, no broken half-states). Print stylesheet: the sheet prints flat and complete (a chart's final test is paper).

**Fallback & watchdog.** No-JS: no unroll, no skeleton — the sheet and its content, printed. **Watchdog: 1200ms** — any unroll not completed snaps the clip open; the skeleton has its own 3000ms cap (above). Content can never be trapped under a half-unrolled sheet.

**Reduced motion.** No unroll, no lift: sheets print; transitions are cuts. The skeleton still applies (it is a state, not a motion) with entries printing at once.

**Accessibility.** The unroll is visual only; focus is never moved by it; the skeleton's `AWAITING THE PLOT` line is `aria-hidden` and the content region carries `aria-busy` until entered. Nothing is announced about the paper.

**Performance & mobile variant.** Clip-path + transform on one container: compositor-only, ≤0.4ms/frame for 700ms. Mobile: cut to print (above) — zero cost.

**Tokens.** `--cream`, `--oak`, `--ease-unroll`, `--unroll-dur: 700ms`, `--unroll-dur-page: 400ms`, `--skeleton-cap: 3000ms`.

### 6.15 The chart surface & margin ruler

**What & why.** The chart itself, specified as an element: the cream sheet with its printed graticule (latitude/longitude lines in `--pencil-soft`), its compass (§6.5) in the corner, its course line (§6.1/§6.3), and — its own signature furniture — the **margin ruler**: a vertical scale in the sheet's left margin, ruled in miles, that fills with pencil shading as the day runs, its current value printed at the fill's edge (`MILES RUN 074.2`). The ruler is the theme's progress indicator (§5): progress measured in the medium's own unit, in the margin where a navigator would pencil it. It merges with content because the ruler is *part of the chart's print* — it ships in the sheet, reads the same `p` as everything else (§5's one-cause rule), and its final state (112.8 nm, full) is the day's total from the record (§6.16).

**Structure.** The sheet is a `<section>` with a background of layered CSS gradients (the graticule: vertical/horizontal hairlines every 56px at desktop, representing 10′ of latitude at the declared scale — the spacing and its meaning printed in the margin: `GRATICULE 10′`) over `--cream`, plus a faint paper grain (a 3KB repeating PNG at 4% opacity — the only texture asset in the theme). The margin ruler is an SVG-free construct: a 10px-wide, full-height track in the left margin with a fill div (height % from `p × 112.8 / 112.8`), tick marks every 10 nm (CSS repeating gradient), and the miles-run figure as HTML text rotated 0° at the fill's leading edge, in margin mono (§3). The scale declaration (§4) is printed at the ruler's foot: `ALONG-TRACK 9.0 PX/NM · CROSS-TRACK AT QUARTER SCALE, AS CHARTED`.

**Motion spec.** The fill height and figure update from the shared loop (lerp 0.12 via `p`); the figure quantises to 0.1 nm. The graticule has the theme's only parallax: in the hero region the graticule layer drifts at 0.92× the sheet's scroll (±6px total) — the paper settling on the table (§5). Nothing else on the sheet moves except through its tenant elements (§6.1–§6.9).

**Choreography timeline.** Continuous with scroll: fill 0 at the departure, 37.6 at Fix I, 94.0 at Fix II, 112.8 at the foot — agreeing with §6.17's miles-run counter at every point, because both read `p`.

**State matrix.** *Rest (top):* fill 0.0, figure `MILES RUN 000.0`. *Travelling:* as above. *End:* full, `MILES RUN 112.8` — and the figure's final value is the totals row of §6.12, agreeing. *Disabled:* n/a. *Touch:* on <768px the ruler becomes the horizontal strip (§4) with identical behaviour and figure.

**Content-merge.** The ruler's ticks are the entries' distances: each log entry's prick (§6.9) has a corresponding ruler tick labelled with its hour in the margin — the margin is the day's index in distance, as §6.10's is in time.

**Breakpoints.** ≥1200px: vertical ruler in the 64px margin, graticule 56px. 768–1199px: margin 36px, ruler 8px wide, graticule 40px (re-declared `GRATICULE 10′` at the halved scale). <768px: horizontal strip above the cartouche, 8px tall, figure at its right end; graticule 32px, decorative density reduced (every other line dropped — a small chart is a *generalised* chart, and the margin says `GRATICULE 20′` truthfully).

**Edge cases & failure modes.** Records longer than the sheet (a 300 nm day): the ruler's scale re-declares itself (`RULER 300 NM`) and ticks re-space — the figure logic is scale-free because it reads `p` and the record's total. If the loop dies: the ruler prints full with the final figure (the finished day, consistent with §6.6's fallback). Grain asset fails: the sheet is plain cream — the chart loses texture, never content.

**Fallback & watchdog.** No-JS: ruler printed full at 112.8 with the final figure; graticule printed; the sheet complete. **Watchdog:** covered by the loop's poll rule (§6.3); the shipped state is the completed day.

**Reduced motion.** Fill and figure still track scroll (readings, not animation) with the lerp replaced by direct setting and quantisation at 250ms; the graticule parallax is off.

**Accessibility.** The ruler is `aria-hidden` (its figure duplicates §6.17's counter and §6.12's totals in text). The scale declaration is real text, printed twice (here and §6.2's cartouche small print) because it is a claim the page makes about itself. Grain and graticule are background layers, invisible to assistive tech.

**Performance & mobile variant.** One height write per frame from the shared loop: ≤0.05ms/frame. Backgrounds are gradients + one 3KB texture. Mobile: the strip is one width write.

**Tokens.** `--cream`, `--pencil`, `--pencil-soft`, `--ease-drift: 0.12`, `--ruler-total-nm: 112.8` (from §6.16), `--graticule-step: 56px` (40px / 32px by breakpoint), `--chart-scale-x: 9.0px/nm`.

### 6.16 The passage record (the one data object)

**What & why.** Every figure on the page — the marker's offsets, the footer's two positions, the table's totals, the form's error rate — traces to one declared object: the **passage record**, the day's log abstracted. This element specifies it, because in this theme the data model *is* a design element: the record is printed in the page's margin as a fair-copy abstract (the visitor can read the whole day in one ruled block), and it is the single source from which the chart, entries, table, footer and form are generated. If two printings disagree, the bug is a second source — and §10's audit greps for exactly that.

**Structure.** A ruled margin block (in the chart's right margin at ≥1200px; a section after the table at smaller widths) titled `THE PASSAGE RECORD — № 214`, printing the record's fields in log voice, and — in the build — a JSON object of the same fields from which all components render. The record for the worked day:

- **Vessel / service:** MV *Kestrel Wind* — Kestrel Passage, Lisbon → Boston, day 1.
- **Departure fix (by observation), 0800:** `41°12.0′N 009°30.0′W`. Patent log at departure: **1,204.0 nm**.
- **Course steered:** 285°T throughout. **Speed by log:** 9.4 kn throughout (the steady day — a record with varying speed stores it per leg, and §6.9's prick spacing shows it).
- **Hourly entries 0800–2000 (13):** log readings 1,204.0 + 9.4 per hour (0900: 1,213.4 · 1000: 1,222.8 · 1100: 1,232.2 · 1200: 1,241.6 · 1300: 1,251.0 · 1400: 1,260.4 · 1500: 1,269.8 · 1600: 1,279.2 · 1700: 1,288.6 · 1800: 1,298.0 · 1900: 1,307.4 · 2000: 1,316.8); each entry carries a prose line and an observed line (for §6.7).
- **Fix I — 1200, by observation** (meridian altitude + two intercepts; chronometer allowed): DR was `41°21.7′N 010°18.3′W`; observed `41°23.5′N 010°21.7′W`; **error 3.1 nm**, corrected, initialled J.M.
- **Fix II — 1800, by observation** (three bearings on the headland marks): DR (from Fix I) was `41°38.1′N 011°34.5′W`; observed `41°41.7′N 011°41.3′W`; **error 6.2 nm**, corrected, initialled J.M. Set & drift found from Fix II: **set 305°, drift 1.0 kn** (6.2 nm found in the 6 hours since Fix I; the rate carried forward is 1.0 kn — the set is no metronome, and the log says so) — the rate §6.13's form uses.
- **2000, end of page:** by DR (from Fix II, 2h run) `41°46.6′N 012°05.6′W`; by observation (evening sights) `41°47.8′N 012°07.8′W`; **margin 2.0 nm** — 1.0 kn × 2h since the fix, consistent with the found drift.
- **Totals:** distance run **112.8 nm** (12 × 9.4); log at 2000 **1,316.8** (1,204.0 + 112.8). Chronometer: **4s fast on GMT**, allowed for in every time printed.

**Motion spec.** None — the record does not move. Its printings move (§6.3, §6.6, §6.17); it abides.

**Choreography timeline.** None. The record is printed complete at first paint and is the last thing on the page that could ever be called finished.

**State matrix.** *Rest:* printed in full. *All other states:* identical — the record has no states, which is the point of it. *Disabled:* n/a. *Touch:* the block moves below the table (see Breakpoints) but loses no field.

**Content-merge.** The record is not *merged with* the content; it **is** the content, abstracted. Its margin printing is the page's contract with an auditor: everything above can be checked against this block, and §10's gate does exactly that.

**Breakpoints.** ≥1200px: right-margin block, 260px wide, sticky within the chart's middle third (the one sticky element — the abstract travels with the auditor). 768–1199px: a full-width ruled section between the table (§6.12) and the form (§6.13). <768px: same section, fields stacked two per line → one per line for the position fields.

**Edge cases & failure modes.** A record whose legs vary (speed changes, course alterations): the record stores per-leg arrays; the entries, pricks, marker path and totals all generate from them unchanged in structure — the worked day's steadiness is a property of *this* record, not of the theme. A record with one fix or none: `error(p)` (§6.3) degenerates honestly (one snap, or a single growing error and a footer whose observation column is the departure, labelled). A record that fails validation (positions that don't reconcile with course/speed/time within 0.3 nm by plane sailing): the build fails (§10) — the page may not publish a day that doesn't reckon.

**Fallback & watchdog.** No-JS: the record block is the most important no-JS element on the page — it *is* the static summary. No watchdog.

**Reduced motion.** Identical (it never moves).

**Accessibility.** The block is a `<section>` with a heading and a definition-list structure (`<dl>`) so its field/value pairs are navigable; every position in it follows §3's format. Contrast: log voice `--pencil` on `--cream` 6.47:1, values `--ink` 12.17:1.

**Performance & mobile variant.** One static block + one JSON payload (~1.2KB) that the whole page shares. Mobile: same payload.

**Tokens.** `--ink`, `--pencil`, `--cream`, `--record-id: 214`, `--drift-set: 305deg`, `--drift-rate: 1.0kn`, `--chrono-error: +4s`.

### 6.17 Counters that agree to disagree (miles run · error · chronometer)

**What & why.** Three instrument readings live in the chart's margin beneath the compass: **miles run**, **DR error**, and **chronometer time**. They count because the ship moves — scrubbed to scroll via the shared loop — and they embody the theme in miniature: the miles-run counter and §6.15's ruler always agree (same `p`, same record), while the error counter and the footer's margin (§6.6) always agree *with each other* and never with the visitor's hope: the error counts **up** between fixes and snaps to 0.0 at each fix, in plain sight. The chronometer counts the day in GMT with its +4s error *included and labelled* — `CHRONOMETER 14:22:31 (+4S FAST, ALLOWED)` — an instrument that publishes its own correction. It merges with content because these are the log's three vital signs, printed where a navigator glances for them, and every value is derivable from the record (§6.16) at the current `p`.

**Structure.** A margin stack of three ruled readouts, each: label (log voice), value (mono 15px, tabular, fixed-width boxes so digits never shift layout), and a method line (6.47:1 pencil, 11px). Miles run: value to 0.1 nm. Error: value to 0.1 nm, labelled `ERROR BY DR — SINCE 1200 FIX` (the label updates at fixes — the counter names its own epoch). Chronometer: HH:MM:SS ticking in real time from the page's 0800 = visitor's arrival mapped to the day (the day runs at scroll pace for position, but the chronometer ticks at *real* seconds from a stated start — it is the one reading tied to the visitor's clock, and its method line says so: `RUNS WITH YOUR CLOCK FROM 0800`). Wait — that dual allegiance is a confusion; the ruling: the chronometer shows **the log's time at the current `p`** (0800 + 12h × p), ticking forward in real seconds *between* scroll movements at the day's compressed rate of 12h per full page — no. Simplest honest ruling, and the one this spec fixes: the chronometer displays log time as a pure function of `p` (0800 at top, 2000 at foot), updating on scroll quanta like the footer (§6.6); its "+4s fast, allowed" label is the character. It does not free-run. A free-running clock would be a fourth data source, and the theme has one record.

**Motion spec.** Values update from the shared loop at 100ms quanta when `p` changes; digits swap, never roll or flip (a log is written, not spun). The error counter's snap at a fix is instant with the marker's (§6.4's 180ms window: the value holds its pre-fix figure until the snap frame, then reads 0.0). The chronometer's seconds hand equivalent — the seconds digits — change on the same quanta; there is no continuous sweep.

**Choreography timeline.** Continuous with scroll. At Fix I: miles 37.6 · error 3.1 → 0.0 · time 12:00:00. At Fix II: miles 94.0 · error 6.2 → 0.0 · 18:00:00. At foot: 112.8 · 2.0 · 20:00:00 — the three numbers §6.12's totals and §6.6's margin must match, and do, being one function.

**State matrix.** *Rest (top):* 0.0 · 0.0 · 08:00:00 — the day's only all-zero moment, at the departure fix. *Travelling:* as above. *At fixes:* the error snap. *End:* the totals above. *Disabled:* n/a. *Touch:* the stack relocates (§4: margin instruments move to a ruled strip above the footer on <768px) with identical values.

**Content-merge.** The counters are the margin's abstract of the chart's geometry: §6.3's offset in pixels and this error in miles are the same number at the declared scale (14px ÷ 2.26 = 6.2 nm at the maximum) — a visitor with dividers (§6.8) can verify the page against itself.

**Breakpoints.** ≥1200px: margin stack under the compass. 768–1199px: a horizontal ruled strip at the chart's head, three readouts in a row. <768px: the strip moves above the footer (the day's instruments are consulted at day's end on a small chart) — values and labels unchanged.

**Edge cases & failure modes.** Scroll quantisation: below 0.1 nm of travel the values hold — the counters never flicker sub-quantum digits. A record with a mid-day fix added later: the error counter's epoch label is generated from the fix list, so it renames itself truthfully. If the loop dies: counters print the end-of-day values (112.8 · 2.0 · 20:00:00) — the finished day again.

**Fallback & watchdog.** No-JS: the end-of-day values, printed. **Watchdog:** the loop poll (§6.3) covers update death; the shipped defaults are the final values.

**Reduced motion.** Values update on scroll at 250ms quanta, by cut. No other change — readings are not animation.

**Accessibility.** Each readout is text; the trio is grouped in a `<section aria-label="Instruments">` with the values as plain text (not live regions — a screen-reader user scrolling should not be read the log unbidden; the values are there when sought). Tabular figures at 15px, `--ink` on `--cream` 12.17:1; method lines `--pencil` 6.47:1.

**Performance & mobile variant.** Three text writes per quantum, only on change: negligible. Mobile: same writes, relocated strip.

**Tokens.** `--ink`, `--pencil`, `--cream`, `--ease-drift: 0.12`, `--counter-quanta: 100ms`, `--chrono-error: +4s` (from §6.16).

### 6.18 The lost fix (404)

**What & why.** The 404 page is a chart in fog: the sheet prints, the graticule fades toward its edges into unprinted cream, the course line runs a short way and stops — its end unmarked by any cross, because no fix was taken — and the log's line for the hour is written in full: `POSITION REQUESTED NOT IN THIS LOG. BY DR, YOU ARE SOMEWHERE OFF THE CHART.` Beneath it, the two honest ways onward: the log index (§6.10's hours, linking to real entries) and a `TAKE A FIX` button that returns the visitor to the departure — home — labelled as what it is: `RETURN TO THE LAST FIX (HOME)`. It merges with content because it is the theme's epistemology at the exact moment it matters: a missing page is a failed observation, and the theme responds not with a joke graphic but with its own procedure — state the position honestly (unknown), offer the instruments, send them to a known fix.

**Structure.** An oak-deep page (`--oak-deep` surround) with a single cream sheet: graticule at full print in the top-left two-thirds, dissolving (a cream-on-cream gradient mask — fog is the *absence of print*, not a blur filter, §5's refusal) toward the bottom-right; a course line drawn 40% across and stopped; the message block set as a log entry (§6.11's structure: hour line reads `HOUR NOT LOGGED`); the index and the return button (§11's primary). No illustration, no mascot, no compass — in fog, the compass is not shown: the theme does not pretend an instrument it cannot read. (The needle's absence is the detail that makes the page: §6.5's corner is empty.)

**Motion spec.** Almost none: the course line is printed stopped (it does not draw — a line that performs its own loss would be theatre). One licensed motion: on load, the fog edge breathes once — the gradient mask's position shifts 12px over 2400ms `--ease-unroll` and stills — weather passing, barely. The return button's hover is §11's standard. That is all; a lost page should be quiet.

**Choreography timeline.** Load: sheet printed, fog breathes 0–2400ms, stills. Nothing follows. The stillness is the spec.

**State matrix.** *Rest:* as above — its only state. *Hover/focus:* standard control states. *Disabled:* n/a. *Touch:* identical.

**Content-merge.** The 404's index links are the real log index; its message uses the log's grammar (an entry, a position statement, a procedure). A visitor who learns the theme from its 404 has learned it correctly.

**Breakpoints.** ≥1200px: sheet 900px centred, fog to the bottom-right. 768–1199px: sheet full width, fog from the right. <768px: sheet full width, the stopped line runs down the vertical channel (§4) and stops mid-sheet; message block below it.

**Edge cases & failure modes.** A 404 reached with a referrer from inside the site: the log line adds the requested path in mono (`REQUESTED: /passage-215`) — the log records what was asked for, as a log would. Search-engine arrivals: the same page; the index is the sitemap's honest abstract. The fog gradient must never reduce the message block's contrast: the text sits in the fully printed region at all breakpoints (gate-checked, §10).

**Fallback & watchdog.** No-JS: identical (the page is nearly static by design). **Watchdog:** none — nothing can strand.

**Reduced motion.** The fog does not breathe. The page prints, stopped and quiet.

**Accessibility.** The message is an `<h1>` in the log entry's heading position ("Position requested not in this log"), the path in mono text, both at full contrast (`--ink` on `--cream` 12.17:1). The empty compass corner is `aria-hidden` emptiness. Focus lands on the H1 via `tabindex="-1"` on load for screen-reader arrivals — the one page where the theme moves focus, because the visitor is, definitionally, lost.

**Performance & mobile variant.** The lightest page in the theme: one sheet, one gradient, one short path. ≤40KB total. Mobile: same, smaller.

**Tokens.** `--oak-deep`, `--cream`, `--pencil`, `--pencil-soft`, `--ink`, `--ease-unroll`, `--fog-breathe: 2400ms`.

## 7. Page application map

**Home (the day's reckoning — the worked page of this expansion).** The full system: unroll (§6.14), plot (§6.1), cartouche (§6.2), thirteen entries (§6.11) along the line, two fixes (§6.4), the table (§6.12), the record (§6.16), the form (§6.13), the dual footer (§6.6). One day, completely reckoned.

**Listing page (the passage index — many days, many routes).** A chart *drawer*: entries become index rows ruled like the table (§6.12) — one row per passage: route, departure fix, run, greatest error, whether corrected. Each row's error figure is set in pencil if the passage is still at sea (its reckoning open) and ink if the log is closed — the listing's sort order is by departure, never by "accuracy": the theme does not rank voyages by how little they drifted; it records them. Filters are log-voice disclosures (`ROUTE`, `MONTH`, `STATE: AT SEA / LOG CLOSED`). No card grid: a drawer of logs is a list, ruled.

**Detail page (a single passage, another day).** The home system with a different record: the same eighteen elements generated from that passage's §6.16-equivalent. A short coastal hop (3 hours, one fix) shows the system degenerating gracefully — fewer entries, one snap, a footer whose observation column is a landfall bearing. A passage with no fix (an overcast day) is a legitimate detail page: its footer observation column reads `NO OBSERVATION OBTAINED — OVERCAST` and its margin is the full day's drift, stated large. The theme can tell a day when the sky never opened; that may be its best page.

**About / method page (how the reckoning works).** The chart becomes a teaching plate: the course line is a worked example with every instrument labelled by leader lines (dividers, log, chronometer — §6.8's ring grammar at rest), the prose in Cormorant explains plane sailing, set and drift, and the page's own footer still prints a dual position (the method page is also at sea). The form (§6.13) appears here in its teaching variant: pre-filled with the day's figures, inviting the visitor to amend the speed and watch the error grow.

**Pricing / plans page.** Set as a *table of allowances*: what each plan plots, how often it fixes. The theme's honesty is the pricing page's asset — the tiers are distinguished by fix frequency (`BY DR ONLY` / `A FIX EVERY WATCH` / `CONTINUOUS OBSERVATION`), which is a true and legible difference, stated in the theme's own terms rather than feature confetti. Prices are figures, so they are mono (§3 law 1), and each tier's card is a log entry block (§6.11) — ruled, unshadowed.

**Contact page.** A log page addressed to the chartroom: the form grammar of §6.13 (ruled lines, ink writing, amendment-style errors) with fields for name, address and message; the confirmation is an entry in the margin: `LOGGED. WE REPLY BY THE NEXT FIX — WITHIN ONE WORKING DAY.` Contact is correspondence here, and its promise is a fix schedule, not "ASAP".

**Checkout / signup.** The theme routes *payment* out of the chartroom (a chart table is not a till) — the signup's final step hands to the provider's plain page without apology — but the *signup form itself* (account creation: name, email, vessel or fleet) is a log-opening ceremony in §6.13's grammar: to sign up is to **open a log**, and the confirmation prints the account's first entry: `LOG OPENED. DEPARTURE FIX: YOUR FIRST PASSAGE, WHEN YOU PLOT IT.` The conversion the theme owns is the opening of the book, not the taking of the card.

**404.** §6.18 — the lost fix.

## 8. Worked examples

### 8.1 The hero — the 0800 chart (worked example A)

**What the visitor gets.** The table (oak masthead above, §6.10; oak footer far below), and between them the cream sheet unrolling (§6.14). In the sheet's top-right corner the compass (§6.5), already trembling. The course line begins to plot (§6.1) from a departure cross at the sheet's lower-left, running WNW up the sheet — the day's geometry: Lisbon-side water at the bottom, the Western Ocean opening above. As the line completes, the cross lands and its label stands: `0800 — BY DR`. Then the cartouche border draws itself (§6.2) around the standing headline:

> **Twelve hours by dead reckoning.**
> *PASSAGE № 214 · MV KESTREL WIND · LISBON — BOSTON, DAY 1 · ALONG-TRACK 9.0 PX/NM, CROSS-TRACK AT QUARTER SCALE, AS CHARTED*

and beneath the frame, the hero's one prose paragraph in Cormorant: *"No satellites. No signals from shore. A course, a log line, a chronometer — and a position that is an argument, not a fact. This is how Kestrel Passage plans every crossing: estimate honestly, fix when you can, and print the error where everyone can see it."* At the sheet's left margin, the ruler (§6.15) stands at `MILES RUN 000.0`; beneath the compass, the counters (§6.17) read `0.0 · ERROR 0.0 · 08:00:00 (+4S FAST, ALLOWED)`.

**Scroll timeline.** 0ms table painted · sheet unrolls 0–700ms · plot 200–2600ms · cross at 2400ms · cartouche 2720–4120ms · visitor scrolls: the marker (§6.3) leaves the departure cross, the ruler fills, the 0900 entry is entered up. The hero's job is done by the first scroll: the visitor knows the instrument, the day, and the rules.

**Why it works.** Everything the page will do has been shown once, quietly, in the hero: a line plotted, a position labelled by its method, an error at zero *because the day starts at a fix* — the one honest zero. The visitor who reads nothing else has still been told the truth about the product.

### 8.2 Mid-page — the 1200 fix (worked example B)

**The section as built.** The morning entries (0900, 1000, 1100) have been entered up; the marker has drifted 7px off the line (3.1 nm at quarter scale); the 1100 entry's error line reads `ERROR GROWING: 2.6 NM BY DR`. The 1200 section opens with its hour and watch, its prose first — readable before anything moves: *"Forenoon watch ends. Sky cleared at 1140. Meridian altitude of the sun, with Venus and Deneb by intercept — the first fix of the day."* Its figure block stands in pencil: `DR 41°21.7′N 010°18.3′W — BY DR`.

**Scroll timeline.** The visitor scrolls the fix point to the reading line · the marker hesitates (240ms, §6.4) · three sight lines draw to the sun point and two star points (620ms) · the marker snaps 7px to the true line (180ms) · in the figure block, the DR position is struck through in pencil and the observed figure inks beside it: `41°23.5′N 010°21.7′W — BY OBSERVATION` · the error line is entered: `ERROR: 3.1 NM, CORRECTED. J.M.` · a visually-hidden announcement speaks the correction once · the visitor scrolls on; the 1300 entry begins with a clean marker and a growing error, and the margin tally (§6.17) now reads its epoch as `SINCE 1200 FIX`.

**Why it works.** The correction is the product demo: a forecasting tool's whole pitch — *we were 3.1 miles wrong, here is the sighting that proved it, here is the corrected figure, initialled* — performed in 1.55 seconds with the working left on the chart. The prose carried the facts throughout; the geometry made them felt.

### 8.3 Conversion — Plot your passage (worked example C)

**The section as built.** After the table (§6.12) and beside the record (§6.16), the log-page form (§6.13): `PLOT YOUR PASSAGE`. The fields stand blank except the offered convenience: `USE THE DAY'S DEPARTURE` fills `41°12.0′N / 009°30.0′W`. The visitor — our worked visitor — enters course `285`, speed `9.4`, hours `6`, initials `R.A.`, and their email, and presses `PLOT IT`.

**Scroll/submit timeline.** Submit · the mini-chart plots their line (900ms) on the day's own course geometry · their DR cross lands and the figure prints in pencil: `DR 41°26.6′N 010°42.5′W — BY DR` (plane sailing: 6 × 9.4 = 56.4 nm on 285° from the departure — Δlat 14.6′, westing 54.5 nm at mean latitude 41.3° — the arithmetic is the record's method, §6.16) · at +1000ms the honest beat inks in: `UNRULED ERROR AT 6 HOURS: ±6.0 NM — SET 305°, DRIFT 1.0 KN, AS FOUND AT THE 1800 FIX` · the margin gains a new log line: `R.A. PLOTTED A RECKONING — 6H AT 9.4 KN` · the send completes and the line beneath the button amends: `ENTERED. THE FULL PLAN FOLLOWS BY POST — ALLOW ONE WORKING DAY, AS WITH ANY CHART CORRECTION.`

**Why it works.** The visitor's own numbers indict and vindicate the product in one gesture: their position is *useful* (plotted, printed, theirs) and *honestly bounded* (±6.0 nm, derived from the day's real found drift, not a marketing ±). The email is exchanged for a full plan at the exact moment the visitor has felt why a plan needs fixing. That is the conversion this theme exists to make.

## 9. Anti-slop — what makes THIS theme look cheap

Each failure below is specific to Dead Reckoning; each cure is enforceable at the gate (§10).

1. **The marker glued to the line.** Drift faked as zero because a wobbling marker "looked buggy" in review. The theme's entire argument collapses — a DR that cannot drift is a GPS wearing a costume. *Cure:* §6.3's offset function is generated from the record's fix errors; the gate measures the marker's offset at three scroll depths (must be ≈7px before Fix I, ≈14px before Fix II, ≈4.5px at the foot, ±1px).
2. **Footer figures that agree.** A developer "tidies" the dual position into one number, or makes the margin a vague "approximately". *Cure:* the two positions and the stated margin are gate-checked against §6.16 character-for-character (§10.2).
3. **GPS blue and satellite clip-art.** A #2196F3 accent, a location pin, a "live" pulsing dot — one asset from a mapping starter kit and the chartroom is a food-delivery app. *Cure:* the palette is closed (§2); any colour outside the eleven tokens fails the build.
4. **Pirate cosplay.** Treasure-map edges, a skull, "ahoy" in the copy, a script font for "ye olde log". This theme is a *professional instrument*, not a fancy-dress party. *Cure:* §12's voice rules; the copy audit greps a banned list (ahoy, ye, treasure, booty, matey).
5. **A handwriting font for the data.** Setting positions in a script face to feel "hand-logged" destroys legibility and the audit trail — figures must be checkable, so figures are mono (§3 law 1). The hand in this theme is the pencil *line*, never the letterforms. *Cure:* two families only; the font audit (§10) fails a third.
6. **The needle as a toy.** A compass that spins on hover, points at the cursor, or does a flourish on load. Instruments behave; §6.5's needle ignores the visitor entirely and trembles within ±2°, seeded. *Cure:* needle bounds audit (§10) — sample the rotation over 60s; it must never exceed ±2.0° nor sit at a constant angle for >3s (a settled needle is as false as a spinning one).
7. **Red as the error colour.** Form errors, "delayed" badges and warnings sprayed in `--fix` until red means "bad" instead of "corrected". In this theme red is the colour of the day's two best moments. *Cure:* the red census (§10) — licensed surfaces only: two fix sections, two table ticks, the BY OBSERVATION chips, §6.7's focus ring, the two red pricks. Anything else red fails.
8. **Counters that count from zero for theatre.** A miles-run counter that spins up 0 → 112.8 on scroll into view, unconnected to the marker's position. The counters are *readings of `p`* (§6.17), not odometers performing. *Cure:* at any scroll depth, counter value must equal the record's function of `p` within its 0.1 quantum — sampled at five depths at the gate.
9. **Uncertainty in a tooltip.** The error figure tucked behind a hover "ⓘ" so the clean position can shine. The theme's law (§1) forbids it: the error prints beside the position, always, at the same size. *Cure:* DOM audit — every position string must be followed within the same block by its method label and, where applicable, its error.
10. **The plot that replays.** The entrance draw (§6.1) re-running on every scroll to top, every tab refocus, every route change — a party trick repeated until it is noise. *Cure:* once per session, short form on repeat (§6.1); the gate reloads and checks.
11. **Fixes that teleport.** The marker snapping with no sight lines and no hesitation, so the correction reads as a glitch. The 240ms hesitation and 620ms of sight lines are what make the snap read as *seamanship*. *Cure:* §6.4's timeline is gate-timed.
12. **Chart as wallpaper.** The cream-and-graticule look applied as a background behind ordinary SaaS cards with shadows and rounded corners, the course line nowhere, the entries unrelated to the line. Paper does not cast shadows on paper (§4); if the line does not organise the page, it is not this theme. *Cure:* the layout audit — every content block must hang from the line, the table, or the record; an orphan block fails.

## 10. Quality gate

Blocking checks. The theme may not be used in a build until every one passes, signed by a non-builder.

1. **Record validation.** §6.16's record reconciles by plane sailing: every DR position derivable from its departure/fix origin, course, speed and time within 0.2 nm; log readings arithmetic (start + rate × hours); totals equal the sums printed in §6.12. A day that doesn't reckon does not ship.
2. **Two-printings audit.** Every position, error and total that appears more than once (chart, entries, table, record, footer, form) is string-identical in every printing — grep the built page for each §6.16 value.
3. **Method-label audit.** Every position in the DOM carries BY DR or BY OBSERVATION within its block (§9.9); every error figure is printed, none is tooltip-only.
4. **Drift-honesty test.** Marker offset measured at the three depths of §9.1; error counter and footer margin agree with the geometry at five sampled depths (one `p`, one record).
5. **No-JS pass.** JavaScript disabled: the full day reads — plot printed, cartouche framed, both fixes in their taken state, entries with both figure lines, table complete, record complete, footer printing the 2000 dual position, form submittable to its server path.
6. **Watchdog drill.** With animation frames artificially stalled: the plot completes by 4000ms, the cartouche by its 2000ms, each fix by 2500ms, the form plot by 2500ms, the unroll by 1200ms — end states everywhere, no half-drawn anything.
7. **Reduced-motion pass.** `prefers-reduced-motion` emulated: no draw, no unroll, no tremor, no snap — and both fixes still *taken*, the marker still travelling (on the line), counters and footer still live. The reduced page must tell the whole story in print.
8. **Red census.** Count `--fix` surfaces in the rendered page; must equal the licensed list (§9.7) exactly.
9. **Needle bounds audit.** 60s sample per §9.6.
10. **Contrast audit.** The §2 pairings as measured: ink/cream 12.17, pencil/cream 6.47, fix/cream 4.88, cream/oak-deep 14.65, fix-deep/cream 6.77; the two forbidden pairings (§2) absent from the build.
11. **Reader-fix audit.** Every entry carries an observed line in the record (§6.7); fixing each entry in turn inks its table row and increments the margin tally; no entry's button exists without its observed line.
12. **Performance pass.** §14's budget verified on a mid-tier Android over throttled 4G: LCP ≤2.5s, CLS 0.00, shared loop ≤0.6ms/frame average during scroll.

## 11. Component inventory

Every UI component a real site in this theme needs, with its themed treatment. If a component is not listed here, it is built as a log entry (§6.11) wearing the component's semantics — never imported from a generic kit.

| Component | Treatment in this theme |
|---|---|
| Primary button | Log voice, uppercase mono 12px, `--ink` text on `--cream`, 1.5px `--pencil` rule border, 2px radius (paper is nearly square-cornered). Press: 1px downward stamp. The fix action (§6.7) is the only button with a `--fix` border. |
| Secondary button | Same, border `--pencil-soft`, text `--pencil`. Never filled. |
| Text link | Cormorant prose links: `--ink`, underline in `--brass` (brass's rule-work, §2), hover deepens the underline to 2px. Log-voice links: mono, hover to `--fix-deep` only in fix contexts. |
| Text input | A log line: transparent ground, bottom hairline `--pencil-soft`, mono 15px `--ink`; on focus the rule inks to `--pencil` and thickens to 1.5px. The label sits above in log voice, as a log heading. No boxes, no fills — you write *on the line*. |
| Number input | As text input, tabular mono, with the unit printed after the line (`KN`, `°`, `H`) in `--pencil` — units are part of the log's print, not placeholders. |
| Select | A log line with a brass rule-end marker; the native select, styled ground/rule only. Options are log entries in the OS menu — accepted; the theme does not fake a dropdown. |
| Checkbox / radio | A small pencil square/circle that is *ticked by a drawn check* (SVG stroke, 180ms `--ease-plot`) when chosen — the day's self-drawing pencil grammar (§6 theme-wide). Radio = a pricked point (§6.9) that fills. |
| Chip / badge | The method chips are the theme's only badges: `BY DR` (pencil text, pencil hairline) and `BY OBSERVATION` (`--cream` on `--fix`, 4.88:1). No other chip colours exist; a status that is neither estimate nor observation is written as a sentence. |
| Data table | §6.12 — ruled mono on `--cream-dim`, fix rows banded with a red tick. |
| Tabs | **Refused.** A day is one line; you do not tab a log. Multi-day content uses the log index (§6.10) and pagination by watch (below). |
| Accordion | Older days' logs on the listing page (§7): each day a ruled block that opens by *unrolling* its sheet region (§6.14's gesture at 300ms) — the only accordion motion licensed. |
| Modal | **Refused.** Corrections happen in place on the chart (§6.4, §6.7); nothing in a chartroom floats above the chart. A truly blocking decision (deleting a log) is a page, not a dialog. |
| Toast | **Refused.** Nothing pops on a chart. Confirmations are entered in the margin as log lines (§6.13) and stay there — a toast that vanishes is a correction nobody initialled. |
| Alert / notice | The *no-fix notice*: a ruled entry block in the log's voice — `NO OBSERVATION OBTAINED — OVERCAST. POSITION BY DR CARRIED FORWARD.` — ink text, pencil rules, no icon, no colour. Form amendments are §6.13's ink sentences. |
| Pagination | By watch: `FORENOON · AFTERNOON · DOGS · FIRST` as ruled page-turn links (§6.12's long tables, the listing's days) — you turn the log's pages by the watch, not by numbered beads. |
| Progress | The course line + margin ruler (§6.15). No bar, no percentage — a passage is some miles along, and the miles are printed. |
| Skeleton | The unplotted chart (§6.14): graticule and ruled blank log lines, `AWAITING THE PLOT` in the margin. |
| Tooltip | **Refused for data** (§9.9). Permitted only for instrument names on the method page (§7), as plain log-voice text on `--oak`, and never carrying a figure. |
| Breadcrumbs | A reckoning trail: `PASSAGE 214 › DAY 1 › 1200 FIX` in log voice, each step a position in the day — crumbs are fixes here. |
| Avatar / user mark | The navigator's initials in a small pencil circle (`J.M.`) — identity on a log is a signature, not a photograph. |
| Divider | A ruled hairline, `--pencil-soft`; the double rule (two hairlines 3px apart) marks a change of watch or the form's service line (§6.13) — the log's own punctuation. |
| Empty state | A ruled blank entry with the log's line for it: `NOTHING TO LOG. THE WATCH WAS QUIET.` — emptiness is entered, not illustrated. |
| Search | A "consult the index" field in the masthead's site row: results return as log-index lines (hour, place, figure) — you search a log by its entries. |
| Footer | §6.6 — the dual position first, the site's ordinary duties beneath it, subordinate. |

## 12. Copywriting voice

Two registers, never blended within a line.

**The Log** (IBM Plex Mono, uppercase labels, terse declarative figures) — the voice of record. It states what was done, measured or corrected, with the number attached. It never hedges an observation and never inflates an estimate: an estimate is labelled, an observation is plain. *Examples:* `ERROR: 6.2 NM, CORRECTED.` · `SET 305°, DRIFT 1.0 KN, AS FOUND.` · `NO OBSERVATION OBTAINED — OVERCAST.`

**The Chartroom** (Cormorant prose) — the voice of the person keeping the log: measured, dry, quietly proud of the craft. It may be wry about the weather; it is never wry about a figure. *Example:* "The morning's reckoning was, as mornings are, optimistic by three miles. The noon sight said so, and the log does not argue with the sun."

**Rules.**
- **Every estimate is labelled, every error is numbered.** "Approximately", "roughly", "a small error" are banned phrases — the theme's whole courtesy is the number. Write `ERROR GROWING: 1.8 NM BY DR`, never "error growing slightly".
- **Corrections are credited, not confessed.** The voice is `CORRECTED. J.M.` — an initial, a fact. Never "oops", never "we were wrong!!" — being corrected by a fix is the system *working*.
- **Times are four figures, always** (`0800`, `1340`), positions in §3's one format, distances to one decimal with `NM`. A figure in any other format is a typo and fails review.
- **Headlines** (Cormorant) state the day or the idea, spelled numbers only: "Twelve hours by dead reckoning." Never a digit, never a promise of precision the theme cannot keep ("Know exactly where your fleet is" is a banned headline — it is the one thing this theme refuses to say).
- **Buttons** are log imperatives of at most three words: `PLOT IT`, `TAKE A FIX`, `RETURN TO THE LAST FIX`.
- **Error messages** (form amendments) are log sentences with the correction stated: "Course is written in degrees, 000 to 359. Amend and re-enter." — fault, rule, remedy, no apology, no exclamation.
- **Empty states** are log lines: "Nothing to log. The watch was quiet."
- **Fixed strings (verbatim, never paraphrased):** the departure label `0800 — BY DR`; the correction formula `ERROR: [n] NM, CORRECTED.`; the footer labels `BY DR` / `BY OBSERVATION`; the 404's position statement (§6.18); the colophon beneath the footer: `KEPT BY DEAD RECKONING — ESTIMATED, CHECKED, AND CORRECTED IN THE OPEN.`

## 13. Scroll choreography map

The whole day's page, top to footer, in order. (`p` = the shared progress value, §5.)

1. **Arrival.** Table painted (masthead §6.10, footer below the fold). The sheet unrolls (700ms, §6.14); the plot begins inside it (+200ms, §6.1). Counters at zero; needle already trembling (§6.5).
2. **The plot completes** (~2600ms): departure cross, `0800 — BY DR`; the cartouche draws (2720–4120ms, §6.2). The hero stands: headline framed, paragraph readable, ruler at 000.0.
3. **First scroll.** The marker (§6.3) leaves the departure cross; the shadow track begins; the 0900 prick darkens as it is passed; the 0900 entry is entered up (§6.11). The error counter leaves 0.0 — the day's tension begins, quietly, in the margin.
4. **The morning.** 1000, 1100 entered in turn; the offset grows 3.5px → 7px; the ruler passes 18.8, 28.2; the index tick (§6.10) walks the hours. Nothing performs; the chart accumulates.
5. **Fix I (p = 0.333).** Hesitation, sight lines, the 180ms snap, the inked correction, `ERROR: 3.1 NM, CORRECTED. J.M.` (§6.4, §8.2). The error counter reads 0.0 and begins again under a new epoch label.
6. **The afternoon.** Entries 1300–1700; the offset regrows past Fix I's maximum — the visitor who has learned the system now *watches* it grow toward the second fix; the table (§6.12) is passed mid-afternoon, its fix rows inked, its reader-fix rows awaiting §6.7.
7. **Fix II (p = 0.833).** The full sequence at the day's greatest offset (14px): snap, `ERROR: 6.2 NM, CORRECTED.`, and the margin gains the found set and drift — `SET 305°, DRIFT 1.0 KN, AS FOUND` — the day's second harvest.
8. **Evening.** 1900 entered; the record block (§6.16) is read in the margin — the whole day, abstracted, while the marker runs the last miles beside it.
9. **The form (§6.13).** The visitor plots their own reckoning; their error line inks from the day's found drift; their initials enter the margin.
10. **The footer (§6.6).** The marker rests at the terminus, 4.5px off the true cross — visible. Below, the two positions and the stated 2.0 nm between them. The colophon line. The day is closed, not concluded: the two figures still disagree, in print, by a stated amount. That is the ending the theme considers happy.

**Reverse pass.** Scrolling up: the marker retreats along its shadow track, offsets un-grow symmetrically (offset is a function of `p`, §6.3); the ruler and counters run backwards as readings. But **ink does not unwrite**: fixes stay taken (§6.4), entries stay entered (§6.11), pricks stay dark (§6.9), reader fixes stay inked (§6.7). The visitor retreats through a day that remembers being sailed — the chart's state is the integral of the visit, the marker alone is the derivative.

**Jump scroll.** Landing mid-page (restoration, anchor link, find-in-page): everything initialises at the landed `p` in its correct state — fixes above shown taken, entries above entered, marker placed with its true offset, counters and footer reading the landed hour. No beat is owed to a reader who teleported; the log is correct at every depth on arrival.

## 14. Whole-page performance budget

| Budget | Limit | Notes |
|---|---|---|
| Total page weight (home) | ≤ 560KB | Fonts ≤ 96KB (§3 subsets); paper grain 3KB; all chart art is inline SVG (≤14KB total: graticule is CSS gradients, not SVG) |
| Shared loop | One rAF; ≤0.6ms/frame average during scroll on a mid-tier laptop; sleeps when settled | Owns marker, shadow track, ruler, counters, footer, index tick, needle (§5's one-cause rule) |
| Needle tremor | ≤0.05ms/frame | One rotation write; pauses off-screen/hidden |
| Fix sequences | ≤0.3ms/frame during their 1.55s | Three path draws + one transform each |
| Long tasks | None >50ms; the record's render is one pass at build/hydration | Plane-sailing for the form is <1ms |
| LCP | ≤2.5s throttled 4G, mid-tier Android | The hero is DOM + printed chart at first paint; the plot draw never gates content |
| CLS | 0.00 target | All figure boxes fixed-width (tabular mono, reserved boxes, §3); the cartouche frame scales to its text block; no image loads late (there are no raster images above the fold) |

**Cut order when the budget is exceeded** (in this order, never silently): 1) the needle tremor slows (target rate halves, §6.5), 2) graticule parallax (§6.15), 3) the fog breath on the 404 pattern (other pages unaffected), 4) hero plot to its 500ms short form, 5) sight-line staggers collapse (lines draw together, duration kept), 6) the unroll loses its rotateX settle (clip only). **Never cut:** the dual footer, the record block, any figure or method label, the watchdogs, any reduced-motion variant, the no-JS completeness. A chart that must choose between its tremor and its truth keeps its truth.

## 15. Build-order checklist

1. **The record first.** Author §6.16's passage record (positions as stored strings, per §6.12); write the plane-sailing validation (§10.1) and make it pass before any component renders a figure.
2. **Print the chart.** Static HTML/CSS: sheet, graticule, masthead, all entries with both figure lines, both fixes in taken state, table, record, form (server path), dual footer at 2000 values, 404. Verify the no-JS pass (§10.5) — the finished day is the foundation.
3. **Tokens & typography** exactly as §2–§3; run the contrast audit (§10.10) and the font audit (§9.5: two families).
4. **The chart system.** Sheet + margin ruler (§6.15) with its scale declaration; the course path from the record; pricks (§6.9) generated at their true along-track places.
5. **The shared loop** with the 0.12 lerp and the single progress value `p`; register ruler, counters (§6.17), footer (§6.6), index tick (§6.10).
6. **The marker** (§6.3) with `error(p)` generated from the record's fix list; the shadow track; the drift-honesty test (§10.4) wired as a dev check.
7. **Entrance.** Unroll (§6.14), plot (§6.1) with its watchdog, cartouche (§6.2) sequenced after it.
8. **The fixes** (§6.4): thresholds from the record, hesitation, sight lines, snap, inked corrections, live-region announcements.
9. **The needle** (§6.5) with its seeded walk (seed = passage number) and bounds audit (§10.9).
10. **Reader's seamanship.** Click-to-fix (§6.7) with the tally and table sync; divider rings (§6.8) with their stated magnification.
11. **The form** (§6.13) end-to-end: plane sailing, the drift-derived error line, amendment-voice validation, the no-JS server path, the margin entry on success.
12. **Transitions & the lost fix.** Page unrolls (§6.14); the 404 (§6.18) with its empty compass corner.
13. **Reduced-motion variants** for every element; run §10.7.
14. **Mobile transformations**: vertical channel, stacked entries, horizontal ruler strip, relocated compass and counters (§4, per-element Breakpoints).
15. **The gate.** §10 signed by a non-builder — record validation, two-printings audit, drift honesty, red census, watchdog drill — before the theme may be used in a build.

---

*End of Theme 081 — Dead Reckoning (50x expansion). Identity preserved from the original entry: same concept, same five palette anchors, same two type families, all nine original signature elements deepened, and the theme's anti-slop heart kept intact — the footer position is always given two ways, "by DR" and "by observation", and they never quite agree, by a small, consistent, stated margin.*
