# Plays game once


from chemistry_app import ChemApp
import pandas as pd

class GuessElement:
    def __init__(self, level = 3):
        self.chem_app = ChemApp()
        self.level = level
        self.set_level()
        self.lives = 10
        self.highscore = 0
        self.max_level = 4
        self.scores_file = pd.read_csv("highscore.csv")

    def set_level(self):
        if self.level == 1:
            self.chem_app.set_element_dict(10)
        elif self.level == 2:
            self.chem_app.set_element_dict(25)
        elif self.level == 3:
            self.chem_app.set_element_dict(55)
        elif self.level == 4:
            self.chem_app.set_element_dict(75)

    def user_chooses_level(self):
        try:
            level_choices = " "
            for level in range(1, self.max_level+1):
                level_choices += f"{str(level)} "
            choice = int(input(f"Choose a level [{level_choices}]: "))
            if choice > self.max_level or choice < 1:
                choice = self.max_level
            self.level = choice
            self.set_level()

        except:
            print("Invalid Option. ")


    # def get_highscore(self):
    #     """Searches file for highscore for current level"""
    #     with open("highscore.txt") as file:
    #         highscore = file.readlines()[self.level-1]
    #         print(highscore)
    #         return int(highscore)

    def print_intro_msg(self):
        print(f"###################################\n\t\t\t Level {self.level}\n###################################")
        print(f"Correctly guess the chemical name from the given chemical symbol. To quit type QUIT any time.")
        print(f"Current HighScore: {self.highscore}")

    def guess_the_element_name(self):
        correct = 0

        self.print_intro_msg()

        while self.lives > 0 :
            self.chem_app.set_random_element()
            print(f"Lives: {self.lives}/10    Correct {correct}")
            # if debug:
            #     print(chem.get_current_element_name())
            user_resp = input(f"{self.chem_app.get_current_element_symbol()}: ")
            if user_resp.lower() == self.chem_app.get_current_element_name().lower():
                print("Correct\n")
                correct += 1
                # Remove from list
                self.chem_app.delete_current_element()
            elif user_resp == "QUIT":
                self.lives = -5
            else:
                print(
                    f"WRONG. {self.chem_app.get_current_element_symbol()} is the symbol for the element {self.chem_app.get_current_element_name()}.\n")
                self.lives -= 1

        if self.lives == 0:
            print(f"Well done you correctly guessed {correct} elements\n")
        elif self.lives == -5:
            print("Returning to main menu.\n")


        self.reset_app()

    def reset_app(self):
        self.lives = 10
        self.chem_app = ChemApp()
        self.set_level()
