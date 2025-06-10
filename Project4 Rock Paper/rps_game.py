import random

options = ["rock", "paper", "scissors"]
comp_choice = options[random.randint(0, 2)]

win_msg = "Computer chooses " + comp_choice + ", you win!!"
draw_msg = "Computer chooses " + comp_choice + ", it's a draw"
lose_msg = "Computer chooses " + comp_choice + ", you lose!"


player_choice = input("What do you chose? ROCK, PAPER or SCISSORS?\n").upper()

if player_choice == "ROCK":
    if comp_choice == "rock":
        print(draw_msg)
    elif comp_choice == "paper":
        print(lose_msg)
    elif comp_choice == "scissors":
        print(win_msg)

elif player_choice == "PAPER":
    if comp_choice == "rock":
        print(win_msg)
    elif comp_choice == "paper":
        print(draw_msg)
    elif comp_choice == "scissors":
        print(lose_msg)

elif player_choice == "SCISSORS":
    if comp_choice == "rock":
        print(lose_msg)
    elif comp_choice == "paper":
        print(win_msg)
    elif comp_choice == "scissors":
        print(draw_msg)

elif player_choice == "DRAGON":
    print("Dragons always win, well done!")

else:
    print("You fail to even type correctly, computer wins")
