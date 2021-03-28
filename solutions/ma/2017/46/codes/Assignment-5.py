from scipy.stats import geom
import numpy as np
import seaborn as sb


simlen=int(1e8) # calculating expectation value upto the largest possible value keeping tim ein mind
p=0.25
t=[]
s=geom.rvs(p,size=simlen)
#for i in range(1,simlen):

unique, counts = np.unique(s, return_counts=True)
for i in range(len(unique)):
  t.append(unique[i]*counts[i]/simlen)#calculating expectation values of each event from the generated data
sum=0
for q in range(len(t)):
  sum=sum+t[q]
sim_expected=sum
theo_expected=4
#plotting
x = np.arange(0,25)

p=0.25
dist=geom(p)
ax = sb.barplot(x=x, y=dist.pmf(x))
ax.set(xlabel='n', ylabel='p(n)')
print(f'The theoretical expected value is 4 and the simulated expected value is {sim_expected}')