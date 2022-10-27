print("Adjon meg egy számot")
alapszam = float(input())
a = 0
for i in range(5):

    print("Adjon meg még egy számot")
    b = float(input())
    a = a+b
if alapszam < a:
    print(a/5)
else:
    print(a**2)