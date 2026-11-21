# Example 3 — Closing a finding on retest, not on a promise

## Before

The report lists a high-severity finding: session tokens remain valid after logout. The engineer replies in the ticket, "Fixed — we now rotate tokens," and the tester closes the finding on the strength of the reply. Nobody re-runs the attack. Two months later a customer reports account takeover; the rotation was implemented for the web login but not for the mobile API's refresh flow, and the original flaw is still live there.

## After

The finding stays open until retest. After the fix deploys to staging, the tester re-runs the original reproduction exactly as written: log in, capture the token, log out, replay the token — now rejected. The tester then retests the flaw class across the implicated surface, including the mobile API's refresh flow, where the replay still succeeds; that result goes back as a continuation of the same finding, not a new one. Only when every path in the reproduction set rejects the replayed token is the finding marked closed, with the retest date and results recorded in the report's retest table. Fixes without a retest appear under "Unverified fixes," never as closed.

Note: corrects SE-231 — every critical/high finding is retested after remediation with the original reproduction; an unretested fix is reported as unverified.
