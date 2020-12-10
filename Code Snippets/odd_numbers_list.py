# odd_numbers_list.py
# List all odd numbers between 1 and 100 using list comprehension

list_of_numbers = range(1, 101)
print([n for n in list_of_numbers if n % 2])