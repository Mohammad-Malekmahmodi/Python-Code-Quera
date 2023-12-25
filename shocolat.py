a = input("").split()
xa = int(a[0])
xb = int(a[1])

if xa == xb:
    print("YES")
elif xa % xb == 0:
    print("YES")
else:
    print("NO")

