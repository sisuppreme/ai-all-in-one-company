# Example 3 — Closed without a word

## Before

```text
Ticket #3917 — "Export button fails on large files"
  Agent finds and fixes the bug, sets status: Closed.
  No message sent to the requester.
  Requester's next contact: a new ticket, "Did anyone even
  look at my export problem?" — unlinked to #3917, which the
  team then handles as a fresh issue.
```

The work was done, but the customer was never told, could not confirm the fix, and had no way to reopen the original request.

## After

```text
Ticket #3917 — "Export button fails on large files"
  Agent fixes the bug, sets status: Solved.
  Automatic resolution notice to the requester:
    "We believe this is fixed in today's release. Your ticket
     #3917 is marked Solved. Reply within 7 days if it still
     fails and it reopens; otherwise it closes automatically."

  Day 2: requester replies "Works now, thanks" → Closed
  (customer-confirmed). Had they replied "still broken," the
  same ticket would have returned to Open with its history.

G-CX-005 flow test: notice sent, ticket held at Solved, reply
inside the window reopened it, Closed reached only on
confirmation or lapse.
```

## Note

Corrected under CX-010 (BAN-CX-005): Solved is not Closed — the customer gets a resolution notice and a stated reopen window, and the ticket closes only on their confirmation or after the window lapses.
