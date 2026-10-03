# Q1 不同浮點型態的效能與精度

## 目的與目前狀態

比較 float、double、long double 的基本算術時間與有限精度影響。程式已在 WSL GCC 15.2.0 成功編譯，18 條 kernel 路徑通過不計時 smoke check。**尚未執行正式 benchmark 或精度實驗；沒有結果可填入報告。**

`main.cpp` 負責執行期參數、計時、統計與精度案例；`kernels.cpp` 是獨立編譯的待測迴圈；`kernels.hpp` 定義介面。初版只測 scalar，不測 SIMD 或大型陣列的記憶體成本。`__float128` 暫不納入。

## 測量設計

| 運算 | 每條鏈每迭代的運算 | 用途 |
|---|---|---|
| add_sub | `x += step; x -= step;` | 比較加／減混合的基本成本 |
| multiply | `x *= factor; x *= inverse;` | 比較乘法成本 |
| divide | `x /= factor; x /= inverse;` | 比較除法成本 |

`step=1/1024`、`factor=1+1/1024`，起始值為 `1+(seed%1024)/1024`。這些輸入在三種型態都可精確表示；`inverse=1/factor` 各自以待測型態計算，可能具有不同捨入。seed 是決定起始值的參數，不是亂數產生器 seed。

每個運算測兩個模式：`latency1` 使用一條相依鏈，每迭代 2 個運算；`throughput4` 使用四條獨立鏈，每迭代 8 個運算。四條鏈不保證已達 CPU 峰值吞吐量，結果只能代表這個 kernel。加減配對刻意維持穩定值域；即使 checksum 不變，CPU 仍須執行迴圈內運算，需由反組譯佐證。乘除配對使用近似倒數，可能緩慢漂移。

計時使用 steady_clock；計時區域只有型態分派、少量參數準備（包含一次倒數計算）、kernel 呼叫與結果轉換。I/O、樣本儲存、排序在計時外。時間包含呼叫、迴圈控制及一次收尾 checksum 的成本，`ns_per_operation` 是有效平均成本，不能直接視為單條指令的硬體 latency。

每組預設 2 次暖機（每次最多 100000 iterations），7 次正式測量（每次 5000000 iterations）。每回合輪換型態順序，列出所有原始時間、checksum、中位數、最小／最大值。不同型態的運算數一致，但 throughput4 的總運算數是 latency1 的四倍，請用每運算時間比較。

## 避免計算被刪除

- kernels 在另一個 translation unit，關閉 LTO，並標示 noinline。
- GCC／Clang optimization barrier 僅在迴圈前後，不加入每迭代 volatile 記憶體存取。
- 每個 sample 的 checksum 會輸出；結果若非有限值或非正值，執行失敗。
- 關閉 fast-math、FMA contraction 與自動向量化。
- 編譯後查閱 `kernels.s` 或 `kernels.disasm.txt`，確認迴圈內有算術指令及返回迴圈的分支。不得只憑程式碼或 checksum 就認定 benchmark 有效。

這些 barrier 與屬性為 GCC／Clang 擴充，初版不支援 MSVC。

## 編譯

在 WSL Ubuntu，專案根目錄執行：

```bash
mkdir -p results/q1-wsl
bash experiments/q1_benchmark/build.sh 2>&1 | tee results/q1-wsl/build.txt
objdump -d -C build/q1-scalar/kernels.o > results/q1-wsl/kernels.disasm.txt
```

核心旗標：`-std=c++20 -O3 -Wall -Wextra -fno-fast-math -ffp-contract=off -fno-lto -fno-tree-vectorize`。來源分別編譯成 object，再連結；`build.sh` 同時輸出 assembly。未指定 `-march=native`，使用 GCC 預設 target。CMake 的 q1_benchmark target 也已接上兩份來源及相同的最佳化控制。

Mac 若用現有 Apple Clang：`CXX=clang++ bash experiments/q1_benchmark/build.sh build/q1-mac-scalar`。script 會用 Clang 的 `-fno-vectorize -fno-slp-vectorize`，所以跨平台比較旗標會有 compiler-specific 差異；這個 Q1 比較不是 Q5。

## 本人執行

先檢查程式可用，不採集時間：

```bash
./build/q1-scalar/q1_benchmark --check
```

正式計時（下列命令尚未由助手執行）：

```bash
set -o pipefail
./build/q1-scalar/q1_benchmark --iterations 5000000 --repeats 7 --warmup 2 --seed 20261004 2>&1 | tee results/q1-wsl/run-01.txt
echo "exit=${PIPESTATUS[0]}"
```

若 sample 太短或波動很大，可將 iterations 提高至 20000000 後完整重跑，保存新檔案及旗標。不要挑選較快的樣本替換原始紀錄。正式測量前重新採集 Q0、關閉明顯背景工作，記錄電源模式與插電狀態；此處不會更動系統設定。

單独跑精度，不計時：

```bash
./build/q1-scalar/q1_benchmark --precision-only 2>&1 | tee results/q1-wsl/precision-01.txt
```

精度案例分別使用 10000 組 `[2^24, 1, -2^24]`、`[2^53, 1, -2^53]`，依序與反序加總。輸入皆可精確表示，實數精確答案為整數 10000，且在三種型態可精確表示。因此誤差參考不是任意假定 long double 為真值。觀察中間加法的捨入與順序影響；最終答案與相對誤差仍須本人執行取得。

## 預期觀察與分析問題

以下為待驗證問題，不是結果：三種型態是否產生不同算術指令？long double 是否比 float／double 慢？單鏈與四鏈的每運算時間是否不同？CPU 分派、背景負載是否讓樣本波動？不同有效位數是否改變精度案例的結果？不要事先寫「float 一定最快」。

目前只有準備階段的組合語言檢查：WSL 編譯的 float／double kernel 含 scalar SSE 算術，long double kernel 含 x87 算術；必須進一步截取相關 loop 說明，速度原因仍待正式數據判斷。

## 截圖與報告

1. 完整編譯旗標、GCC 版本與執行參數。
2. 三種型態同一運算／模式的原始 sample 與 summary（必要時多張），包含 checksum。
3. 兩個精度案例的三種型態輸出，包含精確答案、絕對及相對誤差。
4. 三種型態對應的代表性 assembly loop，包含算術指令與 loop branch。

Word 的 Q1 方法已可填入，結果表與截圖位置須保留待填，等本人回傳原始紀錄後再整理分析。
