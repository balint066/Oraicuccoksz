ember = {"név":"Géza",
         "születési_év":1999,
         "lakhely":"Makkoshotyka",
         "foglalkozás":"szarvasmarha-tenyésztő",
         "szemei_száma":2,
         "kedvenc_lottószámok":[1,2,3,4,5]
         }
print(ember.keys())
for i in ember.values():
    print(i)

for i in ember.keys():
    print(i, ":", ember[i])

print(ember["név"])

ember["kutya"]="Bodri"
print(ember)

ember.pop("szemei_száma")
print(ember)

ember["születési_év"]=1980
print(ember)