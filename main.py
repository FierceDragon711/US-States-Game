import pandas as pd
import turtle

data = pd.read_csv("50_states.csv")
states = data.state.tolist()
screen = turtle.Screen()
image = "blank_states_img.gif"
screen.title("US STATE GAME")
screen.addshape(image)
turtle.shape(image)
guessed_state = []
while len(guessed_state) < 50:
    answer_prompt = (screen.textinput(title=f"{len(guessed_state)}/50 Correct Guess The State", prompt="Whats your guess ")).title()
    if answer_prompt == "Exit":
        missed_states = [state for state in states if state not in guessed_state]
        df = pd.DataFrame(missed_states)
        df.to_csv("States_To_Learn")
        break
    if answer_prompt in states:
        guessed_state.append(answer_prompt)
        text = turtle.Turtle()
        text.penup()
        text.hideturtle()
        x_cor = int(data[(data.state == answer_prompt)].x)
        y_cor = int(data[(data.state == answer_prompt)].y)
        text.goto(x_cor, y_cor)
        text.write(f"{answer_prompt}")

