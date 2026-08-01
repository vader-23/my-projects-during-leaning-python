import random
answer = random.randint(1, 10)
guess = 0
tries = 0

while guess != answer:
    guess = int(input("Enter your guess: "))
    tries += 1

    if answer > guess:
        print("too low")

    elif answer < guess:
        print("too high")

    else:
        print("YOU'RE CORRECT")
        print("You guessed it in", tries, "tries!")