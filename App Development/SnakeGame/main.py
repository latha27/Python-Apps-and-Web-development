from turtle import Screen
from snake import SnakeBody
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
snake = SnakeBody()
food = Food()
score = ScoreBoard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.listen()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move_snake()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        snake.reset()
        score.score_reset()

    for seg in snake.all_turtle:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 4:
            score.score_reset()