---
name: ai-news-radar
description: Summarize current AI news by searching for recent developments across model releases, product launches, research, regulation, funding, and major industry moves. Use when the user wants a concise snapshot of what is happening in AI right now.
---

# AI News Radar

Create a concise, current summary of important AI news.

When to use

- The user asks for today's AI news, recent AI updates, trending AI topics, or a quick AI industry briefing.
- The user wants a ranked summary instead of a raw dump of links.

Core workflow

1. Search for very recent AI news. Prioritize the last 7 days unless the user asks for a different window.
2. Cover multiple lanes:
   - frontier model launches or upgrades
   - major product releases from leading AI companies
   - important research announcements
   - regulation, policy, safety, or legal changes
   - major funding, acquisitions, partnerships, or enterprise adoption
3. Prefer primary and high-signal sources:
   - official company blogs, newsroom posts, and research pages
   - major reporting outlets with clear publication dates
4. Verify notable claims across at least two sources when possible. If a claim appears only once, say so.
5. Rank items by likely impact, not just publication time.

Output format

- Start with `AI news snapshot`.
- List 5 to 8 items.
- For each item include:
  - a one-line headline
  - why it matters in one sentence
  - the publication date
  - one or two source links
- End with `Watch next` and list 2 or 3 developments worth monitoring.

Quality bar

- Do not present stale background pieces as breaking news.
- Call out exact dates to avoid ambiguity.
- Distinguish confirmed announcements from rumors or analyst speculation.
- If the news cycle is light, say that clearly instead of padding the list.

Optional filters

- If the user cares about a segment such as open source, regulation, coding agents, China AI, or enterprise AI, narrow the search and say that the summary is filtered.
