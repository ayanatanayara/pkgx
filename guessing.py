import random

def guess_number():
    while True:
        secret_number = random.randint(1, 100)
        guess = None
        attempts = 0

        print("Hello! I have a secret number between 1 and 100. Try to guess it!")

        while guess != secret_number:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low. Try again.")
            elif guess > secret_number:
                print("Too high. Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts!")
                break

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

if __name__ == "__main__":
    guess_number()
