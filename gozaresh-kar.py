x = input("").split()
nb = int(x[0])
maye = int(x[1])
sb = int()
for i in range(nb):
    hb = int(input(""))
    sb += hb
if sb >= maye:
    print("YES")
else:
    print("NO")