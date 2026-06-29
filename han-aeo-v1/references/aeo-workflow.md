# AEO Workflow Reference

Use this file when running a full AEO/AI SEO cycle or when implementation is likely.

## Authority Model

AI may inspect code, propose strategy, draft content, implement approved code/content changes, and run local validation. AI must not publish, submit, deploy, alter business facts, invent services, change legal/privacy statements, or make production-account changes without explicit human approval.

The human owner approves business facts, priority services, priority locations, visible content, brand voice, legal/privacy-sensitive claims, conversion objectives, production release, submissions, and observation decisions.

## Evidence Classes

- E1: implemented and locally verified. Examples: source file exists, build passed, raw HTML contains metadata, JSON-LD parses.
- E2: implemented but external outcome pending. Examples: sitemap submitted, schema published, page indexed status not yet measured.
- E3: recommended experiment. Must include hypothesis, implementation scope, metric, guardrail, observation window, and stop rule.
- E4: general or external guidance. Must be current-verified when platform rules, docs, policies, prices, or product behavior may have changed.

Use evidence precedence in this order: production state, repository state, approved business source, analytics/search export, git history, prior project notes, browser history, course/general material.

## Stop Conditions

Stop and ask or report a blocker when:

- authoritative sources conflict;
- a business fact, service, location, credential, or claim is unknown;
- visible UI/content changes are not approved;
- legal, medical, financial, privacy, or review-policy claims need owner/professional review;
- validation fails;
- production access or logged-in account action is required;
- external platform submission, review reply, or publication would affect another system;
- evidence is insufficient to support a completion claim.

## State Machine

Use these states for long-running work:

```text
S0 UNINITIALIZED
S1 CONTEXT_INSPECTED
S2 FACTS_PENDING_APPROVAL
S3 FACTS_APPROVED
S4 BASELINE_CAPTURED
S5 STRATEGY_PROPOSED
S6 STRATEGY_APPROVED
S7 IMPLEMENTATION_IN_PROGRESS
S8 IMPLEMENTATION_VALIDATED
S9 RELEASE_PENDING_APPROVAL
S10 RELEASED
S11 SUBMISSION_PENDING
S12 OBSERVATION_ACTIVE
S13 EXPERIMENT_REVIEW
S14 ITERATION_APPROVED
S15 COMPLETE_FOR_CURRENT_CYCLE
SB BLOCKED
SR ROLLBACK_REQUIRED
```

Illegal transitions:

- S1 to implementation without approved facts;
- S4 to implementation without approved strategy;
- S7 to release without validation;
- release to outcome success without observation;
- submission to indexed;
- indexed to ranking success;
- ranking to qualified conversion.

## Eight Phases

1. Bootstrap and context inspection
   - Inputs: repo path, domain, framework, branch, business source, user goal.
   - Output: scope, protected files, commands, risks, missing inputs.

2. Business truth and entity model
   - Normalize name, alternate names, owner/practitioner, business type, address/publicity, service areas, contacts, services, languages, profiles, differentiators, proof assets, privacy constraints.
   - Output: approved fact table and claim ledger.

3. Baseline audit
   - Technical: route inventory, metadata, canonical, robots, sitemap, raw HTML, schema, performance, mobile, multilingual.
   - Search: indexed pages, Search Console exports, branded/non-branded visibility, existing rankings if available.
   - AI visibility: fixed question set across approved AI/search surfaces when authorized.
   - Authority: local profiles, reviews, citations, backlinks, social/proof assets.

4. Query, entity, and page strategy
   - Map user questions to services, locations, entities, pages, and conversion events.
   - Identify cannibalization, missing pages, weak pages, proof gaps, and measurement gaps.
   - Produce priority score and strategy approval gate.

5. Technical implementation
   - Metadata, canonical, robots, sitemap, server-rendered content, JSON-LD, image SEO, icons/manifest, `llms.txt`, locale alternates, performance and device checks.

6. Answer and content engineering
   - Use answer-first structure: question, direct answer, applicability, limits, steps/table/comparison, proof, related FAQs, links, CTA, owner/freshness.
   - Do not add FAQ schema without real visible FAQ content.

7. Authority and distribution
   - Local entity consistency, official profiles, reviews, legitimate partnerships/citations, original assets, distribution record.
   - Avoid fake authority and bulk low-value pages.

8. Release, submission, measurement, and iteration
   - Release gate, Search Console/Bing runbooks, structured data validation, performance verification, observation plan, experiment review, rollback plan.

## Validation Contract

Run the relevant checks for the project:

- lint, type, build, tests;
- key URL status;
- robots and sitemap;
- canonical and noindex intent;
- raw HTML contains core content and metadata;
- JSON-LD parses and matches approved facts;
- mobile/tablet/desktop key flow;
- contact and conversion actions;
- approved diff scope only.

Outcome checks require time and data: index status, impressions, non-brand visibility, AI mention accuracy, citations, qualified inquiries, and guardrail stability.
