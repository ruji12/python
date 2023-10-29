from turtle import Turtle
import random


timmy = Turtle()
colors = ["cyan","royal blue","lime green","gold","magenta","rosy brown","pink","indigo","dark magenta","salmon","violet"	]



def draw_shapes(num_sides): 
    angle = 360  / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shape_size in range(3,11):
    timmy.color(random.choice(colors))
    draw_shapes(shape_size)

        