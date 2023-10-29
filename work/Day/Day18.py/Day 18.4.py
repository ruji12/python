from turtle import Turtle,Screen
import random
import turtle

degree = [90,180,0,270]

# colours = ["violet","misty rose","pink","violet","medium purple","bisque","blue violet","orchid","pale violet red","aquamarine","light sea green","gray","mint cream"]



timmy = Turtle()
turtle.colormode(255)
def colors():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color = (r,g,b)
    return(random_color)

for _ in range(400):
    directions = [timmy.right,timmy.left]
    set_directions=random.choice(directions)
    set_directions(random.choice(degree))
    timmy.color(colors())
    
    timmy.speed(20)
    timmy.forward(40)
    timmy.pensize(10)
    


    # timmy.forward(100)
    # timmy.right(90)
# screen = Screen()
# screen.exitonclick()


