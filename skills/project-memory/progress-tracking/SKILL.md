# progress-tracking

## Metadata

- **Owner department:** D10 Project & Memory (PM)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** datadef.io, docs checks in CI (freshness-gate pattern) — https://datadef.io/guides/en/docs-checks-in-ci ; Sourcegraph, "Documentation as code" — https://sourcegraph.com/blog/documentation-as-code
- **Depends on:** project-templates, decision-logs
- **Feeds into:** handover, memory-retrieval, postmortem-writing

## When to use / Do NOT use

- **Use when:** any work starts, changes state, blocks, or finishes on a project — progress.md is updated as part of that work, and every gate result from every skill is recorded here. Anyone asking "where does this project stand?" is answered from this file.
- **Do NOT use when:** recording history or rationale — effort narration belongs in the work log and git, decisions belong in DECISIONS.md via decision-logs, incident analysis belongs in postmortem-writing. progress.md holds current verified state only.

## Rules

1. **PM-141 — One status of record.** progress.md is the project's single status file. Status maintained in chat, a dashboard, or a README section instead is merged into progress.md or deleted.
2. **PM-142 — Verified state only.** An item is marked done only when its gate result is recorded in progress.md. Attempted, drafted, or "should work" is in progress — never done.
3. **PM-143 — Gate results land here.** Every gate run, from every skill loaded for the work, records its result in progress.md: gate ID, pass or fail, date. A gate with no recorded result is treated as never run.
4. **PM-144 — Every entry is dated.** Each status entry carries an ISO 8601 date. An undated entry is treated as stale: re-verify it or remove it at the next update.
5. **PM-145 — Done names the artifact.** Every done item names or links what was produced. A done claim whose artifact cannot be found in the repo is not done.
6. **PM-146 — Updated with the work.** progress.md is updated in the same change as the work it reports. A separate status-update commit made later is a process defect.
7. **PM-147 — Blocked is a triple.** A blocked item names the blocker, the blocker's owner, and the condition that unblocks it. "Waiting" alone is not a status.
8. **PM-148 — Four states only.** Entries are done, in progress, blocked, or next. No other status vocabulary: "almost done", "wrapping up", and "90%" are not states.
9. **PM-149 — State, not effort.** progress.md reports state. Hours spent, difficulty, and history belong in the work log and git history, never in the status file.
10. **PM-150 — Decisions and incidents link out.** A decision made during the work is appended to DECISIONS.md via decision-logs and linked from progress.md; an incident links its postmortem. progress.md is never the only copy of either.
11. **PM-151 — Next is concrete.** The Next section names the upcoming actions, each with an owner. An empty Next while unfinished work exists is a defect.
12. **PM-152 — Stale entries are resolved, not carried.** At each update, entries older than the current work cycle are re-verified against the deliverable, then corrected or deleted — never silently carried forward.

## BAN list

- **BAN-PM-071 — Done on attempt.** Banned: marking an item done because the work was attempted or drafted, with no gate result recorded. Defeats: DET-CON-015. Bad: "Auth flow — done" while the auth gate never ran and the flow accepts a wrong password. Instead: run the gate, record its result with gate ID and date, and only then mark the item done. Severity: BLOCK.
- **BAN-PM-072 — The invented percentage.** Banned: progress figures ("80% complete", "frontend 90% done") with no counted list of items behind them. Defeats: DET-CON-011. Bad: a status report claims the frontend is 90% done with no inventory of frontend items anywhere. Instead: report counts over a named item list ("14 of 16 screens pass their gates"), or report states with no percentage. Severity: BLOCK.
- **BAN-PM-073 — The kickoff fossil.** Banned: progress.md entries that predate the current work cycle presented as current status. Defeats: DET-CON-018. Bad: progress.md still says "scaffolding in progress" three releases after launch because nobody touched it since kickoff. Instead: update the file in the same change as the work; re-verify or delete stale entries at every update. Severity: BLOCK.
- **BAN-PM-074 — Template status shipped.** Banned: generator boilerplate or placeholder text ("Project status — TODO", "coming soon") surviving in a shipped progress.md. Defeats: DET-CON-004. Bad: the scaffold's "Status: TODO" line is still the first line of progress.md in a released repo. Instead: replace boilerplate with dated, verified entries at project start, or delete the placeholder line. Severity: WARN.
- **BAN-PM-075 — The bare "blocked".** Banned: a blocked entry naming no blocker, no owner, and no unblocking condition. Defeats: DET-CON-028. Bad: "Blocked: waiting on API keys" — nobody can act on it, and nobody is named who could. Instead: record the triple — what blocks, who owns the blocker, what unblocks it — plus a re-check date. Severity: WARN.

