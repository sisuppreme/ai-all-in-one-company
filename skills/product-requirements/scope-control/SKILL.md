# scope-control

## Metadata

- **Owner department:** D1 Product & Requirements (PR)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://projeric.com/blogs/scope-management/moscow-prioritization ; https://resources.rework.com/libraries/project-management/moscow-prioritization
- **Depends on:** requirements-writing
- **Feeds into:** roadmapping, user-stories

## When to use / Do NOT use

- **Use when:** a release or iteration has a fixed timeframe and more candidate work than capacity; a scope document is being written, re-triaged, or changed mid-flight; public copy is about to describe what the release includes.
- **Do NOT use when:** there is no requirements list yet (use requirements-writing first), or the question is long-term sequencing rather than this release's boundary (use roadmapping).

## Rules

1. **PR-141 — Four classes, always.** Every scope document classifies every candidate item as Must, Should, Could, or Won't have (this time), per DSDM/MoSCoW. An item with no class is not in scope and not out of scope — it is undecided, and undecided items never reach build or copy.
2. **PR-142 — Non-empty Won't-have list.** The scope document contains a Won't have (this time) section with at least one named item. A boundary that excludes nothing bounds nothing.
3. **PR-143 — Every Must traces to an objective.** Each Must have carries a link to the stated project objective it serves. A Must with no objective is demoted to Should pending review.
4. **PR-144 — Must effort capped at ~60%.** Must haves total no more than about 60% of the timeframe's estimated effort, measured by effort, not by item count, so Should and Could items act as contingency.
5. **PR-145 — Over-cap Musts force re-triage.** If estimated Must effort exceeds ~60% of capacity, re-triage happens before build starts. Proceeding anyway is a defect, not enthusiasm — unless the release records an explicit override, mirroring PR-224 in unit-economics: the override note states that the cap is exceeded, the reason, and the contingency risk accepted. An unrecorded over-cap is still a defect.
6. **PR-146 — Fixed de-scope order.** When the timeframe is threatened, items are cut in the agreed order: Could first, then Should. Musts and the date hold unless the release is re-baselined under PR-147.
7. **PR-147 — Changes displace or re-baseline.** A scope change enters only by displacing equal estimated effort from a lower class, or by a recorded re-baseline of the release (new date or new capacity) approved by the decider named in the document.
8. **PR-148 — Every change is logged.** Each scope change records the item, the decider, the date, and what it displaced. An unlogged change is treated as never approved.
9. **PR-149 — Public copy mirrors Must and Should only.** Marketing pages, changelogs, and sales material may describe Must and Should items as included. Could items are never presented as included, and Won't-have items are never presented at all.
10. **PR-150 — Owner and review date.** The scope document names one owner and a review date. A scope document past its review date cannot authorize new commitments until re-reviewed.

## BAN list

- **BAN-PR-071 — Unscoped feature in public copy.** Banned: describing a feature in marketing copy, a changelog, or a sales deck when the scope document classes it Could or Won't have (this time). Defeats: DET-CON-004. Bad: the landing page lists "SSO login — included in Pro" while the scope document has SSO under Won't have (this time). Instead: copy is written from the Must and Should classes only (PR-149). Severity: BLOCK.
- **BAN-PR-072 — Dated promise for unvalidated scope.** Banned: attaching a launch date or "coming soon" announcement to any item that is not a Must have with acceptance criteria attached. Defeats: DET-CON-018. Bad: a banner reads "AI reports launch March 1" for an item classed Could with no criteria written. Instead: announce only Must items, and only with the release's own date. Severity: BLOCK.
- **BAN-PR-073 — Silent scope absorption.** Banned: adding an item to the build without a change-log entry naming the decider and the displaced item. Defeats: DET-CON-015. Bad: a stakeholder asks in chat for CSV export, it gets built, and the help center and the pricing page end up describing different feature sets. Instead: log the change under PR-148 before build starts. Severity: BLOCK.
- **BAN-PR-074 — Promising a scope item as an operational commitment.** Banned: copy that commits the business to an ongoing service (support hours, uptime, response times) that no scope item or policy funds. Defeats: DET-CON-028. Bad: the pricing page promises "24/7 support" while the release scope contains no support staffing item at all. Instead: the promise is scoped and funded first, or the copy is cut. Severity: BLOCK.

