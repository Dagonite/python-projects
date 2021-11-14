"""Graphical representation of the hangman."""
# pylint: disable=anomalous-backslash-in-string

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

if __name__ == "__main__":
    print(len(HANGMAN_STAGES))
