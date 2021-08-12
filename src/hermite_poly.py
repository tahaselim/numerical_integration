# function to evaluate Hermite polynomials using
# the recursion relation 
# H_{n+1}(x) = 2xH_{n}(x) - 2nH_{n-1}(x)
# another formalism
# H_{n}(x) = 2xH_{n-1}(x) - 2(n-1)H_{n-1}(x) 
# Taha Selim

import numpy as np
def fhermite(x,n):
    Hpoly = [] # prepare the list of Hermite polynomials 
    H_0 = 1
    H_1 = 2*x
    if n == 0:
        Hpoly = H_0
    elif n == 1:
        Hpoly = H_1

    if n > 1 :
        H0 = H_0
        H1 = H_1 
        # Hpoly.insert(0,H_0)
        for i_n in range(2,n+1) :
            # recursion relation
            H2 = 2*x*H1 - 2*(i_n-1)*H0
            H0 = H1
            H1 = H2
    return H2