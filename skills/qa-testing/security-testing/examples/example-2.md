# Example 2 — Scanner output triaged into a finding record

## Before

The CI dependency scanner reports 14 results. The raw report is pasted into a ticket titled "Security scan," the ticket is closed, and the release notes say "security scanned." Three of the results are a critical vulnerability in a package the app actually loads at runtime; nobody confirmed, accepted, or dismissed any of the 14, and the critical ships.

## After

Each of the 14 results gets a triage line in the finding record: verdict (confirmed / accepted-risk / false positive), the reason, and an owner. The critical in the runtime package is marked confirmed, the dependency is upgraded, and the finding is retested — the scanner exits 0 on the fixed tree and the retest result is attached before the finding closes. The remaining results carry written false-positive reasons or dated accepted-risk notes.

*Demonstrates QA-185: every scanner result is triaged with a verdict and reason; raw output is never the finding record.*
