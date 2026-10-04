# Q5 執行環境差異的兩個候選

1. **目的**：準備相同來源、同 compiler 版本、同 flags、無一般 C++ UB 的環境差異實驗。Q5 加分結論仍需本人結果與條件核對。
2. **程式**：`main.cpp`、`operations.cpp`。候選 A：同一 binary、同數值输入，僅 HW2_ROUNDING 選擇不同浮點執行環境，計算 `1+2^-53`。候選 B：nearest 下計算 long double 的 `(2^53+1)-2^53`，比較平台 ABI／有效位數。
3. **編譯**（兩平台必須逐字相同的 flags）：

```bash
source scripts/compiler_env.sh
mkdir -p build
"$CXX" -std=c++20 -Wall -Wextra -fno-lto -ffp-contract=off -O2 -fno-fast-math -frounding-math experiments/q5_portability/main.cpp experiments/q5_portability/operations.cpp -o build/q5_portability
```

可替換 compiler executable 的完整路徑，但須同 compiler 家族與確切版本。不同 target 是環境差異，須記錄。`-frounding-math`、獨立函式與關閉 LTO 保留執行期運算；long double 加法結果會經 memory barrier 存回型態再相減。

4. **執行**：

```bash
HW2_ROUNDING=nearest ./build/q5_portability
HW2_ROUNDING=upward ./build/q5_portability
HW2_ROUNDING=downward ./build/q5_portability
```

候選 A 直接重用同一 binary，numeric operands 完全相同，只有 execution floating-point environment 不同；這是受控的執行環境案例，不能描述成兩台硬體的比較。候選 B 在兩平台都設定 nearest，需同版 GCC 或同版其他 compiler；正式執行改用 WSL 本地 GNU GCC 16.2.0 與 Mac Homebrew GCC 16.2.0；Mac 版本目前依本人提供，完整輸出與對照仍待實機核對。原先 GCC 15.2.0 與 Apple Clang 的歷史結果不可挪作本次同版本證據。

5. **預期觀察**：中點在 directed rounding 下是否不同？不同 long double digits 是否改變 increment？若兩平台型態相同或輸出相同，保存負結果。浮點精度／環境是有規格的機制；不以 overflow 的 signed integer、未初始化值、aliasing、資料競爭等製造差異。這裡沒有除零、越界或無效記憶體使用。
6. **截圖**：候選 A 保存同 binary 雜湊與兩 modes 輸出；候選 B 保存同 source 雜湊、compiler 完整版本、flags、long double 特性與兩边輸出。

批次結果包含 metadata。完成兩平台執行後可用 `python3 scripts/verify_q5_pair.py results/linux-時間 results/darwin-時間` 檢查必要的版本／旗標／來源一致性；這不是自動認定所有加分條件或因果推論已完成。
