#include "kernels.hpp"
#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <vector>

struct Config { std::size_t iterations=5000000, repeats=7, warmup=2; std::uint64_t seed=20261004; };
const char* names[] = {"float", "double", "long_double"};
const char* operations[] = {"add_sub", "multiply", "divide"};
template<class T> T call(const Config& cfg, Operation op, bool throughput, bool warm=false) {
    // Shared exactly representable initial values; no RNG in the timed region.
    T initial = T(1) + T(cfg.seed % 1024) / T(1024);
    T factor = T(1) + T(1)/T(1024);
    return kernel<T>(warm ? std::min<std::size_t>(cfg.iterations,100000) : cfg.iterations,
                     initial,T(1)/T(1024),factor,T(1)/factor,op,throughput);
}
long double dispatch(int type, const Config& cfg, Operation op, bool throughput, bool warm=false) {
    if (type==0) return call<float>(cfg,op,throughput,warm);
    if (type==1) return call<double>(cfg,op,throughput,warm);
    return call<long double>(cfg,op,throughput,warm);
}
template<class T> void accuracy(int type, int exponent) {
    // All inputs and the exact real sum are representable in all three types.
    // The compiler sees ordered scalar sums; neither fast-math nor LTO is allowed.
    constexpr std::size_t blocks=10000;
    T big=std::ldexp(T(1),exponent);
    std::vector<T> input; input.reserve(3*blocks);
    for(std::size_t i=0;i<blocks;++i) {input.push_back(big);input.push_back(T(1));input.push_back(-big);}
    T forward=0, reverse=0;
    for(T value:input) forward+=value;
    for(auto i=input.rbegin();i!=input.rend();++i) reverse+=*i;
    for(auto pair: {std::pair{"forward",forward},std::pair{"reverse",reverse}}) {
        long double result=static_cast<long double>(pair.second);
        long double error=std::fabs(result-static_cast<long double>(blocks));
        std::cout<<"accuracy,"<<names[type]<<",big=2^"<<exponent<<','<<pair.first
                 <<",result="<<result<<",exact_integer="<<blocks
                 <<",absolute_error="<<error<<",relative_error="<<error/blocks<<'\n';
    }
}
int main(int argc,char** argv) try {
    Config cfg; bool check=false, precision_only=false;
    for(int i=1;i<argc;++i) {
        std::string arg=argv[i];
        if(arg=="--help") {
            std::cout<<"Usage: q1_benchmark [--iterations N] [--repeats N] [--warmup N] [--seed N]\n"
                        "       q1_benchmark --precision-only\n       q1_benchmark --check (untimed smoke check)\n"; return 0;
        }
        if(arg=="--check") {check=true;continue;}
        if(arg=="--precision-only") {precision_only=true;continue;}
        if(arg!="--iterations"&&arg!="--repeats"&&arg!="--warmup"&&arg!="--seed") throw std::runtime_error("Unknown option: "+arg);
        if(++i==argc) throw std::runtime_error("Missing option value");
        std::string value=argv[i];
        if(value.empty()||value.find_first_not_of("0123456789")!=std::string::npos) throw std::runtime_error("Expected unsigned integer");
        std::size_t used=0; auto n=std::stoull(value,&used);
        if(arg=="--iterations") {if(n<1||n>100000000) throw std::runtime_error("iterations must be 1..100000000");cfg.iterations=n;}
        if(arg=="--repeats") {if(n<3||n>101) throw std::runtime_error("repeats must be 3..101");cfg.repeats=n;}
        if(arg=="--warmup") {if(n>100) throw std::runtime_error("warmup must be 0..100");cfg.warmup=n;}
        if(arg=="--seed") cfg.seed=n;
    }
    if(check) {
        cfg.iterations=100;
        for(int t=0;t<3;++t) for(int o=0;o<3;++o) for(bool mode:{false,true}) {
            auto result=dispatch(t,cfg,static_cast<Operation>(o),mode);
            if(!std::isfinite(result)||result<=0) throw std::runtime_error("Kernel smoke check failed");
            long double initial=1.L+(cfg.seed%1024)/1024.L;
            long double expected=mode ? 4*initial+1.5L : initial;
            if(std::fabs(result-expected)>0.01L) throw std::runtime_error("Unexpected smoke checksum");
        }
        std::cout<<"CHECK PASSED: 18 kernel paths; no timing collected.\n";return 0;
    }
    std::cout<<std::setprecision(std::numeric_limits<long double>::max_digits10)
             <<"compiler="<<__VERSION__<<",iterations="<<cfg.iterations<<",repeats="<<cfg.repeats
             <<",warmup="<<cfg.warmup<<",seed="<<cfg.seed<<"\n";
    if(!precision_only) {
        using Clock=std::chrono::steady_clock;
        for(int o=0;o<3;++o) for(bool mode:{false,true}) {
            auto op=static_cast<Operation>(o); std::array<std::vector<double>,3> samples;
            for(std::size_t w=0;w<cfg.warmup;++w) for(int t=0;t<3;++t)
                if(!std::isfinite(dispatch(t,cfg,op,mode,true))) throw std::runtime_error("Warmup not finite");
            for(std::size_t r=0;r<cfg.repeats;++r) for(int k=0;k<3;++k) {
                int t=static_cast<int>((r+k)%3); // Rotate type order each round.
                auto start=Clock::now(); auto checksum=dispatch(t,cfg,op,mode); auto stop=Clock::now();
                if(!std::isfinite(checksum)||checksum<=0) throw std::runtime_error("Invalid checksum");
                double seconds=std::chrono::duration<double>(stop-start).count();
                if(seconds<=0) throw std::runtime_error("Timer resolution insufficient");
                samples[t].push_back(seconds);
                double count=static_cast<double>(cfg.iterations)*(mode?8:2);
                std::cout<<"sample,"<<operations[o]<<','<<(mode?"throughput4":"latency1")<<','<<names[t]
                         <<",run="<<r+1<<",seconds="<<seconds<<",ns_per_operation="<<seconds*1e9/count
                         <<",checksum="<<checksum<<'\n';
            }
            for(int t=0;t<3;++t) {
                auto times=samples[t];std::sort(times.begin(),times.end());
                double median=times[times.size()/2];
                if(times.size()%2==0) median=(median+times[times.size()/2-1])/2;
                std::cout<<"summary,"<<operations[o]<<','<<(mode?"throughput4":"latency1")<<','<<names[t]
                         <<",median_seconds="<<median<<",min_seconds="<<times.front()<<",max_seconds="<<times.back()<<'\n';
            }
        }
    }
    for(int exponent:{24,53}) {accuracy<float>(0,exponent);accuracy<double>(1,exponent);accuracy<long double>(2,exponent);}
} catch(const std::exception& e) {std::cerr<<"ERROR: "<<e.what()<<'\n';return 1;}
