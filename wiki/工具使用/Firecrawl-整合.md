# Firecrawl 整合

> Sources: 未知作者, Unknown
> Raw: [firecrawl-整合筆記](../../raw/claude-code/firecrawl-整合筆記.md)

## 定義
Firecrawl 是一個爬蟲工具，透過與 Claude Code 整合，解決因 403 Error 或 JavaScript 動態渲染導致 WebSearch 抓不到網站內容的問題。

## 重點整理

**安裝三步驟**
1. 在 Claude Code 說：「幫我安裝 Firecrawl CLI，然後設定好讓你可以用它來爬網站。」→ 按「允許」
2. 去 firecrawl 免費註冊，複製 API Key → 說：「幫我登入 Firecrawl，我的 API Key 是 [Key]」
3. 說：「幫我看一下 Firecrawl 的狀態和剩餘 Credits。」→ 確認已認證

**Credits 說明**
- 免費帳號：500 Credits，爬一頁約 1-2 Credits
- 優惠碼 NATE（firecrawl → Settings → Billing → Apply Coupon）：額外 1000 Credits
- 合計免費額度：1500 Credits
- Hobby 方案：$16 美金/月（3,000 Credits）

**四個核心爬蟲場景**

| 場景 | 適用情況 | 關鍵 Prompt |
|------|----------|-------------|
| 網頁爬取 | JS 動態渲染讓 WebSearch 拿到空白 | 「幫我用 Firecrawl 爬取 [URL] 的資料」|
| 競品分析 | 想了解競爭對手產品、定價、優劣勢 | 參考 Competitor Analysis Workflow |
| 行業研究 | 開發某行業客戶、需要先了解市場 | 明確列出公司名單 + 設定搜索次數上限 |
| SEO 審計 | 想知道網站 SEO 健康度和改善建議 | 參考 seo-audit workflow 格式 |

**行業研究 Prompt 關鍵技巧（避免 Token 爆掉）**
- 明確列出要查的公司（不要讓 AI 自己找）
- 明確列出每間公司需要什麼資料（不要寫「相關資料」）
- 設定搜索次數上限：「每間公司最多搜 10 次」
- 明確告訴何時停：「做完就停，不需要額外報告」
- 範圍越窄 = 結果越精準 = 消耗越少

**Firecrawl 做不到的事**
- 社交媒體（Facebook、Instagram、X）：需要登入，爬不到 → 改用 Apify
- 強反爬蟲網站（Cloudflare 保護）：不保證能爬到
- 核心原則：有 API 的平台用 API，沒有 API 的才用 Firecrawl

## 延伸閱讀
- [[Claude-Code-Skills]]
- [[Claude-模型方案比較]]

## 來源
- raw/Claude_Code__Firecrawl_安裝及使用筆記_(免費版).pdf
