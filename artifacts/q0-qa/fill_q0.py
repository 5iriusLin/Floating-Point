from copy import deepcopy
from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E

source = Path(r'C:\Users\ALAN\Downloads\Floating_Point_Report_Template.docx')
output = Path(r'C:\Users\ALAN\Desktop\floating-point-hw2\artifacts\report\Floating_Point_Report_Q0.docx')
NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
W = '{' + NS['w'] + '}'
with ZipFile(source) as z:
    root = E.fromstring(z.read('word/document.xml'))
    body = root.find('w:body', NS)
    paras = body.findall('w:p', NS)
    tables = body.findall('w:tbl', NS)
    def set_text(p, text):
        r = p.find('w:r', NS)
        props = deepcopy(r.find('w:rPr', NS)) if r is not None and r.find('w:rPr', NS) is not None else None
        for child in list(p):
            if child.tag != W + 'pPr': p.remove(child)
        r = E.SubElement(p, W + 'r')
        if props is not None: r.append(props)
        for i, line in enumerate(text.split('\n')):
            if i: E.SubElement(r, W + 'br')
            t = E.SubElement(r, W + 't'); t.text = line
    def cell_text(c, text):
        ps = c.findall('w:p', NS)
        set_text(ps[0], text)
        for p in ps[1:]: c.remove(p)
    def row_text(row, texts):
        for c, text in zip(row.findall('w:tc', NS), texts): cell_text(c, text)
    rows = tables[0].findall('w:tr', NS)
    data = [
        ['項目', '主要平台（助手本機採集）', '輔助平台（本人提供）'],
        ['裝置', 'ASUS TUF Gaming F16 FX608JMR', 'MacBook Air（2025）'],
        ['處理器', 'Intel Core i7-14650HX', 'Apple M4'],
        ['架構／target', 'x86_64-linux-gnu', 'arm64-apple-darwin27.0.0'],
        ['主機系統', 'Windows 11 家用版 25H2\nBuild 26200.9457', 'macOS Golden Gate 27.0.1\n名稱與 build 待 sw_vers 核對'],
        ['執行環境', 'WSL2／Ubuntu 26.04.1 LTS', 'macOS 原生環境'],
        ['編譯器與版本', 'GCC 15.2.0\nUbuntu 15.2.0-16ubuntu1', 'Apple Clang 21.0.0\nclang-2100.3.24.2'],
        ['Q0 編譯參數', '-std=c++20 -O2\n-fno-fast-math -ffp-contract=off', '尚未執行 Q0 型態程式'],
    ]
    for row, texts in zip(rows, data): row_text(row, texts)
    extras = [
        ['核心／執行緒', 'Windows：16／24\nWSL 虛擬拓樸：12／24', '待採集'],
        ['記憶體', '實體 32 GiB；WSL 約 15 GiB\nWSL swap 4 GiB', '24 GB（本人提供）'],
        ['WSL／kernel', 'WSL 2.7.3.0\n6.6.114.1-microsoft-standard-WSL2', '不適用／Darwin kernel 待採集'],
        ['函式庫', 'glibc 2.43-2ubuntu2.4\nlibstdc++6 16-20260322-1ubuntu1', '實際連結版本待採集'],
        ['電源與採集日期', '平衡；AC 電源；電池 100%\n2026/10/04（Asia/Taipei）', '資訊提供：2026/10/04\n電源狀態待採集'],
    ]
    for texts in extras:
        row = deepcopy(rows[-1]); row_text(row, texts); tables[0].append(row)
    set_text(paras[12], 'Windows PowerShell：\n./experiments/q0_environment/collect_windows.ps1\nWSL Ubuntu（專案根目錄）：\nbash experiments/q0_environment/collect_linux.sh results/q0-wsl\nMac（專案根目錄）：\nbash experiments/q0_environment/collect_mac.sh')
    set_text(paras[15], '下表為 WSL GCC 的實際輸出。sizeof 表示儲存空間；long double 的 16 bytes 不等於 128-bit 有效精度。Mac 型態特性尚待實測。')
    # Keep the type-information heading with its table on the next page.
    ppr = paras[14].find('w:pPr', NS)
    if ppr is None: ppr = E.Element(W + 'pPr'); paras[14].insert(0, ppr)
    if ppr.find('w:pageBreakBefore', NS) is None: E.SubElement(ppr, W + 'pageBreakBefore')
    type_rows = tables[1].findall('w:tr', NS)
    for row, texts in zip(type_rows[1:], [
        ['float', '4', '24', '6', '9', 'true'],
        ['double', '8', '53', '15', '17', 'true'],
        ['long double', '16', '64', '18', '21', 'true'],
    ]): row_text(row, texts)
    # Add paragraphs within Q0, preserving existing paragraph style.
    def insert_before(anchor, text, prototype):
        p = deepcopy(prototype); set_text(p, text); anchor.addprevious(p)
        # Avoid inheriting an explicit page break from the prototype.
        ppr = p.find('w:pPr', NS)
        if ppr is not None:
            for tag in ('pageBreakBefore', 'keepNext'):
                for e in ppr.findall('w:' + tag, NS): ppr.remove(e)
        return p
    insert_before(paras[12], 'WSL 的核心與快取資訊為虛擬環境呈現，不能直接當成實體 CPU 拓樸。Mac 的 g++ --version 回報 Apple Clang，與主要平台 GCC 不同；目前不符合 Q5 的同編譯器版本條件。', paras[15])
    insert_before(paras[17], 'WSL 補充輸出：radix=2；alignof 為 4／8／16 bytes；epsilon 為 2^-23／2^-52／2^-63；FLT_EVAL_METHOD=0；捨入模式為 FE_TONEAREST；fast-math 關閉。編譯器支援 __float128 擴充，但尚未測試其運算。', paras[15])
    insert_before(paras[17], 'Q0 重現指令（WSL，專案根目錄）：\ng++ -std=c++20 -O2 -fno-fast-math -ffp-contract=off experiments/q0_environment/main.cpp -o results/q0-wsl/q0_environment\n./results/q0-wsl/q0_environment', paras[12])
    insert_before(paras[17], '原始紀錄：results/q0-windows/hardware.json、results/q0-windows/wsl-power.txt、results/q0-wsl/environment.txt。環境採集與型態程式由助手執行；本人仍須重跑、觀察並加入截圖。CPU 即時頻率、溫度與 Mac 完整採集尚待補充。', paras[15])
    xml = E.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)
    with ZipFile(output, 'w') as out:
        for item in z.infolist():
            out.writestr(item, xml if item.filename == 'word/document.xml' else z.read(item.filename))
with ZipFile(source) as a, ZipFile(output) as b:
    changed = [n for n in a.namelist() if a.read(n) != b.read(n)]
    assert changed == ['word/document.xml'], changed
print(output)
print('Only word/document.xml changed; other package parts preserved.')
