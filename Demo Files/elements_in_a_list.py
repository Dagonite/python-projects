################################################################################
# elements_in_a_list.py
#
# Program that shows that the following list alteration results in a row amount
# of references to the same list
################################################################################


from numpy import array


cols, rows = 3, 6

grid = [[0] * cols] * rows

grid[2][0] = 5

grid = array(grid)

print(grid)
