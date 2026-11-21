# media-processing

## Metadata

- **Owner department:** D4 Backend & APIs (BE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** OWASP File Upload Cheat Sheet (image re-encoding, parser-exploit and decompression threats), https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html
- **Depends on:** file-uploads, queues-jobs
- **Feeds into:** api-building, admin-tools

## When to use / Do NOT use

- **Use when:** uploaded media must be transformed before use — thumbnails, image re-encoding, video transcodes, waveform/OCR/metadata extraction — or when an asset pipeline's states and failures need to be made honest.
- **Do NOT use when:** the work is accepting and storing the upload itself (file-uploads), or generic background-job mechanics unrelated to media (queues-jobs).

## Rules

1. **BE-241 — Off the request path.** All processing runs as queued jobs. The upload request returns once the asset is registered in a quarantine state; it never waits for a thumbnail, transcode, or extraction to finish.
2. **BE-242 — Quarantine until processed.** An asset is not publishable until its processing job has succeeded and produced the normalized master and required derivatives. Quarantined assets are not served to end users.
3. **BE-243 — Re-encode images.** Images are decoded and re-encoded into an allowed format. Re-encoding is also the sanitation step: embedded payloads and metadata not meant to ship do not survive it.
4. **BE-244 — Resource limits.** Processing runs with explicit time, memory, and pixel/frame caps. Inputs that exceed the caps are rejected as a class; they are never attempted "to see if it works."
5. **BE-245 — Fixed rendition ladder.** Video transcodes target a fixed, documented ladder of renditions for adaptive delivery through the CDN. Renditions are not invented per upload.
6. **BE-246 — Recipe provenance.** Every derivative records its source object, the recipe version that produced it, and its status. A derivative whose origin cannot be stated is treated as corrupt.
7. **BE-247 — Honest failure.** A failed job leaves the asset in a visible failed state with a retry path. The raw original is never silently served in place of the derivatives that failed to appear.
8. **BE-248 — State from the job record.** User-visible state (processing, ready, failed) is read from real job state. No timer, delay, or client-side guess may stand in for it.
9. **BE-249 — Metadata by policy.** EXIF location data is stripped from user photos by default. Handling of other document and media metadata is set per product in writing, not inherited from a library default.
10. **BE-250 — Regenerable derivatives.** The stored original plus its recipe must be able to reproduce every served rendition. Reprocessing after a recipe change is a batch job over the provenance records, not a manual hunt.

## BAN list

- **BAN-BE-121 — The silent fallback to raw.** Banned: serving the unprocessed original when processing fails, with no visible failure state. Defeats: DET-CODE-005. Bad: the transcode throws, the catch block logs "oops," and the page serves the 2 GB raw upload as if it were the finished video. Instead: the asset stays visibly failed with a retry path (BE-247). Severity: BLOCK.
- **BAN-BE-122 — Unbounded processing.** Banned: decoding or transcoding user media with no time, memory, or pixel/frame caps. Defeats: DET-CODE-033. Bad: a decompression-bomb image expands until it kills the worker processing everyone's uploads. Instead: enforce caps and reject over-cap inputs before decoding (BE-244). Severity: BLOCK.
- **BAN-BE-123 — Location data shipped.** Banned: publishing user photos with EXIF GPS coordinates intact by default. Defeats: DET-CODE-020. Bad: profile photos quietly leak their owners' home addresses through embedded coordinates. Instead: strip location metadata by default; any exception is a written product decision (BE-249). Severity: BLOCK.
- **BAN-BE-124 — The lying progress state.** Banned: showing an asset as "ready," or animating a progress bar on a timer, before its processing job has actually completed. Defeats: DET-FAKE-022. Bad: the UI flips to Ready after three seconds while the transcode is still queued behind other jobs. Instead: read the state from the job record (BE-248). Severity: BLOCK.

## Gates

- **G-BE-121 — Golden-file test.** Verifies: BE-242, BE-245, BE-246. Check: automated — a fixed input set is processed in staging; assert every derivative matches the expected dimensions, formats, and duration, and that each carries a provenance row with source and recipe version. Pass: all match. Fail: block shipment. Recorded in: progress.md.
- **G-BE-122 — Bomb-resistance test.** Verifies: BE-244. Check: automated in staging — submit a decompression-bomb fixture and an over-cap video; assert both are rejected within the resource limits and the worker is alive and processing normally afterward. Pass: rejected, worker healthy. Fail: block shipment. Recorded in: progress.md.
- **G-BE-123 — Failure-state drill.** Verifies: BE-247, BE-248. Check: automated — submit a corrupt input that cannot transcode; assert the asset shows a failed state with a retry action and the raw original is not served at the derivative's URL. Pass: both hold. Fail: block shipment. Recorded in: progress.md.
- **G-BE-124 — Metadata strip check.** Verifies: BE-243, BE-249. Check: automated — process a photo carrying GPS EXIF data; assert the published derivative contains no location tags. Pass: no GPS data present. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Recipe archaeology.** Derivatives exist across the bucket, but nobody can say which settings produced any of them. Catch it: sample one derivative and demand its provenance row; a shrug is the finding.
- **The quarantine leak.** Assets marked unprocessed are still reachable by guessing their storage URL, so "quarantine" is a label, not a state. Catch it: request a quarantined asset as an anonymous user.
- **The poison-file loop.** A file that always crashes the processor is retried forever, re-killing workers on every attempt. Catch it: check attempt caps and what happens to a job that fails identically three times.
- **Thumbnail-only testing.** The pipeline is verified on one small JPEG and declared done; video, huge images, and odd formats were never run. Catch it: compare the test fixture list against the formats the product accepts.

## Examples

- [Example 1 — Failed transcode silently serving the raw file](examples/example-1.md) — corrects BE-247.
- [Example 2 — Uncapped decode replaced by capped decode and re-encode](examples/example-2.md) — corrects BE-243, BE-244.
- [Example 3 — EXIF-carrying photo replaced by a stripped, provenanced derivative](examples/example-3.md) — corrects BE-246, BE-249.

## Recall anchors

- Processing is a job, never a request.
- Nothing publishes from quarantine.
- Caps first: over-limit media is rejected, not attempted.
- Failure is a visible state with a retry, never a silent raw file.
- Every derivative can name its source and recipe.

## Checklist

- [ ] Processing runs from the queue; the upload request returns at quarantine (BE-241).
- [ ] Assets are unpublishable until their job succeeds (BE-242).
- [ ] Golden-file test green, provenance rows present (G-BE-121).
- [ ] Bomb and over-cap fixtures rejected, worker unharmed (G-BE-122).
- [ ] Forced failure shows a failed state; raw original not served (G-BE-123).
- [ ] Published photos carry no location metadata (G-BE-124).
- [ ] Rendition ladder is the documented one, not per-upload inventions (BE-245).
