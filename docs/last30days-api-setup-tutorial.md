# last30days API Setup Tutorial

Audience: beginners who want to use `last30days` as an AEO/SEO keyword supplement.

Goal: unlock more real-user language from social, video, and web sources without exposing secrets.

## What You Need First

The base setup already works with:

- Reddit
- YouTube, when `yt-dlp` is installed
- Hacker News
- Polymarket
- GitHub, when `gh` is installed

For basic AEO/SEO keyword research, this is enough to collect:

- customer-style questions;
- FAQ phrasing;
- comparison language;
- pain points;
- content angles;
- long-tail topic ideas.

## Optional API Keys

Use these only when you want deeper coverage.

| Variable | Unlocks | Beginner value | Official starting point |
|---|---|---|---|
| `SCRAPECREATORS_API_KEY` | TikTok, Instagram, Threads, Reddit fallback | Best add-on for creator/social language | `https://scrapecreators.com` |
| `XAI_API_KEY` | X/Twitter path used by the skill when configured | Useful for recent conversation and public reactions | `https://console.x.ai` |
| `BRAVE_API_KEY` | Brave Search backend for auto-resolve and web context | Useful when the model cannot use WebSearch | `https://api.search.brave.com` |
| `OPENROUTER_API_KEY` | Optional deep research / Perplexity route | Useful for deeper summaries, not required for keywords | `https://openrouter.ai/settings/keys` |

Do not start with every API. For AEO/SEO, start with:

1. `SCRAPECREATORS_API_KEY`
2. `BRAVE_API_KEY`
3. `XAI_API_KEY`, only if X coverage matters
4. `OPENROUTER_API_KEY`, only for deep research

## Safety Rules for the Tutorial GIF

- Never show a real API key.
- Record only the steps before the key value is revealed, or cover the value with a black box.
- Use fake examples in `.env`, such as `SCRAPECREATORS_API_KEY=sk_demo_xxxxx`.
- Do not record account email, billing page, card details, organization IDs, or usage dashboards.
- Pause recording before clicking "Create key" if the platform immediately reveals the secret.

## Beginner Walkthrough

### Step 1 - Open the provider page

Open the official provider page in Chrome.

Example:

```text
https://scrapecreators.com
```

### Step 2 - Sign in or create an account

Use the provider's normal signup flow. Stop recording if private profile or billing details appear.

### Step 3 - Find API keys

Look for labels such as:

- API Keys
- Developer
- Dashboard
- Settings
- Tokens

### Step 4 - Create a key

Name the key after the project:

```text
han-aeo-last30days
```

Copy the key only after pausing or masking the recording.

### Step 5 - Add the key to `.env`

Create or edit:

```text
~/.config/last30days/.env
```

Use this shape:

```dotenv
SETUP_COMPLETE=true
FROM_BROWSER=false
SCRAPECREATORS_API_KEY=sk_demo_replace_me
XAI_API_KEY=xai_demo_replace_me
BRAVE_API_KEY=brave_demo_replace_me
OPENROUTER_API_KEY=or_demo_replace_me
```

Only include keys you actually have.

### Step 6 - Check available sources

Run:

```bash
python C:/Users/User/.agents/skills/last30days/scripts/last30days.py --diagnose
```

Expected result after full setup:

```json
{
  "available_sources": [
    "reddit",
    "youtube",
    "hackernews",
    "polymarket",
    "github",
    "x",
    "tiktok",
    "instagram"
  ]
}
```

Your exact list may be different.

### Step 7 - Use it for AEO/SEO keyword supplement

Use concrete topics, not generic keywords.

Good:

```text
/last30days bridal makeup booking concerns --agent
/last30days graduation photo makeup questions --agent
/last30days how people choose a makeup artist --agent
```

Avoid:

```text
/last30days makeup
/last30days seo keywords
```

### Step 8 - Convert findings into AEO work

Map results into:

- FAQ questions;
- answer-first page sections;
- service page subtopics;
- comparison/trust sections;
- proof gaps;
- long-tail query clusters.

Treat `last30days` as a language and intent supplement. It does not replace Search Console, keyword tools, SERP checks, or business facts.
