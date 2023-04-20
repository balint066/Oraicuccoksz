te=[]
with open("autok.csv","r",encoding="utf-8")as file:
    for sor in file:
        te.append(sor.strip().split(";"))


te=te[1:]

for i in te:
    i[4]=int(i[4])

hel=0

for i in te:
    if i[0] == "Munkács" and i[1] == "Záhony":

        hel= hel + i[4]

print(hel)



