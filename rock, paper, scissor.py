import random

game = ["rock", "paper", "scissor"]

computer = ""

per_point = 0
com_point = 0

game_chance = True

while(game_chance):

    person = input("rock, paper, scissor?:")

    computer = game[random.randint(0 , 2)]


    if person == "exit":
        game_chance = False


    if person == computer:
        print("it's a tie!")

    elif person == "rock" and computer == "paper":
        print("you lose!")
        com_point = com_point + 1

    elif person == "paper" and computer == "rock":
        print("you win!")
        per_point = per_point + 1

    elif person == "rock" and computer == "scissor":
        print("you win!")
        per_point = per_point + 1

    elif person == "paper" and computer == "scissor":
        print("you lose!")
        com_point = com_point + 1

    elif person == "scissor" and computer == "rock":
        print("you lose!")
        com_point = com_point + 1

    elif person == "scissor" and computer == "paper":
        print("you win!")
        per_point = per_point + 1

    print("i choose" , computer , "and you choose", person)
    print("your point:", per_point , "computer's point:", com_point)


    if per_point >= 3 or com_point >= 3:
        game_chance = False

if per_point > com_point:
    print("")
    print("You win the game!")
else:
    print("")
    print("You lost the game!")

print("your point: ", per_point)
print("computer's piont: ", com_point)