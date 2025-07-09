from turtle import Turtle

class Timmy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.speed("slow")

    def next_letter(self, join=True):
        if join:
            self.penup()
        self.setheading(0)
        self.forward(10)
        self.pendown()

    def draw_a(self):
        self.left(90)
        self.forward(20)
        self.left(180)
        self.forward(10)
        self.left(90)
        self.forward(20)
        self.left(90)
        self.forward(10)
        self.left(90)
        self.forward(20)
        self.left(180)
        self.forward(20)
        self.right(90)
        self.forward(20)

    def draw_b(self):
        self.draw_a()
        self.right(90)
        self.forward(20)
        self.right(180)
        self.forward(20)

    def draw_c(self):
        self.left(90)
        self.forward(20)
        self.right(90)
        self.forward(20)

        self.right(180)
        self.forward(20)
        self.left(90)
        self.forward(20)
        self.left(90)
        self.forward(20)

    def draw_d(self):
        pass