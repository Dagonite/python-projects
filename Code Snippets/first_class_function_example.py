########################################################################################
# first_class_function_example.py
#
# A programming language is said to have first-class functions if it treats functions as
# first-class citizens.
#
# A first-class citizen (also type, object, entity, or value) in a given programming
# language is an entity which supports all the operations generally available to other
# entities. These operations typically include being passed as an argument, returned
# from a function, modified, and assigned to a variable.
########################################################################################


def square(x):
    return x * x


f = square

print(square)
print(f)
print(f(5))