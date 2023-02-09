lista=[]
def májnimum(lista):
    legkisebb=lista[0]
    for i in lista:
        if i < legkisebb:
            legkisebb = i
    return legkisebb
def kilep(szam):
    if szam == 0:
        return True
    else:
        return False
lista= []

while True:
    a = int(input("adjál számot"))
    if kilep(a):
        break
    else:
        lista.append(a)
pici = májnimum(lista)
print(pici)


