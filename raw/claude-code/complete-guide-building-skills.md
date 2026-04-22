---
source: raw/The-Complete-Guide-to-Building-Skill-for-Claude.pdf; raw/The-Complete-Guide-to-Building-Skill-for-Claude.zh-tw.pdf
collected: 2026-04-22
published: Unknown
---

# The Complete Guide to Building Skills for Claude（完整指南：打造 Claude 的技能）

官方 Anthropic 出版的完整 Skill 開發指南，涵蓋從規劃到發佈的所有流程。

## Ch1. 基礎（Fundamentals）

### Skill 是什麼

Skill 是一個**資料夾**，包含：
- `SKILL.md`（必填）：含 YAML frontmatter 的 Markdown 指引
- `scripts/`（選填）：可執行程式碼（Python、Bash 等）
- `references/`（選填）：需要載入的文件
- `assets/`（選填）：輸出使用的範本、字型、圖示

### 核心設計原則

**漸進式揭露（Progressive Disclosure）**：3 層系統
- **第一層（YAML frontmatter）**：永遠載入 system prompt，告訴 Claude 何時用此 skill，不必把全部內容載入上下文
- **第二層（SKILL.md 主體）**：Claude 認為 skill 相關時載入，包含完整指示
- **第三層（連結檔案）**：skill 目錄中的其他檔案，Claude 視需求自行瀏覽探索

→ 最小化 token 消耗，同時維持專業能力

**可組合性**：Claude 可同時載入多個 skill，skill 之間不衝突

**可攜性**：skill 在 Claude.ai、Claude Code、API 上完全相同運作，一次建立跨平台使用

### MCP + Skills 廚房比喻

- MCP 提供「專業廚房」：工具、食材、設備
- Skills 提供「食譜」：一步步教你如何做出有價值的東西

沒有 skills 的 MCP 用戶：連上了但不知道下一步、每次對話重新開始、結果不一致
有了 skills：預建工作流自動啟用、工具使用一致可靠、最佳實務內建每次互動

## Ch2. 規劃與設計（Planning and Design）

### 從使用情境開始

寫任何程式碼前，先找出 2-3 個 skill 應支援的具體使用情境。

良好的使用情境定義範例：
```
使用情境：專案 Sprint 規劃
觸發條件：使用者說「幫我規劃這個 sprint」或「建立 sprint 任務」
步驟：
1. 從 Linear 取得目前專案狀態（透過 MCP）
2. 分析團隊速度與產能
3. 建議任務優先順序
4. 在 Linear 中建立任務，加上適當標籤與估點
結果：完成規劃的 sprint，且任務已建立
```

### 三種常見 Skill 類別

**類別 1：文件與資產製作**
- 用途：產出一致且高品質的內容，包括文件、簡報、應用程式、設計、程式碼
- 關鍵技巧：內嵌風格指南與品牌規範、範本結構確保輸出一致、定稿前的品質檢查清單

**類別 2：工作流程自動化**
- 用途：可受益於一致方法論的多步驟流程，包括跨多個 MCP 伺服器的協作
- 關鍵技巧：具驗證關卡的逐步工作流程、常見結構範本、內建審查和改善建議、反覆迭代的精煉循環

**類別 3：MCP 強化**
- 用途：提供工作流程引導，強化 MCP 伺服器所提供的工具存取能力
- 關鍵技巧：依序協調多次 MCP 呼叫、內嵌領域專業知識、提供使用者原本需要自行指定的脈絡、針對常見 MCP 問題的錯誤處理

### 技術需求

**檔案結構：**
```
your-skill-name/
├── SKILL.md          # 必要
├── scripts/          # 選填
│   ├── process_data.py
│   └── validate.sh
├── references/       # 選填
│   └── api-guide.md
└── assets/           # 選填
    └── report-template.md
```

**關鍵規則：**
- 檔案必須命名為 `SKILL.md`（區分大小寫，無例外）
- 資料夾名稱用 kebab-case（例：`notion-project-setup`）
- 不要在 skill 資料夾內放 README.md（說明文件放 SKILL.md 或 references/）

**YAML frontmatter 必填欄位：**
```yaml
---
name: your-skill-name
description: 它做什麼。當使用者詢問 [特定使用片語] 時使用。
---
```

- `name`：kebab-case，無空格、無大寫，應與資料夾名稱一致
- `description`：必須同時包含「做什麼」和「何時使用（觸發條件）」，1024 字元以內，不含 XML 標籤

**description 好壞範例：**
- 好：`分析 Figma 設計檔並產生開發交付文件。當使用者上傳 .fig 檔、詢問「design specs」、「component documentation」或「design-to-code handoff」時使用。`
- 壞：`有助於專案。`（太模糊）/ `建立精密的多頁文件系統。`（沒有觸發條件）

**安全限制（frontmatter 禁止）：**
- XML 角括號（`< >`）
- 名稱含有「claude」或「anthropic」（保留字）
- 原因：frontmatter 會出現在 Claude 的 system prompt 中，惡意內容可能注入指令

## Ch3. 測試與迭代（Testing and Iteration）

### 測試方式

