def can_sit_safely(m, seats):
    n = len(seats)

    # بررسی اولیه: اگر تعداد کل صندلی‌ها کمتر از تعداد دانش‌آموزان باشد، حتما می‌توانند با حداقل یک صندلی فاصله اجتماعی بنشینند
    if n < m:
        return "safe"

    # بررسی اگر تمامی دانش‌آموزان جدید به تعداد صندلی‌های خالی جا داشته باشند
    if m <= seats.count(0):
        return "safe"

    # بررسی اگر حداقل یک صندلی خالی بین هر دو دانش‌آموز جدید وجود داشته باشد
    for i in range(n - 1):
        if seats[i] == seats[i + 1] == 0:
            return "safe"

    # بررسی اگر میان دانش‌آموزان قدیمی یک صندلی خالی وجود داشته باشد
    for i in range(n - 2):
        if seats[i] == seats[i + 2] == 0:
            return "safe"

    # بررسی اگر بین دانش‌آموزان جدید یک صندلی خالی وجود داشته باشد
    for i in range(m - 1):
        if seats[i] == seats[i + 1] == 0:
            return "safe"

    return "danger"


# ورودی را دریافت کنیم
m = int(input())
seats = list(map(int, input().split()))

# نتیجه را چاپ کنیم
result = can_sit_safely(m, seats)
print(result)
