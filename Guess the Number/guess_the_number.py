"""Guess a randomly selected number within a certain amount of tries."""

import random

UPPER_LIMIT = 100  # highest number the secret number can be
GUESSES = 7  # number of guesses the player has


def ordinal(n):
    """Code golf way of returning a number and it's ordinal suffix as a string."""
    return str(n) + "tsnrhtdd"[(n // 10 % 10 != 1) * (n % 10 < 4) * n % 10 :: 4]


def guess_the_number(UPPER_LIMIT=UPPER_LIMIT, GUESSES=GUESSES):
    SECRET_NUMBER = random.randint(1, UPPER_LIMIT)  # pick a random number
    print(
        f"\nI am thinking of a number between 1 and {UPPER_LIMIT}. You have {GUESSES} guess{'es' if GUESSES != '1' else ''}"
    )

    won = False
    for attempt in range(1, GUESSES + 1):
        while True:
            try:
                guess = int(input(f"\nWhat is your {ordinal(attempt)} guess? > "))

                if guess > UPPER_LIMIT:
                    raise ValueError(f"number beyond upper-limit: {guess} > {UPPER_LIMIT}")
                elif guess < 1:
                    raise ValueError(f"number below lower-limit: {guess} < 1")
                else:
                    break

            except ValueError as error:
                print(error)

        if guess > SECRET_NUMBER:
            print("Too high")
        elif guess < SECRET_NUMBER:
            print("Too low")
        elif guess == SECRET_NUMBER:
            won = True
            break

    if won:
        print(f"\nYes! The number was {SECRET_NUMBER}. You got it in {attempt} guess{'es' if attempt != '1' else ''}\n")
    else:
        print(f"\nYou lose! The number I was thinking of was {SECRET_NUMBER}\n")


if __name__ == "__main__":
    guess_the_number()

    while True:
        play_again = input("Play again, (y)es or (n)o? > ")
        if play_again == "y":
            guess_the_number()
        elif play_again == "n":
            break

    print("Goobye!")
