#!/usr/bin/env bash
# Compiles, runs real experiments, and preserves all raw output.
set -euo pipefail
cd "$(dirname "$0")/.."
source scripts/compiler_env.sh
stamp=$(date +%Y%m%d-%H%M%S)
platform=$(uname -s | tr '[:upper:]' '[:lower:]')
role=${HW2_RUN_ROLE:-student}
[[ $role == student || $role == assistant ]] || { echo 'HW2_RUN_ROLE must be student or assistant'; exit 2; }
suffix=""; [[ $role != assistant ]] || suffix="-assistant"
run_dir="results/${platform}-${stamp}${suffix}"
# Refuse overwrite if launched twice in the same second.
mkdir "$run_dir"
build_dir="build/run-${platform}-${stamp}"
export CXX=${CXX:-g++}
failures=0
record() {
    local file=$1; shift
    {
        printf '$ ';printf '%q ' "$@";printf '\n'
        set +e
        "$@"
        rc=$?
        printf '\n[exit=%s]\n' "$rc"
        exit "$rc"
    } 2>&1 | tee "$run_dir/$file"
}
date '+%Y-%m-%dT%H:%M:%S%z' > "$run_dir/start.txt"
printf 'CXX=%s\n' "$CXX" >> "$run_dir/start.txt"
printf 'executed_by=%s\n' "$role" >> "$run_dir/start.txt"
printf 'LD_LIBRARY_PATH=%s\n' "${LD_LIBRARY_PATH:-}" >> "$run_dir/start.txt"
if ! record build.txt bash scripts/build_all.sh "$build_dir"; then
    echo 'Build failed; see build.txt. No experiment was run.'; exit 1
fi
if [[ $platform == darwin ]]; then
    record q0-collection.txt bash experiments/q0_environment/collect_mac.sh "$run_dir/q0"
else
    record q0-collection.txt env CXX="$CXX" bash experiments/q0_environment/collect_linux.sh "$run_dir/q0"
fi
record q0-types.txt "$build_dir/q0_environment"
hash_tool=(sha256sum); [[ $platform != darwin ]] || hash_tool=(shasum -a 256)
find experiments scripts -type f \( -name '*.cpp' -o -name '*.hpp' -o -name '*.sh' \) -print | LC_ALL=C sort |
while IFS= read -r source; do "${hash_tool[@]}" "$source"; done > "$run_dir/source-sha256.txt"
cp "$build_dir/q5-flags.txt" "$build_dir/q5-compiler-version.txt" "$build_dir/compiler-target.txt" "$build_dir/compiler-full-version.txt" "$run_dir/"
cp "$build_dir/"*.s "$build_dir/q1-scalar/kernels.s" "$run_dir/"
iterations=${HW2_ITERATIONS:-5000000}; repeats=${HW2_REPEATS:-7}
record q1-timing-and-precision.txt "$build_dir/q1-scalar/q1_benchmark" --iterations "$iterations" --repeats "$repeats" --warmup 2 --seed 20261004 || failures=$((failures+1))
record q2-default.txt "$build_dir/q2_cmath" 2 || failures=$((failures+1))
record q2-libm.txt "$build_dir/q2_libm" 2 || failures=$((failures+1))
record q3-strict.txt "$build_dir/q3_strict" 1e16 -1e16 1 || failures=$((failures+1))
record q3-fast.txt "$build_dir/q3_fast" 1e16 -1e16 1 || failures=$((failures+1))
diff -u "$run_dir/q3-strict.txt" "$run_dir/q3-fast.txt" > "$run_dir/q3-output.diff" || [[ $? == 1 ]]
if ! "$CXX" --version | grep -qi clang; then
    "$CXX" -Q -O3 -fno-lto -ffp-contract=off -fno-fast-math --help=optimizers > "$run_dir/q3-strict-options.txt"
    "$CXX" -Q -O3 -fno-lto -ffp-contract=off -ffast-math --help=optimizers > "$run_dir/q3-fast-options.txt"
fi
record q4-formatting.txt "$build_dir/q4_formatting" 0.0009765625 || failures=$((failures+1))
for mode in nearest upward downward towardzero; do
    record "q5-$mode.txt" env HW2_ROUNDING="$mode" "$build_dir/q5_portability" || failures=$((failures+1))
done
record q6-underflow.txt "$build_dir/q6_extra" || failures=$((failures+1))
if [[ $platform != darwin ]] && command -v objdump >/dev/null; then
    for name in q2_cmath q2_libm q3_strict q3_fast q5_portability q6_extra; do
        objdump -d -C "$build_dir/$name" > "$run_dir/$name.disasm.txt"
    done
    objdump -d -C "$build_dir/q1-scalar/kernels.o" > "$run_dir/q1-kernels.disasm.txt"
    ldd "$build_dir/q2_libm" > "$run_dir/q2-linked-libraries.txt"
    libm=$(ldd "$build_dir/q2_libm" | awk '/libm\.so/{print $3;exit}')
    if [[ -r $libm ]]; then
        bash scripts/inspect_libm.sh "$build_dir/q2_libm" "$run_dir"
    fi
else
    otool -L "$build_dir/q2_libm" > "$run_dir/q2-linked-libraries.txt" 2>&1 || true
fi
"${hash_tool[@]}" "$build_dir/q5_portability" > "$run_dir/q5-binary-sha256.txt"
printf 'run_dir=%s\nfailed_experiments=%s\n' "$run_dir" "$failures" | tee "$run_dir/completion.txt"
[[ $failures == 0 ]]
