from pathlib import Path
from zipfile import ZipFile
from copy import deepcopy
from lxml import etree as E

p = Path(__file__).resolve().parents[1] / 'Floating_Point_Report_Q0.docx'
ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
w = '{' + ns['w'] + '}'
with ZipFile(p) as z:
    entries = [(i, z.read(i.filename)) for i in z.infolist()]
r = E.fromstring(next(b for i, b in entries if i.filename == 'word/document.xml'))
count = 0
for para in r.xpath('.//w:p', namespaces=ns):
    old = ''.join(para.xpath('.//w:t/text()', namespaces=ns))
    new = old
    if old.startswith('WSL 的核心與快取資訊'):
        new = 'WSL 拓樸為虛擬環境資訊。正式執行改用 GNU GCC 16.2.0：WSL 安裝於使用者目錄，Mac 為本人提供的 Homebrew 版本，完整輸出待核對。原有 compiler 保留，上表與型態表為先前採集；新版紀錄待本人重跑。'
    elif old.startswith('下表為 WSL GCC 的實際輸出'):
        new = old.replace('WSL GCC', 'WSL GCC 15.2.0')
    elif old.startswith('GCC 15.2.0 的 fast-math'):
        new = old.replace('GCC 15.2.0', 'GCC 16.2.0')
    elif old.startswith('本節準備兩個候選。'):
        new = '本節準備兩個候選。A 以同一 binary、相同数值輸入比較捨入環境；B 以 GNU GCC 16.2.0 比較兩平台 long double ABI。Mac 版本依本人提供，兩邊完整版本、來源、flags 與實際輸出待核對，不能只憑同版安裝即宣稱完成。'
    elif old.startswith('[1] C++ working draft'):
        new = old.replace('GCC 15.2.0', 'GCC 16.2.0').replace('gcc-15.2.0', 'gcc-16.2.0')
    if old != new:
        run = para.find('w:r', ns)
        props = deepcopy(run.find('w:rPr', ns)) if run is not None and run.find('w:rPr', ns) is not None else None
        for child in list(para):
            if child.tag != w+'pPr': para.remove(child)
        run = E.SubElement(para,w+'r')
        if props is not None: run.append(props)
        for j,line in enumerate(new.split('\n')):
            if j: E.SubElement(run,w+'br')
            E.SubElement(run,w+'t').text=line
        count += 1
assert count == 5, count
with ZipFile(p,'w') as z:
    for i,b in entries:
        z.writestr(i, E.tostring(r,xml_declaration=True,encoding='UTF-8',standalone=True) if i.filename=='word/document.xml' else b)
print('Updated paragraphs:',count)
