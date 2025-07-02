import random

from quotes import quotes

options_str = ("1) For a random quote\n"
               "2) To exit\n")

def run_app(debug = True):
    running = True
    while running:
        user_resp = get_user_input()
        if user_resp == 1:
            print_random_quote()
            #TODO 1: Remove quote
        elif user_resp == 2:
            running = close_app()
        elif user_resp == 999:
            print("Please enter a number.\n")
        else:
            print("Sorry that option was not recognized.\n")


def get_user_input():
    global options_str

    try:
        user_input = int(input(options_str))
    except:
        user_input = 999

    return user_input

def print_random_quote():
    """Prints one random quotes from quotes and then deletes it"""
    ref = random.randint(1, len(quotes))
    print(f"\n\t\"{quotes[ref]['quote']}\" \n\t\t-{quotes[ref]['author']}\n")
    remove_quote(ref)

def remove_quote(ref):
    del quotes[ref]

def close_app():
    print("Goodbye. Stay Wise.")
    return False



run_app()