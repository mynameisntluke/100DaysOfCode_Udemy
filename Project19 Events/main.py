from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def print_stuff():
    print("stuff")
    timmy.forward(100)

def draw_fwd(dist = 25):
    timmy.forward(dist)

def draw_bck(dist = 25):
    timmy.backward(dist)

def turn_left(deg = 10):
    timmy.left(deg)

def turn_right(deg = 10):
    timmy.right(deg)

def reset():
    timmy.home()
    timmy.clear()

screen.listen()
screen.onkey(key = "space", fun = print_stuff)
screen.onkey(key = "w", fun = draw_fwd)
screen.onkey(key = "s", fun = draw_bck)
screen.onkey(key = "a", fun = turn_left)
screen.onkey(key = "d", fun = turn_right)
screen.onkey(key = "c", fun = reset)

screen.onkeypress(key = "w", fun = draw_fwd)
screen.onkeypress(key = "s", fun = draw_bck)
screen.onkeypress(key = "a", fun = turn_left)
screen.onkeypress(key = "d", fun = turn_right)

screen.exitonclick()
