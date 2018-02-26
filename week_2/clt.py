import numpy as np
import matplotlib.pyplot as plt
# In a jupyter-notebook you can add the line "%matplotlib inline"

x = np.random.randn(1000000)
plt.hist(x, bins=100)
plt.show()  # and remove this line (in jupyter-notebook)


# Show the consequences of the central limit theorem using numpy

