################################################################################
# elements_in_a_list.py
#
# Program that shows that the first list results in a row amount of references
# to the same element. The second list has unique references for each element in
# the list
################################################################################

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
