# 理論與來源筆記

本檔是實驗準備用筆記，不能代替本人的結果與分析。來源索引見 `references/sources.md`；每個結論須區分規格、原始碼路徑與實際觀察。

## Q1 型態與硬體

Q0 已取得 WSL float／double／long double 的有效位數為 24／53／64 bits。準備階段反組譯的 Q1 kernel 顯示 float 使用 addss／mulss／divss 類型的 scalar SSE 指令，double 使用 addsd／mulsd／divsd，long double 使用 x87 stack 算術。這是產生碼證據，尚不是速度證據。

解釋正式時間時同時考慮相依链、可併行鏈數、loop overhead、register pressure、CPU 排程與電源。不能從型態名稱推導某個速度比例。sizeof 是 ABI 儲存大小；有效位數才描述 precision。Intel 指令語意可查 [6]，CPU 單一機型的 latency／throughput 還需對應文件或本機量測。

## Q2 sqrt

C++20 的標準浮點 overload 為 sqrt(float)、sqrt(double)、sqrt(long double)，輸入整數時另有讓呼叫等效於 double 的支援。本程式用 static_assert 檢查實際標頭的回傳型態。[1] 是現行 working draft，並非聲稱其所有最新 overload 都屬 C++20。sqrt 計算非負平方根；負有限輸入的 domain error、errno 與 floating-point exception 必須依 math_errhandling 與所用平台解釋。[2]

研究路徑：C++ <cmath> 的 overload → compiler builtin 或 C library symbol → libm wrapper／architecture implementation → hardware instruction 或軟體計算。預設 builtin 可內聯硬體 sqrt，同時保留處理負輸入的 library fallback。forced-libm 版本只是確保從 symbol 進入函式庫，仍可能由函式庫使用硬體 sqrt。批次會保存兩種 caller assembly 與實際 libm 的符號反組譯；看到 PLT 呼叫不代表已掌握 library 內部。

已查阅的 glibc generic double sqrt [3] 包含兩個條件路徑：USE_SQRT_BUILTIN 路徑直接呼叫 builtin；軟體路徑以 exponent／mantissa 做尺度調整，用表格取得 reciprocal sqrt 初值，再以多項式修正、誤差補償與乘积檢查處理最後捨入；極小輸入先縮放。sqrt 沒有 sin 的週期輸入縮減，這裡的縮減是 exponent／mantissa 的範圍正規化。x86 long double 的參考來源 [4] 呼叫 builtin，wrapper [5] 處理負值的 errno。

**[3]～[5] 是查閱的 master 參考來源，未確認與本機 Ubuntu glibc 2.43-2ubuntu2.4 套件完全一致。** 此版本 tag 的線上讀取失敗，不能宣稱來源已精確匹配。正式報告若要把原始碼演算法指認為本機執行路徑，須再以實際反組譯或套件 source version 核對。不應把 generic 軟體演算法套到直接使用硬體指令的路徑，也不能從 FSQRT／SQRTSD 猜測 CPU 內部微架構採用何種迭代方法。

## Q3 fast math

對應 GCC 16.2.0 官方文件 [7]：fast-math 會啟用 no-math-errno、unsafe-math-optimizations、finite-math-only、no-rounding-math、no-signaling-nans、cx-limited-range、excess-precision=fast。unsafe-math-optimizations 又允許 no-signed-zeros、no-trapping-math、associative-math、reciprocal-math 等轉換。這些選項放寬 compiler 必須保留的數值語意，不是讓硬體增加有效位數。

數值有限仍可能因重結合改變中間捨入。準備階段的 operations.s 顯示 strict 與 fast 的 left_grouped 加法順序不同，self_inequality 在 fast 版本變為常數回傳。助手驗證輸出已保存於獨立 assistant 目錄，報告仍需以本人結果與產生碼共同說明。NaN 補充案例專門展示有限值假設的限制；不能在 fast-math 下假定 isnan／isfinite 判定仍可當一般安全檢查。

## Q4 格式化

「四捨五入」若指精確中點一律進位，與 ties-to-even 不同。`1/1024` 可精確表示為二進位；十進位恰為 `0.0009765625`，是小數 9 位的精確中點。這個反例隔離了輸出捨入政策，不混入字面值轉換誤差。nextafter 邻居再用來測略高／略低中點。

程式切換 mode 後比較 printf 與 iostream，須以實際輸出判斷本平台是否遵循相同政策；[8] 說明四種算術 rounding modes，不足以單獨證明所有 C++ 格式化 implementation 的行為。報告不要從預設 rounding mode 推出所有 formatting API 的跨平台保證。

## Q5 条件与合法性

候選 A 的 numeric operands 相同，同 binary 只以環境變數選取浮點環境，再以 fesetround 設定受控的 rounding mode。[8] 定義其支援與成功回傳。這是执行環境案例，不能寫成 OS 自行選了不同 mode；也不能只展示同一 executable 的不同輸入數字來聲稱環境差異。

候選 B 的 long double expression 用明確存回型態的結果，避免 excess precision 混淆。相同 numeric operands 在不同 precision／ABI 下可能不同，但須先滿足同 compiler 家族、版本、同 flags、同 source，再核對數值特性。不同 distribution patch 與函式庫也要保留紀錄，不能只看 `g++` 檔名。兩平台已規劃使用 GNU GCC 16.2.0，完整 Mac 版本與執行輸出尚待取得，故候選 B 未完成。Apple 官方 ABI 文件 [10] 規定 arm64 Apple long double 等同 double；可據此推論候選差異，但不能冒充 Mac 實測。

## Q6 額外細節

subnormal 提供接近零的 gradual underflow。[8][9] 一個小結果即使可精確表示為 subnormal，也不一定和 tiny 且 inexact 的結果具有相同 exception flags；以 min_normal×0.5、denorm_min×0.5、denorm_min×1 三組隔離這些條件。

x86 程式會讀 MXCSR 的 FTZ／DAZ，但不更動它們；x87 long double 不能直接以 SSE control bits 解釋。這次沒有 subnormal benchmark，所以不能宣稱慢多少。所有 exceptions 與輸出待本人採集。
