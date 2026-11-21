# Example 1 — The NPS popup nobody read

## Before

```text
In-product NPS popup:
  Trigger: fires on every page load, every session, all users.
  Submit: writes score + comment to a shared spreadsheet.
  Confirmation: "Thanks! Your feedback helps us improve."
  Owner: none. Last time the spreadsheet was opened: launch week.
  Responses this quarter: 1,140. Responses reviewed: 0.
```

The popup asks constantly and the answers go nowhere — the loop is a form with a thank-you message wired to nothing, and repeat prompting trains users to dismiss it unread.

## After

```text
In-product NPS survey:
  Trigger: account-age day 30, then at set intervals;
  shared per-user cap blocks any re-prompt inside the window.
  Submit: response stored on the user record with context
  (trigger: day-30 lifecycle, segment, timestamp) — the
  confirmation shows only after the store is acknowledged.
  Owner: CX lead. Review cadence: weekly; last-reviewed date
  recorded in the survey configuration.
  Detractor scores create a follow-up task automatically.

G-CX-061 trace: test submission landed on the test user's
record with context, appeared in the owner's queue, and an
immediate second trigger was blocked by the cap.
```

## Note

Corrected under CX-123, CX-124, and CX-125 (BAN-CX-061): responses attach to the user record, a shared frequency cap replaces every-load firing, and a named owner reviews on a recorded cadence — or the survey is removed.
