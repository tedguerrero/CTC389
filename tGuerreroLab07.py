#Ted Guerrero
#CTC389
#Lab 7a, Extra Credit

guess = 23
print("\n")
print("*** Number Guessing Game ***")
x = 21

while (20<x<26 and x != 23):
    x = int(input("Guess my Number: "))
    if x == 24 or x == 25 or x == 22 or x ==21:
        print("\n")
        print("Close, try again: ",x)
    elif x > 24:
        print("\n")
        print("Sorry, you lost. Your guess was higher than my number of 23.")
    elif x < 21:
        print("\n")
        print("Sorry, you lost. Your guess was lower than my number of 23.")

if x == 23:
    print("\n")
    print("Congrats! you guessed my number of 23!")

