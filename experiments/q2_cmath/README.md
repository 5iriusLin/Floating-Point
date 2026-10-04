# Q2 std::sqrt 的規格與實作

1. **目的**：區分 C++ overload、compiler builtin、libm 與硬體指令；比較正常值、負值、±0、∞、NaN 及極小值。此題不做計時 benchmark。
2. **程式**：`main.cpp` 記錄各型態的輸入、sqrt、hexfloat、errno、FE_INVALID、FE_INEXACT、signbit；`sqrt_paths.cpp` 隔離待測函式。default 版本呼叫 std::sqrt；libm 版本經 volatile function pointer 呼叫實際 sqrt／sqrtf／sqrtl 符號，不假定 -fno-builtin 能阻止明確寫出的 builtin。
3. **編譯**（專案根目錄，WSL）：

```bash
source scripts/compiler_env.sh
mkdir -p build
"$CXX" -std=c++20 -O2 -fno-fast-math -frounding-math -ffp-contract=off -fno-lto experiments/q2_cmath/main.cpp experiments/q2_cmath/sqrt_paths.cpp -o build/q2_cmath
"$CXX" -std=c++20 -O2 -fno-fast-math -frounding-math -ffp-contract=off -fno-lto -DHW2_FORCE_LIBM=1 experiments/q2_cmath/main.cpp experiments/q2_cmath/sqrt_paths.cpp -o build/q2_libm
```

4. **執行**：`./build/q2_cmath 2`、`./build/q2_libm 2`；`bash scripts/run_all.sh` 自動保存兩版本、assembly、動態依賴與 libm 符號反組譯。
5. **預期觀察**：不同型態是否使用不同 sqrt 指令？預設路徑是否保留負值 fallback？負數是否設定 errno／exception？不要因看到函式名稱就假定實際呼叫某份 generic 原始碼。方法與演算法筆記見 `docs/reference_notes.md`。所有執行輸出待本人採集。
6. **截圖**：兩版本編譯與 positive／negative／signed zero 輸出；三種型態的 sqrt_paths assembly；libm 連結版本與 sqrt 符號反組譯。完整輸出留存文字，不需把全部特殊值塞進一張圖。

`--check` 只測程式入口與 binary floating-point 支援，不執行 sqrt 實驗。C++ overload 以 static_assert 在編譯時檢查。errno／exception 只能依目標平台與 math_errhandling 解釋，不把 GCC／Clang 不同預設設定混作硬體差異。
