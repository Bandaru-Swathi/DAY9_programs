import numpy as np
from matplotlib import pyplot as plt
import cmath as cm

def idft(x):
	j=cm.sqrt(-1)
	y=[ ]
	N=len(x)
	for n in range(0,N):
		w=((2*np.pi)/N)
		sum=0
		for k in range(0,N):
			sum=sum+(x[k]*np.exp(j*w*k*n))
		sum=sum/N
		y.append((sum))                             #y.append(abs(sum))   
	
	return y


x=input('enter seq1=')	
t=idft(x)
print t
plt.stem(t)            #plt.plot(t)
plt.show()




