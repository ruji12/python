import turtle

screen = turtle.Screen()
screen.title("U.S States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

import pandas
data = pandas.read_csv("50_states.csv")
text_data=data.state.to_list()
guessed_states=[]

while len(guessed_states)<50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 correct states", prompt="What's another state name?")
    title_cased_text= answer_state.title()
    print(title_cased_text)

    if title_cased_text in text_data:
        guessed_states.append(title_cased_text)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state == title_cased_text]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(title_cased_text)






screen.exitonclick()