def caracter_mas_repetido(frase):
    contador = [0] * 256 #Palabras con la ñ
    y = ("abcdefghijklmnñopqrstuvwxyz")
    p = []
    
    for c in frase:
        contador[ord(c)] += 1
        
    maximo = -1
    caracter = '' 

    for y in frase:
        if y in frase:
            p.append(y)
    print(p)

    for c in frase:
        if maximo < contador[ord(c)]:
            maximo = contador[ord(c)]
            caracter = c
    return caracter


cadena = input("Digite una palabra: ")
print("La letra más repetida es la " + caracter_mas_repetido(cadena))