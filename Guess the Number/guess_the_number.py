"""
Guess a randomly selected number within a certain amount of tries. Can alter the
number of guesses and the upper limit by using command line arguments, e.g:

`$ py guess_the_number.py --guesses 9 --limit 1000`
"""

import os
import random
import argparse

_UPPER_LIMIT = 100  # Highest number the secret number can be
_GUESSES = 6  # Number of guesses the player has


def ordinal(n):
    """Code golf way of returning a number and it's ordinal suffix as a string."""
    return str(n) + "tsnrhtdd"[(n // 10 % 10 != 1) * (n % 10 < 4) * n % 10 :: 4]


def guess_the_number(UPPER_LIMIT, GUESSES):
    if UPPER_LIMIT < GUESSES:
        raise ValueError(f"upper limit can't be less than guesses: {UPPER_LIMIT} < {GUESSES}")

    secret_number = random.randint(1, UPPER_LIMIT)  # Pick a random number
    print(
        f"I am thinking of a number between 1 and {UPPER_LIMIT}. You have {GUESSES} guess{'es' if GUESSES != 1 else ''}"
    )

    prev_guesses = []
    won = False
    for attempt in range(1, GUESSES + 1):
        while True:
            try:
                guess = int(input(f"\nWhat is your {ordinal(attempt)} guess? > "))
                if guess > UPPER_LIMIT:
                    raise ValueError(f"number beyond upper-limit: {guess} > {UPPER_LIMIT}")
                if guess < 1:
                    raise ValueError(f"number below lower-limit: {guess} < 1")
                if guess in prev_guesses:
                    raise ValueError(f"number entered previously: {guess}")

                prev_guesses.append(guess)
                break

            except ValueError as error:
                print(error)

        if guess > secret_number:
            print("Too high")
        elif guess < secret_number:
            print("Too low")
        elif guess == secret_number:
            won = True
            break

    if won:
        print(f"\nYes! The number was {secret_number}. You got it in {attempt} guess{'es' if attempt != 1 else ''}\n")
        return True

    print(f"\nYou lose! The number I was thinking of was {secret_number}\n")
    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--guesses", type=int)
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()

    play_again = "y"
    while play_again != "n":
        if play_again == "y":
            os.system("cls" if os.name == "nt" else "clear")
            guess_the_number(args.limit or _UPPER_LIMIT, args.guesses or _GUESSES)
        play_again = input("Play again, (y)es or (n)o? > ")

    print("Goobye!")


if __name__ == "__main__":
    main()
