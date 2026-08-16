# Han AEO v1

Han AEO v1 is an **Agent Skill** for evidence-led AEO, AI SEO, entity, content, and technical SEO work. It helps an agent research a site, prepare a proposal, and carry out only the scope you approve.

It is not a SaaS product, website, crawler, or GUI application.

## Quick Start

This repository is currently private, so cloning requires authenticated GitHub access. A future public release still requires an owner-selected `LICENSE` and final review; once public, use the same clone command directly.

Clone the repository, then copy the skill directory to `$HOME/.agents/skills/han-aeo-v1`.

```bash
git clone https://github.com/hanco1/han-aeo-v1.git
cd han-aeo-v1
mkdir -p "$HOME/.agents/skills"
cp -R han-aeo-v1 "$HOME/.agents/skills/han-aeo-v1"
```

In PowerShell, the same destination is `$env:USERPROFILE\.agents\skills\han-aeo-v1`:

```powershell
git clone https://github.com/hanco1/han-aeo-v1.git
Set-Location han-aeo-v1
New-Item -ItemType Directory -Force "$env:USERPROFILE\.agents\skills" | Out-Null
Copy-Item -Recurse -Force ".\han-aeo-v1" "$env:USERPROFILE\.agents\skills\han-aeo-v1"
```

Open a new agent session after copying it so the skill list is discovered again.

Optionally validate the installed skill with `quick_validate.py`:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "$env:USERPROFILE\.agents\skills\han-aeo-v1"
```

The skill itself does not depend on Python; Python is only needed when running this validator.

## Use It

Start with a clear goal, the site URL, and the facts the agent may rely on:

```text
Use $han-aeo-v1 to audit this site for AEO and SEO. Build the evidence base and a prioritized proposal first. Wait for my approval before making any changes.
```

The default workflow is short:

1. Gather business facts and inspect the site or repository.
2. Research intent, entities, content, and technical risks.
3. Produce a prioritized proposal.
4. After approval, implement the approved scope, validate it, and observe results over time.

## What It Produces

Depending on the task, the skill can produce a fact/claim ledger, keyword–entity–page map, content brief, technical change proposal, release checklist, and measurement plan.

It does not add `llms.txt` by default. Consider it only when it fits the approved scope.

A recommendation is not implementation. Implementation is not proof of indexing, rankings, or AI citations; those need post-release observation.

## Mock Project

[`examples/mock-aeo-project/`](examples/mock-aeo-project/) contains three prefilled fake-data text files, not a website or program. There is nothing to run:

- `site-facts.yaml` is the input: fictional business facts.
- `ai-visibility-prompts.md` is the questions: example questions to test or research.
- `strategy-brief.md` is the proposal: a sample strategy and approval brief.

## Optional Integration

[`last30days`](docs/integrations/last30days.md) is an optional, separately installed research skill. It can supply additional customer-language findings, but it is not part of the main Han AEO workflow.

## Upload and License

See [UPLOAD_REVIEW.md](UPLOAD_REVIEW.md) before sharing this repository. No license has been selected; a public open-source release remains blocked until the owner makes that choice.
