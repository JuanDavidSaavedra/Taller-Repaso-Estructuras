def calcularBase(pot,exp):
    if (exp==0):
        return 1
    else:
        return int(pot**(1/exp))

pot = int(input("Digite un número (potencia): "))
exp = int(input("Digite otro número (exponente)"))
print("La base es: ", calcularBase(pot,exp))