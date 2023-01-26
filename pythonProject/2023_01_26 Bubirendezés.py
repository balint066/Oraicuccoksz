lista=[1,3,6,7,8,3,4,4546,5,6,4,4,3,0,-434]
for i in range(len(lista),0,-1):
    for j in range(0,i-1):
        if lista[j] > lista[j+1]:
            #print(lista)
            b = lista[j+1]
            #print(lista)
            lista[j+1] = lista[j]
            #print(lista)
            lista[j]=b

print("A vége:",lista)
lista1=[1,3,6,7,8,3,4,4546,5,6,4,4,3,0,-434]
