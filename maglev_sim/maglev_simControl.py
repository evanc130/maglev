import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import sympy as sy
import control

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
step = R_hat_0*np.heaviside(t,1)


# ---------------- Initiate Plant ------------------
num = 2*gamma*v_bar/(r_bar**2)
p1 = 2*gamma*v_bar**2/r_bar**3
den = [1, 0, p1]

Gsys = control.TransferFunction(num, den)


#  ------------- Initiate Controller ---------------
Kgain = 75
tau = .5    # 1/intended zero placement
numC = np.array([tau, 1])*Kgain
Csys = control.TransferFunction(numC, 1)


# ---------------- Multiply the transfer functions -------------
CGsys = control.series(Csys, Gsys)
control.pzmap(CGsys, Plot=True, title='Pole Zero Map of Plant')
print(Csys)
print(Gsys)
print(CGsys)

plt.figure()
tout, y, x = control.forced_response(CGsys, t, step, R_hat_0)
plt.plot(t, y)
plt.show()

# tout,y,x = signal.lsim(CG, step, t, R_hat_0)
# print(y)
# plt.plot(t,y)
# #plt.legend(loc='best')
# plt.show()
