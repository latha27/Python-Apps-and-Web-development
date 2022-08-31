from turtle import Turtle
import random
COLORS = ["red", "blue", "pink", "green", "yellow", "brown"]
num = [1, 2, 3, 4, 5, 6]
MOVE_DISTANCE = 10


class CarCreate:
    def __init__(self):
        self.cars = []

    def create_car(self):
        rand_num = random.randint(0, 8)
        if rand_num == 1:
            tim = Turtle()
            tim.shape("square")
            tim.setheading(180)
            tim.shapesize(0.7, 3)
            tim.color(random.choice(COLORS))
            tim.penup()
            random_x = 370
            random_y = random.randint(-300, 300)
            tim.goto(random_x, random_y)
            self.cars.append(tim)

    def move_car(self):
        for car in self.cars:
            car.forward(MOVE_DISTANCE)











