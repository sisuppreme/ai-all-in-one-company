# Example 1 — A cron chain replaced with a declared DAG

## Before

Three cron lines on one application server run the billing pipeline:

```cron
0 1 * * *  /opt/jobs/extract_orders.sh
20 1 * * * /opt/jobs/transform_orders.sh
45 1 * * * /opt/jobs/load_warehouse.sh
```

The "dependencies" are the clock: the transform starts 20 minutes after the
extract because the extract *usually* takes 10. When the extract runs long,
the transform processes a half-landed window. When the server is rebuilt,
the crontab is not restored and the pipeline silently stops for a week.
There are no retries, no timeouts, and no alerts — only three shell scripts
and a superstition about timing.

## After

One DAG declares the schedule, the dependencies, and each task's contract:

```python
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    "owner": "data-team",
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
    "execution_timeout": timedelta(minutes=30),
    "email": ["data-alerts@example.com"],
    "email_on_failure": True,
}

with DAG(
    dag_id="orders_pipeline",
    schedule="0 1 * * *",
    start_date=days_ago(1),
    catchup=False,
    default_args=default_args,
) as dag:
    extract = BashOperator(
        task_id="extract_orders",
        bash_command="/opt/jobs/extract_orders.sh "
                     "--start {{ data_interval_start }} "
                     "--end {{ data_interval_end }}",
    )
    transform = BashOperator(
        task_id="transform_orders",
        bash_command="/opt/jobs/transform_orders.sh "
                     "--start {{ data_interval_start }} "
                     "--end {{ data_interval_end }}",
    )
    load = BashOperator(
        task_id="load_warehouse",
        bash_command="/opt/jobs/load_warehouse.sh "
                     "--start {{ data_interval_start }} "
                     "--end {{ data_interval_end }}",
    )

    extract >> transform >> load
```

Ordering now comes from declared dependencies, not from the clock; a slow
extract delays the transform instead of corrupting it; and the DAG lives in
the repository, deployed like any other code (DB-366). The cron census gate
(G-DB-184) asserts no pipeline jobs remain outside the orchestrator.

Note: corrects DB-361 — every production pipeline runs under the orchestrator; none runs on a bare cron entry.
