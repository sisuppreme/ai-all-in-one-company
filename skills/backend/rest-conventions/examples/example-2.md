# Example 2 — 200-with-error replaced by problem details

## Before

```ts
app.post("/orders", async (req, res) => {
  const result = await createOrder(req.body);
  if (!result.ok) {
    // Validation failed, but the status still says success:
    return res.status(200).json({ success: false, error: "Invalid order" });
  }
  res.status(200).json({ success: true, order: result.order });
});
```

Clients must parse the body to learn the request failed, monitors record a
success, and every endpoint invents its own error wording.

## After

```ts
app.post("/orders", async (req, res) => {
  const parsed = orderSchema.safeParse(req.body);
  if (!parsed.success) {
    return res
      .status(422)
      .type("application/problem+json")
      .json({
        type: "https://api.example.com/problems/validation-failed",
        title: "Order validation failed",
        status: 422,
        detail: "One or more fields failed validation.",
        instance: "/orders",
        errors: parsed.error.issues.map((i) => ({
          field: i.path.join("."),
          rule: i.code,
          message: i.message,
        })),
      });
  }

  const order = await createOrder(parsed.data);
  res.status(201).location(`/orders/${order.id}`).json(orderView(order));
});
```

The status now carries the outcome (422 for a business-rule rejection, 201 +
`Location` for a create), and the body is the one RFC 9457 shape every
endpoint in the API returns.

Note: corrects BE-025 — status codes follow the decision rule and an error is never 200; and BE-030 — every error is RFC 9457 problem details.
