---
name: han-aeo-v1
description: "Evidence-governed AEO, AI SEO, GEO, entity SEO, local SEO, technical SEO, content, structured data, llms.txt, keyword/entity/page mapping, AI visibility research, approval-gated implementation, and measurement workflow. Use when a user wants an AEO/SEO audit, keyword optimization plan, answer-engine optimization strategy, page/content/schema implementation, search or AI visibility baseline, browser-assisted verification, or a reusable execution plan that requires research first and human approval before changes."
---

# Han AEO v1

## Core Contract

Use this skill to turn business truth into a crawlable, indexable, unambiguous, answer-ready, measurable website or content system.

Never claim AEO/SEO success from implementation alone. Code, content, schema, `llms.txt`, metadata, and submissions are implementation evidence. Indexing, ranking, AI mentions, citations, referrals, and qualified inquiries require a dated observation window.

For substantial AEO work, create or continue a goal only when the user explicitly asks for goal-based work or the active thread already has a matching goal. The goal should cover research, proposal, approval, execution, validation, and measurement.

## Workflow

1. Scope the request.
   - If the user has not selected a track, ask them to choose from: full AEO audit, keyword/entity strategy, technical SEO, answer-first content, local authority, multilingual SEO, AI visibility measurement, release/submission, or ongoing experiment review.
   - If the user asks to execute immediately, still separate research/proposal from implementation unless they have already approved a specific strategy.

2. Inspect context before advice.
   - Read repository instructions, current project files, routing/content structure, package scripts, current branch/status, and any provided business facts.
   - Inspect production URLs, Google Search Console, Bing Webmaster Tools, AI interfaces, or social/search surfaces only when authorized and useful.
   - Prefer local code, official APIs, exported data, and direct artifacts over generic web advice.

3. Build the evidence base.
   - Maintain a claim ledger for business facts, technical facts, content claims, and outcome claims.
   - Use evidence classes: E1 locally verified implementation, E2 implemented with external outcome pending, E3 recommended experiment, E4 general or externally sourced guidance.
   - Stop when business facts conflict, production access is required, validation fails, legal/privacy review is needed, or evidence is insufficient.

4. Produce a research plan before deep research.
   - Resolve the entity, domain, services/products, locations, languages, competitors, audience, conversion goals, and ambiguity risks.
   - Plan source lanes before searching: first-party data, repository, production pages, search exports, SERP/PAA/autocomplete, competitor pages, reviews, local profiles, community/social proof, official platform docs, and AI-answer tests.
   - For current or volatile platform behavior, verify with live sources before making claims.

5. Generate the proposal and wait for approval.
   - Deliver a strategy brief with facts, evidence, keyword/entity/page clusters, priority scoring, implementation backlog, risks, validation plan, measurement window, and exact approval questions.
   - Do not implement visible content, schema claims, submissions, or production-affecting work until the user approves the scope.

6. Execute the approved scope.
   - Make the minimum necessary changes that match the repository style.
   - Typical execution areas: metadata, canonical URLs, sitemap, robots, raw HTML renderability, JSON-LD, `llms.txt`, answer-first content, FAQ rules, internal links, image SEO, local entity consistency, multilingual alternates, measurement hooks, and release validation.

7. Validate and report.
   - Run relevant lint/type/build/tests plus route, raw HTML, JSON-LD, robots, sitemap, mobile/desktop, and diff-scope checks when applicable.
   - Distinguish implementation status from search/AI outcomes.
   - Provide a release or handoff report with human actions and observation dates.

## Reference Routing

- Read `references/aeo-workflow.md` for the complete phase model, evidence rules, gates, stop conditions, and validation contract.
- Read `references/keyword-research.md` when the user asks for keyword optimization, entity/page mapping, keyword ratio, search demand, AEO coverage, or prioritization.
- Read `references/output-templates.md` before producing strategy briefs, approval gates, backlogs, change reports, release reports, or weekly visibility reports.
- Read `references/browser-automation.md` before using browser automation, in-app browser, Chrome, logged-in search tools, AI interfaces, or visual validation.

## Output Rules

- Lead with the decision or recommendation, then the evidence.
- Cite concrete evidence sources in the work product; do not invent volume, competition, ranking, AI citation, or conversion data.
- Treat keyword ratio as portfolio allocation across intent clusters, not keyword stuffing or fixed on-page density.
- Rank by signal quality, not mention count. Strong practitioner/customer/search-console evidence beats many weak generic mentions.
- Make approval questions explicit: what will change, where, why, how it will be validated, and what outcome window will be observed.

## Script

Use `scripts/aeo_plan_scaffold.py` to generate a reusable Markdown approval brief scaffold:

```bash
python scripts/aeo_plan_scaffold.py --project "Example Brand" --domain "https://example.com" --track keyword-entity --track technical-seo --output aeo-brief.md
```
