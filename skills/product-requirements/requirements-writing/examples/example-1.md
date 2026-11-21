# Example 1 — Splitting a compound requirement

## Before

REQ-14: "The system shall send email and SMS notifications to the account
owner and log all deliveries for audit."

Three obligations share one ID. When the SMS channel fails its test, nobody
can tell whether REQ-14 passes or fails.

## After

REQ-14: "The system shall send an email notification to the account owner when
an order status changes." Verification: test.

REQ-15: "The system shall send an SMS notification to the account owner when
an order status changes." Verification: test.

REQ-16: "The system shall record every notification delivery attempt, with
channel, timestamp, and outcome, in the audit log." Verification: inspection
of the audit log after a test send.

Each obligation can now pass or fail on its own.

Note: corrects PR-061 — one obligation per requirement; compound requirements are split.
