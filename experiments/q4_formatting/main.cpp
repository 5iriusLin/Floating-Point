#include "../common/support.hpp"
#include <cstdio>
#include <locale>
#include <sstream>

void show(const char* name,double x) {
    char printf_text[128];std::snprintf(printf_text,sizeof printf_text,"%.9f",x);
    std::ostringstream stream;stream.imbue(std::locale::classic());
    stream<<std::fixed<<std::setprecision(9)<<x;
    std::cout<<"case="<<name<<'\n';value("stored",x);
    std::cout<<"printf_9="<<printf_text<<",iostream_9="<<stream.str()<<'\n';
}
int main(int argc,char** argv) try {
    if(help_or_check(argc,argv,"Usage: q4_formatting [decimal_input=0.0009765625] | --help | --check")) return 0;
    if(argc>2) throw std::runtime_error("Too many arguments");
    double input=argc==2 ? parse_finite(argv[1]) : 1./1024.;
    metadata("Q4 formatting");
    const int saved=std::fegetround();
    if(std::fesetround(FE_TONEAREST)!=0) throw std::runtime_error("FE_TONEAREST unavailable");
    std::cout<<"exact_tie=1/1024=0.0009765625; tie is between 0.000976562 and 0.000976563\n";
    show("runtime_decimal",input);
    double tie=std::ldexp(1.,-10);
    for(auto mode:{std::pair{"nearest",FE_TONEAREST},std::pair{"upward",FE_UPWARD},
                   std::pair{"downward",FE_DOWNWARD},std::pair{"towardzero",FE_TOWARDZERO}}) {
        if(std::fesetround(mode.second)!=0) {std::cout<<"mode="<<mode.first<<",unsupported\n";continue;}
        std::cout<<"mode="<<mode.first<<",fegetround="<<std::fegetround()<<'\n';
        show("exact_positive_tie",tie);show("exact_negative_tie",-tie);
        show("below_positive_tie",std::nextafter(tie,0.));
        show("above_positive_tie",std::nextafter(tie,1.));
    }
    if(std::fesetround(saved)!=0) throw std::runtime_error("Cannot restore rounding mode");
} catch(const std::exception& e) {std::cerr<<"ERROR: "<<e.what()<<'\n';return 1;}
