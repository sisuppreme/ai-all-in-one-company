# Example 3 — Replacing a sample-PDF download with a render of the stored record

## Before

The billing page has a Download Invoice button wired to a static asset:

```text
GET /billing/invoice.pdf
  → serves assets/sample-invoice.pdf
    "INV-1001 — Pro plan — $49.00 — Jane Sample"
```

Every customer gets the same sample document whatever they bought, and
the marker test proves it: buy a uniquely named plan, download the
"invoice," and nothing about the purchase appears in the file.

## After

The button renders the customer's own stored record, on demand:

```text
GET /billing/invoices/INV-1042.pdf
  → load invoice INV-1042 from the billing store
    (number, lines, tax breakdown, customer legal name/address,
     tax ID, provider charge ID — all captured at purchase)
  → render PDF from that record
  → totals recomputed from line items match the provider charge
```

Create a record with a unique marker, download immediately, and the
marker is in the file; re-download a year later and the document is
identical to the one issued at purchase.

Note: corrects IN-069 — the download renders the same stored data that was issued; a static sample delivered as "your invoice" is fabrication.
