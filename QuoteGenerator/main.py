import random
#TODO 1: Nicer interface
#TODO 2: More quotes

from quote_handler import QuoteHandler

quote_handler = QuoteHandler()

def run_app(debug = True):
    running = True
    while running:
        user_resp = get_user_input()
        if user_resp == 1:
            quote_handler.print_random_quote()
            quote_handler.remove_quote()

        elif user_resp == 2:
            running = close_app()

        elif user_resp == 999:
            print("Please enter a number.\n")

        else:
            print("Sorry that option was not recognized.\n")

        if quote_handler.is_empty():
            print("App out of quotes")
            running = close_app()


def get_user_input():
    options_str = ("1) For a random quote\n"
                   "2) To exit\n"
                   "Response: ")

    try:
        user_input = int(input(options_str))
    except:
        user_input = 999

    return user_input


def close_app():
    print("Goodbye. Stay Wise.")
    return False



run_app()