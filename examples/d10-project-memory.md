# D10 Project Memory — End-to-End Example

## Scenario

A solo developer built "NoteNest," a small note-taking SaaS, over eight months and is
handing it to a new maintainer before leaving the project. The transfer package is the
repo plus a handover note. Everything the receiver needs to run, fix, and trust the
project has to survive the giver walking away.

## Before — the slop version

`handover.md`, written on the giver's last day:

```markdown
# Handover — NoteNest

Status: about 90% done, basically launch-ready. Auth flow — done.

## Access (so you can log in right away)
- Production database: postgres://notes_admin:Tr7!falcon@db.notenest.internal:5432/notes
- Payment provider secret key: <the live key, pasted in full>

## Known issues
None — all good. The app is stable.

Repo's all yours — good luck! 🚀
```

What is wrong, visibly: real credentials sit in a document; "90%" has no counted list
behind it; "Auth flow — done" names no gate result and no artifact; the risks section
says "none" while the project's own postmortem follow-up about a payment-retry defect
is still open; there is no named accepting owner, no date, and no walkthrough.

## What the skills caught

- **BAN-PM-091 — Secret values in handover materials** (defeats DET-CON-003). The
  database password and the live payment key are pasted into a transferred document.
  **PM-185** requires the credentials *path* — system, vault, grant procedure — never
  the values.
- **BAN-PM-093 — Landmines by omission** (defeats DET-CON-014). "None — all good"
  contradicts the project's own records. **PM-184** requires every open risk listed
  with evidence, or an explicit "no known landmines" finding after checking them.
- **BAN-PM-072 — The invented percentage** (defeats DET-CON-011). "90% done" has no
  item inventory behind it. **PM-148** allows four states only: done, in progress,
  blocked, next.
- **BAN-PM-071 — Done on attempt** (defeats DET-CON-015). "Auth flow — done" with no
  gate result recorded violates **PM-142** (verified state only) and **PM-143** (gate
  results land in progress.md with ID and date).
- **BAN-PM-092 — The link-and-cheer handover** (defeats DET-CON-028). A repo link and
  encouragement is not a transfer: **PM-181** makes handover a readiness review,
  **PM-182** requires a named accepting owner, **PM-183** a dated, recorded acceptance,
  and **PM-190** makes the receiver's cold run the acceptance test.

## After — the corrected version

`handover.md` (maintained during the project per PM-192, finalized at transfer):

```markdown
# Handover — NoteNest

## Acceptance
Accepted by: A. Rahman, maintainer (role: project owner), 2026-11-14.
Scope accepted: application repo, runbooks, decision records, progress file.
Cold run (PM-190) completed 2026-11-14: deployed from these materials alone,
located the incident runbook for "payment webhook failing," named the top
open risks below.

## Access — credentials path only (PM-185)
- Production database: credentials in the project vault (folder "NoteNest/prod");
  access is granted by the vault owner on request — no values in this document.
- Payment provider: secret key held in the provider dashboard's team settings;
  the accepting owner was added as a team member on 2026-11-14.

## Landmines (PM-184)
1. Payment-retry defect: a failed first charge is retried without an idempotency
   key in one legacy path. Evidence: postmortem 2026-10-30, follow-up item 3,
   still open. Owner: A. Rahman. Unblocks: scheduled fix in the December cycle.
2. Session tokens do not rotate on password change. Evidence: issue #112.
   Owner: A. Rahman.

## Status of record
See progress.md — every item is dated, in one of the four states (PM-148),
and every "done" names its artifact and gate result (PM-143, PM-145).
Auth flow: done — the auth gate's result is recorded in progress.md, 2026-11-09.
```

The memory set — runbooks, postmortems, DECISIONS.md and the ADR set, progress.md,
the fact sheet — is a line item in the transfer manifest (PM-186), so the receiver
gets the project's memory, not only its code (BAN-PM-094).

## Skills used

- [handover](../skills/project-memory/handover/SKILL.md)
- [progress-tracking](../skills/project-memory/progress-tracking/SKILL.md)
- [decision-logs](../skills/project-memory/decision-logs/SKILL.md)
- [project-templates](../skills/project-memory/project-templates/SKILL.md)
