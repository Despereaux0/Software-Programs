import random

def number_guessing_game():
    secret_number = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0

    print("🎯 Welcome to the Number Guessing Game!")
    print("Try to guess the number (between 1 and 100). Type 'exit' to quit.\n")

    while True:
        guess = input("Enter your guess: ")

        if guess.lower() == "exit":
            print(f"👋 Thanks for playing! The number was {secret_number}.")
            break

        if not guess.isdigit():
            print("❌ Please enter a valid number!")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("⬆️ Too low! Try again.")
        elif guess > secret_number:
            print("⬇️ Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
            break

number_guessing_game()
