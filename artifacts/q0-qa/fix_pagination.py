from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
p=Path(r'C:\Users\ALAN\Desktop\floating-point-hw2\artifacts\report\Floating_Point_Report_Q0.docx')
n={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
w='{'+n['w']+'}'
with ZipFile(p) as z:
    entries=[(i,z.read(i.filename)) for i in z.infolist()]
root=E.fromstring(dict((i.filename,b) for i,b in entries)['word/document.xml'])
for para in root.findall('w:body/w:p',n):
    if ''.join(para.itertext()).strip()=='0 2 浮點型態資訊':
        pp=para.find('w:pPr',n)
        if pp is None: pp=E.Element(w+'pPr'); para.insert(0,pp)
        if pp.find('w:pageBreakBefore',n) is None: E.SubElement(pp,w+'pageBreakBefore')
xml=E.tostring(root,xml_declaration=True,encoding='UTF-8',standalone=True)
with ZipFile(p,'w') as z:
    for i,b in entries: z.writestr(i,xml if i.filename=='word/document.xml' else b)
