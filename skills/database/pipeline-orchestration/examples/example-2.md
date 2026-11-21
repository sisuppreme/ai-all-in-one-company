# Example 2 — A silent failure wired to a named alert target

## Before

A DAG fails on Friday night. Airflow marks the run failed — in its own UI,
which nobody opens over the weekend. Dashboards serve Friday's data all
weekend, and the team learns about the failure from a customer on Monday.
The pipeline had monitoring in the sense that a log existed; it had no
alerting in the sense that a human was told.

## After

Exhausted retries call a failure callback that pages a named channel, and
the DAG carries an SLA so staleness alerts before the failure is even
noticed downstream:

```python
import requests

def alert_on_failure(context):
    ti = context["task_instance"]
    requests.post(
        "https://hooks.example.com/data-alerts",   # monitored on-call channel
        json={
            "dag": ti.dag_id,
            "task": ti.task_id,
            "window": str(context["data_interval_start"]),
            "log_url": ti.log_url,
        },
        timeout=10,
    )

default_args = {
    "owner": "data-team",
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
    "on_failure_callback": alert_on_failure,
}

# on the DAG:
#   sla=timedelta(hours=2)  -- a run not finished 2h after schedule alerts
```

The kill test (G-DB-182) terminates a task in staging and asserts the full
chain: retries happen per policy, the callback fires to the named target on
exhaustion, and no partial output reaches downstream. An alert path that has
never been test-fired is assumed broken.

Note: corrects DB-368 — when retries are exhausted, the failure alerts a named, monitored target; a log entry alone alerts nobody.
