from copy import deepcopy
from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E

p=Path(r'C:\Users\ALAN\Desktop\floating-point-hw2\Floating_Point_Report_Q0.docx')
n={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}; w='{'+n['w']+'}'
with ZipFile(p) as z: entries=[(i,z.read(i.filename)) for i in z.infolist()]
root=E.fromstring(dict((i.filename,b) for i,b in entries)['word/document.xml'])
def text(para): return ''.join(para.xpath('.//w:t/text()',namespaces=n))
def replace(para,value):
    r=para.find('w:r',n); props=deepcopy(r.find('w:rPr',n)) if r is not None and r.find('w:rPr',n) is not None else None
    for e in list(para):
        if e.tag!=w+'pPr': para.remove(e)
    r=E.SubElement(para,w+'r')
    if props is not None:r.append(props)
    for i,line in enumerate(value.split('\n')):
        if i:E.SubElement(r,w+'br')
        E.SubElement(r,w+'t').text=line
changes=0
for para in root.findall('w:body/w:p',n):
    old=text(para)
    value=None
    if old.startswith('【待填】說明運算核心、輸入資料'):
        value='準備測量 float、double、long double 的 scalar 加減、乘法及除法。每個 kernel 分為一條相依链與四條獨立鏈，每迭代分別為 2 與 8 個算術運算。初始值由執行期 seed 決定，factor=1+1/1024，配對運算維持值域。預設每組 2 次暖機（每次最多 100000 迭代）、7 次測量（每次 5000000 迭代）；使用 steady_clock，保留原始秒數、每運算時間、中位數與最小／最大值，輪換型態順序。'
    elif old.startswith('【待填】說明如何防止計算被刪除'):
        value='待測 kernel 獨立編譯，關閉 LTO、fast-math、FMA contraction 與自動向量化；noinline 與迴圈前後的 optimization barrier 防止跨函式簡化，每回合輸出 checksum。正式測量前檢查反組譯中仍有算術迴圈與分支。時間包含呼叫、少量參數準備、迴圈控制及收尾 checksum 成本；每運算時間不直接等於單條指令硬體 latency。'
    elif old.startswith('g++ -std=c++20 -O2 benchmark.cpp -o benchmark') and 'benchmark.s' in old:
        value='在 WSL Ubuntu 專案根目錄執行：\nbash experiments/q1_benchmark/build.sh\n./build/q1-scalar/q1_benchmark --check\n./build/q1-scalar/q1_benchmark --iterations 5000000 --repeats 7 --warmup 2 --seed 20261004\nobjdump -d -C build/q1-scalar/kernels.o\n編譯旗標：-std=c++20 -O3 -Wall -Wextra -fno-fast-math -ffp-contract=off -fno-lto -fno-tree-vectorize'
    elif old.startswith('【待填】描述誤差累積實驗與參考值'):
        value='精度測試使用 10000 組 [2^24, 1, -2^24] 與 [2^53, 1, -2^53]，分別正序與反序加總。所有輸入皆可精確表示；實數精確答案為整數 10000，且三種型態都能精確表示。程式報告結果、絕對誤差與相對誤差，不假定 long double 為真值。執行：./build/q1-scalar/q1_benchmark --precision-only。'
    if value is not None:replace(para,value);changes+=1
assert changes==4,changes
q1=None
for para in root.findall('w:body/w:p',n):
    if text(para)=='1 3 效能結果':q1=para;break
assert q1 is not None
notice=deepcopy(q1)
replace(notice,'目前僅完成程式建置、18 條 kernel 路徑的不計時 smoke check 與組合語言檢查。尚未執行正式 benchmark 或精度實驗，以下結果表與截圖待本人執行後填入。')
props=notice.find('w:pPr',n)
if props is not None:notice.remove(props)
q1.addnext(notice)
xml=E.tostring(root,xml_declaration=True,encoding='UTF-8',standalone=True)
with ZipFile(p,'w') as z:
    for i,b in entries:z.writestr(i,xml if i.filename=='word/document.xml' else b)
print('Updated Q1 methods in project-root report; result tables remain pending.')
