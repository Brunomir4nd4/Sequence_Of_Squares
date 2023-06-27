n = 0
r = 1
sqrt = 0
soma = 0
cont = 1
listaNum = []
listaSqrt = []

num = input("Insira o número A0: ")

while r != 0:
    
    for i in range(len(num)):
        n = int(num[i])
        listaNum.append(n)

    listaSqrt.append(int(num))

    for i in range(len(listaNum)):
        sqrt = listaNum[i]**2
        soma += sqrt

    for i in range(len(listaSqrt)):
        if soma == listaSqrt[i]:
            r = 0
            break

    num = str(soma)
    cont += 1
    listaNum = []
    soma = 0
    

print(cont)

