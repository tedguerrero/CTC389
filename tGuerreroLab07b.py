#Ted Guerrero
#CTC389
#Lab 7b, Extra Credit

guess = 23
print("\n")
print("*** Number Guessing Game ***")
x = 21

def game(guess):
    while (20<guess<26 and guess != 23):
        guess = int(input("Guess my Number: "))
        if guess == 24 or guess == 25 or guess == 22 or guess ==21:
            print("\n")
            print("Close, try again: ",guess)
        elif guess > 24:
            print("\n")
            print("Sorry, you lost. Your guess was higher than my number of 23.")
        elif guess < 21:
            print("\n")
            print("Sorry, you lost. Your guess was lower than my number of 23.")
    if guess == 23:
        print("\n")
        print("Congrats! you guessed my number of 23!")


print("Welcome to the Guessing Game!")
print("\n")
ans = input("Would you like to play my game? ")

if ans == "yes":
    game(x)


if ans == "no":
    print("bye")

