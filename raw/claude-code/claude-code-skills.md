# Claude Code Skills：用這 3 層架構，讓 AI 真正幫你工作

> Source: raw/Claude Code Skills：用這 3 層架構，讓 AI 真正幫你工作_Resource.pdf
> Collected: 2026-04-17
> Published: Unknown

Skill 就是你給 Claude Code 的一份可重複使用的指令。把一個流程寫清楚，存成 skill，之後一個指令就跑，結果越來越穩定。最簡單的比喻：Skill = AI 的 SOP（標準作業流程）。

## 三大理由

1. **個人效率**：同時跑 4 個 agent，不是 10% 提升，是 10 倍
2. **團隊槓桿**：SOP 數位化，整個組織一起升級
3. **好時機**：Skill 生態系剛起步，現在學走在前面

## Skill 能做的事

- 執行多步驟流程（腳本生成、資料分析、報告整理）
- 呼叫 API、執行 script、建立檔案
- 啟動 sub-agent，讓多個 agent 並行工作
- 跨專案被呼叫（global skill）

## Skill 解剖：SKILL.md 結構

一個 skill 就是一個 SKILL.md 檔案，分為兩個部分：

**Part 1 · Frontmatter（用 --- 包起來）**
```yaml
---
name: transcript
description: Use when Jay provides a video outline and asks for a script...
---
```

**Part 2 · Instructions（步驟指令）**
```
Step 1 讀 patterns.md，套用風格規則
Step 2 根據大綱生成完整腳本
Step 3 存檔，auto-trigger Phase 1.5
```

Frontmatter 必填欄位：`name`、`description`。進階欄位：`allowed_tools`、`argument_hint`、`model`、`disablePromptCaching`。

最佳實踐：保持 SKILL.md 在 500 行以內，詳細的 reference 資料放進支援檔案。

## 支援檔案架構

**Option A · Self-Contained**：支援檔案直接放在 skill 資料夾內，適合獨立的 skill。

**Option B · External References**：支援檔案放在專案其他位置，SKILL.md 內用路徑指向它們。

常見支援檔案類型：風格規則（patterns.md）、品牌資料、資料檔案、執行腳本（Python/JS）。

## 觸發方式

| 方式 | 說明 |
|------|------|
| Slash Command `/transcript` | 明確觸發，直接指定 skill 名稱，即時執行 |
| 自然語言 "幫我寫影片腳本" | 自動搜尋最符合的 skill 並執行 |

自然語言觸發流程：接收請求 → 搜尋 skills（只讀 frontmatter）→ 找到 skill → 執行

## Progressive Context Loading：3 層架構

Claude Code 不會一次把所有 skill 全讀完，用 3 層漸進式載入：

| 層次 | 載入內容 | Token 消耗 |
|------|----------|------------|
| Layer 1 | 只讀 Frontmatter（name + description）| ~100 tokens/skill |
| Layer 2 | 讀完整 Skill 指令 | ~1,000 tokens |
| Layer 3 | 載入支援檔案（references, scripts, templates）| 視需求而定 |

設計意義：Token 成本只在需要時才花，搜尋效率極高，可以有很多個 skill 不怕 token 爆炸。Description 要寫清楚，是 Layer 1 的唯一判斷依據。

## Local vs Global Skill

| 類型 | 位置 | 適用情況 |
|------|------|----------|
| Local | `.claude/skills/{skill-name}/` | 只對這個專案有意義的 skill |
| Global | `~/.claude/skills/{skill-name}/` | 描述你這個人（寫作風格、設計語言、品牌設定）|

## Debug 清單：6 種症狀對照表

| 症狀 | 解法 |
|------|------|
| 步驟順序不對或跳過步驟 | 修改 SKILL.md 指令順序，寫清楚先後關係 |
| 輸出語氣或風格跑掉 | 建立 reference 檔存入風格規則和語氣範例 |
| 同樣的錯誤一直反覆出現 | 在 skill 指令明確加一條「不可以做 XXX」 |
| 一直重複搜尋同樣資訊 | 建立 reference 文件把資訊存起來 |
| Skill 完全沒有觸發 | 回去改 frontmatter description，寫得更具體 |
| Skill 觸發太頻繁 | 在 frontmatter 設定 disablePromptCaching，限制為 slash command only |

## Feedback Cycle

跑 Skill → 看輸出 → 給具體回饋 → Skill 更新，重複循環。

- 前幾次：親眼看著它跑，觀察每個步驟找出改進點
- 持續給具體回饋：「輸出格式不對」不夠用，要說「第三段應該用列表，不是段落文字」
- Skill 穩定（約 10+ 次）後才能放心讓它背景跑

## 三個核心重點

1. Skill = AI 的 SOP，寫一次，反覆用，越用越好
2. 3 層漸進式載入：skill 庫再大也不會拖慢速度，但 description 一定要寫清楚
3. Feedback Cycle：不是一次到位，是邊用邊優化
