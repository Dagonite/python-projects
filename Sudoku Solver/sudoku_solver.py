"""Program which solves Sudoku puzzles using backtracking."""

from typing import Union, Tuple, List


def main(puzzle: list) -> None:
    print_formatted(puzzle)
    print("_____________________\n")
    solve(puzzle)
    print_formatted(puzzle)


def solve(puzzle: list) -> bool:
    # co-ords of empty square unless puzzle solved
    current_coords = find_empty_coords(puzzle)

    # co-ords stored as row, col if current_coords is truthy
    if current_coords != (-1, -1):
        row, col = current_coords
    else:
        return True

    for n in range(1, 10):
        # check if n is valid for empty square
        if valid(puzzle, row, col, n):
            puzzle[row][col] = n

            # solve recursively called until n is incompatible or puzzle solved
            if solve(puzzle):
                return True

            # puzzle isn't solved so current n must be wrong
            puzzle[row][col] = 0
    return False


def find_empty_coords(puzzle: list) -> Tuple[int, int]:
    # searches co-ords from left-to-right, top-to-bottom
    for y in range(9):
        for x in range(9):
            if not puzzle[y][x]:
                return y, x  # co-ords of an empty square

    return -1, -1  # there are no empty squares (puzzle solved)


def valid(puzzle: list, row: int, col: int, n: int) -> bool:
    for y in range(9):
        if puzzle[y][col] == n:
            return False  # n exists in row y and column col

    for x in range(9):
        if puzzle[row][x] == n:
            return False  # n exists in row row and column x

    # determines the 3x3 box the square is in
    box_row = row // 3
    box_col = col // 3

    for y in range(3):
        for x in range(3):
            if puzzle[box_row * 3 + y][box_col * 3 + x] == n:
                return False  # n exists in box y, x

    return True  # valid if another n not found in same row, column, or box


def print_formatted(puzzle: list) -> None:
    for y in range(9):
        if not y % 3 and y:
            print("- - - - - - - - - - - ")

        for x in range(9):
            current_square = str(puzzle[y][x]).replace("0", "·")
            if not x % 3 and x:
                print("| ", end="")
            if x == 8:
                print(current_square)
            else:
                print(current_square + " ", end="")


if __name__ == "__main__":
    puzzle: List[List[int]] = [
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [1, 2, 0, 0, 0, 4, 0, 0, 0],
        [5, 7, 0, 0, 0, 6, 0, 3, 0],
        [6, 0, 0, 2, 0, 9, 0, 0, 8],
        [0, 0, 0, 0, 0, 3, 6, 0, 5],
        [7, 0, 0, 6, 0, 8, 0, 0, 1],
        [9, 4, 0, 0, 0, 2, 0, 1, 0],
        [2, 3, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
    ]

    main(puzzle)
