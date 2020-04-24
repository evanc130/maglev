import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

g = 9.8                                 #[m/s^2]
gamma = 1                             #[who knows?]
v_bar = 6                               #[V]
r_bar = np.sqrt((gamma*v_bar**2)/g)     #[length]


t = np.arange(0.0,10.0,0.01)
step = v_bar*np.heaviside(t,1)

name = 'Test'
num = 2*gamma/(r_bar**2)
p1 = 2*gamma*v_bar**2/r_bar**3
den = [1, 0, p1]
sys = signal.TransferFunction(num,den)
tout,y,x = signal.lsim(sys, step, t)
plt.figure(1)
plt.plot(t,y,'k-',label=name)
plt.legend(loc='best')
plt.show()
