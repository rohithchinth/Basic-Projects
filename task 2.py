import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    attempts = 0
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try guessing higher.")
        elif guess > secret_number:
            print("Too high! Try guessing lower.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts!")
            break

def main():
    play_again = "yes"
    while play_again.lower() == "yes" or play_again.lower() == "y":
        guessing_game()
        play_again = input("Do you want to play again? (yes/no): ")

    print("Thanks for playing!")

if __name__ == "__main__":n