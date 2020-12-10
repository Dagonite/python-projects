########################################################################################
# elements_in_a_list.py
#
# Program demonstrating that the first 2d list `grid1` results in a row amount of
# references to the same element. The second 2d list `grid2` has unique references for
# each element in the list. The second list is usually the desired result.
########################################################################################

from numpy import array


cols, rows = 3, 6
grid1 = [[0] * cols] * rows
grid1[2][0] = 5
grid1 = array(grid1)
print(grid1)

print()

grid2 = [[0] * cols for _ in range(rows)]
grid2[2][0] = 5
grid2 = array(grid2)
print(grid2)
