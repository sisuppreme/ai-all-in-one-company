# Example 2 — Context-free handoff mistranslates a payment button

## Before

A string list goes to the translation vendor as a bare spreadsheet — key, source text, nothing else:

```text
checkout.chargeButton | Charge
```

"Charge" here is the verb on the payment button: tapping it charges the saved card. With no screenshot, no screen reference, and no note, the translator reads it as the noun — a fee — and the machine-translation draft the vendor returns renders it in the target language as the word for a criminal charge/accusation. The string is marked "translated" in the spreadsheet and ships unreviewed. At the payment step — the most trust-sensitive screen in the product — the button effectively accuses the user, and users abandon a working checkout because the label is frightening nonsense.

## After

The handoff ships the string with the context AC-143 requires:

```text
Key:        checkout.chargeButton
Source:     Charge
Appears:    Primary button on the final payment step (screenshot attached:
            checkout-step-3.png). Tapping it charges the saved card and
            completes the order.
Meaning:    Verb — "charge my card now". NOT a fee, NOT an accusation.
Limit:      20 characters (button sits beside a Cancel button of equal width)
Glossary:   "card" = payment card term #G-114; product name on
            do-not-translate list does not appear in this string.
Class:      Payment — native-speaker review mandatory before release.
```

The translator renders the verb form that fits the limit, the string is labeled with its class in the pipeline, and the locale's named reviewer confirms it in context on the staging payment step during the G-AC-074 walk — reading the actual button, in the actual layout, before sign-off.

Note: corrects AC-143, AC-147 — strings ship with screenshots, meaning notes, and character limits, and payment-class strings are native-speaker reviewed; a bare word in a spreadsheet is not a handoff.
