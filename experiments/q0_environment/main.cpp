#include <cfenv>
#include <cfloat>
#include <iostream>
#include <limits>

template<class T> void describe(const char* name) {
    using L = std::numeric_limits<T>;
    std::cout << name << ": bytes=" << sizeof(T) << " alignment=" << alignof(T)
              << " radix=" << L::radix << " digits=" << L::digits
              << " digits10=" << L::digits10 << " max_digits10=" << L::max_digits10
              << " min_exponent=" << L::min_exponent << " max_exponent=" << L::max_exponent
              << " is_iec559=" << L::is_iec559 << " has_denorm=" << L::has_denorm
              << " epsilon=" << std::hexfloat << L::epsilon()
              << " min_normal=" << L::min() << " denorm_min=" << L::denorm_min()
              << " max=" << L::max() << std::defaultfloat << '\n';
}

int main() {
    std::cout << std::boolalpha << "compiler=" << __VERSION__
              << "\n__cplusplus=" << __cplusplus << "\npointer_bytes=" << sizeof(void*)
              << "\nFLT_EVAL_METHOD=" << FLT_EVAL_METHOD
              << "\nrounding_mode=" << std::fegetround() << " FE_TONEAREST=" << FE_TONEAREST << '\n';
#ifdef __FAST_MATH__
    std::cout << "fast_math=true\n";
#else
    std::cout << "fast_math=false\n";
#endif
    describe<float>("float"); describe<double>("double"); describe<long double>("long double");
#ifdef __SIZEOF_FLOAT128__
    std::cout << "compiler_float128_bytes=" << __SIZEOF_FLOAT128__
              << " (extension only; libquadmath not tested)\n";
#endif
}
