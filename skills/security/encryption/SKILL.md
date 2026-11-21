# encryption

## Metadata

- **Owner department:** D7 Security (SE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** OWASP Cryptographic Storage Cheat Sheet and Transport Layer Protection Cheat Sheet, https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html ; Mozilla SSL Configuration Generator, https://ssl-config.mozilla.org/
- **Depends on:** secrets-management, auth-hardening
- **Feeds into:** security-audit, pci-compliance, api-security

## When to use / Do NOT use

- **Use when:** choosing or reviewing how data is encrypted in transit or at rest — TLS configuration, field or file encryption, key storage, certificate lifecycle — in any application this repo builds.
- **Do NOT use when:** the question is password verification parameters (use auth-hardening) or where secret values live day to day (use secrets-management); this skill owns the constructions and the transport profile, they own those surfaces.

## Rules

1. **SE-141 — Standard constructions only.** Every cipher, mode, and protocol comes from a maintained library as a standard option; no hand-designed cipher, protocol, key exchange, or obfuscation scheme ships. If the library does not offer it as a standard option, the design is wrong.
2. **SE-142 — TLS 1.2 minimum, 1.3 preferred.** The deployed TLS configuration is generated from a maintained profile (Mozilla SSL Configuration Generator, Intermediate or stricter) and the generated file is committed; TLS 1.0/1.1 and obsolete cipher suites are disabled (DET-INF-015).
3. **SE-143 — HTTP redirects, HSTS after proof.** Every HTTP request 301-redirects to HTTPS on every route including APIs; HSTS is enabled only after HTTPS is verified working on all hosts, and the decision is recorded (DET-INF-014).
4. **SE-144 — Certificates renew automatically.** Certificates are ACME-issued or provider-managed with unattended renewal proven by a dry run at setup; an expiry alert fires weeks before the expiry date as a backstop, never as the mechanism (DET-INF-016).
5. **SE-145 — AEAD at rest.** Sensitive data at rest is encrypted with an AEAD construction — AES-256-GCM or ChaCha20-Poly1305 — through the platform or library API; unauthenticated modes and hand-assembled encrypt-then-MAC do not ship.
6. **SE-146 — Fresh random nonce per message.** Every AEAD encryption generates a new random nonce/IV from the library's CSPRNG and stores it with the ciphertext; a nonce is never constant, derived from the key alone, or reused under the same key.
7. **SE-147 — Keys come from a key store, never from code.** Encryption keys are generated and held by a KMS or platform key store; no key material appears in source, committed config, environment files in the repo, or the same store as the ciphertext it protects (DET-CODE-018).
8. **SE-148 — Envelope encryption for per-record keys.** Where individual records or tenants need their own keys, a data key encrypts the record and is itself stored encrypted under the key-store master key; master keys never leave the key store.
9. **SE-149 — Key access is logged and rotation is planned.** Every key use by the application is attributable in logs (key ID, caller, time — never key material), and each key has a recorded rotation path that re-wraps or re-encrypts without downtime.
10. **SE-150 — Passwords are hashed, never encrypted.** Passwords go through a dedicated password KDF per auth-hardening (Argon2id first choice per the OWASP Password Storage Cheat Sheet); reversible encryption of passwords does not ship, because anyone with the key recovers every password.
11. **SE-151 — Tokens are stored hashed.** Session tokens, API reset links, and similar bearer secrets are stored as hashes and compared against the hash of the presented value, so a database leak does not hand out working tokens.
12. **SE-152 — No downgrade path.** Sensitive traffic has no plaintext fallback: a failed TLS handshake, an expired certificate, or an unreachable key store fails the operation closed — it never retries over HTTP, skips verification, or serves the data unencrypted.

## BAN list

- **BAN-SE-071 — Banned primitives and modes.** Banned: ECB mode, static or zero IVs, MD5 or SHA-1 for any security purpose, or a home-grown cipher/obfuscation routine. Defeats: DET-CODE-020. Bad: `createCipheriv("aes-256-ecb", key, null)` for customer records. Instead: use an AEAD construction — `createCipheriv("aes-256-gcm", key, randomBytes(12))` — and a current hash where a hash is the right tool. Severity: BLOCK.
- **BAN-SE-072 — Plaintext or unverified transport.** Banned: serving any route over HTTP without redirect, calling an internal API over `http://`, or disabling certificate verification to make a call succeed. Defeats: DET-INF-014. Bad: `fetch("http://billing.internal/charge")` because the internal cert had expired. Instead: renew the certificate, call the `https://` endpoint with verification on, and let the call fail closed until transport is sound. Severity: BLOCK.
- **BAN-SE-073 — Weak TLS profile or mixed content.** Banned: enabling TLS 1.0/1.1 or obsolete ciphers for compatibility, or loading any script, image, or API call over `http://` on an HTTPS page. Defeats: DET-INF-015. Bad: server profile keeps `TLSv1` enabled "for old clients" with no exception record. Instead: ship the Mozilla Intermediate profile (TLS 1.2+); a genuine legacy need gets a written exception with an expiry date, never silent acceptance. Severity: BLOCK.
- **BAN-SE-074 — Manually tended certificates.** Banned: a certificate installed by a one-off manual step with no auto-renewal configured and no expiry alert. Defeats: DET-INF-016. Bad: a Certbot run done once at launch; the cert expires 90 days later and the site goes down. Instead: enable the ACME client's unattended renewal (or the provider's managed certificate), prove it with a renewal dry run, and set an expiry alert weeks ahead. Severity: BLOCK.
- **BAN-SE-075 — Keys beside the data.** Banned: an encryption key stored in source code, a committed config file, or the same database/volume as the ciphertext it protects. Defeats: DET-CODE-018. Bad: `FIELD_KEY = "9f2c…"` in `config.py`, committed next to the encrypted columns it unlocks. Instead: hold the key in the KMS or platform key store, reference it by key ID, and log every access. Severity: BLOCK.

