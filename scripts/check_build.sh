#!/usr/bin/env bash
# Non-timing infrastructure checks, never used as report experiment evidence.
set -euo pipefail
cd "$(dirname "$0")/.."
source scripts/compiler_env.sh
out=${1:-build/all}
q1="$out/q1-scalar/q1_benchmark"
[[ -x $q1 ]] || q1="$out/q1_benchmark"
"$q1" --check
for program in q2_cmath q2_libm q3_strict q3_fast q4_formatting q5_portability q6_extra; do
    "$out/$program" --check
    "$out/$program" --help
done
