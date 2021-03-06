# -*- coding: utf-8 -*-
"""Assignment4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qay6O0blUGpwvdC0qu1Y--Jy1IHPkvWw
"""

import numpy as np
import matplotlib.pyplot as plt

def F(x):
  if (x<0):
    return 0
  elif (x>0) and (x< 1/2):
    return x**2
  elif (x>=1/2) and(x<1):
    return 3/4
  elif (x>=1):
    return 1;
  else:
      return 0


X = np.linspace(-5,5,1000000)

Y = [F(x) for x in X]
plt.xlabel('x')
plt.ylabel('$F(x)$')
plt.plot(X,Y)
plt.grid()
plt.savefig('Assignment4.png' , dpi=100)
plt.show()