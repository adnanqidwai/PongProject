from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.rscore = 0
        self.lscore = 0
        self.penup()
        self.color("purple")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lscore, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("Courier", 80, "normal"))

    def lpoint(self):
        self.lscore += 1
        self.update_scoreboard()

    def rpoint(self):
        self.rscore += 1
        self.update_scoreboard()
