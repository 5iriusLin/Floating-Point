"""Insert the personally collected Mac Q5 evidence into the existing report."""
from pathlib import Path
from copy import deepcopy
import json,hashlib
from docx import Document
from docx.shared import Inches,Pt
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'Floating_Point_Report_Q0.docx';d=Document(p);ps=list(d.paragraphs)
assert 'Mac Q5 的本人重跑與截圖尚待補入' in ps[6].text,'Already filled or unexpected report'
mac='results/q5-darwin-20261004-211048-student-wdBjAR'
replacements={
6:'本報告整理我於 2026/10/04 親自執行的 Windows／WSL 與 Mac Q5 實驗。Windows 採集時間為 20:07:12；WSL 批次於 20:13:49 開始，結果目錄為 results/linux-20261004-201349。Mac Q5 於 21:10:48 開始，結果目錄為 '+mac+'。兩批皆標示 executed_by=student，failed_experiments=0；助手試跑不混入本人數據。',
120:'本人已在 Windows／WSL 與 Apple M4 Mac 完成 Q5。案例 A 使用各平台的同一 binary、同一輸入，只改變 rounding environment；案例 B 使用相同 Q5／common 來源、GNU GCC release 16.2.0 與逐字相同旗標，在 nearest 下比較 long double ABI。pair checker 的 compiler family、version、flags 與 source 四項皆 MATCH；完整版本與 vendor configuration 另存於原始資料，兩端不是同一 compiler binary。',
123:'案例 A：add_double(1.0, 2^-53)，以 HW2_ROUNDING 選 mode；案例 B：nearest 下以 long double 計算 (2^53+1)-2^53，加法結果經 memory barrier 明確存回型態。輸入有限且不溢位，不使用越界、未初始化值或資料競爭；使用本機 GCC 支援的 inline asm，並核對兩端實際產生碼。獨立函式、關閉 LTO 與 fast-math，使本例的加法、儲存與減法仍可觀察。[2]',
129:'Mac 本人採集目錄：'+mac+'。下列新增證據均來自本人執行與截圖；先前 assistant 目錄只保留為流程預檢。正式命令：CXX=g++-16 bash scripts/run_q5.sh run；核對命令：python3 scripts/verify_q5_pair.py results/linux-20261004-201349 '+mac+'。',
131:'案例 A：double 的 1+2^-53 為 1 與下一個可表示值的中點。兩平台本人結果皆在 nearest／downward／towardzero 得 0x1p+0，upward 得 0x1.0000000000001p+0；應比較 hexfloat，十進位格式化也受捨入模式影響。案例 B：WSL long double 的有效位數為 64，能精確保留 2^53+1，再減 2^53 得 1；Mac 的有效位數為 53，2^53 附近相鄰值間隔為 2，2^53+1 是中點，nearest ties-to-even 存回 2^53，因此減法得 0。兩端產生碼都保留加、存回與減，差異符合 long double 型態精度及 ABI，無需假設未定義行為。Apple arm64 ABI 的 long double 與 double 相同，與本次 8 bytes／53 digits 的實測一致。[6]',
133:'在相同來源、相同 GNU GCC release 16.2.0 與旗標下，本人實測同一 long double 計算於 WSL 得 1、Mac 得 0；nearest 狀態及實際產生碼均已核對。本例顯示相同型態名稱不保證跨平台精度相同。這是兩套已記錄 target／vendor build 的比較，不能把相同 release 說成相同 compiler binary；pair checker 也不單獨證明所有浮點語意相同。GCC 對 frounding-math 的文件仍有限制，因此本例以旗標、產生碼和實測共同支持結論。[2]',
136:'本機結果支持按需求選擇浮點型態：float／double 沒有固定速度比例；較高精度能保留某些小增量，但仍是有限精度。std::sqrt 可經 compiler builtin 或 libm，兩者最終都可使用硬體。fast-math 會改變重結合與特殊值語意；十進位輸出不能概括為中點一律進位。Q5 又實測到 WSL 與 Mac 的 long double 有效精度不同，使同一運算分別得 1 與 0；跨平台重現還必須記錄 ABI、型態參數、compiler、旗標、runtime 與捨入狀態。Mac 本次只做 Q5，不作跨平台速度比較。',
151:'以下依本人實際執行與 Codex 協助範圍揭露。',
152:'我提供 Windows／Mac 設備資訊，親自在 Windows PowerShell／WSL 執行環境採集與完整 Q0～Q6 批次，再於 Mac 執行 Q5、採集環境與 compiler 資訊，並顯示結果後截圖。Codex 協助建立程式與保存腳本、安裝 WSL GCC 16.2.0、查閱來源、做 assistant 預檢，以及將本人真實數據與截圖整理成表格和分析。本報告取用 linux-20261004-201349 與 q5-darwin-20261004-211048-student-wdBjAR 的本人結果，不混用 assistant 計時。原因分析由 AI 協助草擬，我仍需逐段驗證理解。',
163:'[6] Apple Writing ARM64 code\nhttps://developer.apple.com/documentation/xcode/writing-arm64-code-for-apple-platforms\nApple arm64 ABI；本次本人 Mac long double 8 bytes／53 digits 的實測及產生碼與此規定一致。',
165:'目前完成範圍與提交檢查',
166:'Windows／WSL 本人數據、Mac 本人 Q5、兩端條件核對、原始 log 與必要截圖均已整理。Mac 電源狀態未採集，如實列為未記錄；本次未宣稱 Mac benchmark 效能。提交前仍需本人確認分析與 AI 揭露，另輸出 PDF，命名為 113062331_林欣磊.pdf。',
179:'本人 WSL 結果：results/linux-20261004-201349/；Windows snapshot：results/q0-windows/20261004-200712/；本人 Mac Q5：'+mac+'/。Windows 圖片位於 screenshot，Mac 圖片位於 mac截圖。原始檔與截圖均保留；Word 只裁去空白或縮放，未重繪數字。',
187:'Windows screenshot 共 21 張原圖，18 張已嵌入，另三張為重複顯示。Mac 四張原圖全部嵌入；圖 0-5 為環境，圖 5-3 為條件核對，圖 5-4 為四模式輸出，圖 5-5 為組合語言。全部 25 張原圖均保存。'}
for i,s in replacements.items():ps[i].text=s
T=d.tables
macenv={0:'輔助平台（本人實測）',3:'aarch64-apple-darwin27',4:'macOS 27.0.1\nBuild 26A434',6:'GNU GCC 16.2.0\nHomebrew GCC 16.2.0',7:'Q5 使用相同旗標\n-O2 -frounding-math',8:'實體核心 10／執行緒 10',9:'25,769,803,776 bytes\n24 GiB（sysctl 實測）',10:'Darwin 27.0.0\nARM64_T8132',11:'Homebrew libstdc++.6.dylib\n系統 libSystem.B.dylib',12:'本人 Q5：2026/10/04 21:10:48\n電源狀態未採集'}
for row,val in macenv.items():T[0].cell(row,2).text=val
q5vals={1:'Q5／common 四個來源 SHA-256\n與本人 WSL 全部 MATCH',2:'GNU GCC 16.2.0\nHomebrew build',3:T[7].cell(3,1).text,4:'aarch64-apple-darwin27',5:'long double 8 bytes／53 digits\n(2^53+1)-2^53 = 0',6:'macOS 27.0.1／Darwin 27.0.0\nHomebrew libstdc++、libSystem'}
for row,val in q5vals.items():T[7].cell(row,2).text=val
T[9].cell(1,1).text='提供設備資訊；Windows／WSL 環境、完整批次與截圖；Mac Q5 執行、环境採集與四張截圖'
figs=[]
def para_before(anchor,text,style=None):
 x=anchor.insert_paragraph_before(text,style);return x
