# Q4 九位小數輸出與捨入

1. **目的**：檢驗 printf("%.9f") 與 fixed/setprecision(9) 是否等同日常「5 就進位」；分開討論表示誤差、格式化中點與 rounding mode。
2. **程式**：`main.cpp` 測精確二進位值 `1/1024=0.0009765625`、負值與 nextafter 鄰居，並比較四種 rounding mode 下的 printf、iostream。每筆先印高精度實際儲存值與 hexfloat。C locale／iostream classic locale 避免小數點格式干擾。
3. **編譯**：

```bash
source scripts/compiler_env.sh
mkdir -p build
"$CXX" -std=c++20 -O2 -fno-fast-math -frounding-math -ffp-contract=off experiments/q4_formatting/main.cpp -o build/q4_formatting
```

4. **執行**：`./build/q4_formatting 0.0009765625`；另可用 `0.1` 作自選十進位表示案例。批次脚本保存主案例。
5. **預期觀察**：這個精確中點位於 `0.000976562` 與 `0.000976563` 之間，不需猜測十進位字面值是否偏離中點。觀察 nearest 是否選偶數末位，兩種 API 是否一致，以及向上／向下捨入對正負值的影響。`fesetround` 的成功與實際結果均須檢查，不能預先寫下本機結果。
6. **截圖**：exact tie 的 hexfloat、兩種九位輸出與 mode；至少包含 nearest 下正負中點，以及一組鄰近值／另一 mode 對照。

程式完成後恢復原始 rounding mode；四個 modes 都只影響本程式的浮點環境。文件不能把所有 C++ implementation 的格式化政策概括為同一結果。
