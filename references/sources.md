# 來源紀錄

查閱日期：2026/10/04（Asia/Taipei）。下列來源用於準備方法與理論；不能當作本機執行結果。已查閱 Apple arm64 ABI 文件；本機 glibc 套件原始碼的精確版本匹配尚未完成，但已採集實際 libm 反組譯。

| 支持的主張／題目 | 文件與 URL | 版本或 commit | 查閱日期 | 與實驗的對應 |
|---|---|---|---|---|
| [1] Q2 overload／規格 | [C++ working draft c.math](https://eel.is/c++draft/c.math) | 現行草案；實驗以 C++20 編譯時 static_assert 核對 | 2026/10/04 | sqrt overload；不把草案新增功能套入 C++20 |
| [2] Q2 sqrt／domain error | [glibc Exponents and Logarithms](https://sourceware.org/glibc/manual/latest/html_node/Exponents-and-Logarithms.html) | latest manual | 2026/10/04 | 與 math_errhandling、errno／exception 實測對照 |
| [3] Q2 generic 演算法 | [glibc double e_sqrt.c](https://raw.githubusercontent.com/bminor/glibc/master/sysdeps/ieee754/dbl-64/e_sqrt.c) | master；未匹配本機 2.43 套件 | 2026/10/04 | builtin 分支／表格初值／多項式修正／捨入 |
| [4] Q2 x86 long double 路徑 | [glibc x86 e_sqrtl.c](https://raw.githubusercontent.com/bminor/glibc/master/sysdeps/x86/fpu/e_sqrtl.c) | master；未匹配本機 2.43 套件 | 2026/10/04 | builtin 路徑参考 |
| [5] Q2 wrapper | [glibc w_sqrt_template.c](https://raw.githubusercontent.com/bminor/glibc/master/math/w_sqrt_template.c) | master；未匹配本機 2.43 套件 | 2026/10/04 | 負值 errno handling |
| [6] Q1／Q2／Q6 指令 | [Intel SDM 官方入口](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html) | 入口更新 2026/09/21；特定指令章節尚待詳讀 | 2026/10/04 | SSE／x87／MXCSR 來源入口；不能只凭入口證明微架構細節 |
| [7] Q3／Q5 GCC flags | [GCC 16.2.0 Optimize Options](https://gcc.gnu.org/onlinedocs/gcc-16.2.0/gcc/Optimize-Options.html) | 精確 GCC release 15.2.0 | 2026/10/04 | fast-math 子旗標与 rounding-math 限制 |
| [8] Q4／Q5／Q6 modes | [glibc Rounding Modes](https://sourceware.org/glibc/manual/latest/html_node/Rounding.html) | latest manual | 2026/10/04 | fesetround／四種模式／underflow；不是所有格式化 API 的保證 |
| [9] Q0 型態參數 | [glibc Floating Point Parameters](https://sourceware.org/glibc/manual/latest/html_node/Floating-Point-Parameters.html) | latest manual | 2026/10/04 | digits／min／epsilon 的定義 |
| [10] Q5 Apple ABI | [Writing ARM64 code for Apple platforms](https://developer.apple.com/documentation/xcode/writing-arm64-code-for-apple-platforms) | Apple 官方文件，現行 | 2026/10/04 | long double 等同 double；Mac Q0 仍需核對 |
