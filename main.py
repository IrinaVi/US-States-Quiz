import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
list_of_states = data.state.to_list()
right_answers = []
style = ("Roboto", 15, "normal")
game_is_on = True


while len(right_answers) < 50:
    answer = screen.textinput(title=f"{len(right_answers)}/50 States Correct", prompt="Enter state name or "
                                                                                      "enter 'EXIT to quit the game'").title()
    if answer == "Exit":
        break
    for state in list_of_states:
        if answer == state:
            right_answers.append(answer)
            state_row = data[data.state == answer]
            x_pos = int(state_row.x)
            y_pos = int(state_row.y)
            new_turtle = turtle.Turtle()
            new_turtle.hideturtle()
            new_turtle.penup()
            new_turtle.goto(x_pos, y_pos)
            new_turtle.write(answer, font = style)

missing_states = [state for state in list_of_states if state not in right_answers]

print(f"Missing states: {missing_states}")

data = pandas.DataFrame(missing_states)
data.to_csv("missing states.csv")