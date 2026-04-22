# Claude Routines

> Sources: Hei.AI, Unknown
> Raw: [claude-routines-自動化任務](../../raw/claude-code/claude-routines-自動化任務.md)
> Updated: 2026-04-22

## 定義

Claude Routines 是讓 Claude 定時自動執行完整任務工作流的功能，像「會思考的鬧鐘」，觸發後能自動搜尋資料、分析內容、並推送結果到 Notion / Slack / Gmail 等服務。

## 重點整理

**三種觸發方式**
- **定時排程**：每小時、每天、每週固定時間執行
- **API 觸發**：從外部系統發 HTTP 請求觸發
- **GitHub Event**：當有新 PR 或 Release 時自動執行

**Local vs Remote 的關鍵差異**

| 模式 | 執行環境 | 電腦關機是否執行 |
|------|----------|----------------|
| Local | 自己的電腦 | 否，電腦必須開機 |
| Remote | Claude 雲端 | 是，雲端持續執行 |

→ **除非有特殊理由，否則一定要明確要求 Remote 模式**

**7 步搭好一個 Routine**
1. 打開 Claude Code（Desktop App 或 claude.ai）
2. 用自然語言描述需求（不需要自己寫 Prompt）
3. 回答 AI 的澄清問題（輸出存到哪、監控哪些來源）
4. 明確要求「幫我建立 Remote 版本的 Routine」
5. AI 自動完成系統搭建（裝工具、寫腳本、建 DB、設觸發時間）
6. **必須按 Run Now 測試**（完成首次授權，否則之後自動執行會卡住）
7. 繼續用自然語言修改：「幫我加一個 XX 功能」

**使用限制**

| 方案 | 每日執行次數上限 |
|------|----------------|
| Pro | 5 次 |
| Max | 15 次 |
| Team / Enterprise | 25 次 |

- 複雜多步驟工作流做不好（只有一個 Prompt 控制全部）
- 不像 n8n 可以每一步分開控制，出問題難以定位
- 目前仍在 Research Preview 階段，功能和限制可能改變

**適用場景範例**
- 每天早上 8 點搜集最新 AI 資訊整理放入 Notion
- 每天追蹤 YouTube 頻道新影片，自動翻譯字幕做繁中摘要
- 每天早上 9 點檢查 Gmail 未回覆郵件，生成回覆草稿

## 延伸閱讀
- [[Claude-Code-Skills]]
- [[Claude-Code-進階功能]]
- [[Claude-Dispatch]]

## 來源
- raw/Hei.ai_claude_routines_新功能：讓_ai_每天自動幫你做事.pdf
