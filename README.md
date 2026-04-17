# Kenny-Wiki 個人知識庫

以 Claude Code 維護的個人 AI 工具學習知識庫，搭配 AI 查詢儀表板，讓知識可以被對話式搜尋。

## 資料夾結構

```
Kenny-Wiki/
├── raw/                  # 原始資料（只讀，不修改）
│   ├── claude-入門/
│   ├── claude-code/
│   └── ai-agent/
├── wiki/                 # AI 維護的 Wiki 文章
│   ├── 工具使用/         # Claude 工具操作指南
│   ├── 學習筆記/         # 整合性知識與比較
│   ├── index.md          # 總索引
│   └── log.md            # 操作日誌
├── dashboard/            # AI 查詢介面
│   ├── app.py            # FastAPI 後端
│   ├── requirements.txt
│   └── static/           # 前端（HTML / CSS / JS）
├── .claude/              # Claude Code 技能包
│   └── skills/karpathy-llm-wiki/
├── .env.example          # LLM 設定範本
├── CLAUDE.md             # Claude Code 專案規則
└── README.md
```

## 快速開始

### 1. 複製設定檔

```bash
cp .env.example .env
```

編輯 `.env`，選擇 LLM Provider 並填入對應的 API Key：

```env
# 選擇其中一個：ollama | openai | gemini | anthropic
LLM_PROVIDER=ollama

# Ollama（本地端，無需 API Key）
OLLAMA_BASE_URL=http://localhost:11434/v1
OLLAMA_MODEL=llama3.2

# OpenAI
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4o-mini

# Google Gemini
GEMINI_API_KEY=...
GEMINI_MODEL=gemini-2.0-flash

# Anthropic Claude
ANTHROPIC_API_KEY=sk-ant-...
ANTHROPIC_MODEL=claude-sonnet-4-6
```

### 2. 啟動查詢儀表板

```bash
cd dashboard
uv run uvicorn app:app --reload --port 8765
```

瀏覽器開啟 `http://localhost:8765`

## Wiki 操作指令

在 Claude Code 中使用以下指令維護知識庫：

| 指令 | 說明 |
|------|------|
| `ingest` | 讀取 `raw/` 新資料，更新 Wiki 文章與索引 |
| `query [問題]` | 從 Wiki 查詢並回答 |
| `lint` | 檢查 Wiki 的格式和連結是否正確 |

## 新資料加入流程

### Step 1：把原始檔案放入 `raw/`

將 PDF 或任何來源資料放到對應的子目錄：

```
raw/
├── claude-入門/      ← Claude 基礎相關
├── claude-code/      ← Claude Code 工具相關
└── ai-agent/         ← AI Agent 工具相關
```

主題不屬於現有分類時，直接新建子目錄即可。

> ⚠️ `raw/` 裡的原始檔案**永遠不要修改或刪除**，它是知識庫的唯一資料來源。

### Step 2：執行 ingest

在 Claude Code 輸入：

```
ingest
```

Claude Code 會自動完成：
- 讀取 `raw/` 中的新資料
- 判斷新增文章或合併到現有文章
- 建立或更新 `wiki/` 文章
- 同步更新 `wiki/index.md`
- 寫入 `wiki/log.md` 操作紀錄

### Step 3：確認結果

| 確認項目 | 說明 |
|---------|------|
| `wiki/index.md` 已更新 | 新文章出現在列表中 |
| 交叉連結完整 | 新文章有被其他相關文章的延伸閱讀連結到 |
| 無孤立文章 | 每篇文章至少被一篇其他文章連結 |

如有格式或連結問題，執行：

```
lint
```

### Step 4：Commit

```bash
git add raw/ wiki/
git commit -m "新增：XXX 筆記"
```

### 完整流程

```
放檔案到 raw/  →  ingest  →  確認 wiki/  →  （選用）lint  →  git commit
```

完成後重新整理儀表板即可用 AI 查詢新知識。

## Wiki 文章分類

**工具使用**
- Claude 模型方案比較（Free / Pro / Max）
- CLAUDE.md 入門指南
- Claude Code Skills
- Claude Dispatch
- Firecrawl 整合
- Hermes Agent
- OpenClaw Discord 部署

**學習筆記**
- Claude Code 進階功能（CLAUDE.md / Skills / Subagents / Hooks）
- AI 工具選型比較（Dispatch vs OpenClaw vs Hermes）

## 技術架構

- **知識庫維護**：Claude Code + karpathy-llm-wiki skill
- **查詢介面後端**：FastAPI + Server-Sent Events（串流回覆）
- **LLM 支援**：Ollama（本地）/ OpenAI / Gemini / Anthropic
- **前端**：純 HTML / CSS / JS + marked.js（Markdown 渲染）
- **套件管理**：uv
- **Wiki 閱讀器**：Obsidian（`wiki/` 資料夾）
