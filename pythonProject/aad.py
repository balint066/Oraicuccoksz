lista1 = [6, 5, 6, 254, 6, 4, 4, 4, 44, 5432, 5, 43]
for i in range(len(lista1)-1):
    minindex = i

    for j in range(i + 1, len(lista1)):
        if lista1[j] < lista1[minindex]:
            minindex = j
    if i != minindex:
        lista1[i], lista1[minindex] = lista1[minindex], lista1[i]

print(" ", lista1)