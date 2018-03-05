import numpy as np
import matplotlib.pyplot as plt

n = 1000000
m = 15

r = (np.random.rand(n, m) * 2 - 1) * 3 ** 0.5  # uniform with normalized variance and zero mean
r = r.sum(1)
plt.hist(r, bins=100, normed=True)

x = np.linspace(-4, 4, 100) * m ** 0.5
y = np.exp(-x ** 2 / (2 * m)) / (2 * np.pi * m) ** 0.5
plt.plot(x, y)

plt.show()

