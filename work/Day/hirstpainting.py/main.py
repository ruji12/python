from turtle import Turtle,Screen
import turtle
import random

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124),(140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (174, 94, 97), (176, 192, 209)]

no_of_dots = 100



timmy = Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
turtle.colormode(255)

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)



for dot_count in range (1,no_of_dots+1):
    timmy.dot(30,random.choice(color_list))
    timmy.forward(50)
    if dot_count %  10 ==0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


    


screen = Screen()
screen.exitonclick()