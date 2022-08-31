
def coolest(num_int, num_coolness):
    binary_num = bin(num_int)
    result = ""
    cnt = 0
    for i, k in enumerate(binary_num):
        if (i > 1):
            result += str(k)
        if result.__contains__("101"):
            result = str(1)
            cnt += 1
    if (cnt >= num_coolness):
        return cnt

print(coolest(5, 1))

