# Q1 actual measured summary

compiler=16.2.0,iterations=5000000,repeats=7,warmup=2,seed=20261004

Source: q1-timing-and-precision.txt

| Operation | Mode | Type | Samples | Median ns/op | Min ns/op | Max ns/op |
|---|---|---|---:|---:|---:|---:|
| add_sub | latency1 | double | 7 | 0.400218 | 0.394254 | 0.422413 |
| add_sub | latency1 | float | 7 | 0.405265 | 0.395554 | 0.457201 |
| add_sub | latency1 | long_double | 7 | 0.597353 | 0.592662 | 0.627594 |
| add_sub | throughput4 | double | 7 | 0.116538 | 0.115437 | 0.124235 |
| add_sub | throughput4 | float | 7 | 0.116258 | 0.111189 | 0.127506 |
| add_sub | throughput4 | long_double | 7 | 0.268194 | 0.253914 | 0.273551 |
| divide | latency1 | double | 7 | 3.04234 | 3.00454 | 3.30164 |
| divide | latency1 | float | 7 | 2.38409 | 2.32976 | 2.71429 |
| divide | latency1 | long_double | 7 | 3.44968 | 3.37364 | 3.47626 |
| divide | throughput4 | double | 7 | 0.834115 | 0.819049 | 0.878926 |
| divide | throughput4 | float | 7 | 0.631555 | 0.605646 | 0.65581 |
| divide | throughput4 | long_double | 7 | 0.941836 | 0.909969 | 0.967772 |
| multiply | latency1 | double | 7 | 0.843797 | 0.798877 | 0.867025 |
| multiply | latency1 | float | 7 | 0.824646 | 0.803116 | 0.901947 |
| multiply | latency1 | long_double | 7 | 0.840276 | 0.801072 | 0.867389 |
| multiply | throughput4 | double | 7 | 0.214401 | 0.198212 | 0.219134 |
| multiply | throughput4 | float | 7 | 0.214824 | 0.200563 | 0.218639 |
| multiply | throughput4 | long_double | 7 | 0.211233 | 0.200149 | 0.218466 |

Effective kernel costs include loop/call overhead; these are not isolated instruction latencies.

## Original precision output

```text
accuracy,float,big=2^24,forward,result=0,exact_integer=10000,absolute_error=10000,relative_error=1
accuracy,float,big=2^24,reverse,result=10000,exact_integer=10000,absolute_error=0,relative_error=0
accuracy,double,big=2^24,forward,result=10000,exact_integer=10000,absolute_error=0,relative_error=0
accuracy,double,big=2^24,reverse,result=10000,exact_integer=10000,absolute_error=0,relative_error=0
accuracy,long_double,big=2^24,forward,result=10000,exact_integer=10000,absolute_error=0,relative_error=0
accuracy,long_double,big=2^24,reverse,result=10000,exact_integer=10000,absolute_error=0,relative_error=0
accuracy,float,big=2^53,forward,result=0,exact_integer=10000,absolute_error=10000,relative_error=1
accuracy,float,big=2^53,reverse,result=0,exact_integer=10000,absolute_error=10000,relative_error=1
accuracy,double,big=2^53,forward,result=0,exact_integer=10000,absolute_error=10000,relative_error=1
accuracy,double,big=2^53,reverse,result=10000,exact_integer=10000,absolute_error=0,relative_error=0
accuracy,long_double,big=2^53,forward,result=10000,exact_integer=10000,absolute_error=0,relative_error=0
accuracy,long_double,big=2^53,reverse,result=10000,exact_integer=10000,absolute_error=0,relative_error=0
```
