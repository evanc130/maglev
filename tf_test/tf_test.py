import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

t = np.arange(0.0,10.0,0.01)
step = 2*np.heaviside(t,1)

name = 'Problem 1C'
num = [1]
p1 = np.poly1d([1,1])
p2 = np.poly1d([1,1,1])
den = p1*p2
print(den)
sys = signal.TransferFunction(num,den)
tout,y,x = signal.lsim(sys, step, t)
plt.figure(3)
plt.plot(t,y,'k-',label=name)
plt.legend(loc='best')
plt.show()