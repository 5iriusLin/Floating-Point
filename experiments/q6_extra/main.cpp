#include "../common/support.hpp"
#include "operations.hpp"
#if defined(__SSE__)
#include <xmmintrin.h>
#endif
const char* classify(int c) {
    switch(c) {case FP_NORMAL:return "normal";case FP_SUBNORMAL:return "subnormal";
    case FP_ZERO:return "zero";case FP_INFINITE:return "infinite";default:return "nan";}
}
template<class T> void test(const char* type,const char* name,T x,T factor) {
    if(std::feclearexcept(FE_ALL_EXCEPT)!=0) throw std::runtime_error("Cannot clear exceptions");
    T y=multiply_runtime(x,factor);int flags=std::fetestexcept(FE_ALL_EXCEPT);
    std::cout<<"type="<<type<<",case="<<name<<'\n';value("input",x);value("factor",factor);value("result",y);
    std::cout<<"input_class="<<classify(std::fpclassify(x))<<",result_class="<<classify(std::fpclassify(y))
      <<",FE_UNDERFLOW="<<bool(flags&FE_UNDERFLOW)<<",FE_INEXACT="<<bool(flags&FE_INEXACT)<<'\n';
}
template<class T> void cases(const char* name) {
    test(name,"exact_subnormal",std::numeric_limits<T>::min(),T(0.5));
    test(name,"tiny_inexact",std::numeric_limits<T>::denorm_min(),T(0.5));
    test(name,"subnormal_preserved",std::numeric_limits<T>::denorm_min(),T(1));
}
int main(int argc,char** argv) try {
    if(help_or_check(argc,argv,"Usage: q6_extra | --help | --check")) return 0;
    if(argc!=1) throw std::runtime_error("Unexpected argument");
    if(std::fesetround(FE_TONEAREST)!=0) throw std::runtime_error("Nearest rounding unavailable");
    metadata("Q6 gradual underflow");
#if defined(__SSE__)
    auto mxcsr=_mm_getcsr();std::cout<<"MXCSR=0x"<<std::hex<<mxcsr<<std::dec
      <<",FTZ="<<bool(mxcsr&(1u<<15))<<",DAZ="<<bool(mxcsr&(1u<<6))<<'\n';
#else
    std::cout<<"MXCSR not applicable; no architecture-specific mode changed.\n";
#endif
    cases<float>("float");cases<double>("double");cases<long double>("long_double");
} catch(const std::exception& e) {std::cerr<<"ERROR: "<<e.what()<<'\n';return 1;}
