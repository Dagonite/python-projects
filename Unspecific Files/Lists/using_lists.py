########################################################################################
# using_lists.py
#
# Demonstrates how to optionally provide a list as an argument and how to create an
# empty list within the function if no list is provided. Putting emp_list=[] as the
# parameter would not have the desired affect as lists are mutable. So function calls to
# add_employee would append names to the same list each time.
########################################################################################


def add_employee(emp, emp_list=None):
    if emp_list is None:
        emp_list = []
    emp_list.append(emp)
    print(emp_list)


emps = ["Alex", "John", "Seb"]

add_employee("Maria", emps)
add_employee("Nathan")