## Gates

- **G-SE-071 — TLS profile scan.** Verifies: SE-142, SE-143, SE-152. Check: run `testssl.sh https://<prod-domain>` (or SSL Labs) against the deployed endpoint each release and archive the report. Pass: TLS 1.2+ only, no obsolete ciphers, HTTP 301-redirects to HTTPS, HSTS present. Fail: block shipment. Recorded in: progress.md.
- **G-SE-072 — Banned-primitive scan (automated).** Verifies: SE-141, SE-145. Check: `grep -rnEi "aes-[0-9]+-ecb|createCipher\(|md5|sha1|DES|RC4" src/` plus the SAST crypto ruleset in CI, and a manual read of every hit. Pass: zero hits in security-relevant code (checksums of public files with a recorded reason are the only exception). Fail: block shipment. Recorded in: progress.md.
- **G-SE-073 — Certificate lifecycle check (automated).** Verifies: SE-144. Check: `echo | openssl s_client -connect <prod-domain>:443 -servername <prod-domain> 2>/dev/null | openssl x509 -noout -dates` and confirm the renewal mechanism (ACME timer or provider setting) and expiry alert exist. Pass: more than 30 days of validity remaining, auto-renewal configured, alert rule present. Fail: block shipment. Recorded in: progress.md.
- **G-SE-074 — Key custody review.** Verifies: SE-147, SE-148, SE-149. Check: manual, checklist-driven — list every encryption key in the system; for each, name its key-store location, who/what can use it, its access log, and its rotation path; grep the repo for key-shaped strings as a cross-check. Pass: every key lives in a key store, separated from its ciphertext, logged, and rotatable. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Encryption theater.** Data is "encrypted at rest" by the disk or platform default while application-level secrets sit in plaintext columns. Catch it: ask which fields the application itself encrypts; if the answer is "the volume handles it," sensitive fields are unprotected against a database leak.
- **Nonce reuse by convenience.** A fixed IV constant sits at the top of the crypto module because per-message randomness "complicated the format." Catch it: search for IV/nonce literals; under GCM, one reused nonce pair breaks confidentiality of both messages.
- **Encrypting passwords "for recovery."** Passwords are reversibly encrypted so support can "look them up." Catch it: any decrypt path for a password column means a key holder — or a key thief — recovers every user's password, including ones reused elsewhere.
- **Verify-off debugging left in.** `rejectUnauthorized: false` or `verify=False` was added to get past a staging certificate error and rode along to production. Catch it: the G-SE-072 scan and a production-config read; the fix is always the certificate, never the check.

## Examples

- [Example 1 — AEAD field encryption with a fresh nonce](examples/example-1.md) — violates/corrects SE-145, SE-146 (BAN-SE-071).
- [Example 2 — Key held by the key store, not the code](examples/example-2.md) — violates/corrects SE-147 (BAN-SE-075).
- [Example 3 — HTTPS-only internal call that fails closed](examples/example-3.md) — violates/corrects SE-143, SE-152 (BAN-SE-072).

## Recall anchors

- Library constructions only — if it is not a standard option, the design is wrong.
- AEAD, fresh random nonce, every single message.
- Keys live in the key store, never beside the data they protect.
- Passwords are hashed; tokens are hashed; only data is encrypted.
- Renewal is automated and proven; the expiry alert is only the backstop.

## Checklist

- [ ] TLS profile is generated from the Mozilla profile and committed; scan shows TLS 1.2+ only (SE-142, G-SE-071).
- [ ] HTTP redirects to HTTPS everywhere and HSTS is on, with the decision recorded (SE-143).
- [ ] Certificate auto-renewal is configured and dry-run proven; expiry alert exists (SE-144, G-SE-073).
- [ ] At-rest encryption is AEAD with a fresh random nonce per message (SE-145, SE-146).
- [ ] Banned-primitive scan returns zero security-relevant hits (G-SE-072).
- [ ] Every key is in a key store, separated from its ciphertext, access-logged, and rotatable (SE-147–SE-149, G-SE-074).
- [ ] Passwords and stored tokens are hashed, never reversibly encrypted (SE-150, SE-151).
- [ ] No plaintext or verification-off fallback exists in any sensitive path (SE-152).
