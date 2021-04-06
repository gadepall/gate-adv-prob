import numpy as np
import matplotlib.pyplot as plt
import random
count=0
sample_size=1000
x=[]
def F(x):
  if (x<-1):
    return 0
  elif (x>=-1) and (x<=1):
    return (1+x)/2
  else :
    return 1
for i in range(sample_size):
    t=np.random.choice(a=[-1,1],size=1000)
    p=0
    for j in range(1000):
        p=p+(t[j]/pow(2,j+1))
    x.append(p)
X1 = np.sort(x)
Y1 = np.array(range(sample_size))/float(sample_size)
X = np.linspace(-2,2,1000000)

Y = [F(x) for x in X]
plt.xlabel('y')
plt.ylabel('$F_Y(y)$')

plt.plot(X1,Y1,label="Simulated cdf")
plt.plot(X,Y,label="Expected cdf")
plt.legend()
plt.show()
