
lista1 = list()

lista2 = list()

lista3 = list()

soma = 0
for i in range(0, 3):

    for j in range(0, 4):

        lista2.append(float(input(f"Digite um valor para coordenada [{i}, {j}]: \n")))

    lista1.append(lista2[:])

    lista2.clear()

for l in lista1:

    print(l)

for i in range(0, 3):

    for j in range(0, 4):

        if j == 1 and j == 3:

            soma += lista2[i][j]

        else:

            soma += lista3[i][j]

print(soma)

print(lista2)