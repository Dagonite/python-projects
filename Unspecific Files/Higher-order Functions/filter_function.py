########################################################################################
# filter_function.py
#
# The filter() function returns an iterator were the items are filtered through a
# function to test if the item is accepted or not. In this example, filter takes a
# function and a list, filters even numbers using the modulus operator to give a new
# list.
########################################################################################

number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers = filter(lambda x: x % 2 == 0, number_list)

for n in even_numbers:
    print(n)