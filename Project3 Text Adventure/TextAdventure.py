game_over = False

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("\n")
response = input("Do you go LEFT or RIGHT: ")

if response == "right":
    print("You fell into a hole!")
    print("Game Over")
    game_over = True

if not game_over:
    print("You come across a giant lake")
    response = input("Do you WAIT and assess the situation or "
                     "do you CROSS straight away: ")
    if response == "CROSS":
        print("A sea serpent coils around your limbs dragging you deep underwater")
        print("Game Over")
        game_over = True

if not game_over:
    print("While staring into the lake you notice a colorful reflection")
    print("There are three coloured doors embedded into the cliffs behind you!")
    response = input("Do you enter the RED door, BLUE door or YELLOW door? ")
    if response != "YELLOW":
        if response == "RED":
            print("The door handle radiates with a molten glow as you turn it, "
                  "suddenly you are engulfed in flames")
            print("Oh no the agony")
        if response == "BLUE":
            print("You open the door with great effort, a huge gasp of wind throws you into the lake")
            print("A sea serpent destroys you.")
        print("Game Over")
        game_over = True
    else:
        print("Yay treasure")


