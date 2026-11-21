# Example 3 — A duplicated field with a source of truth

## Before

```javascript
// displayName is copied into orders with no owner and no update path.
// A rename updates the user document only; 10,000 order documents keep the old name.
db.users.updateOne({ _id: userId }, { $set: { displayName: "New Name" } });
// db.orders: customer.name still says the old name, forever, inconsistently.
```

## After

```javascript
// Design note (in the data-model document):
//   Field: orders.customer.name
//   Source of truth: users.displayName
//   Update strategy: historical orders keep the name as it was at purchase time
//   (it is a snapshot, like the price); the account screen always reads users.
//   Current-name reads never use the order copy. Reconciliation: none needed —
//   the copy is a snapshot by design, not a replica.
// If the copy had to stay current instead, the strategy would be:
//   fan-out on rename (updateMany in the same job) + a nightly reconciliation
//   job that reports any order whose name differs from the source.
db.users.updateOne({ _id: userId }, { $set: { displayName: "New Name" } });
```

Corrects DB-045 (every duplicated field has one named source of truth and a written update strategy).
