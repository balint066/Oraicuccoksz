def harommal_oszthatok(lista):
    db = 0
    for i in lista:
        if i%3==0:
            db = db+1
    return db

def negativ_(szam):
    if szam < 0:
        return True
    else:
        return False
ureslista = []
while True:
    adottszam = int(input())
    if negativ_(adottszam):
        break
    else:
        ureslista.append(adottszam)
db = harommal_oszthatok(ureslista)
print(db)