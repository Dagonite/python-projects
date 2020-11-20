################################################################################
# map_function.py
#
# Python includes (like Haskell) anonymous functions called lambda expressions.
# The map function takes a function and a list, and gives a new list.
################################################################################

number_list = [0, 1, 2, 3, 4, 5, 6, 7, 9]

numbers_times_ten = map(lambda x: x * 10, number_list)

for n in numbers_times_ten:
    print(n)
