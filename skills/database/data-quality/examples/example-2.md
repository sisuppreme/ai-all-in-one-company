# Example 2 — Key and relationship tests that catch injected faults

## Before

The warehouse models ship with descriptions but no tests at all:

```yaml
# models/schema.yml
models:
  - name: orders
    description: "One row per order."
  - name: order_items
    description: "One row per line item."
```

A source-system replay duplicates a block of orders, and a delete upstream
orphans a set of line items. Nothing notices: there is no assertion anywhere
that order IDs are unique or that line items belong to real orders. The
corruption is discovered weeks later, downstream, in a revenue report.

## After

Every key carries its tests, declared next to the models they guard:

```yaml
# models/schema.yml
models:
  - name: orders
    columns:
      - name: order_id
        tests:
          - unique
          - not_null
  - name: order_items
    columns:
      - name: order_item_id
        tests:
          - unique
          - not_null
      - name: order_id
        tests:
          - not_null
          - relationships:
              arguments:
                to: ref('orders')
                field: order_id
```

The suite is proven, not assumed: the negative-test gate (G-DB-192) injects
a duplicate `order_id` and an `order_items` row pointing at a nonexistent
order into a staging fixture, and the suite must catch both and name the
datasets. Only a suite that has caught a planted fault is trusted to catch
a real one.

Note: corrects DB-381 — every primary key has unique and not-null tests; every foreign key has a relationships test.
