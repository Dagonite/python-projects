################################################################################
# single_line_vs_separate_lines.py
#
# Quite often it is important that expressions are evaluated before being
# assigned to variables. This can be seen when trying to code the Fibonacci
# sequence.
################################################################################

def separate_lines():
    a, b = 0, 1
    while a < 17:
        print(a)
        a = b
        b = a+b


def single_line():
    a, b = 0, 1
    while a < 17:
        print(a)
        a, b = b, a+b


separate_lines()
print()
single_line()
