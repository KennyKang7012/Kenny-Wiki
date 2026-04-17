# Claude Dispatch

> Sources: Wilson AI Lab, Unknown
> Raw: [claude-dispatch](../../raw/claude-code/claude-dispatch.md)

## 定義
Claude Dispatch 是 Claude Cowork 裡的功能，讓你用手機遠端控制桌機上的 Claude Agent 執行任務，手機是遙控器，桌機是執行引擎。

## 重點整理

**前置條件**
- 付費方案：Claude Pro（$20/月）或 Max（$100/月），免費版無法使用
- 安裝 Claude Desktop 和手機 Claude App，登入同一個 Anthropic 帳號
- 關閉電腦自動睡眠（Dispatch 任務在本地電腦跑，電腦睡眠任務就停）

**設定流程（約 2 分鐘）**
1. 打開 Claude Desktop → Cowork → Dispatch → Get Started
2. 授權檔案存取
3. 手機掃描 QR Code（只有第一次配對才需要）
4. 完成：手機和桌機共用同一個 Dispatch 對話

**Connectors 整合**
- Notion Connector：授權後可直接寫入 Notion 頁面
- Gmail Connector：授權後可讀取和傳送郵件
- 官方支援 38+ 個 Connectors

**三個串接示範任務**
- 任務一：讀 Excel → 生成 PDF 報告（存在桌面）
- 任務二：把報告摘要 → 新增子頁面到 Notion
- 任務三：發 Gmail 給自己，附上 Notion 連結
→ 三個任務可以串接，前一個結果作為下一個的來源

**現狀與限制**
- 目前是 Research Preview（公開測試版）
- 複雜任務成功率約 50%，簡單任務（找檔案、摘要、整理資料夾）表現穩定
- 任務失敗時：把要求寫更清楚（描述結果而非步驟）通常就能成功
- OneDrive 桌面需要給完整路徑，建議在 Global Instructions 預先設定

**vs OpenClaw**：不懂技術、想直接用 → Claude Dispatch；需要完整自主控制、進階客製化 → OpenClaw

## 延伸閱讀
- [[OpenClaw-Discord部署]]
- [[Hermes-Agent]]
- [[AI-工具選型比較]]

## 來源
- raw/Claude Dispatch 初級使用指南.pdf
