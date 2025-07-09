from quotes import quotes
import random

class QuoteHandler():
    def __init__(self):
        self.quote_dict = quotes
        self.ref = ""

    def print_random_quote(self):
        """Prints one random quote from quotes and then deletes it"""
        self.ref = random.choice(list((quotes.keys())))
        print(f"\n\t\"{quotes[self.ref]['quote']}\" \n\t\t-{quotes[self.ref]['author']}\n")

    def remove_quote(self):
        del self.quote_dict[self.ref]

    def is_empty(self):
        """Returns true if out of quotes"""
        if self.quote_dict == {}:
            return True
        return False