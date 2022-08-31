from turtle import Screen
from player import CreateTurtle
from car import CarCreate
from scoreboard import ScoreBoard
import random
import time

screen = Screen()
screen.screensize(canvwidth=600, canvheight=600)
screen.bgcolor("white")
screen.tracer(0)
shape = CreateTurtle()
car = CarCreate()
score = ScoreBoard()


screen.onkey(shape.go_up, "Up")
screen.listen()


is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()

    for cars_sub in car.cars:
        if cars_sub.distance(shape) < 20:
            is_game_on = False
            score.game_over()

    if shape.ycor() > 290:
        shape.start_position()
        score.increase_score()


