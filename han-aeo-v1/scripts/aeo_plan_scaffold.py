#!/usr/bin/env python3
"""Generate a reusable AEO strategy approval brief scaffold."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


VALID_TRACKS = {
    "full-audit": "Full AEO audit",
    "keyword-entity": "Keyword, entity, and page strategy",
    "technical-seo": "Technical SEO and machine readability",
    "content-aeo": "Answer-first content engineering",
    "local-authority": "Local authority and distribution",
    "multilingual": "Multilingual SEO",
    "measurement": "Search and AI visibility measurement",
    "release-submission": "Release, submission, and verification",
    "experiment-review": "Experiment review",
}


def split_tracks(values: list[str]) -> list[str]:
    tracks: list[str] = []
    for value in values:
        tracks.extend(part.strip() for part in value.split(",") if part.strip())
    unknown = [track for track in tracks if track not in VALID_TRACKS]
    if unknown:
        valid = ", ".join(sorted(VALID_TRACKS))
        raise SystemExit(f"Unknown track(s): {', '.join(unknown)}. Valid tracks: {valid}")
    return tracks or ["full-audit"]


def render_brief(project: str, domain: str, tracks: list[str]) -> str:
    track_lines = "\n".join(f"- {VALID_TRACKS[track]} (`{track}`)" for track in tracks)
    today = date.today().isoformat()
    domain_text = domain or "TBD"

    return f"""# AEO/SEO Strategy Approval Brief

Date: {today}
Project: {project}
Domain: {domain_text}

## Selected Tracks

{track_lines}

## Objective

State the business outcome, not just the SEO artifact.

## Known Facts

| Claim | Source | Evidence class | Public? | Status |
|---|---|---|---|---|
|  |  | E1/E2/E3/E4 | yes/no | unverified |

## Unknowns and Stop Conditions

- Business facts needing approval:
- Production or account access needed:
- Legal/privacy/content review needed:
- Validation risks:

## Research Plan

- First-party/repository evidence:
- Search exports or analytics:
- Production page and raw HTML checks:
- SERP/PAA/autocomplete/local pack checks:
- Competitor/entity checks:
- Customer/review/community language:
- AI visibility prompt set:

## Keyword, Entity, and Page Clusters

| Cluster | Intent | Primary page | Current coverage | Priority | Recommended share | Evidence |
|---|---|---|---|---:|---:|---|
|  |  |  |  |  |  |  |

## Priority Formula

Use:

```text
Priority =
  (BusinessValue * IntentFit * AEOExtractability * EvidenceStrength * CoverageGap * Measurability)
  / (Effort * Risk)
```

## Proposed Backlog

| Priority | Item | Track | Page/File | Effort | Risk | Validation | Approval |
|---|---|---|---|---:|---:|---|---|
| P1 |  |  |  |  |  |  | pending |

## Validation Plan

- Local commands:
- Route/raw HTML checks:
- JSON-LD checks:
- Robots/sitemap/canonical checks:
- Browser/device checks:
- Diff scope checks:

## Measurement Plan

- Primary metric:
- Guardrail metric:
- Observation window:
- AI visibility prompt set:
- Reporting cadence:

## Approval Needed

Please approve or revise:

1. Priority services:
2. Priority locations:
3. Pages/content that may visibly change:
4. Schema/business claims:
5. Validation commands:
6. Release/submission actions:
7. Observation window and metrics:
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, help="Project or brand name")
    parser.add_argument("--domain", default="", help="Production domain")
    parser.add_argument(
        "--track",
        action="append",
        default=[],
        help="Track key. Repeat or comma-separate. Example: keyword-entity,technical-seo",
    )
    parser.add_argument("--output", help="Output Markdown file. Defaults to stdout.")
    args = parser.parse_args()

    tracks = split_tracks(args.track)
    brief = render_brief(args.project, args.domain, tracks)

    if args.output:
        output_path = Path(args.output)
        output_path.write_text(brief, encoding="utf-8")
        print(output_path.resolve())
    else:
        print(brief)


if __name__ == "__main__":
    main()
