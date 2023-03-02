a = input("adj meg egy szót ")

for i in a:
    b = ord(i)
    c = b-32
    d = chr(c)
    print(d, end=" ")


    def rendeznov(lista):
        for i in range(len(lista), 0, -1):
            for j in range(0, i - 1):
                if lista[j] > lista[j + 1]:
                    b = lista[j + 1]
                    lista[j + 1] = lista[j]
                    lista[j] = b
        return lista
