# decision-logs

## Metadata

- **Owner department:** D10 Project & Memory (PM)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Nygard, "Documenting Architecture Decisions" — https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions ; MADR 4.0.0 — https://adr.github.io/madr/ ; adr-tools — https://github.com/npryce/adr-tools
- **Depends on:** project-templates (emits `docs/adr/` and DECISIONS.md)
- **Feeds into:** progress-tracking, handover, memory-retrieval

## When to use / Do NOT use

- **Use when:** a project makes a significant, hard-to-reverse decision — stack, vendor, data model, protocol, a mandated-set change — or reverses one already recorded.
- **Do NOT use when:** the choice is trivially reversible or purely local (naming, formatting) — those belong in the work log or a commit message, not an ADR. Do not use DECISIONS.md as a second copy of the records; it is their index (PM-109).

## Rules

1. **PM-101 — One decision, one numbered file.** Each significant decision gets exactly one file in `docs/adr/`, named `NNNN-short-title.md`. Numbers are sequential and never reused; a withdrawn number stays withdrawn and is noted in DECISIONS.md.
2. **PM-102 — Written at decision time.** The record is created in the same change as the decision itself, while the context and the decider are known — never reconstructed later from chat or memory.
3. **PM-103 — Fixed structure.** Default to Nygard's five sections: Title, Status, Context, Decision, Consequences. Escalate to MADR when the decision is contested, adding decision drivers, considered options with pros and cons, and a Confirmation section.
4. **PM-104 — Context is neutral fact.** Context states the forces, constraints, and evidence at play, without advocacy. Persuasion belongs in the options analysis and the Decision, never in Context.
5. **PM-105 — Decision in active voice, with a named decider.** The Decision reads "We will…" and the record names who decided (person or role) and the date. A record with no decider is incomplete.
6. **PM-106 — Consequences include the negatives.** Every record states what becomes harder, what is given up, and what risk is accepted — not only the benefits.
7. **PM-107 — Closed status lifecycle.** Status is exactly one of: proposed → accepted → deprecated, or superseded-by-ADR-NNNN. No other values, no free-text statuses.
8. **PM-108 — Accepted records are immutable except for Status.** A reversal is a new ADR that supersedes the old one and links to it; the old record's body is never edited, and its Status is updated to superseded-by-ADR-NNNN.
9. **PM-109 — DECISIONS.md is the index, not a copy.** The index lists each record's number, title, status, and link — and nothing else. Record content lives only in `docs/adr/`.
10. **PM-110 — Rejected options are recorded.** For contested decisions, each considered option is listed with why it lost. That record is what stops the decision being reopened later.
11. **PM-111 — Every fact in a record traces to evidence.** Figures, constraints, and claims in Context cite their source (a fact-sheet entry, a benchmark, a document). No number or constraint is invented to justify the choice.
12. **PM-112 — MADR records state how compliance is confirmed.** The Confirmation section names the check — a test, a review step, or a gate — that will show the decision is actually being followed.

## BAN list

- **BAN-PM-051 — Rewriting an accepted ADR in place.** Banned: editing the Context, Decision, or Consequences of an accepted record so the file no longer shows what was decided. Defeats: DET-CON-015. Bad: ADR-0007 said "We will use SQLite"; after the switch to Postgres someone edits it to say Postgres, and every document citing ADR-0007 now contradicts the record. Instead: leave ADR-0007 untouched, write ADR-0019 choosing Postgres, link it, and set ADR-0007's Status to superseded-by-ADR-0019. Severity: BLOCK.
- **BAN-PM-052 — Invented rationale.** Banned: stating figures, benchmarks, or constraints in Context that have no source behind them. Defeats: DET-CON-014. Bad: "Context: the current API handles only ~200 req/s" when no measurement exists and the fact sheet records no such limit. Instead: cite the measurement or fact-sheet entry, or state the limit as an unverified assumption and mark it as one. Severity: BLOCK.
- **BAN-PM-053 — The non-decision.** Banned: a Decision section hedged until it commits to nothing. Defeats: DET-CON-009. Bad: "We may possibly migrate to the new queue at some point if it seems beneficial." Instead: "We will migrate the notification queue to SQS by 2026-12-01; the decider is the tech lead; revisit only if the cost ceiling in ADR-0011 is exceeded." Severity: BLOCK.
- **BAN-PM-054 — Index as second copy.** Banned: pasting full ADR text into DECISIONS.md alongside the record in `docs/adr/`. Defeats: DET-CON-015. Bad: DECISIONS.md carries the full text of ADR-0003; the ADR is later superseded but the index copy is not, so the project states two different current decisions. Instead: the index holds number, title, status, and link only (PM-109); readers follow the link to the single canonical record. Severity: WARN.
- **BAN-PM-055 — Reused or duplicated ADR number.** Banned: assigning a number that an earlier record already used, or two records sharing one number. Defeats: DET-CON-017. Bad: a deleted draft's number 0012 is given to a new record, so existing citations to "ADR-0012" now point at two different decisions. Instead: numbers are allocated once, in order, and never recycled; a withdrawn record keeps its number with Status deprecated. Severity: BLOCK.

