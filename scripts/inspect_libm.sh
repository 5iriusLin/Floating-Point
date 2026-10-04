#!/usr/bin/env bash
# Versioned libm symbols cannot always be selected by --disassemble=name.
set -euo pipefail
binary=$1
out=$2
libm=$(ldd "$binary" | awk '/libm\.so/{print $3;exit}')
[[ -r $libm ]] || { echo 'libm not found' >&2; exit 1; }
objdump -T "$libm" | awk '$NF ~ /^(sqrt|sqrtf|sqrtl|__sqrt_finite|__sqrtf_finite|__sqrtl_finite)$/ {print}' > "$out/q2-libm-symbols.txt"
{
    while read -r address size symbol; do
        printf '\nSymbol: %s address=0x%s size=0x%s\n' "$symbol" "$address" "$size"
        objdump -d --start-address="0x$address" --stop-address="$((16#$address+16#$size))" "$libm"
    done < <(awk '{print $1,$5,$NF}' "$out/q2-libm-symbols.txt")
} > "$out/q2-libm-address-ranges.disasm.txt"
sha256sum "$libm" > "$out/q2-libm-sha256.txt"
