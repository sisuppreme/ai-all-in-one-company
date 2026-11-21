# Example 1 — From a fashionable pick to a criteria-based decision

## Before

The project README announces: "Database: MongoDB — modern, scalable, used by major platforms." No criteria were listed, no alternative was evaluated, and nobody recorded that the project's dominant queries are relational joins across orders, customers, and payments. The choice was copied from a conference talk.

## After

Criteria are written first: relational integrity for order/payment data, fit for the project's named join queries, team operational experience, managed-hosting availability on the target platform, license, exit cost. PostgreSQL and MongoDB are scored in one table against those criteria; PostgreSQL wins on integrity and query fit, MongoDB's document flexibility is recorded as the losing advantage. ADR-0004 records the decision, the rejected alternative, and the accepted downside (less flexible ad-hoc document storage).

## Note

Corrects AR-041 (selection criteria are written before candidates are named) and AR-043 (adoption happens only through an accepted ADR naming a rejected alternative).
