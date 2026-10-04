"""Validate completed real experiment logs; never supplies missing measurements."""
import argparse
import math
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('run_directory', type=Path)
args = parser.parse_args()
p = args.run_directory

def read(name):
    s = (p / name).read_text(encoding='utf-8')
    assert s.rstrip().endswith('[exit=0]'), f'{name}: batch command did not complete successfully'
    return s

def value(s, key):
    line = next(line for line in s.splitlines() if line.startswith(key+'='))
    return line.split('=',1)[1].split(',',1)[0]

try:
    assert 'failed_experiments=0' in (p/'completion.txt').read_text(), 'incomplete batch'
    names = ['q0-collection.txt','q0-types.txt','q1-timing-and-precision.txt',
             'q2-default.txt','q2-libm.txt','q3-strict.txt','q3-fast.txt',
             'q4-formatting.txt','q6-underflow.txt']
    logs = {name: read(name) for name in names}
    for mode in ['nearest','upward','downward','towardzero']:
        logs['q5-'+mode+'.txt'] = read('q5-'+mode+'.txt')
    q1 = logs['q1-timing-and-precision.txt']
    config = dict(field.split('=',1) for field in next(line for line in q1.splitlines() if line.startswith('compiler=')).split(','))
    samples = [line for line in q1.splitlines() if line.startswith('sample,')]
    assert len(samples) == 18 * int(config['repeats']), 'Q1 missing samples'
    for line in samples:
        fields = dict(field.split('=',1) for field in line.split(',')[4:])
        for key in ['seconds','ns_per_operation','checksum']:
            x = float(fields[key]); assert math.isfinite(x) and x > 0, f'Q1 {key}'
    accuracy = [line for line in q1.splitlines() if line.startswith('accuracy,')]
    assert len(accuracy) == 12, 'Q1 missing accuracy cases'
    for line in accuracy:
        f = dict(field.split('=',1) for field in line.split(',')[4:])
        assert float(f['absolute_error']) == abs(float(f['result'])-10000), 'accuracy error mismatch'
    strict = logs['q3-strict.txt']
    assert value(strict,'finite_control') == '6', 'Q3 finite control'
    assert value(strict,'left_grouped') == '1' and value(strict,'right_grouped') == '0', 'Q3 strict reference'
    for name in ['q2-default.txt','q2-libm.txt']:
        s = logs[name]
        assert s.count('case=exact_square') == 3 and s.count('case=negative_zero') == 3, 'Q2 coverage'
        for block in s.split('case=exact_square')[1:]:
            assert value(block,'sqrt') == '2', 'sqrt(4) reference'
    near = logs['q5-nearest.txt']; up = logs['q5-upward.txt']
    assert 'double_half_ulp_at_one=1,hex=0x1p+0' in near, 'Q5 nearest reference'
    assert 'hex=0x1.0000000000001p+0' in up, 'Q5 upward reference'
    assert logs['q6-underflow.txt'].count('case=') == 9, 'Q6 missing cases'
    print('PASS: completed batch, Q1 sample/accuracy checks, Q2 exact reference, Q3 controls, Q5 directed rounding, Q6 coverage.')
    print('This validates the assistant/student run named in start.txt; it does not certify compiler correctness or replace personal observations.')
except (AssertionError, StopIteration, ValueError, OSError) as e:
    raise SystemExit('VALIDATION FAILED: '+str(e))
