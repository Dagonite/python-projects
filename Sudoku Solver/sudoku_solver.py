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
    :param puzzle: 2d array of ints
    :return: solved puzzle
    """
    current_coords = find_empty_coords(puzzle)    # fetches the co-ords of an empty square in the puzzle
    if current_coords:
        row, col = current_coords     # stores the co-ords of the empty square as row, col
    else:
        return True     # return when no empty squares are found

    for n in range(1, 10):
        if valid(puzzle, row, col, n):    # check if an int is valid for current empty square
            puzzle[row][col] = n        # insert n into the array

            if solve(puzzle):       # solve is recursively called until n is incompatible or the puzzle is solved
                return True

            puzzle[row][col] = 0    # if incompatible, n is removed from the current co-ords

    return False


def find_empty_coords(puzzle):
    """
    Finds the next empty square in the puzzle (indicated by a 0).
    :param puzzle: 2d array of ints
    :return x, y: row (int), col (int)
    """
    for y in range(9):      # searches the first row
        for x in range(9):
            if puzzle[y][x] == 0:   # finds the first empty column in the first row, otherwise moves to the next row
                return y, x      # returns co-ordinates of the empty square

    return False        # there are no empty squares


def valid(puzzle, row, col, n):
    """
    Returns if n is a valid number.
    :param puzzle: 2d array of ints
    :param row: square's y co-ord
    :param col: square's x co-ord
    :param n: current int being tried
    :return: bool
    """
    # checks if n exists in the current column
    for y in range(9):  # starts from the first row (0, col)
        if puzzle[y][col] == n:    # not valid if n already exists in the column
            return False

    # checks if n exists in the current row
    for x in range(9):  # starts from the first column (row, 0)
        if puzzle[row][x] == n:    # not valid if n already exists in the row
            return False

    # determines which 3x3 box the empty square is in
    # starts from box (0, 0) and ends at box (2, 2)
    box_row = row // 3
    box_col = col // 3

    for y in range(0, 3):
        for x in range(0, 3):
            if puzzle[box_row*3+y][box_col*3+x] == n:   # not valid if n is already in the box
                return False

    return True     # n is valid if not found in same row, column, or box


def print_formatted(puzzle):
    """
    Prints the puzzle into a readable format.
    :param puzzle: 2d array of ints
    :return: None
    """
    for y in range(9):
        if y % 3 == 0 and y != 0:
            print("- - - - - - - - - - - ")

        for x in range(9):
            current_value = str(puzzle[y][x]).replace("0", " ")  # holds the int of the current co-ord
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
