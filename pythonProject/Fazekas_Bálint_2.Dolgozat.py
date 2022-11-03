a = int(input("Adjon meg egy számot! "))
logikai = True
for i in range(2,a,1):
    if a % i == 0:
        logikai = False
if logikai :
    a = int(input("Adjon meg egy számot! "))
else:
    if a % 2 == 0:
        print("Hurrá")
    if a % 2 != 0 and a % 3 == 0:
        print("Három a magyar igazság")
    if a <= 10:
        if a == 1:
            print("I")
        if a == 2:
            print("II")
        if a == 3:
            print("III")
        if a == 4:
            print("IV")
        if a == 5:
            print("V")
        if a == 6:
            print("VI")
        if a == 7:
            print("VII")
        if a == 8:
            print("VIII")
        if a == 9:
            print("IX")
        if a == 10:
            print("X")

