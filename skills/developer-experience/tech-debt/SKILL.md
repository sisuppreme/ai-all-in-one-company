# tech-debt

## Metadata

- **Owner department:** D15 Developer Experience (DX)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://learningloop.io/glossary/technical-debt ; https://martinfowler.com/articles/workflowsOfRefactoring/fallback.html ; https://martinfowler.com/articles/feature-toggles.html
- **Depends on:** none — standalone: the debt register is built from shortcuts, workarounds, and TODO/FIXME markers found in the project's own codebase, inspected directly; it records debt rather than consuming another skill's output. It feeds refactoring and legacy-migration.
- **Feeds into:** refactoring, legacy-migration

## When to use / Do NOT use

- **Use when:** a shortcut, workaround, duplication, or stale toggle is being introduced or discovered; TODO/FIXME markers exist in the codebase; a release or iteration plan is being drawn up and repayment capacity must be allocated; the debt register is due its review.
- **Do NOT use when:** the work is the repayment itself (use refactoring for behavior-preserving cleanup, legacy-migration for replacing a system in slices), or the item is a defect in current behavior rather than a known shortcut (track it as a bug, not debt).
- **Cross-reference:** the commented-out-code pattern banned here as BAN-DX-042 is also banned at refactor time in refactoring (BAN-DX-054); the two entries cover the same pattern in different moments.

## Rules

1. **DX-081 — One register, one record.** Every known item of technical debt is a numbered entry (DEBT-NNN) in the project's single debt register, `docs/tech-debt.md`. Debt known only from chat, memory, or code comments is not recorded debt — it is invisible debt, and invisible debt is never scheduled.
2. **DX-082 — Complete fields at birth.** Every entry carries, from the moment it is created: location (file/module), Fowler quadrant (deliberate/inadvertent × prudent/reckless), the interest it charges, a named owner, a repayment trigger (a date, or the next feature/release touching that area), and the date incurred. An entry missing any field is incomplete and fails G-DX-042.
3. **DX-083 — Deliberate debt is registered in the same change that incurs it.** A shortcut taken on purpose gets its register entry in the same pull request that merges the shortcut. Registering it "later" is how deliberate debt becomes inadvertent.
4. **DX-084 — Deliberate + reckless is not a permitted category.** A shortcut with no repayment trigger and no plan is not debt, it is an unmade decision: the review blocks it, or the scope is cut until the work can be done properly.
5. **DX-085 — Interest is stated concretely.** The interest field names the work the debt slows or the risk it creates, in observable terms ("every billing change requires the same edit in three duplicated places"). "Code is messy," "needs cleanup," and similar phrases are not interest statements and are rejected at review.
6. **DX-086 — Code markers must reference the register.** Every `TODO`, `FIXME`, `HACK`, or `XXX` comment carries a register reference, e.g. `TODO(DEBT-123): …`. A marker with no reference is either fixed in place, converted into a register entry with a reference, or deleted in the same change that touches it. Core functionality is never deferred to a marker — a marker may only defer minor, already-working-around items.
7. **DX-087 — Temporary means an expiry.** Every workaround and hack carries its repayment trigger as its expiry. When a trigger fires (the date passes, or work touches the area), repayment is scheduled into the next plan — the trigger firing is the scheduling event, not a reminder to update the date.
8. **DX-088 — Inadvertent debt is logged as a defect to schedule.** Debt discovered while reading or changing code (reckless shortcuts, rotted patterns, undocumented workarounds) is entered in the register the day it is found, classified inadvertent, and scheduled like a defect. It is neither silently fixed opportunistically inside an unrelated change nor noted and forgotten.
9. **DX-089 — Repayment is a standing capacity slice.** Each iteration or release plan reserves a stated slice of capacity for repayment (the project names its figure, e.g. one item or a fixed share of the plan) before new feature work is allocated. Repayment is never negotiated item-by-item against features at planning time.
10. **DX-090 — Closure requires a merged change.** An entry is closed only by a merged change that removes the debt, and the closure records the date and the change reference. Editing an entry away, or deciding it "no longer matters," is not closure; an item the project consciously accepts permanently is reclassified as a recorded accepted-risk decision, with the decider named.
11. **DX-091 — The register is reviewed on a cadence and reported.** The register is reviewed at least once per release (or monthly, whichever is sooner): triggers checked against today, owners confirmed live, expired items scheduled. The open-item count and the age of the oldest open item are reported in progress.md like any other project metric.
12. **DX-092 — Stale flags are a debt class.** Every feature flag/toggle is a register entry (or register-listed) with an owner and a removal trigger, classified by its toggle type (release, experiment, ops, permissioning). A flag whose trigger has passed is debt in default and is scheduled for removal before new flags are added in the same area.

