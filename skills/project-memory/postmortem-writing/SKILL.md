# postmortem-writing

## Metadata

- **Owner department:** D10 Project & Memory (PM)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Google SRE Workbook, "Postmortem Culture: Learning from Failure" — https://sre.google/workbook/postmortem-culture/ ; Atlassian, "Incident postmortems" — https://www.atlassian.com/incident-management/handbook/postmortems
- **Depends on:** runbook-writing (the runbook used in the incident is an input and a link target), progress-tracking (incidents and postmortems are recorded there)
- **Feeds into:** progress-tracking, handover, runbook-writing (lessons learned update the runbook that failed)

## When to use / Do NOT use

- **Use when:** an incident meets one of the project's configured postmortem triggers (PM-081) — user-visible downtime, data loss, manual on-call intervention, or a severity at or above the project's mandatory threshold.
- **Do NOT use when:** the event was a routine deployment, a caught-in-testing defect, or a near-miss below every trigger — those get a work-log or runbook note, not a postmortem. Do not use it to assign personal blame; that is the failure this skill exists to prevent (BAN-PM-041).

## Rules

1. **PM-081 — Triggers are configured parameters, never hardcoded.** The project sets its own trigger thresholds — severity levels, downtime minutes, data-loss classes — in its project files before incidents happen. Google SRE's triggers (user-visible downtime, data loss, on-call manual intervention) and Atlassian's (severity 1–2 mandatory) are worked examples to start from, not universal values; a small project copies the shape and sets its own numbers.
2. **PM-082 — Blameless by construction.** People are referred to by role ("the on-call engineer", "the deployer"), never named as a cause. Every cause is framed as a system or process property: what the system allowed, lacked, or failed to signal.
3. **PM-083 — Fixed structure, all sections present.** Every postmortem carries, in order: Summary, Impact, Timeline, Contributing causes, Mitigation, Follow-up actions. A missing section is an incomplete postmortem, not a stylistic choice.
4. **PM-084 — The timeline is built from records, never memory.** Each timeline entry carries a timestamp and its source (alert log, deploy log, monitoring graph, chat log). An event whose time cannot be sourced is marked "time unverified" — it is never given a plausible-looking time.
5. **PM-085 — Impact is measured, not estimated.** Duration, scope (users, requests, data affected), and severity come from monitoring and incident records. A figure with no record behind it is stated as unknown, not rounded into existence.
6. **PM-086 — Causes are contributing and multiple.** The analysis names every contributing system/process factor, plural. A single "root cause" line that stops at the triggering event — and any analysis that ends at "human error" — is incomplete: the question is always what made that action possible and its effect undetected.
7. **PM-087 — Every follow-up action has an owner, a due date, and a tracking ID.** Owner is a named person or role, the due date is an ISO date, and the tracking ID points at the project's tracker. An action missing any of the three does not count as an action and blocks closure.
8. **PM-088 — A named owner drives it to closure.** One named postmortem owner (by role) drives drafting, review, and approval. The postmortem closes only when every preventive action is filed in the tracker and tracked — writing the document is not closure.
9. **PM-089 — Review includes a blameless-language pass by a non-participant.** Someone not involved in the incident reviews the draft specifically for blame framing, memory-sourced timeline entries, and unsupported figures, before the postmortem is published.
10. **PM-090 — Published where the team can find it, and linked.** The finished postmortem lives in the project's postmortem location (repo or docs index) and is linked from progress.md and from the runbook for that incident class.
11. **PM-091 — Corrections are appended, never silently rewritten.** If a fact in a published postmortem turns out wrong, a dated correction note is appended stating what changed and why. The original text is not edited to look as if it was always right.
12. **PM-092 — Lessons reach the runbook.** Any procedure gap the incident exposed is fixed in the relevant runbook in the same change that closes the postmortem, or filed as a follow-up action under PM-087.

## BAN list

- **BAN-PM-041 — Naming a person as the cause.** Banned: any sentence that makes an individual the cause of the incident ("the outage happened because Alex deployed without checking"). Defeats: DET-CON-014. Bad: "Root cause: Priya restarted the wrong service." — a claim the logs contradict: the system offered two identically named services and no confirmation step. Instead: "Contributing cause: the admin console listed two services under the same display name and the restart action required no confirmation; the on-call engineer (role) selected the staging entry." Severity: BLOCK.
- **BAN-PM-042 — Timeline from memory.** Banned: timeline entries with timestamps reconstructed from recollection or rounded to plausible times, with no log source. Defeats: DET-CON-014. Bad: "14:05 — team noticed errors; 14:20 — rollback started" written the next day from memory, when the alert log shows first alert 13:47 and rollback 14:31. Instead: every entry cites its source — "13:47 — alert fired (alert log #A-2214); 14:31 — rollback initiated (deploy log)". Severity: BLOCK.
- **BAN-PM-043 — "Be more careful" actions.** Banned: follow-up actions that are exhortations or intentions — "be more careful", "double-check next time", "pay more attention" — or any action with no owner, due date, or tracking ID. Defeats: DET-CON-028. Bad: "Action: engineers will be more careful with migrations. Owner: team." Instead: "Action: add a pre-migration dry-run check to the deploy pipeline. Owner: platform lead. Due: 2026-12-05. Tracker: OPS-118." Severity: BLOCK.
- **BAN-PM-044 — Invented impact figures.** Banned: impact numbers with no monitoring or incident record behind them ("about 10,000 users were affected", "roughly two hours of downtime") presented as findings. Defeats: DET-CON-011. Bad: "Impact: ~5,000 users, ~3 hours" in a postmortem whose monitoring shows 41 minutes and no user-count query was ever run. Instead: "Impact: 41 minutes of elevated errors (monitoring, incident window 13:47–14:28); affected-user count not measured — recorded as unknown." Severity: BLOCK.
- **BAN-PM-045 — The single root cause that stops at the trigger.** Banned: a Contributing causes section with one line naming the triggering event or a person's action as "the root cause", with no system or process factors. Defeats: DET-CON-014. Bad: "Root cause: a bad config was deployed." — contradicted by the postmortem's own timeline, which shows the config passed a validator that did not check that field. Instead: list each contributing factor: the field was unvalidated, staging did not mirror the production value, and the deploy had no canary stage. Severity: BLOCK.

