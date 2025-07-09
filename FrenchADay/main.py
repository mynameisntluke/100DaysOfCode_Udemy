from french import FrenchApp

#TODO 1 More words

app = FrenchApp()


def word_game(lives = 10):
    guess = " "
    correct = 0

    while guess != "exit" and lives > 0 and not app.is_empty():
        print(f"\n {lives}/10 Lives")
        guess = input(f"{app.get_current_word_eng()}: ").lower()
        correct_answer = app.get_current_word_fr()

        if guess == correct_answer:
            print("Correct！")
            app.delete_current_word()
            app.set_random_eng_word()
            correct += 1

        elif guess == "exit":
            print("goodbye")

        elif guess == "example":
            print(app.get_example_text())

        else:
            print(f"The correct answer was: {correct_answer}")
            app.set_random_eng_word()
            lives -= 1

    print("\n GameOver.")
    print(f"You got {correct} words correct!")

word_game()