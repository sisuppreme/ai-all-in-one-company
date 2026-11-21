# handover

## Metadata

- **Owner department:** D10 Project & Memory (PM)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Google Cloud Blog, "How SREs find the landmines in a service" (Production Readiness Review practice) — https://cloud.google.com/blog/products/gcp/how-sres-find-the-landmines-in-a-service-cre-life-lessons ; datadef.io, docs checks in CI (freshness-gate pattern) — https://datadef.io/guides/en/docs-checks-in-ci ; Sourcegraph, "Documentation as code" — https://sourcegraph.com/blog/documentation-as-code
- **Depends on:** project-templates, progress-tracking, memory-retrieval
- **Feeds into:** none — handover is the terminal transfer step; its outputs are consumed by the receiving owner, not by another skill

## When to use / Do NOT use

- **Use when:** a project changes hands — new owner, new maintainer, end of engagement, or the single agent's work is picked up by a different operator. handover.md is maintained during the project and finalized at transfer; this skill runs the readiness review and the acceptance test that close the transfer.
- **Do NOT use when:** recording day-to-day status (progress-tracking), writing the runbooks and postmortems that transfer (runbook-writing, postmortem-writing), or recording why decisions were made (decision-logs). This skill verifies and transfers the project's memory; it does not author it.

## Rules

1. **PM-181 — Handover is a process, not a document.** It runs as a readiness review against a checklist — mandated file set fresh and complete, architecture and failure-mode walkthroughs, landmines list, credentials path, acceptance — modeled on Google's Production Readiness Review. A file drop with no review is not a handover.
2. **PM-182 — No handover without a named accepting owner.** The receiver is a named person or role who agrees to take the project on. A transfer addressed to "the team" or to nobody has not happened.
3. **PM-183 — Acceptance is recorded, with a date.** handover.md records who accepted, in what role, on which ISO 8601 date, and what scope they accepted. Undated or unsigned acceptance does not count.
4. **PM-184 — Landmines are listed explicitly, each with evidence.** Every open risk, known fragility, and unresolved follow-up appears in the landmines list with evidence or a link to where the evidence lives. If there are none, handover.md states "no known landmines" as a finding — silence is never read as none.
5. **PM-185 — Credentials path, never credentials.** Handover materials name each system, where its secrets live (vault, provider, owner), and the procedure by which access is granted or transferred. Secret values — passwords, tokens, keys — never appear in handover.md or any transferred document.
6. **PM-186 — The memory transfers, not only the code.** Runbooks, postmortems, DECISIONS.md and the ADR set, progress.md, and the fact sheet are line items in the transfer manifest. A receiver who gets code without the project's memory has received a partial handover.
7. **PM-187 — Failure modes are walked through, not just listed.** Before sign-off, the giver walks the receiver through the architecture and the known failure modes — what breaks, how it presents, which runbook answers it. The walkthrough is recorded in handover.md with its date and participants.
8. **PM-188 — The mandated set is fresh at transfer.** Every mandated file is present and within its freshness window (a project-policy parameter, per file tier) at the transfer date. A stale runbook or a kickoff-era progress.md is refreshed or flagged as a gap before sign-off, not discovered after.
9. **PM-189 — Open work transfers with owners.** Every blocked item, postmortem follow-up, and deferred fix open at transfer is listed with its current owner, its state, and what unblocks or completes it, so nothing open depends on the giver's memory after they leave.
10. **PM-190 — The cold run is the acceptance test.** Using only the handover materials, the receiving owner deploys the project, finds the runbook for a named incident class, names the top open risks, and states who accepted the transfer and when. Any failed step is a handover gap.
11. **PM-191 — Gaps block sign-off and are recorded.** A failed cold-run step, a missing mandated file, or an unlisted landmine is written into handover.md as a gap with an owner and a fix date. Sign-off waits until gaps are closed or the accepting owner explicitly accepts them in writing in handover.md.
12. **PM-192 — handover.md is maintained during the project.** It is updated as owners, risks, and systems change, and finalized at transfer. A handover.md authored from scratch on the exit day is a defect — it will carry the author's memory gaps as the project's record.

## BAN list

- **BAN-PM-091 — Secret values in handover materials.** Banned: pasting passwords, API keys, tokens, or recovery codes into handover.md, a transferred doc, or the transfer message. Defeats: DET-CON-003. Bad: handover.md's "Access" section lists the production database password and the Stripe secret key "so the new owner can log in right away." Instead: name the system, the vault or provider where the secret lives, and the grant procedure — the receiver is given access through that procedure, never the value in a document. Severity: BLOCK.
- **BAN-PM-092 — The link-and-cheer handover.** Banned: a transfer consisting of a repository link and an encouraging message, with no review, no walkthrough, and no acceptance. Defeats: DET-CON-028. Bad: the giver's last message is "Repo's all yours — good luck! 🚀" and handover.md does not exist. Instead: run the readiness review (PM-181), walk the failure modes (PM-187), and close with a recorded, dated acceptance (PM-183). Severity: BLOCK.
- **BAN-PM-093 — Landmines by omission.** Banned: a handover whose risks section is empty, absent, or "all good" while the project's own records — progress.md blockers, postmortem follow-ups, the issue tracker — name open risks. Defeats: DET-CON-014. Bad: handover.md says "No known issues" while a postmortem follow-up about the payment-retry defect is still open. Instead: build the landmines list from the project's records, each entry with evidence or a link; "none known" appears only as an explicit finding after that check. Severity: BLOCK.
- **BAN-PM-094 — The code-only transfer.** Banned: transferring the repository without the project memory — runbooks, postmortems, DECISIONS.md/ADRs, progress.md — while handover.md claims a complete transfer. Defeats: DET-CON-015. Bad: the receiver gets the code repo; the runbooks live in the giver's private notes and the decision rationale lives in a chat thread nobody exported. Instead: the memory set is a line item in the transfer manifest (PM-186) and the manifest gate (G-PM-091) fails until each item is present in the transferred repo. Severity: BLOCK.
- **BAN-PM-095 — The exit-day handover.** Banned: a handover.md written entirely at exit, presenting kickoff-era or from-memory content as the project's current state. Defeats: DET-CON-018. Bad: handover.md, dated the giver's last day, describes the launch architecture — two services have since been replaced and the on-call rotation it names no longer exists. Instead: maintain handover.md during the project (PM-192); at transfer, re-verify each section against the current repo and records, and date the verification. Severity: WARN.

