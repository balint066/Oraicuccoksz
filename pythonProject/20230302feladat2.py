szotar = {}

while True:
    mufaj = {}
    címek = {}
    szerzo = input("adjon meg egy szerzőt")
    if szerzo == "":
        break
    else:
        while True:
            cim = input("adja meg a szerző műjét")
            if cim == "":
                break
            else:
                kiadas = int(input("adj meg egy kiadási évet"))
                mufajka = input("adja meg a műfajt")
                leiras = input("irjon le valamit a műről")
                címek[cim]={"Kiadási év:",kiadas,",műfaj",mufajka, "leírás:", leiras}
            szotar[szerzo] = címek


for i, j in szotar.items():
    print(i, ":", j)
