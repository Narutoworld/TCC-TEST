# tcc-test

## CPU Specs:

|Processor Number | i5-5257U |
|---|---|
| Cores  | 2 |
| Threads  | 4 |
| Base Frequency | 2.70GHz |
| Turbo Frequency | 3.10GHz  |
| Cache | 3Mb  |
| TDP  | 28W  |
| Bus Speed | 5 GT/s  |

## Table of Inference Time (Avg of 5 times)

| Condition  | Inference |
|---|---|
| TF Thread=1  | 0.987266 |
| TF Thread=2  | 0.983502  |
| TF Thread=3  | 0.975702  |
| TF Thread=4  | 0.98477  |
| TCC OpenMp | 4.5208 |
| WebAssembly Old Chrome | 5.0366  |
| WebAssembly New Chrome | 34.0354  |
| WebAssembly Old Safari | 32.77124  |
| WebAssembly New Safari | 32.8444  |

## Capabilty of other architecture

### ARM
**Reference**

### RISCV
**Reference**
