# Example 1 — Replacing a simulated send with a provider send

## Before

The "send SMS" step writes a local row and shows a success toast:

```text
POST /orders/42/notify
  → insert notifications row: "Your order has shipped"
  → render toast "SMS sent to +1 555 010 2030"
```

No provider is ever called and no phone receives anything. The
notification exists only inside the app, while the user was told a text
was sent — support has no message ID to trace when the customer says
nothing arrived.

## After

The send goes through the provider and the record carries its ID:

```text
POST /orders/42/notify
  → check suppression list for the number and category (clear)
  → enqueue to messaging provider, from the registered campaign number
  → provider returns message SID SM_789
  → store send record: sid = SM_789, state = queued, opt-in ref #opt-311

Provider status callback (signature verified)
  → state advances queued → sent → delivered, each step timestamped
  → UI reads the send record: "Text delivered"
```

If the callback ends at `failed`, the record and the UI say failed —
the claim always matches the provider's state.

Note: corrects IN-143 — every SMS is enqueued through the messaging provider and the returned message SID is stored against the send record.
