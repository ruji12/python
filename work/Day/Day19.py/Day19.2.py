import turtle

# Create a screen
screen = turtle.Screen()

# Create a turtle
t = turtle.Turtle()


def move_forward():
    t.forward(10)


screen.onkey(key="w", fun=move_forward)
screen.listen()
screen.mainloop()