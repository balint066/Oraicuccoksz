lista=[10,-2,1,25,22,30,60,-99,-1252,3000,2123,16,12]

for i in range(len(lista)-1):
    minindex = i

    for j in range(i + 1, len(lista)):
        if lista[j] < lista[minindex]:
            minindex = j
    if i != minindex:
        lista[i], lista[minindex] = lista[minindex], lista[i]

print("A növekvő sorrend:  ", lista)
print("A legkisebb:  ", lista[0])

for i in range(len(lista)-1):
    minindex = i

    for j in range(i + 1, len(lista)):
        if lista[j] > lista[minindex]:
            minindex = j
    if i != minindex:
        lista[i], lista[minindex] = lista[minindex], lista[i]
print("A csökkenő sorrend:  ", lista)
print("A legnagyobb:  ", lista[0])