## Gates

- **G-PM-091 — Mandated-file manifest and freshness check.** Verifies: PM-186, PM-188. Check: automated — a script diffs the repo's file list against the mandated set for the project type (the project-templates manifest) and asserts every memory-set item (runbooks, postmortems, DECISIONS.md, docs/adr/, progress.md, fact sheet, handover.md) is present; then for each file carrying a `last_reviewed` date or git-tracked mtime, asserts it falls within its freshness window (project-policy parameter). Pass: zero mandated files missing, zero outside their window unflagged. Fail: each miss or stale file is recorded as a handover gap (PM-191); sign-off is blocked. Recorded in: progress.md.
- **G-PM-092 — Secrets scan and credentials-path check.** Verifies: PM-185. Check: automated — grep the handover materials and transfer manifest for credential patterns (high-entropy strings, `password`, `secret`, `token`, `api_key` followed by a value, private-key headers); assert zero matches, and assert handover.md has a credentials-path section naming at least one system with its secret location and grant procedure. Pass: zero secret-value matches and the path section present. Fail: remove the value, rotate the exposed secret, and re-run; sign-off is blocked until clean. Recorded in: progress.md.
- **G-PM-093 — Acceptance record check.** Verifies: PM-182, PM-183. Check: automated — grep handover.md for the acceptance block: a named accepting owner (person or role), an ISO 8601 date, and the accepted scope. Pass: all three present and the date is the transfer date or later. Fail: no acceptance, no handover — the transfer stays open in progress.md. Recorded in: progress.md.
- **G-PM-094 — Landmines cross-check.** Verifies: PM-184, PM-189. Check: automated assist — extract open items from progress.md (blocked entries), postmortem follow-up actions not marked closed, and any open risks in the issue tracker export; diff against the landmines list in handover.md. Pass: every open item appears in the landmines list with evidence or a link, or is explicitly closed with a date. Fail: add the missing entries and re-run; an unexplained diff blocks sign-off. Recorded in: progress.md.
- **G-PM-095 — Cold-run acceptance test.** Verifies: PM-187, PM-190. Check: manual — the receiving owner, using only the handover materials and no help from the giver: (1) deploys or starts the project following the transferred docs, (2) finds the runbook for a named incident class, (3) names the top open risks from the landmines list, (4) states who accepted the transfer and on what date. Pass: 4 of 4 steps completed unaided. Fail: each failed step is recorded as a gap with an owner and fix date (PM-191); the cold run repeats after fixes before sign-off. Recorded in: progress.md.

## Anti-patterns

- **The component inventory.** handover.md lists what the system is made of — services, tables, pages — and nothing about how it fails, who owns it, or what is still open. Catch it: check the document against the four questions a receiver actually asks (how do I run it, what breaks, what is risky, who accepted it); an inventory answers none of them.
- **The verbal walkthrough.** The failure-mode walkthrough happened — in a call, unrecorded — so its content leaves with the giver. Catch it: handover.md must carry the walkthrough's date, participants, and the failure modes covered (PM-187); if it is not written there, it did not happen for handover purposes.
- **Acceptance by silence.** The giver sends the materials, hears nothing back, and marks the transfer complete. Catch it: the only acceptance that exists is the recorded one (PM-183); a transfer with no acceptance block is still open, however long the silence.
- **The clean-sheet risks section.** The landmines list is short and reassuring because it was written from the giver's impression, not from the project's records. Catch it: run the cross-check (G-PM-094); the list is built by diffing records, not by remembering.

## Examples

- [Example 1 — A link-and-cheer transfer corrected to a recorded acceptance](examples/example-1.md) — corrects PM-183.
- [Example 2 — Secrets pasted into handover.md, replaced by a credentials path](examples/example-2.md) — corrects PM-185.
- [Example 3 — "No known issues" replaced by an evidenced landmines list](examples/example-3.md) — corrects PM-184.

## Recall anchors

- No named accepting owner, no handover.
- Acceptance is recorded, dated, and scoped — or it did not happen.
- Landmines are listed with evidence; silence never means none.
- Credentials path, never credentials.
- The memory transfers with the code — and the cold run proves it.

## Checklist

- [ ] Readiness review run against the mandated set; manifest and freshness gate passes (G-PM-091).
- [ ] Landmines list built from the project's records, each entry with evidence or a link (PM-184, G-PM-094).
- [ ] Credentials path names every system, secret location, and grant procedure — and the secrets scan is clean (PM-185, G-PM-092).
- [ ] Failure-mode walkthrough held and recorded with date and participants (PM-187).
- [ ] Runbooks, postmortems, DECISIONS.md/ADRs, and progress.md are in the transfer manifest (PM-186).
- [ ] Cold run passed 4 of 4, or every failed step is recorded as a gap with an owner and fix date (G-PM-095, PM-191).
- [ ] Acceptance block present in handover.md: named owner, ISO date, accepted scope (PM-183, G-PM-093).
