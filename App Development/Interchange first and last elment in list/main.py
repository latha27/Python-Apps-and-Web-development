list_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

temp = list_a[0]
list_a[0] = list_a[-1]
list_a[-1]=temp
print(list_a)