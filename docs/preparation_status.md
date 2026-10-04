# 準備完成清單

更新：2026/10/04（Asia/Taipei）。

| 項目 | 狀態 |
|---|---|
| Q0 Windows／WSL 環境採集 | 先前由助手實際執行；本人仍需正式重跑與截圖 |
| Mac 基本資訊 | 本人提供，完整實機採集待執行 |
| Q1～Q6 來源與獨立說明 | 已實作，包含各題六項要求 |
| GCC 15.2.0 直接建置 | 成功，沒有 compiler warning |
| GCC 15.2.0 CMake 全部建置 | 成功 |
| WSL GNU GCC 16.2.0 | 官方來源／SHA-512 核對，本地並存安裝成功 |
| GCC 16.2.0 全部建置與入口檢查 | 通過；本地 runtime 依賴已核對 |
| GCC 16.2.0 CMake 建置 | 全部 target 建置與入口檢查通過 |
| Q1 smoke check | 18 條 kernel 路徑，100 iterations，不計時 |
| Q2～Q6 入口檢查 | --help／--check 通過；沒有執行數值案例 |
| 防止最佳化／Q3 flag 差異 | 已檢查產生碼；正式输出待採集 |
| Bash scripts／Python CLI | 語法／入口檢查通過 |
| 根目錄 Word 報告 | 直接更新方法、新版工具鏈、Q6 主題、AI 揭露；11 頁排版已檢查 |
| 助手 benchmark／精度／Q2～Q6 驗證 | 完整批次成功，assistant 目錄保存實際原始資料與摘要 |
| 本人正式 benchmark／精度／截圖 | 待明天親自執行；Word 本人結果欄仍待填 |
| 截圖／最後 PDF | 待本人執行後整理 |
| Mac 編譯與批次脚本 | 未在實體 Mac 驗證 |
| Q5 跨平台同 compiler 條件 | 選用 GNU GCC 16.2.0；Mac 完整版本與實測仍待取得 |
| glibc 精確 source version | master 僅參考；Ubuntu 套件需與反組譯／source 進一步核對 |

直接執行步驟見 `docs/runbook.md`。建置檢查輸出在 `build/preparation-build.txt` 與 `build/cmake-all-check.txt`；它們不是提交用的正式實驗結果。
