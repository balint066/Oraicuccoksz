for i in range(1,6,1):
    print("Adjon meg egy számot")
    elsoszam = float(input())

    if elsoszam == 0:
        print("Adja meg a kör sugarát")
        a = float(input())
        negyzet = a*a
        kerulet = 2*3.14*a
        terulet = 3.14*negyzet
        sugar = a
        print("A kör opciót választotta")
        print("A kör sugara:",sugar)
        print("A kör területe:",terulet)
        print("A kör kerülete:",kerulet)
    elif elsoszam % 2 == 0:
        print("A négyzet opciót választotta A", elsoszam, "páros szám. A szám négyzete:", elsoszam**2,)
    else:
        print("Nincs ilyen opció")