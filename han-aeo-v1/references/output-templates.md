# Output Templates

Use these four lightweight records. Keep change work separate from later observations by using independent status fields.

Use these four fields in every record:

- **Confidence:** `verified`, `inference`, or `hypothesis`.
- **Change status:** `not-applicable`, `proposed`, `implemented-locally`, or `deployed`.
- **Observation status:** `not-measured`, `observing`, or `observed`.
- **Source:** a specifically named source, such as `owner`, `repository`, `live-site`, `platform-data`, `official-docs`, `analytics-export`, or `search-results`; include its date.

Keep approval status (`pending`, `approved`, or `not-required`) as a separate field.

## 1. Project Brief

```markdown
# Project Brief

Date: YYYY-MM-DD
Task ID: TASK-000
Owner:
Project / example domain:
Approval scope:
Approval status: pending / approved / not-required

Goal:
Known facts (source + date):
Unknowns and guardrails:
Baseline to capture before changes:

| Claim ID | Claim | Source + date | Confidence | Change status | Observation status | Approval status |
|---|---|---|---|---|---|---|
| CLM-001 |  |  |  |  |  | pending |

Confidence: verified / inference / hypothesis
Change status: not-applicable / proposed / implemented-locally / deployed
Observation status: not-measured / observing / observed
Source: repository: [path] — YYYY-MM-DD
```

## 2. Proposal, Approval, and Backlog

```markdown
# Proposal / Approval / Backlog

Date: YYYY-MM-DD
Task ID: TASK-000
Owner:
Approval scope: pages, claims, schema, release, or observation only
Approval status: pending / approved / not-required
Baseline reference:

| Priority | Proposed item | Existing or proposed page | Evidence (source + date) | Effort/risk | Approval |
|---|---|---|---|---|---|
| High |  |  |  | Low / Medium / High | pending |

Decision and approver:
Confidence: verified / inference / hypothesis
Change status: not-applicable / proposed / implemented-locally / deployed
Observation status: not-measured / observing / observed
Source: owner / repository / live-site / platform-data / official-docs / analytics-export / search-results — YYYY-MM-DD
```

## 3. Change / Release Report

```markdown
# Change / Release Report

Date: YYYY-MM-DD
Task ID: TASK-000
Owner:
Approval scope:
Approval status: pending / approved / not-required

Implemented changes:
Files / URLs affected:
Validation and baseline reference:
Release record:
Known limitations:

External results: recorded separately in an Observation Report
Confidence: verified / inference / hypothesis
Change status: not-applicable / proposed / implemented-locally / deployed
Observation status: not-measured / observing / observed
Source: repository / live-site / platform-data — YYYY-MM-DD
```

## 4. Observation Report

```markdown
# Observation Report

Date / observation window:
Task ID: TASK-000
Owner:
Approval scope: observation only; no implementation implied
Approval status: pending / approved / not-required

Baseline reference:
Method and environment:
Observed result (not a causal claim):
Comparison with baseline:
Uncertainty and limitations:
Next decision:

Submitted: [record only when actually verifiable]
Indexed: [record only when actually verifiable]
Ranked: [record only when actually verifiable]
Cited: [record only when actually verifiable]
Converted: [record only when actually verifiable]

Confidence: verified / inference / hypothesis
Change status: not-applicable / proposed / implemented-locally / deployed
Observation status: not-measured / observing / observed
Source: platform-data / analytics-export / search-results — YYYY-MM-DD
```
