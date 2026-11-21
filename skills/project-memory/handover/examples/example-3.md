# Example 3 — "No known issues" replaced by an evidenced landmines list

## Before

handover.md's risks section reads, in full:

"Risks: No known issues. The system is stable."

The project's own records disagree. progress.md carries a blocked item on
the payment-retry defect, owned and waiting on a provider change. A
postmortem from the last outage has two follow-up actions still open. The
database backup job has never been restore-tested. None of this is secret —
it is simply not in the handover, so the receiver inherits the risks without
inheriting the knowledge.

## After

The landmines list is built by diffing the project's records (G-PM-094), not
from the giver's impression:

- **Payment retries can double-charge on provider timeout.** Status: blocked
  in progress.md since 2026-11-14, owner named, unblocks when the provider
  ships idempotency keys. Evidence: progress.md blocked entry; runbook
  "Payments — duplicate charge" describes the manual check.
- **Postmortem follow-ups open (2 of 5).** Add alerting on the queue-depth
  metric and automate the cache-warm step. Owners and due dates as recorded
  in the postmortem; both transfer with the project.
- **Backups never restore-tested.** Nightly backups run and report success;
  no restore has ever been performed. First restore test is the receiver's
  opening task, scheduled in the transfer plan.

Each entry names the risk, its state, its owner, and where the evidence
lives. The receiver can now repeat the top risks back in the cold run —
because they were handed over, not discovered.

Note: corrects PM-184 — open risks and landmines are listed explicitly, each with evidence or a link; "none known" is a stated finding, never an omission.
