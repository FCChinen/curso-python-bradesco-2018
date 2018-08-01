import numpy as np
import matplotlib.pyplot as plt

def densidadedeprobabilidade(x, u, v):
    return np.exp(-(np.power((xis-u),2))/2*np.power(v,2))/np.sqrt(2*np.pi*np.power(v,2))

x = np.linspace(-5,5,100)
y = np.linspace(-5,5,100)
for i, xis in enumerate(x):
    y[i] = densidadedeprobabilidade(xis, 0, 1)

plt.plot(x, y)
plt.show()