## Gates

- **G-PM-051 — Filename and numbering lint.** Verifies: PM-101. Check: automated — `ls docs/adr/ | grep -vE '^[0-9]{4}-[a-z0-9-]+\.md$'` must print nothing, and `ls docs/adr/ | cut -d- -f1 | sort | uniq -d` must print nothing (no duplicate numbers). Pass: zero output from both commands. Fail: block the change; renumber before merge. Recorded in: progress.md.
- **G-PM-052 — Index cross-check.** Verifies: PM-107, PM-109. Check: automated — script compares the set of files in `docs/adr/` against the links in DECISIONS.md and diffs each index status against the record's Status line. Pass: every record is indexed exactly once, every index link resolves, statuses agree. Fail: block; fix the index or the record, never both silently. Recorded in: progress.md.
- **G-PM-053 — Status and section lint.** Verifies: PM-103, PM-107. Check: automated — for each record, `grep -E '^## Status' -A1` yields a value in {proposed, accepted, deprecated, superseded-by-ADR-NNNN}, and the five section headings Title/Status/Context/Decision/Consequences are all present. Pass: all records conform. Fail: block; correct the status value or add the missing section. Recorded in: progress.md.
- **G-PM-054 — Immutability check.** Verifies: PM-108. Check: manual-assisted (script-supported) — for each accepted record, run the project's immutability script (sketch below) with the record's file and its acceptance commit. The script walks the `git log -p --follow` hunks after acceptance, tracks the current `## ` section from diff context lines, and prints a FLAG line for every added or removed line outside the Status section. The agent then reads each flagged line in the full diff and confirms it is a genuine body edit — hunk context can omit the section heading, so the script over-reports rather than under-reports, and the human/agent judgment on the flagged lines is part of the check. Pass: no confirmed body edits to any accepted record after its acceptance commit. Fail: block; restore the original body and express the change as a new superseding ADR. Recorded in: progress.md.

  ```bash
  # scripts/adr-immutability-check.sh FILE ACCEPTANCE_COMMIT
  git log -p --follow "$2..HEAD" -- "$1" | awk '
    /^diff --git/ { section = "" }
    /^ /  { if ($0 ~ /^ ## /) section = substr($0, 2); next }
    /^[+-]/ && $0 !~ /^\+\+\+/ && $0 !~ /^---/ {
      if (section != "## Status") print "FLAG: " $0
    }'
  ```

## Anti-patterns

- **The retroactive batch.** A dozen ADRs written in one sitting at project end, "reconstructing" decisions nobody remembers making. Catch it: creation dates cluster and Context reads omniscient — real records are written one at a time, at decision time (PM-102).
- **The rubber stamp.** Every record accepted with one option and "Consequences: none." Catch it: a record with no rejected option and no negative consequence has not been thought through (PM-106, PM-110).
- **The orphan decision.** Architecture visibly changed in the code but no ADR exists. Catch it: before accepting a structural change, search DECISIONS.md for its record; no hit means the record is written first.
- **The zombie proposal.** Records sit at "proposed" for months while the team already follows them. Catch it: the index cross-check (G-PM-052) review includes aging proposals — accept them or mark them deprecated.

## Examples

- [Example 1 — Reversal by supersession, not rewrite](examples/example-1.md) — corrects PM-108 / BAN-PM-051.
- [Example 2 — A decision that actually decides](examples/example-2.md) — corrects PM-105 / BAN-PM-053.
- [Example 3 — Index entry, not a second copy](examples/example-3.md) — corrects PM-109 / BAN-PM-054.

## Recall anchors

- One decision, one file, one number — never reused.
- Write it when you decide it, not when you remember it.
- Accepted means frozen; reversal means a new record.
- DECISIONS.md points; `docs/adr/` holds.
- Consequences include what it costs.

## Checklist

- [ ] Record created at decision time, in `docs/adr/`, with the next unused number (PM-101, PM-102).
- [ ] Five sections present; MADR escalation used if the decision was contested (PM-103).
- [ ] Decision is active voice and names the decider and date (PM-105).
- [ ] Negative consequences and rejected options are written down (PM-106, PM-110).
- [ ] Every fact in Context cites a source (PM-111).
- [ ] Status is a lifecycle value, and DECISIONS.md index entry added (PM-107, PM-109).
- [ ] Gates G-PM-051 to G-PM-054 pass; results recorded in progress.md.
