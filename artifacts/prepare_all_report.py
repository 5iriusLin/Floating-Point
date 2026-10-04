from copy import deepcopy
from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E

p=Path(r'C:\Users\ALAN\Desktop\floating-point-hw2\Floating_Point_Report_Q0.docx')
n={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'};w='{'+n['w']+'}'
with ZipFile(p) as z: entries=[(i,z.read(i.filename)) for i in z.infolist()]
root=E.fromstring(dict((i.filename,b) for i,b in entries)['word/document.xml'])
def text(para):return ''.join(para.xpath('.//w:t/text()',namespaces=n))
def replace(para,value):
    r=para.find('w:r',n); props=deepcopy(r.find('w:rPr',n)) if r is not None and r.find('w:rPr',n) is not None else None
    for e in list(para):
        if e.tag!=w+'pPr':para.remove(e)
    r=E.SubElement(para,w+'r')
    if props is not None:r.append(props)
    for i,line in enumerate(value.split('\n')):
        if i:E.SubElement(r,w+'br')
        E.SubElement(r,w+'t').text=line
mapping=[
('本節預定研究 std::sqrt。', '本節研究 std::sqrt，比較預設 std／builtin 路徑與強制 libm symbol 路徑，並測試三種型態及特殊值。'),
('【待填】記錄 overload、回傳型態', 'C++20 標準浮點 overload 分別回傳 float、double、long double；整數呼叫等效使用 double，本程式已用 static_assert 核對標頭。sqrt 計算非負平方根；負值 domain error 的 errno／exception 行為依 math_errhandling 與本機實測判斷。[1][5]'),
('#include <cmath>', '#include <cmath>\n// experiments/q2_cmath/sqrt_paths.cpp\nfloat sqrt_path(float x) { return std::sqrt(x); }\ndouble sqrt_path(double x) { return std::sqrt(x); }\nlong double sqrt_path(long double x) { return std::sqrt(x); }\n// 實際程式另有 noinline；libm 版使用 volatile function pointer。'),
('g++ -std=c++20 -O2 -S sqrt_test.cpp', '在專案根目錄：bash scripts/build_all.sh\n./build/all/q2_cmath 2\n./build/all/q2_libm 2\n旗標：-O2 -fno-fast-math -frounding-math -ffp-contract=off -fno-lto\nlibm 版另加 -DHW2_FORCE_LIBM=1；完整命令記錄在 build.txt。'),
('【待填】追蹤 std::sqrt', '研究路徑為 C++ overload、compiler builtin／libm、硬體指令或軟體演算法。查閱的 glibc generic double sqrt 以 exponent／mantissa 縮放、表格 reciprocal sqrt 初值、多項式修正與誤差補償處理捨入；另有直接 builtin 分支。此 master 來源尚未與 Ubuntu 套件精確匹配，正式路徑須用批次保存的反組譯驗證，不能將 generic 分支直接認定為本機實作。[5]'),
('【待填】依 GCC 官方文件說明本實驗涉及', 'GCC 15.2.0 的 fast-math 會放寬 errno、有限值、捨入模式與運算順序等語意，並允許 associative／reciprocal 類轉換。本實驗主要隔離加法重結合，另測 NaN 的有限值假設；兩版本同設 -ffp-contract=off，避免混入 FMA。[2]'),
('【待填】放入完整關鍵運算', '關鍵運算為 (a+b)+c、a+(b+c)、x!=x。a、b、c 從 argv 讀入，使用 1e16、-1e16、1；獨立 translation unit 與關閉 LTO 保留執行期計算。NaN 以 binary64 quiet NaN bits 建立，屬有限值假設的補充案例，與主要有限輸入反例分開分析。'),
('g++ -std=c++20 -O2 fast_math.cpp', 'bash scripts/build_all.sh\n./build/all/q3_strict 1e16 -1e16 1\n./build/all/q3_fast 1e16 -1e16 1\n兩版本同用 -std=c++20 -O3 -fno-lto -ffp-contract=off；\n只將 -fno-fast-math 換成 -ffast-math。\n完整來源：experiments/q3_fast_math/main.cpp 與 operations.cpp。'),
('【待填】選擇反例，記錄十進位字面值', '選用 1/1024=0.0009765625，這是可精確表示的二進位值，也是 9 位小數的精確中點，介於 0.000976562 與 0.000976563。比較正負值、nextafter 鄰居及四種 rounding mode；每筆記錄 hexfloat、高精度儲存值、printf 與 iostream。結果仍待本人驗證。'),
('#include <cstdio>', '// 完整程式：experiments/q4_formatting/main.cpp\ndouble tie = std::ldexp(1.0, -10);\nstd::fesetround(FE_TONEAREST);\nprintf("%.9f\\n", tie);\nstd::cout << std::fixed << std::setprecision(9) << tie;\n// 另測負值、nextafter 與 upward／downward／towardzero。\n// 編譯：bash scripts/build_all.sh\n// 執行：./build/all/q4_formatting 0.0009765625'),
('本節為加分實驗。', '本節準備兩個候選。A 在同一 binary、相同數值輸入下，只改浮點捨入執行環境；B 比較兩平台 long double ABI，但需同來源、compiler 家族／確切版本與 flags。現有 WSL GCC 與 Mac Apple Clang 不匹配，B 尚未滿足條件。'),
('【待填】放入實驗程式並解釋標準允許差異', '候選 A：add_double(1.0, 2^-53)，以 HW2_ROUNDING 選 mode；候選 B：nearest 下對 long double 計算 (2^53+1)-2^53，加法結果明確存回型態。獨立函式、關閉 LTO、-frounding-math 保留執行期運算；本案例不使用越界、未初始化值、資料競爭等一般 C++ UB。結果與條件仍待本人採集。[2]'),
('候選主題為 catastrophic cancellation。', '額外主題為 gradual underflow。觀察接近零時 subnormal 的保留與精度，以及精確 subnormal 和 tiny／inexact 結果是否有不同 exception flags；這與 Q1 的加總案例分開討論。'),
('直接計算：sqrt(x + 1)', '三組算式：min_normal × 0.5；denorm_min × 0.5；denorm_min × 1。\n每組記錄結果、hexfloat、fpclassify、FE_UNDERFLOW、FE_INEXACT。'),
('【待填】選擇 x，說明 x + 1', '程式：experiments/q6_extra/main.cpp 與 operations.cpp。\n編譯：bash scripts/build_all.sh；執行：./build/all/q6_extra。\n先設定 nearest，x86 另讀取 MXCSR 的 FTZ／DAZ，但不改設定。不能以 SSE 控制位解釋 x87 long double；本題不量測 subnormal 速度。'),
('【截圖位置】6 1 兩種公式', '【截圖位置】6 1 三種型態的 subnormal／underflow 輸出\n包含 exception flags、rounding mode 與 x86 MXCSR。'),
('【待填】根據實驗說明數學等價', '【待填】根據實測區分 subnormal 表示、捨入為零與 underflow／inexact flags，並整合 Q1～Q5 提出浮點運算使用準則。'),
('本次作業使用 ChatGPT 與 Codex', '我使用 Codex 協助建立專案、撰寫 Q0～Q6 程式、建置與批次執行腳本、查閱來源及整理報告方法。助手曾在本機執行 Q0 採集、编譯與不計時程式檢查；尚未執行正式 benchmark 或 Q1 精度／Q2～Q6 案例。我已提供 Mac 設備與 compiler 資訊，完整實驗預定最後統一手動執行。本人實際執行、觀察、截圖與驗證方式：【待填】。'),
('[1] C++ 標準或標準函式庫文件', '[1] C++ working draft c.math：https://eel.is/c++draft/c.math（現行草案；C++20 overload 另以編譯檢查）。\n[2] GCC 15.2.0 Optimize Options：https://gcc.gnu.org/onlinedocs/gcc-15.2.0/gcc/Optimize-Options.html\n[3] IEEE 754 正式標準／相關表示與例外條文：【待本人查閱】\n[4] Intel SDM：https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html（特定章節待詳讀）。\n[5] glibc sqrt manual 與 e_sqrt.c／e_sqrtl.c／wrapper：完整 URL 見專案 references/sources.md；master source 尚未匹配本機套件。\n[6] ARM／Apple ABI：【待本人查閱】。\n上述已查閱來源日期：2026/10/04；理論筆記見 docs/reference_notes.md。'),
]
changed=0
for para in root.findall('w:body/w:p',n):
    old=text(para)
    for prefix,new in mapping:
        if old.startswith(prefix):replace(para,new);changed+=1;break
assert changed==len(mapping),(changed,len(mapping))
tables=root.findall('w:body/w:tbl',n)
def fill_table(table,rows):
    for row,values in zip(table.findall('w:tr',n),rows):
        for cell,s in zip(row.findall('w:tc',n),values):
            ps=cell.findall('w:p',n);replace(ps[0],s)
            for extra in ps[1:]:cell.remove(extra)
fill_table(tables[8],[['型態／案例','result / hexfloat','分類','UF / inexact'],
                     ['待本人執行','待填','待填','待填']])
fill_table(tables[9],[['工具','協助內容','本人驗證方式'],
                     ['ChatGPT','依本人實際使用補充','待填'],
                     ['Codex','程式、腳本、來源查閱、Q0 採集、報告方法','正式執行、觀察與截图待補']])
# Add a short unified-run paragraph before the Q1 section, after Q0.
for para in root.findall('w:body/w:p',n):
    if text(para)=='Q1 不同浮點型態的效能與精度':
        note=deepcopy(para);replace(note,'统一執行方式：Windows 先跑 collect_windows.ps1；WSL 專案根目錄執行 bash scripts/run_all.sh。每次自動建立 results/linux-日期時間，保存所有原始紀錄、命令、flags、來源雜湊與 assembly。各題結果及截图尚待本人完成，實驗手冊見 docs/runbook.md。')
        props=note.find('w:pPr',n)
        if props is not None:note.remove(props)
        para.addprevious(note);break
xml=E.tostring(root,xml_declaration=True,encoding='UTF-8',standalone=True)
with ZipFile(p,'w') as z:
    for i,b in entries:z.writestr(i,xml if i.filename=='word/document.xml' else b)
print('Prepared all methods in the same root report; no measured results inserted.')
