#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
source scripts/compiler_env.sh
mkdir -p results/toolchain-gcc16.2
{
    date -Is
    printf 'CXX=%s\nLD_LIBRARY_PATH=%s\n' "$CXX" "${LD_LIBRARY_PATH:-}"
    "$CXX" --version
    "$CXX" -dumpfullversion
    "$CXX" -dumpmachine
    "$CXX" -print-file-name=libstdc++.so
    printf 'Original system GCC: '
    /usr/bin/g++ -dumpfullversion
} > results/toolchain-gcc16.2/compiler.txt
