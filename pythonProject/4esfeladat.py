c = input("Adj meg egy szót")
h = ""
for i in range(len(c)-1,-1,-1):
    h = h+c[i]
#print(a[::-1])
print(h)
if h == c:
    print("ez egy palindrom")
else:
    print("ez egy nem palindrom")

