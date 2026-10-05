# 本人 Windows 實驗已整理

本人 Windows snapshot：`results/q0-windows/20261004-200712/`。
本人 WSL 結果：`results/linux-20261004-201349/`。
操作者標記為 student，完整批次的 failed_experiments=0。

原始數據已通過 validate_run.py；18 組中位數由 126 筆原始樣本獨立核對，與 q1-summary.csv 一致。

## 目前 Word 版本

根目錄 `Floating_Point_Report_Q0.docx` 最終潤飾版為 7 頁、3 張關鍵截圖，保留原題標題並以連續技術敘述呈現。正文移除來源／編譯／執行指令、結果目錄、核對腳本及不必要的程式片段；精確重現資訊仍在專案。Q0 縮成第一頁內的必要平台與型態資料。Q1 的 18 組速度及 12 個精度結果完整保留，重複 benchmark 圖移出；Q2 保留規格、硬體／libm 路徑、短指令摘錄與通用軟體算法參考。Q3 保留差異輸出圖；Q4 保留中點反例與模式表，重複截圖移出。Q5 保留兩平台完整比較及兩張原圖；Q6 結論串連全份報告，再補充 gradual underflow 與原數值表。Q7 簡短揭露分工。正文 12 pt、表格 11 pt，頁邊界不變。

完整計時樣本、全部案例與原始截圖仍保留於 results、screenshot、mac截圖，並未因報告精簡而刪除。圖與原始檔的 SHA-256／對照索引見 `docs/student_report_evidence.json`；included_in_condensed_report 與 condensed_figure_label 標示目前正文使用的圖片。

Word 已透過 Microsoft Word 匯出供內部檢查的 7 頁預覽，逐頁檢查表格、截圖、圖說及頁尾。3 張嵌入圖片的原始媒體雜湊均與截圖一致；裁切與縮放使用 Word 原生設定。內部預覽不作為提交 PDF，也不放入 Git。

## Mac Q5 已完成

結果目錄：`results/q5-darwin-20261004-211048-student-wdBjAR/`。開始時間 21:10:48，failed_experiments=0。四項 pair checker 皆 MATCH；nearest long double 於 WSL 為 16 bytes／64 digits、增量 1，Mac 為 8 bytes／53 digits、增量 0。兩張 Mac 結果截圖已嵌入目前 Word。

## Mac Q5 重現方式

先 pull 本次更新，再於 Mac 專案根目錄執行：

```bash
CXX=g++-16 bash scripts/run_q5.sh run
```

指令會建立 `results/q5-darwin-日期時間-student-隨機碼/`。使用最後印出的實際資料夾名稱，比較本人兩端條件：

```bash
python3 scripts/verify_q5_pair.py results/linux-20261004-201349 results/q5-darwin-你的實際資料夾
```

保留 q5-nearest.txt、compiler-full-version.txt、q5-flags.txt、source-sha256.txt、pair checker 輸出及你的 Mac 截圖。四項 MATCH 只是必要條件；還需看 long double digits、實際 nearest 結果與產生碼。本人 Mac 結果已補入 Q5、Q0 輔助平台與 Q7 揭露；提交 PDF 尚需本人確認分析後輸出。

換行修正 `.gitattributes` 已包含 Bash／C++ 來源，避免 Windows checkout 造成 WSL 腳本 CRLF 錯誤或跨平台來源雜湊不同。

目前無必要補跑實驗；交稿前需確認 Q7 分工與對各題解釋的理解。Q5 比較相同 GNU GCC release 16.2.0，但不是相同編譯器建置。Q2 本機 libm 指令已驗證，通用源碼版本未精確匹配，故只作算法參考。
