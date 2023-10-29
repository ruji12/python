from turtle import Turtle


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.start_new()
        self.setheading(90)


    def go_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(),new_y)

    def start_new(self):
        self.goto(0,-280)
        

    def go_to_finish_line(self):
        if self.ycor()>280:
            return True
        else:
            return False



    


