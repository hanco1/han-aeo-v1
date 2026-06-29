# Keyword, Entity, and Ratio Reference

Use this file for keyword optimization, AEO coverage, entity mapping, and portfolio allocation.

## Optimization Tracks

Ask the user to choose one or more tracks when the scope is unclear:

- Brand/entity disambiguation;
- service/product discovery;
- local/location discovery;
- problem/education answers;
- comparison and alternatives;
- proof/portfolio/trust;
- booking/conversion;
- multilingual coverage;
- AI visibility/citation testing;
- technical machine readability.

## Research Plan

Before researching, define:

- entity to optimize for;
- domain and canonical pages;
- services/products and inactive exclusions;
- priority locations and languages;
- target customer segments;
- conversion events;
- competitors and adjacent alternatives;
- data sources available now;
- source freshness needs;
- ambiguity risks.

Use source lanes:

1. Approved business facts and repository artifacts.
2. Search Console/Bing exports if available.
3. Production pages and raw HTML.
4. SERP, autocomplete, People Also Ask, related searches, local packs.
5. Competitor pages that actually rank or are cited.
6. Customer conversations, reviews, emails, DMs, FAQ logs.
7. Community/social posts where real users discuss needs.
8. AI answer tests with a fixed prompt set.
9. Official platform documentation for technical requirements.

## Query Cluster Schema

Use this shape for each cluster:

```yaml
cluster:
  id: ""
  name: ""
  business_goal: ""
  services: []
  locations: []
  languages: []
  representative_queries: []
  intents: []
  primary_page: ""
  supporting_pages: []
  current_coverage: ""
  evidence_gap: ""
  content_type: ""
  conversion_event: ""
  primary_metric: ""
  guardrail_metric: ""
  human_approved: false
```

## Ratio Means Allocation, Not Density

When a user asks for keyword "ratio" or "占比", treat it as allocation of optimization attention across intent clusters, not a fixed keyword density target.

Recommended portfolio buckets:

- Primary commercial/service intent: 35 to 50 percent.
- Local/location intent: 15 to 30 percent for local businesses.
- Trust/proof/comparison intent: 10 to 25 percent.
- Educational/problem intent: 10 to 20 percent.
- Brand/navigation/entity protection: 5 to 15 percent.
- Multilingual intent: allocate only where the business can support the language and conversion path.

Adjust these with evidence. A high-value service with weak coverage may deserve more share than a high-volume generic term.

## Priority Formula

Use a transparent heuristic and show the inputs:

```text
Priority =
  (BusinessValue * IntentFit * AEOExtractability * EvidenceStrength * CoverageGap * Measurability)
  / (Effort * Risk)
```

Score each factor 1 to 5. Never fabricate volume or competition numbers. If real exports or paid-tool data exist, label the source and date.

Convert scores to recommended share:

```text
cluster_share = cluster_priority / sum(all_cluster_priorities)
```

Use caps and floors:

- Cap any single cluster at 40 percent unless the business is truly single-service.
- Give active core services a floor when the business must be discoverable for them.
- Give unapproved, inactive, or unsupported services 0 percent.
- Keep brand/entity protection even when it has low generic search volume.

## Signal Weighting

Rank by signal quality, not mention count.

- Weight 5: first-party business facts, Search Console/Bing exports, current production/repository evidence, customer questions, reviews with real booking friction.
- Weight 4: expert/operator testimony, credible case study, official local/profile data, measurable before/after evidence.
- Weight 3: ranking competitor pages, multi-source SERP pattern, repeated community discussion with engagement.
- Weight 2: general web articles, directories, topical social chatter, weakly sourced comparisons.
- Weight 1: descriptive mentions with no intent or no business fit.
- Weight 0: promotional noise, unrelated trend terms, doorway-city variants, inactive services, claims the business cannot support.

Multi-source clusters beat single-source clusters. Exact customer language is more useful for FAQ and answer copy than generic keyword-tool phrases.

## Page Mapping Rules

- Assign one primary page to each high-value intent.
- Identify missing pages and pages carrying too many unrelated intents.
- Avoid cannibalization between similar service pages.
- Avoid city-swap doorway pages.
- Avoid pages for inactive services.
- Prefer one strong experiment with proof and measurement over many weak AI-generated pages.

## On-Page Keyword Use

Use keywords as retrieval cues, not stuffing:

- Put the primary intent in the title, H1, direct answer, first visible section, canonical internal links, and metadata when natural.
- Use entity variants, locations, service details, proof terms, and customer questions in visible helpful content.
- Use structured data only for facts visible on the page or approved by the business.
- Do not repeat exact-match phrases mechanically.
