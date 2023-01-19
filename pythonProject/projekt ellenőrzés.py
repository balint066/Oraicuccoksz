lista = [6, 5, 6, 254, 6, 4, 4, 4, 44, 5432, 5, 43]
for i in range(len(lista) - 1):
    for j in range(i + 1, len(lista)):
        #print(i, j, lista, end=" ")
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]
            #print("!", lista[i], lista[j], )

        #else:
           # print("")
print(" ", lista)


