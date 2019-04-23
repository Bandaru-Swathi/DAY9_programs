import numpy as np
from matplotlib import pyplot as plt
import cmath as cm

def dtft(x):
	j=cm.sqrt(-1)
	y=[ ]
	N=14
	n=len(x)
	p=np.linspace(0,2*np.pi,N)
	for i in range(0,N):
		w=p[i]
		print w
		sum=0
		for k in range(0,n):
			sum=sum+(x[k]*np.exp(-j*w*k))
		y.append(abs(sum))
	return y


x=input('enter seq1=')	
t=dtft(x)
plt.plot(t)
plt.show()




