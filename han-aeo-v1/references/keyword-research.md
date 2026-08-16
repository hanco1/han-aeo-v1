# Keyword and Entity Research Reference

Use this reference to turn evidence into a small, reviewable query and page plan. It is not a keyword-density or percentage-allocation method.

## Start with approved scope

Record the entity, active services, locations, languages the business can actually support, conversion goal, and known exclusions. Mark anything unconfirmed as unknown instead of turning it into content or a claim.

## Sources

Use the strongest available source and record its date:

1. Approved business facts and visible repository or production pages.
2. Search Console/Bing exports and analytics, when supplied.
3. Search results, autocomplete, People Also Ask, local results, and ranking pages.
4. Customer questions, reviews, support or sales conversations where approval permits.
5. Dated AI-answer observations using a fixed prompt set.
6. Official platform documentation for technical requirements.

Separate observed evidence from assumptions. A competitor page, AI answer, or search suggestion is a research signal, not proof that the business offers a service or has a result.

## Query clusters

Use one row per coherent customer need. Representative queries are examples to investigate, not promises of demand or rankings.

```yaml
cluster:
  id: ""
  customer_need: ""
  representative_queries: []
  intent: "discovery | comparison | booking | support | brand"
  business_fit: "High | Medium | Low"
  sources:
    - source: ""
      date: "YYYY-MM-DD"
      note: ""
  current_coverage: ""
  coverage_gap: "High | Medium | Low"
  primary_page: ""
  supporting_pages: []
  negative_or_guardrail: ""
  owner_approval: "pending | approved | not-required"
```

## Triage, not a formula

Prioritize with a transparent 0–3 triage. Do not multiply scores or convert them into percentages.

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Business fit | Unsupported, inactive, or irrelevant | Plausible but needs confirmation | Approved but secondary need | Approved core customer or business need |
| Evidence | No usable source | One weak or indirect dated signal | One relevant dated source | Approved fact or multiple relevant dated sources |
| Coverage gap | Already clear and sufficient | Small clarity gap | Incomplete or mixed coverage | Missing, inaccurate, or hard-to-find coverage |
| Feasibility/risk | Infeasible or high risk | Major review or disproportionate effort | Manageable work and review | Low-risk, feasible next step |

Record the four labels and explain the recommendation in one sentence. Keep unsupported, inactive, privacy-sensitive, misleading, or doorway-location terms in the negative/guardrail field.

## Intent-to-page mapping

| Cluster / intent | Existing or proposed primary page | Supporting page(s) | Evidence and date | Guardrail | Approval |
|---|---|---|---|---|---|
|  |  |  |  |  | pending |

- Give a high-value intent one clear primary page.
- Mark a missing destination as a **proposed page** until it exists and is approved.
- Avoid city-swapped doorway pages, duplicate service pages, and pages for services the business cannot confirm.
- Use visible, approved facts in content and structured data; do not manufacture proof, availability, languages, or outcomes.
