# file-uploads

## Metadata

- **Owner department:** D4 Backend & APIs (BE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** OWASP File Upload Cheat Sheet, https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html ; AWS S3 presigned URLs, https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html
- **Depends on:** backend-auth, validation, queues-jobs
- **Feeds into:** media-processing, admin-tools

## When to use / Do NOT use

- **Use when:** users upload files of any kind — avatars, documents, attachments, imports — or when reviewing an existing upload flow for safety and honesty.
- **Do NOT use when:** the file never leaves the server that generated it (server-side exports are api-building plus data-access), or for what happens to media after upload — derivatives and transcodes are media-processing.

## Rules

1. **BE-221 — Presigned direct upload.** The app server authenticates the user, registers the upload intent, and issues a short-lived presigned URL; bytes flow from the client directly to private object storage. The database stores metadata and the object key only, never file contents.
2. **BE-222 — Completion means stored.** An upload is complete only when the object exists in storage (verified by a storage existence check) and the metadata row points at its key. A client-side preview or progress bar is never evidence of completion.
3. **BE-223 — Layered validation.** Every upload passes, in order: authenticated user, size cap, extension allowlist checked on the decoded filename, and content signature sniffing. The client-supplied Content-Type is never trusted as evidence of type.
4. **BE-224 — Generated stored names.** Stored object names are server-generated (UUID or equivalent). The original filename is kept as display metadata only and never reaches a filesystem path or object key.
5. **BE-225 — Private by default.** Buckets and storage containers are private. Downloads are authorized per request and served through a signed URL or a handler that maps an opaque ID to the object after an authorization check.
6. **BE-226 — Inert where served.** Uploads are stored outside any executable path and served with a safe Content-Type and `Content-Disposition`; user content is never rendered as active content from the application's own origin.
7. **BE-227 — Limits at the storage layer.** Size and type limits are encoded in the presigned policy as well as enforced in code, so a forged direct upload that bypasses the application still fails at storage.
8. **BE-228 — Scan before visible.** A malware scan completes before an uploaded file becomes visible or downloadable to anyone, including the uploader's audience. Unscanned files stay in a quarantined state.
9. **BE-229 — Orphan reaping.** Uploads never attached to a record are reaped by a scheduled job on a documented threshold; abandoned bytes are not kept forever.
10. **BE-230 — State is read, not assumed.** Upload states shown anywhere (pending, stored, scanned, failed) are read from the storage and metadata records, never inferred from what the client claims happened.

## BAN list

- **BAN-BE-111 — The discarding upload.** Banned: an upload flow that previews the file locally and reports success without storing it server-side. Defeats: DET-FAKE-012. Bad: the avatar upload shows a preview from a `blob:` URL and toasts "Upload successful"; after reload the placeholder returns. Instead: presigned upload to storage plus a metadata row, complete only when the object exists (BE-221, BE-222). Severity: BLOCK.
- **BAN-BE-112 — Content-Type trust.** Banned: accepting a file because the client-supplied Content-Type or extension claims a safe type, with no signature sniffing. Defeats: DET-CODE-019. Bad: `if (file.mimetype === 'image/png') save(file)` lets a script renamed `.png` straight through. Instead: allowlist the extension on the decoded name and sniff the content signature (BE-223). Severity: BLOCK.
- **BAN-BE-113 — User-named public storage.** Banned: storing uploads under the original filename in a public bucket or a web-served executable folder. Defeats: DET-CODE-020. Bad: the file lands at `/public/uploads/report.pdf` — guessable by anyone, and a crafted name traverses paths. Instead: generated names in a private bucket, downloads via signed URL (BE-224, BE-225). Severity: BLOCK.
- **BAN-BE-114 — The uncapped upload.** Banned: an upload path with no size limit enforced in code and in the presigned policy. Defeats: DET-CODE-033. Bad: the UI hints "max 10 MB" but a 4 GB direct upload exhausts the bucket because nothing enforces the cap. Instead: enforce the cap at both layers (BE-227). Severity: BLOCK.

## Gates

- **G-BE-111 — Upload round-trip.** Verifies: BE-221, BE-222, BE-225. Check: automated script — upload a uniquely named file through the real flow, HEAD the bucket object, assert the metadata row holds the key and no contents, assert an unauthenticated GET is denied, and assert the signed URL stops working after expiry. Pass: all assertions hold. Fail: block shipment. Recorded in: progress.md.
- **G-BE-112 — Hostile-file pack.** Verifies: BE-223, BE-227. Check: automated test pack — double extension, spoofed Content-Type, oversized file, and a polyglot file are each submitted; assert every one is rejected. Pass: zero accepted. Fail: block shipment. Recorded in: progress.md.
- **G-BE-113 — Path and bucket scan.** Verifies: BE-224, BE-225, BE-226. Check: automated — grep the codebase for original-filename use in path or key construction, and scan storage configuration for public-read policies. Pass: no hits. Fail: block shipment. Recorded in: progress.md.
- **G-BE-114 — Quarantine and reaper review.** Verifies: BE-228, BE-229. Check: manual step in staging — upload a file, confirm it is not downloadable before its scan completes, then inspect the reaper job's log and confirm orphans past the threshold are gone. Pass: both confirmed. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **The two-step mirage.** The metadata row is created, the object upload silently fails, and the record points at nothing. Catch it: the round-trip check reads the object from storage, not the row.
- **Preview-equals-proof.** The flow is "tested" by watching the in-browser preview render and calling upload done. Catch it: reload and open the asset in a private window before accepting.
- **The eternal presign.** Presigned URLs carry day-long expiries and are pasted into pages and emails. Catch it: read the policy expiry values; minutes are normal, days are a finding.
- **Scan theater.** A scanner is wired in, but its result never gates visibility, so infected files publish anyway. Catch it: trace one unscanned file and try to download it.

## Examples

- [Example 1 — The avatar upload that discarded the file](examples/example-1.md) — corrects BE-221, BE-222.
- [Example 2 — Content-Type trust replaced by layered validation](examples/example-2.md) — corrects BE-223.
- [Example 3 — Public folder and original names replaced by generated keys](examples/example-3.md) — corrects BE-224, BE-225.

## Recall anchors

- Bytes go client → storage directly; the app only authorizes and registers.
- Complete means the object exists and the row points at it.
- Never trust the client's Content-Type; sniff the signature.
- Stored names are generated; original names are display metadata.
- Private bucket, signed downloads, scan before visible.

## Checklist

- [ ] Presigned flow in place; database holds metadata and key only (BE-221).
- [ ] Completion verified against storage, not the client's progress bar (BE-222).
- [ ] Layered validation passes the hostile-file pack (G-BE-112).
- [ ] No original filename reaches a path or key; bucket is private (G-BE-113).
- [ ] Size and type limits enforced in the presigned policy too (BE-227).
- [ ] Unscanned files are not downloadable; orphans are reaped (G-BE-114).
- [ ] Upload round-trip gate green (G-BE-111).
