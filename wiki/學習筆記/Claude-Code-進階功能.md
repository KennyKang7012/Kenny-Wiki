# Claude Code 進階功能

> Sources: Wilson AI Lab, Unknown
> Raw: [claude-入門指南](../../raw/claude-入門/claude-入門指南.md)

## 定義
Claude Code 是直接運行於 Terminal 的進階 AI 程式助手，提供 CLAUDE.md、Skills、Subagents、Hooks 四大進階機制，讓你從「使用一套軟體」升級為「領導一個數位團隊」。

## 重點整理

**四大進階機制**

| 機制 | 說明 | 類比 |
|------|------|------|
| CLAUDE.md | 放在專案根目錄，每次啟動自動讀取的大腦指令集 | 部門工作手冊 |
| Skills | 封裝好的 SOP，不佔用 Context，讓 Agent 成為特定領域專家 | 武功秘笈 |
| Subagents | 平行處理複雜任務的臨時工，每個有獨立上下文，互不干擾 | 小弟分隊 |
| Hooks | 系統層級自動化，條件達成後自動觸發動作，100% 執行不依賴 AI 心證 | 自動感應器 |

**CLAUDE.md 放什麼**
- 專案架構說明：這個專案在做什麼
- 程式碼風格規範：變數命名方式
- 格式文件要求：生成檔案類型、HTML 風格
- 語言和常用指令：輸出語言和測試指令
- 禁止事項說明：未經允許不能刪檔案

**Skills Checklist（你的 Skill 寫對了嗎？）**
- 是否有包含「做什麼」以及「何時使用」
- SKILL.md 是否小於 500 字，精簡不複雜
- 路徑設置是否正確，不會找不到檔案
- 複雜操作是否有驗證方式或循環測試
- 若為 Code 是否實際測試過並進行修正

**Subagents 特性**
- 平行處理，多個任務同時進行，不用排隊等
- 每個 Subagent 有自己的 Context，互不干擾
- 打破一問一答限制，給目標就自動規劃到完成

**Hooks 觸發範例**
- Project Status Hooks：開新對話時自動檢查專案進度
- Task Complete Hooks：長時間工作結束自動跳桌面通知
- Code Commit Hooks：上傳前自動執行程式碼審查

**常用指令**

| 指令 | 功能 |
|------|------|
| /compact | 壓縮上下文，避免 Context 爆滿 |
| /account | 查看使用額度和下次重設時間 |
| /init | 初始化專案記憶，建立 CLAUDE.md |
| /clear | 清除當前對話 |
| /config | 個人化設定（主題、輸出格式偏好）|
| /context | 視覺化呈現上下文使用狀態 |
| /model | 切換模型（Sonnet / Haiku / Opus）|

## 延伸閱讀
- [[CLAUDE-md-入門指南]]
- [[Claude-Code-Skills]]
- [[Claude-Skills-完整開發指南]]
- [[Claude-Routines]]
- [[Claude-模型方案比較]]

## 來源
- raw/Claud 入門指南.pdf
