"""A guessing game."""
import random

target = random.randint(1,9)

num_guesses = 0

guessStr = input("Guess the secret number between 1 and 9: ")
guess = int(guessStr)
num_guesses = num_guesses + 1

while guess != target and guessStr != "exit":
    if guess > target:
        print("Guess lower!")
    else:
        print("Guess higher!")
    guessStr = input("Enter the new guess: ")
    guess = int(guessStr)
    num_guesses = num_guesses + 1

if guessStr == "exit":
    print("You took the easy way out :(")
else:
    print("Correct! That took "+str(num_guesses)+" guesses")
    

