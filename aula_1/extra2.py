import matplotlib.pyplot as plt
import numpy as np

def densidadedeprobabilidade(x, u, v):
    return np.exp(-(np.power((x-u),2))/2*np.power(v,2))/np.sqrt(2*np.pi*np.power(v,2))

x = np.linspace(-10,10,500)
y = np.zeros(500)
y1 = np.zeros(500)
y2 = np.zeros(500)
y3 = np.zeros(500)

for i, xis in enumerate(x):
	y[i] = densidadedeprobabilidade(xis, 0, 1)
	y1[i] = densidadedeprobabilidade(xis, 0, 5)
	y2[i] = densidadedeprobabilidade(xis, 0, 0.2)
	y3[i] = densidadedeprobabilidade(xis, 5, 1)

plt.plot(x, y)
plt.plot(x, y1, 'green')
plt.plot(x, y2, 'red')
plt.plot(x, y3, 'yellow')
plt.show()
