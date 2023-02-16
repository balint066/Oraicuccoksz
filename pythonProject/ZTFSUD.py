a = input("adj meg egy szót ")

for i in a:
    b = ord(i)
    c = b-32
    d = chr(c)
    print(d, end=" ")
