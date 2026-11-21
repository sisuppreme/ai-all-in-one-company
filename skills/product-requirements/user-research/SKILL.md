# user-research

## Metadata

- **Owner department:** D1 Product & Requirements (PR)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Nielsen Norman Group, "Personas Make Users Memorable for Product Team Members" — https://www.nngroup.com/articles/persona/ ; Torres, Opportunity Solution Tree — https://www.chameleon.io/blog/opportunity-solution-tree
- **Depends on:** discovery
- **Feeds into:** personas-jtbd, requirements-writing

## When to use / Do NOT use

- **Use when:** evidence about users must be gathered, recorded, or cited — before personas are built, before a segment claim is made, before a requirement claims user backing.
- **Do NOT use when:** the question is what to build next (that is discovery working from this evidence) or how a claim may be published (that is fact-sheet and real-content). Do not run "research" whose only source is the team's own opinion.

## Rules

1. **PR-021 — Findings before interpretations.** The research file writes findings (what was observed) separately from interpretations (what the team concludes). The two are never merged into a single statement.
2. **PR-022 — Every study is fully attributed.** Each study entry records method, participant count, participant source, and dates. An entry missing any of the four is incomplete and cannot be cited.
3. **PR-023 — Real segment only.** Participants come from the actual target segment. Team members, friends, and other builders never count as user evidence.
4. **PR-024 — No claim without a citation.** No persona, segment claim, or "users want X" statement exists without a cited finding ID behind it.
5. **PR-025 — Sample limits are stated.** Every study states who was not reached and what the sample cannot support; the limit is part of the finding.
6. **PR-026 — Context travels with quotes.** Every quote or observation keeps its context (task, moment, segment). A decontextualized quote is not evidence.
7. **PR-027 — Staleness is enforced.** Research past its stated refresh date is marked STALE in the file and cannot justify new commitments until refreshed.
8. **PR-028 — Triangulation for load-bearing claims.** A claim that a persona or requirement depends on is corroborated by a second source type (survey, support tickets, or analytics alongside interviews).
9. **PR-029 — Raw records are kept.** The notes or recordings the method allows are stored with the study, so any finding can be re-checked against its source.
10. **PR-030 — Supplied-material honesty.** When research is built from user-supplied material rather than studies the team ran, the file says so and names the material; anything inferred from it is labeled an inference.

## BAN list

- **BAN-PR-011 — The uncited "users want".** Banned: any "users want / need / prefer X" statement in a research artifact with no finding ID behind it. Defeats: DET-CON-014. Bad: the findings file states "Users want a mobile app" and no study exists. Instead: cite the finding ("F-07: 6 of 9 dispatchers exported reports to phone spreadsheets during the March study") or delete the claim. Severity: BLOCK.
- **BAN-PR-012 — Invented participants.** Banned: participant counts, quotes, or studies that were never run. Defeats: DET-CON-011. Bad: "We interviewed 20 users" when the team read three support tickets. Instead: record what actually happened ("3 support tickets, March export, supplied by the user"). Severity: BLOCK.
- **BAN-PR-013 — Colleague-as-user.** Banned: counting team members, friends, or role-play sessions as research participants. Defeats: DET-CON-011. Bad: "Tested with 8 users" — the 8 were coworkers from the same office. Instead: recruit from the target segment, or label the session an internal review, not research. Severity: BLOCK.
- **BAN-PR-014 — Stale research presented as current.** Banned: citing research past its refresh date as justification for a new commitment without showing the date and the STALE mark. Defeats: DET-CON-018. Bad: a 14-month-old pricing study cited in this quarter's roadmap with no date shown. Instead: show the date and the STALE mark, or refresh the study first. Severity: WARN.

## Gates

- **G-PR-011 — Study-field completeness.** Verifies: PR-022. Check: automated — run a template check over the research file confirming every study entry has non-empty method, participant count/source, and date fields. Pass: 100% of entries complete. Fail: block citation of the incomplete studies. Recorded in: progress.md.
- **G-PR-012 — Persona traceability.** Verifies: PR-024. Check: automated — run a script confirming every persona in the persona file cites at least one finding ID that exists in the research file. Pass: 100% of citations resolve. Fail: block persona sign-off. Recorded in: progress.md.
- **G-PR-013 — Claim citation audit.** Verifies: PR-024, PR-028. Check: manual — sample 5 load-bearing claims in downstream artifacts; each must resolve to a finding, and load-bearing claims to two source types. Pass: 5 of 5 resolve. Fail: warn; a repeat failure blocks handoff. Recorded in: progress.md.
- **G-PR-014 — Staleness sweep.** Verifies: PR-027. Check: automated — compare each study's refresh date against today's date and flag overdue studies STALE in the file. Pass: no overdue study remains unmarked. Fail: warn, and mark before any further citation. Recorded in: progress.md.

## Anti-patterns

- **Findings–interpretation blend.** "Users struggled with the export and clearly need a wizard" — observation and prescription in one breath. Catch it: prescriptions belong in the interpretation section; if a finding contains a feature name, it is blended.
- **Quote mining.** One vivid quote carries an entire segment claim. Catch it: ask for the count behind the quote; if the answer is one participant, the claim shrinks to match.
- **Convenience-sample laundering.** Participants were whoever replied to a forum post, then described in the file as "our users." Catch it: compare the participant source field against the segment definition, word by word.
- **Refresh-date drift.** Refresh dates get quietly extended instead of studies being re-run. Catch it: diff the file history; a changed refresh date with no new study attached is the tell.

## Examples

- [Example 1 — A complete study entry](examples/example-1.md) — corrects PR-022.
- [Example 2 — Separating a finding from its interpretation](examples/example-2.md) — corrects PR-021.
- [Example 3 — A claim that carries its citation and its limits](examples/example-3.md) — corrects PR-024, PR-025.

## Recall anchors

- Findings and interpretations live in separate sections.
- Method, count, source, date — or it did not happen.
- No claim without a finding ID.
- Who was not reached is part of the finding.
- Stale research is marked, never silently reused.

## Checklist

- [ ] Every study entry has method, participant count/source, and dates (G-PR-011).
- [ ] Findings and interpretations are in separate sections (PR-021).
- [ ] No participant comes from outside the target segment (PR-023).
- [ ] Every downstream claim sampled resolves to a finding ID (G-PR-013).
- [ ] Each study states who was not reached (PR-025).
- [ ] No overdue study is unmarked STALE (G-PR-014).
- [ ] Supplied material is named as supplied, with inferences labeled (PR-030).
