himnusz = []
uressor = []
with open("himnusz.txt","r" ,encoding ="utf-8") as file:
    for sor in file:
        himnusz.append(sor.strip())
print(himnusz)
print(len(himnusz))
db = 0
for i in himnusz:
     if i != "":
         db = db + 1
print(db)
for i in himnusz:
