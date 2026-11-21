# Example 2 — The policy that "passed" retention

Note: demonstrates LG-124 (test flows, not documents) and BAN-LG-063.

## Before

The audit marks the storage-limitation control as passing. The evidence field cites the privacy policy, which states that support tickets are deleted after 12 months. No one runs anything. In the live database, support tickets from the product's first year — over three years old — are still stored, because no deletion job was ever built; the policy describes an intention, not a mechanism.

## After

The auditor tests the flow: a query against the ticket store for records older than the registered retention period returns thousands of rows, and that query output is filed as the evidence artifact. The control is recorded as failing, with a finding carrying severity, owner, and a remediation date. After the deletion job is built and run, the auditor re-runs the same query; the empty result is filed, and only then does the finding close (LG-128).
