count = int(input(""))
x = int()
for i in range(count):
    name = input("").split()
    if int(name[1]) > x:
        y = name[0]
        x = int(name[1])
print(y)
