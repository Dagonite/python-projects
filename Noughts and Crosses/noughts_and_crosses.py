"""A game of Noughts and Crosses."""

from random import choice, randint, shuffle
from time import sleep
from itertools import combinations

# constants
SYMBOLS = {"O": "Noughts", "X": "Crosses"}
MAGIC_SQUARE = [6, 7, 2, 1, 5, 9, 8, 3, 4]
MAGIC_VALUE = 15
human_squares = []
computer_squares = []


def main():
    while True:
        # generate starting grid
        squares = [[" " for _ in range(3)] for _ in range(3)]

        # give computer and human a random symbol
        symbol_keys = list(SYMBOLS.keys())
        shuffle(symbol_keys)
        human_symbol = symbol_keys.pop()
        computer_symbol = symbol_keys[0]

        # determine if human will go first or second
        turns = ["first", "second"]
        shuffle(turns)
        human_turn = turns.pop()

        print(f"\nYou are playing as {SYMBOLS[human_symbol]}. You will go {human_turn}\n")

        players_data = [
            ["Computer", "Human"],
            [computer_squares, human_squares],
            [computer_symbol, human_symbol],
        ]

        # reverse element order if human has the first turn
        if human_turn == "first":
            players_data = [data[::-1] for data in players_data]

        # zip data for both computer and human
        players_data = list(zip(*players_data))

        # draw initial empty grid
        draw_grid(squares)

        # main gameplay loop
        drawn = False
        gameover = False
        while not drawn and not gameover:
            for player, player_squares, player_symbol in players_data:
                # simulate wait time for computer to make move
                if player is "Computer":
                    sleep(1.5)

                # prompt player for a move then draw the updated grid
                player_input(squares, player_squares, player_symbol, player)
                draw_grid(squares)

                # a win can be determined using a magic square where all lines add up to 15
                if MAGIC_VALUE in player_sums(player_squares):
                    print(f"{player} wins with {SYMBOLS[player_symbol]}")
                    gameover = True
                    sleep(3)
                    break

                # check if it is a drawn game
                if len(find_available_squares(squares)) == 0:
                    print("It's a draw")
                    drawn = True
                    sleep(3)
                    break

        human_squares.clear()
        computer_squares.clear()

        # ask human if they want to play again
        ans = ""
        while ans not in ("y", "n"):
            ans = input("Play again, (y)es or (n)o? > ")
        if ans == "n":
            print("Goodbye!")
            break


def draw_grid(squares):
    """Print the current grid layout."""
    print(f"{squares[0][0]}|{squares[0][1]}|{squares[0][2]}")
    print("-+-+-")
    print(f"{squares[1][0]}|{squares[1][1]}|{squares[1][2]}")
    print("-+-+-")
    print(f"{squares[2][0]}|{squares[2][1]}|{squares[2][2]}\n")


def player_input(squares, player_squares, player_symbol, player):
    """Prompt the player for a square to put their symbol in."""
    available_squares = tuple(find_available_squares(squares))
    ans = 0
    if player == "Computer":
        for i in available_squares:
            print(player_sums(player_squares + [i]))
            if MAGIC_VALUE in player_sums(player_squares + [i]):
                ans = i
                break
        if ans == 0:
            for i in available_squares:
                print(player_sums(player_squares + [i]))
                if MAGIC_VALUE in player_sums(human_squares + [i]):
                    ans = i
                    break
            else:
                ans = choice(available_squares)
        print(f"The computer has chosen square {ans}")
    elif player == "Human":
        while ans not in available_squares:
            try:
                ans = int(input(f"Choose a square {available_squares}: > "))
            except ValueError:
                print("Invalid: enter one of the shown numbers")

    make_move(squares, player_squares, player_symbol, ans)


def make_move(squares, player_squares, player_symbol, ans):
    """Modify the grid by inserting the player's symbol."""
    row, col = find_square_pos(ans)
    squares[row][col] = player_symbol
    player_squares.append(ans)
    print()


def find_available_squares(squares):
    """Rerturn a list of available squares in the grid."""
    return [i * 3 + j + 1 for i, row in enumerate(squares) for j, item in enumerate(row) if item == " "]


def find_square_pos(num):
    """Rerturn the (row, column) of the supplied square."""
    return (num - 1) // 3, num % 3 - 1


def player_sums(player_squares):
    """Return a list of sums generated using the magic values which correspond to the squares the supplied player has
    taken."""
    player_values = [MAGIC_SQUARE[i - 1] for i in player_squares]
    value_combos = list(combinations(player_values, 3))
    return list(map(sum, value_combos))


if __name__ == "__main__":
    main()
