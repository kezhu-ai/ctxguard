# 给 ChatGPT 的 brief v3 (聚焦版) — 请完整复制粘贴到 chatgpt.com

---

## 你是谁（这次的角色）

你是 GitHub 开源项目的 **launch strategist + naming consultant**。我是一个独立开发者，过去 4 周做了 2 个项目（ctxguard = context budget tool，mcp-sentry = MCP policy firewall），都 0 stars。我现在请你帮我做**最终决策**：**聚焦 1 个项目**（不要再 5 个候选让我选），**不惜代价**做出 10k GitHub stars。给我**项目名 + 一句话定位 + 12 周详细 path**。

不是 brainstorm，是 **commit**。我已经有足够的 idea，你的工作是帮我 **pick one and ship**。

---

## 我的硬约束 (固定不变)

| 维度 | 实际 |
|---|---|
| 开发者 | 1 个人，中文 + 英文 working |
| 时间 | 每周 15-20 小时（下班后 + 周末） |
| 预算 | $0 营销 / $0 工具订阅 / $0 LLM API（用现成订阅） |
| 技术栈 | Rust 1.94 (主) + Python 3.13 + Node 24 + bash |
| 已会 | async Rust, tokio, clap, notify, serde, JSON-RPC, stdio pipe |
| GitHub | kezhu-ai 账号, 可创建 public repo + 配 Actions CI |
| browser 栈 | cloakbrowser + firecrawl-local + agent-reach (13 平台) + intelligence-gather skill |
| 调研能力 | deep-research workflow + HN Algolia + V2EX API + GitHub API 直连 |
| AI 工具 | ChatGPT 网页 (你) + Claude Code MiniMax-M3 (我执行) |
| X / Reddit / V2EX 账号 | 0 followers，**没有任何 baseline audience** |

## 我已经做过的事 (历史 context，避免你让我重做)

- **ctxguard** (Rust CLI): 跨 Claude Code + Codex CLI 的 context budget 工具。21 commits + v0.1.0 + v0.2.0 release，5 个 asset，812x faster than ccusage 的真 benchmark。GitHub kezhu-ai/ctxguard, 0 stars.
- **mcp-sentry** (Rust CLI): MCP policy firewall, list/audit/wrap 3 subcommand + policy.yaml + audit log. 已推 master + v0.1.0-alpha tag, CI red. GitHub kezhu-ai/mcp-sentry, 0 stars.

两个都是**真实 production-grade 项目**。**0 stars 是因为没人发现，不是因为产品烂**。

## 我卡住的地方

我已经发现 ctxguard / mcp-sentry 这种"developer tool for AI agents"赛道是真实的、有用户的，但**单点工具的 10k star 极难**：因为受众太精确（"知道 AI token 浪费" + "用 Claude Code" + "愿意装 CLI" = 10000-100000 人），转化漏斗漏到 100-1000 就停了。

**新洞察**：要 10k star，**需要"AI 时代每个人都会用"的工具**，不是"开发者会用"的工具。这两者受众差 10-100 倍。

## 我要你做的 (聚焦 1 个项目)

请在下面 3 个备选里 **直接选 1 个**（不要再 brainstorm 第 4 个），告诉我:

### 备选 A: AI 时代的"Ctrl+F" — 让任何人都能从自己的全部 AI 对话历史里搜东西
- 痛点: Claude Code / ChatGPT / Cursor 用户的对话历史 = 个人第二大语料库（仅次于邮件）。但**没法搜**。
- 现有: macOS Spotlight 不索引 JSONL，VS Code 搜太慢，grep 太丑
- 候选名: `recall` / `find` / `aha` / `lens`
- 受众: **任何用过 AI coding agent 的人** = 上百万
- 你的工作: 选名 + 定位 + 12 周 path

### 备选 B: AI 时代的"Shell history but for prompts" — 命令行 prompt log + replay
- 痛点: 开发者用 Claude Code 写了 100 个 prompt，但**过几天就找不到 "我让 Claude 写的那个 SQL 是啥"**
- 现有: Claude Code 自带 /resume 但只在 session 内
- 候选名: `promptly` / `recall-cli` / `tape`
- 受众: 重度 Claude Code / Codex CLI 用户 = 1-10 万
- 你的工作: 选名 + 定位 + 12 周 path

### 备选 C: AI 时代的"自己跟自己聊" — 把 100 次 AI 对话"压缩"成一篇可读的日志
- 痛点: 用户每天用 AI 10+ 次，每次 5 分钟，但**下周完全不记得这周跟 AI 聊了啥**
- 现有: 无
- 候选名: `digest` / `journal` / `minutes` / `recollect`
- 受众: **任何每天用 AI 的人** = 上百万
- 你的工作: 选名 + 定位 + 12 周 path

## 你必须输出的格式

**请直接给 1 段 markdown, 不超过 1500 字:**

```markdown
# 1. 选定项目

我选 [A / B / C], 因为 [3 句话理由，基于上面硬约束].

# 2. 项目名

[你选的名字]

# 3. 一句话定位

[填空: 项目名] = [目标人群] + [核心动词] + [核心收益]

# 4. 12 周 path

**W1-2** (MUST): [具体任务 + 可执行步骤]
**W3-4** (MUST): [...]
**W5-8** (NICE): [...]
**W9-12** (DISTRIBUTION): [...]

# 5. 启动动作 (明天就做)

[3 件事，按时间顺序]

# 6. 我应该避免的 3 个错

[基于硬约束的 anti-pattern]
```

## 不要做的事

- ❌ 不要列 5 个候选让我选 (我已经给了 3 个, 你选 1 个)
- ❌ 不要 hedge ("could be A or B depending on...") — 直接 commit
- ❌ 不要加 "depends on what you want" 之类的反问 — 我已经告诉你我想要什么
- ❌ 不要 2000 字以上 — 你自己控制密度
- ❌ 不要建议 "做 marketing / 写博客 / 做 SEO" — 2020 年过时
- ❌ 不要假设我有大预算 — $0

## 输出后再做的事

我会把你这段输出复制回 Claude Code (我执行)。然后 Claude Code 会立即:
1. cargo init + 实现 MVP (W1-2)
2. 录 demo gif
3. 推 GitHub
4. 准备 Show HN 投递素材

**你的工作 = 给最锋利的前 3 步决策。剩下的执行我来做。**

请直接开始输出, 不要先问问题。