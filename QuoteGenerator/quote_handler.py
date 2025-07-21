from quotes import quotes
import random

#TODO 1 User can add quotes

class QuoteHandler():
    def __init__(self):
        self.quote_dict = quotes
        self.ref = ""

    def print_random_quote(self):
        """Prints one random quote from quotes and then deletes it"""
        self.ref = random.choice(list((quotes.keys())))
        print(f"\n\t\"{quotes[self.ref]['quote']}\" \n\t\t-{quotes[self.ref]['author']}\n")

    def remove_quote(self):
        """Removes quote from dictionary"""
        del self.quote_dict[self.ref]

    def is_empty(self):
        """Returns true if out of quotes"""
        if self.quote_dict == {}:
            return True
        return False