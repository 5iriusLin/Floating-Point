# Q3 IEEE 754 與 fast math

1. **目的**：使用相同來源、輸入及最佳化等級，只改 fast-math 狀態，找出結果與產生碼的差異。
2. **程式**：`operations.cpp` 包含 `(a+b)+c`、`a+(b+c)`、`x!=x`；`main.cpp` 以執行期 argv 提供有限輸入，另以 memcpy 建立 binary64 quiet NaN。主要數值案例用 `a=1e16,b=-1e16,c=1`；NaN 是有限值假設的補充案例，與有限值重結合分開解釋。NaN 案例只適用此 binary64 平台，不是任意 C++ 平台的 representation 保證。
3. **編譯**（兩指令只有 fast-math 狀態不同）：

```bash
source scripts/compiler_env.sh
mkdir -p build
"$CXX" -std=c++20 -O3 -fno-lto -ffp-contract=off -fno-fast-math experiments/q3_fast_math/main.cpp experiments/q3_fast_math/operations.cpp -o build/q3_strict
"$CXX" -std=c++20 -O3 -fno-lto -ffp-contract=off -ffast-math experiments/q3_fast_math/main.cpp experiments/q3_fast_math/operations.cpp -o build/q3_fast
```

4. **執行**：`./build/q3_strict 1e16 -1e16 1`、`./build/q3_fast 1e16 -1e16 1`。批次腳本保存逐版本输出、產生碼與 diff。
5. **預期觀察**：重結合是否改變中間捨入？`x!=x` 是否被常數化？fast-math 是允許一組轉換，不保證所有 expression 都會改變。`-ffp-contract=off` 在兩版本相同，避免把 FMA 混入本反例；不得額外修改其他旗標來製造差異。
6. **截圖**：兩個編譯指令、兩版本相同輸入的 output；left_grouped 与 self_inequality 的 strict／fast assembly。已有準備階段組合語言證據，但正式結果仍待本人執行。

NaN 補充案例違反 fast-math 的有限值假設，正是說明此選項的適用限制；不要把這項 compiler assumption 說成一般 C++ 未初始化值或資料競爭造成的 UB。GCC 15.2.0 各子選項來源見 `references/sources.md`。
