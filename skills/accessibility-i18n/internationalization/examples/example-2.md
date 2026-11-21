# Example 2 — Concatenated message and `count == 1` plural replaced by one ICU message

## Before

```js
function inboxLabel(count) {
  const noun = count === 1 ? t('messageSingular') : t('messagePlural');
  return t('youHave') + ' ' + count + ' ' + t('new') + ' ' + noun;
}
// "You have" + " " + 3 + " " + "new" + " " + "messages"
```

Two defects in four lines: the sentence is glued from fragments, so a locale with different word order produces garbled output; and the plural is chosen by an English-only `count === 1` branch, so locales with more CLDR categories (Polish: one/few/many/other; Arabic: six) get grammatically wrong forms.

## After

One catalog message, translated as a unit; the count is passed raw and CLDR categories select the form:

```json
{
  "inbox": {
    "unread": "You have {count, plural, one {# new message} other {# new messages}}.",
    "_unread_comment": "Inbox header. {count} is the number of unread messages; the plural form is chosen per locale by CLDR rules."
  }
}
```

```js
function inboxLabel(count) {
  return t('inbox.unread', { count });
}
```

The translator for each locale writes that locale's full set of plural forms inside the message — the code never learns how many forms exist.

Note: corrects AC-122 and AC-123 — whole messages are the unit of translation, and plurals come from CLDR categories, never from code branches.
