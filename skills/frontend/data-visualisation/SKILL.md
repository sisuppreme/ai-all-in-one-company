# data-visualisation

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Datawrapper, A friendly guide to choosing a chart type — https://www.datawrapper.de/blog/chart-types-guide ; inherited Web Craft Pro Max §6.7 data-visualization rules, cure CD-17, parameter DAT-07, and BAN-099/BAN-120, mapped in docs/WCPM_MAPPING.md
- **Depends on:** frontend-core, design-tokens
- **Feeds into:** component-library, ui-states

## When to use / Do NOT use

- **Use when:** any chart, graph, stat band, or data graphic is being designed or rendered — dashboards, reports, marketing pages, admin panels.
- **Do NOT use when:** the data itself is being collected or computed (D5/D12 own data and metrics definitions), or the "chart" is a single number with no comparison — that is copy, and frontend-core plus the fact-sheet rules govern it.

## Rules

1. **FE-261 — Message first, chart second.** Before choosing a library or chart type, write the one-sentence statement the chart must make (change over time, comparison, share, correlation, flow, geography). If the sentence cannot be stated, the chart is decoration and is removed.
2. **FE-262 — Type matches the message.** Lines for change over time, bars for comparison across categories, scatter for correlation, stacked bars for part-to-whole, histograms for distribution (inherited §6.7). A type chosen because it "looks good" fails this rule.
3. **FE-263 — Bar axes start at zero.** A truncated bar axis is a defect unless the truncation is explicitly justified in the project notes and flagged on the chart itself.
4. **FE-264 — No 3D charts, no overloaded pies, no implied correlation.** No 3D chart effects; no pie with more than 5 slices (use a stacked bar or bar chart instead); no dual axes implying a correlation without a stated basis.
5. **FE-265 — Color encodes meaning, and never alone.** One accent color carries the story, gray carries context. Series colors are checked for colorblind distinguishability, rainbow palettes are forbidden, and meaning is never carried by color alone — series are labeled or patterned as well (inherited §6.7).
6. **FE-266 — Every chart is labeled and sourced.** Axis labels, units, and the data source with its date appear on or directly under every chart (inherited cure CD-17; parameter DAT-07). An unsourced chart is treated like an unsourced statistic and escalates per DET-VIS-035.
7. **FE-267 — The title states the conclusion.** A chart's title says what the data shows ("Signups doubled after the March launch"), not what it contains ("Signups"). Series are labeled directly where possible instead of forcing legend lookups.
8. **FE-268 — Every chart ships an accessible alternative.** Each chart is accompanied by its data table or a text summary (visually hidden is acceptable) describing the series and the takeaway, reachable via `aria-describedby` or adjacent markup.
9. **FE-269 — Real data only.** Charts render real, possible values that add up. Demo or sample data is plausible, specific, and uneven — and clearly marked as sample wherever it appears (inherited BAN-099).
10. **FE-270 — Uncertainty is shown, not hidden.** Where the underlying data carries ranges, estimates, or partial coverage, the chart shows it (range bands, "estimated" markers, a coverage note) instead of drawing a single confident line.

## BAN list

- **BAN-FE-131 — The unsourced or impossible chart.** Banned: a chart with no source line, no axis labels, or values that cannot be true (shares summing past 100%, counts below zero). Defeats: DET-VIS-035. Bad: a dashboard area chart of "revenue growth" with no axes, no source, and a curve that only rises (inherited BAN-120). Instead: labeled axes, units, source with date, and real values (FE-266, FE-269). Severity: BLOCK.
- **BAN-FE-132 — The truncated bar axis.** Banned: a bar chart whose value axis starts above zero to exaggerate a small difference. Defeats: DET-VIS-035. Bad: bars for 41% vs 44% drawn from a 40% baseline, making one look triple the other. Instead: start the axis at zero (FE-263); if scale genuinely hides the story, switch to a dot plot and say why. Severity: BLOCK.
- **BAN-FE-133 — Decoration wearing a chart's clothes.** Banned: 3D bars, exploded pies, and gradient-filled shapes whose form distorts or hides the values. Defeats: DET-VIS-028. Bad: a 3D pie with nine slices, three of them pulled out, as the "market share" visual. Instead: a flat stacked bar or bar chart with direct labels (FE-262, FE-264). Severity: BLOCK.
- **BAN-FE-134 — Rainbow, color-only encoding.** Banned: a rainbow or random multi-hue palette where hue is the only thing distinguishing series. Defeats: DET-VIS-022. Bad: twelve categories in twelve unrelated colors; in grayscale or to a colorblind reader, the chart is unreadable. Instead: one accent plus gray context, direct labels, colorblind-checked pairs (FE-265). Severity: WARN.

