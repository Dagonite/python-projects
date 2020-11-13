puzzle1 = [
    [0, 0, 0, 0, 0, 0, 8, 0, 0],
    [1, 2, 0, 0, 0, 4, 0, 0, 0],
    [5, 7, 0, 0, 0, 6, 0, 3, 0],
    [6, 0, 0, 2, 0, 9, 0, 0, 8],
    [0, 0, 0, 0, 0, 3, 6, 0, 5],
    [7, 0, 0, 6, 0, 8, 0, 0, 1],
    [9, 4, 0, 0, 0, 2, 0, 1, 0],
    [2, 3, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
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
    [0, 6, 0, 9, 5, 0, 0, 8, 0]
]


def solve(puzzle):
    """
    Solves the Sudoku using backtracking.
    :param puzzle: 2d list of ints
    :return: solved puzzle
    """
    current_coords = find_empty_coords(puzzle)    # co-ords of empty square
    if current_coords:
        row, col = current_coords     # co-ords stored as row, col
    else:
        return True     # return when no empty squares are found

    for n in range(1, 10):
        if valid(puzzle, row, col, n):    # check if n is valid for empty square
            puzzle[row][col] = n        # insert n into the square

            if solve(puzzle):       # solve is recursively called until n is incompatible or the puzzle is solved
                return True

            puzzle[row][col] = 0    # puzzle isn't solved so current n must be wrong

    return False


def find_empty_coords(puzzle):
    """
    Finds the next empty square in the puzzle (indicated by a 0).
    :param puzzle: 2d list of ints
    :return x, y: row (int), col (int)
    """
    for y in range(9):      # searches all the rows from top to bottom
        for x in range(9):
            if puzzle[y][x] == 0:
                return y, x      # returns co-ordinates of the empty square

    return False        # there are no empty squares (puzzle solved)


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
            return False        # n exists in column y

    for x in range(9):
        if puzzle[row][x] == n:
            return False        # n exists in row x

    # finds what 3x3 box the square is in: (0, 1, 2) by (0, 1, 2)
    box_row = row // 3
    box_col = col // 3

    for y in range(0, 3):
        for x in range(0, 3):
            if puzzle[box_row*3+y][box_col*3+x] == n:
                return False        # n exists in box (y, x)

    return True     # n valid if not found in its row, column, or box


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


print_formatted(puzzle2)
print("_____________________\n")
solve(puzzle2)
print_formatted(puzzle2)
