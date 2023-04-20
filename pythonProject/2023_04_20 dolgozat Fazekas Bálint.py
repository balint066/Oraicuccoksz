import copy
konyvtar={}
zenek=[]
zenehossz=[]
with open("playlist.csv","r",encoding="utf-8") as file:
    for sor in file:

        konyvtar["eloado"]= sor.strip().split(";")[0]
        konyvtar["cim"]= sor.strip().split(";")[1]
        konyvtar["mufaj"]= sor.strip().split(";")[2]
        konyvtar["hossz"]= int(sor.strip().split(";")[3])
        zenek.append(copy.deepcopy(konyvtar))
        zenehossz.append(sor.strip().split(";"))
print(zenek)
print(zenehossz)

for i in range(len(zenehossz)):
    zenehossz[i][3]= int(zenehossz[i][3])

#for i in zenek:
#   zenehossz.append(zenek[i][3])
#print(zenehossz)

def teljes_hossz(lista):
    hossz=0
    for i in lista:
        hossz=i[3]+hossz
    return hossz
hosszmp=(teljes_hossz(zenehossz))
hosszp0=round(hosszmp/60)-1
hosszmp2=hosszmp-hosszp0*60
hosszmp2=str(hosszmp2)
hosszp0=str(hosszp0)
hosszp=hosszp0+","+hosszmp2
print(hosszp)
with open("02_hossz.txt","w",encoding="utf-8") as celfile:
    celfile.write("A lejatszasi lista hossza:"+hosszp0+"perc"+hosszmp2+"másodperc")