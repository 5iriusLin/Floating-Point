# Windows 與 WSL 本次執行紀錄

2026/10/04，Asia/Taipei。本人要求開始執行 Windows 項目，由助手操作本機執行；所有目錄保留實際原始输出，操作者標為 assistant。

## 本次資料

| 項目 | 目錄／檔案 | 狀態 |
|---|---|---|
| Windows 環境 | results/q0-windows/20261004-195423/ | 硬體、電源、Windows／WSL 版本已採集 |
| WSL Q0～Q6 完整批次 | results/linux-20261004-195428-assistant/ | 全部成功，failed_experiments=0 |
| Q1 摘要 | 上述目錄的 q1-summary.md／q1-summary.csv | 126 筆實際計時、12 個 precision 案例已整理 |
| 同步 Mac 更新後的 Q5 專用重跑 | results/q5-linux-20261004-195639-assistant-tEK4jC/ | 四種捨入模式全部成功 |
| Mac Q5 已同步紀錄 | results/q5-darwin-20261004-143814-assistant-cR4taw/ | 從 Mac commit 7031670 取得，非 Windows 上執行 Mac binary |

WSL 使用本地 GNU GCC 16.2.0；Windows 為平衡電源，採集時插電、電池 100%。沒有控制實體 P/E 核心、即時頻率或溫度，時間不可直接解釋成單條指令 latency。Q1 使用 5000000 iterations、7 repeats、2 warmups、seed 20261004。完整批次已通過 `validate_run.py`，摘要由 `summarize_q1.py` 讀取真實樣本產生。

## Mac 更新核對與修正

Mac commit 未改 C++ 實驗來源或既有完整批次旗標，新增 Q5 專用腳本、說明及 Mac 實測資料。因此本次完整批次仍可使用，另外實際執行新版 Q5 腳本。

第一次執行 `run_q5.sh` 因 Windows Git checkout 將換行轉為 CRLF，在 `set -euo pipefail` 處退出，尚未執行數值實驗。原失敗 log 保存在 `build/windows-q5-current-run.txt`。已將該腳本轉回 LF，加入 `.gitattributes` 固定 Bash／C++ 來源換行；成功重跑 log 為 `build/windows-q5-current-run-fixed.txt`。未改 C++ 計算或編譯旗標。

## Q5 跨平台實測

`verify_q5_pair.py` 核對新版 Windows／WSL Q5 與 Mac 紀錄：compiler family、確切 release、flags、Q5／common source hashes 四項均為 MATCH；結果保存於 WSL Q5 目錄的 `pair-check.txt`。

| nearest 下的 ABI 案例 | Windows／WSL | Mac |
|---|---:|---:|
| GNU GCC release | 16.2.0 | 16.2.0 |
| long double bytes | 16 | 8 |
| long double digits | 64 | 53 |
| `(2^53+1)-2^53` | 1 | 0 |

兩邊的 nearest 紀錄與產生碼支持不同 long double 精度導致此案例差異。相同 release 不代表 compiler binary、build configuration 或 vendor patch 完全相同，這些資訊已保留。候選 A 的 directed rounding 是另一個受控執行環境實驗，不混作候選 B 的硬體／ABI 對照。

## 截圖入口

完整清單見 docs/runbook.md。Q1 可先開本次 q1-summary.md，再顯示原始 q1-timing-and-precision.txt 的命令／設定與對應樣本；Q3 顯示 strict／fast 原始输出；Q4 顯示精確中點與捨入 mode；Q5 顯示两邊的 q5-nearest.txt、compiler／flags 與 pair-check.txt；Q6 顯示 underflow／inexact 案例。

若截圖呈現保存的輸出，保留檔名、原執行時間與操作者資訊。本人要親自重跑時，在 WSL 專案根目錄執行 `bash scripts/run_all.sh`；Q5 專用流程為 `bash scripts/run_q5.sh run`，都會另建目錄，不覆寫本次資料。
