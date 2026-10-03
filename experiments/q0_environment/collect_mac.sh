#!/usr/bin/env bash
# Run on the actual Mac, from the project root. No Mac results are included.
set -u
out=${1:-results/q0-mac}
mkdir -p "$out"
exec > >(tee "$out/environment.txt") 2>&1
run() { printf '\n$'; printf ' %q' "$@"; printf '\n'; "$@"; local status=$?; printf '[exit=%s]\n' "$status"; }
run date
run sw_vers
run uname -a
run sysctl hw.model hw.memsize hw.physicalcpu hw.logicalcpu machdep.cpu.brand_string
run pmset -g custom
run pmset -g batt
run xcode-select -p
run clang++ --version
run g++ --version
run sh -c 'command -v clang++; command -v g++; command -v cmake'
run shasum -a 256 experiments/q0_environment/main.cpp
# CXX can select a specific installed compiler; this does not install tools.
compiler=${CXX:-clang++}
run "$compiler" -std=c++20 -O2 -fno-fast-math -ffp-contract=off experiments/q0_environment/main.cpp -o "$out/q0_environment"
if test -x "$out/q0_environment"; then
    run "$out/q0_environment"
    run otool -L "$out/q0_environment"
fi
