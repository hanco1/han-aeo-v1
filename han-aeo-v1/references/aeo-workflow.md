# Full AEO Workflow

Use this reference only for a requested full audit or complete AEO/SEO cycle. For a focused review or local change, follow the quick path in `SKILL.md` instead.

## Operating model

Treat a direct request to implement a defined local scope as approval for that scope. Confirm immediately before any external write: publishing or deployment, Search Console or Bing submission/request, or external-account change.

Record each material claim with four independent fields:

| Axis | Values | Meaning |
|---|---|---|
| confidence | `verified`, `inference`, `hypothesis` | Directly supported fact, reasoned conclusion, or testable assumption |
| change_status | `not-applicable`, `proposed`, `implemented-locally`, `deployed` | Lifecycle of the change |
| observation_status | `not-measured`, `observing`, `observed` | Status of outcome measurement |
| source | A specific source plus date, such as `owner`, `repository`, `live-site`, `platform-data`, or `official-docs` | Origin and freshness of the evidence |

Never collapse these fields. Record a deployed but unmeasured change as `change_status=deployed` and `observation_status=not-measured`. Record `submitted`, `indexed`, `ranked`, `cited`, and `converted` separately when applicable; do not infer one from another. One AI citation is not a stable visibility result.

## User-facing states

Use these six states for the current cycle:

1. **Understanding scope** — target, goals, available evidence, and missing decision-critical facts.
2. **Measuring baseline** — current technical, search, entity, content, and AI-visibility observations.
3. **Planning changes** — prioritized strategy and validation/observation plan.
4. **Implementing locally** — approved local changes and local validation.
5. **Ready for external action** — any publish, deploy, submission, or account action awaiting confirmation.
6. **Observing results** — dated live data, experiment review, and next iteration.

Attach a hold to a specific risky or unsupported action, not to the whole cycle. While an action is held, report known facts and conflicts, complete safe work, and request the one input needed to continue that action.

## Eight phases for a full audit

1. **Scope and guardrails** — identify domain, audience, conversion goal, requested tracks, repository constraints, and the facts that could alter the work.
2. **Business truth and entity model** — verify names, services, locations, languages, owners, proof, public contacts, and prohibited claims with an owner or approved source.
3. **Baseline audit** — inspect routes, raw HTML, metadata, canonicalization, robots, sitemap, structured data, rendering, performance, index/search exports, and authorized AI tests.
4. **Opportunity mapping** — map questions and intents to entities, pages, proof, locations, and conversion events; identify coverage gaps and cannibalization.
5. **Strategy and action boundary** — rank work by business value, evidence strength, coverage gap, effort, risk, and measurability. Separate local work from external actions.
6. **Local implementation** — make the smallest repository-compatible changes to content, technical SEO, structured data, internal linking, or measurement hooks. Do not invent business facts.
7. **Validation and external-action decision** — run relevant project checks; validate rendered output, metadata, sitemap/robots intent, and structured data; then prepare the exact external-action details.
8. **Observation and iteration** — capture dated platform/search/AI evidence, compare against the baseline and guardrails, and decide whether to continue, revise, or stop an experiment.

## Implementation guidance

Prefer first-party facts, repository state, platform exports, live-site checks, and official documentation over generic advice. Verify current platform behavior before relying on it.

Use answer-first content only where it answers a real user question and reflects approved facts. Keep structured data aligned with visible, supported content. Do not add FAQ markup without real visible FAQ content. Avoid doorway pages, keyword stuffing, fake authority, or unsupported service/location claims.

Treat `llms.txt` only as an optional experiment for systems that may choose to use it. Google Search does not use it, and Google Search has no dedicated AI schema; exclude it from the default backlog.

## Validate and report

Run the applicable lint, type, build, test, route, raw-HTML, metadata, canonical, robots, sitemap, structured-data, device-flow, and diff-scope checks. Report the decision, source/date, four evidence fields, files changed, local validation, live observations, uncertainties, and observation window.

Keep implementation, submission, indexing, rankings, AI citations, and business outcomes as separate claims.
