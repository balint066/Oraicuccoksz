szam = -3
vege = 0

while vege != -1:
    while szam < 0:
        szam = float(input("Adja meg a mértek számát:"))
        mertekegyseg = input("Adja meg a mértértékegységet: cm, m, km")
        valto = input("Adja meg hogy mibe váltsuk át: cm, m, km")

    if mertekegyseg == "cm" and valto == "cm":
        print("Az átváltás:",szam,"Cm")
    elif mertekegyseg == "cm" and valto == "m":
            print("Az átváltás:",szam/100 ,"M")
    elif mertekegyseg == "cm" and valto == "km":
        print("Az átváltás:",szam/100000,"Km")
    elif mertekegyseg == "m" and valto == "cm":
        print("Az átváltás:", szam*100, "cm")
    elif mertekegyseg == "m" and valto =="m":
        print("Az átváltás:", szam, "m")
    elif mertekegyseg == "m" and valto == "km":
        print("Az átváltás:", szam / 1000, "Km")
    elif mertekegyseg == "km" and valto == "cm":
        print("Az átváltás:", szam*100000, "cm")
    elif mertekegyseg == "km" and valto == "m":
        print("Az átváltás:", szam*1000, "Km")
    elif mertekegyseg == "km" and valto =="km":
        print("Az átváltás:", szam, "Km")

    vege = int(input("Szeretné folyatatni? nem =-1"))
    szam = -1