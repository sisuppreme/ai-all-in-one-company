# Example 1 — Warning-only checks made into a real gate

## Before

The dbt project's test configuration was softened during a crunch and never
restored:

```yaml
# models/schema.yml
models:
  - name: orders
    columns:
      - name: order_id
        tests:
          - unique:
              config:
                severity: warn      # failure prints a warning; run exits 0
          - not_null:
              config:
                severity: warn
```

Duplicate order IDs land in the warehouse for a month. Every pipeline run
reports success — with warnings, in a log nobody reads — and the duplicates
surface only when finance reconciles by hand.

## After

The checks run at full severity, and the suite is wired into CI and the
orchestrator so a failure stops promotion:

```yaml
# models/schema.yml
models:
  - name: orders
    columns:
      - name: order_id
        tests:
          - unique        # default severity: error -- dbt exits non-zero
          - not_null
```

```bash
# the gate, identical in CI and in the pipeline's promotion step
dbt build --select orders+     # exits non-zero on any failed test
```

The suite-gate check (G-DB-191) proves the wiring with a planted failure:
a deliberately duplicated key in a scratch schema must make both the CI run
and the pipeline step exit non-zero. A suite that has never been seen to
fail is not yet a gate.

Note: corrects DB-383 — a failing check fails the run with a non-zero exit and an alert; a check that cannot fail a run is a report, not a gate.
