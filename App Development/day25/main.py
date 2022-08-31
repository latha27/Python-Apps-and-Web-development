# with open("./weather_data.csv", mode="r") as weather:
#    weather_data = weather.readlines()
#    print(weather_data)

# import csv
# with open("weather_data.csv") as weather:
#    data = csv.reader(weather)
#    temperature = []
 #   for row in data:
 #       if row[1] != 'temp':
#            temperature.append(int(row[1]))
#    print(temperature)

#import pandas
#data = pandas.read_csv("weather_data.csv")
#temp_list = data["temp"].tolist()
#print(temp_list)
#count = 0
#for num in temp_list:
#    count = count + num
#
#average = count / len(temp_list)
#print(average)
import csv

import pandas
#data = pandas.read_csv("weather_data.csv")
## print(data["temp"].max())
## print(data["temp"].mean())
## print(data[data.temp == data.temp.max()])
#monday = data[data.day == "Monday"]
## print(monday.condition)
#degree = monday.temp
#print(degree)
#fahrenheit = (degree * 1.8) + 32
#print(fahrenheit)

#data_dict = {
 #   "students": ["Latha", "Geetha", "Priya", "Shobha"],
 #   "marks": [75, 85, 65, 95]
#}

#data = pandas.DataFrame(data_dict)
#data.to_csv("new_dict.csv", mode="w")

data = pandas.read_csv("Squirrel_Data.csv")
#print(data)
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
print(gray_squirrel_count)
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(red_squirrel_count)
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_output.csv")