## BAN list

- **BAN-DX-041 — Bare TODO/FIXME marker.** Banned: a `TODO`, `FIXME`, `HACK`, or `XXX` comment with no register reference, owner, or trigger. Defeats: DET-CODE-011. Bad: `// TODO: add validation later` above the checkout form handler, merged and forgotten. Instead: fix it now, or create the register entry and write `// TODO(DEBT-123): validate postcode format — see register` (DX-086). Severity: BLOCK.
- **BAN-DX-042 — Commented-out code kept as memory.** Banned: leaving a superseded implementation commented out "in case we need it" instead of deleting it and, if the reason matters, recording the decision in the register or decision log. Defeats: DET-CODE-010. Bad: 60 lines of the old pricing function commented out above its replacement for three releases. Instead: delete it — version control is the archive — and note the replacement in the changelog (DX-090). Severity: BLOCK.
- **BAN-DX-043 — Duplication merged as the permanent solution, off-register.** Banned: copy-pasting logic into a second or third location and merging it with no register entry recording the duplication and its consolidation trigger. Defeats: DET-CODE-007. Bad: the tax calculation pasted into checkout, invoice, and refund code, described in review as "fine for now," with nothing recorded. Instead: either extract the shared function now, or register the duplication as deliberate + prudent debt with the trigger "next change to any copy" (DX-083, DX-085). Severity: BLOCK.
- **BAN-DX-044 — Register entry deleted to close it.** Banned: removing or rewriting a register entry so the debt disappears from the record without a merged fix. Defeats: DET-CODE-031. Bad: a cleanup commit deletes DEBT-009 ("old, probably fine") and the duplicated logic it described ships for another year. Instead: close entries only under DX-090 — merged change reference recorded, or a named accepted-risk reclassification. Severity: BLOCK.
- **BAN-DX-045 — Stub shipped as done, gap relabeled "debt" off-register.** Banned: presenting a placeholder or stub as the finished feature and calling the missing behavior "technical debt" without a register entry. Defeats: DET-CODE-003. Bad: the export button downloads a hardcoded sample file; the missing real export is described in the handover as "a bit of debt." Instead: the feature is not done — either implement it, or ship it visibly incomplete with the gap registered, triggered, and owned (DX-082, DX-083). Severity: BLOCK.

## Gates

