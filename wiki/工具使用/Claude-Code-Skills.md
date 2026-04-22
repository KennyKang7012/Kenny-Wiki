# Claude Code Skills

> Sources: JayLuxAI AI 自動化, Unknown
> Raw: [claude-code-skills](../../raw/claude-code/claude-code-skills.md)

## 定義
Skill 是你給 Claude Code 的一份可重複使用的指令（SOP），把一個流程寫清楚存成 SKILL.md 檔案，之後一個指令就跑，結果越來越穩定。

## 重點整理

**三大理由**
- 個人效率：同時跑 4 個 agent，效率提升 10 倍而非 10%
- 團隊槓桿：SOP 數位化，整個組織一起升級
- 時機好：Skill 生態系剛起步，現在學走在前面

**SKILL.md 結構**
```yaml
---
name: transcript
description: Use when user provides a video outline and asks for a script...
---
Step 1 讀 patterns.md，套用風格規則
Step 2 根據大綱生成完整腳本
Step 3 存檔
```
- 必填欄位：`name`、`description`
- 最佳實踐：SKILL.md 保持 500 行以內，詳細資料放支援檔案

**觸發方式**
- Slash Command `/transcript`：明確觸發，直接執行
- 自然語言「幫我寫影片腳本」：Claude Code 自動搜尋最符合的 skill

**Progressive Context Loading：3 層架構**

| 層次 | 載入內容 | Token 消耗 |
|------|----------|------------|
| Layer 1 | 只讀 Frontmatter（name + description）| ~100 tokens/skill |
| Layer 2 | 讀完整 Skill 指令 | ~1,000 tokens |
| Layer 3 | 載入支援檔案（references, scripts）| 視需求而定 |

→ Description 要寫清楚，是 Layer 1 的唯一判斷依據，skill 不觸發就先改 description

**Local vs Global**

| 類型 | 位置 | 適合 |
|------|------|------|
| Local | `.claude/skills/` | 只對此專案有意義的 skill |
| Global | `~/.claude/skills/` | 描述你這個人的 skill（寫作風格、品牌設定）|

**Feedback Cycle（邊用邊優化）**
- 前幾次：親眼看著它跑，觀察每個步驟
- 持續給具體回饋：不是「輸出格式不對」，而是「第三段應該用列表」
- 約 10+ 次後 skill 穩定，才能放心讓它背景跑

**Debug 6 種症狀速查**
- Skill 沒觸發 → 改 frontmatter description，寫得更具體
- 觸發太頻繁 → 設定 `disablePromptCaching`，限制為 slash command only
- 風格跑掉 → 建立 reference 檔存入風格規則
- 同樣錯誤重複 → 在指令明確加「不可以做 XXX」

## 延伸閱讀
- [[CLAUDE-md-入門指南]]
- [[Claude-Code-進階功能]]
- [[Claude-Skills-完整開發指南]]

## 來源
- raw/Claude Code Skills：用這 3 層架構，讓 AI 真正幫你工作_Resource.pdf
