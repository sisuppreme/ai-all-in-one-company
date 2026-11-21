# Example 1 — Analytics SDK added with no transfer mechanism

## Before

A product-analytics SDK is added to the web app to track signups. The transfer register gains a row filled in from the vendor's marketing page:

| Processor | Data received | Locations | Mechanism |
|---|---|---|---|
| Analytics vendor | Page views, signup events, IP addresses | "Global" | GDPR compliant (see vendor site) |

The vendor in fact processes and stores event data in the United States. No DPA or SCCs have been signed, no adequacy check was done, and the privacy notice is never updated.

## After

The integration is paused until the register row is real:

| Processor | Data received | Locations | Mechanism |
|---|---|---|---|
| Analytics vendor | Page views, signup events, IP addresses | Processed and stored: United States | No adequacy decision relied on for this flow; SCCs (2021, controller-to-processor module) signed and stored with the register; transfer impact assessment dated and on file |

Only then is the SDK enabled, and the privacy notice's processor list is updated from the same register row.

*Corrects LG-022 (register row with a named mechanism before integration) and LG-024 (SCCs as documents, not checkboxes).*
