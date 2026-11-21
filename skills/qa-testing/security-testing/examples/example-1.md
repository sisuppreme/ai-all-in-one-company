# Example 1 — Authorization proven by replay, not by a hidden button

## Before

The release checklist marks authorization "tested": a reviewer logged in as a standard user, confirmed the admin **Delete user** button does not appear on the admin page, and signed off. The `DELETE /api/admin/users/:id` endpoint itself was never called with a non-admin session — and in fact returns 200 and deletes the user for any authenticated account, because enforcement exists only in the UI.

## After

An automated test in the authz suite logs in with a standard-user session, replays `DELETE /api/admin/users/<id>` exactly as an admin would send it, and asserts the response is 403 and the target user still exists. The test fails against the unprotected endpoint, the server-side role check is added, and the test passes — authorization is now proven from the attacker's seat.

*Demonstrates QA-186: every privileged endpoint is replay-tested with a lower-privilege session and must be rejected.*
