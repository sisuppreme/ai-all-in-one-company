# Example 1 — Hard-coded checkout strings externalized

## Before

```jsx
function DeleteAccountDialog() {
  return (
    <div role="alertdialog">
      <h2>Delete your account?</h2>
      <p>This cannot be undone. All your projects will be permanently removed.</p>
      <button>Cancel</button>
      <button className="danger">Delete account</button>
    </div>
  );
}
```

Every string is a literal in the component. The rest of the settings screen renders from the catalog, so in the German build this dialog — the most destructive one in the product — stays in English, and no translator ever sees it.

## After

```jsx
function DeleteAccountDialog() {
  const t = useTranslations('settings.deleteDialog');
  return (
    <div role="alertdialog">
      <h2>{t('title')}</h2>
      <p>{t('body')}</p>
      <button>{t('cancel')}</button>
      <button className="danger">{t('confirm')}</button>
    </div>
  );
}
```

Catalog entry (source locale), with the context note AC-131 requires:

```json
{
  "settings": {
    "deleteDialog": {
      "title": "Delete your account?",
      "_title_comment": "Heading of the delete-account confirmation dialog in Settings > Danger zone.",
      "body": "This cannot be undone. All your projects will be permanently removed.",
      "cancel": "Cancel",
      "confirm": "Delete account",
      "_confirm_comment": "Button that permanently deletes the account. Keep it short; shown next to Cancel."
    }
  }
}
```

Note: corrects AC-121 — every user-facing string lives in a message catalog keyed by meaning; no literal remains in the component.
