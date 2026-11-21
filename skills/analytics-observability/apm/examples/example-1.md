# Example 1 — The trace that ended at the queue

## Before

The checkout request traces beautifully through the web service and the orders service — then stops. The confirmation and fulfilment work runs in background jobs, and the job payloads carry only the order ID. When a fulfilment job starts timing out and retrying, its spans form short, unrelated traces under fresh IDs. During the incident the team can see that checkout "succeeded" and that some job is slow, but cannot connect the two: which requests produced the failing jobs, and how many customers are affected, is unanswerable from the telemetry.

## After

The enqueue call writes the current trace context into the job payload, and the consumer extracts it and continues the originating trace before doing any work. The same incident now shows one trace per affected checkout: HTTP span, orders span, enqueue span, and the consumer's processing span — including its timeout and retries — all under the original trace ID. The blast radius is a trace search, not a guess, and the job's log lines join the same view through the shared ID.

Note: corrects AN-182 — trace context propagates across every boundary, queues and jobs included; a trace that ends at the queue ends where incidents live (BAN-AN-092).
