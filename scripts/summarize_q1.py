"""Summarize actual Q1 logs; never generates benchmark values without data."""
import argparse
import csv
import math
import statistics
from collections import defaultdict
from pathlib import Path

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('run_directory',type=Path)
args=parser.parse_args()
p=args.run_directory
text=(p/'q1-timing-and-precision.txt').read_text(encoding='utf-8')
if '[exit=0]' not in text or '[exit=1]' in text:raise SystemExit('Missing successful original execution; no summary written.')
groups=defaultdict(list)
for line in text.splitlines():
    fields=line.split(',')
    if fields[0]!='sample':continue
    if len(fields)<8:raise SystemExit('Malformed sample')
    data=dict(item.split('=',1) for item in fields[4:])
    seconds=float(data['seconds']);ns=float(data['ns_per_operation'])
    if not math.isfinite(seconds) or seconds<=0 or not math.isfinite(ns) or ns<=0:
        raise SystemExit('Invalid timing sample; no summary written.')
    groups[tuple(fields[1:4])].append((int(data['run']),seconds,ns))
if len(groups)!=18:raise SystemExit(f'Expected 18 kernel/type/mode groups, found {len(groups)}; no summary written.')
metadata=next((line for line in text.splitlines() if line.startswith('compiler=')),None)
if metadata is None:raise SystemExit('Missing configuration')
expected=int(dict(item.split('=',1) for item in metadata.split(','))['repeats'])
rows=[]
for key,samples in sorted(groups.items()):
    if sorted(s[0] for s in samples)!=list(range(1,expected+1)):raise SystemExit('Missing or duplicate rounds')
    seconds=[s[1] for s in samples];ns=[s[2] for s in samples]
    rows.append((*key,len(samples),statistics.median(seconds),statistics.median(ns),min(ns),max(ns)))
headers=['operation','mode','type','samples','median_seconds','median_ns_per_operation','min_ns_per_operation','max_ns_per_operation']
with (p/'q1-summary.csv').open('w',encoding='utf-8',newline='') as f:
    writer=csv.writer(f);writer.writerow(headers);writer.writerows(rows)
lines=['# Q1 actual measured summary','',metadata,'','Source: q1-timing-and-precision.txt','',
       '| Operation | Mode | Type | Samples | Median ns/op | Min ns/op | Max ns/op |',
       '|---|---|---|---:|---:|---:|---:|']
for op,mode,typ,count,sec,med,lo,hi in rows:lines.append(f'| {op} | {mode} | {typ} | {count} | {med:.6g} | {lo:.6g} | {hi:.6g} |')
lines+=['','Effective kernel costs include loop/call overhead; these are not isolated instruction latencies.','',
        '## Original precision output','', '```text']
lines.extend(line for line in text.splitlines() if line.startswith('accuracy,'));lines.append('```')
(p/'q1-summary.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('Created q1-summary.csv and q1-summary.md from original samples.')
