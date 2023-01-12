lista1=[-14,23,1,-48,-43,28,-77,-33,-95,38,-9,98,-61,58,21,87,41,-56,-22,-20,-56,-7,5,80,-77,100,67,22,8,-78,-6]
#1
elem = 0
for num in lista1:
    if num:
        elem = elem+1
print("Elem számok",elem)
#2
count = 0
for num in lista1:
    if num < 0:
        count = count + 1
print("A listában van negatív szám")
#3
paros = 0
for num in lista1:
    if num%2 == 0:
        paros = paros + 1
print(paros)
#4
maxElem = lista1[0]
for i in range(1,len(lista1)):
    if lista1[i] > maxElem:
        maxElem = lista1[i]
print(maxElem,)
#5
tizes = 0
for num in lista1:
    if num%10 == 0:
       tizes = tizes + 1
print(tizes)
#6
i = 0
while i < elem and lista1[i] % 29 != 0:
    i = i+1
print(i, lista1[i])
#7
logikai = True
while i < elem and lista1[i] % 2 == 0:
    i = i+1
if i< elem:
    logikai=False
print(logikai)
#8
atl = 0
osszeg = 0
for i in lista1:
    osszeg= osszeg+i
atl = osszeg/elem
print(atl)