# Floating Point 行為專案 — Advanced C++ Homework 2

截止：2026/10/07 23:59（Asia/Taipei），於 eeclass 繳交 `學號_姓名.pdf`。
PDF 第一頁必須包含 **Advanced C++ Homework 2**、學號與姓名。

## 目前狀態

Q0 已完成本機環境採集，實測摘要見 [Q0 環境紀錄](docs/q0_environment.md)。Q1 的程式與實驗流程已準備完成，見 [Q1 執行說明](experiments/q1_benchmark/README.md)，尚未執行正式 benchmark。Q2～Q6 C++ 檔案仍是占位程式，會印出 `NOT IMPLEMENTED` 並以狀態碼 2 結束；不能把占位輸出當作實驗證據。以下「預期觀察」都是待驗證的假設。

主要環境由使用者提供：Windows 11 + WSL2 Ubuntu、Intel Core i7-14650HX、GCC/G++。Apple M4 MacBook Air 為選用比較環境。實際 OS、編譯器版本、CPU 設定與型態特性仍須量測記錄。

## 目錄

```text
experiments/q0_environment/main.cpp
experiments/q1_benchmark/main.cpp
experiments/q2_cmath/main.cpp
experiments/q3_fast_math/main.cpp
experiments/q4_formatting/main.cpp
experiments/q5_portability/main.cpp
experiments/q6_extra/main.cpp
docs/experiment_protocol.md     實驗及 benchmark 原則
docs/report_outline.md         Q0～Q7 報告填寫架構
results/                       原始輸出與數據（目前為空）
screenshots/                   本人執行截圖（目前為空）
references/                    資料來源與版本紀錄
CMakeLists.txt                 各題獨立 executable
```

Q6 包含額外細節實驗；Q7 是自我揭露，不需要 C++ executable。

## 編譯與執行

主要實驗請在 **WSL Ubuntu 終端**執行，不要混用 Windows 上的 MinGW/Clang 與 WSL GCC。以下建置只會產生占位 executable。

```bash
cd /mnt/c/Users/ALAN/Desktop/floating-point-hw2
mkdir -p build results screenshots
g++ --version
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_COMPILER=g++
cmake --build build -j
./build/q0_environment
```

也可單獨编譯，無需 CMake。各題指令見下表；正式實驗實作後再保存輸出。占位程式狀態碼 2 是刻意設計。

| 題目／實驗目的與程式 | 獨立編譯指令（WSL Bash） | 執行方式 | 預期觀察（待驗證） | 需截圖的證據 |
|---|---|---|---|---|
| Q0：記錄環境與型態特性；`experiments/q0_environment/main.cpp` | `g++ -std=c++20 -O2 experiments/q0_environment/main.cpp -o build/q0_environment` | `./build/q0_environment`，另執行下方環境指令 | 型態大小、有效位數、指數範圍與 ABI 是否相符 | OS、CPU、編譯器版本、完整旗標、型態輸出 |
| Q1：比較 float/double/long double 的算術速度與誤差；`main.cpp` 與 `kernels.cpp` | `bash experiments/q1_benchmark/build.sh` | `./build/q1-scalar/q1_benchmark --iterations 5000000 --repeats 7 --warmup 2 --seed 20261004` | 相依鏈與獨立鏈成本是否不同；不能先假定 float 必然更快；初版不測記憶體成本 | 參數、每次原始時間、統計值、checksum、精度案例、assembly 與旗標 |
| Q2：追蹤 `std::sin` 的規格、實作與輸入縮減；`experiments/q2_cmath/main.cpp` | `g++ -std=c++20 -O2 -fno-fast-math -fno-builtin-sin -fno-builtin-sinf -fno-builtin-sinl experiments/q2_cmath/main.cpp -o build/q2_cmath` | `./build/q2_cmath`；搭配 `ldd build/q2_cmath`、`objdump -d -C build/q2_cmath` | 一般與大輸入的縮減路徑可能不同；由实际連結與反組譯驗證 | 輸入／輸出、動態函式庫版本、呼叫位置與來源版本 |
| Q3：僅切換 fast-math 比較結果；`experiments/q3_fast_math/main.cpp` | 見下方雙版本指令 | 分別執行 `./build/q3_strict`、`./build/q3_fast` | 候選：NaN 判定被簡化或加法重結合造成差異；須先實驗確認 | 相同輸入、兩個編譯指令、不同輸出及相關反組譯 |
| Q4：驗證小數 9 位輸出是否等於日常「四捨五入」；`experiments/q4_formatting/main.cpp` | `g++ -std=c++20 -O2 -fno-fast-math experiments/q4_formatting/main.cpp -o build/q4_formatting` | `./build/q4_formatting` | 區分儲存的二進位值、十進位文字及 tie 規則；候選精確中點 `1.0/1024.0` | `hexfloat`、高精度輸出、printf 與 iostream 的 9 位結果、rounding mode |
| Q5：找合法且滿足同編譯器版本／同旗標的環境差異；`experiments/q5_portability/main.cpp` | `g++ -std=c++20 -O2 -fno-fast-math -ffp-contract=off experiments/q5_portability/main.cpp -o build/q5_portability` | 在兩個已記錄環境執行 `./build/q5_portability` | 候選是 ABI 下 long double 有效位數差異；先驗證兩邊確實不同 | 兩邊來源雜湊、編譯器版本、逐字相同旗標、numeric_limits 與輸出 |
| Q6：補充非結合性與求和順序；`experiments/q6_extra/main.cpp` | `g++ -std=c++20 -O2 -fno-fast-math -ffp-contract=off experiments/q6_extra/main.cpp -o build/q6_extra` | `./build/q6_extra` | 正向、反向、補償求和可能有不同誤差；使用可驗證的參考值 | 相同資料的三種求和結果、誤差與資料產生方法 |
| Q7：記錄本人與 AI 分工 | 不適用 | 編輯 `docs/report_outline.md` | 分工敘述應與實際工作一致 | 不要求程式截圖；保留必要的 AI 協助紀錄 |

Q3 的成對指令（只有 fast-math 狀態不同）：

```bash
g++ -std=c++20 -O3 -fno-fast-math experiments/q3_fast_math/main.cpp -o build/q3_strict
g++ -std=c++20 -O3 -ffast-math experiments/q3_fast_math/main.cpp -o build/q3_fast
```

Q0 環境紀錄，在 WSL 執行：

```bash
uname -a
cat /etc/os-release
lscpu
g++ --version
g++ -dumpmachine
ldd --version
```

另在 Windows PowerShell 執行 `wsl --version`、`wsl -l -v`，記錄 Windows 版本與電源模式。M4 上記錄 `sw_vers`、`uname -m`、`sysctl -n machdep.cpu.brand_string` 與實際編譯器版本；`g++` 名稱不代表一定是 GCC。不同 GCC/Clang 版本的比較可用於 Q1，但不能直接當作满足 Q5 條件的證據。

實驗完成後，建議每個執行環境使用獨立目錄，例如 `results/wsl-gcc-版本/`、`screenshots/wsl-gcc-版本/`。保存 stdout、stderr、退出狀態與命令；截圖需能對應原始文字紀錄。不要覆寫失敗或異常的執行紀錄。

## 實作順序

先完成 Q0 環境採集，再實作並親自執行 Q1～Q4；確認 Q5 的比較條件可成立後才安排跨平台實驗。最後根據實際證據撰寫 Q6、Q7。`__float128`／libquadmath 是選用擴充，確認支援後再加入，不作為預設建置依賴。各題完成時都需補上程式參數與實際重現指令。
