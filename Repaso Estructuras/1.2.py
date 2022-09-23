
import random as random
from time import time 


inicio= time()
x = []

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

for i in range(800):
    x.append(random.randint(1,400))
for i in range(800):
    x.append(random.randint(401,800))
for i in range(800):
    x.append(random.randint(801,1200))
for i in range(800):
    x.append(random.randint(1201,1600))  
for i in range(800):
    x.append(random.randint(1601,2000))  

burbuja_optimus(x)

print(x)

tiempo = time() - inicio
print(str(tiempo))