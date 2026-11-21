# status-communications

## Metadata

- **Owner department:** D18 Customer Experience (CX)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://support.atlassian.com/statuspage/docs/incident-communication-tips/ ; https://www.atlassian.com/incident-management/incident-communication
- **Depends on:** monitoring, alerting
- **Feeds into:** support-ticketing, help-center

## When to use / Do NOT use

- **Use when:** setting up or auditing a public status page; writing or reviewing incident posts, update cadence, maintenance announcements, resolution posts, and postmortems; running the incident-communication drill.
- **Do NOT use when:** the work is detecting or fixing the outage itself (use monitoring, alerting, and incident-response runbooks — this skill owns only what customers are told), one-to-one replies to affected users (use support-ticketing), or internal incident discussion, which never goes on the public page.

## Rules

1. **CX-161 — Components are customer-facing capabilities.** The public status page lists only the capabilities customers use — sign-in, dashboard, API, checkout — never internal services, hostnames, or vendor names.
2. **CX-162 — A named owner posts during every incident.** One named role owns status posting for each incident, with a named fallback. An incident with no posting owner is a process defect found in the drill (G-CX-082), not during a real outage.
3. **CX-163 — First post on confirmed impact, not on found cause.** When customer impact is confirmed, the first public post goes out within the operator's stated target time. Waiting for a root cause before posting anything is a rule violation, however fast the diagnosis is.
4. **CX-164 — First post carries three facts.** The first post states what is known (the impact, in customer terms), what is not yet known, and the time the next update will arrive. A post missing any of the three is incomplete.
5. **CX-165 — One consistent state sequence.** Incidents move through Investigating → Identified → Monitoring → Resolved, in that order. A state is never skipped silently and never moves backward without an update explaining why.
6. **CX-166 — The stated cadence is kept.** Every update names when the next update will arrive, and that time is kept; if nothing has changed by then, the update says so and names a new time. The cadence is an operator-set configuration value the operator can actually staff — a solo operator sets a longer honest cadence rather than copying a two-person team's.
7. **CX-167 — The page reflects measured reality.** Displayed component states come from the monitoring source or the incident owner's posts. No component is shown as operational while its monitor is failing or an open incident covers it; manually overriding a state to operational during an outage is forbidden.
8. **CX-168 — Subscribers are notified at every transition.** Opening, each state change, and resolution notify subscribers, and the current status is embedded where customers already look — the app and the help center — not only on a page they must remember to visit.
9. **CX-169 — Maintenance is announced in advance.** Scheduled maintenance is posted before its window starts, naming the affected components, the start and end times with timezone, and the expected customer impact. Unannounced planned downtime is treated as an incident.
10. **CX-170 — Resolution posts state cause and duration honestly.** The resolution post names the affected components, the total duration from first impact to resolution, and the cause at the level it is actually established — "cause under investigation" if it is not yet known, never a guessed cause stated as fact.
11. **CX-171 — Major incidents end with a postmortem.** Every major incident gets a public postmortem summary within the operator's stated window, linked from the incident: timeline, cause, impact, and what changes to prevent recurrence. The incident is not fully closed until the postmortem is published or the window is publicly extended.
12. **CX-172 — Templates exist before they are needed.** Pre-written templates for the common incident shapes, maintenance, and a holding update ("impact confirmed, cause not yet known, next update at …") are stored with the status configuration. A solo operator's degraded mode — holding template plus the longer honest cadence of CX-166 — is configured in advance, not improvised mid-incident.

## BAN list

- **BAN-CX-081 — All-operational during an outage.** Banned: the status page showing "All systems operational" while a known outage or degradation is in progress. Defeats: DET-CON-015. Bad: checkout has been failing for 40 minutes and support has confirmed it, while the status page still reads "All systems operational" because nobody updated it. Instead: the posting owner opens an incident on confirmed impact and the affected component shows its real state (CX-163, CX-167). Severity: BLOCK.
- **BAN-CX-082 — Silence until root cause.** Banned: withholding any public post until the cause is diagnosed, while customer impact continues. Defeats: DET-CON-028. Bad: the team posts nothing for two hours "until we know what happened," then publishes a single post-mortem-style entry after the fix. Instead: post early with impact, unknowns, and the next update time (CX-163, CX-164). Severity: BLOCK.
- **BAN-CX-083 — Invented cause or fix time.** Banned: stating a root cause, a culprit, or a restoration time in a public post before it is established. Defeats: DET-CON-014. Bad: the first update announces "a database failure, expected fix within 30 minutes" when neither the component nor any fix time is known. Instead: state what is known, label the rest as not yet known, and commit only to the next update time (CX-164). Severity: BLOCK.
- **BAN-CX-084 — Uptime figure with no measurement.** Banned: displaying an uptime percentage or availability claim that no monitoring history produces. Defeats: DET-CON-011. Bad: the status page header shows "99.99% uptime over the last 90 days" on a page created last week with no monitor data behind it. Instead: show only figures the monitoring source computes from real history, or show no figure (CX-167). Severity: BLOCK.
- **BAN-CX-085 — Internal detail on the public page.** Banned: public posts naming internal hostnames, internal service names, IP addresses, or a vendor as the blamed culprit. Defeats: DET-CON-004. Bad: "Our payments worker on ip-10-0-3-17 is down; waiting on our hosting vendor again." Instead: describe the customer-facing capability and its impact — "Payments: customers cannot complete checkout" (CX-161). Severity: BLOCK.

