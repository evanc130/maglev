import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

name = 'Problem 1C'
num = [1]
p1 = np.poly1d([1,1])
p2 = np.poly1d([1,1,1])
den = p1*p2
print(den)
sys = signal.TransferFunction(num,den)
t,y = signal.step(sys,T=t)
plt.figure(3)
plt.plot(t,y,'k-',label=name)
plt.legend(loc='best')
plt.show()