## Gates

- **G-FE-131 — Accessible-alternative DOM check.** Verifies: FE-268. Check: automated — script/DOM query over the built pages: every chart root (`canvas`, `svg` with a chart role) must have an accompanying data table in the DOM or an `aria-describedby` target containing a text summary. Pass: 0 chart roots without an alternative. Fail: block shipment. Recorded in: progress.md.
- **G-FE-132 — Message test.** Verifies: FE-261, FE-262, FE-267. Check: manual — for each chart, state its one-sentence message from the title alone, then confirm the chart type is the family that answers that message per FE-262. Pass: every chart's type matches its stated message. Fail: warn, rework before release. Recorded in: progress.md.
- **G-FE-133 — Axis, label, and source inspection.** Verifies: FE-263, FE-266, FE-269. Check: manual — inspect each rendered chart: bar axes start at zero (or carry the on-chart truncation flag), axes and units are labeled, the source and date are present, and values are possible and sum correctly. Pass: all charts pass all four checks. Fail: block shipment. Recorded in: progress.md.
- **G-FE-134 — Colorblind simulation pass.** Verifies: FE-265. Check: manual with tooling — view each chart through a colorblind simulator (browser DevTools vision-deficiency emulation) and in grayscale; every series must remain distinguishable by label, position, or pattern. Pass: no series becomes ambiguous. Fail: warn, fix before release. Recorded in: progress.md.

## Anti-patterns

- **The smooth-curve demo.** Sample data where every metric rises in a clean curve and every total is round. Catch it: real data is uneven; if the chart looks like a screensaver, FE-269's marked-sample rule was skipped.
- **The legend scavenger hunt.** Six series identified only by a legend in a corner, forcing constant eye travel. Catch it: if a reader must look away from a line to learn its name, direct labeling (FE-267) was skipped.
- **The dashboard wall.** Ten charts on one screen, none with a stated message, because the template had ten slots. Catch it: ask each chart for its one sentence (FE-261); the ones without answers are removed, not shrunk.
- **Precision theater.** Percentages to two decimals from a sample of nine responses. Catch it: compare displayed precision against the dataset size in the source line; precision the data cannot support is cut.

## Examples

- [Example 1 — Nine-slice pie replaced by a labeled bar chart](examples/example-1.md) — corrects FE-262 and FE-264.
- [Example 2 — Truncated, unsourced bars replaced by a zero-based sourced chart](examples/example-2.md) — corrects FE-263 and FE-266.
- [Example 3 — Canvas-only chart given a data-table alternative](examples/example-3.md) — corrects FE-268.

## Recall anchors

- No message, no chart.
- Bars start at zero; pies stop at five slices.
- Every chart: labels, units, source, date.
- Color means something — and is never the only signal.
- If it can't be read as a table, it isn't accessible.

## Checklist

- [ ] Each chart's one-sentence message is written down and its type matches it (FE-261, FE-262).
- [ ] Bar axes start at zero or carry the on-chart truncation flag (FE-263).
- [ ] No 3D charts, no pies over 5 slices, no unstated dual axes (FE-264).
- [ ] DOM check passes: every chart has a table or text alternative (G-FE-131).
- [ ] Axis/source inspection passes on every chart (G-FE-133).
- [ ] Colorblind and grayscale pass done; series labeled directly (G-FE-134, FE-265).
- [ ] Sample data, where used, is marked as sample (FE-269).
