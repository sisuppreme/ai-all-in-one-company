# Example 1 — The database version in three places

## Before

The project's database version is stated in three documents:

- `stack.md`: "Database: PostgreSQL 15"
- `README.md` (setup section): "You need PostgreSQL 15 running locally."
- `docs/runbook.md` (backup procedure): "Dump with the PostgreSQL 15 client tools."

The project upgrades to PostgreSQL 16. `stack.md` is updated; the README and the runbook are not. A new contributor installs version 15 from the README, and the on-call engineer runs the old client tools from the runbook during an incident. A search for "PostgreSQL" returns three answers, two of them wrong — the site contradicts itself (DET-CON-015).

## After

The fact lives in exactly one home, and every other mention links to it:

- `stack.md`: "Database: PostgreSQL 16" ← the canonical statement
- `README.md` (setup section): "Install the database version specified in [stack.md](../stack.md)."
- `docs/runbook.md` (backup procedure): "Dump with the client tools matching the database version in [stack.md](../stack.md)."

The upgrade edits one line in `stack.md`. A grep for the old version returns no live copies, and every path a reader can take leads to the same answer.

Note: corrects PM-161 — one canonical home per fact; every other document links instead of restating the value.
