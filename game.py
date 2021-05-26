# game.py
print("Rock, Paper, Scissors, Shoot!")

user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")

print("USER CHOICE: ", user_choice)

if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("VALID. KEEP GOING")
else:
    print("OOPS, invalid input. Please try again.")
    exit()
    
print("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN.")