#include <cmath>
#include "sqrt_paths.hpp"
// Volatile function pointers force actual libm symbol calls in the comparison.
#ifdef HW2_FORCE_LIBM
__attribute__((noinline)) float sqrt_path(float x) {float (*volatile f)(float)=&::sqrtf;return f(x);}
__attribute__((noinline)) double sqrt_path(double x) {double (*volatile f)(double)=&::sqrt;return f(x);}
__attribute__((noinline)) long double sqrt_path(long double x) {long double (*volatile f)(long double)=&::sqrtl;return f(x);}
#else
__attribute__((noinline)) float sqrt_path(float x) {return std::sqrt(x);}
__attribute__((noinline)) double sqrt_path(double x) {return std::sqrt(x);}
__attribute__((noinline)) long double sqrt_path(long double x) {return std::sqrt(x);}
#endif
