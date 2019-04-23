import numpy as np
from matplotlib import pyplot as plt
import cmath as cm

fm=input('enter freq=')	
fs=2*fm
x=np.sin(2*np.pi*fm)
y=[ ]

for n in range(0,1,10):
		s=np.sin(((2*np.pi*fm)/fs)*n)
		y.append(abs(s))



plt.plot(x)
plt.show()
plt.stem(y)							
plt.show()






