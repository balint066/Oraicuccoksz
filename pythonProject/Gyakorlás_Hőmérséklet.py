szam = int(input())
logikai = True
for i in range(2,szam,1):
    if szam % i == 0:
        logikai = False
if logikai:
   print("prímszám")
else:
    print("nem prímszám")
