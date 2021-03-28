import numpy as np
import matplotlib.pyplot as plt

def F(x):
  if (x<0):
    return 0
  elif (x>=0) and (x<0.5):
    return x
  elif (x>=0.5) and(x<1):
    return (1+x)/2
  else :
    return 1


X = np.linspace(-2,4,1000000)

Y = [F(x) for x in X]
plt.xlabel('x')
plt.ylabel('$F_X(x)$')
plt.plot(X,Y)
plt.grid()
plt.show()