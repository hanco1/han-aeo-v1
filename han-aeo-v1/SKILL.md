---
name: han-aeo-v1
description: "Evidence-led AEO, GEO, AI visibility, SEO audits, and keyword/entity/page mapping. Use for strategy, visibility research, or user-approved AEO/SEO content, metadata, and structured-data changes in a website repository."
---

# Han AEO v1

## Start

Infer the most suitable task type from the request. Use the quick path by default; ask one focused question only when a missing business fact, target page, goal, or constraint would materially change the recommendation.

Treat a user's direct request to implement a defined local scope as approval for that local work. Inspect the relevant repository context, make the smallest compatible change, and run proportionate local validation. Obtain confirmation immediately before publishing or deploying, submitting to Google Search Console or Bing, requesting indexing, or changing an external account.

## Use the quick path

1. Inspect the relevant pages, files, facts, and current state.
2. State the decision, known facts, uncertainty, and proposed or completed local work.
3. Make the requested local change when authorized, then validate it.
4. Report the four evidence fields below and any outcome still awaiting observation.

Do not turn a focused fix, page review, or strategy question into a full audit. Load `references/aeo-workflow.md` only when the user explicitly requests a full audit or complete AEO cycle.

## Label evidence precisely

Label material claims with four independent fields:

- **confidence:** `verified`, `inference`, or `hypothesis`;
- **change_status:** `not-applicable`, `proposed`, `implemented-locally`, or `deployed`;
- **observation_status:** `not-measured`, `observing`, or `observed`;
- **source:** a specific source, such as `owner`, `repository`, `live-site`, `platform-data`, `official-docs`, `analytics-export`, or `search-results`, plus its date.

Use `verified` only for directly supported facts. Use `inference` for a reasoned conclusion and `hypothesis` for a testable assumption. Record `submitted`, `indexed`, `ranked`, `cited`, and `converted` separately when applicable; do not infer any of them from another field or outcome. A recommendation is not implementation, and one citation is not a stable result.

## Keep work moving

Pause only the action that is risky or lacks evidence. Continue with known facts, conflicts, and safe local work; then identify the one next input needed to resume the paused action.

Treat `llms.txt` as an optional experiment that other systems may adopt. Google Search does not use it, and Google Search has no dedicated AI schema. Do not add it to a default implementation checklist.

## Route detailed work deliberately

- Read `references/aeo-workflow.md` only for a full audit or complete cycle.
- Read `references/keyword-research.md` for keyword/entity/page mapping, demand evidence, allocation, or prioritization.
- Read `references/output-templates.md` when producing a project brief, claim ledger, proposal/backlog, change/release report, or observation report; adapt its structure to these four fields.
- Read `references/browser-automation.md` before browser, logged-in platform, AI-interface, or visual-verification work.

## Report

Lead with the decision or completed change. Cite concrete sources and dates for volatile facts. Separate local validation from live observations, state the observation window when outcomes matter, and name only the external action that still needs confirmation.
