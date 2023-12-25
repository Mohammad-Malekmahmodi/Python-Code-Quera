def find_next_power_of_two(n):
    power_of_two = 1
    while power_of_two <= n:
        power_of_two *= 2
    print(power_of_two)

# خواندن عدد n
n = int(input())

# فراخوانی تابع با استفاده از عدد n
find_next_power_of_two(n)
