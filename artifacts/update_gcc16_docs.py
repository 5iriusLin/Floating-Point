from pathlib import Path

root = Path(__file__).resolve().parents[1]
def change(name, pairs):
    p = root / name
    s = p.read_text(encoding='utf-8')
    for old, new in pairs:
        if new in s: continue
        assert old in s, (name, old)
        s = s.replace(old, new)
    p.write_text(s, encoding='utf-8', newline='\n')

change('README.md', [
 ('主要平台：Windows 11 + WSL2 Ubuntu、Intel Core i7-14650HX、GCC 15.2.0；比較平台：MacBook Air 2025、Apple M4、24 GB、Apple Clang 21.0.0。詳見 [Q0 紀錄](docs/q0_environment.md)。兩平台目前 compiler 不同，不可直接宣稱 Q5 ABI 候選滿足同版本條件。', '主要平台：Windows 11 + WSL2 Ubuntu、Intel Core i7-14650HX；比較平台：MacBook Air 2025、Apple M4、24 GB。兩平台正式執行改用 GNU GCC 16.2.0（WSL 本地建置／Mac Homebrew）；Mac 版本由本人提供，完整輸出待核對。原有 GCC 15.2.0 與 Apple Clang 21.0.0 保留。詳見 [Q0 歷史紀錄](docs/q0_environment.md) 與 [工具鏈說明](docs/gcc16_toolchain.md)。Q5 仍需核對來源、版本、flags 與實際輸出。'),
 ('CXX=clang++ bash scripts/run_all.sh', 'CXX=g++-16 bash scripts/run_all.sh'),
])
change('docs/runbook.md', [
 ('CXX=clang++ bash scripts/run_all.sh', 'CXX=g++-16 bash scripts/run_all.sh'),
 ('這可做 Q1 與其他題的跨平台補充，**不能拿不同 compiler 的結果直接宣稱 Q5 候選 B 完成**。若另有匹配版本 GCC，以 `CXX=/完整路徑/g++-版本` 選擇。', '兩平台使用 GNU GCC 16.2.0；Mac 的完整版本輸出仍需實機保存。Q5 候選 B 必須另核對來源、確切版本、flags 與實際結果，不能只憑安裝同版本就宣稱完成。以 `CXX=/完整路徑/g++-16` 可明確選擇 compiler。'),
])
change('experiments/q5_portability/README.md', [
 ('現有 WSL GCC 15.2.0 與 Mac Apple Clang 21.0.0 不符合此條件。', '正式執行改用 WSL 本地 GNU GCC 16.2.0 與 Mac Homebrew GCC 16.2.0；Mac 版本目前依本人提供，完整輸出與對照仍待實機核對。原先 GCC 15.2.0 與 Apple Clang 的歷史結果不可挪作本次同版本證據。'),
])
change('docs/q0_environment.md', [
 ('主實驗使用 WSL `/usr/bin/g++`。', '上述歷史採集使用 WSL `/usr/bin/g++`；正式執行改用本地 GCC 16.2.0，詳見 `docs/gcc16_toolchain.md`。'),
 ('此環境的 `g++` 指令回報 Apple Clang，並非 GCC。它與 WSL GCC 15.2.0 可作跨平台比較，但目前不符合 Q5 的相同編譯器版本條件。', '先前 `g++` 指令回報 Apple Clang，並非 GCC。本人後續提供 Mac 已安裝 GNU GCC 16.2.0（Homebrew），正式執行選用 `g++-16`；完整版本、路徑與 target 尚待採集。WSL 同步使用本地 GCC 16.2.0，歷史 GCC 15.2.0 數據保留。'),
 ('該 script 預設 Apple Clang；若做 Q5，仍需另外滿足同 compiler 版本與旗標條件。', '該 script 優先使用可用的 `g++-16`；可用 `CXX=g++-16` 明確指定。Q5 仍需核對確切 compiler 版本與旗標條件。'),
])
