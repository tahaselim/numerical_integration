##!/usr/bin/python

import numpy as np
import math

# functions
from trapz_int_f1 import *
from sin_fun import *

N = 10
a = 0
b = math.pi

## fsin for sin(x)
## fsin2 for sin(x)^2

Int_value = trapz_int1(fsin2,a,b,N)

print("For N = ",N, "points", "Numerical integration is ",
Int_value)
print("Done")
# print(Int_value)

## now let see the convergence
N = []
N = [2,4,6,8,10,12,14,16,18,20]
nN = len(N)
a = 0
b = math.pi

I_list = []
err = []
Ig = math.pi/2
for i in range(0,nN-1):
    I1 = 0
    Idiff = 0 
    I1 = trapz_int1(fsin2,a,b,N[i])
    I_list.append(I1)
    Idiff = 100 * abs(I1 - Ig)/Ig 
    err.append(Idiff) 

## printing
print("    i        trapezoidal          error %")
for i in range(0, nN-1):
    print ('%7d %.16f %.16f' % (N[i], I_list[i], err[i]))
3



