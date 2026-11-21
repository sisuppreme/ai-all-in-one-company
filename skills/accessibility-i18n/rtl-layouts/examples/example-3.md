# Example 3 — Un-isolated product name and price isolated with `<bdi>`

Violates/corrects AC-166, AC-167: embedded opposite-direction runs are isolated so numbers and punctuation land on the correct side, and inherently LTR content (phone numbers, code) keeps `dir="ltr"` inside RTL text.

## Before

```html
<p lang="ar" dir="rtl">
  اطلب Pro Max 12 اليوم مقابل 499 ر.س فقط، أو اتصل على +966 55 123 4567
</p>
```

With no isolation, the bidi algorithm reorders the mixed run: the "12" detaches from the product name, the price digits and currency land on the wrong side of the sentence, and the phone number's digit groups display in scrambled order.

## After

```html
<p lang="ar" dir="rtl">
  اطلب <bdi>Pro Max 12</bdi> اليوم مقابل <bdi>499 ر.س</bdi> فقط،
  أو اتصل على <span dir="ltr">+966 55 123 4567</span>
</p>
```

The product name and the price are isolated with `<bdi>`, so the Arabic sentence orders itself around them; the phone number is wrapped in `dir="ltr"` and reads in its native order. This exact string belongs in the G-AC-083 bidi test set for the product and checkout screens.