1. **在 Claude.ai 進行手動測試**：直接執行查詢並觀察行為，快速迭代，無需設定
2. **在 Claude Code 進行腳本化測試**：自動化測試案例，以便在變更間可重複驗證
3. **透過 skills API 進行程式化測試**：建立評估套件，針對定義好的測試集系統性執行

### 三個測試面向

**1. 觸發測試**：確保技能在正確時機載入
- 應觸發：明顯任務、改寫後的請求
- 不應觸發：不相關主題

**2. 功能測試**：驗證技能產出正確輸出
- 有效輸出、API 呼叫成功、錯誤處理正常運作、邊界案例涵蓋

**3. 效能比較**：證明技能相較於基準能改善結果
- 與 vs. 不使用 skill 的 token 消耗、來回次數、API 呼叫失敗次數比較

### skill-creator 工具

- 內建於 Claude.ai，也可下載用於 Claude Code
- 可從自然語言描述生成技能、產出格式正確的 SKILL.md with frontmatter
- 建議觸發語：「使用 skill-creator 技能協助我建立一個技能，用於 [你的使用情境]」

### 迭代訊號

**觸發不足**：skill 沒載入時 → 在 description 中加入更多細節和細微差異（包含關鍵字，特別是技術術語）

**過度觸發**：skill 載入不相關查詢 → 加入負向觸發條件，更具體

## Ch4. 發佈與分享（Distribution and Sharing）

### 取得 Skills 的方式

個別使用者：
1. 下載 skill 資料夾
2. 視需要壓縮為 zip
3. 透過 Settings > Capabilities > Skills 上傳到 Claude.ai
4. 或放入 Claude Code 的 skills 目錄

組織層級：管理員可部署 skills 工作區域全體（2025 年 12 月 18 日推出）、自動更新、集中式管理

### 透過 API 使用 Skills

- `/v1/skills` 端點列出與管理 skills
- 透過 `container.skills` 參數加入 Messages API 請求
- 適用場景：應用程式中以程式化方式使用技能、大規模生產部署、自動化管線與代理系統

### 開放標準

Anthropic 已將 Agent Skills 發佈為開放標準，與 MCP 類似，skill 應能在各種工具和平台間攜帶移植。

## Ch5. 模式與疑難排解（Patterns and Troubleshooting）

### 5 大常見 Skill 模式

**模式 1：順序工作流程協調（Sequential workflow orchestration）**
- 使用時機：使用者需要以特定順序執行多步驟流程
- 關鍵技巧：明確步驟順序、步驟間的依賴關係、每個階段的驗證、失敗時的回滾指示

**模式 2：多 MCP 協調（Multi-MCP coordination）**
- 使用時機：工作流程橫跨多個服務
- 關鍵技巧：清晰的階段分離、MCP 之間的資料傳遞、進入下一個階段前的驗證、集中式錯誤處理

**模式 3：迭代精煉（Iterative refinement）**
- 使用時機：輸出品質可透過迭代改善
- 關鍵技巧：明確品質標準、迭代改善、驗證腳本、知道何時停止迭代

**模式 4：上下文感知工具選擇（Context-aware tool selection）**
- 使用時機：同樣結果但根據上下文使用不同工具
- 關鍵技巧：清晰決策標準、後備選項、對使用者透明說明選擇原因

**模式 5：領域特定智識（Domain-specific intelligence）**
- 使用時機：skill 為工具存取之外增添專業知識
- 關鍵技巧：領域專業嵌入邏輯、行動前合規確認、完整文件、清晰治理

### 常見疑難排解

**Skill 無法上傳：**
- 錯誤「Could not find SKILL.md」→ 檔名需完全是 `SKILL.md`（區分大小寫）
- 錯誤「Invalid frontmatter」→ YAML 格式問題，確認有 `---` 分隔符號

**Skill 不觸發：**
- description 太模糊，需包含使用者可能說的具體短語
- 調試方式：問 Claude「你什麼時候會使用 [skill 名稱] skill？」

**Skill 觸發太頻繁：**
- 加入負向觸發條件（description 中說明「Do NOT use for...」）

**指令未被遵循：**
- 指令太冗長 → 保持精簡，使用條列和編號清單
- 重要指令被淹沒 → 關鍵指令放最上面，使用 `## Important` 或 `## Critical` 標題
- 語言模糊 → 用明確語言，例如 `CRITICAL: Before calling create_project, verify:...`

**大型上下文問題（回應變慢）：**
- SKILL.md 內容太大 → 移至 references/，用連結替代，保持 SKILL.md 在 5000 字以內
- 同時啟用太多 skill → 若有 20-50 個以上，考慮選擇性啟用或 skill 「套件」組合

## Ch6. 資源與參考（Resources and References）

### Quick Checklist（上傳前確認）

- 資料夾名稱為 kebab-case
- SKILL.md 檔案存在（拼法正確）
- YAML frontmatter 有 `---` 分隔符號
- `name` 欄位：kebab-case、無空格、無大寫
- `description` 包含「做什麼」和「何時使用」
- 沒有 XML 標籤（`< >`）
- 指令清晰且可執行
- 包含錯誤處理
- 提供範例
- 清楚引用附帶資源
