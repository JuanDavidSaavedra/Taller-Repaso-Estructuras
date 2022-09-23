import random as random
from time import time 

inicio= time()
arreglo = []
n = 2000

def burbuja_optimus(arreglo):
    n = len(arreglo)
  
    for i in range(n-1):
        intercambio = False
 
        for j in range(n-1-i):
            if arreglo[j] > arreglo[j+1] :
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
                intercambio = True
 
        if intercambio == False:
            break

def suma_2_numeros_menores(arreglo):
    suma = arreglo[0] + arreglo[1]
    return suma

for i in range(n):
    arreglo.append(random.randint(1,100))

burbuja_optimus(arreglo)

print("\n", arreglo)
print("\nLa suma de los 2 menores números es:", suma_2_numeros_menores(arreglo))
print("Los 3 mayores números de este nuevo conjunto son: " + str(arreglo[n-3]) + ", " + str(arreglo[n-2]) + ", " + str(arreglo[n-1]))

tiempo = time() - inicio
print("\nTiempo de ejecucción: ", str(tiempo))