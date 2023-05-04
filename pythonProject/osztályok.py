import tegla_c

T1 = tegla_c.Kor(int(input("adja meg az r-t")))
T5 = tegla_c.Teglalap(int(input("A oldal")), int(input("B oldal")))


print(T5.kiir())
print(T1.kkir())
