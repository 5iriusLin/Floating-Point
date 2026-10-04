#include "../common/support.hpp"
#include "operations.hpp"
#include <cstring>

int main(int argc,char** argv) try {
    if(help_or_check(argc,argv,"Usage: q3 [a=1e16 b=-1e16 c=1] | --help | --check")) return 0;
    if(argc!=1 && argc!=4) throw std::runtime_error("Provide either zero or three numeric arguments");
    double a=argc==4 ? parse_finite(argv[1]) : 1e16;
    double b=argc==4 ? parse_finite(argv[2]) : -1e16;
    double c=argc==4 ? parse_finite(argv[3]) : 1.;
    metadata("Q3 fast math");value("a",a);value("b",b);value("c",c);
    value("left_grouped",left_grouped(a,b,c));value("right_grouped",right_grouped(a,b,c));
    // memcpy avoids floating-point parsing of NaN inside the fast-math build.
    static_assert(sizeof(double)==sizeof(std::uint64_t));
    std::uint64_t bits=UINT64_C(0x7ff8000000000001);double nan;
    std::memcpy(&nan,&bits,sizeof nan);
    std::cout<<"nan_input_bits=0x7ff8000000000001\n"
             <<"nan_self_inequality="<<self_inequality(nan)<<'\n';
    value("finite_control",left_grouped(1.,2.,3.));
} catch(const std::exception& e) {std::cerr<<"ERROR: "<<e.what()<<'\n';return 1;}
