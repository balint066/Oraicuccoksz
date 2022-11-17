szam = -3
mertekegyseg = input("Mértékegység: mm, cm, dm, m, km    ")
valt = input("Váltómértékegység: mm, cm, dm, m, km   ")

while szam<=0 and :
    szam = float(input("Adja meg az átváltani kívánt értéket   "))


if mertekegyseg == "mm":
    if valt == "mm":
        print("A választott szám mm-ben", szam)
    elif valt == "cm":
        CM = szam/10
        print("A választott szám cm-ben", CM)
    elif valt == "dm":
        DM = szam/100
        print("A választott szám dm-ben", DM)
    elif valt == "m":
        M = szam/1000
        print("A választott szám m-ben", M)
    elif valt == "km":
        KM = szam/1000000
        print("A választott szám km-ben", KM)

elif mertekegyseg == "cm":
    if valt == "mm":
        MM = szam*10
        print("A választott szám mm-ben", MM)
    elif valt == "cm":
        CM = szam
        print("A választott szám cm-ben", CM)
    elif valt == "dm":
        DM = szam/10
        print("A választott szám dm-ben", DM)
    elif valt == "m":
        M = szam/100
        print("A választott szám m-ben", M)
    elif valt == "km":
        KM = szam/100000
        print("A választott szám km-ben", KM)

elif mertekegyseg == "dm":
    if valt == "mm":
        MM = szam * 100
        print("A választott szám mm-ben", MM)
    elif valt == "cm":
        CM = szam*10
        print("A választott szám cm-ben", CM)
    elif valt == "dm":
        DM = szam
        print("A választott szám dm-ben", DM)
    elif valt == "m":
        M = szam/10
        print("A választott szám m-ben", M)
    elif valt == "km":
        KM = szam/10000
        print("A választott szám km-ben", KM)

elif mertekegyseg == "m":
    if valt == "mm":
        MM = szam * 1000
        print("A választott szám mm-ben", szam)
    elif valt == "cm":
        CM = szam*100
        print("A választott szám cm-ben", CM)
    elif valt == "dm":
        DM = szam*10
        print("A választott szám dm-ben", DM)
    elif valt == "m":
        M = szam
        print("A választott szám m-ben", M)
    elif valt == "km":
        KM = szam/1000
        print("A választott szám km-ben", KM)

elif mertekegyseg == "km":
    if valt == "mm":
        MM = szam * 1000000
        print("A választott szám mm-ben", szam)
    elif valt == "cm":
        CM = szam*100000
        print("A választott szám cm-ben", CM)
    elif valt == "dm":
        DM = szam*10000
        print("A választott szám dm-ben", DM)
    elif valt == "m":
        M = szam*1000
        print("A választott szám m-ben", M)
    elif valt == "km":
        KM = szam
        print("A választott szám km-ben", KM)
