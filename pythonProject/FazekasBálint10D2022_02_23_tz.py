lista=[]

def vege(szam):
    if szam == -1:
        return True
    else:
        return False
def paros(szam):
    if szam % 2 == 0:
        return True
    else:
        return False

def legnagyobb(lista):
    legnagyobb = lista[0]
    for i in lista:
        if i > legnagyobb:
           legnagyobb = i
    return legnagyobb

def nagynezo(lista):
    nagy=legnagyobb(lista)
    if nagy%2 == 0:
        return True
    else:
        return False

def rendeznov(lista):
    for i in range(len(lista), 0, -1):
        for j in range(0, i - 1):
            if lista[j] > lista[j + 1]:
                b = lista[j + 1]
                lista[j + 1] = lista[j]
                lista[j] = b
    return lista

def paros(szam):
    paros = []
    if szam%2 == 0:
        paros.append(szam)
    return paros
def paratlan(szam):
    paratlan = []
    if szam%2 != 0:
        paratlan.append(szam)
    return paratlan

while True:

    a = int(input("adj meg egy számot"))

    if vege(a):
        break
    else:
        lista.append(a)
nagyka = legnagyobb(lista)

print("Az eredeti lista",lista)
print("A rendezett lista", rendeznov(lista))
print("A legnagyobb szám", nagyka)
