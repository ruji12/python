from turtle import Turtle,Screen
import random
import turtle





turtle.colormode(255)
timmy = Turtle()

def colors():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color = (r,g,b)
    return(random_color)

def draw_spirograph(no_of_gaps):
    for _ in range(int(360/no_of_gaps)):
        timmy.circle(100)
        timmy.speed("fastest")
        timmy.color(colors())

        timmy.setheading(timmy.heading() + no_of_gaps)


draw_spirograph(5)

screen=Screen()
screen.exitonclick()

   


  


