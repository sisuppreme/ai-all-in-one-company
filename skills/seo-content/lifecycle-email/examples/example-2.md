# Example 2 — Sending domain authenticated before the first program

## Before

The onboarding journey is built and scheduled to send from `mail.example.com`. The domain has an SPF record only — no DKIM key, no DMARC record — and the footer unsubscribe link points to a preferences page that requires login. At volume, Gmail begins deferring and then rejecting the mail.

## After

Before any send, the domain is authenticated and the unsubscribe path is fixed:

```
dig +short TXT mail.example.com
  → "v=spf1 include:_spf.provider.example -all"
dig +short TXT s1._domainkey.mail.example.com
  → DKIM public key present
dig +short TXT _dmarc.mail.example.com
  → "v=DMARC1; p=none; rua=mailto:dmarc@example.com" (aligned with From)
Headers: List-Unsubscribe + List-Unsubscribe-Post (RFC 8058 one-click)
Opt-outs: honored within 48 hours, checked in the pre-send audience assertion
```

Note: corrects CO-141 (SPF, DKIM, and aligned DMARC in place before volume, verified by the G-CO-071 DNS check) and CO-152 (one-click unsubscribe, opt-outs honored within 48 hours).
