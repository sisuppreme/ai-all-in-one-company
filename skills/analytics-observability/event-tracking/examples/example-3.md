# Example 3 — The email address riding in a property

## Before

A `Support Requested` event is shipped with helpful debugging properties: `user_email: "customer@example.com"` and `message: <the full typed support text>`. The analytics store now holds personal data and free text for every requester, outside the retention and deletion rules that govern the support system itself.

## After

The event carries only `user_id` (the opaque account ID), `topic_category`, and `attachments_count`. The message and the email stay in the support system of record, reachable by ID when a human actually needs them, and the event stream holds nothing D14's rules would flag.

_Rule: AN-026 — no personal data in event names or properties; people are referenced by opaque IDs only (BAN-AN-012)._
