# threat-modelling

## Metadata

- **Owner department:** D7 Security (SE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html ; https://owasp.org/www-project-threat-dragon/
- **Depends on:** owasp
- **Feeds into:** security-audit, penetration-testing

## When to use / Do NOT use

- **Use when:** Designing any major feature before code is written — always when the feature touches authentication, payments, personal data, file upload, or admin capability; also when an existing feature's data flow or trust boundaries change.
- **Do NOT use when:** The task is finding flaws in already-built code (use security-audit or penetration-testing instead), or the change cannot move data across a trust boundary and touches no asset (a copy edit, a static style change).

## Rules

1. **SE-181 — Model before build.** A feature that touches auth, payments, personal data, file upload, or admin capability has a written threat model in `docs/threat-models/<feature>.md` before implementation starts; no model, no build.
2. **SE-182 — Diagram first.** The model opens with a data-flow diagram (Threat Dragon or equivalent) naming every process, data store, external actor, data flow, and trust boundary; an element not on the diagram is out of scope for the model and must be added or explicitly excluded.
3. **SE-183 — List the assets.** The model names the assets an attacker wants: credentials, personal data, money movement, admin capability, and any tenant data — each with the store or flow where it lives.
4. **SE-184 — Enumerate with STRIDE per element.** Threats are enumerated element by element using STRIDE (or a named equivalent); a single free-form brainstorm list does not satisfy this rule.
5. **SE-185 — Every crossing gets a threat and a control.** Each trust-boundary crossing on the diagram has at least one named threat and at least one named control; a crossing with neither blocks the design review.
6. **SE-186 — Abuse cases beside use cases.** Every use case that reads or mutates data carries a paired abuse case in the attacker's voice (e.g., "user views another tenant's invoice by changing an ID"), written in the model next to the use case.
7. **SE-187 — Disposition per threat.** Every enumerated threat ends in exactly one disposition: a control to build, a test to write, or a written risk acceptance; threats left "noted" with no disposition are unfinished work.
8. **SE-188 — Acceptances expire.** Each risk acceptance names an owner and a review/expiry date; an undated or unowned acceptance counts as an open threat, and an expired acceptance reopens automatically.
9. **SE-189 — Outputs become work items.** The model emits concrete outputs before build starts: the ASVS requirements selected for the feature, the authorization/abuse tests to write, and the DET parameters to re-check after implementation.
10. **SE-190 — The model is a living file.** The model carries a "Last reviewed" date inside the current work cycle and is updated in the same change that alters the feature's data flow, boundaries, or assets.
11. **SE-191 — Traceability is checkable.** Each threat ID in the model resolves to a control location (file/config), a test name, or an acceptance entry — a reviewer can follow any threat ID to its disposition in under a minute.
12. **SE-192 — Cross-tenant and privilege threats are mandatory.** Multi-tenant or role-bearing features always enumerate elevation-of-privilege and cross-tenant access threats, even when "users are trusted"; trusted-user assumptions are recorded as acceptances under SE-188, never silently assumed.

## BAN list

- **BAN-SE-091 — Unexamined admin surface.** Banned: designing an admin or debug capability with no abuse case and no authorization threat in the model. Defeats: DET-INF-021. Bad: an `/admin/impersonate` endpoint designed as "internal only, link not shown in UI". Instead: model the stolen-session and curious-insider abuse cases and require a server-side role control plus an audit-log entry per use. Severity: BLOCK.
- **BAN-SE-092 — Client-side control.** Banned: naming a client-side check (hidden button, disabled field, client validation) as the control for an enumerated threat. Defeats: DET-CODE-027. Bad: "Threat: user submits a negative quantity. Control: the form's `min=0` attribute." Instead: enforce the rule server-side and write the abuse test against the raw API request. Severity: BLOCK.
- **BAN-SE-093 — Orphan risk acceptance.** Banned: a risk acceptance with no owner and no expiry/review date. Defeats: DET-CODE-031. Bad: "Risk accepted: session tokens in localStorage." — no name, no date, filed once and forgotten. Instead: record owner, date, compensating control, and expiry; on expiry the threat reopens (SE-188). Severity: BLOCK.
- **BAN-SE-094 — Boilerplate model.** Banned: a copied generic STRIDE checklist whose threats name no element of this feature's actual diagram. Defeats: DET-CODE-024. Bad: "Spoofing: attackers may spoof identity" pasted identically into five feature models. Instead: write each threat against a named element and flow ("attacker replays the reset token at flow F3 before expiry"). Severity: WARN.
- **BAN-SE-095 — Authenticated means authorized.** Banned: closing an authorization threat with "the user is logged in" as the control. Defeats: DET-CODE-020. Bad: "Threat: user reads another tenant's invoice. Control: route requires login." Instead: require a per-object ownership check on the server and an abuse test that swaps the object ID (SE-186). Severity: BLOCK.

## Gates

- **G-SE-091 — Model presence and freshness (automated).** Verifies: SE-181, SE-190. Check: `test -f docs/threat-models/<feature>.md && grep -E "Last reviewed: $(date +%Y-%m)" docs/threat-models/<feature>.md`. Pass: file exists and its review date falls in the current month. Fail: block the build. Recorded in: progress.md.
- **G-SE-092 — Boundary coverage count (automated).** Verifies: SE-185. Check: `grep -c "^| C[0-9]" docs/threat-models/<feature>.md` (crossing rows) equals `grep -c "Control:" docs/threat-models/<feature>.md` entries mapped to crossings, and no crossing row has an empty Threat or Control cell. Pass: counts match, no empty cells. Fail: block the design review. Recorded in: progress.md.
- **G-SE-093 — Traceability spot-check (manual).** Verifies: SE-187, SE-191. Check: pick any three threat IDs at random; for each, open the named control in code/config or run the named test. Pass: all three resolve within a minute each. Fail: block shipment until the model traces cleanly. Recorded in: progress.md.
- **G-SE-094 — Acceptance hygiene scan (automated).** Verifies: SE-188. Check: `grep -c "Risk acceptance" docs/threat-models/<feature>.md` equals `grep -c "Expires:" docs/threat-models/<feature>.md`, and every acceptance also matches `grep "Owner:"`. Pass: every acceptance has an owner and an unexpired date. Fail: block shipment; expired acceptances reopen as threats. Recorded in: progress.md.

## Anti-patterns

- **Scanner substitution.** Running SAST/DAST and calling it threat modeling; scanners find code flaws, never the design flaw where the code does exactly what was designed (A06 Insecure Design). Catch it: if the "model" contains no diagram and no abuse cases, it is a scan report.
- **Severity flattening.** Rating every threat "critical" (nothing gets prioritized) or every threat "low" (nothing gets fixed). Catch it: if the model has no spread of dispositions — controls, tests, and acceptances — the ratings were not honestly assigned.
- **Kickoff fossil.** The model was written once at project start and never touched while the feature gained a webhook, an export, and an admin role. Catch it: compare the diagram's flows against the current route list; any route not on the diagram is an unmodeled flow.
- **Happy-path cast.** The only attacker in the model is an anonymous outsider; no insider, no authenticated abuser, no curious tenant. Catch it: if no abuse case starts from a logged-in account, the cast is incomplete (SE-192).

## Examples

- [Example 1 — No model, then a model](examples/example-1.md) — violates/corrects SE-181, SE-185.
- [Example 2 — Use case without an abuse case](examples/example-2.md) — violates/corrects SE-186.
- [Example 3 — Orphan risk acceptance](examples/example-3.md) — violates/corrects SE-188.

## Recall anchors

- No model, no build — for anything touching auth, money, data, uploads, or admin.
- Every boundary crossing: one threat, one control, or the design does not pass.
- Abuse case next to every use case, in the attacker's voice.
- Control, test, or acceptance — a threat with none of the three is unfinished.
- An acceptance without an owner and a date is an open threat.

## Checklist

- [ ] Threat model file exists for the feature and its "Last reviewed" date is in the current work cycle (SE-181, SE-190).
- [ ] Data-flow diagram names every process, store, actor, flow, and trust boundary (SE-182).
- [ ] Assets are listed with the store or flow where each lives (SE-183).
- [ ] Threats enumerated with STRIDE per element, not a free-form list (SE-184).
- [ ] Every trust-boundary crossing has a named threat and a named control (SE-185).
- [ ] Each data-reading or data-mutating use case has a paired abuse case (SE-186).
- [ ] Every threat has a disposition: control, test, or acceptance (SE-187, SE-191).
- [ ] Every risk acceptance names an owner and an unexpired review date (SE-188).
