import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y=[] 
y1=[]
# plt.figure(figsize=(10,7))
plt.ylim(0,0.3)
plt.xlim(-1,7)
for i in range(100):
    y.append(1/(2*np.pi))
    y1.append(0)
# fig = plt.figure() 
plt.plot(x, y,color='black') 
plt.vlines(x=[0,2*np.pi], ymin=[0,0], ymax=[1/(2*np.pi), 1/(2*np.pi)], ls='-', color='orange')
plt.vlines(x=[2.3, 2.3+np.pi], ymin=[0,0], ymax=[1/(2*np.pi), 1/(2*np.pi)], ls='--', color='g')
section = np.arange(2.3, np.pi+2.3, 1/20.)
for i in range(63):
  section_=[1/(2*np.pi)]
plt.fill_between(section,section_, color = 'r')
plt.xticks([0,np.pi,np.pi/2,2*np.pi, 3/2*np.pi])
plt.yticks([0,1/(2*np.pi),1/(4*np.pi),3/(4*np.pi)])
plt.xlabel('\u03B8 values')
plt.ylabel('Density Function')
plt.show() 
