# Example 1 — Replacing a hardcoded rate with operator configuration

## Before

The checkout computes tax from a rate a developer typed in from memory:

```text
TAX_RATE = 0.20   // "standard VAT"
total = subtotal + round(subtotal * TAX_RATE)
```

No one can say which jurisdiction this rate belongs to, when it was last
checked, or whether it applies to this product at all — but the receipt
presents the result as the tax charged, and the same constant quietly
survives every pricing change and every new market the product enters.

## After

The checkout asks the tax configuration for the rate; code holds none:

```text
category   = product.tax_category            // set in configuration
rate_entry = tax_config.lookup(
               jurisdiction = customer.place_of_supply,
               category     = category,
               on           = charge_date)   // operator-entered,
                                             // operator-verified,
                                             // effective-dated
total      = subtotal + tax_from(rate_entry, line_items)
invoice.tax_breakdown records: jurisdiction, category,
               rate_entry ID, effective date, tax amount
```

When the operator's accountant supplies updated figures, the operator
edits configuration with a new effective date; historical invoices keep
pointing at the rate entry that was actually applied to them.

Note: corrects IN-062 — rates are operator-supplied configuration, verified against the operator's own jurisdiction sources at setup, never literals in code.
