import random
from prettytable import PrettyTable
#TODO 2: Expand element list(currently only contains first 60)
from elements import elements


def run_app():
    running = True
    print("Welcome")
    print("Chose game mode.")
    while running:
        user_choice = input("1) Guess the correct Element from its symbol\n"
              "2) Guess the correct Symbol from its chemical name\n"
              "3) For review\n"
              "4) Exit\n")

        #TODO 5: make a proper try-except clause
        try:
            user_choice = int(user_choice)
        except:
            print("Please enter a number.")

        if user_choice == 1:
            guess_the_element_name()
        elif user_choice == 2:
            guess_the_symbol_name()
        elif user_choice == 4:
            running = False
        elif user_choice == 3:
            review()
        elif user_choice == 5:
            settings()
        else:
            print("Sorry incorrect input")

    print("Goodbye")

def guess_the_element_name(debug = False):
    """Give user the elements symbol, user must guess
    the name, the winning condition is ten correct
    answers, the losing condition is ten incorrect """
    lives = 10
    correct = 0
    # A list of chemical symbols
    symbols = list(elements.keys())
    print(f"You have {lives} lives to correctly guess the chemical name from "
          f"the given chemical symbol. To quit type QUIT any time.")
    while lives > 0 and correct < 10:
        # A random chemical name. User must guess
        symbol = symbols[random.randint(0, len(symbols)-1)]
        print(f"Lives: {lives}/10    Correct {correct}/10")
        if debug:
            print(symbol)
        user_resp = input(f"{symbol}: ")
        if user_resp.lower() == elements[symbol].lower():
            print("Correct\n")
            correct += 1
            # Remove from list
            symbols.remove(symbol)
        elif user_resp == "QUIT":
            lives = -5
        else:
            print(f"WRONG. {symbol} is the symbol for the element {elements[symbol]}.\n")
            lives -= 1

    if lives == 0:
        print("You lost. Too bad.\n")
    if lives == -5:
        print("Returning to main menu.\n")
    else:
        print("Well done! You won!\n")

def guess_the_symbol_name(debug = False, lives = 10, win_condition = 15):
    """Give user the elements name, user must guess
    the symbol, the winning condition is ten correct
    answers, the losing condition is ten incorrect """
    #TODO 4: Change code (currently a copy of the above game)
    lives = lives
    correct = 0
    # A list of elements tuples
    # 0 is symbol    1 is name
    elem_names = list(elements.items())

    print(f"You have {lives} lives to correctly guess the chemical symbol from "
          f"the given chemical name. To quit type QUIT any time.")

    while lives > 0 and correct < win_condition:
        # A element tuple
        elem_ref = elem_names[random.randint(0, len(elem_names)-1)]
        # A random chemical name with symbol.
        #TODO 6 Use elem_symbol
        elem_symbol = elem_ref[0]
        elem_name = elem_ref[1]

        print(f"Lives: {lives}/10    Correct {correct}/10")
        #print(f"Current tuple: {elem_ref}")
        if debug:
            print(elem_name)
        user_resp = input(f"{elem_name}: ")
        if user_resp.lower() == elem_ref[0].lower():
            print("Correct\n")
            correct += 1
            # Remove from list
            elem_names.remove(elem_ref)
        else:
            print(f"WRONG. {elem_name} has symbol {elem_ref[0]}.\n")
            lives -= 1

    if lives == 0:
        print("You lost. Too bad.\n")
    else:
        print("Well done! You won!\n")


def settings():
    #TODO 1: Implement setting
    pass

def review():
    table = PrettyTable()
    element_numbers = make_num_row(len( list(elements.keys()) ))
    table.add_column("Atomic Number", element_numbers)
    table.add_column("Name", list(elements.values())  )
    table.add_column("Symbol",  list(elements.keys())  )
    print(table)

def make_num_row(n):
    num_list = []
    for i in range(1, n+1):
        num_list.append(i)
    return num_list


run_app()