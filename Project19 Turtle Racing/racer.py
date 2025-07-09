from turtle import Turtle

class TurtleRacer(Turtle):
    def __init__(self, name, color):
        super().__init__()

        self.penup()
        self.shape("turtle")
        self.name = name

        self.color(color)

    def return_name(self):
        """Returns name of turtle"""
        return self.name