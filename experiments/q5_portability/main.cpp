#include "../common/support.hpp"
#include "operations.hpp"

int main(int argc,char** argv) try {
    if(help_or_check(argc,argv,"Usage: q5_portability | --help | --check; HW2_ROUNDING=nearest/upward/downward/towardzero")) return 0;
    if(argc!=1) throw std::runtime_error("Unexpected argument");
    const char* env=std::getenv("HW2_ROUNDING");std::string mode=env?env:"nearest";
    int rounding=FE_TONEAREST;
    if(mode=="upward") rounding=FE_UPWARD;
    else if(mode=="downward") rounding=FE_DOWNWARD;
    else if(mode=="towardzero") rounding=FE_TOWARDZERO;
    else if(mode!="nearest") throw std::runtime_error("Invalid HW2_ROUNDING");
    if(std::fesetround(rounding)!=0) throw std::runtime_error("Requested rounding mode unavailable");
    metadata("Q5 execution environment");std::cout<<"HW2_ROUNDING="<<mode
      <<"\nlong_double_bytes="<<sizeof(long double)<<",digits="<<std::numeric_limits<long double>::digits
      <<",max_exponent="<<std::numeric_limits<long double>::max_exponent<<'\n';
    value("double_half_ulp_at_one",add_double(1.,std::ldexp(1.,-53)));
    if(std::fesetround(FE_TONEAREST)!=0) throw std::runtime_error("Cannot select nearest for ABI case");
    std::cout<<"abi_case_rounding=FE_TONEAREST\n";
    value("long_double_big",std::ldexp(1.L,53));
    value("long_double_increment",increment_long_double(std::ldexp(1.L,53),1.L));
} catch(const std::exception& e) {std::cerr<<"ERROR: "<<e.what()<<'\n';return 1;}
