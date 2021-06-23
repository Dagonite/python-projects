"A game of Hangman. Select a difficulty then try to win as many rounds as possible without losing all of your lives."
# pylint: disable=anomalous-backslash-in-string

import json
import random
import csv
import datetime

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
BASE_LIVES = len(HANGMAN_STAGES) - 1
DIFFICULTIES = {
    "e": BASE_LIVES,
    "m": BASE_LIVES - 1,
    "h": BASE_LIVES - 2,
    "i": BASE_LIVES - 3,
    "q": 0,
}
used_letters = []


def main():
    starting_lives, difficulty = select_difficulty()
    lives = starting_lives

    total_score = 0
    score_mult = 500 - starting_lives * 40

    rounds = 0
    while lives:
        category, phrase = choose_random_word()
        hidden_phrase = ["_"] * len(phrase)

        for i, ch in enumerate(phrase):
            if ch in (" ", "'", "-", ":"):
                hidden_phrase[i] = ch

        lives, score = prompt_user_for_letters(starting_lives, category, phrase, hidden_phrase)
        total_score += score * score_mult
        rounds += 1

    total_score = f"{total_score:.2f}"
    print(f"\nYour score is {total_score}\nGoobye!")

    if rounds:
        write_to_csv(total_score, rounds, difficulty, datetime.datetime.now().date())


def select_difficulty():
    difficulty = ""
    while difficulty not in DIFFICULTIES.keys():
        difficulty = input("\nEnter a difficulty or (q)uit:\n(e)asy, (m)edium, (h)ard, or (i)mpossible: > ")

    return DIFFICULTIES[difficulty], difficulty


def prompt_user_for_letters(lives, category, phrase, hidden_phrase):
    starting_lives = lives
    note = ""
    while lives > 0:
        while True:
            display_hangman(category, hidden_phrase, lives, note)
            try:
                letter = input("Enter a letter: > ").upper()

                if not letter.isalpha():
                    raise ValueError(f"input has to be a letter")
                elif len(letter) > 1:
                    raise ValueError(f"input has to be only one letter")
                elif letter in used_letters:
                    raise ValueError(f"'{letter}' has already been used")
                elif letter in phrase:
                    note = f"{letter} is in the phrase"
                    indices = [i for i, ch in enumerate(phrase) if ch == letter]
                    for i in indices:
                        hidden_phrase[i] = letter
                    break
                elif letter not in phrase:
                    note = f"{letter} is NOT in the phrase"
                    lives -= 1
                    break

            except ValueError as error:
                note = error

        used_letters.append(letter)
        used_letters.sort()

        if "_" not in hidden_phrase:
            break

    display_hangman(category, hidden_phrase, lives, note)

    score = lives / starting_lives

    if lives:
        print(f"\nYou win! The word was {phrase}\n")
        option = ""
        while option not in ("c", "q"):
            option = input("Enter an option, (c)ontinue or (q)uit: > ")
        if option == "q":
            lives = 0
    else:
        print(f"\nYou lose! The word was {phrase}")

    used_letters.clear()

    return lives, score


def display_hangman(category, hidden_phrase, LIVES, note=""):
    print(f"\nCategory: {category}   Lives: {LIVES}   Used letters: {used_letters}   Note: {note}\n")
    print(" ".join(hidden_phrase))
    print(f"{HANGMAN_STAGES[LIVES]}\n")


def choose_random_word():
    with open("words.json") as fh:
        j_obj = json.load(fh)

    category = random.choice(list(j_obj.keys()))
    phrase = random.choice(j_obj[category]).upper()

    return category, phrase


def write_to_csv(*data, path="scores.csv"):
    with open(path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(data)


if __name__ == "__main__":
    main()
