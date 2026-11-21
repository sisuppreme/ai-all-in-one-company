# runbook-writing

## Metadata

- **Owner department:** D10 Project & Memory (PM)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** PagerDuty, "What is a Runbook?" (Limoncelli's runbook sections) — https://www.pagerduty.com/resources/automation/learn/what-is-a-runbook/ ; PROJECT_ANATOMY.md Appendix A, runbook.md row (Google SRE practice)
- **Depends on:** documentation-writing
- **Feeds into:** postmortem-writing, handover, incident-response

## When to use / Do NOT use

- **Use when:** an incident class recurs, an alert fires, or a procedure (deploy rollback, failover, certificate renewal, data backfill) must be executable by whoever is on call — including someone who did not build the system, at 3 a.m., under pressure.
- **Do NOT use when:** the document explains how the system works (that is documentation-writing / explanation), records a past incident (postmortem-writing), or is a one-off task never expected to repeat. A runbook is a procedure to execute, not a narrative to read.

## Rules

1. **PM-061 — One runbook, one incident class.** Each runbook covers exactly one alert, symptom, or repeated procedure. Two failure modes in one file get two files, each named for its trigger.
2. **PM-062 — Fixed section order.** Every runbook carries, in order: service overview, trigger/symptom, prerequisites, numbered steps, escalation, verification. No section is omitted; an inapplicable section states why.
3. **PM-063 — Steps are actions with expected results.** Each step is one action — an exact command or a concrete UI action — followed by the output or state that confirms it worked. A step with no expected result is unfinished.
4. **PM-064 — Branch on difference.** Where a step's output can differ, the runbook states what to do in each case ("if the pod does not appear, go to step 9"). The executor never has to guess which branch reality took.
5. **PM-065 — Exact, runnable values.** Commands are copy-paste runnable against the real system: real hostnames, real service names, real flags. Placeholder tokens (`<host>`, `your-server`, `example.com`) never survive into a shipped runbook.
6. **PM-066 — Prerequisites up front.** Access required, where credentials live (the vault or system name — never the secret values), tools to install, and the dashboards to open are all listed before step 1, never discovered mid-incident.
7. **PM-067 — The alert links here.** Every alert this runbook serves links to the runbook file, and the runbook's trigger section names that alert or symptom verbatim, so the path from page to procedure is one click and unambiguous.
8. **PM-068 — Escalation names a role.** The escalation path names a role (e.g. "database on-call"), how to reach it, and the condition or time threshold that triggers escalation. A person's name may appear additionally, never instead.
9. **PM-069 — Verification closes the runbook.** The final step is an observable check that proves resolution — a health endpoint returning 200, the alert cleared, a real user action succeeding — not the absence of error messages.
10. **PM-070 — Same-change updates.** A runbook is updated in the same change as any incident that used it and exposed an error, and after any change to the procedure it describes. A runbook known to be wrong is fixed or withdrawn that day, not left for the next incident.
11. **PM-071 — Written for the stranger.** The runbook must be executable by a competent engineer who did not build the system and has never seen this incident. Every term, system, and "usual" step is spelled out or linked.
12. **PM-072 — Reference generic process, never copy it.** Incident-wide process (declare the incident, open the timeline, notify stakeholders) is linked to the one canonical process document, not pasted into each runbook where copies drift apart.

## BAN list

- **BAN-PM-031 — The filler step.** Banned: a step that gestures at the work instead of specifying it ("check the database and fix any issues"). Defeats: DET-CON-006. Bad: step 3 reads "Investigate the connection pool and resolve the problem." Instead: give the exact query, the healthy output range, and the action for each outcome (PM-063, PM-064). Severity: BLOCK.
- **BAN-PM-032 — Placeholder values shipped.** Banned: unreplaced template values in commands, hosts, or contacts (`<your-db-host>`, `TODO: add command`, `admin@example.com`). Defeats: DET-CON-003. Bad: the failover step runs `psql -h <db-host>` and the on-call must hunt for the hostname mid-incident. Instead: ship the real hostname, or the exact command that retrieves it (PM-065). Severity: BLOCK.
- **BAN-PM-033 — Person-only escalation.** Banned: an escalation path that names only an individual ("call Dave") with no role, channel, or fallback. Defeats: DET-CON-005. Bad: Dave left the company in March; the runbook still routes a page-down incident to his phone. Instead: escalate to the owning role via the paging tool, with the time threshold stated (PM-068). Severity: BLOCK.
- **BAN-PM-034 — The stale runbook.** Banned: shipping or keeping a runbook whose commands, hosts, or thresholds no longer match the system, past its `last_reviewed` date. Defeats: DET-CON-018. Bad: the rollback runbook targets a cluster decommissioned two releases ago; the review date is eight months old. Instead: re-verify against the live system and update `last_reviewed`, or withdraw the runbook (PM-070). Severity: BLOCK.
- **BAN-PM-035 — Resolution declared without verification.** Banned: ending a runbook at the fix ("restart the service and close the ticket") with no step that proves the user-visible problem is gone. Defeats: DET-CON-028. Bad: the service restarts cleanly, the ticket closes, and checkout is still failing for users. Instead: end with the observable verification check and its pass value (PM-069). Severity: BLOCK.

## Gates

- **G-PM-031 — Structure check.** Verifies: PM-061, PM-062, PM-063. Check: automated — script asserts each runbook file contains the six PM-062 section headings in order, and that every numbered step is followed by an "Expected:" line. Pass: all runbooks conform. Fail: block the change. Recorded in: progress.md.
- **G-PM-032 — Placeholder scan.** Verifies: PM-065, PM-066. Check: automated — `grep -rnE '<[a-z-]+>|TODO|FIXME|example\.com|your-[a-z]+|localhost' runbooks/` returns no hits outside explicitly marked illustrative blocks. Pass: zero hits. Fail: block the change. Recorded in: progress.md.
- **G-PM-033 — Freshness gate.** Verifies: PM-070. Check: automated — compare each runbook's `last_reviewed` front matter against the project's review window (a project policy parameter; default 90 days). Pass: every runbook is inside its window. Fail: block release until re-verified or withdrawn. Recorded in: progress.md.
- **G-PM-034 — Link check.** Verifies: PM-066, PM-067. Check: automated — run lychee over the runbooks directory; every dashboard, tool, and alert link resolves. Pass: zero broken links. Fail: fix or remove the link before merge. Recorded in: progress.md.
- **G-PM-035 — Cold-run drill.** Verifies: PM-063, PM-064, PM-071. Check: manual — someone other than the author executes the runbook in a drill or tabletop exercise and completes it without asking the author a single question. Pass: completed unaided; every hesitation is filed as a runbook fix. Fail: revise and re-drill. Recorded in: progress.md.

## Anti-patterns

- **The war story.** The runbook narrates one past incident ("On 14 May the cache filled because…") instead of giving a reusable procedure. Catch it: dates and past tense in the steps; rewrite each anecdote into the action it taught.
- **The screenshot procedure.** Steps exist only as UI screenshots, unsearchable and silently wrong after the next UI release. Catch it: search the file for its own key commands — if the text is not in the file, neither is the procedure.
- **The expert's shorthand.** "Bounce the usual box and clear the queue like last time." Catch it: any step the author cannot expand into PM-063 form on demand fails PM-071; the cold-run drill (G-PM-035) exposes it.
- **The twin runbooks.** One copy in the repo, one in a wiki, each edited independently. Catch it: search both locations for the procedure's name; one canonical file survives, the other becomes a link (PM-072's rule applied to the runbook itself).

