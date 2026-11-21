# Example 3 — The committed `.env` and the quiet rotation

**Skill:** project-takeover
**Rules exercised:** DX-184 (access and ownership mapped; credentials only through the secret store), DX-188 (security audit precedes any change; a live secret is compromised), DX-189 (detection sweep recorded by ID), DX-190 (risk-map disposition), DX-191 (rotation is stabilization)
**Violations in the Before:** BAN-DX-093 (inherited secrets left live or passed around in the clear), BAN-DX-094 (first run pointed at production)
**Gates referenced:** G-DX-093 (security and detection sweep — zero unrotated live secrets)

**Scenario:** A support team inherits `helpdesk-lite`, a small internal ticketing app, from a contractor whose engagement has ended. The handover is a repo transfer, a shared-drive folder containing a handover document and an exported password spreadsheet, and the contractor's parting message in chat: "All the credentials you need are in the doc."

The inheriting engineer has not yet changed a single line of the running system — which, under DX-188, is exactly the right moment for the security audit.

---

## Before

The engineer starts by getting the app running. To save time, they copy the credentials from the handover document into a local `.env` — including the production database password and the production email-provider API key — and boot the app against the real production database "just to see it work" (BAN-DX-094). They run the seed-and-notify script the README mentions; it sends real notification emails to real ticket requesters from the production provider before anyone notices.

During a later read-through of the repo history, the engineer finds that a `.env` file containing the same production database password was committed two years ago and later "removed" in a follow-up commit. The team discusses it in chat — pasting the password into the thread so everyone can confirm it's "the same one" (BAN-DX-093) — and records a line in the takeover notes:

> "Old .env in git history with prod DB password — file was deleted in a later commit. Low risk now. Clean up later."

Nothing is rotated. The password stays valid for the entire takeover and afterwards, recoverable by anyone who ever clones the full history. The contractor's personal account — which still has admin access to the app and to the hosting account — is also never revoked, because the audit covered the code and never asked who else could log in. When the contractor's engagement formally ends, their access does not.

Three separate failures compound here: a live secret treated as closed because the *file* was deleted, credentials moved through chat and a spreadsheet instead of a secret store (DX-184), and a first local run wired to production data and a production sender (DX-192, BAN-DX-094).

## After

The same inheritance, with the DX-188 audit run before any change to the running system and before the first local run is pointed at anything real.

**Step 1 — Security audit and detection sweep (DX-188, DX-189, G-DX-093).**
Before the first stabilization change, the inheritor runs:

- A secret scan over the working tree **and the full version-control history** (`gitleaks detect --log-opts="--all"` or equivalent). It hits on the `.env` committed two years ago: production database password, still present in history despite the later deletion commit.
- The ecosystem dependency audit, with vulnerability findings routed per dependency-management.
- The auth surface review: roles in the app, any test/default accounts, and — reading the DX-184 access map alongside the audit — who holds admin access today. This surfaces the contractor's still-active personal admin account and personal deploy key, plus the password spreadsheet in the shared-drive folder.
- The DET sweep over code and infra (skills/detection/code/PARAMETERS.md, skills/detection/infra/PARAMETERS.md), with every hit entered in the audit by its DET ID and the file or configuration that triggered it. The committed secret is recorded against DET-INF-005; the production-configured local environment against DET-INF-003. Hits that do not meet the DX-191 stabilization bar are findings for the risk map, not a work list.

**Step 2 — Treat the found secret as compromised (DX-188).**
The finding is written up with the rule stated plainly: a live secret found anywhere — tree, history, CI logs, a handover document — is compromised. Deleting the file does not close it; the later deletion commit is irrelevant, because the secret remains in history and must be assumed copied. **Rotation is the closure.**

**Step 3 — Rotate as stabilization, transfer through the secret store (DX-191, DX-184).**
Each action below is its own labeled stabilization change, tied to a `stabilize-now` row in the risk map (DX-190):

1. The production database password is rotated. The new credential is issued directly into the project's secret store and deployed from there; it is never pasted into chat, email, a ticket, or a committed file.
2. The production email-provider API key found in the handover document is rotated the same way, because it was stored in a shared-drive document — exposure, not just age, is the trigger.
3. The contractor's personal admin account and personal deploy key are revoked — revoking a departed predecessor's live access is explicitly DX-191 stabilization.
4. The password spreadsheet is removed from the shared drive after its still-needed entries are re-issued through the secret store; the spreadsheet itself is recorded in the audit as a finding, not quietly kept "just in case."
5. History rewriting to purge the old `.env` is *not* done during takeover: it is disruptive, it does not un-compromise the rotated secret, and it is not needed once rotation has happened. It is dispositioned `schedule` in the risk map as a post-takeover decision — the rotation record, not the purge, is what G-DX-093 checks.

**Step 4 — First run, safely (DX-192, BAN-DX-094 avoided).**
Only after the audit does the inheritor boot the app locally — against a restored copy / anonymized fixture data and sandbox email credentials, never the production database or the production sender. The seed-and-notify script is run against the sandbox provider, where its output can be inspected without a single real customer being emailed. If production separation for any integration cannot be established, that itself becomes a `stabilize-now` finding rather than a risk the first run takes silently.

**Risk-map rows (DX-190).**

| Finding | Disposition |
|---|---|
| Production DB password in git history (DET-INF-005) | `stabilize-now` — closed by the rotation record, not by file deletion |
| Production email API key stored in handover document | `stabilize-now` — closed by rotation via the secret store |
| Contractor personal admin account + deploy key still active | `stabilize-now` — closed by revocation |
| Password spreadsheet in shared drive | `stabilize-now` — entries re-issued via secret store, spreadsheet removed |
| Old secret remains readable in pre-rotation history | `schedule` — optional history purge decided post-takeover; risk is neutralized by rotation |
| Remaining DET sweep hits below the stabilization bar | `register` — tech-debt register IDs recorded per row |

**Gate check (G-DX-093).** The gate passes only when all three sweeps have run, every hit is recorded by ID or scanner finding, and every live-secret hit shows a rotation record — zero unrotated live secrets. In the After, that check is mechanical: scan output, rotation records, revocation records, all in the audit.

**Difference:** in the Before, the team found the secret, discussed it in chat — spreading it further — and left it valid indefinitely because the file "was already deleted." In the After, the same discovery triggers the quiet, unglamorous sequence the skill prescribes: scan, record by ID, rotate, revoke, transfer through the secret store, and only then run the system — against copies, not production. Nothing about the app's behavior changed; that is precisely why it counts as stabilization under DX-191.
