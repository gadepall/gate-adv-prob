import numpy as np
import matplotlib.pyplot as plt

def F(x):
  if (x<0):
    return 0
  elif (x>=0) and (x< 1):
    return x/2
  elif (x>=1) and(x<2):
    return 3/5
  elif (x>=2) and(x<3):
    return 1/2 + x/8
  elif (x>=3):
    return 1;
  else:
      return 0


X = np.linspace(-3,6,1000000)

Y = [F(x) for x in X]
plt.xlabel('x')
plt.ylabel('$F(x)$')
plt.plot(X,Y)
plt.grid()
plt.show()