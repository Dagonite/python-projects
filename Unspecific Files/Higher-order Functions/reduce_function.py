########################################################################################
# reduce_function.py
#
# The reduce() function applies the function to the first two elements of the list, then
# on the result and the next item, and so on. In this example, reduce takes a function
# and a list, sums the elements to give a new list.
########################################################################################

from functools import reduce

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum_of_numbers = reduce(lambda x, y: x + y, number_list)

print(sum_of_numbers)