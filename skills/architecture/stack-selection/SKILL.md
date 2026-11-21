# stack-selection

## Metadata

- **Owner department:** D2 Architecture & System Design (AR)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** MADR template and guidance — https://adr.github.io/madr/ ; Twelve-Factor config and portability constraints — https://12factor.net/config
- **Depends on:** requirements-writing, system-design
- **Feeds into:** adr-writing, system-design

## When to use / Do NOT use

- **Use when:** choosing or replacing a language, framework, database, queue, or any component the project will depend on for its lifetime; re-evaluating a settled stack decision.
- **Do NOT use when:** the component is already settled by an accepted ADR and nothing material has changed (build on it), or the choice is a leaf utility inside one module with no architectural reach (decide locally, note it in the pull request).

## Rules

1. **AR-041 — Criteria before candidates.** The selection criteria are written down before any candidate is named: requirements fit, data-model fit, team skill, ecosystem maturity and maintenance health, license, operational cost, hosting constraints, exit cost.
2. **AR-042 — Same table for every candidate.** Each candidate is scored against the same criteria in one comparison table. A candidate evaluated on criteria the others were spared is re-evaluated.
3. **AR-043 — Every adoption is an ADR.** No stack component is adopted without an ADR in MADR format whose status is "accepted", naming at least one seriously considered alternative and why it lost.
4. **AR-044 — Popularity is not a criterion.** "Popular", "trending", and "used at a big company" never appear as selection criteria or as a candidate's scored advantage.
5. **AR-045 — Versions agree everywhere.** Versions named in the ADR, the README stack list, and any prose must match the dependency manifest exactly. A mismatch is a defect.
6. **AR-046 — Pin in the same change.** Exact versions are pinned in the dependency manifest in the same change that adopts the component; "install latest" is not a pin.
7. **AR-047 — Disqualifiers are recorded.** A candidate with no maintenance activity, a license conflict with the project's license, or no production hosting path on the target platform is disqualified, and the disqualification is written in the ADR — not silently dropped from the table.
8. **AR-048 — Downsides are accepted on record.** The ADR states the chosen component's accepted downsides (the criteria where it scored worst). An ADR claiming no downsides is incomplete.
9. **AR-049 — Exit cost is assessed.** For data stores and platforms, the ADR states what leaving would cost: data export path, proprietary features in use, and contract or ecosystem lock-in.
10. **AR-050 — Changes supersede, never swap silently.** Replacing a settled component requires a new ADR that supersedes the old one and links both ways. Editing the manifest alone is forbidden.

## BAN list

- **BAN-AR-021 — Fashion adoption.** Banned: adopting a component because it is fashionable, with no criteria table and no ADR. Defeats: DET-CODE-024. Bad: the README announces a stack copied from a conference talk — a database the team has never operated, chosen before anyone listed the project's actual queries. Instead: write the criteria, score at least two candidates in one table, and record the choice as an ADR (AR-041, AR-043). Severity: BLOCK.
- **BAN-AR-022 — Version drift between prose and manifest.** Banned: a version named in the README or ADR that differs from the dependency manifest. Defeats: DET-CODE-028. Bad: the README says "PostgreSQL 16", the ADR says 15, and the deployment manifest pins 14; the team debugs behavior that only exists in one of them. Instead: the manifest is the single source; prose is regenerated or corrected to match it (AR-045). Severity: BLOCK.
- **BAN-AR-023 — The silent swap.** Banned: replacing a settled stack component by editing the manifest, with no superseding ADR. Defeats: DET-CODE-032. Bad: the queue library is swapped over a weekend; the old ADR still says "accepted", and the next incident review reconstructs the rationale from chat logs. Instead: a new ADR supersedes the old one, links both ways, and lands in the same change (AR-050). Severity: BLOCK.
- **BAN-AR-024 — The unmaintained dependency.** Banned: adopting a component with no maintenance activity or an unresolved license conflict without recording the risk. Defeats: DET-INF-025. Bad: a charting library unmaintained for years, with a known unpatched vulnerability, is added because its demo looked good. Instead: disqualify it in the ADR with the reason recorded, or accept the risk explicitly with a mitigation (AR-047). Severity: WARN.

## Gates

- **G-AR-021 — Manifest-to-ADR coverage (citation).** Verifies: AR-043. Check: automated — this requirement is verified by the canonical manifest cross-check, G-AR-122 in adr-writing (every top-level manifest dependency maps to an ADR by name or tag match); run that gate for the full procedure and pass criteria. Recorded in: progress.md.
- **G-AR-022 — Version agreement.** Verifies: AR-045, AR-046. Check: automated — a script extracts version strings from the README stack list and the ADRs and compares them with the manifest's pinned versions. Pass: zero mismatches and zero unpinned top-level dependencies. Fail: block merge. Recorded in: progress.md.
- **G-AR-023 — Criteria predates decision.** Verifies: AR-041, AR-042, AR-048. Check: manual — in git history, confirm the criteria table exists at or before the commit that records the decision, the table scores every candidate on the same criteria, and the ADR names a rejected alternative and accepted downsides. Pass: all three hold. Fail: block stack sign-off. Recorded in: progress.md.

## Anti-patterns

- **Criteria written to fit the winner.** The criteria table appears after the choice and, miraculously, the favorite wins every row. Catch it: compare the table's first commit date with the decision date (G-AR-023); criteria that postdate the choice are advocacy, not evaluation.
- **The phantom alternative.** The ADR names a "considered alternative" that was never seriously evaluated — one line, no scores. Catch it: the alternative must appear in the same comparison table with real scores (AR-042), or the ADR is incomplete.
- **Benchmark theater.** Candidates ranked by a synthetic benchmark that resembles no workload the project has. Catch it: ask which stated criterion the benchmark measures; if it maps to none of AR-041's list, it is decoration.
- **Stack sprawl by accretion.** A second database, queue, or framework added for one feature without an ADR, because "it's just for this." Catch it: run G-AR-021; every top-level dependency without an ADR is sprawl made visible.

## Examples

- [Example 1 — From a fashionable pick to a criteria-based decision](examples/example-1.md) — corrects AR-041, AR-043.
- [Example 2 — Repairing version drift between README, ADR, and manifest](examples/example-2.md) — corrects AR-045.
- [Example 3 — Replacing a settled component with a superseding ADR](examples/example-3.md) — corrects AR-050.

## Recall anchors

- Criteria first, candidates second — always in that order.
- No ADR with a rejected alternative, no adoption.
- Popularity is not a criterion.
- The manifest is the only version that counts.
- A swap without a superseding ADR is a silent swap.

## Checklist

- [ ] Criteria were written before candidates were named (AR-041).
- [ ] Every candidate is scored in one table against the same criteria (AR-042).
- [ ] The ADR is accepted, names a rejected alternative, and states accepted downsides (AR-043, AR-048).
- [ ] Manifest-to-ADR coverage is 100% (G-AR-021).
- [ ] Versions in prose match the manifest exactly; everything is pinned (G-AR-022).
- [ ] Disqualified candidates are recorded with their disqualifier (AR-047).
- [ ] Exit cost is stated for stores and platforms (AR-049).
