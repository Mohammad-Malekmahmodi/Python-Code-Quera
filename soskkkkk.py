a, b, c, d, m = map(int, input().split())

# قیمت هر شیشه معجون در آینده برای هر نوع معجون
price_red = a + (m * c)
price_green = b + (m * d)

# مقایسه قیمت‌ها و تصمیم‌گیری
if price_red > price_green:
    print("Eyval baba!")
else:
    print("Naaa, eshtebahe!")
