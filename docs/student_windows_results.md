# 本人 Windows 實驗已整理

本人 Windows snapshot：`results/q0-windows/20261004-200712/`。
本人 WSL 結果：`results/linux-20261004-201349/`。
操作者標記為 student，完整批次的 failed_experiments=0。

原始數據已通過 validate_run.py；18 組中位數獨立重新由 126 筆原始樣本核對，與 q1-summary.csv 一致。Word 已放入 18 張必要截圖、18 組 timing 摘要、全部 7 回合 ns/op、12 個 accuracy 案例、Q2 的 30 組合併案例（default／libm 共 60 呼叫）、Q3 對照、Q4 的 16 組 mode／case、Q5 本人 Windows 證據及 Q6 全部 9 案例。

圖與原始檔的 SHA-256／對照索引見 `docs/student_report_evidence.json`。21 張原始 screenshot 全部保留；三張重複畫面未再貼入正文。名稱含 2025 的 precision 圖，其命令指向本次 student 結果，已與原始 log 核對，報告有說明，不以檔名推定日期。

主要 Word 仍是根目錄 `Floating_Point_Report_Q0.docx`，直接修改原檔。Mac 先前 assistant 結果沒有替代本人的待完成結果。原因分析由 AI 協助整理，本人仍需檢查理解。

Word 已透過 Microsoft Word 匯出供內部檢查的 25 頁預覽，逐頁檢查表格、截圖、圖說及頁尾。DOCX 的 18 個嵌入圖片與原始截圖 SHA-256 全部一致；裁切使用 Word 的圖片裁切設定。內部預覽不作為提交 PDF，也不放入 Git。

## Mac Q5 下一步

先 pull 本次更新，再於 Mac 專案根目錄執行：

```bash
CXX=g++-16 bash scripts/run_q5.sh run
```

指令會建立 `results/q5-darwin-日期時間-student-隨機碼/`。使用最後印出的實際資料夾名稱，比較本人兩端條件：

```bash
python3 scripts/verify_q5_pair.py results/linux-20261004-201349 results/q5-darwin-你的實際資料夾
```

保留 q5-nearest.txt、compiler-full-version.txt、q5-flags.txt、source-sha256.txt、pair checker 輸出及你的 Mac 截圖。四項 MATCH 只是必要條件；還需看 long double digits、實際 nearest 結果與產生碼。完成後再將本人 Mac 結果補進 Q5，更新 Q0 輔助平台與 Q7 揭露，最後輸出提交 PDF。

換行修正 `.gitattributes` 已包含 Bash／C++ 來源，避免 Windows checkout 造成 WSL 腳本 CRLF 錯誤或跨平台來源雜湊不同。
