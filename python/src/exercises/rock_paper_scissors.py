"""Rock, paper scissors game."""
import random

options = ["rock", "paper", "scissors"]

random_choice = random.choice(options)

user_choice = ""

while user_choice not in options:
    user_choice = input("Enter rock, paper or scissors: ")

print("You chose "+user_choice)
print("I chose "+random_choice)

if user_choice == "rock":
    if random_choice == "rock":
        print("rock vs rock: it's a draw!")
    elif random_choice == "paper":
        print("paper wraps rock: you lose!")
    else: # random_choice is scissors
        print("rock blunts scissors: you win!")
elif user_choice == "paper":
    if random_choice == "rock":
        print("paper wraps rock: you win!")
    elif random_choice == "paper":
        print("paper vs paper: it's a draw!")
    else: # random_choice is scissors
        print("scissors cut paper: you lose!")
else: # user_choice is scissors
    if random_choice == "rock":
        print("rock blunts scissors: you lose!")
    elif random_choice == "paper":
        print("scissors cut paper: you win!")
    else: # random_choice is scissors
        print("scissors vs scissors: it's a draw!")
