# Hermes Agent 完整安裝部署教學

> Source: raw/HermesAgent_install_guide_final.pdf
> Collected: 2026-04-17
> Published: Unknown

Hermes Agent 是一個開源 AI Agent 系統，支援 VPS 部署和 Windows 本地安裝，可透過 Telegram Bot 進行手機控制。by Wilson 威爾森實驗室。

## 安裝前唯一需要確認

- Git 已安裝（git --version）
- 其他所有依賴（Python 3.11、Node.js、ffmpeg）安裝腳本會自動處理

## Part 1：Hostinger VPS 安裝（推薦）

VPS 部署是最推薦的方式，24 小時待命，手機可隨時透過 Telegram 控制。

```bash
# Step 1：SSH 連線進 VPS
ssh 你的用戶名@你的IP

# Step 2：確認 Git
git --version

# Step 3：一行指令安裝（自動安裝 Python 3.11、Node.js、ripgrep、ffmpeg）
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

# Step 4：重載 Shell
source ~/.bashrc

# Step 5：互動式設定（選擇模型供應商，填入 API Key）
hermes setup

# Step 6：健康檢查
hermes doctor

# Step 7：啟動
hermes
```

設定精靈支援 OpenRouter、Anthropic Claude、Google AI Studio、MiniMax 等 20+ 供應商。推薦選 OpenRouter，支援最多模型。

## Part 2：Telegram Bot 綁定

```bash
# Step 1：到 Telegram 搜尋 @BotFather，建立新 Bot
# /newbot → 輸入 Name（顯示名稱）和 Username（必須以 bot 結尾）
# 複製 Token（格式：123456789:ABCdef...）
# 到 @userinfobot 取得你的 Telegram User ID

# Step 2：設定 Gateway
hermes gateway setup  # 選 Telegram，貼上 Bot Token，輸入 User ID

# Step 3：安裝系統服務（常駐，重開機後自動啟動）
hermes gateway install
hermes gateway start
hermes gateway status  # 看到 active (running) 代表成功
```

## Part 3：Windows 本地安裝（WSL2）

本地安裝的缺點：電腦關機後 Agent 就停了，建議長期使用改用 VPS。

```powershell
# Step 1：以系統管理員身份打開 PowerShell
wsl --install
# 安裝完成後重新開機
```

```bash
# Step 2：打開 Ubuntu App（搜尋「Ubuntu」）
# 在 Ubuntu 中執行（不能在 PowerShell 裡跑）：
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
source ~/.bashrc
hermes setup
hermes gateway setup
hermes gateway start
```

## Part 4：從 OpenClaw 一鍵遷移

遷移是複製操作，不會刪除或修改 OpenClaw 資料。

```bash
# 預覽遷移內容
hermes claw migrate --dry-run

# 正式執行遷移
hermes claw migrate
```

自動搬移項目：SOUL.md（人格設定）、記憶（MEMORY.md、USER.md）、Skills、API Keys、訊息平台設定。

## 常用指令速查

| 指令 | 功能 |
|------|------|
| hermes | 啟動 Hermes 對話介面 |
| hermes setup | 重新執行設定精靈 |
| hermes model | 切換模型供應商 |
| hermes doctor | 健康檢查，診斷問題 |
| hermes update | 更新到最新版本 |
| hermes gateway start | 啟動 Telegram/Discord Gateway |
| hermes gateway stop | 停止 Gateway |
| hermes gateway status | 查看 Gateway 狀態 |
| hermes claw migrate | 從 OpenClaw 遷移 |
