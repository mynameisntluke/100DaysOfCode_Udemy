# Made during DAY17- OOP Quiz

from words import words
import random


class JapanApp:
    def __init__(self, lives=10):
        self.word_dict = words
        self.current_word = ""
        self.lives = lives
        self.intro_msg()

    def intro_msg(self):
        """Introduces App and sets the first word to guess"""
        print("Welcome. Add a new word everyday to learn!")
        self.set_random_eng_word()

    def set_random_eng_word(self):
        """Gets a random key from word dictionary and sets it as current word"""
        self.current_word = random.choice(list(words.keys()))

    def delete_current_word(self):
        """If current_word is set, the related entry in word_dict
        is deleted"""
        if self.current_word != "":
            self.word_dict.pop(self.current_word)

    def get_current_word_eng(self):
        """Returns current word in English"""
        return self.current_word

    def get_current_word_jp(self):
        """Returns current word in Japanese"""
        return self.word_dict[self.current_word]["Japanese"][0]

    def get_example_text(self):
        """Returns an example sentence for the current word"""
        return self.word_dict[self.current_word]["example"]