# AI News Radar Skill

`ai-news-radar` is a small Codex skill for summarizing current AI news.

It is designed to:

- scan recent AI developments from the last 7 days by default
- prioritize high-impact items over raw chronology
- cover model launches, product updates, research, regulation, funding, and major industry moves
- return a concise ranked briefing with dates and source links

## Who this is for

This repository is for people who want a ready-made prompt skill that can summarize the latest AI news without manually designing the prompt every time.

If you are new to Codex skills, the short version is:

- install this skill into your local skills folder
- invoke it with `$ai-news-radar`
- ask for the AI news window or topic you care about

If you do not have a skill system yet, you can still use the prompt examples in this repository directly.

## How to use this skill

There are two common ways to use it.

### Option 1: Install it as a Codex skill

1. Clone this repository:

```bash
git clone https://github.com/HUANGYming/ai-news-radar-skill.git
```

2. Copy or place the folder into your local Codex skills directory, usually:

```bash
$CODEX_HOME/skills/ai-news-radar
```

3. In a Codex chat, invoke the skill explicitly:

```text
$ai-news-radar Summarize the most important AI news from the last 7 days.
```

4. You can also ask for a filtered version:

```text
$ai-news-radar Summarize this week's open-source AI news in Chinese and include source links.
```

### Option 2: Use it as a prompt template

If you are not using Codex skills yet, open `SKILL.md` and reuse its instructions directly in ChatGPT, Codex, or another LLM.

For example:

```text
Summarize the most important AI news from the last 7 days.
Cover model releases, product launches, research, regulation, funding, and major industry moves.
Rank items by impact. Include publication dates and source links. Use Chinese for the summary.
```

## Files

- `SKILL.md`: the actual skill definition used by Codex
- `agents/openai.yaml`: UI metadata for skill lists and quick invocation
- `README.md`: beginner-facing instructions for GitHub visitors

## Example prompts

- `Summarize the most important AI news from the last 7 days.`
- `Give me a Chinese summary of this week's AI news with source links.`
- `Summarize only open-source AI news from the last 14 days.`
- `Track recent AI policy and regulation developments.`

## Beginner examples

Try one of these exactly as written:

- `$ai-news-radar What are the hottest AI news items today?`
- `$ai-news-radar Give me a Chinese summary of this week's AI news.`
- `$ai-news-radar Track recent AI regulation and policy updates from the last 14 days.`
- `$ai-news-radar Summarize only model launches and major product updates from this week.`

## Output style

The skill is intended to produce:

- an `AI news snapshot` header
- 5 to 8 ranked items
- one-line explanation of why each item matters
- exact publication dates
- one or two source links per item
- a short `Watch next` section

## What this skill does well

- saves you from rewriting the same AI-news prompt repeatedly
- keeps the output concise instead of dumping many links
- pushes the model to use exact dates and clearer source attribution
- works for both broad news scans and focused categories like regulation or open source

## What it does not do

- it does not crawl private data sources for you
- it does not guarantee every item is independently verified if only one official source exists
- it does not replace human judgment on whether a story is truly important

## Repository

GitHub: [HUANGYming/ai-news-radar-skill](https://github.com/HUANGYming/ai-news-radar-skill)