## Gates

- **G-CX-081 — Status-page truthfulness check.** Verifies: CX-167, CX-161. Check (automated): fetch the monitoring source's current component states and the status page's displayed states (status tool API or rendered page) and diff them; also grep the public page for internal hostnames and vendor names from the internal inventory list. Pass: every displayed state matches its monitor or an open incident covering it, no component shows operational while its monitor fails, and no internal name appears. Fail: block shipment; during a live incident, correct the page immediately and record the gap. Recorded in: progress.md.
- **G-CX-082 — Incident-posting drill.** Verifies: CX-162, CX-163, CX-164, CX-166, CX-168. Check (automated): via the status tool's API, create a test incident and assert from timestamps and dispatch logs: the first post lands within the operator's stated target and contains impact, unknowns, and a next-update time; a subscriber notification is dispatched; the in-app/help-center embed reflects the incident; a cadence update posts at the promised time. Pass: every assertion true with the named owner and fallback both exercised across drills. Fail: block launch of the status page until the drill passes. Recorded in: progress.md.
- **G-CX-083 — Template inventory check.** Verifies: CX-172, CX-169. Check (automated): list the status configuration's stored templates and assert one exists for each of: service outage, degraded performance, maintenance announcement, holding update, and resolution. Pass: all five templates present and using the state names of CX-165. Fail: block launch until the missing templates are written. Recorded in: progress.md.
- **G-CX-084 — Resolution and postmortem audit.** Verifies: CX-170, CX-171. Check (automated): query the status tool for all incidents resolved in the last 90 days; assert every resolution post states affected components and a duration, and every major incident has a linked postmortem or a publicly posted extension. Pass: zero incidents missing a required element. Fail: publish the missing postmortem or extension before the next release. Recorded in: progress.md.
- **G-CX-085 — Maintenance announcement check.** Verifies: CX-169. Check (automated): for every scheduled maintenance window in the next 30 days, assert a public announcement exists whose posting time precedes the window start and which names affected components, times with timezone, and expected impact. Pass: every upcoming window announced. Fail: post the announcement before the window opens; if the window has already started, treat it as an incident under CX-163. Recorded in: progress.md.

## Anti-patterns

- **The vague reassurance.** Updates that say "we're working on it" with no impact statement, no state change, and no next-update time — motion without information. Catch it by reading each draft update against CX-164's three facts before posting.
- **The single marathon post.** One incident entry edited silently for hours instead of discrete, timestamped updates, so subscribers get no notifications and the timeline is unrecoverable. Catch it by checking that each cadence point is its own post (CX-166, CX-168).
- **Resolved-and-vanished.** The incident flips to Resolved and the page returns to green with no cause, no duration, and no postmortem — the outage effectively erased. Catch it in the G-CX-084 audit and in review of every major incident.
- **Maintenance as a surprise.** Planned downtime announced in a post timestamped after the window began, or only in a channel customers do not watch. Catch it by running G-CX-085 on a schedule, not when someone remembers.

## Examples

- [Example 1 — Green page, broken checkout](examples/example-1.md) — violates/corrects CX-167, CX-163 (BAN-CX-081).
- [Example 2 — Waiting for the root cause](examples/example-2.md) — violates/corrects CX-163, CX-164 (BAN-CX-082).
- [Example 3 — "Issue fixed," nothing more](examples/example-3.md) — violates/corrects CX-170, CX-171 (BAN-CX-083).

## Recall anchors

- Post on impact, not on diagnosis.
- Known, not known, next update — every post, every time.
- The page shows measured reality or it shows nothing.
- Cadence is a promise: keep it or post why not.
- Resolution states cause and duration, or says the cause is still unknown.

## Checklist

- [ ] Components are customer-facing capabilities only, no internal names anywhere on the page (CX-161, G-CX-081).
- [ ] Posting owner and fallback are named, and the drill has exercised both (CX-162, G-CX-082).
- [ ] First-post target and update cadence are set to values the operator can actually staff (CX-163, CX-166).
- [ ] First post and every update carry known / not known / next update time (CX-164, CX-166).
- [ ] Displayed states match the monitoring source; no operational override during an outage (CX-167, G-CX-081).
- [ ] Subscriber notifications and the app/help-center embed fire at every transition (CX-168, G-CX-082).
- [ ] Templates for outage, degradation, maintenance, holding, and resolution are stored (CX-172, G-CX-083).
- [ ] Resolution posts state cause and duration; major incidents have linked postmortems (CX-170, CX-171, G-CX-084).
