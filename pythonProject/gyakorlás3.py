import math
a = int(input())
muvelet = input()
b = int(input())



eredmeny = -1
if muvelet == "+":
    eredmeny = a + b
elif muvelet == "-":
    eredmeny = a - b
elif muvelet == "*":
    eredmeny = a * b
elif muvelet == "/":
    eredmeny = a / b
elif muvelet == "**":
    eredmeny = a ** b
elif muvelet == "/-":
    eredmeny =  math.sqrt(a)
print(eredmeny)