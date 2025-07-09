from chemistry_app import ChemApp
import random

#TODO 1 Make other User choices active again
#TODO 2: User can chose how many elements they want in the __init__ phase

LIVES = 10
chem = ChemApp()

def run_app():
    running = True

    print("Welcome")
    print("Chose game mode.")

    while running:
        user_choice = display_options()


        if user_choice == 1:
            guess_the_element_name()
        # elif user_choice == 2:
        #     guess_the_symbol_name()
        # elif user_choice == 3:
        #     review()
        # elif user_choice == 4:
        #     settings()
        # elif user_choice == 5:
        #     running = False
        else:
            print("Sorry incorrect input")

def guess_the_element_name(debug = False):
    lives = LIVES
    correct = 0

    # A list of chemical symbols
    print(f"You have {lives} lives to correctly guess the chemical name from "
          f"the given chemical symbol. To quit type QUIT any time.")
    while lives > 0 and correct < 10:
        chem.set_random_element()
        # A random chemical name. User must guess
        print(f"Lives: {lives}/10    Correct {correct}/10")
        if debug:
            print(chem.get_current_element_name())
        user_resp = input(f"{chem.get_current_element_symbol()}: ")
        if user_resp.lower() == chem.get_current_element_name().lower():
            print("Correct\n")
            correct += 1
            # Remove from list
            chem.delete_current_element()
        elif user_resp == "QUIT":
            lives = -5
        else:
            print(f"WRONG. {chem.get_current_element_symbol()} is the symbol for the element {chem.get_current_element_name()}.\n")
            lives -= 1


    if lives == 0:
        print("You lost. Too bad.\n")
    if lives == -5:
        print("Returning to main menu.\n")
    else:
        print("Well done! You won!\n")


def display_options():
    """gives user all available choices and returns user input, if input is invalid returns 'wrong' """
    user_choice = input("1) Guess the correct Element from its symbol\n"
                        "2) Guess the correct Symbol from its chemical name\n"
                        "3) For review\n"
                        "4) Settings\n"
                        "5) Exit\n")
    try:
        user_choice = int(user_choice)
    except:
        user_choice = "wrong"

    return user_choice

run_app()