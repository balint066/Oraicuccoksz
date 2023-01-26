lista = [34,3,435,65,46,6,757,3,55,3535,3,54,-25,-325,-45,2,5443,-6]
lista1 = [34,3,435,65,4632,423,3,23,432,54,-25,-325,-45,2,5443,-6]
lista2 = [34,3,4,5,3,35,435,34,43,-45,2,5443,-6]
lista3 = [2135343245,62435,652,546,23546,5,-325,-45,2,5443,-6]
lista4 = [34,3,435,65,46,6,757,3,55,3535023432,23,5324,415,5443,-6]

def minkeres(lista):
    min = lista[0]
    for i in lista:
        if i < min:
            min = i
    #print(min)
    return min
minimum1 = minkeres(lista1)
print(minimum1)
minimum2 = minkeres(lista2)
minimum3 = minkeres(lista3)
minimum4 = minkeres(lista4)
