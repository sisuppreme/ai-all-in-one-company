# Example 3 — The poison message gets a DLQ, not a loop

## Before

One event with a payload the fulfillment consumer cannot parse is retried
forever at the head of the partition. Every later order queues behind it.
The consumer looks "busy" in the dashboard for nine hours while no order
ships, until a customer complains.

## After

The consumer retries a poison candidate a bounded number of times (3, with
backoff), then moves it to the dead-letter queue, fires an alert with the
event `id` and payload reference, and continues with the next message.
On-call inspects the DLQ entry, fixes the payload or the parser, and replays
the message through the documented replay procedure. The consumer's
idempotency (dedupe on `id` + `source`) makes the replay safe.

Note: corrects AR-208 and AR-206 — poison messages go to a dead-letter queue with an alert after bounded retries, and consumers are idempotent so replay applies no duplicate effects.
