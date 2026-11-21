# Example 2 — Blaming, coded error replaced by field, problem, and fix

## Before

```
Error 422: Invalid input. You failed to enter a valid date.
Please correct the fields shown in red and try again.
```

The message blames the user, cites a code that means nothing to them, and locates the problem by color alone. The required format is nowhere stated — the user discovers it only by failing again. Their other entries are cleared when the form reloads, so they also lose work.

## After

Field, shown before entry:

```
Start date
Format: DD/MM/YYYY — for example, 03/04/2026
[ 03/13/2026 ]
```

Error, attached to the field after a failed submit (the user's other entries are kept):

```
Start date — the month "13" is not valid. Dates here use DD/MM/YYYY,
so 3 April 2026 is written 03/04/2026.
```

The error names the field, states the problem in the user's terms, and gives the fix with an example — no blame, no code, no color reference. The format hint was also present before entry, so most users never trigger the error at all.

Note: corrects AC-184 and AC-185 — error copy names the field, the problem, and the fix, and format requirements are stated before the control, not revealed by failure.
