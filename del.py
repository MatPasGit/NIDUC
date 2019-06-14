import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import scipy.stats

arr = np.random.randn(1000)

plt.figure(1)
result = plt.hist(arr)
plt.xlim((min(arr), max(arr)))

mean = np.mean(arr)
variance = np.var(arr)
sigma = np.sqrt(variance)
x = np.linspace(min(arr), max(arr), 100)
dx = result[1][1] - result[1][0]
scale = len(arr)*dx
plt.plot(x, scipy.stats.norm.pdf(x, mean, sigma)*scale)

plt.show()
