def calculate_floor(string):
    current_floor = 0  # ما از طبقه‌ی همکف شروع می‌کنیم

    for move in string:
        if move == 'U':
            current_floor += 1  # حرکت به طبقه‌ی بالاتر
        elif move == 'D':
            current_floor -= 1  # حرکت به طبقه‌ی پایین‌تر

    return current_floor

# نمونه تست
print(calculate_floor('UUDU'))  # خروجی باید 2 باشد
print(calculate_floor('DDDD'))  # خروجی باید -4 باشد
