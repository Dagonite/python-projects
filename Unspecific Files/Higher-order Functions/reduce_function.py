########################################################################################
# reduce_function.py
#
# The reduce() function applies the function to the first two elements of the list, then
# on the result and the next item, and so on. In this example, reduce takes a function
# and a list, and gives the sum of the elements.
########################################################################################

from functools import reduce

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_of_numbers = reduce(lambda x, y: x + y, number_list)
print(sum_of_numbers)

# a third argument can be passed that gives a “starting” value
sum_of_numbers = reduce(lambda x, y: x + y, number_list, 5)
print(sum_of_numbers)