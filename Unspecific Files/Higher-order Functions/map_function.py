########################################################################################
# map_function.py
#
# The map() function executes a specified function for each item in an iterable. In this
# example, map takes a function and a list, multiplies items in the list by 10 to give a
# new list.
########################################################################################

number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_times_ten = map(lambda x: x * 10, number_list)

for n in numbers_times_ten:
    print(n)
