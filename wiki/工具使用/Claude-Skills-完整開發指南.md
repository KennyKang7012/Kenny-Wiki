# Claude Skills 完整開發指南

> Sources: Anthropic, Unknown
> Raw: [complete-guide-building-skills](../../raw/claude-code/complete-guide-building-skills.md)
> Updated: 2026-04-22

## 定義

Anthropic 官方出版的 Skill 完整開發指南，涵蓋從規劃、技術規格、測試、到發佈分享的所有流程，是建立 Claude Skills 的權威參考文件。

## 重點整理

### Skill 檔案結構

```
your-skill-name/
├── SKILL.md          # 必要（區分大小寫）
├── scripts/          # 選填：可執行程式碼
├── references/       # 選填：需要載入的文件
└── assets/           # 選填：範本、字型、圖示
```

**命名規則：**
- 資料夾：kebab-case（`notion-project-setup` ✅，`Notion Project Setup` ❌）
- 主檔案必須命名為 `SKILL.md`，不接受任何變體（`skill.md`、`SKILL.MD` 均錯誤）
- 不可在 skill 資料夾內放 README.md

### YAML frontmatter 規格

```yaml
---
name: your-skill-name
description: 它做什麼。當使用者詢問 [特定使用片語] 時使用。
---
```

**description 必須同時包含：**
- 做什麼（功能說明）
- 何時使用（觸發條件，列出使用者可能說的具體短語）
- 長度：1024 字元以內，不含 XML 標籤（`< >`）

**好的 description 範例：**
```
分析 Figma 設計檔並產生開發交付文件。當使用者上傳 .fig 檔、
詢問「design specs」、「component documentation」或
「design-to-code handoff」時使用。
```

**安全限制（frontmatter 禁止）：**
- XML 角括號（`< >`）
- 名稱含「claude」或「anthropic」（保留字）

### 三種 Skill 類別

| 類別 | 用途 | 典型範例 |
|------|------|---------|
| 文件與資產製作 | 產出一致且高品質的內容 | 前端設計 skill、PPT 生成 |
| 工作流程自動化 | 可受益於一致方法論的多步驟流程 | skill-creator skill |
| MCP 強化 | 工作流程引導，強化 MCP 工具存取 | Sentry code review skill |

### 三層漸進式揭露（Progressive Disclosure）

| 層次 | 何時載入 | 內容 | Token 消耗 |
|------|----------|------|------------|
| 第一層 | 永遠（system prompt）| YAML frontmatter | 約 100 tokens |
| 第二層 | 認為 skill 相關時 | SKILL.md 主體 | 約 1,000 tokens |
| 第三層 | 按需 | references/、scripts/ 等連結檔案 | 視需求而定 |

### 測試三大面向

1. **觸發測試**：確保 skill 在正確時機載入（90% 相關查詢應觸發）
2. **功能測試**：驗證輸出正確、API 呼叫成功、錯誤處理正常
3. **效能比較**：與不使用 skill 相比，減少 token 消耗和來回次數

**skill-creator 工具：** 內建於 Claude.ai，可從自然語言描述自動生成合規的 SKILL.md

### 5 大 Skill 設計模式

1. **順序工作流程協調**：多步驟有序執行（明確步驟順序、每步驟驗證、失敗回滾）
2. **多 MCP 協調**：工作流程橫跨多個服務（清晰階段分離、集中式錯誤處理）
3. **迭代精煉**：輸出品質透過循環改善（明確品質標準、驗證腳本）
4. **上下文感知工具選擇**：同一結果根據情境選不同工具（清晰決策標準、後備選項）
5. **領域特定智識**：為工具存取之外增添專業知識（領域知識嵌入邏輯）

### 疑難排解速查

| 問題 | 症狀 | 解法 |
|------|------|------|
| 無法上傳 | SKILL.md 找不到 | 確認檔名拼法正確（區分大小寫） |
| 不觸發 | 需手動啟用 | 改寫 description，加入具體觸發短語 |
| 觸發太頻繁 | 載入不相關查詢 | 加入負向觸發（`Do NOT use for...`） |
| 指令未遵循 | Claude 忽略指示 | 精簡指令、重要指令放最上面、用明確語言 |
| 回應變慢 | skill 大且慢 | 移詳細文件至 references/，SKILL.md 保持 5000 字以內 |

### 發佈與分享

- **個人使用**：上傳至 Settings > Capabilities > Skills，或放入 Claude Code skills 目錄
- **組織部署**：管理員可工作區域全體部署（2025/12 起可用）
- **API 使用**：透過 `/v1/skills` 和 `container.skills` 參數程式化管理
- **開放標準**：Anthropic 已將 Agent Skills 定為開放標準，跨平台可攜

## 延伸閱讀
- [[Claude-Code-Skills]]
- [[Claude-Code-進階功能]]
- [[CLAUDE-md-入門指南]]

## 來源
- raw/The-Complete-Guide-to-Building-Skill-for-Claude.pdf
- raw/The-Complete-Guide-to-Building-Skill-for-Claude.zh-tw.pdf
