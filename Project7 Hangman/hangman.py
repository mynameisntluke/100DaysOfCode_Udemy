import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)


# debug
def get_user_guess(chosen_word, debug=False):
    correct_input = False
    while not correct_input:
        if debug:
            guess = input(f"The word is {chosen_word}. Guess a letter\n").lower()
        else:
            guess = input("Guess a letter\n").lower()

        if guess == "exit":
            correct_input = True
        elif len(guess) != 1:
            print("Invalid Guess Dude")
        else:
            correct_input = True
    return guess


guess = get_user_guess(chosen_word, debug=True)
if chosen_word.count(guess) != 0:
    print("Aha!")
else:
    print("One step closer to death, mate.")
