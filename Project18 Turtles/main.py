import turtle
from turtle import Turtle, Screen
import random
import colorgram

timmy = Turtle()
screen = Screen()

turtle.colormode(255)
screen.bgcolor((240, 240, 240))


def timmy_settings(pensize = 6, speed = "fast"):
    timmy.shape("turtle")
    timmy.pensize(pensize)
    timmy.speed(speed)

    timmy.pendown()


def set_random_color():
    """Returns a tuple with a random valid RGB color"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def start_timmy_at_the_edge(x = -210, y = 190):
    """Moves timmy to the top left corner"""
    timmy.penup()
    timmy.setpos(-210, 190)
    timmy.pendown()


def timmy_gets_drunk(n = 150, m = 20):
    """Timmy goes on a random walk of n steps each of length m"""
    for i in range(n):
        timmy.color(set_random_color())
        turn = random.randint(0, 3)
        timmy.right(90 * turn)
        timmy.forward(m)
    return True


def timmy_makes_spiro(size_of_gap, radius = 30):
    for i in range(int(360/size_of_gap)):
        timmy.color(set_random_color())
        timmy.circle(radius)
        timmy.setheading(timmy.heading() + size_of_gap)


def timmy_does_a_circle(radius = 10):
    """Timmy draws one circle and returns to his initial position. Increase size by changing radius"""
    for n in range(40):
        timmy.forward(radius)
        timmy.right(360/40)


def get_rgb_list():
    rgb_list = []
    colors = colorgram.extract("mario.jpg", 20)
    for color in colors:
        rgb_list.append((color.rgb.r, color.rgb.g, color.rgb.b))
    return rgb_list


def timmy_does_hirst():
    # use get_rgb_list once and copy and paste the list
    rgb_list = [(0, 95, 173), (222, 144, 107), (176, 9, 6), (250, 209, 170), (243, 51, 44), (207, 49, 25), (3, 12, 47), (17, 42, 159), (70, 172, 55), (254, 210, 0), (248, 33, 36), (191, 7, 11), (48, 89, 232), (31, 6, 11), (1, 158, 219), (252, 214, 31), (119, 167, 206), (197, 165, 18)]

    timmy.penup()
    timmy.setpos(-220, -220)
    for y in range(10):
        for x in range(10):
            timmy.pendown()
            timmy.dot(20, random.choice(rgb_list))
            timmy.penup()
            timmy.forward(50)
        timmy.right(180)
        timmy.forward(500)
        timmy.right(90)
        timmy.forward(50)
        timmy.right(90)

    # excitement
    for z in range(80):
        timmy.right(270)



timmy_settings(pensize = 2, speed = "fastest")
# timmy_makes_spiro(size_of_gap = 4, radius = 100)
timmy_does_hirst()

screen.exitonclick()
