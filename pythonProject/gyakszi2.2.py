lista=[]
osszeg = 0
maximum  = -1
for i in range(5):
    a = int(input())
    lista.append(a)
    osszeg = osszeg+a
    if maximum < a:
        maximum = a
print(lista)
print(osszeg/len(lista))
print(maximum,lista.index(maximum))
