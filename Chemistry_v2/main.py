from chemistry_app import ChemApp
import random
from guess_element_handler import GuessElement

#TODO 1: Print highscore from .csv file

LIVES = 10
chem = ChemApp()
guess_the_element = GuessElement()

def run_app():
    running = True

    print("Welcome")
    print("Chose game mode.")

    while running:
        user_choice = display_options()


        if user_choice == 1:
            guess_the_element.guess_the_element_name()
        elif user_choice == 2:
            guess_the_element.user_chooses_level()
        elif user_choice == 3:
            running = False
        else:
            print("Sorry incorrect input")





def display_options():
    """gives user all available choices and returns user input, if input is invalid returns 'wrong' """
    user_choice = input("1) Play the game\n"
                        "2) To change the difficulty level\n"
                        "3) Exit\n")
    try:
        user_choice = int(user_choice)
    except:
        user_choice = "wrong"

    return user_choice

run_app()