from turtle import Turtle, Screen
import random

WIDTH = 600
HEIGHT= 600

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

screen = Screen()
screen.setup(WIDTH, HEIGHT)


def add_racers():
    """Resets turtle list to a blank list and then adds the six turtles"""
    global turtles
    turtles = []
    for i in range(6):
        new_turtle = Turtle("turtle")
        new_turtle.penup()
        new_turtle.goto(-WIDTH / 2 + 20, HEIGHT / 2 - 60 - (90 * i))
        new_turtle.color(colors[i])
        turtles.append(new_turtle)


def play_race():
    bet = screen.textinput(title="Turtle Racing", prompt="Chose your turtle color: ")
    racing = True


    while racing:
        fwd = random.randint(0, 10)
        random.choice(turtles).forward(fwd)
        if check_winner(bet):
            racing = False


def check_winner(bet):
    for turtle in turtles:
        if turtle.pos()[0] > 250:
            print(f"{turtle.pencolor().upper()} wins!")
            if bet == turtle.pencolor():
                print("Your turtle wins!")
            else:
                print("Your turtle lost!")
            return True
    return False


add_racers()
play_race()

screen.listen()
screen.exitonclick()
