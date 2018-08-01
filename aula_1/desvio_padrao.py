import numpy as np

def desviopadrao1(array_pontos):
	desv = 0
	med = np.mean(array_pontos)
	for ponto in array_pontos:
		aux = ponto - med
		aux = np.power(aux,2)
		desv += aux
	desv = desv/len(array_pontos)
	desv = np.power(desv,0.5)
	return desv

def desviopadrao2(array_pontos):
	med1 = np.power(np.mean(array_pontos),2)
	med2 = np.mean(np.power(array_pontos,2))
	desv = med2 - med1
	desv = np.power(desv,0.5)
	return desv

def main():	
	a = np.array([2, 4, 4, 4, 5, 5, 7, 9])
	print("Desvio do numpy: "+ str(np.std(a)))
	print("Desvio padrao 1: "+ str(desviopadrao1(a)))
	print("Desvio padrao 2: "+ str(desviopadrao2(a)))	
if __name__ == "__main__":
	main()
