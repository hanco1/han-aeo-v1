# Mock AEO Strategy Brief

Project: Sample Glow Studio
Domain: `https://example-glow.test`
Status: mock-only public sample

## Recommendation

Prioritize service and local intent first, then build proof and answer-first content around high-friction booking questions.

## Evidence Inspected

| Evidence | Class | Notes |
|---|---|---|
| Mock business facts | E1 | Sanitized local sample data only |
| Mock route inventory | E3 | Intended implementation target |
| Mock keyword clusters | E3 | Demonstrates allocation logic, not real volume |

## Keyword, Entity, and Page Clusters

| Cluster | Intent | Primary page | Recommended share | Rationale |
|---|---|---|---:|---|
| Bridal trial | Commercial service | `/services/bridal-trial` | 35% | High conversion value and clear service fit |
| Event makeup | Service discovery | `/services/event-makeup` | 20% | Active core service with broad use cases |
| Graduation photo makeup | Local seasonal service | `/services/graduation-photo-makeup` | 20% | Local and seasonal AEO opportunity |
| Proof and portfolio | Trust/proof | `/portfolio` | 15% | Needed to support answer citations and conversions |
| Brand/entity | Navigation/entity | `/about` and home | 10% | Protects entity disambiguation |

## Proposed Backlog

| Priority | Item | Track | Validation |
|---|---|---|---|
| P1 | Create approved business fact ledger | Entity SEO | Fact table reviewed by owner |
| P1 | Add route-level metadata and canonical URLs | Technical SEO | Raw HTML and build checks |
| P1 | Add truthful local business JSON-LD | Structured data | JSON-LD parse and fact match |
| P2 | Draft answer-first service page sections | Content AEO | Owner review and visible content check |
| P2 | Add `llms.txt` with canonical pages | AI SEO | Route returns plain text and canonical links |
| P3 | Run fixed AI visibility prompt set | Measurement | Dated prompt/output log |

## Approval Needed

Approve or revise:

1. Priority services.
2. Public business facts.
3. Pages that may visibly change.
4. Schema claims.
5. Validation commands.
6. Observation window.
