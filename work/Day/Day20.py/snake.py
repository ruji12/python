from turtle import Turtle
starting_positions=[(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT= 0



class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        
        for positions in starting_positions:
            self.add_segment(positions)

    def add_segment(self,positions):
        tim=Turtle()
        tim.shape("square")
        tim.color("white")
        tim.penup()
        tim.goto(positions)
        self.segments.append(tim)
        

    def extend(self):
        #add a new segment to the snake
        self.add_segment(self.segments[-1].position())
    

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(20)

    def reset(self):
        for seg in self.segments:
            self.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]



    def moveup(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def movedown(self):
         if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def moveleft(self):
         if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def moveright(self):
         if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)