## Gates

- **G-PM-071 — Freshness gate.** Verifies: PM-144, PM-146. Check: automated — `git log -1 --format=%cs -- progress.md` must fall within the current work cycle (project policy window, default 7 days while work is active), and a grep confirms every entry line carries an ISO date. Pass: both conditions true. Fail: all status is treated as stale; update progress.md before any status report leaves the project. Recorded in: progress.md.
- **G-PM-072 — Done-artifact check.** Verifies: PM-142, PM-145. Check: automated — extract the file paths and links named by done entries and assert each exists (`test -f` for paths, link resolution for URLs). Pass: every done item's artifact exists. Fail: the item reverts to in progress until the artifact exists. Recorded in: progress.md.
- **G-PM-073 — Gate-result completeness.** Verifies: PM-143. Check: automated — collect the gate IDs recorded in progress.md and diff them against the gate IDs of the skills loaded for the current work. Pass: every loaded skill's gates appear with a pass/fail result and a date. Fail: block the status report; run the missing gates or record why they do not apply. Recorded in: progress.md.
- **G-PM-074 — Sampled truth audit.** Verifies: PM-142, PM-152. Check: manual — sample three entries (one done, one in progress, one blocked) and confirm each against the actual deliverable, the named blocker owner, and the repo state. Pass: 3 of 3 match reality. Fail: correct the file and re-audit the full entry list. Recorded in: progress.md.

## Anti-patterns

- **The victory lap.** progress.md narrates effort — "long week wrestling with the build" — instead of state. Catch it: scan for effort language; a status entry is a dated fact about an item, nothing else (PM-149).
- **The parallel status.** The real status lives in chat messages or a separate dashboard while progress.md quietly rots. Catch it: ask where a newcomer would look; if the honest answer is not progress.md, merge the rival and delete it (PM-141).
- **Zombie next steps.** The Next section lists items already finished or abandoned long ago, so nobody trusts it. Catch it: at every update, each Next item is promoted, re-dated with an owner, or deleted (PM-151, PM-152).
- **The silent unblock.** The blocker cleared days ago but the entry still says blocked, so readers route around finished work. Catch it: blocked entries carry re-check dates; an entry past its re-check date is tested against its unblocking condition before anything else is updated.

## Examples

- [Example 1 — Done on attempt, corrected to done on gate result](examples/example-1.md) — corrects PM-142.
- [Example 2 — A bare "blocked" rewritten as a triple](examples/example-2.md) — corrects PM-147.
- [Example 3 — A kickoff-fossil progress.md re-verified entry by entry](examples/example-3.md) — corrects PM-152.

## Recall anchors

- Done means a gate result is recorded — not attempted, recorded.
- Every entry dated; undated is stale.
- Done names the artifact; no artifact, no done.
- Blocked is a triple: blocker, owner, unblocking condition.
- Update progress.md in the same change as the work.

## Checklist

- [ ] progress.md updated in the same change as the work it reports (PM-146).
- [ ] Every done item has its gate result recorded, with gate ID and date (PM-143).
- [ ] Every done item names or links an artifact that exists (G-PM-072).
- [ ] No undated entries; stale entries re-verified or removed (PM-144, PM-152).
- [ ] Every blocked item names blocker, owner, and unblocking condition (PM-147).
- [ ] No percentage appears without a counted item list behind it (BAN-PM-072).
- [ ] Decisions appended to DECISIONS.md and incidents linked to their postmortems (PM-150).
