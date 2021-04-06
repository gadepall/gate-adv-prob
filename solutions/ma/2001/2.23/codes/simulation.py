import random 
import numpy as np
from matplotlib import pyplot as plt

#a function that calculates the probability for a random m value
def get_probability(num_samples, r):
    i=0
    t=0

    m = (1 if random.random() > 0.5 else -1) * random.randint(-10000,10000)
    while i<num_samples:
        mult = 1 if random.random() > 0.5 else -1
        X = random.random()*r*mult
        Y = random.random()*r*mult
        if Y>=m*X:
            t=t+1
        i=i+1
    return t/num_samples

su_ = 0
num_samples = 10000
ite = 10

#calculating the probability 'ite' times by generating 'num_samples' points (X,Y)
for i in range(ite):
    cur = get_probability(num_samples, 10)
    su_ += cur
prob = su_/ite
print('probability: ',prob)

#plotting the graphs 

prob_plot = []
prob_cal = []
for x in range(4):
    prob_plot.append(get_probability(num_samples, 10))
    prob_cal.append(1/2)
x = np.arange(1,5)

plt.ylim(0,0.75)
plt.stem(x,prob_plot, markerfmt='o', use_line_collection=True, label='Simulation')
plt.stem(x,prob_cal, markerfmt='o',use_line_collection=True, label='Analysis')
plt.xlabel('Simulation')
plt.ylabel('Probability')
plt.xticks( x)
plt.legend()
plt.grid()
plt.show()
