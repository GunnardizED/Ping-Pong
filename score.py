from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.goto(-30, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.l_score} : {self.r_score}", align=ALIGNMENT, font=FONT)

    def increase_l_score(self):
        self.l_score +=1
        self.clear()
        self.update_scoreboard()

    def increase_r_score(self):
        self.r_score +=1
        self.clear()
        self.update_scoreboard()



