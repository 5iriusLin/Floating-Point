# Q1 actual measured summary

compiler=16.2.0,iterations=5000000,repeats=7,warmup=2,seed=20261004

Source: q1-timing-and-precision.txt

| Operation | Mode | Type | Samples | Median ns/op | Min ns/op | Max ns/op |
|---|---|---|---:|---:|---:|---:|
| add_sub | latency1 | double | 7 | 0.429384 | 0.426806 | 0.442344 |
| add_sub | latency1 | float | 7 | 0.432182 | 0.428256 | 0.454953 |
| add_sub | latency1 | long_double | 7 | 0.64565 | 0.644454 | 0.648011 |
| add_sub | throughput4 | double | 7 | 0.117475 | 0.116476 | 0.132681 |
| add_sub | throughput4 | float | 7 | 0.117829 | 0.11664 | 0.120701 |
| add_sub | throughput4 | long_double | 7 | 0.275822 | 0.268891 | 0.283149 |
| divide | latency1 | double | 7 | 2.99996 | 2.89106 | 3.0411 |
| divide | latency1 | float | 7 | 2.33313 | 2.26979 | 2.36895 |
| divide | latency1 | long_double | 7 | 3.32692 | 3.23662 | 3.43419 |
| divide | throughput4 | double | 7 | 0.828075 | 0.799301 | 0.85876 |
| divide | throughput4 | float | 7 | 0.61773 | 0.606113 | 0.625987 |
| divide | throughput4 | long_double | 7 | 0.923359 | 0.915669 | 0.965714 |
| multiply | latency1 | double | 7 | 0.858836 | 0.854283 | 0.862247 |
| multiply | latency1 | float | 7 | 0.860375 | 0.85848 | 0.863835 |
| multiply | latency1 | long_double | 7 | 0.859048 | 0.856811 | 0.865561 |
| multiply | throughput4 | double | 7 | 0.215547 | 0.21054 | 0.239099 |
| multiply | throughput4 | float | 7 | 0.215455 | 0.213723 | 0.217149 |
| multiply | throughput4 | long_double | 7 | 0.216369 | 0.209509 | 0.219529 |

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
