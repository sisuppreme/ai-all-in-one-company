# incident-response

## Metadata

- **Owner department:** D6 DevOps & Deployment (DO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://docs.pagerduty.com/ops-guides/incident-response-guide/different-roles ; https://sre.google/sre-book/managing-incidents/
- **Depends on:** alerting, monitoring, rollback
- **Feeds into:** postmortem-writing, reliability, status-communications

## When to use / Do NOT use

- **Use when:** Setting up or auditing how a production service responds to outages and major failures — on-call rotation, severity levels, incident command, runbooks, user communication, and postmortems.
- **Do NOT use when:** Defining the alerts and dashboards that detect failure — that is alerting and monitoring. Executing the technical act of reverting a release — that is rollback; this skill decides when to call it and who coordinates.

## Rules

1. **DO-281 — A named on-call rotation exists, with at least two escalation levels.** The current week's primary and escalation responders are named people in the paging tool or a committed rotation file — never "the team" — and any responder can state who is on call right now without asking. In single-operator mode (DO-293), the two levels read as a named primary plus a named escalation contact.
2. **DO-282 — Severity levels and declaration rights are written down before the first incident.** The document defines each severity by user impact, states who may declare an incident at each level, and names the response each level triggers; nobody negotiates definitions during an outage.
3. **DO-283 — Every major incident has exactly one Incident Commander.** The IC coordinates, assigns all repair work to named responders, and owns the communication cadence; the IC does not personally fix anything while commanding. (Single-operator mode sequences the two roles in one person instead — DO-293.)
4. **DO-284 — A scribe keeps the timeline from declaration.** From the moment an incident is declared, the scribe records timestamped events — detection, declaration, decisions, mitigations, resolution — in the incident record, not from memory afterward. (In single-operator mode the operator keeps the timeline — DO-293.)
5. **DO-285 — The runbook covers the top failure modes with exact commands.** Each entry names the symptom, the exact commands or console steps to mitigate, and the escalation trigger; the runbook lives at a recorded path the on-call can open at 3 a.m. — a chat thread is not a runbook.
6. **DO-286 — Mitigate first, diagnose second.** Under outage pressure the default first move is rollback, restore, or failover to a known-good state; root-cause debugging happens after service is restored, unless mitigation is demonstrably impossible and the IC records why.
7. **DO-287 — One voice speaks for the incident.** All status updates come from the IC or a named liaison, on a cadence stated in the first update, and the cadence is kept even when the update is "still investigating."
8. **DO-288 — The user-facing channel is prepared before it is needed.** A status page or equivalent comms channel exists, is linked from the product, and has a pre-written first-update template; for a major incident the first user-facing update goes out within the time the severity definition states.
9. **DO-289 — Every significant incident closes with a blameless postmortem.** The postmortem contains the timeline, the root cause stated as a system property, and follow-up actions each with an owner and a due date; it names no person as a cause.
10. **DO-290 — Postmortem actions are tracked to completion like features.** Each action lives in the same tracker as product work, with its owner and due date visible, and overdue actions surface in the regular review until closed.
11. **DO-291 — The paging path is proven, not assumed.** Alerts for downtime and SLO burn route to the current rotation, and a test alert is fired and acknowledged by the named responder on a regular cadence and after every rotation or tooling change.
12. **DO-292 — The process is rehearsed.** A game day or tabletop drill runs the declaration, command, communication, and postmortem steps on a stated cadence, and the drill's gaps are filed as follow-up actions under DO-290.
13. **DO-293 — Single-operator mode is a named variant, never a silent deletion.** Where one operator runs the service, the rotation is the named operator as primary plus the project owner or user as the escalation contact (level 2). The operator acts as Incident Commander and fixer in sequence — declare, then mitigate, then communicate — and keeps the timeline contemporaneously in the incident record in place of a separate scribe, so DO-284 is satisfied by the operator's own timestamped entries. Every other rule in this skill applies unchanged; the multi-person form above remains the general case wherever more than one responder exists.

## BAN list

- **BAN-DO-141 — "Contact the developer" as the response path.** Banned: the only documented response to an outage is a person's name, a chat handle, or "contact the developer if something breaks." Defeats: DET-INF-029. Bad: the README's operations section reads "If the site goes down, message Alex." Instead: publish a rotation with at least two escalation levels — in single-operator mode (DO-293), a named primary plus a named escalation contact — and a runbook, so the response survives any one person being unreachable. Severity: BLOCK.
- **BAN-DO-142 — Alerts that reach nobody.** Banned: alert rules fire into an unmonitored channel, a departed member's inbox, or a dashboard nobody opens, with no named on-call owner. Defeats: DET-INF-012. Bad: downtime alerts post to a Slack channel muted by the whole team, and the last test alert was never acknowledged. Instead: route alerts to the paging tool against the named rotation and prove receipt with a test alert. Severity: BLOCK.
- **BAN-DO-143 — Users learn from social media.** Banned: no status page or comms channel exists, so users discover outages from complaints and rumors while the team stays silent. Defeats: DET-INF-028. Bad: during a two-hour outage the product, help center, and social accounts say nothing; users announce the outage first. Instead: prepare the status channel and first-update template in advance and post on the stated cadence from declaration. Severity: WARN.
- **BAN-DO-144 — Debugging forward while a rollback sits unused.** Banned: responders spend the outage hunting root cause in production while a tested rollback or restore path exists and is not executed. Defeats: DET-INF-017. Bad: ninety minutes of live log-diving during a full outage, then the rollback that fixed it in four minutes. Instead: the IC orders mitigation first (rollback, restore, failover) and diagnosis moves to after service is restored. Severity: BLOCK.
- **BAN-DO-145 — A person named as root cause.** Banned: a postmortem that attributes the incident to an individual's mistake, or no postmortem at all for a significant incident. Defeats: DET-INF-029. Bad: the review concludes "root cause: Sam deployed a bad config" and closes with no system change. Instead: state the root cause as the system property that let one action cause an outage, and file tracked follow-ups with owners and dates. Severity: WARN.

## Gates

- **G-DO-141 — On-call inspection (automated).** Verifies: DO-281, DO-282, DO-293. Check: query the paging tool's API (or parse the committed rotation file) for the current week and confirm a named primary plus at least one escalation level, and confirm the severity/declaration document exists at its recorded path. Pass: a named primary plus at least one named escalation level for the current week — in single-operator mode, a named primary plus a named escalation contact (DO-293) — and the severity document present. Fail: block shipment — the service has no response path. Recorded in: progress.md.
- **G-DO-142 — Paging-path test (automated).** Verifies: DO-291. Check: fire a test alert through the production alert route and confirm the currently named primary acknowledges it within the response time the severity definition states; log the drill timestamp. Pass: acknowledged in time by the named responder. Fail: block shipment until the route is fixed and the test passes. Recorded in: progress.md.
- **G-DO-143 — Runbook coverage scan (automated).** Verifies: DO-285. Check: open the runbook at its recorded path; for each of the top failure modes confirm an entry containing a symptom and at least one exact command or console step; `grep -in "tbd\|todo\|someone should" <runbook>` returns no hits. Pass: every top failure mode has an actionable entry and no placeholder text. Fail: warn, and complete the runbook before the next release. Recorded in: progress.md.
- **G-DO-144 — Last-incident audit (manual).** Verifies: DO-283, DO-284, DO-289, DO-290. Check: open the most recent significant incident's record; it must name the IC, contain a timestamped timeline kept during the incident, and link a postmortem whose every follow-up action has an owner and a due date in the work tracker. Pass: all four elements present. Fail: warn, and complete the record before the next incident review. Recorded in: progress.md.
- **G-DO-145 — Status-channel readiness check (manual).** Verifies: DO-287, DO-288. Check: open the status page or comms channel from the product's public links; confirm it exists, that a first-update template is stored with it, and that the last drill or real incident posted its first update within the stated time. Pass: channel reachable, template present, first-update time on record. Fail: warn, and prepare the channel before the next major release. Recorded in: progress.md.

## Anti-patterns

- **War-room sprawl.** Five responders post competing updates across three chat channels and nobody can say what the current state is; catch it by asking who the IC is — if two people answer, there is none.
- **Timeline from memory.** The incident record is written two days later from scrollback and recollection, with times rounded and decisions missing; catch it by comparing the record's timestamps against the alert log.
- **Postmortem as paperwork.** The review is written, applauded, and filed while its actions quietly expire unowned; catch it by listing postmortem actions older than their due dates at the regular review.
- **Everything is SEV-1, or nothing is.** Severities are declared by adrenaline instead of the written user-impact definitions, so escalation either always fires or never does; catch it by sampling past incidents against the definitions.

## Examples

- [Example 1 — Declaring and commanding an incident](examples/example-1.md) — violates/corrects DO-282, DO-283.
- [Example 2 — Mitigate first at 3 a.m.](examples/example-2.md) — violates/corrects DO-285, DO-286.
- [Example 3 — A blameless postmortem with tracked actions](examples/example-3.md) — violates/corrects DO-289, DO-290.

## Recall anchors

- Mitigate first, diagnose second — rollback beats log-diving under outage pressure.
- One incident, one commander, one voice.
- If the timeline is written from memory, it is fiction.
- A chat message is not a runbook.
- Postmortems blame systems; actions have owners and dates.

## Checklist

- [ ] Current week's rotation names a primary and at least one escalation level (DO-281).
- [ ] Severity levels and who may declare are written and linked from the runbook (DO-282).
- [ ] The last major incident record names one IC and a scribe-kept timeline (DO-283, DO-284).
- [ ] Runbook covers the top failure modes with exact commands and no placeholder text (DO-285).
- [ ] A test alert was acknowledged by the named primary within the stated response time (DO-291).
- [ ] Status channel exists, is linked from the product, and holds a first-update template (DO-288).
- [ ] The last postmortem is blameless and every action has an owner and due date in the tracker (DO-289, DO-290).
- [ ] The last drill or game day is dated, and its gaps are filed as tracked actions (DO-292).
