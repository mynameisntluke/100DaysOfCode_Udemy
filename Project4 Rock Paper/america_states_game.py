import random
from american_states import state_names
states_to_guess = 5
lives = "*****"
points = 0


for n in range(states_to_guess):

    rand_state_ref = random.randint(0, len(state_names)-1)
    rand_state = state_names[rand_state_ref]

    print(f"\nPoints: {points}")
    print(f"{rand_state[0:3]}______:")
    guess = input()
    if guess.lower() == rand_state.lower():
        print("CORRECT!")
        # Remove from list so as not to be repeated
        state_names.pop(rand_state_ref)
        points += 1
    elif guess.lower() == "cheat":
        print(f"The state is: {rand_state}")
        # Remove from list so as not to be repeated
        state_names.pop(rand_state_ref)
    else:
        # One more try
        print("Try again!")
        print(f"{rand_state[0:4]}______:")
        guess = input()
        if guess.lower() == rand_state.lower():
            print("CORRECT!")
            # Remove from list so as not to be repeated
            state_names.pop(rand_state_ref)
            points += 1
        else:
            print("NAH!!!")
            print(f"The correct state was: {rand_state}")

print("\n Goodbye for now")
