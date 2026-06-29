# Browser Automation Reference

Use browser automation only when it adds evidence that local files, APIs, exports, or direct HTTP checks cannot provide.

## Tool Choice

- Use local repository commands for code, generated routes, metadata, schema, robots, sitemap, and raw HTML whenever possible.
- Use web search or official docs for current platform rules, policy, or documentation.
- Use an in-app/public browser for local dev server rendering, public production pages, screenshots, mobile/desktop checks, and visual verification.
- Use Chrome when the task depends on the user's existing Chrome profile, logged-in sessions, extensions, or the user explicitly requests Chrome.
- Do not use Chrome merely to bypass missing connector/API authentication. Ask the user to sign in or approve Chrome fallback.

## Evidence to Capture

For each browser-assisted finding, record:

- URL;
- timestamp/date;
- viewport/device if visual;
- query or prompt used;
- visible result or DOM evidence;
- screenshot path when relevant;
- account/tool state if logged-in;
- limitation or uncertainty.

## AI Visibility Tests

Use a fixed question set so future runs are comparable. Include:

- brand/entity questions;
- service plus location questions;
- comparison/trust questions;
- proof/portfolio questions;
- Chinese or other language questions only when the business supports the language.

Do not over-read one AI answer. Treat AI mentions as directional evidence until repeated across prompts, dates, and surfaces.

## Search Console and Bing

Logged-in dashboards may be used only with user authorization. Do not submit, validate fixes, request indexing, or change settings without explicit approval.

When exports are available, prefer export data over screenshots for analysis. Screenshots are evidence of UI state, not a substitute for dated data tables.

## Release and Submission

Before browser actions that affect external systems, confirm:

- exact URLs;
- action to take;
- account/platform;
- expected effect;
- rollback or undo path;
- whether this is release, submission, validation, or observation only.

Never treat "submitted" as "indexed" or "ranked".
