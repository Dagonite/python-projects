# using_lists.py

def add_employee(emp, emp_list=None):
    if emp_list is None:
        emp_list = []
    emp_list.append(emp)
    print(emp_list)

emps = ["Alex", "John", "Seb"]

add_employee("Maria", emps)
add_employee("Nathan")
