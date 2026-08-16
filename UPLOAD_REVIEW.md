# Current-Branch Candidate Review

Branch candidate: `codex/han-aeo-v1-optimization`
Commit reviewed: **not yet bound**

## Status

**Pending review.** This document does not mark the candidate as passed. Bind the review to an exact commit hash, then rerun the review against that commit immediately before publication.

## Candidate file inventory

| Path | Intended role |
|---|---|
| `.gitignore` | Keeps local secrets, exports, reports, screenshots, and Playwright state out of the repository. |
| `README.md` | Installation and concise usage guide for the Agent Skill. |
| `UPLOAD_REVIEW.md` | Candidate-review record and release gate. |
| `docs/integrations/last30days.md` | Optional third-party research-skill integration note. |
| `examples/mock-aeo-project/ai-visibility-prompts.md` | Mock questions. |
| `examples/mock-aeo-project/site-facts.yaml` | Mock business-fact input. |
| `examples/mock-aeo-project/strategy-brief.md` | Mock proposal. |
| `han-aeo-v1/SKILL.md` | Agent Skill instructions. |
| `han-aeo-v1/agents/openai.yaml` | Skill metadata. |
| `han-aeo-v1/references/*.md` | General AEO workflow references. |

The former API tutorial, GIF storyboard, and GIF-rendering script are not part of this candidate.

## Required review before publication

- Record the branch and exact commit hash being reviewed.
- Recheck the candidate for private source material, credentials, exports, logged-in browser state, and generated reports.
- Rerun the relevant validation and review the final file inventory after all release changes are in place.
- Have the owner choose a license.

## License gate

There is no `LICENSE` file. A public open-source release is **blocked pending the owner's license choice**. Do not publish as open source until that decision and the final commit-bound review are complete.
