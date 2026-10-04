#!/usr/bin/env bash
# Q5 only. Never overwrites a previous result directory.
set -euo pipefail
cd "$(dirname "$0")/.."
source scripts/compiler_env.sh
action=${1:-run}
[[ $action == run || $action == build ]] || { echo 'Usage: bash scripts/run_q5.sh [build|run]'; exit 2; }
role=${HW2_RUN_ROLE:-student}
[[ $role == student || $role == assistant ]] || exit 2
platform=$(uname -s | tr '[:upper:]' '[:lower:]')
run_dir=$(mktemp -d "results/q5-${platform}-$(date +%Y%m%d-%H%M%S)-${role}-XXXXXX")
record() {
    local file=$1; shift
    ( printf '$ '; printf '%q ' "$@"; printf '\n'
      set +e; "$@"; rc=$?; printf '\n[exit=%s]\n' "$rc"; exit "$rc"
    ) > "$run_dir/$file" 2>&1
    cat "$run_dir/$file"
}
printf 'executed_by=%s\naction=%s\nCXX=%s\n' "$role" "$action" "$CXX" > "$run_dir/start.txt"
date '+%Y-%m-%dT%H:%M:%S%z' >> "$run_dir/start.txt"
git rev-parse HEAD > "$run_dir/source-commit.txt"
git status --short > "$run_dir/working-tree.txt"
"$CXX" --version > "$run_dir/compiler-full-version.txt"
"$CXX" -dumpfullversion > "$run_dir/q5-compiler-version.txt"
"$CXX" -dumpmachine > "$run_dir/compiler-target.txt"
if ! "$CXX" --version | grep -q 'Free Software Foundation' || [[ $("$CXX" -dumpfullversion) != 16.2.0 ]]; then
    echo "Q5 requires GNU GCC 16.2.0 to match the saved WSL run. See $run_dir"; exit 2
fi
flags=(-std=c++20 -Wall -Wextra -fno-lto -ffp-contract=off -O2 -fno-fast-math -frounding-math)
printf '%s\n' "${flags[*]}" > "$run_dir/q5-flags.txt"
hash_tool=(sha256sum)
[[ $platform != darwin ]] || hash_tool=(shasum -a 256)
find experiments/q5_portability experiments/common -type f \( -name '*.cpp' -o -name '*.hpp' \) -print | LC_ALL=C sort |
while IFS= read -r file; do "${hash_tool[@]}" "$file"; done > "$run_dir/source-sha256.txt"
record compiler-config.txt "$CXX" -v
record environment.txt uname -a
if [[ $platform == darwin ]]; then
    record macos.txt sw_vers
    record hardware.txt sysctl hw.model hw.memsize hw.physicalcpu hw.logicalcpu machdep.cpu.brand_string || true
    record sdk.txt xcrun --show-sdk-path
fi
binary="$run_dir/q5_portability"
record build.txt "$CXX" "${flags[@]}" experiments/q5_portability/main.cpp experiments/q5_portability/operations.cpp -o "$binary"
record assembly-build.txt "$CXX" "${flags[@]}" -S experiments/q5_portability/operations.cpp -o "$run_dir/q5_portability.s"
"${hash_tool[@]}" "$binary" > "$run_dir/q5-binary-sha256.txt"
if [[ $platform == darwin ]]; then
    record linked-libraries.txt otool -L "$binary"
    record q5_portability.disasm.txt otool -tvV "$binary"
else
    record linked-libraries.txt ldd "$binary"
    record q5_portability.disasm.txt objdump -d -C "$binary"
fi
record check.txt "$binary" --check
if [[ $action == run ]]; then
    failures=0
    for mode in nearest upward downward towardzero; do
        record "q5-$mode.txt" env HW2_ROUNDING="$mode" "$binary" || failures=$((failures+1))
    done
    printf 'failed_experiments=%s\n' "$failures" > "$run_dir/completion.txt"
    [[ $failures == 0 ]] || exit 1
fi
echo "Q5 results: $run_dir"
