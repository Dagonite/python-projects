"""Program which solves Sudoku puzzles using backtracking."""

from typing import Tuple, List


def main() -> None:
    """Program entry point."""
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
    print_formatted(puzzle)
    print("_____________________\n")
    solve(puzzle)
    print_formatted(puzzle)


def solve(puzzle: List) -> bool:
    """
    Call a helper function to find an empty puzzle square then recursively
    insert numbers into the puzzle until it is solved.

    Args:
        puzzle: A 2d list containing 81 ints.

    Returns:
        A bool indicating if the puzzle is solved.
    """
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


def find_empty_coords(puzzle: List) -> Tuple[int, int]:
    """
    Search the puzzle for the first empty square.

    Args:
        puzzle: A 2d list containing 81 ints.

    Returns:
        A tuple of ints indicating the (row, col) of an empty square. If no
        empty square is found, return (-1, -1), indicating that the puzzle is
        solved.
    """
    # searches co-ords from left-to-right, top-to-bottom
    for y in range(9):
        for x in range(9):
            if not puzzle[y][x]:
                return y, x  # co-ords of an empty square

    return -1, -1  # there are no empty squares (puzzle solved)


def valid(puzzle: List, row: int, col: int, n: int) -> bool:
    """
    Insert n into the puzzle at the supplied row and col then check if the
    puzzle is still valid.

    Args:
        puzzle: A 2d list containing 81 ints.
        row: An int for the outer index of the 2d puzzle list.
        col: An int for the inner index of the 2d puzzle list.
        n: The current int being inserted into the puzzle.

    Returns:
        A bool indicating if n is currently a valid value at the supplied (row,
        col) in the puzzle.
    """
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


def print_formatted(puzzle: List) -> None:
    """
    Print a formatted display of a supplied puzzle.

    Args:
        puzzle: A 2d list containing 81 ints.
    """
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
    main()
