## script to test integration of exp function
# first add "src" directory to the paths
import sys
sys.path.append('src/')

import numpy as np
import math

# functions
from trapz_int_f1 import *
from exp_x2 import *

a = -10
b = 10
N = 10

Int_value = trapz_int1(fexp_x2,a,b,N)

print("For N = ",N, "points", "Numerical integration is ",
Int_value)
print("Done")
# print(Int_value)

## Since the test is done, we have to check where the integrand
## becomes negligible to determine good estimate of the bounds
## of the integration,
## we can use sympolic integration but here we only apply
## the numerical integration part
## first we plot the integrand:
import matplotlib.pyplot as plt

a = -10
b = 10
N = 100
x = np.linspace(a, b, N)
nx = len(x)
y = []
for i in range (0,nx):
    y.append(fexp_x2(x[i]))

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('exp (x^2)')
plt.show()
# plt.xlim([0,1])
# plt.ylim([0, np.e])

## now let's see what happens for the limits

N=10000
Int_value = trapz_int1(fexp_x2,a,b,N)
I = []
I_lim = []
for i in range (2,1000):
    I_lim.append(i)
    b = i
    a = -b
    int = 0
    int = trapz_int1(fexp_x2,a,b,N)
    I.append(int)

## printing
nI = len(I)
print("    lim_a         lim_b        trapezoidal ")
for i in range(0, nI-1):
    print ('%7d %7d     %.16f' 
    % (-I_lim[i], I_lim[i], I[i]))

## now we can check that the results started to converge
## we can trace that visually or by calculating the 
## difference between the two succssive values. 

# convergence plot
plt.plot(I_lim, I)
plt.xlabel('x [a,b]')
plt.ylabel('∫ exp (x^2) dx')
plt.show()

## from the curve everything is progressive. 
## if we increase the number of points
# conclusion: as much as the interval increases, as 
# much we need more points to converge
# becuase of the way that the trapz. works 

## now let's compute the integral over interval -10 to 10

N = []
Nmin = 2
Nmax = 40
Ig = math.sqrt(math.pi)
a = -10
b = 10
I_list = []
err = []
N_list = []
for N in range(Nmin,Nmax):
    int = 0
    Idiff = 0
    N_list.append(N)
    int = trapz_int1(fexp_x2,a,b,N)
    I_list.append(int)
    Idiff = 100 * abs(int - Ig)/Ig 
    err.append(Idiff) 

## printing
nN = len(N_list)
print("    N        trapezoidal          error %")
for i in range(0, nN):
    print ('%7d %.16f %.16f' 
    % (N_list[i], I_list[i], err[i]))

## the error disappear within 1% of the analytic value
# this is to show the numerical convergence anyway

# convergence plot
import matplotlib.pyplot as plt
plt.plot(N_list, I_list)
plt.xlabel('Number of points')
plt.ylabel('∫_a^b exp (x^2) dx')
plt.show()


## there are may ways to compute and quantify the error 
# error = M^2 * (b-a)^3  / (24 * n^2)  
# whre M is the max. of 2nd derivative of the function f. 