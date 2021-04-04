import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from scipy import signal

#verifying the result obtained with numerical value
c=2 

#generating two uniform distributions 
y_1 = stats.uniform(loc=-c/4, scale=c/2)
y_2 = stats.uniform(loc=(2/c)+(c/4), scale=c/2)

dx = 0.0001
x = np.arange(-4,4,dx)

pmf1 = y_1.pdf(x)*dx
pmf2 = y_2.pdf(x)*dx
conv_pmf = signal.fftconvolve(pmf1,pmf2,'same')

pdf1 = pmf1/dx
pdf2 = pmf2/dx
conv_pdf = conv_pmf/dx


print("Area under pdf of Y_1: " +str(np.trapz(pdf1,x)))
print("Area under pdf of Y_2: " +str(np.trapz(pdf2,x)))
print("Area under convoluted pdf: " +str(np.trapz(conv_pdf,x)))

#plotting pdfs of uniform distributions and convoluted function
plt.plot(x,pdf1, label='$Y_2$')
plt.plot(x,pdf2, label='$Y_1$')
plt.plot(x,conv_pdf, label='X')
plt.legend(loc='best')
plt.suptitle('PDFs')
plt.grid()
plt.show()

# Normalize the data to a proper PDF
Z=conv_pdf/ (dx * conv_pdf).sum()

# Compute the CDF
cdf = np.cumsum(Z * dx)
plt.plot(x,cdf)
plt.xlabel('Random Variable , X')
plt.ylabel('$F_{X}(x)$')
plt.suptitle('CDF of X')
plt.grid()
plt.show()
