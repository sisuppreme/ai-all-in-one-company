# Example 3 — Styled text vs. a real heading outline

## Before

```html
<p class="font-32 bold">Account settings</p>
<p class="font-24 bold">Change password</p>
<p class="font-24 bold">Two-factor authentication</p>
<p class="font-32 bold">Billing</p>
<p class="font-24 bold">Invoices</p>
```

Everything is a paragraph with size classes. A screen reader's headings list for this page is empty, so a user cannot jump to "Invoices" — they must listen to the whole page linearly to find it.

## After

```html
<h1>Settings</h1>
  <h2>Account</h2>
    <h3>Change password</h3>
    <h3>Two-factor authentication</h3>
  <h2>Billing</h2>
    <h3>Invoices</h3>
```

Visual sizes stay exactly as designed — set by CSS on the heading elements. The headings dialog now reads as a table of contents ("Settings → Account → Change password, Two-factor authentication; Billing → Invoices"), levels nest without skips, and each section is one keystroke away.

*Demonstrates AC-043 — headings are a navigation outline, not font sizing.*
