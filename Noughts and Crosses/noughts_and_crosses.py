"""A game of Noughts and Crosses."""

import os
from copy import deepcopy
from itertools import combinations
from random import choice, shuffle
from time import sleep

# globals
MARKS = {"O": "Noughts", "X": "Crosses"}
GRID_SIZE = 3
MAGIC_VALUE = 15
MAGIC_SQUARE = [
    [6, 7, 2],
    [1, 5, 9],
    [8, 3, 4],
]


def main():
    """Entry point for the program."""
    # determine if player 2 is cpu or human
    player2_is_cpu = cpu_or_human()
    play_game(player2_is_cpu)


def cpu_or_human():
    """Ask user if they want to play against another player of the computer."""
    ans = ""
    while ans not in ("y", "n"):
        ans = input("Do you want to play against another human, y/n? > ")
    return ans == "n"


def play_game(player2_is_cpu):
    """Play a game of Noughts and Crosses."""
    while True:
        # generate starting grid
        squares = [[" " for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

        # give player 1 and 2 random marks
        mark_keys = list(MARKS.keys())
        shuffle(mark_keys)
        player1_mark = mark_keys.pop()
        player2_mark = mark_keys.pop()

        # determine who will go first
        turns = ["first", "second"]
        shuffle(turns)
        player1_turn = turns.pop()
        player2_turn = turns.pop()

        # container for some player specific data
        data = [
            ["player 1", "computer" if player2_is_cpu else "player 2"],
            [player1_mark, player2_mark],
        ]

        # reverse the data if player 1 is going second
        if player1_turn == "second":
            data = [data[::-1] for data in data]

        # zip the data so the columns can be iterated over
        data = list(zip(*data))

        if player2_is_cpu:
            print(f"\nYou are playing as {MARKS[player1_mark]} - you will go {player1_turn}\n")
        else:
            print(f"\nPlayer 1 has {MARKS[player1_mark]} - they will go {player1_turn}")
            print(f"Player 2 has {MARKS[player2_mark]} - they will go {player2_turn}\n")

        input("Press Enter to continue... ")
        print_grid(squares)

        # main gameplay loop
        drawn = False
        gameover = False
        while not drawn and not gameover:
            for player, player_mark in data:
                # determine whether to prompt cpu or human for a move
                if player == "computer":
                    print(f"The computer is thinking...")
                    prompt_cpu_for_move(squares, player_mark, player1_mark)
                else:
                    prompt_player_for_move(squares, player, player_mark)

                print_grid(squares)

                # check if the current player has won
                player_has_won = check_for_win(squares, player_mark)
                if player_has_won:
                    print(f"{player.title()} wins with {MARKS[player_mark]}")
                    gameover = True
                    break

                # check if it is a drawn game
                if len(get_available_squares(squares)) == 0:
                    print("It's a draw")
                    drawn = True
                    break

        sleep(1.5)
        print()

        # prompt user if they want to play again
        ans = ""
        while ans not in ("y", "n"):
            ans = input("Play again, y/n? > ")
        if ans == "n":
            print("\nGoodbye!")
            break


def prompt_cpu_for_move(squares, cpu_mark, player_mark):
    """Prompt computer for a square to put their mark in."""
    # generate list of available moves for the cpu
    available_squares = get_available_squares(squares)

    # create a copy of the grid
    tmp_squares = deepcopy(squares)

    sleep(1.5)

    # cpu looks for a winning move first
    ans = 0
    for square in available_squares:
        row, col = get_square_pos(square)
        tmp_squares[row][col] = cpu_mark

        if check_for_win(tmp_squares, cpu_mark):
            ans = square
            break

        tmp_squares[row][col] = " "

    # cpu looks for a blocking move second
    if ans == 0:
        for square in available_squares:
            row, col = get_square_pos(square)
            tmp_squares[row][col] = player_mark
            if check_for_win(tmp_squares, player_mark):
                ans = square
                break

            tmp_squares[row][col] = " "
        else:
            # otherwise goes for a random move
            ans = choice(available_squares)

    make_move(squares, cpu_mark, ans)


def prompt_player_for_move(squares, player, player_mark):
    """Prompt player for a square to put their mark in."""
    available_squares = tuple(get_available_squares(squares))
    ans = 0

    while ans not in available_squares:
        try:
            ans = int(input(f"{player.title()} choose a square {available_squares}: > "))
        except ValueError:
            print("Invalid: enter one of the shown numbers")

    make_move(squares, player_mark, ans)


def make_move(squares, player_mark, ans):
    """Modify the grid by inserting the player's symbol."""
    row, col = get_square_pos(ans)
    squares[row][col] = player_mark
    print()


def print_grid(squares):
    """Print the current grid."""
    os.system("cls" if os.name == "nt" else "clear")
    print("\n-+-+-\n".join("|".join(row) for row in squares) + "\n")


def get_available_squares(squares):
    """Return a list of available squares in the grid."""
    return [i * GRID_SIZE + j + 1 for i, row in enumerate(squares) for j, item in enumerate(row) if item == " "]


def get_square_pos(square):
    """Return the (row, column) of the supplied square."""
    return (square - 1) // GRID_SIZE, square % GRID_SIZE - 1


def check_for_win(squares, player_mark):
    """
    Return whether the MAGIC_VALUE is in the list of combinations which are
    generated using the magic square.
    """
    player_values = [
        MAGIC_SQUARE[i][j] for i, row in enumerate(squares) for j, square in enumerate(row) if square == player_mark
    ]
    value_combos = list(combinations(player_values, 3))
    return MAGIC_VALUE in list(map(sum, value_combos))


if __name__ == "__main__":
    main()
