def rendezo(lista):
    for i in range(len(lista), 0, -1):
        for j in range(0, i - 1):
            if lista[j] > lista[j + 1]:
                b = lista[j + 1]
                lista[j + 1] = lista[j]
                lista[j] = b
        return lista
lista=[]
with open("egysoros.txt","r",encoding="utf-8") as forras:
    for sor in forras:
        lista = sor.strip().split(";")

print(lista)
for i in lista:
    lista[0]=int(lista[0])
print(rendezo(lista))
with open("egysoros_eredmeny.txt","w",encoding="utf-8") as cel:
    for i in lista:
        cel.write(i,",")