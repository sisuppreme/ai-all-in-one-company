# Example 1 — `SendWelcomeEmail` becomes `UserRegistered`

## Before

The signup service publishes an event named `SendWelcomeEmail`. It is a
command aimed at one consumer, wearing an event's clothes: signup's
definition of "registration complete" quietly includes the email service
obeying. When the email team renames their consumer, signups "succeed" and
no welcome email ever arrives — and no contract anywhere said one would.

## After

Signup publishes the fact:

```json
{
  "specversion": "1.0",
  "id": "9f3c…",
  "source": "/accounts/signup",
  "type": "UserRegistered",
  "data": { "user_id": "u_123", "registered_at": "2026-11-21T10:15:00Z" }
}
```

The email service is listed in the AsyncAPI document as a known consumer of
`UserRegistered` and sends the welcome email as its own decision. Analytics
later subscribes to the same fact without signup changing at all.

Note: corrects AR-202 — events are facts in the past tense, never commands a producer secretly depends on a specific consumer executing.
