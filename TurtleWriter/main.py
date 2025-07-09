from turtle import Turtle, Screen

from timmy import Timmy

#TODO 1 First six letters
#TODO 2 User can type and then have their input processed
#TODO 3 Multiple classes


timmy = Timmy()

screen = Screen()



def init_pos():
    timmy.penup()
    timmy.goto(-200, 200)
    timmy.pendown()



init_pos()

timmy.draw_c()


screen.exitonclick()
