# AI News Radar Skill

## 简介

`ai-news-radar` 是一个用于汇总近期 AI 热点新闻的 Codex skill。

它会优先关注近 7 天的重要动态，并按影响力整理输出，覆盖这些方向：

- 模型发布与升级
- 产品更新
- 研究进展
- 监管与政策
- 融资、收购与行业合作

输出目标是：给出一份简洁、可读、带日期和来源链接的 AI 新闻摘要。

仓库里还带了一个格式化脚本 `scripts/render_news_brief.py`，可以把结构化 JSON 渲染成固定 markdown 结果，用来规范输出格式。

## 结果示例

下面是一份基于真实新闻生成的输出示例：

```markdown
AI news snapshot

- OpenAI announced it will acquire Promptfoo.
Why it matters: 这指向企业级 AI 的下一轮重点正在从“能不能做 agent”转向“能不能安全评测和治理 agent”。
Publication date: March 9, 2026.
Sources: https://openai.com/index/openai-to-acquire-promptfoo/

- Google expanded Gemini in Chrome to India, New Zealand, and Canada.
Why it matters: 这说明浏览器内置 AI 正在从实验功能转向更大范围分发，Chrome 会继续成为 Google 端侧和入口级 AI 的重要落点。
Publication date: March 11, 2026.
Sources: https://blog.google/products-and-platforms/products/chrome/chrome-expands-india-new-zealand-canada/

- Ai2 released OLMo Hybrid, a fully open 7B model family focused on better data efficiency.
Why it matters: 开源阵营正在继续押注“更高训练效率”的模型架构，而不只是单纯堆更多参数和算力。
Publication date: March 5, 2026.
Sources: https://allenai.org/blog/olmohybrid, https://allenai.org/newsletters/2026-03-newsletter

Watch next

- GTC 2026 期间是否会出现新的开源模型或算力合作发布。
- Google I/O 2026 前后 Gemini 是否会有更大范围产品更新。
- 美国政府与 AI 公司在军用和监控用途上的政策边界是否继续升级。
```

## 怎么通过 Codex 使用

1. 克隆仓库：

```bash
git clone https://github.com/HUANGYming/ai-news-radar-skill.git
```

2. 把这个目录放到本地 Codex skills 目录，例如：

```bash
$CODEX_HOME/skills/ai-news-radar
```

3. 在 Codex 中直接调用：

```text
$ai-news-radar 帮我总结最近 7 天最重要的 AI 新闻，按影响力排序，并附上日期和来源链接。
```

也可以这样用：

```text
$ai-news-radar 请只总结这周的开源 AI 新闻，用中文输出。
```

如果你想把输出格式固定下来，也可以配合脚本使用：

```bash
python3 scripts/render_news_brief.py references/sample_brief.json
```
