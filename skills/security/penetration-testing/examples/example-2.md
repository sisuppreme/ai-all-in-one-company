# Example 2 — Proving BOLA without taking data

## Before

Testing the orders API, the tester finds that changing the order ID in `GET /api/orders/{id}` returns other customers' orders. To "prove impact," the tester scripts a loop that downloads 500 real orders — names, addresses, phone numbers — and attaches the spreadsheet to the findings folder as evidence. The proof itself is now the engagement's worst data exposure: real customer data copied out of the system, stored unencrypted, and shared with everyone who can read the report.

## After

The tester creates two tester-owned accounts, A and B. Account A places one order. Authenticated as B, the tester requests A's order ID once and captures the response: a single cross-account read, with the customer fields in the screenshot redacted except the order ID and the account mismatch. The finding records the reproduction (SE-230), rates severity on the class of data reachable rather than on a downloaded volume, and the tester reports through the agreed channel that the endpoint exposes real records — without ever copying them. One request proves the flaw; zero real records leave the system.

Note: corrects SE-227 — real user data is evidence to minimize; demonstrate the flaw with tester-owned records, never exfiltrate datasets as proof.
