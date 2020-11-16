import numpy as np
from random import random


'''
7. [Harder]
Write a two-dimensional version tracedwalk2d.py of tracedwalk.py. This should
simulate a single random walk of the form considered in pract08, where the walker
begins in the central square of a square two dimensional grid of dimensions 9 by
9 steps, and where the walk ends when the walker steps off the grid. Output the
results in tabular form. (Hint: you may need to use nested (two dimensional) lists.)
'''
# grid = [[0] * cols] * rows    # this makes a list with col times references
                                # to the same list, grid[2][0] = 5 would make
                                # all values in the first column 5

def simulate_steps(cols, rows):
    grid = [[0] * cols for _ in range(rows)]
    current_col = int(cols / 2)
    current_row = int(rows / 2)

    while True:
        random_step = random()
        if random_step < .25:
            current_row -= 1    # go up
        elif random_step >= .25 and random_step < .5:
            current_col += 1    # go right
        elif random_step >= .5 and random_step < .75:
            current_row += 1    # go down
        else:
            current_col -= 1    # go left
        if current_row == -1 or current_row == rows \
        or current_col == -1 or current_col == cols:
            break

        grid[current_row][current_col] += 1

    # this might come in helpful later on
    # for i in range(rows):
    #     grid[i] = [" " if j == 0 else j for j in grid[i]]

    grid = np.array(grid)
    print(grid)


simulate_steps(9, 9)
