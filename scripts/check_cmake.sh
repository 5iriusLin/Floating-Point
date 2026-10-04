#!/usr/bin/env bash
# Optional build-system validation; does not collect benchmark measurements.
set -euo pipefail
cd "$(dirname "$0")/.."
source scripts/compiler_env.sh
out=${1:-build/cmake-gcc16-check}
cmake -S . -B "$out" -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_COMPILER="$CXX"
cmake --build "$out" -j2
bash scripts/check_build.sh "$out"
