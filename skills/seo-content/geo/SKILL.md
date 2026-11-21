# geo

## Metadata

- **Owner department:** D9 SEO & Content (CO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://arxiv.org/abs/2311.09735 ; https://developers.google.com/search/docs/appearance/ai-features ; https://www.kevinleary.net/blog/llms-txt-myth/
- **Depends on:** technical-seo, on-page-seo, aeo, real-content, fact-sheet
- **Feeds into:** web-analytics, content-strategy

## When to use / Do NOT use

- **Use when:** planning, executing, or reporting work aimed at inclusion and citation inside synthesized answers (ChatGPT, Perplexity, Copilot, Google AI Overviews / AI Mode) — building citable content, aligning brand facts across sources, or measuring citation presence over time.
- **Do NOT use when:** the target is a ranked position, featured snippet, or AI Overview eligibility on Google Search itself (use aeo and technical-seo), when the deliverable is ordinary page copy (use copywriting), or when a claim's evidence is in dispute — resolve it under real-content first.

## Rules

1. **CO-061 — Every GEO claim carries an evidence tag.** Each tactic or claim in a GEO plan or report is labeled documented (platform-stated), peer-reviewed, correlational (vendor/observational), or hype (contradicted or unsupported); an untagged claim fails review.
2. **CO-062 — Documented layer first.** Before any GEO tactic is planned, the site meets Google's stated AI-features fundamentals: indexed and snippet-eligible, crawling allowed including at CDN/hosting level, important content in textual form and findable through internal links, structured data matching visible text.
3. **CO-063 — No special files, markup, or scores are requirements.** No plan presents llms.txt, a special schema type, a machine-readable AI file, or a paid "GEO score" as a platform requirement or platform metric — Google states none exist.
4. **CO-064 — llms.txt is hygiene, never a result.** llms.txt may be shipped as harmless hygiene; it is never reported as an AI-visibility win, because Google has stated on the record that it does not use the file and large-scale correlational evidence agrees.
5. **CO-065 — Citable content carries provenance.** Content built to be cited uses original data, named sources, direct quotations, and statistics with their source stated on the page — the methods the peer-reviewed GEO study measured; keyword stuffing is not a GEO method.
6. **CO-066 — Citability never overrides real content.** Every statistic, quotation, or credential added for citability passes real-content first: it traces to fact-sheet.md or a producible source record, or it is cut. An invented figure is a blocker even if an engine cites it.
7. **CO-067 — Brand facts are identical everywhere.** Name, offer, prices, and locations are word-for-word consistent across the site and major third-party profiles (business listings, directories, review platforms); engines synthesize across sources, so an off-site contradiction is treated as a site contradiction.
8. **CO-068 — One canonical statement per fact.** Each brand fact an engine might quote is stated once, canonically, on an owned page, and other pages link to or reuse that statement rather than re-typing a variant.
9. **CO-069 — Citation measurement uses a fixed prompt panel.** Measurement runs a fixed, written set of prompts per engine on a set cadence, with engine, model/version where shown, date, and cited sources logged per run; the panel changes only by a recorded decision.
10. **CO-070 — A single answer is an anecdote.** No report, dashboard, or client update presents one screenshot or one run as a citation result; reports show the panel, the number of runs, and the variance across runs.
11. **CO-071 — No guaranteed outcomes.** No plan, proposal, or report promises AI citation, inclusion, or a visibility percentage; peer-reviewed effects are quoted only with their limits (study's models, method, and "up to" bound), never as an expected average.
12. **CO-072 — Structured data matches visible text.** Any structured data on a page targeted for citation describes only what the page visibly shows, with identical values; markup describing absent content is removed, not "optimized".

## BAN list

- **BAN-CO-031 — AI citation guarantee.** Banned: promising or implying guaranteed citation, inclusion, or a fixed visibility lift in AI answers. Defeats: DET-CON-026. Bad: proposal states "Our GEO package guarantees your brand appears in ChatGPT answers within 60 days." Instead: state the work and the measurement method, with each expected effect tagged by evidence level (CO-061, CO-071). Severity: BLOCK.
- **BAN-CO-032 — llms.txt reported as a visibility win.** Banned: listing llms.txt (or any special AI file/markup) in a results report as an AI-visibility achievement or requirement met. Defeats: DET-NONE — no DET parameter names this signal; governed by CO-064. Bad: monthly report claims "AI readiness improved: llms.txt deployed, AI crawlers can now read the site." Instead: record llms.txt as hygiene in the change log only; report citation results from the prompt panel (CO-064, CO-069). Severity: BLOCK.
- **BAN-CO-033 — Invented statistic added for citability.** Banned: adding a statistic, quotation, or study result to content to make it more citable without a producible source behind it. Defeats: DET-CON-011. Bad: a guide gains the line "Teams using checklists ship 43% faster (industry study)" with no study named or held. Instead: cite a named source on the page or use the project's own measured data from fact-sheet.md — otherwise cut the figure (CO-066). Severity: BLOCK.
- **BAN-CO-034 — Vendor metric presented as a platform fact.** Banned: presenting a vendor's GEO score, correlation study, or lift figure as a search/AI platform's stated ranking or citation factor. Defeats: DET-CON-011. Bad: plan states "Brand mentions are a confirmed AI ranking factor, so we will buy mention placements." Instead: label the study correlational, name its source, and treat it as a hypothesis the prompt panel can test (CO-061). Severity: WARN.
- **BAN-CO-035 — Single-screenshot citation report.** Banned: reporting citation success or failure from one answer, one run, or one screenshot. Defeats: DET-CON-015. Bad: a slide shows one ChatGPT answer citing the brand, captioned "GEO is working — cited by ChatGPT." Instead: report the fixed prompt panel over repeated dated runs, including runs where the brand is absent (CO-069, CO-070). Severity: BLOCK.

## Gates

- **G-CO-031 — Evidence-tag audit.** Verifies: CO-061, CO-071. Check: manual checklist over the GEO plan/report — every tactic and claim carries one of the four evidence tags, and every peer-reviewed figure is quoted with its limits. Pass: 100% tagged, no guarantees anywhere in the document. Fail: return the plan for tagging before any work starts. Recorded in: progress.md.
- **G-CO-032 — Citation-claim provenance scan.** Verifies: CO-065, CO-066. Check: automated assist plus manual verdict — extract every statistic and attributed quotation from pages in the GEO set (`grep -rEo '[0-9]+(\.[0-9]+)?%' pages/ | sort -u`) and trace each to fact-sheet.md or a named on-page source. Pass: every figure traces; zero untraced figures. Fail: block shipment of the page. Recorded in: progress.md.
- **G-CO-033 — Brand-fact consistency diff.** Verifies: CO-067, CO-068. Check: build the fact table (name, offer, prices, locations) from the site and each major third-party profile; diff every value against fact-sheet.md. Pass: zero conflicting values across all surfaces. Fail: correct the wrong surface before the measurement cycle starts. Recorded in: progress.md.
- **G-CO-034 — Prompt-panel run log.** Verifies: CO-069, CO-070. Check: the citation tracker contains the fixed prompt set, one row per run with date, engine, and cited sources, and at least the scheduled number of runs for the period. Pass: log complete; reports cite panel aggregates only. Fail: mark the period's GEO results "insufficient data" — never substitute a single run. Recorded in: progress.md.

## Anti-patterns

- **Panel drift.** Prompts are quietly swapped after bad runs so the trend line improves; catch it by diffing the current panel against the version recorded when the cycle started.
- **Engine cherry-picking.** Results are reported only for the engine that cited the brand this month; catch it by requiring every report to show all engines in the panel, including zero-citation ones.
- **Citation bait clutter.** Pages accumulate tacked-on stat blocks and quote boxes that serve engines but confuse readers; catch it in editorial review — if a passage would be cut for a human reader, its citation value does not save it.
- **Fact fork.** A directory or profile keeps an old price or address because "engines read that one anyway"; catch it in the G-CO-033 diff — every surface is corrected, not just the website.

## Examples

- [Example 1 — GEO plan claims tagged by evidence level](examples/example-1.md) — violates/corrects CO-061, CO-071.
- [Example 2 — Statistic made citable with provenance, not invention](examples/example-2.md) — violates/corrects CO-065, CO-066.
- [Example 3 — Citation report rebuilt from a fixed prompt panel](examples/example-3.md) — violates/corrects CO-069, CO-070.

## Recall anchors

- No GEO claim without its evidence tag.
- Documented layer first: ordinary eligibility, accurate facts everywhere.
- llms.txt is hygiene — never report it as a result.
- Citable means sourced: an invented statistic is a blocker, cited or not.
- A single screenshot is an anecdote; the panel is the report.

## Checklist

- [ ] Every tactic and claim in the plan carries an evidence-level tag (CO-061, G-CO-031).
- [ ] Documented fundamentals verified: indexed, snippet-eligible, crawlable at CDN/hosting level, textual content, internal links (CO-062).
- [ ] No file, markup, or vendor score is presented as a platform requirement or metric (CO-063).
- [ ] Every statistic and quotation in GEO-targeted pages traces to fact-sheet.md or a named source (CO-066, G-CO-032).
- [ ] Brand facts diffed identical across the site and major third-party profiles (CO-067, G-CO-033).
- [ ] Citation results come from the fixed prompt panel over repeated dated runs — no single-run claims (CO-069, CO-070, G-CO-034).
- [ ] No guarantee of citation, inclusion, or visibility percentage appears anywhere in the deliverable (CO-071).
