#pragma once
#include <cfenv>
#include <cmath>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <utility>

inline bool help_or_check(int argc, char** argv, const char* usage) {
    if (argc == 2 && std::string(argv[1]) == "--help") {std::cout << usage << '\n'; return true;}
    if (argc == 2 && std::string(argv[1]) == "--check") {
        // Infrastructure only. Never prints or evaluates experiment cases.
        if (std::numeric_limits<double>::radix != 2) throw std::runtime_error("Binary floating point required");
        std::cout << "CHECK PASSED: binary floating-point support; experiment not run.\n"; return true;
    }
    return false;
}
inline double parse_finite(const char* text) {
    char* end=nullptr; double v=std::strtod(text,&end);
    if (end==text || *end!='\0' || !std::isfinite(v)) throw std::runtime_error("Expected a finite numeric input");
    return v;
}
inline void metadata(const char* experiment) {
    std::cout << std::boolalpha << "experiment=" << experiment << "\ncompiler=" << __VERSION__
              << "\nrounding_mode=" << std::fegetround() << "\n";
#ifdef __FAST_MATH__
    std::cout << "fast_math=true\n";
#else
    std::cout << "fast_math=false\n";
#endif
}
template<class T> void value(const char* label, T v) {
    std::cout << label << '=' << std::setprecision(std::numeric_limits<T>::max_digits10)
              << std::defaultfloat << v << ",hex=" << std::hexfloat << v << std::defaultfloat << '\n';
}
