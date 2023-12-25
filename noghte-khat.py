x = input().split()
a1=x[0]
a2=x[1]
b1=x[2]
b2=x[3]
if a1==a2==b1==b2:
    print("Try again")
elif a1==b1:
    print("Vertical")
elif a2==b2:
    print("Horizontal")
else:
    print("Try again")
