# Example 2 — The detractor who heard nothing

## Before

```text
Post-resolution CSAT survey (after a support ticket closes):
  Score: 1 of 5. Comment: "Export still fails on large files.
  Support closed my ticket without testing it."
  Stored: yes, on the survey report.
  Follow-up task: none. Owner notified: no.
  What the customer received after submitting: "Thanks!"
```

The survey collected a specific, fixable complaint from an unhappy customer and routed it to no one — the pain was harvested, the human response never happened.

## After

```text
Post-resolution CSAT survey:
  Score: 1 of 5 with the same comment.
  On submit: a follow-up task is created in the CX queue,
  assigned to a named agent, with the original ticket linked
  and the customer's contact path attached.
  The customer sees: "Thanks — a member of the team will
  follow up on this within our stated support hours."
  The agent reopens the ticket, reproduces the export
  failure, and replies to the customer the same day.

G-CX-065 test: a test detractor submission created the
assigned follow-up task in the owning team's queue.
```

## Note

Corrected under CX-127 (BAN-CX-064): a low score creates a follow-up task for a named human and tells the respondent how they will be reached — collecting detractor pain with no response path is worse than not asking.
