from turtle import Turtle
STARTING_POSITION = [0, -300]
MOVE_DISTANCE = 10


class CreateTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("turtle")
        self.penup()
        self.start_position()

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def start_position(self):
        self.goto(STARTING_POSITION)

