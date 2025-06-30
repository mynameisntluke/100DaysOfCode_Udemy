import random
from elements import elements


def run_app():
    print("Welcome")
    guess_the_element_name()
    print("Goodbye")

def guess_the_element_name():
    """Give user the element symbol, user must guess
    the name, the winning condition is ten correct
    answers, the losing condition is ten incorrect """
    lives = 10
    correct = 0
    symbols = list(elements.keys())
    while lives > 0 and len(symbols) > 20:
        symbol = symbols[random.randint(0, len(symbols)-1)]
        user_resp = input(f"{symbol}: ")
        if user_resp.lower() == elements[symbol].lower():
            print("Correct")
            correct += 1
            # Remove from list
        else:
            print(f"The correct answer was {elements[symbol]}")
        lives -= 1

def answer_the_symbol_name():
    pass


run_app()