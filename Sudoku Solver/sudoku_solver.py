########################################################################################
# sudoku_solver.py
#
# Program which solves Sudoku puzzles using backtracking.
########################################################################################

puzzle1 = [
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

puzzle2 = [
    [0, 0, 0, 0, 0, 0, 4, 6, 0],
    [0, 0, 0, 0, 9, 4, 3, 0, 7],
    [0, 0, 0, 7, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 8, 3, 0, 0, 9],
    [0, 5, 0, 2, 0, 0, 0, 3, 1],
    [0, 8, 0, 4, 0, 5, 0, 0, 0],
    [7, 9, 0, 0, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 4, 0, 0, 0, 3],
    [0, 6, 0, 9, 5, 0, 0, 8, 0],
]


def solve(puzzle):
    """
    Solves the Sudoku puzzle through backtracking.
    :param puzzle: 2d list of ints
    :return: solved puzzle
    """
    current_coords = find_empty_coords(puzzle)  # co-ords of empty square
    if current_coords:
        row, col = current_coords  # co-ords stored as row, col
    else:
        return True  # no empty squares are found (puzzle solved)

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


def find_empty_coords(puzzle):
    """
    Finds the next empty square in the puzzle (indicated by a 0).
    :param puzzle: 2d list of ints
    :return x, y: row (int), col (int)
    """
    # searches co-ords from left-to-right, top-to-bottom
    for y in range(9):
        for x in range(9):
            if puzzle[y][x] == 0:
                return y, x  # co-ords of an empty square

    return False  # there are no empty squares (puzzle solved)


def valid(puzzle, row, col, n):
    """
    Returns if n is a valid number.
    :param puzzle: 2d list of ints
    :param row: square's y co-ord
    :param col: square's x co-ord
    :param n: current int being tried
    :return: bool
    """
    for y in range(9):
        if puzzle[y][col] == n:
            return False  # n exists in row (y) and column (col)

    for x in range(9):
        if puzzle[row][x] == n:
            return False  # n exists in row (row) and col (x)

    # determines the 3x3 box the square is in: (0, 1, 2) by (0, 1, 2)
    box_row = row // 3
    box_col = col // 3

    for y in range(0, 3):
        for x in range(0, 3):
            if puzzle[box_row * 3 + y][box_col * 3 + x] == n:
                return False  # n exists in box (y, x)

    return True  # valid if another n not found in same row, column, or box


def print_formatted(puzzle):
    """
    Prints the puzzle in a readable format.
    :param puzzle: 2d list of ints
    :return: None
    """
    for y in range(9):
        if y % 3 == 0 and y != 0:
            print("- - - - - - - - - - - ")

        for x in range(9):
            current_value = str(puzzle[y][x]).replace("0", " ")
            if x % 3 == 0 and x != 0:
                print("| ", end="")
            if x == 8:
                print(current_value)
            else:
                print(current_value + " ", end="")


print_formatted(puzzle1)
print("_____________________\n")
solve(puzzle1)
print_formatted(puzzle1)
