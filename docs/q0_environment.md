# Q0 實際環境採集

採集日期：2026/10/04（Asia/Taipei）。此處為助手在本機執行環境採集的實際結果，非 benchmark；本人仍需親自重跑並截圖。

| 項目 | 實際採集值 |
|---|---|
| 電腦 | ASUS TUF Gaming F16 FX608JMR |
| Windows | Windows 11 家用版 25H2，完整 build 26200.9457 |
| CPU | Intel Core i7-14650HX |
| Windows 核心／執行緒 | 16／24 |
| 實體 RAM | 2 × 16 GiB；韌體回報 configured speed 5600 |
| 電源 | 平衡；採集時電池 100%，BatteryStatus=2（AC 電源） |
| WSL | 2.7.3.0，Ubuntu 發行版使用 WSL2 |
| Ubuntu | 26.04.1 LTS，x86_64、little endian |
| Linux kernel | 6.6.114.1-microsoft-standard-WSL2 |
| WSL CPU 拓樸 | 24 logical CPUs；虛擬拓樸顯示 12 cores × 2 threads |
| WSL 可見 RAM／swap | 約 15 GiB／4 GiB，精確數值见原始紀錄 |
| GCC/G++ | Ubuntu 15.2.0-16ubuntu1，版本 15.2.0，`/usr/bin/g++` |
| glibc | 2.43-2ubuntu2.4 |
| CMake | 4.2.3（WSL） |
| runtime 套件 | libstdc++6／libquadmath0：16-20260322-1ubuntu1；與 GCC 前端版本分開記錄 |
| GCC 預設 target | x86_64-linux-gnu；此組旗標下 `-march=x86-64`、`-mtune=generic` |
| CPU 可見能力 | SSE、SSE2、AVX、AVX2、FMA 等；完整 flags 已保存 |
| Q0 編譯 | `g++ -std=c++20 -O2 -fno-fast-math -ffp-contract=off experiments/q0_environment/main.cpp -o results/q0-wsl/q0_environment` |
| Q0 runtime | 64-bit pointer、`FLT_EVAL_METHOD=0`、`FE_TONEAREST`、fast-math 關閉 |

WSL 的拓樸及 cache 資訊是虛擬環境提供的資訊，不能當成實體 P/E 核心配置。CPU 的即時頻率、溫度與 Windows 對實體核心的排程尚未採集；WSL 中 cpufreq governor／driver 介面不可用。正式 benchmark 前應重新記錄電源與背景負載。Windows 中 `g++.exe` 位於 llvm-mingw 目錄，上述歷史採集使用 WSL `/usr/bin/g++`；正式執行改用本地 GCC 16.2.0，詳見 `docs/gcc16_toolchain.md`。

## Mac 比較環境（使用者提供）

以下資訊由使用者於 2026/10/04 提供，助手未在 Mac 上執行採集。

| 項目 | 使用者提供值 |
|---|---|
| 電腦 | MacBook Air（2025），Apple M4 |
| 記憶體 | 24 GB |
| macOS | Golden Gate 27.0.1（依使用者提供名稱記錄；待 `sw_vers` 核對版本與 build） |
| 執行的版本指令 | `g++ --version` |
| 實際編譯器 | Apple clang version 21.0.0（clang-2100.3.24.2） |
| compiler target | arm64-apple-darwin27.0.0 |
| thread model | posix |

先前 `g++` 指令回報 Apple Clang，並非 GCC。本人後續提供 Mac 已安裝 GNU GCC 16.2.0（Homebrew），正式執行選用 `g++-16`；完整版本、路徑與 target 尚待採集。WSL 同步使用本地 GCC 16.2.0，歷史 GCC 15.2.0 數據保留。compiler target 不取代 `sw_vers` 的 OS 版本紀錄，thread model 也不代表 CPU 執行緒數。

待補：`sw_vers` 完整輸出、核心數、電源狀態、編譯器路徑、實際連結函式庫，以及 Q0 浮點型態輸出。尚未將 WSL 的型態結果套用到 Mac。

## WSL 浮點數型態的實測特性

| 型態 | sizeof | alignof | 二進位有效位數 | digits10 | max_digits10 | epsilon |
|---|---:|---:|---:|---:|---:|---|
| float | 4 | 4 | 24 | 6 | 9 | 2^-23 |
| double | 8 | 8 | 53 | 15 | 17 | 2^-52 |
| long double | 16 | 16 | 64 | 18 | 21 | 2^-63 |

三者 `radix=2`、`is_iec559=true`、`has_denorm=1`；這些型態特性不代表已測試所有執行時 IEEE 754 行為。long double 的結果符合 x86 extended precision 型態特性，16 bytes 是儲存／ABI 大小，不能視為 128-bit 有效精度。編譯器回報 `__float128` 大小 16 bytes，但本次未測其計算與 libquadmath 呼叫。

## 重現與截圖

Windows PowerShell：

```powershell
./experiments/q0_environment/collect_windows.ps1
```

WSL Ubuntu 終端：

```bash
cd /mnt/c/Users/ALAN/Desktop/floating-point-hw2
bash experiments/q0_environment/collect_linux.sh results/q0-wsl
```

原始資料：`results/q0-windows/hardware.json`、`results/q0-windows/wsl-power.txt`、`results/q0-wsl/environment.txt`。Linux 紀錄包含每個指令與退出碼、compiler target/options、函式庫套件版本、可執行檔依賴與來源／binary SHA-256。工具探索命令因未找到 ninja 退出 127，Q0 編譯與執行均成功。Windows WSL 版本輸出的中文標籤存在編碼問題，數字已保留；截圖時可直接在終端執行 `wsl --version`。

截圖建議：① Windows 硬體與 WSL 版本；② Ubuntu／kernel、GCC 與 glibc 版本；③ Q0 編譯指令及三種浮點型態輸出。助手本次只保存文字資料，尚未產生截圖。

Mac 已有上述使用者提供資訊，尚未執行完整採集。在 Mac 專案根目錄執行 `bash experiments/q0_environment/collect_mac.sh`；結果存入 `results/q0-mac/`。該 script 優先使用可用的 `g++-16`；可用 `CXX=g++-16` 明確指定。Q5 仍需核對確切 compiler 版本與旗標條件。
