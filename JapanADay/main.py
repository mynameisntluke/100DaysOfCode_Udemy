from japan import JapanApp

app = JapanApp()

lives = 10
guess = " "
while guess != "exit" and lives > 0:
#TODO 1: Allow for multiple correct answers
    print(f"\n {lives}/10 Lives")
    guess = input(f"{app.get_current_word_eng()}: ").lower()
    correct_answer = app.get_current_word_jp()

    if guess == correct_answer:
        print("Correct！")
        app.delete_current_word()
        app.set_random_eng_word()

    elif guess == "exit":
        print("goodbye")

    elif guess == "example" or guess == "れい":
        print(app.get_example_text())

    else:
        print(f"The correct answer was:{correct_answer}")
        app.set_random_eng_word()
        lives -= 1