#Ted Guerrero
#CTC 389
#Lab 8

#Opening/greeting
def opening():
    print("\n")
    print("Welcome to Walt Disney World!")
    name = input("What is your name: ")
    print("Greetings",name,"you have won an all-inclusive trip to the most magical place on earth!")
    print("You find yourself at your resort, Carribean Beach.")
#Decision 1
    print("\n")
    print("From here, you are to decide your first move on your vacation!")
    print("\n")
    print("1. Hop on the Skyliner to EPCOT")
    print("2. Line up for the next bus to Magic Kingdom")
    print("3. Check out my room")
    choice1 = int(input("Where to next? "))
    choice2 = 0
    choice3 = 0
    choice4 = 0
    choice5 = 0

    if (choice1 == 1):
        print("\n")
        print("After enjoying a smooth trip through the skys, you touch down in the EPCOT travel center")

#Decision 2
        print("1. Head straight to Canada to begin the World Showcase.")
        print("2. Beeline to Guardians of the Galaxy Cosmic Rewind, because hey, it's the best ride here.")
        print("3. Turn back around, hop back on the skyliner, and go back to the resort.")
        choice2 = int(input("Where to next? "))

    elif (choice1 == 2):
        print("\n")
        print("After waiting over 30 minutes, you give up and head back to your room to sleep.")
        
    elif (choice1 == 3):
        print("\n")
        print("After walking into your room, seeing your bed, and feeling exhauseted, you fall into bed and are asleep the second your head hits the pillow.")

    if (choice2 == 1):
        print("\n")
        print("Welcome to Canada! You see The Cellar Steakhouse, disappear within its bowels, enjoy a great steak, and head back to the room to enjoy your food coma.")
    elif (choice2 == 2):
        print("\n")
        print("Wow! Guardians has an incredibly long line! You have a choice to make!")

#Decision 3
        print("1. Buy a lightning lane ticket to get on ASAP!")
        print("2. Walk away, head hung low, as you decide to give up and head back to your room.")
        print("3. Get in the long line, and prepare to meet some interesting new people in line.")
        choice3 = int(input("What's your choice? "))

    elif (choice2 == 3):
        print("\n")
        print("The call to your room is strong. You heed its call, see the bed, and collapse asleep.")

    
    if (choice3 == 1):
        print("\n")
        print("What a rush! There is no greater ride in this park than Guardians. After realizing how much money you spent, you head back to your room.")
    elif (choice3 == 2):
        print("\n")
        print("Hey, you tried. But at least you're back in your room.")

#Decision 4
    elif (choice3 == 3):
        print("\n")
        print("The line wraps back and forth, so you get to see the same people. You see someone with a cool shirt with an inside joke that you recognize on it.")
        print("1. Do you decide to chat them up, leading with a comment only they would get?")
        print("2. Ignore it and focus on your phone?")
        print("3. Reminded by the image on the shirt you haven't called your mom in awhile, and call them right then?")
        choice4 = int(input("What's your choice? "))

    if (choice4 == 1):
        print("\n")
        print("You... have chosen wisely.")
        print("You meet your soulmate and recall this day as the most important day in your life!")
#Decision 5
    elif (choice4 == 2):
        print("\n")
        print("The time flys by and before you know it, you are boarding queue of the ride, but your phone is dead.")
        print("1. Do you board the ride, and try to get by in the park without your phone?")
        print("2. Ignore the fact that you'll never make it home without your phone and hop on the ride?")
        print("3. Become overcome with the thought of not having your phone and need to be carted off the attraction?")
        choice5 = int(input("What's your choice? "))
    elif (choice4 == 3):
        print("\n")
        print("You get so loud talking on the phone, you are removed from the line and the park.")

    if (choice5 == 1):
        print("\n")
        print("Congratulations! You have discovered that you are a capable human being, and can live a full life without a smartphone.")
        print("You have won the game of life.")
    elif (choice5 == 2):
        print("\n")
        print("Ignorance is not bliss. You have lost at the game of life.")
    elif (choice5 == 3):
        print("\n")
        print("Well, this wasn't a fun day after all. That is all.")
        





opening()
restart = input("Looks like you are back at square one. Want to try again? (y/n): ")
if (restart == "y"):
    opening()
else:
    print("Thank you for playing, good-bye.")

