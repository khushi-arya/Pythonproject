import random

def number_guessing_game():
    print("Welcome, traveler, to the Number Guessing Game!")
    print("I am the guardian of this enchanted forest. To prove your worthiness, guess the magic number I'm thinking of.")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        try:
            guess = int(input("\nEnter your guess (between 1 and 100): "))
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the magic number {secret_number}!")
                print("You've proven yourself worthy. The secrets of the enchanted forest await.")
                return

            print(f"Attempts left: {max_attempts - attempts}")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    print("Sorry, you've run out of attempts. The magic of the forest overwhelms you. You are lost forever.")

number_guessing_game()
