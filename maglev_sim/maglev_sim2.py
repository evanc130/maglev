import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import sympy as sy

# ---------------  Functions ---------------------
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
    l_num, l_den = [sy.lambdify((), c)() for c in c_num_den] #convert to floats
    return signal.lti(l_num, l_den)


# ------------ Initiate variables  -------------------
g = 9.8                                 #[m/s^2]
gamma = 1                             #[who knows?]
v_bar = 6                               #[V]
r_bar = -np.sqrt((gamma*v_bar**2)/g)     #[length]
print('r_bar = ',r_bar)
#R_hat_0 = [-1, -0.5, -0.25, -0.1, -0.05, 0.05, 0.1, 0.25, 0.4, 0.5, 1, 2]
R_hat_0 = 1
print('R_hat_0 = ',R_hat_0)
t = np.arange(0.0,1.0,0.01)
step = 0*np.heaviside(t,1)


# ---------------- Initiate Plant ------------------
name = 'Test'
num = 2*gamma*v_bar/(r_bar**2)
p1 = 2*gamma*v_bar**2/r_bar**3
den = [1, 0, p1]
G = signal.TransferFunction(num,den)
z,p,k = signal.tf2zpk(num,den)
#print(G)


#  ------------- Initiate Controller ---------------
Kd = 1;
Kp = 1;
Ki = 1;
C = signal.TransferFunction([Kd, Kp, Ki],1)
#print(C)
plt.figure(1)
#for i in R_hat_0:


# ---------------- Multiply the transfer functions -------------
symG, symC = lti_to_sympy(G), lti_to_sympy(C)
symCG = symG*symC

CG = sympy_to_lti(symCG)

tout,y,x = signal.lsim(CG, step, t, R_hat_0)
print(y)
plt.plot(t,y)
#plt.legend(loc='best')
plt.show()
