# GCC 16.2.0 工具鏈

Mac 的 GNU GCC 16.2.0（Homebrew）由使用者提供，完整 `g++-16 --version`、`-dumpfullversion`、`-dumpmachine` 尚待實機保存。原本 Apple Clang 仍可保留。

WSL 的 Ubuntu 套件目前只有 GCC 16 開發快照，因此使用 GNU 官方 GCC 16.2.0 原始碼，安裝到 `$HOME/.local/toolchains/gcc-16.2.0`。安裝腳本是 `scripts/install_gcc_16_2_wsl.sh`；先驗證官方 SHA-512，再以四個平行工作建置 C/C++。這是單階段建置，未執行 GCC bootstrap 或完整 compiler testsuite。

安裝完成後，專案腳本自動選取此工具鏈；Mac 優先選取 `g++-16`。明確指定的 `CXX` 永遠優先。腳本只設定自身程序的環境與 WSL 本地 libstdc++ 搜尋路徑，不修改 shell profile、系統 compiler symlink 或 Windows llvm-mingw。

版本核對：

```bash
# WSL
$HOME/.local/toolchains/gcc-16.2.0/bin/g++ --version
$HOME/.local/toolchains/gcc-16.2.0/bin/g++ -dumpfullversion
$HOME/.local/toolchains/gcc-16.2.0/bin/g++ -dumpmachine
# Mac
g++-16 --version
g++-16 -dumpfullversion
g++-16 -dumpmachine
```

Mac 正式執行用 `CXX=g++-16 bash scripts/run_all.sh`。兩邊 GCC 版本相同後，仍須保存相同來源、編譯旗標、target、ABI 與實际函式庫資訊。版本一致本身不是 Q5 結果，須由本人執行並比較輸出。先前 GCC 15.2.0 的 Q0 紀錄保留為歷史採集，不挪作新版執行結果。

來源：[GNU GCC 16](https://gcc.gnu.org/gcc-16/)、[16.2.0 發行檔案](https://gcc.gnu.org/pub/gcc/releases/gcc-16.2.0/)、[Homebrew gcc](https://formulae.brew.sh/formula/gcc)。
