import csv

import pandas

numbers = [1, 2, 3]
new_list = [n+1 for n in numbers]
# print(new_list)

name = "Latha"
new_list = [letter for letter in name]
# print(new_list)

new_list = [i*2 for i in range(1, 5)]
#print(new_list)

names = ["alex", "lomb", "Geetha", "Pooja", "Santhosh", "Druva"]

short_names = [name for name in names if len(name) == 4]
#print(short_names)

changed_names = [name.upper() for name in names if len(name) >= 5]
#print(changed_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [n*n for n in numbers]
#print(squared_numbers)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:

result = [n for n in numbers if n%2 == 0]

#Write your code 👆 above:

# print(result)

with open("file1.txt") as data1:
    list_1 = data1.readlines()

with open("file2.txt") as data2:
    list_2 = data2.readlines()

result = [int(num) for num in list_1 if num in list_2]

print(result)




