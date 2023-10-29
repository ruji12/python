from turtle import Turtle ,Screen
import random
 

is_bet=False
screen = Screen()

screen.setup(width=500,height=400)
user_bet=screen.textinput(title="turtle races!", prompt="who do you think will win this game?Please insert color:")
colors=["black","green","red","blue","purple","purple"]
y_position=[-70,-40,10,40,70,100]
all_turtles=[]
# screen.exitonclick()

for turtle_index in range(0,6):
    tim=Turtle()
    tim.shape("turtle")
    tim.speed("fastest")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-230,y=y_position[turtle_index])

    all_turtles.append(tim)

if user_bet:
    is_bet=True

while is_bet:
    for turtle in all_turtles:
    
        if turtle.xcor() > 230:
            is_bet=False
            winner_turtle=turtle.pencolor()
            if winner_turtle == user_bet:
                print(f"you've won the game {winner_turtle} turtle is a winner!")

            else:
                print(f"you are wrong , {winner_turtle} turtle is a winner!")

    
    
    
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)





screen.exitonclick()


