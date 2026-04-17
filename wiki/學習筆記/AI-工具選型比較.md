# AI 工具選型比較

> Sources: Wilson AI Lab, Unknown
> Raw: [claude-dispatch](../../raw/claude-code/claude-dispatch.md); [hermes-agent-安裝教學](../../raw/ai-agent/hermes-agent-安裝教學.md); [openclaw-discord-部署](../../raw/ai-agent/openclaw-discord-部署.md)

## 定義
Claude Dispatch、OpenClaw、Hermes Agent 是三種讓你遠端控制 AI Agent 的工具，各有不同的目標用戶、設定難度和適用場景。

## 重點整理

**三大工具比較**

| 比較項目 | Claude Dispatch | OpenClaw | Hermes Agent |
|---------|-----------------|----------|--------------|
| 設定難度 | 極低（2 分鐘 QR Code）| 中等（Node.js）| 中等（Git + 一行安裝）|
| 目標用戶 | 非技術用戶 | 開發者、進階用戶 | 進階用戶 |
| 操控介面 | 手機 App（Claude）| Discord / API | Telegram Bot |
| 伺服器 | 本地電腦（需保持開機）| 本地或 VPS | VPS（推薦）或 Windows WSL2 |
| 資安設計 | 本地 sandbox VM | 自行管理伺服器 | 自行管理 |
| 整合工具 | 38+ 官方 Connectors | API 自行串接 | 20+ 模型供應商 |
| 穩定性 | Research Preview ~50% | 取決部署品質 | 取決部署品質 |
| 費用 | Pro $20/月起 | 免費開源 + 伺服器費 | 免費開源 + 伺服器費 |
| 開源 | 否 | 是 | 是（NousResearch）|

**選型建議**
- 不懂技術、想快速上手 → **Claude Dispatch**（官方產品，設定最簡單，38+ 原生 Connectors）
- 需要 Discord 多 Agent 工作團隊 → **OpenClaw**（每個頻道對應一個 Agent）
- 需要 Telegram 控制、24 小時待命的 VPS Agent → **Hermes Agent**（支援 20+ 模型，可從 OpenClaw 一鍵遷移）

**各工具最適合的任務**

| 工具 | 最適合 |
|------|--------|
| Claude Dispatch | 讀 Excel→生成報告→存 Notion→發 Gmail 的串接任務 |
| OpenClaw | 多角色 AI 工作團隊（貿易助理、內容創作、程式助手等）|
| Hermes Agent | 24 小時待命的個人 AI 助理，手機隨時控制 |

**從 OpenClaw 遷移到 Hermes Agent**
- 執行 `hermes claw migrate` 可自動搬移所有設定（SOUL.md、記憶、Skills、API Keys）
- 遷移是複製操作，不會刪除原本的 OpenClaw 資料
- 可以兩者同時使用，針對不同任務選擇不同工具

## 延伸閱讀
- [[Claude-Dispatch]]
- [[OpenClaw-Discord部署]]
- [[Hermes-Agent]]

## 來源
- raw/Claude Dispatch 初級使用指南.pdf
- raw/HermesAgent_install_guide_final.pdf
- raw/OpenClaw_Discord_教學指南.pdf
