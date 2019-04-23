import numpy as np
from matplotlib import pyplot as plt
import cmath as cm

x=input('enter seq1=')	
d=input('delay=')


def dft(x,d):
	j=cm.sqrt(-1)
	y=[ ]
	N=len(x)
	
	for k in range(0,N):
		w=((2*np.pi)/N)
		sum=0
		for n in range(0,N):
			sum=sum+(x[n]*np.exp(-j*w*k*n))
		p=np.exp(-j*(2*np.pi/N)*k*d) 
		sum=sum*p
		y.append(abs(sum))
		 
		         		         
	return y

t=dft(x,d)
print t
plt.stem(t)							#plt.stem(t)
plt.show()






