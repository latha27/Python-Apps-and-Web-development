from turtle import Screen, Turtle
import time
import random
COLORS = ["red", "black", "orange", "green", "pink", "blue"]
random_x = -370
Y_COORDINATE = [-80, -50, -20, 10, 40, 70]


screen = Screen()
screen.screensize(canvwidth=400, canvheight=400)
user_bet = screen.textinput(title="Make your bet", prompt= "Which turtle will win the race? Enter the color?")
screen.tracer(0)

all_turtle = []

for turtle_index in range(0, 6):
    tim = Turtle("turtle")
    tim.color(COLORS[turtle_index])
    tim.penup()
    tim.goto(random_x, Y_COORDINATE[turtle_index])
    all_turtle.append(tim)

if user_bet:
    is_race_on = True
while is_race_on:
    time.sleep(0.1)
    screen.update()

    for position in all_turtle:
        rand_distance = random.randint(0, 18)
        position.forward(rand_distance)

    for position in all_turtle:
        if position.xcor() > 310:
            is_race_on = False
            winning_turtle = position.pencolor()
            if winning_turtle == user_bet:
                print(f"Game over, you win. The winning turtle is {winning_turtle}")
            else:
                print(f"Game over, You loose.The winning turtle is {winning_turtle}")





