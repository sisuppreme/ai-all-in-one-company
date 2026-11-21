# Example 3 — The trail everyone could read

## Before

The audit trail is exposed at an internal `/admin/audit` page that every staff login can open — support, contractors, interns — and opening it records nothing. The trail names who was erased, who consented, and which admin viewed which customer's data, so the most sensitive metadata in the product is browsable by the whole company with no record of who looked.

## After

Trail access is restricted to the two roles named in the project file (privacy lead, compliance reviewer). Every open, search, and export writes its own trail entry naming the reader and the query scope, and an access attempt by any other role is refused and logged. A quarterly access audit confirms the role list still matches the project file.

*Demonstrates LG-168 — access to the trail is restricted, and reading the trail is itself a trailed act.*
