# Example 2 — Replacing acceptance-as-delivered with callback terminal states

## Before

The send handler treats the API response as the outcome:

```text
provider.send(...) → HTTP 201
  → messages.status = "delivered"
  → dashboard delivery rate: 100%
```

The provider accepted the messages, but carriers filtered a third of
them as unregistered traffic. Every filtered message sits in the local
table as "delivered," the delivery report is fiction, and nobody
investigates because nothing looks broken.

## After

The API response records acceptance; callbacks decide delivery:

```text
provider.send(...) → HTTP 201, SID SM_456
  → messages.status = "accepted"

Status callbacks for SM_456 arrive over the following seconds:
  → "queued" → "sent" → "undelivered" (carrier filtered, error 30034)
  → messages.status = "undelivered", error recorded
  → dashboard delivery rate counts only terminal "delivered" rows
  → the undelivered cluster raises the registration finding (IN-152)
```

The report now shows the real rate, and the failure has a name and a
fix instead of a green dashboard.

Note: corrects IN-144 — delivery is a terminal state reached through provider status callbacks, never the API's acceptance response.
