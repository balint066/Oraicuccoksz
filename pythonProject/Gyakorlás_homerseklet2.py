# F to C = (F-32)/18
# C to F = c*1.8+32

homerseklet = float(input("Adja meg az alap hőfokot   "))
mertekegyseg = input("Mértékegység: f,c,k    ")
valt = input("Váltómértékegység: f,c,k    ")
if mertekegyseg == "c":
    if valt == "c":
        print("TE IDES HÁ E UGYAN ANNYI, NIND E", homerseklet)
    elif valt == "f":
        F = homerseklet * 1.8 + 32
        print("A hőmérséklet F°-ben", F)
    elif valt == "k":
        K = homerseklet+273.15
        print("A hőmérséklet K°-ben", K)

elif mertekegyseg == "f":
    if valt == "f":
        print("TE IDES HÁ E UGYAN ANNYI, NIND E", homerseklet)
    elif valt == "c":
        C = (homerseklet - 32) / 1.8
        print("A hőmérséklet C°-ban", C)
    elif valt == "k":
        K = ((homerseklet - 32) / 1.8)+273.15
        print("A hőmérséklet K°-ben", K)

elif mertekegyseg == "k":
    if valt == "k":
        print("TE IDES HÁ E UGYAN ANNYI, NIND E", homerseklet)
    elif valt == "f":
        F = (homerseklet-273.15) * 1.8 + 32
        print("A hőmérséklet F°-ben", F)
    elif valt == "c":
        C = homerseklet - 273.15
        print("A hőmérséklet C°-ban", C)



