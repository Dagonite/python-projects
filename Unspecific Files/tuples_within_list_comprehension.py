# tuples_within_list_comprehension.py

students = [
    ("Sam", 67),
    ("Kate", 35),
    ("Jill", 75),
    ("Fred", 45),
    ("Alice", 50),
    ("Bob", 38),
]


def passed(students):
    return [name for (name, mark) in students if mark >= 40]


print(passed(students))


# imperative version
def passed_imperative(students):
    names = []
    for (name, mark) in students:
        if mark >= 40:
            names.append(name)
    return names


print(passed_imperative(students))