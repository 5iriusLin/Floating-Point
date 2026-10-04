#include "operations.hpp"
__attribute__((noinline)) double add_double(double a,double b) {return a+b;}
__attribute__((noinline)) long double increment_long_double(long double a,long double b) {
    long double sum=a+b;
    asm volatile("" : "+m"(sum) : : "memory");
    return sum-a;
}
