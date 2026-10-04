#!/usr/bin/env bash
# Source this file from project scripts. It changes only the current process.
# Explicit CXX always wins; no shell profile or system symlink is changed.
if [[ -z ${CXX:-} ]]; then
    if [[ $(uname -s) == Linux && -x "$HOME/.local/toolchains/gcc-16.2.0/bin/g++" ]]; then
        export CXX="$HOME/.local/toolchains/gcc-16.2.0/bin/g++"
    elif command -v g++-16 >/dev/null 2>&1; then
        export CXX=$(command -v g++-16)
    else
        export CXX=g++
    fi
fi
# Select the local toolchain's own runtime, without changing link flags used
# for Q5 or altering system libraries. Actual dependencies are logged by ldd.
if [[ $(uname -s) == Linux && $CXX == "$HOME/.local/toolchains/gcc-16.2.0/bin/g++" ]]; then
    export LD_LIBRARY_PATH="$HOME/.local/toolchains/gcc-16.2.0/lib64${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
fi
