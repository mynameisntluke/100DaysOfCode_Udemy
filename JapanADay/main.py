from japan import JapanApp

app = JapanApp()

correct = 0
incorrect = 0

guess = " "
while guess != "exit" :
    # Shows user the English word and prompts them for the Japanese word
    guess = input(f"{app.get_current_word_eng()}: ").lower()
    correct_answer = app.get_current_word_jp()

    if guess == correct_answer:
        print("Correct！")
        # app.delete_current_word()
        app.set_random_eng_word()
        correct += 1
        print(f"Current Score: {correct}/{correct + incorrect}\n")

    elif guess == "exit" or guess == "やめる" or guess == "quit":
        print("goodbye")

    elif guess == "example" or guess == "れい":
        print(app.get_example_text())

    else:
        print(f"The correct answer was:{correct_answer}")
        app.set_random_eng_word()
        incorrect += 1
        print(f"Current Score: {correct}/{correct + incorrect}\n")





# print(f"You knew {correct} words")