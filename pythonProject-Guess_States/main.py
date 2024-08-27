import turtle
import pandas
screen=turtle.Screen()
screen.title("India States Game")
screen.setup(width=600, height=600)
image="indian map (1).gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)

data=pandas.read_csv("states coordinates - Sheet1.csv")
guessed_states = []
while len(guessed_states) < len(data):
    answer_state = screen.textinput( title=f"{len(guessed_states)}/{len(data)} States Correct",
        prompt="Give the name of an Indian state (or type 'exit' to quit)"
    )

    if answer_state is None or answer_state.lower() == 'exit':
        turtle.bye()
        break

    answer_state = answer_state.title()

    if answer_state in data["state"].values and answer_state not in guessed_states:

        state_data = data[data["state"] == answer_state]
        x = int(state_data.x.iloc[0])  # Use .iloc[0] to avoid the FutureWarning
        y = int(state_data.y.iloc[0])  # Use .iloc[0] to avoid the FutureWarning

        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        pen.goto(x, y)
        pen.write(answer_state, align="center", font=("Arial", 8, "normal"))

        guessed_states.append(answer_state)

turtle.mainloop()