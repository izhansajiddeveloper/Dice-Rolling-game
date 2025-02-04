import random

def roll_dice():
    dice1 = random.randint(1, 6)  # First dice roll
    dice2 = random.randint(1, 6)  # Second dice roll
    return dice1, dice2  # Returning both dice results

while True:
    user_input = input("Press Enter to roll the dice or type 'exit' to quit: ")
    
    if user_input.lower() == "exit":
        print("Thanks for playing! Goodbye!")
        break  # Exit the game
    
    dice1, dice2 = roll_dice()  # Get both dice results
    total = dice1 + dice2  # Sum of both dice
    
    print(f"You rolled a {dice1} and a {dice2}! (Total: {total})")

