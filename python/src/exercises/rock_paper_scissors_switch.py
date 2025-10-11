"""Rock, paper scissors game."""
import random

options = ["rock", "paper", "scissors"]

random_choice = random.choice(options)

user_choice = ""

while user_choice not in options:
    user_choice = input("Enter rock, paper or scissors: ")

print("You chose "+user_choice)
print("I chose "+random_choice)


match user_choice:
    case "rock":
        match random_choice:
            case "rock":
                print("rock vs rock: it's a draw!")
            case "paper":
                print("paper wraps rock: you lose!")
            case _: # random_choice is scissors
                print("rock blunts scissors: you win!")
    case "paper":
        match random_choice:
            case "rock":
                print("paper wraps rock: you win!")
            case "paper":
                print("paper vs paper: it's a draw!")
            case _: # random_choice is scissors
                print("scissors cut paper: you lose!")
    case _: # user_choice is scissors
        match random_choice:
            case "rock":
                print("rock blunts scissors: you lose!")
            case "paper":
                print("scissors cut paper: you win!")
            case _: # random_choice is scissors
                print("scissors vs scissors: it's a draw!")
