# OpenClaw Discord 部署

> Sources: WilsonAILab, Unknown
> Raw: [openclaw-discord-部署](../../raw/ai-agent/openclaw-discord-部署.md)

## 定義
OpenClaw 是一個多 Agent 系統，可部署到 Discord，讓每個頻道對應一個專屬 AI Agent，實現 AI 工作團隊，無需程式底子即可在 30 分鐘內完成。

## 重點整理

**前置需求**
- 一台電腦（Windows / Mac / Linux 均可）
- Discord 帳號 + 自己的 Discord 伺服器
- Node.js 已安裝（nodejs.org 免費下載）
- 已申請 OpenClaw API Key 或使用開源版本

**8 步部署流程**

1. **建立 Discord Bot**：前往 discord.com/developers/applications → New Application → 建立 Bot → 複製 Token（只顯示一次！）→ 開啟 Message Content Intent 和 Server Members Intent
2. **取得頻道 ID**：Discord 設定 → 進階 → 開啟「開發者模式」→ 對頻道右鍵 → 複製頻道 ID
3. **安裝 OpenClaw**：`npm install -g openclaw`
4. **設定 Discord 頻道**：`openclaw setup` → 選 Discord (Bot API) → 貼上 Bot Token
5. **建立 Sub-Agents**：`openclaw agents add trader; openclaw agents add content; ...`（支援 trader、content、artist、coder、researcher、sales、blogger）
6. **綁定 Agent 到頻道**：`openclaw agents bind --agent trader --bind discord:頻道ID`（頻道 ID 為純數字）
7. **啟動 Gateway**：本機用 `openclaw gateway start`；VPS 用 `nohup openclaw gateway start > /tmp/openclaw-gateway.log 2>&1 &`
8. **測試驗證**：在 Discord 對應頻道傳訊息，AI Agent 應自動回應

**確認成功 Checklist**
- Bot 在 Discord 伺服器顯示上線（綠點）
- `openclaw gateway probe` 顯示 Reachable: yes
- `openclaw agents list` 每個 Agent 的 Routing rules = 1
- WebUI（`openclaw open`）可以正常開啟

**常見問題速查**
- Agent 沒回應 → 執行 `openclaw gateway probe` 確認狀態
- 關 SSH 後 Gateway 停了 → 改用 nohup 背景執行
- Routing rules 顯示 0 → 重新執行 bind 指令，確認頻道 ID 為純數字
- Bot Token 失效 → 到 Discord Developer Portal 重新 Reset Token

## 延伸閱讀
- [[Hermes-Agent]]
- [[Claude-Dispatch]]
- [[AI-工具選型比較]]

## 來源
- raw/OpenClaw_Discord_教學指南.pdf
