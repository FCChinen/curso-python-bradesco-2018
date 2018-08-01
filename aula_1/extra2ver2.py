import matplotlib.pyplot as plt
import numpy as np

def densidadedeprobabilidade(x, u, v):
	aux = np.zeros(len(x))
	for i, ex in enumerate(x):
		aux[i] = np.exp(-(np.power((ex-u),2))/2*np.power(v,2))/np.sqrt(2*np.pi*np.power(v,2))
	return aux

x = np.linspace(-10,10,500)
y = np.zeros(500)
y1 = np.zeros(500)
y2 = np.zeros(500)
y3 = np.zeros(500)

y = densidadedeprobabilidade(x, 0, 1)
y1 = densidadedeprobabilidade(x, 0, 5)
y2 = densidadedeprobabilidade(x, 0, 0.2)
y3 = densidadedeprobabilidade(x, 5, 1)

plt.plot(x, y)
plt.plot(x, y1, 'green')
plt.plot(x, y2, 'red')
plt.plot(x, y3, 'yellow')
plt.show()
