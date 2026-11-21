# Example 1 — The form that went nowhere

## Before

```text
Contact page (live):
  "Questions? Write to us — we reply within 24 hours."
  [ Name ] [ Email ] [ Message ] [ Send ]

Form action: POST /api/contact
Server handler: validates fields, returns 200 OK, discards the body.
No ticket created. No email sent. No inbox notified.
Submissions this month: 41. Replies sent: 0.
```

The page promises a reply within 24 hours; the system behind the promise does not exist, so every one of the 41 submissions vanished silently.

## After

```text
Contact page (live):
  "Questions? Write to us — we reply within 24 hours."
  [ Name ] [ Email ] [ Message ] [ Send ]

Form action: POST /api/contact
Handler: creates a ticket in the ticketing system
  (requester, type=question, priority=normal, tags=web-form),
  returns the ticket reference to the confirmation screen.

Automatic acknowledgment email to the requester:
  "Thanks — your request is #4821. Current status: New.
   Track it any time from the link in this email."

G-CX-001 intake test: submission from an external address created
ticket #4821, acknowledgment arrived with the reference, ticket
visible in the agent queue and in the customer's request view.
```

## Note

Corrected under CX-001 and CX-004 (BAN-CX-001): every intake channel creates a tracked ticket, and the acknowledgment is automatic and carries the reference the customer can quote.
