#!/usr/bin/env bash
# GCC/Clang toolchain, run from the project root. Does not run benchmarks.
set -euo pipefail
source scripts/compiler_env.sh
compiler=${CXX:-g++}
out=${1:-build/q1-scalar}
mkdir -p "$out"
flags=(-std=c++20 -O3 -Wall -Wextra -fno-fast-math -ffp-contract=off -fno-lto)
if "$compiler" --version | grep -qi clang; then
    flags+=(-fno-vectorize -fno-slp-vectorize)
else
    flags+=(-fno-tree-vectorize)
fi
printf 'compiler: %s\n' "$compiler"
"$compiler" --version
printf 'flags:'; printf ' %q' "${flags[@]}"; printf '\n'
"$compiler" "${flags[@]}" -c experiments/q1_benchmark/main.cpp -o "$out/main.o"
"$compiler" "${flags[@]}" -c experiments/q1_benchmark/kernels.cpp -o "$out/kernels.o"
"$compiler" "${flags[@]}" "$out/main.o" "$out/kernels.o" -o "$out/q1_benchmark"
"$compiler" "${flags[@]}" -S experiments/q1_benchmark/kernels.cpp -o "$out/kernels.s"
printf 'Built %s/q1_benchmark and kernels.s; no benchmark run.\n' "$out"
