from pathlib import Path

root = Path(__file__).resolve().parents[1]
def replace(name, old, new):
    p = root/name
    s = p.read_text(encoding='utf-8')
    if new in s: return
    assert old in s, (name,old)
    p.write_text(s.replace(old,new),encoding='utf-8',newline='\n')

replace('README.md','**尚未執行正式 benchmark、精度或 Q2～Q6 實驗案例；結果表與截圖待本人實際執行。** 準備階段的編譯／入口／短程 kernel 檢查不是正式數據。','**助手已用 GCC 16.2.0 執行一輪實際 benchmark、精度與 Q2～Q6 案例，全部成功；本人明天的執行與截圖仍待完成。** 助手紀錄獨立保存在 `results/linux-20261004-032643-assistant/`，不填作本人結果。見 [檢查紀錄](docs/assistant_validation.md)。')
replace('README.md','**這是正式實驗執行命令，準備階段未由助手執行。**','預設記錄 `executed_by=student`；助手驗證使用 `HW2_RUN_ROLE=assistant` 並加目錄後綴，兩者分開保存。')
replace('README.md','cmake -S . -B build/cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_COMPILER=g++','source scripts/compiler_env.sh\ncmake -S . -B build/cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_COMPILER="$CXX"')
replace('docs/runbook.md','沒有正式 timing、精度或 Q2～Q6 的執行結果，沒有偽造截圖。','助手已按本人後續授權，以 GCC 16.2.0 實際跑完整批次與 benchmark，保存到帶 assistant 後綴的目錄；詳見 `docs/assistant_validation.md`。本人仍需明天親自跑與截圖，Word 的本人結果欄保留待填。')
replace('docs/runbook.md','若用 CMake：`cmake -S . -B build/cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_COMPILER=g++`','若用 CMake，先 `source scripts/compiler_env.sh`，再 `cmake -S . -B build/cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_COMPILER="$CXX"`')
replace('docs/report_outline.md','尚未執行正式 benchmark、精度或 Q2～Q6 正式案例。','後續經本人授權，安裝 WSL GCC 16.2.0 並執行完整 benchmark／精度與 Q2～Q6 驗證，原始紀錄明確標為 assistant。')
replace('docs/reference_notes.md','對應 GCC 15.2.0 官方文件','對應 GCC 16.2.0 官方文件')
replace('docs/reference_notes.md','程式的正式輸出尚未執行，報告需以本人結果與產生碼共同說明。','助手驗證輸出已保存於獨立 assistant 目錄，報告仍需以本人結果與產生碼共同說明。')
replace('docs/reference_notes.md','現有 Mac／WSL compiler 不匹配，故目前候選 B 未完成。','兩平台已規劃使用 GNU GCC 16.2.0，完整 Mac 版本與執行輸出尚待取得，故候選 B 未完成。Apple 官方 ABI 文件 [10] 規定 arm64 Apple long double 等同 double；可據此推論候選差異，但不能冒充 Mac 實測。')
replace('references/sources.md','尚未完成 ARM／Apple ABI 文件與本機 glibc 套件原始碼的精確版本匹配。','已查閱 Apple arm64 ABI 文件；本機 glibc 套件原始碼的精確版本匹配尚未完成，但已採集實際 libm 反組譯。')
replace('references/sources.md','GCC 15.2.0','GCC 16.2.0')
replace('references/sources.md','gcc-15.2.0','gcc-16.2.0')
p=root/'references/sources.md'
s=p.read_text(encoding='utf-8')
if '[10] Q5 Apple' not in s:
    s += '| [10] Q5 Apple ABI | [Writing ARM64 code for Apple platforms](https://developer.apple.com/documentation/xcode/writing-arm64-code-for-apple-platforms) | Apple 官方文件，現行 | 2026/10/04 | long double 等同 double；Mac Q0 仍需核對 |\n'
p.write_text(s,encoding='utf-8',newline='\n')

for p in (root/'experiments').glob('*/README.md'):
    s=p.read_text(encoding='utf-8')
    if 'g++ -std=' in s:
        s=s.replace('g++ -std=', '"$CXX" -std=')
        s=s.replace('```bash\n','```bash\nsource scripts/compiler_env.sh\nmkdir -p build\n',1)
        p.write_text(s,encoding='utf-8',newline='\n')
