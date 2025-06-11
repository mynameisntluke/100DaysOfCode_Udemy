# OWN VERSION OF TEXT ADVENTURE FROM THIS DAYS PROJECT/LESSONS

is_alive = True
user_input = ""
time = 40
tickets = 0

# begin game
user_input = input("Do you wish to BEGIN game or READ the instructions?\n").upper()

# prologue
if user_input == "BEGIN":
    print("""You wake up late in the staff room of Python Amusements, the arcade you work for. 
          You don't remember falling asleep here. It's dark. And quiet. 
          You should have left hours ago. 
          You get up from the sofa feeling disorientated.""")

    user_input = input("Do you ASSESS your surroundings or quickly LEAVE for the brightly lit "
                       "main room.\n").upper()

if user_input == "ASSESS":
    print("""The room is as you remember it. Or appears to be. It's dark here and in your 
          just-waking state you struggle to remember how it should look. But isn't everything 
          too neat? There is nothing of interest here and you move on to the beating heart 
          of the arcade- the cavernous games room. As you reach for the door you find two prize tickets lying 
          on the floor. You pocket them- afterall you are a regular here both its customer and 
          technician.""")
    input("Press ENTER to continue")
    tickets += 2
user_input = input("""The main room is as it should be for this time of day. 0240. According to the 
                   mascot analogue clocks on the wall. Midnight already. You should have left at 6pm. 
                   All the machines are switched off, main lights dimmed, silent but for three machines 
                   which someone has left powered up and are now running in idle. Do you EXAMINE the machines 
                   or head for one of the EXIT doors that dominate the seaside facing part of the 
                   building.\n""").upper()

if user_input == "EXAMINE":
    print("""The first machine still running is a coin pusher, small silver coins ebb and flow. No music plays.
          There's something about the machine that strikes you as somewhat wrong. The second is a UFO Catcher. An 
          immaculate shiny claw hangs patiently- waiting to nab one of the stuffed toys below. Suddenly you
          recall what is wrong here too - both machines were broken earlier. Hadn't they been for weeks? 
          You look further down into the gloomy depths of the closed arcade where a third plethora of lights
          cheerfully play. It's coming from the over 18 gambling area and you've no doubt which machine it is,
           three of you had tried, uselessly, to get it working for weeks. You don't examine in and instead, 
          feeling uneasy, head for the exits.""")
    print("The clock makes an exaggerated TICK sound, practically a screech as the minute hand drags into "
          "its new position: 0241. Something else to fix but definitely not now.")
    time += 1
    input("Press ENTER to continue")


    input("""You practically jog for one of the doors, as you push against it it doesn't budge. You try another.
          Nothing. As you try a third, you take a look out the window, it's not dark outside. It's empty. 
          A perfect void. The view is one of a sleek uniform black, perhaps it's just the windows? 
          """)

input("Before you can investigate further you notice a message has been etched on each window. It's crude but legible: ")

input("'Freedom is yours if you gather twenty tickets before the witching hour of 3, damnation is yours for anything less'")

time+=1

input("This all seems insane to you but without any better plan you decide to follow the instructions. The minute hands screeches again: ")
