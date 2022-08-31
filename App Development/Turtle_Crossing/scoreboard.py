from turtle import Turtle
FONT = 'Arial', 25, 'normal'


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-350, y=280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level = {self.level}", align="left", font=FONT)

    def increase_score(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)




