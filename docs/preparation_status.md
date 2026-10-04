# 準備完成清單

更新：2026/10/04（Asia/Taipei）。

| 項目 | 狀態 |
|---|---|
| Q0 Windows／WSL 環境採集 | 本人已於 2026/10/04 正式執行與截圖，Windows snapshot 200712、WSL 批次 201349 |
| Mac 基本資訊 | 本人提供，完整實機採集待執行 |
| Q1～Q6 來源與獨立說明 | 已實作，包含各題六項要求 |
| GCC 15.2.0 直接建置 | 成功，沒有 compiler warning |
| GCC 15.2.0 CMake 全部建置 | 成功 |
| WSL GNU GCC 16.2.0 | 官方來源／SHA-512 核對，本地並存安裝成功 |
| GCC 16.2.0 全部建置與入口檢查 | 通過；本地 runtime 依賴已核對 |
| GCC 16.2.0 CMake 建置 | 全部 target 建置與入口檢查通過 |
| Q1 smoke check | 18 條 kernel 路徑，100 iterations，不計時 |
| Q2～Q6 入口檢查 | --help／--check 通過；沒有執行數值案例 |
| 防止最佳化／Q3 flag 差異 | 本人正式產生碼與 strict／fast 輸出已保存並整理入 Word |
| Bash scripts／Python CLI | 語法／入口檢查通過 |
| 根目錄 Word 報告 | 本人 Windows 數據、126 筆計時樣本、18 張必要截圖與 AI 揭露已填入；Word 匯出 25 頁，逐頁排版已檢查 |
| 助手 benchmark／精度／Q2～Q6 驗證 | 完整批次成功，assistant 目錄保存實際原始資料與摘要 |
| 本人正式 benchmark／精度／截圖 | 已完成；student 批次 failed_experiments=0，資料驗證通過，18 組中位數由原始樣本獨立核對一致 |
| 截圖／最後 PDF | 21 張原圖全部保存，18 張嵌入 Word；提交 PDF 待本人 Mac Q5 完成後輸出 |
| Mac 編譯與批次脚本 | 先前 assistant 實機試跑已保存；本人 Q5 尚待執行，不能以助手結果替代 |
| Q5 跨平台同 compiler 條件 | GNU GCC 16.2.0；Windows 本人證據已整理，Mac 本人結果與 pair checker 核對待補 |
| glibc 精確 source version | master 僅參考；Ubuntu 套件需與反組譯／source 進一步核對 |

直接執行步驟見 `docs/runbook.md`。建置檢查輸出在 `build/preparation-build.txt` 與 `build/cmake-all-check.txt`；它們不是提交用的正式實驗結果。
