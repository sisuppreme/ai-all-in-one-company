# Example 1 — A profile edit that only existed in local state

## Before

The verifier opens Settings on the preview deployment, changes the display
name to "Test User 2", and clicks Save. A toast appears: "Profile updated ✓".
The screenshot of the toast is filed and the feature is recorded as verified.

What was never checked: no reload, no re-login, no look at the network tab.
The save handler wrote to local state and fired the toast; no request left
the browser. On reload, the old display name returns — the edit never
existed anywhere but in memory.

## After

The same edit, run under the two-test protocol:

1. Network tab open: clicking Save fires no request at all. That alone fails
   the network test (QA-066).
2. Persistence test anyway: reload the page, sign out and back in, open a
   second browser. The display name is the old value in all three (QA-065).
3. Verdict recorded in progress.md: profile edit — FAKE, matching
   DET-FAKE-016 (profile edits that don't stick), with the network capture
   (empty) and before/after values filed as evidence. A defect is opened the
   same day (QA-072).

Note: corrects QA-065 and QA-066 — an edit is verified only when it survives reload and re-login and a real server write is observed.