## Gates

- **G-PR-071 — Won't-have presence check.** Verifies: PR-141, PR-142. Check (automated): `sed -n "/won't have/I,/^## /p" scope.md | grep -q "^- "` — the Won't have section must contain at least one list item. Pass: command exits 0. Fail: block shipment. Recorded in: progress.md.
- **G-PR-072 — Must effort-share computation.** Verifies: PR-144, PR-145. Check (automated): export the requirements table to CSV (columns: item,class,effort) and run `awk -F, '$2=="Must"{m+=$3} {t+=$3} END {print m/t}' requirements.csv`. Pass: output ≤ 0.60. Fail: block shipment until re-triage is recorded. Recorded in: progress.md.
- **G-PR-073 — Must-to-objective trace check.** Verifies: PR-143. Check (automated): every row classed Must in the requirements table has a non-empty objective column; a script or spreadsheet filter for `class=Must AND objective=""` must return zero rows. Pass: zero rows. Fail: block shipment. Recorded in: progress.md.
- **G-PR-074 — Change-log audit.** Verifies: PR-147, PR-148. Check (manual): diff the current scope document against its previous version; every added or reclassed item must have a matching change-log entry with decider, date, and displaced item. Pass: zero unexplained diffs. Fail: block shipment. Recorded in: progress.md.
- **G-PR-075 — Copy-to-scope sweep.** Verifies: PR-149. Check (manual): list every feature named in the release's public copy; each must appear in the scope document as Must or Should. Pass: zero features sourced from Could or Won't have. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Priority by loudness.** The class of an item quietly tracks who asked most recently or most seniorly, while the document still shows the old classes. Catch it by comparing the change log against who requested each reclass.
- **Contingency spent twice.** The same Should item is named as the buffer for two different Must overruns. Catch it by listing, for each Must, which contingency covers it — duplicates mean the buffer does not exist.
- **Shadow scope in tickets.** Work enters through the issue tracker without ever touching the scope document, so the document stays clean and wrong. Catch it by sampling closed tickets each iteration and checking each against the scope classes.
- **Won't-have amnesia.** An item classed Won't have (this time) reappears next release with no record that it was ever excluded, so its earlier rejection reasoning is lost. Catch it by carrying the Won't-have list forward into the next scope document as the starting draft.

## Examples

- [Example 1 — The boundary that excluded nothing](examples/example-1.md) — violates/corrects PR-142.
- [Example 2 — Ninety percent Must](examples/example-2.md) — violates/corrects PR-144, PR-145.
- [Example 3 — The chat-request feature](examples/example-3.md) — violates/corrects PR-148.

## Recall anchors

- Four classes or it is not a scope document.
- A boundary that excludes nothing bounds nothing.
- Musts ≤ ~60% of effort — the rest is contingency.
- Changes displace, or the release is re-baselined. Never both silently.
- Public copy mirrors Must and Should only.

## Checklist

- [ ] Every candidate item carries a MoSCoW class (PR-141).
- [ ] Won't have (this time) section exists and is non-empty (PR-142, G-PR-071).
- [ ] Every Must links to a stated objective (PR-143, G-PR-073).
- [ ] Must effort share computed and ≤ ~60% (PR-144, G-PR-072).
- [ ] De-scope order (Could, then Should) written in the document (PR-146).
- [ ] Every change since the last version is logged with decider, date, and displacement (PR-148, G-PR-074).
- [ ] Public copy checked against Must/Should classes only (PR-149, G-PR-075).
- [ ] Owner and review date present and current (PR-150).
