def is_cool_username(username):
    char_count = {}
    for char in username:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for count in char_count.values():
        if count < 2:
            return False
    return True
username = input("")
if is_cool_username(username):
    print("cool")
else:
    print("not cool")
