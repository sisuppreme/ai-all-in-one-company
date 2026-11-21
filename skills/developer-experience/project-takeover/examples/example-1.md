# Example 1 — The first PR that did everything

**Skill:** project-takeover
**Rules exercised:** DX-181 (takeover mode declared, scope frozen), DX-183 (inherited state preserved), DX-185 (clean-clone run), DX-187 (as-found baseline), DX-190 (risk-map disposition), DX-191 (stabilization is minimal and separable)
**Violations in the Before:** BAN-DX-091 (work before the freeze lifts)
**Gates referenced:** G-DX-092 (clean-clone run and baseline), G-DX-095 (freeze and exit)

**Scenario:** A two-person team inherits `shopfront-api`, a Node service handed over by a departing contractor. The repo arrives as a Git remote plus a zip of loose files: an uncommitted `.env.staging`, a `notes.txt`, and a database dump. Production is live and taking orders. On the handover call the contractor mentions, in passing, "login is a bit flaky sometimes."

---

## Before

Day one, 09:40, the inheriting developer clones the repo, cannot get it to boot, and starts "fixing" whatever is in front of them — in the working tree, with no record of what was there first:

1. The uncommitted changes already sitting in the contractor's exported working copy are discarded with a clean checkout because "they looked like experiments." Nobody recorded the starting commit hash or the `git status` output, so there is no way to reconstruct the inherited state (breaks DX-183).
2. The boot failure is traced to a missing environment variable. Instead of logging it as a finding, the developer renames the variable, rewrites the config loader, and commits it.
3. Remembering the "flaky login" remark, the developer fixes the login bug, bumps the web framework two major versions "while I'm in here," and renames the `services/` module to `domain/` because the old name was "confusing."
4. All of this lands as one pull request: `fix: get it running and tidy up`. It is merged on day two and deployed that evening.

That night the order-confirmation flow breaks in production. The team cannot answer the basic takeover questions:

- Was the flow already broken as inherited, or did one of today's changes break it? There is no DX-187 baseline — no build result, no test counts, no smoke pass recorded before the first edit — so the argument is settled by opinion.
- Which hunk caused it: the config rewrite, the framework bump, or the module rename? They are inseparable in one PR, so the only safe rollback is "everything," which also rolls back the boot fix.
- What did the project look like as inherited? Unrecoverable — the discarded uncommitted changes and the pre-edit tree are gone.

This is exactly BAN-DX-091: feature work, cleanup, and an upgrade performed between inheritance and exit, mixed into a single change. It also fails G-DX-095 on inspection: `git log` since the handover contains changes that map to no `stabilize-now` risk-map row, because there is no risk map.

## After

The same inheritance, run under this skill:

**Day one, morning — declare and preserve (DX-181, DX-183).**
`progress.md` gets a dated declaration: project `shopfront-api`, inherited from the contractor, starting commit recorded by hash, plus the captured `git status` output. The uncommitted changes in the exported copy are preserved as a patch file and a snapshot branch — not judged, not discarded. The loose `.env.staging`, `notes.txt`, and dump are listed in the inventory as non-versioned material, marked `unknown` until inspected (DX-182). From this moment the scope is frozen: inventory, local run, audit, risk mapping, and DX-191 stabilization only.

**Day one, afternoon — inventory and clean-clone run (DX-182, DX-185).**
The developer clones fresh into a clean container with none of the contractor's local state and follows only the README. The boot fails at the same missing environment variable. That failure is logged verbatim as a takeover finding — "setup step missing from README: service will not start without `SESSION_STORE_URL`, which is documented nowhere" — not silently fixed by redesigning config.

**Day two — as-found baseline (DX-187, G-DX-092).**
Once the app runs locally against fixture data, the baseline is recorded exactly as found: build result, full test-suite pass/fail counts as they actually are (including the pre-existing failures, preserved with their output and explicitly *not* fixed during baselining), and a smoke pass over the primary flows — browse, add to cart, checkout, order confirmation. The order-confirmation smoke step passes as inherited. That single record later settles any "was it already broken?" argument.

**Risk-map dispositions (DX-190).** Each finding gets one row, an owner, and exactly one disposition:

| Finding | Disposition |
|---|---|
| Boot requires undocumented `SESSION_STORE_URL`; README step missing | `stabilize-now` — restoring a missing pin/instruction so the as-found code runs is DX-191 stabilization |
| Flaky login reported by contractor, not yet reproduced | `register` — entered in the tech-debt register, register ID recorded in the row; reproducing it is part of inventory, fixing it is not stabilization |
| Framework two majors behind current | `schedule` — follow-on work for dependency-management, with a named trigger (after takeover exit) |
| `services/` naming is confusing | `schedule` — follow-on work for refactoring, post-exit only |

**The only PR in takeover mode (DX-191).**
One small, separately labeled commit — `takeover stabilization: document and default SESSION_STORE_URL for local run` — tied to the single `stabilize-now` row and judged against the DX-187 baseline: same test counts, same smoke results, app now boots from the repo's own instructions. No login fix, no framework bump, no rename in the branch.

**Exit (G-DX-095).**
Auditing every commit since the declaration shows exactly one change, labeled stabilization and mapped to its risk-map row. The takeover report is signed, and the login bug, the upgrade, and the rename leave takeover as dispositioned findings for their owning skills — to be done after exit, one at a time, against a known-good baseline.

**Difference:** in the Before, day two ends with a broken production flow and no evidence. In the After, day two ends with a preserved inheritance, a recorded baseline, a risk map, and one separable stabilization change — and if order confirmation ever breaks later, the baseline proves what changed and when.
