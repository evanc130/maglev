# Last edited by Hannah 4/30
# testing out multiplication of transfer functions together

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import sympy as sy
from IPython.display import display

sy.init_printing()
pG, pC, pGC, pIGC = sy.symbols("G, C, CG, IGC") # for pretty display

# ---------------------- Functions --------------------------
def lti_to_sympy(lsys, symplify=True):
    """Convert Scipy's LTI instance to Sympy expression """
    s = sy.Symbol('s')
    G = sy.Poly(lsys.num, s) / sy.Poly(lsys.den, s)
    return sy.simplify(G) if symplify else G


def sympy_to_lti(xpr, s=sy.Symbol('s')):
    """Convert Sumpy transfer function polynomial to Scipy LTI """
    num, den = sy.simplify(xpr).as_numer_denom() # expressions
    p_num_den = sy.poly(num, s), sy.poly(den, s) # polynomials
    c_num_den = [sy.expand(p).all_coeffs() for p in p_num_den] # coefficients
    l_num, l_den = [sy.lambdift((), c)() for c in c_num_den] #convert to floats
    return signal.lti(l_num, l_den)

# ------------------- An example ---------------------------

# set up transfer functions
lti_G = signal.lti([1], [1, 2])
lti_C = signal.lti([2], [1, 0, 3])

# convert to sympy
Gs, Cs = lti_to_sympy(lti_G), lti_to_sympy(lti_C)

print("Converted LTI expressions:")
display(sy.Eq(pG, Gs))
display(sy.Eq(pC, Cs))

GCs = sy.simplify(Gs*Cs).expand()
display(sy.Eq(pGC, GCs))

IGCs = sy.simplify(GCs/(1+GCs)).expand()
display(sy.Eq(pIGC, IGCs))



# # -------------------- Initiate Variables --------------------------
# g = 9.8                                 #[m/s^2]
# gamma = 1                             #[who knows?]
# v_bar = 6                               #[V]
# r_bar = -np.sqrt((gamma*v_bar**2)/g)     #[length]
# print('r_bar = ',r_bar)
# #R_hat_0 = [-1, -0.5, -0.25, -0.1, -0.05, 0.05, 0.1, 0.25, 0.4, 0.5, 1, 2]
# R_hat_0 = 1
# print('R_hat_0 = ',R_hat_0)
# t = np.arange(0.0,1.0,0.01)
# step = 0*np.heaviside(t,1)
#
# name = 'Test'
# num = 2*gamma*v_bar/(r_bar**2)
# p1 = 2*gamma*v_bar**2/r_bar**3
# den = [1, 0, p1]
# G = signal.TransferFunction(num,den)
# z,p,k = signal.tf2zpk(num,den)
# #print(G)
#
# # Creating Controller Transfer Function C####################################
# Kd = 1;
# Kp = 1;
# Ki = 1;
# C = signal.TransferFunction([Kd, Kp, Ki],1)
# #print(C)
# plt.figure(1)
# #for i in R_hat_0:
# CG = C*G
# tout,y,x = signal.lsim(CG, step, t, R_hat_0)
# print(y)
# plt.plot(t,y)
# #plt.legend(loc='best')
# plt.show()
