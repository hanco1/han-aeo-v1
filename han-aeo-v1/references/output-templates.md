# Output Templates

Use these templates for proposal, approval, execution, and measurement outputs.

## Intake Object

```yaml
project:
  name: ""
  repository_path: ""
  production_domain: ""
  framework: ""
  deployment_platform: ""
  default_branch: ""
  working_branch: ""
business:
  primary_name: ""
  alternate_names: []
  type: ""
  services: []
  locations: []
  languages: []
  contacts: []
  profiles: []
goals:
  selected_tracks: []
  conversion_events: []
  observation_window: ""
constraints:
  private_facts: []
  legal_or_privacy_review: []
  no_go_actions: []
```

## Claim Ledger

```markdown
| Claim ID | Claim | Source | Evidence class | Public? | Last verified | Owner | Status |
|---|---|---|---|---|---|---|---|
| CLM-001 |  |  | E1/E2/E3/E4 | yes/no | YYYY-MM-DD |  | active/unverified |
```

## Research Plan

```markdown
**Research Plan**

Objective:

Selected tracks:

Known facts:

Unknowns:

Source lanes:

Competitors/entities to inspect:

AI/search questions to test:

Freshness requirements:

Stop conditions:
```

## Strategy Proposal

```markdown
**AEO/SEO Strategy Proposal**

Recommendation:

Evidence inspected:

Business facts used:

Keyword/entity/page clusters:

Recommended allocation:

Priority backlog:

Risks and anti-patterns:

Validation plan:

Measurement window:

Approval needed:
```

## Backlog

```markdown
| Priority | Item | Track | Page/File | Evidence | Effort | Risk | Validation | Approval |
|---|---|---|---|---|---:|---:|---|---|
| P1 |  |  |  |  |  |  |  | pending |
```

## Change Report

```markdown
**Change Summary**

Objective:

Approved scope:

Evidence inspected:

Files changed:

Visible UI/content impact:

Business facts used:

Validation performed:

Results:

Known limitations:

Search/AI outcome status:

Human actions required:

Measurement window:
```

## Release Validation

```markdown
**Release Validation**

Build:

URLs:

SEO:

Structured data:

UX/device:

Analytics/conversion:

Diff scope:

Human approval:
```

## Weekly Visibility Report

```markdown
**Weekly Search and AI Visibility Report**

Date range:

Search:

AI visibility:

Conversions:

Notable changes:

Experiment decisions:

Next actions:
```

## Approval Gate

Ask for approval in concrete terms:

```markdown
Please approve or revise:

1. Priority services:
2. Priority locations:
3. Pages/content that may visibly change:
4. Schema/business claims:
5. Validation commands:
6. Release/submission actions:
7. Observation window and metrics:
```
