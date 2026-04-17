# Claude Code + Firecrawl 安裝及使用筆記（免費版）

> Source: raw/Claude_Code__Firecrawl_安裝及使用筆記_(免費版).pdf
> Collected: 2026-04-17
> Published: Unknown

Firecrawl 是一個爬蟲工具，解決 Claude Code 的 WebSearch 因 403 Error 或 JS 動態渲染抓不到網站內容的問題。

## 安裝流程

**Step 1：安裝 Firecrawl CLI**
在 Claude Code 裡說：「幫我安裝 Firecrawl CLI，然後設定好讓你可以用它來爬網站。」Claude Code 會自動跑安裝指令，你只需要按「允許」。

**Step 2：拿 API Key**
去 firecrawl 免費註冊帳號，在首頁右邊複製 API Key。在 Claude Code 裡說：「幫我登入 Firecrawl，我的 API Key 是 [Key]」

**Step 3：確認安裝成功**
說：「幫我看一下 Firecrawl 的狀態和剩餘 Credits。」顯示已認證 + Credits 數量就代表成功。

## Credits 說明

- 免費帳號：500 Credits
- 爬取一個頁面：約 1-2 Credits
- 優惠碼 NATE：額外 1000 Credits（firecrawl → Settings → Billing → Apply Coupon）
- 合計可免費使用：1500 Credits

## 四個最實用的爬蟲場景

### 場景一：網頁爬取
適用：想抓某個網站的資料，但 Claude Code 的 WebSearch 抓不到（JS 動態渲染問題）。

Prompt：「幫我用 Firecrawl 爬取 [URL] 的資料，把相關的數據整理好列出來。」

### 場景二：競品分析報告
適用：想了解競爭對手的產品、定價、優劣勢。Firecrawl 有內建的 Competitor Analysis Workflow。

做法 A（參考 Firecrawl Workflow 模板）：報告結構完整，維度齊全（7 個分析角度），但個別維度分析深度可能不夠。
做法 B（讓 Claude Code 自己發揮）：背景調查更仔細，但分析維度可能不如模板全面。
建議：兩份都跑一次，取各自長處合併成最終版本。

### 場景三：行業研究 / Lead Research
適用：想開發某個行業的客戶，需要先了解市場。

重要 Prompt 技巧（避免 Token 爆掉）：
1. 明確列出要查的公司（不要讓 AI 自己找）
2. 明確列出每間公司需要什麼資料
3. 設定搜索次數上限（「每間公司最多搜 10 次」）
4. 明確告訴它什麼時候停（「做完就停，不需要額外報告」）

範圍越窄 = 結果越精準 = 消耗越少。

### 場景四：SEO 審計
適用：想知道網站 SEO 健康度，有什麼可以改善。

Prompt：「用 Firecrawl 幫我做一次 SEO 審計，目標是 [URL]。參考 firecrawl claude seo-audit workflow 的固定報告格式。」

SEO 審計會生成兩份報告：完整審計報告（問題清單 + 得分）+ 行動計劃（按優先級排好的修改建議）。之後可讓 Claude Code 直接根據行動計劃修改網站，從審計到修改一條龍完成。

## Firecrawl 做不到的事

1. **社交媒體**：Facebook、Instagram、X 等需要登入的平台爬不到，推薦用 Apify
2. **有些強反爬蟲網站**：有 Cloudflare 保護的不一定能爬到
3. **費用**：免費 500 Credits 用完就沒了，Hobby 方案 $16 美金/月（3,000 Credits）

核心原則：有 API 的平台用 API，沒有 API 的才用 Firecrawl。工具是死的，場景是活的。
