#include "operations.hpp"
__attribute__((noinline)) double left_grouped(double a,double b,double c) {return (a+b)+c;}
__attribute__((noinline)) double right_grouped(double a,double b,double c) {return a+(b+c);}
__attribute__((noinline)) bool self_inequality(double x) {return x!=x;}
