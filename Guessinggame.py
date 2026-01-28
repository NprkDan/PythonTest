"""
A simple number guessing game using a while loop and random module.
"""
import random

def main():
    """Main function for the guessing game."""
    # The program picks a random number between 1 and 100
    target_number = random.randint(1, 100)
    guess = 0
    attempts = 0

    print("--- Number Guessing Game ---")
    print("I have picked a number between 1 and 100. Try to guess it!")

    # The loop runs until the user guesses the correct number
    while guess != target_number:
        try:
            # Getting input from the user
            user_input = input("Enter your guess: ")
            guess = int(user_input)
            attempts += 1

            if guess < target_number:
                print("Too low! Try a higher number.")
            elif guess > target_number:
                print("Too high! Try a lower number.")
            else:
                print(f"CONGRATULATIONS! You guessed it in {attempts} attempts.")
        
        except ValueError:
            # Handling the risk of non-integer inputs
            print("Error: Please enter a valid whole number.")

if __name__ == "__main__":
    main()