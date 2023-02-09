def rendeznov(lista):
    for i in range(len(lista), 0, -1):
        for j in range(0, i - 1):
            if lista[j] > lista[j + 1]:
                b = lista[j + 1]
                lista[j + 1] = lista[j]
                lista[j] = b
    return lista
def minimum(lista):
    minimum = lista[0]
    for i in lista:
        if i < minimum:
            minimum = i
    return minimum

def maximum(lista):
    maximum = lista[0]
    for i in lista:
        if i > maximum:
            maximum = i
    return maximum
lista=[1,9,-6,11,7,12,120,-96,55,42,300,15,-1]
lista = rendeznov(lista)
legkisebb1 = minimum(lista)
legnagyobb1 = maximum(lista)

legkisebb = lista[0]
legnagyobb = len(lista) - 1

print("A legkisebb:",legkisebb,",függvénnyel:", legkisebb1)
print("A legnagyobb:",lista[legnagyobb],",függvénnyel:", legnagyobb1)