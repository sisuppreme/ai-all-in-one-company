# Example 3 — Hand-rolled date and price formatting replaced by `Intl`

## Before

```js
function invoiceLine(invoice) {
  const d = invoice.issuedAt;
  const date = (d.getMonth() + 1) + '/' + d.getDate() + '/' + d.getFullYear();
  const price = '$' + invoice.total.toFixed(2);
  return `Issued ${date} — Total ${price}`;
}
// "Issued 3/4/2026 — Total $120.00"
```

The date is one hard-coded MM/DD/YYYY pattern — a day-first reader reads 3 April as 4 March — and the price forces a `$` sign and two decimals onto every currency, implying a US-dollar amount even when the invoice is in euros or yen (which has no minor unit at all).

## After

```js
function invoiceLine(invoice, locale) {
  const date = new Intl.DateTimeFormat(locale, { dateStyle: 'medium' })
    .format(invoice.issuedAt);
  const price = new Intl.NumberFormat(locale, {
    style: 'currency',
    currency: invoice.currency, // the invoice's own currency, e.g. "EUR"
  }).format(invoice.total);
  return t('invoice.line', { date, price });
}
// en-US: "Issued Mar 4, 2026 — Total €120.00"
// de-DE: "Ausgestellt am 04.03.2026 — Gesamt 120,00 €"
```

The amount is formatted in its own currency with that locale's conventions; nothing is converted, and the surrounding sentence is itself a catalog message rather than a template literal.

Note: corrects AC-124 and AC-125 — all formatting goes through locale APIs, and formatting is never silent currency conversion.
