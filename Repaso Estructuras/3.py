y = "Muy buenas noches como estan hoy miercoles"
x = input("Digite una palabra: ")
h = 0

for i in range(len(y)):
    if x[0]==y[i]:
        c=0
        for j in range(len(x)):
            if x[j]==y[i+j]:
                c = c +1
            else:
                break
        if c==len(x):
            if h==0:
                print("La palabra está incluida")
                h=1
        else:
            print("No está incluida")
print(y)