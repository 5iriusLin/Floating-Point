#include "../common/support.hpp"
#include "sqrt_paths.hpp"
#include <cerrno>
#include <type_traits>

static_assert(std::is_same_v<decltype(std::sqrt(1.f)),float>);
static_assert(std::is_same_v<decltype(std::sqrt(1.)),double>);
static_assert(std::is_same_v<decltype(std::sqrt(1.L)),long double>);
static_assert(std::is_same_v<decltype(std::sqrt(1)),double>);

template<class T> void test(const char* name, const char* input_name,T x) {
    if(std::feclearexcept(FE_ALL_EXCEPT)!=0) throw std::runtime_error("Cannot clear FP exceptions");
    errno=0;
    T y=sqrt_path(x);
    int saved_errno=errno, flags=std::fetestexcept(FE_ALL_EXCEPT);
    std::cout << "type="<<name<<",case="<<input_name<<"\n";
    value("input",x); value("sqrt",y);
    std::cout<<"errno="<<saved_errno<<",EDOM="<<EDOM
             <<",FE_INVALID="<<bool(flags&FE_INVALID)<<",FE_INEXACT="<<bool(flags&FE_INEXACT)
             <<",negative_sign="<<std::signbit(y)<<",isnan="<<std::isnan(y)<<'\n';
}
template<class T> void cases(const char* name, double runtime_input) {
    test(name,"runtime",T(runtime_input));
    test(name,"positive_zero",T(0));test(name,"negative_zero",-T(0));
    test(name,"exact_square",T(4));test(name,"irrational_root",T(2));
    test(name,"negative",T(-1));
    test(name,"min_normal",std::numeric_limits<T>::min());
    test(name,"min_subnormal",std::numeric_limits<T>::denorm_min());
    test(name,"infinity",std::numeric_limits<T>::infinity());
    test(name,"quiet_nan",std::numeric_limits<T>::quiet_NaN());
}
int main(int argc,char** argv) try {
    if(help_or_check(argc,argv,"Usage: q2_cmath [finite_input=2] | --help | --check")) return 0;
    if(argc>2) throw std::runtime_error("Too many arguments");
    double x=argc==2 ? parse_finite(argv[1]) : 2.;
    metadata("Q2 sqrt");
#ifdef HW2_FORCE_LIBM
    std::cout<<"path=forced_libm_symbol\n";
#else
    std::cout<<"path=std_sqrt_default\n";
#endif
    std::cout<<"math_errhandling="<<math_errhandling
      <<",MATH_ERRNO="<<MATH_ERRNO<<",MATH_ERREXCEPT="<<MATH_ERREXCEPT<<'\n';
    cases<float>("float",x);cases<double>("double",x);cases<long double>("long_double",x);
} catch(const std::exception& e) {std::cerr<<"ERROR: "<<e.what()<<'\n';return 1;}
