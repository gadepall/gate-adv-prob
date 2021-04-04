from scipy.stats import expon, gamma

sim_len = 1000000
count = 0

Y = []
for i in range(10):
    Y.append(expon.rvs(size=sim_len))

Y11 = expon.rvs(size=sim_len)
Y12 = expon.rvs(size=sim_len)

X1 = gamma.rvs(a=2, size=sim_len)
X2 = gamma.rvs(a=2, size=sim_len)
X3 = gamma.rvs(a=2, size=sim_len)

for i in range(sim_len):
    temp1 = 0
    temp2 = 0
    for j in range(10):
        if Y[j][i] < X1[i] + X2[i]:
            temp1 = 1
        if Y[j][i] < X1[i] + X2[i] + X3[i]:
            temp2 = 1
    if (X1[i] + Y11[i] > X1[i] + X2[i]) and (temp1 == 0):
        if (X1[i] + Y11[i] < X1[i] + X2[i] + X3[i]) or (X1[i] + X2[i] + Y12[i] < X1[i] + X2[i] + X3[i]) or (temp2 == 1):
            count += 1

print("Experimental probability = ", count / sim_len)
print("which is approximately equal to 5.7e-05(theoritical value)")
