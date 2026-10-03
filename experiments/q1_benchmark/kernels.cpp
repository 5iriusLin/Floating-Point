#include "kernels.hpp"

// Separate translation unit; do not enable LTO. The barriers are outside loops.
template<class T>
__attribute__((noinline)) T kernel(std::size_t n, T initial, T step,
                                  T factor, T inverse, Operation op, bool throughput) {
    T a = initial, b = initial + T(0.25), c = initial + T(0.5), d = initial + T(0.75);
    asm volatile("" : "+m"(a), "+m"(b), "+m"(c), "+m"(d) : : "memory");
    // Dispatch outside the measured arithmetic loop.
    if (!throughput) {
        switch (op) {
        case Operation::add:
            for (std::size_t i = 0; i < n; ++i) { a += step; a -= step; }
            break;
        case Operation::multiply:
            for (std::size_t i = 0; i < n; ++i) { a *= factor; a *= inverse; }
            break;
        case Operation::divide:
            for (std::size_t i = 0; i < n; ++i) { a /= factor; a /= inverse; }
            break;
        }
    } else {
        switch (op) {
        case Operation::add:
            for (std::size_t i = 0; i < n; ++i) {
                a += step; b += step; c += step; d += step;
                a -= step; b -= step; c -= step; d -= step;
            }
            break;
        case Operation::multiply:
            for (std::size_t i = 0; i < n; ++i) {
                a *= factor; b *= factor; c *= factor; d *= factor;
                a *= inverse; b *= inverse; c *= inverse; d *= inverse;
            }
            break;
        case Operation::divide:
            for (std::size_t i = 0; i < n; ++i) {
                a /= factor; b /= factor; c /= factor; d /= factor;
                a /= inverse; b /= inverse; c /= inverse; d /= inverse;
            }
            break;
        }
    }
    asm volatile("" : "+m"(a), "+m"(b), "+m"(c), "+m"(d) : : "memory");
    return throughput ? ((a + b) + c) + d : a;
}
template float kernel(std::size_t, float, float, float, float, Operation, bool);
template double kernel(std::size_t, double, double, double, double, Operation, bool);
template long double kernel(std::size_t, long double, long double, long double, long double, Operation, bool);
