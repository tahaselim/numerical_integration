# In this job, we test the numerican integration using 
# first add "src" directory to the paths
import sys
sys.path.append('src/')
## Gauss quadrature methods
import numpy as np
import math
import matplotlib.pyplot as plt
# functions
from trapz_int_f1 import *
from exp_x2 import *
from hermite_poly import *

# G-Hermite polynomials and quadratures
#G-Hermite quadrature method is used to approximate the integral
# ∫_{-inf}^{inf} exp(-x**2) f(x) dx 
# exp(-x**2) is the weighting factor or the weights
#  
# First let's visualize G-Hermite polynomials:
# at n=1
# first construct a grid for plotting purposes
n = 4
a = -2
b = 2
N = 100
x = np.linspace(a, b, N)
nx = len(x)
y = []
for i in range (0,nx):
    y.append(fhermite(x[i],n))

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('H_{4}')
plt.ylim([-30, 30])
plt.show()
# plt.xlim([0,1])
# plt.ylim([0, np.e])

# Now, let's test the integration of
#  ∫_{-inf}^{inf} exp(-x**2) f(x) dx 
# First let's compute the quadrature points and 
