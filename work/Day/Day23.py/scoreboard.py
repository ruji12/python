from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
       
        self.level=0
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.level, align="center", font=("Courier", 80, "normal"))

    def update_level(self):
        self.clear()
        self.level +=1
        self.update_scoreboard()
        