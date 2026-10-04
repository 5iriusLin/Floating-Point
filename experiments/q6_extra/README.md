# Q6 額外細節 gradual underflow

1. **目的**：觀察接近零的表示與精度，以及「得到 subnormal」和「觸發 underflow exception」是否為同一件事。此實驗補充 Q1 的加總問題，不重複其 cancellation 案例。
2. **程式**：`main.cpp`、`operations.cpp`。float／double／long double 各測 min_normal × 0.5、denorm_min × 0.5、denorm_min × 1；輸出實際值、hexfloat、fpclassify、FE_UNDERFLOW、FE_INEXACT。x86 上讀取並記錄 MXCSR 的 FTZ／DAZ，沒有改動設定；不把 SSE 的 MXCSR 套用到 x87 long double。
3. **編譯**：

```bash
source scripts/compiler_env.sh
mkdir -p build
"$CXX" -std=c++20 -O2 -fno-fast-math -frounding-math -ffp-contract=off -fno-lto experiments/q6_extra/main.cpp experiments/q6_extra/operations.cpp -o build/q6_extra
```

4. **執行**：`./build/q6_extra`；批次腳本會保存輸出。
5. **預期觀察**：精確的 subnormal 結果是否仍保留非零值？更小且不精確的結果是否捨入為零？exception flags 是否不同？Q0 的 denorm_min 只是型態資訊，不能證明執行時沒有 FTZ／DAZ。這裡不測 subnormal 的速度，不以 theory 宣稱本 CPU 會慢多少。
6. **截圖**：三個案例的分類及 exception flags，連同 rounding mode；x86 上另包含 MXCSR。Q6 總結待正式數據完成後整合，不先代寫結論。
