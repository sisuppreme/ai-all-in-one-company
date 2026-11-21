# Example 2 — A bare "blocked" rewritten as a triple

## Before

progress.md carries the entry:

"Blocked: waiting on API keys."

No date, no owner, no statement of what is actually missing or what would
clear it. A reader cannot act on it, cannot escalate it, and cannot tell
whether it has been true for a day or a month. The work behind it sits idle
while everyone assumes someone else holds the keys.

## After

The entry is rewritten as a dated triple:

"Blocked (2026-11-21): sandbox API keys for the payments provider have not
been issued, so the checkout gate cannot run against the provider. Owner:
the project owner, who holds the provider account. Unblocks when: the keys
are created in the provider dashboard and added to the project's secret
store. Re-check: 2026-11-23."

Now the blocker is a fact with a name attached: one person can act, the
condition for clearing it is testable, and the re-check date forces the
entry to be re-verified instead of carried forward forever.

Note: corrects PM-147 — a blocked item names the blocker, its owner, and the condition that unblocks it.
