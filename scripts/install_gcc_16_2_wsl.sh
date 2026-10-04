#!/usr/bin/env bash
# User-local native GCC; leaves /usr/bin/g++ and shell settings unchanged.
# Prerequisites (already installed on this machine):
# sudo apt-get install --no-install-recommends libgmp-dev libmpfr-dev libmpc-dev flex bison libzstd-dev
set -euo pipefail
cache="$HOME/.cache/hw2-gcc-16.2.0"
prefix="$HOME/.local/toolchains/gcc-16.2.0"
mkdir -p "$cache" "$HOME/.local/toolchains"
cd "$cache"
if [[ ! -f gcc-16.2.0.tar.xz ]]; then
    curl -fL --retry 2 -o gcc-16.2.0.tar.xz https://gcc.gnu.org/pub/gcc/releases/gcc-16.2.0/gcc-16.2.0.tar.xz
fi
expected=c51c30ca7422d0cbecf504b2e0f33c3aca31e0f90a76b65217f465163fa6fa17b3f5de39e145c47e5bab90ac0ce7fff3b03c8d553ae36e01faaea5a50f8648d1
printf '%s  gcc-16.2.0.tar.xz\n' "$expected" | sha512sum -c -
[[ -d gcc-16.2.0 ]] || tar -xf gcc-16.2.0.tar.xz
mkdir -p native-build
cd native-build
if [[ ! -f Makefile ]]; then
    ../gcc-16.2.0/configure --prefix="$prefix" --enable-languages=c,c++ \
      --disable-multilib --disable-bootstrap --disable-libsanitizer \
      --without-isl --enable-checking=release --with-pkgversion='HW2 local GCC 16.2.0' \
      > configure.log 2>&1
fi
# Bound parallelism because WSL sees about 15 GiB RAM.
make -j"${HW2_BUILD_JOBS:-4}" > build.log 2>&1
make install > install.log 2>&1
"$prefix/bin/g++" --version
[[ $("$prefix/bin/g++" -dumpfullversion) == 16.2.0 ]]
printf 'Installed: %s\nLogs: %s/native-build/\n' "$prefix" "$cache"
