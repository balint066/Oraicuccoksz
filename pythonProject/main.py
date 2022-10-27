#pitagorasz tétel
import math
print("Add meg az a oldalt")
a = float(input())
print("Add meg a b oldalt")
b = float(input())

if a==0:
    print("píha ne legyél piszkos")
elif b==0:
    print("píha te megint piszkos vagy")


pitagorasz1 = math.sqrt(a**2+b**2)

print("A c oldal:", round(pitagorasz1,8))


