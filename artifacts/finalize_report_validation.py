from pathlib import Path
from zipfile import ZipFile
from copy import deepcopy
from lxml import etree as E

p=Path(__file__).resolve().parents[1]/'Floating_Point_Report_Q0.docx'
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
w='{'+ns['w']+'}'
with ZipFile(p) as z: entries=[(i,z.read(i.filename)) for i in z.infolist()]
r=E.fromstring(next(b for i,b in entries if i.filename=='word/document.xml'))
count=0
for para in r.xpath('.//w:p',namespaces=ns):
    old=''.join(para.xpath('.//w:t/text()',namespaces=ns));new=old
    if old.startswith('目前僅完成程式建置、18 條 kernel'):
        new='助手已用 GCC 16.2.0 完成全部建置、入口檢查及一輪真實 benchmark／精度驗證。原始樣本保存於 results/linux-20261004-032643-assistant/，明確標示操作者；以下本人結果表與截圖仍待親自執行後填入。'
    elif old.startswith('我使用 Codex 協助建立專案'):
        new='我使用 Codex 協助建立專案、撰寫程式與腳本、查閱來源及整理報告方法。助手執行 Q0 採集與建置檢查，後續依我授權安裝 WSL GCC 16.2.0，跑真實 benchmark／精度及 Q2～Q6 驗證，資料獨立標示 assistant。我提供 Mac 設備與 compiler 資訊；本人實際執行、觀察、截圖與驗證方式：【待填】。'
    elif old.startswith('[1] C++ working draft'):
        new=old.replace('[6] ARM／Apple ABI：【待本人查閱】。','[6] Apple arm64 ABI：https://developer.apple.com/documentation/xcode/writing-arm64-code-for-apple-platforms（long double 等同 double；Mac 實測待取得）。')
    if new!=old:
        run=para.find('w:r',ns);props=deepcopy(run.find('w:rPr',ns)) if run is not None and run.find('w:rPr',ns) is not None else None
        for child in list(para):
            if child.tag!=w+'pPr':para.remove(child)
        run=E.SubElement(para,w+'r')
        if props is not None:run.append(props)
        for j,line in enumerate(new.split('\n')):
            if j:E.SubElement(run,w+'br')
            E.SubElement(run,w+'t').text=line
        count+=1
assert count==3,count
with ZipFile(p,'w') as z:
    for i,b in entries:z.writestr(i,E.tostring(r,xml_declaration=True,encoding='UTF-8',standalone=True) if i.filename=='word/document.xml' else b)
print('Updated validation and AI disclosure:',count)
