# Example 2 — Making a vague requirement measurable

## Before

REQ-22: "The dashboard shall load fast and feel seamless for all users."

No tester can pass or fail this. Whatever ships will be declared "fast" after
the fact, and the argument will be settled by opinion.

## After

REQ-22: "The dashboard shall render first contentful paint within 2.0 seconds
and complete its data load within 3.5 seconds, measured on the reference
device (mid-range Android, 4G throttling) against the reference dataset
(500 orders, 30 days)." Verification: test, using the performance harness
named in the test plan.

"Fast" is gone; the criterion, the device, and the dataset are all stated in
the same sentence as the obligation.

Note: corrects PR-063 — vague terms are banned unless the same sentence carries the measurable criterion.