## Examples

- [Example 1 — Narrative steps rewritten as actions with expected results](examples/example-1.md) — corrects PM-063.
- [Example 2 — Person-only escalation replaced by role escalation and verification](examples/example-2.md) — corrects PM-068.
- [Example 3 — Placeholder commands and missing prerequisites made executable](examples/example-3.md) — corrects PM-066.

## Recall anchors

- Steps are actions with expected results — never explanations.
- Prerequisites before step 1; nothing is discovered mid-incident.
- Escalate to a role, not a person.
- The runbook ends by proving the fix, not by performing it.
- If an incident exposed an error, the fix lands in the same change.

## Checklist

- [ ] Sections present in order: overview, trigger, prerequisites, steps, escalation, verification (G-PM-031).
- [ ] Every step has an exact command or action and an "Expected:" result (PM-063).
- [ ] Every step whose output can differ carries a branch (PM-064).
- [ ] Placeholder scan is clean: no `<tokens>`, TODOs, or example values (G-PM-032).
- [ ] Prerequisites list access, credential locations (never values), tools, dashboards (PM-066).
- [ ] Escalation names a role, a channel, and a time threshold (PM-068).
- [ ] Final step is an observable verification with a pass value (PM-069).
- [ ] `last_reviewed` is inside the review window; cold-run drill passed or scheduled (G-PM-033, G-PM-035).
