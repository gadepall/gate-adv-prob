import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(0, np.pi/2-0.1, 100)
plt.plot(x, np.tan(x), color='orange') 
plt.vlines(x=[np.arctan(2.5), np.arctan(2.5)+np.pi], ymin=[-10,-10], ymax=[2.5,2.5], ls='--', color='g')
plt.vlines(x=[np.pi/2,3*np.pi/2], ymin=[0,-10], ymax=[10,0], ls='--', color='r')
plt.xticks([0,np.pi,np.pi/2,2*np.pi, 3/2*np.pi])
x = np.linspace(np.pi/2+0.1, 3*np.pi/2-0.1, 100)
plt.plot(x, np.tan(x), color='orange') 
x = np.linspace(3*np.pi/2+0.1,2*np.pi, 100)
plt.plot(x, np.tan(x), color='orange') 
x = np.linspace(0, 2*np.pi, 100)
plt.plot(x, 0*np.tan(x), color='black') 
plt.plot(x, 0*np.tan(x)+2.5, color='black', ls='--') 
plt.plot(np.arctan(2.5),0,'bo')
plt.plot(np.arctan(2.5)+np.pi,0,'bo')
plt.plot(np.pi/2,0,'bo')
plt.plot(3*np.pi/2,0,'bo')

plt.xlabel('$\u03B8$')
plt.ylabel('$tan\u03B8$')
plt.show() 