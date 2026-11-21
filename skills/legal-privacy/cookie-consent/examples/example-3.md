# Example 3 — Withdrawal that actually stops the tags

## Before

A visitor who accepted analytics later looks for a way to change their mind. The footer has no cookie link; the only route is an email address in the privacy notice. When support manually flags the account, the banner stops appearing — but the tag manager still loads the analytics tag on every page, because nothing in the loading layer reads the flag. The withdrawal was recorded; it was never honored.

## After

A persistent "Cookie settings" link in the footer reopens the same choices panel in one click. Turning analytics off writes a new consent event (LG-088) and updates the runtime consent state:

```js
// Tag-loading layer: every non-essential tag is gated on consent state.
if (consentState.allows('analytics')) {
  loadTag('analytics');
}
if (consentState.allows('marketing')) {
  loadTag('marketing');
}
```

On the next page load the analytics tag does not fire, and its cookies are deleted. The G-LG-042 matrix run for "withdraw after accept" asserts exactly this: tags present before withdrawal, absent after.

*Violates/corrects LG-089 (withdrawal as easy as giving, effective next load); see also BAN-LG-044.*
