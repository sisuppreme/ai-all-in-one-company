# Example 2 — Revenue LTV in disguise

## Before

Board deck:

> "LTV: $4,000 (ARPA $120/month ÷ 3% monthly churn). CAC: $1,000. LTV:CAC = 4.0 — comfortably above the 3.0 bar."

The LTV is revenue-based: it assumes every dollar of revenue is profit. Gross margin is 75%, so a quarter of that "LTV" is spent delivering the service.

## After

Margin-based LTV under PR-222, same inputs:

- Average revenue per account: $120/month
- Gross margin: 75% → monthly gross profit per account = $120 × 0.75 = **$90**
- Monthly churn: 3% → expected lifetime = 1 ÷ 0.03 ≈ 33.3 months
- **LTV = $90 × 33.3 ≈ $3,000** (equivalently, $120 × 0.75 ÷ 0.03 = $3,000)

Revised ratio and payback, reported together (PR-223):

- LTV:CAC = $3,000 ÷ $1,000 = **3.0** — at the heuristic bar, not comfortably above it
- CAC payback = $1,000 ÷ $90 ≈ **11.1 months** — just inside the 12-month heuristic

The decision changes: instead of "comfortably above the bar, scale," the honest read is "at the bar on both measures — improve margin or churn before scaling spend."

## Note

Corrected under PR-222: LTV = average revenue per account × gross margin ÷ churn rate. Revenue-based LTV is never reported as LTV.