- **G-DX-041 — Marker-reference lint (automated).** Verifies: DX-086. Check: `grep -rnE '\b(TODO|FIXME|HACK|XXX)\b' --exclude-dir=node_modules --exclude-dir=.git . | grep -vE '(TODO|FIXME|HACK|XXX)\(DEBT-[0-9]+\)' | grep -vE '(samples|templates|examples|docs|locales)/'` — instructional fill-in prompts in copy-and-edit templates are excluded per DET-CODE-011. Pass: no output (every marker carries a register reference). Fail: block shipment until each hit is fixed, registered, or deleted. Recorded in: progress.md.
- **G-DX-042 — Register completeness check (automated).** Verifies: DX-081, DX-082. Check: parse the register table in `docs/tech-debt.md` (columns: ID, location, quadrant, interest, owner, trigger, incurred) and assert no cell is empty: `awk -F'|' 'NR>2 {for(i=2;i<=8;i++) if($i ~ /^[[:space:]]*$/) {print "incomplete:", $2; bad=1}} END {exit bad}' docs/tech-debt.md`. Pass: exit 0. Fail: block shipment; complete the fields before merge. Recorded in: progress.md.
- **G-DX-043 — Cross-reference and expiry check (automated).** Verifies: DX-086, DX-087. Check: extract register IDs from code (`grep -rhoE 'DEBT-[0-9]+' --exclude-dir=.git . | sort -u`) and from the register's ID column; `comm` the two lists — code references with no register entry, and register entries with no code reference where a location is in code, are reported; entries whose trigger date is past are listed. Pass: zero dangling references; past-trigger entries appear on the next plan. Fail: block shipment on dangling references; warn on past triggers until scheduled. Recorded in: progress.md.
- **G-DX-044 — Register audit (manual).** Verifies: DX-088, DX-091. Check: at the release/monthly review, sample at least five open entries (or all, if fewer): confirm each owner is still the right owner, each trigger is in the future or scheduled, and each interest statement still describes reality; record open count and oldest-item age in progress.md. Pass: every sampled entry verified and metrics recorded. Fail: warn; correct entries and re-run before the next release. Recorded in: progress.md.
- **G-DX-045 — Closure audit (manual).** Verifies: DX-090. Check: list every entry closed since the last release; for each, open the recorded change reference and confirm the merged change actually removes the debt at the entry's location; diff the register against its previous version (`git log -p docs/tech-debt.md`) and confirm no entry vanished without a closure record. Pass: zero unexplained closures or deletions. Fail: block shipment; restore the entry or record a proper closure. Recorded in: progress.md.

## Anti-patterns

- **Invisible interest.** Entries whose interest field says "messy" or "tech debt" — nothing can be weighed against feature work, so the item loses every planning argument forever. Catch it by reading the interest field aloud: if no concrete work is named as slower or riskier, the entry is not finished.
- **Register graveyard.** Entries are written faithfully at birth and never reviewed; triggers pass, owners move on, and the register becomes a museum. Catch it at each cadence review by listing entries whose trigger date is already past — a growing list means the review is theater.
- **Amnesty by rewrite.** A big refactor or rewrite is declared to "clear the tech debt," and the register is zeroed without mapping which entries the change actually closed. Catch it by requiring per-entry closure references (G-DX-045) — a rewrite closes only the entries it names and demonstrably removes.
- **Interest paid forever, principal never.** The same duplicated or awkward area is worked around change after change — the team pays the interest monthly — while its entry stays "low priority." Catch it by counting touches: if an entry's location has been edited repeatedly since the entry was created, its trigger has effectively fired; schedule the principal.

## Examples

- [Example 1 — The bare TODO](examples/example-1.md) — violates/corrects DX-086, DX-082.
- [Example 2 — The deliberate shortcut, registered](examples/example-2.md) — violates/corrects DX-083, DX-085.
- [Example 3 — The entry that vanished](examples/example-3.md) — violates/corrects DX-090.

## Recall anchors

- If it is not in the register, it is not scheduled — it is invisible.
- Deliberate debt is registered in the same change that incurs it.
- "Temporary" without a trigger and an owner is permanent.
- Interest is concrete work slowed or risk created — never "messy."
- Entries close by merged changes, never by editing the register.

## Checklist

- [ ] Every new shortcut from this change has a register entry created in the same change (DX-083).
- [ ] Every entry has location, quadrant, concrete interest, owner, trigger, and incurred date (DX-082, G-DX-042).
- [ ] No deliberate + reckless item was merged — blocked or scope cut (DX-084).
- [ ] Marker lint passes: every TODO/FIXME/HACK carries a DEBT reference (DX-086, G-DX-041).
- [ ] No core functionality is deferred to a code marker (DX-086).
- [ ] Inadvertent debt found during this work is logged and scheduled (DX-088).
- [ ] This plan reserves its standing repayment slice before feature allocation (DX-089).
- [ ] Closures since the last release each cite a merged change; register metrics are in progress.md (DX-090, DX-091, G-DX-045).
