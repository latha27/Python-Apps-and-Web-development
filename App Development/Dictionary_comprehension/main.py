import random
names = ["alex", "deepa", "pavitra", "shalini", "Latha", "jalaja"]

student_details = {student: random.randint(1, 100) for student in names}

passed_students = {student: score for (student, score) in student_details.items() if score >= 60}
#print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
word_in_sentence = sentence.split()
result = {word: len(word) for word in word_in_sentence}

#print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {key: round((value*1.8)+32, 2) for (key, value) in weather_c.items()}

#print(weather_f)

