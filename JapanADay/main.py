from japan_app import JapanApp


app = JapanApp()

#one round
guess = " "
while guess != "exit":

    guess = input(f"{app.get_current_word_eng()}:")
    correct_answer = app.get_current_word_jp()

    if guess == correct_answer:
	    print("correct")
	    app.delete_current_word()
	    app.set_random_eng_word()
	   
    elif guess == "exit":
    	print("goodbye")
    
    else:
    	print(f"The correcr answer was:{correct_answer}")