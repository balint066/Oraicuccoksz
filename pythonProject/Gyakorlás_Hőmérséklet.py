# F to C = (F-32)/18
# C to F = c*1.8+32

homerseklet = float(input("Adja meg az alap hőfokot   "))
mertekegyseg = input("Mértékegység: f,c,k    ")

if mertekegyseg == "c":
    F = homerseklet * 1.8 + 32
    K = homerseklet+273.15
    print("A hőmérséklet C°-ban", homerseklet)
    print("A hőmérséklet F°-ben", F)
    print("A hőmérséklet K°-ben", K)

elif mertekegyseg == "f":
    C = (homerseklet-32)/1.8
    K = C+273.15
    print("A hőmérséklet F°-ben", homerseklet)
    print("A hőmérséklet C°-ban", C)
    print("A hőmérséklet K°-ben", K)

elif mertekegyseg == "k":
    C = homerseklet-273.15
    F = C*1.8+32
    print("A hőmérséklet K°-ben", homerseklet)
    print("A hőmérséklet F°-ben", F)
    print("A hőmérséklet C°-ban", C)
