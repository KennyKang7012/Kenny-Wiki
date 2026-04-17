# Hermes Agent

> Sources: Wilson 威爾森實驗室, Unknown
> Raw: [hermes-agent-安裝教學](../../raw/ai-agent/hermes-agent-安裝教學.md)

## 定義
Hermes Agent 是開源 AI Agent 系統，支援 VPS 部署和 Windows 本地安裝，可透過 Telegram Bot 進行手機遠端控制，並支援從 OpenClaw 一鍵遷移。

## 重點整理

**安裝前提**
- 只需確認 Git 已安裝（`git --version`）
- Python 3.11、Node.js、ffmpeg 等依賴由安裝腳本自動處理

**VPS 安裝（推薦，24 小時待命）**
```bash
# 一行安裝所有依賴
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
source ~/.bashrc
hermes setup   # 選擇模型供應商（推薦 OpenRouter，支援 20+ 供應商）
hermes doctor  # 健康檢查
hermes         # 啟動
```

**Telegram Bot 綁定（手機控制）**
1. 到 @BotFather 建立 Bot，取得 Token
2. 到 @userinfobot 取得你的 Telegram User ID
3. 執行 `hermes gateway setup` → 選 Telegram → 貼上 Token 和 User ID
4. `hermes gateway install` + `hermes gateway start`（設定為開機自動啟動）

**Windows 本地安裝**
- 先安裝 WSL2（PowerShell 管理員執行 `wsl --install`，重開機）
- 打開 Ubuntu App，在 Ubuntu 中執行相同的安裝腳本
- 缺點：電腦關機後 Agent 就停，長期使用建議改用 VPS

**從 OpenClaw 一鍵遷移**
```bash
hermes claw migrate --dry-run  # 預覽遷移內容
hermes claw migrate             # 正式執行（複製操作，不會刪除 OpenClaw 資料）
```
自動搬移：SOUL.md、記憶（MEMORY.md / USER.md）、Skills、API Keys、訊息平台設定

**常用指令**

| 指令 | 功能 |
|------|------|
| `hermes` | 啟動對話介面 |
| `hermes doctor` | 健康檢查，診斷問題 |
| `hermes update` | 更新到最新版本 |
| `hermes gateway start/stop/status` | 管理 Gateway |
| `hermes claw migrate` | 從 OpenClaw 遷移 |

## 延伸閱讀
- [[OpenClaw-Discord部署]]
- [[Claude-Dispatch]]
- [[AI-工具選型比較]]

## 來源
- raw/HermesAgent_install_guide_final.pdf
