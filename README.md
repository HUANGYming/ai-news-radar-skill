# AI News Radar Skill

`ai-news-radar` is a small Codex skill for summarizing current AI news.

It is designed to:

- scan recent AI developments from the last 7 days by default
- prioritize high-impact items over raw chronology
- cover model launches, product updates, research, regulation, funding, and major industry moves
- return a concise ranked briefing with dates and source links

## Files

- `SKILL.md`: the actual skill definition used by Codex
- `agents/openai.yaml`: UI metadata for skill lists and quick invocation

## Example prompts

- `Summarize the most important AI news from the last 7 days.`
- `Give me a Chinese summary of this week's AI news with source links.`
- `Summarize only open-source AI news from the last 14 days.`
- `Track recent AI policy and regulation developments.`

## Output style

The skill is intended to produce:

- an `AI news snapshot` header
- 5 to 8 ranked items
- one-line explanation of why each item matters
- exact publication dates
- one or two source links per item
- a short `Watch next` section

## Repository

GitHub: [HUANGYming/ai-news-radar-skill](https://github.com/HUANGYming/ai-news-radar-skill)
