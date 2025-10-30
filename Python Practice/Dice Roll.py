import random

def roll_dice():
    return random.randint(1, 6)

print("🎲 Dice Roller: Press Enter to roll, or type 'exit' to quit.")

while True:
    user_input = input()
    
    if user_input.lower() == 'exit':
        print("Thanks for playing!")
        break
    
    result = roll_dice()
    print(f"🎲 You rolled a {result}!")
