import random

while True:
    player = input("Rock, Paper, or Scissors? (or 'quit' to exit): ").lower()
    if player == 'quit': break
    if player not in ['rock', 'paper', 'scissors']:
        print("Invalid choice!"); continue
    
    computer = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose: {computer}")
    
    if player == computer:
        print("It's a tie!")
    elif (player, computer) in [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]:
        print("You win!")
    else:
        print("Computer wins!")
