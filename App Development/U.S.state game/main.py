import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/ 50 states correct",
                                    prompt="What's another state's name?").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        tim = turtle.Turtle()
        tim.color("black")
        tim.hideturtle()
        tim.penup()
        data = states_data[states_data.state == answer_state]
        tim.goto(int(data.x), int(data.y))
        tim.write(answer_state)





screen.exitonclick()