from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore=0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        
        # self.write(f"Score:{self.score}" ,align="center",font=("Arial",24,"normal"))
        self.hideturtle()
        self.update_score()
       


    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score}  highscore:{self.highscore}" ,align="center",font=("Arial",24,"normal"))
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER!" ,align="center",font=("Arial",24,"normal"))
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            
        self.score=0
        self.update_score()

    def increase_score(self):
        self.score += 1
        
        self.update_score()



