# game.py

print("'Rock', 'Paper', 'Scissors,' 'Shoot!'")

import random

import os

import dotenv

dotenv.load_dotenv()

PLAYER_NAME = os.getenv("PLAYER_NAME")
print(f"Welcome '{PLAYER_NAME}' to my Rock-Paper-Scissors game!")

#non .env way
#PLAYER_NAME = input ("Please select a player name:")
#print("WELCOME" f"{PLAYER_NAME} to my Rock-Paper-Scissors game...")

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

#adapted from Jan's code from slack
if user_choice == "rock":
    if computer_choice == "rock":
        print("IT'S A TIE")
    elif computer_choice == "paper":
        print("OH, THE COMPUTER WON...")
    elif computer_choice == "scissors":
        print("YOU WON! CONGRATS!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("YOU WON! CONGRATS!")
    elif computer_choice == "paper":
        print("IT'S A TIE")
    elif computer_choice == "scissors":
        print("OH, THE COMPUTER WON...")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("OH, THE COMPUTER WON...")
    elif computer_choice == "paper":
        print("YOU WON! CONGRATS!")
    elif computer_choice == "scissors":
        print("IT'S A TIE")


#my original code 
#if (user_choice == "rock") and (computer_choice == "rock"):
#     print("WE HAVE A TIE!")

# if (user_choice == "rock") and (computer_choice == "scissors"):
#     print("CONGRATULATIONS! YOU WON!")

# if (user_choice == "rock") and (computer_choice == "paper"):
#     print("UH OH! The computer won. Better luck next time!")

# if (user_choice == "paper") and (computer_choice == "paper"):
#     print("WE HAVE A TIE!")

# if (user_choice == "paper") and (computer_choice == "scissors"):
#     print("UH OH! The computer won. Better luck next time!")

# if (user_choice == "paper") and (computer_choice == "rock"):
#     print("CONGRATULATIONS! YOU WON!")

# if (user_choice == "scissors") and (computer_choice == "scissors"):
#     print("WE HAVE A TIE!")

# if (user_choice == "scissors") and (computer_choice == "rock"):
#     print("UH OH! The computer won. Better luck next time!")

# if (user_choice == "scissors") and (computer_choice == "paper"):
#     print("CONGRATULATIONS! YOU WON!")

print("THANK YOU FOR PLAYING! PLEASE PLAY AGAIN.")