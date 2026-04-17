# Claude Dispatch 初級使用指南

> Source: raw/Claude Dispatch 初級使用指南.pdf
> Collected: 2026-04-17
> Published: Unknown

Dispatch 是 Claude Cowork 裡的功能，讓你用手機遠端控制桌機上的 Claude Agent。手機 = 遙控器 → 桌機 = 執行引擎。

注意：Dispatch 目前是 Research Preview（公開測試版）。複雜任務成功率約 50%，簡單任務（找檔案、摘要、整理資料夾）表現穩定。

## 必要條件

1. 付費方案：Claude Pro（$20/月）或 Max（$100/月），免費版無法使用
2. Claude Desktop：claude.com/download 下載最新版
3. Claude 手機 App：App Store 或 Google Play，與桌面版登入同一個 Anthropic 帳號
4. 關閉電腦自動睡眠

OneDrive 用戶注意：如果桌面透過 OneDrive 同步，下指令時需給完整路徑。建議在 Cowork → Customize → Global Instructions 輸入你的路徑，之後說「桌面」就能自動對應。

## 設定步驟（2 分鐘完成）

1. 開啟 Cowork → 左側欄找到 Dispatch → 點 Get Started
2. 授權檔案存取：開啟「Give Claude access to your files」，選擇資料夾
3. 手機掃描 QR Code（只在第一次配對時出現，之後走帳號同步）
4. 完成：手機和桌機共用同一個 Dispatch 對話

## Connectors 設定

**Notion Connector**：在 Connectors 找到 Notion → 點連接 → 用 Notion 帳號授權 → 新建工作紀錄頁面

**Gmail Connector**：在 Connectors 找到 Gmail → 點連接 → 授權讀取和傳送郵件權限

## 三個串接示範任務

**任務一：讀取 Excel → 生成 PDF 報告**
```
請開啟 C:\Users\[名稱]\OneDrive\桌面\客戶名單.xlsx，
整理成一份客戶摘要 PDF 報告，包含：
- 總覽數字（總客戶數、各狀態數量、總月營業額）
- 產業分佈、前三大客戶、完整客戶清單
```

**任務二：摘要存進 Notion**
```
把剛才整理的客戶名單摘要，新增子頁面到 Notion「工作紀錄」頁面，
頁面標題用「客戶名單摘要」加今天日期
```

**任務三：發 Gmail 通知自己**
```
發一封 Gmail 給我自己，主旨「客戶名單摘要已更新」，
附上 Notion 頁面連結
```

三個任務串接：任務一結果 → 任務二來源，任務二連結 → 任務三信件。

## Claude Dispatch vs OpenClaw 比較

| 比較項目 | Claude Dispatch | OpenClaw |
|---------|-----------------|----------|
| 設定難度 | 2 分鐘 QR Code | Node.js + VPS 自架 |
| 目標用戶 | 非技術用戶 GUI | 開發者、進階用戶 |
| 資安設計 | 本地 sandbox VM | 自行管理伺服器 |
| 整合工具 | 38+ 官方 Connectors | API 自行串接 |
| 穩定性 | Research Preview ~50% | 取決部署品質 |
| 費用 | Pro $20/月起 | 免費開源 + 伺服器費 |

結論：不懂技術、想直接用 → Claude Dispatch。需要完整自主控制 → OpenClaw。

## 常見問題

- **Q：電腦一定要開著嗎？** A：是的，Dispatch 不是雲端服務，電腦睡眠任務就停
- **Q：Pro 方案夠用嗎？** A：入門夠用，Cowork 比一般聊天耗費更多額度
- **Q：任務失敗怎麼辦？** A：重新下指令，把要求寫更清楚（描述結果而非步驟）通常就能成功
