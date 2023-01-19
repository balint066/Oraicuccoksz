hőm=[]
for i in range(1, 31):
    ho = float(input("Adjon meg hőmérsékletet a (z) " + str(i) + ". napon:" ))
    hőm.append(ho)
atlag = sum(hőm)/len(hőm)
minimum = min(hőm)
maxElem = hőm[0]
for i in range(1, len(hőm)):
    if hőm[i] > maxElem:
        maxElem = hőm[i]
fagy = []
for i in hőm:
    if i < 0:
        fagy.append(i)
    fagyszam = len(fagy)

print("Az átlagos hőmérséklet: ",atlag,"C°")
print("A legkisebb hőmérésklet: ", minimum,"C°")
print("A legmelegebb hőmérséklet:",maxElem,"C°. Ezt a",hőm.index(maxElem)+1,".dik napon mérték")
print(fagyszam, "napon fagyott.")