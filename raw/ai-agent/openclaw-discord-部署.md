# OpenClaw 部署到 Discord 完整步驟教學指南

> Source: raw/OpenClaw_Discord_教學指南.pdf
> Collected: 2026-04-17
> Published: Unknown

OpenClaw 多 Agent 系統部署到 Discord，讓每個頻道對應一個專屬 AI Agent，實現真正的 AI 工作團隊。WilsonAILab 出品。

- 完整步驟：8 步
- 支援 Agent 數：7
- 完成時間：約 30 分鐘
- 需要程式底子：否

## 前置需求

- 一台電腦（Windows / Mac / Linux 均可）
- Discord 帳號 + 自己的 Discord 伺服器
- Node.js 已安裝（nodejs.org 免費下載）
- 已申請 OpenClaw API Key 或使用開源版本

## Step 1：建立 Discord Bot

1. 前往 discord.com/developers/applications
2. 點 New Application → 輸入 Bot 名稱（例如：WilsonAIBot）
3. 左側選 Bot → 點 Add Bot → 確認建立
4. 點 Reset Token → 複製 Bot Token（只會顯示一次！請立即保存）
5. 開啟 Privileged Gateway Intents 的兩個選項：Message Content Intent、Server Members Intent
6. 前往 OAuth2 → URL Generator，勾選 Scopes：bot、applications.commands；Permissions：Send Messages、Read Messages/View Channels
7. 複製邀請連結，把 Bot 加入你的 Discord 伺服器

## Step 2：取得 Discord 頻道 ID

Discord → 使用者設定 → 進階 → 開啟「開發者模式」
對每個要綁定的頻道右鍵 → 複製頻道 ID

預設 Agent 對應：trader、content、artist、coder、researcher、sales、blogger

## Step 3：安裝 OpenClaw

```bash
npm install -g openclaw
openclaw --version  # 確認安裝成功
```

## Step 4：設定 Discord 頻道

```bash
openclaw setup
# 選擇 Channel 類型 → 選 Discord (Bot API)
# 填入 Step 1 取得的 Bot Token
# 其餘選項按 Enter 使用預設值
```

設定完成後，設定檔存在 `~/.openclaw/openclaw.json`

## Step 5：建立 Sub-Agents

```bash
# 一行全部建立
openclaw agents add trader; openclaw agents add content; openclaw agents add artist; openclaw agents add coder; openclaw agents add researcher; openclaw agents add sales; openclaw agents add blogger

# 確認建立成功
openclaw agents list
```

## Step 6：綁定 Agent 到 Discord 頻道

```bash
openclaw agents bind --agent trader --bind discord:你的頻道ID
openclaw agents bind --agent content --bind discord:你的頻道ID
# ... 重複所有 Agent
```

執行 `openclaw agents list` 確認每個 Agent 的 Routing rules = 1。頻道 ID 為純數字。

## Step 7：啟動 Gateway

```bash
# 本機（前景執行）
openclaw gateway start

# VPS 伺服器（背景執行，斷線不中斷）
nohup openclaw gateway start > /tmp/openclaw-gateway.log 2>&1 &

# 確認成功
openclaw gateway probe  # 看到 Reachable: yes 代表正常
openclaw open           # 開啟 WebUI
```

## Step 8：測試與驗證

到 Discord 在對應頻道傳訊息，AI Agent 應該自動回應。

## 完成 Checklist

- Discord 伺服器中看到 Bot 上線（綠點）
- 在綁定的頻道傳訊息，對應 Agent 有回應
- `openclaw gateway probe` 顯示 Reachable: yes
- `openclaw agents list` 每個 Agent 的 Routing rules = 1
- WebUI（openclaw open）可以正常開啟

## 常見問題排查

| 問題 | 解法 |
|------|------|
| WebUI 顯示 Unauthorized | 用 openclaw open，或網址後加 ?token=你的token |
| Agent 沒有回應 | 執行 openclaw gateway probe 確認狀態，若掛掉重新啟動 |
| 關 SSH 後 Gateway 停了 | 改用 nohup 背景執行方式 |
| Model request timed out | 在 WebUI 更換 LLM 模型 |
| Routing rules 顯示 0 | 重新執行 bind 指令，確認頻道 ID 格式正確（純數字）|
| Bot Token 失效 | 到 Discord Developer Portal 重新 Reset Token |

## 重啟 Gateway 指令

```bash
ps aux | grep openclaw        # 找到 PID
kill -9 你的PID               # 殺掉舊的
nohup openclaw gateway start > /tmp/openclaw-gateway.log 2>&1 &
sleep 3 && openclaw gateway probe  # 確認成功
```
