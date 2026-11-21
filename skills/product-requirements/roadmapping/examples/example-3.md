# Example 3 — The quiet swap

## Before

After a stakeholder call, the roadmap file is edited directly: "Guest access" and "Audit log" trade places in Now, and "Offline mode" disappears from Next. No note is left. The public roadmap still shows the old order, support answers a customer question from the public version, and at the next review nobody can reconstruct why offline mode was dropped — including the person who dropped it.

## After

The same changes, recorded as roadmap changes (PR-248):

```markdown
## Roadmap change log

| Date | Change | Why | Displaced |
|---|---|---|---|
| 2026-11-20 | Audit log moved Next → Now; guest access moved Now → Next | Two signed enterprise contracts require an audit log this quarter (contracts #114, #117) | Guest access slips one horizon; its discovery notes carry over |
| 2026-11-20 | Offline mode removed from Next | Assumption test AT-12 failed: field users in the pilot already had a workaround they preferred | Slot in Next taken by "explain metric movement" discovery |
```

The public roadmap is regenerated from the same item list in the same edit, so the two views cannot drift apart.

## Note

Corrected under PR-248: every roadmap change records what moved, why, and what it displaced; silent re-sequencing is a defect (see also PR-250).
