import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

g = 9.8                                 #[m/s^2]
v_bar = 6                               #[V]
gamma = 1                             #[who knows?]


name = 'Test'
num = g
p1 = 2*g/(np.sqrt(gamma*v_bar/g))
den = [v_bar, 0, p1]
sys = signal.TransferFunction(num,den)
t,y = signal.step(sys)
plt.figure(1)
plt.plot(t,y,'k-',label=name)
plt.legend(loc='best')
plt.show()