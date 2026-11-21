# Example 3 — Double-click duplicates replaced by idempotent submission

Corrects rule **FE-248** (submission is idempotent from the user's side).

## Before

```jsx
// Every click fires a fresh POST. A double-click — or a retry
// after a slow network — creates a second order.
async function onSubmit(e) {
  e.preventDefault();
  await fetch("/api/orders", {
    method: "POST",
    body: JSON.stringify(cart),
  });
  showConfirmation();
}
```

## After

```jsx
// One idempotency key per checkout attempt: the button disables
// on submit, and the server dedupes retries carrying the same key.
import { useRef, useState } from "react";

function CheckoutButton({ cart }) {
  const [submitting, setSubmitting] = useState(false);
  const keyRef = useRef(crypto.randomUUID()); // one key per attempt

  async function onSubmit(e) {
    e.preventDefault();
    if (submitting) return;
    setSubmitting(true);
    try {
      await fetch("/api/orders", {
        method: "POST",
        headers: { "Idempotency-Key": keyRef.current },
        body: JSON.stringify(cart),
      });
      showConfirmation();
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <button type="submit" onClick={onSubmit} disabled={submitting}>
      {submitting ? "Placing order…" : "Place order"}
    </button>
  );
}
```

Note: the before version is BAN-FE-124 — the server cannot tell a retry from a second order. The after version makes one user intent produce exactly one record, which gate G-FE-123 verifies by double-clicking.
