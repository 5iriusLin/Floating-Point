#!/usr/bin/env bash
# Build only. No benchmark or experiment outputs are collected here.
set -euo pipefail
cd "$(dirname "$0")/.."
source scripts/compiler_env.sh
compiler=${CXX:-g++}
out=${1:-build/all}
mkdir -p "$out"
common=(-std=c++20 -Wall -Wextra -fno-lto -ffp-contract=off)
strict=(-O2 -fno-fast-math -frounding-math)
printf 'compiler: %s\n' "$compiler"; "$compiler" --version
build() {
    local name=$1; shift
    printf '\nBUILD %s\n' "$name"
    printf '%q ' "$compiler" "${common[@]}" "$@" -o "$out/$name"; printf '\n'
    "$compiler" "${common[@]}" "$@" -o "$out/$name"
}
build q0_environment "${strict[@]}" experiments/q0_environment/main.cpp
bash experiments/q1_benchmark/build.sh "$out/q1-scalar"
build q2_cmath "${strict[@]}" experiments/q2_cmath/main.cpp experiments/q2_cmath/sqrt_paths.cpp
build q2_libm "${strict[@]}" -DHW2_FORCE_LIBM=1 experiments/q2_cmath/main.cpp experiments/q2_cmath/sqrt_paths.cpp
build q3_strict -O3 -fno-fast-math experiments/q3_fast_math/main.cpp experiments/q3_fast_math/operations.cpp
build q3_fast -O3 -ffast-math experiments/q3_fast_math/main.cpp experiments/q3_fast_math/operations.cpp
build q4_formatting "${strict[@]}" experiments/q4_formatting/main.cpp
build q5_portability "${strict[@]}" experiments/q5_portability/main.cpp experiments/q5_portability/operations.cpp
build q6_extra "${strict[@]}" experiments/q6_extra/main.cpp experiments/q6_extra/operations.cpp
printf '%s\n' "${common[*]} ${strict[*]}" > "$out/q5-flags.txt"
if "$compiler" --version | grep -qi clang; then
    "$compiler" --version | head -n 1 > "$out/q5-compiler-version.txt"
else
    "$compiler" -dumpfullversion > "$out/q5-compiler-version.txt"
fi
"$compiler" --version > "$out/compiler-full-version.txt"
"$compiler" -dumpmachine > "$out/compiler-target.txt"
for variant in default libm; do
    extras=(); [[ $variant != libm ]] || extras=(-DHW2_FORCE_LIBM=1)
    "$compiler" "${common[@]}" "${strict[@]}" "${extras[@]}" -S experiments/q2_cmath/sqrt_paths.cpp -o "$out/q2-$variant.s"
done
for mode in strict fast; do
    mathflag=-fno-fast-math; [[ $mode != fast ]] || mathflag=-ffast-math
    "$compiler" "${common[@]}" -O3 "$mathflag" -S experiments/q3_fast_math/operations.cpp -o "$out/q3-$mode.s"
done
for q in q5_portability q6_extra; do
    "$compiler" "${common[@]}" "${strict[@]}" -S "experiments/$q/operations.cpp" -o "$out/$q.s"
done
printf '\nAll programs built. No formal experiments run.\n'
