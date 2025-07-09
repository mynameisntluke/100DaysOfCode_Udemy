from turtle import Turtle, Screen
import random
from racer import TurtleRacer

#TODO 1 Give speed to actual turtle in turtle class
#TODO 2 Add a commentator
#TODO 3 Writer has own class
#TODO 4 Draw finish line

WIDTH = 600
HEIGHT= 600

turtles = []

screen = Screen()
screen.setup(WIDTH, HEIGHT)

writer = Turtle()
writer.hideturtle()
writer.penup()
writer.goto(0, 270)

def add_racers():
    """Resets turtle list to a blank list and then adds the six turtles"""
    names = ["Kiwi", "Gary", "Bob", "Timmy", "Chip", "Jarvis"]
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    global turtles
    turtles = []
    for i in range(6):
        new_turtle = TurtleRacer(names[i], colors[i])
        new_turtle.goto(-WIDTH / 2 + 20, HEIGHT / 2 - 60 - (90 * i))
        turtles.append(new_turtle)


def play_race():
    bet_prompt = ("Chose your turtle:\n  Kiwi (Red Turtle)\n  Gary (Orange Turtle)\n  Bob (Yellow Turtle)  \n  Timmy (Green Turtle)\n  Chip (Yellow Turtle)\n  Jarvis (Purple Turtle)")
    bet = screen.textinput(title = "Turtle Racing", prompt = bet_prompt).lower()
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
            if bet == turtle.pencolor() or bet == turtle.return_name():
                print("Your turtle wins!")
                writer.write(f"Your turtle wins", False, "center", ("Courier", 18, "bold"))
            else:
                print("Your turtle lost!")
                writer.write(f"{turtle.return_name()} wins", False, "center", ("Courier", 18, "bold"))

            return True
    return False


add_racers()
play_race()

screen.listen()
screen.exitonclick()