## Gates

- **G-PM-041 — Section completeness check.** Verifies: PM-083. Check: automated — `grep -cE '^## (Summary|Impact|Timeline|Contributing causes|Mitigation|Follow-up actions)' postmortem-<incident>.md` returns 6. Pass: all six sections present. Fail: block publication; add the missing section. Recorded in: progress.md.
- **G-PM-042 — Action-row completeness check.** Verifies: PM-087. Check: automated — parse the Follow-up actions table and assert every row has non-empty Action, Owner, Due date (matching `^[0-9]{4}-[0-9]{2}-[0-9]{2}$`), and Tracking ID fields, e.g. `awk -F'|' 'NR>2 && NF>5 && ($3=="" || $4=="" || $5=="" || $6=="") {print "incomplete action row:", NR}' postmortem-<incident>.md` prints nothing. Pass: zero incomplete rows. Fail: block closure until each action is owned, dated, and tracked. Recorded in: progress.md.
- **G-PM-043 — Blame and vagueness lint.** Verifies: PM-082, PM-086, PM-087. Check: automated plus manual — `grep -inE 'be more careful|double-check next time|pay more attention|root cause: (a |the )?(human|operator|engineer)' postmortem-<incident>.md` prints nothing, and the PM-089 non-participant reviewer signs off that no person is named as a cause. Pass: no lint hits and reviewer sign-off recorded. Fail: rewrite the flagged passages as system/process causes before publication. Recorded in: progress.md.
- **G-PM-044 — Timeline sourcing and linkage check.** Verifies: PM-084, PM-090. Check: automated — every Timeline row carries a source marker (log, alert, or record reference) or the words "time unverified", and `grep -l 'postmortem-<incident>' progress.md <runbook>.md` lists both files. Pass: all entries sourced or marked, both links present. Fail: block publication; source the entries from the logs and add the links. Recorded in: progress.md.

## Anti-patterns

- **The sanitized timeline.** Detection and response gaps are quietly smoothed over: the 25 minutes between first alert and first responder vanish, so the timeline reads as instant response. Catch it: diff the timeline against the alert log — any gap with no entry is a gap to explain, not to hide.
- **The orphaned actions.** Actions are filed at closure, then never looked at again; due dates pass silently and the same incident recurs. Catch it: closure (PM-088) means the tracker owns the actions — review open postmortem actions wherever the project reviews its tracker, not only when writing the next postmortem.
- **The copy-paste postmortem.** Causes and actions are boilerplate reused across incidents ("add more monitoring", "improve communication") regardless of what actually failed. Catch it: if an action sentence could be pasted into a different incident unchanged, it describes nothing about this one.
- **The victory lap.** Three paragraphs celebrate the heroic fix; the causes section is one line and prevention is an afterthought. Catch it: compare section lengths — when Mitigation dwarfs Contributing causes and Follow-up actions combined, the document is a story, not an analysis.

## Examples

- [Example 1 — Blame line rewritten as a system cause](examples/example-1.md) — corrects PM-082 / BAN-PM-041.
- [Example 2 — Memory timeline replaced by a log-sourced timeline](examples/example-2.md) — corrects PM-084 / BAN-PM-042.
- [Example 3 — "Be more careful" replaced by an owned, dated, tracked action](examples/example-3.md) — corrects PM-087 / BAN-PM-043.

## Recall anchors

- Blame the system that allowed it, never the person who did it.
- Timeline from logs, or mark it unverified — never from memory.
- Causes are plural; "human error" is where analysis starts, not ends.
- No owner, no due date, no tracking ID — no action.
- Closed means the preventive actions are tracked, not that the document is written.

## Checklist

- [ ] Incident met a configured trigger, and the trigger values came from the project's own settings (PM-081).
- [ ] All six sections present: Summary, Impact, Timeline, Contributing causes, Mitigation, Follow-up actions (PM-083).
- [ ] People appear by role only; every cause is a system or process property (PM-082).
- [ ] Every timeline entry is timestamped with its log source, or marked "time unverified" (PM-084).
- [ ] Impact figures come from monitoring/incident records; unmeasured values are stated as unknown (PM-085).
- [ ] Every follow-up action has an owner, an ISO due date, and a tracking ID (PM-087).
- [ ] Non-participant blameless review passed, postmortem published and linked from progress.md and the runbook (PM-089, PM-090).
- [ ] Gates G-PM-041 to G-PM-044 pass; results recorded in progress.md.
