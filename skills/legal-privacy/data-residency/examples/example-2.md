# Example 2 — "Data never leaves the EU" vs. a US log sink

## Before

The pricing page carries the line: **"Your data never leaves the EU."**

The claim was written when only the primary database existed, and it is in the EU. Since then the team added an error tracker whose reports (stack traces, request URLs, user IDs) are stored in a US region, and support agents in a third country can view account data through the helpdesk. Neither appears in the inventory, and the claim was never re-checked.

## After

The G-LG-013 inventory enumeration surfaces the error tracker and the helpdesk access. The team chooses to keep the tools, so the claim is deleted and replaced with a statement the register can prove:

**"Your account data is stored in the EU. Some support and diagnostic tools process limited data outside the EU under the safeguards listed in our privacy notice."**

The error tracker and the support-access locations get register rows with named mechanisms, and the privacy notice's transfer section is generated from those rows.

*Corrects LG-027 (residency claims must be provable from the register and config, or deleted) and LG-029 (support access is a transfer).*
