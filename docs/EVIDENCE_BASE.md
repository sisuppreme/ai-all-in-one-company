# EVIDENCE_BASE.md — harvested real-world AI issues

Purpose: the X-Crawl evidence base (§3.3) — real-world AI-building issues, each verified, with source + timestamp, indexed by department and detection parameter. Audience: detection squads and departments. Full transcripts never enter the repo (copyright + bloat, §3.3); this file carries issue summaries with sources.

## Method and constraints (recorded honestly, QB-07)

- Source rules (§3.3): English-language videos, published within 24 months, ≥10k views or from a named conference; D14 reviews the source list before harvesting; volume target ≥200 transcripts and ≥50 verified issues per department, recorded in METRICS.md.
- Environment constraint found 2026-11-21: this executor's network has repeatedly failed YouTube media/subtitle downloads (HTTP 403 on yt-dlp attempts, 2026-11-20) and geo-blocks some sources. Per the §3.3 rate-limit/block rule — a blocked source is dropped and logged, not worked around — the transcript harvest proceeds only through routes that work (official captions access and web-readable sources), and the shortfall against the 200-transcript target is reported in METRICS.md rather than padded with unverifiable entries.
- Until the harvest grows, the seed evidence below comes from sources already in hand and verifiable: the Web Craft Pro Max research paper (711 lines, 9 sections, references section) and this build's own verified findings.

## Seed entries (from the handoff package itself)

| # | Issue | Evidence | Maps to |
|---|---|---|---|
| E-001 | AI-generated websites are detectable by systematic surface tells (layout, type/colour, copy, motion, components, code/meta clusters) — the "AI look" is a measurable parameter surface, not a vibe | Web Craft Pro Max research: 178 parameters / 17 families / 221 tells (corrected figures; paper in handoff still prints 170/16/213) | X-Visual, X-Code, X-Content, X-UX → D3 primarily |
| E-002 | Humans detect AI sites at only ~55.5% accuracy while detector vendor claims run 15–30 points above independent benchmarks — calibration fact, to be re-verified by X-Visual in Phase 1 (§2) | Web Craft Pro Max RESEARCH_PAPER.md (handoff copy), §2 of the brief flags it for re-verification | X-Visual; Verification & Sources |
| E-003 | A 4,015-line single-file skill is not safely consumable: long files get forgotten/truncated by agents — memory-proof structure (small self-contained sections, recall anchors, checklists) is a requirement, not a style | Web Craft Pro Max design (§2 inheritance) + brief §5.4 length cap (≤400 lines per SKILL.md) | Forge; all departments |
| E-004 | Brief-vs-reality drift happens even in audited documents: the v5.1 brief's §2 summary describes WCPM rule IDs in a scheme the actual file does not use (`R-<section>-<n>` in the file) — inherited claims must be script-verified against the artifact, never trusted from summaries | This build's kickoff verification, 2026-11-21 (KICKOFF_NOTES.md) | Verification & Sources; D3 integration (Phase 2) |

## Harvest log

| Date | Source batch | Transcripts | Verified issues | Notes |
|---|---|---|---|---|
| 2026-11-21 | Handoff package (WCPM paper + brief) | n/a (documents, not transcripts) | 4 seed entries | Transcript harvest pending working routes; see constraints above |
