import random


def guessing_game():
    print("\nWelcome to the Guessing Game!")
    print("=============================")

    play_again = 'Y'

    while play_again.upper() == 'Y':
        number_to_guess = random.randint(1, 100)
        attempts = 0
        guessed_correctly = False

        print("\nI have generated a random number between 1 and 100.")

        while not guessed_correctly:
            user_guess = int(input("Please enter your guess: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number correctly in {attempts} attempts.")
                guessed_correctly = True

        play_again = input("Do you want to play again? (Y/N): ").strip()

    print("\nThank you for playing the Guessing Game! :)")


if __name__ == "__main__":
    guessing_game()
