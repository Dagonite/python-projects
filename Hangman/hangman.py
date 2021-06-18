"A game of Hangman. Select a difficulty then try to guess the hidden word."
# pylint: disable=anomalous-backslash-in-string

import json
import random

HANGMAN_STAGES = [
    """
 +---+
 |   |
 O   |
/|\  |
/ \  |
    ===""",
    """
 +---+
 |   |
 O   |
/|\  |
/    |
    ===""",
    """
 +---+
 |   |
 O   |
/|\  |
     |
    ===""",
    """
 +---+
 |   |
 O   |
/|   |
     |
    ===""",
    """
 +---+
 |   |
 O   |
 |   |
     |
    ===""",
    """
 +---+
 |   |
 O   |
     |
     |
    ===""",
    """
 +---+
 |   |
     |
     |
     |
    ===""",
    """
 +---+
     |
     |
     |
     |
    ===""",
    """
     +
     |
     |
     |
     |
    ===""",
    """





    ===""",
    """





    """,
]

used_letters = []


def main():
    select_difficulty()
    LIVES = len(HANGMAN_STAGES) - 1
    category, phrase = choose_random_word()
    hidden_phrase = ["_"] * len(phrase)

    for i, ch in enumerate(phrase):
        if ch in (" ", "'", "-"):
            hidden_phrase[i] = ch

    prompt_user_for_letters(LIVES, category, phrase, hidden_phrase)


def select_difficulty():
    while True:
        difficulty = input("Enter a difficulty, (e)asy, (m)edium, or (h)ard: > ")
        if difficulty in ("e", "m", "h"):
            break

    if difficulty in ("m", "h"):
        del HANGMAN_STAGES[-1]
        del HANGMAN_STAGES[-1]

    if difficulty == "h":
        del HANGMAN_STAGES[-1]
        del HANGMAN_STAGES[-1]


def prompt_user_for_letters(LIVES, category, phrase, hidden_phrase):
    win = False
    while LIVES > 0:
        while True:
            print(f"Category: {category:<8} Lives: {LIVES:<4} Used letters: {used_letters}\n")
            print_hidden_phrase(hidden_phrase)
            print(f"\n{HANGMAN_STAGES[LIVES]}\n")
            try:
                letter = input("Enter a letter > ").upper()

                if not letter.isalpha():
                    raise ValueError(f"input has to be a letter")
                elif letter in used_letters:
                    raise ValueError(f"'{letter}' has already been used, enter a different letter")
                elif letter in phrase:
                    indices = [i for i, ch in enumerate(phrase) if ch == letter]
                    for i in indices:
                        hidden_phrase[i] = letter
                    break
                elif letter not in phrase:
                    LIVES -= 1
                    break

            except ValueError as error:
                print(error)

        used_letters.append(letter)

        if "_" not in hidden_phrase:
            win = True
            break

    print(f"\n{HANGMAN_STAGES[LIVES]}\n")

    if win:
        print(f"You win! The word was {phrase}")
    else:
        print(f"You lose! The word was {phrase}")


def print_hidden_phrase(hidden_phrase):
    print(" ".join(hidden_phrase))


def choose_random_word():
    with open("words.json") as fh:
        j_obj = json.load(fh)

    category = random.choice(list(j_obj.keys()))
    phrase = random.choice(j_obj[category]).upper()

    return category, phrase


if __name__ == "__main__":
    main()

    while True:
        play_again = input("Play again, (y)es or (n)o? > ")
        if play_again == "y":
            main()
        elif play_again == "n":
            break

    print("Goobye!")