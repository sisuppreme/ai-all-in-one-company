# Example 2 — Wiped form and generic error replaced by inline errors with data preserved

Corrects rules **FE-244** (errors inline, named, summarized) and **FE-245** (entered data survives errors).

## Before

```jsx
// On any error: one generic banner at the top, and the form
// resets — every field the user filled in is gone.
function CheckoutForm() {
  const [error, setError] = useState("");
  async function onSubmit(e) {
    e.preventDefault();
    const res = await submitOrder(collectValues(e.target));
    if (!res.ok) {
      setError("Something went wrong. Please try again.");
      e.target.reset(); // destroys the user's work
    }
  }
  return (
    <form onSubmit={onSubmit}>
      {error && <div className="banner">{error}</div>}
      {/* name, address, city, postal code inputs… */}
      <button type="submit">Place order</button>
    </form>
  );
}
```

## After

```jsx
// Errors are per-field, inline, and announced; the summary takes
// focus; values live in state and are never cleared on failure.
function CheckoutForm() {
  const [values, setValues] = useState({ name: "", postalCode: "" });
  const [errors, setErrors] = useState({});
  const summaryRef = useRef(null);

  async function onSubmit(e) {
    e.preventDefault();
    const fieldErrors = validate(values); // { postalCode: "…" }
    setErrors(fieldErrors);
    if (Object.keys(fieldErrors).length > 0) {
      summaryRef.current?.focus();
      return; // values untouched — the user fixes one field
    }
    await submitOrder(values);
  }

  return (
    <form onSubmit={onSubmit} noValidate>
      {Object.keys(errors).length > 0 && (
        <div ref={summaryRef} tabIndex={-1} role="alert">
          <p>There is a problem with this order:</p>
          <ul>
            {Object.entries(errors).map(([field, msg]) => (
              <li key={field}><a href={`#${field}`}>{msg}</a></li>
            ))}
          </ul>
        </div>
      )}
      <label htmlFor="postalCode">Postal code</label>
      <input
        id="postalCode"
        value={values.postalCode}
        onChange={(e) => setValues({ ...values, postalCode: e.target.value })}
        aria-invalid={Boolean(errors.postalCode)}
        aria-describedby={errors.postalCode ? "postalCode-error" : undefined}
      />
      {errors.postalCode && (
        <p id="postalCode-error">Postal code: enter the 5-digit code for your address.</p>
      )}
      <button type="submit">Place order</button>
    </form>
  );
}
```

Note: the before version commits BAN-FE-122 (no field named, no fix stated) and BAN-FE-123 (input destroyed). The after version names the field and the fix, moves focus to the summary, and keeps every value.
