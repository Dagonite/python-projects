# noughts_and_crosses.py
"""A game of Noughts and Crosses."""

from random import choice, randint, shuffle
from time import sleep
from itertools import combinations

# constants
SYMBOLS = {"O": "Noughts", "X": "Crosses"}
MAGIC_SQUARE = [6, 7, 2, 1, 5, 9, 8, 3, 4]


def main():
    while True:
        # generate starting grid
        squares = [["•" for _ in range(3)] for _ in range(3)]

        # track player squares
        human_squares = []
        computer_squares = []

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
            [computer_input, human_input],
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
            for player, player_input, player_squares, player_symbol in players_data:
                # simulate wait time for computer to make move
                if player is "Computer":
                    sleep(1.5)

                # prompt player for a move then draw the updated grid
                player_input(squares, player_squares, player_symbol)
                draw_grid(squares)

                # a win can be determined using magic square where all 3-number lines add up to 15
                if 15 in is_game_over(player_squares):
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
            try:
                ans = input("Play again (y)es or (n)o? > ")[0]
            except:
                pass
        if ans == "n":
            print("Goodbye!")
            break


def is_game_over(player_squares):
    player_values = [MAGIC_SQUARE[i - 1] for i in player_squares]
    value_combos = list(combinations(player_values, 3))
    return list(map(sum, value_combos))


def draw_grid(squares):
    for row in squares:
        print(*row)
    print()


def human_input(squares, human_squares, human_symbol):
    available_squares = tuple(find_available_squares(squares))
    ans = ""
    while ans not in available_squares:
        try:
            ans = int(input(f"Choose a square {available_squares}: > "))
        except:
            pass
    row, col = find_square_pos(ans)
    squares[row][col] = human_symbol
    human_squares.append(ans)
    print()


def computer_input(squares, computer_squares, computer_symbol):
    ans = choice(find_available_squares(squares))
    print(f"The computer has chosen square {ans}")
    row, col = find_square_pos(ans)
    squares[row][col] = computer_symbol
    computer_squares.append(ans)
    print()


def find_available_squares(squares):
    return [i * 3 + j + 1 for i, row in enumerate(squares) for j, item in enumerate(row) if item == "•"]


def find_square_pos(num):
    return (num - 1) // 3, num % 3 - 1


if __name__ == "__main__":
    main()
