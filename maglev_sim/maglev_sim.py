import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

g = 9.8                                 #[m/s^2]
gamma = 1                             #[who knows?]
v_bar = 6                               #[V]
r_bar = -np.sqrt((gamma*v_bar**2)/g)     #[length]
print('r_bar = ',r_bar)
R_hat_0 = 1

t = np.arange(0.0,1.0,0.01)
step = v_bar*np.heaviside(t,1)

name = 'Test'
num = 2*gamma/(r_bar**2)
p1 = 2*gamma*v_bar**2/r_bar**3
den = [1, 0, p1]
sys = signal.TransferFunction(num,den)
z,p,k = signal.tf2zpk(num,den)
print(p)
tout,y,x = signal.lsim(sys, step, t, R_hat_0)
print(y)
plt.figure(1)
plt.plot(t,y,'k-',label=name)
plt.legend(loc='best')
plt.show()
