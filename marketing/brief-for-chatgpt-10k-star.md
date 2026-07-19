# 给 ChatGPT 的 brief v2 — 请完整复制粘贴到 chatgpt.com

---

## 你是谁（这次的角色）

你是 **「用 AI 工具组合做开源项目并冲击 10k GitHub stars」的方法论顾问**。我是一个独立开发者，想要弄清楚：在 2026 年的今天，用 ChatGPT 网页版 + Claude Code（MiniMax-M3 模型内核）这套 AI 工具组合，怎么从 0 到 1 做出一个 **第一个 10k star 的 GitHub 项目**。

不是做 marketing，是做**项目选择 + 工作流设计 + 工具编排** 的顶层策略。

---

## 我的工具栈（固定不变）

| 工具 | 用法 | 限制 |
|---|---|---|
| **ChatGPT 网页版** | brainstorming, strategy, market research, 写作 | 只能输出文字 (代码要在 Claude Code 里写) |
| **Claude Code (MiniMax-M3)** | coding, debugging, deep research (workflow agent), git 操作, GitHub API | 中文 developer, 本机 Windows 11 + Rust 1.94 + Python 3.13 + Node 24 + GitHub CLI |
| **GitHub** | repo hosting, Actions CI, Releases, Issues | 已有 kezhu-ai (恢复后) + kezhu-ai 两个账号 |
| **mcp__plugin__context7** | 实时查库文档 | 这次可能不需要 |
| **browser automation 栈** | cloakbrowser + firecrawl + agent-reach (13 平台) + intelligence-gather skill | 做 research / 抓社区帖子 |
| **deep-research workflow** | 调研流水线 (multi-agent parallel + adversarial verify) | 但上次跑抓 Reddit/HN 翻车过，需要走直连 API 路径 |

---

## 我已有的资产（背景）

我已经做了一个 **ctxguard** 项目 (Rust CLI, 跨 Claude Code + Codex CLI 的 context-window budget 工具):

- 21 commits + v0.1.0 / v0.2.0 两个 release
- 跨平台 binary (Linux + macOS Apple Silicon + 部分 Windows)
- 真数据: 812x faster than ccusage, 2.1B context tokens 真实发现
- Display name "祝可", bio 设置
- **0 stars / 0 watchers** (截至 2026-07-19)
- 当前 mirror 到两个账号: `kezhu-ai/ctxguard` + `kezhu-ai/ctxguard`

**ctxguard 是我的 "trail run" 试水项目**, 我想从中学习经验, 然后用同样工作流**做下一个更可能爆的项目**。

---

## 我的 5 个核心问题（按优先级）

### Q1 (最重要): 选题策略 — 下一个项目该做什么?

(a) **赛道选择**: 2026 年下半年, 哪些赛道最可能让一个独立开发者的开源项目冲到 10k stars? 候选我初步想到的方向:
   - AI agent infrastructure (MCP server / context window / agent debugger)
   - Developer DX CLI (替代 git/docker/kubectl/tailwind 之类的老工具)
   - Local-first / privacy-first SaaS 的开源版
   - LLM 微调 / 数据集工具
   - AI cost observability (LangSmith/Helicone 替代)
   - 中国开发者专门工具 (国内 LLM API 代理 / 钉钉飞书集成 / 微信支付 SDK)

请基于 GitHub Trending 历史 (2024-2026), 告诉我哪些赛道最可能爆, **并且具体推荐 5 个细分垂直方向** (不是宽泛的"AI infra", 而是"AI agent 的对话历史压缩工具"这种颗粒度)。

(b) **差异化定位**: 在你推荐的每个细分方向, 现有 top 项目是什么 (列 3-5 个 + star 数 + 痛点)? 我的新项目能切哪个具体空隙? 不要泛泛说"做差异化", 要具体到 "现有 X 项目没做 Y, 但 Reddit 上 W 个帖子抱怨需要 Y"。

(c) **10k star 真实门槛**: 在 2026 年, 一个**单人维护**的开源项目冲到 10k stars 实际需要什么? 不要给我 2020 年的过时建议 ("写好 README + 发 Show HN + 等"), 要 2026 年的 distribution 矩阵 (Show HN / Reddit / X / 中文社区 / YouTube / KOL / Hacker Newsletter / Product Hunt 等)。

### Q2: 工具组合工作流 — ChatGPT 和 Claude Code 怎么分工?

请画出 **完整的工作流图**, 包括:

