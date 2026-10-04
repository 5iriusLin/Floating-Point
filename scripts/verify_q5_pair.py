"""Check necessary Q5 cross-platform conditions; no experiments executed."""
import argparse
from pathlib import Path

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('first',type=Path);parser.add_argument('second',type=Path)
args=parser.parse_args()
def read(p,name):return (p/name).read_text(encoding='utf-8').strip()
def family(p):
    s=read(p,'compiler-full-version.txt').lower()
    if 'clang' in s:return 'clang'
    if 'free software foundation' in s:return 'gcc'
    return s.splitlines()[0]
def source_map(p):
    result={}
    for line in read(p,'source-sha256.txt').splitlines():
        digest,name=line.split(maxsplit=1);result[name.lstrip('*')]=digest
    return {k:v for k,v in result.items() if k.startswith(('experiments/q5_portability/','experiments/common/'))}
conditions={
    'compiler_family':family(args.first)==family(args.second),
    'compiler_version':read(args.first,'q5-compiler-version.txt')==read(args.second,'q5-compiler-version.txt'),
    'flags':read(args.first,'q5-flags.txt')==read(args.second,'q5-flags.txt'),
    'q5_and_common_source':bool(source_map(args.first)) and source_map(args.first)==source_map(args.second),
}
for name,passed in conditions.items():print(name+': '+('MATCH' if passed else 'MISMATCH'))
print('Targets: '+read(args.first,'compiler-target.txt')+' / '+read(args.second,'compiler-target.txt'))
print('Necessary checks only. Inspect vendor patches, ABI, outputs, and validity before claiming Q5 completion.')
raise SystemExit(0 if all(conditions.values()) else 1)
