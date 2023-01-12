lista = []
minimum = 10000000000000000000000
mximum = -10000000000000000000000
helymax = 0
helymin =0
for i in range(5):
    a = int(input())
    lista.append(a)
    if mximum < a:
        mximum = a
        helymax = lista.index(a)
    if minimum > a:
        minimum = a
        helymin = lista.index(a)
print("A maximum érték:", mximum, "helye:", helymax)
print("A minimum érték :", minimum, "helye:", helymin)
