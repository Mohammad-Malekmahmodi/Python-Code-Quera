xxx = input("").split()
start = int(xxx[0])
finish = int(xxx[1])
limit = int(xxx[2])
x = int(xxx[3])

if x == start:
    print(limit)
elif x < start:
    print("exam did not started!")
elif start < x < finish:
    xx = finish - x
    if xx <= limit:
        print(xx)
    else:
        print(limit)
elif x >= finish:
    print("exam finished!")