def fig_before(anchor,name,label,width=6.5):
 f=ROOT/'mac截圖'/name
 x=para_before(anchor,'');x.paragraph_format.keep_with_next=True;x.add_run().add_picture(str(f),width=Inches(width))
 c=para_before(anchor,label+'（原檔：'+name+'）');c.paragraph_format.space_after=Pt(10)
 for r in c.runs:r.font.size=Pt(9)
 figs.append({'file':'mac截圖/'+name,'caption':label,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
q1=next(x for x in ps if x.text=='Q1 不同浮點型態的效能與精度')
para_before(q1,'Mac 本人環境採集','Heading 2').paragraph_format.page_break_before=True
fig_before(q1,'截圖 2026-10-04 晚上9.15.04.png','圖 0-5 Mac 本人 macOS build、M4 核心／記憶體、GCC 16.2.0 與 target。')
para_before(q1,'本次 Mac 的 Q5 由原生 arm64 程式執行。sysctl 的 hw.model 為 Mac16,12；完整 uname、otool runtime 依賴與 Xcode SDK 路徑保存在本人結果目錄。電源與溫度未採集；本次 Mac 不提供效能計時比較。')
a=ps[130]
fig_before(a,'截圖 2026-10-04 晚上9.15.48.png','圖 5-3 本人兩端 GCC family／release、逐字旗標與來源的四項 MATCH。')
para_before(a,'兩平台本人 Q5 結果對照','Heading 2')
t=d.add_table(rows=1,cols=3);t.style=T[7].style;a._p.addprevious(t._tbl)
rows=[['觀察','Windows／WSL 本人','Apple M4 Mac 本人'],['long double sizeof／digits','16 bytes／64 bits','8 bytes／53 bits'],['max_exponent','16384','1024'],['ABI 案例捨入狀態','FE_TONEAREST','FE_TONEAREST'],['(2^53+1)-2^53','1，hex 0x8p-3','0，hex 0x0p+0'],['double 1+2^-53：nearest／down／towardzero','0x1p+0','0x1p+0'],['double 1+2^-53：upward','0x1.0000000000001p+0','0x1.0000000000001p+0']]
for j,row in enumerate(rows):
 cells=t.rows[0].cells if j==0 else t.add_row().cells
 for k,val in enumerate(row):
  cells[k].text=val
  for pp in cells[k].paragraphs:
   for r in pp.runs:r.font.size=Pt(10)
  cells[k].width=Inches([2.9,1.8,1.8][k])
 if j==0:
  trpr=t.rows[0]._tr.get_or_add_trPr();trpr.append(OxmlElement('w:tblHeader'))
 for c in cells:
  for pp in c.paragraphs:pp.paragraph_format.space_after=Pt(3)
  if j==0:
   for r in c.paragraphs[0].runs:r.bold=True
   shade=OxmlElement('w:shd');shade.set(qn('w:fill'),'E8EDF2');c._tc.get_or_add_tcPr().append(shade)
fig_before(a,'截圖 2026-10-04 晚上9.16.28.png','圖 5-4 Mac 本人四模式：double 的受控捨入差異與 nearest long double 結果 0。')
fig_before(a,'截圖 2026-10-04 晚上9.17.09.png','圖 5-5 Mac 的 FADD D 暫存器、STR／LDR 與 FSUB；加法存回後才減回。')
para_before(a,'WSL 的相同函式使用 FLDT、FADD、FSTPT、FLDT、FSUBP；Mac 使用 FADD d1、STR d1、LDR d31、FSUB d0。記憶體 barrier 使中間值必須存回 long double 的平台表示，沒有把整式常數折疊或消去；Mac D 暫存器的運算為 64-bit floating point。完整 .s 與反組譯均保存在兩端 student 目錄。')
for f in figs:
 row=T[17].add_row().cells;row[0].text=f['caption'].split(' ')[0]+' '+f['caption'].split(' ')[1];row[1].text=f['file']
d.save(p)
m=ROOT/'docs/student_report_evidence.json';data=json.loads(m.read_text(encoding='utf-8'));data['mac_student_run']=mac;data['mac_student_q5']='completed';data['mac_figures']=figs;data['mac_q5_status']='completed_student_run_four_pair_checks_match';
# Remove obsolete pending state if present.
for k in list(data):
 if 'pending' in k and 'mac' in k.lower():data[k]=False
m.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Updated Mac Q0/Q5/Q6/Q7; pictures',len(d.inline_shapes))
