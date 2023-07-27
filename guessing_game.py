import random


def generate_secret_number():
    return random.randint(1, 3)


def get_user_guess():
    return int(input("Guess: "))


def play_again():
    return input("Do you want to play again? (yes/no): ").lower() == "yes"


def guessing_game():
    guess_limit = 3
    play_again_flag = True

    while play_again_flag:
        secret_number = generate_secret_number()
        guess_count = 0

        while guess_count < guess_limit:
            guess = get_user_guess()
            guess_count += 1
            if guess == secret_number:
                print("You won!")
                play_again_flag = play_again()
                break
        else:
            print("Try again!")


if __name__ == "__main__":
    guessing_game()
