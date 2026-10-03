#pragma once
#include <cstddef>

// Each iteration performs two arithmetic operations on each active chain.
enum class Operation { add, multiply, divide };
template<class T> T kernel(std::size_t iterations, T initial, T step,
                           T factor, T inverse, Operation operation, bool throughput);
