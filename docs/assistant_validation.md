# 助手實際驗證紀錄

2026/10/04 在本機 WSL Ubuntu 執行，操作者為 AI 助手。這是本人授權的準備驗證；本人明天的執行、觀察與截圖仍須另行完成。沒有以預期值補造測量資料。

## 工具鏈與建置

GNU GCC 16.2.0 已安裝於 `/home/alan/.local/toolchains/gcc-16.2.0`，target 為 `x86_64-pc-linux-gnu`。原 `/usr/bin/g++` 仍為 15.2.0。專案程序使用本地 libstdc++／libgcc_s，glibc／libm 仍為 Ubuntu 的系統版本。實際版本與依賴見 `results/toolchain-gcc16.2/`。

Q0～Q6 全部直接建置成功；Q1 的 18 條 kernel 路徑不計時檢查與其餘入口檢查通過。建置／檢查輸出為 `build/gcc16-preparation-build.txt`、`build/gcc16-preparation-check.txt`。

## 實際批次

執行指令：`HW2_RUN_ROLE=assistant bash scripts/run_all.sh`。

原始輸出目錄：`results/linux-20261004-032643-assistant/`。`start.txt` 記錄操作者、時間、compiler 與 runtime 路徑，`completion.txt` 記錄 `failed_experiments=0`。Q1 設定為 5000000 iterations、7 repeats、2 warmups、seed 20261004，共 18 組、126 筆實際計時及 12 個 precision 案例。摘要已由原始樣本產生於 `q1-summary.csv`／`q1-summary.md`。

| 核對項目 | 本機實際觀察 | 證據 |
|---|---|---|
| Q1 | 計時均為有限正值，各組 7 筆；精度誤差与解析整數參考值一致 | q1-timing-and-precision.txt |
| Q2 | sqrt(4) 三型態均為 2；負值記錄 NaN／errno／exception；負零符號保留 | q2-default.txt、q2-libm.txt |
| Q3 | left_grouped：strict=1、fast=0；NaN self inequality：true／false | q3-strict.txt、q3-fast.txt |
| Q4 | nearest 的精確中點 1/1024 由兩種格式化輸出為 0.000976562；其他 mode 輸出不同 | q4-formatting.txt |
| Q5 A | 同一 binary：nearest 的 1+2^-53 為 0x1p+0，upward 為 0x1.0000000000001p+0 | q5-nearest.txt、q5-upward.txt、binary hash |
| Q6 | 精確 subnormal 未設 underflow／inexact；最小 subnormal×0.5 成為零並設定兩旗標 | q6-underflow.txt |

Q1 時間是含 loop／call 等成本的有效平均 ns/op，不等於單條指令硬體 latency。第一輪沒有控制實體 P/E 核心與溫度，不拿這一輪推論固定速度比例。

Q2 原本使用 `--disassemble=sqrt` 時，版本化符號造成部分輸出空白。已修正 `scripts/inspect_libm.sh`，從實際符號地址與長度採集所有相關版本與 finite implementation；第一輪補充證據為 `q2-libm-address-ranges.disasm.txt`。本機可見 SQRTSS、SQRTSD、FSQRT，wrapper 有負值分支。這證明本機使用硬體指令的路徑，不證明硬體內部微演算法。

`python3 scripts/validate_run.py results/linux-20261004-032643-assistant` 已通過完整性與解析參考檢查；`summarize_q1.py` 已成功處理實際資料。新版反組譯採集會在本人下次批次自動使用。

## 仍需本人完成

Mac 尚無工具連線，沒有在其實機編譯或執行。Mac Q0／Q5、正式截圖、本人對結果的解釋、姓名學號核對與最後 PDF 繳交仍待本人完成。Apple ABI 文件支持 long double 與 double 相同的預期，但尚無 Mac 實測，不能寫成跨平台結果。Word 的本人結果欄保留待填，AI 揭露已更新實際分工。
