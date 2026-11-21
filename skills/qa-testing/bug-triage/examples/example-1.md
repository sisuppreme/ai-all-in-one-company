# Example 1 — A merged PR is not a closure

## Before

Defect #412: "Checkout total ignores the applied discount code." The developer merges a fix, comments "fixed in PR #88", and moves the ticket to Verified. No test is run against the original reproduction steps and no retest note is attached. The next release ships with the same defect: the fix handled one discount type and the reported one still fails — but the tracker showed the defect as verified and closed.

## After

The ticket stays open after the merge. The verifier re-runs the original reproduction steps on the release build, attaches a retest note naming the build and environment, and the new regression test for the discount case is linked and green. Only then does the defect close. When a second discount type fails the same check a week later, the original defect reopens with its history intact instead of appearing as an unrelated new ticket.

Note: corrects QA-267 (closure requires verification) and QA-268 (reopen without penalty).
