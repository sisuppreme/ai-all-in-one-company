# Example 3 — Mail sent before its records existed

Demonstrates DO-206: SPF, DKIM, and DMARC ship with the domain setup.

## Before

The domain is pointed at the host and the app starts sending signup and
password-reset mail the same day. No SPF, DKIM, or DMARC records exist.
Receiving providers cannot verify the mail, reset messages land in spam, and
the fix only starts after users report missing emails — diagnosed as an app
bug first, because nobody checked DNS.

## After

Mail authentication is part of the domain setup, before the first send:

```
@              TXT  "v=spf1 include:_spf.mailprovider.example -all"
<selector>._domainkey  TXT  "v=DKIM1; k=rsa; p=<public-key-from-provider>"
_dmarc         TXT  "v=DMARC1; p=none; rua=mailto:dmarc@example.com"
```

The DKIM selector and key come from the sending provider's own setup page,
not from a tutorial. Verification before any mail is sent:
`dig +short example.com TXT`, `dig +short <selector>._domainkey.example.com TXT`,
and `dig +short _dmarc.example.com TXT` each return their record. The DMARC
policy starts at `p=none` for reporting and is tightened once reports show
all legitimate senders aligned.
