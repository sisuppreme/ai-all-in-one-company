# Example 1 — The reset email that was never sent

Note: the Before violates IN-124 (and is banned by BAN-IN-061); the After corrects IN-124.

## Before

The forgot-password handler validates the email format, renders a success toast — "Reset link sent, check your inbox" — and returns. No token is generated, nothing is enqueued, and no email provider is ever called. The user waits at an inbox that will stay empty, and support has no record to check because no message row exists.

## After

The handler generates a single-use reset token with a stated expiry, stores its hash against the account, and enqueues a send job carrying the reset template ID and the token link. The worker sends through the authenticated provider; on acceptance the message ID is written to the message row, and only then does the UI say the email was sent. Delivery and bounce events land on the same row, so support can answer "did it arrive" with a query.
