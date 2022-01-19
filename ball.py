from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("white")
        self.xmove = 10
        self.ymove = 10
        self.ballspeed= 0.1
    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def wallbounce(self):
        self.ymove = -1 * self.ymove
    def paddlebounce(self):
        self.xmove = -1 * self.xmove
        self.ballspeed*= 0.9

    def resetposition(self):
        self.goto(0,0)
        self.ballspeed=0.1
        self.paddlebounce()