(a) **哪个阶段用 ChatGPT, 哪个用 Claude Code**? 比如:
   - "市场调研" → ChatGPT (你能跑更长的 brainstorm)
   - "代码实现" → Claude Code (有 file/git/test)
   - "README + Show HN 文案" → ChatGPT (writing skill 强)
   - "deep research / 用户访谈" → Claude Code (用 deep-research workflow + browser 自动化)

(b) **怎么避免工具切换的 context loss**? 比如 ChatGPT 给我一个 1000 字的战略分析, 我怎么**无损传给 Claude Code** 让它执行? 当前做法: 我手动复制粘贴 → ChatGPT 输出就被存到 `~/.claude/projects/` 对话历史 → 长期 risk。

(c) **有没有更优的编排**: 比如我是不是应该把 ChatGPT 当 "顾问", Claude Code 当 "执行者", 通过一个共享的 markdown 文件做 handoff? 还是用 GitHub Issues / Notion / Obsidian? 给我具体的 handoff 流程。

### Q3: 投放时机 — 什么时候 launch?

(a) **2026 年下半年有没有特殊的 launch 时机**? (Black Friday / Hacktoberfest / 圣诞节 / 春节 / GitHub Universe / 等)

(b) **Reddit / Hacker News / X / V2EX 的最佳发稿时间** (考虑用户群跨时区)

(c) **我应该提前多久准备 release artifacts** (README / demo.gif / Show HN draft / benchmarks)?

### Q4: 营销放大器 — 怎么从 0 到 1000 个真实用户?

不要告诉我 "发 Twitter / Reddit" 这种废话. 给我**具体 4 周 action plan**:

- 周一-周日排期
- 每个动作的执行步骤 + 模板 (e.g. "Show HN 标题格式: Show HN: <工具> – <一句话价值 prop, with <量化数据>")
- KOL / Newsletter 列表 (具体名字, 不要 "find AI influencers")
- 中国开发者社区 (V2EX / 掘金 / 知乎 / 哔哩哔哩) 的具体打法 (中外差别很大)

### Q5: 数据驱动 — 怎么知道哪些项目会爆, 哪些不会?

请给我**预判指标清单**:

- 一个新 GitHub repo 上线 48 小时内, 哪些数字能预判 "会爆" vs "会沉"?
  (e.g. "前 24 小时 stars > 50 + Show HN 上首页" 是个好信号)
- 哪些早期 engagement 指标比 stars 数更重要?
  (e.g. fork rate / issue open rate / retention)
- 怎么用 Playwright / GitHub API **自动监控自己项目的指标**, 而不必每天手动看?

---

## 期望输出格式

请用 **单一长 Markdown 文档**, 分 6 大节:

1. **赛道推荐 TOP 5** (每个 100-150 字, 含竞品 + 切入点)
2. **工具组合工作流图** (Mermaid 或 ASCII diagram 都可以)
3. **2026 下半年 launch 时机表** (日历格式)
4. **4 周 marketing 排期** (4 个表, 每个 7 行)
5. **预判指标清单** (指标名 + 阈值 + 监控方法)
6. **我应该立即做的 3 件事** (明天就动手, 不要 4 周后才做)

---

## 不要做的事

- 不要问我澄清问题 (所有需要的信息上面都有)
- 不要给通用 startup advice ("找到 PMF", "做用户访谈") — 要 actionable 步骤
- 不要推荐 2020 年的过时做法 ("写博客 / 做 SEO")
- 不要假设我有大预算 ("投 Google Ads") — 我是个人开发者, 预算 = $0
- 不要给我"积极正面的鼓励" — 我需要的是 cold-eyed 评估, 不是鸡汤

---

## 补充背景 (如果你问起, 我会再贴)

如果你的回答里需要这些具体数据, 直接问, 我再贴:

- 当前 ctxguard 项目的真 benchmark (812x vs ccusage, 14 MB Claude Code session → 37 ms / ccusage 30s)
- 我手上的 3 个 GitHub PAT (都暴露在对话里了, 安全风险已知)
- 我能调用的 browser automation 栈细节 (cloakbrowser 路径 / firecrawl-local / agent-reach doctor 输出)
- 我能用的 wiki 系统 (`~/.claude/wiki/`) 里的循环沉淀 (deep-research 失败教训 / render-demo vhs 失败原因 / Claude Code Windows bsdtar 坑等)

---

请直接开始输出完整规划, 不要先问问题。