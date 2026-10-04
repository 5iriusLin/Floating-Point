# Floating Point 行為專案

Advanced C++ Homework 2。截止：2026/10/07 23:59（Asia/Taipei），於 eeclass 提交 `學號_姓名.pdf`。第一頁須含 **Advanced C++ Homework 2**、學號與姓名。

## 目前狀態

**Windows／WSL 與 Mac Q5 實驗已完成，結果已整理入原 Word。** 報告精簡為 12 頁、14 張關鍵截圖，各題著重本機的觀察、執行證據與原因；AI 使用說明集中於 Q7。完整 126 筆計時樣本及 Windows 21 張、Mac 4 張原始截圖仍保留於專案。[結果與重現紀錄](docs/student_windows_results.md)。

主要平台：Windows 11 + WSL2 Ubuntu、Intel Core i7-14650HX；比較平台：MacBook Air 2025、Apple M4、24 GB。兩平台正式執行改用 GNU GCC 16.2.0（WSL 本地建置／Mac Homebrew）；Mac 完整版本、硬體與 runtime 已由本人採集。原有 GCC 15.2.0 與 Apple Clang 21.0.0 保留。詳見 [Q0 歷史紀錄](docs/q0_environment.md) 與 [工具鏈說明](docs/gcc16_toolchain.md)。Q5 已核對本人兩端來源、版本、flags 與實際輸出，WSL／Mac long double 增量分別為 1／0。

## 最後一次手動跑

Windows PowerShell，在專案根目錄：

```powershell
./experiments/q0_environment/collect_windows.ps1
```

WSL Ubuntu：

```bash
cd /mnt/c/Users/ALAN/Desktop/floating-point-hw2
bash scripts/run_all.sh
```

此命令重新編譯並跑所有正式案例，各次使用新的 `results/linux-日期時間/`，保存 stdout／stderr、exit code、命令、compiler、flags、source SHA-256、assembly 與函式庫資訊。預設記錄 `executed_by=student`；助手驗證使用 `HW2_RUN_ROLE=assistant` 並加目錄後綴，兩者分開保存。 詳細操作、截圖與 Mac 流程見 [執行手冊](docs/runbook.md)。

Mac 專案根目錄可執行 `CXX=g++-16 bash scripts/run_all.sh`；實體 Mac 尚未驗證。Python 不是執行 C++ 實驗的必要依賴；`python3 scripts/summarize_q1.py results/實際目錄` 只用於跑完後產生實際數據摘要。

## 各題程式與說明

| 題目 | 程式與方法 | 目的 |
|---|---|---|
| Q0 | [環境程式](experiments/q0_environment/main.cpp)、[已採集紀錄](docs/q0_environment.md) | 硬體、OS、compiler、ABI、型態資訊 |
| Q1 | [獨立重現說明](experiments/q1_benchmark/README.md)、main.cpp／kernels.cpp | 三型態、加減／乘／除、相依與獨立鏈、精度 |
| Q2 | [獨立重現說明](experiments/q2_cmath/README.md)、main.cpp／sqrt_paths.cpp | std::sqrt overload、builtin、libm、hardware |
| Q3 | [獨立重現說明](experiments/q3_fast_math/README.md)、main.cpp／operations.cpp | fast-math 的重結合與有限值假設 |
| Q4 | [獨立重現說明](experiments/q4_formatting/README.md)、main.cpp | printf／iostream 九位小數、中點／mode |
| Q5 | [獨立重現說明](experiments/q5_portability/README.md)、main.cpp／operations.cpp | 同 binary 捨入環境与同版本 compiler ABI 候選 |
| Q6 | [獨立重現說明](experiments/q6_extra/README.md)、main.cpp／operations.cpp | gradual underflow、subnormal、exception |
| Q7 | [報告大綱](docs/report_outline.md) | 本人／AI 分工與實際驗證 |

各題 README 均列出目的、程式、編譯指令、執行方式、待驗證觀察與截圖要求。Q7 不需要 executable。__float128 為選用型態，本版本未加入其 benchmark。

## 只準備，不正式執行

```bash
bash scripts/build_all.sh
bash scripts/check_build.sh
```

或使用 CMake：

```bash
source scripts/compiler_env.sh
cmake -S . -B build/cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_COMPILER="$CXX"
cmake --build build/cmake -j2
```

GCC／Clang 是目前支援的 compiler。Q1 需兩個 translation units，不能只編 main.cpp；所有正式旗標以 build.txt 為準。不要把 Windows llvm-mingw 的 g++.exe 混作 WSL GCC。

## 資料與報告

- [根目錄 Word 報告](Floating_Point_Report_Q0.docx)：後續直接在同一份修改。
- [實驗規範](docs/experiment_protocol.md)：benchmark、防止最佳化與保存證據原則。
- [來源筆記](docs/reference_notes.md)、[來源索引](references/sources.md)：版本与已查證範圍。
- `results/` 保存真正原始輸出，`screenshots/` 保存真正執行／結果檔案畫面。

來源與理論不取代本機觀察。AI 不補造數值、圖表或執行截圖；實際跑完前不要把準備稿當作完成報告。
