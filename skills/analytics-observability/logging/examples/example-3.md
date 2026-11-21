# Example 3 — The failure no one could reconstruct

## Before

A payment request crosses the web service, a queue, and a worker. Each writes plain-text lines to its own container's stdout, with no shared ID:

```text
web:    POST /checkout 500
worker: job failed: timeout
```

The containers are redeployed during the incident. Afterwards nobody can say which job belonged to which checkout, in what order things failed, or whether the timeout caused the 500 — the worker's lines vanished with its container, and the survivors cannot be joined.

## After

The trace ID is generated at ingress and propagated through the queue payload; every service ships its lines to the central store:

```text
{"ts":"2026-11-21T14:03:11Z","level":"info","service":"web","trace_id":"tr_EXAMPLE123","request_id":"rq_EXAMPLE9","message":"checkout_started","order_id":"ord_EXAMPLE7"}
{"ts":"2026-11-21T14:03:13Z","level":"error","service":"worker","trace_id":"tr_EXAMPLE123","request_id":"rq_EXAMPLE9","message":"payment_job_failed","order_id":"ord_EXAMPLE7","error_code":"PROVIDER_TIMEOUT"}
```

One query on `tr_EXAMPLE123` reconstructs the whole path after any redeploy (gate G-AN-044), and the restart test (G-AN-045) proves the lines outlive the containers that wrote them.

Note: the Before violates AN-083 (correlation ID on every request-scoped line) and AN-087 (logs ship off the host); the After corrects both.
