# Example 2 — "Delivered" copied from the send response

Note: the Before violates IN-125 (and is banned by BAN-IN-063); the After corrects IN-125.

## Before

The send worker calls the provider API, gets a 200 response, and immediately writes `status = delivered` on the message row. When a customer's mailbox rejects the message, the bounce event arrives at a webhook endpoint nobody wired up, and the admin panel keeps showing "delivered" for mail that never reached an inbox.

## After

Acceptance writes `status = accepted` with the provider message ID. A webhook handler consumes the provider's delivery, bounce, and complaint events and advances the row to `delivered`, `bounced`, or `complained` as the events actually arrive. The admin panel reads those recorded states, and a bounced reset email triggers suppression of the address instead of a confident lie.
