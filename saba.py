import math
x = input("").split()
n = int(x[0])
k = int(x[1])
a = n
for _ in range(k):
    a/=2
r = math.floor(a)
print(r)