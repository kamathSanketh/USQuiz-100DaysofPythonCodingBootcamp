import turtle
import pandas
data = pandas.read_csv("50_states.csv")
states = data["state"]
x = data["x"]
y = data["y"]
leftStates = list(data["state"])

screen = turtle.Screen()
screen.title("United States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title="You have guessed " + f"{len(guessed_states)}/50 states", prompt="What's another state")
    answer_state = answer_state.lower()
    if answer_state == "exit":
        new_data = pandas.DataFrame(leftStates)
        new_data.to_csv("states_to_learn.csv")
        break;
    for a in range(0, len(states)):
        if answer_state == states[a]:
            temp = turtle.Turtle()
            temp.hideturtle()
            temp.penup()
            temp.goto(x[a], y[a])
            temp.pendown()
            temp.write(states[a])
            guessed_states.append(states[a])
            leftStates.remove(states[a])




