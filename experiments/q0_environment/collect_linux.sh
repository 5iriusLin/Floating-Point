#!/usr/bin/env bash
# Execute from repository root; optional first argument is output directory.
set -u
out=${1:-results/q0-wsl}
mkdir -p "$out"
exec > >(tee "$out/environment.txt") 2>&1
run() { printf '\n$'; printf ' %q' "$@"; printf '\n'; "$@"; local status=$?; printf '[exit=%s]\n' "$status"; }
run date --iso-8601=seconds
run uname -a
run cat /etc/os-release
run lscpu
run free -h
run cat /proc/meminfo
run taskset -pc $$
run findmnt -T .
run g++ --version
run g++ -v
run g++ -dumpmachine
run g++ -print-file-name=libstdc++.so
run ldd --version
run cmake --version
run dpkg-query -W gcc g++ libc6 libstdc++6 libquadmath0
run sh -c 'command -v g++; command -v cmake; command -v make; command -v ninja'
run sh -c 'for f in /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor /sys/devices/system/cpu/cpu0/cpufreq/scaling_driver; do if test -r "$f"; then printf "%s: " "$f"; cat "$f"; else printf "%s: unavailable\n" "$f"; fi; done'
run g++ -Q -O2 -fno-fast-math -ffp-contract=off --help=target
run sha256sum experiments/q0_environment/main.cpp
run g++ -std=c++20 -O2 -fno-fast-math -ffp-contract=off experiments/q0_environment/main.cpp -o "$out/q0_environment"
if test -x "$out/q0_environment"; then
    run "$out/q0_environment"
    run ldd "$out/q0_environment"
    run sha256sum "$out/q0_environment"
fi
