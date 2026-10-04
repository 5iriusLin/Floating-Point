# Q1 actual measured summary

compiler=16.2.0,iterations=5000000,repeats=7,warmup=2,seed=20261004

Source: q1-timing-and-precision.txt

| Operation | Mode | Type | Samples | Median ns/op | Min ns/op | Max ns/op |
|---|---|---|---:|---:|---:|---:|
| add_sub | latency1 | double | 7 | 0.428799 | 0.409473 | 0.430715 |
| add_sub | latency1 | float | 7 | 0.428827 | 0.408541 | 0.43625 |
| add_sub | latency1 | long_double | 7 | 0.628838 | 0.609816 | 0.652821 |
| add_sub | throughput4 | double | 7 | 0.110696 | 0.107785 | 0.118559 |
| add_sub | throughput4 | float | 7 | 0.108452 | 0.107661 | 0.11732 |
| add_sub | throughput4 | long_double | 7 | 0.249418 | 0.247006 | 0.260839 |
| divide | latency1 | double | 7 | 3.02516 | 2.94283 | 3.18598 |
| divide | latency1 | float | 7 | 2.37823 | 2.25131 | 2.52789 |
| divide | latency1 | long_double | 7 | 3.43707 | 3.21657 | 3.8677 |
| divide | throughput4 | double | 7 | 0.853958 | 0.815605 | 0.864675 |
| divide | throughput4 | float | 7 | 0.644156 | 0.635677 | 0.645814 |
| divide | throughput4 | long_double | 7 | 0.96528 | 0.925646 | 0.975581 |
| multiply | latency1 | double | 7 | 0.838062 | 0.820982 | 0.863882 |
| multiply | latency1 | float | 7 | 0.826191 | 0.818062 | 0.855615 |
| multiply | latency1 | long_double | 7 | 0.827093 | 0.804691 | 0.865503 |
| multiply | throughput4 | double | 7 | 0.215398 | 0.20425 | 0.217701 |
| multiply | throughput4 | float | 7 | 0.209012 | 0.201639 | 0.216248 |
| multiply | throughput4 | long_double | 7 | 0.215604 | 0.202152 | 0.235 |

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
