print("\n","1.feladat")
for i in range(0,1):
    a = input("Adj meg egy számot: ")
    b = input("Adj meg egy számot: ")
if a<b:
    print(b, "a nagyobb szám")
else:
    print(a, "a nagyobb szám")
if a==b:
    print("egyenlő")

print("\n","2.feladat")
def kodolas(mondat,betu,darab):
    cserel = ""
    db=0
    for i in mondat:
        if i == betu and db < darab:
            cserel=cserel+str(ord(i))
            db = db + 1
        else:
            cserel = cserel+i
    return cserel
szoveg= kodolas("Kijött a börtönből az anyja megkurvút","a",2)
print(szoveg)


