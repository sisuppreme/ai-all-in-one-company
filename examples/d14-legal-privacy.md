# D14 Legal & Privacy — End-to-End Example

## Scenario

"NoteNest," a small note-taking SaaS selling into the EU and the US, adds analytics,
a cookie banner, a privacy notice, and a "delete my account" flow before launch.
The legal surface has to be built from the product's own data inventory — and every
promise the notice makes has to be backed by a working process.

## Before — the slop version

```html
<!-- analytics + marketing tags pasted into <head>: they fire on first load -->
<script src="https://analytics.example/track.js"></script>
<script src="https://ads.example/pixel.js"></script>

<!-- cookie banner -->
<div class="banner">
  <p>We value your privacy. We only track with your consent.</p>
  <label><input type="checkbox" checked> Analytics</label>
  <label><input type="checkbox" checked> Marketing</label>
  <button>Accept all</button>   <!-- Reject lives two layers deep, in Settings -->
</div>

<footer>100% GDPR Compliant ✓</footer>
```

```js
// "Delete my account"
await db.query('UPDATE users SET visible = false WHERE id = ?', [userId]);
res.render('deleted', { message: 'Your account has been deleted.' });
```

What is wrong, visibly: the trackers fire before any consent exists while the copy
claims the opposite; both toggles start pre-ticked; rejecting is harder than
accepting; a compliance badge is published with no tested process behind it; and
"deletion" only hides the record, which stays queryable in the database, search
index, and admin views.

## What the skills caught

- **BAN-LG-043 — Trackers loaded before consent** (defeats DET-CON-015). **LG-083**:
  enforcement lives in the tag-loading layer — nothing non-essential fires until a
  consent state allowing that purpose exists. Banner copy is not enforcement.
- **BAN-LG-041 — Pre-ticked toggles** (defeats DET-NONE — no DET parameter names
  this signal; pattern owned by the cookie-consent skill). **LG-085**: every toggle
  starts off; consent is a positive action (the *Planet49* judgment, C-673/17).
- **BAN-LG-042 — Decorative reject** (defeats DET-CON-028). **LG-084**: accept,
  reject, and granular purposes sit on the first layer at equal prominence.
- **BAN-LG-001 — Compliance claimed without a tested process** (defeats
  DET-CON-012). **LG-011**: the skill never declares a product "GDPR compliant";
  publish only what a dated audit artifact proves, worded as what was tested.
- **BAN-LG-021 — Delete that only hides** (defeats DET-FAKE-011). **LG-050**:
  erasure deletes or irreversibly anonymizes the subject's records in the primary
  store, indexes, analytics, and file storage, and instructs every processor to
  delete — proven by a residue check, not by a confirmation screen.
- **LG-001 / LG-004** frame the whole fix: the obligations register derives from
  this product's own data map (markets × data categories × purposes, each with a
  lawful basis and retention period) — never from a template copied from another
  product (BAN-LG-002).

## After — the corrected version

Consent and erasure, rebuilt from the inventory (LG-081: inventory before banner;
LG-091: inventory, banner, and notice generated from one dataset):

```js
// Tag layer: the ONLY place third-party tags load (LG-083, LG-092)
function loadTags(consent) {
  if (consent.purposes.analytics) loadAnalytics();       // strictly-necessary
  if (consent.purposes.marketing) loadMarketingPixel();  // tags need no consent
}                                                        // and load without it

// Banner state on first render: every purpose OFF (LG-085),
// Accept / Reject / per-purpose choices on the first layer (LG-084, LG-087).
// Each choice is stored as a record — subject ID, timestamp, banner version,
// per-purpose choices (LG-088) — and withdrawal reopens the same control
// in the same number of steps (LG-089).
```

```js
// Erasure executes across every store the register names (LG-050, LG-047)
await eraseSubject(userId, {
  stores: ['primary-db', 'search-index', 'analytics', 'file-storage'],
  processors: processorRegister.forSubject(userId),   // each files a confirmation
  backups: 'suppress now; delete at documented rotation',  // LG-051
});
await residueCheck(userId);   // export, admin search, and indexes return nothing
logRequest({ type: 'erasure', outcome: 'delivered', closedAt: now() });  // LG-052
```

The footer badge is gone. In its place, the privacy notice states only what the
register and a dated check support — and the DSAR intake behind it is a real
state machine with a clock computed from the regime table in the project file
(LG-041, LG-043), not an unmonitored inbox (BAN-LG-004).

## Skills used

- [privacy-laws](../skills/legal-privacy/privacy-laws/SKILL.md)
- [cookie-consent](../skills/legal-privacy/cookie-consent/SKILL.md)
- [dsar-handling](../skills/legal-privacy/dsar-handling/SKILL.md)
- [legal-documents](../skills/legal-privacy/legal-documents/SKILL.md)
