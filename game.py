# game.py
print("'Rock', 'Paper', 'Scissors,' 'Shoot!'")
PLAYER_NAME = input ("Please select a player name:")
print("WELCOME" f"{PLAYER_NAME} to my Rock-Paper-Scissors game...")

import random

user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

print("You chose: ", user_choice)

if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("Thank you for choosing.")
else:
    print("OOPS, invalid input. Please try again.")
    exit()

valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("The computer chose: ", computer_choice)

if (user_choice == "rock") and (computer_choice == "rock"):
    print("WE HAVE A TIE!")

if (user_choice == "rock") and (computer_choice == "scissors"):
    print("CONGRATULATIONS! YOU WON!")

if (user_choice == "rock") and (computer_choice == "paper"):
    print("UH OH! The computer won. Better luck next time!")

if (user_choice == "paper") and (computer_choice == "paper"):
    print("WE HAVE A TIE!")

if (user_choice == "paper") and (computer_choice == "scissors"):
    print("UH OH! The computer won. Better luck next time!")

if (user_choice == "paper") and (computer_choice == "rock"):
    print("CONGRATULATIONS! YOU WON!")

if (user_choice == "scissors") and (computer_choice == "scissors"):
    print("WE HAVE A TIE!")

if (user_choice == "scissors") and (computer_choice == "rock"):
    print("UH OH! The computer won. Better luck next time!")

if (user_choice == "scissors") and (computer_choice == "paper"):
    print("CONGRATULATIONS! YOU WON!")

print("THANK YOU FOR PLAYING! PLEASE PLAY AGAIN.")